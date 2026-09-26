# tools/: validation, traceability and review-trend tooling

Three Python 3 scripts check the requirement, test case, hazard, review and evidence files of the repository and generate the matrices and trends that every review package carries (charter sections 4, 5, 7 and 9). All run from the repository root through the project virtual environment; no file is executable on its own.

```sh
.venv/bin/python tools/validate_docs.py                    # every JSON document, peer-review record and decision memo against its schema
.venv/bin/python tools/traceability.py                     # traceability checks, report and data file
.venv/bin/python tools/traceability.py --render            # same, after rendering expectations.md and every requirements.md
.venv/bin/python tools/review_trend.py --date YYYY-MM-DD   # review-trend TPM (TPM-003) summary
.venv/bin/python -m unittest discover -s tools/tests       # known-answer tests (the SWE-136 validation of 05 section 9.2)
```

The software gate `tools/sw_gate.sh` (07 section 8.4) runs three further scripts of this directory, written on 2026-09-26 (SRR package item R3; sections below): `measurements.py` (G2, G3, G6), `unsafe_audit.py` (G5) and `complexity_gate.py` (G5, fed by `rust-code-analysis-cli`).

**Accreditation status (SWE-136).** `validate_docs.py`, `traceability.py`, `review_trend.py`, `render_review_figures.py`, `unsafe_audit.py`, `complexity_gate.py` and `measurements.py` are class B evidence-generating tools (05 section 9.1). Their tool validation records are TV-003 (`validate_docs.py`), TV-002 (`traceability.py`), TV-007 (`review_trend.py`), TV-010 (`render_review_figures.py`), TV-011 (`unsafe_audit.py`), TV-012 (`complexity_gate.py`) and TV-013 (`measurements.py`) in `docs/cm/tool-validation/`, with TV-001 for the Python and jsonschema runtime they share. Section 3 of TV-001 to TV-010 was re-run at commit `400e59d` on 2026-09-26 (SRR package item R5). None is accredited yet: the records are filed and under independent review (`docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`). Until the owner records the accreditation in those TV records (05 section 9.2 step 3), the output of these tools is developer evidence only and a review package cites it as such.

**Dependencies.** The venv is recorded, with versions, in `tools/toolchain.lock.md` section 2: `jsonschema` (all three tools), PyYAML for YAML front matter (a subset parser in `validate_docs.py` is the fallback), and matplotlib for the `review_trend.py --write` figure and for `render_review_figures.py`. Everything else is the standard library. `tools/requirements.txt` lists the direct dependencies of the venv without versions; matplotlib was added to it on 2026-09-25 with `render_review_figures.py`, its first direct importer outside `review_trend.py`. Pinning every package with `==` remains lock action AL-4 (05 section 9.3), an SRR readiness prerequisite (owner: Claude as maintainer of the lock).

Other scripts in this directory carry their own usage in their docstrings: `render_rmm.py` (Requirements Mapping Matrix), `render_compliance.py` (NPR 7123.1D compliance matrix), `render_risk.py` (risk register), `render_review_figures.py` (review-package and deck figures, section below), `slides/render_deck.py` (review decks), `refs/` (corpus conversion).

## validate_docs.py

Discovers documents by path convention and validates each against its schema (JSON Schema draft detected from `$schema`). A document at a conventional path whose schema file is absent is a failure. This is a design decision of this tool based on `docs/process/05-configuration-and-data-management.md` section 10.2, where authoritative JSON is "JSON validated by the row 9 schemas", and Table 4-1 row 9, where every schema gates validation evidence.

| Document | Schema | State on 2026-09-26 |
|---|---|---|
| `docs/requirements/**/requirements.json` | `docs/requirements/schema.json` | validated |
| `docs/requirements/l0-stakeholder/expectations.json` | `docs/requirements/l0-stakeholder/schema.json` | validated |
| `docs/test_cases/**/test_cases.json` | `docs/test_cases/schema.json` | validated when a file exists |
| `docs/risk/register.json` | `docs/risk/schema.json` | validated |
| `docs/safety/hazards.json` | `docs/safety/schema.json` | validated |
| `docs/process/rmm.json` | `docs/process/rmm.schema.json` | validated |
| `docs/process/se-compliance-matrix.json` | `docs/process/se-compliance-matrix.schema.json` | validated (`render_compliance.py --check` adds the App. H cross-check) |
| `docs/plan/tpm.json` | `docs/plan/tpm.schema.json` | validated, including every `history` entry against `history_entry` (`conventions.history_entry_shape`), so the entries `review_trend.py --write` appends are checked |
| `docs/plan/measurements.json` | `docs/plan/measurements.schema.json` | validated (the SRR seed of 2026-09-25 and the append of 2026-09-26; schema committed 2026-09-26 with the known-answer fixture `tools/tests/fixtures/measurements/` and `MeasurementsSchemaKnownAnswerTests` in `test_tools.py`). The cross-record rules JSON Schema cannot express (append-only order, supersedes resolution, evidence hash equal to the committed file) wait for `tools/measurements.py` (07 section 11.1) |
| `docs/design/allocation.json` | `docs/design/allocation.schema.json` | validated (preliminary at SRR, baselined at PDR, SEMP section 4.3; schema committed 2026-09-26, INSP-003 finding-9). The fixture copy `tools/tests/fixtures/valid_project/docs/design/allocation.schema.json` equals it (`SchemaTripwireTests.test_allocation_schema`) |
| `docs/reviews/*/rfa-rid-log.json` | `docs/templates/rfa-rid-log.schema.json` | validated when a log exists |
| `docs/templates/<name>.example.json` | `docs/templates/<name>.schema.json`, else the alias for `<name>` (`requirements`, `test_cases`, `expectations`, `register`, `hazards`, `rmm`, `se-compliance-matrix`, `tpm`, `measurements`, `allocation`) | validated; `rfa-rid-log.example.json` also gets the item and history rules below |
| `docs/reviews/*/checklists/<product-slug>.md` (YAML front matter) | built-in `PEER_REVIEW_RECORD_SCHEMA` (01 section 13; optional `product_files` and `product_blob` patterns added 2026-09-26 for the record drift rule): required `id` (`INSP-NNN`), `checklist` (pattern `^peer-review-checklist-[a-z]+(-[a-z]+)*$`, so hyphenated stems such as `peer-review-checklist-visual-product` are valid; a file in `docs/templates/`), `product`, `product_commit` (7 to 40 hex digits, quoted when all digits), `verdict` (`APPROVED` or `NEEDS CHANGES`), `author_agent`, `reviewer_agent`, `iteration` (1 to 3), `date`, `readiness_met` (boolean), and the integers of at least 0 `findings_major`, `findings_minor`, `findings_fixed`, `findings_deferred`, `effort_turns`, `effort_minutes` (SWE-089); optional `assurance_reviewer_agent`, `checklist_revision`, `checklist_file` | validated when a record exists |
| `docs/reviews/*/decision-memo.md` (YAML front matter) | built-in `DECISION_MEMO_SCHEMA` (front matter of `docs/templates/decision-memo.md`): required `review`, `disposition` (null, `Approved`, `Approved with liens`), `signed` (ISO date or null); optional `package_revision`, `baseline_tag` (`baseline/<srr\|pdr\|cdr\|sar>` or null), `revoked` (ISO date or null) | validated when a memo exists |

Cross-file rules applied on top of the schemas (charter sections 2, 5 and 6; `docs/process/01-lifecycle-and-reviews.md` sections 10.3, 10.4, 10.6, 12 and 13):

| Rule | Failure message names |
|---|---|
| Every folder under `docs/reviews/` is a review token (SRR, PDR, CDR, TRR, TRR-Dn, SAR); a folder holding a log, record or memo is reported on that file, any other folder on itself; folders starting with `.` are ignored | the file or the folder |
| A log's `review` equals its folder | the log |
| Every item's `review` equals the log's `review` and its id starts with `<type>-<review>-` (01 section 10.4 check 2; this is the exact-`n` check of a `TRR-Dn` log: a `TRR-D1` log holding `RID-TRR-D2-001` fails). The one-line `python -c` check of 01 section 10.4 remains a fallback for a single log | the item index and id |
| Every item history follows 01 section 10.3: the first entry is from null to Open dated `opened`; each `from` equals the previous `to`; dates never decrease; each transition is Open to Answered, Answered to Verified, Answered to Open, Verified to Open, Verified to Closed, Open or Answered to Withdrawn, or same-state in a non-terminal state; nothing follows Closed or Withdrawn; the last `to` equals `state` (`review_trend.py` computes every SE-64 measure from the history); `closed` equals the date of the entry that enters the terminal state and is null otherwise | the item index and id |
| Every `verification.record` of a log names an existing file (the schema pattern admits only `docs/reviews/<REVIEW>/checklists/<product-slug>.md`), and that record's `product` is the item's `product` | the item index |
| `INSP-NNN` ids are unique across all reviews; a record's `checklist_file`, when present, is the record's own path | the second holder |
| A record's `reviewer_agent` differs from its `author_agent` (charter sections 2 and 11 rule 4; NPR 7123.1D App. G Table G-19 entrance 2) | the record |
| A record needs `assurance_reviewer_agent` other than `none`, the author and the reviewer (SWE-088 d, required participants) when its product is a whole-product item of 07 section 2.1.1 (`docs/requirements/sw/requirements.json`, `docs/process/07-software-engineering-plan.md`, `docs/process/03-software-classification-and-rmm.md`, `docs/vv/plan.md`, `docs/design/architecture.md`) or belongs to a safety-critical (`SW-KEYER`, `SW-TXSEQ`, `SW-PWR`, `SW-SAFE`, `SW-AUDIO`, `SW-BOOT`, `SW-SCHED`) or mission-critical (`SW-SYNTH`, `SW-CFG`, `SW-DISPLAY`) module of 07 section 14.1. The module is read from a `sw-<sub>` token in the product path or the record slug, and from a path segment named `<sub>` under `firmware/` or `docs/design/sw/` | the record |
| `verdict: APPROVED` needs `readiness_met: true` (SWE-088 b) and no body line naming a `finding-<n>` anchor together with the words `Major` and `Open` (SWE-088 b, c; 01 section 13) | the record |
| Record drift (SRR package section 2.3 and item R13, added 2026-09-26): when `--root` is the top of a git work tree with a HEAD commit, every blob a record names in `product_files` (entries `path@blob`, 7 to 40 hex digits, schema-checked) or `product_blob` (the blob of its single-file `product`) is compared with `git ls-tree -r HEAD` (the value of `git rev-parse HEAD:<path>`). An `APPROVED` record fails when a named blob differs from HEAD, a named path is not in HEAD, or it names no blob; a record with any other verdict passes and its drift is printed as `note: record drift: ...` under its `PASS` line. Outside a work tree top (the fixtures and their temporary copies) every record gets the note "record drift rule not applied" | the record |
| A memo's `review` equals its folder; `disposition` and `signed` are both set or both null (01 section 12.1); `revoked` needs `signed` and is not earlier than it (01 section 12.2); `baseline_tag` needs `signed`, is set only for SRR, PDR, CDR and SAR, and equals `baseline/<review>` | the memo |
| No `docs/reviews/*/peer-reviews/` folder exists (charter section 5 as amended 2026-09-25) | the folder |

Options: `--root PATH` (default: the repository root), `--quiet` (failures and their errors only; no notes). Output is one `PASS`/`FAIL` line per document with the error path in dotted notation (`requirements[3].id: ...`) and, without `--quiet`, the `note:` lines of the record drift rule. Exit 0 when every discovered document validates, 1 on any failure, 2 on a usage error.

## traceability.py

Of the six Class A rows of NPR 7150.2D section 3.12.1 Table 1 (SWE-052) that charter section 7 adopts, the tool enforces rows 1 (higher-level to software requirements), 5 (requirements to verifications) and 6 (requirements to nonconformances), row 2 (requirements to hazards) in part, and not yet rows 3 (requirements to design components) and 4 (design components to code). `SWE052_COVERAGE` in the source, printed as report section 1.4, lists per row the forward and backward link, the codes enforced today and the codes planned with their gates from `docs/process/03-software-classification-and-rmm.md` section 8. The tool also applies the requirement-side rules of `docs/process/02-requirements-and-traceability.md` section 8.2 and the evidence-side rules of `docs/process/04-verification-and-validation.md` section 7.3 that the catalogue below lists, then writes the report and a data file.

```sh
.venv/bin/python tools/traceability.py [--root PATH] [--output PATH] [--json PATH] [--report-only] [--quiet] [--render]
.venv/bin/python tools/traceability.py --regression DESIGN_REF [DESIGN_REF ...]
```

| Option | Behavior |
|---|---|
| (none) | Reads every input below, runs every check of the catalogue, writes `docs/vv/traceability-report.md` and `docs/vv/traceability.json`; exit 0 with no violation, 1 with violations, 2 on a usage error |
| `--output PATH` | Report path (relative to root unless absolute); the JSON is written beside it as `traceability.json` unless `--json` names another path |
| `--report-only` | Writes the outputs and exits 0 even with violations (while drafting) |
| `--quiet` | Prints violations only |
| `--render` | First writes `expectations.md` beside `expectations.json` (from the JSON and the `OPS-NNN` headings of `docs/conops/conops.md`) and `requirements.md` beside each `requirements.json` (from that file alone), then runs as above (02 section 8.1). Rendered files are deterministic, carry the line "Generated from ... by `tools/traceability.py --render` (02 section 8.1)" and are never edited by hand |
| `--regression DESIGN_REF ...` | Prints the hardware regression set of 04 section 10.5 (every `Passed` Bench case whose requirements' `design_refs` intersect the arguments, plus every live `TC-ATP` case) and exits without writing a report |

Inputs (relative to root; a missing optional input is a `WARNING`, never a crash): `docs/requirements/**/requirements.json`, `docs/requirements/l0-stakeholder/stakeholder-inputs.md` (`SI-NNN` rows; a row containing `**` is a core input), `docs/requirements/l0-stakeholder/expectations.json` (`NGO-`, `MOE-`, `CON-` entries with kinds, links, text and `source_ids`), `docs/conops/conops.md` (`OPS-NNN` headings and titles; table rows and scenario sections for the TBD rule), `docs/plan/semp.md` (table rows, for the TBD rule), `docs/test_cases/**/test_cases.json`, `docs/safety/hazards.json` (`requirement_ids` and the controls' `control_req_ids`), `docs/risk/register.json` (`RSK-NNN`, validated against `docs/risk/schema.json`), `docs/plan/tpm.json` (`mops[]` and `tpms[]`), `docs/references/md/regulatory/47cfr-<part>.<section>[-<slug>].md` for Parts 1, 2, 15 and 97 (resolution of `47CFR<part>.<section>(<para>)` clauses; an extract such as `47cfr-2.106-harmonic-bands.md` resolves its section), `docs/decisions/adr/ADR-NNN-*.md`, `docs/decisions/trade-studies/TS-NNN-*.md`, `docs/icd/ICD-*.md` (table rows, for the TBD rule), `docs/design/allocation.json` (preliminary at SRR; the record forms of rule T-18 below), `docs/vv/ncr/NCR-NNN.md` and `docs/vv/reports/TC-*-r<N>.md` (YAML front matter; every `artifacts` entry `"<path> sha256=<64 hex>"` is hashed), `docs/reviews/SAR/decision-memo.md` (existence, for `Closed`), and the rendered `.md` files (for `RENDER_STALE`). Files under `docs/templates/` are never read.

Hazard trace (04 section 3; charter section 7): a requirement traces to a hazard through its own `hazard_ids` or when `hazards.json` names it in a hazard's `requirement_ids` or a control's `control_req_ids`. `HAZARD_REQ_NOT_TESTED` and `HAZARD_REQ_NOT_ON_TARGET` run on that union, and report section 9 lists the union as the controlling requirements. The message cites SWE-192 for modules `SW` and `SW-<SUB>` only; for every other module it cites 04 rule 7.3.6, the project extension of SWE-192 to every hazard-control requirement.

Retirement markers (02 section 11.3, until a schema CR adds `Retired`): a requirement is retired when its status is `Closed` and its tags include `retired`; a test case is retired when its status is `Blocked` and its `setup` begins `Retired by `. Retired entries count for no coverage, appear in no matrix row, and are checked by `RETIRED_INCONSISTENT`; a status `Retired` is honoured as soon as a schema admits it.

Severities: `VIOLATION` sets the exit status; `WARNING` never does. One code has one severity. The plain-run severity of every rule follows the `check` column of 02 section 8.2. The `gate` column (for example T-08 set disagreement, T-17 group B words and T-20 core SI and Objective coverage as Errors at SRR) is not applied by the tool until `--gate` exists (below); until then the reviewer applies it by hand to the report's Warnings at the readiness declaration (02 section 8.1; 01 section 3.1), and the package records that manual gate run in its traceability section.

### Outputs

`docs/vv/traceability-report.md` is the working copy, refreshed by any plain run and never edited by hand. At package build 01 section 3.1 item 2 writes the frozen per-review record with `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --output docs/reviews/<REVIEW>/traceability-report.md` (the relative path is taken from the root), which also writes `docs/reviews/<REVIEW>/traceability.json` beside it.

| Section | Content |
|---|---|
| 1 Summary | Counts by status and evidence class, upstream artifacts consulted (1.1), open TBR list (1.2), key driving requirements (1.3), SWE-052 Table 1 coverage (1.4: one row per Class A row with the codes enforced, the codes planned with their gates, and the state Enforced, Partial or Not enforced) |
| 2 Findings | Violations, then warnings: `code`, `location`, `message` |
| 3 Requirements verification matrix | SE HB Appendix D, one table per requirements file, columns of 04 section 7.1: source, shall statement, success criteria (closing cases' acceptance criteria), method, evidence class, closing and supporting cases, facility, phase (credit event of 04 section 5.2), acceptance (Yes when a `TC-ATP` case cites the requirement: initial acceptance of each unit, App. D "Acceptance Requirement?"), recurring acceptance (Yes only when such a case carries `Recurring: yes` in its setup: App. D "Preflight Acceptance?"; default No), performer, results (latest credited report and NCRs), status. Retired requirements and retired cases are omitted |
| 4 Validation matrix | SE HB Appendix E, one row per `OPS-NNN` heading and per `MOE-NNN`, filled from the live `TC-VAL` cases whose `setup` names the target after `Validates:`; phase from `Phase:` in the setup; row status `Validated` when every case is `Passed` |
| 5, 6 | Orphan requirements (no live case), orphan test cases |
| 7 Parent coverage | Requirements without a parent, allocation to children, requirements tree |
| 8 Per-module coverage | Coverage, closing coverage, closure, children and open TBR per module |
| 9 Hazard traceability | Per hazard: the controlling requirements (hazard trace union), the cases citing them, and the live software requirements without a Passed, credited Bench or OnAir closing case (the SAR list for SWE-192, 01 section 8.6) |
| 10 Nonconformance traceability | NCR list and requirement to NCR list (SWE-052 Table 1 row 6) |
| 11 Checks performed | The check catalogue: every code, its severity and its rule |

`traceability.json` holds the same result as data: counts, coverage per module, validation row statuses, the SWE-052 coverage rows, the findings, and the measurements MSR-01 (requirements by level and status), MSR-03 (traceability gaps), MSR-04 (open TBR count) and MSR-23 (test counts by status and class) of 07 section 11.2. The planned consumer is `tools/measurements.py` (07 section 11.1), which does not exist yet: owner Claude as software lead, TV due PDR (`tools/toolchain.lock.md` section 1.2). Until it exists nothing appends these values to `docs/plan/measurements.json`.

### Rule coverage

This table and `CHECK_CATALOGUE` (report section 11) describe what the tool enforces today and are current as of 2026-09-25. 02 section 8.5, 04 section 7.4 and 03 section 8 bind the codes to their rules; where they differ from this table they are pending update by their owners, and this table is the statement of the tool.

| Rule | Codes |
|---|---|
| T-01 | `SCHEMA_MISSING`, `SCHEMA_ID_PATTERN_MISSING` (warning), `SCHEMA_INVALID` (requirements, expectations including an unparsable file, test cases, hazards, risk register) |
| T-02 | `MODULE_MISMATCH` (module equals the directory; id is exactly `<REQ\|TC>-<module>-NNN`), `MODULE_DUPLICATE`, `MODULE_UNKNOWN` (charter section 6 module sets), `ID_FORMAT` |
| T-03 | `ID_DUPLICATE` (REQ, TC and NCR across and within files; NGO, MOE and CON within `expectations.json`; HZ within `hazards.json`; RSK within `register.json`; MOP and TPM within `tpm.json`; repeated `OPS-NNN` headings; two ADR or TS files with one number; the first definition is kept); a stakeholder `name` used twice is `STAKEHOLDERS_MISSING` (T-21) |
| T-05 | `L1_PARENT_NOT_NULL`, `PARENT_UNRESOLVED`, `PARENT_CYCLE`, `PARENT_MISSING`, `SELF_DERIVED_UNSUPPORTED` |
| T-06 | `CHILD_INVERSE` |
| T-07 | `SOURCE_UNRESOLVED` (requirement and `expectations.json` sources; `SI-`, `NGO-`, `MOE-`, `CON-`, `OPS-`, `ADR-`, `TS-`, `47CFR` Parts 1, 2, 15, 97), `SOURCE_L0_MISSING`, `SOURCE_FILE_MISSING`, `SOURCE_FORMAT_UNKNOWN`, `REGULATORY_TAG_NO_CLAUSE` |
| T-08 | `HAZARD_ID_FORMAT`, `HAZARD_UNRESOLVED`, `HAZARD_FILE_MISSING`, `SAFETY_TAG_NO_HAZARD`, `HAZARD_CONTROL_UNTRACED` (a SW requirement named in `hazards.json` without the hazard id), `HAZARD_INVERSE` (warning; includes the control union rule), `HAZARD_REQ_NOT_TESTED` (on the hazard trace union), `HAZARD_REQ_NOT_ON_TARGET` (a Closed SW hazard requirement without Bench or OnAir evidence), `RISK_FILE_MISSING` |
| T-09 | `REQ_UNVERIFIED`, `REQ_NO_CLOSING_CASE` (live cases only) |
| T-10 | `TC_REQ_UNRESOLVED`, `TC_TYPE_METHOD`, `RETIRED_INCONSISTENT` (citation of a retired requirement by a live case) |
| T-11 | `VERIFIED_WITHOUT_EVIDENCE` (every live closing case `Passed` with a `credit: true`, `result: Pass` report citing the requirement), `VERIFIED_WITH_OPEN_NCR`, `CLOSED_WITHOUT_SAR`, `CHILD_AHEAD_OF_PARENT`, `TC_STATUS_EVIDENCE`, `REPORTS_DIR_MISSING`, `FAILED_TC_WITHOUT_NCR`, `REPORT_*`, `NCR_*` |
| T-14 | `TBD_PRESENT` (requirement and test case text, `expectations.json` text, ICD table rows, ConOps table rows and `OPS-NNN` scenario sections, SEMP table rows; in Markdown a mention of the policy terms such as `TBD and TBR`, `TBD/TBR`, `` `TBD` `` or `no TBD` is not a placeholder), `TBR_UNDOCUMENTED`, `TBR_UNMARKED`, `TBR_ON_FINAL_STATUS`, `TBR_CLOSE_BY` |
| T-16 | `MOP_UNRESOLVED` (warning) |
| T-17 | `SHALL_COUNT`, `MODAL_IN_DESCRIPTION`, `SHALL_IN_TITLE`, `DESCRIPTION_LENGTH`, `UNVERIFIABLE_WORD` |
| T-19 | `RETIRED_INCONSISTENT` (prefix, live child, live citing case, tag `retired` on a status other than `Closed`, retired case citing a live requirement without `superseded by TC-...`); a retired requirement's `tbr` object is `TBR_ON_FINAL_STATUS` |
| T-18 | `SYS_UNALLOCATED` (warning, the SRR severity of 02 section 8.2; one finding per `Draft` or `Active` SYS requirement that names no receiving L2 module, and one on `docs/design/allocation.json` when it does not parse). A requirement is allocated when `child_ids`, or a child's `parent_id`, names a live requirement of module RX, TX, PWR, CTL, ME, SW or SW-<SUB>, or when `docs/design/allocation.json` lists it under such a module in one of three record forms: an object with `requirement_ids` under its own or the nearest enclosing `module` (for example `elements[]`), an entry of a `modules` list whose `id` is the module token, or an object with `requirement_id` and a `modules` list (for example `allocations[]`); a `requirement_ids` list with no module above it (`functions[]`, `gaps[]`) allocates nothing. Report section 7.2 lists the receiving L2 modules of every requirement |
| T-20 | `CORE_SI_UNCOVERED`, `OBJECTIVE_UNCOVERED`, `MOE_WITHOUT_OPS`, `OPS_UNCITED` (warnings, evaluated once a requirement exists) |
| T-21 | `EXPECTATIONS_INCONSISTENT`; `STAKEHOLDERS_MISSING` (warning, the plain-run severity before SRR: `stakeholders` array absent, empty or not an array, no entry of role `customer`, `user` or `regulator`, a `name` used twice, a `source_ids` entry that does not resolve or matches no scheme; a source that cannot be checked because `stakeholder-inputs.md` is absent joins that file's `SOURCE_FILE_MISSING`). `--render` writes the array as section 7 of `expectations.md` |
| T-22 | `INTERFACE_TAG_NO_ICD` (warning) |
| 04 section 7.3 rules 5, 7, 8 | `VAL_TARGET_MISSING`, `VAL_TARGET_UNRESOLVED` (a mistyped target next to an existing one), `TC_SETUP_INCOMPLETE`, `REPORT_*`, `NCR_*` |
| SWE-052 row 6, SWE-202 | `NCR_NO_REQUIREMENT` (a product NCR of severity S1 to S3 without `requirement_ids`; the message names the requirements of its test cases), `NCR_FIELD_INVALID` (severity outside S1 to S4, status outside the 04 section 10.7 lifecycle, classification other than product or procedure) |
| 02 section 8.1 rendered files | `RENDER_STALE` (warning: rendered file absent, not written by `--render`, or different from the rendering of its JSON) |

### Not implemented, with gates

Each row below is a tool task of Claude as software lead; the gate's readiness declaration is blocked until its unit test passes on the fixtures (02 section 8.5; 04 section 7.4). Until the code exists, the check named in the last column is made by hand and recorded in the package.

| Planned code or option | Rule and source | Gate | Manual check until then |
|---|---|---|---|
| `HAZARD_UNCONTROLLED` | SWE-052 row 2 (03 section 8) | before PDR | hazard analysis reviewer, PDR hazard-to-requirement table |
| `HAZARD_INVERSE` promoted to a violation | T-08 (03 section 8; 04 section 7.3 rule 6 asks for every gate) | PDR | reviewer treats every `HAZARD_INVERSE` warning as blocking (04 section 7.4) |
| `DESIGN_REF_UNRESOLVED`, `DESIGN_REF_MISSING`, `DESIGN_ELEMENT_ORPHAN`, `REUSED_TAG_NO_REF` | SWE-052 row 3, T-15 (03 section 8; 02 section 8.5) | before PDR | design reviewer (`peer-review-checklist-design.md`) |
| `TAG_UNRESOLVED`, `REQ_UNTAGGED`, `DESIGN_ELEMENT_UNIMPLEMENTED` | SWE-052 row 4, T-15 (03 section 8) | before CDR | code reviewer (`peer-review-checklist-code.md`) |
| `NCR_BLOCKS_VERIFIED` | SWE-052 row 6 (03 section 8) | before TRR | none needed: `VERIFIED_WITH_OPEN_NCR` already blocks Verified for an open NCR of any severity |
| `HAZARD_REQ_NOT_ON_TARGET` for status `Verified` | SWE-192 at SAR (01 section 8.6); needs `--gate SAR`, because charter section 9 admits a host-verified software requirement as Verified before SAR | with `--gate` (PDR), applied at SAR | SAR package builder (Claude) confirms that report section 9 lists no requirement in "not yet tested on target" |
| `--gate <SRR\|PDR\|CDR\|TRR\|SAR>` | 02 section 8.2 `gate` column | PDR (02 section 8.1) | reviewer applies the `gate` column to the Warnings at every readiness declaration from SRR, recorded in the package traceability section |
| `--volatility --from <tag>` | SWE-200, MSR-02, TPM-012 (02 section 10.4) | PDR, first interval after `baseline/srr` | none before the first change after `baseline/srr` |
| `--fix-children` | T-06 convenience | PDR | authors maintain `child_ids`; `CHILD_INVERSE` catches mismatches |
| `BASELINE_ID_MISSING`, `TRANSITION_FORBIDDEN`, `CHANGE_UNCOVERED` | T-04, T-12, T-13 (git history, `docs/cm/cr/`) | PDR | CM reviewer against the baseline record |
| `SYS_UNALLOCATED` as an Error, and the `leaf` tag rule | T-18 `gate` column (the SRR Warning listing is implemented) | PDR, with `--gate` | requirements reviewer, check CK-REQ-B3 |
| `KDR_WITHOUT_MOP`, `MOE_WITHOUT_MOP` | T-16, T-20 | PDR | reviewer of `docs/plan/tpm.json` |
| `ICD_NAME`, `ICD_UNPAIRED`, `ICD_SECTION4_MISMATCH` | T-22 | PDR | interface reviewer |
| `SYS_NO_VALIDATION_PATH`, `SECURITY_TAG_NO_SOURCE`, T-09 and T-10 module rule | T-07, T-09, T-10 (02 section 8.5) | before SRR | requirements reviewer, checklist sections B and E |
| `CLOSING_CLASS`, `CLOSED_NOT_INSTALLED` (a `Closed` `REQ-SW-*` whose credited release no PCA-05 line names; the single name for this check in 02 T-11, 04 section 7.4 and 05), `VERIFIED_RELEASE_STALE`, `REPORT_RELEASE_UNRESOLVED`, `WAIVER_UNRECORDED` | 04 rules 7.3.3 and 7.3.4, T-11 (charter section 9) | CDR | procedure reviewer (04 section 8.3) |
| `VAL_PHASE_MISSING` | 04 rule 7.3.5 | before SRR | procedure reviewer |
| `CASE_STALE`, `DEVBOARD_CASE_CLOSING` | 04 rules 7.3.11 and 7.3.12 | PDR; before the first dev-board case becomes Active | procedure reviewer |
| Report section for retired entries | T-19 (02 section 11.3) | PDR | reviewer reads the retired count in report section 1 |

## render_review_figures.py

Renders the review-package and deck figures of one review into `docs/reviews/<REVIEW>/figures/` (charter section 4 items 1 and 2). The SRR set is `entrance-checklist.png`, `success-criteria.png`, `requirements-by-group.png`, `kdr-map.png`, `hazard-matrix.png`, `tpm-status.png` and `conops-modes-scenarios.png`. The tool also implements `risk-matrix.png` and `concept-block-diagram.png` (known-answer tested), but leaves them out of the SRR set because those two files have their own generators in `docs/reviews/SRR/figures/` since 2026-09-25, which a default run must not overwrite; one generator per figure is Claude's choice (open item). It is the controlled successor of the SRR deck figure generator that was kept outside the repository (deck-review finding F2; package section 2 item H10).

```sh
.venv/bin/python tools/render_review_figures.py --review SRR [--root PATH] [--out DIR] [--check] [FIGURE ...]
```

Statuses come from `docs/reviews/<REVIEW>/package.md` (entrance section 4, requirements section 8 with its functional-group table, success section 20); counts come from `docs/requirements/sys/requirements.json`, `docs/safety/hazards.json`, `docs/risk/register.json`, `docs/plan/tpm.json` and the section 6 headings of `docs/conops/conops.md`. Short labels, layouts and the concept block diagram are literals of the review's figure set (`FIGURE_SETS`; only `SRR` exists, and `--review PDR` exits 2 until a PDR set with its test is added). Every literal that restates repository content is cross-checked first: the labels against the package rows, each package group row against the requirement file, the KDR list against the `KDR` priorities, the TPM rows and their text against `tpm.json` and the review's `cbe`, the scenario lists against the ConOps. Any disagreement exits 1 before anything is written. Since 2026-09-26 (package section 15 item 56) a label may not restate a status word or a number that its package criterion cell lacks, the dagger rows must equal the package rows that say they rest on an uncredited tool run, the KDR map tags each open TBR with its `close_by` review, and the entrance and success lanes are fitted (one shared row height; fonts from 19 pt down to 12 pt) so that no row is dropped or clipped and no footnote overlaps a row; a lane that does not fit at 12 pt exits 1. Figure-set overrides (re-ratings a deck review asks the package to carry) are printed on every run and reported as redundant once the package carries them. `--check` runs the cross-checks and writes nothing. Exit 0 written or checked, 1 disagreement or missing input, 2 usage error. Source Sans Pro comes from `tools/slides/node_modules/` (npm install in `tools/slides/`), else the matplotlib default font with a notice.

## unsafe_audit.py

Unsafe-code audit of 07 CS-05 to CS-07 (gate G5; MSR-11; TV-011). Finds every `unsafe` keyword outside comments and literals (block, fn, impl, trait, extern block, unsafe attribute; an `unsafe fn(..)` pointer type is not a site; `target/` is skipped), requires a `// SAFETY:` comment in the comment block directly above each site in the audited roots (default rustos `api` and `firmware/pico2`), fails any site in the forbidden roots (default `firmware/`), and generates or checks the audit list `firmware/unsafe-audit.md` whose Reviewer (`INSP-NNN`) and Date cells are the only hand-edited cells; a rewrite keeps a signature while the site is unchanged and appends the signature of a changed or removed site to a "Superseded signatures" section.

```sh
.venv/bin/python tools/unsafe_audit.py --check [--gate SRR|PDR|CDR|TRR|SAR] [--json]   # gate G5 form
.venv/bin/python tools/unsafe_audit.py --write                                        # regenerate the list, keeping signatures
```

Unsigned entries are a note before CDR and a failure with `--gate CDR`, `TRR` or `SAR` (07 section 8.2). Exit 0 no failure, 1 failure, 2 usage error. State on 2026-09-26: the rustos sources at `c54d35a` hold 37 sites, 36 without a SAFETY comment, and the list is not yet generated, so G5 "unsafe audit" fails; both are work items outside this tool (rustos sources; the first `--write` with the software lead's commit of `firmware/unsafe-audit.md`).

## complexity_gate.py

Cyclomatic-complexity gate of 07 CS-17 (SWE-220), CS-38 and CS-19 (gate G5; MSR-17; TV-012). Reads the JSON of `rust-code-analysis-cli --metrics --output-format json` on standard input (or `--input`), derives each function's own CC (its `cyclomatic.sum` less its direct child spaces), fails a function above `--max` unless a waiver `W<n>` named in the decision memo covers it (`--waivers`, 07 section 14.3), fails a function above CC 1 in a file tagged `// @target-only` (plus one per `::take()`, the CS-11 board take), reports functions above 12 and every name-based call cycle (CS-19, never failing), and prints MSR-17.

```sh
rust-code-analysis-cli --metrics --output-format json --paths firmware ../rustos/api ../rustos/firmware/pico2 \
  | .venv/bin/python tools/complexity_gate.py --max 15 [--yellow 12] [--waivers FILE] [--json]
```

Exit 0 no failure, 1 a CS-17 or CS-38 failure, 2 usage error or input not understood (not JSON, no function space, own CC below 1): an empty pipe is never a pass. `rust-code-analysis-cli` is not installed (owner-approved download, decision 109); the known-answer test uses hand-written analyzer output, and the end-to-end check of TV-012 limitation 1 runs when the analyzer is installed.

## measurements.py

Software measurements of 07 sections 8.4 and 11 (TV-013). One mode per run: `--link-map MAP [--link-ld LD]` (gate G2: flash and RAM use against the TPM-010 and TPM-011 red lines, MSR-18 and MSR-19 with their assessment), `--diff-runs RUN1 RUN2` (gate G3: identical, all-passed JUnit result sets, SWE-186), `--coverage LCOV [--branch-condition JSON] [--emu JSON]` (gate G6 summary; an optional input not produced is reported NOT PRODUCED), `--check-records [--file PATH] [--against REV]` (the 07 section 11.1 rules JSON Schema cannot express on `docs/plan/measurements.json`: catalog ids, append order, `updated`, `supersedes`, append-only against REV, evidence hashes at the first commit containing each record, and the re-derivation of MSR-18 and MSR-19 from a cited link map) and `--analyze` (current record per id and scope, 07 section 11.3, without plots).

```sh
.venv/bin/python tools/measurements.py --link-map firmware/target/thumbv8m.main-none-eabihf/release/cwht-app.map
.venv/bin/python tools/measurements.py --check-records
```

Exit 0 pass, 1 a gate criterion or record rule failed, 2 usage error or unreadable required input. The tool never writes `docs/plan/measurements.json` or `docs/plan/tpm.json`; the append and the TPM mirror of 07 section 11.1 are due with FW-B1. State on 2026-09-26: `--check-records` exits 1 on the repository with 80 evidence entries that do not hold at `1d423e5`, the first commit containing the records (56 name evidence committed later with the recorded hash, 24 evidence that changed); the records owner supersedes them under the 07 section 11.1 rule.

## review_trend.py

Computes the review-trend TPM (`TPM-003`, key `review-trend`; NPR 7123.1D SE-64) exactly as `docs/process/01-lifecycle-and-reviews.md` section 11 defines it, from the RFA/RID logs and the `signed` dates of the decision memos. It is the only writer of the `TPM-003` history in `docs/plan/tpm.json` (01 section 11); no other script or hand edit appends to it.

```sh
.venv/bin/python tools/review_trend.py [--root PATH] [--date YYYY-MM-DD] [--json]
.venv/bin/python tools/review_trend.py --package <REVIEW> --write [--root PATH] [--date YYYY-MM-DD]
```

| Option | Behavior |
|---|---|
| `--date` | Package date `T` (default: today). Every item state is evaluated at `T` from its `history` |
| `--json` | Prints the computed result as JSON instead of the text table |
| `--package REVIEW --write` | Also writes `docs/reviews/<REVIEW>/figures/review-trend.png` (one burndown panel per logged review: cumulative raised and cumulative closed plus withdrawn as step lines, signed gate memos marked, `T` marked) and appends one history entry per logged review to `TPM-003` in `docs/plan/tpm.json` (fields of `conventions.history_entry_shape`: `review` = the package, `date` = `T`, `cbe` = closure fraction at `T`, `status`, `evidence` = the figure, `credit: false`, plus `log_review`, `raised`, `open`, `verified_pending`, `closed`, `withdrawn`, `overdue`, `closure_fraction_at_gate`, `zone`). A rerun for the same package and date replaces that run's entries; only the history array of `TPM-003` is rewritten in the file. With no log it writes a placeholder figure and one zero-count Green entry |

Inputs: `docs/reviews/*/rfa-rid-log.json` (validated against `docs/templates/rfa-rid-log.schema.json` first), `docs/reviews/*/decision-memo.md` front matter `signed`, `docs/plan/tpm.json` (with `--write`). Run `validate_docs.py` first: `review_trend.py` checks only the log schema, while `validate_docs.py` also fails a log whose history disagrees with its `state`, a log or memo outside a review-token folder, and an inconsistent memo.

Decisions the tool applies where 01 section 11 leaves a reading open: the next gate of review `R` is the first review after `R` in the order SRR, PDR, CDR, TRR, TRR-D1, TRR-D2, ..., SAR whose memo is signed on or before `T`; `closure_fraction_at_gate` is undefined until then and when every raised item was withdrawn; a review is "prior" (dispositioned) once its memo is signed on or before `T`, and its Major RIDs and Blocking RFAs count as open in any state other than Closed or Withdrawn; the zones are evaluated Red first, then Green, then Yellow (an undefined closure fraction does not block Yellow), and anything else is Red; the overall zone is the worst review zone; the burndown series lists the dates on which an item was raised, closed or withdrawn (the dates where the step lines move, which reproduces the 01 section 11 known answer).

Known limitations, open for the `review_trend.py` maintainer: the memo key `revoked` (01 section 12.2) is not read, so a revoked review stays dispositioned and remains a gate date; a log or memo in a folder that is not a review token is read and ranked after SAR. `validate_docs.py` fails the second case; the first needs a rule in 01 section 11 and a change to the tool.

Exit 0 when every zone is Green or Yellow (and when no log exists yet), 1 when any zone is Red (a Red zone blocks the readiness declaration), 2 on a usage error or invalid input (schema failure, bad date, missing `TPM-003` with `--write`).

## Tests and fixtures

`tools/tests/` holds the `unittest` known-answer tests (05 section 9.2; SWE-136):

- `test_validate_docs.py`: conventions, peer-review records, log cross-checks, usage errors (`UsageErrorTests`: an unknown option and a `--root` that is not a directory exit 2), and a repository class.
- `test_traceability.py`: the original rule set, the exact seeded code sets, and a repository class.
- `test_tools.py`: the pre-SRR additions (retirement markers, evidence rules, TBD scope, `--render`, front matter, matrix columns, JSON output, both tools together), one targeted test for every catalogue code that no fixture seeds with a guard test that fails when a new code has no test, and the 2026-09-25 revision classes: hazard trace union, on-target evidence, duplicate ids, module sets, schema findings, baselined Markdown TBDs, NCR fields, SWE-052 coverage, log items and history, peer-review record rules, decision memos and review folders, the new conventions, and the schema tripwires.
- `test_review_trend.py`: the 01 section 11 known answers on `docs/templates/rfa-rid-log.example.json`, CLI, `--write`, zones.
- `test_traceability_srr_rules.py`: the known answers of `STAKEHOLDERS_MISSING` (T-21) and `SYS_UNALLOCATED` (T-18): every sub-rule, each `allocation.json` record form, the unparsable file, retired children and requirements, report section 7.2, the stakeholders section of `expectations.md`, the tripwire on the fixture copy of `docs/requirements/l0-stakeholder/schema.json`, and a repository-content class that checks the tool's reading of `docs/design/allocation.json` against that file's own `allocations[]` records.
- `test_git_known_answer.py`: the git row of `tools/toolchain.lock.md` section 1.1 (blob hash of `fixtures/git/hello.txt`, `ls-tree`, tree and commit hashes of a one-file commit with a fixed identity and dates, `fsck --full` clean and after one corrupted byte, `git --version` equal to the lock), with git isolated from the user's configuration.
- `test_render_review_figures.py`: `render_review_figures.py` on `fixtures/review_figures/` with a fixture figure set: parsers, every drawn value, every cross-check, exit statuses, nothing written on a failed check, and the pixel size of all nine renders; `LabelAndDaggerTests` and `LayoutKnownAnswerTests` (2026-09-26, package section 15 item 56): labels that restate a status or count, the dagger rows, and lanes of 19 rows with hand-computed row heights and font sizes; a repository-content class runs the SRR `--check` on the repository.
- `test_validate_docs.py` `RecordDriftTests` (2026-09-26): the record drift rule on temporary git repositories (SRR package item R13).
- `test_unsafe_audit.py`: `unsafe_audit.py` on `fixtures/unsafe_audit/` (nine hand-counted sites with decoys, a seeded CS-06 and a seeded CS-05 fault, list generation, signatures, gates).
- `test_complexity_gate.py`: `complexity_gate.py` on `fixtures/complexity_gate/` (hand-written analyzer output with hand-computed CC values, the CS-17, CS-38 and CS-19 known answers, waivers, input errors).
- `test_measurements.py`: `measurements.py` on `fixtures/measurements/` (the FW-B0 link map against the SRR seed values, a map above the red line, JUnit, lcov, the record rules on temporary git repositories, `--analyze`).

`test_render_rmm.py`, `test_render_compliance.py`, `test_render_risk.py` and `test_render_deck.py` belong to their own tools (`test_render_deck.py` also holds `LocationGuard`, which checks that `tools/slides/render_deck.py` exits 2 and writes nothing for a deck outside `docs/reviews/<REVIEW>/slides/`, and `SeededFailures`, which checks exit 1 on an unreadable deck and on a failing headless shell). The `RepositoryTests` classes check repository content, not the tools; 05 section 9.2 records them separately from the accreditation run.

The fixtures are miniature repositories:

- `tools/tests/fixtures/valid_project`: every rule satisfied; `validate_docs.py` and `traceability.py` exit 0 with zero findings. It holds an Active L1 requirement with an open TBR, a self-derived L2 requirement backed by `ADR-001`, a non-software hazard control closed by `Analysis accepted per RSK-001`, an `expectations.json` in the real L0 structure with its rendered `expectations.md`, rendered `requirements.md` files, a `TC-VAL` case, a `tpm.json` valid against a copy of `docs/plan/tpm.schema.json`, regulatory corpus sections of Parts 1, 2 (extract file) and 97, a credited Bench report with a hashed artifact and the CM keys of `docs/templates/verification-report.md` (`source_commit`, `firmware_elf_sha256`, `procedure_blob`, `harness_versions`; 05 section 7.3 item 1), an NCR of severity S3, and an SRR RFA/RID log whose RID is verified by the complete record `docs/reviews/SRR/checklists/requirements-sys.md`.
- `tools/tests/fixtures/invalid_project`: seeded defects; both tools exit 1. `test_traceability.py` and `test_validate_docs.py` assert that exactly the seeded codes and the seeded failing documents are reported. Seeds added on 2026-09-25 that keep those sets: a duplicate `HZ-001` and a duplicate `RSK-001` (`ID_DUPLICATE`), and `REQ-SYS-005` named by `HZ-001` without `hazard_ids` (`HAZARD_REQ_NOT_TESTED` on the union).
- `tools/tests/fixtures/valid_project` also carries, for T-18 and T-21, a `stakeholders` array with the roles customer, user and regulator (its `docs/requirements/l0-stakeholder/schema.json` is a copy of the repository schema), a rendered section 7 in `expectations.md`, and `docs/design/allocation.json` with a fixture schema `allocation.schema.json` that allocates `REQ-SYS-004` to CTL (`modules[]`), `REQ-SYS-005` to PWR (`allocations[]`) and `REQ-SYS-006` to TX and ME (`modules[]`, `elements[]`). The fixture schema is replaced by a copy of `docs/design/allocation.schema.json` once that file exists.
- `tools/tests/fixtures/review_figures`: a miniature package with sections 4, 8 and 20, five SYS requirements, two hazards, four risks, three TPMs and a two-scenario ConOps; the known answers are in the test module.
- `tools/tests/fixtures/git`: `hello.txt` and `known-answers.json` (blob, tree and commit hashes, commit identity and date).
- `tools/tests/fixtures/unsafe_audit`, `tools/tests/fixtures/complexity_gate`: miniature Rust sources (and, for the gate, hand-written analyzer output, a waiver file and a memo); the `target/` case is built by the test in a temporary copy because the repository ignores `target/`.
- `tools/tests/fixtures/measurements`: `valid.json` and `invalid.json` (the schema known answer of `test_tools.py`); `linkmap/` (a byte copy of the committed FW-B0 map of `docs/vv/reports/TC-SW-TOOL-001-r1/` and the rustos `link.ld` at `c54d35a`, plus a small seeded map), `junit/`, `lcov/` and `records/`.
- `tools/tests/fixtures/review_trend`: a verbatim copy of `docs/templates/rfa-rid-log.example.json` as the SRR log, the SRR memo signed 2026-10-05, the record the log names, and a minimal `tpm.json` whose exact formatting the `--write` tests of `test_review_trend.py` check (it is not valid against `docs/plan/tpm.schema.json`, and `validate_docs.py` is not run on this fixture); `--write` tests run on a temporary copy.

Copies that must track the repository: the `review_trend` fixture log equals `docs/templates/rfa-rid-log.example.json`, and the fixture copies of `docs/templates/rfa-rid-log.schema.json`, `docs/plan/tpm.schema.json` (`SchemaTripwireTests`) and `docs/requirements/l0-stakeholder/schema.json` (`test_traceability_srr_rules.FixtureSchemaTripwireTests`, `valid_project` only) carry the repository constraints, compared with every `description` removed. Any change to one of those four repository files is committed together with the re-copied fixture files and a green suite (`.venv/bin/python -m unittest discover -s tools/tests`).

To add a check:

1. Add the code to `CHECK_CATALOGUE` with one severity and its rule text; for a SWE-052 row, update `SWE052_COVERAGE`.
2. Implement it in a `check_*` function.
3. Seed one defect in `invalid_project` without changing its seeded code sets, or add a targeted test in `test_tools.py` (keep `valid_project` clean). When a fixture change alters a seeded set, extend `EXPECTED_INVALID_VIOLATIONS` in `test_traceability.py` or `EXPECTED_INVALID_FAILURES` in `test_validate_docs.py` in the same commit.
4. Run the suite until it is green, then write or update `docs/cm/tool-validation/TV-NNN-<tool>.md` with the suite result and the commit tested, and update the tool's rows in `tools/toolchain.lock.md` sections 1.1 and 1.2 (05 section 9.2 steps 1 to 4).
5. Update this README's tables, and ask the owners of 02 section 8.5, 03 section 8 and 04 section 7.4 to update their tables in the same change set.

After any change to a fixture JSON with a rendered `.md`, re-render the fixture: `.venv/bin/python tools/traceability.py --root tools/tests/fixtures/valid_project --output <scratch path>/r.md --render`.
