---
id: CR-008
title: Fix the SRR peer review liens of the L1 requirements and the TC-SYS cases
status: Submitted
class: I
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); HEAD ab2af2d on main
baseline_affected: baseline/srr
affected_cis: [7, 11, 15, 17]
affected_paths: [docs/requirements/sys/requirements.json, docs/requirements/sys/requirements.md, docs/test_cases/sys/test_cases.json, docs/test_cases/sys/test_cases.md, docs/safety/hazards.json, docs/safety/hazard-analysis.md, docs/design/allocation.json]
affected_ids: [REQ-SYS-014, REQ-SYS-044, REQ-SYS-045, REQ-SYS-054, REQ-SYS-077, REQ-SYS-083, REQ-SYS-087, REQ-SYS-088, REQ-SYS-093, REQ-SYS-161, REQ-SYS-166, REQ-SYS-167, REQ-SYS-185, REQ-SYS-186, REQ-SYS-194, TC-SYS-003, TC-SYS-008, TC-SYS-013, TC-SYS-030, TC-SYS-031, TC-SYS-034, TC-SYS-036, TC-SYS-038, TC-SYS-047, TC-SYS-050, TC-SYS-056, TC-SYS-060, TC-SYS-061, TC-SYS-064, TC-SYS-065, TC-SYS-066, TC-SYS-073, TC-SYS-082, TC-SYS-083, TC-SYS-101, TC-SYS-102, TC-SYS-105, TC-SYS-108, TC-SYS-109, TC-SYS-110, TC-SYS-111, TC-SYS-112, TC-SYS-113, TC-SYS-116, HZ-002, RSK-007]
related: [INSP-003, INSP-025, RFA-SRR-006, RFA-SRR-007, RID-SRR-003, CR-002, CR-003, CR-006, CR-009, WP-PDR-11]
target_release: none
branch: cr/CR-008-srr-liens-l1-and-tc-sys
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-008: Fix the SRR peer review liens of the L1 requirements and the TC-SYS cases

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3 and `docs/process/02-requirements-and-traceability.md` §10.2 and §10.3. File location: this file, committed on `main` with `Refs: CR-008`. The product changes are prototyped on the branch `cr/CR-008-srr-liens-l1-and-tc-sys` at commit `c629198` (05 §5.2, Submitted: the branch "may be opened for prototyping; nothing merges"). Work package: WP-PDR-11 of `docs/plan/pdr-work-plan.md` (revision 2, `ab2af2d`), wave 0, writer of `docs/requirements/sys/requirements.json` and `docs/test_cases/sys/test_cases.json` before WP-PDR-02 (plan §5.3). The number CR-008 was taken when the branch was created; CR-007 was reserved by the plan for WP-PDR-05.

The L1 requirements (05 Table 4-1 row 7) and the cases that cite them (row 17) are under CR control from SRR, and every requirement is `Active` in `baseline/srr` (L1 status delta P9, `61a3cb7`). A lien against them is therefore fixed by CR, not by a Log commit (05 §5.1 row 1). The class is proposed as **I** because 14 `description` fields change and one requirement is added (02 §10.2 Class I rows); the other edits are Class II (rationale, `verification_note`, `source_ids`, `tbr` text) or test-case edits, which ride in the same CR so that the owner rules one coherent set and the INSP-003 and INSP-025 reviewers verify one set of blobs.

## 1. Description of the change

Every change fixes a Minor finding that the SRR records carry as "Lien: fix before PDR" (`docs/reviews/SRR/checklists/requirements-sys.md`, INSP-003, post-SRR-ruling delta: finding-12 and finding-25 to finding-31; `docs/reviews/SRR/checklists/test-cases-sys.md`, INSP-025, lien table after the delta: finding-2 to finding-5 and finding-7 to finding-12), a cross item of those records (INSP-025 X1, X5, X6, X8), or the L-7 lien of RFA-SRR-007 ("ADR citations in `source_ids` where the ADR 4.1 tables list a requirement"). No hazard control is added or removed, and no ruled SRR value changes. The values the TC-SYS cases had set as "the test author's" move into the requirements, where the owner approves them with this CR.

### 1.1 Requirement statements (Class I)

| Requirement | Before (baseline/srr) | After | Lien |
|---|---|---|---|
| REQ-SYS-014 | The transceiver shall shape keyed rises and falls as raised cosines with an operator-set 10-to-90 percent time of 3 to 8 ms (TBR). | The transceiver shall shape keyed edges as raised cosines within 5 percent, with operator-set 10-to-90 percent times of 3 to 8 ms +/-0.5 ms (TBR). | INSP-003 finding-25 |
| REQ-SYS-044 | The transceiver shall return to receive after an operator-set hang time of 3 to 30 dits (TBR) at the displayed speed, following the last key-up. | The transceiver shall return to receive 3 to 30 operator-set dits (TBR) after the last key-up, within the larger of +/-1 percent and +/-0.5 ms. | INSP-003 finding-25 |
| REQ-SYS-045 | The transceiver shall generate a sidetone at an operator-set frequency from 300 Hz to 1000 Hz in 10 Hz steps. | The transceiver shall generate a sidetone at an operator-set frequency from 300 Hz to 1000 Hz in 10 Hz steps, each within +/-5 Hz. | INSP-003 finding-25 |
| REQ-SYS-054 | The transceiver shall end keying until both paddles open after 128 consecutive identical elements or 30 s (TBR) without 7-dit or 500 ms (TBR) gaps. | The transceiver shall end keying until both paddles open after 128 consecutive identical elements or 30 s (TBR) without min(7-dit, 500 ms) gaps (TBR). | INSP-003 finding-28 (and finding-25 by the decision rule) |
| REQ-SYS-077 | The transceiver shall disable the headphone amplifier output while no plug is inserted in the headphone jack. | The transceiver shall disable the headphone amplifier output within 20 ms of plug removal and while no plug is inserted. | INSP-003 finding-25 |
| REQ-SYS-083 | The transceiver shall stop charging, independently of charger and firmware, at a cell threshold set within 4.25-4.30 V (TBR) from 0 C to 45 C. | The transceiver shall stop charging, independently of charger and firmware, at a cell threshold within 4.25-4.30 V (TBR) at 18 C to 28 C. | INSP-025 finding-5, cross item X1 |
| REQ-SYS-087 | The transceiver shall refuse charging while its cells differ by more than 300 mV (TBR) or either reads outside 2.5 V to 4.3 V (TBR). | The transceiver shall hold charge current below 5 mA while its cells differ by over 300 mV (TBR) or either reads outside 2.5-4.3 V (TBR). | INSP-003 finding-25; INSP-025 finding-4 |
| REQ-SYS-088 | The transceiver shall stop charging when two independent measurements of a cell voltage differ by more than 100 mV (TBR). | The transceiver shall cut charge current below 5 mA when two independent measurements of a cell voltage differ by more than 100 mV (TBR). | INSP-003 finding-25 |
| REQ-SYS-093 | The transceiver shall pause charging while the power switch is on and USB power is present. | The transceiver shall hold charge current below 5 mA while the power switch is on and USB power is present. | INSP-003 finding-25 |
| REQ-SYS-161 | The transceiver shall delay every radiated element of an over by the same lead-in of at most 12 ms (TBR) after the receive-to-transmit changeover. | The transceiver shall delay each radiated element of an over by one lead-in of at most 12 ms (TBR), constant within 0.5 ms. | INSP-003 finding-25 |
| REQ-SYS-166 | The transceiver shall keep its regulated rails off while either cell reads outside 2.5 V to 4.3 V (TBR). | The transceiver shall keep its regulated rails below 0.5 V (TBR) while either cell reads outside 2.5 V to 4.3 V (TBR). | INSP-003 finding-25 |
| REQ-SYS-167 | The transceiver shall stop charging when its constant-voltage charge current falls by less than 20 mA (TBR) over 60 min (TBR). | The transceiver shall stop charging when its constant-voltage charge current falls by less than 20 mA (TBR) over 60 min +/-2 min (TBR). | INSP-003 finding-25 |
| REQ-SYS-185 | The transceiver shall open the charge path, independently of charger, 4.25 V protector and firmware, at a cell threshold within 4.30-4.35 V (TBR). | The transceiver shall cut charge current below 1 mA, independently of charger, 4.25 V protector and firmware, at a cell threshold within 4.30-4.35 V (TBR). | INSP-003 finding-31 |
| REQ-SYS-186 | The transceiver shall retain per-cell voltage detection in all but one protection layer after any single cell-sense connection opens or exceeds 10 kohm (TBR). | The transceiver shall keep cell thresholds of all but one protection layer within 20 mV when one cell-sense connection opens or exceeds 10 kohm (TBR). | INSP-003 finding-31 |

New requirement (Class I, `status: Draft` until this CR is approved; 08 §3.1):

| Field | Value |
|---|---|
| id | REQ-SYS-194 (REQ-SYS-191 to 193 are claimed by CR-003) |
| title | Independent cell over-voltage threshold over the charging temperature range |
| description | The transceiver shall hold the independent cell over-voltage stop threshold within 4.25-4.30 V (TBR) from 0 C to 45 C. |
| verification_method, closing case | Analysis, TC-SYS-116 (Simulation, datasheet computation); note begins "Analysis accepted per RSK-007" (04 §3, rule 7.3.6) |
| tags, hazard_ids, source_ids, tbr | revA, safety; HZ-002; those of REQ-SYS-083; closes with REQ-SYS-083 at PDR |

Why each statement changed:
- **Tolerances stated (INSP-003 finding-25, finding-31).** REQ-SYS-014 (5 percent shape, +/-0.5 ms, both under the existing TBR), REQ-SYS-044 (the REQ-SYS-042 tolerance, since the keyer clock times the hang), REQ-SYS-045 (+/-5 Hz, half a step), REQ-SYS-077 (20 ms), REQ-SYS-161 (constant within 0.5 ms, the REQ-SYS-042 floor), REQ-SYS-167 (+/-2 min, under the existing TBR), REQ-SYS-186 (20 mV, the S-8252-class threshold accuracy at 25 C). "Refuse", "stop", "pause" and "open" charging become measurable currents: below 5 mA (REQ-SYS-087, 088, 093), below 1 mA for the hardware open path (REQ-SYS-185); "rails off" becomes below 0.5 V (REQ-SYS-166, the rail-off level of REQ-SYS-149, TBR with it).
- **One-sided bounds keep their statements.** The finding-25 and finding-31 values of TC-SYS-034, 038 and 113 (+0.25 ms and +0.1 s) were allowances beyond an upper or lower bound that the requirement already states completely (REQ-SYS-048, 053, 054, 162, 184, 188, 189). They are removed from the cases, which now apply the decision rule of 04 §8.2 ("Pass if the reading plus the instrument accuracy is within the limit") inward with one capture sample period. The REQ-SYS-053, 054, 188 and 189 rationales say so.
- **REQ-SYS-054 gap (INSP-003 finding-28).** "without 7-dit or 500 ms (TBR) gaps" becomes "without min(7-dit, 500 ms) gaps (TBR)": the qualifying gap is the shorter of 7 dit times and 500 ms, as HZ-004 K4 item (ii), the rationale and TC-SYS-038 already use. The finding's own wording is 34 words; the min form keeps 25. No split, so `hazards.json` is untouched.
- **REQ-SYS-083 split (INSP-025 finding-5, cross item X1).** REQ-SYS-083 is the room-temperature threshold that the Bench Test of TC-SYS-061 measures; REQ-SYS-194 carries the 0 C to 45 C span by Analysis, because 04 §3 allows one closing method per requirement and the bench has no temperature chamber.

### 1.2 Rationales (Class II)

55 rationales change. 02 §4.3 limits a rationale to 120 words; 34 exceeded it at `baseline/srr` (INSP-003 finding-12 and finding-30). All 189 live rationales are now at most 120 words, in the §4.3 label order:
- The item "Hazard controls implemented (docs/safety/hazards.json control_req_ids): ..." is removed from the 23 rationales that carried it; it is not a §4.3 label and it duplicates the `control_req_ids` of `hazards.json`, which the tool checks (T-08, `HAZARD_INVERSE`).
- Rewritten to fit, keeping one "SRR decision NN (owner ruling 2026-09-26)" citation each and dropping history that the hazard file, the research reports or the decision memo already hold: REQ-SYS-008, 009, 010, 014, 015, 018, 020, 034, 044, 045, 053, 054, 055, 065, 077, 083, 087, 088, 090, 093, 121, 122, 125, 130, 137, 154, 161, 166, 167, 179, 180, 181, 182, 184, 185, 186, 188, 189, 190. REQ-SYS-008 no longer carries text after its `KDR:` item.
- **Fault-tolerance pointers (INSP-003 finding-26).** Hazard-analysis §8.1 item 5 (Marginal hazards and the harmonic-filter exception) is no longer cited for Critical controls: REQ-SYS-009 and 154 cite item 4 (HZ-008 C7) and §8.2 row 4; REQ-SYS-112 and 113 cite items 4 and 7; REQ-SYS-008 and 034 cite item 7 (closed by Test on every unit); REQ-SYS-153 cites item 7 and §8.2 row 11. REQ-SYS-010 (same class of pointer, not named by the finding) cites item 7. Item 5 stays only where the harmonic-filter exception or a Marginal hazard applies (REQ-SYS-017, 018, 090, 093).
- **TBR items (INSP-003 finding-29 (iii)).** The generic "TBR: value is a research or author proposal pending the decision named in the tbr plan" of REQ-SYS-009, 031, 059, 062, 086, 100, 102 and 103 states the estimate and the PDR evidence that closes it.

### 1.3 Verification notes (Class II)

| Requirement | Change | Source |
|---|---|---|
| REQ-SYS-184 | The 5 WPM squeezed characters are "recorded as data for the TBR (a squeezed C at 5 WPM holds both contacts for 2.64 s, above the 2 s limit)", no longer "which do not trip" | INSP-003 finding-27; INSP-025 X5 |
| REQ-SYS-185 | Closing Bench with the other cell held at 3.70 V (charger in constant current), judged by the 1 mA level, switching-element voltage as supporting data | INSP-003 finding-31 (ii); INSP-025 finding-11 |
| REQ-SYS-083 | Closing Bench at 18 C to 28 C; the span is REQ-SYS-194 | INSP-025 finding-5 |
| REQ-SYS-087, 088, 166 | Test points "beyond each threshold by the fixture setting accuracy" in place of 400 mV, 150 mV, 2.4 V and 4.4 V | INSP-025 finding-4 |
| REQ-SYS-051, 094, 171, 173 | The closing sources follow SRR decision 41: 5 W tune carriers and hand keying (051), the keying fixture at 5 W (094, 173), the test-mode generator at 0.5 W in four 110 s entries (171) | INSP-025 X6 |

### 1.4 `tbr` objects (Class II)

- `owner` of the 104 `tbr` objects that read "Robin decides at SRR on Claude's proposal; Claude produces the closing evidence" becomes "Robin approves on Claude's proposal at PDR; Claude produces the closing evidence", the wording REQ-SYS-184 to 189 already carry (INSP-003 finding-29 (ii)). No `close_by` changes; every TBR still closes at PDR.
- `plan` of REQ-SYS-014 (the two tolerances), REQ-SYS-054 (the shorter-of gap, and word spaces near 7 dits above about 17 WPM, INSP-025 X8), REQ-SYS-166 (the rail-off level closes with REQ-SYS-149) and REQ-SYS-167 (the window tolerance).
- INSP-003 finding-29 (i), the decision-memo count of REQ-SYS-180 to 182, is resolved by memo amendment A-2 (`docs/reviews/SRR/decision-memo.md` §13), which keeps their `tbr` objects to PDR; no requirement edit is needed.

### 1.5 `source_ids` (Class II; L-7, RFA-SRR-007)

46 ADR citations on 40 requirements. Rule applied (every case, plan lesson L5): a requirement gets the ADR when an Accepted ADR's §4.1 row names it as allocated from the ADR ("allocated ...", or "at L1") and it does not cite that ADR, unless the row says it cites another ADR "not this ADR" (ADR-002 for REQ-SYS-008 and 021, ADR-022 for REQ-SYS-017) or that it constrains the decision (ADR-027 for REQ-SYS-128, 129). Rows that say a requirement was "not created" are not allocations and are left out. The eight requirements the L-7 text names (REQ-SYS-011, 063, 064, 092, 146, 175, 178, 182) are all covered; REQ-TX-004 is an L2 requirement and goes to the L2 writer (WP-PDR-34).

ADR-002: REQ-SYS-146; ADR-003: REQ-SYS-011, 014, 015, 017, 018, 063, 064; ADR-004: REQ-SYS-092, 132, 133; ADR-005: REQ-SYS-012, 097, 098; ADR-006: REQ-SYS-058; ADR-007: REQ-SYS-139; ADR-008: REQ-SYS-175; ADR-009: REQ-SYS-040, 047 to 056; ADR-012: REQ-SYS-178; ADR-013: REQ-SYS-010; ADR-014: REQ-SYS-011, 063, 064, 172; ADR-016: REQ-SYS-009, 182; ADR-020: REQ-SYS-095; ADR-022: REQ-SYS-012; ADR-023: REQ-SYS-015, 034; ADR-024: REQ-SYS-042, 043, 135, 136; ADR-026: REQ-SYS-136; ADR-027: REQ-SYS-127.

### 1.6 TC-SYS cases (05 Table 4-1 row 17)

| Finding | Cases | Change |
|---|---|---|
| INSP-025 finding-2 | TC-SYS-003, 008 | TC-SYS-003 connects the attenuator and tinySA, measures the S21 and runs the calibration-output check, and reads the level at every F1 to F4 attempt; TC-SYS-008 step 5 reads the tinySA level at every out-of-range frequency, 144.0011 and 147.9989 MHz included |
| INSP-025 finding-3 | TC-SYS-003, 008, 047, 066, 082, 083, 101, 108, 109, 110 | The RF-off criterion reads "... on the tinySA Ultra, corrected for the attenuator and increased by the tinySA level accuracy", the TC-SYS-014 form |
| INSP-025 finding-4 | TC-SYS-064 | Each threshold approached from its violating side by the fixture setting accuracy a: 300 mV + a, 2.5 V - a, 4.3 V + a, 100 mV + a |
| INSP-025 finding-5 | TC-SYS-061; new TC-SYS-116 | TC-SYS-061 closes REQ-SYS-083 at 18 C to 28 C; TC-SYS-116 (Analysis, Simulation, `hardware/sim/checks/protector_threshold_temp.py`, planned) closes REQ-SYS-194 |
| INSP-025 finding-7 | TC-SYS-073 | `automation_ref` `hardware/sim/checks/sma_mating_life.py` (planned), with its run step and log artifact |
| INSP-025 finding-8 | 57 Bench cases | A `photo` artifact of the as-run setup (04 §8.1) on every Bench case that had none: the 56 cases the finding lists plus TC-SYS-112 |
| INSP-025 finding-9 | TC-SYS-060 | Every temperature point guarded inward per 04 §8.2: -2 C + e, +2 C - e, 43 C + e, 47 C - e, 58 C + e, 62 C - e; the "whatever the fixture resistor error" sentence is now true and the accepted guard band is stated |
| INSP-025 finding-10 | TC-SYS-036, 105 | Word spaces of at least 10 dits (0.6 s at 20 WPM), hand keying included; the capture shows keying through each minute (TC-SYS-105 gains the logic capture) |
| INSP-025 finding-11 | TC-SYS-111 | The other cell at 3.70 V so that current flows below the trip; open judged by the 1 mA of REQ-SYS-185; the REQ-SYS-087 firmware refusal also disabled in the fault build |
| INSP-025 finding-12 | `test_cases.md` summary | TC-SYS-049 listed with the cases fitted to the limits, not with the cases whose generator was replaced |
| INSP-003 finding-25, 31 | TC-SYS-013, 030, 031, 034, 038, 050, 056, 064, 065, 102, 111, 112, 113 | No "test author's" value remains (TC-SYS-103's legibility metric is the owner's D-UI-01 question, outside these findings): each case takes its tolerance from the amended requirement, or applies the one-sided bound with the 04 §8.2 rule |

`test_cases.md` is regenerated from the JSON: the body by a script that reproduces the `baseline/srr` rendering byte for byte from the `baseline/srr` JSON, and the summary counts (114 cases, 189 of 189 live requirements, Analysis 23, Demonstration 6, Inspection 14, Test 71; Bench 77, Inspection 14, Simulation 23) and a revision line. INSP-025 X3 (no committed render script) stays with the tool owner.

## 2. Reason

The PDR readiness declaration needs every SRR lien closed (01 §3.2 row S2; RFA-SRR-006 for lien L-6, RFA-SRR-007 for L-7), and the SRR records dispositioned these Minor findings "Lien: fix before PDR" with the L1 requirements author and the TC-SYS test author as owners. Plan WP-PDR-11 closes carried items C-019 to C-025 and C-038 to C-047 and the content of RID-SRR-003 (REQ-SYS-054 wording; its log move is WP-PDR-15). Workaround while the CR is open: none needed; the findings are Minor and every case is Draft.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | Eighteen Minor liens stay open and the S2 Hard criterion is not met at readiness |
| Only Class II edits now; the tolerances with the TBR closure of WP-PDR-45 | Leaves INSP-003 finding-25 and finding-31 open past F1, and REQ-SYS-045, 077 and 093 have no TBR to carry a value; the tolerances are small and visible now |
| Tolerances in the L2 children only (the finding's second route) | The L2 files are written in wave 2 (WP-PDR-34, 35), so the TC-SYS cases would cite values that do not exist at F1. Kept only where the child must follow the parent (section 4, Requirements) |
| Split REQ-SYS-054 into two watchdog requirements | Adds an id, a `hazards.json` link and a TC mapping for a wording fix; the min form states the ruled gap within 25 words |
| Keep REQ-SYS-083 whole and test at 0 C and 45 C | No chamber on the bench (CON-016); a Bench Test at the temperature extremes is not credible |
| Put the CR-008 changes directly on `main` | 05 §5.1 row 1: a non-editorial change to a class-CR CI after SRR needs an approved CR |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM or MOP value changes. TPM-013 (lead-in) keeps its 12 ms bound; the new 0.5 ms is the constancy of that lead-in, not a budget item. |
| Safety | Hazards whose control requirements change wording or gain a stated tolerance: HZ-002 (REQ-SYS-083, 087, 088, 093, 167, 185, 186, new 194), HZ-004 (REQ-SYS-054 wording), HZ-005 (REQ-SYS-077), HZ-007 (REQ-SYS-087, 166, 186), HZ-008 (REQ-SYS-014), HZ-011 (REQ-SYS-093). No control is added, removed or weakened; each change makes an existing control measurable. No module of 07 §14.1 changes. Hazard analysis re-issue: yes, limited to REQ-SYS-194: HZ-002 K2 `control_req_ids` and HZ-002 `requirement_ids` gain REQ-SYS-194 (until then `HAZARD_INVERSE` warns on it), and `docs/safety/hazard-analysis.md` §8.1 item 7 lists REQ-SYS-194 (HZ-002 K2 over 0 C to 45 C, Analysis accepted per RSK-007) as an exception; the Catastrophic HZ-002 keeps the room-temperature Test of REQ-SYS-083. RF exposure evaluation: no change. |
| Risk | RSK-007 (carries HZ-002) gains REQ-SYS-194 as an Analysis-accepted control; likelihood and consequence unchanged. The risk register is Log class; its owner (WP-PDR-18) adds the reference at the next Track pass. |
| Software classification and tailoring | None: no RMM, compliance-matrix or classification change. |
| Interfaces | None: no ICD changes. REQ-SYS-077 is internal to the jack detect and amplifier enable; no external-interface flag. |
| Operations and ConOps | None: no OPS scenario, operator procedure or handbook content changes. The REQ-SYS-054 wording states the gap that ConOps Table 3.4-4 row 3 already carries under SRR decision 42. |
| Cybersecurity | None: neither the USB firmware-load path nor the key-input command path changes. |
| Verification | Cases modified: the 64 listed in section 1.6 and the branch commit (TC-SYS-003, 004, 007, 008, 013 to 016, 022, 025, 027 to 031, 033, 034, 036 to 039, 041, 042, 045, 047, 048, 050, 051, 053, 056, 057, 059 to 062, 064 to 071, 073, 081 to 083, 089, 090, 094 to 096, 100 to 102, 104 to 106, 108 to 113), 36 of them only by the setup photograph. Added: TC-SYS-116. None invalidated; every case is Draft and none has run, so there is no re-test. Evidence classes: Bench, Simulation. No safety-critical software decision table or independence pair changes (07 §9.6). Cases whose cited requirements change (SWE-071, 04 §8.2): TC-SYS-013, 030, 031, 038, 050, 056, 061, 064, 065, 102, 111, 112, each updated here. |
| Cost | None: no BOM line, fabrication or shipping change. |
| Schedule | Fits WP-PDR-11 (wave 0). Disposition requested at B1a (Tue 09-29, OD-37) with the section 6 review before it. Plan §5.3 puts this file's writer before WP-PDR-02, so CR-008 merges before the CR-003 and CR-006 branches, which then rebase: CR-006 touches REQ-SYS-125 (rationale here), 029, 030, 037 and 147 (`tbr.owner` here) and TC-SYS-025 (photograph here); CR-003 touches REQ-SYS-103, 105, 107, 112 to 116 and 177 (`tbr.owner`, and the REQ-SYS-103, 112 and 113 rationales here) and adds REQ-SYS-191 and TC-SYS-114. The conflicts are textual in list and text fields; the WP-PDR-02 author resolves them at rebase. CR-008 does not depend on CR-003 or CR-006 and is not AT RISK. |
| Requirements and traceability | L1: 14 modified by Class I (`description`), 1 added (REQ-SYS-194); 55 rationales, 10 notes, 40 `source_ids`, 104 `tbr` owners and 4 `tbr` plans by Class II. Volatility contribution (02 §10.4): (A + M + R) / N_start = (1 + 14 + 0) / 188 = 8.0 percent at L1 from `baseline/srr`, below the 10 percent yellow threshold (07 §11.2), before CR-003 and CR-006. Children to align at PDR (sent to the L2 writers): REQ-TX-005 allows +/-10 percent of the commanded 10-to-90 time, looser than the new +/-0.5 ms of REQ-SYS-014 at the 8 ms setting (WP-PDR-34, and the TBR closure of WP-PDR-45); REQ-SW-KEYER-032 (hang) should carry the REQ-SYS-044 tolerance; REQ-SW-KEYER-020 and 021 (2 and 5 consecutive 1 ms samples) guarantee only more than 1 ms and 4 ms of contact, while REQ-SYS-048 and 162 require at least 2 ms and 5 ms, which the inward rule of TC-SYS-034 now checks (WP-PDR-35 and the debounce TBR of WP-PDR-40). `tools/traceability.py --report-only` on the branch: 0 violations, 4 warnings: `SYS_UNALLOCATED` REQ-SYS-125 and 148 (the confirmed leaf gaps) and, new, `HAZARD_INVERSE` and `SYS_UNALLOCATED` on REQ-SYS-194, which steps 3 and 5 clear before the merge. |
| Regulatory | None: no Part 97 limit changes. REQ-SYS-014 (47 CFR 97.307(a), (b)) gains shape and time tolerances inside its existing TBR; REQ-SYS-015 and the REQ-SYS-008 guard are unchanged. |
| Documentation | `docs/requirements/sys/requirements.md` (rendered by `tools/traceability.py --render`), `docs/test_cases/sys/test_cases.md` (regenerated); `docs/safety/hazards.json`, `docs/safety/hazard-analysis.md` and `docs/design/allocation.json` by their writers (section 5); `docs/vv/traceability-report.md` at the merge; RSK-007 text (Log). The SRR records INSP-003 and INSP-025 name the `baseline/srr` blobs, so `tools/validate_docs.py` reports record drift on them on the branch (48 of 50) until their delta iterations name the frozen blobs below. |
| Released units | None: no unit exists. |

Classification rationale: Class I, because 14 requirement statements change and one requirement is added (02 §10.2; 05 §2 Class I: "affects a baselined requirement"). No value that the owner ruled at SRR changes.

Independence note (charter §2): WP-PDR-11 assigns the L1 author and the TC-SYS test author roles to one work package, and this revision was written by one invocation in both roles. No implementation exists, so IEEE 1012 test independence from the design is intact, but the author and test-author roles were not separate invocations. The INSP-003 and INSP-025 reviewers are asked to treat every case change as author-written and check it against the requirement text alone.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Section 1.1 to 1.5 in `docs/requirements/sys/requirements.json`; `requirements.md` rendered by `tools/traceability.py --render` | Claude (L1 requirements author, WP-PDR-11) | Prototyped on the branch at `c629198` |
| 2 | Section 1.6 in `docs/test_cases/sys/test_cases.json`; `test_cases.md` regenerated | Claude (TC-SYS test author, WP-PDR-11) | Prototyped on the branch at `c629198` |
| 3 | `docs/safety/hazards.json`: REQ-SYS-194 in HZ-002 K2 `control_req_ids` and in HZ-002 `requirement_ids` (T-08) | Writer of `hazards.json` per plan §5.3 (WP-PDR-02, then WP-PDR-16b), on this branch before the merge | |
| 4 | `docs/safety/hazard-analysis.md` §8.1 items 3 and 7: REQ-SYS-194 as the Analysis exception for HZ-002 K2 over temperature (RSK-007) | Safety analyst (WP-PDR-16) | |
| 5 | `docs/design/allocation.json`: REQ-SYS-194 allocated as REQ-SYS-083 is (PWR) | Writer of `allocation.json` (WP-PDR-02, then WP-PDR-31) | |
| 6 | `docs/risk/register.json` RSK-007: cite REQ-SYS-194 | Risk manager (WP-PDR-18, Log class) | |
| 7 | Delta iterations of INSP-003 and INSP-025 verify each lien on the frozen blobs below | Independent reviewers (new invocations of `reviewer:requirements-sys` and `reviewer:INSP-025`) | |
| 8 | After approval: rebase onto `main` if `main` moved these files, re-render, re-run `tools/validate_docs.py`, `tools/traceability.py` and the unit tests, merge `--no-ff` with the owner's merge approval, before WP-PDR-02 merges CR-003 and CR-006 | Claude (CM) | |

Frozen products for review (plan rule C2), at branch commit `c629198`: `docs/requirements/sys/requirements.json@a73449377e8d055f5d247130b8850bf3f5a151d9`, `docs/requirements/sys/requirements.md@4e110b16027fbe446e846a8c5f9d2dc5c2899af6`, `docs/test_cases/sys/test_cases.json@117c08dedd65171f88d5bff015d0914db97b3065`, `docs/test_cases/sys/test_cases.md@00e4454f5c836df0eac430b9ec9f95b99630d316`.

Verification of the implementation (what the independent reviewer checks, every case named, plan rule C7): each before and after of section 1.1 against the blob and the 25-word limit; that every one of the 189 live rationales is at most 120 words and none carries the hazard-controls item; each of the seven finding-26 pointers and REQ-SYS-010 against `hazard-analysis.md` §8.1 items 4, 5 and 7 and §8.2 rows 4 and 11; the eight finding-29 (iii) items against their `tbr.plan`; the 104 owner fields; the 46 ADR citations against the rule of section 1.5, and that no §4.1 row that meets the rule was missed; for each of the 57 photograph additions that the case is Bench and had no photo; the TC-SYS-060 guard arithmetic at the six points; the TC-SYS-064 points; that TC-SYS-111 can reach constant current with one cell at 3.70 V; REQ-SYS-194 and TC-SYS-116 against 04 §3 and rule 7.3.6; that no other line of the four files changed (`git diff ab2af2d c629198`); and the tool runs of section 4.

## 6. Independent review of the impact assessment

Required (Class I, and requirements and test cases are affected). Not yet performed. The review is requested before the owner's disposition (plan rule C6).

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

### 6.1 Round 1 (2026-09-27)

Reviewer: independent reviewer agent, a separate invocation that authored none of this CR, none of the prototype commit `c629198`, and none of the INSP-044 or INSP-045 records (`c199eb2`). Date 2026-09-27. Configuration reviewed: HEAD `6086319` on `main` (this CR at `4dab5dc`); branch `cr/CR-008-srr-liens-l1-and-tc-sys` at `c629198` (merge base `ab2af2d`); `baseline/srr` on `779f93f`. Method: 05 §5.2 and §5.3 field by field and 02 §10.2 and §10.3. Then the class, the effectivity, the branch contents against the CR (`git diff main...cr/CR-008-srr-liens-l1-and-tc-sys`; a field-level script diff of both JSON files between `baseline/srr` and `c629198`), the section 5 verification plan, and whether any requirement or control is weakened. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search, with queries on REQ-SYS-083 and the over-voltage band, the REQ-SYS-054 watchdog and decision 37, the stale "30 s" wording and TBR finding 7, and the CR `affected_ids` tooling. `grep` was then used over `docs/`, `hardware/` and `tools/` for every changed id, only to pin files and lines. The tools ran on `git archive` exports in the scratchpad, never on the shared tree.

Severity rule: Major if the owner would disposition on an incomplete or wrong basis; otherwise Minor.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| R1-F1 (Major): the Interfaces row says "None", but three ICDs bound or quote the changed statements, and one of them conflicts with the new REQ-SYS-077 value that question 2 asks the owner to accept | Independent reviewer agent | 2026-09-27 | The section 4 Interfaces row reads "None: no ICD changes. REQ-SYS-077 is internal to the jack detect and amplifier enable; no external-interface flag". 05 §5.3 names the headphone jack, the key jack and the battery as external interfaces, and 05 Table 4-1 row 10 makes a change to any of them Class I once the ICDs are baselined. 02 §10.3 item 5 requires the Interfaces row to name the ICD and the requirements on both sides. The repository shows three affected ICDs. (a) **Headphone jack, `docs/icd/ICD-CTL-PHONES.md`.** REQ-SYS-077 cites this ICD in `design_refs`. Its line 140 gives PHONES_DET the timing "debounced 50 ms", with no exemption for removal, and the figure source `docs/icd/figures/render_icd_figures.py` line 404 says "detect debounced 50 ms". The new statement requires the amplifier off "within 20 ms of plug removal", and the new rationale says "20 ms covers the jack-detect debounce and the enable path". If the 50 ms debounce applies at removal, as the ICD reads, no design that follows the ICD can meet 20 ms. The ICD's §4 table (line 215) also quotes the old REQ-SYS-077 statement word for word. Question 2 asks the owner to accept "amplifier off within 20 ms of plug removal" with the recommendation "each is the value the cases already used". Nothing tells the owner that the interface definition the requirement cites sets 50 ms. CR-003 also edits this ICD (its `affected_ids`). (b) **Battery, `docs/icd/ICD-PWR-CELL.md`.** Line 139 credits the 0 C to 45 C span to REQ-SYS-083, which after the split states 18 C to 28 C; the span is now REQ-SYS-194. Line 143 and the §4 lists (lines 50, 146, 210, 217, 235) carry "refused", "stopped" and REQ-SYS-083 alone, but not REQ-SYS-194 or TC-SYS-116. (c) **Key jack, `docs/icd/ICD-CTL-KEY.md`.** Lines 161 and 261 still give the pre-SRR paddle watchdog, "128 consecutive identical elements or 10 s (TBR)", with the D-KN3 TBR plan. This staleness predates the CR and is not caused by it. But this CR rewrites REQ-SYS-054, and WP-PDR-11 is charged with "the stale '30 s' wording against decision 37", so the CR is the place to route it | Open. Fix: rewrite the Interfaces row. It should name ICD-CTL-PHONES (headphone flag), ICD-PWR-CELL (battery flag) and ICD-CTL-KEY (key-jack flag), each with the rows above, and route the changes to the ICD writer (WP-PDR-36a/36b; for ICD-CTL-PHONES, together with CR-003). For REQ-SYS-077, state the resolution before the disposition: either a removal path with no 50 ms debounce (for example an asymmetric debounce, removal acted on within about 15 ms), recorded as an ICD change, or a removal bound that includes the 50 ms debounce. Add that choice to question 2, and add row 10 to `affected_cis` if the ICDs change under this CR |
| R1-F2 (Minor): `affected_ids` lists 15 of the 145 requirements and 29 of the 65 test cases that the branch changes | Independent reviewer agent | 2026-09-27 | 02 §10.3 item 1: "`affected_ids` in the front matter lists every `REQ-`, `TC-` ... id touched". The script diff from `baseline/srr` to `c629198` finds 145 requirement entries changed or added: 14 in `description`, 1 added, 55 in `rationale`, 10 in `verification_note`, 40 in `source_ids`, 104 in `tbr.owner` and 4 in `tbr.plan`. It finds 65 test cases changed or added: 64 modified and TC-SYS-116. The front matter lists only the 15 requirements whose statements change or which are added, and 29 cases. It leaves out 130 requirement ids and 36 cases (TC-SYS-004, 007, 014 to 016, 022, 025, 027 to 029, 033, 037, 039, 041, 042, 045, 048, 051, 053, 057, 059, 062, 067 to 071, 081, 089, 090, 094 to 096, 100, 104, 106), all of which the body names. No tool reads `affected_ids` today, so nothing breaks. But the CSA register and a later T-13 comparison would under-report the CR's scope, and the CR-003 and CR-006 authors would not see the overlaps from the front matter | Open. Fix: list every touched id in `affected_ids` (script-generated from the diff), or amend 02 §10.3 item 1 by CR to allow a range or reference form |
| R1-F3 (Minor): "below 5 mA" for REQ-SYS-093 does not carry the reason other products rely on this requirement | Independent reviewer agent | 2026-09-27 | "Pause charging" becomes "hold charge current below 5 mA while the power switch is on and USB power is present". Three products use REQ-SYS-093 to assume that the charger's 1.5 MHz boost converter is not running while the radio operates: HZ-011 K2 ("the charger's boost ripple is absent whenever the radio is operating"), `docs/icd/ICD-CTL-USB.md` line 177, and `docs/icd/ICD-PWR-CELL.md` line 176. The clock-plan analysis in progress under WP-PDR-20 (uncommitted at review time) makes the same assumption. A current below 5 mA is necessary for that, but it does not imply a converter that has stopped switching. The L1 control of HZ-011 K2 is not weakened, since termination masking is what the statement bounds. The ripple assumption, however, now rests on no requirement | Open. Fix: in the section 4 Requirements row, add a child to align. The PWR (WP-PDR-34) and SW (WP-PDR-35) L2 children of REQ-SYS-093 should state that the charger is disabled, not merely current-limited, or the analyses that assume no boost ripple should cite that child |
| R1-F4 (Minor): the Schedule row and the section 5 verification plan leave out how steps 3 to 6 reach the merge | Independent reviewer agent | 2026-09-27 | (a) Steps 3 and 5 must land on this branch before the merge, which also clears `HAZARD_INVERSE` and `SYS_UNALLOCATED` on REQ-SYS-194. Their wave-1 writer is WP-PDR-02 (plan §5.3 rows for `hazards.json` and `allocation.json`), and WP-PDR-02 depends on OD-02 and OD-03, the CR-003 and CR-006 dispositions (plan §3.2). The statement "CR-008 does not depend on CR-003 or CR-006" is therefore true of the content but not of the merge date. If B0 or B1a slips OD-02 or OD-03, this merge waits too, and WP-PDR-02 then cannot start on the same files before CR-008 merges. (b) CR-003 step 6 also writes HZ-002 links in `hazards.json` (CR-003 `affected_ids` has HZ-002 and RSK-007), but the conflict list in the Schedule row names only requirements and TC-SYS-114. (c) Step 4 (`hazard-analysis.md` §8.1 item 7) falls to WP-PDR-16, which runs in wave 2, after this merge. Between the merge and WP-PDR-16, §8.1 item 7 calls itself "the complete list" but omits REQ-SYS-194. The requirement's note records the acceptance, so the 04 rule 7.3.6 check still passes. (d) The section 5 verification plan asks for "the tool runs of section 4". It does not name checks of the step 3 to 6 content: REQ-SYS-194 in HZ-002 K2 `control_req_ids` and in HZ-002 `requirement_ids`, the module in `allocation.json`, the new §8.1 item 7 row, and the RSK-007 citation | Open. Fix: state in the Schedule row that the merge waits for WP-PDR-02 steps 3 and 5 (and so for OD-02 and OD-03), or let the hazards.json and allocation.json writer act for this CR alone before those dispositions. Name the HZ-002 overlap with CR-003 step 6. Say that step 4 lands after the merge and when. Add the step 3 to 6 checks to the verification plan |
| R1-F5 (Minor): the new TBR and REQ-SYS-194's downstream routing are not in the assessment | Independent reviewer agent | 2026-09-27 | (a) REQ-SYS-194 carries a new `tbr` object, which makes 110 L1 TBR objects (109 at `baseline/srr`, counted by script). The plan counts "109 L1" in WP-PDR-45 and OD-09, and the §10.2 G9 row (WP-PDR-24, power) does not list REQ-SYS-194. (b) CR-011 (Submitted) adds a PDR-gate form of `SYS_UNALLOCATED` that needs "a live L2 child or the tag `leaf`". An `allocation.json` entry (step 5) clears the warning under today's tool, but not under that gate rule. The Requirements row's "Children to align at PDR" does not route REQ-SYS-194 to the PWR L2 writer (WP-PDR-34). (c) TC-SYS-116 and TC-SYS-073 name planned checkers (`hardware/sim/checks/protector_threshold_temp.py`, `hardware/sim/checks/sma_mating_life.py`), and no work package or owner is named for them | Open. Fix: in the Requirements row, give the L1 TBR count (110) and route REQ-SYS-194 to G9 and WP-PDR-45 and to a PWR child (or `leaf`) through WP-PDR-34. In the Verification row, name who writes the two planned checkers and by when |

Items checked with no finding:
- **Class I is correct.** Fourteen `description` changes and one added requirement are Class I under 02 §10.2. `verification_method`, `priority`, `parent_id`, `hazard_ids`, `status` and the controlled tags are unchanged on every existing entry (script). All other changes are Class II fields or test-case edits.
- **Effectivity.** Documents only. `target_release: none`, and no unit or release exists. REQ-SYS-194 and TC-SYS-116 are Draft until the approval.
- **Branch contents.** `git diff main...cr/CR-008-srr-liens-l1-and-tc-sys` touches exactly the four files of section 5, and `main` has not changed them since `ab2af2d` (the blobs are byte-identical to `baseline/srr`). The four frozen blob ids equal `git rev-parse c629198:<path>`. The commit carries `CR: CR-008`. No other open `cr/` branch touches `docs/requirements/sys/`, `docs/test_cases/sys/`, `docs/safety/`, `docs/design/allocation.json` or `docs/icd/`.
- **Counts in sections 1 and 4, reproduced by script.**
  - Requirements: 14 statements, 1 added, 55 rationales, 10 notes, 40 `source_ids`, 104 `tbr.owner`, 4 `tbr.plan`, none removed.
  - Test cases: 64 modified. Of those, 36 change only `expected_artifacts`, and 57 gain a `photo` artifact, all of type Bench. TC-SYS-116 is added and none is removed, and no case changes `requirement_ids` or `status`.
  - Limits: the longest live statement is 25 words and the longest rationale is 120 words, and no rationale carries the hazard-controls item.
  - Volatility: (1 + 14 + 0) / 188 = 8.0 percent, with 188 Active at `baseline/srr`.
- **Tool runs, reproduced.**
  - `tools/traceability.py --report-only` on an export of `c629198`: 0 violations and 4 warnings, as section 4 states.
  - The same on a merge preview (the `main` tree with the four branch files; `tools/traceability.py` is unchanged from `ab2af2d` to `main`): the same 0 violations and 4 warnings.
  - `tools/validate_docs.py` on the merge preview: 71 of 71 pass. The record drift rule does not run outside a work tree, so the INSP-003 and INSP-025 drift that section 4 predicts is not shown there.
- **Cases citing changed statements (SWE-071).** A script over every test-case file finds TC-SYS-013, 030, 031, 038, 050, 056, 061, 064, 065, 102, 111 and 112 citing a changed statement in `requirement_ids`, which is the list in the Verification row. The text-only mentions of REQ-SYS-054 in TC-TX-007, 008, 012 and TC-SW-KEYER-019, 038 ("below the 128-element and 30 s limits"; single-paddle PARIS) stay true under the min(7-dit, 500 ms) wording.
- **L2 children.**
  - `parent_id` points to REQ-SYS-014, 044, 048 and 162 only from REQ-TX-005 and REQ-SW-KEYER-020, 021 and 032, the four the Requirements row routes.
  - No L2 requirement has REQ-SYS-045, 077, 083, 087, 088, 093, 161, 166, 167, 185 or 186 as parent. Their children arrive at PDR through WP-PDR-34 and 35.
- **Hazard links.** `hazards.json` at `main` ties the changed statements to HZ-001 K3, HZ-002 K2 to K6 and K9, HZ-003 K3, HZ-004 K4, HZ-005 K6, HZ-006 K6, HZ-007 K3, HZ-008 K4, HZ-011 K2 and HZ-012 K2. The Safety row names HZ-002, 004, 005, 007, 008 and 011. HZ-001, 003, 006 and 012 reach REQ-SYS-054 only through the HZ-004 K4 wording, which is unchanged in meaning.
- **Risk.** RSK-007 carries HZ-002 (`related.hazard_ids` HZ-002, HZ-007, HZ-011), so the note "Analysis accepted per RSK-007" on REQ-SYS-194 meets 04 rule 7.3.6.
- **No requirement or control is weakened beyond what the owner is asked to rule.**
  - The REQ-SYS-083 split does not lose a Test that existed. At `baseline/srr`, TC-SYS-061 already measured only at room temperature and left the span to "the supporting threshold analysis". The split makes that Analysis an explicit, risk-accepted exception for the Catastrophic HZ-002, and question 3 puts it to the owner.
  - The one-sided bounds tighten, since the allowances beyond the bound are removed (question 4).
  - The other statement changes add a tolerance or a measurable level to an existing control.
  - No value ruled at SRR changes. The REQ-SYS-045 range and step (decision 46), the REQ-SYS-044 3 to 30 dits (decision 47) and the REQ-SYS-054 limits (decision 37) are kept.
- **Rows that need no change:** Performance margins (TPM-013 bounds the lead-in, not its constancy), Software classification, Operations and ConOps (ConOps OPS-013 step 3 already states "whichever is shorter"), Cybersecurity, Cost, Regulatory and Released units.
- **Observation (no finding).** The WP-PDR-33 keyer host study, uncommitted in the working tree at review time (`docs/design/analysis/keyer-host-study/keyer_model.py`), models a proposed 2-dit qualifying gap against the baselined "7 dit times or 500 ms, whichever is shorter". If WP-PDR-45 adopts a different gap at the REQ-SYS-054 TBR closure, the statement changes again. That does not affect this disposition, because the CR's min form keeps the ruled meaning.

Reviewer concurrence: I concur with the class, the effectivity, the branch contents and the direction of every change. I do not concur with disposition until R1-F1 is resolved, because question 2 presents the REQ-SYS-077 value to the owner without the interface conflict. **Impact review complete, with findings: 1 Major (R1-F1), 4 Minor (R1-F2 to R1-F5).** The CR stays Submitted. The author revises section 4 (and section 1 or 12 as R1-F1 requires), and the reviewer re-checks under a new round heading.

## 7. CCB disposition (owner)

Not dispositioned. Requested at owner session B1a (Tue 09-29, OD-37), after the section 6 review, so that the branch merges before WP-PDR-02 implements CR-003 and CR-006 on the same files. Questions for the owner are in section 12.

| Field | Value |
|---|---|
| Decision | |
| Class confirmed | |
| Date | |
| Conditions | |
| Rationale | |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

## 8. Implementation record

Not yet implemented (the branch holds a prototype only).

| Commit | Files | Trailer check (`CR: CR-008` present) |
|---|---|---|
| `c629198` (prototype, branch `cr/CR-008-srr-liens-l1-and-tc-sys`) | `requirements.json`, `requirements.md`, `test_cases.json`, `test_cases.md` | Present |

Traceability report after implementation: to be regenerated at merge; renders regenerated: `docs/requirements/sys/requirements.md`, `docs/test_cases/sys/test_cases.md`.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| | | | |

Independent verifier (agent invocation): pending.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Draft, then Submitted | Claude (WP-PDR-11 author) | this file's commit | Created with the impact assessment complete; product prototype on the branch at `c629198` |
| 2026-09-27 | Submitted (impact review round 1 recorded) | Independent reviewer agent | the commit that records section 6.1 | Impact review complete with 1 Major (R1-F1, Interfaces row and the REQ-SYS-077 debounce conflict) and 4 Minor (R1-F2 to R1-F5) findings; stays Submitted for author revision before disposition |

## 12. Questions for the owner (answer with the disposition)

1. Approve CR-008 as Class I? Recommendation: approve.
2. Accept the values that move from the test cases into the requirements: sidetone +/-5 Hz (REQ-SYS-045), amplifier off within 20 ms of plug removal (REQ-SYS-077), charge current below 5 mA for a refused, stopped or paused charge (REQ-SYS-087, 088, 093), below 1 mA for the hardware open path (REQ-SYS-185), thresholds kept within 20 mV under a sense-path fault (REQ-SYS-186), lead-in constant within 0.5 ms (REQ-SYS-161), hang within the REQ-SYS-042 tolerance (REQ-SYS-044), and, under their existing TBRs, the envelope shape and time tolerances (REQ-SYS-014), the +/-2 min current-fall window (REQ-SYS-167) and the 0.5 V rail-off level (REQ-SYS-166)? Recommendation: accept; each is the value the cases already used, now visible for your approval.
3. Accept the split of REQ-SYS-083: the room-temperature threshold by Bench Test, and new REQ-SYS-194 for 0 C to 45 C by Analysis accepted per RSK-007, a new Analysis exception for a control of the Catastrophic HZ-002? Recommendation: accept; the bench has no chamber, and the Test of the same threshold at room temperature stays.
4. Accept that one-sided bounds (5 s, 30 s, 2 s, 120 s, 60 s, and the 2 ms and 5 ms debounce minima) are verified with the instrument accuracy applied inward (04 §8.2), with no allowance beyond the bound? Recommendation: accept; the design then targets inside the bound.
