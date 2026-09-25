# SWE-142 - Software Cost Repositories

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695500. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories

SWE-142 - Software Cost Repositories

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695500/SWE-142+-+Software+Cost+Repositories#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695500)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695500&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

## 1. Requirements

2.1.5.10 For Class A, B, and C software projects, each Center Director, or designee, shall establish and maintain software cost repository(ies) that contains at least the following measures: 

a. Planned and actual effort and cost.  
b. Planned and actual schedule dates for major milestones.  
c. Both planned and actual values for key cost parameters that typically include software size, requirements count, defects counts for maintenance or sustaining engineering projects, and cost model inputs.  
d. Project descriptors or metadata that typically includes software class, software domain/type, and requirements volatility.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-142 History

SWE-142 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 2.1.3.12 For Class A, B, and C software projects, each Center Director shall establish and maintain a software cost repository(ies) that contains at least the following measures:  a. Planned and actual effort and cost. b. Planned and actual schedule dates for major milestones. c. Both planned and actual values for key cost parameters that typically include software size, requirements count, defects counts for maintenance or sustaining engineering projects, and cost model inputs. d. Project descriptors or metadata that typically includes software class, software domain/type, and requirements volatility. |
| Difference between B and C | Added "or designee" |
| C | 2.1.5.12 For Class A, B, and C software projects, each Center Director, or designee, shall establish and maintain software cost repository(ies) that contains at least the following measures:   1. 1. Planned and actual effort and cost.    2. Planned and actual schedule dates for major milestones.    3. Both planned and actual values for key cost parameters that typically include software size, requirements count, defects counts for maintenance or sustaining engineering projects, and cost model inputs.    4. Project descriptors or metadata that typically includes software class, software domain/type, and requirements volatility. |
| Difference between C and D | No Change |
| D | 2.1.5.10 For Class A, B, and C software projects, each Center Director, or designee, shall establish and maintain software cost repository(ies) that contains at least the following measures:   a. Planned and actual effort and cost. b. Planned and actual schedule dates for major milestones. c. Both planned and actual values for key cost parameters that typically include software size, requirements count, defects counts for maintenance or sustaining engineering projects, and cost model inputs. d. Project descriptors or metadata that typically includes software class, software domain/type, and requirements volatility. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

The establishment and maintenance of a software cost repository are critical to ensuring effective project control, accurate estimation for future projects, continuous improvement in project management, and organizational learning. This data repository serves as a centralized and reliable source for tracking, analyzing, and improving the planning and management of software projects. Below are the key reasons why this requirement is necessary.

## 2.1 Key Rationale for the Requirement

### 1. Enables Accurate Project Tracking and Oversight

Having a repository with detailed actual and planned measures, including cost, schedule, and parameter data, allows Center Directors, project managers, and engineers to:

* **Track project progress**: Compare planned and actual data to identify deviations early.
* **Mitigate risks**: Detect cost or schedule overruns and understand their potential downstream impacts on resources and mission objectives.
* **Improve accountability**: Centralized, well-maintained data reinforces the need for accurate reporting and operational transparency, especially for high-visibility Class A, B, and C projects.

*Example*: If actual effort metrics consistently exceed planned estimates, resource constraints or underestimations can be swiftly corrected.

### 2. Supports Data-Driven Decision-Making

A software cost repository provides the quantitative data necessary for proactive, objective decision-making across the software lifecycle. These decisions include budget adjustments, resource optimization, schedule realignments, or scope moderation.

**Key Benefits**:

* Ensure that decisions are supported by historical and real-time data rather than subjective speculation.
* Evaluate the trade-offs between cost, schedule, and quality when encountering constraints.
* Justify funding and staffing changes based on data trends.

### 3. Enhances Future Project Planning and Cost Estimation

A repository serves as a valuable knowledge base for planning future software projects. By analyzing historical data, teams can generate realistic estimates of cost and schedule and understand typical performance trends or challenges.

#### Benefits for Future Projects:

* Provides baseline comparisons for new efforts of similar class, size, or type.
* Serves as input to cost models (e.g., COCOMO II, parametric models) for more accurate forecasting of resource needs.
* Helps refine estimation processes to reduce the risk of overly aggressive schedules or underestimations.

*Example*: If past projects demonstrate that requirements counted during the planning phase increased by 20% on average during development, this trend can inform better requirements volatility assumptions in future work.

### 4. Facilitates Process Improvement

The repository is not just a tool for immediate project tracking but also a resource for learning and improving software engineering practices over time. By analyzing trends and correlations in repository data, organizations can identify systemic issues or improvement opportunities.

#### Examples of Improvement Areas:

* **Effort estimation accuracy**: If deviations between planned and actual effort are consistently large, corrective actions and refinements can be implemented for future projects.
* **Defect reduction**: Correlating defect counts with cost or software size can help drive process improvements in coding, testing, or peer review practices.

#### Organizational Benefits:

* Encourages a culture of continuous feedback and learning.
* Identifies successful strategies or common failure points for use in future development methodologies.

### 5. Facilitates NASA-Wide Analysis and Benchmarking

NASA engages in a variety of software projects across diverse domains, from missions critical to space safety (Class A) to supporting infrastructure (Class C). A consistent, detailed repository enables:

* **Agency-wide benchmarks**: Establishing norms for cost efficiency, schedule adherence, and quality.
* **Cross-project comparisons**: Identifying trends, bottlenecks, or best practices shared across different projects and Centers.
* **Mission-critical evaluation**: Bringing high-quality data to senior decision-makers regarding the health, risks, and return-on-investment for NASA’s portfolio of software development efforts.

### 6. Addresses Requirements Complexity and Volatility

Software projects often face challenges in managing scope, particularly for complex missions. By including project descriptors/metadata like software class, software domain/type, and requirements volatility, this repository captures contextual factors that influence project performance.

#### Why Metadata Matters\*\*:

* **Software class**: Helps stratify data to distinguish performance differences among critical (Class A) and less critical (Class C) efforts.
* **Software domain/type**: Allows Centers to identify domain-specific efficiencies or issues (e.g., flight software vs. ground support systems).
* **Requirements volatility**: Provides insights into how changing requirements affect cost, effort, and schedule, enabling better strategies for requirement management.

### 7. Promotes Consistency and Compliance Across Projects

Requiring the same set of planned and actual measures across all Class A, B, and C projects fosters consistency and standardization in reporting. Consistent data makes it easier to:

* Aggregate information for Center- or agency-level analysis.
* Verify compliance with NASA’s processes and standards (e.g., **NPR 7150.2**[083](#_tabs-<p></p>)).
* Ensure a complete historical record that can be audited or referenced when needed.

### 8. Improves Defect Tracking for Maintenance Projects

For sustaining engineering or maintenance-focused efforts, tracking defect counts provides critical visibility into long-term software performance and reliability. Including defect counts in the repository allows:

* Identification of high-defect areas that need redesign or additional attention.
* Analysis of defect trends over time to evaluate software stability.
* Planning for ongoing maintenance costs based on the historical defect load.

*Example*: A repository might reveal that highly volatile systems experience four times the defects post-deployment. This insight could support additional testing investment during pre-deployment for similar future projects.

## 2.2 Conclusion

This requirement ensures NASA’s software projects are supported by a rich dataset that serves multiple stakeholders:

1. **Project teams**: Gain insights into progress, risks, and areas for improvement.
2. **Center Directors and designees**: Monitor project health, resource usage, and compliance.
3. **NASA Agency**: Rely on this repository for benchmarks, process improvement, and better-informed decision-making across all Centers.

In short, a software cost repository strengthens NASA’s capacity to execute projects efficiently, deliver high-quality software, and learn from its extensive portfolio of software development efforts.

# 3. Guidance

## 3.1 Purpose of a Cost Repository

A cost repository is a centralized tool designed to capture, maintain, and analyze historical project data, enabling more accurate project estimations while fostering effective planning and cost management. It serves the following purposes:

1. **Historical Reference**
   * Provides a record of past cost estimates and actuals for comparison and analysis.
   * Enables systematic learning by identifying trends, risks, and deviations in project execution.
2. **Improved Cost Estimation Accuracy**
   * By comparing estimated costs to actual costs, organizations can refine estimation models and improve the accuracy of future cost predictions.
   * Helps assess the drivers behind cost growth or discrepancies, such as scope changes, resource constraints, or unexpected technical challenges.
3. **Planning Support Across Lifecycles**
   * Useful during various phases of project planning, including proposals, concept studies, feasibility studies, detailed task planning, and independent cost assessments.
   * Provides actionable insights to support decision-making in resource allocation, risk mitigation, and timeline adjustments.

### Key Points Regarding Cost Repository Implementation

* **Data Accuracy**: Ensure repository data reflects reality by updating it continuously throughout the project lifecycle.
* **Granularity**: Maintain sufficient detail so that project data can be broken down to lower levels for work breakdown structure (WBS) elements.
* **Data Pedigree**: Establish lineage and traceability for cost model inputs and assumptions. Clearly document where the data originated and its level of validity.

## 3.2 Cost Repository Data

A cost repository should contain a comprehensive dataset with meaningful information to facilitate project estimation, performance tracking, and historical comparisons.

### 3.2.1  Minimum Recommended Data Set for Cost Repository

1. **Planned and Actual Effort**
   * Track hours or days planned vs. actual effort spent per task or phase.
2. **Planned and Actual Schedule Dates**
   * Include key dates such as start, major milestones, and project completion.
   * Provide visibility into deviations between planned timelines and actual outcomes.
3. **Planned and Actual Costs**
   * Document estimated vs. actual budgets to identify cost growth and better forecast financial needs for future projects.
4. **Planned and Actual Values for Key Project Metrics**
   * **Software Size**: Lines of code (new, reused, and modified reused).
   * **Requirements Count**: Planned and delivered requirements to track volatility and scope creep.
   * **Defects Count**: Defect trends for maintenance or sustaining engineering projects.
   * **Cost Model Inputs**: Factors like complexity (e.g., algorithmic complexity), requirements volatility, team size, and other elements driving costs.
5. **Project Descriptors/Metadata**
   * **Software Classification**: Class A, B, C, or safety-criticality levels.
   * **Software Domain/Type**: Flight software, ground systems, or scientific applications.
   * **Requirements Volatility**: Frequency and impact of requirement changes during the project lifecycle.

### 3.2.2  Additional Recommended Data

To enhance the repository’s utility for future analysis and comparisons:

* **Project Name/Organization**: Ensure traceability to specific efforts and responsible teams.
* **Platform and Software Language**: Hardware/software considerations.
* **Constraints**: Resource issues, budget overruns, or schedule pressures.
* **Safety/Criticality Level**: Identify software that directly impacts safety or mission-critical functions.

See also SWEs for Related Insights:

* **[SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation)**: Cost Estimation Guidance.
* **[SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions)**: Specification of Cost Estimate Conditions.
* **[SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)**: Repository Measurement Guidance.

## 3.3 Data Retention, Accessibility, and Reporting

### 3.3.1  Retention and Storage

The cost repository can range from basic tools like spreadsheets to advanced databases, depending on the complexity and scale of the repository. Key considerations include:

1. **Volume of Stored Data**
   * A spreadsheet format may suffice for small projects with fewer data points or lower reporting needs.
   * A database format is recommended for organizations managing large-scale projects with diverse stakeholders requiring real-time data access.
2. **Tools for Analysis and Benchmarking**
   * Tools with advanced features (e.g., dashboards, queries, analytics) can simplify data roll-up for organizational, Center-level, or multi-project insights.

### 3.3.2  Accessibility and Reporting:

1. **Organizational and Center-Level Systems**
   * Ensure data in the repository is accessible to organizational and Center-level systems to support holistic analysis, benchmarks, and process improvements across projects.
2. **Stakeholder Communication**
   * Report repository data periodically to stakeholders through summaries, trend analyses, dashboards, or presentations.
   * Highlight actionable insights, such as areas for cost control, sources of delays, or resource optimization opportunities.
3. **Continuous Updates**
   * Ensure real-time or regular updates of repository data throughout the project's lifecycle to reflect changes.

## 3.4  Best Practices for Cost Repository Implementation

1. **Maintain Data Integrity**
   * Ensure all repository data is systematically validated for accuracy, completeness, and reliability.
   * Implement checks to prevent entry errors and ensure actual vs. planned comparisons are meaningful.
2. **Use Consistent Data Templates Across Projects**
   * Develop standardized templates and data formats to ensure consistency across the organization. This allows for easier comparisons and roll-ups across different projects and Centers.
3. **Automate Where Possible**
   * Use tools or systems to automate data collection. For example, integrate cost models, version control systems, or defect tracking tools to feed data directly into the repository.
4. **Regular Reviews and Feedback Loops**
   * Periodically review repository data for trends, anomalies, or improvement opportunities.
   * Analyze deviations (e.g., actual vs. planned metrics) and incorporate lessons learned into future cost estimations.
5. **Align with Organizational Priorities**
   * Ensure the cost repository aligns with NASA’s larger goals for cost estimation, resource management, and continuous improvement initiatives.

## 3.5  How Cost Repository Data Helps Improve Processes

1. **Improves Estimation Accuracy**
   * Historical data informs better cost predictions and identifies common underestimation issues.
2. **Enhances Project Control**
   * Compare real-time data against planned milestones to detect schedule slippage or cost overruns early.
3. **Supports Organizational Benchmarking**
   * Enables NASA Centers to analyze projects within or across domains (e.g., flight software vs. ground systems) for trends and efficiencies.
4. **Drives Process Refinements**
   * Use metrics like defect counts, requirement changes, or cost model inputs to identify areas for process improvements (e.g., refined peer reviews, better testing coverage).
5. **Facilitates Transparency and Accountability**
   * Repository data ensures all stakeholders work from the same reference points when discussing performance, risks, or corrective actions.

## 3.6 Conclusion

A well-maintained cost repository provides NASA with the tools and information necessary to make data-driven decisions during project planning, execution, and improvement activities. By capturing detailed planned and actual metrics, tracking key cost parameters, and storing meaningful metadata, Centers can significantly improve their ability to accurately estimate costs, manage deviations, and learn from historical insights. With robust data retention, accessibility, and reporting practices, cost repositories empower teams to achieve project and organizational goals efficiently and consistently.

See also [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation), [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions),

See also [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository).

See also [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements),

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement)      * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

# 4. Small Projects

For small projects, which typically have fewer resources, modest budgets, and condensed schedules, this requirement should be scaled appropriately to ensure compliance with minimal administrative burden while maintaining the value and purpose of the cost repository. Below is tailored guidance for small projects.

## 4.1 Guidance for Small Projects

### 4.1.1  Keep It Simple and Lightweight

Small projects should avoid overly complex tools or processes. Use simple yet effective templates and tools to meet the requirement.

#### Recommended Tools:

* **Spreadsheets (e.g., Excel, Google Sheets)**:
  + Create a single, well-structured spreadsheet to capture all required data fields.
  + Use tabs or sections to organize planned and actual metrics, major milestones, and metadata.
* **Project Management Tools** (e.g., Trello, Asana, or Microsoft Project):
  + Log milestone dates and effort directly within the tool and export data for periodic updates to the cost repository.
  + Use built-in reporting features for tracking progress.
* **Issue Tracking Tools** (e.g., Jira, GitHub Issues):
  + Use issue trackers to capture defects and requirements count, which can be manually added to the spreadsheet repository.

**Tip**: Avoid introducing unnecessary tools or automation that could be time-consuming to set up. Instead, focus on tools already familiar to the team that can meet the minimum requirements.

### 4.1.2. Focus on Core Metrics Only

Small projects should prioritize collecting only the most critical fields outlined in the requirement. Avoid the "nice-to-have" metrics unless they provide clear value to the project or organization.

#### Minimum Required Metrics (for Small Projects):

* **Planned and Actual Effort**:
  + Capture summary-level data for major project phases (e.g., planning, design, coding, testing).
  + Track hours or person-days at the team or task level rather than at granular levels of individual contributors.
* **Planned and Actual Schedule Milestones**:
  + Track dates for critical milestones only (e.g., project start, Preliminary Design Review (PDR), Critical Design Review (CDR), testing completion, and delivery).
  + Keep milestone tracking to significant events rather than day-to-day activities.
* **Planned and Actual Costs**:
  + Focus on tracking total project costs and high-level cost categories (e.g., labor, software tools, and hardware).
* **Key Cost Parameters**:
  + Software size: Use approximate counts of new, reused, or modified code (track in LOC if feasible).
  + Requirements count: Capture initial planned requirements vs. final delivered requirements.
  + Defect counts: For maintenance or sustaining projects, track the number of defects reported and fixed.
* **Project Descriptors (Metadata)**:
  + Software class: (e.g., A, B, or C).
  + Software domain/type: (e.g., flight software, ground systems, or scientific analysis).
  + Requirements volatility: Record whether there are frequent requirement change requests.

### 4.1.3. Use Templates for Consistency

Create or borrow pre-defined templates that address the minimum data requirements to reduce the setup time and ensure consistency across projects.

#### Example Simple Spreadsheet Format:

| **Category** | **Planned** | **Actual** | **Notes** |
| --- | --- | --- | --- |
| Project Start Date | MM/DD/YYYY | MM/DD/YYYY |  |
| Design Completion | MM/DD/YYYY | MM/DD/YYYY |  |
| Testing Completion | MM/DD/YYYY | MM/DD/YYYY |  |
| LOC - New | 5,000 | 5,250 | **(+5% growth)** |
| LOC - Reused | 3,000 | 3,000 |  |
| Requirements Count | 120 | 135 | **(+15 changes)** |
| Labor Cost ($) | $250,000 | $275,000 | **Overrun due to testing** |
| Defects Found/Fix | N/A | 25 | For maintenance projects only |

### 4.1.4. Plan for Regular Updates

Timely updates are critical even for small projects. However, the frequency can be scaled to reflect the project’s need for agility and simplicity.

#### Recommended Update Frequency for Small Projects:

* **During Major Phases or Milestones**: Update the repository when transitioning between project phases, such as design, development, or testing completion.
* **At Regular Check-In Points**: For projects lasting several months, update the data repository monthly or biweekly. Weekly updates may not be necessary unless there is significant activity.
* **At Project Closeout**: Perform a final update at project completion to capture post-project metrics, such as actual schedule dates, defects, and cost data.

### 4.1.5. Automate Where Possible (But Don’t Overcomplicate)

Small projects can make use of semi-automation if it reduces the effort required to update the cost repository.

#### Ways to Automate:

* Use formulas in spreadsheets to calculate cost growth, effort deviations, or schedule slippage automatically.
* Export data from project management tools (e.g., Jira, Trello) to populate portions of the repository, such as defect counts or task start/completion dates.
* Where defects are tracked in issue tracking systems, use bulk exports/import functions to avoid manual entry.

### 4.1.6. Focus on Lessons Learned

Small projects may not generate vast datasets, but their repository is still critical for identifying lessons learned and improving future projects.

#### Examples of Lessons from Repository Data:

* **Underestimated Effort**: If actual hours exceed planned hours consistently, future projects may require better resource allocation.
* **Schedule Slippage Triggers**: Identifying milestones affected by late requirements or testing delays can improve future planning.
* **Predictable Requirement Volatility**: If requirements frequently change, it may signal the need to improve the initial requirements definition process.

### 4.1.7. Ensure Traceability with Metadata

Even in small projects, metadata is important for future historical analysis or audits.

* Keep metadata simple: Include the project name, organization, software classification, and a brief platform description (e.g., “Flight Software for CubeSat”).
* Record additional constraints (e.g., limited resources, schedule challenges) to contextualize any deviations.

#### Example Metadata Entry:

* **Project Name**: "CubeSat Guidance Software."
* **Organization**: ABC Research Center.
* **Software Class**: Class B.
* **Domain**: Flight software.
* **Constraints**: Aggressive timeline, limited developer availability.

### 4.1.8. Reporting for Small Projects

The cost repository should be targeted when shared with stakeholders to avoid overwhelming them with data. Use simple dashboards, one-page summaries, or concise tables to highlight key findings.

#### Example Report for Stakeholders:

* Key Milestones (Planned vs. Actual)
* Total Cost (Planned vs. Actual)
* Total Hours and Team Size
* Major Deviations (e.g., requirement volatility or test defects).

### 4.1.9. Benefits of Scaling to Small Projects

By tailoring the cost repository process, small projects can:

1. **Reduce administrative burden**: Save time and resources by focusing on essential metrics.
2. **Ensure compliance with minimal effort**: Meet NASA standards without overcomplicating workflows.
3. **Leverage historical knowledge**: Build a dataset that improves accuracy in future estimates for small or similar-sized efforts.
4. **Promote Process Improvement**: Learn how to adjust planning to minimize common risks like scope creep, delays, or under-budgeting.

## 4.2 Conclusion

For small software projects, a lightweight and flexible approach to cost repository implementation ensures compliance with NASA standards without exhausting limited resources. By focusing on the most critical data, using familiar tools, and maintaining consistency, small projects can both meet the requirement and achieve meaningful insights for future software efforts.

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
* (SWEREF-419)

  [GAO Cost Estimating and Assessment Guide, Best Practices for Developing and Managing Capital Program Costs.](http://www.gao.gov/new.items/d093sp.pdf "Click to open in new window")

  GAO-09-3SP. United States Government Accountability Office. Applied Research and Methods. March, 2009.
* (SWEREF-460) NPR 7150 traced to NASA-STD-8739 8 and NASA-STD-8719 13B\_20100924 This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
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

 The following lessons learned from NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** emphasize the importance of cost management practices.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. How is the Data Used?  [567](#_tabs-<p></p>)

* **Lesson Title**: *Know How Your Software Measurement Data Will Be Used*
* **Lesson Number**: 1772
* **Summary**:
  + This lesson emphasizes the importance of understanding how software measurement data will be interpreted and applied in NASA’s cost estimation process. Discrepancies between project-supplied data and NASA's interpretation can lead to faulty cost estimates, causing disruptions in project assessment and approval. For major flight projects, it is important to verify NASA’s approach to data interpretation and replicate their parametric cost modeling processes to ensure alignment before data submission.
* **Application to Cost Repository Requirement**:  
  This lesson underlines the critical role played by accurate measurement data in generating reliable project estimations. It highlights the need for consistency between what is input into the cost repository and how it will be used downstream in NASA’s parametric cost models. To align with this lesson:
  + Ensure software metrics such as size, requirements count, and defects are calculated consistently with NASA's cost estimation models (e.g., COCOMO II or other agency-standard tools).
  + Communicate with stakeholders and cost analysts during the cost estimation process to validate how project data will be interpreted.
  + Cross-check estimates using similar cost models to identify and resolve potential discrepancies before submission.
* **Key Takeaway**: Analyze and validate how project cost data will be used and interpreted to avoid misunderstandings in both internal and external cost modeling and approval processes.

#### 2. Use Realistic Assumptions for Cost Estimates

* **Lesson Title**: *The Challenge of Unrealistic Cost Assumptions*
* **Lesson Number**: 1261
* **Summary**:
  + Cost estimates often deviate from actual project costs due to the use of unrealistic assumptions during the initial estimation process. Inadequate evaluation of assumptions such as team experience, complexity of requirements, or reuse of software components can lead to overly optimistic or highly inaccurate estimates. This has been a common cause for cost overruns in NASA projects.
* **Application to Cost Repository Requirement**:  
  The foundation of a reliable cost repository lies in the accuracy of its baseline data and assumptions. To comply with this lesson:
  + Document all assumptions used in cost estimations in the cost repository (e.g., assumed team productivity, availability of reusable code, and anticipated volatility in requirements).
  + Include pedigree information (origin and justification) for each assumption or cost model input, so deviations can be tracked and analyzed.
  + Adjust assumptions based on historical project data stored in the repository to ensure future estimates are based on real-world experience.
* **Key Takeaway**: Avoid overly optimistic assumptions. Use realistic, data-driven inputs verified by historical performance when populating cost repositories.

#### 3. Understand and Manage Cost Growth

* **Lesson Title**: *The Causes and Trends of Cost Growth in NASA Projects*
* **Lesson Number**: 0934
* **Summary**:
* Analysis of historical NASA projects showed that cost growth often results from unforeseen technical challenges, incomplete requirements, and schedule pressure. Without a mechanism to track planned versus actual values at each phase of a project, teams struggle to understand and mitigate cost growth until it is too late.
* **Application to Cost Repository Requirement**:  
  The ability to track and compare planned and actual metrics at a detailed level is critical to managing cost growth. To address this lesson:
  + Frequently update the cost repository with actual data as the project progresses, especially during major milestones (e.g., PDR, CDR, testing).
  + Use cost growth trends from previous projects stored in the repository to predict risk factors and proactively manage them (e.g., incorporating buffers for unclear requirements or technical complexity).
  + Break large project metrics into smaller work breakdown structure (WBS) categories to better identify localized cost growth.
* **Key Takeaway**: Track planned vs. actual data rigorously, and use historical project trends to anticipate and mitigate cost growth.

#### 4. Ensure Proper Definition of Requirements Early

* **Lesson Title**: *Requirements Definition Issues Impact on Cost and Schedule*
* **Lesson Number**: 0721
* **Summary**:
  + Cost overruns and schedule slippages in software projects were often traced back to unclear or incomplete requirements during early stages of development. Changes to requirements late in a project lifecycle were found to disproportionately increase costs, primarily due to rework.
* **Application to Cost Repository Requirement**:  
  Requirements volatility is a key parameter captured in the cost repository. Incorporating this lesson into repository design ensures teams are alerted to issues early that could affect cost and schedule:
  + Track requirements volatility explicitly: calculate the number of changes to requirements across design, development, and test phases.
  + Flag significant increases in requirements count during development as a risk factor for cost overruns and update cost projections accordingly.
  + Use past requirements volatility metrics from the repository to estimate new project's contingency or risks associated with unstable requirements.
* **Key Takeaway**: Capture requirements-related trends (counts, changes, volatility) in the cost repository to anticipate and address cost overruns driven by scope changes.

#### 5. Account for Software Complexity in Estimation

* **Lesson Title**: *Impact of Software Complexity in Project Schedules and Budgets*
* **Lesson Number**: 0983
* **Summary**:
  + Higher-than-anticipated software complexity was found to be a recurring factor in project delays and cost overruns because it was not properly accounted for during cost estimation. This issue is particularly critical for innovative or domain-specific software projects where complexity metrics (e.g., algorithmic complexity, architecture) are underestimated.
* **Application to Cost Repository Requirement**:  
  To comply with this lesson, small projects should explicitly track complexity measures and inputs during the estimation process:
  + Include cost model inputs that quantify software complexity (e.g., algorithmic complexity, number of interfaces, platform dependencies).
  + Record assumptions about complexity at the start of the project and track if actual complexity (e.g., number of modules, lines of code) exceeds initial expectations.
  + Use historical data for projects of similar class or domain from the repository to refine project-specific complexity parametrics before estimates are finalized.
* **Key Takeaway**: Capture and adjust for software complexity as a critical factor when establishing inputs to cost estimates.

#### 6. Leverage Lessons from Prior Projects

* **Lesson Title**: *Importance of Historical Data in Software Project Estimates*
* **Lesson Number**: 1152
* **Summary**:
  + The absence of accessible, detailed historical data made it difficult for teams to create accurate cost estimates for new projects. Furthermore, when such data was available, lack of alignment between historical context and current project parameters resulted in flawed estimates. Careful mining and adjustments of historical data significantly improved estimate reliability.
* **Application to Cost Repository Requirement**:   
  The main purpose of the cost repository is to serve as a knowledge base for future projects:
  + Populate the repository with historical data on similar projects, including planned and actual cost, schedule, effort, defects, and metadata.
  + When estimating new projects, compare current project parameters (e.g., software class, size, complexity) with historical ones to identify applicable analogies.
  + Update the repository continuously to ensure that new lessons feed into the organization’s estimation practices.
* **Key Takeaway**: Build and maintain a complete, detailed repository as the foundation for data-driven cost estimation.

### 6.1.2  Conclusion

#### Summary of Lessons Learned Application to Cost Estimation

By integrating lessons learned into the cost repository requirement, small and large projects alike can experience significant improvements in cost estimation accuracy and project management outcomes. Key guidance includes:

1. Understand how NASA will use software measurement data to ensure alignment in inputs and interpretation.
2. Base all estimates on realistic assumptions and validate them with historical project data.
3. Manage scope changes and requirements volatility, as they have a disproportionate impact on cost and schedule.
4. Account for software complexity explicitly in the estimation process.
5. Leverage lessons from prior projects to inform and refine new cost models and parameters.

These lessons emphasize the repository's dual role in tracking current progress and serving as a knowledge base for future process improvement and estimation activities.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Maintain budgets on-line](https://software.gsfc.nasa.gov/lesson-details/134/). **Lesson Number 134**: The recommendation states: "Maintain budgets on-line."

# 7. Software Assurance

**SWE-142 - Software Cost Repositories**

2.1.5.10 For Class A, B, and C software projects, each Center Director, or designee, shall establish and maintain software cost repository(ies) that contains at least the following measures: 

a. Planned and actual effort and cost.  
b. Planned and actual schedule dates for major milestones.  
c. Both planned and actual values for key cost parameters that typically include software size, requirements count, defects counts for maintenance or sustaining engineering projects, and cost model inputs.  
d. Project descriptors or metadata that typically includes software class, software domain/type, and requirements volatility.

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

This requirement ensures the Center establishes and maintains reliable software cost repository(ies) for Class A, B, and C software projects. The primary purpose is to support accurate cost tracking, provide visibility into cost-related performance, and enable informed decision-making about future projects based on historical data.

Software Assurance (SA) personnel are responsible for ensuring the completeness, accuracy, usability, and compliance of the repository. Their role is to verify that the repository’s data is relevant, consistent, and actionable for assessing project performance and enhancing cost estimation practices.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Verify the Establishment of the Software Cost Repository

1. **Ensure Repository Exists**
   * Confirm that a centralized and accessible software cost repository has been established for collecting and retaining data for Class A, B, and C software projects.
   * Verify that the repository supports the required measures (see sections a–d below) and includes the necessary tools to analyze and report cost-related data.
2. **Evaluate Repository Design**
   * Confirm that the repository is designed to:
     + Securely store and centralize data, preventing data loss or discrepancies.
     + Support version control for maintaining planned and actual values.
     + Be accessible to key stakeholders while ensuring confidentiality and appropriate access control.

#### 7.4.2.2  Verify Inclusion of Required Data Measures

Ensure the Software Cost Repository captures the following required measures for planned and actual values:

##### **(a) Planned and Actual Effort and Cost**

* + Verify that the repository records planned and actual time (effort) and cost (budgeted vs. actual expenses) at detailed levels throughout the project lifecycle, including:
    - Requirements definition.
    - Design, development, and implementation.
    - Verification and Validation (V&V).
    - Maintenance or sustaining engineering phases.

*SA Oversight*:

* + Ensure that the effort data (e.g., hours worked) matches team reports and timesheets.
  + Confirm that cost data categories (labor, tools, materials, etc.) are clear and based on standards, such as NASA’s cost estimation guidance.

##### **(b) Planned and Actual Schedule Dates for Major Milestones**

* + Verify that the repository tracks major project milestones, including:
    - SRR (System Requirements Review).
    - PDR (Preliminary Design Review).
    - CDR (Critical Design Review).
    - Test Readiness Reviews and operational readiness milestones.
  + Compare planned milestone dates to actual outcomes to identify variances.

*SA Oversight*:

* + Check for consistency between schedule data in the repository and official project schedules or Gantt charts.
  + Verify that any deviations from planned milestones are explained and documented.

##### **(c) Planned and Actual Key Cost Parameters**

* + Confirm the repository includes the following cost-related parameters for planned and actual values:
    - **Software size estimates (e.g., KSLOCs or another size metric)**: Ensure proper estimation practices are applied.
    - **Requirements count**: Track total requirements planned and implemented, along with changes.
    - **Defect counts for maintenance projects**: Capture defect introduction and resolution trends for sustaining engineering projects.
    - **Inputs into cost models**: Ensure parameters like productivity rates, team sizes, or risk factors feeding into cost estimation models are included and validated.

*SA Oversight*:

* + Verify that size, requirements, defect counts, and model inputs are consistent with associated engineering documentation and impact cost projections.

##### **(d) Project Descriptors or Metadata**

* + Confirm the repository includes metadata to describe each project, such as:
    - **Software Class**: Class A, B, or C as defined by NASA’s software classification process.
    - **Software Domain/Type**: Type of software (e.g., flight, ground, embedded) and application domain.
    - **Requirements Volatility**: Measure of requirements changes over time and its documented impact on cost, effort, and schedule.

*SA Oversight*:

* + Verify metadata completeness and ensure the repository tracks requirements volatility quantitatively (e.g., percentage of requirements modified).

#### 7.4.2.3  Monitor the Repository’s Maintenance and Data Quality

1. **Perform Data Validations**
   * Verify that data in the repository is:
     + **Accurate**: Matches project source documents, such as schedule tracking tools, timesheets, or cost reports.
     + **Complete**: Contains all essential information required for cost and effort tracking.
     + **Timely**: Includes regular updates, especially when milestones are completed or changes in the project lifecycle occur.
2. **Conduct Periodic Audits**
   * Validate the repository against project artifacts (e.g., Software Development/Management Plans, Cost Estimation Reports, and Test Reviews).
   * Monitor for consistent population of planned and actual values for effort, cost, schedules, and key parameters across all Class A, B, and C projects.
3. **Ensure Traceability**
   * Confirm that all cost repository data is traceable to its original source, with clear links between planned and actual values to identify variances.

#### 7.4.2.4  Monitor How the Repository Data Is Used

1. **Support Cost and Effort Analysis**
   * Ensure that the repository is actively used to:
     + Identify trends (e.g., recurring schedule delays, under/overestimated costs).
     + Analyze actual vs. expected performance on cost model parameters.
     + Adjust cost estimation approaches using lessons learned from historical data.
2. **Support Decision-Making and Improvement Activities**
   * Validate that the repository data informs:
     + Software engineering process improvements to reduce cost overruns or effort inefficiencies.
     + Risk assessments based on past cost or schedule variability trends.
     + Fact-based decision-making for resource allocation or productivity enhancements.
3. **Track Project Variances**
   * Confirm that the repository helps the Center monitor actual cost and schedule variances against planned metrics at program reviews, enabling timely corrective actions if needed.

#### 7.4.2.5  Drive Continuous Improvement

1. **Analyze Long-Term Trends**
   * Ensure data from the repository is analyzed post-project to identify systemic issues, such as chronic underestimation or frequent requirements volatility leading to cost increases.
2. **Improve Estimates Through Historical Data**
   * Advocate for using historical repository data to refine cost estimation techniques, driving closer alignment between planned and actual values for future projects.
3. **Identify Lessons Learned**
   * Support efforts to document and share lessons learned from variations captured in the repository, improving estimating and tracking capabilities across the Center.
4. **Recommend Enhancements**
   * Suggest refinements to repository structure or tools, such as:
     + Adding automated data collection capabilities.
     + Expanding metadata (e.g., risk criticality, team experience factors) to improve analysis.

### 7.4.3  Expected Outcomes

Through SA support, the Center will achieve the following:

1. **Comprehensive Repository**:
   * A well-maintained repository that tracks complete and accurate planned vs. actual cost, effort, schedule, size, and parameters for Class A, B, and C projects.
2. **Improved Visibility**:
   * Consistent access to reliable data for analyzing cost and effort performance.
3. **Informed Decision-Making**:
   * Data from the repository drives quality improvements, resource allocation, and risk management.
4. **Enhanced Estimations**:
   * Historical data improves future cost and effort estimation processes.
5. **Compliance**:
   * The repository meets NASA’s requirements per **NPR 7150.2**[083](#_tabs-<p></p>), supporting audits and organizational accountability.

### 7.4.4  Conclusion

Software Assurance (SA) personnel are responsible for verifying that the software cost repository meets all data requirements (planned and actual values for effort, cost, schedule, size, and metadata) and is actively maintained for Class A, B, and C software projects. By ensuring the repository’s accuracy, proper use, and periodic updates, SA directly contributes to better project oversight, informed decision-making, and improved cost estimation practices.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) |
