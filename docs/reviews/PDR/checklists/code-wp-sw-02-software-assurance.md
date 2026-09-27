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
# product_commit and product_files: equal to INSP-098 iteration 1 (readiness R1; rule C2). The five rustos:
# blobs exist only on the unmerged rustos branch cwht/wp-sw-02 (git -C rustos rev-parse f85a190:<path>, checked
# 2026-09-27); the three cwht blobs are on main and equal at HEAD and at 618e441
product_commit: "f85a19085760f7c34803c094e918f6115c21da3d"
product_files: ["docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md@848102d2dac6d026a4718ae1fd57eb5f270c8245", "docs/sprints/SW-04-wp-sw-02-sio-snapshot.md@1686ecc09144d6ef16644522eff1cd0fb65f3584", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/gpio/mod.rs@f0250c93e08856270a702324b19fda0b04e9199b", "rustos:api/tests/gpio_snapshot_contract.rs@0918c1933350c2b159924d480a1738768f4b34c2", "rustos:firmware/pico2/src/gpio/gpio.rs@d7ea7a706b4131e5625aac2755845882c172e807", "rustos:firmware/pico2/src/gpio/mod.rs@d71011bf3934812b52eaac6fa3ccebaae0067a41", "rustos:firmware/pico2/src/gpio/snapshot.rs@6b5ddac5ff90032bf07c9ba9fac4f4fa96378a5b"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/code-wp-sw-02.md (INSP-098 iteration 1, main 9d3734c)", "docs/safety/hazards.json (HZ-004, HZ-010)", "docs/icd/ICD-CTL-KEY.md (section 3.2.5)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 3.5, 9.5, 9.6, 14.1, 14.2, 14.3, 15, 19)", "docs/process/03-software-classification-and-rmm.md (section 4.3 drivers row, section 5)", "docs/process/05-configuration-and-data-management.md (Table 4-1 rows 13 and 44)", "docs/plan/pdr-work-plan.md (sections 3.8, 5)", "rustos:firmware/pico2/src/gpio/gpio.rs configure_gpio_pin_in at f85a190 (pre-existing, not in the change)"]
paired_record: INSP-098
# product_type: code (07 section 2.1.1 row "code": every file of a safety-critical component). Task set applied:
# the section B rows "Every product type" and "code"; the section 7.1 tasks of the SWEs the product cites or
# serves (SWE-134 items g and i and SWE-219, ADR-054 section 1 "Guidance consulted"; SWE-205, SWE-052, SWE-192,
# SWE-184 through section D; SWE-080, SWE-081, SWE-187 and SWE-087 to SWE-089 through section E)
product_type: code
# criticality: safety-critical by inheritance, 07 section 14.1 drivers row "GPIO (SIO)" (pico2 WP-SW-02), serving
# the keyer and keying output (HZ-004, HZ-010); 03 section 4.3 drivers row; hazard-analysis.md section 7 drivers row
criticality: safety-critical
product_size: "409 lines added and 3 removed in f85a190, about 185 non-test lines (api gpio 72, snapshot.rs 69 before its test module, gpio.rs 37 changed, gpio/mod.rs 1); 174-line contract test draft; ADR-054 86 lines; SW-04 60 lines"
sprint: SW-04-wp-sw-02-sio-snapshot
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-02"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-02 (software assurance function; paired file review INSP-098 by reviewer:WP-PDR-41-code)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: NEEDS CHANGES at iteration 1 (rule C1). This record raises one Minor
# finding of its own. It concurs, under swe-061 7.1 task 2, with INSP-098 finding-1 (CS-18, Major, Open), which by
# the template finding rules is cited and not raised again; the assurance lens cannot confirm conformance to the
# coding standard while that Major is open, and its fix changes the product blobs, so a delta iteration of both
# records follows (SA-A3). Iteration 2 verifies INSP-098 finding-1 at the new blobs and re-checks this record's
# tasks on the changed lines
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: both reviews are NEEDS
# CHANGES; the five rustos blobs exist only on the unmerged rustos branch cwht/wp-sw-02 and the checklist applied
# only on cr/CR-012-pdr-checklist-templates (lead SE convention of 2026-09-27); INSP-098 does not yet name this
# record (paired_record, assurance_reviewer_agent, assurance_verdict; each reviewer updates only its own record).
# The software lead sets verdict in the commit that brings the blobs to a configuration cwht consumes (the owner's
# merge and the PCR-4 pin-move CR), or the commit right after it
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 1
findings_open: 1
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 1
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 3", "swe-135 7.1 task 5", "swe-135 7.1 task 6", "swe-134 7.1 task 2", "swe-087 7.1 task 4", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 4", "swe-052 7.1 task 2", "swe-192 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 3", "swe-081 7.1 task 2", "swe-187 7.1 task 1", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: [a, e, f, g, h, i, j, k]
deferred_rids: []
items_no: ["swe-061 7.1 task 2", "swe-062 7.1 task 1", SA-D1]
effort_turns: 32
effort_minutes: 60
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
