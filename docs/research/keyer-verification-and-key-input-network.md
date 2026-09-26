# Research report: keyer timing verification, hand-key semantics, key input network and stuck-key controls (reconciled numbers)

**Assignment key:** keyer-numbers. **Date:** 2026-09-25. **Author:** research agent (independent invocation). **Status:** input to SRR/PDR requirements and ICD work; not a baseline. Extends, and where necessary corrects, `keyer-and-key-interfaces.md`, `rustos-toolchain-proof.md` (F10, F11, F13, implications) and `2m-cw-transceiver-reference-designs.md` (F27 to F31). Every number is flagged **Sourced** (quoted from a primary document), **Derived** (computed here from sourced inputs, formula shown) or **Proposal** (a design choice for the owner to ratify). TBR items are named as such.

Stakeholder inputs that arrived after the three reports were written and that this report applies: SI-026 (host-first verification with dependency injection; emulation optional and secondary), SI-033 (speed range 5 to 50 WPM accepted; drivers developed upstream in rustos), SI-034 (owner's straight key and paddle both carry 3.5 mm TRS plugs, brands unknown; tinySA Ultra will be purchased), SI-035 (full QSK versus semi break-in still open).

## 1. Question

Produce one reconciled proposal for the cwht keyer and key interface covering: (1) the keyer timing verification approach (HostUnit with a simulated clock as primary evidence, golden vectors from the Curtis 8044 mode A and B definitions and the ITU-R M.1677-1 element ratios, Emulation limited to event ordering, and a Bench method that uses a Pico 2 as the logic capture because the owner has no oscilloscope); (2) hand-key semantics through the envelope shaper and T/R sequencer (key-up overhang, minimum radiated element, semi-break-in hang with a hand key, and how the paddle keyer shares the shaper); (3) a single derivation of the key and paddle input network from RP2350 VIL/VIH, hysteresis, erratum E9, contact resistance, RF pickup at 5 W and ESD, giving one pull-up, series resistor, RC constant, clamp part and the debounce numbers, with TBRs named; (4) mono-plug and stuck-key hazard controls (power-on interlock, paddle watchdog, hardware PA-enable cutoff with T_max and parts, and its relation to the CPU watchdog); (5) one reconciled number set (speed and tolerance, envelope and keying-sideband target, sidetone, break-in hang, ratio and weight) with each number flagged; and correct the contradictions between the three earlier reports.

## 2. Method

1. Read: `docs/process/00-charter.md` sections 9 to 11; `docs/research/keyer-and-key-interfaces.md` (all); `docs/research/rustos-toolchain-proof.md` F10, F11, F13, F14, peripheral map, implications; `docs/research/2m-cw-transceiver-reference-designs.md` F27 to F31 and implications 2, 3, 17, 18; `docs/requirements/l0-stakeholder/stakeholder-inputs.md` (SI-001 to SI-035); `docs/risk/register.md` (RSK-012 and the bench-instrument risks); `docs/process/04-verification-and-validation.md` sections 6.1, 6.2 and the platform-independent-logic definition; `docs/references/md/swehb/swe-134-safety-critical-software-design-requirements.md` (items a to l).
2. No file named as the "completeness critic" output exists in the repository (searched `docs/`, `tools/`, `result.json` for "critic" and "contradiction"); the contradictions were therefore re-derived by cross-reading the three reports and are listed in F1 with the conflicting sentences.
3. Primary documents downloaded into the session scratchpad and converted with `pdftotext -layout` (poppler): RP2350 datasheet, current online build 2025-07-29, build-version d126e9e-clean, 1380 pages (`https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf`); Curtis 8044 application note 1/22/92 (`https://users.ox.ac.uk/~malcolm/radio/8044print.pdf`); Nexperia 74LVC1G123 product data sheet Rev. 8, 14 August 2023; Nexperia PESD3V3L2BT product data sheet 27 June 2023; TI TPD2E001 SLLS684I (July 2006, revised March 2016); TI TPD2E2U06 SLLSEG9C (June 2013, revised December 2019); Maxim/ADI MAX6369 to MAX6374 datasheet 19-1676 Rev 6 3/15 (analog.com refused the fetcher; Farnell mirror `https://www.farnell.com/datasheets/1904457.pdf`); ADI LTC6993-1/-2/-3/-4 datasheet 69931234fb (DigiKey media mirror). 47 CFR 97.307 and 97.119 were pulled from the eCFR versioner API at issue date 2026-09-23 (`https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.307` and `...section=97.119`) and the XML stripped to text.
4. Web pages read: sigrok-pico README (`https://github.com/pico-coder/sigrok-pico`), tinySA Ultra specification wiki (`https://tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification`). Distributor stock and price signals come from search-result snippets observed 2026-09-25 about 11:45 PDT; DigiKey product pages returned HTTP 403 to the fetcher, so stock counts are Low confidence. The session's web-search budget was exhausted after the part searches; two intended searches (sigrok-pico sample rates, tinySA close-in phase noise) were replaced by direct page reads.
5. Two Python scripts were written in the scratchpad and run: `derive.py` (input-network voltages, RC constants, RF attenuation, ESD currents, cutoff-timer RC values, quantisation and hang tables) and `keyer_ref.py` (a reference iambic keyer model that generates the golden vectors and the debounce vectors). Outputs are excerpted in the findings; formulas are stated inline so a reviewer can recompute them by hand.
6. All work was headless and read-only outside `docs/research/` and the scratchpad; no packages were installed; the rustos repository was not modified (charter section 11).

## 3. Findings

### F1. Contradictions between the three reports, with the reconciled resolution

| # | Topic | keyer-and-key-interfaces.md | rustos-toolchain-proof.md | 2m-cw-transceiver-reference-designs.md | Resolution (detail in the finding named) |
|---|---|---|---|---|---|
| C1 | External pull-up on key inputs | CTL-KEY-03: "external pull-up of 4.7 to 8.2 kΩ to 3.3 V (erratum E9 bound)" | REQ (CTL/ICD): "internal pull-up enabled, an external pull-up of about 10 kOhm" | not addressed | 10 kΩ external, internal pull-up and pull-down both disabled. The E9 8.2 kΩ figure bounds pull-downs, not pull-ups (F3). The binding constraint on a pull-up input is the closed-contact VIL margin, which 4.7 kΩ fails with a 1 kΩ series resistor and 500 Ω contact (F3, F4) |
| C2 | Speed range | SW-KEY-03: 5 to 50 WPM, "owner may extend to 60" | REQ: "over 5 to 40 WPM" | REQ 3: "from at least 5 to 40 WPM" | 5 to 50 WPM in 1 WPM steps (Sourced, SI-033); HostUnit golden vectors additionally run at 60 WPM to show margin (Proposal) |
| C3 | Element timing tolerance | SW-KEY-02: "+/-1 ms or +/-2 % of a dit, whichever is larger" | "accurate to within 1 percent of 1200 ms / WPM" | none | +/-1 % of nominal or +/-0.5 ms, whichever is larger, at the engine output before the shaper (F8) |
| C4 | Keying-sideband offset | SW-KEY-09: "<= -60 dBc at abs(offset) >= 500 Hz" | none | REQ 2: "at least 60 dB down beyond +/-300 Hz" | Requirement at 500 Hz (includes PA distortion, closable by Analysis of the measured envelope); 300 Hz is the design goal for the ideal shaper output (F12) |
| C5 | Envelope rise and fall | F10 "never below 4 ms"; CTL-KEY-08 "2 to 10 ms"; SW-KEY-09 "5 ms +/-1 ms at >= 25 WPM ... may lengthen to 8 ms below 15 WPM" (speed-adaptive) | none | REQ 2: "default to 5 ms (10 to 90 %), be configurable" | 5 ms 10-to-90 % raised cosine (total ramp 8.5 ms), range 3 to 8 ms in 1 ms steps, not speed-adaptive; the 10-to-90 % definition is made explicit because the total ramp is 1.7 times longer and sets the overhang (F11, F12) |
| C6 | Bench method for timing and envelope | SW-KEY-08: "Bench with oscilloscope on key, T/R and RF envelope" | Bench "sidetone frequency measured against a known reference" | REQ 2: "Bench spectrum at 60 WPM per ARRL method" | The owner has no oscilloscope (SI-013). Bench uses a second Pico 2 as a sigrok logic capture plus the Pico ADC for the detected RF envelope; the tinySA Ultra's close-in phase noise makes the -60 dBc at 500 Hz figure unverifiable on it (F10) |
| C7 | Key-down-to-RF delay | SW-KEY-08: "key-down-to-RF delay <= 5 ms" (from the KX2 TX DLY figure) | none | F28/F29: relay operate 3 ms max plus 5 ms shaping | In semi break-in the first element after changeover needs a T/R lead-in (5 ms) plus half the ramp: about 12 ms to RF 50 %; later elements about 7 ms. The 5 ms figure is replaced by the sequencer budget in F11 |
| C8 | Watchdog | CTL-KEY-07: "hardware or independent-timer mechanism ... T_max (owner: 10 to 60 s)" | REQ: "A watchdog of at most 2 s shall be enabled before the transmitter can be keyed" | none | Three independent layers with different jobs: CPU watchdog 2 s (firmware hung), hardware key-down cutoff 10 s (firmware alive but TX line stuck), firmware timeouts 5 s / 128 elements (operator or plug faults) (F13) |
| C9 | Full QSK | SW-KEY-08: "Full QSK: receiver re-enabled within 1 dit ... after the RF envelope has decayed" written as a requirement | none | F28: relay timing "rules out true QSK at paddle speeds unless ... solid-state" | Full QSK is conditional on the T/R trade (SI-035); semi break-in with an 8-dit hang is the default; QSK becomes a requirement only if a solid-state switch is selected at PDR (F11) |
| C10 | Emulation as timing evidence | SW-KEY-02, -08, -12 assign "[Emulation ...]" for timing | Work packages cite emulation for alarms | none | Charter section 9 and SI-026: Emulation is for event ordering only, never timing. Timing evidence moves to HostUnit (primary) and Bench (F8, F9) |
| C11 | TVS figures | F11: PESD3V3L2BT "VCL = 26 V", "IRM = 90 nA" | none | none | 26 V is the clamping voltage at the 15 A, 8/20 µs surge; at 1 A the datasheet gives 8 V max. 90 nA is typical; the maximum is 2000 nA. Also its 101 pF diode capacitance was not mentioned. Corrected in F5; a unidirectional part is preferred |
| C12 | Debounce numbers | SW-KEY-06: 3 consecutive 1 ms samples for paddles, 5 ms default in Straight mode | "software debounce" without numbers | none | One asymmetric filter for both key types: close confirmed after 2 consecutive closed samples (2 ms), open after 5 consecutive open samples (5 ms), TBR after measuring the owner's key and paddle (F6) |
| C13 | Sidetone | SW-KEY-07: 300 to 1000 Hz, default 600 or 700 Hz (decision) | peripheral map: PWM "fixed TOP for 600 to 800 Hz" | none | 300 to 1000 Hz in 10 Hz steps, default 600 Hz, locked to the receiver CW offset (F14) |
| C14 | Input RC constant | CTL-KEY-05: "RC low-pass >= 10 µs" | none | none | RC is an RF filter, not a debounce: 10 kΩ x 4.7 nF = 47 µs on release, about 5 µs on closure; debounce is digital (F4, F6). The Curtis 10 ms RC (1 MΩ x 0.01 µF) was the 8044's debounce and is not reused |
| C15 | Input mechanism | CTL-KEY-02 ">= 1 kHz or edge-timestamped <= 1 ms"; SW-KEY-12 "hardware timer/PIO path" | DECISION: 1 kHz timer-sampled polling recommended, PIO deferred | none | 1 kHz sampling from TIMER0 ALARM1 in an interrupt, element timing from ALARM0; no PIO (F8) |

### F2. RP2350 facts that drive the input network and the safety outputs (Sourced)

All from the RP2350 datasheet build 2025-07-29 unless stated.

- Table 1436 "Digital IO characteristics", IOVDD = 3.3 V: VIH minimum 2.0 V (standard and FT pads); VIL maximum 0.8 V; VHYS 0.2 V with the Schmitt trigger enabled; IIN (pin input leakage) 1 µA maximum; pull-up RPU 32 to 86 kΩ; pull-down RPD 36 to 113 kΩ; VOL 0.5 V maximum and VOH 2.62 V minimum at the programmed drive.
- Table 1433 absolute maximum: VPIN_FT -0.5 V to +5.5 V at IOVDD 3.3 V, "IOVDD must be present". Table 1434 ESD: HBM 2 kV all pins, 4 kV "Digital (FT) pins only" (JEDEC JS-001-2012), CDM 500 V (JESD22-C101E).
- Table 853 `PADS_BANK0: GPIO0` reset values: ISO = 1, OD = 0, IE = 0, DRIVE = 4 mA, PUE = 0, PDE = 1, SCHMITT = 1, SLEWFAST = 0. `IO_BANK0: GPIOn_CTRL.FUNCSEL` resets to 0x1f (NULL). Section 9.7: "the input enable control (GPIO0.IE) resets to 0 (input-disabled)". So after any chip reset a GPIO is not driven, has a 36 to 113 kΩ pull-down, and its input buffer is off.
- Erratum RP2350-E9 ("Affects RP2350 A2"; "Fixed by RP2350 A3"): "When the pad is set as an input (input enable is enabled and output enable is disabled) and the voltage on the pad is within the undefined logic region, the leakage current exceeds the standard specified IIN leakage level. During this condition the pad can source current (... typically around 120μA). This leakage will hold the pad at around 2.2 V"; "The pad pull-down (if enabled) is significantly weaker than the leakage current"; "Driving / pulling the pad input low with a low impedance source of 8.2 kΩ or less will overcome the erroneous leakage"; "The erroneous leakage only occurs (and continues to occur) when the pad input enable is enabled"; "The pad pull-up still works. If enabled it will pull the pad to IOVDD as it will pull the input voltage out of the problematic range."
- Watchdog: `WATCHDOG: LOAD` bits 23:0, "The maximum setting is 0xffffff which corresponds to approximately 16 seconds" (section 12.9.7); the tick comes from the TICKS block (section 12.9.2, 8.5), 1 µs when clk_ref is the 12 MHz crystal.
- ADC: "Capturing a sample takes 96 clock cycles (96 x 1/48 MHz) = 2 μs per sample (500 kS/s)" (section 12.4.3).

### F3. Erratum E9 reasoning corrected: pull-up inputs are helped by the leakage; the binding constraint is the closed-contact VIL margin (Derived)

The E9 leakage sources current into a pad that sits between VIL and VIH and pushes it toward 2.2 V. For a switch-to-ground input with a pull-up, the pad is either held low by the closed contact (low impedance, the leakage adds at most 120 µA through the series path) or rising toward 3.3 V through the pull-up, where the leakage pushes in the same direction. The 8.2 kΩ figure in the erratum is the impedance needed to pull a pad *down* against the leakage; it does not bound a pull-up. The keyer report's "E9 bound" of 4.7 to 8.2 kΩ and the rustos report's "10 kOhm for RF and ESD robustness" were both reasoning from the wrong constraint.

The real constraint is the pad voltage with the contact closed: V_pad = 3.3 V x (R_s + R_c)/(R_pu + R_s + R_c) + I_leak x (R_pu || (R_s + R_c)), which must stay below VIL = 0.8 V with margin. Results from `derive.py` (I_leak = 120 µA applied as a worst case even though it only flows in the undefined region):

| R_pu | R_s | R_c (contact) | V_pad closed, no leakage | V_pad closed, 120 µA | Margin to 0.8 V | Closed-contact current |
|---|---|---|---|---|---|---|
| 4.7 kΩ | 470 Ω | 500 Ω | 0.565 V | 0.661 V | +0.139 V | 0.58 mA |
| 4.7 kΩ | 1.0 kΩ | 100 Ω | 0.626 V | 0.733 V | +0.067 V | 0.57 mA |
| 4.7 kΩ | 1.0 kΩ | 500 Ω | 0.798 V | 0.935 V | fails | 0.53 mA |
| 10 kΩ | 1.0 kΩ | 100 Ω | 0.327 V | 0.446 V | +0.354 V | 0.30 mA |
| 10 kΩ | 1.0 kΩ | 500 Ω | 0.430 V | 0.587 V | +0.213 V | 0.29 mA |
| 10 kΩ | 2.2 kΩ | 100 Ω | 0.617 V | 0.841 V | fails | 0.27 mA |
| 10 kΩ || internal 32 kΩ (7.6 kΩ) | 1.0 kΩ | 500 Ω | 0.544 V | 0.694 V | +0.106 V | 0.39 mA |

Conclusions (Derived): with the 1 kΩ series resistor that ESD protection wants (F5) and a 500 Ω contact-resistance allowance (keyer report CTL-KEY-03), the pull-up must be at least 10 kΩ, and the internal pull-up should be left off so that the margin is not eroded by its 32 kΩ minimum. Open-contact pad voltage is 3.3 V - 1 µA x 10 kΩ = 3.29 V (IIN maximum), far above VIH 2.0 V. If the reset-default pull-down (PDE = 1) were left enabled, the open-contact voltage would drop to 3.3 V x 36/(36 + 10) = 2.58 V worst case; still above VIH but the firmware must clear PDE explicitly (Table 853 reset value), which is a pad-configuration inspection item.

### F4. The key input network, derived once (Derived and Proposal)

Per line (tip = dit or hand key, ring = dah), from the jack toward the RP2350 pad:

| Ref | Part | Value | Purpose | Flag |
|---|---|---|---|---|
| J1 | 3.5 mm TRS jack, sleeve to signal ground at the jack | | keyer report F1 convention | Sourced (keyer report) |
| C1 | C0G/NP0 0603 50 V | 100 pF | first RF shunt at the connector; self-resonance above 500 MHz keeps it capacitive at 144 MHz | Proposal |
| D1 | TI TPD2E2U06DRLR (one part covers tip and ring) | | IEC 61000-4-2 clamp at the connector (F5) | Proposal |
| R1 | thick-film 0603 1 % 100 mW | 1.0 kΩ | ESD and abuse current limit (Curtis: 470 Ω to 1 kΩ), RF low-pass with C2 | Sourced range, Proposal value |
| R2 | 0603 1 % | 10 kΩ to 3V3 | pull-up; sets closed-contact current 0.30 mA | Derived (F3) |
| C2 | X7R 0603 | 4.7 nF | RF low-pass at the pad node; absorbs the residual ESD transient | Proposal |
| D2 | BAT54S dual Schottky at the pad node to 3V3 and ground | | secondary clamp so a +12 V or -5 V abuse never exceeds the pad absolute maximum (F5) | Proposal, DECISION D-IN-3 |
| pad | `PADS_BANK0.GPIOn`: IE = 1, SCHMITT = 1, PUE = 0, PDE = 0, OD = 1, ISO = 0; `FUNCSEL` = SIO; read active-low | | E9-safe input configuration (F3) | Derived |

Time constants (Derived): release, C2 charges through R2: tau = 10 kΩ x 4.7 nF = 47 µs; time spent between 0.8 V and 2.0 V = tau x ln((3.3 - 0.8)/(3.3 - 2.0)) = 31 µs, during which the E9 leakage (if A2 silicon) helps the rise. Closure, C2 discharges through R1 plus a 100 Ω contact: tau = 1.1 kΩ x 4.7 nF = 5.2 µs. Both are below 5 % of the 1 ms sampling period, so the RC has no effect on debounce or timing; it exists for RF. Cut-off 1/(2 pi R1 C2) = 34 kHz.

RF immunity (Derived, Medium): at 144 MHz the shunt impedance of 4.7 nF is 0.235 Ω ideal; with 0.6 nH of 0603 lead inductance the magnitude is about 0.31 Ω, so the R1/C2 divider attenuates cable pickup by 20 log(1000/0.31) = 70 dB before C1 and the Schmitt hysteresis (0.2 V) are counted. Order-of-magnitude exposure: the far-field formula E = sqrt(30 x P x G)/d gives 155 V/m at 0.1 m from a 5 W, 1.6-gain antenna (Low confidence, near-field); tens of volts peak on a 1 m unshielded paddle cable is plausible, and 70 dB leaves tens of millivolts at the pad. Bench requirement CTL-KEY-05 (keyer report) stands: key the transmitter into the dummy load from memory while a 1 m cable hangs on the jack and confirm zero false state changes in a 5 minute logic capture (F10).

TBR items in this network, pending the owner's actual key and paddle (SI-034: TRS plugs, brands unknown): the contact-resistance allowance (500 Ω assumed; a measurement with the multimeter on each closed contact closes it), the make and break debounce times (F6, measured with the logic capture), and whether the 100 pF C1 is needed (decided by the RF-immunity bench case).

### F5. ESD and abuse clamp selection (Sourced table, Derived currents)

| Part | Type | VRWM | VBR | Clamp | Capacitance | Leakage | IEC 61000-4-2 | Package | Source |
|---|---|---|---|---|---|---|---|---|---|
| Nexperia PESD3V3L2BT | bidirectional, 2 lines | 3.3 V | 5.8 / 6.4 / 6.9 V at 5 mA | 8 V max at IPP 1 A; 26 V at 15 A 8/20 µs surge (the "VCL = 26 V" headline) | 101 pF typ at 0 V | 90 nA typ, 2000 nA max at 3.3 V | contact 30 kV, level 4 | SOT23 | data sheet 27 June 2023 |
| TI TPD2E001 | unidirectional, 2 lines | not tabulated | 11 V at 10 mA | VCC + 25 V positive, -60 V negative at +/-8 kV contact ("not production tested") | 1.5 pF typ | 1 nA max | +/-8 kV contact, +/-15 kV air | DRL SOT-5, DRY, DRS, DZD | SLLS684I, March 2016; TI recommends TPD2E2U06 as the pin-compatible lower-clamp part |
| TI TPD2E2U06 | unidirectional, 2 lines | 5.5 V | 6.5 to 8.5 V at 1 mA | IO to GND 9.7 V at 1 A TLP, 12.4 V at 5 A TLP; GND to IO 1.9 V at 1 A, 4 V at 5 A; RDYN 0.5 Ω | 1.5 typ, 1.9 max pF | 1 typ, 10 max nA | +/-8 kV contact, +/-15 kV air (level 4); 85 W 8/20 µs surge | DRL SOT-5X3, DCK | SLLSEG9C, December 2019 |

Choice (Proposal): TPD2E2U06DRLR at the jack. Reasons: unidirectional, so a negative excursion (an audio source or reversed device on the jack) is clamped at -0.7 to -1.9 V instead of the -6.4 V a bidirectional part allows, which matters because the pad absolute minimum is -0.5 V; IEC level 4 with a datasheet clamp figure that is production-characterised; one package protects both lines. The 101 pF of the PESD3V3L2BT would have been useful as an RF shunt, which C1 provides instead.

Currents (Derived): during an 8 kV contact discharge the jack node is held near the 12.4 V (5 A TLP) figure; through R1 the pad-side current is (12.4 - 3.3 - 0.7)/1 kΩ = 8.4 mA for about 100 ns, which raises C2 (4.7 nF) by 0.18 V: the pad never leaves its normal range. Continuous +12 V abuse (an external keyer with a positive keying line, owner bound TBR): TVS current (12 - 6.5)/1 kΩ = 5.5 mA, 36 mW in the TVS, 30 mW in R1 (0603 rated 100 mW). Without D2 the pad node would sit at the TVS voltage minus nothing (R1 carries only the pad's own clamp current), i.e. potentially above the +5.5 V absolute maximum with about 1 to 3 mA into the pad's internal structure; with D2 (BAT54S) the pad node is held at 3.3 V + 0.4 V and R1 passes (12 - 3.7)/1 kΩ = 8.3 mA into the 3V3 rail, which the rail's load absorbs. For -5 V abuse D2 passes (5 - 0.4)/1 kΩ = 4.6 mA from ground. Abuse bound proposed: -5 V to +12 V continuous (Proposal; keyer report D9 asked the owner to confirm). A +24 V bound would need R1 in 1206 (310 mW).

Stock and price signals (Low confidence, search snippets 2026-09-25 about 11:45 PDT): TPD2E001DRLR DigiKey USD 0.82 at quantity 1; PESD3V3L2BT,215 TME USD 0.41; 74LVC1G123DP,125 DigiKey USD 0.45; MAX6369KA+T DigiKey USD 5.01, 8,500 in stock; TPD2E2U06DRLR and BAT54S not checked (budget exhausted). ACTION A4 verifies all of them on the distributor sites before the BOM freeze.

**Addendum 2026-09-26 (integrator; INSP-012 F-03).** The continuous +12 V abuse currents above are corrected. The TVS current is set by the abuse source, not by (12 - 6.5)/1 kΩ: R1 lies between the jack node and the pad, not in series with the TVS. With the 50 mA current-limited bench source of the REQ-SYS-049 verification note the TVS conducts about 45 to 47 mA at its 6.5 to 9 V clamp, 0.3 to 0.4 W for the 10 min case; R1 dissipates about 69 mW at 8.3 mA with the TVS open and 8 to 28 mW with the TVS clamping, not 30 mW. Whether the TPD2E2U06 takes 0.3 to 0.4 W for 10 min is checked against its absolute maximum ratings at PDR (docs/icd/ICD-CTL-KEY.md section 3.2.7.1 and its section 6 TBR row); otherwise the bench limit is lowered or a series element is added.

### F6. Debounce filter numbers and golden vectors (Sourced inputs, Proposal values)

Sourced: Curtis: "The bounce is usually on the order of 5-10 milliseconds ... Dot length, at 50 wpm, is only 24 ms. The debouncing must not be so sluggish that it slows an operator"; the 8044 used 1 MΩ and 0.01 µF (10 ms) RC filters on the paddle lines and "a (pullup) resistor of from 5.6K to 100K" on the manual key pin. Ganssle (via keyer report F7): average bounce 1557 µs, maximum 6200 µs over 18 switches.

Proposal: sample both inputs at 1 kHz (TIMER0 ALARM1); a line is confirmed closed after N_make = 2 consecutive closed samples (2 ms) and confirmed open after N_break = 5 consecutive open samples (5 ms); the same filter serves hand key and paddles; each count is configurable 1 to 20 ms; defaults are TBR until the owner's key and paddle have been captured (F10) and the observed maximum bounce is known. Why asymmetric: a fast make keeps paddle latency at 1 to 3 ms; a slower break absorbs make-bounce (the contact opening briefly right after the first make) and break-bounce without lengthening the response to a press. Consequence for the hand key (Derived): every element is lengthened by N_break - N_make = 3 ms at the engine output, 4 % of a dit at 15 WPM, which the sequencer treats as part of the key's weight; the envelope shifts both edges equally (F11), so it adds nothing further.

Golden vectors from `keyer_ref.py` (sample index at which the state change is reported; sample k is taken at t = k ms):

| ID | Input pattern (ms, closed = C, open = O) | Expected confirmed events (sample, state) |
|---|---|---|
| D1 | C at 0, O at 100 | (1, closed), (104, open) |
| D2 | C at 0, O at 1, C at 2 (1 ms make bounce) | (3, closed), (104, open) |
| D3 | O at 100, C 102 to 104, O from 105 (3 ms re-close) | (1, closed), (109, open); no second element |
| D4 | O at 100, C 101 to 107, O from 107 (6 ms re-close after a 1 ms open) | (1, closed), (111, open); the re-close merges into the element because the 1 ms open was never confirmed |
| D5 | 1 ms closed glitch at 50 while open | no event |

A break bounce that opens for 5 ms or more and then re-closes will register as two elements with any 5 ms filter; that is the residual behaviour the bench measurement must show does not occur with the owner's hardware.

### F7. Reference keyer semantics and the iambic golden vectors (Sourced definitions, Proposal for the tunables)

Sourced definitions. ITU-R M.1677-1 section 2 (via keyer report F4): dash = 3 dots; space within a letter = 1 dot; between letters = 3 dots; between words = 7 dots. PARIS: dit = 1200/WPM ms (QMX manual via keyer report F4). Curtis 8044 note: "Most recent keyer designs produce a dit or dah of the correct length, regardless of when the paddle is released ... the space between elements must never be allowed to shorten by early key closure"; "Dot memory allows a keyer to remember that you hit the dot key even though you hit the key early and did not wait for the dot to commence. Send a fast N on any keyer to test this feature"; "send an A as fast as you can move the paddles. You will always get the dit followed by the dah" (dash memory); type A: "when a squeeze is released, the element underway is completed and nothing else follows"; type B: "a squeeze released during an element (dot or dash) will cause another alternate element to follow the one being produced. For example, if you squeeze to produce a period, then you must release during the third dit (or the space following). The last dah will automatically transmit. ... to make a C, you must release during the second dah (or the space following) and the last dit will automatically transmit."

Reference semantics encoded in `keyer_ref.py` (Proposal where not quoted above):

1. Idle: dit closed starts a dit; else dah closed starts a dah; both in the same sample: dit first.
2. Elements self-complete; the 1-dit space after an element never shortens.
3. Opposite-paddle memory (both modes): a rising edge of the opposite paddle at any sample during the element or its space latches the alternate element (dot and dash memory).
4. Mode B squeeze latch: if both paddles are closed at any sample from S x L after the element start to the end of the space, where L is the current element length and S the switchpoint (0 to 0.9), the alternate element is latched. S = 0 is pure Curtis type B. Mode A has no squeeze latch.
5. Same-paddle rising edge during the space latches a repeat (fast "I"); during the element it is ignored (lockout).
6. Decision at the end of the space: alternate (latched or held) beats repeat (held or latched); otherwise idle.

Golden vectors at 20 WPM (dit 60 ms, dah 180 ms, space 60 ms), 1 ms ticks, paddle inputs already debounced, output as key-down intervals in ms. Both modes share the same output except where two rows are shown.

| ID | Paddle pattern (ms) | Mode | Output intervals (ms) | Reads | Checks |
|---|---|---|---|---|---|
| V1 | dit 0 to 10 | A, B | (0, 60) | . | self-completing dit |
| V2 | dah 0 to 10 | A, B | (0, 180) | - | self-completing dah, 3:1 |
| V3 | dit 0 to 250 | A, B | (0,60) (120,180) (240,300) | ... | 1-dit spaces; third dit because still held at 240 |
| V4 | dah 0 to 50, dit 30 to 40 | A, B | (0,180) (240,300) | -. | dot memory ("fast N") |
| V5 | dit 0 to 20, dah 15 to 30 | A, B | (0,60) (120,300) | .- | dash memory ("fast A") |
| V6 | dit 0 to 390, dah 5 to 390 (release during 3rd element, a dit) | A | (0,60) (120,300) (360,420) | .-. | Curtis A: nothing follows |
| V6 | same | B (S = 0) | ... plus (480,660) | .-.- | Curtis B: alternate follows |
| V7 | dit 0 to 430, dah 5 to 430 (release in the space after the 3rd element) | A / B | as V6 A / as V6 B | .-. / .-.- | "or the space following" |
| V8 | dah 0 to 450, dit 5 to 450 (release during 2nd dah) | A / B | (0,180) (240,300) (360,540) / plus (600,660) | K / C | Curtis C example |
| V9 | dah 0 to 380, dit 5 to 380 (release 11 % into the 2nd dah) | B, S = 0.5 | (0,180) (240,300) (360,540) | K | switchpoint not reached: no latch |
| V9b | same | B, S = 0 | plus (600,660) | C | pure B latches |
| V10 | both 0 to 1000 (release during the 6th element) | A / B | .-.-.- ending (840,1020) / plus (1080,1140) | period / period plus dit | alternation and release rule |
| V11 | dit 0 to 10, dit 70 to 80 | A, B | (0,60) (120,180) | .. | same-paddle tap in the space accepted |
| V12 | dit 0 to 10, dit 30 to 40 | A, B | (0,60) | . | same-paddle tap during the element ignored |
| V13 | dit 0 to 750, dah 5 to 750 (release during the 5th element) | B (S = 0) | .-.-.- ending (840,1020) | period | Curtis period example |

The switchpoint default is a Proposal of 50 % of the element (WinKeyer's default "50" is defined against the dit time and starts the lookout for new presses; the two definitions differ, so cwht's is stated as its own tunable) and is TBR by the owner's human-in-the-loop session (risk register RSK-012 mitigation S3); the golden vectors are produced for S = 0 and S = 0.5 so that either default is already covered. Weight and ratio vectors: the same set is re-run with ratio 2.5, 3.0, 4.0 and weight 25, 50, 75 %, asserting dah = ratio x dit and that weight moves time from spaces to elements without changing the element-plus-space period (WinKeyer definition, keyer report F5).

### F8. Timing tolerance and the simulated-clock HostUnit harness (Derived, Proposal)

Quantisation (Derived): 1 ms is 0.4 % of a dit at 5 WPM and 4.2 % at 50 WPM; 0.1 ms is 0.04 % and 0.42 %. The RP2350 TIMER0 has 1 µs resolution from the 12 MHz crystal (rustos report F10), so element generation can be exact to a few µs; the only millisecond-scale uncertainty is when a paddle event is *observed* (1 kHz sampling plus N_make), and that shifts element start times, not element lengths.

Proposal: each element and each space, measured at the engine output (the key stream before the sequencer and shaper), shall be within +/-1 % of nominal or +/-0.5 ms, whichever is larger, at every speed from 5 to 50 WPM (2.4 ms at 5 WPM, 0.5 ms above 24 WPM). Paddle-to-element latency shall not exceed 3 ms (1 ms sample plus 2 ms make filter). This replaces "+/-1 ms or +/-2 % of a dit" and "1 percent".

Harness (Proposal, consistent with SI-026 and the rustos report's `time::Clock`/`Alarm` traits): `cwht-core` exposes `Keyer::on_sample(dit, dah)` (called at the 1 kHz tick) and `Keyer::on_alarm()` (called when the element alarm fires), both against the injected `Clock`. The host test advances a simulated microsecond clock in 100 µs steps (10 kHz), delivers the 1 kHz sample tick and the alarm at their scheduled instants, and records key-stream edges with 0.1 ms resolution. The golden vectors of F7 are stored as data (JSON) and the test asserts every interval to within the tolerance above; `keyer_ref.py` run at 0.1 ms ticks gives, for a held dit, intervals (0, 2400) (4800, 7200) (9600, 12000) ticks at 5 WPM and (0, 240) (480, 720) (960, 1200) at 50 WPM, i.e. exact. The debounce vectors D1 to D5 run on the sampler stage alone. This is the primary Class A timing evidence (MC/DC measured here, SWE-219).

### F9. Emulation restricted to event ordering (Sourced charter, Proposal scenarios)

Charter section 9 (post SI-026): "Emulation (optional, secondary: whole-binary scenarios on an RP2350 emulator for event ordering only, never timing)". Scenarios worth running if an emulator is available: (1) boot with a key input held low reaches the interlock state and never asserts PA enable; (2) ALARM0 (element) and ALARM1 (sampler) interrupts nest and re-enter without losing a sample; (3) TX_KEY is never asserted before the T/R line and never after the hardware cutoff timer would have expired in a stuck-key scenario (checked as ordering of events, not durations); (4) a watchdog reset returns all pads to the reset state (F2) with PA enable low. No timing credit is taken from emulation (C10).

### F10. Bench method without an oscilloscope (Sourced tools, Derived capability)

1. Logic capture with a second Pico 2 (Sourced: sigrok-pico README): "implements a sigrok driver for the Raspberry Pi PICO RP2040 using the PICO SDK CDC serial library", "21 digital channels (D2-D22) and 3 analog channels (A0-A2)", works with "sigrok-cli (command-line)", firmware list includes "pico2_*.uf2" Pico 2 variants, GPL-3.0. Sample rates were not in the README text (Low confidence; the digital rate is far above the 1 kHz to 10 kHz needed). Channels to capture: tip and ring contact lines at the jack (through 10 kΩ series resistors so the capture cannot disturb the input network), the debounced key stream if exported on a test pad, TX_KEY, the hardware cutoff output Q, the T/R drive, the sidetone PWM, and the detected RF envelope on A0. sigrok-cli is headless (charter section 11); its installation by the owner is a decision (D-VER-2).
2. RF envelope (Derived from F2): the diode RF probe already planned in the V&V plan section 6.2 (1N5711 on the dummy load) drives a Pico 2 ADC input at 500 kS/s (2 µs per sample, 12 bit). Rise and fall 10-to-90 % of a 5 ms ramp is then measured to about 0.01 ms, and the FFT of the captured envelope, multiplied onto an ideal carrier, gives the keying-sideband spectrum by Analysis with the PA's real envelope distortion included. This closes the -60 dBc at 500 Hz requirement (F12) as Analysis with measured input, which the charter allows when the method is Analysis.
3. tinySA Ultra (Sourced wiki): resolution filters "0.2, 1, 3, 10, 30, 100, 300, 600 and 850 kHz"; "Phase noise at 30MHz of -108dB/Hz at 100kHz offset and -115dB/Hz at 1MHz offset"; "Spur free dynamic range when using a 30kHz resolution bandwidth of 70dB"; level accuracy +/-2 dB. The phase noise at 500 Hz offset is not published and will be far worse than at 100 kHz, so a -60 dBc sideband at 500 Hz is below the instrument's own skirt (Derived, Medium). Use the tinySA for the click floor at offsets of 10 kHz and beyond (a square-keyed 12.5 Hz dot stream reaches -60 dBc only at 12.5 kHz per IVARC) and for spurs; do not assign it the close-in sideband requirement.
4. Timing on the bench: with the logic capture, the element and space lengths of a 30 s memory-keyed PARIS string at 5, 15, 25 and 50 WPM are compared with F8's tolerance; the same capture times the hand-key chain of F11 (contact edge to TX_KEY edge to envelope 50 %), the overhang and the hang time. This is the "run for the record" Test on the delivered unit.

### F11. Hand-key semantics through the sequencer and shaper (Derived and Proposal)

Signals: KEY_REQ (debounced contact for the hand key, or the engine output for paddles); TX_KEY (sequencer output that enables the PA path and gates the envelope; watched by the hardware cutoff); TR (relay or switch drive); ENV (DAC or PWM raised-cosine envelope). Envelope: 5 ms 10-to-90 % raised cosine, whose full 0-to-100 % ramp is 5/0.59 = 8.5 ms (Derived: the 10 % and 90 % points of (1 - cos(pi t/T))/2 lie at 0.205 T and 0.795 T).

Timeline for one hand-key element in semi break-in, starting from receive (relay operate and release 3 ms max from Omron G6K-2F-RF via reference report F28; margins are Proposals):

| Step | Time | Rule |
|---|---|---|
| Contact closes | 0 | |
| Closure confirmed | +1 to +3 ms | 1 kHz sample plus N_make = 2 |
| RX audio muted; TR asserted; PA bias enabled; TX_KEY asserted; sidetone starts | +3 ms | sidetone is aligned with TX_KEY so the operator's feel does not depend on the lead-in |
| Envelope rise begins | +3 ms + T_lead, T_lead = 5 ms | T_lead >= relay operate 3 ms max + 2 ms margin; the lead applies only to the first element after a changeover |
| RF at 50 % | +12.25 ms | half of the 8.5 ms ramp |
| RF at 100 % | +16.5 ms | |
| Contact opens | t1 | |
| Opening confirmed | t1 + 5 to 6 ms | N_break = 5 |
| Envelope fall begins | first element: t1 + 5 ms + T_lead; later elements: t1 + 5 ms | first-element extension = T_lead (WinKeyer "1st extension" concept), so every radiated element equals its key-down time plus 3 ms |
| RF reaches zero | fall begin + 8.5 ms | |
| TX_KEY and PA bias released (key-up overhang) | fall begin + 8.5 ms + 1 ms margin = 9.5 ms after fall begin | the overhang is the full fall time, not the 10-to-90 % figure; QRP Labs AN005: the Key OUT line "overhangs key-up by the fall time" |
| Hang timer starts | at RF zero | T_hang = 8 dits of the displayed WPM (default 15 WPM: 640 ms; 5 WPM: 1920 ms; 50 WPM: 192 ms); alternatives 6.1 dits ("Contest") or a fixed 50 to 2500 ms |
| TR released; RX unmuted 3 ms later | hang expiry | relay release 3 ms max |

Rules that fall out of the timeline (Proposal unless marked):

- Key-up overhang = full fall duration (8.5 ms for the 5 ms 10-to-90 % ramp) plus 1 ms; the T/R switch never opens under RF (reference report REQ 3, AN005 rule). With the 3 to 8 ms configurable ramp the overhang is 6.1 to 14.6 ms (Derived).
- Minimum radiated element: the shaper never reverses mid-ramp; a confirmed closure shorter than the ramp still produces a full rise then a full fall, i.e. a minimum element of 8.5 ms at the 50 % points. A mid-ramp reversal would put a slope discontinuity into the envelope and widen the spectrum (IVARC, W8JI via keyer report F10). Confirmed closures cannot be shorter than 2 ms because of N_make.
- The paddle keyer uses the identical sequencer and shaper: the engine's key stream replaces the contact, the first-element extension still applies after each changeover, and the engine's shortest element (24 ms at 50 WPM) is 2.8 times the full ramp, so the AN005 rule "the rise/fall speed must never be more than the symbol rate" is met with margin (Derived). At 50 WPM the rise plus fall occupy 10/24 = 42 % of a dit at the 10-to-90 % points (keyer report F10 arithmetic, Derived).
- Semi break-in with a hand key: the hang reference is the displayed WPM even though no element engine runs, so the speed control doubles as the hang control in Straight mode; the LCD shows the hang in ms while adjusting (Proposal). Full QSK with a hand key over a relay would operate the relay once per element (about 18,000 operations per hour at 20 WPM; relay life not verified, Low) and leave about 60 ms of listening in an 80 ms space at 15 WPM; it is offered only if the T/R trade (SI-035) selects a solid-state switch, in which case T_lead drops to the switch's settling time and the hang default becomes 1 dit.
- Straight-mode inputs: tip only by default; "both" (cootie) and "ring" as menu options (keyer report F2). In Straight mode the ring contact is ignored unless selected, which is what makes the mono-plug case safe once the interlock has passed (F13).

### F12. Envelope shape and keying-sideband target (Sourced, Derived)

Sourced (via the earlier reports, primary citations there): ARRL practice 5 ms rise and fall measured 10-to-90 % for a 30 WPM fading circuit, 10 ms for non-fading; IVARC/G3OTK: a raised cosine with the same maximum slope as a 5 ms linear ramp (total ramp pi x 5/2 = 7.85 ms, 10-to-90 % 4.6 ms, Derived) reaches -60 dBc just under 300 Hz; a 4-pole Gaussian-to-6 dB filter at 70 Hz reaches -60 dBc above 230 Hz; QRP Labs AN005: raised cosine adjustable 2 to 113 ms, "Practically, 5 to 10 ms is most commonly used"; Icom IC-705: 2, 4, 6 or 8 ms, default 4 ms. Regulatory basis (Sourced, eCFR API 2026-09-23): 47 CFR 97.307(a) "No amateur station transmission shall occupy more bandwidth than necessary for the information rate and emission type being transmitted, in accordance with good amateur practice"; (b) "Emissions outside the necessary bandwidth must not cause splatter or keyclick interference to operations on adjacent frequencies." No numeric keying-sideband limit exists in Part 97; the number below is a design target chosen to satisfy (a) and (b) with margin.

Reconciled (Proposal): default 5 ms 10-to-90 % raised cosine (total 8.5 ms), configurable 3 to 8 ms in 1 ms steps, the same at all speeds (a speed-adaptive shaper adds a code path to a safety-critical component for a benefit that IVARC quantifies as usable only below 20 WPM). Target: keying sidebands of a 30 WPM dit stream at least 60 dB below the carrier at offsets of 500 Hz and beyond (requirement, verified by Analysis on the captured envelope of F10 and by tinySA beyond 10 kHz), with 300 Hz as the shaper design goal checked by Analysis of the DAC sequence alone. 60 WPM (20 ms on, 20 ms off) is the ARRL measurement condition and is added to the analysis set.

### F13. Stuck-key and mono-plug hazard controls (Sourced parts, Derived numbers, Proposal architecture)

The hazard: unintended continuous transmission from a mono plug grounding the ring, a key or paddle stuck closed, headphones plugged into the key jack (a 32 Ω load reads as a closed contact), or firmware holding TX_KEY. Documented occurrences: Elecraft KX3 note and QRP Labs QCX/QMX manuals (keyer report F1). Controls, in layers:

1. **Power-on and reset interlock (firmware, SWE-134 a and h).** TX arming requires both inputs confirmed open for at least 500 ms after boot or after any reset (Proposal). Otherwise the LCD shows "KEY CLOSED: check plug", TX is inhibited, sidetone is off, and the check repeats every sample. If the ring stays closed while the tip toggles (mono plug with a hand key), the radio does not change mode by itself; the user selects Straight-on-tip from the menu, an explicit second action (SWE-134 d), after which the ring is ignored (F11). This replaces PicoKeyer-style automatic detection (keyer report D2) for rev A; automatic detection can be added later if it "cannot produce false positives" (RSK-012 S1 wording).
2. **Straight-key timeout (firmware, SWE-134 j).** A confirmed continuous closure longer than T_sw = 5 s (configurable 2 to 6 s) drops TX_KEY through the normal fall, keeps the sidetone on so the operator hears the fault (WinKeyer paddle-watchdog pattern), shows "KEY?" and re-arms when the contact is confirmed open. T_sw must stay below the hardware cutoff's minimum (7.5 s, item 4) so that the firmware acts first in the nominal case. Longest legitimate closure for comparison (Derived): a 5 WPM dah is 720 ms, 1080 ms with ratio 4:1 and 75 % weight; a tune-up carrier of 3 to 5 s fits under T_sw.
3. **Paddle watchdog (firmware).** Stop keying after 128 consecutive identical elements (WinKeyer figure, keyer report F5) or 30 s of continuous identical elements, whichever comes first; sidetone continues (Proposal). 128 dits last 3.1 s at 50 WPM, 7.7 s at 20 WPM and 30.7 s at 5 WPM; 128 dahs last 9.2, 23.0 and 92.2 s, hence the 30 s cap (Derived). The hardware cutoff does not catch a stuck paddle because every element produces a TX_KEY edge.
4. **Hardware PA-enable cutoff (independent of firmware, SWE-134 i: no single software event may initiate the hazard).** Topology (Proposal): a retriggerable monostable watches TX_KEY; each key-down edge starts a pulse of length T_max; the PA path is enabled only while TX_KEY AND Q are both true. A TX_KEY that stays high longer than T_max, from any cause, loses Q and the PA is off until the line falls and rises again. Cutoff node: the envelope modulator's control input (the QRP Labs style series pass element on the PA drain, reference report F31), pulled to zero when Q is low, rather than the LDMOS gate bias alone, because a driven LDMOS can conduct on drive peaks with the bias removed (Proposal; confirm against the PA topology chosen at PDR). Part candidates:

| Candidate | Behaviour | Timing set by | T_max = 10 s design | Accuracy | Supply, package | Verdict |
|---|---|---|---|---|---|---|
| Nexperia 74LVC1G123 (Rev. 8, 14 Aug 2023) | "Single retriggerable monostable multivibrator; Schmitt trigger inputs"; "Retriggerable for very long pulses up to 100 % duty factor"; trigger on B rising with A low and CLR high (standard '123 table; confirm at schematic review) | "If CEXT > 10 nF ... tW = K x REXT x CEXT ... K = constant = 1"; measured 1.0 ms typ, 1.05 ms max at 10 kΩ, 0.1 µF | REXT 1 MΩ 1 %, CEXT 10 µF X7R 16 V 1206: tW = 10 s typ; 7.5 to 11 s with -25 % to +10 % capacitance including DC-bias derating (Derived) | K spread vs VCC in Fig. 14 not extracted (Low); +/-25 % dominated by the capacitor | 1.65 to 5.5 V; SOT505-2 (DP), SOT765-1 (DC), SOT833-1, SOT1116, SOT1203 | **Recommended**: cheapest (USD 0.45 snippet), level output, self-resetting |
| ADI LTC6993-2 (69931234fb) | "monostable multivibrator ... programmable pulse width of 1µs to 33.6 seconds"; -2 = rising edge, retrigger "Yes" | tOUT = NDIV x RSET/50 kΩ x 1 µs, NDIV 1 to 2^21, RSET 50 k to 800 kΩ | NDIV = 2^21, RSET = 238 kΩ gives 10.0 s (range 2.1 to 33.6 s at that NDIV) (Derived) | "<2.3% for Pulse Width > 512µs" | 2.25 to 5.5 V; idle 135 to 200 µA at 5.5 V; TSOT-23-6 or 2 x 3 mm DFN | Alternative when the +/-25 % of the RC is judged too loose; price and stock not checked |
| Maxim MAX6369 (19-1676 Rev 6 3/15) | pin-selectable watchdog: "If WDI remains either high or low for the duration of the watchdog timeout period (tWD), WDO triggers a pulse"; WDO open-drain pulse 100 ms (MAX6369); "The internal watchdog timer clears ... whenever WDI sees a rising or falling edge"; timeout 10 to 30 s at SET2 = SET1 = VCC, SET0 = 0 | SET pins | 10 to 30 s window | 3:1 window | 2.5 to 5.5 V, 8 µA; SOT23-8 | **Rejected**: WDO is a 100 ms pulse, not a level, and it fires during idle receive because WDI sees no edges; it would need a firmware heartbeat, which defeats independence; USD 5.01 |
| Discrete RC plus 74LVC1G14 Schmitt inverter plus diode reset | TX_KEY charges C through R; low discharges it through the diode; inverter output is the enable | R 1 MΩ, C 10 µF | 6.6 to 9.3 s for VT+ 1.6 to 2.0 V of 3.3 V (Derived) | about +/-30 % | 3 parts | Fallback if the '123 is unavailable |

T_max (Proposal): 10 s nominal, acceptance window 7.5 to 13 s, chosen so that firmware timeouts (5 s, item 2) always act first, a tune-up carrier of a few seconds is never interrupted, and a fault can transmit for at most 13 s (PA thermal budget: 5 W output, about 4 to 7 W dissipated per RSK thermal entry, well inside a 13 s transient). The keyer report's 10 to 60 s range is narrowed to 10 s.

5. **CPU watchdog and pad reset states (Sourced, Derived).** The rustos report's "watchdog of at most 2 s ... before the transmitter can be keyed" stands; the RP2350 counter allows up to about 16 s (F2). On a watchdog reset every pad returns to ISO = 1, IE = 0, PDE = 1, FUNCSEL = NULL (F2), so TX_KEY and the PA-enable line are undriven with a 36 to 113 kΩ internal pull-down and no E9 leakage (E9 requires IE = 1). To make the safe state independent of the internal pull-down and of any future firmware pad configuration, TX_KEY and PA_EN carry external 4.7 kΩ pull-downs, inside the erratum's "8.2 kΩ or less" guidance (Proposal). The firmware is initialised to the safe state and re-runs the interlock (SWE-134 a).

Coverage (Derived): firmware hung -> CPU watchdog (2 s) -> reset -> pads low -> PA off; firmware alive but TX_KEY stuck (logic fault, or timeouts misconfigured) -> hardware cutoff at 10 s; hand key stuck -> firmware at 5 s, hardware at 10 s; paddle stuck -> paddle watchdog within 30 s (hardware does not catch it); mono plug or headphones in the key jack at boot -> interlock; the same after boot -> reads as a continuous closure -> firmware 5 s then hardware 10 s.

**Addendum 2026-09-26 (integrator; ICD-CTL-KEY review INSP-012 F-03 and hazards OQ-SAF-007).** Two corrections to this finding. (1) Headphones or a shorted TRS cable inserted after boot read as a closure on both key inputs: in Straight mode a continuous key-down (item 2 limits apply), and in the iambic modes a squeeze, which the keyer answers with an alternating element stream that retriggers the monostable of item 4 at every element, so the 13 s bound of item 4 holds for a continuous key-down only; the stream is stopped by the proposed no-gap and squeeze watchdog of HZ-004 K4 and, if adopted, by the transmission-length backstop REQ-SYS-180 (docs/conops/conops.md OPS-013 step 6). (2) The tune carrier bound is now REQ-SYS-020, at most 5.5 s after it starts, 2 s below the 7.5 s floor of the cutoff; the few-seconds tune assumption of item 4 stands.

### F14. Reconciled number set

| Item | Value | Flag | Source or derivation |
|---|---|---|---|
| Speed range | 5 to 50 WPM, 1 WPM steps | Sourced | SI-033 |
| Speed default | 15 WPM | Proposal | between QCX/YACK 12 and K3NG 26 (keyer report F6); owner may change |
| Dit length | 1200/WPM ms | Sourced | PARIS convention (QMX manual, keyer report F4) |
| Ratios | dah 3 dits; intra-character 1 dit; inter-character 3; inter-word 7 | Sourced | ITU-R M.1677-1 section 2 |
| Element and space tolerance | +/-1 % or +/-0.5 ms, whichever larger, at the engine output | Proposal | F8 |
| Paddle-to-element latency | <= 3 ms | Derived | 1 kHz sample + 2 ms make |
| Sampling | 1 kHz, TIMER0 ALARM1; element timer ALARM0 at 1 µs | Sourced/Proposal | rustos report peripheral map; F8 |
| HostUnit clock | simulated µs clock stepped at 100 µs (10 kHz) | Proposal | F8 |
| Debounce | make 2 ms (2 samples), break 5 ms (5 samples), each 1 to 20 ms configurable | Proposal, TBR | F6; Curtis 5 to 10 ms, Ganssle max 6.2 ms |
| Iambic modes | A, B, Ultimatic, Bug, Straight (tip, ring, both) | Sourced | keyer report F2, F3 |
| Default mode | A | Proposal | Elecraft and QRP Labs default; "more forgiving for first-time operators" (KX2 manual via keyer report F3); owner decision D1 |
| Switchpoint | 0 to 90 % of the element, default 50 % | Proposal, TBR by HITL | F7 |
| Dah:dit ratio | 2.5:1 to 4.0:1 in 0.1 steps, default 3.0 | Sourced default, Proposal range | ITU; range inside IC-705 2.8 to 4.5 and WK3 2 to 4 |
| Weight | 25 to 75 %, default 50 % | Proposal | WK3 10 to 90, QCX 5 to 95; narrowed against the Curtis "forgotten weight" failure |
| Key compensation | 0 to 25 ms, default 0 | Sourced range basis | WK3 0 to 250 ms; keyer report SW-KEY-05 |
| First-element extension | = T_lead (5 ms) after a T/R changeover, fixed | Derived | F11 |
| Envelope | raised cosine, 5 ms 10-to-90 % (8.5 ms total), 3 to 8 ms configurable, not speed-adaptive | Sourced default, Proposal range | ARRL 5 ms; IC-705 2 to 8; QRP Labs 5 to 10 common |
| Keying sidebands | <= -60 dBc at abs(offset) >= 500 Hz, 30 WPM dit stream (requirement); 300 Hz shaper design goal | Proposal | F12; IVARC 300 Hz for the ideal shape |
| Minimum radiated element | 8.5 ms at 50 % points (no mid-ramp reversal) | Derived/Proposal | F11 |
| T_lead (PTT lead-in, first element) | 5 ms | Derived | relay 3 ms max + 2 ms |
| Key-up overhang | full fall (8.5 ms) + 1 ms | Derived/Proposal | F11, AN005 |
| Break-in default | semi | Proposal | reference report F28; SI-035 open |
| Hang | 8 dits (default), 6.1 dits (contest), 50 to 2500 ms custom; hand key uses displayed WPM | Sourced values, Proposal range | QCX Auto 8 / Contest 6.1; WK3 1 wordspace + 1 dit |
| Sidetone | 300 to 1000 Hz, 10 Hz steps, default 600 Hz, locked to RX CW offset; level 0 to 99 relative or absolute | Proposal | IC-705 300 to 900, K3NG 600, KX2 600, QCX 700 |
| Sidetone onset | aligned with TX_KEY (within 1 ms) | Proposal | F11 |
| Pull-up | 10 kΩ external; PUE = 0, PDE = 0 | Derived | F3 |
| Series resistor | 1.0 kΩ | Proposal within Sourced range | Curtis 470 Ω to 1 kΩ; F5 |
| Pad-node capacitor | 4.7 nF; tau 47 µs release, 5 µs closure | Proposal/Derived | F4 |
| Jack capacitor | 100 pF C0G (optional) | Proposal | F4 |
| ESD clamp | TPD2E2U06DRLR at the jack; BAT54S at the pad node | Proposal | F5 |
| ESD level | IEC 61000-4-2 level 4: 8 kV contact, 15 kV air | Sourced | TPD2E2U06 SLLSEG9C |
| Abuse bound | -5 V to +12 V continuous | Proposal, TBR owner | F5 |
| Closed-contact current | 0.30 mA per line (R_c 100 Ω) | Derived | F3 |
| Contact resistance allowance | closed <= 500 Ω, open >= 100 kΩ | Sourced (keyer report), TBR measurement | F3 |
| Interlock | both inputs open >= 500 ms before TX arm | Proposal | F13 |
| Straight-key timeout T_sw | 5 s (2 to 6 s) | Proposal | F13 |
| Paddle watchdog | 128 identical elements or 30 s | Sourced 128 (WK3), Proposal cap | F13 |
| Hardware cutoff T_max | 10 s nominal, 7.5 to 13 s window; 74LVC1G123, 1 MΩ, 10 µF | Proposal/Derived | F13 |
| CPU watchdog | 2 s | Sourced (rustos report) | RP2350 max about 16 s |
| PA-enable pull-downs | 4.7 kΩ external on TX_KEY and PA_EN | Proposal | E9 "8.2 kΩ or less" |
| Automatic CW ID speed | <= 20 WPM | Sourced | 47 CFR 97.119(b)(1), eCFR 2026-09-23 |

## 4. Implications for cwht

Verification classes in brackets follow charter section 9.

**REQ-candidate**

1. **SW-KEY-02 (revised).** Elements and spaces at the engine output within +/-1 % of nominal or +/-0.5 ms, whichever is larger, 5 to 50 WPM; paddle-to-element latency <= 3 ms. [HostUnit with the F7 vectors at 0.1 ms; Bench logic capture of a PARIS string at 5, 15, 25, 50 WPM]
2. **SW-KEY-04 (revised).** Mode A and mode B semantics as F7 items 1 to 6; switchpoint 0 to 90 % of the element, default 50 % (TBR by HITL). [HostUnit vectors V1 to V13 for S = 0 and S = 0.5]
3. **SW-KEY-06 (revised).** Sampler at 1 kHz; close confirmed after 2 consecutive closed samples, open after 5 consecutive open samples, both configurable 1 to 20 ms; the filter never exceeds 25 % of a dit at 50 WPM. [HostUnit vectors D1 to D5; Bench capture of the owner's key and paddle]
4. **SW-KEY-08 (revised).** Semi break-in default: T_lead 5 ms on the first element after changeover, first-element extension equal to T_lead, key-up overhang equal to the full fall plus 1 ms, hang 8 dits (6.1 dits or 50 to 2500 ms selectable) referenced to the displayed WPM in every mode. Full QSK only if the T/R trade selects a solid-state switch. [HostUnit sequencer model; Bench logic capture with the RF envelope on the ADC]
5. **SW-KEY-09 (revised).** Envelope raised cosine 5 ms 10-to-90 % (3 to 8 ms configurable), no mid-ramp reversal, minimum radiated element one full ramp; keying sidebands <= -60 dBc beyond 500 Hz at 30 WPM. [Analysis on the DAC sequence and on the captured envelope; tinySA beyond 10 kHz]
6. **SW-KEY-10 (revised).** (a) interlock: both inputs open >= 500 ms before TX arm, "KEY CLOSED" indication otherwise; mode changes only by menu; (b) straight-key timeout 5 s with sidetone continuing; (c) paddle watchdog 128 identical elements or 30 s; (d) automatic CW ID <= 20 WPM. [HostUnit; Bench]
7. **SW-KEY-12 (revised).** Element timing from TIMER0 ALARM0 and sampling from ALARM1, both in interrupt context independent of the UI loop; no PIO. [Inspection of the driver against the datasheet; Bench capture under UI load]
8. **CTL-KEY-03 (revised).** Per line: 10 kΩ pull-up to 3V3, 1.0 kΩ series, 4.7 nF at the pad, pad configured IE = 1, SCHMITT = 1, PUE = 0, PDE = 0; closed at <= 500 Ω contact resistance with the pad below 0.6 V including 120 µA E9 leakage; closed-contact current <= 0.35 mA. [Analysis F3; Inspection of schematic and pad configuration; Bench multimeter on the pad node]
9. **CTL-KEY-04 (revised).** TPD2E2U06 at the jack (IEC 61000-4-2 level 4) and BAT54S at the pad node; survives -5 V to +12 V continuous on either contact. [Analysis F5; Inspection]
10. **CTL-KEY-07 (revised).** Hardware cutoff: retriggerable monostable on TX_KEY with T_max 10 s (7.5 to 13 s), PA path enabled only while TX_KEY AND Q; cutoff acts on the envelope modulator control. [Analysis; Bench: hold TX_KEY high with the PA disconnected and time Q with the logic capture]
11. **CTL-TX (new).** TX_KEY and PA_EN carry external 4.7 kΩ pull-downs so that reset, bootloader and isolated pad states read low at the PA logic. [Inspection; Bench at first power-on stage 6 of the V&V plan]
12. **SW (from rustos report, kept).** CPU watchdog 2 s enabled before TX can be armed; reset reason recorded; the interlock runs after every reset. [HostUnit; Bench]

**RISK-candidate**

- R-KN1: the 74LVC1G123 pulse width depends on a 10 µF ceramic whose DC-bias derating is part-specific; T_max could fall below T_sw and the hardware cutoff would then interrupt legitimate 5 s tune carriers. Control: choose the capacitor from its vendor's DC-bias curve at 3.3 V, verify tW on the bench, keep T_sw <= 5 s.
- R-KN2: sigrok-pico Pico 2 firmware and sigrok-cli on macOS are unverified for this project (rates not extracted). Control: a fallback capture firmware built on the rustos TIMER and UART drivers is scoped in WP-11 if sigrok-pico fails to install headlessly.
- R-KN3: the owner's friends' keys (SI-019) may use mono plugs; the interlock and the Straight-on-tip menu handle it but the ConOps must tell them so. Control: a one-line "plug check" in the user notes.
- R-KN4: the switchpoint default and the asymmetric debounce are feel-dependent; a wrong default makes SI-018 "unpleasant" (RSK-012). Control: HITL session S3 with both defaults exposed in the menu.
- R-KN5: the cutoff node depends on the PA topology chosen at PDR; if the PA has no modulator (gate-bias keying only), a bias-only cutoff may not silence a driven LDMOS. Control: PDR trade study includes "hardware cutoff node" as a criterion.
- R-KN6: the tinySA Ultra cannot verify the close-in sideband number; the closure is Analysis on measured data, which a reviewer may challenge as not "Test". Control: state the method as Analysis in the requirement; add an OnAir listening check by the second station.

**DECISION-needed** (for the owner; recommendations in section "decisions_for_owner" of the structured return)

- D-KN1 default iambic mode A or B.
- D-KN2 hardware cutoff: adopt, T_max 10 s, 74LVC1G123 versus LTC6993-2.
- D-KN3 firmware straight-key timeout 5 s and paddle watchdog 128 elements or 30 s.
- D-KN4 semi break-in default with 8-dit hang; QSK tied to the T/R trade (SI-035).
- D-KN5 sidetone default 600 Hz locked to the RX offset.
- D-KN6 envelope 5 ms fixed (not speed-adaptive), 3 to 8 ms range.
- D-KN7 abuse bound -5 V to +12 V and the BAT54S secondary clamp.
- D-KN8 mono plug: interlock plus menu (no automatic mode change) for rev A.
- D-KN9 bench: second Pico 2 with sigrok-pico and `brew install sigrok-cli` by the owner.
- D-KN10 speed default 15 WPM.

**ACTION**

- A-KN1: encode the F7 and F6 vectors as `docs/test_cases/sw-keyer/keyer-golden-vectors.json` (schema: id, wpm, mode, switchpoint, inputs, expected intervals, tolerance) and generate them from a checked-in copy of `keyer_ref.py` under `tools/`, so the reference model and the Rust implementation are compared, not both written by hand.
- A-KN2: write `docs/icd/ICD-CTL-KEY.md` from F4 and F5 (pin map, values, pad configuration bits, TVS orientation, test pads for the logic capture).
- A-KN3: add the hazard "unintended continuous transmission from key input or TX line fault" to `docs/safety/hazard-analysis.md` with the F13 layers as controls and the coverage table as the fault tree; link RSK-012.
- A-KN4: verify distributor stock and price for TPD2E2U06DRLR, BAT54S, 74LVC1G123DP, 10 µF X7R 16 V 1206 (with DC-bias curve) on the distributor sites with timestamps before the BOM freeze.
- A-KN5: bench procedure TC-KEY-BOUNCE: capture 50 closures and 50 openings of the owner's hand key and paddle with sigrok-pico at >= 100 kHz, report maximum bounce, and close the debounce TBR.
- A-KN6: PDR trade study on T/R (SI-035) to include the QSK relay-life question and the cutoff node (R-KN5).
- A-KN7: update `keyer-and-key-interfaces.md` F11 wording on PESD3V3L2BT (C11) or supersede it by reference to this report.

## 5. Confidence

| Finding | Confidence | Why |
|---|---|---|
| F1 contradiction list | High | Sentences quoted from the three reports and the charter |
| F2 RP2350 facts | High | Current datasheet build 2025-07-29 quoted; table values read from the extracted text |
| F3 E9 reasoning and VIL table | High for the logic, Medium for the 120 µA worst case | The erratum gives "typically around 120μA" and a graph that was not extracted; applying it at all pad voltages is conservative |
| F4 network values | Medium | Straightforward circuit arithmetic; RF attenuation depends on layout and part parasitics (0.6 nH assumed) |
| F5 clamp selection | High for datasheet values; Low for stock and price | Distributor pages returned 403; snippets only |
| F6 debounce numbers | Medium | Sourced bounce statistics, but the owner's hardware is unmeasured (TBR) |
| F7 semantics and vectors | High for Curtis-derived cases (V4 to V8, V13 match the note's own examples); Medium for the switchpoint and same-paddle rules (Proposal) | Model output inspected case by case |
| F8 tolerance and harness | High | Arithmetic and the existing rustos trait plan |
| F9 emulation scope | High | Charter text |
| F10 bench method | Medium | sigrok-pico Pico 2 support confirmed from the README, sample rates not; tinySA close-in phase noise not published |
| F11 hand-key timeline | Medium | Depends on the relay figures (Omron via the reference report) and on Proposal margins |
| F12 envelope | High for definitions and CFR text; Medium for the -60 dBc at 500 Hz target | The target is a design choice; Part 97 is qualitative |
| F13 hazard controls | High for the architecture and the MAX6369 rejection (datasheet quoted); Medium for the 74LVC1G123 timing spread (K versus VCC figure not extracted) | |
| F14 number set | as per the rows' flags | |

## 6. Open items

1. RP2350 stepping of the procured Pico 2 modules (A2 versus A3/A4); the design is E9-safe either way, read `CHIP_ID.REVISION` at bring-up (carried from the rustos report).
2. Owner's key and paddle bounce and contact resistance (SI-034 gives TRS plugs only): measure per A-KN5; closes the debounce and contact-resistance TBRs.
3. 74LVC1G123 K factor versus VCC (Fig. 14) and the 10 µF capacitor's DC-bias derating: needed to state T_max's window with a datasheet basis instead of the assumed -25 % to +10 %.
4. sigrok-pico digital and analog sample rates on Pico 2 and the headless install path of sigrok-cli on macOS; if unavailable, scope the fallback capture firmware.
5. tinySA Ultra phase noise below 10 kHz offset (not published); determines how close in the tinySA can be used at all.
6. PA topology and the cutoff node (R-KN5): resolved by the PDR PA trade.
7. T/R architecture (SI-035): decides whether full QSK enters the requirements and changes T_lead and hang defaults.
8. Distributor stock and price for every part named here (A-KN4); all figures in this report are snippet-based.
9. Whether an external keyer's positive keying line (WinKeyer "high true TTL") is a supported input; it sets the +12 V abuse bound and is the case D2 protects.
10. ARRL Test Procedures Manual text for the 5 ms figure remains cited via secondary sources (carried from the reference-designs report).

## 7. Sources

- RP2350 datasheet, build 2025-07-29, build-version d126e9e-clean: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf (Table 853 PADS_BANK0 GPIO0; section 9.7; section 12.4.3; section 12.9; Table 1433, 1434, 1436; Appendix E RP2350-E9)
- Curtis Electro Devices, 8044 Series Keyer-on-a-Chip Application Note, 1/22/92: https://users.ox.ac.uk/~malcolm/radio/8044print.pdf
- ITU-R M.1677-1 (10/2009) section 2, via `keyer-and-key-interfaces.md` F4: https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
- 47 CFR 97.307 and 97.119, eCFR versioner API, issue date 2026-09-23: https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.307 ; https://www.ecfr.gov/api/versioner/v1/full/2026-09-23/title-47.xml?part=97&section=97.119
- Nexperia 74LVC1G123 product data sheet Rev. 8, 14 August 2023: https://assets.nexperia.com/documents/data-sheet/74LVC1G123.pdf
- Nexperia PESD3V3L2BT product data sheet, 27 June 2023: https://assets.nexperia.com/documents/data-sheet/PESD3V3L2BT.pdf
- Texas Instruments TPD2E001, SLLS684I, July 2006 revised March 2016: https://www.ti.com/lit/ds/symlink/tpd2e001.pdf
- Texas Instruments TPD2E2U06, SLLSEG9C, June 2013 revised December 2019: https://www.ti.com/lit/ds/symlink/tpd2e2u06.pdf
- Maxim Integrated MAX6369 to MAX6374 datasheet 19-1676 Rev 6 3/15 (Farnell mirror): https://www.farnell.com/datasheets/1904457.pdf ; product page https://www.analog.com/en/products/max6369.html
- Analog Devices LTC6993-1/-2/-3/-4 datasheet 69931234fb (DigiKey media mirror): https://media.digikey.com/PDF/Data%20Sheets/Linear%20Technology%20PDFs/LTC6993(-1,-2,-3,-4).pdf
- sigrok-pico (pico-coder), README: https://github.com/pico-coder/sigrok-pico
- tinySA Ultra specification: https://tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification
- QRP Labs AN005, HF PA kit with built-in standalone raised cosine controller: https://www.qrp-labs.com/images/appnotes/AN005_A4.pdf
- Omron G6K-2F-RF datasheet via `2m-cw-transceiver-reference-designs.md` F28: https://omronfs.omron.com/en_US/ecb/products/pdf/en-g6k_2f_rf.pdf
- IVARC/G3OTK key-click paper and W8JI note via `keyer-and-key-interfaces.md` F10: http://www.ivarc.org.uk/uploads/1/2/3/8/12380834/keyclicks_version_1.pdf ; https://www.w8ji.com/what_causes_clicks.htm
- K1EL WinKeyer3 datasheet rev 1.3 via `keyer-and-key-interfaces.md` F3, F5: https://www.k1elsystems.com/files/WK3_Datasheet_v1.3.pdf
- Distributor snippets observed 2026-09-25 about 11:45 PDT (Low confidence): https://www.digikey.com/en/products/detail/analog-devices-inc-maxim-integrated/MAX6369KA-T/948135 ; https://www.digikey.com/en/products/detail/nexperia-usa-inc/74LVC1G123DP-125/3679026 ; https://www.digikey.com/en/products/detail/texas-instruments/TPD2E001DRLR/1629057 ; https://www.tme.com/us/en-us/details/pesd3v3l2bt.215/protection-diodes-arrays/nexperia/pesd3v3l2bt-215/
- Project documents: `docs/process/00-charter.md` sections 9 to 11; `docs/process/04-verification-and-validation.md` sections 6.1, 6.2; `docs/requirements/l0-stakeholder/stakeholder-inputs.md` SI-013, SI-018, SI-019, SI-026, SI-033, SI-034, SI-035; `docs/risk/register.md` RSK-012; `docs/references/md/swehb/swe-134-safety-critical-software-design-requirements.md`; `docs/research/keyer-and-key-interfaces.md`; `docs/research/rustos-toolchain-proof.md`; `docs/research/2m-cw-transceiver-reference-designs.md`
- Scratch scripts (session scratchpad, not part of the repository): `calc/derive.py`, `calc/keyer_ref.py`
