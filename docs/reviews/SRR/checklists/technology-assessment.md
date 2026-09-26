---
id: INSP-014
checklist: peer-review-checklist-design
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/technology-assessment.md
product: docs/plan/technology-assessment.md
# product_commit: last commit that touched the product; iteration 2 re-reviews the uncommitted revision 2 on top of it
product_commit: "4e3f891"
# product_blob: git hash-object of the reviewed file on 2026-09-25 (iteration 2; iteration 1 blob 97bb4c94ed67208150399b3df22a7f2ee1f5c91f)
product_blob: "bcd7b9d41b6d643b1a652edd3711a08b8864e2ee"
product_size: 417 lines, 9 sections, 22 element assessments, 27 matrix rows, 7 roll-up rows, 13 heritage rows, 10 tool rows
sprint: SRR-prep
author_agent: author:tech (Claude, lead systems engineer, commit 4e3f891)
reviewer_agent: reviewer:tech
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 5
findings_minor: 3
findings_open: 1
findings_fixed: 0
findings_verified: 7
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: iteration 2 answers (iteration 1: CK-DES-G1, CK-DES-H1, CK-REQ-G1, CK-REQ-G7)
items_no: [CK-DES-H1, CK-REQ-G7]
# effort: cumulative over iterations 1 (40 turns, 35 min) and 2 (14 turns, 15 min)
effort_turns: 54
effort_minutes: 50
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-014: technology readiness and heritage assessment

**Product:** `docs/plan/technology-assessment.md`, blob `97bb4c94ed67208150399b3df22a7f2ee1f5c91f` (unchanged since commit `4e3f891`). **Checklist:** `docs/templates/peer-review-checklist-design.md` revision B, as assigned. **Criterion judged:** SRR entrance row 20 of `docs/process/01-lifecycle-and-reviews.md` section 4.3 (Hard: "Technology readiness and heritage assessment, including toolchain proof"; evidence form "TRL-style table; toolchain sanity-check results"; G-4 6.16, 6.17; G-3 5.9), and review package `docs/reviews/SRR/package.md` section 2 item H1 (the technology assessment needs its record) with row 20 and item H12. **Reviewer:** reviewer:tech, independent of the author. **Date:** 2026-09-25. **Verdict:** NEEDS CHANGES (5 Major, 3 Minor).

**Verdict (iteration 2): NEEDS CHANGES.** The author reported F-01 to F-08 fixed and none disputed. Seven are Verified closed (F-01, F-03 to F-08). F-02 (Major) stays Open on a narrowed residual: the SRR TV set of 05 section 13 has grown to ten records since iteration 1 and the product still lists nine. Readiness R4 still fails (no author self-check on record). The section tables below are the iteration 1 answers; the iteration 2 answers are in "Closure (iteration 2)".

**Checklist fit.** The assigned design checklist targets software architecture, ICDs and hardware; its sections A to F, I and J do not apply to a technology assessment. `docs/process/08-agent-briefing.md` section 3.1 (technology assessment row) and section 3.5 ("plans, process documents and the technology assessment (section G)") name `peer-review-checklist-requirements.md` section G for this product. This record therefore answers the applicable design items (G, H) and, as supplementary evidence, CK-REQ-G1, G7 and G8. The mismatch is reported to Claude as an open question; it is not a product finding.

**Search.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every `grep`; grep was used only to pin lines the semantic hits pointed at.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>F-01 (finding-1) | reviewer | Major | CK-DES-H1, CK-REQ-G1 | Sections 1.1, 2, 3 (every "n-equiv" cell), 7 | The "TRL-equivalent" scale equates simulation with TRL 4 ("Breadboard ... LTspice or S-parameter simulation"; "breadboard = a simulation deck with checkers") and lets firmware reach 5-equivalent by "a whole-binary emulation scenario". This contradicts NPR 7123.1D App. E (TRL 4 hardware: "A low fidelity system/component breadboard is built and operated"), NPR 7123.1D section 5.1.6 (other maturity measures mapped back to TRLs), SEMP section 6.0 (DML-2 to DML-8; DML-4 and DML-5 are both hardware TRL 3; firmware DML-5 is the bare Pico 2 dev board) and SEMP Appendix F item F-07. Section 1.1 also attributes to SEMP section 6.0 a rule "any technology below TRL 6 at PDR opens a risk" that section 6.0 does not contain, and section 7 cites "SEMP section 6.0 TRL-equivalent gates (4 by PDR, 5 by CDR)". The hardware-TRL-3-at-procurement-release residual (SEMP section 6.0 gate rule, RSK-008, OQ-SE-006, package decision 11) is not stated. Fix: rename the scale DML-n with the SEMP section 6.0 definitions, add an App. E TRL column for the cwht design, delete the unsourced TRL 6 rule or cite its source, and state the RSK-008 residual. | Verified | | Closed. Section 1.1 now uses the SEMP section 6.0 DML-2 to DML-8 table verbatim in substance (checked against `semp.md` lines 289 to 297) with an App. E TRL column; states that a simulation deck is not a breadboard and hardware in simulation is at most TRL 3; emulation never raises firmware above TRL 4 (also section 3.21). The unsourced TRL 6 at PDR rule is gone ("SEMP section 6.0 contains none"); section 7 now cites the DML gates (hardware TRL 3). The RSK-008 residual is stated in section 1.1 and carried in the section 2.1 roll-up; RSK-008 condition (`register.md` line 371) and SEMP Appendix F item F-12 (`semp.md` line 475) confirm it. Section 8 item 5(b) puts it to the owner (decision 11, OQ-SE-006) |
| <a id="finding-2"></a>F-02 (finding-2) | reviewer | Major | CK-REQ-G7 | Section 5 (toolchain proof table) | Row 20 requires "toolchain sanity-check results". Section 5 marks LTspice, kicad-cli, Rust, Python and OpenSCAD "Demonstrated" from research runs, but `tools/toolchain.lock.md` section 1.1 records the sanity checks for kicad-cli, LTspice, rustc and cargo, picotool, the venv Python with jsonschema, and OpenSCAD with FreeCAD as "not yet run, pending" (lock lines 58 to 84). The section omits the FW-B0 toolchain proof `TC-SW-TOOL-001` and its report `docs/vv/reports/TC-SW-TOOL-001-r1.md` (now filed, result Blocked: owner flash steps 11 and 12 pending; `tools/sw_gate.sh` fails at G4). Its SRR TV schedule ("SRR (schema and traceability TV)") disagrees with `docs/process/05-configuration-and-data-management.md` section 13, which requires nine SRR TV records: the venv Python with jsonschema, `traceability.py`, `validate_docs.py`, `render_rmm.py`, `render_compliance.py`, `render_risk.py`, `review_trend.py`, `render_deck.py` with the Chromium headless shell, and `git`. The table has no row for `render_deck.py`, Chromium or `git`. Package row 20 is Not met for this reason (item H12). Fix: report each lock section 1.1 check with its result and date, cite `TC-SW-TOOL-001-r1` with its result, and list the nine SRR TV records with status from 05 section 13. | Open | | Open, narrowed. Fixed: section 5.1 reports every lock section 1.1 row with its last run and result, and each cell agrees with `tools/toolchain.lock.md` section 1.1 as read today; section 5.2 cites `TC-SW-TOOL-001-r1` with result Blocked, steps 11 and 12 pending, and the G4 failure (agrees with the report lines 9, 46, 88, 90); section 5.3 tabulates the SRR TV records with status. Residual: the SRR row of `05-configuration-and-data-management.md` section 13 (line 583, working tree) now names ten TV records, adding `tools/render_review_figures.py` with `tools/tests/test_render_review_figures.py` (both files exist). Sections 2 (Tool row), 5.3, 6 (Tools row) and 8 item 3 still say "the nine SRR TV records", so the product again disagrees with 05 section 13 on the SRR TV set, the defect this finding names. Fix: add the tenth row to section 5.3 and change "nine" to "ten" in sections 2, 6 and 8, or raise the difference against 05 |
| <a id="finding-3"></a>F-03 (finding-3) | reviewer | Major | CK-DES-H1 | Section 2 rows "CTL Pico 2 module" and "SW rustos runtime" (the only Green cells); section 3.13; section 1.2; section 4 row 1 | The 6-to-7 rating rests on "rustos boot ... and GPIO driver run on the Pico 2 board (blinky)", citing `docs/research/rustos-toolchain-proof.md` F1 to F5. Those findings cover a host build, `cargo test -p api`, a cross build, an offline application build and a UF2 conversion "without a device". None records an on-board run, and no on-board run exists in the repository: `TC-SW-TOOL-001-r1` steps 11 and 12 (flash and observe) are pending the owner. The Figure G.4-2 reasoning is also misapplied. Section 3.13 claims "the identical unit in the identical configuration", but section 4 row 1 lists "cwht pin map and clock tree added". SE HB App. G (Heritage Systems note) says a changed architecture or environment "drops to TRL 5, at least initially", and TRL 6 or 7 follows only after analysis of the differences. Section 1.2 says an identical unit in an identical configuration is TRL 9, so 6 to 7 matches neither branch. Fix: rate the module and runtime by the evidence that exists (TRL 5 per the G.4-2 second question until the owner's flash run, or a cited on-board result), recolor, and record the difference evaluation. | Verified | | Closed. The Green cells are gone: CTL Pico 2 row is unit TRL 5 (Figure G.4-2 second question) and integration TRL 3, Yellow; the rustos runtime row is DML-3, TRL 3 until `TC-SW-TOOL-001` steps 11 and 12 pass. Section 3.13 states "No on-board run of rustos is recorded", cites the r1 facts (1608 B flash, 8200 B RAM, Blocked; agrees with report lines 9, 46, 88), and adds the difference evaluation table (form and fit, pin map, clock tree, RF environment, supply, stepping) with dispositions. Section 1.2 and section 4 row 1 apply the G.4-2 branch consistently |
| <a id="finding-4"></a>F-04 (finding-4) | reviewer | Major | CK-DES-H1, CK-REQ-G1 | Section 2 "Technology TRL" column (rustos drivers 2, `cwht-core` 2, "DSP TRL 2"), section 2 reading paragraph, section 7 | Section 2 and section 7 conclude "nothing in the radio requires a technology below TRL 6" and "no technology below TRL 6 is required", and 01 section 4.7 marks the G-3 5.8 Technology Development Plan Not Applicable on that basis. But the product's own Technology TRL column carries TRL 2 for three software elements, and section 3.18 and section 3.19 assign App. E software TRL 2 to them as technology. The key SRR finding, which package decision 13 asks the owner to accept, contradicts the table that supports it. Fix: either move these elements to the design-maturity scale and give the technology TRL of the underlying technique with its heritage (for example keyer semantics, Cortex-M33 peripheral drivers), or name them in section 7 with the reason each does not need a Technology Development Plan. | Verified | | Closed. Section 2 Technology TRL column now gives the underlying technique and its heritage (register-level RP2350 drivers 9, keyer and sequencing semantics 9, DSP filtering 9, boot and linker technique 9) and moves cwht code to the DML scale (section 1.1 item 1). The one technique below TRL 6, PIO I2S receive on RP2350 (TRL 5), is named in section 2, section 3.10 and section 7 as an exception with the reason no Technology Development Plan is written at SRR (not baseline, TRL 9 fallback candidate A, loopback planned under RSK-013 S4). The section 7 finding now reads "the cwht baseline requires no technology whose underlying technique is below TRL 6", which the table supports |
| <a id="finding-5"></a>F-05 (finding-5) | reviewer | Major | CK-DES-G1, CK-DES-H1 | Section 2 row "SW rustos drivers (WP-01 to WP-10)"; section 3.18; section 6 row "rustos drivers" | The driver work packages contradict `docs/process/07-software-engineering-plan.md` section 19 and the charter section 6 id scheme `WP-SW-NN`. The product has WP-01 clocks, WP-02 IRQ plumbing, WP-03 TIMER0, WP-04 GPIO, WP-13 hygiene, and "WP-01 to WP-10". 07 section 19 has WP-SW-01 time base and alarms, WP-SW-02 GPIO sampling through SIO, WP-SW-03 PWM, WP-SW-04 ADC, WP-SW-09 NVIC helpers, WP-SW-11 clocks and PLL, and WP-SW-13 optional USB CDC, thirteen in all. The PDR target also differs. 07 section 3.1 (FW-B1 row) plans WP-SW-01 to 07, 09 and 11 "implemented with host mocks and dev-board checks" by PDR. The product sets 4-equivalent for "WP-01 to WP-04" only, "the remaining packages at 3", and dev-board check binaries "by CDR". A PDR gate level stated against the wrong packages cannot be assessed. Fix: use the 07 section 19 ids and the FW-B1 scope, or raise the difference against 07. | Verified | | Closed. Sections 1.1, 2, 3.18, 6 and 8 item 2 use WP-SW-01 to WP-SW-13 with the titles of 07 section 19 (lines 723 to 735 agree, including WP-SW-08 flash write, WP-SW-10 UART, WP-SW-12 CRC-32 in FW-B2 and WP-SW-13 optional) and the FW-B1 PDR scope WP-SW-01 to 07, 09 and 11 of 07 section 3.1 (line 149). The register-ICD column claims (02, 05, 06, 10, 11 yes; 09 partial) agree with 07 section 19. The research report "WP-13" hygiene items are carried as a sprint task with the question put to the 07 author (section 8 item 2) |
| <a id="finding-6"></a>F-06 (finding-6) | reviewer | Minor | CK-REQ-G7 | Header location note; section 3.17; section 3.19; section 3.20; section 5 rows Rust, OpenSCAD, FreeCAD; section 8 items 1 to 4 | Content is stale against sibling products. 01 section 4.3 row 20, section 5.3 row 16, and SEMP sections 3.6 and 6.0 already name `docs/plan/technology-assessment.md` (header note and section 8 item 1). The lock OpenSCAD row now records `/Applications/OpenSCAD-2021.01.app` (section 8 item 2). SEMP section 3.1 now reads "micro-USB connector ... (SI-022)" (section 8 item 3). The lock FreeCAD row reads "installed 2026-09-25", yet sections 3.17 and 5 and section 8 item 4 say "not installed". The lock's second observation lists cargo-llvm-cov 0.9.1, cargo-nextest, cargo-geiger, cargo-deny and cargo-audit, yet sections 3.20 and 5 say "not installed". Sections 3.19 and 3.20 say SWE-219 tailoring is "pending", while charter sections 10 and 12 record SWE-219 as Tailored. Fix: refresh these statements and close section 8 items 1 to 3. | Verified | | Closed. Header now names the product path and revision 2; section 8 item 1 closes the location pointer, OpenSCAD path and SEMP section 3.1 connector items; section 5.4 records the OpenSCAD 2021.01 path and FreeCAD 1.1.3 installed (lock lines 42, 43); sections 3.17, 3.20 and 5.4 say the cargo tools are installed with no sanity check (lock change log line 217); sections 3.19 and 7 say SWE-219 Tailored (charter line 160) |
| <a id="finding-7"></a>F-07 (finding-7) | reviewer | Minor | CK-DES-H1 | Section 2 "Risk links" column; section 7 watch items | Risk links are incomplete. The rustos drivers row omits RSK-013 ("rustos driver work packages not demonstrated on hardware before CDR"), although package section 11 names the driver gap list of section 3.18 as the RSK-013 S1 content. The ME enclosure row omits RSK-044 ("Enclosure CAD pipeline yields a STEP unfit for machining"). The section 7 PIO I2S watch item says "risk or a risk candidate" without an id. SEMP section 5.13 requires a risk for any element below its gate maturity. Fix: add RSK-013 and RSK-044 and name the PIO I2S risk id, or state that none exists. | Verified | | Closed. Section 2 rustos drivers row carries RSK-013, RSK-003, RSK-008; ME enclosure row carries RSK-006, RSK-044; the section 7 PIO I2S watch item names RSK-013 step S4 (register RSK-013 S4 row: PIO I2S receive prototype, CWSEL-10) and RSK-003. RSK-044 exists (register heading "Enclosure CAD pipeline yields a STEP unfit for machining") |
| <a id="finding-8"></a>F-08 (finding-8) | reviewer | Minor | CK-DES-H4 | Section 2; header governing text | There is no subsystem or system roll-up. SE HB App. G Figure G.3-1 assigns subsystem and system TRLs "based on lowest TRL of components and TRL state of integration". Figure G.4-3 text says "The TRL of the system is determined by the lowest TRL present in the system", but the matrix stops at elements. The governing text also omits NPR 7123.1D App. G Table G-4 item 6.17 (updated technology readiness assessment with assets, heritage products and capability gaps), which 01 row 20 cites. Fix: add a per-module and system row with the lowest-level rule, and cite G-4 6.16 and 6.17. | Verified | | Closed. Section 1.3 states the Figure G.3-1 and Figure G.4-3 lowest-TRL rule with the quoted text verified in iteration 1; new section 2.1 gives a per-module and system roll-up (system TRL 2 today, 3 at PDR and at procurement release) with no integration credit taken. The header cites Table G-4 items 6.16 and 6.17 and section 7 dispositions 6.17 and 5.9 |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Figures rendered and inspected | N/A | The product contains no figure; its row 20 evidence form is a table |
| R2 | `REQ-SW-*` allocated to design units | N/A | Not a design product |
| R3 | Implemented requirements Active or CR named | N/A | Not a design product |
| R4 | Author return lists acceptance criteria and self-check | No | No author return exists for this product ("no new authoring this run"); the header lists the governing text and section 8 lists open items, which is not a self-check. `readiness_met: false` records this. |

## A to F. Software architecture, traceability, SWE-134, detailed design, interfaces, cybersecurity

ITEMS N/A: CK-DES-A1 to A8, B1 to B5, C1 to C15, D1 to D13, E1 to E4, F1 to F3. The product is a technology and heritage assessment, not a software architecture or design (checklist scope paragraph).

## G. Reuse and dependencies

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-G1 | No | Section 3.18 names drivers by WP ids that do not exist in `07-software-engineering-plan.md` section 19 and scopes them differently (F-05). The reused rustos runtime is correctly tied to the 07 section 17.1 register (section 4 row 1). |
| CK-DES-G2 | Yes | No external runtime crate is adopted. The `sharp-memory-display` crate is used "for behavior ideas" only, with an own driver against `bus::SpiTx` (section 3.15; section 4 Sharp row). |

## H. Consistency and presentation

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-H1 | No | The product contradicts SEMP section 6.0 and Appendix F F-07 (F-01) and 07 sections 3.1 and 19 (F-05). It is internally inconsistent on the TRL 6 finding (F-04) and on the Figure G.4-2 heritage branch (F-03). |
| CK-DES-H2 | N/A | No figures |
| CK-DES-H3 | Yes | `wc -l`: 326 lines (at most 500) |
| CK-DES-H4 | Yes | Verified in the corpus: NPR 7123.1D App. E TRL rows 1 to 9 (`npr-7123-1d/11-appendixe.md`); section 5.1.6 (`05-chapter5.md` line 42); App. G Table G-3 MCR items 5.8 and 5.9 and Table G-4 items 6.16 and 6.17 (`13-appendixg.md` lines 57 to 80); SE HB Figures G.4-1, G.4-2 and G.4-3 with Green 6 and above, Yellow 3 to 5, Red below 3, the Heritage Systems note and "final TMA ... just prior to PDR" (`nasa-se-handbook/29-appendix-g-technology-assessment-insertion.md` lines 37, 217 to 237, 328 to 374); 47 CFR 97.307(e) 25 µW cap (`regulatory/47cfr-97.307.md`). The G-4 6.17 omission is F-08. |

## I. Interface control documents; J. Hardware design products

ITEMS N/A: CK-DES-I1 to I8 (no ICD), CK-DES-J1 to J10 (no schematic, PCB, enclosure or BOM).

## Supplementary: requirements checklist section G (the checklist 08 sections 3.1 and 3.5 name for this product)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Contradicts SEMP section 6.0 (F-01) and 07 section 19 (F-05). The 01 section 4.7 TDP disposition rests on a finding the product's own table contradicts (F-04). |
| CK-REQ-G7 | No | Tool statements disagree with `tools/toolchain.lock.md`: FreeCAD installed, cargo tools installed, OpenSCAD path recorded, sanity checks not yet run (F-02, F-06). Versions that agree with the lock: kicad-cli 10.0.6, rustc 1.98.0, picotool 2.3.0, jsonschema 4.26.0, OpenSCAD 2021.01, FreeCAD 1.1.3, node v25.9.0, rp2350js `af0114cb`, ltspice 1.0.6, PyLTSpice 6.0.1. The limits the product states honestly are MC/DC for Rust and emulator durations never credited. |
| CK-REQ-G8 | Yes | As CK-DES-H4. No NASA requirement is quoted as a paraphrase. |

## Numbers verified against their sources

| Product claim (section) | Source checked | Result |
|---|---|---|
| Si5351 -127 to -135 dBc/Hz at 10 kHz at HF; -112 dBc/Hz at 156 MHz, secondary and unverified; divider 6 (3.1) | `docs/research/2m-cw-transceiver-reference-designs.md` F16, F17 | Agrees (KX2 -127, QCX -135.6, -112 at 156.2 MHz unverified) |
| LMX2571 -123 dBc/Hz at 12.5 kHz at 480 MHz; about -133 at 144 MHz (3.1) | same report F20 | Agrees |
| Reciprocal mixing about 85 dB with a Si5351 LO (3.1) | same report F15 and decision 9 | Agrees |
| +/-370 Hz error budget (3.1) | `docs/research/regulatory-corpus-and-operators.md` line 217 | Agrees (+/-2.5 ppm at 148 MHz) |
| AFT05MS004N EOL; Newark 1,519, Mouser 72 (3.2) | `docs/research/pa-device-candidates.md` F10 and line 90 | Agrees |
| LPF goals 40 dB at 288 MHz, 35 dB at 432 MHz (3.4) | same report line 70 | Agrees |
| 53.0 dB at 5 W from 97.307(e) (3.4) | `docs/research/part97-regulatory-basis.md` F2; `47cfr-97.307.md` (e): 25 µW cap for 25 W or less; 10 log10(5 W / 25 µW) = 53.0 dB | Agrees |
| 33.5 V peak, 0.67 A at VSWR 3:1, 5 W (3.5) | Arithmetic: Vpk = sqrt(2 x 5 x 50) = 22.36 V; x (1 + 0.5) = 33.5 V; Ipk = 0.447 A x 1.5 = 0.67 A | Agrees |
| Monostable T_max 10 s, 7.5 to 13 s (3.6); pad below 0.6 V with 120 µA E9 leakage (3.14) | `docs/research/keyer-verification-and-key-input-network.md` lines 55 to 59, 295, 297 | Agrees |
| Ladder 98.5 % yield at 1.0 kHz; 15 to 51 % at 500 Hz (3.10) | `docs/research/cw-selectivity-options.md` line 74, decision 6 (14.5 % strict to 51 % relaxed) | Agrees within rounding |
| BQ25887 DigiKey 10,972; Keystone 1043P 10,041 (3.11) | `docs/research/power-tree-and-charging.md` lines 52, 184 | Agrees |
| Via array 7.6 to 4.7 K/W at 25 vias (3.17) | `docs/research/pcbway-export-and-vendor-questions.md` line 267 | Agrees |
| "run on the Pico 2 board (blinky)" (3.13) | `docs/research/rustos-toolchain-proof.md` F1 to F5; `docs/vv/reports/TC-SW-TOOL-001-r1.md` | Not supported (F-03) |
| FreeCAD "not installed"; cargo tools "not installed" (3.17, 3.20, 5) | `tools/toolchain.lock.md` FreeCAD row and change log of the second observation | Stale (F-06) |
| Color bands (1.3) | SE HB Figure G.4-3 text | Agrees |

## Closure (iteration 2)

Re-review of the revision 2 working-tree file, blob `bcd7b9d41b6d643b1a652edd3711a08b8864e2ee`, 417 lines (CK-DES-H3 holds). Every fix was checked against its source, not the author's statement: SEMP section 6.0 DML table and gate rule (`docs/plan/semp.md` lines 289 to 299) and Appendix F items F-07 and F-12 (lines 470, 475); RSK-008 condition, RSK-013 S4 row and RSK-044 (`docs/risk/register.md`); 07 section 19 rows WP-SW-01 to WP-SW-13 (lines 723 to 735) and section 3.1 PDR scope (line 149); `tools/toolchain.lock.md` section 1.1 result cells, OpenSCAD and FreeCAD rows (lines 42, 43) and change log (line 217); `docs/vv/reports/TC-SW-TOOL-001-r1.md` (lines 9, 46, 88, 90); charter SWE-219 row (line 160); 05 section 13 SRR row (line 583). `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every grep.

| Finding | Severity | Author claim | Disposition |
|---|---|---|---|
| F-01 | Major | fixed | Closed (Verified) |
| F-02 | Major | fixed | Open: tenth SRR TV record (`tools/render_review_figures.py`) missing from sections 2, 5.3, 6, 8 item 3 |
| F-03 | Major | fixed | Closed (Verified) |
| F-04 | Major | fixed | Closed (Verified) |
| F-05 | Major | fixed | Closed (Verified) |
| F-06 | Minor | fixed | Closed (Verified) |
| F-07 | Minor | fixed | Closed (Verified) |
| F-08 | Minor | fixed | Closed (Verified) |

Iteration 2 item answers: CK-DES-G1 Yes (07 section 19 ids and FW-B1 scope used; F-05 closed). CK-DES-H1 No (the product disagrees with 05 section 13 on the SRR TV set; F-02 residual; the SEMP, 07, heritage-branch and TRL 6 inconsistencies are closed). CK-DES-H4 Yes (G-4 6.17 now cited; roll-up rule stated). CK-REQ-G1 Yes (SEMP section 6.0 and 07 section 19 agree with the product; the section 7 finding is supported by the table). CK-REQ-G7 No (F-02 residual only; every lock statement now agrees with the lock). Readiness R4 No: no author return with acceptance criteria and self-check is on record for revision 2, so `readiness_met` stays false.

Observed outside the product (not findings against it): `docs/plan/semp.md` line 299 still says this assessment "reports the same levels as a 'TRL-equivalent' column that equates simulation with TRL 4" and Appendix F item F-07 (line 470) is still open, although revision 2 has done what F-07 asks; the SEMP author should close F-07 and drop that sentence. `tools/toolchain.lock.md` section 1.1 has no row for `tools/render_review_figures.py` although 05 section 13 now requires its SRR TV record.

Counts: open Major 1, open Minor 0, Verified 7, Deferred 0. Record stays Open; the verdict turns APPROVED when F-02 is closed and R4 holds.

## Measurements (SWE-089)

Items in the checklist 72 (design) plus 3 supplementary; applicable and answered 9 (CK-DES-G1, G2, H1 to H4; CK-REQ-G1, G7, G8); answered No 4; readiness items 4 (3 N/A, 1 No); findings Major 5, Minor 3; fixed 0; deferred 0; iteration 1; effort 40 turns, 35 minutes.

## Verdict

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-DES-H1 sections 1.1, 2, 7: simulation rated TRL 4-equivalent; adopt SEMP 6.0 DML mapping (F-01).
- [Major] CK-REQ-G7 section 5: no toolchain sanity-check results; TC-SW-TOOL-001-r1 and the nine SRR TV records absent (F-02).
- [Major] CK-DES-H1 section 3.13: Green 6-to-7 rests on an unevidenced on-board run and a misapplied G.4-2 branch (F-03).
- [Major] CK-DES-H1 sections 2, 7: TRL 2 technology cells contradict "no technology below TRL 6" (F-04).
- [Major] CK-DES-G1 section 3.18: WP ids and PDR scope contradict 07 sections 3.1 and 19 (F-05).
- [Minor] CK-REQ-G7 sections 3.17 to 3.20, 5, 8: stale statements against the lock, 01, SEMP, charter (F-06).
- [Minor] CK-DES-H1 section 2: RSK-013, RSK-044 missing (F-07).
- [Minor] CK-DES-H4 section 2: no subsystem or system roll-up; G-4 6.17 not cited (F-08).
ITEMS N/A: CK-DES-A1 to F3, I1 to I8, J1 to J10, H2
MEASUREMENTS: size=26 matrix rows; turns=40; minutes=35; major=5; minor=3
```
