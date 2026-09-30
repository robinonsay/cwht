---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/08-agent-briefing.md sections 3.4 and 3.5). To review an analysis product,
# copy this whole file to docs/reviews/<REVIEW>/checklists/analysis-<product-stem>.md: that copy is
# the single peer-review record (there is no peer-reviews/ folder). Fill every field below, answer
# every applicable checklist item, fill the per-case table and the findings table. Both
# front-matter parsers (PyYAML and the subset parser of tools/validate_docs.py) strip a comment on
# its own line and a comment written after a value (" # ..."); this template keeps each comment on
# its own line for readability, and comment lines may stay or be deleted when filing.
# tools/validate_docs.py checks the record against the field list of
# docs/process/01-lifecycle-and-reviews.md section 13 (its PEER_REVIEW_RECORD_SCHEMA) and fails while
# the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6); Claude assigns it in the assignment block
id: INSP-NNN
checklist: peer-review-checklist-analysis
checklist_revision: A
# checklist_file: this record's own path; the stem is the analysis note's file stem, for example
# analysis-rx-cascade for docs/design/analysis/rx-cascade.md
checklist_file: docs/reviews/<REVIEW>/checklists/analysis-<product-stem>.md
# product: the analysis note, which states the question, inputs, results and margins (08 section
# 3.4); the deck, checker, plot and input data files are reviewed with it and listed in product_files
product: docs/design/analysis/<product-stem>.md
# product_commit: the freeze commit named in the reviewer brief (PDR work plan rule C2), quoted so
# that an all-digit hash stays a string
product_commit: "<commit>"
# product_files: path@git blob of every reviewed file at product_commit (git rev-parse
# <commit>:<path>): the note, every deck and netlist, every checker, every rendered plot and every
# input data file the analysis owns (record drift rule)
product_files: ["docs/design/analysis/<product-stem>.md@<blob>", "hardware/sim/<area>/<deck>.net@<blob>", "hardware/sim/<area>/check_<deck>.py@<blob>", "hardware/sim/<area>/<deck>.png@<blob>"]
# analysis_kind: one or more of simulation-deck, budget, thermal, rf-exposure, cascade, timing,
# worst-case, other (sections G1 to G7 below)
analysis_kind: [simulation-deck]
# product_size: N cases, N input values, N decks, N plots
product_size: N cases
# tools_used: every tool that produced a number in the product, with its TV record or "none"
# (section C), for example ["LTspice 26.0.2 (TV-NNN)", "venv Python 3.x (TV-001)"]
tools_used: []
# values_proposed: every TBR value or TPM current best estimate the analysis proposes, as
# "<REQ-, TPM- or HZ- id>: <value with unit>"; empty when it proposes none (PDR work plan rule C10)
values_proposed: []
# renders_inspected: number of PNG or SVG files the reviewer opened with the Read tool
renders_inspected: 0
# sprint: the gate preparation, for example PDR-prep
sprint: PDR-prep
author_agent: <invocation id>
# reviewer_agent: never the author of the note, the deck, the checker or the design data analysed
reviewer_agent: <invocation id>
# criticality: safety-critical | mission-critical | neither: the criticality of the 07 section 14.1
# component whose value the analysis sets (a firmware timing analysis of SW-KEYER is
# safety-critical); neither for a hardware-only analysis
criticality: neither
# assurance_required: true only when docs/process/07-software-engineering-plan.md section 2.1.1
# routes the product to the software assurance reviewer (an analysis inside a trade study or ADR that
# constrains a section 14.1 component; the software section of a plan). A stand-alone analysis note
# is not a row of that table: false, and section J below is answered by this reviewer. Exception:
# tools/validate_docs.py requires an assurance reviewer (assurance_reviewer_agent not none) when the
# product path or the record slug carries the sw-<sub> token of a 07 section 14.1 module (for example
# analysis-sw-keyer-timing); such a record is then held with the assurance reviewer, true here
assurance_required: false
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: none
# iteration: 1 to 3 (07 section 10.2; PDR work plan rule C1)
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: not-required
# verdict: set by Claude as lead SE; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
# assurance_tasks_applied: the SWEHB section 7.1 tasks applied in section J, for example
# [swe-070 7.1 task 1, swe-134 7.1 task 1]
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

# Peer review checklist: analyses (simulation decks and checkers, budgets, thermal, RF exposure, cascade and timing analyses)

**Product types and the sections that apply.** A reviewer answers the applicable items and lists the others under `ITEMS N/A`.

| Product type (`analysis_kind`) | Examples on cwht | Applicable sections |
|---|---|---|
| `simulation-deck`: an LTspice deck (netlist) with its automated checker and rendered plot | Harmonic low-pass filter response, PA bias and matching, key clamp, supply start-up | A to F, G1, H, I; J when `criticality` is not neither |
| `budget`: a line-item budget with totals and margins | Power, mass, link, noise, frequency (reference and synthesizer error), spurious budgets of `docs/design/budgets.md`; TPM current best estimates | A to F, G2, H, I |
| `thermal`: a dissipation and temperature analysis | PA and regulator junction temperatures, accessible-surface temperature, enclosure material limits | A to F, G3, H, I |
| `rf-exposure`: the RF Exposure Evaluation or a delta to it | `docs/design/analysis/rf-exposure-evaluation.md` (charter section 5; 05 Table 4-1 row 48) | A to F, G4, H, I |
| `cascade`: a receiver or transmitter stage-by-stage chain | Receiver noise figure, gain, intercept and selectivity; transmit line-up gain and drive | A to F, G5, H, I |
| `timing`: a timing budget of a firmware path, a hardware timer or a keying or sequencing edge | Key-to-RF latency, T/R sequencer timing, debounce, keyer element timing, hardware timer and watchdog budgets | A to F, G6, H, I; J when `criticality` is not neither |
| `worst-case`: a tolerance, derating or worst-case analysis | Component stress and derating, reference tolerance stacks | A to F, G7, H, I |
| Analysis section of a trade study or ADR | The analysis that scores an option | This checklist for the analysis; the study itself is reviewed with `peer-review-checklist-risk.md` section B (trade studies) or `peer-review-checklist-design.md` sections A, B and H (ADRs) under its own record |

**Governing:** SE HB §5.3 (sidebar "Methods of Verification": Analysis is "the use of mathematical modeling and analytical techniques", including modeling and simulation and verification by similarity); `docs/process/04-verification-and-validation.md` section 3 (method rule and the hazard-tracing rule), section 4 (evidence class Simulation and the tool accreditation paragraph) and section 5 (credit rules: Analysis closes only Analysis-method requirements, section 5.1 item 2; Analysis credit is taken on the CDR design data and confirmed at SAR, item 5; credit row `A`, section 5.2); `docs/plan/semp.md` section 7.2 (methods and tools); `docs/process/08-agent-briefing.md` section 3.4 (analyst deliverables: the model or deck, an automated checker that asserts the acceptance value, a rendered plot, and a note with assumptions, inputs with sources, results, margin against the requirement or TPM, and limitations); `docs/process/05-configuration-and-data-management.md` section 9 (tool classes and TV records); NPR 7150.2D SWE-070 (4.5.6) and SWE-136 (4.4.8) with SWEHB `swe-070-models-simulations-tools.md` section 3 (verification and validation of models and simulations, uncertainty and credibility reporting; NASA-STD-7009, which that page cites, is not in the corpus); the TPM conventions of `docs/plan/tpm.json` (`planned_value`, `margin_policy`, `threshold_yellow`, `threshold_red`, `history[].cbe` and `credit`); the `tbr` object of `docs/requirements/schema.json` (`owner`, `plan`, `close_by`); PDR work plan rules C2 (freeze), C7 (every case named) and C10 (analysis review before value ruling); charter section 11 rule 3 (visual closure). **Used by:** an independent reviewer agent that did not author the note, the deck, the checker or the design data analysed (charter sections 2 and 11 rule 4); a second, software assurance reviewer only where 07 section 2.1.1 says Yes, with `peer-review-checklist-software-assurance.md`.

Answer every item Yes, No or N/A with evidence (note section and line, deck line, checker output pasted, plot path, source document and page, or `docs/research/<file>.md F<n>` with its confidence tag). Every No is a finding. **Major**: an input value that sets a result is wrong or has no source; a model is used outside its validity range for a case that is reported; a tool without an accredited TV record produces a number used to close a requirement or to propose a TBR value without the result being marked developer evidence; a unit or arithmetic error changes a pass or fail, a margin sign or a proposed value; a case the governing requirement or regulation names is missing; the checker does not assert the acceptance value, or its result disagrees with the note; a margin is negative, or smaller than the stated uncertainty, and the note does not say so; a regulatory limit is misquoted; a plot has no render or its render was not inspected. **Minor**: a stale citation, a missing confidence tag, wording or presentation that changes no number, margin or conclusion.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/analysis-<product-stem>.md`, is the single peer-review record for the analysis (charter section 5). The slug follows the `<type>-<product-stem>` rule of `docs/process/01-lifecycle-and-reviews.md` section 13 with type `analysis`; `<REVIEW>` is the next gate the analysis feeds. The front matter above is the first thing in the file, unfenced. When one note carries several analyses of one subsystem (for example the receiver cascade and its selectivity), one record reviews the note; when two notes are frozen separately, each gets its own record.

### Findings (filled by the reviewer and, where required, the assurance reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer or assurance | Major or Minor | CK-ANA-xx | file and line, deck line, or checker output | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | Pending, `Adopt as RID RID-<REVIEW>-NNN`, `Adopt as RFA RFA-<REVIEW>-NNN` or `No action` | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

Finding rules: ids are `finding-<n>`, numbered from 1 in this record, each with the anchor `<a id="finding-<n>"></a>` in its first cell so that `checklists/analysis-<product-stem>.md#finding-<n>` resolves (01 section 13). The reviewer writes `Pending` in the owner ruling column; Claude transcribes the owner's ruling (*Adopt as RID*, *Adopt as RFA* or *No action*, 01 section 10.1) at the review. `tools/validate_docs.py` rejects `verdict: APPROVED` while any line holding a `finding-<n>` id also holds the words `Major` and `Open`, so write the state only in the State column and keep severity and state words out of the per-case table. Replace the placeholder row above; do not leave it in a filed record.

### Per-case results (one row per case the governing requirement, TPM or regulation names; section F)

| Case | Condition (mode, power step, frequency, temperature, supply, key type) | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check (re-run, hand calculation or not re-checked) | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | for example: 5 W step, 148.000 MHz, 13.8 V equivalent input, +45 C | `REQ-<MOD>-NNN`: limit with unit | value with unit | limit minus result, in the note's convention | value with unit | re-run: same value | `finding-<n>` or none |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | The product is committed and frozen: every `product_files` blob equals `git rev-parse <product_commit>:<path>` (PDR work plan rule C2) | `git rev-parse` output |
| R2 | The checker runs from the repository root by one command named in the note and exits with the result the note states; for a deck, the run uses the headless command of the `tools/toolchain.lock.md` LTspice row (its wrapper once committed), with the `CaptureAnalytics=false` precondition read through `iconv` and a time-out guard that kills only its own run | command and exit status |
| R3 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 when the product includes a JSON file under a schema (for example `docs/plan/tpm.json`) | tool output line, or N/A |
| R4 | The author's return states the question, the assumptions, the inputs with sources, the results with margins, the limitations, every proposed value (`values_proposed`) and every tool used with its TV record | author return |
| R5 | No `TBD` string in the product; every TBR the note introduces or relies on names its `REQ-<MOD>-NNN` id and `tbr` object | vector search, then grep to pin |
| R6 | Every render the note cites exists next to its source (charter section 11 rule 3; 08 section 1 "VISUAL CLOSURE") | file listing |

## A. Question, scope and traceable inputs

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-A1 | The note states the question it answers and names every requirement, TPM, TBR, hazard control and trade criterion it serves by id; every id exists in its file | note introduction; requirement files, `tpm.json`, `hazards.json` |
| CK-ANA-A2 | The design data analysed are identified by path and commit or blob (schematic sheet, design BOM line, CAD file, concept section, ICD section) and are the current ones; a product marked AT RISK names the CR it is drafted on and the CR state (PDR work plan section 3.1 "At risk" and rule C8) | note; `git log` of the design files; CR files |
| CK-ANA-A3 | Every input value has a source: a datasheet (part number, revision, page or figure), a requirement or ICD id, a measured value with its report and TV-backed instrument, a research finding cited as `docs/research/<file>.md F<n>` with its confidence tag, or an owner statement in a status note; a stated engineering assumption is labelled as one | input table |
| CK-ANA-A4 | The reviewer checks every input value that sets a reported result against its source (not a sample) and lists any disagreement; a value read from a curve states the reading and its resolution | sources; per-input check list in the record body |
| CK-ANA-A5 | Every assumption is stated, justified, and bounded: the note says in which direction each assumption moves the result (conservative or not) and what would invalidate it; an operating assumption (duty cycle, transmit time, ambient, supply range, posture, key type) agrees with the ConOps, the stakeholder inputs and the current owner decisions | assumptions list; `docs/conops/conops.md`; `stakeholder-inputs.md`; status notes |
| CK-ANA-A6 | The analysis stays inside its question: it does not change a requirement, an interface or a hazard control silently; each consequence for another product is stated as a request to that product's writer (PDR work plan section 5.3) or as a CR trigger (register of section 6.2, for example PCR-9) | note conclusions |

## B. Model validity (SWEHB `swe-070` section 3; SE HB §5.3)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-B1 | The model represents the physics that sets the result for the stated purpose; every simplification (ideal parts, lumped elements, linearization, steady state, one-dimensional heat flow, far-field formula) is stated with its effect on the result | model description; deck |
| CK-ANA-B2 | Every vendor or third-party model (SPICE model, S-parameter file, thermal model) is identified by source, file name, version or date and blob, and its stated validity range (frequency, bias, temperature) covers every case of the per-case table | model files; vendor documentation |
| CK-ANA-B3 | The model has validation evidence for its intended use: agreement with a datasheet curve or table at stated points, a hand calculation, a known answer, a measurement, or a heritage comparison; the agreement is quantified | validation section of the note |
| CK-ANA-B4 | Numerical settings that can change the answer are stated and adequate: simulator time step and stop time, tolerance options, frequency points per decade, mesh or node count, iteration or convergence limits; a result near a limit is shown not to move when the setting is tightened | deck directives; note |
| CK-ANA-B5 | The reviewer reproduces at least one reported result independently, by hand calculation or by a different method, and states the agreement; a disagreement larger than the stated uncertainty is a finding | record body (independent check) |
| CK-ANA-B6 | Uncertainty is reported: the sources of uncertainty in the result (input tolerances, model error, numerical error, instrument error for measured inputs) are listed and their combined effect on each margin is quantified or bounded (SWEHB `swe-070` section 3.6.1: uncertainty analysis, credibility assessment, error quantification) | uncertainty section of the note |

## C. Tools, validation status and reproducibility (NPR 7150.2D SWE-070, SWE-136; 05 section 9; 04 section 4)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-C1 | Every tool that produced a number is listed in `tools_used` with the version `tools/toolchain.lock.md` records, and the version in the run log equals it (for LTspice the `.log` first line) | lock rows; run log |
| CK-ANA-C2 | Each such tool has a TV record (`docs/cm/tool-validation/TV-NNN-<tool>.md`) whose purposes cover the use made here; where the record is not yet accredited (section 9) or does not exist, the note marks the result developer evidence (05 section 9.1) and the result neither closes a requirement nor goes to the owner as a TBR value until the record is accredited or the owner rules on the basis of developer evidence | TV records; lock accreditation column; note |
| CK-ANA-C3 | The run is headless and scripted (charter section 11 rule 8): one command reproduces every number; a deck for the record is a netlist, one analysis per deck, never an `.asc` run (lock section 1.4) | command in the note; deck |
| CK-ANA-C4 | The reviewer re-runs the checker at `product_commit` (an export of that commit, or the working tree when it equals it) and obtains the same exit status and the same values; outputs with time stamps are compared after normalization | reviewer run output pasted |
| CK-ANA-C5 | Every tool limitation stated in its TV record section 6 is respected by this use (for example a known time-out behaviour, an unvalidated purpose, a unit convention) | TV record limitations |

## D. Units, arithmetic and consistency of numbers

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-D1 | Every quantity carries a unit; every conversion is correct (W and dBm, dB and dBc, dBi and dBd, V rms and V peak, C and K, ppm and Hz, mils and mm, duty and average power) | note tables; checker source |
| CK-ANA-D2 | Every number in the note equals the checker output or a computation shown in the note; the same quantity has the same value in the note, the checker, the plot annotations, `docs/design/budgets.md` and `docs/plan/tpm.json` | cross-comparison list in the record body |
| CK-ANA-D3 | Rounding is conservative with respect to the limit (a result is rounded toward the limit, never away from it) and the stated precision does not exceed the input precision | results table |
| CK-ANA-D4 | The checker's acceptance constant equals the governing limit verbatim (value, unit, inclusive or exclusive comparison) and is traceable to the requirement, TPM or regulation id in a comment next to it | checker source |

## E. Results, margins, proposed values and credit

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-E1 | Each acceptance value is quoted from its governing source with the id: the requirement `description`, the TPM `planned_value` and `margin_policy`, or the regulation from `docs/references/md/regulatory/` (cited as `47 CFR <part.section>(<para>) (corpus: <file>, eCFR issue 2026-09-23)`) | sources |
| CK-ANA-E2 | Each margin is computed as the note's stated convention (limit minus result, or result minus limit), has the right sign, and is compared with the TPM thresholds (`threshold_yellow`, `threshold_red`) where a TPM applies | margins table; `tpm.json` |
| CK-ANA-E3 | Each margin exceeds the uncertainty of CK-ANA-B6, or the note states that it does not, names the consequence (a risk entry request, a design change, a CR trigger) and does not report the case as passing | margins table |
| CK-ANA-E4 | The automated checker asserts every acceptance value and exits non-zero on any failing case (08 section 3.4); it is not a plot or a print statement alone | checker source; R2 run |
| CK-ANA-E5 | Each proposed TBR value (PDR work plan rule C10) states the requirement id, the value with unit and tolerance, the margin that supports it, the requirement's `tbr.plan` step it executes, and, where the plan says "else a CR", whether that branch is triggered; the note does not edit the requirement file (section 5.3 writer order) | note proposals; requirement `tbr` objects |
| CK-ANA-E6 | Each proposed TPM current best estimate names the TPM key and id, the value, the `credit` flag (true only on an accredited tool and design data of record), and the evidence path, and the note does not edit `tpm.json` unless the assignment names it (08 section 3.4) | note; assignment |
| CK-ANA-E7 | Credit is claimed only as 04 section 5 allows: an analysis closes only requirements whose `verification_method` is Analysis (credit row `A`); for a Test-method requirement it is supporting evidence; a PDR analysis on preliminary design data is not closing credit, which is taken at CDR on the product baseline and confirmed at SAR (04 section 5.1 item 5); every linked `TC-*` case carries the right `Credit row:` line | note; test case files |

## F. Every case named (PDR work plan lesson L5 and rule C7)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-F1 | The reviewer lists, from the governing requirement, TPM or regulation text itself, every case it enumerates (every limit point, frequency or harmonic order, every operating mode and state, every power step, both band edges and the band centre where a frequency matters, both key types where keying matters, each environment extreme, each supply extreme) and the per-case table has one row for each; a missing case is Major | governing texts; per-case table |
| CK-ANA-F2 | Off-nominal and boundary cases the requirement implies are analysed: fault states that the analysis is used to bound (for example stuck key, full-duty key-down, cell at end of discharge, charger active during transmit) where the hazard analysis names them | `hazards.json` causes; note |
| CK-ANA-F3 | Worst-case combinations are analysed, not only each extreme alone: the note states which combination is worst for each result and why | note |
| CK-ANA-F4 | Sensitivity: for every case whose margin is within twice its uncertainty, the note shows the result's sensitivity to the two inputs with the largest effect | note |

## G. Kind-specific items (answer the subsections of the product's `analysis_kind`)

### G1. Simulation decks and checkers

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G1-1 | The deck and checker are under `hardware/sim/<area>/` (05 Table 4-1 row 24) or `docs/design/analysis/` for CDR analyses, with the plot rendered beside the deck; file names tie deck, checker and plot together | file listing |
| CK-ANA-G1-2 | Each deck runs one analysis (`.ac`, `.tran`, `.noise`, `.op` or `.dc`), and the netlist has no unconnected (`NC_`) nets | deck; netlist |
| CK-ANA-G1-3 | Sources, loads and terminations model the real interface (50 ohm port impedance where the ICD says so, the stated source impedance, the actual load); component values equal the design data of CK-ANA-A2, with parasitics stated where modelled | deck versus design data |
| CK-ANA-G1-4 | The checker reads the simulator output files (`.raw` or `.log` measurements), not values typed by hand, and fails when the output file is missing or stale | checker source |

### G2. Budgets (power, mass, link, noise, frequency, spurious)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G2-1 | Every line item has a source (datasheet, measurement, estimate labelled as such with its basis) and a state (estimate, calculated, measured) | budget table |
| CK-ANA-G2-2 | The totals recompute from the line items (the reviewer recomputes them and pastes the differences, or "none"); contingency or reserve follows the TPM `margin_policy` | recomputation |
| CK-ANA-G2-3 | The allocation to each subsystem agrees with `docs/design/allocation.json`, and the budget in `docs/design/budgets.md` agrees with `tpm.json` for every TPM it feeds | allocation file; budgets; `tpm.json` |
| CK-ANA-G2-4 | Every operating mode of the ConOps that changes a line item has a column (for example receive, transmit at each power step, standby, charging) | budget table; ConOps modes |

### G3. Thermal

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G3-1 | Dissipations come from the electrical analysis at the same operating point (power step, supply, efficiency), and the transmit duty or key-down time comes from the ConOps or the governing requirement, including the worst allowed key-down | electrical analysis; ConOps; requirements |
| CK-ANA-G3-2 | Every thermal resistance and material property is sourced (datasheet junction-to-case, board and via assumptions, interface material, enclosure material and coating) and the ambient range is the environment set of the governing requirements | inputs table |
| CK-ANA-G3-3 | Every limit in the path is checked: junction maxima with the derating the design applies, cell temperature limits, material softening or service limits of every enclosure part, and the accessible-surface limit of the governing requirement with the accessibility definition it states | per-case table |
| CK-ANA-G3-4 | Transient versus steady state is justified: a steady-state result is not used for a limit that a transient reaches first, and a transient uses the thermal capacities it states | note |

### G4. RF exposure (charter section 5 controlled regulatory document; 47 CFR 97.13, 1.1307, 1.1310, 2.1091, 2.1093)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G4-1 | Each limit and exemption threshold is quoted from the verbatim corpus in `docs/references/md/regulatory/` with its paragraph, and the two exposure tiers of SI-030 are each evaluated | corpus files; SI-030 |
| CK-ANA-G4-2 | The time-averaging basis and the CW duty factor are stated and sourced (the averaging period of 47 CFR 1.1310 for each tier; the keying duty the ConOps and requirements allow), and the worst transmit power step is used | note; corpus |
| CK-ANA-G4-3 | Every exposure geometry of the ConOps postures and the antenna options is evaluated (handheld at the face, body-worn, portable with an external antenna) with the distances stated and sourced; a near-field case uses a method valid in the near field, and a far-field formula used closer than its validity is a finding | note; ConOps postures |
| CK-ANA-G4-4 | The conclusion is linked both ways with HZ-001 and its controls (`hazards.json`), and any change to the evaluation is routed as a Class I change once 05 Table 4-1 row 48 is under CR control (CR from PDR) | `hazards.json`; note change history |

### G5. Cascades (receiver and transmitter chains)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G5-1 | The stage table lists every stage in signal order with gain, noise figure, intercept or compression point and bandwidth, each sourced at the operating frequency and bias, including passive losses (filters, switches, connectors, mismatch) | stage table |
| CK-ANA-G5-2 | The cascade formulas are applied correctly (Friis for noise; intercept referred to one reference plane; image and IF rejection in dB relative to the wanted response) and the reviewer recomputes the totals | recomputation |
| CK-ANA-G5-3 | Selectivity and spurious responses are evaluated at every frequency the requirement or the frequency plan names (image, half-IF, adjacent channel spacing, band edges) | frequency plan; per-case table |

### G6. Timing (firmware paths, hardware timers, keying and sequencing edges)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G6-1 | The time base is stated with its tolerance (crystal or oscillator ppm, PLL settings from the clock plan, timer resolution) and every duration is converted from it correctly | clock plan; note |
| CK-ANA-G6-2 | The worst-case path is analysed: interrupt latency and pre-emption, critical sections, scheduler tick and dispatch jitter, peripheral settling, and hardware edges (relay or switch settling, envelope rise and fall); the sum is compared with the governing limit | timing budget |
| CK-ANA-G6-3 | No duration, frequency or timeout is taken from an Emulation run (charter section 9; ADR-011; 04 section 4); host results with the mock clock are used only for platform-independent logic (04 section 5.2) | sources of each duration |
| CK-ANA-G6-4 | For a response to an off-nominal condition, the analysis shows the response completes within the time needed to prevent the hazardous event (SWE-134 item j) and names that hazard and control | hazard control; note |

### G7. Worst-case, tolerance and derating

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-G7-1 | The method is stated and suited to the use (extreme value, root-sum-square with its independence argument, or Monte Carlo with seed, run count and distribution) | note |
| CK-ANA-G7-2 | Tolerances include initial tolerance, temperature coefficient over the environment range, and ageing where the datasheet gives it; the derating rule applied to each part class is stated and sourced | inputs; derating rule |

## H. Hazards, risks and records

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-H1 | Every hazard the analysis bounds is named by id, and a result that changes a hazard control, a residual level or a single point failure entry is sent as a request to the `hazards.json` writer (PDR work plan section 5.3), not edited here | note; `hazards.json` |
| CK-ANA-H2 | Every risk the result raises, retires or re-scores is submitted to the risk register writer with its id or as a new entry request (section 5.3: WP-PDR-18 only) | note |
| CK-ANA-H3 | The note's change history names each revision with its date and the reason; a revision after the freeze of R1 names the delta iteration of this record (rule C2) | note history |

## I. Visual closure (charter section 11 rule 3; 08 section 1)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-I1 | Every plot and figure the note cites is rendered to PNG or SVG next to its source and was opened by the reviewer with the Read tool; `renders_inspected` counts them; a missing or unopened render is Major | render paths |
| CK-ANA-I2 | Each plot has labelled axes with units, the limit or mask drawn and labelled with its id, a legend where more than one trace is drawn, and a title or caption that names the case; the plotted values agree with the checker output at the marked points | renders |

## J. Software assurance items (when `criticality` is safety-critical or mission-critical; SWEHB section 7.1 tasks)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-ANA-J1 | SWEHB `swe-070` section 7.1 task 1: the models, simulations and analysis tools used to qualify flight software or flight equipment are validated and accredited (CK-ANA-C2 answered for each) | TV records |
| CK-ANA-J2 | SWEHB `swe-134` section 7.1 tasks 1 and 6: where the analysis sets a value for a SWE-134 item (for example item j response time, item i single event), the value is consistent with the hazard analysis and the 07 section 14.2 provision for that item | 07 section 14.2; `hazards.json` |
| CK-ANA-J3 | The tasks applied are listed in `assurance_tasks_applied` and each task's result is stated in this record | front matter |

## Completion criteria (SWE-088 b, c)

`verdict: APPROVED` when: readiness R1 to R6 were true; every applicable item is answered and the others are listed as N/A; the per-case table has one row per case of CK-ANA-F1 and every row has a result and a margin; the reviewer's own re-run (CK-ANA-C4) and independent check (CK-ANA-B5) are recorded; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate (under the convergence rule, a Minor finding raised after the first APPROVED verdict is a lien due at the CDR readiness declaration, PDR work plan rule C1); `renders_inspected` equals the number of renders the note cites; the front matter is complete with the measurements (SWE-089) filled; where 07 section 2.1.1 says Yes the assurance reviewer has returned `APPROVED` (`assurance_verdict`); and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. Findings stay Open until Claude marks them Verified after re-reading the corrected files at their new blobs. On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, and is listed in `deferred_rids`. An APPROVED record is the precondition for a value in `values_proposed` to go to the owner (PDR work plan rule C10); the value itself is ruled by the owner, never by this record.

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
PRODUCT: <path>@<blob>[, <path>@<blob> ...] at <product_commit>
FINDINGS:
- [Major] CK-ANA-F1 C-3 missing: REQ-<MOD>-NNN names 144.000 MHz and 148.000 MHz; only 146.000 MHz is analysed.
- [Minor] CK-ANA-A3 input table row 7: research citation lacks its confidence tag.
ITEMS N/A: CK-ANA-G2 to G7 (analysis_kind is simulation-deck), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: <id>: <value with unit> (supported | not supported)
MEASUREMENTS: size=N cases; inputs_checked=N; renders=N; turns=N; minutes=N; major=N; minor=N
```
