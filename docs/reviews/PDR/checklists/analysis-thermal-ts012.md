---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-28 pre-order
# thermal note for the TS-012 finalists A4 and A5, iteration 1 at the freeze commit 0caa0cc (rule C2).
# X-1 (checklist field): the item set applied is docs/templates/peer-review-checklist-analysis.md revision A,
# blob 0386cc6e, on branch cr/CR-012-pdr-checklist-templates (CR-012 Approved 2026-09-28, merge held at the
# section 9 pre-merge check, a17af87). The template is not on main, and tools/validate_docs.py rejects a
# checklist field whose template is absent from docs/templates/, so the field names the design checklist, as
# INSP-056 did. The delta iteration after CR-012 merges switches the field to peer-review-checklist-analysis.
# id: INSP-112 is the next free id (highest on main and on the cr/ branches at 1ec9906 is INSP-111); the lead
# SE reassigns it if a parallel review took the same number.
# Filed by the lead SE on 2026-09-28 from the reviewer's own text: the harness refused the reviewer's Write of this
# new file ("Subagents should return findings as text"). Content is verbatim; this record keeps INSP-112, and the
# parallel spur and PA drive reviews that also chose INSP-112 are filed as INSP-113 and INSP-114.
# Iteration 2 (2026-09-28, delta on the INSP-112 fixes, rule C1): product re-frozen at 35fc7ee (note revision 1,
# run 2026-09-28-ts012-r2); HEAD equals 35fc7ee. X-1 still holds: CR-012 is not merged (branch head 7784672 is not
# an ancestor of main), so the checklist field still names the design checklist; checklist_analysis records the
# template actually applied, as INSP-083 does.
id: INSP-112
checklist: peer-review-checklist-design
checklist_revision: A
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-thermal-ts012.md
product: docs/design/analysis/thermal-ts012.md
# product_commit (iteration 2): 35fc7ee, note revision 1 with run 2026-09-28-ts012-r2. Every blob below equals
# git rev-parse 35fc7ee:<path> and HEAD:<path>; the scripts/ copies in the run directory equal the committed scripts
# (SHA-256 54b5ecf4...3e66e0 and 09cf75ef...b97ce0). product_files_iteration_1 keeps the 0caa0cc blobs.
product_commit: "35fc7ee58fb603e885f661b1f3e69b4d33e04c49"
product_files: ["docs/design/analysis/thermal-ts012.md@81592c3439e86125d836150ed2fec8747c477eb5", "hardware/sim/thermal/thermal_model.py@54573514ad75cbae6edee930996f5fa5a745eed6", "hardware/sim/thermal/ts012_thermal.py@3eb26aaace15c59002c9820d26b36461e1760105", "hardware/sim/thermal/README.md@b06cdbf5ce81894f5262f15227dede8449a1545e", "hardware/sim/thermal/results/2026-09-28-ts012-r2/bands.csv@e381a8aa3f807fe4f4d68a0d28f186d53ef0ed40", "hardware/sim/thermal/results/2026-09-28-ts012-r2/check-stdout.txt@281fb8bd590612e470bca67e97719d1d42d121af", "hardware/sim/thermal/results/2026-09-28-ts012-r2/duty_sweep.csv@5fc41842ab8070ab8722101ffa1a04e447ff5cdf", "hardware/sim/thermal/results/2026-09-28-ts012-r2/inhibit.csv@0e3210da6a4820d8d67ddc4d31ad6db2a8e23cf7", "hardware/sim/thermal/results/2026-09-28-ts012-r2/inhibit_bound.png@e164278845705c332437dab937d041deaa49ac3d", "hardware/sim/thermal/results/2026-09-28-ts012-r2/inputs.csv@5f51608eb1fb45774da344739df641d4f249ff18", "hardware/sim/thermal/results/2026-09-28-ts012-r2/levers.csv@4745e9215be36339e757e0f4d000bd61f56ef615", "hardware/sim/thermal/results/2026-09-28-ts012-r2/ltspice/ltspice-batch.stderr.txt@d1eaf270ba02a63468d0297ca20fe0c683eccff1", "hardware/sim/thermal/results/2026-09-28-ts012-r2/ltspice/thermal_a5dc.log@0f7119b459776917b14e8bb0ed32ac2c337c4e60", "hardware/sim/thermal/results/2026-09-28-ts012-r2/ltspice/thermal_a5dc.net@e95654f30a2c9d6b355ae80f559ab53cd5994281", "hardware/sim/thermal/results/2026-09-28-ts012-r2/ltspice_crosscheck.png@67b90d274b80620b6afa73ca0a4428bcd3a1eebc", "hardware/sim/thermal/results/2026-09-28-ts012-r2/margins_vs_band.png@8bbbd527ea21f6f527cf45ffe2b9d9e2dfa968e4", "hardware/sim/thermal/results/2026-09-28-ts012-r2/network_a5dc.png@530e7080085db881a5b9da1cca30af6137883227", "hardware/sim/thermal/results/2026-09-28-ts012-r2/petg_and_cells_45C.png@e11ef3c18acfc83b34a740cc1086635d8255d7aa", "hardware/sim/thermal/results/2026-09-28-ts012-r2/run-stdout.txt@281fb8bd590612e470bca67e97719d1d42d121af", "hardware/sim/thermal/results/2026-09-28-ts012-r2/sink_catalog_curve.png@e49cfa808fcf103f464c3e4182e8bd09d6e17e92", "hardware/sim/thermal/results/2026-09-28-ts012-r2/summary.csv@33b9ee3ab4294a141008a8cf5d653db319706d9b", "hardware/sim/thermal/results/2026-09-28-ts012-r2/surfaces_25C_5min.png@fa017cc40fe15fdd4843a50667f7edb6b3c6de74", "hardware/sim/thermal/results/2026-09-28-ts012-r2/tj_vs_duty.png@6837f9b4bc334a1ac81415ae27aded07726d1481", "hardware/sim/thermal/results/2026-09-28-ts012-r2/tj_vs_time_45C.png@37d978ccacb739ab15573a45cf9ed47ac9b27d27", "hardware/sim/thermal/results/2026-09-28-ts012-r2/tornado.csv@6315b2231debf82d3d7b8c7575a9db6a1a41c24c", "hardware/sim/thermal/results/2026-09-28-ts012-r2/tornado.png@0e0ceb1a7013bab25b39bd204cfe55b7c2d19528", "hardware/sim/thermal/results/2026-09-28-ts012-r2/trips.csv@168adde30d3c4ae65e1f4959c4492a0457555514", "hardware/sim/thermal/results/2026-09-28-ts012-r2/verdict_set.csv@3de569765fd26a3fb7ee436d5a6afdd8c988897e", "hardware/sim/thermal/results/2026-09-28-ts012-r2/verdicts.md@63b15a1095686586531df206ff2ad1fb5df7b3ec"]
product_files_iteration_1: ["docs/design/analysis/thermal-ts012.md@9ea3374f0f758676b25d3e300b70225c9d33af16", "hardware/sim/thermal/thermal_model.py@a7a8693c8ca5a18461f4be550f02bc20a2aa0f1c", "hardware/sim/thermal/ts012_thermal.py@0c24b94a0be2b82caf7f12e9f42c2acaaf051a22", "hardware/sim/thermal/README.md@64490d801b6f39206b26f00ece5a29b685ee0af8", "hardware/sim/thermal/results/2026-09-28-ts012-r1/verdicts.md@ae9fd6f040c3a684486a64f4284274a976b5799e", "hardware/sim/thermal/results/2026-09-28-ts012-r1/summary.csv@3d6bec29de36411dd75312011c43e9ab8b8c9ae7", "hardware/sim/thermal/results/2026-09-28-ts012-r1/inputs.csv@9a6fac4130c1d6ff30862f21e106ebffebae0dd4", "hardware/sim/thermal/results/2026-09-28-ts012-r1/duty_sweep.csv@7a87aa03e7cfd5d73ae15a4556ad9f540fb8c40d", "hardware/sim/thermal/results/2026-09-28-ts012-r1/tornado.csv@1963a4212403103b4f3fda02769d5b86f0254c71", "hardware/sim/thermal/results/2026-09-28-ts012-r1/ltspice/thermal_a5dc.net@981274a25b4937f733d01a0c48cc01de6c88dd9b", "hardware/sim/thermal/results/2026-09-28-ts012-r1/ltspice/thermal_a5dc.log@0d5e77eeb54c93876c1711e6ae0241f6e71bd712", "hardware/sim/thermal/results/2026-09-28-ts012-r1/tj_vs_time_45C.png@38ee4154a26a15115cfbd75ab7cbb677d1678bbd", "hardware/sim/thermal/results/2026-09-28-ts012-r1/tj_vs_duty.png@003529d53f11022a0b6eb33a08e2c2c09c68a088", "hardware/sim/thermal/results/2026-09-28-ts012-r1/surfaces_25C_5min.png@2d79b6e18fa0952838857625b01f21625b6a10ef", "hardware/sim/thermal/results/2026-09-28-ts012-r1/petg_and_cells_45C.png@15bad0994e8a9806114f23fdfd035acef28e1ca7", "hardware/sim/thermal/results/2026-09-28-ts012-r1/tornado.png@e7b0b9fbfd0d7c0a4f528983385539e0a03e44ff", "hardware/sim/thermal/results/2026-09-28-ts012-r1/sink_catalog_curve.png@e49cfa808fcf103f464c3e4182e8bd09d6e17e92", "hardware/sim/thermal/results/2026-09-28-ts012-r1/network_a5dc.png@77bd9d6705d04ec5b2ab7e6c0562b1609d6c542f", "hardware/sim/thermal/results/2026-09-28-ts012-r1/ltspice_crosscheck.png@178cad87501d427fffc55a766b2e5715c8b46999"]
analysis_kind: [thermal, simulation-deck, worst-case]
product_size: 1 note (516 lines, revision 1), 4 layouts x 22 verdict criteria (V01 to V22, 82 cells), 112 classed inputs (86 swept) plus 10 curve points, 1 LTspice deck, 2 scripts, 10 plots
tools_used: ["LTspice 26.0.2 through tools/ltspice-batch.sh blob 88b71475 (TV-014, accredited ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter)", "numpy 2.5.3, matplotlib 3.11.2, spicelib 1.6.3 with scipy 1.18.1 as its dependency (lock section 2, class B, no TV record: developer evidence per 05 section 9.1)"]
# values_proposed (iteration 2): what note revision 1 section 9.2 and section 8 change 6 put to the owner or to the
# SW requirements writer (R-5). Supported as proposals once this record is APPROVED (rule C10); the owner rules the
# values. The S values carry finding-16 item (e) (rounded up by 0.04 K; round down)
values_proposed: ["REQ-SYS-112: delta by CR to a duty-limited corner (for example at most 110 C at 50 % key-down duty in 13 s key-downs at 45 C) or a 25 C continuous corner (A5-DC 106.1 C, A4-DC 102.8 C nominal, no band)", "REQ-SYS-118: NTC on the PA case in the heat path, threshold about 81 C (A5) or 77 C (A4) at the NTC (sensor adverse, +3 C tolerance), final value after the bench offset measurement; 100 ms kept; or a sink-NTC duty limit programmed at S = 79.4 C (A5), 67.2 C (A4)", "REQ-SYS-113: 48 C confirmed met with the wrap guard (A5-DC 32.3 C, A4-DC 29.5 C at 5 min, bands within 48 C)", "REQ-SYS-181: confirmation deferred (request R-3, sensor location)"]
renders_inspected: 10
sprint: PDR-prep
author_agent: "author:WP-PDR-28 TS-012 pre-order thermal item (Claude as analysis author, commit 0caa0cc; revision 1 at 35fc7ee)"
reviewer_agent: "reviewer:WP-PDR-28-thermal-ts012-iter1 (independent; authored no part of the note, the model, the runner, TS-012 or the design data analysed); iteration 2 by reviewer:WP-PDR-28-thermal-ts012-iter2 (independent; authored no part of the note, its revision 1, the model, the runner, TS-012 or the design data analysed)"
# criticality: the note proposes the REQ-SYS-118 sensor location and setpoints and a firmware duty limit that the
# SW-SAFE thermal unit implements (07 section 14.1 row "Thermal protection", HZ-003 criteria b and e,
# safety-critical); section J is answered here
criticality: safety-critical
# assurance_required: a stand-alone analysis note is not a row of 07 section 2.1.1, and no sw-<sub> token is in
# the product path or the slug (template front matter rule)
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
# reviewer_verdict (iteration 2): APPROVED (rule C1). finding-1 to finding-4 (Major) and finding-5 to finding-14
# (Minor) are Verified at 35fc7ee. The new finding-15 to finding-17 are Minor and Open: liens due at the CDR
# readiness declaration (plan rule C1), owner Claude as the WP-PDR-28 analysis author.
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES. The applied analysis template is still only on cr/CR-012 (blob 0386cc6e, branch
# head 7784672, not merged at 35fc7ee), so, per the lead SE convention of 2026-09-27 (INSP-083), the lead SE sets
# the record verdict to APPROVED in the CR-012 merge commit (or the commit right after it) if that blob and the
# product blobs are unchanged
verdict: NEEDS CHANGES
findings_major: 4
findings_minor: 13
findings_open: 3
findings_fixed: 0
findings_verified: 14
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 6]
deferred_rids: []
# items_no (iteration 2): the items that stay No on the open Minor liens finding-15 to finding-17
items_no: [CK-ANA-B6, CK-ANA-D2, CK-ANA-D3, CK-ANA-E1, CK-ANA-F4]
items_no_iteration_1: [CK-ANA-A3, CK-ANA-A4, CK-ANA-B2, CK-ANA-B6, CK-ANA-C1, CK-ANA-C3, CK-ANA-D2, CK-ANA-D3, CK-ANA-E1, CK-ANA-E3, CK-ANA-E4, CK-ANA-E5, CK-ANA-F2, CK-ANA-F4, CK-ANA-G3-2, CK-ANA-H1, CK-ANA-H2, CK-ANA-I2, CK-ANA-J2]
# effort: cumulative (iteration 1: 45 turns, 75 minutes; iteration 2: 45 turns, 80 minutes)
effort_turns: 90
effort_minutes: 155
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record INSP-112: PA, heat sink and PETG case thermal model for the TS-012 finalists (iteration 1)

**Product:** `docs/design/analysis/thermal-ts012.md` (blob `9ea3374f`) with the model `hardware/sim/thermal/thermal_model.py` (`a7a8693c`), the runner `ts012_thermal.py` (`0c24b94a`), the block README, the run `hardware/sim/thermal/results/2026-09-28-ts012-r1/` (results file, CSVs, LTspice deck and log) and its eight plots, at the freeze commit `0caa0cc` (rule C2). `main` moved to `1ec9906` during the review (`b705428` WP-PDR-21 PA run, `1ec9906` INSP-075); `git diff --stat 0caa0cc 1ec9906 -- docs/design/analysis/thermal-ts012.md hardware/sim/thermal` is empty, so every product blob is unchanged at `HEAD`. The script copies in `results/.../scripts/` equal the committed scripts byte for byte (SHA-256 `a5843f9a...69cac` and `7f576ee8...ce96cf`, as the README states).

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch blob `0386cc6e`; front matter X-1). `analysis_kind` thermal, simulation-deck (the LTspice analogue) and worst-case (input stacks): sections A to F, G1, G3, G7, H, I, and J (criticality safety-critical).

**Acceptance criteria (rule C7, every case the governing clauses enumerate):**
- REQ-SYS-112: continuous key-down at the 5 W step, 45 C ambient, junction at most 110 C (TBR); for A5 both channels.
- REQ-SYS-113: hand-hold surfaces at most 48 C after 5 min of continuous key-down at 5 W in 25 C (TBR); WP-PDR-28 reads it as "every reachable surface".
- TS-012 revision 4 section 7.3 pre-order criteria: stage-2 channel at most 110 C and case at most 90 C at the corner; every PETG surface within 5 mm of the sink at most 60 C at the 45 C corner; guard outer surface at most 48 C at 25 C, 5 min; (a) 50 % duty for 30 min at 45 C, cell surface and main-bay air at most 55 C; (b) at the continuous corner no cell above 60 C before the cell trip operates; (c) every PETG surface, bay walls and bulkhead included, at most 60 C.
- REQ-SYS-118 (85 C +/-3 C inhibit) and REQ-SYS-181 (95 C +/-3 C sink cut-off): the relation of each trip to the junction and the cells.
- HZ-003 K7 (thermal budget: 50 % duty and a 5 min continuous worst case), K8 and K10 (13 s and 180 s bounds), and HZ-007 C5 (PA heat conducted to the cells).

**Independence (rule C4):** this invocation authored no part of the note, the model, the runner, TS-012 or the data analysed, and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: analysis checklist template and rule C1; PDR work plan rule C1; TS-012 section 7.3 thermal pass criteria). `grep -n` and `sed -n` afterwards only pinned lines in known files. **Sources read on the web (2026-09-28, public pages, no login):** the Mitsubishi RA07M1317M datasheet (Jun 2019, https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/ra07m1317m.pdf, pages 1, 2, 6 and 8) and the Boyd Board Level Cooling Catalog (https://info.boydcorp.com/hubfs/Thermal/Air-Cooling/Boyd-Board-Level-Heatsinks-Catalog.pdf, the index page and catalog page 56), both through the web-fetch tool, which cached the PDFs; the reviewer rendered the pages with `pdftoppm` and opened them.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-D2, D3, E3, F4 | note section 4.3 row "Cells, long session at the duty limit" (A4-DC "55 C"), section 5 rows "Cells and main bay" and "Reading", section 7 residual table (A4 "none"); `verdicts.md` row "Duty-limited corner: cells, steady" | (1) The note disagrees with its own results file. `verdicts.md` gives the A4-DC long-session cells as 55.2 C FAIL against 55 C (summary.csv `dl_cell` 55.171); the note rounds it to "55 C", reports A4 "PASS with the design changes ... long session 55 C", says "every case, surface and cell criterion passes" for A4, and lists no A4 residual. The rounding goes away from the limit. (2) The note separates the finalists on margins far inside the model's own spread. A5 "misses by 0.1 to 0.4 K" (PETG 60.1 C, main-bay air 55.4 C) while A4 "passes" at +0.4 K (PETG 59.6 C continuous) and +1.5 K (main-bay air 53.5 C). The reviewer ran the note's own tornado on the cases the note did not tornado: A4-DC hottest PETG 59.6 C spans -3.1 to +10.0 K (RSS 4.3 K), A4-DC cells at 50 % 54.4 C span -4.7 to +8.2 K (RSS 3.1 K); A5-DC PETG RSS 6.5 K, A5-DC cells RSS 4.3 K; finding-2 adds 1 to 2.6 K more. No margin in (2) exceeds its uncertainty, the note does not say so, and the "Reading" row turns the difference into a verdict (A4 clean, A5 marginal) that feeds the TS-012 revision. Fix: report A4-DC long-session cells as over 55 C by 0.2 K; for every PETG, cell, main-bay and relay case whose margin is inside its band, write "not shown" with the band (tornado and stacks for A4-DC too); restate the reading on the physical difference (A5 puts about twice the heat in the case) rather than on sub-kelvin pass and fail | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A3, A4, B6, G3-2 | `thermal_model.py` `build()`: `h_gc = 5.0`, `v_g = 0.45`, radiation splits `(0.3, 0.4, 0.3)`, `(0.3, 0.0, 0.7)`, `0.3`, `0.2`, `0.5`; `g_gap_face`; `g_gapc = 3.0 * a_ew * 0.5`; areas `a_guard`, `a_ef`, `a_bw`, `a_bh`, `a_mw = 262.0e-4`; capacities `J2 0.2`, `J1 0.1`, `CASE 3.0` (A5) and `1.0` (A4), `J 0.05`, `BAY 25.0`, `MAIN 60.0`; `CASE`-bay `0.003`; vent `Cd 0.6`, heights `0.035` and `0.03`, `rho 1.1`; note header "every input is classed in inputs.csv" and section 2 case 7 "a one-at-a-time tornado over every D, DD and E input" | About 30 values in the network builder are inputs with no class, no source in `inputs.csv`, no range and no tornado row, although the note says every input is tagged and swept. Several set reported results. Reviewer sensitivity (source edited in a scratch copy, same solver): main-case wall area `a_mw` +/-20 % moves the A5-DC criterion (a) main-bay air by +1.45/-1.15 K and the A5-DC duty-limited cells by +1.7/-1.3 K (A4-DC +1.2/-1.0 and +1.4/-1.0 K); grille intercept `v_g` 0.30 to 0.60 moves the A5-DC guard PETG by -1.1 to +2.6 K; vent discharge coefficient 0.4 moves the PETG maxima by +1.7 to +1.9 K; MAIN heat capacity 30 to 120 J/K moves the (a) main-bay air by +0.3 to -0.9 K. Each exceeds the 0.1 to 0.4 K margins the verdicts rest on. Fix: move every such constant into `P` with its class (geometry values as DD from TS-012 section 8.5 or E), source and range; include them in the tornado and the stacks; report the result bands | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-E4, D2 | `ts012_thermal.py` `main()`; README "Run"; note header "Model and checker" | The runner asserts nothing and exits 0 whatever the results (reviewer re-run: exit 0). The PASS and FAIL words in `verdicts.md` are computed, but the verdicts in the note and the README are transcribed by hand, and finding-1 shows one transcription disagreeing with the results file. 08 section 3.4 asks for an automated checker that asserts the acceptance value. For a screen where failures are expected results, the shape other records accepted (INSP for the shielding estimate) is a check mode that asserts the stated verdict set and the headline numbers and exits 1 on any difference. Fix: add `--check` that asserts every verdict the note states (per layout and criterion) and the key values within a stated tolerance, name the command in the note, and record its exit status | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Major | CK-ANA-E3, B6; HZ-003 C4 | note section 4.1 "Junction bound by an inhibit", section 5 A5 column "from datasheet values" and "Reading" ("bounded more robustly by the inhibit"), section 7 change 6; `ts012_thermal.py` `duty_limit()` (`tj_inh_*`) | The inhibit bound assumes the NTC reads the temperature to which Rth(ch-case) is referred, with no lag. Neither holds at the proposed locations, and the note carries no term for either. (a) A5: the RA07M1317M outline (page 6) puts the 19.2 mm contact face under the body; the slotted ears at 26.6 mm lie outside it, and the screw that would hold the NTC passes through the 1.57 mm web to a nut, so it is thermally tied to the sink. An NTC under that screw reads between the flange and the sink, which differ by the 0.5 K/W interface (about 5 K at 9.94 W) (reviewer reading of the outline and estimate). (b) A4: the tab-pad NTC sits across `a4_r_pad` 0.5 to 1.5 K/W from the tab, 2.8 to 8.3 K at 5.55 W. (c) Lag: from S the A5 case rises at about 9.94 W / 54 J/K = 0.18 K/s, so each second of sensor time constant is about 0.2 K of overshoot. The A5 bound at the +3 C tolerance has 1.7 K of margin, which (a) and (c) can consume; HZ-003 cause C4 is "sensor reading cold". The note presents this as the more robust of the two bounds and uses it to rank the finalists. Fix: add a sensor offset and lag term (estimate with range) to the bound and to S, recompute the setpoints, name the bench measurement that closes the offset (NTC reading against a thermocouple on the case at a known dissipation), and state the margin as not shown where it is inside the band | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-H1, H2, F2 | whole note (no HZ or RSK id appears); section 8 | The note bounds HZ-003 and HZ-007 controls and proposes changes to HZ-003 K2 (sensor location and setpoint) but names no hazard or risk id and routes no request to the `hazards.json` writer or to WP-PDR-18 (RSK-006, RSK-007, RSK-026). Hazard-named cases are not reported: HZ-003 K7 "5 minute continuous worst case", K8 (13 s) and K10 (180 s). Reviewer values from the model (45 C soak, continuous): junction at 300 s A5-R4 110.5 C, A5-DC 107.8 C, A4-R4 108.3 C, A4-DC 107.0 C; at 180 s 96.3 to 100.0 C; at 40 C ambient (the HZ-003 K1 figure, against REQ-SYS-112's 45 C) 102.0 to 105.6 C at 300 s. HZ-003 causes C1 and C5 (pocket, sun, hand over the guard, radio flat on a table blocking the bottom slots) are neither analysed nor listed as not analysed. Fix: name the ids, add the K7, K8 and K10 cases, list the unanalysed postures, and send the requests (including the K1 40 C against 45 C mismatch) | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-D2 | note section 4.3 paragraph after the table ("For A4 as revision 4 drew it, the cell trip (38 min) is what ends ... for A5 the 95 C sink trip acts first (7 to 9 min)") | With REQ-SYS-118 on the sink NTC as the model places it, the 85 C firmware inhibit acts first: sink at 85 C at 4.9 min (A5-R4) and 5.5 min (A5-DC), when the junction is 110.0 and 110.1 C, and at 11.7 min for A4-R4, when the A4 junction is already 123.0 C (reviewer re-run, 1 s steps). The paragraph names the wrong protection and hides that the 85 C sink inhibit leaves the A4 junction unprotected (the note's own S = 70 C for A4 says so). Fix the paragraph | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-E1, A5 | note section 1 bullet 5 and section 5 row REQ-SYS-113 ("every accessible surface"); section 2 case 3 and `ts012_thermal.py` `ON_S` ("10 s is the longest key-down the REQ-SYS-055 cutoff allows"); section 4.1 line 150 ("passes 110 C") | REQ-SYS-113 reads "hand-hold surfaces"; "every reachable surface" is the WP-PDR-28 reading and "the guard's outer surface" the TS-012 criterion; quote the requirement and name the set used. REQ-SYS-055 ends RF "7.5 s to 13 s (TBR) ... 10 s nominal", so 13 s is the longest key-down (the setpoint calculation uses 13 s correctly). Reviewer re-run with 13 s key-downs: peaks change by less than 0.1 K and no largest duty changes, so no result moves. "Continuous key-down at 45 C passes 110 C" reads as a pass; write "exceeds" | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-C3, D2 | note section 4.1 "Levers tried" and section 7 "Two further no-cost levers" | Six numbers do not come from the committed command. Reviewer re-run of two of them: guard effectiveness 0.95 gives 124.7 C (A5-DC) and 121.4 C (A4-DC), not 124.4 and 121.0 C; extrusion vertical (`k_orient` 1.0) reproduces 116.5 and 114.5 C. "Removing the guard" (123.3, 120.0 C) and the DMP3099L move ("-1.5 K main-bay air and +3 K bay air", "in the author's check before the final run") cannot be reproduced. Fix: add the lever cases to the runner and quote its output, or drop the numbers | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-C1 | note header "Evidence status" ("numpy, scipy and matplotlib") | spicelib 1.6.3 reads the LTspice `.raw` and so produces every LTspice cross-check number, but is not named; scipy is not imported by the model or the runner (it enters only as a spicelib dependency). Name every tool with its lock version | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-ANA-B2 | `thermal_model.py` `g_cat()` (`np.interp` clamps above `CAT_DT_K[-1]` = 59.0 K); `tj_vs_duty.png` A5-R4 kink at 75 to 85 % | The catalog curve ends at 59 K rise (19.8 W). A5-R4 continuous runs at 71.9 K rise, and A5-R4 above about 75 % duty passes 59 K; there the conductance is held at the last point. Natural-convection conductance rises with rise, so the clamp is conservative, and A5-R4 fails either way, but the note does not state that a reported case lies outside the curve. Also cite the catalog's own definition, which reconciles the 2.6 K/W figure directly: the index footnote "n = Natural convection thermal resistance based on a 75 C heat sink temperature rise" (catalog index page; the 530002B02500G row reads 2.6, V, page 56) | Open | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | CK-ANA-B6, E3 | note section 4.2 A4 rows and section 5 last bullet ("The TS-012 statement that A4's surfaces hold without a guard is withdrawn") | The A4 fin-tip values (50.4 C as revision 4 drew it, bare sink 49.1 C with the changes) are 1.1 to 2.4 K over 48 C on an isothermal sink node. At 5 min the sink is still heat-capacity dominated, so the sink mass range (52 to 62 g, class DD) and the fin-tip-to-base drop (not modelled) each move it by about that much. The finding that A4 needs the wrap guard stands as a design choice, but "withdrawn" overstates it: state "not shown to hold" with the band | Open | Pending | |
| <a id="finding-12"></a>finding-12 | reviewer | Minor | CK-ANA-E5 | note sections 7 change 6 and 8 items 1 and 6; REQ-SYS-118 and REQ-SYS-181 `tbr.plan` | The note proposes values (REQ-SYS-112 corner delta; REQ-SYS-118 sensor location and setpoints) without naming them as TBR proposals with the `tbr.plan` step they execute, and says nothing on REQ-SYS-181, whose plan asks the PDR thermal analysis to confirm 95 C +/-3 C against the device rating. Reviewer arithmetic for the note to state or defer: at the 98 C sink trip edge A5-DC has the channel at about 98 + 9.94 x 0.50 + 8.44 x 2.4 = 123 C and the case at about 103 C, under the 175 C channel rating and the 110 C Tcase(OP) maximum (datasheet pages 2 and 8) and over the 90 C guidance. State for each of REQ-SYS-112, 113, 118 and 181 whether the note proposes, confirms or defers, and fill `values_proposed` in the note's return | Open | Pending | |
| <a id="finding-13"></a>finding-13 | reviewer | Minor | CK-ANA-A5 | note section 8 item 2 ("The owner's Fluke meter can do this only if it has a temperature function ... If it has none, a K-type bead probe is an equipment-cap item") | Stale against the status note of 2026-09-28 section 2 (commit `02e3474`, before the freeze): the meter is a Fluke 174, it has no temperature input, and the thermal measurements use a stand-alone K-type thermocouple thermometer with a bead probe, inside the USD 300 cap, with its own TV record and known-answer check before credited use. A bead probe alone reads nothing. Cite the status note | Open | Pending | |
| <a id="finding-14"></a>finding-14 | reviewer | Minor | CK-ANA-I2 | `network_a5dc.png`; README ("every line to AMB ends at the AMB box") | The MW to AMB line (3.7 K/W) is drawn straight through the BH1 box, so the figure reads as a BH1 to MW link that the network does not have. Route the line around the box or move BH1 | Open | Pending | |

Four Major findings are open, so the reviewer verdict is NEEDS CHANGES (rule C1). Under rule C10 neither value in `values_proposed` goes to the owner until this record is APPROVED. What the review supports: the datasheet reads (Boyd profile, curve and mass order; RA07M1317M outline and thermal data; interface resistance), the headline junction results and the conclusion that neither finalist meets REQ-SYS-112 as written at 45 C, and the need for a wrapping guard for A5. The comparison of A4 and A5 on the PETG, cell, main-bay and inhibit criteria is not yet supported (findings 1, 2 and 4).

## Per-case results

Values are the model's (all estimates). "Re-run" means the reviewer's run of the runner at `0caa0cc` in a scratch export, which reproduced every CSV byte for byte.

| Case | Condition | Governing id and limit | Result (checker output) A5-R4 / A5-DC / A4-R4 / A4-DC | Margin with sign (limit minus result) | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Continuous key-down, 45 C, 8.4 V pack, 5 W at the SMA, steady | REQ-SYS-112: 110 C | 142.1 / 125.9 / 130.9 / 122.6 C | -32.1 / -15.9 / -20.9 / -12.6 K | input stacks 97 to 174 C (A5-DC), 92 to 174 C (A4-DC) | re-run: same; hand: A5 dissipation 7.888 x 1.970 - 5.6 = 9.94 W, A4 8.039 x 1.387 - 5.6 = 5.55 W | none |
| C-1b | A5 stage-1 channel, same corner | REQ-SYS-112: 110 C | J1 112.4 C (A5-DC) | -2.4 K | as C-1 | re-run (network plot); J1 is always under J2 (case + 1.5 x 4.5 against case + 8.44 x 2.4) | none |
| C-2 | Module case (A5), continuous | TS-012 7.3 and datasheet p.8: 90 C guidance | 121.8 / 105.7 C | -31.8 / -15.7 K | as C-1 | re-run: same | none |
| C-3 | Periodic 10 s key-downs at 50 %, 45 C | TS-012 duty-limited corner: 110 C | 114.4 / 104.2 / 111.5 / 105.2 C | -4.4 / +5.8 / -1.5 / +4.8 K | tornado not run at 50 % | re-run: same; dt 0.05 s and 150 cycles move it at most 0.06 K; 13 s key-downs under 0.1 K | finding-7 |
| C-4 | Largest duty holding 110 C | note section 4.1 | 40 / 60 / 45 / 60 % | A5-DC at 60 %: +0.4 K; A4-DC +1.1 K | as C-3 | re-run: same with 10 s and 13 s key-downs | none |
| C-5 | Inhibit bound, sensor on the PA case, +3 C tolerance | REQ-SYS-118 with REQ-SYS-112: 110 C | 108.3 (A5) / 112.4 (A4) C | +1.7 / -2.4 K | sensor offset and lag not carried | hand: 85 + 3 + 8.44 x 2.4 = 108.3; 85 + 3 + 5.55 x 4.4 = 112.4 | finding-4 |
| C-6 | Sink duty-limit setpoint S (13 s key-down from S) | REQ-SYS-118 proposal | 82.4 (A5) / 70.2 (A4) C | n/a | sensor offset not carried | hand: 110 - 20.26 - 9.94 x 0.503 - 9.94 x 13 / 54.1 = 82.35 C | finding-4, finding-12 |
| C-7 | 25 C soak, continuous, 5 min, hottest reachable surface | REQ-SYS-113: 48 C | 65.6 (fin tips) / 37.4 (guard) / 50.4 (fin tips) / 32.6 (guard) C | -17.6 / +10.6 / -2.4 / +15.4 K | sink mass 52 to 62 g; isothermal sink | re-run: same | finding-7, finding-11 |
| C-8 | Hottest PETG face, continuous, 45 C | TS-012 7.3 (c): 60 C | 92.3 BH1 / 66.0 guard / 68.3 EF / 59.6 BH1 C | -32.3 / -6.0 / -8.3 / +0.4 K | A4-DC RSS 4.3 K; A5-DC RSS 6.5 K (reviewer tornado) plus finding-2 terms | re-run: same | finding-1, finding-2 |
| C-9 | Hottest PETG face, duty-limited corner | TS-012 7.3 (c): 60 C | 70.7 / 60.1 / 58.6 / 56.5 C | -10.7 / -0.1 / +1.4 / +3.5 K | as C-8 | re-run: same | finding-1, finding-2 |
| C-10 | FR4 end wall (design change), continuous and duty-limited | note: 105 C (estimate) | 74.8 and 66.3 / 66.9 and 60.4 C (A5-DC / A4-DC) | +30.2 and +38.7 / +38.1 and +44.6 K | FR4 limit class E | re-run: same | none |
| C-11 | (a) 50 % duty, 30 min from a 45 C soak: cells | TS-012 7.3 (a): 55 C | 52.4 / 51.1 / 53.0 / 49.5 C | +2.6 / +3.9 / +2.0 / +5.5 K | cells RSS 3.1 to 4.3 K | re-run: same | finding-2 |
| C-12 | (a) same: main-bay air | TS-012 7.3 (a): 55 C | 59.3 / 55.4 / 62.3 / 53.5 C | -4.3 / -0.4 / -7.3 / +1.5 K | `a_mw` alone +/-1.2 to 1.5 K | re-run: same | finding-1, finding-2 |
| C-13 | Cells, steady at the duty-limited corner | note: 55 C, trip 60 C | 59.6 / 58.9 / 61.5 / 55.2 C | -4.6 / -3.9 / -6.5 / -0.2 K | as C-11 | re-run: same; note states A4-DC "55 C" | finding-1 |
| C-14 | (b) continuous from a 45 C soak: time to 60 C cells | TS-012 7.3 (b): trip operates first | 41.7 / 61.5 / 37.7 min / never (58.2 C) | holds by construction of the trip | n/a | re-run: same; the 85 C sink inhibit acts earlier (finding-6) | finding-6 |
| C-15 | PA-bay air, continuous and duty-limited | Omron G5V-2: 65 C | 88.8 and 69.8 / 67.1 and 61.4 / 73.3 and 63.5 / 61.0 and 57.2 C | -23.8 and -4.8 / -2.1 and +3.6 / -8.3 and +1.5 / +4.0 and +7.8 K | not swept | re-run: same | none |
| C-16 | Continuous, 45 C soak, junction at 300 s (not in the note) | HZ-003 K7: 5 min continuous; REQ-SYS-112 110 C | 110.5 / 107.8 / 108.3 / 107.0 C | -0.5 / +2.2 / +1.7 / +3.0 K | as C-1 | reviewer run, dt 0.1 s | finding-5 |
| C-17 | Continuous, 45 C soak, junction at 180 s (not in the note) | HZ-003 K10 (REQ-SYS-180 bound) | 97.3 / 96.3 / 100.0 / 99.4 C | +12.7 / +13.7 / +10.0 / +10.6 K | as C-1 | reviewer run | finding-5 |
| C-18 | Continuous at 25 C, steady | note (25 C corner option) | 122.9 / 106.1 / 111.9 / 102.8 C | -12.9 / +3.9 / -1.9 / +7.2 K | as C-1 | re-run: same | none |
| C-19 | LTspice analogue of A5-DC against the Python solver | note criterion 0.5 K | 0.017 K | +0.483 K | n/a | re-run through the wrapper: deck byte-identical (SHA-256 `b804c278...b4901`), exit 0, `.meas` J2 125.945 C, same 0.017 K | none |

## Readiness criteria

| # | Answer | Evidence |
|---|---|---|
| R1 | Yes | `git rev-parse 0caa0cc:<path>` gives every `product_files` blob; equal at `HEAD` `1ec9906` |
| R2 | Yes | `.venv/bin/python hardware/sim/thermal/ts012_thermal.py --run-id review-r1` in a `git archive 0caa0cc` export (with `tools/ltspice-batch.sh` blob `88b71475`): exit 0 in 36 s; wrapper result line "PASS deck=thermal_a5dc.net sha256=b804c278... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0"; the wrapper waited for another session's lock, then ran and ended the Wine session. The precondition and time-out guard are the wrapper's (TV-014) |
| R3 | N/A | No JSON product file |
| R4 | Yes, with gaps | The author summary and the note state the question, evidence status, inputs, results, limitations and the tools; the values proposed are not listed as such (finding-12) |
| R5 | Yes | No `TBD` in the note; the TBRs relied on (REQ-SYS-112, 113, 118, 181) are named |
| R6 | Yes | All eight cited renders exist in the run directory and were opened |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Section 1 names REQ-SYS-112, 113, the TS-012 7.3 criteria and the adversarial and INSP-110 items; each id exists. HZ and RSK ids are missing (finding-5) |
| CK-ANA-A2 | Yes | TS-012 revision 4 at `7d0d450`, the RA07M1317M and AFT05 datasheets, the Boyd drawing; AT RISK names TS-012 Proposed and the parallel WP-PDR-21 and 22 runs. `b705428` (WP-PDR-21) landed after the freeze; it computes no dissipation at 8.4 V, and its efficiency inputs (A5 0.45 minimum, 0.60 typical; A4 0.55 low, 0.67 typical) bracket the note's corner currents, so no input is contradicted |
| CK-ANA-A3 | No | About 30 builder constants have no source row (finding-2) |
| CK-ANA-A4 | No | Reviewer checks, all inputs that set a headline result: RA07M1317M total efficiency 45 % minimum at Pout 6 W (VGG control), 7.2 V (datasheet p.1 and p.2): matches; Rth(ch-case) 2.4 and 4.5 C/W, stage conditions (stage 1 IDD 0.40 A, 1.5 W out) and "keep the module case temperature (Tcase) below 90 C", 3.77 C/W for 60 C air (p.8): match; outline 30.0 x 10.0 mm, body 21.2 mm, height 5.4 mm, slots 26.6 mm, leads 6.0 mm at 2.3 mm above the base, contact face 19.2 mm long and 7.4 mm wide (p.6): match; Tcase(OP) -30 to +110 C and the 175 C channel rating: not used by the note (finding-12). Boyd page 56: 530002B02500G row A 63.50, B 18.29, C 3.17 mm; profile 41.91 x 25.40 mm, web 1.57 mm, channel 17.02 mm: match. Curve: the reviewer digitized the 5300 dashed curve at 900 dpi against its own grid (63.35 px/W, 7.51 px/K): 3 W 13.5 K, 5 W 21.4 K, 7 W 29.0 K, 11 W 41.1 K, 13 W 46.3 K, 15 W 51.1 K, 17 W 55.3 K, 19.8 W 59.2 K, against the model's 13.5, 21.6, 28.6, 41.2, 46.3, 51.2, 55.3, 59.0 K: within 0.4 K (the note's +/-1 K reading holds). 3.81 K/W at 9.94 W and 4.18 K/W at 6.05 W recomputed. Interface 50 um / (0.70 x 1.42 cm2) = 0.503 K/W. AFT05 4.4 C/W and the reference-circuit figures: taken from `docs/research/pa-device-candidates.md` F10 as cited, not re-read. PETG HDT 69 C: labelled typical, filament TDS unread (stated). The builder constants are unchecked because they have no source (finding-2) |
| CK-ANA-A5 | No | Assumptions mostly stated with direction (feed resistance minimum is hottest; radio lying flat for the chimney; worst key-down length); the REQ-SYS-055 length is misquoted (finding-7) and the equipment statement is stale (finding-13) |
| CK-ANA-A6 | Yes | The note changes no requirement or hazard file; the TS-012 effects are "input to its revision" and the mechanical items go to WP-PDR-27 and 37 as findings M-1 to M-3 (the reviewer confirmed M-1 and M-2 against the Boyd and Mitsubishi drawings) |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | Yes | Section 6 states the lumped, isothermal-sink, one-node-per-part simplifications and their effect. Physics checked by the reviewer: node equations, wall mid-plane and hot-face post-processing, stack-effect vent (Cd x A/sqrt(2) x sqrt(2 g h dT/T) times rho cp), radiation linearization, the backward-Euler step, and the A4 and A5 dissipation (a backed-off class-B stage draws current in proportion to output amplitude, so holding the saturated current at the higher drain voltage is the right form, not only a conservative one). The bulkhead chain sums to 114 K/W (0.0088 W/K), inside INSP-110 O-9's 0.006 to 0.01 W/K |
| CK-ANA-B2 | No | The catalog curve is used beyond its 59 K end for a reported case (finding-10) |
| CK-ANA-B3 | Yes (limited) | The sink submodel is anchored to the catalog curve by construction; the network has no physical validation, which the note states (section 6 item 7) and routes to an in-situ sink measurement before the order (section 8 item 2). Adequate for a pre-order screen whose outputs are all labelled estimates |
| CK-ANA-B4 | Yes | Settings are in the runner (1 s and 0.5 s transient steps, 0.25 s and 30 cycles for the periodic peak, fixed-point steady state with tolerance 1e-7). Reviewer tightening: dt 0.05 s moves the 50 % and 60 % peaks by at most 0.05 K; 150 cycles by at most 0.06 K; 0.1 s moves the time to 110 C from 5.52 to 5.50 min (A5-DC); every steady state (4 layouts, 2 ambients, 4 duties) has an energy residual under 1e-4 W. The steady solver returns its last iterate without a convergence flag; none failed here |
| CK-ANA-B5 | Yes | Independent hand checks: dissipations (C-1), inhibit bounds and setpoint S (C-5, C-6), interface resistance, in-situ sink resistances (A5-DC (100.74 - 45) / 9.94 = 5.61 K/W, A5-R4 7.23, A4-DC 6.54, A4-R4 7.92 K/W, as the note says), the A4 50 % case (137.6 C, pad setpoint 76.8 C, note "138" and "about 77"), and the curve digitization (A4) |
| CK-ANA-B6 | No | Tornado and stacks exist for three metrics; the A4-DC PETG and cell cases, the surfaces and the inhibit bound have none, and the builder constants are outside every sweep (findings 1, 2, 4, 11) |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | No | LTspice `.log` reads LTspice 26.0.2 as locked; spicelib is not named and scipy is named but unused (finding-9) |
| CK-ANA-C2 | Yes | LTspice through the accredited wrapper blob `88b71475` (TV-014, ACC-LTSPICE-001); numpy, matplotlib and spicelib have no TV record and the note marks every result developer evidence; nothing closes a requirement |
| CK-ANA-C3 | No | One command reproduces the tables and plots; the lever numbers are outside it (finding-8). The deck is a netlist with one `.tran` |
| CK-ANA-C4 | Yes | Re-run at `0caa0cc` (R2): `summary.csv`, `duty_sweep.csv`, `tornado.csv`, `inputs.csv` and the deck are byte-identical; `verdicts.md` differs only in the run id; the LTspice `.log` differs only in the temporary directory, start time and elapsed time |
| CK-ANA-C5 | Yes | TV-014 limitations respected: wrapper only, short run directory, lock, time-out (`-t 180`), raw file required |

## D. Units, arithmetic and consistency of numbers

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | Units on every quantity; K and C used correctly; the analogue maps 1 V = 1 C, 1 A = 1 W, 1 ohm = 1 K/W, 1 F = 1 J/K |
| CK-ANA-D2 | No | Cross-comparison of every number in sections 3 to 7 against `summary.csv` and `verdicts.md`: all agree to the stated rounding except A4-DC long-session cells (finding-1), the section 4.3 trip statement (finding-6) and the lever numbers (finding-8) |
| CK-ANA-D3 | No | 55.17 C reported as "55 C" and as a pass (finding-1); other roundings (82.36 to 82 C for S, 111.5 to 112 C) are toward the limit |
| CK-ANA-D4 | Yes | Limits in `P` equal the governing values (110, 48, 60, 55, 60, 65, 85, 95 C), each with its source string; comparisons are inclusive (`<=`), matching "at or below" and "at most" |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | No | REQ-SYS-112 quoted correctly; REQ-SYS-113 and REQ-SYS-055 not (finding-7) |
| CK-ANA-E2 | Yes | Margins as limit minus result, signs right; no TPM applies |
| CK-ANA-E3 | No | Findings 1, 4 and 11 |
| CK-ANA-E4 | No | Finding-3 |
| CK-ANA-E5 | No | Finding-12 |
| CK-ANA-E6 | N/A | No TPM value proposed |
| CK-ANA-E7 | Yes | No credit claimed; the note is developer evidence feeding a trade study |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | Yes | Every case of the acceptance list above has a row: REQ-SYS-112 corner (both A5 channels), REQ-SYS-113, the TS-012 criteria (a) to (c) and the guard and case criteria, for four layouts |
| CK-ANA-F2 | No | HZ-003 K7, K8 and K10 cases and the C1 and C5 postures (finding-5) |
| CK-ANA-F3 | Yes | The 8.4 V pack with minimum feed drop is justified as the hottest corner; favourable and adverse stacks of all inputs are run |
| CK-ANA-F4 | No | The within-band A4-DC cases have no sensitivity (finding-1) |

## G. Kind-specific items

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | Deck, runner and plots under `hardware/sim/thermal/`, one run directory |
| CK-ANA-G1-2 | Yes | One `.tran`; the wrapper's NC_ check passed |
| CK-ANA-G1-3 | Yes | The analogue's elements are the frozen conductances and capacities of the Python network, by design (it checks the solver, as the note says) |
| CK-ANA-G1-4 | Yes | The comparison reads the `.raw` through spicelib; a failed wrapper run is reported as "Not run or failed" (no non-zero exit: finding-3) |
| CK-ANA-G3-1 | Yes | Dissipations follow the TS-012 7.3 derivation at the same corner; the key-down length follows REQ-SYS-055 (quote corrected by finding-7) |
| CK-ANA-G3-2 | No | Finding-2 |
| CK-ANA-G3-3 | Yes | Junction (both channels), module case, cells, PETG (HDT and the 60 C criterion), FR4, relay ambient and the reachable surfaces are checked |
| CK-ANA-G3-4 | Yes | REQ-SYS-113 and criterion (a) use transients with stated capacities; the duty-limited corner uses the average-power steady state, which is the long-session bound |
| CK-ANA-G7-1 | Yes | Extreme-value stacks and one-at-a-time tornado, stated |
| CK-ANA-G7-2 | Yes | Datasheet thermal resistances carry +/-10 % bands labelled E; no ageing term applies to these parts at this stage |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | Finding-5 |
| CK-ANA-H2 | No | Finding-5 (RSK-006, RSK-007, RSK-026 not named) |
| CK-ANA-H3 | Yes | Change log revision 0, 2026-09-28 |

## I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | Opened with the Read tool: `tj_vs_time_45C.png`, `tj_vs_duty.png`, `surfaces_25C_5min.png`, `petg_and_cells_45C.png`, `tornado.png`, `sink_catalog_curve.png`, `network_a5dc.png`, `ltspice_crosscheck.png` (8). Also opened: the reviewer's renders of the RA07M1317M outline page and of Boyd page 56 and its curve |
| CK-ANA-I2 | No | Limits drawn and labelled with their ids on every plot, legends and titles present, plotted values agree with `summary.csv` at the marked points (110 C crossings, trip markers, 5 min values); the network diagram misleads (finding-14) |

## J. Software assurance items

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-J1 | Yes | swe-070 7.1 task 1: the only accredited tool is LTspice (TV-014); the Python results are developer evidence and qualify nothing |
| CK-ANA-J2 | No | swe-134 7.1 tasks 1 and 6: the proposed REQ-SYS-118 sensor location and setpoints (HZ-003 K2, SW-SAFE thermal unit) do not carry the sensor offset and lag that HZ-003 C4 names (finding-4), and the proposal is not sent to the hazards writer (finding-5) |
| CK-ANA-J3 | Yes | `assurance_tasks_applied` lists the three tasks; results above |

## Completion criteria and verdict

Readiness R1 to R6 were true. Every applicable item is answered. The per-case table has a row for every case of CK-ANA-F1, each with a result and a margin. The reviewer's re-run (C4) and independent checks (B5) are recorded. Four Major findings are open, so `reviewer_verdict: NEEDS CHANGES` and `verdict: NEEDS CHANGES` (rule C1). Iteration 2 is a delta that verifies the fixes of findings 1 to 4 at their new blobs; the Minor findings are expected to be fixed in the same revision, and any not fixed become liens due at the CDR readiness declaration once the record is APPROVED.

## Verdict format

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/thermal-ts012.md@9ea3374f, hardware/sim/thermal/thermal_model.py@a7a8693c, hardware/sim/thermal/ts012_thermal.py@0c24b94a, run 2026-09-28-ts012-r1 (results, deck, 8 plots) at 0caa0cc
FINDINGS:
- [Major] finding-1 CK-ANA-D2, D3, E3, F4: A4-DC long-session cells 55.17 C is FAIL in verdicts.md and "55 C" PASS in the note; the A4-versus-A5 PETG, cell and main-bay verdicts rest on 0.1 to 1.5 K margins inside 3 to 6 K bands.
- [Major] finding-2 CK-ANA-A3, A4, B6: about 30 builder constants are untagged, unsourced and unswept; wall area, grille intercept and vent coefficient each move the marginal results by 1 to 2.6 K.
- [Major] finding-3 CK-ANA-E4: the runner asserts nothing and always exits 0; the note's verdicts are hand-transcribed.
- [Major] finding-4 CK-ANA-E3: the inhibit bound omits sensor offset and lag at the proposed NTC locations; A5 margin 1.7 K; used to rank the finalists.
- [Minor] finding-5 to finding-14: hazard and risk linkage and K7/K8/K10 cases; wrong first-trip statement; REQ-SYS-113 and 055 quotes; unreproducible lever numbers; spicelib omitted; curve extrapolation above 59 K; A4 fin-tip band; TBR proposals unstated; stale Fluke statement; network diagram line.
ITEMS N/A: CK-ANA-E6 (no TPM); G2, G4, G5, G6 (analysis_kind thermal, simulation-deck, worst-case)
VALUES PROPOSED: REQ-SYS-112 corner delta (not supported until APPROVED); REQ-SYS-118 location and setpoints (not supported: finding-4)
MEASUREMENTS: size=19 cases x 4 layouts; inputs_checked=21 datasheet or drawing values plus 8 curve points; renders=8; turns=45; minutes=75; major=4; minor=10
```

## Iteration 2: delta verification of the INSP-112 fixes (2026-09-28, HEAD `35fc7ee`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fixes of finding-1 to finding-4 (Major) and, since revision 1 answers them too, finding-5 to finding-14 (Minor), and scans the changed text, model and runner for new defects. Product: the 29 blobs of front matter `product_files`, committed as `35fc7ee` (note revision 1, run `2026-09-28-ts012-r2`, re-freeze under rule C2). Each equals `git rev-parse 35fc7ee:<path>` and `git rev-parse HEAD:<path>`; `git log 35fc7ee..HEAD` is empty. No product blob is on a `cr/` branch. The script copies in `results/2026-09-28-ts012-r2/scripts/` equal the committed scripts byte for byte (SHA-256 `54b5ecf4...3e66e0` and `09cf75ef...b97ce0`). Checklist as iteration 1: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` (head `7784672`, not an ancestor of `main`).

**Independence (rule C4).** This invocation authored no part of the note, its revision 1, the model, the runner, TS-012 or the design data analysed, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the TS-012 thermal verdict-set checker; rule C1 and the severity definitions). `grep` and `sed -n` then only pinned lines in known files (`requirements.md`, `hazards.json`, the status note, the CR-012 template). The rustos tree was not read. No web page was read in this iteration; the datasheet reads of iteration 1 stand.

**Reproduction (CK-ANA-C4, readiness R2).** In a `git archive 35fc7ee` export in the scratchpad (with `tools/ltspice-batch.sh` blob `88b71475`): `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/thermal/ts012_thermal.py --check --run-id review-r2`, exit 0 in 288 s, last line "CHECK PASS: the note's verdict set equals the computed verdict set; LTspice cross-check within 0.5 K". The wrapper waited for another session's lock, then printed "result: PASS deck=thermal_a5dc.net sha256=bf655e99...e18e36 version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0" and ended the Wine session. Byte-identical to the committed run: `summary.csv`, `inputs.csv`, `tornado.csv`, `bands.csv`, `verdict_set.csv`, `inhibit.csv`, `levers.csv`, `duty_sweep.csv`, `trips.csv`, the deck `thermal_a5dc.net` and all ten PNGs; `verdicts.md` differs only in the run id; the LTspice `.log` only in the temporary directory, start time and elapsed time. The `.raw` was read through spicelib by the runner (maximum node difference 0.016 K after 30 s).

**Reviewer scripts (scratchpad, not product):** `rv_checker.py` (known-answer test of `check()`), `rv_refactor.py` (revision 0 reproduction), `rv_hyst.py` (inhibit hysteresis), `rv_paired.py` (A5 against A4 at device-specific extremes), `rv_coupled_bands.py` and `rv_coupled_cont.py` (duty-limit metrics with the duty limit recomputed per input). All import the committed `thermal_model.py` and `ts012_thermal.py` unchanged.

### Verification of the Major findings, case by case (rule C7)

| Finding | Case the finding named | Check | Result |
|---|---|---|---|
| finding-1 | (1) A4-DC long-session cells reported as over 55 C | Note sections 4.3 (rows "Cells, long session at the duty limit" 55.2 C "FAIL by 0.2 K" and main-bay air 55.3 C "FAIL by 0.3 K"), 6 ("Cells and main bay"), 8 (residual table); `summary.csv` `dl_cell` 55.1711, `dl_main` 55.2340; values rounded up (`up1`, runner line 408) | Yes |
| finding-1 | (2) every PETG, cell, main-bay and relay case with its band; within-band cases not reported as passing | Every V01 to V18 cell of the section 5 block carries `+band` from `bands_from()` over 86 inputs and all four layouts (A4-DC included); `verdict_set()` line 424 gives FAIL when the value exceeds the limit, OPEN when value plus upward band exceeds it, else PASS. Reviewer classification of the design-change V08 to V18 margins against the band on their side (`verdict_set.csv`) reproduces the section 5 sort table: A5-DC outside the band V08 (5.98 K over, band -3.80 K), V17 (3.88 K over, band -2.90 K), V11 and V14 PASS; A4-DC PASS outside V09, V11, V13, V14, no fail outside; everything else inside | Yes (the duty-limit bands are narrowed by a frozen duty limit: new finding-15, Minor) |
| finding-1 | (3) reading restated on the physical difference | Section 5 last paragraphs and section 6 "Reading": about 9.9 W against 5.6 W into the case; A4-DC 1.5 to 6.3 K cooler; no pass and fail ranking. Reviewer paired check (`rv_paired.py`): with A5 at its lowest current (`a5_idd` 1.79 A, 8.60 W) and A4 at the 50 % hand match (`a4_isat` 1.558 A, 6.86 W), A4-DC still runs cooler on every box metric, by 1.2 to 4.9 K (continuous PETG 2.85, 50 % PETG 2.16, duty-limit PETG 2.51, bay air 4.85, duty-limit bay 3.26, cells 50 % 1.38, duty-limit cells 1.64, duty-limit main 1.23 K). The direction the note states survives the device-specific inputs | Yes |
| finding-2 | Builder constants into `P` with class, source and range; in the tornado and the bands | `inputs.csv`: 112 inputs (86 `yes`, 5 `inhibit cases`, 21 `no (fixed)`) plus 10 curve points `via k_cat`; no value lies outside its own range. The iteration 1 examples are now inputs and swept: `a_mw` (A5-DC 30 min main-bay air driver, 1.4 K), `v_g`, `cd_vent`, `c_main`, `h_gc`, the radiation splits, gap terms, stack heights and every capacity. `build()` reads only `v`, apart from the residues of observation O-1 | Yes |
| finding-2 | Refactor exact; units defect | `rv_refactor.py`: with `rho_petg` and `rho_fr4` divided by 1000 (revision 0's capacities), the revision 1 model gives `tj_ss45`, `petg_max_ss45` and `surf_max_5min_25C` equal to r1 `summary.csv` to the three decimals it writes for all four layouts, and the 300 s junction 110.52 / 107.77 / 108.24 / 106.97 C against iteration 1's reviewer values 110.5 / 107.8 / 108.3 / 107.0 C (0.1 s steps). The fixed capacity is right in magnitude: the A5-DC guard is 43 cm2 x 2 mm x 1270 kg/m3 x 1200 J/kg K = 13.1 J/K, about 11 g of PETG | Yes |
| finding-3 | Checker that asserts the stated verdicts and exits 1 | `check()` compares the block between the markers line by line with the rendered verdict set (value, band and verdict of every layout and criterion) and the LTspice difference with 0.5 K. Reviewer known-answer test (`rv_checker.py`): unchanged note exit 0; A4-DC V17 FAIL to PASS exit 1; one value 126.0 to 125.9 exit 1; end marker removed exit 1; LTspice 0.6 K exit 1; LTspice failed exit 1. Re-run exit 0 (above). Prose outside the block is still transcribed (finding-16 shows small drifts there) | Yes |
| finding-4 | Sensor offset and lag in the bound and in the setpoints; bench measurement named; margin not claimed where inside the band | `inhibit_run()`: NTC reading from `ntc_reading()` (A5 `case - f (case - sink)`, A4 `tab - f q r_pad`) through a first-order lag, trip at setpoint plus tolerance, RF off 0.15 s later, hysteresis re-arm; four cases per layout (V19 to V22); setpoint found by two secant steps, floored to 0.1 C and stepped down until a verifying run holds 110 C. Hand checks: A5-DC offset at the first nominal trip 3.02 K (`inhibit.csv`) against 0.5 x 9.94 W x 0.503 K/W = 2.50 K plus lag; A4-DC 4.50 K against 5.55 W x 0.8 K/W = 4.44 K. Hysteresis held at 5 C: reviewer runs at 3, 5 and 10 C move the V20 and V21 peaks by at most 0.07 K (`rv_hyst.py`), as the note says. Section 4.1 withdraws the ranking claim; section 9.1 item 2 names the NTC-against-thermocouple measurement. Plot `inhibit_bound.png` shows the reading 5.4 K (A5-DC) and 4.6 K (A4-DC) below the true case at the first trip | Yes |

**Result: finding-1 to finding-4 Verified.**

### Verification of the Minor findings

| Finding | Check at `35fc7ee` | Result |
|---|---|---|
| finding-5 | Section 1 names HZ-003 (K1, K2, K7 to K10; C1, C4, C5), HZ-007 (C5, K4, K5), RSK-006, RSK-007, RSK-026 (ids and texts checked in `hazards.json`: HZ-003 K1 states 40 C; HZ-007 K4 carries the 60 C discharge lock-out); V03 (K7, 300 s), V04 (K10, 180 s) and the 40 C case in section 4.1 (`summary.csv` `tj_300_40C` 101.4 to 104.2 C); postures listed as not analysed (section 7 item 9); requests R-1 to R-8 (section 9.3) | Verified |
| finding-6 | Section 4.1 trip table equals `trips.csv` (for example A4-R4 sink inhibit 12.8 min at 123.0 C; A4-DC sink never, 84.6 C) | Verified |
| finding-7 | REQ-SYS-112 and 113 quoted verbatim (`requirements.md` statements); REQ-SYS-055 "7.5 s to 13 s (TBR) ... 10 s nominal" quoted and 13 s used (`ON_S` 13.0); "exceeds" | Verified |
| finding-8 | `levers.csv`: 116.4597 / 114.5351 and 124.7424 / 121.3689 C, as section 4.1 states; the other two numbers withdrawn | Verified |
| finding-9 | Note header names numpy, matplotlib, spicelib with lock versions and scipy as a dependency only (the model's docstring still says "numpy, scipy and matplotlib": observation O-1) | Verified |
| finding-10 | Section 2 states the 59 K end and the clamp; `verdicts.md` rows "Sink rise" and "Beyond the catalog curve" (A5-R4 71.9 K, yes); the catalog "75 C rise" definition cited in section 3 | Verified |
| finding-11 | Section 4.2 "not shown to hold" with sink mass and fin-tip drop named | Verified |
| finding-12 | Section 9.2 states propose, confirm or defer for REQ-SYS-112, 113, 118 and 181 (quotation of the `tbr.plan` text: new finding-17, Minor) | Verified |
| finding-13 | Section 9.1 item 2: Fluke 174, no temperature input, stand-alone K-type thermometer with bead probe, TV record and known-answer check; matches the status note 2026-09-28 section 2 (`02e3474`, the owner's last statement that the meter has no temperature setting) | Verified |
| finding-14 | `network_a5dc.png` opened: BH1, BH2 and CELL moved; the MW to AMB line (3.7 K/W) and the MAIN to AMB line (61 K/W) pass below BAY and above BH1 without crossing a box they do not end at | Verified |

### Per-case results (iteration 2; the verdict set V01 to V22 of note section 5, one row per criterion, four layouts)

Values are the model's (all estimates), from `verdict_set.csv` of the committed run, which the reviewer's re-run reproduced byte for byte. Result rounded up to 0.1 C as the note states it; margin is limit minus the exact value; the band is the RSS of the 86 one-at-a-time swings (up / down). Order in every cell: A5-R4 / A5-DC / A4-R4 / A4-DC.

| Case | Condition | Governing id and limit | Result (checker output) and verdict word | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| V01 | Junction, continuous key-down, steady, 45 C | REQ-SYS-112 (TBR): 110 C | 142.1 / 126.0 / 131.0 / 122.7 C (FAIL / FAIL / FAIL / FAIL) | -32.09 / -15.95 / -20.94 / -12.62 K | +28.1/-18.6 / +20.0/-12.4 / +19.7/-14.6 / +20.3/-14.7 K | re-run; hand: A5 7.888 V x 1.970 A - 5.6 W = 9.94 W, A4 8.039 V x 1.387 A - 5.6 W = 5.55 W; LTspice J2 125.94 C | none |
| V02 | Junction peak, 50 % duty in 13 s key-downs, 45 C | REQ-SYS-112 delta option: 110 C | 114.6 / 104.4 / 111.9 / 105.6 C (FAIL / OPEN / FAIL / OPEN) | -4.57 / +5.61 / -1.86 / +4.47 K | +12.7/-11.1 / +12.4/-10.9 / +16.7/-12.0 / +16.2/-12.0 K | re-run; `tj_vs_duty.png` 50 % points | none |
| V03 | Junction after 5 min continuous from a 45 C soak | HZ-003 K7 design case: 110 C | 109.2 / 107.1 / 107.6 / 106.5 C (OPEN / OPEN / OPEN / OPEN) | +0.82 / +2.94 / +2.45 / +3.55 K | +6.1/-10.9 / +6.4/-10.8 / +15.2/-11.9 / +15.2/-11.9 K | re-run; old-capacity values reproduce iteration 1 C-16 | none |
| V04 | Junction after 180 s continuous from a 45 C soak | HZ-003 K10 backstop bound: 110 C | 96.7 / 95.9 / 99.6 / 99.2 C (PASS / PASS / OPEN / OPEN) | +13.38 / +14.16 / +10.41 / +10.87 K | +4.9/-9.2 / +4.9/-9.1 / +13.7/-10.6 / +13.7/-10.6 K | re-run | none |
| V05 | Module case, continuous, steady | RA07M1317M datasheet p.8: 90 C | 121.9 / 105.7 / - / - C (FAIL / FAIL / - / -) | -31.84 / -15.69 / - / - K | +28.0/-15.9 / +19.9/-9.6 K | re-run | none |
| V06 | Module case at the duty limit | RA07M1317M datasheet p.8: 90 C | 84.5 / 87.3 / - / - C (OPEN / OPEN / - / -) | +5.56 / +2.79 / - / - K | +11.1/-6.9 / +12.7/-8.4 K | re-run; with the duty limit recomputed per input the A5-DC band is +4.1/-8.1 K (still OPEN) | finding-15 |
| V07 | Hottest accessible surface, 25 C, 5 min | REQ-SYS-113 (TBR): 48 C | 64.2 / 32.3 / 49.7 / 29.5 C (FAIL / PASS / FAIL / PASS) | -16.18 / +15.71 / -1.66 / +18.59 K | +4.4/-6.4 / +2.4/-2.8 / +5.8/-4.9 / +1.8/-1.8 K | re-run; `surfaces_25C_5min.png` 5 min values | none |
| V08 | Hottest PETG face, continuous, steady | TS-012 7.3 (c): 60 C | 92.3 / 66.0 / 68.4 / 59.7 C (FAIL / FAIL / FAIL / OPEN) | -32.28 / -5.98 / -8.34 / +0.39 K | +17.4/-8.0 / +7.7/-3.8 / +5.3/-4.8 / +5.7/-2.0 K | re-run; `petg_and_cells_45C.png` left panel | none |
| V09 | Hottest PETG face, 50 % duty, steady | TS-012 7.3 (c): 60 C | 74.7 / 58.8 / 59.6 / 55.7 C (FAIL / OPEN / OPEN / PASS) | -14.63 / +1.29 / +0.41 / +4.39 K | +9.6/-4.4 / +4.7/-1.9 / +3.4/-3.0 / +3.9/-1.7 K | re-run | none |
| V10 | Hottest PETG face at the duty limit | TS-012 7.3 (c): 60 C | 70.7 / 60.1 / 58.7 / 56.5 C (FAIL / FAIL / OPEN / OPEN) | -10.66 / -0.05 / +1.35 / +3.55 K | +8.4/-3.8 / +5.1/-2.1 / +3.2/-2.8 / +4.1/-1.7 K | re-run; duty limit recomputed per input: A5-DC +6.0/-3.8, A4-DC +5.1/-3.4 K | finding-15 |
| V11 | FR4 end wall, continuous, steady | design limit (E): 105 C | - / 74.9 / - / 66.9 C (- / PASS / - / PASS) | - / +30.18 / - / +38.11 K | +7.8/-4.2 / +6.2/-3.8 K | re-run | none |
| V12 | PA-bay air, continuous, steady | G5V-2 ambient rating: 65 C | 88.9 / 67.1 / 73.4 / 61.0 C (FAIL / FAIL / FAIL / OPEN) | -23.83 / -2.05 / -8.33 / +4.05 K | +26.8/-7.6 / +8.6/-2.9 / +6.1/-5.1 / +6.3/-2.2 K | re-run | none |
| V13 | PA-bay air at the duty limit | G5V-2 ambient rating: 65 C | 69.9 / 61.4 / 63.5 / 57.2 C (FAIL / OPEN / OPEN / PASS) | -4.84 / +3.61 / +1.50 / +7.83 K | +13.1/-3.8 / +6.4/-2.2 / +3.9/-3.5 / +5.2/-1.7 K | re-run; duty limit recomputed per input: A4-DC +6.2 K, still PASS | finding-15 |
| V14 | Cells after 30 min at 50 % duty | TS-012 7.3 (a): 55 C | 51.9 / 50.7 / 52.5 / 49.2 C (PASS / PASS / PASS / PASS) | +3.17 / +4.31 / +2.54 / +5.84 K | +2.1/-1.5 / +1.9/-1.2 / +2.0/-1.7 / +1.4/-1.0 K | re-run; right panel of `petg_and_cells_45C.png` | none |
| V15 | Main-bay air after 30 min at 50 % duty | TS-012 7.3 (a): 55 C | 58.6 / 55.0 / 61.8 / 53.2 C (FAIL / OPEN / FAIL / OPEN) | -3.59 / +0.04 / -6.76 / +1.83 K | +3.9/-2.9 / +3.5/-2.3 / +3.1/-3.0 / +2.6/-2.1 K | re-run; the band comes from average-power runs (`metrics_eval`), stated in the runner | none |
| V16 | Cells, long session at 50 % duty, steady | TS-012 7.3 (a), extended: 55 C | 61.4 / 57.6 / 62.5 / 54.5 C (FAIL / FAIL / FAIL / OPEN) | -6.33 / -2.52 / -7.41 / +0.59 K | +5.2/-3.4 / +4.4/-2.7 / +4.2/-3.4 / +3.2/-2.2 K | re-run | none |
| V17 | Cells, long session at the duty limit, steady | TS-012 7.3 (a), extended: 55 C | 59.6 / 58.9 / 61.5 / 55.2 C (FAIL / FAIL / FAIL / FAIL) | -4.55 / -3.88 / -6.47 / -0.17 K | +4.5/-3.1 / +5.0/-2.9 / +4.0/-3.2 / +3.5/-2.3 K | re-run; duty limit recomputed per input: A5-DC +6.3/-4.4 K (5 % grid) or +6.6/-3.9 K (continuous), A4-DC +4.5/-3.5 K | finding-15 |
| V18 | Main-bay air, long session at the duty limit | TS-012 7.3 (a), extended: 55 C | 60.2 / 57.8 / 63.5 / 55.3 C (FAIL / FAIL / FAIL / FAIL) | -5.20 / -2.79 / -8.50 / -0.23 K | +4.6/-3.4 / +4.7/-2.8 / +3.9/-3.5 / +3.5/-2.5 K | re-run; duty limit recomputed per input: A5-DC +6.0/-3.6 K, A4-DC +4.3/-3.1 K | finding-15 |
| V19 | Inhibit bound (closed loop), nominal | REQ-SYS-118, HZ-003 K2 and C4: 110 C | 108.6 / 108.3 / 114.8 / 114.2 C (PASS / PASS / FAIL / FAIL) | +1.49 / +1.70 / -4.80 / -4.13 K | explicit case; hysteresis 3 to 10 C moves it at most 0.07 K | re-run; hand offsets above | none |
| V20 | Inhibit bound (closed loop), +3 C tolerance | REQ-SYS-118, HZ-003 K2 and C4: 110 C | 111.5 / 111.3 / 117.5 / 117.0 C (FAIL / FAIL / FAIL / FAIL) | -1.46 / -1.22 / -7.49 / -6.96 K | explicit case | re-run | none |
| V21 | Inhibit bound (closed loop), +3 C, sensor offset and lag adverse | REQ-SYS-118, HZ-003 K2 and C4: 110 C | 114.4 / 113.9 / 117.8 / 117.1 C (FAIL / FAIL / FAIL / FAIL) | -4.33 / -3.89 / -7.75 / -7.09 K | explicit case | re-run; setpoints 80.4 / 80.9 / 75.9 / 77.1 C (`inhibit.csv`) | finding-16 |
| V22 | Inhibit bound (closed loop), +3 C, sensor, Rth and dissipation adverse | REQ-SYS-118, HZ-003 K2 and C4: 110 C | 123.2 / 122.8 / 133.5 / 132.4 C (FAIL / FAIL / FAIL / FAIL) | -13.15 / -12.75 / -23.50 / -22.36 K | explicit case | re-run; setpoints 71.4 / 71.7 / 60.0 / 60.0 C | finding-16 |
| C-19 | LTspice analogue of A5-DC against the Python solver | note criterion: 0.5 K | 0.016 K | +0.484 K | n/a | re-run through the wrapper, deck byte-identical (SHA-256 `bf655e99...e18e36`) | none |

### Findings (iteration 2; current state of every finding of this record)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-D2, D3, E3, F4 | note sections 4.3, 5, 6, 8 | See iteration 1 and the verification table | Verified (iteration 2, revision 1 at 35fc7ee) | n/a | |
| finding-2 | reviewer | Major | CK-ANA-A3, A4, B6, G3-2 | `thermal_model.py` `P`, `build()` | See iteration 1 | Verified (iteration 2) | n/a | |
| finding-3 | reviewer | Major | CK-ANA-E4, D2 | `ts012_thermal.py` `check()`; note section 11 | See iteration 1 | Verified (iteration 2) | n/a | |
| finding-4 | reviewer | Major | CK-ANA-E3, B6 | `thermal_model.py` `inhibit_run()`, `ntc_reading()`; note section 4.1 | See iteration 1 | Verified (iteration 2) | n/a | |
| finding-5 to finding-14 | reviewer | Minor | as iteration 1 | as iteration 1 | See the Minor verification table | Verified (iteration 2) | n/a | |
| <a id="finding-15"></a>finding-15 | reviewer | Minor | CK-ANA-B6, F4, G7-1 | `ts012_thermal.py` `tornado_all(L, limits[L]["dmax"])` and `metrics_eval()` (`Td = net.steady(dmax)`); note section 5 sort table (A5-DC "V17 long-session cells at the duty limit (3.9 K over, band -2.9 K)") and section 6 A5 "Reading" ("two fail outside their bands") | The tornado holds the duty limit at its nominal value (60 % for both design-change layouts) while it sweeps the inputs, but the duty-limited corner is defined as the largest duty that holds 110 C, and the protection the note proposes (the inhibit setpoint or the duty limit S) sets the duty from the thermal state. An input that cools the junction raises the allowed duty and heats the box; one that heats it lowers the duty and cools the box. The bands of V06, V10, V13, V17 and V18 therefore leave out a first-order term. Reviewer recomputation with the duty limit re-found for each input value (`rv_coupled_bands.py`, 5 % grid as the runner; `rv_coupled_cont.py`, bisection to 0.5 %): A5-DC V17 -2.9/+5.0 K becomes -4.4/+6.3 K (grid) or -3.9/+6.6 K (continuous); A5-DC V18 -2.8/+4.7 becomes -3.6/+6.0 K; A5-DC V10 -2.1/+5.1 becomes -3.8/+6.0 K; A4-DC V17 -2.3/+3.5 becomes -3.5/+4.5 K; A4-DC V13 +5.2 becomes +6.2 K (still PASS at 7.8 K margin); A5-DC V06 +12.8 becomes +4.1 K (the frozen duty overstates it). The largest single terms are `k_orient` (A5-DC cells -2.5 to -2.7 K) and `r_feed` (+4.4 K). No verdict word of the section 5 block changes (no PASS becomes OPEN; the R4 layouts have no duty-limit PASS), and the reading on the heat is unaffected. But the A5-DC V17 fail that section 5 and section 6 call shown outside its band sits at the edge of the corrected band (margin 3.88 K against 3.9 to 4.4 K), so "two A5-DC failures outside the band" is one clearly (V08) and one at the edge (V17). Fix: recompute the duty limit for each tornado input (or define the duty-limited corner as a fixed duty cap and say that under the proposed protection the duty moves with the inputs), and restate V17 A5-DC in sections 5 and 6 | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-16"></a>finding-16 | reviewer | Minor | CK-ANA-D2, D3 | note section 4.1 inhibit table and the paragraph after it, section 4.1 duty-limit paragraph, section 5 paragraphs after the block, section 8 change 6, section 9.3 R-5 | Hand-transcribed prose outside the checked block drifts from the results in six places. (a) The section 4.1 inhibit table gives the A5-DC all-adverse maximum as 122.7 C; `inhibit.csv` 122.7485, rounded up 122.8 C as V22 states. (b) "The R4 layouts give the same picture within 0.5 K": A4-R4 against A4-DC differs by 0.5 to 1.1 K in maximum junction (114.80 / 114.13, 117.49 / 116.96, 117.75 / 117.09, 133.50 / 132.36 C) and its setpoints are 0.7 to 1.2 K lower (79.6, 76.6, 75.9 against 80.3, 77.3, 77.1 C). (c) "1.4 to 5.7 K up for A4-DC" (V08 to V18): V11 is +6.3 and V12 +6.4 K, so 1.4 to 6.4 K. (d) "1.5 to 6.3 K cooler": the continuous PETG difference is 65.98 - 59.61 = 6.37 K, so 1.5 to 6.4 K. (e) The duty-limit S is 82.36 C (A5) and 70.19 C (A4) in `summary.csv`, stated as 82.4 and 70.2 C, and the programmed values 79.36 and 67.19 C as 79.4 and 67.2 C: an upper temperature setpoint rounded up, away from the safe side, where the runner's own inhibit setpoints are floored (`math.floor`, line 253); R-5 sends these to the SW requirements writer. (f) "At the first trip the case stands 2.9 to 5.4 K (A5) ... above the reading, and up to 10.4 K in the all-adverse A4 case": the all-adverse A5 cases are 8.8 and 9.3 K. No verdict word changes; (e) moves two proposed values by 0.1 K. Fix: correct (a) to (f), round S down (82.3 and 70.1 C; programmed 79.3 and 67.1 C), and consider generating the section 4.1 tables from the runner as the section 5 block is | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-17"></a>finding-17 | reviewer | Minor | CK-ANA-E1, E5 | note section 9.2, column "TBR plan step" and the REQ-SYS-181 row | (1) The REQ-SYS-112 row puts in quotation marks "The PDR thermal analysis fixes the value"; the requirement's `tbr.plan` reads "TS-003 (device RthJC) and the thermal budget at PDR fix the limit and the condition; Robin approves in the PDR memo." The proposal changes the condition (the corner), which that plan allows, so no conclusion moves, but the quote is not the text. (2) The REQ-SYS-113 row paraphrases the plan as fixing "the value and the test-finger set"; the plan says the thermal budget at PDR fixes the value and that the value is re-based by CR if the owner adopts IEC 62368-1 or ISO 13732-1; E5 asks whether that "else a CR" branch is triggered, and the row does not say. (3) The REQ-SYS-181 row takes the RA07M1317M ratings (175 C channel, 110 C Tcase(OP) maximum) from this record ("not re-read here"); the basis of a deferred confirmation should cite the datasheet pages (Jun 2019, pp.2 and 8). Fix: quote the plans exactly, state the IEC 62368-1 / ISO 13732-1 branch as not triggered (or triggered), and cite the datasheet | Open | Pending | CDR readiness declaration (lien, rule C1) |

### Observations (not findings)

- O-1. `thermal_model.py` docstring (lines 36 to 37) still names "numpy, scipy and matplotlib"; `build()` keeps three numbers outside `P`: the 0.5 V drop and 5 V rail in the relay-hold LM2940 correction (lines 500 to 501) and the 0.05 K floor of the stack-effect rise (line 379). The note says `build()` has "no numeric input left (physical constants only)". Effect: under 0.2 W in the design-change layouts; no verdict can move.
- O-2. `run-stdout.txt` and `check-stdout.txt` are the same blob (`281fb8bd`), both the `--check` run; harmless, because `--check` re-runs everything.
- O-3. "About twice the PA heat" is 1.8 at the corner (9.94 / 5.55 W) and 1.25 at the device-specific extremes of the paired check above; the direction holds in both.
- O-4. The proposed inhibit thresholds (about 81 C A5, 77 C A4) hold 110 C with the sensor adverse and the tolerance, but with nominal Rth(ch-case) and dissipation; with those adverse (V22) the thresholds are 71.7 and 60.0 C. The note states both (sections 4.1 and 6); the owner ruling under rule C10 should name which case the threshold is set for. The bench offset measurement closes the sensor terms, not the dissipation term.
- O-5. The RSS band is not a worst-case stack (limitation 7 says so); iteration 1's favourable and adverse stacks were dropped in revision 1. For a safety-critical threshold the explicit V19 to V22 cases carry the stack, which is adequate for this screen.

### Checklist items changed at iteration 2

CK-ANA-A3, A4 (finding-2), B2 (finding-10), C1 (finding-9), C3 (finding-8), E3 (findings 1, 4, 11), E4 (finding-3), F2 (finding-5), G3-2 (finding-2), H1, H2 (finding-5), I2 (finding-14), J2 (finding-4 and R-1): now Yes. E5: Yes (section 9.2 states propose, confirm or defer for every value; the quotation defect is finding-17 under E1). Still No on the open Minor liens: CK-ANA-B6 and F4 (finding-15), D2 and D3 (finding-16), E1 (finding-17). CK-ANA-H3: the change log names revision 1 with its date and reason and names INSP-112 (section 12); Yes. CK-ANA-J1: unchanged, LTspice is the only accredited tool and every Python number is marked developer evidence. CK-ANA-J2: the proposed REQ-SYS-118 threshold now carries the HZ-003 C4 sensor offset and lag, and R-1 sends the placement and setpoints to the hazards writer; Yes.

### Visual closure (iteration 2)

All ten renders of the run opened with the Read tool (`renders_inspected: 10`): `margins_vs_band.png` (every verdict with its band; error bars drawn with the upward band to the left of the margin, correct on a limit-minus-value axis; verdict words and margins agree with `verdict_set.csv`), `inhibit_bound.png` (four closed-loop cases per design-change layout, legends agree with `inhibit.csv`; zooms show the case 5.4 K and 4.6 K above the reading at the first trip; the A4-DC junction sits at 116 to 117 C for several key-downs before the pad NTC trips), `network_a5dc.png` (finding-14 fixed), `tj_vs_time_45C.png` (markers at the `trips.csv` times and junctions), `tornado.png` (eight panels, RSS band shaded, limits drawn), `petg_and_cells_45C.png` (60 C criterion, 69 C HDT, 105 C FR4 lines; FR4 bars hatched), `surfaces_25C_5min.png` (48 C line; 5 min values as the note), `tj_vs_duty.png` (the A5-DC and A4-DC curves sit about 0.1 to 0.3 K under 110 C at 60 %, which is why the duty limit moves with small input changes, finding-15), `ltspice_crosscheck.png` (six nodes overlaid, 0.016 K), `sink_catalog_curve.png` (digitized points, 2.6 and 3.4 K/W lines, the two corner points 3.81 and 4.18 K/W). Legends round to nearest (for example 111.2 C) where the note and block round up (111.3 C); cosmetic.

### Completion criteria (SWE-088), iteration 2

Readiness R1 to R6 are true at `35fc7ee` (R2: reviewer re-run exit 0; R6: all ten renders exist and were opened). Every applicable item is answered. The per-case table has a row for every criterion of the verdict set and every row has a result and a margin. The reviewer's re-run (C4) and independent checks (B5: dissipation, NTC offsets, refactor reproduction, paired comparison, hysteresis, coupled bands) are recorded. Zero Major findings are open: `reviewer_verdict: APPROVED` (rule C1). finding-15 to finding-17 are Minor and Open, liens due at the CDR readiness declaration, owner Claude as the WP-PDR-28 analysis author. The record `verdict` is held at NEEDS CHANGES only because the applied template is still on the CR-012 branch (front matter); the lead SE sets it to APPROVED in the CR-012 merge commit if the template blob `0386cc6e` and the product blobs are unchanged. Under rule C10 the `values_proposed` then go to the owner as proposals; the owner rules the values (see observation O-4 for the choice the REQ-SYS-118 ruling has to make).

```
ITERATION 2 (2026-09-28, HEAD 35fc7ee, product commit 35fc7ee): REVIEWER VERDICT: APPROVED (liens finding-15 to finding-17); RECORD VERDICT: NEEDS CHANGES (held: analysis template only on cr/CR-012)
PRODUCT: docs/design/analysis/thermal-ts012.md@81592c34, hardware/sim/thermal/thermal_model.py@54573514, hardware/sim/thermal/ts012_thermal.py@3eb26aaa, README.md@b06cdbf5, run 2026-09-28-ts012-r2 (CSVs, verdicts.md, deck, log, 10 plots) at 35fc7ee
FINDINGS:
- [Major] finding-1 to finding-4: Verified (A4-DC 55.2 C FAIL reported; RSS bands on every verdict with PASS / OPEN / FAIL; 112 classed inputs, 86 swept, refactor exact; --check exits 1 on any difference (known-answer tested); closed-loop inhibit with NTC offset and lag).
- [Minor] finding-5 to finding-14: Verified.
- [Minor] finding-15 (new): duty-limit metric bands freeze the duty limit; A5-DC V17 "outside the band" is at the edge (3.9 K against 3.9 to 4.4 K); no verdict word changes. Open, lien.
- [Minor] finding-16 (new): six prose numbers drift from the results (122.7 vs 122.8 C; R4 "within 0.5 K" is up to 1.2 K for A4; band and difference ranges; S rounded up, away from the safe side). Open, lien.
- [Minor] finding-17 (new): section 9.2 misquotes the REQ-SYS-112 tbr.plan, omits the REQ-SYS-113 re-base branch, cites the RA07M1317M ratings to this record. Open, lien.
ITEMS N/A: CK-ANA-E6 (no TPM); G2, G4, G5, G6 (analysis_kind thermal, simulation-deck, worst-case)
VALUES PROPOSED: REQ-SYS-112 corner delta; REQ-SYS-118 threshold about 81 C (A5) / 77 C (A4) at a PA-case NTC in the heat path or duty limit S; REQ-SYS-113 48 C confirmed with the wrap guard; REQ-SYS-181 deferred (supported as proposals once the record verdict is APPROVED)
MEASUREMENTS: size=22 criteria x 4 layouts (82 cells) plus the LTspice check; blobs equal HEAD 29/29; checker CHECK PASS exit 0 in 288 s; outputs byte-identical 9 CSV + deck + 10 PNG; checker known-answer cases 6/6; reviewer model runs: refactor 4 layouts, hysteresis 12, paired 2, coupled bands 2 x 86 x 2 (twice); renders=10; major open=0; minor open=3; turns=45; minutes=80 (cumulative 90 and 155); iteration=2
```
