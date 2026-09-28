---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-21 PA drive window and
# output power analysis for the TS-012 finalists A4 and A5, iteration 1 at freeze commit b705428 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Approved 2026-09-28, merge held at the
# section 9 pre-merge check). tools/validate_docs.py requires the checklist field to name a template that exists
# on main, so the field names peer-review-checklist-design revision B and checklist_analysis records the template
# actually applied, as INSP-056 and INSP-083 did. The delta iteration after CR-012 merges switches the field.
# id: the brief assigned no id. INSP-114 is above every id on main (HEAD 6bff79c), on every cr/ branch and in the
# working tree at the time of filing (INSP-111 is the highest in use).
# Filed by the lead SE on 2026-09-28 from the reviewer's own text: the harness refused the reviewer's Write of this
# new file ("Subagents should return findings as text"). Content is verbatim except the id, reassigned from
# INSP-112 to INSP-114 because three parallel reviewers (review:pa-drive-1 among them) each took INSP-112 as the next free id.
id: INSP-114
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-pa-drive-ts012.md
product: docs/design/analysis/pa-drive-ts012.md
# product_commit: b705428, the WP-PDR-21 tx-pa commit. Every blob below equals git rev-parse b705428:<path> and
# HEAD:<path> at HEAD 6bff79c (no product file changed after the freeze).
product_commit: "b705428a34ae6f0db25263a2fe953c481b537568"
product_files: ["docs/design/analysis/pa-drive-ts012.md@ecffcb3ff90eb115cf6204a9a3f835756405f0ee", "hardware/sim/tx-pa/README.md@4c44ad9fdc0b6feb57453d8571fbe04bab0e1aab", "hardware/sim/tx-pa/run_pa.py@acbe1457a7a26cf4980afa8e3222350f34e1248a", "hardware/sim/tx-pa/digitize_ra07.py@85c2e226def52682a1d5c622fcb9d57bc31f3584", "hardware/sim/tx-pa/digitize_aft05.py@94bb20e56436d39f423426284fca7ad4a1b3bafb", "hardware/sim/tx-pa/decks/drive_a4.cir@7d06ec7a61b84fb82365a34db0232488e6a8e6e8", "hardware/sim/tx-pa/decks/drive_a5.cir@5cce872bfaec25e26da07e0948ecd96096d44f84", "hardware/sim/tx-pa/decks/gva_check.cir@d73282853f2693d3e3ab9b7d3c62251b1c3a4b3f", "hardware/sim/tx-pa/decks/power_a4.cir@9d935a12cc9d5888de481d1eecc3c790d8a1fd87", "hardware/sim/tx-pa/decks/power_a5.cir@ea5b3ed0e465e4f65d5b82a5ed9477b580a09f07", "hardware/sim/tx-pa/decks/power_a5_sot.cir@515c59356eca9bbad229f3b4410dfd99f44d806d", "hardware/sim/tx-pa/data/aft05_pout_vs_pin_135.csv@c42891a3e844844c433791d7d6fc15e5a982eb29", "hardware/sim/tx-pa/data/aft05_pout_vs_pin_155.csv@c868b3f90db74c4b165aec3c7a578c5af64207c3", "hardware/sim/tx-pa/data/aft05_pout_vs_pin_overlay.png@ef68932c8fcbf2b57f01b30c5ac8b357be9ea7dd", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_135.csv@fa9a9268175ef36e4a5a1315c8ef214216f72009", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_135_overlay.png@c47e16290f9162ecde031ce910fc02f9cd0603c7", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_155.csv@940931a7e169483373ef2155022fa8a15fa55e81", "hardware/sim/tx-pa/data/ra07_pout_vs_pin_155_overlay.png@f12256f8e2d7abb28ac6d6cdeb40ba3ba93bc3a1", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_135.csv@653ad373080ec2e92f53cbca27072afb6e32963b", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_135_overlay.png@9feb9fcc54abc91cfb15a39bfb12c68b905eaf80", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_155.csv@a92785b7f643fe012b431bf655f825f9ff8ff967", "hardware/sim/tx-pa/data/ra07_pout_vs_vdd_155_overlay.png@b96503dd4aab6c4e489f76a664edffde4f3ad5ed", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_135.csv@9a877b511ffa2e9d0a9a31d53502b80f59cee9c9", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_135_overlay.png@5033bbe003a3296837a5a1ca313edadb0a11c2ad", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_155.csv@83a9f93a85484025d2f3217a11b6873f414ced4b", "hardware/sim/tx-pa/data/ra07_pout_vs_vgg_155_overlay.png@0602ee3e1a6ad2fcbd9475d1aec36d88772704fe", "hardware/sim/tx-pa/results/2026-09-28-d1-gva-model/gva_compression.png@e96846e2cb3c2ba197997702d8532427e15372a5", "hardware/sim/tx-pa/results/2026-09-28-d1-gva-model/result.json@db04d4e5c43dc4aa776109be6f65396464b654c6", "hardware/sim/tx-pa/results/2026-09-28-d2-drive-a5/drive_a5_corners.png@9934bf5fd06dd730c50b1627f5bc8c9a79b68b96", "hardware/sim/tx-pa/results/2026-09-28-d2-drive-a5/drive_a5_h3.png@04ad79329eeaca3126e5f2391b2808dc5ad24cc3", "hardware/sim/tx-pa/results/2026-09-28-d2-drive-a5/result.json@6d50c1202e08326ad3869ba5f10602237ffa4697", "hardware/sim/tx-pa/results/2026-09-28-d3-drive-a4/drive_a4_corners.png@353196998dd4e12d418da3b1bf1b9cdf9917cdf3", "hardware/sim/tx-pa/results/2026-09-28-d3-drive-a4/drive_a4_h3.png@15e738c62d1d884631256faa8ba4228ceee72512", "hardware/sim/tx-pa/results/2026-09-28-d3-drive-a4/result.json@fa99e6e09a69f031fce50a8068cb7bc6f6b51e08", "hardware/sim/tx-pa/results/2026-09-28-p1-power-a5/power_a5_sma.png@6eb740e79cb257c7c85157d4cb7427d12869065d", "hardware/sim/tx-pa/results/2026-09-28-p1-power-a5/result.json@9cd9adc302cd808108fdd2c797159b6597484f74", "hardware/sim/tx-pa/results/2026-09-28-p2-power-a4/power_a4_sma.png@fef34efa40494ad77ead4f8b33e75d6ab6cdc68a", "hardware/sim/tx-pa/results/2026-09-28-p2-power-a4/result.json@0eb8087763665980ef64246d151a615373925034", "hardware/sim/tx-pa/results/2026-09-28-p3-power-a5-sot/power_a5_sma.png@09795d539d3e5112a1819fcfb8d91efda50c9f60", "hardware/sim/tx-pa/results/2026-09-28-p3-power-a5-sot/result.json@3836ce85522bd78f126db448ab2a40fabe4e8ece", "hardware/sim/tx-pa/results/2026-09-28-s1-summary/pin_at_pa_vs_pack.png@427733e5ce69f8304f21f18c1a10764bc971be6f", "hardware/sim/tx-pa/results/2026-09-28-s1-summary/pout_at_sma_vs_pack.png@d5735481713975d86ac1f74f460af30a8ca3d27b", "hardware/sim/tx-pa/results/2026-09-28-s1-summary/result.json@2dcb45ab6935bf6ac60e2a8b55153d9652014187"]
analysis_kind: [simulation-deck, cascade, worst-case]
product_size: 1 note; 6 LTspice decks (270 + 270 drive corners, 648 + 1458 + 648 power corners, 75 model-check steps); 1 checker; 2 digitizers; 8 digitized curves; 17 renders (10 result plots, 7 digitizer overlays); 66 input rows
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/tx-pa/*.py: developer evidence per 05 section 9.1, as the note says"]
# values_proposed: the note proposes no TBR value and no TPM current best estimate; section 7 C4 and C5 put
# requirement-delta choices to the owner through TS-012, not values.
values_proposed: []
renders_inspected: 17
sprint: PDR-prep
author_agent: "author:WP-PDR-21 tx-pa (Claude as analysis author, TS-012 discriminating analyses; commit b705428)"
reviewer_agent: "reviewer:WP-PDR-21-analysis-pa-drive-iter1 (independent; authored no part of the note, decks, checker, digitizers or TS-012)"
# criticality: a hardware-only transmit analysis; it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
# verdict (rule C1, iteration 1): two Major findings are open, so NEEDS CHANGES. Iteration 2 is a delta that verifies
# the Major fixes only; Minor findings raised after the first APPROVED verdict become liens due at the CDR
# readiness declaration.
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 6
findings_open: 8
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A1, CK-ANA-A2, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B2, CK-ANA-B6, CK-ANA-D2, CK-ANA-E2, CK-ANA-E3, CK-ANA-E4, CK-ANA-F1, CK-ANA-F4, CK-ANA-G1-3, CK-ANA-G7-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-I2]
effort_turns: 70
effort_minutes: 95
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record: PA drive window and output power, TS-012 finalists A4 and A5 (INSP-114, iteration 1)

**Product:** `docs/design/analysis/pa-drive-ts012.md` (`ecffcb3f`) with `hardware/sim/tx-pa/` (README `4c44ad9f`; checker `run_pa.py` `acbe1457`; digitizers `digitize_ra07.py` `85c2e226` and `digitize_aft05.py` `94bb20e5`; six decks; eight digitized curves with overlays; seven result runs) at freeze commit `b705428` (rule C2). Every blob equals `git rev-parse HEAD:<path>` at `HEAD` `6bff79c`. No product blob lives on a `cr/` branch.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck, cascade (the transmit line-up drive) and worst-case (extreme-value corners): sections A to F, G1, G5, G7, H and I apply. G2, G3, G4 and G6 are N/A (not a budget, thermal, RF exposure or timing analysis); J is N/A (criticality neither).

**Acceptance criteria (rule C7, every case the governing texts enumerate):**
- REQ-SYS-012 (`docs/requirements/sys/requirements.json`): "The transceiver shall hold its 5 W step within +/-1 dB (TBR) into 50 ohm over its transmit range at 6.4-8.4 V pack." Bounds 3.972 and 6.295 W. Verification note: pre-build supporting simulation "over 6.4 to 8.4 V at 144, 146 and 148 MHz".
- REQ-SYS-008: transmit carrier 144.0012 to 147.9988 MHz (TBR), so the band edges and centre (144, 146, 148 MHz in the decks).
- REQ-SYS-114: "The transceiver shall meet its requirements at ambient temperatures from -10 C to +45 C (TBR)", which conditions REQ-SYS-012.
- TS-012 revision 4 section 7.3, WP-PDR-21 pre-order drive check: "pass: module input 10 to 30 mW at every corner (144 to 148 MHz, 25 and 50 ohm source, GVA gain 22.5 and 25 dB), 3f at the GVA input at least 25 dB below the fundamental."
- RA07M1317M datasheet (Jun. 2019, page 2): Pin 30 mW maximum rating; stability "VDD=4.0/7.2/9.2V, Pin=10/20/30mW, Pout<=8W (VGG control), Load VSWR=4:1"; Pout 10 W maximum at VGG 3.5 V or less; VGG 4 V maximum at VDD 7.2 V or less.
- GVA-84+ Rev. F absolute maximum input +13 dBm.
- TPM-015 (carrier-power: PDR "within +/-1 dB by analysis ... over the pack voltage range"; red threshold includes "the 5 W step unreachable at the cutoff voltage") and TPM-004 (pa-efficiency, planned 60 %, red below 55 %), both in the `mop_ids` of REQ-SYS-012.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (the PA drive analysis, the INSP id register) preceded every `grep` and `find`; `grep` only pinned lines in TS-012, INSP-110, 04 and the requirement file. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).** The four vendor PDFs the note cites, from the session cache, each matching the SHA-256 prefix in the block README: Mitsubishi RA07M1317M Jun. 2019 (`5a847a09`), https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/ra07m1317m.pdf; NXP AFT05MS004N Rev. 0 (`84cd9fae`), https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf; Mini-Circuits GVA-84+ Rev. F (`49daf1cb`), https://www.minicircuits.com/pdfs/GVA-84+.pdf; Skyworks Si5351A/B/C-B Rev. 1.3 (`f3bc5285`), https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf. RA07M1317M pages 3 to 5 were rendered at 110 dpi and read beside the overlays.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-G1-3, B2, E3, A6 | decks `drive_a5.cir` and `drive_a4.cir` lines `Rsrc vs clk`, `Ctap clk 0 5p`, `C1 clk 0 18p`; note sections 2, 4.2 ("Overdrive is designed out"), 5 (a), 4.7; TS-012 section 8.1 block diagram | The Si5351-to-drive-LPF interface is not modelled as designed, and the drive result that decides the A5 window rests on it. (i) The decks put the LPF's 18 pF input capacitor and the 5 pF tap directly on the CLK1 pin, 23 pF in all, against the Si5351 "Load Capacitance CL ... 15 pF" maximum (Rev. 1.3 Table 7); the edge and duty values the source model takes from Table 7 are specified at CL 5 pF inside that limit, so every reported drive corner uses the source outside its specified load range. (ii) TS-012 section 8.1 puts the Si5351 on the Adafruit 2045 module and the drive LPF on the separate RF board, so a board-to-board interconnect lies between them; the note does not model or mention it. Reviewer estimate (a frequency-domain model that reproduces the note's 270 A5 corners within 0.02 dB, with a lossless 50 ohm line, velocity factor 0.66, the tap at the pin): the A5 drive range becomes 5.8 to 30.5 mW with 5 cm of line (1 corner above 30 mW), 5.7 to 32.7 mW with 10 cm (12 corners above) and 5.7 to 36.2 mW with 15 cm (18 corners above); over any line length the highest corner spans 29.6 to 48.7 mW. The note's highest corner, 29.5 mW, is 0.07 dB under the 30 mW maximum rating, yet sections 4.2 and 5 (a) state "Overdrive is designed out" and the author summary "Overdrive never happens": that margin is far below the uncertainty of this unmodelled term and of the estimated source terms (25 ohm corner, 0.5 ns edge, VDDO +/-3 %). Fix: state the designed interface (placement, line or wire length and impedance, where the tap sits) and model it, or bound it over the plausible lengths; keep the CLK1 load within 15 pF (for example an L-first drive filter or a series element at the pin) or state the out-of-rating use and send it to the TS-012 author as a design request (A6); report the overdrive margin with its uncertainty and withdraw "designed out" unless shown. The select-on-test route (C1) absorbs a fixed line in the build reading, which the note can say once the interface is stated | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-F1, A5, G7-2, B6, E3 | note sections 2 ("Corners"), 3, 5 (b), 6, 7 C2 and C3; decks `power_a5.cir`, `power_a4.cir` | REQ-SYS-114 makes REQ-SYS-012 hold from -10 C to +45 C ambient; the note has no temperature case, and it does not state that every curve and value it uses is at Tcase or TA 25 C (both PA datasheets and the GVA-84+ and Si5351 tables), nor in which direction temperature moves the result. The terms that move with temperature are not small against the closure margin the note reports: the drain feed includes two cells whose resistance rises in the cold (TS-012 section 7.3 takes 0.04 to 0.06 ohm at room temperature, estimate), and the module sits on a sink whose flange TS-012 estimates at 70 to 99 C at the 45 C corner, while the RA07M1317M output data are all at Tcase 25 C. The closure claim of section 5 (b), "The lowest corner passes (4.31 to 4.45 W) with two TS-012 items", has +0.35 dB of margin at 4.31 W (+0.23 dB at the VGG the revision-4 clamp can reach, finding-3), and the note does not compare that margin with its uncertainty (graph reads about +/-0.1 W, the separable module model, the output-loss allocation). The GVA-84+ gain drift is negligible (0.0004 dB/C at 0.1 GHz, Rev. F), so the open terms are the cell resistance and the module output at temperature. Fix: add a cold (-10 C) and a hot (+45 C ambient, with the WP-PDR-28 flange temperature) corner with sourced or labelled-estimate values for the cell resistance and the module output, or state the omission as a limitation with its direction and carry it into the C2 and C3 pass criteria; state the uncertainty of the (b) margin | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-A5, B1 | note section 3 row "VGG at the ALC top: 3.5 V, or 3.08 V"; sections 4.4, 5 (b), 6 item 2, 7 C3; `run_pa.py` `A5_VGG_CLAMP_LO`, `ivgg` values | The revision-4 clamp puts VGG at 3.08 to 3.46 V (nominal 5.0 x 0.654 = 3.27 V), so the "3.5 V" level that the nominal and highest corners and the closure figure 4.31 W use is above what the design can reach. Reviewer re-solve of the same model: nominal at 6.4 V 4.70 W at 3.27 V (4.87 W reported at 3.5 V, -0.15 dB); lowest corner with the feed at most 0.35 ohm 4.28 W at 3.46 V and 4.19 W at 3.3 V (C3's "at least 3.3 V"), against 4.31 W reported. No verdict changes, but C3's pass figure is at a VGG the design cannot reach. Also, limitation 2 gives a direction only for the VGG-at-low-VDD term; the drive and VGG interaction at the lowest corner (Pin 6 mW with VGG 3.08 V, a less saturated module, where Pin sensitivity is larger than the 0.28 dB the VGG 3.5 V curve shows) may be optimistic, and the note should say so. Fix: use the clamp's nominal and maximum for the nominal and highest corners, state C3 at the VGG it requires, and state the interaction's direction | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-F4, E3, A6 | note section 4.2 "Select-on-test pad", its pad table; section 7 C1; `run_pa.py` `SOT_STEP_DB`, `SOT_MEAS_DB` | The select-on-test result 11.0 to 27.2 mW (0.41 dB inside the window) rests on three things the note does not show. (i) The step: the E24 table's losses step by up to 1.38 dB (19.88 to 21.26) and 1.26 dB (17.79 to 19.05), not 1 dB; with a 0.69 dB half-step the band is 10.5 to 28.4 mW (reviewer, same method). (ii) The +/-1 dB level reading at about 17 mW with a diode probe on the Fluke 174 has no basis: 04 section 6.2 expects the probe's 10 to 15 % at the 5 W level, while at 17 mW the peak is about 1.3 V, where the diode drop is a large fraction; with +/-1.5 dB the band is 9.8 to 30.5 mW, outside the window (F4 sensitivity, not shown). (iii) The REQ-SYS-144 delta that admits "drive pad selection" is a Proposed row of TS-012 section 8.10 and names the NanoVNA and tinySA, not the diode probe; REQ-SYS-144 as baselined allows no adjustment. Fix: use the table's real steps, state the reading method and its uncertainty basis (or a probe characterization at this level) with the sensitivity, and say that C1 depends on the owner accepting the REQ-SYS-144 delta and on the instrument (the owner buys the tinySA later, status note 2026-09-28 section 1) | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-E4 | `run_pa.py` `main()` | The checker computes pass flags against the acceptance values into `result.json` and `result.md`, but always exits 0, including on the FAIL verdicts the note reports (reviewer run: exit 0 with d2, p1, p2 and p3 FAIL). 08 section 3.4 and E4 ask for a non-zero exit on a failing case. Fix: exit non-zero when a verdict fails (or add a `--check` mode that does, with the expected FAIL states listed in the note so that a changed verdict is detected) | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A1, A2, E2, H1, H2 | note header "Serves" row, sections 4.4, 5, 7 C4 | (i) TPM-015 and TPM-004 (the `mop_ids` of REQ-SYS-012) are not named: the nominal corner under 5.0 W at 6.4 V for both finalists meets TPM-015's red wording "the 5 W step unreachable at the cutoff voltage" if 6.4 V is that voltage, and A5's 0.45 minimum efficiency is below TPM-004's 55 % red line; the note gives the numbers but not the TPM comparison or a request to the TPM owner. (ii) REQ-SYS-114 is not named (finding-2). (iii) Hazards are not named: HZ-001's description assumes "up to 10 W at 8.4 V full drive" with the ALC open, which the note's 9.86 W module and 8.99 W at the SMA bound, and HZ-003 carries the module dissipation; no request goes to the `hazards.json` writer. (iv) The re-quantified REQ-SYS-012 risks (TS-012 section 7.1 rows A5 9 Yellow and A4 15 Red) go to the owner in C4 but not as a request to the WP-PDR-18 risk writer. (v) The design data are cited as "TS-012 revision 4" without its commit (`7d0d450`). Fix: add the ids, the TPM threshold comparison and the requests (PDR work plan section 5.3) | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-D2, I2 | note section 5, A4 second bullet; `results/2026-09-28-d2-drive-a5/result.md` first line and last bullet; `results/2026-09-28-p3-power-a5-sot/power_a5_sma.png` title | (i) Section 5 says A4 misses 3.97 W "at every corner below about 6.8 V"; section 4.5 and `p2` give the highest corner 4.49 W at 6.4 V, so it is the nominal corner that crosses at 6.8 V. (ii) `result.md` of d2 reads "FAIL at all 270 corners (210 in the window ...)", which reads as all corners failing; it means the all-corners verdict. Its line "A fixed pad 0.00 dB larger would bring the maximum to 30 mW" carries no information. (iii) The p3 plot has the same title as the p1 plot and does not name the select-on-test case (I2). Fix: reword the three | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-B1 | note sections 2 and 6 item 4; `run_pa.py` `GAINS`, `RAPP_*` | TS-012 section 7.3 names "the GVA-84+ S-parameters" for this check; the note uses a flat 50 ohm behavioural block with the 0.1 GHz gain limits and does not say it departed from the named method or why. The departure is reasonable (Rev. F gives 22.9 and 23.3 dB input and output return loss at 0.1 GHz), but the typical gain falls from 24.1 dB at 0.1 GHz to 21.7 dB at 1 GHz, so taking the 0.1 GHz limits at 144 to 148 MHz is slightly optimistic for the under-drive corners, and the direction is not stated. Fix: state the departure and its direction, or read the gain at 146 MHz from the vendor S2P file | Open | Pending | |

Two Major findings are open, so the reviewer verdict is NEEDS CHANGES. The arithmetic, the digitizing, the LTspice runs and the datasheet reads all hold (sections B5, C4 and the input check below); both Majors concern what the model leaves out (the CLK1 interface and temperature) against margins of 0.07 and 0.35 dB that the note reports as conclusions.

### Per-case results (section F; one row per case the governing texts name)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | A5 drive, all 270 corners (Si5351 25 and 50 ohm, 3 edge and VDDO cases, GVA gain 22.5 to 25.3 dB, 3 P1dB sets, 144, 146, 148 MHz) | TS-012 WP-PDR-21: 10 to 30 mW; RA07M1317M Pin 30 mW maximum | 6.0 to 29.5 mW, nominal 12.6 mW; 60 below 10 mW, 0 above 30 mW | low -2.2 dB (FAIL); high +0.07 dB | not stated; interface term up to +2.2 dB (finding-1) | LTspice re-run identical; phasor model 5.98 to 29.58 mW, 60 below | finding-1 |
| C-2 | A5 drive, TS-012 criterion corners (25 and 50 ohm, gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 case) | TS-012: 10 to 30 mW | 8.5 to 22.7 mW, 27 of 36 inside | low -0.71 dB (FAIL) | as C-1 | phasor 8.51 to 22.71 mW, 27 inside | finding-1 |
| C-3 | 3f at the GVA-84+ input, both chains | TS-012: at most -25 dBc | worst -34.4 dBc (A5), -34.5 dBc (A4) | +9.4 dB | edge-time estimate | re-run same; tight-step run same (-34.42 dBc) | none |
| C-4 | GVA-84+ input level | Rev. F: +13 dBm maximum | -7.5 dBm (A5), -1.1 dBm (A4) | +20.5 dB, +14.1 dB | small | phasor -7.51 and -1.05 dBm | none |
| C-5 | A4 drive, all 270 corners | AFT05 Table 9 0.2 W ruggedness drive (informative, no rating) | 50 to 168 mW, nominal 96 mW | +0.76 dB | as C-1 | phasor 50.4 to 168.4 mW | finding-1 |
| C-6 | A5 at 6.4 V pack, lowest corner, typical module | REQ-SYS-012: at least 3.972 W | 3.71 W | -0.30 dB (FAIL) | graph reads, separable model, no temperature | Python fixed-point re-solve 3.71 W | finding-2, finding-3 |
| C-7 | A5 at 6.4 V, nominal corner | REQ-SYS-012 band; TPM-015 5 W reachable | 4.87 W (at VGG 3.5 V) | +0.89 dB to 3.97 W; -0.11 dB to 5.0 W | as C-6 | re-solve 4.87 W; 4.70 W at the 3.27 V nominal clamp | finding-3, finding-6 |
| C-8 | A5 at 6.4 V, datasheet-minimum module, lowest corner | REQ-SYS-012: 3.972 W | 3.03 W (3.62 W with feed at most 0.35 ohm and VGG 3.5 V) | -1.18 dB (FAIL) | uniform 6.5 W scale (estimate) | re-solve 3.04 W | none (stated, C4 to the owner) |
| C-9 | A5 at 6.4 V, lowest corner with the C2 and C3 levers | REQ-SYS-012: 3.972 W | 4.31 W | +0.35 dB | not stated | re-solve 4.30 W; 4.19 W at VGG 3.3 V | finding-2, finding-3 |
| C-10 | A5 at 8.4 V, ALC open (VGG 3.5 V) | RA07M1317M: stability to 8 W; 10 W maximum | module 9.13 W nominal, 9.86 W highest; above 8 W from 7.5 V | -0.9 dB to 8 W (outside the stability range); +0.06 dB to 10 W | as C-6 | re-solve 9.15 W nominal | none (stated, WP-PDR-22) |
| C-11 | A5 with the select-on-test drive, 6.4 V | REQ-SYS-012 | lowest 3.83 W, nominal 4.93 W | -0.16 dB (FAIL) | as C-6 | re-run identical | finding-4 |
| C-12 | A5 select-on-test drive window | TS-012: 10 to 30 mW | 11.0 to 27.2 mW (estimate) | +0.41 dB | not stated | 10.5 to 28.4 mW with the table's steps; 9.8 to 30.5 mW at +/-1.5 dB reading | finding-4 |
| C-13 | A4 at 6.4 V: lowest, nominal, highest | REQ-SYS-012: 3.972 W | 2.05, 3.54, 4.49 W | lowest -2.87 dB, nominal -0.50 dB (FAIL) | estimated (Vd/7.5)^n and match loss (Low) | re-solve 2.05, 3.54, 4.50 W; hand: 6.75 W x (5.96/7.5)^2 x 0.944 x 0.891 = 3.56 W | finding-7 |
| C-14 | A4 at 8.4 V lowest corner | REQ-SYS-012: 3.972 W | 3.76 W | -0.24 dB (FAIL over the whole range) | as C-13 | re-solve 3.76 W | none |
| C-15 | Band edges and centre, 144.0012 and 147.9988 MHz | REQ-SYS-008 | 144, 146 and 148 MHz in every deck | n/a | 0.34 dB drive span in a unit | corners checked | none |
| C-16 | -10 C and +45 C ambient | REQ-SYS-114 with REQ-SYS-012 | not analysed | not shown | not stated | none possible | finding-2 |
| C-17 | GVA-84+ model check | Rev. F P1dB 19.4 / 20.4 dBm, Psat 21.7 dBm | 19.37 / 20.37 / 21.37 and 20.69 / 21.69 / 22.69 dBm | within 0.03 dB | model fit | re-run identical | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse b705428:<path>` | Yes | 43 of 43 equal at `b705428` and at `HEAD` `6bff79c` (Python loop over `git rev-parse`) |
| R2 | The checker runs by one command and exits with the stated result; LTspice through the wrapper | Yes | Clean export of `b705428` (`git archive`) to the scratchpad with the author's `results/` moved aside; `.venv/bin/python hardware/sim/tx-pa/run_pa.py all`: exit 0, every run's LTspice provenance `exit 0`, log first line `LTspice 26.0.2 for MacOS` (six decks), no "warning" in any log |
| R3 | `validate_docs.py` on a JSON product | N/A | No JSON product under a schema |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary in the brief; note sections 1 to 7 and header |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note or README; REQ-SYS-012 named with its TBR |
| R6 | Every cited render exists | Yes | 9 cited renders present, plus the p3 plot and 7 overlays |

## Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

- **Full re-run.** All seven runs regenerated from LTspice (not the `CWHT_PA_REPLOT` path, so the author's "redrawn without re-running LTspice" last pass is also covered). Against the committed outputs: all six decks and all six `result.md` byte-identical; all seven `result.json` identical after removing the provenance block; both `corners.json` identical; all 10 result PNGs pixel-identical (matplotlib image arrays equal); the seven copies of `run_pa.py` in `results/` equal the checker blob.
- **Numerical settings (B4).** A variant of `drive_a5.cir` with `.tran 0 230n 200n 2p` (maximum step 2 ps instead of 10 ps, settling 200 ns instead of 90 ns) at the highest (idx 128), lowest (141) and nominal (202) corners, through the wrapper (exit 0, no warning): 29.521, 5.967 and 12.612 mW and 3f -34.42, -56.00, -45.39 dBc, equal to the note's corners within 0.0001 dB.
- **Drive chain by a different method (B5).** A frequency-domain model written by the reviewer: trapezoid Fourier coefficient (2 Vpp / pi) |sin(pi d)| sinc(f tr), nodal solution of the source, tap, LPF with its parasitics and pads, and the Rapp limiter as a describing function on a sine. A5 5.98 / 12.64 / 29.58 mW, 60 corners below 10 mW, 27 of 36 criterion corners inside, GVA input -10.07 and -7.51 dBm; A4 50.4 / 96.0 / 168.4 mW. Agreement within 0.02 dB. Hand checks: ideal 3.3 Vpp square into 50 / 50 ohm, 10.43 dBm available (TS-012's +10.4 dBm); 1 ns 20-80 % edge factor at 146 MHz -0.86 dB; 18 / 82 / 18 C-L-C Butterworth corner 1 / (2 pi 18 pF 50 ohm) = 177 MHz and 10 log(1 + (146/177)^6) = 1.19 dB (the note's 1.2 dB).
- **Power path by a different method (B5).** A Python fixed-point solve of Vd = Vp - Rf (Ibus + P / (eta Vd)) on the digitized curves read by median and interpolation (not the author's resampled tables or LTspice): A5 at 6.4 V nominal 4.87 W (Vd 5.76 V), lowest 3.71 W, highest 5.42 W, minimum module 3.04 W, levers 4.30 W; at 8.4 V nominal 8.15 W, module 9.15 W; A4 3.54 / 2.05 / 4.50 W at 6.4 V and 6.15 / 3.76 / 7.60 W at 8.4 V. All within 0.02 W of the note.
- **Sensitivity terms.** Recomputed from `corners.json` and the p1 and p2 `.raw`: A5 drive gain 2.74, Si5351 case 2.37, source R 1.51, frequency 0.26, P1dB 0.04 dB, within-unit frequency span 0.336 dB; A5 power at 6.4 V module spread 0.95, feed 0.44, VGG 0.41, drive 0.30, efficiency 0.20, loss 0.20, frequency 0.03 dB; A4 drive 1.66, n 0.44, match 0.44, feed 0.33, frequency 0.22, loss 0.20, efficiency 0.10 dB; A4 drive spread 5.23 dB. Match the note within 0.01 dB.
- **Pads.** ABCD recomputation of the eight select-on-test pads and the three design pads: losses as tabulated, return loss 25.8 dB or more, design pads 18.42, 3.00 and 11.97 dB.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a reported result)

| Note section 3 row | Source read by the reviewer | Agreement |
|---|---|---|
| Si5351 ZO 50 ohm; edge 1 / 1.5 ns at CL 5 pF; duty 45 to 55 % below 160 MHz | Rev. 1.3 Table 4 "Output Impedance ZO ... 50" (3.3 V VDDO, default high drive); Table 7 rows as quoted | Yes; Table 7 also gives CL maximum 15 pF, not respected (finding-1) |
| GVA-84+ gain 22.9 / 24.1 / 25.3 dB; P1dB +19.4 min, +20.4 typ; Psat +21.7 at 3 dB compression; input +13 dBm maximum | Rev. F electrical specifications at 0.1 GHz and absolute maximum ratings | Yes (finding-8 on the frequency) |
| RA07M1317M: 6.5 W minimum at 7.2 V, VGG 3.5 V, Pin 20 mW; efficiency 45 % minimum at 6 W; Pin 30 mW, Pout 10 W at VGG 3.5 V or less, stability conditions, input VSWR 4:1 | Datasheet page 2 | Yes |
| RA07M1317M curves (Pout versus Pin, VDD, VGG at 135 and 155 MHz) | Pages 3 to 5 rendered; overlays opened; spot values: VDD curve 155 MHz 5.85 W at 6.0 V and about 8.2 W at 7.2 V; VGG curve 135 MHz 7.2 W at 3.0 V and 8.6 W at 3.5 V; Pin curve 39.38 dBm at 13 dBm (135 MHz) | Yes; the note's correction of TS-012 (5.85 W, not 5.3 W, at 6.0 V) is right. TS-012 section 7.3's "4 W at 3.0 V, 7 W at 3.5 V" on the VGG graph does not match the page (X-2) |
| RA07M1317M efficiency 0.60 typical | Page 4: about 1.63 A at 6.0 V, 155 MHz | Yes (graph read, estimate) |
| AFT05MS004N Figure 13 and Table 8 | Datasheet: Table 8 6.0 W at 135 MHz, Pin 0.10 W (62.3 %); 6.0 W at 155 MHz, Pin 0.06 W (69.1 %); Table 9 0.2 W at 155 MHz, 9.0 V; no Pin rating in Table 1. Overlay: the blue-dotted track is the 135 MHz curve (gain check at 0.03 W) | Yes; the 155 MHz track reads 6.32 W at 0.06 W against Table 8's 6.0 W (+0.2 dB, within a typical-curve read) |
| Drain feed 0.26 / 0.35 / 0.45 ohm; LPF 0.4 dB plus relay 0.1 dB; bus 0.2 A in TS-012 | TS-012 section 7.3 | Yes; 0.25 A bus is conservative |
| VGG clamp 3.08 V | TS-012 section 7.3: 4.75 x 0.6493 = 3.08 V, maximum 3.46 V | Yes for the low end; the 3.5 V level is above the clamp (finding-3) |
| REQ-SYS-012 bounds 3.972 and 6.295 W | requirements.json; 5 x 10^(-0.1) = 3.9716 W | Yes; the checker's 3.972 W rounds toward the stricter side |
| Stability window 10 to 30 mW | Datasheet: stability tested at Pin 10, 20 and 30 mW | Yes (a reasonable reading of three test points as a window) |

## Checklist answers

### A. Question, scope and traceable inputs

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | No | REQ-SYS-012, REQ-SYS-144, TS-012 criteria and WP-PDR-22 named and exist; REQ-SYS-114, TPM-015, TPM-004 and the hazards are not (finding-6, finding-2) |
| CK-ANA-A2 | No | TS-012 revision 4 cited by revision, not commit; no schematic exists yet, and the drive LPF values are "chosen here" (stated) (finding-6) |
| CK-ANA-A3 | Yes | Section 3 gives a source or "estimate" for every row |
| CK-ANA-A4 | Yes | Reviewer table above; disagreements listed (findings 1, 3, 8; X-2) |
| CK-ANA-A5 | No | Temperature assumption unstated (finding-2); VGG level and the drive and VGG interaction direction (finding-3) |
| CK-ANA-A6 | No | The CLK1 load and interface consequence is not sent to TS-012 (finding-1); the REQ-SYS-144 delta status (finding-4) |

### B. Model validity

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Simplifications listed in section 6, but the interconnect, temperature and the GVA-84+ departure from S-parameters are not (findings 1, 2, 8) |
| CK-ANA-B2 | No | No vendor SPICE model is used; the Si5351 source is built from Table 7 values specified at CL 5 pF, used at 23 pF against the 15 pF maximum (finding-1) |
| CK-ANA-B3 | Yes | d1 fits the GVA-84+ compression within 0.03 dB; digitized curves checked against Table 8 and the RA07M1317M frequency plot; overlays |
| CK-ANA-B4 | Yes | `.tran` 10 ps maximum step, 90 ns settling, `plotwinsize=0`; the reviewer's 2 ps / 200 ns variant moves nothing (above) |
| CK-ANA-B5 | Yes | Phasor and fixed-point re-solves agree within 0.02 dB and 0.02 W (above) |
| CK-ANA-B6 | No | Graph-read error and estimates listed, but the combined uncertainty is not set against the thin margins (0.07 dB overdrive, 0.35 dB closure, 0.41 dB select-on-test) (findings 1, 2, 4) |

### C. Tools, validation status and reproducibility

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | Log first line `LTspice 26.0.2 for MacOS` equals the lock; venv versions equal the note (Python 3.13.5, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2) |
| CK-ANA-C2 | Yes | LTspice accredited (TV-014, ACC-LTSPICE-001, wrapper blob `88b71475`); the Python checker has no TV record and the note marks the result developer evidence |
| CK-ANA-C3 | Yes | `run_pa.py all` reproduces every number; netlists, one analysis each |
| CK-ANA-C4 | Yes | Reviewer re-run identical (above) |
| CK-ANA-C5 | Yes | TV-014 limitations respected: short run directory, lock, no `.asc` runs, exit and log checks by the wrapper |

### D. Units, arithmetic and consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | mW, dBm, dBc, W and V consistent; dB conversions re-computed (for example 10 log(4.87 / 3.54) = 1.39 dB, the note's 1.4 dB) |
| CK-ANA-D2 | No | Numbers equal the checker output throughout; one sentence contradicts the table (finding-7) |
| CK-ANA-D3 | Yes | Limits rounded toward the stricter side (3.972 W); results given to the input precision |
| CK-ANA-D4 | Yes | `REQ012_LO`, `A5_PIN_MIN_MW`, `A5_PIN_MAX_MW`, `H3_MIN_DBC`, `GVA_ABSMAX_IN_DBM` with their source in the comment next to each |

### E. Results, margins, proposed values and credit

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | REQ-SYS-012, the TS-012 criterion and the datasheet limits quoted with their ids and sources |
| CK-ANA-E2 | No | Margins have the right sign; TPM-015 and TPM-004 thresholds not compared (finding-6) |
| CK-ANA-E3 | No | "Overdrive designed out" at +0.07 dB (finding-1); the (b) closure and the select-on-test pass at +0.35 and +0.41 dB without their uncertainty (findings 2, 4) |
| CK-ANA-E4 | No | Exit 0 on FAIL (finding-5) |
| CK-ANA-E5 | N/A | No TBR value proposed |
| CK-ANA-E6 | N/A | No TPM current best estimate proposed (the missing comparison is finding-6) |
| CK-ANA-E7 | Yes | Supporting pre-build evidence for a Test-method requirement (REQ-SYS-012), developer evidence; no credit claimed |

### F. Every case named

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Pack ends and band edges covered; the REQ-SYS-114 temperature extremes are missing (C-16, finding-2) |
| CK-ANA-F2 | Yes | Open-loop ALC at 8.4 V analysed (C-10); cell at end of discharge is the 6.4 V end |
| CK-ANA-F3 | Yes | Extreme-value corners with the worst combination named per result (result files "Lowest corner" lines) |
| CK-ANA-F4 | No | Sensitivity tables given for drive and power; the select-on-test pass is not shown against its reading uncertainty (finding-4) |

### G1. Simulation decks and checkers

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | Decks, checker and plots under `hardware/sim/tx-pa/`, run-id folders tie them |
| CK-ANA-G1-2 | Yes | Drive decks `.tran` only, power decks `.dc` only; the wrapper's `NC_` check passed |
| CK-ANA-G1-3 | No | The CLK1 interface is not the designed interface (finding-1); the 50 ohm PA inputs follow the datasheet ZG = ZL = 50 ohm definition (stated) |
| CK-ANA-G1-4 | Yes | The checker reads the `.raw` through spicelib; the replot path re-reads only when the deck SHA-256 equals the recorded one; the wrapper removes stale outputs |

### G5. Cascades

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G5-1 | Yes | Source, LPF with parasitics, tap, pads, GVA-84+ and PA input, each sourced (the missing interconnect is finding-1) |
| CK-ANA-G5-2 | Yes | Reviewer recomputed the cascade by a different method (B5) |
| CK-ANA-G5-3 | Yes | The only spurious criterion in scope, 3f at the GVA-84+ input, is evaluated at every corner; the other lines belong to WP-PDR-20 |

### G7. Worst-case and tolerance

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme-value corners, full factorial, stated in section 2 |
| CK-ANA-G7-2 | No | Initial tolerances used; temperature coefficients over REQ-SYS-114 not included (finding-2); ageing N/A |

### H. Hazards, risks and records

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | HZ-001 and HZ-003 not named; no request to the hazards writer (finding-6) |
| CK-ANA-H2 | No | Risk re-quantification not sent to the risk writer (finding-6) |
| CK-ANA-H3 | Yes | Change log revision 0 with its date |

### I. Visual closure

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | The reviewer opened all 9 cited plots, the p3 plot and the 7 digitizer overlays (17), and rendered and read RA07M1317M pages 3 to 5 |
| CK-ANA-I2 | No | Axes, units, limits with ids and legends present on all; the p3 plot title does not name its case (finding-7). Plotted values agree with the checker at the marked points (for example 29.5 mW top point, 3.71 W envelope floor at 6.4 V, 8 W crossing at 7.5 V) |

**ITEMS N/A:** CK-ANA-E5, CK-ANA-E6, CK-ANA-G2 to G4, CK-ANA-G6 (analysis_kind is simulation-deck, cascade and worst-case), CK-ANA-J1 to J3 (criticality neither).

## Cross items (returned to Claude as lead SE)

- **X-1. Output-loss allocation against the new LPF result.** `docs/design/analysis/lpf-ts012.md` (commit `6bff79c`, Draft, not reviewed) reports passband loss of the TS-012 LPF at median 0.76 dB and worst 1.21 dB with the BOM values, and worst 0.71 dB retuned. This note allocates 0.4 to 0.6 dB including the relay. Reviewer arithmetic (estimate): with the retuned worst 0.71 + 0.1 dB the (b) closure figure 4.31 W becomes about 4.11 W; with the BOM worst 1.21 + 0.1 dB about 3.66 W, under 3.97 W. The note's C6 anticipates this rerun; it belongs with the finding-2 fix.
- **X-2. TS-012 VGG graph read.** TS-012 section 7.3 "Drive gating" reads the RA07M1317M VGG graph as "about 0 W at 1.5 V, 2 W at 2.5 V, 4 W at 3.0 V, 7 W at 3.5 V". The datasheet page 5 (135 MHz) gives about 1.0 W at 2.5 V, 7.2 W at 3.0 V and 8.6 W at 3.5 V, consistent with its own text "nominal output power becomes available at 3V (typical)". The WP-PDR-22 envelope-loop deck should take the digitized curve, not the TS-012 figures. A request to the TS-012 author.
- **X-3. Section 4.7 margin wording.** "At least 1.0 V of margin" for the prescaler input is the total margin (0.5 V on each side with the bias midway), the same convention as INSP-110 O-5's 0.45 V. Not a finding; the WP-PDR-20 and prescaler designers should read it as a total.

## Commands

- Search: `mcp__claude-context__search_code` path `/Users/robinonsay/rust/cwht`, queries "PA drive window output power analysis TS-012 A4 A5 WP-PDR-21" and "INSP id register next free inspection id assigned".
- Freeze and blobs: Python loop over `git rev-parse b705428:<path>` and `git rev-parse HEAD:<path>` (43 files).
- Re-run: `git archive b705428 tools hardware/sim/tx-pa | tar -x -C <scratchpad>/exp`; author results moved to `results-author`; `cd <scratchpad>/exp && /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_pa.py all` (exit 0); JSON, Markdown, deck and PNG comparisons in Python.
- Tight-step check: `tools/ltspice-batch.sh -t 600 -o <scratchpad>/rv/b4 -b drive_a5_b4.cir` (PASS, exit 0, sha256 `ba314986`).
- Independent models: `<scratchpad>/rv/phasor.py`, `<scratchpad>/rv/power_check.py`, `<scratchpad>/rv/line.py` (scratchpad only, not committed).
- Datasheets: `pdftotext -layout` and `pdftoppm -r 110 -f 3 -l 5` on the cached PDFs, SHA-256 checked against the block README.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py --quiet` (this record not listed among the failures; the failures listed are pre-existing records).

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/pa-drive-ts012.md@ecffcb3f, hardware/sim/tx-pa/run_pa.py@acbe1457, decks and results as in product_files, at b705428
FINDINGS:
- [Major] CK-ANA-G1-3, B2, E3, A6 finding-1: CLK1 loaded with 23 pF (Si5351 CL maximum 15 pF) and the Si5351-to-LPF interconnect of TS-012 8.1 not modelled; 5 to 15 cm of line puts 1 to 18 A5 corners above 30 mW (reviewer estimate); "overdrive designed out" rests on a 0.07 dB margin.
- [Major] CK-ANA-F1, A5, G7-2, B6, E3 finding-2: REQ-SYS-114 (-10 to +45 C) not analysed or stated; the +0.35 dB closure margin of section 5 (b) is not set against its uncertainty.
- [Minor] CK-ANA-A5, B1 finding-3: VGG 3.5 V is above the revision-4 clamp (3.08 to 3.46 V); nominal and C3 figures at an unreachable VGG; interaction direction unstated.
- [Minor] CK-ANA-F4, E3, A6 finding-4: select-on-test band uses 1 dB steps (table has up to 1.38 dB), an unsourced +/-1 dB reading, and a Proposed REQ-SYS-144 delta.
- [Minor] CK-ANA-E4 finding-5: checker exits 0 on FAIL.
- [Minor] CK-ANA-A1, A2, E2, H1, H2 finding-6: TPM-015, TPM-004, REQ-SYS-114, HZ-001, HZ-003, risk requests and the TS-012 commit not named.
- [Minor] CK-ANA-D2, I2 finding-7: A4 "every corner below 6.8 V" wording; d2 result.md wording; p3 plot title.
- [Minor] CK-ANA-B1 finding-8: departure from the TS-012 GVA-84+ S-parameter method and its direction unstated.
ITEMS N/A: CK-ANA-E5, E6, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: none
MEASUREMENTS: size=6 decks, 3294 LTspice corners; inputs_checked=10 rows (every input that sets a reported result); renders=17; turns=70; minutes=95; major=2; minor=6
```
