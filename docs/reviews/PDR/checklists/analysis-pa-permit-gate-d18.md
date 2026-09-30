---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-22 D-18 PA-permit
# gate analysis (level interface, unpowered states, single faults and the A5 key-up case). Iteration 1 (full
# review, rule C2) at freeze commit 078f2f7, revision 0. Iteration 2 (delta on the Major fix, rule C1) at the
# re-freeze commit c397ab1, revision 1; the reviewer's verdict is APPROVED at iteration 2, but the record verdict
# is held at NEEDS CHANGES until the software assurance pair (INSP-120) returns APPROVED and CR-012 merges.
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Submitted, not merged). tools/validate_docs.py
# requires the checklist field to name a template that exists on main, so the field names
# peer-review-checklist-design revision B, and checklist_analysis records the template actually applied.
# Filing (lead SE, per the iteration 2 reviewer's filing note): id INSP-119 (the id iteration 1 was given);
# iteration 1's front matter values, body and findings table first, iteration 2's section after; iteration 1's
# Minor count (5) added to findings_minor and findings_deferred; iteration 2's new Minor findings kept as
# finding-21 to finding-25.
# The software assurance pair (plan WP-PDR-22 "SA pair") is a separate invocation, record INSP-120,
# docs/reviews/PDR/checklists/analysis-pa-permit-gate-d18-software-assurance.md.
id: INSP-119
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-pa-permit-gate-d18.md
product: docs/design/analysis/pa-permit-gate-d18.md
product_commit: "c397ab171b4c564c402f806bd617a796e74a96d1"
product_files: ["docs/design/analysis/pa-permit-gate-d18.md@a6bcc2b14710730d6c5bee3a61a4cbcfda919e19", "hardware/sim/tx-pa-permit/d18_run.py@5a06cfd879f2f885a42f41fcb7667be42abaa48e", "hardware/sim/tx-pa-permit/d18_keyup.cir@bce02858a570d9f7decc4d9910fe73caaee0ecea", "hardware/sim/tx-pa-permit/d18_seq.cir@de50be4d518f8a117e7b1ce627d72e7f91e695c5", "hardware/sim/tx-pa-permit/d18_asis.cir@191ba96d9acfbf5cbebd7401458080297567ce68", "hardware/sim/tx-pa-permit/README.md@f085dc40f83668fda775303dd5d2a734462dde5d", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/result.json@72ec935d2d26d0d0c5285b4f4a0de2825f9c8215", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/result.csv@e0d930735be99bfdb537e39c454d74e0f1be3a8f", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/raw.sha256@fcfa74faa7999ed69eeba0440ed0fa0b35b3992d", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/result.json@66e3ce29fb12b01ede582f40533a84e6a9a59414", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/result.csv@1166f1f51e0f521dc57042f78feb49a6dfd16002", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/d18_seq.raw@78d72824b470f439e1cefe59e75ba7ae5e9f6d71", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-summary/summary.json@df81781b6176c18fe729cb340c717cd0489696e6", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/result.json@1b1a51f9f521260e65007c3a3f429721b5f093dc", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_keyup.png@3fb64a679b62fb090e8b3afb498e0eee150d5476", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_timeline.png@097c0c3a89cc1d903575473bcbb8801093a58d06", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/keyup_timeline.png@0f2baec0ca34108fb9dc60decd743494620ab0c6", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/keyup_edges.png@28d9fde0d5c8c48daceac94de4ff6a770e853d05", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/keyup_metrics.png@6a09ad7a48e070b0b6e568de76126ea0a0cb46f1", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/level_cases.png@1e96eecf124c3acaf937807924b5c2d2bb8cd99e", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/off_states.png@07640f12eab0dbb725dfeb3b8f54696d6c08a2ee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/seq_cases.png@2b60e05ff102ab1ed99accaa4807b4ceef70a2aa", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/cutoff_levels.png@34e92fde1007c0c021fa4ce63f06e94bcab3f753"]
product_commit_iteration_1: "078f2f7618be52a9d35d2133e77778c8d0582d17"
product_files_iteration_1: ["docs/design/analysis/pa-permit-gate-d18.md@b8361270902be239833ca9e33e1a2571226c9a3c", "hardware/sim/tx-pa-permit/README.md@cf1c08881eaf66756e469ae8f1994a6a514fab9c", "hardware/sim/tx-pa-permit/d18_asis.cir@191ba96d9acfbf5cbebd7401458080297567ce68", "hardware/sim/tx-pa-permit/d18_keyup.cir@c0bdd5158cacc9882626b7f8bf0930105950f5b7", "hardware/sim/tx-pa-permit/d18_run.py@a6916e0fb481586516c7e7901d45c3a4fc4c442a", "hardware/sim/tx-pa-permit/d18_seq.cir@16ea43784e87230b66f2e13f2a0b8ae7526e4e39", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_keyup.png@3fb64a679b62fb090e8b3afb498e0eee150d5476", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_timeline.png@097c0c3a89cc1d903575473bcbb8801093a58d06", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/d18_asis.cir@191ba96d9acfbf5cbebd7401458080297567ce68", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/d18_run.py@a6916e0fb481586516c7e7901d45c3a4fc4c442a", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/raw.sha256@9072b7b3276aa1905b5366841e65e6b02dcebcee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/result.csv@95058940fd97ff6d87ab58fa3140fce82bb0557b", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/result.json@1b1a51f9f521260e65007c3a3f429721b5f093dc", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/d18_keyup.cir@c0bdd5158cacc9882626b7f8bf0930105950f5b7", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/d18_run.py@a6916e0fb481586516c7e7901d45c3a4fc4c442a", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_edges.png@4f639026aaa8d12cced8b42bc45b8737f062b463", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_metrics.png@76a212c0e3a50d250a4bfa8c7b853c7e820b18a0", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_timeline.png@29a7879235e3ede67f507e861dc13706243ee634", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/level_cases.png@890bf7cbf4b2a658b36efd0ead7b939e7631c1c7", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/raw.sha256@4584e215e2e6193cff4aa389e1c652e9e6416a11", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/result.csv@5996e4c05c40a78b5049674b735c71f260051740", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/result.json@ee1c17713701dae4c97ba1a9ab7cacb6129c9e1d", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/d18_run.py@a6916e0fb481586516c7e7901d45c3a4fc4c442a", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/d18_seq.cir@16ea43784e87230b66f2e13f2a0b8ae7526e4e39", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/result.csv@bda5014d1f456ca951c2cf45138007f76d9dd4d5", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/result.json@d2741ca5c5c631222a63f7e137de98ea8183c55c", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/seq_cases.png@74a7aeee4411e8b7214738152c9812e6cf4a7fee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-summary/d18_run.py@a6916e0fb481586516c7e7901d45c3a4fc4c442a", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-summary/summary.json@6f2999468754221e855e71153fdcb2e4c75069ac"]
analysis_kind: [simulation-deck, worst-case, budget]
analysis_kind_iteration_1: [simulation-deck, worst-case, timing]
product_size: "iteration 2: 1 note (550 lines, 11 sections, revision 1), 1 checker and generator (1256 lines), 3 generated decks (key-up 52 corners, as-drawn 36, sequencing and faults 20: 7 new in revision 1), 21 static datasheet checks (6 new), 4 isolation cases x 5 RF-off state rows (new section 5.8), 9 plots (2 new: off_states.png, cutoff_levels.png). Iteration 1: 1 note (434 lines, revision 0); 1 generator and checker (1026 lines); 3 generated decks (52 + 36 + 13 steps); 4 runs; 7 plots; 15 static datasheet checks; 16 input rows"
tools_used: ["LTspice 26.0.2 through tools/ltspice-batch.sh (TV-014, ACC-LTSPICE-001; .log first line 'LTspice 26.0.2 for MacOS' in d18r1-keyup and d18r1-seq)", "venv Python with numpy, matplotlib and spicelib 1.6.3 (checker d18_run.py has no TV record: developer evidence per 05 section 9.1, as the note's Evidence status row states)"]
values_proposed: ["REQ-TX-014: 1 uW (-30 dBm), TBR kept"]
renders_inspected: 9
renders_inspected_iteration_1: 7
sprint: PDR-prep
author_agent: "author:WP-PDR-22 D-18 gate analysis (Claude as analysis author; revision 0 078f2f7, revision 1 c397ab1)"
reviewer_agent: "reviewer:WP-PDR-22-d18-iter2 (independent analysis reviewer; authored no part of WP-PDR-22, the note, its decks, its checker, TS-012 or ADR-056)"
reviewer_agent_iteration_1: "reviewer:WP-PDR-22-analysis-d18-iter1 (independent invocation; authored no part of the note, decks, checker, TS-012, INSP-110 or INSP-118)"
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/analysis-pa-permit-gate-d18-software-assurance.md (plan WP-PDR-22: reviewer plus SA; the SA finding-1 fix of revision 1 is verified there)"
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
reviewer_verdict_iteration_1: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 10
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 10
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A6, CK-ANA-D2, CK-ANA-H2, CK-ANA-I2]
items_no_iteration_1: [CK-ANA-A1, CK-ANA-A3, CK-ANA-A4, CK-ANA-B3, CK-ANA-C1, CK-ANA-D2, CK-ANA-E3, CK-ANA-E4, CK-ANA-F1]
effort_turns: 115
effort_minutes: 150
record_status: Open
date: 2026-09-29
date_closed: null
---

# Peer review record INSP-119: D-18 PA-permit gate and the A5 key-up case (WP-PDR-22)

## Iteration 1 (2026-09-29; revision 0 at `078f2f7`)

**Product:** `docs/design/analysis/pa-permit-gate-d18.md` revision 0 (blob `b8361270`, as the author's brief states) with `hardware/sim/tx-pa-permit/` (README `cf1c0888`; generator and checker `d18_run.py` `a6916e0f`; decks `d18_keyup.cir`, `d18_asis.cir`, `d18_seq.cir`; runs `2026-09-29-d18-keyup`, `-asis`, `-seq`, `-summary`) at freeze commit `078f2f7` (rule C2). All 29 blobs of `product_files` equal `git rev-parse 078f2f7:<path>` and `HEAD:<path>` at HEAD `9c40ef9`; `git hash-object` of the working-tree note is `b8361270`.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck, worst-case (extreme-value corners and datasheet-limit arithmetic) and timing (turn-on, turn-off and the interval-13 fallback edge): sections A to F, G1, G6, G7, H, I and J apply. G2 to G5 are N/A.

**Acceptance criteria (rule C7; texts read at HEAD):**
- REQ-TX-014 (`docs/requirements/tx/requirements.md`): "at most 1 uW (TBR) while TX_KEY is deasserted with PA_EN asserted and the exciter driven"; verification note: closing bench test at 144.0012, 146.000 and 147.9988 MHz; method Test.
- REQ-SYS-120: "produce RF output only while both a keyer key-down and a separately maintained PA permit are asserted"; rationale: "RF off is the REQ-SYS-183 level"; HZ-004 K8 (SWE-134 f, i).
- REQ-SYS-183: "at or below -57 dBm (TBR) in every state with RF ended, inhibited or off".
- INSP-118 finding-9 (a), (b), (c) and its Fix text (state the rail and a level interface taking the P-FET gate to its source rail and the clamp gate to full drive; bias resistors for an unpowered or floating gate output; the power-up order; the fallback's driver power-up time); INSP-110 finding-24 (same defect; the key-up case with the realised gate).
- Operating temperature -10 to +45 C (REQ-SYS rationale "-10 to +60 C" display bound, verification "every part's rated range against -10 to +45 C").

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (the D-18 analysis and the INSP register) preceded every `grep`; `grep` only pinned lines in TS-012, INSP-110, INSP-118, the requirement files, the research note, `pa-drive-ts012.md`, `keying-ts012.md`, `spurs-ts012.md` and the checker. The rustos tree was not read.

**Reviewer re-run (CK-ANA-C4).** `git archive 078f2f7` exported to the scratchpad; from the export, `.venv/bin/python hardware/sim/tx-pa-permit/d18_run.py keyup`, `asis`, `seq`, `summary`, every LTspice run through the export's `tools/ltspice-batch.sh` (blob `88b71475`). Results:
- `keyup`: wrapper PASS, `version_line='LTspice 26.0.2 for MacOS'`, deck sha256 `20048185...`; "52 cases; criteria failing: none"; L1 -58.3, L2 -38.8, L3 -88.3, L4 -34.0 dBm; t_on 0.53 to 1.20 us; VGS permitted -4.708 to -4.258 V; drop 6.90 to 11.15 mV; key-up VGS -1.4 uV; driver 0.34 to 0.38 mV; t_off 0.768 to 0.782 ms; clamp gate 4.75 to 5.25 V; VGG up to 7.90 mV. Exit 0.
- `asis`: "36 cases; driver powered at key-up in 25; REQ-TX-014 (L1) fails in 21". Exit 0.
- `seq`: every case PASS or as expected; "not as required: none". Exit 0.
- `summary`: analytic equals simulated worst for L1 to L4; break-even 21.23 / 26.01 dB; 15 static checks PASS. Exit 0.
- Byte comparison with the frozen files: every `result.json`, `result.csv`, `summary.json`, every generated deck and all 7 PNGs are identical. `.log` files differ only in the temp directory, start time and elapsed time; each regenerated `.raw` differs in 9 or 10 header bytes (date) and has the committed size.

**Independent checks (CK-ANA-B5).**
- Key-up level, hand chain: L1 = 10 log(26.5) + 3.00 - 22.5 = -5.27 dBm into the GVA-84+; -5.27 - 19.57 - 3.00 - 30 - 0.5 = **-58.34 dBm**. L4: 10 log(48.6) + 3.00 - 25.3 + 18.42 - 13.48 = -0.49 dBm; -0.49 - 0 - 3.00 - 30 - 0.5 = **-33.99 dBm**. Unpowered isolation: Rf = 50 (1 + 10^(24.1/20)) = 851.6 ohm; 100 / 951.6 = -19.57 dB. All agree with the checker to 0.05 dB.
- Turn-off: 2.2 kohm x 100 nF = 0.22 ms; from about 3.1 V to 0.1 V takes 0.22 x ln 31 = 0.755 ms, plus about 20 us to reach 3.1 V: **0.775 ms** against 0.768 to 0.782 ms simulated.
- VGS permitted: (4.75 - 0.05 regulator and bead drop - 0.02) x 10/11 = 4.25 V against 4.26 V simulated at the 4.75 V bus.
- MOSFET fits, reviewer operating-point deck (`fitchk.cir`, scratchpad, through the wrapper, PASS): DMP3099L fit at VGS -4.5 V, Vto -2.1 V: **99.5 mohm** (datasheet 99 mohm max, agrees). 2N7002 fit at VGS 4.5 V: **4.86 ohm**, against the note's "5.3 ohm at 4.5 V" (finding-3).
- Wound-loop VGG: 5.25 V x 4.07 ohm / 2.7 kohm = 7.9 mV (the fit at VGS 5.25 V), equal to the simulated 7.90 mV.

**Sources re-read by the reviewer (2026-09-29), each fetched through the web-fetch tool and read with pdftotext; every SHA-256 equals the prefix the note gives.**
- Nexperia 74LVC1G11 Rev. 13.1 (`9588c447...bae09`), Table 7: VIH 2.0 V and VIL 0.8 V at VCC 2.7 to 3.6 V; VOH VCC - 0.1 V at -100 uA and 2.3 V at -24 mA, VCC 3.0 V (-40 to +85 C); IOFF +/-2 uA; II +/-1 uA; recommended VI 0 to 5.5 V; "Schmitt-trigger action at all inputs". Agree.
- Diodes DMP3099L DS36081 Rev. 5-2 (`06f30303...b442c`): VGS(th) -1.0 to -2.1 V at -250 uA; RDS(on) 99 mohm at -4.5 V; IDSS -800 nA at -30 V; IDM -11 A; Ciss 563 pF; Crss 41 pF; RG 10.3 ohm. Agree. Figure 7 was not re-read (the hot threshold is labelled DD/E).
- onsemi 2N3903/D Rev. 9 (`4a32e2ab...77b8d`): 2N3904 hFE 40 at 0.1 mA and 70 at 1 mA; VCE(sat) 0.2 V and VBE(sat) 0.65 to 0.85 V at 10 mA / 1 mA; ICEX 50 nA; ts 200 ns. Agree.
- Nexperia 2N7002 Rev. 7 (`cc9c2754...46475`), Table 7: VGSth 1 / 2 / 2.5 V (25 C), 0.6 V min (150 C), 2.75 V max (-55 C); RDSon 5 ohm (10 V, 25 C), 9.25 ohm (10 V, 150 C), 5.3 ohm (4.5 V, 75 mA); IDSS 10 uA (150 C); IGSS 100 nA. Agree.
- TI LM393 SLCS005AH (`f28830c2...e9456`): two tables (finding-4).
- Mini-Circuits GVA-84+ Rev. F (`49daf1cb...be95`): device 4.8 / 5.0 / 5.2 V; 85 / 108 / 130 mA; 0.058 mA/mV; gain 22.9 / 24.1 / 25.3 dB at 0.1 GHz; input +13 dBm. Agree.
- In-repo: `pa-drive-ts012.md` (26.5 mW in service; 48.6 mW fixed-pad maximum at any coax length; highest corner gain 25.3 dB, lowest 22.5 dB at 148 MHz; pads 18.42 dB and 3.00 dB; set 13.48 to 22.04 dB), `keying-ts012.md` (0.5 dB LPF and relay; 43 dB module check), `spurs-ts012.md` F3, `docs/research/keyer-verification-and-key-input-network.md` (Table 1436; RP2350-E9), TS-012 revision 8 (sections 7.3, 8.10 row REQ-TX-014, rows 12 and 23, section 8.4 USD 299.83). Agree.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-E3, F1, A1 | note header "Serves" row; section 1 table row "REQ-SYS-120 (hardware half)"; Summary; section 5.4 table (column "Information: REQ-SYS-183 ... if a fault left CLK1 on after the over"); section 6.2; section 7 F-3; `keyup_timeline.png` panel 5 | **REQ-SYS-120 is reported as served on a state proxy, but its own RF-off level is not met at the bounds and only 1.3 dB inside it on the estimates, in normal operating states.** REQ-SYS-120 requires RF output only while both key-down and the permit are asserted, and its rationale defines RF off as the REQ-SYS-183 level, -57 dBm. The note checks REQ-SYS-120 only as "driver unpowered and VGG clamped". By the note's own chain, every state with CLK1 running, the relay in TX and only one condition asserted gives the key-up level: -58.3 dBm on the estimates (+1.3 dB, far inside the uncertainty of the 19.6 dB and 30 dB isolation estimates), -38.8 dBm at the GVA-84+ passive bound and -34.0 dBm at the drive bound (18.2 and 23.0 dB over). Those states are not faults: between elements and in the hang time (TX_KEY low, PA_EN asserted, the REQ-TX-014 state), and in the interval-13 fallback from the relay close (about 7.5 ms) to PA_EN at 11 ms (TX_KEY high, PA_EN low). The note gives the -57 dBm comparison only as information for a firmware fault that leaves CLK1 on after the over, and section 6.2 proposes HZ-004 K8 wording on the state alone. INSP-118 (context row, TS-012 section 7.3) made TS-012's "-61 dBm, under REQ-SYS-183's -57 dBm" claim "subject to finding-9"; the fix of finding-9 now shows that claim does not hold at the bounds, and the note does not say so for REQ-SYS-120. **Fix:** add REQ-SYS-120 / REQ-SYS-183 rows to the section 1 and 5.4 tables for these states, with the margins (+1.3 dB estimate; -18.2 and -23.0 dB at L2 and L4) and their uncertainty; do not report the hardware half of REQ-SYS-120 as met at its level; correct F-3 (normal states, not only a fault); and route the conflict to the requirement owner, CR-018, WP-PDR-16b and WP-PDR-23 as a finding: REQ-TX-014 allows 1 uW in the state where REQ-SYS-120's rationale requires -57 dBm (for example, scope REQ-SYS-120's "RF off" to exclude the key-up state that REQ-TX-014 governs, or add isolation). The REQ-TX-014 result and the gate design are not affected | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-ANA-D2, E4 | note section 5.7 row F2; `d18_run.py` `seq_cases()` F2 `expect` and `analyse_seq()`; `seq_cases.png` panel F2 | **The F2 row does not match its simulation, and the checker does not test what the row claims.** The row says the driver "stays on after TX_KEY falls (gate charge held)". In the run the driver is at 4.96 V from t = 0, before any permit (reviewer read of `d18_seq.raw` step 10: VGS -3.32 V at 0 to 4 ms). With the 10 kohm open the gate floats, and its state is indeterminate from power-up. The checker's expected state reads only the value at the end of the run, so it cannot tell the two apart. The consequence (driver on at key-up; REQ-TX-014 fails; latent) is unchanged. **Fix:** describe F2 as "driver state indeterminate, on at any time", as F3; make the expectation test the pre-permit window too | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-B3 | note section 3.1 "2N7002: VDMOS ... and 5.3 ohm at 4.5 V"; `d18_run.py` `MODELS` comment | **The 2N7002 fit is stated wrongly.** The model gives 4.86 ohm at VGS 4.5 V (reviewer operating-point run), 8 % under the 5.3 ohm datasheet maximum it is said to equal. The simulated VGG clamp is therefore slightly optimistic (7.9 mV against about 10.3 mV at 5.3 ohm). The static check at the 150 C value (9.8 ohm, 19 mV) covers the result, so no conclusion changes. **Fix:** state the fit value, or set Rd + Rs so that the fit gives 5.3 ohm at 4.5 V | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-A4 | note section 4 row "LM393"; section 5.2 rows "Q high" and "Q low"; `d18_run.py` `static_checks()` | **The LM393 values mix the two tables of SLCS005AH.** IOH-LKG 20 nA max comes from the LM393B table (VOL 400 mV, 550 mV at -40 to +85 C). VOL 700 mV "full range" comes from the legacy LM393 table, whose full range for the LM393 is 0 to 70 C, so it does not cover the -10 C operating minimum. The Q low check (0.7 V against VIL 0.8 V) would hold with more margin on the LM393B figure. **Fix:** name the die the design buys (to WP-PDR-26 with F-4), and take both values from its table and temperature range | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-A3, C1, F1 | note section 4 row "RP2350 GPIO"; header "Tool" row; section 5.4 | **Source tags, tool versions and the frequency coverage are not stated.** (i) The research note is cited without its finding number and confidence tag; its E9 leakage is "typically around 120 uA", with Medium confidence for a worst case (research note confidence table, row F3). (ii) The Tool row names spicelib 1.6.3 but not the Python, numpy and matplotlib versions. (iii) REQ-TX-014 names 144.0012, 146.000 and 147.9988 MHz. The analysis covers them through band-worst inputs (the 48.6 mW highest corner at 144 MHz, the 22.5 dB lowest gain at 148 MHz) and isolation estimates that do not depend on frequency, but the note does not say so. **Fix:** add the tag, the versions and one sentence on the frequency coverage | Open | Pending | |

## Per-case results

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Key-up window, TX_KEY low, PA_EN asserted, CLK1 running; 52 corners; L1 estimates | REQ-TX-014: at most -30 dBm | -58.3 dBm | +28.3 dB | GVA-84+ unpowered 19.6 dB (E, 0 dB bound) and module 30 dB (E) | re-run and hand chain: -58.34 dBm | none |
| C-2 | As C-1, L2 (GVA-84+ passive bound) | REQ-TX-014: -30 dBm | -38.8 dBm | +8.8 dB | module 30 dB (E) | re-run: same | none |
| C-3 | As C-1, L3 (module 60 dB) | REQ-TX-014: -30 dBm | -88.3 dBm | +58.3 dB | "up to 60 dB" is not a limit | re-run: same | none |
| C-4 | As C-1, L4 (drive bound, passive bound) | REQ-TX-014: -30 dBm | -34.0 dBm | +4.0 dB | module 30 dB (E) | re-run and hand chain: -33.99 dBm | none |
| C-5 | 144.0012, 146.000, 147.9988 MHz | REQ-TX-014 test frequencies | covered by band-worst drive and gain inputs; not stated in the note | as C-1 to C-4 | as C-1 to C-4 | checked against `pa-drive-ts012.md` corners | finding-5 |
| C-6 | One-condition states with CLK1 on and the relay in TX (between elements, hang time, fallback 7.5 to 11 ms) | REQ-SYS-120 via REQ-SYS-183: at most -57 dBm | L1 -58.3, L2 -38.8, L4 -34.0 dBm (same chain; note reports REQ-SYS-120 on the state only) | +1.3, -18.2, -23.0 dB | as C-1 to C-4 | hand chain: same | finding-1 |
| C-7 | P-FET VGS, key-up window, threshold -0.73 (hot E), -1.0, -2.1 V | finding-9 (a): at most 0.3 V magnitude | 0.000 V (-1.4 uV) | +0.3 V (threshold margin 0.73 V) | hot collector leakage 0.05 V (E) | re-run: same | none |
| C-8 | Driver supply in the key-up window; below 0.1 V after TX_KEY falls | at most 50 mV; at most 1 ms | 0.34 to 0.38 mV; 0.768 to 0.782 ms | +49.6 mV; +0.22 ms | hot IDSS x 2.2 k 0.11 V (E) | re-run; hand RC 0.775 ms | none |
| C-9 | Clamp gate and VGG in the key-up window, loop nominal and wound to 5.25 V | at least 4.0 V; at most 50 mV | 4.75 V; 7.9 mV | +0.75 V; +42.1 mV | 2N7002 fit (finding-3); 150 C static 19 mV | re-run; hand 7.9 mV | finding-3 |
| C-10 | Permitted: VGS, drop, turn-on, inrush, bus dip | -4.0 V; 30 mV; 0.25 ms; 11 A; 100 mV | -4.26 V; 11.1 mV; 1.2 us; 2.44 A; 39 mV | 0.26 V; 18.9 mV; 0.249 ms; 8.6 A; 61 mV | regulator and bead dynamics (E) | re-run; hand VGS 4.25 V | none |
| C-11 | Interval-13 fallback, 4 cases | finding-9 (c): turn-on at most 0.25 ms | 0.55 to 1.2 us | +0.249 ms | as C-10 | re-run: same | none |
| C-12 | Only one of PA_EN and TX_KEY high, before the permit | at most 50 mV at the driver | under 1 uV | +50 mV | none material | re-run: same | none |
| C-13 | Power-up orders S1, S2; brown-outs S3, S4 | finding-9 (b): driver at most 0.1 V and VGG at most 0.1 V (2.0 V while a rail ramps) when not permitted | S1 36 mV, VGG 1.05 V in the ramp; S2 36 mV, 1.07 V; S3, S4 off | +64 mV; +0.95 V | regulator LC ringing (E) | re-run: same | none |
| C-14 | Single lines L1 to L4; U1 open F1 | HZ-004 K8: no single line powers the driver | off throughout | pass | none | re-run: same | none |
| C-15 | Component faults F2 to F5 | expected states (section 5.7) | as expected | not applicable | F2 description (finding-2) | re-run: same; raw read for F2 | finding-2 |
| C-16 | As drawn in TS-012, 36 cases | expected defect | powered in 25; REQ-TX-014 fails in 21, up to -14.7 dBm | not applicable | as C-1 | re-run: same | none |
| C-17 | Static datasheet checks (15 rows) | datasheet limits | all PASS | smallest +0.037 mA (base current), +0.10 V (Q low) | LM393 table (finding-4) | recomputed from the re-read datasheets | finding-4 |

## Readiness

| # | Criterion | Evidence |
|---|---|---|
| R1 | Frozen | 29 of 29 blobs equal at `078f2f7` and HEAD `9c40ef9`; note blob `b8361270` as the brief states |
| R2 | Checker runs by the note's commands | four stages, exit 0 each, through the wrapper (re-run above) |
| R3 | validate_docs for a JSON product | N/A: no JSON under a schema |
| R4 | Author return complete | question, inputs with sources, results with margins, limitations, the proposed value and the tools are in the note and the summary |
| R5 | No TBD | 0 hits in the note; REQ-TX-014 TBR named with its value |
| R6 | Renders exist | 7 PNGs next to their runs |

## Checklist answers

**A. Question, scope, inputs.**
- A1 No (finding-1): REQ-SYS-120 is named as served but is checked against a state, not its level.
- A2 Yes: TS-012 revision 8 (`bb5dee7`) sections 7.3, 8.1, 8.14 D-18 and E5 (g); A5 is the owner's choice.
- A3 No (finding-5 (i)); every other input has a datasheet with revision, page and hash, or a labelled estimate.
- A4 No (finding-4). Every other input that sets a result was checked against its source (list above).
- A5 Yes: the estimates are labelled E, bounded by passivity (L2) and the drive bound (L4), and their direction is stated.
- A6 Yes: every consequence is a request (F-1 to F-5, R-1 to R-3); no requirement, interface or hazard file is edited.

**B. Model validity.**
- B1 Yes: behavioural U1, fitted MOSFETs and a GVA current law, each stated with its effect (section 8).
- B2 Yes: the 2N3904 model is identified as the published Fairchild/onsemi model, with beta stepped.
- B3 No (finding-3); the DMP3099L fit agrees at 99.5 mohm.
- B4 Yes: 20 us maximum step and `plotwinsize=0`. The edges that matter (1 us turn-on, 0.78 ms turn-off) are resolved (`keyup_edges.png`), and the steady results do not depend on the step.
- B5 Yes (independent checks above).
- B6 Yes: the uncertainty is carried as the L1 to L4 bounds and the hot-leakage multipliers, and the note states that the closing evidence is the bench test.

**C. Tools.**
- C1 No (finding-5 (ii)); the LTspice log line equals the lock version.
- C2 Yes: TV-014 is accredited for the run, and the checker's numbers are marked developer evidence.
- C3 Yes: netlists only, one `.tran` per deck, generated and run by one command per stage.
- C4 Yes (re-run above).
- C5 Yes: TV-014 limitation 1 (nonlinear devices and `.step` not validated by the TV record) is met by the note's own model checks, subject to finding-3.

**D. Units and arithmetic.**
- D1 Yes.
- D2 No (finding-2); every other number in the note equals the checker output.
- D3 Yes: rounding toward the limit (for example -34.0 dBm from -33.99).
- D4 Yes: `REQ_TX_014_DBM = -30.0` and `REQ_SYS_183_DBM = -57.0`, with each criterion's reason in `CRIT`.

**E. Results and credit.**
- E1 Yes.
- E2 Yes: limit minus result.
- E3 No (finding-1).
- E4 No (finding-2, the F2 expectation). Every other criterion is asserted, with exit 3 on failure.
- E5 Yes: the REQ-TX-014 TBR is kept at 1 uW with its margins, the TBR plan's TS-003 step is taken by this analysis under TS-012, and no requirement file is edited.
- E6 N/A: no TPM.
- E7 Yes: REQ-TX-014 is a Test requirement; the analysis is stated as supporting, with TC-TX-014 closing.

**F. Every case named.**
- F1 No (finding-1 for REQ-SYS-120; finding-5 (iii) for the frequencies, covered in substance).
- F2 Yes: stuck lines, brown-outs, U1 open or unpowered and the component faults.
- F3 Yes: the corners combine bus, rails, threshold, beta and the loop state.
- F4 Yes: the smallest REQ-TX-014 margin (L4, 4.0 dB) is shown against its two driving inputs (drive level and the GVA-84+ isolation).

**G1.**
- G1-1 Yes.
- G1-2 Yes: one `.tran` per deck, no `NC_` nets.
- G1-3 Yes: the part values equal section 2 and TS-012 D-18 as revised.
- G1-4 Yes: the checker reads the `.raw` through spicelib, and replot refuses a deck that differs from the run's.

**G6.**
- G6-1 N/A: hardware edges only, no firmware time base.
- G6-2 Yes: the gate delay (ns), transistor storage (200 ns max) and RC edges against the 2 ms and 0.5 ms leads.
- G6-3 Yes: no Emulation.
- G6-4 Yes: HZ-004 K8. The turn-off (0.78 ms to under 0.1 V; clamp under 0.12 us) completes before the next element.

**G7.**
- G7-1 Yes: extreme value.
- G7-2 Yes: the temperature extremes of the thresholds and leakages are applied (hot and cold); ageing is N/A for this part set.

**H. Hazards, risks and records.**
- H1 Yes: HZ-004 K5 and K8, with requests to WP-PDR-16b (section 6.2, R-1). The wording is subject to finding-1.
- H2 Yes: the cost effect on the A5 ordering gate (USD 299.83 becomes about 300.55 to 300.88) is routed to the TS-012 author and the ordering-gate recompute.
- H3 Yes: revision 0, dated.

**I. Visual closure.**
- I1 Yes: all 7 cited PNGs were opened with the Read tool (`asis_keyup`, `asis_timeline`, `keyup_timeline`, `keyup_edges`, `keyup_metrics`, `level_cases`, `seq_cases`).
- I2 Yes: axes are labelled with units (the `keyup_edges.png` turn-on panel titles carry the quantity), limits are drawn, legends are present, and the plotted values agree with the checker at the marked points.

**J. Software assurance items** (answered by this reviewer for the engineering content; the SA pair answers them in its own record).
- J1: TV-014 is accredited; the checker has no TV record and is developer evidence.
- J2: the analysis supports SWE-134 item i (no single line or flag produces RF) for the driver-supply and clamp states. The RF level of REQ-SYS-120 in one-condition states is finding-1.
- J3: no SWEHB tasks are claimed here; they go to the SA pair.

**ITEMS N/A:** CK-ANA-G2 to G5 (not a budget, thermal, RF-exposure or cascade analysis); CK-ANA-E6 (no TPM); CK-ANA-G6-1.

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/pa-permit-gate-d18.md@b8361270902be239833ca9e33e1a2571226c9a3c (and the 28 hardware/sim/tx-pa-permit blobs of product_files) at 078f2f7
FINDINGS:
- [Major] finding-1 CK-ANA-E3, F1, A1: REQ-SYS-120 reported served on a state proxy; its RF-off level (REQ-SYS-183, -57 dBm) in normal one-condition states is +1.3 dB on the estimates and -18.2 / -23.0 dB at the bounds, and the note frames the comparison as a fault case only.
- [Minor] finding-2 CK-ANA-D2, E4: F2 row and expectation do not match the run (driver on from t = 0).
- [Minor] finding-3 CK-ANA-B3: 2N7002 fit is 4.86 ohm at 4.5 V, not 5.3 ohm.
- [Minor] finding-4 CK-ANA-A4: LM393 values mix the LM393B and legacy tables; the legacy full range is 0 to 70 C.
- [Minor] finding-5 CK-ANA-A3, C1, F1: research tag, tool versions and frequency coverage not stated.
ITEMS N/A: CK-ANA-G2 to G5, CK-ANA-E6, CK-ANA-G6-1
VALUES PROPOSED: REQ-TX-014: 1 uW (-30 dBm), TBR kept (supported: +28.3 dB on the estimates, +4.0 dB at the drive and passive bounds)
MEASUREMENTS: size=101 simulated cases + 15 static checks; inputs_checked=16; renders=7; turns=55; minutes=75; major=1; minor=5
```


## Iteration 2 (delta, rule C1): revision 1 at `c397ab1`

**Product.** `docs/design/analysis/pa-permit-gate-d18.md` revision 1 (blob `a6bcc2b1`) with `hardware/sim/tx-pa-permit/d18_run.py` (blob `5a06cfd8`), the generated decks `d18_keyup.cir` (`bce02858`) and `d18_seq.cir` (`de50be4d`), the block README (`f085dc40`) and the runs `2026-09-29-d18r1-keyup`, `2026-09-29-d18r1-seq` and `2026-09-29-d18r1-summary`, all at `c397ab1` on `main` (not pushed). The as-drawn run `2026-09-29-d18-asis` and its deck are reused unchanged from revision 0. Every blob equals `git rev-parse c397ab1:<path>`; the note and the checker also equal `HEAD:<path>` at `c8b7bd2` and `git hash-object` of the working tree. The `d18r1-keyup` `.raw` (11,633,088 bytes) is kept outside git; its SHA-256 `04fb27d3...96ff5` equals the committed `raw.sha256` (CR-017 C2). `tools/check_commit_msg.py --range c397ab1~1..c397ab1` gives PASS.

**Scope of this iteration.** Rule C1: a delta that verifies the Major fixes only. It verifies reviewer finding-1 of iteration 1 (Major; CK-ANA-E3, F1, A1: REQ-SYS-120 reported met without its -57 dBm level). For the SA pair's finding-1 (the REQ-SYS-180, 181 and 092 cutoffs clamp only VGG), the finding itself is verified in the SA record. This record checks the analysis the fix added: the design change, its decks, cases, static checks, arithmetic and plots. It looks for any new Major that revision 1 brings in. Minor findings of iteration 1 stay as liens in iteration 1's table; they are not re-reviewed here.

**Checklist.** The `peer-review-checklist-analysis.md` revision A item set (CR-012 branch, blob `0386cc6e`) applied to the revision 1 hunks (`git diff 078f2f7 c397ab1`: note +161/-45, checker +245/-15, decks +48/-14, README +5). `analysis_kind` simulation-deck, worst-case (static datasheet rows) and budget (isolation chains, cost row). Sections A to F, G1, G2, G7, H and I apply. G3 to G6 are N/A. J is answered by the SA pair.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first ("WP-PDR-22 PA permit gate D-18 review record checklist"). `git grep`, `grep -n` and read-only Python over the committed JSON were used afterwards, only to pin lines and read values.

### Readiness (iteration 2)

| # | Result |
|---|---|
| R1 | Pass. Every `product_files` blob equals `git rev-parse c397ab1:<path>`. No product file has changed since (`git diff --stat c397ab1 HEAD` on the note and on `hardware/sim/tx-pa-permit` is empty). |
| R2 | Pass. See CK-ANA-C4 below: `d18_run.py seq`, `keyup` and `summary` re-run from a `git archive c397ab1` export, and `replot keyup` and `replot seq` on a second export. |
| R3 | N/A. No JSON file under a schema is in the product. |
| R4 | Pass. The author's return and note section 11 list each change against the finding it resolves. The Evidence status row marks the checker as developer evidence. |
| R5 | Pass. No `TBD` string (0 hits). The TBRs relied on are named: REQ-TX-014 (1 uW, TBR) and REQ-SYS-183 (-57 dBm, TBR, `close_by` PDR). |
| R6 | Pass. All 9 cited renders exist beside their runs. |

### Verification of the iteration 1 Major finding

**finding-1 (reviewer, Major): Verified at `a6bcc2b1`.** Each part the finding named, checked against the note at its new blob:
- **The level is now stated and compared (CK-ANA-E3).** The note adds a criteria-table row (section 1, line 73), turns the section 5.4 column into a requirement comparison (lines 328 to 337), and adds section 5.8 (lines 407 to 432). Section 5.8 gives the level against -57 dBm in five rows: lead-in, one line only, key-up and hang time, end of the over, and after each hardware cutoff with CLK1 running. Each row has four isolation cases. The 1.3 dB margin on the estimates is stated to be inside the uncertainty of two estimated isolations, and the case is not reported as passing ("not shown", line 424). The bounds are stated as 18.2 and 23.0 dB over. The consequence is named: F-6 (line 486) goes to the owner as requirement owner, to CR-018, to WP-PDR-16b and to WP-PDR-23. That is what CK-ANA-E3 requires.
- **No residual "met" claim (CK-ANA-A1).** A search of the note for "met", "not affected" and "REQ-SYS-120 is" finds only the corrected wording (Summary line 33; sections 5.3 line 314, 5.8 line 424, 6.2 line 454). The Serves row (line 14) now reads "the state, and the level REQ-SYS-183 sets, section 5.8".
- **Every state the requirement implies (CK-ANA-F1).** REQ-SYS-120 (`docs/requirements/sys/requirements.json`) reads: RF only while both a key-down and a separately maintained PA permit are asserted, and "RF off is the REQ-SYS-183 level". REQ-SYS-183 applies "in every state with RF ended, inhibited or off". With TS-012 section 7.3 revision 6 (CLK1 on from t0 + 1 ms to the end of the hang time), the states with fewer than both conditions while CLK1 runs are the five rows of section 5.8. None is missing. The two states the rows leave out are both stated: CLK1 off (-111 dBm, keying note) and relay in receive with CLK1 on (WP-PDR-23b; limitation 11).
- **F-3 corrected.** F-3 (line 483) now applies the -57 dBm comparison to normal operation and asks that TS-012's "about -61 dBm (A5), under -57 dBm" be withdrawn as a REQ-SYS-120 or REQ-SYS-183 claim (TS-012 lines 489 and 492 hold that claim, checked).
- **The conflict is routed, not resolved by the analyst (CK-ANA-A6).** The REQ-TX-014 rationale says it is "the transmitter half of the two conditions of REQ-SYS-120". Its limit is 1 uW in the same state where REQ-SYS-183 asks for -57 dBm. Section 5.8 gives options (i) to (iii) and picks none. Sections 6.1 and 6.2 carry the conflict into the CR-018 and K8 text. That respects the section 5.3 writer order.
- **Reproduced (CK-ANA-C4, B5).** The section 5.8 table equals `result.json` key `req_sys_183_off_states`, byte-identical on the reviewer's replot. The hand chain gives the same values: L1 -5.27 - 19.6 - 3.0 - 30 - 0.5 = -58.37 dBm (+1.37 dB); L2 -38.77 dBm (-18.23 dB); L3 -88.37 dBm; L4 -0.49 - 3.0 - 30 - 0.5 = -33.99 dBm (-23.01 dB). Option (ii)'s isolation needs also recompute: 57 - 5.27 - 3.5 = 48.23 dB at the design drive and 57 - 0.49 - 3.5 = 53.01 dB at the drive bound, against 19.6 + 30 = 49.6 dB.

### Check of the analysis added for the SA finding-1 fix (design D18-2B revision 1)

No Major. The fix puts the backstop, the 95 C trip, the cell 60 C trip and the VBUS inhibit onto the Q node, and adds D1 (1N5711W) from VGG to Q.
- **Inputs against sources (CK-ANA-A3, A4).**
  - The 1N5711W values were read from Diodes DS11015 Rev. 15-2, fetched by this reviewer. Its SHA-256 `e9d83888...f19bc` equals the note's. VF max is 0.41 V at 1.0 mA and 1.00 V at 15 mA; IR max 200 nA at 50 V; V(BR)R 70 V min; CT 2.0 pF max; IFM 15 mA. Every value in the note's section 4 row equals the datasheet.
  - The fit Is 1.07 nA, N 1.05, Rs 36.9 ohm goes back through both points: 0.410 V at 1 mA and 1.000 V at 15 mA.
  - TS-012 revision 8 row 14 has 8 parts: detector 1, RX clamps 2, ring 4, spare 1. D-9 names that spare (line 1045). So the cost range of +0 to 0.31 for D1 is stated correctly, and the row stands.
  - The requirement texts of REQ-SYS-055, 180, 181, 092, 120 and 183 and REQ-TX-014 match the note's quotes.
  - TS-012 section 7.3 line 489 ("The existing wired-OR clamps ... stay on the same node") and the section 8.1 diagram lines 595 to 597 are quoted correctly.
- **Independent checks (CK-ANA-B5).**
  - Q high, every cutoff off: 4.75 - 10 k x (4 x 20 nA + 10 uA + 1 uA + 12.8 uA) = 4.511 V (note 4.51 V).
  - VGG through D1 with U1 stuck high, amplifier at 5.25 V. Iterating (5.25 - V)/2.7 k - V/5.1 k through the fit gives I_D1 = 1.30 mA, VF = 0.428 V and VGG = 1.128 V (note 1.13 V; simulation F6 1.123 V).
  - LM393 sink current: 0.525 + 1.30 = 1.83 mA, within the 4 mA VOL test point.
  - A1 level with the driver powered: -5.27 + 24.1 - 3 - 30 - 0.5 = -14.67 dBm (L1), -9.89 dBm (L4), -44.67 dBm (L3). That is 42.3 and 47.1 dB over -57 dBm, as the note states.
  - Cost: 0.63 to 0.91 plus 0 to 0.31 gives 0.63 to 1.22. At revision 0's contingency ratio (1.154) that is 1.41, so A5 is at 300.55 to 301.24 against 299.83. Note section 6.3 agrees.
- **Cases (CK-ANA-F1, F2).** C1 (backstop, standing for the 95 C and cell trips on the same LM393 output), C2 and C3 (VBUS inhibit held from power-up, and arriving during an over), C4 (D1 open) and A1 (TS-012 wiring as drawn) cover each cutoff and D1 open. F6 and F7 (U1 stuck high) cover the common element. D1 short, and a base pull-down open, are analysed by inspection (section 5.7). With U1 stuck high, section 5.7 and R-1 now state the true consequence: -9.9 to -14.7 dBm, not RF off. That replaces "still ends RF".
- **Model and deck (CK-ANA-B1, G1-2, G1-3).** Each LM393 cutoff is modelled at its 0.7 V VOL maximum, and D1 with a maximum-VF fit. Both are the worst case for Q low and for VGG through D1. The key-up deck carries D1 and all cutoff switches off. Against revision 0, the largest change over the 52 corners is 0.20 mV of bus dip, 0.049 A of turn-on peak current and 3.3 us of turn-off time (`summary.json` `keyup_max_abs_delta_vs_rev0`). The key-up levels do not change (delta 0.0). Limitation 10 explains the ringing of the D1 current trace, and no criterion uses it.

### Reviewer re-run (CK-ANA-C4, R2)

The commands ran from `git archive c397ab1` exports under the reviewer's scratchpad. They used the repository venv and LTspice only through `tools/ltspice-batch.sh`:
- **Replot on the committed and kept `.raw` files, no LTspice.** `d18_run.py replot keyup` (the kept `.raw`, SHA-256 checked first) exited 0 with "52 cases; criteria failing: none" and "REQ-SYS-183 verdicts as the record states: True". `d18_run.py replot seq` exited 0 with "20 cases; not as required: none". The regenerated `result.json` and `result.csv` of both runs are byte-identical to the committed blobs (`cmp`).
- **Full LTspice re-run:** `d18_run.py seq`, `keyup` and `summary`, with `CWHT_LTSPICE_LOCK_WAIT=5400` because another agent's run held the wrapper lock. Each exited 0:
  - "2026-09-29-d18r1-seq: 20 cases; not as required: none";
  - "2026-09-29-d18r1-keyup: 52 cases; criteria failing: none" and "REQ-SYS-183 verdicts as the record states: True";
  - "2026-09-29-d18r1-summary: every criterion as required".

  Both wrapper lines read `result: PASS`, `version_line='LTspice 26.0.2 for MacOS'`, and give deck SHA-256s (`2a6b4d39...`, `047bd05d...`) equal to the committed `wrapper.txt`. The generated decks, both `result.json`, both `result.csv` and `summary.json` are byte-identical to the committed blobs. Only the `.raw` files differ. The new `d18_seq.raw` differs from the committed one in 10 bytes (`cmp -l`), all in the header's temporary-folder name and `Date:` line. The new `d18_keyup.raw` has SHA-256 `b6369a1e...` against the kept `04fb27d3...`. The `result.json` computed from it is identical, so its analysed content is the same.

### Findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-21"></a>finding-21 | reviewer | Minor | CK-ANA-A6, B1 | note section 2 lines 126 to 127, section 6.1 line 444; TS-012 section 7.3 line 512 | TS-012 draws the hardware cutoffs as pulls "on the envelope reference and VGG node". Revision 1 moves them to the Q node, so none of them pulls the envelope reference any more (section 6.1 keeps only the firmware reference clamp there). The note does not say so, and it does not analyse what happens when a cutoff releases while TX_KEY and PA_EN are still high. Two cases: the 95 C trip releasing through its hysteresis, and the VBUS inhibit ending when USB is unplugged during an element. The error amplifier is then wound up against an unclamped reference, so the driver is re-powered and VGG steps to the divider limit, at most 3.46 V, with no ramp. That is the open-loop case TS-012 already bounds (8 W stability, REQ-SYS-156 within 100 ms, the 10 s cutoff), so no hazard level changes. But the loss of the reference pull, and the release step, are consequences of the fix and should be stated and sent to the WP-PDR-22 loop rerun (release of each cutoff while keyed) | Deferred | Pending | lien: due at the CDR readiness declaration (rule C1) |
| <a id="finding-22"></a>finding-22 | reviewer | Minor | CK-ANA-A5, A6 | note F-4 line 484, F-7 line 487; REQ-SYS-055 rationale | The shared Q node works only if every output on it is open-collector or open-drain. The note states this for the VBUS inhibit (F-7) but not for the monostable. The monostable is an LM393 open collector in TS-012 revision 8 (row 27; section 8.1), and the note models it that way. But the REQ-SYS-055 rationale names "the 74LVC1G123 and a capacitor", whose output is push-pull. On a shared node, any other cutoff would then fight it. F-4 to WP-PDR-26 should add the output-type condition, and name the part mismatch between REQ-SYS-055's rationale and TS-012 for the requirement writer | Deferred | Pending | lien: due at the CDR readiness declaration (rule C1) |
| <a id="finding-23"></a>finding-23 | reviewer | Minor | CK-ANA-D2 | `hardware/sim/tx-pa-permit/README.md` file table row `d18_seq.cir`; `d18_run.py` docstring stage `seq` (line 42) | Both still say the sequencing deck has "13 cases". Revision 1 has 20 (note section 3.1; README runs table; `result.json`). Also, `result.json` `req_sys_183_off_states` labels the L1 and L3 rows "PASS", while the note calls the L1 row "not shown" (inside the isolation uncertainty). The label is the checker's expected-state flag, but a reader of the JSON alone would take it as the requirement being met. It could read, for example, "PASS (estimate, margin inside uncertainty)". No number or conclusion changes | Deferred | Pending | lien: due at the CDR readiness declaration (rule C1) |
| <a id="finding-24"></a>finding-24 | reviewer | Minor | CK-ANA-H2 | note section 5.8 line 424, F-6 line 486 | Section 5.8 finds REQ-SYS-183 not shown in five normal transmit-side states: 1.3 dB on the estimates, 18.2 to 23.0 dB over at the bounds. F-6 routes the requirement conflict. But neither F-6 nor any other routing sends the risk (the REQ-SYS-183 and TC-SYS-039, 066, 083, 108 and 109 closing cases may fail on the bench with CLK1 running) to the risk register writer (WP-PDR-18) as a new entry or a link to an existing RSK. Add it as an entry request | Deferred | Pending | lien: due at the CDR readiness declaration (rule C1) |
| <a id="finding-25"></a>finding-25 | reviewer | Minor | CK-ANA-I2 | `results/2026-09-29-d18r1-seq/seq_cases.png` | The 20-panel figure's title overlaps the panel titles of the first row (S1, S2, S3). No panel has a y-axis label or unit (the volts show only in the legend of panel S1). The green U1 trace is scaled (x0.5, -1.2) and that is stated only in that legend. The values agree with `result.json` at the points checked (A1 VGG 0.70 V, F6 1.12 V, F7 0.64 V; driver 4.97 V). Presentation only | Deferred | Pending | lien: due at the CDR readiness declaration (rule C1) |

### Per-case results (revision 1 cases; section F)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| K-1 | Key-up: TX_KEY low, PA_EN high, CLK1 running, 52 corners | REQ-TX-014: at most -30 dBm | L1 -58.3, L2 -38.8, L3 -88.3, L4 -34.0 dBm | +28.3 / +8.8 / +58.3 / +4.0 dB | isolations are estimates (L2 and L4 bound the GVA-84+ by passivity) | replot byte-identical; hand chain equal | none |
| O-1 | Lead-in, CLK1 on, neither line asserted | REQ-SYS-120 through REQ-SYS-183: at most -57 dBm | L1 -58.3, L2 -38.8, L3 -88.3, L4 -34.0 dBm | +1.3 / -18.2 / +31.3 / -23.0 dB; reported "not shown" | 1.3 dB is inside the two estimated isolations | replot identical; hand chain | finding-24 |
| O-2 | One line only (PA_EN 7 to 8 ms; TX_KEY 8 to 11 ms, fallback) | REQ-SYS-183: -57 dBm | as O-1 | as O-1 | as O-1 | replot identical | finding-24 |
| O-3 | Key-up and hang time | REQ-SYS-183: -57 dBm | as O-1 | as O-1 | as O-1 | replot identical | finding-24 |
| O-4 | End of the over: PA_EN cleared, CLK1 on | REQ-SYS-183: -57 dBm | as O-1 | as O-1 | as O-1 | replot identical | finding-24 |
| C-1 | Backstop (and the 95 C and cell trips) on Q at 20 ms, lines high | REQ-SYS-180, 181: RF off to the REQ-SYS-183 level | Q 0.70 V; driver off in under 1 ms; VGG 7.8 mV; level as O-1 | as O-1 | LM393 at VOL max | replot identical | finding-21 |
| C-2 | VBUS inhibit held from power-up, fault build drives both lines | REQ-SYS-092 | driver off throughout; VGG at most 0.40 V during the bus ramp | under the 2.0 V dead-zone criterion by 1.6 V | open-drain part assumed (E) | replot identical | finding-22 |
| C-3 | VBUS inhibit arrives at 20 ms during an over | REQ-SYS-092 | as C-1 | as O-1 | as C-2 | replot identical | finding-21 |
| C-4 | D1 open plus the backstop | single fault, latent | driver off; VGG clamped by U1 | as expected | - | replot identical | none |
| A-1 | TS-012 wiring as drawn (cutoff on VGG) | comparison | driver 4.97 V; VGG 0.70 V; -14.7 (L1), -9.9 (L4), -44.7 dBm (L3) | 42.3 / 47.1 / 12.3 dB over -57 dBm | as O-1 | hand chain -14.67 dBm | none |
| F6 | U1 stuck high plus the backstop | common element | driver on; VGG 1.12 V through D1; level as A-1 | not RF off (stated) | D1 at max VF | hand 1.128 V | none |
| F7 | U1 stuck high, monostable expires | common element | driver on; VGG 0.64 V; level as A-1 | not RF off (stated) | - | replot identical | none |
| S-D1 | Static: Q high with all cutoffs off (hot leakage) | U1 VIH 2.0 V | 4.51 V | +2.51 V | hot leakage x64 (E) | hand 4.511 V | none |
| S-D2 | Static: Q low, one LM393 cutoff on | U1 VIL 0.8 V | 0.70 V | +0.10 V | datasheet maximum | datasheet (as iteration 1) | none |
| S-D3 | Static: VGG via D1, U1 stuck high | 2.0 V (dead zone to about 2.3 V) | 1.13 V | +0.87 V | VF fit at 25 C; colder VF is higher by tens of mV | hand 1.128 V | none |

### Checklist items (revision 1 hunks)

- **A.**
  - A1 Yes: every id exists; REQ-SYS-183 and REQ-SYS-055, 180, 181 and 092 are added to the Serves row.
  - A2 Yes: TS-012 revision 8 `bb5dee7`.
  - A3 and A4 Yes: 1N5711W, cutoff sinks and requirement texts checked in full, above.
  - A5 Yes, with finding-22.
  - A6 No: finding-21, finding-22.
- **B.**
  - B1 Yes, with finding-21.
  - B2 Yes: the D1 fit is stated with its basis.
  - B3 Yes: the fit is checked against both datasheet points.
  - B4 Yes: unchanged from revision 0; the key-up delta against revision 0 is at most 0.2 mV.
  - B5 Yes: the hand checks above.
  - B6 Yes: the section 5.8 verdict states the uncertainty.
- **C.**
  - C1 Yes: LTspice 26.0.2 in both logs.
  - C2 Yes: developer evidence is stated.
  - C3 and C4 Yes.
  - C5 Yes: every run went through the wrapper.
- **D.**
  - D1 Yes.
  - D2 No: finding-23.
  - D3 Yes. The rounded L1 margin (+1.3 dB) is toward the limit. The L4 REQ-TX-014 margin, 4.0 dB against 4.01 dB exact, has no effect.
  - D4 Yes: `REQ_SYS_183_DBM = -57.0` and `REQ_TX_014_DBM = -30.0` are named with their ids.
- **E.**
  - E1 Yes: -57 dBm is quoted from REQ-SYS-183, and "RF off is the REQ-SYS-183 level" from REQ-SYS-120.
  - E2 Yes.
  - E3 Yes: finding-1 Verified.
  - E4 Yes, stated: the REQ-SYS-183 rows are expected states, not design criteria, and the note does not claim them met.
  - E5 Yes: REQ-TX-014 kept at 1 uW with the conflict stated.
  - E6 N/A.
  - E7 Yes: Test-method requirements; supporting evidence only.
- **F.** F1 to F3 Yes. F4 Yes: section 5.8 names the two isolations that set the margin, and option (ii) gives the sensitivity.
- **G1.** G1-1 to G1-4 Yes. G2-1 and G2-2 Yes (the cost row). G7-1 and G7-2 Yes (extreme-value datasheet maxima; hot leakage x64 stated as E).
- **H.**
  - H1 Yes: K8 wording to WP-PDR-16b, not edited.
  - H2 No: finding-24.
  - H3 Yes: section 11 names revision 1 and this delta iteration.
- **I.** I1 Yes: 9 of 9 renders opened with the Read tool. I2 No: finding-25.

ITEMS N/A: CK-ANA-G2-3, G2-4 (no allocation or TPM line), G3 to G6, J1 to J3 (answered by the SA pair record).

### Verdict (iteration 2)

```
VERDICT: APPROVED
PRODUCT: docs/design/analysis/pa-permit-gate-d18.md@a6bcc2b14710730d6c5bee3a61a4cbcfda919e19, hardware/sim/tx-pa-permit/d18_run.py@5a06cfd879f2f885a42f41fcb7667be42abaa48e, hardware/sim/tx-pa-permit/d18_keyup.cir@bce02858a570d9f7decc4d9910fe73caaee0ecea, hardware/sim/tx-pa-permit/d18_seq.cir@de50be4d518f8a117e7b1ce627d72e7f91e695c5 at c397ab171b4c564c402f806bd617a796e74a96d1
FINDINGS:
- [Major] finding-1 (iteration 1): Verified at a6bcc2b1 (section 5.8, F-3, F-6; the level stated in every state with fewer than both conditions and not claimed met).
- [Minor] CK-ANA-A6 finding-21: the fix removes the hardware pull on the envelope reference; release of a cutoff while keyed not stated or analysed.
- [Minor] CK-ANA-A6 finding-22: the shared Q node needs every source open-collector; REQ-SYS-055 rationale names the push-pull 74LVC1G123.
- [Minor] CK-ANA-D2 finding-23: README and docstring say 13 sequencing cases (20); result.json labels the L1 REQ-SYS-183 row PASS.
- [Minor] CK-ANA-H2 finding-24: the REQ-SYS-183 shortfall is not sent to the risk register writer.
- [Minor] CK-ANA-I2 finding-25: seq_cases.png title overlap, no y-axis units.
ITEMS N/A: CK-ANA-G2-3, G2-4, G3 to G6, J1 to J3 (SA pair)
VALUES PROPOSED: REQ-TX-014: 1 uW, TBR kept (supported for REQ-TX-014 alone; the conflict with REQ-SYS-183 goes to the requirement owner with it, F-6)
MEASUREMENTS: size=108 simulated cases (52 + 36 + 20), 21 static checks; inputs_checked=12 (revision 1 rows); renders=9; turns=60; minutes=75; major=0 new (1 verified); minor=5 new
```

### Cross items (iteration 2)

- **X-1 (lead SE).** File iteration 1's text first (see the filing note in the front matter). This record's id and new finding numbers depend on it.
- **X-2 (SA pair).** SA finding-1 is verified in the SA record. This record found no Major in the analysis of the fix, but found finding-21 and finding-22, which the SA pair should weigh under SWE-134 (cutoff release while keyed; output type on the shared node).
- **X-3 (INSP-118 X-12 and INSP-110 finding-24).** Both close only when this record and its SA pair are APPROVED and a TS-012 or ADR-056 revision adopts D18-2B revision 1 (F-1, F-7). The move of the cutoffs to the Q node changes the TS-012 section 7.3 and 8.1 text that ADR-056 cites.
- **X-4 (owner, CR-018, WP-PDR-16b, WP-PDR-23).** F-6 is an open requirement conflict for the owner as requirement owner. The REQ-TX-014 value this note proposes (1 uW, TBR kept) should not go to the owner at S2 or B2 without F-6 beside it (rule C10).

