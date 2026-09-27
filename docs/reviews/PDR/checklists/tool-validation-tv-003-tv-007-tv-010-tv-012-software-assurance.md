---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the tool validation review INSP-100
# (docs/reviews/PDR/checklists/tool-validation-tv-003-tv-007-tv-010-tv-012.md, iteration 1 by
# reviewer:WP-PDR-09-tv-and-code, committed 3837edb), requested there in assurance_reviewer_agent and cross item
# X-1; PDR work plan WP-PDR-09 names "SA for credit tools" and CR-014 section 5 step 5 names the pair.
# Record path: 07 section 10.2 Record row, <product-slug>-software-assurance.md with the slug of INSP-100 (the path
# INSP-100 names).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged, CR-012
# still Submitted on main). The `checklist` field names peer-review-checklist-code revision B, the checklist
# INSP-100 names, because tools/validate_docs.py fails a record whose `checklist` names a template absent from
# main, and the lead SE convention of 2026-09-27 does not change the validator. `assurance_checklist` names the
# template actually applied (the form of INSP-048, INSP-049 and INSP-051).
id: INSP-101
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-003-tv-007-tv-010-tv-012-software-assurance.md
product: docs/cm/tool-validation/TV-003-validate-docs.md
# product_commit and product_files: equal to INSP-100 iteration 1 (readiness R1; rule C2), all 43 entries and the
# six trees re-checked with git rev-parse 367b3dd:<path> (CR file: main:<path>) on 2026-09-27; 38 of the 43 blobs
# exist only on the unmerged branch cr/CR-014-tool-liens-srr (5 are equal on main, the CR file among them)
product_commit: "367b3dd481fdbde0170582607d2285dfdae4bc9f"
product_files: ["docs/cm/cr/CR-014-tool-liens-srr.md@139d860d3b69c960fde9fb306470ed624c3a085e", "tools/validate_docs.py@e5b692e154eed71a664ce2bdd95b8e64906b79b8", "tools/tests/test_validate_docs.py@e9c305fc5c3e64e7796585002675c83ab5c15559", "tools/review_trend.py@9e451fa24a1707d53420cb12590fbfd39fef6f1b", "tools/tests/test_review_trend.py@9fa7908d351688612abb7f7cea7affe405220674", "tools/render_review_figures.py@7607e7c258f29d58287a15103903b99e6206b94d", "tools/tests/test_render_review_figures.py@366dc553d907f1f075ab0d3ca548526d9fb0ffda", "tools/tests/fixtures/review_figures/docs/conops/conops.md@f02154a86fee760e6ec8f73c4f6d1cb0c1c2a0f9", "tools/tests/fixtures/review_figures/docs/design/concept.md@65b554bef9df2f3c285a23aa0804d1d68b9beaaa", "tools/tests/fixtures/review_figures/docs/plan/tpm.json@45325583fef4b82a8f3fc66c25836ef3dbb83d76", "tools/tests/fixtures/review_figures/docs/requirements/sys/requirements.json@5be9a3d53aff1efa4838751b2a7778338524c839", "tools/tests/fixtures/review_figures/docs/reviews/SRR/package.md@ab1d40e0d093549607bee03451cbc3b979e125de", "tools/tests/fixtures/review_figures/docs/risk/register.json@8fd300159e7ffcbd075f3e6765174d3569611be7", "tools/tests/fixtures/review_figures/docs/risk/register.md@86e23b96ad888d05b60d3600b5475c401b970c3a", "tools/tests/fixtures/review_figures/docs/safety/hazards.json@4f973f926ea6e53491eabc668512796454b0ebc3", "tools/complexity_gate.py@e9cfd465a7412549c0347dfac59080ec83964c18", "tools/tests/test_complexity_gate.py@6199fcd8f707692ffd14c07a67a9d403d399a31e", "tools/measurements.py@cec467f17a89e61ab49b5a46cb03cfaa855c2e9b", "tools/tests/test_measurements.py@3b43ec1fb256e637c376843b3a0de56c08a318b8", "tools/sw_gate.sh@6048c8015b1e2fd4f40bf9f900ee1a69681380e0", "firmware/cwht-app/src/main.rs@3006d072986f5d6379863179000e2a2a3dd36e7c", "tools/toolchain.lock.md@836536ce9aa603aa8d53c178ad573f46b47571dc", "tools/README.md@bc4e43900b775ddca1c708dfbffda199870af0fd", "docs/cm/tool-validation/README.md@2ff68008aeac136360885f607b9eeaadb3805b8c", "docs/cm/tool-validation/TV-001-python-jsonschema.md@08125d63c20221dcf63f2f02108d405a52ba00cc", "docs/cm/tool-validation/TV-003-validate-docs.md@3eb258f15361acf137312cfc40e1befb9add333e", "docs/cm/tool-validation/TV-007-review-trend.md@1ecc089aba0131949f3ca496863dd64e8a967de6", "docs/cm/tool-validation/TV-010-render-review-figures.md@31d328fb97974bc0e4122d442a6a1dd34b8e9feb", "docs/cm/tool-validation/TV-012-complexity-gate.md@87bc6e2570d761a282976f4e01efb592039f1200", "docs/cm/tool-validation/TV-013-measurements.md@91101cf7667f5b6b6d5b0ecfb52c612a364dbc2a", "docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.py@3095a9332710be0a0a42f2ff11095a16292421b8", "docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.log.txt@d81e7dd5c58d8983556884658e3f6abd787fdd7e", "docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.sh@2adb7e8e2783184fb84ede5198324a489086f3b4", "docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.log.txt@0ccfea97171cbea82658427383a82f8bbc8eab9b", "docs/cm/tool-validation/evidence/complexity-gate-2026-09-27-r4.log.txt@10f125a61a42e817b46569fd6415d3355547061c", "docs/cm/tool-validation/evidence/requirements-freeze-2026-09-27.log.txt@84904d6d375201d95017e70c86b68db3d2f05de0", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/concept-block-diagram.png@ec80831017de889e758f04a32a20c654592a5987", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/fixture/risk-matrix.png@f5175ed8202aa9ab95686a765825ff2cc3bc7da3", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/fixture/success-criteria.png@04d4e5162f1af36b91cbb224b936e4b703bb8a76", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/review-trend-2026-09-26.png@18c38e5043579890239dd9800bafe68aa8b53182", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/review-trend-2026-10-06.png@4b5a8d463a7e246b7c02e52e9941563f44e16901", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/risk-matrix.png@fc52c4890fd6bec69fcebec26ccec31709950146", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/success-criteria.png@5fdf6a7ad94ec52e816a752f8b055628af374cf5"]
fixture_trees: ["tools/tests/fixtures/review_figures@fd5b721d4a2c29ee95a4dab8f642e15789331dcd", "docs/cm/tool-validation/evidence/wp-pdr-09-renders@7b58395d8575d8ff0860eb169c0e33abefe62b61", "tools/tests/fixtures/review_trend@2109a738ea23d5b0befdd8756a171595ddb879b6", "tools/tests/fixtures/complexity_gate@23f23d9d305fbc18fcb9cd5b8e8ba6c50581c7e5", "tools/tests/fixtures/measurements@ed4414ecd9336349d4ba03cd8257b0079d470d8d", "tools/tests/fixtures/record_state@b7c20457f2ae8c4d0fec41b52abd127003aa34ff"]
# inputs read (not reviewed), at main 3837edb unless stated
input_files: ["docs/reviews/PDR/checklists/tool-validation-tv-003-tv-007-tv-010-tv-012.md@27476ec062c0d46463acd3d4849f70afe7b1613f (INSP-100 iteration 1)", "docs/reviews/PDR/checklists/tool-validation-tv-002-software-assurance.md (INSP-051, form)", "docs/reviews/PDR/checklists/tool-validation-rust-toolchain-software-assurance.md (INSP-048 finding-1)", "docs/reviews/PDR/checklists/tool-validation-tv-013-software-assurance.md (INSP-049)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 10.2, 14.1, 14.3, 15, 22; and as on cr/CR-010-apply-srr-decisions-9-and-40)", "docs/reviews/SRR/decision-memo.md (decision 9)", "docs/plan/pdr-work-plan.md (WP-PDR-09, section 5)", "rustos objects 2ec64c0 and c54d35a (git archive and a no-checkout clone of the object store only)"]
paired_record: INSP-100
tv_ids: [TV-003, TV-007, TV-010, TV-012, TV-013]
# product_type: 07 section 2.1.1 has no row for tool validation records (the dispatch gap is INSP-048 finding-1,
# cited, not raised again). Task set applied: the section B row "Every product type"; swe-136 task 1 and swe-070
# task 1 (section B row trade-study-or-adr "when the decision selects a tool"; TV template section H); and the
# section 7.1 tasks of the SWEs the changed tools implement or enforce: SWE-220 and SWE-135 (complexity_gate.py,
# gate G5), SWE-219 and SWE-186 (measurements.py, gates G3 and G6), SWE-081 (sw_gate.sh G0, the lock), SWE-080
# (CR-014), SWE-087, SWE-088, SWE-089 (validate_docs.py record rules), SWE-090 (MSR-17), SWE-040 (07 section 15)
product_type: tool-validation
# criticality: a tool is neither safety-critical nor mission-critical (03 sections 4.3.1 and 6.1.1; INSP-100);
# validate_docs.py enforces the 07 section 2.1.1 dispatch and the zero-open-Major rule on every record, and
# complexity_gate.py enforces SWE-220, which is why the safety-designated tasks below are applied, not relieved
criticality: neither
product_size: "5 TV records (26 purposes, 5 new runs), 1 CR file, 7 changed tool or source files, 285 known-answer tests in the re-run selections, 8 fixture files, 6 evidence files, 7 renders"
sprint: PDR-prep
author_agent: "author:WP-PDR-09 (Claude as tool owner and software lead, CR-014)"
reviewer_agent: "sa-reviewer:WP-PDR-09-tv-003-tv-007-tv-010-tv-012"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-09-tv-003-tv-007-tv-010-tv-012 (software assurance function; paired file review INSP-100 by reviewer:WP-PDR-09-tv-and-code)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major; two Minor findings, liens due the CDR
# readiness declaration under PDR work plan rule C1 unless fixed on the CR-014 branch before the merge)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES under the lead SE convention of
# 2026-09-27 (INSP-031 practice): 38 reviewed blobs exist only on the unmerged branch cr/CR-014-tool-liens-srr, and
# the checklist applied only on cr/CR-012-pdr-checklist-templates; INSP-100 does not yet name this record
# (paired_record, assurance_verdict; each reviewer updates only its own record, cross item X-1). The software lead
# sets verdict APPROVED on both records in the CR-014 merge commit (or the commit right after it) when the blobs
# reach main unchanged; a blob change before then needs a delta iteration of both records (rule C2)
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 2
findings_open: 2
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 2
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2", "swe-135 7.1 task 1", "swe-135 7.1 task 6", "swe-186 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 1", "swe-081 7.1 task 2", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-090 7.1 task 1", "swe-040 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
items_no: ["swe-136 7.1 task 1"]
effort_turns: 40
effort_minutes: 75
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-101: software assurance pair of INSP-100, the CR-014 re-validations TV-003 run 7, TV-007 run 4, TV-010 run 5, TV-012 run 4 and TV-013 run 4 (WP-PDR-09, iteration 1)

**Product.** The INSP-100 product: the CR-014 branch `cr/CR-014-tool-liens-srr` at head `367b3dd` and the CR-014 file on `main` (`eb200de`, blob `139d860d`, unchanged at `main` `3837edb`). All 43 `product_files` entries and the six trees were checked with `git rev-parse 367b3dd:<path>` (CR file `main:<path>`): all equal to INSP-100. The branch head has not moved since INSP-100 was filed. 38 of the 43 blobs exist only on the branch.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; CR-012 is still Submitted, not merged). Sections R, A, B, D, E and F are applied. Section C (SWE-134 a to l) is N/A for criticality neither. `product_type` tool-validation has no 07 section 2.1.1 row (INSP-048 finding-1, cited, not raised again); the pair is dispatched by plan WP-PDR-09 ("SA for credit tools") and CR-014 section 5 step 5.

**Acceptance criteria (rule C7).** Every task of the section B row "Every product type"; swe-136 task 1 and swe-070 task 1 for each of the five TV records; the section 7.1 tasks of the SWEs the changed tools enforce (front matter list). Each INSP-100 finding and observation was re-read under the assurance lens. Each assurance-relevant behaviour the branch changes was confirmed to have a known answer that discriminates it:
- the 07 section 2.1.1 dispatch constants of `validate_docs.py` (05 and TS-002 as whole products; `SW-SYNTH` class);
- the record state rule (zero open Major, SWE-088 b and c);
- the CC count of `complexity_gate.py` (SWE-220);
- the G0 rustos identity of `sw_gate.sh` (SWE-081);
- the result lines of `measurements.py` (gate log integrity).

**Independence (rule C4).** This invocation authored no part of WP-PDR-09, CR-014, the TV records, the tools, the evidence or the renders. It did not write INSP-100 and edited no product file. It is neither `author:WP-PDR-09` nor `reviewer:WP-PDR-09-tv-and-code`. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: "software assurance pair record for tool validation review, assurance_verdict, software-assurance.md"; "parse measurements.py output lines PASS FAIL in sw_gate.sh log or TC-SW-TOOL-001 report"; "SWEHB 7.1 Tasking for Software Assurance cyclomatic complexity safety-critical SWE-220 tool accreditation SWE-136". `grep -n` and read-only scripts were used afterwards only to pin lines and to extract the SWEHB section 7.1 lists. The rustos working tree was not read: rustos content came only from `git -C /Users/robinonsay/rust/rustos archive 2ec64c0`, `rev-parse 2ec64c0^{tree}` and `--no-checkout` clones of its object store in the scratch directory. LTspice was not run: no full-suite `unittest discover` was run, only the named TV selections (INSP-100 X-4). No download, install or push.

**Lead SE convention.** The reviewed blobs exist only on the unmerged branch. This record sets `reviewer_verdict` and `assurance_verdict` on its own, holds `verdict`, and is committed on `main`. The software lead sets `verdict` in the CR-014 merge commit or the commit right after it.

## Assurance re-runs and checks

| # | Check | Result |
|---|---|---|
| S0 | `git archive 367b3dd` export in the scratch directory; identity of the 43 `product_files` and six trees against INSP-100 | all equal; `git hash-object` of `tools/validate_docs.py` in the export `e5b692e1` |
| S1 | TV section 3 selections on the export as it comes from `git archive`: no `tools/slides/node_modules` (gitignored, `.gitignore:28`), so no Source Sans Pro | `test_validate_docs.py` TV-003 selection 40 OK; `test_tools.py` 117 OK; `test_review_trend.py` 25 OK; `test_complexity_gate.py` 28 OK; `test_measurements.py` 20 OK. `test_render_review_figures.py` TV-010 selection: 55 run, **1 failure, 1 error, 1 skipped** (finding-2) |
| S2 | The same TV-010 selection with the fonts linked, as the author's procedure does (`evidence/wp-pdr-09-2026-09-27.py` lines 85 to 87); INSP-100 V1 | 55 OK, 0 skipped (INSP-100 V1, the author's log); the three S1 cases pass only with Source Sans Pro |
| S3 | Five mutants of the 07 section 2.1.1 dispatch and record-state code of `validate_docs.py` in a copy of the export: M1 05 removed from `ASSURANCE_WHOLE_PRODUCTS`; M2 TS-002 removed; M3 `SW-SYNTH` back to `MISSION_CRITICAL_MODULES`; M4 `SW-SYNTH` removed from both tuples (its products would lose the assurance reason); M5 `finding_key` returns the id unchanged | all killed by the TV-003 selection: M1 to M4 1 failure each (`SrrToolLienTests`), M5 3 failures; `test_tools.py` OK in each; copy restored and re-hashed `e5b692e1` |
| S4 | `finding_key` against every record body on `main`: records whose finding tables hold both an `F-<k>` and a `finding-<k>` id, and whether the two name the same finding | five SRR records (INSP-002 `conops-and-concept.md`, `fw-b0-tests-test-author.md`, `icd-stubs-external.md`, `risk-register-06.md`, INSP-010 `software-plan-07.md`); in each, `F-<k>` and `finding-<k>` are the same finding of that record (dual-labelled rows or a later restatement). Open Major set old and new: equal except INSP-010 `F-21`, which the new rule reads as superseded by its later `finding-21` rows, as CR-014 section 1 states |
| S5 | Probe of `approval_errors` on one body under blobs `3aa03681` (accredited, `main`) and `e5b692e1` (branch). The body has `## Findings` with own `finding-2`, Major, Open, then a later finding table that verifies another record's lien in a row whose id cell is `F-02 (INSP-015)`, Minor, Verified | `3aa03681`: fails, "finding-2 is a Major finding in state Open". `e5b692e1`: **passes** with no error (finding-1) |
| S6 | 07 section 2.1.1 plans row and section 14.1 against the constants. SRR decision memo decision 9. 07 on `main` (line 598 and line 863 "Tool constants") and on `cr/CR-010-apply-srr-decisions-9-and-40` (lines 583, 642, 863) | the plans row names 07, the V&V plan software section, 03, 05 and TS-002: all five now in `ASSURANCE_WHOLE_PRODUCTS`. Decision 9 concurred with frequency control safety-critical; the CR-010 text removes "Proposed" and keeps the `SW-SYNTH` units outside the word path mission-critical. The module-level `SW-SYNTH` class of the tool is the conservative reading (07 line 863: "only the reported class changes"). The safety-critical menu override command path (decision 9) has no module yet (WP-PDR-32); its interim home `SW-DISPLAY` (07 line 605) is in `MISSION_CRITICAL_MODULES`, so its products still get the assurance reason. No dispatch gap |
| S7 | Gate row of TV-012 run 4: `rust-code-analysis-cli` 0.0.25 on the export (`firmware`) and the rustos export of `2ec64c0` (`api`, `firmware/pico2`), piped to `tools/complexity_gate.py --max 15` at `e9cfd465` | `MSR-17 functions 52, max_cc 5, mean_cc 1.46, above_12 0, above_15 0`; `main.rs:30 main CC 4 = analyzer 2 + 2 let ... else`; `complexity_gate: PASS`, equal to `evidence/complexity-gate-2026-09-27-r4.log.txt` |
| S8 | G0 evidence procedure `sw-gate-g0-export-2026-09-27.sh` with the head `sw_gate.sh` and lock, fresh layouts (export, seeded, outer/export, clone at `2ec64c0`, clone at `c54d35a`); `git -C rustos rev-parse 2ec64c0^{tree}` | `39d8d8a9d54c7e3dc1b5b675a7dffe7cc743612d`, the lock's "tree of the pin"; 5 of 5 MATCH, `# result 0` |
| S9 | Two further G0 export probes (the G0 block extracted as the procedure does): the export plus a new file `NEWFILE.txt` and a build file under `target/`; then the export plus the `target/` file only | first: FAIL, "G0 rustos export tree differs" (tree `7b9d2eed`); second: PASS (`target/` is in the export's own `.gitignore`, as `git status` ignores it in clone mode). Fail-safe on any tracked-path change |
| S10 | Commit route: `git log 7bb994f..367b3dd` trailers of the eight CR-014 product commits and the merge; the CR file commit on `main` | `16cdd3e`, `067966c`, `012d53c`, `fcb9ba7`, `e024b24`, `dacc6e9`, `f924595` (with `CR: CR-001`), `7b4e3b4` and the merge `367b3dd` each carry `CR: CR-014`; `eb200de` carries `Refs: CR-014`. The other commits in the range are `main` commits brought in by the merge |
| S11 | Consumers of `measurements.py` result lines (search, then `grep -n`): does any tool parse a line that begins `PASS` or `FAIL` from its output | none; `sw_gate.sh` uses the exit status, and the prefix keeps the gate step count clean (C-185) |
| S12 | Render `evidence/wp-pdr-09-renders/risk-matrix.png` opened (visual closure) for the safety override | RSK-034 drawn in the Yellow (2, 5) cell with an asterisk and the red "* safety override" note; legend "Red 32 (1 by safety override)"; footer states the 06 section 7 rule. Counts as INSP-100 states |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-136 7.1 task 1, swe-080 7.1 task 1 | `tools/validate_docs.py` `finding_key` and `finding_rows` (blob `e5b692e1`); TV-003 purpose 7 amendment (blob `3eb258f1` line 45) and limitation 7 (line 104) | The C-173 fix treats `F-<nn>` and `finding-<n>` as one finding wherever they stand, so it assumes that every id cell of every finding table in a record names that record's own findings. Nothing states or checks that. A lien-verification table that cites another record's id in its first cell (`F-02 (INSP-015)`) now supersedes the record's own `finding-2`. In S5, an own Major Open `finding-2` followed by such a row, Verified, passes rule (c) at `e5b692e1` and fails at the accredited `3aa03681`. This is the first change of the record state rule that can turn a fail into a pass. The rule is the automated form of SWE-088 b and c (zero open Major before APPROVED) and gates every record verdict. No record on `main` has this form today (S4: every `F-<k>` and `finding-<k>` pair names one finding), so no result is wrong. But ACC-VALDOCS-001 as proposed would accredit purpose 7 without the condition it depends on, and CR-014 section 4 (Safety, Verification) reports only the conservative effect of the widened read. INSP-100 finding-1 is the reverse gap (a table not read); this one is a table read under another record's key. Fix: apply `finding_key` only to ids in the record's own form (an `F-<nn>` or `finding-<n>` cell with no other record id in it), and add a known answer for the S5 body; or state in TV-003 purpose 7 and limitation 7 that a finding table's id cell names only the record's own findings, and send that rule to the 01 section 13 and template writers as a cross item | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | swe-136 7.1 task 1, swe-070 7.1 task 1 | TV-010 (blob `31d328fb`) section 1 "Runtime" (line 26: "else DejaVu Sans with a printed notice") and section 3 note (line 45: only `test_srr_layout_reproduces_the_srr_render` "is skipped without it"); `tools/tests/test_render_review_figures.py` `FoldedFigureTests.test_concept_slide_layout_meets_the_floor`, `RunTests.test_render_every_figure_at_its_slide_size` | Without `tools/slides/node_modules` (gitignored, outside git; the reveal.js 5.2.1 font folder), the TV-010 selection on an export of `367b3dd` gives 1 failure, 1 error and 1 skip, not 1 skip (S1). The layout checks refuse the `CONCEPT_LAYOUT_SLIDE` figure with DejaVu Sans: 11 blocks' text does not fit, labels overlap blocks and edges, and the CTL title is clipped. So `render_review_figures.py` exits 1 and writes nothing for the default figure set. The tool fails safe: no wrong figure is drawn. But purpose 3 and the ACC-FIGS-001 extension hold only with the font files present, and TV-010 identifies them only by package version: no file hash in section 1, no mention in the extension. A run for the record needs them, as the author's procedure provides. Section 1 and section 3 describe the fallback as working, and a reviewer or deck agent in a fresh clone or export meets an unexplained failure. SWE-136 accreditation is read from the TV record, so the record should state what the known answers depend on. Fix: state in TV-010 section 3 and a limitation that the folded slide layouts pass only with Source Sans Pro, and that without it the concept figure exits 1 (the two tests named); record the SHA-256 of the three `source-sans-pro-*.ttf` files in section 1; name the font identity in the ACC-FIGS-001 extension | Open | Pending | |

**Paired record findings under the assurance lens (not raised again; template finding rules).**
- INSP-100 finding-1 (exact "Findings" heading): concur at Minor. Under the assurance lens its reverse case matters most: an open Major in a "## Findings (iteration 1)" table before a higher iteration heading, not restated later, still passes rule (c). That is the pre-CR-014 gap left open for the heading form the project uses, not a regression, and no record has it today (INSP-100 V9, V10). The severity does not rise. finding-1 here is a different defect: a new false-pass path that the change adds.
- INSP-100 finding-2 (TV-010 purpose 3 unseeded clauses): concur at Minor. The unseeded checks guard legibility, not a safety conclusion, and the tool fails closed. finding-2 here is a separate gap in the same record: the dependency of the seeded checks on untracked font files.
- INSP-100 finding-3 (TV number under 05 section 9.2 steps 4 and 5): concur at Minor. It is an owner ruling shared with INSP-043 finding-2, and it does not change which blob is accredited or when.
- INSP-100 observations 1 to 4 and cross items X-1 to X-5: concur. On X-4, this review ran only the named selections, never the full suite (Independence paragraph).

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the review of tools that gate safety-critical evidence: the assurance dispatch and the zero-open-Major rule of every record (`validate_docs.py`), SWE-220 (`complexity_gate.py`) and the rustos pin identity (`sw_gate.sh` G0). Dispatched by plan WP-PDR-09 and CR-014 section 5 step 5 (07 section 2.1.1 gap: INSP-048 finding-1) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against 07 section 15 by this record; the NASA-STD-8739.8 part is relieved (`rmm.json` SWE-022 T) | | none |
| swe-136 7.1 task 1 | | No | The five changed blobs are validated (runs 7, 4, 5, 4, 4; re-run S1, S2, INSP-100 V1) and reviewed (INSP-100, this record). They are not yet accredited: each TV record keeps the accredited blob on `main` in force until the merge and the owner's decision (TV-003 line 131). Two proposed scopes cover more than the records state: purpose 7 without its id-namespace condition, and purpose 3 without its font dependency | | finding-1, finding-2 |
| swe-070 7.1 task 1 | | Yes | Qualification-relevant outputs: MSR-17 and gate G5 (`complexity_gate.py`), gates G2, G3, G6 (`measurements.py`), G0 (`sw_gate.sh`, no TV record, due CDR, lock section 5). Each proposed extension names its blob, commit, interpreter and imported blobs (ACC-TREND-001 names `validate_docs.py` `e5b692e1`). `render_review_figures.py` output is review evidence, not qualification; its font dependency is finding-2 | | finding-2 |
| swe-220 7.1 task 1 | SC | Yes | CC metrics re-run on the current code with the changed tool (S7): 52 functions, max 5. The let-else count after a type's closing `>` is discriminated by the TV-012 selection (28 OK; fails on `ddf10798`, INSP-100 V1). The `..=` pattern mis-split that INSP-100 CK-CODE-E1 notes still counts the site (the +2 is kept), so CC is not under-counted | | none |
| swe-220 7.1 task 2 | SC | Yes | No function above 15 (`above_15 0`); no safety-critical application component has code yet (07 section 3.1: FW-B0 holds no application module), so no waiver is needed (07 section 14.3) | | none |
| swe-135 7.1 task 1 | | Yes | The complexity part of the static analysis gate G5 re-run (S7); the other G5 tools are not changed by CR-014 | | none |
| swe-135 7.1 task 6 | SC | Yes | As swe-220 task 2 | | none |
| swe-186 7.1 task 1 | | Yes | `--diff-runs` keeps its three clauses (TV-013 run 4, 20 OK, S1); only the result-line prefix changed, and no consumer parses those lines (S11) | | none |
| swe-080 7.1 task 1 | SC | Yes | CR-014 impact analysed. The Safety row is correct for hazards and controls. The dispatch outcome is unchanged: both classes need the assurance review, and the 05, TS-002 and `SW-SYNTH` constants are each discriminated (S3 M1 to M4). The widened record-state read is conservative except for one new false-pass path that section 4 does not report | | finding-1 |
| swe-080 7.1 task 2 | | Yes | a: CR-014 on `main` (`eb200de`), Submitted; b: the class-CR tools changed only on the branch, not merged before disposition (05 Table 4-1 row 28); c: steps 1 to 3 done with SHAs; d: runs 7, 4, 5, 4, 4, G0 evidence, and two reviews (INSP-100, this record) | | none |
| swe-080 7.1 task 3 | | Yes | S10: every CR-014 product commit and the merge carry `CR: CR-014` | | none |
| swe-081 7.1 task 1 | | Yes | Each changed file identified by blob and SHA-256 in its TV record; the rustos pin by commit and, new, by "tree of the pin" `39d8d8a9` (S8) | | none |
| swe-081 7.1 task 2 | SC | Yes | The safety-critical module list the tool enforces is a class-CR constant, changed only under CR-014, and equals the owner's decision 9 determination (S6). No hazard data changed. G0 export mode fails on any change to a tracked rustos path (S9) | | none |
| swe-087 7.1 task 1 | | Yes | INSP-100 performed and recorded (code and TV items); this record completes the WP-PDR-09 assurance review | | none |
| swe-087 7.1 task 2 | | Yes | The SRR liens C-172, C-173, C-186, C-170, C-072, C-203, C-204, C-175, C-185, C-179 and C-178 are implemented (INSP-100 CK-CODE-E1, concur). Their verification against the SRR records is the INSP-015 and INSP-016 delta iterations (CR-014 step 6), still pending | | none |
| swe-088 7.1 task 1 | | Yes | INSP-100: TV template item set through the code checklist field, readiness R1 to R5, findings with state, participants named (SWE-088 a to d) | | none |
| swe-088 7.1 task 2 | | Yes | INSP-100 findings are liens with a due event (rule C1). This record asks for no new action outside its findings (cross items) | | none |
| swe-089 7.1 task 1 | | Yes | INSP-100 and this record carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes`, `iteration` | | none |
| swe-090 7.1 task 1 | | Yes | MSR-17 line format unchanged (S7); the `measurements.py` prefix change keeps the gate log count of step results exact | | none |
| swe-040 7.1 task 1 | | Yes | Tools, tests, fixtures, TV records, evidence and renders are repository files (branch, then `main`); the fonts of finding-2 are the exception (npm, gitignored) | | none |
| swe-219 7.1 task 1 | SC | N/A | No safety-critical component has code yet; `--coverage` mode unchanged except the line prefix | 07 section 3.1 (FW-B0 holds no application module) and section 9.6 (the SWE-219 record starts with the first safety-critical module) | none |
| swe-135 7.1 task 5 | SC | N/A | As swe-219 task 1 | 07 sections 3.1 and 9.6 | none |
| swe-087 7.1 task 4 | SC | N/A | `main.rs` changed in a comment only (INSP-100 V7); no safety-critical source code in the product | 07 section 3.1 | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | S0: 43 of 43 blobs and six of six trees equal to INSP-100; branch head `367b3dd` unchanged |
| R2 | 07 section 2.1.1 row and criticality identified | Yes, with the known gap | No 07 section 2.1.1 row for TV records (INSP-048 finding-1); criticality neither (03 sections 4.3.1 and 6.1.1); dispatched by plan WP-PDR-09 |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` no violation for the ids touched | Yes | The product touches no requirement, case or hazard id; INSP-100 V12: 0 violations, 2 warnings, as `main`. On `main` `3837edb`, `validate_docs.py` reports 94 passed, 8 failed before this record, all records of other work packages (record drift and schema failures listed in the Commands table); on the branch INSP-100 V8 adds only the INSP-016 drift CR-014 foresees. S1 and S2 known answers pass (the S1 font case is finding-2) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-100 committed on `main` (`3837edb`), `author_agent` "author:WP-PDR-09", `reviewer_agent` "reviewer:WP-PDR-09-tv-and-code"; this invocation is `sa-reviewer:WP-PDR-09-tv-003-tv-007-tv-010-tv-012` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with the known gap | Dispatched by plan WP-PDR-09 ("SA for credit tools"), CR-014 section 5 step 5 and INSP-100 X-1. 07 section 2.1.1 has no TV row and the TV template says `assurance_required: false`. The inconsistency is INSP-048 finding-1, cited and not raised again |
| SA-A2 | Yes | Three invocations: author `author:WP-PDR-09`, file reviewer `reviewer:WP-PDR-09-tv-and-code`, this assurance reviewer. INSP-100 names this record's path but not yet its id (X-1) |
| SA-A3 | Yes | Same product, same `product_commit` `367b3dd`, same 43 blobs and six trees (S0) |
| SA-A4 | Yes | INSP-100 applied the TV template item set (R, A to F, G1, H; G2 to G4 N/A) with the code checklist for TV-G1-3, every item answered with evidence, and the rule C7 case list of CR-014 section 5 |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table covers: the "Every product type" row; the swe-136 and swe-070 tool tasks; the section 7.1 tasks of SWE-220, 135, 186, 219, 080, 081, 087, 088, 089, 090 and 040. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows cite 07 sections 3.1 and 9.6. The product is of criticality neither. Each SC task answered N/A (swe-219 task 1, swe-135 task 5, swe-087 task 4) concerns safety-critical code, which does not exist yet |
| SA-B3 | Yes | swe-136 task 1 (No) carries finding-1 and finding-2 |

## C. SWE-134 items a to l

N/A for every item: `criticality` neither (07 section 14.1 lists no tool component), so `swe134_items_checked` is empty.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | N/A | The product changes no hazard and adds no software contribution (CR-014 section 4 Safety row) |
| SA-D2 | Yes, for the tool constants | No component is created or renamed. The component classes the tool enforces equal 07 section 14.1 as ruled at SRR decision 9 (S6). The menu override command path module joins at WP-PDR-32; until then its products keep an assurance reason through `SW-DISPLAY` |
| SA-D3 | N/A | No requirement or hazard id touched; traceability unchanged (INSP-100 V12) |
| SA-D4 | N/A | No safety-tagged software requirement changes |
| SA-D5 | N/A | No hazard-tracing software requirement changes |
| SA-D6 | N/A | The hazard analysis is not re-issued by this product |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | The SRR liens this change closes are implemented as their source findings ask (INSP-100 CK-CODE-E1, concur). None is marked closed yet: the verification is the INSP-015 and INSP-016 delta iterations and the INSP-041 delta (CR-014 steps 6 and 7), not this record |
| SA-E2 | Yes | INSP-100 and this record carry the SWE-089 fields (07 section 10.3) |
| SA-E3 | Yes | S10; the four accredited tools are class-CR items (05 Table 4-1 row 28) changed only on the CR branch before disposition; the Log-class items ride on the branch for the record drift reason CR-014 states |
| SA-E4 | N/A | No item under test and no credit run in this product |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the product needs a risk entry. The dispatch gap is INSP-048 finding-1; the full-suite LTspice exposure is INSP-100 X-4; the pairing is X-1 below |
| SA-F2 | Yes | Front matter carries `findings_*`, `assurance_findings_major` 0, `assurance_findings_minor` 2 (the same findings, counted once, 07 section 10.2), `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true. Every task SA-B1 requires is in the task table. Every applicable item of sections A, D, E and F is answered, and section C is N/A with its reason. There are zero Major findings. The two Minor findings are open. Under PDR work plan rule C1 and 08 section 3.2 ("Minor findings ride with APPROVED"), as INSP-100 applies them, they are written for the tool owner to fix on the CR-014 branch before the merge. A finding not fixed then is a lien due at the CDR readiness declaration, listed in PDR package section 15. A fix before the merge changes blobs of `product_files` and needs a delta iteration of both records (rule C2).

`assurance_verdict: APPROVED`. With INSP-100 `reviewer_verdict: APPROVED`, both reviews of the product are APPROVED. The record `verdict` stays NEEDS CHANGES under the lead SE convention: the reviewed blobs are on the unmerged CR-014 branch, and the software lead sets APPROVED at the merge.

## Cross items (returned to Claude)

- **X-1.** INSP-100 (`tool-validation-tv-003-tv-007-tv-010-tv-012.md`) reads `assurance_verdict: pending` and has no `paired_record`. Its reviewer updates it: `paired_record: INSP-101`, `assurance_reviewer_agent` naming this invocation, and `assurance_verdict: APPROVED` copied from here (07 section 10.2 Record row). TV-003, TV-007, TV-010 and TV-012 section 8 then list both records.
- **X-2.** Dispatch of the SA review for TV records: INSP-048 finding-1. No new item.
- **X-3.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `assurance_checklist`.
- **X-4.** TV-013 run 4 (blob `cec467f1`) is in this product only as a revalidation row. Its assurance review is the INSP-049 delta that follows the INSP-041 delta (CR-014 step 7); this record does not replace it.
- **X-5.** finding-1 has a process side: 01 section 13 and the checklist templates' finding rules say ids are `finding-<n>` numbered in the record, but they do not forbid another record's id in the first cell of a finding table. If the fix takes the documentation route, the 01 writer and the CR-012 template writer add that sentence.
- **X-6.** 07 section 22 "Tool constants" row: on `main` it reads "if the SRR decision memo records concurrence", and on the CR-010 branch "PDR (tool liens, after CR-010 is merged)". CR-014 moves `SW-SYNTH` before CR-010 merges. The memo already records the concurrence, so the tool is right. The CR-010 row wording should not be read as a sequencing condition at the CR-014 merge; the CR-010 writer may note CR-014 there.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse 367b3dd:<path>` for the 42 branch `product_files` and six trees; `git rev-parse main:docs/cm/cr/CR-014-tool-liens-srr.md` | 0 | 43 of 43 and 6 of 6 equal to INSP-100 (S0) |
| `git rev-parse cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md`; `git show` of that path | 0 | Template revision A, blob `5b135285` |
| `git archive 367b3dd` into the scratchpad; the TV section 3 selections with `.venv/bin/python -m unittest discover -s tools/tests -p <module> [-k ...]` | 0, 0, 0, 1, 0, 0 | S1: 40, 117, 25, 55 (1 failure, 1 error, 1 skipped without fonts), 28, 20 |
| Five text-substitution mutants of `validate_docs.py` in a copy of the export, TV-003 selection and `test_tools.py` each; copy restored | 1 each; 0 each | S3 |
| Scratch script over `docs/reviews/*/checklists/*.md` with `finding_rows` and `current_findings` under the identity key and `finding_key` | 0 | S4 |
| Scratch probe of `approval_errors` with the blob `3aa03681` (`git show 7bb994f:tools/validate_docs.py`) and the export's `e5b692e1` | 0 | S5 |
| `rust-code-analysis-cli --metrics --output-format json --paths firmware --paths <rustos export>/api --paths <rustos export>/firmware/pico2 \| tools/complexity_gate.py --max 15` | 0 | S7 |
| `sh docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.sh tools/sw_gate.sh tools/toolchain.lock.md <D>` and two extra probes | 0; 1, 0 | S8, S9 |
| `git log 7bb994f..367b3dd` trailers; `git log -1 eb200de` | 0 | S10 |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-136, 070, 220, 135, 080, 081, 205, 186, 040, 090, 087, 088, 089, 219, 134, 022; SC marks from the template section B rows | 0 | Task texts of the task table |
| `.venv/bin/python tools/validate_docs.py` on `main` | 1 | Before this record 94 passed, 8 failed: `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md` (PDR); `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md` (SRR); this record PASS |

## Verdict format

```
ASSURANCE VERDICT: APPROVED
PRODUCT: TV-003@3eb258f1, TV-007@1ecc089a, TV-010@31d328fb, TV-012@87bc6e25, TV-013@91101cf7 and the 38 other INSP-100 product_files at 367b3dd (CR file 139d860d on main); PAIRED RECORD: INSP-100
PRODUCT TYPE: tool-validation (no 07 section 2.1.1 row; INSP-048 finding-1); CRITICALITY: neither
FINDINGS:
- [Minor] swe-136 7.1 task 1, swe-080 7.1 task 1: finding_key merges another record's F-nn cited in a finding table with the record's own finding-n; an own open Major then passes rule (c) at e5b692e1 (fails at 3aa03681); condition not stated in TV-003 purpose 7 or limitation 7.
- [Minor] swe-136 7.1 task 1, swe-070 7.1 task 1: TV-010 known answers need the untracked Source Sans Pro files; without them 1 failure, 1 error, 1 skip and the concept figure exits 1; TV-010 says only one test is skipped and names no font hash.
TASKS APPLIED: swe-134 task 5, swe-022 task 1, swe-136 task 1, swe-070 task 1, swe-220 tasks 1 and 2, swe-135 tasks 1 and 6, swe-186 task 1, swe-080 tasks 1 to 3, swe-081 tasks 1 and 2, swe-087 tasks 1 and 2, swe-088 tasks 1 and 2, swe-089 task 1, swe-090 task 1, swe-040 task 1
TASKS N/A (relief): swe-219 task 1, swe-135 task 5, swe-087 task 4 (07 sections 3.1 and 9.6)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=5 TV records, 26 purposes, 285 tests; tasks=24; tasks_no=1; mutants=5 (5 killed); probes=3; turns=40; minutes=75; major=0; minor=2
```
