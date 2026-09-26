---
# Peer-review record (charter section 5; 01 section 13; 08 section 3.2). Copy of
# docs/templates/peer-review-checklist-requirements.md revision C, product type "plans and process
# documents" (section G and A8). Slug software-plan-07 as assigned by the dispatching session
# (01 section 4.6 and 07 section 10.2 give plan-07-software-engineering-plan; see Observations O-1).
id: INSP-010
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/software-plan-07.md
product: docs/process/07-software-engineering-plan.md
# product_commit: HEAD, the base of the reviewed working tree (07 last committed at 4e3f891 and modified
# since, revision A.3; docs/plan/measurements.json is untracked). Reviewed content is the two blobs below.
product_commit: "28e49e6e48ce02d6827e2cc015621900dccc2d1d"
# product_blob: git hash-object of each reviewed file. Iteration 1 (2026-09-25): 07 1b8864b0121f3f8547e1b194d63b41752ab946b9,
# measurements.json 9bb5989e7080c55e8c97d82e64256a07f9b8788f (07 revision A.3, 960 lines; 47 records).
# Iteration 2 (2026-09-26, values below): 07 revision A.4 and the 2026-09-26 append, both still uncommitted on HEAD 28e49e6.
product_blob: "eba15bcb8ab0cecfd8bc155bd749bc89fdcddb34"
product_second: docs/plan/measurements.json
product_second_blob: "5e2d1755c6ad43d1c3cdf6fae0ff0edbfeb7346b"
product_size: 07 revision A.4, 23 sections and annexes A to D, 1007 lines; measurements.json 89 records (62 current after supersession)
sprint: SRR-prep
author_agent: author:software-plan (Claude software lead; revision A.3 of 2026-09-25, SRR items H14 07 part and H16 SWE-089)
reviewer_agent: reviewer:software-plan
criticality: safety-critical
# assurance_required: true; 07 section 2.1.1 row "Software plans" is Yes in every column (the plan is
# the software assurance plan and software safety plan, NPR 7150.2D 6.1 items k and l)
assurance_required: true
# assurance_reviewer_agent: the distinct invocation that filed the paired assurance record INSP-018
# (docs/reviews/SRR/checklists/software-plan-07-software-assurance.md; 07 section 10.2 paired form).
# assurance_verdict below is copied from INSP-018 as read on 2026-09-26.
assurance_reviewer_agent: "sa-reviewer:software-plan (paired assurance record INSP-018)"
paired_record: INSP-018
iteration: 2
# readiness_met: false because R1 still fails at iteration 2 (measurements.json has no schema) and R3
# (author self-check against sections A to G) was again supplied as a per-finding response only; see Readiness
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
verdict: NEEDS CHANGES
findings_major: 2
# counts cover iterations 1 and 2: finding-14 (Minor) is new at iteration 2; open = finding-2 (Major), finding-14
findings_minor: 12
findings_open: 2
findings_fixed: 12
findings_verified: 12
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no at iteration 2 (iteration 1: G1, G2, G3, G4, G6, G7)
items_no: [CK-REQ-G6, CK-REQ-G7]
# effort cumulative: iteration 1 42 turns, 55 min; iteration 2 24 turns, 35 min
effort_turns: 66
effort_minutes: 90
record_status: Open
date: 2026-09-25
date_updated: 2026-09-26
date_closed: null
---

# Peer review record INSP-010: Software Development and Management Plan (07) and the measurement repository

**Products:** `docs/process/07-software-engineering-plan.md` revision A.3 (working tree on HEAD `28e49e6`, blob `1b8864b0121f3f8547e1b194d63b41752ab946b9`; last commit touching it `4e3f891`) and `docs/plan/measurements.json` (untracked, blob `9bb5989e7080c55e8c97d82e64256a07f9b8788f`), reviewed as one product. **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G (CK-REQ-G1 to G8) and CK-REQ-A8, per 08 section 3.1 "plans and process documents" and 07 section 10.1 row b. **Minimum content judged:** SRR entrance row 23 (`docs/process/01-lifecycle-and-reviews.md` section 4.3: "Software plans (preliminary) covering the life cycle with approved tailoring", SWE-013, SWE-033, SWE-037; evidence "Plan outline; acquisition-vs-development record; software review milestones", Hard), the NPR 7150.2D chapter 6 records (section 6.1 items a to y) and 01 section 4.6 rows SWE-013, SWE-033, SWE-037, SWE-087 b, SWE-089. **SRR context:** package `docs/reviews/SRR/package.md` section 2 items H1 (07 record), H14 (07 section 14 reconciliation, SWE-033 trade study) and H16 (SWE-089 measurements file).

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: section G plan items and the 07 record; hazard analysis section 6.2 determination and the union rule). The tool was available. `grep -n`, `sed -n` and read-only Python over the JSON files were used afterwards only to pin the lines and values the hits and the product pointed at.

**Independence.** The reviewer did not author 07, `measurements.json` or any file they cite, and edited none of them. This record is the file review; the software assurance second review that 07 section 2.1.1 requires for a software plan (SWE-013; the plan is also the 6.1 item k and l record) has not been performed, and the record cannot reach `verdict: APPROVED` until that reviewer returns `APPROVED` (07 section 10.2 completion criteria).

## Findings

Severity: Major blocks the baseline; Minor is fixed before the next review. Iteration 1 (2026-09-25) filed all findings Open. Iteration 2 (2026-09-26, same reviewer role, new invocation) re-read the corrected product and filled State and Disposition: Verified with the closing evidence, or Open with the reason (01 section 10.1; 07 section 10.2 action tracking).

| Finding | Severity | Item | Location | Description and expected fix | State | Disposition |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>F-01 (finding-1) | Major | CK-REQ-G4, CK-REQ-G1 | 07 section 22 first paragraph ("SWE-174, SWE-094, SWE-045 (institutions)"); section 11.3 last sentence ("SWE-094 (access for NASA organizations) is not applicable") | 07 states that SWE-045 and SWE-094 are rows "dispositioned T or NA in `docs/process/rmm.json`". The RMM has both as `FC`: SWE-045 (5.1.9) "The owner, in the acquirer role ... participates in the functional and physical configuration audits at SAR", SWE-094 (5.4.4) "The owner ... has direct access to `docs/plan/tpm.json`, to `docs/plan/measurements.json` ...", status In place. The charter tailoring register was changed at commit `4e3f891` to drop "Center reporting (SWE-094, ...), joint audits (SWE-045)" from the Not applicable row (`git diff b8214ca 4e3f891 -- docs/process/00-charter.md`); `render_rmm.py --check` lists T and NA rows without either id. The plan misstates two Class A dispositions, which charter sections 1 and 11 rule 5 permit only through the RMM, and the 07 header rule ("Where this plan and `rmm.json` disagree, the RMM row ... governs and this plan is corrected") is violated in the plan itself. Same defect class as INSP-006 finding-1 (05, Major). Fix: remove SWE-045 and SWE-094 from the section 22 list; rewrite the section 11.3 sentence as fully compliant, citing the owner's direct access to the repository and `measurements.json` (RMM SWE-094). | Verified | Closed. 07 section 22 preamble now states SWE-045 and SWE-094 are fully compliant and not tailored; neither id is in the 25-row mirror. Section 11.3 last sentence reads SWE-094 fully compliant (`rmm.json` SWE-094, 5.4.4, In place) with the owner's direct access. `rmm.json` has both FC (read 2026-09-26). |
| <a id="finding-2"></a>F-02 (finding-2) | Major | R1, CK-REQ-G6 | `docs/plan/measurements.json`; 07 sections 11.1 and 22 row "Measurements schema and tool rows" | The product fails the gate validator: `tools/validate_docs.py` exit 1 with `FAIL docs/plan/measurements.json (schema: docs/plan/measurements.schema.json) - schema not found`, and the same failure makes `test_validate_docs.RepositoryTests.test_repository_exit_zero` fail (`unittest discover -s tools/tests`: 331 run, 1 failure). 07 section 11.1 acknowledges this and defers the schema to "the same commit as the first commit of the measurements file"; until then the file cannot be committed, cited as SRR evidence (package H16, H17) or enter `baseline/srr` without an unlogged validator failure. Fix: the tool owner writes `docs/plan/measurements.schema.json` encoding the section 11.1 field table and rules (required fields, `state` enum, `value` null when Not yet measured, `evidence` required when Measured with the `<path> sha256=<64 hex>` form, `credit` false when Not yet measured, `due` required when Not yet measured, `assessment` enum), with a known-answer fixture, and re-runs `validate_docs.py` to exit 0 on the file. | Open | Open. 07 section 11.1 now names the schema content, fixture and commit rule (fixed in the plan), but `docs/plan/measurements.schema.json` does not exist in the repository; a scratchpad draft is not evidence. Re-run 2026-09-26: `validate_docs.py` exit 1 with `FAIL docs/plan/measurements.json ... schema not found`, and `unittest discover` 335 run, 1 failure (`test_repository_exit_zero`). Closes when the tool owner commits the schema and fixture and both commands exit 0 (07 section 22 row 'Measurements schema and tool rows'). |
| <a id="finding-3"></a>F-03 (finding-3) | Minor | CK-REQ-G6 | `measurements.json` record MSR-05 (`note`) | The note reads "No record has reached APPROVED at this snapshot (10 records, all NEEDS CHANGES)". The seed's own MSR-20 evidence contradicts it: the MSR-20 records name `docs/reviews/SRR/checklists/semp.md` and `trade-studies-ts-001-ts-002.md` with sha256 values that equal those files today (recomputed 2026-09-25), and both carry `verdict: APPROVED`, `iteration: 2` (INSP-005, INSP-013). By 07 section 10.3 ("MSR-05 when a record reaches `APPROVED`") MSR-05 should be `Measured` for those two scopes with value 2. Fix: append MSR-05 records for INSP-005 and INSP-013 (value 2 each) and a corrected note, per the append-only rule with `supersedes`. | Verified | Closed. `measurements.json` appends MSR-05 `INSP-005 docs/plan/semp.md` value 2 (supersedes the seed Not yet measured record and corrects its note) and MSR-05 `INSP-013 docs/decisions/trade-studies/` value 2. |
| <a id="finding-4"></a>F-04 (finding-4) | Minor | CK-REQ-G6 | `measurements.json` records MSR-01, 03, 04, 06, 20, 21, 23, 27; 07 section 11.1 `commit` row and the re-derivation sentence | (a) 23 of the 32 Measured records name evidence that is not in commit `28e49e6` (untracked checklists, sw-keyer and sw-tool test cases, `TC-SW-TOOL-001-r1.md`), yet their notes do not say "working tree", which the section 11.1 `commit` row requires; only the MSR-07, 10, 13, 18 and 19 notes do. (b) MSR-01, 03 and 04 cite `docs/vv/traceability.json sha256=ab6d5345...`, which equals neither the blob at `28e49e6` (sha256 `9e90c865...`) nor the current working file, so the section 11.1 known-answer test ("re-derives the seed's `Measured` records from the evidence files as they stand at the seed's commit") cannot be run for them. The values themselves still agree with the current file (33 Draft, 8 TBR, 0 and 0). (c) MSR-03 is assessed Green against "Must be 0" although two of its four sub-measures (design units without `@design`, functions without `@req`) are null in the source. Fix: add "working tree" to the affected notes by superseding records; state in 11.1 how untracked evidence is preserved for the re-derivation (for example commit the evidence with the seed, or store a copy under `docs/vv/reports/`); assess MSR-03 Not assessed or state the partial scope. | Verified | Closed. (a) Every current Measured record whose evidence is untracked says 'working tree' in its note (checked by script over the 62 current records). (b) MSR-01, 03 and 04 superseded with `traceability.json sha256=e796e0f6...`, which equals the file on 2026-09-26 after a `traceability.py` run; 11.1 adds the evidence-preservation rule (commit with the record, frozen `docs/reviews/<REVIEW>/traceability.json`, mismatches reported not skipped). (c) MSR-03 superseded as Not assessed with the partial scope stated. |
| <a id="finding-5"></a>F-05 (finding-5) | Minor | CK-REQ-G4 | 07 section 22 first paragraph, last sentence | "Their rationale is in the RMM and is not repeated here." The RMM row SWE-121 (3.1.12, FC) implements the requirement as: every T or NA row "is mirrored, with its rationale and residual risk, into `docs/process/07-software-engineering-plan.md` section 22". The plan and the RMM disagree on how SWE-121 is met. Fix: mirror rationale and residual risk per row in section 22 (a table), or have the 03 author change the RMM SWE-121 text to a list-with-reference mirror (cross item) and cite it. | Verified | Closed. 07 section 22 mirrors all 25 T and NA rows with relief, residual risk and plan location; the set and dispositions equal `rmm.json` (script: 25 vs 25, no difference); the RMM text governs any difference. |
| <a id="finding-6"></a>F-06 (finding-6) | Minor | CK-REQ-G1 | 07 section 14.1 first paragraph ("its re-transcription from 0.3.0-pha is the 03 author's item ... until it lands"); scheduler row ("03 section 4.3 records a, c until its re-transcription"); drivers row ("which gains ... at its re-transcription"); section 22 rows "Safety-critical list outside this plan" and "OQ-SAF-022 status" | Stale against the files of 2026-09-25: 03 is re-transcribed from 0.3.0-pha (03 status line; its section 4.3 scheduler row reads a, b, c, e and its drivers row names clocks and PLL), OQ-SAF-023 is Closed and OQ-SAF-022 Answered at `hazards.json` 0.4.0-pha, and `hazard-analysis.md` section 11.1 item 2 asks the 07 author to remove "two stale notes in 07 section 14.1". 07 also cites `hazards.json` 0.3.0-pha while the file is 0.4.0-pha; the reviewer recomputed the union from 0.4.0-pha (every hazard's `firmware_role.components`, `criteria`, `swe134_items`) and it equals the section 14.1 hazard lists and criteria, as `hazard-analysis.md` section 6.2 states, so only the version citation is stale. Fix: delete the three notes and the two section 22 rows (or mark them done), and state "0.3.0-pha, unchanged in firmware role at 0.4.0-pha". | Verified | Closed. The three 14.1 notes are gone (no hit for the stale phrases); 14.1 and 14.2 cite `hazards.json` '0.3.0-pha, unchanged in firmware role at 0.4.0-pha'; the two section 22 rows are removed and recorded as closed in the open-items preamble. |
| <a id="finding-7"></a>F-07 (finding-7) | Minor | CK-REQ-G1 | 07 section 14.1 first paragraph ("03 section 4.3 records the same determination"), safe-state manager and scheduler rows; section 1.2 `cwht-core` row and CS-38 | 03 section 4.3 (lines 137 and 138, and the "Type (ii) findings for HZ-008" paragraph) lists HZ-008 for the safe-state manager and for the scheduler and runtime by type (ii) finding (proposed with decisions 9 and 40); 07 section 14.1 lists neither, so the two records are not "the same determination". 03 also places `SW-SCHED` "in `cwht-app`: main-loop queue, task dispatch and period supervision", whereas 07 section 1.2 puts the dispatcher, tick accounting, overrun detection and kick decision in `cwht-core` and CS-38 forbids decisions in `cwht-app`. Charter section 10 makes 07 section 14.1 the single authoritative list, so the difference must be carried somewhere. Fix: add "HZ-008 (type (ii), proposed; 03 section 4.3)" to the two hazard cells, or list the difference in section 22 for the 03 author; carry the `cwht-app` wording to the 03 author (cross item). | Verified | Closed. 14.1 SW-SAFE and SW-SCHED hazard cells add 'HZ-008 by type (ii) finding (proposed ...)'; the SW-SCHED location difference is the section 22 row '03 alignment with section 14' for the 03 author. |
| <a id="finding-8"></a>F-08 (finding-8) | Minor | CK-REQ-G7 | 07 section 8.1 paragraph after the table ("The lock still lacks the pinned nightly ... its `cargo-miri` row says 'Not permitted (would need CR)'") | False against `tools/toolchain.lock.md` today: line 20 is the `nightly-2026-08-24 (date-pinned)` row with `rustc 1.100.0-nightly (fb6531d55 2026-08-23)` and its components; line 19 makes the floating nightly "Not permitted for any use"; line 33 says Miri runs only on `nightly-2026-08-24`. 07 section 22 row "Toolchain lock rows" already says these rows exist, so the plan contradicts itself. Versions verified by running the commands on 2026-09-25: `rustc 1.98.0 (88d9e12ae 2026-08-18)`, `rustc 1.100.0-nightly (fb6531d55 2026-08-23)` with no `miri` or `llvm-tools` component, `cargo-llvm-cov 0.9.1`, `cargo-audit-audit 0.22.2`, `cargo-deny 0.20.2`, `cargo-geiger 0.13.0`, `cargo-nextest 0.9.146 (8af696ddc 2026-09-21)`, `picotool v2.3.0`, `rust-code-analysis-cli` not found; all equal the plan and the lock. Fix: reword the sentence to what remains (install `miri` and `llvm-tools` on the pinned nightly; add the `rust-code-analysis-cli` version in FW-B0). | Verified | Closed. 07 section 8.1 paragraph now matches `tools/toolchain.lock.md` lines 19, 20 and 33 and states what remains for FW-B0 (miri, llvm-tools on the pinned nightly; rust-code-analysis-cli version). A new wrong row reference in the same paragraph is finding-14. |
| <a id="finding-9"></a>F-09 (finding-9) | Minor | CK-REQ-G1, CK-REQ-G2 | 07 header ("Aligned to: charter at commit `b8214ca`"; "Charter section 1 records 268 pages"); section 13 last paragraph ("the ten steps of `docs/process/05-configuration-and-data-management.md` section 8.1") | The charter changed at `4e3f891` (SWEHB now "267 files, 130 of them SWE pages"; the SWE-045 and SWE-094 tailoring removed, finding-1; SWE-211 row added), so the alignment statement names a superseded charter and the "268 pages" claim is false (charter line 14). 05 section 8.1 has 12 numbered steps, not ten (counted 2026-09-25; also INSP-006 observation O-4). Fix: re-align to the current charter commit and correct both counts. | Verified | Closed. Header aligned to charter `4e3f891` (the last commit touching the charter, `git log`) with 267 files and 130 SWE pages; section 13 says twelve steps, and 05 section 8.1 has 12 numbered steps (counted 2026-09-26). |
| <a id="finding-10"></a>F-10 (finding-10) | Minor | CK-REQ-G3 | 07 section 2.1.1 table; section 17.2 | Section 2.1.1 is "the single rule for dispatching the software assurance reviewer", and it has no row for trade studies or ADRs. Section 17.2 says TS-002 (make/buy of the runtime and HAL, whose drivers are in the safety-critical call path of section 14.1) has "its independent review with the software assurance function pending". Consequence observed: INSP-013 set `assurance_required: false` citing the missing row, while the TS-002 header asks for an assurance reviewer; SRR row 23 needs the SWE-033 record. Fix: add a row (trade studies and ADRs whose decision constrains a safety-critical or mission-critical component: Yes), or correct section 17.2 to match the table. | Verified | Closed. 2.1.1 'Software plans' row names 05 and TS-002 with the swe-013 basis; new row routes trade studies and ADRs constraining safety-critical or mission-critical components (Yes, Yes, No); 10.1 row b and 17.2 agree; dispatch of the 05 and TS-002 assurance reviews is a section 22 row. |
| <a id="finding-11"></a>F-11 (finding-11) | Minor | CK-REQ-G2 | 07 section 21 preamble and rows; section 16.2 column 4; section 1.3 row r | Section 21 says "rows without an id are opened at SRR", but the register already holds RSK-019 (complexity tool mis-measures Rust 2024 code), RSK-021 (flash write hangs with XIP disabled) and RSK-063 (host mock diverges from the RP2350), which the rows "Complexity tool staleness", "Flash write path" and "Host mock diverges from silicon" do not cite; "Toolchain not qualified" and "Single maintainer of rustos" have no register entry. Section 16.2 gives "5x5 inputs for `RSK-NNN` tagged `cyber`" but cites only RSK-015, although RSK-022, RSK-060, RSK-061 and RSK-062 (all tagged `cyber`) match the debug, key-line, diagnostic and supply-chain rows. Section 1.3 row r says software risks are "tagged `software`", but RSK-003, 010, 013, 019, 021 and 063 carry no tags. Fix: cite the existing ids in both tables, open or explicitly decline the two missing risks, and have the risk owner add the `software` tag (cross item). | Verified | Closed; part disputed and the dispute accepted. RSK-019, 020, 021, 023 and 063 are cited in section 21, RSK-015, 022, 060, 061 and 062 per row in 16.2, and the `software` tag is a section 22 row for the risk owner. Dispute: `docs/risk/register.json` holds RSK-020 'Upstream rustc miscompiles a safety-critical construct for Cortex-M33' and RSK-023 'rustos upstream change breaks cwht firmware undetected', present already at commit `28e49e6`; this reviewer's claim that the two risks had no entry was wrong. |
| <a id="finding-12"></a>F-12 (finding-12) | Minor | CK-REQ-G4 | 07 section 22 open-items table (only an RMM SWE-089 row) | The RMM SWE-090 (5.4.2) implementation reads "`docs/plan/tpm.json`: requirement count and volatility, test pass rate, coverage, complexity, defect counts ...", while 07 section 11.1 makes `docs/plan/measurements.json` the SWE-090 repository with a TPM mirror. The RMM SWE-094 text says the first `measurements.json` records are "Planned for PDR: first records at the FW-B1 sprint closures", while the SRR seed exists. Section 22 lists the SWE-089 mismatch but not these two. Fix: add section 22 rows for RMM SWE-090 and SWE-094 (03 author). | Verified | Closed. Section 22 row 'RMM rows SWE-089, SWE-090 and SWE-094' carries both texts to the 03 author; the quoted RMM texts match `rmm.json` (read 2026-09-26). |
| <a id="finding-13"></a>F-13 (finding-13) | Minor | CK-REQ-G1 | 07 section 14.2 row i, L1 column | The column is defined as "the `REQ-SYS` requirements that `hazard-analysis.md` section 7 names for the row". 07 lists REQ-SYS-181 for row i; `hazard-analysis.md` section 7 row i lists REQ-SYS-055, 071, 083, 092, 119, 120, 180, 182 and its provision text does not mention the hardware over-temperature cut-off. The 07 content is the more complete (REQ-SYS-181 is an independent-of-firmware limit, HZ-003 K9), but the column no longer does what its definition says. Every other row's L1 column equals section 7 (checked rows a to l). Fix: either keep 181 and mark it "07 addition, for the hazard analysis author" in section 22, or remove it. | Verified | Closed. 14.2 row i keeps REQ-SYS-181 marked as a 07 addition; the column definition in the 14.2 preamble covers such additions; section 22 row 'Hazard analysis follow-ups' item (2) carries it to the hazard analysis author. |
| <a id="finding-14"></a>F-14 (finding-14) | Minor | CK-REQ-G7 | 07 section 8.1 paragraph after the table ("`tools/toolchain.lock.md` rows 21 to 25 already list `cargo-llvm-cov`, `cargo-audit`, `cargo-deny`, `cargo-geiger` and `cargo-nextest`") | Found at iteration 2. In `tools/toolchain.lock.md` those five tools are on file lines 24 to 28 (section 1 table data rows 14 to 18); lines 21 to 25 hold `llvm-tools`, the cargo-installed inventory, `cargo-llvm-cov` and two others, so the reference points at the wrong rows. Fix: cite the rows by tool name (or by the correct line numbers) instead of by position. | Open | Open (new at iteration 2). |

## Readiness criteria (all true before the review starts)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Not met | Run 2026-09-25: `validate_docs: 30 passed, 3 failed, 33 checked`, exit 1. Failures: `docs/plan/measurements.json` (schema not found; this product, finding-2), `docs/design/allocation.json` (schema not found) and `docs/reviews/SRR/checklists/risk-register-06.md` (APPROVED with an open Major); the last two are outside this product. 07 is Markdown and is not schema-validated. |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | Met | `traceability.py --report-only` exit 0: "231 requirements, 167 test cases, 0 violation(s), 2 warning(s)" (SYS_UNALLOCATED REQ-SYS-125, REQ-SYS-148; not 07 ids) |
| R3 | Author self-check against sections A to G and the brief's acceptance criteria | Not met | The assignment carried an author summary of the changes made for H14 and H16 (a change list with citations checked against the corpus), not a self-check against CK-REQ-A8 and G1 to G8. `readiness_met: false` records it; the review was held at the dispatching session's direction. |
| R4 | Every `TBR` has owner, plan, close_by; no `TBD` | Met | No "TBD", "as appropriate" or "should consider" in 07 or `measurements.json` (grep, no hit); every TBR the plan quotes belongs to a cited L1 requirement, whose `tbr` object carries owner, plan and close_by (section 14.2 preamble); no em dash in either file |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

## Participants

Author agent `author:software-plan` (not present). Reviewer agent `reviewer:software-plan` (this record). Software assurance reviewer: required by 07 section 2.1.1 (software plans: Yes); not dispatched at iteration 1; filed at iteration 2 as the paired assurance record INSP-018 (`sa-reviewer:software-plan`). Owner: disposition of the findings at the review.

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A8 | Yes | Identifiers and terms match charter sections 5 and 6 (`REQ-SW-<SUB>-NNN`, `TC-SW-<SUB>-NNN`, `SW-NN-<module>`, `INSP-NNN`, `CS-NN`, `MSR-NN`, `WP-SW-NN`, `ACC-EMU-001`, `FW-vX.Y.Z` of 05 section 4.3); Annex D defines the plan-specific terms; `measurements.json` uses the 11.1 field names exactly (all 47 records checked by script: every required field present, no extra field, `state` and `assessment` in their enums, every Not yet measured record with `value: null`, `credit: false`, a `due` and `Not assessed`, every Measured record with evidence, no `credit: true`). |

ITEMS N/A: CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 and the per-requirement validation table (the product is a plan and its measurement repository, not a requirement file or CR; checklist product-type row "Plans and process documents").

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Expands charter section 10 consistently: SWE-057/058 (section 5), coding standard with clippy, unsafe audit, complexity (section 7), repeatable unit tests with measured coverage (9.2, 9.5), regression (9.3), SWE-134 a to l for the charter's component list (14.2), MC/DC tailoring with the nightly MSR-14 as required non-credit measure (CS-03, 9.6), CC 15 (CS-17), peer review with checklists (10), VDD (13), NCRs (12), traceability (CS-24). Section 14.1 hazard lists and criteria equal the union recomputed from `hazards.json` 0.4.0-pha. Section 14.2 numbers equal `hazard-analysis.md` section 7 and the cited L1 statements (REQ-SYS-004 20 ms TBR, 009 144.001 to 147.999 MHz, 020 5.5 s, 048 2 ms, 052 500 ms, 053 5 s, 054 128 or 10 s, 055 7.5 to 13 s, 097 3.20 V, 118 85 C and 100 ms, 131 2 s, 155 -20 to +150 C, 162 5 ms, 180 180 s, 181 95 C, 182 10 kHz; read from `docs/requirements/sys/requirements.json`). Disagreements: finding-1 (RMM and charter), finding-6 and finding-7 (03 and the hazard analysis), finding-9 (charter commit, 05 step count), finding-13 (section 7 row i). |
| CK-REQ-G2 | No | Procedure steps name artifacts, paths and id schemes (sections 3.4, 8.4, 10.2, 11.1, 13; Annex C); open decisions name owner and gate (section 22, package decisions 9, 36 to 41). Defects: finding-11 (risk ids not named although they exist), finding-9 (wrong step count). |
| CK-REQ-G3 | No | Roles, independence and approval points are stated (section 2.1 with SWE-039 insight, 2.1.1 dispatch table, 1.3 owner-action column, 3.2 exit criteria, 10.2 completion; SWE-013 plan content via 1.4 item 1 and 11). Gap: finding-10 (no dispatch row for make/buy trade studies touching safety-critical drivers). |
| CK-REQ-G4 | No | Section 22 mirrors every T and NA row of `rmm.json` (25 rows: SWE-015, 016, 017, 018, 022, 023, 027, 032, 046, 131, 141, 143, 147, 148, 151, 154, 156, 157, 159, 174, 178, 179, 210, 211, 219; compared by script with `render_rmm.py --check` output "T=17, NA=8"). Defects: finding-1 (two FC rows listed as tailored), finding-5 (SWE-121 mirror form), finding-12 (RMM SWE-090 and SWE-094 texts). |
| CK-REQ-G5 | Yes | Section 16: assets (image, configuration, inputs, debug, diagnostics, supply chain), surfaces, threats, 5x5 inputs, mitigations tied to CS-29 to CS-33 and SWE-134 d, g, i, j; verification cases `TC-SW-BOOT-*`, `TC-SW-CFG-*`, `TC-SW-KEYER-*`, `TC-SW-DIAG-*` and gate G5 in the regression set (16.4, 9.3); privacy (16.6). Register ids missing from the table are finding-11, not a G5 gap. |
| CK-REQ-G6 | No | Catalog 11.2 gives source, unit, collection point and rule for MSR-01 to MSR-28; analysis procedure 11.3 (SWE-093) and record format 11.1 (SWE-090). The seed has one or more records for every MSR; its 20 MSR-20 and MSR-21 values equal the front matter of the ten records they name (checked field by field; MSR-22 numerator 118 equals the sum); MSR-06 Yellow and MSR-10 Red notes carry the corrective action (package H12, OQ-SW-001). Defects: finding-2 (no schema; validator fails), finding-3 (MSR-05 false note), finding-4 (working-tree provenance, unreproducible hashes, MSR-03 assessment). |
| CK-REQ-G7 | No | Tool versions verified by running the commands (finding-8 lists them; all equal the plan and `tools/toolchain.lock.md`). Honest limits are stated: no MC/DC for Rust (8.1, 9.6), Miri cannot run MMIO (8.1), emulation never carries timing (9.4), `rust-code-analysis-cli` staleness (8.1, 21). Defect: finding-8 (stale lock statement). |
| CK-REQ-G8 | Yes | Every SWE id cited in 07 exists in `docs/references/md/npr-7150-2d/` (script over 90 ids, none missing); pinned: SWE-013 3.1.3 (text read: "software plans, including security plans, that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring"), SWE-033 3.1.2, SWE-037 3.1.7, SWE-089 5.3.4, SWE-090 5.4.2, SWE-093 5.4.3, SWE-219 3.7.4. NPR 7150.2D section 6.1 items a to y in 07 section 1.3 match the corpus names (`06-chapter6.md` lines 13 to 61). SWEHB 5.08 25 minimum-content items (section 1.4) match `5-08-sdp-smp-software-development-management-plan.md` items 1 to 25. The SWEHB count of 267 files and 130 `swe-` pages was recounted (`ls`). No requirement is quoted as a quotation it is not. |

## SRR row 23 and SWE-013 judgment

| Row 23 evidence | Result | Evidence |
|---|---|---|
| Plan outline covering the life cycle (SWE-013) | Present | Sections 3.1 to 3.5 (gates, increments FW-B0 to FW-B4, sprint phases), 20 (operations, maintenance, retirement); every NPR 7150.2D 6.1 record a to y assigned to an artifact and gate (1.3) |
| Approved tailoring | Not yet | Tailoring is the RMM (owner approval at SRR, pending); the plan's mirror has finding-1, finding-5 and finding-12 |
| Acquisition-vs-development record (SWE-033) | Present | `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` exists (Draft, revision 1), reviewed in INSP-013 (verdict APPROVED); assurance dispatch gap is finding-10 |
| Software review milestones (SWE-037) | Present | Section 3.3 (five gates plus sprint closures) and 10.1 |
| Software assurance review of the plan (07 section 2.1.1; SWE-013 as the SA and safety plan) | Not done | No assurance reviewer invoked; this record stays NEEDS CHANGES until one returns |

Row 23 is not met at this record's date: two Major findings are open and the assurance second review is outstanding.

## Observations (not findings)

- **O-1 (slug).** 01 section 4.6, 07 section 10.2 and package section 4 row S3 name the 07 record `plan-07-software-engineering-plan.md`; this record uses `software-plan-07.md` as the dispatching session assigned it. `validate_docs.py` accepts both; the package and 01 references need the actual path (cross item).
- **O-2 (seed coverage).** 07 section 10.3 says the SRR seed "rolls up the records filed on that date". The seed has MSR-20 and MSR-21 for 10 records; on 2026-09-25 the `checklists/` folder also holds `classification-03-software-classification-and-rmm.md`, `icd-stubs-external.md`, `requirements-sys.md` and `requirements-tx-and-sw-keyer.md` (filed after the snapshot) and now this record. The gate-package roll-up of section 10.3 covers them; no finding.
- **O-3 (validator).** `validate_docs.py` accepts any non-`none` string distinct from author and reviewer as `assurance_reviewer_agent`, including this record's "not yet dispatched" value; it cannot tell a planned from a performed assurance review. A check that `assurance_verdict` is `APPROVED` before `verdict: APPROVED` would close the gap (tool owner; cross item).
- **O-4 (SW-SYNTH class).** The Proposed rows follow package decision 9; the plan names the change set that follows either ruling (section 14.1 owner decision paragraph, section 22). No finding.

## Tool runs (2026-09-25)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before this record) | 1 | 30 passed, 3 failed, 33 checked: `docs/plan/measurements.json` (this product, finding-2), `docs/design/allocation.json`, `risk-register-06.md` |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 231 requirements, 167 test cases, 0 violations, 2 warnings |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings, hazard cross-check; `register.md` current |
| `tools/render_rmm.py --check` | 0 | 100 rows; FC 75, T 17, NA 8 |
| `tools/render_compliance.py --check` | 0 | validation passed, rendered file current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 331 run, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero` (the repository validator failures above, including `measurements.json`) |
| `.venv/bin/python tools/validate_docs.py` (after this record) | 1 | 32 passed, 2 failed, 34 checked; this record PASS as a peer-review record; remaining failures `docs/plan/measurements.json` (finding-2) and `docs/design/allocation.json` (`risk-register-06.md` was corrected by its owner in the meantime) |

## Completion criteria (SWE-088 b, c)

Iteration 1 (2026-09-25): not met; R1 and R3 not met, two Major and eleven Minor findings Open, assurance review not dispatched.

Iteration 2 (2026-09-26): not met. Finding-2 (Major) stays Open because the schema file that closes it is not in the repository and the validator and the repository unit test still fail on `measurements.json`; finding-14 (Minor, new) is Open; R1 is still not met. The paired assurance record INSP-018 is filed and its `assurance_verdict` is NEEDS CHANGES (read 2026-09-26). Verdict NEEDS CHANGES. The software lead sets `record_status: Closed` only when every finding is Verified or Deferred (07 section 10.2).

## Iteration 2 closure (2026-09-26)

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (query: 07 section 22 tailoring mirror, SWE-094, SWE-045, measurements schema); the tool was available. `grep -n`, `sed -n` and read-only Python were used afterwards to pin the lines and values the hits and the author's fix list pointed at. The reviewer edited only this record.

**Author's fix list against the product.** Each claim was checked in 07 revision A.4 (blob `eba15bcb`) and `measurements.json` (blob `5e2d1755`); results are in the State and Disposition columns above.

| Finding | Severity | Iteration 2 result |
|---|---|---|
| finding-1 | Major | Closed (Verified) |
| finding-2 | Major | Open: plan text fixed, schema file absent, validator exit 1 |
| finding-3 to finding-10, finding-12, finding-13 | Minor | Closed (Verified) |
| finding-11 | Minor | Closed (Verified); RSK-020 and RSK-023 part disputed by the author, dispute accepted |
| finding-14 | Minor | Open (new) |

**Checklist items re-answered.** CK-REQ-G1 Yes (finding-6, 7, 9, 13 closed; 14.1 hazard lists re-read against the HZ-008 type (ii) wording of 03). CK-REQ-G2 Yes (finding-9, 11 closed). CK-REQ-G3 Yes (finding-10 closed). CK-REQ-G4 Yes (mirror equals `rmm.json`: 17 T, 8 NA; finding-1, 5, 12 closed). CK-REQ-G6 No (finding-2). CK-REQ-G7 No (finding-14). CK-REQ-A8, G5, G8 unchanged Yes. Readiness R1 Not met (same failure), R2 Met (0 violations), R3 Not met (per-finding response, no A to G self-check), R4 Met (no TBD, no em dash found in 07 by grep).

**Observations at iteration 2 (not findings).**
- **O-5 (evidence drift).** Four current MSR-20 and MSR-21 pairs (INSP-003, INSP-004, INSP-009, INSP-017) cite checklist hashes that no longer equal the files on 2026-09-26, because those records changed after the append. The 11.1 evidence-preservation rule requires a superseding record at commit; the same will hold for this record's own MSR-20 and MSR-21 (iteration 2 changes its counts). Cross item for the software lead at the commit of `measurements.json`.
- **O-6 (tool constant).** `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` does not yet list 05 or TS-002, which 07 section 2.1.1 now routes to assurance; 07 section 22 carries it to the tool owner.
- **O-7 (paired_record).** This record now carries `paired_record: INSP-018` as 07 section 10.2 and section 22 ask; the validator schema accepts the field but does not yet check it (01 section 13 and tool owner, section 22 row "Paired assurance record fields").

**Tool runs (2026-09-26).**

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before this update) | 1 | 35 passed, 2 failed, 37 checked: `docs/design/allocation.json` and `docs/plan/measurements.json` (schema not found; finding-2) |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 7 warnings; `docs/vv/traceability.json` sha256 `e796e0f6...` unchanged (equals MSR-01, 03, 04 evidence) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 0 warnings, register current |
| `tools/render_rmm.py --check` | 0 | 100 rows; FC 75, T 17, NA 8; SWE-045 and SWE-094 FC |
| `tools/render_compliance.py --check` | 0 | validation passed, rendered file current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 335 run, 1 failure: `test_repository_exit_zero` (the validator failures above) |

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-REQ-G4 07 s22, s11.3: SWE-045 and SWE-094 listed as tailored or NA; RMM has both FC and the charter dropped them at 4e3f891.
- [Major] R1, CK-REQ-G6 docs/plan/measurements.json: fails validate_docs (schema not found); repository unit test fails.
- [Minor] CK-REQ-G6 MSR-05 note says no record APPROVED; INSP-005 and INSP-013 are APPROVED at iteration 2.
- [Minor] CK-REQ-G6 seed provenance: working-tree notes missing, traceability.json hash not reproducible, MSR-03 Green with null sub-measures.
- [Minor] CK-REQ-G4 s22 does not mirror rationale and residual risk as RMM SWE-121 states.
- [Minor] CK-REQ-G1 s14.1 and s22: stale notes on the 03 re-transcription and OQ-SAF-022; hazards.json version 0.3.0 vs 0.4.0.
- [Minor] CK-REQ-G1 s14.1: omits the 03 type (ii) HZ-008 entries; 03 places SW-SCHED in cwht-app.
- [Minor] CK-REQ-G7 s8.1: says the lock lacks the pinned nightly row; the lock has it.
- [Minor] CK-REQ-G1, G2 header and s13: charter commit b8214ca superseded; 268 pages vs 267 files; ten vs twelve 05 s8.1 steps.
- [Minor] CK-REQ-G3 s2.1.1: no assurance dispatch row for make/buy trade studies (TS-002).
- [Minor] CK-REQ-G2 s21, s16.2, s1.3 r: existing RSK ids not cited; software tag missing.
- [Minor] CK-REQ-G4 s22: RMM SWE-090 and SWE-094 text mismatches not carried.
- [Minor] CK-REQ-G1 s14.2 row i: L1 column adds REQ-SYS-181 not named by hazard-analysis s7.
ITEMS N/A: CK-REQ-A1 to A7, B to F, per-requirement table
MEASUREMENTS: size=960 lines + 47 records; items_checked=9; items_no=6; major=2; minor=11; fixed=0; deferred=0; iteration=1; turns=42; minutes=55
```

Iteration 2 (2026-09-26):

```
VERDICT: NEEDS CHANGES
CLOSED (Verified): finding-1 (Major), finding-3 to finding-13 (Minor; finding-11 with the author's RSK-020/RSK-023 dispute accepted)
OPEN:
- [Major] finding-2 R1, CK-REQ-G6: docs/plan/measurements.schema.json absent; validate_docs exit 1; repository unit test fails.
- [Minor] finding-14 CK-REQ-G7 07 s8.1: "toolchain.lock.md rows 21 to 25" points at the wrong rows.
MEASUREMENTS: size=1007 lines + 89 records; items_checked=9; items_no=2; major=2; minor=12; open=2; verified=12; deferred=0; iteration=2; turns=66; minutes=90 (cumulative)
```
