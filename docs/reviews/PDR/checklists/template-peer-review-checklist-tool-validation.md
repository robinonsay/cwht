---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, section G and CK-REQ-A8, as PDR work plan
# WP-PDR-03 names. Product: the new tool validation checklist template of CR-012 (Submitted, Class II),
# frozen on branch cr/CR-012-pdr-checklist-templates at ac9b7a5 for iteration 1 and at 7784672 for the
# iteration 2 delta (rule C2). The 08 delta and the CR-012
# checks shared by the three WP-PDR-03 records are in INSP-031
# (docs/reviews/PDR/checklists/template-peer-review-checklist-analysis.md).
id: INSP-033
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/template-peer-review-checklist-tool-validation.md
product: docs/templates/peer-review-checklist-tool-validation.md
# product_commit: iteration 2 delta at the branch head 7784672 (iteration 1: ac9b7a5)
product_commit: "778467249fe42d59706e3c4beb7bcb893d7b2671"
product_files: ["docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900", "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4", "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921", "docs/process/08-agent-briefing.md@56c540113110b0d8916219d3cb531d6a76587713", "docs/cm/cr/CR-012-pdr-checklist-templates.md@91c8c6261a4b2bd9b3d789676c1188b54f022ddd"]
product_size: 1 template (257 lines, sections R, A to H, per-record and per-purpose tables)
sprint: PDR-prep
author_agent: "author:WP-PDR-03 (Claude as checklist owner)"
reviewer_agent: "reviewer:WP-PDR-03-templates"
# criticality and assurance: a TV review checklist is not a product type of 07 section 2.1.1; no tool is
# safety-critical or mission-critical (03 section 4.3.1)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
# reviewer_verdict: APPROVED at iteration 2 (finding-1 and finding-2 Verified; finding-3 Minor lien, rule C1)
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES on the completion criterion "validate_docs.py passes on the record" only.
# The reviewed blobs are on the CR branch, not in main HEAD; tools/validate_docs.py fails an APPROVED record
# whose product_files are not in HEAD (record drift rule; same hold as INSP-031). The software lead sets
# APPROVED when CR-012 merges with these blobs unchanged (section "Iteration 2", "Record verdict")
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 1
# findings_open: 0 at iteration 2; finding-3 (Minor) is a lien due the CDR readiness declaration (PDR work
# plan rule C1, lesson L1), listed in the iteration 2 lien table, not a Deferred RID
findings_open: 0
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: empty at iteration 2 (CK-REQ-G1 and CK-REQ-G7 were No on finding-1 and finding-2, now Verified;
# CK-REQ-G8 was "Yes, with finding-3")
items_no: []
# effort: iteration 1 (16 turns, 30 min) plus iteration 2 delta (14 turns, 20 min)
effort_turns: 30
effort_minutes: 50
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-033: tool validation checklist template (WP-PDR-03, CR-012)

**Product:** `docs/templates/peer-review-checklist-tool-validation.md`, blob `c94fa383`, on branch `cr/CR-012-pdr-checklist-templates` at `ac9b7a5` (identity checked with `git ls-tree ac9b7a5`). **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G and CK-REQ-A8 (PDR work plan WP-PDR-03). **Acceptance criteria (rule C7):** SRR decision 117 (`docs/reviews/SRR/decision-memo.md` line 329: "Accept INSP-015's item set for SRR; Claude writes `docs/templates/peer-review-checklist-tool-validation.md` before the PDR TV set"), so every INSP-015 item TV-S1 to TV-S10 and every INSP-015 finding class must be carried; every clause of 05 section 9.2 steps 1 to 5 and of its known-answer table; every tool class and kind of 05 section 9.1 and section 13; and the template must be usable as written, which includes its own completion criterion that `tools/validate_docs.py` passes on an APPROVED record.

**Independence (rule C4):** this invocation authored no part of WP-PDR-03 or CR-012 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: TV record section 8 Independent review, reviewer writes date, invocation and result). `grep -n` was used afterwards only to pin lines.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G1 | "Record" paragraph (line 107) and completion criteria (line 236, "section 8 of each record names this review") | The template tells the reviewer to write the date, its invocation and the result into section 8 of each TV record it reviews, "the only change it makes to a TV record (05 section 9.2 step 3)". This contradicts 08 section 1 INDEPENDENCE ("A reviewer never edits the product it reviews") and 08 section 3.2 ("Do not edit the product"), both baselined, and 07 section 10.2 ("the reviewer of each record updates its own record"). 05 section 9.2 step 3 only says the independent reviewer checks the TV record and the fixture; it assigns no write. SRR practice agrees with 08: section 8 of TV-004 to TV-010 was recorded "by Claude, software lead and tool owner" after INSP-015. The edit also changes the TV record's blob after the review, so the record's own `product_files` then drift, and the completion criterion makes APPROVED depend on that edit: the record cannot be both APPROVED and valid. Fix: section 8 is written by the TV record author (Claude as tool owner) after the review record is filed, citing its `INSP-NNN`; remove the section 8 condition from the completion criteria, or check it at the next delta iteration | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-REQ-G7 | Front matter comment and example on `product_files` (lines 28 to 31) | The template directs "a fixture directory is listed by its tree hash (git rev-parse <commit>:<dir>)" in `product_files`. `tools/validate_docs.py` compares `product_files` with `git ls-tree -r --full-tree HEAD` (lines 935 to 943), which lists blobs only, so a directory entry is "not in HEAD" and fails every APPROVED record under the record drift rule. The reviewer reproduced this: a probe record `tool-validation-tv-001-probe.md` with `tools/tests/fixtures/schema@<tree>` and verdict APPROVED in a scratch repository failed with "product_files: tools/tests/fixtures/schema@ba38d329 is not in HEAD; record drift rule". The template's completion criteria require `validate_docs.py` to pass on the record, so a record that follows the template cannot close. CR-012 section 9 did not detect it because its filled copies were not APPROVED and ran outside a git work tree (drift rule not applied). Fix: list each fixture file by its blob in `product_files` and give the tree hash in the record body or in a separate front-matter field the validator ignores; a validator change would be WP-PDR-09's (plan section 5.3) | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G8 | Item TV-G3-3 (line 217) | TV-G3-3 cites "the fallback of 07 section 9.4 item 3". In 07 section 9.4 item 3 is "Credit"; the fallback is item 6 ("Fallback", RSK-003). Fix: cite 07 section 9.4 item 6. (04 section 5.2 row `T-SW-ORDER` carries the same stale "07 section 9.4 item 3 fallback"; cross item for the 04 writer) | Open | Pending | |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product validates | Yes, with finding-2 | A filled copy as `tool-validation-tv-014-ltspice.md` (placeholders replaced by valid values only, verdict NEEDS CHANGES) passes `tools/validate_docs.py --root <export of ac9b7a5>`; the APPROVED case fails in a git repository (finding-2) |
| R2 | Traceability clean | N/A | No requirement or test case is touched |
| R3 | Author self-check | Yes | Author summary; CR-012 sections 1.1 and 9 |
| R4 | No TBD | Yes | `grep -n TBD` on the blob: none |
| R5 | CR impact assessment | Yes | CR-012 section 4 (INSP-031, section "CR-012") |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Agrees with 05 sections 9.1 (classes A, B, C; TV-A5 restates the class rule), 9.2 steps 1 to 5 (TV-A1 to TV-F5), 13 (TV-F2), 03 sections 4.3.1 and 6.1.1 (tool source reviewed as code, row "Peer review"; TV-G1-3), 04 section 4 (developer evidence until accredited; TV-F4) and charter section 11 rule 8 (TV-A6). Disagreement: the section 8 write (finding-1) |
| CK-REQ-G2 | Yes | Every item names the TV record section, command, blob, fixture or lock section it inspects; the per-record and per-purpose tables name their columns |
| CK-REQ-G3 | Yes | The reviewer is neither the TV record author nor the tool author (`tool_author_agent` field; "Used by"); accreditation stays the owner's (TV-F4, completion criteria) |
| CK-REQ-G4 | Yes | No tailored row relied on; SWE-136 and SWE-070 are FC in `rmm.json` |
| CK-REQ-G5 | N/A | No cybersecurity content |
| CK-REQ-G6 | Yes | SWE-089 fields; RE-RUN and MEASUREMENTS lines |
| CK-REQ-G7 | No | Tool claims checked: the LTspice example of TV-C4 equals the 05 section 9.2 table row (-3 dB within 1 %, `.log` version line, seeded-error netlist exit 1, time-out guard); the `kicad-cli` example equals its row; TV-G2-1 preconditions equal lock section 1.4 findings 1 to 4; the flock serialization of TV-G2-2 exists in `tools/ltspice-batch.sh` lines 19 to 21. False claim: a directory tree hash is accepted in `product_files` (finding-2) |
| CK-REQ-G8 | Yes, with finding-3 | SWE-136 and SWE-070 quotations are verbatim substrings of `npr-7150-2d/04-chapter4.md` lines 83 and 111; SWEHB `swe-136` and `swe-070` 7.1 task 1 exist with the stated text; SRR decision 117 pinned; 05 Table 4-1 rows 27, 28 and 30 exist with the stated content. Stale section number: finding-3 |
| CK-REQ-A8 | Yes | Terms match 05 section 9 (Validated, Reviewed, Accredited; purposes; known answer); no em dashes |

## Every case named (rule C7)

**INSP-015 items carried (SRR decision 117).** Each item of `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` lines 174 to 183 is carried with the same sense: TV-S1 (identification, commit tested) by TV-A1 to TV-A4; TV-S2 (class and one-line purposes) by TV-A5 and TV-B1; TV-S3 (fixture root, run command, pass criteria, seeded faults) by TV-C1, TV-C2, TV-C4; TV-S4 (every accredited purpose exercised) by TV-B3 and TV-C2; TV-S5 (result, count, excerpt, evidence file) by TV-C5 and TV-D1; TV-S6 (class A reproducibility) by TV-D3; TV-S7 (limitations and triggers) by TV-E1 and TV-E2; TV-S8 (expected answers independent of the tool) by TV-C3; TV-S9 (records exist, reviewed, accredited) by TV-F2 to TV-F4; TV-S10 (lock section 1.1 and section 5) by TV-D2 and TV-F3. All ten are carried.

**INSP-015 finding classes.** F-01 (purpose wider than its known answer) is TV-B3; F-02 (no result tied to a commit containing what was tested) is TV-A4 and R1; F-04 (limitation contradicted by the code) is TV-E1; F-05 (exit-code purposes without a known answer) is TV-G1-2; F-03 and F-07 (stale status statements) are covered by TV-F3; F-06 (a count error) is a Minor under the severity paragraph. All covered.

**05 section 9.2 steps and 05 section 9.1 and 13 tool set.** Step 1 fields are all checked (TV-A1 to TV-A5, TV-B1, TV-C1, TV-D1, TV-D3, TV-E1, TV-E2); step 2 by TV-D2; step 3 by TV-F4 and the Record paragraph (finding-1); step 4 by TV-E2 and the `revalidation` kind; step 5 by TV-F5. The four `tool_kind` values cover every class B and class A tool of 05 section 9.1 and every PDR, CDR and TRR TV record of 05 section 13, including the emulator (G3) and instrument firmware (G4).

## Verdict format

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-REQ-G1 the reviewer is told to edit section 8 of the TV records it reviews (contradicts 08 sections 1 and 3.2; drifts its own product_files; circular completion criterion).
- [Major] CK-REQ-G7 product_files guidance to list fixture directories by tree hash fails every APPROVED record under the validate_docs drift rule (reproduced).
- [Minor] CK-REQ-G8 TV-G3-3 cites 07 section 9.4 item 3; the fallback is item 6.
ITEMS N/A: CK-REQ-G5
MEASUREMENTS: size=1 template; items=9; items_no=2; turns=16; minutes=30; major=2; minor=1
```

## Iteration 2: delta verification of the Major fixes (2026-09-27, branch head `7784672`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the Major fixes only. Product: `docs/templates/peer-review-checklist-tool-validation.md` blob `7be809d4ceb9a202473eb19da3627fe0cd427900` at `7784672` (`git ls-tree 7784672` checked for all five `product_files` blobs; the CR-012 blob `91c8c626` checked with `git ls-tree 4552943`). `git diff --stat ac9b7a5 7784672`: 2 files, 25 insertions, 14 deletions (this template and the software assurance template, whose delta is in INSP-032). The fix commit carries the trailer `CR: CR-012` (CR-012 section 5 step 6).

**Independence (rule C4).** This invocation authored no part of WP-PDR-03, CR-012 or the fix commit, and edited no product file.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: WP-PDR-03 checklist templates review record path; iteration 2 delta verification record practice). `grep -n` was used afterwards only to pin lines.

### Verification of finding-1 and finding-2 (Major)

| Finding | Fix at blob `7be809d4` | Check | Result |
|---|---|---|---|
| finding-1: the reviewer was told to write section 8 of each TV record (against 08 sections 1 and 3.2 and 07 section 10.2), drifting its own `product_files`, with a circular completion criterion | Record paragraph (line 115): "The reviewer edits no TV record", citing 08 section 1 INDEPENDENCE and section 3.2 and 07 section 10.2. After this record is filed, the TV record author (Claude as software lead and tool owner) writes section 8; the owner's accreditation goes into section 9 and the lock. Those edits go in commits confined to sections 8 and 9, the status line and the README and lock status rows. A reviewer then re-issues the record at the same iteration and re-pins `product_files`. Completion criteria (line 244): the section 8 condition is removed and replaced by the statement that it is not a condition of this verdict | The 08 quotation "A reviewer never edits the product it reviews" is verbatim in 08 section 1 (INDEPENDENCE line). The SRR precedent holds: TV-004 section 8 line 72 reads "recorded by Claude, software lead and tool owner". The re-issue practice exists: INSP-015 "Re-issue 2 of iteration 3, post-SRR-ruling delta", which verified sections 8 and 9 after `b2d3538`. No other place in the template still assigns a TV record write to the reviewer (TV-F1 to TV-F5 only inspect the record, the index, the lock and the CR file). The circularity is gone: the record can be APPROVED and valid at filing, and the later author edits are handled by the re-issue | Verified |
| finding-2: a fixture directory listed by tree hash in `product_files` fails every APPROVED record under the record drift rule | Front matter lines 28 to 37: fixture files are listed one by one by blob, from `git ls-tree -r`; the new field `fixture_trees` carries each directory's tree hash, and its comment says the validator does not read it. R1 (line 141) follows | Reproduced on a `git archive` export of `7784672` made a git work tree. A filled copy of the template, `tool-validation-tv-012-complexity-gate.md`, had verdict APPROVED, `product_files` holding TV-012, `tools/complexity_gate.py`, `tools/tests/test_complexity_gate.py`, every file of `tools/tests/fixtures/complexity_gate/` by blob and `tools/toolchain.lock.md`, and `fixture_trees` holding the directory tree. Committed, `validate_docs.py --root <probe>` gave PASS under the drift rule. Negative control: the same record with the directory `tools/tests/fixtures/complexity_gate@23f23d9d` added to `product_files` gave FAIL ("is not in HEAD; record drift rule"). 01 section 13 lets templates carry fields the validator does not check, so `fixture_trees` breaks no field-list rule | Verified |

**Readiness at iteration 2.** R1 Yes (the filled APPROVED copy above passes with the drift rule applied). R2 N/A. R3 Yes (author summary; CR-012 sections 8 and 9 at `91c8c626`). R4 Yes (`grep -n TBD` on the blob: none; no em dash). R5 Yes (CR-012 section 4). `readiness_met: true`.

**Answers changed at the delta.** CK-REQ-G1 becomes Yes (finding-1 Verified; the template now agrees with 08 sections 1 and 3.2 and 07 section 10.2). CK-REQ-G7 becomes Yes (finding-2 Verified; the `product_files` guidance is true of `tools/validate_docs.py`). CK-REQ-G8 stays "Yes, with finding-3".

**Scan of the delta for new defects.** None found.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Major | Verified | Closed at iteration 2 on blob `7be809d4` (table above) |
| finding-2 | Major | Verified | Closed at iteration 2 on blob `7be809d4` (table above) |
| finding-3 | Minor | Lien: fix before CDR | TV-G3-3 (line 225) still cites "07 section 9.4 item 3"; not addressed at `7784672` (author election, rule C1). Owner: Claude as checklist owner; due the CDR readiness declaration; listed in PDR package section 15. The 04 section 5.2 `T-SW-ORDER` cross item stays with the 04 writer |

### Record verdict

The reviewer's verdict is APPROVED, with lien finding-3. The record `verdict` stays NEEDS CHANGES only because the reviewed blobs are on the CR branch, not in `main` HEAD. An APPROVED record would therefore fail the record drift rule of `tools/validate_docs.py` (the same hold as INSP-031). The software lead sets `verdict: APPROVED` when CR-012 merges with these blobs unchanged.

```
VERDICT (iteration 2, 2026-09-27): reviewer APPROVED (with lien finding-3); record verdict NEEDS CHANGES (held: branch-only blobs)
PRODUCT: cr/CR-012-pdr-checklist-templates at 7784672; peer-review-checklist-tool-validation.md 7be809d4
FINDINGS: finding-1, finding-2 Major Verified; finding-3 Minor lien due CDR; no Major open
ITEMS N/A: CK-REQ-G5
MEASUREMENTS: blobs re-checked 5; probe records 2 (positive, negative control); new findings 0; iteration 2 14 turns, 20 minutes; cumulative 30 turns, 50 minutes
```
