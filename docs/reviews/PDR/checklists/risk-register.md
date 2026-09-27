---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/06-risk-and-decision-analysis.md section 16). Checklist:
# docs/templates/peer-review-checklist-risk.md revision A, section A, as PDR work plan WP-PDR-18 names.
# Iteration 1 reviews the WP-PDR-18 wave 0 product (the Track pass, commit 4df6606, register 0.7.0-pre-pdr).
# The final pass of wave 2 is a new product state and comes back to this record as iteration 2.
id: INSP-036
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/risk-register.md
product: docs/risk/register.json
# product_commit: the Track pass commit; the register blobs are unchanged from 4df6606 to HEAD 091bceb
product_commit: "4df6606ec6f32c1865a9d3e695c2629e1100e58d"
product_files: ["docs/risk/register.json@6685aa0eadc9e8bd806f1920e20d2209e8ae130e", "docs/risk/register.md@f8c28b363035cc3ce4cb15a5f7c0056f95febbf7"]
product_size: 65 active risks (32 Red) and 159 candidates; Track pass delta of 65 history entries, 9 field-level rewrites
sprint: PDR-prep
author_agent: "author:WP-PDR-18 wave 0 (Claude as risk manager)"
reviewer_agent: "reviewer:WP-PDR-18-risk-register"
# criticality neither for the register as a whole; the SWE-086 audit is item CK-RSK-A11, done by this reviewer
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: APPROVED with liens under plan rule C1 (Majors block; Minors are liens); no Major was found
verdict: APPROVED
findings_major: 0
findings_minor: 5
findings_open: 0
findings_fixed: 0
findings_verified: 0
# findings_deferred counts the five Minor liens (precedent INSP-007), due in the WP-PDR-18 final pass
findings_deferred: 5
deferred_rids: []
items_no: []
effort_turns: 38
effort_minutes: 55
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-036: risk register, WP-PDR-18 Track pass (iteration 1)

**Product reviewed (committed blobs, frozen per plan rule C2).**

| File | Blob | Commit | State |
|---|---|---|---|
| `docs/risk/register.json` (version 0.7.0-pre-pdr, updated 2026-09-27) | `6685aa0eadc9e8bd806f1920e20d2209e8ae130e` | `4df6606` (unchanged at HEAD `091bceb`) | committed |
| `docs/risk/register.md` (rendered) | `f8c28b363035cc3ce4cb15a5f7c0056f95febbf7` | `4df6606` (unchanged at HEAD `091bceb`) | committed; `render_risk.py --check` reports it current |

Previous register state: `4df6606^` (blob `0c25c0c5`, 0.6.0-pre-srr), the state INSP-007 iteration 3 re-issue 2 approved.

**Checklist applied.** `docs/templates/peer-review-checklist-risk.md` revision A, section A (CK-RSK-A1 to A11). Section B is N/A (the product is the register).

**Scope of this iteration.** `docs/plan/pdr-work-plan.md` WP-PDR-18 has two passes: the Track pass (wave 0, "first a Track pass before any overdue count", C-142) and the final pass (wave 2, after WP-PDR-16 and 19 to 27). This iteration judges the Track pass product against section A and against INSP-007 finding-18, the item it closes. The WP outputs that the plan places after the Track pass are not yet in the product and are not findings here: REQ or HZ links on the 11 Red risks without one; S1 steps due PDR done or re-dated; RSK-009 closure S2 to S4 with the PAT-071 step; RSK-013 re-score; enclosure candidates (coating adhesion, PETG creep, CR006-R1, CR006-R2); single-source list; SPF-to-risk mapping; cyber and interface risks; artifact-name reconciliation (design reader item 103); `docs/reviews/PDR/figures/risk-matrix.png`; 06 section 15 and 17 text fixes (C-140, C-141, INSP-007 finding-16 and finding-17); the 14-day trigger poll schedule; and the PDR-point Track pass that makes `--gate PDR` pass. The final pass returns to this record as iteration 2, a full section A review of the new state.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (queries: "WP-PDR-18 Risk register PDR Track pass reviewer checklist"; "frequency error budget 370 Hz guard keying sideband offset"). `grep -n` and read-only Python over the committed JSON were used afterwards only to pin lines and to run population checks.

**Independence (rule C4).** This reviewer invocation authored no part of the register, of the Track pass or of 06, and edited no product file. It wrote this record and the INSP-007 re-issue 3 delta only.

**Author summary (R4).** The author's return lists the risks changed: RSK-030 Accepted with its acceptance record; RSK-028 S2, RSK-030 S1, RSK-046 S1 Done; RSK-046 re-assessed on REQ-SYS-182; RSK-016 and RSK-008 notes; four conditions beyond finding-18 (RSK-024, RSK-052, RSK-057, RSK-014); 65 statuses set (55 Open, 9 Mitigating, 1 Accepted); CR-003 and CR-006 notes without value changes.

## Findings

Severity per the template: Major is a Red risk without the section 8 minimums, a hazard with unverified controls carried by no risk or with a one-way link, or a score that disagrees with the scales. Minor is wording, a missing citation, or an incomplete rationale that does not change a level. Under plan rule C1 every Minor finding is a lien, fixed in the WP-PDR-18 final pass (wave 2) and verified at iteration 2, at the latest by the CDR readiness declaration. History entries are append-only, so a fix to a history note is a new dated entry.

| Finding | Severity | Item | Location | Description and expected fix | State | Deferred to |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | Minor | CK-RSK-A3, CK-RSK-A4 | RSK-028 `statement.condition`, `likelihood_rationale`, `related.requirement_ids` | The Track pass restated the condition and rationale and kept the claim that the guest lock "is not yet a requirement" ("S1 due PDR"). The functional baseline already carries it at L1: REQ-SYS-065 "Guest lock transmit inhibit" and REQ-SYS-066 "Guest lock set and release", both Active at `baseline/srr`, sources ADR-015, OPS-019, hazard HZ-006. S1 derives the SW L2 requirement (`docs/requirements/sw/sw-txseq/`), which is still open. `related.requirement_ids` is empty. The level does not change: the control has no design, so 06 section 6 case (a) keeps level 3, as it does for RSK-046. Fix: say that the guest lock is required at L1 by REQ-SYS-065 and REQ-SYS-066 and that the SW L2 derivation and design are open (S1); add both ids to `related.requirement_ids`. This also clears RSK-028 from the 11 Red risks without a REQ or HZ link. If HZ-006 is to be linked, the back-link in `hazards.json` goes through the hazard writer (plan 5.3, WP-PDR-16b). | Lien | WP-PDR-18 final pass |
| <a id="finding-2"></a>finding-2 | Minor | CK-RSK-A3 (`related` consistency) | RSK-024 `statement.condition`, `related.requirement_ids` | The restated condition names the requirements that carry the HZ-004 controls (K4 to REQ-SYS-054 and REQ-SYS-184, K5 to REQ-SYS-055, K12 to REQ-SYS-180). These match `hazards.json` `control_req_ids`. But `related.requirement_ids` is empty, while the same pass added REQ-SYS-182 to RSK-046 on the same reasoning. Fix: add REQ-SYS-054, REQ-SYS-055, REQ-SYS-180 and REQ-SYS-184 to RSK-024 `related.requirement_ids`. | Lien | WP-PDR-18 final pass |
| <a id="finding-3"></a>finding-3 | Minor | CK-RSK-A10 | 2026-09-27 `history` notes of RSK-002, RSK-008, RSK-014, RSK-034, RSK-065 | Each note says "CR-006 revision 2 (Submitted, 39a6b13; section 1.7) proposes changes to this risk". CR-006 section 1.7 proposes changes only to RSK-004, RSK-052, RSK-038 (none to the text) and RSK-025. It says RSK-002, RSK-034 and RSK-065 "need no change" and keeps RSK-008 and RSK-014 "unchanged as conservative". The CR-003 notes are correct: they are on exactly the 11 risks of CR-003 section 4, Risk row (RSK-006, 007, 018, 025, 026, 030, 039, 043, 044, 052, 053). Fix: in the final pass entry of these five risks, record that CR-006 section 1.7 names them and proposes no change. | Lien | WP-PDR-18 final pass |
| <a id="finding-4"></a>finding-4 | Minor | CK-RSK-A8 | RSK-008 `likelihood_rationale` and `related.risk_ids` | The rationale says the risk is an "Aggregate of RSK-001, RSK-003, RSK-004, RSK-006, RSK-012, RSK-013, RSK-014, RSK-024 and RSK-027". `related.risk_ids`, which the tool uses, holds 13 children: those names without RSK-013, plus RSK-025, RSK-043, RSK-049 and RSK-064. The Track pass note repeats "Aggregate likelihood 4 equals the maximum of the active children", which holds for both lists (RSK-013 is at level 3). The discrepancy predates the Track pass: INSP-007 finding-5 added RSK-025 to the list without aligning the rationale. Fix: make the rationale name the `related.risk_ids` list, and either add RSK-013 as a child (a first-power-on risk: its first_power_on is 3) or remove it from the rationale. | Lien | WP-PDR-18 final pass |
| <a id="finding-5"></a>finding-5 | Minor | CK-RSK-A3 | RSK-014 `statement.condition` | The condition still says the owner approved "PDR on Saturday evening and CDR with procurement release on Sunday evening". The Track pass note records that the owner approved plan revision 2 dates on 2026-09-27 (status note section 4: readiness Tue 10-06, PDR about Thu 10-08, CDR about 10-14 to 10-15), which "relaxes the compressed PDR and CDR windows of this condition". The condition is therefore no longer a fact true today (06 section 4). The pass restated four other stale conditions but deferred this one, with the reason that the re-score waits for the updated `schedule.md` (WP-PDR-02, WP-PDR-46). The deferral of the score is sound. The condition text did not need to wait. Fix: restate the condition with the approved dates, and re-score on the updated schedule, as the note already plans. | Lien | WP-PDR-18 final pass |

### Risks passing the Analyze check (section A only)

This table is the 06 section 9 Analyze-row record at the path 06 names (`docs/reviews/<REVIEW>/checklists/risk-register.md`, `<REVIEW>` = PDR, the next gate). It confirms, on the Track pass blob, the INSP-007 result that the author used for the Proposed to Open move (see CK-RSK-A2). Method: the 56 risks whose non-history fields changed only in `status`, `trend` and `last_assessed` were checked by the tool, which covers statement parts, levels, score, band, plan minimums, triggers, the Low-confidence rule, the software-tag artifact rule, aggregates and hazard links, and by the population checks below. Their content is the content INSP-007 passed. The 9 risks with rewritten fields (RSK-008, 014, 016, 024, 028, 030, 046, 052, 057) were read in full against 06 sections 4 to 8 and against the decision memo rulings they cite. A finding against a risk is a Minor lien and does not change the pass.

| Risk | Passes (Yes or No) | Status after the Track pass | Finding ids |
|---|---|---|---|
| RSK-001 | Yes | Open | none |
| RSK-002 | Yes | Open | finding-3 |
| RSK-003 | Yes | Open | none |
| RSK-004 | Yes | Open | none |
| RSK-005 | Yes | Open | none |
| RSK-006 | Yes | Open | none |
| RSK-007 | Yes | Mitigating | none |
| RSK-008 | Yes | Mitigating | finding-3, finding-4 |
| RSK-009 | Yes | Mitigating | none |
| RSK-010 | Yes | Open | none |
| RSK-011 | Yes | Open | none |
| RSK-012 | Yes | Mitigating | none |
| RSK-013 | Yes | Mitigating | none |
| RSK-014 | Yes | Open | finding-3, finding-5 |
| RSK-015 | Yes | Mitigating | none |
| RSK-016 | Yes | Mitigating | none |
| RSK-017 | Yes | Open | none |
| RSK-018 | Yes | Open | none |
| RSK-019 | Yes | Open | none |
| RSK-020 | Yes | Open | none |
| RSK-021 | Yes | Open | none |
| RSK-022 | Yes | Open | none |
| RSK-023 | Yes | Open | none |
| RSK-024 | Yes | Open | finding-2 |
| RSK-025 | Yes | Open | none |
| RSK-026 | Yes | Open | none |
| RSK-027 | Yes | Open | none |
| RSK-028 | Yes | Mitigating | finding-1 |
| RSK-029 | Yes | Open | none |
| RSK-030 | Yes | Accepted | none |
| RSK-031 | Yes | Open | none |
| RSK-032 | Yes | Open | none |
| RSK-033 | Yes | Open | none |
| RSK-034 | Yes | Open | finding-3 |
| RSK-035 | Yes | Open | none |
| RSK-036 | Yes | Open | none |
| RSK-037 | Yes | Open | none |
| RSK-038 | Yes | Open | none |
| RSK-039 | Yes | Open | none |
| RSK-040 | Yes | Open | none |
| RSK-041 | Yes | Open | none |
| RSK-042 | Yes | Open | none |
| RSK-043 | Yes | Open | none |
| RSK-044 | Yes | Open | none |
| RSK-045 | Yes | Open | none |
| RSK-046 | Yes | Mitigating | none |
| RSK-047 | Yes | Open | none |
| RSK-048 | Yes | Open | none |
| RSK-049 | Yes | Open | none |
| RSK-050 | Yes | Open | none |
| RSK-051 | Yes | Open | none |
| RSK-052 | Yes | Open | none |
| RSK-053 | Yes | Open | none |
| RSK-054 | Yes | Open | none |
| RSK-055 | Yes | Open | none |
| RSK-056 | Yes | Open | none |
| RSK-057 | Yes | Open | none |
| RSK-058 | Yes | Open | none |
| RSK-059 | Yes | Open | none |
| RSK-060 | Yes | Open | none |
| RSK-061 | Yes | Open | none |
| RSK-062 | Yes | Open | none |
| RSK-063 | Yes | Open | none |
| RSK-064 | Yes | Open | none |
| RSK-065 | Yes | Open | none |

## Readiness criteria

| # | Criterion | Met | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | Met for the product; the repository run is not clean | Before this record: 52 passed, 2 failed, exit 1. The two failures are record drift in `docs/reviews/SRR/checklists/risk-register-06.md` (INSP-007, whose `product_files` still name register blobs `0c25c0c5` and `a3a983e5`; the Track pass changed them) and `tool-validation-tv-001-to-tv-010.md` (outside this product). The first is repaired by the INSP-007 re-issue 3 delta that this reviewer files with this iteration. The second belongs to the TV records. Neither is a defect of the register. |
| R2 | `render_risk.py --check` exits 0 | Met | "register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used"; "register.md is current"; exit 0 |
| R3 | Section B only | N/A | Product is the register |
| R4 | Author return lists the changed risks | Met | Author summary, and commit `4df6606` message with its `Refs:` trailer |

## A. Risk register (06 section 16, items 1 to 11)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-A1 | Yes (for the Track pass, gate SRR); `--gate PDR` is final-pass scope | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: "register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check", "register.md is current", exit 0. `--gate PDR --hazards`: 76 errors, "nothing written". They are 65 "last assessed at SRR, before the PDR Track pass (process section 10)" and 11 "Red risk has no REQ or HZ link at PDR or later (process section 11)" (RSK-002, 003, 004, 005, 008, 012, 014, 027, 028, 029, 063). The plan puts both sets in the final pass. The Track pass records `review: SRR` for the last gate passed, which the commit message states. The PDR-point pass comes at package assembly (06 section 10 item 1). No other error class appears: no `plan_approval`, score, band, trigger, aggregate or hazard-link error. |
| CK-RSK-A2 | Yes | No risk is Proposed: Open 55, Mitigating 9, Accepted 1 (population count on the blob). The Proposed to Open move cites INSP-007 CK-RSK-A2 (iteration 2: all 65 pass). INSP-007 added its own condition ("They may move to Open when the software lead sets the findings Verified"; its line 150), and INSP-007's `findings_verified` is still 0. The 06 section 9 transition table requires only "The reviewer's INSP record (Analyze row) passes the risk". This record re-performs the Analyze check at the path 06 names, and the table above passes all 65, so the transition has its record either way. Open to Mitigating was checked against the transition "first mitigation step is InProgress or Done". The 9 Mitigating risks each have one (RSK-007 S1, 008 S5, 009 S1, 012 S5, 013 S1, 015 S1, 016 S3, 028 S2, 046 S1). No Open risk has a step InProgress or Done. RSK-042, RSK-054 and RSK-057 are Open, not Watch, because their confirmation steps are Planned (06 section 8, Watch row). |
| CK-RSK-A3 | Yes (with finding-1, finding-2, finding-5) | Rewritten conditions checked against their sources. RSK-008: decision 11, memo line 220 "Accept at SRR and reconfirm in the CDR memo" and line 378. RSK-024: decisions 37 and 38 (memo lines 208 and 211); `hazards.json` HZ-004 K4 `control_req_ids` [REQ-SYS-054, REQ-SYS-184], K5 [REQ-SYS-055], K12 [REQ-SYS-180]; OQ-SAF-003 Closed. RSK-028: decisions 17, 19, 20 (memo lines 223, 225, 226) and ADR-015 Status "Accepted"; finding-1. RSK-030: decision 32 (line 221) and RFX-D6. RSK-046: REQ-SYS-008 and REQ-SYS-009 read 144.0012 to 147.9988 MHz (TBR); decision 25 (line 250); ADR-023 Status "Accepted"; REQ-SYS-182 Active with 10 kHz and 100 ms TBR; HZ-008 K7 lists REQ-SYS-182; OQ-SAF-013 Closed. RSK-052: decision 90 (line 251) and REQ-SYS-147 "at most USD 610 (TBR)". RSK-057: decision 29 (line 249) and ADR-022 Status "Accepted". Each still states one departure and a cited condition, with no solution language. RSK-014: finding-5. |
| CK-RSK-A4 | Yes (with finding-1) | RSK-046 names case (a) and level 4 on "no analysis": REQ-SYS-182 is a requirement, not an analysis. This matches the 06 section 6 case (a) rule ("no analysis gives 4"). Its trigger threshold of +/-370 Hz is still right under the 1.2 kHz guard: it is the reference error term of the REQ-SYS-008 rationale (750 + 370 = 1120 Hz), not the guard. RSK-028 keeps anchor 3. Its premise is corrected by finding-1, and the level does not change. RSK-030 keeps its case (b) band argument at level 2, confidence Medium. No level or consequence value changed in the pass. The last `history` entry of every risk equals its current L, max(C), safety, score and status. `trend` moved from Increasing or New to Stable on 18 risks, which is the value 06 section 11 computes from two equal last history scores. |
| CK-RSK-A5 | Yes | 32 Red risks, all strategy Mitigate, each with at least two active steps, a fallback, at least one trigger and `plan_approval` (SRR decision memo, 2026-09-26). RSK-008 stays Red and Mitigating after decision 11 (06 section 8 Red row: never Accept while active). The note explains this correctly. |
| CK-RSK-A6 | N/A at this iteration (the rule applies from PDR; final-pass scope) | 11 Red risks have no REQ or HZ link (list in CK-RSK-A1), the number the plan names ("the 11 Red risks lacking them"). finding-1 gives the link for RSK-028. |
| CK-RSK-A7 | Yes | Hazard cross-check passes. RSK-030 moved to Accepted, which stays active for the hazard link rule (`tools/render_risk.py` line 67: `INACTIVE = {"Closed", "Retired"}`), so HZ-001 is still carried by RSK-016 and RSK-030 both ways. This answers INSP-007 cross item (3). Every hazard lists at least one risk (HZ-001 to HZ-015 `related_risk_ids`), and each listed risk carries the hazard back. |
| CK-RSK-A8 | Yes (with finding-4) | One aggregate (RSK-008): likelihood 4 equals the maximum of its 13 active children. The rationale's child list disagrees with `related.risk_ids` (finding-4). |
| CK-RSK-A9 | Yes | Low confidence: RSK-007, RSK-034, RSK-065, each under Mitigate with steps, unchanged by the pass and accepted by the tool's Low-confidence rule. |
| CK-RSK-A10 | Yes (with finding-3) | There is no PDR package yet (WP-PDR-48). The changes in the commit `4df6606` message and its `Refs:` trailer match the history entries: one entry per risk, dated 2026-09-27, review SRR, no earlier entry rewritten (checked by comparing every `history[:-1]` with `4df6606^`), no em dash in either file. `candidates` is unchanged (159). The candidates named in artifacts committed since SRR are the CR-003 section 4 candidates (a) to (e) and CR-006 CR006-R1 and CR006-R2. They sit in Submitted CRs that change no baseline until disposition, and the plan assigns them to the final pass ("enclosure candidates"). Their disposition is due there, and iteration 2 checks it. |
| CK-RSK-A11 | Yes (Track-pass scope) | 30 software risks (14 category software, 16 tagged; `register.md` summary row "Software risks (SWE-086 record ...)"), each with a 2026-09-27 Track entry. Six steps: record (register), analysis (INSP-007 and this record), plan (steps with due gates; RSK-009 S2 to S4 due PDR, final pass), tracking (history entry, `last_assessed`), control (status transitions above), communication (PDR package risk section, WP-PDR-48, not yet due). The 07 sections 16.2 and 21 risks that INSP-007 finding-3 required are still present: RSK-060 to RSK-063, and the cyber list RSK-015, 022, 060, 061, 062. Measures table: not due until the PDR package. |

ITEMS N/A: CK-RSK-B1 to CK-RSK-B10 (the product is the register); CK-RSK-A6 at this iteration (final-pass scope).

## Checks of every case finding-18 and the Track pass name (rule C7)

| Case | Required by | Result |
|---|---|---|
| (a) RSK-030 Accepted with `acceptance` {memo, 2026-09-26, residual 4} | INSP-007 finding-18 (a); 06 section 8 Acceptance | Done. `acceptance` = {`docs/reviews/SRR/decision-memo.md`, 2026-09-26, 4}; `score` 4 (L2 x C2); the tool checks residual = score. The strategy was Accept (Green), so the band table allows it. Both triggers are kept, and they re-open the risk. S2 (reference antenna, due PDR) stays Planned, which is allowed for an Accepted risk. |
| (b) RSK-028 S2, RSK-030 S1, RSK-046 S1 Done with the memo as evidence | finding-18 (b) | Done. Each step names the memo section and decision with the quoted ruling. RSK-030 S1's "the evaluation cites the acceptance" clause moved to a new S3 (due PDR, artifact `docs/design/analysis/rf-exposure-evaluation.md`). The move is honest because that document is a PDR product. No SRR-due step is left Planned or InProgress in the register (population check), so the PDR overdue count is zero for SRR steps. |
| RSK-046 re-assessed on REQ-SYS-182 | finding-18 fix | Done. Re-assessed, level 4 kept with the case (a) reason, REQ-SYS-182 added to `related`, and the 1.2 kHz guard in the condition. |
| (c) RSK-008 decision 11 note | finding-18 (c) | Done. There is a dated note, and the condition carries "the owner accepted this residual at SRR, decision 11 (OQ-SE-006), to be reconfirmed in the CDR decision memo". |
| RSK-016 and RSK-046 rationale "in the past tense" | finding-18 fix | RSK-046 done. For RSK-016, the future-tense wording INSP-007 quoted ("owner decision 17 disposes ADR-015") is in a 2026-09-25 history note, not in the rationale, which is unchanged and has no tense issue. The Track entry records decisions 17 to 20 in the past tense. History is append-only, so this is the correct fix. |
| (d) all 65 statuses set | finding-18 (d) | Done (CK-RSK-A2). |
| The four conditions beyond the finding-18 list (RSK-024, RSK-052, RSK-057, RSK-014) | Author summary | RSK-024, RSK-052 and RSK-057 are correct against their rulings (CK-RSK-A3). RSK-024 relates to finding-2 and RSK-014 to finding-5. |
| Other rulings of memo line 378 and the consent agenda | Completeness | RSK-010 (decisions 6 and 8): the condition already reads "approved by the owner at SRR", as INSP-007 re-issue 2 found. No change is needed. RSK-058, RSK-039, RSK-040, RSK-059, RSK-015, RSK-022 (decisions 55, 66, 68, 85, 95): their steps already state the ruled direction. A pattern scan of every active risk for pending-SRR wording ("decides at SRR", "proposed decision", "pending the owner") found nothing further. |
| CR-003 and CR-006 notes, values unchanged | Rule C8 (AT RISK) | CR-003: correct set (finding-3 table). CR-006: over-inclusive wording on five risks (finding-3). No value was changed ahead of the dispositions. |

## Tool runs (2026-09-27, HEAD `091bceb` (re-checked at `bfed1b0`), register blobs identical to `4df6606`)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before this record) | 1 | 52 passed, 2 failed (INSP-007 drift, TV-001 to TV-010 drift; see R1) |
| `.venv/bin/python tools/render_risk.py --check` | 0 | 65 risks, 159 candidates, 0 warnings; register.md current |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | hazard cross-check passes |
| `.venv/bin/python tools/render_risk.py --check --gate PDR --hazards docs/safety/hazards.json` | 1 | 76 errors, the expected final-pass set (CK-RSK-A1) |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 unallocated); `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout` |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 453 tests, 1 failure `test_repository_exit_zero` (the repository-wide `validate_docs.py` result of R1), 11 skipped |

No figure is part of the Track pass product (the matrix figure `docs/reviews/PDR/figures/risk-matrix.png` is final-pass output), so rule C5 has nothing to render at this iteration.

## Cross items (outside the product; for Claude to route)

1. `docs/safety/hazards.json` HZ-008 K7 `text` still says REQ-SYS-182 is "Draft", while REQ-SYS-182 is Active. This is for the hazard writer (WP-PDR-16b).
2. INSP-007 `findings_verified` is 0 and its `record_status` is Open. The software lead sets the Fixed findings Verified and, once finding-16 and finding-17 are fixed in 06 (C-140, C-141), closes the record.
3. If RSK-028 is linked to HZ-006 (finding-1), `hazards.json` HZ-006 `related_risk_ids` needs RSK-028 for the two-way rule (WP-PDR-16b).

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien | Risk manager (WP-PDR-18) | WP-PDR-18 final pass; verified at iteration 2 |
| finding-2 | Minor | Lien | Risk manager (WP-PDR-18) | WP-PDR-18 final pass; verified at iteration 2 |
| finding-3 | Minor | Lien | Risk manager (WP-PDR-18) | WP-PDR-18 final pass; verified at iteration 2 |
| finding-4 | Minor | Lien | Risk manager (WP-PDR-18) | WP-PDR-18 final pass; verified at iteration 2 |
| finding-5 | Minor | Lien | Risk manager (WP-PDR-18) | WP-PDR-18 final pass; verified at iteration 2 |

## Completion criteria (SWE-088 b, c)

The readiness criteria that apply were met for the product. Every applicable item is answered. CK-RSK-A6 and section B are N/A with the reason given. There are zero Major findings. The five Minor findings are liens with an owner and a due event under plan rule C1 and the convergence rule (charter section 4 item 3). The measurements are in the front matter. `validate_docs.py` passes on this record.

## Verdict (returned by the reviewer)

```
VERDICT: APPROVED (with liens; iteration 1, Track pass, blobs register.json 6685aa0e, register.md f8c28b36)
FINDINGS:
- [Minor] CK-RSK-A3/A4 RSK-028: condition and rationale say the guest lock is not yet a requirement; REQ-SYS-065 and REQ-SYS-066 are Active at baseline/srr; related.requirement_ids empty.
- [Minor] CK-RSK-A3 RSK-024: condition names REQ-SYS-054, 055, 180, 184; related.requirement_ids empty.
- [Minor] CK-RSK-A10 RSK-002, 008, 014, 034, 065 history notes: CR-006 section 1.7 proposes no change to these risks.
- [Minor] CK-RSK-A8 RSK-008: rationale child list (with RSK-013) differs from related.risk_ids (13 children, without RSK-013).
- [Minor] CK-RSK-A3 RSK-014: condition keeps the superseded Saturday and Sunday gate windows.
ITEMS N/A: CK-RSK-B1 to CK-RSK-B10 (product is the register); CK-RSK-A6 (applies from PDR; final-pass scope)
MEASUREMENTS: size=65 risks, 159 candidates; turns=38; minutes=55; major=0; minor=5
```
