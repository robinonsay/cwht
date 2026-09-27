---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the code review INSP-096
# (docs/reviews/PDR/checklists/code-wp-sw-09.md, iteration 1 by reviewer:WP-PDR-41-code, main 9d3734c), which
# names this path in assurance_reviewer_agent. PDR work plan WP-PDR-41 names the record ("Records:
# code-wp-sw-<nn>.md and -software-assurance.md per WP"; "Reviewer: independent code reviewer ... and SA").
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged).
# The `checklist` field names peer-review-checklist-code revision B, the checklist INSP-096 names, because
# tools/validate_docs.py fails a record whose `checklist` names a template absent from main, and the lead SE
# convention of 2026-09-27 does not change the validator. `assurance_checklist` names the template actually
# applied (the form of INSP-048, INSP-049, INSP-051 and INSP-070).
# id: the brief assigned no id; INSP-100 is the highest id on main, on every cr/ branch and in the working tree
# (2026-09-27); 101 is left for the sibling WP-SW-11 pair filed in the same wave, and 102 is taken here
id: INSP-102
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-09-software-assurance.md
product: "rustos cwht/wp-sw-09: api/src/irq/mod.rs, firmware/pico2/src/irq/mod.rs, firmware/pico2/src/critical_section.rs, firmware/pico2/link.ld and the vector table of firmware/pico2/src/lib.rs (WP-SW-09)"
# product_commit and product_files (iteration 2): equal to INSP-096 iteration 2 (readiness R1; rule C2): rustos branch
# head cwht/wp-sw-09 c6e5100 (the INSP-096 finding-1 fix on the merge 8b67385 of cwht/wp-sw-11 4a8e825 into 9305f59).
# The eleven rustos blobs equal git rev-parse c6e5100:<path> and git rev-parse cwht/wp-sw-09:<path> and exist only on
# unmerged rustos branches; the three cwht blobs equal git rev-parse HEAD:<path> and git hash-object <path> at cwht HEAD
# 0be8bab (checked 2026-09-27). The iteration 1 list is kept in product_files_iteration_1
product_commit: "c6e5100b237a5995c2ec9852b8f8b340fc3b506b"
product_files: ["docs/decisions/adr/ADR-052-wp-sw-09-interrupts.md@58c06b4f4c2866332065520d296a4a7494113a5c", "docs/sprints/SW-02-wp-sw-09-interrupts.md@e02db842240d91cad7ab066f2543297efb3addb9", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:firmware/pico2/src/lib.rs@1f3a4c919e3ca69f3ac2ab06f49d11aa9d808383", "rustos:firmware/pico2/src/irq/mod.rs@7f395b2732727a5a68d7a97a52577044198dc870", "rustos:firmware/pico2/src/irq/vectors.rs@8034c93a4cbf3f6de11ad1767c7d8b143820f165", "rustos:firmware/pico2/src/critical_section.rs@1f7e011a2f1383b1627f814591726fd937f81320", "rustos:firmware/pico2/link.ld@f157f6fa1016b7032c89a3f05db8282d2123c336", "rustos:api/src/irq/mod.rs@260fa0a6ff3eef4bff31511a726ca0577267a248", "rustos:api/src/lib.rs@12d5d0ef9e672bcc1791f4086c9825798535d6a7", "rustos:api/tests/irq_contract.rs@9f118d179919c8801e41346f836f03a52b12bf50", "rustos:firmware/pico2/src/common/board.rs@7a88c173087b85a8e69347a70f5c6d174d48e6a6", "rustos:firmware/pico2/src/common/reg.rs@f0b8f8732b516609444594dc73b3dc7a317bc19a", "rustos:firmware/pico2/src/common/reg/fake.rs@02e31cf54132c43b9dfba6607e1bc2ed6786d22f"]
# product_commit at iteration 1: 9305f593c50f338652dac18f6308d088b083b621
product_files_iteration_1: ["docs/decisions/adr/ADR-052-wp-sw-09-interrupts.md@f1ee2e75ae027ffe868366ffeaef417f2a7b19b3", "docs/sprints/SW-02-wp-sw-09-interrupts.md@4adccaf6954561d621236fd72c9d476f16d598dc", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/irq/mod.rs@260fa0a6ff3eef4bff31511a726ca0577267a248", "rustos:api/src/lib.rs@12d5d0ef9e672bcc1791f4086c9825798535d6a7", "rustos:api/tests/irq_contract.rs@9f118d179919c8801e41346f836f03a52b12bf50", "rustos:firmware/pico2/link.ld@f157f6fa1016b7032c89a3f05db8282d2123c336", "rustos:firmware/pico2/src/critical_section.rs@1f7e011a2f1383b1627f814591726fd937f81320", "rustos:firmware/pico2/src/irq/mod.rs@f1366bfc74315d2d539da8f2b61106f2b1bc3959", "rustos:firmware/pico2/src/lib.rs@6008ddba48a8af1106e4607363bdec1321f7bf54", "rustos:firmware/pico2/src/common/board.rs@7a88c173087b85a8e69347a70f5c6d174d48e6a6", "rustos:firmware/pico2/src/common/reg.rs@f0b8f8732b516609444594dc73b3dc7a317bc19a", "rustos:firmware/pico2/src/common/reg/fake.rs@02e31cf54132c43b9dfba6607e1bc2ed6786d22f"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/code-wp-sw-09.md@62da3b111a3909ab4bb89347624a4c9fd978c3f0 (INSP-096 iteration 1)", "docs/reviews/PDR/checklists/code-wp-sw-09.md@815e1e685d321e432b279d5f5331c0c12375570d (INSP-096 iteration 2)", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8 (sections 2.1.1, 7, 14, 15, 19)", "docs/safety/hazards.json@81cacde47d4f2066ecac3947f3acf65e646b1ad0 (HZ-004)", "docs/safety/hazard-analysis.md (section 7 row l)", "docs/plan/pdr-work-plan.md (WP-PDR-41, section 5)", "docs/research/rustos-toolchain-proof.md (F8)", "docs/risk/register.md (RSK-013, RSK-023, RSK-063)"]
paired_record: INSP-096
# product_type: code (07 section 2.1.1 row "Code": Yes for a safety-critical component, and Yes for every file that
# contains unsafe; both hold here). Task set applied: the section B row "Every product type"; the section B row
# "code"; the section 7.1 tasks of the SWEs ADR-052 cites as guidance (SWE-134, SWE-219, SWE-220, already in the code
# row); and the section E tasks (SWE-087, SWE-088, SWE-089, SWE-080, SWE-081) (07 section 15)
product_type: code
# criticality: safety-critical by inheritance: 07 section 14.1 drivers row names the critical section among the
# drivers the safety-critical components depend on, and the SW-SCHED row names "the pico2 reset handler, vector
# table and NVIC plumbing" (SWE-134 items a, c, f, j, k, l for SW-SCHED, 07 section 14.2 module table)
criticality: safety-critical
product_size: "iteration 1: 1027 lines added and 3 removed in 9305f59 (about 620 non-test lines; 12 developer tests and a 189-line contract draft); ADR-052 89 lines; SW-02 61 lines; 13 product files. Iteration 2 delta: 8b67385..c6e5100 172 insertions and 144 deletions in 3 files (irq/vectors.rs 163 new); ADR-052 and SW-02 27 changed lines; sprint index 5 rows; 14 product files"
sprint: SW-02-wp-sw-09-interrupts
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "sa-reviewer:WP-PDR-41-wp-sw-09 (iterations 1 and 2)"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-wp-sw-09 (software assurance function; paired file review INSP-096 by reviewer:WP-PDR-41-code)"
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 2 (rule C1): zero Major findings under the assurance
# lens. Iteration 1 findings 1 to 3 (Minor) are not addressed by revision 2 (ADR-052 section 8) and become liens under
# rule C1; the delta raises one new Minor (finding-4, a CS-27 nursery lint on the new irq/vectors.rs), also a lien.
# Liens: owner the firmware developer, due at the CDR readiness declaration
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES at iteration 2: (a) cleared:
# INSP-096 is reviewer_verdict APPROVED at iteration 2 (finding-1 Verified at c6e5100); (b) open: the eleven rustos
# blobs exist only on unmerged rustos branches and the checklist applied only on cr/CR-012-pdr-checklist-templates
# (lead SE convention of 2026-09-27, INSP-031 practice); (c) in part: INSP-096 names this record (paired_record
# INSP-102) but still carries assurance_verdict pending (X-1). The software lead sets APPROVED on both records when
# they clear; a blob change before then needs a further delta iteration of both records (rule C2)
verdict: NEEDS CHANGES
findings_major: 0
# findings (iteration 2): finding-1 to finding-3 (iteration 1) and finding-4 (new at iteration 2) are Open as liens
# under rule C1, due at the CDR readiness declaration (not Deferred RIDs)
findings_minor: 4
findings_open: 4
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 4
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 3", "swe-135 7.1 task 4", "swe-135 7.1 task 5", "swe-135 7.1 task 6", "swe-135 7.1 task 7", "swe-134 7.1 task 2", "swe-087 7.1 task 4", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 1", "swe-081 7.1 task 2"]
# swe134_items_checked: the SW-SCHED items of 07 section 14.2 (a, c, f, j, k, l), which cover the vector table and
# NVIC plumbing, plus the drivers-row items this package can carry; b, d, e, g, h, i are answered N/A in section C
swe134_items_checked: [a, c, f, j, k, l]
deferred_rids: []
# items_no (iteration 2): swe-135 7.1 task 3 is No on finding-4
items_no: ["swe-134 7.1 task 2", "swe-087 7.1 task 4", "swe-135 7.1 task 3", SA-C-a, SA-C-c, SA-C-k, SA-C-l]
# effort: iteration 1 (44 turns, 80 min) plus iteration 2 delta (30 turns, 45 min)
effort_turns: 74
effort_minutes: 125
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-102: software assurance pair of INSP-096, code review of WP-SW-09 interrupts and critical section (rustos `cwht/wp-sw-09` at `9305f59`)

**Product.** rustos branch `cwht/wp-sw-09` at `9305f59` (parent `cwht/wp-sw-11` `213c536`), the ten rustos blobs of `product_files`, and ADR-052, SW-02 and the sprint index on cwht `main`. Identity checked with `git rev-parse 9305f59:<path>` in the rustos repository and `git rev-parse HEAD:<path>` and `618e441:<path>` in cwht: all thirteen equal INSP-096. `git rev-parse cwht/wp-sw-09` is still `9305f59`, so the product has not moved since INSP-096.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Readiness, sections A to F and the task table are applied. `product_type` code, `criticality` safety-critical.

**Acceptance criteria (rule C7).** Every task of the section B rows "Every product type" and "code"; the section 7.1 tasks of SWE-134, SWE-219 and SWE-220 (cited by ADR-052) and of SWE-087, 088, 089, 080 and 081 (section E); the SW-SCHED SWE-134 items a, c, f, j, k and l of 07 section 14.2, since 07 section 14.1 puts "the `pico2` reset handler, vector table and NVIC plumbing" in SW-SCHED; the HZ-004 software causes that the interrupt plumbing can contribute to (SWEHB `swe-205` section 7.7.2 walk); each INSP-096 finding (finding-1 to finding-6) re-read under the assurance lens; each `unsafe` site of the package re-read for the assumption it makes about the interrupt model; the two ADR-052 assumptions.

**Independence (rule C4).** This invocation (`sa-reviewer:WP-PDR-41-wp-sw-09`) authored no part of WP-PDR-41, of the rustos branches or of ADR-052 and SW-02, wrote no part of INSP-095 to INSP-099, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "software assurance peer review record pair template assurance_tasks_applied SWEHB"; "HardFault handler DefaultHandler safe state outputs unhandled interrupt spin loop watchdog"; "OnHardFault overridable fault handler application safe_state rustos pico2"; "RP2350 bootrom state on entry to image NVIC interrupts disabled VTOR launch flash image"). `grep -n` and read-only scripts were used afterwards only to pin lines, extract the SWEHB section 7.1 lists and find the highest `INSP` id. The rustos code was read with `git show` and in a detached scratch worktree of `9305f59` created from the rustos repository under the session scratchpad and removed afterwards; the owner's rustos working tree was not read. LTspice was not run. Nothing was downloaded or installed.

**Lead SE convention.** The ten rustos blobs exist only on the unmerged rustos branch `cwht/wp-sw-09`. This record sets `reviewer_verdict` and `assurance_verdict` on its own, holds `verdict`, and is committed on `main`. The software lead sets `verdict` when the blobs reach a configuration cwht consumes (the owner's merge and the PCR-4 pin-move CR), in that commit or the commit right after it.

## Assurance re-runs and checks

| # | Check | Result |
|---|---|---|
| S0 | Blob identities: `git rev-parse 9305f59:<path>` for the ten rustos entries; `git rev-parse HEAD:<path>` and `618e441:<path>` for the three cwht entries; `git rev-parse cwht/wp-sw-09`; `git diff --stat 213c536 9305f59` | all thirteen equal INSP-096; branch head `9305f59`; 10 files, 1027 insertions, 3 deletions |
| S1 | `cargo +1.98.0 test --offline -p pico2 --lib` and `-p api --test irq_contract` in the scratch worktree | pico2 46 passed; `irq_contract` 4 passed; none ignored |
| S2 | `cargo +1.98.0 llvm-cov --offline -p pico2 --lib --summary-only` (host coverage, stable toolchain) | `irq/mod.rs` 144 of 144 regions, 77 of 77 lines, 12 of 12 functions; `critical_section.rs` 116 of 117 regions, 72 of 73 lines, 13 of 13 functions. The one missed region is the closure `\|w\| *w = 98` of the test `nested_access_to_the_same_cell_is_busy_and_harmless` (line 181), which is correct by design: the `Busy` path must not run `f`. Every host-compiled flight region is covered |
| S3 | Eight mutants of the host-compiled decisions and register arithmetic, each by exact text substitution and a full `-p pico2 --lib` run, the file restored by `git checkout` after each: M1 `line >= LINES` to `>`; M2 word stride `* 4` to `* 8`; M3 bit `line % 32` to `% 31`; M4 `read_line` ignores the word offset; M5 `replace` without the borrow check; M6 `with_mut` never clears the flag; M7 `with_mut` checks the flag without setting it; M8 `LINES` 52 to 64 | all eight killed (2, 4, 3, 1, 1, 3, 1 and 2 failing tests). The single-condition decisions of `locate`, `replace` and `with_mut` have both outcomes exercised, so decision coverage equals MC/DC for them (07 section 9.6) |
| S4 | `rust-code-analysis-cli -m -O json` over the four package source files, then `tools/complexity_gate.py --max 15 --yellow 12` | PASS; MSR-17 66 functions, max CC 13 (`api/tests/irq_contract.rs:48` `check_out_of_range`, test code, yellow), none above 15; the two CS-19 "cycle" reports (`new -> new`, `replace -> replace`) are name-based matches of `UnsafeCell::new` and `Cell::replace` or `mem::replace`, not recursion |
| S5 | `tools/unsafe_audit.py --write` into a scratch audit file with `--root` the worktree and `--audited firmware/pico2 --audited api` | 46 sites, 0 without `SAFETY`. The seven new sites are rows 9 to 13 (`critical_section.rs:60`, `:67`, `:99`, `:123`, `:143`), row 23 (`irq/mod.rs:305`, the `interrupt!` `no_mangle`) and row 43 (`lib.rs:651`, the extern block). The tool records row 23 with enclosing name `tests` (it is the macro, not the test module): cross item X-5. The "forbidden" failures come from the scratch root layout (the default forbidden roots are cwht crates) and are not product results |
| S6 | `cargo +1.98.0 clippy --offline -p pico2 --target thumbv8m.main-none-eabihf -- -W clippy::pedantic -W clippy::nursery`, filtered to the package files | only `semicolon_if_nothing_returned` at `critical_section.rs:61` and `:68`, as INSP-096 finding-6; no nursery lint on the package |
| S7 | Reading of the vector table and fault handlers at `9305f59` (`lib.rs:510-534`, `:580-586`; `link.ld` `PROVIDE` block) | `DefaultHandler` and `OnHardFault` are strong `#[unsafe(no_mangle)]` definitions in `pico2` whose bodies are `loop {}`; slot 2 (NMI), slots 4 to 15 and, through the 52 new `PROVIDE` defaults, every device slot without an application handler land on `DefaultHandler`. `link.ld` provides no `PROVIDE` for `DefaultHandler` or `HardFault`, so an application cannot replace either (finding-1) |
| S8 | `Rp2350Nvic::new` (`irq/mod.rs:244-252`) against IRQ-6 and SWE-134 a; the planned dev-board check of ADR-052 section 4.3 | `new` writes no register and relies on "every line is disabled and not pending out of reset". No datasheet clause for the state the bootrom leaves at image entry is cited, and the dev-board check list does not read the lines back after power-on or after a watchdog reset. The six target-only method-to-register bindings (`enable` to `ISER`, `disable` to `ICER`, and so on) are not compiled on the host, so no host test would catch a swapped binding (finding-2) |
| S9 | `CsCell::replace` error path (`critical_section.rs:111-124`) under 07 section 14.2 row k | on `Busy` the offered value is dropped (doc: "the cell is unchanged and `value` is dropped"). The ADR-052 example cell holds a driver object (`Option<Rp2350Alarm<1>>`), built from a one-per-boot `DeviceHandle`, which would then be lost for the rest of the boot (finding-3) |
| S10 | HZ-004 `causes` in `docs/safety/hazards.json` (blob `81cacde4`) against the interrupt plumbing | C5 "Firmware hung or a task stalled with TX_KEY high" covers a spin in a fault vector or an over-long critical section; its controls are the watchdog (REQ-SYS-131, 2 s) and the hardware PA-enable cutoff (REQ-SYS-055). No new hazard cause is introduced by the package |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-c, SA-C-l) | rustos `firmware/pico2/src/lib.rs:510-534` (`DefaultHandler`, `OnHardFault`, blob `6008ddba`), `:581-584` (table fill); `firmware/pico2/link.ld` `PROVIDE` block (blob `f157f6fa`); ADR-052 section 2 item 1 | The fault and default vectors cannot be routed to the safe state by the application. 07 section 14.2 row l requires `safe_state()` to be "invoked by ... every fault handler", and row c requires every termination path to call it first. After this package, the vector table sends HardFault to `OnHardFault`, and NMI, the other system exceptions and every device line enabled without an `interrupt!` handler to `DefaultHandler`. Both are strong `pico2` symbols whose bodies are `loop {}`, and `link.ld` gives no `PROVIDE` default for them, so `cwht-app` cannot install a handler that writes the safe-state registers first (CS-12 style). On such a fault, `TX_KEY` and `PA_EN` keep their last value until the watchdog resets the chip. The hazard data covers this as HZ-004 C5 (firmware hung with `TX_KEY` high): the watchdog (2 s, REQ-SYS-131) and the hardware cutoff (REQ-SYS-055) bound it, and the reset leaves the safe outputs held by the external pull-downs. So no safety conclusion changes, and the severity is Minor. But the provision of row l cannot be implemented on this vector table, and the package is the one that defines how vectors are overridden (ADR-052 section 2 item 1). Fix: give `DefaultHandler` and the HardFault vector overridable symbols with the same mechanism as the device lines (for example `PROVIDE(HardFault = OnHardFault)` and `PROVIDE(DefaultHandler = DefaultHandler_)`, with slot 3 and the fill value pointing at the provided names, the `cortex-m-rt` convention), plus a checked macro that accepts only a `fn() -> !`. Record in ADR-052 that cwht overrides both with handlers that call the `pico2` safe-state register writes and then request a watchdog reset. Until the fix, state in ADR-052 section 4.3 that the fault vectors end in a spin that only the watchdog ends (cross item X-4) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-a); `swe-062 7.1 task 1` | rustos `firmware/pico2/src/irq/mod.rs:244-252` (`Rp2350Nvic::new`, blob `f1366bfc`), `:259-282` (trait impl); `api/src/irq/mod.rs` IRQ-6; ADR-052 section 1 assumptions and section 4.3 dev-board check | The known state of the interrupt lines at every start and restart (SWE-134 a, SW-SCHED row a) rests on an unconfirmed assumption. `new` writes no register and claims IRQ-6 ("every line is disabled and not pending out of reset"). The bootrom runs before the image, and a restart can come from a watchdog reset or the restart-to-bootloader path of `ICD-CTL-USB`. ADR-052 does not list this as an assumption and cites no datasheet clause for the NVIC state at image entry. The planned dev-board check covers pend, enable and one-priority order, but it does not read `ISER` and `ISPR` back at construction after power-on, after a watchdog reset or after a debugger reset. IRQ-6 is checked only against the reference model of `irq_contract.rs`. Also, the six target-only method-to-register bindings are not host-compiled (S8), and the dev-board list does not exercise `unpend`, `is_enabled` and `is_pending`, so a swapped binding has no test at all. Fix (either): make IRQ-6 hold by construction, with `new` writing all ones to `ICER0/1` and `ICPR0/1` (four straight-line writes, CS-38 compatible) and a host test of that write sequence through `Regs`; or add IRQ-6 as ADR-052 assumption 3 with its datasheet basis, and add to the dev-board check a read-back of every line after each reset kind. In both cases, extend the dev-board check to call each of the six methods once and read the register effect back (cross item X-6) | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-k) | rustos `firmware/pico2/src/critical_section.rs:109-124` (`CsCell::replace`, blob `1f7e011a`) | `replace` drops the offered value when it returns `Busy`. 07 section 14.2 row k says no error is silently discarded. The error is reported, but the value is discarded with it. The documented use (ADR-052 section 2 item 4 and the module example) moves a driver object built from a one-per-boot `DeviceHandle` into a cell. A `Busy` there loses that driver for the rest of the boot, and the caller cannot retry or reach the safe-state path with it. `Busy` arises only from a nested access in the same context, a programming defect, so no hazard follows today. Fix: return the value with the error, for example `Result<T, (Busy, T)>` or a `Busy<T>` carrying it (the `RefCell::try_replace` direction), with a host test that the value comes back unchanged | Open | Pending | |

**Paired record findings under the assurance lens (not raised again; template finding rules).**
- INSP-096 finding-1 (CS-18, `lib.rs` 704 lines): concur at the paired record's severity. No assurance aspect beyond maintainability of the vector table. The move it proposes (the 52 entries and their extern block into the `irq` module) is also the natural place for the finding-1 fix above.
- INSP-096 finding-2 (`Mmio` SAFETY text and the NVIC window): concur at Minor. Under the assurance lens, the unmasked `offset & 0x3ffc` window from `RegAddr::NVIC` reaches `NVIC_IPR0` (`+0x300`), whose write would break CS-34, and the SCB `AIRCR` (`+0xc0c`), whose write can reset the chip. CS-34 then rests only on the four offset constants and `no_priority_register_is_ever_addressed`, which S3 and INSP-096 C7 confirm. The severity does not rise. The fix option "mask NVIC offsets to that window in `address`" is preferred, because it makes CS-34 hold at the only integer-to-pointer site.
- INSP-096 finding-3 (CS-10 wording against the two `asm!` blocks): concur at Minor. The two blocks are the CS-09 masking site. Their SAFETY arguments (not `nomem`, so a compiler barrier; `PRIMASK` restored to the value read) are correct for single-core use.
- INSP-096 finding-4 (`CsCell` SAFETY omits NMI and HardFault): concur at Minor, with one addition. When finding-1 above is fixed, an application HardFault handler will exist, so the added SAFETY text must also say that the fault handlers write only the safe-state registers and never touch a `CsCell`.
- INSP-096 finding-5 (`critical_section::with` placement against the 07 section 19 row): concur at Minor. The assurance aspect is testability. `cwht-core` code that shares state with a handler cannot name `with` on the host, so the host tests of that sharing need the pattern WP-PDR-32 is to define (cross item X-3).
- INSP-096 finding-6 (pedantic lint; SW-02 claim): concur at Minor (S6 reproduces it).

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the code review of a driver package of the safety-critical components (07 section 14.1 drivers row and SW-SCHED row). Dispatched by plan WP-PDR-41 ("Reviewer: ... and SA") and by INSP-096 `assurance_reviewer_agent` | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed by this record against 07 section 15, the project's software assurance plan. The NASA-STD-8739.8 part is relieved (`rmm.json` SWE-022 T) | | none |
| swe-060 7.1 task 1 | | Yes | The code implements ADR-052 section 2 items 1 to 4: 52 `PROVIDE` defaults and slots 16 to 67 (INSP-096 C7, all 52 agree); `InterruptController` with six methods and no priority operation; `Rp2350Nvic` with one access per call and lines above 51 rejected first (S3 M1, M8); `with` and `CsCell` as stated. The one departure from 07 section 19 is INSP-096 finding-5 (concurred) | | none (INSP-096 finding-5) |
| swe-060 7.1 task 2 | | Yes | No function outside the design: every `pub` item (`Irq`, `Irq::line`, `LINES`, `NoSuchLine`, `Rp2350Nvic`, `interrupt!`, `with`, `CriticalSection`, `CsCell`, `Busy`) is named in ADR-052 section 2 or 4.2. The `pub(crate)` helpers `locate`, `write_line` and `read_line` are the CS-38 host-compilable decision functions | | none |
| swe-061 7.1 task 1 | | Yes | The coding standard is 07 section 7 (CS-01 to CS-39), normative for "the rustos crates as used by cwht" (07 section 7 preamble) and applied by INSP-096 with `peer-review-checklist-code.md` revision B | | none |
| swe-061 7.1 task 2 | | Yes | Conformance analyzed by INSP-096 and re-checked here (S4, S5, S6). Non-conformances: CS-18 (INSP-096 finding-1), CS-10 (finding-3), CS-27 pedantic (finding-6), CS-06 text (findings 2 and 4). No `static mut`, no `transmute`, no `union`, no priority write (CS-09, CS-10, CS-34) | | none (INSP-096 findings 1 to 4, 6) |
| swe-207 7.1 task 1 | | Yes | 07 section 7.6 (CS-29 to CS-33) holds secure-coding practices, and the code checklist section G applies them | | none |
| swe-185 7.1 task 1 | | Yes | Independent analysis S3 to S6. The only input crossing the boundary is the line number, validated by `locate` before any access (S3 M1, M8; CS-29). There are no buffers, no parsing and no dynamic dispatch. The unsafe sites all carry SAFETY text (S5) | | none |
| swe-135 7.1 task 1 | | Yes | Independent static analysis: clippy default, pedantic and nursery on the target (S6); complexity (S4); unsafe scan (S5); host coverage (S2); mutation of the decisions (S3) | | none |
| swe-135 7.1 task 2 | SC | Yes | clippy is run with the 07 CS-27 lint set (INSP-096 C4 and S6), and `tools/unsafe_audit.py` checks CS-06 (S5). The `firmware/Cargo.toml` `[workspace.lints]` do not reach rustos crates, so the rustos lint set is the one INSP-096 C4 applied on the command line | | none |
| swe-135 7.1 task 3 | | Yes | The static-analysis results are addressed: the pedantic lint is INSP-096 finding-6. The complexity yellow is in test code and needs no action (CS-17). No unsafe site lacks SAFETY text | | none |
| swe-135 7.1 task 4 | | Yes | Security scan: clippy and the unsafe audit (S5, S6). `cargo audit` and `cargo deny` are not needed, because there is no dependency change (the manifests are untouched, CS-02; INSP-096 CK-CODE-A2) and the advisory database download is not permitted. `cargo geiger` is replaced by S5 for the new sites | | none |
| swe-135 7.1 task 5 | SC | Yes | SWE-219 coverage verified, see the swe-219 row. No coverage waiver is needed or on record | | none |
| swe-135 7.1 task 6 | SC | Yes | SWE-220 complexity verified, see the swe-220 rows. No waiver is needed (07 section 14.3) | | none |
| swe-135 7.1 task 7 | | Yes | The quality thresholds are defined in 07: `-D warnings` with pedantic and nursery promoted to deny in the gate (CS-27), CC 15 with yellow 12 (CS-17), 0 unsafe sites without SAFETY (CS-06), and 100 percent region coverage for safety-critical code (07 section 14.1) | | none |
| swe-134 7.1 task 2 | SC | No | Section C answers for the SW-SCHED items a, c, f, j, k and l at code maturity. Items f and j hold. Item a rests on an unconfirmed reset-state assumption (finding-2). Items c and l cannot be provided for the fault vectors (finding-1). Item k discards a value on `Busy` (finding-3) | | finding-1, finding-2, finding-3 |
| swe-134 7.1 task 3 | SC | N/A | The package holds no loaded data. The vector table is code addresses fixed at link time, not a safety-critical loaded parameter | section B code row condition ("for code that holds safety-critical loaded data"); 07 sections 9.7 and 14.1 (configuration guard record and firmware image only) | none |
| swe-087 7.1 task 4 | SC | No | The same evidence as swe-134 7.1 task 2, for this code inspection | | finding-1, finding-2, finding-3 |
| swe-062 7.1 task 1 | SC | Yes | The unit tests run and pass (S1; INSP-096 C1, C3 Miri clean). The host-compiled decisions are discriminated (S3: 8 of 8 mutants killed). The target-only bindings and IRQ-6 on silicon have no test yet, which is finding-2 | | finding-2 |
| swe-062 7.1 task 2 | | Yes | Unit testing found no defect. The defects found by review are tracked as INSP-096 findings 1 to 6 and findings 1 to 3 here, each with a fix route. The contract-test independence item (SW-02 phase 2 open item) is tracked in SW-02 and INSP-096 R5 | | none |
| swe-219 7.1 task 1 | SC | Yes | 100 percent region coverage of every host-compiled flight region (S2). The target-only code (`with`, the six trait methods, `Rp2350Nvic::new`, the macro expansion and the table) is straight-line by CS-38 and has no host coverage. Its disposition is the 07 section 22 "target-only coverage disposition" item of WP-PDR-47, and its evidence is the dev-board check (extended by finding-2). MC/DC equals decision coverage for the three single-condition decisions (S3) | | none |
| swe-220 7.1 task 1 | SC | Yes | Measured independently (S4): 66 functions, max CC 13 (test code) | | none |
| swe-220 7.1 task 2 | SC | Yes | No function of the package is above 15. The flight functions are at most 12, and there are no target-only decisions (CS-38; S4 `target_only_above_1 0`) | | none |
| swe-087 7.1 task 1 | | Yes | INSP-096 iteration 1 was performed and recorded. This record is its SA pair | | none |
| swe-087 7.1 task 2 | | Yes | INSP-096 findings are Open with a fix route (iteration 2 delta on a new frozen commit for finding-1). None is closed without evidence | | none |
| swe-088 7.1 task 1 | | Yes | INSP-096 met SWE-088 a to d: checklist revision B answered item by item (a), readiness R1 to R6 stated (b), findings with state (c), participants named (d) | | none |
| swe-088 7.1 task 2 | | Yes | The actions are tracked in the INSP-096 findings table and in the cross items below, each with an owner | | none |
| swe-089 7.1 task 1 | | Yes | INSP-096 and this record carry `findings_*`, `items_no`, `unsafe_sites_reviewed` (INSP-096), `effort_turns`, `effort_minutes` and `iteration` | | none |
| swe-080 7.1 task 1 | SC | Yes | Impact on safety of the rustos change: it adds interrupt entry, the NVIC enable path and the masking primitive. No new hazard cause (S10). The weak points are finding-1 (fault-vector termination) and finding-2 (reset state). There is no security impact: no new external interface (07 section 16) | | finding-1, finding-2 |
| swe-080 7.1 task 2 | | Yes | a: tracked on rustos branch `cwht/wp-sw-09` and in SW-02. b: the cwht baseline is unchanged until the owner's merge and the PCR-4 Class I pin-move CR (plan section 6.2), which carries the approval. c: phase 1 complete (SW-02). d: host tests run (S1); dev-board check pending (SW-02 phase 5) | | none |
| swe-080 7.1 task 3 | | Yes | The route is the plan's: a cwht/ branch in the rustos repository, never pushed or merged by an agent, owner merge as maintainer (OD-23), and pin move by CR (PCR-4). The cwht records (ADR-052, SW-02) are on `main` as Record-class files | | none |
| swe-081 7.1 task 1 | | Yes | Every reviewed file is identified by path and blob (front matter). The rustos pin in `firmware/Cargo.toml` and `tools/toolchain.lock.md` moves only by PCR-4 | | none |
| swe-081 7.1 task 2 | SC | Yes | The safety-critical code stays under configuration control: the branch commit is frozen (S0), and the unsafe audit list is regenerated and signed on the pin-move CR branch (CS-07; INSP-096 CK-CODE-B7). Hazard data is unchanged by the package | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | S0: all thirteen blobs equal INSP-096; the branch head has not moved |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | Row "Code", Yes for a safety-critical component and for files with `unsafe`. Criticality safety-critical by the 07 section 14.1 drivers row (critical section) and the SW-SCHED row (vector table and NVIC plumbing) |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with a scratch `--output` shows no violation for the ids touched | Yes | The product touches no requirement, case or hazard id (ADR-052 section 4.1: none), and the rustos code carries no CS-24 tags by plan WP-PDR-41. `validate_docs.py` on `main` passes this record (Commands) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-096 iteration 1 is committed on `main` (`9d3734c`) with `author_agent` "author:WP-PDR-41 wave 1a" and `reviewer_agent` "reviewer:WP-PDR-41-code". This invocation is `sa-reviewer:WP-PDR-41-wp-sw-09` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | Row "Code" of 07 section 2.1.1. The component is safety-critical from the 07 section 14.1 drivers row ("... watchdog, critical section, clocks and PLL ...", `pico2` WP-SW-09) and the SW-SCHED row ("with the `pico2` reset handler, vector table and NVIC plumbing"). Every package file with `unsafe` is also routed there |
| SA-A2 | Yes | Three invocations: author `author:WP-PDR-41 wave 1a`, file reviewer `reviewer:WP-PDR-41-code`, and this assurance reviewer. INSP-096 names this record's path but not yet its id or verdict (X-1) |
| SA-A3 | Yes | Same product, the same `product_commit` `9305f59` and the same thirteen blobs. A change before the merge needs a delta of both records (rule C2) |
| SA-A4 | Yes | INSP-096 applied `peer-review-checklist-code.md` revision B, the checklist 07 section 10.1 and 08 section 3.5 assign to code. Every item is answered with evidence, and N/A items carry a reason |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: the "Every product type" row; every task of the "code" row, with swe-134 task 3 answered N/A with its relief; the section 7.1 tasks of SWE-219 and SWE-220 (cited by ADR-052, and in the code row); and SWE-087, 088, 089, 080 and 081 (section E). `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | The one N/A row (swe-134 task 3, SC) cites the section B code row condition and 07 sections 9.7 and 14.1 |
| SA-B3 | Yes | swe-134 7.1 task 2 and swe-087 7.1 task 4 (No) are carried by finding-1, finding-2 and finding-3 |

## C. SWE-134 items a to l

The component items are those of `SW-SCHED` in the 07 section 14.2 module table (a, c, f, j, k, l), which covers the vector table and NVIC plumbing, and the drivers row that inherits them. Items that belong to state machines, commands or I/O data of other modules are N/A for this package.

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | No | Handlers only run once their line is enabled (`interrupt!` doc; ADR-052 section 2 item 1), and `PRIMASK` is restored exactly (`critical_section.rs:67-69`). The start state of the lines at construction is assumed, not established or tested on silicon (finding-2) |
| SA-C-b | N/A | The package holds no state machine. Transitions are the modules' own (07 section 14.2 row b) |
| SA-C-c | No | No termination path is added by the package. The fault vectors it routes (HardFault, NMI, unhandled device lines) end in `loop {}` without the safe-state writes, and the application cannot override them (finding-1). The watchdog backstop of row c ("watchdog expiry") bounds the effect |
| SA-C-d | N/A | No operator override passes through the package |
| SA-C-e | N/A | No command sequencing in the package. `enable` before a handler exists is a design rule of the caller (`interrupt!` doc) |
| SA-C-f | Yes | The vector table is an immutable `static` in `.vector_table` in flash (`lib.rs:580`, SAFETY at `:572-578`). Handler addresses are fixed at link time, and no RAM copy exists to corrupt. `CsCell` state is RAM data whose complement storage, where safety-critical, is the owning module's duty (07 section 14.2 row f) |
| SA-C-g | N/A | The only input is the line number, range-checked in `locate` (S3 M1, M8). No safety-relevant data passes through |
| SA-C-h | N/A | No safety-critical command in the package |
| SA-C-i | N/A | The package cannot produce RF. CS-34 (no priority write, test `no_priority_register_is_ever_addressed`, S3) keeps one handler from preempting another, which supports the single-event argument of 07 section 14.2 row i made by SW-SAFE and SW-KEYER |
| SA-C-j | Yes | One priority, run-to-completion handlers (CS-34), confirmed in code (no `NVIC_IPR` offset reachable through `write_line`, S3). The response-time effect of a masked region, which delays the keyer alarm by the length of `f` (doc of `with`), is a budget item of the SW-SCHED design and the handler timing of CS-22. It is not bounded in this package, which cannot know `f`: cross item X-3 |
| SA-C-k | No | Every method returns `Result` with a single-variant error (`NoSuchLine`, `Busy`). `Busy` on `replace` drops the offered value (finding-3) |
| SA-C-l | No | `with` and the NVIC trait do not prevent the safe-state call from any context: `safe_state()` writes registers directly and needs no `CsCell`, and `with` is callable from a handler. The fault vectors cannot call it (finding-1) |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | The SWEHB `swe-205` section 7.7.2 considerations that apply: 1 (software controls safety-critical hardware: handlers drive `TX_KEY` through the keyer), 14 (new hazard causes from the controls: a preempting handler, prevented by CS-34; a lost update of shared keyer state, prevented by `CsCell`), 16 (common cause: every unhandled vector shares one `DefaultHandler`, finding-1), 20 (recovery if monitoring fails: the watchdog ends a fault-vector spin), and section 7.7.3 "failure to terminate or complete a process in a given time" (masked duration, X-3). Each maps to HZ-004 C5 (firmware hung or task stalled with `TX_KEY` high), whose controls are the watchdog and the hardware cutoff (S10). No new cause needs a `hazards.json` entry. The 07 section 14.2 row c path list should name the fault vectors (X-4) |
| SA-D2 | Yes | The criticality equals the 07 section 14.1 determination (drivers row, inherited; SW-SCHED row for the vector table and NVIC). No component is created or renamed (ADR-052 section 4.2) |
| SA-D3 | N/A | The package traces to no hazard id directly. Its requirement REQ-SYS-129 is met by construction (ADR-052 section 4.1), and the L2 row is written in WP-PDR-35 |
| SA-D4 | N/A | No safety-tagged software requirement is created or changed by the package |
| SA-D5 | N/A | No hazard-tracing software requirement is closed by the package. The dev-board check is `credit: false` (ADR-052 section 4.3) |
| SA-D6 | N/A | The hazard analysis is not re-issued by this product. ADR-052 section 4.3 states "Hazard analysis update required: no", and S10 agrees |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | Iteration 1 of INSP-096. No earlier iteration or lien exists for this package |
| SA-E2 | Yes | INSP-096 and this record carry the 07 section 10.3 measurements |
| SA-E3 | Yes | swe-080 tasks 2 and 3 rows. The rustos change is on a cwht/ branch, and the cwht pin moves only by the PCR-4 Class I CR |
| SA-E4 | N/A | No item under test and no credit run in this product (the dev-board check is `credit: false` and not yet run) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | The assurance concerns that are not defects of this product are existing risks, and no new entry is needed. RSK-063 covers host behaviour diverging from silicon (finding-2 is an instance of it: IRQ-6 and the six bindings are credited only by the reference model and inspection). RSK-013 covers the rustos packages not demonstrated on hardware before CDR (the dev-board check is still unwritten). RSK-023 covers upstream rustos changes breaking cwht (the fault vector symbols are part of the application interface after the finding-1 fix). The WP-PDR-18 writer may cite this record on those entries |
| SA-F2 | Yes | The front matter carries `findings_*`, `assurance_findings_major` 0 and `assurance_findings_minor` 3 (the same findings, counted once, 07 section 10.2), `items_no`, and effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied, the relief used and the cross items are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true. Every task that SA-B1 requires is in the task table. Every applicable item of sections A, C, D, E and F is answered, and the rest are N/A with their reason. There are zero Major findings under the assurance lens. The three Minor findings are Open. They ride with APPROVED (plan rule C1; 08 section 3.2) and go to the author for fixing on the rustos branch together with the INSP-096 fixes. Finding-2 has one part for the test author (X-6). A fix changes blobs of `product_files`, so both records then need a delta iteration (rule C2). If a finding is not fixed before the owner's merge, it becomes a lien due at the CDR readiness declaration, listed in PDR package section 15.

`assurance_verdict: APPROVED`. The record `verdict` stays NEEDS CHANGES. INSP-096 has `reviewer_verdict: NEEDS CHANGES` on its finding-1. The ten rustos blobs are on an unmerged branch, and the checklist applied is on the unmerged CR-012 branch (lead SE convention).

## Cross items (returned to Claude)

- **X-1.** INSP-096 (`code-wp-sw-09.md`) reads `assurance_reviewer_agent: "pending: ..."` and `assurance_verdict: pending`, and it has no `paired_record`. Its reviewer updates it to `paired_record: INSP-102`, names this reviewer and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row).
- **X-2.** After CR-012 merges, the next delta of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `assurance_checklist`. At the owner's merge and the PCR-4 pin move, both records name the merged commit if it differs from `9305f59`.
- **X-3.** For the firmware architecture ADR (WP-PDR-32) and the SW-SCHED design: bound the longest masked region (every `critical_section::with` body) in the handler latency budget of CS-22 and the SWE-134 j timing of the keyer alarm (HZ-004 C5). Also define how `cwht-core` code that shares state with a handler is written and host-tested, given that `with` is target-only (INSP-096 finding-5).
- **X-4.** For the writer of 07 (plan section 5.3: WP-PDR-13 or WP-PDR-47 in its slot) and the hazard analysis writer (WP-PDR-16b): name the HardFault and default (unhandled-interrupt) vectors among the termination paths of 07 section 14.2 row c. State that, until the finding-1 fix, they end in a spin that the watchdog ends (HZ-004 C5). The hazard analysis section 7 row l ("applied on every reset ..., panic and latched fault") then covers them through the watchdog reset.
- **X-5.** For the owner of `tools/unsafe_audit.py`: the `interrupt!` `no_mangle` site (`irq/mod.rs:305`) is recorded with enclosing name `tests`, because the scan takes the next `mod` or `fn` name after a `macro_rules!` body (S5 row 23). The audit list signed under CS-07 should name the macro. This is a tool item, not a product defect.
- **X-6.** For the independent test author of SW-02 phase 2 (`firmware/devcheck/src/bin/irq_check.rs`): take the finding-2 checks into the dev-board check. Read `ISER0/1` and `ISPR0/1` at `Rp2350Nvic` construction after power-on, after a watchdog reset and after a debugger reset. Call each of the six methods once on a spare line and read back the register effect.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git -C /Users/robinonsay/rust/rustos rev-parse 9305f59:<path>` for the ten rustos `product_files`; `git rev-parse cwht/wp-sw-09`; `git diff --stat 213c536 9305f59` | 0 | S0 |
| `git rev-parse HEAD:<path>` and `618e441:<path>` in cwht for ADR-052, SW-02 and `docs/sprints/index.md` | 0 | S0 |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md`; `git rev-parse` of that path and of the branch | 0 | Template revision A, blob `5b135285`, branch `7784672` |
| `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa096 9305f59`; `git worktree remove` at the end | 0 | Scratch worktree; removed after the checks |
| `cargo +1.98.0 test --offline -p pico2 --lib`; `cargo +1.98.0 test --offline -p api --test irq_contract` (scratch `CARGO_TARGET_DIR`) | 0, 0 | S1 |
| `cargo +1.98.0 llvm-cov --offline -p pico2 --lib --summary-only` and `--text` | 0 | S2 |
| Eight mutants by exact text substitution, each followed by `cargo +1.98.0 test --offline -p pico2 --lib` and `git checkout -- <file>` | 101 each | S3: all killed; worktree clean afterwards |
| `rust-code-analysis-cli -m -O json -p <four files>`; `tools/complexity_gate.py --max 15 --yellow 12 --input <json> --root <worktree>` | 0 | S4 PASS |
| `tools/unsafe_audit.py --write --root <worktree> --audited firmware/pico2 --audited api --audit-file <scratch> --date 2026-09-27` | 1 | S5: 46 sites, 0 without SAFETY; failures are scratch-layout artefacts |
| `cargo +1.98.0 clippy --offline -p pico2 --target thumbv8m.main-none-eabihf --message-format short -- -W clippy::pedantic -W clippy::nursery` | 0 | S6 |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-060, 061, 207, 185, 135, 134, 087, 062, 219, 220, 022, 088, 089, 080, 081; `swe-205` section 7.7.2 | 0 | Task texts of the task table and the SA-D1 walk. SC marks follow the template's section B rows |
| `.venv/bin/python tools/validate_docs.py` on `main` | see summary | This record PASS |

## Verdict format

```
ASSURANCE VERDICT: APPROVED
PRODUCT: rustos cwht/wp-sw-09 (ten rustos blobs of INSP-096) with ADR-052@f1ee2e75, SW-02@4adccaf6, docs/sprints/index.md@fb217bcb at 9305f59; PAIRED RECORD: INSP-096
PRODUCT TYPE: code; CRITICALITY: safety-critical (07 section 14.1 drivers row and SW-SCHED row)
FINDINGS:
- [Minor] swe-134 7.1 task 2 (SA-C-c, SA-C-l) DefaultHandler and OnHardFault are strong pico2 spin loops with no PROVIDE default, so the application cannot route the fault vectors through safe_state (07 section 14.2 row l "every fault handler"); bounded by the watchdog (HZ-004 C5).
- [Minor] swe-134 7.1 task 2 (SA-C-a), swe-062 7.1 task 1 IRQ-6 on silicon is assumed, not established; Rp2350Nvic::new writes nothing; the dev-board check reads no reset state and does not exercise all six target-only bindings.
- [Minor] swe-134 7.1 task 2 (SA-C-k) CsCell::replace drops the offered value on Busy, which loses a one-per-boot driver object.
TASKS APPLIED: swe-134 tasks 2 and 5, swe-022 task 1, swe-060 tasks 1 and 2, swe-061 tasks 1 and 2, swe-207 task 1, swe-185 task 1, swe-135 tasks 1 to 7, swe-087 tasks 1, 2 and 4, swe-062 tasks 1 and 2, swe-219 task 1, swe-220 tasks 1 and 2, swe-088 tasks 1 and 2, swe-089 task 1, swe-080 tasks 1 to 3, swe-081 tasks 1 and 2
TASKS N/A (relief): swe-134 task 3 (section B code row condition; 07 sections 9.7 and 14.1)
SWE-134 ITEMS CHECKED: a, c, f, j, k, l
MEASUREMENTS: size=1027 lines added (about 620 non-test), 13 product files; tasks=33; tasks_no=2; mutants=8 (8 killed); host region coverage of flight code 100 percent; turns=44; minutes=80; major=0; minor=3
```

## Iteration 2: software assurance delta on the INSP-096 finding-1 fix (2026-09-27, cwht HEAD `0be8bab`)

**Scope (rules C1 and C2).** Iteration 1 was APPROVED with the verdict held. Revision 2 of the package changed blobs of `product_files` (INSP-096 finding-1 fix), so this is a delta that reads every changed hunk under the assurance lens and re-sets `product_files` to the current blobs. Product: rustos `cwht/wp-sw-09` at `c6e5100` (parent `8b67385`, the merge of `cwht/wp-sw-11` at `4a8e825` into `9305f59`); package delta `git diff 8b67385 c6e5100` (`firmware/pico2/src/irq/mod.rs` 5 added lines, `firmware/pico2/src/irq/vectors.rs` 163 new lines, `firmware/pico2/src/lib.rs` 3 added and 144 removed lines). The merge `8b67385` changes only the four `clocks` files of WP-SW-11 (`git diff --stat 9305f59 8b67385`), which are INSP-095 and INSP-106 scope, not this package. The cwht blobs moved on `main`: ADR-052 `f1ee2e75` to `58c06b4f`, SW-02 `4adccaf6` to `e02db842`, `docs/sprints/index.md` `fb217bcb` to `7ae0cbcc`; each diff was read in full. The other eight rustos blobs are unchanged (`git rev-parse` equal at `9305f59` and `c6e5100`). Checklist as at iteration 1 (template blob `5b135285`, `cr/CR-012-pdr-checklist-templates` still at `7784672`, not merged).

**Independence (rule C4).** This invocation authored no part of WP-PDR-41, of revision 2, of the rustos fix commits or of INSP-096, and edited no product file. The rustos repository was read with `git show` and in two detached scratch worktrees (`c6e5100` and `9305f59`) created under the session scratchpad with `git worktree add --detach` and removed with `git worktree remove` afterwards; the owner's rustos working tree was not read. Two throw-away link applications were built in the scratchpad, outside both repositories, and deleted. **Search first.** `mcp__claude-context__search_code` ran on `/Users/robinonsay/rust/cwht` ("software assurance record iteration 2 delta product_files drifted blobs verdict held") and on `/Users/robinonsay/rust/rustos` ("vector table device interrupts with_device_interrupts DefaultHandler OnHardFault") before any manual search; `grep` afterwards only pinned lines in known paths. LTspice was not run. Nothing was downloaded or installed.

### Assurance re-runs and checks, iteration 2

| # | Check | Result |
|---|---|---|
| T0 | Blob identities: `git rev-parse c6e5100:<path>` and `git rev-parse cwht/wp-sw-09:<path>` for the eleven rustos entries; `git rev-parse HEAD:<path>` and `git hash-object <path>` for the three cwht entries; `git rev-parse cwht/wp-sw-09` | all fourteen equal INSP-096 iteration 2 `product_files`; branch head `c6e5100` |
| T1 | Hunk reading, `git diff 8b67385 c6e5100` and the three cwht blob diffs | every hunk read; see "Hunks read" below |
| T2 | Moved code compared by script between `lib.rs` at `9305f59` and `irq/vectors.rs` at `c6e5100` | extern block of the 52 symbols with its `// SAFETY:` text: byte-identical (52 declarations each); `unsafe impl Sync for Vector` with its SAFETY text: byte-identical; `union Vector`: identical apart from the added `pub(crate)` on the type and its four fields; slot map 16 to 67: 52 of 52 slot numbers and names identical and in the same order |
| T3 | `cargo +1.98.0 test --offline -p pico2 --lib` and `-p api --test irq_contract` at `c6e5100` (scratch `CARGO_TARGET_DIR`) | pico2 49 passed; `irq_contract` 4 passed; none failed or ignored |
| T4 | `cargo +1.98.0 build --offline -p pico2 --target thumbv8m.main-none-eabihf`, dev and `--release` | no warning, no error |
| T5 | Link test, independent of INSP-096 D10: a scratch `#![no_std]` `#![no_main]` binary using `pico2::entry!`, `pico2::interrupt!(SPAREIRQ_IRQ_0, ..)` and `pico2::interrupt!(TIMER0_IRQ_0, ..)`, built `--release` with `-C link-arg=-Tlink.ld` against `9305f59` and against `c6e5100`; `llvm-objdump -s -j .vector_table` and `llvm-nm -n` of the 1.98.0 toolchain | the two `.vector_table` dumps are byte-identical (the diff shows only the file name line). Slot 16 and slot 62 hold `0x10000125` (the two application handlers, folded by the linker to `0x10000124`); slots 2, 3, 4 to 7, 11, 12, 14, 15 and every other device slot hold `0x10000131`; `DefaultHandler` and `OnHardFault` are both at `0x10000130` in both builds (identical code folding) |
| T6 | `cargo +1.98.0 clippy --offline -p pico2 --target thumbv8m.main-none-eabihf -- -W clippy::pedantic -W clippy::nursery` (the iteration 1 S6 command), filtered to the package files | new on the package: `clippy::redundant_pub_crate` (nursery) at `irq/vectors.rs:22` (`pub(crate) union Vector`) and `:48` (`pub(crate) const fn with_device_interrupts`), "pub(crate) ... inside private module" (finding-4). Unchanged: `semicolon_if_nothing_returned` at `critical_section.rs:61` and `:68` (INSP-096 finding-6). The `lib.rs` reports are on lines the package does not add (boot block literals, reset code, the two handler bodies and the table doc), as at iteration 1 |
| T7 | `tools/unsafe_audit.py --write --json --root <worktree> --audited firmware/pico2 --audited api --audit-file <scratch>` at `c6e5100` | 46 sites, 0 without SAFETY (as iteration 1 S5). The two moved sites are rows 24 (`irq/vectors.rs:37`, `impl Sync for Vector`) and 25 (`irq/vectors.rs:110`, the extern block); the `interrupt!` `no_mangle` is now `irq/mod.rs:310`, still recorded with enclosing name `tests` (X-5 unchanged). The CS-05 "forbidden" reports come from the scratch root layout, as at iteration 1 |
| T8 | `rust-code-analysis-cli -m -O json` over `lib.rs`, `irq/mod.rs` and `irq/vectors.rs` at `c6e5100`, then `tools/complexity_gate.py --max 15 --yellow 12` | PASS; 27 functions, max CC 3, `target_only_above_1` 0. `with_device_interrupts` and `handler` are straight-line (CS-38) |
| T9 | `wc -l` at `c6e5100` | `lib.rs` 564, `irq/mod.rs` 394, `irq/vectors.rs` 163 (CS-18 met by the package, as INSP-096 D9) |

### Hunks read

| Blob change | Hunk | Assurance reading |
|---|---|---|
| `irq/mod.rs` `f1366bfc` to `7f395b27` | `#[cfg(target_os = "none")] mod vectors;` and `pub(crate) use vectors::{Vector, with_device_interrupts};` | Target-only, private module, crate-visible re-export: the public API of `pico2` is unchanged. Lines below shift by 5, so `Rp2350Nvic::new` is now `:249-257` and the trait impl `:266-285` (finding-2 locations updated). No host-compiled flight region changes, so iteration 1 S2 and S3 (coverage and mutants of `locate`, `write_line`, `read_line`) still hold for this file |
| `irq/vectors.rs` new `8034c93a` | module doc; `union Vector` with its `Sync` impl; `const fn handler`; `const fn with_device_interrupts`; extern block | Moved text, confirmed by T2 and T5. `handler` coerces a function item of the extern block to `unsafe extern "C" fn()` without calling it, so it needs no `unsafe` and adds no site. `with_device_interrupts` writes slots 16 to 67 only and returns 0 to 15 unchanged, which the byte-identical table confirms. The `Sync` SAFETY text argues from "the table is immutable, lives in read-only flash"; the type is now crate-visible, but it has no interior mutability and exposes no dereference, so the impl is sound for any crate-internal use and the text is sufficient. The two `pub(crate)` items raise a CS-27 nursery lint (finding-4) |
| `lib.rs` `6008ddba` to `1f3a4c91` | `use irq::Vector;` (target-only); removal of the `Vector` union and `Sync` impl; removal of the 52 slot assignments in favour of `irq::with_device_interrupts(t)`; removal of the extern block | `VECTOR_TABLE` keeps its `#[used]`, `link_section` and SAFETY text, and is still a compile-time constant (T5). `DefaultHandler` (`:493`) and `OnHardFault` (`:506`) are unchanged, still strong `#[unsafe(no_mangle)]` definitions with `loop {}` bodies, and slot 3 still names `OnHardFault` (`:558`): finding-1 stands as written, at the new locations |
| ADR-052 `f1ee2e75` to `58c06b4f` | "Date proposed" revision note; section 2 item 1 (the move); section 4.2 design elements (`irq/vectors.rs`); section 4.3 revision 2 evidence; new section 8 revision history | Accurate against T2 to T9. Section 4.3 says the slot-62 link test was not repeated at revision 2; INSP-096 D10 and T5 here both repeat it with a byte-identical result. Section 4.3 claims `clippy::pedantic` clean on the `irq` files, which T6 confirms; it makes no nursery claim, so finding-4 is not a false claim. Section 8 records that the Minor findings of INSP-096 and INSP-102 are not addressed in revision 2 (rule C1). The finding-1 (assurance) interim statement asked of ADR-052 section 4.3 (X-4) is still absent |
| SW-02 `4adccaf6` to `e02db842` | product row; new "Phase 1, revision 2"; phase 3 review line | Accurate. The line "the delta is `git diff 9305f59 c6e5100`" includes the merged WP-SW-11 files; the package delta is `8b67385..c6e5100`, as INSP-096 iteration 2 and this record use. No assurance effect |
| `docs/sprints/index.md` `fb217bcb` to `7ae0cbcc` | five rows: product commit and status for revision 2 | SW-02 row matches `c6e5100`; the other four rows are other packages' records and match their branch tips (`git branch -v`) |

### Re-answered items (iteration 2)

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| R1 | Yes | T0: all fourteen blobs equal INSP-096 iteration 2 `product_files`; branch head `c6e5100` |
| R4 | Yes | INSP-096 iteration 2 is committed on `main` (`134e555`) by `reviewer:WP-PDR-41-code`; this invocation is not that reviewer and authored nothing |
| SA-A2 | Yes | INSP-096 now names this record (`paired_record: INSP-102`) but still reads `assurance_verdict: pending` and names the reviewer `sa-reviewer:WP-PDR-41-code-wp-sw-09`, not this record's `reviewer_agent` (X-1) |
| SA-A3 | Yes | Same product, `product_commit` `c6e5100`, the same fourteen blobs as INSP-096 iteration 2 |
| SA-C-a, c, k, l | No (unchanged) | Revision 2 touches none of the code these items rest on: findings 1 to 3 stand at the updated locations |
| SA-C-f | Yes | The vector table is still an immutable `static` in `.vector_table`, now computed through a `const fn` (T5: identical image) |
| SA-E1 | Yes | Iteration 2 of INSP-096 and of this record; iteration 1 findings carried as liens under rule C1 |
| swe-135 7.1 task 3 | No | The static-analysis results of the new file are not all addressed: T6 finding-4 |
| swe-061 7.1 task 2 | Yes | CS-18 now met by the package (INSP-096 finding-1 Verified; T9). New non-conformance CS-27 nursery (finding-4) |
| swe-219 7.1 task 1 | Yes | `irq/vectors.rs` is target-only and straight-line (CS-38; T8). Its evidence is the linked-table check (T5) and the dev-board check (X-6). Host coverage of `irq/mod.rs` flight code is unchanged (no host-compiled line changed) |
| swe-081 7.1 task 1 | Yes | `product_files` re-set to the fourteen current blobs; the iteration 1 list is kept in `product_files_iteration_1` |
| swe-080 7.1 task 1 | Yes | Impact on safety of revision 2: none. The linked vector table is byte-identical (T5), so no hazard cause or control changes (iteration 1 S10 stands) |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location (blobs at `c6e5100`) | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-c, SA-C-l) | rustos `firmware/pico2/src/lib.rs:493` (`DefaultHandler`), `:506` (`OnHardFault`), `:554-564` (`VECTOR_TABLE`, slot 3 at `:558`), blob `1f3a4c91`; `irq/vectors.rs:48-102` (device slots, blob `8034c93a`); `link.ld` blob `f157f6fa` | As iteration 1: the fault and default vectors cannot be routed to the safe state by the application. Not addressed by revision 2 (ADR-052 section 8). T5 shows `DefaultHandler` and `OnHardFault` folded to one address, so a halted core cannot even tell them apart. The fix of iteration 1 now lands in `lib.rs` (slot 3 and the fill value) and `link.ld` | Open (lien, rule C1) | CDR readiness declaration |
| finding-2 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-a); `swe-062 7.1 task 1` | rustos `firmware/pico2/src/irq/mod.rs:249-257` (`Rp2350Nvic::new`), `:266-285` (trait impl), blob `7f395b27` | As iteration 1: IRQ-6 (every line disabled and not pending at construction) is assumed, not established; the six target-only bindings have no test. Not addressed by revision 2 | Open (lien, rule C1) | CDR readiness declaration |
| finding-3 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-k) | rustos `firmware/pico2/src/critical_section.rs:109-124`, blob `1f7e011a` (unchanged) | As iteration 1: `CsCell::replace` drops the offered value on `Busy`. Not addressed by revision 2 | Open (lien, rule C1) | CDR readiness declaration |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-135 7.1 task 3`; CS-27 | rustos `firmware/pico2/src/irq/vectors.rs:22` (`pub(crate) union Vector`), `:48` (`pub(crate) const fn with_device_interrupts`), blob `8034c93a` | The new file raises `clippy::redundant_pub_crate` (nursery) twice under the iteration 1 S6 command (T6). CS-27 puts `clippy::nursery` among the lints "promoted to deny in the gate", and MSR-07 has threshold 0, so the new file would fail the G1 lint gate once the CS-27 set reaches rustos crates (it is applied on the command line today, iteration 1 swe-135 task 2). At iteration 1 the same items were private in `lib.rs` and raised no nursery lint (S6), so the fix commit introduced it. No safety or behaviour effect. Fix: declare the items `pub` inside the private module (the `pub(crate) use` in `irq/mod.rs` keeps them crate-visible, so the API does not change), or allow the lint on the two items with a stated reason; and report the nursery result in SW-02 next to the pedantic one | Open (lien, rule C1) | CDR readiness declaration |

The paired record's iteration 2 (INSP-096 finding-1 Verified) is concurred with under the assurance lens: T2 and T5 confirm the move changes neither the unsafe sites nor the linked table. The concurrences of iteration 1 on INSP-096 findings 2 to 6 stand; the addition to INSP-096 finding-4 (fault handlers never touch a `CsCell`) still applies when finding-1 here is fixed.

### Cross items, iteration 2

- **X-1 (updated).** INSP-096 names `paired_record: INSP-102`. It still reads `assurance_verdict: pending` and names `sa-reviewer:WP-PDR-41-code-wp-sw-09`; its next edit copies `assurance_verdict: APPROVED` (iteration 2) and uses this record's `reviewer_agent` name.
- **X-2, X-3, X-6.** Unchanged.
- **X-4 (unchanged, still open).** ADR-052 section 4.3 revision 2 does not yet state that the fault vectors end in a spin that only the watchdog ends; the 07 section 14.2 row c path list does not yet name them.
- **X-5 (updated).** The `interrupt!` `no_mangle` site is now `irq/mod.rs:310` and is still recorded with enclosing name `tests` (T7).

### Commands, iteration 2

| Command | Exit | Result |
|---|---|---|
| `git -C /Users/robinonsay/rust/rustos rev-parse c6e5100:<path>`, `cwht/wp-sw-09:<path>` and `9305f59:<path>`; `git rev-parse cwht/wp-sw-09`; `git branch -v --list 'cwht/*'`; `git log --oneline 9305f59..c6e5100`; `git diff --stat 8b67385 c6e5100` and `9305f59 8b67385` | 0 | T0, scope |
| `git rev-parse HEAD:<path>` and `git hash-object <path>` in cwht; `git diff f1ee2e75 58c06b4f`, `4adccaf6 e02db842`, `fb217bcb 7ae0cbcc`; `git diff 8b67385 c6e5100 -- firmware/pico2/src/lib.rs firmware/pico2/src/irq/mod.rs`; `git show c6e5100:firmware/pico2/src/irq/vectors.rs` | 0 | T0, T1 |
| `git -C /Users/robinonsay/rust/rustos worktree add --detach <scratchpad>/rustos-sa102 c6e5100` (and `-r1` at `9305f59`); `git worktree remove --force` at the end | 0 | Scratch worktrees; removed |
| Python comparison of the moved blocks (`lib.rs` at `9305f59` against `irq/vectors.rs` at `c6e5100`) | 0 | T2 |
| `cargo +1.98.0 test --offline -p pico2 --lib`; `cargo +1.98.0 test --offline -p api --test irq_contract` | 0, 0 | T3 |
| `cargo +1.98.0 build --offline -p pico2 --target thumbv8m.main-none-eabihf` and `--release` | 0, 0 | T4 |
| Scratch link application `cargo +1.98.0 build --offline --release --target thumbv8m.main-none-eabihf` with `RUSTFLAGS="-C link-arg=-Tlink.ld"` against each worktree; `llvm-objdump -s -j .vector_table`; `llvm-nm -n`; `diff` | 0 | T5 |
| `cargo +1.98.0 clippy --offline -p pico2 --target thumbv8m.main-none-eabihf --message-format short -- -W clippy::pedantic -W clippy::nursery` | 0 | T6 |
| `.venv/bin/python tools/unsafe_audit.py --write --json --root <worktree> --audited firmware/pico2 --audited api --audit-file <scratch> --date 2026-09-27` | 1 | T7: 46 sites, 0 without SAFETY; failures are scratch-layout artefacts |
| `rust-code-analysis-cli -m -O json -p <three files> \| .venv/bin/python tools/complexity_gate.py --max 15 --yellow 12` | 0 | T8 PASS |
| `.venv/bin/python tools/validate_docs.py --quiet` on cwht `main` | see summary | This record passes |

### Measurements (SWE-089), iteration 2

Lines reviewed: the 316 changed lines of `8b67385..c6e5100`, the 27 changed lines of ADR-052 and SW-02 and the 5 changed rows of the sprint index. Unsafe sites: 2 moved (text re-read, byte-identical), none added. Findings: 1 new (Minor); 3 carried. Effort of this iteration: about 30 turns and 45 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`reviewer_verdict: APPROVED` and `assurance_verdict: APPROVED`: zero Major findings under the assurance lens; revision 2 changes no behaviour, no unsafe site and no linked table, and meets CS-18. Findings 1 to 4 (Minor) are liens under rule C1, owner the firmware developer, due at the CDR readiness declaration. `verdict` stays `NEEDS CHANGES`: the rustos blobs are on unmerged branches, the checklist applied is on the unmerged CR-012 branch, and INSP-096 does not yet carry this assurance verdict (lead SE convention of 2026-09-27). The software lead sets it when the owner's merge and the PCR-4 pin-move CR bring `c6e5100` into a configuration cwht consumes, in that commit or the commit right after it.

```
ASSURANCE VERDICT (iteration 2, 2026-09-27): APPROVED; record verdict NEEDS CHANGES (held)
PRODUCT: rustos cwht/wp-sw-09 at c6e5100 (eleven rustos blobs of INSP-096 iteration 2) with ADR-052@58c06b4f, SW-02@e02db842, docs/sprints/index.md@7ae0cbcc; PAIRED RECORD: INSP-096 (iteration 2)
FINDINGS:
- [Minor] finding-1 lien (fault vectors not overridable to the safe state), due CDR readiness declaration
- [Minor] finding-2 lien (IRQ-6 reset state assumed; target-only bindings untested), due CDR readiness declaration
- [Minor] finding-3 lien (CsCell::replace drops the value on Busy), due CDR readiness declaration
- [Minor] finding-4 new, lien: clippy::redundant_pub_crate (nursery, CS-27) at irq/vectors.rs:22 and :48, due CDR readiness declaration
MEASUREMENTS: changed lines=348; unsafe sites moved=2 (byte-identical), added=0; linked vector table byte-identical; tests 49+4 passed; new findings=1; iteration 2 turns=30, minutes=45; cumulative turns=74, minutes=125
```
