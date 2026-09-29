---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-22 pre-order keying
# envelope and key-click analysis of the TS-012 finalists A4 and A5, iteration 1 at freeze commit 4ea4607 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e). tools/validate_docs.py requires the checklist field to
# name a template that exists on main, so the field names peer-review-checklist-design revision B and
# checklist_analysis records the template actually applied, as INSP-056, INSP-083 and INSP-114 did.
# id: the brief assigned no id. INSP-116 is above every id on main (HEAD 35fc7ee), on every cr/ branch and in the
# working tree at the time of filing (INSP-114 is the highest in use). If a parallel reviewer filed INSP-116 first, the
# lead SE renumbers this record.
# Filed by the lead SE on 2026-09-28 from the reviewer's own text (its later, scratch-copy Write, which differs from
# the first only in HEAD citations and effort counts): the harness refused the reviewer's Write of this new file
# ("Subagents should return findings as text"). Content is verbatim except the id, reassigned from INSP-115 to
# INSP-116 because review:lpf-1 also took INSP-115.
id: INSP-116
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-keying-ts012.md
product: docs/design/analysis/keying-ts012.md
# product_commit: 4ea4607, the WP-PDR-22 tx-keying commit. Every blob below equals git rev-parse 4ea4607:<path> and
# HEAD:<path> at HEAD 35fc7ee (no product file changed after the freeze).
product_commit: "4ea460733a52881a0536838d3b3f68e3337ad649"
product_files: ["docs/design/analysis/keying-ts012.md@bad537544e50cad797be11fb5009eb8e7ea448c3", "hardware/sim/tx-keying/README.md@031c25f9f44b7f11bf2db05c161a3c1402b9357e", "hardware/sim/tx-keying/det_char.cir@059595d7034f385a08dc8a84654d01c8692f9485", "hardware/sim/tx-keying/det_char_biased.cir@5911e4396425b17bf4b48c4146e3b0b898b1c2c4", "hardware/sim/tx-keying/keying_a4_asis.cir@2c4f1d86aa0b3895fdbbe3a60a3126c652b0ee6a", "hardware/sim/tx-keying/keying_a4_mitig.cir@d209bbd419e0b106375b7a2856ef64c8af2702a2", "hardware/sim/tx-keying/keying_a5_asis.cir@aebb89253184c785598442ac80533241db037bac", "hardware/sim/tx-keying/keying_a5_mitig.cir@fd4ec933178342d196e2c5943736094e54dc77a2", "hardware/sim/tx-keying/keying_run.py@f85f2e2965d18288cce8cd55b7b60aa6fd1f774f", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/envelope.png@66a0c0de303bf92b781080b8df4ef3b1b89ad55b", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/keyup_level.png@0fe31b1ef50030051232237295421c307e926b7d", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/result.json@abbfca5dde2e19f6c109b5ec25a1752fa944a6f2", "hardware/sim/tx-keying/results/2026-09-28-a4-asis/spectrum.png@89eb1791e90b4c3c5cb245569138362d10e66ac3", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/corners.png@15cadaf455c525a84599bbb54789fe258c564fa6", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/envelope.png@0010dc46e65aacdae1713c7d38777d7c6297166d", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/keyup_level.png@57a805ded1f9f768bd6bf6247b6c1400620795c3", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/result.json@c7ea5dc5fcfa69266f51c1e1aca72b0b2a88e382", "hardware/sim/tx-keying/results/2026-09-28-a4-mitig/spectrum.png@ca11b04a0497f1526f67e3864ca4e9686fe051ed", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/envelope.png@b387cf0ad695fbfbc59c2fa4e6a598f1fc8bfd0c", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/keyup_level.png@06525e4f2d1ccf6af06cfe260c38efc433821188", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/result.json@3e473721292dfce47c5ba21352cc85f1c5b6cd1e", "hardware/sim/tx-keying/results/2026-09-28-a5-asis/spectrum.png@f1d37da0de814cc307b5cd7e23b9a383d602f9e2", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/corners.png@ef095896f28b454e7dda755a51e014d378970320", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/envelope.png@3af80d18b2a8ab8168c36f867de8494eb8de52be", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/keyup_level.png@255cd4d1eef0786603d502c069be2da2938f209f", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/result.json@2792dd1a30da7c34ed3af37cabc765fa0e6a958b", "hardware/sim/tx-keying/results/2026-09-28-a5-mitig/spectrum.png@92e69e6dab86396c566181c6e7a3768c6b50dd49", "hardware/sim/tx-keying/results/2026-09-28-det-char-biased/det_law.png@be1c380b6b5c3a42a4254a18a0bbcd4b0d23c071", "hardware/sim/tx-keying/results/2026-09-28-det-char-biased/result.json@584d5e6dace081012c3b8997a3ce0be88c01f985", "hardware/sim/tx-keying/results/2026-09-28-det-char/det_law.png@582e4e076e638cfd78cdc438de6223157432e53e", "hardware/sim/tx-keying/results/2026-09-28-det-char/result.json@17c4d924c8e04b0541e49493ea84ac9b62b4a0a9", "hardware/sim/tx-keying/results/2026-09-28-summary/pwm_ripple.png@2e28ecce6f1a0872f8e2d2dfc6ed3c3917a57323", "hardware/sim/tx-keying/results/2026-09-28-summary/summary.json@6fc2fe2ee6969365c3f12e30dcaa68c07df5e63f", "hardware/sim/tx-keying/results/2026-09-28-summary/summary.png@069cb9295c9aef4d952f4a2fd0be8b60c839f6a8"]
analysis_kind: [simulation-deck, timing, worst-case]
product_size: 1 note; 2 detector decks (13 amplitudes each at 146 MHz); 4 envelope decks (6 + 6 + 30 + 30 runs); 1 generator and checker; 18 renders (16 cited); 22 input rows
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/tx-keying/keying_run.py: developer evidence per 05 section 9.1, as the note says"]
# values_proposed: the note proposes no TBR value and no TPM current best estimate; its section 5.2 design changes and
# section 8 item 4 (REQ-TX-014 disposition) go to the owner through TS-012 and the PDR memo, not as values.
values_proposed: []
renders_inspected: 18
sprint: PDR-prep
author_agent: "author:WP-PDR-22 tx-keying (Claude as analysis author, TS-012 discriminating analyses; commit 4ea4607)"
reviewer_agent: "reviewer:WP-PDR-22-analysis-keying-iter1 (independent; authored no part of the note, decks, checker or TS-012)"
# criticality: a hardware transmit analysis; the firmware ramp and feedforward tables it proposes are SW design items
# not yet allocated, and it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
# verdict (rule C1, iteration 1): three Major findings are open, so NEEDS CHANGES. Iteration 2 is a delta that verifies
# the Major fixes only; Minor findings raised after the first APPROVED verdict become liens due at the CDR readiness
# declaration.
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 6
findings_open: 9
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A1, CK-ANA-A4, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B6, CK-ANA-C1, CK-ANA-D4, CK-ANA-E3, CK-ANA-E4, CK-ANA-F1, CK-ANA-F2, CK-ANA-F4, CK-ANA-G7-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-H3]
effort_turns: 80
effort_minutes: 130
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record: keying envelope and key clicks, TS-012 finalists A4 and A5 (INSP-116, iteration 1)

**Product:** `docs/design/analysis/keying-ts012.md` (`bad53754`) with `hardware/sim/tx-keying/` (README `031c25f9`; generator and checker `keying_run.py` `f85f2e29`; decks `det_char.cir`, `det_char_biased.cir` and the four keying decks; seven result runs) at freeze commit `4ea4607` (rule C2). Every blob equals `git rev-parse HEAD:<path>` at `HEAD` `35fc7ee`. No product blob lives on a `cr/` branch.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck, timing (keying envelope edges, which G6 names) and worst-case (extreme-value corners): sections A to F, G1, G6, G7, H and I apply. G2 to G5 are N/A; J is N/A (criticality neither).

**Acceptance criteria (rule C7; texts read at HEAD from `requirements.json` and `test_cases.json`):**
- REQ-SYS-014: "shape keyed rises and falls as raised cosines with an operator-set 10-to-90 percent time of 3 to 8 ms (TBR)". TC-SYS-013: normalized envelope within 5 % of full scale of the ideal raised cosine at every sample, and 10-to-90 % times equal to the setting within +/-0.5 ms, at 3, 5 and 8 ms, "nominal and at every tolerance corner".
- REQ-SYS-015: "26 dB bandwidth at most 350 Hz (TBR) at every envelope setting with continuous dits at 50 WPM" (97.3(a)(8) power containment).
- REQ-TX-005: "10-to-90 percent times within +/-10 percent (TBR) of the command". TC-TX-005 accepts 2.7 to 3.3 ms, 4.5 to 5.5 ms and 7.2 to 8.8 ms "at the 0.5 W and 5 W steps, at 6.4, 7.4 and 8.4 V supply and at every shaping-network tolerance corner".
- REQ-TX-006: "at least 60 dB below total mean power beyond 750 Hz (TBR) offset with continuous 50 WPM dits"; its verification note says "at the 3, 5 and 8 ms settings and every tolerance corner". TC-TX-006 step 2 is a known answer (614 Hz within one cell) and step 6 reads "Repeat the three settings at the 0.5 W step and at every shaping-network tolerance corner".
- REQ-TX-014: at most 1 uW (TBR) "while TX_KEY is deasserted with PA_EN asserted and the exciter driven". REQ-SYS-183: -57 dBm (TBR) in every RF-ended, inhibited or off state.
- REQ-SYS-011: "0.5, 1 and 2 W steps within +/-1 dB (TBR)"; REQ-SYS-064 makes 1 W the default step. REQ-SYS-114: requirements met from -10 C to +45 C (TBR).
- TS-012 revision 4 section 7.3, WP-PDR-22 pre-order criteria: overshoot at most 0.2 dB, loop phase margin at least 45 degrees, VGG never above 3.5 V with the LM2940 at 4.75 to 5.25 V, and the 12 ms late-contact and open-loop fault cases.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (the keying analysis; the INSP id register) preceded every `grep`; `grep` only pinned lines in TS-012, INSP-110, the research note F7, the note and the checker. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).**
- NXP AFT05MS004N Rev. 0 (https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf), fetched through the web-fetch tool; SHA-256 prefix `84cd9fae`, equal to the prefix in the `hardware/sim/tx-pa` README. Read: Table 5 (VGS(th) 1.7 / 2.2 / 2.5 V at VDS 10 V, ID 67 uA; Crss 1.63 pF; Ciss 57.6 pF), and Figure 12 on page 11, rendered at 200 dpi.
- Mitsubishi RA07M1317M (Jun. 2019), through the digitized curves `hardware/sim/tx-pa/data/ra07_pout_vs_vgg_{135,155}.csv` and `ra07_pout_vs_vdd_{135,155}.csv` (reviewed under INSP-114 with their overlays).
- `docs/research/regulatory-corpus-and-operators.md` F7.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-F1, E3, A5 | note sections 1, 2 (runs per deck), 4.3 and 5.1; author summary ("both pass every keying check at every corner I tried"); `keying_run.py` `run_params` (`pset = 5.0`) | **The power steps below 5 W are not analysed, and the note does not say so.** REQ-SYS-011 sets 0.5, 1 and 2 W steps, and 1 W is the default (REQ-SYS-064). The keying requirements hold at every step. TC-TX-005 and TC-TX-006 name the 0.5 W step, and TC-TX-005 also names 7.4 V. This case exercises the mechanism the note itself identifies. The biased detector sees down to -35.5 dB re 5 W, which is only -25.5 dB re 0.5 W, so the feedforward alone shapes a 10 dB larger part of each edge. **Reviewer run** (the note's own mitigated model and five corners, setpoint 0.5 W, both drain ends, 30 runs per finalist, through the wrapper): nominal and the +/-1 mV corners pass for both finalists. At the -0.1 V corner: A5 has shape error 6.3 % and rise 3.40 ms at 3 ms (REQ-TX-005 +13 %), rise 5.68 ms at 5 ms and 9.02 ms at 8 ms (TC-SYS-013 +/-0.5 ms fails). A4 has rise 3.38 ms at 3 ms (+13 %) and 5.54 ms at 5 ms (TC-SYS-013 and REQ-TX-005 fail), with shape at most 4.4 %. At the +0.1 V corner: A5 has rise 2.57 ms at 3 ms (-14 %) and shape 5.5 %. So at the note's own corner set both finalists fail REQ-TX-005 at the 0.5 W step, and A5 also fails REQ-SYS-014. **Fix:** add the 0.5, 1 and 2 W steps (and 7.4 V) to the decks and the per-case results. If they fail, the mitigation needs a step-dependent change (for example a detector tap or gain switched with the step, or a tighter calibration), and the verdicts of sections 4.3 and 5.1 and the summary are restated | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A4, A5, B6, E3, F4, G7-2 | note section 4.3 corners; section 3 rows "AFT05MS004N Crss, VGS(th)" and "Sub-threshold slope"; section 7 item 1; section 8 item 2 ("A5 only"); `keying_run.py` `CORNERS_MITIG` | **The PASS "at every corner" rests on a +/-0.1 V transfer-curve corner that has no source and is narrower than the known variation.** The variation comes from the note's own inputs and the project's other analyses, and the reviewer's wider corners show that both finalists' margins are about the corner's size. (i) Lot spread: the AFT05MS004N VGS(th) is 1.7 to 2.5 V (Table 5, the note's own input row), yet section 8 asks for per-unit feedforward calibration for A5 only. (ii) Drive level: Figure 12 shows the Pout-versus-VGS curve moving about +0.5 V when Pin halves from 0.1 to 0.05 W. `docs/design/analysis/pa-drive-ts012.md` gives A4 drive 50 to 168 mW and A5 6 to 29.5 mW over its corners, with a 0.34 dB span within one unit over 144 to 148 MHz. The RA07M1317M VGG curve is given at 20 mW only. (iii) Temperature: neither REQ-SYS-114 (-10 to +45 C) nor the module heating that TS-012 section 7.3 estimates (flange 70 to 99 C) is a corner. Section 7 item 1 lists "no thermal drift of the threshold" as a limitation, but the verdict does not carry it. An LDMOS threshold coefficient of the order of -2 mV/C (reviewer estimate, not read from either datasheet) moves the curve 0.1 to 0.2 V over those ranges. (iv) The A5 table sits up to about 0.05 V left of the project's digitized curves at 2.3 to 2.5 V (finding-4). **Reviewer runs** (the mitigated decks with wider threshold corners, 36 runs per finalist, through the wrapper): A5 at -0.15 V: rise 3.47 ms at 3 ms (REQ-TX-005 +16 %; the checker still reports t1090 PASS, finding-3) and shape 5.1 %. A5 at -0.2 V: rise 3.60 ms, shape 6.4 to 6.6 %. A5 at +0.2 V: shape 5.0 to 5.1 %. A5 at +/-0.4 V: setpoint not reached, worst cell -55.0 dB. A4 at -0.2 V: shape 5.2 % (3 ms, 6.1 V). A4 at -0.4 V: rise 3.50 ms, shape 6.6 %, worst cell -60.1 dB. A4 at +0.4 V: setpoint not reached, rise 2.67 ms (-11 %). So A5 holds for about +/-0.12 V of residual curve error and A4 for about +/-0.15 to 0.2 V. The note's A5 margin (3.285 ms against 3.3 ms) is 0.015 ms, against an uncertainty the note does not bound. **Fix:** bound the residual curve error after calibration (lot, drive over frequency and temperature, device temperature, table read) with sources or labelled estimates. State that A4 also needs per-unit calibration and what calibration covers. Add the temperature case, and report the margin against that bound. Or state the pass as conditional on a residual of at most about 0.1 V (A5) and 0.15 V (A4), and carry that as a design requirement and a risk | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-E4, D4, D2 | `keying_run.py` `REQ` (`t1090_tol_ms: 0.5`), `analyse()` `pass`, `stage_deck()`; note section 4.3 table row "10-to-90 % error" | **The checker does not assert REQ-TX-005.** Its only timing criterion is TC-SYS-013's +/-0.5 ms. That is looser than REQ-TX-005's +/-10 % at the 3 ms setting (2.7 to 3.3 ms) and tighter at 8 ms (7.2 to 8.8 ms). The note's "+9.7 % of 10 %" is a hand computation on the checker output. In the reviewer runs the checker reports t1090 PASS for A5 at 3.47 ms and for A4 at 3.38 ms and 2.67 ms, all outside REQ-TX-005. The checker also exits 0 whatever the verdicts (reviewer runs: exit 0 on every as-written FAIL). Its `setpoint` criterion (+/-0.5 dB) has no source, and it passes A5 as written at 4.48 W against 5 W (-0.48 dB) although the integrator has wound up. **Fix:** add a REQ-TX-005 criterion (+/-10 % of the setting, with its id in a comment) and keep TC-SYS-013's separately. Source or drop the setpoint criterion (REQ-SYS-012 is +/-1 dB of 5 W). Exit non-zero on a failing case, or add a `--check` mode with the expected FAIL states listed | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-A4, A3 | note section 3 rows "RA07M1317M Pout vs VGG", "Pout vs VDD", "AFT05MS004N Pout vs VGS" and "Sub-threshold slope"; section 6 F1; `keying_run.py` `A5_W`, `A5_SCALE`, `A4_W` | **The graph reads disagree with the project's digitized curves by more than the stated 0.05 W resolution at the foot.** A5 table against the mean of `ra07_pout_vs_vgg_135.csv` and `_155.csv`: 0.17 against 0.08 W at 2.3 V, 0.55 against 0.36 W at 2.4 V, and 1.25 against 1.02 W at 2.5 V (about 0.03 to 0.05 V of curve shift). F1's "1.1 to 1.3 W at 2.5 V" reads 0.98 to 1.06 W on the digitized curves. VDD scale at 155 MHz: 4.8 / 7.75 / 9.1 W at 5.5 / 7.2 / 7.9 V against 4.93 / 8.23 / 9.76 W digitized (ratio at 5.5 V 0.619 against 0.599). AFT05 Figure 12 (rendered): the Pin 0.1 W curve ends near 2.42 V and 5.7 W, not 2.35 V and 5.6 W. The 100 dB/V sub-threshold estimate is about three times steeper than the last graph segments (A5 about 33 dB/V at 2.2 to 2.3 V, A4 about 39 dB/V at 1.2 to 1.5 V), and its direction is not stated. **Fix:** take the digitized RA07M1317M curves (or state why not), state the read resolution, and state the direction of the slope estimate | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-C1 | note header "Tool" row | **Wrong tool version.** The note says "spicelib 2.5", but the venv has spicelib 1.6.3 (`pip show`); numpy is 2.5.3. **Fix:** correct the version and list numpy and matplotlib | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A1, H1, H2, H3 | note header "Serves" row, sections 5.1 and 8; no change history | **Missing ids, requests and change history.** (i) The hazards are not named: HZ-008 (REQ-SYS-014, 015, REQ-TX-005, 006) and HZ-004 (REQ-TX-014, REQ-SYS-183). REQ-SYS-011 and REQ-SYS-114 are not named (findings 1 and 2), nor is RSK-011 (Analysis accepted). (ii) Section 5.1 re-scores the TS-012 section 7.1 A5 envelope-loop risk ("a certainty" as written) and shows that A4 carries the same loop (INSP-110 finding-17 asked for the A4 counterpart row). No request goes to the WP-PDR-18 risk writer or to the `hazards.json` writer (PDR work plan section 5.3). (iii) The note has no change history. **Fix:** add the ids, the two requests and a change log | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-B3, A6 | note section 7 item 9; section 2 step 3 | **The explanation of the -60 dB point is not shown.** The note gives 395 Hz here against F7's 614 Hz and attributes the difference to "record length and window: a radix-2 record in F7, whose rectangular-window leakage raises the far cells". Reviewer computation on the ideal envelope: an integer number of periods gives 395 Hz (5.08 ms full transition) and 435 Hz (5.00 ms). A radix-2 rectangular record (2^15 samples at 10 kHz) gives 435 Hz for both, and a Blackman-Harris window gives 395 and 435 Hz. None reproduces 614 Hz. The metric also jumps with the position of the spectral nulls (395 against 435 Hz for a 1.6 % change of transition). TC-TX-006 step 2 requires the checker to place the point at 614 Hz within one cell, which this checker does not. The 26 dB bandwidth (292 Hz) agrees, and that is the check that matters here. **Fix:** state the cause as not established, and send a request to the TC-TX-006 and F7 owners (the 614 Hz known answer feeds the REQ-SYS-008 and REQ-TX-006 rationale) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-A6, F2 | note header "Work package" row, section 1 "It does not cover", author summary | **A partial WP-PDR-22 run is presented as the pre-order check.** The header calls the note "the pre-order LTspice check that TS-012 revision 4 section 7.3 names", but most WP-PDR-22 pass criteria of TS-012 section 7.3 are not run: the 12 ms late-contact fault case (at most 8 W, and the mid-ramp check tripping); the open-loop case at 8.4 V (at most 8 W at the clamp); VGG with the LM2940 at 4.75 to 5.25 V and the divider at +/-1 % (the decks use 5.00 V; 5.25 V gives 3.43 V as written); the module VGG input current; and the 3.08 V clamp REQ-SYS-012 check. Section 1 lists some of these exclusions and section 8 item 1 carries two, but a reader of the header and the summary takes the pre-order item as done. **Fix:** call it a partial WP-PDR-22 run in the header, and list every TS-012 criterion not run with where it closes | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-B1, D2 | `det_char.cir` hold capacitor; note sections 4.1, 4.3 and 4.5 | **Three statements need correcting.** (i) The detector law is characterized with a 22 pF hold (50 ohm at 146 MHz) instead of the design's 470 pF. The RF divides between the diode capacitance and the hold, so the square-law output is about 17 % low (reviewer analytic, below). The direction is conservative (with 470 pF the blind point moves about 0.3 to 0.6 dB lower) but is not stated. (ii) Section 4.5 says the 30.5 kHz feedforward ripple fails REQ-TX-006. The figure is a bound: it holds duty 0.5 at the steepest slope continuously, while the steep part of the transfer is crossed for only a few ms per 48 ms. "Not shown" is the supported wording. The 122 kHz rule stands as a conservative choice, and the 10-bit staircase it implies is not simulated (section 7 item 6 says so). (iii) Section 4.3 says "gate step -54 to -57 dB", but A5 reaches -53.5 dB (`result.json` `gate_step_rel_db`). **Fix:** state (i), reword (ii), correct (iii) | Open | Pending | |

Three Major findings are open, so the reviewer verdict is NEEDS CHANGES.

What holds:
- The re-run reproduces every number, plot and verdict of the note exactly.
- The detector law agrees with an independent analytic solution.
- The as-written failure is sound.
- REQ-TX-014 and REQ-SYS-183 are handled with the right caution.
- The comparative reading (A4 has more keying margin than A5) holds in every reviewer run.

The three Majors concern the claim that the mitigated loop passes for both finalists:
- The claim was not tried at the lower power steps, where both finalists fail REQ-TX-005 at the note's own corners (finding-1).
- The corner set is narrower than the known curve variation, and both finalists' margins are about the corner's size (finding-2).
- The checker cannot flag a REQ-TX-005 failure (finding-3).

### Per-case results (section F; one row per case the governing texts name)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | As written, 5 W, 3 / 5 / 8 ms, both drain ends | REQ-SYS-014 and TC-SYS-013: shape 5 %, +/-0.5 ms | A4 shape 10.0 to 19.2 %, rise 1.64 to 7.46 ms; A5 17.8 to 27.1 %, rise 1.31 to 5.66 ms | negative (FAIL both) | model | re-run identical | none |
| C-2 | As written, 3 ms | REQ-SYS-015: 350 Hz | A4 417 Hz, A5 542 Hz | -67 / -192 Hz (FAIL) | model | re-run identical; ideal envelope 291.7 Hz by independent code | none |
| C-3 | As written | REQ-TX-006: -60 dB beyond 750 Hz | A4 -49.8 dB, A5 -48.3 dB | -10.2 / -11.7 dB (FAIL) | model | re-run identical | none |
| C-4 | Mitigated, 5 W (4.0 / 2.9 W at the low pack end), 5 corners | REQ-SYS-014 and TC-SYS-013 | shape at most 2.5 % (A4) and 3.3 % (A5); times within 0.06 / 0.29 ms | +2.5 / +1.7 % shape; +0.44 / +0.21 ms | curve corner not bounded | re-run identical; 4 us step and 2 us resampling move times by at most 0.008 ms | finding-2 |
| C-5 | Mitigated, 3 ms, A5 -0.1 V corner | REQ-TX-005: 2.7 to 3.3 ms | 3.285 ms | +0.015 ms (0.5 %) | not bounded; -0.15 V gives 3.47 ms | re-run identical; wide corners | finding-2, finding-3 |
| C-6 | Mitigated, all corners | REQ-SYS-015: 350 Hz | 292 / 208 / 125 Hz | +58 Hz | small | re-run identical | none |
| C-7 | Mitigated, all corners | REQ-TX-006: -60 dB | A4 -67.2 dB, A5 -64.1 dB | +7.2 / +4.1 dB | not bounded (A4 -60.1 dB at -0.4 V, A5 -55.0 dB at +0.4 V) | re-run identical; fine-step worst cells unchanged (-67.21, -64.10 dB) | finding-2 |
| C-8 | Mitigated, 0.5 W step, the note's 5 corners | REQ-SYS-014, REQ-TX-005, REQ-TX-006 (TC-TX-005, TC-TX-006) | not analysed | not shown | | reviewer run: A5 FAIL (shape 6.3 %, rise 3.40 ms at 3 ms and 5.68 ms at 5 ms at -0.1 V; 2.57 ms at +0.1 V); A4 FAIL (rise 3.38 ms at 3 ms and 5.54 ms at 5 ms at -0.1 V); worst cells -60.6 dB (A5), -62.1 dB (A4) | finding-1 |
| C-9 | 1 W and 2 W steps; 7.4 V supply | REQ-SYS-011 with the keying requirements; TC-TX-005 | not analysed | not shown | | none | finding-1 |
| C-10 | -10 C and +45 C ambient, module heating | REQ-SYS-114 | not analysed | not shown | threshold drift 0.1 to 0.2 V (reviewer estimate) | none possible | finding-2 |
| C-11 | Overshoot, both variants | TS-012 WP-PDR-22: 0.2 dB | at most 0.01 dB | +0.19 dB | small | re-run identical | none |
| C-12 | VGG maximum, A5 | TS-012 WP-PDR-22: 3.5 V with the LM2940 at 4.75 to 5.25 V | 3.26 V (as written, 5.00 V rail), 3.13 V (mitigated) | +0.24 / +0.37 V | 5.25 V rail not modelled (3.43 V) | hand: 5.25 x 0.654 = 3.43 V | finding-8 |
| C-13 | Loop phase margin, mitigated | TS-012 WP-PDR-22: 45 degrees | 75.8 to 80.2 degrees (analytic) | +30.8 degrees | first-order model | hand: 90 - atan(2 pi 1706 x 17.7 us) - atan(2 pi 1706 x 4.7 us) = 76.4 degrees (A5, 7.9 V) | none |
| C-14 | Key-up, exciter driven | REQ-TX-014: -30 dBm | A4 -19.5 dBm (modelled leakage; range -23 to -19), A5 -17.5 dBm (at 30 dB isolation) | A4 -7 to -11 dB (FAIL by estimate); A5 not shown | estimates | hand: 2.0 to 3.0 mA through 1.63 pF at 146 MHz into 2.56 ohm gives 5.2 to 11.5 uW | none |
| C-15 | RF-ended states | REQ-SYS-183: -57 dBm | about -117 (A4) and -111 dBm (A5) | +54 to +60 dB | estimates | chain arithmetic re-added | none |
| C-16 | 12 ms late contact; open loop at 8.4 V | TS-012 WP-PDR-22 fault cases | not analysed (declared) | not shown | | none | finding-8 |
| C-17 | PWM carrier ripple at 30.5 / 61 / 122 kHz | REQ-TX-006 | A5 feedforward -43.2 / -60.7 / -78.7 dBc (analytic bound) | bound | conservative | hand: 2.10 V x 0.01183 x 0.283 x 44.1 V/V / 44.7 V = -43.2 dBc | finding-9 |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse 4ea4607:<path>` | Yes | 34 of 34 equal at `4ea4607` and at `HEAD`, checked with a Python loop over `git rev-parse`. The seven copies of `keying_run.py` in `results/` and the four run-directory decks equal the checked-in files |
| R2 | The checker runs by one command and exits with the stated result; LTspice through the wrapper | Yes | README commands run on a clean export of `4ea4607` (`git archive`) with the author's `results/` moved aside. Both detector decks and the four keying decks ran through `tools/ltspice-batch.sh`: every run PASS, exit 0, log first line `LTspice 26.0.2 for MacOS`, no warning in any log. `detchar`, the four `deck` stages and `summary` exit 0 |
| R3 | `validate_docs.py` on a JSON product | N/A | No JSON product under a schema |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary in the brief; note sections 1 to 9 |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note or the README; the six requirements are named with their TBRs |
| R6 | Every cited render exists | Yes | 16 cited renders present, plus the two uncited key-up plots |

## Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

- **Full re-run.** Every run regenerated from LTspice. Against the committed outputs:
  - all six decks byte-identical (the generator rewrote the four keying decks identically);
  - `det_law.csv`, every `result.json`, every `result.csv` and `summary.json` byte-identical;
  - all 18 PNGs pixel-identical (matplotlib image arrays equal).
- **Numerical settings (B4).** A variant of each mitigated deck with a 4 us maximum step (20 us in the record), analysed with 2 us resampling (10 us in the record), all 30 runs, through the wrapper:
  - rise and fall within 0.008 ms and shape within 0.1 % of the record in every run;
  - 26 dB bandwidths unchanged;
  - worst cells unchanged (A5 -64.10 dB, A4 -67.21 dB); individual runs within 1 dB (A5) and 2.8 dB (A4).

  The detector deck's convergence claim was not re-run; the analytic check below agrees with it.
- **Detector law by a different method (B5).** The reviewer solved the large-signal equation Is (exp(-Vo/nVt) I0(V/nVt) - 1) = Vo/RL with the deck's diode parameters, the 0.0756 tap, and the RF division between the diode capacitance (1.6 pF), the 22 pF hold and the 166 ohm tap source (factor 0.909). Results against LTspice agree within 5 %:

  | Amplitude (V peak) | Analytic | LTspice |
  |---|---|---|
  | 0.05 | 5.09 uV | 4.87 uV |
  | 0.35 | 0.259 mV | 0.248 mV |
  | 1 | 2.68 mV | 2.56 mV |
  | 1.7 | 11.2 mV | 10.6 mV |
  | 3 | 51.8 mV | 49.4 mV |
  | 22.36 | 1.27 V | 1.24 V |

  Without the hold division (the 470 pF design) the output is about 17 % higher (finding-9).
- **Spectrum routine (B5).** Independent code on the ideal envelope gives 291.7 / 208.3 / 125.0 Hz and -74.0 / -84.5 / -91.8 dB at 3 / 5 / 8 ms, equal to the note. The 28 800-sample record is exactly six periods. The F7 comparison is finding-7.
- **Analytic items.** The PWM ripple and loop margin hand checks are in rows C-13 and C-17. The slopes in `summary.json` (44.1 and 20.6 V/V, ratio 2.14) agree with the note's 44, 21 and 2.1.
- **Reviewer variants (scratchpad only, not committed).** `keying_rv.py` adds two variants to a copy of the checker:
  - `p05`: setpoint 0.5 W at both drain ends, the note's five corners;
  - `wide`: threshold corners -0.4, -0.2, -0.15, +0.15, +0.2 and +0.4 V.

  `keying_rv2.py` adds `fine` (B4). Every deck ran through `tools/ltspice-batch.sh` (PASS, exit 0). The reviewer opened the `p05` A5 corners render; it shows the foot step at the -0.1 V corner. Results are quoted in findings 1 and 2 and in rows C-5, C-7 and C-8.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a reported result)

| Note section 3 row | Source read by the reviewer | Agreement |
|---|---|---|
| RA07M1317M Pout vs VGG (7.2 V, 20 mW) | `hardware/sim/tx-pa/data/ra07_pout_vs_vgg_{135,155}.csv` (digitized, INSP-114) | Above 2.6 V within 0.1 W; at 2.3 to 2.5 V the table is 0.9 to 3.3 dB high (finding-4) |
| RA07M1317M Pout vs VDD at VGG 3.5 V | `ra07_pout_vs_vdd_155.csv` | Scale 0.619 against 0.599 at 5.5 V, and 1.174 against 1.186 at 7.9 V (finding-4, small effect) |
| AFT05MS004N Pout vs VGS (Figure 12, 155 MHz, 7.5 V, 0.1 W) | Datasheet page 11, rendered | Shape agrees within graph reading at 1.5 to 2.2 V. The curve ends at about 2.42 V and 5.7 W (finding-4), and moves about +0.5 V at Pin 0.05 W (finding-2) |
| AFT05MS004N Crss 1.63 pF, VGS(th) 1.7 / 2.2 / 2.5 V | Table 5 | Yes (the spread is finding-2) |
| A4 drain scaling; A5 and A4 leakage | TS-012 sections 1 and 7.3 (estimates) | Quoted correctly; labelled E |
| 1N5711W model (HSMS-280x parameters) | Deck `.model` line against the note | Consistent; the surrogate is labelled E; analytic cross-check above |
| Idle bias 4.7 M, 10.6 mV | 5 V x 10 k / 4.7 M = 10.6 mV | Yes; the value is the author's (TS-012 gives none), labelled E |
| Divider 0.654, 1.77 k, 10 nF | TS-012 section 7.3: 2.7 k / 5.1 k | 5.1 / 7.8 = 0.654, and 2.7 k parallel 5.1 k = 1.77 k: yes |
| Key-down sequence 7.5 / 8 / 10 ms, gate 1 ms | TS-012 section 7.3 | Yes |
| Losses 0.5 dB; drain 5.5 / 7.9 V (A5) | TS-012 section 7.3 | Yes. `lpf-ts012.md` reports up to 1.21 dB passband loss (INSP-114 X-1), which moves the low-pack setpoint, not the keying shape |
| Firmware PWM 12 bits at 30.5 kHz | 125 MHz / 4096 = 30.52 kHz, 32.768 us | The arithmetic holds; the 125 MHz clock is an assumption (ADR-031 gives 150 MHz) |
| Raised-cosine convention | REQ-SYS-014 rationale: 3 ms is a 5.1 ms full transition | `RC_1090` = 0.5903: yes |

## Checklist answers

### A. Question, scope and traceable inputs

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | No | Six requirements, RSK-045, TC-SYS-013 and WP-PDR-22 are named and exist. HZ-008, HZ-004, REQ-SYS-011, REQ-SYS-114 and RSK-011 are not named (finding-6) |
| CK-ANA-A2 | Yes | TS-012 revision 4 is cited with its commit `7d0d450`; no schematic exists; every value the note chooses is labelled |
| CK-ANA-A3 | Yes | Section 3 gives a class and a source for every row |
| CK-ANA-A4 | No | Reviewer table above: the foot of the A5 curve and the end of the A4 curve disagree with the sources (finding-4) |
| CK-ANA-A5 | No | The +/-0.1 V corner is unsourced and not bounded; the temperature and drive-level assumptions are unstated (finding-2) |
| CK-ANA-A6 | No | The F7 and TC-TX-006 conflict is not routed (finding-7); the header does not state the partial WP-PDR-22 coverage (finding-8) |

### B. Model validity

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Simplifications are listed in section 7, but the detector hold value and the ripple bound are not stated as such (finding-9) |
| CK-ANA-B2 | Yes | The only third-party model is the HSMS-280x diode, identified and labelled a surrogate |
| CK-ANA-B3 | Yes | The bandwidth routine is checked against F7's 292 Hz, and the detector law agrees with the reviewer's analytic solution within 5 % (the unexplained -60 dB point is finding-7) |
| CK-ANA-B4 | Yes | Detector step convergence is stated; the reviewer's 4 us / 2 us variant moves no reported number (above) |
| CK-ANA-B5 | Yes | Analytic detector law, independent spectrum code, and loop-margin and ripple hand checks (above) |
| CK-ANA-B6 | No | Uncertainty is listed qualitatively but not set against the A5 REQ-TX-005 margin of 0.015 ms or the corner width (finding-2) |

### C. Tools, validation status and reproducibility

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | No | The LTspice `.log` first line equals the lock; the note's spicelib version is wrong (finding-5) |
| CK-ANA-C2 | Yes | LTspice is accredited (TV-014, ACC-LTSPICE-001, wrapper blob `88b71475`); the checker has no TV record and the note marks the result developer evidence |
| CK-ANA-C3 | Yes | The README commands reproduce every number; netlists, one analysis each |
| CK-ANA-C4 | Yes | Reviewer re-run identical (above) |
| CK-ANA-C5 | Yes | TV-014 limitations respected: wrapper only, short run directories, lock, exit and log checks |

### D. Units, arithmetic and consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | V peak, dBm, dB relative to total power and dBc are used consistently; conversions re-computed (for example 22.36 V peak = 5 W in 50 ohm) |
| CK-ANA-D2 | Yes | Every table value equals the checker output. The 9.7 % is 3.29 / 3 from the rounded 3.285 ms, rounded toward the limit. The -54 dB wording is finding-9 (iii), not a number used |
| CK-ANA-D3 | Yes | Rounding goes toward the limit where it matters (3.29 ms, +9.7 %) |
| CK-ANA-D4 | No | No REQ-TX-005 constant; the setpoint constant has no source (finding-3) |

### E. Results, margins, proposed values and credit

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Limits are quoted with their ids and match the requirement texts at HEAD |
| CK-ANA-E2 | Yes | Margins have the right sign; no TPM applies to these requirements |
| CK-ANA-E3 | No | A5 REQ-TX-005 is reported PASS with 0.015 ms of margin against an unbounded corner, and both finalists' PASS depends on the corner width (finding-2); the 0.5 W step fails (finding-1) |
| CK-ANA-E4 | No | Exit 0 on FAIL; REQ-TX-005 not asserted (finding-3) |
| CK-ANA-E5 | N/A | No TBR value proposed |
| CK-ANA-E6 | N/A | No TPM current best estimate proposed |
| CK-ANA-E7 | Yes | Developer evidence on preliminary design data; no closing credit claimed |

### F. Every case named

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | 3, 5 and 8 ms and both pack ends are covered. The 0.5, 1 and 2 W steps, 7.4 V and the REQ-SYS-114 temperatures are missing (C-8 to C-10; findings 1 and 2) |
| CK-ANA-F2 | No | TS-012's late-contact and open-loop fault cases are not run (declared in section 1; finding-8) |
| CK-ANA-F3 | Yes | The worst corner is named per criterion in `result.json` and section 4.3 (the -0.1 V corner at 3 ms) |
| CK-ANA-F4 | No | The A5 REQ-TX-005 margin is within its uncertainty, and no sensitivity to the curve shift, drive level or temperature is shown (finding-2) |

### G1. Simulation decks and checkers

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | Decks, checker and plots are under `hardware/sim/tx-keying/`, and run-id folders tie them together |
| CK-ANA-G1-2 | Yes | Detector decks are `.tran` with `.meas`; keying decks are `.tran` only; the wrapper's `NC_` check passed |
| CK-ANA-G1-3 | Yes | The as-written loop follows TS-012 section 7.3 (reference, detector, idle bias, integrator, divider, clamps, sequence). The values TS-012 does not state (tap, idle bias, Cf, VGG node capacitor) are labelled as the author's |
| CK-ANA-G1-4 | Yes | The checker reads the `.raw` with spicelib and the `.meas` table of the log; `replot` refuses a changed deck; the wrapper removes stale outputs |

### G6. Timing

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G6-1 | Yes | PWM period 32.768 us from an assumed 125 MHz clock (labelled); relay 7 ms plus 0.5 ms bounce from TS-012 |
| CK-ANA-G6-2 | Yes | The keying sequence edges (relay, CLK1, ramp start, drive gate) are all in the decks |
| CK-ANA-G6-3 | Yes | No duration comes from an Emulation run |
| CK-ANA-G6-4 | N/A | No off-nominal response time is claimed (the late-contact case is finding-8) |

### G7. Worst-case and tolerance

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme-value corners, one factor at a time, stated in section 4.3 |
| CK-ANA-G7-2 | No | No temperature coefficient; the threshold corner is not derived from the device tolerances (finding-2) |

### H. Hazards, risks and records

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | HZ-008 and HZ-004 are not named; no request to the hazards writer (finding-6) |
| CK-ANA-H2 | No | The re-scored envelope-loop risk is not sent to the risk writer (finding-6) |
| CK-ANA-H3 | No | No change history (finding-6) |

### I. Visual closure

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | The reviewer opened all 16 cited renders and the two uncited key-up plots (18), plus the rendered AFT05MS004N Figure 12 |
| CK-ANA-I2 | Yes | Axes carry units; limits are drawn with their ids (TC-SYS-013 band, REQ-SYS-015 band, REQ-TX-006 mask, REQ-TX-014 and REQ-SYS-183 lines); legends are present; each title names its case. Plotted values agree with `result.json` at the titled points (for example A5 as written, 542 Hz and -48.4 dB at 3 ms, 5.5 V; A5 mitigated, -64.1 dB at the -0.1 V corner) |

**ITEMS N/A:** CK-ANA-E5, CK-ANA-E6, CK-ANA-G2 to G5 (analysis_kind is simulation-deck, timing and worst-case), CK-ANA-G6-4, CK-ANA-J1 to J3 (criticality neither).

## Cross items (returned to Claude as lead SE)

- **X-1. TS-012 section 7.3 VGG graph read.** The note's F1 agrees with INSP-114 X-2: TS-012's "about 0 W at 1.5 V, 2 W at 2.5 V, 4 W at 3.0 V, 7 W at 3.5 V" does not match the RA07M1317M page 5 curves (digitized: about 1.0 W at 2.5 V, 7.1 W at 3.0 V, 8.4 W at 3.5 V). One request to the TS-012 author covers both.
- **X-2. TC-TX-006 known answer.** Two independent computations give 395 to 435 Hz for the -60 dB point, not the 614 Hz of F7 that TC-TX-006 step 2 uses as the checker's known answer. The TC-TX-006 author and the F7 owner should re-derive it before the TC-TX-006 checker is written (finding-7).
- **X-3. Owner-facing reading.** Three conclusions of the note hold in every reviewer run and can be read now: A4 has more keying margin than A5; the loop as written fails for both; REQ-TX-014 fails for A4 by estimate. The absolute claim "both pass every keying check" should not go to the owner until findings 1 and 2 are answered: at the 0.5 W step both finalists fail REQ-TX-005 at the note's own corners.

## Commands

- Search: `mcp__claude-context__search_code` on path `/Users/robinonsay/rust/cwht`, with the queries "keying envelope analysis TS-012 ALC detector key click review checklist" and "INSP id register next free inspection id INSP-116".
- Freeze and blobs: a Python loop over `git rev-parse 4ea4607:<path>` and `git rev-parse HEAD:<path>` (34 files).
- Re-run:
  1. `git archive 4ea4607 tools hardware/sim/tx-keying | tar -x -C <scratchpad>/kx`, then move the author's results to `results-author`.
  2. Run the two `tools/ltspice-batch.sh -t 600 -o ... -b det_char*.cir` commands of the README.
  3. Run `.venv/bin/python hardware/sim/tx-keying/keying_run.py` with `detchar`, `deck a4 asis`, `deck a4 mitig`, `deck a5 asis`, `deck a5 mitig` and `summary` (every exit 0).
  4. Compare bytes and pixels in Python.
- Variants: `<scratchpad>/kv/hardware/sim/tx-keying/keying_rv.py deck {a5,a4} {wide,p05}` and `keying_rv2.py deck {a5,a4} fine`, each through the wrapper (PASS, exit 0).
- Datasheet: the AFT05MS004N PDF from the web-fetch tool (SHA-256 prefix `84cd9fae`), read with `pdftotext -layout` and `pdftoppm -r 200 -f 11 -l 11`.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` (result in the reviewer's return).

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keying-ts012.md@bad53754, hardware/sim/tx-keying/keying_run.py@f85f2e29, decks and results as in product_files, at 4ea4607
FINDINGS:
- [Major] CK-ANA-F1, E3, A5 finding-1: the 0.5, 1 and 2 W steps (REQ-SYS-011; TC-TX-005 and TC-TX-006 name 0.5 W) are not analysed; reviewer run at 0.5 W with the note's own +/-0.1 V corners: A5 fails REQ-SYS-014 and REQ-TX-005 (shape 6.3 %, rise 3.40 ms at 3 ms, 5.68 ms at 5 ms), A4 fails REQ-TX-005 (rise 3.38 ms at 3 ms, 5.54 ms at 5 ms).
- [Major] CK-ANA-A4, A5, B6, E3, F4, G7-2 finding-2: the +/-0.1 V curve corner is unsourced and narrower than lot spread (AFT05 VGS(th) 1.7 to 2.5 V), drive-level shift (Figure 12) and temperature; A5 holds for about +/-0.12 V and A4 for about +/-0.15 to 0.2 V; the A5 REQ-TX-005 margin is 0.015 ms.
- [Major] CK-ANA-E4, D4, D2 finding-3: the checker does not assert REQ-TX-005 (+/-0.5 ms only), exits 0 on FAIL, and its setpoint criterion has no source.
- [Minor] CK-ANA-A4, A3 finding-4: graph reads differ from the project's digitized RA07M1317M curves at the foot and from Figure 12's end point; the slope estimate's direction is unstated.
- [Minor] CK-ANA-C1 finding-5: spicelib version misstated (1.6.3, not 2.5).
- [Minor] CK-ANA-A1, H1, H2, H3 finding-6: HZ-008, HZ-004, REQ-SYS-011, REQ-SYS-114 and RSK-011 not named; no risk or hazard requests; no change history.
- [Minor] CK-ANA-B3, A6 finding-7: the 395 against 614 Hz explanation is not shown; the TC-TX-006 known-answer conflict is not routed.
- [Minor] CK-ANA-A6, F2 finding-8: the header presents a partial WP-PDR-22 run as the pre-order check; the fault cases and the LDO range are not run.
- [Minor] CK-ANA-B1, D2 finding-9: detector hold value effect, PWM ripple "fail" wording on a bound, gate-step range.
ITEMS N/A: CK-ANA-E5, E6, G2 to G5, G6-4 (analysis_kind simulation-deck, timing, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: none
MEASUREMENTS: size=6 decks, 84 envelope runs and 26 detector steps; inputs_checked=12 rows (every input that sets a reported result); renders=18; turns=80; minutes=130; major=3; minor=6
```
