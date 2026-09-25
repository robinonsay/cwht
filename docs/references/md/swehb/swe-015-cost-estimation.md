# SWE-015 - Cost Estimation

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695400. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation

SWE-015 - Cost Estimation

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695400)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695400&showCommentArea=true&showComments=true#addcomment)

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

3.2.1 To better estimate the cost of development, the project manager shall establish, document, and maintain:

1. 1. Two cost estimate models and associated cost parameters for all Class A and B software projects that have an estimated project cost of $2 million or more.
   2. One software cost estimate model and associated cost parameter(s) for all Class A and Class B software projects that have an estimated project cost of less than $2 million.
   3. One software cost estimate model and associated cost parameter(s) for all Class C and Class D software projects.
   4. One software cost estimate model and associated cost parameter(s) for all Class F software projects.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-015 History

SWE-015 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.3 The project shall establish, document, and maintain at least one software cost estimate and associated cost parameter(s) that satisfies the following conditions:   1. 1. Covers the entire software life cycle.    2. Is based on selected project attributes (e.g., assessment of the size, functionality, complexity, criticality, and risk of the software processes and products).    3. Is based on the cost implications of the technology to be used and the required maturation of that technology. |
| Difference between A and B | Further defines that Class A and B software over $2M need 2 cost estimates, others only need 1 estimate. Removed the conditions that need to be satisfied. |
| B | 3.2.1 The project manager shall establish, document, and maintain two cost estimates and associated cost parameters for all software class A and B projects that have an estimated project cost of $2 million dollars or more or one software cost estimate and associated cost parameter(s) for other software projects. |
| Difference between B and C | Made requirement more explicit; Added requirement for the use of a "model" and deleted the requirement for Class E to develop a cost estimate. |
| C | 3.2.1 To better estimate the cost of development, the project manager shall establish, document, and maintain:   1. 1. Two cost estimate models and associated cost parameters for all Class A and B software projects that have an estimated project cost of $2 million or more.    2. One software cost estimate model and associated cost parameter(s) for all Class A and Class B software projects that have an estimated project cost of less than $2 million.    3. One software cost estimate model and associated cost parameter(s) for all C and D software projects.    4. One software cost estimate model and associated cost parameter(s) for all Class F software projects. |
| Difference between C and D | Clarification - added the word Class in front of C & D in item c. |
| D | 3.2.1 To better estimate the cost of development, the project manager shall establish, document, and maintain:   1. 1. Two cost estimate models and associated cost parameters for all Class A and B software projects that have an estimated project cost of $2 million or more.    2. One software cost estimate model and associated cost parameter(s) for all Class A and Class B software projects that have an estimated project cost of less than $2 million.    3. One software cost estimate model and associated cost parameter(s) for all Class C and Class D software projects.    4. One software cost estimate model and associated cost parameter(s) for all Class F software projects. |

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

In modern acquisition practices, cost estimates are now developed much earlier in the project life cycle, often before detailed technical information or finalized requirements are available. This early estimation process introduces significantly greater uncertainty than in the past, particularly for large-scale, complex projects. Establishing **two independent cost estimation models** for Class A and Class B software projects with an estimated cost of $2 million or more mitigates this uncertainty by enabling cross-validation of cost predictions, thereby reducing reliance on a single, potentially flawed model. This approach increases confidence in the accuracy of the estimates and ensures that critical financial decisions are based on credible data.

Credible cost estimates are essential to effective project management and lifecycle planning, as emphasized in **NPR 7150.2, NASA Software Engineering Requirements**, Section 3.2. Regular updates to cost estimates throughout the life cycle allow projects to stay aligned with evolving technical, budgetary, and schedule considerations. In contrast, unreliable cost estimates can lead to severe issues in planning and budgeting, such as misallocation of resources, inadequate staffing, and project delays. These cascading effects can ultimately jeopardize the project's ability to meet its objectives efficiently or effectively.

By requiring the use of two independent cost estimation models, NASA ensures that large, mission-critical software projects operate under more robust financial planning, reducing the risk of overestimation or underestimation and enabling project teams to make better-informed decisions. This strategy reflects a proactive effort to mitigate uncertainty during the early stages of project development, ensuring that resources are used optimally and project objectives are achieved without unnecessary setbacks.

The requirement ensures **accurate, reliable, and scalable software cost estimation practices**, aligned with the project's scale, complexity, and criticality. It reduces risks, enhances accountability, and supports financial planning efforts, making it easier to manage resources effectively and sustain confidence among stakeholders.

The direct rationale for this requirement is largely tied to **accountability, financial planning, and risk management**. Here’s why this requirement exists:

## **2.1 Improved Cost Estimation Accuracy**

For projects of differing classes and sizes, using defined cost estimate models ensures that the estimation process is tailored to the complexity and effort associated with the software. By requiring multiple models for higher-stakes projects (Class A and B with estimated costs of $2 million or more), the project manager can better triangulate and validate estimates, thereby reducing the risk of underestimating or overestimating project costs.

## **2.2 Complexity of Class A and B Projects**

Class A and B projects often involve higher complexity, criticality, and larger scopes (sometimes with safety or mission-critical considerations). Using at least two cost estimate models introduces redundancy and ensures broader consideration of cost drivers, which is critical for high-cost projects ($2 million or more). Robust estimations reduce financial risks and provide informed decision-making at higher levels.

## **2.3 Risk Mitigation for High-Cost Projects**

Large software projects (greater than $2 million) often face greater financial, schedule, and scope risks. Requiring two cost estimation models ensures that any blind spots from one model are offset by a second, minimizing the likelihood of budget overruns or project failures.

## **2.4 Scaling Estimation Effort by Project Size and Criticality**

Smaller projects (less than $2 million) or projects classified as Class C, D, or F typically don't have the same complexity or risk exposure as Class A and B projects. Therefore, one cost estimate model is adequate for these projects, balancing thoroughness with efficiency in planning. Requiring just one model avoids unnecessary administrative overhead while still enforcing proper cost-estimation practices.

## **2.5 Documentation for Accountability and Future Use**

Documenting and maintaining cost estimation models ensures transparency, traceability, and replicability of the estimates. This is useful both for internal reviews (e.g., audits or stakeholder reviews) and for lessons learned in future projects. Proper documentation also helps identify trends in cost estimation inaccuracies over time.

## **2.6 Tailoring Practices to Software Classification Types**

Software classifications are typically based on the criticality of the software's functionality (e.g., safety-critical, mission-critical). By differentiating requirements for cost estimation based on software classification (Class A/B/C/D/F), the organization ensures that the estimation effort corresponds directly to the project's risk and importance. For example:

* **Class F** software typically involves smaller, less critical projects, requiring minimal resources for cost estimation.
* **Class A/B** systems are typically robust, mission-critical systems, warranting more detailed and redundant cost modeling.

## **2.7 Compliance with Organizational and Industry Standards**

This requirement is likely aligned with broader industry or organizational standards (such as NASA’s software engineering management standards). These standards emphasize cost estimation rigor, especially for high-risk and high-cost projects, and help organizations avoid common pitfalls, including scope creep, funding shortages, and stakeholder dissatisfaction.

## **2.8 Cost Parameter Definition for Consistency**

Incorporating specific cost parameters as part of the requirement ensures that cost estimations remain consistent across projects and teams. It also provides insight into assumptions or metrics that drive estimates, improving the credibility of cost estimates.

# 3. Guidance

Creating accurate cost estimates for embedded flight software in space missions is inherently challenging due to the complexity, high standards of reliability, and critical role the software plays in mission success. Embedded flight software requires rigorous development practices across the entire software lifecycle to ensure functionality, safety, and compliance with stringent standards. As a result, estimating costs for such software involves accounting for multiple factors that influence development and operational costs. Below is enhanced guidance for meeting this requirement:

## 3.1 General Considerations for Software Cost Estimation

Determining the cost of embedded flight software depends on numerous interrelated factors. While no single formula applies universally, the following considerations are essential for accurate estimation:

### 3.1.1 Development Costs

* The salaries or hourly wages of software engineers are a primary driver of development costs. These costs vary based on:
  + The expertise level of personnel (junior engineers vs. senior developers specializing in mission-critical systems).
  + The geographic location of the development team (local labor costs and technical resources).
  + The duration and complexity of the software project.

### 3.1.2 Tooling and Infrastructure Costs

* Embedded software development frequently depends on specialized tools, platforms, and hardware for activities like simulation, testing, and debugging. Examples include:
  + Integrated Development Environments (IDEs).
  + Simulation software (e.g., real-time simulators for flight environments).
  + Hardware-in-the-loop (HIL) testing platforms.
  + Version control, configuration management, and test automation systems.
* License fees, maintenance costs, updates, and support for these tools must be included in the cost estimation.

### 3.1.3 Quality Assurance Costs

* Software quality assurance is critical for space missions, encompassing tasks such as:
  + Testing, validation, and verification (benchmarks, unit tests, integration tests).
  + Certification efforts to comply with NASA standards (e.g., NASA-STD-8739) or aerospace industry standards like DO-178C.
  + Specialized test equipment and highly skilled test engineers.
* Robust testing processes are often time-intensive but essential, as they reduce mission risks and costly post-launch corrections.

### 3.1.4 Documentation and Compliance Costs

* Space software projects require comprehensive documentation and compliance with rigorous technical standards (e.g., NPR 7150.2). This contributes to additional costs, such as:
  + Creating detailed documentation (e.g., requirements breakdown, design documents, test plans, operational manuals).
  + Performing audits and reviews to meet programmatic or regulatory requirements.

### 3.1.5 Risk Management Costs

* Embedded flight software often involves high mission-critical risks, leading to costs for activities like:
  + Risk assessments (e.g., identifying software vulnerabilities or mission failure points).
  + Mitigation strategies, including redundancy, code hardening, and back-up procedures.
  + Contingency planning and adjustments if unexpected issues arise during development.

### 3.1.6 Lifecycle Costs

* The cost of embedded flight software goes beyond initial development and includes maintenance, support, and updates throughout the software's lifecycle.
  + Bug fixes, patches, and performance enhancements after deployment.
  + Support for evolving mission requirements or upgrades in the operating environment.
  + Personnel and infrastructure costs for sustaining technical support after project delivery.

## 3.2. Role of Software Cost Estimation in Mission and Lifecycle Management

Embedded flight software plays an increasingly critical role in space missions, and underestimating its costs can lead to severe consequences such as launch delays, mission failures, or significant budget overruns. NASA standards like *NPR 7150.2* emphasize regular updates to cost estimates throughout the software lifecycle to account for evolving requirements, schedule changes, and technical scope adjustments.

Cost estimation errors are a common source of software cost growth in retrospective lessons learned, with observed overruns often exceeding 50%–100%. By using **two independent software cost estimates** for high-cost projects (Class A and B, $2 million or more), NASA aims to:

* Address the inherent uncertainty of early-stage estimates.
* Validate the accuracy of primary estimates for mission-critical software efforts.
* Ensure strategic use of project resources to mitigate risks and maximize performance.

Additionally, models like Barry Boehm’s seminal uncertainty chart highlight the variability of cost estimates during early phases of the lifecycle, underscoring the importance of using multiple estimation approaches to counteract errors.

## 3.3. Recommended Approach for Implementing the Requirement

### 3.3.1 Establishing a Software Cost Estimation Process

NASA recommends using industry-standard tools and practices for cost estimation, such as COCOMO™ II or SEER® SEM, tailored to project-specific parameters and performance data. This approach should include:

* A documented process for generating cost estimates, including defined inputs, assumptions, and methodologies.
* Continuous updates to estimates during the project lifecycle as new information (e.g., scope changes or technical requirements) becomes available.

### 3.3.2 Documenting and Maintaining Software Cost Parameters

* Clear documentation is essential for traceability, validation, and reproducibility of estimates. Key items to document include:
  + The process used for cost estimation.
  + All parameters, assumptions, and uncertainties associated with the estimate.
  + Supporting evidence or references for inputs, such as analogous projects or historical records.
* Parameters should be maintained and updated as needed, ensuring alignment with lifecycle adjustments.

### 3.3.3 Cost Estimation Across Project Scope

* Class A and B projects require **two independent cost estimates** to enhance validation and mitigate the extensive uncertainties inherent in high-cost, complex software efforts. One estimate should ideally be **model-based**, using parametric cost modeling or analogous reasoning.
* Smaller projects (Class C, D, and F) may require one cost estimate due to reduced complexity and risk, thereby streamlining estimation efforts.

## 3.4. Key Elements of the Cost Estimation Process

### 3.4.1 Scoping and Planning

* Define the scope of the software task, including the full set of deliverables and development activities. Scoping should include assessments of:
  + Key complexity factors, such as operating environment and concept of operations.
  + Planned inheritance and reuse of software components.
  + Risk posture and any new technology assumptions.

Scoping is not requirements writing – requirements are generally developed after the initial planning and estimating are completed.

### 3.4.2 Bottom-Up Estimate

* The bottom-up estimate is often the most accurate form of cost prediction in later stages and involves:
  + Developing a Work Breakdown Structure (WBS).
  + Estimating effort and size for each WBS element.
  + Mapping size and complexity to historical or analogous data, and adjusting for project-specific factors.
  + Documenting these assumptions carefully to support future updates and review.

One recommendation is that if the reused code will require greater than 50 percent modifications, then it should be treated as a new code for cost estimation purposes.

### 3.4.3 Model-Based Estimates

* Parametric models like COCOMO™ II and SEER® SEM are widely used at NASA and can:
  + Serve as primary estimates during early lifecycle phases.
  + Provide a secondary estimate to validate bottom-up predictions.
  + Enable reasoning about cost impacts from scenario-based decisions (e.g., changes to scope or reuse levels).

### 3.4.4 Validation and Reconciliation

* Review estimates to validate alignment with project budgets and schedules. Ensure all assumptions and inputs are accurate and accounted for.
* If discrepancies arise, prioritize adjusting scope rather than forcing optimistic or unrealistic assumptions on inheritance or reuse.

### 3.4.5 Review, Approval, and Maintenance

* Conduct peer reviews to verify estimates against project goals, ensuring alignment with BOE and WBS.
* Secure formal approval from stakeholders, including project and software managers, before finalizing estimates.
* Configuration-manage cost estimates and related data for accessibility and updates during the software lifecycle.

## 3.5. Addressing Challenges in Cost Estimation

### 3.5.1 Measuring Software Size

* Software size is a critical input for cost modeling. Accurate size estimation depends on distinguishing between new, reused, and modified-reused lines of code. Use tools like SLiC (Source Lines Counter) for precise counts. *Best practice*: If reused code requires more than 50% modifications, treat it as new code for cost estimation purposes.

### 3.5.2 Multiple Estimates for Risk Mitigation

* Two cost estimates are highly recommended for validation, especially when project scope is unclear. Cross-referencing bottom-up estimates with parametric model-based estimates helps reduce misalignment and highlights critical uncertainties.

## 3.6. Final Recommendations

* **Invest in Proper Estimation Practices**: Focus on reliability, safety, and mission success rather than minimizing cost per line of code. Rigorous estimation and testing practices reduce risks associated with failure and costly rework.
* **Leverage Historical Data**: Anchor predictions on proven metrics and lessons learned from prior projects where possible.
* **Focus on Uncertainty Management**: Use tools like probabilistic estimation in parametric models to express and manage estimation uncertainties effectively.

By implementing these best practices, drivers of cost overruns can be addressed early, ensuring seamless project execution within budgetary constraints and mission timelines

Effort multipliers characterize the product, platform, personnel, and project attributes of the software project under development.

Do not reduce costs by eliminating reserves and making optimistic and unrealistic assumptions, especially concerning the amount of code inheritance.

 If the project has a cost repository, that repository should be updated with data related to this cost estimate, including software size, effort, and schedule data. See also, [SWE-142 - Software Cost Repositories](/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories).

For Additional Guidance on Peer Reviews see [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-142 - Software Cost Repositories](/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.8 Center Process Asset Libraries

NASA-specific cost estimation process information is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook. Also, see below for SPAN

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Estimation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Estimation)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting) |

# 4. Small Projects

The same basic estimation principles apply to both small and large software projects, but they must be adjusted to suit small tasks. For smaller projects, the focus should be on balancing the reduced effort, shorter timelines, and scaled-down deliverables with the need for credible and actionable cost estimates.

## 4.1 Tailoring Estimation Techniques for Small Projects

* **Simplify Your Methods:** While parametric models or detailed bottom-up estimates are common in large-scale projects, small projects can benefit from lightweight, streamlined estimation techniques that save time while maintaining accuracy.
  + Use analogy-based estimates when sufficient historical data is available for comparison.
  + If historical data is unavailable, start with effort-based estimates (e.g., hours or weeks per task) anchored on expert judgment.
* **Focus on Critical Drivers:** Small projects are more sensitive to specific cost drivers (e.g., rework or testing costs). Ensure these key drivers are accounted for even in simplified estimates.

### 4.2 Challenges with Cost Models for Small Projects

Many parametric cost models, such as COCOMO™ II and SEER®-SEM, are calibrated for medium- to large-scale projects, with assumptions regarding economies of scale that may not hold true for small tasks. These models may generate inaccurate results if applied directly to small projects without careful adjustment.

* **Recommendation: Rely More Heavily on Analogy-Based Estimates**

  + Analogy-based estimates—comparing your small project to similar, completed tasks—are often more effective for small projects. This approach allows you to leverage historical data instead of relying on assumptions embedded in cost models.
  + Use projects of a comparable size, scope, and complexity from your local data repository or lessons learned database as reference points.
  + Where analogy-based data is insufficient, involve subject matter experts to provide insight into likely similarities or differences.
* **Validation of Cost Models for Small Tasks:**

  + If a cost model must be used, verify that it is appropriate for small tasks by validating its predictions against historical outcomes on projects of similar size.
  + Adjust the model inputs and cost drivers to reflect the unique characteristics of smaller projects, such as reduced technical complexity or streamlined documentation requirements.

## 4.3 Streamlining the Estimation Process

Small projects typically have a limited budget and shorter schedules, so overburdening them with detailed documentation and complex estimation tools is counterproductive. However, these projects still benefit from disciplined planning and forecasting.

* **Reduce Estimation Overhead**: Focus on key deliverables, such as high-level scope, lifecycle cost estimates, and a risk-informed contingency budget.
* **Focus on Agility and Flexibility**: Revisit and refine estimates more frequently during execution as small projects are often more susceptible to scope changes or unplanned issues.

## 4.4 Additional Considerations for Small Project Cost Estimation

### 4.4.1 Documentation and Traceability

Although smaller projects require less detailed documentation than larger ones, it is still critical to document the assumptions, methods, and parameters used to develop estimates. This enables future validation and allows lessons learned from the project to feed into future cost estimation efforts.

### 4.4.2 Testing and Quality Assurance

Even for small projects, quality assurance is important. Testing costs should be factored in, especially when the software has critical functionality or interfaces with other systems. Underestimating quality assurance efforts is a common pitfall, even for simpler tasks.

### 4.4.3 Planning for Reuse

If the project involves modifying or reusing existing code, avoid assuming a one-to-one reduction in effort. Factor in costs for understanding and adapting the inherited code, which may involve additional testing, debugging, or redesign.

## **4.5 Summary of Recommendations for Small Projects**

* **Greater Reliance on Analogy-Based Methods**: Analogy-based approaches, supported by historical data or expert opinion, are often more accurate and practical for small projects, given the limitations of models tailored for larger efforts.
* **Validate Cost Models for Small Tasks**: If parametric models are used, ensure their calibration for small-project environments and adjust inputs accordingly.
* **Simplify and Streamline Estimates**: Use lightweight and agile estimation techniques to avoid unnecessary overhead while maintaining sufficient accuracy to guide decision-making.
* **Document Assumptions and Parameters**: Even for small tasks, documenting the reasoning behind estimates enhances reproducibility and provides value for future analogous efforts.
* **Account for Risk and Testing Costs**: Ensure that critical factors such as testing efforts, rework, and risk mitigation remain part of the estimate.

By adopting these tailored practices, project teams can ensure reliable cost estimates for small projects while avoiding excessive complexity or unnecessary cost escalations. This approach ensures that smaller efforts are managed effectively and deliver value without underestimating the resources needed for success.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-116)

  [2008 NASA Cost Estimation Handbook (CEH),](http://ceh.nasa.gov/ "Click to open in new window")

  2008. Accessed August 15, 2011 at http://ceh.nasa.gov.  This URL is a website that lists multiple resources for download.
* (SWEREF-135)

  [Software Cost Estimation with COCOMO II,](https://www.amazon.com/Software-Cost-Estimation-COCOMO-II/dp/0137025769 "Click to open in new window")

  Boehm, B., et. al. (2000). Prentice Hall, Upper Saddle River, N.J.,  ISBN-10: 0130266922
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
* (SWEREF-366)

  [Handbook for Software Cost Estimation JPL CL#00-0169, May 30, 2003.](https://www.academia.edu/19060864/Handbook_for_Software_Cost_Estimation "Click to open in new window")

  JPL, Hihn, Jarius, Lum, Karen; 2000,
* (SWEREF-419)

  [GAO Cost Estimating and Assessment Guide, Best Practices for Developing and Managing Capital Program Costs.](http://www.gao.gov/new.items/d093sp.pdf "Click to open in new window")

  GAO-09-3SP. United States Government Accountability Office. Applied Research and Methods. March, 2009.
* (SWEREF-461)

  [Cost Estimation of Software Intensive Projects: A Survey of Current Practices.](https://dl.acm.org/citation.cfm?id=256780 "Click to open in new window")

  Jairus Hihn and Hamid Habib-agahi, Jet Propulsion Lab., California Inst. of Technol., Pasadena, CA. 1991.
* (SWEREF-567)

  [Know How Your Software Measurement Data Will Be Used](https://llis.nasa.gov/lesson/1772 "Click to open in new window")

  Public Lessons Learned Entry: 1772.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains the following lessons learned related to cost estimation:

### **1.Know How Your Software Measurement Data Will Be Used. Lesson Number 1772[567](#_tabs-<p></p>):**

When software measurement data used to support cost estimates is provided to NASA by a project without an understanding of how NASA will apply the data, discrepancies may produce erroneous cost estimates that disrupt the process of project assessment and approval. Major flight projects should verify how NASA plans to interpret such data and use it in their parametric cost estimating model and consider duplicating the NASA process using the same or a similar model before submission.

### **2. Late and Incomplete Flight Software (FSW) Delivery**

**Incident:**  
The Psyche mission experienced an eight‑month late delivery of the final GNC flight software build, with hundreds of control parameters and fault protection behaviors still undefined. This delay, combined with numerous unresolved software issues, contributed directly to the missed 2022 launch opportunity. citeturn1search1.page21

**Lesson Learned:**

* **Early Software Definition & Maturity:** Mission‑critical software requirements, parameters, and behaviors must be fully defined and matured early to prevent cascading delays.
* **Rigorous Defect Disposition:** “Use‑as‑is” and unverified failure dispositions must undergo strict technical review to prevent acceptance of excessive residual risk. citeturn1search1.page22

**Implication:**  
Delays and ambiguity in software maturity directly threaten launch schedules, increasing cost, workforce strain, and mission‑risk exposure.

## 6.2 Other Lessons Learned

* Other Lessons Learned from experience (Hihn, Jairus M. JPL. 818.354.1248) and the JPL Cost Estimation Handbook include the following concepts:
  + Keep your history.  
    - Keep the basis of estimates (BOE) and cost data to support future analogies.
    - Keep data on your estimation vs. actual performance.
    - For incremental deliveries, the best data you have is what it took to get the job done on the earlier deliveries.

* + When the budget is cut, descope the effort.

* + When in sales mode, there is tremendous pressure to be optimistic about the cost and capability to sell the job.

* + Budget 'bogies' get set very early in the life cycle. Sometimes based on casual conversations.
    - You will typically get held to this number!

* + Software estimation is fundamentally an uncertain business under the best of conditions.

* + Common causes of cost growth. Historically, there is a pattern of being overly optimistic in cost estimates by not taking sufficient account for the following:
    - Changes and increases in scope.
    - Concurrent hardware development.
    - Inability to scope software functionality due to inadequate project definition.
    - Software is used for risk mitigation but never planned for upfront.
    - Software is the system complexity sponge.
    - Test Bed and simulator development, availability, and maturity.
    - Optimistic software inheritance assumptions.
    - Is anything new or being done for the first time?
    - Developing Technologies.
    - Autonomy.
    - Precision landing.
    - Hazard avoidance.
    - Design.
    - Language.
    - Tools.
    - Development environment.
    - Processes.
    - Customer or sponsor-initiated changes.
* In addition to these Lessons Learned, Chapter 12 of the GAO Cost Estimating and Assessment Guide, Best Practices for Developing and Managing Capital Program Costs (GAO-09-3SP) [419](#_tabs-<p></p>), discusses problems with underestimating software costs, including this excerpt from a case study, "The original estimate for the Space-Based Infrared System for nonrecurring engineering, based on experience in legacy sensor development and assumed software reuse, was significantly underestimated. Nonrecurring costs should have been two to three times higher, according to historical data and independent cost estimators. Program officials also planned on savings from simply rehosting existing legacy software, but those savings were not realized because all the software was eventually rewritten. It took 2 years longer than planned to complete the first increment of software."
* Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:
  + [Project plans and estimates need to be updated based on requirement changes](https://software.gsfc.nasa.gov/lesson-details/58/). **Lesson Number 58**: The recommendation states: "Project plans and estimates need to be updated based on requirements changes."
  + [Responding to cost/schedule/performance challenges may require hard choices](https://software.gsfc.nasa.gov/lesson-details/154/). **Lesson Number 154**: The recommendation states: "Responding to cost/schedule/performance challenges may require hard choices."

# 7. Software Assurance

**SWE-015 - Cost Estimation**

3.2.1 To better estimate the cost of development, the project manager shall establish, document, and maintain:

1. 1. Two cost estimate models and associated cost parameters for all Class A and B software projects that have an estimated project cost of $2 million or more.
   2. One software cost estimate model and associated cost parameter(s) for all Class A and Class B software projects that have an estimated project cost of less than $2 million.
   3. One software cost estimate model and associated cost parameter(s) for all Class C and Class D software projects.
   4. One software cost estimate model and associated cost parameter(s) for all Class F software projects.

This requirement ensures appropriate, consistent, and traceable cost estimation practices across software projects based on their classification, size, and complexity. Software Assurance (SA) personnel have the responsibility to verify the accuracy, completion, and compliance of cost estimates, including ensuring Software Assurance and software safety costs are included as part of the process.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the required number of software cost estimates are complete and include software assurance cost estimate(s) for the project, including a cost estimate associated with handling safety-critical software and safety-critical data.

## 7.2 Software Assurance Products

### 7.2.1 Software Assurance Cost Estimate Report

**Purpose**: Ensures SA costs and software safety costs are estimated and included in the total project software cost.  
**Contents**:

* Detailed breakdown of SA costs, which may include:
  + SA personnel hours for audits, reviews, safety activities, and analyses.
  + Costs for SA tools (e.g., static analysis tools, risk tracking software).
  + SA planning and auditing activities.
  + Support for safety-critical software evaluations (if applicable).
  + Grassroots estimate or percentage approximation (e.g., 5-6% of total software cost).
* Explanation of cost estimation methodology (e.g., historical comparison, grassroots estimation).
* Alignment of SA cost estimates with the overall cost model(s).
* Evidence of communication with the project team to integrate the SA cost estimate into the primary project estimate.

### 7.2.2 Cost Estimate Completeness Assessment Report

**Purpose**: Evaluates whether the correct number of cost estimates has been completed for the project, based on its classification and expected cost, as required by this requirement.  
**Contents**:

* Verification that the project generated:
  + **Two cost estimate models with parameters** for all Class A and B projects with software costs of $2M or more.
  + **One cost estimate model with parameters** for all Class A and B projects with software costs of less than $2M.
  + **One cost estimate model** for all Class C, D, and F projects.
* Confirmation that cost estimates align with project classification (Class A, B, C, D, or F) per NASA classification criteria.
* Issues, risks, or missing cost estimate models identified during the assessment.
* Recommended resolutions and actions tracked to closure (e.g., generation of missing estimates).

### 7.2.3 SWE-151 Compliance Assessment

**Purpose**: Assesses the completeness and quality of each cost estimate against [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions).  
**Contents**:

* Completed review checklist of SWE-151 conditions:
  + Lifecycle coverage.
  + Project size and attribute assessment (e.g., size, functionality, criticality, risk).
  + Cost of technology maturation.
  + Inclusion of risk and cybersecurity impacts.
  + Completeness of SA and safety cost inclusion.
  + Inclusion of direct costs (e.g., procurement, travel, training).
* Documentation of areas where cost estimates are non-compliant with SWE-151.
* Recommendations for enhancements and resolutions for missing elements, tracked to closure.

## 7.3 Metrics

Metrics track the completeness, accuracy, and trends in cost estimates over the lifecycle of software projects.

### Key Metrics

**1. Completeness Metrics:**

* **% of Projects with Required Number of Cost Estimates:**
  + Tracks adherence to the required number of cost estimates for each Class (A, B, C, D, F).

**2. Resource Allocation Metrics:**

* **Planned SA Resource Allocation vs. Actual Allocation:**
  + Monitors alignment between planned and actual effort spent for SA tasks.

**3. Cost Estimate Trends:**

* **Comparison of Initial SA Cost Estimates vs. Final Costs:**
  + Tracks changes in SA cost estimates across lifecycle phases, including assumptions and actual values.

**4. Compliance Metrics:**

* **% of Cost Estimates Fully Meeting SWE-151 Conditions:**
  + Measures compliance with cost estimation requirements (e.g., lifecycle coverage, risks and uncertainties).

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

By following these steps, Software Assurance personnel can ensure cost models satisfy this requirement, including proper SA cost inclusion, lifecycle coverage, and adherence to project classification criteria. This approach improves cost estimation processes and supports better project planning and execution.

### Step 1: Confirm the Correct Number of Cost Models

* Ensure the project has generated and documented the required number of cost estimate models:
  + Class A/B projects over $2M: Two models with associated parameters.
  + Class A/B projects under $2M, and Class C/D/F projects: One model with associated parameters.
* Access cost estimates submitted to project repositories, verify their presence, and confirm alignment with the requirement.
* Track any missing or incorrect cost estimates as risks and follow up with the project team until resolution.

### Step 2: Develop and Validate SA Cost Estimates

* Independently develop an estimate for SA and software safety costs, accounting for:
  + Lifecycle phases requiring SA support (e.g., audits, testing, code analysis).
  + Expected effort for safety-critical evaluations, if applicable.
  + Tools, training, travel, and documentation preparation costs.
  + Grassroots or percentage-based estimates (e.g., 5-6% of overall software cost).
* Verify that developed SA cost estimates are included in the project's cost model. Address gaps in inclusion with the project manager.

### Step 3: Assess Cost Models for Completeness

* Confirm that cost estimates satisfy all conditions outlined in [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions):
  + Cover the entire software lifecycle, including development, operations, and retirement.
  + Incorporate size, functionality, complexity, risk, and other selected project attributes.
  + Include cost implications of technology (e.g., tool maturation, process immaturity, learning curves).
  + Incorporate risks, including cybersecurity threats.
  + Add direct costs (e.g., procurements, training, travel).
* Document any issues identified during the assessment and track their resolution with the project.

### Step 4: Verify Submission to Repositories

* Ensure cost estimates (including SA-specific estimates) are submitted to:
  + Project repositories as required.
  + SA repositories for independent review and lessons learned.
* Confirm submission completeness and periodic updates after major milestones (e.g., SDR, PDR, CDR).

### Step 5: Track Metrics and Evaluate Trends

* Continuously monitor and report metrics such as:
  + Planned vs. actual resource allocation for SA costs.
  + Changes in lifecycle cost estimates impacting SA budgets.
* Use lessons learned to improve the accuracy of future cost estimation activities.

Confirm the cost estimate satisfies the conditions in [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) - Confirm that the project cost estimate(s) contains all of the required information per [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions). Track to closure with the project any missing information.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-142 - Software Cost Repositories](/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence ensures traceability, accountability, and compliance with the requirement to establish and document cost estimates.

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

### 8.1.1 Verification of Complete Cost Estimates:

* Documents showing the correct number of cost estimate models have been created based on project classification and software cost thresholds.
* Repository records (or archived emails) confirming cost estimate submissions.

### 8.1.2 Compliance with SWE-151 Criteria:

* Cost estimates that demonstrate:
  + Coverage of the entire lifecycle.
  + Inclusion of selected project attributes (e.g., software size, reuse, modified code, risk).
  + Incorporation of technology costs (e.g., tool maturity, learning curves).
  + Inclusion of SA and software safety costs.
  + Inclusion of direct costs such as training and procurement.
* Review notes or reports showing evaluation of SWE-151 conditions.

### 8.1.3 Evidence of SA Cost Estimation Submission:

* Documentation showing SA cost estimates were created, verified, and included in the overall cost model(s).
