---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the code review INSP-098
# (docs/reviews/PDR/checklists/code-wp-sw-02.md, iteration 1 by reviewer:WP-PDR-41-code), at the path INSP-098
# names in assurance_reviewer_agent and PDR work plan WP-PDR-41 "Records" names (code-wp-sw-<nn>.md and
# -software-assurance.md per WP).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged,
# git merge-base --is-ancestor false on 2026-09-27). The `checklist` field names peer-review-checklist-code
# revision B, the checklist INSP-098 names, because tools/validate_docs.py fails a record whose `checklist` names a
# template absent from main, and the lead SE convention of 2026-09-27 does not change the validator.
# `assurance_checklist` names the template actually applied (the form of INSP-048, INSP-049, INSP-051, INSP-070).
# id: no id was assigned in the brief. INSP-095 to INSP-099 are the five WP-PDR-41 code reviews in the order
# WP-SW-11, 09, 01, 02, 03 and INSP-100 is taken (WP-PDR-09); this record takes INSP-104, the fourth of 101 to 105
# in the same order, leaving 101 to 103 and 105 to the sibling assurance pairs. Checked free on main, on every
# local branch and in the working tree at commit time.
id: INSP-104
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-02-software-assurance.md
product: "rustos cwht/wp-sw-02: api/src/gpio/mod.rs (InputLevels, InputSnapshot), firmware/pico2/src/gpio/snapshot.rs and the input tracking in firmware/pico2/src/gpio/gpio.rs (WP-SW-02)"
# product_commit and product_files (iteration 2): equal to INSP-098 iteration 2 (readiness R1; rule C2). rustos
# cwht/wp-sw-02 at 38434b2 (the finding-1 fix on the merge 5d4637f of cwht/wp-sw-01 58fe739 into f85a190); the five
# rustos: blobs equal git -C rustos rev-parse 38434b2:<path> and exist only on the unmerged branches cwht/wp-sw-02 and
# cwht/wp-sw-03; the three cwht blobs equal git rev-parse HEAD:<path> and git hash-object at HEAD 0be8bab (2026-09-27).
# Drift from iteration 1: ADR-054, SW-04, the sprint index, gpio/gpio.rs and gpio/snapshot.rs; the other three blobs
# are unchanged
product_commit: "38434b26dd74ebf288a63eff42331d73913e6087"
product_files: ["docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md@ae2afdd838fb08909d88e727c7bb6b6dce509dc8", "docs/sprints/SW-04-wp-sw-02-sio-snapshot.md@a79d4d99185c92aa7ddff700b570e5a8e4a27884", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:api/src/gpio/mod.rs@f0250c93e08856270a702324b19fda0b04e9199b", "rustos:api/tests/gpio_snapshot_contract.rs@0918c1933350c2b159924d480a1738768f4b34c2", "rustos:firmware/pico2/src/gpio/gpio.rs@cdb5fc92052e74727106486163d3965454538979", "rustos:firmware/pico2/src/gpio/mod.rs@d71011bf3934812b52eaac6fa3ccebaae0067a41", "rustos:firmware/pico2/src/gpio/snapshot.rs@00e2c30105014dc7d970e0b45491e5bd84ebe6e3"]
product_files_iteration_1: ["docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md@848102d2dac6d026a4718ae1fd57eb5f270c8245", "docs/sprints/SW-04-wp-sw-02-sio-snapshot.md@1686ecc09144d6ef16644522eff1cd0fb65f3584", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/gpio/mod.rs@f0250c93e08856270a702324b19fda0b04e9199b", "rustos:api/tests/gpio_snapshot_contract.rs@0918c1933350c2b159924d480a1738768f4b34c2", "rustos:firmware/pico2/src/gpio/gpio.rs@d7ea7a706b4131e5625aac2755845882c172e807", "rustos:firmware/pico2/src/gpio/mod.rs@d71011bf3934812b52eaac6fa3ccebaae0067a41", "rustos:firmware/pico2/src/gpio/snapshot.rs@6b5ddac5ff90032bf07c9ba9fac4f4fa96378a5b"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/code-wp-sw-02.md (INSP-098 iteration 1, main 9d3734c; iteration 2, main 134e555)", "docs/safety/hazards.json (HZ-004, HZ-010)", "docs/icd/ICD-CTL-KEY.md (section 3.2.5)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 3.5, 9.5, 9.6, 14.1, 14.2, 14.3, 15, 19)", "docs/process/03-software-classification-and-rmm.md (section 4.3 drivers row, section 5)", "docs/process/05-configuration-and-data-management.md (Table 4-1 rows 13 and 44)", "docs/plan/pdr-work-plan.md (sections 3.8, 5)", "rustos:firmware/pico2/src/gpio/gpio.rs configure_gpio_pin_in at f85a190 (pre-existing, not in the change)", "rustos:firmware/pico2/src/gpio/gpio.rs new_input at 38434b2 (pre-existing, not in the change)", "docs/plan/pdr-work-plan.md (rule C1, L1)"]
paired_record: INSP-098
# product_type: code (07 section 2.1.1 row "code": every file of a safety-critical component). Task set applied:
# the section B rows "Every product type" and "code"; the section 7.1 tasks of the SWEs the product cites or
# serves (SWE-134 items g and i and SWE-219, ADR-054 section 1 "Guidance consulted"; SWE-205, SWE-052, SWE-192,
# SWE-184 through section D; SWE-080, SWE-081, SWE-187 and SWE-087 to SWE-089 through section E)
product_type: code
# criticality: safety-critical by inheritance, 07 section 14.1 drivers row "GPIO (SIO)" (pico2 WP-SW-02), serving
# the keyer and keying output (HZ-004, HZ-010); 03 section 4.3 drivers row; hazard-analysis.md section 7 drivers row
criticality: safety-critical
product_size: "409 lines added and 3 removed in f85a190, about 185 non-test lines (api gpio 72, snapshot.rs 69 before its test module, gpio.rs 37 changed, gpio/mod.rs 1); 174-line contract test draft; ADR-054 86 lines; SW-04 60 lines. Iteration 2 delta: 5d4637f..38434b2, 70 insertions and 52 deletions in gpio/gpio.rs and gpio/snapshot.rs; 29 changed lines in ADR-054, SW-04 and the sprint index"
sprint: SW-04-wp-sw-02-sio-snapshot
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-02"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-02 (software assurance function, iterations 1 and 2; paired file review INSP-098 by reviewer:WP-PDR-41-code)"
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 2 (rule C1). Iteration 1 was NEEDS CHANGES only on
# the concurred INSP-098 finding-1 (CS-18, Major); iteration 2 verifies that fix under the assurance lens at 38434b2
# (INSP-098 iteration 2 records it Verified). No Major is open. finding-1 (Minor, iteration 1) is unaddressed by
# revision 2 and finding-2 (Minor, new at iteration 2 on the moved lines) is raised; both become liens under rule C1
# (plan L1), owner the firmware developer (finding-2 (b) with the SW-04 phase 2 test author), due at the CDR readiness
# declaration
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: at iteration 1 both reviews were
# NEEDS CHANGES; at iteration 2 both are APPROVED, and the hold remains because INSP-098 readiness R3 and R5 do not hold
# and the five rustos blobs exist only on the unmerged rustos branch cwht/wp-sw-02 and the checklist applied
# only on cr/CR-012-pdr-checklist-templates (lead SE convention of 2026-09-27). INSP-098 names this record since its
# iteration 2 (paired_record INSP-104) and carries assurance_verdict pending until this delta is filed; each reviewer
# updates only its own record.
# The software lead sets verdict in the commit that brings the blobs to a configuration cwht consumes (the owner's
# merge and the PCR-4 pin-move CR), or the commit right after it
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 2
findings_open: 2
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 2
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 3", "swe-135 7.1 task 5", "swe-135 7.1 task 6", "swe-134 7.1 task 2", "swe-087 7.1 task 4", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 4", "swe-052 7.1 task 2", "swe-192 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 3", "swe-081 7.1 task 2", "swe-187 7.1 task 1", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: [a, e, f, g, h, i, j, k]
deferred_rids: []
items_no: ["swe-061 7.1 task 2", "swe-062 7.1 task 1", "swe-219 7.1 task 1", SA-D1]
effort_turns: 57
effort_minutes: 105
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-104: software assurance pair of INSP-098, code review of WP-SW-02 SIO input snapshot (rustos `cwht/wp-sw-02` at `f85a190`, WP-PDR-41)

**Product.** rustos branch `cwht/wp-sw-02` at `f85a190` (parent `cwht/wp-sw-01` `a1cd160`), the five `rustos:` blobs of `product_files`, with ADR-054, SW-04 and the sprint index at cwht `main`. Identity checked with `git -C /Users/robinonsay/rust/rustos rev-parse f85a190:<path>` and `git rev-parse HEAD:<path>` (and `618e441:<path>`) on 2026-09-27: all eight equal INSP-098. The branch head has not moved (`git rev-parse cwht/wp-sw-02` = `f85a190`).

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Sections R, A, B, C, D, E and F are applied. `product_type` code; `criticality` safety-critical (inherited, 07 section 14.1 drivers row).

**Acceptance criteria (rule C7).** Every task of the section B rows "Every product type" and "code"; the section 7.1 tasks of every other SWE the product implements or serves (front matter comment); each SWE-134 item a to l that the drivers row inherits from `SW-KEYER` (07 section 14.2), answered for this driver's role; the product's contract clauses SNP-1 to SNP-4; the three mask cases (empty, stray, accepted) and the safety meaning of the mask check; the HZ-004 and HZ-010 software causes the input path touches (HZ-010 C6 and C7, HZ-004 C8); the three INSP-098 findings re-read under the assurance lens.

**Independence (rule C4).** This invocation (`sa-reviewer:WP-PDR-41-code-wp-sw-02`) authored no part of WP-PDR-41, ADR-054, SW-04 or the rustos commits, wrote no part of INSP-098, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "software assurance peer review record code WP-SW software-assurance.md assurance_tasks_applied"; "WP-PDR-41 RSK-013 minimal keyer set WP-SW-02 SIO snapshot records software assurance"; "07 section 14.2 SWE-134 items applied per module drivers pico2 GPIO SIO safety-critical inheritance"; "key paddle input active low pull-up contact to ground GPIO dit dah level closed"). `grep -n`, `awk` over the SWEHB pages and `git grep` on rustos objects were used afterwards only to pin lines and extract the section 7.1 task lists. **rustos.** The owner's rustos working tree was not read or changed. All builds ran in a detached scratch worktree of `f85a190` created from the rustos repository with `git worktree add --detach` under the session scratchpad (no branch created; a review needs no commit), with a scratch `CARGO_TARGET_DIR`; the worktree and the target directories were removed afterwards and the worktree was clean (`git status --short` empty) before removal. Nothing was pushed or merged. No download or install; every `cargo` run was `--offline`. LTspice was not run.

**Lead SE convention.** The five rustos blobs exist only on the unmerged rustos branch `cwht/wp-sw-02`, and the checklist applied only on `cr/CR-012-pdr-checklist-templates`. This record sets `reviewer_verdict` and `assurance_verdict` on its own, holds `verdict`, and is committed on `main`.

## Assurance re-runs and checks

| # | Check | Result |
|---|---|---|
| S0 | Blob identities, rustos `git rev-parse f85a190:<path>` for the five rustos entries; cwht `git rev-parse HEAD:<path>` and `618e441:<path>` for the three cwht entries | all eight equal INSP-098 `product_files` |
| S1 | `cargo test --offline -p pico2` and `cargo test --offline -p api --test gpio_snapshot_contract` in the worktree | pico2 77 passed (the 6 `gpio::snapshot::tests` among them); contract 5 passed; none failed. Equal to INSP-098 C1 |
| S2 | Independent static analysis: `cargo clippy --offline -p pico2 -p api --all-targets -- -W clippy::pedantic`, locations filtered to the product files and compared with the lines `f85a190` adds or changes | on added or changed lines only `gpio.rs:156` and `gpio.rs:195` (`needless_return`); nothing in `snapshot.rs`, in the new lines of `api/src/gpio/mod.rs` or in the contract test. The other `gpio.rs` and `api/src/gpio/mod.rs` hits are on pre-existing lines. Agrees with INSP-098 C4 and finding-2 |
| S3 | Host line and region coverage, `cargo llvm-cov --offline -p pico2 -p api` (stable, `cargo-llvm-cov 0.9.1`; developer evidence, not the MSR-13 credit run of 07 section 9.6) | `api/src/gpio/mod.rs` 100 % lines and regions (15 of 15 lines). `pico2/src/gpio/snapshot.rs` 86.96 % lines, 91.86 % regions: `check_snapshot_mask` and `read_inputs` fully covered; not executed are `Rp2350InputSnapshot::new` (`:29-31`) and `mask` (`:35-37`), reached only from `Rp2350Gpio::input_snapshot`. `pico2/src/gpio/gpio.rs` 0 % on the host (88 lines): `Rp2350Gpio::new` releases resets through MMIO, so `input_from_handle`, the `inputs` record and `input_snapshot` are target-only (07 section 9.5 disposition; 07 line 31) |
| S4 | Decision inventory and MC/DC independence pairs (07 section 9.6 items 1 and 2; CS-38) | Two new boolean decisions. `check_snapshot_mask` (`snapshot.rs:43-46`): `requested == 0 \|\| stray != 0`; pairs empty against accepted (c1) and stray against accepted (c2) are the tests `empty_mask_is_rejected`, `mask_naming_a_non_input_is_rejected_with_the_stray_pins` and `mask_of_configured_inputs_is_accepted`. `InputLevels::level` (`api/src/gpio/mod.rs`): `pin >= 32 \|\| mask & (1 << pin) == 0`; pairs `level(32)` and `level(3)` against `level(1)` in `input_levels_masks_and_reports_levels`. Both decisions have 2 conditions (CS-17 limit 4) |
| S5 | Eight mutants in the worktree, each run against `cargo test -p pico2 -p api` (the worktree restored with `git checkout -- .` after each): M1 `requested == 0` clause removed; M2 `stray != 0` clause removed; M3 stray forced to 0; M4 the `self.inputs \|= BIT` record removed from `input_from_handle`; M5 `inputs` set to every pin in `input_from_handle`; M6 `InputLevels::new` stops masking; M7 `level` ignores the mask; M8 `read_inputs` reads `GPIO_IN` twice | killed: M1 (1 failure), M2 (1), M3 (1), M6 (2), M7 (2), M8 (2). **Survive: M4 and M5**, every host test passing. The `inputs` record is the only thing that makes the NotInput check mean "configured input" (see S6), and it is target-only (S3); ADR-054 section 4.3 plans its dev-board check for one of its two failure cases only (finding-1) |
| S6 | Safety meaning of the mask check, read against the pre-existing pad configuration at `f85a190` (`configure_gpio_pin_in`, `gpio.rs:405-470`) and ICD-CTL-KEY section 3.2.5 | A pin configured through `input_from_handle` has `IE` = 1, `OD` = 1, the pulls as requested, `FUNCSEL` = SIO with `INOVER` normal, `SCHMITT` at its reset value, and `ISO` cleared last. A pin never configured keeps its reset pad (`IE` = 0, `ISO` = 1), and its `GPIO_IN` bit reads 0 ("Without it GPIO_IN reads 0 forever", `gpio.rs` comment). cwht key and paddle lines are read **active-low** (ICD-CTL-KEY 3.2.5; HZ-010 K2), so 0 is "contact closed". The NotInput check therefore stops the keyer's sample from including a pad that would read as a permanent closure, the HZ-010 C6 cause ("the pad left input-disabled ... reading an open contact as closed") |
| S7 | Target build and Miri | not repeated; INSP-098 C2 (target dev and release, no warning) and C3 (Miri clean at the stack head) accepted as the file reviewer's evidence |
| S8 | `tools/traceability.py --report-only --output <scratch>/trace-sa02.md` on cwht `main` | 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125, REQ-SYS-148; neither touched by the product). `docs/vv/` unchanged (`git status --short docs/vv` empty) |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | SA-D1; `swe-205 7.1 task 1`; `swe-062 7.1 task 1`; SWE-134 items f and g | ADR-054 section 4.3 (blob `848102d2`), "Dev-board check" and "Hazard analysis update required: no" bullets; rustos `api/src/gpio/mod.rs` `InputLevels` docs (`f0250c93`, SNP-2); `firmware/pico2/src/gpio/gpio.rs` `input_from_handle` (`d7ea7a70`, `:192-196`) | The fail direction of the input path is not recorded, and one of its two guard failures has no planned check. (a) Two values that mean "no valid reading" are 0: a bit outside the mask (SNP-2) and a pad that was never configured (S6). On the active-low cwht key and paddle lines, 0 is "contact closed". `level()` returns `None` outside the mask, but `bits()` does not show the difference, and ADR-054 does not tell the `cwht-hal-mock` author or the `cwht-core` consumer that a raw-bits consumer must apply the mask. (b) The guard that keeps a never-configured pad out of the sample is the `inputs` record in `input_from_handle`. It has no host test (S5: M4 and M5 survive; S3: `gpio.rs` 0 % on the host), which 07 section 9.5 allows for target-only code. But the ADR-054 dev-board check names only "a snapshot with a mask naming an output pin is refused". The HZ-010 C6 case, a mask naming a pin that was never configured, is not named. (c) The sampler's mask sits in RAM with no complement. SNP-1 makes a per-sample check `levels.mask() == expected` cheap for the consumer (the SWE-134 f and g provisions of `SW-KEYER`), but no document asks for it. The hazard data already carry the cause (HZ-010 C6), and the HZ-004 K1 interlock and REQ-SW-KEYER-036 catch a reading stuck at closed. So no safety conclusion changes, and the finding is Minor. **Fix:** (a) one ADR-054 section 4.3 sentence: for the active-low key inputs, 0 means closed; the snapshot's no-data value and an unconfigured pad both read 0; consumers take levels through `level()` or apply `mask()` first. The same sentence can go on `InputLevels::bits` in rustos house style. (b) add to the planned dev-board check `sio_check` "a mask naming a pin never configured is refused" as the HZ-010 C6 case, next to the output-pin case. (c) name the per-sample `mask()` check as an input to the `SW-KEYER` design (WP-PDR-32 or 35) | Open | Pending | |

**Paired record findings under the assurance lens (not raised again; template finding rules).**
- INSP-098 finding-1 (CS-18, `gpio.rs` grows from 512 to 546 lines): concur at Major. Under `swe-061 7.1 task 2`, safety-critical code must conform to the coding standard. A standard rule broken by avoidable growth, with no waiver on record, cannot be passed by assurance. The fix moves code between files and changes the blobs, so both records need a delta iteration (SA-A3). That delta also re-checks S2 to S5 on the moved `impl` block.
- INSP-098 finding-2 (new lines fail `rustfmt` and `clippy -D warnings`; SW-04 line 30 reports "clippy-clean"): concur at Minor. S2 reproduces the two `needless_return` hits. Under `swe-135 7.1 task 3`, the author's report of a static-analysis result should match the measured result. The severity does not rise, because both hits are style lints, not defect lints.
- INSP-098 finding-3 (`InputSnapshot::snapshot` replaces the 07 section 19 row name `SioInputs::snapshot()` with no note): concur at Minor. Under `swe-060 7.1 task 1`, the design (07 section 19 row, ADR-054) and the code should use one name. The fix should reach the mock author before the mock is written, and finding-1 (a) goes to the same reader.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the code review of a safety-critical driver (07 section 2.1.1 row "code"; plan WP-PDR-41 "Reviewer ... and SA") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against 07 section 15, the project's software assurance plan. The NASA-STD-8739.8 part is relieved (`rmm.json` SWE-022 T) | | none |
| swe-060 7.1 task 1 | | Yes | The code implements ADR-054 section 2 items 1 and 2 clause by clause: `InputLevels` with the mask (SNP-2 by construction in `new`), the trait with SNP-1 to SNP-4, the `inputs` record, `input_snapshot` with `NotInput` carrying the stray pins, one `GPIO_IN` load (S5 M8 killed), and no `IO_BANK0` or pad write in the new code (CS-35). The name departs from the 07 section 19 row (INSP-098 finding-3, concurred) | | none (INSP-098 finding-3) |
| swe-060 7.1 task 2 | | Yes | No function outside ADR-054 section 2. `Rp2350GpioIn::BIT` is the design's pin bit. The existing pin API is unchanged, as ADR-054 section 2 item 2 states | | none |
| swe-061 7.1 task 1 | | Yes | 07 section 7 (CS-01 to CS-38) is the coding standard for `pico2`. INSP-098 applied the code checklist revision B against it | | none |
| swe-061 7.1 task 2 | | No | The new code conforms apart from CS-18 (`gpio.rs` 546 lines, avoidable growth; INSP-098 finding-1) and CS-26 and CS-27 on three new lines (INSP-098 finding-2). CS-35 and CS-38 are met: the decisions are host-compilable pure functions (S4) | | INSP-098 finding-1, finding-2 |
| swe-207 7.1 task 1 | | Yes | The coding standard carries secure-coding rules (07 CS-29 to CS-33). 07 section 16.2, row "Keying and control inputs", states the key line feeds only the keyer state machine. The snapshot reads levels only, and no input changes configuration | | none |
| swe-185 7.1 task 1 | | Yes | S2 and a reading of the change. No `unsafe` is added (the read goes through `Regs`/`Mmio`, ADR-051). No external data reaches an index or a shift: the pin bit is a const-asserted `N < MAX_GPIO_PIN`, `level` bounds `pin < 32` before shifting, and the mask is checked before a sampler exists | | none |
| swe-135 7.1 task 1 | | Yes | S2 (clippy pedantic), S3 (coverage), S4 (decision complexity), S5 (mutants). No defect lint on the product lines. Coverage and complexity are under tasks 5 and 6 | | none |
| swe-135 7.1 task 2 | | Yes | Clippy with `-D warnings` is the lint checker of gate G1 (07 section 8.2 gate table; TV-020), and G5 adds `cargo audit`, `cargo deny`, `cargo geiger`, the unsafe audit and the complexity gate. S2 reproduces the INSP-098 C4 result | | none |
| swe-135 7.1 task 3 | | Yes | The two `needless_return` hits on new lines are tracked as INSP-098 finding-2 (concurred). The author's "clippy-clean" statement differs from the measured result, and that difference is in the same finding | | none (INSP-098 finding-2) |
| swe-135 7.1 task 4 | | N/A | The security scan (G5 `cargo audit`, `cargo deny check`, `cargo geiger --forbid-only`) runs on the pin-move CR branch against the merged rustos commit, and no result exists at this commit. The change adds no dependency and no manifest line (INSP-098 CK-CODE-A1 to A3), and the CS-29 to CS-33 reading is under swe-185 | 07 section 8.2 gate G5; plan section 6.2 PCR-4 (SW-04 phase 4) | none |
| swe-135 7.1 task 5 | SC | Yes | Under swe-219 task 1 below | | none |
| swe-135 7.1 task 6 | SC | Yes | Under swe-220 below | | none |
| swe-135 7.1 task 7 | | N/A | Static-analysis quality thresholds are set by the gate definitions (G2 zero warnings, G5 complexity 15), not per product | 07 section 8.2 | none |
| swe-134 7.1 task 2 | SC | Yes | Section C: items a, e, f, g, h, i, j and k answered for the driver's inherited role. b, c, d and l have no function in this driver. f and g are partial and carried by finding-1 | | finding-1 |
| swe-134 7.1 task 3 | SC | N/A | The product holds no safety-critical loaded data. The pin mask is a code constant of the consumer (the ICD-CTL-SW pin map), not persisted configuration | 07 section 9.7 (loaded items are the image and the persisted configuration) | none |
| swe-134 7.1 task 6 | SC | Yes | The input path's contribution is consistent with HZ-004 C8 and HZ-010 C6 and C7 (S6). The fail direction is not recorded in the ADR (finding-1) | | finding-1 |
| swe-087 7.1 task 4 | SC | Yes | Section C, as for swe-134 task 2 | | finding-1 |
| swe-062 7.1 task 1 | SC | No | The unit tests run and pass (S1), and they kill the mutants of both decision functions (S5 M1 to M3, M6 to M8). The safety-relevant `inputs` record has no host test (S5 M4, M5), which the target-only rule allows (07 section 9.5). But its planned dev-board check omits the never-configured case | | finding-1 |
| swe-062 7.1 task 2 | | Yes | The open items of phase 2 (contract test adopted or replaced by the independent test author, SW-04 line 46; INSP-098 R5 and CK-CODE-H2) are tracked in SW-04 and INSP-098 | | none |
| swe-219 7.1 task 1 | SC | Yes | 07 section 9.6 method (`rmm.json` SWE-219 T): the decision table and independence pairs exist for both new decisions (S4), and host coverage of the decision code is 100 % (S3). The remaining lines are target-only MMIO wrappers under 07 section 9.5 (dev-board check, Bench, emulation if ACC-EMU-001 is accepted). The credit record (TC-SW-COV-001 with MSR-13 and MSR-14) is produced by gate G6 at the release gates and from CDR onward (07 section 8.2) | | none |
| swe-220 7.1 task 1 | SC | Yes | Cyclomatic complexity by reading, because the gate needs analyzer JSON input (`tools/complexity_gate.py --input`): `check_snapshot_mask` 3, `InputLevels::level` 3, `input_from_handle` 1 plus the `?` early return (2), every other new function 1. The author reports `complexity_gate.py --max 15` passing (SW-04 phase 1) | | none |
| swe-220 7.1 task 2 | SC | Yes | Every new function is at 15 or lower. No waiver is needed (07 section 14.3) | | none |
| swe-205 7.1 task 1 | SC | Yes | Section D, SA-D1 | | finding-1 |
| swe-205 7.1 task 3 | SC | Yes | No new component. WP-SW-02 is in the 07 section 14.1 drivers row and in the 03 section 4.3 drivers row | | none |
| swe-205 7.1 task 4; swe-052 7.1 task 2 | SC | Yes | Section D, SA-D3 | | none |
| swe-192 7.1 task 1 | SC | Yes | Section D, SA-D5 | | none |
| swe-080 7.1 task 1 | SC | Yes | Safety impact of the change: it adds a sampler and no output path. It narrows what can be sampled to configured inputs, and a never-configured pad would read as closed (S6). It weakens no existing control: `GpioPinIn::read` is unchanged, and no pad or `IO_BANK0` write is added. Security: swe-185 | | none |
| swe-080 7.1 task 3 | | Yes | Section E, SA-E3 | | none |
| swe-081 7.1 task 2 | SC | Yes | The rustos code enters cwht configuration only through the Class I pin-move CR (plan PCR-4, section 6.2). The hazard data it serves (`hazards.json`) are unchanged | | none |
| swe-187 7.1 task 1 | | Yes | Section E, SA-E4 | | none |
| swe-187 7.1 task 2 | | N/A | No credit test has started. The dev-board check is `credit: false`, and the Bench cases follow the pin move | 04 section 5.2 (credit runs name a tagged release) | none |
| swe-087 7.1 task 1 | | Yes | INSP-098 iteration 1 was performed and recorded. This record is its SA pair | | none |
| swe-087 7.1 task 2 | | Yes | INSP-098 findings 1 to 3 are Open with a fix route. Iteration 2 is a delta that verifies finding-1 | | none |
| swe-088 7.1 task 1 | | Yes | INSP-098 meets NPR 7150.2D 5.3.3 a to d: (a) checklist revision B with every item answered; (b) readiness R1 to R6 answered, with R1, R2, R3 and R5 not met and their consequence recorded; (c) findings with state; (d) participants named in the front matter | | none |
| swe-088 7.1 task 2 | | Yes | The INSP-098 findings each carry a fix, and SW-04 phases 2 to 5 carry the open author and test-author actions | | none |
| swe-089 7.1 task 1 | | Yes | Both records carry `findings_*`, `items_no`, `unsafe_sites_reviewed` (INSP-098), `effort_turns`, `effort_minutes`, `iteration` and `product_size` | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | S0: all eight blobs equal INSP-098 |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | Row "code". The criticality is safety-critical by inheritance: 07 section 14.1 drivers row, "GPIO (SIO) ... `pico2` (WP-SW-01, 02, ...)", "as the components they serve", items "inherited" |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with a scratch `--output` reports no violation for the ids touched | Yes | S8: 0 violations. The product touches no requirement, case or hazard id. ADR-054 and SW-04 pass `validate_docs.py` on `main` (Commands) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-098 is committed on `main` (`9d3734c`), with `author_agent` "author:WP-PDR-41 wave 1a" and `reviewer_agent` "reviewer:WP-PDR-41-code". This invocation is `sa-reviewer:WP-PDR-41-code-wp-sw-02` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | The 07 section 2.1.1 row "code" is Yes for safety-critical. The 14.1 line is the drivers row (R2). Plan WP-PDR-41 names the SA review ("drivers of safety-critical components") |
| SA-A2 | Yes | Three invocations: author "author:WP-PDR-41 wave 1a", file reviewer "reviewer:WP-PDR-41-code" and this assurance reviewer. INSP-098 names the pairing as "pending" with this record's path, and it does not yet carry `paired_record` (each reviewer updates only its own record) |
| SA-A3 | Yes | Same `product` text, same `product_commit` `f85a190` and the same eight blobs. The INSP-098 finding-1 fix changes blobs, so a delta iteration of both records is needed (rule C2) |
| SA-A4 | Yes | INSP-098 applied `peer-review-checklist-code.md` revision B, which 07 section 10.1 and 08 section 3.5 assign to code. Every item is answered with evidence, and the cwht-only items (F1 to F3) are N/A with the reason "rustos code" (plan WP-PDR-41 exempts rustos from CS-24 tags) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds the "Every product type" row, every task of the "code" row, and the section 7.1 tasks of SWE-205, 052, 192, 080, 081, 187, 087, 088 and 089. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | Each N/A row cites its relief: swe-134 task 3 (07 section 9.7), swe-135 task 4 (07 section 8.2 G5 on the pin-move CR), swe-135 task 7 (07 section 8.2), swe-187 task 2 (04 section 5.2). No SC task is N/A except swe-134 task 3, whose condition (loaded data) does not arise |
| SA-B3 | Yes | swe-061 task 2 (No) is carried by INSP-098 finding-1 and finding-2, and swe-062 task 1 (No) by finding-1 |

## C. SWE-134 items a to l (the drivers row inherits the `SW-KEYER` items a to l, 07 section 14.2; answered for this driver's role)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | `Rp2350Gpio::new` starts with `inputs: 0`, so no sampler can exist before a pin is configured as an input. The keyer's `TX_KEY` idle state and interlock are not in this driver |
| SA-C-b | N/A | The driver has no state machine. The `inputs` set only grows, and sampling changes no state (`GPIO_IN` read has no side effect, datasheet section 3.1.11) |
| SA-C-c | N/A | The driver has no termination path of its own. `snapshot` is `Infallible` |
| SA-C-d | N/A | No operator override passes through the driver |
| SA-C-e | Yes | An out-of-order request, a sampler asked for before its pins are configured, is refused with `NotInput` (S4, S5 M1 to M3) |
| SA-C-f | Partial | The sampler's mask sits in RAM with no complement. SNP-1 makes a per-sample `mask()` check cheap for the consumer, but no document asks for it (finding-1 (c)). The keyer's own f provision (dit and dah memories and key-down state with complements) is `cwht-core` work |
| SA-C-g | Partial | The driver checks the configuration of what it samples (the mask check) and returns raw levels. Debounce, stuck-input detection and jack-detect checks are `SW-KEYER` duties (07 section 14.2; HZ-010 K3). The fail direction of the raw levels (0 = closed) is not recorded (finding-1 (a)) |
| SA-C-h | Yes | Prerequisite: every sampled pin is a configured input (IE on, ISO off; S6), checked when the sampler is built. The unconfigured-pin case lacks a planned check (finding-1 (b)) |
| SA-C-i | Yes | One sample cannot key the transmitter. Debounce needs consecutive samples (REQ-SW-KEYER-020, 021), and RF also needs the separate PA-permit flag (07 section 14.2 row i). One `GPIO_IN` load means no mixed-instant sample (SNP-4; S5 M8 killed) |
| SA-C-j | Yes | The sample is one load with no loop and no wait, a fixed cost well inside the 1 ms ALARM1 period of REQ-SW-KEYER-019. The key-up response budget is a `SW-KEYER` item |
| SA-C-k | Yes | `NotInput { mask }` names the stray pins, and an empty request is refused. The read cannot fail (`Infallible`). No error path is ignored |
| SA-C-l | N/A | The driver cannot place the system in the safe state. The keyer and the safe-state manager do |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | `hazards.json` names the input-path software causes: HZ-010 C6 (pad configuration, "reading an open contact as closed"), HZ-010 C7 (debounce and stuck-input misclassification) and HZ-004 C8. Of the SWEHB `swe-205` section 7.7 considerations, three apply: control of safety-critical hardware (the key input feeds `TX_KEY` through the keyer), interlocks (HZ-004 K1 relies on the samples) and monitoring (HZ-010 K3). The hazard data are complete. The design record does not state the fail direction, and the check plan omits the never-configured case (finding-1) |
| SA-D2 | Yes | The drivers row criticality ("as the components they serve", inherited) equals the 03 section 4.1 union for the keyer, which is safety-critical through HZ-004 criteria a, b, c and HZ-010 criterion c. No component is new or renamed |
| SA-D3 | Yes | The product implements no requirement id of its own. The requirements it serves (REQ-SW-KEYER-019 to 022, 036, 039) trace to HZ-004 and HZ-010 and back (S8: 0 violations, no `HAZARD_INVERSE`) |
| SA-D4 | N/A | No requirement is created or changed (ADR-054 section 4.1). The `Depends on:` rationales are the requirement author's |
| SA-D5 | Yes | S8 reports no `HAZARD_REQ_NOT_TESTED` for the served requirements. The closing Test cases for the keyer sampling are `SW-KEYER` cases that run on the mock and at Bench after the pin move |
| SA-D6 | Yes | ADR-054 section 4.3 states "Hazard analysis update required: no", and the assurance lens concurs. The cause is already HZ-010 C6, and the snapshot adds a guard against it, not a new contribution. Recording the fail direction (finding-1) is a design-record change, not a hazard change |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | N/A | Iteration 1: there is no earlier review of this product. INSP-098 findings are Open at the same iteration |
| SA-E2 | Yes | Both records carry the 07 section 10.3 measurements (front matter) |
| SA-E3 | Yes | The rustos code is outside cwht control until the owner's merge. It enters cwht configuration by the Class I pin-move CR (PCR-4, plan section 6.2). ADR-054 and SW-04 are Record-class items (05 Table 4-1 rows 13 and 44), added as new files on `main` in `618e441`. The Record class is append-only and needs no `CR:` or `Refs:` trailer (05 control classes) |
| SA-E4 | Yes | The tested items are the committed rustos branch `f85a190` and the committed cwht files. No credit run has taken place (the dev-board check is `credit: false`) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the finding needs a risk entry. The target-only verification of the `inputs` record (dev-board check `credit: false` until Bench, ACC-EMU-001 pending WP-PDR-42) is the RSK-013 schedule path of the minimal keyer set, already in the register |
| SA-F2 | Yes | Front matter: `findings_*`, `assurance_findings_major` 0 and `assurance_findings_minor` 1, `items_no`, effort |
| SA-F3 | Yes | This record supports the package's "Software assurance findings" section on its own: assurance NEEDS CHANGES on the concurred INSP-098 finding-1 (Major, CS-18); one Minor of its own (finding-1); tasks and reliefs in the task table |

## Commands run

| Command | Result |
|---|---|
| `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa-wp-sw-02 f85a190`, then `worktree remove` | created, used for S1 to S5, clean, removed |
| `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --report-only --output <scratchpad>/trace-sa02.md` | 0 violations, 2 warnings; `docs/vv/` unchanged |
| `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` | passes with this record (run before commit) |

## Measurements (SWE-089)

Lines reviewed: about 185 non-test lines, the 174-line contract draft, 6 developer tests, the pre-existing `configure_gpio_pin_in` for S6, ADR-054 and SW-04 in full. Unsafe sites added: 0. Mutants: 8 (6 killed, 2 survive). Tasks in the table: 36 rows (4 N/A, 2 No). Findings: 0 Major, 1 Minor of this record; 3 INSP-098 findings concurred. Effort: 32 turns, 60 minutes.

## Record verdict

`assurance_verdict: NEEDS CHANGES`. The reason is INSP-098 finding-1 (CS-18, Major), concurred under `swe-061 7.1 task 2` and not raised again. This record's own finding-1 is Minor. Iteration 2 is a delta at the new blobs. It verifies INSP-098 finding-1 and re-runs S2 to S5 on the moved code. finding-1 here is fixed with that change or becomes a lien due at the CDR readiness declaration (rule C1). `verdict` stays `NEEDS CHANGES` under the lead SE convention until both records are APPROVED and the blobs reach a configuration cwht consumes.

## Iteration 2: assurance delta at rustos `38434b2` (2026-09-27, cwht HEAD `0be8bab`)

**Scope (rule C1).** Iteration 2 is a delta. It verifies the INSP-098 finding-1 fix (CS-18, Major) under the assurance lens, re-runs S2 to S5 on the moved code, re-checks this record's tasks on the changed lines and reads every hunk of the five drifted blobs: ADR-054 `848102d2` to `ae2afdd8`, SW-04 `1686ecc0` to `a79d4d99`, `docs/sprints/index.md` `fb217bcb` to `7ae0cbcc`, rustos `firmware/pico2/src/gpio/gpio.rs` `d7ea7a70` to `cdb5fc92` and `firmware/pico2/src/gpio/snapshot.rs` `6b5ddac5` to `00e2c301`. The other three blobs are unchanged. The rustos package delta is `git diff 5d4637f 38434b2` (2 files, 70 insertions, 52 deletions). `git diff --stat f85a190 5d4637f` on the product paths is empty, so the merge of `cwht/wp-sw-01` at `58fe739` changes no product file. SW-04 "Phase 1, revision 2" names the delta as `git diff f85a190 38434b2`; on the product paths that equals the diff above. Checklist as at iteration 1.

**Independence (rule C4).** Same invocation role as iteration 1. It authored no part of revision 2, the rustos fix commits or INSP-098, and it edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: "INSP-098 iteration 2 code-wp-sw-02 CS-18 gpio.rs split snapshot verified delta"). Afterwards `grep` was used only on known paths (the record, INSP-098, 07, the plan, the validator header) and `git grep` on rustos objects. **rustos.** The owner's rustos working tree was not read or changed. All runs used a detached scratch worktree of `38434b2` (`git worktree add --detach` under the session scratchpad) with scratch `CARGO_TARGET_DIR`s. Every mutant and the probe tests were reverted with `git checkout -- .`, `git status --short` was empty before `git worktree remove`, and the target directories were deleted. No branch was created, nothing was pushed or merged, every `cargo` run was `--offline` with `RUSTUP_AUTO_INSTALL=0`, and there was no download. LTspice was not run.

### Assurance re-runs and checks, iteration 2

| # | Check | Result |
|---|---|---|
| T0 | Blob identities: `git -C rustos rev-parse 38434b2:<path>` for the five rustos entries (branch head `cwht/wp-sw-02` = `38434b2`); `git rev-parse HEAD:<path>` and `git hash-object <path>` for the three cwht entries | all eight equal INSP-098 iteration 2 `product_files` |
| T1 | `cargo +1.98.0 test --offline -p pico2` and `-p api --test gpio_snapshot_contract` | pico2 81 passed; contract 5 passed; none failed. Equal to INSP-098 D2 at `38434b2` |
| T2 | `cargo +1.98.0 clippy --offline -p pico2 -p api --all-targets -- -W clippy::pedantic`, hits in the product files located with `git blame 38434b2` | Every hit in `gpio.rs` and `api/src/gpio/mod.rs` is on a line from before the package (`48cd871d`, `f1b2b218`, `5ea7472f`, `d4573ed1`). No hit in `snapshot.rs`. The two iteration 1 `needless_return` hits (`gpio.rs:156`, `:195`) are gone: `new` ends in `Self { inputs: 0 }` and `input_from_handle` is one expression |
| T3 | `rustfmt +1.98.0 --edition 2024 --check` on `snapshot.rs`, and the difference count of `gpio.rs` at `38434b2` against `2ec64c0` | `snapshot.rs` clean. `gpio.rs` 35 differences, the same as `2ec64c0` before the package (38 at `f85a190`), so the package adds no `rustfmt` difference. INSP-098 finding-2 stays that reviewer's to close |
| T4 | CS-18 file length (`wc -l` through `git show`) | `gpio.rs` 512 at `2ec64c0`, 546 at `f85a190`, 512 at `38434b2`; `snapshot.rs` 177. Agrees with INSP-098 D9 |
| T5 | Target build, `cargo +1.98.0 build --offline -p pico2 --target thumbv8m.main-none-eabihf` (dev) | no warning, no error. INSP-098 D3 (release) and D4 (Miri at the stack head) accepted as the file reviewer's evidence |
| T6 | Host coverage, `cargo llvm-cov --offline -p pico2 -p api` (developer evidence, not MSR-13) | `api/src/gpio/mod.rs` 100 % (15 of 15 lines). `snapshot.rs` 68.42 % lines (39 of 57), 79.79 % regions: not executed are `input_snapshot` (`:49-51`), `track_input` (`:55-63`), `Rp2350InputSnapshot::new` and `mask`. `gpio.rs` 0 % (82 lines) |
| T7 | Decision inventory (07 section 9.6 item 1; CS-38) on the changed lines | The two iteration 1 decisions are unchanged (S4). New: `track_input` holds the decision `pin.is_ok()` (`snapshot.rs:59`), 1 condition, CC 2. `new_input` always returns `Ok` (`gpio.rs:272-280`), so its false outcome cannot occur in the product. Its true outcome cannot be reached from a host test either, because `Rp2350GpioIn` has a field private to `gpio.rs` and `snapshot.rs` tests cannot build one. Not in ADR-054 or S4 (finding-2 (a)) |
| T8 | Mutants on the moved code, each run against `cargo test -p pico2 -p api` and reverted: M1 to M3 as at iteration 1, now on `NotInput`; M4 `track_input` record removed; M5 `track_input` sets every pin; M9 `is_ok` inverted; M10 `new` starts with `inputs: u32::MAX`; M11 `input_snapshot` checks against `u32::MAX` instead of `self.inputs` | killed: M1, M2, M3 (1 failure each). **Survive: M4, M5, M9, M10, M11.** M6 to M8 are on unchanged blobs (`api/src/gpio/mod.rs`, `read_inputs`) and are not repeated |
| T9 | Host-testability probe: two throw-away tests appended to `snapshot.rs` in the worktree (reverted): `Rp2350Gpio { inputs: 0b100 }` with `input_snapshot(0b100)` accepted and `input_snapshot(0b1100)` refused with `NotInput { mask: 0b1000 }`; `track_input::<3>(Err(GpioError::PinOOB { .. }))` leaves `inputs` at 0 | Both pass on `38434b2`. With M11 applied, the first fails. The move makes the record check of `input_snapshot` host-testable, because `inputs` is `pub(super)`, and one short test kills M11. The `Ok` arm of `track_input` (M4, M5, M9) stays unreachable from a host test (finding-2) |
| T10 | `tools/traceability.py`: not re-run | The delta touches no requirement, case or hazard id, and S8 stands |

### Hunk reading of the drifted blobs

- **`gpio.rs` `d7ea7a70` to `cdb5fc92`.** (1) The `use` of `snapshot` is removed, which also removes the iteration 1 import-order difference. (2) The `GpioError::NotInput` variant and its `Debug` arm are removed, so `GpioError` is as on rustos master. (3) The struct doc now describes the one word of state. It says the field is "private to `gpio`": `pub(super)` on a field of `crate::gpio::gpio` makes it visible in `crate::gpio` and its descendants, which is what the doc means. The struct literal stays unwritable outside `crate::gpio`, so `new` with its `DeviceHandle` is still the only route outside the module (SA-C-a holds: `inputs` starts at 0). (4) `_private` and the doc of `inputs` are replaced by `pub(super) inputs: u32`. (5) `new` returns `Self { inputs: 0 }`. (6) `input_snapshot` moves out. (7) `input_from_handle` becomes `self.track_input(Rp2350GpioIn::new_input(handle, pull))`. The record is still made only after a successful configuration, as the `?` did at iteration 1. (8) `BIT` moves out. No pad, `IO_BANK0` or `unsafe` line changes (CS-35; R6).
- **`snapshot.rs` `6b5ddac5` to `00e2c301`.** A module note says where the additions live. `NotInput { pub mask: u32 }` is its own `Copy`, `PartialEq` type. The inherent `impl Rp2350Gpio` holds `input_snapshot` (now `Result<_, NotInput>`, same body) and `track_input` (T7). The inherent `impl Rp2350GpioIn<N>` holds `BIT` with the same compile-time `N < MAX_GPIO_PIN` assert, now referenced from `track_input`, so the bound is still checked for every input pin built. `check_snapshot_mask` returns `NotInput`, same logic. The two rejection tests compare values with `assert_eq!`, which is stricter than the iteration 1 `matches!`. No new `unsafe`.
- **ADR-054 `848102d2` to `ae2afdd8`.** The Date row, section 2 item 2 (the `NotInput` type) and section 4.2 (design elements, the no-growth statement) are updated. Section 4.3 gains a revision 2 evidence bullet, and section 8 (revision history) is new. Section 8 states that the Minor findings of INSP-098 and INSP-104 are not addressed (rule C1). The section 4.3 dev-board bullet is unchanged, so finding-1 (b) stands. Section 4.2 now places `track_input` in `snapshot.rs` but lists no decision table entry for it (finding-2 (a)). Status stays Proposed.
- **SW-04 `1686ecc0` to `a79d4d99`.** The Product row points to `38434b2`. The new "Phase 1, revision 2" block gives the findings addressed, the merge, the fix, the evidence (81 host tests, which T1 reproduces) and the file lengths (which T4 reproduces). Phase 3 names the iteration 2 delta. Phase 2 (independent test author) is still open, and it is the route for finding-2 (b).
- **`docs/sprints/index.md` `fb217bcb` to `7ae0cbcc`.** The five FW-B1 rows move to their revision 2 commits, and the SW-04 row reads `38434b2`, equal to T0. No row is added or removed.

### Verification of INSP-098 finding-1 under the assurance lens

| Case | Assurance question (`swe-061 7.1 task 2`, CS-18) | Evidence | Result |
|---|---|---|---|
| Growth of `gpio.rs` | Does the package still grow a file that is over 500 lines? | T4: 512 before and after the package | Verified |
| Behaviour preserved | Does the move change what the guard accepts or refuses? | `check_snapshot_mask` logic is unchanged and M1 to M3 are killed (T8). `track_input` records only on success, the same as the iteration 1 `?`. `BIT` keeps its compile-time bound | Verified |
| No new coding-standard breach on moved lines | Do the moved lines break CS-26 or CS-27 (INSP-098 finding-2 lines)? | T2 and T3: no lint or `rustfmt` difference added by the package | Verified |
| Pre-existing excess | Is the 12-line excess of `gpio.rs` recorded? | ADR-054 section 4.2 and SW-04 revision 2: reported to the owner as a rustos item | Verified |

INSP-098 finding-1 is Verified at `38434b2`. This agrees with INSP-098 iteration 2.

### Task table, rows re-answered at iteration 2

Rows not listed stand as at iteration 1. The moved lines do not change them: no new `unsafe`, no new dependency, no new requirement or hazard link.

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-061 7.1 task 2 | | No | CS-18 is now met by the package (INSP-098 finding-1 Verified). The package adds no CS-26 or CS-27 difference (T2, T3), and INSP-098 finding-2 stays Open with that reviewer. It stays No on CS-38: the new decision in `track_input` is in safety-critical driver code, but it is not a function whose two outcomes a HostUnit test can show (T7) | | finding-2 |
| swe-062 7.1 task 1 | SC | No | T1 passes. Host tests still do not guard the record (T8: M4, M5, M9, M10, M11 survive). Part of that is now host-testable (T9) but untested, and the dev-board check still omits the never-configured case | | finding-1, finding-2 |
| swe-219 7.1 task 1 | SC | No | The two iteration 1 decisions keep their independence pairs (S4; M1 to M3 killed). The new `pin.is_ok()` decision is not in the decision table, and neither of its outcomes can be shown by a host test (T7) | | finding-2 |
| swe-220 7.1 task 1 and task 2 | SC | Yes | By reading: `track_input` CC 2, `input_snapshot` 1, `check_snapshot_mask` 3 (unchanged), `input_from_handle` 1 (was 2). All are at 15 or lower. INSP-098 D5 (`complexity_gate.py --max 15`) PASS at the stack head | | none |
| swe-135 7.1 task 3 | | Yes | The author's revision 2 statement ("`rustfmt` and `clippy::pedantic` clean on `snapshot.rs` and on the changed `gpio.rs` lines", ADR-054 section 4.3, SW-04) matches T2 and T3 | | none |
| swe-060 7.1 task 1 | | Yes | ADR-054 section 2 item 2 and section 4.2 describe the code at `38434b2` (the `NotInput` type, `track_input`, `BIT`, the `inputs` field). INSP-098 finding-3 is unchanged | | none (INSP-098 finding-3) |
| swe-080 7.1 task 1 | SC | Yes | The change is a move. It adds no output path and weakens no control. The only change a caller sees is the error type of `input_snapshot`, and nothing outside the package used the iteration 1 variant (`git grep` at `38434b2`) | | none |
| swe-087 7.1 task 2 | | Yes | INSP-098 finding-1 is Verified. INSP-098 findings 2 and 3 and this record's findings 1 and 2 are Open as liens, each with a fix route | | none |
| SA-C-a | SC | Yes | `Rp2350Gpio::new` returns `Self { inputs: 0 }`. The struct literal cannot be written outside `crate::gpio` (hunk reading) | | none |
| SA-C-h | SC | Yes | Unchanged prerequisite. The record check of `input_snapshot` is now host-testable (T9) but untested | | finding-1, finding-2 |
| SA-A3 | | Yes | Same `product_commit` `38434b2` and the same eight blobs as INSP-098 iteration 2 (T0) | | none |
| SA-E1 | | Yes | Earlier review: iteration 1 of this record and INSP-098. The finding-1 fix is verified above. The two Minors of this record are carried | | none |
| SA-F3 | | Yes | For the package's "Software assurance findings" section: assurance APPROVED at iteration 2, 0 Major, 2 Minor liens (findings 1 and 2) due at the CDR readiness declaration | | finding-1, finding-2 |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | assurance | Minor | SA-D1; `swe-205 7.1 task 1`; `swe-062 7.1 task 1`; SWE-134 items f and g | ADR-054 section 4.3 (now blob `ae2afdd8`), "Dev-board check" and "Hazard analysis update required: no" bullets; rustos `api/src/gpio/mod.rs` `InputLevels` docs (`f0250c93`, SNP-2); the input record, now `snapshot.rs` `track_input` (`00e2c301`, `:55-63`) | As at iteration 1: (a) the fail direction (0 = closed on the active-low key lines, both for the no-data value and for an unconfigured pad) is not recorded; (b) the dev-board check names only the output-pin case, not the HZ-010 C6 never-configured case; (c) no document asks for the per-sample `mask()` check. Revision 2 does not address it (ADR-054 section 8, rule C1). At iteration 2 the "07 section 9.5 target-only" premise of (b) holds only for the `Ok` arm of `track_input`; the rest is finding-2. Fix as at iteration 1 | Open (lien, rule C1) | Pending | CDR readiness declaration |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-219 7.1 task 1`; `swe-062 7.1 task 1`; `swe-061 7.1 task 2` (07 CS-38; 07 section 9.5 item 3; 07 section 9.6 items 1 and 2) | rustos `firmware/pico2/src/gpio/snapshot.rs` `00e2c301` `:49-51` (`input_snapshot`) and `:55-63` (`track_input`); ADR-054 section 4.2 (`ae2afdd8`) | The move puts the HZ-010 C6 guard into host-compilable code, so CS-38 now applies to it: every decision of a `pico2` driver used by a safety-critical component is a host-compilable function exercised by HostUnit tests with MC/DC independence pairs. Two gaps. (a) `track_input` adds the decision `pin.is_ok()`, which is not in the ADR-054 decision inventory. Its false outcome cannot occur, because `new_input` always returns `Ok` (`gpio.rs:272-280`), and its true outcome cannot be built in a host test, because `Rp2350GpioIn`'s field is private to `gpio.rs`. So no HostUnit pair can show both outcomes (T7), and M4, M5 and M9 survive (T8). (b) `input_snapshot`, which applies the record, is now host-testable (`inputs` is `pub(super)`; T9), but no test calls it, and M10 and M11 survive. A 5-line test kills M11 (T9). Behaviour is unchanged from iteration 1, the test author's phase 2 is open (07 section 9.6 item 2), and the HZ-004 K1 interlock and REQ-SW-KEYER-036 are unchanged, so no safety conclusion changes and the finding is Minor. **Fix:** (a) enter the `track_input` decision in the ADR-054 decision inventory. Then either take the decision out (record the bit only on the success path, with no `Result` test in `snapshot.rs`), or make both outcomes host-reachable, or disposition the unreachable outcome in the MC/DC table under 07 section 9.6 item 4. (b) add to the SW-04 phase 2 test list a host test of `input_snapshot` against a written `inputs` record (accepted, and refused with the stray pins), as the HostUnit half of the HZ-010 C6 guard. It complements the finding-1 (b) dev-board case | Open (lien, rule C1) | Pending | CDR readiness declaration |

**Paired record findings (not raised again).** INSP-098 finding-1: Verified (above). INSP-098 finding-2: T2 and T3 show that the package adds no lint or `rustfmt` difference at `38434b2`; the state stays with that reviewer. INSP-098 finding-3: unchanged, concur Minor.

### Commands run, iteration 2

| Command | Result |
|---|---|
| `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa02-it2 38434b2`, then `worktree remove` | created, used for T1 to T9, clean, removed; target directories deleted |
| `git -C /Users/robinonsay/rust/rustos diff 5d4637f 38434b2`; `diff --stat f85a190 5d4637f -- <product paths>`; `git diff <old blob> <new blob>` for ADR-054, SW-04 and the sprint index | every hunk read (above) |
| `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` | this record PASS. Overall exit 1 from 8 other records (for example `cm-plan-05-software-assurance.md`, `configuration-status.md` and five SRR records), none of them in this record's scope |

### Measurements (SWE-089), iteration 2

Lines reviewed: the 122 changed lines of `5d4637f..38434b2` and the 29 changed lines of ADR-054, SW-04 and the sprint index, plus the pre-existing `new_input` for T7. Unsafe sites added: 0. Mutants: 8 (3 killed, 5 survive), plus 2 probe tests (reverted). Findings: 0 Major, 1 new Minor (finding-2); finding-1 carried; INSP-098 finding-1 Verified. Effort of this iteration: about 25 turns and 45 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`assurance_verdict: APPROVED` and `reviewer_verdict: APPROVED`. INSP-098 finding-1 (CS-18, Major), the only reason for NEEDS CHANGES at iteration 1, is Verified at `38434b2`, and no Major is open. finding-1 and finding-2 (Minor) become liens under rule C1, owner the firmware developer (finding-2 (b) with the SW-04 phase 2 test author), due at the CDR readiness declaration. `verdict` stays `NEEDS CHANGES` under the lead SE convention of 2026-09-27: INSP-098 readiness R3 (ADR-054 Proposed) and R5 (no independent test-author file) do not hold, and the reviewed blobs exist only on unmerged rustos branches. The software lead sets `verdict` when the owner's merge and the PCR-4 pin-move CR bring `38434b2` into a configuration cwht consumes. INSP-098 still reads `assurance_verdict: pending`, and its reviewer updates it to APPROVED (cross item).
