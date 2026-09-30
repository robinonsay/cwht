---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, row "Change Requests that touch
# requirements": sections A to F for every added or changed requirement, B7, readiness R5 and one
# per-requirement validation row per added or changed requirement.
# This record is the INSP-003 delta iteration that PDR work plan WP-PDR-11 names ("Reviewer: INSP-003 and
# INSP-025 delta iterations"), filed under PDR per plan section 3.1 "Records". Its companion for the TC-SYS
# cases (the INSP-025 delta) is docs/reviews/PDR/checklists/cr-008-test-sys.md (INSP-045).
# The product is CR-008 (Submitted, proposed Class I), prototyped on branch
# cr/CR-008-srr-liens-l1-and-tc-sys at c629198 and frozen there (plan rule C2).
# Iteration 2 (2026-09-27, main ae29a98): delta under plan rule C1 on the drift of the CR file only,
# 3b9266ff (4dab5dc) to 5e6ceb62 (cccbfda section 6.1 impact review round 1, blob ade26204; a244b05
# revision 2, blob 5e6ceb62). The four branch blobs at c629198 are unchanged and remain the frozen product.
# CR file re-pin delta (2026-09-29, main 0680af9; WP-PDR-55): delta under plan rule C1 on the drift of the CR file,
# 5e6ceb62 (a244b05) to aa65e826 (6485bd3 section 6.3, a17af87 disposition, 9c40ef9 and 726cd44 sections 5, 8, 9);
# the CR sections this record reviewed changed (section 5 Done cells; front matter status), so a delta, not a removal.
# Iteration stays 2: a re-pin delta is not a new review iteration (INSP-003 convention).
# Status re-pin delta (2026-09-29, main 9fda694; WP-PDR-55; lead SE rulings 1 and 2): delta on the two CR-008 section 5
# step 10 blobs at c1955b3 (REQ-SYS-194 Draft to Active) and on the CR file aa65e826 to c1a52ab6 (b630269, 1fe68cb). The
# CR sections this record reviewed changed (section 5 step 10 and the frozen-products paragraph; front matter status), so a
# delta was done first; after it, the CR file is dropped from product_files (ruling 2, INSP-060 precedent; reason in the section).
id: INSP-044
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/cr-008-requirements-sys.md
product: CR-008
# product_commit: the branch head that holds the frozen blobs (base ab2af2d on main); the CR file is on main at a244b05 (iteration 2)
# re-pin delta: product_commit stays c629198 (the four frozen blobs, equal at the branch head e26ce46); the CR file is on main at 726cd44
# status re-pin delta: product_commit is c1955b3, the branch commit of step 10 (the two new requirement blobs; the two case
# blobs equal c629198; equal at the branch head 92727f1); was c629198. The CR file is on main at 1fe68cb (blob c1a52ab6)
product_commit: "c1955b34695949bae86b02d5728a3c7f28f50b55"
# product_files at iteration 2: the four as below and docs/cm/cr/CR-008-srr-liens-l1-and-tc-sys.md@5e6ceb627a75e769d9898c107b9e87e3bb152f69
# product_files at the re-pin delta: requirements.json@a73449377e8d055f5d247130b8850bf3f5a151d9, requirements.md@4e110b16027fbe446e846a8c5f9d2dc5c2899af6,
# the two case blobs as below, and docs/cm/cr/CR-008-srr-liens-l1-and-tc-sys.md@aa65e8261da4193707b561dba6e8a841451cf88f
# status re-pin delta: the two requirement blobs are the step 10 blobs (git rev-parse c1955b3:<path>); the CR file entry is
# dropped (lead SE ruling 2). The CR is a record on main whose sections 5 (Done cells) and 8 to 11 and whose front matter
# (status, merge_sha) change again at the merge, so a pinned CR blob cannot equal HEAD when the merge commit sets the verdict.
# The reviewed CR text stays identified in the body: blob c1a52ab6 (section "Status re-pin delta")
product_files: ["docs/requirements/sys/requirements.json@c68584cf62895a6b0a6d4a5d45e19fd190dd1af1", "docs/requirements/sys/requirements.md@47c2beaacc2037d08011b56b36efde90c4f334f0", "docs/test_cases/sys/test_cases.json@117c08dedd65171f88d5bff015d0914db97b3065", "docs/test_cases/sys/test_cases.md@00e4454f5c836df0eac430b9ec9f95b99630d316"]
product_size: 145 requirements added or changed (1 added, 14 statements, 55 rationales, 10 notes, 40 source_ids, 104 tbr objects); 191 entries, 189 live
sprint: PDR-prep
author_agent: "author:WP-PDR-11 (L1 requirements author and TC-SYS test author, one invocation; CR-008 section 4 independence note)"
reviewer_agent: "reviewer:WP-PDR-11-INSP-003-delta"
# criticality and assurance: the SYS L1 file is a system requirements file, not a software requirement
# file of 07 section 2.1.1 (as INSP-003): no software assurance pair
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES on the completion criterion "validate_docs.py passes on the record" only.
# The reviewed blobs are on the CR branch, not in main HEAD; tools/validate_docs.py fails an APPROVED
# record whose product_files are not in HEAD (record drift rule). The software lead sets APPROVED when
# CR-008 merges with these blobs unchanged (section "Record verdict"; precedent INSP-031). Iteration 2 keeps the
# hold: the four requirement and test-case blobs are still only on the unmerged branch (lead SE convention).
# The re-pin delta keeps the hold for the same reason. The status re-pin delta keeps it too: the two step 10 blobs exist only
# on the branch.
verdict: APPROVED
# re-pin delta counts: finding-1 Open to Lien (rule C1: CR-008 dispositioned Approved on 2026-09-28 without a revision;
# due at the CDR readiness declaration), counted in findings_deferred; finding-2 new, Minor, Open (fix before the merge,
# record text only). Was minor 1, open 1, deferred 0
# status re-pin delta counts: finding-2 Verified (CR-008 section 10 cell fixed at 1fe68cb); finding-1 stays a Lien; no new
# finding. Was open 1, verified 0
findings_major: 0
findings_minor: 2
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 1
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-D4]
# effort: iteration 1 (60 turns, 120 min) plus iteration 2 delta (14 turns, 25 min) plus the re-pin delta (12 turns, 25 min)
# plus the status re-pin delta (16 turns, 30 min)
effort_turns: 102
effort_minutes: 200
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-044: CR-008, L1 requirement liens of INSP-003 (WP-PDR-11, INSP-003 delta)

**Product.** CR-008 (`docs/cm/cr/CR-008-srr-liens-l1-and-tc-sys.md`, blob `3b9266ff` on `main` at `4dab5dc`, Submitted, proposed Class I) and its prototype on branch `cr/CR-008-srr-liens-l1-and-tc-sys` at `c629198` (base `ab2af2d`). Blob identity: `git rev-parse c629198:<path>` for the four product files and `main:` for the CR equal the brief exactly. `git diff --name-only ab2af2d c629198` lists only the four product files; on `main` the four files are byte-equal to `baseline/srr` (no commit between `baseline/srr` and `main` touches `docs/requirements/sys/` or `docs/test_cases/sys/`), so the diff reviewed is `baseline/srr` to `c629198`.

**Checklist.** `docs/templates/peer-review-checklist-requirements.md` revision C, row "Change Requests that touch requirements": A to F for every added or changed requirement, B7, R5 and one per-requirement validation row each. Section G is N/A (not a plan). C4 (SW-SAFE), C7, C8 and D1 to D3 carry no L1 content changed by this CR.

**Acceptance criteria (rule C7, every case the governing clauses enumerate).** Each lien of INSP-003 carried by WP-PDR-11 (plan section 3.4: C-019 to C-025): finding-12 and finding-30 (all 189 live rationales), finding-25 (fourteen requirements, ten cases), finding-26 (seven named requirements plus REQ-SYS-010), finding-27, finding-28, finding-29 items (i) to (iii), finding-31 items (i) and (ii); L-7 of RFA-SRR-007 (the eight named requirements and the stated rule over every Accepted ADR section 4.1 row); INSP-025 cross items X1, X5, X6, X8 on the requirement side; RID-SRR-003 content and TBR finding 7 (REQ-SYS-054 wording); and every item of CR-008 section 5 "Verification of the implementation" that concerns the L1 file. The TC-SYS side is verified in INSP-045.

**Independence (rule C4).** This invocation authored no part of WP-PDR-11, CR-008 or the branch, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried before any manual search (queries: "WP-PDR-11 SRR liens L1 requirements TC-SYS reviewer checklist"; "REQ-SYS-054 stale 30 s wording decision 37 RID-SRR-003 TBR finding 7"; "TBR closure map reader finding REQ-SYS-054 30 s wording"; "2S charger selection D-PWR-01 per-cell balancing overvoltage charger part"); `grep -n` was used afterwards only to pin lines. **Method.** Field-by-field diff of `baseline/srr` against `c629198` by script (every key of every entry), word counts and label order by script over every live entry, ADR section 4.1 rows parsed from every file in `docs/decisions/adr/`, tool runs on an export of `c629198` in the scratchpad (`git archive`), never on the shared tree.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-D4 (INSP-003 finding-25 class) | REQ-SYS-167 `description` (also REQ-SYS-089, unchanged by the CR); TC-SYS-065 `acceptance_criteria` | CR-008 turns "refuse", "stop" and "pause" charging into a measurable level (charge current below 5 mA) in REQ-SYS-087, 088 and 093, but REQ-SYS-167 ("shall stop charging when its constant-voltage charge current falls by less than 20 mA ...") and REQ-SYS-089 ("shall stop any charge that lasts longer than 15 h") keep "stop charging" with no level. Their closing case TC-SYS-065, which the CR edits, now supplies the level itself: "charging stopped means a charge current below 5 mA, the level of REQ-SYS-087, 088 and 093". That is the pattern INSP-003 finding-25 recorded (a pass/fail value set in the case, taken from a sibling), now introduced in a case this CR amends. Minor, as finding-25 was: the value is narrow, visible and identical to the sibling statements, so no verifier reaches a different result. Fix: state "hold charge current below 5 mA" in REQ-SYS-089 and REQ-SYS-167 (Class I, with CR-008 or at the PDR TBR closure of REQ-SYS-167), or cite the level from the requirement once it is stated there | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer (re-pin delta) | Minor | R5 (CR record content); 05 section 5.2 (Closed: "owner approves the merge") | CR-008 section 10, row "Owner merge approval" (`aa65e826`, line 352) | The cell reads "2026-09-28, with the disposition: 'their branches merge after the section 9 checks' (lead SE reading ...)". That makes the record look as though the owner approved the merge on 2026-09-28. The plan instead puts the merge approval of CR-008, 009, 010, 013, 015 and 016 at session S1 as OD-43 (`pdr-work-plan.md` S1 row, "OD-43 batch 1"), and CR-008 section 9 item (d) of the same file says "then the owner's merge approval at S1 (batch 1)". The two parts of the record disagree about an owner approval point. Minor, because the cell also says "Merge held at the disposition", and no product or blob depends on it. Fix (configuration manager, record text only, before the merge): give the cell "Pending: owner merge approval at S1 (OD-43, batch 1)", keep the 2026-09-28 reading as the disposition's context, and fill it with the S1 answer | Verified (status re-pin delta: the `c1a52ab6` cell reads "Pending: the owner's merge approval for this CR is asked at S1 (OD-43 ...)") | Not needed | Before the CR-008 merge |

**Counts.** 1 finding, Minor; open Major 0. Under plan rule C1 the Minor finding is a lien if CR-008 is not revised before its disposition.

**Counts at the re-pin delta (2026-09-29).** 2 findings, both Minor; open Major 0. finding-1 is a Lien (rule C1: CR-008 was dispositioned Approved on 2026-09-28 without a revision; due at the CDR readiness declaration). finding-2 is new and Open, to be fixed before the merge (record text only).

### Lien verification (INSP-003 liens, RFA-SRR-007 L-7, INSP-025 cross items on the L1 side)

| Lien | Required fix (source record) | Evidence on the frozen blobs | Result |
|---|---|---|---|
| INSP-003 finding-12, finding-30 (rationale length and form) | Every live rationale at most 120 words, 02 section 4.3 label order, one SRR decision citation kept | Script over all 189 live entries (188 Active, 1 Draft): maximum 120 words (REQ-SYS-055 and 161 at 120), none above; labels `Why:`, `Assumes:`, `Ops:`, `Depends on:`, `Fault tolerance:`, `Constraint:`, `KDR:`, `TBR:` in 02 section 4.3 order in every entry, no label repeated; every entry starts `Why:` or `Self-derived:`; no `shall` in any rationale; every entry with a `tbr` object has a `TBR:` item. At `baseline/srr` 34 live rationales exceeded 120 words (REQ-SYS-054 at 283); all 34 are among the 55 changed. The "Hazard controls implemented" item is in 0 rationales (23 at `baseline/srr`); its content is the `control_req_ids` of `docs/safety/hazards.json`, unchanged. No label present at `baseline/srr` is lost in any changed rationale (script); every rewritten rationale that cited an SRR decision still cites at least one | Verified |
| INSP-003 finding-25 (tolerances supplied by the test author) | State each tolerance in the L1 statement (or the L2 child) and have the case take it from there | Statements now carry the value: REQ-SYS-014 (5 percent shape, +/-0.5 ms, under the TBR, `tbr.plan` names both), 044 (larger of +/-1 percent and +/-0.5 ms, the REQ-SYS-042 tolerance), 045 (+/-5 Hz), 077 (20 ms), 087, 088, 093 (below 5 mA), 161 (constant within 0.5 ms), 166 (below 0.5 V, TBR with REQ-SYS-149 in `tbr.plan`), 167 (+/-2 min, under the TBR). The one-sided bounds REQ-SYS-048, 053, 054 and 162 keep their statements: each states its bound completely, and the cases now apply the 04 section 8.2 decision rule inward (04 line 320: "Pass if the reading plus the instrument accuracy is within the limit"); rationales of REQ-SYS-053 and 054 say so. Each case side is verified in INSP-045. One residual of this class in TC-SYS-065 is finding-1 | Verified (residual finding-1) |
| INSP-003 finding-26 (fault-tolerance pointers) | Item 4 for REQ-SYS-009, 154, 112, 113 (item 7 kept for 112, 113); the governing item for 008, 034, 153; item 5 only where the harmonic-filter exception or a Marginal hazard applies | Against `docs/safety/hazard-analysis.md` section 8.1 (lines 235 to 269) and 8.2: REQ-SYS-009 item 4 (HZ-008 C7) and 8.2 row 4, as item 4 names REQ-SYS-009, 154 and 182; REQ-SYS-154 item 4 and row 4; REQ-SYS-112 and 113 items 4 and 7 (item 4 covers HZ-003; the item 7 table lists both against RSK-006); REQ-SYS-008 item 7 (HZ-008 K4, Test on every unit; `hazards.json` HZ-008 K4 lists REQ-SYS-008); REQ-SYS-034 item 7 (HZ-008 K6, which lists REQ-SYS-034); REQ-SYS-153 item 7 (HZ-008 K3, which lists REQ-SYS-153) and row 11 (ALC detector reading low, full output at full charge, the case the high-pack-voltage lockout bounds); REQ-SYS-010 item 7 alone (the item 7 table row HZ-008 K4, RSK-011). Remaining item 5 citations, script over all live entries: REQ-SYS-017, 018, 151 (the harmonic-filter exception, row 10), and requirements of Marginal hazards or sharing one (011, 013, 047, 049, 050, 070, 079, 090, 093, 105, 106, 107, 110, 111, 152, 168); none controls only a Critical hazard | Verified |
| INSP-003 finding-27 (REQ-SYS-184 note) | Record the 5 WPM squeezed characters as data for the TBR | Note now reads "... at 5 WPM recorded as data for the TBR (a squeezed C at 5 WPM holds both contacts for 2.64 s, above the 2 s limit)". Checked: 11 dits of 240 ms is 2.64 s. Also closes INSP-025 X5 | Verified |
| INSP-003 finding-28, RID-SRR-003 content, TBR finding 7 (REQ-SYS-054 wording) | Say how the two gap lengths combine, within 25 words | "... or 30 s (TBR) without min(7-dit, 500 ms) gaps (TBR)", 24 words, one `shall`; the shorter-of reading equals HZ-004 K4 item (ii), the rationale ("the shorter of 7 dit times and 500 ms") and `tbr.plan`. The rationale no longer carries the MOE-012 "13 s ... bounded at 30 s here" history sentence or any other 10 s or 30 s wording that disagrees with SRR decision 37 (the stale wording the plan names). RID-SRR-003's requested content (no-gap form, REQ-SYS-184 squeeze limit, REQ-SYS-053 covering the Bug dah, cases updated) holds at `c629198`; its log move stays with WP-PDR-15 | Verified |
| INSP-003 finding-29 (i) | Memo amendment or `tbr` removal for REQ-SYS-180 to 182 | `docs/reviews/SRR/decision-memo.md` section 13, amendment A-2, records that REQ-SYS-180, 181 and 182 keep their `tbr` objects to PDR and sets the L1 TBR count to 109; no requirement edit needed | Verified |
| INSP-003 finding-29 (ii) | 104 stale `tbr.owner` fields | All 104 fields that read "Robin decides at SRR on Claude's proposal; ..." now read "Robin approves on Claude's proposal at PDR; Claude produces the closing evidence"; the 110 `tbr` objects (109 plus REQ-SYS-194) all carry that owner and `close_by: PDR`; no `close_by` changed; `(TBR)` appears in a description exactly when a `tbr` object exists (script) | Verified |
| INSP-003 finding-29 (iii) | Eight generic `TBR:` items | REQ-SYS-009, 031, 059, 062, 086, 100, 102 and 103 each state the estimate and the PDR evidence that closes it, consistent with its `tbr.plan` (read one by one); the generic sentence is in no rationale (script) | Verified |
| INSP-003 finding-31 (i) (REQ-SYS-185, 186 side) | State the open-path level and the agreement band in the requirements | REQ-SYS-185 "cut charge current below 1 mA ..."; REQ-SYS-186 "keep cell thresholds of all but one protection layer within 20 mV ..."; the REQ-SYS-188 and 189 allowances are handled as one-sided bounds (rationales say "an upper bound, verified with the capture resolution applied inward (04 section 8.2)") | Verified |
| INSP-003 finding-31 (ii) (REQ-SYS-185 note) | Remove the charger-in-regulation ambiguity | Note: other cell at 3.70 V so the charger stays in constant current, firmware charge stops disabled, judged by the 1 mA level, switching-element voltage as supporting data. The pack-regulation part is removed; the per-cell charger part is INSP-045 finding-2 | Verified on the requirement side |
| INSP-025 X1 and finding-5 (requirement side) | Split REQ-SYS-083 into a room-temperature Test companion and a 0 C to 45 C Analysis companion with the RSK note | REQ-SYS-083 "... at 18 C to 28 C", method Test, note "The 0 C to 45 C span is REQ-SYS-194, closed by Analysis"; new REQ-SYS-194 (Draft, method Analysis, note begins "Analysis accepted per RSK-007", the 04 section 3 rule 7.3.6 form; RSK-007 carries HZ-002 per hazard-analysis section 8.1 item 7 table), tags `revA`, `safety`, `hazard_ids` HZ-002, `source_ids` as REQ-SYS-083, `tbr` closing with REQ-SYS-083 at PDR, closing case TC-SYS-116 | Verified |
| INSP-025 X6 | Notes of REQ-SYS-051, 094, 171, 173 follow SRR decision 41 | 051: 5 W tune carriers and hand keying, test mode at 0.5 W not used; 094: keying fixture 1:9 pattern at 5 W, closures shorter than the REQ-SYS-053 timeout; 171: generator at 0.5 W in four 110 s entries, each under the REQ-SYS-188 120 s, together over the 6 min window (440 s); 173: keying fixture at 5 W with 10-dit word spaces, test mode not used | Verified |
| INSP-025 X8 | Confirm the gap definition at the PDR TBR | REQ-SYS-054 `tbr.plan` adds "including word spaces near 7 dits above about 17 WPM (INSP-025 cross item X8)" | Verified (carried to the PDR TBR) |
| L-7, RFA-SRR-007 (ADR citations in `source_ids`) | ADR citation where the ADR 4.1 table lists a requirement; the eight named requirements | 46 ADR ids added on 40 requirements, no `source_ids` entry removed or reordered (script). Each of the 46 pairs was matched to its ADR section 4.1 row: in 33 the requirement heads a row whose Relationship column says "allocated" or "allocated at L1"; in 12 the Relationship column of a candidate row names it as the L1 allocation (ADR-009: REQ-SYS-047 to 051 and 055 "at L1", and 040, 052 to 054 and 056 in the "Modes ..." row; ADR-022: "allocated as REQ-SYS-012"); REQ-SYS-178 is named in the note of the ADR-012 REQ-SYS-140 row and by L-7 itself. Every 4.1 row of an Accepted ADR that names a REQ-SYS id the requirement still does not cite was listed by script (27 pairs) and each is excluded by the stated rule: rows marked "not created" or "covered by" (ADR-005, 008, 012, 015, 020, 024), "cite ADR-NNN, not this ADR" (ADR-002 for 008 and 021; ADR-022 for 017; ADR-014 for 065, 066, which cite ADR-015; ADR-027 for 128, 129, which cite ADR-011), notes that say the requirement "does not cite this ADR" by design (ADR-006 for 059, 060, 061, 165), and ADR-010 for 136 (Superseded by ADR-026, which REQ-SYS-136 now cites). The one judgment call, REQ-SYS-124 in ADR-014's third row ("ConOps text and REQ-SYS-122, REQ-SYS-124"), carries no "allocated" wording and is outside the eight L-7 names. The eight named requirements REQ-SYS-011, 063, 064, 092, 146, 175, 178, 182 all cite their ADR; REQ-TX-004 is correctly left to WP-PDR-34; "ADR-026 after decision 47" holds (REQ-SYS-044, 136, 160, 161 cite ADR-026) | Verified |

### CR-008 section 5 items on the L1 file

| Item (CR-008 section 5) | Check | Result |
|---|---|---|
| Each before and after of section 1.1 against the blob and the 25-word limit | The 14 `description` changes of the diff are exactly REQ-SYS-014, 044, 045, 054, 077, 083, 087, 088, 093, 161, 166, 167, 185, 186; each "before" equals `baseline/srr` and each "after" equals `c629198`; word counts 20 to 25 (script); one `shall` each | Yes |
| All 189 live rationales at most 120 words, none with the hazard-controls item | Lien table row 1 | Yes |
| The seven finding-26 pointers and REQ-SYS-010 against 8.1 items 4, 5, 7 and 8.2 rows 4, 11 | Lien table row 3 | Yes |
| The eight finding-29 (iii) items against their `tbr.plan` | Lien table row 8 | Yes |
| The 104 owner fields | Lien table row 7 | Yes |
| The 46 ADR citations against the section 1.5 rule; no 4.1 row that meets the rule missed | Lien table last row | Yes |
| REQ-SYS-194 against 04 section 3 and rule 7.3.6 | Lien table row X1 | Yes |
| No other line of the four files changed (`git diff ab2af2d c629198`) | Field-level diff: requirements change only in `description` (14), `rationale` (55), `verification_note` (10), `source_ids` (40), `tbr` (104 owners, 4 plans: REQ-SYS-014, 054, 166, 167), plus REQ-SYS-194 appended; `module`, titles, methods, statuses, parents, children, tags, hazards, `design_refs`, `mop_ids` and priorities unchanged; `requirements.md` equals the `tools/traceability.py --render` output of the frozen JSON (rendered on the export, `cmp` equal) | Yes |
| Tool runs of section 4 | On the export of `c629198`: `tools/traceability.py --report-only`: 246 requirements, 174 test cases, 0 violations, 4 warnings (`HAZARD_INVERSE` REQ-SYS-194; `SYS_UNALLOCATED` REQ-SYS-125, 148, 194), as CR-008 section 4 states; `tools/validate_docs.py` 50 passed, 0 failed (drift rule not applied on an export without HEAD) | Yes |
| Volatility (02 section 10.4) | (A + M + R) / N_start = (1 + 14 + 0) / 188 = 8.0 percent; 188 live at `baseline/srr` (script) | Yes |

## Readiness criteria (all true before the review starts)

| Id | Criterion | Answer and evidence |
|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 for the product | Yes on the export of `c629198` (50 passed, 0 failed). On `main` at `1b93d83` the run exits 1 on one record not in this product (`docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`, record drift on `docs/cm/tool-validation/README.md` and `tools/toolchain.lock.md`), cross item X-3 |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | Yes: 0 violations on the export; the 4 warnings are the ones CR-008 section 4 lists |
| R3 | The author's return states the self-check and lists the acceptance criteria | Yes: CR-008 section 5 "Verification of the implementation" lists the acceptance criteria item by item, section 1 maps every change to its lien, and the author summary in the brief states the lien-by-lien closure. No separate A to G self-check file exists; for a lien-closure CR the section 1 tables serve it |
| R4 | Every TBR has `owner`, `plan`, `close_by`; no `TBD` | Yes: 110 `tbr` objects, each with all three, `close_by: PDR`; T-17 reports no `TBD` |
| R5 | For a CR, the impact assessment is attached | Yes: CR-008 section 4, every field filled with numbers and ids. Its section 6 independent impact review is still pending (rule C6); this record is an input to it, not a substitute |

## Participants

Author: WP-PDR-11 author invocation (L1 requirements author and TC-SYS test author in one invocation, disclosed in CR-008 section 4). Reviewer: this invocation (`reviewer:WP-PDR-11-INSP-003-delta`). Software assurance: not required (07 section 2.1.1, row "Software requirement files", column "Neither": the SYS L1 file is not a software requirement file; INSP-003 recorded the same).

## A. Format and editorial

| Item | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 | Yes | The 15 new or changed statements each contain exactly one `shall` in the form "The transceiver shall ..." (script; T-17 lint clean) |
| CK-REQ-A2 | Yes | 20 to 25 words each; REQ-SYS-077 ("within 20 ms of plug removal and while no plug is inserted") and REQ-SYS-087 (two refusal conditions of one insertion check, rationale explains) are intrinsic couplings; REQ-SYS-083 split into 083 and 194 removes a two-method statement |
| CK-REQ-A3 | Yes | Every quantity added has a number, unit and tolerance or bound: +/-0.5 ms, 5 percent, +/-5 Hz, 20 ms, 5 mA, 1 mA, 0.5 V, 0.5 ms, +/-2 min, 20 mV, 18 C to 28 C; the REQ-SYS-054 gap is min(7-dit, 500 ms). The residual in TC-SYS-065 is finding-1 (item D4) |
| CK-REQ-A4 | Yes | No WR-07 word in any changed statement (script and T-17) |
| CK-REQ-A5 | Yes | No part number in a statement; S-8252 and BQ29209 appear only in rationales |
| CK-REQ-A6 | Yes | REQ-SYS-194 title 76 characters, next free id after the 191 to 193 that CR-003 claims; no id reused; TC-SYS-061 title updated to "at room temperature" |
| CK-REQ-A7 | Yes | Lien table rows 1 and 3; REQ-SYS-194 rationale cites NGO-022, HZ-002 K2, CON-016, F11, SRR decision 72, 04 section 3 |
| CK-REQ-A8 | Yes | Terminology unchanged; "10-to-90 percent", "keyer test point", "cell-sense connection" as in the file |

## B. Stakeholder satisfaction and traceability

| Item | Answer | Evidence |
|---|---|---|
| CK-REQ-B1 | Yes | REQ-SYS-194 `parent_id` null with `source_ids` NGO-022, OPS-016, CON-011 and a rationale, as REQ-SYS-083; no other parent field changed |
| CK-REQ-B2 | Yes | REQ-SYS-194 is necessary: without it the 0 C to 45 C span of HZ-002 K2 has no closing method (INSP-025 finding-5) |
| CK-REQ-B3 | Yes | No allocation change in this file; `docs/design/allocation.json` gains REQ-SYS-194 at CR-008 step 5 (`SYS_UNALLOCATED` warning until then) |
| CK-REQ-B4 | Yes | No OPS coverage changes; both key types untouched |
| CK-REQ-B5 | Yes | REQ-SYS-194 carries `hazard_ids` HZ-002; `docs/safety/hazards.json` HZ-002 K2 gains it at CR-008 step 3 (`HAZARD_INVERSE` warning until then, a merge condition) |
| CK-REQ-B6 | Yes | REQ-SYS-194 tags `revA`, `safety`; no tag changed elsewhere |
| CK-REQ-B7 | Yes | CR-008 section 4 lists every downstream item: 64 cases modified and TC-SYS-116 added, the L2 children to align (REQ-TX-005, REQ-SW-KEYER-032, 020, 021), `hazards.json`, `hazard-analysis.md`, `allocation.json`, RSK-007, the rebase of CR-003 and CR-006, and the volatility count 8.0 percent (checked above) |

## C. Technical correctness

| Item | Answer | Evidence |
|---|---|---|
| CK-REQ-C1 | Yes | Values checked: +/-5 Hz is half the 10 Hz step; 11 dits at 5 WPM is 2.64 s; the qualifying gap at 5, 25, 50 WPM is 500, 336, 168 ms (7 x 1200/WPM against 500 ms); 4.30-4.35 V starts where 4.25-4.30 V ends; 20 mV equals the S-8252-class accuracy the REQ-SYS-083 rationale uses; the REQ-SYS-014 tolerances sit inside the regulatory basis of 47 CFR 97.307(a), (b) that its rationale cites |
| CK-REQ-C2 | Yes | No ICD value changes; REQ-SYS-077 is internal (CR-008 section 4 Interfaces) |
| CK-REQ-C3 | Yes | "independently of charger and firmware" kept in REQ-SYS-083; REQ-SYS-185 keeps "independently of charger, 4.25 V protector and firmware" |
| CK-REQ-C4 | N/A | No `SW-SAFE` requirement in the file |
| CK-REQ-C5 | Yes | No state name changes |
| CK-REQ-C6 | Yes | Undesired-event requirements (054, 087, 088, 166, 185, 186) keep their responses; the change makes each measurable |
| CK-REQ-C7 | N/A | No cybersecurity requirement touched |
| CK-REQ-C8 | N/A | No loaded-data requirement touched |

## D. Feasibility

| Item | Answer | Evidence |
|---|---|---|
| CK-REQ-D1 | Yes | 0.5 ms constancy (REQ-SYS-161) and +/-0.5 ms hang floor (044) are the REQ-SYS-042 tolerance already ruled; 20 ms amplifier disable is far above the 1 ms tick |
| CK-REQ-D2 | N/A | No resource values |
| CK-REQ-D3 | N/A | No firmware construction constraint changed |
| CK-REQ-D4 | No | Every new tolerance is defended in its rationale ("+/-5 Hz is half a 10 Hz step", "20 ms covers the jack-detect debounce", "Below 5 mA ... above the charger's standby leakage", "Below 1 mA states an open charge path", "the S-8252-class accuracy at 25 C", REQ-SYS-042 floor for 044 and 161); REQ-SYS-167's +/-2 min is stated as the author's proposal under its TBR. No: finding-1 (the "stop charging" level of REQ-SYS-089 and 167 is set in TC-SYS-065, not in the statements) |

## E. Verifiability

| Item | Answer | Evidence |
|---|---|---|
| CK-REQ-E1 | Yes | REQ-SYS-083 Test at 18 C to 28 C (the bench has no chamber, CON-016); REQ-SYS-194 Analysis, because a Test over 0 C to 45 C is impossible on the bench, with the 04 rule 7.3.6 acceptance note |
| CK-REQ-E2 | Yes | The ten changed notes each name the pre-build and post-build classes and the closing case (read one by one); X6 notes now match SRR decision 41 |
| CK-REQ-E3 | Yes | REQ-SYS-194 is hazard-linked with method Analysis under the "Analysis accepted per RSK-007" route of 04 section 3 and hazard-analysis section 8.1 item 7, which CR-008 step 4 extends; every other changed hazard requirement keeps method Test or its existing accepted route |
| CK-REQ-E4 | Yes | Each new level is observable at the unit boundary: charge current on the multimeter, rail voltage, capture edges, tinySA level |
| CK-REQ-E5 | Yes | 5 mA and 1 mA on the multimeter current range; 0.5 V on the multimeter; +/-5 Hz and 0.5 ms on the 1 MS/s Pico logic capture (04 section 6.1) |
| CK-REQ-E6 | Yes | REQ-SYS-194 closed by TC-SYS-116; every changed requirement keeps its closing case; traceability shows 189 of 189 live covered |

## F. Non-redundancy and consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-REQ-F1 | Yes | REQ-SYS-083 and 194 split the same threshold by temperature range with one method each, not a duplicate; REQ-SYS-093 and 087 now share the 5 mA level without conflict. Child conflicts named by CR-008 section 4 (REQ-TX-005 at +/-10 percent against +/-0.5 ms; REQ-SW-KEYER-032 hang tolerance; REQ-SW-KEYER-020 and 021 sampling counts) are routed to WP-PDR-34 and 35, cross item X-2 |
| CK-REQ-F2 | Yes | Terms identical to the file |
| CK-REQ-F3 | Yes | All entries are system-level |
| CK-REQ-F4 | Yes | REQ-SYS-194 `priority: Baseline`; no priority changed |

ITEMS N/A: CK-REQ-C4, C7, C8, D2, D3, G1 to G8.

## Per-requirement validation (every added or changed requirement, 145 rows)

V1 to V6 for Class II-only rows (rationale, note, `source_ids`, `tbr` text) re-check that the change keeps the INSP-003 cell true; statements unchanged since INSP-003 keep its V2 cell. For REQ-SYS-183 to 190 (added at R16) the V2 cell names the groups of their SRR ruling. WR failures are the script results (WR-01, 03, 07, 10, 12) plus the reviewer's reading of WR-02, 04, 05, 06, 08, 09, 11, 13 and 14 for the 15 new or changed statements.

| Requirement | Fields changed | WR failures | V1 | V2 | V3 | V4 | V5 | V6 | CK-REQ items answered No | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| REQ-SYS-002 | rationale | none | Pass | Ready: customer, user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-004 | tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-005 | rationale | none | Pass | Ready: customer, user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-008 | rationale, tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-009 | rationale, source_ids, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-010 | rationale, source_ids, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-011 | source_ids, tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-012 | source_ids, tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-014 | description, rationale, source_ids, tbr.owner, tbr.plan | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-015 | rationale, source_ids, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-017 | rationale, source_ids | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-018 | rationale, source_ids, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-019 | tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-020 | rationale, tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-022 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-023 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-024 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-025 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-026 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-027 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-028 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-029 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-030 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-031 | rationale, tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-032 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-033 | tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-034 | rationale, source_ids, tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-035 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-036 | tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-037 | tbr.owner | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-040 | source_ids | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-042 | source_ids | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-043 | source_ids | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-044 | description, rationale, tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-045 | description, rationale | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-047 | source_ids | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-048 | source_ids, tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-049 | source_ids, tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-050 | source_ids | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-051 | verification_note, source_ids | none | Pass | Ready: customer, user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-052 | source_ids, tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-053 | rationale, source_ids, tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-054 | description, rationale, source_ids, tbr.owner, tbr.plan | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-055 | rationale, source_ids, tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-056 | source_ids | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-058 | source_ids, tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-059 | rationale, tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-061 | tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-062 | rationale, tbr.owner | none | Pass | Ready: guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-063 | source_ids | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-064 | source_ids, tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-065 | rationale | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-067 | tbr.owner | none | Pass | Ready: customer, user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-068 | tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-069 | tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-071 | tbr.owner | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-072 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-073 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-074 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-076 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-077 | description, rationale | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-078 | tbr.owner | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-081 | tbr.owner | none | Pass | Ready: customer, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-082 | tbr.owner | none | Pass | Ready: customer, guest operator, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-083 | description, rationale, verification_note, tbr.owner | none | Pass | Ready: customer, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-084 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-085 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-086 | rationale, tbr.owner | none | Pass | Ready: customer, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-087 | description, rationale, verification_note, tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-088 | description, rationale, verification_note, tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-089 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-090 | rationale | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-092 | source_ids | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-093 | description, rationale | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-094 | verification_note | none | Pass | Ready: customer | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-095 | source_ids, tbr.owner | none | Pass | Ready: customer | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-097 | source_ids, tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-098 | source_ids, tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-099 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-100 | rationale, tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-102 | rationale, tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-103 | rationale, tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-105 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-106 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-107 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-112 | rationale, tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-113 | rationale, tbr.owner | none | Pass | Ready: customer | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-114 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-115 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-116 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-117 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-118 | tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-121 | rationale | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-122 | rationale | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-125 | rationale | none | Pass | Ready: user, guest operator, regulator, vendor, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-127 | source_ids | none | Pass | Ready: customer | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-130 | rationale | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-131 | tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-132 | source_ids | none | Pass | Ready: customer | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-133 | source_ids | none | Pass | Ready: guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-135 | source_ids | none | Pass | Ready: guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-136 | source_ids, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-137 | rationale | none | Pass | Ready: vendor, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-139 | source_ids, tbr.owner | none | Pass | Ready: vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-141 | tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-146 | source_ids | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-147 | tbr.owner | none | Pass | Ready: vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-149 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-151 | rationale, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-152 | tbr.owner | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-153 | rationale, tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-154 | rationale, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-155 | tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-156 | tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-158 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-159 | tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-160 | tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-161 | description, rationale, tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-162 | tbr.owner | none | Pass | Ready: user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-164 | tbr.owner | none | Pass | Ready: guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-165 | tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-166 | description, rationale, verification_note, tbr.owner, tbr.plan | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-167 | description, rationale, tbr.owner, tbr.plan | none | Pass | Ready: guest operator | Pass | Pass | Pass | Pass | CK-REQ-D4 | finding-1 |
| REQ-SYS-168 | tbr.owner | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-169 | tbr.owner | none | Pass | Ready: user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-171 | verification_note | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-172 | source_ids, tbr.owner | none | Pass | Ready: user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-173 | verification_note | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-175 | source_ids | none | Pass | Ready: customer, vendor | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-176 | tbr.owner | none | Pass | Ready: user, regulator, vendor, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-177 | tbr.owner | none | Pass | Ready: user, regulator, vendor, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-178 | source_ids | none | Pass | Ready: vendor, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-179 | rationale | none | Pass | Ready: customer | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-180 | rationale, tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-181 | rationale, tbr.owner | none | Pass | Ready: customer, user, guest operator, regulator, public | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-182 | rationale, source_ids, tbr.owner | none | Pass | Ready: user, regulator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-183 | rationale, tbr.owner | none | Pass | Ready: customer, user, guest operator (NGO-021, MOE-012) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-184 | rationale, verification_note | none | Pass | Ready: customer, user, guest operator (SRR decision 37) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-185 | description, rationale, verification_note | none | Pass | Ready: customer, user (SRR decision 72) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-186 | description, rationale | none | Pass | Ready: customer, user (SRR decision 72) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-187 | rationale | none | Pass | Ready: customer, user, guest operator (SRR decision 41) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-188 | rationale | none | Pass | Ready: customer, user, guest operator (SRR decision 41) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-189 | rationale | none | Pass | Ready: customer, user (SRR decision 41) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-190 | rationale | none | Pass | Ready: customer, user (SRR decision 41) | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SYS-194 | added | none | Pass | Ready: customer, guest operator (as REQ-SYS-083) | Pass | Pass | Pass | Pass | none | Pass |

V2 confirmation: no statement's stakeholder trace changed; the groups and counts of INSP-003's V2 block stand, and Robin's confirmation of the fourteen amended statements and REQ-SYS-194 is the owner's disposition of CR-008 (section 12 questions 2 to 4, OD-37).

| Stakeholder group (`name` and `role`) | `represented_by` | Requirements whose V2 cell names the group (count), and those marked `Fail` (ids) | Robin's confirmation |
|---|---|---|---|
| Robin (customer), `customer`; Robin (operator), `user` | Robin | 15 new or changed statements; Fail: none | CR-008 disposition (OD-37) |
| Guest operators, `guest operator` | Robin (representation rule, 02 section 3.0) | REQ-SYS-054, 083, 161, 167, 194 among the changed statements; Fail: none | CR-008 disposition (OD-37) |
| FCC, `regulator` | Verbatim corpus; Robin as licensee | REQ-SYS-014 (47 CFR 97.307(a), (b)); Fail: none | CR-008 disposition (OD-37) |

V6 notes:

| Requirement | Worst outcome if omitted, or the level that keeps a cross-level duplicate |
|---|---|
| REQ-SYS-194 | Without it the HZ-002 K2 threshold over 0 C to 45 C has no closing requirement once REQ-SYS-083 is narrowed to 18 C to 28 C; the Catastrophic overcharge branch would lose its temperature coverage |

## Cross items (outside this product; not findings against it)

- X-1 (CR-008 steps 3 to 6, before the merge): HZ-002 K2 `control_req_ids` and `requirement_ids` gain REQ-SYS-194 (clears `HAZARD_INVERSE`); `hazard-analysis.md` section 8.1 item 7 lists REQ-SYS-194 against RSK-007 (its `Fault tolerance:` item already cites items 3 and 7); `allocation.json` allocates REQ-SYS-194 (clears `SYS_UNALLOCATED`); RSK-007 cites it. The rationale of REQ-SYS-194 cites the item 7 table before step 4 adds the row.
- X-2 (WP-PDR-34, WP-PDR-35, WP-PDR-40): align REQ-TX-005, REQ-SW-KEYER-032, 020 and 021 with the amended parents, as CR-008 section 4 lists.
- X-3 (lead SE, not this WP): `tools/validate_docs.py` on `main` at `1b93d83` exits 1 on `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` (record drift), and `tools/tests` `test_validate_docs.RepositoryTests.test_repository_exit_zero` fails for the same reason; both predate this record.
- X-4 (lead SE; charter section 11 rule 4): one invocation wrote both the requirement changes and the case changes. CR-008 section 4 discloses it and asks the reviewers to treat each case change as author-written; INSP-045 checked every changed case against the requirement text alone. Recommend recording it in `docs/cm/deviations.md` or confirming at OD-37 that the plan's WP-PDR-11 role assignment covers it.
- X-5 (INSP-003 record): INSP-003 names the `baseline/srr` blobs, so it drifts when CR-008 merges; this record and INSP-045 are its delta iteration on the frozen blobs, as plan WP-PDR-11 names. The lead SE cross-references them in INSP-003 or the PDR package section 15 lien table when CR-008 merges.

## Record verdict

Reviewer verdict **APPROVED**, readiness met, one Minor finding (finding-1, a lien under rule C1 if CR-008 is not revised before its disposition). Every INSP-003 lien carried by WP-PDR-11 (finding-12, 25 to 31), L-7 of RFA-SRR-007, INSP-025 X1, X5, X6 and X8 on the requirement side, and the RID-SRR-003 and TBR finding 7 wording are Verified on the frozen blobs. No Major finding. The record `verdict` stays NEEDS CHANGES only because `tools/validate_docs.py` fails an APPROVED record whose `product_files` are not in `main` HEAD. When CR-008 merges and `git rev-parse HEAD:<path>` equals each `product_files` blob (or a delta iteration verifies new blobs), the software lead sets `verdict: APPROVED`. Software assurance pair: not required (07 section 2.1.1).

## Verdict format

```
VERDICT: APPROVED (record verdict held at NEEDS CHANGES until CR-008 merges; drift rule)
FINDINGS:
- [Minor] finding-1 CK-REQ-D4 REQ-SYS-167 (and 089) description: "stop charging" has no level; TC-SYS-065 supplies 5 mA from REQ-SYS-087, 088, 093. State the level in the statements.
ITEMS N/A: CK-REQ-C4, C7, C8, D2, D3, G1 to G8
MEASUREMENTS: size=145 requirements added or changed (191 entries, 189 live); rows=145; rows_with_wr_failures=0; v_fail=V1:0 V2:0 V3:0 V4:0 V5:0 V6:0; turns=60; minutes=120; major=0; minor=1
```

## Iteration 2: drift delta on the CR file (2026-09-27, main `ae29a98`)

**Scope (plan rule C1, record drift rule).** The record named the CR file at blob `3b9266ff` (`4dab5dc`). Main has since changed that one file twice: `cccbfda` appended section 6.1, the independent impact review round 1 (blob `ade26204`), and `a244b05` recorded revision 2, the author's fix of R1-F1 (blob `5e6ceb62`, the blob at `main` `ae29a98`). The brief named `ade26204`. Revision 2 had already landed on `main` when this iteration started, so this delta covers both commits and names `5e6ceb62`. The four requirement and test-case blobs are unchanged: `git rev-parse cr/CR-008-srr-liens-l1-and-tc-sys` is still `c629198`, and `git rev-parse c629198:<path>` equals each of the four `product_files` blobs. Nothing in iterations 1 or 2 changes the L1 content, so the iteration 1 rows stand. The only thing to decide was whether the new CR text changes any answer in this record.

**Independence (rule C4).** This invocation authored no part of CR-008, its section 6.1 or 6.2, or the branch, and it edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (query: "PDR work plan rule C1 delta iteration record drift product_files verdict"). After that search, `grep -n` and `sed -n` only pinned lines in known files: the plan's rule C1 (line 975), the validator's drift rule (line 924), and the ICD lines that revision 2 cites.

### Hunks read (`git diff 3b9266ff 5e6ceb62`: 5 hunks, 63 insertions, 6 deletions; read as `3b9266ff..ade26204`, 2 hunks, then `ade26204..5e6ceb62`, 5 hunks)

| Hunk | Change | Effect on this record (L1 lens) |
|---|---|---|
| `cccbfda` @@ -180 | Section 6.1, impact review round 1: R1-F1 (Major, the Interfaces row said "None" although ICD-CTL-PHONES, ICD-PWR-CELL and ICD-CTL-KEY bind or quote changed statements, including the 50 ms PHONES_DET debounce against the new REQ-SYS-077 20 ms bound); R1-F2 to R1-F5 (Minor); items checked with no finding | Iteration 1 answered CK-REQ-C2 "No ICD value changes; REQ-SYS-077 is internal (CR-008 section 4 Interfaces)". That answer relied on the CR row that R1-F1 shows to be wrong, so it was an escape of this review. It is corrected below on the revision 2 evidence. The "items checked with no finding" repeat this record's counts (14 statements, 1 added, 55 rationales, 10 notes, 40 `source_ids`, 104 owners, 4 plans; volatility 8.0 percent; 0 violations and 4 warnings) and agree with them |
| `cccbfda` @@ -234 | Section 11 status row for round 1 | Status record only; no effect |
| `a244b05` @@ -8 | Front matter: `affected_cis` adds row 10; `affected_paths` adds the three ICDs and `render_icd_figures.py`; `affected_ids` adds the three ICD ids; `related` adds WP-PDR-36 and WP-PDR-40 | No L1 field is affected. `affected_ids` still lists 15 of the 145 changed requirements, which is R1-F2 (open in section 6.1, CR-document scope) |
| `a244b05` @@ -138 | Section 4 Interfaces row rewritten: (a) ICD-CTL-PHONES, where question 2a is an asymmetric detect (50 ms debounce on insertion; at most 10 ms (TBR) on removal; enable low within 20 ms of the removal edge) and question 2b is a 70 ms bound; (b) ICD-PWR-CELL line edits; (c) ICD-CTL-KEY lines 161 and 261 take the SRR decision 37 wording | Each line citation checked at `ae29a98`. ICD-CTL-PHONES line 140 has "debounced 50 ms" with no direction, line 143 is the detect and enable behaviour, and line 215 quotes the old REQ-SYS-077. `render_icd_figures.py` line 404 has "detect debounced 50 ms". ICD-PWR-CELL line 139 credits 0 C to 45 C to REQ-SYS-083; lines 142 and 143 have "rails held off", "refused" and "stopped"; line 234 has "over 60 min". ICD-CTL-KEY lines 161 and 261 have "128 ... or 10 s (TBR)" with D-KN3. Also checked: `hazards.json` HZ-005 K6 places the 50 ms debounce on insertion ("on insertion the output ramps from zero over 100 ms after a 50 ms debounce"); the frozen REQ-SYS-077 statement ("within 20 ms of plug removal and while no plug is inserted") and its rationale ("20 ms covers the jack-detect debounce and the enable path") hold unchanged under 2a; and the REQ-SYS-054 text quoted for ICD-CTL-KEY line 161 equals the frozen statement word for word. The replacement wording for ICD-PWR-CELL ("held below 0.5 V (TBR)", "below 5 mA", "+/-2 min", REQ-SYS-194) equals the frozen REQ-SYS-166, 087, 088, 167 and 194 |
| `a244b05` @@ -164 | Section 5 step 9: ICD alignment by the ICD writer (WP-PDR-36a/36b) before the ICD baseline, checked under `peer-review-checklist-design.md` section I | Downstream item only, off this branch. The row sits between steps 7 and 8, and step 8 (after approval) follows in time; this ordering is editorial and raises no finding |
| `a244b05` @@ -223 | Section 6.2 author response: R1-F1 fixed; R1-F2 to R1-F5 not addressed (rule C1) | The round 2 re-check belongs to the impact reviewer; this record does not stand in for it |
| `a244b05` @@ -278 | Section 11 row for revision 2 and section 12 questions 2a and 2b | Question 2b ("within 70 ms of plug removal") would revise REQ-SYS-077, its rationale and TC-SYS-056 on the branch. If the owner picks 2b, the frozen blobs change and this record needs a further delta. Under 2a no L1 blob changes |

### Items revisited

| Item | Iteration 2 answer | Evidence |
|---|---|---|
| CK-REQ-C2 | Yes (corrects the iteration 1 evidence) | Iteration 1 said "No ICD value changes", which was wrong: ICD-CTL-PHONES line 140 conflicts with REQ-SYS-077 if the 50 ms debounce applies at removal. At revision 2 the conflict is named and resolved before the disposition. Under 2a the statement stays as frozen, and the ICD changes through step 9 before the ICD baseline. The ICDs are preliminary stubs, not baselined (CR-008 section 4, row 10), so no baselined interface disagrees with the L1 file. Under 2b the statement changes before the merge, which requires a further delta of this record. The ICD-PWR-CELL and ICD-CTL-KEY edits are wording and citations that follow the frozen statements |
| CK-REQ-B7 | Yes | The downstream list now includes the three ICDs (section 4 Interfaces, step 9). R1-F5 (b), no PWR L2 child or `leaf` routing for REQ-SYS-194 and no G9 routing, stays open in CR section 6.1. It is a CR-document gap already recorded there, so it is not counted again here (cross item X-6) |
| CK-REQ-D4 (finding-1) | No (unchanged) | Revision 2 does not change REQ-SYS-089 or 167, and the ICD-PWR-CELL line 234 edit adds only "+/-2 min". Finding-1 stays Open and is a lien under rule C1 unless the MF-CR-008 fix revises the branch |

No new finding. Open Major 0; finding-1 (Minor) Open.

### Cross items added

- X-6 (CR-008 author and impact reviewer): R1-F2 (`affected_ids` completeness), R1-F3 (REQ-SYS-093 "below 5 mA" does not carry the no-boost-ripple assumption; route it to the PWR and SW L2 children) and R1-F5 (REQ-SYS-194 routing and the 110 TBR count) are open in CR section 6.1. From the L1 lens this reviewer concurs with each one. Only R1-F3 touches an L1 statement, and its fix belongs in an L2 child, not in REQ-SYS-093.
- X-7 (lead SE, lessons learned): the iteration 1 CK-REQ-C2 answer took the CR's Interfaces row on trust and did not check the ICDs named in `design_refs` (REQ-SYS-077 cites ICD-CTL-PHONES). Candidate lesson: for a CR requirement review, grep every changed statement's `design_refs` ICD for the old value.

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: no Major finding is open, and the drifted CR blob changes no L1 content and no Verified lien row. `product_files` now names the CR at `5e6ceb62` and the four branch blobs at `c629198`. `verdict` stays NEEDS CHANGES under the lead SE convention, because the four reviewed blobs exist only on the unmerged branch `cr/CR-008-srr-liens-l1-and-tc-sys`. The software lead sets APPROVED when CR-008 merges with them unchanged. Any branch change, including the pending MF-CR-008 fix or an owner choice of question 2b, needs a further delta iteration first.

```
VERDICT (iteration 2): APPROVED (record verdict held at NEEDS CHANGES until CR-008 merges; drift rule)
FINDINGS: finding-1 [Minor] unchanged, Open (lien under C1 unless fixed on the branch); no new finding
MEASUREMENTS (iteration 2): hunks=5 (2 + 5 read across the two commits); files_changed=1; product blobs re-identified=4 of 4 unchanged; turns=14; minutes=25; major=0; minor_new=0
```

## Re-pin delta on the CR file (2026-09-29, main `0680af9`; WP-PDR-55)

**Scope (plan rule C1, record drift rule).** The record named the CR file at `5e6ceb62` (`a244b05`). `main` changed that file four times after that: `6485bd3` (section 6.3, impact review round 2, blob `9cb5db1f`), `a17af87` (owner disposition, `d10804cd`), `9c40ef9` (section 9 pre-merge check and the step 7 Done cell, `4ae5e83e`) and `726cd44` (section 8 and the step 3 and 5 Done cells, `aa65e826`, the blob at `main` `0680af9`). This record reviewed sections 1, 4 and 5 (iteration 1) and, at iteration 2, the section 6.1 and 6.2 hunks. Section 5 changed, so this is a delta, and the CR file is re-pinned at `aa65e826`. Taking the file out of `product_files` would have been right only if no reviewed section had changed. The four frozen blobs have not changed: `git rev-parse e26ce46:<path>` (the branch head after the INSP-003 and INSP-008 updates) equals `c629198:<path>` for `requirements.json` `a7344937`, `requirements.md` `4e110b16`, `test_cases.json` `117c08de` and `test_cases.md` `00e4454f`. The branch commits after `c629198` (`ebeb069` records, `a36a828` `hazards.json` and `allocation.json`, `e26ce46` records) touch none of them. So the iteration 2 condition "any branch change ... needs a further delta" is not triggered for this record's L1 lens.

**Independence (rule C4).** This invocation authored no part of CR-008, of its sections 6 to 9, of steps 3 and 5, of this record's iterations 1 and 2, or of the INSP-003 and INSP-025 deltas at `ebeb069`. It wrote the INSP-003 and INSP-008 updates at `e26ce46`, which are records, not this product. It edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (query: CR-008 SRR liens, REQ-SYS-194, INSP-003 and INSP-008 delta). After it, `git diff -U0 5e6ceb62 aa65e826` and `sed -n` only pinned lines.

### Hunks read (`git diff -U0 5e6ceb62 aa65e826`: 16 hunks, 94 insertions, 16 deletions)

| Hunk (new lines) | Section | Change | Effect on this record (L1 lens) |
|---|---|---|---|
| 4; 17 and 18 | Front matter | `status` Submitted to Dispositioned; `disposition` Approved, `disposition_date` 2026-09-28 | Consistent with section 7 and with the 05 section 5.2 state table (Dispositioned: the owner records the decision and the class). `affected_ids`, `affected_paths` and `affected_cis` are unchanged from revision 2. No L1 field is affected |
| 162, 164, 166 | 5 | "Done (SHA)" cells of steps 3, 5 and 7 filled (`a36a828`, `a36a828`, `ebeb069`) | Only the Done column changes. The artifact, the responsible role and the ordering of every step are unchanged, including step 9 read at iteration 2. The SHAs resolve on the branch (`git log c629198..e26ce46`). The step 7 cell says that INSP-003 and INSP-008 need further deltas. Both are now on the branch at `e26ce46` (INSP-003 section "CR-008 allocation delta", INSP-008 section "CR-008 hazards delta"), so the cell is out of date but not wrong, and it is left for the CM record |
| 236 to 255 | 6.3 (new) | Impact review round 2: R1-F1 Verified; new Minor R2-F1 (the HZ-010 K5 undirected 50 ms), R2-F2 (WP-PDR-36a routing), R2-F3 (closure of the 10 ms removal TBR, bookkeeping) | Reviewer text, not the author's. It confirms the revision 2 Interfaces row, which the iteration 2 CK-REQ-C2 answer relied on. None of R2-F1 to R2-F3 names an L1 statement. R2-F1 is a hazard control text, and R2-F3 (a) is an ICD TBR with no bench source. From the L1 lens this reviewer concurs, without counting them here |
| 258 to 275 | 7 | Disposition: Approved, Class I, 2026-09-28, no owner conditions; rationale accepts R1-F2 to R1-F5 and R2-F1 to R2-F3 as liens; source transcribed from `status-2026-09-28.md` section 1 (`e288add`) | The CR was dispositioned without a revision. So, under rule C1, finding-1 of this record becomes a lien due at the CDR readiness declaration, as the iteration 1 counts said it would. Section 12 records question 2 answered 2a, so REQ-SYS-077 keeps its frozen statement and the iteration 2 CK-REQ-C2 answer stands |
| 279 to 296 | 8 | Implementation record for steps 1, 2, 3, 5 and 7, with the `ebeb069` and `a36a828` rows of the commit table | Checked against the branch: the commit list and file sets are exact, and the new blobs are `416b3e19` and `028facf7`. The step 5 text says "seven hunks", but `git diff` shows six (editorial; INSP-003 "CR-008 allocation delta"). No L1 blob changes |
| 305 to 347 | 9 | Configuration manager pre-merge check (2026-09-28) and its update (2026-09-29) | CM record, not the independent verification (which is still pending, as it says). Its note that this record names the CR at `5e6ceb62` is what this delta clears. Items (a) and (b) of its blocker list are now done on the branch (`a36a828`, `e26ce46`) |
| 352 | 10 | "Owner merge approval" filled with the 2026-09-28 disposition reading | Disagrees with section 9 item (d) and with plan S1 OD-43: **finding-2** (Minor, Open) |
| 365 to 367 | 11 | History rows for round 2, the disposition and the 2026-09-29 pre-merge check | Status record only. The rows agree with sections 6.3, 7 and 9 |
| 377 and 378 | 12 | Answers recorded with the disposition: Q1 Class I, Q2 accepted with 2a, Q3 and Q4 accepted | Q2 with 2a means no L1 blob changes, as the iteration 2 row for section 12 foresaw. Q3 confirms the REQ-SYS-083 and REQ-SYS-194 split that iteration 1 reviewed |

Sections 1 to 4, 6.1 and 6.2, and every section 5 cell other than the three Done cells, are byte-identical between `5e6ceb62` and `aa65e826`. The diff has no hunk there.

### Findings at the re-pin delta

| Finding | Severity | State | Basis |
|---|---|---|---|
| finding-1 | Minor | Lien (rule C1; due at the CDR readiness declaration) | Was Open. CR-008 was dispositioned Approved on 2026-09-28 without a revision, and section 7 accepts the section 6 Minors as liens |
| finding-2 | Minor | Open (fix before the merge; record text only) | New at this delta: CR-008 section 10 "Owner merge approval" against section 9 item (d) and plan OD-43 at S1 (findings table) |

### Items revisited

| Item | Answer at this delta | Evidence |
|---|---|---|
| CK-REQ-D4 (finding-1) | No (unchanged) | REQ-SYS-089 and 167 are unchanged in the frozen blob. finding-1 moves from Open to Lien under rule C1, due at the CDR readiness declaration (CR-008 section 7 accepts the section 6 Minors as liens, and no revision was made before the disposition) |
| CK-REQ-C2 | Yes (unchanged) | Question 2 was answered 2a, so REQ-SYS-077 is unchanged, and the ICDs align through step 9 before the ICD baseline |
| CK-REQ-B7 | Yes (unchanged) | The downstream list is unchanged. Steps 3 and 5 are done on the branch, and steps 4, 6 and 9 are still downstream |
| R5 | Yes, with finding-2 | The impact assessment is unchanged and attached. The section 10 cell misstates the owner's merge approval point |

### Record verdict at the re-pin delta

`reviewer_verdict: APPROVED`. No Major finding is open. finding-1 is a Lien, and the new finding-2 is a Minor record-text defect to fix before the merge. `product_files` names the CR at `aa65e826` and the four branch blobs at `c629198`. `verdict` stays NEEDS CHANGES under the lead SE convention, because the four reviewed blobs exist only on the unmerged branch. The software lead sets APPROVED in the merge commit.

Note for the merge (lead SE, software lead): the merge and its CM record will change the CR file again (`merge_sha`, sections 8 to 10, and the finding-2 fix). When the verdict is set, re-pin after a delta of those hunks, or take the CR file out of `product_files`. The second is enough if the delta finds, as here, that sections 1 to 5 changed only in the Done cells.

```
VERDICT (re-pin delta, 2026-09-29): APPROVED (record verdict held at NEEDS CHANGES until CR-008 merges; drift rule)
FINDINGS: finding-1 [Minor] Lien (rule C1, due CDR readiness declaration); finding-2 [Minor] new, Open: CR-008 section 10 "Owner merge approval" cell against section 9 (d) and plan OD-43 at S1; fix before the merge
PRODUCTS: CR-008@aa65e826 (was 5e6ceb62); requirements.json@a7344937, requirements.md@4e110b16, test_cases.json@117c08de, test_cases.md@00e4454f (c629198, equal at the branch head e26ce46)
MEASUREMENTS (re-pin delta): hunks=16; files_changed=1; product blobs re-identified=4 of 4 unchanged; turns=12; minutes=25; major=0; minor_new=1
```

## Status re-pin delta (2026-09-29, main `9fda694`; WP-PDR-55; CR-008 section 5 step 10 at `c1955b3`)

**Scope (plan rule C1, record drift rule, lead SE rulings 1 and 2 of 2026-09-29).** Two things changed after the re-pin delta. (1) On the branch, step 10 (`c1955b3`, lead SE ruling 1) sets REQ-SYS-194 from `Draft` to `Active`. That changes two of this record's four product blobs: `requirements.json` `a7344937` becomes `c68584cf62895a6b0a6d4a5d45e19fd190dd1af1`, and `requirements.md` `4e110b16` becomes `47c2beaacc2037d08011b56b36efde90c4f334f0`. `test_cases.json` (`117c08de`) and `test_cases.md` (`00e4454f`) are unchanged. The branch head is now `92727f1` (the INSP-003 status delta, a record only), where all four blobs are equal to `c1955b3`. (2) On `main`, the CR file changed from `aa65e826` to `c1a52ab6e06f9123b0b78afad74d69bd01674254` in `b630269` (section 9 independent verification) and `1fe68cb` (IV-F1 to IV-F3, step 10). `main` has moved on to `9fda694`, and the CR file is still `c1a52ab6` there. Ruling 2 has a record re-pin drop the CR file from `product_files` when the CR sections the record reviewed are unchanged, and otherwise do a delta. This record reviewed sections 1, 4 and 5, the section 6.1 and 6.2 hunks, and at the re-pin delta the front matter `status` and every hunk. Section 5 gains step 10 and a sentence in its frozen-products paragraph, and the front matter `status` changes. So a delta is due, and it is done below.

**Independence (rule C4).** This invocation authored no part of CR-008 (sections 1 to 12, including `b630269` and `1fe68cb`), no branch commit that changes a product (`c629198`, `a36a828`, `c1955b3`), no earlier iteration or delta of this record or of INSP-045, and none of the INSP-003, INSP-025 and INSP-008 updates at `ebeb069` and `e26ce46`. It wrote the INSP-003 status delta at `92727f1` on the branch, which is a record, not this product. It edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: INSP-003 requirements-sys delta and `product_files`; the 02 section 8.3 status transitions; the T-12 check in `tools/traceability.py`). After it, only read-only Python over `git show`, `git diff` of the named commits and the tools in a scratch worktree of the branch were used.

### Delta of the L1 blobs (`git diff e26ce46 c1955b3`: 2 files, 4 insertions, 5 deletions)

| Check | Result |
|---|---|
| `requirements.json`, record by record | 191 records at both commits, the same ids in the same order, top-level keys unchanged. The only differing record is REQ-SYS-194, and its only differing field is `status`, `Draft` to `Active`. Every other field of every record, including the 145 rows of this record's per-requirement validation table, equals `a7344937`. So no validation row, lien row or checklist answer changes, except the status wording noted below |
| Transition (02 section 8.3 row 2) | REQ-SYS-194 is added after the L1 baseline (`baseline/srr` does not hold it). The approved CR that adds it is the trigger. CR-008 lists it in `affected_ids`, section 1.1 held it at `Draft` "until this CR is approved", and the front matter records `disposition: Approved`, `disposition_date: 2026-09-28`. `tools/traceability.py` does not implement T-12 yet, so this was checked by reading. No forbidden transition occurs |
| Active-status rules (02 section 8.2) | T-09: TC-SYS-116 (Analysis, Simulation) cites it. T-11: no parent. T-14: the `tbr` object is admitted on `Active`, `close_by` PDR. T-18 (from PDR): no child and no `leaf` tag, the same as REQ-SYS-083 and 150 other `Active` L1 requirements, which is the general L2 allocation work of PDR. The CK-REQ-B7 routing gap for REQ-SYS-194 is R1-F5 (b) of CR section 6.1, a lien accepted with the disposition (cross item X-6) |
| `requirements.md` | Three changed spots, each derived from the one field: the summary table (`Status Active` 188 to 189, and the `Status Draft 1` row removed), the index row (`Draft (TBR)` to `Active (TBR)`) and the section 3 `Status` row. `tools/traceability.py --report-only --render` on a worktree of `c1955b3` left every tracked file unchanged |
| Tools on the branch | `tools/traceability.py`: 246 requirements, 174 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and 148). `tools/validate_docs.py` at `92727f1`: 50 passed, 0 failed. `tools/check_commit_msg.py --range e26ce46..c1955b3`: PASS |

The lien row for INSP-003 finding-12 and finding-30 counts "189 live entries (188 Active, 1 Draft)". That was right for `a7344937`. At `c68584cf` the same 189 entries are 189 `Active`, and every rationale is unchanged, so the row's result stands.

### Hunks read (`git diff -U0 aa65e826 c1a52ab6`: 14 hunks, 38 insertions, 16 deletions; L1 lens)

| Hunk (new lines) | Section | Change | Effect on this record |
|---|---|---|---|
| 4 | Front matter | `status` Dispositioned to Implemented | Consistent with section 8, which says every step placed on the branch is done (1, 2, 3, 5, 7, 10), that steps 4 and 6 follow the merge and step 9 is off the branch, as the disposition accepted, and that `c629198` fails the trailer condition of 05 section 5.2 and is covered by deviations entries 8 and 9. No L1 field is affected. Whether "Implemented" may be set with the post-merge steps still open is for the independent verifier's re-check of IV-F3 (cross item X-8) |
| 166, 168 | 5 | Step 7 Done cell adds `e26ce46`; new step 10 (REQ-SYS-194 `Draft` to `Active`, TC-SYS-116 stays `Draft`, the deltas, the ruling 2 re-pin rule) | Step 10 is the change checked in the table above. Its content equals `c1955b3`: one field and its render. Its reading of 02 section 8.4 for TC-SYS-116 is right: a test case moves to `Active` on the procedure-checklist review, not on the CR. Its Done cell still says "Deltas: pending", which this record, INSP-045 and INSP-003 at `92727f1` now answer (for the CM record) |
| 171 | 5 | Frozen-products paragraph: after step 10 the two requirement blobs are `c68584cf` and `47c2beaa`, differing only in the REQ-SYS-194 status field and its three render cells | Verified above: exact |
| 177, 179 | 6 | Lead text now points to rounds 6.1 to 6.3 and records the concurrence of round 6.3 | Agrees with sections 6.1 to 6.3 as read at iteration 2 and the re-pin delta |
| 276, 278, 283, 289, 292 to 295 | 8 | Implementation state, the `e26ce46` and `c1955b3` rows, and the `c629198` correction of record | Checked against the branch: file sets and blobs are exact. The `c629198` row now lists the three `check_commit_msg.py` failures instead of "Present" and cites deviations entries 8 (`c9f611d`) and 9 (`48f596a`). No L1 content is affected |
| 303 to 323 | 9 | Independent verification table and IV-F1 to IV-F3 | Verifier text. Its L1 rows (statements, rationales, notes, `tbr`, ADR citations) agree with this record's lien table. IV-F2 is the step 10 trigger |
| 372 | 10 | "Owner merge approval": "Pending: the owner's merge approval for this CR is asked at S1 (OD-43, WP-PDR-55 merge batch 1) ..." and the 2026-09-28 entry kept as the disposition's context | This is the fix that finding-2 asked for: **finding-2 Verified** |
| 388 and 389 | 11 | History rows for the section 9 verification and the step 10 and IV fixes | Status record only. They agree with sections 5, 8 and 9 |

Sections 1 to 4, 6.1 to 6.3, 7 and 12 are byte-identical between `aa65e826` and `c1a52ab6`, and so is every section 5 row other than steps 7 and 10 and the frozen-products paragraph.

**Why the CR file is dropped from `product_files` after this delta (ruling 2).** Every CR section this record reviewed has now been read at `c1a52ab6`. What is still to come in the CR file is record text: the section 5 Done cells (step 10, step 8), sections 8 to 11, and the front matter `status` and `merge_sha` at the merge. A pinned CR blob would drift at the merge commit, which is the very commit that sets this record's verdict. So the entry is removed and the reviewed text stays named here (`c1a52ab6`), as INSP-060 did. The condition for the merge: `git diff c1a52ab6 <merge HEAD> -- docs/cm/cr/CR-008-srr-liens-l1-and-tc-sys.md` changes nothing in sections 1 to 4, 6 and 7, and nothing in section 5 except Done cells. Otherwise a further delta of this record is due before the verdict is set.

### Findings at the status re-pin delta

| Finding | Severity | State | Basis |
|---|---|---|---|
| finding-1 | Minor | Lien (rule C1; due at the CDR readiness declaration; unchanged) | REQ-SYS-089 and 167 are unchanged at `c68584cf` |
| finding-2 | Minor | Verified (closed; was Open) | CR-008 section 10 at `c1a52ab6` puts the merge approval at S1 (OD-43) and keeps the 2026-09-28 reading as the disposition (hunk 372) |

No new finding. Open Major 0 and open Minor 0.

### Items revisited

| Item | Answer at this delta | Evidence |
|---|---|---|
| CK-REQ-D4 (finding-1) | No (unchanged) | As at the re-pin delta |
| CK-REQ-F1 to F4, E6 | Yes (unchanged) | The status change adds no redundancy or conflict. REQ-SYS-194 keeps its closing case, and 189 of 189 live requirements are covered |
| R1 | Yes | The four product blobs pass their schemas. `tools/validate_docs.py` on the branch at `92727f1`: 50 passed, 0 failed. On `main` with this update, this record passes (held verdict) |
| R2 | Yes | 0 violations on the branch at `c1955b3` |
| R5 | Yes (finding-2 Verified) | The impact assessment is unchanged, and the section 10 cell now states the merge approval point correctly |

### Cross items added

- X-8 (independent verifier, the re-check of IV-F1 to IV-F3 that CR-008 section 11 lists as blocking). 05 section 5.2 defines Implemented as all branch commits carrying `CR: CR-008` and every affected artifact updated. At `c1a52ab6`, `c629198` fails the trailer condition (covered by deviations entries 8 and 9, the owner's S1 ruling), the record-only commits `ebeb069`, `e26ce46` and `92727f1` carry no `CR:` trailer (section 8: "Not required (records only)"), and `hazard-analysis.md`, `register.json` and the three ICDs in `affected_paths` wait for steps 4, 6 and 9 after the merge. Section 8 discloses all of this, so it is not a finding here. The verifier confirms that this is an accepted reading of the state table.
- X-9 (configuration manager). The CR-008 step 10 Done cell ("Deltas: pending") and the section 8 commit table need the three delta commits: INSP-003 at `92727f1` on the branch, and this record and INSP-045 on `main`. Under the condition above, those edits are Done cells and record text, so they do not require a further delta of this record.

### Record verdict at the status re-pin delta

`reviewer_verdict: APPROVED`, readiness met. No Major finding is open. finding-1 is a Lien, and finding-2 is Verified. `product_files` names the two step 10 requirement blobs and the two unchanged case blobs, all at `c1955b3`, with the CR file dropped as explained above. `verdict` stays NEEDS CHANGES under the lead SE convention, because the two requirement blobs exist only on the unmerged branch. The software lead sets APPROVED in the CR-008 merge commit, once `git rev-parse HEAD:<path>` equals each `product_files` blob and the CR-file condition above holds.

```
VERDICT (status re-pin delta, 2026-09-29): APPROVED (record verdict held at NEEDS CHANGES until CR-008 merges; drift rule)
FINDINGS: finding-1 [Minor] Lien (rule C1, due CDR readiness declaration); finding-2 [Minor] Verified; no new finding
PRODUCTS: requirements.json@c68584cf, requirements.md@47c2beaa (c1955b3; were a7344937, 4e110b16); test_cases.json@117c08de, test_cases.md@00e4454f (unchanged); CR-008 read at c1a52ab6 and dropped from product_files (lead SE ruling 2)
MEASUREMENTS (status re-pin delta): hunks=2 files on the branch plus 14 in the CR file; product blobs re-identified=4 (2 new, 2 unchanged); turns=16; minutes=30; major=0; minor_new=0
```
