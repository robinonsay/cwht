---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the tool validation review INSP-041
# (docs/reviews/PDR/checklists/tool-validation-tv-013.md, iteration 2 by reviewer:WP-PDR-08-tv-013-iter2,
# committed f38159d), requested there as "SA pair needed" and named by PDR work plan WP-PDR-08 ("Reviewer:
# independent reviewer plus SA"), wave 0.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged).
# The `checklist` field names peer-review-checklist-code revision B, the checklist INSP-041 names for the same
# reason: tools/validate_docs.py fails a record whose `checklist` names a template absent from main, and the lead
# SE convention of 2026-09-27 does not change the validator. The field `assurance_checklist` names the template
# actually applied (the form of the sibling WP-PDR-08 pair INSP-048).
id: INSP-049
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-013-software-assurance.md
product: docs/cm/tool-validation/TV-013-measurements.md
# product_commit and product_files: equal to INSP-041 iteration 2 (readiness R1; rule C2). Every blob below is on
# main and equal to its HEAD blob (git rev-parse HEAD:<path> at 13a4f66, 2026-09-27): the products are not
# branch-only, so the lead SE branch-only convention concerns only the checklist template
product_commit: "c827202144e73328b816e666e48dbcd1b3afaae8"
product_files: ["docs/cm/tool-validation/TV-013-measurements.md@71a676ef74ba9990dc307d97ed82015f06be5ec2", "docs/cm/tool-validation/evidence/measurements-2026-09-27.log.txt@8868280979b422742e7d04f6ee5869ffa37c8dd2", "docs/cm/tool-validation/evidence/measurements-2026-09-27-r3.log.txt@eff9035ff7a85ac9c7e7778d755ed5f028510909", "tools/measurements.py@abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a", "tools/tests/test_measurements.py@7ccc293e102f58c62d676b94074bc17b3232e166", "tools/tests/fixtures/measurements/invalid.json@15231171b06297dfd45632bef5d22757374b0970", "tools/tests/fixtures/measurements/junit/empty.xml@a5e08f193d942833cc2b5283ff72e8740f7fa773", "tools/tests/fixtures/measurements/junit/run1.xml@cb071c37b1f13fa52fe0a9958aaababfb736f54b", "tools/tests/fixtures/measurements/junit/run2-diff.xml@7294a61c042aa6105dc84d79a702afc7518a4efb", "tools/tests/fixtures/measurements/junit/run2-same.xml@cb071c37b1f13fa52fe0a9958aaababfb736f54b", "tools/tests/fixtures/measurements/junit/run-failing.xml@13eb0ded84967e44f211202655fc0b66c42bd120", "tools/tests/fixtures/measurements/junit/run-skipped.xml@11e505175f394fbe934624cffc91371ea0faf775", "tools/tests/fixtures/measurements/lcov/branch-condition.json@e569b1722f7fa5237f8c1b149a38e714d45b3f70", "tools/tests/fixtures/measurements/lcov/lcov.info@9368449affe9f81534ec020dcf2c983436ff343c", "tools/tests/fixtures/measurements/linkmap/cwht-app.map@e5557024967701cbee3661601e39572bf22afa80", "tools/tests/fixtures/measurements/linkmap/link.ld@8ab6e6e242e3daf0449ff34cb58f75168acabf40", "tools/tests/fixtures/measurements/linkmap/over-red-line.map@ab15c48a1463c8b124198eae273ea02d2877ea57", "tools/tests/fixtures/measurements/linkmap/small.ld@f6be72a5bfa9bcfbe99761771549e9fd95b810d1", "tools/tests/fixtures/measurements/records/records.json@5b760ab006e936e10d28130373b1c525c4dc79c1", "tools/tests/fixtures/measurements/valid.json@3938cd57aaeb99e1c5065594c915c99014d34026", "tools/toolchain.lock.md@b45c8654476be36b3b1918fbe9ff2040ac6c941e", "docs/cm/tool-validation/README.md@87fb1e8cab28baf623981a3386fb260f5263d1be"]
fixture_trees: ["tools/tests/fixtures/measurements@ed4414ecd9336349d4ba03cd8257b0079d470d8d"]
# inputs read (not reviewed), at HEAD 13a4f66
input_files: ["docs/reviews/PDR/checklists/tool-validation-tv-013.md@bd250f023f10e8b835b59c74e49c84c9130cc766 (INSP-041 iteration 2)", "docs/process/07-software-engineering-plan.md", "docs/process/03-software-classification-and-rmm.md", "docs/process/05-configuration-and-data-management.md", "docs/process/rmm.json", "docs/plan/pdr-work-plan.md", "docs/plan/tpm.json", "docs/plan/measurements.json", "tools/sw_gate.sh", "firmware/.config/nextest.toml", "docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900 (CR-012 branch)", "docs/reviews/PDR/checklists/tool-validation-rust-toolchain-software-assurance.md (INSP-048)"]
paired_record: INSP-041
tv_ids: [TV-013]
# product_type: 07 section 2.1.1 has no row for tool validation records (the dispatch gap is INSP-048 finding-1,
# cited here, not raised again). Task set applied: the section B row "Every product type", the swe-136 and swe-070
# tool tasks (section B row trade-study-or-adr "when the decision selects a tool"; TV template section H), and the
# section 7.1 tasks of every SWE the product governs (TV-013 "Governs" row: SWE-090, SWE-093, SWE-186) or whose
# rmm.json row names the tool (SWE-200), plus SWE-189 and SWE-190 for purpose 3 (07 section 15)
product_type: tool-validation
# criticality: 03 section 3 table row "Firmware test tooling" (03 line 12) names tools/measurements.py: "No;
# verification software of safety-critical components, rigor of section 4.3.1"
criticality: neither
product_size: 1 TV record (92 lines), 6 purposes, 18 known-answer tests, 15 fixture files; tool 456 lines, test module 256 lines
sprint: PDR-prep
author_agent: "author:SRR R3 and WP-PDR-08 (Claude as software lead and tool owner)"
reviewer_agent: "sa-reviewer:WP-PDR-08-tv-013"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-08-tv-013 (software assurance function; paired file review INSP-041 by reviewer:WP-PDR-08-tv-013-iter2, iteration 1 by reviewer:WP-PDR-08-tv-013)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major; one Minor finding, a lien due the CDR
# readiness declaration under PDR work plan rule C1 unless fixed with the WP-PDR-09 revision of the tool)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES here, as INSP-048 holds its own:
# the product blobs are on main, but the checklist applied exists only on cr/CR-012-pdr-checklist-templates (lead
# SE convention of 2026-09-27), and INSP-041 does not yet name this record (paired_record, assurance_reviewer_agent,
# assurance_verdict; each reviewer updates only its own record). Both reviews of the product are now APPROVED; the
# software lead sets APPROVED on both records when INSP-041 carries the pairing and CR-012 merges with the template
# blob unchanged
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 1
findings_open: 1
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 1
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-186 7.1 task 1", "swe-090 7.1 task 1", "swe-090 7.1 task 2", "swe-093 7.1 task 1", "swe-093 7.1 task 2", "swe-189 7.1 task 1", "swe-190 7.1 task 1", "swe-190 7.1 task 2", "swe-190 7.1 task 3", "swe-200 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
items_no: []
effort_turns: 36
effort_minutes: 55
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-049: software assurance second review of TV-013 (`tools/measurements.py`), WP-PDR-08

**Product.** `docs/cm/tool-validation/TV-013-measurements.md` blob `71a676ef` at `c827202`, with the tool `tools/measurements.py` blob `abe25acb`, the known-answer module `tools/tests/test_measurements.py` blob `7ccc293e`, the fixture tree `ed4414ec` (15 files), the run 2 and run 3 evidence logs, the lock and the TV README: the 22 `product_files` of INSP-041 iteration 2, each recomputed with `git rev-parse HEAD:<path>` at `13a4f66` and equal. **Paired record:** INSP-041 (`tool-validation-tv-013.md`, blob `bd250f02`), reviewer verdict APPROVED at iteration 2 with liens finding-2 to finding-4.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Sections R, A, B, E and F are applied; section C is N/A (criticality neither) and section D is answered N/A item by item (the tool traces to no hazard). The TV template section H items (swe-136 and swe-070) are applied here as task rows.

**Acceptance criteria (rule C7).** Every task of the section B row "Every product type"; swe-136 task 1 and swe-070 task 1 (the tool tasks); the section 7.1 tasks of SWE-090, SWE-093 and SWE-186 (TV-013 "Governs" row, line 8), SWE-200 (its `rmm.json` row names the TPM-012 mirror of `tools/measurements.py`), SWE-189 and SWE-190 (purpose 3 summarises MSR-13 and MSR-14); every purpose 1 to 6 of TV-013 section 2 read for the clauses the known-answer tests leave unseeded; the 03 row "Firmware test tooling" rigor (03 section 4.3.1: a seeded fault for each safety-relevant check, `rmm.json` SWE-136 implementation text); the INSP-041 findings re-read under the assurance lens.

**Independence (rule C4).** This invocation authored no part of WP-PDR-08, of the tool, of TV-013 or of INSP-041 (either iteration), and edited no product file; it is neither the author nor either file-review invocation of INSP-041. **Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-041 WP-PDR-08 tool validation record peer review"; "SWEHB software assurance tasking software tool accreditation validate tools SWE-136 7.1"; "validate_docs peer review record schema paired_record product_type assurance_reviewer_agent checks"; "measurements.json evidence preservation failures check-records 80 evidence entries superseded records fix"). `grep -n`, `awk` over the SWEHB pages and `git grep` were used afterwards only to pin lines and extract the section 7.1 task lists. **Headless, no download, no LTspice.** The rustos working tree was not read (no check below passes the default `../rustos/firmware/pico2/link.ld`; every link-map run named a fixture or scratch script).

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-186 7.1 task 1, swe-136 7.1 task 1 | TV-013 section 2 purposes 1 and 2 (lines 25, 26) and section 3 pass criteria (line 42); `tools/measurements.py:151` (red-line comparison) and `:174` to `:175` (`error` outcome); `tools/tests/test_measurements.py` `LinkMapTests` and `DiffRunsTests` | Two stated behaviours have no known answer, and a mutation of each survives the 18 tests (independent checks M1 and M2 below). (a) Purpose 2 "all passed" is now seeded for the `failure` and `skipped` outcomes (INSP-041 finding-1 Verified), but the tool classifies a third non-passed outcome, `error` (`<error>`, `rerunError`, `flakyError`); mapping `error` to passed (M2) leaves all 18 tests OK, so a defect that let two identically errored G3 runs pass would not be detected by the validation. The real tool is correct (reviewer run on two identical files with one `<error>` case: `NOT PASSED (... 'error')`, `FAIL`, exit 1). Gate G3 is the repeatability check of the HostUnit evidence for the safety-critical decisions, and 03 line 12 gives this tool the section 4.3.1 rigor (a seeded fault for each safety-relevant check), so each non-passed outcome the tool distinguishes needs its seeded case. (b) Purpose 1 "failing above the TPM-010 and TPM-011 red lines" has no boundary answer: changing `<=` to `<` at `:151` (M1) leaves all tests OK. The tool is correct against `docs/plan/tpm.json` TPM-010 `threshold_red` "below 30 %" unused (reviewer run with a 1000-byte FLASH region: 700 B = 70.00 % PASS exit 0, 701 B FAIL exit 1). Minor: the tool gives the right answer in both cases, every current MSR record is `credit: false`, and no safety conclusion changes; not raised by INSP-041 (its finding-2 lists other clauses). Fix: add `junit/run-error.xml` (one `<error>` case) with a test asserting exit 1 and the `NOT PASSED ... 'error'` line, and a boundary map at exactly the FLASH red line (PASS) and one byte above (FAIL); re-run as TV-013 run 4 with a mutation check, on the same revision as the INSP-041 finding-2 fix and the WP-PDR-09 C-185 change (INSP-041 X-2), followed by one delta of INSP-041 and of this record. If the owner accredits before the fix, the ACC-MEASURE-001 scope statement names these two clauses (and the INSP-041 finding-2 clauses) as unvalidated | Open | Pending | |

**INSP-041 findings under the assurance lens (not raised again; template finding rules).** finding-1 (Major, Verified): concur; reproduced independently: the iteration 1 mutation (`ok = bool(a) and a == b`) in a scratch export fails `test_identical_failing_runs_fail` and `test_identical_skipped_runs_fail` (2 of 18). finding-2 (Minor lien): concur at Minor; the "evidence ... does not exist" clause of purpose 4 was confirmed unseeded (M3 survives), while the append-only, `updated`, catalog and re-derivation-mismatch clauses are seeded (M4, M5, M7, M8 killed). finding-3 (Minor lien): concur at Minor, with one assurance addition for its fix: the default `--link-ld` of `--check-records` is `../rustos/firmware/pico2/link.ld` (`:79`), the rustos working tree, which is neither pinned nor checked by the tool; inside the gate, G0 checks that rustos HEAD equals the lock pin and that its firmware paths are clean (`tools/sw_gate.sh:117` to `:121`) before G2 reads the same file (`:155`), but a standalone `--check-records` run has no such check, so its MSR-18 and MSR-19 re-derivation depends on an uncontrolled input as well as being skipped silently when it is absent. The fix of finding-3 (a) should name the source of the script it re-derives against (for example the pinned blob, `git show <pin>:firmware/pico2/link.ld`). No safety conclusion changes (MSR-18 and MSR-19 are not safety measures). finding-4 (Minor lien): concur; TV-013 line 6 ("Independent review (delta iteration) ... pending") and section 8 (one row, iteration 1) also predate INSP-041 iteration 2 (`f38159d`) and this record; the author writes section 8 after the records (TV template), so this is currency, not a new defect.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the review of a tool whose outputs (gate G3 repeatability, G6 coverage summary) are verification evidence of the safety-critical components (03 line 12, "verification software of safety-critical components") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 section 15) by this record; the NASA-STD-8739.8 part is relieved | `rmm.json` SWE-022 T (the standard is not in the corpus) | none |
| swe-136 7.1 task 1 | | Yes | Validated: TV-013 runs 1 to 3 (run 3 at `c28dd60`, 18 tests twice, mutation check), independent review INSP-041 APPROVED at iteration 2; reviewer re-run here equal (18 OK twice). Accredited: not yet, and not yet due (05 section 13 PDR row; TV-013 section 9 "Pending"); until then the output is developer evidence (05 section 9.1), and every MSR-13, MSR-18 and MSR-19 record in `docs/plan/measurements.json` is `credit: false` (checked by script). Validation gaps under the 03 section 4.3.1 rigor: finding-1 and INSP-041 finding-2 | | finding-1 |
| swe-070 7.1 task 1 | | Yes | Applied: the tool's G3 and G6 outputs are analysis results used in the qualification of the flight software (the release gate, 07 section 8.4; `rmm.json` SWE-070 names "Python checkers"). Same state as swe-136: validated, accreditation pending, no credited use. INSP-041 answers TV-H2 N/A ("not an analysis tool") while listing `swe-070 7.1 task 1` in `assurance_tasks_applied`; cross item X-1 | | none |
| swe-186 7.1 task 1 | | Yes | The G3 procedure keeps both JUnit files (`tools/sw_gate.sh:238` to `:251`; 07 section 8.4 G3 row, copied into `TC-SW-REG-001-r<N>/` at release); the `ci` profile has `retries = 0` (`firmware/.config/nextest.toml`), so a flaky pass cannot be recorded as passed; the tool's comparison is validated for identical, non-empty and all-passed (failure and skipped); the `error` outcome is unseeded | | finding-1 |
| swe-090 7.1 task 1 | | Yes | The tool is the rule checker of the measurement repository (purpose 4). Reviewer run of `--check-records` on the repository at `13a4f66`: exit 1, 80 evidence failures at `1d423e5`, as TV-013 line 53 records; tracked as INSP-010 finding-15 (lien "fix before PDR") and `tools/README.md` measurements section. The append and TPM mirror are not implemented (TV-013 limitation 1, due FW-B1); cross item X-2 | | none |
| swe-090 7.1 task 2 | | Yes | `--analyze` resolves the current records per 07 section 11.3 without plots (limitation 3, declared); trending is the software lead's analysis at each package (07 section 11.3; WP-PDR-47) | | none |
| swe-090 7.1 task 3 | | N/A | No organizational repository | `rmm.json` SWE-174 NA (Center measurement reporting; intent preserved in `docs/plan/tpm.json`) | none |
| swe-093 7.1 task 1 | | Yes | `--analyze` implements the 07 section 11.1 current-record rule (supersedes retires; first Measured retires Not yet measured); seeded by `test_analyze_current_records` | | none |
| swe-093 7.1 task 2 | | Yes | This record's measurements (front matter) are the MSR-20 and MSR-21 inputs for the assurance scope `INSP-049` (07 section 10.3) | | none |
| swe-189 7.1 task 1 | | Yes | Purpose 3 summarises MSR-13 per crate and MSR-14 totals; values recorded in `measurements.json` (MSR-13 two scopes Measured, `credit: false`; MSR-14 Not yet measured); region coverage and the 100 % thresholds come from `cargo llvm-cov` (limitation 4, declared) | | none |
| swe-190 7.1 task 1 | | Yes | Coverage is computed from executed runs (`cargo llvm-cov nextest`, 07 section 8.4 G6); the tool only summarises the lcov and JSON exports, seeded by `test_totals` (hand-counted) | | none |
| swe-190 7.1 task 2 | | Yes | The tool reports totals, not locations; uncovered code is identified from the `cargo llvm-cov` report and classified in the coverage report (`rmm.json` SWE-190, planned CDR). TV-013 does not claim identification, so no gap in the product | | none |
| swe-190 7.1 task 3 | | Yes | No uncovered code exists in the FW-B0 scopes (MSR-13 100 % lines and functions for `cwht-core` and `cwht-hal-mock`); the risk assessment of uncovered code is due with the first coverage report (CDR) | | none |
| swe-200 7.1 task 1 | | Yes | `rmm.json` SWE-200 plans "the TPM-012 mirror of tools/measurements.py" for PDR; the tool does not implement it (limitation 1) and 07 section 11.1 puts the first mirror at FW-B1, a PDR exit item; no PDR work plan output names the tool change. Not a TV-013 defect (the limitation is declared); cross item X-2 | | none |
| swe-200 7.1 task 2 | | N/A | The product computes and analyzes no volatility | 07 section 11.3 (analysis at each package, WP-PDR-47 with its own SA pair) | none |

### Independent assurance checks

Run in a scratch export (`git archive HEAD tools`, tool blob `abe25acb`, test blob `7ccc293e` recomputed with `git hash-object`); no repository file changed. Each mutation is one exact-string replacement in the exported tool, followed by `.venv/bin/python -m unittest discover -s tools/tests -p test_measurements.py`.

| Check | Change or command | Exit | Result |
|---|---|---|---|
| Re-run, twice | unmodified export | 0, 0 | `Ran 18 tests`, `OK` both passes; equal to TV-013 run 3 |
| M0 (INSP-041 iteration 1 mutation) | `:189` `ok = bool(a) and a == b` | 1 | killed: 2 of 18 fail (`test_identical_failing_runs_fail`, `test_identical_skipped_runs_fail`) |
| M1 red-line boundary | `:151` `<=` to `<` | 0 | survives, 18 OK (finding-1 b) |
| M2 `error` outcome | `:175` `outcome = "error"` to `"passed"` | 0 | survives, 18 OK (finding-1 a) |
| M3 missing evidence | after `:369`, `continue` when the evidence file is absent | 0 | survives (INSP-041 finding-2, `:369`) |
| M4 append-only | `if records[:len(old)] != old:` to `if False:` | 1 | killed by `test_seeded_record_faults` |
| M5 `updated` rule | `if records and data.get("updated") != latest:` to `if False:` | 1 | killed by `test_git_rules_not_applied_outside_a_work_tree` |
| M6 LMA for FLASH | FLASH extent from VMA instead of LMA | 1 | killed by `test_red_line` |
| M7 re-derivation mismatch | `if mismatch:` to `if False:` | 1 | killed by `test_rederivation_mismatch_in_a_commit` |
| M8 catalog | `if r.get("id") not in CATALOG:` to `if False:` | 1 | killed by `test_seeded_record_faults` |
| Real tool, identical errored runs | `--diff-runs run-error.xml run-error.xml` (copy of `run-failing.xml` with `<error>`) | 1 | `NOT PASSED ('cwht-core::heartbeat', 'spin_wait_counts', 'error')`, `FAIL identical result sets, all passed (SWE-186)` |
| Real tool, red-line boundary | `--link-map` with a scratch script of 1000-byte regions; `.text` 0x2bc, then 0x2bd | 0, 1 | 700 B = 70.00 % `PASS`; 701 B = 70.10 % `FAIL`; equal to TPM-010 `threshold_red` "below 30 %" unused |
| Repository records | `.venv/bin/python tools/measurements.py --check-records --link-ld /dev/null` at `13a4f66` | 1 | `measurements: 89 records, FAIL (80 failure(s))`; equal to TV-013 line 53 |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | 22 blobs and the fixture tree `ed4414ec` equal to INSP-041 `product_files` and to `git rev-parse HEAD:<path>` at `13a4f66`; no product commit after `c827202` (`git log c827202..HEAD` on the product paths is empty) |
| R2 | 07 section 2.1.1 row and criticality identified | Yes, with INSP-048 finding-1 | No 07 section 2.1.1 row exists for TV records; routed by PDR work plan WP-PDR-08 (owner-approved 2026-09-27). Criticality neither: 03 line 12 (firmware test tooling, `tools/measurements.py`: "No; verification software of safety-critical components, rigor of section 4.3.1") |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with a scratch `--output` reports no violation for the ids touched | Yes | `validate_docs.py` exit 1: 64 passed, 5 failed, all five SRR records (`adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`), none a product file of this review. `traceability.py --report-only --output <scratch>/tr.md`: exit 0, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148, not touched) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-041 committed at `1b93d83` (iteration 1, `reviewer:WP-PDR-08-tv-013`) and `f38159d` (iteration 2, `reviewer:WP-PDR-08-tv-013-iter2`); `author_agent` "author:SRR R3 and WP-PDR-08"; this invocation is `sa-reviewer:WP-PDR-08-tv-013` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with INSP-048 finding-1 | Routed by PDR work plan WP-PDR-08 line 264 ("independent reviewer plus SA"); 07 section 2.1.1 (lines 110 to 126) has no TV row and the TV template sets `assurance_required: false` (CR-012 branch, lines 59 to 63). The same dispatch gap is INSP-048 finding-1 (Minor), whose fix covers TV-013; not raised again. TV-013 itself cites no dispatch basis, so it carries no wrong claim |
| SA-A2 | Yes | Four invocations: author (Claude as software lead and tool owner), file reviewers `reviewer:WP-PDR-08-tv-013` and `reviewer:WP-PDR-08-tv-013-iter2`, this assurance reviewer; INSP-041 records the request for the pair ("pending (separate invocation ...)"), and this record names the pairing (cross item X-3) |
| SA-A3 | Yes | Same `product`, same `product_commit` `c827202`, same 22 blobs and fixture tree; the pending WP-PDR-09 change of `abe25acb` (C-185) is a re-validation trigger covered by a delta of both records (INSP-041 X-2) |
| SA-A4 | Yes | INSP-041 applied the tool validation item set (revision A, CR-012 branch) for `tool_kind` repository-tool with the code checklist revision B for item TV-G1-3, every item answered with evidence (sections R, A to F, G1, H and the code review); SWE-088 criteria a to d met (checklist, readiness R1 to R5, findings with state, participants named). The TV-H2 N/A answer against its own `assurance_tasks_applied` is cross item X-1 |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table above: the row "Every product type", the two tool tasks, and SWE-186, SWE-090, SWE-093 (TV-013 line 8), SWE-200 (`rmm.json` row names the tool), SWE-189 and SWE-190 (purpose 3). `assurance_tasks_applied` lists every Yes row |
| SA-B2 | Yes | N/A rows: swe-090 task 3 (`rmm.json` SWE-174 NA), swe-200 task 2 (07 section 11.3); criticality neither |
| SA-B3 | Yes | No task is answered No; finding-1 is carried by the swe-136 and swe-186 rows |

## C. SWE-134 items a to l

N/A for every item: `criticality` neither (03 line 12; 07 section 14.1 lists no tool component), so `swe134_items_checked` is empty. The tool implements no safety-critical provision; its link to the safety-critical components is as evidence producer, assessed under swe-136, swe-186 and finding-1.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | N/A | No `HZ-NNN` names the tool as a cause or control; a wrong G3 or G6 result would be a verification escape, covered by the 03 section 4.3.1 rigor (finding-1), not a hazard cause |
| SA-D2 | N/A | No component created or renamed; the 03 line 12 determination is unchanged |
| SA-D3 | N/A | No requirement or hazard changed; R3 shows 0 violations |
| SA-D4 | N/A | No safety-tagged software requirement touched |
| SA-D5 | N/A | No hazard-tracing requirement touched |
| SA-D6 | N/A | The hazard analysis is not affected by a tool validation record |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-041 finding-1 (Major) Verified at iteration 2 with an element table, a reviewer re-run and the mutation, reproduced here (M0); finding-2 to finding-4 carried as liens with owner (Claude as tool owner) and due event (CDR readiness declaration); none closed without evidence |
| SA-E2 | Yes | INSP-041 and this record both carry `findings_*`, `items_no`, `iteration`, `effort_turns`, `effort_minutes` (07 section 10.3) |
| SA-E3 | Yes | 05 Table 4-1 row 28: `tools/` and `tools/tests/` are Log with `Refs:` until accreditation puts a tool under CR control; row 30: TV records are Record. Every product commit after `baseline/srr` carries `Refs:` (`71bf509` `Refs: TV-013, ...`; `c28dd60` `Refs: TV-013, TV-020, TV-021`; `c827202` `Refs: TV-013, ...`); `3de1e2d` and `1d423e5` precede `baseline/srr` |
| SA-E4 | Yes | Runs 2 and 3 ran on commit exports (`d3de579`, `c28dd60`) with the blobs recorded (TV-013 section 4 lines 51, 52); run 1 was a working-tree run and is superseded by the commit-bound runs |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | Two assurance concerns that are not TV-013 defects: (i) the measurement repository fails its own evidence-preservation rule (80 failures), already tracked as INSP-010 finding-15 (lien fix before PDR); (ii) the append and TPM mirror that 07 section 11.1 and `rmm.json` SWE-200 plan for FW-B1 and PDR have no PDR work plan output, submitted to the lead SE as cross item X-2 for a risk entry with tag `assurance` to the risk register writer (WP-PDR-18, plan section 5.3) or a WP output |
| SA-F2 | Yes | Front matter carries `findings_*`, `assurance_findings_major` 0 and `assurance_findings_minor` 1 (the same finding, counted once, 07 section 10.2), `items_no`, effort |
| SA-F3 | Yes | Verdict, open finding, tasks applied, reliefs and cross items are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true; every task SA-B1 requires is in the task table; every applicable item of sections A, E and F is answered and sections C and D are N/A with their reasons; zero Major findings. finding-1 is Minor and Open: INSP-041 is past its first APPROVED reviewer verdict, so under PDR work plan rule C1 and 08 section 3.2 ("Minor findings ride with APPROVED") it rides with this APPROVED verdict and is a lien due at the CDR readiness declaration unless fixed with the WP-PDR-09 revision of the tool (TV-013 run 4). **`assurance_verdict: APPROVED`.** The record `verdict` stays NEEDS CHANGES for the software lead to set (07 section 10.2), for the two reasons in the front matter: the checklist template is branch-only until CR-012 merges, and INSP-041 does not yet carry `paired_record: INSP-049`.

## Cross items (returned to the lead SE)

- **X-1.** INSP-041 lists `swe-070 7.1 task 1` in `assurance_tasks_applied` but answers TV-H2 N/A ("not an analysis tool"). Under the assurance lens the task applies (task table row); INSP-041's reviewer reconciles the answer at its next delta.
- **X-2.** The append and TPM mirror of `tools/measurements.py` (07 section 11.1: first mirror at FW-B1; `rmm.json` SWE-200 "Planned for PDR ... the TPM-012 mirror of tools/measurements.py") appear in no PDR work plan output (WP-PDR-29, WP-PDR-41 and WP-PDR-47 name the tool only as an input). Implementing them changes the tool, a TV-013 re-validation trigger (section 7). Route: a WP output, or an `rmm.json` SWE-200 text change through WP-PDR-17, and a risk entry with tag `assurance` through WP-PDR-18.
- **X-3.** INSP-041 still reads `assurance_reviewer_agent: "pending ..."`, `assurance_verdict: pending` and no `paired_record`. Its reviewer updates it to `paired_record: INSP-049`, names this reviewer and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row).
- **X-4.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `assurance_checklist` (as INSP-048 and INSP-047 plan).

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD:<path>` for the 22 `product_files` and the fixture tree at `13a4f66` | 0 | All equal to INSP-041's list |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md` | 0 | Template revision A, blob `5b135285` |
| Section 7.1 extraction (`awk`) from `docs/references/md/swehb/swe-NNN-*.md` for SWE-022, 070, 090, 093, 134, 136, 186, 189, 190, 199, 200 | 0 | Task texts used in the task table |
| Scratch re-run and mutations M0 to M8, real-tool probes | see table | See "Independent assurance checks" |
| `.venv/bin/python tools/traceability.py --report-only --output <scratch>/tr.md` | 0 | 0 violations, 2 warnings; `docs/vv/` unchanged |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; the five failures are pre-existing SRR records outside this review |

No visual product was produced or changed by this review (charter section 11 rule 3).

## Verdict format

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/cm/tool-validation/TV-013-measurements.md@71a676ef (and the 21 other INSP-041 product_files; tool abe25acb, test 7ccc293e, fixture tree ed4414ec) at c827202; PAIRED RECORD: INSP-041
PRODUCT TYPE: tool-validation (no 07 section 2.1.1 row; routed by PDR work plan WP-PDR-08); CRITICALITY: neither
FINDINGS:
- [Minor] swe-186 7.1 task 1, swe-136 7.1 task 1 (finding-1): the `error` outcome of --diff-runs and the red-line boundary of --link-map have no known answer (mutations M2 and M1 survive); the tool is correct in both.
TASKS APPLIED: swe-134 task 5, swe-022 task 1, swe-136 task 1, swe-070 task 1, swe-186 task 1, swe-090 tasks 1 and 2, swe-093 tasks 1 and 2, swe-189 task 1, swe-190 tasks 1 to 3, swe-200 task 1
TASKS N/A (relief): swe-090 task 3 (rmm.json SWE-174 NA), swe-200 task 2 (07 section 11.3)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=1 TV record, 6 purposes, 18 tests; tasks=16; tasks_no=0; mutations=9 (3 survive); turns=36; minutes=55; major=0; minor=1
```
