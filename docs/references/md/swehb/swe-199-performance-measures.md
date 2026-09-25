# SWE-199 - Performance Measures

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695532. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695532/SWE-199+-+Performance+Measures

SWE-199 - Performance Measures

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695532/SWE-199+-+Performance+Measures#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695532)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695532&showCommentArea=true&showComments=true#addcomment)

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

5.4.5 The project manager shall monitor measures to ensure the software will meet or exceed performance and functionality requirements, including satisfying constraints.

## 1.1 Notes

The metrics could include planned and actual use of computer hardware resources (such as processor capacity, memory capacity, input/output device capacity, auxiliary storage device capacity, and communications/network equipment capacity, bus traffic, partition allocation) over time. As part of the verification of the software detailed design, the developer will update the estimation of the technical resource metrics. As part of the verification of the coding, testing, and validation, the technical resource metrics will be updated with the measured values and will be compared to the margins.

## 1.2 History

Click here to view the history of this requirement: SWE-199 History

SWE-199 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 5.4.5 The project manager shall monitor measures to ensure the software will meet or exceed performance and functionality requirements, including satisfying constraints. |
| Difference between C and D | No change |
| D | 5.4.5 The project manager shall monitor measures to ensure the software will meet or exceed performance and functionality requirements, including satisfying constraints. |

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
| * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) |

# 2. Rationale

It is very important to consider constraints on resources in the design of a system so that the development effort can make appropriate decisions for both hardware and software components.  As development proceeds, it is important to check regularly that the software is meeting the performance and functionality constraints. These results should be reported at major milestone reviews and regularly to the Project Manager.

This requirement is critical because software's performance, functionality, and compliance with constraints directly impact the success of NASA’s missions and projects. Monitoring measures provides a proactive approach to verifying that the software remains on track to meet all required standards, reduces the risk of late-stage failures, and ensures alignment with mission goals.

---

### **Key Reasons for the Requirement**

#### **1. Ensuring Software Reliability and Mission Success**

* NASA software products are often developed for high-stakes systems, such as space exploration, flight control, and scientific data collection. These systems require software to perform **reliably and accurately** under mission-critical conditions.
* By monitoring software-specific measures (e.g., performance metrics, functional compliance) throughout the lifecycle, the project manager ensures that issues are identified early, reducing the likelihood of catastrophic failures during operations.

---

#### **2. Performance and Functionality Validation**

* Modern software is often complex, with numerous performance and functional requirements to satisfy specific mission needs.
* Monitoring metrics such as **response time, throughput, accuracy, and stability** ensures that performance expectations are consistently met.
* Functional requirements include adherence to project specifications, interface definitions, and system goals. Continuous monitoring ensures that the software development adheres to the **intended scope** and functionality.

---

#### **3. Early Identification of Risks**

* Tracking specific measures allows the project manager to identify **potential risks and deviations** from requirements during development, testing, or integration phases.
  + Examples:
    - Poor defect resolution rates may signal quality issues.
    - Trends in dropped test cases or missed requirements can highlight compliance gaps.
    - Performance regressions during testing could indicate the introduction of inefficiencies.
* Early identification of such trends enables the team to quickly address and mitigate these risks, avoiding significant project delays or cost overruns later.

---

#### **4. Compliance with Mission Constraints**

* Many NASA software systems operate under constraints such as:
  + Limited processing power and memory in embedded systems.
  + Radiation, thermal, and other environmental extremes.
  + Tight deadlines and budgetary constraints for mission integration.
  + Government and regulatory standards for system safety and security.
* Monitoring metrics related to these constraints (e.g., resource usage, timing constraints, adherence to safety/security specifications) ensures the software remains capable of functioning within these boundaries.

---

#### **5. Supporting Stakeholder Confidence and Transparency**

* Regularly monitoring and reporting key measures enables transparency with stakeholders (e.g., managers, engineers, and customers). By providing quantifiable evidence that the project is meeting performance, functionality, and constraint requirements, project managers:
  + Build stakeholder confidence.
  + Ensure alignment between project development and stakeholder expectations.
  + Provide early visibility into challenges and corrective actions.

---

#### **6. Baseline Establishment and Continuous Improvement**

* Monitoring measures allows project managers to establish **baselines** for expected performance and quality. Deviations from these baselines can be flagged for further analysis.
* Lessons learned from monitoring software metrics can be stored and applied to **future projects**, enabling process improvement across NASA’s software engineering practices.

---

#### **7. Avoiding Late-Stage Rework and Reducing Costs**

* Monitoring critical measures during the development lifecycle reduces the cost of addressing issues by catching them earlier.
* Addressing functional gaps, performance bottlenecks, or constraint violations late in the lifecycle (e.g., during integration or after deployment) is considerably more resource-intensive and can jeopardize mission objectives.
* Frequent monitoring ensures **on-going compliance** with requirements, minimizing the need for significant late-stage rework.

---

#### **8. Alignment with NASA’s Engineering Standards**

* This requirement ensures alignment with NASA’s broader **engineering and quality assurance principles** by embedding a robust monitoring culture into software lifecycle processes (e.g., supporting SWE-090 on management and technical measurements).
* NASA’s standards place a strong emphasis on **continuous assessment and traceability**—this requirement enforces those standards by ensuring measurable progress in performance, functionality, and compliance with constraints.

---

#### **9. Supporting Long-Term System Sustainability**

* In many NASA missions, software updates and modifications may be required after initial deployment (e.g., for spacecraft, rovers, or operational ground systems).
* Monitoring measures during the development phase ensures that robust systems are delivered that can be maintained and evolved throughout their lifespan.
* Ensuring software is within resource constraints (e.g., CPU usage, memory limits) enables easier upgrades and reduces technical debt.

Requirement 5.4.5 is essential for **proactive management and verification** of software performance and functionality. Monitoring measures throughout the software lifecycle ensures alignment with mission needs, compliance with constraints, and timely identification of risks. This systematic approach not only reduces the likelihood of costly failures but also enhances software quality, process discipline, and stakeholder confidence—all critical components of NASA’s high-stakes projects.

# 3. Guidance

## 3.1 Requirements Testing

* Software testing spans both **functional** and **nonfunctional requirements**. It is essential to understand the distinction between these two types of requirements:
  + **Functional Requirements**: Define the "what"—i.e., the actions the system or software must perform in response to specific inputs, conditions, or events. Testing these requirements verifies that the software correctly executes its intended operations.
  + **Nonfunctional Requirements**: Define the "how"—i.e., the quality attributes, constraints, and conditions under which the software must operate. Testing these requirements ensures that customer expectations, usability, and mission constraints (e.g., performance, reliability) are being met.
* Effective testing of both types of requirements ensures that the software delivers **both correct functionality** and meets **defined quality attributes** in alignment with mission needs.

### Key Tests for Each Requirement Type:

1. **Functional Testing**: Focus on verifying inputs/outputs, boundary conditions, and expected results.
2. **Nonfunctional Testing**: Target areas like performance, scalability, reliability, usability, and security.

> **Tip**: Identify test goals as early as possible during requirements development and design phases and develop testing strategies aligned with the type of requirement under evaluation.

## 3.2 Functional Requirements

* Monitoring the success of functional requirements begins with creating a robust process. Functional requirements must pass through progressively detailed stages of validation and verification to ensure coverage and correctness:
  1. **Early Validation - Unit Testing Results**:
     + Start with unit testing for each module, subsystem, or function.
     + Metrics to collect:
       - Number of unit tests executed.
       - Percentage of unit tests passed.
       - Number of defects found during unit testing (categorized by severity).
  2. **Issue Detection during Dry-Run Verification**:
     + Dry-run verifications simulate formal verification activities, enabling teams to identify issues in the test setup, procedure, or software itself.
     + Metrics to track:
       - Number of issues found in dry-run verifications.
       - Average time to resolve dry-run issues.
  3. **Formal Verification Success**:
     + Formal verification ensures that requirements are implemented correctly. Successfully verified functional requirements provide reasonable confidence in system behavior.
     + Metrics to collect:
       - Number of requirements successfully verified (against the total).
       - Number of issues or defects identified during formal verification.
       - Number of critical functional issues resolved before verification closure.
* **Guidance**:
  + Use traceability matrices to confirm that all functional requirements have corresponding verification tests.
  + Automate testing where possible to improve test coverage and consistency.
  + Analyze trends across all verification stages to identify areas of improvement in future developments.

## 3.3 Performance Requirements

Performance is a critical aspect of nonfunctional requirements, particularly for NASA software systems that operate within strict mission constraints. Testing for performance ensures that the system can meet its required quality attributes such as reliability, speed, and resource efficiency.

#### **Challenges of Performance Requirements Testing**

* Performance requirements often depend on the interaction between software, hardware, and external systems. Understanding system design and constraints is crucial to crafting realistic and mission-relevant performance tests.
* These requirements can vary greatly across projects and domains. For example, trajectory computation for a spacecraft requires vastly different performance optimization compared to data handling for ground systems.

#### **Common Types of Performance Requirements**

Performance requirements often relate to the software system’s ability to process, respond, or manage resources under specific conditions. Below are examples and considerations:

1. **Peak Demand Processing**

   * Evaluate maximum transactions per second under high-demand periods over a set timeframe.
   * Ensure tolerances for short bursts of high usage. Example: Data throughput during an instrument's fixed observation window.
2. **Sustained Processing**

   * Assess the software’s ability to handle consistent transaction loads over extended periods.
   * Example: Real-time position updates for prolonged satellite operations.
3. **Response Time**

   * Measure the latency of time-critical events, such as servicing interrupts or performing real-time computations.
   * Example: Flight control software handling critical interrupts during descent.
4. **Storage Capacity and Utilization**

   * Confirm that the software does not exceed allowable storage use under typical loads and includes capacity for future mission expansion.
   * Example: Image storage on a space probe operating under limited memory constraints.
5. **Sampling Rates**

   * Test the software's ability to maintain stable acquisition or sampling rates in real time.
   * Example: Calibration of sensors collecting scientific data on fast-changing physical phenomena.
6. **CPU and Memory Utilization**

   * Validate that software can run within specified CPU and memory allowances while maintaining critical system performance.
   * Example: Onboard resource-constrained processors for long-duration missions.

#### **Performance Metrics to Monitor**

The following metrics and measures can guide performance monitoring:

1. **CPU Utilization** (%): Average and maximum utilization during different workload scenarios.
2. **Memory Utilization** (MB, %): Total memory used against available capacity.
3. **Transaction Throughput** (transactions/sec): Successful processing rates under normal and stress-test conditions.
4. **Response Time** (milliseconds): Time to respond to user actions, interrupts, or data requests.
5. **Error/Retry Rates**: Frequency of failed processes or processed events requiring retries.
6. **Latency Variability**: Consistency in response time—with significance to real-time systems.

#### **Reporting Performance Results**

* Test results from performance validation should be shared during **major milestone reviews** (e.g., PDR, CDR, TRR, or ORR), and any observed deficiencies should trigger corrective actions.
* For maintenance upgrades involving software changes, these metrics should be retested to ensure legacy functionality remains unaffected.
* **Guidance**: Use automated tools for profiling, benchmarking, and testing to provide reproducible and detailed results.

### **Additional Resources**

* Refer to **SWE-195** for guidance during the Software Maintenance Phase to plan for long-term performance testing and validation under evolving conditions.
* Review **Software Entrance and Exit Criteria (Topic 7.09)** for comprehensive guidance before transitioning between lifecycle phases.
* **SWE-090 and SWE-093** serve as references for identifying and tracking metrics during all lifecycle stages.
* Consult **Software Assurance Status Reports (Topic 8.52)** for templates on reporting verification and performance results.

Successfully meeting this requirement depends on having a robust testing and metrics framework in place for both functional and performance requirements. Functional testing evaluates the "what" of the system, while performance testing ensures the "how" quality attributes are achieved under mission-specific constraints. By using defined metrics, tailoring tests to system goals, and reporting results throughout the software development lifecycle, project managers ensure that NASA software remains reliable, traceable, and mission-ready.

It is important to remember that functional requirements are the ‘what’ and nonfunctional requirements are the ‘how’. So, the testing of functional requirements is the verification that the software is executing actions as it should, while nonfunctional testing helps verify that customer expectations are being met.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

# 4. Small Projects

When working on smaller projects, adhering to this requirement should be tailored to the constraints of the project, including limited resources, smaller teams, reduced budgets, or shorter timelines. However, small projects still require a systematic approach to ensure performance, functionality, and constraint compliance.

### **Guidance for Functional and Performance Requirements in Small Projects**

#### **1. Simplify Requirements Management**

* Focus on identifying and documenting **only the high-priority functional and performance requirements** that are critical to mission success or customer needs.
* Use simple tools such as spreadsheets, checklists, or lightweight requirement-tracking software (e.g., Excel, Trello, Jira) to manage and track requirements.
* **Useful Tip**: Prioritize requirements using the **MoSCoW method**:
  + **M**ust have: Absolutely essential for the software.
  + **S**hould have: Important but not critical.
  + **C**ould have: Nice to have but not necessary.
  + **W**on’t have: Not in this release or phase.

---

#### **2. Focus on Essential Metrics**

* **Functional Requirements Metrics**:
  + Track the **number of requirements verified** against the total number of functional requirements.
  + Count the **issues found during testing** and number of issues resolved.
* **Performance Requirements Metrics**:
  + Identify at least **one key performance metric** that aligns with your system's primary purpose (e.g., response time for user inputs, CPU/memory usage, or data processing rates).
  + Monitor trends in this key metric during testing (e.g., small-scale stress tests for memory/CPU limits).
* **How-to-do-it with Small Projects**: Focus on a small set of key metrics and avoid overloading the team with unnecessary data tracking. Tie these metrics directly to your project goals.

---

#### **3. Leverage Lightweight Testing Practices**

Testing is crucial for verifying functional and performance requirements, but smaller projects can streamline testing by focusing on essential and efficient approaches.

1. **Unit Tests**:

   * Prioritize creating simple unit tests for critical code modules.
   * Use basic testing frameworks such as Python's `unittest` or Java's JUnit to validate functionality.
2. **Manual Testing for Functionality**:

   * For small-scale projects with limited automation capability, manual verification of functional requirements can suffice. Use checklists or simple test procedures.
   * Example: Verify that a user input form properly validates entries and stores data.
3. **Performance Testing**:

   * Use a **prototyping approach**: Build a prototype of the most performance-critical functionality and perform basic tests for response time or resource usage.
   * Perform manual performance tests under typical or peak workload scenarios to determine if key performance goals are met.
   * Use lightweight tools such as `top`, `htop`, or `Task Manager` for monitoring resource usage during performance tests.

---

#### **4. Involve the Team in Frequent Reviews**

* Host **frequent, informal reviews**, even if the team is small. Spend time collectively reviewing progress on functional and performance metrics.
* Small teams can use "daily standups" or similar agile practices to assess progress and discuss issues related to functional and performance measures.

---

#### **5. Use Simple Infrastructure for Managing Data**

* Centralize tracking and reporting of software measures with low-overhead solutions. Small projects don’t need sophisticated tools; common options include:
  + **Google Sheets or Excel** for tracking requirements, verification status, and metrics.
  + **Basic dashboards** (built in spreadsheets/low-coding tools) to monitor critical performance statistics.
  + **Version Control Tags/Markers** (e.g., Git tags) to indicate completed verification for specific requirements.

---

#### **6. Ensure Proper Constraints Compliance**

For small projects, constraints (e.g., hardware limits, environmental factors) are likely to be simpler but should still be tracked and evaluated:

* Example: **Hardware resource limits** like available memory or CPU utilization for embedded environments.
* How to monitor:
  + Run **simple benchmarks** to assess whether targets are being met (e.g., measure peak memory while running critical processes).
  + Document key constraints in a lightweight format (e.g., a checklist or a section in the project plan) and validate compliance at key stages.

---

#### **7. Adopt Incremental Testing and Monitoring**

* Software development in small projects is often iterative due to resource and time limitations. Break down functional and performance tests into **small, manageable pieces** and verify results incrementally.
* Example Incremental Steps:
  1. Test a single function/module for correctness.
  2. Test combined modules for integration.
  3. Measure performance incrementally after integrating major subsystems.

---

#### **8. Regularly Communicate Progress with Stakeholders**

On small projects, stakeholders (e.g., customers, team leads) are often directly involved with project progress. Use the following lightweight communication techniques to share progress:

* Provide concise updates **on verified requirements** and completed testing during project checkpoints (e.g., weekly meetings, email summaries).
* Share **key performance results** using visual aids such as trend graphs or short test outcome summaries.

---

#### **9. Prepare for Reviews with a Small Checklist**

For milestone reviews or handovers (e.g., small project Phase Closure Reviews), prepare a checklist to ensure you’ve addressed all elements of functional completeness, performance compliance, and constraints.

**Example Checklist for Small Projects:**

* Functional: Are all high-priority requirements verified?
* Performance: Have you validated key performance metrics at least under typical operating conditions?
* Constraints: Are hardware, timing, and environmental constraints met?
* Test Completion: Have required manual or automated tests been executed?
* Risk Tracking: Have risks related to functionality and performance been mitigated or documented?

---

#### **10. Lean into Existing Resources and Best Practices**

Even in small projects, teams can reuse or adapt existing NASA resources to reduce the time required for planning, testing, and monitoring. Examples include:

* Reusing test cases or requirements templates from previous projects.
* Referring to guidance in SWE-195 (Software Maintenance Plan and associated metrics) for improving the project’s lightweight testing approach.
* Using open-source or free tools to handle smaller-scale performance evaluations (e.g., JMeter, Apache Bench for testing transaction rates).

#### **Example Scenario (Small Project Applied Practice)**:

**Scenario**: A small CubeSat mission requires lightweight onboard software for temperature monitoring and transmitting data back to Earth.

* **Functional Verification**:
  + Use manual verification for critical functions such as sensor readings, threshold alarms, and command responses.
  + Track status of functional tests in a simple spreadsheet.
* **Performance Monitoring**:
  + Verify operational CPU utilization does not exceed 50% under peak data transmission. Test this manually using monitoring tools during integration testing.
  + Validate transmission response time under simulated orbital conditions.
* **Reporting**:
  + Summarize tested functionality and performance results in a brief status report shared monthly with stakeholders.

For small projects, simplicity and efficiency are key. By focusing on priority metrics, leveraging lightweight tools/practices, using incremental testing strategies, and maintaining frequent and clear communication, small projects can still effectively meet software functionality, performance, and constraint requirements. This ensures the project's success without exceeding its resource limitations.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The following lessons are drawn from NASA’s **Lessons Learned Information System (LLIS)** and historical practices, tailored to emphasize the importance of monitoring software measures related to **functionality, performance, and constraints**. These lessons highlight real-world examples that emphasize the necessity of adhering to this requirement and the consequences of failing to comply.

---

### **1. Early Definition and Monitoring of Requirements (Functional and Nonfunctional)**

#### **Lesson Learned**:

Failure to define, validate, and verify requirements early in the software lifecycle increases the risk of costly rework, missed functionality, or failure to meet constraints.

* **Case Example**:  
  In a project involving flight control software, insufficient early coordination between software teams and system engineers resulted in late discovery of conflicting functional requirements. The software failed to satisfy interoperability constraints critical to mission operations. This led to delayed delivery and extensive rework during integration testing.
* **Key Takeaway**:

  + Collaborate closely with all stakeholders (e.g., systems engineers, mission designers, customers) during the requirements definition phase.
  + Establish a **requirements baseline** and monitor progress using straightforward metrics like percentage of verified requirements.
  + Update baselines and metrics throughout the lifecycle when requirements evolve.

---

### **2. Verify Functional Requirements Incrementally Through All Lifecycle Stages**

#### **Lesson Learned**:

Functional requirements should be tested incrementally to catch errors early and reduce the risk of software failing to meet mission needs during critical integration or operational phases.

* **Case Example**:  
  The **Mars Climate Orbiter (1999)** failed in part because of incomplete testing of functional requirements. Key unit and integration tests were skipped or assumed successful, leading to undetected discrepancies (e.g., metric unit errors in navigation calculations). This testing gap resulted in the loss of the spacecraft.
* **Key Takeaway**:

  + Test functional requirements **at every lifecycle stage**, starting from unit tests through integration, and finishing with user acceptance or mission simulation tests.
  + Ensure robust traceability of test cases to the original requirements using a **requirements verification matrix (RVM)** or similar tool.
  + Always fully test critical functionality, especially those involving interfaces, navigation, or safety systems.

---

### **3. Monitor and Test for Performance Degradation over Time**

#### **Lesson Learned**:

Performance requirements are difficult to manage during continuous system updates or upgrades (e.g., during long-lasting missions). Without consistent monitoring, performance can degrade and lead to system bottlenecks or failures.

* **Case Example**:  
  In the **Hubble Space Telescope** project, performance metrics such as response times for fine guidance instruments were not initially validated under actual operational loads. When instrument software was upgraded during the mission, this caused unexpected system delays and disrupted mission efficiency. The issue was resolved after additional testing, but only after significant operational delays.
* **Key Takeaway**:

  + Continuously evaluate performance metrics such as processing speed, response time, and resource utilization even after software is deployed.
  + Test software performance for different workload scenarios (e.g., peak usage or high data acquisition periods).
  + Define thresholds for acceptable performance early and monitor against them throughout the lifecycle.

---

### **4. Constraints Compliance Must Be Rigorously Verified**

#### **Lesson Learned**:

Software must comply with **mission constraints** such as limited memory, processing power, environmental conditions, and mission deadlines. Ignoring these constraints can lead to mission failures or inoperability of the system.

* **Case Example**:  
  During the **Mars Polar Lander (1999)** mission, the software failed to meet timing constraints for detecting touchdown events. This critical timing misstep caused the lander’s descent engine to shut off prematurely, resulting in the vehicle crashing on the Martian surface.
* **Key Takeaway**:

  + Include constraints as part of the monitored requirements, and incorporate tests that validate compliance with timing, resource, or system conditions.
  + Develop **constraint-specific test cases**, such as stress tests for CPU/memory or timing validation for real-time systems.
  + Document assumptions about constraints (e.g., processing resources) and validate that these assumptions hold true in real-world environments throughout testing.

---

### **5. Nonfunctional Requirements (e.g., Performance) May Be Overlooked**

#### **Lesson Learned**:

Nonfunctional requirements, such as usability, scalability, and performance, are often underestimated or deferred, leading to problems during late stages of the project. Attention to nonfunctional characteristics is just as important as addressing functional aspects of the system.

* **Case Example**:  
  The **Suomi NPP (National Polar-orbiting Partnership)** weather satellite experienced delays because early nonfunctional performance issues with onboard processing software were not adequately addressed. These delays arose from challenges in scaling software performance under real-world operational loads.
* **Key Takeaway**:

  + Treat nonfunctional requirements as **equal in importance** to functional requirements. Define and monitor **key nonfunctional metrics** such as scalability, reliability, and system resource efficiency during early verification activities.
  + Use performance benchmarks to validate nonfunctional requirements (e.g., stress and load tests relevant to mission scenarios).

---

### **6. Monitor Software Metrics to Avoid Unanticipated System Behavior**

#### **Lesson Learned**:

Software-related failures can stem from inadequate tracking of metrics such as resource utilization or error rates. If metrics are not monitored consistently or thoroughly, latent problems in design or implementation may go unnoticed.

* **Case Example**:  
  The Space Shuttle **Ariane 5 Flight 501 (ESA)** failure was caused by an unhandled software exception stemming from resource overflow. This issue went undetected because system constraints (e.g., input magnitude limits) were not comprehensively tested in simulation.
* **Key Takeaway**:

  + Establish critical resource metrics such as memory usage, transaction rates, and error frequencies early in development.
  + Engage Software Assurance teams to validate whether these metrics are being monitored throughout the lifecycle.
  + Integrate regular **simulation tests**, even for low-probability scenarios, to prevent latent errors from escalating.

---

### **7. Document Issues and Resolutions for Continuous Process Improvement**

#### **Lesson Learned**:

Many failures repeat lessons from earlier NASA projects, demonstrating the importance of maintaining institutional knowledge and sharing lessons learned. Proper issue tracking and resolution documentation helps prevent the recurrence of similar issues.

* **Case Example**:  
  In a project for autonomous spacecraft navigation, recurring bugs were traced back to performance measurement tools used inconsistently in multiple mission software builds. Developers had no centralized knowledge-sharing database to refer to earlier bug resolution hints.
* **Key Takeaway**:

  + Use an issue-tracking system or repository to record, resolve, and document performance and functionality issues.
  + Capture lessons learned with sufficient detail for future reuse, emphasizing corrective actions that can be implemented on subsequent projects.

These NASA lessons highlight the criticality of monitoring and verifying software against **functional, performance, and constraint requirements**. Using metrics, incremental testing, and proper tools to track and document compliance minimizes risks, improves project outcomes, and fosters continuous improvement across projects. Each lesson reinforces the overarching goal: **creating robust, high-quality software systems that meet mission objectives consistently and reliably.**

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-199 - Performance Measures**

5.4.5 The project manager shall monitor measures to ensure the software will meet or exceed performance and functionality requirements, including satisfying constraints.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project monitors and updates planned measurements to ensure the software meets or exceeds performance and functionality requirements, including satisfying constraints.

2. Monitor and track any performance or functionality requirements that are not being met or are at risk of not being met.

## 7.2 Software Assurance Products

#### **Key Products SA Should Deliver:**

1. **Analysis of Software Measures:**

   * Independently examine all provided software measurement and metric data related to performance and functionality requirements. Ensure this analysis identifies any emerging trends, deviations, and risks.
   * Provide a **highlight summary** of specific issues, observations, and early warnings, with clear recommendations to mitigate highlighted risks.
2. **Software Measurement or Metric Data Validation:**

   * Confirm that the measurement data provided by the project is accurate, complete, and up-to-date. This includes validating whether the data aligns with pre-established performance and functionality goals.
   * Example: Review whether performance metrics (e.g., CPU/memory utilization trends) are appropriately derived from testing activities and whether anomalies exist.
3. **Trend and Analysis Reports:**

   * Produce analysis reports that include trend observations over time (for example, defect density dropping post-integration or increasing response time under stress scenarios).
   * Ensure that visual aids (e.g., trend graphs, heatmaps, or dashboards) are provided to make patterns in the data clear and understandable to stakeholders.
   * Highlight threshold breaches or unexpected deviations (e.g., early warnings of requirements test incompletion, unresolved defects, or resource overuse trends).
4. **Status Presentations:**

   * Present **status updates** summarizing current metric trends, early issues, unresolved items, and actions taken by engineering teams as a result of SA’s feedback.
   * Include updates on:
     + Percentage of requirements tested vs. total.
     + Functional gaps or unmet performance goals.
     + Metric-based risks to schedule, cost, or quality.

## 7.3 Key Metrics for Monitoring

Software Assurance personnel must monitor the following key metrics, ensuring alignment with both functional and performance expectations. These metrics provide a quantitative view of whether the software will meet, exceed, or fall short of system requirements:

#### **Functional Metrics:**

* **Requirements Traceability and Completion Metrics:**

  + Percentage of fully tested requirements.
  + Count and assessment of unresolved TBD (To Be Determined), TBC (To Be Confirmed), TBR (To Be Reviewed) requirements.
  + Number of verified requirements compared to project schedule milestones.
* **Defect Metrics:**

  + Number of defects per milestone, categorized by severity (critical, major, minor).
  + Trends in defect closure rates (tracked against the test execution schedule).
* **Testing Metrics:**

  + Number of unit tests planned versus executed.
  + Percentage of unit tests passed/failed.
  + Coverage metrics: Percentage of code covered by tests (e.g., statement, branch, or condition coverage).
* **Process Predictability:**

  + Requirement changes or volatility: Number of requirements updated, added, or deleted at each lifecycle stage.
  + Peer review outcomes: Number of findings from functional artifacts (e.g., design documents, test plans).

#### **Performance Metrics:**

* **Timing and Processing Measures:**

  + Peak demand processing rates (transactions/second).
  + Sustained processing performance (consistency of throughput over extended durations).
  + Event response timing (e.g., time to service interrupts).
* **Resource Utilization Measures:**

  + CPU utilization during typical and stress conditions.
  + Memory utilization trends over time.
  + Storage use for collected data or temporary files.
* **Other Key Performance Indicators:**

  + Sampling rates: Stability and compliance with real-time system requirements.
  + Latency and jitter variability for real-time or critical operations.
* **Corrective Action Closure Rates:**

  + Monitor whether performance-related issues raised in earlier reviews or tests are being addressed, and determine how unresolved actions impact system performance functionality.

> **See also:**

* Topic **8.18 - SA Suggested Metrics.**

## 7.4 Software Assurance Guidance

#### **Task 1: Review and Assess the Project’s Metrics Strategy**

1. **Engage Early & Understand Planned Metrics:**

   * SA personnel should review the **software development and management plans** early to ensure that both functional and performance metrics are explicitly documented, measurable, and relevant to project goals.
   * Confirm whether selected metrics (e.g., pass rates, CPU utilization, defect trends) are updated frequently enough to provide teams with actionable feedback.
2. **Validate Data Collection Strategy:**

   * Confirm that the project team has implemented a robust approach to **collect real, accurate data**, and verify that the gathered metrics align with the established needs for monitoring progress.
   * Example: Confirm test teams are capturing **peak demand processing rates** during performance testing of high-priority subsystems.
3. **Advise on Adjustments to the Metric Set:**

   * If current metrics fail to offer actionable information, advise the engineering team to refine or supplement their metric set.
   * Example: If system latency becomes a critical risk early in integration, recommend adding specific tests focused on interrupt-response time monitoring.

---

#### **Task 2: Independent Analysis of Metrics & Results**

1. **Perform Independent Trend & Risk Assessments:**

   * SA must independently analyze collected software metrics (don’t rely solely on engineering assessments). Focus on uncovering emerging risks that could impact whether requirements will be met.
   * Flag potential risks by comparing actual results against historical benchmarks, predefined acceptance criteria, or expectations based on schedules and lifecycle maturity.
2. **Flag Early Performance and Functionality Risks:**

   * Use collected data and trends to identify possible shortfalls, disruptions, or risks at the earliest opportunity.
   * Example Indicators to Address Immediately:
     + **Unit Test Coverage:** If significantly lower than expected for the current phase, delivery may be delayed.
     + **Requirements Volatility:** If requirements changes are still occurring late in the design or development phases, raise concerns of downstream impacts to implementation or testing.
3. **Avoid Sole Reliance on Project Team Assessments:**

   * Ensure independent analysis is performed. While the project’s engineering team may provide assessments of their collected metrics, SA must validate and verify these conclusions for accuracy and thoroughness.
   * Example: Instead of only accepting engineering conclusions about defect closure progress, track defect trends independently and check if defects are clustering around specific features or subsystems requiring additional attention.

---

#### **Task 3: Support and Communicate Findings**

1. **Provide Actionable Feedback to the Project Team:**

   * Regularly share the results of metric reviews, identifying concrete risks and making clear recommendations such as:
     + Adjusting resource allocations to safety-critical testing.
     + Prioritizing fixes for functionality gaps affecting performance.
     + Conducting interim reviews of metric outliers.
2. **Communicate Risks Proactively in Reviews:**

   * Share SA findings regularly during key milestone reviews (e.g., PDR, CDR, TRR, ORR). Use trend reports, summaries of unmet requirements, or graphs to demonstrate patterns/issues.
   * Highlight areas where metric results are approaching predefined thresholds or deviating significantly from expectations.
3. **Support Continuous Improvement:**

   * Document recurring issues or gaps in metric collection to enhance measurement planning in future phases or related projects.

The success of software assurance in ensuring compliance with functional and performance requirements largely depends on **proactive, independent metric analysis**, frequent review of project progress, and transparent communication of findings. By following this enhanced guidance, software assurance personnel can help identify risks early, address functionality and performance gaps, and build confidence that the software will meet the project's objectives and constraints.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) |

# 8. Objective Evidence

Objective Evidence

Objective evidence consists of artifacts, data, documentation, and results that demonstrate compliance, monitoring, and validation of this requirement. Below is a list of key pieces of objective evidence that project managers and software assurance personnel can collect to verify that the required monitoring measures are in place and are effective.

---

### **1. Requirements Documentation and Traceability Artifacts**

* **System and Software Requirements Documents (SRD/SSD):**
  + Documented functional and performance requirements, including specifications defining "what" the software must do and constraints like timing, resource utilization, or system interfaces.
  + Ensure the requirements are clearly measurable or testable to validate compliance.
* **Requirements Verification Matrix (RVM):**
  + A traceability matrix mapping software requirements to:
    - Planned verification/test activities.
    - Test cases and results.
    - Coverage status (verified, unverified, incomplete).
  + This demonstrates that all functional and performance requirements are fully monitored and verified.
* **Requirements Change Logs:**
  + Logs of requirement updates, showing the history of changes and their impacts on functionality, performance, or constraints.

**Objective Evidence Example**:

* Traceability matrix linking requirements to pass/fail status during system-level testing.
* Confirmation that 100% of High Priority (HP) requirements are tested and verified.

---

### **2. Software Testing Artifacts**

* **Test Plans and Procedures:**
  + Test plans that describe how functional and performance requirements will be validated, including pass/fail criteria.
  + Example: A plan for validating "peak demand processing" under high-load conditions.
* **Test Data and Reports:**
  + Results from testing activities at all lifecycle levels (unit, integration, system-level testing), showing metrics collected for functionality and performance verification.
    - Examples: Unit test execution results, functional integration testing results, real-time performance test logs.
* **Test Coverage Reports:**
  + Percentages of software covered during testing (e.g., statement, branch, or path coverage) as evidence of sufficient functional testing.
* **Test Defect Reports:**
  + Documentation of defects found during testing that impact the software's ability to meet functional or performance requirements.
  + Include closure records for resolved defects.

**Objective Evidence Example**:

* Test execution logs demonstrating that the software achieved required CPU utilization during peak conditions.
* Unit test reports showing all critical modules passed functional verification.

---

### **3. Metrics Collection and Analysis Artifacts**

* **Software Metrics Plans:**
  + Documents describing the planned software metrics (e.g., functional and performance metrics), baseline thresholds, collection schedule, and analysis procedures.
* **Metrics Dashboards and Reports:**
  + Regularly updated charts and reports showing trends over time for essential software metrics, such as:
    1. Requirements verification progress (e.g., percentage of verified requirements).
    2. Test pass/fail rates.
    3. Schedule-related milestones being met.
    4. Performance thresholds (e.g., CPU usage, response time, resource utilization).
* **Deviations or Variance Logs:**
  + Records documenting deviations observed from expected metric trends, thresholds exceeded, or corrective actions taken.

**Objective Evidence Example**:

* Dashboard showing that memory usage stayed within predefined constraints across multiple test iterations.
* A trend graph highlighting defect closure rates improving after systemic coding issues were corrected.

---

### **4. Risk and Issue Management Artifacts**

* **Risk Management Plan (RMP):**
  + Plans showing how software-related risks, such as performance and functionality risks, will be tracked, mitigated, or resolved.
    - Example: Risk logs capturing potential schedule and budget impacts if critical performance metrics are not met.
* **Risk Logs and Status Reports:**
  + Updated logs tracking identified risks related to functional or performance requirements. Ensure each risk has:
    - A mitigation plan.
    - Current resolution or monitoring status.
* **Corrective Action Logs:**
  + Evidence that deficiencies identified in monitoring or testing activities (e.g., unmet requirements, failing metrics) have been addressed through corrective actions, tracked to closure.

**Objective Evidence Example**:

* Risk log documenting analysis and mitigation of schedule risks caused by unresolved TBD requirements.
* Status report showing closure of corrective actions tied to noncompliance of response time requirements.

---

### **5. Reviews and Audit Artifacts**

* **Review Records:**
  + Evidence that key lifecycle reviews (e.g., Preliminary Design Review, Critical Design Review, Test Readiness Review) included evaluations of functional and performance requirements.
  + Records showing how unmet requirements or risks were discussed and resolved during these panels.
* **Peer Review Findings and Resolutions:**
  + Findings from code reviews, design reviews, or requirement walkthroughs identifying gaps in meeting functional or performance goals.
* **Audit Reports:**
  + Results of project audits confirming compliance with plans for collecting and monitoring functional/performance metrics.

**Objective Evidence Example**:

* PDR/Design Review report documenting approval of planned performance metrics for system timing and resource utilization.
* Audit findings confirming software assurance independently analyzed metrics for requirement verification.

---

### **6. Software Performance and Resource Utilization Logs**

* **Performance Test Reports and Logs:**
  + Detailed evidence from test environments demonstrating actual performance of the system under various mission-relevant conditions. Examples include:
    - Stress test reports showing system capacity under peak loads.
    - Real-time performance metrics such as sampling rates or response times during integrated subsystem tests.
* **Resource Utilization Records:**
  + Logs demonstrating resource consumption (CPU, memory, storage, bandwidth) under both normal and stress conditions.

**Objective Evidence Example**:

* Test application logs showing system stayed within allowable utilization limits (e.g., ≤ 80% CPU usage under maximum throughput).
* Data from latency tests showing interrupt handling completed within required real-time constraints.

---

### **7. Configuration and Change Control Documentation**

* **Configuration Management Plan and Logs:**
  + Records showing how software and its metrics collection tools were baselined and configured.
* **Change Requests and Approvals:**
  + Records of changes made to functional or performance requirements, or updates to planned metrics, with clear justifications and impact assessments.

**Objective Evidence Example**:

* Configuration log showing the addition of new functional test cases to verify previously undefined requirements.
* Change request documentation showing updates to test procedure metrics after new hardware constraints were identified.

---

### **8. Lessons Learned and Knowledge Sharing**

* **Lessons Learned Reports:**
  + Documentation collected at the end of the project that describes successes, challenges, and specific lessons regarding how functional and performance requirements were monitored and verified.
* **Post-Mortem Reports:**
  + Analysis of metrics after deployment, noting whether monitoring activities accurately forecasted final software performance and functionality outcomes.

**Objective Evidence Example**:

* Lessons learned documentation highlighting the importance of early metric-trend monitoring for preventing schedule slips.
* Report detailing how overlooked metrics contributed to unmet performance goals during early development phases.

Objective evidence plays a critical role in demonstrating compliance with the requirement to monitor measures ensuring software functionality, performance, and alignment with constraints. By collecting and analyzing artifacts such as metrics reports, test results, review documentation, and performance logs, the project manager and assurance teams can provide confidence that the software is meeting or exceeding its requirements while proactively identifying and resolving issues.

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
