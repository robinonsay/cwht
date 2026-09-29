# Frequency budget, band-edge guard and frequency-verification counter

| Field | Value |
|---|---|
| Product | `docs/design/analysis/frequency-budget.md` (analysis note, `analysis_kind`: budget, timing, worst-case) |
| Work package | WP-PDR-20 (`docs/plan/pdr-work-plan.md` section 3.6), wave 1a; **revision 2: WP-PDR-20a** (plan revisions 6 and 7, section 3.0 row 20: the route R3 budget of D-17, the Si5351A relock time against its 1 ms allocation, the TCXO ratio freshness over a long over against its 1 ppm allocation), wave W-A |
| Author | Claude, RF designer (TX) author invocation, 2026-09-27 (revisions 0 and 1); Claude, WP-PDR-20a analysis author invocation, 2026-09-29 (revision 2); Claude, WP-PDR-20a author invocation for the Major findings, 2026-09-29 (revision 3); Claude, WP-PDR-20a author invocation for INSP-111 finding-13, 2026-09-29 (revision 4) |
| Checker | `hardware/sim/freq/freq_budget.py` (sections 3.1 to 3.3, unchanged in revisions 2 and 3) and `hardware/sim/freq/r3_a5.py` (sections 3.4 and 3.5 and the A5 rows of section 3.1; new in revision 2, run `r3a5-20260929-01`; revision 3, run `r3a5-20260929-02`; revision 4, run `r3a5-20260929-03`); one command each, section 7 |
| Figure | `docs/reviews/PDR/figures/frequency-budget.png` (sections 3.1 to 3.3); `hardware/sim/freq/results/r3a5-20260929-03/relock-sequence.png`, `ratio-freshness.png`, `xosc-slope.png`, `r3-budget-and-buffer.png`, `settle-and-guard.png` (section 3.4 and the A5 rows of section 3.1; byte-identical to the revision 3 run `r3a5-20260929-02`) and `reference-budget-a5.png` (section 3.5; revision 4). All rendered and inspected (section 7) |
| Review record | `docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md` (INSP-056; one record for this note and `clock-plan.md`, plan section 3.6), with `docs/templates/peer-review-checklist-analysis.md` (on `cr/CR-012-pdr-checklist-templates`, not yet on `main`). Revision 2 is reviewed as the WP-PDR-20a delta of INSP-056 with its software assurance pair (plan row 20: "the INSP-056 and INSP-111 deltas with the SA pair"); the lead SE assigns the iterations |
| Evidence status | **Developer evidence** (05 section 9.1). Both checkers are class B scripts without a TV record; `r3_a5.py` also imports the WP-PDR-28a thermal model (`hardware/sim/thermal/thermal_model.py`, unchanged). Under CK-ANA-C2 no value here closes a requirement or goes to the owner as a TBR value until a TV record covers the checkers or the owner rules on developer evidence (section 6, item 1) |
| Staging | The guard values depend on REQ-TX-006 (750 Hz, TBR), which WP-PDR-22 confirms. The TS-007 part choice is decided at B1a. These values are finalized after WP-PDR-22 and ruled at B2 (plan WP-PDR-20 "Depends on"; rule C10) |
| AT RISK | Revisions 0 and 1: no. **Revision 2: AT RISK (A5 CRs)** (plan rules C8 and C13): section 3.4 uses REQ-SYS-160, 161 and 180 as they stand before the S1 disposition of CR-003 revision 4, CR-006 revision 3 and CR-018; it is re-checked against the disposition before F1 |

## 1. Question and scope

This note answers six questions (five and six added by revisions 2 and 4):

1. Does the 1.2 kHz band-edge guard of REQ-SYS-008, REQ-SYS-009 and REQ-TX-002 keep the -60 dB keying-sideband point (REQ-TX-006) and the 26 dB bandwidth (REQ-SYS-015) inside 144.000 to 148.000 MHz? The check uses the +/-2.5 ppm reference of REQ-SYS-010 and the frequency-word error, at both band edges.
2. Which reference budget makes REQ-SYS-010 (+/-2.5 ppm for one year after calibration) and the band-edge guard hold even if the firmware calibration constant is wrong? What two-unit offset remains for RSK-002?
3. Can the independent frequency verification of REQ-SYS-182 and REQ-SYS-154 (HZ-008 K7) hold its 10 kHz window and 100 ms limit on the RP2350 crystal timebase? What prescaler ratio and sample does REQ-TX-013 need? How are both REQ-SYS-154 triggers ("unlocked" and "off its set frequency by over 10 kHz") detected at both moments ("on key-down" and "during transmission"), and how fast?
4. Which TBR values does this analysis propose, and which of them trigger the "else a CR" branch of their `tbr.plan`?
5. **(Revision 2, WP-PDR-20a.)** For A5, the design the owner chose (TS-012 revision 7 section 10; D-17), does route R3 still hold at the changeover and over a whole over? Three parts:
   - the Si5351A PLL A relock after the changeover writes, read from a source, against the 1 ms allocation of the TS-012 section 7.3 key-down sequence;
   - the age of the XOSC/TCXO ratio at each check, with the squaring stage off in transmission, against the 1 ppm XOSC drift allocation;
   - the receive-only TCXO squaring stage and the 150.000 MHz line.

   Both of the first two are TS-012 section 10 revisit conditions of revision 6. Section 3.4 answers them. **Revision 3** adds, for A5, the carrier's settle residual at the ramp as a named term of the band-edge guard (section 3.1, A5 rows).
6. **(Revision 4, INSP-111 finding-13.)** For A5, with the TG2520SMN on XA, does question 2 still have an answer? Section 3.5 gives the A5 reference budget. For A5 it supersedes sections 3.2 and 4 wherever they differ.

Identifiers served:
- Requirements: REQ-SYS-008, REQ-SYS-009, REQ-SYS-010, REQ-SYS-154, REQ-SYS-182, REQ-TX-002, REQ-TX-013.
- Inputs: REQ-TX-006, REQ-SYS-015, REQ-SYS-004, REQ-SYS-161.
- TPM-006 (`frequency-stability`); RSK-002 step S1; RSK-046 step S2.
- HZ-008 controls K4 and K7 (`docs/safety/hazards.json` 0.5.0-pha); SRR decisions 25 and 40.
- TS-007 criteria M3 and R-M3.
- Revision 2: TS-012 decision A5 and design items D-12 (C6), D-17 and D-18; TS-012 section 10 revisit conditions on the relock time and the ratio freshness; REQ-SYS-160, REQ-SYS-180; INSP-110 finding-25 (the squaring stage, as it bears on the refresh time).

The receiver phase-noise and reciprocal-mixing arithmetic is in TS-007 section 4 (criterion C1). The clock harmonics are in `docs/design/analysis/clock-plan.md`.

**Revision 2 and TS-007.** Sections 3.1 to 3.3 were written for the TS-007 alternatives: A1, a Si5351A with the carrier on its own PLL, and A2, the recommended LMX2571. TS-012 supersedes TS-007. A5 is neither alternative: the Si5351A of A1 is used, but its PLL A carries the receive LO and is retuned to the carrier at every changeover, as A2's synthesizer was. Section 3.4 governs for A5 wherever it differs from sections 3.3 and 4. The clk_sys 96 MHz re-run of `clock-plan.md` and the ADR-031 revision (also WP-PDR-20a) are not in this note.

## 2. Inputs

| Input | Value | Source | State |
|---|---|---|---|
| Band edges | 144.000 and 148.000 MHz | 47 CFR 97.301(a) (corpus: `47cfr-97.301.md` line 26, eCFR issue 2026-09-23) | Regulation |
| CW-only segment | 144.0 to 144.1 MHz (other emissions start at 144.1 MHz) | 47 CFR 97.305(a), (c) (corpus: `47cfr-97.305.md` lines 17, 58) | Regulation |
| Carrier limits | 144.0012 to 147.9988 MHz | REQ-SYS-008, REQ-SYS-009, REQ-TX-002 (TBR); SRR decision 25 | TBR |
| Reference ceiling | +/-2.5 ppm total, -10 to +45 C, one year after calibration | REQ-SYS-010 (TBR); ADR-023 item (1) | TBR |
| -60 dB keying-sideband offset | 750 Hz; research cases 614 and 735 Hz | REQ-TX-006 (TBR); `docs/research/regulatory-corpus-and-operators.md` F7 | TBR (WP-PDR-22) |
| 26 dB bandwidth | at most 350 Hz (175 Hz each side) | REQ-SYS-015 (TBR) | TBR |
| Frequency-word error | 5 Hz | **Allocation** of this note. Section 3.2 shows it is conservative for both TS-007 candidates | Allocation |
| TCXO temperature-stability classes | 0.1, 0.25, 0.5 ppm | `docs/research/2m-cw-transceiver-reference-designs.md` F21 (Medium) | Research |
| TCXO uncalibrated total | 1.5 ppm (initial, reflow, temperature -10 to +45 C, 1 yr aging, supply and load) | **Allocation**; it becomes the datasheet acceptance test R-M3 of TS-007 | Allocation |
| Aging, supply and load inside it | 0.5 ppm and 0.1 ppm | **Allocation** (engineering assumption for a TCXO class; the datasheet confirms at CDR) | Allocation |
| Calibration range and uncertainty | +/-0.9 ppm; 0.1 ppm | **Allocation**; calibration by zero-beat per RSK-002 step S4 | Allocation |
| CW filter half-bandwidth | 250 Hz | RSK-002 statement | Risk register |
| Agreement window, time limit | 10 kHz measured agreement, 100 ms | REQ-SYS-182 (TBR); SRR decision 40 | TBR |
| Synthesizer true-error limit | Fault-safe when "off its set frequency by over 10 kHz" (a true error, not a measured one) | REQ-SYS-154 (TBR); SRR decision 40 | TBR |
| Measured detection threshold T | 5.0 kHz | **Proposal** of this note (section 3.3, revision 1); an SW-SAFE L2 value, distinct from the 10 kHz system values | Proposal |
| Fault-injection offset | 12 kHz above or below the set frequency | REQ-SYS-154 and REQ-SYS-182 verification notes; TC-SYS-101 procedure | Verification case |
| Lock-detect sample period during transmission | at most 10 ms | **Allocation** of this note (section 3.3, revision 1), to be confirmed by the WP-PDR-32 timing analysis | Allocation |
| Lock-detect means | A2 (recommended): LMX2571 lock-detect indication, form not in the corpus (a TS-007 value-of-information item 4 question; INSP-055 finding-4 asks TS-007 to add it). A1: Si5351A loss-of-lock status read over I2C (register map AN619 not in the corpus) | TS-007 section 1 recommendation; 07 section 14.2 `SW-SYNTH` rows, items g and l | Research gap |
| RF-off time after detection | 20 ms | REQ-SYS-004 (TBR) | TBR |
| Lead-in after RX-to-TX changeover | at most 12 ms | ADR-026 section 2 (REQ-SYS-161, TBR) | TBR |
| Retune time at changeover | A1 0 ms (TX on its own Si5351A PLL); A2 below 1.5 ms (LMX2571 FastLock) | TS-007 section 3.2; F20 (High) | Research |
| Software latency of the changeover check; service period during transmit | 2 ms; 10 ms | **Allocations**, to be confirmed by the WP-PDR-32 timing analysis | Allocation |
| Prescaler ratio | 8 | **Proposal** of this note (section 3.3) | Proposal |
| Sample ceiling | below 20 MHz | REQ-TX-013 (TBR) | TBR |
| GPIN input limit | 50 MHz | RP2350 datasheet section 8.1.1.4 ("GPIN0-GPIN1 ... is limited to 50MHz"); datasheet extract `docs/extracted/rp2350-datasheet.md` at rustos commit `2ec64c0f` (read with `git show`, never from the working tree) | Datasheet |
| FC0 test interval and accuracy | interval 12: 4 ms, 500 Hz; 13: 8 ms, 250 Hz; 14: 16 ms, 125 Hz; 15: 32 ms, 62.5 Hz | RP2350 datasheet section 8.1.3, Table 541. FC0_INTERVAL (Table 582) says "0.98us * 2**interval". Sections 3.1 to 3.3 use the rounded Table 541 times (INSP-056 finding-5, a lien). **Revision 3, section 3.4:** the count lasts 2^n x 1 us, the upper value of the 0.98 us tick, so conservative for time: 4.096, 8.192 and 32.768 ms (INSP-056 finding-12) | Datasheet |
| FC0 sources and status | GPIN0, GPIN1 selectable; DONE, PASS, FAST, SLOW, DIED, FAIL status | RP2350 datasheet Tables 583, 584 | Datasheet |
| RP2350 crystal (XOSC) | 12.000 MHz; +/-30 ppm tolerance, +/-30 ppm stability, +/-5 ppm first-year aging | RP2350 datasheet section 8.2.1.1, Table 596 (ABM8-272-T3) | Datasheet |
| TCXO frequency | 25.000 MHz | TS-007 section 8 (R-M4); `clock-plan.md` section 4 | Proposal |
| **Revision 2 inputs (section 3.4)** | | | |
| Si5351A timing | TRDY power-up time, "From VDD = VDDmin to valid output clock, CL = 5 pF, fCLKn > 1 MHz": typ 2 ms, max 10 ms. TFREQ output frequency transition time, "fCLKn > 1 MHz": max 10 us. TOE output enable time: max 10 us. **No PLL lock or relock time is given** | Skyworks Si5351A/B/C-B data sheet Rev. 1.3 (August 27, 2021), Table 5 "AC Characteristics", page 9. Read 2026-09-29 through the web-fetch tool from the Skyworks site (PDF SHA-256 `f3bc5285...a4851101f`); text taken with pdftotext in the session scratchpad; no file added to the repository | Datasheet |
| Si5351A status and reset | Register 0 bit 5 LOL_A, "PLL A Loss Of Lock Status ... 0: PLL A is operating normally. 1: PLL A is unlocked" (page 13). Register 177 PLLA_RST "Writing a 1 to this bit will reset PLLA. This is a self clearing bit". Data sheet Figure 10 applies the PLLA and PLLB soft reset (reg 177 = 0xAC) after a configuration write. I2C Standard-Mode 100 kbps or Fast-Mode 400 kbps, burst writes with auto address increment (data sheet section 5) | Skyworks AN619 Rev. 0.8 (September 23, 2021), Registers 0 and 177. Read as above (PDF SHA-256 `0135b3a3...4783f36b`) | Application note |
| C6 changeover writes | MSNA (reg 26 to 33, 8 bytes), CLK0 to CLK2 control (reg 16 to 18), output enable (reg 3), MSNB (reg 34 to 41, 8 bytes); optional PLL reset (reg 177) | `spurs-ts012.md` option C6; TS-012 D-12; register numbers from AN619 | Design (TS-012) |
| I2C SCL with the ADR-031 counts at clk_sys 96 MHz | about 256 kHz | `spurs-ts012.md` section 6, "I2C" (counts to be re-derived by WP-PDR-32) | Analysis |
| Key-down sequence | t0 = changeover command, after 1 ms sampling and the 2 ms make filter; 1 ms for writes and settle (allocation); FC0 interval 12 from t0 + 1 ms; 2 ms software; PA_EN at t0 + 7 ms; TX_KEY at t0 + 8 ms; ramp at t0 + 10 ms. The GVA-84+ is powered and its bias clamp released when TX_KEY, PA_EN and Q are all true (D-18) | TS-012 section 7.3 revision 6, D-18 | Design (TS-012) |
| Contact-to-RF latency | RF rise within 15 ms of each straight-key closure | REQ-SYS-160 (TBR) | TBR |
| Longest over with RF | RF ends 150 s to 180 s into continuous transmit and is held off until receive resumes | REQ-SYS-180 (TBR) | TBR |
| XOSC crystal curve | AT-cut cubic about its inflection: third-order coefficient 0.8e-4 to 1.3e-4 ppm/K^3, inflection 20 to 35 C, first-order term free inside the Table 596 band | Standard AT-cut crystal model (Bechmann's coefficients as summarized in the crystal literature); not in the corpus, not read in this invocation | **Estimate, Low** |
| Crystal temperature in service | -10 to +65 C | REQ-SYS-010 span; thermal note main-bay long-session value 57.8 C plus its band and the local rise | Estimate |
| Main-bay (Pico 2) temperature transients | the MAIN node of the thermal model, layouts A5-DC and A5-R4, ambients -10, 25, 45 C, with its 86 ranged inputs | `hardware/sim/thermal/thermal_model.py` (WP-PDR-28a, `thermal-ts012.md`), imported unchanged | Model (developer evidence) |
| Pico 2 local step at the changeover | 0.03 W change of the board's own dissipation, 47 K/W board to air, time constant 30 s (rate) | **Estimates, Low** (board area and a convective coefficient near 10 W/m2K) | Estimate |
| XOSC pushing at the changeover | 0.2 ppm | **Allocation** (3.3 V rail step); confirmed by measurement M-2 | Allocation |
| Squaring-stage settle after power-up | 50 ms | **Allocation**: a requirement on the stage that answers INSP-110 finding-25 | Allocation |
| **Revision 3 inputs** | | | |
| TG2520SMN frequency/temperature | "C: +/-0.5 x 10-6 Max. / -40 C to +85 C" (standard stability version). **No slope is given** | Seiko Epson brief sheet "TCXO / VC-TCXO TG2016SMN / TG2520SMN" ((c) 2025, 2 pages, PDF created 2025-06-25), "Specifications (characteristics)". Read 2026-09-29 through the web-fetch tool from `download.epsondevice.com` (PDF SHA-256 `df16ac04...7d846612`); text taken with pdftotext in the session scratchpad; no file added to the repository | Datasheet |
| TG2520SMN load and supply coefficients | fo-Load "+/-0.1 x 10-6 Max.", "10 kOhm // 10 pF +/- 10 %"; fo-VCC "+/-0.1 x 10-6 Max.", "VCC +/- 5 %"; output load 10 kOhm and 10 pF through a 0.01 uF DC cut | As above | Datasheet |
| TCXO step between the stage-on refresh and the stage-off check | at most 0.4 ppm: 2 x 0.1 (load) + 2 x 0.1 (supply), on the condition that both stage states and both breakout clock states keep the TCXO inside 10 kOhm // 10 pF +/-10 % and 3.3 V +/-5 % | **Allocation** built on the two coefficients above; conditions on WP-PDR-20b, 37 and 38; confirmed by measurement M-2(b) | Allocation |
| Carrier settle residual at and after the ramp (A5) | S_RAMP = 5 Hz, carrier referred, from the ramp at t0 + 10 ms | **Allocation** of this note (INSP-111 finding-7); closed by measurement M-1(c) | Allocation |
| PLL A phase-detector period | 40 ns (25 MHz reference) | TS-012 D-17 (TCXO on XA) | Design |
| **Revision 4 inputs (section 3.5)** | | | |
| TG2520SMN frequency tolerance | "+/-1.5 x 10-6 Max.", "After reflow, +25 C" | TG2520SMN brief sheet as above, "Specifications (characteristics)"; re-read 2026-09-29 in the revision 4 invocation through the web-fetch tool (PDF SHA-256 `df16ac04...7d846612`, equal to the revision 3 read); text taken with pdftotext in the session scratchpad; no file added | Datasheet |
| TG2520SMN first-year aging | "+/-0.5 x 10-6 Max.", "+25 C, First year", for 24 MHz <= fo <= 40 MHz (25 MHz) | As above | Datasheet |
| Reference temperature of the fo-TC band | **Not stated** by the brief sheet. Two readings of the temperature term of the uncalibrated error, the largest distance of f(T) from f(+25 C): 0.5 ppm if the band is referred to +25 C ("ref25"); 1.0 ppm if it is a 1.0 ppm window of unstated centre ("pp"), the reading section 3.4.2 uses for a change between two temperatures. **pp governs** until the full datasheet (TS-007 value-of-information item 5) states the reference | Reading of this note | Datasheet gap |
| A5 band-edge guard limit on the reference error | 2.972 ppm at the -60 dB point (G-6: word 5 Hz and S_RAMP 5 Hz already taken) | Section 3.1, G-6 | Analysis |

## 3. Method and results

The checker computes every number below with exact rational arithmetic. Margins are rounded toward the limit (floored). Sums compared with a ceiling are rounded up.

### 3.1 Band-edge guard (REQ-SYS-008, 009, 010; REQ-TX-002, 006; REQ-SYS-015)

The worst case at each edge adds four terms toward that edge:
- the carrier set at the guard limit;
- the reference error at +/-2.5 ppm;
- the frequency-word error of 5 Hz;
- the keying-sideband or bandwidth offset.

The lower edge uses 144.0012 MHz minus every term. The upper edge uses 147.9988 MHz plus every term. The 2.5 ppm term is 360.003 Hz at the lower edge and 369.997 Hz at the upper edge, so the upper edge governs.

| Case | Condition | Result | Margin inside the band |
|---|---|---|---|
| C-1 | Lower edge, -60 dB point at 750 Hz | 144.0000849 MHz | +84.9 Hz |
| C-2 | Upper edge, -60 dB point at 750 Hz | 147.9999250 MHz | **+75.0 Hz** (governs) |
| C-3 | Lower edge, 26 dB half-bandwidth 175 Hz | | +659.9 Hz |
| C-4 | Upper edge, 26 dB half-bandwidth 175 Hz | | +650.0 Hz |
| C-5 | Largest REQ-TX-006 offset the guard supports | 825.0 Hz | 75.0 Hz above the 750 Hz TBR |
| C-6 | Largest reference error the guard supports at 750 Hz | 3.006 ppm | 0.506 ppm above the 2.5 ppm ceiling |
| C-7.1 to C-7.3 | Research offsets 614, 735 and 750 Hz (F7) | | +211.0, +90.0, +75.0 Hz |

Known answer: with no word error the upper margin is 1200 - 370 - 750 = 80 Hz, the SRR decision 25 arithmetic (checker KA-1).

**A5: the settle residual at the ramp (revision 3, INSP-111 finding-7).** On A5, PLL A is retuned by the 8 MHz IF at the first element of every over, 10 ms before the ramp (section 3.4.1). The key-down count does not show that the carrier has settled by the ramp (section 3.4.1, ST-1). So the worst case at each edge carries a fifth term for A5: the **settle residual S_RAMP = 5 Hz**, the largest carrier error, relative to the settled frequency, at and after the ramp. It is an allocation, closed by the time-resolved measurement M-1(c) of section 3.4.1. The cases below are computed by `r3_a5.py` with the section 3.1 method and the extra term (known answer KA-R4: with S_RAMP = 0 they reproduce C-2).

| Case | Condition | Result | Margin inside the band |
|---|---|---|---|
| G-1 | A5 lower edge, -60 dB point at 750 Hz | | +79.9 Hz |
| G-2 | A5 upper edge, -60 dB point at 750 Hz | | **+70.0 Hz** (governs; C-2 is 75.0 Hz) |
| G-3, G-4 | A5 lower and upper edge, 26 dB half-bandwidth 175 Hz | | +654.9 and +645.0 Hz |
| G-5 | Largest REQ-TX-006 offset the guard supports on A5 | 820.0 Hz | 70.0 Hz above the 750 Hz TBR |
| G-6 | Largest reference error the guard supports at 750 Hz on A5 | 2.972 ppm | 0.472 ppm above the 2.5 ppm ceiling |
| G-7.1 to G-7.3 | Research offsets 614, 735 and 750 Hz (F7) on A5 | | +206.0, +85.0, +70.0 Hz |

**Finding 3.1.** The 1.2 kHz guard holds with the 5 Hz word allocation, with 75.0 Hz to spare at the upper edge. It stays valid while WP-PDR-22 confirms a REQ-TX-006 offset of at most 825.0 Hz. Above that, the "else a CR" branch of the REQ-SYS-008 `tbr.plan` applies. **For A5 (revision 3)** the settle residual lowers the upper-edge margin to 70.0 Hz and the offset limit to **820.0 Hz** (G-2, G-5), provided M-1(c) passes. The margin is small compared with the uncertainty of the REQ-TX-006 offset itself, which is a TS-006 simulation result (section 5). WP-PDR-22 therefore reports the offset at every envelope setting and tolerance corner against the 825.0 Hz limit (820.0 Hz for A5), not against 750 Hz.

### 3.2 Reference budget (REQ-SYS-010, TPM-006, RSK-002)

**A5 (revision 4).** This section is written on the TS-007 allocations: a TCXO that passes R-M3 (uncalibrated total at most 1.5 ppm). A5 puts the TG2520SMN on XA, which does not pass R-M3. **For A5, section 3.5 supersedes this section**, its cases C-8 to C-10, the two-unit table and finding 3.2.

**Frequency-word term.** The 5 Hz allocation covers both TS-007 candidates.
- Si5351A: the PLL feedback divider with a 20-bit denominator at a 25 MHz reference gives a 3.97 Hz output step at divider 6. This is an engineering assumption: the vendor register map (AN619) is not in the corpus. Rounding to the nearest step errs by at most 2.0 Hz.
- LMX2571: its fractional denominator width is not in the corpus. The allocation is therefore a requirement on the SW-SYNTH frequency-word design, verified by HostUnit tests against an independent reference model (RSK-046 step S3). It is not a property claimed for the part.

**Two budget identities** set the reference class:

1. **Calibrated case (REQ-SYS-010 as written, "after calibration").** The firmware calibration offset removes the initial and reflow terms:
   `u_cal + temperature + aging + supply/load + word <= 2.5 ppm`
2. **Guard-protecting case (HZ-008 K4).** A calibration constant entered wrongly, but inside its allowed range, adds to the uncorrected error. So the band-edge guard holds whatever the calibration state only if:
   `uncalibrated total + calibration range + word <= 2.5 ppm`
   with the calibration range no larger than the uncalibrated total it corrects. This bound makes the calibration constant a safety-relevant configuration value of the SW-SYNTH "calibration application" unit, which is safety-critical in 07 section 14.1 (HZ-008 cause C7 names "a calibration value out of range").

| Case | Terms | Result | Limit | Margin |
|---|---|---|---|---|
| C-8 | 1.5 ppm uncalibrated + 0.9 ppm range + 0.034 ppm word | 2.434 ppm | 2.5 ppm | 0.066 ppm (9.7 Hz at 148 MHz) |
| C-9 | range 0.9 ppm vs uncalibrated 1.5 ppm | range smaller | range <= uncalibrated | holds |
| C-10.1 | Calibrated, 0.1 ppm temperature class | 0.834 ppm | 2.5 ppm | 1.666 ppm |
| C-10.2 | Calibrated, 0.25 ppm class | 0.984 ppm | 2.5 ppm | 1.516 ppm |
| C-10.3 | Calibrated, 0.5 ppm class | 1.234 ppm | 2.5 ppm | 1.266 ppm |
| C-10.xu | Share of the 1.5 ppm uncalibrated allocation left for initial and reflow | 0.8 / 0.65 / 0.4 ppm for the three classes | | datasheet test at CDR |

**Two-unit offset after calibration (RSK-002 step S1), Hz at 146 MHz.** Both units are calibrated. Each unit's residual is `u_cal + temperature + aging + supply/load`, and the word error is counted for each unit.

| Temperature class | At calibration (aging 0) | After one year (aging 0.5 ppm) | Against the 250 Hz half-passband |
|---|---|---|---|
| 0.1 ppm | 97.6 Hz | 243.6 Hz | inside, both |
| 0.25 ppm | 141.4 Hz | 287.4 Hz | inside at calibration, outside after a year |
| 0.5 ppm | 214.4 Hz | 360.4 Hz | inside at calibration, outside after a year |

**Finding 3.2.**
- REQ-SYS-010 at +/-2.5 ppm closes with margin for every class. The margin sits in the calibrated case.
- The guard-protecting identity is the binding one. It turns into two derived constraints:
  - (a) a TCXO datasheet acceptance test: uncalibrated total at most 1.5 ppm over -10 to +45 C and one year, including reflow (TS-007 R-M3);
  - (b) a firmware calibration range of at most +/-0.9 ppm (+/-133 Hz at 148 MHz), which is a new SW-SYNTH requirement (section 5).
- RSK-002 is fully mitigated only with the 0.1 ppm class, or with re-calibration within a year. Otherwise the receiver incremental tuning of RSK-002 step S3 remains the operator's tool.
- The TPM-006 current best estimate, calibrated worst case, is 0.834, 0.984 or 1.234 ppm by class, `credit: false`. The estimate becomes credit-bearing on the datasheet of the part chosen at CDR.

### 3.3 Frequency-verification counter (REQ-SYS-182, REQ-SYS-154, REQ-TX-013; HZ-008 K7)

**Architecture assumed** (proposal; the SW-SAFE design belongs to WP-PDR-32 and WP-PDR-35):
- A hardware divide-by-8 prescaler on the transmit carrier sample (taken at the exciter, ahead of the PA) drives one RP2350 GPIN input.
- The RP2350 frequency counter FC0 counts it. FC0's interval is timed by clk_ref from the XOSC (datasheet section 8.1.3), so it is independent of the synthesizer reference and of the SW-SYNTH driver.
- FC0 sets DIED when the counted clock stops. This implements the rule of REQ-SYS-182 that "no valid measurement means no agreement" in hardware.
- The prescaler input is on the TX path only, so it adds no receive line (see `clock-plan.md`).

**Sample (REQ-TX-013).** 144.0012 to 147.9988 MHz divided by 8 gives 18.000 15 to 18.499 85 MHz (C-11). This is below the 20 MHz ceiling of REQ-TX-013 and below the 50 MHz GPIN limit. A digital divider is exact, so the sample times 8 equals the carrier: the 1 kHz accuracy of REQ-TX-013 is met with no error term, and 1 kHz stays as the Test tolerance. A ratio of 16 is rejected: 144 MHz / 16 is 9.000 MHz, on the candidate IF (`clock-plan.md` section 4).

**Timebase routes.** A fault-free unit shows a disagreement between the counted and the set frequency. The window W must exceed that disagreement, or healthy units trip into Fault-safe.

- **R1, raw XOSC timebase (HZ-008 K7 text as written).** Disagreement = FC0 accuracy x 8 + TCXO error + XOSC error (65 ppm = 9 620 Hz at 147.9988 MHz).
- **R2, XOSC corrected by a constant stored at unit calibration.** Rejected. Table 596 gives only a +/-30 ppm stability band with no curve, so a room-temperature calibration cannot be shown to shrink the bound below R1's without an assumption on the crystal's temperature curve.
- **R3, XOSC corrected by a TCXO count taken in receive.** FC0 counts the TCXO on the second GPIN during receive (interval 15) and refreshes the XOSC/TCXO ratio at least once a second. In a healthy unit, carrier and TCXO are then in an exact ratio, so the TCXO error cancels. The remaining disagreement is:
  - FC0 accuracy x 8;
  - the TCXO-count quantization (62.5 Hz / 25 MHz = 2.5 ppm);
  - an allocated 1 ppm XOSC drift between refreshes.

  The refreshed ratio is accepted only within +/-67.5 ppm (XOSC 65 + TCXO 2.5). Outside that, the unit enters Fault-safe, so a gross TCXO or XOSC fault is itself detected.

**Measured threshold and true-error limit (revision 1, INSP-056 finding-1).** Two limits apply, and they are not the same quantity:
- REQ-SYS-154 bounds the **true** error: Fault-safe when the synthesizer is off its set frequency by over 10 kHz.
- The counter sees only the **measured** error, which differs from the true error by up to the healthy disagreement d.

A measured threshold T therefore meets REQ-SYS-154 only if two conditions hold:
- no false trip: d < T;
- no missed trip: T + d <= 10 kHz, so any true error over 10 kHz measures above T.

With a 10 kHz measured threshold (revision 0), a true error up to 10 kHz + d passes: 14 518 Hz at interval 12. That did not meet REQ-SYS-154. This revision proposes a **measured threshold T = 5.0 kHz** for both intervals. It lies inside the R3 interval at interval 12 (4 518 < T <= 5 482 Hz) and at interval 13 (2 518 < T <= 7 482 Hz). T is an SW-SAFE design value (L2, WP-PDR-35). REQ-SYS-154 (10 kHz true error) and REQ-SYS-182 (10 kHz measured agreement) keep their values: a measured agreement within 5 kHz is also an agreement within 10 kHz, so RF is still withheld whenever the measurement disagrees by more than 10 kHz.

| Case | Route and use | FC0 interval | Healthy disagreement d | No false trip: d < T = 5 kHz | Largest undetected true error T + d, against REQ-SYS-154 10 kHz | TC-SYS-101 12 kHz injection: 12 kHz - d > T |
|---|---|---|---|---|---|---|
| C-12.iv12, C-16.iv12, C-18.iv12 | R3, check before PA_EN at changeover | 12 (4 ms) | 4 518.0 Hz | holds, margin 482.0 Hz | 9 518.0 Hz, margin 482.0 Hz | trips, margin 2 482.0 Hz |
| C-12.iv13, C-16.iv13, C-18.iv13 | R3, repeated check during transmit | 13 (8 ms) | 2 518.0 Hz | holds, margin 2 482.0 Hz | 7 518.0 Hz, margin 2 482.0 Hz | trips, margin 4 482.0 Hz |
| C-13.iv12 | R1, changeover | 12 | 13 990.0 Hz | no T exists below 10 kHz | at least 27 609.9 Hz (T just above d) | not applicable |
| C-13.iv13 | R1, transmit | 13 | 11 990.0 Hz | no T exists below 10 kHz | at least 23 609.9 Hz | not applicable |
| (table) | R1 | 14 (16 ms) | 10 990.0 Hz | no T exists below 10 kHz | at least 21 609.9 Hz | not applicable |

C-12w checks that T (5 kHz) does not exceed the REQ-SYS-182 10 kHz window. Under R1, no threshold meets both conditions with REQ-SYS-154 at 10 kHz, because d alone exceeds 10 kHz. R1 would need REQ-SYS-154 at 23.7 kHz or more (interval 13) and the REQ-SYS-182 window at 12.0 kHz or more, both by CR.

**Sensitivity to the FC0 accuracy (C-16a).** The 482 Hz margin at interval 12 is small beside the 4 000 Hz FC0 term inside d. Both conditions hold while the FC0 accuracy at the counted input is at most 560.2 Hz at interval 12, against the 500 Hz of Table 541, and at most 560.2 Hz at interval 13, against its 250 Hz. The 560 Hz ceiling at interval 12 becomes the acceptance limit of the FC0 known-clock check on the dev board (07 WP-SW-14; section 6 item 4). If that check fails, the changeover check moves to interval 13: C-14.A2 then takes 11.5 ms, 0.5 ms inside the 12 ms lead-in.

**Effect on TC-SYS-101.** With T = 5 kHz, the 12 kHz injection of TC-SYS-101 (and of the REQ-SYS-182 verification note) measures at least 7 482 Hz at interval 12 and at least 9 482 Hz at interval 13, so it trips at key-down and during the over, with 2 482 Hz and 4 482 Hz to spare (C-18). The case needs no change: its acceptance criteria and its 12 kHz injection stand as written. The threshold itself is verified at L2 by HostUnit cases with injected counts on both sides of T (request to WP-PDR-35, section 5).

**Unlocked synthesizer (revision 1, INSP-056 finding-2).** REQ-SYS-154 also calls for Fault-safe when the synthesizer is unlocked, whatever its frequency. An unlocked VCO can sit inside T for a while as it drifts, so the counter alone does not catch every unlocked state. Two means apply, and the device lock-detect indication is the primary one:

| Case | Moment | Primary means | Second means | Time budget | Result |
|---|---|---|---|---|---|
| U-1.A1, U-1.A2 | Unlocked at key-down (before PA_EN) | `SW-SYNTH` reads the lock-detect indication after the last synthesizer write and again immediately before it sets the `PA_EN` frequency prerequisite (07 section 14.2 `SW-SYNTH` items g and l). The read is inside the 2 ms software allocation of C-14 | The FC0 interval 12 check (C-12): an unlocked output more than 5.482 kHz off trips; FC0 DIED catches a stopped output | changeover 6.00 ms (A1) and 7.50 ms (A2), inside the 12 ms lead-in (REQ-SYS-161) | PA_EN is never set with an unlocked synthesizer |
| U-2 | Unlocked during transmission | `SW-SYNTH` samples the lock-detect indication at least every 10 ms (allocation), or takes it as a GPIO edge interrupt if the part has a lock-detect pin, and requests Fault-safe on loss of lock | The FC0 interval 13 repeated check (C-15, 46.0 ms to RF off) | 10 ms to detection + 20 ms RF off (REQ-SYS-004) = 30.0 ms, inside the 100 ms of REQ-SYS-182, which bounds detection plus the fall for frequency faults | RF off within 30 ms of loss of lock; 70 ms margin |

REQ-SYS-154 sets no time of its own. REQ-SYS-004 bounds the RF-off time after detection (20 ms), and REQ-SYS-182 bounds detection plus the fall (100 ms) for the same fault family, so the U-2 budget is checked against both.

The lock-detect form for the recommended line-up is a research gap. The LMX2571 lock-detect indication (a pin, or a status register read over SPI) is not in the corpus. It belongs to TS-007 value-of-information item 4, the LMX2571 datasheet read, which INSP-055 finding-4 asks TS-007 to extend with the lock-detect output. The allocations therefore cover both forms:
- **Lock-detect pin:** one RP2350 GPIO input, read by `SW-SYNTH` (request to WP-PDR-36a).
- **Status register only:** an SPI status read in each 10 ms service period during transmission. The read is a transmit-time SPI transaction, so it adds no receive line (`clock-plan.md` rule 4).

If the LMX2571 offers neither form, an unlocked VCO within 9.518 kHz of the set frequency is not detected before it drifts past T. The "unlocked" trigger of REQ-SYS-154 would then be met only for an unlock that the counter sees, and REQ-SYS-154 would need a CR to restate that trigger. This is the "else a CR" branch for the unlock half, decided when value-of-information item 4 is answered (TS-007 section 8, before CDR).

For A1 (Si5351A as transmit synthesizer, not recommended), the loss-of-lock status bit is read over I2C with the same 10 ms period. Its register map (AN619) is not in the corpus.

**Times.**

| Case | Path | Result | Limit | Margin |
|---|---|---|---|---|
| C-14.A1 | Changeover: no retune + 4 ms FC0 + 2 ms software | 6.00 ms | 12 ms lead-in (REQ-SYS-161, TBR) | 6.00 ms |
| C-14.A2 | Changeover: 1.5 ms FastLock + 4 ms + 2 ms | 7.50 ms | 12 ms | 4.50 ms |
| C-15 | Fault during transmit: two 8 ms intervals + 10 ms service period + 20 ms RF off (REQ-SYS-004) | 46.0 ms | 100 ms (REQ-SYS-182) | 54.0 ms |

A fault that starts inside an interval may not trip that interval, because the count mixes the good and bad frequencies. The next full interval trips it, hence two intervals in C-15.

**Finding 3.3.**
- On the raw XOSC timebase (route R1), a fault-free unit at a worst-case crystal disagrees by up to 11.99 kHz at interval 13. The adopted 10 kHz window of REQ-SYS-182 would then trip healthy units, and no measured threshold can meet the 10 kHz true-error limit of REQ-SYS-154. R1 therefore needs, by CR, a REQ-SYS-182 window of at least 12.0 kHz and a REQ-SYS-154 limit of at least 23.7 kHz at interval 13. This is the "else they change by CR" branch of the REQ-SYS-182 `tbr.plan`. Interval 13 leaves only 0.5 ms of lead-in margin for A2.
- Route R3 with the measured threshold T = 5.0 kHz meets REQ-SYS-154 (10 kHz true error) and REQ-SYS-182 (10 kHz, 100 ms) as written. The margins are 482 Hz at interval 12 and 2 482 Hz at interval 13, both sides of T, and 54 ms in time. The largest undetected synthesizer error is 9.518 kHz under R3, against at least 23.6 kHz under R1. Both routes catch the gross error the hazard names (5 W on 150 to 174 MHz, HZ-008 C7).
- The 12 kHz injection of TC-SYS-101 trips under R3 at both intervals (C-18); the case stands as written.
- Both REQ-SYS-154 triggers have a detection means at both moments. The unlocked trigger rests on the device lock-detect indication, read before PA_EN and every 10 ms during transmission (U-1, U-2; 30 ms to RF off), with the counter as the second means. Its form on the LMX2571 is TS-007 value-of-information item 4.
- R3 departs from one phrase of the HZ-008 K7 text, "uses the RP2350 crystal timebase rather than the synthesizer reference". The gate stays on the XOSC, but the scale factor uses the TCXO, bounded by the 67.5 ppm plausibility test.
- **Recommendation:** R3, with FC0 on two GPIN pins, interval 12 before PA_EN and interval 13 during transmit, and a measured threshold of 5.0 kHz. The K7 wording change goes to the hazards writer (section 5). If the owner prefers the K7 text as written, route R1 is taken, with REQ-SYS-182 at 12 kHz or more and REQ-SYS-154 at 23.7 kHz or more by CR.

### 3.4 Route R3 for A5: Si5351A relock, ratio freshness and the receive-only squaring stage (revision 2, WP-PDR-20a)

**The A5 arrangement** (TS-012 D-12, D-17, D-18; the key-down sequence of TS-012 section 7.3, revision 6):
- The Adafruit Si5351A runs from the TG2520SMN on XA.
- In receive, PLL A drives CLK0, the LO, and PLL B drives CLK2, the 8 MHz BFO.
- At the changeover command t0, the C6 writes retune PLL A to the carrier multiplier, power up CLK1, power down CLK0 and CLK2, and park PLL B on the PLL A multiplier.
- The /8 prescaler drives GPIN0.
- The TCXO drives GPIN1 through a squaring stage that is powered only in receive.
- FC0 counts interval 12 before PA_EN and interval 13 during transmission, against the measured threshold T = 5.0 kHz.

Checker `hardware/sim/freq/r3_a5.py`, run `r3a5-20260929-02` (revision 3): 38 PASS, 0 FAIL, 14 INFO. The case ids below are its output lines. Revision 3 times every FC0 count at 2^n x 1 us: 4.096 ms at interval 12, 8.192 ms at 13 and 32.768 ms at 15 (INSP-056 finding-12; KA-R3).

#### 3.4.1 Si5351A PLL relock at the changeover (TS-012 section 10, revisit condition 1)

**What the sources say.** The Skyworks data sheet (Rev. 1.3) and AN619 (Rev. 0.8) were read for a lock, settle or acquisition time (RL-0, RL-1). **Neither gives a PLL lock time or a relock time after a feedback-divider (MSNA) change.** Three timing values exist, and none of them decides:

| Sourced value | What it covers | Bearing on the relock |
|---|---|---|
| TFREQ, output frequency transition time, at most 10 us (fCLKn > 1 MHz) | a frequency change at an output | Table 5 does not say whether it covers a PLL feedback change or only a MultiSynth change. If it covers the MSNA retune, the relock fits the allocation with 0.34 ms to spare (RL-7a) |
| TRDY, power-up time, typ 2 ms, max 10 ms | power-up to a valid output: NVM copy, system initialization and PLL acquisition from power-up | A superset of a relock, so it is an upper bound only on that reading. At 10 ms it exceeds every settle time the sequence allows (RL-7b) |
| TOE, output enable time, at most 10 us | CLK1 enable | Negligible |

AN619 gives the lock status, register 0 bit 5 LOL_A, readable over I2C. It gives the PLL reset in register 177. The data sheet's Figure 10 procedure applies the reset after a configuration write; whether the changeover writes need it is not stated.

**Time the sequence allows.**
- The C6 writes are four I2C bursts of 28 data bytes. At 400 kHz Fast-Mode they take **0.650 ms**, or 0.723 ms with the reg 177 reset (RL-2). That leaves **0.35 ms** of the 1 ms allocation for the PLL to settle.
- At 100 kHz Standard-Mode the same writes take 2.6 ms (RL-2s).
- At the SCL of about 256 kHz that the ADR-031 counts give at clk_sys 96 MHz (`spurs-ts012.md` section 6), they take 1.016 ms, over the allocation before any settle time (RL-2b).
- One LOL_A read takes 0.098 ms, inside the 2 ms software allocation (RL-3).

Let L be the time from t0 to the start of the FC0 count, writes included. PA_EN must be set no later than 2 ms before the ramp. That is TX_KEY at t0 + 8 ms against the ramp at t0 + 10 ms, the drive power-up time the TS-012 sequence keeps.

| Case | Sequence | Largest L | Largest settle after the 0.65 ms writes |
|---|---|---|---|
| RL-4, RL-4d | Interval 12 (4.096 ms), ramp kept at t0 + 10 ms (the TS-012 sequence with PA_EN at TX_KEY) | 1.904 ms; proposed deadline **L_max = 1.9 ms** (rounded down to 0.1 ms): PA_EN at t0 + 7.996 ms, 0.004 ms before TX_KEY. A 2.0 ms deadline would set PA_EN at t0 + 8.096 ms, after TX_KEY | 1.25 ms |
| RL-5 | Interval 12, ramp moved to t0 + 12 ms, the limit of both REQ-SYS-161 (12 ms) and REQ-SYS-160 (15 ms less the 3 ms before t0) | 3.904 ms (3.9 ms rounded down), **0.096 ms below the TS-012 revisit threshold of 1 + 3 ms** | 3.25 ms |
| RL-6 | Interval 13 (8.192 ms) at the changeover, ramp at t0 + 12 ms | **-0.192 ms** (infeasible) | none |
| RL-6f | The TS-012 fallback as written: 1 ms allocation, interval 13, ramp at t0 + 11.5 ms | PA_EN at t0 + 11.192 ms, **0.308 ms** before the ramp | none beyond the 1 ms allocation |

**Reading.**
- The 1 ms allocation is **not confirmed by a source**. The relock time is not specified.
- The revisit condition is therefore neither triggered nor excluded by the read. The source bounds a relock at 0.01 ms if TFREQ applies, and at 10 ms only through TRDY.
- The TS-012 threshold as worded ("exceeds 1 ms by more than 3 ms") is 0.096 ms looser than the sequence allows: a relock of L between 3.904 and 4 ms is inside the threshold and yet fits no sequence inside REQ-SYS-161 (RL-5). The feasible edge is L = 3.9 ms, a settle of 3.25 ms after the writes.
- The TS-012 fallback rule for a triggered condition (the check moves to interval 13 and the ramp to 11.5 ms) is no remedy for a slow relock. Interval 13 at the changeover leaves no time for any relock with the 2 ms drive power-up before the ramp (RL-6). TS-012's fallback keeps only 0.308 ms between PA_EN at t0 + 11.192 ms and the ramp at t0 + 11.5 ms (RL-6f), which WP-PDR-23a has to accept or reject. The fallback still serves its other trigger, an FC0 known-clock check above its acceptance limit (532.5 Hz for A5, section 3.4.2), if 23a accepts the 0.308 ms.

**What the key-down count verifies, and what it does not (revision 3, INSP-111 finding-7).** A counter measures cycles, so a count bounds only the **mean** frequency over its own interval, from t0 + L to t0 + L + 4.096 ms. Revision 2 read that as proof that a slow relock costs availability only, "for any relock time". That holds for one part of the settle and not for the other:
- **The slewing part is caught.** While PLL A slews from the LO setting, the output is near the old LO frequency, 8 MHz away, with one sign. A full-error transient longer than 2.56 us inside the interval-12 count moves the mean by more than T (5 kHz x 4.096 ms / 8 MHz; ST-2), so PA_EN stays low. That part costs availability: a late or lost first element, not RF at an unchecked frequency. A loop that settles to a wrong frequency is caught by the interval-13 checks during transmission, within the 46.4 ms of B-15, inside the 100 ms "or end it" branch of REQ-SYS-182.
- **The linear tail is not caught.** Once the phase error at the phase detector is inside one reference period (40 ns at 25 MHz), the error a tail can add to a count is at most the phase error at the count's start minus that at its end: two reference periods, 80 ns, about 12 carrier cycles. That shifts an interval-12 count by at most 2 x 40 ns x 147.9988 MHz / 4.096 ms = **2 890.7 Hz**, inside T (ST-1). The instantaneous excursion of a ringing tail can meanwhile be larger. So a count that agrees does not show the frequency at the ramp (t0 + 10 ms) or during the first element's rise.

The frequency at the ramp therefore needs a **bound on the settle**, not the count. This revision makes it a named allocation, the settle residual **S_RAMP = 5 Hz** from the ramp onward, carried as a fifth term of the A5 band-edge guard (section 3.1, G-1 to G-7; upper-edge margin 70.0 Hz), and closes it by the time-resolved measurement M-1(c) below. The count stays the credited means for the frequency agreement over its interval (REQ-SYS-182, HZ-008 K7); it is not credited for the frequency at the ramp. INSP-118 item (3) states the revision 2 premise ("a PLL still settling gives a count outside T"); its correction is routed to the TS-012 record (section 5, WP-PDR-54).

The retune happens once per over, at its first element. The tail is a property of the Si5351A loop, not of the frequency word, so it is bounded by verification of the design: M-1(c) on the dev board, repeated on each assembled unit at 147.990 MHz as a unit acceptance step (request to WP-PDR-43). A carrier that stays off frequency after the tail is still caught by the interval-13 checks.

**Design response (proposal; requests in section 5).**
1. **Lock-gated start.** SW-SYNTH issues the C6 writes at t0, with MSNA first. It then polls LOL_A until the bit reads 0, and starts FC0 interval 12 on GPIN0 at the first 0 read, and no later than t0 + L_max. Here **L_max = 1.9 ms** (RL-4d; revision 2 had 2.0 ms on the rounded 4 ms count), so the TS-012 ramp at t0 + 10 ms is kept with PA_EN at t0 + 7.996 ms at the latest.
   - If LOL_A is still 1 at L_max, or the count disagrees, PA_EN is not set for that element.
   - LOL_A is not credited as proof of settling. AN619 describes it as a reference or lock-range fault indication, so the FC0 count stays the credited means.
   - The lead-in stays constant (REQ-SYS-161), because the ramp time does not depend on when the count starts.
2. **I2C at Fast-Mode.** Derived constraint: SCL of at least 263 kHz, so that the 260 SCL clocks of the C6 writes and a TFREQ-scale settle fit the 1 ms allocation (RL-2b); 400 kHz is recommended. The WP-PDR-32 re-derivation of the I2C counts at 96 MHz must meet it.
3. **No reg 177 reset at the changeover**, unless measurement M-1 shows that the retune needs it. A reset restarts acquisition, and the data sheet gives no time for it.
4. **Measurement M-1** (dev board: a Pico 2 and the Adafruit Si5351A with a 25 MHz reference; 07 WP-SW-14, beside the FC0 known-clock check). Three parts; (a) and (b) bound the settle for availability (when the count can start), (c) bounds the frequency at the ramp (the band-edge guard):
   - Set CLK1 to VCO/48 (about 17 to 18.5 MHz, inside the GPIN limit).
   - Issue the C6 writes from an LO setting to a carrier setting at 144.010, 146.000 and 147.990 MHz. Take 20 changeovers at each frequency.
   - **(a) LOL_A.** Poll LOL_A with timestamps. It measures no frequency (AN619 ties it to the reference), so it is logged, not credited.
   - **(b) Count start.** Start an interval-12 count at a delay D after the last write, stepping D from 0 to 3.4 ms in 0.05 ms steps over repeated changeovers. The smallest D whose counts all agree within T/8 at the counted input bounds the slewing part of the settle (ST-2). It does not bound a linear tail (ST-1). Short intervals (8 or 9) are too coarse for this: 8 kHz at the input at interval 8.
   - **(c) Frequency at the ramp (time-resolved; revision 3).** Record the CLK1 frequency against time from the last C6 write to t0 + 150 ms. Proposed method (ST-3): a D flip-flop samples CLK1 with a steady reference about 1 kHz away, independent of the TCXO (for example the tinySA Ultra generator output, squared; CON-016), and an RP2350 PIO program timestamps the beat edges at clk_sys. One beat period per 1 ms window gives a resolution of 0.63 Hz carrier referred, inside the required S_RAMP/3 = 1.67 Hz. The settled frequency f_final is the mean over t0 + 50 to t0 + 150 ms of the same record, so the reference's own offset cancels. Another method is acceptable if it meets the resolution; it goes on the WP-PDR-43 bench list, with the CON-016 relief if the tinySA generator does not suit.
   - **Pass, in order:**
     - (c) **|f - f_final| <= S_RAMP = 5 Hz (carrier referred) in every 1 ms window from the ramp at t0 + 10 ms to t0 + 50 ms**, at all three frequencies and all 20 changeovers. Let t_R be the latest time at which a window is outside 5 Hz. If t_R is at most t0 + 10 ms, the sequence stands. If it is at most t0 + 12 ms, the ramp moves to t_R, a WP-PDR-23a timing-table change inside REQ-SYS-161 and REQ-SYS-160 with no requirement delta. Above that, a design change is needed (below).
     - (b) settle at most 0.35 ms, which keeps the 1 ms allocation at 400 kHz. If it is at most **1.25 ms**, the sequence stands with L_max = 1.9 ms. If it is at most **3.25 ms**, the ramp moves toward t0 + 12 ms (L_max 3.9 ms), the same timing-table change. Above that, a design change is needed: for example, retune at the first key sample instead of at t0, which gains up to the 3 ms of sampling and make filter and needs a receive-restore path for a rejected closure.
     - The later ramp of (b) and (c) governs.
   - Faster frequency modulation inside a 1 ms window is not a carrier offset. Its sidebands are part of the keyed spectrum that TC-TX-006 measures.

**Finding 3.4.1.**
- Revisit condition 1 is **open, not triggered by the source read**. The source does not specify the relock time.
- The key-down count bounds the mean over its own interval. It catches the slewing part of a slow relock (availability) and not a linear tail (ST-1). The frequency at the ramp rests on the settle residual allocation S_RAMP = 5 Hz, closed by M-1(c), and the A5 guard margin falls from 75.0 to 70.0 Hz (G-2).
- WP-PDR-32 and WP-PDR-36a can be written now: the lock-gated structure, the pins and the timing table do not depend on the measured value, which only sets L_max (1.9 ms) and, in the worst branches, the ramp time.
- No requirement or CR-018 row changes. The REQ-TX-006 offset limit for A5 becomes 820.0 Hz (G-5).
- The TS-012 fallback rule does not cover this trigger (RL-6), and the TS-012 threshold is 0.096 ms looser than the sequence allows (RL-5). Both are requests to WP-PDR-54 (the TS-012 record) and to WP-PDR-23a.

#### 3.4.2 XOSC/TCXO ratio freshness (TS-012 section 10, revisit condition 2)

**Where the ratio's age matters.**
- The squaring stage is off from t0 until receive resumes, so every check during an over uses the last ratio taken before the over.
- The ratio's age at a check is its age at t0, plus the time into the over. RF can run at most 180 s into an over (REQ-SYS-180), so no check with RF comes later than that.
- The first element's check is at interval 12, whose drift ceiling is 4.26 ppm at zero margin (FR-5). The checks during the over are at interval 13, whose ceiling is 17.77 ppm (FR-6). The ceiling is the largest drift for which T = 5.0 kHz still meets d < T and T + d <= 10 kHz.
- Revision 1 put one 1 ppm allocation on both.

**Drift bound (revision 3, INSP-056 finding-11).** Under route R3 the carrier estimate is the GPIN0 count scaled by the last XOSC/TCXO ratio. In a healthy unit the carrier is N x f_TCXO(now), so the estimate differs from the set frequency by [f_TCXO(now) / f_TCXO(refresh)] x [f_XOSC(refresh) / f_XOSC(now)] - 1. Both factors count. Revision 2 budgeted only the XOSC factor. The ratio drift is therefore:
- the XOSC slope times the crystal's temperature change, plus pushing (revision 2);
- the TCXO's own temperature change since the refresh. The TG2520SMN sits on the Adafruit breakout in the main bay, so it sees about the same temperature change. Its brief sheet gives the band, +/-0.5 ppm over -40 to +85 C, and **no slope**. Without a slope, the change over any temperature step, and so at any ratio age, is bounded only by the band: **1.0 ppm** peak to peak;
- the TCXO load and supply step between the refresh, counted with the squaring stage on and the breakout in its receive clock state (CLK0 and CLK2 on), and every check, made with the stage off and CLK1 on. The brief sheet gives fo-Load +/-0.1 ppm for 10 kOhm // 10 pF +/-10 % and fo-VCC +/-0.1 ppm for VCC +/-5 %. If both states keep the TCXO inside those ranges, each state is within 0.1 ppm of the nominal-condition frequency for each cause, so the step is at most 2 x 0.1 + 2 x 0.1 = **0.4 ppm**. It is systematic and present at every check, interval 12 included. The two ranges become conditions on the squaring stage and its supply (WP-PDR-20b, 37, 38), and M-2(b) measures the step.

| Term | Value | Basis |
|---|---|---|
| Largest XOSC slope in service | **0.924 ppm/K** (FR-1) | 15 392 AT-cut curves admitted inside the +/-30 ppm Table 596 band over -40 to +85 C. Largest slope over -10 to +65 C: at 25 C, first-order term -0.924 ppm/K, third-order 1.3e-4 ppm/K^3 (`xosc-slope.png`). Estimate, Low |
| Main-bay (Pico 2) change over the window W = A_kd + 180 s = 190 s | nominal **2.589 K** (A5-R4 at -10 C, continuous transmit from the receive steady state), RSS band +2.404 K, total **4.993 K** (FR-3) | Thermal model MAIN node, both A5 layouts, three ambients, heating and cooling (`ratio-freshness.png` left). The band is dominated by the feed resistance: r_feed 0.26 to 0.45 ohm adds 2.245 K, and c_main 40 to 90 J/K adds 0.812 K |
| Pico 2 local step | 1.41 K (0.03 W x 47 K/W, taken in full with no time-constant credit) | Estimate, Low |
| Pushing | 0.2 ppm | Allocation (M-2(b)) |
| XOSC part over the longest over | 0.924 x (4.993 + 1.41) + 0.2 = 6.116 ppm | revision 2 bound |
| TCXO temperature change | 1.0 ppm (FR-T) | TG2520SMN fo-TC band, +/-0.5 ppm; no slope given |
| TCXO load and supply step | 0.4 ppm (FR-T) | TG2520SMN fo-Load and fo-VCC, 2 x 0.1 each; allocation with the load and supply conditions (M-2(b)) |
| **Drift over the longest over** | 6.116 + 1.0 + 0.4 = **7.516 ppm** (FR-4) | |

**Reading.**
- **Revisit condition 2 is triggered as worded.** The ratio cannot be kept within 1 ppm over the longest over: the bound is 7.52 ppm. Even a fresh ratio carries 1.4 ppm of TCXO terms, so no ratio age meets 1 ppm.
- The bound also exceeds the interval-12 ceiling of 4.26 ppm (FR-5). So an aged ratio must never serve an interval-12 check.
- It is well inside the interval-13 ceiling of 17.77 ppm.
- The budget therefore closes, **with no requirement change**, by splitting the drift term by check. Both allocations are the bound rounded up to 0.5 ppm:

| Check | Ratio age | Drift allocation | Healthy d | Margin to T | Largest undetected true error | 12 kHz injection |
|---|---|---|---|---|---|---|
| B-*.iv12: key-down, before PA_EN | at most **A_kd = 10 s** | **2.5 ppm** (proposed; bound at A_kd 2.358 ppm: XOSC 0.958 + TCXO 1.4) | 4 740.0 Hz | 260.0 Hz | 9 740.0 Hz (margin 260.0 Hz) | trips, margin 2 260.0 Hz |
| B-*.iv13: during the over | at most A_kd + 180 s | **8.0 ppm** (proposed; bound 7.516 ppm) | 3 554.0 Hz | 1 446.0 Hz | 8 554.0 Hz (margin 1 446.0 Hz) | trips, margin 3 446.0 Hz |

Both allocations are inside their ceilings: 2.5 against 4.256 ppm at interval 12, and 8.0 against 17.77 ppm at interval 13 (FR-2, FR-6).

**FC0 accuracy ceilings for A5 (B-16a).** The larger allocations lower the FC0 accuracy for which both threshold conditions hold: **532.5 Hz** at the counted input at interval 12 (was 560.2 Hz), against the 500 Hz of Table 541, and **430.7 Hz** at interval 13, against its 250 Hz. For A5 these replace the C-16a values as the dev-board known-clock acceptance limits (section 3.3 governs A1 and A2 only).

**A_kd.** The largest rate of change is 0.035 K/s in the main bay (0.017 K/s nominal plus its band, over any window) plus 0.047 K/s from the local step (1.41 K over a 30 s time constant). With the 0.2 ppm pushing and the 1.4 ppm TCXO terms, the ratio age at which the drift reaches the 2.5 ppm interval-12 allocation is 11.8 s, floored (FR-2). **A_kd = 10 s** is kept as proposed in revision 2: at 10 s the drift is 2.358 ppm (rounded up), 0.142 ppm inside the allocation.

In receive the ratio is never older than 1.083 s: the 1 s refresh plus the 50 ms stage settle and the 32.768 ms interval-15 count (FR-2r). So A_kd binds only on a key-down that follows an over by less than one refresh.

**Two rules the split needs** (requests to WP-PDR-23a, 32 and 35, section 5):
- **R-FRESH-1: refresh at once on return to receive.** When receive resumes after an over, the squaring stage is powered and one ratio refresh is started at once.
- **R-FRESH-2: no interval-12 check on a ratio older than A_kd.** If the ratio is older than 10 s at t0, because the operator keyed again before the refresh of R-FRESH-1 completed, PA_EN is not set on the aged ratio. One refresh (at most 82.8 ms) completes first.
  - Whether the changeover waits for it (that element is then late, outside REQ-SYS-160) or the element is not radiated is for 23a and 32 to fix. Both outcomes are on the safe side.
  - The case needs a key-down within about 83 ms of the hang expiring, after an over longer than 10 s.

**FC0 is a single counter.** A refresh in progress at t0 must be abandoned so that the interval-12 count can start at t0 + L. R-FRESH-2 then decides whether the older ratio may be used. WP-PDR-32 confirms from the RP2350 data sheet that writing FC0_SRC stops a count in progress. This invocation did not read the RP2350 data sheet.

**Measurement M-2** (the assembled unit on the bench, 07 WP-SW-14 and the WP-PDR-43 bench plan). The ratio is counted with the stage on, in receive, so it sees the XOSC thermal drift and the TCXO temperature change but not the pushing or the TCXO step, which exist only in the transmit state. M-2 therefore has two parts whose limits add up to the allocations (FR-7):
- **M-2(a) ratio change.**
  - Log the ratio in receive, averaging 16 interval-15 counts for a resolution near 0.6 ppm. The averaging holds if the count quantization dithers; if it does not, build a longer software gate from successive counts.
  - Transmit into the dummy load at 5 W, at the highest duty the keyer limits allow, until REQ-SYS-180 ends RF (150 to 180 s).
  - Log the ratio at once on return to receive, and keep logging for the first 10 s.
  - Pass: the change over the over is at most **7.4 ppm** (the 8.0 ppm interval-13 allocation less the 0.2 ppm pushing and the 0.4 ppm TCXO step), and the change within A_kd = 10 s after an over is at most **1.9 ppm** (the 2.5 ppm interval-12 allocation less the same).
- **M-2(b) transmit-state steps**, measured on the carrier, which follows the TCXO, with the M-1(c) beat fixture on CLK1 (resolution far below 0.01 ppm over 1 s):
  - TCXO step: CLK1 frequency with the squaring stage on against off, and in the receive clock state (CLK0, CLK2 on) against the transmit clock state (CLK1 only), alternated at least 10 times to cancel reference drift. Pass: at most **0.4 ppm** between any two states.
  - Pushing: the XOSC change across a changeover without RF, from the interval-13 GPIN0 count of a fixed CLK1 with the Pico 2 rail in its receive and transmit load states, averaged as in (a). Pass: at most 0.2 ppm (unchanged).

**Finding 3.4.2.**
- Revisit condition 2 **triggers as worded**: 7.52 ppm over the longest over (6.12 ppm XOSC and 1.4 ppm TCXO), against 1 ppm.
- The route R3 budget still closes for REQ-SYS-154 and REQ-SYS-182 **as written, with T = 5.0 kHz and intervals 12 and 13 unchanged**. It needs the ratio-age rule at the key-down check (A_kd = 10 s, with R-FRESH-1 and R-FRESH-2), a 2.5 ppm drift allocation at the key-down check (margin 260.0 Hz) and an 8.0 ppm allocation for the checks during the over (margin 1 446.0 Hz), with the TCXO load and supply conditions on the squaring stage.
- No CR-018 row changes. Under the plan's rule for this condition (plan section 10.6, the "§10 revisit conditions of revision 6" row: "a trigger goes to the owner at S1 if it changes CR-018, else at S2"), the trigger goes to the owner at S2.
- The TS-012 fallback (interval 13 at the changeover) is not needed for this trigger.

#### 3.4.3 Receive-only squaring stage and the 150.000 MHz line

- **In transmission.** The stage's supply is off from t0 until receive resumes, so the stage adds nothing to the 150.000 MHz line (25 MHz x 6). The `spurs-ts012.md` figure stands: plan PB high estimate -12.1 dBm at the SMA, 3.9 dB over 25 uW, a residual line closing at the bench (BL-2).
  - The unpowered stage's input must neither load nor rectify the TCXO, which also drives XA. That needs a partial-power-down input, or an isolating series element sized with the stage: a part constraint for WP-PDR-37 and 38.
  - **Revision 3 (INSP-056 finding-11):** in both stage states, powered and unpowered, the TCXO's total load (the XA input, the stage input and its bias network) stays inside the rated 10 kOhm // 10 pF +/-10 %, and its supply inside 3.3 V +/-5 % in both breakout clock states. These are the conditions of the 0.4 ppm step allocation of section 3.4.2.
- **In receive.** Harmonics 1 to 8 of the squared 25 MHz, with the 2.5 ppm TCXO tolerance, fall in none of the receive windows: 144.010 to 147.999 MHz, the 8 MHz IF, the LO and image bands for either injection side (BL-1, `r3-budget-and-buffer.png` right). The nearest is 150.000 MHz, 2.0 MHz above the receive range. The stage adds level, not new frequencies, to the 25 MHz lines `clock-plan.md` already carries.
- **Refresh time.** The 50 ms settle allocation plus the 32.768 ms interval-15 count is 82.8 ms per refresh, 8.3 % of receive if the stage is power-cycled each second (B-19). It can also stay on through receive, which only helps.
- **The stage itself is not designed here.** TS-012 revision 8 section 8.1 note 3 records INSP-110 finding-25: a 74LVC1G17 Schmitt buffer cannot be self-biased, and a stage that toggles at the TCXO's 0.8 V peak-to-peak minimum is still to be named. The 50 ms settle allocation is a requirement on that stage. Its valid-clock run is requested of WP-PDR-20b, beside the prescaler-tap run at 1.66 Vpp. Until it runs, a stage that does not toggle reads as FC0 DIED, so RF is withheld: safe, but at a cost in availability.

#### 3.4.4 The unlocked trigger on A5, and I2C during transmission

For A5 the device lock-detect indication of U-1 and U-2 is the Si5351A **LOL_A bit** (AN619 register 0 bit 5), read over I2C. This closes, for A5, the research gap of section 3.3: the lock-detect form was a TS-007 value-of-information item 4 question for the LMX2571, and the "else a CR" branch for a part without a lock-detect indication no longer applies.
- **U-1 (key-down) is unchanged.** The read after the writes and before PA_EN is inside the 2 ms software allocation (RL-3). The A5 changeover time is 1 + 4.096 + 2 = 7.096 ms with the allocation, and at most 1.9 + 4.096 + 2 = 7.996 ms with L_max. Both are inside the 12 ms lead-in.
- **U-2 (during transmission) conflicts with D-12 (C6: "I2C only in the lead-in").** U-2 samples the indication at least every 10 ms during transmission, and on the 10-MSOP Si5351A that is an I2C read, since only the Si5351C has an INTR pin (data sheet section 4.6). TS-012 and the spur plan admit no I2C traffic in transmission. The options, for WP-PDR-32 and 35 with the spur plan's owner:
  - (a) Admit one register-0 read (4 bytes, 0.098 ms at 400 kHz) per 10 ms service period, and add its SCL line set to the transmit spur inventory.
  - (b) Read LOL_A only in key-up gaps and at each element's key-down. Then an unlock that stays inside T during a long element is caught only by the counter once it drifts past T.

  This note does not choose. With (b), the REQ-SYS-154 "unlocked during transmission" case rests on the counter alone, and the U-2 row of section 3.3 must be restated. Whether that needs a REQ-SYS-154 wording CR is a question for the requirement owner (the owner, on the WP-PDR-35 proposal).

**Finding 3.4.** Route R3 holds for A5 with REQ-SYS-154 and REQ-SYS-182 as written and the section 3.3 threshold and intervals unchanged (the transmit detection time is 46.4 ms on the 2^n x 1 us basis, B-15), on these conditions:
- the lock-gated changeover (L_max 1.9 ms, Fast-Mode I2C of at least 263 kHz);
- the ratio-age rule at the key-down check (A_kd 10 s, R-FRESH-1 and R-FRESH-2) with a 2.5 ppm drift allocation there;
- the interval-13 drift allocation of 8.0 ppm;
- the TCXO load and supply conditions on the squaring stage (section 3.4.3);
- the settle residual S_RAMP = 5 Hz at the ramp, which keeps the A5 band-edge guard at 70.0 Hz (section 3.1, G-2).

The two TS-012 revisit conditions stand as follows:
- **Relock: open**, not triggered by the source read; closure by M-1, whose part (c) also closes the settle residual at the ramp.
- **Freshness: triggered as worded**, and closed in the budget without a requirement change; confirmation by M-2(a) and M-2(b).

Two items are open for other writers: the U-2 I2C conflict, and the squaring stage of INSP-110 finding-25.

### 3.5 A5 reference budget with the TG2520SMN (revision 4, INSP-111 finding-13)

**Why this section.** Section 3.2 protects the band-edge guard against a wrong calibration constant with identity 2, uncalibrated total + calibration range + word <= 2.5 ppm. That rests on the 1.5 ppm uncalibrated allocation, which TS-007 made the datasheet acceptance test R-M3. A5 puts the TG2520SMN on XA (TS-012 D-17), and TS-007 left R-M3 "not shown" for it (row RB2). The brief sheet read for revision 3 gives its terms. Checker `r3_a5.py`, run `r3a5-20260929-03`, cases KA-R5, KA-R6 and RB-0 to RB-8.

**Terms.** The sheet does not say at what temperature the +/-0.5 ppm fo-TC band is referred (section 2). Two readings are carried. The "pp" reading governs, because it is the one section 3.4.2 already uses and it lies on the hazard side.

| Term (ppm) | Band referred to +25 C ("ref25") | Band as a 1.0 ppm window ("pp", governs) | Source |
|---|---|---|---|
| Tolerance after reflow, at +25 C | 1.5 | 1.5 | f_tol |
| Temperature, largest distance from f(+25 C) | 0.5 | 1.0 | fo-TC |
| First-year aging at 25 MHz | 0.5 | 0.5 | f_age |
| Load | 0.1 | 0.1 | fo-Load |
| Supply | 0.1 | 0.1 | fo-VCC |
| **Uncalibrated total** (RB-0) | **2.7** | **3.2** | against R-M3 1.5 ppm: **not met** |

**After a correct calibration (identity 1, REQ-SYS-010).** The error is taken from the calibration condition, so the terms are the ones section 3.4.2 uses for a change: calibration uncertainty 0.1, temperature change 1.0 (the whole band), aging 0.5, load and supply step 0.4 (2 x 0.1 + 2 x 0.1), word 0.034. The sum is **2.034 ppm**, 0.466 ppm inside 2.5 ppm, and the A5 guard keeps 144.0 Hz (RB-3). This needs a calibration range of at least **+/-1.5 ppm**, the +25 C tolerance. It is the smallest range. Calibration away from +25 C, or a re-calibration after aging, needs more (section 6 item 17).

**Cases** (upper edge governs; the -60 dB point at 750 Hz, word 5 Hz and S_RAMP 5 Hz counted once each through the section 3.1 method; KA-R5 reproduces C-8 and G-2):

| Case | Reference error, ppm (ref25 / pp) | Identity 2, limit 2.5 ppm | -60 dB point inside the band, Hz (ref25 / pp) |
|---|---|---|---|
| RB-1: no calibration, or a constant of 0 | 2.7 / 3.2 | 2.734 / 3.234 ppm: fails | +40.4 / **-33.6** |
| RB-2: constant wrong within +/-0.9 ppm | 3.6 / 4.1 | 3.634 / 4.134 ppm: fails | **-92.8 / -166.8** |
| RB-2: constant wrong within +/-1.5 ppm | 4.2 / 4.7 | 4.234 / 4.734 ppm: fails | **-181.6 / -255.6** |
| RB-3: correct calibration, range at least +/-1.5 ppm | 2.0 | (identity 1: 2.034 ppm, holds) | +144.0 |
| RB-4: unit at +1.5 ppm, range held at +/-0.9 ppm | 2.6 (0.6 ppm left uncorrected) | (identity 1: 2.634 ppm, **over REQ-SYS-010**) | +55.2 |

`reference-budget-a5.png` shows each case against the R-M3, REQ-SYS-010 and G-6 limits, and where the -60 dB point falls.

**Reading.**
- For A5, **identity 2 fails at every calibration range**, 2.734 ppm even at zero range (ref25). So neither derived constraint of finding 3.2 holds for A5. The TG2520SMN fails R-M3. The +/-0.9 ppm range does not protect the guard: a constant wrong within it puts the -60 dB point 92.8 Hz (ref25) to 166.8 Hz (pp) beyond 148.000 MHz.
- **No fixed range meets both** REQ-SYS-010 for every unit and the guard (RB-5). REQ-SYS-010 needs at least +/-1.5 ppm: with +/-0.9 ppm a unit at +1.5 ppm stays at 2.634 ppm (RB-4). The guard tolerates at most 0.272 ppm of range on the ref25 reading. On the pp reading it fails even with no calibration.
- **An uncalibrated unit.** On the pp reading, a unit with no valid constant (before its first calibration, or with a lost constant set to zero) puts the -60 dB point 33.6 Hz beyond the band (RB-1). This holds for the TG2520SMN whatever option is chosen below, until the full datasheet shows the band is referred to +25 C.
- **Difference from the finding's figures.** The finding gives 97.8 and 186.6 Hz beyond the band and a 50.2 Hz guard margin in the clamped case. On the same ref25 reading the checker gives 92.8, 181.6 and 55.2 Hz. Each differs by 5.0 Hz: the finding adds the 5 Hz word term (0.034 ppm) to the reference error and compares it with G-6, which has already taken the word term off. The checker counts it once. The finding's conclusions stand.

**Options** (named for the decision, not chosen; RB-6a to RB-6c):

| Option | What it takes | Arithmetic | Effect on requirements and hazards |
|---|---|---|---|
| (a) A TCXO that meets R-M3 | A part on XA with an uncalibrated total of at most 1.5 ppm over -10 to +45 C and one year, reflow included (TS-007: the SiT5356 class), whose datasheet states the fo-TC reference | Identity 2 with +/-0.9 ppm: 2.434 ppm, inside 2.5 ppm (C-8 stands); with a wrong constant the -60 dB point stays 84.8 Hz inside (RB-6a) | No requirement CR. Section 3.2, the +/-0.9 ppm bound and the K4 bound stand. A part change on D-17 (TS-012 record, BOM, cost) |
| (b) A guard CR | Keep the TG2520SMN with a calibration range of at least +/-1.5 ppm, and widen the band-edge guard | Needed guard 1 381.6 Hz (ref25) or 1 455.6 Hz (pp): **1.4 or 1.5 kHz**; carrier limits 144.0015 to 147.9985 MHz on the governing reading (RB-6b) | CR on REQ-SYS-008, REQ-SYS-009 and REQ-TX-002 (the "else a CR" branch of their `tbr.plan`). REQ-SYS-010 holds (RB-3). The K4 bound becomes the +/-1.5 ppm range with the new guard. Each band end loses 0.3 kHz |
| (c) A software integrity check on the calibration value | The unit's factory offset, measured at unit calibration, is stored with an integrity check. A constant is accepted only within +/-delta of that stored offset, and only through the verified calibration procedure. A missing, corrupt or out-of-bound value withholds transmission; it never falls back to 0 (RB-1) | A wrong constant inside the bound errs by at most 2.0 + delta ppm. The guard holds for **delta <= 0.972 ppm**; at delta = 0.9 ppm the margin is 10.8 Hz (RB-6c) | No requirement value CR. Part of K4 becomes a `SW-SYNTH` hazard control (07 section 14.1), with SWE-134 items g and k, a WP-PDR-16b input and a Test closing case (SWE-192). The stored factory offset becomes safety data |

**RSK-002 and TPM-006 for A5.** The two-unit offset after calibration at 146 MHz is 448.0 Hz at calibration and 594.0 Hz after one year (RB-7), both outside the 250 Hz half-passband, so the receiver incremental tuning of RSK-002 step S3 is the operator's tool on A5. The TPM-006 current best estimate for A5 is **2.034 ppm** calibrated, `credit: false` (RB-3), in place of the 0.834 to 1.234 ppm of section 3.2. Re-read with a class of c ppm as a 2c change, the section 3.2 values for the TS-007 classes become 0.934, 1.234 and 1.734 ppm (all inside 2.5 ppm), and the two-unit offsets 126.8 / 272.8, 214.4 / 360.4 and 360.4 / 506.4 Hz at calibration / after one year (RB-8). The 0.1 ppm class then also exceeds 250 Hz after a year. These govern no A5 value.

**Finding 3.5.**
- The TG2520SMN does not pass R-M3: 2.7 ppm (ref25) or 3.2 ppm (pp) uncalibrated, against 1.5 ppm.
- REQ-SYS-010 holds for A5 after a correct calibration (2.034 ppm, margin 0.466 ppm) if the calibration range is at least +/-1.5 ppm.
- The guard-protecting identity fails for A5 at every range. The three items that sections 4 and 5 sent on for the TS-007 allocations are therefore **held open for A5**, as U-2 is: the +/-0.9 ppm `SW-SYNTH` requirement to WP-PDR-35, the HZ-008 K4 bound to WP-PDR-16b, and the REQ-SYS-010 "else a CR: No" to the owner.
- The choice among options (a), (b) and (c) goes to the lead SE for the owner (section 5). This note does not choose. The choice changes no pin, no timing value and no section 3.4 result.

## 4. Proposed TBR values (rule C10: to the owner only after this note's record is APPROVED and a TV record or owner ruling covers the checker)

| Requirement | Proposed value | Margin that supports it | `tbr.plan` step executed | "Else a CR" branch triggered? |
|---|---|---|---|---|
| REQ-SYS-008 | 144.0012 to 147.9988 MHz (1.2 kHz guard), unchanged | 75.0 Hz at the upper edge with REQ-TX-006 at 750 Hz; holds up to 825.0 Hz | "the frequency error budget and the TS-006 sideband offset confirm the 1.2 kHz guard at PDR" | No, provided WP-PDR-22 confirms at most 825.0 Hz. **For A5: open** (section 3.5): Yes if the owner takes option (b), a 1.4 or 1.5 kHz guard |
| REQ-SYS-009 | Same limits as REQ-SYS-008 | same | "closes with the guard value" | No |
| REQ-TX-002 | Same limits as REQ-SYS-008 | same | "closes with REQ-SYS-008" | No |
| REQ-SYS-010 | +/-2.5 ppm, -10 to +45 C (span follows REQ-SYS-114, WP-PDR-28), one year after calibration, unchanged | calibrated case 1.266 to 1.666 ppm; guard-protecting identity 0.066 ppm with the section 3.2 constraints | "TS-NNN selects the reference grade; the error budget fixes the tolerance; span reconciled with TPM-006" (the budget lives here; WP-PDR-29 carries it into `docs/design/budgets.md`) | No, for the TS-007 allocations. **For A5: open** (revision 4, section 3.5): the value holds after a correct calibration (2.034 ppm) with a range of at least +/-1.5 ppm, but the guard-protecting identity fails at every range, so this row does not go to the owner as "No" until the section 3.5 option is chosen |
| REQ-SYS-154 | 10 kHz true-error limit, unchanged, with route R3 and the measured threshold T = 5.0 kHz (an SW-SAFE L2 value, distinct from this limit). Unlocked trigger: device lock-detect indication read before PA_EN and at least every 10 ms during transmission, with the counter as the second means | Off-frequency: 482 Hz (changeover) and 2 482 Hz (transmit) on both sides of T (C-12, C-16). Unlocked: 30.0 ms to RF off, 70 ms inside 100 ms (U-2). TC-SYS-101 12 kHz injection trips with 2 482 Hz to spare (C-18); the case is unchanged | "TS (synthesizer and lock detect) fixes the counting tolerance": the counting tolerance is T = 5.0 kHz; the lock-detect means is as stated | No with R3, provided the LMX2571 exposes a lock-detect indication (TS-007 value-of-information item 4); if it does not, a CR restates the unlocked trigger. Yes with R1 (at least 23.7 kHz) |
| REQ-SYS-182 | 10 kHz and 100 ms, unchanged, with route R3 | measured threshold 5.0 kHz is within the 10 kHz window (C-12w); healthy margin 482 Hz; 54 ms | "the PDR prescaler, counter and timebase design confirms them against the counter gate time, resolution and crystal tolerance, else they change by CR" | No with R3. Yes with R1 (window at least 12 kHz; 100 ms holds) |
| REQ-TX-013 | Fixed ratio 8; sample 18.000 15 to 18.499 85 MHz, 3.3 V, below 20 MHz; within 1 kHz (exact division) | 1.5 MHz under the 20 MHz ceiling | "fixes the division ratio, the counting input and the sample accuracy" (counting input: an RP2350 GPIN pin to FC0) | No |

**Revision 2 (A5, section 3.4; its margins and allocations are superseded by revision 3 below).** No proposed value in this table changes:
- **REQ-SYS-154 and REQ-SYS-182** keep 10 kHz, 100 ms and T = 5.0 kHz on route R3, with the section 3.4 conditions: the lock-gated changeover, the ratio-age rule at the key-down check (A_kd = 10 s) and the 6.5 ppm interval-13 drift allocation.
- **Changed margins.** The margins at interval 13 fall from 2 482.0 Hz to 1 668.0 Hz, because the drift allocation there rises from 1 to 6.5 ppm. The interval-12 margins are unchanged at 482.0 Hz.
- **REQ-SYS-154, "else a CR" column.** For A5 the lock-detect indication exists (Si5351A LOL_A), so the LMX2571 branch no longer applies. It is replaced by the open U-2 question of section 3.4.4: if lock status is not read during transmission, the unlocked trigger during transmission rests on the counter, and the requirement owner decides whether the REQ-SYS-154 wording needs a CR.
- **Revisit conditions.** The TS-012 conditions give no value change: the relock condition is open (M-1), and the freshness condition triggered and closed in the budget (M-2 confirms). Under rule C10 these values still go to the owner only on this note's APPROVED record.

**Revision 3 (A5; INSP-056 findings 11 and 12, INSP-111 finding-7).** Still no requirement value in this table changes. What changes for A5:
- **REQ-SYS-008, 009, REQ-TX-002.** The A5 upper-edge margin is 70.0 Hz, not 75.0 Hz, with the 5 Hz settle residual at the ramp (G-2). The guard holds up to a REQ-TX-006 offset of **820.0 Hz** (G-5), provided M-1(c) passes. "Else a CR" is triggered only if WP-PDR-22 reports more than 820.0 Hz.
- **REQ-SYS-154 and REQ-SYS-182.** The margins to T at the key-down check fall from 482.0 Hz to **260.0 Hz** (2.5 ppm drift allocation, TCXO terms included); the TC-SYS-101 injection margin there is 2 260.0 Hz. During the over they are **1 446.0 Hz** (8.0 ppm allocation, was 6.5 ppm and 1 668.0 Hz); the injection margin is 3 446.0 Hz. The transmit detection time is 46.4 ms, 53.6 ms inside 100 ms. Both checks stay inside their ceilings (4.26 and 17.77 ppm).
- **SW-SAFE and SW-SYNTH values.** L_max 1.9 ms (was 2.0 ms); A_kd 10 s (unchanged, limit 11.8 s); drift allocations 2.5 ppm at interval 12 and 8.0 ppm at interval 13; FC0 known-clock acceptance limits 532.5 Hz at interval 12 and 430.7 Hz at interval 13 (B-16a).

**Revision 4 (A5; INSP-111 finding-13).** Still no requirement value in this table changes, but three items are held open for A5 (section 3.5):
- **REQ-SYS-010.** +/-2.5 ppm holds for A5 after a correct calibration: 2.034 ppm, margin 0.466 ppm, with a calibration range of at least +/-1.5 ppm. The guard-protecting identity (0.066 ppm in the row above) does not hold for A5: 2.734 ppm at zero range. The "else a CR" column is **open for A5**; it is not sent to the owner as "No".
- **REQ-SYS-008, REQ-SYS-009, REQ-TX-002.** Open for A5 on the same decision. Option (b) is a CR to a 1.4 kHz (ref25) or 1.5 kHz (pp) guard. Options (a) and (c) keep 1.2 kHz.
- **TPM-006 for A5.** Current best estimate 2.034 ppm calibrated, `credit: false` (RB-3).

The choice among the section 3.5 options (a TCXO that meets R-M3, a guard CR, or a software integrity check on the calibration value) is routed to the lead SE for the owner (section 5, revision 4 rows).

TPM-006: planned value +/-2.5 ppm, per the ADR-023 ceiling. Current best estimate 0.834 / 0.984 / 1.234 ppm (calibrated, by class; TS-007 allocations), and 2.034 ppm for A5 (revision 4), `credit: false`, evidence this note. The value is sent to the TPM writer (WP-PDR-29). This note does not edit `docs/plan/tpm.json`.

## 5. Derived constraints and requests to other writers (plan section 5.3; this note edits none of these files)

| To | Request |
|---|---|
| WP-PDR-16b (`docs/safety/hazards.json`, sole writer) | HZ-008 K7: replace "uses the RP2350 crystal timebase rather than the synthesizer reference" with route R3's wording: gate on the XOSC; XOSC/TCXO ratio refreshed in receive and bounded at +/-67.5 ppm; FC0 DIED status as "no valid measurement"; a measured threshold of 5.0 kHz, so that a true error over 10 kHz always trips. HZ-008 C8 and K7: name the device lock-detect indication as the primary means for the unlocked cause, with the counter as the second means. HZ-008 K4: add the calibration-range bound of section 3.2 (calibration constant within +/-0.9 ppm); **revision 4: held open for A5** (section 3.5: with the TG2520SMN the bound does not protect the guard; see the revision 4 rows). If R1 is chosen instead, K7 keeps its text, its window becomes 12 kHz and the REQ-SYS-154 limit at least 23.7 kHz |
| WP-PDR-35 (`docs/requirements/sw/**`) | New SW-SYNTH requirements: calibration constant bounded at +/-0.9 ppm, out-of-range value rejected (**revision 4: held open for A5**, not to be written for A5 until the section 3.5 option is chosen; see the revision 4 rows); lock-detect indication read after every write and immediately before the `PA_EN` frequency prerequisite is set; lock-detect sampled at least every 10 ms during transmission, loss of lock requesting Fault-safe (07 section 14.2 items g, l). New SW-SAFE requirements: FC0 on the carrier sample at interval 12 before PA_EN and 13 during transmit; measured threshold 5.0 kHz (disagreement above 5.0 kHz is a disagreement); TCXO ratio refresh at least once a second in receive; ratio plausibility +/-67.5 ppm; DIED or FAIL as disagreement. Test author: HostUnit cases with injected counts at 4.9 and 5.1 kHz and with an injected lock-detect loss before PA_EN and during transmission |
| WP-PDR-32 (software architecture, 07 WP-SW-14) | The frequency counter is FC0 with two GPIN inputs, not a PIO or TIMER capture. It needs a timing analysis confirming the 2 ms changeover latency (now including the lock-detect read), the 10 ms transmit service period and the 10 ms lock-detect sample period allocated here. The FC0 known-clock check on the dev board has the acceptance limit 560 Hz at interval 12 (C-16a) |
| WP-PDR-36a (`ICD-CTL-SW` pin map) | Two GPIN-capable pins: GPIO 20 or 22 (GPIN0, GPIN1), or GPIO 12 or 14 (RP2350 datasheet GPIO function table). One carries the prescaled carrier, one the TCXO (or a divided TCXO copy). One GPIO input for the synthesizer lock-detect pin, if TS-007 value-of-information item 4 shows the LMX2571 has one |
| WP-PDR-22 (TS-006) | Report the REQ-TX-006 offset at every setting and corner against the 825.0 Hz limit of case C-5; for A5 against **820.0 Hz** (case G-5, revision 3) |
| WP-PDR-29 (`docs/design/budgets.md`, `docs/plan/tpm.json`) | Frequency budget section and TPM-006 current best estimate as in section 4 |
| WP-PDR-18 (`docs/risk/register.json`) | RSK-002: step S1 evidence is this note. It stays at likelihood 3 or above unless the 0.1 ppm class or yearly re-calibration is adopted. RSK-046: step S2 evidence is this note. The software-fault member now has an analysis (section 3.3); re-score at the Track pass |

**Revision 2 requests (section 3.4; A5), with the revision 3 values. This note edits none of these files.**

| To | Request |
|---|---|
| WP-PDR-23a (key-down and key-up sequence, ICD-TX-SW timing table) | Write the changeover as lock-gated: C6 writes at t0 with MSNA first, LOL_A polled, FC0 interval 12 (4.096 ms) started at the first LOL_A = 0 or at t0 + L_max = **1.9 ms** (revision 3; 2.0 ms would put PA_EN after TX_KEY), PA_EN only on agreement, and the ramp fixed at t0 + 10 ms so that the lead-in stays constant. Carry both M-1 ladders: (b) count start, settle at most **1.25 ms**, sequence unchanged; at most **3.25 ms**, ramp toward t0 + 12 ms; (c) frequency at the ramp, within 5 Hz of the settled frequency by t0 + 10 ms, sequence unchanged; by t0 + 12 ms, the ramp moves to that time; the later ramp governs. Accept or reject the TS-012 fallback's **0.308 ms** from PA_EN to the ramp (RL-6f): with the 2 ms drive power-up of the nominal sequence, interval 13 at the changeover leaves no relock time (RL-6). Fix the R-FRESH-2 outcome for a key-down on a ratio older than A_kd = 10 s: late element or element not radiated |
| WP-PDR-32 (software architecture) | The lock-gated changeover and the L_max deadline of 1.9 ms. The count is credited for the frequency agreement over its own interval, not for the frequency at the ramp (section 3.4.1). For A5 the FC0 known-clock acceptance limits are 532.5 Hz at interval 12 and 430.7 Hz at interval 13 (B-16a), replacing 560 Hz. I2C SCL of at least 263 kHz in the count re-derivation at clk_sys 96 MHz (400 kHz recommended; 256 kHz fails, RL-2b). No reg 177 reset at the changeover unless M-1 needs one. FC0 as a single counter: confirm from the RP2350 data sheet that writing FC0_SRC stops a count in progress, so that a receive refresh can be abandoned at t0. R-FRESH-1 and R-FRESH-2. Resolve the U-2 I2C conflict of section 3.4.4, option (a) or (b), with the spur plan's owner |
| WP-PDR-35 (`docs/requirements/sw/**`) | SW-SAFE: the ratio age at an interval-12 check is at most 10 s, else no PA_EN on that ratio; refresh at once on return to receive; checks during an over at interval 13 only; the drift allocations of 2.5 ppm at interval 12 and 8.0 ppm at interval 13 (revision 3: XOSC and TCXO terms) are the design basis for T (T itself unchanged at 5.0 kHz); the start deadline L_max is 1.9 ms after t0. SW-SYNTH: LOL_A (Si5351A register 0 bit 5) is the lock-detect indication, read after the C6 writes and before PA_EN; the read during transmission follows the WP-PDR-32 resolution of U-2. HostUnit cases: an injected ratio age of 9.9 and 10.1 s at key-down; a LOL_A that stays 1 until after L_max; a refresh abandoned at t0 |
| WP-PDR-36a (`ICD-CTL-SW` pin map) | No change from revision 1: GPIN0 carrier/8, GPIN1 TCXO from the squaring stage (GPIO 20 and 22, or 12 and 14). Add one GPIO for the squaring-stage supply switch (on in receive, off from t0), unless WP-PDR-37 derives it from an existing receive-only rail. No lock-detect pin: the 10-MSOP Si5351A has none |
| WP-PDR-20b | The squaring stage that answers INSP-110 finding-25, with its valid-clock run at the TCXO's 0.8 V peak-to-peak minimum and the Si5351A XA input in parallel. Its settle after power-up must be at most 50 ms. Its unpowered input must neither load nor rectify the TCXO. **Revision 3:** in both stage states the TCXO's total load (XA input, stage input, bias network) stays inside 10 kOhm // 10 pF +/-10 % (TG2520SMN fo-Load condition), shown by the run for both states |
| WP-PDR-37 and 38 (schematic, BOM) | The squaring stage part with a partial-power-down input (or an isolating element) and a switched supply. The Si5351A I2C bus on its own RP2350 instance (TS-007 SA finding-3) with pull-ups sized for Fast-Mode. **Revision 3:** the TCXO supply stays inside 3.3 V +/-5 % in the receive and transmit clock states of the breakout (TG2520SMN fo-VCC condition) |
| WP-PDR-43 (V&V plan), 07 WP-SW-14 (dev-board checks) | M-1: Si5351A relock after the C6 writes, parts (a) LOL_A, (b) count start and **(c) time-resolved CLK1 frequency, pass within 5 Hz of the settled frequency from the ramp** (section 3.4.1, pass criteria and ladder there); the beat fixture of M-1(c) on the bench list (tinySA Ultra generator, a D flip-flop, the RP2350 PIO; CON-016 relief if needed); M-1(c) repeated on each assembled unit at 147.990 MHz as a unit acceptance step. M-2(a): ratio change at most 7.4 ppm over a 180 s transmission and at most 1.9 ppm in the first 10 s after it; M-2(b): TCXO step at most 0.4 ppm between the stage and clock states, and pushing at most 0.2 ppm (section 3.4.2). All beside the FC0 known-clock check (532.5 Hz at interval 12, 430.7 Hz at interval 13 for A5) |
| WP-PDR-54 (TS-012 record, sole writer) | TS-012 section 10, revision 6 revisit conditions: relock **open**, not triggered by the source read (Si5351A data sheet Rev. 1.3 and AN619 Rev. 0.8 give no relock time), closing by M-1; freshness **triggered as worded** (revision 3: 7.52 ppm over the longest over, of which 1.4 ppm is the TCXO's own terms), closed in the budget without a requirement change (A_kd 10 s with 2.5 ppm at interval 12, 8.0 ppm at interval 13); the stated consequence "the check moves to interval 13 and the lead-in to 11.5 ms" does not remedy a slow relock (RL-6) and keeps only 0.308 ms from PA_EN to the ramp (RL-6f). Revision 3: the relock threshold "1 ms exceeded by more than 3 ms" is 0.096 ms looser than any sequence inside REQ-SYS-161 allows (RL-5; the feasible edge is L = 3.9 ms); section 7.3's key-down sequence carries L_max 1.9 ms on the 4.096 ms count; and the premise of INSP-118 item (3), cited by section 7.3, that "a PLL still settling gives a count outside T" holds for the slewing part only: the frequency at the ramp rests on the settle residual and M-1(c) (INSP-111 finding-7, cross item X-7). For the owner at S2 (plan section 10.6 row) |
| WP-PDR-16b (`docs/safety/hazards.json`) | HZ-008 K7, in addition to the revision 1 wording: the ratio used at the key-down check is at most 10 s old. HZ-008 C8: the lock-detect indication on A5 is Si5351A LOL_A. **Revision 3:** HZ-008 K4 on A5: the carrier settle residual at the ramp is bounded by design verification (M-1(c), 5 Hz), not by the key-down count |

**Revision 4 requests (section 3.5; A5 reference budget, INSP-111 finding-13). This note edits none of these files.**

| To | Request |
|---|---|
| Lead SE, for the owner | Route the decision of section 3.5 to the owner on the next owner sheet, in plain terms: the chosen TCXO (TG2520SMN) is looser than the budget assumed (2.7 to 3.2 ppm against 1.5 ppm before calibration), so a calibration value that is wrong but inside the planned +/-0.9 ppm limit can put the keyed signal's -60 dB point up to 92.8 to 166.8 Hz beyond 148.000 MHz. Three ways to keep the band edge safe: (a) a TCXO that meets the 1.5 ppm test, a part change; (b) a wider band-edge guard, 1.4 or 1.5 kHz instead of 1.2 kHz, by CR on REQ-SYS-008, 009 and REQ-TX-002; (c) a software check that accepts a calibration value only close to the unit's stored factory measurement (within 0.97 ppm) and withholds transmission otherwise. Until she chooses, the three items below stay open. The risk request of INSP-111 cross item X-13 (a member of RSK-002) goes to WP-PDR-18 with it |
| WP-PDR-35 (`docs/requirements/sw/**`) | For A5, **do not write** the "calibration constant bounded at +/-0.9 ppm" `SW-SYNTH` requirement of the revision 1 row. Hold it open on the section 3.5 decision. Under option (a) it stands as written. Under (b) the bound is +/-1.5 ppm. Under (c) it is replaced by: the constant is accepted only within +/-delta (at most 0.97 ppm) of the stored factory offset; the stored offset carries an integrity check; entry only through the verified calibration procedure; a missing, corrupt or out-of-bound value withholds transmission, with no fall back to zero. Under every option on the pp reading of the TG2520SMN: no transmission without a valid constant (RB-1) |
| WP-PDR-16b (`docs/safety/hazards.json`) | HZ-008 K4 for A5: **hold the calibration-range bound open** on the section 3.5 decision. Cause C7 ("a calibration value out of range") also covers a value wrong inside its range, which with the TG2520SMN exceeds the guard (RB-2). Under option (c) part of K4 becomes a `SW-SYNTH` software control (SWE-134 items g and k) with a Test closing case (SWE-192). On the pp reading an uncalibrated TG2520SMN unit is 33.6 Hz outside the band (RB-1), a K4 condition under every option but (a) |
| WP-PDR-54 (TS-012 record, sole writer) | TS-007 R-M3 result for RB2, the TG2520SMN on XA (D-17): **not met**, 2.7 ppm (fo-TC band referred to +25 C) or 3.2 ppm (band read as a 1.0 ppm window), against 1.5 ppm (section 3.5, RB-0). The D-17 part stands unless the owner takes option (a) |
| WP-PDR-20b (INSP-055 and INSP-074 deltas) | The same R-M3 result for RB2, for TS-007 and the clock plan |
| WP-PDR-29 (`docs/design/budgets.md`, `docs/plan/tpm.json`) | TPM-006 current best estimate for A5: 2.034 ppm calibrated, `credit: false` (RB-3) |
| WP-PDR-18 (`docs/risk/register.json`) | RSK-002 for A5: the two-unit offset after calibration is 448.0 Hz at calibration and 594.0 Hz after one year (RB-7), both over the 250 Hz half-passband; step S3 (receiver incremental tuning) stays the operator's tool. With the INSP-111 X-13 risk entry |
| WP-PDR-38 (BOM) | The full TG2520SMN datasheet (TS-007 value-of-information item 5): the reference temperature of the fo-TC band decides between the ref25 and pp readings of section 3.5 |

## 6. Uncertainty and limitations

1. **Tool status.** The checker has no TV record. Its arithmetic has three known-answer self-checks (KA-1 to KA-3) and can be recomputed by hand from the tables above. Before the section 4 values go to the owner, a TV record must cover `hardware/sim/freq/*.py`, or the owner must rule to accept developer evidence. The lead SE decides which route (return, open_questions).
2. **Allocations are not datasheet values.** The allocations include the TCXO uncalibrated total, aging, supply and load, calibration uncertainty, software latency and service period. Each is a requirement on a later design or part choice, verified at CDR (datasheet Inspection, WP-PDR-32 timing analysis). A part that misses an allocation re-opens this note.
3. **REQ-TX-006 dominates the guard margin.** The 75.0 Hz margin is smaller than any plausible uncertainty of a simulated -60 dB offset. The guard is only as good as the WP-PDR-22 corner analysis.
4. **FC0 accuracy semantics.** Table 541 gives "accuracy" per interval without saying whether it is a bound or a typical value. This note treats it as a +/- bound at the counted input. The dev-board check of 07 WP-SW-14 is to confirm it with a known clock, against the 560 Hz ceiling at interval 12 that the 5.0 kHz threshold needs (C-16a). **Revision 3:** for A5 the ceilings are 532.5 Hz at interval 12 and 430.7 Hz at interval 13 (B-16a).
5. **XOSC bound.** 65 ppm is the Table 596 sum over -40 to +85 C. Over -10 to +45 C the true value is smaller, so R1's result is conservative.
6. **LMX2571 retune time.** "FastLock < 1.5 ms" (F20) is a datasheet feature statement. Its conditions for a 12 MHz jump (RX LO to TX carrier with a 9 to 10.7 MHz IF) are not in the corpus. C-14.A2 has 4.5 ms of margin for it.
7. **Lock-detect form.** The LMX2571 lock-detect indication and its latency are not in the corpus (TS-007 value-of-information item 4, as INSP-055 finding-4 asks it to be extended). U-1 and U-2 assume the indication is valid within the 10 ms sample period. **Revision 2:** for A5 the indication is the Si5351A LOL_A bit (AN619). Its latency after a real loss of lock is not specified; AN619 ties it to a reference outside the lock range or an invalid reference.
8. **(Revision 2) The relock time is unspecified.** Section 3.4.1 rests on the absence of a value in the data sheet and AN619. Revision 3: the key-down count validates only the mean over its interval, so the slewing part of the settle is covered by the count and the tail by the S_RAMP allocation and M-1(c). The 0.650 ms write time assumes 9 SCL clocks per byte plus one per START and STOP at exactly 400 kHz. A slower SCL or clock stretching lengthens it in proportion.
9. **(Revision 2) The XOSC slope is a model.** The AT-cut cubic, its third-order coefficient and its inflection are literature values, not a datasheet read (Low). The slope bound comes from the Table 596 band, which bounds the first-order term. A crystal outside that band, or a different cut, re-opens section 3.4.2.
10. **(Revision 2) The crystal temperature is the thermal model's MAIN node.** That node lumps the main-bay air, the main board and the Pico 2 (c_main 40 to 90 J/K). The crystal's own lag behind the node is not credited. The local Pico 2 step (0.03 W, 47 K/W) is an estimate taken in full, and the band is a one-at-a-time RSS, as in the thermal note. M-2 measures the result directly.
11. **(Revision 2) Continuous transmit bounds the heating.** The heating case keys the transmitter for the whole 190 s window, which REQ-SYS-055 and the keyer never allow (13 s key-downs at most), so it bounds any keying pattern from above. The cooling case starts from the continuous steady state, which is not reachable in service either.
12. **(Revision 3) The TCXO has no sourced slope.** The TG2520SMN brief sheet gives only the +/-0.5 ppm band, so the TCXO temperature term is the full 1.0 ppm band at every ratio age, including the fresh ratio at interval 12. That is the reason for the 2.5 ppm interval-12 allocation and its 260.0 Hz margin. A full datasheet with a slope or a curve would shrink the term; M-2(a) measures the combined change directly. The brief sheet is a 2-page summary ("please contact us for requirements not listed"); the full datasheet is still TS-007 value-of-information item 5.
13. **(Revision 3) The TCXO step is a coefficient bound with conditions.** The 0.4 ppm step takes each of fo-Load and fo-VCC at twice its limit, on the condition that both states stay inside the rated load and supply ranges. The squaring stage is not designed yet (INSP-110 finding-25), so the condition is a requirement on it (WP-PDR-20b, 37, 38). A stage that pulls the load outside 10 kOhm // 10 pF +/-10 % re-opens section 3.4.2. M-2(b) measures the step.
14. **(Revision 3) Settle residual and M-1(c).** S_RAMP = 5 Hz is an allocation with no source value; the Si5351A data sheet gives "Glitchless frequency changes" and TFREQ 10 us, which suggest a microsecond-scale tail, but not for an MSNA change. M-1(c)'s resolution (0.63 Hz per 1 ms window) is computed for the proposed beat fixture from the reference-period quantization of the flip-flop; the reference's own short-term stability over a 1 ms window is assumed much better than 1 Hz and is to be shown in the fixture check on the bench list. The linear-tail bound of two reference periods (ST-1) is the INSP-111 reviewer's bound for a charge-pump PLL whose phase error is inside one reference period; the Si5351A loop is not documented.
15. **(Revision 3) Observation outside this revision (rule C1).** The TG2520SMN brief sheet also gives a frequency tolerance of +/-1.5 ppm after reflow at +25 C, first-year aging of +/-0.5 ppm at 25 MHz, and +/-0.1 ppm each for load and supply. Summed with the +/-0.5 ppm band, that is 2.7 ppm uncalibrated, against the 1.5 ppm uncalibrated-total allocation of section 3.2 (the TS-007 R-M3 acceptance test) and its 0.1 ppm supply-and-load share. Section 3.2 and case C-8 are not re-examined in this revision, which fixes only the Major findings of the WP-PDR-20a reviews. The observation is sent to the lead SE (section 5 is unchanged for it). **Revision 4:** INSP-111 raised it as finding-13 (Major). Section 3.5 now gives the A5 reference budget, and sections 3.2, 4 and 5 are qualified for A5.
16. **(Revision 4) The fo-TC reference temperature is not stated.** The brief sheet gives "+/-0.5 x 10-6 Max. / -40 C to +85 C" with no reference. Section 3.5 carries both readings, and the 1.0 ppm window governs. That reading puts an uncalibrated unit 33.6 Hz outside the band (RB-1), which the ref25 reading does not (40.4 Hz inside). The full datasheet decides (TS-007 value-of-information item 5; request to WP-PDR-38).
17. **(Revision 4) The calibration range and the calibration temperature.** The +/-1.5 ppm range of RB-3 corrects the +25 C tolerance only. A calibration made away from +25 C, or a re-calibration after aging (RSK-002 step S4), can need up to the uncalibrated total, 2.7 or 3.2 ppm. The option (b) guard is computed for +/-1.5 ppm. A wider range needs a wider guard, by the same method (`guard_needed` in the checker). The calibration procedure (operations handbook, RSK-002 step S4) should state its temperature.
18. **(Revision 4) Option (c) arithmetic.** delta <= 0.972 ppm rests on the correct-calibration residual of 2.0 ppm (RB-3). That residual includes the full 1.0 ppm band change and the 0.4 ppm step, so it is not reduced by the ref25 reading. The factory offset is itself a measurement; its own error is the 0.1 ppm calibration uncertainty, and a wrong factory measurement is outside what the integrity check can catch. It is covered only by the verified procedure.

## 7. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/freq_budget.py --plot
```

Expected: 35 PASS, 0 FAIL, 4 INFO lines, exit status 0 (revision 1, run 2026-09-27). The figure `docs/reviews/PDR/figures/frequency-budget.png` has two panels:
- the edge margins against the REQ-TX-006 offset, with the 750 Hz TBR, the 825.0 Hz limit and the F7 cases marked;
- the healthy disagreement and the largest undetected true error per route and interval (R3 at the 5 kHz threshold, R1 at the smallest threshold that avoids false trips), against the 5 kHz threshold and the 10 kHz REQ-SYS-154 limit.

The author opened and inspected it after two layout corrections (overlapping labels). Revision 1 re-rendered it and moved the two limit labels into the legend after one inspection showed them over the bars.

**Revision 2 (section 3.4):**

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-01
```

Expected: 23 PASS, 0 FAIL, 10 INFO lines, exit status 0 (run 2026-09-29, about 5 s). The run directory `hardware/sim/freq/results/r3a5-20260929-01/` holds `checker-output.txt`, `results.json` (every case, the relock and freshness summaries, the thermal cases and tornado, the buffer lines), a copy of the script and four figures:
- `relock-sequence.png`: the key-down timelines (TS-012, latest with the ramp kept, latest with the ramp at 12 ms, the interval-13 fallback) and the sourced timing values against the settle budget on a log scale;
- `ratio-freshness.png`: the MAIN-node change over the over (both A5 layouts, three ambients, heating and cooling) and the drift bound against the ratio age, with the 1 ppm and 6.5 ppm allocations and the two ceilings;
- `xosc-slope.png`: the admissible AT-cut curves in the Table 596 band and the slope envelope in service;
- `r3-budget-and-buffer.png`: d and T + d per check against T and 10 kHz, and the 25 MHz harmonics against the receive windows.

`freq_budget.py` is unchanged and still gives 35 PASS, 0 FAIL. The author opened each revision 2 figure after rendering and re-rendered two of them after one inspection: labels over the title in `r3-budget-and-buffer.png`, and the 12 ms label over the title in `relock-sequence.png`.

**Revision 3 (section 3.4 and the A5 rows of section 3.1; superseded by the revision 4 run, which reproduces every revision 3 case line and figure):**

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-02
```

Expected: 38 PASS, 0 FAIL, 14 INFO lines, exit status 0 (run 2026-09-29, about 5 s). The run `r3a5-20260929-01` is kept as the revision 2 record and is superseded. The run directory `hardware/sim/freq/results/r3a5-20260929-02/` holds `checker-output.txt`, `results.json` (as revision 2, plus the `settle` summary with the A5 guard, the TCXO terms, both allocations, the M-2 limits and the FC0 times), a copy of the script and five figures:
- `relock-sequence.png`: the key-down timelines on the 2^n x 1 us counts (TS-012, the proposed 1.9 ms deadline with the ramp at 10 ms, the latest with the ramp at 12 ms, the TS-012 fallback with its 0.308 ms from PA_EN to the 11.5 ms ramp, red) and the sourced timing values against the 0.35, 1.25 and 3.25 ms settle budgets on a log scale;
- `ratio-freshness.png`: the MAIN-node change over the over, and the ratio drift bound (XOSC plus the 1.4 ppm TCXO terms, with the XOSC part dotted) against the ratio age, with the 2.5 and 8.0 ppm allocations, the 4.26 and 17.77 ppm ceilings, A_kd = 10 s and its 11.8 s limit, and 7.52 ppm at W;
- `xosc-slope.png`: unchanged in content;
- `r3-budget-and-buffer.png`: d of 4 740 and 3 554 Hz and T + d of 9 740 and 8 554 Hz against T and 10 kHz; the 25 MHz harmonics against the receive windows;
- `settle-and-guard.png` (new): the 2 891 Hz tail bound on a count against T = 5 kHz, and the A5 upper-edge stack (370.0 + 5 + 5 + 750 Hz, margin 70.0 Hz) with the M-1(c) resolution and pass criterion.

The author opened each revision 3 figure after rendering. Two changes followed one inspection: the A_kd limit label now floors as the checker text does (11.8 s, not 11.9 s), and two stray zero-width bars were removed from `settle-and-guard.png`.

**Revision 4 (section 3.5; this run governs):**

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-03
```

Expected: 43 PASS, 0 FAIL, 24 INFO lines, exit status 0 (run 2026-09-29, about 5 s). The 52 revision 3 case lines are unchanged, word for word (checked by `diff` against `r3a5-20260929-02/checker-output.txt` with the new lines removed). New: KA-R5, KA-R6 (known answers) and RB-0 to RB-8. The run `r3a5-20260929-02` is kept as the revision 3 record and is superseded. The run directory `hardware/sim/freq/results/r3a5-20260929-03/` holds `checker-output.txt`, `results.json` (as revision 3, plus `reference_a5`: the uncalibrated totals on both readings, the correct-calibration residual, each case's reference error and edge margin, the option (b) guards, the option (c) delta, the two-unit offsets and the C-10 re-read), a copy of the script and six figures. The five revision 3 figures are byte-identical to those of `r3a5-20260929-02` (same SHA-1). The new one:
- `reference-budget-a5.png`: left, the reference error of each section 3.5 case against the 1.5 ppm R-M3 allocation, the 2.5 ppm REQ-SYS-010 and identity 2 limit and the 2.972 ppm A5 guard limit (G-6); right, the margin of the -60 dB point inside the band for the same cases (green inside, red outside); footer, the option (b) guards and the option (c) rule on a rejected value.

`freq_budget.py` is unchanged and still gives 35 PASS, 0 FAIL. The author opened `reference-budget-a5.png` after each render. Three changes followed inspection: the legend moved off the lowest bar, and value labels clear of the limit lines; the G-6 label floored to 2.972 ppm as the checker text is; the right-hand axis label shortened so that it is not cut off at the figure edge.

## 8. Per-case index

C-1 to C-7 band edges; C-8 to C-10 reference identities; C-11 sample; C-12w threshold within the REQ-SYS-182 window; C-12 no false trip per interval (R3); C-13 R1 per interval (informational, with the limits R1 needs); C-14 changeover time per alternative; C-15 transmit detection time; C-16 REQ-SYS-154 true-error limit per interval (R3); C-16a FC0 accuracy ceiling (informational); C-17 plausibility bound (informational); C-18 TC-SYS-101 12 kHz injection per interval; U-1 unlocked at key-down per alternative; U-2 unlocked during transmission. The REQ-SYS-154 cases are: off-frequency at key-down C-12.iv12, C-16.iv12, C-18.iv12; off-frequency during transmission C-12.iv13, C-16.iv13, C-18.iv13, C-15; unlocked at key-down U-1; unlocked during transmission U-2. Checker output lines carry the same ids.

Revision 2 (`r3_a5.py`):
- KA-R1 to KA-R3 known answers.
- RL-0 to RL-8 relock: sources; writes at 400 kHz, 256 kHz and 100 kHz; the LOL_A read; L max per sequence; the TFREQ and TRDY readings; the verdict.
- FR-1 to FR-6 freshness: slope bound; A_kd; the receive age; the window; the drift over the over; the interval-12 and interval-13 ceilings.
- B-11, B-12.iv12 and iv13, B-15, B-16.iv12 and iv13, B-18.iv12 and iv13, B-19: the A5 budget and the refresh time.
- BL-1 and BL-2: the squaring-stage lines in receive and in transmission.

Revision 3 (`r3_a5.py`, run `r3a5-20260929-02`):
- KA-R3 (now: the 2^n x 1 us FC0 times) and KA-R4 (the A5 guard with no settle residual reproduces C-2).
- RL-4d proposed L_max deadline; RL-6f the TS-012 fallback as written.
- ST-1 to ST-3 what the key-down count verifies: the linear-tail bound on a count, the slewing detection time, the M-1(c) resolution.
- G-1 to G-7 the A5 band-edge guard with the settle residual (section 3.1).
- FR-T the TCXO terms; FR-7 the M-2 limits; B-16a.iv12 and iv13 the A5 FC0 accuracy ceilings.

Revision 4 (`r3_a5.py`, run `r3a5-20260929-03`):
- KA-R5 (identity 2 with the section 3.2 allocations reproduces C-8; the A5 guard function at 2.5 ppm reproduces G-2) and KA-R6 (the needed-guard function leaves exactly zero margin at the governing edge).
- RB-0 the TG2520SMN terms and uncalibrated totals; RB-1 no calibration; RB-2 a constant wrong within +/-0.9 and +/-1.5 ppm; RB-3 a correct calibration (REQ-SYS-010, TPM-006); RB-4 the +/-0.9 ppm range held; RB-5 no fixed range meets both; RB-6a to RB-6c the three options; RB-7 the A5 two-unit offset; RB-8 the section 3.2 C-10 re-read. Each of RB-1 and RB-2 is given for both readings (suffix `.ref25`, `.pp`).

For A5 the REQ-SYS-154 cases are: off-frequency at key-down B-12.iv12, B-16.iv12, B-18.iv12 with FR-2; off-frequency during transmission B-12.iv13, B-16.iv13, B-18.iv13, B-15 with FR-6; unlocked at key-down U-1 (section 3.4.4, RL-3); unlocked during transmission U-2, open on the I2C conflict of section 3.4.4.

## Change history

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial issue, frozen for its first review (freeze F0, rule C2) | WP-PDR-20 wave 1a |
| 1 | 2026-09-27 | Section 3.3: measured threshold T = 5.0 kHz distinct from the REQ-SYS-154 true-error limit, with the no-false-trip and no-missed-trip conditions, the FC0 accuracy ceiling and the effect on TC-SYS-101 (cases C-12w, C-16, C-16a, C-18); unlocked-synthesizer cases at key-down and during transmission with the lock-detect means and time budget (U-1, U-2). Sections 1, 2, 4, 5, 6, 7, 8 and the figure follow. Minor findings 5 to 7 are not addressed in this revision (rule C1) | INSP-056 finding-1 and finding-2 (Major) |
| 2 | 2026-09-29 | WP-PDR-20a, for A5 (TS-012 revision 7 decision; D-12, D-17, D-18). New section 3.4 with the checker `r3_a5.py` (run `r3a5-20260929-01`). Si5351A relock read from the data sheet Rev. 1.3 and AN619 Rev. 0.8: no relock time specified; the lock-gated changeover with L_max 2.0 ms; Fast-Mode I2C constraint; M-1. Ratio freshness: 6.12 ppm over the longest over, triggering the TS-012 condition as worded; the budget closes with A_kd = 10 s at the key-down check and 6.5 ppm at interval 13; R-FRESH-1, R-FRESH-2; M-2. Squaring stage and the 150 MHz line; LOL_A as the A5 lock-detect indication; the U-2 I2C conflict. Header, sections 1, 2, 4 to 8 follow. Sections 3.1 to 3.3, `freq_budget.py` and `frequency-budget.png` unchanged. INSP-056 Minor findings 5 to 7 and 9 not addressed (rule C1) | WP-PDR-20a (plan revisions 6 and 7, section 3.0 row 20); TS-012 section 10 revisit conditions of revision 6 |
| 3 | 2026-09-29 | WP-PDR-20a Major findings only (rule C1). Checker `r3_a5.py` revised, run `r3a5-20260929-02` (38 PASS, 0 FAIL, 14 INFO). (1) Ratio drift with the TCXO's own terms from the TG2520SMN brief sheet: 1.0 ppm temperature band (no slope given) and a 0.4 ppm load and supply step between the stage-on refresh and the stage-off check, with the load and supply conditions on the squaring stage; allocations 2.5 ppm at interval 12 (A_kd 10 s kept, limit 11.8 s) and 8.0 ppm at interval 13; margins 260.0 and 1 446.0 Hz; A5 FC0 acceptance limits 532.5 and 430.7 Hz; M-2 split into (a) ratio change, 7.4 and 1.9 ppm, and (b) transmit-state steps. (2) FC0 counts at 2^n x 1 us: L_max 1.9 ms, RL-5 3.904 ms against the 4 ms TS-012 threshold, RL-6 -0.192 ms, fallback 0.308 ms, M-1 branches 1.25 and 3.25 ms, U-1 7.096 and 7.996 ms, refresh 82.8 ms, B-15 46.4 ms. (3) Section 3.4.1 restated: the count bounds its own mean; a linear tail (2 891 Hz at most) passes it; the settle residual S_RAMP = 5 Hz at the ramp is a named term of the A5 guard in section 3.1 (G-1 to G-7: margin 70.0 Hz, REQ-TX-006 limit 820.0 Hz) and is closed by the new time-resolved M-1(c); RL-8 restated. Header, sections 1, 2, 4 to 8 follow; new figure `settle-and-guard.png`. `freq_budget.py`, sections 3.2 and 3.3 and `frequency-budget.png` unchanged. Minor findings of INSP-056 (5 to 7, 9, 10, 13 to 17) and INSP-111 (8 to 12) not addressed (rule C1); section 6 item 15 records an observation on the TG2520SMN tolerance for the lead SE | INSP-056 iteration 3 re-issue 1 finding-11 and finding-12 (Major); INSP-111 iteration 2 finding-7 (Major) |
| 4 | 2026-09-29 | INSP-111 finding-13 (Major) only (rule C1). Checker `r3_a5.py` revised, run `r3a5-20260929-03` (43 PASS, 0 FAIL, 24 INFO; every revision 3 line unchanged). New section 3.5, the A5 reference budget with the TG2520SMN brief-sheet terms on two readings of the fo-TC band (1.0 ppm window governs): uncalibrated 2.7 or 3.2 ppm against R-M3 1.5 ppm; REQ-SYS-010 holds after a correct calibration (2.034 ppm) with a range of at least +/-1.5 ppm; identity 2 fails at every range; a constant wrong within +/-0.9 ppm puts the -60 dB point 92.8 to 166.8 Hz beyond 148.000 MHz; three options named, not chosen (a TCXO that meets R-M3; a 1.4 or 1.5 kHz guard CR; a software integrity check on the calibration value, delta at most 0.972 ppm). Section 3.2 marked superseded for A5; section 4 REQ-SYS-010, REQ-SYS-008 rows and TPM-006 qualified; section 5 WP-PDR-35 (+/-0.9 ppm) and WP-PDR-16b (K4) requests held open for A5, with new revision 4 rows (lead SE for the owner, 35, 16b, 54, 20b, 29, 18, 38); section 2 inputs, section 6 items 15 to 18, sections 7 and 8 follow; new figure `reference-budget-a5.png`. INSP-111 finding-7 stays Verified; nothing it rests on changed. Minor findings of INSP-056 and INSP-111 (8 to 12, 14, 15) not addressed (rule C1) | INSP-111 iteration 3 finding-13 (Major) |
