# Keyer host study: interlock, stuck-key timeouts, paddle watchdog, squeeze limit and watchdog period

| Field | Value |
|---|---|
| Product | Analysis note of WP-PDR-33 (`docs/plan/pdr-work-plan.md` section 3.7), G13 TBR group of plan section 10.2 |
| Status | Draft, revision 4: fixes the Major finding of review iteration 3 (INSP-075 finding-7) for the delta iteration (plan rule C1), frozen again at F0 (rule C2). Revision 3 fixed the Major finding of iteration 2 (INSP-075 finding-6); revision 2 fixed the Major findings of iteration 1 (INSP-071 finding-1; INSP-075 findings 1 and 2). The Minor findings are not addressed in this revision. It proposes values; it changes no requirement, hazard or interface file (plan section 5.3) |
| Author | Claude, software lead (keyer) role, WP-PDR-33 author invocation, 2026-09-27 |
| Review records (plan section 3.7) | `docs/reviews/PDR/checklists/analysis-keyer-host-study.md` (INSP-071, independent reviewer, `peer-review-checklist-analysis.md`) and `analysis-keyer-host-study-software-assurance.md` (INSP-075, SA reviewer, `peer-review-checklist-software-assurance.md`) |
| Analysis kind | timing, worst-case (checklist sections G6 and G7); criticality safety-critical (`SW-KEYER` and the safe-state manager, `docs/process/07-software-engineering-plan.md` section 14.1) |
| Model and checker | `docs/design/analysis/keyer-host-study/keyer_model.py` (reference keyer, debounce, monitors, corpus); `docs/design/analysis/keyer-host-study/check_keyer_host_study.py` (asserts every number below) |
| Outputs | `docs/design/analysis/keyer-host-study/keyer-host-study-results.json`; plots `keyer-squeeze-vs-speed.png`, `keyer-nogap-vs-speed.png`, `keyer-nogap-fault-coverage.png`, `keyer-nogap-short-interval.png`, `keyer-squeeze-timeline.png` in the same folder |
| Reproduce | `cd /Users/robinonsay/rust/cwht && .venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py` (exit 0, 571 assertions, about 85 s) |
| Credit | Developer evidence (`docs/process/05-configuration-and-data-management.md` section 9.1): the model has no TV record (section 10) |

## 1. Question and scope

The study answers, for each G13 TBR, whether the ratified value holds against legitimate sending at 5 to 50 WPM and against the fault cases it must stop, and proposes the value for the owner's ruling (plan rule C10). The requirements, with their text at `main` blob `f128235e` (`docs/requirements/sys/requirements.json`) and `f9141160` (`docs/requirements/sw/sw-keyer/requirements.json`):

| Id | Value under study (TBR) | `tbr.plan` step this study executes |
|---|---|---|
| REQ-SYS-052 | interlock, each used input open 500 ms | "the HostUnit bounce study at PDR confirms it" |
| REQ-SW-KEYER-022 | interlock, 500 consecutive samples | closes with REQ-SYS-052 |
| REQ-SYS-053 | manual-closure timeout 5 s | "confirms the value and fixes the configurable range (2 to 6 s)" |
| REQ-SW-KEYER-026 | manual-closure timeout 5 s | closes with REQ-SYS-053 |
| REQ-SYS-054 | paddle watchdog: 128 identical elements, or 30 s without a 7-dit or 500 ms gap (whichever gap is shorter) | "confirms that no legitimate sending at 5 to 50 WPM reaches them, else the values change by CR"; the CR-008 branch (`c629198`, blob `a7344937`) adds "including word spaces near 7 dits above about 17 WPM (INSP-025 cross item X8)" and writes the gap as "min(7-dit, 500 ms)" (TBR reader finding 7) |
| REQ-SYS-184 | squeeze limit 2 s in Iambic A, Iambic B, Ultimatic | "checks it against the longest squeezed character at 5 WPM (C, 11 dit times, 2.64 s), and if normal squeezing trips it the limit becomes the longer of 2 s and 16 dit times by CR" |
| REQ-SYS-131 | firmware hang recovery within 2 s | "fixes the watchdog period against the longest legitimate loop" |
| REQ-SYS-188 | bench test mode left at most 120 s after entry | "confirms it against the longest bench procedure and the REQ-SYS-180 floor" |
| REQ-SYS-189 | full-scale test tone at most 60 s | "the PDR audio and test-mode design confirms it" |
| REQ-SW-KEYER-036 | key-down withheld while a key input reads closed and the plug-presence input reads no plug | "the CTL schematic at PDR confirms the plug-presence switch and its reading against the jack drawing" (G14; placed here because it is a `SW-KEYER` safety value with an SA review) |

Hazard controls served: HZ-004 K1 (REQ-SYS-052), K3 (REQ-SYS-053), K4 (REQ-SYS-054, REQ-SYS-184; its two `tbr` items), K7 (REQ-SYS-131), K9 (REQ-SW-KEYER-036), K13 (REQ-SYS-188); HZ-005 K9 (REQ-SYS-189) (`docs/safety/hazards.json` blob `81cacde4`). Expectations: NGO-021 and MOE-012 (`expectations.json` blob `52b6cf5e`), which mirror the REQ-SYS-054 and REQ-SYS-184 values.

Out of scope: debounce values (REQ-SYS-048, REQ-SYS-162, REQ-SW-KEYER-020, 021, G12, WP-PDR-40), the Iambic B switchpoint and the override interval (REQ-SW-KEYER-009, 039, G14 HIL, WP-PDR-40), hardware cutoff and backstop timing (REQ-SYS-055, REQ-SYS-180, G7, WP-PDR-26).

## 2. Inputs

| # | Input | Value used | Source |
|---|---|---|---|
| I-1 | Dit length | 1200/WPM ms; dah 3 dits; intra-character space 1 dit, letter space 3, word space 7 | `docs/research/keyer-verification-and-key-input-network.md` (blob `53345cb1`) F7, F14 (ITU-R M.1677-1 section 2 and the PARIS convention, Sourced) |
| I-2 | Keyer semantics, Iambic A and B | rules 1 to 6 of F7: dit first on a simultaneous press; self-completing elements; opposite-paddle memory; mode B squeeze latch from S x L after element start to the end of the space; same-paddle repeat latch in the space; alternate beats repeat | F7 (Curtis 8044 definitions, Sourced; tunables Proposal) |
| I-3 | Switchpoint S | 0 to 0.9, default 0.5 | REQ-SW-KEYER-009 (TBR, G14 HIL); F7 |
| I-4 | Ratio, weight, key compensation | 3.0, 50 percent, 0 (build-time defaults) | F14; SRR decision 48 (`docs/conops/conops.md` blob `6c3fbb2b` section 3.5.1 item 3) |
| I-5 | Debounce | make 2 samples, break 5 samples, 1 kHz sampling, sample k at k ms | F6 (Proposal, TBR by the G12 capture); REQ-SW-KEYER-020, 021 |
| I-6 | Element timing tolerance | +/-0.5 percent or 0.2 ms | REQ-SW-KEYER-013 |
| I-7 | Longest contact bounce | 10 ms (Curtis 5 to 10 ms; Ganssle maximum 6.2 ms) | F6 (Sourced) |
| I-8 | Hardware cutoff window | 7.5 s to 13 s | REQ-SYS-055 (TBR, G7) |
| I-9 | Transmission-length backstop floor | 150 s | REQ-SYS-180 (TBR, G7) |
| I-10 | Longest keyed bench step | element timing at 5 WPM, about 60 s | REQ-SYS-188 rationale |
| I-11 | Plug-presence circuit | SJ1-3535N ring switch to a GPIO with 100 kohm pull-down; no plug: the shunt ties the detect pin to the ring node | `docs/research/display-and-ui-parts.md` (blob `11c497ba`) F17 (High), F19 (Medium, derived); `docs/icd/ICD-CTL-KEY.md` (blob `5e9f1888`) section 3.2.5 row J1-5 |
| I-12 | Morse character set | ITU-R M.1677-1 letters, figures, punctuation and service signals, transcribed by the author (the standard is not in the corpus); plus `;`, `!`, `$`, `_` in common amateur use (marked EXTRA in the model) | Author transcription; the two worst characters (period `.-.-.-`, figure 1 `.----`) are also in the keyer research vectors (F7 V13 period) |
| I-13 | Flash erase and program times | 4 KB sector erase 400 ms maximum; 256-byte page program 3 ms maximum | Assumption A-7 |
| I-14 | Pico 2 flash part and store scheme | Winbond W25Q32RV, 4 KiB sectors; A/B records in the top two sectors | `docs/research/rustos-toolchain-proof.md` (blob `74e5363f`) F15 (High) |

## 3. Model

### 3.1 Structure

`keyer_model.py` is an independent host model of the keyer engine, the input sampler and debouncer, the interlock, the manual-closure timeout and the safe-state monitors (squeeze limit and no-gap watchdog). It is the SEMP section 7.3.1 "keyer timing model on the host". It is not the flight code: the `cwht-core` keyer is written by WP-PDR-41 against the rustos `api` traits, and its HostUnit cases (TC-SW-KEYER-*) are the credited evidence (section 10).

Time base: raw contact states are sampled at integer milliseconds; element and space boundaries are computed in microseconds from the dit length, so element timing is exact (F8: TIMER0 has 1 us resolution). When a sample and an element boundary fall on the same instant, the sample is processed first; the F7 golden vectors pass with this rule (section 5.1).

### 3.2 Modes

- **Iambic A and B**: F7 rules 1 to 6 verbatim.
- **Ultimatic**: while both paddles are held, the last-closed paddle's element repeats; with one held, that paddle's element repeats; a tap of the opposite paddle during an element or its space is remembered as for iambic memory (the REQ-SYS-184 rationale: "a squeeze repeats the last-closed element").
- **Bug** (REQ-SW-KEYER-011, REQ-SW-KEYER-012): the dit contact gives self-timed dits at the selected speed with 1-dit spaces while it is closed; the dah contact keys for as long as it is closed. So the dahs, every space next to a dah, every letter space and every word space are operator-timed, and only dit-to-dit spaces are keyer-timed. The engine is not simulated for Bug: the monitors see only TX_KEY, which is built from text (`key_stream_bug`, corpus B, section 3.4).
- **Straight and Straight-on-tip** (REQ-SW-KEYER-002): every element and every space is hand-timed. TX_KEY is built from text with hand-timing profiles (`key_stream_hand`, corpus S, section 3.4). A manually timed closure (the straight key, the Bug dah contact) is also bounded by the manual-closure timeout (section 6.4).

### 3.3 Operator model for the squeeze study

The quantity REQ-SYS-184 bounds is the longest continuous time both debounced contacts are closed. For a correct sending, that time is longest when the operator squeezes over a whole alternating run and releases at the latest instant that still gives the right character. The model therefore searches, by simulation, for the latest raw release that yields the target pattern, for every alternating run of length 2 to 6 (both starting elements) in Iambic A, Iambic B (S = 0, 0.5, 0.9) and every "X then Y repeated n times" pattern (n = 1 to 4) in Ultimatic, at 5, 10, 15, 25 and 50 WPM.

Script: the first paddle closes at raw 0 ms; the second at raw 0 ms when the run starts with a dit (one sample, dit first) or at raw 1 ms otherwise; both open at raw t1. The correct-release window found by simulation is compared with the analytic window:

- Iambic A: the debounced release r must satisfy SE(k-1) < r <= SE(k), where SE(i) is the end of the space after element i: at SE(k) nothing may be held.
- Iambic B: start(k-1) + S L(k-1) < r <= start(k) + S L(k): the last element must not latch another.
- Ultimatic: SE(n) < r <= SE(n+1) over the pattern X Y^n.

A run inside a character behaves as the isolated run: the second paddle cannot close before the run's first element starts (else it would change the previous decision), and the release window is the same. The character bound is the longest of its runs. Three whole characters are simulated as a cross-check (section 5.1).

### 3.4 Sending corpora for the paddle watchdog

The no-gap watchdog sees only TX_KEY. The model builds TX_KEY from text for each key mode. Two texts, author-written, with the placeholder call N0CALL:

- **QSO text**: a complete CW contact (CQ, call exchange with portable suffixes, RST 599 and 5NN, name, QTH, grid square, rig, weather, 73, the prosigns AR, KN, SK, CT, BT, the error signal, HH HH, 55555, 00000, EEEEE, IIIII, SSSSS) and every punctuation character.
- **Stress tokens**: the longest tokens an operator plausibly sends without a word space: a 20-letter word, `VE3/N0CALL/QRP`, `N0CALL/MM/QRP/P`, `1234567890`, `0000000000`, a 13-letter word.

Three corpora send both texts (no recorded sending is available, limitation L-2):

| Corpus | Key modes | TX_KEY timing | Profiles | Streams |
|---|---|---|---|---|
| P (`key_stream`) | Iambic A, Iambic B, Ultimatic | keyer-timed elements and intra-character spaces; operator-timed letter and word spaces | letter / word space in dits: nominal 3/7; short word 3/6 and 3/5; fast 2.5/5; spread 4.5/10; every speed 5 to 50 WPM | 460 |
| B (`key_stream_bug`) | Bug | automatic dits and dit-to-dit spaces at the selected speed; manual dahs of 3 or 6 Bug dits, or drawn from 2.5 to 6 per dah; every other space in the operator unit k x Bug dit, with k = 0.75, 1, 1.5, 2 (operator spacing from 1.33 times faster to 2 times slower than the Bug dits); letter / word spaces 3/7, 3/5, 2.5/5, 4.5/10 units; every manual length scaled by an independent factor within +/-15 percent; 15 speeds 5 to 50 WPM; 2 seeds (A-10) | 2880 |
| S (`key_stream_hand`) | Straight, Straight-on-tip | every element and space hand-timed | five hand profiles H1 to H5 (A-11): nominal; heavy (elements 1.3, dah 3.5, intra 0.7, letter 2.5, word 5); light (elements 0.8, dah 2.5, intra 1.3, letter 3, word 6); spread (letter 4.5, word 10); run-together (letter 2.5, word 5); each length scaled within +/-10 to +/-20 percent; 15 hand speeds 5 to 50 WPM; 3 seeds | 450 |

Three watchdog rules are applied to every stream (section 6.2): the baselined rule ("current"), the revision 1 proposal ("rev1", a gap of 2 dit times at the selected speed) and the revision 4 proposal ("rev4", `watchdog_relative`). The withdrawn revision 2 and revision 3 rules (`watchdog_rev2`, `watchdog_rev3`) are run only on the short-interval variants of section 6.2. For the current and rev1 rules the monitor uses the selected keyer speed. In Straight mode that speed has no relation to the hand speed, so corpus S is also run with the keyer set to 5 WPM, the setting with the longest threshold (the INSP-071 finding-1 counter-example).

The watchdog model, current and rev1 rules: a key-up gap qualifies when it is at least the gap threshold; the no-gap span runs from the start of the element after the last qualifying gap; the identical-element count resets on a different element or a qualifying gap; the watchdog trips at the 128th identical element or when the span reaches 30 s. The rev4 rule is defined in section 6.2; it quantises the TX_KEY edges to the 1 ms read-back sample, filters read-back glitches shorter than 10 ms and filters split pulses (spurious key-downs shorter than half the stream's own space and element).

### 3.5 Key-mode scope of the monitors (INSP-071 finding-1)

| Monitor | Runs in | Dit length it uses |
|---|---|---|
| REQ-SYS-054 items (i) and (ii), revision 4 rule | every key mode: Straight, Straight-on-tip, Iambic A, Iambic B, Ultimatic, Bug (HZ-004 K4 "whatever the element pattern", on the TX_KEY read-back) | none: the reference interval is measured on TX_KEY (section 6.2), so no keyer parameter enters the monitor |
| REQ-SYS-184, item (iii) | Iambic A, Iambic B, Ultimatic (its statement) | the selected speed from the configuration-guarded value, with its complement and its 5 to 50 WPM range checked at every use; on a failure the 50 WPM value (section 6.1) |
| REQ-SYS-053 manual-closure timeout | Straight, Straight-on-tip, the Bug dah contact | none (a time) |

Revision 1 of this note proposed "2 dit times at the selected speed" for item (ii) in every mode without stating the scope. In Straight and Bug sending the selected speed does not fix the operator's spacing, and that rule trips correct sending in both modes (section 6.2). Revisions 2 to 4 remove the selected speed from items (i) and (ii).

## 4. Assumptions

| # | Assumption | Direction of effect | What would invalidate it |
|---|---|---|---|
| A-1 | The worst legitimate squeeze is a squeeze held over a whole alternating run and released at the latest correct instant | Conservative: any real release is earlier | An operator who keeps both paddles closed through an element that the keyer then must not send; that is not a correct sending |
| A-2 | Build-time ratio 3.0, weight 50 percent, key compensation 0 (I-4) | Neutral at these values; a ratio of 4.0 raises the worst squeeze to 21 dits (period) and 22 dits (figure 1 in Ultimatic) | A build that changes the ratio; the squeeze limit in dits must then be re-derived (section 6.1, request R-3) |
| A-3 | Debounce adds at most 3 ms (break minus make) to the both-closed time the monitor sees | Conservative (added) | G12 capture changing the debounce counts; the effect is milliseconds against a limit of seconds |
| A-4 | Legitimate sending uses the character set of I-12 | The period and semicolon (18 dits, Iambic A) and the figure 1 and apostrophe (18 dits, Ultimatic) set the bound | A longer alternating prosign run; none exists in the set |
| A-5 | The longest token sent without a word space has at most 20 characters | Sets the current-rule no-gap result at 8 WPM | Longer run-together strings; the revision 4 rule does not depend on it (section 6.2) |
| A-6 | Operator word spaces, and in most sending the letter spaces, are at least twice the reference interval r of the same stream: the lower quartile of its key-up intervals in the preceding 10 s. In correct sending at least a quarter of the key-up intervals are intra-character spaces, so r is the 1-dit keyer space in paddle and Bug sending, or the operator's own intra-character space in Straight and in the manual parts of Bug sending | Sets the revision 4 gap rule (section 6.2) | Letter spaces shorter than twice the intra-character space merge characters: receiving operators and decoders then read one character. Where the letter spaces do not qualify, only the word spaces end a span (the 16.94 s longest span of section 6.2). Corpora B and S test it with independent jitter on every length (A-10, A-11) |
| A-7 | W25Q32RV 4 KB sector erase at most 400 ms, page program at most 3 ms, read-back of 512 bytes at most 1 ms (Winbond W25Q-family datasheet values; the W25Q32RV datasheet is not in the repository) | Sets the longest interval in which the watchdog cannot be fed | The WP-SW-08 DML-3 note (WP-PDR-41) states the part's values; a larger erase time raises the watchdog load |
| A-8 | Bootrom plus runtime start-up to Self-test entry at most 100 ms | Adds to the hang-to-Self-test time | A slower boot; 0.9 s of margin remains (section 6.5) |
| A-9 | The longest single level reading taken within one full-scale tone start is 30 s | Sets the REQ-SYS-189 margin | A procedure that needs a longer tone; it restarts the tone (TC-SYS-042 and TC-SYS-051 already do) |
| A-10 | Bug sending (corpus B): manual dahs of 2.5 to 6 Bug dits; operator unit from 0.75 to 2 Bug dits; each manual length within +/-15 percent of its nominal value | Bounds corpus B; the revision 4 rule depends only on A-6. With the unit at 0.75 Bug dits only the word spaces qualify (16.94 s longest span); a unit faster than 0.75 Bug dits, outside the corpus, moves the word spaces toward 2 r (A-6) | Bug sending with dahs longer than 6 dits (REQ-SYS-053 also bounds these at 5 s) or with letter spaces under twice the shortest intra-character space (A-6) |
| A-11 | Straight sending (corpus S): the hand profiles H1 to H5 of section 3.4, independent jitter of +/-10 to +/-20 percent on every length | Bounds corpus S | A recorded Straight-key sending (L-2, request R-7) outside these profiles; it is replayed through `watchdog_relative` before the ruling |
| A-12 | Keyer-fault streams (section 6.2 catalogue): spaces stretched 1 to 8 dits, element ratio 1 to 6, weight shift from -0.5 to +0.9 dit, a stuck element timer, random element order, equal elements with random spaces, periodic patterns of 2 and 3 elements, and a text-like stream; and the short-interval variants of INSP-075 findings 6 and 7 (a key-up break of 1 to 15 ms inside an element, a spurious key-down element of 1 ms to 1 dit in a space, or a shortened space, every 1 to 10 s) | Sets the fault-side results; the residual is the text-like class and the short-interval class of section 6.2 | A fault that produces a non-repeating stream with letter-length gaps, or one whose short key-up intervals make up a quarter or more of its key-up intervals (the residual, bounded by K12) |

## 5. Model validation and uncertainty

### 5.1 Validation

1. **Golden vectors.** The model reproduces all 19 iambic golden vectors of F7 (V1 to V13 with the A and B variants) and all five debounce vectors of F6 (D1 to D5) exactly: 24 of 24 (`golden_vectors` in the results file). These vectors were produced by the independent reference `keyer_ref.py` of the research report, so the agreement validates the engine against a second implementation.
2. **Analytic against simulated windows.** For all 240 run, mode and speed combinations of section 3.3, the latest correct release found by simulation equals the analytic boundary within 1 ms (the sampling resolution), a release in the middle of the window gives the right character, and a release beyond the window gives a wrong one (`squeeze_windows`).
3. **Whole characters.** Simulated longest correct squeezes at 5 WPM: SK (`...-.-`) in Iambic A 11.99 dits against the run bound 12; Y (`-.--`) in Iambic A 9.996 against 10; apostrophe (`.----.`) in Ultimatic 17.996 against 18 (`whole_character_checks`).
4. **Watchdog model.** Fault streams reproduce the figures of the hazard analysis: a held dit stops at the 128th element after 20.4 s at 15 WPM and 6.12 s at 50 WPM (`docs/safety/hazard-analysis.md` section 5, HZ-004 row 4: "about 6.1 s elapsed at 50 WPM", "20.5 s at 15 WPM"); the model reports the end of the 128th element (20.4 s), the hazard analysis 128 element-plus-space periods (20.48 s).

### 5.2 Uncertainty

| Source | Size | Effect on margins |
|---|---|---|
| Sampling (1 kHz) | 1 ms on every edge | Included: the checker adds the 3 ms debounce offset and compares debounced times |
| Element timing tolerance (I-6) | 0.5 percent of the squeeze | Included: the checker scales the worst squeeze by 1.005 |
| Semantics outside F7 (Ultimatic memory, tie rule) | Ultimatic worst case depends only on "last-closed repeats", which the REQ-SYS-184 rationale states | None found; the WP-PDR-41 HostUnit cases re-check the same patterns on the flight keyer (section 10) |
| Operator spacing (A-5, A-6, A-10, A-11) | Unbounded in principle | The revision 4 rule removes the dependence on word spacing and on the selected speed; the residual is word spaces under twice the reference interval r (A-6) |
| TX_KEY read-back sampling (1 kHz) | 1 ms on every edge | Included: `watchdog_relative` quantises every edge to 1 ms; at 50 WPM the smallest qualifying margin (2.5-dit letter space against 2 x 1 dit) is 12 ms. The 10 ms glitch length lies 3 ms under the shortest key-up interval of corpora P, B and S (13 ms after quantisation, Straight profile H2 at 50 WPM, `nogap_min_keyup_ms`); bridging a legitimate interval only lengthens a key-down, the direction that stops a stream earlier |
| Flash timing (A-7) | Part-specific | Watchdog load keeps 2.46 times the assumed worst interval |

## 6. Results

### 6.1 Squeeze limit (REQ-SYS-184)

Worst correct squeeze, both debounced contacts closed, in dits (debounce excluded):

| Mode | All characters (I-12) | ITU-R M.1677-1 set only | Characters | C | K, Q |
|---|---|---|---|---|---|
| Iambic A | 18.0 | 18.0 | period, semicolon | 12.0 | 10.0 |
| Iambic B, S = 0 | 16.0 | 14.0 | semicolon (period in the ITU set) | 10.0 | 6.0 |
| Iambic B, S = 0.5 (default) | 16.5 | 15.5 | semicolon (period) | 10.5 | 7.5 |
| Iambic B, S = 0.9 | 16.9 | 16.7 | semicolon (period) | 10.9 | 8.7 |
| Ultimatic | 18.0 | 18.0 | figure 1, apostrophe | 6.0 | 6.0 |

The `tbr.plan` case: a squeezed C at 5 WPM is 11 dit times long (2.64 s) as a character, but the contacts can stay closed up to 12 dits (2.88 s) in Iambic A and 10.5 dits (2.52 s) in Iambic B at the default switchpoint, and a squeezed K or Q up to 10 dits (2.40 s) in Iambic A.

Speeds at which correct sending trips each limit option (checker section 4, with the 3 ms debounce offset and +0.5 percent timing):

| Limit option | Iambic A | Iambic B S = 0.5 | Iambic B S = 0.9 | Ultimatic | Squeezed C, Iambic A |
|---|---|---|---|---|---|
| 2 s (baselined) | 5 to 10 WPM | 5 to 9 WPM | 5 to 10 WPM | 5 to 10 WPM | 5 to 7 WPM |
| Longer of 2 s and 16 dit times (`tbr.plan` CR branch) | 5 to 10 WPM | 5 to 9 WPM | 5 to 10 WPM | 5 to 10 WPM | none |
| Longer of 2 s and 20 dit times (proposed) | none | none | none | none | none |

Conclusion: normal squeezing trips 2 s, so the `tbr.plan` CR branch is triggered. The branch's 16 dit times fixes the letter C but not the period, the semicolon, the figure 1 or the apostrophe: in Iambic A the release window of a squeezed period runs from 14 to 18 dits, so a release in the last two dits of the final dah or its space (Curtis: "release during ... (or the space following)", F7) trips the branch limit at every speed up to 10 WPM (below 9.6 WPM the limit is 16 dits; from 9.6 to 10.8 WPM it is 2 s, which 18 dits exceed). The plot `keyer-squeeze-vs-speed.png` shows the curves and `keyer-squeeze-timeline.png` the period released at 4.32 s at 5 WPM.

**Proposed value:** the longer of 2 s and 20 dit times at the selected speed. It trips no correct sending at 5 to 50 WPM in any mode; minimum margin 188 ms over the speed range (at 12 WPM, where 20 dits = 2 s and the worst squeeze with offsets is 1.81 s); at 5 WPM the margin is 2 dits nominal, 455 ms with the offsets.

**Fault side** (HZ-004 row 5, headphones or a shorted TRS cable after boot): keying stops at the limit: 4.80 s at 5 WPM, 2.40 s at 10 WPM, 2.00 s at 12 WPM and above (`squeeze_fault_stop`). The 30 s no-gap window and the 150 s backstop are not reached first. Against the baselined 2 s, the stream lasts up to 2.8 s longer at 5 WPM.

**Speed source (INSP-075 finding-2).** The limit is in dit times, so the squeeze monitor needs the speed. The keyer speed is not in the configuration guard's field list (03 section 4.3; 07 section 14.1 configuration guard row), and the range checks REQ-SW-KEYER-015 and REQ-SW-KEYER-037 sit in the monitored keyer. Proposed design: the settings record holds the speed with its complement, the configuration guard range-checks it with the other safety-relevant fields, and `SW-SAFE` reads that guarded value and repeats the complement and 5 to 50 WPM checks at every use. On any failure (complement mismatch, 0, 4, 51, 255, a negative or a missing value) it uses 50 WPM, the shortest limit (`squeeze_limit_monitor_ms`). Result (`squeeze_speed_source`): the limit lies between 2.00 s and 4.80 s for every stored value, range end and complement failure, so no single corrupted value lengthens a squeeze stream beyond 4.80 s or leaves the limit undefined. A monitor value above the true keyer speed can only shorten the limit (an earlier stop, the nuisance side): for example a 20 WPM monitor value against a 5 WPM stream cuts a correct Iambic A squeeze at 2.00 s. A value at or below the stream speed never cuts a correct squeeze, and the longest fault stop at any pairing is 4.80 s (`squeeze_speed_mismatch`). The field-list change and the new software cause go to their writers (section 9, R-9 and R-8).

REQ-SYS-184 verification-note cases: a 1.9 s squeeze trips neither limit; a 2.1 s squeeze trips the proposed limit at 25 and 50 WPM and not at 5 WPM (limit 4.8 s); a 60 s squeeze trips at every speed; the squeezed C, K and Q at 5 WPM trip the baselined 2 s in Iambic A (C also in Iambic B) and never the proposed limit (`req_sys_184_cases`).

### 6.2 Paddle watchdog (REQ-SYS-054)

**Current rule ("7 dit times or 500 ms, whichever is shorter").** A qualifying gap exists in correct paddle sending only at word spaces when the speed is above 7.2 WPM (a 3-dit letter space is shorter than 500 ms), and only at word spaces of 7 dits or more above 16.8 WPM (7 dits is shorter than 500 ms). Results over corpus P (`nogap_corpus`, `keyer-nogap-vs-speed.png`):

| Spacing profile | QSO text trips at | Stress tokens trip at |
|---|---|---|
| nominal 3/7 | none | 8 WPM (the 20-letter word lasts 32.6 s) |
| short word 3/6 | 15 to 50 WPM | 8, 15 to 43 WPM |
| short word 3/5 | 13 to 50 WPM | 8, 13 to 42 WPM |
| fast 2.5/5 | 13 to 50 WPM | 7, 8, 13 to 41 WPM |
| spread 4.5/10 | none | none |

The current rule also trips 796 of the 2880 Bug streams and, in Straight, 166 of the 450 hand streams with the keyer set to the hand speed and 241 with it set to 5 WPM (`nogap_bug`, `nogap_straight`). So it is met only by exact ITU word spacing, and its threshold sits on the nominal word space above 16.8 WPM: an operator whose word spaces fall slightly under 7 dits (INSP-025 cross item X8) has no qualifying gap at all, and 30 s of ordinary sending trips the watchdog. The `tbr.plan` "else the values change by CR" branch is triggered for the gap.

**Revision 1 proposal (2 dit times at the selected speed) does not hold.** It passes corpus P, but it is not a rule for every key mode (INSP-071 finding-1). In Straight the selected speed is unrelated to the hand speed: the QSO text hand-sent at 20 WPM with the keyer set to 5 WPM trips it, and the current rule, at 30.24 s (reviewer counter-example reproduced, `nogap_insp071_counterexample`). Over corpus S with the keyer at 5 WPM it trips 228 of 450 streams. In Bug it trips 15 streams, all with the operator spacing faster than the Bug dits (k = 0.75, fast profile). On the fault side (INSP-075 finding-1) it misses every stream whose spaces are stretched to 2 dits or more: 96 of the 156 uniform fault streams of the catalogue below. Its dependence on the selected speed also puts a keyer parameter inside the `SW-SAFE` monitor (INSP-075 finding-2). Revision 1 is withdrawn.

**Revision 2 proposal (self-referenced rule with the minimum as reference) does not hold.** It took r as the shortest key-up interval of the preceding 10 s with no lower bound. One short key-up interval then set r for 10 s: every normal space became a qualifying gap and a word gap, and the interval broke the pattern the period count matches (INSP-075 finding-6). A 1 ms key-up glitch every 5 s kept a held-dit stream, an alternating stream and a held-dit stream with 2-dit spaces keying at 5, 15, 25 and 50 WPM (12 of 12; reproduced, `nogap_short_interval`), and it missed 284 of the 384 short-interval variants below, all of which the current rule stops. Revision 2 is withdrawn.

**Revision 3 proposal (glitch filter and lower-quartile reference) does not hold.** It added the 10 ms glitch filter and took r as the lower quartile of the key-up intervals of 10 s. The lower quartile resists a rare short interval only when the 10 s window holds many key-up intervals. At 5 WPM the four periodic fault streams below hold only 10 to 21 of them, and one spurious key-down element of 10 ms or more (above the glitch length, so an element) splits a space into two short intervals. Two such elements in one 10 s window make the short parts the lower quartile: r drops to about half a space, every normal space becomes a qualifying gap, and the extra element breaks the (i-a) and (i-b) runs (INSP-075 finding-7). Revision 3 stops none of the 30 finding-7 streams (a key-down element of 10, 11, 15, 30 or 60 ms every 5 or 9 s in the alternating, held-dit 2-dit-space and held-dah streams at 5 WPM), which the current rule stops at 30.0 to 30.24 s, and it misses 250 of the 1568 short-interval variants below (reproduced, `nogap_short_interval`). Its statements that a rare short interval no longer sets r and that short intervals every 5 s or more no longer defeat K4 were wrong and are withdrawn. Revision 3 is withdrawn.

**Revision 4 proposal (self-referenced rule, glitch filter, split filter and lower-quartile reference).** The monitor reads only the TX_KEY read-back, in every key mode (section 3.5), and uses no keyer parameter. Revision 4 is revision 3 plus the split filter (the two rows "Key-down reference e" and "Split filter"):

| Term | Definition (constant in `keyer_model.py`) |
|---|---|
| Glitch filter | a key-up interval shorter than 10 ms is bridged: the key-down on either side is one element. A key-down pulse shorter than 10 ms is a glitch pulse: it is not an element for items (i-a) and (i-b), it still counts as key-down for item (ii), and the key-up interval it sits in is left out of the reference set; the gap tests apply to each pulse-free part of that interval (`GLITCH_MS`) |
| Reference interval r | the lower quartile (nearest rank: the ceil(n/4)-th shortest of n) of the key-up intervals without a glitch or split pulse that ended in the preceding 10 s, the current interval included (`REF_QUANTILE`, `REF_WINDOW_S`); with no such interval only the 2 s gap qualifies |
| Key-down reference e | the lower quartile (nearest rank) of the durations of the key-downs of 10 ms or more that started in the preceding 10 s, split pulses included |
| Split filter | once the reference set and the key-down set each hold at least 4 entries (`REF_MIN_N`), a key-down of 10 ms or more that is shorter than half the smaller of r and e (`SPLIT_FRAC`), both as they stand when it starts, is a split pulse and is treated as a glitch pulse: it is not an element for items (i-a) and (i-b), it still counts as key-down for item (ii), and the key-up interval it sits in is left out of the reference set; the gap tests apply to each pulse-free part of that interval |
| Qualifying gap | a key-up interval of at least 2 r, or of at least 2 s (`GAP_FACTOR`, `ABS_GAP_S`) |
| Word gap | a key-up interval of at least 4 r, or of at least 2 s (`WORD_FACTOR`) |
| Equal | two durations that differ by at most 25 percent of the longer (`SAME_TOL`) |
| (i-a) count | 128 consecutive key-down elements of equal duration with no word gap between them; a letter-length gap does not reset it |
| (i-b) period count | 128 consecutive elements that repeat the pattern of key-down duration and preceding key-up interval with a period of 1 to 6 elements (`MAX_PERIOD`) |
| (ii) window | 30 s without a qualifying gap |

Items (i-a) and (i-b) together replace the baselined item (i). A held lever is a period-1 stream, so the 128-element result of the baselined count is unchanged. The count limit 128 and the 30 s window keep their baselined values. Because a stream is judged against its own spacing, items (i) and (ii) have no speed input that a keyer fault or a corrupted setting could falsify (INSP-075 finding-2). Only the 2 s absolute gap, which ends a span after an idle key, is a fixed time. The 2 s value is above the 1.68 s word space at 5 WPM, so correct sending never needs it, and it is below the 7.5 s cutoff floor. The 10 ms glitch length is a read-back filter, not a speed: it lies under the shortest legitimate key-up interval of the corpora (13 ms, section 5.2) and it removes the 1 ms read-back disturbances of INSP-075 finding-6 whatever their rate. The split filter removes a spurious key-down of any length from 10 ms up to half the stream's own space and element: its two key-up parts never enter the reference set, so they cannot become r, and the stream keeps its own element count. Taking the smaller of r and e keeps the filter off the elements of a stream whose spaces are more than twice its elements (the stretched-space faults of the catalogue, whose count and period stops are unchanged). The split filter does not remove a spurious element of half the stream's space or element or longer, a key-up break of 10 ms or more inside an element, or a shortened space. For those the lower quartile is the only protection, and it holds only while the short intervals stay under a quarter of the key-up intervals of every 10 s; that bound, not the rarity of the short interval, sets the extent of residual class (3) below.

**Correct sending under revision 4** (`nogap_corpus`, `nogap_bug`, `nogap_straight`, `nogap_speed_steps`): no trip in any of the 3790 streams of corpora P, B and S, every profile, every speed, and none in 12 speed changes without a pause (the QSO text from 5 to 50, 5 to 20, 10 to 50, 15 to 40, 50 to 5 and 20 to 5 WPM, nominal and fast spacing; longest span 7.24 s), which the split filter's 10 s memory of r and e could otherwise affect. The split filter acts on correct sending: 1856 key-downs in 324 of the 3803 correct-sending streams (the corpora, the INSP-071 counter-example and the speed changes) are split pulses, dits after a run of dahs or after long letter spaces (`nogap_split_filter_correct_sending`). None of them changes a trip, span or count result of corpora P, B and S against revision 3. The longest span without a qualifying gap is 16.94 s (Bug, k = 0.75, fast profile 2.5/5, 6-dit dahs, 5 WPM: the automatic 1-dit spaces set r, the operator's letter spaces of 1.9 Bug dits do not qualify, and only word spaces end a span), a margin of 13.1 s to the 30 s window (revision 3: the same; revision 2: 9.91 s). Corpus S: 10.08 s. Corpus P alone: 4.56 s, the longest character at 5 WPM. The largest count is 50 (the token `0000000000`: 50 equal dahs, whose 3-dit letter spaces are under 4 r). That is 0.39 of the 128 limit, against 55 under the current rule. The INSP-071 counter-example does not trip. **Confirmed for every key mode: 128, 30 s, with the gap and count definitions above.**

**Fault side (INSP-075 finding-1).** Catalogue of keyer-fault streams (`nogap_fault_catalogue`, `keyer-nogap-fault-coverage.png`), each at 5, 15, 25 and 50 WPM, each started from an idle key and after 15 s of correct sending, under the three rules, horizon 300 s. Stop times in seconds from the fault start under revision 4, which equal those of revision 3 for every catalogue stream (idle / after sending), with the current rule's stop from idle in brackets; "none" means not stopped within 300 s:

| Fault stream (HZ-004 row) | 5 WPM | 15 WPM | 25 WPM | 50 WPM |
|---|---|---|---|---|
| Held dit lever, 1-dit spaces (4) | 30.0 / 30.0 window (30.0) | 20.4 / 19.9 count (20.4) | 12.2 / 12.2 count (12.2) | 6.1 / 6.1 count (6.1) |
| Alternating, 1-dit spaces (5, 6) | 30.0 / 30.0 window (30.0) | 30.0 / 30.0 window (30.0) | 18.5 / 18.5 period (30.0) | 9.2 / 9.2 period (30.0) |
| Held dit, spaces stretched to 2 dits (INSP-075) | 30.2 / 35.3 window (30.2) | 30.0 / 29.8 (30.0) | 18.3 / 18.3 count (18.3) | 9.2 / 9.1 count (9.2) |
| Alternating, spaces stretched to 3 dits (INSP-075) | 30.0 / 36.0 window (none) | 30.0 / 36.4 (30.0) | 30.0 / 30.6 (30.0) | 15.4 / 15.3 period (30.0) |
| Alternating, spaces stretched to 8 dits | 31.0 / 38.4 window (none) | 30.4 / 39.1 (none) | 30.2 / 37.9 (none) | 30.0 / 30.7 (none) |
| Element ratio corrupted to 6 | 30.0 / 30.0 (30.0) | 30.0 / 30.0 (30.0) | 27.7 / 27.7 period (30.0) | 13.9 / 13.9 period (30.0) |
| Weight shift +0.9 dit (spaces 0.1 dit) | 30.0 / 30.0 (30.0) | 30.0 / 30.0 (30.0) | 30.0 / 30.0 window (18.4) | 30.0 / 30.0 window (9.2) |
| Stuck element timer, continuous key-down (10) | 30.0 / 30.0 window (30.0) | 30.0 (30.0) | 30.0 (30.0) | 30.0 (30.0) |
| Random dit and dah order, 1-dit spaces | 30.0 / 30.0 window (30.0) | 30.0 (30.0) | 30.0 (30.0) | 30.0 (30.0) |
| Dits, spaces randomly 1 or 3 dits | 92.4 count (none) | 30.8 count (30.1) | 18.5 count (18.5) | 9.2 count (9.2) |
| Dit-dah pairs, spaces 1 and 3 dits ("AAAA") | 123.1 period (none) | 41.0 period (30.1) | 24.6 period (30.0) | 12.3 period (30.0) |
| Dah pairs, spaces 1 and 7 dits | 215.8 period (none) | 71.9 period (none) | 43.1 period (none) | 21.6 period (none) |
| Random elements, spaces randomly 1 or 3 dits (text-like) | none (none) | none (30.0) | none (30.0) | none (30.1) |

Every uniform stream (one gap length, any element pattern, gaps under 2 s) is stopped within 30 s plus one element and gap from an idle key (31.7 s at most), and within 39.6 s after correct sending: the 10 s reference window must first lose enough correct 1-dit spaces for the fault's own spacing to become its lower quartile (revision 2: 40.8 s). That is 156 of 156, against 117 for the current rule and 60 for revision 1 (`nogap_fault_missed`). The weight shift of +0.9 dit leaves spaces of 0.1 dit, which at 15 WPM and above are under the 10 ms glitch length: the stream is bridged into one key-down and the window stops it at 30.0 s, later than the period count of revision 2 (18.5 s at 25 WPM, 9.3 s at 50 WPM) and the current rule (18.4 s and 9.2 s), and within the 30 s window. The current rule misses every uniform stream with spaces of 7 dits or more, and at 5 WPM every one with spaces of 2.5 dits or more (a gap of 500 ms or more qualifies). Revision 4 stops every periodic and equal-element stream of the catalogue as well, by the count or the period count. At 5 WPM that can take up to 215.8 s, after the K12 backstop floor of 150 s, so there K12 acts first, as it does under the current rule, which does not stop those streams at 5 WPM at all. Because the rule has no speed parameter, its behaviour scales with the dit length. The four speeds span the range, and only the 2 s absolute gap, the 10 ms glitch length and the 1 ms sampling break the scaling, all covered at the range ends.

**Short-interval variants (INSP-075 findings 6 and 7).** A short interval or a spurious element is inserted every 1, 2, 3, 5, 7, 9 or 10 s into four periodic fault streams (held dit, alternating, held dit with 2-dit spaces, held dah) at 5, 15, 25 and 50 WPM, from an idle key, horizon 300 s (`perturb_short_interval`, `nogap_short_interval`, `keyer-nogap-short-interval.png`): 1568 streams. The inserted intervals are a key-up break of 1, 10, 12 or 15 ms inside an element; a spurious key-down element of 1, 10, 11, 15, 30 or 60 ms or of 0.25, 0.5 or 1 dit in the middle of a space (centred when it fits with 10 ms of key-up on each side, else inserted with the space split in halves around it and the rest of the stream moved later); or one space shortened to 0.4 dit (0.9 dit in the 2-dit-space stream). Streams not stopped by K4 within 300 s, and streams stopped later than 30 s plus one cycle ("late"):

| Inserted interval | Streams | Current not stopped | Revision 2 (withdrawn) not stopped | Revision 3 (withdrawn) not stopped / late | Revision 4 not stopped / late |
|---|---|---|---|---|---|
| 1 ms key-up break or 1 ms key-down pulse (glitch; the finding-6 case) | 224 | 0 | 214 | 0 / 0 | 0 / 0 |
| Key-up break of 10, 12 or 15 ms inside an element | 336 | 0 | 293 | 24 / 0 | 24 / 0: 5 WPM, every 1 to 3 s |
| Spurious element shorter than half the smaller of the stream's space and element (split pulse; includes the 30 finding-7 streams) | 504 | 0 | 489 | 163 / 0 | 30 / 6: 5 WPM, every 1 to 2 s (late stops 36.0 s) |
| Spurious element of half the smaller of the stream's space and element or longer | 392 | 0 | 307 | 60 / 5 | 60 / 5: 5 WPM every 1 to 9 s, 15 WPM every 1 to 2 s, 25 WPM every 1 s (late stops 49.7 to 135.6 s) |
| One space shortened | 112 | 0 | 27 | 3 / 8 | 3 / 8: 5 WPM every 1 to 3 s, 15 WPM every 1 s (late stops 39.1 to 117.2 s) |
| All | 1568 | 0 (all by 30.43 s) | 1330 | 250 / 13 | 117 / 19 |

Revision 4 stops all 30 finding-7 streams, at 30.0 to 30.24 s by the window. It stops every glitch variant at every rate, and every spurious element shorter than half the smaller of the stream's space and element when it comes every 3 s or less often, at every speed, within 30 s plus one cycle. It stops every variant that revision 3 stops, never later than revision 3 or 30 s plus one cycle (checker assertions). A pure stream of glitch pulses (5 ms every 50 ms, or 9 ms every 20 ms, `nogap_glitch_pulse_streams`) is stopped by the window at 30.0 s, because a glitch pulse still counts as key-down. Every one of the 136 streams that revision 4 misses or stops late has, within some 10 s, at least a quarter of its key-up intervals at most half its nominal space (checker assertion; the share is 0.25 to 1.0): the short intervals are then the stream's own spacing, the lower quartile takes them as r, and the nominal spaces become letter-length gaps. The late stops (at most 135.6 s) come before the 150 s K12 floor. The per-speed counts are in `keyer-nogap-short-interval.png`; at 5 WPM revision 4 misses or stops late 47, 32, 14, 6, 6, 6 and 0 of the 56 variants at every 1, 2, 3, 5, 7, 9 and 10 s.

**Coverage given up (residual, routed to WP-PDR-16, request R-8).** Three classes. (1) A keyer fault that produces a non-repeating stream with a letter-length gap (2 r or more) at least every 30 s is not stopped by K4 items (i) and (ii). On TX_KEY such a stream cannot be told from correct sending of text without word spaces. The current rule stops it within 30 s at 15 to 50 WPM, but only because it treats every letter space as no gap, which is the same property that makes it trip correct sending. (2) Streams whose every key-up interval is 2 s or more are also outside K4, as under the current rule, for which every interval of 500 ms or more qualifies. (3) Short-interval streams: a stream in which, within some 10 s, key-up intervals of 10 ms or more and at most half its other spaces make up a quarter or more of its key-up intervals, and that does not repeat with a period of 1 to 6 elements, is not stopped by items (i-b) and (ii), and item (i-a) stops it only if its elements are equal. The split filter keeps a spurious element shorter than half the smaller of the stream's space and element out of this class; a longer spurious element, a key-up break of 10 ms or more inside an element, or a shortened space can bring a stream into it. The quarter share, not the rarity of the insertions, sets the extent. With n key-up intervals of the stream in some 10 s, k insertions in the same 10 s reach the share when k is at least n/7 for spurious elements of half the reference or longer (each replaces one space by two short intervals), n/3 for key-up breaks (each adds one short interval) and n/4 for shortened spaces (derived from the share definition; the runs agree). n grows with the speed: at 5 WPM the four variant streams hold 10 to 21 key-up intervals per 10 s, so two spurious elements less than 10 s apart defeat K4 items (i) and (ii) in three of them (the runs: missed at every 9 s, stopped at every 10 s), and a stream with 7 or fewer key-up intervals per 10 s at 5 WPM needs only one. At 15 WPM the runs need a spurious element every 1 to 2 s, at 25 WPM every 1 s, and at 50 WPM no variant (every 1 s or more) reaches the share; by the same count a stream at 50 WPM needs a spurious element about every 0.3 to 0.7 s. In the variants revision 4 misses 117 of 1568 and stops 19 late (36.0 to 135.6 s), against 250 and 13 for revision 3. The spurious element, break or shortened space can come from the fault that makes the stream, so no second independent event is needed. The current rule stops every such variant by 30.43 s, so class (3) is coverage given up against the current rule; the owner rules on it with the rest of the residual (plan rule C10). All three residual classes are bounded by K12 at 150 s to 180 s (REQ-SYS-180) and, while each key-down lasts under the cutoff window, not by K5. A text-like stream also needs the keyer engine to produce varying spaces and elements with no repetition. This changes the HZ-004 coverage table of `docs/safety/hazard-analysis.md` section 5 rows 4, 6 and 10 (firmware control column) and its section 8 fault trees, which WP-PDR-16 revises from this note. The residual also goes into the CR and its impact review (rule C6).

What rows 7 and 8 keep: the bench PARIS loop (row 7) repeats a 14-element word with 7-dit word spaces, outside the period count and with qualifying gaps, as under the current rule (K13 and K12 bound it). K4 may be unable to act on a pin-map error (row 8) under any rule, and K12 bounds it.

### 6.3 Interlock (REQ-SYS-052, REQ-SW-KEYER-022)

With any closed sample restarting the count, the interlock arms exactly 500 samples after the last closed sample, whatever the release bounce: clean release at 1000 ms arms at 1499 ms; with 6.2 ms and 10 ms of release chatter at 1506 and 1509 ms; an intermittent short that opens for 499 ms never arms; a mono plug never arms a paddle mode and arms Straight-on-tip at 499 ms (the 500th open sample) (`interlock`). 500 ms is 50 times the longest bounce (I-7), and it runs during Self-test, which lasts a few seconds (`docs/conops/conops.md` Table 3.4-1), so an operator does not wait for it. **Confirmed: 500 ms and 500 consecutive 1 kHz samples.**

### 6.4 Manual-closure timeout (REQ-SYS-053, REQ-SW-KEYER-026)

Key-down ends 5.0 s after the confirmed make for any closure of 5.0 s or longer and follows the contact for 4.9 s (`manual_timeout_cases`). The longest legitimate manual closure is taken as a 6-dit dah at 5 WPM, 1.44 s (twice the nominal dah, for a heavy straight-key or Bug fist; F13 item 2 gives 1.08 s for a 4:1 ratio with 75 percent weight). Margins: default 5 s over the longest closure 3.56 s; the 2 s floor of the range 0.56 s; the 7.5 s cutoff floor over the 6 s ceiling 1.5 s, over the default 2.5 s. **Confirmed: 5 s, range 2 to 6 s.** Because SRR decision 48 makes only the switchpoint and the debounce operator-set, the range is a build-time parameter, not an operator setting (request R-6).

### 6.5 Firmware hang recovery (REQ-SYS-131)

The longest interval in which firmware cannot feed the watchdog is a configuration-store sector update with interrupts masked and XIP off (F15; RSK-021): erase 400 ms, two pages 6 ms, read-back 1 ms, 0.407 s (A-7). Proposed watchdog load: 1.0 s, 2.46 times that interval. A hang at the instant after a feed resets the controller 1.0 s later and reaches Self-test by 1.1 s (A-8), 0.9 s inside the 2 s requirement. **Confirmed: 2 s, with a design watchdog load of 1.0 s** (for WP-PDR-32, request R-1). Consequence: the 1 kHz key sampler stops during a sector update, so a configuration write must never run in Transmit-keyed or while a key input reads closed (request R-2).

### 6.6 Bench test-mode timeouts (REQ-SYS-188, REQ-SYS-189)

A PARIS word at 5 WPM lasts 12.0 s, so the longest keyed bench step (element timing at 5 WPM, about 60 s) is five words; 120 s covers it twice and ends 30 s before the 150 s backstop floor, so the mode always ends before the backstop acts on its PARIS loop (HZ-004 row 7). The full-scale tone of 60 s covers twice the longest single reading (A-9); longer procedures restart the tone. **Confirmed: 120 s and 60 s.**

### 6.7 Plug presence (REQ-SW-KEYER-036)

Truth table of the F19 circuit (`plug_presence`): with no plug, a short of the tip line to ground reads "closed with no plug" and is withheld (HZ-004 K9, HZ-010 K3); a short of the ring line to ground pulls the detect pin low through the shunt, which reads "plug present", so REQ-SW-KEYER-036 cannot see a ring-line short. That fault is still covered: at power-on or reset by the interlock (the ring is used in every paddle mode), and after boot by the manual-closure timeout (Straight) or the squeeze limit and watchdog (paddle modes). **Confirmed: the circuit is kept, "no plug" means the detect input reads high, and the requirement stands**, with the ring-line coverage limit recorded for the hazard analysis (request R-4). The jack's shunt behaviour is still to be confirmed on the CTL schematic against the SJ1-3535N drawing (ICD-CTL-KEY TBR row "Plug-detect wiring"), which is WP-PDR-37 work.

## 7. Per-case table (plan rule C7)

Every case the governing requirement text or its verification note names:

| Case | Governing id | Result | Margin |
|---|---|---|---|
| Closed inputs at boot, after reset, after mode change, 0 to 2 s | REQ-SYS-052, REQ-SW-KEYER-022 | arms 500 samples after the last closed sample in every case | 50 x the longest bounce |
| Mono plug, paddle mode and Straight-on-tip | REQ-SYS-052 | never arms / arms at 499 ms | not applicable |
| Straight on tip, ring, both; Bug dah; held 4.9, 5.0, 5.1, 60 s | REQ-SYS-053, REQ-SW-KEYER-026 | 4.9 s follows the contact; 5.0 s and longer end at 5.0 s | 3.56 s over the longest legitimate closure |
| Held lever to the 128th element at 5, 25, 50 WPM | REQ-SYS-054 | revision 4: 5 WPM window at 30.0 s first; 25 and 50 WPM the 128th element (dit 12.24 s and 6.12 s, dah 24.53 s and 12.26 s) (`req_sys_054_cases_rev4`) | count 2.56 x the corpus maximum |
| Alternating stream, no qualifying gap, 30 s | REQ-SYS-054 | revision 4: 30.0 s at 5 WPM; the period count first at 25 WPM (18.48 s) and 50 WPM (9.24 s) | not applicable |
| Qualifying gap every 25 s keeps keying | REQ-SYS-054 | revision 4: a non-repeating stream (random dit and dah order, 1-dit spaces) with a 7.5-dit gap every 25 s keeps keying at 5, 25 and 50 WPM (window restart). The alternating stream of the baselined note case stops at 25 and 50 WPM by the period count, which is intended: the CR restates the case with the non-repeating stream | 5 s |
| Correct paddle sending (corpus P), Iambic A, Iambic B, Ultimatic, 5 to 50 WPM, five spacing profiles | REQ-SYS-054 | current: trips (section 6.2); revision 4: never, longest span 4.56 s | 25.4 s |
| Correct Bug sending (corpus B): automatic dits, manual dahs to 6 dits, operator unit 0.75 to 2 Bug dits, 2880 streams | REQ-SYS-054 `tbr.plan`; WP-PDR-33 output "Bug dahs" | current trips 796, revision 1 trips 15, revision 4 never; longest span 16.94 s | 13.1 s |
| Correct Straight sending (corpus S): five hand profiles, 5 to 50 WPM, 450 streams, keyer set to the hand speed and to 5 WPM | REQ-SYS-054; HZ-004 K4 "whatever the element pattern" | current trips 166 and 241, revision 1 trips 0 and 228, revision 4 never (no keyer parameter); longest span 10.08 s | 19.9 s |
| INSP-071 counter-example: QSO text hand-sent at 20 WPM, keyer set to 5 WPM | REQ-SYS-054 | current and revision 1 trip at 30.24 s; revision 4 never | not applicable |
| Keyer-fault streams: stretched spaces 1 to 8 dits, ratio 1 to 6, weight shift, stuck element timer, random order, equal elements with random spaces, periodic patterns, text-like; idle and after correct sending; 5, 15, 25, 50 WPM | HZ-004 K4; hazard-analysis section 5 rows 4, 6, 10 | revision 4 stops 156 of 156 uniform streams by 39.6 s and every periodic stream; the text-like class is the residual (section 6.2) | residual bounded by K12 |
| Correct sending with a speed change and no pause: 5 to 50, 5 to 20, 10 to 50, 15 to 40, 50 to 5, 20 to 5 WPM, nominal and fast spacing | REQ-SYS-054 (split filter memory) | revision 4 never; longest span 7.24 s | 22.8 s |
| Short-interval variants (INSP-075 findings 6 and 7): key-up break of 1 to 15 ms, spurious key-down element of 1 ms to 1 dit, shortened space, every 1 to 10 s, four periodic streams, 5, 15, 25, 50 WPM, 1568 streams | HZ-004 K4; hazard-analysis section 5 rows 4, 6, 10 | revision 2 misses 1330, revision 3 misses 250 (all 30 finding-7 streams among them); revision 4 stops every glitch variant, every finding-7 stream and every split-pulse variant at every 3 s or more by 30 s plus one cycle; it misses 117 and stops 19 late (to 135.6 s), all in residual class (3), extent stated in section 6.2 | residual bounded by K12 |
| Both contacts closed 1.9, 2.1, 60 s at 5, 25, 50 WPM in A, B, Ultimatic | REQ-SYS-184 | section 6.1 | not applicable |
| Squeeze limit with a corrupted, out-of-range or mismatched speed value | REQ-SYS-184; HZ-004 K4 independence | limit between 2.00 s and 4.80 s for every stored value; a monitor value at or below the stream speed never cuts a correct squeeze (section 6.1) | fault stop at most 4.80 s |
| Squeezed C, K, Q at 5 WPM | REQ-SYS-184 | trip 2 s (C in A and B; K, Q in A); never the proposed limit | at least 8 dits at 5 WPM |
| Every character, every mode, 5 to 50 WPM | REQ-SYS-184 | proposed limit never tripped | 188 ms minimum |
| Hang in receive and while keyed | REQ-SYS-131 | Self-test by 1.1 s | 0.9 s |
| Each keying sub-mode left running | REQ-SYS-188 | mode ends at 120 s | 30 s to the backstop floor |
| Tone started and left running | REQ-SYS-189 | ends at 60 s | 2 x the longest reading |
| Every mode, no plug, tip, ring, both closed | REQ-SW-KEYER-036 | tip withheld; ring reads plug present (limit) | not applicable |

## 8. Proposed values

| Id | Proposed value | Supports it | `tbr.plan` branch | Margin |
|---|---|---|---|---|
| REQ-SYS-052 | 500 ms (unchanged) | 6.3 | confirm | 50 x bounce |
| REQ-SW-KEYER-022 | 500 consecutive samples (unchanged) | 6.3 | confirm | as above |
| REQ-SYS-053 | 5 s, build range 2 to 6 s (unchanged) | 6.4 | confirm | 3.56 s |
| REQ-SW-KEYER-026 | 5 s (unchanged) | 6.4 | confirm | 3.56 s |
| REQ-SYS-054 | Revision 4, in every key mode on the TX_KEY read-back: 128 consecutive equal elements with no word gap, or 128 consecutive elements repeating with a period of 1 to 6 elements (item (i), count unchanged); or 30 s (unchanged) without a qualifying gap. Read-back intervals under 10 ms are glitches (a key-up glitch is bridged; a key-down glitch pulse is no element and its key-up interval is no reference). A key-down shorter than half the smaller of the lower quartiles of the key-up intervals and of the key-down durations of the preceding 10 s is a split pulse, treated as a glitch pulse. Qualifying gap: at least 2 times the lower quartile of the key-up intervals of the preceding 10 s, or at least 2 s. Word gap: at least 4 times it, or at least 2 s. Equal: within 25 percent (changed from "7 dit times or 500 ms"; section 6.2 table). Residual: text-like fault streams, streams with every gap 2 s or more, and short-interval streams (a quarter or more of short key-up intervals in some 10 s, non-repeating; reached with k spurious elements of half the reference or longer, key-up breaks or shortened spaces when k is at least n/7, n/3 or n/4 of the stream's n key-up intervals in 10 s: at 5 WPM two spurious elements less than 10 s apart can suffice), bounded by K12 | 6.2 | **else a CR: triggered** (PCR-9 row "REQ-SYS-054") | 13.1 s window over P, B and S; count 2.56 x |
| REQ-SYS-184 | the longer of 2 s and 20 dit times at the selected speed (changed from 2 s; the branch names 16 dits), with the speed from the configuration-guarded value, complement and 5 to 50 WPM checked at every use, 50 WPM on a failure (section 6.1) | 6.1 | **CR branch triggered** (PCR-8), with 20 in place of 16 | 188 ms minimum; 455 ms at 5 WPM; fault stop 2.00 to 4.80 s for any stored value |
| REQ-SYS-131 | 2 s (unchanged); design watchdog load 1.0 s | 6.5 | confirm | 0.9 s |
| REQ-SYS-188 | 120 s (unchanged) | 6.6 | confirm | 30 s to 150 s |
| REQ-SYS-189 | 60 s (unchanged) | 6.6 | confirm | 2 x |
| REQ-SW-KEYER-036 | unchanged; "no plug" = detect input reads high | 6.7 | confirm (circuit kept) | not applicable |

No value goes to the owner before this note's record is APPROVED (plan rule C10). Proposed values carry no TPM.

## 9. Consequences for other products (requests to their writers; plan section 5.3)

- **CR triggers.** PCR-8 (REQ-SYS-184) and the REQ-SYS-054 item of PCR-9 are triggered. The CR changes REQ-SYS-184 and REQ-SYS-054 (statements, rationales, verification notes), their mirrors NGO-021 and MOE-012 ("2 s for a squeeze", "7 dit times or 500 ms"), HZ-004 K4 text and its two `tbr` items, `docs/conops/conops.md` Table 3.4-1 Transmit-keyed row, Table 3.4-4 row 3, section 3.5.1 item 10 and OPS-013, the concept section 7 and 14 item 3 values, TC-SYS-038, and the ICD-CTL-KEY TBR row "Paddle watchdog time cap" (which still reads "128 identical elements or 10 s"). The REQ-SYS-054 CR carries the revision 4 definitions of section 6.2 and the statement that items (i) and (ii) run in every key mode. It also carries the stated residual and the restated verification-note case (a non-repeating stream with a qualifying gap every 25 s keeps keying; an alternating stream stops by the period count). The L1 statement keeps 128, 30 s and the qualifying-gap definition; the constants (10 ms glitch length, split fraction 0.5 of the smaller of r and e with its 4-entry minimum, lower-quartile reference, 10 s reference window, factors 2 and 4, 2 s absolute gap, 25 percent, period 1 to 6) go to the `SW-SAFE` child (R-10). Each CR gets its section 6 impact review from a separate invocation before the owner is asked (rule C6).
- **R-1 (WP-PDR-32, firmware architecture):** watchdog load 1.0 s, fed from the main loop only after every safety monitor has run.
- **R-2 (WP-PDR-32, firmware design rules; WP-PDR-41):** no configuration-store write in Transmit-keyed or while a key input reads closed; defer it to Receive after the hang time.
- **R-3 (WP-PDR-35, SW L2):** the squeeze limit child states its dit count against the build ratio; a ratio change re-derives it (A-2).
- **R-4 (WP-PDR-16, hazard analysis):** HZ-004 K9 and HZ-010 K3 credit REQ-SW-KEYER-036 for the tip line only; the ring-line short with no plug is covered by K1, K3 and K4.
- **R-5 (WP-PDR-35 and WP-PDR-16):** consider re-running the interlock on a plug-presence change from no plug to plug; headphones or a shorted cable inserted after boot would then never key, instead of keying up to the squeeze limit. This is a candidate SW-KEYER requirement, not a value of this study.
- **R-6 (requirements writer, WP-PDR-11 then WP-PDR-45):** REQ-SYS-053 `tbr.plan` says "configurable range (2 to 6 s)"; SRR decision 48 leaves only the switchpoint and the debounce operator-set, so the range is a build parameter. The REQ-SYS-184 rationale says keying resumes "once either contact opens", while `docs/conops/conops.md` Table 3.4-4 row 3 clears the inhibit when "both paddle contacts are confirmed open"; one of the two changes (the analysis is unaffected).
- **R-8 (WP-PDR-16, hazard analysis; INSP-075 findings 1, 2, 6 and 7):** (a) the K4 residual of section 6.2 (class 1, non-repeating text-like streams; class 2, streams whose every key-up interval is 2 s or more; class 3, short-interval streams in which short key-up intervals make up a quarter or more of the key-up intervals of some 10 s, reached by k spurious elements of half the stream's space or element or longer, key-up breaks or shortened spaces when k is at least n/7, n/3 or n/4 of the stream's n key-up intervals in 10 s, so at 5 WPM two spurious elements less than 10 s apart can defeat K4 items (i) and (ii), and one in a stream with 7 or fewer key-up intervals per 10 s; missed or stopped up to 135.6 s in the variants, where the current rule stops them by 30.43 s) for the `hazard-analysis.md` section 5 coverage rows 4, 6 and 10 and the section 8 fault trees, bounded by K12; (b) the revised K4 stop times for uniform streams (at most 39.6 s after correct sending, 31.7 s from idle) and the earlier period-count stops of alternating streams (18.48 s at 25 WPM, 9.24 s at 50 WPM); (c) a new software cause for the squeeze limit: a corrupted or mismatched speed value, bounded by the guarded read to a stop between 2.00 s and 4.80 s.
- **R-9 (WP-PDR-17, the 03 and 07 writer):** add the keyer speed to the configuration guard field list (03 section 4.3 line 176; 07 section 14.1 configuration guard row, "power step, tune level, guest lock, frequency calibration, thermal thresholds, keyer mode, debounce"). The speed is held with its complement in the settings record, and `SW-SAFE` reads the guarded value (SWE-134 items f and g).
- **R-10 (WP-PDR-35, SW L2):** the `SW-SAFE` children of REQ-SYS-054 and REQ-SYS-184 state the revision 4 constants of section 6.2, including the 10 ms glitch length, the split filter and the lower-quartile reference, and the speed source of section 6.1. The TX_KEY monitor reads no keyer data. The HostUnit cases replay the section 7 rows for corpora P, B and S, the fault catalogue and the short-interval variants on the flight monitor.
- **R-7 (WP-PDR-45):** the HZ-004 K4 `tbr` plan names "HostUnit replays of recorded normal sending"; no recording exists. This study uses the synthetic corpus of section 3.4; a recording from the owner's WP-PDR-40 session, if made, is replayed through `watchdog_relative` (the revision 4 rule) before the ruling, for each key mode the owner uses.

## 10. Tools, credit and verification route

| Tool | Version | TV record | Use |
|---|---|---|---|
| venv Python | 3.13.5 | TV-001 (accredited for schema validation only) | interpreter |
| `keyer_model.py`, `check_keyer_host_study.py` | this commit | none | every number of sections 5 and 6 |
| matplotlib | 3.11.2 (venv) | none (plots only) | four plots |

Because the model has no TV record, its results are developer evidence (05 section 9.1; checklist item CK-ANA-C2): they neither close a requirement nor go to the owner as TBR values until a TV record covers the model or the owner rules on the basis of developer evidence (owner action proposed in the author's return). HostUnit credit was the plan's first route (WP-PDR-33 "Tools: HostUnit"): it becomes available when WP-PDR-41 delivers the `cwht-core` keyer and WP-PDR-08 accredits the Rust toolchain (TV-020 to TV-022); the TC-SW-KEYER cases for REQ-SW-KEYER-022 and 026 and the SW-SAFE children of REQ-SYS-054 and 184 then replay the section 7 cases on the flight code. REQ-SYS-052 to 054, 131, 184, 188, 189 are Test-method requirements closed by Bench cases after TRR; this analysis is supporting evidence only (04 section 5.1).

## 11. Limitations

- L-1. The model is not the flight keyer. Ultimatic memory details and the tie rule are the author's; the F7 vectors do not cover Ultimatic.
- L-2. No recorded sending: corpora P, B and S are synthetic and the operator timing is bounded by profiles (A-10, A-11), not measured.
- L-3. The character table (I-12) is transcribed without the standard in the corpus.
- L-4. Flash timing (A-7) and boot time (A-8) are assumptions until the WP-SW-08 note and a dev-board boot measurement.
- L-5. The squeeze limit in dits holds for the build ratio 3.0 only (A-2).
- L-6. The revision 4 constants (10 ms, split fraction 0.5 with a 4-entry minimum, lower quartile, 10 s, factors 2 and 4, 2 s, 25 percent, period 1 to 6) are fixed from synthetic corpora and a synthetic fault catalogue (A-12); the flight monitor's HostUnit cases (R-10) and a recorded sending (R-7) re-check them.

## 12. Change history

| Date | Revision | Change |
|---|---|---|
| 2026-09-27 | 1 | First issue for the F0 freeze (WP-PDR-33, wave 1a) |
| 2026-09-27 | 2 | Major findings of iteration 1. INSP-071 finding-1: key-mode scope stated (section 3.5); Bug corpus B and Straight corpus S added (section 3.4; A-10, A-11); revision 1 gap rule withdrawn. INSP-075 finding-1: fault catalogue under the current, revision 1 and revision 2 rules; revision 2 self-referenced rule with a count that a letter-length gap does not reset and a period count; residual stated and routed (section 6.2; A-12; R-8). INSP-075 finding-2: REQ-SYS-054 items (i) and (ii) use no keyer parameter; the squeeze limit's speed source guarded and bounded (section 6.1; R-9, R-10). New plot `keyer-nogap-fault-coverage.png` |
| 2026-09-27 | 3 | Major finding of iteration 2. INSP-075 finding-6: revision 2 rule (minimum reference) withdrawn; revision 3 adds a 10 ms read-back glitch filter and takes r as the lower quartile of the clean key-up intervals of 10 s (section 6.2; `watchdog_relative`, `watchdog_rev2` kept for comparison). Short-interval variants (1 ms and 15 ms key-up breaks, 1 ms key-down pulses, shortened spaces, every 1 to 10 s; 384 streams) run under the current, revision 2 and revision 3 rules (`perturb_short_interval`, `nogap_short_interval`); fault catalogue and corpora P, B and S re-run; residual class 3 stated and routed (sections 6.2, 7, 8; A-6, A-12; R-8, R-10; L-6). Plots `keyer-nogap-vs-speed.png` and `keyer-nogap-fault-coverage.png` re-rendered. Checker 563 assertions, exit 0 |
| 2026-09-28 | 4 | Major finding of iteration 3. INSP-075 finding-7: revision 3 rule withdrawn, with its statements that a rare short interval no longer sets r and that short intervals every 5 s or more no longer defeat K4; revision 4 adds the split filter (a key-down of 10 ms or more shorter than half the smaller of r and the lower quartile e of the key-down durations of 10 s is no element and its key-up interval no reference; `SPLIT_FRAC`, `REF_MIN_N`; `watchdog_rev3` kept for comparison). Short-interval variants extended to key-up breaks of 10 to 15 ms, spurious key-down elements of 10 ms to 1 dit and an insertion every 7 s (1568 streams, `perturb_short_interval` generalised) under the current, revision 2, 3 and 4 rules; 12 speed changes without a pause added to the correct-sending side; residual class 3 restated with its extent from the quarter share (n/7, n/3, n/4) and the runs (sections 6.2, 7, 8; A-12; R-8, R-10; L-6). New plot `keyer-nogap-short-interval.png`; `keyer-nogap-vs-speed.png` and `keyer-nogap-fault-coverage.png` re-rendered with the revision 4 labels. Checker 571 assertions, exit 0 |
