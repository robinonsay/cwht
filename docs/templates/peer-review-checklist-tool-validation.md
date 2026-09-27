---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/05-configuration-and-data-management.md section 9.2 step 3). To review one
# tool validation record, or a set reviewed together, copy this whole file to
# docs/reviews/<REVIEW>/checklists/tool-validation-tv-nnn-<tool>.md (a set:
# tool-validation-tv-nnn-to-tv-mmm.md): that copy is the single peer-review record (there is no
# peer-reviews/ folder). Fill every field below, answer every applicable checklist item for each
# record, fill the per-record and per-purpose tables and the findings table. Both front-matter
# parsers (PyYAML and the subset parser of tools/validate_docs.py) strip a comment on its own line
# and a comment written after a value (" # ..."); this template keeps each comment on its own line
# for readability, and comment lines may stay or be deleted when filing. tools/validate_docs.py
# checks the record against the field list of 01 section 13 (its PEER_REVIEW_RECORD_SCHEMA) and fails
# while the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6); Claude assigns it in the assignment block
id: INSP-NNN
checklist: peer-review-checklist-tool-validation
checklist_revision: A
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/tool-validation-tv-nnn-<tool>.md
# product: the TV record (for a set, the first record; every record of the set is in product_files)
product: docs/cm/tool-validation/TV-NNN-<tool>.md
# product_commit: the commit that holds the TV record and everything it tested (item TV-A4), quoted
# so that an all-digit hash stays a string
product_commit: "<commit>"
# product_files: path@git blob at product_commit of every TV record reviewed, every repository tool
# file validated, its known-answer test module, each committed evidence log, and the lock; a fixture
# directory is listed by its tree hash (git rev-parse <commit>:<dir>)
product_files: ["docs/cm/tool-validation/TV-NNN-<tool>.md@<blob>", "tools/<tool>.py@<blob>", "tools/tests/test_<tool>.py@<blob>", "tools/tests/fixtures/<tool>@<tree>", "tools/toolchain.lock.md@<blob>"]
# tv_ids: every TV-NNN reviewed in this record
tv_ids: [TV-NNN]
# tool_class: A (product-generating) | B (evidence-generating), per record (05 section 9.1)
tool_class: B
# tool_kind: repository-tool | external-tool | emulator | instrument | revalidation (section G)
tool_kind: repository-tool
# acc_proposed: the ACC-<TOOL>-NNN scope statements the records propose (charter section 6)
acc_proposed: [ACC-<TOOL>-NNN]
# product_size: N records, N purposes, N known-answer tests, N fixture files
product_size: N records
# sprint: the gate preparation, for example PDR-prep
sprint: PDR-prep
# author_agent: the TV record author; tool_author_agent: the author of a repository tool's source
author_agent: <invocation id>
tool_author_agent: <invocation id or n/a for an external tool>
# reviewer_agent: never the TV record author and never the tool author (charter sections 2 and 11
# rule 4; 05 section 9.2 step 3)
reviewer_agent: <invocation id>
# criticality: neither. No tool is a safety-critical or mission-critical component
# (03 sections 4.3.1 and 6.1.1)
criticality: neither
# assurance_required: false. 07 section 2.1.1 has no row for TV records; the SWEHB swe-136 and swe-070
# section 7.1 tasks are items TV-H1 and TV-H2 of this checklist, done by this reviewer as the
# software assurance function (charter section 2). A trade study or ADR that selects a tool for a
# 07 section 14.1 component is routed to the assurance reviewer under its own record
assurance_required: false
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: none
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: not-required
# verdict: set by Claude as lead SE; APPROVED only when reviewer_verdict is APPROVED
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
# assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1] when section H is answered
assurance_tasks_applied: []
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by Claude as lead SE)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: tool validation records (TV-NNN)

**Product types and the sections that apply.** A reviewer answers the applicable items for each TV record in scope and lists the others under `ITEMS N/A`.

| `tool_kind` | Examples on cwht | Applicable sections |
|---|---|---|
| `repository-tool`: a Python or shell tool under `tools/` with its known-answer module under `tools/tests/` | `tools/traceability.py`, `tools/validate_docs.py`, `tools/render_tpm.py`, `tools/csa.py`, the LTspice wrapper, `tools/normalize_fab.py`, `tools/scad2step.py` | A to F, G1, H |
| `external-tool`: an installed program or toolchain run by its locked command | LTspice through the CrossOver wrapper, `kicad-cli`, OpenSCAD 2021.01 with FreeCAD 1.1.3, `rustc` and `cargo`, `cargo-llvm-cov`, `cargo-nextest`, `picotool`, `git`, `shasum` | A to F, G2, H |
| `emulator`: the RP2350 emulator selected by the PDR emulator ADR | The candidate of 07 section 9.4 with its per-peripheral credit scope `ACC-EMU-NNN` | A to F, G2, G3, H |
| `instrument`: instrument firmware and host software whose output is Bench evidence (04 section 6) | tinySA Ultra firmware, sigrok-pico capture firmware with `sigrok-cli` (TV due TRR, 05 section 13) | A to F, G4, H |
| `revalidation`: a new result row appended to an existing TV record after a 05 section 9.2 step 4 trigger (no version change) | A fixture change, an OS major version change, a class A re-run at a new baseline | A1, A3, A4, C5, D1, D2, E2, F3, and the section G subsection of the tool; the unchanged remainder is cited from the earlier record |

**Governing:** NPR 7150.2D SWE-136 (4.4.8: "validate and accredit the software tool(s) required to develop or maintain software") and SWE-070 (4.5.6: "use validated and accredited software models, simulations, and analysis tools required to perform qualification"), with SWEHB `swe-136-software-tool-accreditation.md` and `swe-070-models-simulations-tools.md` section 7.1; `docs/process/05-configuration-and-data-management.md` section 9.1 (classes A, B and C), section 9.2 (procedure steps 1 to 5 and the known-answer table), section 9.3 (toolchain lock), section 13 (the single schedule of TV records by gate) and Table 4-1 rows 27, 28 and 30; `tools/toolchain.lock.md`; `docs/cm/tool-validation/README.md` (index and common owner actions); `docs/process/03-software-classification-and-rmm.md` sections 4.3.1 and 6.1.1 (tools under the single matrix; a tool's source is peer-reviewed as code); `docs/process/04-verification-and-validation.md` section 4 (tool accreditation paragraph: a tool absent from the lock, or without an accredited TV record, produces developer evidence only); charter sections 8 and 11 rule 8 (headless only). **Basis of the item set:** SRR decision 117 (adopted with the consent agenda: accept INSP-015's item set for SRR; this template before the PDR TV set), whose items TV-S1 to TV-S10 (`docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`) are carried here with their numbers in the "Carries" column, and INSP-015 findings F-01 (a purpose claim wider than its known answer) and F-02 (no result tied to a commit that contains what was tested). **Used by:** an independent reviewer agent that authored neither the TV record nor the tool (charter sections 2 and 11 rule 4). The tool's source, for a repository tool, is reviewed as code with `docs/templates/peer-review-checklist-code.md` (03 section 6.1.1, row "Peer review"), either in this record as an appended section or in its own record; this checklist covers the validation, not the code.

Answer every item Yes, No or N/A with evidence (TV record section and line, command and exit status pasted, blob or tree hash, fixture file and value, lock row). Every No is a finding. **Major**: a result is not tied to a commit that contains the tool, test module and fixture tested; an accredited or proposed purpose has no known answer, or the known answer does not exercise it; a class B purpose has no seeded fault; a class A tool has no reproducibility result; an expected answer was produced by the tool under validation; the reviewer's re-run disagrees with the recorded result; the version recorded is not the version run; a limitation hides a use the project relies on. **Minor**: a stale status line, a count or date error that changes no result, a missing installer checksum with a stated substitute, a README or lock entry out of step with the record.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/tool-validation-tv-nnn-<tool>.md` (or `tool-validation-tv-nnn-to-tv-mmm.md` for a set), is the single peer-review record for the TV records in `tv_ids` (charter section 5). The slug follows the `<type>-<product-stem>` rule of 01 section 13 with type `tool-validation`. The reviewer also writes the date, its invocation and the result into section 8 ("Independent review") of each TV record in scope, which is the only change it makes to a TV record (05 section 9.2 step 3); the accreditation in section 9 is the owner's.

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major or Minor | TV-xx | TV record, section and line; tool or fixture file | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | Pending, `Adopt as RID RID-<REVIEW>-NNN`, `Adopt as RFA RFA-<REVIEW>-NNN` or `No action` | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

Finding rules: ids are `finding-<n>`, numbered from 1 in this record, each with the anchor `<a id="finding-<n>"></a>` in its first cell so that `checklists/<slug>.md#finding-<n>` resolves (01 section 13). The reviewer writes `Pending` in the owner ruling column; Claude transcribes the owner's ruling (01 section 10.1). `tools/validate_docs.py` rejects `verdict: APPROVED` while any line holding a `finding-<n>` id also holds the words `Major` and `Open`, so write the state only in the State column and keep severity and state words out of the tables below. Replace the placeholder row above; do not leave it in a filed record.

### Per-record results (one row per TV record in `tv_ids`)

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-NNN | name, version string | A or B | short hash | command; exit; same or different | ids or none | `finding-<n>` or none |

### Per-purpose results (one row per purpose of every record; items TV-B1 to TV-C3)

| TV record | Purpose (as numbered in the record) | Known answer that exercises it (test name or fixture case) | Seeded fault (class B) | Cited uses of the purpose in the project | Finding ids |
|---|---|---|---|---|---|
| TV-NNN | 1 | `test_...` or fixture case | fault and expected failure | products or procedures that cite this output | `finding-<n>` or none |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | Every TV record in scope, the tool files, the known-answer test module, the fixture and the evidence logs are committed; `product_files` lists their blobs and trees at `product_commit` (PDR work plan rule C2; INSP-015 F-02) | `git rev-parse` output; `git status --short` on the paths prints nothing |
| R2 | The known-answer command named in each record's section 3 runs from the repository root and exits 0 on the committed state | command and exit status |
| R3 | `cd /Users/robinonsay/rust/cwht && .venv/bin/python -m unittest discover -s tools/tests` passes, and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 | tool output lines |
| R4 | Each tool has its `tools/toolchain.lock.md` rows (section 1 version row, section 1.1 sanity-check row, section 5 status) and each record is in the `docs/cm/tool-validation/README.md` index | lock; README |
| R5 | The author's return lists, per record, the purposes, the uses the project cites, the known-answer tests, the runs with their commits, and the proposed `ACC-<TOOL>-NNN` scope | author return |

## A. Identification (05 section 9.2 step 1)

| Id | Check | Carries | Evidence to inspect |
|---|---|---|---|
| TV-A1 | The exact version string and the command that produced it are recorded, and the reviewer's run of that command on the build machine prints the same string | TV-S1 | record section 1; reviewer run |
| TV-A2 | The install source is recorded with installer URL and SHA-256 (lock section 7); where upstream publishes neither, the record says so and names its substitute | TV-S1 | record section 1; lock section 7 |
| TV-A3 | Every file validated is identified by git blob and SHA-256, and each fixture directory by a tree hash or digest; the reviewer recomputes them at `product_commit` and they match | TV-S1 | record section 1; reviewer recomputation |
| TV-A4 | Every result row names a commit that contains the tool, the test module and the fixture exactly as identified in TV-A3 (no untracked or modified file; INSP-015 F-02) | TV-S1 | `git ls-tree <commit>` output |
| TV-A5 | The class (A, B or C) follows 05 section 9.1: output entering a release or design CI is class A; output cited as verification, inspection, audit or review evidence is class B; class C is never cited as evidence | TV-S2 | record header; 05 section 9.1 |
| TV-A6 | The run is headless and scripted (charter section 11 rule 8); no step needs a GUI, a screen capture or a macOS privacy permission | none | record section 3 |

## B. Purposes (05 section 9.2 step 1: "each purpose is one line and is what accreditation covers")

| Id | Check | Carries | Evidence to inspect |
|---|---|---|---|
| TV-B1 | Each purpose is one line and states an observable behaviour (inputs, output, exit status) that a known answer can check | TV-S2 | record section 2 |
| TV-B2 | The purposes cover every use the project cites: the reviewer searches the repository for the tool's cited outputs (process documents, test cases, reports, review records, the lock) and lists any use no purpose covers; an uncovered cited use is Major | none | vector search for the tool name, then grep to pin; per-purpose table |
| TV-B3 | No purpose claims more than its known answer checks (INSP-015 F-01): a list of supported cases, keywords, formats or exit codes in a purpose equals the list the tests exercise | TV-S4 | record section 2 versus section 3; test module |

## C. Known-answer test (05 section 9.2 steps 1 and 2 and its table; 05 section 9.1 validation required per class)

| Id | Check | Carries | Evidence to inspect |
|---|---|---|---|
| TV-C1 | The fixture is under the single fixture root `tools/tests/fixtures/<tool>/` with its inputs and expected outputs committed, and the run command and numeric pass criteria are stated | TV-S3 | record section 3; fixture listing |
| TV-C2 | Every purpose is exercised by at least one known answer, and for class B each purpose has a seeded fault whose expected failure (exit status, message, code) is stated; a negative control shows the test can fail | TV-S3, TV-S4 | per-purpose table; test module |
| TV-C3 | The expected answers are independent of the tool under validation: computed by hand, analytically, by a different tool, or taken from a source outside the tool; the record states how each was obtained | TV-S8 | fixture expected files; record section 3 |
| TV-C4 | The known answer implements every clause of the tool's row in the 05 section 9.2 table (for example, for LTspice: the stored -3 dB frequency within 1 %, the `.log` version line, the seeded-error netlist exit status and the time-out guard; for `kicad-cli`: exactly the seeded ERC and DRC violations and none on the clean files, and each export comparison), or the record states which clause is not met and the item is a finding | TV-S3 | 05 section 9.2 table row; record section 3 |
| TV-C5 | The reviewer re-runs the known-answer command at `product_commit` (on an export of that commit, or the working tree when it equals it) and obtains the recorded test count, outputs and exit status | TV-S5 | reviewer run output pasted |

## D. Results and reproducibility (05 section 9.2 steps 1 and 2)

| Id | Check | Carries | Evidence to inspect |
|---|---|---|---|
| TV-D1 | Each result row has the date and time, the commit tested, the test count, an output excerpt and a committed evidence file whose content supports the row | TV-S5 | record section 4; `docs/cm/tool-validation/evidence/` |
| TV-D2 | `tools/toolchain.lock.md` section 1.1 records each run with its date, the commit tested and the test count, and section 5 agrees with the record's status | TV-S10 | lock sections 1.1 and 5 |
| TV-D3 | Class A only: the record shows two runs with identical output hashes, normalized per 05 section 8.2 where the tool writes time stamps; N/A for class B, where the record may still show repeat runs | TV-S6 | record section 5 |

## E. Limitations and re-validation triggers (05 section 9.2 steps 1 and 4)

| Id | Check | Carries | Evidence to inspect |
|---|---|---|---|
| TV-E1 | The limitations are true to the tool: the reviewer confirms at least one limitation per record by reading the code or by a run, and no limitation is contradicted by the tool's behaviour (INSP-015 F-04); every limitation that bounds a cited use is reflected in the proposed scope statement | TV-S7 | record section 6; tool source or reviewer run |
| TV-E2 | The re-validation triggers include every trigger of 05 section 9.2 step 4 that applies: a version change of the tool, of the OS major version or of a fixture; a defect found in the tool (also an NCR, SWE-201); expiry at each new baseline for class A tools; plus the triggers specific to the tool (for example an interpreter or dependency change) | TV-S7 | record section 7 |

## F. Accreditation readiness, schedule and indexes (05 sections 9.2 steps 3 and 5, and 13)

| Id | Check | Carries | Evidence to inspect |
|---|---|---|---|
| TV-F1 | The proposed scope statement `ACC-<TOOL>-NNN` names the purposes it covers, the tool version or blob, and the conditions of use (interpreter, wrapper, precondition), and covers nothing the known answers do not | none | record section 9 |
| TV-F2 | The record is due at the gate 05 section 13 names for it, or earlier when a product cites the tool's output before that gate (05 section 9.1: a TV record before the first cited use), and its header states which | TV-S9 | record header "Due"; 05 section 13 |
| TV-F3 | The README index row, the lock section 5 row and the record header agree on status (Validated, Accredited, Not yet validated) and on the due gate | TV-S9, TV-S10 | README; lock section 5; record header |
| TV-F4 | Section 9 of the record leaves the accreditation decision to the owner and states that, until it is recorded, the tool's output is developer evidence (04 section 4; 05 section 9.1). A pending owner decision is not a finding; this record's APPROVED verdict is the reviewer precondition for it (05 section 9.2 step 3) | TV-S9 | record section 9 |
| TV-F5 | For a version change of an already accredited tool, a CR is named (Class I when the tool can change a released image) together with a new TV number (05 section 9.2 step 5; Table 4-1 row 27) | none | CR file; record header |

## G. Kind-specific items (answer the subsection of the record's `tool_kind`)

### G1. Repository tools

| Id | Check | Evidence to inspect |
|---|---|---|
| TV-G1-1 | The known-answer module separates fixture-only tests (the validation) from repository-content tests (a check of the repository, recorded separately, 05 section 9.2 table rows for `tools/traceability.py` and `tools/render_review_figures.py`) | test module classes |
| TV-G1-2 | Every exit status the tool documents (0, 1, 2 or others in its docstring) has a known answer, including the usage-error status (INSP-015 F-05) | test module; tool docstring |
| TV-G1-3 | The tool's code review exists or is appended to this record with `peer-review-checklist-code.md` (03 section 6.1.1 row "Peer review"), at the same blob as TV-A3 | code review record |

### G2. External tools and the emulator

| Id | Check | Evidence to inspect |
|---|---|---|
| TV-G2-1 | The locked command is the one the process documents and the analyses use (the lock row and its wrapper), and preconditions are checked as the lock states them (for example the LTspice `CaptureAnalytics=false` key read through `iconv`, never appended to; the OpenSCAD absolute `-o` path; the `freecadcmd` success marker instead of its exit status) | lock sections 1 and 1.4 |
| TV-G2-2 | Every run has a time-out guard that kills only its own processes where the tool can hang (lock section 1.4) | wrapper or record section 3 |
| TV-G2-3 | Downloads or installs needed by the validation were approved by the owner and are recorded with their source and checksum (lock section 7); none was performed without that approval | status notes; lock section 7 |

### G3. Emulator (07 section 9.4; ADR-011; 04 section 4 Emulation row)

| Id | Check | Evidence to inspect |
|---|---|---|
| TV-G3-1 | The credit scope is per peripheral: each peripheral in `ACC-EMU-NNN` has its own known answer against a stored reference trace, and every peripheral outside it is stated as outside | record sections 2, 3 and 9 |
| TV-G3-2 | The scope asserts event order only, in TIMER0 microseconds, and grants no credit for a duration, frequency or timeout (charter section 9; ADR-011) | scope statement |
| TV-G3-3 | The fallback of 07 section 9.4 item 3 is named for the case the emulator is not accredited | record; 07 section 9.4 |

### G4. Instrument firmware and host software (04 section 6; TV due TRR)

| Id | Check | Evidence to inspect |
|---|---|---|
| TV-G4-1 | The known answer uses a reference whose value is independent of the instrument (the stored period of a Pico-generated reference for the logic capture; the instrument's internal calibration output or the NanoVNA level through the attenuator whose S21 was measured that session for the tinySA Ultra, 04 section 4) and states the tolerance it checks | record section 3 |
| TV-G4-2 | The owner's bench steps are written so the owner can perform them without Claude present, with the setup, the cabling and the safety line (04 section 8.3 items 4 and 6) | record section 3 |

## H. Software assurance tasks (SWEHB section 7.1; charter section 2)

| Id | Check | Evidence to inspect |
|---|---|---|
| TV-H1 | swe-136 7.1 task 1: the software tools needed to create and maintain the software are validated and accredited; for a tool that builds or checks firmware (the Rust toolchain, the coverage, complexity, unsafe-audit and gate tools), the record's purposes cover the gate steps of 07 section 8.4 that cite it | record; 07 section 8.4 |
| TV-H2 | swe-070 7.1 task 1: the models, simulations and analysis tools used to qualify flight software or flight equipment are validated and accredited; for an analysis tool, the purposes cover the analyses that cite it (`peer-review-checklist-analysis.md` item CK-ANA-C2) | record; analysis notes |
| TV-H3 | The tasks applied are listed in `assurance_tasks_applied` and each task's result is stated in this record | front matter |

## Completion criteria (SWE-088 b, c)

`verdict: APPROVED` when: readiness R1 to R5 were true; for every record in `tv_ids`, every applicable item is answered and the others are listed as N/A; the per-record table has a row for every record with the reviewer's own re-run; the per-purpose table has a row for every purpose of every record; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate (a Minor finding raised after the first APPROVED verdict is a lien due at the next readiness declaration, PDR work plan rule C1); section 8 of each record names this review; the front matter is complete with the measurements (SWE-089) filled; and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. Findings stay Open until Claude marks them Verified after re-reading the corrected records at their new blobs. On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, and is listed in `deferred_rids`. Accreditation itself is the owner's decision, recorded in section 9 of each TV record and in `tools/toolchain.lock.md` (05 section 9.2 step 3), never this record's.

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
PRODUCT: TV-NNN[, TV-MMM ...] at <product_commit>
FINDINGS:
- [Major] TV-A4 TV-NNN section 4 run 2: the commit named does not contain tools/tests/fixtures/<tool>/expected.json.
- [Minor] TV-F3 README index row TV-NNN: status Validated, record header says Not yet validated.
ITEMS N/A: TV-D3 (class B), TV-G2 to G4 (repository tool)
RE-RUN: <command>; exit <n>; <count> tests; same as record run <n>
MEASUREMENTS: size=N records, N purposes; turns=N; minutes=N; major=N; minor=N
```
