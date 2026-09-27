---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the tool validation review INSP-043
# (docs/reviews/PDR/checklists/tool-validation-tv-002.md, iteration 2 by reviewer:WP-PDR-06-code-and-tv), which
# asked for it as "SA pair needed"; PDR work plan WP-PDR-06 names the SA second review ("tool used for credit").
# Record path: 07 section 10.2 Record row, <product-slug>-software-assurance.md with the slug of INSP-043. INSP-043
# and TV-002 section 8 name code-tools-traceability-software-assurance.md, which by the same rule is the pair of
# the code record INSP-042 (a different product); cross item X-1.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged).
# The `checklist` field names peer-review-checklist-code revision B, the checklist INSP-043 names, because
# tools/validate_docs.py fails a record whose `checklist` names a template absent from main, and the lead SE
# convention of 2026-09-27 does not change the validator. `assurance_checklist` names the template actually
# applied (the form of INSP-048 and INSP-049).
id: INSP-051
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-002-software-assurance.md
product: docs/cm/tool-validation/TV-002-traceability.md
# product_commit and product_files: equal to INSP-043 iteration 2 (readiness R1; rule C2). Twelve blobs exist only
# on the CR-011 branch (git rev-parse 2b004b1:<path>, checked 2026-09-27); the CR file is on main, where it has
# since moved from d597899b to 892670b6 (CR-011 revision 2, 7bb994f; cross item X-4)
product_commit: "2b004b17bf94ecf3dc3591cbc34892e6620ad8a7"
product_files: ["docs/cm/tool-validation/TV-002-traceability.md@94ae3af57e6d5527ccd5ff76ab7aa8724fb0b395", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.py@e6f3785628ee376a921a1176883f475c086ab656", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.log.txt@1e30bb222b51ecdf3800f6bb5c4a243ce94f0ef3", "tools/tests/test_traceability.py@6ead56414127f9c13cd39e3662a2118e2acd470e", "tools/traceability.py@d4cde9f54386373017f21825d4fd7cc0a42ac373", "tools/tests/test_tools.py@f8289a443f6ca2d837ab2df07df5a3dfc0722f27", "tools/README.md@d61156d8966178e958df4539adab60e8c0ff8b0d", "docs/process/02-requirements-and-traceability.md@d4934d0e7c9648c13ea7d50c1b28faba45b86c00", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py@220ae2e0118fe13e8237b628d6192a0c67e3c44e", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt@e26b24368088c56bf18c920b34a12e5dfdd1966a", "docs/vv/traceability-report.md@f49f4215b34179caca551dcfd9a348fdf17c288e", "docs/vv/traceability.json@0f0ea6ef18bdcabd3cba6ef9d6853296de6c476f", "docs/cm/cr/CR-011-traceability-pdr-rules.md@d597899b9f442bfc9c3983cb28f15998eb78c197"]
fixture_trees: ["tools/tests/fixtures/valid_project@bcd898307e93113336cf9b1045d7a8ce827f42cc", "tools/tests/fixtures/invalid_project@6a046bae3fe2a86c2e4b00a41954f1946b5e3b1f"]
# inputs read (not reviewed), blobs at main 0baa7a4 unless stated
input_files: ["docs/reviews/PDR/checklists/tool-validation-tv-002.md (INSP-043 iteration 2)", "docs/reviews/PDR/checklists/code-tools-traceability.md (INSP-042)", "docs/reviews/PDR/checklists/tool-validation-rust-toolchain-software-assurance.md (INSP-048 finding-1)", "docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md (INSP-015 re-issue 3, 26011f1)", "docs/process/04-verification-and-validation.md@0b197bba692237ed9860ba49c4422f12fa8512dc (equal at 2b004b1)", "docs/process/07-software-engineering-plan.md", "docs/process/rmm.json@e326ddd1b7296d7d7fe172be6f33535cee3192d7", "docs/plan/pdr-work-plan.md", "docs/cm/cr/CR-011-traceability-pdr-rules.md@892670b609f4bbd1d4c0c12de8a75f7890e2bf69 (revision 2, diff only)"]
paired_record: INSP-043
tv_ids: [TV-002]
# product_type: 07 section 2.1.1 has no row for tool validation records (the dispatch gap is INSP-048 finding-1,
# cited here, not raised again). Task set applied: the section B row "Every product type"; swe-136 task 1 and
# swe-070 task 1 (section B row trade-study-or-adr "when the decision selects a tool"; TV template section H); and
# the section 7.1 tasks of every SWE the product governs (TV-002 "Governs" row: SWE-136, SWE-070, SWE-052) or whose
# rmm.json row names the tool (SWE-040, SWE-052, SWE-054, SWE-066, SWE-071, SWE-192, SWE-194, SWE-200), plus
# SWE-191 for purpose 9 (04 section 10.5), SWE-080 and SWE-081 for purpose 7, SWE-090 for the MSR outputs, and
# the section E tasks (SWE-087, SWE-088, SWE-089) (07 section 15)
product_type: tool-validation
# criticality: a tool is neither safety-critical nor mission-critical (03 sections 4.3.1 and 6.1.1; INSP-042,
# INSP-043); its output routes safety-critical evidence (hazard trace, SWE-192, Bench carry-forward), which is why
# the safety-designated tasks below are applied, not relieved
criticality: neither
product_size: "1 TV record (226 lines, 9 purposes, 7 runs), 235 known-answer tests (86 + 32 + 117), 74 fixture files (42 + 32), 4 evidence files; tool 4156 lines"
sprint: PDR-prep
author_agent: "author:WP-PDR-06 (Claude as tool owner and software lead, CR-011)"
reviewer_agent: "sa-reviewer:WP-PDR-06-tv-002"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-06-tv-002 (software assurance function; paired file review INSP-043 by reviewer:WP-PDR-06-code-and-tv)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major; three Minor findings, liens due the
# CDR readiness declaration under PDR work plan rule C1 unless fixed on the CR-011 branch before the merge)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES under the lead SE convention of
# 2026-09-27 (INSP-031 practice): twelve reviewed blobs exist only on the unmerged branch
# cr/CR-011-traceability-pdr-rules, and the checklist applied only on cr/CR-012-pdr-checklist-templates. Both
# reviews of the product are APPROVED (INSP-043 reviewer_verdict APPROVED; this record). The software lead sets
# verdict APPROVED on both records in the CR-011 merge commit (or the commit right after it) when the blobs reach
# main unchanged and INSP-043 carries the pairing (X-1); a blob change before then needs a delta iteration of both
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 3
findings_open: 3
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 3
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-052 7.1 task 1", "swe-052 7.1 task 2", "swe-054 7.1 task 1", "swe-066 7.1 task 1", "swe-071 7.1 task 1", "swe-191 7.1 task 1", "swe-191 7.1 task 3", "swe-192 7.1 task 1", "swe-194 7.1 task 1", "swe-200 7.1 task 1", "swe-040 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 1", "swe-081 7.1 task 2", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-090 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
items_no: ["swe-052 7.1 task 2", "swe-191 7.1 task 3", SA-D3, SA-E1]
effort_turns: 45
effort_minutes: 80
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-051: software assurance pair of INSP-043, TV-002 runs 6 and 7 of `tools/traceability.py` blob `d4cde9f5` (WP-PDR-06, CR-011)

**Product.** `docs/cm/tool-validation/TV-002-traceability.md` blob `94ae3af5` at the CR-011 branch head `2b004b1`, with the tool, test modules, evidence and outputs of the paired record's `product_files` (twelve blobs on the branch, the CR-011 file on `main`). Identity checked with `git rev-parse 2b004b1:<path>` and `git hash-object` in an export (`git archive 2b004b1`): all thirteen blobs and both fixture trees equal INSP-043. The branch head has not moved since INSP-043 iteration 2.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Sections R, A, B, D, E and F are applied; section C (SWE-134 a to l) is N/A for criticality neither; section D is applied to the tool's hazard-trace and SWE-192 checks, since those are what the tool contributes to software safety analysis. `product_type` tool-validation (no 07 section 2.1.1 row; INSP-048 finding-1).

**Acceptance criteria (rule C7).** Every task of the section B row "Every product type"; swe-136 task 1 and swe-070 task 1; the section 7.1 tasks of every SWE the product governs or whose `rmm.json` row names the tool (list in the front matter); each INSP-043 finding (finding-1 Verified, finding-2 to finding-5 liens) and each INSP-042 finding re-read under the assurance lens; each safety-designated check the tool performs (hazard trace both ways, SWE-192 closing Test, on-target evidence at SAR, regression selection for Bench credit carry-forward) confirmed to have a known answer that discriminates it.

**Independence (rule C4).** This invocation authored no part of WP-PDR-06, CR-011, TV-002, the tool or its tests, wrote neither INSP-042 nor INSP-043, and edited no product file. It is neither `author:WP-PDR-06` nor `reviewer:WP-PDR-06-code-and-tv`. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-043 WP-PDR-06 CR-011 peer review record"; "software assurance second review of tool validation record tool used for credit SWE-136 product_type"; "SWEHB 7.1 Tasking for Software Assurance software tool accreditation validate models simulations"). `grep -n` and read-only scripts were used afterwards only to pin lines and to extract the SWEHB section 7.1 lists and the topic 8.10 section 6 designations.

**Lead SE convention.** The reviewed blobs exist only on the unmerged branch `cr/CR-011-traceability-pdr-rules`. This record sets `reviewer_verdict` and `assurance_verdict` on its own, holds `verdict`, and is committed on `main`; the software lead sets `verdict` in the CR-011 merge commit or the commit right after it.

## Assurance re-runs and checks

| # | Check | Result |
|---|---|---|
| S0 | Blob identities in an export of `2b004b1` (`git hash-object`) | `traceability.py` `d4cde9f5`, `test_traceability.py` `6ead5641`, `test_tools.py` `f8289a44`, `test_traceability_srr_rules.py` `86606485`, `validate_docs.py` `3aa03681`: equal to TV-002 "Identities for run 7" (lines 61 to 65) |
| S1 | TV-002 section 3, run 7 selection, in the export | three commands exit 0: 86, 32 and 117 tests, `OK`, none skipped (235), equal to run 7 (line 121) |
| S2 | Mutant M-A, hazard trace direction "requirement lists the hazard, the hazard's `requirement_ids` does not list the requirement" (`traceability.py:1748` to `:1750`) replaced by `pass`; every test of `test_traceability.py`, `test_traceability_srr_rules.py` and `test_tools.py` run | **survives**: `OK` on all three modules (finding-1) |
| S3 | The same direction checked by hand on the original blob: a copy of `valid_project` with `HZ-002` added to `REQ-SW-KEYER-001` `hazard_ids` (`HZ-002` `requirement_ids` is `[REQ-SYS-006]`) | plain run exit 0 with `HAZARD_INVERSE` warning at `REQ-SW-KEYER-001`; `--gate SRR` exit 1 with the same code as a violation; unmodified `valid_project` under `--gate SRR` exit 0. The code is correct today; only its known answer is missing |
| S4 | Mutants on the other hazard and SWE-192 branches: M-B `HAZARD_CONTROL_UNTRACED` disabled (`:1754`); M-C union check of `control_req_ids` disabled (`:1775`); M-D SW "no exception" branch of `HAZARD_REQ_NOT_TESTED` disabled (`:1809`); M-E "method Test without a closing Test case" disabled (`:1806`); M-F `HAZARD_REQ_NOT_ON_TARGET` disabled (`:1803`) | all killed: M-B 1 failure (`test_tools.py`), M-C 1, M-D 2 (`test_traceability.py`), M-E 1, M-F 2 (one in each module) |
| S5 | Export restored and re-hashed after the mutants | `traceability.py` `d4cde9f5` |
| S6 | `regression_set` and `design_ref_matches` (`traceability.py:3421` to `:3433`) against 04 section 10.5 (line 397) and section 5.2 row `T-SW-TARGET` (line 123), 04 blob `0b197bba` (equal on `main` and at `2b004b1`) | a path argument matches a `design_refs` entry only as equal path or on a `/` boundary; an element or ICD id matches only itself (finding-3) |
| S7 | Distinct `design_refs` of the software requirement files at `2b004b1` | every `REQ-SW-KEYER-*` carries `firmware/cwht-core/src/keyer/`; some add `rustos:firmware/pico2/src/timer.rs`, `ICD-CTL-SW` or `ICD-CTL-KEY`. No software requirement today is traced by element or ICD id alone |
| S8 | INSP-015 re-issue 3 (commit `26011f1`, an ancestor of the branch base `a3cacee`) against TV-002 sections 8 and 9 | re-issue 3 is APPROVED and makes the ACC-TRACE-001 extension to blob `12de3545` effective from 2026-09-26 (SRR record line 603); TV-002 at `94ae3af5` still reads it as pending (finding-2) |
| S9 | Commit route of the branch (`git log a3cacee..2b004b1`) and of the CR file on `main` | five branch commits, each with `CR: CR-011` and `Refs: CR-011, ...`; CR file commits `b01b9cd` and `7bb994f` on `main` with `Refs: CR-011` |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-052 7.1 task 2, SA-D3 | `tools/traceability.py:1748` to `:1750` (blob `d4cde9f5`); TV-002 section 2 purpose 1 (line 73, "hazard-control union") and section 3; `tools/tests/test_traceability.py`, `tools/tests/test_tools.py` | SWE-052 Table 1 row 2 is bidirectional, and the tool checks both directions. The direction "a requirement lists a hazard whose `requirement_ids` does not list it" (a `HAZARD_INVERSE` warning in a plain run, a violation under `--gate`, 02 T-08) has no known answer: with those three lines disabled (S2) all 235 known-answer tests and the rest of the three modules still pass. The other hazard branches are discriminated (S4). The code is correct at `d4cde9f5` (S3), so no output is wrong today; but ACC-TRACE-002 would accredit a check that no test holds, and a later edit that breaks it would pass the re-validation run that the TV-002 section 7 triggers require. TV-002 limitation 3 bounds known answers to one per rule, not one per branch, so it does not state this gap. Fix: add a known answer (a `SW-<SUB>` and a `SYS` requirement each listing a hazard that does not list it: warning in a plain run, violation under `--gate SRR`, exact code set), and add the direction to the step 3b mutant set; or state the gap as a limitation of purpose 1 | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | swe-136 7.1 task 1, SA-E1 | TV-002 blob `94ae3af5`: status line (line 6, "Independent review of this re-validation (INSP-015 delta) pending"), section 8 (line 213 "**pending**"; line 215 "The INSP-015 delta of run 5 may be folded into the tool-validation record"), section 9 row 3 (line 225, "Effective on the date the INSP-015 delta review of run 5 records APPROVED ... until then the output of blob `12de3545` is developer evidence"); `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` line 603 and cross item 1 (line 641) | INSP-015 re-issue 3 (`26011f1`, in the branch base) is the run 5 review of CM plan section 9.2 step 3, recorded APPROVED with liens, and it made the ACC-TRACE-001 extension to blob `12de3545` effective from 2026-09-26. Its cross item 1 asked the tool owner to record this in TV-002 section 8 and the status line. The run 6 and run 7 revisions of TV-002 did not carry it. So the accreditation record of the tool understates the accredited version on `main` (`12de3545`, the blob that writes every `main` traceability report until CR-011 merges), and section 8 proposes to fold into INSP-043 a review that is already done (INSP-043 did not fold it). No evidence was wrongly credited: the error is conservative. But SWE-136 accreditation status is read from the TV record (05 section 9.2 step 3), and the record disagrees with the review that governs it. Fix: in TV-002, record INSP-015 re-issue 3 (date, result, record commit `26011f1`) in section 8, mark the section 9 extension row effective 2026-09-26 with that citation, update the status line, and delete the fold-in sentence | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | swe-191 7.1 task 3 | TV-002 purpose 9 (line 89) and limitation 9 (line 197); `tools/traceability.py:3421` (`design_ref_matches`); 04 section 10.5 bullet "Firmware release on a delivered unit" (line 397) and section 5.2 row `T-SW-TARGET` (line 123) | For a firmware release installed on a delivered unit, 04 section 10.5 passes the changed files under `firmware/` as arguments, and 04 section 5.2 `T-SW-TARGET` lets a safety-relevant Bench credit carry forward when "the requirement's `design_refs` are untouched". The tool matches a path argument to a `design_refs` entry only as an equal path or on a `/` boundary, and an element id (`Bxx`) or ICD id matches only itself (purpose 9, S6). A `REQ-SW-*` traced by element or ICD ids alone, which 02 T-15 admits at PDR, is therefore never selected by a changed firmware file, and its Bench credit would carry forward unretested. Limitation 9 (b) states id-only matching for the rustos pin move only; neither (a) to (d) nor purpose 9 states the consequence for the firmware form. No case is affected today: every software requirement carries a `firmware/` path (S7). The PDR L2 software requirements (WP-PDR-35) and the Bench credits after TRR are where it would bite. Fix: add to limitation 9 that for the firmware form the caller also passes the element and ICD ids whose code paths contain a changed file (the `allocation.json` code map), or that the selection is valid only when every `REQ-SW-*` carries a `firmware/` path in `design_refs`; send the matching sentence to the 04 section 10.5 writer as a cross item | Open | Pending | |

**Paired and code record findings under the assurance lens (not raised again; template finding rules).**
- INSP-043 finding-1 (Major, Verified at iteration 2): concur. Purpose 9, `RegressionSetTests` and the step 3b mutants cover the `--regression` use. finding-3 here is a different defect: a limitation of the selection the tool prints, not a missing purpose.
- INSP-043 finding-2 (TV number): concur at Minor. It is an owner ruling on 05 section 9.2 steps 4 and 5 and does not change which blob is accredited.
- INSP-043 finding-3 (OS trigger): concur at Minor.
- INSP-043 finding-4 (run 6 time, lock and README rows lag): concur at Minor. Under swe-136 task 1 the lock is the summary a reader checks first, so it should be fixed before the merge, as the finding's due date allows. finding-2 here is the TV record's own lag, which finding-4 does not cover.
- INSP-043 finding-5 (purpose 8 schema claim; T-13 and T-12 limitations): concur at Minor. Under swe-200 task 1 an unchecked MSR-02 append could corrupt the measurement record that 07 section 11 reads. Under swe-080 task 3, T-13 accepting any later change to an id that an approved CR once listed (INSP-042 finding-1) weakens the automated change-control check. Peer review of each CR and the swe-082 audit remain as independent controls, so the severity does not rise.
- INSP-042 finding-6 (single-code assertions): concur at Minor. finding-1 here is the same kind of gap on a hazard branch; it is raised separately because it is a safety-designated task and because a mutant shows it, not just a code reading.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the review of a tool whose output feeds safety-critical evidence (hazard trace, SWE-192, SAR on-target rule, Bench carry-forward); dispatched by plan WP-PDR-06 (INSP-048 finding-1 for the 07 section 2.1.1 gap) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against 07 section 15 by this record; the NASA-STD-8739.8 part is relieved (`rmm.json` SWE-022 T) | | none |
| swe-136 7.1 task 1 | | Yes | Blob `d4cde9f5` is validated (runs 6 and 7, reproduced S0, S1), reviewed (INSP-042, INSP-043) and not yet accredited. TV-002 correctly holds its output as developer evidence until ACC-TRACE-002 (line 226; limitation 6). The ACC-TRACE-002 conditions name the three records and the merge. The record understates the accreditation of the predecessor blob on `main` | | finding-2 |
| swe-070 7.1 task 1 | | Yes | The tool's matrices and Inspection-class checks are qualification evidence (04 section 7.3; 01 section 3.1 item 2). The scope requested (purposes 1 to 9 at `d4cde9f5` with `validate_docs.py` `3aa03681`, TV-001 interpreter, TV-009 git) names every dependency the runs used | | none |
| swe-052 7.1 task 1 | | Yes | The tool records and checks Table 1 rows 1, 2, 5 and 6 and rows 3 and 4 in part (T-15 from PDR); limitation 2 names the rows it does not check and the manual checks that remain | | none |
| swe-052 7.1 task 2 | SC | No | Traceability to hazards is checked both ways (S3, S4), but one direction has no known answer (S2) | | finding-1 |
| swe-054 7.1 task 1 | | Yes | Differences are reported as findings with codes and locations (report section 2); `rmm.json` SWE-054 routes each to a RID, RFA or NCR; the tool itself tracks nothing to closure, which the RMM row does not claim | | none |
| swe-066 7.1 task 1 | | Yes | T-09 coverage (every Draft or Active requirement has a closing case of matching method) is purpose 1, with seeded faults in `invalid_project` | | none |
| swe-066 7.1 task 2 | SC | N/A | The product executes no test of flight software; witnessing is the owner's for Bench and OnAir runs | 07 section 2.1 (owner witnesses Bench and OnAir runs) | none |
| swe-066 7.1 task 3 | SC | N/A | No testing of flight software in this product, so no newly found software contribution to a hazard | 07 section 15 (software safety analysis is the hazard analysis) | none |
| swe-071 7.1 task 1 | SC | Yes | The tool flags stale cases (`CASE_STALE`, 04 rule 7.3.11, purpose 7; the `rmm.json` SWE-071 "stale-test flagging option", now implemented) and hazard requirements without a closing Test case (S4). The adequacy of off-nominal coverage is the test reviewer's, not the tool's | | none |
| swe-191 7.1 task 1 | SC | Yes | Safety-critical code is retested by the whole HostUnit and Emulation suite on every release (04 section 10.5 first bullet; 07 section 9.3), which does not depend on this tool. The tool's set is the Bench and ATP subset | | none |
| swe-191 7.1 task 2 | | N/A | No firmware release or unit exists; no regression run is due | 07 section 9.3 (regression runs per tagged release) | none |
| swe-191 7.1 task 3 | | No | Risk in the regression set selection: firmware-path arguments never select a requirement traced by element or ICD id alone | | finding-3 |
| swe-191 7.1 task 4 | | N/A | No critical anomaly has been corrected; no regression procedure exists yet | 04 section 10.5 (regression procedure set per NCR disposition) | none |
| swe-192 7.1 task 1 | SC | Yes | `HAZARD_REQ_NOT_TESTED` enforces a closing Test case for every hazard-tracing `SW` and `SW-<SUB>` requirement with no exception; the SW branch and the Test branch are each killed by a mutant (S4 M-D, M-E); the CR-002 Inspection route is closed to `SW` modules (`InspectionRouteTests`) | | none |
| swe-194 7.1 task 1 | | Yes | The tool gives the SAR entrance its checks (purpose 5: `HAZARD_REQ_NOT_ON_TARGET` for `Verified` at SAR, S4 M-F; `CLOSED_NOT_INSTALLED`, PCA-05); the delivery list itself is the SAR package's (`rmm.json` SWE-194) | | none |
| swe-194 7.1 tasks 2 to 6 | | N/A | No delivery exists before SAR | 07 section 13 (VDD and release procedure at the first release) | none |
| swe-200 7.1 task 1 | | Yes | Purpose 8 (`--volatility`, MSR-02, 02 section 10.4) gives the collection method; its schema-check claim is INSP-043 finding-5 (concur) | | none |
| swe-200 7.1 task 2 | | N/A | No MSR-02 record exists yet to analyze | 07 section 11.3 (analysis at each gate package) | none |
| swe-040 7.1 task 1 | | Yes | Tool, tests, fixtures, TV record, evidence and outputs are text files in the repository (branch, then `main`) | | none |
| swe-080 7.1 task 1 | SC | Yes | CR-011 impact: the Safety row (CR line 69) changes no hazard or control and reports four new `HAZARD_UNCONTROLLED` warnings that WP-PDR-35 and WP-PDR-16 close; the Cybersecurity row (line 74) is correct (no USB or key-input path). The tool's safety effect is on evidence routing (finding-1, finding-3) | | none |
| swe-080 7.1 task 2 | | Yes | a: CR-011 on `main` (`b01b9cd`, `7bb994f`); b: tool change on `cr/CR-011-traceability-pdr-rules`, not merged before disposition (05 Table 4-1 row 28 class-CR rule; limitation 6); c: implementation steps 1 to 3a done with SHAs; d: runs 6 and 7 and three reviews | | none |
| swe-080 7.1 task 3 | | Yes | S9: every branch commit carries `CR: CR-011`; the CR file commits carry `Refs: CR-011` | | none |
| swe-081 7.1 task 1 | | Yes | Every validated file is identified by blob and SHA-256 (run 7 table), fixtures by tree digest and git tree | | none |
| swe-081 7.1 task 2 | SC | Yes | The tool reads `hazards.json` and the requirement files as committed CIs and enforces id persistence across baselines (T-04, purpose 7); it does not change them except `--render` and `--fix-children` outputs, which are editorial (02 section 10.2) | | none |
| swe-087 7.1 task 1 | | Yes | INSP-042 (code) and INSP-043 (tool validation) performed and recorded; this record completes the WP-PDR-06 assurance review of the TV record | | none |
| swe-087 7.1 task 2 | | Yes | INSP-043 finding-1 fixed (`709e95f`, `2b004b1`) and Verified at iteration 2; its Minor findings and INSP-042's are liens with owners and a due event | | none |
| swe-088 7.1 task 1 | | Yes | INSP-043: checklist (TV template items via the code checklist field), readiness R1 to R5, findings with state, participants named (SWE-088 a to d) | | none |
| swe-088 7.1 task 2 | | Yes | Actions from INSP-043 are tracked in its iteration 2 lien table; INSP-015 cross item 1 was not actioned | | finding-2 |
| swe-089 7.1 task 1 | | Yes | INSP-043 and this record carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes`, `iteration` | | none |
| swe-090 7.1 task 1 | | Yes | The tool produces MSR-01, 03, 04 and 23 in `traceability.json` and MSR-02 by `--volatility` (02 section 8.1 option table) | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | S0 and `git rev-parse 2b004b1:<path>`: twelve branch blobs equal INSP-043; the CR file blob `d597899b` is the one INSP-043 read (on `main` it has moved to `892670b6`, a description-only revision; X-4) |
| R2 | 07 section 2.1.1 row and criticality identified | Yes, with the known gap | No 07 section 2.1.1 row for TV records (INSP-048 finding-1); criticality neither (03 sections 4.3.1 and 6.1.1); dispatched by plan WP-PDR-06 |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with a scratch `--output` reports no violation for the ids touched | Yes | The product touches no requirement, case or hazard id. On `main` (`fefcf55`), `validate_docs.py` exits 1 only on records of other work packages (SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`; PDR `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md`: record drift after later commits to their products); on the branch INSP-043 V9 records the INSP-015 and INSP-020 drift that TV-002 limitation 6 states. S1 on the export: 235 tests OK |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-043 iteration 2 committed on `main`, `author_agent` "author:WP-PDR-06", `reviewer_agent` "reviewer:WP-PDR-06-code-and-tv"; this invocation is `sa-reviewer:WP-PDR-06-tv-002` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with the known gap | Dispatched by plan WP-PDR-06 (SA second review, tool used for credit) and INSP-043 ("SA pair needed"); 07 section 2.1.1 has no TV row and the TV template says `assurance_required: false`. The inconsistency is INSP-048 finding-1, cited and not raised again |
| SA-A2 | Yes | Three invocations: author `author:WP-PDR-06`, file reviewer `reviewer:WP-PDR-06-code-and-tv`, this assurance reviewer. INSP-043 does not yet name this record (X-1) |
| SA-A3 | Yes | Same product, same `product_commit` `2b004b1`, same thirteen blobs and two fixture trees. The CR file moved on `main` after INSP-043 iteration 2; CR-011 section 5 step 5 already plans the merge-time delta that names the new CR blob or drops the CR file as context (X-4) |
| SA-A4 | Yes | INSP-043 applied the TV template item set (TV-A1 to TV-H3, G2 to G4 N/A) with readiness R1 to R5, every item answered with evidence, the code review of TV-G1-3 in INSP-042 |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: the "Every product type" row, the swe-136 and swe-070 tool tasks, and the section 7.1 tasks of SWE-052, 054, 066, 071, 191, 192, 194, 200, 040, 080, 081, 087, 088, 089 and 090. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows cite 07 sections 2.1, 9.3, 11.3, 13, 15 or 04 section 10.5; the product is of criticality neither, and each SC task answered N/A (swe-066 tasks 2 and 3) concerns test execution, which this product does not perform |
| SA-B3 | Yes | swe-052 task 2 carries finding-1; swe-191 task 3 carries finding-3 |

## C. SWE-134 items a to l

N/A for every item: `criticality` neither (07 section 14.1 lists no tool component), so `swe134_items_checked` is empty.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | N/A | The product changes no hazard and adds no software contribution (CR-011 Safety row, line 69) |
| SA-D2 | N/A | No component created or renamed; 07 section 14.1 unchanged |
| SA-D3 | No, on finding-1 | The tool checks the hazard trace both ways, with zero violations of `HAZARD_CONTROL_UNTRACED` and `HAZARD_INVERSE` on `main` data in the plain run (TV-002 R-3, R-4: no such code in the violation list). One direction has no known answer (S2) |
| SA-D4 | N/A | No safety-tagged software requirement changes |
| SA-D5 | Yes | `HAZARD_REQ_NOT_TESTED` enforces SWE-192 with no exception for `SW` and `SW-<SUB>` (S4 M-D, M-E) |
| SA-D6 | N/A | The hazard analysis is not re-issued by this product |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | No, on finding-2 | INSP-043 finding-1 was closed with evidence (iteration 2, seven fix elements; reproduced here by S1). INSP-015 re-issue 3 cross item 1 (record the run 5 review in TV-002 section 8) was not carried into the run 6 and run 7 revisions |
| SA-E2 | Yes | INSP-043 and this record carry the SWE-089 fields (07 section 10.3) |
| SA-E3 | Yes | S9; the tool is a class-CR item (05 Table 4-1 row 28) changed only on the CR branch before disposition |
| SA-E4 | N/A | No item under test and no credit run in this product |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the product needs a risk entry: the dispatch gap is INSP-048 finding-1 and the pairing and record-name items are cross items X-1 and X-4. The accreditation timing of ACC-TRACE-002 (needed by B4, plan OD-24 (b)) is on the plan's critical path, not a new risk |
| SA-F2 | Yes | Front matter carries `findings_*`, `assurance_findings_major` 0, `assurance_findings_minor` 3 (the same findings, counted once, 07 section 10.2), `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true. Every task SA-B1 requires is in the task table. Every applicable item of sections A, D, E and F is answered, and section C is N/A with its reason. There are zero Major findings. The three Minor findings are open. Under PDR work plan rule C1 and 08 section 3.2 ("Minor findings ride with APPROVED"), as INSP-043 and INSP-047 apply them, they are written for the tool owner to fix on the CR-011 branch before the merge. A finding not fixed then is a lien due at the CDR readiness declaration, listed in PDR package section 15. A fix before the merge changes blobs of `product_files` and needs a delta iteration of both records (rule C2).

`assurance_verdict: APPROVED`. With INSP-043 `reviewer_verdict: APPROVED`, both reviews of the product are APPROVED. The record `verdict` stays NEEDS CHANGES under the lead SE convention: the reviewed blobs are on the unmerged CR-011 branch, and the software lead sets APPROVED at the merge.

## Cross items (returned to Claude)

- **X-1.** INSP-043 (`tool-validation-tv-002.md`) reads `assurance_reviewer_agent: "pending: ... code-tools-traceability-software-assurance.md"`, `assurance_verdict: pending` and has no `paired_record`. Its reviewer updates it to `paired_record: INSP-051`, names this reviewer, and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row). By the 07 section 10.2 slug rule, `code-tools-traceability-software-assurance.md`, which plan WP-PDR-06, TV-002 section 8 (line 215) and CR-011 section 5 step 5 name, is the pair of the code record INSP-042. It is still to be filed. At its next revision, TV-002 section 8 lists this record as well.
- **X-2.** Dispatch of the SA review for TV records: INSP-048 finding-1 (07 section 2.1.1, the TV template and plan WP-PDR-06 and 08 disagree). No new item.
- **X-3.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `assurance_checklist`.
- **X-4.** Both INSP-043 and this record name the CR-011 file at `d597899b`. On `main` it is `892670b6` (revision 2, `7bb994f`: the branch head moved to `2b004b1` and run 7 is described, no product file changed; read here as a diff). CR-011 section 5 step 5 plans the merge-time delta, which either names the CR blob then read or drops the CR file from `product_files` as context. This record follows the same route.
- **X-5.** finding-3 has a process side. The 04 section 10.5 "Firmware release on a delivered unit" bullet (04 writer WP-PDR-13, plan section 5.3) should say how element and ICD ids are derived from changed firmware files, so that the tool limitation and the procedure agree.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse 2b004b1:<path>` for the twelve branch `product_files`; `git rev-parse main:docs/cm/cr/CR-011-traceability-pdr-rules.md` | 0 | Twelve equal to INSP-043; CR file `892670b6` on `main` (X-4) |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md`; `git rev-parse` of that path | 0 | Template revision A, blob `5b135285` |
| `git archive 2b004b1` into the scratchpad; `git hash-object` of the five tool and test files | 0 | S0 |
| TV-002 section 3 commands with the run 7 selection in the export | 0, 0, 0 | S1: 86, 32, 117 tests, OK, 0 skipped |
| Six mutants of `traceability.py` in the export (exact text substitution), `unittest discover -p 'test_traceability*.py'` and `-p test_tools.py` for each; export restored | varies | S2, S4, S5 |
| `traceability.py --root <copy of valid_project with HZ-002 on REQ-SW-KEYER-001> --output <scratch> --quiet`, plain and `--gate SRR`; the unmodified fixture under `--gate SRR` | 0, 1, 0 | S3 |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-136, 070, 052, 054, 066, 071, 191, 192, 194, 200, 040, 134, 022, 087, 088, 089, 080, 081, 090; designations from `8-10-facility-software-with-safety-considerations.md` section 6 | 0 | Task texts and SC marks of the task table |
| `git log a3cacee..2b004b1` trailers; `git log main -- docs/cm/cr/CR-011-traceability-pdr-rules.md` | 0 | S9 |
| `git merge-base --is-ancestor 26011f1 a3cacee` | 0 | S8: INSP-015 re-issue 3 precedes the branch |
| `.venv/bin/python tools/validate_docs.py` | 1 | This record PASS; the failures are the pre-existing records listed in R3 |

## Verdict format

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/cm/tool-validation/TV-002-traceability.md@94ae3af5 (and the twelve other INSP-043 product_files) at 2b004b1; PAIRED RECORD: INSP-043
PRODUCT TYPE: tool-validation (no 07 section 2.1.1 row; INSP-048 finding-1); CRITICALITY: neither
FINDINGS:
- [Minor] swe-052 7.1 task 2 (SA-D3) the hazard-trace direction "requirement lists a hazard that does not list it" has no known answer; mutant survives all 235 tests.
- [Minor] swe-136 7.1 task 1 (SA-E1) TV-002 still reads the INSP-015 run 5 review as pending; the ACC-TRACE-001 extension to 12de3545 is effective since 2026-09-26.
- [Minor] swe-191 7.1 task 3 limitation 9 omits that firmware-path arguments never select a REQ-SW traced by element or ICD id alone (04 section 5.2 T-SW-TARGET carry-forward).
TASKS APPLIED: swe-134 task 5, swe-022 task 1, swe-136 task 1, swe-070 task 1, swe-052 tasks 1 and 2, swe-054 task 1, swe-066 task 1, swe-071 task 1, swe-191 tasks 1 and 3, swe-192 task 1, swe-194 task 1, swe-200 task 1, swe-040 task 1, swe-080 tasks 1 to 3, swe-081 tasks 1 and 2, swe-087 tasks 1 and 2, swe-088 tasks 1 and 2, swe-089 task 1, swe-090 task 1
TASKS N/A (relief): swe-066 tasks 2 and 3 (07 sections 2.1, 15), swe-191 task 2 (07 section 9.3), swe-191 task 4 (04 section 10.5), swe-194 tasks 2 to 6 (07 section 13), swe-200 task 2 (07 section 11.3)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=1 TV record, 9 purposes, 235 tests; tasks=36; tasks_no=2; mutants=6 (5 killed, 1 survived); turns=45; minutes=80; major=0; minor=3
```
