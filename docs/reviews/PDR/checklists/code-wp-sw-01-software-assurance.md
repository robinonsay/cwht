---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the code review INSP-097
# (docs/reviews/PDR/checklists/code-wp-sw-01.md, iteration 1 by reviewer:WP-PDR-41-code), at the path INSP-097
# names in assurance_reviewer_agent and PDR work plan WP-PDR-41 "Records" names ("code-wp-sw-<nn>.md and
# -software-assurance.md per WP").
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged,
# git merge-base --is-ancestor false on 2026-09-27). The `checklist` field names peer-review-checklist-code
# revision B, the checklist INSP-097 names, because tools/validate_docs.py fails a record whose `checklist` names a
# template absent from main, and the lead SE convention of 2026-09-27 does not change the validator.
# `assurance_checklist` names the template actually applied (the form of INSP-048, INSP-051 and INSP-070).
# id: the brief assigned no id. INSP-100 is the highest id on main, on every cr/ branch and in the working tree
# (2026-09-27). INSP-095 to INSP-099 are the five WP-PDR-41 code reviews in the order WP-SW-11, 09, 01, 02, 03;
# this record takes INSP-103, the third of the five SA pairs in that order, leaving 101, 102, 104 and 105 to the
# other pairs if they follow the same order (the validator's unique-id check catches any collision)
id: INSP-103
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-01-software-assurance.md
product: "rustos cwht/wp-sw-01: api/src/time/mod.rs, firmware/pico2/src/timer/ and docs/icd/rp2350/timer/ (WP-SW-01)"
# product_commit and product_files: iteration 2, equal to INSP-097 iteration 2 (readiness R1; rule C2; SA-A3). The
# sixteen rustos blobs exist only on the unmerged rustos branch cwht/wp-sw-01 (head 58fe739; git rev-parse
# 58fe739:<path> for each, 2026-09-27); the three cwht blobs are equal at cwht HEAD a244b05. Eight blobs drifted from
# iteration 1 (ADR-053, SW-03, sprint index, api time/mod.rs, timer/mod.rs, timer/tests.rs, timer/timer_tests.rs,
# pico2 lib.rs); the other eleven are unchanged
product_commit: "58fe739e964435996001ed61a47423409010a09d"
product_files: ["docs/decisions/adr/ADR-053-wp-sw-01-timer0-time-base-and-alarms.md@71f0b629402dbe8c596825b21e97d4a1905c7b0d", "docs/sprints/SW-03-wp-sw-01-timer0.md@1cea48ef0db4fb9558c1a8d51698395fc7c520b8", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:api/src/time/mod.rs@3c6c567381ecbb37a39bb9bdb16f3e2012cb955a", "rustos:api/tests/time_contract.rs@f9293ee88a267cadc319f7c79664498ae4b0379e", "rustos:api/src/lib.rs@a189e7bdc5c3fdc3249836997691e7c7397f77b5", "rustos:firmware/pico2/src/timer/mod.rs@4004047d3c725929ff3e806377b394bd10f201ee", "rustos:firmware/pico2/src/timer/tests.rs@ed14e12ea380af12f91382589f4f3af8feba3542", "rustos:firmware/pico2/src/timer/timer.rs@e24f1d525e11029df5b43521914ed84dc1bd6322", "rustos:firmware/pico2/src/timer/timer_tests.rs@bbe9427594a88e8547e27daacd5c1fe03218421b", "rustos:firmware/pico2/src/common/board.rs@c69de18ce76e4bfbd6bc9041af8f92a875830659", "rustos:firmware/pico2/src/common/reg.rs@93e97f73e735698b7a12c2e5129a4ee6eda9720c", "rustos:firmware/pico2/src/common/reset.rs@4f26beb0c8b53258f1bc78f112eaf56360af4915", "rustos:firmware/pico2/src/lib.rs@5393076ccf56ebfa2ea17056284f8f7cb341f044", "rustos:docs/icd/rp2350/timer/index.md@11c66ca302a4429a4a9f3d5f93180844d7acf509", "rustos:docs/icd/rp2350/timer/01_overview.md@39bb74ec115f35c8d1671f520fe1413a40fabe8c", "rustos:docs/icd/rp2350/timer/02_programming.md@be5fe7f2bc4a12e59f0a4321b965c29fe82da65f", "rustos:docs/icd/rp2350/timer/03_registers.md@ca7ea335deede210c1b4222a2a23cd1290facb1d", "rustos:docs/icd/rp2350/index.md@41ba1c62d239fc2508cc8bf87388647021607d03"]
# product_files_iteration_1: the blobs iteration 1 reviewed at rustos a1cd160 and cwht 618e441
product_files_iteration_1: ["docs/decisions/adr/ADR-053-wp-sw-01-timer0-time-base-and-alarms.md@471b900f52211b6096259c62c651c19fa6df789e", "docs/sprints/SW-03-wp-sw-01-timer0.md@8fed7b88be09a0294df2c0b00b513e15876a2cbb", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/time/mod.rs@f62b496149a3813b8fd3281523f2c3c001fa97b2", "rustos:api/tests/time_contract.rs@f9293ee88a267cadc319f7c79664498ae4b0379e", "rustos:api/src/lib.rs@a189e7bdc5c3fdc3249836997691e7c7397f77b5", "rustos:firmware/pico2/src/timer/mod.rs@a1ef29c8ffaf56c1b4c23c92d9da944f958480ee", "rustos:firmware/pico2/src/timer/tests.rs@247eeb82a4623ba75bd12a94fbd5efd2e2b78c27", "rustos:firmware/pico2/src/timer/timer.rs@e24f1d525e11029df5b43521914ed84dc1bd6322", "rustos:firmware/pico2/src/timer/timer_tests.rs@e1657cab15530f62d291a7dba99ab0ec18577416", "rustos:firmware/pico2/src/common/board.rs@c69de18ce76e4bfbd6bc9041af8f92a875830659", "rustos:firmware/pico2/src/common/reg.rs@93e97f73e735698b7a12c2e5129a4ee6eda9720c", "rustos:firmware/pico2/src/common/reset.rs@4f26beb0c8b53258f1bc78f112eaf56360af4915", "rustos:firmware/pico2/src/lib.rs@dcd1c254e01474c56ce2f43a97afb26171c25579", "rustos:docs/icd/rp2350/timer/index.md@11c66ca302a4429a4a9f3d5f93180844d7acf509", "rustos:docs/icd/rp2350/timer/01_overview.md@39bb74ec115f35c8d1671f520fe1413a40fabe8c", "rustos:docs/icd/rp2350/timer/02_programming.md@be5fe7f2bc4a12e59f0a4321b965c29fe82da65f", "rustos:docs/icd/rp2350/timer/03_registers.md@ca7ea335deede210c1b4222a2a23cd1290facb1d", "rustos:docs/icd/rp2350/index.md@41ba1c62d239fc2508cc8bf87388647021607d03"]
# inputs read (not reviewed), blobs at cwht HEAD 1353bb3
input_files: ["docs/reviews/PDR/checklists/code-wp-sw-01.md@88654178e2160fd0c661b63cc1e453ea4f4ed7a3 (INSP-097 iteration 2, committed 134e555)", "docs/reviews/PDR/checklists/code-wp-sw-01.md@f3ffb1088e51b5767e8833a814f0c9cfbc62ad19 (INSP-097 iteration 1, committed 9d3734c)", "rustos:firmware/pico2/src/irq/vectors.rs at 58fe739 (WP-SW-09 product of INSP-096, read for the TIMER0 slots the lib.rs hunk moves)", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8 (sections 2.1.1, 7, 9.5, 9.6, 10.2, 14, 15, 19)", "docs/safety/hazards.json@81cacde47d4f2066ecac3947f3acf65e646b1ad0 (HZ-004)", "docs/process/rmm.json@e326ddd1b7296d7d7fe172be6f33535cee3192d7", "docs/process/03-software-classification-and-rmm.md (section 4.3 HZ-004 row)", "docs/plan/pdr-work-plan.md (sections 1, 3.1, 3.8 WP-PDR-41, 5)"]
paired_record: INSP-097
# product_type: code (07 section 2.1.1 row "Code", Yes for a safety-critical component). Task set applied: the
# section B row "Every product type", the row "code", the section 7.1 tasks of the other SWEs the package implements
# (SWE-134 task 6 through ADR-053 section 4.3, SWE-205 task 1 and SWE-052 through the HZ-004 argument, SWE-211 through
# 07 section 9.9) and the section E tasks (SWE-087, SWE-088, SWE-089, SWE-080, SWE-081, SWE-187) (07 section 15)
product_type: code
# criticality: 07 section 14.1 drivers row, "TIMER alarms", pico2 WP-SW-01, criteria "inherited" from the keyer
# (ALARM0 element timing) and the scheduler (ALARM1, the 1 kHz tick), both safety-critical
criticality: safety-critical
product_size: 1429 lines added in a1cd160 (about 590 non-test Rust lines, 231 ICD lines, 342-line contract draft, 25 developer tests); ADR-053 88 lines; SW-03 61 lines; 19 product files
sprint: SW-03-wp-sw-01-timer0
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-01"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-01 (software assurance function; paired file review INSP-097 by reviewer:WP-PDR-41-code)"
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 2 (delta, rule C1). The concurred Major INSP-097
# finding-1 is Verified at 58fe739 (independent re-run, mutation check and hunk read, section "Iteration 2"); no Major
# is open against a SWE-134 item. Findings 1 and 2 of this record were not addressed by revision 2 and become liens
# (rule C1); new Minor finding-3 (the planned dev-board case for the now == at edge cannot reach it) is a lien at
# once. Iteration 1 was NEEDS CHANGES on the concurred finding-1
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2); held at NEEDS CHANGES. Both reviews are APPROVED at
# iteration 2, but under the lead SE convention of 2026-09-27 (INSP-031 practice) the record verdict stays held while
# the sixteen reviewed rustos blobs exist only on the unmerged rustos branch cwht/wp-sw-01; it is set in the pin-move
# CR merge commit (PCR-4), or the commit right after it, when the blobs reach a configuration cwht consumes
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 3
findings_open: 3
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 3
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 3", "swe-135 7.1 task 4", "swe-135 7.1 task 5", "swe-135 7.1 task 6", "swe-135 7.1 task 7", "swe-134 7.1 task 2", "swe-087 7.1 task 4", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-052 7.1 task 2", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 2", "swe-187 7.1 task 1"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
# items_no at iteration 2: SA-C-g, SA-C-j and swe-087 7.1 task 4 are Yes (INSP-097 finding-1 Verified); the rest
# are carried by the Minor liens finding-1 and finding-2; SA-D6 was answered No at iteration 1 and omitted here then
items_no: ["swe-134 7.1 task 2", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "SA-C-i", "SA-C-k", "SA-D1", "SA-D6"]
effort_turns: 65
effort_minutes: 115
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-103: software assurance pair of INSP-097, code review of WP-SW-01 TIMER0 time base and alarms (rustos `api::time` and `pico2::timer`), iterations 1 and 2

**Product.** rustos branch `cwht/wp-sw-01` at `a1cd160` (parent `cwht/wp-sw-09` `9305f59`), the sixteen rustos blobs of `product_files`, with ADR-053, SW-03 and the sprint index at cwht `618e441`. Identity checked on 2026-09-27: `git -C /Users/robinonsay/rust/rustos rev-parse cwht/wp-sw-01` is `a1cd160` (the head has not moved since INSP-097); `git rev-parse a1cd160:<path>` equals every rustos blob; the three cwht blobs are equal at `618e441` and at `HEAD`. The product was read with `git show` and exercised in a detached scratch worktree of the rustos repository made with `git worktree add --detach` at `a1cd160` (removed after the review). The owner's rustos working tree was not read or changed.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Sections R, A, B, C, D, E and F are applied. `product_type` code; `criticality` safety-critical (07 section 14.1 drivers row: "TIMER alarms", `pico2` WP-SW-01, criteria inherited).

**Acceptance criteria (rule C7).** Every task of the section B rows "Every product type" and "code"; the section 7.1 tasks of every other SWE the package implements (front matter list); SWE-134 items a to l (section C) for a driver of the keyer and the scheduler, including the 07 section 14.2 `SW-KEYER` and `SW-SCHED` rows it serves; each INSP-097 finding (finding-1 to finding-5) re-read under the assurance lens; the three decisions `select_time`, `plan_arm` and `after_arm` against their truth tables and MC/DC pairs; the concurrency of `schedule` against the `TIMER0_IRQ_N` handler; the HZ-004 argument of ADR-053 section 4.3.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-PDR-41, ADR-053, SW-03 or INSP-097, edited no product file, and is neither the author (`author:WP-PDR-41 wave 1a`) nor the file reviewer (`reviewer:WP-PDR-41-code`). **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: paired software assurance record form and slug; HZ-004 keyer timer alarm stuck key-down causes; SWEHB SWE-135 section 7.1 tasking). `grep -n` and `awk` were used afterwards only to pin lines and extract the SWEHB section 7.1 lists; files at known paths were read directly.

## Assurance re-runs and checks

| # | Command or check (scratch worktree at `a1cd160`, `RUSTUP_AUTO_INSTALL=0`, `--offline`; no download) | Result |
|---|---|---|
| S1 | `cargo test --offline -p pico2 -p api` | pico2 71 passed (25 in `timer`); api `time_contract` 5 passed, `irq_contract` 4 passed; equal to INSP-097 C1 |
| S2 | `cargo llvm-cov --offline -p pico2 -p api --summary-only` (cargo-llvm-cov 0.9.1, already installed) | `api/src/time/mod.rs` regions 100 %, lines 100 %; `pico2/src/timer/mod.rs` regions 100 %, lines 100 %; `pico2/src/timer/timer.rs` regions 98.05 % (3 of 154 missed), functions 100 %. The text report shows every line of `timer.rs` executed; the three missed regions are the arms of `match N` in `irq()` (lines 88 to 92) that each monomorphized `Rp2350Alarm::<N>` instance does not take, while every arm runs in one instance (count 1 on each of lines 89 to 92). Development-build measurement, not the credited MSR-13 figure (07 section 9.5 item 4) |
| S3 | `cargo clippy --offline -p pico2 -p api --all-targets -- -W clippy::pedantic`, filtered to the package files | `module_inception` at `timer/mod.rs:32`; `cast_possible_truncation` at `timer_tests.rs:16`; equal to INSP-097 C4. Inspection adds the numeric `as u32` at `timer/tests.rs:41`, which clippy does not flag because the operand is masked, and `timer_tests.rs:15`, which it does not flag because of the shift (CS-15 forbids both; see the finding-5 re-read) |
| S4 | `rust-code-analysis-cli --metrics -O json` per file of `timer/` and `api/src/time/mod.rs`, then `tools/complexity_gate.py --max 15` | PASS; 27 functions, max CC 7, mean 1.81, none above 12; one CS-19 name-based cycle report `checked_add -> checked_add` (`Instant::checked_add` calling `u64::checked_add`, a false positive of the name match) |
| S5 | `git diff 9305f59 a1cd160 \| grep -c unsafe` | 0: no new `unsafe` site, no `unsafe` word in the diff (R6 of INSP-097; the `Mmio` accesses are the WP-SW-11 sites) |
| S6 | Concurrency walk of `schedule` (`timer.rs:176-200`) against a `TIMER0_IRQ_N` handler calling `take_fired` | A handler that took the fire between the `ALARMn` write (line 185) and the `INTR` read (line 188) would make `after_arm` see `armed = 0`, `intr = 0` and return `Err(NotArmed)` for an alarm that fired. The ownership design excludes it: `split` yields each `Rp2350Alarm<N>` once, so thread code and the handler can share it only through the `CsCell` of ADR-052 (ADR-053 section 4.2; `timer.rs:16-18`), whose borrow runs inside a critical section, and a call from the handler itself cannot be pre-empted by the same line at the single priority of CS-34. The other alarms' handlers write only their own bits (`ARMED` and `INTR` write-1-to-clear, `INTE` through the set alias), so no read-modify-write crosses alarms. No finding; the `CsCell` rule is a design constraint for WP-PDR-35 and the `SW-SCHED` design |
| S7 | `tools/traceability.py --report-only --output <scratch>/trace-sa01.md` (cwht HEAD) | 245 requirements, 173 cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125, REQ-SYS-148, unrelated to the package); the tracked `docs/vv/traceability-report.md` and `traceability.json` were not rewritten |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | SA-C-k; `swe-134 7.1 task 2` | `api/src/time/mod.rs:17-35`, `:128-136`; `api/tests/time_contract.rs:147-160` | The portable contract states no alarm state after an `Err` other than ALM-6 `TooFar`: `schedule_at` documents a second error, "the implementation detected that the hardware did not arm", with no clause for the state it leaves, and `time_contract.rs` has no check of it. `pico2` leaves the alarm disarmed with no latch (`timer.rs:58-60`, `:195-198`), but the `cwht-hal-mock` alarm and the `cwht-core` keyer and scheduler fault handling are written against the clauses (ADR-053 section 4.3), so a mock may diverge. Fix: widen ALM-6 (or add ALM-7) to "every `Err` from `schedule_at` leaves the alarm not armed with no latched fire", add the contract check with a rig that injects the refused arm, and carry it into the WP-PDR-35 `SW-HAL` behaviours | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | SA-D1; SA-C-i; `swe-205 7.1 task 1`; `swe-134 7.1 task 6` | ADR-053 section 4.3 (line 68) and section 3 option D (line 45) | ADR-053 states "Hazard analysis update required: no" while its option D decision puts the keyer element alarm (ALARM0) and the 1 kHz tick (ALARM1) on one TIMER0 counter, and the tick dispatches the HZ-004 firmware key-down controls K3 (manual-closure timeout) and K4 (no-gap and squeeze watchdog) (`03` section 4.3 HZ-004 row). A TIMER0 fault (counter stopped through `PAUSE` or `DBGPAUSE`, or a silent missed match of INSP-097 finding-1 on ALARM1) ends the element timing and those monitors together: a common-cause fault of the software controls (SWEHB `swe-205` section 7.7.2 item 16, "Can common cause faults affect the software controls?"). The bound holds through controls that do not use the TIMER0 counter: the CPU watchdog K7 (REQ-SYS-131, 2 s, kicked only when every monitor ran; its tick is the separate `TICKS.WATCHDOG` generator of CS-37) and the hardware cutoff K5 (REQ-SYS-055, 7.5 to 13 s). No safety conclusion changes, but the argument is recorded nowhere. Fix: ADR-053 section 4.3 states the common cause and the two bounding controls, and the item goes to WP-PDR-16b (sole writer of `hazards.json`, plan section 5.3) for the HZ-004 fault tree of `hazard-analysis.md` section 8 (07 section 14.2 row i) | Open | Pending | |

**INSP-097 findings re-read under the assurance lens (not raised again; 07 section 10.2).**

- **finding-1 (Major, Open): concurred, same severity.** The lens adds that the silent 71-minute wait is safety-relevant on both alarms: on ALARM0 it holds key-down past the element end (HZ-004); on ALARM1 it stops the tick that dispatches the key-down monitors, so the firmware controls are lost together (this record's finding-2) and only the watchdog and the hardware cutoff act. The safe fix INSP-097 gives (`Missed` when `armed && now >= at`, MC/DC pair `tests.rs:60` changed) keeps the ALM-1 intent under either comparator behaviour. It carries the No answers of `swe-134 7.1 task 2`, `swe-087 7.1 task 4` and SA-C-g, SA-C-j, SA-C-k below.
- **finding-2 (Minor): concurred.** It interacts with this record's finding-1: both reword the `schedule_at` clauses, so one change set should carry both.
- **finding-3 (Minor): concurred.** `irq()` for `N > 3` returning `TIMER0_IRQ_3` would enable the wrong line; no instance exists today because `new` is the only constructor and asserts `VALID`.
- **finding-4 (Minor): concurred.** Two constant sets for `RESETS` are a configuration risk (`swe-080 7.1 task 2`), not a behaviour defect today (both give `0x0` and `0x8`).
- **finding-5 (Minor): concurred, one location added.** `timer/tests.rs:41` also uses a numeric `as u32` (masked, so clippy is silent; S3), and `timer_tests.rs:15` shifts before its cast; the CS-15 fix should cover all three.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the code review of a safety-critical driver (07 section 2.1.1 row "Code") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan, 07 section 15, by this record | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-060 7.1 task 1 | | Yes | The code implements ADR-053 section 2 items 1 to 3: `api::time` shapes (`api/src/time/mod.rs:39-158`), the `new`, `split`, `schedule`, `take_fired` sequences (`timer.rs:97-217`), the ICD pages; the arm sequence equals ICD `02_programming.md` steps 1 to 5 | | none |
| swe-060 7.1 task 2 | | Yes | No functionality outside ADR-053 or 07 section 19 row WP-SW-01: no `TIMEW`, `LOCKED` or `SOURCE = clk_sys` use (`timer/mod.rs:39-58`), no busy wait (ICD 12.8.4.3) | | none |
| swe-061 7.1 task 1 | | Yes | 07 section 7 (CS-01 to CS-39) is the selected standard; CS-34 to CS-38 bind the rustos WP (07 section 19) | | none |
| swe-061 7.1 task 2 | | Yes | CS-13 (`TimerError`, `AlarmError`, `Infallible`), CS-16 (no floating point), CS-37 (`&ClocksReady`, `timer.rs:110`; loop-count poll budget, not TIMER0), CS-38 (target-only code straight-line, `timer.rs:109-112`, `:223-251`) hold; CS-15 and CS-21 do not at three test-code locations and one module name (INSP-097 finding-5, Minor) | | none (INSP-097 finding-5) |
| swe-207 7.1 task 1 | | Yes | 07 section 7.6 holds the secure coding practices (charter section 12, SWE-185 and SWE-207 fully compliant) | | none |
| swe-185 7.1 task 1 | | Yes | Independent clippy run (S3): no security-relevant lint; no `unsafe` (S5); the only external input is the caller's `Instant`, validated by `plan_arm` (`Due`, `TooFar`) before any register write | | none |
| swe-135 7.1 task 1 | | Yes | Independent static analysis S3 (clippy), S4 (complexity), S2 (coverage) performed and compared with INSP-097 C1 to C5 and SW-03 line 31: defects and complexity values agree; SW-03 understates the lint result (INSP-097 finding-5) | | none |
| swe-135 7.1 task 2 | SC | Yes | clippy with `-W clippy::pedantic` (CS-27 set) and Miri (INSP-097 C3, clean at the stack head) are the checkers of 07 section 8.1 | | none |
| swe-135 7.1 task 3 | | Yes | The two lint results are raised as INSP-097 finding-5 with a fix; nothing unaddressed | | none |
| swe-135 7.1 task 4 | | Yes | No security defect class applies beyond S3 and S5 (no `unsafe`, no parsing, no buffer); `cargo deny` is a cwht-side gate (G-row of 07 section 8.4) run on the pin-move CR branch | | none |
| swe-135 7.1 task 5 | SC | Yes | S2: host lines 100 % for the three package files; the credited SWE-219 figure is `TC-SW-COV-001-r<N>` at a tagged release (07 section 9.5 item 4), not due at this review | | none |
| swe-135 7.1 task 6 | SC | Yes | S4: max CC 7, no waiver needed (07 section 14.3) | | none |
| swe-135 7.1 task 7 | | Yes | Thresholds set: CS-27 lint levels, CS-17 CC 15 with yellow 12, 07 section 9.5 coverage 100 % | | none |
| swe-134 7.1 task 2 | SC | No | Section C: items a, b, d, e, f, h and l hold or are met by construction; g, j and k are not met at `now == at` (INSP-097 finding-1, Major, Open), and k lacks the error-state clause (finding-1 of this record); i is recorded as finding-2 | | INSP-097 finding-1; finding-1; finding-2 |
| swe-134 7.1 task 3 | SC | N/A | The package holds no loaded data, uplinked data, rules or scripts: the only constants are register offsets and fixed values checked at compile time (`timer/mod.rs:74-97`) | Not applicable by construction: 07 section 9.7 names the loaded items (image, persisted configuration), neither in this package | none |
| swe-087 7.1 task 4 | SC | No | As swe-134 task 2, at this code inspection | | INSP-097 finding-1 |
| swe-062 7.1 task 1 | SC | Yes | S1: 30 tests executed and passed, including every safety-relevant path (`Due` at and before now, `TooFar` edge, fire during arming, missed match, failed arm, latch cleared only after a read); the contract draft (5 tests) and the dev-board check are test-author phase-2 items (SW-03 lines 44 to 48), not due at this review | | none |
| swe-062 7.1 task 2 | | Yes | Defects found in unit testing are tracked as review findings (INSP-097, this record); none closed without evidence | | none |
| swe-219 7.1 task 1 | SC | Yes | MC/DC pairs for `after_arm` (`timer/tests.rs:53-78`: A, I and L each with the others held) and single-condition decisions `plan_arm` (`tests.rs:22-51`) and `select_time` (`tests.rs:6-20`) checked; host line and region coverage S2; the SWE-219 record (table, MSR-13, MSR-14) is due at release (07 section 9.6 item 3). The pair at `tests.rs:60` encodes the INSP-097 finding-1 boundary and changes with its fix | SWE-219 method T in `rmm.json` (manual MC/DC tables, 07 section 9.6) | none |
| swe-220 7.1 task 1 | SC | Yes | S4 performed | | none |
| swe-220 7.1 task 2 | SC | Yes | Every function CC at most 7, below 15 | | none |
| swe-134 7.1 task 6 | SC | No | ADR-053 section 4.3 is consistent with HZ-004 for items g and k but states no hazard-analysis update although the shared time base is a common cause of the HZ-004 software controls | | finding-2 |
| swe-205 7.1 task 1 | SC | No | HZ-004 names "a firmware or reset fault" as a cause (`03` section 4.3 row), which covers a TIMER0 fault generically; the common cause of the keyer and monitor timing on one counter is not recorded | | finding-2 |
| swe-052 7.1 task 2 | SC | Yes | HZ-004 traces to REQ-SW-KEYER and REQ-SYS rows both ways (S7: 0 violations); the package is a driver and carries no requirement id (CS-24 applies to cwht code only, plan WP-PDR-41); the SW-HAL behaviours it serves are to be written by WP-PDR-35 (ADR-053 section 4.1) | | none |
| swe-211 7.1 task 1 | | N/A | rustos `api` and `pico2` are tested to the custom-code level in full, not as reused code (charter section 12 row SWE-211; 07 section 9.9) | charter section 12 row SWE-211 | none |
| swe-087 7.1 task 1 | | Yes | INSP-097 filed with evidence and findings | | none |
| swe-087 7.1 task 2 | | Yes | No earlier iteration; findings open with fixes named | | none |
| swe-088 7.1 task 1 | | Yes | SA-A4: NPR 7150.2D 5.3.3 a to d met by INSP-097 (checklist revision B, readiness, every item answered with evidence, findings tracked) | | none |
| swe-088 7.1 task 2 | | Yes | Actions are the open findings; resolution is the iteration 2 delta | | none |
| swe-089 7.1 task 1 | | Yes | SA-E2: both records carry size, findings by severity and state, turns and minutes | | none |
| swe-080 7.1 task 2 | | Yes | The change is tracked as WP-SW-01 on a rustos branch for the owner's merge (OD-23), with a Class I pin-move CR at merge (PCR-4); not yet implemented in cwht | | none |
| swe-080 7.1 task 3 | | Yes | ADR-019 route: rustos change proposed by ADR, merged by the owner; nothing pushed or merged | | none |
| swe-081 7.1 task 2 | SC | Yes | The package is under git CM at `a1cd160`; the hazard data it touches (finding-2) is `hazards.json` under 05 control | | none |
| swe-187 7.1 task 1 | | Yes | The developer tests run on the committed blobs at `a1cd160` (S1); run-for-record credit comes only from a tagged release (07 section 9.8) | | none |
| swe-187 7.1 task 2 | | N/A | No test for record has started on this package | 07 section 9.8 (credit only on a tagged release; none exists for FW-B1) | none |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | Yes | `product_files` equal INSP-097; `git rev-parse` of every blob (Product paragraph); frozen before both reviews (SW-03 line 17) |
| R2 | Yes | 07 section 2.1.1 row "Code", safety-critical column; 07 section 14.1 drivers row "TIMER alarms", `pico2` WP-SW-01 |
| R3 | Yes | `tools/validate_docs.py` passes on the cwht product files (ADR and sprint files carry no schema; the pre-existing failures are other records); S7 reports no violation |
| R4 | Yes | INSP-097 filed (`9d3734c`) by `reviewer:WP-PDR-41-code`; this invocation is a third invocation |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row "Code" Yes for safety-critical; 07 section 14.1 drivers row (line "Drivers these depend on: ... TIMER alarms ...", `pico2` WP-SW-01, criteria inherited) |
| SA-A2 | Yes | `author_agent`, `reviewer_agent` and this record's `reviewer_agent` are three invocations; INSP-097 names this path in `assurance_reviewer_agent` |
| SA-A3 | Yes | Same product, product commit and nineteen blobs as INSP-097 |
| SA-A4 | Yes | INSP-097 used `peer-review-checklist-code.md` revision B (07 section 10.1; 08 section 3.5), answered every item with evidence and ran six commands (C1 to C6) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: every task of the rows "Every product type" and "code", plus SWE-134 task 6, SWE-205 task 1, SWE-052 task 2, SWE-211 task 1 and the section E tasks; `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | The three N/A rows cite 07 section 9.7, charter section 12 and 07 section 9.8 |
| SA-B3 | Yes | Each No row names INSP-097 finding-1 or this record's finding-1 or finding-2 |

## C. SWE-134 items a to l

The package is a driver: 07 section 14.1 gives it the criteria of the components it serves, `SW-KEYER` (items a to l) and `SW-SCHED` (a, c, f, j, k, l), and 07 section 14.2 has no TIMER row of its own. Each item is answered for what the driver contributes.

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | `release` brings TIMER0 to a known state after every construction, whether or not the block was reset: `SOURCE` tick, `PAUSE` 0, `DBGPAUSE` reset value, `INTE` 0, every alarm disarmed, every latch cleared (`timer.rs:137-156`; test `timer_tests.rs:21-37`); no alarm can fire from a previous run |
| SA-C-b | Yes | Alarm states (disarmed, armed, fired and latched) are the hardware `ARMED` and `INTR` bits; every transition goes through `schedule`, `disarm` or `clear_fired`, and `schedule` disarms first (`timer.rs:177`) |
| SA-C-c | N/A | The driver drives no safety output; a construction failure returns `ResetTimeout` for the caller's `safe_state()` path (07 section 14.2 row c) |
| SA-C-d | N/A | No operator override passes through the driver |
| SA-C-e | Yes | Out-of-sequence use is excluded by construction: no alarm before `ClocksReady` (CS-37), a reschedule replaces the target (ALM-5, disarm first), `take_fired` clears only a latch it saw (`timer.rs:210-217`) |
| SA-C-f | N/A | The driver holds no RAM state (zero-sized types); the targets live in hardware registers read back after the arm (item g) |
| SA-C-g | No | Read-back of `ARMED` and `INTR` after the arm (`timer.rs:186-188`) is the output integrity check, but at `now == at` it accepts an arm that may never fire (INSP-097 finding-1) |
| SA-C-h | Yes | The prerequisite of every TIMER0 use, the running 1 µs tick from the crystal, is enforced by the `&ClocksReady` argument (`timer.rs:110`; CS-37) |
| SA-C-i | No | No single driver event initiates RF (RF needs the keyer key-down and the PA-permit flag, 07 section 14.2 row i), but the single shared counter is a common cause of the keyer timing and the firmware key-down monitors that is not recorded (finding-2) |
| SA-C-j | No | Absolute scheduling bounds drift (ADR-053 assumption 2) and `Due` reports a late target at once, except the `now == at` case (INSP-097 finding-1), where the response is 2^32 µs late |
| SA-C-k | No | Every hardware refusal and impossible target returns a distinct error (`TooFar`, `NotArmed`, `ResetTimeout`) and the bounded poll ends in an error; the gap at `now == at` (INSP-097 finding-1) and the missing error-state clause of the portable contract (finding-1) remain |
| SA-C-l | N/A | The driver has no safe-state command; `cancel` disarms from any context |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | Considerations of SWEHB `swe-205` section 7.7.2 walked for the driver: control of safety-critical timing (element end, 1 kHz tick) applies and is covered by HZ-004's firmware-fault cause; common-cause faults (item 16) apply and are not recorded (finding-2); stored sequences, interlocks, operator disabling of controls do not apply to a driver |
| SA-D2 | Yes | The drivers row criteria are "inherited" from `SW-KEYER` and `SW-SCHED`, both safety-critical in 07 section 14.1 and 03 section 4.3; no new component |
| SA-D3 | Yes | S7: 0 violations; HZ-004 traces to its REQ-SW-KEYER and REQ-SYS rows both ways |
| SA-D4 | N/A | The package adds or changes no requirement |
| SA-D5 | N/A | No hazard-tracing requirement is added; the HZ-004 closing Test cases are in `docs/test_cases/sw-keyer/` (S7) |
| SA-D6 | No | The software safety analysis is not updated for the shared-counter common cause (finding-2) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | N/A | Iteration 1: no earlier findings |
| SA-E2 | Yes | INSP-097 and this record carry `product_size`, findings by severity and state, `effort_turns`, `effort_minutes` |
| SA-E3 | Yes | The rustos change follows ADR-019 (branch for the owner's merge, OD-23) and becomes a cwht configuration change only through the Class I pin-move CR (PCR-4); the cwht files (ADR-053, SW-03) were committed on main before the review (SW-03 line 17) |
| SA-E4 | Yes | Items under test are committed at `a1cd160` (S1); no credit run exists or is claimed |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the product findings; finding-2 is a hazard-data item routed to WP-PDR-16b, not a risk entry, and the related keyed-on risk is RSK-024 |
| SA-F2 | Yes | Front matter: `findings_*`, `assurance_findings_*`, `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are stated in this record |

## Completion criteria and verdict

`assurance_verdict: NEEDS CHANGES`. Readiness R1 to R4 were true; every task SA-B1 requires is in the task table; this record raises no Major finding of its own and two Minor findings; it concurs with the open Major INSP-097 finding-1, which leaves `swe-134 7.1 task 2` and `swe-087 7.1 task 4` answered No for SWE-134 items g, j and k of a safety-critical driver. The assurance review becomes APPROVED at a delta iteration that verifies the INSP-097 finding-1 fix at its new blobs; findings 1 and 2 of this record are then fixed or become liens due at the CDR readiness declaration (rule C1). The record `verdict` stays held under the lead SE convention of 2026-09-27 until the blobs reach a configuration cwht consumes (the owner's merge and the PCR-4 pin-move CR).

## Cross items (returned to Claude)

- **X-1 (to INSP-097, its reviewer's own record):** INSP-097 carries `assurance_verdict: pending` and no `paired_record`; its reviewer sets `paired_record: INSP-103` and copies `assurance_verdict: NEEDS CHANGES` (07 section 10.2). This record does not edit INSP-097.
- **X-2 (to WP-PDR-16b):** finding-2, the shared TIMER0 counter as a common cause of the HZ-004 K3 and K4 firmware controls, bounded by K5 and K7, for the HZ-004 fault tree of `hazard-analysis.md` section 8.
- **X-3 (to WP-PDR-35 and the `SW-SCHED` design):** the `SW-HAL` behaviours cwht relies on include the `CsCell` sharing rule of S6 (an alarm reached from thread code only inside a critical section) and the handler response to `Scheduled::Due` on the 1 kHz tick (process the tick, advance the target by 1000 µs and re-arm, with the overrun counted; 07 section 14.2 `SW-SCHED` row k), since a handler that stops at `Due` leaves no alarm armed.
- **X-4 (to the lead SE):** INSP-103 was chosen without an assigned id (front matter comment).

## Commands

| # | Command | Exit |
|---|---|---|
| 1 | `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa-wp-sw-01 a1cd160` (removed afterwards with `git worktree remove`) | 0 |
| 2 | S1 to S5 in that worktree | 0 |
| 3 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --report-only --output <scratchpad>/trace-sa01.md` | 0 |
| 4 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` | 1 (eight pre-existing failures in other records; this record PASS) |

## Verdict format

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: rustos cwht/wp-sw-01 blobs of product_files at a1cd160, ADR-053@471b900f, SW-03@8fed7b88; PAIRED RECORD: INSP-097
PRODUCT TYPE: code; CRITICALITY: safety-critical
FINDINGS:
- [Major, concurred, not re-raised] INSP-097 finding-1: missed-match check treats armed with now == at as pending (SWE-134 g, j, k).
- [Minor] finding-1 SA-C-k: portable contract has no clause or check for the alarm state after a non-TooFar Err.
- [Minor] finding-2 SA-D1: ADR-053 records no common cause of the HZ-004 K3 and K4 controls on the shared TIMER0 counter.
TASKS APPLIED: 34 (front matter)
TASKS N/A (relief): swe-134 7.1 task 3 (07 section 9.7), swe-211 7.1 task 1 (charter section 12), swe-187 7.1 task 2 (07 section 9.8)
SWE-134 ITEMS CHECKED: a to l (c, d, f, l N/A for a driver; g, i, j, k No)
MEASUREMENTS: size=1429 lines added, 19 files; tasks=37; tasks_no=4; turns=45; minutes=80; major=0 (plus INSP-097 finding-1 concurred); minor=2
```

## Iteration 2: assurance delta on the drifted blobs (2026-09-27, cwht HEAD `a244b05`, rustos `58fe739`)

**Scope (rule C1; SA-A3).** INSP-097 iteration 2 (`134e555`) moved to rustos `cwht/wp-sw-01` at `58fe739` and verified its finding-1 (Major) and finding-2 (Minor). This delta reads every hunk of the eight blobs that drifted from iteration 1 and verifies the concurred Major under the assurance lens: ADR-053 `471b900f` to `71f0b629`; SW-03 `8fed7b88` to `1cea48ef`; `docs/sprints/index.md` `fb217bcb` to `7ae0cbcc`; rustos `api/src/time/mod.rs` `f62b4961` to `3c6c5673`, `timer/mod.rs` `a1ef29c8` to `4004047d`, `timer/tests.rs` `247eeb82` to `ed14e12e`, `timer/timer_tests.rs` `e1657cab` to `bbe94275`, `firmware/pico2/src/lib.rs` `dcd1c254` to `5393076c`. The other eleven blobs are unchanged (`git rev-parse 58fe739:<path>` equals iteration 1), `timer.rs` (`e24f1d5`) among them. Findings 1 and 2 of this record are re-read for state, not re-reviewed. Checklist as at iteration 1.

**Independence (rule C4).** This invocation authored no part of WP-PDR-41, of revision 2, of the rustos fix commits or of INSP-097, and edited no product file. The rustos repository was read with `git show` and `git diff`, and exercised in a detached scratch worktree at `58fe739` (`git worktree add --detach` in the scratchpad, removed after the review; `git worktree list` shows none left). The owner's rustos working tree was not read or changed. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: INSP-097 iteration 2 finding-1 verification) ran before any `grep`; `grep` afterwards only pinned lines in known files.

### Assurance re-runs and checks, iteration 2

| # | Command or check (scratch worktree at `58fe739`, `RUSTUP_AUTO_INSTALL=0`, `--offline`; no download) | Result |
|---|---|---|
| T1 | `git rev-parse 58fe739:<path>` for the sixteen rustos paths; `git rev-parse HEAD:<path>` for the three cwht paths | all nineteen equal `product_files` and INSP-097 iteration 2 |
| T2 | `git diff a1cd160 58fe739 --` the five drifted rustos files; `git diff <old> <new>` of the three cwht blobs; every hunk read | hunks as in the table below |
| T3 | `cargo +1.98.0 test --offline -p pico2 --lib`; `cargo +1.98.0 test --offline -p api` | pico2 75 passed, 0 failed (includes `after_arm_armed_and_late_is_missed`, `after_arm_armed_and_not_late_is_pending`, `schedule_still_armed_when_the_time_equals_the_target_is_due_and_disarmed`); api `irq_contract` 4, `time_contract` 5 passed |
| T4 | Mutation check of the fix: `now >= at` set back to `now > at` in the worktree copy of `timer/mod.rs`, T3 re-run, then `git checkout` of the file | 2 failed (`after_arm_armed_and_late_is_missed`, `schedule_still_armed_when_the_time_equals_the_target_is_due_and_disarmed`), 73 passed: the new unit test and the new driver test each detect the iteration 1 behaviour; worktree clean afterwards |
| T5 | `cargo llvm-cov --offline -p pico2 -p api --summary-only` (cargo-llvm-cov 0.9.1) | `api/src/time/mod.rs` regions and lines 100 %; `timer/mod.rs` regions and lines 100 %; `timer.rs` regions 98.05 % (3 of 154), lines 96.55 % (3 of 87). The text report shows a non-zero count on every line of `timer.rs`; the three missed regions and lines are the `match N` arms of `irq()` (lines 88 to 92) counted per monomorphized `Rp2350Alarm::<N>` (each arm count 1). The blob is unchanged, so the difference from the 100 % line figure of S2 is a counting of the same arms, not new uncovered code. Development-build measurement, not the credited MSR-13 figure |
| T6 | `cargo +1.98.0 clippy --offline -p pico2 -p api --all-targets --message-format=short -- -W clippy::pedantic`, filtered to `timer/` and `time/` | `module_inception` at `timer/mod.rs:32`; `cast_possible_truncation` at `timer_tests.rs:16`; both INSP-097 finding-5 (lien); no lint on a line revision 2 adds or changes |
| T7 | `git show 58fe739:firmware/pico2/src/irq/vectors.rs` for the slots the `lib.rs` hunk moves | `with_device_interrupts` sets `t[16]` to `t[19]` to `TIMER0_IRQ_0` to `TIMER0_IRQ_3`, the lines `Rp2350Alarm::<N>::irq()` returns (`timer.rs:87-94`); the extern declarations moved with them |

### Hunks read, under the assurance lens

| Blob | Hunk | Assurance reading |
|---|---|---|
| `api/src/time/mod.rs` | ALM-1 and ALM-2 (lines 17 to 26) | ALM-1 is stated against the clock at the start of the call and allows `Due` for a target reached during the call, always with the alarm not armed and nothing latched; ALM-2 allows `Armed` with the fire latched before return. Both outcomes the driver can produce at `now == at` are within the contract, and neither leaves a silent wait (SWE-134 j, k). The `schedule_at` error clause is unchanged: finding-1 of this record stands |
| `timer/mod.rs` | `AfterArm` docs; truth table; `after_arm` `now >= at` | The decision now classifies `armed && now >= at` as `Missed`; the disarm on `Missed` discards a fire latched after the read, so a `Due` result never leaves a latched fire (ALM-1). Under a comparator that does fire on a write in the matching microsecond, `ARMED` is clear and `INTR` set, the row `0 1 any` gives `Pending` and `Armed` is returned with one fire latched (ALM-2). Safe under both behaviours; SWE-134 g (read-back) and j (bounded response) now hold at the edge |
| `timer/tests.rs` | L pair `(199, 200)` Pending against `(200, 200)` Missed; `(201, 200)` kept | The MC/DC pair of condition L sits on the `>=` edge (SWE-219 task 1), confirmed sensitive by T4 |
| `timer/timer_tests.rs` | `schedule_still_armed_when_the_time_equals_the_target_is_due_and_disarmed` | Time 99 at the plan read (so `plan_arm` arms) and 100 after the write, `ARMED` 1, target 100: `Due`, then disarm and `INTR` clear as the last two writes; exercises the full `schedule` path of the edge, confirmed sensitive by T4 |
| `firmware/pico2/src/lib.rs` | `Vector`, the device-interrupt slots and their extern block move to `irq::vectors` (merge `698929d` of `cwht/wp-sw-09` at `c6e5100`, INSP-096 finding-1) | No behaviour change for this package: slots 16 to 19 keep `TIMER0_IRQ_0` to `TIMER0_IRQ_3` (T7). The moved `unsafe` extern block and `unsafe impl Sync` are WP-SW-09 sites reviewed under INSP-096 and its assurance pair INSP-102; this package adds no `unsafe` site (S5 holds) |
| ADR-053 | status date; section 2 items 1 and 2; section 3 row A; section 4.3 evidence and dev-board case; new section 8 | Section 2 and row A match the code. Section 4.3 "Hazard analysis update required: no" is unchanged: finding-2 of this record stands. The new dev-board case for the `now == at` edge cannot reach that edge: finding-3 |
| SW-03 | product row; "Phase 1, revision 2"; phase 3 line | Accurate to the rustos history (`698929d`, `58fe739`) and to the rule C1 scope; the evidence line (75 `pico2` tests) matches T3 |
| `docs/sprints/index.md` | five product and status cells | SW-03 row names `58fe739`, as T1; the other four rows are other packages (not assessed here) |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| INSP-097 finding-1 (concurred) | reviewer (INSP-097) | Major | SA-C-g, SA-C-j, SA-C-k; `swe-134 7.1 task 2`; `swe-087 7.1 task 4` | `timer/mod.rs:165-184`; `timer/tests.rs:60-68`; `timer_tests.rs:119-127` | missed-match check treated `armed` with `now == at` as pending | Verified (`58fe739`; T3, T4, hunk table) | | |
| finding-1 | assurance | Minor | SA-C-k; `swe-134 7.1 task 2` | `api/src/time/mod.rs` `schedule_at` error clause (line 138 at `3c6c567`); `api/tests/time_contract.rs` | no contract clause or check for the alarm state after a non-`TooFar` `Err` | Open (lien, rule C1; not addressed by revision 2, ADR-053 section 8) | Pending | CDR readiness declaration |
| finding-2 | assurance | Minor | SA-D1; SA-C-i; `swe-205 7.1 task 1`; `swe-134 7.1 task 6` | ADR-053 section 4.3 "Hazard analysis update required: no" (unchanged at `71f0b629`) | shared TIMER0 counter is an unrecorded common cause of the HZ-004 K3 and K4 firmware controls, bounded by K5 and K7 | Open (lien, rule C1; X-2 to WP-PDR-16b stands) | Pending | CDR readiness declaration |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-062 7.1 task 1`; SA-C-g (hardware evidence) | ADR-053 section 4.3, dev-board check bullet (at `71f0b629`) | The new dev-board case, "a target equal to the time read at arming returns `Due` (the `now >= at` edge ...)", cannot reach the `after_arm` edge it names. `schedule` reads the time itself before arming (`timer.rs:178`, `plan_arm(read_time(regs), at)`), and the counter never decreases, so a target equal to an earlier caller read gives `at <= now` and `plan_arm` returns `Due` before `ALARMn` is written (`timer/mod.rs:132-134`). The case passes 10 000 times with or without the fix (T4 shows the host tests, not this case, detect it), and the pass criterion "returns `Due`" is also narrower than ALM-2, which allows `Armed` with the fire latched before return when a write in the matching microsecond fires. The fix is verified by analysis and host tests; the gap is in the hardware evidence of section 12.8.3 behaviour the ADR plans. Fix: the test author arms for `t + k` with `k` swept over the first few microseconds after a time read `t`, so the `ALARMn` write lands in the matching microsecond in some repetitions, and accepts `Due`, or `Armed` with `take_fired()` true within a stated bound, and fails only on `Armed` with no fire within that bound; ADR-053 section 4.3 is reworded to match | Open (lien, rule C1; for the phase 2 test author, SW-03 lines 52 to 55) | Pending | CDR readiness declaration |

### Items re-answered at iteration 2

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| SA-C-g | Yes | Read-back of `ARMED` and `INTR` after the arm now treats `armed && now >= at` as a missed match and disarms (T3, T4); finding-3 is a lien on the planned hardware evidence, not on the code |
| SA-C-j | Yes | No path leaves a 2^32 µs wait: `Due` at and before the start of the call (`plan_arm`), `Due` or `Armed` with the fire latched at the edge (`after_arm`) |
| SA-C-k | No (Minor, lien) | The `now == at` gap is closed; the missing error-state clause of the contract (finding-1) remains as a lien |
| `swe-087 7.1 task 4` | Yes | INSP-097 finding-1 Verified; no Major open on the code inspection of a safety-critical driver |
| `swe-134 7.1 task 2` | No (Minor liens only) | Items a, b, e, g, h, j hold; c, d, f, l N/A; i (finding-2) and k (finding-1) carried as Minor liens due at the CDR readiness declaration |
| `swe-219 7.1 task 1` | Yes | The L pair is on the `>=` edge and T4 shows it detects the iteration 1 comparator |
| `swe-062 7.1 task 1` | Yes | T3: 75 pico2 and 9 api contract tests pass; the planned dev-board case is corrected by finding-3 (lien), and the dev-board check is still a phase 2 item, not due at this review |
| SA-E1 | Yes | `swe-087` tasks 1 and 2, `swe-088` task 2: the earlier Major (INSP-097 finding-1) is addressed and verified with evidence (T3, T4); findings 1 and 2 of this record are not closed and are carried as liens with an owner and a due event |
| SA-A3 | Yes | This record and INSP-097 iteration 2 name the same product commit `58fe739` and the same nineteen blobs (T1) |

### Cross items, iteration 2 (returned to Claude)

- **X-5 (to INSP-097, its reviewer's own record):** INSP-097 carries `assurance_verdict: pending` at iteration 2; its reviewer copies `assurance_verdict: APPROVED` (INSP-103 iteration 2). This record does not edit INSP-097.
- **X-6 (to the phase 2 test author of SW-03 and the ADR-053 author):** finding-3, the dev-board case for the `now == at` edge.
- **X-7 (to the lead SE, PDR package section 15):** three liens of this record (findings 1, 2 and 3), owner the firmware developer (findings 1 and 3, with the test author for 3) and WP-PDR-16b with the ADR-053 author (finding-2), due at the CDR readiness declaration.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 53 changed lines of the four package files in `698929d..58fe739`, the `lib.rs` hunk (3 added, 146 removed lines), the unchanged `timer.rs` `schedule` path and `irq/vectors.rs` slot table as context, and the changed lines of ADR-053, SW-03 and the sprint index. Unsafe sites added by the package: none. Findings: 1 new (Minor), 0 new Major; the concurred Major Verified. Effort of this iteration: about 20 turns and 35 minutes (front matter totals include iteration 1).

### Commands, iteration 2

| # | Command | Exit |
|---|---|---|
| 1 | `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa2-wp-sw-01 58fe739`; removed with `git worktree remove --force` after T6 | 0 |
| 2 | T3 to T6 in that worktree (T4 edits only the worktree copy and restores it with `git checkout`) | 0 (T4 run: 101, expected) |
| 3 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` | see the commit of this record |

### Completion criteria and verdict, iteration 2

`assurance_verdict: APPROVED`. The concurred Major INSP-097 finding-1 is Verified at `58fe739` by independent re-run, a mutation check that shows both new tests detect the iteration 1 behaviour, and a reading of every drifted hunk; no Major is open against a SWE-134 item of this safety-critical driver. Findings 1 and 2 of this record were not addressed by revision 2 and, with new finding-3, are Minor liens due at the CDR readiness declaration (rule C1). The record `verdict` stays held at `NEEDS CHANGES` under the lead SE convention of 2026-09-27 until the owner's merge of `cwht/wp-sw-01` and the PCR-4 pin-move CR bring `58fe739` into a configuration cwht consumes.

```
ASSURANCE VERDICT: APPROVED (iteration 2, delta)
PRODUCT: rustos cwht/wp-sw-01 blobs of product_files at 58fe739, ADR-053@71f0b629, SW-03@1cea48ef, sprint index@7ae0cbcc; PAIRED RECORD: INSP-097 (iteration 2)
PRODUCT TYPE: code; CRITICALITY: safety-critical
FINDINGS:
- [Major, concurred] INSP-097 finding-1: Verified at 58fe739 (T3, T4).
- [Minor, lien] finding-1 SA-C-k: contract error-state clause for a non-TooFar Err.
- [Minor, lien] finding-2 SA-D1: common cause of HZ-004 K3 and K4 on the shared TIMER0 counter not recorded.
- [Minor, lien, new] finding-3 swe-062: dev-board case for the now == at edge cannot reach it (plan_arm returns Due first).
SWE-134 ITEMS CHECKED: a to l (c, d, f, l N/A; g, j now Yes; i, k No on Minor liens)
MEASUREMENTS: iteration 2 turns=20; minutes=35; major new=0; minor new=1; record verdict held (unmerged rustos branch)
```
