# 7.12 – Software Technology Readiness Levels STRLs and Milestone Review Alignment

> NASA Software Engineering Handbook (SWEHB Ver D), page id 240222216. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/240222216/7.12+%E2%80%93+Software+Technology+Readiness+Levels+STRLs+and+Milestone+Review+Alignment

7.12 – Software Technology Readiness Levels (STRLs) and Milestone Review Alignment

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/240222216/7.12+%E2%80%93+Software+Technology+Readiness+Levels+STRLs+and+Milestone+Review+Alignment#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=240222216)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=240222216&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Scope](#tabs-2)
* [3. Background](#tabs-3)
* [4. Rationale for Integrating STRLs into Reviews](#tabs-4)
* [5. TRL <-> Milestone Review Mapping](#tabs-5)

# 1. Purpose

This topic defines how Software Technology Readiness Levels (STRLs) are used as part of Entrance and Exit Criteria (EEC) across NASA software and system milestone reviews. STRLs provide a maturity-based assessment that complements artifact-based evaluations, enabling better-informed technical and risk decisions.

# 2. Scope

* All NASA programs using software that implements new, modified, or reused technologies.
* Human-rated and non-human-rated systems.
* Heritage, COTS/MOTS/GOTS, research, and newly developed components.
* All major milestone reviews (MCR, SRR, SwRR, PDR, CDR, SIR, TRR, ORR, FRR).

# 3. Background

### 3.1 Software TRLs

* Define maturity levels from TRL 1 (concept) to TRL 9 (flight-proven).
* Evaluate documentation, logic stability, prototype demonstrations, and test fidelity.
* Support maturity-based readiness assessments.
* NASA NPR 7123.1 NASA Systems Engineering Processes and Requirementsdefines the TRLs at an agency level.

### 3.2 System Technology Readiness Alignment

* Provides correlation between software maturity and system-level TRAs.
* Supports continuous maturity assessment and risk reduction.
* Informs technology transition planning for low-TRL items.

# 4. Rationale for Integrating STRLs into Reviews

Although STRLs provide useful structure, traditional TRL concepts have known limitations when applied to software. Software maturity is heavily influenced by the hardware and system context in which it executes, meaning that the same code may demonstrate different levels of readiness depending on processor architecture, memory layout, timing behavior, or I/O interactions. Additionally, even small changes in software can have cascading effects across an entire code base, effectively resetting maturity in ways not seen in hardware. Frameworks and reusable infrastructures also present challenges because they often evolve non-linearly, making it difficult to assign a single maturity level. Finally, software flown in space may not have executed all paths or functions, leaving unexercised logic that prevents full confidence in TRL 9 readiness.

* Artifact completeness alone does not ensure technical maturity.
* STRLs provide objective evidence of feasibility and readiness.
* Early identification of immature software reduces downstream risk.
* Supports consistent decision-making across programs.

Integrating TRLs with milestone reviews has advantages but does not represent a complete solution, the software itself may be matured through multiple projects that have their own milestone reviews.  These alternate milestone reviews increase the TRL for that instantiation of the software and system.

The distinction between the algorithm (the mathematical equations and/or logic) and the software code (including implementation) must be made.  The algorithm may have been used before but the implementation of that into the software can be different.

# 5. TRL ↔ Milestone Review Mapping

The TRLs presented below are based on a new development of software in a complete project.  If software is being reused, it is possible that the software TRL is higher or lower depending on the scenario and the key inputs presented below.

Key inputs to be considered:

* Configuration files
* Tool chains
* Inputs into the software
  + Sensors, Simulations, and similar
* Platform Hardware/software
  + Processor, RAM, Operating System, Endian
* Algorithm assumptions/limitations

| TRL | Software Description | Exit Criteria | Verification | Documentation Need to Advance |
| --- | --- | --- | --- | --- |
| TRL 1 — Proposal Stage Aligned Review: MCR (PAT‑066) | Initial concept defined with mission contribution. Technical feasibility logically supported. High-level functionality and constraints documented. | Mission objectives and software role documented. Preliminary requirements & risks identified. Applicable standards identified. Initial V&V concept established. Stakeholder alignment achieved. | Feasibility analyses and conceptual modeling. Peer-reviewed technical basis. Traceability to mission concept. | Mission Concept documentation. High-level requirements & risks. Standards list & initial V&V concept. Early scientific/algorithmic evidence. |
| TRL 2 — Study Stage Aligned Review: SRR (PAT‑067) | Preliminary software requirements defined. Interfaces and constraints identified. Prototype analyses performed. | Requirements complete, feasible & traceable. Safety & cybersecurity requirements captured. Interfaces baselined. Preliminary V&V plan established. Stakeholder approval obtained. | Requirements reviews & traceability. Safety/cyber PHA & hazard mapping. Standards mapping to NPR 7150.2 & 8739.8. | Preliminary SRS. ICDs & interface definitions. Prelim V&V plan. Safety/cyber hazard analysis. |
| TRL 3 — Software Unit Feasibility Aligned Review: SwRR (PAT‑068) | Requirements validated and baselined. Early algorithm prototyping completed. Interfaces confirmed. | All requirements testable and complete. Acceptance criteria defined. Hazard-controls traceability complete. Baseline approved. Volatility thresholds met. | Requirements peer reviews. Hazard/controls verification mapping. SA & IV&V requirement analyses. | Baselined SRS & ICDs. Verification Plan. Hazard traceability. Compliance matrices. |
| TRL 4 — Software Component Feasibility Aligned Review: PDR (PAT‑071) | Components integrated in laboratory environment. Architecture defined with preliminary design. Interfaces understood and documented. | Baselined SRS supports design. Preliminary design features complete. Architecture & data dictionary defined. Hazard traceability updated. Trade studies completed. | Preliminary design analyses. Architecture/interface consistency checks. SA/IV&V design reviews. | Prelim design documentation. CM plan & schedule. Test plans. Design analysis outputs. |
| TRL 5 — Software Architecture Feasibility Aligned Review: CDR (PAT‑072) | End-to-end architecture maturity demonstrated. Design artifacts complete. Interfaces consistent. | Reqts-to-design traceability complete. Design supports safety & functional needs. Verification plan across levels. Interface definitions finalized. Risks & mitigations dispositioned. | CDR design assessments. Safety/IV&V analyses. Interface validation reviews. | Final design documentation. Risk/hazard analyses. Regression test plans. Coverage/testability evidence. |
| TRL 6 — Software Engineering Feasibility Aligned Review: SIR (PAT‑074) | Software integrated with HW/SW systems. Interfaces validated during integration. Operational modes tested. | Integration complete & stable. Interfaces mature. Issues dispositioned. Staffing/resources confirmed. System test readiness demonstrated. | Integration test execution. Interface verification. Config/load data review. | Integration procedures. ICD maturity evidence. Issue logs. System test planning artifacts. |
| TRL 7 — Software Operational Feasibility Aligned Review: TRR (PAT‑075) | All key functionality ready for formal test. Test environments & scripts approved. Regression approach defined. | Test plans & procedures approved. Acceptance criteria reviewed. Test environment validated. Interface risks dispositioned. Sim/stimulation qualified. | Test readiness package review. Procedure execution dry-runs. Discrepancy tracking. | Approved test plans/cases. Configuration records. V&V/regression artifacts. Risk tracking data. |
| TRL 8 — Hardware/Software Functionality Aligned Review: ORR (PAT‑077) | V&V complete. Operational scenarios demonstrated. Documentation & training complete. | Acceptance tests passed. Operational procedures validated. All waivers/TBD/TBR closed. Coverage criteria met. Security/config data verified. | Operational scenario execution. Coverage analyses. Hazard verification. | Final V&V reports. Ops/training procedures. Configuration evidence. Coverage/hazard records. |
| TRL 9 — System Operational Environment Functionality Aligned Review: FRR (PAT‑078) | Software operated on flight hardware. Mission readiness established. Sustaining engineering in place. | All requirements verified & validated. Flight procedures approved. Waivers/deviations closed. Safety/reliability margins acceptable. Operational risks acceptable. | FRR package review. Mission-specific scenario verification. Final HW/SW integration validation. | Flight documentation. Hazard verification. Test/coverage reports. Sustainment plans. |
