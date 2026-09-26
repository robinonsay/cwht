# 02 Requirements Definition, Management and Bidirectional Traceability

**Status:** Draft for SRR (revision D, 2026-09-25: revision C after its second independent review, re-aligned to charter commit b8214ca, which writes the software module files as `sw/sw-<sub>/`, lists the test-only case modules, keeps one peer-review record per product in `checklists/`, records the committed tinySA Ultra, and makes a host-verified software requirement `Verified` on its credited report and `Closed` only after PCA-05). **Expands:** charter `docs/process/00-charter.md` section 7 (levels, writing rules, validation, traceability set, TBD/TBR, change control), section 6 (identifiers) as they apply to requirements, and section 5 (Interface Requirements / Control Documents). **Owner:** Robin (Decision Authority, CCB, Engineering Technical Authority). **Author:** Claude (lead systems engineer). **Approval:** Robin approves this process as Engineering Technical Authority (charter section 2) in the SRR decision memo `docs/reviews/SRR/decision-memo.md`; SE-07, SE-08, SE-17 and SE-18 each require an ETA-approved process. Until that memo exists this document is the Draft that governs the work toward SRR.

**Governing text.** NPR 7123.1D SE-07 (Stakeholder Expectations Definition, §3.2.2.1; the expectation factors of §3.2.2.2, whose item h includes system security, transportability and disposability), SE-08 (Technical Requirements Definition, §3.2.3.1; §3.2.3.2: the technical team ensures system security requirements, including cybersecurity, are considered), SE-17 (Requirements Management, §3.2.12.1), SE-18 (Interface Management, §3.2.13.1); the minimum review products of §5.2.2.2 this process delivers: SE-35 and SE-37 (MCR, absorbed by SRR), SE-39 (SRR), SE-40 and SE-42 (SDR, absorbed by PDR). NPR 7150.2D SWE-027 (item a: the requirements to be met by a reused component are identified), SWE-050, SWE-051, SWE-052 (§3.12.1 Table 1), SWE-053, SWE-054, SWE-055, SWE-087, SWE-184, SWE-200, SWE-210, SWE-211. SE HB §4.1 (§4.1.1.2.1 identify stakeholders; NGOs; MOEs), §4.2 (§4.2.1.2.2 sources of technical requirements; §4.2.1.2.3 acceptable statements, rationale and KDRs; §4.2.1.2.4 validation; §4.2.1.2.5 MOPs and TPMs; Table 4.2-2 metadata), §6.2 (requirements management, self-derived requirements, CCB), §6.3 (interface management), §6.5.1.2.3 (change classes; waiver), App. C (how to write a good requirement), App. D (verification matrix), App. E (validation matrix), App. L (interface requirements document outline). Review criteria: NPR 7123.1D App. G Tables G-3 (MCR, absorbed by SRR, charter section 3), G-4 (SRR), G-5 (MDR/SDR, absorbed by PDR), G-6 (PDR), G-7 (CDR), G-10 (TRR), G-11 (SAR).

**Schemas.** `docs/requirements/schema.json` (L1 and L2 requirements), `docs/requirements/l0-stakeholder/schema.json` (L0 stakeholders and expectations; owned by this process), `docs/test_cases/schema.json` (verification cases). This document never overrides a schema; where a rule below is not machine-checkable by the schema it is checked by `tools/traceability.py` (section 8, with the implementation status of every rule in section 8.5) or by the independent reviewer (sections 4 and 5).

---

## 1. Purpose, scope and roles

This process turns stakeholder inputs into a validated, baselined, traceable requirement set and keeps that set consistent with interfaces, design, code, verification and nonconformances for the life of the product. It applies to every requirement file under `docs/requirements/`, every verification case file under `docs/test_cases/`, the ConOps scenarios in `docs/conops/conops.md`, every interface control document under `docs/icd/`, and the traceability tool `tools/traceability.py`.

| Role | Who | Responsibilities in this process |
|---|---|---|
| Decision Authority, CCB and Engineering Technical Authority | Robin | Approves this process (SRR decision memo), baselines (decision memo per charter section 4), every CR-NNN after SRR and every waiver (section 8.7); closes TBRs; dispositions RIDs and RFAs; performs validation step V2 for every stakeholder group of section 3.0 (section 5). |
| Author | Claude (main session) or an author agent | Writes the stakeholder entries, expectations, requirements, ICDs, rationale and verification notes; allocates IDs; runs the two checks of section 4.1 step 8 before every commit that touches a requirement, expectation, ICD or test file. |
| Independent reviewer | Reviewer agent, never the author of the product (charter section 2) | Applies the writing-rules checklist (section 4.2) and the six validation steps (section 5) line by line using `docs/templates/peer-review-checklist-requirements.md`; records the result in `docs/reviews/<REVIEW>/checklists/requirements-<module>.md`, the single peer-review record of the product (charter section 5). |
| Test author | Test-author agent, never the requirement author | Writes `TC-<MOD>-NNN` cases citing requirements; in the commit that ends a requirement draft, adds a `Draft` closing case of the same `verification_method` and of a closing type of section 4.4 for the requirement's module (section 4.1 step 7). |
| Tool | `tools/traceability.py` | Enforces the rules of section 8.2 to the extent stated in section 8.5; its report `docs/vv/traceability-report.md` is an entrance product of every review (charter section 7). |
| Software lead | Claude | Implements every open row of section 8.5 by the gate named there; a gate's readiness declaration is blocked until the rows due at that gate exit 0 on a seeded fixture (04 section 7.4, `tools/toolchain.lock.md` section 1.1). |

---

## 2. Requirement levels, files and identifiers

### 2.1 Levels

| Level | Content | Artifact | ID scheme | Under configuration control from |
|---|---|---|---|---|
| L0 inputs | Owner statements, verbatim, dated, never edited | `docs/requirements/l0-stakeholder/stakeholder-inputs.md` | `SI-NNN` | Append-only; not baselined |
| L0 stakeholders and expectations | Identified stakeholders; Need, Goals, Objectives; Measures of Effectiveness; Constraints | `docs/requirements/l0-stakeholder/expectations.json` (+ rendered `expectations.md`, section 8.1) | stakeholder `name` (section 3.0); `NGO-NNN`, `MOE-NNN`, `CON-NNN` | SRR (functional baseline) |
| L0 operations | ConOps scenarios, nominal and off-nominal | `docs/conops/conops.md`, one heading per scenario | `OPS-NNN` | SRR |
| L1 system | System requirements on the transceiver as a whole | `docs/requirements/sys/requirements.json` | `REQ-SYS-NNN` | SRR |
| L2 subsystem | Subsystem specifications | `docs/requirements/<mod>/requirements.json` for `rx`, `tx`, `pwr`, `ctl`, `me`, `sw` | `REQ-RX-NNN` ... `REQ-SW-NNN` | PDR (allocated baseline) |
| L2 software module | Software Requirements Specification, one file per firmware module | `docs/requirements/sw/sw-<sub>/requirements.json` (e.g. `sw/sw-keyer/`) | `REQ-SW-<SUB>-NNN` (e.g. `REQ-SW-KEYER-003`) | PDR |
| Interfaces | Interface control documents, one per interface | `docs/icd/ICD-<A>-<B>.md` (section 3.5) | `ICD-<A>-<B>` | PDR (allocated baseline, charter section 3; 05 Table 4-1 row 10). External stubs are reviewed at SRR but not baselined there |
| Design elements | Architecture blocks, schematic sheets, Rust modules | `docs/design/architecture.md`, `docs/design/allocation.json`, `hardware/kicad/<board>/<sheet>.kicad_sch` (05 Table 4-1 row 21; the architecture ADR names the boards), `firmware/cwht-core/src/<module>/<unit>.rs` and `firmware/cwht-app/src/**` (07 sections 1.2 and 3.5) | element id, sheet path, module path in `design_refs` | PDR (architecture), CDR (sheets, modules) |
| Code | Rust source | `firmware/**/*.rs` (workspace crates `firmware/cwht-core/`, `firmware/cwht-app/`, `firmware/cwht-hal-mock/`, `firmware/emu/`; 07 section 1.2) with `// @req`, `// @verify`, `// @design` tags (07 coding standard CS-24) | `REQ-` ids in tags | CDR / SAR |
| Verification | Verification cases, procedures | `docs/test_cases/<module>/test_cases.json` (`<module>` is the module id lower-cased, e.g. `sys`, `tx`, `sw-keyer`, `val`) | `TC-<MOD>-NNN` | With the requirements they cite: SRR for a case citing an L1 requirement, PDR for a case citing only L2 requirements (05 Table 4-1 row 17). `Active`, `Passed` and the other statuses are transitions of section 8.4, not baselines |
| Nonconformance | Discrepancies found in verification | `docs/vv/ncr/NCR-NNN.md` | `NCR-NNN` | n/a |

**Layout rule (tool rule T-02).** Charter sections 5 and 6 write the software module files as `docs/requirements/sw/sw-<sub>/requirements.json` (module id is the upper-cased directory name, `sw-keyer` gives `SW-KEYER`) with their cases in `docs/test_cases/sw-<sub>/`. The `module` of every `requirements.json` and `test_cases.json` is the upper-cased name of the file's immediate parent directory: `sys` is `SYS`, `sw` is `SW`, `sw/sw-keyer` is `SW-KEYER`, `docs/test_cases/sw-keyer` is `SW-KEYER`. A directory `docs/requirements/sw/keyer/` is rejected by T-02 because its module would read `KEYER`.

Hazards (`HZ-NNN`, `docs/safety/hazards.json`), decisions (`ADR-NNN`, `TS-NNN`), measures (`MOP-NNN`, `TPM-NNN`, `docs/plan/tpm.json`) and change requests (`CR-NNN`) are lateral references from requirements; their files are owned by the safety (SEMP section 7.1), decision-analysis (06), technical-assessment (SEMP sections 5.16 and 7.4) and CM (05) processes respectively.

### 2.2 Module set

| Module | Scope | Level |
|---|---|---|
| `SYS` | The transceiver as delivered to the operator: RF, controls, audio, power, enclosure, firmware behavior visible at the boundary | L1 |
| `RX` | Receive chain from antenna port to headphone audio | L2 |
| `TX` | Transmit chain from keyed carrier generation to antenna port, including PA and low-pass filtering | L2 |
| `PWR` | Battery cells and holder, charging, regulation, power sequencing, thermal sensing | L2 |
| `CTL` | Controller electronics: Pico 2 carrier, key jack input conditioning, encoder, LCD, audio output, USB connector | L2 |
| `ME` | Enclosure, antenna mount, knobs, facade, mechanical interfaces, mass and envelope | L2 |
| `SW` | Firmware requirements common to all modules (boot, scheduling, fault handling, update). Charter sections 5 and 7 use this module; charter section 6 omits it from its module list (section 14, CI-9) | L2 |
| `SW-<SUB>` | One firmware module. `SW-KEYER` exists from SRR because SI-018 (straight key and iambic paddles) is a core requirement. Further `<SUB>` names are created only by the ADR that records the firmware architecture (PDR); the ADR creates `docs/requirements/sw/sw-<sub>/` and `docs/test_cases/sw-<sub>/` in the same commit. `<SUB>` is one uppercase token `[A-Z][A-Z0-9]*`. | L2 |
| `VAL`, `ATP`, `SW-COV`, `SW-REG`, `SW-TOOL` | Test-only case modules (charter section 6; 04 section 1): `docs/test_cases/<module>/test_cases.json` exists, no requirements file exists, and their cases cite requirements of any module (`TC-VAL-NNN` validation cases name the `OPS-`/`MOE-` ids they validate after `Validates:` in `setup`; `TC-ATP-NNN` acceptance cases cite the requirements re-verified per unit; `TC-SW-TOOL-NNN` toolchain-proof and tool-accreditation runs, 07 section 3.1, with `credit: false` before a TV record exists). `SW-BOOT` and `SW-CFG` are firmware modules with requirement files (07 section 4), not test-only. | test only |

The requirements schema also names a `VER` module; charter section 6 reserves it as unused. No file declares it, and giving it a scope is a charter change through a CR.

### 2.3 Level rules

| Rule | L1 (`SYS`) | L2 (`RX`, `TX`, `PWR`, `CTL`, `ME`, `SW`, `SW-<SUB>`) |
|---|---|---|
| `parent_id` | Always `null`. | A `REQ-SYS-NNN` (allocated requirement) or another L2 id (derived requirement, e.g. an interface requirement whose driver is a sibling module's requirement, or a `REQ-SW-<SUB>-` requirement under a `REQ-SW-` one). `null` only for a self-derived requirement (below). |
| `source_ids` | At least one entry. The first entry is the primary L0 source, an `NGO-`, `MOE-`, `CON-` or `OPS-` id (section 3.4); `SI-` ids follow as supporting sources. | Optional. Required (an `ADR-` or `TS-` id) when `parent_id` is `null`. |
| Validation path (Table G-4 entrance 6.8: verification and validation method identified for each requirement) | At least one `source_ids` entry is an `OPS-` or `MOE-` id. That id's row of the App. E validation matrix (04 section 7.2) names the `TC-VAL-NNN` case that validates it, and the SRR validation summary lists, per L1 requirement, the `OPS` or `MOE` id and the `TC-VAL` case. | Inherited through `parent_id`. |
| Self-derived (SE HB §6.2.1.2.3) | Not applicable: every L1 requirement traces to L0. | `parent_id` is `null`, `rationale` begins with the literal `Self-derived:` and either `source_ids` contains an `ADR-NNN` or `TS-NNN` that records the design decision, or `hazard_ids` is non-empty (control derived from hazard analysis, SWE-184). SE HB §6.2.1.2.3 asks for concurrence from "the next higher level requirements sources": Robin, as owner of the parent level, concurs in the V2 record (before the level's baseline) or in the PDR decision memo, and the reviewer checks that the concurrence is recorded. Without it the requirement is gold plating and is retired (section 11.3). |
| Subject of the statement | `The transceiver` | The subsystem name as written in `docs/design/architecture.md` (e.g. `The receiver`, `The keyer firmware`). |
| Flowdown | At SRR, preliminary allocation (Table G-4 entrance 5.1; 01 section 4.3 row 7): every SYS requirement names at least one receiving L2 module, either through `child_ids` naming `Draft` L2 entries or through a preliminary `docs/design/allocation.json` record that lists the SYS id in `requirement_ids` under the receiving module (T-18 lists every gap as a Warning; the reviewer confirms or corrects each in V6). From PDR, every Active SYS requirement has at least one child or carries tag `leaf` with the rationale stating why it is verified at system level only (T-18 Error; SE-42). | Duplication between levels is resolved (SE HB §6.2.1.2.3): when an L2 requirement repeats its parent and is not an externally imposed constraint, the reviewer records in V6 which level keeps the requirement (SE HB: such a requirement "may not belong at the higher level"), and the other one is retired. |
| Reused and OSS components (SWE-050; SWE-027 item a) | Not applicable: L1 names no component. | A requirement that a reused or OSS component of the third-party register (07 section 17.1: rustos `api` and `pico2`, Rust `core`) must meet is written in the `SW-HAL` module file (07 section 4 item 1: the rustos driver behaviors cwht relies on) once the architecture ADR creates that module at PDR, and in `SW` before then; a requirement that concerns only one consuming module's use of the component sits in that module's `SW-<SUB>` file. Each carries tag `reused`, a `design_refs` entry `rustos:<path>` naming the crate or module path relative to the rustos repository root (e.g. `rustos:firmware/pico2/src/timer.rs`; commit per `tools/toolchain.lock.md` section 3), and the `WP-SW-NN` work package (07 section 19) in its `Why:` item. Each is verified to the same level as developed code (SWE-027 item e; SWE-211; RMM rows SWE-027 and SWE-211). |
| TBR closure limit | PDR | CDR |

Tags with obligations (the same for L1 and L2; other tags carry no obligation):

| Tag | Obligation | Checked by |
|---|---|---|
| `safety` | `hazard_ids` non-empty; on a `SW` or `SW-<SUB>` requirement, the rationale item `Depends on:` (section 4.3; SWE-184) | T-08 (`SAFETY_TAG_NO_HAZARD`); reviewer in V3 for `Depends on:` |
| `regulatory` | `source_ids` contains a `47CFR<part>.<section>` clause of Part 1, 2, 15 or 97 (section 3.4) | T-07 (`REGULATORY_TAG_NO_CLAUSE`) |
| `security` | `source_ids` contains a `CON-` or `ADR-` id that records the cybersecurity assessment scope of charter section 12 (assessment in 07 section 16), and the `Why:` item names the 07 section 16.2 row and the `RSK-NNN` (tag `cyber`) the requirement mitigates | T-07 (planned `SECURITY_TAG_NO_SOURCE`); reviewer in V3 for the named assessment |
| `interface` | an `ICD-<A>-<B>` id in `design_refs` (section 3.5) | T-22 (`INTERFACE_TAG_NO_ICD`) |
| `reused` | a `rustos:` or other component path in `design_refs` and the `WP-SW-NN` in `Why:` (row above) | T-15 (planned `REUSED_TAG_NO_REF`) |
| `leaf` | the rationale states why the requirement is verified at system level only | T-18 |
| `waived` | an approved product waiver (section 8.7; 05 section 2: a CR with disposition `Approved (waiver)` or a numbered waiver `W<n>` in a decision memo) names the requirement, and the waiver register (CSA item 12, 05 section 6) lists it | T-11 (planned `WAIVER_UNRECORDED`) |
| `retired` | the interim retirement marker of section 11.3 | T-19 |
| `hsi` | none; marks human-systems-integration requirements (SEMP section 7.3.1) | none |
| `70cm-ready` | none; marks growth provisions (SI-002) | none |

### 2.4 Requirement types that a complete set covers

Completeness is checked against this list at SRR for L1 and at PDR for each L2 module (SE HB App. C C.4 Completeness, whose list of requirement areas the rows follow; SE HB §4.2.1.2.2, sources of technical requirements; NPR 7123.1D §3.2.2.2 item h for security, transportability and disposability; §3.2.3.2 for system security in the technical requirements). Each row is either covered by at least one requirement or marked not applicable with a reason in the validation record; the SRR package carries the filled table (section 5).

| Type | cwht examples |
|---|---|
| Functional | Key from a straight key and from iambic paddles (SI-018, one requirement per key type); tune within the 2 m band (SI-024); sidetone; receive A1A |
| Performance | Carrier power and tolerance; keying speed range and element timing; receiver sensitivity; frequency accuracy; battery endurance |
| Interface | Key jack (3.5 mm TRS for both key types, CON-012, ADR-009), headphone jack, antenna connector, USB (firmware load and charging, SI-022), 18650 cells (SI-023); internal ICDs between CTL, RX, TX, PWR, ME and SW (section 3.5) |
| Environment | Operations: operating temperature range, handheld shock (NGO-026). Transport and storage: OPS-010 storage and transport, storage temperature, cell state of charge in storage. Manufacturing and test: reflow and hand-solder limits of the kit model (SI-031, CON-014), bench test conditions (04 section 6.1) |
| Safety | PA over-temperature inhibit; charging faults; RF exposure; unintended continuous transmission (stuck key or paddle, mono plug, OPS-013) |
| Security | Integrity check of a USB-loaded firmware image and rejection of an image that fails it (OPS-011); rejection of malformed input on the key and USB serial paths; the persistent event log of integrity failures, rejected configuration loads, watchdog resets and brown-out resets (RMM row SWE-210; 07 section 16.5); tag `security`. Scope per charter section 12: the radio has no network interface |
| Regulatory | 47 CFR 97.307 emission standards; 97.305 authorized emission types (A1A); 97.313 transmitter power; 97.119 station identification; RF exposure 1.1310 and 2.1093 (charter section 1); tag `regulatory`. Every clause is cited in the `47CFR<part>.<section>` form of section 3.4 and resolves to a file of the regulatory corpus `docs/references/md/regulatory/` (verbatim eCFR text, issue 2026-09-23), which exists and so meets 01 section 4.3 row 28 and section 5.3 row 12 |
| Human systems integration and operability | Control count and placement (SI-006); display legibility; audio level range; key and paddle ergonomics, keyer settings (charter section 12); tag `hsi` |
| Training | Content of the operations handbook `docs/ops/operations-handbook.md` that lets a Technician-class friend operate the unit from the handbook alone (MOE-008, MOP-017); no separate training product exists |
| Transportation | Pocket carry between sites (OPS-010); antenna port ruggedness (NGO-026); shipping is the vendors' packaging only, recorded as the reason no further requirement exists |
| Appearance and physical characteristics | Enclosure envelope and mass (MOP-001, MOP-002); panel marking of jacks and controls; enclosure finish and edges (HZ-013) |
| Producibility | PCBWay turnkey SMT assembly with owner hand-soldering of through-hole parts and simple pads (SI-031, CON-014); stocked catalog parts (SI-028); CNC-machinable enclosure (SI-008, CON-015) |
| Maintainability | Firmware update over USB; user-replaceable cells; test pads for the sensor and key inputs |
| Reliability and fault response | Detection, reporting and response to stuck key, sensor failure, low battery, synthesizer unlock (App. C C.4: undesired events and their responses); every requirement that implements the fault tolerance philosophy of `docs/safety/hazard-analysis.md` section 8.1 carries the rationale item `Fault tolerance:` (section 4.3; Table G-4 success criterion 14) |
| Disposal | End of life of the unit and of the 18650 cells through the end-of-life section of the operations handbook (NPR 7123.1D §3.2.2.2 item h, disposability; charter section 12: SE-51 and SE-52 tailored with this intent) |
| Facility and personnel | Not applicable at L1, with the reason recorded: no facility beyond the owner's bench (04 section 6.1); operator qualification is a constraint (CON-001, ADR-014), and App. C C.4 Compliance keeps personnel assignments out of requirements |
| Design constraints | Mandated technology (the `CON-` entries of kind `Technology`: Pico 2 and rustos, 18650 cells, semi break-in, full 2 m band) reflected as requirements where they bound the product |
| Growth | 70 cm path kept open (SI-002, CON-022), tag `70cm-ready` |

---

## 3. L0: stakeholders, inputs, expectations, ConOps scenarios and interfaces

### 3.0 Identify stakeholders (SE HB §4.1.1.2.1; SE-35)

Consumes: `stakeholder-inputs.md`, charter section 2. Produces: the `stakeholders` array of `docs/requirements/l0-stakeholder/expectations.json` (schema definition `stakeholder`: `name`, `role`, `interests`, `represented_by`, `source_ids`, optional `note`), baselined at SRR with the rest of the file (NPR 7123.1D §5.2.2.2: SE-35, baselined stakeholder identification and expectation definitions; Table G-3 entrance 3.1; 01 section 4.3 row 1). The schema requires the array once `baseline` is set; tool rule T-21 reports it missing before SRR, checks that names are unique and that every `source_ids` entry resolves.

Stakeholders identified for cwht (Claude writes these entries; the JSON is the record):

| Stakeholder (`name`) | `role` | Interests | `represented_by` in V2 | `source_ids` |
|---|---|---|---|---|
| Robin (customer) | `customer` | A pocket true-CW 2 m radio for contacts among friends, accepted at SAR; the evidence that it works at first power-on | Robin | SI-001, SI-010, SI-015 |
| Robin (operator) | `user` | Operates his unit as his own station with a straight key or paddles and headphones | Robin | SI-005, SI-014, SI-018 |
| Friends who receive and operate units | `guest operator` | Operate a unit as their own station; usability from the handbook; safety | Robin (representation rule below) | SI-019, SI-030 |
| Federal Communications Commission (47 CFR Parts 1, 2, 15 and 97) | `regulator` | Emission limits, power, station identification, RF exposure | The verbatim regulatory corpus, read clause by clause by the reviewer in V3; Robin as licensee in V2 | SI-014, SI-030 |
| PCBWay | `vendor` | Fabrication, SMT assembly and CNC machining within its published capabilities | Its published design rules and DFM feedback, checked in V4 | SI-008, SI-009, SI-031 |
| DigiKey and the turnkey distributors | `vendor` | Stocked parts | Catalog availability, checked in V4 | SI-009, SI-028 |
| Claude | `supplier` | Requirements it can design to and verify | Not a V2 voice (author of the requirements) | SI-011 |
| Open-source reusers and bystanders | `public` | Reuse under the MIT license; RF exposure of non-operators near a transmitting unit | Robin in V2; bystander exposure through HZ-006 and 47 CFR 1.1310 | SI-025, SI-030 |

**Representation rule.** Robin represents the guest-operator group and the public in V2. Basis: charter section 2 makes the owner customer and end user, and charter section 9 validates with the owner as the user. SE HB §4.2.1.2.4 step 2 reads "All relevant stakeholder groups identify and remove defects", so the V2 record names, for each L1 requirement, the stakeholder groups its confirmation speaks for. Robin confirms or changes this representation in the SRR decision memo; a later change (for example, a friend reviewing the operations handbook directly) is logged as a new `SI-NNN` and, after SRR, made to the array by a CR (section 10.2). Charter section 6 has no stakeholder id scheme, so entries are keyed by `name` (section 14, CI-10).

### 3.1 Stakeholder inputs (`SI-NNN`)

Consumes: owner statements in conversation. Produces: a new row in `docs/requirements/l0-stakeholder/stakeholder-inputs.md`.

1. Record each owner statement the day it is made as a new row `SI-NNN` with date and the statement in the owner's words. Never edit a row; a clarification, restatement or reversal is a new row that names the row it clarifies (a restatement that adds no new content is still logged when the owner asks for it to be, otherwise the existing row is cited).
2. An input marked by the owner as a core requirement (as SI-018 is: **straight key and iambic paddles, built-in keyer**) is flagged in bold in the row and must be cited in `source_ids` of at least one L1 requirement at SRR (tool rule T-20); the validation record for SRR lists every bold row with the requirement ids that cover it.
3. Inputs are the only admissible evidence of stakeholder intent in validation step V2 (section 5).

### 3.2 Expectations (`NGO-NNN`, `MOE-NNN`, `CON-NNN`)

Consumes: `stakeholder-inputs.md`, `docs/conops/conops.md`, the stakeholders of section 3.0. Produces: `docs/requirements/l0-stakeholder/expectations.json` validated against `docs/requirements/l0-stakeholder/schema.json`, and the rendered `expectations.md` (section 8.1).

| Entry | Definition applied on cwht | Fields (schema) |
|---|---|---|
| Need (`NGO-NNN`, kind `Need`) | The single problem statement; one per project; not a solution (SE HB §4.1.1.2.3). | `statement`, `rationale`, `source_ids` (SI), `parent_id` null |
| Goal (`NGO-NNN`, kind `Goal`) | Elaboration of the Need; need not be quantitative but must be assessable (SE HB §4.1.1.2.3). | `parent_id` is the Need |
| Objective (`NGO-NNN`, kind `Objective`) | Specific, measurable, attainable, results-oriented target for a Goal (SE HB §4.1.1.2.3). Objectives are not requirements; they are what the L1 set is validated against. | `parent_id` is a Goal |
| MOE (`MOE-NNN`) | Success criterion from the owner's point of view; failure to meet it makes the radio unacceptable to the owner (SE HB §4.1.1.2.6; NPR 7123.1D App. A). May be qualitative. | `statement`, `success_criterion`, `ngo_ids`, `ops_ids`, `source_ids` |
| Constraint (`CON-NNN`) | A condition the design must meet that is not open to trade (SE HB §4.2.1.2.1): regulation, an existing interface, a mandated technology, a resource limit. | `kind`, `statement`, `rationale` (who imposes it, what relief exists), `source_ids` (SI or regulation clause) |

Rules:

1. Expectation statements never contain `shall` (schema-enforced). They say what the owner expects, not what the product does.
2. Every NGO cites at least one `SI-NNN`. Every MOE cites at least one NGO and, once the ConOps exists, at least one `OPS-NNN` in which the owner will judge it.
3. Exactly one entry has kind `Need`; every Goal's `parent_id` is the Need; every Objective's `parent_id` is a Goal; every `ngo_ids` and `ops_ids` entry resolves (tool rule T-21; the schema checks the id patterns only).
4. Constraints derived from 47 CFR cite the clause in `source_ids` in the form `47CFR<part>.<section>[(paragraph)]` for Parts 1, 2, 15 and 97 (`47CFR97.307(e)`, `47CFR1.1310`; schema definition `regulation_clause`), together with SI-014 as the input that makes Part 97 applicable. The clause resolves per section 3.4 (T-07).
5. `expectations.json`, including the `stakeholders` array, is baselined at SRR (section 11.2 sets `baseline` to `"baseline/srr"` and every `Draft` entry to `Baselined`); after that, every change is a `CR-NNN` (section 10). Allowed status transitions of L0 entries are in section 8.3.

### 3.3 ConOps scenarios (`OPS-NNN`)

`docs/conops/conops.md` (SE HB App. S outline) carries one heading per scenario in the form `### OPS-NNN <title>`, nominal and off-nominal, each stating actors, preconditions, steps, expected outcome and the MOEs it exercises. Scenarios are the reference for validation (charter section 9) and for the App. E validation matrix (section 7). A requirement whose rationale describes operator activity cites the scenario instead of describing it (writing rule WR-06). At least one scenario exercises the straight key (OPS-005) and at least one the iambic paddles (OPS-004) (SI-018; 01 section 4.3 row 10).

### 3.4 Citing sources in `source_ids`

`source_ids` is an ordered list; the first entry is the primary source the requirement most directly derives from, and for a SYS requirement it is an L0 id (`NGO-`, `MOE-`, `CON-` or `OPS-`, section 2.3). Accepted forms and their resolution:

| Form | Resolves to | File | If the file does not exist yet |
|---|---|---|---|
| `SI-NNN` | Table row | `docs/requirements/l0-stakeholder/stakeholder-inputs.md` | Not applicable (file exists) |
| `NGO-NNN`, `MOE-NNN`, `CON-NNN` | Entry `id` | `docs/requirements/l0-stakeholder/expectations.json` | Warning in `check`, Error in `gate` |
| `OPS-NNN` | Heading `OPS-NNN` | `docs/conops/conops.md` | Warning in `check`, Error in `gate` |
| `ADR-NNN` | File `docs/decisions/adr/ADR-NNN-*.md` | | Error |
| `TS-NNN` | File `docs/decisions/trade-studies/TS-NNN-*.md` | | Error |
| `47CFR<part>.<section>` or `47CFR<part>.<section>(x)`, `<part>` one of 1, 2, 15, 97 | Regulation clause: the `<part>.<section>` resolves to a corpus file; the paragraph letter is checked by the reviewer against that file | `docs/references/md/regulatory/47cfr-<part>.<section>.md`, or an extract `47cfr-<part>.<section>-<slug>.md` such as `47cfr-2.106-harmonic-bands.md` (charter section 1; verbatim eCFR text, issue 2026-09-23) | Error. The corpus exists, so a clause without a file is a wrong citation or a missing corpus section. Claude adds the section in the same commit with the eCFR versioner API command recorded in `docs/references/md/regulatory/README.md` ("Provenance and currency"), saves the text verbatim with the header fields listed there (API URL, reader URL, amendment dates) and adds its row to that README's index |

The tool resolves every form of this table today (section 8.5, T-07). Hazards are cited in `hazard_ids`, never in `source_ids`. Measures are cited in `mop_ids`. Interfaces are cited in `design_refs`. Research reports (`docs/research/*.md`) are cited by path inside `rationale`, not in `source_ids`.

### 3.5 Interface requirements and ICDs (SE-18; SE HB §6.3, App. L)

Consumes: `docs/design/architecture.md` (module boundaries), the ADR that records the architecture, L2 requirements tagged `interface`, external-interface constraints (`CON-NNN` of kind `Interface`: CON-010 USB, CON-012 key jack, CON-013 headphones; SI-023 cells). Produces: `docs/icd/ICD-<A>-<B>.md` from `docs/templates/icd.md`, and one `interface`-tagged requirement per side in the module files.

| Rule | Statement |
|---|---|
| Identity | One file per interface, `docs/icd/ICD-<A>-<B>.md`, id `ICD-<A>-<B>`. `<A>` and `<B>` are module tokens from section 2.2 (`SYS` excluded; `SW` stands for the firmware as a whole, a per-module firmware boundary is a design interface in `architecture.md`, not an ICD) or, for an external interface, `<B>` is one of the external tokens `KEY` (key or paddle jack), `PHONES` (headphone jack), `ANT` (antenna connector), `USB` (USB connector: firmware loading and charge power, SI-022), `CELL` (18650 cells and holder, SI-023), `HOST` (USB host computer: bootloader and serial command set). Adding a token is a Class II change to this document. |
| Order | For two modules, `<A>` precedes `<B>` in the charter module order `RX, TX, PWR, CTL, ME, SW` (so `ICD-CTL-SW`, never `ICD-SW-CTL`). For an external interface, `<A>` is the module and `<B>` the external token (`ICD-CTL-KEY`, `ICD-SW-HOST`, `ICD-TX-ANT`, `ICD-PWR-CELL`). The file name is therefore unique per pair. |
| Owner | The author of side `<A>` writes and maintains the file (App. L 1.3 responsibility); both sides' authors and the independent reviewer sign the PDR validation record; Robin approves the ICD with the allocated baseline. A third module with requirements against the interface (PWR against `ICD-CTL-USB` for charge power) cites the ICD in `design_refs` but is not a side. |
| Creation | External-interface stubs (`ICD-CTL-KEY`, `ICD-CTL-PHONES`, `ICD-TX-ANT`, `ICD-CTL-USB`, `ICD-PWR-CELL`) are created before SRR by Claude with sections 1, 2 and 3.1 filled and every 3.2 subsection either filled, marked `Preliminary` or marked `Not applicable` (01 section 4.3 row 17: external interfaces identified with preliminary definitions). Internal ICDs and `ICD-SW-HOST` (charter section 5, additional ICDs) are created by the ADR that records the architecture (ADR section 4.2 names them and the same commit creates them) or by the L2 allocation that first needs one, whichever is earlier. The architecture ADR may move an external interface to another owning module by superseding the stub with a renamed file and a superseding note. |
| Content | The outline of `docs/templates/icd.md`, which maps one to one onto SE HB App. L sections 1.1 to 3.2.8 with two cwht additions: section 4 (requirements on each side) and section 5 (verification cases). The ICD holds the definition tables (pins, levels, timing, connector, envelope, protocol); no `TBD`; an estimated value carries `(TBR)` and a row in the ICD's TBR table with owner, plan and `close_by` (CDR at the latest, SEMP section 5.12). Every ICD with a physical interface carries a rendered figure (charter section 11 rule 3). The ICDs of the paths that carry data or commands, `ICD-CTL-USB` (firmware loading), `ICD-SW-HOST` (bootloader and serial command set) and `ICD-CTL-KEY` (the key input as a command-injection path), carry a row `Security expectations` in section 3.2.6 (section 3.2.5 for `ICD-CTL-KEY`) stating what each side accepts, rejects and logs (Table G-4 success criterion 4; charter section 12; 07 section 16.2). |
| Pairing | Every interface has at least one requirement tagged `interface` in the module file of each side (both sides for a module pair; the module side only for an external interface; for `<B>` = `SW`, any file under `docs/requirements/sw/` counts as the SW side), each with the ICD id in `design_refs`. Each side's requirement states what that side delivers or accepts at the interface plane with a value, so it is verifiable alone (SE HB §6.3.1.2.3: interface requirements verification is part of system verification); the reviewer checks that the two sides and the ICD tables agree (checklist item CK-REQ-C2). The two sides and the ICD change in one CR. Tool rule T-22 checks the pairing. |
| Baseline and change | External stubs are reviewed before SRR against `docs/templates/peer-review-checklist-design.md` section I (Table G-4 entrance 6.11) but are not baselined at SRR, because the charter section 3 functional baseline does not list ICDs. Every ICD is baselined at PDR with the allocated baseline (charter section 3; 05 Table 4-1 row 10) after independent review; any change after PDR is `Class I` (section 10.2). |
| Measures | ICDs approved versus identified, and open ICD TBR count (zero at CDR), reported in the PDR and CDR packages (SEMP section 5.12). |

Worked example (SI-018, SI-034, ADR-009): `ICD-CTL-KEY` defines the single 3.5 mm TRS KEY jack: tip = dit and hand key, ring = dah, sleeve = signal ground, tip and ring sensed as two independent inputs; the input network, contact voltage and current, debounce times (TBR per ADR-009) and ESD provision; key type selected by menu, with no automatic detection in rev A. A mono (TS) plug grounds the ring; it is the OPS-013 off-nominal case, handled by the firmware power-on interlock. Each requirement states one capability (WR-03): `REQ-CTL-005` (tag `interface`, `design_refs` `[ICD-CTL-KEY]`) states that the controller accepts a TRS plug; `REQ-CTL-006` and `REQ-CTL-007` (CTL side of `ICD-CTL-SW`) state the registration time of a tip closure and of a ring closure; `REQ-SW-KEYER-001` (SW side of `ICD-CTL-SW`) states what the keyer firmware does with a straight-key closure. The ids are illustrative until those files exist.

---

## 4. Writing requirements

### 4.1 Procedure

| Step | Consumes | Produces | Rule reference |
|---|---|---|---|
| 1. Bound the problem | `expectations.json` stakeholders and constraints, `conops.md`, ICD list (section 3.5) | List of constraints and external interfaces to be reflected as requirements | SE HB §4.2.1.2.1 |
| 2. Draft functional requirements | NGOs, OPS scenarios | `REQ-<MOD>-NNN` entries, status `Draft`, one function each | SE HB §4.2.1.2.2 |
| 3. Attach performance requirements | MOEs, MOPs in `docs/plan/tpm.json`, budgets in `docs/research/` and `docs/design/budgets.md` | Separate `REQ` entries quantifying each function with value, unit, tolerance; `mop_ids` set when the value is a MOP or TPM | SE HB §4.2.1.2.2, §4.2.1.2.5 |
| 4. Write rationale | Sources | `rationale` per section 4.3 | SE HB §4.2.1.2.3, Table 4.2-2 |
| 5. Assign verification | The instrument set of charter section 9 and CON-016 as detailed in 04 section 6 (6.1 credit-bearing measurements, 6.2 quantities measured indirectly or by Analysis); the closing evidence by module (section 4.4) | `verification_method`, `verification_note` per section 4.4 | Table 4.2-2; 04 section 5.2 |
| 6. Set traceability fields | Sections 2.3, 3.4 and 3.5 | `parent_id`, `source_ids` (primary L0 id first for SYS), `hazard_ids`, `design_refs` (ICD ids), `tags`, `priority` | SWE-052 |
| 7. Draft the closing case | The drafted requirements | A test-author agent (not the requirement author) adds, in the same commit, a `Draft` case `TC-<MOD>-NNN` in `docs/test_cases/<module>/test_cases.json` of the requirement's module, citing the requirement, with the same `verification_method` and a closing type of section 4.4 for that module; the requirement's `verification_note` names the case id | 04 section 16 (SRR: L1 cases drafted by the test author); T-09 |
| 8. Self-check | Section 4.2 checklist; `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`; `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py` | Zero violations; Warnings listed in the commit message. `--report-only`, and `TC pending` in a `verification_note`, are admitted only in drafting runs before step 7; the commit that ends the draft exits 0 | Section 8 |
| 9. Independent review | Sections 4.2 and 5; `docs/templates/peer-review-checklist-requirements.md` | `docs/reviews/<REVIEW>/checklists/requirements-<module>.md` | SWE-087, charter section 2 |
| 10. Baseline | Review decision memo | Status `Draft` to `Active` for the level; git tag `baseline/<review>` (section 11.2) | SE HB §4.2.1.2.6, charter section 8 |

### 4.2 Writing-rules checklist (SE HB App. C, distilled)

The reviewer applies every rule to every requirement and records the failing rule ids per requirement. A requirement with any failure is a RID candidate: Major for WR-01, WR-03, WR-04, WR-05, WR-07, WR-11 and WR-13 (the requirement cannot be verified or traced as written), Minor for the others. Rules marked "tool" are also linted by `tools/traceability.py` (rule T-17, status in section 8.5); the reviewer still judges the cases the lint cannot.

| Id | Rule | Pass test | Source |
|---|---|---|---|
| WR-01 (tool) | Terms | `description` contains exactly one `shall` and none of the WR-07 group A words. `will` appears only in `rationale` to state a fact. `should` appears only in the `rationale` of a `priority: Goal` requirement. | App. C C.1 |
| WR-02 | Form and voice | Statement has the form `The <product> shall <verb> <object> [<performance>]`. Subject per section 2.3. Active voice. None of `shall be able to`, `shall be capable of`, `shall be designed to`, `shall allow`. Not `The operator shall`. | App. C C.2 |
| WR-03 | One thought | One subject, one predicate, one verifiable outcome. No `and` joining two capabilities, no `and/or`, no lists, no rationale text in `description`. Test: one verification case with one pass/fail result can close it. | App. C C.4 Clarity |
| WR-04 | Quantified | Every performance value has a number, a unit (SI, dB, WPM, %) and a bound or tolerance (`at least`, `at most`, `±`, a range) in `description`; a tolerance that appears only in `verification_note` fails. No adjective stands in for a number. A best-estimate value is followed by `(TBR)`. | App. C C.2 |
| WR-05 | Implementation-free | States what is needed, not how. A part, topology, algorithm or component name appears only when it is a `CON-NNN` constraint or the `rationale` states why the solution is limited to that method. | App. C C.2, Table 4.2-2 rationale box |
| WR-06 | Product, not operations or tasks | No description of how the operator uses the radio (cite `OPS-NNN` instead) and no personnel or task assignment (belongs in the SEMP). | App. C C.2, C.4 Compliance |
| WR-07 (tool) | No unverifiable or ambiguous words | This rule holds the single banned-word list of the project; T-17 and any lint copy it verbatim. Group A (modal verbs other than `shall`): `will`, `should`, `must`, `may`, `can`, `might`. Group B (unverifiable or ambiguous): `flexible`, `easy`, `easily`, `sufficient`, `safe`, `ad hoc`, `adequate`, `adequately`, `accommodate`, `user-friendly`, `usable`, `when required`, `if required`, `as required`, `if possible`, `to the extent practicable`, `appropriate`, `as appropriate`, `approximately`, `fast`, `portable`, `light-weight`, `small`, `large`, `maximize`, `minimize`, `robust`, `quickly`, `clearly`, `etc.`, `and/or`, `but not limited to`, `support`, `TBD`. Matching is case-insensitive on whole words (`(?<![\w-])word(?![\w-])`); state names defined in the architecture are written in their CamelCase enum spelling (`SafeState`, `TxPending`) and are not matched. The reviewer additionally rejects standalone `this`/`these` and any other `-ly` adverb or `-ize` verb standing in for a measurable criterion. | App. C C.4 Verifiability, Clarity |
| WR-08 | Positive form | Written as `shall`, not `shall not`. `shall not` is admitted only when the prohibition is itself the regulatory or safety requirement and no positive form exists; the reviewer records why. | App. C C.3 |
| WR-09 | Level and location | The requirement sits in the file of the module that satisfies it; L1 names no subsystem or part; duplication between levels is resolved (SE HB §6.2.1.2.3): unless the requirement is an externally imposed constraint, the reviewer records which level keeps it. | App. C C.4 Compliance; SE HB §6.2.1.2.3 |
| WR-10 | Rationale content | `rationale` meets section 4.3. | SE HB §4.2.1.2.3, Table 4.2-2 |
| WR-11 | Verification assigned at definition | `verification_method` is set and consistent with the statement per section 4.4; `verification_note` names the pre-power-on evidence class, the post-build instrument or procedure from the instrument set of 04 section 6 (charter section 9, CON-016), and the closing `TC` id. `TC pending` is admitted only in a drafting run before section 4.1 step 7 and never in a commit that ends a draft (T-09 is an Error). | Table 4.2-2; charter section 9 |
| WR-12 (tool) | TBD/TBR | No `TBD` anywhere. `(TBR)` follows the value in `description` if and only if the `tbr` object is present with `owner`, `plan`, `close_by` within the level limit (section 2.3). | App. C C.3; section 9 |
| WR-13 | Traceability fields | `parent_id` and `source_ids` per section 2.3 (primary L0 id first and a validation path for SYS); tag obligations per section 2.3 (`safety`, `regulatory`, `security`, `interface`, `reused`, `leaf`, `waived`); interface pairing per section 3.5. | App. C C.4 Traceability; SWE-052 |
| WR-14 (tool, partly) | Editorial and schema | Grammar and spelling correct; `title` has no `shall`; `description` at most 25 words; terminology matches `conops.md` and the ICDs; id matches the pattern; file validates against `docs/requirements/schema.json`. | App. C C.3; schema |

### 4.3 Rationale content (SE HB §4.2.1.2.3 and the Table 4.2-2 rationale box)

`rationale` is free text of at most 120 words that contains, in this order and with these labels where the item applies:

1. `Why:` the reason the requirement exists, pointing to the constraint, ConOps scenario, parent or trade study that explains it (ids from section 3.4), including why the value and tolerance are what they are.
2. `Assumes:` every assumption the value or function rests on (technology, environment, load, operator). Assumptions are confirmed before baselining (App. C C.4 Correctness).
3. `Ops:` the `OPS-NNN` scenario(s) in which the requirement is exercised, when not already the primary source.
4. `Depends on:` for a `safety`-tagged `SW` or `SW-<SUB>` requirement, the hardware requirement ids and the `OPS-NNN` operator actions the software control relies on (SWE-184: constraints, controls, mitigations and assumptions "between the hardware, operator, and software"), for example the hardware PA-enable cutoff requirement and the operator's two-action override of RMM row SWE-184.
5. `Fault tolerance:` for a requirement that implements the fault tolerance philosophy of `docs/safety/hazard-analysis.md` section 8.1, the philosophy item number and any single point failure candidate of its section 8.2 the requirement addresses (Table G-4 success criterion 14; the SRR package lists these requirements).
6. `Constraint:` when WR-05 admits an implementation term, why the solution is limited to it.
7. `KDR:` for `priority: KDR`, which cost or schedule element the requirement drives (part, fabrication, enclosure, vendor lead time, verification effort).
8. `TBR:` for a TBR value, why the value is an estimate and what evidence closes it (the `tbr.plan` holds the plan; the rationale holds the reason).
9. `Self-derived:` as the first token when section 2.3 requires it; `Retired by ` as the first token of a retired requirement (section 11.3).

No `shall` appears in a rationale. `docs/templates/requirements.example.json` shows the order.

### 4.4 Verification method and closing evidence, assigned at definition

"Run for the record" verification is performed on the delivered unit, and only software requirements take HostUnit or Emulation credit (charter section 9; 04 section 5.2). A requirement is verified at the level at which it is stated (SE HB App. C C.4 Verifiability asks "Can this be done at the level of the system at which the requirement is stated?"; Table 4.2-2 "Verification level"). The module of the requirement therefore decides which evidence class can close it:

| `verification_method` | Closing case `type`, module `SYS`, `RX`, `TX`, `PWR`, `CTL`, `ME` | Closing case `type`, module `SW`, `SW-<SUB>` (04 section 5.2 rows) | Supporting only (never closes) | Assign when |
|---|---|---|---|---|
| Test | `Bench`, on the delivered unit (TRR-authorized, owner witnessed) | `HostUnit` for platform-independent logic; `Emulation` for a requirement that states only an event order, inside `ACC-EMU-001`; `Bench` for timing, peripherals, interrupts, DMA, clocks or power states | `Simulation`; `HostUnit` and `Emulation` for the hardware and system modules; dev-board `Bench` runs with `credit: false` | The quantity is measurable with the instrument set of 04 section 6.1 (charter section 9; CON-016: NanoVNA, tinySA Ultra with 30 to 40 dB attenuator, Pico-based logic capture, dummy load, bench supply, multimeter) or with the firmware test harness. A `regulatory`-tagged requirement is Test on the Bench unless a class 1 trade study decided by Robin changes it (06 section 14.1 item (g)). |
| Demonstration | `Bench` or `OnAir`, owner-operated on the delivered unit | `Bench` or `OnAir` | `Emulation` demonstration | The behavior is observed as pass/fail without a measured value (e.g. keying from a straight key and from paddles, menu operation, sidetone present). |
| Analysis | `Simulation` (LTspice, budgets, S-parameter models, Python checks); credit at CDR on the product baseline, confirmed at SAR (04 section 5.1 item 5) | `Simulation` | A Bench measurement that corroborates the analysis | The quantity cannot be measured with the instrument set: the quantities 04 section 6.2 assigns to Analysis (close-in keying bandwidth and envelope shape, RF exposure, receiver MDS and selectivity, thermal rise of the PA and enclosure, hardware switching delays). `verification_note` states the instrument gap and the model used. Analysis in place of Test on a `regulatory`-tagged requirement needs a class 1 trade study decided by Robin (06 section 14.1 item (g)). |
| Inspection | `Inspection` (ERC, DRC, schema and traceability checks, rendered-image review, receipt inspection, visual) | `Inspection` (code structure, driver-to-datasheet traceability) | none | The attribute is visible in an artifact: BOM part, connector type, marking, dimension on CAD, code structure. |

The closing case is a `TC` that cites the requirement, has the same `verification_method` and has a closing type of this table for the requirement's module; its `Passed` status with a credited report moves the requirement to `Verified` (section 8.3). Supporting cases reduce risk but do not close (charter section 9). A `HostUnit` or `Emulation` case that cites both a software requirement and its system parent is closing for the software requirement and supporting for the parent (T-10). Every `Draft` or `Active` requirement is cited by at least one case and has one closing case (rule T-09; 04 section 7.3 rule 2). The closing case sits in the module of the requirement it closes (section 11.1); supporting cases may sit in any module.

**Software requirements closed by `HostUnit` or `Emulation` (charter section 9).** Such a requirement becomes `Verified` on a credited report (front matter `credit: true`, `result: Pass`) run against the tagged release whose version description `firmware/releases/VDD-<version>.md` names it (`firmware_version` of the report; 05 section 4.3), with no NCR open against it. It becomes `Closed` only after the SAR decision memo and the physical configuration audit line PCA-05 (05 section 7.2) in `docs/vv/adp/CWHT-A-NNN/as-built.md`, which records the release installed on the delivered unit, names the same release as the credited report of every closing case (04 section 5.3). If a later release is installed, the release regression run `TC-SW-REG-001` on that release (04 section 10.5) supplies the credited report. T-11 checks both rules.

### 4.5 Metadata mapping: SE HB Table 4.2-2 to `docs/requirements/schema.json`

| Table 4.2-2 item | Function per SE HB | Schema field(s) | Note |
|---|---|---|---|
| Requirement ID | Unique numbering for sorting and tracking | `id` | Pattern `REQ-<MOD>-NNN`; allocation per section 11 |
| Rationale | Clarifies intent at time of writing | `rationale` | Content per section 4.3 |
| Traced from | Bidirectional parent and child links and relationships | Upward: `parent_id`, `source_ids`. Downward: `child_ids`, `design_refs`, and `requirement_ids` in test cases. Lateral: `hazard_ids`, `mop_ids` | Section 7 gives the full model |
| Owner | Writes, manages, approves changes | No field. Author is the git author of the commit; approval authority for every requirement is Robin through the baseline decision memo and CRs; the file-level `module` names the specification that owns it. | Schema has `additionalProperties: false`; a per-requirement owner field would need a schema CR and is not needed with one approver |
| Verification method | Test, Inspection, Analysis, Demonstration, decided as requirements are developed | `verification_method`, `verification_note` | Section 4.4 |
| Verification lead | Who verifies | No field. The independent test-author agent that owns the closing `TC` is named in the V&V report for that case (`docs/vv/reports/`); `automation_ref` in the test case names the executable check. | |
| Verification level | System, subsystem, element | The requirement's `module`: the closing case sits in that module and has a closing type of section 4.4 for it (`TC-SYS-` Bench, OnAir, Simulation or Inspection is system level; `TC-<L2>-` is subsystem level) | Section 4.4 |
| Project additions | | `title`, `description`, `status`, `tags`, `tbr`, `priority`, `module` | `priority`: `KDR`, `Baseline`, `Goal` (section 6.4, a project customization) |

### 4.6 Worked example: SI-018, straight key and iambic paddles

The example uses the real L0 ids of `expectations.json`, `conops.md` and `hazards.json`; the `REQ-` and `TC-` ids other than `REQ-SYS-002` (which is in `docs/templates/requirements.example.json`) are illustrative until those files exist. The owner's "both straight keys and iambic paddles" becomes two L1 functional requirements, one per key type, so that each is closed by its own demonstration (WR-03). Both keys use 3.5 mm TRS plugs (SI-034, CON-012), so one jack serves both (ADR-009); the key type is selected by menu.

```
SI-018  "Core requirement: straight key and iambic paddles (built-in electronic keyer)"   SI-034 TRS plugs
 └ NGO-003 (Goal)  Natural CW operation with either key type, headphones and minimal controls
    ├ NGO-013 (Objective)  Keyer modes, speed range and element timing
    ├ MOE-005  Keying feel and timing with both key types   ops_ids [OPS-004, OPS-005]
    ├ REQ-SYS-004 (L1, functional, Demonstration)
    │   The transceiver shall key the transmitter from a straight key connected to the key jack.
    │   source_ids [NGO-003, OPS-005, MOE-005, SI-018, SI-034, ADR-009]   closing TC-SYS-004 (Bench)
    │   ├ REQ-CTL-005 (L2, interface)  The controller shall accept a 3.5 mm TRS plug in the key jack.
    │   │    tags [interface]  design_refs [ICD-CTL-KEY]   closing TC-CTL-005 (Inspection)
    │   ├ REQ-CTL-006 (L2, interface)  The controller shall register a tip-to-sleeve closure within 2 ms.
    │   │    tags [interface]  design_refs [ICD-CTL-SW, hardware/kicad/<board>/key-input.kicad_sch]
    │   │    closing TC-CTL-006 (Test, Bench logic capture); supporting Simulation of the input network
    │   └ REQ-SW-KEYER-001 (L2, interface)  The keyer firmware shall key the transmitter for the whole closure of the straight-key contact.
    │        tags [interface]  design_refs [ICD-CTL-SW, firmware/cwht-core/src/keyer/straight.rs]   closing TC-SW-KEYER-001 (Test, HostUnit)
    ├ REQ-SYS-005 (L1, functional, Demonstration)
    │   The transceiver shall key the transmitter with Morse elements generated from iambic paddles connected to the key jack.
    │   source_ids [NGO-003, OPS-004, MOE-005, SI-018, SI-034, ADR-009]   closing TC-SYS-005 (Bench)
    │   ├ REQ-CTL-005 (shared child, parent_id REQ-SYS-004; REQ-SYS-005 named in its Why:)
    │   ├ REQ-CTL-007 (L2, interface)  The controller shall register a ring-to-sleeve closure within 2 ms.
    │   └ REQ-SW-KEYER-002 (L2)  The keyer firmware shall generate iambic mode A elements from paddle closures.
    │        design_refs [firmware/cwht-core/src/keyer/iambic.rs]   closing TC-SW-KEYER-002 (Test, HostUnit)
    └ REQ-SYS-002 (L1, performance, Test)   element timing from 5 to 50 WPM (SI-033, ADR-024, MOP-012)
        │   closing TC-SYS-002 (Test, Bench: TX_KEY captured with the Pico-based logic capture at 5, 15, 25, 50 WPM)
        │   supporting TC-SW-KEYER-003 (HostUnit; cites REQ-SYS-002 and REQ-SW-KEYER-003)
        └ REQ-SW-KEYER-003 (L2)  The keyer firmware shall time a dit at 1200 / WPM ms within ±0.5 %.
             closing TC-SW-KEYER-003 (Test, HostUnit)
HZ-004 "Unintended or stuck transmission"
 ├ REQ-SW-KEYER-004 (L2, safety)  key-down timeout   Depends on: the hardware PA-enable cutoff (a REQ-CTL-NNN of ADR-009 section 4.1), OPS-013
 └ REQ-SW-KEYER-006 (L2, safety)  power-on interlock: keying arms only after both contacts are open for 500 ms,
                                  so a mono (TS) plug that grounds the ring keeps the transmitter unkeyed (OPS-013)
ICD-CTL-KEY  (CTL side: REQ-CTL-005; external side: the TRS plug of SI-034)
ICD-CTL-SW   (CTL side: REQ-CTL-006, REQ-CTL-007; SW side: REQ-SW-KEYER-001)
```

`parent_id` is single-valued, so a child that serves two parents (REQ-CTL-005) is parented to the first and names the second in its `Why:` rationale item; the reviewer confirms in V6 that the second parent is still fully addressed by its remaining children. The plug types are covered one requirement each: the TRS plug of both keys by REQ-CTL-005, the mono plug of OPS-013 by the interlock REQ-SW-KEYER-006. The performance requirement `REQ-SYS-002` (5 to 50 WPM accepted by the owner in SI-033) is separate from the functional ones so that its Test method does not encumber the Demonstrations (WR-03, WR-04). It is closed at system level by the Bench case `TC-SYS-002` on the delivered unit; the HostUnit case `TC-SW-KEYER-003` closes `REQ-SW-KEYER-003` and only supports `REQ-SYS-002` (section 4.4). The firmware tolerance (±0.5 %, the MOP-012 target) is tighter than the system tolerance (the MOP-012 threshold) so that the hardware path keeps a margin.

---

## 5. Requirements validation: the six steps of SE HB §4.2.1.2.4 as a review checklist

The independent reviewer performs the six steps on every L1 requirement before SRR and on every L2 requirement before PDR, using `docs/templates/peer-review-checklist-requirements.md` (items `CK-REQ-A1` to `CK-REQ-F4`) and recording the result in `docs/reviews/<REVIEW>/checklists/requirements-<module>.md`. Charter section 5 (commit b8214ca) makes that filled checklist, with `id: INSP-NNN` in its front matter, the single peer-review record of the product; there is no `peer-reviews/` folder, and `tools/validate_docs.py` rejects one. The product slug is `requirements-<module>`, lower-cased. The record carries the template's front matter (`id: INSP-NNN`, product path and commit, reviewer invocation, verdict, measurements for 07 MSR-20 and MSR-21) followed by one row per requirement: `id | WR failures | V1 | V2 | V3 | V4 | V5 | V6 | CK-REQ items answered No | disposition (Pass, RID-<REVIEW>-NNN, Retire)`. Robin performs step V2 for every stakeholder group of section 3.0; the reviewer prepares the evidence.

Mapping between the two id schemes (so one record answers both):

| This document | Checklist items | This document | Checklist section |
|---|---|---|---|
| WR-01, WR-02 | CK-REQ-A1 | V1 written correctly | A (plus WR rules with no CK item: WR-06, WR-08, judged directly) |
| WR-03 | CK-REQ-A2 | V2 satisfy stakeholders | B4 evidence, Robin's confirmation |
| WR-04 | CK-REQ-A3 | V3 technically correct | C |
| WR-05 | CK-REQ-A5 | V4 feasible | D |
| WR-07 | CK-REQ-A4 | V5 verifiable | E |
| WR-09 | CK-REQ-B1, CK-REQ-F3 | V6 non-redundant | F |
| WR-10 | CK-REQ-A7 | | |
| WR-11 | CK-REQ-E1, CK-REQ-E2 | | |
| WR-12 | readiness R4 | | |
| WR-13 | CK-REQ-B1, CK-REQ-B5, CK-REQ-B6 | | |
| WR-14 | CK-REQ-A6, CK-REQ-A8 | | |

| Step | Question (SE HB §4.2.1.2.4) | Who | Evidence consumed | Pass criterion |
|---|---|---|---|---|
| V1 | Are the requirements written correctly? | Reviewer | Section 4.2 checklist, `tools/traceability.py` output | Zero WR failures; zero tool violations |
| V2 | Do the requirements satisfy stakeholders? | Robin, for every stakeholder group of section 3.0 (as its representative where `represented_by` names him), with the reviewer's trace summary | `stakeholder-inputs.md`; `expectations.json` (stakeholders, NGOs, MOEs, constraints); `conops.md`; the requirement's `source_ids` | Robin confirms that each L1 requirement reflects the cited `SI`/`NGO`/`MOE`/`OPS` and names the groups the confirmation speaks for; every core input (bold `SI`, e.g. SI-018 with one requirement per key type) is covered; disagreements become RFAs or RIDs |
| V3 | Are the requirements technically correct? | Reviewer | Parent and source entries; `rationale` assumptions; research reports cited; ICDs cited; regulatory corpus | (a) bidirectional trace to a baselined expectation exists and is correct; (b) every `Assumes:` item is confirmed or has a closing action; (c) the requirement is essential to and consistent with the phase success criteria (Table G-4 or G-6); (d) interface values agree with the cited ICD (CK-REQ-C2); (e) every `Depends on:` item of a `safety`-tagged software requirement names existing hardware requirements and `OPS-NNN` actions (SWE-184); (f) every `regulatory` requirement agrees with the cited paragraph of the corpus file (the regulator group); (g) every `Fault tolerance:` item names a real item of `docs/safety/hazard-analysis.md` section 8 |
| V4 | Are the requirements feasible? | Reviewer | Budgets and simulations in `docs/research/` and `docs/design/`, `docs/plan/tpm.json` margins, BOM availability, vendor capabilities | Each performance value has a supporting analysis or heritage reference showing it is achievable with the constrained technology (SI-007 Pico 2; SI-031 and CON-014 kit assembly model; SI-028 stocked parts); TPM margin is not negative |
| V5 | Are the requirements verifiable? | Reviewer, test-author agent consulted | Section 4.4 table; the instrument set of 04 section 6 (charter section 9, CON-016) | Method assigned; the drafted closing case (section 4.1 step 7) has a closing type allowed for the requirement's module and can be run with pass/fail criteria at the level at which the requirement is stated (App. C C.4 Verifiability); a `regulatory` requirement is Test on the Bench unless a class 1 item (g) trade decided by Robin says otherwise (06 section 14.1); instrument gaps are named per 04 section 6.2 and covered by Analysis |
| V6 | Are the requirements redundant or over-specified? | Reviewer | Whole module file plus parent file; `docs/design/allocation.json` (preliminary at SRR) | No two requirements verify the same outcome; duplication between levels resolved with the level kept recorded (SE HB §6.2.1.2.3); at SRR every T-18 Warning (SYS requirement with no receiving L2 module) is confirmed or corrected; for every requirement the answer to "what is the worst that happens if it is omitted" is recorded when the necessity is not obvious; tolerances are defendable (App. C C.4 Correctness) |

SRR readiness demonstrations (SE HB §4.2.1.2.4, the five items the team is prepared to show), with the artifact that shows each:

| Demonstration | Artifact |
|---|---|
| Requirements are complete and understandable | Section 2.4 coverage table filled in the SRR package; validation records with zero open Major RIDs |
| Evaluation criteria are consistent with requirements, operations and logistics concepts | `expectations.json` MOEs with `ops_ids`; the validation path of every L1 requirement (section 2.3); App. E validation matrix generated by the tool (section 7) |
| Requirements and MOEs are consistent with stakeholder needs | V2 records confirmed by Robin in the decision memo, naming the stakeholder groups of section 3.0 |
| Operations and architecture concepts support NGOs, assumptions, guidelines and constraints | `conops.md`; `docs/design/architecture.md` (preliminary at SRR); preliminary `docs/design/allocation.json`; external ICD stubs (section 3.5) |
| The process for managing change in requirements is established, recorded and communicated | This document, sections 8.6, 8.7 and 10, with 05 section 5; Table G-4 success criterion 3 |

---

## 6. MOEs, MOPs, TPMs and KDRs

### 6.1 Definitions applied on cwht

| Measure | Definition (SE HB §4.1.1.2.6, §4.2.1.2.3, §4.2.1.2.5; NPR 7123.1D App. A) | Owner's view or supplier's view |
|---|---|---|
| MOE | Measure by which the owner judges satisfaction; critical to acceptability and to use; typically qualitative and not a design-to value | Owner |
| MOP | Quantitative measure that, when met by the design, helps ensure an MOE is satisfied; typically several per MOE | Supplier (Claude) |
| TPM | Physical or functional characteristic associated with or established from the MOPs and deemed critical, monitored during implementation by comparing the current estimate with the value anticipated at that time | Supplier, reported to owner at every review |
| KDR | Requirement that can have a large impact on cost or schedule when implemented. SE HB §4.2.1.2.3: "A KDR can have any priority or criticality." On cwht a KDR can have any criticality; its priority is restricted by the customization of section 6.4 | Both |

### 6.2 Recording

The owning artifacts are `docs/plan/semp.md` sections 5.16 (technical assessment) and 7.4 (TPMs, which names `mops[]` as the source TPMs are selected from) and the data file `docs/plan/tpm.json`. State on 2026-09-25 (read at 18:10): `mops[]` holds MOP-001 to MOP-020 and `tpms[]` holds TPM-001 to TPM-017. Every performance TPM names the MOP it is selected from in `mop_id`; the process leading indicators TPM-003 (review trend), TPM-009 (PCB area) and TPM-012 (requirements volatility) carry `mop_id: null` with a `mop_note`, by the rule of the file's `conventions.mop_rule`. Each of MOE-001 to MOE-012 is named by at least one MOP. The `requirement_ids` and `tc_ids` of the MOPs are empty until the L1 and L2 requirements and cases that carry them are written; the author fills them in the commit that adds the requirement or case.

| Measure | File and fields | Created | Baselined | Linked from requirements by |
|---|---|---|---|---|
| MOE | `expectations.json` `moes[]`: `id`, `statement`, `success_criterion`, `ngo_ids`, `ops_ids`, `source_ids`, `status` | Pre-SRR with the NGOs | SRR | `source_ids` |
| MOP | `docs/plan/tpm.json` `mops[]`: `id` (MOP-NNN), `title`, `moe_ids` (at least one), `requirement_ids` (the requirements that carry the value), `unit`, `threshold` (minimum acceptable), `target`, `tc_ids`, plus `tpm_ids` and `note` | Preliminary at SRR (exists) | PDR | `mop_ids` |
| TPM | `docs/plan/tpm.json` `tpms[]`: `id` (TPM-NNN), `key`, `name`, `definition`, `units`, `formula`, `planned_value`, `margin_policy`, thresholds, `measurement_method`, `history[]`, `mop_id` (null for the process leading indicators, with `mop_note`), fields as the file's `conventions` block defines them | Preliminary at SRR (exists) | PDR | `mop_ids` |
| KDR | `priority: "KDR"` on the requirement; rationale item `KDR:` names the driver | With the requirement | With its level | n/a; the tool lists all KDRs in the report (planned section, section 8.5) |

Selection rules: every MOE has at least one MOP by PDR (T-20); every KDR has at least one MOP or TPM in `mop_ids` by PDR (T-16); the TPM set includes at minimum carrier power, receiver sensitivity, DC current key-down and receive, battery endurance, mass, enclosure envelope, spurious-emission margin to 47 CFR 97.307, firmware flash and RAM use, keyer timing, safety-critical coverage (charter section 10), RFA/RID open counts (charter section 4) and requirements volatility (section 10.4). The `tpm.json` schema is owned by the SEMP; the fields above are the minimum this process needs.

### 6.3 Use in reviews

Every review package (charter section 4) plots each TPM's current best estimate against its planned value and thresholds. A TPM whose estimate falls outside the expected band triggers either a CR (section 10) or a risk entry `RSK-NNN` before the review closes. TPM results are an input to requirements management (SE HB §6.2.1.1).

### 6.4 Priority

`priority` is one of `KDR`, `Baseline`, `Goal`. `KDR` and `Baseline` are both mandatory requirements; `KDR` additionally flags the cost or schedule driver. `Goal` marks a desired capability written as `shall` in `description` (schema rule) with `should` in the rationale; a `Goal` requirement is verified like any other, and one found not met is dispositioned by the waiver path of section 8.7 like any unmet requirement.

**Customization (deviation from SE HB §4.2.1.2.3).** SE HB keeps KDR status independent of priority. The single-valued `priority` field of `docs/requirements/schema.json` merges the two, so on cwht a KDR cannot also be a `Goal`: if a desired capability drives cost or schedule, Robin either promotes it to `Baseline` or retires it. Rationale: with one approver and a build of at most five units, a cost or schedule driver is either committed to knowingly or not spent on at all, and an optional capability that drives the BOM or the vendor lead time is the case that choice exists to prevent. Criticality stays independent of the field (tag `safety` and `hazard_ids`), so a KDR can have any criticality, as SE HB states. The customization is recorded here and is to be listed with the SEMP customizations (charter section 1; section 14, AL-02-26). Restoring the SE HB model (a boolean `kdr` field beside `priority`) is a schema CR that Robin may direct at any review; Claude then drafts it for the next gate.

---

## 7. Traceability model (NPR 7150.2D §3.12.1 Table 1, Class A, all six relationships)

Class A requires all six relationships (SWE-052). The charter applies the same model to hardware modules, with schematic sheets and CAD in place of code. Each link is stored once, in the direction of the arrow, in the field named below; the reverse direction is derived and published by `tools/traceability.py` in the matrices, and where a second file also stores the link the tool checks that the two agree.

| # | Table 1 relationship (text of the Table) | Stored in (forward) | Reverse or cross-check | Rules |
|---|---|---|---|---|
| 1 | Higher-level requirements to the software requirements | `parent_id` in `docs/requirements/sw/**/requirements.json` naming the `REQ-SYS-NNN`, `REQ-SW-NNN` or hardware L2 id; `source_ids` for L0 expectations and scenarios | `child_ids` in the parent (must equal the set of children when present); generated requirements tree in `docs/vv/traceability-report.md` (planned section) | T-05, T-06, T-07, T-18 |
| 2 | Software requirements to the system hazards | `hazard_ids` (`HZ-NNN`) on the requirement; tag `safety`; on a `safety`-tagged software requirement, the rationale item `Depends on:` naming the hardware requirements and `OPS-NNN` operator actions the control relies on (SWE-184). The Note under §3.12.1 extends this trace to "hazardous controls, hazardous mitigations, hazardous conditions, and hazardous events" | `docs/safety/hazards.json` (schema `docs/safety/schema.json`): each hazard's `controls[].control_req_ids` names the requirements implementing that control (charter section 7), and the hazard-level `requirement_ids` is their union; the tool checks that the union is exact and that both agree with `hazard_ids` | T-08 |
| 3 | Software requirements to the software design components | `design_refs`, the authoritative link: an element id listed in `docs/design/allocation.json`, an ICD id `ICD-<A>-<B>`, a schematic sheet path `hardware/kicad/<board>/<sheet>.kicad_sch`, a Rust unit path `firmware/<crate>/src/<module>/<unit>.rs` (07 section 3.5 workspace layout), or a reused-component path `rustos:<path>` (section 2.3) | `docs/design/allocation.json` element records `requirement_ids`, the derived cross-check that the tool compares with `design_refs`; ICD section 4 lists the requirements of each side | T-15, T-22 |
| 4 | Software design components to the software code | Rust module path in `design_refs` exists; each function that implements a requirement carries `// @req REQ-SW-KEYER-001[, ...]` on the line above it and each design unit carries `// @design <module>/<unit>` (07 coding standard CS-24); `allocation.json` element lists `code` paths | The tool scans `firmware/**/*.rs` for `@req` and `@design` tags, checks each id resolves, and checks each `design_refs` Rust path contains at least one `@req` tag naming the requirement | T-15 |
| 5 | Software requirements to the software verification(s) | `requirement_ids` in `docs/test_cases/<module>/test_cases.json`; `automation_ref` names the `cargo test` target, emulator scenario or script; test functions and emulation scenario entry points carry `// @verify REQ-SW-KEYER-001[, ...]` (CS-24); test reports `docs/vv/reports/<TC-ID>-r<N>.md` carry `requirement_ids` in their front matter (04 section 9) | App. D verification matrix, a section of `docs/vv/traceability-report.md` generated per requirement (04 section 7.1); `TC-` tokens in `firmware/` checked to resolve | T-09, T-10, T-11 |
| 6 | Software requirements to the software non-conformances | `docs/vv/ncr/NCR-NNN.md` front matter fields `requirement_ids` and `test_case_ids` (04 section 10) | Report section "Nonconformance traceability"; a requirement with an NCR whose status is not `Closed` cannot be `Verified` | T-11 |

**Field contracts of other processes' files.** The `hazards.json` fields of row 2 are fixed by `docs/safety/schema.json` (`controls[].control_req_ids` per control, `requirement_ids` per hazard as the union) and by charter section 7. The `allocation.json` fields `requirement_ids` and `code` (rows 3 and 4) are proposed by this process as inputs to that product and are confirmed by the architecture ADR (PDR); a different field name chosen there is followed by a same-commit change to this table and to the tool. `design_refs` stays the authoritative link either way: `allocation.json` is regenerated from it or corrected to it, never the reverse.

**Validation trace (SE HB App. E; charter section 9).** The validation matrix is built as 04 section 7.2 defines it: one row per `OPS-NNN` and per `MOE-NNN`, filled from the `TC-VAL-NNN` cases (`docs/test_cases/val/test_cases.json`) whose `setup` names the row's id after `Validates:`, with the cases' `requirement_ids` as the requirements exercised. The requirements-side contribution is the validation path of section 2.3: every MOE carries `ops_ids` and every L1 requirement cites at least one `OPS-` or `MOE-` id in `source_ids` (T-07, T-20), so that a failed validation row leads to the requirements that need a CR. The tool publishes the matrix as section 4 of `docs/vv/traceability-report.md`.

---

## 8. Rules enforced by `tools/traceability.py`

### 8.1 Invocation and outputs

The tool exists and runs today; section 8.5 states rule by rule what it enforces. Invocation (verified 2026-09-25 with `--help`):

```
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py [--root PATH] [--output PATH] [--json PATH] [--report-only] [--quiet] [--render]
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --regression DESIGN_REF [DESIGN_REF ...]
```

| Option | Behavior | Exit code |
|---|---|---|
| (none) | Loads every input below, runs every check of the catalogue (report section 11), writes `docs/vv/traceability-report.md` and `docs/vv/traceability.json` | 0 no violations, 1 violations, 2 usage error |
| `--output PATH` | Report path, relative to the root unless absolute; the JSON is written beside it as `traceability.json` unless `--json` names another path | as above |
| `--json PATH` | Machine-readable output path (counts, coverage by module, the MSR-01, MSR-03, MSR-04 and MSR-23 measurements of 07 section 11, validation rows, findings) | as above |
| `--report-only` | Writes the outputs and exits 0 even with violations (drafting runs only, section 4.1 step 8) | 0 |
| `--quiet` | Prints violations only | as above |
| `--render` | First writes `expectations.md` beside `expectations.json` and `requirements.md` beside each `requirements.json` (generated, never hand-edited; charter section 5 lists the rendered `.md`), then runs the checks | as above |
| `--regression DESIGN_REF ...` | Prints the hardware regression set of 04 section 10.5 and exits; no report | 0 |

A plain run rewrites `docs/vv/traceability-report.md` and `docs/vv/traceability.json`, and `--render` rewrites the rendered `.md` files. A reviewer or agent that needs no repository change passes `--output` (and, if wanted, `--json`) with a path under its scratchpad directory.

The tool's known-answer tests run with `/Users/robinonsay/rust/cwht/.venv/bin/python -m unittest discover -s /Users/robinonsay/rust/cwht/tools/tests` on the seeded fixtures `tools/tests/fixtures/valid_project` (exit 0, zero findings) and `tools/tests/fixtures/invalid_project` (exit 1, one seeded defect per check code); this is the SWE-136 known-answer test of 05 section 9.2.

Planned options (owner Claude as software lead; each is a tool task with the gate by which its unit test passes on the fixtures under `tools/tests/fixtures/`):

| Planned option | Purpose | Due |
|---|---|---|
| `--gate <SRR\|PDR\|CDR\|TRR\|SAR>` | Entrance mode: applies the `gate` column of section 8.2; a rule marked `E@<R>` is a violation at gate `<R>` and every later gate. Until this option exists, the reviewer applies the `gate` column by hand to the report's Warnings at the readiness declaration (01 section 3.1) | PDR |
| `--volatility --from <tag> [--to <ref>]` | Computes the SWE-200 metric of section 10.4 and appends it as `MSR-02` to `docs/plan/measurements.json` | PDR (first interval after `baseline/srr`) |
| `--fix-children` | Regenerates every `child_ids` list from `parent_id` (authors maintain `child_ids` by hand until then; T-06 catches mismatches) | PDR |

Inputs read today: every `docs/requirements/**/requirements.json` (files under `docs/templates/` are never read), `expectations.json`, `stakeholder-inputs.md`, `docs/conops/conops.md`, `docs/test_cases/**/test_cases.json`, `docs/safety/hazards.json`, `docs/risk/register.json`, `docs/plan/tpm.json`, `docs/references/md/regulatory/`, `docs/decisions/adr/`, `docs/decisions/trade-studies/`, the table rows of `docs/icd/ICD-*.md` (TBD check), `docs/vv/ncr/*.md`, `docs/vv/reports/TC-*-r*.md`, and the existence of `docs/reviews/SAR/decision-memo.md`. Inputs added with the planned rules: `docs/design/allocation.json` (T-15, T-18), ICD names and section 4 (T-22), `firmware/**/*.rs` (T-15), `firmware/releases/VDD-*.md` and `docs/vv/adp/*/as-built.md` (T-11), the waiver dispositions of CRs and decision memos (T-11 waivers), `docs/cm/cr/CR-*.md` and git (`baseline/*` tags, commit subjects and trailers) (T-04, T-12, T-13).

Outputs: `docs/vv/traceability-report.md` with sections 1 summary (counts, upstream artifacts consulted), 2 findings (`code | location | message`, violations then warnings), 3 requirements verification matrix (App. D, 04 section 7.1), 4 validation matrix (App. E, 04 section 7.2), 5 orphan requirements, 6 orphan test cases, 7 parent coverage, 8 per-module coverage, 9 hazard traceability, 10 nonconformance traceability, 11 checks performed (the tool's check catalogue); and `docs/vv/traceability.json`. Planned report sections: requirements tree, KDR list, open TBR list, retired entries, changes since baseline (CR-covered, Class II, editorial), ICD pairing table, stakeholders (section 8.5). At package build the per-review report `docs/reviews/<REVIEW>/traceability-report.md` and its data file `docs/reviews/<REVIEW>/traceability.json` are written by the 01 section 3.1 item 2 command (`tools/traceability.py --output docs/reviews/<REVIEW>/traceability-report.md`, which writes the JSON beside the report; 01 section 13); nothing is copied from `docs/vv/`. The report with zero violations is an entrance product of every review (charter section 7).

Section 8.2 lists the requirements-side rules. `docs/process/04-verification-and-validation.md` section 7.3 lists the evidence-side rules (report front matter, credit, NCR closure, hazard-control verification); the tool implements both lists in one findings table and both documents carry an implementation-status table (04 section 7.4; section 8.5 here).

### 8.2 Rule list

Severity: E = Error (violation, blocks), W = Warning (listed), "E@PDR" = Warning until the PDR gate, Error at PDR and later gates. The `check` column is the behavior of a plain run; the `gate` column is the behavior of `--gate` (applied by hand until the option exists, section 8.1).

| Rule | Statement | `check` | `gate` |
|---|---|---|---|
| T-01 Schema | Every requirements file validates against `docs/requirements/schema.json`; `expectations.json` against `l0-stakeholder/schema.json` (including the `stakeholders` array once `baseline` is set); every test file against `docs/test_cases/schema.json`; `hazards.json` and `register.json` against their schemas. | E | E |
| T-02 Path agreement | `module` of `docs/requirements/<dir>/requirements.json` and of `docs/test_cases/<dir>/test_cases.json` equals `upper(<dir>)` where `<dir>` is the immediate parent directory (`sys`, `sw`, `sw-keyer`), no two files declare the same module, and every `id` starts with `REQ-<module>-` or `TC-<module>-`. | E | E |
| T-03 Uniqueness | All `REQ-` ids across all requirement files are unique; all `TC-` ids across all test files are unique; all `NGO-`, `MOE-`, `CON-` ids and all stakeholder `name` values in `expectations.json` are unique. | E | E |
| T-04 Baseline persistence | Every `REQ-`, `TC-`, `NGO-`, `MOE-`, `CON-` id and stakeholder `name` present in the most recent `baseline/*` tag exists in the working tree (retire, never delete). Skipped when no baseline tag exists. | E | E |
| T-05 Parent | `parent_id`, when non-null, resolves to an existing `REQ-` id, is not the requirement itself, forms no cycle, and is a `SYS` id or an L2 id; `SYS` requirements have `parent_id` null. `parent_id` null on a non-`SYS` requirement requires `rationale` starting `Self-derived:` and (`source_ids` containing an `ADR-` or `TS-` id, or `hazard_ids` non-empty). | E | E |
| T-06 Children | When `child_ids` is present it equals the set of requirements whose `parent_id` is this id. | E | E |
| T-07 Sources and source tags | Every `source_ids` entry matches a form in section 3.4 and resolves per that table: `SI-` to a row of `stakeholder-inputs.md`, `NGO-`/`MOE-`/`CON-` to `expectations.json`, `OPS-` to a `conops.md` heading, `ADR-`/`TS-` to a file, `47CFR<part>.<section>` (Parts 1, 2, 15, 97) to `docs/references/md/regulatory/47cfr-<part>.<section>.md` or `47cfr-<part>.<section>-<slug>.md`. `SYS` requirements have at least one entry; once `expectations.json` exists, at least one `NGO-`, `MOE-`, `CON-` or `OPS-` entry, and at least one `OPS-` or `MOE-` entry (validation path, section 2.3). Tag `regulatory` implies a 47 CFR clause of Part 1, 2, 15 or 97; tag `security` implies a `CON-` or `ADR-` entry. | W (missing file; validation path; security source) / E (unresolved id in an existing file or corpus; no L0 source; regulatory tag) | E |
| T-08 Hazards | Every `hazard_ids` entry resolves to `docs/safety/hazards.json`; tag `safety` implies at least one hazard id; every `control_req_ids` entry of every control and every hazard-level `requirement_ids` entry resolves to an existing requirement that lists the hazard; each hazard's `requirement_ids` equals the union of its controls' `control_req_ids` (charter section 7; `docs/safety/schema.json`); a hazard requirement has a closing case of method Test (04 section 7.3 rule 6). | W (file absent, or sets disagree) / E (unresolved, untested) | E |
| T-09 Coverage | Every requirement with status `Draft` or `Active` is cited by at least one test case and has at least one closing case: same `verification_method` and a closing type of section 4.4 for the requirement's module (04 section 7.3 rule 2). Before SRR this means a `Draft` closing case for every L1 requirement (section 4.1 step 7). | E | E |
| T-10 Test citations | Every `requirement_ids` entry in every test case resolves to an existing requirement that is not retired (section 11.3: status `Closed` with tag `retired`), unless the case is itself retired; the test `type` is an evidence class of its `verification_method` (Test: `HostUnit`, `Emulation`, `Bench`; Demonstration: `Emulation`, `Bench`, `OnAir`; Analysis: `Simulation`; Inspection: `Inspection`); a `HostUnit` or `Emulation` case closes only `SW` and `SW-<SUB>` requirements and is supporting for a requirement of any other module, and an `Emulation` case never closes a Demonstration (section 4.4; 04 section 5.2). A case may cite requirements of any module. | E | E |
| T-11 Status consistency | `Verified` requires every closing `TC` to be `Passed` with a report in `docs/vv/reports/` whose front matter has `credit: true` and `result: Pass` (04 section 9), no citing `TC` with status `Failed`, and no NCR with status other than `Closed` citing the requirement; for a `SW` or `SW-<SUB>` requirement, the credited report's `firmware_version` names a tagged release with a version description `firmware/releases/VDD-<version>.md`. `Closed` without the tag `retired` requires the SAR decision memo and the dependent validation rows `Validated` (04 section 5.3); for a `SW` or `SW-<SUB>` requirement closed by `HostUnit` or `Emulation` it also requires the PCA-05 line of `docs/vv/adp/CWHT-A-NNN/as-built.md` to name the release of the credited report (charter section 9). `Closed` is reached from `Verified`, or from `Active` with the tag `waived` and an approved product waiver (section 8.7). `Closed` with the tag `retired` is retirement (T-19). A child with status `Active` or later requires its parent not `Draft`. A `TC` with status `Passed` or `Failed` requires a report naming it. | E (report missing: W) | E |
| T-12 Transitions | Each requirement's, test case's and L0 entry's status change relative to the most recent baseline tag is an allowed transition of section 8.3 or 8.4. | E | E |
| T-13 Change control | After the level's baseline tag, any Class I or Class II difference (section 10.2) between a requirement in the working tree and its baselined version is covered by an approved `CR-NNN` in `docs/cm/cr/` that lists the id. A difference confined to the editorial fields of section 10.2 is accepted when every commit that touched the entry since the baseline has commit type `editorial` or an `Editorial:` trailer (05 section 4.5) and is listed in the report's editorial log. | E | E |
| T-14 TBD/TBR | The token `TBD` appears in no requirement, expectation, ICD or test file. `(TBR)` in `description` if and only if `tbr` is present. `tbr.close_by` is within the level limit (L1: `SRR` or `PDR`; L2: through `CDR`). A `tbr` object is admitted on any status except `Verified` and `Closed` (a retired requirement is `Closed`, section 11.3; an Active L1 TBR closes by PDR, charter section 7). At `gate R`, any `tbr.close_by` equal to or earlier than `R` is an Error. | E | E |
| T-15 Design and code | Every `design_refs` entry resolves: an element id in `docs/design/allocation.json`, an ICD id with a file `docs/icd/ICD-<A>-<B>.md`, an existing `.kicad_sch` path, an existing `.rs` path, or a `rustos:<path>` in the rustos checkout at the commit of `tools/toolchain.lock.md` section 3. `allocation.json` `requirement_ids` agree with `design_refs` (which is authoritative, section 7). Tag `reused` implies a component path in `design_refs`. Every id in an `@req`, `@verify` or `@design` tag in `firmware/**/*.rs` resolves. Every Active L2 requirement has at least one `design_refs` entry from PDR; every Rust path in `design_refs` contains an `@req` tag naming the requirement from CDR; every Active `REQ-SW-*` has at least one `@req` and one `@verify` tag at release (07 gate G4). | W | E@PDR; E@CDR (`@req` per path) |
| T-16 Measures | Every `mop_ids` entry resolves to an id in `docs/plan/tpm.json` `mops[]` or `tpms[]`; every `priority: KDR` requirement has at least one `mop_ids` entry from PDR. | W | E@PDR |
| T-17 Word lint | `description` contains exactly one `shall`, none of the WR-07 group A words (E) and none of the WR-07 group B words (W in check, E at gate); `title` contains no `shall`; `description` has at most 25 words (W). The tool's word list is a verbatim copy of WR-07. | E (shall, group A) / W (group B, length) | E (shall, groups A and B) / W (length) |
| T-18 Allocation | At SRR, every `Draft` or `Active` `SYS` requirement names at least one receiving L2 module through `child_ids` or a preliminary `docs/design/allocation.json` record (section 2.3); each gap is listed and the reviewer confirms or corrects it in V6. From PDR, every Active `SYS` requirement has at least one child or the tag `leaf` (SE-42). | W | W at SRR; E@PDR |
| T-19 Retirement | A retired requirement (section 11.3: status `Closed` and tag `retired` until a schema CR adds `Retired`) has a `rationale` starting `Retired by `, no child that is not itself retired, no citing test case that is not itself retired, no `tbr` object, and keeps its id (T-04); tag `retired` on any status other than `Closed` is an error. A retired test case (status `Blocked`, `setup` starting `Retired by `) cites only retired requirements or names its superseding case. Retired entries are excluded from T-09, T-18, the `Closed` rule of T-11 and the matrices, and are listed in their own report section. | E | E |
| T-20 L0 coverage | Every bold (core) `SI-` row is cited by at least one `SYS` requirement; every Baselined Objective is cited by at least one `SYS` requirement or MOE; every MOE has at least one `ops_ids` entry and, from PDR, at least one MOP in `mops[]` naming it; every `OPS-` heading is cited by at least one requirement or `TC-VAL` case. | W | E (core SI, Objective, OPS per MOE); E@PDR (MOP per MOE); W (OPS cited) |
| T-21 Expectations consistency | `expectations.json` has exactly one entry of kind `Need`; every Goal's `parent_id` is the Need; every Objective's `parent_id` is a Goal; every `ngo_ids` entry of every MOE resolves to a Goal or Objective; every `ops_ids` entry resolves to a heading in `conops.md` (W while the file is absent); every `retired_by` id matches the schema pattern; the `stakeholders` array exists with at least one entry of role `customer`, `user` and `regulator`, unique names and resolving `source_ids`. | E (W for absent `conops.md`; W for the stakeholders array before SRR) | E |
| T-22 ICD pairing | Every `docs/icd/ICD-<A>-<B>.md` has a name whose tokens and order follow section 3.5; is cited in `design_refs` by at least one `interface`-tagged requirement in the module file of `<A>` and, when `<B>` is a module, of `<B>` (for `<B>` = `SW`, any file under `docs/requirements/sw/`); every `interface`-tagged requirement cites at least one ICD id; the ICD's section 4 lists exactly the requirements that cite it. | W | E@PDR |

### 8.3 Requirement and L0 entry status transitions

| From | To | Trigger | Evidence checked by T-12 |
|---|---|---|---|
| (new) | `Draft` | Author creates the entry | Commit |
| `Draft` | `Active` | The requirement's level is baselined (L1 at SRR, L2 at PDR) by decision memo; or, after that baseline, an approved CR adds it | `docs/reviews/<REVIEW>/decision-memo.md` or the CR |
| `Active` | `Verified` | Every closing `TC` (section 4.4) `Passed` with a credited report (`credit: true`, `result: Pass`), no citing `TC` `Failed`, no NCR open against it; for a `SW` or `SW-<SUB>` requirement, the report names a tagged release that has a VDD (charter section 9) | Reports in `docs/vv/reports/` (04 section 9); `firmware/releases/VDD-<version>.md` |
| `Verified` | `Closed` | SAR decision memo accepts the product; dependent validation rows `Validated` and the other conditions of 04 section 5.3; for a `SW` or `SW-<SUB>` requirement closed by `HostUnit` or `Emulation`, the PCA-05 line of `docs/vv/adp/CWHT-A-NNN/as-built.md` names the release of the credited report (charter section 9) | SAR decision memo; validation matrix; `as-built.md` |
| `Active` | `Closed` with tag `waived` | SAR decision memo accepts the product with the product waiver of section 8.7 | Waiver CR disposition `Approved (waiver)` or memo item `W<n>`; CSA item 12; NCR `Use-as-is` |
| `Verified` | `Active` | NCR opened citing the requirement (regression) | `NCR-NNN` |
| `Active` | `Active` (text changed) | Approved CR | CR |
| `Draft`, `Active`, `Verified`, `Closed` | `Closed` with tag `retired` (retirement, section 11.3) | Before the level's baseline: author, with the rationale citing the `RID-<REVIEW>-NNN` or the `INSP-NNN` peer-review record whose finding motivated it. After the level's baseline: approved CR | CR, or the RID or INSP record |
| Forbidden | `Active` to `Draft`; `Verified` to `Draft`; `Closed` to anything except retirement; a retired requirement to anything (the tag is never removed); deletion of any entry | | |

L0 entries (`NGO-`, `MOE-`, `CON-` of `expectations.json`; the schema carries these statuses):

| From | To | Trigger | Evidence checked by T-12 |
|---|---|---|---|
| (new) | `Draft` | Author creates the entry | Commit |
| `Draft` | `Baselined` | SRR baseline flip (section 11.2): every `Draft` entry flips and `baseline` is set to `"baseline/srr"` in one commit citing the SRR decision memo | `docs/reviews/SRR/decision-memo.md` |
| `Draft` | `Retired` | Before SRR: author, with `retired_by` naming the `RID-SRR-NNN` or `INSP-NNN` whose finding motivated it | The RID or INSP record |
| `Baselined` | `Baselined` (text changed) | Approved CR | CR |
| `Baselined` | `Retired` | Approved CR named in `retired_by` | CR |
| Forbidden | `Baselined` to `Draft`; `Retired` to anything; deletion of any entry | | |

A change to the `stakeholders` array after SRR is a Class I change by CR (section 10.2); the array has no per-entry status.

### 8.4 Test case status transitions

| From | To | Trigger |
|---|---|---|
| (new) | `Draft` | Test-author agent creates the case citing existing requirements |
| `Draft` | `Active` | Independent reviewer passes the procedure checklist (SWE-087; 04 section 8.3); `Bench` and `OnAir` cases additionally require the TRR decision memo |
| `Active` | `Passed` or `Failed` | Execution; report filed in `docs/vv/reports/`; `Failed` opens an NCR |
| `Failed` | `Active` | NCR dispositioned and re-run scheduled |
| `Active` | `Blocked` | Prerequisite missing; the report names it |
| `Blocked` | `Active` | Prerequisite met |
| any not retired | `Blocked` with `setup` starting `Retired by ` (retirement, section 11.3; the test schema has no `Closed` status and no `tags`, so this is the interim marker until a schema CR adds `Retired`) | The requirements it cites are retired, or the case is superseded; the reason `Retired by CR-NNN (or, before the citing level's baseline, RID-<REVIEW>-NNN or INSP-NNN): <reason>; superseded by TC-...` is the first sentence of `setup`; reports already filed stay in `docs/vv/reports/` |
| Forbidden | a retired case to anything; deletion of any entry | |

### 8.5 Implementation status (charter rule 11.2: evidence, not assertion)

Verified on 2026-09-25 between 17:57 and 18:26 by reading `tools/traceability.py` (catalogue `CHECK_CATALOGUE`, printed as report section 11), running `--help`, running the tool on the repository with `--output` and `--json` under the scratchpad (148 `Draft` SYS requirements and no test case present: exit 1 with 148 `REQ_UNVERIFIED` and 69 `HAZARD_REQ_NOT_TESTED` violations, which section 4.1 step 7 clears), running it on a scratch root holding `docs/templates/requirements.example.json` as the SYS file (no finding on the three requirements except the expected `HAZARD_INVERSE` warning while `hazards.json` does not yet list REQ-SYS-003), and running `/Users/robinonsay/rust/cwht/.venv/bin/python -m unittest discover -s /Users/robinonsay/rust/cwht/tools/tests` (see the evidence line below the table). The tool has one mode plus `--render` and `--regression` and the check codes of its catalogue; it has no T-rule ids. This table binds each T-rule to the codes that implement it today and names the task, owner (Claude as software lead in every row) and gate for the rest. A gate's readiness declaration is blocked until every row due at that gate has a passing unit test on the seeded fixtures (04 section 7.4; `tools/toolchain.lock.md` section 1.1). `docs/process/03-software-classification-and-rmm.md` section 8 names the same planned codes for the SWE-052 rows.

| Rule | Implemented today | Tool codes today | Remaining task (planned code) | Due |
|---|---|---|---|---|
| T-01 | yes | `SCHEMA_MISSING`, `SCHEMA_INVALID` (same check as `tools/validate_docs.py`, including `register.json`) | none | done |
| T-02 | yes | `MODULE_MISMATCH`, `MODULE_DUPLICATE`, `ID_FORMAT` | none | done |
| T-03 | yes, except stakeholders | `ID_DUPLICATE` (REQ, TC, NCR across and within files; NGO, MOE, CON within `expectations.json`) | stakeholder `name` uniqueness (with `STAKEHOLDERS_MISSING`, T-21) | before SRR |
| T-04 | no | none (git is not read) | `BASELINE_ID_MISSING` | PDR (first check after `baseline/srr`) |
| T-05 | yes | `L1_PARENT_NOT_NULL`, `PARENT_UNRESOLVED`, `PARENT_CYCLE`, `PARENT_MISSING`, `SELF_DERIVED_UNSUPPORTED` | none | done |
| T-06 | yes | `CHILD_INVERSE` (both directions) | none; `--fix-children` (section 8.1) is a convenience | done |
| T-07 | yes, except two new rules | `SOURCE_UNRESOLVED` (every form of section 3.4, including `CON-` and 47 CFR Parts 1, 2, 15 and 97 with the `-<slug>` extract form; `47CFR2.106` resolves to `47cfr-2.106-harmonic-bands.md`), `SOURCE_FILE_MISSING`, `SOURCE_FORMAT_UNKNOWN`, `SOURCE_L0_MISSING`, `REGULATORY_TAG_NO_CLAUSE` (Parts 1, 2, 15, 97) | Validation path, at least one `OPS-` or `MOE-` source on a SYS requirement (`SYS_NO_VALIDATION_PATH`); `security` tag source (`SECURITY_TAG_NO_SOURCE`) | before SRR |
| T-08 | yes, except promotion | `HAZARD_ID_FORMAT`, `HAZARD_UNRESOLVED` (hazard ids, `requirement_ids` and each control's `control_req_ids`), `HAZARD_FILE_MISSING`, `HAZARD_INVERSE` (warning; includes the union check), `SAFETY_TAG_NO_HAZARD`, `HAZARD_REQ_NOT_TESTED` (04 rule 7.3.6), `RISK_FILE_MISSING` | `HAZARD_INVERSE` becomes a violation under `--gate PDR` (03 section 8) | PDR |
| T-09 | yes, except module rule | `REQ_UNVERIFIED`, `REQ_NO_CLOSING_CASE` (closing = same method) | Closing-case selection by module of section 4.4: for `SYS`, `RX`, `TX`, `PWR`, `CTL` and `ME`, a same-method `HostUnit` or `Emulation` case, and for Demonstration an `Emulation` case in any module, is supporting, so `REQ_NO_CLOSING_CASE` fires when no other closing case exists (with T-10) | before SRR |
| T-10 | yes, except module rule | `TC_REQ_UNRESOLVED`, `TC_TYPE_METHOD` (type versus method), retired citations through `RETIRED_INCONSISTENT` (a retired requirement cited by a live case) | Extend `TC_TYPE_METHOD` with the module rule: reported on a `HostUnit` or `Emulation` case that is the only same-method case of a non-software requirement it cites | before SRR |
| T-11 | partly | `VERIFIED_WITHOUT_EVIDENCE`, `VERIFIED_WITH_OPEN_NCR`, `CLOSED_WITHOUT_SAR` (SAR memo and dependent validation rows), `CHILD_AHEAD_OF_PARENT`, `TC_STATUS_EVIDENCE`, `FAILED_TC_WITHOUT_NCR` (W), `REPORTS_DIR_MISSING` (W), `REPORT_FRONT_MATTER`, `REPORT_ID_FORMAT`, `REPORT_UNRESOLVED`, `REPORT_ARTIFACT`, `NCR_FRONT_MATTER`, `NCR_ID_FORMAT`, `NCR_UNRESOLVED`, `NCR_ARTIFACT` | Software `Verified` needs a report release with a VDD (`REPORT_RELEASE_UNRESOLVED`); software `Closed` needs the PCA-05 release to equal the credited release (`CLOSED_NOT_INSTALLED`, the single code name used by 04 section 7.4, 05 and `tools/README.md`); `Closed` with tag `waived` needs an approved product waiver naming the requirement and is exempt from the evidence rule (`WAIVER_UNRECORDED`) | CDR (before the first credit report, 04 section 16) |
| T-12 | no | none | Status diff against the most recent `baseline/*` tag for requirements, cases and L0 entries (`TRANSITION_FORBIDDEN`), memo, RID, INSP and CR existence | PDR |
| T-13 | no | none | Field diff against the baseline tag classified per section 10.2; CR lookup in `docs/cm/cr/`; editorial log from commit types and `Editorial:` trailers (`CHANGE_UNCOVERED`) | PDR |
| T-14 | yes (plain run) | `TBD_PRESENT` (requirement and case text, expectations, ICD table rows), `TBR_UNDOCUMENTED`, `TBR_UNMARKED`, `TBR_ON_FINAL_STATUS`, `TBR_CLOSE_BY` | the gate rule (`close_by` at or before the gate) comes with `--gate` | PDR |
| T-15 | no | none (`design_refs` is read into the data model; the only check that reads it today is `INTERFACE_TAG_NO_ICD`, T-22) | `DESIGN_REF_UNRESOLVED`, `DESIGN_REF_MISSING`, `DESIGN_ELEMENT_ORPHAN` (03 section 8 names) with ICD ids, `.kicad_sch` and `rustos:` paths; `REUSED_TAG_NO_REF`; `@req`/`@verify`/`@design` scan of `firmware/**/*.rs` (`TAG_UNRESOLVED`, `REQ_UNTAGGED`) | PDR (allocation, ICD, sheets, reused); CDR (tags) |
| T-16 | yes, except KDR rule | `MOP_UNRESOLVED` (W), `SOURCE_FORMAT_UNKNOWN` for a malformed measure id, `SOURCE_FILE_MISSING` while `tpm.json` is absent | `KDR_WITHOUT_MOP` | PDR |
| T-17 | yes (`check` severities) | `SHALL_COUNT`, `MODAL_IN_DESCRIPTION`, `SHALL_IN_TITLE`, `DESCRIPTION_LENGTH` (W), `UNVERIFIABLE_WORD` (W); both word lists are a verbatim copy of WR-07 | group B hits become E under `--gate` | PDR |
| T-18 | no | none | `SYS_UNALLOCATED`, reading `child_ids` and the preliminary `allocation.json`: W at SRR, E from PDR | before SRR (W listing); PDR (E) |
| T-19 | yes, except report section | `RETIRED_INCONSISTENT` (requirement: `Retired by ` prefix, live child, live citing case, tag on a wrong status; test case: status `Blocked` with `setup` beginning `Retired by ` recognized as retired, superseding case named and existing); `TBR_ON_FINAL_STATUS` for a `tbr` on a retired requirement; retired entries excluded from coverage and the matrices | A report section listing retired entries | PDR |
| T-20 | yes (`check` severities) | `CORE_SI_UNCOVERED`, `OBJECTIVE_UNCOVERED`, `MOE_WITHOUT_OPS`, `OPS_UNCITED` (all W) | gate severities with `--gate`; `MOE_WITHOUT_MOP` from PDR | PDR |
| T-21 | yes, except stakeholders | `EXPECTATIONS_INCONSISTENT` (Need count, parent kinds, `ngo_ids`, `ops_ids`); `retired_by` pattern by T-01 | `STAKEHOLDERS_MISSING` (array absent, required roles missing, names not unique, sources unresolved); stakeholders rendered by `--render` | before SRR |
| T-22 | partly | `INTERFACE_TAG_NO_ICD` (W) | `ICD_NAME`, `ICD_UNPAIRED`, `ICD_SECTION4_MISMATCH` | PDR |
| Options and outputs | partly | `--render` with `RENDER_STALE` (W); `--json` and `docs/vv/traceability.json`; report sections 1 to 11 of section 8.1 | `--gate`, `--volatility`, `--fix-children`; report sections requirements tree, KDR list, open TBR list, retired entries, changes since baseline, ICD pairing table, stakeholders | PDR |

Evidence line (unit tests): at 17:57 the suite ran 107 tests with 1 failure (`test_validate_docs.InvalidProjectTests.test_exactly_the_seeded_documents_fail`, whose expected-failure set had not yet been updated for the review-record documents seeded into `tools/tests/fixtures/invalid_project`); at 18:14 it ran 167 tests and at 18:26 194 tests, both with 0 failures, after the tool author's concurrent update of `tools/validate_docs.py`, the tests and the fixtures (`tools/traceability.py` last modified 18:09). The fix for that failure belongs to the author of `tools/validate_docs.py` and `tools/tests/` (Claude as software lead, `tools/README.md`). Re-observed by the integrating session on 2026-09-25 at 19:36: `tools/validate_docs.py` 10 passed, 0 failed; the suite ran 258 tests, OK; `tools/traceability.py --report-only` on the repository reported 179 requirements, 0 test cases and 255 violations (177 `REQ_UNVERIFIED`, 78 `HAZARD_REQ_NOT_TESTED`) and 0 warnings, which the SRR test-case set of section 4.1 step 7 clears. The next readiness declaration re-runs the suite and records its count in the package.

### 8.6 Inconsistency handling (SWE-054)

SWE-054 requires inconsistencies among requirements, project plans and software products to be identified, corrected and tracked until closure. Each kind of inconsistency has one record and one owner:

| Found as | Record | Owner and closure |
|---|---|---|
| A tool violation (section 8.2) on an item not yet baselined | The commit that ends the draft clears it (section 4.1 step 8) | The author; no separate record |
| A tool violation or reviewer finding on a baselined item outside a review | `NCR-NNN` in `docs/vv/ncr/` (04 section 10) with the requirement ids in `requirement_ids`; the disposition is a CR when the fix changes a baselined item | Claude opens it the day it is found; closes per 04 section 10.6 |
| A finding raised during a review | `RID-<REVIEW>-NNN` in `docs/reviews/<REVIEW>/rfa-rid-log.json` (charter section 4) | Assignee named in the log; closure evidence verified by an independent reviewer (01 section 10.5) |
| A disagreement between process documents, templates or plans (for example the items of section 14) | An alignment item in `docs/process/05-configuration-and-data-management.md` section 14.1, or in the raising document's section 14 with a document prefix (`AL-02-NN` here), naming the owning author, the edit, the due gate and, once made, the commit | The owning document's author makes the edit; the item is closed only when the edit is verified in the file and its commit is recorded |
| A disagreement with the charter | A charter issue (`CI-N` in section 14) for the integrating session | The charter is edited with a `Refs:` trailer before SRR (Log-class until SRR, 05 Table 4-1 row 1), by CR after |

Every review package lists the open NCRs, RIDs, alignment items and charter issues that touch requirements, with owner and due gate (charter section 4 item 1).

### 8.7 Waivers

A waiver is a documented authorization releasing the project from meeting a requirement after the requirement is under configuration control (NPR 7123.1D App. A); authorized waivers do not constitute a change to a baseline (SE HB §6.5.1.2.3). Tables G-6 entrance 5.1 and G-7 entrance 5 accept a design that meets all requirements "or has waivers". The CM plan defines the record: a *product waiver* is a CR with disposition `Approved (waiver)` or a numbered waiver `W<n>` in a review decision memo, status-accounted in CSA item 12 (05 sections 2, 5.2 and 6). On cwht:

1. A requirement of any priority found not met, by analysis before build or by an NCR after it, is dispositioned by NCR `Use-as-is` (04 section 10.4) and a product waiver. Between reviews the waiver is a `CR-NNN` carrying the full impact assessment (05 section 5.3) with the residual risk as an `RSK-NNN` entry; at a review it may instead be an item `W<n>` of the decision memo. The requirement text does not change; the waiver is not a baseline change and does not count in the volatility metric (section 10.4).
2. Robin approves the waiver as Engineering Technical Authority (05 section 3); for an S1 NCR no waiver is admitted, for an S2 only with an owner decision memo (04 section 10.4).
3. In the commit that records the approval Claude adds the tag `waived` to the requirement (the waiver is the authority for that tag, section 10.2) and enters the waiver in CSA item 12 (05 section 6).
4. At SAR the decision memo accepts the product with the waiver, and the requirement moves from `Active` to `Closed` with the tag `waived` (section 8.3); T-11 accepts `Verified` or waived at SAR (planned `WAIVER_UNRECORDED`, section 8.5).
5. A waiver needed before the PDR or CDR decision memo is listed in that review's package under Table G-6 entrance 5.1 or Table G-7 entrance 5.

---

## 9. TBD and TBR policy

1. `TBD` (value unknown) is never written into a requirement, expectation, ICD or test file. If a value is unknown, the requirement stays out of the file until a best estimate exists, or the estimate is written with `(TBR)`.
2. `TBR` (value estimated, to be resolved) is written as the estimate followed by `(TBR)` in `description`, with the `tbr` object giving `owner` (who produces the evidence and who decides), `plan` (the analysis, trial or measurement that closes it and where the decision is recorded), and `close_by` (a review). L1 TBRs close by PDR and L2 TBRs by CDR (charter section 7); an L1 TBR may be assigned `SRR` when the plan completes before SRR. A TBR is admitted on a `Draft` or `Active` requirement: baselining a level does not require its TBRs closed, only planned (Table G-4 success criterion 8); the tool rejects a `tbr` object only on a `Verified` or `Closed` requirement, retired ones included (`TBR_ON_FINAL_STATUS`), and requires the `(TBR)` mark in `description` whenever the object is present (`TBR_UNMARKED`; section 8.5, T-14).
3. The open-TBR list is part of every review package (Table G-4, G-6 and G-7 success criterion: TBD and TBR items identified with acceptable plans and schedule). Until the planned report section exists (section 8.1), Claude builds the list from the report's summary count (`Requirements with open TBR`) and the `tbr` objects of the requirement files and puts it in the package.
4. Closing a TBR replaces the value, removes `(TBR)` and the `tbr` object, and records the decision in an ADR (when the choice constrains later work) or in the CR. After the level's baseline, TBR closures are Class I changes (section 10.2); several closures may be batched in one CR ahead of a review.
5. A TBR whose `close_by` review passes without closure is handled by the 01 lien rules, not by a closure plan. Inside the charter section 7 limit (an L1 TBR before PDR, an L2 TBR before CDR) it is a missed lien: Claude reports it to the owner, who chooses Extend (a new `close_by` no later than the limit), Convert (to a `CR-NNN` or `RSK-NNN`) or Re-severitize, recorded in the decision memo section 13 and as a same-state history entry (01 section 12.2). At the limit it is never a lien: an open L1 TBR blocks the PDR trigger and an open L2 TBR blocks the CDR trigger (01 sections 5.2 and 6.2; PDR and CDR entrance row 25, Hard), and an open TBR found at that review is a Major RID, which is Closed before the memo is signed (01 sections 10.2 and 12.2).

---

## 10. Change control after SRR

### 10.1 Authority, states and flow

From the SRR decision memo (`baseline/srr`), `expectations.json` (including the `stakeholders` array), `conops.md` and `docs/requirements/sys/requirements.json` are under configuration control; from PDR the L2 files, the ICDs (external stubs included) and `allocation.json` join them; test case files join with the requirements they cite (05 Table 4-1 row 17: from SRR for a case citing an L1 requirement, from PDR for a case citing only L2 requirements). Robin acts as the Configuration Control Board (SE HB §6.2.1.2.4, charter section 7). Anyone (owner, Claude, a reviewer agent through a RID) may propose a change; only Robin dispositions.

CR states, front matter, commit trailers (`CR: CR-NNN` mandatory on every non-editorial commit to a class-CR CI; `Refs:` for the affected ids; `Editorial: <reason>` for editorial commits), lifecycle actors (Draft, Submitted, Assessed by the independent reviewer, Dispositioned by Robin, Implemented by Claude, Verified by the independent reviewer, Closed on Robin's merge approval, Withdrawn) and impact fields are those of `docs/process/05-configuration-and-data-management.md` sections 4.5, 5.2 and 5.3 and of `docs/templates/change-request.md`. This document adds nothing to them; it fixes only what is requirement-specific (10.2 to 10.4) and the waiver use of a CR (section 8.7).

### 10.2 Classes

Class definitions are those of `docs/process/05-configuration-and-data-management.md` (SE HB §6.5.1.2.3); this table maps requirement-file, expectation, ICD and scenario fields onto them.

| Class | Requirement-file changes in this class | Handling |
|---|---|---|
| Class I (major) | Any change to `description`, `verification_method`, `priority`, `parent_id`, `hazard_ids`, `status` other than an evidence-driven transition of 8.3; addition of a requirement; retirement of a requirement; closure of a TBR; adding or removing the tags `safety`, `regulatory`, `security`, `interface`, `reused`, `leaf`; any change to an MOE, constraint or NGO statement or to the `stakeholders` array; any change to an ICD definition table or `OPS` scenario | CR with the full impact assessment (05 section 5.3); independent review; Robin approves |
| Class II (minor) | Changes to `rationale`, `verification_note`, `mop_ids`, `source_ids`, `design_refs`, other `tags`, and wording of `title` that alters meaning; ICD changes outside the definition tables | CR with the 05 section 5.3 fields Verification, Requirements and traceability and Documentation filled, the rest "None" with the one-line reason; independent review when a requirement, ICD, hazard or test case is affected (05 section 5.2); Robin approves |
| Editorial | Spelling, grammar and formatting in any field with no change of technical meaning; regeneration of `child_ids` from `parent_id` (a derived link field whose authority is `parent_id`) | No CR; commit type `editorial` or an `Editorial:` trailer (05 section 4.5); the tool lists them in the report's editorial log since the baseline (T-13) |

The tag `waived` is added only by the waiver process of section 8.7, whose CR is the authority for it.

### 10.3 Requirement-specific content of a CR

The CR file is written from `docs/templates/change-request.md`; the template's fields win. For a CR that touches a requirement, expectation, scenario or ICD:

1. `affected_ids` in the front matter lists every `REQ-`, `TC-`, `NGO-`, `MOE-`, `CON-`, `OPS-` and `ICD-` id touched (and the stakeholder `name` for a change to the array), and `affected_paths` every file.
2. Template section 1 (description) carries the text before and after for every affected `description`, expectation `statement`, stakeholder entry, scenario step or ICD table row, so that the reviewer and T-13 compare exact strings.
3. Template section 2 (reason) names the origin: the RID, RFA, NCR, TPM breach, TBR closure or new `SI-NNN`, and the alternative of not making the change with its risk (SE HB §6.2.1.2.5 requirements creep).
4. The 05 section 5.3 rows **Risk** (`RSK-` ids added, closed or re-scored), **Software classification and tailoring** (classification record, `rmm.json` or compliance-matrix rows), **Operations and ConOps** (`OPS-` scenarios affected), **Cybersecurity** (USB firmware-load or key-input command path) and **Regulatory** carry those impacts of a requirement change; the CR template section 4 has the same rows.
5. The **Requirements and traceability** row states the parents and children affected and the orphans or uncovered requirements the change would create, from a `tools/traceability.py` run on the CR branch; the **Interfaces** row names the ICD and both sides' requirements (section 3.5).

### 10.4 Requirements volatility metric (SWE-200)

The metric is `MSR-02` of `docs/process/07-software-engineering-plan.md` section 11 and is mirrored to `docs/plan/tpm.json` as `TPM-012` by `tools/measurements.py` (07 section 11.1). One script computes it and one file stores it: `tools/traceability.py --volatility --from <baseline tag> [--to <ref>]` (planned option, section 8.1, due PDR) reads the requirement files at the two git refs, classifies every difference per section 10.2, and appends the `MSR-02` record to `docs/plan/measurements.json`. It reports L1, L2 (all modules and per module) and the software modules alone (the SWE-200 scope) separately:

- N_start: number of requirements that are not retired (section 11.3) in the files at the start reference.
- A: requirements added since the start reference (present now, absent at the start).
- M: requirements with at least one Class I change since the start reference (a requirement counts once however many fields changed; TBR closures counted here and also reported as their own line; a waiver of section 8.7 is not a change).
- R: requirements retired since the start reference.
- C2: requirements with only Class II changes (reported beside V, not counted in it).

Formula:

```
V = (A + M + R) / N_start × 100 %
```

Reporting periods: from each baseline tag to the next gate (the gate-to-gate value is the one recorded as `MSR-02` and plotted as `TPM-012`), plus a snapshot at every sprint closure per 07 section 11. `V_cum` is the same formula from `baseline/srr` to the current reference and is reported alongside.

Thresholds between gates (07 section 11): `V ≤ 10 %` green; `10 % < V ≤ 20 %` yellow, Robin reviews requirement quality and the package names the drivers (which CRs, which modules); `V > 20 %` red, an RFA is opened at the next review and Robin records in its disposition whether the affected level is re-baselined or the driving changes are descoped. Volatility from TBR closures is shown as a separate line so that planned resolution is not read as instability. `docs/process/05-configuration-and-data-management.md` section 5.4, 07 section 11.2 (MSR-02), the RMM row SWE-200 and `docs/plan/tpm.json` (TPM-012) state this counting rule, script and storage; the CSA metrics section (05 section 6 item 10) copies the latest `MSR-02` value (alignment item AL-02-09).

---

## 11. ID allocation and retirement

### 11.1 Allocation

1. The next id in a module is `max(NNN)` over every entry in that file, retired entries included, plus one, zero-padded to three digits. Test cases follow the same rule per `docs/test_cases/<module>/test_cases.json`; the closing case of a requirement is allocated in the module of the requirement it closes (a system requirement's closing case in `sys`, a software requirement's in its `sw` or `sw-<sub>` file, section 4.4); supporting cases may be allocated in any module.
2. Allocation and content land in the same commit; no reservations, no placeholders.
3. Ids are never renumbered and never reused (charter section 6). Moving a requirement to another module means retiring the old id and creating a new one, with each rationale naming the other id.
4. `expectations.json` ids (`NGO-`, `MOE-`, `CON-`) and `OPS-` headings follow rule 1 within their file. Stakeholder entries are keyed by unique `name` (section 3.0). ICD ids are the pair names of section 3.5.
5. A new `SW-<SUB>` module is created only by the ADR that records the firmware architecture (section 2.2).

### 11.2 Baseline flip

At each baseline the author sets `status` from `Draft` to `Active` for every requirement of the baselined level in one commit that references the decision memo, then tags `baseline/<review>`. At SRR the same commit sets every `Draft` L0 entry (`NGO-`, `MOE-`, `CON-`) to `Baselined` and sets the `baseline` field of `expectations.json` to `"baseline/srr"`, which makes the `stakeholders` array mandatory under the schema (section 3.0). T-12 (once implemented) accepts these transitions only when the memo file exists. Requirements with an open `tbr` object flip with the rest (section 9 rule 2).

### 11.3 Retirement

Charter section 6: ids are never reused; a retired item keeps its id with status *Retired* where its schema has that status, otherwise status `Closed`, tag `retired` and a rationale. `docs/requirements/schema.json` (`Draft`, `Active`, `Verified`, `Closed`) and `docs/test_cases/schema.json` (`Draft`, `Active`, `Passed`, `Failed`, `Blocked`; no `tags` field) are not changed by this process. The interim markers below apply until a CR adds `Retired` to both enums: Claude drafts that CR for the PDR package and Robin decides it at PDR (05 Table 4-1 row 9 puts the schemas under CR from SRR). After the CR, `status: "Retired"` replaces the interim status and the tag `retired` stays as history; the tool already recognizes both forms (T-19).

| Item | Interim marker (today) | Reason text | Tool rule |
|---|---|---|---|
| Requirement | `status: "Closed"` and `"retired"` in `tags` | `rationale` prefixed `Retired by CR-NNN (or, before the level's baseline, RID-<REVIEW>-NNN or INSP-NNN): <reason>; superseded by REQ-... ` when a replacement exists | T-19; excluded from T-09, T-18, the `Closed` rule of T-11 and the matrices |
| Test case | `status: "Blocked"` | first sentence of `setup`: `Retired by CR-NNN (or, before the citing level's baseline, RID-<REVIEW>-NNN or INSP-NNN): <reason>; superseded by TC-... ` | T-19; a `Blocked` case whose `setup` does not start `Retired by ` is blocked, not retired |
| L0 entry (`NGO-`, `MOE-`, `CON-`) | `status: "Retired"` with `retired_by` (the L0 schema, owned by this process, carries the status) | `rationale` unchanged; `retired_by` names the CR, or before SRR the RID or INSP record (schema definition `cr_id`) | T-21, T-12 |

Procedure:

1. Set the interim marker. `Closed` keeps its accepted-at-SAR meaning for every requirement without the tag (04 section 5.3, T-11), and `Blocked` keeps its cannot-run meaning for every case whose `setup` does not start `Retired by `.
2. Write the reason text of the table. A `tbr` object, if present, is removed: a retired value is not resolved.
3. Children are re-parented or retired in the same commit; `child_ids` are regenerated; the retired id is removed from `requirement_ids` of every live test case that cites it (04 section 7.3 rule 2), and a case left with no live requirement is retired per section 8.4.
4. The entry stays in the file for the life of the repository (T-04); the tool excludes retired entries from coverage, allocation and the matrices (T-19, T-09, T-18; 04 section 7.1).
5. Retirement after the level's baseline is a Class I change (section 10.2) and counts in R of the volatility metric (section 10.4).

---

## 12. Deliverables of this process at each gate

| Gate | This process delivers | Criteria source |
|---|---|---|
| SRR | `expectations.json` complete with the `stakeholders` array (section 3.0; SE-35; Table G-3 entrance 3.1), Need, Goals, Objectives, Constraints and MOEs with `ops_ids` ready to approve (SE-37; T-21); `conops.md` scenarios; `sys/requirements.json` ready to baseline (SE-39), every requirement carrying `verification_method` and a validation path (Table G-4 entrance 6.8; section 2.3); a `Draft` closing case for every L1 requirement in `docs/test_cases/sys/test_cases.json` (section 4.1 step 7; 04 section 16); preliminary allocation of every L1 requirement to at least one L2 module, through `child_ids` or a preliminary `docs/design/allocation.json` (Table G-4 entrance 5.1; 01 section 4.3 row 7; T-18 Warnings confirmed in V6); `docs/requirements/tx/requirements.json` with the `regulatory` `REQ-TX-*` entries (01 section 4.3 row 25) and `docs/requirements/sw/sw-keyer/requirements.json` (SI-018), both `Draft` with their `Draft` closing cases; every core `SI` covered (T-20; SI-018 by one requirement per key type); KDR list and preliminary MOPs and TPMs in `docs/plan/tpm.json` (Table G-4 entrance 6.12); external ICD stubs reviewed, with security expectations where section 3.5 requires them (Table G-4 entrance 6.11, success criterion 4); open TBR list with plans (Table G-4 success criterion 8); the section 2.4 coverage table, including security and the fault-response requirements, and the list of requirements carrying `Fault tolerance:` against `docs/safety/hazard-analysis.md` section 8.1 (Table G-4 success criterion 14; 01 section 4.3 row 15); validation records V1 to V6 for every L1 requirement with zero open Major RIDs; `tools/traceability.py` exit 0 with the `gate` column of 8.2 applied by hand; the section 8.5 rows due before SRR done; this document approved by Robin as Engineering Technical Authority, with 05 section 5 as the change-control procedure (Table G-4 success criterion 3) | NPR 7123.1D App. G Tables G-3 and G-4; §5.2.2.2 SE-35, SE-37, SE-39; SE HB §4.2.1.2.6 |
| PDR | L2 `requirements.json` for every module; allocation of requirements to the next lower level baselined (SE-42; Table G-5 entrance 5.2; every Active `SYS` requirement allocated, T-18); MOPs and TPMs approved and baselined (SE-40; Table G-5 entrance 5.3); `design_refs` to architecture elements; all ICDs written, paired (T-22), reviewed and baselined; all L1 TBRs closed; validation records for every L2 requirement; every unmet requirement waived per section 8.7 (Table G-6 entrance 5.1); `--gate PDR` zero violations | Tables G-5 and G-6; §5.2.2.2 SE-40, SE-42 |
| CDR | All L2 TBRs closed; ICD TBRs closed; every requirement has an Active closing `TC` (T-09); `design_refs` complete to sheets and Rust modules; every unmet requirement waived (Table G-7 entrance 5); `--gate CDR` zero violations | Table G-7 |
| TRR | `Bench` and `OnAir` cases Active; verification matrix shows a procedure for every requirement to be tested on the unit | Table G-10 |
| SAR | Every requirement `Verified`, or `Active` with an approved waiver (section 8.7); software requirements closed by `HostUnit` or `Emulation` with the PCA-05 installed-release line; verification and validation matrices complete; requirements set `Closed` by the memo | Table G-11 |

---

## 13. Compliance mapping

| Governing requirement | Where this process satisfies it |
|---|---|
| NPR 7123.1D SE-07 Stakeholder Expectations Definition process (ETA-approved) | Sections 3.0 to 3.3; ETA approval in the SRR decision memo (header) |
| NPR 7123.1D §3.2.2.2 item h (security, transportability, disposability among the expectation factors) | Section 2.4 rows Security, Transportation, Disposal |
| NPR 7123.1D SE-08 Technical Requirements Definition process (ETA-approved); §3.2.3.2 system security considered in the technical requirements | Sections 2, 4, 5, 6; section 2.4 Security row and tag `security` (section 2.3); ICD security expectations (section 3.5) |
| NPR 7123.1D SE-17 Requirements Management process (ETA-approved) | Sections 7 to 11 |
| NPR 7123.1D SE-18 Interface Management process (ETA-approved, §3.2.13.1) | Section 3.5, `docs/templates/icd.md`, T-22 |
| NPR 7123.1D SE-35 baselined stakeholder identification and expectation definitions (MCR, absorbed by SRR) | Sections 3.0 and 3.2; the `stakeholders` array; section 11.2 flip; section 12 SRR row |
| NPR 7123.1D SE-37 approved MOE definition | Sections 3.2 and 6; section 12 SRR row |
| NPR 7123.1D SE-39 baselined requirements (SRR) | Sections 4, 5, 11.2; section 12 SRR row |
| NPR 7123.1D SE-40 approved TPM definitions (SDR, absorbed by PDR) | Section 6.2; section 12 PDR row |
| NPR 7123.1D SE-42 baselined allocation of requirements to the next lower level (SDR, absorbed by PDR) | Sections 2.3 (Flowdown), 7 row 1, T-18; section 12 SRR (preliminary) and PDR rows |
| NPR 7150.2D SWE-027 item a (requirements to be met by reused components identified) and item e | Section 2.3 row Reused and OSS components; tag `reused` |
| NPR 7150.2D SWE-050 establish, record, approve, maintain software requirements, including for COTS, GOTS, MOTS, OSS and reused components | Sections 2.1, 2.2 (`sw/` files), 2.3 (reused and OSS components, tag `reused`, T-15), 4, 11; the third-party register of 07 section 17.1 lists the components |
| NPR 7150.2D SWE-051 requirements analysis from flowed-down and derived requirements, safety and reliability analyses, hardware | Sections 2.3 (parent, self-derived, hazard-derived), 4.1, 4.3 (`Fault tolerance:`, `Depends on:`) |
| NPR 7150.2D SWE-184 safety constraints, controls, mitigations and assumptions between hardware, operator and software | Section 2.3 (`safety` tag, `hazard_ids`), 4.3 (`Assumes:`, `Depends on:`), 7 row 2, V3 item (e) |
| NPR 7150.2D SWE-052 bidirectional traceability, §3.12.1 Table 1 Class A | Sections 7, 8 |
| NPR 7150.2D SWE-053 track and manage changes to software requirements | Section 10 with 05 section 5 |
| NPR 7150.2D SWE-054 identify, correct and track to closure inconsistencies among requirements, plans and products | Section 8.6; section 10.3 item 5; section 14 |
| NPR 7150.2D SWE-055 requirements validation for the customer environment | Section 5, validation path (section 2.3), validation matrix (section 7), charter section 9 |
| NPR 7150.2D SWE-087 peer review of requirements | Section 4.1 step 9, section 5 records |
| NPR 7150.2D SWE-200 requirements volatility metrics | Section 10.4 |
| NPR 7150.2D SWE-210 software requirements for detection data of adversarial actions | Section 2.4 Security row (the persistent event log of RMM row SWE-210), tag `security` |
| NPR 7150.2D SWE-211 test reused components to the level of developed code | Section 2.3 row Reused and OSS components |
| NPR 7123.1D App. G Tables G-3, G-4, G-5, G-6, G-7, G-10, G-11 | Section 12 |
| SE HB App. C writing checklist and C.4 validation checklist | Sections 4.2, 2.4, 4.4 |
| SE HB Table 4.2-2 metadata | Section 4.5 |
| SE HB §4.1.1.2.1 identify stakeholders | Section 3.0 |
| SE HB §4.2.1.2.4 six validation steps | Section 5 |
| SE HB §4.2.1.2.5 MOPs and TPMs; §4.2.1.2.3 KDRs | Section 6 (6.4 records the priority customization) |
| SE HB §6.3 interface management; App. L interface requirements document outline | Section 3.5, `docs/templates/icd.md` |
| SE HB §6.5.1.2.3 waiver | Section 8.7 |
| SE HB App. D and App. E matrices | Section 7, section 8.1 outputs (04 sections 7.1 and 7.2) |

---

## 14. Charter issues and cross-document alignment items

Raised by the author of this document for the integrating session (section 8.6). Charter commit b3d2e13 closed CI-1, CI-3 and CI-5; charter commit b8214ca closed CI-2, CI-4 and CI-7 and adopted the Verified-versus-Closed rule for host-verified software that AL-02-17 had argued against. CI-9 and CI-10 are open charter wording items (a charter edit with a `Refs:` trailer before SRR, since the charter is Log-class until SRR, 05 Table 4-1 row 1). Alignment items carry the prefix `AL-02-` because 05 section 14.1 already uses `AL-1` to `AL-14` for other items; the number after the prefix keeps the number this document used before (AL-7 is now AL-02-07). All process documents are untracked in git on 2026-09-25, so no closure below has a commit yet; "closed in the working tree" means the edit was verified by reading the named file on 2026-09-25, and the closure is confirmed by the commit that brings the file under version control before SRR.

| # | Kind | Statement | Resolution |
|---|---|---|---|
| CI-1 | Charter section 6 | `CON-NNN` and `SI-NNN` were absent from the identifier list. | Closed by b3d2e13. |
| CI-2 | Charter sections 5 and 6 | The software module layout read as `sw/<sub>/`. | Closed by b8214ca: charter sections 5 and 6 write `docs/requirements/sw/sw-<sub>/requirements.json` (section 2.1). |
| CI-3 | Charter section 6 versus schemas | The requirement and test-case schemas lack a `Retired` status. | Closed by b3d2e13 (interim marker, section 11.3); the schema CR is drafted for PDR. |
| CI-4 | Charter section 6 | Test-only case modules `VAL`, `ATP`, `SW-COV`, `SW-REG`, `SW-TOOL` were not listed. | Closed by b8214ca: charter section 6 lists them (section 2.2). |
| CI-5 | Charter section 7 | The charter stated what the tool enforces without evidence. | Closed by b3d2e13; section 8.5 remains the evidence. |
| CI-6 | Charter section 7 | `control_req_ids` sits on each control; the hazard-level `requirement_ids` is the union. | Closed, no charter change: section 7 row 2 and T-08 state both fields, and the tool reads both. |
| CI-7 | Charter section 5 | The per-review working files listed both `checklists/` and `peer-reviews/INSP-NNN.md`. | Closed by b8214ca: the filled checklist is the single record with `id: INSP-NNN`, no `peer-reviews/` folder (section 5). The other documents still citing `peer-reviews/` are AL-02-10. |
| CI-8 | Charter section 1 versus the tool | The tool and L0 schema admitted Part 97 clauses only. | Closed, no charter change: the L0 schema and the tool admit and resolve Parts 1, 2, 15 and 97 (section 8.5, T-07). |
| CI-9 | Charter section 6 | The module list "SYS, RX, TX, PWR, CTL, ME, SW-<sub>" omits `SW`, the firmware-wide L2 module that charter sections 5 (`docs/requirements/{rx,tx,pwr,ctl,me,sw}/requirements.json`) and 7 (L2 includes SW) use and that section 2.2 and 07 section 4 item 1 define. | Open. Charter edit with a `Refs:` trailer before SRR: add `SW` to the section 6 module list. |
| CI-10 | Charter section 6 | No identifier scheme exists for stakeholders; section 3.0 keys stakeholder entries by unique `name`. | Open, owner's choice before SRR: keep `name` keys (default, no change), or add a scheme such as `STK-NNN` to charter section 6, after which a schema edit adds an `id` field to the `stakeholder` definition. |
| AL-02-07 | 04 sections 7.1 and 7.3 rule 2 | "until the schema gains that value no requirement may be retired" (04 section 7.1, working tree 2026-09-25). | Open, owner: 04 author, before SRR. Reword to the interim marker of section 11.3 (status `Closed`, tag `retired`; test case `Blocked` with `Retired by ` in `setup`), which the tool already recognizes. |
| AL-02-08 | 05 section 5.3, `docs/templates/change-request.md` | No impact rows for software classification and RMM, risk, ConOps. | Closed in the working tree (05 section 5.3 and CR template section 4 read 2026-09-25 have the rows Risk, Software classification and tailoring, Operations and ConOps, and Cybersecurity; 05 section 14.1 AL-10); edits by the 05 author; commit pending. Section 10.3 item 4 now points to those rows. |
| AL-02-09 | 05 section 5.4, 07 MSR-02, RMM SWE-200 | Volatility computed by another script and counting rule. | Closed in the working tree (05 section 5.4, 07 section 11.2 row MSR-02 and RMM row SWE-200 read 2026-09-25 name `tools/traceability.py --volatility` and the section 10.4 rule); edits by the 05, 07 and 03 authors; commit pending. |
| AL-02-10 | 07 sections 1.2 (Records row), 3.4, 10.2 and 22; `docs/templates/peer-review-checklist-requirements.md` "Record front matter" (line 9 and the `checklist_file` line) | These still name `docs/reviews/<REVIEW>/peer-reviews/INSP-NNN.md` as the peer-review record (working tree 2026-09-25, 18:20). Charter section 5 (b8214ca) makes `docs/reviews/<REVIEW>/checklists/<product-slug>.md` with `id: INSP-NNN` the single record with no `peer-reviews/` folder, and `tools/validate_docs.py` rejects such a folder. | Reopened (was closed in revision C), owners: the 07 author and the checklist template maintainer (Claude), before SRR; 01 section 15 row 5 names the same edits. Done in the working tree since revision C: 01 (sections 1 and 13), 05 (section 4.1 row L1; its AL-7 now adopts the charter path) and the templates `baseline-record.md`, `decision-memo.md`, `review-package.md`. Still open from revision C: add the per-requirement table of section 5 (columns WR failures and V1 to V6) to the requirements checklist template before the first L1 review. |
| AL-02-11 | 03 section 8, 07 CS-24 | 03 traced code with `// Trace:` comments. | Closed in the working tree (03 section 8 uses the CS-24 tags and the 07 paths); edit by the 03 author; commit pending. |
| AL-02-12 | 07 section 4 | Called `sw/sw-<sub>/` files "L3". | Closed in the working tree for 07 sections 1.3, 3.1, 3.5 and 4 (edit by the 07 author; commit pending). Residual, owner 07 author, before SRR: 07 section 11.2 row MSR-04 still says "CDR (L2/L3)". |
| AL-02-13 | `docs/process/README.md` | Claimed SE-09 for this document. | Closed in the working tree (SE-09 on the SEMP row); commit pending. |
| AL-02-14 | `docs/plan/semp.md` sections 5.2 and 7.4, `docs/plan/tpm.json` | No `mops[]`; the SEMP did not define MOPs. | Closed in the working tree: `tpm.json` holds MOP-001 to MOP-020 with every performance TPM naming its MOP, and SEMP section 7.4 names `mops[]` (section 6.2); commit pending. |
| AL-02-15 | 08 sections 3.1 and 3.5 | ICD reviewer checklist named a non-existent file. | Closed in the working tree: 08 names `peer-review-checklist-design.md`, which has sections I and J; commit pending. |
| AL-02-16 | 05 section 4.3 identification table; 03 section 8 | Retired status and `control_req_ids` contradicted the charter. | Closed in the working tree: 05 section 4.3 writes status `Closed` with tag `retired`; 03 section 8 names the union of the per-control lists; commit pending. |
| AL-02-17 | 04 section 5.3 | Revision C asked 04 to make `Verified` depend on PCA-05 (charter b3d2e13 wording). | Superseded by b8214ca: charter section 9 now makes such a requirement `Verified` on the credited report and `Closed` after PCA-05; sections 4.4, 8.3 and T-11 follow it. The 04 edit this now requires is AL-02-18. |
| AL-02-18 | 04 sections 5.2 (platform-independent row), 5.3 (requirement status), 7.3 rule 4 and 7.4 row 7.3.4 | 04 made `Verified` for `REQ-SW-*` require the PCA-05 line and named the check `VERIFIED_NOT_INSTALLED`. 05 section 14.1 AL-11 raised the same item. | Closed in the working tree (verified 2026-09-25 by the integrating session): 04 sections 5.2 and 5.3 put the PCA-05 line and the signed SAR memo under `Closed` per charter section 9, and 02 (T-11), 04, 05 and `tools/README.md` use the single code name `CLOSED_NOT_INSTALLED` (implementation due CDR); commit pending. |
| AL-02-19 | RMM row SWE-051 (`docs/process/rmm.json`) | Says ICDs are cited "via source_ids"; section 3.4 cites interfaces in `design_refs`. | Open, owner: 03 author (RMM), before SRR. Write "via design_refs". |
| AL-02-20 | 07 section 4 item 2 | Module-file requirements carry "source_ids naming the hazard (HZ-NNN), ICD, ADR or SWE-134 item". Section 3.4: hazards go in `hazard_ids`, ICDs in `design_refs`, only `ADR-`/`TS-` in `source_ids`; a SWE-134 item is named in `rationale`. | Open, owner: 07 author, before PDR (first module-file requirements). |
| AL-02-21 | `docs/requirements/l0-stakeholder/expectations.json` | Has no `stakeholders` array (section 3.0; schema definition `stakeholder`). | Open, owner: Claude as expectations author, before the SRR readiness declaration; with it, the tool task `STAKEHOLDERS_MISSING` and the `--render` section (section 8.5). |
| AL-02-22 | `expectations.json` or `docs/decisions/adr/` | No `CON-` or `ADR-` records the cybersecurity assessment scope of charter section 12, which the tag `security` requires as a source (section 2.3). | Open, owner: Claude, before the first `security`-tagged requirement is written: a `CON-` of kind `Process` with source SI-015 (Class A process election) stating the charter section 12 scope, added to `expectations.json`. |
| AL-02-23 | 05 sections 2, 5.2 and 6 (CSA item 12); 04 section 10.4 `Use-as-is` row | Revision C had no waiver path. | Closed in the working tree: 05 section 2 defines the product waiver (a CR with disposition `Approved (waiver)` or a memo item `W<n>`), section 5.2 the disposition and CSA item 12 the waiver register; 04 section 10.4 `Use-as-is` already requires a CR that waives the requirement. Section 8.7 follows them; no further edit needed. |
| AL-02-24 | `docs/templates/icd.md` sections 3.2.5 and 3.2.6 | No `Security expectations` row (section 3.5 Content). | Open, owner: Claude as template maintainer, before the ICD stubs are reviewed for SRR. |
| AL-02-25 | 01 section 4.3 row 28 | Names `tools/refs/` as the conversion of the regulatory corpus; the corpus was fetched with the eCFR versioner API command of `docs/references/md/regulatory/README.md` (section 3.4). | Open, owner: 01 author, before SRR. |
| AL-02-26 | `docs/plan/semp.md` customization list | The single-valued `priority` of section 6.4 is a customization of SE HB §4.2.1.2.3. | Open, owner: SEMP author (Claude), before SRR: list it with the other customizations (05 section 14.1 AL-12 asks the SEMP for its CM customizations in the same edit). |
