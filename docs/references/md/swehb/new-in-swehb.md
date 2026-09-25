# New in SWEHB

> NASA Software Engineering Handbook (SWEHB Ver D), page id 122388792. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/122388792/New+in+SWEHB

This BLOG is available from the Introduction page of the SWEHB as well as on all of the other major pages (pages in the button bar) in the SWEHB.

**SWEHB Blog Full History - Most Recent First**

[New Topic - Verification and Assurance Guidelines for Multicore, Concurrent, and Partitioned Software Systems](/spaces/SWEHBVD/blog/2026/06/04/248774669/New+Topic+-+Verification+and+Assurance+Guidelines+for+Multicore+Concurrent+and+Partitioned+Software+Systems)

[Guillermo Del Carmen](    /display/~gdelcarm
) posted on Jun 04, 2026

7.26 - Verification and Assurance Guidelines for Multicore, Concurrent, and Partitioned Software Systems

* [swehb](/label/SWEHBVD/swehb)

[Added Software Lessons Learned from Psyche Project Report](/spaces/SWEHBVD/blog/2026/05/20/245825629/Added+Software+Lessons+Learned+from+Psyche+Project+Report)

[Tim Crumbley](    /display/~rcrumble
) posted on May 20, 2026

Click here for more details ...

## **Lessons Laerned from Psyche Project Report**

## **1. Late and Incomplete Flight Software (FSW) Delivery**

**Incident:**  
The Psyche mission experienced an eight‑month late delivery of the final GNC flight software build, with hundreds of control parameters and fault protection behaviors still undefined. This delay, combined with numerous unresolved software issues, contributed directly to the missed 2022 launch opportunity.

**Lesson Learned:**

* **Early Software Definition & Maturity:** Mission‑critical software requirements, parameters, and behaviors must be fully defined and matured early to prevent cascading delays.
* **Rigorous Defect Disposition:** “Use‑as‑is” and unverified failure dispositions must undergo strict technical review to prevent acceptance of excessive residual risk.

**Implication:**  
Delays and ambiguity in software maturity directly threaten launch schedules, increasing cost, workforce strain, and mission‑risk exposure.

---

## **2. Incomplete Verification & Validation (V&V)**

**Incident:**  
The project faced major V&V shortfalls, including approximately 1,000 unverified system requirements and incomplete GNC, fault protection, and FSW test coverage. Immature and incompatible testbeds further hindered simulation and closed‑loop testing.

**Lesson Learned:**

* **Comprehensive V&V Execution:** V&V must be resourced, scheduled, and monitored with the same rigor as hardware development.
* **Validated Testbeds:** Testbeds and simulations must be synchronized early with vendor tools to ensure accurate system‑level testing.

**Implication:**  
Insufficient V&V undermines mission confidence and may conceal system defects until it is too late to correct them within the launch window.

---

## **3. Undefined and Insufficiently Tested Fault Protection**

**Incident:**  
Fault protection logic was not fully defined or validated prior to the launch delay, leaving mission‑critical behaviors unverified. citeturn1search1.page21

**Lesson Learned:**

* **Early Fault Management Definition:** Fault detection, isolation, and recovery logic must be fully specified and integrated into system testing well before ATLO.
* **Hazard‑Driven Validation:** Fault responses must be validated against hazards and off‑nominal scenarios using high‑fidelity simulations.

**Implication:**  
Incomplete fault protection risks spacecraft safety, autonomy, and ability to recover from anomalies during critical mission phases.

---

## **4. Immature Testbeds and Simulation Environments**

**Incident:**  
Major incompatibilities between JPL and Maxar testbeds delayed verification activities and prevented execution of essential closed‑loop GNC testing. Early assumptions about vendor simulation capabilities proved incorrect.

**Lesson Learned:**

* **Interface Verification:** Simulation environments must be verified early with contractual clarity on capabilities, interfaces, and data integration.
* **End‑to‑End Fidelity:** High‑fidelity closed‑loop simulation must be operational well before system‑level V&V.

**Implication:**  
Faulty assumptions about vendor simulation capacity or testbed interoperability can cripple software testing and threaten mission readiness.

---

## **5. Poor Metrics and Lack of Visibility into Software Health**

**Incident:**  
Psyche’s project metrics masked true software progress. Software risk was consistently under‑reported due to an aversion to categorizing issues as “red,” preventing leadership from recognizing schedule‑threatening problems.

**Lesson Learned:**

* **Objective Software Metrics:** Software maturity must be tracked using measurable indicators such as defect trends, verification progress, and test coverage.
* **Risk Transparency:** Leadership must encourage open reporting and avoid cultural pressures that suppress accurate risk assessments.

**Implication:**  
When metrics fail to reflect reality, management loses the ability to make timely decisions, creating preventable launch‑critical failures.

---

## **6. Insufficient Staffing in Software, GNC, and Systems Engineering**

**Incident:**  
Psyche suffered from persistent understaffing in key areas such as flight software, GNC, systems engineering, and V&V. Many roles were filled with inexperienced personnel, with excessive reliance on stretch assignments and limited mentoring.

**Lesson Learned:**

* **Adequate Expertise:** Complex missions require experienced staff in critical roles (e.g., Project Chief Engineer, GNC CogE, Fault Protection Lead).
* **Sustainable Staffing Models:** Workforce planning must account for burnout, skill mix, mentoring, and retention of highly specialized talent.

**Implication:**  
Understaffing reduces software quality, increases risk of technical debt, delays development, and undermines mission execution.

---

## **7. Communication Failures Suppressing Software Concerns**

**Incident:**  
Software and system engineers raised concerns that were not acted upon. The culture fostered a “prove there is a problem” mentality, making it difficult to elevate software risks. No Independent Technical Authority (ITA) dissents were filed despite significant issues.

**Lesson Learned:**

* **Open Technical Channels:** Projects must maintain safe, responsive pathways for raising technical concerns, including through independent authorities.
* **Cultural Reinforcement:** Leadership must encourage early reporting and prohibit cultures that penalize raising risks.

**Implication:**  
When team members feel unheard, systemic issues go unaddressed, increasing mission risk and slowing problem resolution.

---

## **8. Misalignment with Commercial Vendor (Maxar) Software Capabilities**

**Incident:**  
Misaligned expectations for Maxar’s simulation, interface details, and heritage design significantly delayed testing and integration activities. COVID‑related limitations reduced the required face‑to‑face interaction needed to align on software behaviors.

**Lesson Learned:**

* **Deep Early Integration:** NASA personnel must work side‑by‑side with commercial partners early to align on simulation capabilities, interface assumptions, and development processes.
* **Contractual Clarity:** Software deliverables and testbed capabilities must be unambiguously specified in contracts.

**Implication:**  
Weak alignment with vendor software ecosystems causes delays, rework, and verification gaps that can push missions off launch schedules.

* [swehb](/label/SWEHBVD/swehb)

[Updated the software milestone review criteria and added AI criteria](/spaces/SWEHBVD/blog/2026/05/19/245825574/Updated+the+software+milestone+review+criteria+and+added+AI+criteria)

[Tim Crumbley](    /display/~rcrumble
) posted on May 19, 2026

Click here for more details ...

We updated the software milestone review criteria to strengthen alignment with current engineering best practices and project needs. As part of this revision, we introduced new AI‑focused evaluation criteria to ensure teams are appropriately addressing model reliability, validation and verification, data integrity, risk assessment, and responsible use considerations throughout the development lifecycle.

* [swehb](/label/SWEHBVD/swehb)

[Added Lessons Learned from Starliner CFT and the Lunar Trailblazer mission report](/spaces/SWEHBVD/blog/2026/03/17/235995197/Added+Lessons+Learned+from+Starliner+CFT+and+the+Lunar+Trailblazer+mission+report)

[Tim Crumbley](    /display/~rcrumble
) posted on Mar 17, 2026

* [swehb](/label/SWEHBVD/swehb)

[Added Objective Evidence for Each Requirement](/spaces/SWEHBVD/blog/2025/12/03/223150083/Added+Objective+Evidence+for+Each+Requirement)

[Tim Crumbley](    /display/~rcrumble
) posted on Dec 03, 2025

Added Objective Evidence for Each Requirement

Click here for more details ...

Objective evidence plays a crucial role in ensuring accountability, traceability, and reliability across software assurance and safety activities. It provides documented, unbiased proof that a specific activity has been performed or confirmed by the responsible software assurance/safety personnel — and it’s not just about checking a box. It amplifies the credibility of your processes.

Documenting objective evidence can take multiple forms depending on the activity being verified. Some examples include:

* **Audit Records and Checklist Results**: Observations, findings, or risks identified, documented in a tracking system, or captured in emails.
* **Meeting Records**: Attendance lists, meeting minutes, or notes stored in the project repository.
* **Status Updates**: Memos, emails, or reports confirming an activity took place, supported by summaries or confirmation checklists.
* **Reviewed/Witnessed Activities**: Signatures on reviewed products or processes to validate completion or compliance.
* **Short Summaries**: Concise statements that provide insight into specific activities or milestones, such as:
  + Progress on IV&V Program Execution.
  + Percentage of hazards traced to software requirements.

When implemented consistently, objective evidence strengthens your project’s integrity, enhances collaboration, and aligns with the guidelines set forth in Section 8.16 of the handbook. Not only does it enable teams to track progress effectively, but it also instills confidence in the accuracy of assurance efforts.

The bottom line? Every requirement deserves solid, verifiable evidence. By prioritizing documentation, you’re not just managing activities — you’re building trust across the project.

* [swehb](/label/SWEHBVD/swehb)

[Updated Topic 5.09 - SRS - Software Requirements Specification and PAT-059](/spaces/SWEHBVD/blog/2025/10/15/215777815/Updated+Topic+5.09+-+SRS+-+Software+Requirements+Specification+and+PAT-059)

[CATHRYN SIMPSON](    /display/~csimpso3
) posted on Oct 15, 2025

[5.09 - SRS - Software Requirements Specification](https://swehb.nasa.gov/display/SWEHBVD/5.09+-+SRS+-+Software+Requirements+Specification) guidance was rewritten with assistance from AI and [PAT-059](/spaces/SITE/pages/198770890/PAT-059+-+Software+Requirements+Specification+Assessment) updated.

Click here for more details ...

Guidance for the Minimum Recommended Content of the Software Requirements Specification was rewritten and expanded using AI content. This rewrite includes expanded guidance, examples, and new guidance for Software Assurance. [PAT-059 - Software Requirements Specification Assessment](https://swehb.nasa.gov/display/SITE/PAT-059+-+Software+Requirements+Specification+Assessment) was updated to coincide with this new guidance.

* [swehb](/label/SWEHBVD/swehb)

[Updated Topic 5.10 - STP - Software Test Plan](/spaces/SWEHBVD/blog/2025/10/09/215777789/Updated+Topic+5.10+-+STP+-+Software+Test+Plan)

[CATHRYN SIMPSON](    /display/~csimpso3
) posted on Oct 09, 2025

[5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) guidance has been totally rewritten using AI.

Click here for more details ...

Guidance for the Minimum Recommended Content of the Software Test Plan was rewritten and expanded using AI content. Due to the breadth of information and examples added, this enhanced guidance has been spread across multiple tabs.

* [swehb](/label/SWEHBVD/swehb)

[New Topic 7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/blog/2024/06/24/167804933/New+Topic+7.23+-+Software+Fault+Prevention+and+Tolerance)

[Haigh, Fred](    /display/~fhaigh
) posted on Jun 24, 2024

Topic 7.23 has been added and is now available for use.

Click here to expand...

Topic 7.23 - Software Fault Prevention and Tolerance This topic guides developers to reduce the likelihood of software faults pre-flight and to detect/mitigate the effects of software errors should they occur in-flight.

* [swehb](/label/SWEHBVD/swehb)

[New Topic on PLD Development and Software Assurance](/spaces/SWEHBVD/blog/2025/08/14/209846334/New+Topic+on+PLD+Development+and+Software+Assurance)

[Haigh, Fred](    /display/~fhaigh
) posted on Aug 14, 2025

A new Topic [8.30 - Flight and Ground PLD Development](/spaces/SWEHBVD/pages/209846294/8.30+-+Flight+and+Ground+PLD+Development) is now available.

Click here to expand...

PLDs, especially FPGAs, are becoming increasingly critical in complex avionics and space systems. Establishing a standardized and scalable approach to their development and assurance will not only improve consistency across NASA projects but also enhance mission safety and reliability. By emphasizing early planning, hazard management, training, cross-center collaboration, and consistent application of best practices, NASA can address current limitations while building a foundation for future advancements.

* [swehb](/label/SWEHBVD/swehb)

[New Topic 8.29 - Software Certification in Human-Rated Missions](/spaces/SWEHBVD/blog/2025/08/04/207290833/New+Topic+8.29+-+Software+Certification+in+Human-Rated+Missions)

[Haigh, Fred](    /display/~fhaigh
) posted on Aug 04, 2025

This Topic provides comprehensive data and evidence required to certify software for human-rated missions. 

Click here to expand...

It includes a checklist, a list of Compliance Data Needs and a Safety Case with guidance. It ensures compliance with applicable safety standards, regulatory requirements (NASA NPR 7150.2D, SSP 50038, FAA, NASA-STD-8739.8B), mission-critical functionality, and stakeholder acceptance of residual risks, demonstrating that the software is safe, reliable, and mission-ready for crewed spaceflight operations.

* [swehb](/label/SWEHBVD/swehb)

[New Topic 8.28 - Preparing and Evaluating Commercial Services Contracts](/spaces/SWEHBVD/blog/2025/08/01/207290731/New+Topic+8.28+-+Preparing+and+Evaluating+Commercial+Services+Contracts)

[Haigh, Fred](    /display/~fhaigh
) posted on Aug 01, 2025

[8.28 - Preparing and Evaluating Commercial Services Contracts](/spaces/SWEHBVD/pages/207290446/8.28+-+Preparing+and+Evaluating+Commercial+Services+Contracts)  - Guidance for a well-structured commercial services contract for the development, delivery, and certification of aerospace software systems.

Click here to expand...

Contracts must align with safety, reliability, regulatory, and operational readiness requirements to ensure that the software meets the stringent demands of FAA regulations, NASA standards, space system requirements, cybersecurity expectations, and military-grade fault-tolerance protocols.

* [swehb](/label/SWEHBVD/swehb)

[Updated Topic 7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/blog/2025/07/25/207290544/Updated+Topic+7.09+-+Entrance+and+Exit+Criteria)

[Haigh, Fred](    /display/~fhaigh
) posted on Jul 25, 2025

[7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) has been totally redesigned and now implements Process Asset Template Checklists for Reviews.

Click here for more details ...

Each Review Checklist is contained in a PAT (MS Word Document) which may be downloaded and used in your project. Each of the 13 PATs has a table which may be used:

* to prepare for the review - listing all the documents and expectations that will be covered in the review,
* in the review - the criteria for successful completion are listed as well as an area to note (Y/N) if the criteria is met, and a Comments cell in the table to record any discussion about the item.

* [swehb](/label/SWEHBVD/swehb)

[New Topic on SWE and SA Checklists](/spaces/SWEHBVD/blog/2025/07/09/205029621/New+Topic+on+SWE+and+SA+Checklists)

[CATHRYN SIMPSON](    /display/~csimpso3
) posted on Jul 09, 2025

[8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) is a new topic and is now available for use. Find it under **D. Topics** → **8.xx Assurance and Safety Topics**.

Click here for more details ...

[8.27 - Software Engineering and Software Assurance Checklists](/spaces/SWEHBVD/pages/204079325/8.27+-+Software+Engineering+and+Software+Assurance+Checklists) - Checklists provide a mechanism to independently evaluate the conformance of software products and processes to applicable requirements, standards, guidelines, plans, and procedures.

* [swehb](/label/SWEHBVD/swehb)

[Rewrite of Topic 8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/blog/2025/06/24/203391048/Rewrite+of+Topic+8.10+-+Facility+Software+with+Safety+Considerations)

[CATHRYN SIMPSON](    /display/~csimpso3
) posted on Jun 24, 2025

[8.10 - Facility Software with Safety Considerations](https://swehb.nasa.gov/display/SWEHBVD/8.10+-+Facility+Software+with+Safety+Considerations) was re-written and is now available for use.

Click here for more details ...

[8.10 - Facility Software with Safety Considerations](https://swehb.nasa.gov/display/SWEHBVD/8.10+-+Facility+Software+with+Safety+Considerations) - Facility software safety exists to ensure the safe and continuous operation of software associated with ground-based facilities. This topic provides guidance on the Facility Life Cycle, document maturity schedules, milestone entry/exit criteria, and SW Engineering and SA responsibilities.

* [swehb](/label/SWEHBVD/swehb)

[Audit and Assessment Checklists and Schedules for Topics 8.12 and 8.59](/spaces/SWEHBVD/blog/2025/06/24/203391050/Audit+and+Assessment+Checklists+and+Schedules+for+Topics+8.12+and+8.59)

[CATHRYN SIMPSON](    /display/~csimpso3
) posted on Jun 24, 2025

Audit and Assessment Checklists and Schedules were added to Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) and Topic [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports).

Click here for more details ...

Software Assurance is required to perform audits and assessments. Thirty (30) new Process Asset Templates (PATs) (i.e., compliance audit and work product assessment checklists) were created for SA personnel use while performing these activities. Schedules were also created with guidance on when to perform these audits and assessments.

* [swehb](/label/SWEHBVD/swehb)
