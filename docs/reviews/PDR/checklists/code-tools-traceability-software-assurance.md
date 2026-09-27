---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the code review INSP-042
# (docs/reviews/PDR/checklists/code-tools-traceability.md, iteration 2 by reviewer:WP-PDR-06-code-delta), which
# names this path in assurance_reviewer_agent and cross item X-10. PDR work plan WP-PDR-06 names the record
# ("SA second review (tool used for credit)").
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not merged).
# The `checklist` field names peer-review-checklist-code revision B, the checklist INSP-042 names, because
# tools/validate_docs.py fails a record whose `checklist` names a template absent from main, and the lead SE
# convention of 2026-09-27 does not change the validator. `assurance_checklist` names the template actually
# applied (the form of INSP-048, INSP-049 and INSP-051).
# id: the brief assigned no id; INSP-070 is above every id on main, on every cr/ branch and in the working tree
# (highest INSP-065, uncommitted, 2026-09-27), leaving 066 to 069 and the gaps 055, 057 and 063, which other in-flight
# work packages may hold
id: INSP-070
checklist: peer-review-checklist-code
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/code-tools-traceability-software-assurance.md
product: tools/traceability.py
# product_commit and product_files: equal to INSP-042 iteration 2 (readiness R1; rule C2). Eighteen blobs exist
# only on the CR-011 branch (git rev-parse 2b004b1:<path>, checked 2026-09-27); the CR file blob 892670b6 is the
# one INSP-042 froze (main 7bb994f); on main the CR file has since moved to 49461a58 (86ff3b0; INSP-042 X-7)
product_commit: "2b004b17bf94ecf3dc3591cbc34892e6620ad8a7"
product_files: ["tools/traceability.py@d4cde9f54386373017f21825d4fd7cc0a42ac373", "tools/tests/test_traceability.py@6ead56414127f9c13cd39e3662a2118e2acd470e", "tools/tests/test_tools.py@f8289a443f6ca2d837ab2df07df5a3dfc0722f27", "tools/README.md@d61156d8966178e958df4539adab60e8c0ff8b0d", "docs/process/02-requirements-and-traceability.md@d4934d0e7c9648c13ea7d50c1b28faba45b86c00", "docs/cm/tool-validation/TV-002-traceability.md@94ae3af57e6d5527ccd5ff76ab7aa8724fb0b395", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.py@e6f3785628ee376a921a1176883f475c086ab656", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.log.txt@1e30bb222b51ecdf3800f6bb5c4a243ce94f0ef3", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py@220ae2e0118fe13e8237b628d6192a0c67e3c44e", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt@e26b24368088c56bf18c920b34a12e5dfdd1966a", "tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.json@d0a10e0bb645f016bdf77eebeca0fedfb142240a", "tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.md@5b8f8d87935af6432e713d6d0afc80747e022589", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/straight.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/iambic.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/config.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/hardware/kicad/tx-pa.kicad_sch@b42ba81e76a76cc8a013e23bac36d3c2277ed5c4", "docs/vv/traceability-report.md@f49f4215b34179caca551dcfd9a348fdf17c288e", "docs/vv/traceability.json@0f0ea6ef18bdcabd3cba6ef9d6853296de6c476f", "docs/cm/cr/CR-011-traceability-pdr-rules.md@892670b609f4bbd1d4c0c12de8a75f7890e2bf69"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/code-tools-traceability.md (INSP-042 iteration 2, main 0743499)", "docs/reviews/PDR/checklists/tool-validation-tv-002-software-assurance.md (INSP-051)", "docs/reviews/PDR/checklists/tool-validation-tv-002.md (INSP-043)", "docs/process/03-software-classification-and-rmm.md@ed270f443e2ab648480017df8ad3d0221400cf4c (sections 6.1.1, 6.5 item X9, 8; equal on main and at 2b004b1)", "docs/process/07-software-engineering-plan.md", "docs/process/rmm.json", "docs/cm/tool-validation/TV-024-python-analysis.md", "tools/toolchain.lock.md", "docs/plan/pdr-work-plan.md"]
paired_record: INSP-042
# product_type: code (07 section 2.1.1 row "code"; the tool is Python host code reviewed with the code checklist,
# 03 section 6.1.1 row "Peer review"). Task set applied: the section B row "Every product type"; the section B
# row "code"; and the section 7.1 tasks of every SWE the product implements (02 section 8 commissions the tool for
# SWE-052, SWE-192 via HAZARD_REQ_NOT_TESTED, SWE-071 via CASE_STALE, SWE-080 via T-12 and T-13, SWE-200 via
# --volatility, SWE-090 via the MSR outputs) and of SWE-136, SWE-070 and SWE-081 (tool CM and accreditation),
# with the section E tasks (SWE-087, SWE-088, SWE-089) (07 section 15)
product_type: code
# criticality: a tool is neither safety-critical nor mission-critical (03 sections 4.3.1 and 6.1.1 row "Safety and
# mission-critical rows"); its output routes safety-critical evidence, so the safety-designated tasks of the
# SWEs it implements are applied, not relieved
criticality: neither
product_size: "tools/traceability.py 4156 lines (1465 added by CR-011); test_traceability.py 1219 lines (14 new classes); 19 product files"
sprint: PDR-prep
author_agent: "author:WP-PDR-06 (Claude as tool owner and software lead, CR-011)"
reviewer_agent: "sa-reviewer:WP-PDR-06-code"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-06-code (software assurance function; paired file review INSP-042 by reviewer:WP-PDR-06-code-and-tv and reviewer:WP-PDR-06-code-delta)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (no Major; one Minor finding, a lien due the CDR
# readiness declaration under PDR work plan rule C1 unless fixed on the CR-011 branch before the merge)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES under the lead SE convention of
# 2026-09-27 (INSP-031 practice): eighteen reviewed blobs exist only on the unmerged branch
# cr/CR-011-traceability-pdr-rules, and the checklist applied only on cr/CR-012-pdr-checklist-templates. Both
# reviews of the product are APPROVED (INSP-042 reviewer_verdict APPROVED; this record). The software lead sets
# verdict APPROVED on both records in the CR-011 merge commit (or the commit right after it) when the blobs reach
# main unchanged and INSP-042 carries the pairing (X-1); a blob change before then needs a delta iteration of both
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 1
findings_open: 1
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 1
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-060 7.1 task 1", "swe-060 7.1 task 2", "swe-061 7.1 task 1", "swe-061 7.1 task 2", "swe-207 7.1 task 1", "swe-185 7.1 task 1", "swe-135 7.1 task 1", "swe-062 7.1 task 1", "swe-062 7.1 task 2", "swe-052 7.1 task 1", "swe-052 7.1 task 2", "swe-192 7.1 task 1", "swe-071 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-080 7.1 task 3", "swe-081 7.1 task 1", "swe-081 7.1 task 2", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-200 7.1 task 1", "swe-090 7.1 task 1", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-088 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: []
deferred_rids: []
items_no: ["swe-062 7.1 task 1"]
effort_turns: 40
effort_minutes: 75
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-070: software assurance pair of INSP-042, code review of `tools/traceability.py` blob `d4cde9f5` (WP-PDR-06, CR-011)

**Product.** `tools/traceability.py` blob `d4cde9f5` at the CR-011 branch head `2b004b1`, with the other eighteen `product_files` of INSP-042 iteration 2 (seventeen further blobs on the branch, the CR-011 file `892670b6` of `main` `7bb994f`). Identity checked with `git rev-parse 2b004b1:<path>` (and `7bb994f:` for the CR file): all nineteen equal INSP-042. The branch head has not moved since INSP-042 iteration 2 (`git rev-parse cr/CR-011-traceability-pdr-rules` = `2b004b1`).

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged). Sections R, A, B, D, E and F are applied. Section C (SWE-134 a to l) is N/A for criticality neither. Section D is applied to the hazard checks the tool performs. `product_type` code.

**Acceptance criteria (rule C7).** Every task of the section B rows "Every product type" and "code"; the section 7.1 tasks of every SWE the tool implements or supports (front matter list); each INSP-042 finding (finding-1 to finding-8) re-read under the assurance lens; each safety-designated check the CR-011 change adds or promotes (`HAZARD_UNCONTROLLED`, `SAFETY_PART_UNTRACED`, `HAZARD_INVERSE` under `--gate`, the `GATE_ERROR_FROM` promotion rule, the 02 section 10.2 Class I classification of `hazard_ids` and the `safety` tag) confirmed to have a known answer that discriminates each clause; the INSP-051 hazard-trace and SWE-192 mutants are not repeated.

**Independence (rule C4).** This invocation (`sa-reviewer:WP-PDR-06-code`) authored no part of WP-PDR-06, CR-011, TV-002, the tool or its tests. It wrote none of INSP-042, INSP-043, INSP-051 or the CR-011 section 6.1 review, and it edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "software assurance peer review checklist SWEHB assurance tasks SWE-052 SWE-136 tool traceability"; "07 section 2.1.1 software assurance second review paired record slug-software-assurance.md"; "coding standard for Python tools under tools/ linter static analysis host tool rigor 03 section 6.1.1 peer review row"; "risk register entry Python static analyzer coverage tool not installed owner download permission A-1 TV-024"). `grep -n` and read-only scripts were used afterwards only to pin lines and to extract the SWEHB section 7.1 lists. The rustos working tree was not read: `--rustos` pointed the tool's `git show` reads at the rustos repository objects. LTspice was not run.

**Lead SE convention.** The reviewed blobs exist only on the unmerged branch `cr/CR-011-traceability-pdr-rules`. This record sets `reviewer_verdict` and `assurance_verdict` on its own. It holds `verdict` and is committed on `main`. The software lead sets `verdict` in the CR-011 merge commit or in the commit right after it.

## Assurance re-runs and checks

All work ran in an export (`git archive 2b004b1`) and a detached scratch worktree of `2b004b1` under the session scratchpad. The worktree was removed afterwards.

| # | Check | Result |
|---|---|---|
| S0 | Blob identities: `git rev-parse 2b004b1:<path>` for the eighteen branch entries, `7bb994f:` for the CR file; `git hash-object` of the eight code and output files in the export | all nineteen equal INSP-042 `product_files` |
| S1 | `unittest discover -s tools/tests -p 'test_traceability*.py'` and `-p test_tools.py` in the export | 121 tests `OK` and 117 tests `OK`, none skipped |
| S2 | Independent static analysis (stdlib `ast` script; no analyzer is installed, TV-024 Draft): unused imports, bare or broad `except`, `shell=` keyword, `eval`, `exec`, `os.system`, `popen`, unused locals, functions over 60 lines, over `tools/traceability.py` and `test_traceability.py`; `py_compile` with `-W error` | no bare or broad `except`, no `shell=`, no `eval`, `exec`, `system` or `popen`, no unused import or local (only `from __future__ import annotations`, which is a directive); compiles with warnings as errors. Functions over 60 lines: `load_allocation` 64, `load_upstream` 65, `check_verification` 74, `volatility_record` 62 (CR-011), `render_expectations` 114, `build_report` 199. CS-18 does not apply to tools (INSP-042 R2) |
| S3 | Argument-injection probe (swe-185, swe-207): `--volatility --from=--output=<scratch>/pwn2.txt --gate PDR --dry-run` and `--from=--all` in the worktree; `git rev-parse --verify --quiet "--output=<scratch>/pwn.txt^{commit}"` | exit 2 with "does not name a commit"; no file written. Every ref from the command line passes `GitHistory.resolve` (`rev-parse --verify --quiet <ref>^{commit}`, `:2562`) before any `git show` or `git log`. The rustos `git show` argument starts with the 40-hex lock commit (`:2306`). Every `subprocess.run` passes an argument list |
| S4 | Option set against the design: `add_argument` options of the tool against the README and the 02 section 8.1 synopsis and option table (swe-060 task 2) | all 14 options (`--dry-run`, `--fix-children`, `--from`, `--gate`, `--json`, `--output`, `--quiet`, `--regression`, `--render`, `--report-only`, `--root`, `--rustos`, `--to`, `--volatility`) are documented in both. Acceptance of status `Retired` in `Requirement.is_retired` (`:554`) is covered by 02 section 11.3 (line 670, "status *Retired* where its schema has that status") |
| S5 | Eleven mutants of the PDR safety and gate rules in the export, each run against the `test_traceability*.py` and `test_tools.py` modules (M1 `HAZARD_UNCONTROLLED` gate entry removed; M2 `SAFETY_PART_UNTRACED` gate entry removed; M3 `HAZARD_UNCONTROLLED` emission disabled; M4 the "live" filter of `check_hazard_control` removed, `:2466`; M5 the "retired" clause of `check_safety_parts` removed, `:2378`; M6 safety-part hazard-trace test disabled; M7 no-marked-element check disabled; M8 `is_error_at` `>=` to `>`; M9 `DESIGN_REF_MISSING` gate entry removed; M10 `HAZARD_INVERSE` promoted from PDR instead of SRR; M11 empty `requirement_ids` accepted on a safety part) | killed: M1 1 failure, M2 1, M3 1, M6 1, M7 2, M8 5, M9 1, M10 2, M11 1. **Survive: M4 and M5**, all tests `OK` in both modules (finding-1) |
| S6 | Two mutants of the 02 section 10.2 classification (`:2775`, `:2776`): M12 `hazard_ids` removed from `CLASS_I_REQ_FIELDS`; M13 `safety` removed from `CLASS_I_TAGS` | **both survive**, all tests `OK` (finding-1) |
| S7 | Export restored and re-hashed after S5 and S6 | `traceability.py` `d4cde9f5` |
| S8 | Hand check on the original blob of the M4 and M5 clauses, in memory with the test module's helpers: `HZ-001` given `firmware_criteria ["a"]` with its only software control `REQ-SW-KEYER-001` set to `Retired`; `B21` marked `safety_critical` with `REQ-SYS-006` set to `Retired` | before retirement, no `HAZARD_UNCONTROLLED`; after it, `HAZARD_UNCONTROLLED` at `HZ-001` (warning plain, violation under `--gate PDR`). `SAFETY_PART_UNTRACED` "names requirements that do not exist or are retired: REQ-SYS-006" (violation under `--gate PDR`). The code is correct today; only its known answers are missing |
| S9 | Plain and `--gate PDR` runs of the branch tool on the `2b004b1` worktree (`--rustos /Users/robinonsay/rust/rustos`, scratch `--output` and `--json`) | plain exit 0, 0 violations, 95 warnings, including 4 `HAZARD_UNCONTROLLED`; `--gate PDR` exit 1, 379 violations, including 4 `HAZARD_UNCONTROLLED` and 1 `SAFETY_PART_UNTRACED`. Equal to TV-002 R-3 and INSP-042 C4, C5. Worktree `git status` clean |
| S10 | Catalogue diff `git diff a3cacee 2b004b1 -- tools/traceability.py` for the hazard and safety codes | CR-011 weakens no earlier safety check. `HAZARD_INVERSE` stays a plain-run warning, as at `a3cacee`, and becomes a violation under `--gate` at every gate. `HAZARD_REQ_NOT_ON_TARGET` widens to `Verified` under `--gate SAR`. `HAZARD_UNCONTROLLED` and `SAFETY_PART_UNTRACED` are new |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-062 7.1 task 1 | `tools/traceability.py:2466` (`check_hazard_control`, "live" filter), `:2378` (`check_safety_parts`, "retired" clause), `:2775` and `:2776` (`CLASS_I_REQ_FIELDS` `hazard_ids`, `CLASS_I_TAGS` `safety`), blob `d4cde9f5`; `tools/tests/test_traceability.py:732` (`HazardControlTests`), `:752` (`SafetyPartTests`), `:983` (`test_change_control_classes_and_coverage`) | Four clauses that carry safety meaning have no discriminating known answer. When each is removed (S5 M4, M5; S6 M12, M13), all tests of `test_traceability*.py` and `test_tools.py` still pass. (a) `HAZARD_UNCONTROLLED` counts only a **live** `REQ-SW-*` as the software control of a hazard with a firmware role (03 section 8 row 2, SWE-052 Table 1 row 2). Without the filter, a retired control silently satisfies the hazard. (b) `SAFETY_PART_UNTRACED` rejects a **retired** requirement on a safety-critical hardware part (SRR memo section 9 condition 5). Without the clause, a retired requirement satisfies the part. (c) and (d) 02 section 10.2 puts `hazard_ids` and the `safety` tag in Class I. If either is demoted, a change to hazard trace data is reported as Class II in `CHANGE_UNCOVERED` and in report section 12, which understates it to the CR reviewer. The code is correct at `d4cde9f5` (S8), so no output is wrong today. But ACC-TRACE-002 would accredit these clauses with no test that holds them, and a later edit that breaks one would pass the re-validation run of TV-002 section 7. This is the same kind of gap as INSP-051 finding-1 (a hazard-trace direction) and INSP-042 finding-6 (exact finding sets). It is raised separately because it affects other branches, found by mutants, which the SWE-062 SA task marks "particularly those testing safety-critical functions". Fix: add known answers. (a) a hazard with `firmware_role.criteria` whose only `REQ-SW-*` is retired gives `HAZARD_UNCONTROLLED`, a warning plain and a violation under `--gate PDR`. (b) a marked element whose only requirement is retired gives the "retired" message. (c) and (d) a post-baseline change of `hazard_ids`, and one adding or removing the `safety` tag, classifies as Class I. Then add M4, M5, M12 and M13 to the TV-002 step 3b mutant set | Open | Pending | |

**Paired record findings under the assurance lens (not raised again; template finding rules).**
- INSP-042 finding-1 (T-13 coverage by id only): concur at Minor. Under swe-080 task 3, an approved CR covers every later change to its ids, which weakens the automated change-control check on hazard-tracing requirements too. The CR peer review and the swe-082 audit remain as independent controls, so the severity does not rise (as INSP-051 found).
- INSP-042 finding-2 (`child_ids` editorial acceptance): concur at Minor. `child_ids` is a derived field whose authority is `parent_id` (02 section 10.2 Editorial row). Its silent acceptance leaves no safety data unchecked, because `parent_id` and `hazard_ids` stay Class I.
- INSP-042 finding-3 (T-12 evidence cells; PDR-to-CDR re-plan unstated): concur at Minor. Under swe-080 task 2 d, the unchecked `NCR-NNN` evidence for `Verified` to `Active` and `Failed` to `Active` matters most for hazard-tracing requirements. It is a CDR item and stays with the tool owner. The owner must be told of the re-plan in CR-011 section 1 before disposition (rule C6).
- INSP-042 finding-4 (Draft scope of T-15 and T-18): concur at Minor. The wider scope is the safer direction, because it fires earlier.
- INSP-042 finding-5 (MSR-02 appended without a schema check): concur at Minor, as INSP-051 did under swe-200 task 1.
- INSP-042 finding-6 (single-code assertions): concur at Minor. finding-1 here is a separate gap (a missing clause test, not a weak assertion).
- INSP-042 finding-7 (stale `check_allocation` docstring; exit status 2 not in the module docstring): concur at Minor. Under swe-060 task 1 the module docstring **is** the tool's design (03 section 6.1.1 row "Design and code": "The module docstring states the design (inputs, checks, outputs, exit codes)"), so this is a design-to-code difference, not only a style item. The severity does not rise, because 02 section 8.1 states exit 2 and the known answers test it.
- INSP-042 finding-8 (README and CR-011 section 1 omit `RegressionSetTests`): concur at Minor.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the code review of a tool whose output feeds safety-critical evidence (hazard trace, SWE-192, safety-critical hardware parts, the PDR gate). Dispatched by plan WP-PDR-06 and INSP-042 X-10 | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed by this record against 07 section 15, the project's software assurance plan. The NASA-STD-8739.8 part is relieved (`rmm.json` SWE-022 T) | | none |
| swe-060 7.1 task 1 | | Yes | The design of a tool is its module docstring and its commissioning section (03 section 6.1.1 row "Design and code"): the module docstring (`:1` to `:73`), 02 sections 8 and 10, and the README. INSP-042 CK-CODE-E1 checked the 22 T-rules and the 04 rules clause by clause. The deviations it found are Minor liens: finding-1 to finding-5, and finding-7 for the docstring as design (concurred above) | | none (INSP-042 finding-1 to finding-5, finding-7) |
| swe-060 7.1 task 2 | | Yes | S4: every option is in the README and in 02 section 8.1. Every new check is in `CHECK_CATALOGUE` and the README "Rule coverage", and `CatalogueKnownAnswerTests` (`test_tools.py`) fails on a catalogue code with no known answer. No undocumented function is reachable from `main` (INSP-042 CK-CODE-E9) | | none |
| swe-061 7.1 task 1 | | Yes | For tools, the coding method is the one 03 section 6.1.1 defines: the standard library and the pinned venv (row "Design and code"), and the code checklist adapted to Python (row "Peer review"). No Python style standard or analyzer rule set is in force yet. TV-024 (ruff, Draft) will bring one under 03 section 6.5 item X9, which waits on owner action A-1 (cross item X-3) | | none |
| swe-061 7.1 task 2 | | Yes | New imports are standard library only (`hashlib`, `subprocess`, `datetime`, plus `dataclasses` in the test module). The only third-party package is `jsonschema`, reached through `validate_docs`. S2 found no defect pattern | | none |
| swe-207 7.1 task 1 | | Yes | The tool code checklist carries secure-coding items (section G, CS-29 to CS-33, applied by INSP-042 CK-CODE-G1 adapted). 03 section 6.1.1 row "Static analysis and secure coding" plans the Python analyzer for PDR and makes the code peer review the check until then | | none |
| swe-185 7.1 task 1 | | Yes | Independent analysis S2 and S3: argument lists only, no shell, command-line refs verified before use, no `eval` or `exec`. The one external input that reaches `git` unverified is the lock-file commit, which the `FORTY_HEX` pattern bounds (`:2287`) | | none |
| swe-135 7.1 task 1 | | Yes | Independent analysis S2 for defects and security (stdlib `ast`). Complexity is measured only as function length, because no complexity tool is locked. Coverage is not measured, but the mutants S5 and S6 stand in for it on the safety clauses (finding-1) | | finding-1 |
| swe-135 7.1 tasks 2, 3, 4 and 7 | 2 SC | N/A | No Python static analyzer is installed or configured (TV-024 Draft; lock rows ruff and coverage.py "Not installed"). The product is of criticality neither | `rmm.json` SWE-135 ("Static analysis of the project's Python tools ...: Planned for PDR (03 section 6.1.1)"); 03 section 6.5 item X9 | none |
| swe-135 7.1 tasks 5 and 6 | SC | N/A | SWE-219 and SWE-220 apply to safety-critical software; no tool is safety-critical | 03 section 6.1.1 row "Safety and mission-critical rows" | none |
| swe-134 7.1 task 2 | SC | N/A | Items a to l apply to safety-critical and mission-critical code | 03 section 6.1.1 row "Safety and mission-critical rows" | none |
| swe-134 7.1 task 3 | SC | N/A | The tool holds no loaded data of a delivered unit | 03 section 6.1.1 row "Release, delivery, loaded-data and auto-generation rows" | none |
| swe-087 7.1 task 4 | SC | N/A | SWE-134 a to l at code review apply to safety-critical code | 03 section 6.1.1 row "Safety and mission-critical rows" | none |
| swe-219 7.1 task 1; swe-220 7.1 tasks 1 and 2 | SC | N/A | Safety-critical components only | 03 section 6.1.1 row "Safety and mission-critical rows" | none |
| swe-062 7.1 task 1 | SC | No | The unit tests run and pass (S1; INSP-042 C10: 477 tests, 1 failure, which is record drift). The known answers kill nine of eleven safety and gate mutants (S5) but not the "live" and "retired" clauses or the Class I safety fields (S5 M4, M5; S6 M12, M13) | | finding-1 |
| swe-062 7.1 task 2 | | Yes | The one failing test of the full suite (`test_repository_exit_zero`, the INSP-015 and INSP-020 record drift) is tracked by TV-002 limitation 6, CR-011 section 4 and 02 section 8.5. INSP-042 findings are tracked as liens with a due event | | none |
| swe-052 7.1 task 1 | | Yes | The tool records and checks SWE-052 Table 1 rows 1, 2, 3 (T-15 from PDR), 5 and 6. Row 4 is due before CDR, as the docstring and 03 section 8 state. On the repository, S9 reproduces the matrices and the counts | | none |
| swe-052 7.1 task 2 | SC | Yes | The hazard trace checks run both ways (the INSP-051 mutants cover them). The CR-011 hazard-control check `HAZARD_UNCONTROLLED` and the safety-part check work on the repository (S9: 4 and 1 under `--gate PDR`) and are correct on the original blob (S8). The missing known answers are under swe-062 task 1 | | finding-1 |
| swe-192 7.1 task 1 | SC | Yes | `HAZARD_REQ_NOT_TESTED` is unchanged in its SW branch. `HAZARD_REQ_NOT_ON_TARGET` widens to `Verified` under `--gate SAR` (S10). Both are discriminated by the INSP-051 S4 mutants | | none |
| swe-071 7.1 task 1 | SC | Yes | `CASE_STALE` (04 rule 7.3.11) flags cases whose cited requirement's `description`, `verification_method`, `verification_note` or `tbr` changed after the case became Active (INSP-042 CK-CODE-E1). The adequacy of off-nominal coverage is the test reviewer's to judge | | none |
| swe-080 7.1 task 1 | SC | Yes | Impact of CR-011 on safety: no earlier hazard check is weakened (S10). The change adds two safety checks and promotes `HAZARD_INVERSE` under `--gate`. Security: S3. The weak points are the finding-1 test gaps and INSP-042 finding-1 (concurred) | | finding-1 |
| swe-080 7.1 task 2 | | Yes | a: CR-011 file on `main` (`b01b9cd`, `7bb994f`, `86ff3b0`). b: the tool is changed only on `cr/CR-011-traceability-pdr-rules` before disposition, and the section 6.1 review (`86ff3b0`) precedes the owner ask (rule C6). c: section 5 steps 1 to 3a done. d: runs 6 and 7, INSP-042, INSP-043, INSP-051 | | none |
| swe-080 7.1 task 3 | | Yes | Branch commits carry `CR: CR-011` (INSP-051 S9, unchanged since). The branch head is still `2b004b1` | | none |
| swe-081 7.1 task 1 | | Yes | The tool is a class-CR item (05 Table 4-1 row 28). Every reviewed file is identified by blob (front matter) | | none |
| swe-081 7.1 task 2 | SC | Yes | The tool reads `hazards.json`, `allocation.json` and the requirement files as committed CIs. It writes only the report outputs, the `--render` files, `child_ids` under `--fix-children` and the MSR-02 record. It enforces Class I control of `hazard_ids` and the `safety` tag (T-13), and finding-1 (c) and (d) covers the missing known answer for that | | finding-1 |
| swe-136 7.1 task 1 | | Yes | Blob `d4cde9f5` is validated (TV-002 runs 6 and 7, reproduced in part by S1 and S9) and reviewed (INSP-042, INSP-043, INSP-051, this record), and not yet accredited. TV-002 holds its output as developer evidence until ACC-TRACE-002 | | none |
| swe-070 7.1 task 1 | | Yes | The tool's matrices and gate checks are qualification evidence (04 section 7.3; 01 section 3.1 item 2). Its accreditation route is TV-002, as above | | none |
| swe-200 7.1 task 1 | | Yes | `--volatility` computes MSR-02 per 02 section 10.4 (INSP-042 C6, C12). Its schema-check gap is INSP-042 finding-5 (concurred) | | none |
| swe-200 7.1 task 2 | | N/A | No MSR-02 record exists yet to analyze | 07 section 11.3 (analysis at each gate package) | none |
| swe-090 7.1 task 1 | | Yes | The tool produces MSR-01, 03, 04 and 23 in `traceability.json`, and MSR-02 through `--volatility` | | none |
| swe-087 7.1 task 1 | | Yes | INSP-042 iterations 1 and 2 were performed and recorded. This record is the SA pair | | none |
| swe-087 7.1 task 2 | | Yes | INSP-042 has no Major finding. Its eight Minor findings are liens with the tool owner as owner and the CDR readiness declaration as due event (INSP-042 "Iteration 1 findings at this delta") | | none |
| swe-088 7.1 task 1 | | Yes | INSP-042 met SWE-088 a to d: the code checklist revision B (a), readiness R1 to R6 (b), findings with state (c), participants named (d) | | none |
| swe-088 7.1 task 2 | | Yes | The actions are tracked in the INSP-042 cross items X-1 to X-10, each with an owner | | none |
| swe-089 7.1 task 1 | | Yes | INSP-042 and this record carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes` and `iteration` | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | S0: all nineteen blobs equal INSP-042 iteration 2. The CR file on `main` has moved to `49461a58` since then (INSP-042 X-7). Both records keep `892670b6` until the merge-time delta |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | Row "code". Criticality neither (03 sections 4.3.1 and 6.1.1). Dispatched by plan WP-PDR-06 ("SA second review (tool used for credit)"), since the row routes only safety-critical or mission-critical code or `unsafe` code |
| R3 | `validate_docs.py` exit 0 on the product's files; `traceability.py --report-only` with a scratch `--output` reports no violation for the ids touched | Yes | The product touches no requirement, case or hazard id. On the branch, INSP-042 C11 records 48 passed and 2 failed (the INSP-015 and INSP-020 drift that TV-002 limitation 6 states). On `main` this record passes `validate_docs.py` (Commands) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-042 iteration 2 is committed on `main` (`0743499`) with `author_agent` "author:WP-PDR-06" and reviewers `reviewer:WP-PDR-06-code-and-tv` and `reviewer:WP-PDR-06-code-delta`. This invocation is `sa-reviewer:WP-PDR-06-code` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | Row "code" of 07 section 2.1.1. The tool is of criticality neither, and the dispatch is plan WP-PDR-06, which requires the SA second review because the tool's output is used for credit (INSP-042 front matter comment on `assurance_required`) |
| SA-A2 | Yes | Four invocations are recorded: author `author:WP-PDR-06`, file reviewers `reviewer:WP-PDR-06-code-and-tv` (iteration 1) and `reviewer:WP-PDR-06-code-delta` (iteration 2), and this assurance reviewer. INSP-042 does not yet name this record (X-1) |
| SA-A3 | Yes | Same product, same `product_commit` `2b004b1`, and the same nineteen blobs. A change before the merge needs a delta of both records (rule C2) |
| SA-A4 | Yes | INSP-042 applied `peer-review-checklist-code.md` revision B, the checklist 03 section 6.1.1 row "Peer review" assigns to tool source. Every item is answered with evidence, and the Rust-only items are N/A with a reason |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: the "Every product type" row, every task of the "code" row, and the section 7.1 tasks of SWE-052, 192, 071, 080, 081, 136, 070, 200, 090, 087, 088 and 089. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | Each N/A row cites the `rmm.json` SWE-135 row, 03 section 6.1.1 or 07 section 11.3. The SC tasks answered N/A are those whose condition (safety-critical code, loaded data) 03 section 6.1.1 records as not met for tools |
| SA-B3 | Yes | swe-062 task 1 (No) is carried by finding-1 |

## C. SWE-134 items a to l

N/A for every item: the `criticality` is neither (03 section 6.1.1 row "Safety and mission-critical rows"; 07 section 14.1 lists no tool component), so `swe134_items_checked` is empty.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | N/A | The product changes no hazard and adds no software contribution (CR-011 Safety row) |
| SA-D2 | N/A | No component is created or renamed, and 07 section 14.1 is unchanged |
| SA-D3 | Yes | The tool checks the hazard trace both ways. INSP-051 records one direction without a known answer (its finding-1). CR-011 adds the hazard-to-software-control check (`HAZARD_UNCONTROLLED`), and on the repository it reports the 4 hazards whose firmware role has no live `REQ-SW-*` yet (S9). The missing known answer for its "live" clause is finding-1 |
| SA-D4 | N/A | No safety-tagged software requirement changes |
| SA-D5 | Yes | `HAZARD_REQ_NOT_TESTED` enforces SWE-192 with no exception for `SW` and `SW-<SUB>` (unchanged; INSP-051 S4) |
| SA-D6 | N/A | The hazard analysis is not re-issued by this product |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-042 has no Major finding. Its Minor findings are Open liens, and none is closed without evidence |
| SA-E2 | Yes | INSP-042 and this record carry the 07 section 10.3 measurements |
| SA-E3 | Yes | swe-080 tasks 2 and 3 rows. The tool is a class-CR item changed only on its CR branch before disposition |
| SA-E4 | N/A | No item under test and no credit run in this product |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | One assurance concern that is not a defect of this product is submitted to the risk register writer (WP-PDR-18) as cross item X-3, for an entry with tag `assurance`. The concern: the tool analyzer and coverage (03 section 6.5 item X9, TV-024) wait on owner action A-1, and until they run, only mutation checks by reviewers stand in for coverage of a credit-bearing tool. finding-1 and INSP-051 finding-1 show the gaps that branch coverage would expose |
| SA-F2 | Yes | The front matter carries `findings_*`, `assurance_findings_major` 0 and `assurance_findings_minor` 1 (the same finding, counted once, 07 section 10.2), `items_no` and effort |
| SA-F3 | Yes | Verdict, open finding, tasks applied and reliefs are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true. Every task that SA-B1 requires is in the task table. Every applicable item of sections A, D, E and F is answered, and section C is N/A with its reason. There are zero Major findings. The one Minor finding is Open. Under PDR work plan rule C1 and 08 section 3.2 ("Minor findings ride with APPROVED"), it is written for the tool owner to fix on the CR-011 branch before the merge. If it is not fixed by then, it is a lien due at the CDR readiness declaration, listed in PDR package section 15. A fix before the merge changes blobs of `product_files`, and then both records need a delta iteration (rule C2).

`assurance_verdict: APPROVED`. INSP-042 has `reviewer_verdict: APPROVED`, so both reviews of the product are APPROVED. The record `verdict` stays NEEDS CHANGES under the lead SE convention: the reviewed blobs are on the unmerged CR-011 branch, and the software lead sets APPROVED at the merge.

## Cross items (returned to Claude)

- **X-1.** INSP-042 (`code-tools-traceability.md`) reads `assurance_reviewer_agent: "pending: ..."` and `assurance_verdict: pending`, and it has no `paired_record`. Its reviewer updates it to `paired_record: INSP-070`, names this reviewer and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row). This closes INSP-042 X-10.
- **X-2.** At the CR-011 merge, the delta iterations of INSP-042 and this record name the CR file blob then read, or drop the CR file from `product_files` as context (INSP-042 X-7; CR-011 section 5 step 5). After CR-012 merges, the delta also switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `assurance_checklist`.
- **X-3.** Risk entry for the WP-PDR-18 writer, tag `assurance`: the Python analyzer and coverage for the tools (03 section 6.5 item X9, TV-024 Draft) wait on owner action A-1. Until they run, the credit-bearing tool `tools/traceability.py` has no measured branch coverage, and mutation checks in the reviews stand in. Owner action A-1 is outside this WP.
- **X-4.** TV-002 step 3b mutant set: when finding-1 is fixed, the tool owner adds M4, M5, M12 and M13 (this record S5 and S6) beside the INSP-051 finding-1 mutant, so that re-validation after a tool change holds each safety clause.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse 2b004b1:<path>` for the eighteen branch `product_files`; `git rev-parse 7bb994f:docs/cm/cr/CR-011-traceability-pdr-rules.md`; `git rev-parse cr/CR-011-traceability-pdr-rules` | 0 | S0; the branch head is `2b004b1` |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md`; `git rev-parse` of that path | 0 | Template revision A, blob `5b135285` |
| `git archive 2b004b1` into the scratchpad; `git hash-object` of the code and output files | 0 | S0 |
| `unittest discover -s tools/tests -p 'test_traceability*.py'` and `-p test_tools.py` in the export | 0, 0 | S1: 121 and 117 tests, OK |
| `ast` scan script and `python -W error -m py_compile tools/traceability.py` in the export | 0 | S2 |
| `git worktree add --detach <scratch>/wt42 2b004b1`; S3 probes; S9 plain and `--gate PDR` runs with scratch `--output` and `--json`; `git worktree remove --force` | 2, 2, 0, 1, 0 | S3, S9; worktree removed |
| Thirteen mutants by exact text substitution in the export, each run against both test patterns; export restored and re-hashed | varies | S5, S6, S7 |
| In-memory hand check with `test_traceability` helpers (`load_project`, `rerun`, `of`) | 0 | S8 |
| `git diff a3cacee 2b004b1 -- tools/traceability.py` filtered on the hazard and safety codes | 0 | S10 |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-060, 061, 207, 185, 135, 087, 062, 134, 052, 136, 080, 200, 192, 071, 081, 090, 070, 022, 088, 089, 054 | 0 | Task texts of the task table. SC marks follow the template's section B rows and INSP-051 |
| `.venv/bin/python tools/validate_docs.py` on `main` | see summary | This record PASS |

## Verdict format

```
ASSURANCE VERDICT: APPROVED
PRODUCT: tools/traceability.py@d4cde9f5 (and the eighteen other INSP-042 product_files) at 2b004b1; PAIRED RECORD: INSP-042
PRODUCT TYPE: code; CRITICALITY: neither
FINDINGS:
- [Minor] swe-062 7.1 task 1 the live clause of HAZARD_UNCONTROLLED, the retired clause of SAFETY_PART_UNTRACED and the Class I classification of hazard_ids and the safety tag have no known answer; four mutants survive every test.
TASKS APPLIED: swe-134 task 5, swe-022 task 1, swe-060 tasks 1 and 2, swe-061 tasks 1 and 2, swe-207 task 1, swe-185 task 1, swe-135 task 1, swe-062 tasks 1 and 2, swe-052 tasks 1 and 2, swe-192 task 1, swe-071 task 1, swe-080 tasks 1 to 3, swe-081 tasks 1 and 2, swe-136 task 1, swe-070 task 1, swe-200 task 1, swe-090 task 1, swe-087 tasks 1 and 2, swe-088 tasks 1 and 2, swe-089 task 1
TASKS N/A (relief): swe-135 tasks 2, 3, 4, 7 (rmm.json SWE-135; 03 section 6.5 X9), swe-135 tasks 5 and 6, swe-134 tasks 2 and 3, swe-087 task 4, swe-219 task 1, swe-220 tasks 1 and 2 (03 section 6.1.1), swe-200 task 2 (07 section 11.3)
SWE-134 ITEMS CHECKED: none (criticality neither)
MEASUREMENTS: size=4156 lines (1465 added), 19 product files; tasks=42; tasks_no=1; mutants=13 (9 killed, 4 survived); turns=40; minutes=75; major=0; minor=1
```
