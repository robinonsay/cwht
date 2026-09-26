# cwht Technology Readiness and Heritage Assessment (SRR)

**Status:** Draft for SRR (initial Technology Maturity Assessment; updated at every review). **Owner:** Robin (approves). **Author:** Claude (lead systems engineer); independent reviewer agent checks it before SRR. **Governing text:** SE HB App. G (G.4 Establishing TRLs, Figure G.4-1 levels, Figure G.4-2 TMA thought process for heritage, Figure G.4-3 TRL Assessment Matrix with its Green, Yellow and Red bands, and the AD2 step for elements below the required maturity); NPR 7123.1D App. E (TRL definitions with hardware and software descriptions) and §5.1.6; NPR 7123.1D App. G Table G-3 item 5.9 (initial technology readiness assessed with technology assets, heritage products and gaps identified) and item 5.8 (Technology Development Plan, dispositioned in section 7); SEMP `docs/plan/semp.md` §6.0 (insertion rules) and §7.5 (heritage); `docs/process/01-lifecycle-and-reviews.md` §4.3 row 20 (TRL-style table plus toolchain sanity-check results) and §4.7. **Location note:** 01 row 20 and SEMP §6.0 name `docs/research/technology-assessment.md`; this assessment lives at `docs/plan/technology-assessment.md` by assignment, and the two pointers are corrected by editorial fix before SRR (section 8).

Research reports are cited as `docs/research/<file>.md F<n>`; their confidence tags (High, Medium, Low) are carried over where an assessment rests on one finding. Regulatory text is cited from `docs/references/md/regulatory/` (eCFR 2026-09-23).

---

## 1. Method

### 1.1 Two scales, kept apart

SE HB App. G warns that integration lowers the TRL of a unit whose parts are individually mature, and that terms must be defined before levels are assigned. This assessment therefore reports two quantities for every element:

1. **Technology TRL** (NPR 7123.1D App. E): the maturity of the underlying technology or catalog part in the world at large. A part in mass production and in use in fielded radios is TRL 9. Software that runs on the target board in its intended role is TRL 6 to 7; software whose algorithms are defined but not coded is TRL 2.
2. **cwht design maturity**, expressed as a TRL-equivalent with the definitions the SEMP §6.0 already uses, because cwht's own integration of a mature technology starts at the concept level:

| TRL-equivalent | cwht definition (hardware) | cwht definition (firmware) | Evidence class |
|---|---|---|---|
| 2 | Concept formulated: block named, part family and interfaces identified (this document, `docs/design/concept.md`) | Function and semantics defined, reference behavior chosen | Research report |
| 3 | Analytical proof of the critical function: budget, hand analysis, derived numbers against the requirement | Reference model or golden vectors exist; datasheet ICD extracted for the driver | Analysis (hand) |
| 4 | Breadboard in a laboratory environment: LTspice or S-parameter simulation with pass/fail checkers against the budget, catalog parts and vendor models | Logic implemented in `cwht-core` and passing HostUnit tests against `cwht-hal-mock`; driver register sequence checked by inspection and emulator readback | Analysis, HostUnit, Emulation |
| 5 | Brassboard in a relevant environment: full block simulated in context with layout parasitics estimated; or the function measured on a Pico 2 development board or a vendor evaluation board | Firmware running on a Pico 2 development board or as a whole-binary emulation scenario in the credited scope | Analysis, Emulation, dev-board Bench |
| 6 | Assembled cwht board on the bench meeting its requirements (TRR, Bench) | Firmware on the assembled board through the first-power-on procedure | Bench |
| 7 | Unit in its enclosure operated on air (OnAir demonstration) | Same | OnAir |
| 8 | SAR: acceptance completed, V&V report closed | Same | SAR |
| 9 | Sustained operation by the owner and friends | Same | Phase E |

Gate requirements (SEMP §6.0): every RF block reaches TRL 4-equivalent by PDR and 5-equivalent by CDR; any element below that at the gate opens a risk with a fallback from its trade study; any technology below TRL 6 at PDR opens a risk. Terms for cwht: laboratory environment = simulation and host execution; relevant environment = the Pico 2 development board, a vendor evaluation board or the bench with the owner's instruments; operational environment = the enclosed unit on air; breadboard = a simulation deck with checkers or a host-tested crate; brassboard = the first assembled cwht board or a dev-board check binary; prototype = unit `CWHT-A-001`.

### 1.2 Heritage thought process

For each heritage product the Figure G.4-2 questions are asked: has an identical unit operated in the identical configuration and environment (TRL 9 for cwht)? If the unit is identical but the configuration or environment differs, the element drops to TRL 5 until the differences are evaluated; if only a similar design exists, the element is treated as new and enters at the design-maturity level its analysis supports. SEMP §7.5 adds the project rule: no circuit or algorithm is inherited without re-analysis; heritage supplies starting points and independent evidence, not credit.

### 1.3 Colors

Per SE HB Figure G.4-3: Green = TRL 6 and above, Yellow = TRL 3, 4 and 5, Red = below TRL 3. Colors are assigned to the **cwht design maturity today**; the technology TRL column shows why a Red today is a schedule item and not a technology gap.

## 2. Summary matrix

| Module | Element | Technology TRL | cwht maturity today | Color today | Required at PDR | Required at CDR | Risk links |
|---|---|---|---|---|---|---|---|
| TX | Frequency generation: TCXO plus Si5351A or LMX2571 | 9 (parts) | 3-equiv (phase noise and error budget derived) | Yellow | 4-equiv, TS-002 decided | 5-equiv | RSK-002, RSK-005 |
| TX | Exciter, driver and PA device (TS-003) | 9 (devices), AFT05MS004N EOL with stock | 2-equiv (no model, no circuit) | Red | 4-equiv with a behavioral model | 5-equiv | RSK-001, RSK-005, RSK-006 |
| TX | Gate-bias ALC and envelope shaper (TS-006) | 9 (technique in production radios) | 2-equiv | Red | 4-equiv | 5-equiv | RSK-001, RSK-012 |
| TX | Harmonic LPF | 9 (technique) | 3-equiv (attenuation goals derived) | Yellow | 4-equiv with vendor SRF models | 5-equiv | RSK-011 |
| TX | T/R relay and sequencing (HF3 class) | 9 (part) | 3-equiv (stress and timing derived) | Yellow | 4-equiv | 5-equiv | RSK-005 |
| TX | Hardware PA-enable cutoff and TX inhibits | 9 (parts) | 3-equiv (timing derived) | Yellow | 4-equiv | 5-equiv | RSK-012 |
| TX | Antenna port SMA, boss retention, counterpoise lug | 9 (part) | 3-equiv (load data collected) | Yellow | 4-equiv (tolerance stack) | 5-equiv (fit-check print) | none open |
| RX | Front end: BPF, LNA, mixer | 9 (parts) | 2-equiv | Red | 4-equiv | 5-equiv | RSK-008 |
| RX | Selectivity A: commercial 8-pole can, IF, AGC, detector | 9 (part) | 2-equiv (quote and data pending) | Red | 4-equiv, TS-001 decided | 5-equiv | RSK-005 |
| RX | Selectivity B: 1.0 kHz roofing ladder | 9 (technique) | 4-equiv (Monte Carlo with pass/fail run) | Yellow | 4-equiv | 5-equiv | none open |
| RX | Selectivity B: PCM1808 I2S ADC and DSP | 9 (part); DSP TRL 2 | 2-equiv (PIO I2S on rustos untested) | Red | 4-equiv with a PIO loopback on a Pico 2 | 5-equiv | RSK-003 |
| PWR | Charger, protection, holders, rails | 9 (parts) | 3-equiv (current budget and topology) | Yellow | 4-equiv | 5-equiv | RSK-007 |
| PWR | USB input through the Pico 2 module | 9 (module) | 2-equiv (path unrated) | Red | 5-equiv by measurement on a Pico 2 | same | none open |
| CTL | Pico 2 module and RP2350 | 9 (module) | 6 to 7 for the module itself (rustos blinky on the board) | Green | Assembly confirmation from PCBWay | same | RSK-004 |
| CTL | Key input network, ESD, jacks | 9 (parts) | 3-equiv (network derived) | Yellow | 4-equiv | 5-equiv (bounce capture) | RSK-012 |
| CTL | Display, encoders, buttons | 9 (parts) | 2-equiv | Red | 4-equiv (driver goldens, panel stack) | 5-equiv | none open |
| CTL | Audio: PWM, reconstruction, TPA6132A2 | 9 (parts); PWM audio heritage with noise history | 2-equiv | Red | 4-equiv | 5-equiv | none open |
| ME | CNC 6061 enclosure, thermal pedestal | 9 (service and material) | 3-equiv (thermal chain derived; smoke shell rendered) | Yellow | 4-equiv (model, quote) | 5-equiv (STEP accepted, fit print) | RSK-006 |
| ME | 4-layer PCB, stackup, via fill | 9 (PCBWay standard) | 3-equiv (stackup and impedance estimate) | Yellow | 4-equiv (TS-004) | 5-equiv (DRC clean) | RSK-004 |
| SW | rustos runtime as it exists (boot, vectors, linker, GPIO) | 6 to 7 | 6 to 7 | Green | unchanged | unchanged | none |
| SW | rustos drivers cwht needs (WP-01 to WP-10) | 2 | 2 (datasheet ICD extracted) | Red | 4-equiv for WP-01 to WP-04; others 3 | 5-equiv | RSK-003, RSK-008 |
| SW | `cwht-core` logic: keyer, sequencer, safety manager | 2 (semantics defined) | 3-equiv (golden vectors defined) | Yellow | 4-equiv (HostUnit skeleton, keyer vectors) | 5-equiv | RSK-012 |
| SW | Host-first method (`cwht-hal-mock`) | demonstrated | 4-equiv (mock against `api` works) | Yellow | in use | in use | RSK-010 |
| Tool | Emulator `ACC-EMU-001` | characterized | accreditation case written, not approved | Yellow | ADR and accreditation | scenarios | RSK-003 |
| Tool | LTspice batch, KiCad kicad-cli, Rust toolchain, Python stack, OpenSCAD plus FreeCAD | in use | proofs done, no tool validation record | Yellow | TV records (LTspice, kicad-cli, OpenSCAD, Rust) | TV (picotool, cargo-binutils) | RSK-009, RSK-010 |
| Bench | tinySA Ultra, logic capture, fixtures | commercial | purchase decided; attenuator and capture unverified | Yellow | procedures written | instruments in hand at TRR | RSK-011 |

Reading of the matrix: nothing in the radio requires a technology below TRL 6; every Red cell is cwht design work that has not started, and every one has a named PDR activity in section 6. This is the expected state at the SRR of a Phase A project and is the basis for the section 7 statement.

## 3. Element assessments

### 3.1 Frequency generation (TX)

- **Heritage.** Si5351A: QRP Labs QCX and QMX, Elecraft KX2, uBITX at HF with measured -127 to -135 dBc/Hz at 10 kHz; at 144 MHz only a secondary, unverified report (-112 dBc/Hz at 156 MHz) exists, and the output divider drops to 6 (`docs/research/2m-cw-transceiver-reference-designs.md` F16, F17). LMX2571: TI positions it for battery PMR radios, datasheet -123 dBc/Hz at 12.5 kHz at 480 MHz, derived about -133 dBc/Hz at 144 MHz; no amateur heritage found (F20). TCXO grades from Epson, Abracon, SiTime and the QRP Labs module (F21). Frequency-error and band-edge analysis: `docs/research/regulatory-corpus-and-operators.md` F7, F8.
- **Technology TRL.** 9 for every candidate part (mass production, DigiKey stock recorded 2026-09-25 for Si5351A and LMX2571).
- **cwht maturity.** 3-equivalent: the reciprocal-mixing bound (about 85 dB with a Si5351 LO), the +/-370 Hz error budget and the 1 kHz guard are derived; no register plan, no spur analysis in context.
- **Gaps.** Si5351 phase noise at 144 MHz unverified (Medium); LMX2571 closed-loop plots are images not yet extracted; clipped-sine versus square reference penalty couples TS-002 to the TCXO choice; spur landing map versus 144 to 148 MHz and the IF not computed.
- **Plan to PDR.** TS-002 with the criteria of `docs/design/concept.md` §11.2; extract LMX2571 plots; measure a Si5351 at 144 MHz on the bench or find the primary source; compute the spur map with the chosen IF; register model of the chosen device as the emulator's I2C or SPI target (`docs/research/rp2350-emulation-options.md` implications). Exit: 4-equivalent by an LTspice or Python phase-noise and spur budget with pass/fail against the selectivity set.

### 3.2 Exciter, driver and PA (TX)

- **Heritage.** NXP AFT05MS004N with a full 136 to 174 MHz reference PCB, S-parameters and ADS models behind an NXP account; ST PD54008L-E (AN2048 at 169 MHz, not retrieved); Guerrilla RF GRF5604 (5 V, 450 to 470 MHz evaluation board only); Mitsubishi RD07MUS2B with AN-VHF-053-A harmonic data (excluded by SI-028 unless an authorized BOM-linkable channel appears) (`docs/research/pa-device-candidates.md` comparison table, F21). QRP Labs QCX proves 5 W drain-modulated CW at HF; no vendor provides a SPICE model for any candidate (F6).
- **Technology TRL.** 9 for the devices; AFT05MS004N is End of Life with finite authorized stock (Newark 1,519 and Mouser 72 on 2026-09-25), which is a supply risk, not a maturity gap.
- **cwht maturity.** 2-equivalent: no line-up, match or model exists for 144 MHz at 7.4 V in cwht's stackup.
- **Gaps.** No SPICE model (behavioral model must be built from S-parameters and datasheet tables); PD54008L-E and GRF5604 technical fit unverified; export and lifetime-buy questions if the EOL device is baselined; RthJC versus the pedestal chain; harmonic data from one lot and one circuit (2011) for the Mitsubishi part is not transferable to another device.
- **Plan to PDR.** Retrieve the ST and Guerrilla documents; TS-003 with the mandatory criteria of SI-028; build the LTspice behavioral PA model (S-parameter block plus fitted nonlinear transconductance) for each surviving candidate; run output power across 6.0 to 8.4 V, harmonic content into the LPF, and the ramp; owner buys a lifetime reserve if the EOL device is baselined. Exit: 4-equivalent by a checked simulation of 5.0 W +/-0.5 dB with ALC and 60 dBc at the antenna port. By CDR: 5-equivalent with layout parasitics and the thermal chain (`docs/research/pcbway-export-and-vendor-questions.md` F16, F17). Risks: RSK-001, RSK-005, RSK-006.

### 3.3 ALC loop and envelope shaper (TX)

- **Heritage.** Gate-bias power control is the Mitsubishi RD-series application practice; drain-supply modulation is the QRP Labs QCX practice at 5 W HF; the raised-cosine 5 ms shape is the ARRL and IC-705 class norm; the 26 dB bandwidth computation exists as an 80-line Python script (`docs/research/regulatory-corpus-and-operators.md` F7; `docs/research/keyer-verification-and-key-input-network.md` F11, F12).
- **Technology TRL.** 9 for the techniques.
- **cwht maturity.** 2-equivalent: node chosen as a baseline, no loop design, no simulation.
- **Gaps.** Loop stability and set-point scaling per power step; whether a bias-only cutoff silences a driven LDMOS (R-KN5 in the keyer verification report); 2f content during the ramp; envelope convention (10-to-90 % versus full transition) to be fixed by ADR.
- **Plan to PDR.** TS-006 with LTspice transients of the loop and the ramp for each TS-003 candidate, FFT of the envelope with `bw.py` moved into `tools/`, fault cases (bias lost, TX_KEY stuck) to place the cutoff node. Exit: 4-equivalent by simulation with pass/fail on 26 dB bandwidth at most 350 Hz and -60 dBc beyond 500 Hz.

### 3.4 Harmonic low-pass filter (TX)

- **Heritage.** Seventh-order or elliptic LPFs at the antenna port are universal practice; the attenuation need (at least 40 dB at 288 MHz and 35 dB at 432 MHz, 0.5 dB insertion loss) is derived from the 60 dBc target and the measured in-band 2fo of a 7 V VHF LDMOS (`docs/research/pa-device-candidates.md` F16, F17); the 53.0 dB limit at 5 W derives from 47 CFR 97.307(e) (`docs/research/part97-regulatory-basis.md` F2).
- **Technology TRL.** 9.
- **cwht maturity.** 3-equivalent (numbers derived, no topology simulated).
- **Gaps.** Inductor self-resonance and layout leakage erode simulated attenuation; PIN-free path removes the diode-harmonic concern (SI-036); measurement at TRR depends on the tinySA Ultra and an attenuator not yet in the inventory (RSK-011).
- **Plan to PDR.** S-parameter simulation with vendor inductor models and SRF, pass/fail checker in `tools/ltspice_check.py`; NanoVNA S21 of the assembled filter at TRR. Exit: 4-equivalent by simulation with 10 dB margin over the goals.

### 3.5 T/R relay and sequencing (TX, interface to RX)

- **Heritage.** Relay T/R is the Elecraft XV144 and Kuhne rationale ("avoid receive performance degradation by diode switches"); TE Axicom HF3 54: 50 W carry, 80 dB isolation at 100 MHz, 3 to 5 ms operate, 1e7 operations, 6 V coil straight from the pack, hot-switch rated (`docs/research/tr-switch-candidates.md` F7, F12; `docs/research/2m-cw-transceiver-reference-designs.md` F8). Semi break-in per SI-036 removes the relay-wear concern of full QSK (F5).
- **Technology TRL.** 9.
- **cwht maturity.** 3-equivalent: electrical stress at 5 W into VSWR 3:1 (33.5 V peak, 0.67 A), the sequencing envelope (lead-in 5 ms, envelope fall before release) and the fail-to-receive property are derived (F1, F4, F12).
- **Gaps.** Distributor stock and price could not be read by machine (Open item 1 of that report); coil-clamp choice versus release time; second receiver-protection stage sizing; audible click accepted.
- **Plan to PDR.** Owner or PCBWay stock check with timestamps; LTspice transient of the sequencer with the RF envelope; `ICD-RX-TX` timing table; receiver-protection analysis to +17 dBm under a stuck-relay fault. Exit: 4-equivalent.

### 3.6 Hardware PA-enable cutoff, pull-downs and charge inhibit (TX, CTL, PWR)

- **Heritage.** Retriggerable monostable practice (74LVC1G123, LTC6993-2 alternative); WinKeyer paddle watchdog figure (128 elements); the RP2350 pad reset states and erratum E9 guidance; BQ25887 charge-disable pin (`docs/research/keyer-verification-and-key-input-network.md` F2, F13; `docs/research/power-tree-and-charging.md` F22).
- **Technology TRL.** 9 for the parts.
- **cwht maturity.** 3-equivalent: T_max 10 s with a 7.5 to 13 s window derived including capacitor DC-bias derating; layered coverage table written.
- **Gaps.** Capacitor derating is part-specific (R-KN1); the cutoff node depends on the PA topology (R-KN5); K spread versus VCC for the '123 not extracted (Low).
- **Plan to PDR.** Fold the cutoff node into TS-006; choose the capacitor from its vendor DC-bias curve; LTspice of the monostable; bench timing procedure with the logic capture written for TRR. Exit: 4-equivalent.

### 3.7 Antenna port (TX, with ME)

- **Heritage.** SMA jack conventions of Icom, Yaesu, Kenwood and Alinco handhelds; Amphenol mating-cycle and torque data; measured HT antenna gains and counterpoise effect from KX4O and G4ILO (`docs/research/antenna-and-erp.md` F2, F3, F7, F8).
- **Technology TRL.** 9.
- **cwht maturity.** 3-equivalent: bending moment 4.0 N.m and 1000 matings stated, boss dimensions derived (wall at least 2.5 mm, 6.55 mm hole, flat, nut clearance).
- **Gaps.** Tolerance stack of a PCB-mount bulkhead jack against the lid hole (ANT-R6); jack datasheets not fetched (HTTP 403); stainless versus brass body.
- **Plan to PDR.** Tolerance analysis in the enclosure model and PCB outline; pigtail alternative documented; owner files the datasheets. Exit: 4-equivalent; 5-equivalent at CDR by a printed fit check with the real PCB outline.

### 3.8 Receiver front end and mixer (RX)

- **Heritage.** Anglian and Kuhne 144 MHz transverter front ends (SPF5043 or PSA4-5043 LNA, 3-pole BPF, level-17 ring mixer, NF 0.9 to 1.8 dB) and the FT-290R class portable superhet (NF about 7 dB, MDS about -140 dBm in 500 Hz) (`docs/research/2m-cw-transceiver-reference-designs.md` F2, F6, F7). External-noise analysis shows a -144 dBm stretch buys about 1 dB with a handheld whip in residential noise (`docs/research/antenna-and-erp.md` F10).
- **Technology TRL.** 9.
- **cwht maturity.** 2-equivalent: device class and MDS target chosen; no noise or gain budget, no BPF design, no LNA-off-in-TX network.
- **Gaps.** LNA current versus NF (97 mA versus 30 mA class) unresolved; strong-signal behavior with an external antenna (IIP3, blocking) not budgeted; switching-noise coupling from the 5 V buck and charger into a -140 dBm receiver (`docs/research/power-tree-and-charging.md` F19, F20).
- **Plan to PDR.** Cascade noise and gain budget (Python), BPF and LNA simulation with vendor S-parameters, receiver-protection network, birdie map from the clock plan; fold the LNA device choice into TS-001. Exit: 4-equivalent.

### 3.9 Selectivity candidate A: commercial crystal filter superhet (RX)

- **Heritage.** KVG and Inrad 8-pole cans in decades of CW transceivers; FT-290R and IC-202 single-conversion pattern; QCX-class analog AGC and product detector (`docs/research/cw-selectivity-options.md` F2, F3; `docs/research/2m-cw-transceiver-reference-designs.md` F1, F2).
- **Technology TRL.** 9.
- **cwht maturity.** 2-equivalent: candidate defined with numbers (400 Hz at -6 dB, 800 Hz at -60 dB, shape factor 2.0, about 118 USD), no quote, no IF chain design.
- **Gaps.** Single-source through-hole cans, quote-only, one item shown discontinued; centre and termination uncertain until measured (NanoVNA at 9 MHz); analog AGC design.
- **Plan to PDR.** Quotes and lead times from KVG and Inrad with case drawings; footprint compatible with both; IF chain simulation. Exit: 4-equivalent if selected in TS-001; otherwise closed as the recorded fallback.

### 3.10 Selectivity candidate B: roofing ladder, I2S ADC and DSP (RX, SW)

- **Heritage.** Tolerance-designed crystal ladders (Dishal method) are standard homebrew practice; PCM1808 24-bit ADC is a mass-production codec front end; DSP CW filtering with digital AGC is the QMX and SDR practice; PIO I2S exists in the pico-sdk ecosystem but not in rustos (`docs/research/cw-selectivity-options.md` F7, F8, F11 to F14).
- **Technology TRL.** 9 for the ladder technique and the ADC; TRL 2 for cwht's DSP chain (algorithms defined, not coded).
- **cwht maturity.** Ladder: 4-equivalent already, because the Monte Carlo generator ran through the LTspice batch with pass/fail on bandwidth and loss (98.5 % yield at 1.0 kHz with +/-30 ppm crystals; 15 to 51 % at 500 Hz, which is why 500 Hz is not carried), with the generator reproducing the analytic loss formula within 0.5 dB and the nominal -3 dB bandwidth within 3 % (`docs/research/sim/cw-selectivity/`, figures in `docs/research/figures/cw-selectivity/`). ADC and DSP: 2-equivalent.
- **Gaps.** PIO I2S receive on rustos untested and outside the emulator's credited scope; PCM1808 stock at TI zero (LCSC deep, DigiKey reported); crystal parameters assumed, not measured; lot-to-lot Cm shifts bandwidth 20 %; three extra rustos work packages.
- **Plan to PDR.** PIO I2S loopback prototype on a Pico 2 with a PCM1808 breakout (owner hardware, headless); DSP filter and AGC as pure host-tested Rust with synthetic tones; re-run the Monte Carlo with the chosen crystal part and measured parameters from ten samples (NanoVNA series-resonance method) once bought; second-source ADC named. Exit: 4-equivalent for the ADC path by a working loopback plus HostUnit DSP tests; otherwise TS-001 selects A.

### 3.11 Power: charger, protection, holders, rails (PWR)

- **Heritage.** TI BQ25887 datasheet application circuit (2S boost charger, balancing, ADC, DigiKey stock 10,972); ABLIC S-8252 application circuit with dual N-FET; BQ29209 secondary OV; Keystone 1043P holders (10,041 in stock); Pico 2 datasheet VSYS OR-ing figure; TPS62913 and TPS7A20 class regulators with zero DigiKey and Mouser stock on 2026-09-25 (`docs/research/power-tree-and-charging.md` F3, F5, F11, F13, F18 to F20).
- **Technology TRL.** 9 for every part.
- **cwht maturity.** 3-equivalent: topology drawn, receive and transmit current budgets and the battery-life model exist (F23), safety layering listed (F24 as cited by the report's implications).
- **Gaps.** Rail part stock (second sources); switching-noise residual on the 3.3 V analog rail not simulated; charge termination corrupted by load in receive (mitigated by charge pause); dual-path sense threshold needs calibration analysis; NTC senses board rather than cell temperature with these holders.
- **Plan to PDR.** LTspice of buck output filter plus LDO PSRR against a spur budget from the receiver; second sources for buck and LDO; S-8252 threshold-to-current calculation; digitized discharge curve of the chosen cell replacing the 90 % usable-capacity assumption; `ICD-PWR-CELL` and `ICD-PWR-CTL`. Exit: 4-equivalent. Risk: RSK-007.

### 3.12 USB input through the Pico 2 module (PWR, CTL)

- **Heritage.** Pico 2 datasheet: VBUS pin 40, D1 bypass, no rating for the micro-USB connector current path beyond the USB default (`docs/research/power-tree-and-charging.md` F2).
- **Technology TRL.** 9 for the module.
- **cwht maturity.** 2-equivalent for charging above 500 mA (the path is unrated).
- **Plan to PDR.** Measure voltage drop and temperature of a Pico 2 VBUS path at 0.5, 1.0 and 1.5 A (owner bench, A-PWR-01); TS-005 decides the policy. Exit: 5-equivalent by measurement, or the 500 mA-always alternative closes the item by inspection.

### 3.13 Pico 2 module and RP2350 (CTL)

- **Heritage.** rustos boot metadata, vector table, reset handler, linker script and GPIO driver run on the Pico 2 board (blinky), host and cross builds from clean succeed, `picotool uf2 convert` and `info` work without a device (`docs/research/rustos-toolchain-proof.md` F1 to F5). Errata: RP2350-E9 rules out internal pull-downs on A2 silicon; stepping of procured modules unknown (F11, F12).
- **Technology TRL.** 9 for the module; the identical unit in the identical configuration is used, so the module and the existing rustos runtime enter at 6 to 7 for cwht (Figure G.4-2 first question: identical unit, same environment).
- **Gaps.** PCBWay has no published commitment to reflow castellated modules (R-PCB-02); paste aperture 163 % footprint to be built; USB PLL 3rd harmonic and crystal 12th harmonic land on 144.000 MHz (`docs/research/display-and-ui-parts.md` F10).
- **Plan to PDR.** Send the PCBWay email (answers in the CDR package); qualify the footprint from the official KiCad outline with the datasheet Figure 5 pads and render it; design for A2 silicon; clock plan ADR. Risk: RSK-004.

### 3.14 Key input network, ESD clamps and jacks (CTL)

- **Heritage.** Curtis-era key input practice (470 ohm to 1 kOhm series, 5 to 10 ms debounce), K1EL WinKeyer semantics, Elecraft and QRP Labs mono-plug notes; RP2350 pad specifications and E9 leakage; TI TPD2E2U06 (IEC 61000-4-2 level 4); Same Sky SJ1-3535N switched TRS jacks (`docs/research/keyer-verification-and-key-input-network.md` F2 to F6; `docs/research/keyer-and-key-interfaces.md` F1, F7, F11; `docs/research/display-and-ui-parts.md` F17, F19).
- **Technology TRL.** 9.
- **cwht maturity.** 3-equivalent: the network is derived once with margins (closed-contact pad below 0.6 V including 120 uA E9 leakage, 0.30 mA per line, -5 V to +12 V abuse), debounce vectors D1 to D5 defined.
- **Gaps.** Owner's key and paddle bounce not measured (TBR on 2 ms and 5 ms); RF immunity with a 1 m unshielded lead at 5 W not analyzed (choke impedance at least 500 ohm at 146 MHz proposed in the antenna report); cross-plugging survivability of the headphone amplifier under a permanent short not quantified.
- **Plan to PDR.** `ICD-CTL-KEY` and `ICD-CTL-PHONES` from F4 and F5; common-mode choke analysis; TPA6132A2 short-circuit data; bench procedure TC-KEY-BOUNCE for TRR. Exit: 4-equivalent by analysis and HostUnit debounce tests; 5-equivalent at CDR is the bounce capture on the owner's keys with the second Pico 2 (can run before boards arrive).

### 3.15 Display, encoders and buttons (CTL, ME)

- **Heritage.** Sharp memory LCD in low-power instruments; a Rust `sharp-memory-display` crate (0.3.0) for behavior ideas; Bourns PEC11R and Omron B3F are commodity parts; RF-noise history of OLED and TFT displays in uSDX, (tr)uSDX and uBITX radios motivates the memory LCD (`docs/research/display-and-ui-parts.md` F1, F2, F7, F8, F11, F12, F16).
- **Technology TRL.** 9.
- **cwht maturity.** 2-equivalent: parts chosen with numbers, no driver, no panel stack, no footprint.
- **Gaps.** ZIF contact side and pinout orientation (classic first-board error); Sharp operating-temperature statements disagree; encoder bushing length versus panel stack; distributor stock unreadable by machine; dark-use readability (no light in rev A).
- **Plan to PDR.** Display driver against `bus::SpiTx` with host golden frame bytes and a PNG framebuffer renderer; footprint and 3D model of the panel and ZIF overlaid on the enclosure window render; panel stack-up fixed; owner stock check at CDR. Exit: 4-equivalent.

### 3.16 Audio chain (CTL, SW)

- **Heritage.** PWM audio in uSDX-class radios (functional, with documented noise and tick problems), DirectPath and capacitor-coupled headphone amplifiers, EN 50332 level norms and measured earbud sensitivities (`docs/research/audio-output-and-hearing-safety.md` F1, F10, F19, F23 to F29).
- **Technology TRL.** 9 for the parts and the technique.
- **cwht maturity.** 2-equivalent: network values proposed (F27), ceiling numbers derived, nothing simulated.
- **Gaps.** PWM residual and coupling from display SPI, flash and synthesizer activity; TPA6132A2 short-circuit and thermal behavior; multimeter AC accuracy at 700 Hz for the bench ceiling check unknown.
- **Plan to PDR.** LTspice of divider, reconstruction and coupling with a behavioral amplifier model (full-scale sine and worst-case pattern into 32 and 16 ohm, carrier residual, flatness); host test harness for limiter, AGC, fades, sidetone mixing and volume ramps; DNP I2S DAC footprint reserved. Exit: 4-equivalent.

### 3.17 Enclosure, thermal path and PCB (ME)

- **Heritage.** PCBWay CNC service limits, tolerances and finishes; PCBWay standard 4-layer stackup and DFM limits; IPC-4761 Type VII via fill; the OpenSCAD smoke-test half-shell already rendered and exported (STL, 3MF, CSG, PNG) (`docs/research/enclosure-cnc-and-openscad-pipeline.md` A1 to A11, B2; `docs/research/pcbway-fabrication-and-assembly.md` F5, F6, F9; `docs/research/pcbway-export-and-vendor-questions.md` F14 to F19).
- **Technology TRL.** 9 for the service, material and process.
- **cwht maturity.** 3-equivalent: thermal chain from junction to enclosure surface derived (via array 7.6 to 4.7 K/W at 25 vias for 1.6 versus 1.0 mm; junction at most 110 C target), impedance estimate for 50 ohm microstrip (0.30 mm first estimate), CNC design rules listed; the enclosure itself is at concept level.
- **Gaps.** No enclosure model; FreeCAD not installed so the STEP stage is unproven (SI-032 approves the install); PCBWay tolerance statements conflict (+/-0.125 mm headline versus ISO 2768-m); plating thickness unknown; board thickness undecided (TS-004); panelization undecided.
- **Plan to PDR.** Enclosure envelope model with the SMA boss, pedestal, window and bosses; `scad2step.py` run on the smoke shell with acceptance checks (valid, one solid, no BSpline faces, volume match); instant quotes for the enclosure and for the PCB at both thicknesses with and without via fill; TS-004. Exit: 4-equivalent; 5-equivalent at CDR by the accepted STEP, a clean DRC and an H2C fit-check print. Risk: RSK-006.

### 3.18 rustos drivers (SW, WP-01 to WP-10)

- **Heritage.** rustos `api` philosophy (zero-sized handles, `Read`/`Write` traits) and the `pico2` GPIO driver; the RP2350 datasheet address map, reset bits, IRQ numbers and register names for every cwht peripheral extracted (`docs/research/rustos-toolchain-proof.md` F7 to F10, F14, F15, Peripheral to driver map).
- **Technology TRL.** 2 by the App. E software description: practical application identified, basic properties defined, nothing coded. The peripherals themselves are TRL 9 silicon.
- **cwht maturity.** 2 (3-equivalent for the datasheet ICD side).
- **Gaps.** No clock, interrupt, timer, PWM, ADC, I2C, SPI, watchdog or flash driver exists; every other cwht driver depends on WP-01 and WP-02 landing first (schedule risk); register-level drivers are not host-testable without an injectable register-access trait, so their Class A evidence is inspection against the datasheet plus emulation in the credited scope (`docs/research/emulator-accreditation-and-timer-irq.md` F12).
- **Plan to PDR.** WP-13 (hygiene, enables `-D warnings`), WP-01 clocks with explicit TICKS enable and bounded XOSC and PLL waits, WP-02 IRQ plumbing at a single priority, WP-03 TIMER0 alarms, WP-04 GPIO extension with the E9-safe input policy; each with a trait contract test against the mock and an emulator readback scenario; dev-board check binaries on the owner's Pico 2 by CDR. Exit at PDR: 4-equivalent for WP-01 to WP-04; the remaining packages at 3 with their ICD pages extracted. Risks: RSK-003, RSK-008.

### 3.19 `cwht-core` application logic (SW)

- **Heritage.** Keyer semantics from the Curtis mode A and B definitions, K1EL WinKeyer 3 mode register and paddle watchdog, K3NG and YACK behavior (behavior only, GPL code not reused); ITU-R M.1677-1 element ratios; golden vectors V1 to V13 and debounce vectors D1 to D5 defined; reference keyer model `keyer_ref.py` proposed as the independent oracle (`docs/research/keyer-and-key-interfaces.md` F3, F4, F12; `docs/research/keyer-verification-and-key-input-network.md` F6 to F8, F14).
- **Technology TRL.** 2 (semantics defined, no code).
- **cwht maturity.** 3-equivalent: reference behavior and golden vectors exist, timing tolerance and HostUnit harness (simulated clock at 100 us steps) defined.
- **Gaps.** No crate; MC/DC cannot be instrumented by rustc (RSK-010; RMM tailoring of SWE-219 pending); safety manager, sequencer, DSP and power monitor have no reference models yet.
- **Plan to PDR.** Workspace skeleton FW-B0 (`cwht-app`, `cwht-core`, `cwht-hal-mock`), keyer golden-vector generator checked in under `tools/`, HostUnit tests for the keyer and debounce, sequencer model with the T/R timing table, safety-manager state machine with its MC/DC matrix designed by hand while tooling is open. Exit: 4-equivalent for keyer and debounce; 3 for the rest. Risk: RSK-012.

### 3.20 Host-first verification method (SW, process)

- **Heritage.** rustos methodology (author, reviewer and test-author separation, per-file review, traceability gate); the mock-driver test against `api` as it stands works on the host (`docs/research/rustos-toolchain-proof.md` F13; `docs/plan/semp.md` §7.5).
- **Maturity.** Demonstrated at 4-equivalent (a HostUnit test with mocked drivers ran); the pattern needs the `time::Clock` and `time::Alarm` trait shapes of WP-03 before the keyer can be tested with a simulated clock.
- **Gaps.** Coverage tooling not installed (cargo-llvm-cov, cargo-nextest, cargo-geiger, owner approval needed); MC/DC not measurable (RSK-010); SWE-186 repeatability rules (two identical runs) to be scripted.
- **Plan to PDR.** Install the pinned cargo tools; `tools/sw_gate.sh`; RMM disposition for SWE-219 (condition coverage plus manual MC/DC matrices, or bounded decision complexity).

### 3.21 Emulator `ACC-EMU-001` (tool)

- **Heritage and evidence.** c1570/rp2350js at commit `af0114cb`, ARM mode, characterized with a set of purpose-built firmware images and register probes: TIMER0 alarms and NVIC entry pass (alarm up to 1 us early), PWM slices 0 to 7 pass for period and duty, ADC, I2C0, SPI0 and UART0 pass with zero bus time, SIO GPIO pass; clock tree, TICKS, GPIO edge interrupts, NVIC priorities, SysTick, PWM slices 8 to 11, flash and USB fail or are partial; watchdog fires at 0.53x; the GPIO coprocessor path is a NOP, which is why cwht uses SIO GPIO only (`docs/research/emulator-accreditation-and-timer-irq.md` F1 to F12). Known answers KA-1 to KA-3 with hashes and the credit scope are written as the accreditation case (F13). Alternatives Renode, Wokwi and QEMU were evaluated and rejected or kept as fallback (`docs/research/rp2350-emulation-options.md`).
- **Maturity.** Characterized and ready for accreditation; credited scope is event ordering and register plumbing only, never durations (charter §9, SI-026).
- **Gaps.** Accreditation not yet approved (ADR due PDR); upstream issues A to D unfiled; single-maintainer dependency (mirror fork needed); patched tree would be `ACC-EMU-002` by CR; `npx vitest run` not executed in the study.
- **Plan to PDR.** Vendor as a submodule with a mirror fork; reproduce KA-1 to KA-3; ADR selecting the tool and recording the credit scope in `tools/toolchain.lock.md`; file the upstream issues; decide the patch set for GPIO IRQ decode, PPB offsets and the PWM map. Risk: RSK-003.

### 3.22 Bench instruments and enabling hardware

- **Heritage.** Owner's NanoVNA, 50 ohm BNC dummy load, bench supply and multimeter (SI-013); tinySA Ultra purchase decided (SI-034); sigrok-pico on a second Pico 2 proposed for logic capture; reference antennas and mismatch fixtures proposed (`docs/research/keyer-verification-and-key-input-network.md` F10; `docs/research/antenna-and-erp.md` implications; `docs/research/audio-output-and-hearing-safety.md` A6).
- **Maturity.** Commercial instruments; project procedures not yet written.
- **Gaps.** No calibrated power attenuator for 5 W into the tinySA; tinySA minimum RBW for the keying spectrum unverified (Low); sigrok-pico and `sigrok-cli` on macOS unverified (R-KN2); no USB-serial adapter (Morse-on-LED read-out is the fallback for dev-board tests); multimeter AC accuracy at 700 Hz unknown; no calibrated signal source for MDS (OnAir comparison accepted).
- **Plan to PDR.** Owner buys the attenuator and the second Pico 2; confirm the tinySA RBW; write the TRR procedures for spurious (span 9 kHz to 1.5 GHz, 2f, 3f and 7f reported), band-edge power, keying spectrum, audio ceiling and antenna screen. Risk: RSK-011.

## 4. Heritage assessment (SEMP §7.5 expanded)

| Heritage product | Inherited | Differences (form, fit, function, environment) | Re-qualification required | Recorded in |
|---|---|---|---|---|
| rustos boot, vectors, linker script, GPIO driver | Used as is | Identical module, cwht pin map and clock tree added | Re-run its tests under the cwht toolchain pin; reused-software register (SWE-211) | `docs/process/07-software-engineering-plan.md` §17.1 |
| rustos methodology | Process pattern | Agent invocations instead of people | None; differences recorded | `docs/process/08-agent-briefing.md` §7 |
| FT-290R, IC-202, Mizuho MX-2 architecture | Single-conversion superhet pattern, performance class | 3.3 V rails, synthesizer LO instead of VXO, pocket form | Full re-derivation; no circuit copied | `docs/design/concept.md` §7.3 |
| Anglian, Kuhne, Elecraft XV front-end practice | Device families, BPF and mixer level, relay T/R rationale | 12 V transverters at 100 mA class versus a 3.3 V handheld budget | Noise and gain budget, device choice in TS-001 | TS-001 |
| NXP AFT05MS004N 136 to 174 MHz reference circuit | Match topology, layout hints | cwht stackup, 2S supply with ALC, enclosure thermal path | Behavioral model and simulation; EOL lifetime buy | TS-003 |
| Mitsubishi AN-VHF-053-A harmonic and efficiency data | Harmonic margin logic for the LPF goals | Different device unless a waiver appears | Not transferable; used only to size the LPF margin | `docs/design/concept.md` §7.2 |
| QRP Labs QCX and QMX keying and break-in practice | 5 ms shape, hang-time convention, T/R sequencing order, mono-plug notes | 144 MHz, gate-bias node, relay instead of solid-state switch | LTspice of loop and ramp; sequencer model | TS-006, `ICD-TX-SW` |
| Curtis, K1EL WK3, K3NG, YACK keyer semantics | Mode A and B definitions, watchdog figure, tunable ranges (narrowed) | Rust `no_std` implementation, TIMER0 timing | Golden vectors against an independent reference model | `docs/test_cases/sw/keyer-golden-vectors.json` |
| TI BQ25887, ABLIC S-8252, TI BQ29209 application circuits; Pico 2 VSYS OR-ing figure | Topologies and thresholds | Load-while-charging behavior, holder NTC placement, RF-quiet layout | In-context analysis, bench charge test with dummy cells | `ICD-PWR-CTL`, TRR procedures |
| Sharp memory LCD and the `sharp-memory-display` crate | Interface behavior (EXTCOMIN, frame format) | Own driver against `bus::SpiTx`, no backlight | Host golden frames, PNG renderer | SW-UI |
| TE Axicom HF3 datasheet | Ratings and timings | 6 V coil from a 6.0 to 8.4 V pack, cold switching preferred | Stock check, sequencer transient | `ICD-RX-TX` |
| KX4O and G4ILO antenna measurement methods; OET 65 B exposure method | Relative-EIRP procedure; time-averaging recipe | cwht enclosure and whip | Antenna screen at TRR; RF exposure evaluation at PDR, CDR, TRR | V&V plan; RFX evaluation |
| Owner's bench inventory | Instruments | Added tinySA Ultra and logic capture | Calibration checks per test report | Test reports |

Conclusion: no hardware design is inherited; every reused element is either identical (rustos runtime, catalog parts used within their datasheets) or a starting point re-derived under cwht's own analysis, which is what SEMP §7.5 requires.

## 5. Toolchain proof (01 §4.3 row 20)

Locked versions are in `tools/toolchain.lock.md` (observed 2026-09-25). Proofs below are the research demonstrations; a tool validation record `TV-NNN` with a committed fixture is still required before any output counts as evidence (CM plan §9).

| Tool | Locked version | Proof performed | Sanity check status | Gap | Due |
|---|---|---|---|---|---|
| LTspice for macOS (CrossOver) | 26.0.2.1 | Batch run through the bottle's `wine` with the full `LTspice.exe` path works; consent dialog suppressed by `CaptureAnalytics=false` (SI-027); `.raw` parsed by `ltspice` 1.0.6 and `PyLTSpice` 6.0.1, -3 dB point matches the analytic 1000.000 Hz; the cw-selectivity Monte Carlo batch ran (`docs/research/ltspice-batch-macos.md` F3, F4, F8, F9; `docs/research/sim/cw-selectivity/`) | Demonstrated, TV pending | The documented `LTspice -b` launcher form is broken in 26.0.2; wrapper depends on bundle layout; one Wine bottle forbids parallel runs | PDR (TV) |
| KiCad kicad-cli | 10.0.6 | ERC and DRC known answers deterministic with JSON reports; PCBWay export recipe (11 Gerbers, job file, 2 drill files, CPL with `--smd-only --exclude-dnp`, BOM) verified on a fixture board (`docs/research/verification-tooling-inventory.md` F1 to F7; `docs/research/pcbway-export-and-vendor-questions.md` F1 to F12) | Demonstrated, TV pending | Global library tables absent (project-local tables fix it); published DRC schema is invalid JSON (patched copy needed); SWIG `pcbnew` leaves in KiCad 11 | PDR (TV), CDR (export wrapper) |
| Rust toolchain | rustc 1.98.0, cargo 1.98.0, target `thumbv8m.main-none-eabihf`, picotool 2.3.0 | Host build, `cargo test -p api`, `cargo pico2` dev and release, end-to-end application build against the local rustos checkout offline, ELF to UF2 conversion and `picotool info` without a device (`docs/research/rustos-toolchain-proof.md` F1 to F6) | Demonstrated, TV pending | cargo-llvm-cov, cargo-nextest, cargo-geiger, cargo-audit, cargo-deny not installed (owner approval); MC/DC instrumentation removed from rustc (RSK-010); `rust-toolchain.toml` pin to be added at the first firmware commit | PDR (install, TV); CDR (picotool, cargo-binutils TV) |
| Python venv | 3.13.5 with jsonschema 4.26.0 | `tools/validate_docs.py` and schema validation in use; proposed analysis pins (numpy, scipy, scikit-rf, spicelib, matplotlib, lizard, pytest) install cleanly and pass known answers in a scratch venv (`docs/research/verification-tooling-inventory.md` F15) | Demonstrated, TV pending at SRR for jsonschema and traceability | Analysis pins not yet in `tools/requirements.txt` | SRR (schema and traceability TV), PDR (analysis stack) |
| OpenSCAD | 2021.01 installed at `/Applications/OpenSCAD-2021.01.app` (Intel binary under Rosetta) | CLI exported STL, 3MF, CSG and PNG renders of a representative half-shell; cube known answer passes (`docs/research/enclosure-cnc-and-openscad-pipeline.md` B2; `docs/research/verification-tooling-inventory.md` F11) | Demonstrated, TV pending | `tools/toolchain.lock.md` records OpenSCAD as not installed at `/Applications/OpenSCAD.app`; the lock entry needs the actual path (section 8); snapshot 2026.09.23 versus 2021.01 decision | PDR |
| FreeCAD headless STEP stage | 1.1.3 (Homebrew cask, not installed) | Install approved (SI-032); CSG-to-B-rep import path verified from source reading only (B4, B5) | Not demonstrated | STEP acceptance checks (valid, one solid, no BSpline faces, volume match) never run | PDR (smoke shell), CDR (order STEP) |
| Emulator rp2350js | commit `af0114cb`, node v25.9.0 | Eleven images and three probes; known answers KA-1 to KA-3 defined with hashes (`docs/research/emulator-accreditation-and-timer-irq.md` F12, F13) | Characterized, accreditation pending | Not vendored; ADR due PDR | PDR |
| kicad-cli rendering, pymupdf | in inventory | Rendering for visual closure needs no extra system packages (F20 of the tooling inventory) | Demonstrated | none | none |
| Bambu Studio CLI (fit-check prints) | 02.08.02.61 | Project 3MF export works; headless slicing for the H2C fails on filament mapping (B7) | Partial | Manual GUI slicing step remains and is recorded in the fit-check procedure | CDR |

## 6. Advancement plan to PDR (AD2 step)

Every Red or Yellow element in section 2 maps to at least one activity below. The plan is the Phase B technical content that `docs/plan/schedule.md` places on Saturday 2026-09-26; items marked "owner" need the owner's hands or account.

| Element | Gap closed | Activity | Evidence product | Owner | Gate |
|---|---|---|---|---|---|
| Frequency generation | Candidate choice, phase noise, spur map | TS-002; extract LMX2571 plots; Si5351 at 144 MHz measured or sourced; spur map with the chosen IF | `docs/decisions/trade-studies/TS-002-*.md`; phase-noise and spur budget with checker | Claude; owner for a bench measurement | PDR |
| PA and line-up | Device choice, model | Retrieve ST and Guerrilla documents; TS-003; behavioral LTspice PA model per candidate; LPF with SRF models; owner lifetime buy if EOL device chosen | TS-003; `hardware/sim/pa-*.asc` with `tools/ltspice_check.py` results | Claude; owner (documents behind bot walls, purchase) | PDR |
| ALC, envelope, cutoff node | Loop and ramp design | TS-006; transient simulations; `bw.py` in `tools/` | TS-006; envelope spectrum plot with 26 dB bandwidth | Claude | PDR |
| T/R and receiver protection | Stock, sequencing | Stock check; sequencer transient; protection analysis | `ICD-RX-TX` Draft; deck and checker | Owner (stock), Claude | PDR |
| Antenna port | Tolerance stack | Boss and jack tolerance analysis; pigtail alternative | `ICD-TX-ANT` update; enclosure model | Claude | PDR; fit print at CDR |
| Receiver front end | Budget | Cascade noise and gain budget; BPF and LNA simulation; birdie map | Budget note in `docs/design/budgets.md`; decks | Claude | PDR |
| Selectivity A | Quotes | KVG and Inrad quotes with case drawings | Quote records in the PDR package | Owner (email) | PDR |
| Selectivity B | PIO I2S, DSP | PIO I2S loopback on a Pico 2 with a PCM1808 breakout; DSP chain HostUnit tests; second-source ADC | Loopback report; HostUnit results | Owner (breakout purchase and run), Claude | PDR |
| Power | Noise, second sources, thresholds | Buck and LDO PSRR simulation; second sources; S-8252 calculation; cell curve | Decks; `ICD-PWR-CELL`, `ICD-PWR-CTL` | Claude | PDR |
| USB input | Path rating | Pico 2 VBUS path measurement at 0.5, 1.0 and 1.5 A; DCP detection experiment | Measurement record; TS-005 | Owner | PDR |
| Pico 2 assembly | Vendor confirmation | Send the PCBWay email (module reflow, CPL rotation, via fill, impedance report) | Vendor reply in the CDR package | Owner (send), Claude (draft exists) | Send before PDR; answers by CDR |
| Key inputs, jacks | ICDs, RF immunity | `ICD-CTL-KEY`, `ICD-CTL-PHONES`; choke analysis; TPA6132A2 short data | ICD stubs (before SRR) and Drafts | Claude | SRR stubs; PDR |
| Display and UI | Driver, footprint, stack | Host golden frames and PNG renderer; footprint and 3D overlay render; panel stack-up | Renders in the PDR package; `ICD-CTL-ME` Draft | Claude | PDR |
| Audio | Network, harness | LTspice of the network; host harness for limiter, AGC, fades | Deck and results; HostUnit results | Claude | PDR |
| Enclosure and PCB | Model, STEP, quotes, thickness | Envelope model; FreeCAD install and `scad2step.py` on the smoke shell; instant quotes (enclosure; PCB at both thicknesses); TS-004 | STEP acceptance log; quotes as TPM inputs; TS-004 | Owner (install, quotes), Claude | PDR |
| rustos drivers | WP-13, 01 to 04 | Implement with contract tests and emulator readback | rustos PRs at a pinned commit; `cwht-hal-mock` | Claude | PDR (WP-01 to 04), CDR (rest) |
| `cwht-core` | Skeleton, keyer | FW-B0 skeleton; keyer and debounce HostUnit tests from golden vectors; sequencer and safety-manager models | `tools/sw_gate.sh` exit 0; test reports | Claude | PDR |
| Host method | Tools | Install pinned cargo tools; RMM disposition for SWE-219 | `tools/toolchain.lock.md` update; RMM row | Owner (approval), Claude | PDR |
| Emulator | Accreditation | Vendor and mirror; reproduce KA-1 to KA-3; ADR; file upstream issues | ADR; `tools/toolchain.lock.md` ACC-EMU-001 entry; `docs/vv/reports/ACC-EMU-001/` | Claude; owner (mirror fork under the owner's account) | PDR |
| Tools | TV records | Fixtures and known-answer suite for LTspice, kicad-cli, OpenSCAD, Rust, Python | `tools/validation/`, `docs/cm/tool-validation/TV-NNN` | Claude | PDR |
| Bench | Instruments and procedures | Attenuator and second Pico 2 purchase; tinySA RBW check; TRR procedures | Procedures in `docs/test_cases/`; inventory update | Owner (purchases), Claude | PDR (procedures), TRR (instruments) |

## 7. Technology Development Plan disposition (Table G-3 item 5.8)

Finding: **no technology below TRL 6 is required by the cwht concept.** Every hardware element is a catalog part in mass production or a published circuit technique in fielded amateur and commercial radios (section 3, technology TRL column); the controller module and the existing rustos runtime are at TRL 6 to 7 for the identical unit; the tools are in general use. What is immature is cwht's own integration of these technologies, which is design maturity governed by the SEMP §6.0 TRL-equivalent gates (4 by PDR, 5 by CDR for RF blocks) and tracked in this assessment and the risk register, not by a Technology Development Plan. The disposition of 01 §4.7 (Not Applicable) therefore stands.

Watch items that could change this finding, each already carried as a risk or a risk candidate: the PA device supply (EOL device with finite stock, single-source alternatives; RSK-005), PIO I2S on rustos for candidate B (software integration never demonstrated on rustos; falls back to candidate A), MC/DC measurement for Rust (a process-tooling gap, RSK-010, dispositioned in the RMM), the emulator's uncredited peripherals (RSK-003, mitigated by HostUnit primacy and Bench for timing). If any of these were to require new technology rather than integration work, this document is updated and a research report and risk are opened, as 01 §4.7 requires.

## 8. Open items and owner decisions

1. **Location pointer.** `docs/process/01-lifecycle-and-reviews.md` §4.3 row 20, §7 row 16 and `docs/plan/semp.md` §6.0 name `docs/research/technology-assessment.md`; this file is at `docs/plan/technology-assessment.md`. Editorial fix by the owners of those documents before SRR (charter §8: minor editorial changes are logged, not boarded).
2. **Toolchain lock OpenSCAD entry.** The lock records OpenSCAD as not installed at `/Applications/OpenSCAD.app`; the tooling inventory and the enclosure report ran `/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD` successfully. The lock maintainer records the actual path and version and decides the 2021.01 versus 2026.09.23 snapshot question (verification tooling inventory decision 12).
3. **SEMP §3.1 wording.** The SEMP system description says "USB-C for charging and firmware load"; the owner decision is the Pico 2 module's micro-USB (SI-022). Editorial fix to the SEMP.
4. **Owner actions that gate PDR evidence:** install FreeCAD 1.1.3 (SI-032); approve and install the pinned cargo tools; send the PCBWay email; request KVG and Inrad quotes; buy a PCM1808 breakout if candidate B stays in TS-001; buy the tinySA attenuator and a second Pico 2; run the Pico 2 VBUS path measurement; create the mirror fork of rp2350js; check distributor stock for the relay, display, ZIF, encoders and jacks with timestamps.
5. **Owner decision at SRR:** accept this assessment's two-scale method and the TRL-equivalent definitions of section 1.1 as the project's TMA terminology (SE HB App. G asks that terms be fixed before levels are assigned); accept the section 7 finding.
6. **Confidence.** Technology TRL assignments are High (datasheets, vendor status pages and distributor stock read on 2026-09-25 as cited). Design-maturity levels are High where a report contains the derivation or simulation (sections 3.4 to 3.7, 3.10, 3.11, 3.14, 3.17, 3.19) and Medium where they rest on part selection alone. Stock and lifecycle statements are dated 2026-09-25 and expire at each gate (re-check rule of the research reports).

## 9. Update rule

This assessment is re-issued at PDR, CDR, TRR and SAR with a delta table (01 §5.3 row 16, §7): elements whose maturity changed, new gaps, closed gaps, and any element that missed its gate level with the fallback taken. The PDR issue is the final TMA of SE HB App. G ("performed just prior to PDR") for rev A.
