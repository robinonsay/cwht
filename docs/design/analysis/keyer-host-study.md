# Keyer host study: interlock, stuck-key timeouts, paddle watchdog, squeeze limit and watchdog period

| Field | Value |
|---|---|
| Product | Analysis note of WP-PDR-33 (`docs/plan/pdr-work-plan.md` section 3.7), G13 TBR group of plan section 10.2 |
| Status | Draft, frozen at F0 for its independent review (plan rule C2). It proposes values; it changes no requirement, hazard or interface file (plan section 5.3) |
| Author | Claude, software lead (keyer) role, WP-PDR-33 author invocation, 2026-09-27 |
| Review records (plan section 3.7) | `docs/reviews/PDR/checklists/analysis-keyer-host-study.md` (independent reviewer, `peer-review-checklist-analysis.md`) and `analysis-keyer-host-study-software-assurance.md` (SA reviewer, `peer-review-checklist-software-assurance.md`), INSP numbers assigned by the lead SE |
| Analysis kind | timing, worst-case (checklist sections G6 and G7); criticality safety-critical (`SW-KEYER` and the safe-state manager, `docs/process/07-software-engineering-plan.md` section 14.1) |
| Model and checker | `docs/design/analysis/keyer-host-study/keyer_model.py` (reference keyer, debounce, monitors, corpus); `docs/design/analysis/keyer-host-study/check_keyer_host_study.py` (asserts every number below) |
| Outputs | `docs/design/analysis/keyer-host-study/keyer-host-study-results.json`; plots `keyer-squeeze-vs-speed.png`, `keyer-nogap-vs-speed.png`, `keyer-squeeze-timeline.png` in the same folder |
| Reproduce | `cd /Users/robinonsay/rust/cwht && .venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py` (exit 0, 348 assertions, about 30 s) |
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
- **Bug and Straight** are not simulated. The Bug dit contact is an automatic dit stream (a held lever, section 6.2 fault cases); the Bug dah and the straight key are manually timed closures, analysed in section 6.4.

### 3.3 Operator model for the squeeze study

The quantity REQ-SYS-184 bounds is the longest continuous time both debounced contacts are closed. For a correct sending, that time is longest when the operator squeezes over a whole alternating run and releases at the latest instant that still gives the right character. The model therefore searches, by simulation, for the latest raw release that yields the target pattern, for every alternating run of length 2 to 6 (both starting elements) in Iambic A, Iambic B (S = 0, 0.5, 0.9) and every "X then Y repeated n times" pattern (n = 1 to 4) in Ultimatic, at 5, 10, 15, 25 and 50 WPM.

Script: the first paddle closes at raw 0 ms; the second at raw 0 ms when the run starts with a dit (one sample, dit first) or at raw 1 ms otherwise; both open at raw t1. The correct-release window found by simulation is compared with the analytic window:

- Iambic A: the debounced release r must satisfy SE(k-1) < r <= SE(k), where SE(i) is the end of the space after element i: at SE(k) nothing may be held.
- Iambic B: start(k-1) + S L(k-1) < r <= start(k) + S L(k): the last element must not latch another.
- Ultimatic: SE(n) < r <= SE(n+1) over the pattern X Y^n.

A run inside a character behaves as the isolated run: the second paddle cannot close before the run's first element starts (else it would change the previous decision), and the release window is the same. The character bound is the longest of its runs. Three whole characters are simulated as a cross-check (section 5.1).

### 3.4 Sending corpus for the paddle watchdog

The no-gap watchdog sees only TX_KEY. For correctly sent text, TX_KEY is the ideal element sequence with operator-timed letter and word spaces; the model builds it from text (`key_stream`). Two corpora, author-written, with the placeholder call N0CALL:

- **QSO corpus**: a complete CW contact (CQ, call exchange with portable suffixes, RST 599 and 5NN, name, QTH, grid square, rig, weather, 73, the prosigns AR, KN, SK, CT, BT, the error signal, HH HH, 55555, 00000, EEEEE, IIIII, SSSSS) and every punctuation character.
- **Stress tokens**: the longest tokens an operator plausibly sends without a word space: a 20-letter word, `VE3/N0CALL/QRP`, `N0CALL/MM/QRP/P`, `1234567890`, `0000000000`, a 13-letter word.

Five spacing profiles (letter / word space in dits): nominal 3/7; short word space 3/6 and 3/5; fast 2.5/5; spread 4.5/10. They bound the operator's own spacing; no recorded sending is available (limitation L-2).

The watchdog model: a key-up gap qualifies when it is at least the gap threshold (the comparator is "at least"); the no-gap span runs from the start of the element after the last qualifying gap; the identical-element count resets on a different element or a qualifying gap; the watchdog trips at the 128th identical element or when the span reaches 30 s.

## 4. Assumptions

| # | Assumption | Direction of effect | What would invalidate it |
|---|---|---|---|
| A-1 | The worst legitimate squeeze is a squeeze held over a whole alternating run and released at the latest correct instant | Conservative: any real release is earlier | An operator who keeps both paddles closed through an element that the keyer then must not send; that is not a correct sending |
| A-2 | Build-time ratio 3.0, weight 50 percent, key compensation 0 (I-4) | Neutral at these values; a ratio of 4.0 raises the worst squeeze to 21 dits (period) and 22 dits (figure 1 in Ultimatic) | A build that changes the ratio; the squeeze limit in dits must then be re-derived (section 6.1, request R-3) |
| A-3 | Debounce adds at most 3 ms (break minus make) to the both-closed time the monitor sees | Conservative (added) | G12 capture changing the debounce counts; the effect is milliseconds against a limit of seconds |
| A-4 | Legitimate sending uses the character set of I-12 | The period and semicolon (18 dits, Iambic A) and the figure 1 and apostrophe (18 dits, Ultimatic) set the bound | A longer alternating prosign run; none exists in the set |
| A-5 | The longest token sent without a word space has at most 20 characters | Sets the current-rule no-gap result at 8 WPM | Longer run-together strings; the proposed rule does not depend on it (section 6.2) |
| A-6 | Operator letter spaces are at least 2 dits | Sets the proposed gap rule (2 dits) | Letter spaces shorter than 2 dits merge characters; receiving operators and decoders then read one character, so this is not correct sending |
| A-7 | W25Q32RV 4 KB sector erase at most 400 ms, page program at most 3 ms, read-back of 512 bytes at most 1 ms (Winbond W25Q-family datasheet values; the W25Q32RV datasheet is not in the repository) | Sets the longest interval in which the watchdog cannot be fed | The WP-SW-08 DML-3 note (WP-PDR-41) states the part's values; a larger erase time raises the watchdog load |
| A-8 | Bootrom plus runtime start-up to Self-test entry at most 100 ms | Adds to the hang-to-Self-test time | A slower boot; 0.9 s of margin remains (section 6.5) |
| A-9 | The longest single level reading taken within one full-scale tone start is 30 s | Sets the REQ-SYS-189 margin | A procedure that needs a longer tone; it restarts the tone (TC-SYS-042 and TC-SYS-051 already do) |

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
| Operator spacing (A-5, A-6) | Unbounded in principle | The proposed gap rule removes the dependence on word spacing; the residual is letter spaces below 2 dits (A-6) |
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

REQ-SYS-184 verification-note cases: a 1.9 s squeeze trips neither limit; a 2.1 s squeeze trips the proposed limit at 25 and 50 WPM and not at 5 WPM (limit 4.8 s); a 60 s squeeze trips at every speed; the squeezed C, K and Q at 5 WPM trip the baselined 2 s in Iambic A (C also in Iambic B) and never the proposed limit (`req_sys_184_cases`).

### 6.2 Paddle watchdog (REQ-SYS-054)

**Identical-element count, 128.** The largest count in correct sending is 55 under the current gap rule (the token `1234567890 0000000000` sent with 5-dit word spaces, which do not qualify above 12 WPM) and 8 under the proposed rule (the error signal). 128 is 2.3 times the worst case. **Confirmed.**

**Window 30 s and gap, current rule ("7 dit times or 500 ms, whichever is shorter").** A qualifying gap exists in correct sending only at word spaces when the speed is above 7.2 WPM (a 3-dit letter space is shorter than 500 ms), and only at word spaces of 7 dits or more above 16.8 WPM (7 dits is shorter than 500 ms). Results over the corpus (`nogap_corpus`, `keyer-nogap-vs-speed.png`):

| Spacing profile | QSO corpus trips at | Stress tokens trip at |
|---|---|---|
| nominal 3/7 | none | 8 WPM (the 20-letter word lasts 32.6 s) |
| short word 3/6 | 15 to 50 WPM | 8, 15 to 43 WPM |
| short word 3/5 | 13 to 50 WPM | 8, 13 to 42 WPM |
| fast 2.5/5 | 13 to 50 WPM | 7, 8, 13 to 41 WPM |
| spread 4.5/10 | none | none |

So the current rule is met only by exact ITU word spacing, and its threshold sits exactly on the nominal word space above 16.8 WPM: an operator whose word spaces fall slightly under 7 dits (INSP-025 cross item X8) has no qualifying gap at all, and 30 s of ordinary sending trips the watchdog. The `tbr.plan` "else the values change by CR" branch is triggered for the gap.

**Proposed gap: 2 dit times at the selected speed, with 30 s and 128 unchanged.** Every letter space of correct sending qualifies (A-6), so the longest span in the whole corpus, any profile, any speed, is 4.56 s (the longest character at 5 WPM), 15 percent of the window. The fault streams the watchdog exists for have 1-dit gaps (a held lever, a squeeze stream, an alternating stream from uncleared memory; HZ-004 rows 4 to 6) and a continuous TX_KEY has none (row 10), so they trip exactly as under the current rule:

| Fault stream (HZ-004 row) | 5 WPM | 15 WPM | 25 WPM | 50 WPM |
|---|---|---|---|---|
| Held dit lever (4) | 30.0 s, window | 20.4 s, count | 12.24 s, count | 6.12 s, count |
| Held dah lever (4) | 30.0 s, window | 30.0 s, window | 24.53 s, count | 12.26 s, count |
| Alternating stream (5, 6) | 30.0 s, window | 30.0 s, window | 30.0 s, window | 30.0 s, window |
| Alternating with a 2.5-dit gap every 25 s | keeps keying | keeps keying | keeps keying | keeps keying |
| Alternating with a 7.5-dit gap every 25 s (REQ-SYS-054 note case) | keeps keying | keeps keying | keeps keying | keeps keying |

Both rules give the same trip times for every stream above (checker section 5). What the proposed rule gives up: a stream with gaps of 2 to 7 dits and no longer gap (letter-spaced characters without word spaces) is no longer caught by the no-gap part. No rev A source produces one: the keyer never inserts a gap longer than one dit by itself, and the bench PARIS generator has 7-dit word spaces, which the current rule does not catch either (HZ-004 row 7, bounded by K13 and K12). Row 8 (pin-map error) is unchanged: K4 may be unable to act there under either rule, and K12 bounds it.

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
| Held lever to the 128th element at 5, 25, 50 WPM | REQ-SYS-054 | 5 WPM: window at 30 s first; 25 and 50 WPM: 128th element | count 2.3 x the corpus maximum |
| Alternating stream, no qualifying gap, 30 s | REQ-SYS-054 | trips at 30.0 s, both rules | not applicable |
| Qualifying gap every 25 s keeps keying | REQ-SYS-054 | keeps keying, both rules (7.5-dit gap); proposed rule also with 2.5-dit gaps | 5 s |
| Correct sending 5 to 50 WPM never trips | REQ-SYS-054 | current rule: trips (section 6.2); proposed: never, longest span 4.56 s | 25.4 s |
| Both contacts closed 1.9, 2.1, 60 s at 5, 25, 50 WPM in A, B, Ultimatic | REQ-SYS-184 | section 6.1 | not applicable |
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
| REQ-SYS-054 | 128 identical elements (unchanged) or 30 s (unchanged) without a key-up gap of at least 2 dit times at the selected speed (changed from 7 dit times or 500 ms) | 6.2 | **else a CR: triggered** (PCR-9 row "REQ-SYS-054") | 25.4 s window, count 2.3 x |
| REQ-SYS-184 | the longer of 2 s and 20 dit times at the selected speed (changed from 2 s; the branch names 16 dits) | 6.1 | **CR branch triggered** (PCR-8), with 20 in place of 16 | 188 ms minimum; 455 ms at 5 WPM |
| REQ-SYS-131 | 2 s (unchanged); design watchdog load 1.0 s | 6.5 | confirm | 0.9 s |
| REQ-SYS-188 | 120 s (unchanged) | 6.6 | confirm | 30 s to 150 s |
| REQ-SYS-189 | 60 s (unchanged) | 6.6 | confirm | 2 x |
| REQ-SW-KEYER-036 | unchanged; "no plug" = detect input reads high | 6.7 | confirm (circuit kept) | not applicable |

No value goes to the owner before this note's record is APPROVED (plan rule C10). Proposed values carry no TPM.

## 9. Consequences for other products (requests to their writers; plan section 5.3)

- **CR triggers.** PCR-8 (REQ-SYS-184) and the REQ-SYS-054 item of PCR-9 are triggered. The CR changes REQ-SYS-184 and REQ-SYS-054 (statements, rationales, verification notes), their mirrors NGO-021 and MOE-012 ("2 s for a squeeze", "7 dit times or 500 ms"), HZ-004 K4 text and its two `tbr` items, `docs/conops/conops.md` Table 3.4-1 Transmit-keyed row, Table 3.4-4 row 3, section 3.5.1 item 10 and OPS-013, the concept section 7 and 14 item 3 values, TC-SYS-038, and the ICD-CTL-KEY TBR row "Paddle watchdog time cap" (which still reads "128 identical elements or 10 s"). Each CR gets its section 6 impact review from a separate invocation before the owner is asked (rule C6).
- **R-1 (WP-PDR-32, firmware architecture):** watchdog load 1.0 s, fed from the main loop only after every safety monitor has run.
- **R-2 (WP-PDR-32, firmware design rules; WP-PDR-41):** no configuration-store write in Transmit-keyed or while a key input reads closed; defer it to Receive after the hang time.
- **R-3 (WP-PDR-35, SW L2):** the squeeze limit child states its dit count against the build ratio; a ratio change re-derives it (A-2).
- **R-4 (WP-PDR-16, hazard analysis):** HZ-004 K9 and HZ-010 K3 credit REQ-SW-KEYER-036 for the tip line only; the ring-line short with no plug is covered by K1, K3 and K4.
- **R-5 (WP-PDR-35 and WP-PDR-16):** consider re-running the interlock on a plug-presence change from no plug to plug; headphones or a shorted cable inserted after boot would then never key, instead of keying up to the squeeze limit. This is a candidate SW-KEYER requirement, not a value of this study.
- **R-6 (requirements writer, WP-PDR-11 then WP-PDR-45):** REQ-SYS-053 `tbr.plan` says "configurable range (2 to 6 s)"; SRR decision 48 leaves only the switchpoint and the debounce operator-set, so the range is a build parameter. The REQ-SYS-184 rationale says keying resumes "once either contact opens", while `docs/conops/conops.md` Table 3.4-4 row 3 clears the inhibit when "both paddle contacts are confirmed open"; one of the two changes (the analysis is unaffected).
- **R-7 (WP-PDR-45):** the HZ-004 K4 `tbr` plan names "HostUnit replays of recorded normal sending"; no recording exists. This study uses the synthetic corpus of section 3.4; a recording from the owner's WP-PDR-40 session, if made, is replayed through `paddle_watchdog` before the ruling.

## 10. Tools, credit and verification route

| Tool | Version | TV record | Use |
|---|---|---|---|
| venv Python | 3.13.5 | TV-001 (accredited for schema validation only) | interpreter |
| `keyer_model.py`, `check_keyer_host_study.py` | this commit | none | every number of sections 5 and 6 |
| matplotlib | 3.11.2 (venv) | none (plots only) | three plots |

Because the model has no TV record, its results are developer evidence (05 section 9.1; checklist item CK-ANA-C2): they neither close a requirement nor go to the owner as TBR values until a TV record covers the model or the owner rules on the basis of developer evidence (owner action proposed in the author's return). HostUnit credit was the plan's first route (WP-PDR-33 "Tools: HostUnit"): it becomes available when WP-PDR-41 delivers the `cwht-core` keyer and WP-PDR-08 accredits the Rust toolchain (TV-020 to TV-022); the TC-SW-KEYER cases for REQ-SW-KEYER-022 and 026 and the SW-SAFE children of REQ-SYS-054 and 184 then replay the section 7 cases on the flight code. REQ-SYS-052 to 054, 131, 184, 188, 189 are Test-method requirements closed by Bench cases after TRR; this analysis is supporting evidence only (04 section 5.1).

## 11. Limitations

- L-1. The model is not the flight keyer. Ultimatic memory details and the tie rule are the author's; the F7 vectors do not cover Ultimatic.
- L-2. No recorded sending: the corpus is synthetic and the operator timing is bounded by profiles, not measured.
- L-3. The character table (I-12) is transcribed without the standard in the corpus.
- L-4. Flash timing (A-7) and boot time (A-8) are assumptions until the WP-SW-08 note and a dev-board boot measurement.
- L-5. The squeeze limit in dits holds for the build ratio 3.0 only (A-2).

## 12. Change history

| Date | Revision | Change |
|---|---|---|
| 2026-09-27 | 1 | First issue for the F0 freeze (WP-PDR-33, wave 1a) |
