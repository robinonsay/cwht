---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/05-configuration-and-data-management.md section 9.2 step 3). Record of the independent review
# of TV-020 to TV-023 (PDR work plan WP-PDR-08, record path as the plan names it).
# Item set applied: docs/templates/peer-review-checklist-tool-validation.md revision A, blob 7be809d4, on
# branch cr/CR-012-pdr-checklist-templates at 7784672 (APPROVED by INSP-033 iteration 2; CR-012 Submitted,
# not merged). The template is not on main, and tools/validate_docs.py rejects a checklist field whose
# template is absent from docs/templates/, so the checklist field names the code checklist, as INSP-015 did
# for the SRR TV set (the code checklist applied to the fixture sources, plus the TV item set). Cross item
# X-1: switch the field to peer-review-checklist-tool-validation in the delta after CR-012 merges.
id: INSP-040
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md
product: docs/cm/tool-validation/TV-020-rust-toolchain.md
# product_commit: 71bf509 holds the four TV records; the runs they record are at d3de579, which holds the
# fixtures and the procedure with the same blobs (git diff d3de579 71bf509 on the Rust fixtures, the procedure
# and firmware/ is empty)
product_commit: "71bf509c948fbc8d4ae9b863f2a0226f0bf1bba0"
product_files: ["docs/cm/tool-validation/TV-020-rust-toolchain.md@b020c973dcf7c0bb9c0a227d1e76025b481bd80c", "docs/cm/tool-validation/TV-021-cargo-llvm-cov.md@932d46295ed270095fe6a60964c2415bdff95db0", "docs/cm/tool-validation/TV-022-cargo-nextest.md@308dcf66b4196c3a7127a7060e0cae93592c6931", "docs/cm/tool-validation/TV-023-nightly-miri.md@dd169983c878910728e32154eca4dd01aea82f0b", "docs/cm/tool-validation/evidence/rust-tv-2026-09-27.sh@4c7cb7534b96e77cea16c601dfa00c2f42b3ae1a", "docs/cm/tool-validation/evidence/rust-tv-2026-09-27.log.txt@ac0ac0036cee9ad6b68f0aaf6895dfddd1aab556", "tools/toolchain.lock.md@82005d1b780e272dbf38cd8621d9707996e08f12", "docs/cm/tool-validation/README.md@b267ce08f53a5db8e32eb8cb217435a3efaf1833", "tools/tests/fixtures/rust/pdr-known-answers.json@0e7d72ac78e351e926ebeaab91646d09e080250f", "tools/tests/fixtures/rust/known-answers.json@6311da66a6047b51fa6fe4500e4019c58aba2a00", "tools/tests/fixtures/rust/cond-kat/Cargo.lock@e182713ad234cb0299e19db21bdd60fba19f823a", "tools/tests/fixtures/rust/cond-kat/Cargo.toml@e0766feaaaa3ccf98b4695a05923e6effb263843", "tools/tests/fixtures/rust/cond-kat/src/lib.rs@d5b59f44c44a317687f69aea2aceaddaa2dd6580", "tools/tests/fixtures/rust/cov-kat/Cargo.lock@2b383527992def7ad32c9cad707a6a5a9f46c50e", "tools/tests/fixtures/rust/cov-kat/Cargo.toml@e1e0dbbd1665d11c986110dc3541dfa769932650", "tools/tests/fixtures/rust/cov-kat/src/lib.rs@19ded2eadfe063724c21a43a379a5686150380b6", "tools/tests/fixtures/rust/harness-seeded/.config/nextest.toml@a555946aa3ee04e122b8d22df4f50b9e898e556e", "tools/tests/fixtures/rust/harness-seeded/Cargo.lock@0cb6c2dc1a752c57d88bbc79a55720c45f23ab77", "tools/tests/fixtures/rust/harness-seeded/Cargo.toml@386895fd4e74d812e220f70aa75cf24568ec6f04", "tools/tests/fixtures/rust/harness-seeded/src/lib.rs@7f901c951148cc5f6cc19731b8851c4cdb15b8b4", "tools/tests/fixtures/rust/harness-seeded/tests/harness.rs@e62465bc00f2bfd9beb6e80f0f671fcbb8758613", "tools/tests/fixtures/rust/kat-host/Cargo.lock@6e442470154fa509b20b5e1480ac644d2044473a", "tools/tests/fixtures/rust/kat-host/Cargo.toml@fd9ad9df3ed607030dbe5f4459081da1cff04f99", "tools/tests/fixtures/rust/kat-host/clippy.toml@42020b54612e1bcb2c64149353575b6fa6883d96", "tools/tests/fixtures/rust/kat-host/src/lib.rs@1ac6e57e8dc73773077b8a90a65ac9300e6e09af", "tools/tests/fixtures/rust/kat-target/.cargo/config.toml@6ae26913b43fd609fe0e7e78b6ad886dededb810", "tools/tests/fixtures/rust/kat-target/Cargo.lock@7fed9133c31179b0096217c07862c51812d90827", "tools/tests/fixtures/rust/kat-target/Cargo.toml@d9edf91cdd893fca406e44bd24fb88281f2b2dc9", "tools/tests/fixtures/rust/kat-target/build.rs@4753901c8962d0fa4cc459f00c7e85b246bfcda0", "tools/tests/fixtures/rust/kat-target/link.x@70b6d0d8b890d41e4a5db43aa25d06aefb158779", "tools/tests/fixtures/rust/kat-target/src/main.rs@d97ecd8135bfecf4958de803b452cdfce2f2ee82", "tools/tests/fixtures/rust/miri-kat/Cargo.lock@c0e750f3f8397c332f8dd655714a347524142712", "tools/tests/fixtures/rust/miri-kat/Cargo.toml@24a25655c2a40e9c18a616bb4f913e90a207d928", "tools/tests/fixtures/rust/miri-kat/src/lib.rs@84e8f8c9c46190843074170b4220fb546d153f36"]
fixture_trees: ["tools/tests/fixtures/rust/kat-target@1eae87cd88cfec51f5b46f8450b24a2dd7f5894c", "tools/tests/fixtures/rust/kat-host@d70d2554d7ca0f4c3e7e16fdebbb7998cbe80f9a", "tools/tests/fixtures/rust/cov-kat@970e59d5059906dfea91dd2bae5769da2d66fc0d", "tools/tests/fixtures/rust/cond-kat@cca3b34803faee4b9f4a39f4b993e5fc656202f2", "tools/tests/fixtures/rust/miri-kat@bf632e485880160f57271332f77cc5ea9de78ce4", "tools/tests/fixtures/rust/harness-seeded@dbc9eae482a0a62f663b66d0f3ca7e36fddfb0b0"]
tv_ids: [TV-020, TV-021, TV-022, TV-023]
# tool_class: TV-020 A (build) and B (test, clippy); TV-021, TV-022 B; TV-023 B non-credit
tool_class: A and B
tool_kind: external-tool
acc_proposed: [ACC-RUST-001, ACC-LLVMCOV-001, ACC-NEXTEST-001, ACC-NIGHTLY-001]
product_size: 4 records, 13 purposes, 22 known-answer checks (K20-1 to K20-6, K21-1 to K21-3, K22-1 to K22-7, K23-1 to K23-6), 6 fixture directories (34 files), 1 procedure, 1 log
sprint: PDR-prep
author_agent: "author:WP-PDR-08 (Claude as software lead and tool owner)"
tool_author_agent: n/a (external tools)
reviewer_agent: "reviewer:WP-PDR-08-rust-toolchain (independent, iteration 1)"
criticality: neither
# assurance_required: the TV template (CR-012) says false; PDR work plan WP-PDR-08 names "independent reviewer
# plus SA". Section H is answered here as the template directs; the separate SA invocation the plan names is
# requested from the lead SE (return fix_requests "SA pair needed"); cross item X-2.
assurance_required: true
assurance_reviewer_agent: "pending (separate invocation, PDR work plan WP-PDR-08)"
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 5
findings_open: 7
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
deferred_rids: []
items_no: [TV-B3, TV-C2, TV-C3, TV-C5, TV-E1, TV-G2-1]
effort_turns: 40
effort_minutes: 55
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-040: TV-020 to TV-023 (Rust toolchain, cargo-llvm-cov, cargo-nextest and the HostUnit harness, nightly-2026-08-24 with Miri)

**Product:** `docs/cm/tool-validation/TV-020-rust-toolchain.md`, `TV-021-cargo-llvm-cov.md`, `TV-022-cargo-nextest.md` and `TV-023-nightly-miri.md` at `71bf509`, with the fixtures, procedure and log at the blobs of `product_files` (runs at `d3de579`; the fixture, procedure and `firmware/` blobs are equal at both commits). **Checklist:** the item set of `docs/templates/peer-review-checklist-tool-validation.md` revision A (CR-012 branch `7784672`, blob `7be809d4`), `tool_kind` external-tool, so sections A to F, G2 and H; front matter comment explains the `checklist` field. **Acceptance criteria (rule C7):** every item of sections A to F, G2 and H for each of the four records; every row of 05 section 9.2 for these tools; the 07 section 17.3 accreditation elements (sanity checks, MSR-28, byte-identical rebuild of the rustos blinky, HostUnit suite twice identical); 03 section 6.5 item X10 (seeded failing independence pair and seeded mock fault); the E-14 software part (07 sections 7 and 8 against the lock).

**Independence (rule C4):** this invocation authored no part of WP-PDR-08 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: code review of `tools/measurements.py`; the D13 rustup guard; the 05 section 13 PDR row). `grep -n` was used afterwards only to pin lines. **No download:** every reviewer run was offline (`CARGO_NET_OFFLINE=true`, `RUSTUP_AUTO_INSTALL=0`, `MIRI_AUTO_OPS=no`) behind a copy of `docs/vv/reports/TC-SW-TOOL-001-r3/rustup-guard.sh` first on `PATH`; rustos was taken only by `git archive` of the pin object `2ec64c0`, never from the owner's working tree.

**Not held: TV-024 (`tool-validation-python-analysis.md`).** TV-024 is Draft with no run (its section 4 "None"; ruff and coverage.py not installed, owner action A-1). Readiness R2 and R5 of the checklist cannot be met, and TV-024 section 8 itself schedules the review after run 1. No record is filed and no INSP number is taken for it; the review is held after the owner's A-1 permission and run 1.

## Reviewer re-run (item TV-C5)

Command, from the scratchpad, on a fresh `git archive` export: `sh rust-tv-2026-09-27.sh <scratch>/rr1 <scratch>/guard d3de579` (the script byte-equal to blob `4c7cb753`, `cmp` exit 0). Exit 0, 2026-09-27 11:39:57 to 11:40:19 CDT. Results against the record:

| Check | Record (runs 1 and 2) | Reviewer run | Same? |
|---|---|---|---|
| Section 0 identity | versions, binary and manifest SHA-256 of TV-020 section 1, TV-021, TV-022, TV-023 section 1 | identical strings and hashes | yes |
| K20-1 | three ELF `3201d382...df7d` | three ELF `3201d382...df7d`, equal to stored | yes |
| K20-2 | clean 3 passed exit 0; seeded exit 101 `tests::seeded_failure` | same | yes |
| K20-3 | clean 0; `absurd_extreme_comparisons` 101; `unwrap_used` 101 | same | yes |
| K20-4 | layout A ELF twice equal; three loadable images `c6d27ba1...31df` equal to the reference | layout A ELF `201490f2...` twice (pass); loadable images of layout A and layout B both `7c20cba4...6857`, **not** equal to the reference `c6d27ba1...31df`; same size 2008 B and same section sizes (`rust-size -A`), `main` and `rust_begin_unwind` swapped (`rust-nm -n`), 186 differing bytes | **no** (finding-1) |
| K20-5 | layout A ELF twice equal; loadable images `828bca35...61f4` equal to the reference | layout A ELF `66df543b...` twice; loadable images `828bca35...61f4` (a1, a3, reference); 7 path strings | yes |
| K20-6 | nextest 10 passed twice, triples identical; `measurements.py --diff-runs` PASS; `cargo test` outputs identical | same | yes |
| K21-1, K21-2 | `TOTAL 13 0 100.00% 3 0 100.00% 7 0 100.00%` exit 0; `6| 0| 1` exit 1 | same | yes |
| K21-3 | lcov identical, `cwht-core` 17 of 17, `cwht-hal-mock` 53 of 53 | same | yes |
| K22-1 to K22-7 | as TV-022 section 4 | same outcomes, exit 100 for every seeded run, JUnit failed lists equal | yes |
| K23-1 to K23-6 | as TV-023 section 4 | same, including the Undefined Behavior message and `-p api --lib` 0 tests | yes |

Additional reviewer check (finding-2): `cargo +1.98.0 llvm-cov --locked --features seeded-gap --lcov` on `cov-kat` in the export writes `DA:6,0`, `LF:6`, `LH:5`, and `tools/measurements.py --coverage` on it prints `lines 5/6 = 83.33 %`: the tool is correct, but no known answer of the record shows it.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | TV-B3, TV-C5, TV-E1 | TV-020 section 2 purpose 4; section 3 K20-4 pass criterion; section 4 run 1 and 2 K20-4 rows; `pdr-known-answers.json` `rustos-blinky` | Purpose 4 claims "clean builds in different layouts give byte-identical loadable images", and K20-4 requires the blinky loadable images to equal the reference, "or, where it differs, differing only by function order with identical section sizes". The record's own dry run (log appendix) and the reviewer re-run refute the claim: at the reviewer's scratch path both layouts gave `7c20cba4...` against the reference `c6d27ba1...` (function order swapped, section sizes equal). The recorded "equal to the reference" is a property of the author's scratch path, not of the tool, and the escape clause makes K20-4 a hand judgement that cannot fail mechanically. Limitation 1 states the cause correctly but contradicts purpose 4, and the same mechanism (path-dependency crate hashes; `firmware/Cargo.toml` takes rustos `api` by path) applies to `cwht-app`, whose cross-layout equality in three builds is chance, as limitation 1 itself says. Fix: restate purpose 4 as same-absolute-path identity (ELF and loadable image of two clean builds at one path, which MSR-28 and `tools/release.sh --rebuild-check` need); make K20-4 and K20-5 criteria mechanical (same-path ELF and loadable identity; the cross-layout comparison reported as an observation with section sizes compared by command, not as a pass criterion); bring the `pdr-known-answers.json` `rustos-blinky` and `cwht-app` entries and the ACC-RUST-001 wording in line; state in 07 section 17.3 terms what "byte-identical rebuild of the rustos blinky" means (two rebuilds at one path), since the committed reference ELF is reproducible only at its own build path | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | TV-C2, TV-B3 | TV-021 section 2 purpose 3; section 3 K21-1 to K21-3 | Purpose 3 claims the `lcov` export (read by `tools/measurements.py --coverage` for the credited MSR-13 values) and the text report. Only the text report has a seeded fault (K21-2, line 6). The `lcov` export is checked only on fully covered input (K21-3), so an export that dropped zero-count lines or wrote `LH` equal to `LF` would pass every known answer, while the MSR-13 value recorded from it would read 100 percent. Class B requires a seeded fault per purpose (05 section 9.2 step 1; checklist TV-C2). The reviewer check above shows the tool itself is correct. Fix: add a K21 case that exports `lcov` for `cov-kat --features seeded-gap` and asserts `DA:6,0`, `LF:6`, `LH:5` (and the `measurements.py --coverage` line `lines 5/6`), store it in `pdr-known-answers.json`, re-run | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | TV-A1, TV-E2 | TV-020 section 1 and section 7; procedure sections 4 and 5 | The loadable-image comparisons of K20-4 and K20-5 use `rust-objcopy` (cargo-binutils 0.4.0, which runs the `llvm-objcopy` of the toolchain rustup resolves in the procedure's working directory, not the `firmware/` pin). Neither its version nor that resolution is recorded in TV-020 section 1, and a cargo-binutils change is not a re-validation trigger. Fix: identify `rust-objcopy --version` and the toolchain it resolves in section 0 of the procedure and in TV-020 section 1; run it with `+1.98.0` or from `firmware/`; add the trigger | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | TV-C3 | TV-020 section 3; TV-021 section 3; TV-023 section 3; `pdr-known-answers.json` | The records do not state how each expected answer was obtained. The discriminating answers are derivable from the fixture sources by hand (the failing test names, exit statuses, line 6 of `cov-kat`, the unexercised False outcome of `b`, the out-of-bounds read at offset 0x10 of a 16-byte allocation), but the totals `cov-kat` 13 lines, 3 functions, 7 regions, the workspace 17, 53, 4 of 4 branches and 70 of 70 lines, and the reference hashes are earlier outputs of the same tools (the 2026-09-26 sanity checks and TC-SW-TOOL-001 run 3). Fix: add a provenance column (hand-derived with the derivation, or earlier output of the tool with its run) per answer; hand-count the `cov-kat` line total from the lcov `DA` lines | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | TV-G2-1, TV-B2 | `tools/sw_gate.sh` lines 129 to 130, 137, 241 at `71bf509`; TV-020 purposes 1 and 3; TV-022 purpose 1 | The gate commands differ from the validated ones: G1 runs a target clippy (`cargo clippy -p cwht-app --target thumbv8m.main-none-eabihf -- -D warnings`) that K20-3 does not exercise (host fixture only), and G2 `cargo build` and G3 `cargo nextest run` run without `--locked`, which purposes 1 and K22 include. Fix: add a target clippy seeded lint to K20-3 or state purpose 3 as host and target with the target case covered; make the gate commands and the purposes name the same flags (a change to `tools/sw_gate.sh` belongs to its writer, WP-PDR-09) | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | TV-D2, TV-E2 | procedure section 10 (`junit` after each feature run) | The procedure reads `harness-seeded/target/nextest/ci/junit.xml` after each of the four feature runs without deleting it first, so a run that failed to build would report the previous run's JUnit list. The recorded runs are valid (every seeded run exited 100, a test failure, not 101), but the procedure cannot tell a stale file from a fresh one. Fix: remove the JUnit file before each run and check its time stamp or the run exit status explicitly | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | E-14 (acceptance criterion) | TV-020 Annex A | Annex A omits 07 CS-26 (`rustfmt`, `cargo fmt --check`, gate G1), a tool of the pinned toolchain that the gate runs; no TV record covers it and 05 section 13 does not schedule one. Its version row also transcribes the lock's `cargo-audit-audit 0.22.2` without noting it as the lock's typo. Fix: add the CS-26 row with its state (not scheduled for a TV record; evidence class) and note the lock string | Open | Pending | |

### Per-record results

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-020 | rustc `1.98.0 (88d9e12ae 2026-08-18)`, cargo `1.98.0 (797e8a9bc 2026-08-05)`, clippy `0.1.98 (88d9e12ae1 2026-08-18)` | A (build), B (test, clippy) | `d3de579` | procedure sections 0 to 6; exit 0; K20-1 to K20-3, K20-5, K20-6 same; K20-4 different | TV-B3, TV-C3, TV-C5, TV-E1, TV-G2-1 | finding-1, finding-3, finding-4, finding-5, finding-7 |
| TV-021 | cargo-llvm-cov 0.9.1, LLVM 22.1.8 | B | `d3de579` | sections 7 and 8; exit 0; same | TV-B3, TV-C2, TV-C3 | finding-2, finding-4 |
| TV-022 | cargo-nextest `0.9.146 (8af696ddc 2026-09-21)` and the harness | B | `d3de579` | sections 6, 9, 10; exit 0; same | none | finding-5, finding-6 |
| TV-023 | nightly-2026-08-24 `1.100.0-nightly (fb6531d55 2026-08-23)`, miri `0.1.0 (fb6531d550 2026-08-23)`, LLVM 23.1.0 | B non-credit | `d3de579` | sections 11 to 14; exit 0; same | TV-C3 | finding-4 |

### Per-purpose results

| TV record | Purpose | Known answer that exercises it | Seeded fault (class B) | Cited uses of the purpose | Finding ids |
|---|---|---|---|---|---|
| TV-020 | 1 build | K20-1, K20-5 | n/a (class A: reproducibility K20-1, K20-5) | gate G2; MSR-28; `tools/release.sh` (planned) | finding-5 |
| TV-020 | 2 `cargo test` | K20-2, K20-6 | `seeded-fail`, exit 101 | reference runner (07 section 8.1) | none |
| TV-020 | 3 clippy | K20-3 | `seeded-lint`, `seeded-unwrap`, exit 101 | gate G1 host and target; MSR-07 | finding-5 |
| TV-020 | 4 reproducibility | K20-1, K20-4, K20-5 | n/a (class A) | MSR-28; 07 section 17.3; `tools/release.sh --rebuild-check` | finding-1, finding-3 |
| TV-021 | 1 coverage | K21-1, K21-3 | `seeded-gap` (K21-2) | gate G6; MSR-13; TC-SW-COV-001 | finding-4 |
| TV-021 | 2 thresholds | K21-1, K21-2 | `seeded-gap`, exit 1 | gate G6 | none |
| TV-021 | 3 lcov and text export | K21-2 (text), K21-3 (lcov, full coverage only) | text only | `tools/measurements.py --coverage` (G6), MSR-13 records | finding-2 |
| TV-022 | 1 runner | K22-1 to K22-3, K22-7 | `seeded-fail`, exit 100 | gate G3 | finding-5 |
| TV-022 | 2 JUnit triples | K22-3 to K22-7 | seeded pair and mock fault in JUnit | gate G3 with `measurements.py --diff-runs`; SWE-186, SWE-191 | finding-6 |
| TV-022 | 3 X10 fault path | K22-4 to K22-6 | `seeded-pair` (condition `b` masked, `permit(true,false)` returns true), `seeded-mock-fault` (`failing_after(1)`, second write refused): each fails for the stated reason (fixture source read) | 03 section 6.5 item X10; 03 section 4.3.1 | none |
| TV-022 | 4 runner of llvm-cov | K21-3, K23-3 | via K21-2 | gate G6 | none |
| TV-023 | 1 MSR-14 | K23-1 to K23-3 | `cond-kat` default (False: 0 of `b`) | gate G6 MSR-14; SWE-219 record (non-credit) | finding-4 |
| TV-023 | 2 Miri | K23-4 to K23-6 | `seeded-oob`, exit 1 with the UB message | gate G5; MSR-08 | none |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Everything committed; blobs and trees listed | Yes | `git rev-parse 71bf509:<path>` equals HEAD for every TV record, fixture, procedure and log; `git status --short` on these paths prints nothing. The lock and README blobs moved after `71bf509` only by the TV-014 hunks of `b362395` (`git log 71bf509..HEAD`), not by a WP-PDR-08 row. The brief's `product_files` named fixture directories; this record lists them file by file with `fixture_trees`, as the template requires |
| R2 | Known-answer command exits 0 | Yes | reviewer re-run exit 0 |
| R3 | unit tests and `validate_docs.py` pass | No, not attributable to this product | `validate_docs.py` exit 1 before this record: 2 SRR records fail the drift rule (`risk-register-06.md`, `tool-validation-tv-001-to-tv-010.md`, blobs of the register, lock and README moved), and `test_validate_docs.RepositoryTests.test_repository_exit_zero` fails for the same reason (453 tests, 1 failure). Not held against this review; cross item X-3 |
| R4 | Lock rows and README index | Yes | lock section 1 rows rustc, cargo, nightly-2026-08-24, llvm-tools, cargo-llvm-cov, cargo-nextest; section 1.1 rows with the 2026-09-27 runs and the new X10 row; section 5 rows; README rows TV-020 to TV-023 |
| R5 | Author return lists purposes, uses, tests, runs, scopes | Yes (partly) | the author summary in the assignment gives runs, commits, results and findings; purposes and scopes are in the records |

## A. Identification

| Id | Answer | Evidence |
|---|---|---|
| TV-A1 | Yes for the four records, No for the comparison tool (finding-3) | reviewer section 0 prints the recorded version strings and binary hashes; `rust-objcopy` not identified |
| TV-A2 | Yes | TV-020: channel manifest URL and installed manifest SHA-256 `b17aaaed...`; TV-023: dated nightly manifest SHA-256 `0bfdc1de...`; TV-021, TV-022: crates.io with no upstream binary checksum, substitute stated (binary SHA-256 and `.crates2.json`, limitations 4 and 5) |
| TV-A3 | Yes | recomputed at `71bf509`: trees `1eae87cd`, `d70d2554`, `970e59d5`, `cca3b348`, `bf632e48`, `dbc9eae4`; blobs `0e7d72ac`, `6311da66`, `4c7cb753`; `firmware/` blobs `7799f6b6`, `784605ca`, `ca29c254`, `00b81042`, `42020b54` as the log prints |
| TV-A4 | Yes | `d3de579` contains the fixtures, procedure and `firmware/` exactly as identified (`git diff --stat d3de579 71bf509` on those paths is empty) |
| TV-A5 | Yes | TV-020 A (image) and B; TV-021, TV-022 B; TV-023 B non-credit, per 05 section 9.1 |
| TV-A6 | Yes | shell procedure, offline, no GUI |

## B. Purposes

| Id | Answer | Evidence |
|---|---|---|
| TV-B1 | Yes | each purpose is one line with command, output and exit status |
| TV-B2 | Yes, with finding-5 | searched uses: `tools/sw_gate.sh` G1, G2, G3, G5, G6; 07 sections 8.1, 8.4, 9.5, 9.6, 11.2, 17.3; TC-SW-TOOL-001; `measurements.py --coverage`. Every use maps to a purpose; the target clippy and the unlocked gate commands are the gaps of finding-5 |
| TV-B3 | No | TV-020 purpose 4 (finding-1); TV-021 purpose 3 (finding-2) |

## C. Known-answer test

| Id | Answer | Evidence |
|---|---|---|
| TV-C1 | Yes | `tools/tests/fixtures/rust/` with answers in `known-answers.json` and `pdr-known-answers.json`; command and criteria in each section 3 |
| TV-C2 | No | TV-021 purpose 3 `lcov` has no seeded fault (finding-2); every other class B purpose has one (per-purpose table) |
| TV-C3 | No | provenance not stated per answer (finding-4) |
| TV-C4 | Yes | 05 section 9.2 rows rustc/cargo, clippy, cargo-llvm-cov, nightly and cargo-nextest implemented (lock section 1.1 rows); 07 section 17.3 elements present |
| TV-C5 | No | K20-4 differs at the reviewer's path (finding-1); all other checks same |

## D. Results and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| TV-D1 | Yes | section 4 rows with time, commit, results; log sections 0 to 14 for both runs |
| TV-D2 | Yes | lock section 1.1 rows name 2026-09-27 runs 1 and 2 at `d3de579` and the evidence file |
| TV-D3 | Yes for the fixed path, see finding-1 | K20-1 ELF identical in three directories; K20-4 and K20-5 same-layout ELF identical in both runs and in the reviewer run |

## E. Limitations and triggers

| Id | Answer | Evidence |
|---|---|---|
| TV-E1 | No | TV-020 limitation 1 confirmed by the reviewer run but contradicts purpose 4 (finding-1). Confirmed without contradiction: TV-022 limitation 3 (the JUnit file under the fixture's `target/nextest/ci/`), TV-023 limitation 3 (`-p api --lib` 0 tests), TV-021 limitation 3 (absolute `SF:` paths, reviewer lcov) |
| TV-E2 | Yes, with finding-3 | version, fixture, OS major, defect (NCR) triggers present in all four; class A expiry at each baseline in TV-020; the `rust-objcopy` trigger missing |

## F. Accreditation readiness and indexes

| Id | Answer | Evidence |
|---|---|---|
| TV-F1 | Yes, subject to finding-1 | ACC-RUST-001 (fixed absolute path condition), ACC-LLVMCOV-001, ACC-NEXTEST-001, ACC-NIGHTLY-001 name purposes, versions and conditions |
| TV-F2 | Yes | due PDR per 05 section 13 PDR row (`docs/process/05-configuration-and-data-management.md` line 587) |
| TV-F3 | Yes | README rows, lock section 5 rows and headers: Validated 2026-09-27, review pending, due PDR |
| TV-F4 | Yes | each section 9 leaves the decision to the owner; output is developer evidence until then |
| TV-F5 | N/A | first validation, no accredited version changed |

## G2. External tools

| Id | Answer | Evidence |
|---|---|---|
| TV-G2-1 | No | finding-5 (target clippy, `--locked`) |
| TV-G2-2 | Yes | the one observed hang (cargo-miri install prompt, TC-SW-TOOL-001-r3 D14) is prevented by `MIRI_AUTO_OPS=no` and the rustup guard; no other tool of the set waits on input; the reviewer run completed in 22 s |
| TV-G2-3 | Yes | installs recorded under SRR decision 109 and close-out item 2 (lock section 1.4 finding 8, section 7); no download in the recorded runs or the reviewer run |

## H. Software assurance tasks (answered by this reviewer as the template directs; the separate SA invocation of WP-PDR-08 is still requested)

| Id | Answer | Evidence |
|---|---|---|
| TV-H1 | Yes, with findings 1, 2 and 5 | 07 section 8.4 steps G1 (clippy, TV-020), G2 (build, TV-020), G3 (nextest, TV-022; diff by TV-013), G5 Miri (TV-023), G6 (TV-021, TV-023) are each covered by a purpose; G1 `cargo fmt` is not (finding-7) |
| TV-H2 | N/A | no analysis tool in this set; coverage is a verification measure, answered under TV-H1 |
| TV-H3 | Yes | `assurance_tasks_applied` lists both tasks |

## Code checklist (fixture sources; revision B items that apply to test fixtures)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A3 | Yes | the only `cfg(feature)` switches are the seeded faults, named and documented in each `Cargo.toml` |
| CK-CODE-B2 | Yes | `miri-kat/src/lib.rs` lines 10, 22, 36: each `unsafe` has a SAFETY comment; the seeded site states it violates the contract |
| CK-CODE-E1 | Yes | `harness-seeded`: KAT/D01 `permit = a && b`, pairs tagged `@mcdc` as 07 section 9.6 item 2; `cov-kat` and `cond-kat` match their Cargo comments |
| CK-CODE-H1 | Yes | `harness-seeded` uses the real `cwht-core` `Heartbeat` and `cwht-hal-mock` `MockOutput` by path |
| Other items | N/A | fixtures are not image code (no_std, MMIO, safety-critical, traceability tags do not apply) |

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 4 records (393 lines), 13 purposes, 22 checks, 34 fixture files, procedure 242 lines, log 555 lines |
| Items checked | R1 to R5, A1 to A6, B1 to B3, C1 to C5, D1 to D3, E1 to E2, F1 to F5, G2-1 to G2-3, H1 to H3 (33), plus 4 code items |
| Items answered No | 6 (TV-B3, TV-C2, TV-C3, TV-C5, TV-E1, TV-G2-1); R3 No (not attributable) |
| Items N/A | G1, G3, G4 sections; TV-F5; TV-H2 |
| Findings by severity | Major 2, Minor 5 |
| Findings fixed, deferred | 0, 0 |
| Iteration | 1 |
| Effort | 40 turns, 55 minutes |

## Tool runs (2026-09-27, HEAD `bfed1b0`)

| Command | Exit | Result |
|---|---|---|
| `sh rust-tv-2026-09-27.sh <scratch>/rr1 <scratch>/guard d3de579` | 0 | table "Reviewer re-run" |
| `cargo +1.98.0 llvm-cov --locked --features seeded-gap --lcov` in the export's `cov-kat`; `measurements.py --coverage` | 0, 0 | `DA:6,0`, `LH:5`, `lines 5/6 = 83.33 %` |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 453 tests, 1 failure (`test_repository_exit_zero`, the SRR drift failures of R3) |
| `.venv/bin/python tools/validate_docs.py` (before this record) | 1 | 52 passed, 2 failed (SRR drift, R3) |

No visual product was produced or changed by this review (charter section 11 rule 3).

## Cross items (outside this record's scope; for the lead SE)

- **X-1.** The `checklist` field names `peer-review-checklist-code` because the TV template is only on the CR-012 branch; after CR-012 merges, the delta iteration switches the field to `peer-review-checklist-tool-validation` revision A.
- **X-2.** PDR work plan WP-PDR-08 names "independent reviewer plus SA", while the TV template (CR-012) says `assurance_required: false` for TV records and puts the SWEHB tasks in section H. One of the two needs to change; until then the separate SA invocation is requested.
- **X-3.** `validate_docs.py` exits 1 on HEAD because of two SRR records whose product blobs moved (INSP-015 lock and README; the risk register record). Their delta re-issues are due under the record drift rule.
- **X-4.** TV-020 Annex A "07 stale" and "07 lacks" rows (Miri and llvm-tools installed; no X9 row; the G5 Miri scope) are 07 changes for the 07 writer order of plan section 5.3 (WP-PDR-17, then 13, then 47).
- **X-5.** TV-020 limitation 6: 07 section 17.3 names an "accreditation ADR" for the Ferrocene option that no WP produces.

## Verdict

```
VERDICT: NEEDS CHANGES
PRODUCT: TV-020, TV-021, TV-022, TV-023 at 71bf509c948fbc8d4ae9b863f2a0226f0bf1bba0 (runs at d3de579)
FINDINGS:
- [Major] TV-B3/TV-C5 TV-020 purpose 4 and K20-4: cross-layout loadable identity is refuted; reviewer re-run 7c20cba4 against reference c6d27ba1.
- [Major] TV-C2 TV-021 purpose 3: the lcov export has no seeded fault.
- [Minor] TV-A1/TV-E2 rust-objcopy not identified.
- [Minor] TV-C3 provenance of expected answers not stated.
- [Minor] TV-G2-1 gate target clippy and --locked differ from the validated commands.
- [Minor] procedure reads a possibly stale JUnit file.
- [Minor] Annex A omits CS-26 rustfmt.
ITEMS N/A: G1, G3, G4, TV-F5, TV-H2
RE-RUN: sh rust-tv-2026-09-27.sh <scratch>/rr1 <scratch>/guard d3de579; exit 0; 22 checks; all same as runs 1 and 2 except K20-4
MEASUREMENTS: size=4 records, 13 purposes; turns=40; minutes=55; major=2; minor=5
```
