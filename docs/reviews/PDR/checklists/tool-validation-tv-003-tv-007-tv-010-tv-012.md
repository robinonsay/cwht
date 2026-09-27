---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/05-configuration-and-data-management.md section 9.2 step 3). Record of the independent review of the
# CR-014 re-validations (PDR work plan WP-PDR-09, Records line: "docs/reviews/PDR/checklists/
# tool-validation-tv-003-tv-007-tv-010-tv-012.md for the re-validations"), with the code review of the changed tool
# source appended (TV template item TV-G1-3; 03 section 6.1.1 row "Peer review").
# Item set applied: docs/templates/peer-review-checklist-tool-validation.md revision A on branch
# cr/CR-012-pdr-checklist-templates at 7784672 (not on main), plus docs/templates/peer-review-checklist-code.md
# revision B for the source. tools/validate_docs.py rejects a checklist field whose template is absent from
# docs/templates/ on main, so the checklist field names the code checklist, as INSP-040 to INSP-043 did.
# Product frozen by the brief (rule C2): the CR-014 branch head 367b3dd (main 72d0a2f merged into f924595; every
# tool, test, fixture, TV and evidence blob below equals git rev-parse 367b3dd:<path>, checked by the reviewer),
# plus the CR-014 file on main at eb200de. Directory entries of the brief (fixture tree, renders tree) are
# listed file by file here, with their trees in fixture_trees.
id: INSP-100
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-003-tv-007-tv-010-tv-012.md
product: docs/cm/tool-validation/TV-003-validate-docs.md
product_commit: "367b3dd481fdbde0170582607d2285dfdae4bc9f"
product_files: ["docs/cm/cr/CR-014-tool-liens-srr.md@139d860d3b69c960fde9fb306470ed624c3a085e", "tools/validate_docs.py@e5b692e154eed71a664ce2bdd95b8e64906b79b8", "tools/tests/test_validate_docs.py@e9c305fc5c3e64e7796585002675c83ab5c15559", "tools/review_trend.py@9e451fa24a1707d53420cb12590fbfd39fef6f1b", "tools/tests/test_review_trend.py@9fa7908d351688612abb7f7cea7affe405220674", "tools/render_review_figures.py@7607e7c258f29d58287a15103903b99e6206b94d", "tools/tests/test_render_review_figures.py@366dc553d907f1f075ab0d3ca548526d9fb0ffda", "tools/tests/fixtures/review_figures/docs/conops/conops.md@f02154a86fee760e6ec8f73c4f6d1cb0c1c2a0f9", "tools/tests/fixtures/review_figures/docs/design/concept.md@65b554bef9df2f3c285a23aa0804d1d68b9beaaa", "tools/tests/fixtures/review_figures/docs/plan/tpm.json@45325583fef4b82a8f3fc66c25836ef3dbb83d76", "tools/tests/fixtures/review_figures/docs/requirements/sys/requirements.json@5be9a3d53aff1efa4838751b2a7778338524c839", "tools/tests/fixtures/review_figures/docs/reviews/SRR/package.md@ab1d40e0d093549607bee03451cbc3b979e125de", "tools/tests/fixtures/review_figures/docs/risk/register.json@8fd300159e7ffcbd075f3e6765174d3569611be7", "tools/tests/fixtures/review_figures/docs/risk/register.md@86e23b96ad888d05b60d3600b5475c401b970c3a", "tools/tests/fixtures/review_figures/docs/safety/hazards.json@4f973f926ea6e53491eabc668512796454b0ebc3", "tools/complexity_gate.py@e9cfd465a7412549c0347dfac59080ec83964c18", "tools/tests/test_complexity_gate.py@6199fcd8f707692ffd14c07a67a9d403d399a31e", "tools/measurements.py@cec467f17a89e61ab49b5a46cb03cfaa855c2e9b", "tools/tests/test_measurements.py@3b43ec1fb256e637c376843b3a0de56c08a318b8", "tools/sw_gate.sh@6048c8015b1e2fd4f40bf9f900ee1a69681380e0", "firmware/cwht-app/src/main.rs@3006d072986f5d6379863179000e2a2a3dd36e7c", "tools/toolchain.lock.md@836536ce9aa603aa8d53c178ad573f46b47571dc", "tools/README.md@bc4e43900b775ddca1c708dfbffda199870af0fd", "docs/cm/tool-validation/README.md@2ff68008aeac136360885f607b9eeaadb3805b8c", "docs/cm/tool-validation/TV-001-python-jsonschema.md@08125d63c20221dcf63f2f02108d405a52ba00cc", "docs/cm/tool-validation/TV-003-validate-docs.md@3eb258f15361acf137312cfc40e1befb9add333e", "docs/cm/tool-validation/TV-007-review-trend.md@1ecc089aba0131949f3ca496863dd64e8a967de6", "docs/cm/tool-validation/TV-010-render-review-figures.md@31d328fb97974bc0e4122d442a6a1dd34b8e9feb", "docs/cm/tool-validation/TV-012-complexity-gate.md@87bc6e2570d761a282976f4e01efb592039f1200", "docs/cm/tool-validation/TV-013-measurements.md@91101cf7667f5b6b6d5b0ecfb52c612a364dbc2a", "docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.py@3095a9332710be0a0a42f2ff11095a16292421b8", "docs/cm/tool-validation/evidence/wp-pdr-09-2026-09-27.log.txt@d81e7dd5c58d8983556884658e3f6abd787fdd7e", "docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.sh@2adb7e8e2783184fb84ede5198324a489086f3b4", "docs/cm/tool-validation/evidence/sw-gate-g0-export-2026-09-27.log.txt@0ccfea97171cbea82658427383a82f8bbc8eab9b", "docs/cm/tool-validation/evidence/complexity-gate-2026-09-27-r4.log.txt@10f125a61a42e817b46569fd6415d3355547061c", "docs/cm/tool-validation/evidence/requirements-freeze-2026-09-27.log.txt@84904d6d375201d95017e70c86b68db3d2f05de0", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/concept-block-diagram.png@ec80831017de889e758f04a32a20c654592a5987", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/fixture/risk-matrix.png@f5175ed8202aa9ab95686a765825ff2cc3bc7da3", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/fixture/success-criteria.png@04d4e5162f1af36b91cbb224b936e4b703bb8a76", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/review-trend-2026-09-26.png@18c38e5043579890239dd9800bafe68aa8b53182", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/review-trend-2026-10-06.png@4b5a8d463a7e246b7c02e52e9941563f44e16901", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/risk-matrix.png@fc52c4890fd6bec69fcebec26ccec31709950146", "docs/cm/tool-validation/evidence/wp-pdr-09-renders/success-criteria.png@5fdf6a7ad94ec52e816a752f8b055628af374cf5"]
# fixture_trees: git rev-parse 367b3dd:<dir>; the renders tree is the evidence folder of the brief (5 repository
# renders and 2 fixture renders); the unchanged fixtures read by the re-runs are listed for identity
fixture_trees: ["tools/tests/fixtures/review_figures@fd5b721d4a2c29ee95a4dab8f642e15789331dcd", "docs/cm/tool-validation/evidence/wp-pdr-09-renders@7b58395d8575d8ff0860eb169c0e33abefe62b61", "tools/tests/fixtures/review_trend@2109a738ea23d5b0befdd8756a171595ddb879b6", "tools/tests/fixtures/complexity_gate@23f23d9d305fbc18fcb9cd5b8e8ba6c50581c7e5", "tools/tests/fixtures/measurements@ed4414ecd9336349d4ba03cd8257b0079d470d8d", "tools/tests/fixtures/record_state@b7c20457f2ae8c4d0fec41b52abd127003aa34ff"]
# tv_ids: the four records the plan names, plus TV-013 run 4 (a revalidation row on the same branch; the TV-013
# record review itself is INSP-041 of WP-PDR-08, whose delta on blob cec467f1 is CR-014 section 5 step 7)
tv_ids: [TV-003, TV-007, TV-010, TV-012, TV-013]
tool_class: B
# tool_kind: repository-tool for TV-003, TV-007, TV-010, TV-012; revalidation for TV-013 run 4
tool_kind: repository-tool
acc_proposed: [ACC-VALDOCS-001, ACC-TREND-001, ACC-FIGS-001, ACC-COMPLEXITY-001, ACC-MEASURE-001]
product_size: "5 TV records (26 purposes, 5 new runs), 1 CR file, 7 changed tool or source files (1879 lines added, 305 removed on the branch against 72d0a2f), 6 known-answer modules (285 tests in the re-run selections: 157 + 25 + 55 + 28 + 20), 8 fixture files, 6 evidence files and 7 renders"
sprint: PDR-prep
author_agent: "author:WP-PDR-09 (Claude as tool owner and software lead, CR-014)"
tool_author_agent: "author:WP-PDR-09 (Claude as tool owner, CR-014)"
reviewer_agent: "reviewer:WP-PDR-09-tv-and-code (independent invocation; authored no part of CR-014, WP-PDR-09, the TV records or the tools)"
# criticality: a tool is neither safety-critical nor mission-critical (03 sections 4.3.1 and 6.1.1)
criticality: neither
# assurance_required: the TV template says false and makes section H this reviewer's task; PDR work plan WP-PDR-09
# names "SA for credit tools" and CR-014 section 5 step 5 names a software assurance pair, so the pair is requested
# from the lead SE (the dispatch conflict is INSP-048 finding-1, not raised again here)
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/tool-validation-tv-003-tv-007-tv-010-tv-012-software-assurance.md (plan WP-PDR-09; CR-014 section 5 step 5)"
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED for this lens (zero Major; three Minor findings, liens under plan rule C1 unless the
# author fixes them on the CR-014 branch before the merge)
reviewer_verdict: APPROVED
assurance_verdict: pending
# verdict: held at NEEDS CHANGES (a) until the software assurance pair is APPROVED (07 section 2.1.1 rule as the plan
# applies it) and (b) while every reviewed tool blob exists only on cr/CR-014-tool-liens-srr (lead SE convention of
# 2026-09-27, INSP-031 practice); set in the CR-014 merge commit, or the commit right after it, with these blobs unchanged
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 3
findings_open: 3
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
deferred_rids: []
items_no: [TV-B3, TV-C2, TV-E1, TV-F5, CK-CODE-E1]
effort_turns: 82
effort_minutes: 120
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-100: CR-014 re-validations TV-003 run 7, TV-007 run 4, TV-010 run 5, TV-012 run 4, TV-013 run 4, with the code review of the changed tools (WP-PDR-09, iteration 1)

**Product (frozen, rule C2).** The CR-014 branch `cr/CR-014-tool-liens-srr` at head `367b3dd` (product commits `16cdd3e` to `7b4e3b4`, `main` `72d0a2f` merged in) and the CR file on `main` at `eb200de`. Every path of `product_files` was checked with `git rev-parse 367b3dd:<path>` (CR file: `git rev-parse main:docs/cm/cr/CR-014-tool-liens-srr.md`): all 43 entries and the two trees of the brief are equal to the frozen values. The tool blobs are identical at `f924595`, the commit the author's runs name; the merge changed only `tools/toolchain.lock.md` among the product files (`c890619e` to `836536ce`) and added the WP-PDR-07 tools, which are outside this product.

**Checklist.** The TV template item set (`peer-review-checklist-tool-validation.md` revision A, CR-012 branch `7784672`), sections R, A to F, G1 and H, for each record in `tv_ids`; the code checklist revision B for the source of the six changed tools and the `main.rs` comment (TV-G1-3), appended below. **Governing clauses checked case by case (rule C7):** 05 section 9.2 steps 1 to 5 and the known-answer table rows of `tools/validate_docs.py`, `tools/review_trend.py` and `tools/render_review_figures.py`; every purpose of TV-003 (1 to 8), TV-007 (1 to 3), TV-010 (1 to 4), TV-012 (1 to 5) and TV-013 (1 to 6); every carried item CR-014 section 1 claims (C-170, C-172, C-173, C-175, C-178, C-179, C-185, C-186, C-072, C-203, C-204, and the record side of C-171, C-174, C-176, C-177 and C-182) against its source finding text; the CR-014 section 5 "Verification of the implementation" list (evidence re-run on an export, SRR concept render pixel for pixel, the seven PNGs opened, `validate_docs.py` failures on the branch against `main`, G0 on a fresh export and clone).

**Independence (rule C4).** This invocation authored no part of CR-014, the TV records, the tools, the evidence or the renders. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the WP-PDR-09 checklist and role; 07 section 2.1.1; INSP-015 F-08 and F-09; 05 section 9.2 step 5); `grep -n` only pinned lines afterwards. The rustos working tree was not read: rustos content came only from `git -C /Users/robinonsay/rust/rustos archive 2ec64c0`, `rev-parse 2ec64c0^{tree}` and a `--no-checkout` clone of its object store in the scratch directory. No download, install or push. LTspice was not run by this review; see cross item X-4 for a full-suite run that reached the LTspice wrapper test and was stopped.

## Record

### Reviewer re-runs (evidence)

| # | Check | Result |
|---|---|---|
| V1 | The author's evidence procedure `evidence/wp-pdr-09-2026-09-27.py` (blob `3095a933`, `REPO` pointed at the repository) on an export of `367b3dd` with base `7bb994f`, reviewer scratch directory | exit 0, `# result PASS`. Every identity line "equal to COMMIT" (lock `836536ce` at `367b3dd`; every other blob as in the author's log). TV-003 40 + 117, TV-007 25, TV-010 55, TV-012 28, TV-013 20 tests, each selection twice, all OK, 0 skipped. The five base-blob mutation checks and the five targeted mutants of the fold each FAIL as required, with the same failing test names as the author's log |
| V2 | TV-007 author mutants not in the evidence log (TV-007 section 5 "a reviewer repeats them by the edits named"), in a scratch copy of the export | default date locator restored: 1 failure; closed label always below: 2 failures; series started on the first item's day: 1 failure and 1 error (2 tests). Equal to TV-007 |
| V3 | TV-013 full module against blob `abe25acb` (TV-013 run 4 "fails 8 tests", author scratch run) | 7 failures and 1 error, 8 tests. Equal |
| V4 | TV-012 run 4 gate row repeated: `rust-code-analysis-cli` 0.0.25 on an export of `367b3dd` (`firmware/`) and the rustos export of `2ec64c0`, new blob `e9cfd465` and previous blob `ddf10798` on the same analyzer output | both exit 0 and identical (`diff` exit 0): CS-17 no failure, 52 functions, max CC 5, mean 1.46, `main.rs:30 main CC 4 = analyzer 2 + 2 let ... else`, CS-38 allowance 4, `complexity_gate: PASS`. Equal to `evidence/complexity-gate-2026-09-27-r4.log.txt` apart from the scratch path |
| V5 | G0 evidence procedure `sw-gate-g0-export-2026-09-27.sh` on fresh layouts (export, seeded export, export inside an outer repository, clone at `2ec64c0`, clone at `c54d35a`) with the head `sw_gate.sh` and the head lock; `git -C rustos rev-parse 2ec64c0^{tree}` | `39d8d8a9d54c7e3dc1b5b675a7dffe7cc743612d`, equal to the lock's "tree of the pin"; 5 of 5 MATCH (PASS, FAIL, PASS, PASS, FAIL), `# result 0`. Gate block sha256 `5f8b6b36...2ada` equal to the author's log |
| V6 | `tools/requirements.txt` against `.venv/bin/python -m pip freeze` | 35 of 35 pins equal; only the three header comment lines differ. Equal to `evidence/requirements-freeze-2026-09-27.log.txt` |
| V7 | `rustfmt --check --edition 2024 firmware/cwht-app/src/main.rs` (edition of the firmware workspace) on the export; `wc -l` at `7bb994f` and `367b3dd` | exit 0; 68 and 68 lines. Note: with `--edition 2021` rustfmt reports an import-order diff, so the claim holds for the workspace edition only, which is the one `cargo fmt` uses |
| V8 | `tools/validate_docs.py` on a detached worktree of `367b3dd` and of `72d0a2f` | branch 76 passed, 9 failed; `72d0a2f` 77 passed, 8 failed; the one extra failure is `docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md` (INSP-016 record drift on `main.rs` and `sw_gate.sh`), as CR-014 section 4 foresees; INSP-015's drift is already on `main` |
| V9 | The new `validate_docs.py` against the old on the records of current `main` (`9b20ea5`, detached worktree, tool file swapped) | identical FAIL set and counts (81 passed, 8 failed): the amended purpose 7 changes no record's result today |
| V10 | Unread finding ids under the new rule: every record on `main`, all finding rows of the body against the rows of `latest_iteration_section` | one record has finding ids the rule does not read: INSP-042 (`code-tools-traceability.md`, iteration 2, 8 ids under "### Findings (filled by the reviewer and the assurance reviewer)"); see finding-1 |
| V11 | Module-by-module unit tests on the `367b3dd` worktree, every module except `test_ltspice_batch`, `test_kicad_cli`, `test_scad2step` and `test_render_deck` (WP-PDR-07 and deck tools outside this product; X-4) | all pass except `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the repository-content class, which fails on the V8 record drift set only |
| V12 | `tools/traceability.py --report-only` on the `367b3dd` worktree | 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 `SYS_UNALLOCATED`), as CR-014 section 4 states. The worktree was removed afterwards; nothing written on `main` |
| V13 | Seeded layout faults of the concept checks (reviewer probes on the fixture figure set with `CONCEPT_LAYOUT_SLIDE`, fonts loaded) | a diagonal segment, an emptied crossing set, a label moved onto block PICO, a route through LPF and TR, and a label at the image edge are each detected with the check's own message; the unmodified layout passes. The checks work; their known answers are the subject of finding-2 |
| V14 | Renders opened (visual closure, rule C5): the seven PNGs of `evidence/wp-pdr-09-renders/` | see "Renders inspected" below |

### Renders inspected

| Render | Size | What was checked | Result |
|---|---|---|---|
| `review-trend-2026-09-26.png` | 1200 x 952 | RID-SRR-004 single-date case: SRR panel rise to 22 drawn with a marker on 2026-09-26; dates 2026-09-25 to 2026-09-29 each labelled once; "0 closed + withdrawn" above the axis, clear of the date labels; the empty PDR panel labels each date once | pass |
| `review-trend-2026-10-06.png` | 1200 x 952 | Every other day labelled once (at most 8); the rise stays visible beside the SRR memo line (zoomed at 3x); T label in the top band; end labels clear | pass |
| `risk-matrix.png` | 1760 x 885 | 65 ids drawn; counts per cell sum to 65; Red 31 by cell plus RSK-034 by the safety override = 32, Yellow 25, Green 8, as the legend states; the override mark and note present; text readable at 1:1 | pass |
| `concept-block-diagram.png` | 1760 x 950 | `CONCEPT_LAYOUT_SLIDE`: 22 blocks B01 to B22 in their groups, legend, edge labels, no text over a line or block, two crossings | pass |
| `success-criteria.png` | 1760 x 790 | Not met 4, Partially met 4, Met 10 (SRR package section 20); footer "an owner ruling is pending" (C-204) | pass |
| `fixture/risk-matrix.png` | 1760 x 885 | RSK-001 in (4, 4), RSK-002 marked in (2, 5), RSK-003 in (1, 2); Red 2 (1 by override), Yellow 0, Green 1 | pass |
| `fixture/success-criteria.png` | 1760 x 790 | 2, 0, 1 with the two fixture footer lines | pass |

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | TV-E1, CK-CODE-E1 | `tools/validate_docs.py` `FINDINGS_HEADING` (the line after `ITERATION_HEADING`) and `latest_iteration_section`; TV-003 purpose 7 amendment and limitation 7 | The F-09 fix reads a master finding table only under a heading whose text is exactly "Findings". The project's own headings are longer: the TV template (CR-012) files its table under "### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)", INSP-042 under "### Findings (filled by the reviewer and the assurance reviewer)", and eleven PDR records under "## Findings (iteration 1)". Before the heading that names the highest iteration, such a table is still not read. Effect today (V10): INSP-042 is at iteration 2 with 8 unread Minor ids and `findings_open: 8`; when the software lead sets its verdict to APPROVED at the CR-011 merge, rule (d) fails it ("findings_open is 8 and the latest iteration's finding tables show 0 open Minor finding(s)", reproduced with `approval_errors`). The reverse case, an open Major left in such a table and not restated later, would pass rule (c). No result is wrong today (V9), and limitation 7 states the exact-heading scope, so the limitation is true; but it leaves the F-09 gap open for the template form the project uses. Fix: match a heading whose text begins with the word "Findings" (for example `^(#{1,6})\s+Findings\b`), add a known answer with the template heading and one with "Findings (iteration 1)" before a higher iteration heading, and amend purpose 7 and limitation 7 | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | TV-B3, TV-C2 | TV-010 purpose 3 (as amended from blob `7607e7c2`) and section 3 `FoldedFigureTests`; `tools/tests/test_render_review_figures.py` | Purpose 3 lists the layout checks of the two folded figures: every text inside its cell or box and the image, no text over another text, a block or a foreign edge, orthogonal edges not through blocks and not on top of each other, the reviewed crossing set, and the text floor. The known answers seed a failure for two of them only: block overlap (`MIX` moved onto `FE`) and the floor (SRR layout at 14.5 pt; risk corner text at 16 pt), plus the register.md cross-check. The other clauses (non-orthogonal segment, edge through a block, edges on top of each other, crossing set changed, text over an edge or a block, text clipped by the image, text leaving its box or cell, the risk "ids drawn equals active risks" count, block outside its group) are exercised only in the passing direction. The reviewer's probes (V13) show the checks work, so no claim is false; but the purpose, and ACC-FIGS-001 as proposed, cover more than the known answers check (INSP-015 F-01 pattern), and limitation 2 (render inspected by the author) is what stands behind them today. Fix: add one seeded fault per listed check (V13 gives five ready cases), or narrow purpose 3 and the ACC-FIGS-001 extension to the seeded checks and state the rest as a limitation | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | TV-F5 | TV-003, TV-007, TV-010 and TV-012 headers and section 9 proposed extensions; CR-014 section 1 | 05 section 9.2 step 5 says a version change of an Accredited tool after SRR is "a CR ... plus a new TV record", and step 4 says "no new TV number unless the version changed". CR-014 changes four accredited tool blobs and appends runs and proposed extensions to the existing records instead. This is the same open reading as INSP-043 finding-2 (TV-002 under CR-011), which asks the owner to rule; this record adds the four CR-014 records to that question and does not repeat the argument. Fix: the owner's ruling on INSP-043 finding-2 applies here too; the records then cite it (a new TV number per changed blob, or 05 section 9.2 amended by its writer to admit re-validation inside the record for a repository tool changed under an approved CR) | Open | Pending | |

Findings by severity: 0 Major, 3 Minor. All three are liens due at the CDR readiness declaration under plan rule C1, unless the author fixes them on the CR-014 branch before its merge (a fix changes product blobs and needs a delta iteration of this record).

### Observations (not findings)

1. **Findings sections inside a lower-iteration block.** `latest_iteration_section` now re-reads a "Findings" section even when it stands under a later heading that names a lower iteration (the `SrrToolLienTests` case "a Findings section under a lower-iteration heading after the start is read"). A superseded "Closure as written at iteration 2" block that carries its own "Findings" table after the latest section would then supersede the newer rows in document order. The failure is a false fail, never a false pass, and no record on `main` has that form (V9). Worth a sentence in limitation 7 when finding-1 is fixed.
2. **Base-blob mutation check of TV-010.** Against blob `6f3018fd` the test module fails at import (`_FailedTest`), which shows only that the names are new. The five targeted mutants carry the discriminating evidence and the record says so (TV-010 section 5); no change needed.
3. **Author scratch mutants.** TV-007 run 4 and TV-013 run 4 cite mutant runs made outside the evidence log. V2 and V3 repeated them with equal results, so the rows stand; a future re-validation could fold them into the procedure.
4. **Slide pixel floor.** The folded figures meet 14.5 pt at dpi 100 (20.1 px) at their native size. The 20 px floor on the slide holds only if the deck embeds them at 1:1; that is the WP-PDR-50 deck reviewer's check (TV-010 section 8 names it).

### Cross items (outside this product; for the lead SE)

| # | Item |
|---|---|
| X-1 | The software assurance pair is needed (plan WP-PDR-09 "SA for credit tools"; CR-014 section 5 step 5); this record names it in `assurance_reviewer_agent` and does not do the assurance lens |
| X-2 | The SRR record deltas that the plan names as the lien verifications (INSP-015 for F-07 to F-12, INSP-016 for F-13 and F-16; CR-014 section 5 step 6) and the INSP-041 delta on `measurements.py` `cec467f1` (step 7) are not in this record. This record's evidence (V1 to V8) can be cited by them. C-172, C-173 (partly, finding-1), C-175, C-178, C-179, C-185 and C-186 were checked here against their source finding texts and are implemented as the findings asked |
| X-3 | CR-014 section 6 (rule C6 impact review) is still "Pending" at `eb200de`; it is a separate invocation and precedes the owner's disposition |
| X-4 | The TV template readiness item R3 and the brief's command `python -m unittest discover -s tools/tests` now also run `test_ltspice_batch.py` (merged from `main` at `367b3dd`, WP-PDR-07), which calls `tools/ltspice-batch.sh`. A full-suite run by this reviewer on a scratch worktree reached `ltspice-batch.sh -version` at about 13:34 CDT; the reviewer stopped that run and its wrapper processes at once, no `LTspice.exe` process with the worktree path was seen, and the module-by-module run V11 replaced it. The same minute three other agents' full-suite runs were also calling the wrapper, and `d9c7f69` (13:34) records TV-014 run 4 failing on a held wrapper lock. Recommendation: reviewer briefs name a selection that excludes the LTspice, KiCad and FreeCAD modules, or those modules skip unless a `CWHT_EXTERNAL_TOOLS=1` switch is set |
| X-5 | INSP numbering: while this review ran, the working tree held duplicate ids in other agents' committed and untracked records (INSP-071, INSP-072 and INSP-073 each twice at one reading); this record took INSP-100, the next number after the highest in any branch or file at filing |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Everything committed; `product_files` blobs at `product_commit`; fixture trees | Yes | All 43 blobs and the trees checked with `git rev-parse` (Product paragraph); the branch has no uncommitted state (a worktree of the commit was used) |
| R2 | Section 3 commands exit 0 on the committed state | Yes | V1 |
| R3 | Full unit suite passes; `validate_docs.py` exits 0 | Yes, with the stated exceptions | V11: every module of this product passes; the repository-content class and `validate_docs.py` fail only on record drift, all present on `main` except INSP-016, which CR-014 foresees (V8). The LTspice, KiCad, FreeCAD and deck modules were not run (X-4) |
| R4 | Lock rows and README index | Yes | Lock sections 1.1, 1.2 and 5 carry TV-003 run 7, TV-007 run 4, TV-010 run 5, TV-012 run 4 and TV-013 run 4; `docs/cm/tool-validation/README.md` rows TV-003 to TV-013 updated; the rustos row carries "tree of the pin" `39d8d8a9` |
| R5 | Author's return lists purposes, uses, tests, runs and ACC scopes | Yes | Author summary in the brief and CR-014 sections 1, 4 and 5; each TV record section 2 and 9 |

## Per-record results

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-003 | `tools/validate_docs.py` blob `e5b692e1` | B | `f924595` (runs), `367b3dd` (review) | V1 selection 40 + 117; exit 0; same; mutation 5 of 7 fail on `3aa03681` (the two passing tests are regression guards, as the record says) | TV-E1, TV-F5 | finding-1, finding-3 |
| TV-007 | `tools/review_trend.py` blob `9e451fa2` with `validate_docs.py` `e5b692e1` | B | `f924595` | V1 25; exit 0; same; V2 three mutants equal | TV-F5 | finding-3 |
| TV-010 | `tools/render_review_figures.py` blob `7607e7c2` with `render_risk.py` `d38ba1dd` | B | `f924595` | V1 55 (56 with the repository class, V11); exit 0; same; fonts linked, the pixel test ran (not skipped) | TV-B3, TV-C2, TV-F5 | finding-2, finding-3 |
| TV-012 | `tools/complexity_gate.py` blob `e9cfd465`, `rust-code-analysis-cli` 0.0.25 | B | `f924595` | V1 28; exit 0; same; V4 gate row equal | TV-F5 | finding-3 |
| TV-013 | `tools/measurements.py` blob `cec467f1` (revalidation row) | B | `f924595` | V1 20; exit 0; same; V3 equal | none | none |

## Per-purpose results

| TV record | Purpose | Known answer that exercises it | Seeded fault (class B) | Cited uses of the purpose | Finding ids |
|---|---|---|---|---|---|
| TV-003 | 1 schema discovery | `ValidProjectTests`, `InvalidProjectTests` (unchanged) | invalid project documents | every agent's validation run (08 section 1 COMMANDS); readiness | none |
| TV-003 | 2 record front matter and rules (with 8) | `PeerReviewRecordTests`, `test_tools.py` | invalid records | every INSP record; 07 section 2.1.1 reason check | none |
| TV-003 | 3 RFA/RID logs | `test_tools.py` log classes (unchanged) | invalid log | SRR and PDR logs | none |
| TV-003 | 4 decision memos | `test_tools.py` memo classes (unchanged) | invalid memo | SRR memo | none |
| TV-003 | 5 exit statuses | `UsageErrorTests`, valid and invalid runs | unknown option, bad root | every run | none |
| TV-003 | 6 record drift | `RecordDriftTests` (unchanged) | changed blob in a temporary repository | every APPROVED record | none |
| TV-003 | 7 record state (amended) | `RecordStateTests`, `SrrToolLienTests` (single iteration read whole; "Findings" before "Iteration 3"; lower-iteration Findings after the start; `finding_key`) | open Major in the INSP-028 and INSP-029 forms fail | every APPROVED record | finding-1 |
| TV-003 | 8 L-7 and decision 9 constants | `SrrToolLienTests.test_l7_assurance_products_and_decision_9_module` | fails on `3aa03681` (V1) | assurance reason of 05, TS-002 and SW-SYNTH records | none |
| TV-007 | 1 counts and zones | `KnownAnswerTests`, `ZoneTests` (unchanged) | template log counts | TPM-003, package build | none |
| TV-007 | 2 figure and TPM append (amended) | `PlotKnownAnswerTests` (ticks, leading zero day, markers, label offsets, single-date figure), `WriteTests` | fails on `04493157`; V2 mutants | `docs/reviews/<REVIEW>/figures/review-trend.png`, `tpm.json` TPM-003 | none |
| TV-007 | 3 exit statuses | `CliTests` | Red zone, bad input | package build | none |
| TV-010 | 1 read package and products (amended: risk dimensions, concept Mermaid) | `ParserTests`, `DataKnownAnswerTests`, `FoldedFigureTests.test_concept_model`, `test_risk_scoring_is_render_risk` | missing inputs exit 1 | SRR and later package figures | none |
| TV-010 | 2 cross-checks (amended: register.md, concept model, footer) | `test_register_md_disagreement_stops_the_run`, `test_concept_model_disagreement`, `test_footer_quotes_the_package`, `test_srr_footer_is_the_srr_package_wording` | each disagreement exits 1; targeted mutants (V1) | package figures, next deck (WP-PDR-49, 50) | none |
| TV-010 | 3 render with layout checks (amended) | `test_risk_matrix_layout_and_floor`, `test_concept_slide_layout_meets_the_floor`, `test_srr_layout_reproduces_the_srr_render`, `test_a_layout_failure_exits_one_and_writes_nothing` | overlap and floor only | next deck figures; RID-SRR-014, INSP-029 findings 5 and 6 | finding-2 |
| TV-010 | 4 exit statuses | `RunTests` | usage and data errors | every run | none |
| TV-012 | 1 own CC (amended: let-else after `>`) | `LetElseTests.test_binding_after_a_type_closing_angle_bracket` and the unchanged classes | fails on `ddf10798` (V1) | gate G5, MSR-17 | none |
| TV-012 | 2 CS-17 | `GateKnownAnswerTests` (unchanged) | CC 16 fixture | gate G5 | none |
| TV-012 | 3 CS-38 | `AllowanceTests`, `MainLoopTests` (unchanged) | over-allowance function | gate G5 | none |
| TV-012 | 4 CS-19 report | cycle known answers (unchanged) | comment and string not a cycle | gate G5 | none |
| TV-012 | 5 MSR-17 and exits | `UsageTests`, MSR-17 line | input errors exit 2 | `measurements.json` MSR-17 | none |
| TV-013 | 1 link map | `LinkMapTests` (prefixed lines) | map above the red line | gate G2 | none |
| TV-013 | 2 diff runs | `DiffRunsTests` | differing, empty, failed runs | gate G3 | none |
| TV-013 | 3 coverage | coverage classes (unchanged) | NOT PRODUCED input | gate G6 | none |
| TV-013 | 4 check records | `RecordsTests` | six seeded record faults | measurements records | none |
| TV-013 | 5 analyze | `--analyze` known answer (unchanged) | none needed (report) | measurements review | none |
| TV-013 | 6 exits and result lines (amended) | `ResultLineTests` (2) | fails on `abe25acb` (V1, V3) | `sw_gate.sh` log | none |

## A. Identification

| Id | Answer | Evidence |
|---|---|---|
| TV-A1 | Yes | Blobs and SHA-256 per record section 1 (TV-003 `e5b692e1` / `94a02b3a...6ebb`; TV-007 `9e451fa2` / `d24c3c96...dae2`; TV-010 `7607e7c2` / `15509ea6...59ce`; TV-012 `e9cfd465` / `7d066cfd...3e23`; TV-013 `cec467f1` / `e1b83c6d...ffae`); interpreter Python 3.13.5 printed by V1; analyzer 0.0.25 printed by V4 |
| TV-A2 | N/A | Repository tools, no installer; TV-001 covers the interpreter and venv (V6) |
| TV-A3 | Yes | Blobs recomputed by V1 identity lines; fixture tree `fd5b721d` and the unchanged trees of `fixture_trees` by `git rev-parse` |
| TV-A4 | Yes | Every new run row names `f924595`, which contains each tool, test and fixture at the identified blobs (V1 on `367b3dd` equal; `git diff f924595 367b3dd` touches none of them) |
| TV-A5 | Yes | Class B in every header, unchanged (05 section 9.1: review and gate evidence) |
| TV-A6 | Yes | Headless: unittest, `git archive`, shell; matplotlib Agg backend |

## B. Purposes

| Id | Answer | Evidence |
|---|---|---|
| TV-B1 | Yes | Each amended purpose is one numbered item stating inputs, output and exit status (per-purpose table) |
| TV-B2 | Yes | Cited uses searched: `validate_docs.py` in every brief and readiness step; `review_trend.py` in 01 section 11 and package builds; `render_review_figures.py` in the package and deck WPs (49, 50); `complexity_gate.py` and `measurements.py` in `sw_gate.sh` G2, G3, G5, G6. Every use maps to a purpose |
| TV-B3 | No | finding-2 (TV-010 purpose 3 lists checks with no failing known answer). TV-003 purpose 7 states the exact "Findings" scope truthfully (the gap is finding-1, under TV-E1) |

## C. Known-answer test

| Id | Answer | Evidence |
|---|---|---|
| TV-C1 | Yes | Fixtures under `tools/tests/fixtures/review_figures/` (8 files) and the unchanged fixture roots; run commands and counts in each section 3 |
| TV-C2 | No | Every amended purpose has a known answer and a seeded fault except the unseeded clauses of TV-010 purpose 3 (finding-2); negative controls: the base-blob mutation checks and targeted mutants (V1) |
| TV-C3 | Yes | Expected values hand-read from the record text or the rules (test docstrings); the concept pixel answer is the SRR package render made by the separate SRR generator; risk bands against `render_risk.band` (TV-006); complexity values hand-derived |
| TV-C4 | Yes | 05 section 9.2 rows: `validate_docs.py` fixture-only classes separated from the repository class; `render_review_figures.py` repository-content class separate; `review_trend.py` counts on the template copy. No clause unmet |
| TV-C5 | Yes | V1: counts, outputs and exit statuses equal to the records |

## D. Results and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| TV-D1 | Yes | Each run row has date, commit, count, excerpt and the committed log `evidence/wp-pdr-09-2026-09-27.log.txt`; the gate row has its own log; the author scratch mutants are extras (observation 3) |
| TV-D2 | Yes | Lock section 1.1 rows carry the 2026-09-27 runs with `f924595` and counts; section 5 rows agree with the record status lines |
| TV-D3 | N/A | Class B; each selection run twice with identical results anyway (V1) |

## E. Limitations and re-validation triggers

| Id | Answer | Evidence |
|---|---|---|
| TV-E1 | No | Confirmed by code and runs: TV-003 limitation 7 (exact "Findings", confirmed by probe; the remaining gap is finding-1); TV-007 limitation on colours and fonts (still inspected, true); TV-010 limitation 2 (literals; true, the layout is a literal checked by purpose 3); TV-012 F-11 limitation update (true, V4); no limitation contradicted by behaviour |
| TV-E2 | Yes | Triggers unchanged and complete for the four records (tool, test, fixture, interpreter, git, defect); TV-010 adds `render_risk.py` as an import |

## F. Accreditation readiness, schedule and indexes

| Id | Answer | Evidence |
|---|---|---|
| TV-F1 | Yes, with finding-2 | Each proposed extension names purposes, blob, commit, interpreter, imported blobs (ACC-TREND-001 now names `validate_docs.py` `e5b692e1`, closing the F-10 binding for this tool) and "for runs after the CR-014 merge"; ACC-FIGS-001 covers purpose 3 wider than its seeded faults (finding-2) |
| TV-F2 | Yes | Due gates unchanged (TV-003, 007, 010 SRR; TV-012 CDR; TV-013 PDR); first cited uses precede no due date |
| TV-F3 | Yes | README index, lock section 5 and record headers agree on "Accredited, extension proposed" (TV-003, 007, 010), "ACC-COMPLEXITY-001 effective, extension proposed, F-13 with the owner" (TV-012), "pending" (TV-013). The older leading text of the TV-012 lock row is kept with dated updates, as the lock's append practice does |
| TV-F4 | Yes | Each section 9 leaves the decision to the owner after section 8 and states the accredited blob on `main` stays in force until the merge |
| TV-F5 | No | finding-3 |

## G1. Repository tools

| Id | Answer | Evidence |
|---|---|---|
| TV-G1-1 | Yes | `RepositoryTests` classes separate in `test_validate_docs.py` and `test_render_review_figures.py`; the TV selections exclude them |
| TV-G1-2 | Yes | Exit 0, 1 and 2 of each tool have known answers (`UsageErrorTests`, `CliTests`, `RunTests`, `UsageTests`, `measurements` usage); the new exit 1 of a failed fold check is `test_a_layout_failure_exits_one_and_writes_nothing`. `sw_gate.sh` G0 fatal paths: V5 |
| TV-G1-3 | Yes | Appended below (Code review) at the same blobs |

G2, G3 and G4: N/A (repository tools).

## H. Software assurance tasks

| Id | Answer | Evidence |
|---|---|---|
| TV-H1 | Yes | swe-136 7.1 task 1: the gate tools changed (`complexity_gate.py` G5, `measurements.py` G2, G3, G6, `sw_gate.sh` G0) keep purposes that cover the 07 section 8.4 steps citing them; G0 export mode has a known answer (V5) though `sw_gate.sh` itself has no TV record (due CDR, lock section 5) |
| TV-H2 | Yes | swe-070 7.1 task 1: `render_review_figures.py` and `review_trend.py` are review-evidence tools, not qualification analysis tools; their purposes cover the package figures that cite them; no analysis note cites them |
| TV-H3 | Yes | `assurance_tasks_applied` lists both tasks; the separate SA pair is X-1 |

## Code review (TV-G1-3; `peer-review-checklist-code.md` revision B applied to host Python and shell, as INSP-042 did)

Scope: the diffs `7bb994f..367b3dd` of `tools/validate_docs.py` (65 lines), `tools/review_trend.py` (96), `tools/render_review_figures.py` (999), `tools/complexity_gate.py` (4), `tools/measurements.py` (27), `tools/sw_gate.sh` (40) and `firmware/cwht-app/src/main.rs` (10, comment only), with their test modules.

| Id | Answer | Evidence |
|---|---|---|
| R1 to R4, R6 | N/A | Rust gate, design unit, `@req` and unsafe rules; `main.rs` is comment-only (V7 rustfmt, V4 CC unchanged) |
| R5 | Yes | Test modules exist and pass (V1, V11) |
| CK-CODE-A1, A3, B1 to B8 | N/A | Host Python and shell; `main.rs` unchanged apart from the comment |
| CK-CODE-A2 | Yes | New imports are standard library (`tempfile`, `dataclasses`) and matplotlib already locked; `render_risk` is TV-006; no `tools/requirements.txt` change (V6) |
| CK-CODE-C1, C2 | Yes (adapted) | Fold errors become `FigureDataError` (exit 1) and render into a temporary folder, moved only when all succeed (`run`; targeted mutant V1); `export_tree` in `sw_gate.sh` prints nothing on any git error, which G0 treats as a mismatch (fail-safe); `date_ticks` raises on a reversed range (tested) |
| CK-CODE-C3 to C7 | N/A | Rust rules |
| CK-CODE-D1, D3 to D9 | N/A | SWE-220 and target rules apply to 07 section 14.1 components |
| CK-CODE-D2 | Yes | No recursion added; loops over finite lists (texts, edges, days) |
| CK-CODE-E1 | No | Checked item by item against the source findings: C-172 header "first" (INSP-015 F-08), done; C-173 single iteration read whole and `finding_key`, done, "Findings" read wherever it stands only for the exact heading (finding-1); C-186 `ASSURANCE_WHOLE_PRODUCTS` adds 05 and TS-002 as the 07 section 2.1.1 software plans row names them, and `SW-SYNTH` moves to the safety-critical tuple as the 07 section 22 "Tool constants" row directs on decision 9 concurrence (SRR memo decision 9: "Concur, with frequency control safety-critical"); the menu module waits for WP-PDR-32 as the plan says; C-170 RID-SRR-004 each requested element (labels once, single-date rise and marker, closed label off the axis, known answer, re-render) done; C-072 RID-SRR-014 option 1 (fold with known answers, re-render) done; C-203 floor 14.5 pt held by both slide layouts; C-204 footer quoted from the package; C-175 `code[k - 1] != "="` finds the binding after `>` and still skips `==` and `=>` (a `..=` range pattern before the binding was mis-read before and after the change; no such statement exists in the gate's input, V4); C-185 every result line prefixed; C-179 export mode compares the whole export tree with the lock value (V5, including the outer-repository case); C-178 comment cites CR-001 Approved and the amended CS-11 with the `CR: CR-001` trailer (`f924595`) |
| CK-CODE-E2 to E8 | N/A | Firmware rules |
| CK-CODE-E9 | Yes | Every new function is called: `findings_sections`, `finding_key` from the record rule; `date_ticks`, `series`, `marker_indices`, `end_label_offsets` from `figure`; fold functions from `FIGURES`; `result_line` from every mode; `export_tree` from G0 |
| CK-CODE-F1 to F3 | N/A | Rust tags; each new function's docstring cites its finding or RID |
| CK-CODE-G1 | Yes (adapted) | Subprocess calls take argument lists; `sw_gate.sh` quotes every variable in the new block and deletes its temporary repository |
| CK-CODE-G2 to G5 | N/A | Firmware rules |
| CK-CODE-H1 | Yes | Tests run on fixtures and temporary folders; the pixel test reads the committed SRR render |
| CK-CODE-H2 | Yes (adapted) | Tests are the tool author's, accepted for known answers by 05 section 9.2; independence comes from this record and the SA pair |
| CK-CODE-H3 | N/A | No safety-critical decision table |
| CK-CODE-I1 | Yes | Module and function docstrings updated with the behaviour (validate_docs header, `measurements.py` "Output lines", `render_review_figures.py` header, `sw_gate.sh` G0 header) |
| CK-CODE-I2, I4 | Yes | Names carry their rule; comments give reasons (the `complexity_gate.py` comment on why `<=`, `>=`, `!=` cannot occur); no commented-out code |
| CK-CODE-I3 | N/A | Rust fmt and clippy; `main.rs` rustfmt clean at edition 2024 (V7) |
| CK-CODE-J1 | Yes (adapted) | Every `validate_docs`, `render_risk` and matplotlib symbol used exists at the named blobs and versions (V1 imports) |
| CK-CODE-J2 | N/A | Rust traits |
| CK-CODE-J3 | Yes | RID-SRR-004 and RID-SRR-014 compound requests implemented in full (CK-CODE-E1) |
| CK-CODE-J4 | Yes | Sizes measured with `git diff --stat 72d0a2f 367b3dd` and `wc -l` |

## Record verdict

`reviewer_verdict: APPROVED`: zero Major findings, three Minor findings (finding-1 to finding-3), each a lien due at the CDR readiness declaration under plan rule C1 unless the tool owner fixes it on the CR-014 branch before the merge. `verdict` stays `NEEDS CHANGES` for two reasons outside this lens: the software assurance pair is pending (X-1), and every reviewed tool blob exists only on the unmerged branch `cr/CR-014-tool-liens-srr` (lead SE convention of 2026-09-27). The record verdict is set in the CR-014 merge commit, or the commit right after it, when the blobs reach `main` unchanged and the pair is APPROVED. After this record is filed, the TV record author writes section 8 of TV-003, TV-007, TV-010 and TV-012 (and TV-013 through INSP-041), and a reviewer invocation re-issues this record as a delta naming the new blobs (TV template, Record paragraph).

```
VERDICT: APPROVED (reviewer lens); record verdict NEEDS CHANGES until the SA pair and the CR-014 merge
PRODUCT: TV-003, TV-007, TV-010, TV-012, TV-013 and the CR-014 tool changes at 367b3dd (CR file eb200de)
FINDINGS:
- [Minor] TV-E1, CK-CODE-E1 tools/validate_docs.py FINDINGS_HEADING: only the exact heading "Findings" is read before the latest iteration; the template heading form is not (INSP-042 would fail rule (d) at its merge).
- [Minor] TV-B3, TV-C2 TV-010 purpose 3: most listed layout checks have no seeded failing known answer (reviewer probes show they work).
- [Minor] TV-F5 TV-003, 007, 010, 012: re-validation inside the existing record for a changed accredited blob; same owner ruling as INSP-043 finding-2.
ITEMS N/A: TV-A2, TV-D3 (class B), G2 to G4 (repository tools); code R1 to R4, R6, A1, A3, B1 to B8, C3 to C7, D1, D3 to D9, E2 to E8, F1 to F3, G2 to G5, H3, I3, J2
RE-RUN: evidence procedure on an export of 367b3dd, base 7bb994f; exit 0; 285 tests per pass, twice; mutation and targeted mutants all fail as required; equal to runs 7, 4, 5, 4, 4
MEASUREMENTS: size=5 records, 26 purposes, 7 changed files; turns=82; minutes=120; major=0; minor=3
```
