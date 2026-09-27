# UI design analysis: tuning law, menu depth, display layout, legibility, fault and ID timing, defaults

| Field | Value |
|---|---|
| Product | Analysis note of WP-PDR-33 (`docs/plan/pdr-work-plan.md` section 3.7), G14 TBR group of plan section 10.2 (design part) |
| Status | Draft, revision 2: fixes the two Major findings of review iteration 1 (INSP-072 findings 1 and 2) for the delta iteration (plan rule C1), frozen again at F0 (rule C2). The Minor findings of iteration 1 are not addressed in this revision. It proposes values and a preliminary UI design; it changes no requirement or interface file (plan section 5.3) |
| Author | Claude, ME/UI designer role, WP-PDR-33 author invocation, 2026-09-27 |
| Review record (plan section 3.7) | `docs/reviews/PDR/checklists/analysis-ui-design.md` (INSP-072, independent reviewer, `peer-review-checklist-analysis.md`; the renders also against `peer-review-checklist-visual-product.md` items) |
| Analysis kind | timing, other (legibility, menu depth); criticality: mission-critical (`SW-DISPLAY`, `docs/process/07-software-engineering-plan.md` section 14.2 row `SW-DISPLAY`) |
| Model and checker | `docs/design/analysis/ui-design/ui_model.py`; `docs/design/analysis/ui-design/check_ui_design.py` |
| Outputs | `docs/design/analysis/ui-design/ui-design-results.json`; plot `docs/design/analysis/ui-design/ui-tuning-step-law.png`; display renders `docs/reviews/PDR/figures/display-layout-{receive,transmit,tune,key-inhibit,id-reminder,menu-level-1,menu-level-2-keyer,menu-level-2-keyer-straight,cal-trim}.png` |
| Reproduce | `cd /Users/robinonsay/rust/cwht && .venv/bin/python docs/design/analysis/ui-design/check_ui_design.py` (exit 0, 41 assertions, about 2 s) |
| Credit | Developer evidence (`docs/process/05-configuration-and-data-management.md` section 9.1): the model has no TV record (section 10) |

## 1. Question and scope

The note fixes the preliminary UI design that the G14 TBRs wait on (menu tree, tuning step table, display layout, UI timing) and checks each TBR value against it. Requirement text at `main` blob `f128235e` (`docs/requirements/sys/requirements.json`) and `f9141160` (`docs/requirements/sw/sw-keyer/requirements.json`):

| Id | Value under study (TBR) | `tbr.plan` step this note executes |
|---|---|---|
| REQ-SYS-058 | step from 10 Hz to 10 kHz with rotation rate | "fixes the step table after a HostUnit usability run" |
| REQ-SYS-061 | frequency characters at least 4.0 mm high | "the PDR display layout fixes the character height" |
| REQ-SYS-062 | every setting within two menu levels | "the UI design at PDR fixes the menu tree" |
| REQ-SYS-067 | distinct cause message within 1 s of detection | "the UI response analysis at PDR fixes the latency with the display refresh rate" |
| REQ-SYS-068 | ID reminder 9 min 00 s +/-5 s after the first transmission following the previous reminder | "confirms the 9 min lead and its tolerance" |
| REQ-SYS-136 | defaults Iambic A, 15 WPM, 600 Hz, 8-dit hang, 5 ms envelope | "the PDR keyer design confirms them" |
| REQ-SYS-164 | 144.000 to 148.000 MHz within 30 s at 2 rev/s | "fixes the step table and crossing time after a HostUnit usability run" |
| REQ-SYS-165 | frequency legible at 0.5 m under 300 lux or more, no backlight | "the PDR display design fixes the illuminance floor" |
| REQ-SW-KEYER-014 | keyer timing held at 50 display frames/s and 50 detents/s per encoder | "confirms the 20 ms full-frame time and the 50 detents/s decode rate" |

REQ-SW-KEYER-036 (G14) is in `docs/design/analysis/keyer-host-study.md` section 6.7. REQ-SW-KEYER-009 and 039 (G14 HIL) are WP-PDR-40.

## 2. Inputs

| # | Input | Value | Source |
|---|---|---|---|
| I-1 | Display | Sharp LS013B7DH03, 128 x 128 dots, pitch 0.18 mm, viewing area 23.04 mm square; reflectivity 14 percent minimum; contrast ratio 21 minimum; fSCLK 1.1 MHz maximum; full frame 16.8 ms at 1.1 MHz; no backlight | `docs/research/display-and-ui-parts.md` (blob `11c497ba`) F1, F2 (High); SRR decision 77 (concept section 14 item; ConOps Appendix C "Display and controls") |
| I-2 | Encoders | Bourns PEC11R-4215F-S0024: 24 detents, 24 pulses (one quadrature cycle, 4 edges per detent), bounce 2.0 ms maximum, rated 60 RPM | F12 (High); ADR-006 |
| I-3 | Buttons | Omron B3F-1052, bounce 5 ms maximum | F16 (High) |
| I-4 | Control set | two knobs with push, two buttons, power switch | REQ-SYS-057; ADR-006 |
| I-5 | Status set | frequency, power step, key mode, keyer speed, battery state, transmit state outside menus in Receive, Transmit-keyed, Tune | REQ-SYS-060 |
| I-6 | Fault and inhibit texts | Table 3.4-4 rows 1 to 20 | `docs/conops/conops.md` (blob `6c3fbb2b`) section 3.4 |
| I-7 | KEY inhibit report latency | 20 ms to the display interface | REQ-SW-KEYER-023 |
| I-8 | Identification rule | 47 CFR 97.119(a): "at least every 10 minutes during a communication" | corpus `47cfr-97.119.md`, eCFR issue 2026-09-23 |
| I-9 | Settings and ranges | speed 5 to 50 WPM in 1 WPM steps (REQ-SYS-041); hang 3 to 30 dits (REQ-SYS-044); sidetone 300 to 1000 Hz in 10 Hz steps (REQ-SYS-045); envelope 3 to 8 ms (REQ-SYS-014); modes (REQ-SYS-040); operator-set timing tunables only switchpoint and debounce (SRR decision 48) | requirement file; ConOps section 3.5.1 item 3 |
| I-10 | Separation reminders | 0.5 W 0.2 m, 1 W 0.3 m, 2 W 0.4 m, 5 W 0.6 m, tune 1.0 m (TBR, REQ-SYS-069) | ConOps section 3.5.1 item 5 |
| I-11 | Window geometry | 24.0 x 24.0 mm through-window with a 1.0 mm PC or PMMA lens, recess at most about 2 mm | F23 (Medium) |

## 3. Preliminary UI design

### 3.1 Controls

| Control | Status screen | Menus |
|---|---|---|
| Tuning knob, turn | frequency, with the rate-dependent step of section 3.4 | move the cursor; change a value in edit |
| Tuning knob, push | none | select; confirm an edit or an action |
| Volume knob, turn | headphone level (REQ-SYS-059) | headphone level |
| Volume knob, push | mute | mute |
| MENU button | enter level 1 | back one level; from level 1 back to status |
| FUNC button | press: the tuning knob sets keyer speed for 5 s (REQ-SYS-041 without a menu) | none |
| MENU and FUNC held 2 s | guest lock set or release, then a tuning-knob push to confirm (REQ-SYS-066 two-step action) | not accepted |
| FUNC held while switching on | opens the service calibration screen (section 3.3, REQ-SYS-035), after Self-test | not applicable |

Button inputs are debounced at 20 ms (above the 5 ms B3F bounce, I-3), never sharing the keyer's key-input filter (display report UI-BTN-01 candidate). The distinct-event rule of REQ-SW-KEYER-039 governs the confirmation steps; its interval is WP-PDR-40.

### 3.2 Screens and layout

Nine renders, each at 4x with the true 128 x 128 dot grid (inspected; section 5):

| Render | Content |
|---|---|
| `display-layout-receive.png` | line 1 key mode code and speed ("IA 15WPM"); frequency in 23-dot seven-segment digits "146.520.00" (MHz.kHz.tens of Hz); "RX" and the power step; battery voltage and bar; separation reminder "KEEP 0.3M"; call sign; soft labels |
| `display-layout-transmit.png` | as receive, with the transmit state inverted ("TX", "5W") and the 5 W reminder "KEEP 0.6M" |
| `display-layout-tune.png` | as transmit, "TUNE 0.5W", "KEEP 1.0M" and the countdown "ENDS 4.2S" |
| `display-layout-key-inhibit.png` | Table 3.4-4 row 1 as an inverted two-line banner "KEY CLOSED / CHECK PLUG", "TX OFF" |
| `display-layout-id-reminder.png` | inverted banner "ID NOW / N0CALL" and "ID EVERY 10 MIN" |
| `display-layout-menu-level-1.png` | level 1: KEYER, AUDIO, TX, SETUP; the selected row inverted |
| `display-layout-menu-level-2-keyer.png` | level 2 KEYER: four visible rows of eight, the selected setting's value in an inverted bar "<IAMB A>" |
| `display-layout-menu-level-2-keyer-straight.png` | level 2 KEYER with MODE in edit on a Straight-input value "<STR RING>", the widest bracketed MODE value (section 3.3) |
| `display-layout-cal-trim.png` | service calibration screen: RX TRIM selected, range and step lines, value bar "<-30 HZ>", soft labels EXIT and STORE |

Text other than the frequency uses a 5 x 7 dot font drawn at 2x (10 x 14 dots, 2.5 mm high, 10 characters per line) so that status items and menus read at about 0.35 m; the soft-key labels use 1x. Key-mode codes: SO Straight keyed from the tip only (Straight-on-tip), SR Straight from the ring only, ST Straight from either contact, IA, IB, UL Ultimatic, BG Bug. Frequency digits are 11 x 23 dots with a 3-dot stroke; eight digits and two points occupy 105 of 128 dots.

### 3.3 Menu tree (REQ-SYS-062)

Level 0 is the status screen; level 1 is a category; every setting, action and view is an item at level 2, edited in place (a value change or a confirmation is a step inside the item, not a level).

| Level 1 | Level 2 items (kind) | Governing source |
|---|---|---|
| KEYER | MODE, SPEED, SWAP, SWITCHPT, MAKE MS, BREAK MS, HANG, PRACTICE (settings) | REQ-SYS-040, 056, 041; REQ-SW-KEYER-002 (MODE values below); ConOps 3.5.1 item 3 paddle swap; REQ-SW-KEYER-009; REQ-SYS-048, 162 (decision 48); REQ-SYS-044; Table 3.4-3 PRACTICE |
| AUDIO | TONE HZ, TONE LVL, KEEP UNLK (settings); UNLOCK (action) | REQ-SYS-045; F14 sidetone level; REQ-SYS-170; REQ-SYS-074 |
| TX | POWER, ENVELOPE (settings); TUNE (action); KEYDN TIME (view) | REQ-SYS-063 (5 W after a separate confirmation); REQ-SYS-014; ConOps T12; REQ-SYS-171 |
| SETUP | CALL (setting); BENCH TEST, RESET CFG (actions); INFO (view) | REQ-SYS-006; REQ-SYS-179; REQ-SYS-136 |

**MODE values (INSP-072 finding-1).** The Straight-input setting of REQ-SW-KEYER-002 ("from the tip, the ring or either contact") is carried by three Straight values of KEYER > MODE:

| Value | Status code | Meaning | Source |
|---|---|---|---|
| IAMB A | IA | Iambic A | REQ-SYS-040 |
| IAMB B | IB | Iambic B | REQ-SYS-040 |
| ULTIMATIC | UL | Ultimatic (shown without brackets: the bracketed form exceeds the bar) | REQ-SYS-040 |
| BUG | BG | Bug | REQ-SYS-040 |
| STR TIP | SO | Straight keyed from the tip only; the mono-plug choice (Straight-on-tip) | REQ-SW-KEYER-002 tip; REQ-SYS-163 |
| STR RING | SR | Straight keyed from the ring only | REQ-SW-KEYER-002 ring |
| STR BOTH | ST | Straight keyed from either contact | REQ-SW-KEYER-002 either |

One MODE selection and its confirmation therefore set both the key-input mode (REQ-SYS-056; accepted with a closed input, REQ-SYS-163) and the Straight input. With a mono plug the operator needs one menu path, not two, while the KEY inhibit is showing. A separate Straight-input item would add a 25th item and a second selection before the mono plug is harmless. Every value fits the 124-dot edit bar at the 2x font (checker; render `display-layout-menu-level-2-keyer-straight.png`).

**Calibration trim (INSP-072 finding-1).** The per-unit receive filter-centre trim of REQ-SYS-035 is outside REQ-SYS-062, because it is not an operator setting: NGO-012 states that "the filter-centre offset is a per-unit calibration stored at acceptance over +/-500 Hz in 10 Hz steps, not an operator control". A setting inside the operator tree could be changed by any operator or guest. The trim therefore sits on a service calibration screen, the "calibration menu" of the REQ-SYS-035 verification note and TC-SYS-023. The screen opens when FUNC is held while switching on, after Self-test, and exits on MENU or at switch-off. Its one item, RX TRIM, sets -500 to +500 Hz in 10 Hz steps with the tuning knob and stores the value after a tuning-knob push (render `display-layout-cal-trim.png`). It is one level from its entry and changes no operator setting.

Outside the menus: frequency, volume, guest lock and the speed shortcut (section 3.1). The operator tree holds 24 items in all (20 menu items and 4 direct controls), recounted with the MODE values above; none is deeper than level 2. The calibration screen holds one more item outside the operator tree. The longest category has eight items (two screens of four).

### 3.4 Tuning law (REQ-SYS-058, REQ-SYS-164)

The step per detent follows the rate of the last detent interval; a detent after a pause longer than 0.5 s is a slow detent. At steps of 1 kHz and more the frequency lands on the step grid in the direction of rotation, so the display ends in zeros; tuning stops at 144.000.00 and 148.000.00 MHz.

| Detent rate (per s) | Knob rate (rev/s, 24 detents) | Step |
|---|---|---|
| below 5 | below 0.21 | 10 Hz |
| 5 to below 10 | 0.21 to 0.42 | 100 Hz |
| 10 to below 20 | 0.42 to 0.83 | 1 kHz |
| 20 and above | 0.83 and above | 10 kHz |

Encoder decoding: the 1 kHz sampler (07 section 19, WP-SW-02 SIO snapshot) feeds a Gray-code transition table, which rejects bounce (a bounce toggles between two adjacent states with a net count of zero), so no time debounce is applied to the encoder lines.

### 3.5 UI timing

The UI task runs every 20 ms; it redraws only lines that changed and pushes at most 25 frames per second (one full frame is 16.8 ms of SPI at 1.1 MHz, I-1). The frequency shown is the value written to the synthesizer, never the tuning request (07 section 14.2 row `SW-DISPLAY` (g)).

### 3.6 Fault and inhibit messages (REQ-SYS-067)

Each Table 3.4-4 cause with a display text gets a two-line banner of at most 10 characters per line, drawn over lines 3 and 4 of the status screen (the key-inhibit render). The ConOps texts are longer than 10 characters, so the banner uses the short form and the handbook gives the long form (request R-U4):

| Row | ConOps text | Banner |
|---|---|---|
| 1 | KEY CLOSED: check plug | KEY CLOSED / CHECK PLUG |
| 2 | KEY? | KEY? / OPEN KEY |
| 3 | PADDLE? | PADDLE? / RELEASE |
| 4 | HOT: wait | HOT / WAIT |
| 5 | TX off: low batt | TX OFF / LOW BATT |
| 6 | TX inhibited (USB) | TX OFF / USB POWER |
| 7 | TX guard | TX OFF / BAND EDGE |
| 8 | Lock icon "RX only"; "PRACTICE" | RX ONLY / GUEST; PRACTICE / TX OFF |
| 9 | RESET: <reason> | RESET / <reason> |
| 10 | RESET REPEATED: switch off and report | RESET X2 / SWITCH OFF |
| 11 | The failed item | SELFTEST / <item> |
| 12 | TX CUTOFF: report to owner | TX CUTOFF / REPORT |
| 13 | CELL SENSE: report to owner | CELL SENSE / REPORT |
| 14 | CELL: check polarity; CELLS mismatched | CELL / POLARITY; CELLS / MISMATCH |
| 15 | CHARGER: report to owner | CHARGER / REPORT |
| 16 | USB fault | USB FAULT / UNPLUG |
| 17 | CHG hold: cold; CHG hold: hot | CHG HOLD / COLD; CHG HOLD / HOT |
| 18 | BATT EMPTY | BATT EMPTY / CHARGE |
| 19 | CELL HOT: powering down | CELL HOT / POWER DOWN |

Fault types that the REQ-SYS-067 rationale names ("configuration and sensor faults (REQ-SYS-088, 089, 134, 155, 156, 167)") and that Table 3.4-4 has no row for (INSP-072 finding-2). REQ-SYS-088 is row 13, and REQ-SYS-089 and REQ-SYS-167 are row 15. The other three get banners here, and their rows are requested from the ConOps writer (R-U6):

| Governing id | Detected fault | Proposed class | Banner |
|---|---|---|---|
| REQ-SYS-155 | PA temperature reading outside its plausible range (open or shorted sensor) | Latched (Fault-safe, as the requirement states) | PA SENSOR / REPORT |
| REQ-SYS-156 | Forward-power reading implausible for the ALC drive during key-down | Latched (Fault-safe, as the requirement states) | PWR SENSOR / REPORT |
| REQ-SYS-134 | A stored setting was corrupt or out of range and was replaced by its default at load | Indication, not transmit-stopping: shown after Self-test until the next control input | SETTINGS / DEFAULTED |

All 25 banners (22 for Table 3.4-4 rows 1 to 19 and 3 added) are distinct (checker); row 20 has no display (the unit goes dark). The rows 21 to 23 that the ConOps holds TBR (backstop, hardware over-temperature cut-off, frequency verification) get banners when the ConOps enters them.

### 3.7 Identification reminder (REQ-SYS-068)

A reminder timer starts at the first key-down after power-on or after the previous reminder and shows the "ID NOW" banner 540 s later, with the call sign; the banner clears at the next key-down. No automatic identification is sent (REQ-SYS-007; SRR decision 21).

### 3.8 Defaults (REQ-SYS-136)

A configuration reset restores Iambic A, 15 WPM, 600 Hz sidetone, 8-dit hang and 5 ms envelope, with the separate safety defaults (1 W, REQ-SYS-064; 30 mVrms cap, REQ-SYS-074) and PRACTICE off (Table 3.4-3). GUEST is not changed by a reset (Table 3.4-3; ConOps forbidden property F6).

## 4. Assumptions

| # | Assumption | Direction | What would invalidate it |
|---|---|---|---|
| A-U1 | A character subtending 20 arcmin or more is legible for a numeric readout (a common human-factors design value; the standards that state it are not in the corpus) | Sets the REQ-SYS-061 check | The owner's reading test at the WP-PDR-40 session or the post-build Demonstration |
| A-U2 | Background luminance of 3 cd/m2 or more is enough for photopic reading (same basis as A-U1) | Sets the illuminance floor | As A-U1 |
| A-U3 | Luminance contrast ratio 3:1 or more (same basis) | Sets the lens finding | As A-U1 |
| A-U4 | Worst veiling reflection: a white surround (reflectance 0.8) seen in the specular direction of a plain lens | Conservative | An operator tilting the unit, which removes the specular image |
| A-U5 | Liquid-crystal optical response at most 500 ms at -10 C (the Sharp documents in hand give no response time) | Sets the fault-message budget | A cold response slower than 500 ms; 424 ms of margin remains |
| A-U6 | Rendering a banner into the frame buffer takes at most 2 ms | Small | Not critical |
| A-U7 | Pico 2 crystal within +/-50 ppm | Sets the ID reminder error | Any realistic crystal error is below 0.1 s over 540 s |
| A-U8 | Quadrature edges equally spaced (the PEC11R phase tolerance is not in the research) | Sets the encoder decode capacity | Phase error above 50 percent at 50 detents/s |
| A-U9 | Usability run operator: 2 rev/s until within 20 kHz, 0.75 rev/s until within 1.5 kHz, 0.4 rev/s until within 150 Hz, then 3 detents/s, with 0.3 s between phases | A scripted operator, not a person | The owner's session (WP-PDR-40) |
| A-U10 | The display is initialised in the boot path before the configuration load, so a REQ-SYS-134 replacement found at load is reported through the same path as any other detection (request R-U2) | Sets the REQ-SYS-134 latency | A boot order that loads the configuration before the display is ready; the banner would then wait for the display |

## 5. Validation

- The checker measures the frequency digits from the frame buffer (23 dot rows) rather than trusting the font constant, and asserts every value in sections 6 and 7.
- Every render was opened and inspected by the author: character shapes, the inverted bands, text fit inside 128 dots, the soft labels. Corrections made during inspection: spaces restored in "BAT 7.6V" and "KEEP 0.3M"; the cryptic key-down line on the transmit screen replaced by the call sign; the ID footer reworded. Revision 2 renders (`display-layout-menu-level-2-keyer-straight.png`, `display-layout-cal-trim.png`) inspected the same way: the widest bracketed MODE value "<STR RING>" fits the bar, and a render caption that overran the image width was wrapped onto two lines; the seven revision 1 renders are unchanged byte for byte.
- The tuning model's crossing times agree with hand calculation: at 2 rev/s (48 detents/s), 1 slow detent and 400 detents of 10 kHz, 400 / 48 = 8.33 s.

## 6. Results

### 6.1 Character height (REQ-SYS-061)

The frequency digits are 23 dots, 4.14 mm (23 x 0.18 mm), and subtend 28.5 arcmin at 0.5 m; the 4.0 mm requirement subtends 27.5 arcmin, above the 20 arcmin of A-U1. **Confirmed: 4.0 mm** (design 4.14 mm, margin 0.14 mm, less than one dot; a larger digit is possible in the free rows above and below the frequency if the owner asks for more margin).

### 6.2 Legibility without a backlight (REQ-SYS-165)

At 300 lux and the minimum reflectivity 0.14, the background luminance is 13.4 cd/m2 and the contrast ratio is the datasheet minimum 21:1 without a lens. A reflective display's contrast ratio does not change with illuminance; a lens adds a veiling reflection that scales with the illuminance too, so the ratio with a lens is also independent of it:

| Case at 300 lux | Background (cd/m2) | Contrast ratio |
|---|---|---|
| No lens | 13.4 | 21.0 |
| Plain 1 mm lens (n = 1.49, 3.9 percent per surface), white surround in the specular direction (A-U4) | 17.1 | 2.74 |
| Plain lens, room surround reflectance 0.3 | 13.6 | 5.06 |
| AR-coated lens, 0.5 percent per surface, white surround | 13.9 | 10.0 |

The illuminance floor is set by luminance: 3 cd/m2 (A-U2) needs 78.8 lux through a plain lens, so 300 lux is 3.8 times the floor. **Confirmed: 300 lux**, on the condition that the window lens is AR-coated or the specular case is accepted (the operator tilts the unit): the plain-lens specular case falls below 3:1 (limitation L-U2; request R-U1).

### 6.3 Menu depth (REQ-SYS-062)

Every one of the 24 operator settings, actions and views of section 3.3 is at level 2 or above, recounted with the Straight-input setting carried by the MODE values (every REQ-SYS-040 mode and every REQ-SW-KEYER-002 setting present, checker). The REQ-SYS-035 calibration trim is outside the operator tree for the NGO-012 reason of section 3.3, one level from its own entry. **Confirmed: two levels.**

### 6.4 Step table and band crossing (REQ-SYS-058, REQ-SYS-164)

Crossing 144.000 to 148.000 MHz at a steady rotation:

| rev/s | 0.5 | 0.75 | 0.83 | 0.84 | 1.0 | 1.5 | 2.0 | 3.0 |
|---|---|---|---|---|---|---|---|---|
| Crossing (s) | 333 | 222 | 201 | 19.8 | 16.7 | 11.1 | 8.33 | 5.56 |

At 2 rev/s: 8.33 s, 21.7 s inside the 30 s of REQ-SYS-164. Usability run (A-U9): from 146.520.00 to 144.057.30 MHz in 10.5 s and 275 detents, landing exactly (error 0 Hz); across the band to 147.999.99 MHz in 14.0 s, landing exactly (`usability_run`, `usability_run_full_band`; `ui-tuning-step-law.png`). **Confirmed: 10 Hz to 10 kHz with the table of section 3.4, and 30 s at 2 rev/s.** The table is a proposal for the owner's hands-on session (WP-PDR-40); a change of the rate thresholds does not change a requirement.

### 6.5 Fault message latency (REQ-SYS-067)

| Item | Worst (ms) |
|---|---|
| Detection to report (REQ-SW-KEYER-023; the same rule for the other causes) | 20 |
| Wait for the next 20 ms UI tick | 20 |
| Render the banner (A-U6) | 2 |
| Wait for a frame in flight | 16.8 |
| Write the changed lines (bounded by a full frame) | 16.8 |
| Optical response at -10 C (A-U5) | 500 |
| Total | 575.6 |

The budget holds for every message of section 3.6, the three added ones included. The REQ-SYS-155 and REQ-SYS-156 detections report through the same safe-state path. The REQ-SYS-134 detection happens at the configuration load, after display initialisation (A-U10). **Confirmed: 1 s** (margin 424 ms) over all 25 messages. TC-SYS-005 measures to the display chip-select; the optical part rests on A-U5.

### 6.6 Identification reminder (REQ-SYS-068)

The reminder shows between 0.027 s early (crystal, A-U7) and 0.58 s late (crystal, tick, two frames, optical response) against 9 min 00 s, well inside +/-5 s. The minimum lead to the 10-minute mark is 55 s; sending "DE N0CALL N0CALL" at 5 WPM takes 41.0 s. **Confirmed: 9 min 00 s +/-5 s.**

### 6.7 Defaults (REQ-SYS-136)

Each default lies on its range (15 in 5 to 50 WPM; 600 in 300 to 1000 Hz at 10 Hz steps; 8 in 3 to 30 dits; 5 in 3 to 8 ms; Iambic A a REQ-SYS-040 mode). The 8-dit hang at 15 WPM is 640 ms, longer than a 7-dit word space (560 ms), so the default keeps the transmitter in transmit between words of an over. With the keyer study's proposed squeeze limit, 15 WPM uses the 2 s term (20 dits = 1.6 s). **Confirmed.**

### 6.8 Keyer timing load (REQ-SW-KEYER-014)

The display bus can carry at most 59.5 full frames per second at 1.1 MHz; the design pushes at most 25 (section 3.5); the test load of 50 frames/s is twice the design and 84 percent of the bus. A 24-detent encoder at 2 rev/s (the REQ-SYS-164 condition) gives 48 detents/s; 50 detents/s covers it and exceeds the 60 RPM rating of I-2 (24 detents/s), so it is a stress load. At 50 detents/s each quadrature state lasts 5 ms, five 1 kHz samples (A-U8). **Confirmed: 50 frames/s and 50 detents/s per encoder.**

## 7. Per-case table (plan rule C7)

| Case | Governing id | Result | Margin |
|---|---|---|---|
| Frequency digits at 0.18 mm pitch | REQ-SYS-061 | 4.14 mm | 0.14 mm |
| 0.5 m at 300 lux, no lens, plain lens (two surrounds), AR lens | REQ-SYS-165 | section 6.2 table | 3.8 x luminance floor; contrast 5.06 to 21 except the plain-lens specular case 2.74 |
| Every setting, action and view, the Straight-input setting (tip, ring, either) included | REQ-SYS-062; REQ-SW-KEYER-002 | all at level 2 or above; the three Straight inputs are MODE values | 0 levels over |
| Filter-centre calibration trim | REQ-SYS-035 ("calibration menu"); NGO-012 | outside the operator tree; service calibration screen, one level from its entry | not applicable |
| Slow and fast turning; band crossing at 2 rev/s | REQ-SYS-058, REQ-SYS-164 | 10 Hz to 10 kHz; 8.33 s | 21.7 s |
| Each Table 3.4-4 cause with a text, and the REQ-SYS-134, 155 and 156 fault types | REQ-SYS-067 | 25 distinct banners; 575.6 ms worst | 424 ms |
| Reminder at 540 s after the first key-down | REQ-SYS-068 | -0.027 s / +0.58 s | 4.4 s |
| Configuration reset | REQ-SYS-136 | five defaults on their ranges | not applicable |
| Receive, Transmit-keyed, Tune screens | REQ-SYS-060 | all six fields on each render | not applicable |
| 50 frames/s and 50 detents/s load | REQ-SW-KEYER-014 | 2 x the design frame rate; covers 2 rev/s | not applicable |

## 8. Proposed values

| Id | Proposed value | `tbr.plan` branch | Margin |
|---|---|---|---|
| REQ-SYS-058 | 10 Hz to 10 kHz (unchanged), step table of section 3.4 in the L2 child | confirm | not applicable |
| REQ-SYS-061 | 4.0 mm (unchanged) | confirm | 0.14 mm |
| REQ-SYS-062 | two levels (unchanged) | confirm | 0 |
| REQ-SYS-067 | 1 s (unchanged) | confirm | 424 ms |
| REQ-SYS-068 | 9 min 00 s +/-5 s (unchanged) | confirm | 4.4 s |
| REQ-SYS-136 | Iambic A, 15 WPM, 600 Hz, 8-dit hang, 5 ms (unchanged) | confirm | not applicable |
| REQ-SYS-164 | 30 s at 2 rev/s (unchanged) | confirm | 21.7 s |
| REQ-SYS-165 | 300 lux (unchanged), with the lens condition of section 6.2 | confirm | 3.8 x |
| REQ-SW-KEYER-014 | 50 frames/s and 50 detents/s per encoder (unchanged) | confirm | not applicable |

No value goes to the owner before this note's record is APPROVED (plan rule C10). No CR is triggered.

## 9. Requests to other writers (plan section 5.3)

- **R-U1 (WP-PDR-39 enclosure concept, WP-PDR-27 enclosure trade):** an AR-coated window lens, or no separate lens over the polarizer, to hold 3:1 contrast in the specular case; recess at most about 2 mm (F23).
- **R-U2 (WP-PDR-32 firmware architecture):** UI task period 20 ms, display updates on change only and at most 25 frames/s, the frequency rendered from the synthesizer value; the display initialised in the boot path before the configuration load (A-U10); the SW module name (SW-DISPLAY or SW-UI) is the architecture ADR's.
- **R-U3 (WP-PDR-35 SW L2):** L2 children for the step table (section 3.4), the menu tree with the MODE values and the service calibration screen (section 3.3), the message table with the three added messages (section 3.6) and the ID reminder timer (section 3.7).
- **R-U4 (ConOps writer, WP-PDR-10; handbook at CDR):** Table 3.4-4 display texts in the 10-character two-line form of section 3.6, or the long forms kept as handbook text.
- **R-U6 (ConOps writer, WP-PDR-10):** add rows to Table 3.4-4 for REQ-SYS-155 (PA temperature sensor fault, Latched) and REQ-SYS-156 (forward-power detector fault, Latched), with the texts and classes of section 3.6. Add the REQ-SYS-134 setting-replaced indication, which does not stop transmission, as a note to Table 3.4-3 or a row of a companion table of indications. Also name the service calibration screen (FUNC held while switching on) in section 3.5.1.
- **R-U5 (WP-PDR-40):** the owner's hands-on session tries the step table, the FUNC speed shortcut and the menu, and reads the renders printed at true size (a 23.04 mm square) at 0.5 m.

## 10. Tools, credit and verification route

| Tool | Version | TV record | Use |
|---|---|---|---|
| venv Python | 3.13.5 | TV-001 (accredited for schema validation only) | interpreter |
| `ui_model.py`, `check_ui_design.py` | this commit | none | every number of sections 6 and 7; the renders |
| Pillow, matplotlib | 12.3.0, 3.11.2 (venv) | none | renders and plot |

Results are developer evidence (05 section 9.1; checklist CK-ANA-C2) until a TV record covers the model or the owner rules on that basis. The plan's "host usability run" is here a scripted operator in Python, not HostUnit: the `SW-DISPLAY` code does not exist yet; its HostUnit cases (frame goldens, menu enumeration, step table) follow the L2 children of R-U3. REQ-SYS-061 closes by Inspection of the rendered frame at the pixel pitch (its method), which the flight renderer's golden frame provides at CDR; REQ-SYS-165 closes by Analysis (this note is its first issue); the others are Test or Demonstration closed after TRR.

## 11. Limitations

- L-U1. The legibility criteria A-U1 to A-U3 have no corpus source.
- L-U2. A plain lens in the specular case gives 2.74:1; accepted only if the owner accepts tilting as the mitigation (R-U1).
- L-U3. The LC response time (A-U5) is unmeasured.
- L-U4. The usability run is scripted, not a person; the owner's session confirms the feel.
- L-U5. The renders use an illustrative panel colour; the dot grid, sizes and positions are exact.

## 12. Change history

| Date | Revision | Change |
|---|---|---|
| 2026-09-27 | 1 | First issue for the F0 freeze (WP-PDR-33, wave 1a) |
| 2026-09-27 | 2 | Major findings of iteration 1. INSP-072 finding-1: the REQ-SW-KEYER-002 Straight-input setting as three MODE values with codes SO, SR, ST; the REQ-SYS-035 trim placed outside the operator tree on a service calibration screen for the NGO-012 reason; 24 items recounted; two renders added. INSP-072 finding-2: banners for REQ-SYS-155, REQ-SYS-156 and REQ-SYS-134; distinctness and latency restated over 25 messages; request R-U6 to the ConOps writer; assumption A-U10 |
