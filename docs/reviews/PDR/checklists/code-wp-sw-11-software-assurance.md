---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the code review INSP-095
# (docs/reviews/PDR/checklists/code-wp-sw-11.md, iteration 1 by reviewer:WP-PDR-41-code), at the path INSP-095
# names in assurance_reviewer_agent and PDR work plan WP-PDR-41 "Records" names ("code-wp-sw-<nn>.md and
# -software-assurance.md per WP"; 07 section 2.1.1 row "Code", safety-critical column).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; CR-012 not merged,
# git merge-base --is-ancestor 7784672 main false on 2026-09-27). The `checklist` field names
# peer-review-checklist-code revision B, the checklist INSP-095 names, because tools/validate_docs.py fails a
# record whose `checklist` names a template absent from main, and the lead SE convention of 2026-09-27 does not
# change the validator. `assurance_checklist` names the template actually applied (the INSP-062 and INSP-070 form).
# id: the brief assigned no id; INSP-106 is above every id on main, on every cr/ branch and in the working tree
# (highest INSP-105 in parallel uncommitted records, 2026-09-27; INSP-101 was taken by a parallel record first)
# Iteration 2 (2026-09-27, cwht HEAD a244b05): delta (plan rule C1) on the INSP-095 finding-1 fix, rustos
# cwht/wp-sw-11 at 4a8e825 with ADR-051, SW-01 and the sprint index at cwht e3ce2cb, by a separate invocation;
# section "Iteration 2" at the end of the body. The checklist and the `checklist` field reasoning are unchanged
id: INSP-106
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-11-software-assurance.md
product: "rustos cwht/wp-sw-11: firmware/pico2/src/clocks/ and firmware/pico2/src/common/reg.rs (WP-SW-11), with cwht/l-016-6 firmware/pico2/src/lib.rs"
# product_commit and product_files (iteration 2): equal to INSP-095 iteration 2 blob for blob (readiness R1; rule C2).
# Each rustos blob equals git -C /Users/robinonsay/rust/rustos rev-parse 4a8e825:<path>; each cwht blob equals
# git rev-parse e3ce2cb:<path> and HEAD:<path> at a244b05 (git log e3ce2cb..HEAD touches none of the three). The
# L-016-6 lib.rs blob a3b43183 (5b39e8e) of iteration 1 is an unchanged ancestor of 4a8e825 and is dropped from the
# list as INSP-095 iteration 2 drops it; product_files_iteration_1 keeps the 213c536 set. The rustos blobs exist only
# on the unmerged rustos branches cwht/l-016-6 and cwht/wp-sw-11 (not pushed, not merged; OD-23)
product_commit: "4a8e8258ec3640afe15b7588db1e967679bc1d23"
product_files: ["docs/decisions/adr/ADR-051-wp-sw-11-clocks.md@7085cf5ad97de39c8ce35b02cb56df506a68b62f", "docs/sprints/SW-01-wp-sw-11-clocks.md@2384efff9c888c88a32717ed5a3b3573e56660d3", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:firmware/pico2/src/clocks/clocks.rs@631080987c36a8696b5884aa6dd7a66bf5f3cd4c", "rustos:firmware/pico2/src/clocks/clocks_tests.rs@bf61fcbf2bc6fa3f9586eadbf47278509bc4e5b6", "rustos:firmware/pico2/src/clocks/mod.rs@6aad5a88af7891dc0b48f7734ab164085249114c", "rustos:firmware/pico2/src/clocks/regs.rs@7b2ea2056760edd8d1b06d2cefb0a034e2521f53", "rustos:firmware/pico2/src/clocks/tests.rs@158d75d86168535e2a9d008de077e029baae4b33", "rustos:firmware/pico2/src/common/reg.rs@0f4e3338249d1445ec47a569712f5147549f764b", "rustos:firmware/pico2/src/common/reg/fake.rs@8a61de1ec452aa44d6f42018ca1b46eb83f77575", "rustos:firmware/pico2/src/common/board.rs@06e278af61c3bcaae1d1f67a6e952e70d6bca7c6", "rustos:firmware/pico2/src/lib.rs@0a04c25c374e0fab3a36e4819004767ed305cfd2"]
product_files_iteration_1: ["docs/decisions/adr/ADR-051-wp-sw-11-clocks.md@7f6320cd282cd911cb398c74c986d234fef89795", "docs/sprints/SW-01-wp-sw-11-clocks.md@486f35a1ff2e1b769989eb5cd966c95994041a46", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:l-016-6:firmware/pico2/src/lib.rs@a3b431838acf3d14935b38d19f46706233438fbd", "rustos:firmware/pico2/src/clocks/clocks.rs@685f6ba2c7e667ba902c19bcbbd729a1d2dd26e2", "rustos:firmware/pico2/src/clocks/clocks_tests.rs@9131b879685d517e6d36223f235b289d5babacd3", "rustos:firmware/pico2/src/clocks/mod.rs@b4cd2ebb4cd67b7fde83a2192ef6ae983420a6f6", "rustos:firmware/pico2/src/clocks/regs.rs@959db5cb599505f42b45996a0306ae061ef32279", "rustos:firmware/pico2/src/clocks/tests.rs@158d75d86168535e2a9d008de077e029baae4b33", "rustos:firmware/pico2/src/common/board.rs@06e278af61c3bcaae1d1f67a6e952e70d6bca7c6", "rustos:firmware/pico2/src/common/reg.rs@0f4e3338249d1445ec47a569712f5147549f764b", "rustos:firmware/pico2/src/common/reg/fake.rs@8a61de1ec452aa44d6f42018ca1b46eb83f77575", "rustos:firmware/pico2/src/lib.rs@0a04c25c374e0fab3a36e4819004767ed305cfd2"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/code-wp-sw-11.md (INSP-095 iteration 1, main 9d3734c; iteration 2, main 134e555)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 7.7 CS-37 and CS-38, 9.6, 14.1, 14.2, 14.3, 15, 19)", "docs/safety/hazards.json (0.5.0-pha: HZ-004 K3 and K5, HZ-008 K7)", "docs/safety/hazard-analysis.md (section 6.2 drivers row, section 7 rows j and k)", "rustos docs/extracted/rp2350-datasheet.md at 2ec64c0 (sections 8.1.2.2, 8.2, 8.5, 12.9; Tables 558, 598, 599, 629)", "docs/references/md/swehb/swe-{022,060,061,062,087,134,135,185,207,219,220}-*.md section 7.1", "docs/plan/pdr-work-plan.md (sections 3.8 WP-PDR-41, 5)"]
paired_record: INSP-095
# product_type: code (07 section 2.1.1 row "Code"); the product is the code of a safety-critical component
# (07 section 14.1 drivers row: clocks and PLL) and holds the only new unsafe of WP-SW-11 (common/reg.rs)
product_type: code
# criticality: 07 section 14.1 drivers row ("clocks and PLL (TICKS, XOSC, PLL_SYS: every timing budget depends on
# them)", inherited); 07 section 14.2 module row "pico2 clocks and PLL (WP-SW-11)" allocates SWE-134 a, g, j, k
criticality: safety-critical
product_size: 1981 lines changed (5b39e8e 29 added; 213c536 1952 added, 1 removed), of which 1013 non-test lines; 548 lines of author developer tests (34 tests); ADR-051 94 lines; SW-01 62 lines. Iteration 2 delta: 213c536..4a8e825 196 added, 32 removed (228 changed lines: clocks.rs 51, clocks_tests.rs 168, mod.rs 6, regs.rs 3); ADR-051, SW-01 and index 26 changed lines
sprint: SW-01-wp-sw-11-clocks
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "sa-reviewer:WP-PDR-41-sa-wp-sw-11 (iteration 1); sa-reviewer:WP-PDR-41-sa-wp-sw-11-delta (iteration 2, a separate invocation that authored no part of WP-PDR-41, revision 2, the rustos fix commit, INSP-095 or INSP-106 iteration 1)"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-sa-wp-sw-11 (iteration 1) and sa-reviewer:WP-PDR-41-sa-wp-sw-11-delta (iteration 2) (software assurance function; paired file review INSP-095 by reviewer:WP-PDR-41-code)"
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 2. INSP-095 finding-1 (Major), which carried the
# No of swe-134 task 2, swe-087 task 4, SA-C-j and SA-C-k, is Verified under the assurance lens at 4a8e825; no Major
# is open. Findings 1 to 5 were not addressed by revision 2 (plan rule C1) and new finding-6 is Minor: all six are
# liens under rule C1 (owner the firmware developer, finding-5 the WP-PDR-16b writer; due at the CDR readiness
# declaration). Iteration 1 was NEEDS CHANGES for both
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES by the software lead's rule (07 section 10.2) and the lead SE convention of
# 2026-09-27 (INSP-031 practice): the reviewed rustos blobs exist only on unmerged branches, and INSP-095 readiness
# R3 and R5 do not hold. The software lead sets it when the owner's merge and the pin-move CR PCR-4 bring 4a8e825
# into a configuration cwht consumes
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 6
# findings_open: 6, all liens (rule C1), as INSP-095 iteration 2 counts its liens
findings_open: 6
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 6
assurance_tasks_applied: ["swe-087 7.1 task 2", "swe-088 7.1 task 2", "swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 3", "swe-135 7.1 task 4", "swe-135 7.1 task 5", "swe-135 7.1 task 6", "swe-135 7.1 task 7", "swe-134 7.1 task 2", "swe-134 7.1 task 3", "swe-134 7.1 task 6", "swe-087 7.1 task 1", "swe-087 7.1 task 4", "swe-088 7.1 task 1", "swe-089 7.1 task 1", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 2"]
swe134_items_checked: [a, g, j, k]
deferred_rids: []
# items_no (iteration 2): swe-134 7.1 task 2, swe-087 7.1 task 4, SA-C-j and SA-C-k are Yes now that INSP-095
# finding-1 is Verified; the other five stay No on Minor liens (findings 1, 2 and INSP-095 findings 4 to 7)
items_no: ["swe-061 7.1 task 2", "swe-185 7.1 task 1", "swe-135 7.1 task 5", "swe-062 7.1 task 1", "swe-219 7.1 task 1"]
# effort: iteration 1 45 turns, 95 minutes; iteration 2 30 turns, 50 minutes (cumulative below)
effort_turns: 75
effort_minutes: 145
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-106: software assurance pair of INSP-095, code review of WP-SW-11 clock bring-up (rustos `pico2` at `213c536`), iteration 1

**Product.** rustos branch `cwht/wp-sw-11` at `213c536` (parent `cwht/l-016-6` at `5b39e8e`, parent `master` `2ec64c0`) and the cwht design and sprint records ADR-051 and SW-01 at `618e441`: the thirteen blobs of `product_files`, equal to INSP-095 (each checked with `git rev-parse`). The rustos blobs were read with `git -C /Users/robinonsay/rust/rustos show <commit>:<path>` and in a detached scratch worktree of the rustos repository (`git worktree add --detach`, removed after the runs); the owner's rustos working tree was not read. **Checklist applied:** `peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (see the front matter for why the `checklist` field names the code template). **Paired record:** INSP-095 iteration 1 (main `9d3734c`), file reviewer `reviewer:WP-PDR-41-code`.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-PDR-41, ADR-051, SW-01 or INSP-095, edited no product file, and is not the file reviewer. Author, file reviewer and assurance reviewer are three different invocations.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` ran before any manual search: on `/Users/robinonsay/rust/cwht` (queries: software assurance record template and paired records; clock driver requirement, CS-37 and hazard `firmware_role`; SWEHB SA tasking for static analysis) and on `/Users/robinonsay/rust/rustos` (query: XOSC `CTRL.ENABLE` invalid setting and `BADWRITE`, watchdog tick). `grep -n`, `sed -n` and a Python walk of `hazards.json` were used afterwards only to pin lines. The index had no entry for ADR-051 or SW-01; both were read by path.

**Acceptance criteria (rule C7).** Readiness R1 to R4; SA-A1 to SA-A4; every task of the section B rows "Every product type" and "code" and of the SWEs the product cites (ADR-051 section 1 "Guidance consulted": SWE-134, SWE-219, SWE-220, SWE-058, SWE-060, SWE-062); SWE-134 items a, g, j and k of the 07 section 14.2 clocks row, and items b to f, h, i, l recorded as not allocated; SA-D1 to SA-D6; SA-E1 to SA-E4; SA-F1 to SA-F3; the assurance reading of each INSP-095 finding.

## Commands run by the assurance reviewer (evidence)

| # | Command (read-only for both repositories; outputs in the scratchpad) | Result |
|---|---|---|
| S1 | `cargo +1.98.0 test --offline -p pico2 --lib` at `213c536` | 34 passed, 0 failed |
| S2 | `cargo +nightly-2026-08-24 llvm-cov --offline -p pico2 --lib --branch --summary-only` at `213c536` (MSR-14 form of 07 section 9.6 item 3; nightly, never credit) | `clocks/clocks.rs` regions, functions, lines 100 %; `clocks/mod.rs` lines 72 of 73, branches 31 of 32; `common/reg.rs` 100 %, branches 4 of 4. The one missed branch is `mod.rs:241` (the `else` of `let Ok(vco) = u32::try_from(...)`, True 34, False 0) and the missed line is its `return` at `mod.rs:242` (finding-1) |
| S3 | the same with `RUSTFLAGS="-Zcoverage-options=condition"` and `--text` | no further uncovered branch; `within` (`mod.rs:173`) is one inlined decision reported once for all call sites, so the per-call-site MC/DC of `plan` was checked by hand against `tests.rs` (finding-1) |
| S4 | `rust-code-analysis-cli --metrics` over `clocks/` and `common/`, piped to `tools/complexity_gate.py --max 15 --yellow 12` | PASS; 81 functions, max CC 10 (`check_pll`, analyzer 9 plus 1 `let ... else`), none above 12 |
| S5 | `cargo +1.98.0 clippy --offline -p pico2 --lib --target thumbv8m.main-none-eabihf -- -W clippy::pedantic -W clippy::arithmetic_side_effects`, filtered to the WP-SW-11 files | `module_inception` at `clocks/mod.rs:39` (INSP-095 finding-6); `arithmetic_side_effects` at `mod.rs:196, 209, 210, 232, 241, 250, 251, 254` and `reg.rs:166, 213` (the sites of INSP-095 finding-4; every divisor is checked non-zero first: `refdiv >= 1` at `mod.rs:229`, `post >= 1` at `:247`) |
| S6 | `tools/unsafe_audit.py --write` into a scratch audit file over the worktree | 39 sites at `213c536`, 0 without `SAFETY`; the two WP-SW-11 sites are `reg.rs:179` (`read`) and `reg.rs:188` (`write`). The tool's forbidden-crate classification did not accept the scratch worktree paths as audited in this invocation, so its PASS or FAIL line is not used; INSP-095 C8 (PASS) is the engineering data |
| S7 | `git -C rustos diff --stat 2ec64c0 213c536` | 9 files, all under `firmware/pico2/src/`; no `Cargo.toml` or `Cargo.lock` change |
| S8 | Datasheet check (rustos `docs/extracted/rp2350-datasheet.md` at `2ec64c0`): section 8.1.2.2 (extract lines 37735 to 37790), Table 558 (line 39214), Table 598 and 599 (lines 40928 to 40975), section 12.9.1 and 12.9.2 (lines 89706 to 89734) | INSP-095 finding-1 confirmed; finding-4 below; the watchdog takes its tick from `TICKS` (12.9.2) and is reset by a watchdog chip-level reset (12.9.1) |
| S9 | `tools/validate_docs.py`; `tools/traceability.py --report-only --output <scratchpad>/sa11-trace.md` | the product's cwht files pass; 8 pre-existing failures in other records (record drift, none of this product); traceability 245 requirements, 173 cases, 0 violations, 2 pre-existing warnings (REQ-SYS-125, REQ-SYS-148); `docs/vv/` untouched |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | Yes | `product_files` equals INSP-095 blob for blob; every rustos blob equals `git rev-parse 213c536:<path>` (and `5b39e8e:firmware/pico2/src/lib.rs`); every cwht blob equals `618e441:<path>` and `HEAD:<path>` |
| R2 | Yes | `product_type: code`, `criticality: safety-critical` from 07 section 14.1 drivers row and the 14.2 clocks row |
| R3 | Yes | S9: the product's cwht files pass; no traceability violation (the product touches no requirement id: CS-24 does not apply to rustos code, plan WP-PDR-41) |
| R4 | Yes | INSP-095 filed by `reviewer:WP-PDR-41-code`; author `author:WP-PDR-41 wave 1a`; this invocation is neither |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row "Code", safety-critical column Yes; 07 section 14.1 drivers row names "clocks and PLL"; 14.2 module row `pico2` clocks and PLL (WP-SW-11) items a, g, j, k; `reg.rs` also holds `unsafe` (the Neither column's exception) |
| SA-A2 | Yes | three invocations named in both records (`author_agent`, `reviewer_agent`, this record's `assurance_reviewer_agent`). INSP-095 still reads `assurance_reviewer_agent: "pending: ..."` and carries no `paired_record`; the file reviewer updates its own record (cross item X-1) |
| SA-A3 | Yes | same `product`, `product_commit` and thirteen blobs; no product change after either review |
| SA-A4 | Yes | INSP-095 applied `peer-review-checklist-code.md` revision B, the checklist 07 section 10.1 and 08 section 3.5 assign to code, and answered R1 to R6 and CK-CODE-A1 to J4 with evidence (NPR 7150.2D 5.3.3 a to d: checklist, readiness, findings with severity, measurements). One answer is not borne out: CK-CODE-H3 "every `plan` limit at both edges" (finding-1) |

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | `swe-219 7.1 task 1`, `swe-062 7.1 task 1`, `swe-135 7.1 task 5` | `mod.rs:241-242`, `:247`; `tests.rs:88-133`; ADR-051 line 63 | CS-38 MC/DC pairs and one branch of `plan` not exercised | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-a), `swe-062 7.1 task 1` | `clocks.rs:30-32`; `clocks_tests.rs:18-45`; `fake.rs` | no host test of a restart start state | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-j, SA-C-l) | ADR-051 line 58; `clocks.rs:396-398`; 07 section 14.2 row a; CS-37 | start order of the watchdog and the clock bring-up not defined | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-g) | `clocks.rs:220`; `mod.rs:34-37`; ADR-051 line 33 | first `XOSC.CTRL` write is an invalid `ENABLE` code; `BADWRITE` never read | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | SA-D1 (`swe-134 7.1 task 6`) | `hazards.json` HZ-004 `causes`; `hazard-analysis.md` section 6.2 drivers row | timebase common cause not stated in the hazard data | Open | Pending | |

### finding-1

**Minor, `swe-219 7.1 task 1` (SC), `swe-062 7.1 task 1` (SC), `swe-135 7.1 task 5` (SC); CS-38 and 07 section 9.6 item 2.** 07 CS-38 requires every decision of a `pico2` driver used by a safety-critical component to be exercised "by HostUnit tests with MC/DC independence pairs". Two decisions of `plan` fall short at `213c536`:

1. `mod.rs:247` `!within(pll.postdiv1, 1, 7) || !within(pll.postdiv2, 1, 7)` has four conditions. `tests.rs` `postdiv_limits_and_output_ceiling` shows only `postdiv1 = 0` (lower bound of postdiv1) and `postdiv2 = 8` (upper bound of postdiv2). No test has `postdiv1 = 8` or `postdiv2 = 0`, so two conditions have no independence pair.
2. `mod.rs:241-242`, the `else` arm of `let Ok(vco) = u32::try_from(...)`, never runs (S2: branch 241:9 False 0). The arm is reachable: `xosc_hz` 15 MHz, `refdiv` 1 and `fbdiv` 287 to 320 give a product of 4.305 GHz or more, above `u32::MAX`, and each passes the earlier checks.

ADR-051 section 4.3 (line 63) and INSP-095 CK-CODE-H3 both say "every `plan` limit at both edges", which these gaps contradict. The behaviour is correct by analysis (both paths return the documented error). **Severity:** Minor now, because the SWE-219 record is the release coverage report `TC-SW-COV-001-r<N>` (07 section 9.6 item 3), which is not yet due, and one test per gap closes it. If the gap is still present at that run, it is a shortfall that needs the owner waiver of 07 section 14.3, and then it is Major. **Fix:** add `plan` cases with `postdiv1 = 8` and `postdiv2 = 0` (each with the other three conditions held true), and one with `xosc_hz: 15_000_000`, `refdiv: 1`, `fbdiv: 300` that expects `VcoOutOfRange`; and correct the "both edges" sentence of ADR-051 section 4.3 and SW-01 to what the tests show.

### finding-2

**Minor, `swe-134 7.1 task 2` (SC), item a ("initialized ... at first start and restarts"); `swe-062 7.1 task 1`.** The module doc (`clocks.rs:30-32`) gives step 3 its purpose: "when the bootrom or an earlier image left `clk_sys` on the PLL". A watchdog restart that does not reset the clock blocks can also leave the crystal running, `clk_ref` on the crystal and the tick generators running. No test starts from such a state. `FakeRegs` starts every register at 0, and `healthy()` presets only status bits. So the restart path of item a, and the order of steps 3 to 5 while `clk_sys` runs from `PLL_SYS`, rest on analysis alone. By analysis the path holds: step 3 leaves `AUXSRC` at `PLL_SYS` and moves the glitchless mux to `clk_ref` before step 5 resets the PLL. But nothing checks it. This is separate from INSP-095 finding-1, which asks for the datasheet reset values: those are the cold-boot state, and this is the warm-restart state. **Fix:** in the same change as the INSP-095 finding-1 fix, add a bring-up test whose register file starts in a restart state. That state has `CLK_SYS_CTRL` with `SRC = 1` and `AUXSRC = 0` and `CLK_SYS_SELECTED` on aux; `CLK_REF_CTRL.SRC = 2`; `XOSC.STATUS` `STABLE` and `ENABLED`; `PLL_SYS.CS.LOCK` set; and both tick generators `RUNNING`. The test asserts that the golden order still holds, and that `clk_sys` reads back on `clk_ref` before the first `RESETS` write.

### finding-3

**Minor, `swe-134 7.1 task 2` (SC), items j and l; 07 section 14.2 row a; CS-37.** The start order of the watchdog and the clock bring-up is not defined consistently:

- 07 section 14.2 row a puts "then start the watchdog (REQ-SYS-131)" before "only then are the remaining clocks, peripherals and the display initialized".
- CS-37 requires `TICKS.WATCHDOG` to be enabled "before any TIMER0 or watchdog use".
- ADR-051 section 4.2 (line 58) calls `Rp2350Clocks::init` "right after driving the safe outputs" and says nothing about the watchdog.
- Step 9 stops and restarts the watchdog tick (`clocks.rs:396-398`).

The watchdog is reset by a watchdog chip-level reset and takes its tick from `TICKS` (datasheet 12.9.1 and 12.9.2), so each order has a consequence that no record states:

- **Clocks first (ADR-051 and CS-37):** no watchdog covers the bring-up. A stop that is not bounded by `poll`, such as the `clk_sys` stop of INSP-095 finding-1 or a bus stall, holds the unit until power is cycled.
- **Watchdog first (row a as written):** the watchdog counts on a tick the bootrom configured from the ROSC, and step 9 pauses it.

With the outputs already driven safe and the K5 hardware cutoff independent, this is an availability and item l concern, not an open hazard path. So it is Minor. It is also the reason INSP-095 finding-1 must be fixed rather than covered by recovery. **Fix:**

- ADR-051 section 4.2 states the order. The recommended order is safe outputs, then clock bring-up, then watchdog start, per CS-37. It also states that the bring-up is not watchdog-covered and that every wait inside it is loop-bounded once INSP-095 finding-1 is fixed.
- The 07 section 14.2 row a writer (plan section 5.3: WP-PDR-13 or WP-PDR-47) and the WP-PDR-32 `SW-BOOT` author reword "remaining clocks" to match (cross item X-3).

### finding-4

**Minor, `swe-134 7.1 task 2` (SC), item g (integrity checks on outputs).** Step 2 first writes `XOSC.CTRL = 0x0000_0aa0` (`clocks.rs:220`; golden sequence `clocks_tests.rs:52`). Its `ENABLE` field (23:12) is `0x000`, which is neither `0xd1e` nor `0xfab`. Table 598 says "An invalid setting will retain the previous value", and Table 599 says `STATUS.BADWRITE` (bit 24, write-to-clear) records "An invalid value has been written to CTRL_ENABLE or CTRL_FREQ_RANGE". So every boot sets `BADWRITE` on purpose, and the driver never reads or clears it. The one integrity signal the crystal block gives for a wrong control write is therefore lost. The claims in the `mod.rs` module doc (lines 34 to 37: "writes every field of every control register it uses and relies on no reset value") and ADR-051 section 2 ("Every control field is written explicitly") are not accurate for `XOSC.CTRL.ENABLE`, whose value is retained. Keeping `ENABLE` out of the first write is the safer choice: writing `DISABLE` while `clk_ref` runs from the crystal after a restart "may lock-up the chip" (Table 598). **Fix:**

- clear `BADWRITE` (write 1 to bit 24 of `XOSC.STATUS`) after the enable write of `(0xfab << 12) | 0xaa0`;
- read `STATUS.BADWRITE` together with `STABLE`, and treat a set flag as a new `ClockFault` variant with its host test;
- correct the module doc and ADR-051 section 2 to say that the first write sets the range only.

### finding-5

**Minor, SA-D1 (`swe-205` section 7.7.2 consideration "common-cause faults"), `swe-134 7.1 task 6` (SC).** The clock tree is the single timebase of every software timing control:

- HZ-004 K3 manual-closure timeout of 5 s;
- the paddle no-gap watchdog;
- the tune and test-mode timeouts;
- the CPU watchdog of REQ-SYS-131;
- the HZ-008 K7 frequency count, which "uses the RP2350 crystal timebase".

`hazards.json` 0.5.0-pha names no cause for a timebase error (a Python walk of every hazard found "clock" only in verification notes and the HZ-008 synthesizer and harmonic text). `hazard-analysis.md` section 6.2 carries the driver only as "inherited". The contribution is not missing from the hazard data as a whole: 07 section 14.1 states "every timing budget depends on them", and CS-37 is the control. So this is Minor. But the independence argument the hazards rely on is not stated anywhere. For example: K5 is a monostable independent of the RP2350 clock; a wrong crystal of up to about 1.5 times nominal keeps K3 below the 7.5 s K5 floor; and under K7 a wrong timebase makes the counted frequency disagree with the set frequency, so `PA_EN` is refused, which fails safe. Nor does the hazard data record that the step 10 check does not detect a wrong crystal (INSP-095 finding-2). **Fix:** the `hazards.json` writer (plan section 5.3: WP-PDR-16b) adds a timebase common-cause entry under HZ-004 and HZ-008 (cause: clock tree or crystal frequency wrong; controls: CS-37 and the step 10 frequency-counter check for divider and PLL errors, the dev-board stopwatch check for the crystal, and K5 independent of the RP2350 clock) (cross item X-4).

### Assurance reading of the INSP-095 findings (cited, not raised again)

| INSP-095 finding | Assurance lens | Severity change |
|---|---|---|
| finding-1 (Major) | Concurred, confirmed against section 8.1.2.2 (S8). The datasheet adds "Avoid clock glitches at all costs: they may corrupt the logic running on the clock". The bring-up runs after the application has driven its safe outputs (`clocks.rs:151-152`), so a corrupted core can overwrite those outputs, and no watchdog covers the bring-up (finding-3). SWE-134 items j and k have a path with no fault return. Carries the No of `swe-134 7.1 task 2`, `swe-087 7.1 task 4`, SA-C-j and SA-C-k | none (Major) |
| finding-2 (Minor) | Concurred. A wrong crystal passes step 10. The hazards stay controlled by K5 and fail safe under K7 (finding-5), so the effect is a data and argument gap | none |
| finding-3 (Minor) | Concurred. A step 10 false timeout on healthy hardware ends in the safe-state halt: availability only | none |
| finding-4 (Minor) | Concurred. Every divisor is checked non-zero before use (S5), so no path divides by zero; the overflow bounds hold by the earlier checks. Carries the No of `swe-185 7.1 task 1` (CS-14 is a secure-coding rule of 07 section 7) | none |
| findings 5 to 7 (Minor) | Concurred. With finding-4 they carry the No of `swe-061 7.1 task 2` | none |

## Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the code review of a safety-critical driver (07 section 2.1.1 basis line) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project's software assurance plan, 07 section 15 (section 2.1.1 routing, section 14 provisions); the NASA-STD-8739.8 part is relieved by `rmm.json` SWE-022 T (standard not in the corpus) | | none |
| swe-060 7.1 task 1 | | Yes | `bring_up` (`clocks.rs:187-211`) runs the ADR-051 section 2 steps one to one; the step table (`clocks.rs:17-28`) matches. The datasheet deviation of INSP-095 finding-1 is in both the design and the code | | INSP-095 finding-1 |
| swe-060 7.1 task 2 | | Yes | No function outside ADR-051 section 2 and 4.2: `Regs`, `Mmio`, `poll`, `plan`, `judge`, the step functions and the test-only `FakeRegs`; `ALIAS_XOR` is an unused constant, not a function (INSP-095 finding-5) | | none |
| swe-061 7.1 task 1 | | Yes | 07 section 7 (CS-01 to CS-39, the target platform rules 7.7) is the selected standard; CS-37 and CS-38 are written for this driver | | none |
| swe-061 7.1 task 2 | | No | Not conforming at `213c536`: CS-14 (INSP-095 finding-4), CS-21 (finding-5), G1 `-D warnings` (finding-6), CS-18 `lib.rs` (finding-7); S5 reproduces 4 and 6 | | INSP-095 findings 4 to 7 |
| swe-207 7.1 task 1 | | Yes | 07 section 7 carries the secure coding practices: CS-04 overflow checks, CS-05 to CS-07 `unsafe` confinement and audit, CS-08 MMIO addressing, CS-11 no panic on release paths, CS-14 bounded arithmetic, CS-15 checked casts | | none |
| swe-185 7.1 task 1 | | No | S5, S6 and INSP-095 C1 to C8: `unsafe` is confined to the two `Mmio` blocks with `SAFETY` comments and a masked address (`reg.rs:165-167`); no `unwrap`, `panic!`, indexing or numeric `as`. Plain arithmetic without the CS-14 bound argument (S5) is the one secure-coding gap | | INSP-095 finding-4 |
| swe-135 7.1 task 1 | | Yes | Independent static analysis performed: S2 to S6 (coverage, complexity, clippy pedantic and arithmetic lints, unsafe audit) | | none |
| swe-135 7.1 task 2 | SC | Yes | Checkers used: clippy (pedantic and `arithmetic_side_effects`), `tools/complexity_gate.py`, `tools/unsafe_audit.py`, Miri (INSP-095 C3: 95 passed, no undefined behaviour at the stack head) | | none |
| swe-135 7.1 task 3 | | Yes | Every result is dispositioned: INSP-095 findings 4 and 6 carry the lint results; the pre-existing crate-level lint and fmt debt is carried to the PCR-4 G1 run (INSP-095 R1; cross item X-5) | | none |
| swe-135 7.1 task 4 | | Yes | Code scanned for security defects (S5, S6; INSP-095 C3). A dependency advisory scan is not needed for this change: no `Cargo.toml` or `Cargo.lock` change (S7). The formal `cargo audit` and `cargo deny` run is G5 on the PCR-4 branch | | none |
| swe-135 7.1 task 5 | SC | No | Coverage verified (S2, S3): 100 % lines of `clocks.rs` and `reg.rs`, one branch and two MC/DC pairs short in `mod.rs`; no waiver needed yet (the release report is not due) | | finding-1 |
| swe-135 7.1 task 6 | SC | Yes | S4: max CC 10, none above 12; no waiver needed (07 section 14.3) | | none |
| swe-135 7.1 task 7 | | Yes | Thresholds defined: G1 `-D warnings`, CC 15 with yellow 12 (CS-17, 07 section 14.3), 100 % coverage (07 section 9.6), zero `unsafe` without `SAFETY` (CS-06) | | none |
| swe-134 7.1 task 2 | SC | No | Section C below: items a and g hold with Minor gaps; items j and k have the INSP-095 finding-1 path | | INSP-095 finding-1; findings 2, 3, 4 |
| swe-134 7.1 task 3 | SC | Yes | The driver holds no persisted or loaded record; its one set of defaults and range limits is `ClockConfig::PICO2_150_MHZ` and the `plan` checks, whose values are covered by `pico2_plan_matches_the_datasheet_numbers` and the golden sequence (`clocks_tests.rs:49-110`), apart from finding-1 | | finding-1 |
| swe-134 7.1 task 6 | SC | Yes | The 14.2 clocks row (a, g, j, k) is consistent with `hazard-analysis.md` section 6.2 (drivers "as the components they serve", inherited) and section 7 rows j and k; the common-cause argument is not written down | | finding-5 |
| swe-087 7.1 task 1 | | Yes | INSP-095 performed and filed at main `9d3734c`, and this record | | none |
| swe-087 7.1 task 4 | SC | No | As `swe-134 7.1 task 2` | | INSP-095 finding-1 |
| swe-088 7.1 task 1 | | Yes | SA-A4 | | none |
| swe-089 7.1 task 1 | | Yes | SA-E2 | | none |
| swe-062 7.1 task 1 | SC | No | S1: 34 tests pass, every `ClockFault` variant reached; the CS-38 MC/DC pairs of two conditions, one reachable branch and the restart start state are not tested | | findings 1, 2 |
| swe-062 7.1 task 2 | | Yes | No unit-test failure; every gap is a finding with a state in this record or INSP-095 | | none |
| swe-219 7.1 task 1 | SC | No | 100 % not reached at `213c536` and no rationale recorded; SWE-219 T in `rmm.json` makes the manual MC/DC table of 07 section 9.6 the method | | finding-1 |
| swe-220 7.1 task 1 | SC | Yes | S4 performed on every WP-SW-11 function | | none |
| swe-220 7.1 task 2 | SC | Yes | S4: max 10, no function above 15 | | none |
| swe-080 7.1 task 2 | | Yes | SA-E3 | | none |
| swe-080 7.1 task 3 | | Yes | SA-E3 | | none |
| swe-081 7.1 task 2 | | Yes | SA-E3 | | none |
| swe-058 7.1 tasks 1 to 5; section B row `trade-study-or-adr` tasks for ADR-051 (swe-033, swe-039 task 4, swe-057 task 2, swe-134 task 4, swe-205 task 3) | 4 of swe-058 SC; swe-134 task 4 SC | N/A | ADR-051 is carried in `product_files` as the design this code implements, and its design review is routed separately. SW-01 phase 3 names `adr-051-wp-sw-11-clocks.md` with its SA pair; plan WP-PDR-41 "Records" does not (INSP-095 report; cross item X-2) | 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical ... component" and row "Design": the ADR's own design record and its SA pair | none |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | | N/A | Iteration 1: no earlier finding or lien on this product | 07 section 10.2 (a first iteration has no accepted finding to address) | none |
| swe-187 7.1 tasks 1 and 2 | | N/A | Section B row `test` only; no credit run exists (the dev-board check is `credit: false`, not yet written) | 07 section 2.1.1 (section B routes swe-187 to the test row) | none |

## C. SWE-134 items (07 section 14.2 clocks row: a, g, j, k)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | TICKS started before any TIMER0 or watchdog use: step 9 (`clocks.rs:379-408`) with `RUNNING` read back. The type system enforces it: `ClocksReady` has a private field and is built only in `bring_up` (`clocks.rs:123-125`, `:200`); it is neither `Clone` nor `Copy`, and the TIMER0 and PWM constructors take `&ClocksReady` (ADR-051 section 2). The init runs after the application has driven its outputs safe (`clocks.rs:151-152`). Restart state untested (finding-2) |
| SA-C-b | N/A | not allocated to this row (07 section 14.2 clocks row: a, g, j, k) |
| SA-C-c | N/A | not allocated; the termination path is the `cwht-app` CS-11 halt of 07 section 14.2 row c ("clock fault of CS-37"). By analysis every `ClockFault` return leaves `clk_sys` running from `clk_ref` or `PLL_SYS`, so the SIO writes of `safe_state()` can run. The only exception is the INSP-095 finding-1 path |
| SA-C-d, SA-C-e, SA-C-f, SA-C-h, SA-C-i, SA-C-l | N/A | not allocated to this row (07 section 14.2); item l as a watchdog concern is finding-3 |
| SA-C-g | Yes | `STABLE`, `SELECTED`, `RESET_DONE`, `LOCK`, `ENABLED`, `RUNNING` read back. Both measured frequencies are judged by the hardware `PASS` flag and the software window (`mod.rs:310-318`; MC/DC pairs `tests.rs:167-209`). Gaps: `BADWRITE` (finding-4); the crystal is not checked (INSP-095 finding-2) |
| SA-C-j | No | Every wait is a `poll` bounded by a loop count, independent of TIMER0 (`reg.rs:203-219`; bound tested exactly, `reg.rs:250-258`). But the INSP-095 finding-1 path can stop or glitch `clk_sys` before a bounded wait can run; margin on the step 10 waits is INSP-095 finding-3 |
| SA-C-k | No | Fifteen `ClockFault` variants, one per failed step, each returned and tested; `plan` runs before any register write. The same INSP-095 finding-1 path ends in a hang or corruption rather than a returned fault |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | The 7.7.2 considerations that apply are control of safety-critical timing, common-cause faults and stored sequences (the fixed bring-up order). The driver's contribution is recorded as inherited in `hazard-analysis.md` section 6.2 and 07 section 14.1. The common-cause statement is missing (finding-5) |
| SA-D2 | Yes | 07 section 14.1 drivers row and 03 section 4.3 drivers row (line 168) both name clocks and PLL; the union rule gives "as the components they serve"; no new or renamed component |
| SA-D3 | N/A | The product adds no requirement id and touches none (S9: 0 violations). The L2 rows for CS-37 are written by WP-PDR-35 (ADR-051 section 4.1), so two-way hazard tracing is checked at the delta after WP-PDR-35 |
| SA-D4 | N/A | no safety-tagged requirement is part of the product (WP-PDR-35) |
| SA-D5 | N/A | as SA-D3. The closing Test for the CS-37 rows is due with WP-PDR-35 and the independent test author (SW-01 phase 2) |
| SA-D6 | Yes | ADR-051 section 4.3 states that no hazard analysis update is required, which is correct for the control. The common-cause text of finding-5 is the one update requested |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | N/A | iteration 1; no earlier findings (07 section 10.2) |
| SA-E2 | Yes | INSP-095 and this record carry `findings_*`, `effort_turns`, `effort_minutes`, `product_size` (07 section 10.3) |
| SA-E3 | Yes | ADR-051 and SW-01 are new cwht records committed on main (`618e441`, trailer `Co-Authored-By`), not baselined items, so no `CR:` trailer is needed. The rustos change is on unmerged branches for the owner's merge; the pin in `tools/toolchain.lock.md` moves only by the Class I CR PCR-4 (ADR-051 line 14; plan section 6.2). The safety-critical code is under git on frozen commits |
| SA-E4 | N/A | no test for credit yet: dev-board check `credit: false`, not written (SW-01 phase 2). Credit runs need the merged rustos commit and a VDD (04 section 5.2) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No new assurance risk. The concern that the rustos crate-level lint and fmt debt fails G1 at PCR-4 on items cwht does not own is sent to the lead SE (cross item X-5) as a candidate `assurance`-tagged risk entry for the risk register writer (WP-PDR-18, the only writer of `register.json`, plan section 5.3), or as an addition to RSK-013 |
| SA-F2 | Yes | front matter: findings by severity and state, `assurance_findings_*`, `items_no`, effort |
| SA-F3 | Yes | verdict, open findings, tasks applied and reliefs are all in this record |

## Cross items for the lead SE (not findings of this product)

| # | Item | Owner |
|---|---|---|
| X-1 | INSP-095 front matter: set `paired_record: INSP-106`, name this invocation in `assurance_reviewer_agent`, copy `assurance_verdict: NEEDS CHANGES` (07 section 10.2; the file reviewer updates its own record) | reviewer:WP-PDR-41-code |
| X-2 | The ADR-051 design review record `adr-051-wp-sw-11-clocks.md` and its SA pair (07 section 2.1.1 row 3; SW-01 phase 3) are not in plan WP-PDR-41 "Records"; dispatch them (the swe-058 and ADR tasks above are N/A here only because that record carries them) | lead SE |
| X-3 | 07 section 14.2 row a "then start the watchdog ... only then are the remaining clocks" against CS-37 and ADR-051 section 4.2 (finding-3) | 07 writer of the wave (plan section 5.3), WP-PDR-32 |
| X-4 | Timebase common-cause text in `hazards.json` HZ-004 and HZ-008 (finding-5) | WP-PDR-16b |
| X-5 | Pre-existing rustos lint and fmt debt against G1 at PCR-4 (INSP-095 R1, C4 to C6) as a risk candidate | WP-PDR-18 via the lead SE |

## Completion

`assurance_verdict: NEEDS CHANGES`. Five safety-designated tasks are answered No: two on INSP-095 finding-1 (Major, Open) and three on this record's findings 1 and 2. Iteration 2 is a delta (rule C1) on the new frozen commit of the INSP-095 finding-1 fix. It verifies that fix under the assurance lens (items j and k, the restart test of finding-2), findings 1 and 4 if they are fixed in the same commit, and the ADR-051 wording of findings 3 and 4, and it re-runs S1 to S4. Minor findings not fixed by an APPROVED verdict become liens due at the CDR readiness declaration (rule C1). The record `verdict` is set by the software lead when both records are APPROVED and the reviewed blobs reach a configuration cwht consumes (owner merge, PCR-4; lead SE convention of 2026-09-27).

## Measurements (SWE-089)

Lines reviewed: the 1013 non-test lines at `213c536` and the 29-line L-016-6 change, the 548 lines of author developer tests read in full for coverage and MC/DC, ADR-051 and SW-01 in full. Tasks in the table: 33 rows (30 tasks applied, 7 of them answered No; 3 rows N/A with relief; 2 section C items answered No). SWE-134 items checked: a, g, j, k. Findings: 0 Major, 5 Minor. Effort: 45 turns, 95 minutes.

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: rustos cwht/wp-sw-11 (13 blobs of product_files) at 213c536; PAIRED RECORD: INSP-095
PRODUCT TYPE: code; CRITICALITY: safety-critical
FINDINGS:
- [Minor] finding-1 swe-219/swe-062/swe-135 task 5: MC/DC pairs for postdiv1 <= 7 and postdiv2 >= 1 missing; mod.rs:241-242 u32-overflow arm never executed.
- [Minor] finding-2 swe-134 task 2 item a: no host test from a restart start state.
- [Minor] finding-3 swe-134 task 2 items j, l: watchdog and clock bring-up order undefined across 07 14.2 row a, CS-37 and ADR-051.
- [Minor] finding-4 swe-134 task 2 item g: XOSC.CTRL first write is an invalid ENABLE code; BADWRITE never read.
- [Minor] finding-5 SA-D1: timebase common cause not stated in hazards.json.
- Cited, not raised again: INSP-095 finding-1 (Major, Open) carries swe-134 task 2, swe-087 task 4, SA-C-j, SA-C-k.
TASKS APPLIED: as assurance_tasks_applied
TASKS N/A (relief): swe-058 tasks 1 to 5 and the ADR row tasks (07 2.1.1 rows 3 and design); swe-087 task 2, swe-088 task 2 (07 10.2); swe-187 tasks 1, 2 (07 2.1.1)
SWE-134 ITEMS CHECKED: a, g, j, k
MEASUREMENTS: size=1013 non-test lines; tasks=30 applied, 3 N/A rows; tasks_no=7; turns=45; minutes=95; major=0; minor=5
```

## Iteration 2: assurance delta on the INSP-095 finding-1 fix (2026-09-27, cwht HEAD `a244b05`)

**Scope (rule C1).** Iteration 2 is a delta. It verifies, under the assurance lens, the fix of INSP-095 finding-1 (Major, concurred at iteration 1, Verified by the file reviewer at INSP-095 iteration 2) and reads every hunk of the drifted blobs: rustos `cwht/wp-sw-11` at `4a8e825` (parent `213c536`; `clocks.rs` `685f6ba` to `6310809`, `clocks_tests.rs` `9131b87` to `bf61fcb`, `mod.rs` `b4cd2eb` to `6aad5a8`, `regs.rs` `959db5c` to `7b2ea20`) and, at cwht `e3ce2cb`, ADR-051 (`7f6320c` to `7085cf5`), SW-01 (`486f35a` to `2384eff`) and the sprint index (`fb217bc` to `7ae0cbc`). The unchanged blobs (`tests.rs`, `common/reg.rs`, `fake.rs`, `board.rs`, `lib.rs`) were read only where the new tests rely on them (the alias semantics of `FakeRegs::write`, `fake.rs:133-149`). Findings 1 to 5 of this record were not touched by revision 2 (ADR-051 section 8; SW-01 "Phase 1, revision 2") and are re-stated at their current state, not re-reviewed in full.

**Independence (rule C4).** This invocation authored no part of WP-PDR-41, revision 2, the rustos fix commit, INSP-095 or INSP-106 iteration 1, and edited no product file. The rustos repository was read with `git show` and in a detached scratch worktree at `4a8e825` in the scratchpad (`git worktree add --detach`), restored with `git checkout` after the probe of A6 and removed after the review; the owner's rustos working tree was not read.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` ran on `/Users/robinonsay/rust/cwht` (query: software assurance iteration 2 delta, rule C1 liens and held record verdict) and on `/Users/robinonsay/rust/rustos` (query: `clk_sys` glitchless mux, aux select changed only off the aux path). One `grep -n` on the known file INSP-095, to find its iteration 2 section, ran before the first `search_code` query; that is out of the rule's order and is reported here. Afterwards `grep` only pinned lines in known paths (INSP-095, the plan rule C1, the datasheet extract written from `git show 2ec64c0:docs/extracted/rp2350-datasheet.md` to the scratchpad, `fake.rs`).

### Commands run by the assurance reviewer, iteration 2 (evidence)

| # | Command (read-only for both repositories; outputs in the scratchpad) | Result |
|---|---|---|
| A1 | `git rev-parse 4a8e825:<path>` for the nine rustos blobs; `git rev-parse HEAD:<path>` for the three cwht blobs; `git log e3ce2cb..HEAD` on them | all twelve equal to INSP-095 iteration 2 `product_files`; no cwht commit after `e3ce2cb` touches them |
| A2 | `git diff 213c536 4a8e825` (rustos) and `git diff` of each cwht blob pair; every hunk read | 4 rustos files, 196 added and 32 removed; ADR-051 sections 2, 4.3 and new 8; SW-01 product row, new "Phase 1, revision 2", phase 3 line; index rows of SW-01 to SW-05 |
| A3 | `cargo +1.98.0 test --offline -p pico2 --lib` at `4a8e825` | 37 passed, 0 failed |
| A4 | `cargo +nightly-2026-08-24 llvm-cov --offline -p pico2 --lib --branch` (MSR-14 form, never credit) | `clocks.rs` regions, functions, lines 100 %; `mod.rs` lines 72 of 73, branches 31 of 32, the one missed branch now `mod.rs:243` (True 36, False 0), the same `let Ok(vco) = u32::try_from(...)` `else` as iteration 1 `mod.rs:241` (finding-1, lines moved by the module doc) |
| A5 | `rust-code-analysis-cli --metrics` over `clocks/` and `common/` piped to `tools/complexity_gate.py --max 15 --yellow 12` (and `--yellow 11` to name the maximum); `cargo +1.98.0 clippy --offline -p pico2 --lib --target thumbv8m.main-none-eabihf -- -W clippy::pedantic -W clippy::arithmetic_side_effects`, filtered to the WP-SW-11 files | gate PASS, 94 functions, flight maximum `check_pll` CC 10, overall maximum 12 in the new test helper `assert_aux_changes_only_off_the_aux_path` (`clocks_tests.rs:396`, test code, none above 12); clippy reports only the iteration 1 sites (`module_inception` `mod.rs:41`, INSP-095 finding-6; `arithmetic_side_effects` `mod.rs:198, 211, 212, 234, 243, 252, 253, 256` and `reg.rs:166, 213`, INSP-095 finding-4, lines moved by 2); no lint on a line the fix adds |
| A6 | Probe, scratch worktree only, reverted: two tests appended to `clocks_tests.rs` using its own helpers. (a) `bring_up` from the restart state `RESTART`, comparing `regs.writes()` with `golden_writes()`. (b) `bring_up` from a start state with `clk_ref` on its aux mux from GPIN0 (`CLK_REF_CTRL = 0x21`), checked with `assert_aux_changes_only_off_the_aux_path` | (a) passes: the write order from the restart state equals the golden order. (b) fails: "AUXSRC of 0x30 changed on the aux path: Write { block: CLOCKS, offset: 48, value: 2 }" (step 4, finding-6). Worktree restored with `git checkout`, `git status` clean |
| A7 | Datasheet extract at `2ec64c0`: section 8.1.2.2 (lines 37735 to 37806), Table 555 `CLK_REF_CTRL` (line 39129), Table 558, section 7 reset sources "Watchdog" (line 36111) and `WDSEL` | the three sequences of 8.1.2.2 read against steps 3, 4, 7 and 8; `CLK_REF_CTRL.AUXSRC` "will glitch when switching", values `PLL_USB`, `GPIN0`, `GPIN1`, `PLL_USB_PRIMARY_REF_OPCG`; the watchdog "can trigger various levels of chip-level reset by setting appropriate bits in the WDSEL register", so a warm restart that keeps `CLOCKS` is possible |
| A8 | `tools/validate_docs.py` on this record | see the completion paragraph below |

### INSP-095 finding-1 under the assurance lens (items j and k)

| Case | At `4a8e825` | Assurance result |
|---|---|---|
| Step 3, `clk_sys` leaves aux | `clocks.rs:251` clears `CLK_SYS_CTRL_SRC` (bit 0, `regs.rs` new constant) through `ALIAS_CLR`; `:252-260` poll `CLK_SYS_SELECTED` for `clk_ref` with a bounded `wait` and `ClkSysToRefTimeout`. 8.1.2.2 "switch the glitchless mux to an alternate source" and "poll the SELECTED register". The aux select keeps whatever it holds, so the step works from any start state of `clk_sys` | Verified |
| Step 7, first `AUXSRC` write of `clk_sys` | `:322-331`: `CLK_SYS_DIV`, then `AUXSRC_PLL_SYS \| SRC_REF` while `SELECTED` last showed `clk_ref` (no write to `SRC` since step 3), then `SRC_AUX`, then a bounded poll for aux. 8.1.2.2 steps 3 to 5 | Verified |
| Step 8, `clk_peri` (no glitchless mux) | `:351` clears `ENABLE` alone; `:352-360` bounded wait for `ENABLED` = 0 with `ClkPeriStopTimeout`; `:361` writes `AUXSRC_CLK_SYS` with `ENABLE` still clear; `:362` divider; `:363` sets `ENABLE` alone; `:364-372` bounded wait for `ENABLED`. 8.1.2.2 "without a glitchless mux" steps 1 to 5 and the "polling ... CTRL_ENABLED" rule | Verified |
| Item j (bounded, no hang) | every new wait is the existing `poll` loop bounded by `poll_budget`, independent of TIMER0 (`reg.rs:203-219`, unchanged); with no aux change while a generator is on its aux path, the driver's own writes cannot stop `clk_sys` before a bounded wait runs (from the reset state and the tested restart state; finding-6 names the one start state outside them) | Yes |
| Item k (fault returned, safe state kept) | each new wait returns its named `ClockFault`; no application output is touched; a returned fault leaves `clk_sys` running from `clk_ref` or `PLL_SYS`, so the CS-11 halt of 07 section 14.2 row c can drive `safe_state()` | Yes |
| Test evidence | `no_aux_select_changes_while_its_generator_is_on_the_aux_path` replays the whole access log from `COLD` and `RESTART` and models the set and clear aliases, as `FakeRegs::write` does (`fake.rs:133-149`); the two should-panic tests reject the iteration 1 step 3 and step 8 writes; INSP-095 D9 shows the iteration 1 `clocks.rs` fails it. A3 reproduces 37 passes | Verified |
| Other hunks | `clocks.rs` step table and doc (lines 18 to 40) match the code; `mod.rs` module doc (lines 34 to 39) now claims no reset value is relied on and every field "the tree depends on" is written once its generator is off the aux path; ADR-051 section 2 says the same and quotes 8.1.2.2; section 4.3 separates revision 1 and 2 evidence and adds a dev-board case from a watchdog restart; section 8 revision table; SW-01 revision 2 phase and file lengths (`wc -l` 466, 499, 323, 222 as INSP-095 checked); index rows of SW-01 to SW-05 name the revision 2 commits, which are the heads of the five `cwht/` branches (`git branch -v`) | Consistent, apart from finding-6 (the "relies on no reset value" claim and step 4) and the carried text of finding-4 |

A residual, noted and not raised: in the restart state `clk_peri` runs from `PLL_SYS` through steps 5 and 6, so its source stops while the PLL is reset and resumes after `LOCK` with the post dividers powered only after lock. No aux select changes there, and the peripherals on `clk_peri` (UART, SPI, I2C) are not in use during bring-up, while the safe outputs are SIO on `clk_sys`. No hazard path.

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location (at `4a8e825`) | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | assurance | Minor | `swe-219 7.1 task 1`, `swe-062 7.1 task 1`, `swe-135 7.1 task 5` | `mod.rs:243-244`, `:249`; `tests.rs` (unchanged); ADR-051 revision 1 evidence line | CS-38 MC/DC pairs and one branch of `plan` not exercised (A4) | Open (lien, rule C1) | Pending | CDR readiness declaration |
| finding-2 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-a), `swe-062 7.1 task 1` | `clocks_tests.rs` `RESTART`, `no_aux_select_changes_while_its_generator_is_on_the_aux_path` | restart start state now tested for the aux rule and end values; the test does not assert the write order (A6 (a) shows it holds) | Open (lien, rule C1); fix narrowed below | Pending | CDR readiness declaration |
| finding-3 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-j, SA-C-l) | ADR-051 section 4.2 (unchanged); `clocks.rs` step 9; 07 section 14.2 row a; CS-37 | start order of the watchdog and the clock bring-up not defined | Open (lien, rule C1) | Pending | CDR readiness declaration |
| finding-4 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-g) | `clocks.rs` step 2 first `XOSC.CTRL` write (golden `0x0000_0aa0`, unchanged) | first `XOSC.CTRL` write is an invalid `ENABLE` code; `BADWRITE` never read or cleared. The doc part is partly met: ADR-051 section 2 no longer says "Every control field is written explicitly" | Open (lien, rule C1) | Pending | CDR readiness declaration |
| finding-5 | assurance | Minor | SA-D1 (`swe-134 7.1 task 6`) | `hazards.json` HZ-004, HZ-008 (not in this product) | timebase common cause not stated in the hazard data | Open (lien, rule C1) | Pending | CDR readiness declaration |
| <a id="finding-6"></a>finding-6 | assurance | Minor | `swe-134 7.1 task 2` (SA-C-j, SA-C-k), `swe-062 7.1 task 1` | `clocks.rs:261-262` (step 4); `mod.rs` doc lines 34 to 39; ADR-051 section 2 | step 4 writes `CLK_REF_CTRL.AUXSRC` without first taking `clk_ref` off its aux path | Open (lien, rule C1) | Pending | CDR readiness declaration |

### finding-2 (current state)

Revision 2 adds the restart start state `RESTART` (`clk_sys` on aux from `PLL_SYS`, `clk_ref` on the crystal, `clk_peri` running from `PLL_SYS`), with `healthy()` presetting `XOSC.STATUS` `STABLE`, `PLL_SYS` `LOCK` and the tick and counter status reads, and it checks the aux rule and the end values of `CLK_SYS_CTRL` and `CLK_PERI_CTRL`. That covers most of the iteration 1 fix. What remains is the order: no product test asserts that from `RESTART` the writes follow the golden order, so that `clk_sys` is confirmed on `clk_ref` before the first `RESETS` write. A6 (a) shows the order holds at `4a8e825`. **Fix (narrowed):** add `assert_eq!(regs.writes(), golden_writes())` to the `RESTART` pass of `no_aux_select_changes_while_its_generator_is_on_the_aux_path`.

### finding-6

**Minor, `swe-134 7.1 task 2` (SC), items j and k; `swe-062 7.1 task 1`.** Step 4 writes `CLK_REF_CTRL = CLK_REF_SRC_XOSC` (`clocks.rs:262`) as one word. That write sets `SRC` to the crystal and `AUXSRC` (bits 6:5) to 0 at once, and `clk_ref` is never confirmed off its aux path first. Table 555 says `AUXSRC` "will glitch when switching", and 8.1.2.2 requires the generator to be off its aux path before any aux change. This is the INSP-095 finding-1 defect class, for `clk_ref`, in the one start state the revision 2 test does not cover: `clk_ref` on its aux mux (`SRC = 1`) with `AUXSRC` not 0 (`GPIN0`, `GPIN1` or `PLL_USB_PRIMARY_REF_OPCG`). At that point `clk_sys` runs from `clk_ref` (step 3), so a `clk_ref` glitch reaches the core before the step 4 bounded wait can run. The test's own model already covers `clk_ref` (the `CLK_REF_CTRL` generator of `assert_aux_changes_only_off_the_aux_path`), and A6 (b) shows it fails from `CLK_REF_CTRL = 0x21`.

The driver's documents claim this state is handled. The `mod.rs` doc and ADR-051 section 2 say the driver "relies on no reset value" and changes an aux select "only while the generator is off its aux path". The `clocks.rs` doc gives the purpose of step 3 as a start state left by "the bootrom or an earlier image", and a watchdog reset keeps `CLOCKS` unless `WDSEL` selects it (A7).

**Severity: Minor.** No cwht image puts `clk_ref` on its aux mux. The reset value of `CLK_REF_CTRL` is the ROSC (Table 555). The state needs a warm restart that keeps `CLOCKS` after an image that used `clk_ref` aux with a non-zero `AUXSRC`. INSP-095 finding-1, by contrast, was reached on every cold boot.

**Fix:** in step 4, take `clk_ref` off aux before the `AUXSRC` field changes. One way is to clear `SRC` through `ALIAS_CLR` (to the ROSC), poll `CLK_REF_SELECTED` for the ROSC, then write the full word. Another is to write `SRC` alone and never change `AUXSRC`. Add a `clk_ref`-on-aux start state to the `no_aux_select_changes_...` loop. If the author judges the state out of scope instead, narrow the "relies on no reset value" sentence of the `mod.rs` doc and ADR-051 section 2 to the start states the driver handles.

### Task table and section C, re-answered for iteration 2

| Task or item | Iteration 2 answer | Evidence | Finding ids |
|---|---|---|---|
| swe-134 7.1 task 2 (SC) | Yes | items j and k now hold from the reset state and the tested restart state (table above); items a and g hold with Minor gaps | findings 2, 3, 4, 6 (liens) |
| swe-087 7.1 task 4 (SC) | Yes | the Major that carried the No is Verified in both records | none |
| swe-087 7.1 task 2 | Yes | the one earlier Major (INSP-095 finding-1) is addressed and verified; the earlier Minor findings are liens under rule C1, not silently dropped (ADR-051 section 8 and SW-01 revision 2 both say so) | none |
| swe-088 7.1 task 2 | Yes | INSP-095 iteration 2 and this delta record the verification case by case with commands (INSP-095 D1 to D10; A1 to A8) | none |
| swe-060 7.1 task 1 | Yes | the step table and ADR-051 section 2 match `bring_up` at `4a8e825`; the design now follows 8.1.2.2 for `clk_sys` and `clk_peri`, and not yet for `clk_ref` in the finding-6 start state | finding-6 |
| swe-062 7.1 task 1 (SC) | No | 37 tests pass (A3); the gaps of findings 1 and 2 remain, and finding-6 adds an untested start state | findings 1, 2, 6 |
| swe-135 7.1 task 5 (SC), swe-219 7.1 task 1 (SC) | No | A4: unchanged from iteration 1 | finding-1 |
| swe-135 7.1 task 6 (SC), swe-220 7.1 tasks 1 and 2 (SC) | Yes | A5: flight maximum CC 10, overall 12 in test code, none above 12 | none |
| swe-061 7.1 task 2, swe-185 7.1 task 1 | No | A5: INSP-095 findings 4 to 7 unchanged (liens) | INSP-095 findings 4 to 7 |
| SA-C-a | Yes | as iteration 1; the restart start state is now tested for the aux rule | finding-2 |
| SA-C-g | Yes | as iteration 1 | finding-4 |
| SA-C-j | Yes | table above, item j | finding-3, finding-6 |
| SA-C-k | Yes | table above, item k | finding-6 |
| SA-E1 | Yes | INSP-095 finding-1 verified in both records; this record's findings carried as liens with owner and due event | none |
| SA-E3 | Yes | cwht revision 2 on main at `e3ce2cb` with the `Co-Authored-By` trailer, not a baselined item; rustos `4a8e825` on the unmerged branch, its message citing INSP-095 finding-1; pin unchanged until PCR-4 | none |

All other iteration 1 answers stand: the product change touches none of them (A2).

### Cross items, iteration 2

X-1 is done: INSP-095 carries `paired_record: INSP-106`. Its `assurance_verdict: pending` now becomes `APPROVED` from this record; the file reviewer or the software lead copies it (07 section 10.2). X-2 to X-5 stand as at iteration 1.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 228 changed lines of `213c536..4a8e825` and the 26 changed lines of ADR-051, SW-01 and the index, every hunk, with `fake.rs` read for the alias semantics. Unsafe sites added or changed: none. Findings: 1 new (Minor, finding-6); 0 Major. INSP-095 finding-1 verified under the assurance lens. Effort of this iteration: about 30 turns and 50 minutes (the front matter totals include iteration 1).

### Completion, iteration 2

`assurance_verdict: APPROVED` and `reviewer_verdict: APPROVED`. No Major is open, and findings 1 to 6 are Minor liens under rule C1, due at the CDR readiness declaration. Findings 1, 2, 3, 4 and 6 are owned by the firmware developer and finding-5 by the WP-PDR-16b writer. The record `verdict` stays `NEEDS CHANGES`. The reviewed rustos blobs exist only on unmerged branches, and INSP-095 readiness R3 and R5 do not hold. The software lead sets `verdict` when the owner's merge and PCR-4 bring `4a8e825` into a configuration cwht consumes (lead SE convention of 2026-09-27).

```
ASSURANCE VERDICT: APPROVED (iteration 2 delta; record verdict held NEEDS CHANGES)
PRODUCT: rustos cwht/wp-sw-11 at 4a8e825 (12 blobs of product_files); PAIRED RECORD: INSP-095 iteration 2
FINDINGS:
- INSP-095 finding-1 (Major): Verified under the assurance lens (items j, k).
- [Minor] finding-1 to finding-5: carried as liens (finding-2 fix narrowed to one assertion).
- [Minor] finding-6 (new) swe-134 task 2 items j, k: step 4 writes CLK_REF_CTRL.AUXSRC without taking clk_ref off aux.
MEASUREMENTS: delta 228 rustos + 26 cwht lines; tasks_no=5; turns=30; minutes=50; major=0; minor=6 (1 new)
```
