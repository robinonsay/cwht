# SWE-204 - Process Assessments

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695538. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments

SWE-204 - Process Assessments

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695538)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695538&showCommentArea=true&showComments=true#addcomment)

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

5.5.4 The project manager shall implement process assessments for all high-severity software non-conformances (closed-loop process).

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-204 History

SWE-204 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW  Class A or B only |
| C | 5.5.4 The project manager shall implement process assessments for all high-severity software non-conformances (closed loop process). |
| Difference between C and D | No change |
| D | 5.5.4 The project manager shall implement process assessments for all high-severity software non-conformances (closed-loop process). |

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
| * [A.12 Software Non-conformance or Defect Management](/spaces/SWEHBVD/pages/133235388/A.12+Software+Non-conformance+or+Defect+Management) |

# 2. Rationale

Understand why the high severity software non-conformance or defect occurred and make process changes to avoid additional high severity software non-conformances or defects.  To reduce software defects.

This requirement ensures that high-severity software non-conformances (defects, bugs, or issues that could cause significant harm or failure) are not only resolved, but also thoroughly investigated to identify and address the underlying process weaknesses or gaps that allowed them to occur in the first place. By implementing process assessments in a closed-loop process, projects can reduce the likelihood of recurrence, enhance trust in mission-critical software, and improve the overall quality and reliability of NASA’s software systems.

---

### **Key Rationale**

#### **1. High-Severity Non-Conformances Can Have Critical Consequences**

* High-severity software issues have the potential to:
  + Jeopardize **mission success** by causing complete system failures or degraded functionality during critical operations.
  + Impact **safety** by introducing hazardous conditions for personnel, equipment, or astronauts.
  + Affect **operational reliability** by reducing system availability or performance.
  + Cause **financial and schedule risks** due to costly late-stage fixes and rework.
* Example: A timing failure in embedded software or incorrect calculations in navigation algorithms could have catastrophic effects on the system's performance.

**Process assessment ensures** that these issues are studied in-depth and resolved at their root, preventing downstream impacts.

---

#### **2. The Need to Identify and Eliminate Root Causes**

* A high-severity software non-conformance often stems from underlying process deficiencies, such as:
  + Gaps or failures in requirement elicitation, design, or validation processes.
  + Inadequate testing coverage or failure to analyze specific edge cases.
  + Insufficient software configuration management or documentation.
  + Poor quality assurance or lack of oversight during development/integration.
* Without a process assessment, the root cause(s) could remain undetected, leading to repeated defects that compromise the software’s quality and reliability.

**A process assessment investigates why the non-conformance occurred systematically** and provides recommendations for process improvements, ensuring that similar defects are avoided in the future.

---

#### **3. A Closed-Loop Process Ensures Process Improvements Are Implemented**

* A "closed-loop process" refers to a continuous improvement cycle where:
  1. The non-conformance is identified and analyzed.
  2. The root cause and any contributing processes are assessed.
  3. Corrective actions are proposed and implemented to address both the immediate non-conformance and the process gaps.
  4. The effectiveness of these changes is verified through follow-up assessments.
* Without this closed-loop structure, improvements may remain theoretical, and opportunities for learning and mitigation may be missed.

**The closed-loop process ensures accountability** and feedback into organizational learning and continuous improvement.

---

#### **4. Supports Risk Management and Decision-Making**

* Process assessments on high-severity non-conformances provide leadership with essential insights into the risks associated with software processes and their outcomes. Specifically:
  + They help refine project risk registers by identifying gaps in controls that could translate to additional risks.
  + They improve decision-making regarding resource allocation and process enhancements.

**Proactive risk management** reduces potential losses from future defects and increases the confidence of stakeholders (internal and external to NASA).

---

#### **5. Fosters Safety-Critical and Mission-Critical Resilience**

* NASA missions often involve complex, distributed systems with strict safety requirements. High-severity software defects in any safety-critical pathway can propagate across components, leading to cascading failures that:
  + Disrupt system integrity.
  + Endanger lives.
  + Threaten mission viability.
* By requiring rigorous assessments of the processes that allowed high-severity non-conformances, NASA ensures that safety-critical functions are prioritized, analyzed, and bolstered against future risks.

**This requirement aligns with NASA’s commitment to safety and reliability**, especially in systems where failure is not an option.

---

#### **6. Aligns with NASA's Emphasis on Continuous Improvement**

* NASA has an established culture of learning from past projects, missions, and mistakes. Lessons learned often underscore the importance of investigating and improving processes to prevent similar issues in future projects.
* Implementing process assessments and closing the feedback loop improves software engineering standards, strengthens organizational knowledge, and refines long-term development strategies.

**Key lessons from past NASA missions (e.g., Mars Climate Orbiter, Ariane 5 failure)** illustrate that process failures can be as impactful as technical faults—and often more difficult to detect without rigorous assessment.

---

#### **7. Encourages Consistency Across Development Teams**

* Software development at NASA often involves multiple teams, centers, or external collaborators. By implementing process assessments for high-severity non-conformances, this requirement:
  + Ensures a **consistent methodology** for addressing critical defects across all projects.
  + Promotes uniform adoption of corrective actions and process improvements across different teams.

**Consistency minimizes the risk** of gaps across diverse development projects and ensures agency-wide adoption of best practices.

---

#### **8. Prevents Recurrence of Known Critical Issues**

* High-severity non-conformances often stem from repeatable process failures if not addressed. Examples include:
  + Inconsistent adherence to coding standards.
  + Failure to update test cases for new requirements.
  + Poor management of software dependencies or reused modules.
* By tying non-conformances to specific process failures and implementing remediation, projects can prevent recurrence of similar critical issues across software components.

**The requirement prevents recurrence** of costly, time-consuming defects and reduces long-term risks.

---

#### **9. Cost-Efficiency Through Early Detection**

* Addressing high-severity defects at the process level helps prevent similar issues from surfacing in later lifecycle stages or in operational use, where fixes become more expensive.
  + Late-stage fixes require additional resources (e.g., re-tests or re-design).
  + For deployed systems, recalls, patches, or workarounds can lead to increased costs and reputational damage.
* A process assessment ensures better early defect prevention through improved workflows and methodologies.

**Proactive process improvement reduces the total cost of non-conformance management.**

---

### **Examples Supporting SWE 5.5.4**

1. **Mars Climate Orbiter Loss (1999)**:

   * Problem: A unit conversion error caused the spacecraft to burn up in the Martian atmosphere.
   * Outcome: Root cause analysis revealed inadequate requirements review and validation processes. Process improvements in system integration review and validation were implemented across subsequent missions. This aligns with the intent of SWE 5.5.4.
2. **Ariane 5 Launch Failure (1996)**:

   * Problem: A software overflow error resulted in a catastrophic explosion.
   * Outcome: Root cause analysis determined insufficient testing and reuse processes. Process assessments and changes to verification procedures reduced risks in later launches.
3. **Hubble Space Telescope Mirror Error (1990)**:

   * Problem: A defect in the mirror’s design was not caught during testing, resulting in faulty imaging.
   * Outcome: Process assessments led to improved requirements validation and independent verification procedures for hardware/software testing processes.

---

### **Conclusion**

SWE 5.5.4 is essential for ensuring that NASA closes the loop on high-severity software non-conformances through rigorous process assessments. This requirement serves to:

* Eliminate root causes, preventing defect recurrence.
* Improve safety, reliability, and mission success.
* Reinforce continuous process improvement.
* Enhance NASA-wide consistency and learning.

By addressing process deficiencies identified through high-severity defects and tracking resolutions through a closed-loop process, projects can ensure long-term improvement and mitigate risks for current and future missions.

# 3. Guidance

The following guidance for SWE 5.5.4 provides a clearer structure, enhanced definitions, actionable steps, and tailored methodologies to ensure projects thoroughly investigate high-severity software non-conformances and implement process assessments to prevent recurrence—all as part of a closed-loop process.

## 3.1 Root Cause Analysis

#### **Objective**:

Understand why a high-severity software defect or non-conformance occurred, determine the underlying process failures, and identify targeted actions to prevent recurrence.

#### **Enhanced Guidance**:

* Root Cause Analysis (RCA) is a systematic investigation method that goes beyond troubleshooting the defect itself. It ensures that underlying deficiencies in engineering, management, or organizational processes are identified and addressed.

#### **Steps for Conducting Root Cause Analysis**:

1. **Clearly Identify and Describe the Issue**:

   * Specify the software defect, its functional impact, severity, and operational context (e.g., system failure during critical mission phase).
   * Use precise language to avoid vague problem definitions.
2. **Establish a Robust Timeline**:

   * Create an event timeline tracing the software’s behavior from normal operations to when the defect or failure occurred.
   * Annotate the timeline with critical milestones, contributing events, tests, and decision points.
3. **Separate Root Causes from Causal Factors**:

   * Use event correlation (e.g., cause-effect mapping or Ishikawa/Fishbone diagrams) to distinguish between:
     + **Root Cause(s)**: The fundamental, systemic issue(s) that allowed the defect to manifest.
     + **Causal Factors**: Influences that shaped the problem but are not the source (e.g., environmental stressors, rare conditions).
4. **Link Causes and Effects Visually**:

   * Use tools like causal graphs, cause-effect trees, or 5 Whys analysis to describe the relationship between the root cause(s), contributing factors, and the observed defect.

#### **Goal**:

Ensure the RCA leads to actionable insights that directly address systemic weaknesses and inform long-term corrective actions.

## 3.2 Defining High Severity for the Project

#### **Objective**:

Establish project-specific definitions of "high severity" to ensure focus remains on the most impactful software non-conformances.

#### **Enhanced Guidance**:

* Collaborate with the **engineering team** and **Software Assurance (SA)** to clearly define criteria for high-severity defects, considering the project's mission priorities. Use factors like:

  + **Critical Functionality**: Defects impacting mission-critical or safety-critical functionalities.
  + **Operational Disruption**: Failures that cause significant mission delay or data loss.
  + **Safety**: Software errors leading to hazardous or life-threatening conditions.
  + **System Integrity**: Defects affecting reliability, redundancy, or long-term performance.
* Ensure consistency with **SWE-202: Software Severity Levels**, and categorize issues accordingly (e.g., Critical, Major, Minor).

#### **Practical Application**:

* High-severity defects typically require an RCA and follow-up process improvements. Examples include:
  + Incorrect data resulting in navigation errors.
  + Timing faults disrupting embedded software consistency.
  + Vulnerabilities exposing the system to security risks.

By identifying high-severity issues clearly, projects avoid wasting resources on negligible defects and focus on what truly impacts mission success.

## 3.3 Proactive Management

#### **Objective**:

Shift the mindset from reactive defect correction to proactive prevention of defects by embedding early detection and process improvement practices.

#### **Enhanced Guidance**:

* Utilize **preventative techniques** such as:

  + Comprehensive test coverage, including boundary testing and edge-case scenarios.
  + Design reviews focused on robust error handling and fault tolerance.
  + Static and dynamic code analysis during development phases.
  + Risk analysis tools such as Failure Modes and Effects Analysis (FMEA) to identify potential failure points early.
* Establish processes to analyze "lessons learned" from past defects:

  + Regularly review past high-severity non-conformances to detect trends or repetitive process failures.
  + Incorporate learnings into updated testing, coding standards, and workflows.
* Use **data-driven metrics** to prioritize defect prevention areas (e.g., test effectiveness, defect injection points).

#### **Proactive Mindset**:

Speed of response may be less critical than improving accuracy, precision, and robustness in defect diagnosis and resolution.

## 3.4 Differentiating Root Causes from Causal Factors

#### **Objective**:

Ensure that process assessments identify and resolve systemic root causes, not just causal factors, to prevent recurrence.

#### **Enhanced Guidance**:

* Distinguish between:
  + **Root Cause(s)**:
    - These are the underlying, systemic failures that, if corrected, will prevent the defect from recurring.
    - Examples: Missing test cases, requirements ambiguity, poor coding standard enforcement.
  + **Causal Factors**:
    - Contributing events that shape or exacerbate an issue but are not the fundamental cause.
    - Examples: Unusual stress conditions, hardware-software timing issues.
* During RCA, question beyond the immediate problem (e.g., "Why was this missed?") until reaching the organizational or procedural level.

#### **Checklist for Root Cause Identification**:

* Does removing or correcting this issue prevent future recurrence?
* Does the evidence suggest deep, process-level failure (e.g., engineering, management policy)?

The focus is on solving reasons, not symptoms.

## 3.5 Long-Term Corrective Actions

#### **Objective**:

Ensure identified process weaknesses are remedied through actions that are verified, validated, and institutionalized.

#### **Enhanced Guidance**:

* Tie corrective actions directly to identified root causes and track them in a **closed-loop revision process** to ensure:

  1. Resolution of the specific defect (short-term remediation).
  2. Implementation of actions aimed at preventing similar process failures (long-term measures).
* Examples of corrective actions:

  + Revise the process to eliminate ambiguity in requirements formulation.
  + Train developers to properly use toolchain workflows.
  + Formalize coding standards and hold reviews to detect non-compliance.
  + Restructure test plans for deeper verification of edge cases.
* Verify through **audits or re-tests** that corrective actions were implemented and are effective (e.g., reduced defect recurrence metrics).

#### **Long-Term Success**:

Corrective actions must not only address immediate project needs but create institutional practices for future defect prevention.

## 3.6 Goal: Reduce Software Defects and Non-Conformances

#### **Objective**:

Achieve the overarching NASA software engineering goal of reducing software defects and non-conformances by embedding the lessons learned directly into both the development lifecycle and organizational standards.

#### **Enhanced Guidance**:

* Treat each defect as both a data point and a diagnostic to refine processes.
* Use RCA insights agency-wide to create a library of **"lessons learned"** that drive reliability improvements in the broader NASA software development community.
* Align efforts with **SWE-201: Software Non-Conformances** to ensure consistent and traceable defect tracking, assessments, and closure.

#### Continuous Alignment:

Reduction is achieved not only by fixing the current defect but by crafting a process immune to similar issues in future efforts.

---

### **Definitions and Concepts (Enhanced Clarity)**:

* **Root Cause**: The fundamental reason the issue occurred, inclusive of systemic or process-level failures.
* **Proximate Cause**: The direct but intermediate event leading to the problem.
* **Organizational Factors**: Structural or managerial inefficiencies affecting the system over its lifecycle.
* **Barrier**: Design or operational controls to prevent failure recurrence.

---

### **Final Note: Synergize Reactive and Proactive Techniques**

While RCA and process assessments address past failures, proactive management and long-term corrective actions ensure a forward-looking approach where defect prevention is built into the lifecycle. Continuous improvement strengthens both current and future projects, contributing to NASA's culture of engineering excellence.

| Term | Definition |
| --- | --- |
| Definitions About Root Cause Analysis Cause (Causal Factor) | An event or condition that results in an effect. Anything that shapes or influences the outcome. |
| Proximate Cause(s) | The event(s) that occurred, including any condition(s) that existed immediately before the undesired outcome, directly resulted in its occurrence and, if eliminated or modified, would have prevented the undesired outcome. Also known as the direct cause(s). |
| Root Cause(s) | One of the multiple factors (events, conditions, or organizational factors) that contributed to or created the proximate cause and subsequent undesired outcome, if eliminated or modified, would have prevented the undesired outcome. Typically multiple root causes contribute to an undesired outcome. |
| Root Cause Analysis (RCA) | A structured evaluation method that identifies the root causes of an undesired outcome and the actions adequate to prevent a recurrence. Root cause analysis should continue until organizational factors have been identified, or until data are exhausted. |
| Event | A real-time occurrence describes one discrete action, typically an error, failure, or malfunction. Examples: pipe broke, power lost, lightning struck, the person opened a valve, etc… |
| Condition | Any as-found state, whether or not resulting from an event, that may have safety, health, quality, security, operational, or environmental implications. |
| Organizational  Factors | Any operational or management structural entity that exerts control over the system at any stage in its life cycle, including but not limited to the system’s concept development, design, fabrication, test, maintenance, operation, and disposal.  Examples: resource management (budget, staff, training); policy (content, implementation, verification); and management decisions. |
| Contributing Factor | An event or condition that may have contributed to the occurrence of an undesired outcome but, if eliminated or modified, would not by itself have prevented the occurrence. |
| Barrier | A physical device or administrative control is used to reduce the risk of the undesired outcome to an acceptable level. Barriers can provide physical intervention (e.g., a guardrail) or procedural separation in time and space (e.g., lock-out-tag-out procedure). |

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

See also [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances).

See also [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances).

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects with constrained resources, focused timelines, or lower complexity, the guidance for complying with SWE 5.5.4 can be scaled to remain practical while maintaining adherence to its intent. Below is small-project-specific guidance structured to help teams conduct meaningful process assessments without introducing unnecessary overhead.

---

### **1. Understand the Scope and Prioritize Efforts**

#### **Key Principle**:

Focus on defects or non-conformances that truly impact the project’s success while minimizing effort on less critical issues.

* **Define High Severity Early**:  
  Collaborate with stakeholders—including engineering, software assurance, and the customer—during planning phases to agree on the criteria for "high-severity" defects. Use simplified categories such as:

  + **Critical Issues**: Defects that render the software inoperable, jeopardize safety, or cause mission failure.
  + **Major Issues**: Defects that reduce functionality or performance for critical operations.
  + **Non-Critical Issues**: Low-impact issues that do not affect core operations.
* **Example**: For a small rover control project, a high-severity non-conformance might involve timing errors in motor control that risk rover failure, while spelling glitches in a user interface would not qualify.

#### **Prioritize Root Cause Analysis (RCA)**:

Only perform rigorous RCAs for high-severity non-conformances directly tied to safety-critical, mission-critical, or reliability-critical functions.

---

### **2. Simplified Root Cause Analysis (RCA)**

#### **Key Principle**:

Focus on identifying root causes using lightweight yet effective techniques, taking into account the smaller scale of the project.

#### **Steps for Small Projects**:

1. **Clarify the Problem**:

   * Clearly document the defect's scope and impact in one or two sentences.
   * Example: "Motor controller software failed to switch speed modes during low-battery conditions, causing partial mission failure."
2. **Create a Quick Timeline**:

   * Build a simple timeline of events leading to the defect using informal means, such as a whiteboard, flowchart, or spreadsheet.
   * Example: Identify what subsystem, module, or process triggered the defect (e.g., "Failure occurred during state transition testing under low-battery simulation").
3. **Distinguish Root Causes from Contributing Factors**:

   * Use lightweight tools such as:
     + **5 Whys Analysis**: Ask "Why?" repeatedly to go deeper into the cause.
     + **Cause-Effect Chart**: Use a simple graphic to visualize problem relationships.
   * Outcome: Categorize findings into Root Cause(s) and Contributing Factors.
4. **Use Actionable Templates**:

   * For small projects, reduce documentation burden with a simple RCA template that includes:
     + **Defect Title** and Severity.
     + **Cause Summary**: What went wrong?
     + **Root Cause(s)**: The primary process or system failure.
     + **Contributing Factors**: Secondary effects.
     + **Corrective Actions**: Solutions proposed to prevent recurrence.

---

### **3. Focused Process Assessment**

#### **Key Principle**:

Keep process assessments targeted to avoid unnecessary complexity.

For high-severity non-conformances, assess only the process areas directly impacted. For example:

* If a unit test failure occurs, review test planning and execution processes.
* If integration issues arise, examine interface documentation and build procedures.

#### Questions to Guide the Process Assessment:

1. **What process was followed when the non-conformance occurred?**

   * Example: Did the team skip or shorten design reviews? Were test environments incomplete?
2. **Were there process deficiencies that contributed to the issue?**

   * Example: Was there missing verification or validation for a specific requirement?
3. **What could have been done differently to avoid the non-conformance?**

   * Example: Could better communication between team members or earlier testing have identified the issue?
4. **How can the process be improved?**

   * Suggest corrective or preventive actions specific to the small project’s scale.

---

### **4. Lightweight Long-Term Corrective Actions**

#### **Key Principle**:

Recommend solutions that are practical and sustainable for small teams.

#### Examples of Scaled Corrective Actions:

* **Process Adjustment**: Automate a unit test specific to the detected issue or improve manual test coverage for similar scenarios.
* **Communication Improvement**: Use quick stand-up meetings or shared defect trackers (e.g., a Google Sheet) to ensure issues and fixes are discussed early.
* **Documentation Refinement**: Expand code or system documentation for critical areas instead of creating entirely new processes.
* **Training and Skills Development**: Brief team members on coding or testing best practices relevant to the defect.

#### **Close the Loop**:

Once corrective actions are taken:

* Track the recurrence of similar issues over time (even informally).
* Verify the effectiveness of the change during routine milestone reviews, such as software delivery or testing phases.

---

### **5. Maintain Simplified Metrics**

#### **Key Principle**:

Use a few critical metrics to track non-conformances and their resolutions.

For small projects, limit metrics to actionable data that provides real insight, such as:

1. **# of High-Severity Issues Identified**: Track the total number of critical/major non-conformances.
2. **Time to Closure**: Measure how long it takes to resolve and validate corrective actions.
3. **Recurrence Rate**: Ensure that defects in similar process areas do not reappear.
4. **# of Root Causes Identified and Addressed**: Monitor whether long-term corrective actions are effective.

#### Tools for Small Projects:

* **Spreadsheets**: Use Excel or Google Sheets for metric tracking.
* **Issue Trackers**: Lightweight tools like Trello, Jira (basic plan), or GitHub Issues.

---

### **6. Leverage Existing Tools and Resources**

#### **Key Principle**:

Use tools already in place to minimize effort and maximize output.

Small teams can implement SWE 5.5.4 effectively by leveraging:

* **Open-Source Tools**: Use static analyzers (e.g., SonarQube, ESLint) or lightweight test automation frameworks to prevent recurring defects.
* **Checklists**: Use simple checklists for RCA and process assessments.
* **Existing Project Documentation**: Enhance or directly use the current defect reports, test plans, and logs to identify gaps.

---

### **7. Integration With Small-Scale Workflows**

#### **Key Principle**:

Embed the process into existing workflows to save time.

Instead of establishing standalone, heavy processes:

* Conduct process assessments as part of existing milestones, such as test reviews or sprint retrospectives. Use the time to address defects and discuss improvement actions.
* Schedule focused team discussions after identifying a high-severity issue to collectively consider the root cause, contributing factors, and corrective actions.

#### Example Workflow Integration:

1. Discover High-Severity Defect → Update Issue Tracker → Perform Quick RCA → Present Findings at Next Team Review → Implement and Validate Corrective Actions.

---

### **8. Keep the Focus on the Project Goal**

#### **Key Principle**:

Prioritize effort on activities that align directly with the project’s scope and critical success factors.

* For safety-critical or mission-critical small projects, focus particularly on RCA outcomes that address reliability concerns.
* For simpler systems, reduce the scope of assessments to the essentials needed to achieve operational confidence.

---

### **Example: High-Severity Issue on a Small Project**

#### **Scenario**:

A small CubeSat mission experiences a software failure in its communications module during low-power mode testing. A high-severity defect is logged because the CubeSat loses its ability to transmit data, jeopardizing the mission.

#### **Steps Taken**:

1. **Determine High Severity**: The issue is categorized as high severity because it affects mission-critical operations.
2. **Conduct Root Cause Analysis**:
   * **Defect Identification**: Communications module fails to transition correctly between power states.
   * **Root Cause**: Inadequate test coverage for low-power scenarios and missing edge-case handling in software requirements.
3. **Process Assessment Focus**: Update test plans to include power transition validation in more detail.
4. **Long-Term Corrective Action**: A new step is added to the requirements and test workflow to validate low-power transitions in future CubeSat missions.
5. **Close the Process Loop**: Verify new practices in the next project milestone.

---

### **Conclusion for Small Projects**:

For small projects, applying SWE 5.5.4 means focusing on high-severity issues that matter most and addressing them through streamlined, scalable processes. By simplifying root cause analysis, maintaining lightweight assessments, and emphasizing proactive management, small projects can minimize recurring defects while prioritizing time and resources for their critical goals.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-027)

  [Root Cause Analysis Course](https://satern.nasa.gov/ "Click to open in new window")

   SMA-002-14, provides This course provides training on Root Cause Analysis (RCA) methodology that can be used in both general problem solving and mishap and close call investigations. NOTE: This course is one of five needed to fulfill the requirements for introductory training on NASA mishap investigations in accordance with NPR 8621.1B
   User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-052)

  [NASA ROOT CAUSE ANALYSIS (SMA-002-10)](https://satern.nasa.gov/ "Click to open in new window")

  Introduction to Root Cause Analysis (SMA-002-10) (NASA Root Cause Analysis, combined with the four prerequisite courses, meets the Root Cause Analysis training requirements in NPR 8621.1B) User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-053)

  [NASA ROOT CAUSE ANALYSIS (SMA-SAFE-OSMA-4003)](https://satern.nasa.gov/ "Click to open in new window")

  NASA Root Cause Analysis (SMA-SAFE-OSMA-4003), combined with the five prerequisite courses, meets the Root Cause Analysis training requirements in NPR 8621.1B). User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-054)

  [NASA Procedural Requirements for Mishap and Close Call Reporting, Investigating, and Recordkeeping](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8621&s=1C "Click to open in new window")

  NPR 8621.1C, Office of Safety and Mission Assurance,
  Effective Date: May 19, 2016, Expiration Date: May 19, 2021
   Also see Mishap Investigation web site at https://sma.nasa.gov/sma-disciplines/mishap-investigation
* (SWEREF-058)

  [System for Administration, Training, and Educational Resources for NASA (SATERN)](https://satern.nasa.gov/ "Click to open in new window")

  SATERN is NASA's Learning Management System (LMS) that provides web-based access to training and career development resources.
   Generic Reference to SATERN. User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Training Resources for NASA

* INTRODUCTION TO ROOT CAUSE ANALYSIS (COURSE SMA-002-10) on SATERN. [027](#_tabs-<p></p>)
* NASA ROOT CAUSE ANALYSIS(COURSE SMA-002-14) [052](#_tabs-<p></p>)
* NASA ROOT CAUSE ANALYSIS (COURSE SMA-SAFE-OSMA-4003) [053](#_tabs-<p></p>)

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA's history of complex missions offers valuable insights into the consequences of unmanaged high-severity non-conformances and how process assessments can lead to improvements in software development practices. These lessons learned highlight the importance of conducting thorough root cause analyses, assessing process deficiencies, and implementing corrective actions to prevent a recurrence of critical issues.

---

### **1. Mars Climate Orbiter (MCO) Failure (1999)**

#### **Overview**:

The MCO mission failed due to a navigation error caused by a mismatch between metric and imperial units in software. The spacecraft entered the Martian atmosphere at the wrong altitude and was destroyed.

#### **Root Cause**:

* A software defect resulted from an uncorrected process failure in which metric calculations were not converted for consistency, leading to integration errors.
* The project team lacked sufficient processes to verify software requirements, validate interfaces between integrated subsystems, and catch unit system mismatches.

#### **Lessons Learned**:

1. **Process Improvement**:

   * Software requirements review processes must include steps to validate units of measurement explicitly for all interfaces.
   * Integration and testing processes must verify compatibility among subsystems and catch data inconsistencies early.
2. **Closed-Loop Actions**:

   * Post-deployment corrective actions mandated improved cross-discipline communication and system-level interface validation for all future missions.
3. **Application to SWE 5.5.4**:

   * High-severity non-conformances like mismatched units should trigger a formal process assessment to examine communication protocols, requirements reviews, and validation workflows.
   * Projects must identify organizational factors contributing to missed verifications and revise processes to avoid similar risks.

---

### **2. Apollo 11 Landing Override (1969)**

#### **Overview**:

During the Apollo 11 lunar landing, the computer issued several program alarms (error codes) caused by an overloaded CPU attempting to process sensor data. Despite these alarms, the crew landed successfully due to pre-launch training and robust software failover processes.

#### **Root Cause**:

* The real-time multitasking software was not optimized for handling the specific radar data input received during the landing maneuver.
* The defect resulted from insufficient simulation of real-time operations and communication mismatches between hardware and software teams.

#### **Lessons Learned**:

1. **Process Improvement**:

   * Incorporate real-world scenarios into simulation and testing to detect high-severity timing or load-related issues.
   * Projects must ensure robust collaboration between software and hardware teams to address complex timing dependencies early.
2. **Closed-Loop Actions**:

   * Focus on process improvements that address real-time processing concerns, including hardware/software interaction simulations and better use of test cases.
   * Apollo lessons led to improved simulation environments for real-time scenarios.
3. **Application to SWE 5.5.4**:

   * Assess process gaps in real-time software testing, focusing on scenarios where timing or resource allocation issues could arise.
   * Implement root cause investigations for software interaction failures and refine the process for validating system-level integration.

---

### **3. Ariane 5 Rocket Launch Failure (1996)**

#### **Overview**:

The first launch of the Ariane 5 rocket ended in failure due to a software exception caused by a floating-point operation that produced an unhandled numeric overflow. The software, reused from the Ariane 4, was not modified to account for differences in trajectory parameters.

#### **Root Cause**:

* Failure to assess process weaknesses related to software reuse between significantly different systems.
* Inadequate testing failed to detect the flawed assumptions inherent in the inherited software.

#### **Lessons Learned**:

1. **Process Improvement**:

   * Projects must incorporate process assessments to explicitly evaluate software reuse risks, especially when platform or system contexts differ.
   * Validation and testing processes must account for edge cases involving system parameters outside routine operational ranges.
2. **Closed-Loop Actions**:

   * Post-failure, process assessments mandated stricter reviews of reused software, with clear documentation of assumptions, limitations, and verification of context changes between systems.
3. **Application to SWE 5.5.4**:

   * High-severity non-conformances arising from software reuse should trigger a process assessment to evaluate assumptions, untested edge cases, and changes in operational context.
   * Address reuse-specific process gaps, such as inadequate verification and validation for new contexts, through updated practices.

---

### **4. Hubble Space Telescope (HST) Mirror Issue (1990)**

#### **Overview**:

The Hubble Space Telescope (HST) launched with a significant defect in its primary mirror, suffering from spherical aberration due to a testing error during fabrication. The software and optical systems delivered data as designed, but the flaw was not detected due to insufficient verification processes.

#### **Root Cause**:

* Overreliance on a single flawed test instrument introduced a critical testing blind spot.
* Process gaps existed in independent validation and cross-checking of critical hardware/software testing data.

#### **Lessons Learned**:

1. **Process Improvement**:

   * Ensure redundancy in test and validation strategies, particularly for safety- or mission-critical systems.
   * Implement processes to verify test equipment calibration and assumptions.
2. **Closed-Loop Actions**:

   * Processes were updated to require independent reviews and more rigorous assessments for critical systems.
   * Software and optical system assessments aligned closely with new test validation practices.
3. **Application to SWE 5.5.4**:

   * Perform process assessments whenever high-severity defects arise from missed verification steps, ensuring gaps in test redundancy and validation are corrected.
   * Require root cause analysis for systemic failures caused by overreliance on limited test or validation mechanisms.

---

### **5. Mars Polar Lander (MPL) Loss (1999)**

#### **Overview**:

The Mars Polar Lander mission failed when the spacecraft's landing process triggered premature shutdown of the descent engines. A software design flaw caused the system to interpret vibrations during landing gear deployment as surface contact, triggering engine shutdown too early.

#### **Root Cause**:

* Incorrect software assumptions about sensor data during specific mission phases.
* Inadequate testing of software behavior in response to sensor noise and false positives.

#### **Lessons Learned**:

1. **Process Improvement**:

   * Processes must include specific tests and simulations of sensor data under realistic mission conditions (e.g., vibration, noise).
   * Enhance requirements review to capture edge cases or assumptions about mission-critical sensors.
2. **Closed-Loop Actions**:

   * Future projects mandated comprehensive testing for environmental noise scenarios to ensure the system could differentiate sensor states correctly.
3. **Application to SWE 5.5.4**:

   * Require process assessments to identify gaps in sensor validation testing, edge case scenario design, and requirement clarity.
   * Build feedback loops to continuously refine verification practices for sensor-driven software.

---

### **Key Patterns from NASA’s Lessons Learned**

NASA’s lessons learned reveal recurring patterns of process improvement following high-severity non-conformances:

1. **Importance of Process Assessments**:

   * High-severity defects often highlight systemic weaknesses in requirements, testing, integration, or communication processes.
   * Process assessments ensure systemic issues are corrected at their root.
2. **Critical Role of RCA in a Closed-Loop Process**:

   * Root cause analysis allows teams to identify underlying drivers of defects—not just symptoms—and develop actionable solutions.
   * A closed-loop ensures that these actions are completed and monitored for effectiveness.
3. **Automation and Testing**:

   * Many high-severity defects arise from insufficient testing or unchecked assumptions. Automating tests for edge cases, parameter validation, and interface consistency reduces risk.
4. **Communication and Integration**:

   * Cross-team communication failures frequently contribute to defects. Process assessments often reveal gaps in collaboration or oversight that can be corrected.
5. **Institutional Knowledge**:

   * By sharing lessons learned across organizations, NASA has institutionalized best practices for mitigating high-severity non-conformances.

---

### **Conclusion**

SWE 5.5.4 helps translate NASA’s continuous improvement philosophy into actionable practices. The use of rigorous root cause analysis, process assessments, and closed-loop feedback ensures systemic weaknesses are identified and corrected in a way that eliminates future risk—upholding NASA's commitment to safety, reliability, and mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [FSW/FSSE anomaly investigations and FSW changes](https://software.gsfc.nasa.gov/lesson-details/80/). **Lesson Number 80**: The recommendation states: "Have one FSW/FSSE person not assigned to console support, dedicated specifically to anomaly investigations and FSW changes."
* [Have more responsive CCBs during IOC](https://software.gsfc.nasa.gov/lesson-details/81/). **Lesson Number 81**: The recommendation states: "Have more responsive CCBs during Initial On-Orbit Checkout (IOC),  quickly assembled in response to events with stakeholders with technical expertise and decision authority."

# 7. Software Assurance

**SWE-204 - Process Assessments**

5.5.4 The project manager shall implement process assessments for all high-severity software non-conformances (closed-loop process).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Perform or confirm that a root cause analysis has been completed on all identified high severity software non-conformances, and that the results are recorded and have been assessed for adequacy.

2. Confirm that the project analyzed the processes identified in the root cause analysis associated with the high severity software non-conformances.

3. Assess opportunities for improvement on the processes identified in the root cause analysis associated with the high severity software non-conformances. 

4. Perform or confirm tracking of corrective actions to closure on high severity software non-conformances.

## 7.2 Software Assurance Products

This improved version enhances clarity, structure, and actionable steps to guide software assurance (SA) personnel in executing root cause analyses, tracking corrective actions, and assessing process improvements for high-severity software non-conformances. The guidance ensures a thorough, closed-loop approach while keeping a focus on preventing future issues and improving project outcomes.

The following deliverables are critical for tracking and evaluating software non-conformance issues and process improvements:

1. **Root Cause Analysis Reports**

   * Comprehensive documentation of each root cause analysis (RCA), including the findings and any related problem reports.
   * Include high-severity defect descriptions, causal factors, identified root causes, and recommended corrective actions.
2. **Record of Corrective Action Closures**

   * Document the status of all corrective actions linked to high-severity non-conformances.
   * Include metrics showing closure rates and trends over time, as well as verification of effectiveness.
3. **Process Improvement Status Reports**

   * Include assessments of process deficiencies identified during the RCA and any associated improvement actions taken.
   * Track the implementation status of process changes and monitor their effectiveness in preventing recurrence.
4. **Software Assurance Audit Reports**

   * Provide results of SA audits assessing the adequacy of root cause analyses, closure of corrective actions, and implemented process changes.
   * Document findings and recommendations for additional improvement opportunities.
5. **Lessons Learned Documentation**

   * Summarize insights gained from RCAs and process improvement efforts.
   * Ensure these are recorded in the project’s lessons-learned repository for use in future projects.

## 7.3 Metrics

Software assurance should track metrics to measure progress, identify trends, and validate improvements. Below is an enhanced list of metrics for better tracking and reporting:

#### **Root Cause Analysis Metrics**

* **Number of RCAs Performed**: Total RCA reports completed for high-severity non-conformances.
* **Number of Non-Conformances Identified Per RCA**: Categorized by root cause, severity, and contributing phase.

#### **Corrective Action Metrics**

* **Number of Corrective Actions Raised by SA**: Compare SA contributions to the total corrective actions raised (indicating SA’s involvement).
* **Corrective Action Status Trends**: Track the number of corrective actions (CA) in the following states over time:
  1. Open (including how long they remain open).
  2. In Work.
  3. Closed (including verification of closure efficacy).
* **Average Time to Closure**: Monitor how long, on average, it takes to close corrective actions.
* **Corrective Action Closure Rates**: Identify recurring trends in open vs. closed actions.

#### **Non-Conformance Metrics**

* **Severity Distribution**: Track the distribution of open and closed high-severity non-conformances based on severity level (Critical, Major).
* **Non-Conformance Lifecycle**:
  + **By Life Cycle Phase**: Record how many non-conformances originate in each software development phase (Requirements, Design, Testing, Deployment).
  + **Cumulative Trends**: Monitor cumulative non-conformance numbers (Open, Closed, Severity, Days Open).
  + **Recurring Non-Conformances**: Identify patterns or recurring issues tied to specific root causes or processes.

#### **Process Improvement Metrics**

* **Process Improvement Implementation**: Measure the percentage of identified process changes implemented over time.
* **Effectiveness of Process Changes**: Use recidivism rates (e.g., how often similar non-conformances recur) as indicators of process improvement success.

## 7.4 Detailed Guidance

#### **Task 1: Perform Root Cause Analysis (RCA) for High-Severity Non-Conformances**

* **Objective**: Identify the fundamental causes of high-severity non-conformances and drive long-term solutions.

##### **Steps for RCA Execution**:

1. **Define the Problem**:

   * Identify and focus on non-conformances flagged as high priority. These typically include issues that result in:
     + Complete software crashes.
     + Functional failures preventing primary operations.
     + Safety hazards or erroneous critical outputs.
   * Determine whether high-priority non-conformances can be analyzed as a group or require individual evaluation.
2. **Collect Data**:

   * Gather all relevant data about the defect, including when, where, and under what conditions it occurred. Examples include:
     + Logs, test results, and user reports.
     + Conditions or scenarios (e.g., step in the build/test process) under which the issue arose.
3. **Identify Causes**:

   * Use structured techniques to explore root causes:
     + **Fishbone (Ishikawa) Diagram**: Categorize potential causes into design, requirements, testing, or execution errors.
     + **5 Whys Technique**: Iteratively ask "Why?" to isolate systemic and organizational issues.
4. **Prioritize Causes**:

   * Focus analysis on the root causes with the greatest impact on preventing recurrence. Use evidence from the RCA to confirm findings.
5. **Recommend Solutions**:

   * Provide specific corrective actions to address the root cause:
     + Code fixes or design changes.
     + Test improvements to detect similar issues earlier.
     + Process changes to prevent gaps or errors in future development phases.
6. **Implement Corrective Actions**:

   * Work with the development team to ensure fixes are applied effectively, and software assurance validates the changes.
7. **Monitor and Sustain**:

   * Ensure corrective actions are applied across similar code or requirements to prevent reintroducing the issue elsewhere in the software.

---

#### **Task 2: Confirm Process Analysis**

* **Objective**: Verify that the project has analyzed processes associated with high-severity non-conformance root causes.

##### **Steps to Confirm Process Analysis**:

1. Review process logs, reports, and audit findings to confirm team follow-up.
2. Focus on systemic issues such as:
   * Inadequate requirements elicitation or validation.
   * Weak testing practices, including missing edge case validations.
   * Faulty use of configuration management.
3. Ensure feedback on gaps is documented and communicated to stakeholders.

---

#### **Task 3: Assess Process Improvement Opportunities**

* **Objective**: Identify and act on improvement opportunities for processes linked to identified root cause(s).

##### **Steps to Assess and Improve**:

1. Propose improvements to deficient processes (e.g., better requirements review checklists, additional simulation scenarios, enhanced test automation).
2. Prioritize action items, balancing ease of implementation with impact on defect prevention.
3. Implement pilot studies or phased rollouts of changes.

---

#### **Task 4: Track Corrective Actions to Closure**

* **Objective**: Ensure that corrective actions for high-severity defects are executed and closed in a timely, documented, and verified manner.

##### **Steps for Effective Tracking**:

1. **Monitor Status**:

   * Use an issue tracker (such as Jira or a spreadsheet) to record corrective actions and their states (Open, In Work, Closed).
2. **Verify Completeness**:

   * Ensure all corrective actions address root causes and test for effectiveness.
3. **Review Similar Areas**:

   * Investigate code or requirements similar to those affected by the defect to identify undetected/non-reported issues.
4. **Sustain Oversight**:

   * Revisit corrective actions periodically to ensure sustained effectiveness and prevent re-emergence of issues.

---

### **Summary**

This improved guidance provides clear, structured processes for software assurance personnel to meet the requirements of SWE 5.5.4 effectively. It emphasizes thorough root cause analyses, diligent tracking of corrective actions, and proactive process improvement efforts to ensure that high-severity software non-conformances are resolved at their source—and prevented from recurring.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is tangible, documented information that demonstrates the implementation, execution, and closure of root cause analyses, process assessments, and corrective actions for high-severity non-conformances. This evidence supports compliance with SWE 5.5.4 and shows due diligence in addressing and reducing risks associated with critical software defects.

---

### **Categories of Objective Evidence for SWE 5.5.4**

1. **Root Cause Analysis (RCA) Evidence**  
   Objective evidence must demonstrate that high-severity non-conformances were analyzed to identify root causes and address systemic issues.

   Examples of RCA evidence include:

   * **RCA Reports**:
     + Detailed documentation of the problem, system impacts, and root cause findings.
     + Methods used for the analysis (e.g., Fishbone diagrams, 5 Whys, or cause-effect diagrams).
     + Supporting data from the failure, such as anomaly logs, event timelines, test reports, or telemetry.
   * **Non-Conformance Reports (NCRs)**:
     + Reports describing each non-conformance, including its classification as high-severity.
     + Impact assessment documentation tied to critical mission objectives or safety risks.
   * **Evidence of Grouped RCAs**:
     + Documentation showing related non-conformances were aggregated for collective root cause analysis (if applicable).

---

1. **Corrective Action (CA) Evidence**  
   Objective evidence must demonstrate that corrective actions were identified, implemented, tracked, and validated to address both immediate defects and their root causes.

   Examples of CA evidence include:

   * **Corrective Action Logs**:
     + Records of all corrective actions raised during root cause analysis linked to high-severity non-conformances.
     + Attributes such as action ID, dates raised/resolved, owners, status (Open/In Progress/Closed), and severity.
   * **Closure Records**:
     + Evidence verifying that corrective actions were completed, including code changes, documentation updates, or test case revisions.
     + Validation/verification reports ensuring the corrective actions resolved the defect without introducing unintended side effects.
   * **Test Results After CA Implementation**:
     + Regression test reports confirming the effectiveness of implemented solutions and the absence of related recurring issues.
   * **Trend Metrics**:
     + Data showing trends in corrective action resolutions over time (e.g., open vs. closed actions, days to closure, recurring issues).

---

1. **Process Assessment Evidence**  
   Objective evidence must demonstrate that processes contributing to high-severity non-conformances were reviewed, analyzed, and improved.

   Examples of process assessment evidence include:

   * **Process Assessment Reports**:
     + Analysis of the specific life cycle processes (e.g., requirements review, design, testing, integration, etc.) that contributed to the non-conformance.
   * **Process Gap Documentation**:
     + Evidence of identified weaknesses or failures in the organization's processes (e.g., insufficient requirements validation, inadequate test coverage).
   * **Improvement Recommendations**:
     + Actionable recommendations to improve processes based on the findings from process assessments.
   * **Process Updated Artifacts**:
     + Evidence of changes instituted into affected processes, such as revised procedures, templates, standards, or guidelines to prevent recurrence.
     + Examples include updated requirements review checklists, broadened test case libraries, or enhanced validation workflows.
   * **Audit Reports**:
     + Reports from internal or external audits confirming that process improvements were implemented and followed.

---

1. **Process Monitoring and Sustaining Evidence**  
   Objective evidence must demonstrate that implemented process improvements were monitored and evaluated for long-term effectiveness.

   Examples of monitoring and sustaining evidence include:

   * **Process Review Logs**:
     + Evidence of periodic reviews of the improved processes to ensure ongoing compliance and effectiveness.
   * **Defect Rate Metrics Over Time**:
     + Data demonstrating changes in defect trends after process improvement implementation, such as reduced high-severity defects or faster resolution times.
   * **Lessons Learned Reports**:
     + Documentation summarizing insights related to the non-conformance and how similar defects will be prevented in future projects.
   * **Management Review Results**:
     + Verification sign-offs by stakeholders and leaders that process improvement outcomes align with project goals and risk management strategies.

---

1. **Non-Conformance Tracking and Reporting Evidence**  
   Objective evidence should capture how high-severity non-conformances were tracked, documented, and reported throughout their lifecycle.

   Examples of tracking and reporting evidence include:

   * **Non-Conformance Tracking Logs**:
     + A centralized and up-to-date log of all high-severity non-conformances, including details like severity, lifecycle phase detection, responsible party, and resolution status.
   * **Defect Attribution Data**:
     + Data linking non-conformances to specific processes or lifecycle phases, helping monitor long-term trends (e.g., defects arising in requirements vs. defects arising in design).
   * **Non-Conformance Reports (Summary Level)**:
     + Reports summarizing metrics around high-severity defects, including:
       - Number of high-severity non-conformances found per reporting period.
       - Number of high-severity non-conformances resolved.
       - Average time-to-closure per severity category.
   * **Lifecycle Metrics**:
     + Count of non-conformances by lifecycle phase over time (e.g., how many defects originated in coding vs. testing).

---

1. **Communications and Review Evidence**  
   Objective evidence can also include documentation of team communication, decisions, and oversight during the management of high-severity non-conformances.

   Examples include:

   * **Team Meeting Minutes**:
     + Records of discussions on root cause analyses, corrective actions, and process improvement plans.
   * **Review Agendas/Results**:
     + Evidence of formal reviews of RCAs and corrective actions by the software assurance team, project management, and stakeholders.
   * **Approval Records**:
     + Documentation showing sign-offs on RCA findings, corrective actions, and process improvement recommendations.

---

### **Impact on Project and Compliance**

Providing robust, well-documented evidence not only demonstrates compliance with SWE 5.5.4 but also achieves critical project benefits:

* Improved **reliability** of software systems.
* Reduced **recurrence of defects**, increasing operational efficiency.
* Enhanced **transparency and accountability** during defect resolution.
* Strengthened **institutional learning** through lessons learned and metrics that guide future projects.

Organizing evidence in a consistent, retrievable format ensures readiness for reviews, audits, and lessons-learned activities across NASA projects.

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
