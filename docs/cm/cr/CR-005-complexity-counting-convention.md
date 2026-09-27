---
id: CR-005
title: Fix the CS-17 and CS-38 complexity counting convention and the CS-19 halt-loop allowance
status: Dispositioned
class: I
originator: Claude
date_opened: 2026-09-26
phase: Pre-A/A
configuration_at_origination: eb52766 (SRR close-out, owner approval of the SRR with liens; before the baseline/srr tag); rust-code-analysis-cli 0.0.25; rustos master 2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c
baseline_affected: baseline/srr
affected_cis: [2, 28]
affected_paths: [docs/process/07-software-engineering-plan.md, tools/complexity_gate.py, tools/tests/test_complexity_gate.py, tools/tests/fixtures/complexity_gate/, docs/cm/tool-validation/TV-012-complexity-gate.md]
affected_ids: [CS-17, CS-19, CS-38, MSR-17, TC-SW-TOOL-001, TV-012]
related: [CR-001, INSP-010, INSP-015, INSP-016, INSP-018, RSK-019, RFA-SRR-008]
target_release: none
branch: cr/CR-005-complexity-counting-convention
disposition: Approved
disposition_date: 2026-09-26
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-005: Fix the CS-17 and CS-38 complexity counting convention and the CS-19 halt-loop allowance

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. Source of the change: SRR close-out item 4 (`docs/reviews/SRR/minutes.md`, section "Close-out decisions (after the first close-out run)", commit `dd39332`), ruled as recommended by the owner on 2026-09-26. The item ends "This is applied by a change request."; this file is that CR. Because the owner approved the change before this file existed, it is committed in the Dispositioned state together with the implementation (section 8), as CR-002 and CR-004 were.

## 1. Description of the change

1. **Measure (07 CS-17).** Before: "Measured with `rust-code-analysis-cli` (section 8)", with no counting convention stated; `tools/complexity_gate.py` took the analyzer's own value as the CC and TV-012 compared it with values computed by hand under a convention the analyzer does not follow (TV-012 limitation 1). After: the CS-17 and CS-38 measure is the cyclomatic complexity that `rust-code-analysis-cli` 0.0.25 reports for the function, in which every `match` arm counts (`_` included) and a bare `loop` counts as a decision, plus one for each `let ... else` in the function, which the analyzer does not count and `tools/complexity_gate.py` adds. No function is then under-counted against the textbook count: the analyzer counts a `match` of n arms as n where the textbook counts n - 1, counts the bare `loop` the textbook leaves at no decision, and the tool restores the one decision the analyzer misses.
2. **Halt-loop allowance (07 CS-38).** Before: the CR-001 per-file allowance counts only the CS-11 board `take()` and driver-construction failure arms, so the bare `loop` of a CS-19 halt loop fails CS-38 once the analyzer counts it (TC-SW-TOOL-001 run 3: `safe_state_halt` CC 2). After: the two CS-19 halt loops, in the panic handler and in `safe_state_halt`, each add one to the CS-38 allowance by the CR-001 per-file allowance mechanism.
3. **Limit.** Unchanged: CS-17 limit 15, yellow 12.
4. **Tool (`tools/complexity_gate.py`).** Adds one to the analyzer's own CC for each `let ... else` statement credited to the function (a statement-initial `let` whose statement reaches an `else` at bracket depth 0 before its `;`, in the comment- and literal-masked source); applies the CR-001 per-file allowance in files tagged `// @target-only`, crediting each item to the function whose body holds it: one for each CS-11 failure arm (a `let Some(..) = ..::take() else { safe_state_halt() }` board take or a `let Ok(..) = .. else { safe_state_halt() }` driver construction, CR-001 section 1 item 1) and one for the bare `loop` of the `#[panic_handler]` function and of `safe_state_halt` (item 2). The file's allowance is the sum of those items and is printed; each function is checked against its own share, so one function's allowance never covers another function's decision. This also completes CR-001 implementation step 3 (the per-file allowance for the admitted arms; INSP-018 cross item).
5. **Plan text (07).** CS-17 and CS-38 rows as in items 1 and 2; the CS-38 enforcement cell, the section 8.1 complexity row, the section 8.2 complexity row, the section 8.3 sanity check and the section 8.4 G5 pass criterion aligned; revision A.6.
6. **Tool validation (TV-012).** The fixture analyzer output `rca.json` is re-derived from real analyzer output on the fixture sources, the known answers follow item 1, and the end-to-end check of TV-012 limitation 1 is re-run.

## 2. Reason

TV-012 end-to-end check of 2026-09-26 19:44 (section 4; `tools/toolchain.lock.md` §1.4 finding 9): `rust-code-analysis-cli` 0.0.25 counts every `match` arm, counts a bare `loop` and does not count `let ... else`, so 4 of 13 fixture functions differed from the hand-computed values and the CS-19 halt loop `safe_state_halt` failed CS-38 in TC-SW-TOOL-001 run 3 (`docs/vv/reports/TC-SW-TOOL-001-r3/complexity-diagnostic.txt`). Gate G5 cannot pass and the analyzer's output cannot be cited for the record until the convention is fixed (TV-012 limitation 1; baseline record section 0.1 precondition P6). Workaround while the CR is open: none; G5 fails.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | G5 stays failing on `safe_state_halt` and TV-012 limitation 1 stays open; the analyzer output is not citable for SWE-220. |
| Have `tools/complexity_gate.py` normalize the analyzer's counts to the textbook convention (subtract one per `match`, drop bare loops) | Rejected at the close-out (item 4 recommendation): the tool would re-parse Rust control flow, which is the job the analyzer is pinned for, and a normalizing error would under-count; the accepted convention can only over-count. |
| A project script over `syn` (RSK-019 fallback) | Deferred: the analyzer parses the cwht and rustos sources without error; the fallback stays the RSK-019 trigger response. |
| Waive the halt loops under 07 section 14.3 | Rejected: a waiver is for an exceedance; a halt loop is required by CS-19, so the allowance belongs in the rule. |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM or budget changes. MSR-17 (mirrored to TPM-017) values change by the convention: on the firmware and rustos `2ec64c0` the mean CC moves from 1.38 to 1.46 (four `let ... else`), the max stays 5 (section 9). |
| Safety | None: no code or behavior changes. The halt-loop allowance admits only the bare `loop` of the two CS-19 halt functions, which CS-19 already requires; no hazard control or 07 §14.1 module changes. Hazard analysis re-issue: no. RF exposure evaluation change: no. |
| Risk | RSK-019 (complexity tool mis-measures Rust 2024 code): mitigation step S1 is served by TV-012 run 2 on real analyzer output; the likelihood is re-assessed by the risk owner at the next register pass, not here. |
| Software classification and tailoring | None. |
| Interfaces | None. |
| Operations and ConOps | None. |
| Cybersecurity | None: neither the USB load path nor the key-input path changes. |
| Verification | No test case changes. TC-SW-TOOL-001 gate G5 complexity result changes (section 9). TV-012 re-validated (run 2). |
| Cost | None. |
| Schedule | Needed before the `baseline/srr` tag (precondition P6). |
| Requirements and traceability | None. |
| Regulatory | None. |
| Documentation | 07 CS-17, CS-38, sections 8.1 to 8.4 rows, revision A.6; `tools/complexity_gate.py` header; TV-012; `tools/README.md` complexity section (tools README owner); `tools/toolchain.lock.md` rust-code-analysis-cli sanity-check row (lock owner). |
| Released units | None. |

Classification rationale: Class II proposed. The change fixes the counting convention of an existing coding-standard measure and adds an allowance for loops the standard already requires; no requirement, ICD, hazard control, test case or released image changes (CM plan §2). Superseded 2026-09-27: the owner confirmed Class I under SRR close-out item C (section 7; section 12).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | 07 CS-17, CS-38, sections 8.1 to 8.4, revision A.6 (section 1 item 5) | Claude (07 author) | `e34a27b` |
| 2 | `tools/complexity_gate.py` let-else addition, CS-38 halt-loop allowance and the CR-001 step 3 per-file allowance (section 1 item 4) | Claude (tool owner) | `e34a27b` (blob `9cdc9195`) |
| 3 | `tools/tests/test_complexity_gate.py` and `tools/tests/fixtures/complexity_gate/` (real analyzer output, known answers per rule) | Claude (tool owner) | `e34a27b` |
| 4 | TV-012 run 2 and end-to-end check on an export of the step 1 to 3 commit; firmware and rustos `2ec64c0` run | Claude (tool owner) | runs on `e34a27b`; recorded in the TV-012 commit (section 8) |
| 5 | Independent review of the TV-012 re-validation (INSP-015 delta); ACC-COMPLEXITY-001 then takes effect per the owner's close-out concurrence | independent reviewer; Claude records | pending |
| 6 | Amendment 1 (section 12): 07 CS-38, section 8.2 complexity threshold, section 11.2 MSR-17 threshold, section 14.3 waiver rule, revision A.7 | Claude (07 author) | `106bc3a` |
| 7 | Amendment 1: `tools/complexity_gate.py` CS-19 main-loop credit for `cwht-app::main`; `tools/tests/test_complexity_gate.py` class `MainLoopTests`; fixture `tools/tests/fixtures/complexity_gate/cwht-app/` and `rca-main-loop.json` (real analyzer output) | Claude (tool owner) | `106bc3a` (blob `ddf10798`) |
| 8 | Amendment 1: TV-012 run 3 (tests, end-to-end check, mutation check against blob `9cdc9195`) and the gate run on the firmware and rustos `2ec64c0` | Claude (tool owner) | runs on `106bc3a`; recorded in the TV-012 run 3 commit (section 8) |
| 9 | Independent review of the impact assessment (section 6, Class I) and of the TV-012 run 3 re-validation (INSP-015 delta) | independent reviewers; Claude records | pending |

Verification of the implementation: the INSP-015 delta reviewer re-runs TV-012 section 3, re-derives the known answers from the fixture sources under the section 1 item 1 convention and checks the gate run of section 9.

## 6. Independent review of the impact assessment

Not required: Class II, no requirement, ICD, hazard or test impact. The implementation is reviewed through TV-012 (INSP-015 delta, step 5).

Superseded 2026-09-27 (SRR close-out item C, minutes `786822a`): CR-005 is Class I, so an independent review of this impact assessment, sections 4 and 12.3 together, is required. The CR was dispositioned before that review; the departure is logged as `docs/cm/deviations.md` entry 3 (RFA-SRR-008). A separate reviewer agent performs the review before the `baseline/srr` tag and records it here. Reviewer invocation, date and result: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | Class I, confirmed by the owner on 2026-09-27 under SRR close-out item C (`docs/reviews/SRR/minutes.md` section "Close-out decisions A to C and repository protection", commit `786822a`, owner statement "I approve the other recommendations"); proposed Class II by Claude on 2026-09-26 |
| Date | 2026-09-26 |
| Conditions | None |
| Rationale | SRR close-out item 4, verbatim: "CS-17 and CS-38 complexity counting convention: the counts of `rust-code-analysis-cli` are the measure; `tools/complexity_gate.py` adds one for each `let ... else`; the two CS-19 halt loops (the panic handler and `safe_state_halt`) get a +1 CS-38 allowance by the CR-001 mechanism; the limit stays 15. This is applied by a change request." Recorded in the minutes: "Under items 4 and 5, the changed tools are re-validated, and their accreditations are extended once the independent review of each validation record is complete." |
| Waiver scope (if Approved (waiver)) | not applicable |
| Re-look trigger and re-look-by review (if Deferred) | not applicable |
| Source | Chat transcription by Claude on 2026-09-26: owner statement "I concur with your recommendations" on the twelve close-out items, `docs/reviews/SRR/minutes.md` section "Close-out decisions (after the first close-out run)" (commit `dd39332`) |

Disposition history:

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-26 | Approved (SRR close-out item 4) | none | owner ruling at the SRR close-out, transcribed by Claude |
| 2026-09-27 | Amended (SRR close-out item A: the +1 CS-38 allowance covers the CS-19 main loop of `cwht-app::main` as well; section 12) and Class I confirmed (item C); Dispositioned-before-Assessed logged as `docs/cm/deviations.md` entry 3; impact review by an independent agent before the `baseline/srr` tag (RFA-SRR-008) | none | owner ruling 786822a, transcribed by Claude (07 author and tool owner) |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-005` present) |
|---|---|---|
| `e34a27b` (the commit that adds this file) | `docs/process/07-software-engineering-plan.md` (step 1), `tools/complexity_gate.py` (step 2), `tools/tests/test_complexity_gate.py` and `tools/tests/fixtures/complexity_gate/` (step 3) | yes |
| the TV-012 run 2 commit | `docs/cm/tool-validation/TV-012-complexity-gate.md` (step 4); this file (sections 5, 8, 9, 11) | yes |
| `106bc3a` (the amendment 1 commit) | this file (front matter class, sections 4, 5, 6, 7, 8, 11 and 12), `docs/process/07-software-engineering-plan.md` (step 6), `tools/complexity_gate.py`, `tools/tests/test_complexity_gate.py` and `tools/tests/fixtures/complexity_gate/` (step 7) | yes |
| the TV-012 run 3 commit | `docs/cm/tool-validation/TV-012-complexity-gate.md` (step 8); this file (sections 5, 8, 9, 11) | yes |

Traceability report after implementation: not affected (no requirement, test case or hazard changes); renders regenerated: none.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Convention and allowance in the tool | Steps 2 and 3 | TV-012 run 2 (section 4): 18 known-answer tests, 0 skipped, pass on an export of `e34a27b`; the analyzer's output on the fixture is byte-identical to `rca.json`; mutation check discriminates each rule | pass (author run); independent check pending (INSP-015 delta) |
| Gate G5 complexity on the firmware and rustos `2ec64c0` | Step 4 | TV-012 section 4, run 2 gate row (export of `e34a27b`, clean export of rustos `2ec64c0`, one `--paths` per root) | CS-17: no failure (52 functions, max CC 5, mean 1.46). CS-38: **one failure**, `cwht-app` `main` CC 4 (analyzer 2, of which 1 is the CS-19 main `loop`, plus 2 `let ... else`) against allowance 3 (1 + 2 CS-11 failure arms). `safe_state_halt` passes on the halt-loop allowance. Open for the owner: the ruling covers the two halt loops, not the CS-19 main loop (TV-012 limitation 8) |
| Amendment 1: convention, allowance and main-loop credit in the tool | Steps 7 and 8 | TV-012 run 3 (section 4): 27 known-answer tests, 0 skipped, pass on an export of `106bc3a`; the analyzer's output on both fixtures is byte-identical to `rca.json` and `rca-main-loop.json`; the mutation check discriminates each rule of the amendment | pass (author run); independent check pending (INSP-015 delta) |
| Amendment 1: gate G5 complexity on the firmware and rustos `2ec64c0` | Step 8 | TV-012 section 4, run 3 gate row (export of `106bc3a`, clean export of rustos `2ec64c0`, one `--paths` per root) | **pass**: CS-17 no failure (52 functions, max CC 5, mean 1.46, none above 12); CS-38 no failure (`cwht-app` `main` CC 4 against allowance 4: 1 + 2 CS-11 failure arms + 1 CS-19 main loop; `safe_state_halt` CC 2 against 2). The open item of the row above is resolved (section 12.4) |

Independent verifier (agent invocation): pending (INSP-015 delta).

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | pending |
| Merge commit | pending |
| Waiver entered in CSA item 12 and affected VDDs | not applicable |
| CSA regenerated | pending |
| Date closed | pending |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-26 | Dispositioned | Claude (07 author and tool owner), transcribing the owner | `e34a27b` | Written after the owner approved it as SRR close-out item 4 (the close-out item served as the request); steps 1 to 3 applied in the same commit |
| 2026-09-26 | Dispositioned | Claude (tool owner) | the TV-012 run 2 commit | Step 4 done: TV-012 run 2 pass; gate G5 CS-38 fails on the `cwht-app::main` main loop, which the ruling does not cover (section 9); owner decision requested |
| 2026-09-27 | Dispositioned | Claude (07 author and tool owner), transcribing the owner | `106bc3a` | Amendment 1 (SRR close-out item A) and Class I (item C) recorded (section 12); steps 6 and 7 applied in the same commit; section 6 impact review pending |
| 2026-09-27 | Dispositioned | Claude (tool owner) | the TV-012 run 3 commit | Step 8 done: TV-012 run 3 pass; gate G5 complexity passes on the firmware and rustos `2ec64c0` (section 9); steps 5 and 9 (independent reviews) pending |

## 12. Amendment 1 (2026-09-27): the CS-19 main loop of `cwht-app::main` (SRR close-out item A) and Class I (item C)

This section amends the CR. Sections 1 to 11 keep their original text except where a note or row dated 2026-09-27 says otherwise.

### 12.1 Source

`docs/reviews/SRR/minutes.md`, section "Close-out decisions A to C and repository protection" (commit `786822a`). The presenter's recommendation, verbatim:

> A. Amend CR-005 so that the +1 CS-38 allowance covers all three unbounded loops that CS-19 names: the main loop in `cwht-app::main` as well as the panic handler and `safe_state_halt`. The presenter's close-out item 4 recommendation had named only the two halt loops.

> C. Confirm CR-004 and CR-005 as Class I. Log the three CRs that were dispositioned before their independent impact review (CR-002, CR-004, CR-005) in `docs/cm/deviations.md`, and perform all three impact reviews before the tag. This closes RFA-SRR-008 early.

Owner statement, verbatim: "Done and added. I approve the other recommendations". Recorded in the minutes: "Items A to C are ruled as recommended."

### 12.2 Change

1. **Allowance (section 1 item 2, amended).** Before: the two CS-19 halt loops (the panic handler and `safe_state_halt`) each add one to the CS-38 allowance. After: all three unbounded loops that 07 CS-19 names add one each: the main loop in `cwht-app::main` as well as the two halt loops. Each item is credited once, to the function that holds it, and is never pooled across functions: a second bare `loop` in `main`, or a bare `loop` in any other target-only function, still fails CS-38.
2. **Tool (section 1 item 4, amended).** `tools/complexity_gate.py` credits one for a bare `loop` in the body of `cwht-app::main`, identified as the top-level function `main` (a direct child of the file space: not a method, not nested in a function or module) of a file that is a binary crate root (a `[[bin]]` `path`, `src/main.rs` by default) of the package whose nearest `Cargo.toml` names it `cwht-app`. A manifest that cannot be read or has no package name gives no credit (fails closed). The FAIL, ALLOWANCE and JSON outputs gain the main-loop count (`cs19_main_loops`).
3. **Plan text (section 1 item 5, amended).** 07 CS-38 names the three loops and the per-function crediting; the CS-38 enforcement cell, the section 8.2 complexity threshold, the section 11.2 MSR-17 threshold and the section 14.3 waiver rule say "above the function's own CS-38 allowance" in place of "above 1"; revision A.7. The section 8.4 G5 pass criterion and CS-19 are unchanged. This closes INSP-010 finding-21 and INSP-018 finding-10.
4. **Tool validation (section 1 item 6, amended).** TV-012 run 3: the known-answer tests gain class `MainLoopTests` on a new fixture package `cwht-app` with real analyzer output; the end-to-end and mutation checks re-run; ACC-COMPLEXITY-001 extended per the owner's concurrence (item A).
5. **Class.** Class I, confirmed by the owner (item C); section 6 now requires the independent impact review, performed before the tag.

### 12.3 Impact assessment of the amendment

| Field | Assessment |
|---|---|
| Performance margins | None. MSR-17 unchanged by the amendment: 52 functions, max CC 5, mean 1.46 on the firmware and rustos `2ec64c0`; only the CS-38 verdict on `main` changes. |
| Safety | None: no code or behavior changes. The allowance admits exactly the one bare `loop` in `cwht-app::main` that 07 section 1.2 and CS-19 already require; any other decision in `main` still fails CS-38. No hazard control or 07 section 14.1 module changes. |
| Verification | TC-SW-TOOL-001 gate G5 complexity: expected to pass (no CS-17 and no CS-38 failure), shown by TV-012 run 3. No test case changes. |
| Documentation | 07 (step 6); TV-012 (step 8); `tools/README.md` complexity section and `tools/toolchain.lock.md` TV-012 row (their owners; cross items). |
| Other fields of section 4 | Unchanged by the amendment. |

### 12.4 Resolution of the open item

Section 9 row "Gate G5 complexity on the firmware and rustos `2ec64c0`" left open for the owner the CS-19 main loop, which the ruling did not cover, and TV-012 limitation 8 recorded the same gap. Both are resolved by this amendment. The run 3 evidence is recorded in section 9 and in TV-012 section 4.
