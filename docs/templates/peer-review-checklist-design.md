---
# Peer-review record front matter (charter section 5; docs/process/07-software-engineering-plan.md
# section 10.2). To review a product, copy this whole file to
# docs/reviews/<REVIEW>/checklists/<product-slug>.md: that copy is the single peer-review record
# (there is no peer-reviews/ folder). Fill every field below, answer every applicable checklist item and
# fill the findings table. Both front-matter parsers (PyYAML and the subset parser of
# tools/validate_docs.py) strip a comment on its own line and a comment written after a value
# (" # ..."); this template keeps each comment on its own line for readability, and comment lines
# may stay or be deleted when filing. tools/validate_docs.py checks the record against the field
# list of docs/process/01-lifecycle-and-reviews.md section 13 (its PEER_REVIEW_RECORD_SCHEMA) and
# fails while the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6)
id: INSP-NNN
checklist: peer-review-checklist-design
checklist_revision: B
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/<product-slug>.md
# product: exact path of the design section, ICD, sheet, CAD source or BOM, or CR-NNN
product: docs/design/sw/txseq.md
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: N sections or N design units (N sheets for hardware)
product_size: 9 design units
sprint: SW-NN-<module>
author_agent: <invocation id>
# reviewer_agent: never the author
reviewer_agent: <invocation id>
# criticality: safety-critical | mission-critical | neither (plan section 14.1)
criticality: safety-critical
# assurance_required: true | false, from the table of plan section 2.1.1
assurance_required: true
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: <invocation id>
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: NEEDS CHANGES
# verdict: set by the software lead; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
# assurance_tasks_applied: SWEHB section 7.1 tasks applied, for example [swe-134 7.1 task 4]
assurance_tasks_applied: []
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by the software lead, plan section 10.2)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: design products (software architecture and design, ICDs, hardware)

**Product types:** sections A to H: the software section of `docs/design/architecture.md` (PDR; SWE-057, SWE-143 as tailored), module sections of `docs/design/software-design.md` or `docs/design/sw/<module>.md` (CDR; SWE-058), and design changes by `CR-NNN`. Section I: every interface control document `docs/icd/ICD-<A>-<B>.md`, including the external stubs `ICD-CTL-KEY`, `ICD-CTL-PHONES`, `ICD-TX-ANT`, `ICD-CTL-USB`, `ICD-PWR-CELL` reviewed before SRR (`02-requirements-and-traceability.md` section 3.5; `01-lifecycle-and-reviews.md` section 4.3 row 17). Section J: schematic sheets and PCB layout under `hardware/kicad/`, enclosure CAD under `hardware/enclosure/`, and the BOM under `hardware/bom/` (SEMP sections 5.4 and 7.2). **Governing:** NPR 7150.2D SWE-057 note (structure, qualities, interfaces, components), section 4.2.2 g (valid and invalid states), SWE-058, SWE-134 a to l, SWE-184, SWE-199, SWE-219, SWE-220, SWE-052 (requirements to design, design to code), SWE-154; NPR 7123.1D SE-18 and SE HB section 6.3 and App. L (interfaces); ADR-011 (target platform rules); charter sections 5, 7, 9, 10, 11 rule 3; `docs/process/07-software-engineering-plan.md` sections 2.1.1, 5, 7, 9.6, 14, 16; `docs/process/02-requirements-and-traceability.md` section 3.5 and rule T-22; `docs/templates/icd.md`. **Used by:** an independent reviewer agent; a second, software assurance reviewer where the table of plan section 2.1.1 says Yes. A reviewer answers the sections that apply to the product and marks the others `ITEMS N/A`.

Answer every item Yes, No or N/A with evidence (section, table row, figure). **Major** findings: a requirement not allocated or mis-allocated, a SWE-134 provision missing or weakened, a state or event unhandled, an interface inconsistent with an ICD or the hardware, a budget exceeded, an unverifiable or untestable unit, a design that breaks a target platform rule of ADR-011; for section I an ICD whose sides disagree or whose tables carry a `TBD`; for section J an ERC or DRC error, a part not sourceable, or a missing inspected render. **Minor**: clarity, completeness of a description, missing citation.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, is the single peer-review record for the product (charter section 5; plan section 10.2). Slugs: `design-architecture-sw`, `design-<module>`, `icd-<a>-<b>`, `hw-<sheet-or-part>`, `cr-NNN`. `<REVIEW>` is the next gate the product feeds. The front matter above is the first thing in the file, unfenced.

### Findings (filled by the reviewer and the assurance reviewer)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| F-01 | reviewer or assurance | Major or Minor | CK-DES-xx | section, table row or figure | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

## Readiness criteria

| # | Criterion | Evidence |
|---|---|---|
| R1 | Every figure (block diagram, state machine, timing diagram, ICD figure, schematic sheet, layer view, 3D board, enclosure render) is rendered to a PNG or SVG committed next to its source (`docs/design/`, `docs/icd/`, `hardware/kicad/`, `hardware/enclosure/`; `08-agent-briefing.md` section 1 visual closure rule) and the author states it was inspected (charter section 11 rule 3) | image files beside the source |
| R2 | `tools/traceability.py` shows every `REQ-SW-*` in scope allocated to a design element (`design_refs` filled) and every design unit tagged with the requirements it implements | tool output |
| R3 | The requirements the design implements are `Active` (baselined) or the brief names the CR that changes them | requirement status |
| R4 | The author's return lists the brief's acceptance criteria and the self-check | author return |

## Participants

Author agent (absent); reviewer agent; software assurance reviewer where the table of plan section 2.1.1 says Yes (for this checklist: the software section of the architecture as a whole, and the module design of every safety-critical or mission-critical component or unit of plan section 14.1, including the `pico2` drivers it lists); owner for disposition of deferrals and for PDR and CDR RIDs. The assurance reviewer applies SWEHB topic `6-1` (design for safety checklist) and the `# 7. Software Assurance` section of `docs/references/md/swehb/swe-057-*.md`, `swe-058-*.md` and `swe-134-*.md` (section 7.1 tasks 1, 4 and 6: items a to l implemented, safety-critical elements isolated from non-safety-critical ones, consistency with the hazard analysis), writes its verdict and findings into this record and lists the tasks applied in `assurance_tasks_applied`.

## A. Architecture content (SWE-057 note; NPR 7150.2D §4.2.2)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-A1 | Structure: components are named and each has a purpose, its crate location (`cwht-core`, `cwht-app`, `pico2`) and the `api` traits it consumes; the component list matches plan section 4 or the difference is explained | component table |
| CK-DES-A2 | Quality attributes are quantified: key-to-`PA_EN` latency, element timing jitter, boot-to-safe-state time, scheduler tick and worst-case loop time, flash and RAM budgets, stack budget per task (SWE-199); each timing attribute names its HostUnit (mock clock) and Bench (logic capture) verification, never Emulation (ADR-011) | quality attribute table |
| CK-DES-A3 | External interfaces: every hardware interface (key/paddle inputs, encoder, buttons, LCD bus, synthesizer bus, `PA_EN`, `TR_TX`, charge inhibit, ADC channels, USB bootloader, diagnostic serial) is listed with direction, electrical sense (active-high or low), pull state at reset, and the `ICD-CTL-SW` row it comes from | interface table versus ICD |
| CK-DES-A4 | Internal interfaces: each component boundary is a trait or a typed message with an error type; no shared mutable globals (CS-09) | interface list |
| CK-DES-A5 | States and modes: the state set is enumerated; the transition table covers every (state, event) pair, marking invalid pairs as rejected-and-logged (section 4.2.2 g; SWE-134 b, e) | transition table completeness |
| CK-DES-A6 | Concurrency model of ADR-011 and plan CS-22, CS-23, CS-34 to CS-37: single core; one NVIC priority level for every enabled interrupt, run-to-completion handlers, no nesting and no priority writes; keyer element timing from TIMER0 ALARM0 and 1 kHz input sampling from ALARM1 through SIO (no GPIO edge interrupts); the cooperative main loop dispatched by `SW-SCHED` on the 1 ms tick; each handler's duty and worst-case duration; the shared-data mechanism (atomics or critical section); PWM on slices 0 to 7 only | concurrency section |
| CK-DES-A7 | The safety-critical and mission-critical component and unit list equals plan section 14.1 (including the configuration guard, the `SW-SCHED` dispatcher and the `pico2` clock driver) and the hazard analysis; each unit's criticality is marked in the design | list |
| CK-DES-A8 | Modifiability and the 70 cm path (SI-002): band-dependent constants are isolated in one module and named as such | module boundaries |

## B. Traceability (SWE-052 Table 1; charter section 7)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-B1 | Every `REQ-SW-*` in scope is allocated to at least one design unit; every design unit implements at least one requirement or is justified as infrastructure (scheduler, boot) with the requirement that needs it | allocation matrix in the design |
| CK-DES-B2 | Every hazard `HZ-NNN` with a software control is traced to the component and unit that implements the control | hazard table |
| CK-DES-B3 | Design units map one-to-one to Rust files with the `// @design <module>/<unit>` tag (plan section 3.5, CS-24), so code will trace to design | unit list |
| CK-DES-B4 | `design_refs` in the requirement files name these design units (the reviewer spot-checks three) | requirement files |
| CK-DES-B5 | For a CR: the impact on requirements, tests, ICDs and the unsafe audit is listed | CR record |

## C. Safety design provisions (SWE-134 a to l; plan section 14.2)

Items C1 to C12 apply to every safety-critical and every mission-critical component or unit (SWEHB `swe-134-*.md` section 3.1; plan section 14.1), read against the items plan section 14.2 allocates to it; C13 to C15 apply to safety-critical components and units only.

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-C1 | a. Boot sequence shows the safe outputs (`PA_EN` low, `TR_TX` receive, keyer idle, charge inhibit asserted, audio muted) asserted before any other initialization, on cold start and after watchdog, panic or clock-fault reset; the hardware reset state of `PA_EN` and `TR_TX` (pull-down, active-high) is stated as an assumption traced to the hardware L2 file | boot sequence, assumptions |
| CK-DES-C2 | b. Transition table: the only path to Transmit passes TxPending with its guards; leaving Transmit de-asserts `PA_EN` before T/R changes; illegal transitions are rejected and logged | transition table |
| CK-DES-C3 | c. Every termination path (low battery, over-temperature, fault escalation, operator power-off, panic, watchdog, clock fault, scheduler overrun) calls `safe_state()`; `safe_state()` is specified as infallible, loop-free, callable from interrupt context, and ends with the audio output muted | termination table |
| CK-DES-C4 | d. Transmit requires the key contact and the TX-armed state set by a distinct operator action per power cycle; a lockout override, if the PDR ADR offers one, needs two independent actions on two different controls (03 section 5 item d) and is time-limited and logged; raising the audio level above the default limit and selecting a power step above the lowest need a deliberate action; the ConOps and ICD agree | operator actions section |
| CK-DES-C5 | e. Sequence guards for `PA_EN`, charge enable and configuration write are specified with their prerequisites and the rejection response | guard table |
| CK-DES-C6 | f. Memory integrity: complement-stored flags, periodic CRC of the configuration RAM copy, image CRC at boot, the `SW-SCHED` task table as a flash constant, and the recovery response (safe state, reload, Fault on repeat) are specified with periods | integrity section |
| CK-DES-C7 | g. Input validation (debounce with the make and open times of the `REQ-SW-KEYER` requirement and HZ-010, not a fixed number in the design; rate plausibility; encoder range; ADC ranges and stuck detection; bus read checks) and output read-back (`PA_EN`, `TR_TX` through SIO, synthesizer registers) are specified with the fault response | I/O integrity table |
| CK-DES-C8 | h. The prerequisite check before `PA_EN` is one function with one decision per prerequisite (keyer state, transmit carrier inside 144.001 to 147.999 MHz per REQ-SYS-009, temperature, battery, charge enable de-asserted, T/R settled, TX-armed, guest lock, time-out, duty budget, no Fault) and is listed in the decision table for MC/DC | prerequisite function spec |
| CK-DES-C9 | i. For each hazard a fault tree or argument shows at least two independent events are needed (two GPIO states plus RF drive; the keyer key-down event plus the separately maintained PA-permit flag of the safe-state manager; the hardware PA-enable cutoff; charger IC limits independent of software; hardware thermal cut and headphone level backstop if the hazard analysis requires) | fault trees |
| CK-DES-C10 | j. Time budgets are stated with sampling rates and worst-case paths: over-temperature to `PA_EN` low 100 ms; over-current 10 ms; key-up to `PA_EN` low 2 ms; TX time-out 60 s; under-voltage 1 s; watchdog 100 ms kicked only when every monitor task ran; any different value carries the `TS-NNN` that justifies it; each budget names its Bench logic-capture case | timing table |
| CK-DES-C11 | k. Error taxonomy per module with response class (retry bounded, degrade, safe state, reset) and no discarded error | error table |
| CK-DES-C12 | l. `safe_state()` reachable from every state and by the operator gesture; SafeState display and exit conditions specified | state machine |
| CK-DES-C13 | Decision tables: every boolean decision in a safety-critical unit is listed with its conditions, at most 4 conditions per decision, ready for MC/DC independence pairs (plan section 9.6) | decision table |
| CK-DES-C14 | No floating point in safety-critical units; fixed-point scaling documented (CS-16) | data section |
| CK-DES-C15 | Every decision of a safety-critical unit is in host-compilable code: no decision in `cwht-app` or in `pico2` MMIO, boot or vector-table code other than the board `take()` match (CS-38) | unit list, testability notes |

## D. Detailed design adequacy (SWE-058)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-D1 | Each unit has purpose, public signatures as they will be written (types, error enum, `#[must_use]`), preconditions and postconditions | unit sections |
| CK-DES-D2 | State machines are tables (state, event, guard, action, next state) with every cell filled; timing constants carry units and the requirement id they come from | tables |
| CK-DES-D3 | Data: every field has type, unit, range and invariant; the data dictionary section lists configuration record, event log record and keyer parameters with CRC coverage; no personal data field (plan section 16.6) | data dictionary |
| CK-DES-D4 | Keyer design covers straight key (debounce, direct keying), iambic modes A and B with dit and dah memories, squeeze behavior, weighting, speed range 5 to 50 WPM (SI-033; dot = 1200/WPM ms), and the sidetone path; it names the HSI evaluation result from the dev-board prototype (SI-018) | keyer section |
| CK-DES-D5 | Interrupt handlers are specified with maximum duration, the Bench marker that measures it, and no safety-critical output writes except the safe-state path (CS-22) | ISR table |
| CK-DES-D6 | Resource budgets per unit (flash, RAM, stack) sum to less than the yellow lines of MSR-18, MSR-19 and the stack budget of MSR-16 | budget table |
| CK-DES-D7 | Each unit is testable on the host through the `api` traits with a mock clock, or the design states the Bench case (or the Emulation event-order scenario for ordering) that verifies it and why host testing is impossible | testability note per unit |
| CK-DES-D8 | Predicted cyclomatic complexity per function is at most 15 (CS-17), and 1 for target-only code (CS-38); no recursion; bounded loops (CS-19); no heap (CS-01) | design walk-through |
| CK-DES-D9 | Configuration store and guard: two copies, CRC-32, sequence number, the guard's range check of every safety-relevant field with defaults on failure, write only from task context with interrupts masked and XIP handling per WP-SW-08 | store and guard design |
| CK-DES-D10 | Event log (SWE-210): record set (boot count, reset cause, image CRC result, config load result, safety rejections, panic marker, Fault codes, stack high-water mark, tick overrun counter), ring policy, read-only access | diag design |
| CK-DES-D11 | Audio limiter (HZ-005; plan section 14.2 second table): the output level clamp value and its hardware backstop, the start-up and mode-change ramps, the sidetone amplitude limit, and the mute on PA fault and in SafeState are each specified with the requirement id and the response time (mute within 10 ms) | audio section |
| CK-DES-D12 | Mission-critical units (`SW-SYNTH`, the `SW-TXSEQ` envelope and ALC units, the `SW-CFG` store, `SW-DISPLAY`): transmit carrier limits enforced before every synthesizer write, synthesizer registers read back, the envelope completes its fall before `PA_EN` drops, the ALC set-point is range-checked before every write, configuration is accepted only after the guard with defaults on failure, and the displayed frequency is rendered from the value written to the synthesizer (plan section 14.2 second table) | synth, envelope, config and display sections |
| CK-DES-D13 | `SW-SCHED` and the clock driver (safety-critical, plan section 14.1): task table as a flash constant, per-task periods and deadlines, the watchdog-kick decision, overrun response; TICKS enable and bounded XOSC and PLL waits with the clock fault path (CS-37) | scheduler and clock sections |

## E. Interfaces and ICD consistency (charter section 5; SE-18)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-E1 | Every GPIO, ADC channel, PWM slice (0 to 7 only), I2C or SPI instance and pin number used in the design equals `ICD-CTL-SW` and the rustos board definition (`Rp2350Pins` names) | ICD versus design |
| CK-DES-E2 | Register-level behavior relied on (alarm semantics, ADC FIFO, PWM wrap, I2C timeouts, TICKS) cites the RP2350 datasheet section or the rustos ICD page | citations |
| CK-DES-E3 | Timing across the interface is consistent with the hardware L2 files (T/R switch settle time, synthesizer lock time, ADC sample rate) | hardware L2 |
| CK-DES-E4 | Diagnostic interface choice (UART or USB CDC) matches the PDR ADR | ADR |

## F. Cybersecurity (SWE-154, SWE-156, SWE-157 as tailored)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-F1 | Every mitigation of plan section 16.2 has a design location: image CRC trailer check, configuration integrity, key line confined to the keyer, read-only diagnostics, SWD handling per ADR | design sections |
| CK-DES-F2 | No parser of free-form data and no command channel exists in the image other than the bootrom (CS-30) | interface list |
| CK-DES-F3 | Buffers are fixed-size with capacity constants; no unbounded copy (CS-31) | data section |

## G. Reuse and dependencies (SWE-211, SWE-027)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-G1 | Every rustos feature used appears in the third-party register (plan section 17.1) with its contract test, or a work package of plan section 19 delivers it | register, WP table |
| CK-DES-G2 | No external runtime crate is introduced (CS-02) | dependency list |

## H. Consistency and presentation

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-H1 | The detailed design does not contradict the architecture, this plan or an Accepted ADR (ADR-011 in particular); each difference is a finding with both sentences quoted | architecture, ADRs |
| CK-DES-H2 | Figures rendered and legible; every figure referenced in text; state names in figures equal the tables | images |
| CK-DES-H3 | Files at most 500 lines; index file links sub-files | `wc -l` |
| CK-DES-H4 | Citations name only corpus identifiers that exist; datasheet citations give section and page | vector search (`mcp__claude-context__search_code`, charter section 11 rule 1), then `grep -n` to pin |

## I. Interface control documents (SE-18; SE HB section 6.3, App. L; 02 section 3.5; T-22)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-I1 | Identity and order: file `docs/icd/ICD-<A>-<B>.md` with id `ICD-<A>-<B>`; `<A>` and `<B>` are module tokens in the charter order `RX, TX, PWR, CTL, ME, SW` or, for an external interface, `<B>` is one of `KEY`, `PHONES`, `ANT`, `USB`, `CELL`, `HOST` (02 section 3.5 Identity and Order rows); the owner is the author of side `<A>` | file name, section 1.3 |
| CK-DES-I2 | Outline follows `docs/templates/icd.md` (SE HB App. L sections 1.1 to 3.2.8 plus cwht sections 4 and 5); every 3.2 subsection is filled, marked `Preliminary` (stub before SRR) or marked `Not applicable` with a reason | section headings |
| CK-DES-I3 | Definition tables are complete for the interface kind: pins and signal names, electrical levels with tolerances, timing with limits, connector type and pin-out, mechanical envelope and keep-outs, protocol or register map; every value has a unit; no `TBD`; every estimate carries `(TBR)` and a row in the ICD TBR table with owner, plan and `close_by` (CDR at the latest) | section 3 tables |
| CK-DES-I4 | A rendered figure exists for every physical interface (connector pin-out, mechanical envelope) beside the ICD and was inspected (charter section 11 rule 3); the figure agrees with the tables | figure file, tables |
| CK-DES-I5 | Pairing (T-22): at least one `interface`-tagged requirement in the module file of side `<A>` (and of side `<B>` when `<B>` is a module) cites the ICD id in `design_refs`; each side's requirement states what that side delivers or accepts at the interface plane with a value; the two sides and the ICD tables agree; section 4 of the ICD lists exactly the requirements that cite it | requirement files, ICD section 4 |
| CK-DES-I6 | External constraints are cited: `SI-NNN` or `CON-NNN` that fixes the external item (SI-018 key and paddle; SI-034 3.5 mm TRS plugs; SI-022 micro-USB; SI-023 18650 cells) in section 2 or 1.3 | citations |
| CK-DES-I7 | Section 5 names the verification case(s) for each side's interface requirement, or `TC pending` with the test-author sprint (02 rule WR-11) | section 5 |
| CK-DES-I8 | Change status: an ICD changed after PDR names its `CR-NNN`; definition-table changes are Class I (02 section 10.2) | header, CR |

## J. Hardware design products (schematic, PCB, enclosure, BOM; SEMP sections 5.4, 7.2; 01 sections 5.3 and 6.3)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-DES-J1 | Schematic sheet: `kicad-cli sch erc` at the locked version (`tools/toolchain.lock.md`) reports zero errors; every warning is listed with a disposition; the ERC report is committed beside the sheet or under `docs/reviews/<REVIEW>/` | `erc-report.json` |
| CK-DES-J2 | Schematic render (PNG or SVG per sheet) exists beside the source and was inspected; nets, reference designators and values are legible; every net that crosses to another sheet or module matches the ICD signal name | render, ICD |
| CK-DES-J3 | Every `REQ-*` the sheet implements is named in the sheet notes or `docs/design/allocation.json` and the `design_refs` of those requirements name the sheet path | allocation, requirement files |
| CK-DES-J4 | PCB: `kicad-cli pcb drc` with the PCBWay rule set (clearance, track width, drill, annular ring, mask expansion, courtyard) reports zero violations; the rule file is committed under `hardware/kicad/` and matches the PCBWay capability record in `docs/research/` | `drc-report.json`, rule file |
| CK-DES-J5 | PCB renders (each copper layer, silkscreen, 3D board) exist beside the source and were inspected; RF signal paths, PA thermal relief, keep-outs and the antenna connector placement match the design notes; the revision silkscreen reads `cwht MB rev<X>` | renders |
| CK-DES-J6 | Enclosure: the STEP file is produced by the lock's path, an OpenSCAD 2021.01 CSG export followed by a `freecadcmd` 1.1.3 STEP export (`tools/toolchain.lock.md` section 1 OpenSCAD and FreeCAD rows and section 1.1 known-answer test; OpenSCAD 2021.01 does not export STEP itself); a rendered view exists beside the source and was inspected; a tolerance note states the PCB pocket, connector cut-out and lid fit tolerances against the drawing and the CNC vendor's capability; the antenna sits on one end (SI-008) | STEP file and its export log, render, tolerance note |
| CK-DES-J7 | Enclosure fit against the PCB outline and connector positions is shown (CAD fit check or printed fit-check part, SI-012) with the result recorded | fit-check record |
| CK-DES-J8 | BOM: every line has manufacturer, MPN, DigiKey (or equivalent) part number, quantity and package; availability and lead time checked on the review date with an approved alternate for every single-source part (01 section 6.3 row 20); through-hole and exposed-pad parts the owner hand-solders are marked per the kit assembly model (SI-031; charter section 12) | BOM file |
| CK-DES-J9 | BOM designator count equals the schematic designator count; PCBWay assembly BOM and CPL columns follow the PCBWay format (05 section 8.2) | BOM, CPL, schematic |
| CK-DES-J10 | Hazard controls allocated to hardware (PA over-temperature cut, PA-enable cutoff, charger limits, pull-downs on `PA_EN` and `TR_TX`, headphone level limit) appear on the sheets and are traced to their `REQ-*` and `HZ-NNN` | sheets, hazards file |

## Completion criteria (SWE-088)

`verdict: APPROVED` when readiness R1 to R4 held, every applicable section is answered (sections A to H for software design, I for an ICD, J for a hardware product; the others marked N/A), zero open Major findings, Minor findings fixed or deferred with an owner decision reference and a gate, the measurements are filled in the front matter, the assurance reviewer returned `APPROVED` where plan section 2.1.1 says Yes, and `.venv/bin/python tools/validate_docs.py` passes on the record itself. At SRR every open Major finding on an ICD stub, and at PDR and CDR every open Major finding, becomes `RID-<REVIEW>-NNN`; on record closure every Deferred finding becomes `RID-<REVIEW>-NNN` in the log of its named gate and is listed in `deferred_rids` (plan section 10.2).

## Verdict format

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-DES-C8 software-design.md section 6.3: prerequisite check omits TX time-out state.
- [Minor] CK-DES-H2 fig-txseq-states.png: state "TX_PEND" differs from table name "TxPending".
- [Major] CK-DES-I5 ICD-CTL-KEY: no interface-tagged REQ-CTL-* cites the ICD in design_refs.
ITEMS N/A: CK-DES-J1 to J10 (software design product)
MEASUREMENTS: size=9 units; turns=4; minutes=25; major=1; minor=1
```
