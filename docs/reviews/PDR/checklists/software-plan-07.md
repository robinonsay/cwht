---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, section G (all items) and CK-REQ-A8, the
# "Plans and process documents" row. Record path named by docs/plan/pdr-work-plan.md section 3.1 "Records" for
# WP-PDR-13 ("INSP-010, INSP-018 ... delta iterations (SA for 07)"). This record is the PDR delta iteration of
# INSP-010 (docs/reviews/SRR/checklists/software-plan-07.md) on the CR-013 prototype, which carries the CR-010
# change set (07 blob 3ae7d73b) as its base. Product frozen at branch commit 41c588c (rule C2); the 07 blob exists
# only on branch cr/CR-013-process-04-07-semp-srr-liens (lead SE convention of 2026-09-27, INSP-031 practice).
# Scope: the CR-013 hunks (git diff 5cd87cf 41c588c). The CR-010 hunks (git diff ab2af2d 5cd87cf) are reviewed by
# INSP-037 and INSP-050 and are not re-reviewed here.
# Re-pin delta (2026-09-29, lead SE ruling (2); section "Re-pin delta" at the end): no CR file is in product_files (the
# CR-013 file is an input_files entry, which the record drift rule does not read), so nothing is dropped; the 07 blob is
# unchanged at the CR-013 head 1a486e4. The pair fields now name INSP-073. Iteration stays 1: a re-pin delta is not a new
# review iteration (INSP-003 convention).
id: INSP-059
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/software-plan-07.md
product: docs/process/07-software-engineering-plan.md
product_commit: "41c588cddc9a97cec536482dc2bd164e2bf81ea3"
product_files: ["docs/process/07-software-engineering-plan.md@0ad37a43a9d365408b78488f6c2b02933af56837"]
# input_files: the change record (main 8470350), the CR-010 base blob (5cd87cf) and the baseline blob
input_files: ["docs/cm/cr/CR-013-process-04-07-semp-srr-liens.md@560fe69a6c4e91a0c0221e51d5b5e4452204f42a", "docs/process/07-software-engineering-plan.md@3ae7d73b01810e47fd10251d798e0a047aaa72dd", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8"]
product_size: 23 sections and annexes A to D (1010 lines at 0ad37a43); CR-013 delta 14 change items, 22 insertions, 26 deletions against 3ae7d73b
sprint: PDR-prep
author_agent: "author:WP-PDR-13 (Claude, software lead as 07 author; CR-013 originator)"
reviewer_agent: "reviewer:software-plan (new invocation for WP-PDR-13; authored no part of WP-PDR-13, CR-013 or CR-010)"
criticality: safety-critical
# assurance_required: true. 07 is the 07 section 2.1.1 "Software plans" Yes product and tools/validate_docs.py
# ASSURANCE_WHOLE_PRODUCTS names it. The assurance reviewer is a separate invocation (rule C4). At iteration 1 it was
# not yet assigned. Re-pin: the paired record INSP-073 (docs/reviews/PDR/checklists/software-plan-07-software-assurance.md,
# filed at 9403999, the PDR delta of INSP-018) is copied here as filed: paired_record, assurance_reviewer_agent and
# assurance_verdict (07 section 10.2 Record row; 01 section 13 paired_record)
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-13-software-plan (paired record INSP-073, software-plan-07-software-assurance.md)"
paired_record: INSP-073
iteration: 1
# readiness_met: true at the re-pin (was false). R1 failed at 41c588c (validate_docs 43 passed, 7 failed, all record drift
# that CR-013 states) and was to become true after the SRR record deltas. Those are on the branch (CR-013 step 4b, head
# 1a486e4), where validate_docs gives 50 passed of 50; R2 to R5 unchanged (Yes)
readiness_met: true
# reviewer_verdict: APPROVED. Every INSP-010 lien in scope is Verified or, for finding-15, correctly recorded as open;
# no Major; three new Minor findings are liens due the CDR readiness declaration (plan rule C1)
reviewer_verdict: APPROVED
# assurance_verdict: as the paired record INSP-073 states it (iteration 1, 9403999: assurance_verdict APPROVED, 0 Major,
# 1 Minor lien). At iteration 1 it was NEEDS CHANGES because the pair was not filed
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES (a) until the paired assurance record is APPROVED (07 section 10.2) and (b) while the
# reviewed blob is on the CR branch only; set APPROVED at or right after the CR-013 merge with blob 0ad37a43 unchanged.
# Re-pin: hold (a) is met (INSP-073 assurance_verdict APPROVED); hold (b) remains
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 3
# re-pin: counts reconciled with the finding tables. The Lien table is the last row of each finding, and it reads
# "Lien" (plan rule C1), so the three Minor findings are counted as deferred, not open (was open 3, deferred 0)
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 3
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [R1, CK-REQ-G2, CK-REQ-G7]
# effort: iteration 1 22 turns, 35 minutes; the re-pin delta adds 6 turns, 12 minutes
effort_turns: 28
effort_minutes: 47
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-059: software engineering plan 07, PDR delta of INSP-010 (CR-013, WP-PDR-13)

**Product.** `docs/process/07-software-engineering-plan.md` blob `0ad37a43` (revision A.9, draft) on branch `cr/CR-013-process-04-07-semp-srr-liens` at `41c588c`, parent `5cd87cf` (CR-010 change set, 07 blob `3ae7d73b`, revision A.8); baseline blob `bfe05f43` (`baseline/srr`, `main`). Identity checked with `git ls-tree 41c588c` and `git rev-parse`. The CR-013 change was read as `git diff --word-diff 5cd87cf 41c588c -- docs/process/07-software-engineering-plan.md`; every hunk was checked against the INSP-010 finding it cites and against the tree. Change record: CR-013 blob `560fe69a` on `main` (`8470350`), section 1.2 items 1 to 14.

**Checklist and acceptance criteria (rule C7).** `docs/templates/peer-review-checklist-requirements.md` revision C, section G (all items) and A8. Cases, each checked: INSP-010 finding-14, 16, 17, 18, 20 and 22 at their locations; the finding-15 open row against `tools/measurements.py` `check_records`; the section 8.3 schedule against 05 section 13, row by row; the section 17.1 licence facts against `git -C /Users/robinonsay/rust/rustos show 2ec64c0:LICENSE` and both manifests; that no other line changed. INSP-018 finding-8, 9 and 11 are the software assurance findings. The paired assurance record verifies them; the file-level facts found here are noted below for that reviewer, and this record does not rule on them.

**Independence (rule C4).** This invocation authored no part of WP-PDR-13, CR-013, CR-010 or either branch commit, and edits no product file. **Search first.** `mcp__claude-context__search_code` ran on `/Users/robinonsay/rust/cwht` before any manual search that pinned lines (queries: the WP-PDR-13 reviewer and record path; NPR 7123.1D SE-40). The one prior `grep -n '^#'` over the plan file is the deviation recorded in INSP-058. The rustos repository was read only with `git show` of committed objects; its working tree was not read. **LTspice** was not run.

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 | No (disclosed by the CR, no finding) | At `41c588c` (detached scratch worktree, removed): 43 passed, 7 failed, the record drift of INSP-005, 006, 009, 010, 017, 018 and 021, as CR-013 section 4 and step 2 state (INSP-058 R1) |
| R2 | `tools/traceability.py` reports no violation | Yes | 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148) at `41c588c` |
| R3 | Author self-check and acceptance criteria | Yes | CR-013 section 5 "Verification of the implementation" and section 1.2 before-and-after table |
| R4 | No `TBD`; TBRs complete | Yes | Added lines: 0 `TBD`, "as appropriate", "should consider"; 0 em dashes in blob `0ad37a43` |
| R5 | CR impact assessment attached | Yes | CR-013 section 4; reviewed in CR-013 section 6.1 |

## Verification of the INSP-010 liens (delta)

| INSP-010 finding | Location in blob `0ad37a43` | Check | Result |
|---|---|---|---|
| finding-14 | Section 8.1 paragraph after the table | Lock rows are now cited by tool name ("section 1 lists `cargo-llvm-cov`, ... each in the row named after the tool"), with the rule "cites lock rows by tool name, never by position". Lock section 1 has the rows `nightly-2026-08-24 (date-pinned)` (line 21, components include `miri`) and `rust-code-analysis-cli` (line 32, 0.0.25, installed 2026-09-26 under SRR decision 109), as the paragraph says. The positional reference is gone. The table above the paragraph was not updated: finding-1 | Verified (with finding-1) |
| finding-15 | Section 22 row "Evidence preservation of the SRR roll-up" | Not claimed fixed, and correctly so. `tools/measurements.py` at `7bb994f`, `check_records` (line 305): the evidence loop runs over every record with `state == "Measured"` (loop at line 354) and has no test for supersession. `current_records` (line 390) is used only for the tally, so a superseding record does not clear the failure of the record it supersedes, as the row says. The row names both options, the owners (tool owner with a TV-013 re-run; WP-PDR-47 for the roll-up) and the due gate. `cr/CR-014-tool-liens-srr` (WP-PDR-09) changes only the result-line wording of `tools/measurements.py`, not this rule. The lien stays open, due the PDR readiness declaration, with CR-013 section 12 Q2 as the owner decision | Lien stands (correctly recorded) |
| finding-16 | Section 11.1 first paragraph and "Evidence preservation" | The schema, fixture and README row are stated as committed at `1d423e5` (`git log --diff-filter=A`: `docs/plan/measurements.schema.json` first at `1d423e5`), and `tools/measurements.py` with `test_measurements.py` at `3de1e2d`, TV-013 (`docs/cm/tool-validation/TV-013-measurements.md` exists, status Validated). The section 22 row "Measurements schema and tool rows" is removed with its evidence in the lead-in | Verified |
| finding-17 | Section 14.2 row i, L1 column | REQ-SYS-181 is listed with 180 and 182 ("180, 181 and 182 adopted by SRR decisions 38, 39 and 40; 181 is HZ-003 K9"). `docs/safety/hazard-analysis.md` section 7 row i on `main` reads "REQ-SYS-055, 071, 083, 092, 119, 120, 180, 181, 182 (180, 181 and 182 adopted at SRR by package decisions 38, 39 and 40)". The "07 addition" clause is gone | Verified |
| finding-18 | Section 1.2 paragraph after the table; section 9.5 item 3 | Both passages now name the CS-11 failure arms of `cwht-app::main`: the board `take()` `None` arm and the `Err` arm of each rustos driver constructor that returns `Result` (CR-001, SRR decision 108; CR-001 status Dispositioned, rationale "SRR decision 108 ... admit rustos driver-construction `Err` arms that call `safe_state_halt()`"). Section 9.5 item 3 lists each arm in the MC/DC table as `target-only: Inspection`, with CR-001 section 5 as the inspection rule, which is the fix the finding asked for | Verified |
| finding-20 | Section 10.2 row "Readiness criteria" | Cites memo section 8.2 "Decision 115 (b): readiness waiver for the FW-B0 record" (memo line 352) and W1 by amendment A-1 with the anchor `decision-memo.md#W1` (memo line 425, `<a id="W1"></a>`). Waiver scope unchanged | Verified |
| finding-22 | Section 8.4 row G5; Annex C gate outline | Both read `miri test -p api --lib`, with the item B and FW-B1 citation. No `-p pico2` Miri command remains (`git show 41c588c:<07> \| grep -n 'pico2 --lib'`: none; the Annex comment says "-p pico2 returns at FW-B1") | Verified |
| Section 8.3 against 05 section 13 | Accreditation schedule sentence | Row by row against 05 section 13 on `main`. PDR row, software tools: `rustc`, `cargo`, `clippy`, `cargo-llvm-cov` with llvm-tools, `cargo-nextest`, `nightly-2026-08-24`, `tools/measurements.py`, the emulator: all in 07. CDR row: `tools/sw_gate.sh`, `picotool`, `cargo-binutils`, `cargo-audit`, `cargo-deny`, `cargo-geiger`, `rust-code-analysis-cli` with `tools/complexity_gate.py`, `tools/unsafe_audit.py`: all in 07. The first-use rule equals 05 section 13 lead. TV-023 (`TV-023-nightly-miri.md`) exists and covers Miri. The 05 hardware and CM tools (`tools/render_tpm.py`, `tools/csa.py`, `tools/check_commit_msg.py`, `kicad-cli`, LTspice, OpenSCAD) are outside the 07 scope, which is correct | Correct |
| Section 17.1 rustos rows | Pin and licence cells | `git -C /Users/robinonsay/rust/rustos show 2ec64c0:LICENSE`: "MIT License", "Copyright (c) 2026 Robin Onsay". `api/Cargo.toml` and `firmware/pico2/Cargo.toml` at `2ec64c0`: `license = "MIT"`, `publish = false`. At `c54d35a`: no `LICENSE`, no `license` field. Commit subject "MIT licence, publish = false, and SAFETY comments on every unsafe site". Lock section 3 pins `2ec64c0f15...` (CR-004). All as stated | Correct |
| Section 22 table and lead-in | Six rows removed; rows re-dated | Evidence of each closed row checked: 01 section 13 defines `paired_record`; INSP-010 carries `paired_record: INSP-018`; `rmm.json` rows SWE-089, SWE-090 and SWE-094 name `docs/plan/measurements.json` and read In place; 04 section 12 carries the target-only entry (INSP-058); lock rows of the 2026-09-26 installs; charter section 5 at `6ea6b1d` has the artifact rows and "Status notes between reviews". The INSP-009 half of the paired-record row: finding-2. Re-dated rows: 03 section 4.3 scheduler row places the dispatcher in `cwht-core` and the main loop in `cwht-app` at `5cd87cf`; 03 section 6.5 X13 still Open; `ASSURANCE_WHOLE_PRODUCTS` on `main` names neither 05 nor TS-002; none of RSK-003, 010, 013, 019, 020, 021, 023, 063 carries a tag. All as stated | Correct (with finding-2) |
| No other line changed | Whole file | `git diff --stat 5cd87cf 41c588c`: 3 files; the 07 hunks are the 14 items of CR-013 section 1.2 | Correct |

**Facts for the software assurance pair (not rulings).** INSP-018 finding-8: the "Paired assurance record fields" row is removed; see finding-2 for the INSP-009 half. INSP-018 finding-9: the same fix as INSP-010 finding-17, verified above. INSP-018 finding-11: the G5 and Annex C commands read `-p api`, and the section 8.1 Miri row adds that the `pico2` decision functions join when `pico2` becomes host-compilable (FW-B1, `cfg_attr`, PCR-10). The same row's status cell is stale (finding-1).

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Terms match the tree (CS-11, CS-38, W1, `target-only: Inspection`); 0 em dashes |

CK-REQ-A1 to A7 and sections B to F: N/A (product type "Plans and process documents").

## G. Plans, process documents and decision records

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | Yes | The changed text agrees with charter section 10 (MC/DC method, safety-critical list unchanged by this CR), CR-001, the SRR memo section 8.2, 05 section 13 and `hazard-analysis.md` section 7 row i; no RMM or compliance row is contradicted |
| CK-REQ-G2 | No | The section 22 lead-in still says its rows are "Log-controlled edits" carried "in the SRR package" (finding-3) |
| CK-REQ-G3 | Yes | Roles and owners of each re-dated row are named (WP-PDR-09, 16, 17, 18, 47; the owner for OD-31) |
| CK-REQ-G4 | Yes | No tailoring changed; SWE-219 relief unchanged |
| CK-REQ-G5 | N/A | Section 16 not touched by CR-013 |
| CK-REQ-G6 | Yes | Section 11.1 states the committed schema, fixture and tool, with the evidence-preservation gap recorded as an open section 22 row (finding-15) |
| CK-REQ-G7 | No | Section 8.1 table status cells contradict the revised paragraph (finding-1); the section 22 closure of the paired-record row overstates the INSP-009 half (finding-2) |
| CK-REQ-G8 | Yes | SWE and SE ids in the changed text exist in the corpus; the memo and CR citations resolve |

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-REQ-G7 | 07 section 8.1 table: Miri row, column "Status verified" (line 317); "Coverage (branch, condition)" row, same column | The paragraph after the table now says `miri` and `llvm-tools` were installed on `nightly-2026-08-24` on 2026-09-26 (SRR decision 109). The table still says, for Miri, "Not installed ... To be installed in FW-B0 per CS-03", and for the nightly, "present without `llvm-tools` ...; `llvm-tools` to be installed in FW-B0". CR-013 edited the Miri row's Notes cell in the same commit, and the `rust-code-analysis-cli` row of the same table already reads "Installed 2026-09-26". A reader of the table (the SWE-135 tool status, gate G5) gets the opposite of the paragraph. This is the rest of INSP-010 finding-14 ("state what remains") at a second place. Fix: set both status cells to the lock state (installed 2026-09-26, lock row `nightly-2026-08-24 (date-pinned)`), or mark the table as the 2026-09-25 observation and point to the paragraph | Open (Lien: fix before the CDR readiness declaration, plan rule C1) | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G7, CK-REQ-G1 | 07 section 22 lead-in, closed row "Paired assurance record fields" ("INSP-010 names INSP-018 and INSP-009 names INSP-017") | 07 section 10.2 Record row requires both records of a pair to carry `paired_record`, and names INSP-009 with INSP-017 as the SRR practice. On `main`, INSP-010 has `paired_record: INSP-018`. INSP-009 (`docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm.md`) and INSP-017 carry no `paired_record` field; INSP-009 names INSP-017 only in `assurance_reviewer_agent`. INSP-018 finding-8 asked to keep what remains open ("INSP-009 naming INSP-017 ..., if still open"). Removing the row drops that remainder. Fix: keep a row for the INSP-009 and INSP-017 `paired_record` fields (owners: their reviewers, at their PDR deltas under CR-010), or state in the lead-in why the `assurance_reviewer_agent` naming suffices | Open (Lien: fix before the CDR readiness declaration) | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G2 | 07 section 22 lead-in, first paragraph | The lead-in still reads "Open items found by a diff of this plan against the charter at `4e3f891` ... Before SRR these are Log-controlled edits (05 section 4.2 preamble); they are carried in the SRR package". After SRR, 07 is CR-class (05 Table 4-1 row 2), which is why CR-013 exists. Every remaining row is now dated PDR or later, and the charter moved to `6ea6b1d`. The change route and the carrier stated for the open items are wrong. Fix: state that each remaining row is changed by a CR against 07 (or by its own document's route), carried in the PDR package lien list, and re-align the diff sentence to the current charter commit | Open (Lien: fix before the CDR readiness declaration) | Pending | |

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien (plan rule C1) | 07 author (Claude, software lead) | CDR readiness declaration (or at the CR-013 rebase, step 5) |
| finding-2 | Minor | Lien | 07 author; INSP-009 and INSP-017 reviewers for the fields | CDR readiness declaration |
| finding-3 | Minor | Lien | 07 author | CDR readiness declaration |

INSP-010 liens after this delta: finding-14, 16, 17, 18, 20 and 22 Verified on blob `0ad37a43`. finding-15 stays a lien due the PDR readiness declaration (owner decision CR-013 Q2, then a tool change or plan rule, then the WP-PDR-47 roll-up). The SRR record still names blob `bfe05f43`; its update at the merge is CR-013 section 6.1 IR-F1.

## Observations (not findings)

- **O-1 (merge-time staleness).** The re-checked section 22 rows "Assurance routing of 05 and TS-002" ("the constant names neither") and "Tool constants" (`SW-SYNTH`) are true on `main`. Branch `cr/CR-014-tool-liens-srr` (WP-PDR-09, commit `16cdd3e`) adds 05, TS-002 and `SW-SYNTH` to the tool constants, so the rows go stale when that branch merges. CR-013 section 6.1 IR-F2 covers the re-statement at the rebase.
- **O-2.** The section 17.1 licence cell uses "licence" and "license" in one cell (the manifest field is `license`). Consistent with the rest of 07; no change asked.

## Completion

Readiness R1 No (the CR discloses it; it clears at step 5), R2 to R5 Yes. Section G and A8 answered. No Major finding. Three new Minor findings are liens due the CDR readiness declaration. `reviewer_verdict: APPROVED`. `assurance_verdict` NEEDS CHANGES until the paired record `docs/reviews/PDR/checklists/software-plan-07-software-assurance.md` (PDR delta of INSP-018, separate invocation) is filed and APPROVED. When that record exists, this record takes `paired_record` and `assurance_reviewer_agent` from it; its own reviewer makes that update. The record `verdict` is held at NEEDS CHANGES until both reviews are APPROVED and blob `0ad37a43` reaches `main` unchanged at the CR-013 merge. The merge follows CR-010's.

```
VERDICT: APPROVED (reviewer_verdict); record verdict held NEEDS CHANGES (SA pair not filed; blob on the CR branch only)
FINDINGS:
- [Minor] finding-1 CK-REQ-G7 07 s8.1 table: Miri and branch-coverage status cells still "to be installed in FW-B0"; paragraph says installed 2026-09-26.
- [Minor] finding-2 CK-REQ-G7/G1 07 s22 lead-in: paired-record row closed although INSP-009 and INSP-017 carry no paired_record.
- [Minor] finding-3 CK-REQ-G2 07 s22 lead-in: still "Log-controlled edits ... carried in the SRR package"; charter 4e3f891.
VERIFIED: INSP-010 finding-14, 16, 17, 18, 20, 22; finding-15 open row correct (lien stands); s8.3 = 05 s13; s17.1 licence facts.
SA PAIR NEEDED: docs/reviews/PDR/checklists/software-plan-07-software-assurance.md (INSP-018 finding-8, 9, 11)
ITEMS N/A: CK-REQ-A1 to A7, sections B to F; CK-REQ-G5
MEASUREMENTS: size=23 sections, 14 change items; items checked=R1 to R5, A8, G1 to G8 plus 11 delta rows; items no=R1, G2, G7; major=0; minor=3; verified liens=6 (INSP-010); turns=22; minutes=35; iteration=1
```

## Re-pin delta (2026-09-29, lead SE ruling (2); reviewer, new invocation)

**Why.** Lead SE ruling (2) of 2026-09-29: every record re-pin drops a CR file from `product_files` when the CR sections it reviewed are unchanged, and otherwise makes a delta. This record is one of the CR-013 records whose verdicts are set in the CR-013 merge commit (lead SE ruling (3)). Its front matter also carried `findings_open: 3`, `readiness_met: false` and an unassigned assurance pair, which no longer matched its own tables, its readiness condition and the filed pair. This delta re-pins and reconciles the record. It re-reviews no product text and changes no finding.

**Independence (rule C4) and search first (rule C3).** A new invocation of this record's reviewer role for WP-PDR-55. It authored no part of WP-PDR-13, CR-013 or CR-010 (any section), the branch commits, INSP-073 or iteration 1 of this record, and edited no product file. It is not a software assurance invocation: it copies INSP-073's verdict as filed and rules on nothing in that record. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`. The rustos repository was not read.

**Product blob.** `docs/process/07-software-engineering-plan.md` is `0ad37a43` at `41c588c`, at the CR-013 head `1a486e4` (`git log 41c588c..1a486e4` on the path is empty) and on a trial `git merge --no-ff` of CR-010 (`7963f78`) then CR-013 (`1a486e4`) into `main` `9fda694` (detached scratch worktree, removed after use). `main` has not changed the path since `ab2af2d`. INSP-037 now names the same blob (its re-pin delta, lead SE ruling (3)).

**CR file.** `product_files` names no CR file. The CR-013 file (read at `560fe69a`, now `fef1f9d9` on `main`) is an `input_files` entry, which the record drift rule does not read, so later CR-013 record-text edits cannot make this record drift. Nothing is dropped.

**Assurance pair.** INSP-073 (`docs/reviews/PDR/checklists/software-plan-07-software-assurance.md`, commit `9403999`) is filed with `paired_record: INSP-059`, `assurance_reviewer_agent` "sa-reviewer:WP-PDR-13-software-plan", `assurance_verdict: APPROVED`, `product_files` equal to this record's (07 `0ad37a43`), 0 Major and 1 Minor finding (a lien due the CDR readiness declaration). This record now carries `paired_record: INSP-073`, that assurance reviewer and `assurance_verdict: APPROVED`, copied as filed. Hold (a) of iteration 1 is met.

**Readiness.** Iteration 1 set R1 to become Yes after the SRR record deltas. They are on the branch (CR-013 section 5 step 4b: INSP-021 and INSP-005 at `8d9efdf`, INSP-010 at `b6cc8f8`, INSP-018 at `1a486e4`, the CR-010 records by the merges `eff05e0` and `3aab75b`). At `1a486e4`: `tools/validate_docs.py` 50 passed of 50 (R1 Yes); `tools/traceability.py --report-only` 245 requirements, 173 test cases, 0 violations, 2 warnings (R2 Yes, unchanged). R3 to R5 are unchanged. `readiness_met` is set true.

**Counts.** The Lien table is the last row of each finding and reads "Lien" (plan rule C1). The three Minor findings are therefore liens, counted in `findings_deferred` (3), and `findings_open` is 0.

**Checks run on this record.** `tools/validate_docs.py` on `main` with this record in the working tree: PASS (drift of the branch-only blob printed as a note). A scratch copy on the trial merge: PASS with no drift note, and PASS again with `verdict: APPROVED` (117 passed of 117). The scratch copy was discarded.

### Findings (re-pin delta; current state of every finding of this record)

| Finding | Severity | State | Note |
|---|---|---|---|
| finding-1 | Minor | Lien: fix before the CDR readiness declaration (plan rule C1) | Unchanged at `0ad37a43` |
| finding-2 | Minor | Lien: fix before the CDR readiness declaration | Unchanged at `0ad37a43`; INSP-073 concurs (INSP-018 finding-8 remainder) |
| finding-3 | Minor | Lien: fix before the CDR readiness declaration | Unchanged at `0ad37a43` |

Open Major: 0. New findings: 0.

### Record verdict

**Reviewer verdict: APPROVED** (liens finding-1 to finding-3). `assurance_verdict` APPROVED, copied from INSP-073. `readiness_met` is true. The record `verdict` stays **NEEDS CHANGES** while blob `0ad37a43` exists only on the CR branch (hold (b)). The software lead sets `verdict: APPROVED` in the CR-013 merge commit (or the commit right after it) when `git rev-parse HEAD:docs/process/07-software-engineering-plan.md` is `0ad37a43`. A changed blob needs a delta of this record and INSP-073 first.

```
RE-PIN DELTA (2026-09-29): reviewer APPROVED (liens finding-1 to finding-3); assurance APPROVED (INSP-073, as filed); record verdict NEEDS CHANGES (held for the CR-013 merge); readiness_met true
PRODUCT: 07 0ad37a43, unchanged (41c588c, 1a486e4, trial merge); no CR file pinned
COUNTS: findings_open 3 -> 0, findings_deferred 0 -> 3 (liens); no new finding; open Major 0
MEASUREMENTS: tool runs=4; turns=6; minutes=12; cumulative turns=28, minutes=47
```
