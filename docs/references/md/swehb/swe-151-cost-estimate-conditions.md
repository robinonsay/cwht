# SWE-151 - Cost Estimate Conditions

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695507. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions

SWE-151 - Cost Estimate Conditions

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695507)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695507&showCommentArea=true&showComments=true#addcomment)

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

3.2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions: 

a. Covers the entire software life cycle.  
b. Is based on selected project attributes (e.g., programmatic assumptions/constraints, assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products).  
c. Is based on the cost implications of the technology to be used and the required maturation of that technology.  
d. Incorporates risk and uncertainty, including end state risk and threat assessments for cybersecurity.  
e. Includes the cost of the required software assurance support.  
f. Includes other direct costs.

## 1.1 Notes

In the event of a decision to outsource, it is a best practice that both the acquirer (NASA) and the provider (contractor/subcontractor) be responsible for developing software cost estimates. For any class of software that has significant risk exposure, consider performing at least two cost estimates.

## 1.2 History

Click here to view the history of this requirement: SWE-151 History

SWE-151 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW - Split from Rev A SWE-015 and added items d-f. |
| B | 3.2.2 The project manager‘s software cost estimate(s) shall satisfy the following conditions:   1. 1. Covers the entire software life cycle.    2. Is based on selected project attributes (e.g., assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products).    3. Is based on the cost implications of the technology to be used and the required maturation of that technology.    4. Incorporates risk and uncertainty.    5. Includes the cost for software assurance support.    6. Includes other direct costs. |
| Difference between B and C | To item d., added cybersecurity;  To item e., made SA support required by adding "of the required". |
| C | 3..2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions:   1. 1. Covers the entire software life cycle.    2. Is based on selected project attributes (e.g., assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products).    3. Is based on the cost implications of the technology to be used and the required maturation of that technology.    4. Incorporates risk and uncertainty, including cybersecurity.    5. Includes the cost of the required software assurance support.    6. Includes other direct costs. |
| Difference between C and D | Updated item b. to include programmatic assumptions/constraints and clarified item d. |
| D | 3.2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions:   a. Covers the entire software life cycle. b. Is based on selected project attributes (e.g., programmatic assumptions/constraints, assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products). c. Is based on the cost implications of the technology to be used and the required maturation of that technology. d. Incorporates risk and uncertainty, including end state risk and threat assessments for cybersecurity. e. Includes the cost of the required software assurance support. f. Includes other direct costs. |

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

Credible software cost estimates are a **critical component** of project and software lifecycle management, as outlined in *NPR 7150.2, NASA Software Engineering Requirements, Chapter 3*. These estimates provide the foundation for effective planning, budgeting, and resource allocation, ensuring projects have the necessary tools and support to meet mission goals. NASA policy mandates that software cost estimates adhere to specific standards and exhibit defined characteristics to ensure credibility, accuracy, and traceability.

Credible cost estimates instill **confidence among programs and projects** by reliably representing the scope, effort, and risks associated with the work to be performed. When crafted using rigorous methodologies and clear assumptions, cost estimates allow for informed decision-making, alignment of stakeholder expectations, and proactive management of both financial and technical risks. Furthermore, credible estimates ensure compliance with NASA policies, facilitate audits and reviews, and help avert common issues such as budget shortfalls, schedule delays, and resource misallocation.

Ultimately, credible software cost estimates enable NASA projects to maintain accountability, optimize resources, and achieve mission success without unnecessary disruption or inefficiencies.

### a. Covers the Entire Software Life Cycle

#### **Rationale:**

* Software development costs extend well beyond the initial coding and implementation phases. The software life cycle includes requirements analysis, design, implementation, testing, integration, deployment, maintenance, and eventual decommissioning.
* Omitting lifecycle costs (e.g., maintenance updates, bug fixes, post-deployment support, and retirement plans) can lead to significant underestimation of the total cost of ownership.
* By requiring the cost estimate to encompass the full lifecycle, the organization ensures better financial and resource planning to sustain the software for its operational duration.

### b. Is Based on Selected Project Attributes

#### **Rationale:**

* Software costs are driven by multiple factors such as size, functionality, complexity, and criticality, as well as the extent of code reuse or modification. These project-specific attributes significantly influence effort requirements.
* For example:
  + Larger codebases typically require more effort for development and testing.
  + High-complexity or mission-critical systems (e.g., flight control software) demand greater attention to quality assurance and risk mitigation.
  + Reused or modified code reduces development costs but often comes with hidden costs, such as integrating, refactoring, or documenting legacy code.
* Basing cost estimates on these attributes ensures the estimate is tailored to the unique characteristics of the project, improving its accuracy and reliability.

### c. Is Based on the Cost Implications of the Technology to Be Used and the Required Maturation of that Technology

#### **Rationale:**

* The technology selected for a project directly affects development costs. For example:
  + Cutting-edge tools or languages may promise efficiencies but require significant up-front investment in training or expertise.
  + Immature or experimental technologies may necessitate additional research, prototyping, and validation efforts.
* Cost estimates must account for considerations such as the need to mature specific technologies, integrate proprietary systems, or accommodate unexpected technical challenges. Failure to consider these costs can result in delays or cost overruns if the technology proves more difficult to implement than anticipated.

### d. Incorporates Risk and Uncertainty, Including End-State Risk and Threat Assessments for Cybersecurity

#### **Rationale:**

* Risk is an inherent part of every software project, particularly for space missions and critical systems where failure can have severe consequences. Software cost estimates must:
  + Account for risks such as schedule delays, scope creep, unforeseen technical challenges, and resource availability.
  + Include cybersecurity risk assessments, as software systems must be robust against evolving cyber threats, including vulnerabilities introduced during the development process.
* Incorporating risk and uncertainty ensures the estimate reflects the true range of potential costs and helps stakeholders plan for contingencies, making estimates more robust and realistic.

### e. Includes the Cost of the Required Software Assurance Support

#### **Rationale:**

* Software assurance activities, such as testing, verification, validation, and quality assurance, ensure that the software meets safety, functionality, and reliability requirements. These activities are especially critical for mission-critical and safety-critical systems.
* Neglecting to include software assurance costs in the estimate can result in significant budget shortfalls during critical phases of the development process.
* Including assurance costs ensures that adequate resources are allocated to testing and validation activities, which ultimately reduce the likelihood of costly system failures.

### f. Includes Other Direct Costs

#### **Rationale:**

* Direct costs include all identifiable costs associated with the development and delivery of the software, beyond salaries and development tools. Examples include:
  + Specialized hardware for simulation or testing.
  + Licensing fees for third-party software/components.
  + Compliance costs for audits, certifications, or adherence to safety regulations.
* Omitting these costs from the estimate can lead to inaccurate predictions, misallocated resources, and unexpected budget overruns during project execution.
* Ensuring all direct costs are incorporated into the estimate guarantees a comprehensive financial plan that addresses the full scope of project needs.

## Overall Justification For This Requirement

This requirement establishes expectations for producing **holistic, transparent, and traceable software cost estimates** that account for every facet of the project lifecycle, from development to post-deployment support. By adhering to these conditions, NASA and other stakeholders can better mitigate financial risks, improve planning accuracy, and reduce the likelihood of missed project goals due to underfunding or unforeseen costs.

Additionally, this requirement reflects NASA’s commitment to proper stewardship of public funds while ensuring the successful completion of ambitious and complex space missions. A well-documented and comprehensive estimation process builds confidence with stakeholders, enables informed decision-making, and ensures long-term software sustainability.

# 3. Guidance

Credible software cost estimates are essential for ensuring the successful planning, execution, and delivery of NASA software projects. These estimates must satisfy specific requirements to meet NASA policies and provide confidence to stakeholders. The software acquirer and software provider collaborate to create estimates that address all critical project factors. Below is enhanced guidance on preparing software cost estimates that meet these conditions.

By adhering to these guidelines, NASA project teams can produce credible software cost estimates that meet organizational standards, facilitate informed decision-making, and ensure resources are allocated appropriately for mission success. These practices enable projects to maintain accountability, minimize risk, and deliver high-quality software systems aligned with NASA's goals.

## 3.1 Life Cycle Coverage

#### **Guidance:**

A credible software cost estimate must encompass the entire software lifecycle, from concept and development to maintenance, support, and eventual retirement. This holistic approach allows project teams to account for all phases of software development, including:

* Design, implementation, testing, validation, and deployment.
* Maintenance costs, including updates, bug fixes, and patching.
* End-stage costs, such as decommissioning efforts, knowledge transfer, and final reporting.

Breaking out costs by lifecycle phase and activity is a recommended practice. This detailed view helps ensure that resources are allocated appropriately for each phase and enables adjustments as project assumptions or conditions evolve over time (e.g., changes in functionality, scope, or schedule). Regular updates to the cost estimate improve its accuracy and relevance.

## 3.2 Project Attributes

#### **Guidance:**

Cost estimates must account for key project attributes that directly influence the scope and effort required for software development. Examples include:

* **Size**: The anticipated lines of code or functional components.
* **Functionality**: The software's operational capabilities and requirements.
* **Complexity**: How challenging the development tasks are due to factors such as advanced algorithms, integration with hardware systems, or atypical mission scenarios.
* **Criticality**: The importance of the software to mission success or safety, which often requires additional assurance and quality measures.
* **Risk**: The level of uncertainty, including technical and schedule risks.
* **Reuse/Modification**: Effort associated with incorporating previously developed code, including costs for understanding, testing, and adapting reused components.
* **Documentation Requirements**: Effort required for developing project deliverables such as requirements, architecture, test plans, and design documents.

Attributes not only apply to the software itself but also to the processes used to create, verify, and maintain it, as well as the lifecycle products (e.g., testing procedures, operational manuals).

By fully accounting for these attributes, project teams ensure estimates are realistic and representative of the project's unique characteristics.

## 3.3 Technology Implications

#### **Guidance:**

NASA projects often require new or cutting-edge technologies to achieve mission objectives. These technologies can introduce unique cost drivers, such as research efforts, prototyping, validation, or adaptation to new software environments and tools. Consider the following:

* **Technology Costs**: Include the effort and expenses associated with deploying new software development environments or tools, such as setup, training, and support.
* **Technology Maturation**: Account for costs required to mature experimental or unproven technologies to operational readiness. This may include integration activities, additional testing, and risk mitigation efforts.
* **Cost-Saving Records**: Maintain documentation on any identified cost savings resulting from innovative technology use, ensuring the assumptions behind these savings are realistic and traceable.

Defining new technologies in the estimate includes identifying software tools, development platforms, and frameworks categorized as novel or unproven.

## 3.4 Risk and Uncertainty

#### **Guidance:**

In addition to quantifiable risks, software estimates must incorporate allowances for uncertainty caused by incomplete knowledge or unforeseen circumstances. Addressing both risk and uncertainty ensures that cost estimates remain robust under various operational conditions. Key aspects include:

* **Risk Assessment**: Identify common software risks, assess their cost impact, and include allowances for potential mitigation efforts.
  + Consider risks such as scope changes, unexpected integration challenges, resource availability, and cybersecurity vulnerabilities.
  + Account for the likelihood and timing of risks, their impact on cost and schedule, and mitigation costs.
* **Quantifying Uncertainty**: Recognize uncertainties tied to model inputs (e.g., sizing assumptions, productivity rates) and incorporate them into the estimate.
  + Tools such as risk matrices, expected cost-risk estimations, and Monte Carlo simulations can model cost distributions and provide a range of probable outcomes.
  + Use Monte Carlo methods with cost models to simulate random variations and produce a probability distribution for cost estimates, especially for high-risk projects.

## 3.5 End-State Risk and Threat Assessments for Cybersecurity

The cost estimate should account for cybersecurity risk assessment and management efforts throughout the software's lifecycle. Projects and programs must analyze the software product both during development and operational use. Cost considerations for cybersecurity include:

* Assessments and checks during development and testing to ensure system robustness against cyber threats.
* Monitoring software during operational use (e.g., command and memory monitoring during missions).
* Modifications to address emerging cybersecurity threats (e.g., applying patches or making changes to counter vulnerabilities).
* Updates for commercial-off-the-shelf (COTS) software integrated into the project.
* Long-term cybersecurity planning to address risks for end-stage situations where the software is in its final operational phase.

## 3.6 Software Assurance Support

#### **Guidance:**

Software assurance efforts, including tasks such as testing, verification, validation, and Independent Verification and Validation (IV&V), carry considerable costs. These activities are essential for ensuring the reliability, safety, and quality of mission-critical and safety-critical software.

Including software assurance costs in the estimate ensures:

* Full understanding of the assurance activities required for mission success.
* Appropriate allocation of resources to support these efforts.
* Risk reduction for potential mission failures caused by insufficient assurance funding.

Project teams should also assess the risks of reducing or limiting software assurance efforts due to constrained budgets and clearly communicate the consequences to stakeholders.

## 3.7 Other Costs

#### **Guidance:**

When preparing cost estimates, ensure that ancillary costs are included to account for additional factors influencing the budget. Examples include:

* **Equipment Procurement**: Costs for equipment such as workstations, testbeds, hardware simulators, or specialized tools necessary for development and testing.
* **Tool Procurement**: Costs for shared software tools like compilers, configuration management systems, and licenses.
* **Travel**: Expenses for travel related to reviews, customer interfaces, vendor site visits, or program collaboration.
* **Training**: Costs for training team members in new tools, workflows, or methodologies required for the project.

## 3.8 Best Practices for Developing Credible Estimates

* **Collaboration**: Foster continuous collaboration between the software acquirer and provider to align cost estimates with project needs and constraints.
* **Documentation**: Use a software cost driver sheet (available in NASA's SPAN system) to document assumptions, inputs, and estimation methodologies.
* **Breakout Costs**: Provide lifecycle phase and activity-specific costs to improve traceability and support adjustments over time.
* **Review and Update**: Regularly revisit cost estimates to reflect new information, evolving requirements, and improved understanding of project risks.
* **Risk Awareness**: Investigate both quantified risks and uncertainties to prevent significant budget overruns and schedule delays.

See [SWE-142 - Software Cost Repositories](/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories).

## 3.9 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-142 - Software Cost Repositories](/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 3.10 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Estimation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Estimation) |

# 4. Small Projects

The conditions for cost estimates apply to small as well as large tasks but should be scaled to fit the size and scope of the task.  All estimates are made using some combination of the basic estimation methods of analogy or Cost Estimating Relationship (CER).  Whatever method is used, it is most important that the assumptions and formulas used be documented to enable more thorough reviews and to make it easier to revise estimates at future dates when assumptions may need to be revised.  A documented estimate is the first line of defense against arbitrary budget cuts.  Small projects nominally use the analogy estimates methods if the development organization has data to support them.  The use of at least two estimates is always considered to be a best practice for small and large software estimation activities.

## 4.1 Life Cycle Coverage for Small Projects

Even for small software projects, cost estimates must cover the full lifecycle, including initial development, testing, deployment, maintenance, and eventual decommissioning. While smaller efforts typically have fewer lifecycle phases, important considerations remain:

* **Streamlined Phases**: Small projects often combine or simplify lifecycle phases (e.g., development and testing may occur in parallel). Ensure that the cost estimate reflects these efficiencies without omitting critical activities.
* **Low-Maintenance Assumptions**: Maintenance costs may be reduced for smaller projects, but they should still account for updates, bug fixes, and small enhancements that are likely to occur post-delivery.
* **Annual Code Change Estimates**: For small projects, the percentage of annual lines of code changed may be smaller, but this metric still provides valuable insight into likely maintenance costs.

**Tip:** Use historical data from similar small projects to benchmark lifecycle costs instead of starting from scratch.

## 4.2. Project Attributes for Small Projects

### Guidance:

Small projects generally involve fewer attributes and narrower scopes, but proper attention to the following factors is still necessary:

* **Size**: Small projects typically involve fewer lines of code, which simplifies estimation. Focus on accurate measurement of the estimated size, and consider using analogy-based methods to leverage comparable past projects.
* **Functionality**: Smaller projects usually focus on delivering highly specific functionality rather than complex, multifaceted systems. Ensure the cost estimate reflects this narrower focus.
* **Complexity and Risk**: While small projects are less complex overall, some software tasks can still involve significant technical challenges (e.g., real-time data handling or integration with external systems). Account for complexity proportional to the project's scope.
* **Reuse of Code**: Small projects frequently leverage existing code or components to reduce development effort. Document time spent adapting or verifying inherited code to ensure reuse doesn't lead to underestimated costs.
* **Documentation Requirements**: Small projects may have streamlined documentation needs, but key deliverables such as requirements documentation, user manuals, and test plans are still critical.

**Tip:** Collaborate closely with technical leads and stakeholders to refine project-specific attributes. Avoid overestimating complexity unless justified by the task.

## 4.3 Technology Implications for Small Projects

#### Guidance:

While small projects often rely on mature and familiar technologies, occasionally they involve integrating newer tools or techniques. Address the following:

* **Use of Established Tools**: If the project uses well-established technologies, factor in minimal learning curve and reduced integration costs.
* **New Technology Costs**: If experimental or evolving technologies are used, detail associated costs for setup, validation, or adjustments. For small projects, the scope of technology maturation is usually more limited but can still be significant.
* **Cost Savings**: Small projects may achieve cost savings by leveraging lightweight tools or more efficient workflows. Document any savings assumptions to ensure traceability.

**Tip:** For small projects, new technology implications can often be resolved with simple training or adoption plans. Ensure these efforts are included in the cost estimate.

## 4.4 Risk and Uncertainty for Small Projects

### Guidance:

Small projects experience risks and uncertainties similar to larger initiatives, though with fewer high-impact variables. Tailored strategies for risk identification and management include:

* **Simplifying Risk Analysis**: Focus on core risks specific to the small project (e.g., tight deadlines, limited testing resources, reliance on small teams).
* **Quantifying and Mitigating Uncertainty**: Small projects often encounter uncertainties due to incomplete requirements or assumptions about integration efforts. Include allowances for changes or refinements in the estimate.
* **Low Overhead Strategies**:
  + Use simple risk matrices rather than complex probabilistic models, unless the scope demands it.
  + Consider basic Monte Carlo simulations for estimating uncertainty impact only if variability is significant (e.g., scope uncertainty).
* **Stakeholder and User Perspectives**: For small projects, engaging lightweight discussions with users and stakeholders early in the development phase can help identify risks related to usability or integration.

**Tip:** A short risk brainstorming session with the team can yield significant insights for small projects without requiring extensive formal analysis.

## 4.5 End-State Risk and Threat Assessments for Cybersecurity

### Guidance:

Small projects still require cybersecurity considerations, especially when dealing with web-based systems, critical interfaces, or any network-connected components. To address end-state risks for cybersecurity:

* **Cost of Cybersecurity Checks**: Include costs for simple assessments during software development (e.g., vulnerability scans or penetration testing) and operations.
* **Operational Monitoring**: For small projects with live deployments, budget for ongoing command and data monitoring tools to detect potential threats.
* **COTS Modifications**: Include costs for periodically applying updates to third-party software or hardware, such as patching vulnerabilities in shared codebases.

Cybersecurity threats may be less prominent for small projects with limited complexity or standalone environments but should not be ignored.

## 4.6 Software Assurance Support for Small Projects

### Guidance:

Although scaled-down, small projects still require software assurance efforts. These activities, including testing, validation, and verification, ensure the reliability and quality of the software product. Consider the following:

* **Streamlined Assurance**: Small projects can benefit from lightweight assurance strategies such as automated testing or selective manual validation.
* **IV&V Support**: Independent Verification and Validation (IV&V) may not be necessary for all small projects but should be considered if the software is mission-critical.

**Tip:** Discuss the implications of reduced software assurance with project stakeholders so that risks associated with limited assurances are fully understood.

## 4.7 Other Costs for Small Projects

### Guidance:

Even small projects incur additional costs unrelated to direct development activities. Ensure the following are considered:

* **Equipment and Tools**: Include costs for shared resources like configuration management tools, small workstations, or simulators, scaled appropriately based on the project size.
* **Travel**: For small projects, travel costs may be reduced or eliminated, but ensure necessary site visits for reviews or stakeholder meetings are accounted for.
* **Training**: Small teams may require specific training for tools or workflows, and these expenses should be included in the estimate.

## 4.8 Best Practices for Small Projects

1. **Simplify Estimation**: Focus on analogy-based estimation or bottom-up techniques rather than complex parametric models designed for larger projects.
2. **Collaborate Early**: Engage the software acquirer and provider in discussions to align assumptions and expectations efficiently, avoiding unnecessary iterations.
3. **Document Lightly**: Maintain clear records of assumptions, methods, and data used to develop the estimate but avoid excessive documentation unless required by stakeholders.
4. **Focus on Key Drivers**: For small projects, emphasize the elements that impact cost the most—typically, size, complexity, and reuse.

By applying these tailored practices, teams can develop accurate and credible software cost estimates for small projects with reduced administrative effort while still meeting NASA's requirements and standards.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-116)

  [2008 NASA Cost Estimation Handbook (CEH),](http://ceh.nasa.gov/ "Click to open in new window")

  2008. Accessed August 15, 2011 at http://ceh.nasa.gov.  This URL is a website that lists multiple resources for download.
* (SWEREF-136)

  [Software Engineering Economics,](https://www.amazon.com/Software-Engineering-Economics-Barry-Boehm/dp/0138221227 "Click to open in new window")

  Boehm, Barry. Englewood Cliffs, NJ:Prentice-Hall, 1981.
* (SWEREF-166)

  [Cost Analysis Data Requirement (CADRe),](https://www.nasa.gov/offices/ocfo/functions/models_tools/CADRe_ONCE.html "Click to open in new window")

  Database of cost metrics for NASA missions: http://www.nasa.gov/offices/ooe/CADRe\_ONCE.html#.U0Qc-BC9Z8E, (Accessed December 09, 2014). This URL is a website that lists multiple resources for download.
* (SWEREF-184)

  [Estimating Software-Intensive Systems: Projects, Products, and Processes,](http://www.amazon.com/Estimating-Software-Intensive-Systems-Projects-Processes/dp/0201703122/ref=sr_1_2?s=books&ie=UTF8&qid=1312314470&sr=1-2 "Click to open in new window")

  Stutzke, R., Addison-Wesley Professional (May 6, 2005).
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-306) Reifer, D., (2000). A Poor Man 's Guide to Estimating Software Costs. 8th ed., Reifer Consultants, Inc.
* (SWEREF-419)

  [GAO Cost Estimating and Assessment Guide, Best Practices for Developing and Managing Capital Program Costs.](http://www.gao.gov/new.items/d093sp.pdf "Click to open in new window")

  GAO-09-3SP. United States Government Accountability Office. Applied Research and Methods. March, 2009.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains the following lesson learned related to cost estimation:

* **Flight Software Engineering Lessons. Lesson Number 2218[572](#_tabs-<p></p>):** The engineering of flight software is a major consideration in establishing the JPL project total cost and schedule because every mission requires a significant amount of new software to implement new spacecraft functionality. Constraints to the development and testing of software concurrent to engineering the rest of the flight system have led to flight software errors, including the loss of some missions. The findings of several JPL studies and flight mishap investigations suggest a number of recommendations for mitigating software engineering risk.

## 6.2 Other Lessons Learned

Other Lessons Learned from experience (Hihn, Jairus M. JPL. 818.354.1248) and the JPL Cost Estimation Handbook available in SPAN include the following concepts:

* Common costs left out of cost estimates.

+ Review preparation.
+ Documentation.
+ Fixing Anomalies and Engineering Change Requests (ECRs)’s.

+ Testing.
+ Maintenance.
+ Basic management and coordination activities.
+ Technical leads do spend time doing management activities.
+ Mission Support Software Components.
+ Development and test environments.
+ Travel.
+ Training.

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Incremental development and integration can save life cycle cost and reduce risk](https://software.gsfc.nasa.gov/lesson-details/2/). **Lesson Number 2**: The recommendation states: "Incremental development and integration requires money and coordination up-front, as it can save life cycle cost and reduce risks."
* [Include funding for appropriate tools to ensure IT security](https://software.gsfc.nasa.gov/lesson-details/48/). **Lesson Number 48**: The recommendation states: "The project budget should include funding for appropriate tools to ensure IT security."
* [Develop an attribute based cost estimate](https://software.gsfc.nasa.gov/lesson-details/49/). **Lesson Number 49**: The recommendation states: "In a particularly cost constrained environment, develop attribute-based cost estimates, i.e., based on the attributes of the software and software work products, such as size, number of documents, complexity, etc. This provides a basis of estimate that is justifiable and defensible, and can be re-evaluated if the assumptions and attributes change."
* [Dedicate more hours to FSSE preparation for post-commissioning](https://software.gsfc.nasa.gov/lesson-details/79/). **Lesson Number 79**: The recommendation states: "Dedicate more hours to FSSE preparation for post-commissioning, particularly in the preparation of the Lab as long-term asset for the mission."
* [Staffing plan takes into account continuing support for activities that occur after software is delivered](https://software.gsfc.nasa.gov/lesson-details/90/). **Lesson Number 90**: The recommendation states: "Develop a staffing plan that takes into account continuing support for activities that occur after software is delivered."
* [Ensure assumptions made during Phase E budgets align with historical data](https://software.gsfc.nasa.gov/lesson-details/129/). **Lesson Number 129**: The recommendation states: "Ensure assumptions made during Phase E budgets align with historical data."
* [Fault Detection and Correction (FD/C) effort](https://software.gsfc.nasa.gov/lesson-details/136/). **Lesson Number 136**: The recommendation states: "Sufficiently staff the Fault Detection and Correction (FD/C) effort, and begin at an earlier phase in the mission."
* [The cost of dealing with a small unproven company](https://software.gsfc.nasa.gov/lesson-details/146/). **Lesson Number 146**: The recommendation states: "The cost of dealing with a small unproven company will end up being higher than originally planned."
* [Plan and budget for additional oversight and assistance to R&D focused partners](https://software.gsfc.nasa.gov/lesson-details/150/). **Lesson Number 150**: The recommendation states: "GSFC should plan and budget for additional oversight and assistance to R&D focused partners, based on an assessment of the organization's gaps (e.g., On-site management, Hands-on assistance with verification phase, bring selected components or work products in-house)."
* [Responding to cost/schedule/performance challenges may require hard choices](https://software.gsfc.nasa.gov/lesson-details/154/). **Lesson Number 154**: The recommendation states: "Responding to cost/schedule/performance challenges may require hard choices."
* [For a flight mission, plan and budget from outset for full end-to-end testing simulating an "orbit in the life"](https://software.gsfc.nasa.gov/lesson-details/161/). **Lesson Number 161**: The recommendation states: "For a flight mission, plan and budget from outset for full end-to-end testing simulating an "orbit in the life"."
* [AWS pricing model and discount programs](https://software.gsfc.nasa.gov/lesson-details/175/). **Lesson Number 175**: The recommendation states: "Invest time to consult with subject matter experts familiar with AWS products and discount programs during AWS migration planning stages so costing estimates are as accurate as possible."
* [AWS services availability](https://software.gsfc.nasa.gov/lesson-details/176/). **Lesson Number 176**: The recommendation states: "Ensure that AWS services of interest are available in the AWS region you selected."
* [When using commercial BSP for VxWorks don't forget to include yearly maintenance fees](https://software.gsfc.nasa.gov/lesson-details/304/). **Lesson Number 304**: The recommendation states: "When costing a mission that has software licenses, these fees must be accounted for the duration of the mission, including post launch (through Phase E)."
* [Heritage analysis should consider all aspects of the flight software](https://software.gsfc.nasa.gov/lesson-details/337/). **Lesson Number 337**: The recommendation states: "Heritage analysis should consider operating system selection as well as framework and application software when developing a Basis of Estimate (BOE) and schedule."
* [GOLD Rule 1.43 provides end-to-end demonstration for each SW component that can be changed in flight](https://software.gsfc.nasa.gov/lesson-details/343/). **Lesson Number 343**: The recommendation states: "There are multiple Observatory components with loadable flight software - demonstrating the code change process for each spacecraft and instrument FSW component can be very beneficial and useful. Incorporate into project plans and budgets and provide resources for the satisfaction of the GOLD Rule 1.43 requirement for pre-flight end-to-end code change demonstrations."

# 7. Software Assurance

**SWE-151 - Cost Estimate Conditions**

3.2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions:

a. Covers the entire software life cycle.  
b. Is based on selected project attributes (e.g., programmatic assumptions/constraints, assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products).  
c. Is based on the cost implications of the technology to be used and the required maturation of that technology.  
d. Incorporates risk and uncertainty, including end state risk and threat assessments for cybersecurity.  
e. Includes the cost of the required software assurance support.  
f. Includes other direct costs.

This requirement ensures the accuracy and completeness of software cost estimates across the project's lifecycle, factoring in project attributes, technology considerations, risks, and supporting activities like Software Assurance (SA). SA personnel play a critical role in verifying the inclusion and accuracy of software assurance effort estimates, validating cost inputs, and identifying risks or issues with cost assumptions.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess the project's software cost estimate(s) to determine if the stated criteria listed in "a" through "f" are satisfied.

## 7.2 Software Assurance Products

### 7.2.1 Software Assurance Plan Assessment

**Purpose**: Evaluates whether the Software Assurance Plan adequately includes SA cost estimates and aligns with the project's cost estimation process.  
**Contents**:

* Confirmation that SA support activities and deliverables (e.g., audits, reviews, and analysis) are included in the cost estimate.
* Identification of any gaps in SA resource allocation or budgeting for lifecycle phases.
* Verification of assumptions for SA budgeting (e.g., grassroots estimates, historical benchmarks).
* Recommendations for adjustments where SA costs are inaccurately or incompletely estimated.

### 7.2.2 Software Engineering Plans Assessment

**Purpose**: Assesses whether software engineering plans, such as the Software Development Plan (SDP) or Software Project Plan (SPP), incorporate complete lifecycle cost estimates.  
**Contents**:

* Verification of cost coverage across all lifecycle phases (e.g., conception, development, integration, testing, operations, and maintenance).
* Assessment of cost models or estimation methodologies used in engineering plans (e.g., grassroots estimates, analogy-based estimates).
* Validation of project attributes included in cost estimation (e.g., size, functionality, complexity, reuse, cybersecurity risk).
* Analysis of software development resource allocation against specific engineering tasks and milestones.

### 7.2.3 Software Cost Estimate Assessment Report

**Purpose**: Documents SA’s evaluation of the project’s cost estimate for completeness and compliance with the stated conditions in the requirement.  
**Contents**:

* Analysis of lifecycle cost coverage, identifying gaps in phases not properly estimated.
* Evaluation of project attribute inclusion, identifying missing or underestimated attributes (e.g., reuse code complexity, software risk factors).
* Assessment of cost implications for new technologies, identifying risks related to tool/process immaturity and learning curves.
* Validation of risk and uncertainty inclusion, including evaluation of cybersecurity threat assessments.
* Verification of SA cost inclusion (e.g., grassroots estimates, percentage-based approximation of SA costs).
* Identification of "forgotten items" (e.g., procurements, training, equipment setup).
* Highlighted issues or risks related to cost assumptions or exclusions.

### 7.2.4 SA-Specific Cost Estimate Submission Report

**Purpose**: Confirms submission of SA cost estimates and planning parameters to the project's cost repository.  
**Contents**:

* Breakdown of SA cost components:
  + SA personnel cost estimates across each phase.
  + Cost of SA tools and resources (e.g., issue tracking systems, static analysis tools).
  + Documentation and audit preparation cost estimates.
  + Travel costs for assurance-related meetings or activities.
* Timeline of SA cost estimate updates by lifecycle milestone (e.g., SDR, CDR, TRR, project closure).
* Evidence of repository submission with submission dates and completeness verification.

### **7.3 Metrics**

Metrics track the accuracy, resource allocation, and inclusion of SA-related costs within software project estimates.

### 7.3.1 Lifecycle Cost Metrics:

* **Planned SA Resource Allocation vs. Actual Allocation:**
  + Tracks resource usage across all lifecycle phases compared to original estimates.
* **Comparison of Initial SA Cost Estimates vs. Final Costs:**
  + Measures differences in assumptions versus actual expenditures for SA tasks.

### 7.3.2 Project Attribute Metrics:

* **# of Project Requirements vs. Estimated SLOC:**
  + Tracks the relationship between detailed requirements and estimated source lines of code (SLOC).
* **Size and Complexity Trends:**
  + Monitors changes in project size estimates and their impact on SA effort.

### 7.3.3 Risk Metrics:

* **Inclusion of Risk-Based Costs:**
  + Tracks whether identified risks (e.g., cybersecurity costs, technology immaturity impacts) are assigned dollar values and properly estimated.

### 7.3.4 Repository Submission Metrics:

* **% of Cost Estimate Submission Milestones Met:**
  + Tracks timely submission of cost parameters at major milestones (e.g., SDR, PDR, CDR).

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

Software Assurance Actions to Evaluate Cost Estimates.

### Step 1: Verify Lifecycle Coverage

* Confirm the software cost estimate covers phases from conception through retirement, verifying inclusion of cost coverage for:
  + Requirement analysis, design, implementation, testing, operations, maintenance, and decommissioning.
  + Verify lifecycle definition in the project’s Software Development Plan (SDP) or SPP.

### Step 2: Validate Project Attributes

* Ensure attributes such as functionality, complexity, reuse code, modified code, and risk impacts are represented in the estimate:
  + Confirm grassroots estimates align with known project constraints and complexity ratings.
  + Validate cost models (e.g., COCOMO, historical analogies) appropriately incorporate project attributes.

### Step 3: Assess Technology Maturation Costs

* Verify that cost estimates for new technologies address learning curves and immaturity risks:
  + Confirm cost adjustments for tools or processes requiring additional development time.

### Step 4: Evaluate Risk and Uncertainty Inclusion

* Validate risk-based cost implications:
  + Cybersecurity risks and threat assessments (e.g., static code analysis, vulnerability mitigation costs).
  + Other uncertainties (e.g., unknowns in cross-program dependencies).

### Step 5: Confirm SA Cost Estimates

* Validate inclusion of SA cost:
  + Personnel and activity cost estimates across lifecycle phases (audits, reviews, analysis).
  + Tools and resources necessary for SA execution (e.g., risk management tools, diagnostic software).
  + Grassroots estimates or percentage-based approximations (e.g., 5-6% of lifecycle software cost).

### Step 6: Confirm Inclusion of Forgotten Costs

* Review common "forgotten items," such as:
  + Necessary procurements (e.g., development and test environments, documentation tools).
  + Training costs (e.g., assurance personnel, project team).
  + Travel costs (e.g., meetings, stakeholder collaboration).
  + Costs associated with management tasks and anomaly resolutions.

### Step 7: Submit and Audit Cost Estimates

* Confirm submission of software cost estimates (including SA costs) to the Center repository at major milestones and project completion.
* Perform periodic audits of repository submissions to ensure completeness, flag missed updates, and confirm SA cost incorporation.

By leveraging these steps, Software Assurance personnel ensure thorough evaluation, alignment, and submission of cost estimates for compliance with this requirement. The outlined guidance mitigates risks associated with incomplete or inaccurate cost estimation, enabling smoother project execution and lifecycle coverage.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-142 - Software Cost Repositories](/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective evidence substantiates that the project's software cost estimate covers all required elements, alongside SA-specific cost estimates.

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

## 8.1 Objective Evidence to Be Collected

### 8.1.1 Confirmation of Cost Estimate Completeness:

* Verified software cost estimate covering the entire software lifecycle (e.g., conception through retirement).
* Documentation of attributed project-related costs (e.g., size, functionality, complexity, risk considerations).
* Evidence of accurate cost coverage for critical technology maturation needs (e.g., learning curves, immaturity risks).

### 8.1.2 Evidence of SA Cost Estimates:

* Breakdown of SA lifecycle costs included within the software cost estimate (e.g., audits, reviews, assurance tools).
* Documentation confirming SA effort representation in grassroots estimates or percentage-based approximations (e.g., 5-6% of total software cost).

### 8.1.3 Repository Submission Confirmation:

* Records of cost estimate submission to the Center repository, including SA cost data.
* Evidence of periodic updates to align with lifecycle milestones.
