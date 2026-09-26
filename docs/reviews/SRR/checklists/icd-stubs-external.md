---
id: INSP-012
checklist: peer-review-checklist-design
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/icd-stubs-external.md
product: docs/icd/
# product_commit: the review baseline of iteration 3 (HEAD adcfe09); iterations 1 and 2 reviewed working-tree blobs over 28e49e6 (body tables)
product_commit: "adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1"
# product_files: the committed blobs (git rev-parse HEAD:<path> at adcfe09) reviewed at iteration 3; iteration 2 blobs 0560bd89 (KEY) and ca2081dc (ANT) are not in the object store; iteration 1 blobs are in the body table
product_files: ["docs/icd/ICD-CTL-KEY.md@5e9f1888fcac3003e834bf25b0630e42d447de8a", "docs/icd/ICD-CTL-PHONES.md@a97c636d3d790f1cb82e1c09c1142170fd0573b0", "docs/icd/ICD-CTL-USB.md@0c2541960774f3cbc8828d6e338c2707b092f31c", "docs/icd/ICD-PWR-CELL.md@28e2656ec63073020b34568b423bd7c4473a8bd3", "docs/icd/ICD-TX-ANT.md@394d8bffb419ee5d98528e58fa6cc9475fc2c2bf", "docs/icd/figures/render_icd_figures.py@5e0027af2211af1063cf00463c6175f481c45a44", "docs/icd/figures/ICD-CTL-KEY-plane.png@dfaaeaf4ab6e07e494ee3e0123db83f1d3929fc9", "docs/icd/figures/ICD-CTL-PHONES-plane.png@923539828481ba22012883cd9528a3bfc0250368", "docs/icd/figures/ICD-CTL-USB-plane.png@fd541d5f1c34024157dfe13177d480979df62cee", "docs/icd/figures/ICD-PWR-CELL-plane.png@4a0cf3a46a4c2e1cbf354bf856b53c015998ff81", "docs/icd/figures/ICD-TX-ANT-plane.png@ee75beaf1ba4e2fa09a83bbb78ff8d62491ef402"]
product_size: 5 ICD stubs (1286 lines) plus 5 interface-plane figures and their render script
sprint: SRR-prep
author_agent: "author:icd-author (Claude ICD author invocation 2026-09-25, named in each ICD owner field)"
reviewer_agent: "reviewer:icds"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 0
findings_minor: 11
findings_open: 0
findings_fixed: 0
findings_verified: 8
findings_deferred: 3
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# iteration 3 answers (iteration 2: CK-DES-I5; iteration 1: CK-DES-I3, CK-DES-I4, CK-DES-I5); CK-DES-I5 is No for the CTL and PWR side-A pairing and the KEY section 4 list, both carried as liens
items_no: [CK-DES-I5]
effort_turns: 92
effort_minutes: 120
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-012: external ICD stubs (ICD-CTL-KEY, ICD-CTL-PHONES, ICD-TX-ANT, ICD-CTL-USB, ICD-PWR-CELL)

**Checklist:** `docs/templates/peer-review-checklist-design.md` revision B, section I, as `docs/process/08-agent-briefing.md` section 3.5 assigns to ICD stubs; sections A to H and J are marked N/A. **Governing for the product:** `docs/templates/icd.md` (working tree, with the Security expectations rows of sections 3.2.5 and 3.2.6), `docs/process/02-requirements-and-traceability.md` section 3.5 (Identity, Order, Owner, Creation, Content, Pairing, Baseline and change rows) and rule T-22, charter sections 5, 7 and 11. **Gate:** SRR, entrance criterion row 17 of `docs/process/01-lifecycle-and-reviews.md` section 4.3 ("External interfaces identified with preliminary definitions", NPR 7123.1D App. G Table G-4 entrance criterion 6.11), package `docs/reviews/SRR/package.md` section 2 item H11. **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable, each with evidence.

**Search-first compliance:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was run before any manual search (queries: ICD identity, order and pairing rule T-22; key input network DC abuse and clamp currents; 07 section 16.2 cybersecurity rows; traceability.py ICD pairing check). `grep -n` was used afterwards only to pin lines. Reading files at known paths was not treated as a search.

**Criticality and assurance:** `criticality: neither` and `assurance_required: false` because the table of `docs/process/07-software-engineering-plan.md` section 2.1.1 has no ICD row. ICD-CTL-KEY and ICD-CTL-USB state boundary behaviour of safety-critical components of 07 section 14.1 (keyer, boot and image check); the missing row is returned to Claude as a process issue, not a finding against the ICDs.

**Minimum content judged (row 17):** the row names "key or paddle jack, headphone jack, antenna connector, USB, charger and battery". Key or paddle jack: ICD-CTL-KEY. Headphone jack: ICD-CTL-PHONES. Antenna connector: ICD-TX-ANT. USB and charge input: ICD-CTL-USB. Battery, holders and the charger thresholds applied to the cells: ICD-PWR-CELL. Every item of the row is covered, and the external token set of 02 section 3.5 (`KEY`, `PHONES`, `ANT`, `USB`, `CELL`; `HOST` at PDR) is complete for SRR.

## Product files reviewed

The files are untracked in the working tree on top of commit `28e49e6` (`git status --short docs/icd/` shows `?? docs/icd/` on 2026-09-25), so `product_commit` names the base and the blob hashes below (from `git hash-object`) identify the reviewed content.

| File | Blob | Lines | Result | Findings that apply |
|---|---|---|---|---|
| docs/icd/ICD-CTL-KEY.md | 75c690ce8ad5632d8a0bf04fae31516ad6313776 | 272 | Fail | 1, 2, 3, 4, 5 |
| docs/icd/ICD-CTL-PHONES.md | 9e19c38e32dd27a8b028109cae66763a92550713 | 257 | Fail | 1 |
| docs/icd/ICD-TX-ANT.md | 79fe9fb62f989c440147dc401c9942d455df6a72 | 259 | Fail | 1, 9 |
| docs/icd/ICD-CTL-USB.md | 88ef236c013679950f29877cfbbf4498d286d562 | 249 | Fail | 1, 5, 8 |
| docs/icd/ICD-PWR-CELL.md | 772c758bd5cdf26b36533409819dcce3bf101005 | 249 | Fail | 1, 6, 7 |
| docs/icd/figures/ICD-CTL-KEY-plane.png | c24a2ec117932375b51a66ae3115ba74d5d1e927 | binary | Fail | 2 |
| docs/icd/figures/ICD-CTL-PHONES-plane.png | 923539828481ba22012883cd9528a3bfc0250368 | binary | Pass | none |
| docs/icd/figures/ICD-TX-ANT-plane.png | 420398de74eca4955d42570d3139582e7a3e0784 | binary | Pass | none |
| docs/icd/figures/ICD-CTL-USB-plane.png | 3a86e55dc26e8db5315b45e17b860c43698c04c3 | binary | Fail | 8 |
| docs/icd/figures/ICD-PWR-CELL-plane.png | dcdc8637d9cbc6d079c4335f18aee0d3f43939eb | binary | Fail | 6 |
| docs/icd/figures/render_icd_figures.py | 3aac52d8605b9311a0b217bc22cfab3015c4c287 | 769 | Pass | none (source of finding 8 lines 610 to 620) |

## Checks run by the reviewer

| Check | Command or method | Result |
|---|---|---|
| Outline against the template | heading list of each ICD diffed against `docs/templates/icd.md` | Identical for all five (sections 1.1 to 7, including 3.2.7.1 to 3.2.7.5) |
| `tbr_open` against section 6 rows | row count of each section 6 table | KEY 14 = 14; PHONES 14 = 14; ANT 16 = 16; USB 11 = 11; CELL 20 = 20 |
| Section 4 lists exactly the citing requirements | every requirement in `docs/requirements/**/requirements.json` whose `design_refs` names the ICD, compared with `requirements_other` | Equal for all five; every listed requirement carries the tag `interface` |
| Section 4 statements verbatim | each quoted statement and method compared with `description` and `verification_method` | 20 of 20 verbatim and matching |
| Identifier existence | every REQ, TC, HZ (with control K-numbers), RSK, ADR, SI, CON, OPS, OQ and CS id resolved against its source file; SRR decision items 31, 44, 49, 51, 61 to 66, 68, 70 to 76, 78, 80, 102 resolved in `docs/reviews/SRR/decisions-for-owner.md` | All resolve |
| Section 5 cases | each `Verifies` requirement checked against the case's `requirement_ids` in `docs/test_cases/**` | All agree |
| Front matter `hazard_ids` | compared with every HZ id cited in the body | Equal for all five |
| No placeholder token, no em dash | text scan | Zero in all five |
| Figures current | `.venv/bin/python docs/icd/figures/render_icd_figures.py --check` (layout checks and byte comparison with the PNGs on disk; writes nothing) | exit 0 |
| Figures inspected | all five PNGs opened with the Read tool (1600 x 1000 and 1600 x 1080) | Legible; text inside the frame; no overlaps; contents agree with the tables except findings 2, 6 and 8 |
| Traceability | `.venv/bin/python tools/traceability.py --report-only` | exit 0; 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125, REQ-SYS-148; not ICD related); no INTERFACE_TAG_NO_ICD warning, because every `interface`-tagged requirement cites an ICD |

## Numbers verified against their sources

These checks passed and are recorded as evidence, not findings.

| Claim (ICD, section) | Source checked | Result |
|---|---|---|
| KEY 3.2.5: pad below VIL 0.8 V with at least 0.21 V margin at 500 ohm; 0.587 V with 120 uA E9 leakage; open line 3.29 V | `docs/research/keyer-verification-and-key-input-network.md` F3 table row 10 kohm, 1.0 kohm, 500 ohm (0.430 V, 0.587 V, +0.213 V) | Agrees |
| KEY 3.2.5: release tau 47 us, closure tau 5.2 us, corner 34 kHz | F4: 10 kohm x 4.7 nF; 1.1 kohm x 4.7 nF; 1/(2 pi x 1 kohm x 4.7 nF) = 33.9 kHz | Agrees |
| KEY 3.2.7.1: about 70 dB attenuation of 144 MHz pickup | 4.7 nF reactance at 144 MHz is 0.235 ohm; 0.235/1000 is -72.6 dB (ideal parts) | Agrees |
| KEY 3.2.7.1: ESD 8.4 mA for 100 ns, C2 rise 0.18 V | F5: (12.4 - 3.3 - 0.7)/1 kohm; 8.4 mA x 100 ns / 4.7 nF = 0.179 V | Agrees |
| KEY 3.2.2: SJ1-3535N pins 1 sleeve, 2 tip, 3 ring, 4 tip switch, 5 ring switch; body 14.0 x 8.0 mm; nose 6.0 mm protruding 4.0 mm; 0.3 to 3 kg; 5,000 cycles; 12 V DC 1 A; 50 mohm; -25 to +85 C; 3.60 mm bore; 6.6 mm hole | `docs/research/display-and-ui-parts.md` F17 (line 120) and baseline table row "Key jack" (line 149) | Agrees |
| PHONES 3.2.7.2: divider k = 0.0870; 100 mVrms full-scale sine; 143.6 mVrms full-scale square; poles 3.27 and 3.39 kHz | 953/(10,000 + 953) = 0.0870; 1.65 V/sqrt(2) x 0.0870 = 101 mV; 1.65 V x 0.0870 = 143.6 mV; 1/(2 pi x 870 ohm x 56 nF) = 3.27 kHz; 1/(2 pi x 1 kohm x 47 nF) = 3.39 kHz | Agrees |
| PHONES 3.2.4: 4.7 mA rms at 150 mVrms into 32 ohm, 9.4 mA into 16 ohm; 0.31 mW at 100 mVrms into 32 ohm | I = V/R; P = V^2/R | Agrees |
| ANT 3.2.4: 22.4 V peak at 5 W; 25.1 V at 5 W + 1 dB; 45.6 V at SWR 10:1; 57.5 V at 10 W | sqrt(2 x P x 50); |Gamma| = 9/11; x (1 + 9/11) | Agrees |
| ANT 3.2.1: gravity moments 0.042, 0.078, 0.43 N m | `docs/research/antenna-and-erp.md` F8 bending table; m x g x L/2 | Agrees |
| ANT 3.2.2: 1/4-36 UNS-2A, 6.35 mm; hole 6.55 mm; boss at least 2.5 mm (0.100 in); HEX 8 about 7.9 mm; stainless 500 cycles; SMA 500 V peak | antenna-and-erp.md F8 | Agrees |
| ANT 2.1 and 3.2.7.1: 25 uW and 40 dB for a transmitter of 25 W or less between 30 and 225 MHz; 53.0 dB at 5 W | `docs/references/md/regulatory/47cfr-97.307.md` line 25 (paragraph (e)); CON-002; 37.0 dBm - (-16.0 dBm) | Agrees |
| ANT 2.1: 97.13(c) licensee actions before transmitting where exposure could exceed 1.1310 | `47cfr-97.13.md` line 21 | Agrees |
| USB 3.2.7.1: 48 MHz x 3 and 12 MHz x 12 land on 144.000 MHz | arithmetic | Agrees |
| USB 3.2.2: opening 12.0 x 10.0 mm clears a 10.6 x 8.5 mm overmold by 0.7 mm per side; receptacle face 0 to 1.0 mm; module edge 1.3 mm; centre about 2.3 mm | display-and-ui-parts.md line 131 (F21 derived opening) | Agrees; the section view of the figure is drawn to its stated 10 px per mm (wall 25 px, opening 100 px, overmold 86 px) |
| CELL 3.2.5: BAT+ divider k = 0.333, 2.80 V at 8.4 V, 67 kohm Thevenin; MID divider k = 0.680, 2.96 V at 4.35 V | 100/300; 100/147; 200 kohm parallel 100 kohm | Agrees |
| CELL 3.2.8: 25 mohm x 2.2 A = 55 mV per contact | arithmetic | Agrees (current value itself: finding 6) |
| Every L1 value quoted in a section 3.2 row with its TBR marker (REQ-SYS-004, 008, 011 to 013, 017, 018, 037, 043, 047 to 056, 059, 064, 071 to 074, 076, 078, 081 to 089, 091 to 093, 096 to 100, 106, 107, 116, 149, 151 to 153, 157 to 159, 162, 163, 166 to 170, 172, 173, 176; REQ-TX-003, 006 to 008, 012, 014, 016) | `description` and `tbr` of each requirement | Agrees; every value that carries TBR in its requirement carries (TBR) in the ICD and a section 6 row |
| NASA identifiers: SWE-134 items a, d, f, g, h, i, j; SWE-210; NPR 7123.1D App. G Table G-4 entrance 6.11 and success criterion 4 | `npr-7150-2d/03-chapter3.md` 3.7.3 [SWE-134] a to l, 3.11.8 [SWE-210]; `npr-7123-1d/13-appendixg.md` line 80 ("Interfaces with external systems are identified and preliminary definitions are ready to be baselined"; "System Interfaces with external entities and between major internal elements have been identified, including system security expectations") | Exist and are used correctly |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Every figure rendered beside its source and the author states it was inspected | Yes | Five PNGs in `docs/icd/figures/` beside `render_icd_figures.py`; each ICD section 3.1.1 states "rendered and inspected 2026-09-25"; `--check` exit 0 |
| R2 | `tools/traceability.py` shows every `REQ-SW-*` in scope allocated to a design element | N/A | ICD stubs are not software design units; the ICD pairing trace is checked under CK-DES-I5 |
| R3 | The requirements the design implements are Active or the brief names the CR | N/A | Pre-SRR: every requirement is Draft by rule (08 section 3.1 Status); stubs are reviewed before the functional baseline and baselined at PDR (02 section 3.5 Baseline and change row) |
| R4 | The author's return lists the acceptance criteria and the self-check | Yes | The author summary supplied with the assignment states the template outline, the fill rule of 02 section 3.5 Creation row, the TBR count per ICD, the scripted section 4 and identifier checks and the Security expectations rows |

## Participants

Author: the ICD author invocation of 2026-09-25 named in each ICD owner field (absent). Reviewer: `reviewer:icds` (this invocation). Software assurance reviewer: not required by 07 section 2.1.1 (see above). Owner: disposition of every finding.

## A. to H. Software design sections

Items CK-DES-A1 to CK-DES-H4: **N/A** (the product is a set of ICDs; the completion criteria of the checklist assign section I to an ICD and mark the others N/A).

## I. Interface control documents (SE-18; SE HB section 6.3, App. L; 02 section 3.5; T-22)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| CK-DES-I1 | Identity and order; owner is the author of side `<A>` | Yes | File names equal front matter `id`; `side_a` CTL, CTL, TX, CTL, PWR are module tokens; `side_b` KEY, PHONES, ANT, USB, CELL are external tokens of 02 section 3.5 Identity row; module first, external token second (Order row). Section 1.3 Owner row of each names the author of side A, with Claude as acting author of the stub |
| CK-DES-I2 | Outline follows the template; every 3.2 subsection filled, Preliminary or Not applicable with a reason | Yes | Heading lists identical to `docs/templates/icd.md` (reviewer check above). Every 3.2 subsection reads **Preliminary** with a table, or "Not applicable" with its reason (for example KEY 3.2.1 "no item crossing the plane is carried by the radio"; ANT 3.2.5 "the antenna port carries RF power only"). Both Security expectations rows are present in every file: KEY fills 3.2.5 and points 3.2.6 to it; USB fills 3.2.6 and points 3.2.5 to it; PHONES, ANT and CELL mark both Not applicable with a reason (02 section 3.5 Content row; template comment) |
| CK-DES-I3 | Definition tables complete for the kind; every value has a unit; no placeholder; every estimate carries (TBR) and a section 6 row with owner, plan and close_by (CDR at the latest) | No | Tables are complete for each kind (pins, levels, timing, connector, envelope, protection, security) and every (TBR) has a row with owner, plan and close_by PDR (one CDR row in USB). Defects in derived values: KEY bias current and contact voltage (finding 2), KEY DC abuse dissipation (finding 3), KEY pad configuration (finding 4), KEY and USB security basis (finding 5), CELL discharge current (finding 6), CELL sense ranges (finding 7), ANT brass values on a stainless jack (finding 9) |
| CK-DES-I4 | Rendered figure for every physical interface, inspected, agreeing with the tables | No | Five figures exist and are current (`--check` exit 0) and were opened by the reviewer. KEY, PHONES, ANT and CELL figures agree with their tables apart from the values carried from findings 2 and 6. USB front view claims "to scale (20 px per mm)" but draws the receptacle at about half size (finding 8) |
| CK-DES-I5 | Pairing (T-22): an `interface`-tagged requirement of side `<A>` cites the ICD; each side states its value; section 4 lists exactly the citing requirements | No | Section 4 of each ICD lists exactly the citing requirements (reviewer check above: 20 of 20, all tagged `interface`). No side-A requirement exists for any of the five: `docs/requirements/ctl/` and `docs/requirements/pwr/` do not exist (due PDR), and `docs/requirements/tx/requirements.json` exists but none of REQ-TX-003, 007, 008, 012, 014, 016 carries `ICD-TX-ANT` in `design_refs` (finding 1). Each ICD section 4 states the gap and the route |
| CK-DES-I6 | External constraints cited (SI-NNN or CON-NNN that fixes the external item) | Yes | KEY 1.3: SI-018, SI-034, CON-012 (SI-034 text "standard 3.5 mm TRS (aux) plugs" verified in `stakeholder-inputs.md` line 42). PHONES 1.3: CON-013, SI-005. ANT 1.3: SI-008, CON-015 and antenna report F7. USB 1.3: SI-022, CON-010, SI-007. CELL 1.3: SI-023, CON-011. Each side B row of section 4 quotes the defining text verbatim (checked against `stakeholder-inputs.md` and `expectations.json`) |
| CK-DES-I7 | Section 5 names the case for each side's interface requirement, or TC pending with the test-author sprint | Yes | Each section 5 names a TC-SYS case for every citing requirement (KEY TC-SYS-026, 033, 058, 074; PHONES TC-SYS-056, 057, 074; ANT TC-SYS-058, 072, 040; USB TC-SYS-050, 074, 090 plus TC-SW-TOOL-001 with credit false; CELL TC-SYS-058) and "TC pending" for the side A L2 requirements with the PDR test author (02 rule WR-11) |
| CK-DES-I8 | Change status after PDR names its CR; definition-table changes Class I | N/A | Pre-baseline drafts (status Draft, baseline null, revision A); each section 1.3 states the Class I rule for changes after PDR |

## J. Hardware design products

Items CK-DES-J1 to CK-DES-J10: **N/A** (no schematic, PCB, enclosure CAD or BOM in the product).

## Findings (filled by the reviewer)

Severity: Major = blocks baseline or violates the charter, a schema, a governing process document or a NASA requirement; Minor = fix before the next review. No finding is Major: the stubs are not baselined at SRR (02 section 3.5 Baseline and change row), no two sides disagree, and no table carries a placeholder. The verdict is NEEDS CHANGES because this assignment grants APPROVED only with zero findings.

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| F-01 | reviewer | Minor | CK-DES-I5 | section 4 of all five ICDs; `docs/requirements/tx/requirements.json` REQ-TX-007 | No side-A `interface` requirement cites any of the five ICDs; for ICD-TX-ANT the TX L2 file exists and states port values without the ICD in `design_refs` | Open | | Open: not fixed and not deferred. `docs/requirements/tx/requirements.json` still has no requirement tagged `interface` with `ICD-TX-ANT` in `design_refs` (checked with Python 2026-09-25); all five ICDs keep `requirements_a: []`; each section 4 records the deferral to PDR as proposed to Robin and says the row stays open until an owner decision reference exists; none exists in `decisions-for-owner.md`, `package.md` or `rfa-rid-log.json` (no INSP-012 hit). Closes on the TX tagging (ICD-TX-ANT) or an owner decision naming PDR (all five) |
| F-02 | reviewer | Minor | CK-DES-I3 | ICD-CTL-KEY 3.2.4 current column and derivation paragraph; 3.2.7.1 Cross-plugging row; figure left panel | Bias current and contact voltage carried from the superseded network without the 1.0 kohm series resistor | Verified | | Closed: KEY lines 77, 138, 141 (0.30 mA over 11.0 kohm; 0.33 V at the pad, 0.03 V at a 100 ohm contact; the 0.33 mA and 0.07 V figures marked superseded), line 197 cross-plugging 0.30 mA; figure left panel "Sinks up to 0.30 mA", "(0.30 mA, harmless)" and note box, inspected |
| F-03 | reviewer | Minor | CK-DES-I3 | ICD-CTL-KEY 3.2.7.1 DC abuse row | Clamp and resistor dissipation figures are internally inconsistent and omit the source impedance | Verified | | Closed: KEY line 194 states the 50 mA (TBR) source limit, R1 8 to 28 mW with the TVS conducting and 69 mW with the TVS open (sizing case), TVS about 45 to 47 mA and 0.3 to 0.4 W, and that no continuous rating is shown; section 6 line 264 carries the dissipation analysis at PDR and the REQ-SYS-049 bench-limit route. Arithmetic re-derived: (6.5 to 9 - 3.7) V / 1.0 kohm = 2.8 to 5.3 mA; 50 mA x 6.5 to 9 V = 0.31 to 0.43 W |
| F-04 | reviewer | Minor | CK-DES-I3 | ICD-CTL-KEY 3.2.5 tip row, 3.2.6 register row; figure pad box | Pad configuration omits OD = 1 of the E9-safe configuration | Verified | | Closed: KEY line 149 (3.2.5 tip row) and line 177 (3.2.6 register row) give OD = 1 with ISO = 0, matching keyer-verification F4; figure pad box reads "IE 1, SCHMITT 1, OD 1, PUE 0, PDE 0, ISO 0", inspected |
| F-05 | reviewer | Minor | CK-DES-I3 | ICD-CTL-KEY 3.2.5 Security expectations Basis and section 6 row "Security expectations, logging requirement"; ICD-CTL-USB 3.2.6 Basis and 2.2 risk row | Security basis names a missing `cyber` risk that the register now carries (RSK-060) and omits RSK-061 | Verified | | Closed: KEY line 68 (section 2.2) and line 169 Basis cite RSK-060 (tag `cyber`, plan SEP16-KEY); the cyber-tag open question is gone from section 6 (line 263 keeps only the logging TBR); USB line 65 (section 2.2) and line 166 Basis cite RSK-061 (plan SEP16-DIAG); both ids and tags confirmed in `docs/risk/register.json` |
| F-06 | reviewer | Minor | CK-DES-I3 | ICD-PWR-CELL 3.1.1, 3.2.4 pack row, 3.2.7.1, 3.2.8; figure threshold panel | Key-down discharge current given as 1.6 to 2.2 A, 2.2 A and 2.1 A in one file, against 1.3 to 2.1 A in HZ-007 and 1.59 to 1.9 A in the PA research | Verified | | Closed: CELL lines 73, 136, 146, 176, 196 carry one bound, 1.3 to 2.1 A (TBR), sourced to HZ-007 and pa-device-candidates F19 (1.9 A at 6.0 V plus about 10 percent); fuse hold at least 2.1 A; contact drop 25 mohm x 2.1 A = 53 mV; the ADR-005 1.6 to 2.2 A figure is marked not used; section 6 line 241 names the PDR budget check of the 2.2 to 2.5 A upper-tolerance case; figure threshold panel reads 1.3 to 2.1 A and "2.1 A pulses", inspected |
| F-07 | reviewer | Minor | CK-DES-I3 | ICD-PWR-CELL 3.2.5 BAT+ and MID rows | Sense levels state the operating window, not the range the sense path must measure | Verified | | Closed: CELL lines 154 and 155 separate the operating window from a measurement range of 0 to 8.70 V (BAT+) and 0 to 4.35 V (MID), with withstand to -8.70 V and -4.35 V through a pin clamp (42 uA and 86 uA re-derived through 200 kohm and 47 kohm with a 0.3 V Schottky drop); ADC pin at 8.70 V x 0.333 = 2.90 V and 4.35 V x 0.680 = 2.96 V, inside 3.3 V; section 6 line 242 carries the TBR; figure ADC box updated, inspected |
| F-08 | reviewer | Minor | CK-DES-I4 | ICD-CTL-USB figure, front view panel; `render_icd_figures.py` line 620 | Receptacle drawn at about half size in a panel titled "to scale" | Verified | | Closed: `render_icd_figures.py` lines 618 to 620 draw the receptacle 160 x 52 px, 8.0 x 2.6 mm at 20 px per mm (display F21 width; height marked Low confidence in the legend and in USB line 119); `--check` exit 0; USB figure front view inspected |
| F-09 | reviewer | Minor | CK-DES-I3 | ICD-TX-ANT 3.2.2 Coupling torque row, 3.2.7.3 Static bending row; figure mechanical panel | Brass-body torque and yield values applied to the specified stainless-body jack; one moment range does not follow from its loads | Verified | | Closed: ANT line 130 states the torque basis (brass 0.45 to 0.56 N m kept, stainless class 8 in-lb about 0.90 N m, datasheet at PDR, REQ-SYS-106 check proposed to the requirements author); line 190 gives 6 to 9 N at 0.40 m for 2.4 to 3.6 N m as brass context and a stainless neck yield above 4.0 N m (TBR); section 6 lines 243 and 244; figure mechanical panel inspected |

### <a id="finding-1"></a>finding-1 (F-01, Minor, Open): side-A pairing absent

02 section 3.5 Pairing row and CK-DES-I5 need at least one `interface`-tagged requirement in the side-A module file with the ICD id in `design_refs`. For CTL (KEY, PHONES, USB) and PWR (CELL) the module files do not exist until PDR, which each ICD states in section 4. For ICD-TX-ANT the file `docs/requirements/tx/requirements.json` exists and REQ-TX-007 ("every antenna-port spurious emission at most 25 uW ...") is a port-plane requirement with a value, but its `design_refs` do not name ICD-TX-ANT and it carries no `interface` tag; ICD-TX-ANT section 4 names REQ-TX-007 as the proposed side-A requirement. T-22 is W at SRR and E at PDR (02 section 8.2 row T-22). **Fix:** the TX requirements author tags REQ-TX-007 (and the other port-plane REQ-TX rows the ICD lists) `interface` with `ICD-TX-ANT` in `design_refs`, and the ICD moves it to `requirements_a`; the CTL and PWR L2 authors do the same at PDR. Route: deferral to PDR with an owner decision reference, or fix before the readiness declaration for ICD-TX-ANT. **Citation:** 02 section 3.5 Pairing row; T-22.

### <a id="finding-2"></a>finding-2 (F-02, Minor, Open): KEY bias current and contact voltage

ICD-CTL-KEY 3.2.4 reads "0.33 mA with the contact shorted (3.3 V over 10 kohm)", the derivation paragraph "sink up to 0.33 mA" and "a 100 ohm contact reads 0.07 V", 3.2.7.1 "0.33 mA, inaudible", and the figure left panel "Sinks up to 0.33 mA" and "(0.33 mA, harmless)". The network of the same ICD (3.2.5 and the figure) puts R1 1.0 kohm between the jack and the pad node where the 10 kohm pull-up sits, so a shorted contact draws 3.3 V / 11.0 kohm = 0.30 mA, and a 100 ohm contact puts the pad at 0.327 V (`keyer-verification-and-key-input-network.md` F3 row 10 kohm, 1.0 kohm, 100 ohm: 0.327 V, 0.30 mA). The 0.33 mA and 0.07 V figures come from `docs/research/keyer-and-key-interfaces.md` lines 34 and 122, which have no series resistor. The error is on the safe side for the external keyer, but a definition table must state one value. **Fix:** write 0.30 mA maximum sink current and 0.33 V at the pad through a 100 ohm contact (or state the voltage at the contact, 0.03 V); correct the figure text and re-render. **Citation:** keyer-verification F3, F4.

### <a id="finding-3"></a>finding-3 (F-03, Minor, Open): KEY DC abuse dissipation

The DC abuse row states at +12 V "the TVS carries 5.5 mA (36 mW) and R1 30 mW of its 100 mW rating, and D2 holds the pad node at 3.7 V with 8.3 mA into the 3V3 rail". R1 carries the D2 current, so with D2 fitted R1 passes (12 - 3.7) V / 1.0 kohm = 8.3 mA and dissipates 69 mW (69 percent of its rating, not 30 percent). The TVS (TPD2E2U06) sits at the jack, ahead of R1, so its current is set by the abuse source impedance, not by R1: from the REQ-SYS-049 bench case (current limit 50 mA per its verification note) the TVS near its 6.5 V clamp can take about 50 mA, about 0.3 W for 10 min, a continuous rating this row does not show. The arithmetic is copied from `keyer-verification-and-key-input-network.md` F5, which has the same inconsistency. The row is (TBR) with a clamp dissipation analysis at PDR, so the defect is Minor, but the bench case could damage the clamp it verifies. **Fix:** state the abuse source impedance assumed (for example the 50 mA bench limit), give R1 at 69 mW and the TVS power at the clamp voltage, check the TVS continuous rating, and align the REQ-SYS-049 verification note; return the F5 correction to the research owner. **Citation:** keyer-verification F5; REQ-SYS-049 verification note; HZ-010 K1.

### <a id="finding-4"></a>finding-4 (F-04, Minor, Open): KEY pad configuration

`keyer-verification-and-key-input-network.md` F4 gives the E9-safe pad configuration as "IE = 1, SCHMITT = 1, PUE = 0, PDE = 0, OD = 1, ISO = 0; FUNCSEL = SIO". ICD-CTL-KEY 3.2.5 lists IE = 1, SCHMITT = 1, PUE = 0, PDE = 0, FUNCSEL = SIO, and 3.2.6 adds ISO = 0; neither states OD (output disable), and the text says the reset values "are overridden explicitly". The pad configuration is an Inspection item against the datasheet (HZ-010 verification note). **Fix:** add OD = 1 to both rows and the figure, or record why the output driver stays enabled. **Citation:** keyer-verification F4; charter section 9 driver-to-datasheet traceability.

### <a id="finding-5"></a>finding-5 (F-05, Minor, Open): security expectations basis stale

ICD-CTL-KEY 3.2.5 Basis says "no register entry tagged `cyber` covers this row yet (the `cyber` entries are RSK-015 and RSK-022 ...), recorded as an open question for the risk manager", and section 6 row "Security expectations, logging requirement" carries "the cyber-tag question ... answered by the risk manager at SRR". `docs/risk/register.json` (working tree, 2026-09-25) now holds RSK-060 (tag `cyber`, "Crafted key or control input changes radio state or configuration", source 07 section 16.2 row "Keying and control inputs", plan SEP16-KEY) and RSK-061 (tag `cyber`, diagnostic interface command injection). ICD-CTL-USB 3.2.6 Basis cites the 07 section 16.2 row "Diagnostic interface" with RSK-015 only, and section 2.2 lists RSK-015, RSK-033, RSK-055 without RSK-061. **Fix:** cite RSK-060 in the KEY Basis and section 2.2, drop the open question from the section 6 row (keep the logging TBR), and cite RSK-061 in the USB Basis and section 2.2. **Citation:** 07 section 16.2; `docs/risk/register.md` plan rows SEP16-KEY and SEP16-DIAG.

### <a id="finding-6"></a>finding-6 (F-06, Minor, Open): CELL discharge current

ICD-PWR-CELL gives "up to about 2.2 A key-down pulses" (3.1.1), "discharge about 1.6 to 2.2 A key-down pulses at 5 W ... with a fuse or PTC in the pack lead rated for the 2.1 A pulses" (3.2.4), "about 2.2 A" (3.2.7.1) and "a 2.2 A pulse" (3.2.8); the figure repeats "1.6 to 2.2 A" and "2.1 A pulses". HZ-007 (`hazards.json` line 1946) gives 1.3 to 2.1 A and its control text line 2063 the 2.1 A fuse rating; `docs/research/pa-device-candidates.md` F19 (line 76) derives 1.59 A at 7.2 V and about 1.9 A at 6.0 V. The 1.6 to 2.2 A range is the ADR-005 line 18 figure that INSP-011 finding F-07 found unsupported. A fuse sized for 2.1 A against a stated 2.2 A pulse is a contradiction inside one table. **Fix:** adopt one sourced current bound (the F19 derivation with margin, or the HZ-007 value) in every row and the figure, and size the fuse and the contact drop from it. **Citation:** pa-device-candidates F19; HZ-007; INSP-011 finding F-07.

### <a id="finding-7"></a>finding-7 (F-07, Minor, Open): CELL sense-line ranges

The 3.2.5 Level column gives BAT+ sense "6.0 to 8.4 V pack" and MID sense "3.0 to 4.35 V referred to BAT-". The same ICD requires the sense paths to see cells outside that window: the hardware disconnect at 2.50 V per cell (REQ-SYS-084), the rails held off outside 2.5 to 4.3 V (REQ-SYS-166), the charge refusal outside 2.5 to 4.3 V (REQ-SYS-087) and a reversed cell, which pulls the mid-tap out of range (REQ-SYS-086; power report F12). A divider or ADC designed to the stated 3.0 V floor is not bounded for those checks. **Fix:** state the measurement range each sense line must cover (for example 0 to 4.35 V per cell and the reversed-cell excursion with its clamp), separately from the operating window. **Citation:** REQ-SYS-084, REQ-SYS-086, REQ-SYS-087, REQ-SYS-166; power report F12, F14, F15.

### <a id="finding-8"></a>finding-8 (F-08, Minor, Open): USB front view not to scale

The USB figure's lower-right panel is titled "Front view of the wall opening, to scale (20 px per mm)". The opening (240 x 200 px) and the overmold outline (212 x 170 px) are to that scale, but the receptacle is drawn 68 x 18 px (`render_icd_figures.py` line 620), that is 3.4 x 0.9 mm, while `docs/research/display-and-ui-parts.md` line 129 reads the Pico 2 receptacle body as "about 8 mm wide". **Fix:** draw the receptacle at the research dimensions (about 8 mm wide, the height from the same reading, marked Low confidence), or label that element as not to scale; re-render and inspect. **Citation:** display-and-ui-parts F21 and line 129; charter section 11 rule 3.

### <a id="finding-9"></a>finding-9 (F-09, Minor, Open): ANT brass values on a stainless jack

ICD-TX-ANT 3.2.2 specifies a "stainless steel body, 500 mating cycle class (MIL-PRF-39012 class)" jack with a coupling torque of "0.45 to 0.56 N m", and 3.2.7.3 says a "5 to 10 N push at the tip of a 40 cm whip reaches the 2.4 to 3.6 N m yield moment of a brass SMA neck". `antenna-and-erp.md` F8 gives 0.45 to 0.56 N m "for a brass jack in a handheld" and 8 inch-pounds (about 0.9 N m) for the AEP stainless part, and derives the 2.4 to 3.6 N m yield for free-machining brass. The torque value comes from REQ-SYS-106 and the ICD follows it, so the fix routes through the requirements author. Separately, 5 N at 0.40 m is 2.0 N m (F8 table), below the 2.4 N m it is said to reach. **Fix:** state the torque basis for the stainless class jack (datasheet at PDR, section 6 row) and propose the REQ-SYS-106 torque check to the requirements author. Either state the yield moment of the stainless neck, or mark the brass figure as context for the 4.0 N m case. Correct "5 to 10 N" to the load range that reaches the stated moment. **Citation:** antenna-and-erp F8; REQ-SYS-105, REQ-SYS-106.

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 5 ICDs, 1286 lines; 5 figures; 1 render script (769 lines) |
| Checklist items applicable and answered | 8 (CK-DES-I1 to I8): Yes 4, No 3, N/A 1; readiness R1 to R4: Yes 2, N/A 2 |
| Items answered No | CK-DES-I3, CK-DES-I4, CK-DES-I5 |
| Findings by severity | Major 0, Minor 9 |
| Findings fixed, deferred | 0, 0 (iteration 1) |
| Iteration | 1 |
| Effort | 42 turns, 55 minutes |

## Verdict

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Minor] CK-DES-I5 all five ICDs section 4: no side-A interface requirement cites the ICD; REQ-TX-007 exists without ICD-TX-ANT in design_refs.
- [Minor] CK-DES-I3 ICD-CTL-KEY 3.2.4, 3.2.7.1, figure: 0.33 mA and 0.07 V omit the 1.0 kohm series resistor (0.30 mA, 0.327 V).
- [Minor] CK-DES-I3 ICD-CTL-KEY 3.2.7.1 DC abuse: R1 carries 8.3 mA (69 mW), TVS current set by the source, not R1.
- [Minor] CK-DES-I3 ICD-CTL-KEY 3.2.5, 3.2.6: pad configuration omits OD = 1 (keyer-verification F4).
- [Minor] CK-DES-I3 ICD-CTL-KEY 3.2.5 and section 6, ICD-CTL-USB 3.2.6: security basis misses RSK-060 and RSK-061.
- [Minor] CK-DES-I3 ICD-PWR-CELL 3.2.4 and figure: key-down current 1.6 to 2.2 A, 2.2 A and 2.1 A disagree with each other, HZ-007 and PA F19.
- [Minor] CK-DES-I3 ICD-PWR-CELL 3.2.5: sense levels give the operating window, not the 2.5 V and reversed-cell measurement range.
- [Minor] CK-DES-I4 ICD-CTL-USB figure front view: receptacle 3.4 x 0.9 mm in a to-scale panel (body about 8 mm wide).
- [Minor] CK-DES-I3 ICD-TX-ANT 3.2.2, 3.2.7.3: brass torque and yield values on a stainless jack; 5 N at 0.40 m is 2.0 N m.
ITEMS N/A: CK-DES-A1 to H4 (ICD product), CK-DES-I8 (pre-PDR), CK-DES-J1 to J10 (no hardware design product)
MEASUREMENTS: size=5 ICDs, 1286 lines; turns=42; minutes=55; major=0; minor=9
```

## Closure (iteration 2, 2026-09-25)

**Re-review scope.** The author reported F-01 to F-09 fixed and none disputed. The reviewer (`reviewer:icds`, a new invocation in the same role) did not edit the product. It re-read the working-tree blobs named in `product_files` (all five ICDs, the render script; the PHONES figure is unchanged at 92353982, the other four PNGs were re-rendered: KEY dfaaeaf4, USB fd541d5f, CELL 4a0cf3a4, ANT ee75beaf) and checked each fix against its source (keyer-verification F3 to F5, pa-device-candidates F19, HZ-007, display-and-ui-parts F21, antenna-and-erp F8, `docs/risk/register.json` RSK-060 and RSK-061, `docs/requirements/tx/requirements.json`), not against the author's change log.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (query: "peer review record closure block disposition column findings_verified record_status Closed"). `grep -n` then pinned lines in the product files only. The tool was available throughout.

**Checks run at iteration 2.**

| Check | Result |
|---|---|
| `.venv/bin/python docs/icd/figures/render_icd_figures.py --check` | exit 0 |
| Figures opened with the Read tool (KEY, USB, CELL, ANT) | Legible, no overlaps; values agree with the corrected tables (0.30 mA, OD 1, 1.3 to 2.1 A, 0 to 8.70 V and 0 to 4.35 V, 8 x 2.6 mm receptacle, stainless neck row) |
| `tbr_open` against section 6 rows | KEY 14 = 14; PHONES 14 = 14; USB 11 = 11; CELL 22 = 22; ANT 18 = 18 (new rows for the added TBRs: KEY abuse source limit, CELL sense range and current bound, ANT torque basis and stainless yield) |
| Em dash and bare TBD scan of the five ICDs | 0 and 0 |
| `docs/requirements/tx/requirements.json` for `interface` tag or `ICD-TX-ANT` in `design_refs` | none (Python read) |
| INSP-012 in `decisions-for-owner.md`, `package.md`, `rfa-rid-log.json` | no hit |

**Checklist answers at iteration 2.** CK-DES-I3: Yes (findings 2 to 7 and 9 closed). CK-DES-I4: Yes (finding 8 closed; all five figures agree with their tables). CK-DES-I5: No (finding 1 open). Other items unchanged.

**Dispositions.**

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product, state Verified) | 8 (Minor 8) | F-02 to F-09 |
| Disputed accepted (state Withdrawn) | 0 | none disputed |
| Open | 1 (Minor) | F-01: no side-A pairing and no owner decision reference for the PDR deferral; the ICD text itself says the row stays open until that reference exists |

Open Major: 0. Open Minor: 1. F-01 closes by either route of its fix: the TX requirements author tags REQ-TX-003, 007, 008, 012, 014, 016 `interface` with `ICD-TX-ANT` in `design_refs` and ICD-TX-ANT moves them to `requirements_a`; or Robin records a decision (SRR decision list or decision memo) deferring the side-A pairing of all five ICDs to PDR, after which the finding is Deferred and entered as a `RID-SRR-NNN` in `docs/reviews/SRR/rfa-rid-log.json` (07 section 10.2).

Residual outside the product (not a finding against the ICDs): the keyer-verification F5 arithmetic (R1 30 mW with D2 fitted) remains in `docs/research/keyer-verification-and-key-input-network.md` and the REQ-SYS-049 verification note still names the 50 mA bench limit without the TVS dissipation caveat; both are returned to their owners as cross items.

```
VERDICT (iteration 2): NEEDS CHANGES
FINDINGS:
- [Minor] CK-DES-I5 all five ICDs section 4: side-A pairing absent; neither the TX tagging nor an owner deferral reference exists.
MEASUREMENTS: size=5 ICDs, 1295 lines; 5 figures; 1 render script (773 lines); verified=8; open=1; major_open=0; minor_open=1; iteration=2; turns=62; minutes=80
```

The verdict stays NEEDS CHANGES because 07 section 10.2 completion criteria require every Minor finding fixed or deferred with an owner decision reference. `record_status` stays `Open` for the software lead, who sets `Closed` once F-01 is Verified or Deferred.

## Iteration 3 (2026-09-26, review baseline HEAD `adcfe09`, SRR package items R8, H11 and H17)

**Scope and independence.** A new invocation of the reviewer role (`reviewer:icds`); it did not edit the product. It re-opened F-01 to F-09 against the committed blobs named in `product_files` (read with `git show HEAD:<path>`), not against the author's change log or the package text. The iteration 2 blobs of ICD-CTL-KEY (`0560bd89`) and ICD-TX-ANT (`ca2081dc`) are not in the object store (`git cat-file` fails), so the changed text since the iteration 2 quotes could not be diffed; both files were therefore read in full at HEAD (KEY `5e9f1888`, 273 lines; ANT `394d8bff`, 267 lines). PHONES, USB, CELL, the render script and the five PNGs are byte-identical to the iteration 2 blobs.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-012 ICD stubs side-A pairing deferral to PDR owner decision F-01"; "decision defer side-A ICD pairing CTL PWR to PDR INSP-012 lien"). `grep -n` was used afterwards only to pin lines in known files. The tool was available throughout.

**Checks run at iteration 3.**

| Check | Result |
|---|---|
| `.venv/bin/python docs/icd/figures/render_icd_figures.py --check` | exit 0 |
| Figures opened with the Read tool (ICD-TX-ANT, ICD-CTL-KEY; the other three are the blobs inspected at iteration 2) | Legible, no overlaps; KEY: 0.30 mA, OD 1, 50 mA abuse source limit; ANT: stainless neck above 4.0 N m (TBR), brass 2.4 to 3.6 N m as context. The figures carry no requirement lists, so the section 4 changes do not touch them |
| `.venv/bin/python tools/traceability.py --report-only` | exit 0; 237 requirements, 170 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125, REQ-SYS-148; not ICD related) |
| TX L2 file at HEAD (Python read of `git show HEAD:docs/requirements/tx/requirements.json`) | REQ-TX-003, 007, 008, 012, 014, 016 carry tag `interface` and `ICD-TX-ANT` in `design_refs` (lines 104, 252, 289, 439, 512, 588); no other REQ-TX cites the ICD |
| Section 4 against the citing requirements (every `docs/requirements/**/requirements.json` at HEAD) | Equal for PHONES, USB, CELL and ANT. **Not equal for KEY:** REQ-SW-KEYER-019, 020, 021, 022, 024, 026, 028, 036 and 038 name `ICD-CTL-KEY` in `design_refs` (`docs/requirements/sw/sw-keyer/requirements.json` lines 547 to 1120) and are absent from KEY section 4 and `requirements_other` (finding-10) |
| Side-A statements of ICD-TX-ANT section 4 | 6 of 6 verbatim with the `description`, method Test equal to `verification_method`; TC-TX-003, 007, 008, 012, 014, 016 exist and cite their requirement |
| Identifier existence (every REQ, TC, HZ and RSK id in the five ICDs at HEAD) | All resolve; front matter `hazard_ids` equal the HZ ids in each body; HZ-007 still reads 1.3 to 2.1 A and the 2.1 A fuse rating (CELL F-06 basis unchanged) |
| `tbr_open` against section 6 rows | KEY 14 = 14; PHONES 14 = 14; USB 11 = 11; CELL 22 = 22; ANT 18 = 18 |
| Em dash and bare TBD scan of the five ICDs | 0 and 0 |
| Citations re-verified in the corpus | SWE-134 items g and j (`npr-7150-2d/03-chapter3.md` lines 201 and 205) and SWE-210 (line 315), as cited in KEY 3.2.5 |

**Disposition of every finding at HEAD.**

| Finding | Severity | Disposition | Evidence at HEAD |
|---|---|---|---|
| F-01 | Minor | ICD-TX-ANT part **Closed**; CTL and PWR part **Lien: fix before PDR** | ANT line 11 `requirements_a` lists REQ-TX-003, 007, 008, 012, 014, 016; line 51 and line 209 state the pairing; lines 213 to 218 quote the six statements verbatim; the TX file tags them (lines above). KEY line 221, PHONES section 4, USB section 4 and CELL section 4 still defer the side-A pairing to PDR, when `docs/requirements/ctl/` and `docs/requirements/pwr/` are written; T-22 is W at SRR and E at PDR (02 section 8.2). The residual is Minor and is carried as a lien under the convergence rule, so no owner decision reference is needed for this record |
| F-02 | Minor | Closed (re-verified) | KEY lines 77, 138, 141, 197 (0.30 mA over 11.0 kohm; 0.33 V at the pad and 0.03 V across a 100 ohm contact; superseded figures named); figure left panel |
| F-03 | Minor | Closed (re-verified) | KEY line 194 (50 mA (TBR) source limit, R1 8 to 28 mW with the TVS conducting and 69 mW with it open, TVS 45 to 47 mA and 0.3 to 0.4 W, rating not shown) and line 264 (PDR dissipation analysis and the REQ-SYS-049 route); arithmetic re-derived |
| F-04 | Minor | Closed (re-verified) | KEY line 149 and line 177 carry OD = 1 with ISO = 0; figure pad box "OD 1" |
| F-05 | Minor | Closed (re-verified) | KEY line 68 and line 169 cite RSK-060 (tag `cyber`, SEP16-KEY); line 263 keeps only the logging TBR; USB section 2.2 and 3.2.6 Basis cite RSK-061 (blob unchanged since iteration 2) |
| F-06 | Minor | Closed (re-verified) | CELL blob unchanged since iteration 2 (lines 73, 136, 146, 176, 196: 1.3 to 2.1 A (TBR)); HZ-007 at HEAD still gives 1.3 to 2.1 A |
| F-07 | Minor | Closed (re-verified) | CELL blob unchanged (lines 154, 155, 242) |
| F-08 | Minor | Closed (re-verified) | Render script blob `5e0027af` unchanged (lines 618 to 620); USB PNG `fd541d5f` unchanged; `--check` exit 0 |
| F-09 | Minor | Closed (re-verified) | ANT line 130 (torque basis, stainless 8 in-lb context, PDR datasheet check), line 190 (6 to 9 N for 2.4 to 3.6 N m as brass context; stainless neck above 4.0 N m (TBR)), section 6 lines 248 and 249; figure mechanical panel |
| F-10 (new) | Minor | Lien: fix before PDR | finding-10 below |
| F-11 (new) | Minor | Lien: fix before PDR | finding-11 below |

No new Major defect was found. The KEY and ANT text read in full at HEAD agrees with its sources where checked (KEY bias, abuse and pad rows; ANT section 4 statements, methods, cases and TBR rows).

<a id="finding-10"></a>**finding-10 (F-10, Minor, Lien: fix before PDR): KEY section 4 omits the SW-KEYER requirements that cite it.** Location: ICD-CTL-KEY front matter line 13 and section 4 (lines 219 to 234). Nine L2 requirements name `ICD-CTL-KEY` in `design_refs`: REQ-SW-KEYER-019, 020, 021, 022, 024, 026, 028, 036 and 038 (`docs/requirements/sw/sw-keyer/requirements.json` lines 547, 577, 611, 646, 709, 770, 837, 1064, 1120). The ICD names them in section 2.1 (line 51) and in the 3.2.5 Security expectations Basis (line 169), but section 4 and `requirements_other` list only the six L1 requirements, while line 234 states that "the lists here equal" the front matter and are checked by T-22 against `design_refs`. 02 section 3.5 Owner row makes a third module that cites the ICD a citing module, not a side, and rule T-22 (02 line 493) requires "the ICD's section 4 lists exactly the requirements that cite it". T-22 is W at SRR (the `ICD_SECTION4_MISMATCH` check is not yet implemented, 02 line 562), so the defect is Minor. **Fix:** add the nine SW-KEYER ids to `requirements_other` and as `other` rows of section 4 with their verbatim statements and methods, or have the SW-KEYER author move the reference to `ICD-CTL-SW` at PDR if the boundary belongs there. **Citation:** 02 section 3.5 Owner and Pairing rows; T-22; CK-DES-I5.

<a id="finding-11"></a>**finding-11 (F-11, Minor, Lien: fix before PDR): ICD-TX-ANT side-A rows point at the wrong section and the change history misses the F-01 edit.** Location: ICD-TX-ANT section 4 lines 214 to 216, section 5 line 236, section 7 line 267. The "Section 3.2 rows it depends on" column gives "3.2.4 spurious at the port" for REQ-TX-007, 008 and 012, but the conducted spurious row is in 3.2.7.1 (line 174), not 3.2.4 (lines 142 to 148). Section 5 line 236 still calls TC-TX-003 to 016 cases of "related TX L2 requirements" although those requirements are now the side-A rows. The change history (line 267, dated 2026-09-25) records "F-01 (side-A proposal)" while line 209 says the tagging was applied 2026-09-26; the 2026-09-26 edit has no history row. **Fix:** point the three rows at 3.2.7.1, label the TC-TX row as the side-A cases, and add a change-history row for the 2026-09-26 edit. **Citation:** `docs/templates/icd.md` sections 4, 5 and 7; 02 section 3.5 Content row; CK-DES-I5.

**Checklist answers at iteration 3.** CK-DES-I1, I2, I3, I4, I6, I7: Yes (unchanged, confirmed at HEAD). CK-DES-I5: No, carried by liens F-01 (CTL and PWR side A at PDR), F-10 and F-11; Yes for ICD-TX-ANT side A. CK-DES-I8: N/A.

**Lien table** (convergence rule of 2026-09-26, charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline; each lien is carried by the package as a Routine item).

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 residual (CTL side of KEY, PHONES, USB; PWR side of CELL) | Minor | Lien: fix before PDR | CTL and PWR L2 authors, with the ICD author moving the new ids to `requirements_a` in the same change | PDR (T-22 becomes an error under `--gate PDR`) |
| finding-10 | Minor | Lien: fix before PDR | ICD author (Claude); SW-KEYER requirements author if the reference moves to `ICD-CTL-SW` | PDR readiness declaration |
| finding-11 | Minor | Lien: fix before PDR | ICD author (Claude) | PDR readiness declaration |

**Cross items (outside this record's scope, returned to their owners).** (1) Package `docs/reviews/SRR/package.md` line 100 (H11) says only that F-01 awaits verification, and line 1283 (success criterion 4.4-4) says row 17 cannot be Met with a lien while F-01 is open; the package author reconciles both with this disposition (TX part Closed, CTL and PWR residual a Minor lien) and with the 01 section 12.2 rule that a Hard item may not be a lien. (2) The keyer-verification F5 arithmetic and the REQ-SYS-049 verification note (iteration 2 residual) remain with their owners. (3) The missing ICD row in the 07 section 2.1.1 criticality table (iteration 1 process issue) remains with Claude.

**Result.** Findings 11 (Major 0, Minor 11): 8 Closed (F-02 to F-09, Verified), F-01 Closed for ICD-TX-ANT with its CTL and PWR residual a lien, and F-10 and F-11 liens. Open Major 0. Readiness R1 to R4 still hold. Under the convergence rule the verdict is APPROVED with liens. `record_status` stays `Open` for the software lead.

```
VERDICT (iteration 3): APPROVED (with liens)
FINDINGS:
- [Minor] CK-DES-I5 KEY, PHONES, USB, CELL section 4: CTL and PWR side-A pairing deferred to PDR. Lien: fix before PDR (ICD-TX-ANT part Closed).
- [Minor] CK-DES-I5 ICD-CTL-KEY section 4 and requirements_other: nine citing REQ-SW-KEYER ids not listed (T-22). Lien: fix before PDR.
- [Minor] CK-DES-I5 ICD-TX-ANT section 4, 5, 7: spurious rows point at 3.2.4 not 3.2.7.1; TC-TX labelled related; no history row for the 2026-09-26 edit. Lien: fix before PDR.
MEASUREMENTS: size=5 ICDs, 1300 lines; 5 figures; 1 render script (773 lines); verified=8; lien=3; open_major=0; iteration=3; turns=92; minutes=120
```
