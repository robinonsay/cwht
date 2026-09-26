# cwht Technology Readiness and Heritage Assessment (SRR)

**Status:** Draft for SRR (initial Technology Maturity Assessment; updated at every review), revision 2 applying the independent review record `docs/reviews/SRR/checklists/technology-assessment.md` (INSP-014, findings F-01 to F-08). **Owner:** Robin (approves). **Author:** Claude (lead systems engineer); independent reviewer agent checks it before SRR. **Governing text:** SE HB App. G (Figure G.3-1 Technology Assessment Process with its component, subsystem and system roll-up; G.4 Establishing TRLs, Figure G.4-1 levels, Figure G.4-2 TMA thought process with its Heritage Systems note, Figure G.4-3 TRL Assessment Matrix with its Green, Yellow and Red bands and its lowest-TRL rule, and the AD2 step for elements below the required maturity); NPR 7123.1D App. E (TRL definitions with hardware and software descriptions) and §5.1.6 (other maturity measures mapped back to TRLs); NPR 7123.1D App. G Table G-4 (SRR) item 6.16 (updated Technology Development Plan) and item 6.17 (updated technology readiness assessment with technology assets, heritage products and capability gaps identified), and the MCR items it absorbs, Table G-3 item 5.8 (Technology Development Plan) and item 5.9 (initial technology readiness assessed with technology assets, heritage products and gaps identified), all dispositioned in section 7; SEMP `docs/plan/semp.md` §6.0 (design maturity levels DML-2 to DML-8, their App. E TRL mapping, the RF gate rule and the insertion rules) and §7.5 (heritage); `docs/process/01-lifecycle-and-reviews.md` §4.3 row 20 (TRL-style table plus toolchain sanity-check results) and §4.7.

Research reports are cited as `docs/research/<file>.md F<n>`; their confidence tags (High, Medium, Low) are carried over where an assessment rests on one finding. Regulatory text is cited from `docs/references/md/regulatory/` (eCFR 2026-09-23). Trade-study identifiers TS-003 to TS-006 in this document are the scopes proposed in `docs/design/concept.md` §11.2 and `TS-NNN-synthesizer-reference` is the synthesizer and reference scope first proposed there as TS-002; a number is taken only when the study file is created (06 §13 item 3) (the filed `TS-001` covers the receiver, selectivity and PA device-and-supply concept and the filed `TS-002` the firmware runtime make/buy), so each reference names its scope.

---

## 1. Method

### 1.1 Two scales, kept apart

SE HB App. G warns that integration lowers the TRL of a unit whose parts are individually mature, and that terms must be defined before levels are assigned. This assessment reports, for every element:

1. **Technology TRL** (NPR 7123.1D App. E): the maturity of the underlying technology, technique or catalog part in the world at large, with the heritage that supports it. A part in mass production and in use in fielded radios is TRL 9. For software elements this is the TRL of the technique (for example register-level RP2350 peripheral drivers, iambic keyer semantics, CW DSP filtering), not of cwht's code, which is design maturity (item 2).
2. **cwht design maturity level (DML)**, the project-defined scale of SEMP §6.0, reported together with the **App. E TRL of the cwht design** that SEMP §6.0 maps each DML to (NPR 7123.1D §5.1.6 permits other maturity measures when they are mapped back to TRLs). The definitions are those of SEMP §6.0 and are repeated here so this assessment can be read alone:

| DML | Hardware definition | Firmware definition | App. E TRL of the cwht design |
|---|---|---|---|
| DML-2 | Concept formulated: block named, part family and interfaces identified (`docs/design/concept.md`) | Function and semantics defined, reference behavior chosen | TRL 2 |
| DML-3 | Analytical proof of the critical function: budget or hand analysis against the requirement | Reference model or golden vectors exist; datasheet ICD extracted for the driver | TRL 3 |
| DML-4 | Simulation-verified: LTspice or S-parameter simulation of the block with pass/fail checkers against the budget, catalog parts and vendor models | Logic in `cwht-core` passing HostUnit tests against `cwht-hal-mock` | Hardware TRL 3 (no hardware built); firmware TRL 4 |
| DML-5 | Simulated in context (layout parasitics and component tolerances estimated), or the function measured on a vendor evaluation board on the owner's bench | Firmware image running on a bare Pico 2 development board (Bench, `credit: false`) | Hardware TRL 3 when simulated only, TRL 4 when measured on an evaluation board; firmware TRL 5 when the end-to-end image runs on the dev board, otherwise TRL 4 |
| DML-6 | Assembled cwht board meets its requirements on the bench after TRR | Firmware on the assembled board through the first-power-on procedure | TRL 6 |
| DML-7 | Unit in its enclosure operated on air after the on-air delta TRR | Same | TRL 7 |
| DML-8 | SAR complete: acceptance recorded, V&V report closed | Same | TRL 8 |

App. E TRL 4 hardware requires that "a low fidelity system/component breadboard is built and operated"; a simulation deck is not a breadboard. A hardware design that exists only in simulation is therefore at most TRL 3, whatever the simulation's fidelity (SEMP §6.0), and Emulation evidence does not raise firmware above TRL 4 (only an image running on the dev board gives firmware TRL 5). Terms for cwht: laboratory environment = the owner's bench or the host for software; relevant environment = the Pico 2 development board or a vendor evaluation board on the owner's bench with the owner's instruments; operational environment = the enclosed unit on air; breadboard = a physical article built and operated on the bench (for cwht, a vendor evaluation board or breakout); brassboard = the first assembled cwht board; prototype = unit `CWHT-A-001`.

**Gate levels.** RF hardware blocks follow the SEMP §6.0 gate rule: DML-4 by PDR and DML-5 by CDR, both hardware TRL 3; an RF block below its gate DML opens a risk and a fallback alternative from its trade study. This assessment applies the same DML-4 by PDR and DML-5 by CDR as planning targets to the non-RF hardware blocks; a miss there is reported in the delta table of section 9. Firmware follows `docs/process/07-software-engineering-plan.md` §3.1: the FW-B1 work packages (WP-SW-01 to WP-SW-07, WP-SW-09 and WP-SW-11) and the keyer prototype reach DML-5 (dev-board checks) by PDR; a per-package check binary or the keyer prototype maps to firmware TRL 4, and firmware TRL 5 is reached only when the end-to-end `cwht-app` image runs on the dev board (SEMP §6.0 mapping), and the SEMP §6.0 rustos insertion rule opens a risk with a fallback for any driver not demonstrated on the dev board by CDR. No further TRL threshold at PDR applies (SEMP §6.0 contains none).

**Recorded residual: hardware TRL 3 at procurement release.** Because no RF breadboard is built before the CDR procurement release (the first hardware build follows CDR; charter §3), every RF block is at App. E hardware TRL 3 when PCBWay and DigiKey orders are placed. This is carried by RSK-008, whose condition states it (SEMP §6.0; SEMP Appendix F item F-12). The owner decides at SRR whether to accept it as a recorded residual of RSK-008 (OQ-SE-006; SRR package `docs/reviews/SRR/package.md` decision 11; reconfirmed in the CDR decision memo). The hardware reaches TRL 6 only at DML-6, on the assembled board after TRR.

### 1.2 Heritage thought process

For each heritage product the Figure G.4-2 questions are asked in order. An identical unit operated in the identical configuration and environment is TRL 9. An identical unit operated in a different configuration or system architecture initially drops to TRL 5 until the differences are evaluated (Figure G.4-2 second question; the SE HB App. G Heritage Systems note adds that TRL 6 or higher follows only when analysis shows the new architecture or environment is sufficiently close to the old one). A merely similar design is treated as new and enters at the design-maturity level its analysis supports. SEMP §7.5 adds the project rule: no circuit or algorithm is inherited without re-analysis; heritage supplies starting points and independent evidence, not credit.

### 1.3 Colors and roll-up

Per SE HB Figure G.4-3: Green = TRL 6 and above, Yellow = TRL 3, 4 and 5, Red = below TRL 3. Colors are assigned to the **App. E TRL of the cwht design today** (the DML mapped per section 1.1); the technology TRL column shows why a Red today is design work and not a technology gap. Per Figure G.3-1 and the Figure G.4-3 text ("The TRL of the system is determined by the lowest TRL present in the system"), each module row of section 2.1 carries the lowest element TRL of that module, lowered further if its elements have never been integrated as a unit; the system row carries the lowest module TRL. Enabling products (tools, instruments) are listed for completeness but are rated by their validation status, not by TRL, and are excluded from the roll-up.

## 2. Summary matrix

| Module | Element | Technology TRL (basis) | cwht DML today | App. E TRL of cwht design today | Color today | Required at PDR | Required at CDR | Risk links |
|---|---|---|---|---|---|---|---|---|
| TX | Frequency generation: TCXO plus Si5351A or LMX2571 | 9 (parts in production; section 3.1) | DML-3 (phase noise and error budget derived) | 3 | Yellow | DML-4 (TRL 3), synthesizer trade study (concept §11.2 synthesizer and reference scope, `TS-NNN-synthesizer-reference`, number assigned at creation) decided | DML-5 (TRL 3) | RSK-002, RSK-005 |
| TX | Exciter, driver and PA device (concept TS-003 scope) | 9 (devices); AFT05MS004N EOL with stock | DML-2 (no model, no circuit) | 2 | Red | DML-4 (TRL 3) with a behavioral model | DML-5 (TRL 3) | RSK-001, RSK-005, RSK-006 |
| TX | Gate-bias ALC and envelope shaper (concept TS-006 scope) | 9 (technique in production radios) | DML-2 | 2 | Red | DML-4 (TRL 3) | DML-5 (TRL 3) | RSK-001, RSK-012 |
| TX | Harmonic LPF | 9 (technique) | DML-3 (attenuation goals derived) | 3 | Yellow | DML-4 (TRL 3) with vendor SRF models | DML-5 (TRL 3) | RSK-011 |
| TX | T/R relay and sequencing (HF3 class) | 9 (part) | DML-3 (stress and timing derived) | 3 | Yellow | DML-4 (TRL 3) | DML-5 (TRL 3) | RSK-005 |
| TX | Hardware PA-enable cutoff and TX inhibits | 9 (parts) | DML-3 (timing derived) | 3 | Yellow | DML-4 (TRL 3) | DML-5 (TRL 3) | RSK-012 |
| TX | Antenna port SMA, boss retention, counterpoise lug | 9 (part) | DML-3 (load data collected) | 3 | Yellow | DML-4 (tolerance stack; TRL 3) | DML-5 (fit-check print; TRL 4) | none open |
| RX | Front end: BPF, LNA, mixer | 9 (parts) | DML-2 | 2 | Red | DML-4 (TRL 3) | DML-5 (TRL 3) | RSK-008 |
| RX | Selectivity A: commercial 8-pole can, IF, AGC, detector | 9 (part) | DML-2 (quote and data pending) | 2 | Red | DML-4 (TRL 3), selectivity trade study (TS-001) decided | DML-5 (TRL 3) | RSK-005 |
| RX | Selectivity B: 1.0 kHz roofing ladder | 9 (technique) | DML-4 (Monte Carlo with pass/fail run) | 3 | Yellow | DML-4 (TRL 3) | DML-5 (TRL 3) | none open |
| RX, SW | Selectivity B: PCM1808 I2S ADC, PIO I2S receive and DSP | ADC 9 (part); DSP CW filtering and digital AGC 9 (QMX on a Cortex-M4F; section 3.10); PIO I2S receive on RP2350 **5** (proven on RP2040 only; section 7) | DML-2 (no PIO, DMA or I2S driver in rustos; DSP not coded) | 2 | Red | DML-5 for the capture path (PIO loopback with a PCM1808 breakout on a Pico 2; hardware TRL 4, firmware TRL 4), DML-4 for the DSP chain (firmware TRL 4) | DML-5 | RSK-013 (step S4), RSK-003 |
| PWR | Charger, protection, holders, rails | 9 (parts) | DML-3 (current budget and topology) | 3 | Yellow | DML-4 (TRL 3) | DML-5 (TRL 3) | RSK-007 |
| PWR | USB input through the Pico 2 module | 9 (module) | DML-2 (path unrated) | 2 | Red | DML-5 by measurement on a Pico 2 (TRL 4) | same | none open |
| CTL | Pico 2 module and RP2350 | 9 (module in mass production) | DML-3 (pin budget and clock-harmonic analysis; section 3.13) | Unit: 5 (Figure G.4-2 second question: identical unit, different configuration); integration into cwht: 3 | Yellow | Difference evaluation of section 3.13 closed; PCBWay assembly confirmation sent | DML-5 (TRL 4) with the vendor reply | RSK-004 |
| CTL | Key input network, ESD, jacks | 9 (parts) | DML-3 (network derived) | 3 | Yellow | DML-4 (TRL 3) | DML-5 (bounce capture on a Pico 2; TRL 4) | RSK-012 |
| CTL | Display, encoders, buttons | 9 (parts) | DML-2 | 2 | Red | DML-4 (driver goldens, panel stack; TRL 3 hardware, TRL 4 driver) | DML-5 | none open |
| CTL | Audio: PWM, reconstruction, TPA6132A2 | 9 (parts); PWM audio heritage with noise history | DML-2 | 2 | Red | DML-4 (TRL 3) | DML-5 (TRL 3) | none open |
| ME | CNC 6061 enclosure, thermal pedestal | 9 (service and material) | DML-3 (thermal chain derived; smoke shell rendered) | 3 | Yellow | DML-4 (model, quote; TRL 3) | DML-5 (STEP accepted, fit print; TRL 4) | RSK-006, RSK-044 |
| ME | 4-layer PCB, stackup, via fill | 9 (PCBWay standard) | DML-3 (stackup and impedance estimate) | 3 | Yellow | DML-4 (board-thickness trade study, concept TS-004 scope; TRL 3) | DML-5 (DRC clean; TRL 3) | RSK-004 |
| SW | rustos runtime as it exists (boot, vectors, linker, GPIO) | 9 (Cortex-M boot, vector table and linker-script technique fielded in the pico-sdk and `cortex-m-rt`; section 3.13) | DML-3 (image built for the cwht toolchain and inspected; no on-board run recorded) | 3 until `TC-SW-TOOL-001` steps 11 and 12 pass; then 5 | Yellow | DML-5 (TRL 5): `TC-SW-TOOL-001` run with steps 11 and 12 passed | DML-5 | RSK-013, RSK-010 |
| SW | rustos drivers cwht needs (WP-SW-01 to WP-SW-12 of 07 §19; WP-SW-13 optional) | 9 (register-level RP2350 peripheral drivers fielded in the pico-sdk; `rp235x-hal` and `embassy-rp` as open-source Rust instances, TS-002 firmware runtime make/buy alternatives A1 and A2) | DML-2 (DML-3 for the packages whose register ICD rustos already holds) | 2 | Red | DML-5 (dev-board check per package; firmware TRL 4) for the FW-B1 set WP-SW-01 to 07, 09 and 11 (07 §3.1); WP-SW-08, 10 and 12 at DML-3 | DML-5 for every package (WP-SW-08, 10 and 12 in FW-B2); firmware TRL 5 with the end-to-end image | RSK-013, RSK-003, RSK-008 |
| SW | `cwht-core` logic: keyer, sequencer, safety manager | 9 (keyer semantics fielded in K1EL WinKeyer, K3NG and YACK; T/R sequencing and hang time fielded in QRP Labs QCX and QMX; section 3.19) | DML-3 (golden vectors defined; FW-B0 skeleton builds) | 3 | Yellow | Keyer and debounce DML-5 (host-tested and dev-board keyer prototype with sidetone, 07 §3.1 FW-B1; firmware TRL 4, not the end-to-end image); sequencer and safety manager DML-3 | DML-5 | RSK-012, RSK-010 |
| SW | Host-first method (`cwht-hal-mock`) | 9 (host unit testing against injected device models is general practice) | DML-4 (FW-B0 host tests 10 of 10, 100 % line and region coverage; `TC-SW-TOOL-001-r1`) | 4 | Yellow | in use | in use | RSK-010 |
| Tool | Emulator `ACC-EMU-001` | enabling product (characterized) | accreditation case written, not approved | not rated | Yellow | ADR and accreditation | scenarios | RSK-003 |
| Tool | LTspice batch, kicad-cli, Rust toolchain, Python stack, OpenSCAD plus FreeCAD, render_deck with Chromium, git | enabling products (in use) | research demonstrations; lock §1.1 checks partly recorded; SRR TV records TV-001 to TV-010 filed, not yet accredited (section 5.3) | not rated | Yellow | the ten SRR TV records of 05 §13 (filed as TV-001 to TV-010, Validated; independent review INSP-015 and owner accreditation pending) before the SRR readiness declaration; PDR TV set | CDR TV set | RSK-009, RSK-010 |
| Bench | tinySA Ultra, logic capture, fixtures | enabling product (commercial) | purchase committed; attenuator and capture unverified | not rated | Yellow | procedures written | instruments in hand at TRR | RSK-011 |

### 2.1 Module and system roll-up (Figure G.3-1; Figure G.4-3 lowest-TRL rule)

No element of any module has been integrated with another as a built unit, so no integration credit is taken and each module carries its lowest element level.

| Level | Lowest App. E TRL of the cwht design today (element) | Color | Lowest technology TRL (element) | Level at PDR if every gate of section 2 is met | Level at CDR procurement release |
|---|---|---|---|---|---|
| TX | 2 (PA line-up; ALC and envelope) | Red | 9 | 3 | 3 (RSK-008 residual) |
| RX | 2 (front end; selectivity A; selectivity B ADC and DSP) | Red | 9 for candidate A; 5 for candidate B (PIO I2S receive on RP2350) | 3 | 3 (RSK-008 residual) |
| PWR | 2 (USB input path) | Red | 9 | 3 | 3 (RSK-008 residual) |
| CTL | 2 (display and UI; audio) | Red | 9 | 3 | 3 (RSK-008 residual) |
| ME | 3 (enclosure; PCB) | Yellow | 9 | 3 | 3 (4 for the fit-check print) |
| SW | 2 (rustos drivers) | Red | 9 | 3 (sequencer and safety manager at DML-3; FW-B1 set at DML-5, TRL 4) | 5 once the end-to-end `cwht-app` image with every package runs on the dev board |
| **System (cwht radio)** | **2** | **Red** | **9 for the baseline; 5 if TS-001 selects candidate B** | **3** | **3, the recorded residual of RSK-008 (section 1.1); TRL 6 at DML-6 after TRR** |

Reading of the matrix: the system is at TRL 2 today, as expected at the SRR of a Phase A project, because several blocks are still at concept level; every Red cell is cwht design work with a named PDR activity in section 6. The underlying technology of every baseline element is at TRL 9. The single element whose underlying technique is below TRL 6 is the PIO I2S receive path of selectivity candidate B, dispositioned in section 7. After PDR the system is held at TRL 3 by the hardware until the assembled board is tested (section 1.1 residual).

## 3. Element assessments

### 3.1 Frequency generation (TX)

- **Heritage.** Si5351A: QRP Labs QCX and QMX, Elecraft KX2, uBITX at HF with measured -127 to -135 dBc/Hz at 10 kHz; at 144 MHz only a secondary, unverified report (-112 dBc/Hz at 156 MHz) exists, and the output divider drops to 6 (`docs/research/2m-cw-transceiver-reference-designs.md` F16, F17). LMX2571: TI positions it for battery PMR radios, datasheet -123 dBc/Hz at 12.5 kHz at 480 MHz, derived about -133 dBc/Hz at 144 MHz; no amateur heritage found (F20). TCXO grades from Epson, Abracon, SiTime and the QRP Labs module (F21). Frequency-error and band-edge analysis: `docs/research/regulatory-corpus-and-operators.md` F7, F8.
- **Technology TRL.** 9 for every candidate part (mass production, DigiKey stock recorded 2026-09-25 for Si5351A and LMX2571).
- **cwht maturity.** DML-3 (App. E TRL 3): the reciprocal-mixing bound (about 85 dB with a Si5351 LO), the +/-370 Hz error budget and the 1 kHz guard are derived; no register plan, no spur analysis in context.
- **Gaps.** Si5351 phase noise at 144 MHz unverified (Medium); LMX2571 closed-loop plots are images not yet extracted; clipped-sine versus square reference penalty couples the synthesizer trade study to the TCXO choice; spur landing map versus 144 to 148 MHz and the IF not computed.
- **Plan to PDR.** Synthesizer trade study (concept §11.2 synthesizer and reference scope, `TS-NNN-synthesizer-reference`, number assigned at creation) with the criteria of `docs/design/concept.md` §11.2; extract LMX2571 plots; measure a Si5351 at 144 MHz on the bench or find the primary source; compute the spur map with the chosen IF; register model of the chosen device as the emulator's I2C or SPI target (`docs/research/rp2350-emulation-options.md` implications). Exit: DML-4 (hardware TRL 3) by an LTspice or Python phase-noise and spur budget with pass/fail against the selectivity set.

### 3.2 Exciter, driver and PA (TX)

- **Heritage.** NXP AFT05MS004N with a full 136 to 174 MHz reference PCB, S-parameters and ADS models behind an NXP account; ST PD54008L-E (AN2048 at 169 MHz, not retrieved); Guerrilla RF GRF5604 (5 V, 450 to 470 MHz evaluation board only); Mitsubishi RD07MUS2B with AN-VHF-053-A harmonic data (excluded by SI-028 unless an authorized BOM-linkable channel appears) (`docs/research/pa-device-candidates.md` comparison table, F21). QRP Labs QCX proves 5 W drain-modulated CW at HF; no vendor provides a SPICE model for any candidate (F6).
- **Technology TRL.** 9 for the devices; AFT05MS004N is End of Life with finite authorized stock (Newark 1,519 and Mouser 72 on 2026-09-25), which is a supply risk, not a maturity gap.
- **cwht maturity.** DML-2 (App. E TRL 2): no line-up, match or model exists for 144 MHz at 7.4 V in cwht's stackup.
- **Gaps.** No SPICE model (behavioral model must be built from S-parameters and datasheet tables); PD54008L-E and GRF5604 technical fit unverified; export and lifetime-buy questions if the EOL device is baselined; RthJC versus the pedestal chain; harmonic data from one lot and one circuit (2011) for the Mitsubishi part is not transferable to another device.
- **Plan to PDR.** Retrieve the ST and Guerrilla documents; PA device trade study (concept TS-003 scope, device choice now inside the filed `TS-001`) with the mandatory criteria of SI-028; build the LTspice behavioral PA model (S-parameter block plus fitted nonlinear transconductance) for each surviving candidate; run output power across 6.0 to 8.4 V, harmonic content into the LPF, and the ramp; owner buys a lifetime reserve if the EOL device is baselined. Exit: DML-4 (hardware TRL 3) by a checked simulation of 5.0 W +/-0.5 dB with ALC and 60 dBc at the antenna port. By CDR: DML-5 (hardware TRL 3) with layout parasitics and the thermal chain (`docs/research/pcbway-export-and-vendor-questions.md` F16, F17). Risks: RSK-001, RSK-005, RSK-006.

### 3.3 ALC loop and envelope shaper (TX)

- **Heritage.** Gate-bias power control is the Mitsubishi RD-series application practice; drain-supply modulation is the QRP Labs QCX practice at 5 W HF; the raised-cosine 5 ms shape is the ARRL and IC-705 class norm; the 26 dB bandwidth computation exists as an 80-line Python script (`docs/research/regulatory-corpus-and-operators.md` F7; `docs/research/keyer-verification-and-key-input-network.md` F11, F12).
- **Technology TRL.** 9 for the techniques.
- **cwht maturity.** DML-2 (App. E TRL 2): node chosen as a baseline, no loop design, no simulation.
- **Gaps.** Loop stability and set-point scaling per power step; whether a bias-only cutoff silences a driven LDMOS (R-KN5 in the keyer verification report); 2f content during the ramp; envelope convention (10-to-90 % versus full transition) to be fixed by ADR.
- **Plan to PDR.** ALC and envelope trade study (concept TS-006 scope) with LTspice transients of the loop and the ramp for each PA candidate, FFT of the envelope with `bw.py` moved into `tools/`, fault cases (bias lost, TX_KEY stuck) to place the cutoff node. Exit: DML-4 (hardware TRL 3) by simulation with pass/fail on 26 dB bandwidth at most 350 Hz and -60 dBc beyond 500 Hz.

### 3.4 Harmonic low-pass filter (TX)

- **Heritage.** Seventh-order or elliptic LPFs at the antenna port are universal practice; the attenuation need (at least 40 dB at 288 MHz and 35 dB at 432 MHz, 0.5 dB insertion loss) is derived from the 60 dBc target and the measured in-band 2fo of a 7 V VHF LDMOS (`docs/research/pa-device-candidates.md` F16, F17); the 53.0 dB limit at 5 W derives from 47 CFR 97.307(e) (`docs/research/part97-regulatory-basis.md` F2).
- **Technology TRL.** 9.
- **cwht maturity.** DML-3 (App. E TRL 3): numbers derived, no topology simulated.
- **Gaps.** Inductor self-resonance and layout leakage erode simulated attenuation; PIN-free path removes the diode-harmonic concern (SI-036); measurement at TRR depends on the tinySA Ultra and an attenuator not yet in the inventory (RSK-011).
- **Plan to PDR.** S-parameter simulation with vendor inductor models and SRF, pass/fail checker in `tools/ltspice_check.py`; NanoVNA S21 of the assembled filter at TRR. Exit: DML-4 (hardware TRL 3) by simulation with 10 dB margin over the goals.

### 3.5 T/R relay and sequencing (TX, interface to RX)

- **Heritage.** Relay T/R is the Elecraft XV144 and Kuhne rationale ("avoid receive performance degradation by diode switches"); TE Axicom HF3 54: 50 W carry, 80 dB isolation at 100 MHz, 3 to 5 ms operate, 1e7 operations, 6 V coil straight from the pack, hot-switch rated (`docs/research/tr-switch-candidates.md` F7, F12; `docs/research/2m-cw-transceiver-reference-designs.md` F8). Semi break-in per SI-036 removes the relay-wear concern of full QSK (F5).
- **Technology TRL.** 9.
- **cwht maturity.** DML-3 (App. E TRL 3): electrical stress at 5 W into VSWR 3:1 (33.5 V peak, 0.67 A), the sequencing envelope (lead-in 5 ms, envelope fall before release) and the fail-to-receive property are derived (F1, F4, F12).
- **Gaps.** Distributor stock and price could not be read by machine (Open item 1 of that report); coil-clamp choice versus release time; second receiver-protection stage sizing; audible click accepted.
- **Plan to PDR.** Owner or PCBWay stock check with timestamps; LTspice transient of the sequencer with the RF envelope; `ICD-RX-TX` timing table; receiver-protection analysis to +17 dBm under a stuck-relay fault. Exit: DML-4 (hardware TRL 3).

### 3.6 Hardware PA-enable cutoff, pull-downs and charge inhibit (TX, CTL, PWR)

- **Heritage.** Retriggerable monostable practice (74LVC1G123, LTC6993-2 alternative); WinKeyer paddle watchdog figure (128 elements); the RP2350 pad reset states and erratum E9 guidance; BQ25887 charge-disable pin (`docs/research/keyer-verification-and-key-input-network.md` F2, F13; `docs/research/power-tree-and-charging.md` F22).
- **Technology TRL.** 9 for the parts.
- **cwht maturity.** DML-3 (App. E TRL 3): T_max 10 s with a 7.5 to 13 s window derived including capacitor DC-bias derating; layered coverage table written.
- **Gaps.** Capacitor derating is part-specific (R-KN1); the cutoff node depends on the PA topology (R-KN5); K spread versus VCC for the '123 not extracted (Low).
- **Plan to PDR.** Fold the cutoff node into the ALC and envelope trade study; choose the capacitor from its vendor DC-bias curve; LTspice of the monostable; bench timing procedure with the logic capture written for TRR. Exit: DML-4 (hardware TRL 3).

### 3.7 Antenna port (TX, with ME)

- **Heritage.** SMA jack conventions of Icom, Yaesu, Kenwood and Alinco handhelds; Amphenol mating-cycle and torque data; measured HT antenna gains and counterpoise effect from KX4O and G4ILO (`docs/research/antenna-and-erp.md` F2, F3, F7, F8).
- **Technology TRL.** 9.
- **cwht maturity.** DML-3 (App. E TRL 3): bending moment 4.0 N.m and 1000 matings stated, boss dimensions derived (wall at least 2.5 mm, 6.55 mm hole, flat, nut clearance).
- **Gaps.** Tolerance stack of a PCB-mount bulkhead jack against the lid hole (ANT-R6); jack datasheets not fetched (HTTP 403); stainless versus brass body.
- **Plan to PDR.** Tolerance analysis in the enclosure model and PCB outline; pigtail alternative documented; owner files the datasheets. Exit: DML-4 (hardware TRL 3); DML-5 at CDR by a printed fit check with the real PCB outline (a low-fidelity physical article built and fitted: hardware TRL 4 for the fit function only).

### 3.8 Receiver front end and mixer (RX)

- **Heritage.** Anglian and Kuhne 144 MHz transverter front ends (SPF5043 or PSA4-5043 LNA, 3-pole BPF, level-17 ring mixer, NF 0.9 to 1.8 dB) and the FT-290R class portable superhet (NF about 7 dB, MDS about -140 dBm in 500 Hz) (`docs/research/2m-cw-transceiver-reference-designs.md` F2, F6, F7). External-noise analysis shows a -144 dBm stretch buys about 1 dB with a handheld whip in residential noise (`docs/research/antenna-and-erp.md` F10).
- **Technology TRL.** 9.
- **cwht maturity.** DML-2 (App. E TRL 2): device class and MDS target chosen; no noise or gain budget, no BPF design, no LNA-off-in-TX network.
- **Gaps.** LNA current versus NF (97 mA versus 30 mA class) unresolved; strong-signal behavior with an external antenna (IIP3, blocking) not budgeted; switching-noise coupling from the 5 V buck and charger into a -140 dBm receiver (`docs/research/power-tree-and-charging.md` F19, F20).
- **Plan to PDR.** Cascade noise and gain budget (Python), BPF and LNA simulation with vendor S-parameters, receiver-protection network, birdie map from the clock plan; fold the LNA device choice into the filed `TS-001`. Exit: DML-4 (hardware TRL 3).

### 3.9 Selectivity candidate A: commercial crystal filter superhet (RX)

- **Heritage.** KVG and Inrad 8-pole cans in decades of CW transceivers; FT-290R and IC-202 single-conversion pattern; QCX-class analog AGC and product detector (`docs/research/cw-selectivity-options.md` F2, F3; `docs/research/2m-cw-transceiver-reference-designs.md` F1, F2).
- **Technology TRL.** 9.
- **cwht maturity.** DML-2 (App. E TRL 2): candidate defined with numbers (400 Hz at -6 dB, 800 Hz at -60 dB, shape factor 2.0, about 118 USD), no quote, no IF chain design.
- **Gaps.** Single-source through-hole cans, quote-only, one item shown discontinued; centre and termination uncertain until measured (NanoVNA at 9 MHz); analog AGC design.
- **Plan to PDR.** Quotes and lead times from KVG and Inrad with case drawings; footprint compatible with both; IF chain simulation. Exit: DML-4 (hardware TRL 3) if selected in `TS-001`; otherwise closed as the recorded fallback.

### 3.10 Selectivity candidate B: roofing ladder, I2S ADC and DSP (RX, SW)

- **Heritage.** Tolerance-designed crystal ladders (Dishal method) are standard homebrew practice; PCM1808 24-bit ADC is a mass-production codec front end (`docs/research/cw-selectivity-options.md` F7, F8, F12). DSP CW filtering with digital AGC is fielded: the QMX runs 48 kS/s I/Q DSP with IIR filters on a Cortex-M4F at 168 MHz, the same class as the RP2350's Cortex-M33 with FPU (F14; AGC pumping behavior of DSP-front-end radios in F13). PIO I2S receive is proven on the RP2040 by community code (`rp2040_i2s_example` PIO programs with double-buffered DMA and its forks, a `rp2040-i2s` crate) and pico-extras provides I2S output; no RP2350 or rustos instance is cited (F14).
- **Technology TRL.** 9 for the ladder technique, the ADC and the DSP technique. PIO I2S receive on the RP2350: TRL 5 by Figure G.4-2 (a similar PIO block on a different chip in a different configuration; differences not yet evaluated). This is the one sub-TRL-6 technique in the assessment; section 7 dispositions it.
- **cwht maturity.** Ladder: DML-4 (App. E hardware TRL 3), because the Monte Carlo generator ran through the LTspice batch with pass/fail on bandwidth and loss (98.5 % yield at 1.0 kHz with +/-30 ppm crystals; 15 to 51 % at 500 Hz, which is why 500 Hz is not carried), with the generator reproducing the analytic loss formula within 0.5 dB and the nominal -3 dB bandwidth within 3 % (`docs/research/sim/cw-selectivity/`, figures in `docs/research/figures/cw-selectivity/`). ADC capture path and DSP: DML-2 (App. E TRL 2): rustos has no PIO, DMA or I2S driver and the DSP chain is not coded.
- **Gaps.** PIO I2S receive on rustos untested and outside the emulator's credited scope; PCM1808 stock at TI zero (LCSC deep, DigiKey reported); crystal parameters assumed, not measured; lot-to-lot Cm shifts bandwidth 20 %; three extra rustos work packages (PIO, DMA, I2S), which are not rows of 07 §19 today and would be added by CR if `TS-001` selects candidate B.
- **Plan to PDR.** PIO I2S loopback prototype on a Pico 2 with a PCM1808 breakout (owner hardware, headless; RSK-013 step S4); DSP filter and AGC as pure host-tested Rust with synthetic tones; re-run the Monte Carlo with the chosen crystal part and measured parameters from ten samples (NanoVNA series-resonance method) once bought; second-source ADC named. Exit: DML-5 for the capture path by a working loopback on the dev board with the vendor breakout (hardware TRL 4, firmware TRL 4, and technology TRL 5 for PIO I2S receive on RP2350 then evidenced rather than inferred) plus DML-4 for the DSP chain by HostUnit tests (firmware TRL 4); otherwise `TS-001` selects A.

### 3.11 Power: charger, protection, holders, rails (PWR)

- **Heritage.** TI BQ25887 datasheet application circuit (2S boost charger, balancing, ADC, DigiKey stock 10,972); ABLIC S-8252 application circuit with dual N-FET; BQ29209 secondary OV; Keystone 1043P holders (10,041 in stock); Pico 2 datasheet VSYS OR-ing figure; TPS62913 and TPS7A20 class regulators with zero DigiKey and Mouser stock on 2026-09-25 (`docs/research/power-tree-and-charging.md` F3, F5, F11, F13, F18 to F20).
- **Technology TRL.** 9 for every part.
- **cwht maturity.** DML-3 (App. E TRL 3): topology drawn, receive and transmit current budgets and the battery-life model exist (F23), safety layering listed (F24 as cited by the report's implications).
- **Gaps.** Rail part stock (second sources); switching-noise residual on the 3.3 V analog rail not simulated; charge termination corrupted by load in receive (mitigated by charge pause); dual-path sense threshold needs calibration analysis; NTC senses board rather than cell temperature with these holders.
- **Plan to PDR.** LTspice of buck output filter plus LDO PSRR against a spur budget from the receiver; second sources for buck and LDO; S-8252 threshold-to-current calculation; digitized discharge curve of the chosen cell replacing the 90 % usable-capacity assumption; `ICD-PWR-CELL` and `ICD-PWR-CTL`. Exit: DML-4 (hardware TRL 3). Risk: RSK-007.

### 3.12 USB input through the Pico 2 module (PWR, CTL)

- **Heritage.** Pico 2 datasheet: VBUS pin 40, D1 bypass, no rating for the micro-USB connector current path beyond the USB default (`docs/research/power-tree-and-charging.md` F2).
- **Technology TRL.** 9 for the module.
- **cwht maturity.** DML-2 (App. E TRL 2) for charging above 500 mA (the path is unrated).
- **Plan to PDR.** Measure voltage drop and temperature of a Pico 2 VBUS path at 0.5, 1.0 and 1.5 A (owner bench, A-PWR-01); the USB charge-current trade study (concept TS-005 scope) decides the policy. Exit: DML-5 by measurement on a Pico 2 used as the vendor evaluation board (hardware TRL 4), or the 500 mA-always alternative closes the item by inspection.

### 3.13 Pico 2 module and RP2350 (CTL), and the rustos runtime (SW)

- **Heritage.** The Pico 2 module is a catalog product in mass production, operated in many fielded designs; its official getting-started guide documents flashing and running a blink image with the pico-sdk (`/Users/robinonsay/rust/rustos/docs/extracted/getting-started-with-pico.md`, "Load and run Blink"). rustos boot metadata, vector table, reset handler, linker script and GPIO driver build for the host and for `thumbv8m.main-none-eabihf` from clean, the application build works offline against the local checkout, and `picotool uf2 convert` and `info` work without a device (`docs/research/rustos-toolchain-proof.md` F1 to F5, all host-side or without a device). The FW-B0 toolchain proof `docs/vv/reports/TC-SW-TOOL-001-r1.md` (2026-09-25, result Blocked, `credit: false`) rebuilt the rustos blinky twice from rustos `c54d35aa`, built `cwht-app` for the target (1608 B flash, 8200 B RAM) and inspected both UF2 images (`picotool info -a`: RP2350, ARM Secure, one image definition block); its steps 11 and 12 (flash and observe on the bare Pico 2) are pending the owner. **No on-board run of rustos is recorded in this repository.** The Cortex-M boot, vector-table and linker-script technique itself is fielded in the pico-sdk and in `cortex-m-rt` (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` alternative A1). Errata: RP2350-E9 rules out internal pull-downs on A2 silicon; stepping of procured modules unknown (`docs/research/rustos-toolchain-proof.md` F11, F12).
- **Technology TRL.** 9 for the module and for the runtime technique.
- **Heritage branch (Figure G.4-2).** The module is an identical unit used in a different configuration: the Figure G.4-2 second question applies, so the unit enters at TRL 5 and stays there until the differences below are evaluated; it does not enter at TRL 9 (identical configuration) or at 6 to 7. The rustos runtime has no recorded operation on the unit, so the heritage branch is not yet open to it: it is rated by its own evidence, DML-3 (App. E TRL 3: image built and its critical properties inspected with non-integrated components, no functional result on the target). When `TC-SW-TOOL-001` steps 11 and 12 pass, the runtime is at DML-5 (firmware TRL 5, end-to-end image on the dev board, SEMP §6.0) and the heritage branch gives the same TRL 5. Neither reaches TRL 6 before DML-6 (assembled board after TRR).
- **Difference evaluation (Figure G.4-2 second question; SE HB App. G Heritage Systems note).**

| Difference (form, fit, function, environment) | Evaluation today | Disposition and closing evidence |
|---|---|---|
| Form and fit: module castellations reflowed or hand-soldered to the cwht board instead of used on headers | PCBWay has no published commitment to reflow castellated modules (R-PCB-02); paste aperture 163 % footprint to be built | PCBWay email (owner sends); footprint qualified from the official KiCad outline with the datasheet Figure 5 pads and rendered; SI-031 hand-solder fallback; RSK-004 |
| Function: cwht pin map | Pin budget fits with margin (`docs/research/rustos-toolchain-proof.md` F14, Medium) | `ICD-CTL-SW` at PDR; blinky on the cwht pin map flashed in FW-B0 (07 §3.2) |
| Function: cwht clock tree (XOSC, PLL_SYS at 150 MHz, TICKS) instead of the pico-sdk defaults | Clock driver does not exist (F10); reset values changed for stepping A3, so every field is written explicitly | WP-SW-11 with its dev-board check (FW-B1, by PDR); clock plan ADR |
| Environment: RF field of a 5 W PA and a -140 dBm receiver on the same board | USB PLL 3rd harmonic and crystal 12th harmonic land on 144.000 MHz (`docs/research/display-and-ui-parts.md` F10) | Clock plan ADR with no in-band harmonics (concept §11 ADR list); birdie map in the receiver budget (section 3.8) |
| Environment: supply from the 2S pack through VSYS OR-ing instead of USB only | Topology from the Pico 2 datasheet figure (section 3.11) | `ICD-PWR-CTL`; USB path measurement (section 3.12) |
| Silicon stepping: A2 versus A3 | E9 affects A2; stepping of procured modules unknown | Design for A2 (external pull-ups, no internal pull-downs; section 3.14) |

  Outcome: none of the differences is shown yet to be "sufficiently close" to a fielded configuration, so the module stays at TRL 5 as a unit and its integration into cwht is DML-3 (TRL 3); the row closes at PDR when every disposition above has its evidence and at TRL 6 at DML-6.
- **Plan to PDR.** Owner performs `TC-SW-TOOL-001` steps 11 and 12 and Claude files run 2; send the PCBWay email (answers in the CDR package); qualify the footprint; design for A2 silicon; clock plan ADR. Risks: RSK-004, RSK-013.

### 3.14 Key input network, ESD clamps and jacks (CTL)

- **Heritage.** Curtis-era key input practice (470 ohm to 1 kOhm series, 5 to 10 ms debounce), K1EL WinKeyer semantics, Elecraft and QRP Labs mono-plug notes; RP2350 pad specifications and E9 leakage; TI TPD2E2U06 (IEC 61000-4-2 level 4); Same Sky SJ1-3535N switched TRS jacks (`docs/research/keyer-verification-and-key-input-network.md` F2 to F6; `docs/research/keyer-and-key-interfaces.md` F1, F7, F11; `docs/research/display-and-ui-parts.md` F17, F19).
- **Technology TRL.** 9.
- **cwht maturity.** DML-3 (App. E TRL 3): the network is derived once with margins (closed-contact pad below 0.6 V including 120 uA E9 leakage, 0.30 mA per line, -5 V to +12 V abuse), debounce vectors D1 to D5 defined.
- **Gaps.** Owner's key and paddle bounce not measured (TBR on 2 ms and 5 ms); RF immunity with a 1 m unshielded lead at 5 W not analyzed (choke impedance at least 500 ohm at 146 MHz proposed in the antenna report); cross-plugging survivability of the headphone amplifier under a permanent short not quantified.
- **Plan to PDR.** `ICD-CTL-KEY` and `ICD-CTL-PHONES` from F4 and F5; common-mode choke analysis; TPA6132A2 short-circuit data; bench procedure TC-KEY-BOUNCE for TRR. Exit: DML-4 (hardware TRL 3) by analysis and HostUnit debounce tests; DML-5 at CDR by the bounce capture on the owner's keys with the second Pico 2 (hardware TRL 4; can run before boards arrive).

### 3.15 Display, encoders and buttons (CTL, ME)

- **Heritage.** Sharp memory LCD in low-power instruments; a Rust `sharp-memory-display` crate (0.3.0) for behavior ideas; Bourns PEC11R and Omron B3F are commodity parts; RF-noise history of OLED and TFT displays in uSDX, (tr)uSDX and uBITX radios motivates the memory LCD (`docs/research/display-and-ui-parts.md` F1, F2, F7, F8, F11, F12, F16).
- **Technology TRL.** 9.
- **cwht maturity.** DML-2 (App. E TRL 2): parts chosen with numbers, no driver, no panel stack, no footprint.
- **Gaps.** ZIF contact side and pinout orientation (classic first-board error); Sharp operating-temperature statements disagree; encoder bushing length versus panel stack; distributor stock unreadable by machine; dark-use readability (no light in rev A).
- **Plan to PDR.** Display driver against `bus::SpiTx` with host golden frame bytes and a PNG framebuffer renderer; footprint and 3D model of the panel and ZIF overlaid on the enclosure window render; panel stack-up fixed; owner stock check at CDR. Exit: DML-4 (hardware TRL 3; driver firmware TRL 4).

### 3.16 Audio chain (CTL, SW)

- **Heritage.** PWM audio in uSDX-class radios (functional, with documented noise and tick problems), DirectPath and capacitor-coupled headphone amplifiers, EN 50332 level norms and measured earbud sensitivities (`docs/research/audio-output-and-hearing-safety.md` F1, F10, F19, F23 to F29).
- **Technology TRL.** 9 for the parts and the technique.
- **cwht maturity.** DML-2 (App. E TRL 2): network values proposed (F27), ceiling numbers derived, nothing simulated.
- **Gaps.** PWM residual and coupling from display SPI, flash and synthesizer activity; TPA6132A2 short-circuit and thermal behavior; multimeter AC accuracy at 700 Hz for the bench ceiling check unknown.
- **Plan to PDR.** LTspice of divider, reconstruction and coupling with a behavioral amplifier model (full-scale sine and worst-case pattern into 32 and 16 ohm, carrier residual, flatness); host test harness for limiter, AGC, fades, sidetone mixing and volume ramps; DNP I2S DAC footprint reserved. Exit: DML-4 (hardware TRL 3).

### 3.17 Enclosure, thermal path and PCB (ME)

- **Heritage.** PCBWay CNC service limits, tolerances and finishes; PCBWay standard 4-layer stackup and DFM limits; IPC-4761 Type VII via fill; the OpenSCAD smoke-test half-shell already rendered and exported (STL, 3MF, CSG, PNG) (`docs/research/enclosure-cnc-and-openscad-pipeline.md` A1 to A11, B2; `docs/research/pcbway-fabrication-and-assembly.md` F5, F6, F9; `docs/research/pcbway-export-and-vendor-questions.md` F14 to F19).
- **Technology TRL.** 9 for the service, material and process.
- **cwht maturity.** DML-3 (App. E TRL 3): thermal chain from junction to enclosure surface derived (via array 7.6 to 4.7 K/W at 25 vias for 1.6 versus 1.0 mm; junction at most 110 C target), impedance estimate for 50 ohm microstrip (0.30 mm first estimate), CNC design rules listed; the enclosure itself is at concept level.
- **Gaps.** No enclosure model; FreeCAD 1.1.3 is installed (2026-09-25, `tools/toolchain.lock.md` FreeCAD row, SI-032) but `tools/scad2step.py` is not yet committed and the OpenSCAD plus FreeCAD sanity check of lock §1.1 has not run, so the STEP stage is unproven (RSK-044); PCBWay tolerance statements conflict (+/-0.125 mm headline versus ISO 2768-m); plating thickness unknown; board thickness undecided (concept TS-004 scope); panelization undecided.
- **Plan to PDR.** Enclosure envelope model with the SMA boss, pedestal, window and bosses; commit `tools/scad2step.py` and run it on the smoke shell with acceptance checks (valid, one solid, no BSpline faces, volume match); instant quotes for the enclosure and for the PCB at both thicknesses with and without via fill; board-thickness trade study. Exit: DML-4 (hardware TRL 3); DML-5 at CDR by the accepted STEP, a clean DRC and an H2C fit-check print (hardware TRL 4 for fit). Risks: RSK-006, RSK-044.

### 3.18 rustos drivers (SW, WP-SW-01 to WP-SW-13 of 07 §19)

- **Heritage.** rustos `api` philosophy (zero-sized handles, `Read`/`Write` traits) and the `pico2` GPIO driver; the RP2350 datasheet address map, reset bits, IRQ numbers and register names for every cwht peripheral extracted (`docs/research/rustos-toolchain-proof.md` F7 to F10, F14, F15, Peripheral to driver map). Register-level RP2350 peripheral drivers are fielded in the pico-sdk and exist as open-source Rust HALs (`rp235x-hal`, `embassy-rp`; `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` alternatives A1 and A2, Low confidence on their characterization); rustos writes its own (ADR-019, SI-033) and reuses behavior, not code.
- **Technology TRL.** 9 for the technique (register-level drivers for these peripherals are in fielded use); the peripherals are TRL 9 silicon.
- **cwht maturity.** DML-2 (App. E software TRL 2: basic properties defined, nothing coded); DML-3 for the packages whose register ICD rustos already holds (07 §19 column "Register ICD available": WP-SW-02 `gpio/`, WP-SW-05 `i2c/`, WP-SW-06 `spi/`, WP-SW-10 `uart/`, WP-SW-11 `clocks/`; WP-SW-09 partial).
- **Work packages (07 §19).** WP-SW-01 time base and alarms (TIMER0), WP-SW-02 GPIO sampling through SIO, WP-SW-03 PWM, WP-SW-04 ADC, WP-SW-05 I2C master, WP-SW-06 SPI master, WP-SW-07 watchdog, WP-SW-08 flash write, WP-SW-09 critical section and NVIC helpers, WP-SW-10 UART, WP-SW-11 clocks and PLL (safety-critical, 07 §14.1), WP-SW-12 CRC-32, WP-SW-13 USB CDC (optional, Rev B unless an ADR says otherwise).
- **Gaps.** No clock, interrupt, timer, PWM, ADC, I2C, SPI, watchdog or flash driver exists; WP-SW-11 (clocks, with TICKS enabled explicitly and bounded XOSC and PLL waits, CS-37) and WP-SW-09 (single NVIC priority, CS-34) precede the timer and interrupt-using drivers (schedule risk); register-level drivers are not host-testable without an injectable register-access trait, so their Class A evidence is inspection against the datasheet, host-compilable decision functions (CS-38), the dev-board check and emulation in the credited scope (`docs/research/emulator-accreditation-and-timer-irq.md` F12; RSK-013 step S4 decides the register-access trait at PDR). The rustos repository hygiene items of `docs/research/rustos-toolchain-proof.md` F16 (the research report's "WP-13") have no 07 §19 row; they are carried as a FW-B1 sprint task, not as a work package (section 8 item 2).
- **Plan to PDR (07 §3.1 FW-B1).** WP-SW-01 to WP-SW-07, WP-SW-09 and WP-SW-11 implemented to the `api` trait boundary with host mocks, contract tests, datasheet citations per register access and a dev-board check each (`credit: false`), plus the emulator register-sequence comparison for in-scope peripherals (07 §9.4). Exit at PDR: DML-5 for that set (per-package check binaries: firmware TRL 4; TRL 5 when the end-to-end `cwht-app` image runs on the dev board, SEMP §6.0); WP-SW-08, WP-SW-10 and WP-SW-12 at DML-3 with their ICD pages extracted, reaching DML-5 in FW-B2 before CDR. A FW-B1 package without a dev-board check at PDR entrance is a PDR lien closed at CDR (RSK-013 trigger). Risks: RSK-013, RSK-003, RSK-008.

### 3.19 `cwht-core` application logic (SW)

- **Heritage.** Keyer semantics from the Curtis mode A and B definitions, K1EL WinKeyer 3 mode register and paddle watchdog, K3NG and YACK behavior (behavior only, GPL code not reused); ITU-R M.1677-1 element ratios; golden vectors V1 to V13 and debounce vectors D1 to D5 defined; reference keyer model `keyer_ref.py` proposed as the independent oracle (`docs/research/keyer-and-key-interfaces.md` F3, F4, F12; `docs/research/keyer-verification-and-key-input-network.md` F6 to F8, F14). T/R sequencing, hang time and semi break-in are fielded in the QRP Labs QCX and QMX (section 4).
- **Technology TRL.** 9 for the keyer, debounce and sequencing techniques (fielded in the keyers and radios above). The cwht implementation is design maturity (next item).
- **cwht maturity.** DML-3 (App. E software TRL 3): reference behavior and golden vectors exist, timing tolerance and HostUnit harness (simulated clock at 100 us steps) defined; the FW-B0 workspace skeleton (`cwht-app`, `cwht-core`, `cwht-hal-mock`) builds and its 10 host tests pass (`TC-SW-TOOL-001-r1`), but no keyer logic is coded yet.
- **Gaps.** No keyer code; MC/DC cannot be instrumented by rustc, so SWE-219 is Tailored (charter §10 and §12): independently reviewed decision tables and independence-pair tests, with branch and condition coverage on the date-pinned nightly as a non-credit supporting measure (MSR-14; RSK-010); safety manager, sequencer, DSP and power monitor have no reference models yet.
- **Plan to PDR.** Keyer golden-vector generator checked in under `tools/`; HostUnit tests for the keyer and debounce; keyer prototype on the dev board with PWM sidetone for the owner's HSI evaluation (07 §3.1 FW-B1, SI-018); sequencer model with the T/R timing table; safety-manager state machine with its MC/DC decision tables. Exit: DML-5 for keyer and debounce (dev-board prototype: firmware TRL 4); DML-3 for the rest. Risks: RSK-012, RSK-010.

### 3.20 Host-first verification method (SW, process)

- **Heritage.** rustos methodology (author, reviewer and test-author separation, per-file review, traceability gate); the mock-driver test against `api` as it stands works on the host (`docs/research/rustos-toolchain-proof.md` F13; `docs/plan/semp.md` §7.5).
- **Maturity.** DML-4 (firmware TRL 4): the FW-B0 host crates `cwht-core` and `cwht-hal-mock` build, 10 of 10 tests pass twice with identical result sets, and stable coverage is 100 % of lines and regions (`docs/vv/reports/TC-SW-TOOL-001-r1.md` step results; developer evidence, `credit: false`). The pattern needs the `time::Clock` and `time::Alarm` trait shapes of WP-SW-01 before the keyer can be tested with a simulated clock.
- **Gaps.** cargo-llvm-cov 0.9.1, cargo-nextest 0.9.146, cargo-geiger 0.13.0, cargo-deny 0.20.2 and cargo-audit 0.22.2 are installed (`tools/toolchain.lock.md` second observation, 2026-09-25) but none has a sanity-check result or TV record; the pinned `1.98.0` toolchain of `firmware/rust-toolchain.toml`, the `miri` and `llvm-tools` components of `nightly-2026-08-24` and `rust-code-analysis-cli` are not installed, and the RustSec database has not been fetched (all are downloads awaiting owner approval, `TC-SW-TOOL-001-r1` section 9 item 1); `tools/measurements.py` does not exist, so the SWE-186 run comparison uses the interim check in `tools/sw_gate.sh`.
- **Plan to PDR.** Owner approves the downloads; Claude installs and records them in the lock; `tools/measurements.py`; TV records of the PDR set of 05 §13 (Rust toolchain, `cargo-llvm-cov` with llvm-tools, `cargo-nextest`, the pinned nightly for MSR-14).

### 3.21 Emulator `ACC-EMU-001` (tool)

- **Heritage and evidence.** c1570/rp2350js at commit `af0114cb`, ARM mode, characterized with a set of purpose-built firmware images and register probes: TIMER0 alarms and NVIC entry pass (alarm up to 1 us early), PWM slices 0 to 7 pass for period and duty, ADC, I2C0, SPI0 and UART0 pass with zero bus time, SIO GPIO pass; clock tree, TICKS, GPIO edge interrupts, NVIC priorities, SysTick, PWM slices 8 to 11, flash and USB fail or are partial; watchdog fires at 0.53x; the GPIO coprocessor path is a NOP, which is why cwht uses SIO GPIO only (`docs/research/emulator-accreditation-and-timer-irq.md` F1 to F12). Known answers KA-1 to KA-3 with hashes and the credit scope are written as the accreditation case (F13). Alternatives Renode, Wokwi and QEMU were evaluated and rejected or kept as fallback (`docs/research/rp2350-emulation-options.md`).
- **Maturity.** Characterized and ready for accreditation; credited scope is event ordering and register plumbing only, never durations (charter §9, SI-026). Emulation never raises a firmware element above TRL 4 (section 1.1).
- **Gaps.** Accreditation not yet approved (ADR due PDR); upstream issues A to D unfiled; single-maintainer dependency (mirror fork needed); patched tree would be `ACC-EMU-002` by CR; `npx vitest run` not executed in the study.
- **Plan to PDR.** Vendor as a submodule with a mirror fork; reproduce KA-1 to KA-3; ADR selecting the tool and recording the credit scope in `tools/toolchain.lock.md`; file the upstream issues; decide the patch set for GPIO IRQ decode, PPB offsets and the PWM map. Risk: RSK-003.

### 3.22 Bench instruments and enabling hardware

- **Heritage.** Owner's NanoVNA, 50 ohm BNC dummy load, bench supply and multimeter (SI-013); tinySA Ultra purchase committed (SI-034, ADR-021); sigrok-pico on a second Pico 2 proposed for logic capture; reference antennas and mismatch fixtures proposed (`docs/research/keyer-verification-and-key-input-network.md` F10; `docs/research/antenna-and-erp.md` implications; `docs/research/audio-output-and-hearing-safety.md` A6).
- **Maturity.** Commercial instruments; project procedures not yet written.
- **Gaps.** No calibrated power attenuator for 5 W into the tinySA; tinySA minimum RBW for the keying spectrum unverified (Low); sigrok-pico and `sigrok-cli` on macOS unverified (R-KN2); no USB-serial adapter (Morse-on-LED read-out is the fallback for dev-board tests); multimeter AC accuracy at 700 Hz unknown; no calibrated signal source for MDS (OnAir comparison accepted).
- **Plan to PDR.** Owner buys the attenuator and the second Pico 2; confirm the tinySA RBW; write the TRR procedures for spurious (span 9 kHz to 1.5 GHz, 2f, 3f and 7f reported), band-edge power, keying spectrum, audio ceiling and antenna screen. Risk: RSK-011.

## 4. Heritage assessment (SEMP §7.5 expanded)

| Heritage product | Inherited | Differences (form, fit, function, environment) | Re-qualification required | Recorded in |
|---|---|---|---|---|
| Pico 2 module; rustos boot, vectors, linker script, GPIO driver | Module used as is; runtime used as is | Identical module in a different configuration: cwht pin map, clock tree, board-mounted castellations, 2S supply, RF environment (section 3.13 difference table). Figure G.4-2 second question: TRL 5 until the differences are evaluated; the runtime has no recorded on-board run | `TC-SW-TOOL-001` steps 11 and 12 (flash and observe); re-run its tests under the cwht toolchain pin; reused-software register (SWE-211); section 3.13 dispositions | `docs/process/07-software-engineering-plan.md` §17.1; `docs/vv/reports/TC-SW-TOOL-001-r1.md` |
| rustos methodology | Process pattern | Agent invocations instead of people | None; differences recorded | `docs/process/08-agent-briefing.md` §7 |
| FT-290R, IC-202, Mizuho MX-2 architecture | Single-conversion superhet pattern, performance class | 3.3 V rails, synthesizer LO instead of VXO, pocket form | Full re-derivation; no circuit copied | `docs/design/concept.md` §7.3 |
| Anglian, Kuhne, Elecraft XV front-end practice | Device families, BPF and mixer level, relay T/R rationale | 12 V transverters at 100 mA class versus a 3.3 V handheld budget | Noise and gain budget, device choice in `TS-001` | `TS-001` |
| NXP AFT05MS004N 136 to 174 MHz reference circuit | Match topology, layout hints | cwht stackup, 2S supply with ALC, enclosure thermal path | Behavioral model and simulation; EOL lifetime buy | `TS-001` (device), PA line-up study (concept TS-003 scope) |
| Mitsubishi AN-VHF-053-A harmonic and efficiency data | Harmonic margin logic for the LPF goals | Different device unless a waiver appears | Not transferable; used only to size the LPF margin | `docs/design/concept.md` §7.2 |
| QRP Labs QCX and QMX keying and break-in practice | 5 ms shape, hang-time convention, T/R sequencing order, mono-plug notes | 144 MHz, gate-bias node, relay instead of solid-state switch | LTspice of loop and ramp; sequencer model | ALC and envelope study (concept TS-006 scope), `ICD-TX-SW` |
| Curtis, K1EL WK3, K3NG, YACK keyer semantics | Mode A and B definitions, watchdog figure, tunable ranges (narrowed) | Rust `no_std` implementation, TIMER0 timing | Golden vectors against an independent reference model | `docs/test_cases/sw-keyer/keyer-golden-vectors.json` |
| pico-sdk, `rp235x-hal`, `embassy-rp` register-level drivers | Behavior and register sequences as independent reference only | Own drivers in rustos `pico2` (ADR-019), single NVIC priority, SIO GPIO only | Datasheet citation per register access (Inspection), contract tests, dev-board check per WP-SW-NN | 07 §19; `TS-002` (firmware runtime make/buy) |
| TI BQ25887, ABLIC S-8252, TI BQ29209 application circuits; Pico 2 VSYS OR-ing figure | Topologies and thresholds | Load-while-charging behavior, holder NTC placement, RF-quiet layout | In-context analysis, bench charge test with dummy cells | `ICD-PWR-CTL`, TRR procedures |
| Sharp memory LCD and the `sharp-memory-display` crate | Interface behavior (EXTCOMIN, frame format) | Own driver against `bus::SpiTx`, no backlight | Host golden frames, PNG renderer | SW-UI |
| TE Axicom HF3 datasheet | Ratings and timings | 6 V coil from a 6.0 to 8.4 V pack, cold switching preferred | Stock check, sequencer transient | `ICD-RX-TX` |
| KX4O and G4ILO antenna measurement methods; OET 65 B exposure method | Relative-EIRP procedure; time-averaging recipe | cwht enclosure and whip | Antenna screen at TRR; RF exposure evaluation at PDR, CDR, TRR | V&V plan; RFX evaluation |
| Owner's bench inventory | Instruments | Added tinySA Ultra and logic capture | Calibration checks per test report | Test reports |

Conclusion: no hardware design is inherited. The Pico 2 module is an identical unit in a different configuration (TRL 5 until the section 3.13 differences are evaluated), catalog parts are used within their datasheets, and every other reused element is a starting point re-derived under cwht's own analysis, which is what SEMP §7.5 requires.

## 5. Toolchain proof and sanity-check results (01 §4.3 row 20)

Locked versions are in `tools/toolchain.lock.md` (observed 2026-09-25). A tool's output counts as evidence only after its tool validation record `TV-NNN` is filed, reviewed and accredited (CM plan `docs/process/05-configuration-and-data-management.md` §9.1). As of this revision (2026-09-25) `docs/cm/tool-validation/` does not exist and **no TV record exists** (lock §5), so every result below is developer evidence.

### 5.1 Lock §1.1 sanity checks (results as recorded in the lock)

| Tool (lock §1.1 row) | Last run recorded | Result |
|---|---|---|
| kicad-cli | not yet run | pending |
| `tools/normalize_fab.py` | rules verified in a scratch run 2026-09-25 18:05; tool not yet written | pending |
| `tools/kicad_export/pcbway_package.sh` | blocked: script not yet written (due CDR) | pending |
| LTspice with its Wine layer | not yet run | pending |
| rustc and cargo | not yet run | pending |
| clippy | not yet run | pending |
| cargo-llvm-cov (stable) with llvm-tools | not yet run | pending |
| `nightly-2026-08-24` (MSR-14, non-credit) | not yet run | pending |
| cargo-nextest, cargo-audit, cargo-deny, cargo-geiger, cargo-binutils | not yet run | pending |
| rust-code-analysis-cli | blocked: not installed | pending |
| picotool | not yet run | pending |
| `tools/release.sh`, `tools/image_trailer.py` | blocked: scripts not yet written (due before the first release candidate) | pending |
| shasum | not yet run | pending |
| git | blocked: test module `tools/tests/test_git_known_answer.py` not yet written (lock text) | pending (the module is now present in the working tree; the lock maintainer records its first result, section 8 item 3) |
| python (venv) with jsonschema | not yet run | pending |
| `tools/traceability.py`, `tools/validate_docs.py` (fixture-only classes) | 2026-09-25 earlier session; 18:23 and 19:36, working tree at `b8214ca` | pass (39 tests; 124 fixture-only tests; whole modules 28, 19 and 114 tests) |
| Repository-content check (not a tool accreditation) | 2026-09-25 afternoon, 18:23, 18:5x, 19:36 | fail, pass, fail, pass (19:36: 2 tests) |
| `tools/render_rmm.py` | 2026-09-25; 18:23; 19:36 | pass (20 tests each run) |
| `tools/render_compliance.py` | 2026-09-25 19:36 | pass (27 tests) |
| `tools/render_risk.py` | 2026-09-25 18:33; 19:36 | pass (27 tests each run) |
| `tools/review_trend.py` | 2026-09-25 18:23, 18:28, 19:36 | 19 of 20 (a repository-content test), then pass (20 tests), pass (20 tests) |
| `tools/slides/render_deck.py` with the Chromium headless shell | 2026-09-25; 18:23; 19:36 | pass (1, 1 and 3 tests) |
| OpenSCAD with FreeCAD and `tools/scad2step.py` | not yet run (`tools/scad2step.py` not committed) | pending |
| Logic capture (sigrok-pico with sigrok-cli) | blocked: not installed | pending |
| tinySA Ultra | blocked: instrument not yet received | pending |
| RP2350 emulator | blocked: not selected | pending |

The lock records the 18:23 and 19:36 runs against the working tree at `HEAD` `b8214ca` with the tools and fixtures untracked, so they are tied to the working tree; the TV records re-run them on the commit that adds these files (lock §1.1 preamble).

### 5.2 FW-B0 toolchain proof `TC-SW-TOOL-001`

Report `docs/vv/reports/TC-SW-TOOL-001-r1.md` (case in `docs/test_cases/sw-tool/test_cases.json`, test-only module SW-TOOL; Bench, `credit: false`; 2026-09-25): **result Blocked.** Steps 1 to 10 and 13 were executed: the `firmware/` workspace builds and tests on the host (10 of 10 tests, twice), builds `cwht-app` for `thumbv8m.main-none-eabihf` against rustos by path, is clippy- and format-clean under the 07 Annex B lint set, and the rustos blinky was rebuilt twice and converted to UF2. `tools/sw_gate.sh` passes G0 to G3 but exits 1 at G4 (`tools/traceability.py` on requirements authored concurrently without cases) and, in its keep-going form, also fails G5 `cargo deny` and reports 9 missing prerequisites. Steps 11 and 12 (flash and observe on the bare Pico 2) are pending the owner. Deviation D1: every cargo command ran on `stable` after the gate confirmed its `rustc --version` equals the lock row, because the pinned `1.98.0` toolchain is not installed. The FW-B0 exit criterion (gate exit 0, blinky observed) is not met.

### 5.3 SRR tool validation records (05 §13, SRR row)

| # | TV record required at SRR | Known-answer basis (lock §1.1) | Status on 2026-09-26 |
|---|---|---|---|
| 1 | venv Python with `jsonschema` | `tools/tests/fixtures/schema/` known answers and the keyword survey | TV-001 filed, Validated; review (INSP-015) and accreditation pending |
| 2 | `tools/traceability.py` | fixture-only classes | TV-002 filed, Validated on the uncommitted file; review and accreditation pending |
| 3 | `tools/validate_docs.py` | fixture-only classes | TV-003 filed, Validated; review and accreditation pending |
| 4 | `tools/render_rmm.py` | `test_render_rmm.py` | TV-004 filed, Validated; review and accreditation pending |
| 5 | `tools/render_compliance.py` | `test_render_compliance.py` | TV-005 filed, Validated; review and accreditation pending |
| 6 | `tools/render_risk.py` | `test_render_risk.py` | TV-006 filed, Validated; review and accreditation pending |
| 7 | `tools/review_trend.py` | `test_review_trend.py` | TV-007 filed, Validated; review and accreditation pending |
| 8 | `tools/slides/render_deck.py` with the Chromium headless shell | `test_render_deck.py` | TV-008 filed, Validated; review and accreditation pending |
| 9 | `git` | `tools/tests/test_git_known_answer.py` | TV-009 filed, Validated; review and accreditation pending |
| 10 | `tools/render_review_figures.py` | `tools/tests/test_render_review_figures.py` | TV-010 filed, Validated on the uncommitted file; review and accreditation pending |

Every result row of these records must name the commit it ran on (05 §9.2 step 1); the rows written before the first commit of the tools name HEAD 28e49e6 with uncommitted files and are re-run on the commit that adds them (INSP-015 finding-2).

The PDR, CDR and later TV sets are the single authoritative list of 05 §13; section 6 carries them as activities.

### 5.4 Research demonstrations (developer evidence, input to the TV records)

| Tool | Locked version | Research demonstration | Gap | TV due (05 §13) |
|---|---|---|---|---|
| LTspice for macOS (CrossOver) | 26.0.2.1 (program 26.0.2) | Batch run through the bottle's `wine` with the full `LTspice.exe` path works; consent dialog suppressed by `CaptureAnalytics=false` (SI-027); `.raw` parsed by `ltspice` 1.0.6 and `PyLTSpice` 6.0.1, -3 dB point matches the analytic 1000.000 Hz; the cw-selectivity Monte Carlo batch ran (`docs/research/ltspice-batch-macos.md` F3, F4, F8, F9; `docs/research/sim/cw-selectivity/`) | The documented `LTspice -b` launcher form is broken in 26.0.2; wrapper `tools/ltspice-batch.sh` not yet committed; one Wine bottle forbids parallel runs | PDR |
| KiCad kicad-cli | 10.0.6 | ERC and DRC known answers deterministic with JSON reports; PCBWay export recipe (11 Gerbers, job file, 2 drill files, CPL with `--smd-only --exclude-dnp`, BOM) verified on a fixture board (`docs/research/verification-tooling-inventory.md` F1 to F7; `docs/research/pcbway-export-and-vendor-questions.md` F1 to F12) | Global library tables absent (project-local tables fix it); published DRC schema is invalid JSON (patched copy needed); SWIG `pcbnew` leaves in KiCad 11; `tools/normalize_fab.py` not yet written | PDR (with `tools/normalize_fab.py`); CDR (`pcbway_package.sh`) |
| Rust toolchain | rustc 1.98.0, cargo 1.98.0, target `thumbv8m.main-none-eabihf`, picotool 2.3.0 | Research: host build, `cargo test -p api`, `cargo pico2` dev and release, offline application build, ELF to UF2 and `picotool info` without a device (`docs/research/rustos-toolchain-proof.md` F1 to F6); FW-B0: section 5.2 | cargo-llvm-cov, cargo-nextest, cargo-geiger, cargo-deny and cargo-audit installed with no sanity check run; pinned `1.98.0` toolchain, nightly components and `rust-code-analysis-cli` not installed (section 3.20); MC/DC instrumentation absent from rustc (SWE-219 Tailored; RSK-010); `firmware/rust-toolchain.toml` pin present in the uncommitted workspace | PDR (rustc, cargo, clippy, cargo-llvm-cov, cargo-nextest, nightly); CDR (picotool, cargo-binutils, cargo-audit, cargo-deny, cargo-geiger) |
| Python venv | 3.13.5 with jsonschema 4.26.0 | `tools/validate_docs.py` and schema validation in use; proposed analysis pins (numpy, scipy, scikit-rf, spicelib, matplotlib, lizard, pytest) install cleanly and pass known answers in a scratch venv (`docs/research/verification-tooling-inventory.md` F15) | `tools/requirements.txt` lists names without version pins (CM plan AL-4) | SRR (venv with jsonschema) |
| OpenSCAD | 2021.01 at `/Applications/OpenSCAD-2021.01.app` (x86_64 under Rosetta; the lock row records this path) | CLI exported STL, 3MF, CSG and PNG renders of a representative half-shell; cube known answer passes (`docs/research/enclosure-cnc-and-openscad-pipeline.md` B2; `docs/research/verification-tooling-inventory.md` F11) | Snapshot 2026.09.23 versus 2021.01 decision open (RSK-044) | PDR |
| FreeCAD headless STEP stage | 1.1.3, installed 2026-09-25 (Homebrew cask, SI-032; lock FreeCAD row) | CSG-to-B-rep import path verified from source reading only (B4, B5) | `tools/scad2step.py` not committed; STEP acceptance checks (valid, one solid, no BSpline faces, volume match) never run (RSK-044) | PDR |
| Emulator rp2350js | commit `af0114cb`, node v25.9.0 | Eleven images and three probes; known answers KA-1 to KA-3 defined with hashes (`docs/research/emulator-accreditation-and-timer-irq.md` F12, F13) | Not vendored; ADR due PDR | PDR |
| Slide toolchain (Asciidoctor.js, reveal.js, Chromium headless shell 1223) | lock §3a | Known-answer test passes (section 5.1) | TV record not filed | SRR (with `render_deck.py`) |
| git | 2.50.1 (Apple Git-155) | Known-answer module present in the working tree | Lock result not recorded; TV record not filed | SRR |
| Bambu Studio CLI (fit-check prints) | 02.08.02.61 | Project 3MF export works; headless slicing for the H2C fails on filament mapping (B7) | Manual GUI slicing step remains and is recorded in the fit-check procedure (RSK-044) | CDR |

## 6. Advancement plan to PDR (AD2 step)

Every Red or Yellow element in section 2 maps to at least one activity below. The plan is the Phase B technical content that `docs/plan/schedule.md` places on Saturday 2026-09-26; items marked "owner" need the owner's hands or account.

| Element | Gap closed | Activity | Evidence product | Owner | Gate |
|---|---|---|---|---|---|
| Frequency generation | Candidate choice, phase noise, spur map | Synthesizer trade study (concept §11.2 synthesizer and reference scope, `TS-NNN-synthesizer-reference`, number assigned at creation); extract LMX2571 plots; Si5351 at 144 MHz measured or sourced; spur map with the chosen IF | Trade study in `docs/decisions/trade-studies/`; phase-noise and spur budget with checker | Claude; owner for a bench measurement | PDR |
| PA and line-up | Device choice, model | Retrieve ST and Guerrilla documents; device choice in `TS-001`; behavioral LTspice PA model per candidate; LPF with SRF models; owner lifetime buy if EOL device chosen | `TS-001`; `hardware/sim/pa-*.asc` with `tools/ltspice_check.py` results | Claude; owner (documents behind bot walls, purchase) | PDR |
| ALC, envelope, cutoff node | Loop and ramp design | ALC and envelope trade study (concept TS-006 scope); transient simulations; `bw.py` in `tools/` | Trade study; envelope spectrum plot with 26 dB bandwidth | Claude | PDR |
| T/R and receiver protection | Stock, sequencing | Stock check; sequencer transient; protection analysis | `ICD-RX-TX` Draft; deck and checker | Owner (stock), Claude | PDR |
| Antenna port | Tolerance stack | Boss and jack tolerance analysis; pigtail alternative | `ICD-TX-ANT` update; enclosure model | Claude | PDR; fit print at CDR |
| Receiver front end | Budget | Cascade noise and gain budget; BPF and LNA simulation; birdie map | Budget note in `docs/design/budgets.md`; decks | Claude | PDR |
| Selectivity A | Quotes | KVG and Inrad quotes with case drawings | Quote records in the PDR package | Owner (email) | PDR |
| Selectivity B | PIO I2S on RP2350, DSP | PIO I2S loopback on a Pico 2 with a PCM1808 breakout (RSK-013 S4); DSP chain HostUnit tests; second-source ADC | Loopback report (`credit: false`); HostUnit results | Owner (breakout purchase and run), Claude | PDR |
| Power | Noise, second sources, thresholds | Buck and LDO PSRR simulation; second sources; S-8252 calculation; cell curve | Decks; `ICD-PWR-CELL`, `ICD-PWR-CTL` | Claude | PDR |
| USB input | Path rating | Pico 2 VBUS path measurement at 0.5, 1.0 and 1.5 A; DCP detection experiment | Measurement record; USB charge-current trade study (concept TS-005 scope) | Owner | PDR |
| Pico 2 module and rustos runtime | On-board run; difference evaluation; vendor confirmation | `TC-SW-TOOL-001` steps 11 and 12 (flash and observe) and run 2; section 3.13 dispositions; send the PCBWay email (module reflow, CPL rotation, via fill, impedance report) | `docs/vv/reports/TC-SW-TOOL-001-r2.md`; clock plan ADR; vendor reply in the CDR package | Owner (flash, observe, send), Claude (run 2, draft exists) | Run 2 before the SRR readiness declaration (07 §3.1); email before PDR; answers by CDR |
| Key inputs, jacks | ICDs, RF immunity | `ICD-CTL-KEY`, `ICD-CTL-PHONES`; choke analysis; TPA6132A2 short data | ICD stubs (before SRR) and Drafts | Claude | SRR stubs; PDR |
| Display and UI | Driver, footprint, stack | Host golden frames and PNG renderer; footprint and 3D overlay render; panel stack-up | Renders in the PDR package; `ICD-CTL-ME` Draft | Claude | PDR |
| Audio | Network, harness | LTspice of the network; host harness for limiter, AGC, fades | Deck and results; HostUnit results | Claude | PDR |
| Enclosure and PCB | Model, STEP, quotes, thickness | Envelope model; commit `tools/scad2step.py` and run it on the smoke shell (FreeCAD 1.1.3 is installed); instant quotes (enclosure; PCB at both thicknesses); board-thickness trade study | STEP acceptance log; quotes as TPM inputs; trade study | Owner (quotes), Claude | PDR |
| rustos drivers | FW-B1 set WP-SW-01 to 07, 09, 11 | Implement each to the `api` trait boundary with host mock, contract tests, datasheet citations, dev-board check and emulator register-sequence comparison (07 §19 closure rule); rustos hygiene items (F16) as a sprint task | rustos changes at a pinned commit; `cwht-hal-mock`; dev-board check reports per WP (`credit: false`); sprint records `docs/sprints/SW-NN-<module>.md` | Claude; owner (merge approval as rustos maintainer, dev-board runs) | PDR (FW-B1 set), CDR (WP-SW-08, 10, 12 in FW-B2) |
| `cwht-core` | Keyer, prototype | Keyer and debounce HostUnit tests from golden vectors; keyer prototype on the dev board with sidetone for the owner's HSI verdict; sequencer and safety-manager models | `tools/sw_gate.sh` exit 0; test reports; HSI verdict in `docs/reviews/PDR/decision-memo.md` | Claude; owner (HSI verdict) | PDR |
| Host method | Tools | Approve the downloads (pinned toolchain, nightly components, `rust-code-analysis-cli`, RustSec database); install and record; `tools/measurements.py` | `tools/toolchain.lock.md` update; `TC-SW-TOOL-001-r2` gate exit 0 | Owner (approval), Claude | Before the SRR readiness declaration (FW-B0); PDR (TV) |
| Emulator | Accreditation | Vendor and mirror; reproduce KA-1 to KA-3; ADR; file upstream issues | ADR; `tools/toolchain.lock.md` ACC-EMU-001 entry; `docs/vv/reports/ACC-EMU-001/` | Claude; owner (mirror fork under the owner's account) | PDR |
| Tools | Sanity checks and TV records | Run every lock §1.1 check and record it; review and accredit the ten SRR TV records of section 5.3; then the PDR set of 05 §13 (LTspice with `tools/ltspice-batch.sh`, kicad-cli with `tools/normalize_fab.py`, OpenSCAD and FreeCAD with `tools/scad2step.py`, emulator, Rust toolchain, `tools/render_tpm.py`, `tools/measurements.py`, `tools/csa.py`, `tools/check_commit_msg.py`) | `docs/cm/tool-validation/TV-NNN-<tool>.md`; lock §1.1 result cells | Claude | SRR readiness declaration (nine records); PDR (PDR set) |
| Bench | Instruments and procedures | Attenuator and second Pico 2 purchase; tinySA RBW check; TRR procedures | Procedures in `docs/test_cases/`; inventory update | Owner (purchases), Claude | PDR (procedures), TRR (instruments) |

## 7. Technology Development Plan disposition (Table G-3 item 5.8; Table G-4 items 6.16 and 6.17)

**Item 6.17 / 5.9.** This document is the technology readiness assessment with technology assets, heritage products and gaps identified (sections 2 to 5).

**Items 5.8 / 6.16.** Finding: **the cwht baseline requires no technology whose underlying technique is below TRL 6.** Every baseline hardware element is a catalog part in mass production or a published circuit technique in fielded amateur and commercial radios (TRL 9, section 2 technology column). The software elements rated TRL 2 or 3 in section 2 (rustos drivers, `cwht-core`, the candidate-B DSP chain, the rustos runtime) are rated on the design-maturity scale; their underlying techniques are fielded at TRL 9: register-level RP2350 peripheral drivers in the pico-sdk and open-source Rust HALs (section 3.18), keyer, debounce and T/R sequencing semantics in the K1EL, K3NG, YACK, QCX and QMX products (section 3.19), CW DSP filtering with digital AGC in the QMX on a Cortex-M4F (section 3.10), and Cortex-M boot and linker technique in the pico-sdk and `cortex-m-rt` (section 3.13). What is immature is cwht's own integration of these technologies: design maturity governed by the SEMP §6.0 DML gates (RF hardware DML-4 by PDR and DML-5 by CDR, both hardware TRL 3; firmware per 07 §3.1) and tracked in this assessment and the risk register, not by a Technology Development Plan. No Technology Development Plan exists, so G-4 item 6.16 has nothing to update. The disposition of 01 §4.7 (G-3 5.8 Not Applicable) stands for the baseline.

**Named exception: PIO I2S receive on the RP2350 (selectivity candidate B).** Its technique is TRL 5 (proven on the RP2040 by community code, not shown on the RP2350; section 3.10). No Technology Development Plan is written at SRR because (a) candidate B is one of two candidates carried to the filed `TS-001`, not the baseline; (b) its fallback, candidate A, uses TRL 9 technology throughout, so the system has a recorded off-ramp (SEMP §6.0 off-ramps); and (c) the loopback prototype that would evaluate the RP2040-to-RP2350 difference is already planned before PDR (RSK-013 step S4; section 6). If `TS-001` selects candidate B, either the loopback result is presented at PDR as the difference evaluation (technology TRL 5 on the RP2350 by evidence, reaching TRL 6 only on the assembled board) together with a Technology Development Plan for that path, or the owner selects candidate A. This assessment is re-issued at PDR with that outcome (section 9).

Watch items that could change this finding, each carried as a risk: the PA device supply (EOL device with finite stock, single-source alternatives; RSK-005); PIO I2S on rustos for candidate B (RSK-013 step S4, the merged research candidate CWSEL-10; emulator fidelity for PIO under RSK-003; falls back to candidate A); MC/DC measurement for Rust (a process-tooling gap, SWE-219 Tailored in the RMM and charter §12; RSK-010); the emulator's uncredited peripherals (RSK-003, mitigated by HostUnit primacy and Bench for timing); the STEP export pipeline (RSK-044). If any of these were to require new technology rather than integration work, this document is updated and a research report and risk are opened, as 01 §4.7 requires.

## 8. Open items and owner decisions

1. **Closed items of revision 1.** The location pointer (01 §4.3 row 20 and §5.3 row 16 and SEMP §6.0 now name `docs/plan/technology-assessment.md`), the lock OpenSCAD path (the lock row records `/Applications/OpenSCAD-2021.01.app`) and the SEMP §3.1 connector wording (now the Pico 2 micro-USB, SI-022) are closed; FreeCAD 1.1.3 and the cargo coverage, test and audit tools are installed (lock second observation, 2026-09-25).
2. **Driver work-package alignment.** This revision uses the WP-SW-NN ids and the FW-B1 PDR scope of 07 §19 and §3.1. The rustos repository hygiene items of `docs/research/rustos-toolchain-proof.md` F16 have no 07 §19 row; the 07 author decides whether they stay a FW-B1 sprint task (this assessment's assumption) or become a work package by CR. Candidate B would add PIO, DMA and I2S packages to 07 §19 by CR if `TS-001` selects it.
3. **Toolchain lock results.** The lock maintainer runs and records every lock §1.1 check still pending (section 5.1), including the first result of `tools/tests/test_git_known_answer.py`, and the ten SRR TV records (section 5.3) are reviewed and accredited before the SRR readiness declaration (SRR package item H12).
4. **Owner actions that gate SRR and PDR evidence:** perform `TC-SW-TOOL-001` steps 11 and 12 (flash and observe the blinky and `cwht-app` on the bare Pico 2); approve the downloads of `TC-SW-TOOL-001-r1` section 9 item 1 (pinned `1.98.0` toolchain, `nightly-2026-08-24` components, `rust-code-analysis-cli`, RustSec database); send the PCBWay email; request KVG and Inrad quotes; buy a PCM1808 breakout if candidate B stays in `TS-001`; buy the tinySA attenuator and a second Pico 2; run the Pico 2 VBUS path measurement; create the mirror fork of rp2350js; check distributor stock for the relay, display, ZIF, encoders and jacks with timestamps.
5. **Owner decisions at SRR:** (a) accept this assessment's two-scale method, technology TRL versus the SEMP §6.0 DML with its App. E TRL mapping, as the project's TMA terminology (SE HB App. G asks that terms be fixed before levels are assigned), and the section 7 finding with its named exception (package decision 13); (b) accept hardware TRL 3 at procurement release as a recorded residual of RSK-008 (package decision 11; OQ-SE-006).
6. **Confidence.** Technology TRL assignments are High for parts (datasheets, vendor status pages and distributor stock read on 2026-09-25 as cited) and Medium for the software techniques whose heritage rests on general knowledge of the named products (pico-sdk, `rp235x-hal`, `embassy-rp`; TS-002 marks its characterization of the Rust HALs Low). Design-maturity levels are High where a report contains the derivation or simulation (sections 3.4 to 3.7, 3.10, 3.11, 3.14, 3.17, 3.19) and Medium where they rest on part selection alone. Stock and lifecycle statements are dated 2026-09-25 and expire at each gate (re-check rule of the research reports).

## 9. Update rule

This assessment is re-issued at PDR, CDR, TRR and SAR with a delta table (01 §5.3 row 16, §7): elements whose DML or App. E TRL changed, new gaps, closed gaps, the module and system roll-up of section 2.1, and any element that missed its gate level with the fallback taken. The PDR issue is the final TMA of SE HB App. G ("performed just prior to PDR") for rev A.
