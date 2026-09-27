---
id: CR-004
title: Move the rustos lock pin from c54d35a to 2ec64c0 and regenerate the unsafe audit list
status: Dispositioned
class: I
originator: Claude
date_opened: 2026-09-26
phase: Pre-A/A
configuration_at_origination: 511c0ca (SRR close-out, owner approval of the SRR with liens; before the baseline/srr tag); rustos master 2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c
baseline_affected: baseline/srr
affected_cis: [26, 27, 46]
affected_paths: [tools/toolchain.lock.md, firmware/unsafe-audit.md]
affected_ids: [TC-SW-TOOL-001, CS-05, CS-06, CS-07, MSR-11, OQ-SW-001]
related: [INSP-016, TV-011, CR-001]
target_release: none
branch: cr/CR-004-rustos-pin-2ec64c0
disposition: Approved
disposition_date: 2026-09-26
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-004: Move the rustos lock pin from c54d35a to 2ec64c0 and regenerate the unsafe audit list

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. Source of the change: SRR close-out item 1 (`docs/reviews/SRR/minutes.md`, section "Close-out decisions (after the first close-out run)", commit `dd39332`), ruled as recommended by the owner on 2026-09-26. The recommendation reads: "Merge the rustos branch `cwht/wp-sw-licence-manifest-safety`, and approve the change request that moves the lock pin to the merged commit (CR-004) and regenerates `firmware/unsafe-audit.md` in the same commit." This file is that CR. The `rustos` CI (CM plan Table 4-1 row 26) needs a CR only after the first `release/FW-*` tag; the owner directed one now so that the pin move has a decision record before the `baseline/srr` tag. Because the owner approved the CR before this file existed, it is committed in the Dispositioned state together with the implementation (section 8), as CR-002 was.

## 1. Description of the change

1. `tools/toolchain.lock.md` section 3, row `rustos`, "Observed" cell, before: `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (`c54d35a`, "Fix build"). After: `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (`2ec64c0`), the rustos `master` commit after the owner's fast-forward merge of `cwht/wp-sw-licence-manifest-safety`. The superseded value is kept in the cell as history. The row's command changes from `rev-parse HEAD` to `rev-parse master`, and the rule cell records that builds, audits and gates for the record read a `git archive` export of the pinned commit, never the owner's rustos working tree (it holds uncommitted work of the owner's own).
2. The rustos changes pulled in (CM plan Table 4-1 row 26: "Moving the pin is a CR listing the `rustos` changes pulled in"). `git -C /Users/robinonsay/rust/rustos log --oneline c54d35a..2ec64c0` lists one commit, `2ec64c0` (":page_facing_up: MIT licence, publish = false, and SAFETY comments on every unsafe site"); `c54d35a` is its parent, so the merge was a fast-forward. `git diff --shortstat c54d35a 2ec64c0`: 7 files changed, 200 insertions, 0 deletions:

   | File | Insertions | Content |
   |---|---|---|
   | `LICENSE` | 21 | MIT licence text (new file) |
   | `api/Cargo.toml` | 2 | `license = "MIT"`, `publish = false` |
   | `firmware/pico2/Cargo.toml` | 2 | `license = "MIT"`, `publish = false` |
   | `api/src/device/mod.rs` | 17 | `// SAFETY:` comments only |
   | `firmware/pico2/src/common/reset.rs` | 32 | `// SAFETY:` comments only |
   | `firmware/pico2/src/gpio/gpio.rs` | 51 | `// SAFETY:` comments only |
   | `firmware/pico2/src/lib.rs` | 75 | `// SAFETY:` comments only |

   In the `.rs` files every added line is a `//` comment, and 36 added lines open a `// SAFETY:` comment (`git diff c54d35a 2ec64c0 | grep -c '^+.*// SAFETY:'` gives 36); with the one comment already present at `c54d35a`, `2ec64c0` holds 37 (`git grep -c 'SAFETY:' 2ec64c0 -- api firmware/pico2`: 3, 6, 9 and 19 per file). This is the SRR decision 110 work item (INSP-016 row for `2ec64c0` in `docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`).
3. `firmware/unsafe-audit.md` (Table 4-1 row 46), regenerated with `tools/unsafe_audit.py --write --date 2026-09-26` against the pinned rustos: before, git blob `b232d77a`, 37 rows at the `c54d35a` line numbers, 36 of them "(none: CS-06 violation)"; after, git blob `18ef484b`, the same 37 sites (block 16, fn 11, impl 1, extern 3, attribute 6, same items) at the `2ec64c0` line numbers, each with its SAFETY text, 0 without SAFETY, 37 unsigned, 0 superseded signatures (no row was signed before).
4. `tools/toolchain.lock.md` section 1.2 row `tools/unsafe_audit.py` and section 6 record the regeneration and the pin move.

## 2. Reason

TC-SW-TOOL-001 run 3 (`docs/vv/reports/TC-SW-TOOL-001-r3.md` section 5, blocking items B1 and B2) showed that the repository gate fails `G5 cargo deny (bans, licenses, sources)` and `G5 unsafe audit` at `c54d35a`, because rustos `api` and `pico2` carried no licence and 36 of the 37 unsafe sites had no `// SAFETY:` comment (07 CS-06). Both pass on `2ec64c0`: "They close in the repository gate when the pin moves" (run 3 section 5). Run 4 recommendation 1 (`docs/vv/reports/TC-SW-TOOL-001-r4.md` section 9) names this CR. The owner, as rustos maintainer, merged the branch in the owner's own terminal (`git -C ~/rust/rustos merge --ff-only cwht/wp-sw-licence-manifest-safety`, fast-forward `c54d35a` to `2ec64c0`, seven files, 200 insertions; minutes, close-out section). Workaround while the CR was open: none; the repository gate kept both FAILs.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | G0 and G5 of the FW-B0 gate keep the cargo deny and unsafe-audit FAILs, entrance row 20 (FW-B0 toolchain proof) stays Not met, and the `baseline/srr` tag waits (baseline record section 0.1, P6). |
| Pin the branch commit without the owner's merge | The pin would name a commit that is not on rustos `master`; the merge is the owner's act as rustos maintainer (SI-033; run 3 recommendation 1). |
| Point the gate at the owner's rustos working tree | The working tree holds uncommitted work of the owner's own; evidence built from it is not reproducible from a commit. Every run for the record uses a `git archive` export of the pinned commit, as run 3 used a clean layout. |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: the loadable image bytes do not change (Verification row), so FLASH and RAM use (run 3 step 4, gate G2: FLASH 1608 B, RAM 8200 B, equal to run 2) and every TPM are unchanged. |
| Safety | None changes in behavior. The pulled-in change is comments, a licence file and two manifest fields; no code line of `api` or `pico2` changes, so no component of the 07 §14.1 safety-critical or mission-critical tables changes its behavior. The SAFETY comments document the invariants of the 37 unsafe sites that the safe-state manager, the boot path and the GPIO drivers rely on (CS-06); they are now reviewable, and every entry is signed by a code-review `INSP-NNN` before CDR (CS-07). Hazard analysis re-issue: no. RF exposure evaluation change: no. |
| Risk | None added, closed or re-scored. |
| Software classification and tailoring | None: no classification, `rmm.json` or compliance-matrix row changes. |
| Interfaces | None: the rustos `api` trait signatures and `pico2` public items are unchanged (comment-only diff in the `.rs` files); ICD-CTL-SW and ICD-SW-HOST unchanged; no external-interface change. |
| Operations and ConOps | None: no OPS scenario, operator procedure, operations handbook or maintenance instruction changes. |
| Cybersecurity | None: neither the USB firmware-load path nor the key-input command path changes (07 §16). |
| Verification | TC-SW-TOOL-001 gate evidence changes: in the repository gate, `G5 cargo deny (bans, licenses, sources)` and `G5 unsafe audit` go from FAIL (runs 1, 2 and 4 on `c54d35a`) to PASS, as run 3 showed on `2ec64c0` (`docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-full.txt`, `sw-gate-keep-going.txt`, `unsafe-audit.txt`). G0 (toolchain and pin identity) records the new rustos commit. Images: run 3 built both images against `2ec64c0`; `cwht-app.uf2` (`4e0bd133...3529`) and `rustos-blinky.uf2` (`c45b5268...08d3`) are byte-identical to runs 1 and 2, and all loadable ELF sections are identical (only line numbers in the debug information moved; run 3 section 5). The OA-1 and OA-2 owner steps performed on those images (run 4) therefore stand for `2ec64c0`. Re-test scope: TC-SW-TOOL-001 run 5 (gate part, steps 1 to 10 and 13) on the new pin, run 4 recommendation 4. No TC invalidated, added or modified. No decision table or independence-pair test changes. |
| Cost | None. |
| Schedule | On the critical path of the `baseline/srr` tag: closes run 3 blocking items B1 and B2 in the repository and lets run 5 show gate exit 0 (with the complexity CR of close-out item 4). |
| Requirements and traceability | None: no requirement added, modified or retired; no volatility contribution. |
| Regulatory | None: no 47 CFR clause affected. |
| Documentation | `tools/toolchain.lock.md` §3, §1.2, §6 and `firmware/unsafe-audit.md` (this CR's commit). Cross items for their owners: 07 §17.1 third-party register rows rustos `api` and `pico2` (commit `c54d35a` and "No `LICENSE` file" become `2ec64c0` and MIT), 07 open question `OQ-SW-001` (rustos licence) closes, `firmware/THIRD-PARTY-NOTICES.md` records the rustos MIT licence (07 §17.1); `tools/README.md` `unsafe_audit.py` state line; `docs/reviews/SRR/baseline-record.md` row 26 and P6; `docs/cm/deviations.md` entry for a Class I CR Dispositioned before Assessed (section 6); TC-SW-TOOL-001 run 5 report. No VDD exists yet. |
| Released units | None: no unit is built or delivered. |

Classification rationale: Class I proposed. The change moves the commit of source compiled into every image and changes verification evidence of TC-SW-TOOL-001 (the G5 cargo deny and unsafe-audit results), and the CM plan §2 Class II definition excludes any change with impact on verification evidence. The loadable image bytes are unchanged, so no re-flash would follow. The owner's ruling on close-out item 1 approved the CR as recommended without naming a class, so the class is confirmed at the next owner exchange (section 7).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Owner merges `cwht/wp-sw-licence-manifest-safety` into rustos `master` (fast-forward to `2ec64c0`) | Robin (rustos maintainer) | rustos `2ec64c0` (merged 2026-09-26, minutes) |
| 2 | `tools/toolchain.lock.md` §3 pin, §1.2 `tools/unsafe_audit.py` row, §6 row (section 1 items 1 and 4) | Claude (configuration manager and tool owner) | the commit that adds this file (section 8) |
| 3 | `firmware/unsafe-audit.md` regenerated against a clean export of rustos `2ec64c0` (section 1 item 3) | Claude (tool owner) | the commit that adds this file (section 8) |
| 4 | TC-SW-TOOL-001 run 5 on the new pin (gate part) | Claude (test conductor) | |
| 5 | The documentation cross items of section 4 | their owners | |

Regeneration procedure (step 3), in the session scratchpad: `mkdir -p <dir>/cwht <dir>/rustos`; `git -C /Users/robinonsay/rust/rustos archive 2ec64c0 | tar -x -C <dir>/rustos`; `git -C /Users/robinonsay/rust/cwht archive HEAD | tar -x -C <dir>/cwht` (HEAD `b087a9f`, whose `tools/unsafe_audit.py` is the TV-011 blob `cc3aaa2a`); `.venv` linked; then in `<dir>/cwht`: `tools/unsafe_audit.py --check` (before: FAIL, 74 failures, all "lacks the site" and "lists ... which the scan does not find" pairs from the moved line numbers; `without SAFETY 0`), `tools/unsafe_audit.py --write --date 2026-09-26` ("wrote cwht/firmware/unsafe-audit.md (37 sites, 0 superseded signatures)"), `tools/unsafe_audit.py --check --gate SRR` ("MSR-11 unsafe sites: block 16, fn 11, impl 1, extern 3, attr 6; total 37; without SAFETY 0; unsigned 37; in forbidden crates 0", "PASS (0 failure(s))", exit 0); the generated file copied to `firmware/unsafe-audit.md`. The owner's rustos working tree was neither read nor written.

Verification of the implementation: the independent reviewer checks that the §3 pin equals `git -C /Users/robinonsay/rust/rustos rev-parse master`, that `firmware/unsafe-audit.md` equals a fresh `--write` in a clean layout of the pinned commit (0 sites without SAFETY), and that run 5 shows `PASS G5 cargo deny (bans, licenses, sources)` and `PASS G5 unsafe audit` in the repository gate.

## 6. Independent review of the impact assessment

Required (Class I). Not yet performed: the owner ruled close-out item 1 before this file existed, the same departure from 05 §5.2 (Dispositioned before Assessed) as CR-002, for which `docs/cm/deviations.md` holds entry 1; a matching entry for CR-004 is a cross item to the deviations log owner. The independent reviewer of the FW-B0 record INSP-016 (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`) is proposed to review this section with the run 5 delta and record the result here.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Impact assessment | pending (INSP-016 reviewer, proposed) | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | Pending: Class I proposed by Claude; the ruling did not name a class |
| Date | 2026-09-26 |
| Conditions | None |
| Rationale | SRR close-out item 1 (owner ruling 2026-09-26): merge the rustos branch `cwht/wp-sw-licence-manifest-safety`, and approve the change request that moves the lock pin to the merged commit (CR-004) and regenerates `firmware/unsafe-audit.md` in the same commit. Recorded in the minutes: "CR-004 (the lock pin moved from `c54d35a` to `2ec64c0`) is approved under item 1." |
| Waiver scope (if Approved (waiver)) | not applicable |
| Re-look trigger and re-look-by review (if Deferred) | not applicable |
| Source | Chat transcription by Claude on 2026-09-26: owner statement "I concur with your recommendations" on the twelve close-out items, `docs/reviews/SRR/minutes.md` section "Close-out decisions (after the first close-out run)" (commit `dd39332`), after the presenter confirmed rustos `master` at `2ec64c0` and asked for the CR-004 approval |

Disposition history:

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-26 | Approved (SRR close-out item 1) | none | owner ruling at the SRR close-out, transcribed by Claude |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-004` present) |
|---|---|---|
| the commit that adds this file | `tools/toolchain.lock.md` (§3 pin, §1.2 `tools/unsafe_audit.py` row, §6 row; step 2), `firmware/unsafe-audit.md` (git blob `18ef484b`; step 3) | yes |

Traceability report after implementation: not affected (no requirement, test case or hazard changes); renders regenerated: none.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Lock pin | Step 2 | `tools/toolchain.lock.md` §3 equals `git -C /Users/robinonsay/rust/rustos rev-parse master` (`2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`, observed 2026-09-26 21:11 CDT) | pending independent check |
| Unsafe audit list | Step 3 | `firmware/unsafe-audit.md` blob `18ef484b`; `--check --gate SRR` in the clean layout: 37 sites, 0 without SAFETY, exit 0 (section 5 procedure) | pending independent check |
| Gate G0 and G5 | Step 4 | TC-SW-TOOL-001 run 5 | pending |

Independent verifier (agent invocation): pending.

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
| 2026-09-26 | Dispositioned | Claude (configuration manager and tool owner), transcribing the owner | this file's first commit | Written after the owner approved it as SRR close-out item 1 (the close-out item served as the request) and merged rustos to `2ec64c0`; steps 2 and 3 applied in the same commit |
