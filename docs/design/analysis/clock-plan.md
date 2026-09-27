# Clock plan: harmonic map of every clock against the 2 m band, the IF, the image and the LO

| Field | Value |
|---|---|
| Product | `docs/design/analysis/clock-plan.md` (analysis note, `analysis_kind`: other, frequency plan) |
| Work package | WP-PDR-20 (`docs/plan/pdr-work-plan.md` section 3.6), wave 1a |
| Author | Claude, RF designer (TX) author invocation, 2026-09-27 |
| Checker | `hardware/sim/freq/clock_plan.py` |
| Figure | `docs/reviews/PDR/figures/clock-plan-harmonics.png` (rendered and inspected, section 7) |
| Decision record | ADR-031 (Proposed), `docs/decisions/adr/ADR-031-clock-plan.md`: the rules of section 3 |
| Review record | `docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md` (shared with `frequency-budget.md`, plan section 3.6) |
| Evidence status | **Developer evidence** (05 section 9.1; checker without a TV record; CK-ANA-C2) |
| AT RISK | No dependence on CR-003 or CR-006. Several rules depend on choices other WPs make: the IF and injection side (WP-PDR-19), the buck part (WP-PDR-24), the display and audio (WP-PDR-25). Each dependency is named where it applies |

## 1. Question and scope

The question: which clocks of the cwht design produce a harmonic line that the receiver can hear? The bands checked are:
- the 2 m band 144.000 to 148.000 MHz;
- the CW-only segment 144.0 to 144.1 MHz (47 CFR 97.305(a), (c); corpus `47cfr-97.305.md` lines 17, 58), of which the receive range of REQ-SYS-034 starts at 144.010 MHz;
- the IF window;
- the image band;
- the band the RX LO covers, where a clock line acts as a spurious LO.

The note then sets the rules and frequencies that keep the band clear where that is possible (HZ-008 K6; RSK-040 step S1).

It serves:
- REQ-SYS-034 (TBR: 3 dB above MDS; range 144.010 to 147.999 MHz);
- HZ-008 K6 (`docs/safety/hazards.json` 0.5.0-pha);
- RSK-040 step S1;
- ADR-023 item (5);
- the TS-001 sub-choices of IF (9.000, 9.0106 or 10.7 MHz) and injection side, which WP-PDR-19 decides.

A clock "line" is the interval n x f x (1 +/- tolerance). The tolerance is 65 ppm for XOSC-derived clocks (RP2350 datasheet Table 596: 30 + 30 + 5 ppm) and 2.5 ppm for TCXO-derived clocks (REQ-SYS-010).

**Clock classes.**
- **Clear class**: clocks of 4 MHz or more. Spacing between lines is at least the 4 MHz band width, so a frequency can be chosen with no line in the band.
- **Dense class**: clocks below 4 MHz. They always have lines in the band. Where they fall can be placed; their level is a layout matter (CDR).
- **Residual source** (revision 1): a switching or clock source whose frequency cannot be placed in operation, because it is free-running and can be neither synchronised nor switched off, or because the board sets its period. Its lines are named residual lines (section 2.1); only their level can be controlled.

## 2. Clock inventory and results (checker table "clocks")

| Clock | Class | Status | Lines in 144 to 148 MHz | Lines in 144.010 to 144.100 MHz | Source |
|---|---|---|---|---|---|
| XOSC 12 MHz (clk_ref) | clear | fixed | n = 12: 143.9906 to 144.0094 (coherent) | none | Pico 2 crystal; RP2350 Table 596 |
| clk_usb and clk_adc 48 MHz (PLL_USB) | clear | fixed | n = 3: 143.9906 to 144.0094 (coherent, the same line) | none | RP2350 section 8.1 clock table: clk_adc "Must be 48MHz" |
| clk_sys = clk_peri 150 MHz | clear | fixed | none (150 MHz is 2 MHz above the band) | none | 07 WP-SW-11 |
| TCXO 25.000 MHz | clear | proposed | none | none | TS-007 R-M4 |
| TCXO 26.000 and 27.000 MHz | clear | rejected (section 4) | none | none | F21, F16 |
| Prescaler output, divide by 8 (TX only) | clear | tx-only | n = 8 is the carrier itself | (TX only) | `frequency-budget.md` section 3.3 |
| SPI SCK 150 MHz / d, d = 2 to 24 even | clear | allowed (clear set) | none | none | RP2350 section 12.3 (CPSDVSR even, SCR) |
| SPI SCK 150 / 8 = 18.75 MHz | clear | proposed (LMX2571 SPI) | none | none | this plan |
| SPI SCK 150 / 26 = 5.769 MHz; 150 / 30 = 5 MHz; every d from 26 to 48 | clear | rejected | one line each (for example 144.2214 to 144.2401 MHz for d = 26) | none | checker table "SPI clear set" |
| Audio and sidetone PWM 150 kHz (TOP + 1 = 1000) | dense | proposed | 27 coherent lines, 144.000 + j x 0.15 MHz | none | RP2350 section 12.5; audio research F1 |
| Audio PWM 146.484 kHz (TOP + 1 = 1024) | dense | rejected | 28 lines, one at 144.1313 to 144.1500 and one at 143.9848 to 144.0035 | none, but not coherent | audio research F1 |
| 5 V buck synchronised at 2.4 MHz (12 MHz / 5) | dense | proposed | 144.000 (coherent) and 146.3905 to 146.4095 | none | HZ-008 K6 ("5 V buck synchronised to a firmware-set frequency"); part from WP-PDR-24 |
| 5 V buck free-running 2.2 MHz +/-10 % | dense | rejected | sweeps the band | **sweeps the segment** | power research F19 |
| Charger boost 1.5 MHz +/-10 % | dense | off in operation | sweeps the band | sweeps the segment | power research F20. Charging is paused while the radio is on (REQ-SYS-093, HZ-011 K2), so the boost does not run while receiving |
| PCM1808 SCKI 12.288 MHz (TS-001 option B, 256 fs at 48 kS/s) | clear | rejected | n = 12: 147.4486 to 147.4634 | none | cw-selectivity F12 |
| PCM1808 SCKI 12.5 MHz (150 MHz / 12, fs 48.83 kS/s) | clear | option (only if TS-001 keeps B) | none | none | this plan |
| BFO (Si5351A, IF +/- 1 kHz) | clear | by design, IF-dependent | section 4 | section 4 | TS-001 option A product detector |
| QSPI flash SCK 150 MHz / CLKDIV, CLKDIV 1 to 24 (odd and even) | clear | allowed (clear set, checker table "QSPI SCK clear set") | none | none | RP2350 section 12.14.3 ("Odd and even divisors are supported"); M0_TIMING.CLKDIV, Table 1296 |
| QSPI SCK 150 / 4 = 37.5 MHz (M0_TIMING reset value) | clear | proposed; runs whenever code executes in place from flash | none (n = 4 at 150.0 MHz) | none | Table 1296, reset 0x04 |
| QSPI SCK 150 / 12 = 12.5 MHz | clear | boot and flash program or erase only | none | none | RP2350 section 5.4.8.6 (`flash_enter_cmd_xip`: "CLKDIV is set to 12") |
| RP2350 core voltage regulator, VREG_LX, 3 MHz typ | dense | **residual R-1** | lines anywhere: typical value only | can fall in the segment (section 2.1) | RP2350 sections 6.3.1.1, 6.3.2; section 14.9.6 Table 1441 |
| Pico 2 RT6150 buck-boost, PFM or PWM | dense | **residual R-2** | frequency not in the corpus | cannot be excluded | Pico 2 datasheet section 5.4; power research F18 |
| TPA6130A2 charge pump 300 to 500 kHz (min, typ 400, max) | dense | **residual R-3** (while the amplifier is enabled) | 206 harmonic intervals | 192 harmonic intervals | display research F15 |
| I2C SCL 357.1 to 396.8 kHz (375 ic_clk plus a 20 to 300 ns rise time) | dense, non-coherent | **residual R-4** (only during bus transactions) | 52 harmonic intervals | 41 harmonic intervals | RP2350 sections 12.2.1.2, 12.2.14 (Figure 89) |

**Results of the rules (checker "RESULT"): 0 rule failures in the proposed plan, and 4 named residual sources.** The only clear-class line in the REQ-SYS-034 range is the coherent 144.000 MHz line of the XOSC and the 48 MHz clocks. It lies within +/-9.36 kHz of 144.000 MHz and is excluded by the 144.010 MHz lower limit, with 0.64 kHz to spare. The rules hold for every source that can be placed. They cannot hold for the four residual sources of section 2.1, whose lines can fall anywhere in 144.010 to 147.999 MHz, the CW-only segment included. Revision 0 omitted them and so did not establish its "0 rule failures" result (INSP-056 finding-3, finding-4).

### 2.1 Named residual sources (revision 1)

| Id | Source | Frequency and its basis | Why it cannot be placed | What controls it | Open item |
|---|---|---|---|---|---|
| R-1 | RP2350 on-chip core voltage regulator (switched-mode output VREG_LX to an external inductor on the Pico 2 module) | fsw typ 3 MHz, with no minimum or maximum (section 14.9.6, Table 1441) | It runs in switching mode whenever the core runs: "In Normal mode, the regulator operates in a switching mode" (section 6.3.1.1), and low-power linear mode cannot be selected by software while software runs (section 6.3.2). Section 6.3 describes no synchronisation input. A deviation of only 69.4 ppm from 3.000 MHz puts its 48th harmonic in 144.010 to 144.100 MHz (checker), far less than any free-running oscillator holds | Level only: the module is shielded and partitioned from the RX front end (RSK-040 step S3); the REQ-SYS-034 Test measures it | VOI-CP-1: the fsw tolerance and drift of the RP2350 regulator (not in the corpus) |
| R-2 | Pico 2 RT6150 buck-boost (VSYS to 3.3 V for the RP2350 and its IO) | Not in the corpus. The Pico 2 datasheet (section 5.4) states the modes only: PFM by default ("only turning on the switching MOSFETs occasionally"), PWM when GPIO23 drives the PS pin high ("forces the SMPS to switch continuously"), and PWM under heavy load "irrespective of the PS pin state" | It is on the module and free-running. The module brings out only its PS pin (GPIO23) and its EN pin (3V3_EN) (Pico 2 datasheet sections 3.1 and 5.4), so there is no synchronisation input, and switching it off de-powers the RP2350. In PFM its burst rate follows the load, so its lines move with the firmware's activity | Proposed setting: GPIO23 high (PWM) while the receiver is on, so that the lines form one fixed comb that the bench scan can list, instead of a load-dependent burst spectrum. The light-load efficiency cost goes to the WP-PDR-24 and WP-PDR-29 battery budget; if it breaks TPM-008, PFM is kept and the residual is listed as a moving comb. Level: shielding and partitioning (RSK-040 step S3); the receiver 3.3 V never comes from the module 3V3 pin (power research F20) | VOI-CP-2: the RT6150 switching frequency and its tolerance in PWM (RT6150 datasheet, not in the corpus) |
| R-3 | TPA6130A2 headphone amplifier charge pump | 300 to 500 kHz (min, typ 400, max) (display research F15) | Free-running, no synchronisation. It runs whenever the amplifier is enabled, which is every receive state with headphones inserted | The WP-PDR-25 amplifier choice (display research D-UI-05): a capacitor-coupled amplifier has no charge pump and removes R-3. If the TPA6130A2 is kept: LC filtering of its supply, layout (RSK-040 steps S2, S3) and the REQ-SYS-034 Test with the amplifier enabled | WP-PDR-25 decision |
| R-4 | I2C SCL (RP2350 I2C master) | Period = (HCNT + IC_FS_SPKLEN + 7 + LCNT + 1) ic_clk + SCL rise time, because "SCL_High_time = [(HCNT + IC_*_SPKLEN + 7) * ic_clk] + SCL_Fall_time" and "SCL_low_time = [(LCNT + 1) * ic_clk] - SCL_Fall_time + SCL_Rise_time" (section 12.2.14, Figure 89); ic_clk is clk_sys, 150 MHz (section 12.2.1.2). With the proposed counts HCNT 160, LCNT 199, SPKLEN 8 (375 ic_clk, 2.500 us) and a rise time of 20 to 300 ns (allocation; 300 ns is the Fast-mode ceiling of the I2C-bus specification, not in the corpus), SCL is 357.1 to 396.8 kHz | The rise time depends on the pull-ups and bus capacitance, "beyond the control of the DW_apb_i2c" (section 12.2.14 note), so SCL is not coherent with 144.000 MHz (144 MHz / SCL = 362.9 to 403.2) and varies from unit to unit. Over the rise-time range, 41 harmonic intervals meet the CW-only segment (checker). Lines exist only while a transaction runs | Traffic rule in receive (allocation to WP-PDR-32 and WP-PDR-35): I2C transactions only on events (BFO write on a mode or IF change, volume step, charger or protector reads that the WP-PDR-32 architecture shows are needed while the radio is on), no periodic poll faster than once a second, each transaction at most 1 ms, so the bus is idle at least 99.9 % of receive time. The REQ-SYS-034 Test runs with bus traffic generated | With TS-007 A2 (recommended), no tuning traffic uses I2C. With A1, every tuning step would be an I2C write in receive and R-4 would occur on every step |

The residual sources also put lines into every image and LO band of section 4. They form the "expected birdies" part of HZ-008 K6 that frequency placement cannot remove.

## 3. Rules (proposed for ADR-031)

1. **Clear-class clocks** (4 MHz or more) have no line in 144.010 to 147.999 MHz. A clock derived from the XOSC with 144 MHz / f an integer ("coherent") may put a line only on 144.000 MHz, inside the REQ-SYS-034 exclusion.
2. **No line of any placeable clock running in operation falls in the CW-only receive segment 144.010 to 144.100 MHz.** The four residual sources of section 2.1 (R-1 to R-4) cannot meet this rule. They are named residual lines, held to the REQ-SYS-034 allowance by level (rule 10).
3. **Dense-class clocks** (below 4 MHz) are derived from the XOSC (directly, or through PLL_SYS, which is XOSC x 12.5) and are coherent with 144.000 MHz (144 MHz / f an integer). Their lines then fall on 144.000 MHz and on 144.000 + j x f, which is at or above 144.100 MHz when f is at least 100 kHz. For clocks from clk_sys = 150 MHz this means a divisor that is a multiple of 25 (144 x d / 150 = 24 d / 25). I2C SCL cannot meet this rule, because its period includes the board rise time (rule 4, residual R-4). The level of their lines is a CDR layout item (RSK-040 steps S2, S3) and a TRR bench-scan item (step S4, the REQ-SYS-034 Test).
4. **Serial clocks**: SPI SCK is taken from the clear set 150 MHz / d, d even from 2 to 24 (75, 37.5, 25, 18.75, 15, 12.5, 10.71, 9.375, 8.33, 7.5, 6.82, 6.25 MHz), or from the coherent dense set (d a multiple of 50, for example 3, 1.5 or 1 MHz, for a slow display bus). An SPI device written while receiving (the synthesizer while tuning) uses a clear-set SCK with no line in the LO band of the chosen IF plan: 18.75 MHz is clear for every low-side plan. 12.5 MHz (11th harmonic at 137.5 MHz) and 15 MHz (9th at 135.0 MHz) are not clear for the IF-9 low-side plans. The QSPI flash SCK is clk_sys / CLKDIV with CLKDIV from 1 to 24, all clear; the proposal keeps the reset value 4 (37.5 MHz), and WP-PDR-32 confirms it against the flash part's ceiling. I2C SCL is not a placeable clock: its period is (HCNT + SPKLEN + LCNT + 8) ic_clk plus the rise time (RP2350 section 12.2.14). The proposed counts are HCNT 160, LCNT 199 and SPKLEN 8 (375 ic_clk), giving 357.1 to 396.8 kHz over a 20 to 300 ns rise time, and I2C traffic in receive follows the section 2.1 R-4 rule.
5. **USB and ADC clocks**: clk_usb runs only while USB is enumerated. clk_adc (48 MHz) runs whenever the ADC samples. Both put their line on the same 144.000 MHz line as the XOSC 12th harmonic. They add level there, not a new line. This refines ADR-023 item (5), whose text says no USB clock harmonic falls in the band.
6. **Switchers**: a switcher that can be synchronised or switched off is placed. The 5 V buck is synchronised to 12 MHz / 5 = 2.4 MHz if the WP-PDR-24 part has a SYNC input, and the charger boost does not run while the radio is on (REQ-SYS-093). A free-running switcher that can be synchronised or switched off is not admitted while receiving, because its lines sweep the CW segment. Three switchers can be neither synchronised nor switched off in operation: the RP2350 core regulator (R-1), the Pico 2 RT6150 (R-2) and, if WP-PDR-25 keeps it, the TPA6130A2 charge pump (R-3). They are named residual lines (rule 10), with GPIO23 driven high (RT6150 in PWM) while the receiver is on, subject to the WP-PDR-24 battery budget.
7. **TCXO**: 25.000 MHz.
8. **Prescaler**: divide by 8 on the TX path only (ratio 16 would put the sample on 9.000 MHz).
9. **IF-dependent constraints** (inputs to WP-PDR-19, section 4): low-side injection. BFO harmonics kept out of the band by the IF and BFO-side choice. With IF 9.000 MHz, dense clocks from clk_sys use divisors of 25 x an odd number, so that no line lands on 9.000 MHz.
10. **Named residual lines** (revision 1): the residual sources of section 2.1 are listed in the HZ-008 K6 expected-birdie list with their frequency basis. Their lines are held to the REQ-SYS-034 allowance by level (layout, supply filtering and shielding, RSK-040 steps S2 and S3), not by frequency, and the REQ-SYS-034 Test runs with each of them active.

## 4. IF plans (checker table "IF plans"; the IF and injection side are WP-PDR-19's decision)

| IF plan | Image band | LO band | Si5351A LO in its VCO range (F16: VCO 600 to 900 MHz, output 200 MHz max) | BFO 16th harmonic (BFO = IF +/- 1 kHz) | Clear-class lines in IF window, image or LO band |
|---|---|---|---|---|---|
| 9.000 low | 126.000 to 130.000 | 135.000 to 139.000 | yes, divider 6 | 143.9836 to 144.0164 MHz: **into the CW segment up to 144.016 MHz** if the BFO sits above 9.000 MHz. Below the band if the BFO sits below 9.000 MHz | LO band: SPI 12.5 MHz (n = 11, 137.5 MHz), 15 MHz (n = 9, 135.0 MHz). IF window: the coherent 150 kHz audio PWM (n = 60, 9.000 MHz) unless rule 9 applies |
| 9.000 high | 162 to 166 | 153 to 157 | no with divider 6; divider 4 needed | as above | LO band: XOSC n = 13 at 156.000 MHz. Image: SPI 12.5 and 15 MHz |
| 9.0106 low | 125.979 to 129.979 | 134.989 to 138.989 | yes, divider 6 | **144.1532 to 144.1860 MHz, in the band** (weak-signal area above the CW segment) | LO band: SPI 12.5 and 15 MHz |
| 9.0106 high | 162.021 to 166.021 | 153.011 to 157.011 | no, divider 4 needed | 144.1532 to 144.1860 MHz, in the band | LO band: XOSC n = 13 at 156.000 MHz |
| 10.7 low | 122.600 to 126.600 | 133.300 to 137.300 | yes, divider 6 | **none in the band** (13th at 139.1, 14th at 149.8 MHz) | Image: TCXO 25 MHz n = 5 at 125.000 MHz (image of 146.400 MHz); SPI 25 and 12.5 MHz at 125.0 MHz. LO band: SPI 15 MHz (n = 9, 135.0 MHz) |
| 10.7 high | 165.4 to 169.4 | 154.7 to 158.7 | no, divider 4 needed | none | XOSC n = 13 at 156.000 MHz (LO band), n = 14 at 168.000 MHz (image) |

The dense-class clocks put coherent lines into every image and LO band (for example 10 to 27 lines each). That is inherent in the dense class, which rule 3 covers by level. The residual sources of section 2.1 put non-coherent lines into every image and LO band as well (rule 10); the checker's IF-plan table lists placeable clocks only.

**Findings for WP-PDR-19 (inputs to the IF choice, not decisions of this note).**

1. **Low-side injection.** High-side injection places the XOSC 13th harmonic (156.000 MHz) in the LO band for every IF, and it needs the Si5351A divider 4. For TS-007 alternative A1, where the Si5351A is the LO, that falls outside the F16 recommendation. Its admissibility is Medium-confidence at best.
2. **The BFO's 16th harmonic is the strongest in-band line the plan cannot place by frequency alone.**
   - IF 9.0106 MHz (the TS-001 option A planning baseline, Inrad #111) puts it at 144.153 to 144.186 MHz.
   - IF 9.000 MHz puts it on the 144.000 MHz line, extending to 144.016 MHz if the BFO is above the IF.
   - IF 10.7 MHz has no BFO harmonic in the band.

   An ideal 50 % square wave has no even harmonics. A real Si5351A CMOS output has duty-cycle error, so the 16th harmonic exists at a level this note cannot bound without a measurement. If WP-PDR-19 keeps IF 9.0106 MHz, the BFO needs a low-pass filter at its pin and shielding, and REQ-SYS-034 carries the 144.17 MHz line as a named birdie verified by the bench scan. If it chooses 9.000 MHz, the BFO sits below the IF (BFO 8.9994 MHz gives 143.990 MHz, outside the band).
3. **IF 10.7 MHz** has the fewest conflicts. Its one clear-class hit is the TCXO 5th harmonic at 125.000 MHz in the image band, attenuated by the 70 dB image rejection of REQ-SYS-033 (TBR).

## 5. Proposed TBR values (rule C10) and requests

| Requirement | Proposed value | Support | `tbr.plan` step executed | "Else a CR" branch? |
|---|---|---|---|---|
| REQ-SYS-034 range | 144.010 to 147.999 MHz, unchanged | For the placeable clocks: the only clear-class line in 144 to 148 MHz is the coherent 144.000 MHz line, +/-9.36 kHz, 0.64 kHz inside the exclusion. No exclusion window can remove the residual lines R-1 to R-4, whose frequencies cannot be placed; they are named residual lines inside the range (section 2.1) | "the clock plan at PDR fixes the exclusion window" | No, provided WP-PDR-19 does not place a BFO harmonic between 144.000 and 144.016 MHz (IF 9.000 with the BFO above the IF). That placement would need the exclusion widened by CR, or the BFO moved |
| REQ-SYS-034 allowance | 3 dB above the MDS, unchanged, applied also to the named residual lines R-1 to R-4 | A frequency plan fixes where lines fall, not their level. No analysis available at PDR changes the proposed level. The allowance governs the dense-class lines, the BFO line and the four residual sources. For the residual sources this Analysis gives no supporting evidence at all: their compliance rests on level control (CDR layout, RSK-040 steps S2 and S3) and is shown only by the Test (bench scan, RSK-040 step S4) with each residual source active | "and the birdie allowance" | No at PDR. If the TRR scan finds a residual line above the allowance, the RSK-040 trigger applies: filtering or shielding by CR, or a CR naming that residual frequency as an exception to REQ-SYS-034 |

Requests (this note edits none of these files; plan section 5.3):
- **WP-PDR-16b (`hazards.json`).** HZ-008 K6 text: replace "USB PLL off when not enumerated" with rule 5 (clk_usb gated; clk_adc coherent on the 144.000 MHz line). Add rules 2, 3 and 10, the synchronised buck of rule 6, and the named residual lines R-1 to R-4 of section 2.1 in the expected-birdie list.
- **WP-PDR-19.** Section 4 findings 1 to 3.
- **WP-PDR-24.** Buck with a SYNC input, driven at 2.4 MHz. The charger stays off in operation. The RT6150 PS pin (GPIO23) high while the receiver is on (R-2), with its light-load efficiency cost in the battery budget, and VOI-CP-2 (RT6150 switching frequency) from the RT6150 datasheet.
- **WP-PDR-25.** Display SPI and backlight or audio PWM from rules 3 and 4. The backlight PWM is at least 100 kHz and coherent, or DC. The amplifier choice D-UI-05 decides whether residual R-3 exists: a capacitor-coupled amplifier removes it.
- **WP-PDR-32 and WP-PDR-35.** Clock configuration constants (SPI divisor 8 for the synthesizer, QSPI CLKDIV 4, I2C counts HCNT 160, LCNT 199 and SPKLEN 8, PWM TOP + 1 = 1000, or 25 x odd with IF 9.000, GPIO23 high in receive) as SW-CTL or SW-SYNTH requirements, each checked by a HostUnit test of the configuration table. The R-4 I2C traffic rule in receive (event-driven transactions, no periodic poll faster than once a second, each transaction at most 1 ms) as an SW requirement, confirmed by the WP-PDR-32 architecture.
- **TC-SYS-022 writer (plan section 5.3 order: WP-PDR-11, then WP-PDR-02, then WP-PDR-45).** The REQ-SYS-034 birdie survey runs with each residual source active: headphone amplifier enabled (R-3), I2C traffic generated (R-4), GPIO23 in its operating state (R-2), and the core running (R-1); the expected-birdie list includes R-1 to R-4.
- **WP-PDR-36a.** The clock table goes into `ICD-CTL-SW`.
- **WP-PDR-18.** RSK-040 step S1 evidence is this note and ADR-031. The residual family R-1 to R-4 has no frequency mitigation, so step S1 does not lower the likelihood for it; steps S2 to S4 carry it.

## 6. Limitations

1. The note places lines. It does not predict their level, which depends on layout, edge rates and shielding (CDR). Coupling levels are therefore not analysed. A line absent here can still exist as an intermodulation product of two clocks. The TRR bench scan (RSK-040 step S4) is the closing evidence.
2. The buck and charger frequencies are research values (power research F19, F20) until WP-PDR-24 chooses parts.
3. The Si5351A and LMX2571 internal VCO frequencies are not placed. Their outputs are divided, and the corpus holds no LMX2571 VCO range.
4. Tolerances use datasheet worst cases (XOSC 65 ppm), which is conservative for the -10 to +45 C span.
5. The checker's windows (IF +/-5 kHz) are wider than the crystal-filter passband, which is conservative.
6. Residual sources (revision 1): the RP2350 regulator tolerance (VOI-CP-1) and the RT6150 frequency (VOI-CP-2) are not in the corpus, and the I2C rise-time range of 20 to 300 ns is an allocation. None of these changes the conclusion that the four residual sources cannot be placed; they would only let the expected-birdie list name exact frequencies.
7. The QSPI SCK runs in bursts on cache misses. The gating spreads energy around its 112.5 and 150.0 MHz lines by an amount this note does not bound. It is a level item for the bench scan.

## 7. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/clock_plan.py --plot
```

Expected: "RESULT: 0 rule failure(s) in the proposed plan; 4 named residual source(s)", exit status 0 (revision 1, run 2026-09-27). The residual sources are reported in the checker table "residual sources", not as rule failures. The figure `docs/reviews/PDR/figures/clock-plan-harmonics.png` shows:
- every clock's lines from 124 to 170 MHz, coloured by status, with the residual sources in magenta (the RP2350 regulator drawn at +/-10 % for display only, and the RT6150 marked as frequency not in the corpus);
- the 2 m band, the CW-only segment, and the image and LO bands of the IF-9 low-side plan shaded;
- the harmonic order printed over each clear-class line.

The author opened and inspected it after one correction (lines of fixed clocks were too thin to see; now drawn as markers). Revision 1 re-rendered it and wrapped the title after one inspection showed its second line clipped.

## Change history

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial issue, frozen for its first review (freeze F0, rule C2) | WP-PDR-20 wave 1a |
| 1 | 2026-09-27 | Residual-source class; QSPI flash SCK, RP2350 core regulator, Pico 2 RT6150 and TPA6130A2 charge pump added to the inventory; I2C SCL re-modelled per RP2350 section 12.2.14 as a non-coherent residual source with a traffic rule; section 2.1 named residual lines R-1 to R-4; rules 2, 3, 4 and 6 restated and rule 10 added; REQ-SYS-034 proposal restated with the residual lines; requests, limitations, reproduction and figure follow | INSP-056 finding-3 and finding-4 (Major) |
