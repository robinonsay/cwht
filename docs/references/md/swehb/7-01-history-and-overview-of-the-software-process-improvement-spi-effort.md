# 7.01 - History and Overview of the Software Process Improvement SPI Effort

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695611. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort

7.01 - History and Overview of the Software Process Improvement (SPI) Effort

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695611)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695611&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. NASA Software Engineering Initiative](#tabs-2)
* [3. Conclusion](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Purpose

NASA’s software engineering capability is a cornerstone of mission success. NPR 7150.2, NASA’s Software Engineering Requirements directive, has been central to standardizing practices and improving software reliability across the Agency.

# Historical Context

* 1960s–1970s: Early space missions revealed software reliability challenges, including Apollo 11 lunar landing alarms (1969).
* 1976: NASA held its first Software Engineering Workshop to address software quality and reliability.
* Late 1980s: Software Management and Assurance Program (SMAP) introduced to improve oversight.
* 2000–2002: NASA Software Engineering Initiative (NSEI) launched under Engineering Excellence Initiative to integrate software engineering and assurance principles across Centers.

# NPR 7150.2 – 20 Years of Evolution

NPR 7150.2 was first issued in 2004 to establish a unified set of software engineering requirements across NASA. Below are detailed revision summaries:

* Initial Release (2004): Introduced baseline requirements for software engineering, focusing on consistency and compliance across Centers.
* Revision A (2009): Incorporated lessons learned from early implementations and aligned with evolving mission-critical software needs.
* Revision B (2013): Expanded coverage for software assurance and safety, reflecting increased emphasis on risk management and IV&V.
* Revision C (2017): Integrated updates for cybersecurity, model-based engineering, and clarified tailoring guidance.
* Revision D (2022): Strengthened alignment with NPR 7123.1 (Systems Engineering), added explicit requirements for software assurance and safety (NASA-STD-8739.8), and emphasized continuous improvement and metrics-driven maturity.

# Key Changes Over Time

* Early focus: Basic compliance and standardization.
* Mid-phase: Added assurance, safety, and IV&V requirements.
* Recent updates: Cybersecurity, advanced modeling, and continuous improvement.
* Cultural shift: From compliance-driven to performance-driven, emphasizing metrics and maturity models.

# Impact on Software Assurance and Engineering

NPR 7150.2 provides structured requirements for design, development, and verification (Software Engineering) and ensures compliance with safety standards and risk mitigation strategies (Software Assurance). Together, they create a dual framework for technical rigor and mission safety.

# Lessons Learned

NASA’s experience underscores the importance of Independent Verification & Validation (IV&V), early defect detection, and continuous improvement to adapt to evolving technologies and mission needs.

## 1.1 Introduction

Software engineering is a core capability and a key enabling technology for NASA's missions and supporting infrastructure.

**NPR7150.2D**

1.1.3 The Agency makes significant investments in software engineering to support the Agency’s investment areas: Space Flight, Aeronautics, Research and Technology, Information Technology (IT), and Institutional Infrastructure. NASA ensures that programs, projects, systems, and subsystems that use software follow a standard set of requirements. One of the goals of this directive is to bring the Agency’s engineering and software development and management communities together to optimize resources and talents across Center boundaries. For NASA to effectively communicate and work seamlessly across Centers, a common framework of generic requirements is needed.[083](#_tabs-<p>4</p>)

NPR 7150.2 [083](#_tabs-<p>4</p>) is written in the "shall" statement format with supplemental information in the form of accompanying notes and appendices. While these were included to help explain the meaning of each requirement, it was recognized that additional detail on the scope and the applicability of each SWE would increase the speed of cultural change and adoption of these software requirements. This Handbook, NASA-HDBK-2203, was established in wiki format to help achieve the above goals.

See [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) in this handbook for the requirement.

During the development of the NPR 7150.2, there was an intentional effort to minimize the size of the document by keeping it focused on the requirements. However, the 7150 teams had developed a large amount of additional guidance material for the NPR, which they decided could be more effectively utilized in a NASA Handbook rather than in the NPR itself.

# 2. NASA Software Engineering Initiative

## **NASA Software Engineering Initiative**

### **Overview**

Software engineering is a **core capability and enabling technology** for NASA’s missions and supporting infrastructure. Over time, surveys and assessments revealed significant challenges in software development across the Agency, including increasing complexity, cost, and risk. To address these issues, NASA Headquarters’ Office of the Chief Engineer (OCE) launched the **NASA Software Engineering Initiative (NSEI)** in **2002**. This initiative established a **NASA-wide, comprehensive approach** to improve software engineering processes and achieve quantifiable maturity levels commensurate with mission criticality.

### **What is the Initiative?**

A coordinated, Agency-wide effort to:

* Standardize and improve software engineering processes.
* Infuse advanced tools and technologies.
* Elevate software assurance practices alongside engineering.

### **Why Was It Created?**

To meet NASA’s software challenges:

* Increasing schedule and cost pressures.
* Growing complexity of mission-critical software.
* Need for consistent application of best practices across Centers.

### **Key Elements of NASA’s Approach**

* **Integration of principles:** Combine sound software engineering and software assurance standards.
* **Workforce development:** Enhance knowledge and skills of engineers and assurance personnel.
* **Benchmarking:** Use the Integrated Capability Maturity Model for assessments.
* **Tool infusion:** Deploy modern software engineering tools.
* **Metrics:** Collect and analyze software metrics to drive improvement.

### **Who Deploys It?**

* **OCE** in collaboration with:
  + NASA Engineering and Safety Center (NESC)
  + Office of Safety and Mission Assurance (OSMA)
  + NASA IV&V Facility
  + Center software working groups and projects

### **Guiding Principles**

* Develop efficient, automated methods.
* Improve risk, issue, and defect reporting.
* Reduce software failure risk and increase mission safety.
* Detect and remove defects early in the lifecycle.
* Apply industry and government best practices.
* Provide predictable cost and schedule estimates.
* Educate NASA workforce on software engineering excellence.
* Reduce duplication of effort across projects.
* Adapt to evolving software technologies.

### **Scope**

The initiative addresses:

* **Process improvement** for mission-critical and non-mission-critical software.
* **Software safety and quality.**
* **Workforce development** and retention.
* **Knowledge sharing** through a Software Community of Practice.

### **What It Provides**

* Technical support for project issues and special studies.
* Agency and NESC subject matter expertise.
* Recommendations and maintenance of requirements, policies, and standards.
* Internal and external assessments of software development organizations.
* Reporting on the state of the software discipline.
* Coordination of external interfaces for software engineering.
* Collection and analysis of software metrics to identify trends.
* Continuous improvement of software processes.
* Knowledge management and community engagement.

[Review - SWE-002 - Software Engineering Initiative](#) is the NPR 7150.2 requirement for the Software Engineering Initiative.

[Review - SWE-005 - Software Processes](#) is the NPR 7150.2 requirement for the Software Processes. Addresses Centers establishing an SEPG and a Process Asset Library.

[Review - SWE-095 - Report Engineering Discipline Status](#) requires reporting on the status of the Center’s software engineering discipline, as applied to its projects, upon request by the OCE, OSMA, or OCHMO.

[Review - SWE-208 - Advancing Software Assurance and Software Safety Practices](#) requires that the NASA Chief, SMA shall lead and maintain a NASA Software Assurance and Software Safety Initiative to advance software assurance and software safety practices.

# 3. Conclusion

Ensuring the **quality, reliability, and safety** of NASA software is essential to achieving mission success across all Agency programs and projects. The **NASA Software Process Improvement Initiative** serves as a cornerstone for this effort by uniting a diverse ecosystem of expertise—software engineers, assurance specialists, researchers, and practitioners—with proven processes, maturity models, and advanced tools. Through integrated standards, accredited methodologies, and productivity-enhancing technologies, the initiative drives continuous improvement, reduces risk, and promotes engineering excellence. Ultimately, this collaborative approach strengthens NASA’s ability to deliver robust, mission-critical software that meets the highest standards of performance and safety.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-038)

  [NASA Software Engineering Initiative Implementation Plan,](http://www.nasa.gov/pdf/417063main_NSII_Plan.pdf "Click to open in new window")

  Release 1.0, NASA Office of the Chief Engineer, 2002.
* (SWEREF-040)

  [NASA Study on Flight Software Complexity (Final Report),](http://www.nasa.gov/offices/oce/documents/FSWC_study.html "Click to open in new window")

  Commissioned by the NASA Office of Chief Engineer, Technical Excellence Program, Adam West, Program Manager, and edited by Daniel L. Dvorak, Systems and Software Division, Jet Propulsion Laboratory, 2009.
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-170)

  [NASA Study on Flight Software Complexity.](https://www.nasa.gov/pdf/418878main_FSWC_Final_Report.pdf "Click to open in new window")

  D. Dvorak, Presented at AIAA Infotech@Aerospace, Seattle, WA, April 2009. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-204)

  [The NASA SARP Software Research Infusion Initiative,](https://ntrs.nasa.gov/search.jsp?R=20070016012 "Click to open in new window")

  Hinchey, M., NASA Software Working Group, July 2006.
* (SWEREF-205)

  [NASA Initiative for Software Safety and Quality,](https://trs.jpl.nasa.gov/bitstream/handle/2014/16489/00-2550.pdf?sequence=1 "Click to open in new window")

  John Kelly, 25th Annual Software Engineering Workshop, November 30, 2000,  This is the presentation that introduced the Initiative and for the specific rationale for the Initiative.
* (SWEREF-255) NASA Assurance Process for Complex Electronics: Traceability Analysis (2009, December 14).  Link no longer valid last reviewed March 15, 2012 from http://www.hq.nasa.gov/office/codeq/software/ComplexElectronics/techniques/traceability-analysis.htm.
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-290) OCE Software Survey Instructions and Templates (on SPAN) This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook. 2010 Software Inventory instructions, version 7 (available from the OCE).
* (SWEREF-389)

  [APPEL Software Engineering Management 301 (SWE 301).](http://appel.nasa.gov/course-catalog/appel-swem/ "Click to open in new window")

  Course from APPEL: Academy of Program/Project & Engineering Leadership.
* (SWEREF-408)

  [Computers in Spaceflight: The NASA Experience.](http://history.nasa.gov/computers/Ch1-2.html "Click to open in new window")

  Gemini 1962. NASA. 2005. See Chapter One - The Gemini Digital Computer: First Machine in Orbit.
* (SWEREF-409)

  [Apollo 11 Program Alarms](http://www.hq.nasa.gov/alsj/a11/a11.1201-pa.html "Click to open in new window")

  In the Apollo 11 Lunar Surface Journal. Peter Adler. NASA. 1998. See section on computer restarts.
* (SWEREF-518)

  [Independent Verification and Validation of Embedded Software](https://llis.nasa.gov/lesson/723 "Click to open in new window")

  Public Lessons Learned Entry: 723.

  

## 4.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 4.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-005 - Software Processes](/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes) * [SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-208 - Advancing Software Assurance and Software Safety Practices](/spaces/SWEHBVD/pages/102695328/SWE-208+-+Advancing+Software+Assurance+and+Software+Safety+Practices) |

## 4.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Center Libraries](https://nen.nasa.gov/web/software/wiki) |

## 4.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 5. Lessons Learned

### 5.1 NASA Lessons Learned

### NASA Lessons Learned: SWEHB & Software Engineering Initiative

#### **From the SWEHB History & SPI Effort (Topic 7.01)**

* **Defects found early drive improvement**  
  Evaluations of research-infused tools—like orthogonal-defect classification and code static-analysis tools—revealed defects that traditional testing missed. These insights led to adoption of new techniques across Centers
* **Assessment ensures maturity growth**  
  Tracking SCAMPI/CMMI appraisals from FY07–FY10 showed growth in organizational maturity at major Centers, reinforcing the value of structured improvement
* **Wiki lifecycle enables ongoing enhancement**  
  Shifting NPR 7150.2 guidance to a living wiki (SWEHB) allowed continual content updates based on real project experiences, improving adoption and cultural change

#### **From 25 Years of GSFC Software Engineering Laboratory (SEL)**

* **Data-informed process evolution**  
  SEL’s work showed the importance of collecting project data and analytics to guide software process improvements, avoiding reliance on anecdote
* **Need for institutional support**  
  SEL’s impact declined due to shifting NASA priorities and resource constraints. Lesson: sustaining improvement requires active Agency-level sponsorship

#### **From NASA Lessons Learned Information System (LLIS)**

* **Lessons need closed-loop integration**  
  Audits revealed that merely storing lessons isn’t effective. JPL demonstrated success by incorporating lessons learned compliance assessments at each project milestone
* **Proactive infusion accelerates uptake**  
  JPL’s strategy to embed lessons into procedures and training institutionalized learning, rather than relying on individual awareness

These lessons highlight key strategies for software excellence:

* Leverage practical tools and metrics to uncover and fix defects early.
* Pair Agency-wide leadership with sustained funding to drive lasting process improvement.
* Use living handbooks (like SWEHB) for continuous refinement of guidance.
* Integrate lessons learned systematically into procedures, training, and project milestones.

Would you like me to include a table summarizing each lesson with its source and impact for easy reference in your newsletter or presentation?

Here are key NASA lessons learned associated with the **SWEHB Handbook** and the **NASA Software Engineering Initiative**:

---

### ✅ **Lessons from SWEHB & SPI Effort**

* **Early Defect Detection Improves Quality**  
  Research-infused tools (e.g., orthogonal defect classification, static analysis) uncovered defects missed by traditional testing, leading to adoption of advanced techniques across Centers.  
  *Impact:* Reduced mission risk and improved software reliability.
* **Continuous Improvement via Wiki Handbook**  
  Moving NPR 7150.2 guidance into a living wiki (SWEHB) enabled ongoing updates based on real project feedback, accelerating cultural adoption of best practices.
* **Maturity Assessments Drive Progress**  
  SCAMPI/CMMI appraisals showed measurable growth in Center process maturity, validating structured improvement approaches.

---

### ✅ **Lessons from NASA Software Engineering Laboratory (SEL)**

* **Data-Driven Process Evolution**  
  SEL demonstrated that collecting and analyzing project data is critical for guiding effective process improvements—avoiding reliance on anecdotal fixes.
* **Institutional Support is Essential**  
  SEL’s decline due to shifting priorities and budget cuts underscores that sustained improvement requires strong Agency-level sponsorship.

---

### ✅ **Lessons from NASA LLIS (Lessons Learned Information System)**

* **Closed-Loop Integration is Key**  
  Simply storing lessons isn’t enough. JPL improved uptake by embedding lessons into procedures and training, ensuring they influence projects at the right time.
* **Milestone-Based Compliance Works**  
  JPL’s practice of assessing lessons learned applicability at major reviews helped prevent mission risks (e.g., thruster plume impingement on MER).

### 5.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
