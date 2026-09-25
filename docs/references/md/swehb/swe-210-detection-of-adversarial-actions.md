# SWE-210 - Detection of Adversarial Actions

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695330. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions

SWE-210 - Detection of Adversarial Actions

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695330)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695330&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

3.11.8 The project manager shall identify software requirements for the collection, reporting, and storage of data relating to the detection of adversarial actions.

## 1.1 Notes

Monitoring of key software observables (e.g., number of failed login attempts, performance changes, internal communication changes) is needed to detect adversarial actions that threaten mission success. When an adversarial action occurs, it should be reported. Raw event data should be further analyzed to determine whether an anomalous event represents an attack and if so, the nature of the attack.

## 1.2 History

Click here to view the history of this requirement: SWE-210 History

SWE-210 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B | RESERVED |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE |
| D | 3.11.8 The project manager shall identify software requirements for the collection, reporting, and storage of data relating to the detection of adversarial actions. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 2. Rationale

To provide the capability to monitor key software observables (e.g. number of failed login attempts, performance changes, internal communication changes) to detect adversarial actions that threaten mission success.

This requirement emphasizes the need for **proactive detection**, **documentation**, and **response capabilities** to adversarial actions within a software system. Adversarial actions refer to intentional or malicious activities targeting a system’s integrity, availability, or confidentiality — including but not limited to cyberattacks, unauthorized access, data breaches, system tampering, or sabotage.

By addressing this requirement, the project ensures that capabilities for detecting, analyzing, and mitigating adversarial actions are embedded in the software design and implementation stages. The collection, reporting, and storage of relevant data allow teams to identify threats, prevent further compromise, and support forensics and incident response processes.

---

### **Key Rationale**

#### **1. Cybersecurity Risk Mitigation**

Modern software systems face constant **cybersecurity threats**. Malicious actors can exploit vulnerabilities to disrupt operations, steal sensitive data, or even compromise mission-critical systems. By identifying requirements for **detecting adversarial actions**, the project manager ensures that the software is designed to actively:

* **Log suspicious events** for investigation and mitigation.
* **Identify intrusions or anomalies** (e.g., unauthorized access attempts, exploitation of vulnerabilities).
* **Alert stakeholders** when such events occur in real-time for immediate response.

This proactive approach minimizes risks to the system and its mission objectives and helps meet organizational needs for operational security.

---

#### **2. Compliance with Organizational and Regulatory Standards**

Many regulatory and organizational frameworks require projects to build explicit capabilities for **security monitoring, reporting, and response** into software systems. Examples include:

* **NASA-STD-1006**: Cybersecurity framework for information systems.
* **NIST SP 800-53**: Security and Privacy Controls, which includes logging, monitoring, and intrusion detection mechanisms.
* **FISMA (Federal Information Security Management Act)**: Requires federal information systems to maintain capabilities for incident detection and audit trails.
* **ISO 27001**: Information Security Management System standard, which emphasizes monitoring and response systems for security-related incidents.

By addressing Requirement 3.11.8, the project aligns its software requirements with such frameworks and standards, ensuring **compliance with cybersecurity regulations** central to NASA and federal missions.

---

#### **3. Support for Incident Investigation and Forensics**

* Software requirements for the **storage of detection data** ensure that adversarial actions are not just identified but also recorded for:
  + **Incident investigation** by cybersecurity teams.
  + **Root cause analysis**, enabling teams to understand how and why malicious activity occurred.
  + **Forensics** to determine potential attackers, identify exploited vulnerabilities, and take legal action or preventive measures.

Stored data provides a historical archive that is critical for addressing potential future vulnerabilities and improving the software's defense mechanisms.

---

#### **4. Real-Time Response and Decision Support**

* Without proper mechanisms for **reporting adversarial actions**, malicious activities can go unnoticed or unresolved until significant damage is done. Real-time detection and reporting ensure:
  + **Fast escalation** of suspicious events to stakeholders.
  + **Response orchestration** via automated actions (e.g., locking compromised user accounts, isolating impacted systems, notifying administrators).
  + **Operational continuity** by containing threats quickly before they disrupt critical software functions.

Embedding these capabilities in the software requirements ensures **timely response**, protecting mission-critical activities from operational disruptions.

---

#### **5. Data Integrity and Mission Assurance**

Adversarial actions pose significant risks to the **integrity of data**, systems, and processes in software systems central to NASA's mission objectives. These risks can include:

* **Compromised scientific data** that may affect experiments or mission outcomes.
* **Loss of sensitive information** crucial to mission operations.
* **Targeting critical systems** that control hardware (e.g., spacecraft, robotics, ground systems).

Including requirements for detecting adversarial actions ensures that the software design incorporates defense measures, reducing chances of mission failure due to malicious interference.

---

#### **6. Accountability and Auditability**

* By collecting and storing detection data, organizations maintain **audit trails** to demonstrate accountability for monitoring security events. This is crucial for:
  + **Compliance audits** where detailed records may be required to prove adherence to security practices.
  + **Stakeholder assurance**, ensuring customers, leadership, or regulators that the software is properly designed to handle security threats.

---

#### **7. Scalability for Future Threats**

As technology evolves, threats will become increasingly sophisticated, with adversaries exploiting emerging technologies such as artificial intelligence and quantum computing. By defining requirements for **data collection, reporting, and storage**, projects can:

* Build scalable systems capable of adapting to new or advanced detection mechanisms.
* Future-proof their designs by ensuring rich datasets to train anomaly detection systems or machine learning models used in cybersecurity.

---

#### **8. Alignment with NASA’s Mission Safety Goals**

NASA systems and programs, such as spacecraft operations, ground control systems, and scientific software, often operate in highly sensitive environments. Adversarial actions—whether cyberattacks or insider threats—can directly jeopardize mission safety and success. Addressing Requirement 3.11.8 actively supports:

* **Safety-critical requirements** surrounding the integrity of mission systems.
* **Mitigation of sabotage risks** or intentional interference with mission-critical software.

---

### **Implementation Steps**

To satisfy Requirement 3.11.8, the following actions should be taken:

1. **Define Requirements for Data Collection**:

   * Identify what data needs to be collected to detect adversarial actions (e.g., user activity logs, failed login attempts, system error logs).
   * Specify the tools or mechanisms for collecting relevant data (e.g., endpoint monitoring, intrusion detection systems).
2. **Establish Reporting Framework**:

   * Define how detected malicious actions will be reported (e.g., real-time alerts, email notifications, centralized dashboards).
   * Address escalation processes for high-severity events.
3. **Define Data Storage Requirements**:

   * Specify formats and systems for storing detection data securely.
   * Consider data retention periods aligned with compliance standards and operational needs.
4. **Perform Risk-Based Analysis**:

   * Prioritize adversarial events based on their potential impact on mission-critical software.
   * Ensure that detection mechanisms are focused where risks are highest.
5. **Integrate Detection into Software Architecture**:

   * Embed detection logic (e.g., anomaly detection algorithms, threat signature checks) directly into the software design and architecture.
6. **Leverage Advanced Detection Technologies**:

   * Incorporate advanced techniques such as machine learning, anomaly detection, and big data analysis to improve detection accuracy.
7. **Audit and Validate**:

   * Test detection mechanisms in simulated attack scenarios.
   * Validate reporting and data collection accuracy.

---

### **Summary**

Requirement 3.11.8 ensures the proactive identification and documentation of adversarial actions during software operation. By emphasizing detection, reporting, and storage, projects can mitigate risks to mission safety and ensure compliance with cybersecurity frameworks while providing accountability through detailed records. Addressing this requirement strengthens software resilience against deliberate threats, protects operational continuity, and supports effective incident response and forensics, safeguarding the integrity of NASA’s systems and missions.

# 3. Guidance

# **Introduction**

Detecting adversarial actions and safeguarding mission-critical systems is a continuous challenge as cybersecurity threats evolve. This guidance addresses software engineering considerations for **collection**, **reporting**, and **storage** of data related to the detection of adversarial actions. These principles ensure the systematic capture, notification, and preservation of evidence for cyber incidents, supporting proactive risk mitigation and robust system resilience.

Though adversarial detection shares similarities with mission health and safety monitoring, it diverges in data interpretation, where security contexts drive responses. Furthermore, the **risk posture** of the system shapes how detection mechanisms are scoped and implemented. This guidance is intended to be tailored to the specific system being developed and reviewed/approved by appropriate authorities during the software lifecycle.

This guidance also aligns closely with:

* **SWE-154**: Identify Security Risks
* **SWE-157**: Protect Against Unauthorized Access
* **Topic 8.04**: Additional Requirements Considerations for Safety-Critical Software

---

### **1. Collection Guidance**

#### **Definition**

Collection refers to the systematic gathering of data related to a system's behavior, including hardware, software, interactions with external components, and network activity. Logging mechanisms must be carefully designed to ensure comprehensive coverage while maintaining accuracy and efficiency.

Malicious actors often target logs as part of their attack strategy to conceal evidence, manipulate system records, or obscure their actions. Therefore, robust collection mechanisms must be in place **before deployment**, ensuring key data is preserved even under adversarial conditions.

#### **Improved Guidance**

**1.1 Logging Design Considerations:**

* Log data should be collected **continuously** and automatically across all systems, both onboard flight systems and ground systems.
* **Capture key data types**:
  + System access attempts (successful and failed logins).
  + Configuration changes, especially critical ones.
  + System resource utilization (CPU, memory, storage).
  + Software integrity checks (e.g., hash comparisons, file verifications).
  + Attempts to execute unauthorized commands or access restricted resources.
* **Enable detailed logging**:
  + Timing (precise timestamps for chronological order).
  + Metadata (paths, log sources, file attributes, context).
  + Inputs/outputs of system processes to enable retrospective analysis.

**1.2 Address Adversarial Threats with Redundant Systems:**

* Use **independent logging sources** for comparison and integrity verification when the system is suspected to be compromised.
* Implement agents external to the monitored system for **automatic log collection** to ensure logs are preserved during system failures or adversarial actions.

**1.3 Plan Collection Methods Prior to Deployment:**

* Pre-define collection methods during architecture design, including:
  + Persistent and volatile data capture (ensure temporary data or runtime states can be logged when abnormal conditions occur).
  + Recording external system interactions and abnormal behaviors (e.g., unauthorized access attempts from external networks).

**1.4 Examples of Data to Collect:**  
To assist developers, here are expanded logging examples:

* **Boundary Violations**:
  + Logs of actions exceeding authorized boundaries (e.g., accessing restricted files).
  + Logs of abnormal recurring behaviors violating system patterns.
* **Integrity Violations**:
  + Changes to verified recovery states.
  + Failed system integrity checks (e.g., altered or missing files).
* **Self-Tests**:
  + Reports from Built-In Self-Tests (BITS), showing basic functionality.
* **Accepted/Rejected Actions**:
  + Counts and metadata for accepted and rejected actions.
  + Communication attempts (internal subsystem communications, external networks).
* **Anomalous Resource Usage**:
  + Failure patterns related to hardware utility (e.g., excessive CPU or disk usage during breaches or Denial of Service attacks).

---

### **2. Reporting Guidance**

#### **Definition**

Reporting refers to the systematic notification of potential issues relating to adversarial actions. This includes informing operators, administrators, or automated systems of anomalies or suspicious activity. Effective reporting ensures timely intervention, reducing the risk of prolonged compromise or delayed response.

Over-notification through false positives can desensitize users, while infrequent reporting risks missing critical events. Therefore, reporting systems must offer **customizable reporting thresholds** and prioritization mechanisms based on severity and urgency.

#### **Improved Guidance**

**2.1 Design Reporting Systems for Effective Interpretation:**

* Reports must:
  + Be clear and actionable for their intended audience.
  + Include **severity levels** (e.g., Critical, Severe, Medium, Low) that guide operator urgency.
  + Include **metadata** for context (e.g., timestamps, origin, affected components).
  + Highlight discrepancies identified during log analysis, such as mismatched logs from compromised sources.

**2.2 Reporting Frequency and Accuracy:**

* Avoid generating excessive notifications or false positives that may desensitize operational teams.
* Use **adaptive thresholds** to customize the frequency and criteria for reporting based on system behavior.
* Implement **interactive feedback mechanisms** (e.g., acknowledgment systems) where operators can review and silence items as appropriate.

**2.3 Reporting Requirements:**  
When designing reporting systems, the following must be considered:

* Detect and alert on:
  + **Urgent security compromises** (e.g., malware detection, unauthorized configuration changes).
  + **Boundary violations or anomalous patterns** (e.g., repeated failed access attempts from untrusted origins).
* Create **automated notifications** that escalate critical compromises to trusted recipients.
* Ensure regular review of logs by human operators for anomalies missed by software.

---

### **3. Storage Guidance**

#### **Definition**

Storage refers to preserving detection data for retrieval, analysis, and forensic investigation after events occur. Ensuring data integrity and availability is critical, as adversarial actors often attempt to manipulate or delete logs to cover their tracks.

The storage system must be designed with redundancy and security in mind to ensure that key information remains accessible and protected during or after a system compromise.

#### **Improved Guidance**

**3.1 Redundant and Secure Storage Locations:**

* Store logs in **secure, independent systems** to reduce the risks posed by:
  + Single points of failure (e.g., compromised primary storage).
  + Common-cause failures (e.g., simultaneous hardware loss).
* **Offload logs periodically** to external systems to mitigate risks of denial-of-service (DoS) attacks on local storage.

**3.2 Retain Logs per NASA Records Retention Requirements:**

* Follow NASA's mandatory data retention policies to ensure historical data is stored for required durations (e.g., for regulatory compliance or legal reasons).
* Ensure sufficient space allocation for logs to prevent Denial-of-Service risks caused by exceeding log capacity.

**3.3 Verified Recovery States:**

* Store known, verified recovery states that allow forensic teams to restore compromised systems securely.
* Avoid storing **unverified recovery states**, which risk reintroducing vulnerabilities.

**3.4 Preservation of Metadata:**

* Ensure storage systems include:
  + Paths, timestamps, version history, authors, and context associated with stored logs.
  + Fault/failure conditions detected during execution.

**3.5 Protect Stored Data:**

* Secure log storage systems against adversarial intrusion using:
  + Encryption for logs at rest.
  + Measures to detect tampering or unauthorized access to log files.
  + Checkpointing mechanisms to periodically validate log integrity.

---

### **Final Recommendations**

1. **Review Security Context**: Tailor detection mechanisms to the system’s risk posture, ensuring scalable solutions that meet both current and future mission needs.
2. **Use Automation and Redundancy**: Automate logging, reporting, and storage processes while incorporating redundancy and fail-safe measures.
3. **Integrate Cyber Threat Intelligence**: Enhance detection and storage systems with proactive capabilities, such as leveraging threat intelligence datasets to detect adversarial patterns.
4. **Regular Validation**: Frequently validate the logging/collection system, reporting features, and storage solutions to ensure robustness against evolving threats.

---

### **Conclusion**

This updated guidance introduces improved software engineering practices for detecting adversarial actions while bolstering mission safety and cybersecurity. By emphasizing **collection**, **reporting**, and **storage** methodologies, it supports both proactive and reactive security measures, ensuring resilience against cyber incidents and alignment with NASA's mission-critical needs.

See also [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks), [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access),

Topic  [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software).

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

Small projects typically operate with limited resources (budget, time, and personnel), but they are still exposed to cybersecurity risks. Below is simplified and tailored guidance to help small projects effectively incorporate the detection of adversarial actions without creating excessive overhead. This guidance focuses on addressing the requirement in a practical, lightweight, scalable, and cost-effective manner.

---

### **Guiding Principles for Small Projects**

1. **Focus on Essential Adversarial Detection**:

   * Prioritize detection mechanisms that cover high-impact risks for the project, rather than deploying exhaustive processes.
   * Ensure that the solution is designed to scale and can meet minimum security standards without requiring large manual efforts.
2. **Leverage Existing Tools**:

   * Use **off-the-shelf tools** or open-source solutions for logging, reporting, and storage (e.g., ELK Stack, Graylog, Splunk Free, Syslog-ng).
   * Prefer tools with built-in security features rather than developing custom solutions.
3. **Minimize Complexity**:

   * Streamline collection, reporting, and storage processes by focusing on critical logs only.
   * Avoid overloading the system with excessive data collection or complex workflows that are hard to maintain.
4. **Automate Where Possible**:

   * Use automated logging and reporting features to reduce manual intervention.
   * Configure alerts for **high-severity events only** to avoid overwhelming operators with insignificant data.
5. **Leverage Cloud-Based Solutions**:

   * For small projects, using a **secure cloud logging service** could reduce infrastructure overhead (e.g., AWS CloudWatch, Azure Monitor, Google Workspace security tools).

---

### **Simplified Approach for Small Projects**

#### **1. Collection Guidance**

Collection is vital for detecting adversarial actions, but in small projects, a simplified approach can focus on logging only **critical activities** aligned to cybersecurity risks.

**Implementation Steps**:

* **Identify What to Collect**:

  + Start by identifying the **top-priority incidents** to monitor based on the project’s risk profile. Examples:
    - Failed login attempts with timestamps.
    - Unauthorized access to sensitive files or subsystems.
    - Changes to system configurations (additions, deletions, or modifications).
    - Actions exceeding pre-defined boundaries (e.g., privileged command execution).
  + Exclude unnecessary data to avoid overload and facilitate efficient forensic review.
* **Use Minimal Logging Mechanisms**:

  + Leverage lightweight logging tools or system-native logging features, such as:
    - **Syslog**: Works on most operating systems, simple to configure.
    - **Event Viewer** (Windows): Built-in logging for small systems.
    - Application logs.
  + For embedded small systems, consider buffering logs in memory or writing to a small persistent local file.
* **Plan Logging at the Start**:

  + Define the logging structure (e.g., timestamps, unique identifiers, event descriptions) early in the project.
  + Logging settings should be pre-configured during system initialization to capture essential event data.

**Small Project Collection Tools**:

* Open-source or low-cost tools: **Logstash**, **Fluentd**, **Syslog Server**, **Circular Logging** (especially for embedded systems).

---

#### **2. Reporting Guidance**

For small projects, reporting mechanisms should be lightweight, actionable, and focused on critical issues. Overcomplicating notification features can overwhelm users and waste resources.

**Implementation Steps**:

* **Identify Key Reporting Needs**:

  + Prioritize high-impact events for automated reporting. Examples:
    - Notify operators about repeated failed login attempts within a short timeframe (potential brute-force attack).
    - Generate alerts for unauthorized attempts to access restricted resources.
  + Avoid notifications for routine/low-severity events unless requested by users.
* **Use Simplified Reporting Frameworks**:

  + Reports should provide clear, concise summaries like:
    - Timestamp and description of the event.
    - Severity and urgency rating (e.g., Critical, Warning).
    - Suggested actions for mitigation (if applicable).
  + Provide a mechanism for acknowledging notifications to minimize redundant alerts.
* **Automated Reporting**:

  + Automate notifications using:
    - Email alerts (e.g., triggered by log monitoring tools for critical events).
    - Lightweight dashboards (custom or pre-built by tools like Splunk Free, ELK Stack).
* **Review Logs Periodically**:

  + Regularly audit logs to address risks missed by automated alerts. Use manual reviews for anomalies.

**Small Project Reporting Tools**:

* Email-based reporting tools (e.g., **Postfix**, **Google Workspace**).
* Low-cost monitoring platforms (e.g., **UptimeRobot**, **PagerDuty Free**).

---

#### **3. Storage Guidance**

Storing logs securely enables the project team to monitor past events and provides data for forensic investigations. Small projects should avoid over-engineering storage systems and instead focus on **basic log retention practices**.

**Implementation Steps**:

* **Store Logs Securely**:

  + Use a separate, secure storage medium (e.g., external storage or a secure cloud service) to maintain logs independent of the primary system to mitigate compromise risks.
  + Ensure redundancy, such as using **backups** or decentralized storage systems (two locations minimum).
* **Define Retention Policies Early**:

  + Follow NASA's record retention policy even if scaled down. For example:
    - Critical security event logs (e.g., unauthorized access or failed logins) retained for 6–12 months depending on the system's needs.
    - Routine logs (e.g., resource utilization) retained for shorter periods.
  + Avoid indefinitely storing redundant or routine logs.
* **Ensure Space Availability**:

  + Calculate expected log generation rates and allocate enough space upfront to avoid Denial-of-Service vulnerabilities (log storage exhaustion).
* **Protect against Tampering**:

  + Encrypt stored logs to ensure integrity and confidentiality.
  + Use checksums to validate logs periodically for tampering evidence.

**Small Project Storage Tools**:

* External storage: Secure USB drives or standalone storage systems.
* Cloud storage: Use scalable services like **AWS S3**, **Azure Storage**, or **Google Cloud Storage**.

---

### **Integration Tips for Small Projects**

1. **Use Pre-Built Frameworks Where Possible**:

   * Install and configure log monitoring tools with pre-built templates suited for small-scale systems (e.g., ELK Stack or Splunk Free).
2. **Simplify Implementation**:

   * Start with logging and reporting for the **most critical subsystems**, then expand coverage if resources allow.
3. **Establish Roles for Log Monitoring**:

   * Assign personnel (even if a small team) to periodically audit logs and manage alerts.
4. **Automate and Scale**:

   * Automation (e.g., log collection and reporting pipelines) reduces reliance on manual efforts while improving scalability and reliability.
5. **Tailor Reporting to Minimize Noise**:

   * Use thresholds to minimize unnecessary warnings and focus reporting mechanisms on **high-severity issues**.

---

### **Example Workflow for a Small Project**

1. **Setup Logging Infrastructure**:

   * Install a lightweight logging tool (e.g., Syslog or ELK Stack).
   * Configure logging for critical activity, including failed logins, configuration changes, and unauthorized resource usage.
2. **Configure Reporting Alerts**:

   * Set up email-based automatic notifications for system anomalies like repeated failed logins or detected boundary violations.
3. **Securely Store Logs**:

   * Periodically archive logs in a secure cloud location (e.g., AWS S3 with encryption enabled) and back them up locally.
4. **Monitor, Audit, and Respond Periodically**:

   * Review logs weekly, focusing on discrepancies between expected and actual activity.
   * Respond to anomalies using procedures defined in a lightweight incident response plan.

---

### **Recommended Tools for Small Project Implementation**

* **Logging**: Syslog, Fluentd, ELK Stack, Logstash.
* **Reporting/Monitoring**: UptimeRobot (free), PagerDuty (free), Email alerts.
* **Storage**: AWS S3 Free Tier, Azure Free Tier, local encrypted backups.

---

### **Conclusion**

Small projects can implement Requirement 3.11.8 effectively by focusing on essential capabilities for detecting adversarial actions without overburdening the team or introducing unnecessary complexity. By concentrating on **critical logs**, providing **high-severity reporting**, and **scaling storage securely**, small projects can meet NASA requirements and ensure safe and secure operations. This focused yet scalable approach provides strong defenses against adversarial actions while respecting project constraints.

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

### 5.3 Process Asset Templates

**SWE-210 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-056 - )

  [PAT-056 - Software Development Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770884/PAT-056%20-%20Software%20Development%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Development - Management Plan. Based on the minimum recommended content for a Software Development - Management Plan.

# 6. Lessons Learned

Over the years, NASA has documented numerous **lessons learned** from its projects and missions that highlight both successes and challenges in managing cybersecurity risks associated with adversarial actions. These lessons help inform best practices for implementing this requirement and ensuring the robustness of the system against malicious activities.

---

### **Key NASA Lessons Learned**

#### **1. Criticality of Logging for Incident Detection**

* **Lesson Learned**: Inadequate or incomplete logging has led to difficulties in detecting and analyzing cyber incidents. Failure to log critical system events can leave security vulnerabilities undetected until they are exploited.
* **Example**:
  + **Incident**: A lack of detailed logging in a ground support system limited the ability to diagnose a series of unauthorized access attempts. The failure to log configurations and login attempts delayed incident response and root cause analysis.
  + **Takeaway**:
    - Ensure that logging is **comprehensive** (e.g., records configuration changes, failed/successful login attempts, critical resource usage).
    - Logs need to include sufficient metadata (timestamps, user/actor IDs, source details) to facilitate forensic analysis.

---

#### **2. Failure to Prepare Logging Infrastructure Before Deployment**

* **Lesson Learned**: If data collection methods are not fully enabled prior to deployment, critical data around a cyber incident may be missing, making it impossible to analyze or recover from the intrusion.
* **Example**:
  + **Incident**: In a mission-control application, logging for failed authentication attempts was not pre-configured. During an investigation of suspicious access, the lack of historical data about login behavior prevented uncovering the adversary’s entry point.
  + **Takeaway**:
    - **Enable logging mechanisms during the design and development stages**, with logging infrastructure fully operational before deployment.
    - Test and validate logging to ensure the critical data streams are being collected as intended.

---

#### **3. Adversaries Target Logs to Cover Their Tracks**

* **Lesson Learned**: Adversaries often attempt to alter or delete logs after compromising systems, which can impede investigators’ ability to trace malicious actions.
* **Example**:
  + **Incident**: In an engineering support system, adversaries erased logs immediately after accessing a privileged configuration interface. This erased evidence of their actions, leaving the system administrators with no ability to track the exploit path.
  + **Takeaway**:
    - Store logs in **independent and secure systems** that cannot be altered or erased by a compromised subsystem.
    - Consider implementing append-only logs (e.g., WORM – Write Once Read Many) or cryptographic mechanisms (e.g., hash chains) to protect log integrity.
    - Maintain redundancy by saving logs in multiple locations to reduce the impact of tampering or hardware failures.

---

#### **4. Not Using Independent Monitoring Systems**

* **Lesson Learned**: Relying solely on a system’s internal logs without independent verification or monitoring increases the risk of undetected adversarial actions, especially if the system is compromised.
* **Example**:
  + **Incident**: A misconfigured ground station subsystem prevented sensitive data from being logged. Since no independent monitoring was deployed, significant system activity remained untracked during a suspected breach.
  + **Takeaway**:
    - Ensure independent tools or third-party monitoring agents are in place to capture logs and provide redundancy in case the monitored system becomes compromised.
    - Compare logs from the primary system with data from independent monitoring for discrepancies and tamper detection.

---

#### **5. Alerts and Reports Must Be Actionable**

* **Lesson Learned**: Overwhelming operators with excessive or low-relevance alerts often leads to "alert fatigue," causing critical notifications to be overlooked. Conversely, poor reporting delays operators’ ability to detect and respond to security incidents.
* **Example**:
  + **Incident**: During a simulated attack, an intrusion detection system generated hundreds of low-priority alerts tied to routine activity, causing cybersecurity teams to miss a critical alert about file tampering.
  + **Takeaway**:
    - Design the reporting system with **thresholds based on event severity and urgency**. Critical events (e.g., malware detection) must generate immediate alerts, while routine events can be aggregated into summary reports.
    - Incorporate feedback mechanisms, allowing operators to fine-tune alert thresholds and reporting preferences over time.

---

#### **6. Reporting Discrepancies Between Logs Improves Detection**

* **Lesson Learned**: Discrepancies between multiple log sources can indicate tampering or adversarial actions. Consistently reviewing and reconciling logs from different components has proven to be an effective strategy for detecting compromises.
* **Example**:
  + **Incident**: A spacecraft monitoring system identified discrepancies between telemetry logs stored on-board and those transmitted to ground control. Analysis revealed an adversary was attempting to use false transmission data to mask unauthorized commands.
  + **Takeaway**:
    - Encourage manual or automated reviews to flag mismatches between logs generated by different system components.
    - Automate integrity checks (e.g., comparing log hashes) between primary and backup logs or between multiple systems.

---

#### **7. Data Overload Without Storage Controls**

* **Lesson Learned**: Systems that do not allocate sufficient storage for logs are prone to overwriting critical historical data or failing to log new events. In addition, excessive logging can overload the system, leading to performance degradation.
* **Example**:
  + **Incident**: A misconfigured logging system on a ground-based spacecraft interface began recording every ping response, rapidly filling the storage allocated for mission-critical logs. The resulting overflow led to logging failures during an actual fault event.
  + **Takeaway**:
    - Plan storage capacity based on expected log sizes and allocate sufficient space for logging, with mechanisms in place to automatically archive older data.
    - Set logging rules to avoid collecting redundant or unnecessary data that wastes storage space or overwhelms resources.

---

#### **8. Lack of Training on Log Usage and Forensics**

* **Lesson Learned**: Logs were collected correctly, but personnel lacked training on how to use them effectively for cybersecurity analysis or incident investigation.
* **Example**:
  + **Incident**: After a failed mission interface test, the debugging and forensics team were unable to identify key logs that could provide insights into the failure. This highlighted a skill gap in leveraging collected data for diagnostics.
  + **Takeaway**:
    - **Train operators and engineers** on interpreting logs, recognizing suspicious patterns, and distinguishing between normal and anomalous events.
    - Incorporate log analysis exercises into cybersecurity drills or simulated incidents.

---

#### **9. Delayed Incident Response Due to Sparse Logging**

* **Lesson Learned**: Sparse or incomplete logging delayed the response to adversarial actions, as investigators lacked the breadth of data needed for timely root cause analysis.
* **Example**:
  + **Incident**: During an attempted data exfiltration from a ground-based NASA facility, sparse logging provided little detail about the adversary’s attack methodology or affected resources.
  + **Takeaway**:
    - **Identify critical events early in the design phase** and ensure appropriate logging policies are in place.
    - Include detailed logging of specific areas such as:
      * Privileged user actions.
      * Unauthorized data access.
      * Security system overrides.

---

### **Conclusion: Lessons Learned Summary**

From the above lessons, several key practices emerge for satisfying Requirement 3.11.8 within NASA systems:

1. **Proactive Planning**: Logging, reporting, and storage mechanisms must be designed, enabled, and validated before deployment to ensure data availability during incidents.
2. **Independent Validation**: Use redundant and secure logging sources to detect tampering and provide integrity checks.
3. **Actionable Reporting**: Design reporting systems to prioritize severe events and reduce operator overload.
4. **Training**: Ensure teams are trained to interpret logs effectively and integrate forensic-ready features into the logging system.
5. **Storage and Capacity**: Plan sufficient storage to prevent log overflows or gaps and protect stored data from tampering.

These lessons provide critical guidance for designing systems capable of detecting adversarial actions while ensuring resilience, mission safety, and compliance with NASA’s security objectives.

# 7. Software Assurance

**SWE-210 - Detection of Adversarial Actions**

3.11.8 The project manager shall identify software requirements for the collection, reporting, and storage of data relating to the detection of adversarial actions.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the software requirements exist for collecting, reporting, and storing data relating to the detection of adversarial actions.

## 7.2 Software Assurance Products.

**Objective**: Ensure that Software Assurance (SA) adequately evaluates, tracks, and verifies the inclusion of requirements for the detection, reporting, and storage of adversarial actions throughout the software lifecycle. This section covers the artifacts and deliverables that demonstrate SA's role in assuring compliance with Requirement 3.11.8.

---

##### **Guidance**

1. **Analysis of Software Volatility Measures**:

   * **Purpose**: To track changes in software requirements or implementation over time that may impact the detection of adversarial actions.
   * **Actions**:

     + Regularly assess software **volatility metrics**, which measure how frequently requirements, code, or features related to detecting adversarial actions are changed, added, or removed. Excessive volatility may introduce risks such as incomplete implementation or reduced consistency in adversarial detection capabilities.
     + Evaluate the root cause of high volatility in related requirements. For instance:
       - Is the system operating in a dynamic threat environment leading to frequent security updates?
       - Is there poor initial requirements specification leading to frequent changes?
     + Focus on stability of key areas such as:
       - Logging mechanisms.
       - Alert/reporting mechanisms.
       - Storage and integrity assurance.
   * **Product**: SA will create a report summarizing:

     + Volatility trends over time for security-related requirements, and their potential risks (e.g., undefined functionality, delayed implementation).
     + Recommendations to stabilize requirements and improve adherence to the security controls.
2. **Confirmation Artifacts (Part of Task 1 Completion)**:

   * **Task 1 Objective**: Confirm that requirements relating to detection of adversarial actions have been correctly identified, specified, and assessed for feasibility by the software team.
   * **Deliverable**: Evidence confirming the completion of requirement analysis tasks, including:

     + **Requirements Traceability Matrix (RTM)** linking adversarial action detection requirements to corresponding system functions and tests.
     + Identification of any gaps, risks, or issues during the specification stage and corrective actions to address them (e.g., missing or vague requirements, under-specified data logging needs).
     + Detailed notes from SA's participation in software requirements reviews, highlighting security-specific concerns raised and documented responses from relevant teams (e.g., design adjustments, clarification of requirements implementation plans).
   * **Purpose**: Demonstrate SA's thorough review of requirements related to adversarial action detection, ensuring alignment with mission objectives and risk tolerances.

## 7.3 Metrics

**Objective**: Define measurable indicators for assessing the implementation of requirements related to adversarial action detection. These metrics allow SA to track progress, identify deficiencies, and support data-driven decision-making for improved software security.

---

##### **Improved Metrics Guidance**:

1. **Coverage Metrics**:

   * Define the following coverage metric to assess the completeness of adversarial action requirements implementation:
     + **“# of requirements specified for detecting adversarial actions vs. # of requirements implemented.”**  
       **Actions**:
     + Track how many requirements were initially defined and ensure that they have been implemented in the software. Ensure traceability in the RTM so SA can validate coverage.
     + Record any requirements that were **only partially implemented or omitted**, as this may result in functional gaps.
2. **Verification Metrics**:

   * Add a metric to track the effectiveness of testing requirements related to adversarial actions:
     + **“# of verification tests passed for requirements related to adversarial actions vs. total number of such requirements.”**  
       **Actions**:
     + Ensure that for every security-related requirement, corresponding test cases are developed and executed during verification. Track how many of those tests pass or fail and categorize failures by severity.
3. **Volatility Metrics (Aligning with SA Products)**:

   * Assess the stability of adversarial detection requirements over time:
     + **"Number of changes to adversarial action detection requirements over defined time intervals (e.g., monthly)."**  
       **Purpose**: High volatility could indicate risks, such as unclear requirements, poorly understood system needs, or rapidly evolving cybersecurity threats.
4. **Incident Tracking Metrics**:

   * Track post-deployment adversarial activity to measure system effectiveness:
     + **"Number of adversarial actions detected by the system vs. number of adversarial actions missed or reported after the fact."**
     + **"Number of false positive alerts generated vs. total alerts."**  
       **Purpose**: Provide insights into the performance of implemented security mechanisms, identify weakness in logged data or response actions, and inform future requirements.

**Reference Metric for Additional Detail**: See **Topic 8.18 – SA Suggested Metrics**, which provides generalized metrics that can be refined and tailored to adversarial detection.

---

## 7.4 Guidance

##### **Confirming the Inclusion of Adversarial Detection Requirements**

**Objective**: Verify that requirements for detecting adversarial actions are properly specified as part of the requirements assessment process. Ensure that these requirements adequately address the collection, reporting, and storage of security-related data.

---

##### **Improved Guidance**:

1. **Participation in Requirements Reviews**:

   * SA must actively engage in software requirements reviews to evaluate:
     + **Completeness of security requirements**: Do they cover all major areas (e.g., logging, monitoring, alerting, storage)?
     + **Clarity of requirements**: Are the security requirements specific, measurable, and feasible? Avoid vague terms such as "monitor system activity" without detailed implementation objectives.
   * SA should flag the absence of critical security requirements. For instance:
     + Missing requirements for independent log storage to protect against adversarial modification of primary logs.
     + Insufficient requirements for detecting reporting failures (e.g., undelivered alerts go unnoticed).
2. **Assess Alignment with Risk Posture**:

   * Ensure that the adversarial detection requirements align with the system's **security context and risk posture**. For high-risk or mission-critical systems:
     + Collection mechanisms should be designed for redundancy.
     + Reporting mechanisms must support real-time alerts.
     + Storage should include robust tamper-resistance mechanisms.
   * For lower-risk systems, requirements can prioritize more cost-effective or limited detection features while still meeting the baseline standard.
3. **Traceability Assurance**:

   * Confirm that detection of adversarial actions is explicitly reflected in the **System Hazard Analysis (SHA)** and connected to safety-critical software discussions where applicable.
   * Ensure bi-directional traceability from security requirements to associated design, test, and verification activities in the RTM.
4. **Risk-Based Prioritization of Requirements**:

   * Focus on adversarial actions that pose the greatest risks to mission success. SA should ensure requirements emphasize:
     + Prior detection of unauthorized access or tampering with system-critical assets.
     + Failure to detect adversarial manipulation of mission-critical data or terminals.
   * Track mitigations or design approaches for high-risk events and verify that the implementation addresses these effectively.
5. **Validation During Requirements Assessment**:

   * SA must confirm that:
     + Requirements specify **what to log** (e.g., authentication attempts, resource usage, file changes).
     + Logging designs consider adversary behavior, such as attempts to delete or alter logs.
     + Reporting requirements define severity thresholds and escalation protocols.
     + Storage requirements specify backup, redundancy, and protection against modification.
6. **Post-Deployment Lessons Applied**:

   * Review lessons learned from similar projects to enhance the quality of requirements during assessments. Apply guidance such as:
     + Pre-emptively addressing log tampering risks by requiring secure independent storage.
     + Accurate and actionable reporting requirements based on severity thresholds.

---

### **Summary of Software Assurance Guidance for Requirement 3.11.8**

#### **Key Actions for SA**:

1. Analyze and report on software volatility over time, focusing on adversarial detection requirements.
2. Validate that all adversarial action detection requirements are specified, implemented, and verifiable through traceability artifacts.
3. Track metrics to measure the scope, effectiveness, and stability of security-related requirements.
4. Actively participate in requirements reviews to assess completeness, clarity, and risk alignment of adversarial detection requirements.
5. Ensure post-deployment lessons and system-specific risk profiles shape requirement definitions.

This guidance provides a structured framework for software assurance activities, ensuring adversarial detection capabilities are comprehensively addressed throughout the development lifecycle.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

See also [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)        * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

**Objective Evidence** refers to verifiable documentation, artifacts, and outputs that demonstrate compliance with this requirement. For Requirement 3.11.8, this includes all activities, products, and processes showcasing the identification, implementation, and verification of software requirements related to the detection, reporting, and storage of adversarial actions.

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

  

### **Key Areas of Objective Evidence**

#### **1. Software Requirements Documentation**

The foundation of compliance lies in creating comprehensive and well-documented requirements that explicitly define the system's ability to detect and respond to adversarial actions.

##### **Artifacts and Evidence**:

* **Software Requirements Specification (SRS) Document**:
  + Contains explicit requirements for:
    - **Collection**: Data logging details such as login failures, authentication attempts, system configuration changes, and abnormal boundary violations.
    - **Reporting**: Notification mechanisms for prioritized reporting of adversarial actions (e.g., different severity levels for security incidents).
    - **Storage**: Specifications for secure, redundant, and tamper-proof storage of logs and data.
  + Requirements should be traceable to system-level cybersecurity goals (mission assurance, confidentiality, integrity, and availability).
* **Traceability Matrix (e.g., RTM)**:
  + Tracks each identified requirement for adversarial detection from inception to verification, test, and validation.
  + Ensures traceability between related requirements, system-level needs, implementation, and testing.
* **Derived/Allocated Requirements**:
  + Documents requirements allocated to both software and hardware for implementing adversarial collection, reporting, and storage.

##### **Evidence Review Checklist**:

* Are the adversarial action requirements clearly specified for collection, reporting, and storage?
* Are the key adversarial use cases documented to justify the need for these requirements?
* Are all key requirements mapped to tests and implementation artifacts in the RTM?

---

#### **2. System Architecture & Design Documentation**

System architecture and design evidence must demonstrate how the requirements for adversarial detection are integrated into the software design.

##### **Artifacts and Evidence**:

* **System and Software Architecture Documents**:
  + Describes how collection, reporting, and storage functions are implemented in the system. Examples:
    - Use of logging subsystems for real-time data collection.
    - Use of architecture patterns for secure data storage (e.g., encrypted logs, redundancy mechanisms).
    - Notification systems for reporting threats based on defined severity levels.
* **System Design Review (SDR) and Software Design Review (SwDR) Artifacts**:
  + Confirm that adversarial action requirements are addressed in high-level and detailed design stages.
* **Interface Control Documents (ICDs)**:
  + Defines how systems interact to support adversarial detection (e.g., communication interfaces for external reporting or offloading logs).
* **Data Flow Diagrams (DFDs)**:
  + Provides evidence of how adversarial data is collected, processed, stored, and reported within the system.

##### **Evidence Review Checklist**:

* Has the architecture been designed to support logging, reporting, and secure storage?
* Are redundant or independent systems included for accurate detection and tamper-proof storage?
* Are security mechanisms embedded (e.g., encrypted communication, secure logging channels)?

---

#### **3. Test Plans, Procedures, and Reports**

Testing is critical to provide evidence that the requirements for adversarial action detection have been properly implemented and verified.

##### **Artifacts and Evidence**:

* **Test Plans**:
  + Include specific test cases to verify:
    - Logging completeness: Ensures all critical adversarial actions are detected and logged.
    - Reporting mechanisms: Validates notifications for critical security events.
    - Storage integrity: Confirms that logs cannot be deleted or altered by adversaries.
  + Cover both functional testing (e.g., logging accuracy) and non-functional testing (e.g., system performance under load or during attacks).
* **Test Procedures and Scripts**:
  + Define test automation or manual processes used to verify logging, reporting, and storage capabilities.
* **Test Results and Reports**:
  + Summarize evidence of successful testing for adversarial action-related requirements:
    - Example: "Logs accurately recorded and encrypted all failed login attempts and configuration changes in Test Case X."
    - Example: "Report successfully generated with proper severity categorization for simulated boundary violation."
* **Penetration Test Reports**:
  + Provides evidence of the system's ability to withstand adversarial actions.
  + Includes simulation logs of attacks (e.g., brute-force login attempts) and evaluates logging, reporting, and storage effectiveness.
* **Regression Testing Reports**:
  + Verify that adversarial action detection is not negatively impacted by software updates.

##### **Evidence Review Checklist**:

* Are all adversarial detection requirements mapped to corresponding test cases?
* Were the requirements successfully verified, and were gaps recorded and addressed?
* Is there evidence of targeted adversarial simulations (e.g., tampering, unauthorized access)?

---

#### **4. Implementation and Code Artifacts**

Evidence from implementation demonstrates that the adversarial action requirements have been translated into working code and integrated into the software.

##### **Artifacts and Evidence**:

* **Code Documentation**:
  + Source code evidence implementing:
    - Logging mechanisms (functions or modules that log adversarial actions).
    - Reporting systems for alert generation.
    - Secure storage strategies (e.g., encryption of log files, periodic backups).
  + Includes inline comments describing how code components address requirements.
* **Configuration Files**:
  + Show configurations for logging levels, file rotation/archival policies, reporting triggers, and secure data handling procedures.
  + Examples:
    - Enabling logging for authentication failures (`auth.log` in Linux systems).
    - Defining email alerts for severe security incidents in the reporting system.
* **Version Control System (VCS) Logs**:
  + Details of changes to code/configurations made to implement adversarial detection functions.
* **Code Review Records**:
  + Provide evidence of internal/peer reviews focused on security-related code, ensuring adherence to best practices for detecting adversarial actions.

##### **Evidence Review Checklist**:

* Are security-related detection mechanisms implemented, tested, and documented in the codebase?
* Does the review process confirm that the implementation meets security guidelines?

---

#### **5. Process and Workflow Evidence**

The process evidence provides assurance that the detection of adversarial actions was a deliberate and structured part of the software development lifecycle.

##### **Artifacts and Evidence**:

* **Requirements Review Records**:
  + Confirm adversarial action requirements were discussed, reviewed, and approved during requirements definition phases.
* **Risk Assessment Reports**:
  + Evidence that risks associated with adversarial actions have been identified and mitigated, with detection serving as a primary control for identified risks.
* **Software Assurance Reports**:
  + Certification by Software Assurance that adversarial detection requirements have been properly implemented and validated.
* **Configuration Management Plans**:
  + Ensure files/configurations related to collection, reporting, or storage are version-controlled and protected from adversarial tampering.

---

#### **6. Lessons Learned and Post-Deployment Evidence**

Post-deployment evidence ensures that detection mechanisms work as intended and improve based on operational feedback.

##### **Artifacts and Evidence**:

* **Operational Logs**:
  + Collected real-world logs demonstrating the system’s ability to detect and report adversarial actions during mission use.
* **Incident Response Reports**:
  + Analyze the system's ability to detect adversarial attempts. For example:
    - Did the logging system accurately capture the events?
    - Were alerts sent to operators in a timely manner?
* **Lessons Learned Documentation**:
  + Evidence that adversarial actions were analyzed and used to improve future requirements.

---

### **Summary of Objective Evidence**

Below is a quick-check table summarizing key artifacts:

| **Category** | **Artifacts/Evidence** |
| --- | --- |
| Requirements Documentation | SRS, RTM, risk assessments, derived requirements |
| Architecture/Design | Architecture diagrams, SDR, design reviews, ICDs, DFDs |
| Testing | Test plans, procedures, results, penetration/regression tests |
| Implementation | Code, configuration files, VCS logs, code reviews |
| Processes | Requirements reviews, assurance records, configuration management |
| Post-Deployment | Operational logs, incident reports, lessons learned |

By generating and maintaining these artifacts, a project can demonstrate clear compliance with Requirement 3.11.8 while supporting system security and mission assurance goals.
