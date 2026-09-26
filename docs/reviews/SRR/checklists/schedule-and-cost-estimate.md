---
id: INSP-023
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/schedule-and-cost-estimate.md
product: docs/plan/schedule.md, docs/plan/cost-estimate.md
# product_commit: the author's fix commit a7c70d2 (INSP-023 finding-1, finding-2), HEAD at iteration 2; iteration 1 reviewed b301df2 at HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
product_commit: "a7c70d2568ea19f862bf2f52e87742d7a0f3ab96"
# product_files: committed blobs verified at iteration 2 (git rev-parse HEAD:<path> at HEAD a7c70d2); iteration 1 reviewed schedule.md@2773cfb109cf1715bb4cb20f5e9faeb89274728e and cost-estimate.md@1fcb9ece64e111342e37e391c808f0955eb18090
product_files: ["docs/plan/schedule.md@53de92ae211105127f56103d26884d14342190d0", "docs/plan/cost-estimate.md@0dda83cbd5ada9474562cc1741df67a31e1a7ffb"]
product_size: 2 plans (schedule.md 62 lines at iteration 2: 5 gate rows, 9 firmware milestone rows, rustos dependency section, 9 lead-time rows, 4 risks, lien policy; cost-estimate.md 25 lines, 13 table rows)
sprint: SRR-prep
author_agent: "author:plan (Claude main session, lead SE; schedule.md at 4e3f891, cost-estimate.md revised at b301df2; both revised at a7c70d2 for finding-1 and finding-2)"
reviewer_agent: "reviewer:INSP-023"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
# readiness_met: false because R3 (author self-check) is still not on record; see finding-8
readiness_met: false
# reviewer_verdict: finding-1 and finding-2 Verified at iteration 2; every Minor finding is "Lien: fix before PDR" (convergence rule of 2026-09-26)
# verdict: held at NEEDS CHANGES only by readiness R3 (validate_docs.py: APPROVED needs readiness_met true), as in INSP-019 and INSP-021;
# it becomes APPROVED (with liens) on re-issue once the author self-check is filed or the owner waives it (decision 115)
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 7
findings_open: 0
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G6, R3]
effort_turns: 42
effort_minutes: 55
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-023: schedule and cost estimate (`docs/plan/schedule.md`, `docs/plan/cost-estimate.md`)

**Products.** `docs/plan/schedule.md@2773cfb1` (last commit `4e3f891`) and `docs/plan/cost-estimate.md@1fcb9ece` (last commit `b301df2`), read at the review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; neither file differs from HEAD in the working tree. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents" (section G and A8), the plan review items `docs/process/08-agent-briefing.md` section 3.5 assigns to plans. **Criteria judged:** SRR entrance rows 19 ("Cost estimate and basis (tailored)", Soft, G-4 6.14 and 6.15, evidence `cost-estimate.md` "(BOM, fabrication, assembly, CNC, shipping, contingency)", form "Cost table") and 21 ("Engineering development assessment and technical plan for Phase B", Soft, G-4 6.22, evidence SEMP Phase B section and `schedule.md`, form "Milestone list to PDR") of `docs/process/01-lifecycle-and-reviews.md` section 4.3 (lines 204 and 206); package `docs/reviews/SRR/package.md` section 4 rows 19 and 21 (both rated Met with no record) and section 6.15 (no record named for either product). The two products are also NPR 7150.2D section 6.1 records b (software schedule) and c (software cost estimate) of `07-software-engineering-plan.md` section 1.3 (lines 38 and 39), so the governing requirements are SWE-015, SWE-151 and SWE-016 as tailored in `docs/process/rmm.json`.

**Independence.** The reviewer did not author either product and did not edit them. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: cost estimate, TPM-014, SWE-015 and SWE-151 tailoring, schedule baseline; SRR entrance rows 19 and 21; import duties and shipping for PCBWay orders); `grep -n` was used afterwards only to pin lines. **Convergence rule** (lead SE direction 2026-09-26, charter section 4 item 3): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR" and carried by the package as a Routine item.

**Iteration 2 (2026-09-26, HEAD `a7c70d2`).** The author reported finding-1 and finding-2 fixed in one commit, `a7c70d2` ("Schedule and cost estimate: SWE-016 firmware milestones, rustos dependency and lead times; SWE-151 life-cycle reserves"), which touches only the two products (`git show --stat a7c70d2`: schedule.md +44 -1, cost-estimate.md +7 -2). The reviewer read the whole diff and the new blobs `schedule.md@53de92ae` and `cost-estimate.md@0dda83cb` and checked every new citation against its source (claude-context search first, then `grep -n` to pin): 07 sections 3.1 (line 150, FW-B1 set including WP-SW-14 on package decision 40), 3.2 (FW-B0 to FW-B4), 14 (line 583, no module sprint before the SRR decision memo) and 19 (WP-SW-01 to WP-SW-14); `tools/toolchain.lock.md` line 206 (rustos `c54d35a`); `pcbway-fabrication-and-assembly.md` F17 ("5-7 working days at least") and F21 (quotation within 1 business day, Advanced PCB 4-layer 5 days, assembly about 3 working days, closure 2026-10-01 to 10-04 GMT+8, PCBs and stencil built while parts are in transit); `enclosure-cnc-and-openscad-pipeline.md` A10 (13 to 15 days, 3 days delivery, 6061 3 to 5 business days, 2023, Medium); `register.md` RSK-013, RSK-014 (USD 300 to 800, 6 to 12 weeks), RSK-023, RSK-038, RSK-053 (S1, S2); ADR-019; ADR-025 (cap of five complete units, two unassembled boards as spares); 06 section 14.1 class 2 ("Owner when the ADR ... spends money"); package decisions 40, 109 and 110. The date windows of schedule.md section 3 recompute from the stated durations (parts import 2026-09-29 plus 5 to 7 working days with 2 closure working days gives 10-07 to 10-09; CNC 13 to 15 days plus the 4-day closure gives 10-16 to 10-18; plus 3 days shipping). The cost arithmetic recomputes: 972 + 300 + 40 = 1312; 1836 + 800 + 120 = 2756. No em dash in either blob; no TBD or TBR.

**Tool runs (2026-09-26, repository root, `.venv/bin/python`):** `tools/validate_docs.py` exit 0 (37 passed, 0 failed, before this record was added); `tools/traceability.py --report-only` exit 0 (237 requirements, 170 test cases, 0 violations, 2 warnings REQ-SYS-125 and REQ-SYS-148; no tracked file changed). Neither product carries a requirement id or a TBD/TBR; em dash count 0 in both.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G1, CK-REQ-G4, S2 | `schedule.md` whole table (lines 5 to 11) and "Schedule risks and levers" (lines 13 to 18) | The schedule does not carry the content that the approved SWE-016 tailoring says it carries at SRR. `rmm.json` SWE-016 (disposition T, status Planned) states: "Milestone list in docs/plan/schedule.md: review gates in order with the owner's target dates (SI-020), PCBWay and DigiKey lead times, firmware milestones (HAL bring-up in emulation, keyer complete for straight key and iambic paddle per SI-018, receive chain complete, release candidate) and the hardware, software and operations dependencies between them (a, b, c) ... Planned for SRR: the firmware milestone rows of schedule.md"; its residual-risk control is "docs/plan/schedule.md carries the lead-time entries ... and is re-presented at every gate" (07 section 22 SWE-016 row, line 827, says the same). At `2773cfb1` the schedule has five gate rows; firmware appears only as the activity "Firmware implementation, host tests, emulation scenarios" in the TRR row; there is no firmware milestone row, no dependency between milestones, and one lumped lead time "2 to 4 weeks". The rustos upstream driver work packages (SI-033; 07 section 19) are a cross-project dependency of the firmware milestones (NPR 7150.2D 3.3.1 d, corpus `npr-7150-2d/03-chapter3.md` line 133) that neither the schedule nor the RMM row ("No cross-project dependencies exist (d)") records. The SRR row 21 evidence form "Milestone list to PDR" therefore exists for the gates only, and the RMM row's "Planned for SRR" item is not delivered at SRR. Fix: add the firmware milestone rows keyed to gates, the dependency of each milestone (hardware, software, operations, rustos work package of 07 section 19), and the separate lead-time entries (PCBWay quote response, parts import at least 5 to 7 working days, assembly, CNC 13 to 15 days, shipping; holiday closure 2026-10-01 to 10-04 of RSK-053) with their sources (`docs/research/pcbway-fabrication-and-assembly.md` F17, F21; `docs/research/enclosure-cnc-and-openscad-pipeline.md` A10). Cross: the RMM author corrects SWE-016 item d. **Iteration 2: Verified** at `a7c70d2` (`schedule.md@53de92ae`): section 1 adds FM-1 to FM-9 keyed to the gates (FW-B0 to FW-B4 of 07 section 3 plus the four named RMM milestones: FM-2 HAL bring-up in emulation, FM-5 keyer complete for straight key and iambic paddles, FM-6 receive chain complete, FM-8 release candidate), each with its hardware, software, operations and rustos dependency; section 2 records the rustos cross-project dependency (SWE-016 d) with the work packages per gate, RSK-013, RSK-023 and the pinned commit; section 3 gives the separate lead-time entries (quote, holiday closure, parts import, fabrication, assembly, CNC, shipping, DigiKey, zero-stock lines) with sources and estimated windows; the TRR row points to section 3. The RMM SWE-016 "Planned for SRR" content now exists. Residual gaps are Minor (finding-9; cross item 1). | Verified | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-REQ-G1, CK-REQ-G4, S1 | `cost-estimate.md` lines 3, 7 to 18, note line 20 | The cost model does not contain what the approved SWE-151 tailoring records as "In place". `rmm.json` SWE-151 implementation: "covers the full life cycle (three-unit prototype build, one rework spin, spares) ... includes technology risk (RF component availability, rework-spin contingency) and other direct costs (shipping, instruments)". The product excludes the rework spin from every total (line 20: "A second board spin (rev B), if needed, would repeat the fabrication and assembly lines"), has no spares line, and states shipping only for the fabrication line (line 9). The omitted spin is not covered by contingency: RSK-014 prices a second spin at USD 300 to 800, while the unit contingency is USD 138 to 274 (line 14). The rework spin is a life-cycle cost element that SWE-151 a and d (corpus `npr-7150-2d/03-chapter3.md` lines 107 and 113: "Covers the entire software life cycle", "Incorporates risk and uncertainty") require as tailored, so the RMM compliance claim for SWE-151 is unsupported by its implementing product. The RMM SWE-015 implementation also still reads "optional instrument (SI-021)" while the product (line 16) records the instrument as committed (SI-034, ADR-021). Fix, one of: (a) add a rework-spin reserve line (fabrication plus assembly of rev B, sourced to RSK-014) and a spares line, stated inside or outside the TPM-014 unit basis; or (b) the RMM author restates SWE-151 to what the model covers, for owner acceptance with the RMM in the SRR decision memo. Cross in both cases: correct the SWE-015 instrument wording in `rmm.json` and re-render `rmm.md`. **Iteration 2: Verified** at `a7c70d2` (`cost-estimate.md@0dda83cb`), option (a): a rework-spin reserve line (USD 300 to 800, sourced to the RSK-014 consequence, within the ADR-025 cap) and a spares line (USD 40 to 120, with the two unassembled ADR-025 boards as board spares already in the fabrication line) are added outside the TPM-014 unit basis and the total envelope, with a life-cycle total of USD 1312 to 2756 (arithmetic checked) and a paragraph tying them to SWE-151 a and d and to the ADR draw rule of 06 section 14.1 class 2. The unit budget, total envelope and TPM-014 are unchanged, so SEMP lines 45 and 415 stay consistent. Shipping per line for the reserve lines and the others stays under finding-3; the RMM SWE-015 "optional instrument (SI-021)" wording stays a cross item (rmm.json unchanged since `ae8abd2`). | Verified | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | S1, CK-REQ-G1 | `cost-estimate.md` lines 9 to 12 (Basis column) | The basis of estimate is thinner than the row 19 evidence ("BOM, fabrication, assembly, CNC, shipping, contingency") and the TPM-014 definition ("shipping and duties"; formula `(parts + fab_assembly + enclosure + printing + shipping)`). Shipping is stated for fabrication only; import duties, and shipping of the assembly, enclosure and DigiKey lines, are not stated as included or excluded. The assembly line's "~80 to 120 USD parts per board" does not reflect the research finding that PCBWay-sourced parts may cost 1.5 to 2 times distributor list (R-PCB-05, `pcbway-fabrication-and-assembly.md` F17, F22), and no line cites its source or date (the enclosure line could cite A10). Fix: state per line what shipping and duties are included, and cite the research finding and date behind each figure. | Lien | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-G1 | `cost-estimate.md` line 15 | "SEMP section 7 resources paragraph" points to the wrong section: the resources paragraph with the TPM-014 unit basis is SEMP section 8.0 (`semp.md@77fc9ea4` line 415). Fix: cite SEMP section 8.0. | Lien | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-G6, CK-REQ-G1 | `schedule.md` lines 3 to 18 | The schedule is not updated for this review although SEMP section 3.6 table line 128 says "SRR, updated every review" and the SEMP section 5.0 Technical Planning measure is "slipped milestones without a recovery: 0" (line 204). The SRR target "Sat morning" (line 7) has passed with the package not ready, and the schedule records no actual, slip or recovery; package section 12 carries them instead. The risk list (lines 15 to 18) names no register id although RSK-014 (Red, expedited gates), RSK-053 (holiday closure) and RSK-038 (zero stock) are the schedule risks in `docs/risk/register.json`. Fix: add a status (actual, slip cause, recovery) per milestone or point to package section 12 as the status of record, and give each risk its RSK id. | Lien | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-G1 | `schedule.md` line 20 (Liens policy) | "No liens are carried past CDR into procurement without an explicit owner decision recorded in the CDR decision memo" admits any lien into procurement on an owner decision. `01-lifecycle-and-reviews.md` section 12.1 ("the vendor orders are placed only when those [liens tagged `blocks-order`] are Closed") and SEMP section 3.4 line 106 ("CDR liens tagged `blocks-order` are Closed before any vendor order is placed"; "CDR is not closed with open PDR liens") are stricter, and section 12.2 lists "a cost above the owner's stated envelope at CDR" among items that may never be a lien. Fix: restate the policy as the 01 section 12 rule (PDR liens closed at CDR; `blocks-order` liens Closed before any order). | Lien | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | S2, CK-REQ-G3 | `schedule.md` lines 3 and 7 to 11 | Row 21 and row 19 cite G-4 items 14 and 15 ("Updated cost and schedule estimates", "Updated documentation of Basis of Estimate (cost and schedule)", corpus `npr-7123-1d/13-appendixg.md` line 80); the schedule gives durations (for example "Layout is the longest single task (Sat night)") with no basis, and its approval line does not cite the stakeholder input that records it (SI-020, `stakeholder-inputs.md` line 28, which the SEMP cites). Fix: add a one-line basis per phase (task list or prior run times) and cite SI-020 on the approval line. | Lien | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | R3 | author return | Iteration 2: no author self-check of `schedule.md` or `cost-estimate.md` against checklist sections G and A8, and no acceptance criteria, came with the fix commit `a7c70d2` or exist in the repository (claude-context search for an INSP-023 author self-check found only this record). Readiness R3 is not met and `readiness_met` is false. Fix: the plan author files the self-check with the next re-review brief, or Robin extends package decision 115 to this record. | Lien | Pending (decision 115) | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-G1, S2 | `schedule.md@53de92ae` section 3, DigiKey row | The RMM SWE-016 implementation names "PCBWay and DigiKey lead times"; the DigiKey row gives no duration ("no research finding records a delivery time, so the CDR order confirmation records it"), so the DigiKey lead time is deferred to CDR rather than estimated, and the zero-stock row is a decision, not a duration. Not Major: the DigiKey items ship to the owner and do not gate PCBWay assembly, and the row states its source gap honestly. Fix: give an estimated DigiKey delivery range with a source (distributor shipping policy, dated) before PDR, replaced by the order confirmation at CDR. | Lien | Pending | |

Finding rules as in the template. The reviewer writes `Pending` in the owner ruling column. "Lien" in the State column is the convergence-rule disposition "Lien: fix before PDR" (lien table below). "Verified" is a Major finding whose fix the reviewer confirmed on the committed blob. No finding is disputed. Iteration 2 added finding-8 and finding-9 (Minor); the diff of `a7c70d2` introduces no new Major defect.

### Lien table

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| finding-3 | Minor | Lien: fix before PDR | Cost estimate author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-4 | Minor | Lien: fix before PDR | Cost estimate author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-5 | Minor | Lien: fix before PDR | Schedule author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-6 | Minor | Lien: fix before PDR | Schedule author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-7 | Minor | Lien: fix before PDR | Schedule author (Claude, lead SE) | PDR readiness declaration | Routine item |
| finding-8 | Minor | Lien: fix before PDR (or owner waiver, decision 115) | Plan author (Claude, lead SE); Robin for a waiver | PDR readiness declaration | Routine item; R3 holds the record verdict at NEEDS CHANGES until closed or waived |
| finding-9 | Minor | Lien: fix before PDR | Schedule author (Claude, lead SE) | PDR readiness declaration | Routine item |

### Per-requirement validation

Not applicable: the products are plans, not requirement files (checklist product-type table).

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates | Yes (for the products) | Markdown plans with no `validate_docs.py` convention; `validate_docs.py` exit 0, 37 passed, 0 failed; `tpm.json` (which carries TPM-014 on the cost basis) passes its schema |
| R2 | traceability.py reports no violation for ids in the file | N/A | The plans carry no requirement ids; run: 0 violations, 2 warnings, neither attributable to these products |
| R3 | Author's self-check and acceptance criteria stated | No | No author return with a self-check against sections A to G is on record for `schedule.md` (`4e3f891`) or the `cost-estimate.md` revision (`b301df2`); the package names no record for either (section 6.15). Iteration 2: still none with `a7c70d2` (finding-8). `readiness_met` is false |
| R4 | TBR fields complete; no bare TBD | Yes | `grep -c "TBD\|TBR"` gives 0 in both committed blobs |
| R5 | CR impact assessment | N/A | Not a CR |

## Participants

Author (not present): Claude main session as lead SE. Reviewer: `reviewer:INSP-023`. Software assurance reviewer: not required; 07 section 2.1.1 row "Software plans" lists 07, the software section of `docs/vv/plan.md`, 03, 05 and TS-002, and does not list the section 6.1 records b and c (see cross item 3). Owner: dispositions the findings.

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 to CK-REQ-A7 | N/A | Plans: section G and A8 only (product-type table) |
| CK-REQ-A8 | Yes | Gate names SRR, PDR, CDR, TRR, SAR and "procurement release" as in charter section 3 line 37; "straight key" and "iambic paddles" are not used; "liens" as in 01 section 12; units USD throughout |

## B to F

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 | N/A | Requirement-file items; not applicable to a plan |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Checked against the charter (sections 3, 12), `rmm.json` SWE-015, SWE-016, SWE-151, SWE-174, 01 sections 4.3 and 12, 07 sections 1.3 and 22, SEMP (`77fc9ea4`) sections 3.4, 3.6, 5.0, 8.0 and appendix F F-13, `tpm.json` TPM-014 and MOP-016, `register.json` RSK-014, ADR-021, ADR-025, SI-020, SI-034, SI-035. Consistent: the cost figures (see S3), TPM-014 `cbe` 548 and `cbe_low_usd` 276 (1644 / 3 and 828 / 3), SEMP lines 45 and 415 totals, SEMP F-13 resolution, ADR-025 quantities (5 boards, 3 assembled), SI-034 instrument commitment, "vendor quotes replace estimates at PDR (enclosure) and CDR" as in the RMM SWE-015 residual risk and the TPM-014 margin policy; the schedule's gate order and event-based statement agree with charter section 3 and SEMP 3.4. Disagreements: finding-1 (RMM SWE-016, 07 section 22), finding-2 (RMM SWE-151 and SWE-015), finding-3 (01 row 19, TPM-014), finding-4 (SEMP section numbering), finding-5 (SEMP lines 128 and 204), finding-6 (01 section 12, SEMP 3.4) |
| CK-REQ-G2 | Yes | Each schedule row names the phase products and the gate; the cost model names its update points (every gate, quotes at PDR and CDR) and the TPM it feeds; no "as appropriate", "should consider" or TBD |
| CK-REQ-G3 | Yes (with finding-7) | Schedule: owner approval 2026-09-25 (SI-020 records it), owner review windows per gate, owner decision for long-lead substitutions; cost: owner commitment of the instrument (SI-034, ADR-021), ceiling set by the owner at SRR (TPM-014 TBR, package decision 90) |
| CK-REQ-G4 | Yes (iteration 2) | Iteration 2: `schedule.md@53de92ae` states it is the SWE-016 (T) software schedule and carries the RMM content (finding-1 Verified); `cost-estimate.md@0dda83cb` now carries the rework spin and spares the RMM SWE-151 row claims (finding-2 Verified). Iteration 1 (No): the cost model cites its tailoring ("Tailored replacement for NPR 7150.2D SWE-015/SWE-151 (see `docs/process/rmm.json`)", line 3), but it does not implement what the RMM rows say (finding-2). The schedule mirrors no tailoring: SWE-016 (T) is not mentioned and its "Planned for SRR" content is absent (finding-1) |
| CK-REQ-G5 | N/A | No cybersecurity content in scope; SWE-151 d cybersecurity cost is recorded as zero in the RMM rationale |
| CK-REQ-G6 | No | Cost: measure TPM-014 with source (`cost-estimate.md`), thresholds (`threshold_yellow`, `threshold_red`) and storage (`tpm.json` history), consistent. Schedule: no status or slip measure although SEMP line 204 defines one (finding-5) |
| CK-REQ-G7 | N/A | Neither product makes a tool claim |
| CK-REQ-G8 | Yes | NPR 7123.1D section 5.1.5 (schedule line 3) is accurate: "Life-cycle reviews are event-based and occur when the entrance criteria for the applicable review are satisfied" (`npr-7123-1d/05-chapter5.md` line 40). SWE-015 (3.2.1) and SWE-151 (3.2.2) exist (`npr-7150-2d/03-chapter3.md` lines 95 and 105); SWE-015 b ("One software cost estimate model ... less than $2 million", line 99) supports the single-model rationale of the RMM. No SE-NN or 47 CFR citation appears in either product. SWE-016 (3.3.1, line 125) verified before use in this record |

## Supplementary items (minimum content judged for SRR)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| S1 | Row 19: cost table with basis, covering BOM, fabrication, assembly, CNC, shipping, contingency (G-4 items 14, 15) | Yes (finding-2 Verified at iteration 2; finding-3 lien) | Cost table lines 7 to 18 covers fabrication, assembly with parts, CNC enclosure, non-sourced items, contingency 20 %, instrument; shipping partial (finding-3); life-cycle scope short of the RMM claim (finding-2) |
| S2 | Row 21: milestone list to PDR and the Phase B technical plan (G-4 item 22) | Yes at iteration 2 (finding-7, finding-9 liens); iteration 1 No (Major gap) | Phase B plan: SEMP section 3.4 table PDR row and "Target schedule and liens" paragraph (lines 92, 106) exist. Milestone list: gate rows only, no firmware milestones, dependencies or separate lead times (finding-1); no basis (finding-7) |
| S3 | Arithmetic of the cost model | Yes | Low: 60 + 300 + 250 + 80 = 690; 690 x 0.2 = 138; 690 + 138 = 828; 120 x 0.2 = 24; 828 + 120 + 24 = 972. High: 120 + 500 + 600 + 150 = 1370; 1370 x 0.2 = 274; 1370 + 274 = 1644; 160 x 0.2 = 32; 1644 + 160 + 32 = 1836. Per unit 276 to 548 (three units), equal to TPM-014 and package decision 90 |

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 2 plans, 20 lines each (5 schedule rows, 10 cost rows) |
| Items checked | 12 (A8, G1 to G8, S1 to S3), plus R1 to R5 |
| Items answered No | Iteration 2: 3 (G1, G6, R3); iteration 1: 4 (G1, G4, G6, S2) |
| Items N/A | A1 to A7, B to F, G5, G7 |
| Findings by severity | Major 2, Minor 7 (finding-8, finding-9 added at iteration 2) |
| Findings verified, deferred | 2 (finding-1, finding-2), 0 (7 Minor dispositioned Lien: fix before PDR) |
| Iteration | 2 |
| Effort | 42 turns, 55 minutes (iteration 1: 30 turns, 40 minutes) |

## Cross items (outside the scope of this record; reported to the lead SE)

1. `docs/process/rmm.json` SWE-016 item d says "No cross-project dependencies exist"; the rustos upstream work packages (SI-033, 07 section 19) are one. SWE-015 implementation still reads "optional instrument (SI-021)". Iteration 2: still open (rmm.json last changed at `ae8abd2`, before `a7c70d2`); `schedule.md` section 2 now records the rustos dependency as SWE-016 d, so the RMM row contradicts its implementing product until corrected and re-rendered. The SWE-016 "Planned for SRR" status can move to In place with the same change.
2. `docs/process/07-software-engineering-plan.md` section 22 SWE-016 row (line 827) says "milestone list without dates", while the RMM SWE-016 implementation and `schedule.md` carry the owner's target dates (SI-020).
3. 07 section 2.1.1 does not say whether the section 6.1 records b and c (schedule, cost estimate) need the software assurance review; this record assumed No.
4. Package section 4 rows 19 and 21 are rated Met with no review record; with finding-1 and finding-2 open they meet the package's "Partially met" definition (both rows are Soft, so a lien is possible once the Major findings close).

## Verdict

Iteration 2 (2026-09-26, HEAD `a7c70d2`, schedule blob `53de92ae`, cost blob `0dda83cb`): finding-1 and finding-2 Verified; findings 3 to 7 stay Lien: fix before PDR; finding-8 (R3) and finding-9 (DigiKey lead time) added as Minor liens. No Major finding is open and the diff introduces no new Major defect. reviewer_verdict APPROVED (with liens); the record verdict is held at NEEDS CHANGES only by readiness R3 (finding-8, decision 115), because `tools/validate_docs.py` refuses APPROVED with `readiness_met: false`; it turns APPROVED (with liens) on re-issue once the self-check is filed or Robin waives it. Package rows 19 and 21 may be rated Met with liens once the record is APPROVED.

```
VERDICT: NEEDS CHANGES (readiness R3 only; reviewer_verdict APPROVED with 7 liens)
PRODUCTS: docs/plan/schedule.md@53de92ae211105127f56103d26884d14342190d0, docs/plan/cost-estimate.md@0dda83cbd5ada9474562cc1741df67a31e1a7ffb (HEAD a7c70d2)
FINDINGS:
- [Major] finding-1 CK-REQ-G1, G4, S2: fixed at a7c70d2, Verified.
- [Major] finding-2 CK-REQ-G1, G4, S1: fixed at a7c70d2, Verified.
- [Minor] finding-3 to finding-7: Lien: fix before PDR.
- [Minor] finding-8 R3: no author self-check. Lien: fix before PDR (decision 115).
- [Minor] finding-9 CK-REQ-G1, S2 schedule.md section 3: DigiKey lead time not estimated. Lien: fix before PDR.
MEASUREMENTS: iteration=2; major=2; minor=7; verified=2; lien=7; open_major=0; turns=42; minutes=55
```

Iteration 1 (2026-09-26, HEAD `adcfe09`):

```
VERDICT: NEEDS CHANGES
PRODUCTS: docs/plan/schedule.md@2773cfb109cf1715bb4cb20f5e9faeb89274728e, docs/plan/cost-estimate.md@1fcb9ece64e111342e37e391c808f0955eb18090 (HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1)
FINDINGS:
- [Major] CK-REQ-G1, G4, S2 schedule.md: firmware milestones, dependencies (including rustos) and separate lead times that RMM SWE-016 plans for SRR are absent.
- [Major] CK-REQ-G1, G4, S1 cost-estimate.md: rework spin, spares and full shipping that RMM SWE-151 records as In place are not in the model; rev B not covered by contingency (RSK-014).
- [Minor] S1 cost-estimate.md lines 9 to 12: shipping and duties per line, parts markup basis, sources and dates. Lien: fix before PDR.
- [Minor] CK-REQ-G1 cost-estimate.md line 15: SEMP section 7 should be section 8.0. Lien: fix before PDR.
- [Minor] CK-REQ-G6 schedule.md: no status, slip or recovery for the passed SRR target; risks without RSK ids. Lien: fix before PDR.
- [Minor] CK-REQ-G1 schedule.md line 20: lien policy looser than 01 section 12 blocks-order rule. Lien: fix before PDR.
- [Minor] S2 schedule.md: no schedule basis of estimate; SI-020 not cited. Lien: fix before PDR.
ITEMS N/A: CK-REQ-A1 to A7, B to F (plan), CK-REQ-G5, CK-REQ-G7
MEASUREMENTS: size=2 plans, 40 lines; items=12; no=4; turns=30; minutes=40; major=2; minor=5; lien=5; open_major=2; iteration=1
```

## Author self-check (written by the author; package item R7, readiness R3, finding-8)

**Ownership.** This section is the author's return for readiness R3 of the requirements checklist ("The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"), filed in the record because 01 section 13 keeps no record only in conversation. It is written by `author:plan` (Claude, lead SE), not by the reviewer. The author changed nothing else in this record: the front matter, findings, readiness answers, verdict and measurements stay the reviewer's. Whether R3 is now met and finding-8 closes, and the re-issue of the record, are the reviewer's (package item R8). No product content changed with this self-check (convergence rule, charter section 4 item 3).

**Products checked.** `docs/plan/schedule.md@53de92ae211105127f56103d26884d14342190d0` and `docs/plan/cost-estimate.md@0dda83cbd5ada9474562cc1741df67a31e1a7ffb` (`git rev-parse HEAD:<path>` at HEAD `d4cce27`; last commit `a7c70d2`), the blobs of iteration 2. Date 2026-09-26. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ("author self-check readiness fields R1 to R4 peer review record"; "author self-check section filed by the author against checklist, acceptance criteria listed, decision 115") ran before any `grep`.

**Acceptance criteria.** The author briefs of `4e3f891`, `b301df2` and `a7c70d2` are not in the repository, so the criteria are restated from the governing sources they pointed to:

| # | Acceptance criterion | Source |
|---|---|---|
| AC-1 | Cost table with basis covering BOM, fabrication, assembly, CNC, shipping and contingency | 01 section 4.3 row 19 (G-4 6.14, 6.15) |
| AC-2 | Milestone list to PDR within the Phase B technical plan | 01 section 4.3 row 21 (G-4 6.22) |
| AC-3 | Schedule carries the SWE-016 (T) content: gates with target dates, firmware milestones, dependencies (including rustos, SWE-016 d) and separate lead times | `docs/process/rmm.json` SWE-016 |
| AC-4 | Cost model carries the SWE-015 and SWE-151 (T) content: labor-free, full life cycle (rework spin, spares), risk and other direct costs | `docs/process/rmm.json` SWE-015, SWE-151 |
| AC-5 | Unit budget equals the TPM-014 basis and the SEMP totals | `docs/plan/tpm.json` TPM-014; SEMP section 8.0 |
| AC-6 | No TBD, no em dash; reviews event-based | charter sections 3 and 7; NPR 7123.1D section 5.1.5 |
| AC-7 | Only Major findings change the products before SRR; Minor findings are liens due PDR | charter section 4 item 3 (lead SE convergence rule, 2026-09-26) |

**Self-check against the checklist.** `docs/templates/peer-review-checklist-requirements.md` revision C, product type "Plans and process documents": section G (all items) and A8; sections A1 to A7 and B to F are N/A for a plan.

| Item | Author answer | Evidence |
|---|---|---|
| R1 | Yes | Markdown plans with no schema; `tools/validate_docs.py` exit 0 (run with this self-check) |
| R2 | N/A | No requirement ids in either plan; `tools/traceability.py --report-only` exit 0, 0 violations |
| R3 | Yes (this section) | AC-1 to AC-7 and this table |
| R4 | Yes | `grep -c 'TBD\|TBR'` 0 in both blobs |
| R5 | N/A | Not a CR |
| CK-REQ-A8 | Yes | Gate names as charter section 3; USD throughout |
| CK-REQ-G1 | Yes, with liens | RMM SWE-016 and SWE-151 content now present (finding-1, finding-2 Verified). Accepted as liens due PDR: finding-3 (shipping and duties per line, sources and dates), finding-4 (line 15 "SEMP section 7" should read section 8.0), finding-6 (lien policy to the 01 section 12 `blocks-order` rule), finding-9 (DigiKey lead-time estimate). Known cross item outside these products: `rmm.json` SWE-016 item d and SWE-015 instrument wording (record cross item 1) |
| CK-REQ-G2 | Yes | Each FM-1 to FM-9 row names its gate, products and dependencies; each cost line names its basis and update point; 0 hits for "as appropriate", "should consider" or TBD |
| CK-REQ-G3 | Yes, with finding-7 as a lien | Owner approval, owner decisions for long-lead substitutions and the ADR draw rule of 06 section 14.1 class 2 for the reserves are stated; SI-020 citation and a per-phase basis are finding-7, due PDR |
| CK-REQ-G4 | Yes | `schedule.md` line 5 states it is the SWE-016 (T) schedule; `cost-estimate.md` line 3 cites the SWE-015 and SWE-151 tailoring and carries the life-cycle reserves |
| CK-REQ-G5 | N/A | No cybersecurity content |
| CK-REQ-G6 | No: lien | Cost: TPM-014 source and thresholds in `tpm.json`. Schedule: no actual, slip or recovery status and no RSK ids on the risk list; finding-5, due PDR |
| CK-REQ-G7 | N/A | No tool claim |
| CK-REQ-G8 | Yes | NPR 7123.1D section 5.1.5, SWE-015, SWE-016, SWE-151 exist in the corpus (reviewer pins, record section G) |
| AC-1, AC-4, AC-5 | Yes | Arithmetic recomputed today: 60 + 300 + 250 + 80 = 690, 690 + 138 = 828, 828 + 120 + 24 = 972, 972 + 300 + 40 = 1312; 120 + 500 + 600 + 150 = 1370, 1370 + 274 = 1644, 1644 + 160 + 32 = 1836, 1836 + 800 + 120 = 2756; per unit 276 to 548 for three units |
| AC-6 | Yes | Em dash 0 in both blobs; schedule gates event-based |

**Author statement.** The products meet AC-1 to AC-7 with the Minor liens finding-3 to finding-7 and finding-9 open, owned by the author and due at the PDR readiness declaration; finding-8 is answered by this section, for the reviewer to verify. No finding is disputed.
