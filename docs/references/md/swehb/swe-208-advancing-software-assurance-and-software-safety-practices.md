# SWE-208 - Advancing Software Assurance and Software Safety Practices

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695328. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695328/SWE-208+-+Advancing+Software+Assurance+and+Software+Safety+Practices

SWE-208 - Advancing Software Assurance and Software Safety Practices

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695328/SWE-208+-+Advancing+Software+Assurance+and+Software+Safety+Practices#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695328)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695328&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.2.2 The NASA Chief, SMA shall lead and maintain a NASA Software Assurance and Software Safety Initiative to advance software assurance and software safety practices.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-208 History

SWE-208 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B | RESERVED |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE in D  In previous versions this was a will statement |
| D | 2.1.2.2 The NASA Chief, SMA shall lead and maintain a NASA Software Assurance and Software Safety Initiative to advance software assurance and software safety practices. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

To ensure that the processes, procedures, and products used to produce and sustain NASA software conform to all requirements and standards specified to govern those processes, procedures, and products.

Software assurance (SA) and software safety are critical components of NASA's mission success. Modern space missions heavily depend on software to operate spacecraft, manage systems, process scientific data, enable human safety, and ensure the overall integrity of operations. Given the complexity, scale, and high-risk environment of NASA's software-driven missions, advancing software assurance and safety practices is not optional—it is a strategic necessity.

This requirement establishes the leadership role of the NASA Chief, SMA in maintaining a cohesive, forward-looking initiative to drive continuous improvement in software assurance and safety. By centralizing efforts in this domain, NASA ensures robust practices are developed and shared across the agency, ultimately reducing risk, increasing mission success, and safeguarding astronauts, equipment, and investments.

## 2.1 Key Rationale for the Requirement

### 1. Software is Critical to Mission Success

* **Explanation:** NASA missions rely extensively on software to control spacecraft, execute science objectives, and ensure reliable and safe operation of mission-critical systems.
* **Supporting Points:**
  + Software failures accounted for significant issues in historical missions (e.g., Mars Climate Orbiter, Boeing Starliner Orbital Flight Test). These failures were preventable with better software assurance and safety measures.
  + Software serves as the “brain” of key systems that operate in extreme environments where manual intervention is impossible. For example, spacecraft in deep space or uncrewed Earth-orbit missions rely on fault-tolerant software to autonomously execute critical tasks.
* **Relevance to Requirement:** A dedicated software assurance and safety initiative ensures that software is rigorously tested and verified for functionality and safety across all mission phases, minimizing the potential for catastrophic failures.

### 2. The Unique Challenges of Software Assurance at NASA

* **Explanation:** NASA faces unique challenges in its software development and assurance due to the complexity, criticality, and long lifecycle of its systems.
* **Supporting Points:**
  + Space software must perform flawlessly in unforgiving environments such as space radiation, microgravity, extreme temperatures, and limited bandwidth for communication. Software assurance processes must address these unique constraints.
  + Mission software typically operates for decades (e.g., Voyager spacecraft), requiring sustained assurance and maintenance strategies to support long-term success.
  + Ensuring the safe interaction of software with hardware in high-risk systems (e.g., human-rated spacecraft like Artemis, advanced autonomous systems) demands specialized software safety practices.
* **Relevance to Requirement:** Leading a proactive initiative allows the SMA office to continually adapt and advance software assurance and safety practices to address these NASA-specific challenges efficiently.

### 3. Safety is Paramount in NASA Missions

* **Explanation:** Safety is a cornerstone of NASA’s operations, especially for human spaceflight. Ensuring software functions properly under all conditions is essential to maintaining the safety of astronauts and protecting equipment.
* **Supporting Points:**
  + Software errors with safety-critical consequences can result in avoidable loss of life, mission, or assets.
  + Safety assurance involves the anticipation and prevention of hazardous conditions caused by software failures, such as improper throttling of engines, incorrect trajectory computations, or mismanagement of life support systems.
  + Risks can be introduced during software lifecycle phases (e.g., design, development, testing, maintenance). A unified initiative supports rigorous, systematic safety procedures to mitigate these risks at every stage.
* **Relevance to Requirement:** Central leadership under the SMA office ensures that advancements in software assurance and safety comprehensively address safety concerns for human-rated and high-stakes missions.

### 4. The Complexity of Software Systems is Increasing

* **Explanation:** The increasing complexity of NASA software requires advanced techniques for assurance and safety. Software is more intricate today, with interconnected systems, Artificial Intelligence (AI), Machine Learning (ML), and autonomous decision-making becoming pivotal to NASA missions.
* **Supporting Points:**
  + AI/ML-based systems like those used in autonomous rovers, fault-tolerant autonomy, and decision systems introduce challenges in verification and validation (V&V). These systems demand new assurance techniques that maintain safety while allowing flexibility.
  + The integration of commercial off-the-shelf (COTS) software introduces greater unpredictability, dependencies, and lack of full internal control, necessitating diligent assurance practices.
  + Cybersecurity threats to mission-critical software increase the need for continued focus on secure software assurance strategies.
* **Relevance to Requirement:** Leading an agency-wide initiative ensures that NASA evolves its practices to verify and validate increasingly complex software systems without compromising safety or functionality.

### 5. Lessons Learned from Past Software-Related Anomalies

* **Explanation:** Historical mission anomalies underline the importance of software assurance to prevent recurrence of similar issues.
* **Examples of Past Failures:**
  + **Mars Climate Orbiter (1999):** Metric-to-imperial unit conversion error in software caused the spacecraft to burn up in the atmosphere. A robust software assurance process, including unit-conversion verifications, could have prevented this.
  + **Ariane 5 Maiden Flight:** Software design flaws led to the destruction of the rocket mere seconds after launch.
  + **Boeing Starliner OFT-1 (2019):** Clock synchronization issues in software resulted in the spacecraft being unable to reach its intended orbit.
* **Relevance to Requirement:** An SMA-led initiative preserves institutional knowledge from past failures and ensures that new assurance methods build on lessons learned, driving continual improvement.

### 6. Centralized Leadership Promotes Consistency

* **Explanation:** Software assurance and safety practices can vary between NASA Centers and projects. Without centralized leadership, inconsistencies can arise, leading to varying levels of quality and risk across the Agency.
* **Supporting Points:**
  + Central leadership ensures standardization of processes, tools, and methodologies, such as mandatory adherence to **NPR 7150.2:** **NASA Software Engineering Requirements** [083](#_tabs-<p></p>) and **NASA-STD-8739.8:****Software Assurance and Software Safety Standard** [278](#_tabs-<p></p>).
  + Consistency improves communication and knowledge sharing between Centers and multidisciplinary teams working on interconnected projects.
  + A collaborative framework under centralized leadership ensures that even small projects with limited resources have access to robust assurance practices.
* **Relevance to Requirement:** The NASA Chief, SMA leading the initiative ensures agency-wide consistency while facilitating communication and alignment across all projects.

### 7. Sustaining NASA’s Leadership in Software Engineering and Safety

* **Explanation:** NASA is a world leader in advanced engineering, and maintaining this position requires continuous improvement in software assurance and safety. Establishing the initiative ensures NASA stays ahead of evolving challenges.
* **Supporting Points:**
  + NASA’s software practices frequently inform industry standards and global practices (e.g., lessons applied in aviation, nuclear power plants, and other high-risk industries).
  + Research and innovation in software assurance practices through this initiative enhance NASA’s ability to influence best practices across industries.
  + Proactively advancing software assurance keeps NASA ahead of technological changes and emerging risks, ensuring sustained success over multidecade missions.
* **Relevance to Requirement:** The leadership of SMA in advancing software safety and assurance safeguards NASA’s reputation as a forerunner in reliable and safe mission software engineering.

### 8. Facilitating a Culture of Safety and Continuous Improvement

* **Explanation:** A centralized initiative fosters a culture that prioritizes safety and operational excellence through knowledge sharing, accountability, and innovation.
* **Supporting Points:**
  + Through training, workshops, and tools, the initiative promotes software assurance as an integral part of the engineering culture at NASA.
  + This culture enables continuous knowledge transfer and improvement, particularly as workforce experience evolves and newer engineers join the agency.
  + Promoting safety-consciousness ensures that software assurance and safety remain high priorities regardless of external pressures such as budget or schedule constraints.
* **Relevance to Requirement:** An SMA-led initiative drives the cultural and organizational focus on software safety and quality across all of NASA.

## 2.2 Conclusion

Software assurance and software safety are not merely regulatory requirements at NASA—they are mission-critical activities that safeguard lives, preserve assets, and protect mission success. By leading and maintaining a centralized Software Assurance and Software Safety Initiative, the NASA Chief, SMA fosters standardization, drives innovation, ensures risk reduction, and supports the agency’s goal of safely exploring and advancing human knowledge.

The implementation of this requirement guarantees that all NASA projects, regardless of size or classification, benefit from a unified and advancing approach to assurance and safety, ensuring NASA remains at the forefront of engineering excellence.

# 3. Guidance

Software engineering is a core capability and a key enabling technology for NASA's missions and supporting infrastructure. It is instrumental in ensuring mission success, safety, adherence to schedules, and adherence to budgets. To achieve these outcomes, it is crucial to maintain a disciplined approach to software development, assurance, and safety that complies with Agency standards and utilizes best practices.

The NASA Software Initiative (see [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative)) exists to support NASA programs and projects in achieving their goals while ensuring compliance with specified software requirements. It focuses on improving software reliability, maintainability, security, and performance while proactively addressing risks and challenges associated with evolving software technologies.

**Software Assurance** is defined as the level of confidence that:

1. Software is free from vulnerabilities, whether intentionally designed into the software or accidentally introduced throughout its lifecycle.
2. The software performs as intended and fulfills its functional, safety, and mission requirements.

The **objective of NASA Software Assurance and Software Safety** [352](#_tabs-<p></p>) is to ensure that:

* The processes, procedures, and products used during software development and sustainment conform to all requirements and standards that govern them.
* Software products meet or exceed the levels of safety and assurance necessary for mission success.

Software Assurance Program

**Modern Space Systems Depend on Reliable Software**

* Software is a cornerstone of today's space systems, making "Software Assurance" essential to mission success. As software reliability and safety become increasingly critical, advancing methods to ensure these qualities is a key focus.

**Vision for Program and Discipline Development:**

* **Streamline Software Assurance Processes:** Develop more efficient, automated methods for ensuring software safety, software quality and IV&V across projects.
* **Improve Reporting Capabilities:** Enhance mechanisms for tracking and communicating risks, issues, and findings.
* **Showcase Value and Impact:** Highlight the importance and measurable benefits of Software Assurance and Software Safety activities in supporting NASA missions.
* **Standardize Tools and Methods:** Provide unified tools, services, and scalable improvements to ensure consistency and excellence in Software Assurance and Software Safety processes.
* **Data-Driven Enhancements:** Use analytics and metrics to refine and enhance all aspects of Software Assurance and Software Safety operations.
* **Proactively Address Software Risks:** Focus research and resources on resolving known software issues and advancing assurance strategies aligned with specific challenges.
* **Bolster Training and Standards:** Strengthen workforce skills and refine software safety requirements through NASA’s Software assurance and Software Safety Program and broader agency initiatives.

By pursuing these focused objectives, NASA aims to elevate software safety and assurance to meet the demands of increasingly complex space systems.

## 3.1 NASA Software Initiative

NASA continuously strives to maintain a skilled and diverse workforce with expertise in state-of-the-art technical competencies, including software assurance and software safety, which are core to the Agency's broader capabilities. A goal articulated in the **2018 NASA Strategic Plan** [117](#_tabs-<p></p>) supports this by highlighting the need to build and sustain technical expertise across the Agency.

The NASA Software Initiative ([SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative)) aligns with the Strategic Plan by:

1. Driving process and performance improvements across all software activities.
2. Advancing best practices in software assurance, software safety, and software engineering.

The following are key motivations for the NASA Software Initiative:

1. **Reducing the Risk of Software Failures**
   * Minimize the risk of mission-critical software issues that could result in loss of mission, life, or equipment.
   * Improve overall mission safety by implementing robust software practices.
2. **Improving Processes with Best Practices**
   * Leverage industry-leading best practices such as those defined by the Capability Maturity Model Integration (CMMI) framework.
   * Integrate lessons learned from previous projects to continuously refine and improve NASA software processes.
3. **Enhancing Risk Management**
   * Mitigate software-related risks by proactively identifying and addressing issues early in the development lifecycle.
   * Provide tools and processes to track and manage software risks effectively on Agency projects.
4. **Enabling Predictable Cost and Schedule Estimates**
   * Utilize proven software engineering methods to develop accurate cost estimates and improve delivery schedules for software projects.
   * NASA projects working within the CMMI framework have been shown to demonstrate increased cost accuracy and minimized resource growth over the system lifecycle.
5. **Educating NASA Personnel and Buyers**
   * Educate NASA personnel to become smart buyers and better collaborators when acquiring software from external contractors.
   * Promote a deeper understanding of software engineering principles, enabling NASA workforce members to make informed decisions.
6. **Defect Detection and Prevention**
   * Find and remove software defects earlier in the software lifecycle, where correction costs are significantly lower.
   * Reduce post-delivery defect discovery and associated rework through rigorous V&V (verification and validation) processes.
7. **Eliminating Redundancy**
   * Minimize duplication of software engineering efforts between projects by promoting the reuse of processes, tools, and templates.
   * Share lessons learned and software engineering resources across Centers and teams.
8. **Adapting to Evolving Software Technologies**
   * Increase NASA's ability to adopt cutting-edge software technologies, such as autonomous systems, Artificial Intelligence (AI), Machine Learning (ML), and secure development practices.
   * Encourage innovation while maintaining strict vigilance on safety and assurance.
9. **Improved Software Development Planning**
   * Enhance software development planning processes at the Agency level, with a growing consensus emphasizing that defined processes lead to better project outcomes.
   * Ensure project performance is consistently monitored, risks are managed, and corrective actions are timely.

## 3.2 NASA Software Activity Motivations

Specific software activities within NASA initiatives strive to bring measurable improvements across all aspects of software assurance, software engineering, and software safety. These motivations are as follows:

1. **Risk-Based Performance Requirements**
   * Define and implement risk-based software assurance requirements, ensuring flexibility for projects without compromising safety or mission priorities.
   * Tailor software assurance and safety activities to project-appropriate levels based on classification, criticality, and complexity.
2. **Improved Reporting and Communication**
   * Enhance issue, risk, and finding reporting mechanisms between software assurance teams and project managers, ensuring a transparent understanding of software health.
   * Provide timely feedback loops to prevent issues from escalating.
3. **Add Value to Software Assurance Activities**
   * Demonstrate how proactive software assurance activities directly contribute to mission success, improving confidence in software systems.
   * Focus on data-driven decision-making for identifying assurance challenges and prioritizing corrective actions.
4. **Standard Tools and Services**
   * Develop and share standardized software assurance tools and services across NASA projects to ensure consistency and improve quality.
   * Simplify the integration of these tools into both large-scale and small-scale software development efforts.
5. **Metrics-Driven Process Improvement**
   * Leverage data and metrics to measure the effectiveness of software assurance activities and drive continuous improvement.
   * Collect meaningful metrics that help identify bottlenecks, trends, and opportunities for automation in assurance workflows.
6. **Address Known Software Issues**
   * Focus on assurance activities that preemptively address known software vulnerabilities and issues.
   * Align research efforts to develop innovative solutions for existing and emerging software concerns.
7. **Efficient and Automated Assurance**
   * Invest in automation tools and efficient methods for processes like automated code scans, test case generation, and issue tracking.
   * Reduce manual effort associated with repetitive assurance tasks, freeing personnel to focus on complex challenges.
8. **Shared Assurance Tools and Services**
   * Establish a repository of shared tools, services, and expertise for Agency-wide use.
   * Create a collaborative network that allows teams to share knowledge, lessons learned, and reusable resources.
9. **Enhance Workforce Training**
   * Improve software assurance training programs as part of the Safety and Mission Assurance Technical Excellence Program (SMA-TEP).
   * Provide project-level and agency-wide training in new assurance standards, methodologies, and technologies.
   * Expand training opportunities to ensure the workforce is agile and well-prepared to meet evolving challenges.

## 3.3 Conclusion

The NASA Software Initiative, led by the Office of the Chief Engineer (OCE), plays a vital role in ensuring mission success, safety, and software quality. By advancing education, risk management, planning, and the adoption of best practices, this initiative ensures that NASA stays at the forefront of software engineering excellence. Through disciplined software assurance and software safety practices, NASA’s software engineering workforce is empowered to anticipate challenges, address risks, and deliver high-performing software systems that meet and exceed mission goals.

See also Topic [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) for additional details on the SPI Initiative. 

See also [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software).

See also [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) for the requirement on the Software Engineering Initiative.

See also [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management), [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans),

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)        * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects at NASA typically involve reduced scope, lower budgets, and shorter timelines compared to large-scale efforts. These projects, which can include CubeSats, prototypes, and low-criticality software tools, still require compliance with NASA's software assurance and safety standards. The Software Assurance and Software Safety Initiative ensures that even small projects can adopt right-sized assurance practices that suit their scale while maintaining quality, safety, and risk management throughout the software lifecycle.

The following guidance provides actionable recommendations for small projects, allowing them to effectively comply with this requirement without unnecessary overhead.

## 4.1 Guidance for Small Projects

### 4.1.1  Tailoring Software Assurance and Safety for Small Projects

Small projects can meet the intent of software assurance requirements by tailoring practices to focus on the critical areas of the project. NASA's Software Assurance and Software Safety Initiative provides tailored resources, such as lightweight processes, templates, and checklists, to support efficient and effective compliance for small efforts.

#### Key Actions for Tailoring:

1. **Scope Assurance Activities to Risk and Project Classification:**
   * Focus software assurance on areas with known risks or safety-critical components.
   * Implement only the minimum assurance activities required by **NPR 7150.2** [083](#_tabs-<p></p>) and **NASA-STD-8739.8** [278](#_tabs-<p></p>) for the project classification (e.g., Class C, D, or F).
2. **Simplify Assurance Documentation:**
   * Use lightweight templates for Software Assurance Plans (SAPs), risk management, and verification/validation.
   * Leverage preexisting examples and tools provided by the Process Asset Library (PAL).
3. **Leverage Shared Tools and Resources:**
   * Access standardized assurance tools and services offered by the Software Assurance Initiative (e.g., automated code analysis tools, reusable test cases).
   * Small projects benefit from not having to procure or develop their own tools.
4. **Right-Size Workforce Needs:**
   * Smaller projects typically do not require a dedicated software assurance team. Assign a dual-role engineer (e.g., software developer or systems engineer) to oversee lightweight assurance responsibilities.
   * Consult with an assurance SME (Subject Matter Expert) for periodic guidance and reviews.
5. **Use Agile Assurance Practices:**
   * Apply assurance activities in iterative cycles, aligning assurance tasks with Agile sprints or milestones for faster feedback.

### 4.1.2  Prioritizing High-Value Assurance Activities

Small projects should focus their limited resources on high-value assurance activities that provide the greatest return in terms of risk reduction and safety improvements. The NASA Software Assurance and Safety Initiative recommends the following prioritized practices for small projects:

#### 4.1.2.1  Early Risk Assessment

* **Why It’s Important**: Identifying risks early prevents costly or dangerous development flaws later in the project lifecycle.
* **Best Practices for Small Projects**:
  + Use PAL-provided lightweight risk assessment templates tailored for small projects.
  + Focus on potential risks in interfaces, safety-critical systems, and mission functionality.
  + Track risks using simple tools such as shared spreadsheets or basic issue trackers (e.g., Jira).

#### 4.1.2.2  Lightweight Software Assurance Plan (SAP)

* **Why It’s Important**: A streamlined plan prevents excessive documentation while ensuring relevant assurance goals are set.
* **Best Practices for Small Projects**:
  + Use simplified templates from the Software Assurance Initiative to develop an SAP focused on just the critical assurance activities.
  + Include essential activities like unit testing, peer reviews, and software integration checks.

#### 4.1.2.3  Early and Frequent Peer Code Reviews

* **Why It’s Important**: Peer reviews are highly effective for identifying defects early, especially in resource-constrained projects.
* **Best Practices for Small Projects**:
  + Assign team members to conduct lightweight, focused code reviews using PAL checklists for peer reviews.
  + Incorporate automated static analysis tools (e.g., SonarQube) to support manual code reviews.

#### 4.1.2.4. Verify Software Interfaces

* **Why It’s Important**: Interfaces, especially hardware/software interactions, are common sources of defects in small missions.
* **Best Practices for Small Projects**:
  + Prioritize integration testing for all data, hardware, and system interfaces.
  + Use reusable test cases and simulators provided by the Initiative to reduce development effort.

#### 4.1.2.5  Automated Testing for Efficiency

* **Why It’s Important**: Automation increases efficiency in testing while ensuring robust coverage.
* **Best Practices for Small Projects**:
  + Focus on automating unit and functional tests for critical functionality.
  + Utilize tools recommended by the Software Assurance Initiative, such as PyTest, JUnit, or Selenium.

#### 4.1.2.6  Focused Software Safety Practices

* **Why It’s Important**: Ensuring safety in small projects is vital, especially if software interacts with hardware that is mission-critical.
* **Best Practices for Small Projects**:
  + Conduct a simplified hazard analysis for software (e.g., identifying potential failures in safety-critical processes).
  + Focus safety assurance efforts on preventing high-risk hazards related to actuator controls, flight systems, or life-critical software functions.

#### 4.1.2.7  Secure Software Practices

* **Why It’s Important**: Security vulnerabilities can affect missions, regardless of size.
* **Best Practices for Small Projects**:
  + Implement basic secure coding practices, such as input validation and protection against common exploits (e.g., buffer overflows).
  + Use PAL-provided checklists for lightweight cybersecurity assurance in small projects.

### 4.1.3  Utilizing Software Assurance Tools and Resources

The NASA Software Assurance and Software Safety Initiative provides small projects with tools and services that reduce the overhead of implementing assurance activities. These include:

* **Automated Code Analysis Tools**: Use tools like SonarQube, Coverity, and Cppcheck, which are recommended by the Initiative, to catch common defects without requiring full manual reviews.
* **Shared Test Platforms**: Access testing frameworks and reusable test scripts for integration, regression, and performance testing.
* **Metrics Dashboards**: Use tools to track defect density, test coverage, and assurance progress against defined goals.

### 4.1.4  Training and Support for Small Projects

Small projects often have limited access to a dedicated assurance or safety team. The Software Assurance and Software Safety Initiative can bridge this gap by providing tailored training and support:

* **Training Modules for Small Teams**: Leverage targeted Software Assurance training in the **Safety and Mission Assurance Technical Excellence Program (STEP)**[294](#_tabs-<p></p>), focusing on lightweight practices.
* **Community Webinars**: Attend webinars and virtual workshops facilitated by the Initiative for practical tips on balancing rigorous assurance with small-scale resources.
* **Access to Software Assurance SMEs**: Utilize SMEs to advise on tailoring assurance priorities and resolving unique challenges.

### 4.1.5  Benefits of Following the NASA Software Assurance and Software Safety Initiative

For small projects, this Initiative provides several key advantages:

1. **Efficiency:** Ensures small teams can meet safety and assurance requirements without unnecessary bureaucracy, reducing overhead.
2. **Risk Reduction:** Proactively integrates assurance into the lifecycle, detecting and mitigating critical risks and defects earlier.
3. **Consistency:** Ensures even small-scale projects maintain compliance with **NPR 7150.2** and **NASA-STD-8739.8** standards.
4. **Shared Resources:** Reduces duplication of efforts by offering reusable tools, templates, and lessons learned.
5. **Flexibility:** Allows process tailoring to ensure assurance activities fit within the constraints of small projects.
6. **Workforce Development:** Equips small teams with the knowledge and skills needed to handle software assurance effectively.

## 4.2 Conclusion

By leveraging NASA's Software Assurance and Software Safety Initiative, small projects can achieve compliance and implement robust software assurance and safety practices in a scalable, efficient, and risk-focused manner. The resources, training, tools, and templates provided by the Initiative ensure that small teams can operate with confidence, addressing the critical aspects of software assurance while supporting mission success.

This tailored approach ultimately enables small projects to deliver high-quality software while maintaining safety, reducing risks, and contributing to NASA’s overall mission goals.

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
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-294)

  [OSMA/NSC's SMA Technical Excellence Program (STEP) program.](https://nsc.nasa.gov/professional-development/safety-and-mission-assurance-technical-excellence-program "Click to open in new window")

  The Safety and Mission Assurance (SMA) Technical Excellence Program (STEP) is a career-oriented, professional development roadmap for SMA professionals.
* (SWEREF-352)

  [Software Assurance and Software Safety](https://sma.nasa.gov/sma-disciplines/software-assurance-and-software-safety "Click to open in new window")

  OSMA Web site,
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lessons learned from NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** emphasize the importance of robust software assurance and safety practices. These lessons highlight critical past failures that could have been avoided through improved requirements management, testing discipline, and adherence to software assurance methodologies. They underscore why a centralized initiative for software assurance and safety, led by the NASA Chief, SMA, is vital.

### 6.1.1  Relevant NASA Lessons Learned

#### 1.  Probable Scenario for Mars Polar Lander Mission Loss (1998) [529](#_tabs-<p></p>)

* **Lesson Number:** LLIS-0938
* **Incident Summary:**  
  NASA lost the Mars Polar Lander (MPL) mission in 1998 because hardware operational characteristics were not fully captured in the software requirements. Additionally, software testing did not incorporate proper retest procedures after a test failure. This oversight resulted in mission-critical failure modes that were not detected during spacecraft testing.
  + The software design failed to account for momentary false signals generated by touchdown sensors during leg deployment. These momentary signals were interpreted by the software as valid touchdown events, causing the descent engines to shut down prematurely at an altitude of approximately 40 meters above the Martian surface. The spacecraft fell freely to the surface, resulting in mission loss.
* **Lesson Learned:**
  + **Importance of Requirements Validation:** All known hardware characteristics, particularly operational quirks like transient behavior, must be captured in software requirements. Failure to incorporate key physical properties can lead to catastrophic mission outcomes.
  + **Testing Discipline for Changes:** After a test failure, retesting with updated software must address all known issues comprehensively, including those uncovered during analysis.
  + **Design for Failure Modes:** Anticipate and design for failure modes in software associated with hardware interactions, particularly for mission-critical components.
* **Relevance to the Requirement:**  
  A centralized Software Assurance and Software Safety Initiative ensures that projects address requirements validation comprehensively, focusing on thorough testing and accounting for hardware-software integration risks. Standardized retest procedures can prevent oversight in future missions.

#### 2.  Deficiencies in Mission-Critical Software Development for Mars Climate Orbiter (1999) [521](#_tabs-<p></p>)

* **Lesson Number:** LLIS-0740
* **Incident Summary:**  
  NASA lost the Mars Climate Orbiter (MCO) mission in 1999 due to deficiencies in mission-critical software development and testing processes. Specifically:
  + The "Sm\_forces" program's output files contained engineering units in pounds-force seconds (English units) rather than the specified Newton-seconds (metric units). These erroneous values were delivered to the navigation software and were not caught during requirements walkthroughs, design reviews, or testing procedures.
  + Software management failures included noncompliance with the Software Management and Development Plan (SMDP) and inadequate training for software walkthrough processes. The review board identified several lapses:
    - Key personnel were not consistently present at walkthroughs.
    - The Software Interface Specification (SIS) was not used during reviews.
    - Meeting minutes were not taken, and action items were not published.
  + Communication was lost during Mars orbit insertion (MOI), and the MCO was subsequently destroyed due to incorrect navigation calculations.
* **Lesson Learned:**
  + **Strict Adherence to Process:** All software requirements, specifications, and testing procedures must adhere to documented management plans (e.g., SMDP). Deviations can result in critical errors remaining undetected.
  + **Effective Walkthroughs:** Software walkthrough processes must involve all relevant stakeholders, use complete documentation, and track issues via formal meeting minutes and action items.
  + **Unit Standardization:** Implement robust validation of inputs and outputs to ensure unit consistency, particularly in interfacing software modules.
  + **Training for Assurance Activities:** Proper training in walkthrough processes and requirements validation is essential to avoid gaps in oversight.
* **Relevance to the Requirement:**  
  A centralized Software Assurance and Software Safety Initiative establishes strict compliance practices for process adherence, ensures robust training for assurance personnel, and requires comprehensive validation of mission-critical software interfaces. Standardized walkthrough processes would help prevent simple yet costly errors like unit mismatches.

#### 3.  Software Errors Can Impact Mission Success

* **Case:** Mars Climate Orbiter Mishap
* **Lesson Number:** LLIS-1900
* **Incident Summary:**  
  The Mars Climate Orbiter mission failed in 1999 due to a software integration error, specifically the improper conversion of units between English and metric systems. A critical discrepancy between software developed by mission teams and the actual system requirements went undetected due to insufficient software verification and validation (V&V) practices.
* **Lesson Learned:**
  + Insufficient software V&V can lead to catastrophic mission failures.
  + Rigorous software assurance practices, including independent verification and validation (IV&V), are critical to detecting and resolving issues caused by incomplete or incorrect requirements.
* **Relevance to the Requirement:**  
  This lesson highlights the importance of a unified software assurance initiative, as it would ensure that all projects implement strict V&V processes during software design, testing, and integration.

#### 4.  Addressing Software Safety Risks in Early Design

* **Case:** Space Shuttle Program - Software Defect Management
* **Lesson Number:** LLIS-2220
* **Incident Summary:**  
  During the Space Shuttle program, it was discovered that certain software systems critical to flight control and safety had design vulnerabilities that could have led to unanticipated behavior. While these issues were identified and resolved before launch, the delays and costs associated with late discovery were significant.
* **Lesson Learned:**
  + Early integration of software assurance and safety activities can ensure hazards are identified at more cost-effective stages in the lifecycle.
  + Comprehensive software safety processes not only reduce risks but also minimize cost impacts.
* **Relevance to the Requirement:**  
  This lesson is directly relevant to establishing a Software Assurance and Safety Initiative, ensuring that safety-critical software undergoes early and rigorous safety analyses to prevent later-stage defects that could compromise mission objectives.

#### 5.  Independent Assurance Prevents Oversight

* **Case:** Boeing Starliner OFT-1 Software Issues (2020)
* **Incident Summary:**  
  During the Boeing CST-100 Starliner Orbital Flight Test-1 (OFT-1), multiple software issues arose, including a timer error that led to an incorrect orbital placement and a critical software fault that could have resulted in vehicle loss during maneuvering. These issues were partially mitigated by independent assurance activities, but insufficient oversight left other flaws unaddressed.
* **Lesson Learned:**
  + Independent assurance activities must be persistent across all software lifecycle phases to detect subtle software flaws that internal teams may overlook.
* **Relevance to the Requirement:**  
  A centralized Software Assurance and Safety Initiative ensures that independent software reviews and evaluations are prioritized across all projects, especially for mission-critical systems.

#### 6.  System-Level Testing Prevents Failures

* **Case**: Mars Polar Lander
* **Lesson Number**: LLIS-2145
* **Incident Summary:**  
  Software misinterpreted touchdown sensor inputs as valid landing events, leading to the engines shutting down prematurely during descent. This was attributed to insufficient system-level testing that accounted for known hardware characteristics (e.g., transient signals during leg deployment).
* **Lesson Learned:**
  + Testing must include real-world scenarios to validate system and software behavior under operational conditions.
  + Close alignment between hardware characteristics and software design is critical for preventing failure modes.
* **Relevance to the Requirement:**  
  The Software Assurance and Software Safety Initiative emphasizes system-level testing as a requirement, ensuring proper alignment between hardware and software components.

### 6.1.2  Conclusion

Lessons such as the Mars Polar Lander and Mars Climate Orbiter emphasize the necessity for rigorous software assurance practices, particularly in requirements validation, testing discipline, process adherence, and system-level alignment. The NASA Software Assurance and Software Safety Initiative provides the framework and leadership necessary to standardize these practices across all projects, mitigating the risks that contributed to these historical mission failures. By incorporating the lessons learned, NASA can ensure safer, more reliable software systems for future missions.

## 6.2 Other Lessons Learned

* No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-208 - Advancing Software Assurance and Software Safety Practices**

2.1.2.2 The NASA Chief, SMA shall lead and maintain a NASA Software Assurance and Software Safety Initiative to advance software assurance and software safety practices.

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

The Software Assurance and Software Safety improvements aims to advance software assurance (SA) and software safety practices across NASA by improving policies, procedures, tools, technologies, and workforce expertise. Software Assurance and Software Safety teams are responsible for supporting this initiative by aligning with its goals, integrating Agency-level improvements, and ensuring consistent and effective implementation of SA and software safety practices across all projects and Centers.

This guidance outlines the actions Software Assurance and Software Safety personnel should take in support of this initiative. Also see [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative).

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Collaborate with the NASA Chief, SMA to Support the Initiative

* **Participation in the Initiative**:
  + Actively engage in activities led by the **Chief of Safety and Mission Assurance (SMA)** to improve Agency-wide SA and software safety practices.
  + Share input, lessons learned, and project experiences to help identify gaps and opportunities in current software assurance and safety processes.
* **Contribute Subject Matter Expertise**:
  + Provide ongoing feedback on software assurance and safety trends, challenges, and opportunities from your projects and Center.
  + Suggest improvements to assurance processes based on evolving software development methodologies, such as Agile, DevSecOps, and Model-Based Systems Engineering (MBSE).

#### 7.4.2.2  Promote Consistency and Compliance Across NASA Centers

* **Adopt and Tailor Best Practices**:
  + Work with the SMA initiative team to implement and tailor standardized SA practices and safety strategies that align with **NPR 7150.2** [083](#_tabs-<p></p>), **NASA-STD-8739.8** [278](#_tabs-<p></p>), and other applicable NASA directives.
  + Ensure a consistent approach to software assurance across Centers by coordinating with other SA teams.
* **Monitor Compliance Efforts**:
  + Regularly assess compliance with Agency-level SA and software safety improvements stemming from the initiative.
  + Report deviations or challenges to local Center management and collaborate on corrective actions.

#### 7.4.2.3  Participate in Evolving SA and Safety Standards

* **Engage in Standards Development**:
  + Collaborate with the SMA organization in refining NASA policies and standards related to software assurance and safety, including changes to **NPR 7150.2** and **NASA-STD-8739.8**.
  + Suggest updates to reflect industry best practices, emerging technology trends (e.g., AI/ML techniques), and Lessons Learned from previous NASA missions.
* **Incorporate Standards into Assurance Workflows**:
  + Implement any updated assurance or safety practices into local-level assurance workflows in response to new standards developed by the initiative.

#### 7.4.2.4  Contribute Lessons Learned and Knowledge Sharing

* **Submit Lessons Learned to the Initiative**:
  + Document and share Center-specific Lessons Learned from past projects with the SMA Software Assurance and Software Safety Initiative team.
  + Identify recurring assurance or safety issues (e.g., insufficient testing for safety-critical software) and provide actionable recommendations.
* **Disseminate Initiative Findings and Improvements Locally**:
  + Ensure that your Center’s assurance team and project managers are aware of key improvements or updates from the initiative.
  + Promote training on new assurance processes or tools introduced by the initiative to staff involved in software development, integration, and assurance.

#### 7.4.2.5  Stay Informed About SA and Safety Advancements

* **Engage with Workshops, Trainings, and Demos**:
  + Stay actively involved in webinars, training sessions, and workshops organized under the SMA-led initiative to strengthen knowledge in advanced assurance and safety methods.
  + Provide feedback on tools or methodologies introduced through the initiative to help refine implementation.
* **Identify Center-Specific Improvement Needs**:
  + Collaborate with the initiative team to tailor training programs, tools, or templates to address specific assurance and safety challenges unique to a Center or project.

#### 7.4.2.6  Promote the Adoption of New Tools and Processes

* **Evaluate and Implement Advanced Tools**:
  + Work with the initiative team to evaluate new tools for software assurance and software safety (e.g., automated static analysis, dynamic testing tools, and modeling tools for safety-critical systems).
  + Integrate advanced analysis tools into assurance workflows to improve efficiency in defect detection, test coverage, and risk management.
* **Adopt Advanced Safety Techniques**:
  + Support initiatives that introduce rigorous safety methodologies, such as:
    - Formal software safety analysis techniques (e.g., [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) or [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis)).
    - Enhanced testing techniques for failure injection, boundary conditions, and anomaly identification in safety-critical systems.
    - Safety tracking metrics to identify trends and gaps. (See Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).)

#### 7.4.2.7  Ensure Focus on Scalable SA and Safety Practices

* **Support Tailored Approaches for Projects of All Sizes**:
  + Advocate for scalable assurance and safety solutions that align with project size and complexity, ensuring small projects are not overburdened while maintaining appropriate rigor for large mission-critical efforts.
  + Promote templates and lightweight approaches for smaller projects while retaining high rigor for Class A/B/C safety-critical projects.

#### 7.4.2.8  Contribute to Initiative Metrics and Evaluation

* **Track Implementation Success Locally**:
  + Monitor the adoption and effectiveness of new software assurance and safety practices introduced by the initiative at your Center.
  + Collect and share metrics to demonstrate the impact (e.g., defect detection improvements, risk reduction, or hazard closure rates).
* **Provide Feedback to the Initiative**:
  + Identify and communicate areas where additional improvements or resources are needed to advance software assurance and safety practices further.

### 7.4.3  Key Focus Areas for Software Assurance under the Initiative

1. **Safety-Critical Software Practices**:
   * Enhance focus on processes for hazard analysis, safety testing, and failure management.
2. **Risk Management**:
   * Ensure assurance teams identify and address software risks early in the lifecycle.
   * Support improved metrics for monitoring and mitigating risks to safety-critical systems.
3. **Independent Verification and Validation (IV&V)**:
   * Expand best practices for conducting IV&V of high-risk software systems.
4. **Emerging Software Methodologies**:
   * Tailor assurance and safety practices to work with Agile, DevSecOps, and AI/ML technologies.
5. **Workforce Training and Capability**:
   * Promote broader access to tools and training under the initiative to enhance assurance workforce expertise.

### 7.4.4  Expected Outcomes of Supporting the Initiative

1. **Improved Assurance Practices**:
   * Agency-wide adoption of state-of-the-art assurance and safety methods.
2. **Consistent Software Safety Execution**:
   * Better consistency across Centers in implementing software safety controls and mitigating risks.
3. **Mission Success and Enhanced Reliability**:
   * A reduction in software-related anomalies and improved mission safety and reliability outcomes.
4. **Scalable Processes and Tools**:
   * Practices that adapt to projects of varying size without sacrificing assurance rigor.
5. **Continuous Process Improvement**:
   * A feedback loop that drives further refinements to NASA policies, tools, and practices.

Software Assurance Program Direction

**Modern Space Systems Depend on Reliable Software**

* Software is a cornerstone of today's space systems, making "Software Assurance" essential to mission success. As software reliability and safety become increasingly critical, advancing methods to ensure these qualities is a key focus.

**Vision for Program and Discipline Development:**

* **Streamline Software Assurance Processes:** Develop more efficient, automated methods for ensuring software safety, software quality and IV&V across projects.
* **Improve Reporting Capabilities:** Enhance mechanisms for tracking and communicating risks, issues, and findings.
* **Showcase Value and Impact:** Highlight the importance and measurable benefits of Software Assurance and Software Safety activities in supporting NASA missions.
* **Standardize Tools and Methods:** Provide unified tools, services, and scalable improvements to ensure consistency and excellence in Software Assurance and Software Safety processes.
* **Data-Driven Enhancements:** Use analytics and metrics to refine and enhance all aspects of Software Assurance and Software Safety operations.
* **Proactively Address Software Risks:** Focus research and resources on resolving known software issues and advancing assurance strategies aligned with specific challenges.
* **Bolster Training and Standards:** Strengthen workforce skills and refine software safety requirements through NASA’s Software assurance and Software Safety Program and broader agency initiatives.

By pursuing these focused objectives, NASA aims to elevate software safety and assurance to meet the demands of increasingly complex space systems

### 7.4.5  Conclusion

The **NASA Software Assurance and Software Safety improvement process** provides a pivotal opportunity to continuously improve the effectiveness of software assurance and safety practices across the Agency. Software Assurance personnel must actively engage in supporting the initiative by contributing expertise, lessons learned, and innovative strategies while promoting the adoption of standardized, scalable, and effective approaches Agency-wide. This collaboration ensures that both software assurance and safety practices evolve to meet the demands of emerging technology and complex mission requirements.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)        * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |
