# 7.27 - Software Non-conformance Levels and Fields

> NASA Software Engineering Handbook (SWEHB Ver D), page id 256671746. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/256671746/7.27+-+Software+Non-conformance+Levels+and+Fields

7.27 - Software Non-conformance Levels and Fields

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/256671746/7.27+-+Software+Non-conformance+Levels+and+Fields#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=256671746)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=256671746&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Scope](#tabs-2)
* [3. Non-conformance Levels](#tabs-3)
* [4. Standardized Data Fields for Records](#tabs-4)
* [5. Definitions](#tabs-5)
* [6. Defect Tracking Systems](#tabs-6)
* [7. Lessons Learned](#tabs-7)
* [8. References](#tabs-8)

# 1. Purpose

This topic establishes NASA-specific guidance on standard software non-conformance (defect) levels and fields.  Standardization of these levels enables consistent metrics collection, risk assessment, and management across all NASA software projects.  The non-conformance levels and fields in this guidance have been generalized to apply to all projects.  The guidance aligns with NPR 7150.2 requirements (notably SWE-202) and incorporates lessons learned from NESC assessments.

# 2. Scope

Applies to all software developed, acquired, or managed by NASA, including flight, ground, simulation, and mission support software.  Projects may tailor definitions for their specific context but must maintain traceability to the Agency standard.

# 3. Non-conformance Levels

NASA recommends the following standardized severity levels, mapped to typical criteria and examples. All criteria are “or” statements; not all must be met for a severity assignment.

|  |  |  |
| --- | --- | --- |
| **Severity** | **Criteria** | **Examples** |
| **1. Catastrophic** | ·       Causes loss of life or injury,  ·       Loss of a primary mission essential capability  ·       Complete loss of mission critical asset  ·       Inability to achieve primary mission success criteria | Flight termination system fails, propellant tanks not pressurized, ECLSS systems do not operate, Loss of GNC or vehicle control, primary telescope equipment does not function, failure to detect humans in path, aircraft control surface position commanded into stall regime, rejecting commands based on time roll-over, secret keys are revealed, propellant exhausted, software corrupts critical parameters. |
| **2. Critical** | ·       Degradation of essential mission capability (primary or backup)  ·       Damage/destruction to mission asset which affects performance (primary or secondary)  ·       Impact the accomplishment of a primary mission objective  ·       Significant reduction to requirements margins or design margins | Failure to perform safing actions, efficiency of ECLSS system drops to restricted level, safety critical redundant system does not operate, causes nozzles to impact each other, processor overhead reduced from 20% to 5%, communications packets are lost after a threshold, power management incorrectly prioritizes non-essential systems, unit conversion errors, repeated thruster firings (ie cancelling each other out), calculation errors that accumulate over time. |
| **3. Moderate** | ·       Degradation of system dependability  ·       Loss of non-essential capability  ·       Impact on the accomplishment of extended/optional/secondary mission objectives  ·       Degradation of an essential capability or inability to accomplish mission objective, but with a known or operation work around workaround | Causes intermittent failures (intermittent race condition), loss of functionality in specific (or multiple failure) conditions, secondary payload does not operate/launch, automated commanding does not work resulting in operators having to use manual commands, small memory leak, old log files are not automatically cleared, disabled a secondary sensor (developmental flight instrumentation), incorrect data on screen but log file contains correct data. |
| **4. Minor** | ·       Degradation of a non-essential capability  ·       Creates inconvenience for operators, crew or other projects' personnel  ·       Defect impacting maintainability on current mission or reuse on future missions | Unused code or parameters, confusion of variable usage, software control of a non-critical system does not work (light control, zooming in of parameters, ...), hard coding parameters for current mission, graphical version does not work but textual does, optional video frame rate not as high, auxiliary interface has data lag, secondary payloads are limited to a lower data rate, several manual steps are needed or optional input is required, duplicated constants, repeated code. |
| **5. Communications or Editorial** | ·       Defect impacting documentation and communication clarity | Documentation incorrect, comments in code incorrect, ambiguous messages from software, inconsistent terminology, color indications without explanation or legend, units are missing, wrong time zone, information from previous versions. |

# 4. Standardized Data Fields for Records

To enable consistent analysis and reporting, each defect record should include at minimum:

* Date defect opened
* Date defect closed
* Severity/criticality rating (Catastrophic, Critical, Moderate, Minor, etc.)
* Computer Software Configuration Item(s) (CSCI) affected
* Defect type (e.g., code bug, documentation, requirements, etc.)
* Status (Closed, In Work, No Fix/Deferred)
* Description and rationale for disposition (including workaround or Ops Note if applicable)

# 5. Definitions

Essential Capability: Behaviors required for minimum mission success

Non-Essential Capability: Secondary behaviors not required for minimum mission success

System Dependability: System performs trusted, intended functions safely, securely, and timely

Workaround: Formally documented procedure to mitigate impact

# 6. Defect Tracking Systems

* **Separation of Workflow and Defect Tracking:** Projects may use different tools for workflow management and defect tracking. Guidance should clarify the distinction and ensure defect records are not lost or misclassified when transitioning between builds or launches.
* **Defect Closure Practices:** NASA internal programs typically close defects for a given flight/build and open new records for future builds. Deferred defects should be clearly documented and tracked for subsequent missions.
* **Ops Notes:** Defects not fixed for launch should be accompanied by Operations Notes, which document mitigations and operational impacts. The number and severity of Ops Notes should be tracked as a measure of operational complexity.

# 7. Lessons Learned

* **Standardization Needed:** Comparison across programs was hampered by inconsistent severity definitions and defect tracking practices. NASA should adopt a minimum set of standardized severity levels and data fields.
* **Centralized Repository:** NASA should develop a centralized, cloud-based repository for defect data to enable cross-program analysis and lessons learned.

# 8. References

* NESC-RP-22-01759: Software Defect Density Analysis Report (June 2023)
* IEEE Std 982.1-1988: Measures to Produce Reliable Software
