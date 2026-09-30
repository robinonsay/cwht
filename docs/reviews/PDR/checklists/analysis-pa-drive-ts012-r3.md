---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-21 PA drive note from
# revision 3 on (section R3, A5 as adopted, and its fix revisions R4 and R5). INSP-114
# (docs/reviews/PDR/checklists/analysis-pa-drive-ts012.md) reviewed revisions 0 to 2 and used its three iterations
# under rule C1, so the note's Status row leaves the record of revision 3 on to the lead SE; this is that new record.
# Iteration 1 (2026-09-29): revision 3 frozen at F0 at f1070cf; NEEDS CHANGES on Major finding-1 and finding-2 and
# Minor finding-3 to finding-10. Iteration 2 (delta, rule C1): revision 4 at d0de188; finding-1 and finding-2
# Verified, new Major finding-31 and Minor finding-32 to finding-36 raised. Iteration 3 (delta, rule C1, the last
# iteration): revision 5 at a0c4db6, finding-31 Verified; one new Minor finding, renumbered finding-37 by the lead
# SE at filing (it collided with iteration 2's finding-32; ids are never reused).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; the branch head is not an ancestor of HEAD a0c4db6).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field names
# peer-review-checklist-design revision B and checklist_analysis records the template actually applied, as INSP-083,
# INSP-114 and INSP-115 did.
# id: INSP-124 (the lead SE's assignment; the returned texts proposed INSP-124 as the next free id at the time of
# each review). Filed by the lead SE from the three reviewers' returned texts verbatim (the harness does not let a
# reviewer create a new review-record file); no record previously existed at this path. A record already exists for
# revisions 0 to 2 of this same note: INSP-114, docs/reviews/PDR/checklists/analysis-pa-drive-ts012.md.
id: INSP-124
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-pa-drive-ts012-r3.md
product: docs/design/analysis/pa-drive-ts012.md
product_commit: "a0c4db679653e64a2d30803f1b2000027b6e6516"
product_files: ["docs/design/analysis/pa-drive-ts012.md@309c8744cfa37aa4cb4916f615f358a41716d3a4", "hardware/sim/tx-pa/README.md@b6b86ffa1b0794128e06ac03a256dbcfcc554e02", "hardware/sim/tx-pa/run_a5_r5.py@56da6f40bcd6065d08b52018c61bfa82e081b2c3", "hardware/sim/tx-pa/run_a5_r4.py@4e5e3a3b78a4c4f5cbe7f27dca2ecac661c4ceec", "hardware/sim/tx-pa/run_a5_r3.py@40941ee0870f7c6d16931962dd0e72db003c45ef", "hardware/sim/tx-pa/run_pa.py@44769c4579ef473795504837c96eace1159eca4f", "hardware/sim/tx-pa/results/2026-09-30-r5-p4-power-a5-design/power_a5_added_case_d9.png@b9092e6f753d6dc3c62f084f393dc20ba8c0d4ac", "hardware/sim/tx-pa/results/2026-09-30-r5-p4-power-a5-design/power_a5_step.cir@d06a8b84091c24da01dff5a1ee08f1181e679c6a", "hardware/sim/tx-pa/results/2026-09-30-r5-p4-power-a5-design/power_a5_step.raw@f78fdf1540f6afde466e3c43f8ce0f984f93810f", "hardware/sim/tx-pa/results/2026-09-30-r5-p4-power-a5-design/result.json@128f92d540dae08a1b2d84e8ce45e31b0930b2bb", "hardware/sim/tx-pa/results/2026-09-30-r5-p4-power-a5-design/result.md@62f68b4238931145ef6351deb50eb0ee9abed33e", "hardware/sim/tx-pa/results/2026-09-30-r5-p5-power-a5-clamp-b/power_a5_added_case_clampb.png@1957deb5c4f162ad15793186e71647085ccf0aab", "hardware/sim/tx-pa/results/2026-09-30-r5-p5-power-a5-clamp-b/power_a5_step.cir@15a24a7ddf775f7fc0a92c574c400e61c5ff7e76", "hardware/sim/tx-pa/results/2026-09-30-r5-p5-power-a5-clamp-b/power_a5_step.raw@101fddc49bba5d4223fd1a63adbeb9e99e50d3ca", "hardware/sim/tx-pa/results/2026-09-30-r5-p5-power-a5-clamp-b/result.json@2be1c9d43d2ddef76f9e462d4089146d41fd2d6e", "hardware/sim/tx-pa/results/2026-09-30-r5-p5-power-a5-clamp-b/result.md@fba3272be7aa9e49822e83714c1a3233414b65b6", "hardware/sim/tx-pa/results/2026-09-30-r5-s5-pass-population/pack_current_dissipation.png@22ff5f7b308648d051683decff1d42b2738b1f2b", "hardware/sim/tx-pa/results/2026-09-30-r5-s5-pass-population/pass_population.png@b9f4b01d3c39f0001753949980000995f6847c0e", "hardware/sim/tx-pa/results/2026-09-30-r5-s5-pass-population/result.json@b0dd2839481997086fd2f6e53b25e009a4ffbea0", "hardware/sim/tx-pa/results/2026-09-30-r5-s5-pass-population/result.md@103315e6318ab343242740280af8f41395eeafda"]
product_commit_iteration_1: "f1070cf85a5a5b8e9535e5028bee726ad593671a"
product_files_iteration_1: ["docs/design/analysis/pa-drive-ts012.md@48c0ed44884d6529d59e5d91f42276c00db1e7d7", "hardware/sim/tx-pa/README.md@d3621ee087cb20ed3b8b3dd73a4295c61fccf78c", "hardware/sim/tx-pa/run_a5_r3.py@40941ee0870f7c6d16931962dd0e72db003c45ef", "hardware/sim/tx-pa/run_pa.py@44769c4579ef473795504837c96eace1159eca4f", "hardware/sim/tx-pa/results/2026-09-29-r3-d6-drive-a5-bpf/corners.json@c1d5f81cd9bc0668ec9e39f49760d0f2755737d7", "hardware/sim/tx-pa/results/2026-09-29-r3-d6-drive-a5-bpf/drive_a5_bpf.cir@47103880d57b540f1246b6ff5910de8c5dad6594", "hardware/sim/tx-pa/results/2026-09-29-r3-d6-drive-a5-bpf/drive_a5_bpf_corners.png@69402411e4be29e0b6fa69918f63e4e95b800c41", "hardware/sim/tx-pa/results/2026-09-29-r3-d6-drive-a5-bpf/raw.sha256@b2f07d1e6b1202bb9932dd871d3bce867c11e6ee", "hardware/sim/tx-pa/results/2026-09-29-r3-d6-drive-a5-bpf/result.json@c7391570dc3d67237e6daa7a4caf4ae0dfcaf852", "hardware/sim/tx-pa/results/2026-09-29-r3-d6-drive-a5-bpf/result.md@1cd6a2a604320b308512a2c6defeaf52854c6716", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/coax_a5_bpf.cir@a274290ae568451e2a92c550ae6cf4ca076006df", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/coax_a5_bpf_steps.json@3372b557f7ac1bff1788e2d11c5b1dffd31ce81b", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/coax_length_bound_bpf.png@5668438b48025045c97d9ced33f80e590a7736b0", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/raw.sha256@5fdbb943f63c9d2e4dc5516370c37a72550e056e", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/result.json@87cf69e1c5b7f406f5600dd89740dd0bba59ffd0", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/result.md@73957533a3990195087a822a40b497b6e0c7c678", "hardware/sim/tx-pa/results/2026-09-29-r3-d7-coax-bound-bpf/tstep_a5_bpf.cir@9a14481332c1faca4595b15f9da7a3f5f00bf266", "hardware/sim/tx-pa/results/2026-09-29-r3-k1-probe-17mw/probe_dc.cir@24f2c4785f43f344841ae1b3cf4d223e1b61fe36", "hardware/sim/tx-pa/results/2026-09-29-r3-k1-probe-17mw/probe_reading_error.png@cb74933d4be23cf0599ce2baed62310503c3eea9", "hardware/sim/tx-pa/results/2026-09-29-r3-k1-probe-17mw/probe_rf.cir@a552cca22a7a05f369ebf7a2bd3ecba408d5eac3", "hardware/sim/tx-pa/results/2026-09-29-r3-k1-probe-17mw/raw.sha256@86c9683c97d14792614bc7a803610336f8113510", "hardware/sim/tx-pa/results/2026-09-29-r3-k1-probe-17mw/result.json@284356a2d824fb364f25823ddd09bcc579aef4f7", "hardware/sim/tx-pa/results/2026-09-29-r3-k1-probe-17mw/result.md@6d27ebe49ba3c17632e9d2111dd06a0bdca50551", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/power_a5_design.cir@2470dc68e7ecae8783afd5d5ccbe2563d542c7ca", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/power_a5_design_sma.png@0e881a69afd9b279c11fba90a89319f6e02bd8e9", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/power_a5_design_temperature.png@29d73fe676e4d2f75be505ecbc1ecf97c5073a41", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/raw.sha256@188db8acc2a837bbceddfdc4bf237b65a684c8a3", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/result.json@4d8ebded522b31b81c803637b168b7309820e133", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design/result.md@ae62446a975b7797de378f3c770136c06aca9bc9", "hardware/sim/tx-pa/results/2026-09-29-r3-p5-power-a5-clamp-b/power_a5_clampb_sma.png@bf539f96209f5920356cc9efc464c37db869c8a9", "hardware/sim/tx-pa/results/2026-09-29-r3-p5-power-a5-clamp-b/power_a5_clampb_temperature.png@2aab628ff4b373d776d6caacfdc456f3c4c0cf49", "hardware/sim/tx-pa/results/2026-09-29-r3-p5-power-a5-clamp-b/power_a5_design.cir@606e24dad8a7f98a909fd7260b09f0ba1ff6277f", "hardware/sim/tx-pa/results/2026-09-29-r3-p5-power-a5-clamp-b/raw.sha256@6bb5865eb2e4301b2f0db92150108bc8391b7737", "hardware/sim/tx-pa/results/2026-09-29-r3-p5-power-a5-clamp-b/result.json@f5d9bf3df0cd410e12c1ffec27b75ca0dfaeb172", "hardware/sim/tx-pa/results/2026-09-29-r3-p5-power-a5-clamp-b/result.md@a092878efcf4a060bda88a50e7076a2beb964ece", "hardware/sim/tx-pa/results/2026-09-29-r3-s2-sot-pad/result.json@cdae0e517c0916231d8c075aaa37b0d7cd0f8f20", "hardware/sim/tx-pa/results/2026-09-29-r3-s2-sot-pad/result.md@9d3aff0734dc33764c303e93dd686ddc018b74cd", "hardware/sim/tx-pa/results/2026-09-29-r3-s2-sot-pad/sot_band.png@0846cd839dadbd8974b3dd8e17b7b2f3d9866186", "hardware/sim/tx-pa/results/2026-09-29-r3-s3-req012-basis/req012_basis.png@3a511be8828b869ed5329a2d59e639c136e32af4", "hardware/sim/tx-pa/results/2026-09-29-r3-s3-req012-basis/result.json@66773b44169c7ad02b7b835b91b8bcb712b0f8fb", "hardware/sim/tx-pa/results/2026-09-29-r3-s3-req012-basis/result.md@73f2d4619649e67b6d3f3a63a65a87776e233046", "hardware/sim/tx-pa/results/2026-09-29-r3-s3-req012-basis/verdicts.json@e61bb7dac0a7524145f464ecdaaeec979b7490da"]
product_commit_iteration_2: "d0de188ebfc4b48cd5b9590e1368a8d7ec854cf4"
product_files_iteration_2: ["docs/design/analysis/pa-drive-ts012.md@fc9ebb179349cdfe9873ab85ec06a821e04b2af3", "hardware/sim/tx-pa/README.md@afa6dfdee8a982561f0d3a2382ce31e810acc21d", "hardware/sim/tx-pa/run_a5_r4.py@4e5e3a3b78a4c4f5cbe7f27dca2ecac661c4ceec", "hardware/sim/tx-pa/run_a5_r3.py@40941ee0870f7c6d16931962dd0e72db003c45ef", "hardware/sim/tx-pa/run_pa.py@44769c4579ef473795504837c96eace1159eca4f", "hardware/sim/tx-pa/results/2026-09-29-r4-p4-power-a5-design/power_a5_step.cir@7f7b805108595e7bfdbbad1de53bf7d633817bac", "hardware/sim/tx-pa/results/2026-09-29-r4-p5-power-a5-clamp-b/power_a5_step.cir@cafb48cb429ad81bcc7652cbed172900c800abc5", "hardware/sim/tx-pa/results/2026-09-29-r4-s2-sot-pad/sot_band_r4.png@3578b720e52a023377d6e4f314d36fad999b3a19", "hardware/sim/tx-pa/results/2026-09-29-r4-p4-power-a5-design/power_a5_step_d9_sma.png@0614de27bd85d48fab218816bae8cceba352b9a0", "hardware/sim/tx-pa/results/2026-09-29-r4-p4-power-a5-design/power_a5_step_d9_temperature.png@77a01e6628d57c558cf63bf672793c657f7e8370", "hardware/sim/tx-pa/results/2026-09-29-r4-p5-power-a5-clamp-b/power_a5_step_clampb_sma.png@5f53407e1e6b7505beb12a8255d341afb5bfc977", "hardware/sim/tx-pa/results/2026-09-29-r4-p5-power-a5-clamp-b/power_a5_step_clampb_temperature.png@d50b2394b27ce4ab8c07898199e58ce58a69887d", "hardware/sim/tx-pa/results/2026-09-29-r4-s4-clamp-step/clamp_step.png@39d329eeba96e727916aedc10b51d25524550b54", "hardware/sim/tx-pa/results/2026-09-29-r4-s3-req012-basis/req012_basis_r4.png@f68712a711250d981936043837a7eeba3b73c6d5", "hardware/sim/tx-pa/results/2026-09-29-r4-s3-req012-basis/verdicts.json@bd3d28cf6a4f04f2336c5a48baf2b77c1dbe4c8f"]
analysis_kind: [simulation-deck, cascade, worst-case]
product_size: "iteration 3: 1 note section (R5, 108 lines) plus 12 in-place revision 5 markers and 1 change-log row (note 1147 lines); 1 new checker (run_a5_r5.py, 554 lines, importing run_a5_r4.py); 2 LTspice decks (1944 + 1944 power steps); 1 post-processing run (s5); 4 result plots; 25 verdicts. Iteration 2: note section R4 (about 245 lines of 1092, revision 4); 2 LTspice power decks of 13608 steps each; 3 post-processing runs; 1 checker (run_a5_r4.py, 1224 lines); 7 cited plots. Iteration 1: note section R3 (revision 3, lines 12 to 326 of 843); 1 new checker (run_a5_r3.py, 1683 lines); 6 LTspice decks; 2 post-processing runs; 9 result plots (8 cited); 39 verdicts"
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13 (TV-001 accredits the interpreter); numpy, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/tx-pa/*.py: developer evidence per 05 section 9.1"]
values_proposed: ["REQ-SYS-144: clamp-step reject sentence on the believed spread, a unit whose projected reading puts its module more than 1.5 dB (TBR) above the typical RA07M1317M curve, or whose clamp the trim range cannot bring to that value, is rejected (note R5.4; supported)", "REQ-SYS-012: 5 W +1/-2.7 dB (TBR) at 6.4 V, +1/-2.3 dB (TBR) at 6.7-8.4 V (clamp scenario B with the step; unchanged since iteration 2)"]
renders_inspected: 4
renders_inspected_iteration_1: 9
renders_inspected_iteration_2: 7
sprint: PDR-prep
author_agent: "author:WP-PDR-21 tx-pa revisions 3 to 5 (Claude as analysis author, wave W-A; freeze commits f1070cf, d0de188, a0c4db6)"
reviewer_agent: "reviewer:WP-PDR-21-analysis-pa-drive-r3-iter3 (iteration 3; independent, authored no part of the note or any revision of it, run_a5_r3.py, run_a5_r4.py, run_a5_r5.py, run_pa.py, the decks, TS-012 or the INSP-114 record)"
reviewer_agent_iteration_1: "reviewer:WP-PDR-21-analysis-pa-drive-r3-iter1 (independent; authored no part of the note or its revisions, run_a5_r3.py, run_pa.py, the decks, the digitizers, TS-012 or the INSP-114 record)"
reviewer_agent_iteration_2: "reviewer:WP-PDR-21-analysis-pa-drive-a5-iter2 (independent; authored no part of the note, its revisions, the decks, the checkers, the digitizers or TS-012)"
# criticality: a hardware-only transmit analysis; it sets no value of a 07 section 14.1 component (the D-9 clamp and
# the clamp step are analogue and build-time; WP-PDR-22 owns the keying loop)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3, final): APPROVED. finding-31 (Major) is Verified at a0c4db6; finding-1 and finding-2
# were Verified at iteration 2. No Major finding is open. Fourteen Minor findings are open as liens (finding-3 to
# finding-10 from iteration 1, finding-32 to finding-36 from iteration 2, finding-37 renumbered from iteration 3).
reviewer_verdict: APPROVED
reviewer_verdict_iteration_1: NEEDS CHANGES
reviewer_verdict_iteration_2: NEEDS CHANGES
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES only because the applied analysis template is still only on cr/CR-012 (branch head
# 7784672, not merged; lead SE convention of 2026-09-27, INSP-083 and INSP-114). The reviewer verdict is APPROVED;
# no Major finding is open and nothing escalates to the owner under rule C1.
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 14
findings_open: 14
findings_fixed: 0
findings_verified: 3
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-D2]
items_no_iteration_1: [CK-ANA-A2, CK-ANA-B6, CK-ANA-D2, CK-ANA-E3, CK-ANA-E5, CK-ANA-F3, CK-ANA-G7-2, CK-ANA-H2, CK-ANA-I2]
items_no_iteration_2: [CK-ANA-A3, CK-ANA-A5, CK-ANA-B1, CK-ANA-D2, CK-ANA-F2, CK-ANA-H1, CK-ANA-H2, CK-ANA-H3, CK-ANA-I2]
effort_turns: 165
effort_minutes: 370
record_status: Open
date: 2026-09-30
date_closed: null
---

# Peer review record INSP-124: WP-PDR-21 PA drive note, revisions 3 to 5 (A5 as adopted)

**Product.** `docs/design/analysis/pa-drive-ts012.md`, section R3 (revision 3, A5 as adopted) and its fix sections R4 (revision 4) and R5 (revision 5), with the checkers `hardware/sim/tx-pa/run_a5_r3.py`, `run_a5_r4.py` and `run_a5_r5.py` (all importing `run_pa.py`, reviewed at INSP-114) and their runs under `hardware/sim/tx-pa/results/2026-09-29-r3-*`, `2026-09-29-r4-*` and `2026-09-30-r5-*`.

**Iterations 1 and 2.** Iteration 1 (revision 3 at `f1070cf`) raised Major finding-1 (the select-on-test band used a symmetric frequency term about the 146 MHz selection point) and Major finding-2 (the open-loop ceilings rested on the typical module), with Minor finding-3 to finding-10. Iteration 2 (revision 4 at `d0de188`) Verified finding-1 and finding-2 and raised Major finding-31, introduced by the finding-2 fix: the clamp step's reject rule acts on the spread the step believes, so the true spread of a passing unit reaches +1.5 + g- dB. Their full texts are with the lead SE (filing note in the front matter).

## Iteration 1 (2026-09-29; revision 3, F0 at `f1070cf`)

**Product.** `docs/design/analysis/pa-drive-ts012.md` revision 3 (blob `48c0ed44`), section R3 "A5 as adopted (governs for A5)", with the checker `hardware/sim/tx-pa/run_a5_r3.py` (blob `40941ee0`; it imports `run_pa.py` blob `44769c45`, reviewed at INSP-114 iteration 3) and the seven runs `results/2026-09-29-r3-d6`, `-d7`, `-k1`, `-s2`, `-p4`, `-p5`, `-s3`. Frozen at F0 by `f1070cf` (68 files). Sections 1 to 9 stay the revision 2 text that INSP-114 approved at iteration 3 (`f5960d3`); this record reviews them only where revision 3 changed them (sections 2 and 4.4, the INSP-114 lien finding-11) or where R3 relies on them.

**Scope and question (rule C7, cases named).** The PDR work plan revision 7 section 3.0 row 21 leaves WP-PDR-21 these A5 items: the D-7 select-on-test pad and the 17 mW reading characterization; the drive-chain rerun with C7, C10 and the D-13 drive bandpass; p1 to p3 with the chosen LPF build (D-14) and the read feed resistance; and the REQ-SYS-012 and REQ-SYS-144 rows that CR-018 carries (rule C10: this record must be APPROVED before S1). The cases taken from the governing texts are in the per-case table below: TS-012 row WP-PDR-21 and D-13 ("module input 10 to 30 mW at every corner"); D-7 ("level read at about 17 mW within +/-1.0 dB"); D-8 and Si5351 Table 7 (CLK1 load at most 15 pF); TS-012's 3f criterion at the GVA-84+ input; D-9 ("VGG 3.30 to 3.50 V at 6.4 V and the open-loop module output at most 8 W at 8.4 V from a -10 C start"); C2 (drain feed at most 0.35 ohm) and C7; REQ-SYS-012 as baselined ("5 W step within +/-1 dB (TBR) into 50 ohm over its transmit range at 6.4-8.4 V pack", so 144, 146 and 148 MHz and both pack ends) over REQ-SYS-114 (-10 to +45 C); and the two proposed CR-018 values.

**Independence (rule C4).** This invocation authored no part of the note, its earlier revisions, `run_a5_r3.py`, `run_pa.py`, the decks, the digitizers, TS-012 or the INSP-114 record, and edited no product file. It wrote only scratch files under its own scratchpad.

**Search first (rule C3, charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any grep (queries: "WP-PDR-21 pa-drive-ts012 revision 3 A5 review checklist record"; "RA07M1317M absolute maximum ratings Pout 10 W VGG 3.5 V stability 8 W 4:1 load"; "Coilcraft 1812SMS Midi Spring datasheet Document 184 Q SRF 47N DMP3099L DS36081 MF-R300 AO3400A datasheet file"). `grep` and `sed` then only pinned lines in files those searches or the brief named (the note, `run_a5_r3.py`, `run_pa.py`, the plan, TS-012, `requirements.json`, `tpm.json`, `hazards.json`, the status notes, `lpf-ts012.md`, `tx_spur_filters.cir`, `tools/validate_docs.py`). The rustos tree was not read.

**External reads (2026-09-29, public vendor PDFs through the web-fetch tool, no login or form; each file's SHA-256 equals the prefix the note and README quote).** Diodes DMP3099L DS36081 Rev. 5-2 (`06f30303...`); AOS AO3400A Rev 3.1 (`9c60d0b6...`); Bourns MF-R series REV. AR 09/26 (`d22f0f06...`); Coilcraft Document 184-1 (`e8ce1b27...`). Text extracted with pdftotext.

## Readiness (R1 to R6)

| # | Result | Evidence |
|---|---|---|
| R1 | Met | `git ls-tree f1070cf` gives every `product_files` blob; `git diff f1070cf HEAD -- docs/design/analysis/pa-drive-ts012.md hardware/sim/tx-pa` is empty at HEAD `6eb014c`. No product blob is on a `cr/` branch |
| R2 | Met | `run_a5_r3.py all --expect` from a `git archive f1070cf` export (below): exit 0, LTspice only through the export's `tools/ltspice-batch.sh` |
| R3 | N/A | The product holds no JSON file under a schema. `tools/validate_docs.py` exits 0 at HEAD, and on this record in a scratch worktree |
| R4 | Met | The author summary and note R3.1 to R3.10 state the questions, inputs with classes (R3.2, R3.5), results, limitations (R3.9), the proposed values (R3.7) and the tools (Evidence status row) |
| R5 | Met with finding-7 | No `TBD` in section R3. The two REQ-SYS-144 TBRs the note introduces have no proposed `tbr` object (finding-7) |
| R6 | Met | The eight cited PNGs exist beside their decks (plus `power_a5_clampb_temperature.png`) |

## Re-run from an export of the freeze commit (CK-ANA-C4)

`git archive f1070cf | tar -x` into the reviewer's scratchpad; then, from the export root, `CWHT_LTSPICE_LOCK_WAIT=14400 /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_a5_r3.py all --expect` (no `CWHT_PA_REPLOT`: every deck was solved again by LTspice through the export's wrapper).

- **Exit status.** `all` ran d6, d7, k1, s2, p4, p5 and s3 in 1 h 23 min (the wrapper's lock was shared with other runs); the checker printed every verdict of note section R3.10 unchanged, then "--expect: 0 verdict(s) differ from the analysis record" and exit status **0**, as the note and README state. Every re-run `.log` first line is "LTspice 26.0.2 for MacOS" (26 logs).
- **Decks.** Every regenerated deck is byte-identical to its committed blob (`drive_a5_bpf.cir`, `coax_a5_bpf.cir`, `tstep_a5_bpf.cir`, `probe_rf.cir`, `probe_dc.cir`, both `power_a5_design.cir`), and the wrapper's deck SHA-256 equals the README prefixes (for example `b527e31c4c91cb8b` for d6).
- **Values.** Every re-run `result.json` equals the committed one in every number and string, apart from the wrapper provenance lines (elapsed time, run directory); every `result.md`, `corners.json`, `coax_a5_bpf_steps.json` and `verdicts.json` is byte-identical; all nine PNGs are byte-identical to the committed blobs (so the renders opened at `f1070cf` are the re-run renders).
- **Kept .raw files (CR-017 C2).** The author's five kept `.raw` files in the working tree match their `raw.sha256` lines (`shasum -a 256 -c`: 5 of 5 OK). The re-run `.raw` files differ from them only in the ASCII header (deck path and run date); their binary data sections are byte-identical (5 of 5), so the manifests identify the data the checker read.
- **Reviewer variant for finding-1 (scratch only, not a product change).** In a copy of the export, `run_s2`'s `band()` was changed to the one-sided deviations from the 146 MHz selection point (+0.360 / -0.777 dB per unit) and s2, p4, p5 and s3 were run again. s2: 10.45 to 26.02 mW at the M2 bound (PASS, underdrive margin +0.19 dB); **at the +/-1.0 dB allocation 9.6 to 28.3 mW: FAIL**; the variant `sot_band.png` was opened (the lower edge crosses 10 mW at about +/-0.83 dB). p4, p5 and s3 on the 10.45 mW floor: the scenario B basis at 6.4 V moves from 2.819 to 2.814 W (-2.639 to -2.646 dB from 5 W with the terms), the proposed -2.7 dB limit line still lies under it (smallest margin +0.02 dB at 7.8 V, against +0.03 dB), and the D-9 figures move by at most 0.01 dB; the variant `req012_basis.png` was opened. So finding-1 changes the REQ-SYS-144 value, not the REQ-SYS-012 one.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a revision 3 result)

| Note row (R3.2, R3.5) | Source read by the reviewer | Agreement |
|---|---|---|
| D-13 bandpass: 7.5 pF / 47 nH parallel 16 pF / 2.4 pF / 47 nH parallel 16 pF / 7.5 pF | `hardware/sim/freq/tx_spur_filters.cir` line 59 `.param Lr=47n Csb=7.5p Crb=16p Ccb=2.4p`; `spurs-ts012.md` option C10 | Yes; the d6 deck `bpf_text` places the parts in that order |
| 1812SMS-47N: 47 nH, G 2 %, Q typ 135 / min 100 at 150 MHz, SRF min 2.1 GHz, DCR max 5.6 mohm, TCL +5 to +70 ppm/C | Coilcraft Document 184-1 (revised 12/02/21) table row "1812SMS-47N_L_ 47 5,2 135 100 150 2.1 5.6 3.0"; TCL line | Yes. The deck's 0.12 pF parallel capacitance is 1/((2 pi 2.1 GHz)^2 47 nH) = 0.122 pF (hand check) |
| 68N and 82N exist in G and J; Q min 100; SRF 1.5 and 1.3 GHz (C7) | Same table rows | Yes: C7 PASS stands |
| Bandpass capacitor tolerances: 16 pF G; 7.5 and 2.4 pF B (+/-0.1 pF) | Class E in the note (tolerance codes, parts read at the ordering gate) | Labelled as an assumption; no datasheet to check. Tempco not included (finding-8) |
| DMP3099L RDS(on) max 99 mohm at VGS -4.5 V (ID -3.0 A), 65 mohm at -10 V (ID -3.8 A) | DS36081 Rev. 5-2, electrical characteristics table and front-page summary | Yes. A pair at twice the -4.5 V maximum (0.198 ohm) bounds a 5.9 to 6.4 V gate drive: reasonable |
| AO3400A RDS(on) max 32 mohm at 4.5 V (ID 5 A), 26.5 mohm at 10 V; typ 19 and 18 mohm | AOS Rev 3.1 July 2023, page 2 table | Yes |
| MF-R300 Rmin 0.020, Rmax 0.05, R1max 0.08 ohm; Ihold 3.00 / 2.49 / 2.31 / 2.04 / 1.83 A at 23 / 40 / 50 / 60 / 70 C | Bourns MF-R REV. AR 09/26, electrical table row "MF-R300 30 40 3.00 6.00 0.020 0.05 0.08" and thermal derating row | Yes |
| Feed totals 0.238 / 0.345 / 0.452 ohm at 25 C, lever 0.314 ohm | Hand sum of the FEED3 table and the Molicel cells 0.04 to 0.06 ohm: low 0.04 + 0.038 + 0.020 + 0.02 + 0.110 + 0.01 = 0.238; bound 0.06 + 0.064 + 0.080 + 0.04 + 0.198 + 0.01 = 0.452; lever 0.452 - 0.198 + 0.06 = 0.314 | Yes |
| D-14 output loss 0.84 / 1.03 / 1.86 dB, lever 1.34 dB | `lpf-ts012.md` revision 2 (`92e3805`) lines 102 and 103: r13 1.76 / 0.93 / 0.74 dB, r14 1.24 dB; plus the 0.1 dB relay | Yes |
| Fluke 174 DC volts +/-(0.15 % + 2 counts); 10 Mohm input (170-series nominal, not read) | Status note 2026-09-28 section 2 ("DC volts plus or minus (0.15 % + 2)") | Yes. The 10 Mohm is labelled as not read; the reviewer checked that a +/-3 % error in the 11:1 current ratio (meter resistance and the 1 % 1.00 Mohm resistor) moves the M1 reading by only +/-0.007 dB, so it needs no term |
| RA07M1317M: Pin 30 mW maximum, stability Pin 10 to 30 mW and Pout up to 8 W, Pout 10 W maximum (at VGG 3.5 V or less), 6.5 W minimum at 7.2 V | Note section 3 row, verified against the datasheet at INSP-114 iterations 1 to 3; `pa-device-candidates.md` F8 | Yes. The datasheet gives no maximum output: the typical curve is not an upper bound (finding-2) |
| REQ-SYS-012 and REQ-SYS-144 "Before" text | `docs/requirements/sys/requirements.json` descriptions | Verbatim |
| TPM-015 red threshold "the 5 W step unreachable at the cutoff voltage" | `docs/plan/tpm.json` TPM-015 `threshold_red` | Verbatim |
| D-9 criterion text | TS-012 line 1045 (section 8.14 D-9 row) | Yes; the text sets no module grade, so it applies to every unit (finding-2) |

## Checklist answers

### A. Question, scope and traceable inputs
- **CK-ANA-A1 Yes.** R3.1 states five questions and the Serves row names CR-018, REQ-SYS-012, 144, 114, D-7 to D-14, TPM-015, TPM-004, HZ-001, HZ-003; every id exists (`requirements.json`, `tpm.json`, `hazards.json`, TS-012 section 8.14).
- **CK-ANA-A2 No (finding-10, Minor).** The design data are identified (TS-012 revision 7 section 8.14, `spurs-ts012.md` C10, `lpf-ts012.md` r13 at `92e3805`). But the note, drafted before the S1 disposition of the A5 CR set and carrying CR-018 rows, is not marked AT RISK (A5 CRs) as rule C13 requires; `thermal-budget.md` and `frequency-budget.md` carry the flag.
- **CK-ANA-A3 Yes.** Every R3.2 and R3.5 row has a class (D, G, E) and a source; the estimates are labelled.
- **CK-ANA-A4 Yes.** Table above; no disagreement with a source.
- **CK-ANA-A5 Yes, with finding-2.** Assumptions are stated with direction (R3.9, R3.2). The one that sets the ceiling verdicts, that the typical module is the strongest unit, is not stated (finding-2).
- **CK-ANA-A6 Yes.** R3.8 routes every consequence as a request (R3-1 to R3-5); the note edits no requirement, TPM or hazard file.

### B. Model validity
- **CK-ANA-B1 Yes.** The bandpass, the probe and the power path are modelled with their parasitics; simplifications are stated (R3.9 items 1 to 6, section 6).
- **CK-ANA-B2 Yes.** The only vendor-model stand-in is the HSMS-280x surrogate for the 1N5711, stated as such with the parameter ranges (R3.9 item 1).
- **CK-ANA-B3 Yes.** The s3 replica check (7.900 against 7.905 W; 3.632 against 3.634 W) and the d7 numerical check; the probe method is validated against the LTspice periodic steady state over 8 diode sets.
- **CK-ANA-B4 Yes.** The 250 ns window was checked against 400 ns and a 10 ps step (d7: 0.0028 dB power, 0.040 dB 3f); the probe transient averages the last 4 of 30 periods with a 25 ps step and a bracketed root per case (0 unbracketed of 240).
- **CK-ANA-B5 Yes (independent checks).** (1) An ideal-diode peak detector solved in Python by direct time-domain averaging of the diode current (Is 3e-8 A, n 1.08, 10 Mohm; no LTspice) gives the M0 error -0.68, -0.54 and -0.43 dB at 10, 17.3 and 30 mW, against k1's M0 range -0.73 to -0.42 dB and the plot's S0 point at about -0.56 dB at 17.3 mW (agreement within 0.02 dB). (2) The feed sums by hand (inputs table). (3) The coil parallel capacitance by hand (0.122 pF). (4) The s2 band recomputed per unit from `corners.json` (finding-1). (5) The scenario B clamp trade recomputed with the note's own Python replica for a stronger-than-typical module (finding-2); the replica reproduces the deck's 4.42 W at the 3.120 V top.
- **CK-ANA-B6 No (findings 1 and 2, Major).** The s2 frequency term is the half-span, not the one-sided deviation from the 146 MHz selection point; the ceiling figures carry neither the module's upper spread nor the graph-read uncertainty that the note itself uses for the reach (CLOSURE_UNC, +/-0.07 dB).

### C. Tools
- **CK-ANA-C1 Yes.** LTspice 26.0.2; every re-run `.log` first line is "LTspice 26.0.2 for MacOS".
- **CK-ANA-C2 Yes.** TV-014 is accredited (ACC-LTSPICE-001); the Python checker has no TV record and the note marks every figure developer evidence and estimate.
- **CK-ANA-C3 Yes.** One command, `run_a5_r3.py all --expect`; netlists only; one analysis per deck.
- **CK-ANA-C4 Yes.** Re-run section above.
- **CK-ANA-C5 Yes.** The wrapper's lock, time-out and path-length limits were respected (the run waited on the lock while other agents ran).

### D. Units, arithmetic, consistency
- **CK-ANA-D1 Yes.** mW and dBm, dB and dBc, W at the SMA and at the module are kept apart; P = Vpk^2/100 for 50 ohm is right.
- **CK-ANA-D2 No (findings 4, 5 and 6, Minor).** Every R3 table value equals the committed and the re-run `result.json` (the reviewer compared the p4 and p5 `by_tc` values, the d6 and d7 summaries, k1 `err_db` and the s2 `band` with the note). Three text defects: the p4 nominal row's "3.97 W in every case from 6.9 V" (finding-4); the REQ-SYS-012 rationale sentence quotes the p4 figures beside the scenario B text (finding-5); stale section references and the k1 plot's revision 2 break-even (finding-6).
- **CK-ANA-D3 Yes.** The proposed low limit is rounded toward the limit (x_db rounded up to the next 0.1 dB; the -1 dB start voltage rounded up to the next 0.1 V).
- **CK-ANA-D4 Yes.** `REQ012_LO` 3.972 W (5 x 10^-0.1 = 3.9716, rounded to the stricter side), `A5_PIN_MIN_MW` / `A5_PIN_MAX_MW` 10 / 30, `A5_MOD_STAB_W` / `A5_MOD_MAX_W` 8 / 10, `H3_MIN_DBC` 25 carry their sources in comments.

### E. Results, margins, proposed values
- **CK-ANA-E1 Yes.** The limits are quoted with ids (REQ-SYS-012, D-9, D-13, Table 7, TPM-015).
- **CK-ANA-E2 Yes.** Margins are result minus limit in dB, signs right; TPM-015's red threshold is compared (R3.7).
- **CK-ANA-E3 No (findings 1 and 2, Major).** The s2 underdrive margin is reported as +0.40 dB; per unit it is +0.19 dB, and at the proposed +/-1.0 dB allocation it is -0.17 dB, reported as a PASS. The open-loop ceiling margins (7.92 W against 8 W, +0.04 dB; 9.94 W against 10 W, +0.03 dB) are smaller than the note's own +/-0.07 dB graph-read term and do not cover a unit above typical, and the note does not say so.
- **CK-ANA-E4 Yes.** Every acceptance value is a `verdict()` call; `all` exits 1 on a failing criterion and 2 on a failing check; `--expect` exits 3 on a changed verdict.
- **CK-ANA-E5 No (finding-7, Minor; the values themselves are findings 1 and 2).** R3.7 states the ids, values and margins, and does not edit the requirement file. It does not propose the `tbr` object for the two new REQ-SYS-144 TBRs, nor say that REQ-SYS-012's `tbr.plan` ("TS-003 ... and TS-006 ... at PDR show the tolerance by analysis") names two studies the plan no longer writes, or propose the replacement plan text.
- **CK-ANA-E6 N/A.** No TPM current best estimate is proposed; R3-5 sends figures to WP-PDR-29.
- **CK-ANA-E7 Yes.** REQ-SYS-012 and 144 are Test-method requirements; the note claims supporting pre-build evidence only (proposed verification note: "Pre-build: Analysis ... Post-build: Inspection ... then TC-SYS-096").

### F. Every case named
- **CK-ANA-F1 Yes.** Per-case table: 144, 146 and 148 MHz; 6.4 and 8.4 V (and every 0.05 V between); -10, +25 and +45 C with the key-down and start-of-key-down states; the 5 W step (the only step REQ-SYS-012 names); the D-9 open-loop fault case.
- **CK-ANA-F2 Yes.** The ALC-failed open-loop state (HZ-001) and the steady key-down at the hot bound are analysed; the polyfuse trip at the hot corner is sent to WP-PDR-24 (R3-3).
- **CK-ANA-F3 No (findings 1, 2 and 3).** The worst combination for the underdrive side of the select-on-test band (a unit whose 148 MHz drive sits 0.78 dB under its 146 MHz selection point) is not taken (finding-1); the strongest-unit combination for the ceilings is not taken (finding-2); the "any coax length" pad range uses the nominal bandpass only (finding-3).
- **CK-ANA-F4 Yes.** The s2 sensitivity table and plot (reading 0.25 to 2.0 dB), the clamp trade table and the coverage sets of s3 show the sensitivities of the near-limit results.

### G1. Simulation decks and checkers
- **CK-ANA-G1-1 Yes.** Decks, checker and plots sit in `hardware/sim/tx-pa/` and its run folders, named per run.
- **CK-ANA-G1-2 Yes.** One `.tran` per drive and probe deck, one `.dc` per probe DC and power deck; no NC_ nets.
- **CK-ANA-G1-3 Yes.** 50 ohm source and load at the probe, the Si5351 Thevenin source and CLK1 load as revision 2, the bandpass with parasitics; the module input as 50 ohm, which the datasheet's Pin definition (ZG 50 ohm) supports (section 6 item 5).
- **CK-ANA-G1-4 Yes.** Every figure is read from the `.raw` by spicelib; a missing `.raw` raises.

### G5. Cascade
- **CK-ANA-G5-1 Yes.** Si5351, coax, bandpass, pad, GVA-84+, 3 dB pad, module, LPF and relay are in signal order with sourced gains and losses.
- **CK-ANA-G5-2 Yes.** Power is carried at one reference plane per result (module input for drive; SMA for output).
- **CK-ANA-G5-3 Yes.** 144, 146 and 148 MHz for drive and power; 3f for the drive filter.

### G7. Worst-case and tolerance
- **CK-ANA-G7-1 Yes.** Extreme-value corner sweeps; worst-case sum and RSS both given for the s2 band.
- **CK-ANA-G7-2 No (finding-8, Minor).** The in-service bandpass drift takes the coil's TCL (+70 ppm/C) and sets the C0G capacitors' coefficient to zero; C0G is 0 +/-30 ppm/C.

### H. Hazards, risks, records
- **CK-ANA-H1 Yes, with finding-2.** HZ-001 gets the open-loop figures through R3-1 (7.91 W and 9.94 W); those figures are for the typical module only (finding-2).
- **CK-ANA-H2 No (finding-9, Minor).** No risk-register request carries the revision 3 figures.
- **CK-ANA-H3 Yes.** Change log row 3 and section 9.0; the INSP-114 lien finding-11 is fixed as stated: section 2 now says "at 6.4 V" and section 4.4 "fails, or passes by +0.02 dB before the unmodelled terms"; p4 and p5 check the thermal law at every pack voltage (re-run: 7.63e-06 K and 1.53e-05 K). Finding-11 of INSP-114 is closed by this revision.

### I. Visual closure
- **CK-ANA-I1 Yes.** Nine PNGs opened with the Read tool (the committed blobs; the re-run renders are byte-identical): `drive_a5_bpf_corners.png`, `coax_length_bound_bpf.png`, `probe_reading_error.png`, `sot_band.png`, `power_a5_design_sma.png`, `power_a5_design_temperature.png`, `power_a5_clampb_sma.png`, `power_a5_clampb_temperature.png`, `req012_basis.png`.
- **CK-ANA-I2 No (finding-6, Minor).** Axes, units, limits and legends are present and the marked values agree with the checker (for example the s2 bar 0.57 + 0.38 + 0.64 + 0.39 = 1.98 dB; the s3 limit line just under the scenario B basis band at 6.4 V). The k1 plot draws the revision 2 break-even (+/-1.54 dB, hard-coded default) where revision 3's is +/-1.05 dB (+/-0.83 dB on the underdrive side after finding-1).

### J. Software assurance
N/A: criticality neither.

**ITEMS N/A:** CK-ANA-E6; CK-ANA-G2, G3, G4, G6 (analysis_kind); CK-ANA-J1 to J3 (criticality neither).

## Per-case results

| Case | Condition | Governing id and limit | Result (checker, confirmed by the re-run) | Margin | Uncertainty | Reviewer re-check | Findings |
|---|---|---|---|---|---|---|---|
| C-1 | Fixed 18 dB pad, 8100 corners, 144 / 146 / 148 MHz, coax 5 to 15 cm, 25 C | TS-012 D-13: module input 10 to 30 mW at every corner | 5.5 to 39.1 mW; 1356 under 10 mW, 565 over 30 mW: FAIL | -2.6 dB under, -1.15 dB over | estimate | re-run: same | none |
| C-2 | Same corners | Si5351 Table 7, CLK1 load at most 15 pF | -0.5 to 11.0 pF equivalent: PASS | +4.0 pF | layout estimate | re-run: same | none |
| C-3 | Same corners | TS-012: 3f at the GVA-84+ input at most -25 dBc | -33.8 dBc: PASS | +8.8 dB | estimate | re-run: same | none |
| C-4 | Same corners | GVA-84+ input below +13 dBm | -6.2 dBm: PASS | +19.2 dB | - | re-run: same | none |
| C-5 | Coax 0.5 to 70 cm, extreme part corners, fixed pad | D-13 overdrive at any length | 38.7 mW: FAIL | -1.1 dB | estimate | re-run: same | finding-3 (nominal bandpass only) |
| C-6 | Level reading at 10 / 17.3 / 30 mW, 146 MHz, 8 diode sets, harmonics, DC at 20 to 30 C | D-7 / proposed REQ-SYS-144: within +/-1.0 dB | +/-0.64 dB (M2, worst-case sum): PASS | +0.36 dB | surrogate diode (R3.9 item 1) | re-run: same; independent M0 check agrees within 0.02 dB | none |
| C-7 | Select-on-test, in service, reading +/-0.64 dB, pad chosen at 146 MHz | D-13 / D-7: 10 to 30 mW in service | note: 11.0 to 27.3 mW PASS; per unit: 10.45 to 26.0 mW, still PASS | +0.19 dB under (note +0.40), +0.62 dB over | estimate | recomputed per unit from `corners.json` | finding-1 |
| C-8 | Select-on-test at the proposed +/-1.0 dB allocation | Proposed REQ-SYS-144 value; 10 to 30 mW | note: 10.1 to 29.6 mW PASS; per unit: 9.62 to 28.3 mW, FAIL | -0.17 dB under | estimate | recomputed per unit | finding-1 |
| C-9 | Drain feed, every part at its datasheet maximum, 25 C part temperature | TS-012 C2: at most 0.35 ohm | 0.452 ohm: FAIL | -0.102 ohm | datasheet values | hand sum: same | none |
| C-10 | 1812SMS 47N, 68N, 82N in G | C7: values exist | exist: PASS | - | datasheet | Document 184-1 read: same | none |
| C-11 | Open loop, highest corner, -10 C start, 6.4 to 8.4 V, D-9 as specified | D-9: module at most 8 W | 7.92 W (7.90 W at 8.4 V), typical module: PASS | +0.04 dB, typical module only | +/-0.07 dB graph read; module spread above typical not bounded | re-run: same | finding-2 |
| C-12 | Same, clamp scenario B | Module maximum rating 10 W | 9.94 W (9.90 W at 8.4 V), typical module: PASS | +0.03 dB, typical module only | as C-11 | re-run: same | finding-2 |
| C-13 | 6.4 V, nominal corner, every key-down case, 144 to 148 MHz | REQ-SYS-012 lower bound 3.97 W | 3.44 W (p4), 3.48 W (p5): FAIL | -0.62 / -0.57 dB | +/-0.07 dB graph read and the unmodelled terms (-0.15 dB) | re-run: same | none |
| C-14 | 6.4 V, lowest corner, typical module, LPF at most its MC 99th percentile, every key-down case | REQ-SYS-012 lower bound 3.97 W | 2.76 W (p4), 2.82 W (p5): FAIL | -1.59 / -1.49 dB | as C-13 | re-run: same | none |
| C-15 | 8.4 V, same basis, every key-down case | REQ-SYS-012 lower bound 3.97 W | 2.07 W (p4): FAIL; 4.42 W (p5): PASS | -2.83 / +0.46 dB | as C-13; p5 rests on the typical module setting the clamp | re-run: same; replica 4.42 W | finding-2 |
| C-16 | Proposed REQ-SYS-012 limit line (5 W -2.7 dB at 6.4 V to -1 dB at 7.8 V) against the scenario B basis with the terms | Proposed CR-018 value | limit under the basis at every 0.05 V: PASS | +0.06 dB at 6.4 V; smallest +0.03 dB at 7.8 V | as C-15 | re-run: same; with a module 0.3 dB above typical the 8.4 V end misses 3.97 W (3.96 W with the terms) | finding-2 |
| C-17 | Pack current, ALC at its top, +45 C key-down | MF-R300 hold 2.04 to 2.2 A at 55 to 60 C (WP-PDR-24, request R3-3) | 2.48 A (p4), 2.70 A (p5): negative trip margin | -0.28 to -0.66 A | estimate | re-run: same | none |
| C-18 | CLK1 swing at the prescaler tap, every d6 corner | WP-PDR-20 input (request R3-2) | 1.33 to 3.40 Vpp | 0.13 V total across 0.8 to 2.0 V | estimate | re-run: same | none |

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-B6, E3, F3; E5 (REQ-SYS-144 value) | Note R3.4 s2 table and text, R3.7 REQ-SYS-144 rows, R3.8 C1 row, R3.10 s2 rows; `run_a5_r3.py` `run_s2` `band()` (`half = fspan / 2 + ...`) | The pad is chosen at 146 MHz (`need` uses `v[146e6]`; s2 `result.md` "the pad is chosen at build at 146 MHz"), but the frequency term is half of each unit's 144 to 148 MHz span, applied symmetrically. Per unit, from the committed d6 `corners.json`, the drive rises at most 0.36 dB above its 146 MHz value and falls up to 0.78 dB below it (unit rsrc 25 ohm, gain 22.9 dB, P1dB high, source low, 15 cm, bandpass "high, coupling low", Q 135: 11.08 / 10.73 / 9.95 dBm at 144 / 146 / 148 MHz). With the one-sided terms the in-service band is 10.45 to 26.0 mW, so the underdrive margin is +0.19 dB, not +0.40 dB. At the +/-1.0 dB allocation that R3.7 proposes as the REQ-SYS-144 value, the floor is 9.62 mW (-0.17 dB): the s2 verdict "10 to 30 mW at the +/-1.0 dB reading allocation" is a FAIL, not a PASS, and the underdrive break-even is +/-0.83 dB, not +/-1.05 dB. The proposed REQ-SYS-144 value is therefore not supported as written. **Fix:** use the one-sided deviations from the selection frequency in s2 (and in `sot_band.png` and its RSS); then either (a) keep 17.3 mW and propose a reading uncertainty of at most +/-0.8 dB (TBR), or (b) move the target to about 18.2 mW (the centre of the one-sided band: 10.1 to 29.7 mW at +/-1.0 dB, +0.04 / +0.05 dB; 11.0 to 27.4 mW at +/-0.64 dB), and propose that target; state the selection frequency (146 MHz) in the REQ-SYS-144 clause and in D-7; rerun p4, p5 and s3 on the new drive band (the floor moves from 10.97 to 10.45 mW under (a), which the reviewer's variant run shows moves the REQ-SYS-012 basis by only -0.01 dB; it stays about 11.0 mW under (b)), and restate R3.4, R3.7, R3.8 and R3.10 | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A5, B6, E3, F3, H1 | Note R3.2 VGG clamp rows, R3.6 (p4 bullets, clamp trade table, p5 table, REQ-SYS-012 basis and proposed delta), R3.7 REQ-SYS-012 and TPM-015 rows, R3.8 R3-1, R3.9 item 3, R3.10 p4 and p5 ceiling rows; `run_a5_r3.py` `clamp_top_curve` and `clamp_trade` (`py_module_w(..., True, "coldhi", ...)`: typical module) | The clamp top is set so that the highest corner makes 7.9 W (D-9) or 9.9 W (scenario B), and that corner uses the typical module curve. The RA07M1317M datasheet gives a 6.5 W minimum (1.0 dB under the 8.2 W typical at 7.2 V) and no maximum, so a unit above typical is not bounded; D-9's text ("open-loop module output at most 8 W") sets no grade. The resulting margins, +0.04 dB to 8 W and +0.03 dB to the 10 W maximum rating, are also inside the note's own +/-0.07 dB graph-read term (`CLOSURE_UNC`), and the note does not say so; R3.9 item 3 calls the reach an upper bound but says nothing of the ceiling. The scenario B recommendation (R3.7, R3-1) and the proposed REQ-SYS-012 delta rest on this corner. With the note's own replica (reviewer run): if the 10 W ceiling must hold for a unit x dB above typical, the lowest basis unit at 8.4 V (LPF MC 99 %, 0.03 V window, with the -0.15 dB terms) is 4.27 W at x = 0, 4.08 W at 0.2 dB, 3.96 W at 0.3 dB, 3.77 W at 0.5 dB and 3.33 W at 1.0 dB. The proposed "-1 dB from 7.8 V" therefore fails for any upper spread of about 0.3 dB or more, and at a spread mirroring the datasheet minimum (1.0 dB) scenario B reaches no more than D-9 as specified. The same gap makes R3.7's "5 W is unreachable for every unit in every case" at 6.4 V a statement about the modelled units only. **Fix:** state the assumption and bound it: carry an upper module spread (an estimate with its basis, or the mirror of the datasheet minimum) and the graph-read term in the ceiling cases of p4, p5 and the clamp trade, then restate the D-9 and scenario B ceilings, the reach, the proposed REQ-SYS-012 delta and the HZ-001 figures; or make the ceiling a per-unit build step (R3-1 option (c): an open-loop output check or clamp trim at build, added to the REQ-SYS-144 clause), and propose the REQ-SYS-012 value on that basis | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-F3 | Note R3.3 bullet "The coax length hardly matters"; `deck_d6(mode="d7")` (`bcases = BPF_CASES[:1]`) | d7 sweeps every coax length with the nominal bandpass only (both Q), so its "13.90 to 21.92 dB at any length" pad range and "the revision 2 note that the set grows by one pad past 15 cm no longer applies" do not cover the four bandpass tolerance cases; d6, with them, already needs 13.82 to 21.87 dB at 5 to 15 cm (and 39.1 mW against d7's 38.7 mW). **Fix:** add the bandpass cases to d7, or qualify the claim to the nominal bandpass | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-D2 | Note R3.6 REQ-SYS-012 basis table, row "nominal corner", D-9 column ("8.4 V: 3.50 W; 3.97 W in every case from 6.9 V"); `run_p4` `reach()` and `s3_rows` `pack_v_reaches_3v97_worst` | `reach()` returns the first pack voltage at which a curve reaches 3.97 W, not the voltage above which it stays there. Under D-9 as specified the nominal corner rises above 3.97 W and falls back under it (3.50 W at 8.4 V), so "3.97 W in every case from 6.9 V" is wrong; s3 `result.md` prints the same. `s3_proposal` already tests the sustained condition (`ok[j:].all()`). **Fix:** use the sustained test in `reach()`, or report the voltage interval | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-D2 | Note R3.7 REQ-SYS-012 "Rationale sentence to replace" | The replacement rationale quotes 4.26 W nominal and 2.76 W lowest at 6.4 V, the p4 (D-9 as specified) figures, beside the scenario B requirement text that the record recommends (p5: 4.31 W and 2.82 W). The sentence also reads "4.26 (25 C key-down) W". **Fix:** give the rationale per clamp option, with the figures of that option | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-D2, I2 | Note R3 introduction ("against the verdict list of section R3.9"); `run_a5_r3.py` docstring ("the list of the analysis record section 8.1"); `plot_k1` (`res.get("break_even_db", 1.54)`) | The verdict list is section R3.10, and the script's `EXPECTED` comment says so while its docstring names section 8.1. The k1 plot draws the revision 2 break-even (+/-1.54 dB) because `break_even_db` is never set in the k1 result; revision 3's is +/-1.05 dB (s2), +/-0.83 dB on the underdrive side after finding-1. **Fix:** correct the two references; draw the s2 break-even on the k1 plot or drop the line | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-E5; readiness R5 | Note R3.7 | REQ-SYS-144 has `tbr: null`; the proposed clause introduces two TBRs (17.3 mW, +/-1.0 dB) with no proposed `tbr` object (owner, plan, close_by). REQ-SYS-012's `tbr.plan` names TS-003 and TS-006, which plan revision 7 section 3.0a no longer writes; the note does not say which step of that plan it executes or propose the replacement plan text for CR-018. **Fix:** add both to R3.7 | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-G7-2 | Note R3.4 s2 drift row; `run_s2` (`dl = TCL_MAX_PPM ...`, "C0G about 0") | The bandpass drift takes only the coil TCL (+70 ppm/C over 64 K). C0G capacitors are 0 +/-30 ppm/C; in the worst direction the resonance moves about 1.4 times as far, adding about 0.04 dB to the 0.09 dB term. No verdict changes. **Fix:** include the C0G coefficient or state why it is excluded | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-H2 | Note R3.8 requests | Revision 3 changes the figures behind the TS-012 section 7.1 A5 risk row and the revision 2 section 7.1 risk-register request (C2 now a datasheet FAIL; the basis at 6.4 V -1.49 to -1.59 dB; the polyfuse trip margin negative at the hot corner), but R3.8 sends no request to the WP-PDR-18 risk writer. **Fix:** add a risk-register request with the revision 3 figures | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-ANA-A2 | Note header (Status and Evidence status rows) | The note is drafted before the S1 disposition of CR-003 revision 4, CR-006 revision 3 and CR-018, and supplies CR-018 rows, but it carries no AT RISK (A5 CRs) flag (plan rule C13), unlike `thermal-budget.md` and `frequency-budget.md`. **Fix:** add the flag and the rule C8 re-check note | Open | Pending | |

## Values proposed (rule C10)

- **REQ-SYS-144 drive-pad clause, 17.3 mW (TBR) read within +/-1.0 dB (TBR): not supported** as written (finding-1). With the one-sided band, +/-1.0 dB lets a unit run at 9.62 mW; either +/-0.8 dB at 17.3 mW or +/-1.0 dB at about 18.2 mW is supported by the same runs, with the selection frequency stated.
- **REQ-SYS-012, 5 W +1/-2.7 dB (TBR) at 6.4 V rising to +1/-1 dB (TBR) from 7.8 V, with clamp scenario B: not supported** (finding-2). It holds for the typical module setting the clamp, and fails at the 8.4 V end for a module about 0.3 dB or more above typical. The D-9-as-specified finding (no delta of this form holds; about +1/-4.0 dB) stands on the typical module and is not weakened by finding-2.
- Both values are for the owner at S1 only after this record is APPROVED (rule C10); the owner's alternative of TS-012 follow-on decision 2 (keep +/-1 dB and decide on the TC-SYS-011 bench reading) is unaffected.

## What is right and stays (for the author's fix round)

The D-13 drive results (C-1 to C-5), the closure of DR-PAD-1, the probe method and its +/-0.64 dB bound (C-6), the withdrawal of revision 2's DC-drop-only reading, the datasheet reads (C2 FAIL, C7 PASS), the p4 and p5 low-end figures at 6.4 V (C-13, C-14), the D-9 conflict at 8.4 V (it is 3.4 dB wide and does not depend on finding-2's direction: a stronger unit only deepens it), the requests R3-2 to R3-5, and the fix of the INSP-114 lien finding-11 were re-run and checked and need no change beyond the findings above.

## Verdict (reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/pa-drive-ts012.md@48c0ed44884d6529d59e5d91f42276c00db1e7d7, hardware/sim/tx-pa/run_a5_r3.py@40941ee0870f7c6d16931962dd0e72db003c45ef, hardware/sim/tx-pa/run_pa.py@44769c4579ef473795504837c96eace1159eca4f and the 38 run-folder blobs of product_files, at f1070cf85a5a5b8e9535e5028bee726ad593671a
FINDINGS:
- [Major] finding-1 CK-ANA-B6/E3/F3: s2 uses half the in-unit span about the 146 MHz selection point; per unit +0.36/-0.78 dB. Band 10.45 to 26.0 mW (underdrive +0.19 dB); at the proposed +/-1.0 dB allocation 9.62 mW, FAIL; REQ-SYS-144 value not supported.
- [Major] finding-2 CK-ANA-A5/B6/E3/F3/H1: the D-9 and scenario B ceilings use the typical module (no upper bound in the datasheet) with +0.04 / +0.03 dB margins inside the +/-0.07 dB graph read; the proposed REQ-SYS-012 delta fails at 8.4 V for a module 0.3 dB or more above typical.
- [Minor] finding-3 CK-ANA-F3: d7 "any length" pad range on the nominal bandpass only.
- [Minor] finding-4 CK-ANA-D2: "3.97 W in every case from 6.9 V" for the D-9 nominal corner, which falls to 3.50 W at 8.4 V.
- [Minor] finding-5 CK-ANA-D2: REQ-SYS-012 rationale quotes p4 figures beside the scenario B text.
- [Minor] finding-6 CK-ANA-D2/I2: stale references (R3.9, section 8.1); k1 plot shows the revision 2 break-even.
- [Minor] finding-7 CK-ANA-E5: no tbr objects for the REQ-SYS-144 TBRs; REQ-SYS-012 tbr.plan names unwritten studies.
- [Minor] finding-8 CK-ANA-G7-2: bandpass drift omits the C0G coefficient (about +0.04 dB).
- [Minor] finding-9 CK-ANA-H2: no risk-register request with the revision 3 figures.
- [Minor] finding-10 CK-ANA-A2: no AT RISK (A5 CRs) flag (rule C13).
ITEMS N/A: CK-ANA-E6; CK-ANA-G2, G3, G4, G6 (analysis_kind simulation-deck, cascade, worst-case); CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: REQ-SYS-144: 17.3 mW (TBR) within +/-1.0 dB (TBR) (not supported, finding-1); REQ-SYS-012: 5 W +1/-2.7 dB (TBR) at 6.4 V to +1/-1 dB (TBR) from 7.8 V, clamp scenario B (not supported, finding-2)
MEASUREMENTS: size=18 cases; inputs_checked=14; renders=9; turns=60; minutes=110; major=2; minor=8
```


## Iteration 2: delta verification of finding-1 and finding-2 (Major) (2026-09-30, HEAD `d0de188`)

**Scope (rule C1).** Iteration 2 is a delta on revision 4 of the note (`d0de188`). It verifies the fixes of the two iteration 1 Major findings case by case, re-runs every revision 4 run from a clean export, opens every cited plot, checks the new inputs against their sources, and raises new findings only where revision 4 introduced a defect. The unchanged revision 3 runs (d6, d7, k1) are inputs; their committed `corners.json` and `result.json` were read, not re-run.

**Independence (rule C4).** This invocation authored no part of the note or its revisions, the decks, the checkers, the digitizers or TS-012, and edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (queries: "WP-PDR-21 PA drive analysis review record checklist"; "review of pa-drive-ts012 revision 3 A5 finding-1 drive pad finding-2 clamp ceiling"; "TC-SYS-010 diode probe power characterization combined uncertainty 15 %"). `grep`, `sed` and `awk` then only pinned lines in files those searches or the brief named. The rustos tree was not read.

**Scope of the change.** `git diff d0de188~1 d0de188` on the note: 253 lines added, 4 changed (the header rows, the new section R4, one line under the R3 heading naming what R4 replaces, change-log row 4). Nothing else in R3 or sections 1 to 9 changed. The README gains the `run_a5_r4.py` row and the revision 4 runs table. The fix stays inside the two findings.

**Sources re-read by the reviewer (2026-09-29).**
- TC-SYS-010 (`docs/test_cases/sys/test_cases.md`): the probe is characterized "at 0.4, 0.5, 1, 2, 5 and 6.3 W", the correction curve covers "2 V to 25 V", and the acceptance is a combined power uncertainty of at most 15 percent at every listed power. The note's 15 % term is this criterion. Its use at 7 to 10 W (Vpk up to about 32 V) is outside the listed powers and the curve; the note says so (R4.8 request R4-1, R4.9 item 4).
- RA07M1317M datasheet as INSP-114 recorded it (10 W maximum rating; stability "Pout<=8W (VGG control)" at 4:1; Pin 30 mW maximum; 6.5 W minimum at 7.2 V; no maximum output). The note's claim that the datasheet gives no output maximum stands.
- Revision 3 inputs: `results/2026-09-29-r3-d6-drive-a5-bpf/corners.json` (8100 rows: 2700 units by 144, 146, 148 MHz), `r3-k1` `result.json` (reading bound 0.640 dB), `r3-s2` `result.json` (pad half-gap 0.385 dB, drift 0.387 dB).

**Reproduction (CK-ANA-C4, readiness R2).** `git archive d0de188` into the scratchpad, then from that export `.venv/bin/python hardware/sim/tx-pa/run_a5_r4.py all --expect`, without `CWHT_PA_REPLOT`, so both power decks re-ran in LTspice through `tools/ltspice-batch.sh` (blob `88b71475`): about 62 minutes each, log first line `LTspice 26.0.2 for MacOS`, no warning or error in either `.log`, deck SHA-256 `ff6f622f66d4ce5a` (p4) and `ff44551d88286654` (p5) as the README gives. The checker printed "--expect: 0 verdict(s) differ from the analysis record" and "exit status 0". Every output file was then compared with the committed one: `result.md` of all five runs, `result.json` of s2, s3 and s4, `verdicts.json` and all 7 plots are byte-identical. The p4 and p5 `result.json` differ only in the `ltspice` provenance block (wrapper lines), and their `.raw` SHA-256 differs from `raw.sha256` because LTspice writes the run date into the header; the owner's kept `.raw` files match their `raw.sha256` (`6f3187f9...` p4, `896daeef...` p5).

**Reviewer scripts (scratchpad, not product).** An inline grouping of `corners.json` on all ten non-frequency keys (rsrc, gain, p1db, src, vddo, tr, duty, coax_m, bpf, qbpf), independent of the checker's grouping. `passband.py`: imports the frozen checker's replica (`clamp_top_unit`, `module_vec`), adds the drain-voltage fixed point for the pack current, and sweeps the design corners (feeds low, mid, bound; efficiency 0.45 and 0.60; three drives; both window offsets; three frequencies; nine temperature cases) for true module spreads that the record's seven unit cases do not hold. `readhi.py`: the typical unit read high, at 8.4 V, in its ceiling cases.

### Verification of finding-1 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `d0de188` | Result |
|---|---|---|---|
| finding-1 | One-sided in-unit terms from the 146 MHz selection value | Reviewer grouping of d6: 2700 units; largest rise from the 146 MHz value +0.3599 dB, largest fall -0.7768 dB. Checker r4-s2: +0.360 / -0.777 dB. Equal | Yes |
| finding-1 | The revision 3 target at the +/-1.0 dB allocation fails | 17.3 x 10^(-(0.777 + 0.385 + 1.0 + 0.387)/10) = 9.62 mW and 17.3 x 10^((0.360 + 0.385 + 1.0 + 0.387)/10) = 28.27 mW: FAIL at the bottom, as R4.2 and the s2 verdict say | Yes |
| finding-1 | Re-centred target | sqrt(300) x 10^((2.189 - 1.772)/20) = 18.17 mW, taken as 18.2 mW. At +/-1.0 dB: 10.12 to 29.74 mW (PASS, +0.05 / +0.04 dB); break-even min(10 log(30/18.2) - 1.132, 10 log(18.2/10) - 1.549) = 1.04 dB; with the M2 reading 10.99 to 27.37 mW (+0.41 / +0.40 dB). All equal to the note | Yes |
| finding-1 | The pad set still covers every unit | Pad loss needed at 18.2 mW = 18.416 + (P146 - 12.60 dBm): 13.601 to 21.647 dB over the 2700 units (reviewer), inside the unchanged 14-pad set 13.48 to 22.04 dB, largest gap 0.766 dB. A reading error that moves the believed need outside the set selects an end pad, which only shortens the error, so the half-gap term holds | Yes |
| finding-1 | The selection frequency stated in the REQ-SYS-144 text | R4.7 after-text: "for a drive of 18.2 mW (TBR) at 146 MHz read with an uncertainty of at most +/-1.0 dB (TBR)" | Yes |
| finding-1 | Margin against its uncertainty (CK-ANA-E3) | The +0.04 dB at the allocation is stated with the break-even (+/-1.04 dB) and the M2 margin (+0.40 dB), and the note says the reading bound rests on analysis only (R3.4) | Yes |

**Result: finding-1 Verified.**

### Verification of finding-2 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `d0de188` | Result |
|---|---|---|---|
| finding-2 | A fixed clamp set on the typical curve does not hold the ceiling for a stronger module | r4-s4 part (a), re-run identical: revision 3's clamp gives 10.51 W for a module +0.3 dB above typical (FAIL against 10 W); a fixed clamp set on +0.3 dB (+0.07 dB graph read) leaves the typical unit 4.07 W at 8.4 V, -0.04 dB with the terms. Without a module maximum, no fixed clamp does both; the conclusion follows | Yes |
| finding-2 | The ceiling carried with its uncertainty, not beside it | R4.4 terms recomputed: read low 10 log(1/0.85) = 0.706 dB, read high 10 log(1.15) = 0.607 dB, other terms 0.10 + 0.05 + 0.07 + 0.05 + 0.01 = 0.28 dB; g- = 0.987 dB, g+ = 0.889 dB. Step targets 9.9 x 10^(-0.0987) = 7.887 W (scenario B) and 7.9 x 10^(-0.0987) = 6.293 W (D-9), equal to the decks' `tgt` | Yes |
| finding-2 | The open-loop ceiling for every unit the step passes (HZ-001) | Decks: highest module output 9.65 W (scenario B) and 7.74 W (D-9) over all 54432 corners and every pack voltage. Reviewer replica at the record's +1.5 dB read-low case: 9.646 W and 7.736 W. For true spreads the record does not model (finding-31), +2.0 and +2.49 dB read low: 9.646 W and 7.736 W. In the model the ceiling holds for any true spread whose reading is inside the bound | Yes |
| finding-2 | The deck clamp is what the checker computes | Re-run checks: deck clamp against the closed form within 0.97 of LTspice's reltol; a unit read exactly makes the target within 0.098 % and 0.084 %; PA case temperature within 1.53e-5 K; VGG at most 3.50 V and above the 2.30 V grid floor (lowest 2.430 V, 2.649 V). All PASS | Yes |
| finding-2 | REQ-SYS-012 delta and HZ-001 restated on the new basis | R4.7: REQ-SYS-012 +1/-2.7 dB at 6.4 V and +1/-2.3 dB from 6.7 V (2.69 W, 2.94 W); basis 2.82 W at 6.4 V and 3.09 W at 8.4 V, with the -0.15 dB unmodelled terms 2.72 and 2.98 W, margins about +0.06 and +0.07 dB; s3 check PASS. HZ-001: 9.65 W and 7.74 W with the step as the control. The revision 3 text (-1 dB from 7.8 V) is withdrawn | Yes |
| finding-2 | The reach-setting unit | `readhi.py`: the typical unit read high, 8.4 V, ceiling cases: 6.81 W at most (the note: "about 6.8 W as it is"). Its clamp top is 2.77 to 2.90 V at 8.4 V and 3.50 V at 6.4 V (`clamp_top_*_per_unit` in the p5 `result.json`) | Yes |

**Result: finding-2 Verified** for what it named: the ceiling now carries its uncertainty and holds, in the model, for every unit that passes the step. The fix introduces the new Major finding-31 on which units pass the step.

### New findings (iteration 2)

Ids start at 31 to stay clear of the iteration 1 ids, which this reviewer could not read; the lead SE renumbers if they collide.

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-31"></a>finding-31 | reviewer | Major | CK-ANA-A5, F2, D2, H1 | note R4.4 "The step" and "Reject", R4.5 "Open loop" and "Pack current", R4.7 HZ-001 causes, R4.8 R3-3; `run_a5_r4.py` `unit_cases` | The reject rule acts on what the step believes, not on the true module. A unit is rejected only when its clamp would have to go below the trim range, and the clamp is set from the believed spread (true spread plus the reading error). A module read low by up to g- = 0.99 dB therefore passes with a true spread up to about +1.5 + 0.99 = +2.49 dB above typical. The note says instead that the range covers "modules up to +1.5 dB above the typical curve", that "A stronger unit is rejected at build", that the rejection "is what bounds the upper spread", and lists as an HZ-001 cause "A module above the trim range fitted, detected because the trim cannot reach the step target". The seven unit cases stop at a true +1.5 dB, so the passing population is not covered. The ceiling is unaffected (reviewer replica: 9.646 W and 7.736 W for true +2.0 and +2.49 dB read low, as at +1.5 dB), but the pack current with the ALC at its top is not: the replica gives 3.68 A for scenario B and 3.30 A for D-9 (true +2.49 dB read low, 6.4 V, 25 C key-down, efficiency 0.45), against the note's 3.29 A and 3.00 A, which R3-3 sends to WP-PDR-24 as the upper figure; the fault-state dissipation rises with it. Fix: state the passing population as a believed spread up to the trim-range top, that is a true spread up to top + g-; add that case (true +1.5 + g-, read low) to the unit cases; restate the pack current (R4.5, R3-3) and any dissipation figure it feeds; correct the HZ-001 cause wording (a module above the trim range is caught only if it is above it by more than g-, and one that passes still meets the ceiling). Or set the reject threshold on the believed spread at top - g- and carry what that does to the reach | Open | Pending | |
| <a id="finding-32"></a>finding-32 | reviewer | Minor | CK-ANA-A5, B1 | note R4.4 "Setup" and "Trim", R4.7 REQ-SYS-144 after-text, R4.9 item 2 | The step reads the open-loop output at 8.4 V only, but the modelled clamp is a different curve of pack voltage for each unit: the typical unit read high has its top at 2.77 to 2.90 V at 8.4 V and 3.50 V at 6.4 V; the +1.5 dB unit read high 2.68 to 2.74 V at 8.4 V and 2.89 to 3.50 V at 6.4 V (scenario B). A real clamp has one shape and one trim. The ceiling at 6.4 to 8.4 V then holds only if the trimmed clamp stays at or below the modelled per-unit top at every pack voltage, and the 6.4 V basis (2.82 W) needs the typical units back at 3.50 V by 6.4 V; the proposed REQ-SYS-012 limit sits about +0.06 dB under that basis. R4.9 item 2 calls the reach figures upper bounds, but the note does not state the shape condition for the ceiling or send it to WP-PDR-22. Fix: state both conditions in R4.4 and in R3-1 (the step's projection covers 6.4 to 8.4 V with the designed clamp's shape), and say that the REQ-SYS-012 delta stands only once WP-PDR-22's clamp is shown to meet them | Open | Pending | |
| <a id="finding-33"></a>finding-33 | reviewer | Minor | CK-ANA-H1, A3 | note R4.7 HZ-001 causes; R4.4 terms table, first row | The HZ-001 control named for "the step's reading beyond its bound" is "the TC-SYS-010 characterization being Passed before the step". TC-SYS-010 as written characterizes 0.4 to 6.3 W with a correction curve to 25 V, so a Pass does not cover the step's 7 to 10 W (Vpk to about 32 V). The note knows this (R4-1, R4.9 item 4), but the control text does not say it depends on the R4-1 extension. Fix: name the extended characterization (to 10 W, uncertainty reported at 7 to 10 W, the 1N5711 reverse voltage of about 64 V against its 70 V rating) as the control | Open | Pending | |
| <a id="finding-34"></a>finding-34 | reviewer | Minor | CK-ANA-H3 | commit `d0de188` message; the git note on `d0de188` | The freeze commit of revision 4 carries the WP-PDR-28a thermal message and Refs of `d8dfb26` (REQ-SYS-112, 118, 181, HZ-003, INSP-112), not WP-PDR-21's. `tools/check_commit_msg.py --range d0de188~1..d0de188` passes it, since only the format is checked. The author's correction is a git note, which stays local unless `refs/notes` is pushed, and `git log --grep REQ-SYS-144` does not find the revision. The note's own change log (row 4) is right. Fix: record the correction where CM keeps it (a `docs/cm/deviations.md` entry, or the next WP-PDR-21 commit's message naming `d0de188` as revision 4 with the correct Refs); no amend on main | Open | Pending | |
| <a id="finding-35"></a>finding-35 | reviewer | Minor | CK-ANA-H2, E6 | note R4.8 | Revision 4 raises risks that go to no writer: a unit can be rejected at build (the owner then buys another module), the step relies on a probe reading outside TC-SYS-010's range, and REQ-SYS-012's reach at 8.4 V falls from 4.42 W to 3.09 W on the step basis. R4.8 sends nothing to the risk register writer (WP-PDR-18), and R3-5 to WP-PDR-29 gives the 6.4 V nominal figures but not the 8.4 V basis that TPM-015's red threshold reads. Fix: add a request to WP-PDR-18 and the 8.4 V figure to R3-5 | Open | Pending | |
| <a id="finding-36"></a>finding-36 | reviewer | Minor | CK-ANA-I2 | `results/2026-09-29-r4-s4-clamp-step/clamp_step.png` panel (b) | The six term labels of panel (b) are cut with "..." (for example "unit output loss (LPF and relay) from the NanoVNA S21 at 144..."), so the rows cannot all be read without the R4.4 table. Fix: shorter labels or a wider panel | Open | Pending | |

### Per-case results (iteration 2; the cases revision 4 moved)

Values are the checker's (all estimates), reproduced by the reviewer's re-run; the re-check column is the reviewer's own computation.

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-24 | Select-on-test drive in service, 18.2 mW target, M2 reading | TS-012 and the RA07M1317M window: 10 to 30 mW | 10.99 to 27.37 mW: PASS | +0.41 / +0.40 dB | reading bound by analysis (k1) | 10.99 to 27.37 mW | none |
| C-25 | Same, +/-1.0 dB allocation | REQ-SYS-144 (TBR) with the window | 10.12 to 29.74 mW: PASS | +0.05 / +0.04 dB | the allocation itself; break-even +/-1.04 dB | 10.12 to 29.74 mW | none |
| C-26 | Revision 3 target 17.3 mW at +/-1.0 dB | the window | 9.62 to 28.27 mW: FAIL | -0.17 dB | as C-25 | 9.62 to 28.27 mW | none |
| C-27 | Open loop, every unit that passes the step, scenario B, 6.4 to 8.4 V, 144 / 146 / 148 MHz, -10 to +45 C | RA07M1317M 10 W maximum rating (HZ-001) | 9.65 W: PASS | +0.16 dB | step terms inside g- | 9.646 W at true +1.5, +2.0 and +2.49 dB read low | finding-31, finding-32 |
| C-28 | Same, D-9 8 W | RA07M1317M 8 W stability guarantee | 7.74 W: PASS | +0.14 dB | as C-27 | 7.736 W | finding-31, finding-32 |
| C-29 | Pack current, ALC at its top, 25 C key-down, scenario B | request R3-3 to WP-PDR-24 (MF-R300 hold 2.04 to 2.2 A) | 3.29 A (note) | not an upper bound | module spread of the passing population | 3.288 A at true +1.5 dB; 3.680 A at true +2.49 dB read low | finding-31 |
| C-30 | Same, D-9 | as C-29 | 3.00 A (note) | not an upper bound | as C-29 | 3.002 A; 3.303 A at true +2.49 dB read low | finding-31 |
| C-31 | REQ-SYS-012 at 6.4 V, step basis, LPF at most MC 99 %, worst key-down case, scenario B | REQ-SYS-012: at least 3.972 W | 2.82 W: FAIL | -1.49 dB (-1.64 with the terms) | graph reads; clamp shape (upper bound) | re-run equal | finding-32 |
| C-32 | Same at 8.4 V | REQ-SYS-012 | 3.09 W: FAIL | -1.09 dB (-1.24 with the terms) | as C-31 | re-run 3.090 W; s4 replica 3.091 W | finding-32 |
| C-33 | Proposed delta line against the basis, scenario B | proposed REQ-SYS-012 (TBR) | s3 check PASS | about +0.06 dB at 6.4 V, +0.07 dB at 8.4 V | smaller than the graph-read term (0.07 dB) and the clamp-shape bound | recomputed from the basis | finding-32 |
| C-34 | D-9 with the step, 6.4 and 8.4 V | REQ-SYS-012 | 1.06 W, 0.58 W: FAIL | -5.7, -8.4 dB | as C-31 | re-run equal | none |

### Findings (iteration 2; current state of every finding this reviewer can see)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer (iteration 1) | Major | CK-ANA-B6, E3, F3, E5 | note R3.4 s2 (revision 3) | As note R4.1; verification table above | Verified (iteration 2) | n/a | |
| finding-2 | reviewer (iteration 1) | Major | CK-ANA-A5, B6, E3, F3, H1 | note R3.6 clamp tops (revision 3) | As note R4.1; verification table above | Verified (iteration 2) | n/a | |
| finding-31 | reviewer | Major | CK-ANA-A5, F2, D2, H1 | note R4.4, R4.5, R4.7, R4.8 | See the new findings table above | Open | Pending | |
| finding-32 | reviewer | Minor | CK-ANA-A5, B1 | note R4.4, R4.7, R4.9 | See above | Open | Pending | |
| finding-33 | reviewer | Minor | CK-ANA-H1, A3 | note R4.7, R4.4 | See above | Open | Pending | |
| finding-34 | reviewer | Minor | CK-ANA-H3 | commit `d0de188` | See above | Open | Pending | |
| finding-35 | reviewer | Minor | CK-ANA-H2, E6 | note R4.8 | See above | Open | Pending | |
| finding-36 | reviewer | Minor | CK-ANA-I2 | `clamp_step.png` | See above | Open | Pending | |

The iteration 1 Minor findings (liens) are carried by the iteration 1 text and are not restated here.

### Observations (not findings)

- O-1. The in-band drive terms come from three frequencies (144, 146, 148 MHz). With the D-13 bandpass centred in the band the extremes sit at the edges, so the three points bound the span; unchanged from revision 3.
- O-2. Limitation 5 (the graph-read term counted in g- and g+ and again in the unmodelled terms) is conservative, as the note says.
- O-3. With scenario B the HZ-001 ceiling (9.65 W) is outside the 8 W stability guarantee; that is the revision 3 trade (R3-1 option a), not a revision 4 change.
- O-4. The README says the final outputs were written with `CWHT_PA_REPLOT=1`. The reviewer's run without it gives byte-identical results and plots, so the replot path hides nothing.

### Cross items (returned to Claude as lead SE)

- X-1. File the iteration 1 text of this review above this section and keep its finding ids; renumber finding-31 to finding-36 if they collide, and add the iteration 1 Minor counts to the front matter.
- X-2. Rule C1: iteration 3 is the last. Its delta is finding-31; the Minor findings 32 to 36 become liens unless revision 5 fixes them.
- X-3. Until this record is APPROVED, the CR-018 rows for REQ-SYS-144 and REQ-SYS-012 do not go to the owner on revision 4 (rule C10).

### Checklist items changed at iteration 2

No: CK-ANA-A5, F2, D2, H1 (finding-31); A5, B1 (finding-32); H1, A3 (finding-33); H3 (finding-34); H2 (finding-35); I2 (finding-36). Yes on the items finding-1 and finding-2 named: B6, E3, F3, E5 (finding-1); B6, E3, F3 and A5 for the ceiling (finding-2). CK-ANA-C4 (re-run), B5 (independent checks) and I1 (all 7 renders opened) Yes.

### Visual closure (iteration 2)

Opened with the Read tool: `sot_band_r4.png`, `power_a5_step_clampb_sma.png`, `power_a5_step_clampb_temperature.png`, `power_a5_step_d9_sma.png`, `power_a5_step_d9_temperature.png`, `clamp_step.png`, `req012_basis_r4.png` (7 of the 7 the note cites; the re-run renders are byte-identical). Each shows what the note says: the one-sided band and the two break-evens; the open-loop maximum under 10 W (scenario B) and under 8 W (D-9) at every pack voltage; the step basis under 3.97 W at every pack voltage; the proposed limit line just under the shaded basis with the terms. Only finding-36 (cut labels) was found.

### Commands (iteration 2)

```
git archive d0de188 | tar -x -C <scratchpad>/rev/x
cd <scratchpad>/rev/x && /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_a5_r4.py all --expect
/Users/robinonsay/rust/cwht/.venv/bin/python <scratchpad>/rev/calc/passband.py
/Users/robinonsay/rust/cwht/.venv/bin/python <scratchpad>/rev/calc/readhi.py
/Users/robinonsay/rust/cwht/.venv/bin/python tools/check_commit_msg.py --range d0de188~1..d0de188
```

### Verdict (iteration 2)

**NEEDS CHANGES.** finding-1 and finding-2 are Verified: the drive target now holds 10 to 30 mW with one-sided terms, and the open-loop ceiling carries its reading uncertainty and holds for every unit the step passes. One new Major, finding-31: the step lets through modules up to about 2.5 dB above typical, not 1.5 dB, so the pack-current figure sent to WP-PDR-24 is about 0.4 A low and the HZ-001 cause wording is wrong. Five new Minor findings (32 to 36). One iteration is left under rule C1.


## Iteration 3: delta verification of finding-31 (Major) (2026-09-30, HEAD `a0c4db6`)

**Scope (rule C1, the last iteration).** Iteration 3 is a delta on revision 5 of the note (`a0c4db6`). It verifies the fix of the iteration 2 Major finding-31 case by case, re-runs every revision 5 deck and script from an export, opens every new plot, and checks the new values against their sources and against the revision 4 runs they rest on. finding-1 and finding-2 stay Verified from iteration 2 and are not reopened. New findings are raised only where revision 5 introduced a defect or left a defect of finding-31's kind in place; a new Minor finding is a lien (rule C1). Product: the 20 blobs of front matter `product_files`, each equal to `git rev-parse a0c4db6:<path>` and to `HEAD:<path>` at HEAD `a0c4db6`. `git diff d0de188 a0c4db6` touches only the note, `hardware/sim/tx-pa/README.md` and the new revision 5 files (31 files); no revision 4 input changed. No product blob is on a `cr/` branch. Checklist: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` (head `7784672`, not an ancestor of HEAD).

**Independence (rule C4).** This invocation authored no part of the note or any of its revisions, the decks, the checkers or TS-012, and did not write the iteration 1 or 2 review text. It edited no product file and wrote only scratch files under its own scratchpad.

**Search first (rule C3, charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any grep (queries: "WP-PDR-21 review record checklist pa-drive-ts012 finding-31"; "review of pa-drive-ts012 revision 4 delta iteration finding-31 believed spread reject rule"; "thermal budget A5 module dissipation input watts from pa-drive-ts012 key-down case temperature"; "RA07M1317M operation case temperature range maximum rating Tcase"). `grep` and `sed` then only pinned lines in files those searches or the brief named (the note, `run_a5_r5.py`, `run_a5_r4.py`, the run folders, `thermal-budget.md`, `tools/validate_docs.py`, the PDR work plan). The rustos tree was not read.

### Readiness (R1 to R6)

| # | Result | Evidence |
|---|---|---|
| R1 | Met | `git ls-tree a0c4db6` gives every `product_files` blob; HEAD is `a0c4db6`, so `git diff a0c4db6 HEAD` is empty. The note and `run_a5_r5.py` equal `git hash-object` in the working tree |
| R2 | Met | `run_a5_r5.py all --expect` from a `git archive a0c4db6` export (below): exit 0, LTspice only through the export's `tools/ltspice-batch.sh` (blob `88b71475`, equal to main's) |
| R3 | N/A | The product holds no JSON file under a schema. `tools/validate_docs.py` exits 0 at HEAD (123 of 123) and on this record in a scratch export |
| R4 | Met | Author summary; note R5.1 to R5.6 state the finding, the added case, the results with their classes (every figure an estimate), the restated text, the changed limitation and the verdict list; commit message passes `tools/check_commit_msg.py --range d0de188..a0c4db6` |
| R5 | Met | No `TBD` in section R5. The one restated TBR (+1.5 dB reject threshold) keeps its revision 4 TBR form |
| R6 | Met | The four cited PNGs exist beside their decks |

### Re-run from an export of the freeze commit (CK-ANA-C4)

`git archive a0c4db6 | tar -x` into the reviewer's scratchpad. The two revision 4 `.raw` files that s5 reads (kept on the owner's Mac under CR-017) were copied from the working tree into the export after `shasum -a 256 -c raw.sha256` passed for both. The committed r5 `.raw` and `.log` files were deleted from the export so that LTspice had to solve both decks again. Then, from the export root, `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-pa/run_a5_r5.py all --expect` with no `CWHT_PA_REPLOT`.

- **Exit status.** p4, p5 and s5 ran in about 18 minutes (517 s of LTspice for p4, the rest waiting on the wrapper's lock and solving p5). Every verdict of note section R5.6 printed PASS, then "--expect: 0 verdict(s) differ from the analysis record" and exit status **0**, as the note and README state. Both re-run `.log` files start "LTspice 26.0.2 for MacOS".
- **Decks.** Both regenerated decks are byte-identical to their committed blobs; their SHA-256 prefixes are the README's (`0f12e91657dd7c70`, `d60d0198f2099130`). s5's own check that `run_a5_r4.py` regenerates the committed r4-p4 and r4-p5 decks passed in the re-run.
- **Values.** Each re-run `result.json` equals the committed one in every number and string once the wrapper provenance and the kept-raw manifest are set aside (p4, p5); s5's `result.json` is byte-identical. Every `result.md` and all four PNGs are byte-identical, so the renders opened at `a0c4db6` are the re-run renders.
- **.raw files.** The committed r5 `.raw` files (2,232,612 bytes each, under the CR-017 limit, so committed with no `raw.sha256`, as the README says) differ from the re-run ones only in the UTF-16 header before the `Binary:` marker (byte 884: temporary deck path and date); their binary data sections are byte-identical (2 of 2). The `.log` files differ only in the temporary path, start time and elapsed time.
- **Independent read of the committed .raw files (spicelib, reviewer code).** Over all 1944 steps and 6.4 to 8.4 V: highest `V(pmod)` 9.648 W (p5) and 7.736 W (p4); highest `I(Vp)` 4.221 A (p5) and 3.698 A (p4); highest `V(tc)` 106.6 C (p5); `V(vg)` at most 3.5000 V in both. These equal the note's R5.3 figures (ceilings, the -10 C start pack current 4.22 and 3.70 A, the +45 C key-down case 106.6 C).
- **Check tolerance, noted.** The author's first run (scratch log `r5_all.log`) failed the new pack-current consistency check at 0.1 % (0.111 % and 0.113 %), and the committed check uses 0.2 % with the basis "LTspice reltol 0.1 % on each of V(pmod) and V(d)". The deck solves the pack current from exactly those two node voltages (`Bpa d 0 I=V(pmod)/(eta*max(V(d),1))`), so 0.2 % on their ratio is the right propagation of the solver tolerance, and the check is a consistency check, not a result. No finding.

### Inputs checked against their sources (CK-ANA-A4; every input revision 5 adds or restates)

| Input | Value in revision 5 | Source checked | Result |
|---|---|---|---|
| Step terms g- and g+ | 0.9874 and 0.8886 dB | r4-s2 `result.json` via `R4.step_guard`, and the R4.4 / R4.6 table (0.99 / 0.89 dB at 15 %) | Equal (p4, p5 check within 1e-9) |
| Reject threshold | +1.5 dB (TBR) on the believed spread | `run_a5_r4.py` `STEP_X_TOP_DB`; R4.4 reject bullet | Equal; the added case has true +2.4874 dB, error -0.9874 dB, believed +1.5000 dB |
| Step target | 7.887 W (scenario B), 6.293 W (D-9) | 9.9 and 7.9 W x 10^(-g-/10), R4.4 | Equal to the arithmetic |
| Passing bounds | true up to +2.49 dB read low, +0.61 dB read high | 1.5 + 0.9874 = 2.4874; 1.5 - 0.8886 = 0.6114 | Correct |
| Reviewer's alternative threshold | +0.51 dB believed; rejects a typical unit read high (believed +0.89 dB) | 1.5 - 0.9874 = 0.5126 < 0.8886 | Correct |
| REQ-SYS-012 basis unit at 8.4 V | "+1.5 dB read high" kept (3.09 W) against 3.16 W for "+0.5 dB read high" | R4.6 text ("typical, +0.5, +1.0 and +1.5 dB units read high give 3.24, 3.16, 3.13 and 3.09 W") | Cited value is there; the highest passing unit read high (+0.61 dB) lies between 3.16 and 3.13 W, so keeping 3.09 W is conservative by less than 0.1 dB, as stated |
| MF-R300 hold current | 3.00 A at 23 C, 2.31 A at 50 C, 2.04 A at 60 C; 2.04 to 2.2 A at 55 to 60 C | Note R3.5 row, Bourns MF-R series REV. AR 09/26 (read at iteration 1) | Equal; 2.2 A at 55 C is the linear mid-point (2.175 A) |
| RA07M1317M Tcase(OP) | not used; the note compares 106.6 C with its own 100 C hot bound case | `thermal-budget.md` section 3 (datasheet Jun 2019 p.2: -30 to +110 C; p.8 guidance "below 90 C") | 106.6 C is under the 110 C rating and above the 90 C guidance; the note routes it to HZ-003 and WP-PDR-28 (see F2 below) |
| Rth case to ambient | 6.11 K/W | Note section 3 thermal row (WP-PDR-28) | Equal; 45 + 6.11 x 10.08 = 106.6 C |
| Clamp tops of the added case | 2.73 to 2.82 V (scenario B), 2.67 to 2.72 V (D-9) at 8.4 V | r5-p5 and r5-p4 `result.json` `clamp_top_8v4`: 2.725 to 2.816 V and 2.669 to 2.715 V | Equal (rounded) |
| Revision 4 unit cases | the seven r4 cases, unchanged | r4-p4 and r4-p5 `.raw` (sha256 OK) and `run_a5_r4.py` `unit_cases`; s5 population tables | The s5 revision 4 columns equal the R4.5 figures (3.29 / 3.22 A, 3.00 / 2.93 A, 10.30 W) |

### Checklist answers (delta items touched by finding-31)

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A5 (assumptions stated and bounded) | Yes | R5.2 states the rule on the believed spread and bounds the passing true spread at +1.5 + g- dB; HZ-001 causes restated (R5.4) |
| CK-ANA-B6 (model covers the case range) | Yes | The added case is in both decks; the replica sweep and the reviewer's extended sweep cover the passing region |
| CK-ANA-C4 (reproducible from the repo) | Yes | Re-run above |
| CK-ANA-D2 (numbers consistent across the record) | No (Minor finding-37) | R4.5 D-9 bullets still quote the tops of the rejected unit |
| CK-ANA-E3 (margins against criteria) | Yes | Ceilings 9.648 W against 10 W and 7.736 W against 8 W, unchanged; pack current against the MF-R300 hold stated as negative margin (R5.3, R5.4 R3-3) |
| CK-ANA-F2 (worst case identified) | Yes | Added case shown worst for pack current in every temperature case and for dissipation within the grid (reviewer sweep below) |
| CK-ANA-H1 (hazard inputs sent) | Yes | HZ-001 wording replaced; new HZ-003 request with 10.37 / 10.08 W and 88.4 / 106.6 C; R3-3 to WP-PDR-24 with 3.68 / 3.60 A and 4.22 A |
| CK-ANA-I1 (plots opened, match the text) | Yes | Four PNGs opened (below) |

### Visual closure (CK-ANA-I1)

Each PNG was opened with the Read tool at `a0c4db6` (the re-run renders are byte-identical).

- `r5-s5/pass_population.png`: two panels (scenario B, D-9), true spread against reading error, the black threshold line (believed = +1.5 dB), the dotted -g- and +g+ bounds and the dashed +1.5 dB true bound of revision 4. The darkest cell is at the bottom-right corner (+2.49, -0.99 dB), labelled 3.68 A (scenario B) and 3.30 A (D-9); the revision 4 "+1.5 dB read high" point is marked rejected. It matches R5.2. The colour cells step past the threshold line by half a cell (nearest shading); cosmetic only.
- `r5-s5/pack_current_dissipation.png`: pack current and dissipation against pack voltage; the revision 5 lines lie on or above the revision 4 lines everywhere and meet them above about 7.8 V (scenario B) and 6.9 V (D-9). Scenario B dissipation is flat at about 10.2 to 10.4 W from 6.4 V (revision 4 rose from 8.84 W at 6.4 V to 10.3 W at 7.0 V), which is R5.3's "now reached from 6.4 V". The "with the added case" lines plot the added case alone, not the population maximum; since the added case sets the maximum at every voltage (reviewer sweep), the lines are right.
- `r5-p5/power_a5_added_case_clampb.png` and `r5-p4/power_a5_added_case_d9.png`: module output flat under the 10 W and 8 W lines (9.65 and 7.74 W peaks); pack current per key-down case from 3.68 / 3.30 A at 6.4 V, crossing the 23 C hold line at about 8.0 V (scenario B) and 6.85 V (D-9); dissipation per case matching the R5.3 table.

### Reviewer's independent check of "the added case is the worst one" (CK-ANA-F2)

s5's sweep covers true spreads 0 to +2.49 dB at one pack voltage (6.40 V) and two temperature cases. The reviewer extended it (scratch script, the author's replica functions `replica_sweep` and `clamp_top_unit` called from the export, no product change) to every one of the nine temperature cases, pack voltages 6.4, 6.8, 7.2, 7.6, 8.0 and 8.4 V, true spreads -1.0 to +2.49 dB (15 points) and errors -g- to +g+ (9 points), both scenarios, pack current and dissipation:

- **Pack current.** In every temperature case of both scenarios the highest value over pack voltage and the passing region is at (+2.49, -0.99) dB: scenario B 3.680 A (25 C key-down), 3.598 A (+45 C key-down), 4.221 A (-10 C start), 3.946 A (25 C start, at 6.8 V), 3.561 A (-10 C key-down); D-9 3.303, 3.203, 3.698, 3.579, 3.218 A. These equal the deck figures of the R5.3 table within 0.01 A.
- **Dissipation.** Every maximum lies on the read-low edge (e = -g-), as R5.2 argues; along that edge the values differ by at most about 0.05 W, so the discrete-case figures of R5.3 (10.37, 10.08, 11.71 W scenario B; 8.32, 8.09, 9.42 W D-9) are the maxima within the grid resolution (sweep 10.367, 10.079, 11.710 W; 8.315, 8.092, 9.400 W).
- Units weaker than typical (true -1.0 dB) draw less in every case. The claim holds.

### Verification of finding-31, case by case

| Part of finding-31 | Revision 5 | Verified by | Result |
|---|---|---|---|
| (1) The reject rule acts on the believed spread; the true spread of a passing unit reaches +1.5 + g- = +2.49 dB | R5.2 states it; R4.4 reject bullet, R4.5 ceiling paragraph and limitation 3 marked "(Revision 5)" in place; R5.5 restates limitation 3 | Reading of the diff `d0de188..a0c4db6`; arithmetic above | Fixed |
| (2) The +2.49 dB case was not run | Added to both power decks (r5-p4, r5-p5, 1944 steps each); s5 combines it with the seven revision 4 cases read from their checked `.raw` files | Re-run, independent `.raw` read, extended sweep | Fixed; ceilings unchanged, 9.648 and 7.736 W (PASS) |
| (3) Pack current sent to WP-PDR-24 (3.29 A, 3.00 A) wrong | R5.3 table: 3.68 / 3.60 A (scenario B), 3.30 / 3.20 A (D-9) key-down; start rows 3.95 / 4.22 A and 3.58 / 3.70 A added; R3-3 restated in R5.4; R4.5 and R4.8 marked | Deck and sweep figures above; equal to the iteration 2 reviewer's 3.68 and 3.30 A | Fixed |
| (4) HZ-001 cause "a stronger module is detected" wrong | R5.4 HZ-001 block: the ceiling holds for any true spread given the reading inside its bound; causes restated (mistrim, reading low beyond its bound, a module believed above +1.5 dB rejected, a +2.49 dB module passing with the R5.3 current and dissipation); R4.7 HZ-001 marked | Reading; consistent with the ceiling results | Fixed |
| (5) Consequences of the higher population: trim range and dissipation | Trim range restated on the believed +1.5 dB unit, 2.73 V (scenario B) and 2.67 V (D-9) at 8.4 V (R5.3, R3-1); dissipation 10.37 / 10.08 W from 6.4 V and case 88.4 / 106.6 C (R5.3) with a new HZ-003 request naming WP-PDR-28 (R5.4); section 7.1 HZ-003 text marked | `clamp_top_8v4` values; `.raw` read (106.6 C) | Fixed (the stale D-9 tops of R4.5 are finding-37, Minor) |
| (6) The iteration 2 alternative (threshold at +1.5 - g-) | Assessed and not taken in R5.3: it would reject a typical unit read high; kept as an option for WP-PDR-22 and WP-PDR-24 | Arithmetic above | Disposition accepted: the choice is the author's and the consequence of not taking it is carried in the pack current, dissipation and HZ-003 requests |
| Rule C1 (only finding-31 changed) | Every change in the diff belongs to finding-31 or its bookkeeping (header rows, change-log row 5, README) | `git diff d0de188 a0c4db6` | Met |

**F2, the 106.6 C module case (checked, not a finding).** The +45 C key-down case of scenario B puts the module case of the added unit at 106.6 C (revision 4 already had 106.3 C, unstated). This is under the RA07M1317M Tcase(OP) maximum of 110 C and above the datasheet's 90 C long-term guidance, with the ALC at its top and no thermal inhibit modelled. WP-PDR-28a's thermal budget still uses the TS-012 section 7.3 dissipation of 9.94 W at the corner and flags that WP-PDR-21 may move it (its AT RISK row and limitation 5); revision 5 sends the higher figures to the HZ-003 writer with WP-PDR-28. The note does not use 106.6 C in any REQ-SYS-012 figure: the reach is set by units read high, which dissipate 7.4 to 7.6 W, so the 100 C hot bound case still bounds them. The routing is sufficient for this analysis; the thermal consequence belongs to the thermal budget's next revision.

### Findings (iteration 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-B6, E3, F3, E5 | Note R3.4, R3.7 (fixed in R4) | One-sided drive terms about the 146 MHz selection point | Verified (iteration 2) | - | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A5, B6, E3, F3, H1 | Note R3.2, R3.6, R3.7 (fixed in R4) | Clamp ceiling on the typical module only | Verified (iteration 2) | - | |
| <a id="finding-31"></a>finding-31 | reviewer | Major | CK-ANA-A5, F2, D2, H1 | Note R4.4, R4.5, R4.7, R4.8, R4.9 item 3 (fixed in R5) | The reject rule acts on the believed spread; a unit up to +2.49 dB passes read low; its case, the pack current and the HZ-001 wording were missing or wrong. Fixed case by case as the table above shows | Verified (iteration 3, `a0c4db6`) | - | |
| <a id="finding-3"></a>finding-3 to finding-10 | reviewer | Minor | as iteration 1 | as iteration 1 | The eight Minor findings of iteration 1, held as liens under rule C1 (the note's Status row says so) | Open (lien) | - | CDR readiness declaration |
| <a id="finding-37"></a>finding-37 | reviewer | Minor | CK-ANA-D2 | Note R4.5, "D-9 as specified (8 W ceiling, 0.20 V window) with the step", bullets 3 and 4 | The two bullets still give the clamp tops of the "+1.5 dB, read high" unit, which the revision 5 rule rejects (believed +2.39 dB): "a +1.5 dB unit read high has its top at 2.63 to 2.67 V at 8.4 V" and "Their top at 6.4 V goes down to 2.76 V". They carry no "(Revision 5)" marker, unlike the other R4 statements finding-31 touched. The lowest top of a passing D-9 unit (believed +1.5 dB) is 2.67 V at 8.4 V and 2.85 V at 6.4 V (r5-p4 `clamp_top_8v4` 2.669 V, `clamp_top_6v4` 2.846 V); R5.3 and the restated R3-1 already use 2.67 V. No verdict or request changes. **Fix:** mark both bullets "(Revision 5)" with the passing figures, at the next revision | Open (lien) | - | CDR readiness declaration |

### Values proposed (rule C10)

- **REQ-SYS-144, the restated reject sentence (R5.4): supported.** It states the rule on the step's projection of the reading (the believed spread), which is what the runs model; the ceiling figures it protects (9.65 W, 7.74 W) are verified above.
- REQ-SYS-012 and the other REQ-SYS-144 clauses are unchanged by revision 5; their iteration 2 standing is unchanged.
- The pack current (3.68 A key-down, 4.22 A at the -10 C start, scenario B) is above the MF-R300 hold current at every temperature, and the module dissipation reaches 10.37 W. Both are stated as requests to WP-PDR-24 and to the HZ-003 writer with WP-PDR-28, not as values of this note. The owner should see both figures with the CR-018 rows at S1, because the choice between scenario B and D-9, and any tighter reject threshold, moves them.

### Verdict (reviewer, iteration 3)

```
VERDICT: APPROVED (reviewer); record verdict held at NEEDS CHANGES (analysis template only on cr/CR-012)
PRODUCT: docs/design/analysis/pa-drive-ts012.md@309c8744cfa37aa4cb4916f615f358a41716d3a4, hardware/sim/tx-pa/run_a5_r5.py@56da6f40bcd6065d08b52018c61bfa82e081b2c3 and the 18 other blobs of product_files, at a0c4db679653e64a2d30803f1b2000027b6e6516
FINDINGS:
- [Major] finding-31 CK-ANA-A5/F2/D2/H1: Verified. The rule is stated on the believed spread; the +2.49 dB read-low case is run in both decks; ceilings 9.648 W and 7.736 W unchanged (PASS); pack current 3.68 / 3.60 A (scenario B) and 3.30 / 3.20 A (D-9) key-down, 4.22 / 3.70 A at the -10 C start; dissipation 10.37 / 10.08 W, case 88.4 / 106.6 C; HZ-001, HZ-003, R3-1 and R3-3 restated. Re-run exit 0; extended sweep confirms the added case is the worst.
- [Major] finding-1, finding-2: Verified at iteration 2, not reopened.
- [Minor] finding-3 to finding-10: liens from iteration 1.
- [Minor, new] finding-37 CK-ANA-D2: two R4.5 D-9 bullets still quote the clamp tops of the rejected "+1.5 dB read high" unit (2.63 to 2.67 V at 8.4 V, 2.76 V at 6.4 V; passing 2.67 V and 2.85 V). Lien.
OPEN MAJOR: 0
MEASUREMENTS: iteration 3 turns=45; minutes=40; major=3 (verified 3); minor=9 known to this reviewer (open as liens 9)
```

