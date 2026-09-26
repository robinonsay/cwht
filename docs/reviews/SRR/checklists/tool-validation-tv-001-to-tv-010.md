---
id: INSP-015
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md
product: docs/cm/tool-validation/ (TV-001 to TV-010, README.md, evidence/), tools/toolchain.lock.md, tools/traceability.py, tools/render_review_figures.py, tools/tests/
# product_commit: the review baseline of iteration 3 (HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1, 2026-09-26).
# product_files: the committed blobs reviewed at iteration 3, each equal to git rev-parse HEAD:<path> at that commit
# (record drift rule, TV-003 purpose 6). product_files_iteration_1 and product_files_iteration_2 keep the working-tree
# blobs of iterations 1 and 2 (reviewed at HEAD 28e49e6 while the files were untracked or modified; finding-2).
product_commit: "adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1"
product_files: ["docs/cm/tool-validation/README.md@b8e63c4ef5c0baff324e2fc032dddcb7b1111228", "docs/cm/tool-validation/TV-001-python-jsonschema.md@037888d6aec24ff35193d53d6d9aa5930cf3240c", "docs/cm/tool-validation/TV-002-traceability.md@c95e3488e854adb5c9176bfa956bbc9d0e231ccd", "docs/cm/tool-validation/TV-003-validate-docs.md@ede04566cce5bebda43a2562f4c7752f2907d552", "docs/cm/tool-validation/TV-004-render-rmm.md@901540e3f17c2519413009883bf796e76ca59754", "docs/cm/tool-validation/TV-005-render-compliance.md@da891666f51fd71d3549b61dac4930c48fbf0874", "docs/cm/tool-validation/TV-006-render-risk.md@b39ddbf1b96d7a650e68629ee68fbf9237b720b4", "docs/cm/tool-validation/TV-007-review-trend.md@39d2e80029cfe8693c3a6af97c22fc6da278e496", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@b4124dd555c23176a2ede67ac836543741c00491", "docs/cm/tool-validation/TV-009-git.md@1d89fd2723ae135c1a2c3c64a44478b30b8e49e8", "docs/cm/tool-validation/TV-010-render-review-figures.md@d6999b28f9484dffefdcbb89767478cb305501fb", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5.py@3be96e440e9d84cbe5771231f9a6c659828304ba", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-head.log.txt@57005ef0fb6aaa413546f874ae123937255987ff", "docs/cm/tool-validation/evidence/python-tools-2026-09-26-r5-worktree.log.txt@09b923952b2a00b861c2fff88b20d0d85cc7fb70", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.sh@7edd2c8fbfd0aaf0ad01c4157eab72a153486c73", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26-r5.log.txt@b4a4629ba12262671c4e971c8610529b3ea85ac4", "tools/toolchain.lock.md@2687fb04594ed4489ac43bdb4522f59faab6db51", "tools/traceability.py@0a867523f78c224afdaa938735911b5df8f2920c", "tools/validate_docs.py@33ab5a83fc2063071e1afece416b180518d9da12", "tools/render_review_figures.py@6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "tools/tests/test_render_review_figures.py@cb54d28b00b8c854056b341ece157c00778476cb", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@ed003bad762332310f0bc4d63346ac875f0e0554", "tools/tests/test_traceability.py@d76b06976ba62d374d8c30a8eb08a4cb57d394e7", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@4fb5bcc756b910876340e2f254359d3d9fcf80ef", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c"]
product_files_iteration_1: ["docs/cm/tool-validation/README.md@11001b41386ff134f892b4f7b7595e657d3a8971", "docs/cm/tool-validation/TV-001-python-jsonschema.md@ee60bb9398945d240ec62bebea3a4f1e922ec27b", "docs/cm/tool-validation/TV-002-traceability.md@f53fa153199de5e3e599b3a9b96fe47cabbfc095", "docs/cm/tool-validation/TV-003-validate-docs.md@e787b4b19a90f82bdbe2f15e62dae673807d138a", "docs/cm/tool-validation/TV-004-render-rmm.md@7693fd7c81d43ffbd910e2a536084a3bea6cb2ff", "docs/cm/tool-validation/TV-005-render-compliance.md@2d340044f039fb71b5ba4cca3e0821bd1a611edb", "docs/cm/tool-validation/TV-006-render-risk.md@0f065de27cc1578f06c90bc6c44ddc682984a081", "docs/cm/tool-validation/TV-007-review-trend.md@a716f8da3a68190179feb8229c0f513fefb98482", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@df046f215ee0c824f8788308f1c8810157cfb27f", "docs/cm/tool-validation/TV-009-git.md@8089ba35cc371204cb8d43e550ed8bb507186e2c", "docs/cm/tool-validation/TV-010-render-review-figures.md@7273106b5f7838fce6cc1149372d2a54edb05517", "tools/toolchain.lock.md@8b2324584c79bf70be10f2ea8cd3639828072507", "tools/traceability.py@0a867523f78c224afdaa938735911b5df8f2920c", "tools/render_review_figures.py@979beb139d13df8a64e295b2c6aac0d71a83c0e0", "tools/tests/test_git_known_answer.py@cd8389823bdc34889edc7fc680f1bd8ae4c928a9", "tools/tests/test_render_compliance.py@c40a7f1f514d3784efcbef300d301391d9de84c0", "tools/tests/test_render_deck.py@539e9593f8115045f85407cae95536632a53af52", "tools/tests/test_render_review_figures.py@ff5d81facd2d95718be681270238c6c980f2494c", "tools/tests/test_render_risk.py@05d695a4dd8c7d0510fd9a2c078584d6e3316b21", "tools/tests/test_render_rmm.py@0454936bf20498078de9ae2861af727c3a66350e", "tools/tests/test_review_trend.py@1f3ab0067b9ce33ebedefaf2a460664d2a978bdb", "tools/tests/test_tools.py@af6ed8b7d3b34338d52fef0eba76bc84d27cadb1", "tools/tests/test_traceability.py@d76b06976ba62d374d8c30a8eb08a4cb57d394e7", "tools/tests/test_traceability_srr_rules.py@86606485debd4569954847c5a48e7dd62bbcbcab", "tools/tests/test_validate_docs.py@3b10718d465cf3f796a9e5bcdc55c989c97517c4"]
product_files_iteration_2: ["docs/cm/tool-validation/README.md@5d69da3aecd684d4be9424810f2df5a19a90b68a", "docs/cm/tool-validation/TV-001-python-jsonschema.md@646e2cac45dfa7fd4bbb24794611b9eee4fa738f", "docs/cm/tool-validation/TV-002-traceability.md@ac9e27a62c134b6d46d4d31ae600b86f7a576dc6", "docs/cm/tool-validation/TV-003-validate-docs.md@e9575b7e7a9a09140bade49682945c95f456dac3", "docs/cm/tool-validation/TV-008-render-deck-chromium.md@1aa3099c1df6898077cf7b2e5ad4057ce31d710d", "docs/cm/tool-validation/TV-010-render-review-figures.md@8a7e322be16359767cc85fd6abfccf368863990c", "tools/toolchain.lock.md@f5f810a286a7e1e79d2e58f7409d383386d76e35", "tools/tests/fixtures/schema/keywords.schema.json@42c0822f6c98928ec2b33c14a7f991b6897dfc95", "tools/tests/fixtures/schema/keywords-invalid.json@272b585e327161ad7988896b54871d1e3093460d", "tools/tests/fixtures/schema/known-answers.json@86051ad7ba51c46cb8765b1271ea5d5646d78d1c", "tools/tests/test_validate_docs.py@8944a389618686b58c557f60872238321c5a3106", "tools/tests/test_render_deck.py@ff58fb7b7f1017ab165ad532bac36898f4ed0835", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.sh@458621f37562114fa5f5c96dd3b7697280cd2c99", "docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.log.txt@4a8faec188f30aa1d0fe476796aab4ded2cf0d3b", "docs/cm/tool-validation/evidence/python-tools-2026-09-26.log.txt@9906d1c8840643cd2371f2e591229b6a4dfce52e"]
product_size: 10 TV records and index (953 lines), 32 evidence files, toolchain lock (273 lines), traceability.py (2786 lines; 239-line working-tree delta reviewed), render_review_figures.py (1176 lines), 11 test modules (3844 lines)
sprint: SRR-prep
author_agent: "author:tool-validation (Claude invocation 2026-09-25, SRR package section 2 item H12)"
reviewer_agent: "reviewer:tools"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 2
findings_minor: 5
findings_open: 0
findings_fixed: 6
findings_verified: 6
findings_lien: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: [swe-136 7.1 task 1]
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [TV-S9]
effort_turns: 94
effort_minutes: 130
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-015: tool validation records TV-001 to TV-010 and the toolchain proof

**Checklist:** `docs/templates/peer-review-checklist-code.md` revision B, applied to the Python tool source as `docs/process/03-software-classification-and-rmm.md` (tool rows, "Peer review") directs, plus the tool validation criteria of `docs/process/05-configuration-and-data-management.md` section 9.2 steps 1 to 4 and the SRR row of section 13, which this record lists as items TV-S1 to TV-S10. The code checklist is written for Rust firmware; its Rust-specific items are answered N/A with the reason. **Gate:** SRR (package section 2 item H12; entrance row 20 "Technology readiness and heritage assessment, including toolchain proof", 01 section 4.5 row 20, evidence "toolchain sanity-check results"). **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable, each with evidence.

**Iteration 3 (2026-09-26, review baseline HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`): verdict APPROVED (with liens).** F-02 (Major) is Closed: TV-001 to TV-010 section 3 was re-run on an export of commit `400e59d` (SRR package item R5), every identity of those runs equals the commit, the two tools changed afterwards (TV-003 blob `33ab5a83`, TV-010 blob `6f3018fd`) were committed in `3de1e2d` with their tests and fixture exactly as run, and the reviewer re-ran every record's section 3 on an export of HEAD with every identity equal to HEAD. One new Minor finding, F-07 (the records still call those two blobs uncommitted and name no commit for their runs), is dispositioned "Lien: fix before PDR" under the convergence rule of 2026-09-26 (charter section 4 item 3). No Major finding is open and none needs an owner ruling. Details: section "Iteration 3".

**Iteration 2 (2026-09-26): verdict NEEDS CHANGES.** The author reported F-01, F-03, F-04, F-05 and F-06 fixed and disputed none. The reviewer verified all five against the product (section "Iteration 2 re-review" and the Disposition column). F-02 (Major, commit binding) was not reported fixed and stays Open: `HEAD` is still `28e49e6`, and `docs/cm/`, `tools/render_review_figures.py` and `tools/tests/fixtures/schema/` are still untracked. The verdict can become APPROVED only when F-02 is closed.

**Iteration 1 verdict: NEEDS CHANGES.** Two Major findings: TV-001 claims keyword coverage that it does not have (finding-1), and no validation result is bound to a commit (finding-2). Four Minor findings. Everything else checked holds: every known-answer suite re-runs with the stated counts, every fixture tree digest and tool blob matches its record, and every inspected render agrees with the record.

**Search-first compliance:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and run before any repository search (queries: "tool validation and accreditation TV record criteria SWE-136 section 13"; "SRR package H12 toolchain proof sanity checks readiness shortfall"; "SWE-136 validate and accredit software tools"). One `grep -n '^## 13'` of `docs/process/01-lifecycle-and-reviews.md` ran before the tool was loaded. It pinned a section heading in a file already open at a known path. It is reported here so the order can be audited. All later `grep -n` calls only pinned lines that a search hit or a known file pointed at.

**Independence:** the reviewer did not author any product file and edited none. The known-answer suites were re-run read-only. `tools/traceability.py --report-only` rewrote `docs/vv/traceability-report.md` and `docs/vv/traceability.json`, as the assignment's command requires. `render_deck.py` was not re-run, because it rewrites `png/` in place. The TV-001 procedure was re-run on its own temporary copy.

**Criticality and assurance:** `criticality: neither`. 03 section 4.3.1 finds no tool safety-critical or mission-critical, and the 07 section 2.1.1 code row gives "No" for Neither when no file contains `unsafe` (Python has none), so `assurance_required: false`. The reviewer still applied the SWEHB `swe-136-software-tool-accreditation.md` section 7.1 task 1 ("Confirm that the software tool(s) needed to create and maintain software is validated and accredited") as the software assurance function of charter section 2. Result: every tool is Validated. None is yet Reviewed or Accredited, and two of those gaps are findings 1 and 2.

## Product files reviewed

Blob hashes are from `git hash-object` on 2026-09-26. The last column is the state against `HEAD` `28e49e6`, from `git status --short`.

| File | Blob | State | Findings |
|---|---|---|---|
| `docs/cm/tool-validation/README.md` | `11001b41` | untracked | finding-2, finding-3 |
| `docs/cm/tool-validation/TV-001-python-jsonschema.md` | `ee60bb93` | untracked | finding-1, finding-2 |
| `docs/cm/tool-validation/TV-002-traceability.md` | `f53fa153` | untracked | finding-2, finding-6 |
| `docs/cm/tool-validation/TV-003-validate-docs.md` | `e787b4b1` | untracked | finding-2, finding-5 |
| `docs/cm/tool-validation/TV-004-render-rmm.md` | `7693fd7c` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-005-render-compliance.md` | `2d340044` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-006-render-risk.md` | `0f065de2` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-007-review-trend.md` | `a716f8da` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-008-render-deck-chromium.md` | `df046f21` | untracked | finding-2, finding-5 |
| `docs/cm/tool-validation/TV-009-git.md` | `8089ba35` | untracked | finding-2 |
| `docs/cm/tool-validation/TV-010-render-review-figures.md` | `7273106b` | untracked | finding-2, finding-3, finding-4 |
| `docs/cm/tool-validation/evidence/` (32 files) | per file | untracked | finding-2 |
| `tools/toolchain.lock.md` | `8b232458` | modified | finding-3 |
| `tools/traceability.py` | `0a867523` | modified (235 added, 4 removed) | finding-2 |
| `tools/render_review_figures.py` | `979beb13` | untracked | finding-2, finding-4 |
| `tools/tests/` (11 modules, blobs in front matter; fixtures by tree digest below) | per file | mixed: `test_tools.py` and `test_traceability.py` modified; `test_git_known_answer.py`, `test_render_review_figures.py` and `test_traceability_srr_rules.py` untracked; the rest equal | finding-2 |

Tool blobs checked against their records: `traceability.py` `0a867523` (TV-002), `validate_docs.py` `2bedc2a7` (TV-003), `render_rmm.py` `2386a37f` (TV-004), `render_compliance.py` `d67d6b5e` (TV-005), `render_risk.py` `d38ba1dd` (TV-006), `review_trend.py` `04493157` (TV-007), `slides/render_deck.py` `b42425e9` (TV-008) and `render_review_figures.py` `979beb13` (TV-010). All eight equal their record. SHA-256 prefixes also match. Repository inputs named in TV-005, TV-006 and TV-007 also equal their records: `se-compliance-matrix.schema.json` `ef156b0f`, App. H corpus `8afa36e0`, `docs/risk/schema.json` `473cd797`, `rfa-rid-log.example.json` `0e913114`, `rfa-rid-log.schema.json` `38898b0c` and `docs/reviews/SRR/rfa-rid-log.json` `0dc293ad`.

Fixture tree digests were recomputed with the `tree` function of `evidence/python-tools-2026-09-25.py` (SHA-256 of the sorted `sha256  path` list). Each equals its record:

| Fixture | Files | Digest (prefix) | Record |
|---|---|---|---|
| `valid_project/` | 38 | `6a58c19d` | TV-002, TV-003 |
| `invalid_project/` | 32 | `2377caa9` | TV-002, TV-003 |
| `rmm/` | 17 | `fa7f91af` | TV-004 |
| `compliance/` | 15 | `a95aad46` | TV-005 |
| `risk/` | 5 | `3a594f97` | TV-006 |
| `review_trend/` | 6 | `c7d63b0f` | TV-007 |
| `slides/` | 1 | `f0519294` | TV-008 |
| `git/` | 2 | `bfc6387c` | TV-009 |
| `review_figures/` | 6 | `9cab14eb` | TV-010 |

## Commands run by the reviewer (2026-09-26, repository root, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` | 1 | 34 passed, 2 failed. The failures are `docs/design/allocation.json` and `docs/plan/measurements.json`, whose schemas `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` do not exist. Both are outside this product (cross item 1). This record passes after it was written (see Closure) |
| `tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 7 warnings (`HAZARD_INVERSE` x2, `SYS_UNALLOCATED` for REQ-SYS-125 and REQ-SYS-148, among others) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings; `register.md` current |
| `tools/render_rmm.py --check` | 0 | |
| `tools/render_compliance.py --check` | 0 | |
| `-m unittest discover -s tools/tests` | 1 | 331 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the same two missing schemas (repository content, cross item 1) |
| TV-002 section 3, three commands | 0 | 27 + 32 + 114 = 173 tests, OK |
| TV-003 section 3, two commands | 0 | 18 + 114 = 132 tests, OK |
| TV-004 `-p test_render_rmm.py` | 0 | 20 tests, OK |
| TV-005 `-p test_render_compliance.py -k CorpusParseTests -k ValidFixtureTests -k SeededFaultTests` | 0 | 26 tests, OK (whole module 27, OK) |
| TV-006 `-p test_render_risk.py` | 0 | 27 tests, OK; `faults.json` holds the 23 named faults |
| TV-007 `-p test_review_trend.py` | 0 | 20 tests, OK |
| TV-008 `-p test_render_deck.py` | 0 | 3 tests, OK, none skipped; Chromium `--version` `Google Chrome for Testing 148.0.7778.96`, binary SHA-256 `aa25f2e7...d2dd7b` equal to TV-008 |
| TV-009 `-p test_git_known_answer.py` | 0 | 6 tests, OK; `git --version` 2.50.1 (Apple Git-155), `xcrun --find git` equal to TV-009 |
| TV-010 `-p test_render_review_figures.py -k ParserTests -k DataKnownAnswerTests -k RunTests` | 0 | 32 tests, OK |
| TV-001 procedure `evidence/python-jsonschema-2026-09-25.sh` | 0 | both cases MATCH, PASS; the negative control fails as required (exit 1) |
| `tools/render_review_figures.py --review SRR --check` | 1 | "package group 'Keying and keyer' ... differs": the package says 11 TBR, `requirements.json` gives 16. This is the tool's specified behavior (TV-010 purpose 2) acting on repository content (cross item 2) |

**Independent known answers computed by the reviewer (not by the tool under test):**

- TV-009: blob `d184c928...`, tree `bf3b5c84...` and commit `779d21e2...` for the fixed identity and date 1790294400 +0000 were computed in Python from the git object formats. All three equal `known-answers.json`. The record says only the blob was cross-checked; the reviewer's computation now covers the tree and the commit.
- LTspice: 1/(2 pi x 1 kOhm x 159.155 nF) = 999.99964 Hz, equal to the stored 999.9996 Hz. The transcript measurement is 999.999642 Hz.
- OpenSCAD and FreeCAD: 30 x 20 x 10 - pi x 3^2 x 10 = 5717.257 mm^3, equal to the transcript.

**Renders opened with the Read tool (visual closure, charter section 11 rule 3):** `evidence/render-deck-fixture-slide-01.png` to `-04.png`. They show the title and author, the agenda items 1 and 2, the 3-column table with one row, and the alpha and beta bullets with no note text, all at 1280 x 720, matching the TV-008 inspection row. Also opened: the nine `evidence/render-review-figures-fixture-*.png`. They show entrance 1/2/1 with the dagger; success 2/0/1 with both footers; groups Transmitter 3 and Receiver 2 with 1 TBR; KDRs REQ-SYS-001 and -004; HZ-001 B to D Catastrophic and HZ-002 C to E Marginal; risk RSK-001 at R16, RSK-002 at Y10 with the safety override, RSK-003 at G2; the TPM board Red/Yellow/Not reported; ConOps OPS-001 and OPS-002; and the concept diagram, which is legible. These match the TV-010 inspection row. Also opened: `evidence/kicad-fixture-clean-top.png` and `kicad-fixture-seeded-top.png`, where the seeded trace runs close to TP1 against the clean route, and `evidence/openscad-fixture-cube.png` (block with a through hole).

## Readiness criteria

The R1 to R6 criteria of the code checklist are written for Rust crates. For the Python tools they are read as follows.

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Gate G1 (`cargo fmt`, `clippy`) | N/A | Python tools; no linter is locked for `tools/` (lock section 2 has none) |
| R2 | File at most 500 lines, functions at most 60 lines (CS-18) | N/A | CS-18 is a firmware rule (07 section 7). Measured for the record: `traceability.py` 2786 lines, `render_review_figures.py` 1176 lines (`wc -l`) |
| R3 | Design unit Active | N/A | Tools have no design unit. Their specification is `tools/README.md` together with 05 section 9.2 |
| R4 | `@req` tags | N/A | Rust tag convention |
| R5 | Test file exists | Yes | Every tool has a known-answer module (list above); all pass |
| R6 | `unsafe_audit.py` | N/A | No `unsafe` in Python |
| R-TV | Adapted readiness: every TV record exists, and its section 3 command runs | Yes | Ten records; every command re-run above exits 0 |

`readiness_met: true` on R5 and R-TV.

## Tool validation criteria (05 section 9.2 steps 1 to 4; 05 section 13 SRR row)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| TV-S1 | Step 1 identification: exact version, command, install source with installer URL and SHA-256, SHA-256 or blob of every file validated, "commit SHA tested" | No | Versions, commands and blobs are present and verified above. Installer URLs are absent where upstream publishes none, and each record says so and names its substitute (TV-001 section 1; TV-008 section 1; TV-009 section 1): acceptable. Fails because no record can name a commit containing the files it tested: finding-2 |
| TV-S2 | Step 1 class and purposes, one line each | Yes | Each record, section 2. All are class B, as 05 section 9.1 lists them |
| TV-S3 | Step 1 known-answer test with fixture path under `tools/tests/fixtures/<tool>/`, run command and pass criteria with seeded faults (class B: "Known-answer test with a seeded fault", 05 section 9.1) | Yes, with gaps | Each record, section 3. Seeded faults exist for every tool: `invalid_project` (TV-002, TV-003); 10 RMM faults; 11 compliance faults whose strings were checked in `test_render_compliance.py`; 23 risk faults; zone and CLI cases; the location guard; the git fsck corruption; figure disagreements; 4 plus 18 schema faults with a negative control. Gaps: finding-5 (two accredited exit-code purposes have no known answer) |
| TV-S4 | Step 1 accredited purposes are all exercised by the known-answer test | No | finding-1 (TV-001 keyword `minProperties`); finding-5 (TV-003 purpose 5 exit 2; TV-008 purpose 4 exit 1) |
| TV-S5 | Step 1 result: date, test count, output excerpt, evidence file | Yes | Each record, section 4, cites `evidence/python-tools-2026-09-25.log.txt` or `python-jsonschema-2026-09-25.log.txt`. The counts reproduce (commands table) |
| TV-S6 | Step 1 reproducibility (class A only) | N/A | All ten are class B. Each still records two identical runs |
| TV-S7 | Step 1 limitations and step 4 re-validation triggers present and correct | Yes, with an error | Present in every record (sections 6 and 7). TV-010 limitation 3 misdescribes the tool: finding-4 |
| TV-S8 | Step 3 reviewer checks the TV record and the fixture: the fixture's expected answers are independent of the tool | Yes | Expected values were hand-written for TV-001 (`known-answers.json` pairs), TV-004 to TV-007 (stored strings and 01 section 11 counts), TV-009 (reviewer's independent computation above) and TV-010 (fixture counts checked against the renders). Revisions after a failed run are documented in the transcripts (kicad STEP z, LTspice precondition); both are PDR-due tools |
| TV-S9 | 05 section 13 SRR row: TV records exist for the ten named tools, each reviewed and accredited | No | Ten records exist and match the ten tools of 05 section 13 line 583. Review: this record, NEEDS CHANGES. Accreditation: pending in all ten sections 9. Stale statements that the plan does not list TV-010: finding-3 |
| TV-S10 | Lock section 1.1 records each SRR sanity check with date, the commit tested and the test count (step 2), and section 5 agrees with the records | Yes, with gaps | Lock lines 60 to 87 record the runs of 2026-09-25 23:06 to 23:47 with evidence names. Section 5 lists TV-001 to TV-010 as Validated, equal to the README index. Gaps: finding-2 (commit) and finding-3 (stale note) |

## SRR row 20 toolchain proof: lock section 1.1 sanity checks

This table covers the H12 list only: kicad-cli, LTspice, rustc and cargo, clippy, picotool, OpenSCAD with FreeCAD, and the venv Python with jsonschema. Each check was read against its transcript and `known-answers.json`.

| Lock row | Transcript result | Reviewer check | Answer |
|---|---|---|---|
| kicad-cli (lock line 60) | run 2 pass: ERC clean 0, seeded `pin_not_connected` R1 pin 2 (exit 5); DRC one `clearance`; drill 1 PTH 0.70 mm and 1 NPTH 3.20 mm; CPL and BOM equal; STEP box to z 1.51 mm; normalized hashes blocked | Renders opened. The 1.51 mm correction equals the 1.6 mm board minus two 35 um copper and two 10 um mask layers. It was revised after run 1 and documented (lock section 1.4 finding 5) | Yes (partial: normalized exports blocked until `tools/normalize_fab.py`; TV due PDR) |
| LTspice (line 63) | runs 3 and 4 pass | Analytic value recomputed; seeded netlist exit 1; hang guard counted as failure | Yes |
| rustc / cargo (line 64) | both runs pass; ELF `3201d382...df7d` identical over 3 builds | `known-answers.json` records that the ELF hash came from run 1 (regression value); the 05 section 9.2 criterion is equality across builds, which holds | Yes |
| clippy (line 65) | `absurd_extreme_comparisons` and `unwrap_used` seeded, exit 101 | The seeded `unwrap_used` shows that the project lint table is in force | Yes |
| picotool (line 74) | `uf2 convert` and `info` pass; `verify` blocked (needs a device) | Documented blocked item; TV due CDR | Yes (partial) |
| OpenSCAD + FreeCAD (line 86) | run 2 pass with a one-line listing adaptation; `tools/scad2step.py` absent | Volume recomputed; render opened | Yes (partial: script absent; TV due PDR) |
| python + jsonschema (line 78) | 4 runs pass | Re-run by the reviewer: PASS; negative control exit 1 | Yes (see finding-1 for scope) |

Row 20 status from this product alone: the lock's sanity-check results now exist for every tool H12 names. The blocked parts carry a named reason and gate. The FW-B0 part of row 20 is reviewed in `checklists/fw-b0-toolchain-proof.md`, not here.

## A. Environment, dependencies and build (CS-01 to CS-04)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | N/A | `no_std` rule for image crates; the tools are host Python |
| CK-CODE-A2 | Yes | `render_review_figures.py` adds matplotlib, which is locked (lock section 2: 3.11.2, class B) and named in TV-010 section 1. `tools/requirements.txt` still lists it unpinned (AL-4; cross item 3) |
| CK-CODE-A3 | N/A | Rust `cfg` rule |

## B. Unsafe code (CS-05 to CS-10)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-B1 to B8 | N/A | No `unsafe` in Python; no MMIO |

## C. Panics, errors and arithmetic (CS-11 to CS-16)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-C1 | Yes (adapted) | `load_allocation` (traceability.py, working-tree delta) returns early on an absent file, stores a parse error in `allocation_error` instead of raising, and type-checks every node (`isinstance`). `check_stakeholders` skips non-dict entries. The repository run completes with exit 0 and no traceback |
| CK-CODE-C2 | Yes (adapted) | Failures become catalogue findings (`STAKEHOLDERS_MISSING`, `SYS_UNALLOCATED`) or exit codes, never silent. `render_review_figures.py --check` exits 1 with a named disagreement (commands table) |
| CK-CODE-C3 to C7 | N/A | Rust error and arithmetic rules |

## D. Structure, complexity and target platform rules

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-D1 | N/A | SWE-220 applies to firmware components (07 section 14.1); no complexity tool is locked for Python |
| CK-CODE-D2 | Yes | `load_allocation.visit` recurses over the parsed JSON tree, whose depth is bounded by the file. No other recursion appears in the delta |
| CK-CODE-D3 to D9 | N/A | Rust and target rules |

## E. Correctness against design and requirements

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-E1 | No | The specification of the tools is the TV purposes plus `tools/README.md`. TV-010 limitation 3 states behavior the code does not have (finding-4). `traceability.py` T-18 and T-21 match 02 sections 2.3 and 3.0 as cited in the docstrings, and the known answers in `test_traceability_srr_rules.py` pass (32 tests) |
| CK-CODE-E2 | N/A | Firmware timing constants |
| CK-CODE-E3 to E8 | N/A | Keyer, register and safe-state rules |
| CK-CODE-E9 | Yes | The two figure functions outside the SRR set (`risk`, `concept`) are kept deliberately, with known-answer tests and a comment (render_review_figures.py lines 953 to 957). The catalogue guard test `CatalogueTests` fails on any code without a known answer |

## F. Traceability tags

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-F1 to F3 | N/A | `@design` and `@req` are Rust conventions. The Python tools cite their process sections in their docstrings instead (for example `check_allocation`: "02 T-18 at SRR") |

## G. Secure coding

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-G1 | Yes | The inputs are repository files. JSON goes through `validate_docs.load_json` with the error captured, and every field is type-checked before use |
| CK-CODE-G2 to G4 | N/A | Firmware input rules |
| CK-CODE-G5 | N/A | Gate G5 is a firmware gate |

## H. Tests and testability

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-H1 | Yes | Every tool takes `--root` or an explicit path, and the known answers run on fixtures in temporary copies (TV-002 to TV-010 section 3) |
| CK-CODE-H2 | N/A | 05 section 9.2 step 3 puts fixture independence under the reviewer's check (TV-S8) instead of a separate test author. The tests exist and pass |
| CK-CODE-H3 | N/A | MC/DC applies to safety-critical firmware |

## I. Documentation and style

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-I1 | Yes | Every new function in the delta has a docstring citing its rule (`load_allocation`, `check_stakeholders`, `check_allocation`, `is_l2_module`, `child_modules`, `allocated_modules`, `receiving_modules`). Exception: `allocation_state` has none (trivial) |
| CK-CODE-I2 | Yes | Names are descriptive |
| CK-CODE-I3 | N/A | `cargo fmt`. Observed: three blank lines before `verification_row` in traceability.py (cosmetic; no finding) |
| CK-CODE-I4 | Yes | No commented-out code in the delta |

## J. Common review traps

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-J1 | Yes | Every API used resolves: the suites run with 0 errors |
| CK-CODE-J2 | Yes | `validate_docs.load_json` is called as defined |
| CK-CODE-J3 | Yes | T-18 treats "child_ids or allocation.json" as one union (`receiving_modules`), as 02 section 2.3 states |
| CK-CODE-J4 | Yes | Lines measured with `wc -l` (product_size) |

## Iteration 2 re-review (2026-09-26)

Same reviewer role, new invocation. The author reported `{"fixed":["F-01","F-03","F-04","F-05","F-06"],"disputed":[]}`. Search-first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried ("minProperties seeded fault keywords schema TV-001") before any `grep`; later `grep -n` calls only pinned lines in files at known paths. The reviewer edited no product file. The TV-001 procedure ran with `TMPDIR` set to the reviewer's scratch directory, so its temporary copies did not touch the fixture.

| Command | Exit | Result |
|---|---|---|
| `bash docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.sh` | 0 | case `requirement` 0 and 4 errors MATCH; case `keywords` 0 and 19 errors MATCH (including `entries/16/margins` `minProperties`); PASS; negative control exit 1; survey 9 schemas, 23 keywords, none missing, exit 0; survey negative control names `minProperties`, exit 1 |
| `-m unittest discover -s tools/tests -p test_render_deck.py -v` | 0 | 5 tests OK, none skipped (`SeededFailures` 2 new) |
| `-m unittest discover -s tools/tests -p test_validate_docs.py -k UsageErrorTests -v` | 0 | 2 tests OK |
| `git diff --numstat 28e49e6 -- tools/traceability.py` | 0 | 235 added, 4 removed |
| `git hash-object` on `render_review_figures.py`, `traceability.py`, `validate_docs.py`, `slides/render_deck.py` | 0 | `979beb13`, `0a867523`, `2bedc2a7`, `b42425e9`: every tool is unchanged since iteration 1, so the fixes touched records, tests and fixtures only |
| `git log -1`; `git status --short` on the product | 0 | `28e49e6`; `docs/cm/`, `render_review_figures.py`, `fixtures/schema/` untracked, `traceability.py` modified (F-02 stays Open) |

Checklist answers changed by iteration 2: TV-S4 is now Yes (F-01 and F-05 closed: every accredited purpose, including the `minProperties` keyword and the two exit-code purposes, has a known answer). CK-CODE-E1 is now Yes (F-04 closed: TV-010 limitation 3 matches the code). TV-S3 and TV-S7 lose their gaps. TV-S1, TV-S9 and TV-S10 remain No or gapped on F-02 alone. The iteration 1 tables above are kept as written.

## Iteration 3 (2026-09-26)

**Scope and independence.** New invocation of the reviewer role (`reviewer:tools`); it authored no product file and edited none. Review baseline: HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; every product file is identified by its committed blob in `product_files` (`git rev-parse HEAD:<path>`). The tool paths of the product are clean against HEAD (`git status --short` lists only other review records). Search-first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was loaded and queried ("tool validation commit tested TV record result row HEAD committed INSP-015 F-02") before any manual search; `grep -n` and `git grep -n` afterwards only pinned lines in files at known paths. The known-answer procedures ran on an export of HEAD (`git archive HEAD`) in the reviewer's scratch directory, with `TMPDIR` there, so nothing in the repository was written. Convergence rule (lead SE direction 2026-09-26, applying charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR".

**Commands run by the reviewer (repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `git log --oneline`; `git rev-parse <commit>:<tool>` for the eight Python tools at `1d423e5`, `400e59d`, `3de1e2d` and HEAD | 0 | `400e59d` is an ancestor of HEAD. `traceability.py` `0a867523`, `render_rmm.py` `2386a37f`, `render_compliance.py` `d67d6b5e`, `render_risk.py` `d38ba1dd`, `review_trend.py` `04493157`, `slides/render_deck.py` `b42425e9` are equal at all four. `validate_docs.py` is `2bedc2a7` at `1d423e5` and `400e59d`, `33ab5a83` at `3de1e2d` and HEAD; `render_review_figures.py` is `979beb13`, then `6f3018fd` from `3de1e2d` |
| `evidence/python-tools-2026-09-26-r5.py <export of HEAD> worktree` | 0 | TV-002 176, TV-003 142, TV-004 20, TV-005 26, TV-006 27, TV-007 20, TV-008 5, TV-009 6, TV-010 42 tests, each PASS; all 49 identity lines "equal to HEAD". Apart from paths, run times and the repository-content check, the output equals the author's `python-tools-2026-09-26-r5-worktree.log.txt`: the same results for every tool and the same identities. The repository-content check now passes (the author's run failed it on INSP-005 and INSP-013, since fixed by R13) |
| `evidence/python-jsonschema-2026-09-26-r5.sh <export of HEAD>` | 0 | case `requirement` 0 and 4 errors MATCH; case `keywords` 0 and 19 errors MATCH (including `entries/16/margins` `minProperties`); PASS; negative control exit 1; survey of 11 schemas and 23 keywords, none missing, PASS; the survey negative control names `minProperties` |
| Fixture tree digest of `tools/tests/fixtures/review_figures/` at HEAD (the `tree` function of the procedure) | 0 | `1a2dae0b...b07c`, equal to TV-010 run 4 |
| `tools/validate_docs.py` | 0 | 37 passed, 0 failed; this record PASSES as APPROVED under the record drift rule (every `product_files` blob equals HEAD) |
| `tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148); the rewritten report equals the committed one (`git status` clean) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings; `register.md` current |
| `tools/render_rmm.py --check`; `tools/render_compliance.py --check` | 0; 0 | both current |
| `tools/render_review_figures.py --review SRR --check` | 0 | check passed for 7 figures, nothing written (cross item 2 is resolved) |
| `-m unittest discover -s tools/tests` | 0 | 392 tests, OK |

**Renders opened with the Read tool (visual closure, charter section 11 rule 3), the five of TV-010 inspection 2:** `render-review-figures-fixture-2026-09-26-entrance-checklist.png` (Not met 1: S1; Partially met 2: rows 1 and 2; Met 1: S4 with the dagger and the note "dagger: fixture note"), `...-success-criteria.png` (2, 0, 1 with both footer lines), `...-kdr-map.png` (REQ-SYS-001 tagged "Test TBR PDR", REQ-SYS-004 "Inspection", footer "2 KDRs, 1 with an open TBR"), `render-review-figures-layout-19-rows-entrance.png` (lanes of 5, 19 and 15 rows; P18 ends inside its lane; the three-line footnotes of the first and last lanes clear the rows) and `...-layout-19-rows-success.png` (11 two-line and 19 one-line rows, the last row P18 inside its box, the footer below the boxes). Each matches the TV-010 "Inspection 2" row. The entrance layout arithmetic in the test docstring (`test_render_review_figures.py` lines 293 and 294: (834 - 78) / 19 = 39.789 px, 20 x 39.789 / 43 = 18.51 pt) was re-computed and holds.

**Changed text checked for new Major defects** (diff `1d423e5..HEAD` of the TV records, the README and the lock). TV-003 purpose 6 was compared with `tools/validate_docs.py` lines 760 to 838: the `path@blob` pattern, `git ls-tree -r --full-tree HEAD`, the prefix match, the failure for an APPROVED record that names no blob, the `note:` line for other verdicts, and the "not applied" note outside a work-tree top all match. The TV-010 purpose 2 and 3 additions agree with `LabelAndDaggerTests` and `LayoutKnownAnswerTests` and with the renders above. The ten "R5 re-run" paragraphs and the section 4 rows at `400e59d` agree with the committed transcripts: every identity line reads "equal to HEAD", and the counts are TV-002 176, TV-003 137, TV-010 32, and TV-001 7 and 8 PASS. Lock line 59 and README action 3 describe the R5 runs correctly. No new Major defect. The residual status text on the two tools changed after `400e59d` is the new Minor F-07.

**Disposition table.**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD |
|---|---|---|---|
| F-01 | Major | Closed | Verified at iteration 2. At HEAD the fixture files are unchanged (`keywords.schema.json` `42c0822f`, `keywords-invalid.json` `272b585e`, `known-answers.json` `86051ad7`, equal to the iteration 2 blobs), and the reviewer re-ran the procedure on the export of HEAD: PASS, and the survey of 11 schemas finds no keyword missing (`TV-001-python-jsonschema.md` section 4 rows 7 and 8) |
| F-02 | Major | Closed | TV-001 to TV-010 section 4 each carry a row "`HEAD` `400e59d` ... an export of the commit" (for example TV-002 line 56, TV-003 line 58, TV-010 line 51), backed by `evidence/python-tools-2026-09-26-r5-head.log.txt` and `python-jsonschema-2026-09-26-r5.log.txt`, whose identity lines all read "equal to HEAD" at `400e59d`. `docs/cm/`, the tools, tests and fixtures are committed; lock line 59 names the commit; README line 49 withdraws owner action 3 for this finding. The later blobs `33ab5a83` and `6f3018fd` and their tests and fixture are committed in `3de1e2d` exactly as run 5 and run 4 identified them, and the reviewer's run on HEAD reproduces them. The remaining record wording is F-07 |
| F-03 | Minor | Closed | Verified at iteration 2; `TV-010-render-review-figures.md` line 9 and README line 34 still give Due SRR with no stale note |
| F-04 | Minor | Closed | Verified at iteration 2; `render_review_figures.py` changed (`6f3018fd`), so the reviewer checked limitation 3 again: `TV-010-render-review-figures.md` line 67 states `max(29, largest group count + 3)` and `max(20, largest open-TBR count + 3)`, as `tools/render_review_figures.py` lines 723 and 724 at HEAD read (`git grep -n set_xlim`) |
| F-05 | Minor | Closed | Verified at iteration 2; `UsageErrorTests` and `SeededFailures` are committed (`test_validate_docs.py` `4fb5bcc7`, `test_render_deck.py` `ff58fb7b`) and pass in the reviewer's run on HEAD (TV-003 142, TV-008 5, none skipped) |
| F-06 | Minor | Closed | Verified at iteration 2; `TV-002-traceability.md` line 19 still reads 235 added and 4 removed against `28e49e6` |
| F-07 (new) | Minor | Lien: fix before PDR | See the findings table: TV-003 and TV-010 status lines (line 6 of each) and README line 49 still call the committed blobs uncommitted; no result row names `3de1e2d` or later |

Note on F-04: the line numbers moved with the blob. The reviewer pinned them at HEAD with `git grep -n`.

**Lien table.**

| Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|
| F-07 | Minor | Lien: fix before PDR | Tool validation author (Claude) | PDR readiness declaration | Routine item (package section 20.1, convergence rule) |

**Checklist answers changed by iteration 3.** TV-S1 is now Yes: every record names a commit holding what it tested, `400e59d` for the R5 rows, and the two later blobs are committed unchanged (F-07 is a naming lien). TV-S10 is Yes, with the F-07 lien on lock rows 106 and 112. TV-S9 stays No for one reason only: section 9 of each record still waits for the owner's accreditation (decision 114; owner action OA-7). That is the owner's step 3 decision, which follows this review. It is not a product defect and not a finding. The iteration 1 and 2 tables above are kept as written.

**Cross-document items at HEAD.** Item 1 is resolved: both schemas exist and `validate_docs.py` exits 0. Item 2 is resolved: `render_review_figures.py --check` exits 0. Item 3 is still open as package section 15 item 55 (CM author). Item 4 is still open as package item 38 (H10). Item 5 is still an owner process item.

**Counts.** 7 findings: 2 Major (both Closed), 5 Minor (4 Closed, 1 Lien). Disputed-accepted 0. Open Major 0. No finding needs an owner ruling.

VERDICT (iteration 3, independent reviewer): APPROVED (with liens)

FINDINGS: F-01 to F-06 Closed; F-07 Minor (new) Lien: fix before PDR

MEASUREMENTS: findings re-checked 6 plus the changed passages of 13 files; closed 6; lien 1; open Major 0; iteration 3; turns 32; minutes 45

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition (iteration 2, 2026-09-26) |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>F-01 (finding-1) | reviewer | Major | TV-S4 | `docs/cm/tool-validation/TV-001-python-jsonschema.md` line 30 (section 2); `tools/tests/fixtures/schema/keywords.schema.json` | TV-001 line 30 says every keyword that the nine repository schemas use is in the purpose 2 list. This is false. `docs/plan/tpm.schema.json` line 168 uses `minProperties`, and the file was committed in `4e3f891`, before the survey. `minProperties` is not in the list and has no seeded fault. `docs/plan/tpm.json` is an SRR product that `validate_docs.py` validates with this schema. By TV-001 limitation 1 and TV-003 limitation 2 that keyword is outside the accreditation, yet the record's claim hides the gap. A second error on the same line: "`maxItems` ... no repository schema uses it yet" is also false, because `docs/process/rmm.schema.json` line 52 uses it. A reviewer survey of all nine schemas finds exactly one keyword outside the list, `minProperties`. The claim is wrong and it narrows an SRR evidence path, so it blocks accreditation. Fix: add a `minProperties` constraint to `keywords.schema.json` with one seeded fault in `keywords-invalid.json` and the stored pair in `known-answers.json`; re-run; add the keyword to purpose 2 and to ACC-PYJS-001; correct the `maxItems` note. Citation: charter section 11 rule 2; 05 section 9.2 step 1 | Verified | | Closed. TV-001 section 2 purpose 2 now lists `minProperties`, and the survey note says the 2026-09-25 survey missed `minProperties` and wrongly said no schema used `maxItems`. ACC-PYJS-001 (section 9) lists 23 keywords including `minProperties`. `keywords.schema.json` `definitions.entry.properties.margins` has `minProperties: 1`; `keywords-invalid.json` `entries[16].margins` is `{}`; `known-answers.json` stores `["entries/16/margins", "minProperties"]` (19 pairs); `keywords-valid.json` exercises the passing case. The reviewer re-ran `evidence/python-jsonschema-2026-09-26.sh`: both cases MATCH, PASS, exit 0; negative control exit 1; the new keyword survey finds 9 schemas and 23 keywords, none missing, exit 0, and its negative control fails naming `minProperties`, exit 1. The survey result equals the reviewer's iteration-1 survey (exactly one keyword was missing), and the survey is now a standing step of the procedure and a re-validation trigger (section 7). Lock section 1.1 row `python (venv) + jsonschema` records runs 5 and 6 |
| <a id="finding-2"></a>F-02 (finding-2) | reviewer | Major | TV-S1, TV-S9, TV-S10 | TV-002, TV-009 and TV-010 section 1 and section 4 "Commit tested"; TV-003 section 1 (`test_tools.py`, `valid_project`); lock section 1.1 lines 60 to 87 ("fixture untracked"); all of `docs/cm/tool-validation/` | 05 section 9.2 step 1 requires the "commit SHA tested". 05 section 13 (SRR row) requires the TV records reviewed and accredited, with the tool files as configuration items (Table 4-1 row 28). 01 section 3.1 item 1 requires evidence rows to cite a commit. No result is tied to a commit containing what it tested. `tools/traceability.py` is modified. `tools/render_review_figures.py`, `test_git_known_answer.py`, `test_traceability_srr_rules.py`, `test_render_review_figures.py` and the fixtures `git/`, `schema/`, `review_figures/`, `kicad/`, `ltspice/`, `rust/`, `picotool/` and `openscad/` are untracked. `test_tools.py`, `test_traceability.py` and `valid_project/` are modified. The records and evidence themselves (`docs/cm/`) are untracked. The blob identities make the tested content exact, and README item 3 raises the question honestly. But a baseline cannot cite untracked records, and the owner cannot accredit "at version v" when no commit holds v. Fix: after owner authorization (package item H17), commit the tools, tests, fixtures, records and evidence. Re-run each record's section 3 on that commit, append a result row naming the commit, and update lock section 1.1. Then withdraw README owner action 3. Citation: 05 sections 9.2 step 1 and 13; 01 section 3.1 item 1 | Closed | | Iteration 3: Closed (see section "Iteration 3"). Iteration 2: not reported fixed and not fixed: `git log -1` was `28e49e6`; `git status` shows `docs/cm/`, `tools/render_review_figures.py` and `tools/tests/fixtures/schema/` untracked and `tools/traceability.py` modified. Every new result row (TV-001 runs 5 and 6, TV-003 run 3, TV-008 run 3) again names `HEAD` `28e49e6` with untracked or modified files. README owner action 3 now lists the commit content and ties it to package item H17 and this finding, which is the correct path. Closes when the commit is made after owner authorization, each record's section 3 is re-run on it, and the result rows and lock section 1.1 name that commit |
| <a id="finding-3"></a>F-03 (finding-3) | reviewer | Minor | TV-S9, TV-S10 | TV-010 line 9 (Due); `docs/cm/tool-validation/README.md` line 34; `tools/toolchain.lock.md` line 105 (section 1.2) and line 237 (section 5) | Four places say that CM plan section 13 does not list `tools/render_review_figures.py` and call adding it a cross-document item. The working-tree 05 section 13 SRR row (line 583) lists it with its known-answer test, and 05 section 9.2 has its row (line 473). The statements are stale and contradict the single authoritative schedule. Fix: set Due to "SRR (CM plan section 13)" in TV-010 and the README index, and remove the notes in lock sections 1.2 and 5 | Verified | | Closed. TV-010 line 9 Due is "SRR (CM plan section 13, SRR row; its known-answer row is in CM plan section 9.2)". README index line 34 gives Due SRR under the column "Due (CM plan section 13)" with no cross-document note. Lock line 105 (section 1.2) and line 237 (section 5) carry no statement that the plan omits the tool; the lock change log row of 2026-09-26 (line 255) records the removal |
| <a id="finding-4"></a>F-04 (finding-4) | reviewer | Minor | CK-CODE-E1, TV-S7 | TV-010 line 62 (limitation 3); `tools/render_review_figures.py` lines 621 and 622 | Limitation 3 says the axis ranges of the requirements-by-group figure are fixed ("0 to 25 and 0 to 20"), so a count above them would draw outside the axis. The code sets `ax.set_xlim(0, max(29, widest + 3))` and `ax2.set_xlim(0, max(20, most_tbr + 3))`. The axes grow with the data, and the main axis starts at 29, not 25. The record states a defect the tool does not have and misstates the range. Fix: rewrite limitation 3 to describe the actual rule (minimum ranges 29 and 20, extended to the largest count plus 3), or add a known answer with a count above 29 and cite it | Verified | | Closed. TV-010 line 62 limitation 3 now states the ranges `max(29, largest group count + 3)` and `max(20, largest open-TBR count + 3)`, which equal `tools/render_review_figures.py` lines 621 and 622 (blob still `979beb13`, the tool is unchanged). The thresholds it names (group count above 26, open-TBR count above 17) follow from those expressions, and it states honestly that the extension branch has no known answer |
| <a id="finding-5"></a>F-05 (finding-5) | reviewer | Minor | TV-S3, TV-S4 | TV-003 line 33 (purpose 5, "2 on a usage error"); TV-008 line 30 (purpose 4, "Exit 1 on any conversion or render failure"); `tools/tests/test_render_deck.py` lines 54 and 75 | Two accredited exit-code purposes have no known answer. No test asserts exit 2 of `validate_docs.py`. The reviewer observed exit 2 from argparse on `--bogus`, but that run is not part of the record. `test_render_deck.py` asserts only exit 0 and exit 2, and no seeded conversion or render failure checks exit 1 (`render_deck.py` lines 77, 82, 113). 05 section 9.1 requires class B tools to have a known-answer test with a seeded fault for what is accredited. Fix: add a usage-error test to `test_validate_docs.py` and a seeded failure (for example a deck with an AsciiDoc error, or an unreachable shell path) to `test_render_deck.py`, or remove those clauses from the purposes and scope statements | Verified | | Closed. `test_validate_docs.py` (blob `8944a389`) adds `UsageErrorTests`: `--bogus` and a `--root` that is not a directory each assert exit 2, the argparse message on stderr and no PASS or FAIL output (`validate_docs.py` line 865 `parser.error`). `test_render_deck.py` (blob `ff58fb7b`) adds `SeededFailures`: an unreadable deck makes the converter fail (exit 1, `EACCES`, no HTML, no `png/`) and a headless shell replaced by `/usr/bin/false` makes slide 1 fail (exit 1, "render failed for slide 1", no slide PNG). The tools are unchanged (`validate_docs.py` `2bedc2a7`, `render_deck.py` `b42425e9`). Reviewer re-run: `-p test_render_deck.py` 5 tests OK, none skipped; `-p test_validate_docs.py -k UsageErrorTests` 2 tests OK. TV-003 (run 3, 134 tests) and TV-008 (run 3, 5 tests, 0 skipped) cite them in sections 3 and 4 |
| <a id="finding-6"></a>F-06 (finding-6) | reviewer | Minor | TV-S1 | TV-002 line 19 | The record says "239 lines added and 9 removed against `28e49e6`". `git diff --numstat 28e49e6 -- tools/traceability.py` gives 235 added and 4 removed (239 changed lines in all). Fix: correct the counts | Verified | | Closed. TV-002 line 19 now reads "235 lines added and 4 removed against `28e49e6`", equal to `git diff --numstat 28e49e6 -- tools/traceability.py` (235, 4) re-run by the reviewer; the tool blob is still `0a867523`. Observation, no finding: the sentence that follows ("corrected 2026-09-26 after INSP-015 finding-6 by another author on 2026-09-25") joins two clauses ambiguously; the facts it carries are right |
| <a id="finding-7"></a>F-07 (finding-7) | reviewer (iteration 3) | Minor | TV-S1, TV-S10 | `docs/cm/tool-validation/TV-003-validate-docs.md` lines 1, 6, 20 to 21 and 103; `TV-010-render-review-figures.md` lines 1, 6, 17 to 19, 65 and 85; `README.md` lines 27, 34 and 49; `tools/toolchain.lock.md` lines 106 and 112 | At HEAD the records still describe `tools/validate_docs.py` blob `33ab5a83` and `tools/render_review_figures.py` blob `6f3018fd` as working-tree files "not yet committed", the proposed scopes ACC-VALDOCS-001 and ACC-FIGS-001 say "once committed", and README owner action 3 is "Open again ... authorize their commit". Both blobs, with `test_validate_docs.py` `4fb5bcc7`, `test_render_review_figures.py` `cb54d28b` and the `review_figures/` fixture (tree digest `1a2dae0b`, recomputed by the reviewer), were committed in `3de1e2d` and are unchanged at HEAD, but no result row of TV-003 or TV-010 names a commit that contains them (05 section 9.2 step 1, "commit SHA tested"). The tested content is exact and committed, and the reviewer's run on an export of HEAD reproduces TV-003 (142 tests) and TV-010 (42 tests) with every identity equal to HEAD, so the gap is in the record text, not in the evidence. Fix: append a section 4 row to TV-003 and TV-010 naming `3de1e2d` or a later commit, correct the status lines, headings, identification states, limitation 1 of TV-010 and the two scope statements, close README owner action 3 for TV-003 and TV-010, and update lock rows 106 and 112 | Lien | PDR | Lien: fix before PDR (convergence rule; charter section 4 item 3) |

## Cross-document items (outside this product; for Claude)

1. `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` are absent while their instances exist. `validate_docs.py` exits 1, and `test_validate_docs.RepositoryTests` fails (repository content, lock repository-content row). Owners: the allocation and measurements authors.
2. `tools/render_review_figures.py --review SRR --check` exits 1. `docs/reviews/SRR/package.md` section 8 gives group "Keying and keyer" 11 open TBR, while `docs/requirements/sys/requirements.json` gives 16. Owner: the package author. The figures cannot be regenerated until this is fixed.
3. `tools/requirements.txt` lists ten unpinned names. 05 section 13 SRR row (AL-4) requires `==` pins of lock section 2. This is TV-001 limitation 4, and a remaining row 20 or CM shortfall. Owner: the CM author.
4. `docs/reviews/SRR/figures/risk-matrix.py` and `concept-block-diagram.py` generate package figures (render_review_figures.py comment, lines 953 to 957). 05 section 9.1 class B covers review-package figure generators, but neither has a TV record or a place in 05 section 13. Owner: package item H10.
5. `docs/cm/tool-validation/README.md` owner action 1 notes that no checklist template for TV records exists, and 08 section 3.5 holds a review without its checklist. This review used the code checklist plus 05 section 9.2 and section 13 as items TV-S1 to TV-S10, as assigned. A `peer-review-checklist-tool-validation.md`, or a TV section added to the code checklist, would make the criteria auditable. This is a charter or process issue for the owner.

## Measurements (SWE-089)

Iteration 1: items checked: 10 TV criteria, 7 lock rows, 7 readiness rows and 55 code-checklist items (40 N/A). Items answered No: TV-S1, TV-S4, TV-S9 and CK-CODE-E1. Findings: 2 Major, 4 Minor. Effort: 48 turns, 65 minutes. Lines reviewed: 953 record lines, 273 lock lines, a 239-line tool delta and 1176 new tool lines (sampled around the cited ranges), and 3844 test lines (by execution and targeted reading).

Iteration 2: six findings re-checked; five Verified (F-01 Major; F-03, F-04, F-05, F-06 Minor), one Open (F-02 Major); 0 disputed, 0 deferred. Items answered No after iteration 2: TV-S1 and TV-S9 (both F-02). Effort for iteration 2: 14 turns, 20 minutes (cumulative 62 turns, 85 minutes in the front matter).

Iteration 3: six findings re-checked, all Closed; one new Minor (F-07), Lien: fix before PDR; 0 disputed, 0 deferred. Items answered No after iteration 3: TV-S9 (owner accreditation pending, decision 114; not a finding). Effort for iteration 3: 32 turns, 45 minutes (cumulative 94 turns, 130 minutes in the front matter).

## Closure

The record stays Open (`record_status: Open`, `date_closed: null`) until the software lead closes it. The verdict is APPROVED (with liens) at iteration 3.

| Finding | Severity | Disposition (iteration 3) | Where verified |
|---|---|---|---|
| F-01 | Major | Closed | TV-001 sections 2, 3, 4 and 9; `fixtures/schema/` at HEAD; reviewer re-run of `python-jsonschema-2026-09-26-r5.sh` on an export of HEAD |
| F-02 | Major | Closed | TV-001 to TV-010 section 4 rows at `400e59d`; `evidence/python-tools-2026-09-26-r5-head.log.txt`; lock line 59; README line 49; reviewer re-run on an export of HEAD with every identity equal to HEAD |
| F-03 | Minor | Closed | TV-010 line 9; README line 34 |
| F-04 | Minor | Closed | TV-010 line 67 against `render_review_figures.py` lines 723 and 724 (blob `6f3018fd`) |
| F-05 | Minor | Closed | `test_validate_docs.py` `UsageErrorTests`; `test_render_deck.py` `SeededFailures`; reviewer re-run on HEAD |
| F-06 | Minor | Closed | TV-002 line 19 |
| F-07 | Minor | Lien: fix before PDR | TV-003 and TV-010 line 6; README lines 27, 34 and 49; lock lines 106 and 112 |

Counts: 0 Major open; 1 Minor lien; 6 Closed; 0 disputed; 0 deferred. Verdict APPROVED (with liens).

Next steps: the software lead closes the record. CM plan section 9.2 step 3 is then completed by writing this record's id, date and result into section 8 of each TV record, which the F-07 edit can carry. The owner records the accreditation decision in section 9 of each record (decision 114, owner action OA-7). For TV-003 and TV-010 that decision names the committed blobs `33ab5a83` and `6f3018fd`. The iteration 2 closure text is kept below for the audit trail.

### Closure as written at iteration 2

The record is Open (`record_status: Open`, `date_closed: null`).

| Finding | Severity | Disposition (iteration 2) | Where verified |
|---|---|---|---|
| F-01 | Major | Closed (Verified) | TV-001 sections 2, 3, 4 and 9; `fixtures/schema/` `keywords.schema.json`, `keywords-invalid.json`, `known-answers.json`; reviewer re-run of `python-jsonschema-2026-09-26.sh` |
| F-02 | Major | Open | not reported fixed; `HEAD` `28e49e6`, product untracked or modified |
| F-03 | Minor | Closed (Verified) | TV-010 line 9; README line 34; lock lines 105, 237 and 255 |
| F-04 | Minor | Closed (Verified) | TV-010 line 62 against `render_review_figures.py` lines 621 and 622 |
| F-05 | Minor | Closed (Verified) | `test_validate_docs.py` `UsageErrorTests`; `test_render_deck.py` `SeededFailures`; TV-003 and TV-008 run 3; reviewer re-runs |
| F-06 | Minor | Closed (Verified) | TV-002 line 19 against `git diff --numstat` |

Counts: 1 Major Open, 0 Minor Open; 5 Verified; 0 disputed; 0 deferred. Verdict stays NEEDS CHANGES while F-02 is Open.

To close: the owner authorizes the commit (package item H17; README owner action 3); Claude commits the tools, tests, fixtures, records and evidence; each TV record's section 3 is re-run on that commit and a result row names it; lock section 1.1 names it. A re-review (iteration 3; 01 section 13 limits `iteration` to 1 to 3) then verifies F-02, sets the verdict, and the software lead closes the record. After closure, CM plan section 9.2 step 3 is completed by writing into section 8 of each TV record: this record's id, date and result. The owner then records the accreditation decision in section 9 of each record.
