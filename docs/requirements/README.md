# docs/requirements

Requirement data for the cwht transceiver, from stakeholder inputs down to subsystem and firmware-module specifications. The process that governs this directory is `docs/process/02-requirements-and-traceability.md` (charter section 7); this README is a map and a command sheet, not a rule source.

## Layout

Files marked `[created before SRR]` or `[created at PDR]` do not exist yet; the mark names the gate before which they are written.

```
docs/requirements/
├── README.md                          this file
├── schema.json                        JSON Schema for every requirements.json (L1, L2); statuses Draft, Active, Verified, Closed
├── l0-stakeholder/
│   ├── stakeholder-inputs.md          SI-NNN: owner statements, verbatim, append-only (SI-001 to SI-036)
│   ├── schema.json                    JSON Schema for expectations.json (stakeholders, NGO, MOE, CON entries); stakeholders
│   │                                  required once the file carries a baseline tag (process sections 3.0 and 11.2)
│   ├── expectations.json              NGO-NNN (one Need, Goals, Objectives), MOE-NNN, CON-NNN; baseline null until SRR;
│   │                                  stakeholders array added before SRR (process section 14, AL-02-21)
│   └── expectations.md                rendered from expectations.json by tools/traceability.py --render (never hand-edited)
├── sys/requirements.json              L1  module SYS      REQ-SYS-NNN        (exists, Draft; + rendered requirements.md)
├── rx/requirements.json               L2  module RX       REQ-RX-NNN                                  [created at PDR]
├── tx/requirements.json               L2  module TX       REQ-TX-NNN                                  [created before SRR: the regulatory REQ-TX-*, 01 section 4.3 row 25]
├── pwr/requirements.json              L2  module PWR      REQ-PWR-NNN                                 [created at PDR]
├── ctl/requirements.json              L2  module CTL      REQ-CTL-NNN                                 [created at PDR]
├── me/requirements.json               L2  module ME       REQ-ME-NNN                                  [created at PDR]
├── sw/requirements.json               L2  module SW       REQ-SW-NNN        (firmware-wide)           [created at PDR]
└── sw/sw-<sub>/requirements.json      L2  module SW-<SUB> REQ-SW-<SUB>-NNN  (e.g. sw/sw-keyer -> SW-KEYER)
                                       sw/sw-keyer [created before SRR] (SI-018); other <sub> created by the architecture ADR at PDR
```

The `module` field of each file is the upper-cased name of the file's immediate parent directory (`sys` is `SYS`, `sw` is `SW`, `sw/sw-keyer` is `SW-KEYER`); `tools/traceability.py` rejects any other pairing (rule T-02). Charter section 6 writes the software layout as `docs/requirements/sw/sw-<sub>/requirements.json`. The layouts `sw/keyer/` and `sw-keyer/` directly under `docs/requirements/` are not used.

Related directories and files (state read on 2026-09-25 at 18:15; the files change as the SRR products are written):

| Artifact | Path | Ids and fields | State on 2026-09-25 |
|---|---|---|---|
| Verification cases | `docs/test_cases/<module>/test_cases.json` (`<module>` is the module id lower-cased, e.g. `sys`, `tx`, `sw-keyer`, plus the test-only modules `val`, `atp`, `sw-cov`, `sw-reg`, `sw-tool` of charter section 6 and 04 section 1) | `TC-<MOD>-NNN`, `requirement_ids` | schema only; the `Draft` closing case of every L1 requirement is written before SRR (process section 4.1 step 7) |
| ConOps scenarios | `docs/conops/conops.md` | `OPS-001` to `OPS-021` headings | exists |
| Interface control documents | `docs/icd/ICD-<A>-<B>.md` (template `docs/templates/icd.md`) | `ICD-<A>-<B>` in `design_refs` | none yet; external stubs before SRR (reviewed, not baselined), all baselined at PDR |
| Hazards | `docs/safety/hazards.json` (schema `docs/safety/schema.json`) | `HZ-001` to `HZ-015` (version 0.2.0-pha, 2026-09-25); each control's `control_req_ids`, the hazard-level `requirement_ids` as their union | exists |
| Measures | `docs/plan/tpm.json` | `MOP-001` to `MOP-020` in `mops[]`; `TPM-001` to `TPM-017` in `tpms[]`, each with `mop_id` (null for the process leading indicators TPM-003, TPM-009, TPM-012) | exists |
| Decisions | `docs/decisions/adr/ADR-NNN-<slug>.md`, `docs/decisions/trade-studies/TS-NNN-<slug>.md` (templates `docs/templates/adr.md`, `trade-study.md`) | `ADR-NNN`, `TS-NNN` in `source_ids` | `ADR-001` to `ADR-025` exist; no trade study yet |
| Regulatory corpus | `docs/references/md/regulatory/47cfr-<part>.<section>.md` or `47cfr-<part>.<section>-<slug>.md` (Parts 1, 2, 15, 97; eCFR issue 2026-09-23; fetch procedure in that directory's README) | `47CFR<part>.<section>[(paragraph)]` in `source_ids` | exists |
| Change requests | `docs/cm/cr/CR-NNN-<slug>.md` (template `docs/templates/change-request.md`) | `CR-NNN` | none before SRR |
| Product waivers | A `CR-NNN` with disposition `Approved (waiver)` or an item `W<n>` of a review decision memo (05 section 2); register in CSA item 12 of `docs/process/configuration-status.md` (05 section 6) | requirement id, tag `waived` (process section 8.7) | none yet |
| Traceability outputs | `docs/vv/traceability-report.md`, `docs/vv/traceability.json`; inputs `docs/vv/ncr/`, `docs/vv/reports/` | matrices, findings, measurements; `NCR-NNN`, `<TC-ID>-rN` | outputs exist and are rewritten by every plain run |
| Measurements | `docs/plan/measurements.json` | requirements volatility `MSR-02` (mirrored to `TPM-012`) | created at PDR |

Templates: `docs/templates/requirements.example.json` (three schema-valid SYS requirements: a KDR carrier-power requirement linked to MOP-004 and TPM-015, a Baseline paddle-timing requirement linked to MOP-012 and TPM-013 and closed on the Bench at system level, and a hazard control for HZ-003 carrying a TBR; every cited `SI`, `NGO`, `MOE`, `OPS`, `ADR`, `MOP`, `TPM` and `HZ` id exists in the repository; `child_ids` are empty because the children do not exist yet; the `REQ-SW-*` and `TC-*` ids named in `verification_note` are illustrative), `docs/templates/adr.md`, `docs/templates/icd.md`, `docs/templates/peer-review-checklist-requirements.md` (reviewer checklist).

## Levels in one paragraph

Owner statements are logged as `SI-NNN` and never edited. The stakeholders they name are identified in the `stakeholders` array of `expectations.json`, and the statements are distilled into the Need, Goals and Objectives (`NGO-NNN`), Measures of Effectiveness (`MOE-NNN`) and Constraints (`CON-NNN`) of the same file, and into ConOps scenarios `OPS-NNN`. L1 system requirements (`REQ-SYS-NNN`) have `parent_id: null`, cite a primary L0 id first in `source_ids` (and regulation clauses where they apply), and cite at least one `OPS-` or `MOE-` id as their validation path; every core input (bold `SI`, such as SI-018: straight key and iambic paddles, one requirement per key type) is cited by at least one of them. L2 requirements (`RX`, `TX`, `PWR`, `CTL`, `ME`, `SW`, `SW-<SUB>`) carry a `parent_id` (an L1 id, or another L2 id for a derived requirement) or are self-derived with an `ADR`/`TS` source or a hazard. Every requirement names its verification method when written and is closed by a test case of the same method and of a closing type for its module: system and hardware requirements close on evidence from the delivered unit (Bench, OnAir, Inspection) or by Analysis, and only software requirements close on `HostUnit` or `Emulation` cases (process section 4.4). A software requirement closed by `HostUnit` or `Emulation` becomes `Verified` on a credited report run against the tagged release named in its version description, and `Closed` only after the SAR decision memo and the PCA-05 line of the unit's `as-built.md` confirming that release is installed on the delivered unit (charter section 9). Hazards link through `hazard_ids`, measures through `mop_ids`, interfaces (ICD ids), design elements and code through `design_refs`.

## Adding or changing a requirement

1. Pick the module file (process section 2.2). Allocate the id as `max(NNN)` in that file plus one, retired entries included; never reuse or renumber.
2. Write `description` as one `shall` statement of at most 25 words with number, unit and tolerance and none of the WR-07 words (process section 4.2); `rationale` with `Why:`, `Assumes:`, `Ops:` and the other items of section 4.3 in that order; `verification_method` and `verification_note`; `source_ids` (primary L0 id first for SYS), `parent_id`, `hazard_ids`, `design_refs` (ICD id for an `interface`-tagged requirement), `tags`, `priority`. Mark an estimated value `(TBR)` and fill the `tbr` object.
3. Have a test-author agent add, in the same commit, a `Draft` closing case in `docs/test_cases/<module>/test_cases.json` (process section 4.1 step 7).
4. Run the two checks below and clear every violation before committing (use `--report-only` only while drafting).
5. Request an independent review (writing rules WR-01 to WR-14, validation steps V1 to V6, checklist `docs/templates/peer-review-checklist-requirements.md`). The filled checklist `docs/reviews/<REVIEW>/checklists/requirements-<module>.md`, with `id: INSP-NNN` in its front matter, is the single peer-review record (charter section 5).
6. After SRR (L1) or PDR (L2), any non-editorial change needs an approved `CR-NNN` first (process section 10; CM plan `docs/process/05-configuration-and-data-management.md` section 5). A requirement found not met is waived by CR, not changed (process section 8.7).

Retirement (charter section 6; process section 11.3): never delete an entry. Until a schema CR adds a `Retired` status, a retired requirement keeps its id with `status: "Closed"`, `"retired"` in `tags`, no `tbr` object, and a rationale prefixed `Retired by CR-NNN (or, before the level's baseline, RID-<REVIEW>-NNN or INSP-NNN): ...`; a retired test case has `status: "Blocked"` and a `setup` that starts `Retired by ...`; an L0 entry uses `status: "Retired"` with `retired_by`. A `Closed` requirement without the tag `retired` is one accepted at SAR (with the tag `waived` when accepted under a waiver).

## Commands

Every command below uses absolute paths, so it runs from any working directory. Verified on 2026-09-25 against the shipped tools (`--help`, a plain run, the unit tests).

Validate every JSON document that exists against its schema by path convention (requirements files, `expectations.json`, test case files, the example templates, risk register, hazards, RMM, RFA/RID logs, peer-review records):

```sh
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py            # exit 0 when every discovered document validates
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --quiet    # failures only
```

Traceability checks and report (`tools/traceability.py`; rules T-01 to T-22 of process section 8.2, with the codes the tool implements today listed in process section 8.5):

```sh
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py                  # all checks; rewrites docs/vv/traceability-report.md and docs/vv/traceability.json; exit 1 on any violation
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --report-only    # same, exit 0 (drafting runs only)
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --quiet          # violations only
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --render         # first rewrites expectations.md and every requirements.md, then checks
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --output <scratch>/traceability-report.md --json <scratch>/traceability.json   # no repository change
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --regression <design_ref> ...   # hardware regression set (04 section 10.5); no report
```

A plain run rewrites the two `docs/vv/` outputs, and `--render` rewrites the rendered `.md` files beside the JSON. A reviewer who needs no repository change passes `--output` (the JSON then lands beside it) or both `--output` and `--json`, with paths under the reviewer's scratchpad directory.

Planned options (process section 8.1; Claude implements each by the gate named): `--gate <SRR|PDR|CDR|TRR|SAR>` (entrance-mode severities; PDR; until then the reviewer applies the `gate` column of process 8.2 to the report's Warnings), `--volatility --from <tag>` (SWE-200 metric `MSR-02` into `docs/plan/measurements.json`; PDR), `--fix-children` (regenerate `child_ids` from `parent_id`; PDR). They do not exist yet and any invocation of them exits 2.

The word lint of process rule WR-07 is part of `tools/traceability.py` (T-17); there is no separate lint. The tool's lists are a verbatim copy of WR-07: group A modal verbs are violations (`MODAL_IN_DESCRIPTION`), group B words are warnings in a plain run (`UNVERIFIABLE_WORD`), and `shall` in a title is a violation (`SHALL_IN_TITLE`). The reviewer still judges the cases the lint cannot (standalone `this`/`these`, other `-ly` adverbs and `-ize` verbs). The tool's own known-answer tests run with:

```sh
/Users/robinonsay/rust/cwht/.venv/bin/python -m unittest discover -s /Users/robinonsay/rust/cwht/tools/tests
```

Outputs land in `docs/vv/`: `traceability-report.md` (summary, findings, the SE HB App. D verification matrix and App. E validation matrix, orphan lists, parent and per-module coverage, hazard and nonconformance traceability, the check catalogue) and `traceability.json` (the same data, machine-readable, with the 07 section 11 measurements). A report with zero violations is an entrance product of every review; at package build the per-review report `docs/reviews/<REVIEW>/traceability-report.md` and its data file `traceability.json` are written by the command of `docs/process/01-lifecycle-and-reviews.md` section 3.1 item 2 (`--output docs/reviews/<REVIEW>/traceability-report.md`), not copied from `docs/vv/`.

## Identifier rules (charter section 6)

`REQ-<MOD>-NNN` and `TC-<MOD>-NNN` where `<MOD>` is `SYS`, `RX`, `TX`, `PWR`, `CTL`, `ME`, `SW` or `SW-<SUB>` (test-only `VAL`, `ATP`, `SW-COV`, `SW-REG`, `SW-TOOL` for cases; `VER` is reserved and unused); `NGO-NNN`, `MOE-NNN`, `CON-NNN`, `OPS-NNN`, `SI-NNN` at L0; stakeholder entries keyed by unique `name`; `ICD-<A>-<B>` for interfaces (process section 3.5 fixes the token order). Three digits, allocated sequentially per file, never reused. Charter section 6 omits the firmware-wide `SW` from its module list; process section 14 (CI-9) carries that edit.
