# ADR-001: Class A software rigor, Criticality-1 system rigor and the five-gate review structure

| Field | Value |
|---|---|
| ID | ADR-001 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 2 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2: a process convention, the rigor election and the gate structure; it changes no hazard cause or control). Decision authority stays Robin because the decision fixes baseline content |
| Decision authority | Robin (owner; the decision sets the engineering process for every baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-05 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

A hobby transceiver built by one person falls, by the letter of NPR 7150.2D App. D, in Class D for its safety-critical firmware and Class E for its engineering tools (`docs/process/03-software-classification-and-rmm.md` section 3.1). The owner nevertheless directed that the project be run at the rigor of Class A software ("Human Rated Space Software Systems", NPR 7150.2D App. D) and a Criticality-1 system for requirements, traceability, V&V, configuration management and reviews, with the review gates SRR, PDR, CDR (procurement release), TRR and an acceptance review, and with owner dispositions through RFAs and RIDs. The owner also approved an expedited schedule: SRR Saturday morning, PDR Saturday evening, CDR Sunday evening with procurement release Sunday night, liens on PDR products acceptable when CDR closes them, and three owner review windows. Without this decision no process document could name its governing rigor, and tailoring rows could be relaxed silently.

- Driving inputs and expectations: SI-015, SI-020, SI-010 (must work at first power-on), SI-011 (owner reviews, Claude produces)
- Requirements that constrain the decision: none (this decision precedes the requirement set)
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-001 to HZ-015. The election binds the SWE-134 provisions to the firmware roles of HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012 and HZ-014 (`docs/safety/hazard-analysis.md` section 6.2; the election is what makes the safety-critical determination bind at Class A)
- Research consulted: `docs/research/verification-tooling-inventory.md` F18 (MC/DC instrumentation removed from rustc, which the election must absorb); `docs/research/rustos-toolchain-proof.md` F1 to F6 (the toolchain can support the rigor)
- Guidance consulted: NPR 7150.2D App. D (class definitions), SWE-020, SWE-139, SWE-125, SWE-176; NPR 7123.1D §5.1.5 (event-based reviews), App. G Tables G-4, G-6, G-7, G-10, G-11, SE-33, SE-39; SE HB App. C; SE HB §6.8 and Table 6.8-1 (decision reporting, which this ADR series implements)
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The toolchain gives Class A evidence except MC/DC instrumentation (RSK-010). Confirmed by the toolchain proof, SRR package item H12, before the SRR readiness declaration.
  2. Independent agent review stands in for IV&V. Confirmed by the owner's approval of the RMM tailoring rows in the SRR decision memo.
  3. The weekend dates are targets. Reassessed at each gate's readiness declaration.

## 2. Decision

The project applies the full Class A column of NPR 7150.2D App. C Table 2 (100 SWE rows) to `cwht-fw` and its test tooling, and Criticality-1 rigor to requirements, bidirectional traceability, V&V, CM and reviews, while recording honestly that App. D by the letter would give Class D and E. The life cycle is the condensed NPR 7120.5 cycle with five event-based control gates: SRR (absorbing MCR), PDR (absorbing SDR/MDR), CDR (procurement release), TRR (absorbing SIR) and SAR (absorbing ORR). The owner chairs every review and dispositions Approved, Approved with liens, or Not approved, raising RFA-<REVIEW>-NNN and RID-<REVIEW>-NNN. The expedited target schedule (SRR Sat 2026-09-26 morning, PDR Sat evening, CDR Sun 2026-09-27 evening, procurement release Sun night) is a target, not a trigger: a gate is convened only when its Hard entrance criteria are met. Relief from any Class A row is tailoring recorded row-by-row in `docs/process/rmm.json` with owner approval; customization (combined reviews, consolidated documents) is recorded in the SEMP and needs no waiver.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Elect Class A applicability and Criticality-1 rigor; five gates; expedited schedule with liens permitted at PDR | Owner direction (SI-015, SI-020); gives the strongest evidence for SI-010 (first power-on success) and makes every relief visible as a tailoring row |
| B | Class D by the letter of App. D (64 rows) with Class E tools | Rejected by the owner; would drop architecture and design records (SWE-057, SWE-058), peer reviews (SWE-087 to SWE-089), coverage and regression (SWE-190, SWE-191) and nonconformance handling (SWE-202 to SWE-204) that the owner wants |
| C | Class B or C as an intermediate | Rejected: no Class A row is invoked for Class A alone (every Class A row is also a Class B row, 03 section 3.2), so Class B would buy nothing over A; Class C would drop rows the owner wants |
| D | No NASA framework; informal hobby process | Rejected by SI-015 |

No trade study: the owner's direction eliminated every option but A (SE HB §6.8.1.2.2 permits documenting a decision with one viable alternative).

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none directly | | The election constrains how every requirement is written (SE HB App. C rules of `docs/process/02-requirements-and-traceability.md` section 4.2), validated (six steps of SE HB §4.2.1.2.4) and traced (Class A set of NPR 7150.2D §3.12.1 Table 1); it creates no requirement of its own |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: none; the software architecture and design records (SWE-057, SWE-058) become mandatory products at PDR and CDR
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: none directly; every requirement must carry a verification method at definition and at least one `TC-<MOD>-NNN` (charter section 7)
- Evidence class implications: the six classes of `docs/process/04-verification-and-validation.md` section 4 (Simulation, HostUnit, Emulation, Inspection, Bench, OnAir) exist because Class A demands credited, repeatable evidence; tools need accreditation (SWE-136) before their output counts
- Hazard analysis update required: yes; the safety-critical determination (SWE-205) and SWE-134 provisions a to l apply to keying, PA enable, charging supervision, thermal protection, audio output limiting and the shared safe-state manager, and to mission-critical frequency control and configuration load (charter section 10; the authoritative list is 07 section 14.1)
- Safety-critical software scope changed: yes (established: 03 section 4.3)

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact: none in parts; the cost is review and evidence effort, absorbed by agent invocations
- Gate affected: all five gates defined by this decision; the expedited dates are targets keyed to the vendor lead time of 2 to 4 weeks (`docs/plan/schedule.md`)
- Risks opened, closed or re-scored: RSK-009 (SWEHB corpus incomplete for reviewer checklists) and RSK-010 (MC/DC cannot be measured for Rust) exist because of this election; both stay open
- TPMs affected: TPM-003 (review trend, RFA and RID burndown) is created by this decision; TPM-012 (requirements volatility, SWE-200)

## 5. Compliance and tailoring

Touches every row of `docs/process/rmm.json` (meta `software_class_elected` = "A", `software_class_app_d_assessment` = "D ...; E ...") and every row of `docs/process/se-compliance-matrix.json`. Current disposition summary: 74 FC, 16 T, 10 NA of 100 rows (`docs/process/rmm.md`). The proposed tailoring rows are approved in the SRR decision memo (01 section 3.2 row S6); no CR yet because no baseline exists. A later change of class is a `CR-NNN` with owner approval, an update of the classification record and plan updates per SWE-021 (03 section 3.2 item 3).

## 6. Decision record

> Owner (2026-09-25, SI-015): "Process: NASA SE Handbook + NPR 7150.2D at Class A / Crit-1 rigor; gates SRR, PDR, CDR (procurement release), V&V plan/TRR, acceptance review; owner dispositions with RFAs/RIDs."

> Owner (2026-09-25, SI-020): "Owner approved the expedited schedule and plan: SRR Sat morning, PDR Sat evening, CDR Sun evening with procurement release Sunday night; liens on PDR products acceptable when CDR closes them; three owner review windows accepted."

Both statements were given in chat and transcribed into `docs/requirements/l0-stakeholder/stakeholder-inputs.md` (charter section 2: an approval in chat is transcribed into the memo).

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR (entrance product; the classification record 03 and the RMM are reviewed alongside)
- Revisit conditions: the owner asks for a different class (CR); a Class A row proves unachievable with available tooling (then a tailoring row, as RSK-010 already forces for SWE-219, not a class change)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: F-05 (erratum E-3, the RMM disposition counts of section 5). The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
