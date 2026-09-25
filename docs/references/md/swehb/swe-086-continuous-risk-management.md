# SWE-086 - Continuous Risk Management

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695470. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management

SWE-086 - Continuous Risk Management

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695470)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695470&showCommentArea=true&showComments=true#addcomment)

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

5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans.

## 1.1 Notes

Project managers should be aware of any risks that remain after mitigations have been completed or after a risk has been accepted.

## 1.2 History

Click here to view the history of this requirement: SWE-086 History

SWE-086 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.2.1 The project shall identify, analyze, plan, track, control, communicate, and document software risks in accordance with NPR 8000.4, Agency Risk Management Procedural Requirements. |
| Difference between A and B | Added mitigation plans to scope of the requirement. |
| B | 5.2.2 The project manager shall identify, analyze, plan, track, control, communicate, and record software risks and mitigation plans in accordance with NPR 8000.4. |
| Difference between B and C | Removes the requirement to "identify";  Removed "in accordance with NPR 8000.4" |
| C | 5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans. |
| Difference between C and D | No change |
| D | 5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans. |

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
| * [A.09 Software Risk Management](/spaces/SWEHBVD/pages/133235385/A.09+Software+Risk+Management) |

# 2. Rationale

The purpose of risk management is to identify potential problems before they occur so that risk-handling activities can be planned and invoked as needed across the life of the product or project. Risk handling activities are intended to mitigate adverse impacts on achieving the project's objectives.

**NPR 8000.4B - Agency Risk Management Procedural Requirements**

1.1 Background  
"1.1.1 Generically, risk management is a set of activities aimed at understanding, communicating, and managing risk to the achievement of objectives. Risk management operates continuously in an activity, proactively risk-informing the selection of decision alternatives and then managing the risks associated with the implementation of the selected alternative."[009](#_tabs-<p></p>)

Identification and management of risks provide a basis for systematically examining changing situations over time to uncover and correct circumstances that impact the ability of the project to meet its objectives.

#### **Overview and Importance**

Embedded flight software plays a critical role in NASA missions, serving as the interface between the spacecraft’s hardware systems and the mission objectives. These software systems are often deployed in harsh, unpredictable environments where failure is not an option. To ensure mission success, managing **software risk** is a core responsibility of the project manager, as risks in embedded flight software can have direct and catastrophic consequences for the spacecraft, mission, and broader objectives.

Requirement **5.2.1**, which mandates the recording, analysis, planning, tracking, controlling, and communication of software risks and their mitigation plans, is particularly crucial in the context of embedded flight software for the following reasons:

---

### **1. Criticality of Embedded Flight Software**

Embedded flight software programs control **critical spacecraft functions** such as navigation, propulsion, communication, system health monitoring, and payload management. These systems must operate with a high degree of real-time precision in environments where recovery or repair is difficult or impossible.

* **Example Scenario:**  
  For example, a risk related to a timing issue in real-time task scheduling can affect communication with ground control, leading to missed commands or data loss. Without careful risk management, such flaws can cascade into mission failure.

This requirement ensures that software-related risks—such as timing issues, processor overloads, or failure modes resulting from software/hardware interactions—are identified, documented, analyzed, and mitigated to prevent such scenarios.

---

### **2. Unique Challenges in Embedded Flight Software**

Embedded flight software introduces unique risks due to its complexity and dependencies, such as:

* **Concurrency Issues:** Embedded systems often perform tasks concurrently, which can cause race conditions or deadlocks.
* **Hardware Constraints:** Limited computational resources, memory, and power impose constraints on the software design, increasing the likelihood of bottlenecks.
* **Environment-Induced Failures:** Embedded flight systems operate in harsh environments, such as deep space, where radiation or extreme temperatures can cause system anomalies or faults in hardware, affecting software behavior.
* **Integration Risks:** Embedded software is tightly coupled with hardware. Risks arise during hardware/software integration, where mismatches, latencies, or incorrect interfacing could cause failures.
* **Updates and Recovery:** Once the spacecraft is deployed, patching or updating the embedded flight software is resource-intensive or infeasible, significantly raising risk impacts if unaddressed pre-launch.

Managing software risks under this requirement ensures that project teams anticipate and systematically address these challenges through rigorous analysis, testing, and proactive planning.

---

### **3. Mitigation of Safety-Critical Failures**

Embedded flight software often controls **safety-critical systems**, such as guidance, navigation, and control (GN&C); propulsion; and avionics. These systems ensure the vehicle can achieve its scientific or operational mission objectives.

Failures in software systems managing GN&C, for example, can cause:

* A spacecraft to veer off course (loss of mission).
* An unintended collision during docking maneuvers (hardware damage or loss of spacecraft).
* Inability to return scientific data (partial or total mission failure).

By addressing and controlling risks, project teams can develop robust mitigation plans to ensure that the embedded software continues to function safely under nominal and off-nominal conditions.

---

### **4. Early Risk Identification Reduces Cost and Effort**

For embedded flight software, identifying risks early in the development life cycle is critical because fixing defects becomes significantly more difficult and expensive in later stages.

* **Cost of Late Detection:**
  + A navigation algorithm defect caught during requirements analysis might be fixed with a few modifications to the specification.
  + However, that same defect detected during integration testing or deployment could require rollbacks, hardware modifications, additional manufacturing, or even delays to the mission's launch.

Recording and analyzing risks early provides the project team with the opportunity to mitigate vulnerabilities proactively, preventing late-stage delays or significant financial and reputational costs.

---

### **5. Effective Communication Enhances Team Collaboration**

Embedded flight software development involves collaboration between **cross-disciplinary teams** (e.g., systems engineering, hardware teams, software assurance, and mission stakeholders). Risks often bridge these disciplines—for example, a thermal control system anomaly may be due to both thermal modeling errors (a hardware issue) and incorrect embedded software responses.

* **Centralized Communication of Risks:**  
  By recording and communicating risks to all stakeholders, project managers promote transparency, alignment, and shared responsibility across disciplines.
* **Collaborative Risk Resolution:**  
  Communicating risks and plans fosters collaboration between hardware, software, and systems teams to address and resolve potential integration challenges.

---

### **6. Traceability and Accountability in Risk Management**

Recording and tracking risks ensures **traceability** and **accountability** throughout the software lifecycle. Embedded flight software projects are subject to rigorous audits, reviews, and external oversight. This requirement ensures that:

* **Audit Readiness:** Risk records provide evidence that the project has systematically considered and managed software risks, aligned with NASA policies (e.g., NPR 7150.2).
* **Continuous Monitoring:** With rigorous tracking, software managers can monitor the status of risks over time and evaluate the effectiveness of mitigation strategies.

For example, if a processor utilization risk is flagged during the design phase, tracking ensures its resolution is verified during integration and testing.

---

### **7. Support for System Reliability and Robustness**

Embedded systems are often expected to operate continuously for the duration of the mission without human intervention. Recording, analyzing, and managing software risks directly supports system reliability by:

* Ensuring that failure scenarios (e.g., bit flips due to radiation, watchdog timer overflows) are addressed with mitigation strategies, such as fault-tolerant architectures or redundancy.
* Validating that error-handling mechanisms are implemented to gracefully handle unexpected anomalies during flight.

Risk management under this requirement ensures that embedded software is robust enough to withstand the challenges of the space environment and mission constraints.

---

### **8. Support for Continual Improvement**

Risk management is not a one-time event—it is an ongoing process throughout the project lifecycle. This requirement encourages continual monitoring and assessment of risks to:

* Identify emerging risks as the project progresses through different stages of the software lifecycle.
* Refine mitigation plans based on project-specific lessons learned or issue recurrence.

For example, software risk analyses from past NASA missions, such as **the Mars Climate Orbiter failure** (due to unit conversion issues) or **the Mars Polar Lander loss** (due to lack of adequate fault protection), provide historical context for mitigating similar risks in future projects.

---

### **9. Compliance with NPR 7150.2 and Other NASA Standards**

This requirement reinforces NASA's broader commitment to high-quality, reliable software processes as stated in **NPR 7150.2** and related standards. Embedded flight software, in particular, often involves safety-critical and mission-critical software classifications. The mandated formal risk management processes (recording, planning, tracking, etc.) are foundational practices required to achieve compliance.

---

### **Conclusion**

From an embedded flight software perspective, Requirement **5.2.1** ensures that all software risks are identified, analyzed, and managed systematically throughout the lifecycle. By mandating rigorous risk management, this requirement:

* Enhances the robustness, reliability, and safety of embedded software.
* Prevents late-stage surprises and cost overruns.
* Supports mission success by ensuring all risks are tracked, owned, and resolved in a transparent, collaborative process.
* Aligns with NASA’s overarching goals of delivering high-quality software for missions in complex and unforgiving operational environments.

This requirement not only minimizes operational and schedule risks but also lays the groundwork for delivering embedded software that performs safely and reliably in even the most challenging mission environments.

# 3. Guidance

#### **Introduction**

Over the last decade, software has become increasingly critical to the success of NASA missions. Embedded systems, real-time processing, safety-critical software, and complex spaceborne systems have made effective **software risk management** a cornerstone for mission reliability and safety. This guidance establishes a framework for identifying, analyzing, tracking, mitigating, controlling, and communicating software risks to minimize project uncertainties and optimize outcomes.

Requirement 5.2.1 emphasizes the need to consistently and thoroughly manage all **software risks** throughout the software development lifecycle. It is essential for software organizations and project teams to embrace the inevitability of some level of risk in all software development efforts. Risks that are not proactively addressed can lead to missed schedules, cost overruns, and potentially catastrophic mission failures.

This updated guidance incorporates processes from **NPR 8000.4** (Agency Risk Management Procedures), NASA's Software Risk Management processes, and best practices gleaned from past project lessons learned. The goal is for all stakeholders in the software development chain to anticipate, document, and mitigate risks promptly while improving overall project outcomes.

---

### **Why Software Risk Management Is Important**

Effective software risk management is vital owing to the following reasons:

1. **Increasing Complexity:** Software often integrates with and controls complex hardware systems, making it prone to interface, timing, and resource issues.
2. **Safety-Critical Operations:** Embedded software failures can directly impact the safety and survivability of spacecraft and crew.
3. **Cost and Schedule Risks:** Late identification of risks leads to expensive rework and re-planning.
4. **Lessons Learned:** Historical mission failures (e.g., Mars Climate Orbiter, Mars Polar Lander) highlight the importance of risk-aware development practices.
5. **Cross-Disciplinary Dependency:** Software risks often originate from or intersect with hardware systems, requiring coordinated risk tracking across teams.

NASA projects must recognize risks as early as possible, document them comprehensively, and continuously monitor them throughout the software lifecycle. Proactivity in addressing risks ensures high-quality software deliverables, reduces costly errors or failures, and protects mission success.

---

### **Improved Guidance for Software Risk Management**

#### **Continuous Risk Management Framework**

NASA's approach to software risk management forms a continuous process that spans **identification**, **analysis**, **planning**, **tracking**, **control**, and **communication of risks**. The diagram from *NASA/SP-2007-6105 (NASA Systems Engineering Handbook)* provides a high-level flow of risk management, emphasizing iterative analysis and management throughout the project lifecycle.

Key activities under this process include:

---

### **Step 1: Identify Software Risks**

The foundation of risk management is to proactively identify risks before they turn into problems. Some vital practices for identifying software risks include:

* **Encourage Diverse Participation:** Involve personnel from multiple disciplines (software, systems engineering, assurance, and safety) to capture risks from different perspectives. Diversity in expertise ensures risks from all functional areas, interfaces, and workflows are considered.
* **Brainstorming and Sessions:** Conduct team workshops to identify risks across cost, schedule, performance, technical, programmatic, and external domains.
* **Use Risk Checklists:**
  + Checklists should incorporate risks identified from past projects, ensuring historical lessons aren't overlooked.
  + Augment the checklist with context-specific risks for the current project.
* **Leverage Lessons Learned:** Review **NASA Lessons Learned Database (LLIS)** and prior project artifacts to identify risks related to software environments, mission architectures, or contract-driven constraints.
* **Software Assurance as Risk Identifiers:** Engage software assurance and safety experts on Change Control Boards (CCB) to highlight risks introduced by software changes, non-conformances, or system trade-offs.
* **Risk Re-Evaluation with Project Change:** Assess project risks each time there is a significant change, such as a requirement deviation, new hardware integration, or timeline alteration.
* **Include Broader Risk Areas:** Remember to investigate risks related to the following categories:
  + **Cost Risks**: Underestimated development or testing complexity.
  + **Schedule Risks**: Unrealistic testing windows, software/hardware coordination delays.
  + **Technical Risks**: New algorithms, error-prone reused code, or incomplete external APIs.
  + **Skill Risks**: Personnel expertise gaps or dependence on key individuals.

#### Key Tools:

* **Topic 7.19 - Software Risk Checklists**
* **Topic 8.24 - Software Assurance Risk**

---

### **Step 2: Record and Categorize Software Risks**

Once software risks have been identified, they must be properly documented and categorized. Best practices for risk documentation include:

* **Define Specific Risk Attributes/Properties:**
  + Assign unique identifiers for traceability.
  + Categorize risks by **severity, likelihood**, and **priority** (e.g., immediate, near-term, far-term).
  + Use **probability-impact matrices** to guide priority.
* **Craft Clear and Actionable Risk Statements:** Use the "Condition and Consequence" format:
  + **Condition:** Circumstances causing uncertainty.
  + **Consequence:** The potential effects if the condition materializes.
  + **Example:** *Condition:* The GN&C algorithm includes significant computational complexity. *Consequence:* Late-stage performance testing may reveal that computation times exceed processor limits, requiring last-minute rework.
* **Track Risk Ownership:** Assign accountability for monitoring, reporting, and addressing each risk.

#### Key Considerations:

* Software-specific risks must be captured in **a centralized organizational database or tracking tool** to support visibility.
* Use hierarchical structures to categorize risks into **system-level (mission critical)** or **subsystem-level (specific software modules, APIs, or algorithms)**.

---

### **Step 3: Analyze Software Risks**

Analyze risks by assessing their **likelihood** and **impact**. Consider the following during analysis:

* **Likelihood Evaluation:**
  + Use qualitative and quantitative techniques to estimate the probability of risk occurrence. For example:
    - Low (1): Process is adequate to prevent occurrence.
    - High (4): Likely to occur with the current approach.
    - Inevitable (5): Cannot be prevented using existing methods.
* **Impact Determination:**  
  Categorize effects across dimensions like technical (safety, operation), schedule (delivery delays), and cost (resource overruns). Use impact classification matrices to define consequences (e.g., unacceptable, major, medium).
* **Prioritize Risks:**
  + Combine likelihood and impact to rank risks.
  + Focus on rare but severe risks first (e.g., probabilistic risk assessments or fault tree analysis for black swan scenarios).

---

### **Step 4: Plan Mitigation Strategies**

For each high-priority risk, develop actionable plans using one of the following strategies:

* **Acceptance:** Accept risks with minimal consequences or those considered unavoidable.
* **Mitigation:** Reduce likelihood (avoid triggers) or minimize impact (safety measures, subsystem redundancy).
* **Avoidance:** Alter project scope or requirements to eliminate the condition entirely.
* **Transfer:** Share/collaborate on risks with contractors or partners.
* **Ongoing Monitoring:** Continue to observe minor risks that don’t yet require intervention.

---

### **Step 5: Track and Control Risks**

Create processes to monitor risks throughout development:

* Maintain a **risk watch list** for low-priority risks and escalate as necessary.
* Conduct regular **risk review meetings** at project milestones.
* Adjust mitigation plans if the risk context changes.

---

### **Step 6: Communicate Risks Effectively**

Open, transparent, and continuous **risk communication** ensures that:

* Stakeholders are aligned on the priority and impact of risks.
* Risk mitigation status is well understood across technical authorities, software assurance, and testing teams.

---

### **Roles and Responsibilities**

| Role | Responsibility |
| --- | --- |
| Project Manager | Approve risk plans and oversee implementation. |
| Software Risk Manager | Document, track, and monitor software risks. |
| Software Team Members | Escalate risks to higher levels, execute mitigation activities. |
| Software Assurance Experts | Monitor, assess, and validate risk information; ensure safety-critical risks are addressed. |

---

### **Conclusion**

Through proactive risk identification, detailed tracking, and continuous communication, software teams can mitigate uncertainties, avoid expensive surprises, and ensure high-quality software delivery while remaining aligned with **NPR 8000.4**. This guidance ensures NASA’s software practices evolve alongside the growing complexity of missions, empowering teams to deliver with confidence in even the most challenging environments.

During the past ten years, the importance and complexity of software have grown enormously. With this change has come an increasing awareness of the substantial risks inherent in software development and the ineffectiveness of the usual method of dealing with risk. It is necessary to manage a list of software-related risks throughout the software development life cycle by the software development organizations even if the project office does not recognize or accept the software risks at the project level.  The requirements are for the software organization to recognize that all software development has some level of risk. Each discipline of a project development team is to maintain a list of potential risk items for the development activities.  The software risk process is handled following NPR 8000.4 process to the extent possible.  The most important thing is that software organizations maintain and address risks throughout the software development process.

Software risks also factor in the software cost estimation process (see [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation)).

This diagram from NASA/SP-2007-6105, NASA Systems Engineering Handbook, [273](#_tabs-<p></p>) provides an overview of a risk management process:

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

## 3.10 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.24 - Software Assurance Risk](/spaces/SWEHBVD/pages/150077537/8.24+-+Software+Assurance+Risk) |

## 3.11 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Risk Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Risk+Management) |

# 4. Small Projects

For small projects, managing software risks may seem less critical compared to large-scale, complex projects; however, it is equally important. Risks, even small ones, can have significant impacts on cost, schedule, and technical success, particularly in projects with limited resources. The objective of this guidance is to provide streamlined, **resource-efficient** risk management practices tailored to small software projects while ensuring compliance with NASA's risk management expectations outlined in **NPR 8000.4.**

---

### **Key Considerations for Small Projects**

1. **Simplicity:** Use lightweight and pragmatic processes to avoid overwhelming resources.
2. **Focus on High-Impact Risks:** Small projects often have fewer resources to address risks, so prioritize the most critical risks based on their **likelihood** and **impact** on cost, schedule, or technical performance.
3. **Proactive Identification:** Unlike large projects with specialized risk teams, small projects should empower all team members to identify and flag risks.
4. **Documentation Fit for Purpose:** Avoid unnecessary complexity in tracking. Use simple tools such as spreadsheets or shared documents to record, manage, and track risks.
5. **Iterative Monitoring:** Use scheduled, short check-ins to review risks without burdening the project timeline.

---

### **Guidance for Small Projects**

#### **1. Identify Software Risks**

* **Tips for Small Projects:**

  + Use the expertise of the small team to brainstorm risks during key meetings, such as kickoff or planning meetings.
  + Focus on risks that directly affect small project constraints (e.g., budget, deadlines, team size, or specific technology limitations).
  + Consider historical risks listed in NASA's **Lessons Learned Database** that apply to software involved in similar projects.
  + Use a simple **risk checklist** to ensure common risks—such as incomplete requirements, technology limitations, or integration issues—are not overlooked.
  + Encourage all team members to flag risks during daily or weekly status meetings.
* **Questions to Ask to Identify Risks:**

  + What could prevent us from delivering the software on time?
  + What parts of the software depend on new or uncertain technology?
  + Are we relying on a specific team member's expertise or external resources?
  + Do any requirements seem incomplete, poorly defined, or likely to change?

---

#### **2. Record and Prioritize Software Risks**

* **Tips for Small Projects:**

  + Use a simple **spreadsheet or checklist** to document risks instead of complex tools.
  + At a minimum, capture the following fields for each risk:
    - A **Risk Statement** that describes the *condition* (e.g., what might go wrong) and *consequence* (e.g., its negative impact).
    - **Probability (Likelihood):** High, medium, or low.
    - **Impact:** High, medium, or low, based on effects on cost, schedule, or functionality.
    - **Risk Owner:** The team member responsible for monitoring and addressing the risk.
    - **Mitigation Plan:** A brief explanation of how the risk will be addressed (e.g., schedule adjustment, additional testing).
* **Example Risk Record (Simple Spreadsheet):**

| **Risk ID** | **Description** | **Probability** | **Impact** | **Risk Owner** | **Mitigation Plan** |
| --- | --- | --- | --- | --- | --- |
| R-001 | Requirements changes late in development. | High | High | Project Lead | Schedule a requirements freeze 2 wks earlier. |
| R-002 | Limited team expertise with new API integration. | Medium | Medium | Developer A | Plan training for team on API usage. |
| R-003 | Underestimated unit test resources. | Low | High | Tester | Adjust test schedule & reallocate time. |

---

#### **3. Analyze and Prioritize the Risks**

* **Tips for Small Projects:**

  + Use a light prioritization system for risks. Assign each risk to one of these three categories based on **Likelihood x Impact**:
    1. **Critical Risks (High-High):** Address these immediately. They represent high-probability, high-consequence scenarios that can jeopardize the project.
    2. **Monitor Risks (Medium-Low):** Keep these on a watch list and only allocate resources when they show increased probability or impact.
    3. **No Action Necessary Risks (Low-Low):** Track, but don’t dedicate resources unless there’s a change.
* For critical risks: Discuss mitigation actions or escalations during weekly check-ins.

---

#### **4. Plan Risk Mitigation Strategies**

* **Tips for Small Projects:**

  + Consider the size of the project and resources when choosing a **mitigation strategy**. Options include:
    1. **Accept the Risk:** If the impact is low or unavoidable, build contingency into the project (e.g., extra budget or schedule buffer).
    2. **Mitigate the Risk:** Take early actions to reduce either the likelihood (e.g., additional tests) or the impact (e.g., system redundancy).
    3. **Avoid the Risk:** Change project scope or adjust plans to entirely remove the source of the risk.
    4. **Transfer the Risk:** If possible, delegate the risk management responsibility to an outside entity (e.g., contractors).
* Document the selected approach in the risk spreadsheet or a **lightweight risk plan**, embedded in your **Software Development Plan (SDP)**. For example:

  + "The project will mitigate API integration challenges by scheduling training sessions for team members and running integration tests during early development milestones."

---

#### **5. Track Risks**

* **Tips for Small Projects:**

  + Use a lightweight, centralized tool to manage risk tracking. For example:
    - Use an Excel spreadsheet stored in a shared team folder.
    - Small teams may also use simple ticketing systems (e.g., Jira, Trello) for tracking risks alongside task priorities.
* Regularly review and update the status of risks during team meetings:

  + **Is the risk still valid?**
  + **Have mitigation efforts reduced its likelihood or impact?**
  + **Does the risk require new mitigations or escalation?**

---

#### **6. Control Risks**

* **Tips for Small Projects:**

  + Ensure corrective actions in response to triggered risks are **clearly documented** and **evaluated for effectiveness.**
  + Example: If a risk involves tight integration deadlines, ensure that early integration testing is performed, results are analyzed, and lessons learned are recorded.
* Small teams should adopt **just-in-time adjustments** for changing risks to avoid disrupting day-to-day development unnecessarily.

---

#### **7. Communicate Software Risks**

* **Tips for Small Projects:**

  + Establish simple communication protocols:
    - Project leads can share key risks and status updates during weekly meetings.
    - Share risk updates with stakeholders during scheduled reviews or milestone check-ins.
  + Keep a **Summary Risk Dashboard** visible to the team via a shared folder or Kanban board.
* Ensure all risks are understood by team members, particularly **those assigned as risk owners.**

---

### **Guiding Principles for Small Projects**

1. **Start Simple:** Use basic methods (e.g., Excel spreadsheets, team brainstorming) to capture and prioritize risks. Invest in more sophisticated tools only if the need arises.
2. **Focus on High-Impact Risks:** Small projects often have limited resources, so prioritize the risks that matter the most.
3. **Empower the Team:** In small teams, everyone must take responsibility for spotting, reporting, and mitigating risks. Train the team to recognize common software risks.
4. **Leverage Past Knowledge:** Revisit risk logs from previous projects in your organization to identify recurring risks and lessons learned.
5. **Iterate and Adapt:** Review risks frequently, especially after project milestones or changes, to ensure risks are up-to-date and addressed before escalation.
6. **Integrate Risk Awareness into Processes:** Make risk discussions a standard part of team meetings, reviews, and retrospectives.

---

### **Example: Small Flight Software Project Risk**

**Scenario:** A small CubeSat software project is using an open-source flight software framework for the first time.

* **Risk:** The software team is inexperienced with the framework and faces potential delays during integration.
* **Mitigation Plan:** Schedule a two-day team workshop/tutorial on the framework and conduct an early "hello-world" integration test pre-Milestone A.
* **Tracking:** Monitor for signs of integration issues during unit testing.

By managing this risk early and iteratively, the small project ensures smooth software deployment within the constraints of limited time and resources.

---

### **Conclusion**

Small projects can adopt an efficient risk management strategy by focusing on simplicity, prioritization, and team collaboration. This streamlined approach ensures compliance with NASA protocols while optimizing resources to achieve project goals. Risk management doesn’t need to be a burden—it is a valuable tool for safeguarding small projects from setbacks and supporting mission success.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-009)

  [Agency Risk Management Procedural Requirements,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8000&s=4B "Click to open in new window")

  NPR 8000.4C, NASA Office of Safety and Mission Assurance, 2022. Effective Date: April 19, 2022 Expiration Date: April 19, 2027 See also the Risk Management Plan template.
* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-103) Software Risk Identification,  580-SP-013-03, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2014. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-104) Software Risk Monitoring and Control,  580-SP-014-03, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2014. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-122)

  [Continuous Risk Management Guidebook,](http://acqnotes.com/Attachments/Continuous%20Risk%20Management%20Guidebook.pdf "Click to open in new window")

  Alberts, C.J. , 1996.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-223)

  [IEEE Computer Society, "Systems and software engineering - Life cycle processes - Risk management,"](https://www.iso.org/standard/40723.html "Click to open in new window")

  ISO/IEC 16085, IEEE STD 16085-2006. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-346)

  [Technical Probabilistic Risk Assessment (PRA) Procedures for Safety and Mission Success for NASA Programs and Projects (Rev. w./Change 1)](http://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=5A "Click to open in new window")

  NPR 8705.5A, NASA Office of Safety and Mission Assurance, 2010. Effective Date: June 07, 2010, Expiration Date: June 07, 2022
* (SWEREF-380) Software Risk Checklist,  Flight Software Branch, Software Risk Management Plan, NASA Marshall Space Flight Center (MSFC). This is a list of generic risks organized by life cycle phase. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-500)

  [Flight Anomaly of Atmospheric Trace Molecule Spectroscopy (ATMOS) Instrument Risk Assessment](https://llis.nasa.gov/lesson/272 "Click to open in new window")

  Public Lessons Learned Entry: 272.
* (SWEREF-512)

  [Lewis Spacecraft Mission Failure Investigation Board](https://llis.nasa.gov/lesson/625 "Click to open in new window")

  Public Lessons Learned Entry: 625.
* (SWEREF-524)

  [Identification, Control, and Management of Critical Items Lists](https://llis.nasa.gov/lesson/803 "Click to open in new window")

  Public Lessons Learned Entry: 803.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database is a valuable resource for understanding how past programs and projects have handled risks and identifying best practices to apply in future endeavors. The database contains a wealth of knowledge related to risk management practices, highlighting both successful strategies and areas where project outcomes were negatively affected by unaddressed or poorly managed risks. By reviewing lessons learned, software teams can anticipate risks and develop mitigation strategies early in the project lifecycle to ensure mission success.

Below is a summary of lessons learned relevant to software risk management and their implications for implementing Requirement 5.2.1: "The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans."

---

#### **NASA Lessons Learned Related to Risk Management**

### **Lesson 1: Lewis Spacecraft Mission Failure Investigation Board – Importance of Formal Risk Management**

* **Lesson Number:** 0625
* **Summary:**  
  The "Faster, Better, Cheaper" (FBC) mission approach inherently introduced higher risks due to aggressive cost and schedule constraints. However, these risks were poorly tracked and managed, resulting in small, unmitigated risks aggregating into significant mission failures. The Lewis spacecraft experienced an unexpected combination of these risks, leading to the loss of mission.
* **Key Takeaway:**  
  All risks, no matter how small, must be formally identified, monitored, and mitigated throughout the program lifecycle, starting during the planning phase. Disciplined technical risk management practices should be integrated into program processes.
* **Guidance for Projects:**
  + Require **formal risk tracking mechanisms**, such as risk matrices or logs, to identify and prioritize small risks and prevent aggregation into major failures.
  + Conduct risk reviews during each major milestone to ensure ongoing attention to risks and their mitigations.
  + Acknowledge the challenges posed by low-resource missions (e.g., FBC), where the likelihood of risk is higher and more proactive risk management efforts are needed.

---

### **Lesson 2: Identification, Control, and Management of Critical Items – Role of Probabilistic Risk Assessment (PRA)**

* **Lesson Number:** 0803
* **Summary:**  
  Probabilistic Risk Assessments (PRAs) have proven instrumental in providing development teams with deeper insights into safety margins and critical items (e.g., single failure points). These assessments strengthen retention rationale for critical items by proving that the risk of failure can be reduced to an acceptable level. This highlights the importance of quantitative models for risk evaluation as part of critical system design and failure pathway analysis.
* **Key Takeaway:**  
  Implementing PRA methodologies can increase confidence in mission-critical systems, enabling teams to identify and assess safety margins and determine acceptable levels of risk. PRAs are particularly useful for software systems involved in single failure points or critical functions.
* **Guidance for Projects:**
  + Use PRA methods to evaluate software risks, particularly for **failure modes** that intersect with critical items or single failure points (e.g., critical communication protocols or safety-critical algorithms).
  + Leverage PRA scenarios to assess what software changes or mitigations might strengthen the rationale for retaining critical items.
  + Incorporate PRA results into risk prioritization, allowing quantitative data to guide decision-making for mitigation strategies.

---

### **Lesson 3: Flight Anomaly of Atmospheric Trace Molecule Spectroscopy (ATMOS) Instrument – Adapt Risk Assessments for Multi-Flight Experiments**

* **Lesson Number:** 0272
* **Summary:**  
  For repeated-flight experiments such as those relying on the Space Transportation System (STS), risk assessments should account for specific challenges of multi-use systems versus single-launch experiments. This lesson notes that risks associated with reusable systems require different assessment frameworks, particularly when low-cost experiments are conducted. Risks related to cumulative wear-and-tear, refurbishment, and long-term reliability must be considered for repeated use.
* **Key Takeaway:**  
  Low-cost, multi-flight experiments necessitate specialized risk assessments tailored to repeated-use systems. Risk processes should consider cumulative effects and the changing risk environment over multiple flights or iterative uses of the software.
* **Guidance for Projects:**
  + For reusable flight software systems (e.g., instruments flown across multiple missions), include the following risks:
    - **Cumulative Performance Degradation:** Monitor software behavior under repeated use to prevent performance issues due to hardware/software dependencies over time.
    - **Refurbishment Risks:** Assess risks related to software adjustments or updates between flights.
    - **Design Longevity:** Evaluate software algorithms and modules for their ability to perform consistently across multiple flights without introducing new integration risks.
  + Plan for risk mitigation strategies specific to long-term or repetitive mission cycles (e.g., regular software reviews, defect tracking between missions).

---

#### **Additional Lessons Learned to Enhance Risk Management Guidance**

### **Lesson 4: Mars Climate Orbiter (MCO) – Unit Conversion Error Caused Mission Failure**

* **Lesson Number:** Not Specified in NASA LLIS (widely known failure)
* **Summary:**  
  The Mars Climate Orbiter was lost due to a mismatch in units (imperial versus metric) between its software code and integration testing specifications. This issue was not flagged as a risk, nor was adequate testing conducted to detect it before deployment.
* **Key Takeaway:**  
  Software risks related to **requirements mismatches**, testing gaps, and communication errors can lead to catastrophic failures. Addressing integration risks, particularly when using third-party teams or shared resources, is critical.
* **Guidance for Projects:**
  + Conduct **rigorous requirements reviews** focused on identifying ambiguities, conflicts, or incomplete specifications across all stakeholders.
  + Carefully evaluate risks associated with software **interfaces** in multi-system or multi-agency environments.
  + Plan for robust **integration and acceptance testing** phases to detect and resolve unit mismatches or specification deviations early.

---

### **Lesson 5: Mars Polar Lander – Insufficient Fault Protection on Landing**

* **Lesson Number:** Not Specified in NASA LLIS (widely known failure)
* **Summary:**  
  The Mars Polar Lander failed to deploy safely due to software prematurely cutting off a descent engine, resulting from a false signal triggered by vibrations. Risk analysis failed to highlight this single-point failure or provide adequate fault protection and validation for descent algorithms.
* **Key Takeaway:**  
  Single-point software vulnerabilities must be rigorously assessed, especially for safety-critical systems. Testing must account for false signals, anomalies, and contingency handling.
* **Guidance for Projects:**
  + Highlight **failure modes** with software interactions in safety-critical moments (e.g., descent, docking, or launch systems).
  + Incorporate **redundancy checks** or fallback mechanisms into algorithm design to mitigate risks from false signals or unexpected inputs.
  + Use **simulation-based testing** environments to validate risk mitigations for edge cases and off-nominal conditions.

---

### **Lesson 6:** **Class D Means Higher Risk Tolerance—But Only if the Risks Are *Understood***

The  Lunar Trailblazer (LTB) Anomaly Review Board found LTB teams **accepted risk without truly understanding it**—especially in software‑driven areas like FP, reset behavior, SA phasing, and COTS integration. Class D allows tailoring, but it does **not** allow skipping the understanding phase.

The report stated clearly:

* “Class D projects must ensure their plans include time to look for weaknesses… to ensure that risk is understood, even if unmitigated.”
* “To assess and accept the risk, you must understand the risk.”
* Tailoring can reduce documentation, but never the requirement to **identify, analyze, and communicate software risks**.

LTB’s risk process became overwhelmed; UVFs effectively became silent risk acceptances—a red flag directly addressed in NPR 7150.2D and SWE‑086.

### **Recommendations for Applying Lessons Learned**

1. **Use Lessons Learned in Risk Identification:**

   * Refer to NASA's LLIS database during the early phases of risk identification to understand common risks observed in similar projects.
   * Develop new risk tracking entries based on applicable examples from the LLIS database and augment standard project risk checklists with these insights.
2. **Tailor Lessons Learned to Project Type:**

   * Projects that include reusable systems, tight budgets, or aggressive schedules (e.g., "Faster, Better, Cheaper") should adopt tailored risk mitigation practices focused on aggregation risks, early identification, and low-cost strategies.
3. **Leverage Probabilistic Risk Assessments (PRA):**

   * Incorporate PRA methodologies into risk analysis for critical systems to quantify safety margins and assess the acceptability of risk.
4. **Integrate Risk Awareness into End-to-End Processes:**

   * Lessons Learned emphasize that risk management extends beyond initial planning to ongoing tracking, analysis, and mitigations throughout the project lifecycle.

---

### **Conclusion**

NASA's Lessons Learned database provides invaluable knowledge for proactively managing software-related risks. By systematically studying these lessons, projects can avoid repeating mistakes, strengthen risk methodologies, and improve outcomes on future missions. Adopting formal processes, leveraging PRA, and tailoring risk frameworks for unique project environments enable project managers and software teams to mitigate risks effectively while ensuring mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* Consider innovative and "outside-the-box" approaches to risks and challenges. **Lesson Number 153**: The recommendation states: "Consider innovative and "outside-the-box" approaches to risks and challenges."
* Practice risk management with a skeptical mindset. **Lesson Number 155**: The recommendation states: "Practice risk management with a skeptical mindset rather than a success-oriented mindset."
* Document all Ground System Risks in a common Project Risk Database vs in a Standalone File. **Lesson Number 321**: The recommendation states: "Ensure that all subsystems risks are documented in a common Project database. Get agreement from Project up front to not close software/system project risks without respective subsystems’ concurrence."
* Communicate directly about bad news. **Lesson Number 327**: The recommendation states: "Communicate promptly and directly with project and line management, especially on problems."
* Carefully consider team organization structure during planning. **Lesson Number 335**: The recommendation states: "Ensure that team structure provides clear lines of responsibility and sufficient avenues for communication."

# 7. Software Assurance

**SWE-086 - Continuous Risk Management**

5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm and assess that a risk management process includes recording, analyzing, planning, tracking, controlling, and communicating all software risks and mitigation plans. 

2. Perform audits on the risk management process for the software activities.

## 7.2 Software Assurance Products

#### Software assurance (SA) plays a critical role in validating and ensuring the effectiveness of the project’s software risk management efforts. The following products and deliverables are essential outputs from software assurance activities related to risk management:

1. **Software Engineering Plans Assessment:**

   * Verification that the software risk management processes are adequately planned, established, and documented in the project's Software Development Plan (SDP) and Software Risk Management Plan (SRMP).
2. **Risk Management Process Audit Report:**

   * Results and findings from audits that evaluate the risk management process performance for software development activities.
   * Includes evidence of risks being tracked, mitigations being implemented, personnel participation, and adherence to risk protocols specified in NPR 8000.4.
   * Identifies any risks or issues stemming from audit observations (e.g., lapses in documentation or failure to address identified risks).
3. **Software Risk Documentation:**

   * Confirmation that all software risks are properly identified, tracked, and addressed in accordance with the planned risk management process.
4. **Software Status Products:**

   * **Software risks:** List of all open and mitigated software risks.
   * **Audit results:** Evidence from auditing processes, including compliance assurance, non-conformances, and corrective actions.
   * **Status charts and data:** Dashboards or reports detailing risk metrics and trends over time, including progress toward risk closure.

## 7.3 Metrics

Metrics are critical for monitoring the efficiency and effectiveness of the risk management process. Software assurance provides quantitative and qualitative insights into how risks are handled and tracked.

##### **Recommended Software Assurance Metrics for Risk Management:**

**Risk Management Metrics:**

1. **# of software work product Non-Conformances identified by life cycle phase over time**

   * Tracks defects in software products that might introduce risks during the development life cycle.
2. **# of Risks trending up/down over time:**

   * Provides a visualization of risks that are increasing or decreasing in severity and probability.
3. **# of Risks with mitigation plans vs. total # of Risks:**

   * Measures how proactive the project is in developing risk mitigations.
4. **# of Risks by severity (e.g., red, yellow, green) over time:**

   * Captures risk prioritization and highlights whether critical risks are addressed effectively.
5. **# of Risks identified in each life cycle phase (open/closed):**

   * Shows whether risks are effectively identified and resolved as the project progresses through lifecycle phases.

**Audit and Process Metrics:**  
6. **# of process Non-Conformances identified by SA vs. accepted by the project:**

* Shows the ratio of identified issues to those acknowledged and acted upon by the project team.

1. **Trends over time:**

   * **# Open vs. # Closed risks:** Indicates the effectiveness of risk resolution efforts.
   * **Counts of process, compliance, and standards audit findings:** Tracks improvements or recurring issues in software processes.
2. **# of Compliance Audits planned vs. performed:**

   * Ensures projects are following audit schedules and completing audits as planned.
3. **# of software process Non-Conformances by life cycle phase over time:**

   * Identifies process weaknesses or improvements across specific development phases.

## 7.4 Software Assurance Guidance

Software Assurance involvement in risk management processes is vital from the project’s inception through its completion. SA supports risk management through two primary tasks:

---

##### **Task 1: Confirmation of Risk Management Planning**

Software assurance personnel ensure that the project team has adequately planned for risk management. **Key SA Activities** include:

1. **Reviewing the Risk Management Plan:**

   * SA verifies that the plan contains risk strategies, mitigation criteria, processes, and tools necessary for tracking and addressing risks.
   * SA assesses whether project personnel roles are clearly assigned for active participation in risk identification, tracking, mitigation, and communication.
2. **Ensuring Effective Risk Management Processes:**  
   SA checks the following:

   * Is there a clearly documented risk management strategy?
   * Are criteria for developing and implementing mitigation plans established?
   * Has a tailored risk process (e.g., use of Center-approved libraries) been selected and documented?
   * Are tools or methods for tracking risks (e.g., spreadsheets, databases) defined and in use?
   * Are risk review meetings scheduled regularly?
   * Has a comprehensive communication path been established for escalating risks as severity increases?
3. **Validation of Role Assignments:**

   * Ensure that the project team has established roles for individuals responsible for risk management activities.
   * Confirm that software assurance personnel are participating in risk review meetings.

---

##### **Task 2: Auditing the Risk Management Process**

Software assurance regularly audits the risk management process to ensure the project complies with planned risk management activities. SA completes the following:

1. **Risk Management Process Audits:**

   * Perform audits to confirm risk identification, tracking, and mitigation activities are occurring as outlined in the Risk Management Plan.
   * Evaluate adherence to processes, tools, and regular meetings.
   * Track audit findings and ensure processes are updated accordingly.
2. **Provide Independent Observations:**

   * Beyond audits, SA provides a "second set of eyes" to identify risks that may have been missed by the project team during regular meetings, reviews, and development activities.
3. **Track SA-Submitted Risks:**

   * Risks identified independently by SA must be submitted to the project’s risk management team or risk boards for tracking.
   * If these risks are not acknowledged or addressed by the project, SA will continue monitoring these risks and escalate them as necessary.

---

##### **SA Activities to Incorporate Risk Awareness**

SA personnel must integrate risk awareness into all project activities they are involved in, such as:

* **Process/Product Audits:** Use risk identification criteria during routine audits of software processes and work products.
* **Peer Review Attendance:** Identify risks related to code structure, requirements consistency, and design logic during peer reviews.
* **Participation in Risk Review Meetings:** Contribute to discussions about current and emerging risks.

By embedding risk assessment into their regular SA duties, personnel provide ongoing value to risk mitigation efforts.

---

##### **Tracking Audit Findings**

All audit findings must be promptly communicated to the project. Software Assurance must track these findings to closure and escalate any unresolved issues or risks through SA management channels. This ensures accountability and consistent improvements in risk management processes.

### **Conclusion**

Effective software assurance ensures that proactive risk management remains a priority throughout the software development lifecycle. By confirming planning processes, auditing for compliance, providing independent oversight, tracking risks, and embedding risk awareness into all SA activities, assurance personnel create the foundation for successful risk control. Leveraging this guidance, SA enables teams to deliver robust, reliable software while reducing operational uncertainties and safeguarding mission objectives.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.24 - Software Assurance Risk](/spaces/SWEHBVD/pages/150077537/8.24+-+Software+Assurance+Risk) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is essential for demonstrating compliance with Requirement 5.2.1. Objective evidence refers to verifiable artifacts, documents, and process outputs that show the project team has effectively implemented risk management practices throughout the software development lifecycle. For Requirement 5.2.1, the following types of objective evidence can be collected:

---

### **1. Documentation of Risk Management Plans and Processes**

#### **Purpose:**

To ensure that the project establishes a formal risk management approach aligned with NPR 8000.4 and project-specific requirements.

* **Artifacts:**
  + **Software Risk Management Plan (SRMP):** A documented plan detailing the processes, tools, strategies, and team roles for managing software risks.
  + **Software Development Plan (SDP):** Sections outlining risk management integration within the software development process.
  + Tailored **Center Risk Management Processes** (if using a Center asset library).
  + Documentation of selected risk management tools or databases for recording risks.

---

### **2. Risk Identification Artifacts**

#### **Purpose:**

To capture all potential software risks, including details on how they were identified.

* **Artifacts:**
  + **Risk Registers or Logs:** Comprehensive records of identified risks with details such as conditions, consequences, likelihood, impact, and current status.
  + **Brainstorming Session Notes:** Summaries and action items from team meetings where risks were identified.
  + **Checklists or Templates:** Risk identification tools tailored for software projects (includes reused risks from similar previous projects).
  + **IV&V Documentation of Risk Surveillance Findings:** Independent assessments performed to uncover and document additional risks.
  + **Lessons Learned Documentation:** Citations of past projects and relevant identified risks.

---

### **3. Evidence of Risk Analysis Activities**

#### **Purpose:**

To ensure risks are systematically assessed and prioritized based on their probability and impact.

* **Artifacts:**
  + **Risk Categorization Matrices:** Probability-Impact matrices used to assign severity levels (e.g., high, moderate, low).
  + **Quantitative or Qualitative Risk Analyses:** Documentation of methodologies such as Probabilistic Risk Assessments (PRAs) or Fault Tree Analyses (FTAs).
  + **Failure Modes and Effects Analysis (FMEA/FMECA):** Risk analysis reports highlighting potential software-related failure modes and their criticality.
  + **Risk Prioritization Reports:** Ranked list of risks by severity and their alignment with mission or safety-critical functions.

---

### **4. Risk Mitigation and Planning Documentation**

#### **Purpose:**

To show that appropriate mitigation strategies were developed and documented for all high-priority risks.

* **Artifacts:**

  + **Risk Mitigation Plans:** Documentation outlining specific actions to address or reduce risks (e.g., reducing likelihood, mitigating impact).
  + **Risk Decision Logs:** Records of risk resolutions, including accepted, transferred, or eliminated risks.
  + **Contingency Plans:** Plans for handling "worst-case scenarios" if certain risks occur (e.g., system degradation plans).
  + **Risk Tracking Criteria:** Metrics or conditions that will trigger activation of mitigation plans.
* **Example Evidence Format for a Risk Mitigation Table:**

| **Risk ID** | **Description** | **Likelihood** | **Impact** | **Mitigation Strategy** | **Owner** | **Status** |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Timing issue with GN&C module | High | High | Add additional real-time testing | Developer A | In Progress |

---

### **5. Evidence of Continuous Risk Tracking and Monitoring**

#### **Purpose:**

To ensure risk management activities are continuously performed and updated throughout the project lifecycle.

* **Artifacts:**
  + **Risk Review Meeting Minutes/Notes:** Summaries of regular risk discussions, actions taken, and updates to risk status.
  + **Updated Risk Logs:** Logs showing changes to risk likelihood, impact, and priority as functional and technical details evolve.
  + **Risk Status Reports:** Periodic reports presented at milestones (e.g., Preliminary Design Review, Critical Design Review) detailing the current state of identified risks.
  + **Watchlists:** Separate lists of low-priority risks being monitored for escalation if conditions change.

---

### **6. Risk Communication and Reporting Evidence**

#### **Purpose:**

To demonstrate that risks and their status are effectively communicated to project stakeholders in a timely and transparent manner.

* **Artifacts:**
  + **Risk Management Dashboards:** Visual summaries of risk trends, charts, and metrics tailored for decision-makers.
  + **Risk Reports for Reviews:** Documentation shared at major project reviews (e.g., PDR, CDR, TRR) summarizing top risks, mitigation progress, and open or escalated risks.
  + **Stakeholder Communication Records:** Emails, memos, or meeting communications showing discussion and approval of risk-related actions.
  + Documentation showing external risks (e.g., contractor-provided risks) were communicated and coordinated between teams.

---

### **7. Software Assurance Contributions to Risk Management**

#### **Purpose:**

To verify that software assurance has actively participated in monitoring and auditing the risk management process.

* **Artifacts:**
  + **Software Assurance Audit Reports:** Results of audits assessing compliance with the Risk Management Plan. This includes findings and recommendations.
  + **SA Independent Risks:** Risk submissions by software assurance personnel during inspections or reviews, including evidence of tracking to closure.
  + **Participation Evidence:** Attendance logs, reports, or meeting minutes showing regular SA involvement in risk reviews, peer reviews, and meetings.
  + **Risk Process Evaluations:** Records of audits confirming Risk Management Plan adherence, including periodic assessments of the project's risk tracking and resolution activities.

---

### **8. Audit and Compliance Records**

#### **Purpose:**

To track the effectiveness of the project's compliance with established risk management guidelines.

* **Artifacts:**
  + **Non-Conformance Reports (NCRs):** Findings from process or compliance audits related to risk management, including the status of corrective actions.
  + **Issue Tracking Logs:** Logs that document open/closed findings related to risk management.
  + **Trend Analysis Reports:** Graphs showing trends in risk management compliance over time (e.g., increasing or decreasing audit non-conformances).

---

### **9. Risk Metrics and Analysis Reports**

#### **Purpose:**

To provide quantitative evidence of the effectiveness of the risk management process.

* **Artifacts:**
  + **Risk Metrics Dashboards:** Quantitative summaries of key metrics, including:
    - Number of risks identified, resolved, and closed.
    - Number of risks with mitigation strategies.
    - Trends of risk severity levels (red, yellow, green) over time.
  + **Software Risk Phase Metrics:** Details showing when risks were identified, mitigated, or resolved across project phases.

---

### **10. Final Risk Closure Documentation**

#### **Purpose:**

To confirm that all risks were addressed and formally closed by the end of the software lifecycle.

* **Artifacts:**
  + **Final Risk Status Reports:** Delivered during the project closeout phase, confirming that no open risks were left unresolved.
  + **Risk Closure Logs:** Records establishing the rationale for closing each risk, ensuring all mitigations were completed.
  + **Lessons Learned Reports:** Documentation capturing how risks were managed, along with best practices and future recommendations.

---

### **Conclusion**

The objective evidence outlined above ensures transparency, traceability, and accountability in the risk management process and demonstrates compliance with Requirement 5.2.1. By maintaining thorough records, the project ensures its software risks are effectively identified, managed, and mitigated, supporting project success while satisfying NASA’s rigorous risk management requirements. Collecting this evidence provides confidence to all stakeholders that software risks are addressed proactively, reducing the likelihood of costly or mission-critical failures.

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
