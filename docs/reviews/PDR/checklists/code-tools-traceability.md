---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md section 3.2). Checklist: docs/templates/peer-review-checklist-code.md
# revision B, applied to the Python tool source as 03 section 6.1.1 (row "Peer review") directs and as
# INSP-015 did for the SRR tools. Product: tools/traceability.py of CR-011 (Submitted, Class II), frozen on
# branch cr/CR-011-traceability-pdr-rules at 4774562 (rule C2), with its known-answer modules, fixture
# changes, README, 02 sections 8.1, 8.2, 8.5 and 10.4, TV-002 run 6 and CR-011 as the product_files the
# brief froze. PDR work plan WP-PDR-06 names this record and a separate software assurance record
# (code-tools-traceability-software-assurance.md) and a tool validation record (tool-validation-tv-002.md).
id: INSP-042
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/code-tools-traceability.md
product: tools/traceability.py
product_commit: "4774562e41b2319814fa4fe0ad3075ba70d3bb72"
product_files: ["tools/traceability.py@d4cde9f54386373017f21825d4fd7cc0a42ac373", "tools/tests/test_traceability.py@95f1719b637834719212624b105f54f4a6cfd8b1", "tools/tests/test_tools.py@f8289a443f6ca2d837ab2df07df5a3dfc0722f27", "tools/README.md@d61156d8966178e958df4539adab60e8c0ff8b0d", "docs/process/02-requirements-and-traceability.md@d4934d0e7c9648c13ea7d50c1b28faba45b86c00", "docs/cm/tool-validation/TV-002-traceability.md@1fe6fb756cc21180487c2148de0d02d676d3be37", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py@220ae2e0118fe13e8237b628d6192a0c67e3c44e", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt@e26b24368088c56bf18c920b34a12e5dfdd1966a", "tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.json@d0a10e0bb645f016bdf77eebeca0fedfb142240a", "tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.md@5b8f8d87935af6432e713d6d0afc80747e022589", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/straight.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/iambic.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/config.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/hardware/kicad/tx-pa.kicad_sch@b42ba81e76a76cc8a013e23bac36d3c2277ed5c4", "docs/vv/traceability-report.md@f49f4215b34179caca551dcfd9a348fdf17c288e", "docs/vv/traceability.json@0f0ea6ef18bdcabd3cba6ef9d6853296de6c476f", "docs/cm/cr/CR-011-traceability-pdr-rules.md@d597899b9f442bfc9c3983cb28f15998eb78c197"]
product_size: 4156 lines (tools/traceability.py; 1465 lines added and 142 changed against blob 12de3545, reviewed in full); test_traceability.py 1118 lines (715 added); README 269 lines; 02 sections 8.1 to 8.5 and 10.4
sprint: PDR-prep
author_agent: "author:WP-PDR-06 (Claude as tool owner and software lead, CR-011)"
reviewer_agent: "reviewer:WP-PDR-06-code-and-tv (independent invocation, authored no part of CR-011)"
# criticality: a tool is neither safety-critical nor mission-critical (03 sections 4.3.1 and 6.1.1)
criticality: neither
# assurance_required: true. PDR work plan WP-PDR-06 requires the software assurance second review because
# the tool's output is used for credit (readiness declaration, SWE-052 evidence)
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/code-tools-traceability-software-assurance.md (plan WP-PDR-06; 07 section 2.1.1)"
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED for the engineering lens (zero Major; seven Minor findings, liens under plan rule C1)
reviewer_verdict: APPROVED
# assurance_verdict: pending until the software assurance record is filed
assurance_verdict: pending
# verdict: held at NEEDS CHANGES by the template rule (APPROVED only when the assurance verdict is APPROVED) and
# because the product blobs are on the CR-011 branch, not on main (record drift rule); section "Record verdict"
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 7
findings_open: 7
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-E1, CK-CODE-H2, CK-CODE-I1]
effort_turns: 70
effort_minutes: 120
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-042: `tools/traceability.py` PDR rule set (WP-PDR-06, CR-011), code review

**Product:** `tools/traceability.py` blob `d4cde9f5` (commit `4411a09`, unchanged at the branch head `4774562` of `cr/CR-011-traceability-pdr-rules`), with the other `product_files` at the blobs above (identity checked with `git rev-parse 4774562:<path>` for every entry: all 17 equal). **Checklist:** `docs/templates/peer-review-checklist-code.md` revision B (blob `49912fd5`), applied to host Python as INSP-015 did at SRR: the Rust-only items are N/A with the reason given; the tool's specification is `tools/README.md` with 02 sections 8.1 to 8.5 and 10.2 to 10.4, 03 section 8, 04 section 7.3, the SRR memo section 9 condition 5 and RFA-SRR-007 L-7 (the CR-011 section 5 "what the independent reviewer checks" list).

**Acceptance criteria (rule C7, every case the governing clause enumerates):** each of the 22 T-rules of 02 section 8.2 in its `check` and `gate` columns; every transition row and evidence cell of 02 sections 8.3 and 8.4; every Class I, Class II and Editorial row of 02 section 10.2 and the T-13 coverage rule; the 02 section 10.4 counting rule (N_start, A, M, R, C2, TBR closures, per scope and per module, thresholds); 04 section 7.3 rules 4 (PCA-05 part), 5, 11 and 12; 03 section 8 rows 2 and 3; the 02 section 3.5 Identity, Order and Pairing rows; the 02 section 8.1 option table; and every output the WP-PDR-06 Outputs line names.

**Independence (rule C4):** this invocation authored no part of WP-PDR-06, CR-011 or TV-002 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran (queries: "WP-PDR-06 traceability PDR rules reviewer checklist tool validation"; "04 section 7.4 implementation status rows due before SRR traceability tool evidence-side rules") before any manual search; `grep -n` was used afterwards only to pin lines. The rustos working tree was not read: the one rustos check was `git ls-tree` of the pinned commit `2ec64c0`.

## Record

### Commands run by the reviewer (evidence)

| # | Command (all read-only for the repository; outputs under the scratchpad) | Result |
|---|---|---|
| C1 | `git archive 4774562 \| tar -x` to a scratch export; the three TV-002 section 3 commands with the run 6 selection | 80 + 32 + 117 = 229 tests, `OK`, none skipped; equal to TV-002 run 6 |
| C2 | Full suite in the export: `.venv/bin/python -m unittest discover -s tools/tests` | 471 tests, `OK (skipped=3)` (the three `test_render_deck.py` classes; the export holds no `tools/slides/node_modules/`), equal to the 02 section 8.5 evidence line |
| C3 | Mutation check: the export with `tools/traceability.py` of `a3cacee` (blob `12de3545`, verified with `git hash-object`), each of the 13 PDR classes run alone | every class fails: failures and errors per class identical to the TV-002 run 6 log section 3 |
| C4 | Plain run on the branch worktree (`--root <worktree> --rustos /Users/robinonsay/rust/rustos --output <scratch> --json <scratch> --quiet`) | exit 0, 0 violations, 95 warnings (17 `ADR_BACKREF_MISSING`, 22 `DESIGN_REF_INVERSE`, 44 `DESIGN_REF_UNRESOLVED`, 4 `HAZARD_UNCONTROLLED`, 1 `ICD_SECTION4_MISMATCH`, 4 `ICD_UNPAIRED`, 1 `MOE_WITHOUT_MOP`, 2 `SYS_UNALLOCATED`), equal to TV-002 R-3. The committed `docs/vv/traceability-report.md` and `traceability.json` equal this output except the HEAD short SHA (`4411a09` against `4774562`) in report sections 1.1 and 12 and the `generated` date |
| C5 | The same with `--gate PDR` | exit 1, 379 violations with the code counts of TV-002 R-3 |
| C6 | `--volatility --from baseline/srr --dry-run` on the worktree; the export tool with `--root` on the main repository and `--to cr/CR-008-srr-liens-l1-and-tc-sys --dry-run` | V 0.0 % for L1, L2 and software (the CR-011 section 4 claim); against the CR-008 branch V_L1 8.0 % (N_start 188, A 1, M 14, R 0, C2 130), assessment Green; nothing written (`git status` clean) |
| C7 | `git -C /Users/robinonsay/rust/rustos ls-tree -r --name-only 2ec64c0` for `timer` | no timer file at the pinned commit: the two `rustos:firmware/pico2/src/timer.rs` `DESIGN_REF_UNRESOLVED` warnings are true findings |
| C8 | `validate_docs.py --root <worktree>` | fails only on the SRR records INSP-015 and INSP-020 (record drift), as TV-002 limitation 6 and CR-011 section 4 state |

### Findings (filled by the reviewer and the assurance reviewer)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-CODE-E1 | `tools/traceability.py:2711` (`approved_crs_listing`), `:2856` (`check_changes`); 02 `:552` (8.5 row T-13 "none"); 02 `:627` (10.3 item 2) | T-13 accepts a change when any approved CR lists the id in `affected_ids`, whatever the CR's before and after text; 02 section 10.3 item 2 says the CR carries the exact before and after text "so that the reviewer and T-13 compare exact strings". An approved CR therefore covers every later change to the same id. Neither the 02 section 8.5 T-13 row ("Remaining task: none"), the README "Not implemented" table nor TV-002 section 6 states this. Fix: compare the CR section 1 after-text with the working-tree field, or state the limitation in 8.5, the README and TV-002 section 6 with a due gate | Open | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-CODE-E1 | `tools/traceability.py:2859`; `tools/tests/test_traceability.py:1003` | A `child_ids`-only difference is accepted as editorial without reading the commits: 02 section 10.2 (Editorial row, "commit type `editorial` or an `Editorial:` trailer ... the tool lists them in the report's editorial log") and T-13 accept an editorial difference only when every touching commit is editorial and is logged. A `child_ids` edit in a non-editorial commit passes silently and is absent from report section 12.2. Fix: apply the commit test to `child_ids` changes and log them, or state the exemption in 02 section 10.2 through this CR | Open | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-CODE-E1, CK-CODE-J3 | `tools/traceability.py:2744`, `:2752`; 02 `:551` (8.5 row T-12); CR-011 section 1 row "Git history" | T-12 checks evidence only for `Draft` to `Active` or `Baselined` (memo or CR) and for retirement after the baseline (CR). The 8.3 and 8.4 evidence cells it leaves out are more than the 8.5 remainder lists (RID or INSP record of a pre-baseline retirement, reviewer record making a case `Active`): also the TRR decision memo for a `Bench` or `OnAir` case going `Active` (8.4), the `NCR-NNN` for `Verified` to `Active` (8.3) and for `Failed` to `Active` (8.4), and a new test case entering at any status is not checked (`:2744`). The remainder moved from "PDR" (02 section 8.5 at `main`: T-12 due PDR, "memo, RID, INSP and CR existence") to "CDR"; CR-011 section 1 does not state this re-plan to the owner. Fix: list every unchecked evidence cell in the 8.5 T-12 row, the README "Not implemented" table and TV-002 limitation 8, and state the PDR-to-CDR re-plan in CR-011 section 1; the TRR memo check is one `memo_present` call and may be implemented instead | Open | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-CODE-E1 | `tools/traceability.py:2343` and `:2157` to `:2170`; 02 `:485` (8.2 T-15), `:554` (8.5 T-15) | Two rules apply a wider status scope than their 02 section 8.2 statement: `DESIGN_REF_MISSING` fires on `Draft` L2 requirements (8.2 T-15 and 03 section 8: "Active"), and the PDR form of `SYS_UNALLOCATED` on `Draft` SYS requirements (8.2 T-18: "every Active `SYS` requirement"). The choice is sound (the L2 files flip to `Active` only at the PDR memo, so the rule would otherwise never fire at the PDR readiness declaration), and 02 section 8.5 states it for T-15, but 8.2 and 8.5 of the same blob now disagree. Fix: amend the 8.2 T-15 and T-18 statements in CR-011 to name `Draft` or `Active`; 03 section 8 follows through WP-PDR-17 (already routed in CR-011 section 4) | Open | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-CODE-E1 | `tools/traceability.py:3083` (`append_measurement`); TV-002 purpose 8; README option `--volatility`; 02 `:36` of the 8.1 option table | The record is appended "only after the whole file passes `docs/plan/measurements.schema.json`" (purpose 8, README, 02 section 8.1), but the code writes without any check when the schema file is absent, when it does not parse, or when `jsonschema` is not importable. Fix: exit 2 and write nothing when the schema cannot be applied, with a known answer (absent schema) in `VolatilityTests` | Open | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-CODE-H2 | `tools/tests/test_traceability.py:565`, `:625`, `:747`, `:803`, and most PDR tests that use `of(project, code)` | Most PDR known answers assert the findings of the code under test only (a count and message fragments, or the location list), not the whole finding set after the one change; a regression that adds a spurious finding of another code on the same input would pass. INSP-015 and TV-002 section 8 ask that each seeded fault assert an exact code set. Fix: add `assertEqual({<code>}, codes(project.findings))` (or the exact expected set) to each single-change test | Open | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-CODE-I1, CK-CODE-I4 | `tools/traceability.py:2147`; module docstring `:28` to `:74` | The `check_allocation` docstring says the PDR Error of T-18 is "not yet implemented", but lines 2157 to 2170 implement it. The module docstring states exit 1 on a violation and says nothing of exit 2 (argparse usage errors, including `--gate QDR`, and every `--volatility` failure), which 02 section 8.1 and the known answers use. Fix: correct both docstrings | Open | |

No Major finding. Every finding is Minor under the template's definition (documentation, a scope statement or a test assertion that is weaker than the process text); none makes the tool report a wrong result on the repository today (C4 and C5 reproduce TV-002 R-3).

### Cross-document items (not findings against this product)

| # | Item | Owner |
|---|---|---|
| X-1 | **01 section 3.1 item 2** (`/Users/robinonsay/rust/cwht/docs/process/01-lifecycle-and-reviews.md:66`) runs the tool without `--gate`, and "a failing report blocks readiness for every gate". Until it reads `--gate <REVIEW>`, the gate column of 02 section 8.2 (every "W, E@PDR" code, including `HAZARD_UNCONTROLLED`, `HAZARD_INVERSE`, T-15, T-16, T-20 and T-22) never blocks the PDR readiness declaration, which is the WP-PDR-06 objective. CR-011 section 4 routes it; it must land before WP-PDR-48 | WP-PDR-12 (01 writer); WP-PDR-48 |
| X-2 | 03 section 8 rows 2 and 3 name `HAZARD_UNCONTROLLED` a violation and `DESIGN_REF_MISSING` for `Active` `REQ-SW-*`; the tool makes the first a plain-run warning (violation under `--gate` from PDR, disclosed in CR-011 section 1 and the README) and widens the second to Draft and Active L2 (finding-4). The RMM SWE-052 row lags too | WP-PDR-17 (03 and RMM writer) |
| X-3 | 04 section 7.4 still reads "7.3.11 no", "7.3.12 no" and "Options that do not exist yet: `--gate`, `--volatility`, `--fix-children`" | WP-PDR-13 (04 text) |
| X-4 | `SAFETY_PART_UNTRACED` reads the proposed field `elements[].safety_critical` of `docs/design/allocation.json`; the schema change and the marking of the three parts named by the SRR memo section 9 condition 5 (hardware transmit timer, cell protection ICs, headphone limiter) are needed before the PDR gate run exits 0 | WP-PDR-31 |
| X-5 | 02 section 8.5 rows T-07 (`SYS_NO_VALIDATION_PATH`, `SECURITY_TAG_NO_SOURCE`) and T-09 and T-10 (module rule) were due "before SRR" and stay unimplemented (INSP-020 cross item X-1); the plan maps no WP to them. They block the readiness declaration under 02 section 8.5 ("blocked until every row due at that gate has a passing unit test") | Lead SE (assign a WP or re-plan by CR) |
| X-6 | The data gaps the gate run lists (44 `DESIGN_REF_UNRESOLVED`, mostly the directory form `firmware/cwht-core/src/keyer/`, which 02 T-15 does not admit; 17 `ADR_BACKREF_MISSING`; 4 `HAZARD_UNCONTROLLED`; 134 `TBR_DUE_AT_GATE`) are PDR product work, not tool defects | WP-PDR-31, 35, 16, 45 and the ADR owners |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Gate G1 (`cargo fmt`, `clippy`) | N/A | Python; no linter is locked for `tools/` (lock section 2). Substitute: the full suite (C2) and the module imports cleanly under the TV-001 interpreter |
| R2 | File at most 500 lines, functions at most 60 lines (CS-18) | N/A | CS-18 is a firmware rule (07 section 7). Measured for the record: `tools/traceability.py` 4156 lines (`wc -l`); the longest new functions are `volatility_record` (about 60 lines) and `check_transitions` (about 35) |
| R3 | Design unit Active | N/A | Tools have no design unit; the specification is `tools/README.md` with 02 sections 8 and 10 |
| R4 | `@req` tags | N/A | Rust tag convention |
| R5 | Test file exists | Yes | `tools/tests/test_traceability.py` (13 PDR classes, 49 tests), `test_tools.py` (`CatalogueKnownAnswerTests` guard) |
| R6 | `unsafe_audit.py` | N/A | No `unsafe` in Python |

## Participants

Author agent (absent): WP-PDR-06 tool owner. Reviewer: this invocation. Software assurance reviewer: pending, a separate invocation (plan WP-PDR-06; the SA pair is not done here). Owner: for the rulings of the tool validation record and the CR-011 disposition.

## A. Environment, dependencies and build (CS-01 to CS-04)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | N/A | `no_std` rule for image crates; the tool is host Python |
| CK-CODE-A2 | Yes | New imports are standard library only (`hashlib`, `subprocess`, `datetime`); `jsonschema` is reached through `validate_docs` (TV-001, TV-003); `git` is TV-009 (TV-002 section 1 "Runtime for run 6"). No `tools/requirements.txt` change |
| CK-CODE-A3 | N/A | Rust `cfg` rule |

## B. Unsafe code (CS-05 to CS-10)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-B1 to B8 | N/A | No `unsafe` and no MMIO in Python |

## C. Panics, errors and arithmetic (CS-11 to CS-16)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-C1 | Yes (adapted) | Every new reader tolerates absent or malformed input without raising: `GitHistory.git` returns `None` on `OSError` or a non-zero exit (`:2549`); `json_at` catches `JSONDecodeError`; `rustos_path_exists` catches `OSError` and reports a missing repository or lock row as a finding reason (`:2293`); `load_icds`, `load_adrs`, `load_change_requests` take `parse_front_matter(...) or {}` and type-check. C4 and C5 on the repository and C1 on both fixtures complete with no traceback |
| CK-CODE-C2 | Yes (adapted) | Failures become catalogue findings or exit status 2 with a message on stderr (`main`, `:4132` to `:4142`); an unreadable git root becomes report section 12 text and, under `--gate` from PDR, `BASELINE_NOT_READ` (`:2945`) |
| CK-CODE-C3 to C7 | N/A | Rust error, arithmetic and panic-handler rules. Division in `volatility` is guarded by `if n` (`:2991`) |

## D. Structure, complexity and target platform rules

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-D1 | N/A | SWE-220 applies to 07 section 14.1 components; no Python complexity tool is locked |
| CK-CODE-D2 | Yes | No new recursion except `reachable` (`:2699`), an iterative worklist over the finite status graphs with a `seen` set. Git log parsing is bounded by the history |
| CK-CODE-D3 to D9 | N/A | Rust and target rules |

## E. Correctness against design and requirements

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-E1 | No | Checked rule by rule against the acceptance criteria above. **Agree:** `GATE_ERROR_FROM` (`:397`) equals the 02 section 8.2 `gate` column for all 22 rules (T-07, T-08, T-11, T-17, T-20, T-21 E at every gate; T-15, T-16, T-18, T-22 and T-20 MOP-per-MOE E@PDR; `DESCRIPTION_LENGTH`, `OPS_UNCITED`, `RENDER_STALE`, `SCHEMA_ID_PATTERN_MISSING` stay W), and `HAZARD_INVERSE` is E at every gate as 04 rule 7.3.6 requires; T-04 over REQ, TC, NGO, MOE, CON ids and stakeholder names (`:2763`); the 8.3 and 8.4 forbidden transitions (`REQ_EDGES`, `TC_EDGES`, `L0_EDGES`, `:2694`), reached transitively between the tag and the working tree; the 10.2 Class I field and tag lists and the Class II remainder (`:2775`); T-14 gate rule (`:2020`); T-15 forms including `rustos:` at the lock section 3 commit by `git show` only (`:2293`, C7); T-16 and T-20 MOP rules (`:2259`); T-22 names against the 02 section 3.5 Identity and Order rows and pairing against the Pairing row (`:2394` to `:2456`); 03 section 8 `HAZARD_UNCONTROLLED` on `requirement_ids` (`:2459`); 04 rule 7.3.4 PCA-05 (`:1928`), 7.3.5 (`:1955`), 7.3.11 (`:2915`, fields `description`, `verification_method`, `verification_note`, `tbr`), 7.3.12 (`:1886`, and `closing_cases` excludes dev-board cases, `:781`); 01 section 8.6 on-target rule at SAR (`:1802`); RFA-SRR-007 L-7 against `docs/templates/adr.md` section 4.1 (`:2472`); the 10.4 formula, M with TBR closures, C2 outside V, waiver not a change, per scope and per module, thresholds 10 and 20 % (`:2965`, `:2995`; hand check: `VolatilityTests` 4 of 6 = 66.7 %). **Disagree:** finding-1 (T-13 exact-string comparison), finding-2 (`child_ids` editorial acceptance), finding-3 (T-12 evidence cells), finding-4 (status scope of T-15 and T-18), finding-5 (schema check before append) |
| CK-CODE-E2 | N/A | Firmware timing constants |
| CK-CODE-E3 to E8 | N/A | Keyer, register and safe-state rules |
| CK-CODE-E9 | Yes | Every new function is called from `run_checks` (`:3137`), `build_report`, `build_json` or `main`; `adr_backrefs` and the Snapshot helpers feed report sections 12 and 15. No `pass`-only stubs |

## F. Traceability tags (CS-24; SWE-052)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-F1 to F3 | N/A | Rust tag convention. Substitute: each new check cites its governing clause in its docstring and in its `CHECK_CATALOGUE` text (for example `:2334`, `:2459`, `:2472`, `:2729`), and `test_tools.CatalogueKnownAnswerTests` fails when a catalogue code has no known answer |

## G. Secure coding (CS-29 to CS-33; SWE-207, SWE-185)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-G1 | Yes (adapted) | Every subprocess call passes an argument list, never a shell string (`GitHistory.git`, `rustos_path_exists`); refs from the command line go to `git rev-parse --verify --quiet` before use (`:3015`); `--gate` is restricted by `choices=GATES` |
| CK-CODE-G2 to G5 | N/A | Firmware key-line, buffer, diagnostic and gate G5 rules |

## H. Tests and testability (SWE-062)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-H1 | Yes | The history rules are exercised on temporary git repositories built from `valid_project` with signing off and a fixture identity (`test_traceability.py:448`); rustos on a temporary repository with an uncommitted file that must not resolve (`:575`); no dependency on the repository or the network |
| CK-CODE-H2 | No | Tests exist and pass (C1, C2) and discriminate the change (C3). Their author is the tool author, which the tool validation practice of 05 section 9.2 accepts for known answers (independence is supplied by this review and the TV review). finding-6: most PDR tests assert the code under test only, not the exact finding set |
| CK-CODE-H3 | N/A | No safety-critical decision table |

## I. Documentation and style (CS-25 to CS-28)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-I1 | No | Every new function has a docstring naming its clause; finding-7 (two stale or incomplete docstrings) |
| CK-CODE-I2 | Yes | Names carry their rule (`check_case_stale`, `check_icds`, `GATE_ERROR_FROM`, `TC_EDGES`) |
| CK-CODE-I3 | N/A | Rust `fmt` and clippy |
| CK-CODE-I4 | Yes | Comments explain why (for example `:2855`, "the level is not yet under CR control (02 section 10.1)"); no commented-out code. The stale docstring is counted under finding-7 |

## J. Common review traps

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-J1 | Yes (adapted) | Every `validate_docs` symbol used (`load_json`, `parse_front_matter`, `jsonschema`, `FM_KEY`, `yaml`) exists at blob `3aa03681`; every git sub-command used exists in git 2.50.1 (C1, C4) |
| CK-CODE-J2 | N/A | Rust traits |
| CK-CODE-J3 | No | Compound clauses: 02 section 8.3 "Evidence checked by T-12" is implemented for two of its cells only (finding-3). The compound T-22 clause (side A and, for a module B, side B; section 4 equals the citing set; the front-matter lists by side) is implemented in full (`:2427`) |
| CK-CODE-J4 | Yes | Sizes measured with `wc -l` and `git diff --stat main...4774562` (C1) |

## Record verdict

`reviewer_verdict: APPROVED` for the engineering lens: zero Major findings, seven Minor findings. Under plan rule C1 the seven Minor findings are liens due at the CDR readiness declaration unless the author fixes them in the CR-011 branch before its freeze for the other two WP-PDR-06 records. `verdict` stays `NEEDS CHANGES` for two reasons outside this lens: the software assurance second review (`code-tools-traceability-software-assurance.md`) has not run, and the reviewed blobs are on the CR-011 branch, so an APPROVED verdict would fail the record drift rule of `tools/validate_docs.py` on `main` until CR-011 merges with these blobs unchanged. The companion tool validation record is INSP-043 (`docs/reviews/PDR/checklists/tool-validation-tv-002.md`).

```
VERDICT: APPROVED (reviewer lens); record verdict NEEDS CHANGES until the SA pair and the CR-011 merge
FINDINGS:
- [Minor] CK-CODE-E1 tools/traceability.py:2711: T-13 coverage by id only; 02 section 10.3 item 2 exact-string comparison absent and unstated.
- [Minor] CK-CODE-E1 tools/traceability.py:2859: child_ids change accepted as editorial without the commit test or the editorial log.
- [Minor] CK-CODE-E1 tools/traceability.py:2744: T-12 evidence cells unchecked beyond the listed remainder; PDR-to-CDR re-plan not stated in CR-011.
- [Minor] CK-CODE-E1 tools/traceability.py:2343: Draft scope of DESIGN_REF_MISSING and the T-18 PDR form differs from 02 section 8.2.
- [Minor] CK-CODE-E1 tools/traceability.py:3083: MSR-02 appended without a schema check when the schema cannot be applied.
- [Minor] CK-CODE-H2 tools/tests/test_traceability.py: PDR tests assert the code under test, not the exact finding set.
- [Minor] CK-CODE-I1 tools/traceability.py:2147: stale check_allocation docstring; exit status 2 undocumented in the module docstring.
ITEMS N/A: R1 to R4, R6, A1, A3, B1 to B8, C3 to C7, D1, D3 to D9, E2 to E8, F1 to F3, G2 to G5, H3, I3, J2 (host Python tool)
MEASUREMENTS: size=4156 lines (1465 added); turns=70; minutes=120; major=0; minor=7; unsafe_sites=0
```
