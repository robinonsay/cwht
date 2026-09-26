# TX verification cases (TC-TX)

Rendered from `docs/test_cases/tx/test_cases.json` (module `TX`); the JSON is the controlled record and this file is regenerated from it, never edited by hand. Author: independent test author invocation (charter section 2, IEEE 1012 independence; `docs/process/08-agent-briefing.md` section 3.3), written from `docs/requirements/tx/requirements.json`, its rationales and verification notes, the process documents and the research reports the requirements cite, without reading any schematic, layout or firmware source. Status of every case: Draft (written, not yet reviewed under `docs/process/04-verification-and-validation.md` section 8.3 and `docs/templates/peer-review-checklist-test.md`). Date: 2026-09-25.

## Summary

- Cases: 16; live TX requirements with at least one case of their own method: 16 of 16.
- By method: Analysis 2, Inspection 1, Test 13.
- By evidence class: Bench 13, Inspection 1, Simulation 2.
- Credit rows (04 section 5.2): A 2, I 1, T-HW 13.
- Every case number equals the number of the requirement it closes, as each requirement's verification_note names it.
- Test requirements close by Bench on the delivered unit (T-HW); REQ-TX-005 and REQ-TX-006 by Simulation (A, Analysis accepted per RSK-011); REQ-TX-001 by Inspection of the CDR design data (I).
- Every case verifies a regulatory requirement; its Passed credit report is named by the OnAir authorization of `docs/reviews/TRR-Dn/decision-memo.md` (04 section 6.3).
- The pre-build Simulation and NanoVNA evidence named as supporting in the verification notes is added as supporting cases with the design (PDR, CDR); it never closes a Test requirement (04 section 5.1 item 2).
- Planned scripts, fixtures and records named in `automation_ref`, `setup` and `instruments` (for example `tools/tinysa_scan_check.py`, `tools/rf_probe_power.py`, `tools/analyze_logic_capture.py`, `tools/analyze_keyer_capture.py`, `tools/filter_s21_check.py`, `tools/check_tx_modulation_paths.py`, `tools/keyer_ref.py`, `hardware/sim/checks/*`, `docs/vv/fixtures/*`, the TV records `docs/cm/tool-validation/TV-NNN-*.md`) do not exist yet; each is a prerequisite of the case becoming Active.

## Case index

| Case | Title | Method | Class | Credit row | Requirements |
|---|---|---|---|---|---|
| TC-TX-001 | Keying envelope as the only modulating input of the transmit RF chain: schematic and netlist inspection | Inspection | Inspection | I | REQ-TX-001 |
| TC-TX-002 | Transmit carrier generated at commanded frequencies from 144.001 to 147.999 MHz | Test | Bench | T-HW | REQ-TX-002 |
| TC-TX-003 | Antenna-port carrier at most 1 uW with PA_EN deasserted and the exciter driven (fault-injection build) | Test | Bench | T-HW | REQ-TX-003 |
| TC-TX-004 | Commanded 0.5, 1 and 2 W steps within +/-1 dB into 50 ohm across the band and 6.4 to 8.4 V supply | Test | Bench | T-HW | REQ-TX-004 |
| TC-TX-005 | Raised-cosine envelope reproduced at the antenna port with 10-to-90 percent times within +/-10 percent at 3, 5 and 8 ms (transient Simulation) | Analysis | Simulation | A | REQ-TX-005 |
| TC-TX-006 | Keyed spectrum at least 60 dB below total mean power beyond 750 Hz with continuous 50 WPM dits (envelope FFT Simulation) | Analysis | Simulation | A | REQ-TX-006 |
| TC-TX-007 | Spurious emissions at most 25 uW from 9 kHz to 1.5 GHz at every power step, across the band and at 6.4 and 8.4 V | Test | Bench | T-HW | REQ-TX-007 |
| TC-TX-008 | Spurious emissions at least 60 dB below the mean carrier power at the 5 W step, with 2f, 3f and 7f reported against their victim services | Test | Bench | T-HW | REQ-TX-008 |
| TC-TX-009 | Harmonic-filter attenuation of at least 40 dB from 288 to 296 MHz between the PA output and the antenna port (NanoVNA S21) | Test | Bench | T-HW | REQ-TX-009 |
| TC-TX-010 | Harmonic-filter attenuation of at least 35 dB from 432 to 444 MHz between the PA output and the antenna port (NanoVNA S21) | Test | Bench | T-HW | REQ-TX-010 |
| TC-TX-011 | Harmonic-filter attenuation of at least 40 dB from 576 MHz to 1.5 GHz between the PA output and the antenna port (NanoVNA S21) | Test | Bench | T-HW | REQ-TX-011 |
| TC-TX-012 | Spurious emissions at most 25 uW at the 5 W step into SWR 2:1 loads at four phases | Test | Bench | T-HW | REQ-TX-012 |
| TC-TX-013 | Synthesizer frequency sample below 20 MHz whose frequency times the fixed ratio is within 1 kHz of the carrier | Test | Bench | T-HW | REQ-TX-013 |
| TC-TX-014 | Antenna-port carrier at most 1 uW with TX_KEY deasserted, PA_EN asserted and the exciter driven (fault-injection build) | Test | Bench | T-HW | REQ-TX-014 |
| TC-TX-015 | Output power at most 6.3 W into 50 ohm at every step, carrier frequency and 6.4, 7.4 and 8.4 V supply | Test | Bench | T-HW | REQ-TX-015 |
| TC-TX-016 | Antenna-port power at the set carrier frequency at most -57 dBm in Receive mode | Test | Bench | T-HW | REQ-TX-016 |

## Requirement coverage

| Requirement | Method | Cases (class, credit row) |
|---|---|---|
| REQ-TX-001 | Inspection | TC-TX-001 (Inspection, I) |
| REQ-TX-002 | Test | TC-TX-002 (Bench, T-HW) |
| REQ-TX-003 | Test | TC-TX-003 (Bench, T-HW) |
| REQ-TX-004 | Test | TC-TX-004 (Bench, T-HW) |
| REQ-TX-005 | Analysis | TC-TX-005 (Simulation, A) |
| REQ-TX-006 | Analysis | TC-TX-006 (Simulation, A) |
| REQ-TX-007 | Test | TC-TX-007 (Bench, T-HW) |
| REQ-TX-008 | Test | TC-TX-008 (Bench, T-HW) |
| REQ-TX-009 | Test | TC-TX-009 (Bench, T-HW) |
| REQ-TX-010 | Test | TC-TX-010 (Bench, T-HW) |
| REQ-TX-011 | Test | TC-TX-011 (Bench, T-HW) |
| REQ-TX-012 | Test | TC-TX-012 (Bench, T-HW) |
| REQ-TX-013 | Test | TC-TX-013 (Bench, T-HW) |
| REQ-TX-014 | Test | TC-TX-014 (Bench, T-HW) |
| REQ-TX-015 | Test | TC-TX-015 (Bench, T-HW) |
| REQ-TX-016 | Test | TC-TX-016 (Bench, T-HW) |

## Cases

### TC-TX-001: Keying envelope as the only modulating input of the transmit RF chain: schematic and netlist inspection

| Field | Value |
|---|---|
| Requirements | REQ-TX-001 |
| Method / class | Inspection / Inspection |
| Credit row | I |
| Status | Draft |
| Automation | `tools/check_tx_modulation_paths.py` |

**Setup.** Article: design data at tag baseline/cdr: the transmitter schematic sheets (the design elements B04, B05 and B06 that REQ-TX-001 names in design_refs, plus every sheet that carries a part of the exciter, envelope modulator, PA or synthesizer) and the netlist exported from them. Configuration: kicad-cli at its lock path /Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli exports the netlist and a PDF of every transmitter sheet; the planned checker tools/check_tx_modulation_paths.py (shared with TC-SYS-001) reads a pin table that lists every gain-control, bias, supply-modulation, tuning-voltage, reference and enable pin of the exciter, envelope-modulator, PA and synthesizer parts, taken from each part's datasheet and recorded with the datasheet revision, and lists every net that reaches one of those pins through any number of passive parts, and every path from an audio net (sidetone, receive audio, audio DAC or PWM, headphone) to any RF-chain part. Credit row: I. Inspection of design data closed at CDR on the product baseline (docs/process/04-verification-and-validation.md sections 5.1 item 4 and 5.2 row I) and confirmed at SAR by the physical configuration audit; the post-build Bench check of gross modulation named in the verification_note is supporting only and is not part of this case; the firmware keying-path inspection of the parent REQ-SYS-001 is TC-SYS-001 and is not repeated. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). Tools: kicad-cli 10.0.6 and Python per tools/toolchain.lock.md. Safety: not applicable (design data only). Environment: not applicable.

**Procedure.**

1. Export the netlist and a PDF of the transmitter sheets at tag baseline/cdr with kicad-cli sch export netlist and kicad-cli sch export pdf; record the tag commit.
2. Check that the pin table lists every gain-control, bias, supply-modulation, tuning-voltage, reference and enable pin of each exciter, envelope-modulator, PA and synthesizer part on the sheets, with the datasheet revision of each part; add any missing pin before the run and record the addition.
3. Run tools/check_tx_modulation_paths.py on the netlist and the pin table; save the net list and the audio-path list.
4. Classify every listed net on the rendered sheets as one of: the envelope drive; a DC bias or supply with its decoupling; a static digital setting (synthesizer programming bus, PA_EN, TX_KEY, power-step select); ground. Record any other net as a finding.
5. Confirm that every path in the audio-path list ends in a DC supply or ground return with decoupling and couples no signal into an RF-chain part; record any other path as a finding.
6. Confirm on the rendered sheets that the envelope drive is the only time-varying input to the amplitude-control nodes and that the synthesizer has no modulation input other than its frequency-setting interface.
7. Record the tool versions, the tag commit and the SHA-256 of the checker outputs in the report.
8. On any finding stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every net that reaches a modulating or control pin of the exciter, envelope modulator, PA and synthesizer is classified as the envelope drive, a DC bias or supply with decoupling, a static digital setting or ground, and no audio net reaches any RF-chain part other than through a DC supply or ground return with decoupling; otherwise Fail.

**Expected artifacts.**

- `tx-netlist.net` (other): kicad-cli netlist of the transmitter sheets at baseline/cdr
- `tx-sheets.pdf` (other): Rendered transmitter sheets reviewed against the net list
- `tx-modulation-nets.csv` (csv): Net, pin, part, datasheet revision and classification of every listed net
- `tx-modulation-check.log.txt` (log): Checker output including the audio-path list

### TC-TX-002: Transmit carrier generated at commanded frequencies from 144.001 to 147.999 MHz

| Field | Value |
|---|---|
| Requirements | REQ-TX-002 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra; carrier marker read at 1 kHz resolution bandwidth or narrower in a 100 kHz span centred on the commanded frequency; the frequency is commanded with the tuning control and read from the display; 0.5 W step unless a step names the 5 W step; straight-key holds of 3 s with at least 10 s between them; bench supply through the pack-resistance fixture. The frequency accuracy itself is the Analysis of REQ-SYS-010 (TC-SYS-009); this case shows that a carrier is generated at each commanded frequency across the range. Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-002 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): straight key for every reading, plus one paddle reading at 146.000 MHz. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Command 146.000 MHz, close the straight key for 3 s and read the marker frequency and level; this reading is the level reference.
3. Repeat the reading at 144.001, 144.002, 144.100, 145.000, 147.000, 147.900, 147.998 and 147.999 MHz.
4. Repeat the reading at the off-grid frequencies 144.321, 144.777, 145.555, 146.520, 146.999, 147.123, 147.456 and 147.777 MHz.
5. At 144.001 and 147.999 MHz select the 5 W step and repeat the reading.
6. At 146.000 MHz and the 0.5 W step hold the paddle dit lever in Iambic A at 15 WPM for 3 s and read the marker frequency and max-hold level.
7. Run tools/tinysa_scan_check.py on the exported marker readings to correct each level for the attenuator S21.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-008 and TPM-006 (marker offsets, data only).
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at every commanded frequency the tinySA shows a carrier whose marker frequency differs from the commanded frequency by no more than 2.5 ppm (the REQ-SYS-010 tolerance, 370 Hz at 148 MHz) plus the tinySA frequency uncertainty of its TV record, and whose level corrected to the antenna port is within 3 dB of the 146.000 MHz reference at the same step; otherwise Fail. The 3 dB window separates a generated carrier from leakage or a spurious response; the power level itself is verified by TC-TX-004 and TC-SYS-011.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `carrier-frequencies.csv` (csv): Commanded frequency, step, keying source, marker frequency, offset, corrected level
- `carrier-markers.png` (plot): tinySA marker screenshots exported per frequency
- `attenuator-s21.s2p` (other): Attenuator and cable S21 of the session
- `carrier-setup.jpg` (photo): Photograph of the setup

### TC-TX-003: Antenna-port carrier at most 1 uW with PA_EN deasserted and the exciter driven (fault-injection build)

| Field | Value |
|---|---|
| Requirements | REQ-TX-003 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over USB serial or the UART test pads and which toggles the injection-marker test pad at the instant of each injection; the same flavour TC-SYS-005 uses); the release image is restored and checked with picotool verify at the end of the case. Configuration: an injection command that drives the exciter as in TxPending (synthesizer on the commanded frequency, envelope drive at full scale, TX_KEY asserted) while PA_EN is held deasserted, for 10 s per activation; antenna port to the calibrated power attenuator and the tinySA Ultra at the commanded frequency, resolution bandwidth 1 kHz or narrower, span 100 kHz, max-hold; logic capture on PA_EN, TX_KEY and the injection-marker pad confirms PA_EN stays low; 5 W step selected; readings corrected by the attenuator S21 of this session; the noise floor referred to the antenna port is at least 10 dB below -30.0 dBm (1 uW). Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-003 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-006, HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): the carrier is driven by the injection command, not by a key; the reference key-down of step 4 uses the straight key, and both key types key the transmitter in TC-TX-002, TC-TX-004, TC-TX-007 and TC-TX-015. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Flash the fault-injection build with picotool load, check it with picotool verify and record its SHA-256.
3. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
4. At 146.000 MHz and the 5 W step close the straight key for 3 s and read the carrier level (confirms that the setup reads the carrier).
5. Issue the injection command at 146.000 MHz; during the 10 s activation read the max-hold level at the commanded frequency and confirm on the capture that PA_EN stayed low and TX_KEY high.
6. Repeat the previous step at 144.001 and 147.999 MHz.
7. Set the supply to 8.4 V and repeat the three activations.
8. Restore the release image with picotool load and confirm that picotool verify matches the VDD SHA-256.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if, at 144.001, 146.000 and 147.999 MHz and at 7.4 and 8.4 V supply, with PA_EN low throughout each activation on the capture, the carrier power at the antenna port, corrected for the attenuator S21 and increased by the tinySA level accuracy of its TV record, is at most -30.0 dBm (1 uW); otherwise Fail. An activation in which PA_EN rises is a Procedure-correction NCR against the fault-injection build, not a requirement result.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise; credit-bearing after its TV record docs/cm/tool-validation/TV-NNN-logic-capture.md
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- USB-UART breakout on the UART test pads (docs/vv/fixtures/usb-breakout.md, planned)

**Expected artifacts.**

- `pa-en-isolation.csv` (csv): Frequency, supply, carrier level at the tinySA, corrected antenna-port level, noise floor
- `pa-en-isolation.sr` (other): Logic capture of PA_EN, TX_KEY and the injection marker for every activation
- `pa-en-isolation-traces.png` (plot): tinySA max-hold traces per activation
- `pa-en-isolation-setup.jpg` (photo): Photograph of the setup

### TC-TX-004: Commanded 0.5, 1 and 2 W steps within +/-1 dB into 50 ohm across the band and 6.4 to 8.4 V supply

| Field | Value |
|---|---|
| Requirements | REQ-TX-004 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/rf_probe_power.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: bench supply through the pack-resistance fixture into the battery terminals; dummy load with the diode RF probe on its T; multimeter on the probe output, P = Vpk^2 / 100 with the probe characterization of TC-SYS-010 (docs/process/04-verification-and-validation.md section 6.2); for the secondary reading the dummy load is replaced by the calibrated power attenuator and the tinySA Ultra; key-downs of 3 s with at least 10 s between them. Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-004 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-006 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): straight key for every reading, plus one paddle reading at 146.00 MHz. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Confirm that TC-SYS-010 is Passed and copy its power uncertainty into the report.
2. Set the supply to 6.4 V at the battery terminals under load.
3. At 144.001 MHz select the 0.5 W step, close the straight key for 3 s and read the probe output; repeat for the 1 W and 2 W steps.
4. Repeat the previous step at 144.05, 146.00, 147.95 and 147.999 MHz.
5. Set the supply to 8.4 V and repeat the two previous steps.
6. At 146.00 MHz, 7.4 V and the 1 W step, hold the paddle dah lever at 15 WPM for 3 s and read the probe; compare with a straight-key reading at the same condition.
7. Replace the dummy load by the attenuator and tinySA; at 146.00 MHz and 7.4 V read the carrier power at each step (secondary reading).
8. Run tools/rf_probe_power.py on the readings to compute each power with its uncertainty band.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-004 and TPM-015.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at every frequency and supply voltage the probe power with its characterized uncertainty band lies entirely inside 0.397 to 0.629 W at the 0.5 W step, 0.794 to 1.259 W at the 1 W step and 1.589 to 2.518 W at the 2 W step (+/-1 dB); otherwise Fail. A probe and tinySA disagreement beyond their combined uncertainty, or a paddle reading that differs from the straight-key reading by more than the probe uncertainty, is a Procedure-correction NCR (docs/process/04-verification-and-validation.md section 6.2), not a requirement result.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range (docs/vv/fixtures/rf-probe.md, planned)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `reduced-steps.csv` (csv): Frequency, supply, step, keying source, probe reading, power and uncertainty band
- `reduced-steps-secondary.csv` (csv): tinySA secondary readings with attenuator correction
- `reduced-steps-setup.jpg` (photo): Photograph of the setup

### TC-TX-005: Raised-cosine envelope reproduced at the antenna port with 10-to-90 percent times within +/-10 percent at 3, 5 and 8 ms (transient Simulation)

| Field | Value |
|---|---|
| Requirements | REQ-TX-005 |
| Method / class | Analysis / Simulation |
| Credit row | A |
| Status | Draft |
| Automation | `hardware/sim/checks/envelope_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the envelope drive, shaping network and PA sheets and the model deck built from them. Configuration: the envelope-domain model deck hardware/sim/tx/envelope.asc (planned): envelope drive, shaping network and PA transfer model with the CDR part values and the PA model named by TS-003 and TS-006, antenna port into 50 ohm; the RF envelope a(t) at the antenna port is the simulated quantity (the 146 MHz carrier is not simulated over the record length); runs by the LTspice batch command of the tools/toolchain.lock.md LTspice row (one analysis per deck, ADR-018 telemetry opt-out); tolerance corners by the checker option --corners. The checker hardware/sim/checks/envelope_check.py (planned; the envelope checker of docs/research/regulatory-corpus-and-operators.md ACTION-8) reads the 10-to-90 percent rise and fall times of every keyed element. Credit row: A. Analysis closed by Simulation on the CDR design data (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2 row A) and confirmed at SAR by the physical configuration audit of the shaping-network part values; Analysis accepted per RSK-011 (REQ-TX-005 verification_note; docs/process/04-verification-and-validation.md section 6.2 keying-envelope row: no instrument of section 6.1 captures the analog RF envelope). The Bench logic capture of the envelope drive steps is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-005 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Tools: LTspice and Python versions per tools/toolchain.lock.md. Safety: not applicable. Environment: not applicable.

**Procedure.**

1. Confirm that the deck part values equal the transmitter schematic at tag baseline/cdr (the checker prints the diff; an empty diff is required).
2. Run the deck at the 3 ms setting, the 5 W step and 7.4 V supply with a key-down of 100 ms; export a(t).
3. Run hardware/sim/checks/envelope_check.py on the export; it reports the 10-to-90 percent rise and fall times.
4. Repeat the two previous steps at the 5 ms and 8 ms settings.
5. Repeat the three settings at the 0.5 W step and at 6.4 and 8.4 V supply.
6. Repeat every run with the shaping-network parts at their tolerance corners and record the worst case per setting.
7. Record tool versions and the git commits of the deck and the checker in the report.
8. On any assertion failure stop and open an NCR per docs/process/04-verification-and-validation.md section 10. (a non-empty schematic diff also stops the case)

**Acceptance criteria.** Pass if, at each of the 3, 5 and 8 ms settings, at the 0.5 W and 5 W steps, at 6.4, 7.4 and 8.4 V supply and at every shaping-network tolerance corner, the 10-to-90 percent rise and fall times of the simulated antenna-port RF envelope are within +/-10 percent of the commanded setting (2.7 to 3.3 ms, 4.5 to 5.5 ms and 7.2 to 8.8 ms); otherwise Fail.

**Expected artifacts.**

- `envelope-times.csv` (csv): Setting, step, supply, corner, rise and fall times
- `envelope-plot.png` (plot): Simulated envelopes with the 10 and 90 percent points and the tolerance bands
- `envelope-check.log.txt` (log): Checker output with pass/fail per run and the schematic diff result

### TC-TX-006: Keyed spectrum at least 60 dB below total mean power beyond 750 Hz with continuous 50 WPM dits (envelope FFT Simulation)

| Field | Value |
|---|---|
| Requirements | REQ-TX-006 |
| Method / class | Analysis / Simulation |
| Credit row | A |
| Status | Draft |
| Automation | `hardware/sim/checks/keying_spectrum_check.py` |

**Setup.** Article: design data at tag baseline/cdr: the envelope drive, shaping network and PA sheets and the model deck built from them (the deck of TC-TX-005). Configuration: the envelope-domain model deck hardware/sim/tx/envelope.asc (planned): envelope drive, shaping network and PA transfer model with the CDR part values and the PA model named by TS-003 and TS-006, antenna port into 50 ohm; the RF envelope a(t) at the antenna port is the simulated quantity (the 146 MHz carrier is not simulated over the record length); runs by the LTspice batch command of the tools/toolchain.lock.md LTspice row (one analysis per deck, ADR-018 telemetry opt-out); tolerance corners by the checker option --corners. Keying: continuous 50 WPM dits (24 ms key-down, 24 ms key-up) for at least 4 s of simulated time after a 100 ms settling interval. The checker hardware/sim/checks/keying_spectrum_check.py (planned; the FFT checker of docs/research/regulatory-corpus-and-operators.md ACTION-8) computes the spectrum of a(t) with a Blackman-Harris window at a resolution bandwidth of 10 Hz or finer (stated in its log) and reports the power in every 10 Hz cell from 750 Hz to 50 kHz on both sides relative to the total mean power of the same record, the reference of docs/research/regulatory-corpus-and-operators.md F7 that REQ-TX-006 states; the level relative to the carrier line is recorded as data. Credit row: A. Analysis closed by Simulation on the CDR design data (docs/process/04-verification-and-validation.md sections 5.1 item 5 and 5.2 row A); Analysis accepted per RSK-011 (REQ-TX-006 verification_note; docs/process/04-verification-and-validation.md section 6.1: the close-in keying spectrum on the tinySA is not credit-bearing). The Bench tinySA max-hold and the second-station OnAir report are supporting only and are not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-006 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Tools: LTspice and Python versions per tools/toolchain.lock.md. Safety: not applicable. Environment: not applicable.

**Procedure.**

1. Confirm that the deck part values equal the transmitter schematic at tag baseline/cdr (empty diff required).
2. Known-answer check of the checker: run it on an ideal raised-cosine envelope with a 5 ms full transition and continuous 50 WPM dits; it must place the -60 dB point at 614 Hz within one 10 Hz cell, the F7 value of docs/research/regulatory-corpus-and-operators.md.
3. Run the deck with continuous 50 WPM dits at the 5 ms setting, the 5 W step and 7.4 V; export a(t).
4. Run hardware/sim/checks/keying_spectrum_check.py on the export; it reports the highest 10 Hz cell relative to the total mean power in each 100 Hz band from 750 Hz to 50 kHz on both sides.
5. Repeat the two previous steps at the 3 ms and 8 ms settings.
6. Repeat the three settings at the 0.5 W step and at every shaping-network tolerance corner.
7. Record tool versions, the resolution bandwidth and window, and the git commits of the deck and the checker in the report, and the worst sideband level for MOP-009.
8. On any assertion failure stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the checker known-answer step reproduces 614 Hz within 10 Hz and, for each of the 3, 5 and 8 ms settings, at the 0.5 W and 5 W steps and at every shaping-network tolerance corner, the power in every 10 Hz cell of the simulated keyed signal at offsets from 750 Hz to 50 kHz on both sides of the carrier is at least 60.0 dB below the total mean power of the record, computed with the same window; otherwise Fail.

**Expected artifacts.**

- `keying-spectrum.csv` (csv): Setting, step, corner, offset band and level relative to the total mean power and to the carrier line
- `keying-spectrum.png` (plot): Keyed spectra per setting with the -60 dB limit drawn from 750 Hz
- `keying-spectrum-check.log.txt` (log): Checker output with the window, resolution bandwidth and pass/fail per run

### TC-TX-007: Spurious emissions at most 25 uW from 9 kHz to 1.5 GHz at every power step, across the band and at 6.4 and 8.4 V

| Field | Value |
|---|---|
| Requirements | REQ-TX-007 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra; bench supply through the pack-resistance fixture; transmitter keyed with continuous dits at 25 WPM from the keying fixture holding the paddle dit contact in Iambic A for 10 s per activation (104 dits, below the 128-element and 30 s limits of the paddle watchdog, HZ-004 K4, proposed) with at least 10 s between activations; the bench test-mode generator is not used because every bench test mode forces the 0.5 W step (HZ-004 K13); max-hold over the keyed dits; spurious means any discrete signal outside the carrier +/-10 kHz (47 CFR 97.3(a)(43), corpus: 47cfr-97.3.md; inside that window the close-in keying spectrum is the Analysis of TC-TX-006, docs/process/04-verification-and-validation.md section 6.1 tinySA row); span segmented so that the noise floor referred to the antenna port is at least 10 dB below -16.02 dBm; readings corrected by the attenuator S21 of this session (below the NanoVNA lower limit the S21 at that limit is used and the report says so). Limit: 25 uW, 47 CFR 97.307(e) (corpus: 47cfr-97.307.md, eCFR issue 2026-09-23). Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): the fixture keys the paddle input for the scans; step 7 repeats the harmonic readings with the owner's straight key and paddle. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. At 146.00 MHz, 7.4 V and the 5 W step close the straight key for 3 s and read the key-down carrier level (max-hold, 10 kHz span); compute the carrier power at the antenna port.
3. Scan 9 kHz to 1.5 GHz in segments with max-hold over at least two fixture activations per segment; record 2f, 3f and 7f individually and every other signal more than 6 dB above the noise floor.
4. For every recorded signal within 10 dB of -16.02 dBm, add 10 dB of attenuation and re-read: a true emission drops by 10 dB +/-1 dB; a signal that drops by more is analyzer-generated, excluded and recorded.
5. Repeat the scan at 144.05, 146.00 and 147.95 MHz for the 0.5, 1, 2 and 5 W steps at 6.4 V and at 8.4 V (24 combinations).
6. Repeat the scan at the 5 W step and 7.4 V with the carrier at 144.001 MHz and at 147.999 MHz.
7. At 146.00 MHz, 5 W and 7.4 V re-read 2f and 3f keyed by the straight key (3 s holds) and by the owner's paddle (squeezes of at most 1.5 s at 25 WPM, below the 2 s both-contacts-closed limit of the paddle watchdog, HZ-004 K4, proposed); compare with the fixture readings.
8. Run tools/tinysa_scan_check.py on the exported traces: it corrects for the attenuator S21, adds the tinySA level accuracy and reports each emission in dBm at the antenna port.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-009 and TPM-007.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every spurious emission at the antenna port, corrected for the attenuator S21 and increased by the tinySA level accuracy of its TV record, is at most -16.02 dBm (25 uW) in every one of the 24 step, frequency and supply combinations and at both band-edge carriers; otherwise Fail. Straight-key and paddle readings within 1 dB of the fixture readings confirm that the keying source does not change the result; a larger difference is a Procedure-correction NCR.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Keying fixture: optocoupler contacts across the key-jack tip and ring, driven by a Pico 2 running the scripted closure pattern of the step, pattern timing from its crystal (docs/vv/fixtures/keying-fixture.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `spurious-abs.csv` (csv): Combination, frequency, corrected level in dBm for every recorded emission
- `spurious-abs-traces.png` (plot): tinySA traces per segment and combination
- `attenuator-s21.s2p` (other): Attenuator and cable S21 of the session
- `spurious-abs-check.log.txt` (log): tools/tinysa_scan_check.py output with pass/fail

### TC-TX-008: Spurious emissions at least 60 dB below the mean carrier power at the 5 W step, with 2f, 3f and 7f reported against their victim services

| Field | Value |
|---|---|
| Requirements | REQ-TX-008 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: as TC-TX-007 at the 5 W step: antenna port to the calibrated power attenuator and the tinySA Ultra; bench supply through the pack-resistance fixture; transmitter keyed with continuous dits at 25 WPM from the keying fixture holding the paddle dit contact in Iambic A for 10 s per activation (104 dits, below the 128-element and 30 s limits of the paddle watchdog, HZ-004 K4, proposed) with at least 10 s between activations; the bench test-mode generator is not used because every bench test mode forces the 0.5 W step (HZ-004 K13); max-hold across the keying envelope; spurious means any discrete signal outside the carrier +/-10 kHz; span segmented so that the noise floor referred to the antenna port is at least 6 dB below the carrier level minus 60 dB (about -23 dBm at 5 W); the mean carrier power is the key-down carrier level read in the same session. Victim services from the 47 CFR 2.106 harmonic-band extract (corpus: 47cfr-2.106-harmonic-bands.md): 2f in 267 to 322 MHz (Federal fixed and mobile, military), 3f in 420 to 450 MHz (Federal radiolocation; amateur secondary), 7f in 960 to 1164 MHz (aeronautical mobile (R) and aeronautical radionavigation). Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-008 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): the fixture keys the paddle input for the scans; step 6 repeats the harmonic readings with the owner's straight key and paddle. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. At 146.00 MHz, 7.4 V and the 5 W step close the straight key for 3 s and read the key-down carrier level (max-hold, 10 kHz span); compute the mean carrier power at the antenna port.
3. Scan 9 kHz to 1.5 GHz in segments with max-hold over at least two fixture activations per segment; record 2f, 3f and 7f individually with their victim service and every other signal more than 6 dB above the noise floor.
4. For every recorded signal within 10 dB of the carrier level minus 60 dB, add 10 dB of attenuation and re-read; exclude and record analyzer-generated signals as in TC-TX-007.
5. Repeat the carrier reading and the scan at 144.001, 144.05, 147.95 and 147.999 MHz at 7.4 V, and at 146.00 MHz at 6.4 and 8.4 V.
6. At 146.00 MHz and 7.4 V re-read 2f and 3f keyed by the straight key (3 s holds) and by the owner's paddle (squeezes of at most 1.5 s at 25 WPM, below the 2 s both-contacts-closed limit of the paddle watchdog, HZ-004 K4, proposed); compare with the fixture readings.
7. Run tools/tinysa_scan_check.py: it corrects both levels for the attenuator S21 at their frequencies and reports each emission in dB below the carrier with the tinySA relative level uncertainty of its TV record.
8. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-009 and TPM-007 (margin over 53 dB, CON-002).
9. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if, at every carrier frequency and supply voltage of the procedure at the 5 W step, every spurious emission at the antenna port, with its level increased by the tinySA relative level uncertainty of its TV record, is at least 60.0 dB below the mean carrier power read in the same session, with 2f, 3f and 7f reported individually with their victim service; otherwise Fail. Straight-key and paddle readings within 1 dB of the fixture readings confirm that the keying source does not change the result; a larger difference is a Procedure-correction NCR.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Keying fixture: optocoupler contacts across the key-jack tip and ring, driven by a Pico 2 running the scripted closure pattern of the step, pattern timing from its crystal (docs/vv/fixtures/keying-fixture.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `spurious-margin.csv` (csv): Carrier frequency, supply, emission frequency, corrected level, dB below carrier, victim service
- `spurious-margin-traces.png` (plot): tinySA traces per segment and condition
- `attenuator-s21.s2p` (other): Attenuator and cable S21 of the session
- `spurious-margin-check.log.txt` (log): tools/tinysa_scan_check.py output with pass/fail

### TC-TX-009: Harmonic-filter attenuation of at least 40 dB from 288 to 296 MHz between the PA output and the antenna port (NanoVNA S21)

| Field | Value |
|---|---|
| Requirements | REQ-TX-009 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/filter_s21_check.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for access to the harmonic-filter test point, unit unpowered, firmware irrelevant to the passive path (the installed version is recorded). Configuration: NanoVNA port 1 on the filter test point of docs/safety/hazard-analysis.md section 8.2 row 10 through the filter test-point adapter, with the PA isolated by its test link; port 2 on the antenna port; SOLT calibration with a through at the two cable ends, sweep 270 to 310 MHz with at least 201 points; the T/R relay in its unpowered state unless the CDR build-to specification names another state for this measurement; the isolation floor (both cable ends terminated in 50 ohm) is measured in the same session and must lie at least 10 dB below -40 dB across the sweep, otherwise the case is Blocked with the borrowed-instrument alternative of docs/process/04-verification-and-validation.md section 6.3 named (NanoVNA dynamic range above 900 MHz is unverified, open question of the test author). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-009 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): not applicable; the case measures a passive path with the unit unpowered and involves no keying. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: the unit is unpowered for the whole case and the pack is removed; antistatic wrist strap while the lid is off; the PA test link is restored and inspected before the lid is closed. Environment: room temperature 18 to 28 C; unit unpowered, pack removed.

**Procedure.**

1. Remove the pack, open the PA test link and connect the filter test-point adapter.
2. Calibrate the NanoVNA (SOLT with through) at the two cable ends over 270 to 310 MHz; check the dummy load and the through; save the calibration check.
3. Terminate both cable ends in 50 ohm and record the S21 isolation floor over the sweep.
4. Connect port 1 to the test-point adapter and port 2 to the antenna port; record S21 and save the Touchstone file.
5. Run tools/filter_s21_check.py (planned) on the file: it reports the highest S21 in 288 to 296 MHz, the isolation floor margin, and pass/fail.
6. Disconnect the adapter, restore the PA test link and photograph it restored.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-009 and TPM-007.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the isolation floor lies at least 10 dB below -40 dB across the sweep and S21 from the filter test point to the antenna port, normalized to the through calibration and increased by the NanoVNA S21 uncertainty of its TV record, is at most -40.0 dB at every point from 288 to 296 MHz; otherwise Fail.

**Instruments and fixtures.**

- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Filter test-point adapter from the harmonic-filter test point of docs/safety/hazard-analysis.md section 8.2 row 10 to SMA, with the PA test link open (docs/vv/fixtures/filter-test-point.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report

**Expected artifacts.**

- `filter-s21-009.s2p` (other): S21 from the filter test point to the antenna port, 270 to 310 MHz
- `filter-isolation-009.s2p` (other): Isolation floor with both cable ends terminated
- `filter-s21-009.png` (plot): S21 plot with the -40 dB limit over 288 to 296 MHz
- `filter-s21-009-link-restored.jpg` (photo): Photograph of the restored PA test link

### TC-TX-010: Harmonic-filter attenuation of at least 35 dB from 432 to 444 MHz between the PA output and the antenna port (NanoVNA S21)

| Field | Value |
|---|---|
| Requirements | REQ-TX-010 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/filter_s21_check.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for access to the harmonic-filter test point, unit unpowered, firmware irrelevant to the passive path (the installed version is recorded). Configuration: NanoVNA port 1 on the filter test point of docs/safety/hazard-analysis.md section 8.2 row 10 through the filter test-point adapter, with the PA isolated by its test link; port 2 on the antenna port; SOLT calibration with a through at the two cable ends, sweep 420 to 460 MHz with at least 201 points; the T/R relay in its unpowered state unless the CDR build-to specification names another state for this measurement; the isolation floor (both cable ends terminated in 50 ohm) is measured in the same session and must lie at least 10 dB below -35 dB across the sweep, otherwise the case is Blocked with the borrowed-instrument alternative of docs/process/04-verification-and-validation.md section 6.3 named (NanoVNA dynamic range above 900 MHz is unverified, open question of the test author). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-010 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): not applicable; the case measures a passive path with the unit unpowered and involves no keying. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: the unit is unpowered for the whole case and the pack is removed; antistatic wrist strap while the lid is off; the PA test link is restored and inspected before the lid is closed. Environment: room temperature 18 to 28 C; unit unpowered, pack removed.

**Procedure.**

1. Remove the pack, open the PA test link and connect the filter test-point adapter.
2. Calibrate the NanoVNA (SOLT with through) at the two cable ends over 420 to 460 MHz; check the dummy load and the through; save the calibration check.
3. Terminate both cable ends in 50 ohm and record the S21 isolation floor over the sweep.
4. Connect port 1 to the test-point adapter and port 2 to the antenna port; record S21 and save the Touchstone file.
5. Run tools/filter_s21_check.py (planned) on the file: it reports the highest S21 in 432 to 444 MHz, the isolation floor margin, and pass/fail.
6. Disconnect the adapter, restore the PA test link and photograph it restored.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-009 and TPM-007.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if the isolation floor lies at least 10 dB below -35 dB across the sweep and S21 from the filter test point to the antenna port, normalized to the through calibration and increased by the NanoVNA S21 uncertainty of its TV record, is at most -35.0 dB at every point from 432 to 444 MHz; otherwise Fail.

**Instruments and fixtures.**

- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Filter test-point adapter from the harmonic-filter test point of docs/safety/hazard-analysis.md section 8.2 row 10 to SMA, with the PA test link open (docs/vv/fixtures/filter-test-point.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report

**Expected artifacts.**

- `filter-s21-010.s2p` (other): S21 from the filter test point to the antenna port, 420 to 460 MHz
- `filter-isolation-010.s2p` (other): Isolation floor with both cable ends terminated
- `filter-s21-010.png` (plot): S21 plot with the -35 dB limit over 432 to 444 MHz
- `filter-s21-010-link-restored.jpg` (photo): Photograph of the restored PA test link

### TC-TX-011: Harmonic-filter attenuation of at least 40 dB from 576 MHz to 1.5 GHz between the PA output and the antenna port (NanoVNA S21)

| Field | Value |
|---|---|
| Requirements | REQ-TX-011 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/filter_s21_check.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for access to the harmonic-filter test point, unit unpowered, firmware irrelevant to the passive path (the installed version is recorded). Configuration: NanoVNA port 1 on the filter test point of docs/safety/hazard-analysis.md section 8.2 row 10 through the filter test-point adapter, with the PA isolated by its test link; port 2 on the antenna port; SOLT calibration with a through at the two cable ends, sweep 560 MHz to 1.5 GHz with at least 201 points; the T/R relay in its unpowered state unless the CDR build-to specification names another state for this measurement; the isolation floor (both cable ends terminated in 50 ohm) is measured in the same session and must lie at least 10 dB below -40 dB across the sweep, otherwise the case is Blocked with the borrowed-instrument alternative of docs/process/04-verification-and-validation.md section 6.3 named. The NanoVNA model, its verified upper frequency and its S21 dynamic range are taken from its TV record (docs/cm/tool-validation/TV-NNN-nanovna.md, which states the owner's model); any span above the verified range is measured on a borrowed vector network analyzer under that contingency, with its model, serial and the owner's confirmation of its calibration state in the report. Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-011 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): not applicable; the case measures a passive path with the unit unpowered and involves no keying. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: the unit is unpowered for the whole case and the pack is removed; antistatic wrist strap while the lid is off; the PA test link is restored and inspected before the lid is closed. Environment: room temperature 18 to 28 C; unit unpowered, pack removed.

**Procedure.**

1. Remove the pack, open the PA test link and connect the filter test-point adapter.
2. Calibrate the NanoVNA (SOLT with through) at the two cable ends over 560 MHz to 1.5 GHz; check the dummy load and the through; save the calibration check.
3. Terminate both cable ends in 50 ohm and record the S21 isolation floor over the sweep.
4. Connect port 1 to the test-point adapter and port 2 to the antenna port; record S21 and save the Touchstone file.
5. Run tools/filter_s21_check.py (planned) on the file: it reports the highest S21 in 576 MHz to 1.5 GHz, the isolation floor margin, and pass/fail.
6. Disconnect the adapter, restore the PA test link and photograph it restored.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-009 and TPM-007.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if every point from 576 MHz to 1.5 GHz was measured on an instrument whose TV record or contingency entry covers that frequency, the isolation floor lies at least 10 dB below -40 dB across the sweep and S21 from the filter test point to the antenna port, normalized to the through calibration and increased by the NanoVNA S21 uncertainty of its TV record, is at most -40.0 dB at every point from 576 MHz to 1.5 GHz; otherwise Fail.

**Instruments and fixtures.**

- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Filter test-point adapter from the harmonic-filter test point of docs/safety/hazard-analysis.md section 8.2 row 10 to SMA, with the PA test link open (docs/vv/fixtures/filter-test-point.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report

**Expected artifacts.**

- `filter-s21-011.s2p` (other): S21 from the filter test point to the antenna port, 560 MHz to 1.5 GHz
- `filter-isolation-011.s2p` (other): Isolation floor with both cable ends terminated
- `filter-s21-011.png` (plot): S21 plot with the -40 dB limit over 576 MHz to 1.5 GHz
- `filter-s21-011-link-restored.jpg` (photo): Photograph of the restored PA test link

### TC-TX-012: Spurious emissions at most 25 uW at the 5 W step into SWR 2:1 loads at four phases

| Field | Value |
|---|---|
| Requirements | REQ-TX-012 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: each 2:1 mismatch fixture of the set (four phases) between the antenna port and the calibrated power attenuator ahead of the tinySA Ultra; readings corrected by the NanoVNA-measured S21 of the fixture and the attenuator at each emission frequency; 5 W step; bench supply through the pack-resistance fixture; transmitter keyed with continuous dits at 25 WPM from the keying fixture holding the paddle dit contact in Iambic A for 10 s per activation (104 dits, below the 128-element and 30 s limits of the paddle watchdog, HZ-004 K4, proposed) with at least 10 s between activations; the bench test-mode generator is not used because every bench test mode forces the 0.5 W step (HZ-004 K13); max-hold over the keyed dits; spurious means any discrete signal outside the carrier +/-10 kHz; noise floor referred to the antenna port at least 10 dB below -16.02 dBm. Limit: 25 uW, 47 CFR 97.307(e) (corpus: 47cfr-97.307.md, eCFR issue 2026-09-23). Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-012 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): the fixture keys the paddle input for the scans; step 5 repeats the 2f and 3f readings with the owner's straight key and paddle at one phase. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the S21 of each mismatch fixture and of the attenuator and cable on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz, and the SWR each fixture presents at 144, 146 and 148 MHz; run the tinySA internal calibration-output check; record all.
2. With the phase-1 fixture at 146.00 MHz and 7.4 V, scan 9 kHz to 1.5 GHz in segments with max-hold; record 2f, 3f and 7f and every other signal more than 6 dB above the noise floor.
3. Repeat the scan at 144.05 and 147.95 MHz.
4. Repeat the three scans with the phase-2, phase-3 and phase-4 fixtures.
5. With the phase-1 fixture at 146.00 MHz re-read 2f and 3f keyed by the straight key (3 s holds) and by the owner's paddle (squeezes of at most 1.5 s at 25 WPM, below the 2 s both-contacts-closed limit of the paddle watchdog, HZ-004 K4, proposed).
6. Run tools/tinysa_scan_check.py with the fixture S21 files: it reports each emission in dBm at the antenna port.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-009 and TPM-007.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if each fixture presents an SWR between 1.9:1 and 2.1:1 at 144, 146 and 148 MHz and every spurious emission at the antenna port, corrected for the fixture and attenuator S21 and increased by the tinySA level accuracy of its TV record, is at most -16.02 dBm (25 uW) at every phase and carrier frequency; otherwise Fail. A fixture outside 1.9:1 to 2.1:1 is a Procedure-correction NCR; straight-key and paddle readings within 1 dB of the fixture readings confirm the keying source does not change the result.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- SWR 2:1 mismatch fixture set at four phases, each characterized on the NanoVNA from 9 kHz (or the NanoVNA lower limit) to 1.5 GHz (docs/vv/fixtures/mismatch-set.md, planned)
- Keying fixture: optocoupler contacts across the key-jack tip and ring, driven by a Pico 2 running the scripted closure pattern of the step, pattern timing from its crystal (docs/vv/fixtures/keying-fixture.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `spurious-mismatch.csv` (csv): Phase, carrier frequency, emission frequency, corrected level in dBm
- `mismatch-fixtures.s2p` (other): S21 and SWR of each fixture and of the attenuator
- `spurious-mismatch-traces.png` (plot): tinySA traces per phase and frequency
- `spurious-mismatch-setup.jpg` (photo): Photograph of the setup

### TC-TX-013: Synthesizer frequency sample below 20 MHz whose frequency times the fixed ratio is within 1 kHz of the carrier

| Field | Value |
|---|---|
| Requirements | REQ-TX-013 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | none (manual) |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: antenna port to the calibrated power attenuator and the tinySA Ultra, carrier marker at 1 kHz resolution bandwidth or narrower; the firmware count of the synthesizer sample read from the UART telemetry pad through the USB-UART breakout; the division ratio R read by Inspection of the transmitter schematic at the CDR baseline (the prescaler part and its configuration pins) and recorded; 0.5 W step; straight-key holds of 3 s. The tinySA frequency uncertainty at 148 MHz stated in its TV record must be 200 Hz or less (one fifth of the 1 kHz agreement window), otherwise the case is Blocked with the borrowed-instrument alternative of docs/process/04-verification-and-validation.md section 6.3 named. A count that agrees with the carrier shows that the sample drives the 3.3 V RP2350 counting input as a valid logic signal. Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-013 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-008 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): straight key for every reading, plus one paddle reading at 146.000 MHz. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Read the division ratio R from the schematic at the CDR baseline and record the sheet and part.
3. Command 144.001 MHz, close the straight key for 3 s, read the tinySA marker and the telemetry count during the key-down.
4. Repeat at 146.000 and 147.999 MHz.
5. At 146.000 MHz hold the paddle dit lever in Iambic A at 15 WPM for 3 s and read the marker and the count.
6. Compute for each reading the count times R, its difference from the marker, and the marker divided by R.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at 144.001, 146.000 and 147.999 MHz the telemetry count multiplied by R agrees with the tinySA carrier marker within 1 kHz, and the carrier divided by R is below 20 MHz at 147.999 MHz; otherwise Fail.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- USB-UART breakout on the UART test pads (docs/vv/fixtures/usb-breakout.md, planned)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `synth-sample.csv` (csv): Commanded frequency, marker frequency, telemetry count, R, count times R, difference, marker over R
- `synth-sample-telemetry.txt` (serial_output): Raw UART telemetry of each key-down
- `synth-sample-setup.jpg` (photo): Photograph of the setup

### TC-TX-014: Antenna-port carrier at most 1 uW with TX_KEY deasserted, PA_EN asserted and the exciter driven (fault-injection build)

| Field | Value |
|---|---|
| Requirements | REQ-TX-014 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001, enclosure lid off for test-point access, running the fault-injection test build of release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (a build flavour of the release commit whose injection commands arrive over USB serial or the UART test pads and which toggles the injection-marker test pad at the instant of each injection; the same flavour TC-SYS-005 uses); the release image is restored and checked with picotool verify at the end of the case. Configuration: an injection command that holds PA_EN asserted and TX_KEY deasserted with the exciter running on the commanded frequency, for 10 s per activation; antenna port to the calibrated power attenuator and the tinySA Ultra at the commanded frequency, resolution bandwidth 1 kHz or narrower, span 100 kHz, max-hold; logic capture on PA_EN, TX_KEY and the injection-marker pad confirms the two levels; 5 W step selected; readings corrected by the attenuator S21 of this session; the noise floor referred to the antenna port is at least 10 dB below -30.0 dBm (1 uW). Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-014 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-004 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): the requirement concerns the key-up state, forced by the injection command; the reference key-down of step 4 uses the straight key, and both key types key the transmitter in TC-TX-002, TC-TX-004, TC-TX-007 and TC-TX-015. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Flash the fault-injection build with picotool load, check it with picotool verify and record its SHA-256.
3. Run the logic-capture reference pulse-train check of this session and record the result (docs/process/04-verification-and-validation.md section 4).
4. At 146.000 MHz and the 5 W step close the straight key for 3 s and read the carrier level (confirms that the setup reads the carrier).
5. Issue the injection command at 146.000 MHz; during the 10 s activation read the max-hold level at the commanded frequency and confirm on the capture that PA_EN stayed high and TX_KEY low.
6. Repeat the previous step at 144.001 and 147.999 MHz.
7. Set the supply to 8.4 V and repeat the three activations.
8. Restore the release image with picotool load and confirm that picotool verify matches the VDD SHA-256.
9. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
10. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if, at 144.001, 146.000 and 147.999 MHz and at 7.4 and 8.4 V supply, with PA_EN high and TX_KEY low throughout each activation on the capture, the carrier power at the antenna port, corrected for the attenuator S21 and increased by the tinySA level accuracy of its TV record, is at most -30.0 dBm (1 uW); otherwise Fail. An activation in which TX_KEY rises or PA_EN falls is a Procedure-correction NCR against the fault-injection build, not a requirement result.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Pico-based logic capture (second Pico 2 with sigrok-pico firmware read by sigrok-cli; planned, ADR-009), 3.3 V inputs, 1 MS/s unless a step states otherwise; credit-bearing after its TV record docs/cm/tool-validation/TV-NNN-logic-capture.md
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)
- USB-UART breakout on the UART test pads (docs/vv/fixtures/usb-breakout.md, planned)

**Expected artifacts.**

- `tx-key-isolation.csv` (csv): Frequency, supply, carrier level at the tinySA, corrected antenna-port level, noise floor
- `tx-key-isolation.sr` (other): Logic capture of PA_EN, TX_KEY and the injection marker for every activation
- `tx-key-isolation-traces.png` (plot): tinySA max-hold traces per activation
- `tx-key-isolation-setup.jpg` (photo): Photograph of the setup

### TC-TX-015: Output power at most 6.3 W into 50 ohm at every step, carrier frequency and 6.4, 7.4 and 8.4 V supply

| Field | Value |
|---|---|
| Requirements | REQ-TX-015 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/rf_probe_power.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: bench supply through the pack-resistance fixture into the battery terminals; dummy load with the diode RF probe on its T; multimeter on the probe output, P = Vpk^2 / 100 with the probe characterization of TC-SYS-010 (docs/process/04-verification-and-validation.md section 6.2); for the secondary reading the dummy load is replaced by the calibrated power attenuator and the tinySA Ultra; key-downs of 3 s with at least 10 s between them. The ceiling feeds the RF Exposure Evaluation docs/design/analysis/rf-exposure-evaluation.md (HZ-001). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-015 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: HZ-001, HZ-006 (from the cited requirements; docs/safety/hazards.json). Key types (SI-018; 04 section 8.2): straight key for every reading, plus one paddle reading at the 5 W step. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Confirm that TC-SYS-010 is Passed and copy its power uncertainty into the report.
2. Set the supply to 6.4 V at the battery terminals under load.
3. At 144.05 MHz close the straight key for 3 s at each of the 0.5, 1, 2 and 5 W steps and read the probe output.
4. Repeat the previous step at 146.00 and 147.95 MHz.
5. Repeat the two previous steps at 7.4 V and at 8.4 V.
6. At 8.4 V and the 5 W step repeat the reading at 144.001 and 147.999 MHz.
7. At 146.00 MHz, 8.4 V and the 5 W step hold the paddle dah lever at 15 WPM for 3 s and read the probe.
8. Replace the dummy load by the attenuator and tinySA; at 146.00 MHz and 8.4 V read the carrier power at the 5 W step (secondary reading).
9. Run tools/rf_probe_power.py on the readings to compute each power with its uncertainty band.
10. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report, and the measured values for MOP-004, TPM-015 and MOP-018.
11. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at every step, carrier frequency and supply voltage the upper end of the probe power's characterized uncertainty band is at most 6.3 W; otherwise Fail. A probe and tinySA disagreement beyond their combined uncertainty is a Procedure-correction NCR (docs/process/04-verification-and-validation.md section 6.2), not a requirement result.

**Instruments and fixtures.**

- Diode RF probe (1N5711 or equivalent, printed housing) on a BNC T at the dummy load, characterized by TC-SYS-010, read on the multimeter DC voltage range (docs/vv/fixtures/rf-probe.md, planned)
- Multimeter, DC voltage and DC current ranges, accuracy per datasheet copied into the report (OQ-VV-003)
- Adjustable bench supply, 0 to 30 V, current limit set per step
- Pack-resistance fixture: series resistor equal to the datasheet internal resistance of two cells plus two holders, in the bench-supply lead (docs/vv/fixtures/pack-resistance.md, planned)
- 50 ohm BNC dummy load with SMA adapter, power rating recorded in the report
- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Owner's straight key and iambic paddle, 3.5 mm TRS plugs (SI-034)

**Expected artifacts.**

- `power-ceiling.csv` (csv): Frequency, supply, step, keying source, probe reading, power and uncertainty band
- `power-ceiling-secondary.csv` (csv): tinySA secondary reading with attenuator correction
- `power-ceiling-setup.jpg` (photo): Photograph of the setup

### TC-TX-016: Antenna-port power at the set carrier frequency at most -57 dBm in Receive mode

| Field | Value |
|---|---|
| Requirements | REQ-TX-016 |
| Method / class | Test / Bench |
| Credit row | T-HW |
| Status | Draft |
| Automation | `tools/tinysa_scan_check.py` |

**Setup.** Article: CWHT-A-001 in its enclosure, firmware at the released version release/FW-vX.Y.Z named in firmware/releases/VDD-vX.Y.Z.md (recorded as vX.Y.Z+<short SHA> in the report). Configuration: Receive mode, no key connected (transmit impossible without a key closure); antenna port to the calibrated attenuator and the tinySA Ultra, the attenuator retained to protect the analyzer against an unintended transmission; marker at the set frequency with a resolution bandwidth of 1 kHz or narrower in a 20 kHz span; readings corrected by the attenuator S21 of this session; the noise floor referred to the antenna port at least 6 dB below -57.0 dBm (reduce the resolution bandwidth until it is); bench supply at 7.4 V. Blocked until OQ-VV-001 closes and the tinySA TV record docs/cm/tool-validation/TV-NNN-tinysa.md exists (docs/process/04-verification-and-validation.md sections 6 and 6.3). Credit row: T-HW. Test of a transmitter (module TX) requirement closed by Bench on the delivered unit (docs/process/04-verification-and-validation.md section 5.2), run after the TRR that opens the emission campaign (section 13) and witnessed by the owner; the pre-build Simulation evidence named in the requirement's verification_note is supporting only and is not part of this case. Part 97 gate: this case verifies a regulatory REQ-TX requirement; its Passed report with credit true is one of those the OnAir authorization of docs/reviews/TRR-Dn/decision-memo.md names before the first antenna-connected transmission (docs/process/04-verification-and-validation.md section 6.3). TBR values: the acceptance criteria use the values of REQ-TX-016 as written, including those marked TBR (close by PDR); a change at PDR returns this case to Draft (docs/process/04-verification-and-validation.md section 8.2, SWE-071). Hazard controls exercised: none (REQ-TX-016 traces to no hazard). Key types (SI-018; 04 section 8.2): not applicable; the case is run in Receive mode without keying. Credentials: instruments and tools per tools/toolchain.lock.md at the commit recorded in the report. Safety: every transmission goes into the 50 ohm dummy load or the calibrated power attenuator, connected before power-on, never into an open antenna port; key-down duty kept within the load rating recorded in the report; anyone other than the operator stays 0.6 m or more from the unit and load while keying and 1.0 m or more during a tune carrier (NGO-019); the bench supply current limit is set before each power-on; antistatic wrist strap while the lid is off; the PA area is not touched after key-down runs; the stuck-key abort of the operations handbook (HZ-004 K11: unplug the key, then switch the PA supply off) is ready at every keyed step. Environment: room temperature 18 to 28 C; the pack is supplied by the bench supply at 7.4 V +/-0.05 V through the battery terminals unless a step sets another value; dummy load or calibrated attenuator on the antenna port.

**Procedure.**

1. Measure the attenuator and cable S21 on the NanoVNA over the frequencies the case reads (9 kHz, or the NanoVNA lower limit, to 1.5 GHz for a scan) and save the Touchstone file; run the tinySA Ultra internal calibration-output check; record both.
2. Power the unit on in Receive mode with no key connected and the volume at its default; tune to 144.05 MHz and wait 30 s.
3. Read the max-hold level over 20 s at the set frequency and the highest level within +/-10 kHz of it.
4. Repeat at 146.00 and 147.95 MHz.
5. Repeat the three readings with the volume at maximum (the second receive state).
6. Run tools/tinysa_scan_check.py to correct the readings for the attenuator S21.
7. Record instrument calibration state, instrument and capture firmware versions, tool versions and the firmware version in the report.
8. On any discrepancy, stop and open an NCR per docs/process/04-verification-and-validation.md section 10.

**Acceptance criteria.** Pass if at 144.05, 146.00 and 147.95 MHz, at the default and at the maximum volume, the level at the set frequency, corrected for the attenuator S21 and increased by the tinySA level accuracy of its TV record, is at most -57.0 dBm; otherwise Fail. The highest level within +/-10 kHz is recorded as data.

**Instruments and fixtures.**

- tinySA Ultra spectrum analyzer (ADR-021) through the calibrated 30 to 40 dB attenuator rated 10 W or more, attenuator S21 measured on the NanoVNA in the same session; level and frequency accuracy per its TV record docs/cm/tool-validation/TV-NNN-tinysa.md
- NanoVNA, SOLT calibration with a through at the two cable ends used, checked on the dummy load and on the through; S21 uncertainty and isolation floor per its TV record
- Adjustable bench supply, 0 to 30 V, current limit set per step

**Expected artifacts.**

- `rx-leakage.csv` (csv): Set frequency, receive state, corrected level at the set frequency, highest level within 10 kHz, noise floor
- `rx-leakage-traces.png` (plot): tinySA traces per frequency and state
- `rx-leakage-setup.jpg` (photo): Photograph of the setup with no key connected
