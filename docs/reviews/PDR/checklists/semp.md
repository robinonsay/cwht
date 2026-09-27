---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, section G (all items) and CK-REQ-A8, the
# "Plans and process documents" row (docs/plan/semp.md is named there). Record path named by
# docs/plan/pdr-work-plan.md section 3.1 "Records" for WP-PDR-13 ("INSP-005 delta iterations"). This record is the
# PDR delta iteration of INSP-005 (docs/reviews/SRR/checklists/semp.md) on the CR-013 prototype. Product frozen at
# branch commit 41c588c (rule C2); the SEMP blob exists only on branch cr/CR-013-process-04-07-semp-srr-liens (lead
# SE convention of 2026-09-27, INSP-031 practice).
id: INSP-064
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/semp.md
product: docs/plan/semp.md
product_commit: "41c588cddc9a97cec536482dc2bd164e2bf81ea3"
product_files: ["docs/plan/semp.md@2076eb0acfdfc283483eb2340bcbbf985df00c72"]
# input_files: the change record (main 8470350), the baseline SEMP blob and the charter edit list it points to (Informational)
input_files: ["docs/cm/cr/CR-013-process-04-07-semp-srr-liens.md@560fe69a6c4e91a0c0221e51d5b5e4452204f42a", "docs/plan/semp.md@ccfdecf98a6e2dc1371eb057e6aa37903b672de1", "docs/reviews/PDR/owner-actions.md@0ed18f4c2869c7065cac8ff3c2c65d61babcdd4e"]
product_size: Appendix J outline, 9 sections and appendices A to F (488 lines at 2076eb0a); delta 13 change items, 20 insertions, 20 deletions against ccfdecf9
sprint: PDR-prep
author_agent: "author:WP-PDR-13 (Claude, lead SE as SEMP author; CR-013 originator)"
reviewer_agent: "reviewer:semp (new invocation for WP-PDR-13; authored no part of WP-PDR-13 or CR-013)"
criticality: neither
# assurance_required: false, as INSP-005: the SEMP is not a 07 section 2.1.1 "Software plans" product (its software
# content is 07's) and tools/validate_docs.py ASSURANCE_WHOLE_PRODUCTS does not name it
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
# readiness_met: false. R1 fails at 41c588c (validate_docs 43 passed, 7 failed, all record drift CR-013 states)
readiness_met: false
# reviewer_verdict: APPROVED. INSP-005 finding-10 to finding-13 Verified; no Major; one new Minor finding is a lien due the
# CDR readiness declaration (plan rule C1)
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES while the reviewed blob is on the CR branch only; set APPROVED in the CR-013 merge commit
# (or the commit right after it) when the SEMP reaches main at blob 2076eb0a
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 1
findings_open: 1
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [R1, CK-REQ-G7]
effort_turns: 14
effort_minutes: 25
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-064: SEMP version 0.5, PDR delta of INSP-005 (CR-013, WP-PDR-13)

**Product.** `docs/plan/semp.md` blob `2076eb0a` (version 0.5) on branch `cr/CR-013-process-04-07-semp-srr-liens` at `41c588c`; base blob `ccfdecf9` (version 0.4) at `baseline/srr`, `5cd87cf` and `main` (CR-010 does not touch the SEMP). Identity checked with `git ls-tree 41c588c` and `git rev-parse`. The change was read as `git diff --word-diff 5cd87cf 41c588c -- docs/plan/semp.md` and every hunk was checked against INSP-005 and the tree. Change record: CR-013 blob `560fe69a`, section 1.3 items 1 to 13.

**Checklist and acceptance criteria (rule C7).** `docs/templates/peer-review-checklist-requirements.md` revision C, section G and A8. Cases, each checked: INSP-005 finding-10, finding-11, finding-12 at every one of the eight locations it names (Appendix E rows OQ-SE-001, 003, 005 and 006; section 3.4; section 9.0; section 6.0; section 7.4; F-12), and finding-13; the section 7.1 component list against charter section 10 and 07 section 14.1 at `5cd87cf`; the section 4.3 allocation row and Appendix F items F-06, F-08, F-09 and F-15 against the tree; that no other line changed. `docs/reviews/PDR/owner-actions.md` section 11 (CE-1 to CE-3) is Informational and needs no record. It was read because F-08 and OQ-SE-001 point to it: CE-1 exists, and its before text equals charter section 12 HSI row verbatim.

**Independence (rule C4).** This invocation authored no part of WP-PDR-13 or CR-013 and edits no product file. **Search first.** `mcp__claude-context__search_code` ran before the manual searches that pinned lines (queries as INSP-058; the one prior plan-heading grep is the deviation recorded there). **LTspice** was not run.

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 | No (disclosed by the CR, no finding) | At `41c588c`: 43 passed, 7 failed, the SRR record drift CR-013 names (INSP-058 R1) |
| R2 | `tools/traceability.py` no violation | Yes | 0 violations, 2 warnings at `41c588c` |
| R3 | Author self-check and acceptance criteria | Yes | CR-013 section 5 verification list names the eight finding-12 locations; section 1.3 table |
| R4 | No `TBD`; TBRs complete | Yes | Added lines: 0 hits; 0 em dashes in blob `2076eb0a` |
| R5 | CR impact assessment attached | Yes | CR-013 section 4 (CR-013 section 6.1) |

## Verification of the INSP-005 liens (delta)

| INSP-005 finding | Location in blob `2076eb0a` | Check | Result |
|---|---|---|---|
| finding-10 | Section 4.3 tool-status paragraph | Rewritten at `main` `7bb994f`: `tools/measurements.py`, `tools/unsafe_audit.py`, `tools/complexity_gate.py` first committed at `3de1e2d`, `tools/sw_gate.sh` and both schemas at `1d423e5`, `tools/ltspice-batch.sh` at `41d150e` (`git log --diff-filter=A`). TV states match the files: TV-011, TV-012 and TV-013 Validated, TV-014 not validated. Accreditation gates match 05 section 13 (measurements PDR; unsafe audit and complexity gate CDR). `test_measurements.py`, `test_unsafe_audit.py`, `test_complexity_gate.py` and `test_ltspice_batch.py` exist at `7bb994f`. The file count is finding-1 | Verified (with finding-1) |
| finding-11 | Section 7.2 row "Documentation data" | Names `tools/sw_gate.sh`, `tools/measurements.py`, `tools/unsafe_audit.py`, `tools/complexity_gate.py` (all exist; gates G2, G3, G5, G6 of 07 section 8.4) and `tools/ltspice-batch.sh`; "(planned)" is gone | Verified |
| finding-12, App. E OQ-SE-001 | Row | "Closed 2026-09-26: confirmed (SRR decision 2 ...)"; memo row 4.4-10 reads "Decision 2 confirms HSI as a SEMP section" | Verified |
| finding-12, App. E OQ-SE-003 | Row | "Closed ... approved with the SE-51 and SE-52 scope relief (SRR decision 4)"; memo lines 167 to 172 record SE-51, 52, 55 and 56 T "yes (decision 4)" | Verified |
| finding-12, App. E OQ-SE-005 | Row | "Closed ... add and re-parent (SRR decision 96)"; memo RID-SRR-008 row cites decision 96 "add and re-parent"; MOE-013 "Pocket carry and field ruggedness" is in `expectations.json` (Draft); the `tpm.json` re-parenting is sent to WP-PDR-29 (MOP-001 and MOP-002 `moe_ids` still `[MOE-001]` on `main`, as stated). The row now carries "(§7.4)" twice (observation O-2) | Verified |
| finding-12, App. E OQ-SE-006 | Row | "Closed ... accepted (SRR decision 11; the SRR decision memo residual-risk list), to be reconfirmed in the CDR decision memo"; memo line 378 "RSK-008 (hardware TRL 3 at the CDR procurement release, decision 11; reconfirmed in the CDR memo)" | Verified |
| finding-12, section 3.4 | DR and DRR paragraph | Past tense, "SRR decision 4 ... OQ-SE-003 closed" | Verified |
| finding-12, section 9.0 | First paragraph | "approved by the owner at SRR (SRR decision 4; OQ-SE-003 closed)" | Verified |
| finding-12, section 6.0 | Gate rule for RF hardware | "The owner accepted at SRR ... (SRR decision 11 ...; OQ-SE-006 closed ...) and reconfirms it in the CDR decision memo" | Verified |
| finding-12, section 7.4 | MOP paragraph | Ruling stated (decision 96, OQ-SE-005 closed) with the `tpm.json` state and its writer | Verified |
| finding-12, F-12 | Appendix F | "acceptance part resolved 2026-09-26: the owner accepted it at SRR (SRR decision 11; SRR decision memo residual-risk list), reconfirmed in the CDR memo" | Verified |
| finding-12, section 7.3.1 (not in the finding's list) | Decision sentence | Also restated (decision 2, OQ-SE-001 closed); consistent | Correct |
| finding-13 | Section 9.0 customization row 11 item (ii) | Adds "where the research analysis leaves one viable option" and cites the section 5.17 precondition and ruling R-2. "value or policy" matches section 5.17 item (ii) (line 286), so the row no longer states a wider customization than decision 106 | Verified |
| Section 7.1 component list | Safety-critical determination sentence | Equal to charter section 10 (keying, PA enable, charging supervision, thermal protection, audio output limiting, the shared safe-state manager with the boot path, configuration guard and fault annunciation, the menu override command path, the scheduler and runtime, the transmit frequency-word path with the frequency verification unit; mission-critical: remainder of frequency control, configuration store and non-safety fields, key-input and keyer-mode selection path). 07 section 14.1 at `5cd87cf` carries the same components. The SEMP adds "(SRR decisions 9 and 40 ...)" and names 07 section 14.1 as the single authoritative list, as charter section 10 does | Correct |
| Section 4.3 allocation row; F-06 | Table row; Appendix F | T-18 a Warning, an Error under `--gate`, which CR-011 adds (CR-011 tool blob `d4cde9f5` has `--gate`); T-15 codes due PDR (02 section 8.5); F-06 names CR-011 `CLOSED_NOT_INSTALLED` (on the CR-011 branch, 2 occurrences) | Correct |
| F-08, F-09, F-15 | Appendix F | F-08 names CE-1 (exists in owner-actions section 11); F-09: charter section 5 at `6ea6b1d` has "Status notes between reviews" (`git log -S` first at `6ea6b1d`); F-15: `tools/ltspice-batch.sh` at `41d150e`, `tools/scad2step.py` not in `7bb994f` (true at the observed commit; see O-1) | Correct |
| No other line changed | Whole file | The SEMP hunks are the 13 items of CR-013 section 1.3; the Version row keeps 0.4 as the previous version | Correct |

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Terms match the tree and the memo; 0 em dashes |

CK-REQ-A1 to A7 and sections B to F: N/A (product type "Plans and process documents").

## G. Plans, process documents and decision records

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | Yes | The changed text agrees with charter sections 3, 10 and 12, the SRR decision memo, the compliance matrix T rows and ADR reconciliation R-2 |
| CK-REQ-G2 | Yes | Each re-stated item names its artifact and writer (WP-PDR-29 for `tpm.json`; CE-1 with OD-31) |
| CK-REQ-G3 | Yes | Owner approval points stated in the past tense with decision numbers |
| CK-REQ-G4 | Yes | SE-55 and SE-56 deviation and SE-51 and SE-52 relief mirrored as the matrix records them |
| CK-REQ-G5 | N/A | No cybersecurity text changed |
| CK-REQ-G6 | Yes | Section 7.4 MOP linkage and its pending `tpm.json` re-parenting are stated with the writer |
| CK-REQ-G7 | No | Test-file count (finding-1) |
| CK-REQ-G8 | Yes | SE-40, SE-55, SE-56, NPR 7123.1D section 5.2.1.3 and SE HB section 6.8.1.2.2 exist in the corpus (unchanged citations) |

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G7 | SEMP section 4.3 tool-status paragraph ("16 `test_*.py` files on 2026-09-27") | At `7bb994f`, the commit the paragraph names, `tools/tests/` holds 15 `test_*.py` modules. A clean-worktree run loads 15 and runs 461 tests. 04 section 7.4 of the same CR repeats "16" (INSP-058 finding-1). Fix: "15" | Open (Lien: fix before the CDR readiness declaration, plan rule C1) | Pending | |

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien (plan rule C1) | SEMP author (Claude, lead SE) | CDR readiness declaration (or at the CR-013 rebase, step 5) |

INSP-005 liens after this delta: finding-10, 11, 12 and 13 Verified on blob `2076eb0a`. The SRR record still names blob `ccfdecf9`; its update at the merge is CR-013 section 6.1 IR-F1.

## Observations (not findings)

- **O-1 (merge-time staleness).** Section 4.3 and F-15 are dated at `main` `7bb994f`, and on that commit they are true. `main` commit `86ff3b0` (2026-09-27 12:45, after the prototype at 12:34) added `tools/render_tpm.py` and `tools/scad2step.py`, among others. Section 4.3 still says "`render_tpm.py` is written by Claude before PDR", and F-15 says "`tools/scad2step.py` not yet committed". Both go stale at the merge unless they are re-stated (CR-013 section 6.1 IR-F2).
- **O-2.** Appendix E row OQ-SE-005 ends "re-point MOP-001 and MOP-002 to it (§7.4). Closed ... WP-PDR-29's (§7.4)": the "(§7.4)" is duplicated. Editorial.
- **O-3.** Section 4.3 dates TV-012 accreditation "due CDR", as 05 section 13 does. CR-007 (Submitted) C13 proposes the note "TV-012 ... was accredited early, ACC-COMPLEXITY-001", and 07 section 8.3 of this CR sends the scope confirmation to OD-27. That is consistent with the baseline; re-check it if CR-007 is approved as written.

## Completion

Readiness R1 No (the CR discloses it; it clears at step 5), R2 to R5 Yes. Section G and A8 answered. No Major finding. One new Minor finding is a lien due the CDR readiness declaration. `reviewer_verdict: APPROVED`. The record `verdict` is held at NEEDS CHANGES while blob `2076eb0a` exists only on the CR branch. It is set APPROVED, with `readiness_met: true`, in the CR-013 merge commit or the commit right after it, if the blob reaches `main` unchanged. The CR-003 and CR-006 hunks of the Version row (CR-013 section 4 Schedule) would change the blob and need a delta iteration.

```
VERDICT: APPROVED (reviewer_verdict); record verdict held NEEDS CHANGES until the CR-013 merge (lead SE convention 2026-09-27)
FINDINGS:
- [Minor] finding-1 CK-REQ-G7 SEMP s4.3: "16 test_*.py files"; 7bb994f has 15.
VERIFIED: INSP-005 finding-10, finding-11, finding-12 (all eight locations, plus s7.3.1), finding-13; s7.1 list = charter s10 and 07 s14.1.
ITEMS N/A: CK-REQ-A1 to A7, sections B to F; CK-REQ-G5
MEASUREMENTS: size=9 sections plus App. A to F, 13 change items; items checked=R1 to R5, A8, G1 to G8 plus 17 delta rows; items no=R1, G7; major=0; minor=1; verified liens=4 (INSP-005); turns=14; minutes=25; iteration=1
```
