# SWE-174 - Software Planning Parameters

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695516. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters

SWE-174 - Software Planning Parameters

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695516)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695516&showCommentArea=true&showComments=true#addcomment)

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

3.2.3 The project manager shall submit software planning parameters, including size and effort estimates, milestones, and characteristics, to the Center measurement repository at the conclusion of major milestones.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-174 History

SWE-174 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.2.3 The project manager shall submit software planning parameters, including size and effort estimates, milestones, and characteristics, to the Center measurement repository at the conclusion of major milestones. |
| Difference between C and D | No change |
| D | 3.2.3 The project manager shall submit software planning parameters, including size and effort estimates, milestones, and characteristics, to the Center measurement repository at the conclusion of major milestones. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

NASA software measurement programs are designed to provide specific information necessary to manage software products, projects, and services.  For these programs to be current and accurate, certain center measurements (such as size and effort estimates, milestones, and characteristics) are provided to the Center repository at the end of the major project milestones. Defined software measurements are used to make effective management decisions by Center Management. Historical measurement data can also be used to improve aspects of future projects such as cost estimation.

Submitting software planning parameters, including size and effort estimates, milestones, and characteristics, to the Center measurement repository at the conclusion of major milestones is an essential practice for fostering **data-driven project management**, **increasing organizational knowledge**, and **enhancing future estimations and planning activities**. This requirement aligns with NASA’s commitment to continuous improvement and ensuring accountability in project execution.

Submitting software planning parameters to the Center measurement repository at milestone reviews ensures that NASA projects are managed with **transparency**, **accountability**, and a **commitment to continuous learning**. By leveraging historical data for future planning and fostering a culture of measurement and analysis, NASA can achieve greater accuracy in estimations, improve software project execution, and advance mission success. This practice directly supports NASA's mission of delivering high-quality software systems while upholding fiscal responsibility and operational excellence.

## 2.1 Key Reasons for this Requirement

### 2.1.1 Improve Accuracy of Future Estimates

* Project data such as software size, effort estimates, milestones, and actual outcomes provide valuable input for refining cost estimation models, tools, and methods.
* Historical data enables Centers to establish realistic benchmarks for similar future projects and supports analogy-based and data-driven estimation efforts.
* Reliable planning data helps reduce uncertainty in future projects, leading to better forecasting and resource allocation.

### 2.1.2 Enhance Organizational Knowledge and Best Practices

* Capturing software planning parameters at major milestones ensures that lessons learned, project performance data, and key decisions are systematically documented for future reference.
* By consolidating this information in the Center measurement repository, the organization creates a knowledge base that informs future projects and enables better decision-making.
* Over time, patterns and trends can be analyzed to identify areas for improvement and establish best practices across the Center.

### 2.1.3 Facilitate Accountability and Transparency

* Submission of planning parameters allows for an objective comparison between initial estimates and actual project performance at each milestone. This transparency ensures accountability for both project managers and stakeholders.
* It highlights discrepancies or deviations from the plan, such as underestimations of effort or unanticipated schedule delays, and provides opportunities to identify root causes and implement corrective actions.

### 2.1.4 Enable Project and Process Improvement

* By collecting milestones, size, and effort data at major project reviews, Centers can evaluate the effectiveness of project management and software development practices at each stage of the lifecycle.
* This information enables NASA to assess the efficiency of processes, identify bottlenecks, and recommend improvements for future efforts.
* It also provides an opportunity to adjust practices to mitigate recurring issues or enhance overall project performance.

### 2.1.5 Support Compliance with NASA Standards

* Submitting planning data to the Center measurement repository ensures compliance with NASA’s policies for process measurement, analysis, and continuous improvement as outlined in **NPR 7150.2** [083](#_tabs-<p></p>) and related guidance.
* The requirement supports NASA’s efforts to maintain consistency and standardize practices across different Centers, contributing to high-quality, predictable outcomes.

### 2.1.6 Facilitate Data-Driven Risk Management

* Regular updates of project parameters at major milestones enhance visibility into potential risks or emerging challenges. For example:
  + If actual size or effort parameters deviate significantly from initial expectations, this may flag emerging risks earlier in the lifecycle.
* Collecting and analyzing such data across multiple projects enhances NASA's capability for systemic risk identification and mitigation.

### 2.1.7 Contribute to NASA-Wide Metrics and Reporting

* A centralized measurement repository enables NASA Centers to track contributions to broader agency-level performance metrics.
* Aggregating reporting data allows for comparisons between projects or programs and provides insight into NASA's overall project portfolio performance against strategic goals.

# 3. Guidance

Accurate software planning parameters are essential for maintaining consistency, ensuring accountability, and improving decision-making throughout the software development lifecycle. The submission and documentation of these software parameters at major milestones not only help track project progress but also provide critical inputs for cost modeling, risk assessment, and performance evaluation. The following updated guidance addresses NASA software planning requirements more comprehensively and connects them to relevant references and practices.

The submission of software planning parameters to the Center Measurement Repository is vital for maintaining visibility into project performance, improving future estimations, and fostering organizational learning. Regular updates within the SDP/SMP and adherence to lifecycle milestone expectations ensure accurate tracking of progress and compliance with NASA standards. By following this guidance, project teams can achieve greater accountability, consistency, and efficiency throughout the software development lifecycle.

## 3.1 Minimum Software Planning Parameters

At a minimum, the following software planning parameters must be defined, updated, and submitted at major milestones in accordance with the **Software Development or Management Plan (SDP/SMP)***.* See [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)

#### **Software Size**

* **Definition**: Tracks planned and actual metrics such as lines of code, functional units, modules, or other size-based measures.
* **Purpose**: Software size is a fundamental input for estimating effort, schedule, and cost, while also providing insight into project complexity.
* **Considerations**: Regularly update size metrics in alignment with changes to requirements and scope.

#### **Effort**

* **Definition**: Includes planned and actual workforce size (e.g., number of full-time equivalents) and hours allocated to the project.
* **Purpose**: Effort measurements help gauge team productivity and identify deviations from baseline estimations.

#### **Milestones**

* **Definition**: Includes planned and actual schedule dates for key project phases, including start dates, intermediate milestones, and completion.
* **Purpose**: Milestone tracking facilitates schedule management and highlights variances that may require corrective action.

#### **Characteristics**

* **Definition**: Unique features that describe the project's scope, objectives, constraints, and work products (also referred to as "software attributes").
* **Purpose**: These characteristics enable proper identification of the project, assist with cost modeling, and provide inputs for planning and risk assessments.

## 3.2 Detailed Guidance on Software Characteristics

Software characteristics (or attributes) provide essential insights for project management and cost estimation. These characteristics uniquely define the software's scope, complexity, development environment, and constraints.

#### **Examples of Software Characteristics:**

1. **Required Software Reliability**: The degree of software dependability required for mission success.
2. **Database Size**: The size and structure of any databases the software must manage.
3. **Product Complexity**: The intricacy or difficulty associated with the software.
4. **Developed for Reusability**: Effort required to make the software reusable across projects.
5. **Documentation Needs**: The extent and quality of documentation required across lifecycle phases.
6. **Execution Time Constraints**: The time constraints within which the software must perform critical operations.
7. **Analyst/Programmer Capability**: Skill levels among personnel assigned to the project.
8. **Applications, Language, and Tool Experience**: Familiarity of the development team with relevant applications, development tools, and programming languages.
9. **Multisite Development**: Additional effort required when teams are distributed across multiple locations.
10. **Personnel Continuity**: Consideration of staffing stability and turnover.
11. **Platform Volatility**: Variability or change expected in the hardware platform during development.
12. **Software Tools**: The tools used to assist software development and their effectiveness.
13. **Precedentedness**: Whether the project is a continuation of similar or previously developed systems (versus a novel implementation).

These attributes should be tailored to the specific project and documented to provide a full profile of its requirements and constraints.

## 3.3 Repository Submission Requirements

At the conclusion of each major project milestone, the planning parameters must be submitted to the **Center Measurement Repository**, as defined in [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan). The submission includes both planned and actual values:

* **Planned Parameters**: The original estimates established during the project planning phase.
* **Actual Parameters**: Metrics measured and confirmed during project execution.

This systematic submission helps maintain visibility into project performance and supports future project planning by providing historical data to the repository.

In addition, **cost and effort estimates** should be captured at the conclusion of the project to document deviation from planned measures and to refine cost models.

## 3.4 Documentation and Updates

#### **Software Development or Management Plan (SDP/SMP)**

As established in topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) , the SDP/SMP is the primary document for recording software planning parameters. This plan:

* **Provides Insight**: Outlines processes, tools, approaches, schedules, resources, and constraints to be followed during development.
* **Monitors Progress**: Serves as a living document that tracks updates in parameters as the project evolves.
* **Details Activities**: Includes system software deliverables, project documentation, schedule updates, resources requirements, and all lifecycle activities.

To ensure successful implementation:

* **Keep the Plan Updated**: Regularly revise the SDP/SMP to reflect new information learned during lifecycle milestones and ensure alignment with current project conditions.
* **Identify Scope Deviations**: Use updates to assess the impact of project scope changes or requirement revisions.

#### **Maturity of Lifecycle Products**

Refer to topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) to understand the expected maturity of the documented parameters at each milestone and ensure the consistency of submissions.

## 3.5 Benefits of Tracking Software Planning Parameters

#### **Improved Estimation Accuracy**

* Historical data from submissions are used to refine cost models, effort estimation techniques, and scheduling practices for future projects, contributing to more realistic planning.

#### **Enhanced Accountability**

* Tracking planned vs. actual data ensures transparency and allows project teams to identify root causes for deviations, enabling corrective measures.

#### **Faster Decision-Making**

* Documented characteristics and attributes enable quicker analysis of project risks, bottlenecks, and performance constraints, facilitating informed decisions.

#### **Better Organizational Learning**

* Capturing parameter data in the repository creates a valuable knowledge base that contributes to continuous improvement and informs future projects.

## 3.6 Best Practices for Managing Software Planning Parameters

1. **Start Early**: Define planning parameters during the initial project phases to provide a strong foundation for tracking metrics.
2. **Update Regularly**: Revise parameters at every major milestone to reflect current project realities and avoid gaps in reporting.
3. **Collaborate**: Ensure coordination between the software acquirer and provider to maintain alignment in documented parameters.
4. **Use Standardized Formats**: Ensure submissions to the repository follow a consistent template or structure as defined by SDP/SMP guidelines.
5. **Automate Where Possible**: Leverage software tools to track size, effort, schedules, and other planning parameters for streamlined updates and submission.

## 3.7 Additional Guidance

Additional guidance may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Estimation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Estimation) |

# 4. Small Projects

Small projects, while less resource-intensive compared to larger initiatives, can still benefit significantly from capturing and tracking software planning parameters. Each Center should define criteria for what qualifies as a "small project," ensuring guidance is tailored appropriately to the project's scope and complexity. The decision to capture and track these parameters should be based on the value they provide to the project, organization, and future initiatives.

Capturing and tracking software planning parameters for small projects may not always seem proportionate to the project's size, but it provides valuable insights for both individual projects and broader organizational goals. Centers that frequently handle small projects can leverage this data to refine processes, improve estimation accuracy, and contribute to NASA-wide knowledge sharing. By scaling tracking efforts appropriately and balancing the benefits with the effort required, organizations can ensure that even small projects are managed effectively with optimal resource application and accountability.

## 4.1 Importance of Tracking Software Planning Parameters for Small Projects

Though small projects may have limited budgets, scopes, or lifespans, tracking software planning data remains valuable for several reasons:

#### **Value for Individual Projects:**

* **Improved Visibility:** Capturing data ensures a clear understanding of project progress, enabling teams to identify risks and deviations early, even in smaller efforts.
* **Optimized Decision-Making:** Collected data provides concrete insights for adjusting resources, schedules, and tasks while ensuring the project stays aligned with its goals.
* **Accountability:** Documented planning parameters allow project managers to demonstrate performance against planned objectives to stakeholders.

#### **Value for Organizations Handling Small Projects:**

* **Future Business Growth**: If an organization primarily delivers small projects, consistent data collection can serve as a foundation for improving estimation accuracy and showcasing its capabilities to future clients or stakeholders.
* **Process Improvement**: Trends derived from historical planning data can help refine workflows, improve efficiency, and mitigate recurring challenges.
* **Contributing to NASA Knowledge Sharing**: Even small-scale data collection contributes to the Center measurement repository and the larger NASA ecosystem, enhancing organizational learning and knowledge sharing across projects.

## 4.2 Tailoring Data Collection for Small Projects

The scope and effort for capturing and tracking software planning parameters should be scaled appropriately for small projects to avoid unnecessary overhead while still gaining valuable insights. Consider the following guidelines:

### 4.2.1 Focus on Critical Metrics:

For small projects, collect planning parameters essential to the project's success, such as:

* **Software Size:** Focus on straightforward measures like estimated lines of code or functional modules. Avoid overly detailed size metrics that may increase complexity without adding much value.
* **Effort:** Capture planned workforce hours and actual hours worked, primarily for resource planning and productivity analysis.
* **Milestones:** Track key dates (start, intermediate, and completion milestones) for schedule visibility and accountability.
* **Characteristics:** Document major features and attributes that uniquely define the software's development, making it easier to model and learn from similar projects in the future.

### 4.2.2 Simplify the Reporting Process:

* Use lightweight reporting processes and tools that minimize administrative burden (e.g., simple spreadsheets, small-scale project management tools, or built-in tracking within the SDP/SMP).
* Automate where possible, especially for effort tracking and milestone updates.

### 4.2.3 Prioritize Cost-Benefit Analysis:

* Evaluate whether the effort of tracking data for a small project aligns with the project's value to the organization. For projects that are unlikely to recur or have minimal complexity, the benefits of tracking may outweigh the effort required.
* For organizations focused exclusively on small projects, prioritize data collection to improve long-term organizational efficiency and accuracy in planning similar projects.

## 4.3 Streamlining Tracking for Small Projects

Efforts for tracking software planning parameters should be proportionate to the project's scope. The following approaches are recommended to minimize effort while maximizing benefits for small projects:

### 4.3.1 Collaborative Discussions:

* Engage stakeholders early to determine which metrics the organization finds most valuable for small projects. For example, certain Centers may prioritize schedule adherence over detailed size or cost metrics.
* Ensure alignment with organizational goals, such as improving process maturity or cost-efficiency.

### 4.3.2 Replicate Past Successes:

* Leverage data from analogous small projects to reduce the burden of estimation. Historical trends not only provide benchmarks but also accelerate the data collection process for similar efforts.
* Reuse templates or reporting formats proven effective in prior small project implementations.

### 4.3.3 Scale Plans and Documentation:

* Simplified Software Development or Management Plans (SDP/SMP) are often sufficient for small projects. Focus on essential elements such as basic schedules, high-level resource planning, and workflow descriptions.
* Only update plans at major milestones or when significant scope changes occur to reduce effort.

## 4.4 Benefits of Capturing Data Even for Small Projects

Organizations should determine the value of tracking software planning parameters based on long-term goals. For those primarily focused on small projects, data collection plays a critical role in process improvement and business growth. Examples of benefits include:

#### **For the Project:**

1. **Schedule Accuracy:** Tracking milestones helps ensure timely delivery and flag potential delays early.
2. **Effort Optimization:** Capturing planned and actual effort helps refine resource allocation and identify inefficiencies within the team.
3. **Cost Management:** Documenting actual effort and workforce hours aids in preventing budget overruns, even in smaller scopes.

#### **For the Organization:**

1. **Trend Analysis:** Aggregated data from small projects reveals patterns that can inform realistic future planning and avoid systemic issues.
2. **Benchmarking:** Historical data provides a basis for comparing new projects to past successes or failures, increasing confidence in estimates.
3. **NASA Repository Contribution:** Small projects play a vital role in enriching the organization's repository of measurement data, supporting other Centers and NASA-wide learning.

## 4.5 Considerations for Centers Handling Small Projects

Each Center should evaluate the impact and practicality of capturing software planning data for small projects based on its unique circumstances and priorities. When determining the extent of data collection:

* **Define "Small Project":** Establish clear criteria for identifying small projects. Examples may include budget thresholds, software size limits, or mission importance levels.
* **Assess Organizational Patterns:** If the majority of an organization's work consists of small projects, data collection becomes more critical for ensuring consistency, improving efficiency, and establishing credibility across projects.
* **Balance Effort and Value:** Avoid collecting extensive data unless it directly supports the small project's objectives or long-term organizational goals.

## 4.6 Best Practices for Small Project Data Collection

1. **Tailor Data Requirements:** Focus only on key parameters applicable to both the small project's scope and the organization's priorities. Avoid collecting excessive or overly detailed data.
2. **Reduce Burden:** Use simplified methods for tracking and submitting data, such as using tools already integrated into the project workflow where possible.
3. **Learn from History:** Reference historical data from similar small projects within the organization to guide current estimation and planning.
4. **Update at Key Milestones:** Limit updates to major milestones (e.g., start, midpoint, and completion) to avoid unnecessary administrative overhead.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-174 - Software Planning Parameters**

3.2.3 The project manager shall submit software planning parameters, including size and effort estimates, milestones, and characteristics, to the Center measurement repository at the conclusion of major milestones.

This requirement ensures that key metrics and analytics from software planning activities, including size, effort, milestones, and project characteristics, are captured and submitted to the Center measurement repository for lessons learned, benchmarking, and future project planning purposes. Software Assurance (SA) personnel must verify the collection, accuracy, and submission of these planning parameters and ensure that SA-specific planning data is also submitted to the SA organizational repository.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that all the software planning parameters, including size and effort estimates, milestones, and characteristics, are submitted to a Center repository.

2. Confirm that all software assurance and software safety software estimates and planning parameters are submitted to an organizational repository.

## 7.2 Software Assurance Products

### 7.2.1. Software Assurance Planning Issues & Risks Report

**Purpose**: Documents any identified issues and risks associated with the accuracy, completeness, and submission of software planning parameters to the Center measurement repository.  
**Contents**:

* List of issues or risks discovered during SA assessments of size, effort estimates, milestones, and characteristics.
* Impact analysis of risks associated with delays in submitting software planning data or conflicting metrics in planning parameters (e.g., unrealistic size estimates, milestone misalignment).
* Recommended actions to mitigate risks and resolve identified issues.
* Documentation of communication to management highlighting unresolved risks or issues.

### 7.2.2. Software Planning Metrics Submission Report

**Purpose**: Verifies that software planning data is collected and submitted to the Center repository at major milestones (e.g., SDR, PDR, CDR, TRR).  
**Contents**:

* Summary of submitted software planning parameters:
  + Size estimates (e.g., source lines of code (SLOC), function points).
  + Effort estimates (e.g., person-hours, resource allocation).
  + Milestone data (planned and actual dates).
  + Software characteristics (e.g., reliability metrics, complexity ratings).
* Record of data submission to the Center measurement repository, including submission dates and any required updates.
* Verification of submission completeness by SA personnel.

### 7.2.3. Software Assurance Repository Submission Summary

**Purpose**: Documents SA-specific planning data submitted to the organizational SA repository for lessons learned and benchmarking purposes.  
**Contents**:

* SA planning parameters, including:
  + Initial vs. final SA cost estimates.
  + Resource allocation for SA and safety activities (planned vs. actuals).
  + SA effort estimates (e.g., focus areas like audits, analysis, reviews).
  + SA milestones (e.g., SDR compliance audits, TRR validation reports).
  + SA metrics (e.g., number of peer reviews conducted, number of defects identified).
* Record of submission dates and updates during major milestones and project closeout.
* Summary of findings from SA repository periodic reviews or audits.

### 7.2.4. SA Repository Audit Report

**Purpose**: Documents periodic audits of the SA organizational repository for completeness and traceability of previously submitted project data.  
**Contents**:

* Audit findings highlighting missing or incomplete SA data from past milestones.
* Identification of gaps between planned and actual SA metrics and effort estimates.
* Recommendations to improve data submission processes for future projects.

## 7.3 Metrics

Metrics allow Software Assurance personnel to track trends and discrepancies in software planning and submission activities, aiding corrective actions and future planning. Key metrics include::

### 7.3.1 Cost Estimate Metrics:

* **Comparison of Initial vs. Final SA Cost Estimates:**
  + Tracks differences between initial cost estimate assumptions and actual expenditures, highlighting trends and lessons learned.
* **Trend of SA Cost Estimates Throughout Lifecycle:**
  + Monitors changes to SA cost estimates over time, identifying early trends in cost overruns or resource adjustments.

### 7.3.2 Resource Allocation Metrics:

* **Planned SA Resource Allocation vs. Actual Allocation:**
  + Tracks resource usage discrepancies, identifying inefficiencies or gaps.

### 7.3.3 Software Planning Parameters Metrics:

* **# of Detailed Software Requirements vs. Estimated SLOC:**
  + Tracks requirement volatility versus expected project size (e.g., changes in feature creep, SLOC growth).
* **% of Milestones Met vs. Planned Milestones:**
  + Measures project milestone adherence.

### 7.3.4 Repository Submission Metrics:

* **Repository Completeness Metric:**
  + Tracks the percentage of planned vs. actual data submitted to both the Center and SA organizational repositories.
* **Audit Metrics for Repository Completeness:**
  + Monitors findings from repository audits (e.g., missing or incomplete submissions).

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

By aligning SA activities with project metrics submission requirements outlined in this requirement, Software Assurance personnel contribute to accuracy, traceability, and future project improvements, ensuring compliance and transparency across the organization. Software Assurance Personnel Activities for Compliance include:

#### **Step 1: Confirm Submission of Software Planning Parameters to the Center Repository**

* Verify that software planning parameters (size estimates, effort estimates, milestone data, characteristics) have been submitted to the Center measurement repository at the end of major milestones (e.g., SDR, PDR, CDR, TRR).
* Cross-check submission completeness by reviewing:
  + Submitted SLOC estimates, including planned growth metrics.
  + Effort estimates tied to specific software activities (e.g., development, testing).
  + Milestone alignment between planned and actual dates.
  + Documentation of software characteristics (e.g., complexity ratings, team cohesion).
* Notify management if there are missing or inconsistent submissions during compliance reviews.

#### **Step 2: Collect and Submit SA Planning Data to SA Organizational Repository**

* Ensure SA-specific estimates, metrics, and milestones are submitted to the SA organizational repository at major milestones and project closeout.
* Review repository contents for completeness through regular audits.
* Submit lessons learned and analysis of SA metrics (e.g., cost estimate discrepancies, audit findings) to improve the repository’s usefulness for future projects.

#### **Step 3: Evaluate Software Planning Documentation**

* Confirm that software planning documentation includes:
  + Software metrics and measurements to be collected.
  + Software project size and effort estimates.
  + Planned and actual milestone dates reflecting adherence to the software schedule.
  + Software characteristics influencing planning (e.g., risk management, performance needs).
* Identify missing data elements and recommend corrective actions to project management.

#### **Step 4: Periodic Repository Audits**

* Conduct annual or lifecycle milestone audits of both Center and SA organizational repositories to verify completeness:
  + Identify all submitted data and flag missing or incomplete information.
  + Ensure estimates and metrics accurately match lifecycle performance.

### 7.4.1 Examples of Software Planning Parameters to Collect:

* **Size Estimates:** SLOC, function points, feature scope breakdown.
* **Effort Estimates:** Person-hours/days, resource allocation (staffing).
* **Milestone Data:** Planned vs. actual dates, critical milestones (e.g., SDR, PDR, CDR, TRR).
* **Characteristics:** Reliability metrics, complexity ratings, usability parameters, risk factors.
* **SA and Safety Metrics:** Number of audits, peer reviews, issues identified, resource usage for assurance tasks.

## 7.5 Additional Guidance

Additional guidance may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence ensures compliance with the requirement by verifying the submission of required software planning parameters and SA estimates to respective repositories.

Objective evidence includes auditable records such as submission logs, planning artifacts, reviews, and audit reports to verify compliance with the submission of software planning parameters.

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

### 8.1.1. Submission Confirmation for Center Repository:

* Documentation verifying that software planning parameters were submitted after major milestones (e.g., SDR, PDR, CDR).
* Submission logs or confirmation emails showing size estimates, effort estimates, milestones, and characteristics data were uploaded.
* Records demonstrating updates to submission documentation after major milestone changes.

### 8.1.2. Submission of SA-Specific Planning Data:

* Evidence that SA planning data (e.g., SA metrics, estimates, milestones) was submitted to the SA organizational repository.
* Confirmation that SA deliverables were linked to the Center repository data where applicable (e.g., SA artifacts aligned with software schedule or risk assessments).

### 8.1.3. Software Planning Documentation:

* Approved planning artifacts, including:
  + Software Requirements Specifications (SRS) with project size estimates.
  + Staffing plans reflecting effort estimates for SA and software safety tasks.
  + Project schedules with milestone data (planned and actuals).
  + Software characteristics analysis (e.g., reliability estimates, risk management factors).
