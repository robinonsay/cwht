# SWE-003 - Center Improvement Plans

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695393. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans

SWE-003 - Center Improvement Plans

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695393)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695393&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.5.2 Center Director, or designee, shall maintain, staff, and implement a plan to continually advance the Center’s in-house software engineering capability and monitor the software engineering capability of NASA's contractors.

## 1.1 Notes

The recommended practices and guidelines for the content of a Center Software Engineering Improvement Plan are defined in NASA-HDBK-2203, NASA Software Engineering Handbook.  Each Center has a current Center Software Engineering Improvement Plan on file in the NASA Chief Engineer’s office

## 1.2 History

Click here to view the history of this requirement: SWE-003 History

SWE-003 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 1.2.2 Each Center shall maintain, staff, and implement a plan to continually advance its in-house software engineering capability and monitor the software engineering capability of NASA's contractors, as per NASA's Software Engineering Initiative Improvement Plan. |
| Difference between A and B | Reworded and removed reference to NASA SEIIP. |
| B | 2.1.3.2 Center Directors, or designees, shall maintain, staff, and implement a plan to continually advance the Center’s in-house software engineering capability and monitor the software engineering capability of NASA's contractors. |
| Difference between B and C | No change |
| C | 2.1.5.2 Center Director, or designee, shall maintain, staff, and implement a plan to continually advance the Center’s in-house software engineering capability and monitor the software engineering capability of NASA's contractors. |
| Difference between C and D | No change |
| D | 2.1.5.2 Center Director, or designee, shall maintain, staff, and implement a plan to continually advance the Center’s in-house software engineering capability and monitor the software engineering capability of NASA's contractors. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

This requirement allows the Agency to have insight into each Center's plans for maintaining in-house software engineering capabilities and Center processes used to monitor the software engineering capability of the contractors supporting the Center's projects. 

See also Topic [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) for additional details on the SPI Initiative.

Software systems are at the heart of NASA’s missions, enabling everything from spacecraft control and rover autonomy to data analysis and ground system operations. To sustain mission success and NASA’s technological leadership, it is critical for Centers to continuously improve their software engineering capabilities while maintaining oversight of contractors' software practices. This requirement supports both goals by ensuring software engineering excellence and effective contractor management. Below is the detailed rationale.

## 2.1 Key Rationale for the Requirement

### 1. Ensures High-Quality Software Across NASA Missions

NASA’s missions increasingly demand complex, robust, adaptable, and error-free software systems to ensure safety, reliability, and mission success. Advancing in-house software engineering capabilities at the Centers ensures that NASA teams can maintain the high standards expected of critical software.

* **Why This Requirement Matters**:
  + Developing and sustaining a Center plan for improving in-house capabilities ensures continuous alignment with best practices in software development, verification, validation, and assurance.
  + High-quality, in-house software engineering provides a foundation for identifying risks, preventing defects, and supporting mission-critical activities.

### 2. Addresses Evolving Software Complexity and Risks

Software used in NASA’s missions is becoming increasingly complex, with systems incorporating advanced features such as artificial intelligence (AI), cybersecurity, fault tolerance, and autonomy. This complexity elevates the risk of software errors, which can threaten mission success and safety.

* **Why This Requirement Matters**:
  + Continuous advancements in in-house software engineering capability allow Centers to stay ahead of these complexities and address the unique risks they pose.
  + Enhanced capabilities enable more robust design, analysis, and testing processes, ensuring NASA’s software meets the rigorous demands of space exploration.

### 3. Protects Against Mission Failures Due to Software Defects

Historical lessons learned from NASA missions have highlighted the significant impact of software-related failures:

* Mars Polar Lander (1999): A software misinterpretation of sensor data caused the premature shutdown of descent engines.
* Mars Climate Orbiter (1999): Unit inconsistency (metric vs. imperial) in software interfaces resulted in the loss of the spacecraft.
* Ariane 5 Flight 501 (1996): An unhandled software exception caused a catastrophic launch failure.
* **Why This Requirement Matters**:

  + Advancing software engineering capability minimizes the likelihood of similar issues by employing more advanced verification and validation techniques.
  + Monitoring contractor capabilities ensures that their work aligns with NASA’s high standards, reducing the risk of introducing errors in subcontracted software.

### 4. Aligns with NASA's Strategic and Safety Goals

NASA’s missions rely not only on cutting-edge technology but also on maintaining public trust in the safety and reliability of its systems. Software defects can lead to high-profile failures that undermine mission success and NASA’s reputation.

* **Why This Requirement Matters**:
  + Advancing in-house capabilities ensures that Centers retain the expertise needed to design, assess, and assure the safety and quality of software systems.
  + Oversight of contractor performance ensures contractors uphold NASA’s mission safety and quality standards, aligning their practices with established requirements.

### 5. Empowers NASA to Set and Enforce High Standards with Contractors

NASA relies on contractors across a range of activities, including software development. While contractors provide expertise, their capabilities and adherence to standards must be monitored to ensure alignment with NASA-specific needs and priorities.

* **Why This Requirement Matters**:  
  + Monitoring contractor software engineering capabilities ensures that external organizations are meeting the same high standards as in-house teams.
  + Contractors with insufficient capabilities or divergent practices may introduce risks; continuous monitoring allows NASA to identify and address these gaps proactively.

### 6. Supports Lessons Learned and Continuous Improvement

NASA’s lessons learned (e.g., from the Lessons Learned Information System) emphasize that sustained focus on improving in-house skills and contractor management is key to mission success. Project teams that fail to apply these lessons often repeat past mistakes.

* **Why This Requirement Matters**:
  + By requiring continual advancement of in-house capabilities, Centers ensure that software teams apply lessons learned from NASA’s history to future missions.
  + Through contractor monitoring, Centers can verify that contractors are also embedding prior lessons learned into their work.

### 7. Addresses Fast-Changing Technological Landscapes

The field of software engineering evolves rapidly, with new technologies, tools, practices, and standards emerging regularly. To ensure competitiveness and excellence, NASA must adopt and integrate these advancements into its software engineering processes.

* **Why This Requirement Matters**:
  + Advancing in-house capabilities allows Centers to incorporate emerging technologies (such as AI, machine learning, DevOps, agile methods) to maintain cutting-edge competence.
  + Monitoring contractor practices ensures that NASA contractors are also leveraging emerging technologies appropriately.

### 8. Promotes Workforce Development and Retention

A highly skilled and motivated software engineering workforce is critical to NASA’s ability to fulfill its mission. Continually advancing in-house software engineering capabilities enables Centers to attract, develop, and retain top talent.

* **Why This Requirement Matters**:
  + Training and development programs ensure that software engineers are exposed to the latest tools and methodologies, keeping their skills relevant and sharp.
  + Focusing on continuous improvement fosters an innovative culture, which is essential for retaining highly skilled individuals.

### 9. Balances Cost, Schedule, and Quality

While maintaining and advancing software engineering capability may require initial investment, it ultimately reduces rework, mitigates costly mission errors, and shortens software development cycles. Similarly, strong contractor oversight prevents quality issues that may introduce delays or budget overruns.

* **Why This Requirement Matters**:
  + Proactively advancing capabilities ensures better planning, reduced errors, and fewer iterations during development cycles.
  + Ensuring contractors meet the same high standards reduces the likelihood of costly rework or downstream integration issues.

### 10. Ensures Mission Readiness and Flexibility

NASA missions often involve quick adaptations in response to unforeseen challenges. To ensure readiness and flexibility, Centers need skilled software engineers and proven processes ready to adapt to new mission needs.

* **Why This Requirement Matters**:  
  + In-house capabilities enable Centers to respond quickly to new requirements or unexpected software challenges.
  + Monitoring contractors ensures that they can deliver high-quality work in the accelerated timeframes missions sometimes demand.

### 11. Advances NASA’s Commitment to Quality, Safety, and Excellence

NASA has an ongoing commitment to ensuring the highest standards of quality, safety, and mission assurance. This commitment is especially critical in software engineering, where errors can have far-reaching consequences.

* **Why This Requirement Matters**:
  + By maintaining a plan to advance in-house software engineering capability, Centers demonstrate NASA’s commitment to better processes and safer, more reliable software.
  + Oversight of contractors ensures that external teams align with NASA’s culture of excellence, particularly in safety-critical software development.

## 2.2 Conclusion

The requirement that Center Directors maintain, staff, and implement a plan to continually advance their in-house software engineering capability—and monitor the software engineering capability of contractors—is essential for the following reasons:

1. It ensures critical software meets NASA’s high standards for safety, reliability, and performance.
2. It addresses the complexities of evolving software challenges through sustained improvement in both in-house and contracted capabilities.
3. It strengthens workforce capabilities, incorporates lessons learned, and fosters innovation.
4. It protects NASA from software-related failures by ensuring thorough monitoring of all software development, whether in-house or by contractors.

Ultimately, this requirement guarantees that Centers drive continuous excellence in software engineering while holding contractors accountable for delivering software that contributes to mission success.

# 3. Guidance

This guidance is intended to clarify the expectations for continuously improving software engineering capabilities within NASA Centers and to highlight effective practices for assessing the capabilities of contractors contributing to NASA projects. It emphasizes the responsibility of each Center to implement a structured and adaptable approach to software process improvements, ensuring alignment with NASA’s overall mission goals, safety standards, and quality assurance practices.

## 3.1 Documented Approach for Advancing Software Engineering Capability

Centers must create and maintain a documented approach that:

* **Defines Activities:** Outlines a clear strategy for advancing the in-house software engineering capabilities of the Center. This includes specific goals, activities, and metrics to guide progress.
* **Monitors Contractors:** Details the process for evaluating and monitoring the software engineering capabilities of contractors to ensure alignment with NASA standards and expectations.

#### Key Points to Consider:

* A written **Center Software Engineering Improvement Plan** is encouraged but not mandatory. Instead, a flexible and pragmatic approach should be documented to guide the Center’s improvement efforts.
* The documented approach should be regularly reviewed, updated as needed, and shared among stakeholders, including software engineering teams, leadership, and contractors.

## 3.2 Center Responsibilities for Improvement Activities

Centers are responsible for activities that:

* **Define and Advance Capabilities:** Specify how the Center will continually improve its internal software engineering capabilities.
* **Monitor Effectiveness:** Establish methods to track progress and assess the success of these activities, including how contractors are being evaluated.
* **Align with Agency Requirements:** Ensure the Center’s efforts align with NASA’s overall vision, policies, and standards for software engineering.
* **Engage Stakeholders:** Achieve agreement and support from relevant stakeholders, including project leads and NASA Headquarters, on the defined activities.

## 3.3 Specific Objectives of Improvement Activities

The improvement activities at each Center should be designed to:

1. **Maintain Software Engineering Capabilities:**
   * Continually refine processes, tools, and resources to meet evolving project needs and challenges.
   * Ensure teams remain proficient in software engineering best practices, standards, and frameworks.
   * Identify and address gaps in current capabilities.
2. **Evaluate Contractor Capabilities:**
   * Monitor the performance of contractors building or supporting software systems for NASA projects.
   * Establish criteria for assessing whether contractors meet NASA’s quality and engineering standards.
   * Provide feedback or corrective measures for contractors that fall short of expectations.
3. **Align Local Processes with Agency-Wide Standards:**
   * Define and document the processes, practices, and tools used by the Center for software development, including templates, operating procedures, and compliance policies.
   * Implement any new or revised NASA Headquarters requirements through phased approaches.
4. **Engage and Train Personnel:**
   * Maintain appropriate staffing and expertise for executing improvement activities.
   * Develop training programs to build skill sets in emerging software technologies (e.g., AI, machine learning, cloud systems).
5. **Evaluate and Adapt to Change:**
   * Regularly review and revise the improvement activities to address new project requirements, emerging technologies, and evolving mission challenges.

## 3.4 Stakeholder Involvement

To ensure success, stakeholder engagement is essential throughout the improvement lifecycle. Centers should:

* Involve stakeholders in reviewing and accepting the defined improvement activities.
* Facilitate collaboration with NASA Headquarters (e.g., OCE, OSMA, OCHMO) to ensure alignment with Agency objectives.
* Clearly communicate progress and challenges to all relevant parties, enhancing transparency and accountability.

## 3.5 Establishing and Utilizing Software Engineering Process Groups (SEPG)

A common and effective approach for implementing improvement plans is to form **Software Engineering Process Groups (SEPGs)** at the Center level.

#### Responsibilities of SEPGs:

* **Plan and Oversee Improvements:** The SEPG should be responsible for day-to-day planning and implementation of software process improvements.
* **Monitor Progress:** Regularly review the status of improvement efforts and ensure they align with the Center’s goals.
* **Coordinate Stakeholder Needs:** Engage with stakeholders to refine activities and ensure buy-in.

Centers should allocate staffing and resources to support SEPG activities and associated training programs.

## 3.6 Guidance on Structuring the Center’s Approach

A Center’s **software engineering improvement approach** should include the following components:

### 3.6.1 Core Elements:

* **Improvement Goals:**
  + Define specific process improvement goals related to in-house software engineering and contractor oversight.
  + Ensure goals are measurable and achievable.
* **Scope of Improvement:**
  + Outline the areas of focus, such as software design, testing, assurance, safety, or acquisition.
  + Identify organizations responsible for mission-critical software development, management, or acquisition.
* **Phase-in Plan:**
  + Develop a phased approach for implementing process improvements, balancing urgency with resource capacity.
  + For large Centers, consider domain-specific or organizational-specific phasing to avoid overwhelming teams.
* **Performance Monitoring:**
  + Establish clear metrics for measuring the effectiveness of process improvements (e.g., defect rates, adherence to schedules, contractor performance).
  + Define roles and responsibilities for tracking and reporting progress.

### 3.6.2 Key Strategies and Objectives:

* Map out clear strategies that enable structured progress toward the improvement goals.
* Determine how the Center will implement these strategies, factoring in cross-domain requirements and project-specific challenges.

### 3.6.3 Implementation Schedule:

* Define a realistic timeline for rolling out new processes, tools, and training programs.
* Account for critical mission deadlines, resource limitations, and Agency mandates.

### 3.6.4 Adopting NASA Headquarters Requirements:

* Outline the Center’s plan for integrating new or updated requirements issued by NASA Headquarters.
* Focus on phasing in changes to minimize disruption while ensuring full compliance.

## 3.7 Connections to Related Requirements

Centers should align improvement activities with other relevant requirements to ensure comprehensive software engineering processes:

* **[SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status):**
  + Guidance on providing updates about the status of the Center’s software engineering discipline to NASA Headquarters upon request.
* **[SWE-208 - Advancing Software Assurance and Software Safety Practices](/spaces/SWEHBVD/pages/102695328/SWE-208+-+Advancing+Software+Assurance+and+Software+Safety+Practices):**
  + Encourages proactive measures to enhance software assurance and safety within the Center.
* **[SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes):**
  + Provides recommendations for creating SEPGs and Process Asset Libraries to support process improvement and knowledge sharing.

## 3.8 Additional Considerations for Maintaining Excellence

1. **Continuous Workforce Development:**
   * Plan tailored training and mentorship programs to keep the workforce up to date on evolving software engineering standards and tools.
2. **Knowledge Sharing:**
   * Establish a robust **Process Asset Library** to maintain and share key resources (e.g., templates, documentation, process guides) across NASA Centers.
3. **Integration with Contractors:**
   * Encourage collaboration and alignment between in-house engineering teams and contractors to streamline software development and assurance processes.

## 3.9 Conclusion

This enhanced guidance ensures that Centers implement structured and flexible approaches to advance in-house software engineering capabilities, effectively monitor contractor performance, and align with NASA’s high software engineering standards. By engaging stakeholders, utilizing SEPGs, and maintaining focus on workforce development and process improvement, NASA can ensure mission success while advancing its leadership in innovative software engineering practices.

See also [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination), [SWE-098 - Agency Process Asset Library](/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library).

See also [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) for the requirement on the Software Engineering Initiative. 

## 3.10 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status) * [SWE-098 - Agency Process Asset Library](/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library) * [SWE-208 - Advancing Software Assurance and Software Safety Practices](/spaces/SWEHBVD/pages/102695328/SWE-208+-+Advancing+Software+Assurance+and+Software+Safety+Practices)        * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) |

## 3.11 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects often operate under constraints that include limited budgets, resources, and timeframes. Despite these constraints, maintaining and advancing software engineering capabilities and monitoring contractor performance remains critical for ensuring software quality, reliability, and mission success. The following guidance offers a tailored approach for small projects to meet this requirement effectively without overextending their limited resources.

## 4.1 Simplified Guidance for Small Projects

### 4.1.1  Focus on Scaled and Risk-Based Practices

Small projects should prioritize advancing and monitoring software engineering capabilities based on their specific needs and risk levels.

* **Key Actions:**
  + Identify mission-critical, safety-critical, or high-priority areas that require the most attention and improvement.
  + Focus resources on areas where small gaps in software engineering processes or contractor performance could have a significant impact on mission success.

### 4.1.2  Leverage Existing Center Resources

Small projects can achieve their goals without duplicating effort by leveraging established resources and infrastructure within their Centers:

* **Software Engineering Process Groups (SEPGs):**
  + Engage with the Center’s SEPG to leverage processes, templates, and tools that have already been developed.
  + Request tailored advice from the SEPG for identifying minimal but effective improvements to existing software engineering practices.
* **Process Asset Library (PAL):**
  + Use templates, lessons learned, and standards stored in the PAL to streamline project needs without having to reinvent processes.

### 4.1.3  Implement Minimal Documentation

Unlike larger projects that may require in-depth improvement plans, small projects can adopt a lightweight approach to documenting software engineering improvement activities.

* **Actions:**
  + Define a short and concise written approach that addresses:
    - Specific goals for improving software engineering processes relevant to the project.
    - A process for evaluating contractor adherence to NASA requirements.
  + Include only essential information necessary to align with risk-based decisions and key objectives.
* **Example for Small Projects:**
  + Create a one-page improvement document summarizing the following:
    - The goals of improvement (e.g., "Improve requirements traceability processes").
    - The immediate benefit for the project (e.g., "Ensure clarity between requirements and test cases to reduce errors during integration").
    - Minimal progress metrics (e.g., "Defects discovered via requirements inspection before testing").

### 4.1.4  Small-Scale Monitoring of Contractor Capabilities

Monitoring contractor software engineering practices for a small project can be simplified to focus on critical interactions and deliverables.

* **Key Contractor Monitoring Actions:**
  1. **Review Deliverables Regularly:**
     + Verify that contractor-supplied artifacts, such as software requirements, design documents, or code, conform to NASA’s standards and project needs.
  2. **Risk-Based Oversight:**
     + Focus monitoring on high-risk software components or functions. For low-risk components, contractor adherence to project standards may be sufficient.
  3. **Use Established Criteria:**
     + Use Center-provided or NASA Agency-level checklists, guidelines, and audit processes as benchmarks for contractor compliance.

### 4.1.5  Utilize NASA's Resources for Software Engineering Capabilities

Small projects can rely on NASA resources to minimize workload while ensuring adherence to high standards:

* **Training and Knowledge Sharing:**
  + Utilize free or already-funded training opportunities provided by the Center to enhance the software engineering skills of the in-house team.
  + Participate in community forums, workshops, or NASA Software Working Groups to exchange knowledge and stay informed of best practices.
* **Independent Verification and Validation (IV&V):**
  + If applicable, request assistance from the NASA IV&V facility in identifying risks related to software contractors or in-house processes.

### 4.1.6  Scale the Improvement Plan to Project Needs

Small projects often do not require comprehensive improvement plans. Instead:

* Adopt a **short-term, tactical approach** to software process improvement.
* Focus on specific areas like:
  + Configuration management processes.
  + Automated testing tools.
  + Repeatable defect containment practices.

**Practical Implementation for Small Projects**

1. **Simple Process Improvement Strategy**:  
   A small project can use a lightweight process improvement framework for advancing in-house capability:
   * **Define:**
     + Identify one or two deficiencies in current software development practices.  
       *(Example: Enhance unit testing practices to catch more defects before system integration.)*
   * **Develop:**
     + Outline small, low-cost training sessions or tools to address those gaps.  
       *(Example: Train the team in using an open-source unit-testing framework.)*
   * **Implement:**
     + Integrate changes into the software development workflow.  
       *(Example: Add a requirement that all revisions include passing unit test results.)*
   * **Monitor Progress:**
     + Track improvements using a simple metric (e.g., reduced defects discovered during integration). Report findings to the SEPG or Center Improvement Team for lessons learned.
2. **Monitoring Contractors on Small Projects**:  
   On small projects, contractor evaluation can be simplified:
   * Review critical artifacts during key stages (e.g., requirements, design reviews, testing reports).
   * Request contractors to align their work with NASA’s software engineering standards and verify compliance through periodic performance audits.

## 4.2 Key Simplifications for Small Projects

**Areas Requiring Focus**:

* Reliability of safety-critical or mission-critical components.
* Requirements validation, code quality, and test practices.

**Areas That Can Be Streamlined**:

* Full-scale improvement plans. Focus on lightweight planning and implementation.
* Comprehensive contractor audits. Emphasize deliverables review and targeted evaluations instead.

## 4.3 Related Resources for Small Projects

Small projects can use existing NASA resources and requirements for specific guidance:

1. **[SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status):**
   * Guidance on how small projects can report their software engineering practices and obtain support from the Center if needed.
2. **[SWE-005 – Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes):**
   * A resource for establishing simplified processes and tools relevant to small project needs.
3. **Lessons Learned Database:**
   * Access the NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** to integrate Lessons Learned into the project.

## 4.4 Example for a Small Project

Below is an example of a simple software engineering improvement and contractor monitoring approach for a small project:

**Scenario: A Science Payload Control System (Small Scale)**

* **Process Improvement:**
  + *Focus Area:* Improve error handling in the payload control system.
  + *Task:* Introduce automated static analysis tools to detect coding defects early.
  + *Implementation:* Allocate 2 hours of training on the tool and require its use in all coding commits.
  + *Monitoring:* Measure the defects identified in static analysis vs. integration testing.
* **Contractor Monitoring:**
  + *Approach:* Conduct a focused review of the contractor’s test plan and verify compliance with NASA safety-critical software standards.
  + *Evaluation:* Check whether test cases adequately cover error-handling scenarios and edge cases.

## 4.5 Conclusion for Small Projects

Small projects should adopt pragmatic, lightweight approaches to advancing software engineering capability and contractor monitoring. By focusing on high-risk and high-priority areas, leveraging existing resources, and maintaining simple yet effective processes, these projects can fulfill the requirement without overwhelming limited resources. This ensures that even small efforts drive meaningful improvements and align with NASA’s broader mission goals.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-117)

  [2018 NASA Strategic Plan,](https://nodis3.gsfc.nasa.gov/npg_img/N_PD_1001_000C_/N_PD_1001_000C__main.pdf "Click to open in new window")

  NPD 1001.0C, NASA Office of Office of the Chief Financial Officer, 2018.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following Lessons Learned, derived from the NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)**, are directly applicable and provide important rationales, historical failures, and best practices to support and guide compliance with this requirement.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Independent Verification and Validation of Embedded Software

* **LLIS Lesson Number: 723**
* **Summary:** The use of Independent Verification and Validation (IV&V) ensures that software is developed according to original specifications, performs as intended, and does not perform unintended functions. Errors caught early in the process are significantly less expensive to resolve and improve the quality and reliability of software.
* **Application to This Requirement:**
  + Continually advancing in-house software engineering capability involves embedding processes, tools, and reviews to catch errors early.
  + Centers can use this lesson to advocate for modern validation tools and processes, ensuring the Center’s in-house and contractor-developed software adheres to required functionality.
  + Regularly monitoring contractor software involves verifying that their designs and processes include IV&V-like rigor.

#### 2. Software Deficiencies in the Mars Polar Lander (MPL)

* **LLIS Lesson Number: 1778**
* **Summary:** The Mars Polar Lander failed due to software handling issues, specifically premature shutdown of the descent engines, caused by inadequate testing of software interfaces and limited simulation under actual mission scenarios. Proper software assurance processes, including rigorous testing and validation, could have prevented this loss.
* **Application to This Requirement:**
  + Enhancing in-house capabilities involves the development of robust test environments, simulations, and validation techniques for software, particularly for safety-critical and mission-critical functions.
  + Monitoring contractor capabilities includes ensuring that contractors test software in scenarios that mimic operational environments, thereby avoiding MPL-like oversights.

#### 3. Mars Climate Orbiter Failure Due to Unit Miscommunication

* **LLIS Lesson Number: 0938**
* **Summary:** The Mars Climate Orbiter was lost due to a failure to account for a critical unit conversion mismatch (metric vs. imperial). This issue arose from process gaps, including insufficient rigor in software reviews, weak interface validation, and ineffective contractor oversight.
* **Application to This Requirement:**
  + Center software engineering capability must emphasize the development and use of tools and processes that ensure:
    - Proper validation of interfaces.
    - Rigorous review of contractor-supplied software artifacts.
  + Monitoring the engineering capability of contractors includes requiring validation of all interfaces and adherence to strict quality standards before acceptance of deliverables.

#### 4. Joint Confidence Level (JCL) Practices for Software Development

* **LLIS Lesson Number: 2221**
* **Summary:** A lack of realistic software development Joint Confidence Level (JCL) estimates for time, costs, and risks on past programs caused unanticipated delays and cost overruns. Proper estimation tools, workforce expertise, and contractor reliability are key to mitigating such issues.
* **Application to This Requirement:**
  + Centers should invest in tools and training to ensure accurate resource and risk estimation for software development timelines, especially for contractor-led efforts.
  + Effective contractor monitoring involves evaluating their resource projections for feasibility and alignment with NASA’s mission goals and constraints.

#### 5. Columbia Accident Investigation Board (CAIB) – Software and Workforce Expertise

* **(LLIS Lesson Number: 2106)**
* **Summary:** The **Columbia Accident Investigation Board** highlighted that deficiencies in workforce expertise, inadequate knowledge transfer, and reliance on undertrained personnel contributed to missed risks and oversights. NASA was advised to improve workforce skill development and maintain subject matter expertise, particularly as systems become more dependent on software.
* **Application to This Requirement:**
  + This lesson emphasizes the importance of staffing the Center’s software engineering teams with skilled personnel and continually training them on best practices, standards, and tools.
  + Monitoring contractor capability includes verifying that contractors allocate experienced and trained staff to deliver high-quality software products.

#### 6. The Importance of Software Metrics in Monitoring Capability

* **LLIS Lesson Number: 1485**
* **Summary:** A lack of meaningful software metrics led to deficiencies in tracking software quality and progress on prior NASA projects. Lessons include the need for quantitative metrics to monitor both in-house software development capability and contractor outputs.
* **Application to This Requirement:**
  + Centers should implement tools and practices for collecting and analyzing software metrics (e.g., defect rates, test coverage, schedule adherence).
  + Incorporating these metrics into contractor monitoring facilitates early identification of risks or performance issues in contractor-delivered software.

#### 7. Use of Commercial Off-The-Shelf (COTS) Software Can Present Risks

* **LLIS Lesson Number: 1482**
* **Summary:** NASA projects using **Commercial Off-The-Shelf (COTS)** software have encountered issues such as lack of customization, insufficient compatibility testing, and inadequate documentation provided by contractors. Centers must have advanced capability to perform integration testing and validation for COTS software.
* **Application to This Requirement:**
  + Center capabilities must include strong testing and integration practices to detect risks when COTS software is used.
  + Monitoring contractors includes ensuring that they test and document how COTS products integrate into mission-specific systems.

#### 8. Ariane 5 Flight 501 Software Failure

* **Non-LLIS-Specific Lesson; Widely Referenced in NASA Studies**
* **Summary:** A catastrophic software failure occurred during the Ariane 5 launch due to unhandled exceptions in reused software. Insufficient processes to test software in the new configuration environment resulted in a mission-ending failure.
* **Application to This Requirement:**
  + Advanced in-house capabilities must include the skill and tools to identify and verify the reusability of software across different configurations.
  + Monitoring contractor capability includes ensuring that reused software is rigorously validated for compatibility in the current project environment.

#### 9. Importance of Cybersecurity Practices in Software Engineering

* **LLIS Lesson Number: 22160**
* **Summary:** Cybersecurity vulnerabilities are often introduced by neglecting robust verification processes. NASA projects have identified risks in both in-house and contractor software, where insufficient secure coding practices or testing of critical vulnerabilities led to threats against mission systems.
* **Application to This Requirement:**
  + Centers should focus on training teams in secure coding and vulnerability testing.
  + Monitoring contractor practices must include verifying their adherence to secure coding standards (e.g., OWASP) and cybersecurity validation steps.

#### 10. Early Identification of Software Deficiencies Saves Costs

* **LLIS Lesson Number: 1329**
* **Summary:** Software issues that escape early development cycles propagate and become exponentially more difficult and costly to address. Early investments in IV&V, software assurance, and adequate software engineering capability yield significant cost savings and risk mitigation.
* **Application to This Requirement:**
  + Centers should adopt continuous improvement practices in early detection capabilities, such as static analysis, automated test suites, and modern code review tools.
  + Monitoring contractors includes verifying that they conduct early and regular reviews of software to catch and fix issues promptly.

### 6.1.2  Conclusion

These Lessons Learned provide clear evidence and justification for the importance of advancing software engineering capabilities and monitoring contractor performance. By incorporating these lessons into their practices:

1. Centers can ensure that their teams are equipped with the tools, processes, and knowledge to develop high-quality software.
2. Contractors can be monitored effectively to deliver software that aligns with NASA’s exacting standards, mitigating mission-critical risks and ensuring alignment with objectives.

These lessons emphasize that improving in-house expertise and properly overseeing external efforts are critical to preventing software failures, reducing costs, and ensuring mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Requirements to be levied on contractors and vendors in the original solicitations and contracts](https://software.gsfc.nasa.gov/lesson-details/87/). **Lesson Number 87**: The recommendation states: "It is critical to include all requirements to be levied on contractors and vendors in the original solicitations and contracts."
* [A large ground system requires dedicated ground Software System Engineers, reporting to the ground system manager.](https://software.gsfc.nasa.gov/lesson-details/147/) **Lesson Number 147**: The recommendation states: "A ground system of this size and complexity requires dedicated ground Software System Engineers, reporting to the ground system manager."
* [Starting the project with sufficient cleared personnel.](https://software.gsfc.nasa.gov/lesson-details/148/)**Lesson Number 148**: The recommendation states: "If your project requires cleared personnel, ensure that the project starts staffed with a sufficient number of them to handle the full information transfer that the project needs."
* [Staff stability is particularly important for highly specialized expertise](https://software.gsfc.nasa.gov/lesson-details/151/)[.](https://software.gsfc.nasa.gov/lesson-details/151/)**Lesson Number 151**: The recommendation states: "Staff stability is particularly important for projects where partners are providing highly specialized expertise."
* [Plan for and build teams that can remain with the project for its duration.](https://software.gsfc.nasa.gov/lesson-details/152/) **Lesson Number 152**: The recommendation states: "Plan for and build teams that can remain with the project for its duration without splitting time with other projects."

# 7. Software Assurance

**SWE-003 - Center Improvement Plans**

2.1.5.2 Center Director, or designee, shall maintain, staff, and implement a plan to continually advance the Center’s in-house software engineering capability and monitor the software engineering capability of NASA's contractors.

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

The objective of this requirement is to ensure that NASA Centers maintain robust, forward-looking plans to continually improve their software engineering capabilities. This includes keeping in-house software engineering teams at the cutting edge of technical expertise and ensuring that contractors meet NASA’s software engineering and assurance standards. Software Assurance (SA) personnel play a critical role in supporting the development, monitoring, and refinement of these plans to enhance quality, safety, and mission success.

This guidance outlines the roles and responsibilities of SA personnel in supporting compliance with this requirement, ensuring effective oversight of both the Center’s capabilities and contractor contributions.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Support the Development of the Software Engineering Capability Plan

1. **Engage in Collaborative Planning**:
   * Collaborate with the Center’s software engineering leadership to contribute to the development and refinement of the **software engineering capability advancement plan**.
   * Ensure that the plan incorporates the integration of software assurance processes, tools, and practices.
2. **Provide Assurance-Specific Input**:
   * Recommend areas for improvement in software assurance capabilities, such as:
     + Expanding expertise in verification and validation (V&V).
     + Strengthening risk and safety analysis efforts, especially for safety-critical software.
     + Adopting modern tools and techniques for bug detection, static analysis, automated testing, etc.
3. **Ensure Alignment with Standards**:
   * Analyze and verify that the plan aligns with NASA standards and directives, such as **NPR 7150.2**[083](#_tabs-<p></p>) and **NASA-STD-8739.8**[278](#_tabs-<p></p>).
4. **Incorporate Metrics and Objectives**:
   * Work with Center leadership to include measurable software assurance goals within the plan, such as:
     + Improved defect detection rates during early development.
     + Coverage metrics for testing and assurance.
     + Anomaly resolution timelines.

#### 7.4.2.2  Participate in Monitoring In-House Software Engineering Capability

1. **Assess Assurance Activities**:
   * Regularly evaluate the performance of in-house software assurance activities, such as:
     + Planning and execution of verification and validation (V&V).
     + Compliance with NPR and NASA software assurance requirements.
     + The implementation of risk management for safety-critical software.
2. **Review Metrics and Trends**:
   * Review internal metrics related to the quality of in-house software engineering practices, including defect rates, compliance ratios, and assurance-related outcomes.
3. **Recommend Training and Tools**:
   * Identify gaps in skills, processes, or tools within the in-house team and:
     + Recommend targeted **software assurance training** programs for relevant personnel.
     + Suggest the adoption of modern assurance tools and methodologies to improve efficiency and rigor.
4. **Leverage Lessons Learned**:
   * Use insights from reviews of past projects and software assurance audits to suggest adjustments to processes and to refine the advancement plan.

#### 7.4.2.3  Monitor and Assess Contractor Capabilities

1. **Establish Contractor Oversight**:
   * Work with the Center leadership to establish processes for monitoring contractor compliance with **NPR 7150.2**, **NPR 8739.8**, and contract-specific assurance requirements.
2. **Perform Audits and Reviews**:
   * Participate in periodic audits or reviews of contractor software assurance processes. Key activities may include:
     + Checking contractor Software Assurance Plans (SAPs) for compliance with NASA standards.
     + Ensuring test plans, risk analyses, and verification methods meet required levels of rigor.
     + Confirming that contractors adhere to tailored IV&V and assurance requirements where applicable.
3. **Evaluate Contractor Metrics**:
   * Obtain and analyze assurance metrics from contractors, such as:
     + Defect density and closure rates.
     + Test coverage and assurance evidence for safety-critical software.
     + Compliance with risk mitigation strategies.
4. **Identify and Address Issues**:
   * If gaps in contractor software assurance capabilities are identified, recommend corrective actions to address issues, such as:
     + Additional monitoring or independent verification.
     + Supporting contractors in improving their assurance practices.

#### 7.4.2.4  Support Continuous Improvement of the Plan

1. **Perform Gap Analyses**:
   * Periodically review the Center’s software assurance capabilities (in-house and contractor) to identify gaps in skills, processes, tools, or compliance.
2. **Propose Improvements**:
   * Based on assessments, suggest refinements to the advancement plan, including:
     + Adoption of emerging technologies like DevSecOps, automated assurance tools, or Model-Based Systems Engineering (MBSE).
     + Updates to quality assurance benchmarks and metrics.
     + Additional training programs tailored to evolving mission needs and challenges.
3. **Promote Knowledge Sharing**:
   * Advocate for cross-Center or Agency-wide initiatives to share lessons learned, best practices, and innovations in software assurance and engineering.
4. **Track and Verify Progress**:
   * Help establish mechanisms to track progress against the objectives and metrics set in the software engineering capability plan. Regularly assess and report whether assurance improvements are achieving intended results.

### 7.4.3  Key Focus Areas for Software Assurance

To successfully support this requirement, SA personnel should focus on the following:

1. **Capability Advancement**:
   * Identify and prioritize the software assurance skills and tools that are essential for addressing evolving challenges in software classification and criticality.
2. **Audit and Oversight**:
   * Ensure that both in-house teams and contractors adhere to NASA’s assurance standards, tailored requirements, and mission-specific expectations.
3. **Training and Development**:
   * Recommend targeted assurance training to improve both in-house and contractor proficiency in key areas such as V&V, safety analysis, and risk assessment.
4. **Metrics and Analysis**:
   * Use assurance metrics to assess and improve the Center’s and contractors’ engineering capabilities.
5. **Risk Management**:
   * Monitor the implementation of assurance activities that address safety-critical risks and ensure mitigation strategies are applied effectively.

### 7.4.4  Expected Outcomes

By implementing and supporting this requirement, Software Assurance personnel will:

1. **Enhance Capabilities**:
   * Ensure that the Center’s software assurance processes, tools, and expertise remain current and effective.
2. **Strengthen Oversight**:
   * Build robust processes for monitoring contractor adherence to NASA standards and their ability to deliver high-quality software.
3. **Increase Consistency**:
   * Promote consistent and standardized application of software assurance requirements across the Center and contractor teams.
4. **Mitigate Risks**:
   * Reduce risks associated with software assurance deficiencies, particularly in safety-critical and mission-critical systems.
5. **Achieve Mission Success**:
   * Contribute to successful missions through improved software quality and safety.

### 7.4.5  Summary

Software Assurance (SA) personnel play an integral role in ensuring Centers maintain and improve their software engineering capabilities. By supporting the development, monitoring, and continual improvement of the capability plan, SA helps drive adherence to NASA standards and fosters high-quality software engineering practices. This includes proactive engagement in assessing in-house capabilities, monitoring contractor compliance, and recommending improvements to ensure both quality and safety-critical objectives are consistently achieved.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status) * [SWE-098 - Agency Process Asset Library](/spaces/SWEHBVD/pages/102695483/SWE-098+-+Agency+Process+Asset+Library) * [SWE-208 - Advancing Software Assurance and Software Safety Practices](/spaces/SWEHBVD/pages/102695328/SWE-208+-+Advancing+Software+Assurance+and+Software+Safety+Practices)        * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) |
