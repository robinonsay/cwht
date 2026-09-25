# SWE-147 - Specify Reusability Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695504. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements

SWE-147 - Specify Reusability Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695504)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695504&showCommentArea=true&showComments=true#addcomment)

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

3.10.1 The project manager shall specify reusability requirements that apply to its software development activities to enable future reuse of the software, including the models, simulations, and associated data used as inputs for auto-generation of software, for U.S. Government purposes.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-147 History

SWE-147 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 3.14.2 The project manager shall specify reusability requirements that apply to its software development activities to enable future reuse of the software, including models used to generate the software. |
| Difference between B and C | Changed "used to generate the software" to "simulations, and associated data used as inputs for auto-generation of software, for United States Government purposes." |
| C | 3.10.1 The project manager shall specify reusability requirements that apply to its software development activities to enable future reuse of the software, including the models, simulations, and associated data used as inputs for auto-generation of software, for United States Government purposes. |
| Difference between C and D | Editorial fix: 'United State' became 'U. S.' |
| D | 3.10.1 The project manager shall specify reusability requirements that apply to its software development activities to enable future reuse of the software, including the models, simulations, and associated data used as inputs for auto-generation of software, for U.S. Government purposes. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 2. Rationale

Software systems are often designed using existing components from other systems. It is recognized that reusing existing software components can help achieve the resulting system more quickly and at a lower cost. However, for software components to be truly reusable, reusability needs to be part of the planned initial development of those components.

Reusability is a cornerstone of modern software development and engineering. This requirement ensures that NASA’s software development activities incorporate the principles of reusability to maximize efficiency, reduce costs, and improve the return on investment for software assets. By specifying reusability requirements, project managers enable the software to serve not just its immediate purpose but also to remain valuable for future projects, models, simulations, and other NASA-related endeavors. This aligns with NASA's commitment to sustainability, standardization, and innovation in its software engineering practices.

### **Key Justifications for Reusability Requirements**

1. **Maximizing Return on Investment (ROI)**

   * Developing high-quality software requires significant investments in time, money, and resources. Reusability ensures that this investment can benefit future projects, reducing the need to replicate software development efforts from scratch. By specifying reusability requirements early, NASA can leverage software assets across multiple missions and initiatives, significantly increasing their lifecycle value.
2. **Reducing Time and Costs for Future Projects**

   * Reusable software components, models, simulations, or auto-generation inputs reduce development cycles for new projects. Rather than building systems or tools from the ground up, project teams can integrate pre-existing, proven components into their workflows, saving time and minimizing costs.
   * For instance, reusable simulations and models can serve as starting points for new designs, eliminating the need for redundant creation of assets to meet similar requirements.
3. **Enhancing Consistency and Standardization**

   * Reusability promotes standardization across software systems by promoting the use of common libraries, codebases, and data standards. This consistency improves the interoperability of unique NASA systems, which is critical for complex, highly integrated missions.
   * Reusable assets allow teams to adopt standardized design patterns and data structures, reducing miscommunication and integration challenges.
4. **Improving Software Quality and Reliability**

   * Software assets designed with reusability in mind are typically modular, thoroughly documented, and well-tested. Reusing previously validated software not only reduces the risk of introducing defects but also ensures that future projects benefit from software that has already demonstrated reliability in operational environments.
   * Additionally, allowing models and simulations to be reused across projects enables improvements to those artifacts over time, enhancing the quality and accuracy of successive versions.
5. **Accelerating Innovation and Supporting Agile Development**

   * Reusable components encourage innovation by enabling developers to focus on mission-specific challenges rather than re-solving common problems. For example, instead of recreating baseline models or simulations for a spacecraft's guidance system, developers can rely on existing tools and focus on advancing their mission-critical functionality.
   * Reuse also aligns with agile development methodologies by allowing teams to quickly adapt existing components or simulations to meet new requirements, enabling faster iterations and experimentation.
6. **Streamlining Software Maintenance and Upgrades**

   * Reusable software artifacts are designed to be modular and well-documented, facilitating easier maintenance and upgradability. As technologies and mission requirements evolve, reusable components can be modified or extended without requiring modifications to the entire system, reducing technical debt and long-term maintenance burdens.
7. **Facilitating Collaboration Across NASA and the U.S. Government**

   * By specifying reusability requirements, NASA contributes to the creation of valuable software assets that can be shared across different projects, Centers, and even Federal agencies. This promotes collaboration and data sharing between teams, organizations, and government entities, ensuring that vital investments in software provide a broader benefit.
   * Common software components enable alignment across organizations, improving mission collaboration and reducing redundant efforts.
8. **Future Proofing for Emerging Technologies**

   * With the increasing use of auto-generation tools and software-driven systems, reusable models, simulations, and input data become critical for supporting next-generation software development practices. This requirement prepares NASA to adapt to new technologies (e.g., AI-driven software design or Model-Based Systems Engineering) by ensuring compatibility through reusable software infrastructure.
9. **Supporting NASA’s Long-Term Goals of Sustainability and Cost Efficiency**

   * Given that many NASA missions span decades, this requirement ensures software assets remain maintainable and reusable for long-term objectives. The design for reuse aligns with NASA's sustainability initiatives by optimizing resources, minimizing waste, and supporting economic stewardship through efficient use of budget allocations.
10. **Meeting U.S. Government and NASA-Specific Needs**

    * Ensuring software reuse for U.S. Government purposes aligns with federal mandates that encourage the sharing of software resources across agencies to prevent reinvention and unnecessary spending. This requirement reinforces NASA's responsibility as a government agency to deliver products that serve the broader public and government interests.

### **Implementation Considerations for Reusability**

* **Specify Requirements Early in the Lifecycle:** Address reusability goals during the early phases of software development, such as during requirements gathering and design. It is more cost-efficient to design software for reuse upfront than to retrofit reusable structures later.
* **Adopt Modular Design Principles:** Modular, loosely-coupled software architectures enable easier integration, modification, and reuse of components in future projects.
* **Thorough Documentation:** Software, models, simulations, and data used for auto-generation must be meticulously documented (e.g., purpose, assumptions, data formats) to facilitate reuse by future teams.
* **Well-Defined Standards:** Follow NASA’s software and data standards to ensure compatibility and interoperability of reusable assets across projects and systems.
* **Verification of Reusability:** Conduct testing and validation to confirm that the software artifacts meet reusability criteria and are compatible with potential future use cases.
* **Versioning and Life Cycle Management:** Maintain clear version histories and lifecycle management practices for reusable assets, ensuring their stability, traceability, and evolutionary improvement.

### **Conclusion**

This requirement ensures NASA’s software resources do more than meet the needs of the current project; they also contribute to a larger ecosystem of reusable assets that future projects and U.S. Government endeavors can benefit from. Through careful planning, adherence to reusability principles, and alignment with best practices, this requirement fosters innovation, streamlines processes, reduces costs, and sets NASA up for long-term success in achieving its ambitious space exploration objectives. In doing so, it strengthens NASA’s role as a leader in efficient, sustainable software engineering practices.

# 3. Guidance

## 3.1 Reusing Code

Reusability is a critical component of software engineering that maximizes efficiency, reduces costs, and enhances the longevity of software assets across projects and missions. NASA faces unique challenges when ensuring software reusability, particularly in safety-critical environments. The following sections outline the importance of designing for reuse, planning and executing reuse strategies, and specifying reusability requirements to support future integrations and enhancements. This guidance provides a systematic approach to mitigate the risks and maximize the benefits of software reuse.

Planning, designing, and verifying software for reuse are essential to creating sustainable, efficient, and impactful software systems across NASA projects. Reusability minimizes redundancy, reduces costs, and unleashes the full potential of shared resources. By addressing reusability early in the life cycle, creating detailed documentation, and mitigating the risk of reusing code not designed for reuse, software development teams can build a foundation that supports future projects and NASA’s long-term mission success. Comprehensive reusability requirements and contributions to the Agency Software Catalog will continue to support NASA’s goals of efficiency, innovation, and safety.

#### **Risks of Reusing Code Not Designed for Reuse**

Reusing code not originally designed for reuse can introduce safety, reliability, and integration risks. David B. Stewart’s *"30 Pitfalls for Real-Time Software Developers"* highlights the specific dangers of this practice, particularly for safety-critical systems:

1. **Interdependencies with Other Components**: Code not designed for reuse often has hidden dependencies with other functions, modules, or libraries that make it difficult to extract or adapt a specific portion of the code for a new application.
2. **Unclear or Missing Interfaces**: Non-reusable code may lack well-defined interfaces, increasing the risk of integration failures. If object-oriented, it might not use abstract data types or encapsulation properly.
3. **Excessive Overhead or Functionality Loss**: Reusing poorly structured code often requires including unnecessary components, resulting in inefficiency, or dissecting the code piece by piece, which carries high risks of unintentionally removing needed functionality or creating unintended side effects.

#### **Best Practices for Reusing Existing Code**

* **Avoid Hasty Reuse**: If code was not designed for reuse, analyze its purpose, functionality, and dependencies before migrating it into a new project.
* **Redesign and Re-Implement**: When possible, it is often more efficient to redesign and re-implement the code as reusable, modular components instead of modifying the original non-reusable code. This approach reduces debugging time and establishes a foundation for long-term reuse.
* **Assess Safety and Reliability**: Evaluate how the reused software operates in a new system and ensure that operational constraints, configurations, and functionality align with its intended use in the target environment.
* **Abstract and Modularize**: Refactor critical portions of the reused code into reusable software modules with well-defined interfaces, proper encapsulation, and minimal coupling between components.

## 3.2 Planning for Reuse

Proactive planning for reuse during the software lifecycle ensures that software developed today becomes a valuable asset for future projects. Incorporating reuse requirements early in the project addresses common pitfalls and promotes long-term benefits.

#### **Key Steps for Planning Software Reuse**

1. **Specify Reusability Early in the Software Lifecycle**

   * Identify reusability requirements during the conceptual design and requirements phases. These requirements should address both **development processes** and **technical needs**, and should be reflected in essential project documents such as:
     + Software Development/Management Plans.
     + Software Requirements Specifications.
     + Software Coding Standards.
     + Configuration Management Plans.
2. **Integrate Reuse into Requirements Reviews**

   * Include reusability-related requirements in normal review and validation processes to verify that they outline sufficient documentation, modularity, and extensibility for future projects.
   * Focus on requirements that facilitate:
     + **Documentation and Traceability**: Ensure all code, interfaces, and dependencies are thoroughly documented.
     + **Modularity and Encapsulation**: Separate components into independent, connected units for ease of integration.
     + **Interface Standardization**: Define interfaces that conform to industry or NASA-specific standards.
3. **Address Legal and Licensing Constraints**

   * Record proprietary rights, usage rights, warranties, licensing rights, or transfer rights clearly in project documentation to avoid future legal limitations on software reuse.

## 3.3 Software Catalog of Reusable Code

To streamline reuse across NASA's projects, software should be contributed to the **Agency Software Catalog** (SWE-148) via the NASA Technology Transfer Portal, making it accessible for government inventory reuse.

#### **Reusability Requirements for Cataloged Software**

1. **Technical Validation for Future Projects**

   * Include detailed technical information to help assess whether the software meets future project requirements and environmental constraints.
2. **Comprehensive Documentation**

   * Provide user manuals, developer documentation, and reference materials to reduce the learning curve for integrating the software into new systems.
3. **Support for Testing and Operations**

   * Ensure the software package includes the tools and procedures needed for testing, operations, and ongoing maintenance. This includes test cases, test reports, patching procedures, and configuration files.
4. **Risk and Usage Analysis**

   * Document known risks, defects, and operational constraints of the software to inform future projects about potential limitations and compatibility issues.

## 3.4 Reusability Requirements

Reusability requirements drive the design and creation of software systems that are modular, maintainable, and extensible. These requirements should address documentation, modularity, integration complexity, and software safety.

#### **Core Aspects of Reusability Requirements**

1. **Documentation Requirements**

   * Maintain complete source code with inline comments.
   * Provide design documentation, including architecture, interfaces, and module diagrams.
   * Deliver operations manuals, simulator documentation, and test reports.
2. **Integration Requirements**

   * Specify any interface documentation standards or APIs to support seamless software integration.
   * Provide configuration files or tools needed for integrating software into different system environments.
3. **Safety Assessments**

   * Capture hazard analyses and verification results for reused safety-critical software to ensure it meets the target system’s assurance and reliability requirements.
   * Provide source code access to allow future teams to perform in-depth safety analyses.
4. **Process and Testing Information**

   * Include details about software development processes, tools, and standards used to build the component.
   * Supply testing information, such as test methodologies, code coverage reports, defect tracking logs, and test results.
5. **Known Issues and Limitations**

   * Document known defects, unresolved issues, and "back doors" to help future developers assess risks and security implications.
6. **Support Modular Customization**

   * Enable functionality to be toggled on/off without altering core source code (e.g., compile-time switches or configurable parameters).

#### **Special Considerations for Safety-Critical Software**

* Evaluate reused software with stringent criteria for its safety implications in target systems.
* Account for differences in operational constraints, configurations, or environmental factors that may affect performance or functionality.

**30 Pitfalls for Real-Time Software Developers**

#25 Reusing code not designed for reuse  
Code that is not designed for reuse will not be in the form of an abstract data type or object. The code may have interdependencies with other code, such that if all of it is taken, there is more code than needed. If only part is taken, it must be thoroughly dissected, which increases the risk of unknowingly cutting out something that is needed, or unexpectedly changing the functionality. If code isn’t designed for reuse, it’s better to analyze what the existing code does, then redesign and re-implement the code as well-structured reusable software components. From there on, the code can be reused. Rewriting this module will take less time than the development and debugging time needed to reuse the original code.[481](#_tabs-<p></p>)

See also [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software),

For auto-generated code see Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code). 

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-148 - Contribute to Agency Software Catalog](/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

NASA-specific acquisition process information and resources are available in Software Processes Across NASA (SPAN).

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

Small projects often operate under tighter constraints such as limited resources, reduced budgets, shorter timelines, and smaller teams. Incorporating reusability requirements into these projects requires a tailored and pragmatic approach to balance efficiency with compliance. The guidance below outlines best practices and strategies for enabling reusability while minimizing overhead, ensuring that small projects produce reusable, well-documented software assets that can benefit future initiatives, particularly those within NASA or other U.S. Government agencies.

### **Challenges for Small Projects**

Small projects may face the following challenges when implementing reusability requirements:

1. **Limited Resources:** Small teams may lack dedicated personnel or tools to design modular, reusable components.
2. **Time Constraints:** Building software for reusability can require upfront effort, conflicting with pressure to deliver on tight schedules.
3. **Overhead Risks:** Excessive documentation, testing, or validation requirements can overwhelm small projects.
4. **Potential Complexity:** Integrating reusability into smaller-scale software projects may feel unnecessary if reuse goals are unclear or underfunded.

This guidance addresses these challenges with efficient, scalable strategies tailored to small projects.

### **Strategies and Best Practices**

Small projects can adopt the following practices to comply with reusability requirements efficiently:

#### **1. Define Scoped and Prioritized Reusability Goals**

* Identify critical components of the software that are likely to be reused (e.g., algorithms, models, simulations, APIs, or code modules).
* Focus efforts on making these components reusable instead of applying reusability to every part of the system.
* Document reuse goals in the project’s software development plan to ensure alignment with team efforts and stakeholder expectations.

#### **2. Adopt Lightweight Documentation Standards**

* Apply reduced documentation requirements to small projects while maintaining critical details for reusability. For example:
  + Use concise inline comments in the source code to describe functionality and dependencies.
  + Create high-level design diagrams illustrating system architecture and module interactions.
  + Prepare a basic user guide or operations manual for key components with instructions for setup, execution, and maintenance.

#### **3. Modularity and Encapsulation**

* Design software to be **modular** and **encapsulated**, even at a small scale. Modular software ensures individual components can be reused with minimal dependencies. This can be achieved by:
  + Breaking software into independent, loosely coupled modules with clearly defined interfaces.
  + Using well-established libraries or frameworks to isolate dependencies.
  + Designing code with configurable settings (e.g., parameters or constants) to improve flexibility for future use.

#### **4. Balance Reuse with Project Constraints**

* Start with reusable templates, libraries, or code from the Agency Software Catalog or previously developed NASA projects to meet reusability goals efficiently.
* Avoid spending excessive time reengineering non-critical components for reuse—prioritize simplicity and functionality for small projects.

#### **5. Use Scalable Tools and Processes**

* Use tools and processes that match the scale of the project to promote efficient reusability practices:
  + A lightweight version control platform (e.g., Git) for code tracking and collaborative development.
  + Simple requirements repositories, such as spreadsheets, to document reuse requirements and dependencies.
  + Automated testing frameworks to validate module functionality without extensive manual testing.

#### **6. Incorporate Reusability into Risk Management**

* Evaluate reused components for potential risks (e.g., safety, reliability, performance issues). Tools like lightweight hazard analysis or defect tracking systems can help ensure reuse aligns with project constraints and safety-critical requirements when applicable.

### **Simplified Reusability Requirements for Small Projects**

Small projects should use scaled-down requirements for reusability, focusing on the following essential items:

#### **Documentation**

Simple yet sufficient documentation is key to ensuring small projects enable future reuse. Requirements should include:

* **Source Code Documentation**: Provide inline comments for all critical sections of code, with explanations of inputs, outputs, dependencies, and error handling mechanisms.
* **Design Documentation**: Create lightweight data flow diagrams or component-level design documentation for key reusable modules.
* **Operational Instructions**: Develop high-level usage instructions for models and simulations, covering basic setup and operation.

#### **Integration and Testing**

To ensure components can be reused with minimal effort:

* **Interface Documentation**: Specify inputs, outputs, and APIs for software modules. Keep the documentation concise yet clear.
* **Testing Artifacts**: Provide basic test cases and procedures, focusing on key reusable components.
* **Configuration Information**: Include configuration files or default setup parameters to facilitate integration into other systems.

#### **Risk Mitigation**

Document any risks related to reused software (e.g., defects, limitations, design constraints):

* Address potential safety concerns for reused software, particularly for safety-critical operations.
* Provide defect logs or known bugs to guide future use and prevent unexpected issues.

### **Reusability Planning for Small Projects**

Small teams can ensure a manageable level of reuse by following these streamlined planning steps:

#### **1. Specify Reusability in Early Phases**

* Integrate reusability requirements during requirements gathering and design phases, focusing on reusable components that align with mission needs.
* Reflect these requirements in project documentation, such as coding standards, software requirements specs, and testing plans.

#### **2. Leverage Existing Components**

* Whenever possible, reuse existing code or libraries from the NASA Agency Software Catalog or other verified government sources.
* Evaluate reused software for compatibility with the new system, ensuring functionality aligns with updated operational constraints.

#### **3. Plan Reuse Verification**

Implement simplified verification processes to confirm reusability:

* Use peer reviews or lightweight audits to ensure reusable components meet design and interface standards.
* Perform modular testing to validate reused software independently from other system components.

#### **4. Monitor and Report Reuse Progress**

* Track key performance metrics related to reuse, such as the number of reusable components implemented, successful reuse validations, and unresolved reuse-related defects.
* Document lessons learned during the reuse process to inform future small projects.

### **Example Implementation**

#### **Scenario: Small Project Simulation Reuse**

Imagine a small project developing a simulation for spacecraft trajectory analysis. For reuse by future projects, the simulation team could:

1. Design the simulation as a modular component with configurable inputs for trajectory data and environmental parameters.
2. Provide concise documentation, including an operational guide for setting up the simulation and example use cases.
3. Validate the simulation independently to ensure reliability and performance.
4. Contribute the simulation and its supporting documentation to the NASA Agency Software Catalog for future mission use.

---

### **Benefits of Reusability for Small Projects**

1. **Efficiency Gains**: Reduces duplication of effort, enabling small teams to focus on mission-specific goals while leveraging previously developed components.
2. **Cost Savings**: Minimizes development costs by reusing proven software modules from other projects.
3. **Improved Collaboration**: Facilitates sharing reusable code and resources across NASA Centers and projects.
4. **Future Adaptability**: Ensures small projects deliver software assets that can be integrated into larger systems or long-term missions.

### **Conclusion**

Reusability requirements are achievable and beneficial for small projects when approached with pragmatic strategies. By focusing on modularity, lightweight documentation, integration planning, and leveraging existing resources, small projects can deliver reusable software assets that meet NASA’s long-term goals of efficiency, resource optimization, and scalability while operating within their own constraints. Tailoring reuse planning for small-scale efforts ensures compliance without overwhelming the project team, enabling broader contributions to NASA’s mission success.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-386)

  [NASA Reusable Software](https://nen.nasa.gov/web/software/home?p_p_id=gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_cur=1&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_delta=20&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_orderByCol=modifiedDate&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_orderByType=desc&_gov_nasa_nen_inforesources_web_portlet_InformationResourcesWebPortlet_selectedResourceRecordTypeIds=134 "Click to open in new window")

  NASA developed software eligible for reuse.
* (SWEREF-481)

  [30 Pitfalls for Real-Time Software Developers. Embedded Systems Programming,](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.133.761&rep=rep1&type=pdf "Click to open in new window")

  Stewart, David (1999).
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-592)

  [Reuse of Analysis Software](https://llis.nasa.gov/lesson/2158 "Click to open in new window")

  Public Lessons Learned Entry: 2158.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database provides valuable insights into software engineering practices that emphasize the importance of traceability, maintainability, and reusability. Improving the articulation and applicability of these lessons aligns with NASA’s goal of enhancing software quality and operational efficiency.

Reusing and maintaining software provides significant benefits, but only if executed with careful consideration of compatibility, architecture, and operational requirements. Lessons Learned Numbers 2158 and 838 highlight the importance of thorough review processes, maintainable design practices, and bidirectional traceability to mitigate risks and ensure optimal outcomes across NASA projects. Improving these practices enables NASA to sustain its innovative leadership in software engineering for space exploration and related domains.

### **1. Reuse of Analysis Software (Lesson Number 2158)**

#### **Lesson Learned:**

“When a project plans to reuse existing metrology software for a new application, a thorough **independent review** of the software and its **new interfaces** should be conducted.”

#### **Improved Version:**

#### **Lesson Learned:**

To ensure successful reuse of existing metrology software for new applications, projects must perform thorough **independent reviews** that focus on:

1. **Code Compatibility**: Analyze whether the reused software aligns with the technical and operational requirements of the new application.
2. **Interface Validation**: Evaluate new interfaces for seamless integration, ensuring proper alignment with the reused software’s functionality and avoiding hidden dependencies.
3. **Safety and Reliability Assessments**: Identify potential risks introduced by reusing the software in the new environment (e.g., unexpected behavior due to differing operational constraints).
4. **Documentation Completeness**: Verify that the reused software includes sufficient supporting documentation, such as interface requirements, design specifications, and testing artifacts.

#### **Rationale:**

Reusing metrology software can reduce development time and costs; however, it introduces risks when interfaces, operational constraints, or reliability assumptions change in the new application. An **independent review** mitigates these risks and ensures the reused software functions correctly within its new context.

### **2. Software Design for Maintainability (Lesson Number 838)**

#### **Lesson Learned:**

“By designing maintainable software products, we can update and enhance fielded software much faster and at a lower cost. The software can be reused, thus alleviating costly update time. Also, any faults found in the software can be easily diagnosed and corrected, reducing downtime and meeting delivery schedules. Software maintainability ensures system availability by reducing system downtime.”

#### **Improved Version:**

#### **Lesson Learned:**

Designing software products with **maintainability** as a key principle produces the following benefits:

1. **Cost-Effective Updates and Enhancements**: Maintainable software reduces the time and resources required to introduce updates, modifications, or improvements to fielded systems, ensuring they meet evolving mission needs effectively.
2. **Facilitated Reusability**: Well-structured, maintainable software is easier to adapt and reuse for future projects, minimizing duplication of effort and long-term lifecycle costs.
3. **Simplified Fault Diagnosis and Correction**: By designing software that incorporates clear documentation, modular architecture, and robust error-tracing mechanisms, faults can be quickly identified and resolved, reducing system downtime.
4. **Improved System Availability**: Maintainability supports operational reliability by reducing downtime and ensuring software systems can be repaired or upgraded without extended service interruptions.

#### **Key Practices for Maintainable Software Design:**

* **Modular Architecture:** Design software with independent, loosely coupled modules to simplify updates and isolate faults.
* **Behavioral Transparency:** Provide clear documentation for each module, including functionality, interfaces, constraints, and expected error codes.
* **Robust Testing:** Use automated and regression testing during development to ensure that updates or enhancements do not introduce unintended defects.
* **Ease of Configuration:** Incorporate configuration settings that allow future enhancements or customizations without altering the software’s core logic.

#### **Rationale:**

Prioritizing software maintainability upfront reduces long-term lifecycle costs, accelerates development schedules, and enables higher system availability for NASA missions. Better maintainability translates to fewer disruptions during operations and ensures software systems remain flexible for adaptation and reuse.

### **Enhanced Guidance Across Both Lessons**

#### **Key Link to Bidirectional Traceability:**

Both lessons emphasize the importance of bidirectional traceability when reusing or maintaining software. Bidirectional traceability ensures that every aspect of the software aligns with its requirements, interfaces, constraints, and test results, which is critical for reusability and maintainability. Recommended actions related to traceability include:

1. **Mapping Requirements to Interfaces and Tests**: Ensure all requirements are traceable to software design decisions, interfaces, and operational constraints, both forward (from requirements to implementation) and backward (from implementation to requirements).
2. **Change Impact Assessments**: Use traceability to identify how changes to reused or maintained software will impact the overall system architecture, performance, or safety.
3. **Verification and Validation Tracking**: Confirm that reused or maintained software meets its intended operational requirements through bidirectional traceability with test results and validation artifacts.

#### **Importance for NASA Projects:**

By applying the principles of independent reviews, maintainable design, and traceability, NASA can ensure that both reused and maintained software continues to meet rigorous mission-critical standards, supporting system reliability, adaptability, and long-term sustainability.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Coordination with Export Control Office](https://software.gsfc.nasa.gov/lesson-details/168/). **Lesson Number 168**: The recommendation states: "Coordinate early in the project or release cycle with Export Control and Patent Counsel, via direct real-time communication."

# 7. Software Assurance

**SWE-147 - Specify Reusability Requirements**

3.10.1 The project manager shall specify reusability requirements that apply to its software development activities to enable future reuse of the software, including the models, simulations, and associated data used as inputs for auto-generation of software, for U.S. Government purposes.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project has considered reusability for its software development activities.

## 7.2 Software Assurance Products

No formal software assurance products are identified at this time to specifically address software reuse. As a best practice, software assurance activities should aim to incorporate traceability, documentation, and adherence to reuse considerations throughout the software lifecycle. Adding tailored software assurance tools or reusable templates to assess reusability could be considered for future updates.

Effective software assurance for reusability requires upfront planning, careful documentation, and thorough evaluations throughout the software lifecycle. By integrating reusable software considerations into project plans and lifecycle assessments, addressing ownership and licensing issues, and ensuring comprehensive documentation, small and large NASA projects alike will create sustainable software resources that can benefit future missions. This structured and proactive approach to reuse fosters efficiency, reduces duplication of effort, and promotes collaborative innovation across NASA's software engineering activities.

## 7.3 Metrics for Software Assurance

Metrics play a key role in measuring the effectiveness of software reuse efforts. To monitor and encourage reuse practices, the following metrics should be tracked:

1. **Number of Products Submitted for Reuse**

   * Measure the volume of software products submitted for potential reuse across NASA projects.
2. **Percentage of Developed Products Submitted for Reuse**

   * *Formula*:  
     [ \text{Percentage} = \left( \frac{\text{# of products submitted for reuse}}{\text{Total # of developed products}} \right) \times 100 ]
   * This metric assesses the extent to which developed software products are tagged for reuse.
3. **Percentage of Developed Products Entered in NASA Internal Sharing & Reuse System**

   * *Formula*:  
     [ \text{Percentage} = \left( \frac{\text{# of developed products in Internal Reuse System}}{\text{Total # of developed products}} \right) \times 100 ]
   * Tracks the contribution of reusable components to NASA’s Internal Sharing & Reuse Systems (e.g., Agency Software Catalog).
4. **Ratio of Products Submitted for Reuse to Products Entered in the Internal Sharing System**

   * This ratio helps identify gaps between products designated as reusable and products formally available in NASA’s reuse systems.
5. **Defect Tracking in Reused Software Products**

   * Track defects identified in reused software products as part of validation activities. This can highlight quality or integration issues in components marked as reusable.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance for Software Reuse Assurance

Software assurance plays a crucial role in ensuring that reusability practices are effectively integrated across the software lifecycle. The following steps provide a structured approach to evaluate and guide reusability efforts.

#### **1. Reusability Considerations During Software Development**

* **Determine Reuse Potential in Planning:**

  + Verify whether the project has considered reusability as part of its **software planning**, **process design**, and **software requirements**. If reusability is feasible, ensure it is factored into software plans and requirements early in the lifecycle.
  + Review the Software Development Plan (SDP) and ensure that requirements for reusability have been documented.
* **Review Lifecycle for Reusability Opportunities:**

  + Assess whether software products at different stages (e.g., design, implementation, testing) can be provided for future reuse in other NASA software development activities.
  + Ensure reusability considerations are validated during each software lifecycle peer review or milestone assessment.
* **Leverage Existing Reuse Lists:**

  + Check NASA's **Internal Software Reuse List** or similar systems to identify existing software reusable products that your project may benefit from. Ensure any newly designated reusable software is added to the reuse list for future availability.

#### **2. Ownership, Licensing, and Legal Considerations**

* **Ensure Proper Ownership and Rights:**

  + Confirm that NASA has the appropriate ownership or usage rights for the software product. This includes verifying proprietary rights, usage rights, licensing rights, transfer rights, government purpose rights, and warranty terms (see SWE-027).
* **List of Contributors:**

  + Ensure that all contributors of the software have been documented accurately, with a Civil Servant point of contact (POC) designated for the software product. This is particularly critical for verifying ownership when sharing or reusing software (SWE-217).
* **Third-Party Software Considerations:**

  + Determine whether the software includes commercial or open-source components. If third-party software is involved, ensure compliance with licensing agreements and verify that inclusion will not obstruct future reuse.
* **Collaborate with Legal Expertise:**

  + Consult your Center’s Legal Office if there is any uncertainty regarding ownership, contribution agreements, or rights before submitting software for internal reuse.

#### **3. Documentation for Reusability**

Comprehensive documentation is the cornerstone of safe, reliable, and reusable software. Reusability requirements should ensure that the following items are available:

1. **Design Documentation:** Architectural overviews, system diagrams, and module-level documentation.
2. **Source Code:** Ensure source code is well-commented, modular, and stored in version-controlled repositories.
3. **Development Tools and Configurations:** Provide the tools used for development, testing, and debugging (e.g., setup files, dependencies, and instructions for configuring development environments).
4. **User and Operational Documentation:** Include manuals and usage instructions.
5. **Test Artifacts:** Deliver test cases, reports, procedures, and test results for verification and validation.
6. **Simulation Resources:** Provide models, simulators, or test environments developed to accompany operational software.
7. **Formal Reports:** Submit reports such as Software Assurance evaluation records, inspection reports, hazard analyses, and other verifications.

#### **4. Review and Verify Reused or Third-Party Software**

For software that incorporates **reused** or **third-party components**, conduct thorough reviews to ensure compliance with project requirements:

* **Reuse Disclosure and Documentation:**

  + Verify that the project has documented the reuse of software components, including:
    - Identification of reused code.
    - Known Software Lines of Code (SLOC) for reused components in the Software Development Plan.
    - Testing and risk assessments associated with reused artifacts.
* **Integration Compatibility:**

  + Assess the software’s ability to integrate with the system under development, focusing on interface specifications, modularity, and any additional effort required for integration.
* **Risk Mitigation:**

  + Evaluate risks introduced by reused software, such as unforeseen dependencies, potential defects, or safety concerns in the new operational context.

#### **5. License and Rights Verification for Sharing**

Before software is shared via NASA’s **Internal Sharing & Reuse System** or distributed for use within other NASA projects:

* Verify that the Government holds clear rights in the software or has the appropriate permissions/licenses to share third-party components.
* Address proprietary rights or licensing barriers to prevent potential misuse or legal issues during reuse.
* Document any **restrictions** on the reuse of the software, ensuring they are made clear to potential future users.

#### **6. Learn and Share Best Practices**

* Capture lessons learned and submit them to NASA’s Lessons Learned database for future projects to build upon your reusability successes or challenges.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-148 - Contribute to Agency Software Catalog](/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-217 - List of All Contributors and Disclaimer Notice](/spaces/SWEHBVD/pages/102695548/SWE-217+-+List+of+All+Contributors+and+Disclaimer+Notice) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

This requirement ensures that software, including its associated models, simulations, and data, is developed with reusability in mind, allowing future U.S. Government projects to benefit from the software and avoid unnecessary duplication of effort. The project manager must define and implement reusability requirements to facilitate this, and ensure software artifacts are properly documented, configured, and managed for government accessibility.

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

Below is a breakdown of **objective evidence** demonstrating compliance with this requirement.

---

### **1. Reusability Requirements Documentation**

* **Description:** Evidence that reusability requirements are explicitly defined and communicated to the development teams and suppliers.
* **Examples of Evidence:**
  + **System/Software Requirements Specification (SRS):** A section within the SRS detailing reusability requirements, including U.S. Government ownership rights, file formats, documentation standards, and configuration management.
  + **Reusability Clause in Project Plans:** Documentation in the software development or project management plan (e.g., SDP or PMP) specifying requirements to ensure software artifacts (e.g., models, simulations, and associated data) are reusable across future projects.
  + **Contractual Requirements:** Copies of contracts, Requests for Proposals (RFPs), or Statements of Work (SOWs) that impose reusability conditions on external software suppliers and explicitly include provisions for government reuse.

---

### **2. Ownership and Licensing Agreements**

* **Description:** Evidence verifying that the software, models, simulations, and associated data are owned, or licensing agreements allow future use by the U.S. Government.
* **Examples of Evidence:**
  + **Ownership Declarations:** Documentation confirming that all deliverables, including code, models, and associated data, are the intellectual property of the U.S. Government.
  + **Licensing Agreements:** Agreements signed with suppliers permitting reuse of software and associated components without additional restrictions for future U.S. Government use.
  + **Rights in Data Documentation:** Standard clauses and acknowledgments (e.g., FAR or DFARS clauses) related to government's unlimited or government-purpose data rights.

---

### **3. Version-Controlled Repository Access**

* **Description:** Evidence that the software, models, simulations, and associated data are stored in repositories accessible and traceable for future U.S. Government purposes.
* **Examples of Evidence:**
  + **Repository Records:** Logs or metadata from version control systems (e.g., Git, Subversion, ClearCase) documenting storage of software artifacts for future use.
  + **Access Control Logs:** Evidence showing that authorized U.S. Government personnel have access to the repository for future retrieval.
  + **Repository Metadata:** Documentation describing where models, simulations, and auto-generated software inputs are stored, along with file structure and version records.

---

### **4. Standards for Reusable Software Artifacts**

* **Description:** Evidence that reusable software artifacts conform to established standards, ensuring compatibility and accessibility for future projects.
* **Examples of Evidence:**
  + **Code Development Standards:** Documentation specifying adherence to coding standards (e.g., MISRA, NASA GSFC, or project-specific guidelines) to ensure consistent, maintainable, reusable code.
  + **File Format Specifications:** Evidence that all models, simulations, and associated data are stored in standard, non-proprietary, or widely reusable formats (e.g., XML, YAML, MATLAB, Simulink, SysML, etc.).
  + **Compliance Checklists:** Records demonstrating compliance with project-defined reusability and portability requirements, formalized during design and/or reviews.
  + **Interoperability Reports:** Documentation showing how software artifacts can interface with other systems or projects.

---

### **5. Traceability of Reusable Components**

* **Description:** Evidence confirming the traceability of reusable artifacts from their requirements through to development and testing.
* **Examples of Evidence:**
  + **Requirements Traceability Matrix (RTM):** An RTM mapping reusability requirements to software components, including models and simulations, to confirm reusability is addressed.
  + **Change Logs:** Logs tracking edits or updates to reusable components to ensure traceability for future use.
  + **Configuration Item List:** A list of all software artifacts, models, and simulations designated as reusable and configured for traceability purposes.

---

### **6. Reuse Provisions in Configuration Management**

* **Description:** Evidence that future reuse of software and associated artifacts is enabled through robust configuration management practices.
* **Examples of Evidence:**
  + **Configuration Management Plan (CMP):** A section in the CMP specifying how reusable artifacts (e.g., input models, outputs, and data) will be versioned and retained for government purposes.
  + **Baseline Configuration Records:** Documentation of baselines for all reusable artifacts to ensure their state is preserved for future government use.
  + **Change Management Records:** Logs tracking changes to reusable artifacts to document evolution and facilitate reuse.

---

### **7. Documentation of Reusable Software Artifacts**

* **Description:** Evidence that reusable software artifacts, including their associated models and simulations, are appropriately documented to support future use.
* **Examples of Evidence:**
  + **User Manuals:** Manuals for software, models, and simulations that describe functionality, interfaces, limitations, and usage instructions.
  + **Developer Documentation:** Technical documentation describing the design, architecture, and algorithms of the reusable software for use by future developers.
  + **Metadata Files:** Accompanying metadata files providing descriptions, version information, and usage details for models and simulations.
  + **Execution Environment Specifications:** Documentation of the required hardware and software environments for reproducing or reapplying simulations and models.

---

### **8. Test and Validation Records**

* **Description:** Evidence that reusable software components, models, and simulations have been validated to demonstrate reliability, accuracy, and usability for future applications.
* **Examples of Evidence:**
  + **Validation Reports:** Results of testing that confirm the correctness and reliability of auto-generation input models and their outputs for future reuse.
  + **Test Cases for Reusability:** Listing of test cases specifically designed to confirm that reusable components function properly in different environments or conditions.
  + **Regression Test Logs:** Results of regression testing showing that future modifications or updates preserve the functionality of reusable artifacts.

---

### **9. Review Evidence: Reusability Emphasis**

* **Description:** Evidence from technical reviews and audits to verify that reusability was explicitly addressed during the software development lifecycle.
* **Examples of Evidence:**
  + **Project Review Minutes:** Meeting minutes from requirements, design, or code reviews showing that reusability was discussed, and applicable requirements were implemented.
  + **Peer Review Comments:** Feedback logs confirming compliance with reusability requirements.
  + **Independent Assessment Reports:** Reports from independent evaluators focused on the project's adherence to reusability goals and standards.

---

### **10. Delivery and Acceptance Records**

* **Description:** Evidence showing that reusable software artifacts, along with their associated models and data, were formally delivered to the U.S. Government and accepted for future use.
* **Examples of Evidence:**
  + **Delivery Receipts:** Signed records of delivery of reusable software artifacts, including models and simulations, to the U.S. Government repository.
  + **Acceptance Criteria and Test Results:** Documentation confirming the U.S. Government's review and acceptance of reusable artifacts.
  + **Final Deliverable Inventory:** An indexed list of all reusable artifacts handed over to the U.S. Government at the project’s conclusion.

---

### **Summary Table of Objective Evidence for Requirement 3.10.1**

| **Category** | **Examples of Objective Evidence** |
| --- | --- |
| **Reusability Requirements** | SRS reusability section, Reusability clauses in project plans and contracts. |
| **Ownership/Licensing** | Ownership declarations, Licensing agreements, Rights in data clauses (e.g., FAR/DFARS). |
| **Repository Access** | Repository records, Access logs, Metadata for stored artifacts. |
| **Software Standards** | Code development standards, File format guidelines, Compliance checklists. |
| **Traceability Evidence** | Requirements traceability matrix, Change logs, Configuration item list. |
| **Configuration Management** | Configuration management plan, Baseline configuration records, Change management records. |
| **Artifact Documentation** | User manuals, Developer documentation, Metadata files, Execution environment specs. |
| **Validation Records** | Validation reports, Test cases for reuse, Regression test results. |
| **Review Evidence** | Review minutes, Peer review comments, Independent assessment reports. |
| **Delivery Records** | Delivery receipts, Acceptance reports, Final deliverable inventory. |

---

### **Conclusion**

By collecting and maintaining this evidence, the project can demonstrate compliance with Requirement 3.10.1, enabling efficient reuse of software, models, and simulations for future U.S. Government projects. This approach minimizes duplication of effort, reduces costs, and ensures that components are preserved and ready for reapplication in future mission-critical contexts.
