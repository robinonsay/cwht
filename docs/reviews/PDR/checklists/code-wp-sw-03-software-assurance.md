---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the code review INSP-099
# (docs/reviews/PDR/checklists/code-wp-sw-03.md, iteration 1 by reviewer:WP-PDR-41-code), at the path INSP-099
# names in assurance_reviewer_agent and PDR work plan WP-PDR-41 "Records" names ("code-wp-sw-<nn>.md and
# -software-assurance.md per WP"; SA because the drivers serve safety-critical components, 07 section 14.1).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged: the
# template is absent from main on 2026-09-27). The `checklist` field names peer-review-checklist-code revision B,
# the checklist INSP-099 names, because tools/validate_docs.py fails a record whose `checklist` names a template
# absent from main, and the lead SE convention of 2026-09-27 does not change the validator. `assurance_checklist`
# names the template actually applied (the form of INSP-048, INSP-049, INSP-051 and INSP-070).
# id: the brief assigned no id. The highest id in docs/reviews on main, on every local branch and in the working
# tree was INSP-100 at filing (2026-09-27). Four sibling SA invocations for INSP-095 to INSP-098 run in parallel
# and may take the next numbers, so this record takes INSP-105, the fifth after INSP-100 in the WP-PDR-41 record
# order (WP-SW-11, 09, 01, 02, 03), leaving 101 to 104 to them
id: INSP-105
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-03-software-assurance.md
product: "rustos cwht/wp-sw-03: api/src/pwm/mod.rs, firmware/pico2/src/pwm/ and docs/icd/rp2350/pwm/ (WP-SW-03)"
# product_commit and product_files: equal to INSP-099 (readiness R1; rule C2). The fourteen rustos blobs exist only
# on the unmerged rustos branch cwht/wp-sw-03 (git -C rustos rev-parse 6df18af:<path>, checked 2026-09-27: all
# equal); the three cwht blobs are on main and equal HEAD and 618e441 (git rev-parse). The lead SE branch-only
# convention therefore applies to the rustos blobs and to the checklist template
# product_commit and product_files (iteration 2, 2026-09-27): rustos cwht/wp-sw-03 at 48e07ec (branch tip checked
# with git rev-parse cwht/wp-sw-03), the INSP-099 finding-1 and INSP-105 finding-1 fix on the merge 9df9c57 of
# cwht/wp-sw-02 38434b2; the fourteen rustos: blobs equal git -C rustos rev-parse 48e07ec:<path> and exist only on
# the unmerged branch; the three cwht blobs equal git rev-parse HEAD:<path> and git hash-object at HEAD ae29a98
# (ADR-055 and SW-05 revision 2 committed at e3ce2cb). Drift from iteration 1: ADR-055, SW-05, the sprint index,
# api/src/pwm/mod.rs, pwm/pwm.rs, pwm/pwm_tests.rs, lib.rs (merge only) and the PWM ICD 01_overview.md
product_commit: "48e07ec7d651f8f323f8b82b2af5d5647afe0fe3"
product_files: ["docs/decisions/adr/ADR-055-wp-sw-03-pwm-output.md@c2c7cc999e033340195dd7363fe661b91ece0318", "docs/sprints/SW-05-wp-sw-03-pwm.md@d904d7deaa3553e5685244931a0b96730a8ee8dc", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:api/src/pwm/mod.rs@b859f3705320a2d88bcd6839c540b8068ef6b6ab", "rustos:api/tests/pwm_contract.rs@7df5fdd237aefba2b13ec72d62945ba38092146b", "rustos:api/src/lib.rs@5e79e2b739469c8c077c9a637814977e956e88a5", "rustos:firmware/pico2/src/pwm/mod.rs@9c8ed4c4ba7c2b279cd736c518897206b40689f4", "rustos:firmware/pico2/src/pwm/pwm.rs@92b634e18bcbd4316a92edbfcef66b228b85a93c", "rustos:firmware/pico2/src/pwm/pwm_tests.rs@82d96ce9f75326f3254ebced6a4ff3b64d4b53ff", "rustos:firmware/pico2/src/pwm/tests.rs@c0a59856277c6e45e70dab78f3b6fe058ac4da2b", "rustos:firmware/pico2/src/common/board.rs@eeb8407e77a93718c7e0a2cb320fa2ec6b25f4cc", "rustos:firmware/pico2/src/common/reg.rs@ec94f2cdee391615d8fd88b0650a3f830bc2ef80", "rustos:firmware/pico2/src/lib.rs@46107a9e0e48a88f4ce1c53441bb8bc482c818b2", "rustos:docs/icd/rp2350/pwm/index.md@17e8dabbc10f7a54ce6e50cb0cd50d97378af8f7", "rustos:docs/icd/rp2350/pwm/01_overview.md@98ae5870e970cfdfe644dcb19a3dd7823552b32c", "rustos:docs/icd/rp2350/pwm/02_registers.md@7f93b2004a0d0065bec0342e5f7a0bc28acb5a7a", "rustos:docs/icd/rp2350/index.md@426a75dfd588af945bba6b5533da819b93d18a75"]
product_files_iteration_1: ["docs/decisions/adr/ADR-055-wp-sw-03-pwm-output.md@7b2a9d920d57d0a03e4b995de811cad0e68215c3", "docs/sprints/SW-05-wp-sw-03-pwm.md@975d9268b5b455d7436b919e67fe02d948014764", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/pwm/mod.rs@1c13d0ad73ffb972a59399d9b93ce11b1b7d406f", "rustos:api/tests/pwm_contract.rs@7df5fdd237aefba2b13ec72d62945ba38092146b", "rustos:api/src/lib.rs@5e79e2b739469c8c077c9a637814977e956e88a5", "rustos:firmware/pico2/src/pwm/mod.rs@9c8ed4c4ba7c2b279cd736c518897206b40689f4", "rustos:firmware/pico2/src/pwm/pwm.rs@75bca4e87fe68c4f61906e27b18b0d43cc07fb9f", "rustos:firmware/pico2/src/pwm/pwm_tests.rs@c3286c6d9db9bb776f1d8c2e79107eff1755e60e", "rustos:firmware/pico2/src/pwm/tests.rs@c0a59856277c6e45e70dab78f3b6fe058ac4da2b", "rustos:firmware/pico2/src/common/board.rs@eeb8407e77a93718c7e0a2cb320fa2ec6b25f4cc", "rustos:firmware/pico2/src/common/reg.rs@ec94f2cdee391615d8fd88b0650a3f830bc2ef80", "rustos:firmware/pico2/src/lib.rs@5122df422db03e15da04aa9cc784d4b96d437ec0", "rustos:docs/icd/rp2350/pwm/index.md@17e8dabbc10f7a54ce6e50cb0cd50d97378af8f7", "rustos:docs/icd/rp2350/pwm/01_overview.md@346e561de8e7aea729ffb4e6274d0778d327634b", "rustos:docs/icd/rp2350/pwm/02_registers.md@7f93b2004a0d0065bec0342e5f7a0bc28acb5a7a", "rustos:docs/icd/rp2350/index.md@426a75dfd588af945bba6b5533da819b93d18a75"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/code-wp-sw-03.md (INSP-099 iteration 1, main 9d3734c; iteration 2 at HEAD ae29a98)", "docs/safety/hazards.json (HZ-005 causes C2 and C4, controls K4 and K5)", "docs/requirements/sw/sw-keyer/requirements.json (REQ-SW-KEYER-027, 033, 035)", "docs/test_cases/sw-keyer/test_cases.md (TC-SW-KEYER-039 acceptance criteria)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 14.1, 14.2, 14.3, 15, 17.1, 19)", "docs/process/rmm.json (rows SWE-022, 027, 060, 061, 062, 134, 135, 185, 207, 219, 220)", "docs/plan/pdr-work-plan.md (sections 3.8 WP-PDR-41, 5.1)", "rustos 6df18af:firmware/pico2/src/common/reset.rs and gpio/gpio.rs (git show only; not product files)"]
paired_record: INSP-099
# product_type: code (07 section 2.1.1 row "Code", Yes for a safety-critical component). Task set applied: the
# section B row "Every product type"; the section B row "code"; and the section 7.1 tasks of the other SWEs the
# product implements: SWE-134 (ADR-055 section 4.3 claims items c, g and k; task 6 applied to that claim),
# SWE-219 (ADR-055 section 1 "Guidance consulted"), SWE-027 (07 section 17.1 row rustos pico2), SWE-205 and SWE-052
# (HZ-005 and REQ-SW-KEYER-033, which ADR-055 section 1 names), with the section E tasks (SWE-087, 088, 089)
product_type: code
# criticality: 07 section 14.1 drivers row (line 601): "PWM (sidetone and audio level)", pico2 WP-SW-03, criticality
# "as the components they serve", inherited from SW-AUDIO (HZ-005) and the SW-KEYER sidetone gate
criticality: safety-critical
product_size: "about 470 non-test Rust lines (pwm/mod.rs 165 before its tests, pwm.rs 226, api pwm 80), 18 developer tests, 187-line contract draft, 197 ICD lines; ADR-055 90 lines; SW-05 61 lines; 17 product files. Iteration 2 delta: git diff 9df9c57 48e07ec, 4 files, 116 insertions and 23 deletions; ADR-055 revision 2 (about 35 changed lines) and SW-05 (12 lines)"
sprint: SW-05-wp-sw-03-pwm
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-03"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-03 (software assurance function, iterations 1 and 2; paired file review INSP-099 by reviewer:WP-PDR-41-code)"
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: NEEDS CHANGES at iteration 1 on finding-1 (Major) of this record and on
# INSP-099 finding-1 (Major), whose severity the assurance lens confirms
# iteration 2: APPROVED. finding-1 (Major) is Verified at 48e07ec, and INSP-099 finding-1 (Major, concurred) is
# Verified by INSP-099 iteration 2, with which this delta concurs under the assurance lens. No Major is open.
# findings 2 and 3 (Minor, not addressed, rule C1) and finding-4 (Minor, new) are liens due at the CDR readiness
# declaration
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: this review and INSP-099 are
# NEEDS CHANGES, and under the lead SE convention of 2026-09-27 the record verdict of a review of branch-only blobs
# is set only in the merge commit (or the commit right after it) when the blobs reach a configuration cwht
# consumes (the owner's rustos merge and the PCR-4 pin-move CR).
# Iteration 2: still held. Both reviews are APPROVED, but the fourteen rustos blobs exist only on the unmerged
# branch cwht/wp-sw-03 and the checklist only on cr/CR-012-pdr-checklist-templates (lead SE convention 2026-09-27)
verdict: NEEDS CHANGES
# counts cover iterations 1 and 2: finding-1 (Major) Verified at iteration 2; finding-4 (Minor) new at iteration 2;
# open = findings 2, 3 and 4 (Minor liens)
findings_major: 1
findings_minor: 3
findings_open: 3
findings_fixed: 1
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 1
assurance_findings_minor: 3
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 3", "swe-135 7.1 task 5", "swe-135 7.1 task 6", "swe-135 7.1 task 7", "swe-134 7.1 task 2", "swe-087 7.1 task 4", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 4", "swe-052 7.1 task 1", "swe-052 7.1 task 2", "swe-192 7.1 task 1", "swe-027 7.1 task 1", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 2"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
# items_no at iteration 2 (iteration 1: SA-C-a, SA-C-j, swe-134 7.1 task 2, swe-087 7.1 task 4, swe-134 7.1 task 6,
# swe-062 7.1 task 1); SA-C-a, SA-C-j, swe-134 task 2 and swe-087 task 4 are Yes at iteration 2
items_no: ["swe-134 7.1 task 6", "swe-062 7.1 task 1"]
# effort cumulative: iteration 1 32 turns, 60 min; iteration 2 24 turns, 45 min
effort_turns: 56
effort_minutes: 105
record_status: Open
date: 2026-09-27
date_updated: 2026-09-27
date_closed: null
---

# Peer review record INSP-105: software assurance pair of INSP-099, code review of WP-SW-03 PWM output (rustos `api::pwm` and `pico2::pwm`), iteration 1

**Product.** rustos branch `cwht/wp-sw-03` at `6df18af` (parent `cwht/wp-sw-02` at `f85a190`), with ADR-055, SW-05 and the sprint index at cwht `618e441`: the seventeen blobs of the paired record's `product_files`. Identity checked with `git -C /Users/robinonsay/rust/rustos rev-parse 6df18af:<path>` for the fourteen rustos files and `git rev-parse HEAD:<path>` and `618e441:<path>` for the three cwht files: all seventeen equal the INSP-099 list.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). All sections are applied: R, A, B (row `code`, row "Every product type" and the other SWEs the product implements), C (items a to l), D, E and F. `product_type` is `code`, from the 07 §2.1.1 row "Code", which is Yes for safety-critical. `criticality` is safety-critical, from the 07 §14.1 drivers row (line 601): "PWM (sidetone and audio level)", criticality "as the components they serve", which are `SW-AUDIO` (HZ-005) and the `SW-KEYER` sidetone gate.

**Acceptance criteria (rule C7).** The criteria are:

- every task of the section B row `code` and of the row "Every product type";
- the section 7.1 tasks of SWE-134 (task 6, for the ADR-055 §4.3 claim of items c, g and k), SWE-219, SWE-027, SWE-205 and SWE-052;
- SWE-134 items a to l, taken from the union of the 07 §14.2 module rows the driver serves (`SW-AUDIO` a, b, d, g, j, k, l; `SW-KEYER` a to l);
- HZ-005 causes C2 and C4 and controls K4 and K5, read against ADR-055 §1 lines 22 and 23 and §3 line 44;
- REQ-SW-KEYER-027, 033 and 035 (the sidetone gate) with their closing cases;
- the two INSP-099 findings, re-read under the assurance lens.

**Independence (rule C4).** This invocation authored no part of WP-PDR-41, ADR-055, SW-05 or INSP-099, and edited no product file. It is neither the author (`author:WP-PDR-41 wave 1a`) nor the file reviewer (`reviewer:WP-PDR-41-code`).

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: "software assurance peer review record code-wp-sw software-assurance.md assurance_tasks_applied" and "WP-PDR-41 RSK-013 minimal keyer set WP-SW-03 PWM records reviewer". `grep -n`, `git grep` on committed rustos objects and read-only scripts were used afterwards only to pin lines and to extract the SWEHB section 7.1 lists. The owner's rustos working tree was not read. The one rustos build ran in a scratch worktree made with `git worktree add` from the rustos repository at `6df18af` (branch `cwht/wp-sw-03-sa`). The worktree and the branch were removed after the run. Nothing was pushed or merged.

## Assurance re-runs and checks

| # | Command or check | Result |
|---|---|---|
| S1 | `cargo test --offline -p pico2 pwm` and `cargo test --offline -p api --test pwm_contract` at `6df18af` (rustc 1.98.0, the CS-03 pin) | 18 passed; 5 passed. Agrees with INSP-099 C1 |
| S2 | `cargo llvm-cov --offline -p pico2` (stable, line and region coverage on the host build; developer evidence, not credit) | `pwm/pwm.rs` 100.00 % lines, 99.14 % regions; `pwm/mod.rs` 97.50 % lines, 98.28 % regions. The one missed line is the `_ =>` arm of the `u32::try_from` match (`pwm/mod.rs:150`), unreachable after the range checks at lines 132 and 136. The target-only `new`, `output_from_handle` and trait methods are not compiled on the host. `--branch` needs the nightly of CS-03 and was not run |
| S3 | `cargo clippy --offline -p pico2 --all-targets -- -W clippy::pedantic`, host and `thumbv8m.main-none-eabihf` | Only `module_inception` at `pwm/mod.rs:29` in the package files. Agrees with INSP-099 C4 and finding-2 |
| S4 | `tools/validate_docs.py`; `tools/traceability.py --report-only --output <scratch>/traceability-report.md` | validate_docs: 8 failures, all in records unrelated to this product (APPROVED-record drift on CR-007, ADR-001 to 025, TS-001 and TS-002 and others); none concerns the product files. Traceability: 245 requirements, 0 violations, 2 warnings (REQ-SYS-125, 148 unallocated). HZ-005 traces to REQ-SW-KEYER-033 with TC-SW-KEYER-033 and 039 |
| S5 | Restart path read: `release` (`pwm.rs:110-123`), with `git show 6df18af:firmware/pico2/src/common/reset.rs` and `gpio/gpio.rs` | `release` writes only `RESETS.RESET` through the clear alias, then `EN = 0`. It never asserts the PWM reset. `Rp2350Gpio::new` (`gpio.rs:152-155`) likewise only clears. `RESETS.WDSEL` resets to 0 (`reset.rs:72-84`), and no file of the stack writes it (`git grep -i wdsel 6df18af`) |
| S6 | HZ-005 read from `docs/safety/hazards.json` | C2 (Software): "Full-scale PWM pattern at start-up or after a fault". K4: "no DC step at any transition". K5: amplifier enable asserted "only after the audio source has idled at mid-scale for at least 20 ms" |
| S7 | TC-SW-KEYER-039 acceptance criteria (`docs/test_cases/sw-keyer/test_cases.md:1439`) | Pass if the first sidetone PWM edge is no later than "1.0 ms plus one PWM carrier period". Under ADR-055 the output is the tone itself, not a carrier, so "one PWM carrier period" is one tone period: 1.43 ms at 700 Hz and 10 ms at 100 Hz |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | SA-C-a; `swe-134 7.1 task 2`; `swe-087 7.1 task 4` | `pwm.rs:110-123`; `api/src/pwm/mod.rs:22`; ADR-055 §2 item 2, §3 row C | The PWM output state after a restart that does not reset the PWM block is not a known safe state | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-134 7.1 task 6`; SA-D1 | ADR-055 lines 23, 44, 70; `api/src/pwm/mod.rs:18-19` | The ADR's HZ-005 click argument does not match HZ-005 K4 and K5, and it omits cause C2 | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-062 7.1 task 1`; SA-A4 | SW-05 line 47; INSP-099 CK-CODE-H2 | No independent test of the safety-critical driver exists, and the paired record carries this gap with no finding | Open | Pending | |

#### finding-1

**Major; SA-C-a, `swe-134 7.1 task 2` (SC), `swe-087 7.1 task 4` (SC).** 07 §14.2 row a requires a known safe state "at first start and restarts". It adds: "The same path runs after a watchdog or panic reset". `SW-AUDIO` carries item a ("Audio output starts muted").

`Rp2350Pwm::new` calls `release` (`pwm.rs:110-123`), which does three things:

- it writes the PWM bit to `RESETS.RESET` through the clear alias;
- it polls `RESET_DONE`;
- it writes `EN = 0`.

It never asserts the reset. The driver's starting state is known only when every restart path passes through a PWM block reset first. No product of the stack states or sets the reset scope of a restart: `RESETS.WDSEL` resets to 0 and nothing writes it (S5).

On a restart that leaves PWM out of reset (for example a watchdog or software-requested reset whose scope excludes the PWM block, or a debugger reset), each slice that was running keeps its `CSR.EN`, `CC` and `TOP`. `EN = 0` then freezes its counter, and ADR-055 §3 row C states the consequence: "the output holds whatever level it had, possibly high". Pin `FUNCSEL` is not reset either, because `Rp2350Gpio::new` also only clears. So the sidetone or backlight pin stays at the frozen level, possibly high, from `new` until `attach` reprograms that slice. A slice the new boot never attaches stays that way for good.

This is the software cause HZ-005 C2 names ("Full-scale PWM pattern at start-up or after a fault") and the "DC level held high" that ADR-055 §1 line 23 lists as a click and level cause. PWM-6 (`api/src/pwm/mod.rs:22`) covers only a newly constructed output. The one release test (`release_waits_then_disables_all_slices`) seeds `RESET_DONE` and checks only the clear and the `EN` write. No test and no ADR text covers a warm start.

**Fix:** either of the following:

- In `release`, assert the PWM reset through the set alias before clearing it (the pattern `clocks.rs:282` uses for `PLL_SYS`), so every start begins from the reset state of datasheet §12.5.3 (Tables 1131 to 1135). Add a host test of the set, clear, poll and `EN` order, and add restart to PWM-6 and to the `devcheck-pwm-r1` check.
- Or state in ADR-055 each restart path (power-on, watchdog, software reset, debugger) with the reset scope that returns PWM and `IO_BANK0` to reset, name the product that configures that scope, and test it on the development board.

#### finding-2

**Minor; `swe-134 7.1 task 6` (SC), SA-D1.** ADR-055 claims that option A controls the HZ-005 clicks: "off is a hardware-guaranteed low from the next wrap, with no DC held high and no partial pulse (HZ-005 clicks)" (line 44; also line 23). Section 4.3 (line 70) then records "Hazard analysis update required: no". Neither claim reconciles with the hazard data (S6):

- K4 requires "no DC step at any transition". Off is a constant low (PWM-4, PWM-5). Switching from it to a 50 % square wave moves the mean level of the source by half the supply, which is a DC step at the amplifier input unless the analogue path removes it.
- K5 makes amplifier enable conditional on the source having "idled at mid-scale". A constant-low source is not at mid-scale.
- C2 names a PWM start-up pattern as a software cause. Section 4.3 does not mention it.

Whether the step reaches the ear depends on the audio path, which TS-010 (WP-PDR-25) has not yet decided. So this conclusion is AT RISK on TS-010, and the code needs no change for now. INSP-099 finding-1 raises the onset and envelope half of K4. This finding adds the level half (K4 DC step, K5 mid-scale idle, C2), and both can close in the same ADR-055 revision.

**Fix:** ADR-055 states that PWM-4's constant low is the driver's defined off level and is not itself an HZ-005 click control. It allocates the K4 "no DC step" and the K5 mid-scale idle to `SW-AUDIO` under TS-010, with a revisit condition if TS-010 needs a mid-scale idle from the driver. It cites C2 in section 4.3, tied to finding-1.

#### finding-3

**Minor; `swe-062 7.1 task 1` (SC), SA-A4.** The only test of the contract clauses PWM-1 to PWM-6 is `api/tests/pwm_contract.rs`. It is an author draft (SW-05 line 47), although 07 §3.5 makes it a test-author file. It also runs against reference and faulty models only, because the `Rp2350PwmOut` trait implementation is target-only.

So no test of the safety-critical driver has been written by anyone other than its author. SW-05 records the gap as "Reported to the lead SE". The paired record answers CK-CODE-H2 "No" with the evidence "R5" and raises no finding. The gap therefore has no tracked item that would stop the owner's merge before the test author adopts or replaces the file.

The developer tests themselves run and pass (S1), and their host line coverage is complete apart from one unreachable arm (S2). This finding concerns tracking and independence, not the tests' results.

**Fix:** the lead SE opens a tracked item, such as a finding in INSP-099 iteration 2 or an entry in the WP-PDR-41 sprint record's phase 2 that blocks the merge. The independent test author then adopts the draft against the trait documentation only, or replaces it, before the owner's merge. The adoption is recorded in SW-05.

**INSP-099 findings under the assurance lens.** INSP-099 finding-1 (Major; onset and envelope against REQ-SW-KEYER-033 and HZ-005 K4) stands at Major. It is not raised again here. The assurance lens adds evidence (S7): the closing Bench case TC-SW-KEYER-039 allows "one PWM carrier period", which assumes a carrier. The ADR-055 design has no carrier, so that allowance becomes one tone period, and the case as written would pass an onset of up to 11 ms at 100 Hz. The same one-period latency applies to muting. The `SW-AUDIO` row of 07 §14.2 allocates "a PA fault or SafeState mutes within 10 ms" (items j, l), and `set_enabled(false)` lands at the next wrap, up to 10 ms at 100 Hz before any handler latency. The ADR-055 revision INSP-099 asks for should state both latencies. It should also say whether the safe-state mute uses the PWM output or the K5 amplifier enable. INSP-099 finding-2 (Minor, `module_inception`) is confirmed by S3. The assurance lens does not change its severity.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the code review of a driver of safety-critical components (07 §2.1.1 row "Code") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project's software assurance plan (07 §15) by this review. The NASA-STD-8739.8 part is relieved | `rmm.json` SWE-022 T (the standard is not in the corpus) | none |
| swe-060 7.1 task 1 | | Yes | The code implements ADR-055 §2. `timing` gives `DIV` 53/16 and `TOP` 64 689 at 700 Hz and `DIV` 1 and `TOP` 7 499 at 20 kHz, as the ADR states (INSP-099 C6). The attach order and the slice map match ADR-055 §2 item 2 (`pwm.rs:140-147`, `pwm.rs:52-57`) | | none |
| swe-060 7.1 task 2 | | Yes | No function outside ADR-055 §2: the three `PwmError` variants, `timing`, `cc_value`, `release`, `attach`, `write_cc`, `write_timing` and the trait methods. PWM interrupts are not used | | none |
| swe-061 7.1 task 1 | | Yes | Coding standard 07 §7 (CS-01 to CS-39), `rmm.json` SWE-061 FC In place | | none |
| swe-061 7.1 task 2 | | Yes | Conforms apart from CS-21/CS-27 `module_inception`, which INSP-099 finding-2 carries. CS-36 is met: `SLICE = (N >> 1) & 7` and each slice has its own `CSR.EN` (`pwm.rs:145`) | | none |
| swe-207 7.1 task 1 | | Yes | 07 §7 includes the secure coding practices (`rmm.json` SWE-207 FC In place): no `unsafe` in the package, compile-time bounds, `u64` arithmetic before `try_from`, validated inputs | | none |
| swe-185 7.1 task 1 | | Yes | S3 and a read of the code: no `unsafe`, no numeric `as`, no panic path (`SLICE` asserted at compile time), frequency and duty validated (`timing`, `Duty::from_permille`) | | none |
| swe-135 7.1 task 1 | | Yes | Independent static analysis (S3) and host coverage (S2); complexity from INSP-099 C5 | | none |
| swe-135 7.1 task 2 | SC | Yes | clippy with `-D warnings` and `pedantic` (S3; INSP-099 C4) | | none |
| swe-135 7.1 task 3 | | Yes | The one result (`module_inception`) is carried by INSP-099 finding-2 | | none |
| swe-135 7.1 task 4 | | N/A | No external crate and no manifest change (INSP-099 CK-CODE-A2); the security scan (cargo-audit, cargo-geiger) is CI work planned for CDR | `rmm.json` SWE-135 FC Planned (first CI run for CDR) | none |
| swe-135 7.1 task 5 | SC | Yes | SWE-219 method (07 §9.6) is due at CDR. At this maturity, host line coverage is 100 % for `pwm.rs` and 97.5 % for `pwm/mod.rs`, whose only missed line is an unreachable arm (S2). No waiver is needed | | none |
| swe-135 7.1 task 6 | SC | Yes | Complexity gate PASS; `timing` is the package maximum, below 12 (INSP-099 C5); limit 15 (07 §14.3) | | none |
| swe-135 7.1 task 7 | | Yes | Quality thresholds defined: `-D warnings`, complexity 15 (07 §14.3), CS-38 | | none |
| swe-134 7.1 task 2 | SC | No | Items a to l assessed in section C. Item a fails (finding-1); item j is partial, as INSP-099 finding-1 records | | finding-1 |
| swe-134 7.1 task 3 | SC | N/A | The driver holds no safety-critical loaded data. `DEFAULT_HZ` and the limits are code constants, not loaded items | 07 §9.7 (loaded items are the configuration and calibration record and the image) | none |
| swe-087 7.1 task 4 | SC | No | As swe-134 task 2 | | finding-1 |
| swe-062 7.1 task 1 | SC | No | The 18 developer tests pass (S1). No independent test of the driver exists yet (SW-05 line 47; INSP-099 CK-CODE-H2) | | finding-3 |
| swe-062 7.1 task 2 | | Yes | No unit-test defect is open. The test-author item is tracked by finding-3 | | none |
| swe-219 7.1 task 1 | SC | Yes | Addressed at this maturity: the 07 §9.6 method is `rmm.json` SWE-219 T Planned (MC/DC tables at CDR). The host coverage in S2 is recorded as developer evidence | | none |
| swe-220 7.1 task 1 | SC | Yes | Measured by `tools/complexity_gate.py` (INSP-099 C5) | | none |
| swe-220 7.1 task 2 | SC | Yes | Every package function is below 15; no waiver is needed | | none |
| swe-134 7.1 task 6 | SC | No | ADR-055's HZ-005 claim is inconsistent with K4 and K5, and C2 is not cited | | finding-2 |
| swe-205 7.1 task 1 | SC | Yes | `hazards.json` HZ-005 names the driver's software contributions: C2 (a PWM pattern at start-up or after a fault), C4 (a DC step at transitions) and K4 (onset timing). The drivers inherit through the 07 §14.1 drivers row. The contributions this record finds (the warm-start level, the one-period onset and mute latency) fall under C2, C4 and K4, so no new hazard entry is needed | | none |
| swe-205 7.1 task 4 | SC | Yes | HZ-005 to REQ-SW-KEYER-033 and back, with zero violations (S4) | | none |
| swe-052 7.1 task 1 | | Yes | rustos code carries no CS-24 tags (plan WP-PDR-41: rustos house style). The trace runs through ADR-055 §1 to REQ-SW-KEYER-027, 033, 035 and REQ-SYS-128, and through §4.2 to the design elements | | none |
| swe-052 7.1 task 2 | SC | Yes | HZ-005 and HZ-004 are named in ADR-055 §1, and the report shows the HZ-005 trace (S4) | | none |
| swe-192 7.1 task 1 | SC | Yes | REQ-SW-KEYER-033 has the closing cases TC-SW-KEYER-033 (HostUnit) and 039 (Bench), method Test (S4). The weakness of the 039 criterion is covered under INSP-099 finding-1 above | | none |
| swe-027 7.1 task 1 | | Yes | 07 §17.1 row rustos `pico2` records items a to f. WP-SW-03 adds no crate (INSP-099 CK-CODE-A2) | | none |
| swe-087 7.1 task 1 | | Yes | INSP-099 filed on main (`9d3734c`) with its findings | | none |
| swe-087 7.1 task 2 | | Yes | Iteration 1: no accepted finding is due yet. The iteration 2 delta of both records verifies the fixes | | none |
| swe-088 7.1 task 1 | | Yes | INSP-099 used the code checklist revision B (07 §10.1 row d), answered every item with evidence, stated readiness honestly (`readiness_met: false`, R1, R2, R3, R5) and recorded its participants. The H2 gap is finding-3 | | finding-3 |
| swe-088 7.1 task 2 | | Yes | Both records hold their findings Open with fixes named. None is closed without evidence | | none |
| swe-089 7.1 task 1 | | Yes | Both records carry the 07 §10.3 measurements (size, turns, minutes, findings) | | none |
| swe-080 7.1 task 2 | | Yes | The change is tracked on its own rustos branch, is not merged, and moves the cwht pin only by PCR-4 (plan §6.2). Tests: S1 | | none |
| swe-080 7.1 task 3 | | Yes | The rustos route of ADR-019 is followed (owner merge, OD-23), and the cwht side goes by Class I CR at the merge | | none |
| swe-081 7.1 task 2 | SC | Yes | The product is committed and frozen (rule C2). HZ-005 and the hazard analysis are under git configuration control. `firmware/unsafe-audit.md` is regenerated on the PCR-4 branch | | none |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | Yes | All seventeen blobs equal the INSP-099 list (Product paragraph) |
| R2 | Yes | `code`, 07 §2.1.1 row "Code"; safety-critical, 07 §14.1 drivers row (line 601) |
| R3 | Yes | S4: no validate_docs failure on the product files, and 0 traceability violations for the ids the product touches (HZ-005, REQ-SW-KEYER-027, 033, 035) |
| R4 | Yes | INSP-099 is filed (`9d3734c`) by `reviewer:WP-PDR-41-code`; the author is `author:WP-PDR-41 wave 1a` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 §2.1.1 row "Code", safety-critical Yes; 07 §14.1 line 601 names PWM for the sidetone and audio level |
| SA-A2 | Yes | Three invocations: `author:WP-PDR-41 wave 1a`, `reviewer:WP-PDR-41-code` and this one. INSP-099 names this record's path in `assurance_reviewer_agent` |
| SA-A3 | Yes | Same product string, commit and seventeen blobs |
| SA-A4 | Yes | Code checklist revision B, every item answered with evidence (swe-088 task 1). The unfiled H2 gap is finding-3 |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds every task of the rows `code` and "Every product type", plus the other SWEs named in the front matter comment. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | The two N/A rows (swe-135 task 4, swe-134 task 3) cite `rmm.json` SWE-135 and 07 §9.7. The one SC N/A (swe-134 task 3) has its relief |
| SA-B3 | Yes | Each of the four No task rows is carried by finding-1, 2 or 3; SA-C-a by finding-1 and SA-C-j by INSP-099 finding-1 |

## C. SWE-134 items a to l

The items come from the union of the rows the driver serves (07 §14.2: `SW-AUDIO` a, b, d, g, j, k, l; `SW-KEYER` a to l). A driver has no function of its own for some of them, and those are met by construction or are N/A as stated.

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | No | A cold start is safe: slices are disabled, and a new output is configured with `CC = 0` before `FUNCSEL`, with isolation released last (`pwm.rs:140-147`; PWM-6). A warm start that does not reset PWM is not known safe (finding-1) |
| SA-C-b | Yes | The driver states are unattached, attached-off and attached-on. The only transitions are `attach`, `update_on` and `frequency_on`, and a claimed slice is refused before any write (`pwm.rs:134-137`) |
| SA-C-c | Yes | The driver has no termination path of its own. Off (`set_enabled(false)`) is a defined low from the next wrap (PWM-4). Where the safe-state mute acts is cross item X-2 |
| SA-C-d | N/A | No operator override passes through the driver; the `SW-AUDIO` level unlock is above it (07 §14.2 row d) |
| SA-C-e | N/A | No command sequence in the driver can cause a hazard; the constructor order is enforced by types (`&ClocksReady`, `&Rp2350Gpio`) |
| SA-C-f | N/A | 07 §14.2 row f names the keying, PA-permit and frequency values; the driver's period and duty are not in that list |
| SA-C-g | Yes | Inputs: frequency refused outside the ranges or beyond 0.1 %, and duty bounded by `Duty` (0 to 1000). Output: the achieved frequency is reported (PWM-1). Row g read-back applies to `PA_EN` and `TX_KEY` only |
| SA-C-h | N/A | No safety-critical command in the driver (07 §14.2 row h lists the `PA_EN` prerequisites) |
| SA-C-i | N/A | The sidetone is not an RF path (07 §14.2 row i) |
| SA-C-j | No | Onset and mute latency of up to one tone period (INSP-099 finding-1, with the assurance addition above); counted there, not raised again |
| SA-C-k | Yes | Every refusal is a `PwmError` with state unchanged (PWM-2; `frequency_on` updates `period` only on success). `ResetTimeout` is bounded by `RESET_POLL_BUDGET`. `set_duty` and `set_enabled` cannot fail on the target |
| SA-C-l | Yes | From any state the output can be driven low by `set_enabled(false)` or `Duty::OFF`. Reachability from `safe_state()` is cross item X-2 |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | The SWEHB `swe-205` §7.7.2 considerations that apply are control of hazardous output (audio level and clicks), start-up and restart states, and the stored state of a common peripheral. HZ-005 C2, C4 and K4 cover them. The ADR's mismatch with K4 and K5 is finding-2 |
| SA-D2 | Yes | The 07 §14.1 drivers row names PWM and cites `hazard-analysis.md` §6.2 and the 03 §4.3 drivers row as its source; WP-SW-03 adds no component |
| SA-D3 | Yes | S4: zero `HAZARD_CONTROL_UNTRACED` and zero `HAZARD_INVERSE` |
| SA-D4 | N/A | The product changes no requirement (ADR-055 §4.1) |
| SA-D5 | Yes | REQ-SW-KEYER-033 is closed by Test cases (S4); the 039 criterion is covered under INSP-099 finding-1 |
| SA-D6 | Yes | No hazard-analysis change is required by the code. The ADR text correction is finding-2 |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | Iteration 1: no earlier findings |
| SA-E2 | Yes | Both records carry the measurements |
| SA-E3 | Yes | The rustos change stays on its branch until the owner merges it (ADR-019, OD-23). The cwht pin moves by PCR-4 with `CR:` trailer. ADR-055 and SW-05 were committed on main at `618e441` |
| SA-E4 | N/A | No credit run at this maturity: the dev-board report is `credit: false` and not yet run (SW-05 phase 5) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No concern outside the findings. The TS-010 dependence of finding-2 is an AT RISK product dependence (rule C8), not a new risk, and falls under RSK-013 (minimal keyer set) |
| SA-F2 | Yes | Front matter: 1 Major, 2 Minor, 6 items No (4 tasks, SA-C-a, SA-C-j), 32 turns, 60 minutes |
| SA-F3 | Yes | This record alone gives the verdict, the open findings, the tasks applied and the reliefs used (swe-022 task 1 part, swe-135 task 4, swe-134 task 3) |

## Completion criteria and verdict

The verdict is `assurance_verdict: NEEDS CHANGES`, with one open Major of this record (finding-1) and the INSP-099 finding-1 Major that the assurance lens confirms. The completion criteria are not met: zero open Major findings is required. Iteration 2 is a delta that verifies finding-1 and INSP-099 finding-1 at the new rustos blobs (rule C1). Findings 2 and 3 are Minor. Unless they are fixed before the merge, they become liens due at the CDR readiness declaration after the first APPROVED verdict. `verdict` stays NEEDS CHANGES under the lead SE convention until both records are APPROVED and the blobs reach a configuration cwht consumes.

## Cross items (returned to Claude)

| # | Item |
|---|---|
| X-1 | INSP-099 should add `paired_record: INSP-105`, name this reviewer in `assurance_reviewer_agent` and copy `assurance_verdict: NEEDS CHANGES`. Its reviewer updates it (07 §10.2) |
| X-2 | Firmware architecture (WP-PDR-32) and `SW-AUDIO`: say whether the 07 §14.2 row c and l "audio muted" of `safe_state()` goes through the PWM output (which needs access to the owned `Rp2350PwmOut` from a panic or fault handler) or through the HZ-005 K5 amplifier enable. The driver offers no context-free way to force its pin low |
| X-3 | TC-SW-KEYER-039 criterion "one PWM carrier period": the test author should reconcile it with the ADR-055 design, which has no carrier (S7). This input goes to the INSP-099 finding-1 fix |
| X-4 | 07 §17.1 row rustos `api` states "No `LICENSE` file" at `c54d35a`, but a `LICENSE` file is present at `6df18af` (seen in the scratch worktree). Refresh the row at the PCR-4 pin move (OQ-SW-001) |
| X-5 | The same `release`-only pattern is in `Rp2350Gpio::new` (pre-existing rustos code, not this product) and possibly in the TIMER0 driver. The finding-1 restart question applies to the whole stack, so the sibling SA records of INSP-095 to INSP-098 should check it |

## Verdict format

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: rustos cwht/wp-sw-03 api/src/pwm/mod.rs@1c13d0ad, firmware/pico2/src/pwm/pwm.rs@75bca4e8, firmware/pico2/src/pwm/mod.rs@9c8ed4c4 (and 14 more, as INSP-099) at 6df18af; PAIRED RECORD: INSP-099
PRODUCT TYPE: code; CRITICALITY: safety-critical
FINDINGS:
- [Major] finding-1 SA-C-a, swe-134 7.1 task 2: release does not assert the PWM reset, so a warm start leaves slices frozen at their last level on PWM-function pins (HZ-005 C2).
- [Minor] finding-2 swe-134 7.1 task 6: ADR-055 HZ-005 click argument does not match K4 (no DC step) and K5 (mid-scale idle); C2 not cited.
- [Minor] finding-3 swe-062 7.1 task 1: no independent test of the driver; INSP-099 H2 No carries no finding.
- (confirmed, not raised again) INSP-099 finding-1 Major: onset and mute latency up to one tone period; TC-SW-KEYER-039 criterion assumes a carrier.
TASKS APPLIED: 36 (front matter assurance_tasks_applied)
TASKS N/A (relief): swe-135 7.1 task 4 (rmm.json SWE-135 FC Planned), swe-134 7.1 task 3 (07 section 9.7), swe-022 7.1 task 1 NASA-STD-8739.8 part (rmm.json SWE-022 T)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l
MEASUREMENTS: size=about 470 non-test Rust lines, 17 files; tasks=38; tasks_no=4; turns=32; minutes=60; major=1; minor=2
```

## Iteration 2: assurance delta at rustos `48e07ec` (2026-09-27, cwht HEAD `ae29a98`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fix of finding-1 (Major) only. Findings 2 and 3 (Minor) were not addressed by the author (ADR-055 section 8, SW-05 "Phase 1, revision 2") and are not re-reviewed. INSP-099 finding-1 (Major, concurred at iteration 1) belongs to INSP-099, whose iteration 2 records it Verified; this delta reads its hunks only under the assurance lens (SA-C-j). Product: rustos `cwht/wp-sw-03` at `48e07ec` (`git rev-parse cwht/wp-sw-03` equals it), parent `9df9c57`, which merges `cwht/wp-sw-02` at `38434b2` into the iteration 1 head `6df18af`. The package delta is `git diff 9df9c57 48e07ec`: `api/src/pwm/mod.rs`, `docs/icd/rp2350/pwm/01_overview.md`, `pwm/pwm.rs` and `pwm/pwm_tests.rs`, 116 insertions and 23 deletions. `lib.rs` (`5122df42` to `46107a9e`) changes only through the merge (the INSP-096 vector move), which INSP-102 reviews. ADR-055 `7b2a9d92` to `c2c7cc99` and SW-05 `975d9268` to `d904d7de` (revision 2, `e3ce2cb`); the sprint index `fb217bcb` to `7ae0cbcc` is the FW-B1 row move INSP-104 read. Checklist as at iteration 1.

**Independence (rule C4).** Same role as iteration 1. This invocation authored no part of revision 2, the rustos fix commit or INSP-099, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: "software assurance record iteration 2 delta verification of Major fix, product_files updated, finding Verified"). Afterwards `grep` was used only on known paths and `git grep` on committed rustos objects. **rustos.** The owner's working tree was not read or changed. All runs used a detached scratch worktree of `48e07ec` (`git worktree add --detach` under the session scratchpad) with a scratch `CARGO_TARGET_DIR`. Every mutant was reverted with `git checkout -- .`; `git status --short` was empty before `git worktree remove`, and the target directory was deleted. No branch was created, nothing was pushed or merged, every `cargo` run was `--offline` with `RUSTUP_AUTO_INSTALL=0`, and nothing was downloaded. LTspice was not run.

### Assurance re-runs and checks, iteration 2

| # | Check | Result |
|---|---|---|
| T0 | Blob identities: `git -C rustos rev-parse 48e07ec:<path>` for the fourteen rustos entries; `git rev-parse HEAD:<path>` and `git hash-object <path>` for the three cwht entries | All seventeen equal the brief's list and INSP-099 iteration 2 (front matter `product_files`) |
| T1 | `cargo +1.98.0 test --offline -p pico2 pwm`; `-p api --test pwm_contract`; `-p pico2` | 20 passed; 5 passed; 101 passed; none failed. Agrees with SW-05 revision 2 and ADR-055 section 4.3 |
| T2 | Mutants of `release` (`pwm.rs:124-138`), each against `cargo test -p pico2 pwm` and reverted: M1 set-alias write removed; M2 set and clear swapped; M3 set moved after the `RESET_DONE` poll; M4 set of bit 6 instead of 16; M5 set as a plain write to `RESET` | All five killed, each by both new tests (`release_resets_then_releases_waits_and_disables_all_slices`, `release_from_a_restart_that_left_pwm_running_starts_from_reset`) |
| T3 | `cargo +1.98.0 clippy --offline -p pico2 --all-targets -- -W clippy::pedantic`; `cargo +1.98.0 build --offline -p pico2 --target thumbv8m.main-none-eabihf` | Only `module_inception` at `pwm/mod.rs:29` in the package files (INSP-099 finding-2, unchanged). Target build without warning |
| T4 | Datasheet anchors of the fix, read in the PWM ICD at `48e07ec` | `02_registers.md:7-8`: the `+0x2000` set and `+0x3000` clear aliases of section 2.1.3; `reg.rs:129` `ALIAS_SET = 0x2000`. Tables 1131 to 1135: `CSR.EN` 0, `CTR` 0, `CC` 0, `TOP` 0xffff at reset. `reset.rs:34`: `RESETS` bit 16 is `PWM`, equal to `RESET_BIT_PWM` (`pwm/mod.rs:63`) |
| T5 | Boot path of the stack at `48e07ec`: `git grep "RESET_OFFSET + ALIAS_SET"` over `firmware`; `Rp2350Pwm::new` signature (`pwm.rs:82-91`) and the clock bring-up table (`clocks.rs:20-28`) | The PWM reset is asserted only in `release`, called only from `Rp2350Pwm::new`, which needs `&ClocksReady`. Clock bring-up runs first: crystal start, `clk_sys` moved to `clk_ref`, PLL, and a 1 ms frequency-counter measurement (step 10). No earlier boot code resets PWM (finding-4) |

### Hunk reading of the fix

- **`pwm.rs` `75bca4e8` to `92b634e1`, `release`.** One line added: `regs.write(RegAddr::RESET, RESET_OFFSET + ALIAS_SET, RESET_BIT_PWM)` before the existing clear, poll and `EN = 0`, with the `ALIAS_SET` import. The doc comment names HZ-005 C2 and this finding. The poll waits for `RESET_DONE` bit 16 after the clear, so the release is complete before `EN` is written (T2 M3 shows the order is tested). On hardware, the assert returns every slice register to its reset value (T4), so `CSR.EN = 0` and `CC = 0`, and a PWM-function pin is driven low. The module note is updated to the same effect. The other hunks of this file (`update_on`, `CTR = TOP`) are the INSP-099 finding-1 fix.
- **`pwm_tests.rs` `c3286c6d` to `82d96ce9`.** The release test now checks the writes (set, clear, `EN`) and the full access order through `FakeRegs::log()` (set, clear, `RESET_DONE` read, `EN`). The warm-start test seeds `RESET` as out of reset and checks that the first write is the set alias. `FakeRegs` does not model the reset side effect on the slice registers, so this test shows the assert is issued even when PWM is already released, not that the slices return to reset. That is the limit of a host test, and the dev-board restart case (ADR-055 section 4.3) is the evidence for the hardware effect. Both tests kill every T2 mutant.
- **`api/src/pwm/mod.rs` `1c13d0ad` to `b859f370`.** PWM-6 reads "A newly constructed output is disabled (low), after a power-on start and after a restart alike." The claim holds for a newly constructed output. The PWM-4 hunk is the INSP-099 finding-1 fix.
- **`01_overview.md` `346e561d` to `98ae5870`.** Bring-up step 1 now sets bit 16 through `+0x2000`, clears it through `+0x3000`, waits for `RESET_DONE`, then writes `EN = 0`. This equals the code. Step 5 (on and off) is the INSP-099 finding-1 fix.
- **ADR-055 `7b2a9d92` to `c2c7cc99`.** Section 2 item 2 describes the reset-first release and cites section 12.5.3, Tables 1131 to 1135. Section 4.3 claims SWE-134 item a ("known state at first start and at restarts") and states the driver's share of HZ-005 C2. The dev-board check gains a restart case: the tone is left running, then a watchdog reset whose scope excludes PWM (and a debugger reset), and the PWM pin is to read low "from the new boot until its output is attached". Section 8 records the revision. That last criterion is not what the design gives (finding-4).
- **SW-05 `975d9268` to `d904d7de`.** "Phase 1, revision 2" lists this fix and its files. The evidence it states (101 host tests) is reproduced by T1.

### Verification of finding-1 (Major), element by element (rule C7)

| Element of the iteration 1 fix (first option) | Evidence | Result |
|---|---|---|
| `release` asserts the PWM reset through the set alias before clearing it | `pwm.rs:125-126`; T4 alias and bit | Verified |
| Every start begins from the section 12.5.3 reset state | T4 reset values; ICD step 1 equals the code; a slice the new boot never attaches is now stopped at `CC = 0` instead of frozen at its last level | Verified from `Rp2350Pwm::new` onward. The interval from the restart to `new` is finding-4 (Minor) |
| Host test of the set, clear, poll and `EN` order | `release_resets_then_releases_waits_and_disables_all_slices`; T2 kills M1 to M5 | Verified |
| Restart added to PWM-6 | `api/src/pwm/mod.rs` PWM-6 | Verified |
| Restart added to the `devcheck-pwm-r1` check | ADR-055 section 4.3 "Added at revision 2" restart case | Verified as a planned check. Its pass criterion is corrected under finding-4 |
| ADR text (section 2 item 2, section 3 row C consequence) | Section 2 item 2 revised. Row C still describes clearing `CSR.EN` as the rejected off method, which remains true and is no longer the start state | Verified |

finding-1 is **Verified** at `48e07ec`. The concern of iteration 1, a slice left running or frozen high by an earlier image for the whole of the new boot, cannot occur after `Rp2350Pwm::new`. It does not depend on the reset scope of the restart or on `RESETS.WDSEL`.

### INSP-099 finding-1 under the assurance lens (concurrence, not re-raised)

ADR-055 section 2.1 now states the latency of every operation. On and off take at most one count, 1.71 µs at 150 MHz, at any frequency. Duty and frequency changes take up to one tone period. This answers the iteration 1 assurance addition (S7): mute latency is 1.71 µs, which leaves the 10 ms `SW-AUDIO` budget of items j and l to the handler path. Whether the safe-state mute goes through the PWM output or the K5 amplifier enable is allocated to WP-PDR-32 and WP-PDR-36 (cross item X-2 stands). The TC-SW-KEYER-039 carrier term is reported to WP-PDR-35 (X-3 stands). The forced-wrap click argument (a period cut short once, no level held) is consistent with HZ-005 K4 as far as a two-level driver can be. The envelope and the DC step are allocated to `SW-AUDIO` under TS-010, AT RISK. SA-C-j is Yes. This concurs with INSP-099 iteration 2 (Verified).

### Task table, rows re-answered at iteration 2

Rows not listed stand as at iteration 1. The delta adds no `unsafe`, no dependency, and no requirement or hazard link.

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 2 | SC | Yes | Item a holds from `Rp2350Pwm::new` on (finding-1 Verified). Item j holds for the driver's share (INSP-099 finding-1 Verified; concurrence above). The boot window before `new` is finding-4 | | finding-4 |
| swe-087 7.1 task 4 | SC | Yes | As swe-134 task 2 | | finding-4 |
| swe-087 7.1 task 2 | | Yes | finding-1 Verified with evidence (T1 to T4 and the element table). Findings 2 and 3 are carried as liens with their fixes named | | none |
| swe-062 7.1 task 1 | SC | No | T1 passes, and T2 shows the new tests guard the fix. The contract test is still the author's draft, with no independent test (finding-3, not addressed) | | finding-3 |
| swe-134 7.1 task 6 | SC | No | Not re-reviewed (rule C1). ADR-055 section 2.1 now states the level allocation (K4 DC step, K5 mid-scale idle to `SW-AUDIO`) and section 4.3 cites C2, so finding-2 appears to be largely addressed. Its closure is for the next delta | | finding-2 |
| swe-205 7.1 task 1 | SC | Yes | The boot window of finding-4 is a remaining part of HZ-005 C2 ("a full-scale PWM pattern at start-up"). No new hazard, cause or control is needed | | finding-4 |
| swe-135 7.1 task 3 | | Yes | T3: no new lint result in the package | | none |
| swe-220 7.1 task 1 and task 2 | SC | Yes | `release` gains one straight-line write (CC unchanged). SW-05 revision 2 reports `complexity_gate.py --max 15` PASS, max CC 12 | | none |
| SA-C-a | SC | Yes | Known safe state from `Rp2350Pwm::new` at every start, power-on or restart (finding-1 Verified). The window from the restart to `new` is finding-4 (Minor) | | finding-4 |
| SA-C-j | SC | Yes | On and off within one count (≤ 1.71 µs); duty at the next period (ADR-055 section 2.1; INSP-099 iteration 2) | | none |
| SA-A3 | | Yes | Same `product_commit` `48e07ec` and the same seventeen blobs as INSP-099 iteration 2 (T0) | | none |
| SA-E1 | | Yes | Earlier reviews: iteration 1 of this record and of INSP-099. finding-1 is verified above | | none |
| SA-F3 | | Yes | For the package's "Software assurance findings" section: assurance APPROVED at iteration 2, 0 Major open, 3 Minor liens (findings 2, 3 and 4) due at the CDR readiness declaration | | finding-2, finding-3, finding-4 |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | assurance | Major | SA-C-a; `swe-134 7.1 task 2`; `swe-087 7.1 task 4` | `pwm.rs:124-138` (`92b634e1`); `api/src/pwm/mod.rs` PWM-6 (`b859f370`); ADR-055 section 2 item 2 (`c2c7cc99`) | The PWM output state after a restart that does not reset the PWM block was not a known safe state. Fixed by the reset-first `release` (element table above) | Verified | | |
| finding-2 | assurance | Minor | `swe-134 7.1 task 6`; SA-D1 | ADR-055 section 2.1 and section 4.3 | As at iteration 1. Not re-reviewed (rule C1). Revision 2 text appears to address it; the next delta verifies it | Open (lien, rule C1) | Pending | CDR readiness declaration |
| finding-3 | assurance | Minor | `swe-062 7.1 task 1`; SA-A4 | SW-05 phase 2; INSP-099 CK-CODE-H2 | As at iteration 1: no independent test of the driver and no tracked item that blocks the merge. Not addressed (rule C1) | Open (lien, rule C1) | Pending | CDR readiness declaration |
| <a id="finding-4"></a>finding-4 | assurance | Minor | SA-C-a; `swe-205 7.1 task 1`; `swe-134 7.1 task 2` | ADR-055 section 4.3 dev-board restart case and section 2 item 2 (`c2c7cc99`); `pwm.rs` module note and `Rp2350Pwm::new` (`92b634e1`, `:82-91`); PWM ICD bring-up step 1 (`98ae5870`) | The reset-first `release` makes the state known from `Rp2350Pwm::new` onward, but not "from the new boot". `new` needs `&ClocksReady`, so it runs after clock bring-up (T5: crystal start, `clk_sys` moved to `clk_ref` and back, a 1 ms frequency measurement). No earlier boot code resets PWM. After a restart whose scope excludes PWM, each slice the earlier image left running keeps running through this window, at a pitch that follows `clk_sys` (roughly a tenth of the tone frequency while `clk_sys` runs from `clk_ref`), and a slice left at `CC = TOP + 1` holds a DC high. This is a remaining part of HZ-005 C2. The ADR-055 restart criterion "the PWM pin read low from the new boot until its output is attached" cannot pass as written, and neither the ADR nor the ICD states the window. Minor: the window is bounded (milliseconds, ended by `new`), the level is the earlier image's normal output, and the hardware amplifier enable of K5 is the independent control for it | Open (lien, rule C1) | Pending | CDR readiness declaration |

**finding-4 fix.** Choose one:

- State the window in ADR-055 section 2 item 2 and section 4.3 and in the PWM ICD: from the restart to `Rp2350Pwm::new`, bounded by the clock bring-up time. Change the dev-board restart criterion to "low from `Rp2350Pwm::new` until the output is attached, and the window from the restart to `new` measured and recorded". Name `SW-AUDIO` (the K5 amplifier enable, which must be de-asserted over a restart) as the control for the window, as a cross item to WP-PDR-32 and WP-PDR-36.
- Or reset PWM (and the other output blocks, as cross item X-5) in the earliest boot code, before clock bring-up, so the pin is low from the new boot, and keep the criterion.

### Cross items, iteration 2

| # | Item |
|---|---|
| X-6 | INSP-099 reads `assurance_verdict: pending`. Its reviewer updates it to APPROVED from this delta (07 section 10.2) |
| X-7 | WP-PDR-32 and WP-PDR-36 (`SW-AUDIO`, `ICD-CTL-PHONES` section 3.2.6): whether the K5 amplifier enable is a GPIO that a restart outside the `IO_BANK0` reset scope leaves asserted, which would remove the independent control for the finding-4 window. The same `release`-only pattern is in `Rp2350Gpio::new` (X-5) |

### Commands run, iteration 2

| Command | Result |
|---|---|
| `git -C /Users/robinonsay/rust/rustos rev-parse cwht/wp-sw-03`; `rev-parse 48e07ec:<path>` (14); `git rev-parse HEAD:<path>` and `git hash-object` (3) | T0 |
| `git -C /Users/robinonsay/rust/rustos diff 6df18af 48e07ec -- firmware/pico2/src/pwm api/src/pwm docs/icd/rp2350/pwm`; `diff --stat 9df9c57 48e07ec`; `git diff <old> <new>` for ADR-055 and SW-05 | every hunk of the package read (above) |
| `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa03-it2 48e07ec`, then `worktree remove` | T1 to T4; clean; removed; target directory deleted |
| `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` | this record PASS. Overall exit 1: 102 passed, 8 failed, 110 checked; the 8 failures are other records, none in this record's scope |

### Measurements (SWE-089), iteration 2

Lines reviewed: the 139 changed lines of `9df9c57..48e07ec` in the four package files, about 35 changed lines of ADR-055 and 12 of SW-05. Unsafe sites added: 0. Mutants: 5, all killed. Findings: finding-1 (Major) Verified; 1 new Minor (finding-4); findings 2 and 3 carried. Effort of this iteration: about 24 turns and 45 minutes (the front matter totals include iteration 1).

### Record verdict, iteration 2

`assurance_verdict: APPROVED` and `reviewer_verdict: APPROVED`. finding-1 (Major) is Verified at `48e07ec`, and the concurred INSP-099 finding-1 is Verified by INSP-099 iteration 2. No Major is open. Findings 2, 3 and 4 (Minor) become liens under rule C1: the owner is the firmware developer (finding-3 with the SW-05 phase 2 test author), due at the CDR readiness declaration. `verdict` stays `NEEDS CHANGES` under the lead SE convention of 2026-09-27. The fourteen rustos blobs exist only on the unmerged branch `cwht/wp-sw-03`, and the checklist applied exists only on `cr/CR-012-pdr-checklist-templates`. The software lead sets `verdict` in the commit that brings `48e07ec` into a configuration cwht consumes (the owner's merge and the PCR-4 pin-move CR), or in the commit right after it.

```
ASSURANCE VERDICT (iteration 2, 2026-09-27): APPROVED (liens finding-2, finding-3, finding-4); record verdict NEEDS CHANGES (held, lead SE convention)
PRODUCT: rustos cwht/wp-sw-03 at 48e07ec (pwm.rs@92b634e1, pwm_tests.rs@82d96ce9, api pwm@b859f370, 01_overview.md@98ae5870, and 13 more as front matter); ADR-055@c2c7cc99, SW-05@d904d7de; PAIRED RECORD: INSP-099
FINDINGS:
- [Major] finding-1 Verified (reset asserted through the set alias before release; order tested; PWM-6 covers restarts; dev-board restart case planned)
- [Minor] finding-2 Open (lien), not re-reviewed
- [Minor] finding-3 Open (lien), not addressed
- [Minor] finding-4 Open (lien), new: the window from restart to Rp2350Pwm::new (clock bring-up) is unstated, and the dev-board criterion "low from the new boot" cannot pass
- (concurred) INSP-099 finding-1 Verified by INSP-099 iteration 2
MEASUREMENTS: lines=139 code+doc, about 47 cwht; mutants=5 (5 killed); iteration 2 turns=24, minutes=45; cumulative turns=56, minutes=105
```
