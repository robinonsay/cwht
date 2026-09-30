---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-28a thermal budget of A5
# (docs/design/analysis/thermal-budget.md): iteration 1 (full review of revision 0 at afa80b4), iteration 2 (delta on
# the three Major fixes, revision 1 at 6eb014c) and iteration 3 (delta on the fixes of finding-20 and finding-21,
# revision 2 at d8dfb26), rule C1.
# FILING NOTE FOR THE LEAD SE. No record existed under docs/reviews/PDR/checklists/ at HEAD d8dfb26. The iteration 1
# and iteration 2 reviewers returned their texts as record_text (the harness refuses a subagent's Write of a new
# record). This file merges both texts unchanged in substance, in their own sections, and adds iteration 3. The
# iteration 2 reviewer did not have the iteration 1 text, so its findings are numbered from 20; finding-12 to
# finding-19 were never issued and are not reused (ids are never reused).
# id: INSP-121, the id the iteration 1 reviewer proposed as the next free one. Iteration 2 used INSP-121 as a
# provisional id and asked the lead SE to use the iteration 1 id. At d8dfb26 neither INSP-121 nor INSP-121 appears
# anywhere in the repository. The lead SE confirms or reassigns the id.
# X-1 (checklist field): the item set applied is docs/templates/peer-review-checklist-analysis.md revision A, blob
# 0386cc6e, on cr/CR-012-pdr-checklist-templates (branch head 7784672, not an ancestor of d8dfb26). The template is
# not on main, and tools/validate_docs.py rejects a checklist field whose template is absent from docs/templates/, so
# the field names the design checklist, as INSP-112 did; checklist_analysis records the template actually applied.
id: INSP-121
checklist: peer-review-checklist-design
checklist_revision: A
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-thermal-budget.md
product: docs/design/analysis/thermal-budget.md
# product_commit (iteration 3): d8dfb26, note revision 2 with run 2026-09-29-a5-closure-r3. Every blob below equals
# git rev-parse d8dfb26:<path>, and the note and the runner equal HEAD. thermal_model.py and ts012_thermal.py are
# the INSP-112 frozen files (no commit since 35fc7ee; SHA-256 54b5ecf4...3e66e0 and 09cf75ef...b97ce0, equal to the
# scripts/ copies). Runs r1 and r2, the TS-012 runs and hardware/sim/thermal/README.md have no diff 6eb014c..d8dfb26.
# product_files_iteration_2 and _iteration_1 keep the blobs the earlier iterations reviewed (at 6eb014c and afa80b4).
product_commit: "d8dfb26e958ca21d141f7f84552cf178e99a9831"
product_files: ["docs/design/analysis/thermal-budget.md@5dfa85e053796ee7c0a6702b7e0aac5b6317f7d4", "hardware/sim/thermal/a5_closure.py@6d8b23cff22b7639657225dc0c239f68ac2cc210", "hardware/sim/thermal/thermal_model.py@54573514ad75cbae6edee930996f5fa5a745eed6", "hardware/sim/thermal/ts012_thermal.py@3eb26aaace15c59002c9820d26b36461e1760105", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/README.md@0a930f129767a4e499c2c19d8838bd21c41bc01e", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/results.md@f350f865b25b85f71614888402e1946316c1c22a", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/inputs.csv@402b3d5f55af94f24aecd60bb36c5c82819aa84e", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/verdict_set.csv@ca6e399d03a80c5fa2b903cf0c4a8e3537d944f1", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/inhibit.csv@7d2cdd7768142b4aff8e0479816632abdcda89e9", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/backstop.csv@6ed92c680c7971e1f37fb6006336fe688df00ac4", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/protection_screen.csv@ab1bc08270a776f3f52613ce07d0636791df28de", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/backstop_screen.csv@a0a9e1c5f93aa4744451c727d43fa8a791df338d", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cap_pattern.csv@fe91a613ba719a97d8d569d7bcbab01d1d79565d", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cap_pattern_verdicts.csv@d659ba0194365dd63b245e5c889a8587814d8654", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/bands.csv@a85b710182f3356e872f42dfc0aeb00397d2cfdc", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/bench_acceptance.csv@89273cdfb6c5838fccb7f7c5ae8df3d1f7ba33d6", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/duty_sweep.csv@8953ae4268cdd0d82d43c42fc95eabac8b0cf36b", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/summary.csv@8d496fa44b652fe5b07e2824af4b57e52c5d5123", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/tornado.csv@6b168021ba5581f9ee9d6a43b8cc4ef040046c40", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/check-stdout.txt@8bc929b630cddcbfaccbd14fb52371fc85649270", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/check-stdout-try1.txt@02936794e8214710300d98f0c9c0785f71a1d3d7", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/run-stdout.txt@7b16e7ba06dc221eacd50ea805a91eebbc57a5d5", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/ltspice/thermal_a5cl.net@76d8a08fad7b509d6eb0b15a5c825f11c55b9d5d", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/ltspice/thermal_a5cl.log@bd48d51a6e0cbce4a90aa3ce4a7d46497652cbcd", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/scripts/a5_closure.py@6d8b23cff22b7639657225dc0c239f68ac2cc210", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_box_vs_duty.png@8c6f36437a0ba18a605fcf6f3e53094bacad6448", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_cap_pattern.png@63e7f6ddf44a210452c244e0aa4d37b0acfcc9e0", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_inhibit_backstop.png@598324fab0b188ca13c2df2c97abe08e0b92b0ee", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_protection_screen.png@ef7e83dec0496a02064f2ca9d3bce2c22c8d1885", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_tornado.png@cfde6a9babcc72e87a75f039f677f5b36d39f30e", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_margins.png@99f23fb07d3508239fddbde26d8bd97ea32f7962", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_ltspice_crosscheck.png@40f30ea318293a6597625fa05567f00ef36a4883", "hardware/sim/thermal/results/2026-09-29-a5-closure-r3/cl_bench_acceptance.png@836c6acc5b62bc4a33527f0dabdc1ccfce8efe9c"]
product_files_iteration_2: ["docs/design/analysis/thermal-budget.md@4ff68737d91cd9724cfcadcff768c70a9da809df", "hardware/sim/thermal/a5_closure.py@0e23d4d221fe88d3023b8b648b323e0b017774b4", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/results.md@5a487b8215c9f47592ef9335dd5b12087ee5fe1d", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/cap_pattern_verdicts.csv@114840168a1d862cd3550929460724fd8625d9a9", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/inhibit.csv@3f69d777e576493418738d245543a137f3c710da", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/protection_screen.csv@bab71d596ee1040e6602d465f4ab8839483c1ae9", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/cl_cap_pattern.png@56fe630eaf98da3a173c84e91431528f9b5764a7", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/cl_inhibit_backstop.png@77f0de3f4f333eb4023f3d4204b652beaf34e26e", "hardware/sim/thermal/results/2026-09-29-a5-closure-r2/cl_protection_screen.png@a4b7f9ffaa90c25de02c7dedeb57a66e61acb612"]
product_files_iteration_1: ["docs/design/analysis/thermal-budget.md@d7f6a409628bd3ac1499d5fbf2050135fde59ba0", "hardware/sim/thermal/a5_closure.py@834c217a6fb1e74c87a308baef9cd3b4f55ab4f7", "hardware/sim/thermal/results/2026-09-29-a5-closure-r1/results.md@2fb253340a9c5ef656193081af9cc146b8c93761", "hardware/sim/thermal/results/2026-09-29-a5-closure-r1/verdict_set.csv@df87fec9e2821f1f16bb6b73ef8364f126934aca"]
analysis_kind: [thermal, simulation-deck, worst-case]
product_size: "1 note (433 lines, revision 2); 25 verdict criteria (C01 to C25) over 3 layouts; 125 classed inputs (88 swept on A5-CL); 5 closed-loop inhibit cases, 3 backstop cases, 4 cap-pattern runs; 1 LTspice deck; 1 runner on 2 frozen model files; 8 plots"
tools_used: ["LTspice 26.0.2 through tools/ltspice-batch.sh (TV-014, accredited ACC-LTSPICE-001; .log first line 'LTspice 26.0.2 for MacOS')", "venv Python 3.13 (TV-001 accredits the interpreter)", "numpy 2.5.3, matplotlib 3.11.2, spicelib 1.6.3 (lock section 2, class B, no TV record: developer evidence per 05 section 9.1, as the note's Evidence status row says)"]
# values_proposed: the section 6 block and section 9 of note revision 2. The reviewer finds them supported
# (iteration 3); they go to the owner only once the record verdict is APPROVED (rule C10), and the owner rules them
values_proposed: ["REQ-SYS-112: condition 'at up to 30 % (TBR) key-down duty in 13 s key-downs' at 45 C, limit 110 C kept (supported: C01 97.2 C +10.7 K; junction also bounded by the inhibit, C13)", "new duty-cap requirement: at most 30 % key-down time in any rolling 10 min window at the 5 W step (supported: C22 to C25 PASS under the pattern that holds exactly the cap; 35 % not shown to pass)", "REQ-SYS-118: 71 C +/-3 C at the flange NTC, 100 ms, re-arm hysteresis at least 3 C (supported: C13 108.0 +0.6 C, C14 82.5 +0.6 C, every-input stack 109.3 C; holds for 3 to 10 C hysteresis; f dependence stated as finding-22, Minor)", "REQ-SYS-181: change from 95 C +/-3 C to 92 C +/-3 C on the sink, 100 ms (supported, iteration 2; unchanged in revision 2)", "REQ-SYS-113: 48 C confirmed (not in the deltas; unchanged)", "CR-003 revision 4 Q4 PETG heat-deflection temperature: at least 60.6 C, 64.7 C with the band (supported: C24)", "in-situ sink bench acceptance: at most 8.80 K/W at 5.0 W, 7.27 K/W at 10.0 W (not in the deltas; unchanged; finding-9 Minor lien)", "D-6 alternative sink-NTC duty limit S: 79.2 C as programmed, not recommended (unchanged)"]
# renders_inspected: the 8 PNGs of run r3 that the note cites (7 embedded, plus cl_bench_acceptance.png named in
# section 8), each opened with the Read tool at d8dfb26
renders_inspected: 8
sprint: PDR-prep
author_agent: "author:WP-PDR-28a analysis author (Claude; revision 0 at afa80b4, revision 1 at 6eb014c, revision 2 at d8dfb26)"
reviewer_agent: "reviewer:WP-PDR-28a-analysis-thermal-budget-iter3 (independent; authored no part of the note, its revisions, a5_closure.py, the frozen TS-012 model files, TS-012 or the design data analysed; iterations 1 and 2 by independent reviewers WP-PDR-28a-thermal-budget-iter1 and -iter2)"
# criticality: the note proposes the REQ-SYS-118 setpoint and a firmware duty cap that the SW-SAFE thermal unit
# implements (07 section 14.1 row "Thermal protection", HZ-003), as INSP-112 recorded; section J is answered here
criticality: safety-critical
# assurance_required: a stand-alone analysis note is not a row of 07 section 2.1.1, and no sw-<sub> token is in the
# product path or the slug (template front matter rule)
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3): APPROVED (rule C1). finding-20 and finding-21 (Major, iteration 2) are Verified;
# finding-1 to finding-3 (Major, iteration 1) stay Verified. No Major finding is open. Minor finding-4 to finding-11,
# finding-22 and finding-23 (new here) are open as liens due at the CDR readiness declaration (rule C1).
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES, as for INSP-112: the applied analysis template is still only on cr/CR-012 (blob
# 0386cc6e). The lead SE sets the record verdict to APPROVED in the CR-012 merge commit (or the commit right after
# it) if that blob is unchanged, or rules otherwise
verdict: NEEDS CHANGES
# counts over the whole record: Major finding-1 to 3, 20, 21 (5, all Verified); Minor finding-4 to 11, 22, 23 (10,
# all Open)
findings_major: 5
findings_minor: 10
findings_open: 10
findings_fixed: 0
findings_verified: 5
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 6]
deferred_rids: []
# items_no (iteration 3): none. CK-ANA-D2 and H3 are answered "Yes, one Minor" (finding-23)
items_no: []
items_no_iteration_2: [CK-ANA-A5, CK-ANA-E5, CK-ANA-F3]
items_no_iteration_1: [CK-ANA-A3, CK-ANA-A4, CK-ANA-A6, CK-ANA-B4, CK-ANA-B6, CK-ANA-C3, CK-ANA-D2, CK-ANA-E3, CK-ANA-E5, CK-ANA-F3, CK-ANA-J2]
# effort: iteration 1 45 turns / 70 min; iteration 2 45 / 75; iteration 3 40 / 80
effort_turns: 130
effort_minutes: 225
record_status: Open
date: 2026-09-29
date_closed: null
---

# Peer review record INSP-121: WP-PDR-28a thermal budget of A5 (`docs/design/analysis/thermal-budget.md`)

Every temperature in the note and in this record is an **estimate** from the lumped model of `thermal-ts012.md` (INSP-112). The note's results are developer evidence (class B Python stack without a TV record).

| Iteration | Product | Reviewer verdict | Majors |
|---|---|---|---|
| 1 | Revision 0 at `afa80b4`, run r1 | NEEDS CHANGES | finding-1 to finding-3 raised; 8 Minor |
| 2 (delta) | Revision 1 at `6eb014c`, run r2 | NEEDS CHANGES | finding-1 to 3 Verified; finding-20 and finding-21 raised; 1 Minor |
| 3 (delta) | Revision 2 at `d8dfb26`, run r3 | **APPROVED** | finding-20 and finding-21 Verified; none open; 1 new Minor |

The current state of every finding is the findings table of the iteration 3 section, at the end of this record. The iteration 1 and 2 sections are kept as their reviewers returned them.

## Iteration 1 (full review of revision 0 at `afa80b4`)

Product: `docs/design/analysis/thermal-budget.md@d7f6a409` with `hardware/sim/thermal/a5_closure.py@834c217a` and run `2026-09-29-a5-closure-r1`, at `afa80b4` (WP-PDR-28a, freeze F0). Reviewer: independent (authored nothing in WP-PDR-28a). Checklist: `peer-review-checklist-analysis.md` revision A (X-1 in the front matter). Every temperature in the note and in this record is an estimate from the lumped model of `thermal-ts012.md` (INSP-112).

**Summary for the lead SE.** The run is reproduced exactly: a `git archive afa80b4` export re-run with `--check` gives exit 0, and every CSV, every plot and the LTspice deck are byte-identical to the committed ones. The datasheet values the note cites are correct at the pages it names, with one grade mismatch (finding-4). The L-2 lever (LM2940 on the sink) and the duty cap are sound, and items (1), (2) and (4) close at the steady cap. Three cases are not the worst case the note says they are, and each one changes a value that goes to the owner at S1:
- finding-1: with only the REQ-SYS-181 backstop acting, the module case reaches 111.3 C once the flange-to-sink inputs are at their adverse ends. That is above the 110 C Tcase(OP) rating the note uses to confirm REQ-SYS-181.
- finding-2: the proposed REQ-SYS-118 value of 83 C holds 110 C only when the device and interface inputs are nominal (margin 0.07 K). One in-range input at its adverse end takes the junction to 111.0 to 111.9 C, and the bench rule cannot detect those inputs.
- finding-3: the "worst pattern the cap allows" is run with the nominal sensor. With the governing sensor state, the hottest PETG face is 56.4 C, and 60.5 C with the band (OPEN), not 55.2 C.

Verdict: **NEEDS CHANGES** (3 Major, 8 Minor).

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-F3, CK-ANA-E3 | `a5_closure.py` `backstop_study` lines 356-358; note sections 4.2, 6 (REQ-SYS-181 row), 9 (REQ-SYS-181 row); C23, C25 | The "Rth and dissipation adverse" backstop case sets `a5_rjc2`, `a5_bond`, `a5_p1`, `r_feed` and `tau_ntc_sink` adverse. It leaves `r_spread_x` at 0 K/W, which is the favourable end of its 0 to 0.3 K/W range, and `k_tim` at nominal 0.70 (range 0.60 to 0.80). These two inputs set the flange-to-sink rise, and the backstop senses the sink, so they move the case one for one. Reviewer re-run on the frozen runner, key held for 3 h, 45 C: with `r_spread_x` 0.3 added, the case reaches **110.00 C**; with `k_tim` 0.6 as well, **111.3 C**, channel 137.0 C. The note reports 106.9 C, PASS, 3.1 K margin with no band, and on that basis states REQ-SYS-181 as "confirmed against the device ratings" (p.2 Tcase(OP) -30 to +110 C). Section 4.2 also calls this case "a firmware-fault case of limited duration", but the modelled case runs 3 h, and no duration bound (for example REQ-SYS-180, HZ-003 K10) is credited or analysed. **Fix:** put every case-to-sink and junction-to-case input at its adverse end in the adverse backstop case, and state which inputs that is. If the case is still above 110 C, either bound the fault duration by an analysed control (REQ-SYS-180 or REQ-SYS-055 with its reasoning), or take the REQ-SYS-181 plan's "else they change by CR" branch and route it through Q-1 | Open | Pending | |
| finding-2 | reviewer | Major | CK-ANA-E3, CK-ANA-E5, CK-ANA-J2 | note sections 4.2, 6 (REQ-SYS-118 rows), 8 item 2, 9 (REQ-SYS-118 row); C15, C19 | The proposed REQ-SYS-118 value (83.9 C computed, 83 C +/-3 C proposed) rests on C15 (109.93 C against 110 C, margin 0.07 K) and C19 (89.72 C against 90 C). Both are labelled PASS with no band, although the note's own pass rule (section 1) needs value plus band within the limit. The only uncertainty evaluated for them is C16/C20 (FAIL). The note says the all-adverse value of 76.5 C "is the value the bench rule of section 8 falls back to if the bench shows the adverse terms". But section 8 item 2 measures only the sensor offset and lag. No bench step shows Rth(ch-case), the spreading term, the stage-1 share or the supply feed. Reviewer runs at 83.9 C, +3 C edge, sensor adverse, with one more input at the adverse end of its own range: `a5_rjc2` 2.64 gives junction **111.9 C**; `r_spread_x` 0.3 gives **111.3 C** with case 91.0 C; `a5_bond` 75 um gives **111.0 C** with case 90.8 C. The note's own bench-supply term (`r_feed` 0) alone gives 112.7 C. The largest setpoint that holds both limits is **81.8 C** with only `a5_rjc2` +10 % added, and **77.3 C** with rjc2, bond, spreading, `k_tim` and stage-1 share adverse (feed kept). The offset step also cannot bound f as written. It infers f from dR = (1 - f) x P x R_if, with R_if unknown over 0.24 to 0.72 K/W (3:1). For example, dR = 1.0 K at the 3.5 W average fits any f from 0 to 0.6. The expected dR (about 0.7 to 1.5 K) is also of the order of the uncertainty of an NTC read through firmware against a K bead, and the note states no measurement uncertainty. **Fix:** either propose the setpoint on a stated set that includes the inputs no bench step measures (and name the set), or give C13 to C20 a band over the non-sensor inputs, report C15 and C19 OPEN, and put both values to the owner in Q-1 with what each means. Also rewrite section 8 item 2 so that it bounds f with a stated uncertainty (for example, a bead on the flange top beside the NTC), and so that it says which adverse terms the bench can show and which it cannot | Open | Pending | |
| finding-3 | reviewer | Major | CK-ANA-F3, CK-ANA-D2 | `a5_closure.py` `cap_pattern` line 379 (trip = setpoint, nominal sensor); note sections 4.1, 6 (duty-cap row), 7 item (2), 8 item 4 | The "worst pattern the cap allows" trips the inhibit at the setpoint with nominal sensor inputs. The inhibit then cuts the bursts to 28.3 % key-down, so the pattern is milder than the cap. The sensor state that lets the most key-down through is the one the note itself calls governing (+3 C edge, offset and lag adverse). Reviewer re-run of the same pattern in that state, 4 h from a 45 C soak, last hour: key-down **33.3 %**; hottest PETG face **56.4 C** (note 55.2 C); junction 109.4 C; case 89.2 C; PA-bay air 58.8 C; cells 51.9 C; main-bay air 51.8 C. That PETG value is 1.3 K above the steady value at the cap, which contradicts section 4.1 ("none passes the steady value at the cap by more than 1.2 K"). With the C03 band (+4.0 K) it reaches 60.5 C against 60 C, so it is OPEN under the note's rule. The duty-cap basis in the section 6 block (PETG 55.2 C) and the CR-003 Q4 filament thresholds of section 7 item (2) and section 8 item 4 (60.1 C, and 64.2 C with the band) follow from the milder pattern. The same rule gives about 61.5 C and 65.5 C on the reviewer's run. **Fix:** run the cap pattern in the sensor state that lets the most key-down through (or with the inhibit off, as the bound), carry the result into the generated block and sections 7 and 8, and state its verdict with a band | Open | Pending | |
| finding-4 | reviewer | Minor | CK-ANA-A3, CK-ANA-A4 | note section 3 row "LM2940 operating junction"; `a5_closure.py` line 73 | The part named is the LM2940CT-5.0, which is the LM2940C grade. SNVS769J p.4 (section 6.3) gives 0 to 125 C for "LM2940C NDE". The -40 to 125 C range the note cites is the LM2940-N NDE row. The 125 C upper limit used in C26 and C27 is the same, so no number changes. Cite the LM2940C row | Open | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-A4, CK-ANA-B6 | note section 3 rows "LM2940 RthJC(bot)" and "LM2940 tab to sink"; `r_lm_jc`, `r_lm_if` | The 1.1 C/W RθJC(bot) is correct at SNVS769J p.5, but that table is for a JEDEC test mount. The same datasheet's heatsinking section (p.19, 10.3.1) says "A value of 3°C/W can be assumed for RθJC", with RθCS "from about 0.5°C/W to about 2.5°C/W" (2 C/W if unknown). The note fixes RθJC at 1.1 and ranges the tab from 0.4 to 1.0 K/W, which does not cover the datasheet's own guidance. The effect is on the LM2940 junction only: about +2.8 K at 0.73 W, so C27 goes to about 103 C against 125 C, and no verdict changes. Widen the ranges, or justify the narrower ones | Open | Pending | |
| finding-6 | reviewer | Minor | CK-ANA-D2 | note sections 2 (L-2 row) and 4.1 ("0.8 W of the main bay's 2.1 W") | The model moves `p_lm(v)` = 0.9 - 0.1 x 0.6 x 2.9 = **0.726 W** (the D-5 PWM hold relief included), not 0.8 W. Quote the model value, or say that 0.8 W is rounded up | Open | Pending | |
| finding-7 | reviewer | Minor | CK-ANA-C3, CK-ANA-D2 | note section 2 ("At 40 % the cells (52.7 C, band +3.2 K) and the PETG face (56.1 C, band +4.0 K) are OPEN (author exploration ...)") | The basis for choosing 35 % over 40 % is a banded result that the committed runner does not produce: `duty_sweep.csv` holds nominal values only. One command should reproduce every number (charter section 11 rule 8). Either generate the 40 % bands in the run, or cite only the nominal sweep | Open | Pending | |
| finding-8 | reviewer | Minor | CK-ANA-A6 | note section 10 D-19, Q-5 | SNVS769J p.1 and p.15 require the output capacitor (at least 22 uF, ESR 100 mohm to 1 ohm) to keep that capacitance and ESR over the operating temperature range, and to sit close to the regulator. With the regulator on the sink, the capacitors sit next to a web that reaches 85.0 C under the inhibit (C21) and 98.8 C with the backstop alone. The note gives no temperature for that location and makes no rating request to WP-PDR-37. Add the local temperature bound and the capacitor rating to Q-5 | Open | Pending | |
| finding-9 | reviewer | Minor | CK-ANA-E3 | note sections 6 and 8 item 1 (8.03 and 6.42 K/W) | The bench acceptance values are model crossings with no allowance for the bench's own measurement uncertainty: K thermometer accuracy on a rise of about 34 to 40 K, the power reading, and room drift. A measured R just under 8.03 K/W would pass while the true value is above it. State the measurement uncertainty and lower the acceptance by it, or state the guard band | Open | Pending | |
| finding-10 | reviewer | Minor | CK-ANA-B4 | note sections 2 and 13; `closed_loop` dt 0.1 s (inhibit), 0.2 s (backstop, cap pattern); `periodic_peak` dt 0.25 s, 30 cycles | The numerical settings of the closed-loop and periodic cases are not stated in the note, and C15 sits 0.07 K from its limit. Reviewer check: halving dt to 0.05 s moves C15 from 109.930 to 109.926 C and C19 from 89.718 to 89.714 C, so no result moves. State the settings and this convergence check in the note | Open | Pending | |
| finding-11 | reviewer | Minor | CK-ANA-A6 | note sections 1 ("Not in scope"), 10 | The note is the WP-PDR-28 output file. Two WP-PDR-28 outputs are neither answered nor assigned to 28b: "whether a firmware thermal fold-back requirement is needed (software reader G-14)" and the "A11 stop criterion input (with WP-PDR-43)" (plan section WP-PDR-28 Outputs). HZ-003 K2 also names a power fold-back ahead of the inhibit. State where each is answered | Open | Pending | |

Finding rules: state words appear only in the State column.

### Per-case results (A5-CL, the proposed design, 45 C unless stated; checker output of note section 5; margin = limit - result)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C01 | junction peak, 35 % cap, 13 s key-downs | REQ-SYS-112 110 C (proposed corner) | 100.1 C, OPEN | +9.9 K | +11.6 K RSS (+4.3 K without the sink path) | re-run: same value | none |
| C02 | module case, 35 % cap, steady | RA07M1317M p.8 guidance 90 C | 76.3 C, PASS | +13.7 K | +10.9 K | re-run: same | none |
| C03 | hottest PETG face, 35 % cap | TS-012 7.3 (c) 60 C | 55.1 C, PASS | +4.9 K | +4.1 K | re-run: same; cap pattern gives 56.4 C | finding-3 |
| C04 | PA-bay air, 35 % cap | G5V-2 ambient 65 C | 56.6 C, PASS | +8.4 K | +4.9 K | re-run: same; relay_hold 1.0 gives 59.64 C (tornado row) | none |
| C05 | cells, long session, 35 % cap | TS-012 7.3 (a) extended 55 C | 52.0 C, PASS | +3.0 K | +2.9 K | re-run: same | none |
| C06 | main-bay air, long session, 35 % cap | 55 C | 51.0 C, PASS | +4.0 K | +2.8 K | re-run: same | none |
| C07 | FR4 end wall, 35 % cap | design limit (E) 105 C | 60.5 C, PASS | +44.5 K | +4.6 K | re-run: same | none |
| C08 | cells after 30 min at 50 % | TS-012 7.3 (a) 55 C | 49.2 C, PASS | +5.8 K | +1.8 K | re-run: same | none |
| C09 | main-bay air after 30 min at 50 % | 55 C | 51.0 C, PASS | +4.0 K | +3.1 K | re-run: same | none |
| C10 | junction, 5 min continuous from a 45 C soak | HZ-003 K7 110 C | 108.8 C, OPEN | +1.2 K | +6.6 K | re-run: same | none |
| C11 | junction, 180 s continuous from a 45 C soak | HZ-003 K10 110 C | 97.0 C, PASS | +13.0 K | +5.0 K | re-run: same | none |
| C12 | hottest accessible surface, 25 C, 5 min continuous | REQ-SYS-113 48 C (TBR) | 32.7 C, PASS | +15.3 K | +2.6 K | re-run: same | none |
| C13 / C17 | inhibit at 83.9 C, key held 60 min: nominal | REQ-SYS-112 110 C / case 90 C | 105.7 / 85.5 C | +4.3 / +4.5 K | no band | re-run: same | none |
| C14 / C18 | same, +3 C tolerance | 110 C / 90 C | 108.7 / 88.4 C | +1.3 / +1.6 K | no band | re-run: same | none |
| C15 / C19 | same, +3 C, sensor offset and lag adverse (governing) | 110 C / 90 C | 110.0 (109.93) / 89.8 (89.72) C | +0.07 / +0.28 K (unrounded) | no band; the dt halving moves it by 0.004 K | re-run: same; one device input adverse gives 111.0 to 111.9 C | finding-2, finding-10 |
| C16 / C20 | same, all adverse (note set) | 110 C / 90 C | 117.1 / 91.4 C, FAIL | -7.1 / -1.4 K | n/a | re-run: same | finding-2 |
| C21 | sink, inhibit, governing case | REQ-SYS-181 lower edge 92 C | 85.0 C | +7.0 K | no band | re-run: same | none |
| C22 / C24 / C26 | backstop alone at 98 C, key held 3 h: nominal | channel 175 C / Tcase(OP) 110 C / LM2940 125 C | 123.4 / 103.2 / 99.5 C | +51.6 / +6.8 / +25.5 K | no band | re-run: same; with r_spread_x 0.3: case 106.0 C | none |
| C23 / C25 / C27 | same, Rth and dissipation adverse (note set) | 175 / 110 / 125 C | 132.6 / 106.9 / 100.0 C | +42.4 / +3.1 / +25.0 K | no band | re-run: same; with r_spread_x 0.3 and k_tim 0.6 added: 137.0 / **111.3** / 99.9 C | finding-1, finding-5 |
| CP | worst cap pattern, 4 h, last hour (note: nominal sensor) | 55 / 60 / 65 / 110 / 90 C | cells 51.2, PETG 55.1 (block 55.2), bay 57.8, junction 105.0, case 84.9 C | +3.8 / +4.8 / +7.2 / +5.0 / +5.1 K | no band | reviewer, governing sensor state: 51.9 / 56.4 / 58.8 / 109.4 / 89.2 C, key-down 33.3 % | finding-3 |
| S | D-6 alternative duty limit on the sink NTC | REQ-SYS-112 110 C for a 13 s key-down | S = 82.2 C, 79.2 C as programmed | floored | n/a | hand calculation: 110 - 8.439 x 2.4 - 9.939 x 0.503 - 10.665 x 13 / 56.07 = 82.27 C | none |
| BA | bench acceptance at 5.0 / 10.0 W | junction plus non-sink band 110 C; case plus band 90 C | 8.03 / 6.42 K/W (nominal 6.77 / 5.58) | crossing at k_orient 1.692 | non-sink band +4.34 K (junction), +1.86 K (case) | re-run: same; at k_orient 1.70 the box stays within limits (cells 52.0 C, PETG 55.9 C) | finding-9 |

### Readiness criteria

| # | Answer | Evidence |
|---|---|---|
| R1 | Yes | `git rev-parse afa80b4:<path>` gives every `product_files` blob; unchanged at HEAD `391f0e5` (`git status` clean for these paths). `thermal_model.py` and `ts012_thermal.py` have the same blobs at `35fc7ee` and `afa80b4` (54573514, 3eb26aaa), so the INSP-112 files are unchanged as the note says |
| R2 | Yes | `.venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id rv-2026-09-29` in a `git archive afa80b4` export: "CHECK PASS", exit 0, 416 s. Wrapper line "PASS deck=thermal_a5cl.net sha256=d8c42384...2823e59 version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0" (TV-014 wrapper blob 88b71475: precondition and time-out guard) |
| R3 | N/A | no JSON file under a schema in the product |
| R4 | Yes | author return and note sections 1 to 13 (question, inputs, results, margins, limitations, proposed values, tools and evidence status) |
| R5 | Yes | vector search, then grep: no `TBD` in the note; REQ-SYS-112, 113, 118, 181 and 155 carry `tbr` objects in `requirements.json` |
| R6 | Yes | the 6 embedded figures and `cl_bench_acceptance.png` exist in the run directory |

### A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Section 1 states the seven plan items (plan section 3.0 row 28, 28a, quoted correctly). REQ-SYS-055, 112, 113, 118, 150, 155, 181, HZ-003 (K2, K7, K9, K10), HZ-007, RSK-006, 007 and 026 exist in their files |
| CK-ANA-A2 | Yes | D-1 to D-6 of TS-012 section 8.14 and CR-003 revision 4 (`114b68f`) are named. The AT RISK header names CR-003 revision 4 and CR-018 (rule C13) |
| CK-ANA-A3 | No | finding-4 (LM2940 grade row). Otherwise every added input has a source or is labelled E or R |
| CK-ANA-A4 | No | Reviewer check, against the datasheets fetched 2026-09-29. RA07M1317M, SHA-256 5a847a09..., equal to the `hardware/sim/tx-pa/README.md` record: p.1 "GND (FIN)"; p.2 Tcase(OP) -30 to +110 C; p.8 flatness under 50 um, the case guidance quote, the 175 C channel quote, stage table (stage 2 Rth(ch-case) 2.4 C/W, stage 1 1.4 W). LM2940 SNVS769J (SHA-256 54cf633a...): p.3 NDE pin 4 GND (tab); p.5 RθJC(bot) TO-220 1.1 C/W; p.4 max junction 150 C, operating to 125 C; p.15 COUT at least 22 uF, ESR 100 mohm to 1 ohm. Disagreements: finding-4, finding-5. The OD-01 quote equals status note 2026-09-29 section 8. The CR-003 5 K rule and the 69 C typical PETG agree with CR-003 revision 4. Hand check: p_pa = (8.4 - 0.26 x 1.97) x 1.97 - 5.6 = 9.94 W. The 112 inherited inputs were checked under INSP-112 and are not re-checked here |
| CK-ANA-A5 | Yes | Section 2 bounds each lever. The duty cap and the 10 min window are R-class proposals for the owner (section 9). The 45 C ambient is REQ-SYS-112's |
| CK-ANA-A6 | No | Requests Q-1 to Q-8 route each consequence, and no requirement file is edited. Gaps: finding-8 (capacitor rating request), finding-11 (fold-back and A11 outputs) |

### B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | Yes | The model of INSP-112 is unchanged. L-2 adds the LM node on the sink through RthJC(bot) plus the tab joint. The model's LM2940 source is session-constant (on equals off, `thermal_model.py` line 502), so moving it from both `src_on` and `src_off` is consistent. Limitations 1 to 6 state the simplifications |
| CK-ANA-B2 | Yes | No vendor model. The datasheet values are used inside their stated ranges (Tcase(OP) up to 110 C, LM2940 to 125 C) |
| CK-ANA-B3 | Yes | The A5-DC values that do not depend on the duty limit equal run `2026-09-28-ts012-r2` (section 2). The LTspice analogue agrees to 0.013 K. The note says this checks the solver, not the physics, and there is no bench correlation (limitation 1) |
| CK-ANA-B4 | No | finding-10 (the settings are not stated; the reviewer's dt halving shows no result moves) |
| CK-ANA-B5 | Yes | Hand calculation of S (82.27 C against the runner's 82.2 C floored) and of p_pa (9.94 W). An independent re-run of the backstop, inhibit and cap-pattern cases on different input sets (findings 1 to 3), and a dt halving |
| CK-ANA-B6 | No | The RSS tornado covers C01 to C12. C13 to C27 carry no band, and the explicit "adverse" sets omit in-range inputs that move them (finding-1, finding-2). LM2940 path ranges: finding-5 |

### C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | LTspice `.log` first line "LTspice 26.0.2 for MacOS". Python 3.13.5, numpy 2.5.3, matplotlib 3.11.2 and spicelib 1.6.3, read from the venv, equal the lock rows |
| CK-ANA-C2 | Yes | TV-014 is accredited for LTspice. The numpy, matplotlib and spicelib results are marked developer evidence (note header "Evidence status"), and no requirement is closed |
| CK-ANA-C3 | No | One command reproduces the run, and the deck is a netlist through the wrapper. Exception: finding-7 (the 40 % bands are author exploration outside the runner) |
| CK-ANA-C4 | Yes | Reviewer re-run at `afa80b4` (R2). `verdict_set.csv`, `summary.csv`, `bands.csv`, `tornado.csv`, `inhibit.csv`, `backstop.csv`, `cap_pattern.csv`, `bench_acceptance.csv`, `duty_sweep.csv`, `inputs.csv`, the seven PNGs and `thermal_a5cl.net` are byte-identical. `results.md` differs only in the run id and run time |
| CK-ANA-C5 | Yes | TV-014 limitations: the wrapper's path length, lock and Wine session end are respected (wrapper PASS line). The `.raw` is 934,182 bytes, under the CR-017 C2 5,000,000-byte limit |

### D. Units, arithmetic and consistency of numbers

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | C and K, W, K/W, J/K; the electrical analogue units are stated in the deck header |
| CK-ANA-D2 | No | Sections 5 and 6 are generated and checked. Hand-written numbers checked: 20.3 K (8.44 W x 2.4), 4.2 K (100.1 - 95.9; 76.3 - 72.1), 3.5 K cells, 59.6 C bay under the inhibit (59.55), 59.7 C at hold 1.0 (59.64), 83.9 → 83 C, 76.5 → 76 C, 0.67 x dR (0.40 / 0.60). Differences: finding-3 (cap-pattern claims), finding-6 (0.8 W), finding-7 |
| CK-ANA-D3 | Yes | `up1` rounds results up. S and the bench acceptance are floored. 83.9 → 83 C and 76.5 → 76 C are floored |
| CK-ANA-D4 | Yes | Limits come from `Param` rows with their ids (tj_limit REQ-SYS-112; case_guid p.8; tcase_op_max p.2; tch_max p.8; lm_tj_max p.4), compared as "x > lim is FAIL" |

### E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | The datasheet quotes are verbatim at the pages cited (A4). The TBR plans are quoted from `requirements.json` and match |
| CK-ANA-E2 | Yes | Limit minus result; no TPM threshold applies |
| CK-ANA-E3 | No | finding-1, finding-2, finding-9 |
| CK-ANA-E4 | Yes | `--check` recomputes every criterion, including its verdict word, and fails on any line that differs. So any change of a pass, fail or margin exits 1. The FAIL rows C16 and C20 are expected results stated in the note, as in INSP-112 |
| CK-ANA-E5 | No | Section 9 gives id, value, tolerance, basis and plan step for each. The REQ-SYS-118 value is not supported as stated (finding-2), nor is the REQ-SYS-181 "confirmed" branch (finding-1). The note edits no requirement file |
| CK-ANA-E6 | N/A | no TPM value is proposed (Q-7 routes the summary to WP-PDR-29) |
| CK-ANA-E7 | Yes | No closure is claimed. REQ-SYS-112 and 113 are Analysis-method, and the evidence is developer evidence on preliminary design data. REQ-SYS-118 and 181 are Test-method, and this analysis is supporting evidence |

### F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | Yes | REQ-SYS-112 (45 C, 5 W step: continuous, now the duty corner), REQ-SYS-113 (25 C, 5 min), REQ-SYS-118 (threshold and response), REQ-SYS-181 (95 C +/-3 C edge), HZ-003 K7 (50 % duty and 5 min continuous) and K10 (180 s), and the seven plan items each have a row |
| CK-ANA-F2 | Yes | Stuck key or firmware hung (backstop alone), key held under the inhibit, and the failed PWM hold (relay_hold 1.0) are analysed |
| CK-ANA-F3 | No | finding-1, finding-2, finding-3 |
| CK-ANA-F4 | Yes | The tornado gives the two largest inputs for every banded metric (`bands.csv`, section 4.3) |

### G3. Thermal (G1 answered for the deck; G2, G4 to G7 N/A except G7 below)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G3-1 | Yes | Dissipation at the TS-012 7.3 corner (9.94 W), marked AT RISK on WP-PDR-21 and 22. The 13 s key-down is the REQ-SYS-055 maximum. The duty is the proposed cap |
| CK-ANA-G3-2 | Yes | Sourced or classed (inputs.csv), apart from findings 4 and 5 |
| CK-ANA-G3-3 | Yes | Junction, case (guidance and rating), channel, LM2940 junction, cells, PETG, FR4, relay ambient, accessible surface |
| CK-ANA-G3-4 | Yes | Steady states are used only for the box at a fixed duty. Transients (with stated capacities) are used for the junction, the inhibit, the backstop and the pattern |
| CK-ANA-G1-1 to G1-4 | Yes | The deck and plot sit beside the run. One `.tran`, no `NC_` net (wrapper). The analogue is linearized at the cap, as stated. The checker reads `thermal_a5cl.raw` through spicelib |
| CK-ANA-G7-1 | Yes | One-at-a-time RSS plus explicit extreme cases, stated in sections 2 and 5. The adequacy of the extreme sets is finding-1 and finding-2 |

### H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes | Q-2 to the `hazards.json` writer (HZ-003 K2, K7, K9; HZ-007) |
| CK-ANA-H2 | Yes | Q-6 to WP-PDR-18 (RSK-006, RSK-007) |
| CK-ANA-H3 | Yes | Change log revision 0 |

### I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | All 7 renders opened with the Read tool: `cl_box_vs_duty.png`, `cl_inhibit_backstop.png`, `cl_cap_pattern.png`, `cl_bench_acceptance.png`, `cl_margins.png`, `cl_tornado.png`, `cl_ltspice_crosscheck.png`. The reviewer's re-run renders are byte-identical |
| CK-ANA-I2 | Yes | Axes with units, limits drawn and labelled with their ids, legends and case titles. Marked values agree with `results.md`: inhibit legend 109.9 and 89.7 C, backstop 123.4, 103.1 and 132.6, 106.8 C; pattern J2 105.0 C and case 84.8 C; bench 8.03 and 6.77 K/W; LTspice 0.013 K. The plot legends round to nearest while the block rounds up, which is consistent |

### J. Software assurance items

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-J1 | Yes | CK-ANA-C2: the LTspice cross-check is accredited (TV-014). The Python results are marked developer evidence and close nothing |
| CK-ANA-J2 | No | swe-134 7.1 tasks 1 and 6: the REQ-SYS-118 value is the HZ-003 K2 control threshold. As proposed, it holds the REQ-SYS-112 limit only at nominal device inputs, and its bench verification cannot bound the terms it depends on (finding-2) |
| CK-ANA-J3 | Yes | Front matter `assurance_tasks_applied`. swe-070 task 1: results in J1. swe-134 tasks 1 and 6: results in J2 |

ITEMS N/A: CK-ANA-R3, CK-ANA-E6, CK-ANA-G2, G4, G5, G6 (analysis_kind thermal, simulation-deck, worst-case), CK-ANA-G7-2 (no part derating rule is set here).

### Reviewer evidence (scratchpad, not committed)

- Export and re-run: `git archive afa80b4` into the reviewer scratchpad, `a5_closure.py --check --run-id rv-2026-09-29`: CHECK PASS, exit 0.
- Independent cases (`rv_cases.py`, `rv_cases2.py`, importing the frozen runner unchanged):
  - backstop with the note's adverse set plus `r_spread_x` 0.3 and/or `k_tim` 0.6 (case 110.00 / 108.17 / 111.33 C);
  - inhibit at 83.9 C with one more adverse input (junction 111.02 to 111.95 C; r_feed 0 112.74 C);
  - setpoints with the device inputs adverse (81.8 C, 77.3 C);
  - the cap pattern in the governing sensor state (key-down 33.3 %, PETG 56.43 C);
  - dt 0.05 s (109.926 C).

### Verdict format

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/thermal-budget.md@d7f6a409, hardware/sim/thermal/a5_closure.py@834c217a, run 2026-09-29-a5-closure-r1 at afa80b4
FINDINGS:
- [Major] CK-ANA-F3/E3 finding-1: REQ-SYS-181 backstop-alone adverse case omits r_spread_x and k_tim; module case 111.3 C > 110 C Tcase(OP) (p.2); "confirmed" not supported.
- [Major] CK-ANA-E3/E5/J2 finding-2: REQ-SYS-118 83 C holds 110 C only at nominal device inputs (0.07 K); one in-range input gives 111.0 to 111.9 C; bench rule cannot bound f or see those inputs.
- [Major] CK-ANA-F3/D2 finding-3: cap pattern run with the nominal sensor; governing sensor state gives PETG 56.4 C (60.5 C with band, OPEN), not 55.2 C.
- [Minor] finding-4 LM2940C grade row; finding-5 LM2940 RthJC/RthCS ranges vs p.19; finding-6 0.8 W vs 0.726 W; finding-7 40 % bands outside the runner; finding-8 LM2940 capacitor temperature; finding-9 bench measurement guard band; finding-10 numerical settings; finding-11 fold-back and A11 outputs.
ITEMS N/A: CK-ANA-R3, E6, G2, G4, G5, G6, G7-2
VALUES PROPOSED: REQ-SYS-112 35 % corner (supported as a proposal once the finding-3 cap pattern is fixed); duty cap 35 %/10 min (not supported until finding-3); REQ-SYS-118 83 C +/-3 C (not supported, finding-2); REQ-SYS-181 confirmed (not supported, finding-1); REQ-SYS-113 48 C (supported); bench 8.03/6.42 K/W (supported with finding-9); S 79.2 C (supported)
MEASUREMENTS: size=51 verdict cells + 7 reviewer cases; inputs_checked=12 added + 9 datasheet values; renders=7; turns=45; minutes=70; major=3; minor=8
```

## Iteration 2 (delta on the Major fixes, rule C1)

**Scope.** Rule C1: this iteration verifies the fixes of the three Major findings of iteration 1 and nothing else.
- Revision 1 of the note (`6eb014c`) changes sections 1, 2, 3, 4.1, 4.2 and 5 to 11, and adds section 15.
- The runner `a5_closure.py` adds the governing-state screens, the REQ-SYS-181 search and the cap-pattern box bound.
- The unchanged parts are not re-reviewed: the C01 to C12 method, the tornado, the bench acceptance and the LTspice deck. Their re-run values are compared only as a regression check.

### Readiness (R1 to R6)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes | Every `product_files` blob is `git rev-parse 6eb014c:<path>`. The note and `hardware/sim/thermal/` are unchanged from 6eb014c to HEAD. `thermal_model.py` and `ts012_thermal.py` have no diff since afa80b4 and carry the SHA-256 recorded by the TS-012 README. Run r1 and the TS-012 runs have no diff between afa80b4 and 6eb014c |
| R2 | Yes | From a `git archive 6eb014c` export, `.venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id rv-it2` printed "CHECK PASS", exit 0, run time 2112 s |
| R3 | N/A | No JSON file under a schema in the product |
| R4 | Yes | The author's summary and note section 15 state the three fixes with their numbers, the new proposals, the run and the checker result |
| R5 | Yes | No `TBD` in the note. The TBRs relied on (REQ-SYS-112, 113, 118, 181) are named, with each plan quoted in section 9 |
| R6 | Yes | The 8 PNGs are in `results/2026-09-29-a5-closure-r2/` |

### Re-run from an export of the freeze commit (CK-ANA-C4)

- **Export and command.** Export: `git archive 6eb014c | tar -x` into the reviewer scratchpad. Command: `CWHT_LTSPICE_LOCK_WAIT=14400 .venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id rv-it2`. Result: exit 0, "CHECK PASS: the record's verdict set and proposed values equal the computed ones; LTspice within 0.5 K".
- **CSV outputs.** All 13 are **byte-identical** to the committed run r2: backstop, backstop_screen, bands, bench_acceptance, cap_pattern, cap_pattern_verdicts, duty_sweep, inhibit, inputs, protection_screen, summary, tornado, verdict_set. `results.md` differs only in the run-time line (2112 s against 2513 s).
- **LTspice.** The netlist is byte-identical. The re-run `.log` first line is "LTspice 26.0.2 for MacOS". The largest difference is 0.012 K, PASS.
- **Stage messages.** They equal `run-stdout.txt`: inhibit proposal 72.0 C, REQ-SYS-181 proposal 92 C.

### Independent checks (CK-ANA-B4, B5, F3)

All checks were run with the unchanged `a5_closure.py` functions of the export (reviewer scratchpad scripts `side1.py` to `side3.py`). Plot: `reviewer_side_checks.png` (opened).

| Check | Result | Reading |
|---|---|---|
| Hand check, channel minus case in the backstop governing state: P2 x Rth(ch-case)2 = 9.748 W x 2.64 K/W | 25.73 K. Model at the SRR edge: 137.03 - 111.33 = 25.70 K. Inhibit governing state: 108.58 - 82.96 = 25.62 K | agrees within 0.1 K |
| Hand check, governing dissipation and interface: P_pa = 8.4 V x 1.97 A - 5.6 W; r_if = 75 um / (0.6 W/m K x 1.42 cm2) + 0.3 K/W | P_pa = 10.948 W; the TS-012 note gives "10.95 on a bench supply". r_if = 1.180 K/W, so P x r_if = 12.9 K, against the model's case max minus sink max of 12.55 K (the 0.5 s re-key gaps and the case capacity lower it) | agrees |
| REQ-SYS-118 governing state at 72 C, run for 3 h instead of 60 min | 108.580 / 82.957 C, identical | 60 min is enough |
| Same, time step 0.02 s instead of 0.1 s | 108.588 C (+0.008 K) | numerics adequate |
| REQ-SYS-181 governing state at the 95 C edge, time step 0.05 s instead of 0.2 s (1 h) | case 108.537 against 108.551 C | numerics adequate |
| REQ-SYS-181 comparator hysteresis at 3 C and 10 C (its input range; not stacked) | case 108.536 and 108.545 C, against 108.553 C nominal | no effect: the finding-1 fix holds |
| **REQ-SYS-118 inhibit re-arm hysteresis at 3 C and 10 C.** The input is `inh_hyst`, 5 C (3 to 10), class E, "value not yet set". It is not stacked and not in the band | Governing state at 72 C: junction **108.907 C** at 3 C (+0.33 K), 107.371 C at 10 C. **Every-input stack at 72 C with 3 C: 110.27 C**, over 110 C. The stack's own largest setpoint lies between 71.5 C (109.79 C) and 71.8 C (110.08 C) | finding-21 |
| **REQ-SYS-118 governing state with the flange NTC fraction f beyond its 0.40 upper end** | f = 0.5: 109.19 C, 109.64 C with the band. f = 0.6: 109.89 C, 110.34 C with the band (over the limit) | finding-22 |
| **Cap pattern with 3.0 min of key-down in each window.** The burst is lengthened by 13.5/13 for the 0.5 s re-key gaps; inhibit not counted | Key-down fraction 29.99 %, against the note's 29.15 %. Last hour, reviewer run against the note: PETG face **55.56** (55.24) C; PA-bay air 58.21 (58.00) C; cells 51.43 (51.26) C; main-bay air 51.46 (51.34) C; junction 107.42 (106.58) C; case 87.21 (86.41) C | finding-20 |

### Inputs checked against their sources (CK-ANA-A3, A4: the inputs the delta adds, or uses at new ends)

| Input | Note value | Source checked | Agreement |
|---|---|---|---|
| RA07M1317M Tcase(OP); sets C17 and C20 | -30 to +110 C | `docs/research/pa-device-candidates.md` F8 (datasheet Jun 2019): "Maximum ratings: ... Tcase -30 to +110 C" | agrees |
| RA07M1317M case guidance; sets C14 | 90 C | F8: "Mitsubishi asks for case below 90 C"; `thermal_model.py` `case_guid` | agrees |
| RA07M1317M channel rating; sets C16 and C19 | 175 C (p.8) | Quoted in the note but not in F8, and the PDF was not re-read here. C16 has a 40.7 K margin, so the value does not decide | not re-checked (not deciding) |
| Rth(ch-case) 2.4 / 4.5 K/W +/-10 %; stage-1 share 1.2 to 1.8 W | stacked at 2.64 / 4.95 K/W and 1.2 W | F8: "stage 1 Rth(ch-case) 4.5 C/W at 1.5 W, stage 2 2.4 C/W at 6.5 W" | agrees |
| Drain current 1.97 A (1.79 to 1.97) | The nominal is already the adverse end, so the input is not stacked (screen rise 0) | `thermal_model.py` a5_idd | consistent |
| Feed resistance run down to 0 in the protection cases | drain at 8.4 V, P_pa 10.948 W | `v_pack` 8.4 V (R, full 2S pack); TS-012 note: "10.95 on a bench supply with no feed drop" | agrees |
| Bond line 25 to 75 um, k_tim 0.6 to 0.8 W/m K, web spreading 0 to 0.3 K/W | stacked at 75 um, 0.6 W/m K and 0.3 K/W | `thermal_model.py`, INSP-112 reviewed | agrees |
| REQ-SYS-180 behaviour, used for the fault duration | "re-arms once receive resumes" | REQ-SYS-180 statement: "end RF ... at 150 s to 180 s (TBR) of continuous transmit and hold it off until receive resumes" | agrees |
| REQ-SYS-131 scope | a hung firmware only | REQ-SYS-131 statement: "reset its controller ... within 2 s (TBR) of a firmware hang" | agrees |
| REQ-SYS-181 TBR plan | quoted in section 9 | `docs/requirements/sys/requirements.json` line 5588: "... confirms them against the device rating, else they change by CR." | verbatim |
| Duty-cap definition (L-1) | "key-down time in the last 10 min would exceed 30 % of it (3.0 min in any 10 min window)" | Note section 2, and the proposed requirement text of section 9 | The pattern run does not reach this cap: finding-20 |
| Inhibit re-arm hysteresis | 5 C (3 to 10), E, value not yet set | `thermal_model.py` `inh_hyst` | Held at 5 C in every protection case: finding-21 |

### Checklist answers (delta scope)

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Sections 1, 9 and 15 name REQ-SYS-112, 113, 118, 131, 180 and 181, HZ-003 and HZ-007; every id exists |
| CK-ANA-A2 | Yes | AT RISK row: CR-003 revision 4 and CR-018 are not dispositioned |
| CK-ANA-A3 | Yes | Section 3 table, and the classes in `inputs.csv` |
| CK-ANA-A4 | Yes | Table above. The 175 C channel figure was not re-checked and does not decide |
| CK-ANA-A5 | **No** | Two assumptions that set a proposed value are not bounded: (a) the cap pattern puts the 0.5 s re-key gaps inside a 3.0 min burst, which is not the worst the stated cap allows (finding-20); (b) the inhibit re-arm hysteresis is held at 5 C, not at its 3 C end, and is not stated as a constraint on WP-PDR-35 (finding-21) |
| CK-ANA-A6 | Yes | Q-1 to Q-8 route every consequence. This includes REQ-SYS-181 as a change of an owner-ruled value, and the REQ-SYS-181 verification-note fixture point that falls inside the new 89 to 95 C band |
| CK-ANA-B1 | Yes | The closed-loop model is unchanged in kind. Section 11 item 7 states the one-setpoint screen |
| CK-ANA-B3 | Yes | LTspice cross-check 0.012 K (re-run identical). No bench correlation yet, as the note states |
| CK-ANA-B4 | Yes | Reviewer: the time step and the run duration do not move C13 or C17 (table above) |
| CK-ANA-B5 | Yes | The hand checks of the channel-to-case rise and of the governing dissipation agree (table above) |
| CK-ANA-B6 | Yes | Every row C13 to C25 now has a band, as the section 1 rule requires. The protection-case rule is stated and implemented (`screen`, `stack_from`, `rss`) |
| CK-ANA-C1 to C5 | Yes | The re-run is identical. The results are marked developer evidence. LTspice ran through the wrapper |
| CK-ANA-D1, D4 | Yes | The limits in `a5_closure.py` are traceable: `tcase_op_max`, `tch_max`, `lm_tj_max`, `case_guid`, `petg_crit` |
| CK-ANA-D2 | Yes | Sections 4.1 and 4.2 were cross-checked against `results.md` with no disagreement. Examples: 108.58 → 108.6; 82.96 → 83.0; 111.33 → 111.4; 134.25 → 134.3; 3.7 min; 91.8 %; 17.49 → 17.5 %; 13.65 → 13.7 %; bay +2.3 K, PETG +1.3 K, main-bay +0.9 K; LM2940 74.66 → 74.7 C; 25.6 K |
| CK-ANA-D3 | Yes | Values are rounded up toward the limit (`up1`); the bench acceptance is floored |
| CK-ANA-E1 | Yes | Tcase(OP), the channel rating, the LM2940 limit and the 90 C guidance are quoted with their pages |
| CK-ANA-E2, E3 | Yes | After their bands, C13 has a 0.97 K margin and C17 has 0.71 K; both stay above zero. C20 is reported as FAIL, not as passing |
| CK-ANA-E4 | Yes | `--check` compares both generated blocks and fails on any difference. The verdict words come from `_row` |
| CK-ANA-E5 | **No** | Two proposed values change once the inputs of finding-20 and finding-21 are taken at their worst: the HDT thresholds (60.3 / 64.4 C become 60.6 / 64.7 C), and REQ-SYS-118 under the note's own "at or below both" rule (72 C becomes 71 C, unless a hysteresis of at least 5 C is made a requirement). REQ-SYS-181 (92 C; the "else they change by CR" branch is triggered and stated) and REQ-SYS-112 (30 %) are supported |
| CK-ANA-E7 | Yes | No closing credit is claimed. REQ-SYS-118 and 181 are Test-method requirements, and the values are proposals |
| CK-ANA-F1 | Yes | REQ-SYS-181's case is the sink-temperature trip with the firmware defeated; both 95 C and 92 C are run against Tcase(OP), the channel rating and the LM2940 limit. REQ-SYS-118's case is the key held at 45 C |
| CK-ANA-F2 | Yes | The fault duration is now stated (not bounded; REQ-SYS-180 not credited), as finding-1 asked |
| CK-ANA-F3 | **No** | The worst case of the cap pattern and the worst hysteresis of the inhibit are not taken (finding-20, finding-21). The backstop worst case is complete: the comparator hysteresis was checked and has no effect |
| CK-ANA-F4 | Yes | `cl_protection_screen.png` shows the sensitivities of both protection cases |
| CK-ANA-G3-1 to G3-4 | Yes | Dissipation at the governing 8.4 V supply. Transients for the protection cases. Steady state is used only for the box at a fixed duty |
| CK-ANA-G7-1 | Yes | The method is stated: stack the inputs that no bench step sees, then add the RSS of the rest, whose independence the RSS assumes. Acceptable |
| CK-ANA-H1 | Yes | Q-2 goes to the hazards writer: HZ-003 K2, K7 and K9; HZ-007 |
| CK-ANA-H2 | Yes | Q-6 goes to the risk register writer: RSK-006 and RSK-007 |
| CK-ANA-H3 | Yes | The change log and section 15 name revision 1 and its reason |
| CK-ANA-I1 | Yes | 8 of 8 cited renders opened at 6eb014c |
| CK-ANA-I2 | Yes | Axes, limits, legends and titles are present. The middle panel of `cl_cap_pattern.png` shows the 29.2 % the pattern holds. The top-panel title "3.0 min of held key" gives the burst span, not the key-down time (finding-20) |
| CK-ANA-J1 | Yes | LTspice is accredited. The Python stack is class B and is marked developer evidence |
| CK-ANA-J2 | Partly | The REQ-SYS-118 setpoint is a SWE-134 item j response value of the SW-SAFE thermal unit, and its basis leaves the unit's re-arm hysteresis unconstrained (finding-21). Otherwise it is consistent with HZ-003 K2, and REQ-SYS-181 still acts above REQ-SYS-118 (C15: sink 71.3 C +0.6 K against 89 C) |
| CK-ANA-J3 | Yes | The tasks are listed in the front matter |

ITEMS N/A:
- CK-ANA-B2: no vendor model.
- CK-ANA-E6: no TPM.
- CK-ANA-G1-2 to G1-4: the deck is unchanged and not in the delta.
- G2, G4, G5, G6: not this analysis kind.

### Per-case results (delta cases)

Each case is taken in the governing state as the note defines it. Values are from `results.md`; the re-run is identical.

| Case | Condition | Governing id and limit | Result | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C13 | Inhibit at 72 C, key held 60 min, 45 C, governing state | REQ-SYS-112: 110 C junction | 108.58 C | +1.42 K (+0.97 K after the band) | +0.45 K band; a further +0.33 K at a 3 C re-arm hysteresis | Re-run: same. Hysteresis 3 C: 108.91 C | finding-21 |
| C14 | same | Case guidance 90 C | 82.96 C | +7.04 K | +0.44 K | Re-run: same | none |
| C15 | same | Sink against the proposed REQ-SYS-181 lower edge, 89 C | 71.25 C | +17.75 K | +0.59 K | Re-run: same | none |
| C16 | REQ-SYS-181 alone at 92 C +/-3 C (edge 95 C), key held 3 h, governing state | Channel 175 C | 134.25 C | +40.75 K | +0.72 K | Re-run: same | none |
| C17 | same | Tcase(OP) 110 C | 108.55 C | +1.45 K (+0.71 K after the band) | +0.74 K | Re-run: same. Comparator hysteresis 3 and 10 C: 108.54 C | none |
| C18 | same | LM2940 125 C | 97.22 C | +27.78 K | +1.12 K | Re-run: same | none |
| C19 | REQ-SYS-181 alone at the SRR 95 C +/-3 C (edge 98 C) | Channel 175 C | 137.03 C | +37.97 K | +0.80 K | Re-run: same. Hand check: 25.7 K channel to case | none |
| C20 | same | Tcase(OP) 110 C | 111.33 C | -1.33 K (reported as not passing) | +0.83 K | Re-run: same | none |
| C21 | same | LM2940 125 C | 99.94 C | +25.06 K | +1.19 K | Re-run: same | none |
| C22 | Worst 30 % cap pattern, inhibit not counted, last hour of 4 h | Cells 55 C | 51.26 C | +3.74 K | +2.54 K | At 30.0 % key-down: 51.43 C | finding-20 |
| C23 | same | Main-bay air 55 C | 51.34 C | +3.66 K | +2.46 K | At 30.0 %: 51.46 C | finding-20 |
| C24 | same | PETG 60 C (TS-012 7.3 (c)) | 55.24 C | +4.76 K (+0.69 K after the band) | +4.07 K | At 30.0 %: 55.56 C (+0.37 K after the band) | finding-20 |
| C25 | same | Relay ambient 65 C | 58.00 C | +7.00 K | +4.65 K | At 30.0 %: 58.21 C | finding-20 |
| Cap step | 35 %, inhibit not counted | PETG 60 C | 56.51 C | +3.49 K; the band crosses the limit, so the case is not shown to pass | +4.02 K | Re-run: same | none |
| Usability | 30 % pattern with the inhibit at 72 C, sensor nominal and at its -3 C edge | information | 17.49 % and 13.65 % key-down | n/a | n/a | Re-run: same | none |

### Iteration 1 Major findings: disposition check

| Finding | What was asked (iteration 1, as note section 15 and the author state it) | What revision 1 does | Reviewer check | State |
|---|---|---|---|---|
| finding-1 | REQ-SYS-181 backstop alone: the web spreading and the compound conductivity were left at their favourable ends; the case was 106.9 C, PASS with no band; "limited duration" was not quantified | Stacks all 8 device, interface and supply inputs, found by a closed-loop screen at the 98 C edge, with the sink-NTC lag at 20 s, and adds the RSS of the other 80. At 95 C +/-3 C the case is 111.33 C +0.83 K, FAIL (C20). **92 C +/-3 C** is proposed: C16 to C18 PASS, and 93 C is confirmed to fail. The duration is stated as unbounded: REQ-SYS-180 re-arms, and REQ-SYS-131 covers only a hang | The re-run is identical, and 111.33 / 137.03 C are reproduced. The hand check of channel minus case agrees. The comparator hysteresis and the time step have no effect. The REQ-SYS-180 and 131 texts support the duration statement. The "else they change by CR" branch is triggered and routed (Q-1) | **Verified** |
| finding-2 | The REQ-SYS-118 setpoint, 83.9 C, held by 0.07 K with no band; single device inputs broke it; the bench fallback could not be triggered | Governing state: the sensor ends plus the same 8 inputs stacked, with the RSS band on top. The largest setpoint that holds is 72.9 C, and every swept input adverse at once gives 72.2 C. **72 C +/-3 C** is proposed (C13 108.6 +0.5 C, C14 83.0 +0.5 C). Bench item 2 now checks only the lag and the bonding | The re-run is identical, and the method is implemented as stated (`inhibit_study`). The 60 min run and the time step are adequate. The device-input gap of iteration 1 is closed. The hysteresis, a sensor-side input left at nominal, moves the proposal: new finding-21. The dependence on f is only partly stated: finding-22 | **Verified** (residual: finding-21, finding-22) |
| finding-3 | The worst cap pattern ran with the nominal-sensor inhibit cutting it (28.3 %); "1.2 K above steady"; HDT 60.1 / 64.2 C | The pattern runs with the inhibit not counted, at the cap and one step above, with the steady band. At 35 % the PETG face is OPEN, so the cap is 30 %. "1.2 K" is withdrawn. HDT 60.3 / 64.4 C | The re-run is identical. The inhibit is no longer counted in the box bound (`pattern_run(..., math.inf, ...)`), and the cap rule is applied. The pattern still holds 0.85 points less key-down than the cap allows: new finding-20 | **Verified** (residual: finding-20) |

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer (iteration 1) | Major | CK-ANA-F3, E3 | Note section 4.2 (revision 0) | The REQ-SYS-181 backstop-alone adverse case was incomplete and had no band, and the duration was not quantified. Iteration 2: fixed in revision 1 (C16 to C21, 92 C +/-3 C proposed, duration stated) | Verified | Pending | |
| finding-2 | reviewer (iteration 1) | Major | CK-ANA-E3, E5, J2 | Note sections 4.2 and 8 (revision 0) | The REQ-SYS-118 setpoint rested on the sensor-adverse case alone, with 0.07 K of margin and no band. Iteration 2: fixed in revision 1 (governing state with band, 72 C +/-3 C). The residuals are finding-21 and finding-22 | Verified | Pending | |
| finding-3 | reviewer (iteration 1) | Major | CK-ANA-F3, D2 | Note sections 4.1 and 6 (revision 0) | The worst cap pattern ran with the inhibit cutting it. Iteration 2: fixed in revision 1 (inhibit not counted, cap 30 %). The residual is finding-20 | Verified | Pending | |
| finding-20 | reviewer (iteration 2) | Major | CK-ANA-F3, A5, E5 | `a5_closure.py` `pattern_run`: the burst span is duty x window, with 13 s key-downs re-keyed after 0.5 s. Note sections 2 (case 5), 4.1, 5 (C22 to C25), 6 (HDT row), 7 item (2), 8 item 4 | The cap limits **key-down time** to 3.0 min in any 10 min window (section 2 L-1; section 9 requirement text). The "worst pattern the cap allows" puts the 0.5 s re-key gaps inside a 3.0 min burst, so it holds only 29.15 % key-down; section 4.1 says so. An operator can get 3.0 min of key-down from a 3.12 min burst. The reviewer ran the pattern at 29.99 % key-down. Last-hour maxima, reviewer run against the note: PETG face 55.56 (55.24) C; PA-bay air 58.21 (58.00) C; cells 51.43 (51.26) C; main-bay air 51.46 (51.34) C; junction 107.42 (106.58) C; case 87.21 (86.41) C. Every C22 to C25 verdict stays PASS (PETG 59.63 C with its band) and the cap stays 30 %. But the **proposed PETG heat-deflection thresholds change from 60.3 / 64.4 C to 60.6 / 64.7 C** (CR-003 revision 4 Q4 and bench item 4), and the section 4.1 figures move. Fix: run the burst for duty x window x (13.5 / 13), so that the key-down time equals the cap, and do the same at the 35 % step. Then regenerate the blocks and the plots, and correct the "3.0 min of held key" title of `cl_cap_pattern.png` | Open | Pending | |
| finding-21 | reviewer (iteration 2) | Major | CK-ANA-F3, A5, E5, J2 | `a5_closure.py` `run_inhibit` uses `v["inh_hyst"]` at 5 C. `inh_hyst` is a SENSOR_PARAM, so it is not stacked, not swept and not in the band. Note sections 1, 2 (case 3), 4.2, 6 (REQ-SYS-118 row), 9 and 10 (Q-3) | The REQ-SYS-118 re-arm hysteresis is an input of the note: 5 C (3 to 10), class E, "value not yet set". The SW-SAFE unit (WP-PDR-35) sets it. At its 3 C end the junction rises. In the governing state at 72 C it is 108.91 C (+0.33 K); with the 0.45 K band that is 109.36 C, still PASS. With every input adverse at once at 72 C it is **110.27 C**, and that stack's own largest setpoint falls to about 71.6 to 71.7 C (71.5 C gives 109.79 C, 71.8 C gives 110.08 C). The note's proposal rule is "the whole degree at or below both" the governing-plus-band value and the every-input value. By that rule the proposal becomes **71 C**, and the claim that 72 C "also holds with every swept input adverse at once" does not hold over the hysteresis range. Fix, either: (a) stack the hysteresis at 3 C in the protection cases and re-derive the setpoint; or (b) keep 72 C, state a re-arm hysteresis of at least 5 C as a condition of the setpoint in the CR-018 REQ-SYS-118 row and in Q-3 to WP-PDR-35, and show the 3 C sensitivity | Open | Pending | |
| finding-22 | reviewer (iteration 2) | Minor | CK-ANA-A5, B6 | Note section 8 item 2 ("This step does not measure f, and no setpoint rule depends on f"); section 4.2 ("no bench result is needed for the setpoint to hold"); section 11 item 2 | The setpoint depends on f being at most 0.40, an unmeasured class E upper end. Reviewer runs in the governing state at 72 C: f = 0.5 gives 109.64 C with the band; f = 0.6 gives 110.34 C, over the limit. So the setpoint holds up to about f = 0.55. The bonding check (NTC at or above the sink bead) only detects a gross fault, near f = 1. State this dependence and its margin (about f = 0.55) in sections 4.2 and 8 item 2 and in limitation 2. No number changes | Open | Pending | |

### Values proposed (rule C10)

- **REQ-SYS-112, 30 % in 13 s key-downs at 45 C: supported.** C01 is 97.2 C with a +10.7 K band; finding-20 does not change it.
- **New duty-cap requirement, 30 % of any 10 min window: supported.** At a true 30.0 % key-down every box criterion stays PASS; at 35 % the PETG face is OPEN.
- **REQ-SYS-118, 72 C +/-3 C at the flange NTC: not supported as stated.** Per finding-21 it becomes 71 C by the note's own rule, or stays 72 C with a stated hysteresis of at least 5 C.
- **REQ-SYS-181, 92 C +/-3 C and 100 ms on the sink (change from 95 C): supported.** C16 to C18 PASS, the C20 FAIL is reproduced, and 93 C fails.
- **PETG heat-deflection thresholds 60.3 / 64.4 C: not supported.** Per finding-20 they become 60.6 / 64.7 C.
- **Not in the delta:** REQ-SYS-113 48 C, the bench sink acceptance 8.80 / 7.27 K/W, and the D-6 alternative S. Their re-run values are identical.

### What is right and stays

- The governing-state method is sound and correctly implemented: stack the inputs that no bench step sees, then add the RSS of the rest.
- The finding-1 result holds up. At 95 C +/-3 C the case fails Tcase(OP), so 92 C is proposed. The result does not move with the comparator hysteresis, the time step or the run length, and the numbers of the iteration 1 review are reproduced exactly.
- The duration statement for the double fault is correct against REQ-SYS-180 and REQ-SYS-131.
- The usability cost at 45 C (13.7 to 17.5 % key-down) is stated for the owner.
- The re-run is byte-identical on every CSV.
- Both fixes for iteration 3 are small and need no new method: a burst-length correction, and either stacking the hysteresis or making it a stated condition.

### Verdict (reviewer, iteration 2)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/thermal-budget.md@4ff68737, hardware/sim/thermal/a5_closure.py@0e23d4d2 (run 2026-09-29-a5-closure-r2) at 6eb014c
FINDINGS:
- [Major] finding-1, finding-2, finding-3 (iteration 1): Verified.
- [Major] finding-20 CK-ANA-F3/E5: the "worst pattern the 30 % cap allows" holds 29.15 % key-down, not 30 %; at 30.0 % PETG is 55.56 C and the proposed HDT thresholds become 60.6 / 64.7 C (verdicts and the cap are unchanged).
- [Major] finding-21 CK-ANA-F3/E5/J2: the inhibit re-arm hysteresis (3 to 10 C, E) is held at 5 C; at 3 C the every-input stack reaches 110.27 C at 72 C, so the note's own rule gives 71 C unless a hysteresis of at least 5 C is made a condition.
- [Minor] finding-22 CK-ANA-A5: the setpoint depends on f <= 0.40 (it holds to about 0.55); the wording "no setpoint rule depends on f" is wrong.
ITEMS N/A: CK-ANA-B2, E6, G1-2 to G1-4 (deck not in the delta), G2, G4, G5, G6
VALUES PROPOSED: REQ-SYS-112 30 % (supported); duty cap 30 % / 10 min (supported); REQ-SYS-118 72 C +/-3 C (not supported as stated); REQ-SYS-181 92 C +/-3 C (supported); HDT 60.3 / 64.4 C (not supported)
MEASUREMENTS: size=25 criteria; inputs_checked=12; renders=8; turns=45; minutes=75; major=2 new (3 verified); minor=1
```

## Iteration 3 (delta on the fixes of finding-20 and finding-21, rule C1)

**Scope.** Rule C1: this iteration verifies the fixes of the two Major findings of iteration 2 (finding-20, finding-21) and nothing else. The product is note revision 2 with run `2026-09-29-a5-closure-r3`, at `d8dfb26`.
- `git show --stat d8dfb26` touches only the note, `a5_closure.py` and the new run folder `results/2026-09-29-a5-closure-r3/`. Runs r1 and r2, the TS-012 runs and `hardware/sim/thermal/README.md` have no diff from `6eb014c` to `d8dfb26`.
- The runner diff is 67 lines: the new `INH_PROT` (the eight device, interface and supply inputs plus `inh_hyst`) used in `inhibit_study`; the new `pattern_key`; `pattern_run` built on it; the running RF-on count `kon` in `closed_loop`; plot titles; and the default run id.
- The note diff changes the values that follow from the two fixes, adds section 16 and a change-log row, and does nothing else. A word diff against `6eb014c` shows no change in C01 to C12, the backstop (C16 to C21), the D-6 alternative or the bench acceptance. The r3 files `backstop.csv`, `backstop_screen.csv`, `bands.csv`, `bench_acceptance.csv`, `duty_sweep.csv`, `inputs.csv`, `cl_tornado.png`, `cl_ltspice_crosscheck.png`, `cl_bench_acceptance.png` and `ltspice/thermal_a5cl.net` have the same blobs as in r2.

### Readiness (R1 to R6)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes | Every `product_files` blob is `git rev-parse d8dfb26:<path>`, and the note and runner blobs equal HEAD. `d8dfb26` is a new commit on main, not an amend (parent `249356b`). The frozen model files have SHA-256 `54b5ecf4...3e66e0` and `09cf75ef...b97ce0` in the repository and in `scripts/`, and no commit since `35fc7ee`. `scripts/a5_closure.py` equals the committed runner (SHA-256 `c86050d6...33d2cb3f`, as `results.md` records) |
| R2 | Yes | From a `git archive d8dfb26` export: `CWHT_LTSPICE_LOCK_WAIT=14400 .venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id 2026-09-29-a5-closure-r3`. Result below (CK-ANA-C4) |
| R3 | N/A | No JSON file under a schema in the product |
| R4 | Yes | The author's summary and note section 16 state both fixes, the new values, the run and the checker result |
| R5 | Yes | No `TBD` in the note. The TBRs relied on (REQ-SYS-112, 113, 118, 181) are named, and each plan is quoted in section 9 |
| R6 | Yes | The 8 cited PNGs are in `results/2026-09-29-a5-closure-r3/` |

### Re-run from an export of the freeze commit (CK-ANA-C4)

- **Export and command.** Export: `git archive d8dfb26 | tar -x` into the reviewer scratchpad (`rv28a-it3/exp`). Command, from the export root: `CWHT_LTSPICE_LOCK_WAIT=14400 .venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id 2026-09-29-a5-closure-r3`. Result: **exit 0**, "CHECK PASS: the record's verdict set and proposed values equal the computed ones; LTspice within 0.5 K". Run time 4232 s. About 35 min of that was the LTspice step waiting for the shared lock, which another block's run held; the waiting is the wrapper's lock rule, not a fault.
- **Generated blocks.** Both blocks of the note (sections 5 and 6) equal the blocks of the committed `results.md`, character for character (checked separately with a Python extract), and the checker found no difference.
- **CSV outputs.** All 13 are **byte-identical** to the committed run r3: backstop, backstop_screen, bands, bench_acceptance, cap_pattern, cap_pattern_verdicts, duty_sweep, inhibit, inputs, protection_screen, summary, tornado, verdict_set. `results.md` differs only in the run-time line (4232 s against 2096 s).
- **Plots.** All 8 PNGs are byte-identical to the committed ones.
- **LTspice.** The regenerated netlist `thermal_a5cl.net` is byte-identical (blob `76d8a08f`, the same as r2). The `.log` first line reads "LTspice 26.0.2 for MacOS". The largest difference is **0.012 K** against the 0.5 K criterion, PASS. The `.raw` differs only in its header (the temporary directory name and the run date); it is 934,182 bytes, under the CR-017 C2 limit of 5,000,000 bytes.
- **Stage messages.** They equal `check-stdout.txt` except the elapsed times: inhibit proposal 71.0 C, REQ-SYS-181 proposal 92 C.

### Independent checks (CK-ANA-B4, B5, F3)

All checks call the unchanged functions of `a5_closure.py` at `d8dfb26` (`pattern_key`, `closed_loop`, `vals`, `build`, `reading_cf`) from reviewer scripts in the scratchpad. They are not committed.

| Check | Result | Reading |
|---|---|---|
| `pattern_key(600, 0.30)`, counted independently on the 0.2 s steps | 900 on-steps = **180.0 s** of key-down. The burst ends at **186.4 s**. It has 14 key-downs, the longest 13.0 s (REQ-SYS-055: at most 13 s). The re-key gaps are 0.4 or 0.6 s, alternating, because 13.5 s is 67.5 steps (mean 0.5 s) | finding-20 fixed as stated |
| The pattern repeats every 600 s. Every rolling 600 s window (3000 offsets) was counted | minimum and maximum both **180.0 s**. At 35 %, every window holds 210.0 s and the burst lasts 218.0 s | The pattern meets the rolling-window cap of the proposed requirement exactly, not only in fixed windows |
| Step indexing: `closed_loop` samples `demand(t - dt/2)` for step k; `demand` reads `key[floor(((t - dt/2) mod W) / dt)]`, which is index k-1; `pattern_key` built index i at the midpoint (i + 0.5) dt | same instant | The key the solver applies is the key that was counted |
| The iteration 2 recipe, duty x window x 13.5/13 = 186.9 s of held key | 180.4 s of key-down (both by step count and by 13 x 13 s + 11.4 s) | The author's statement in section 16 is correct: that recipe holds 0.4 s more than the cap allows. The author's fix is the exact one |
| Key-down fraction after the first hour | 18 whole windows in the last 3 h, each 180.0 s: 30.00 %, equal to `results.md` (35.00 % at the step) | `kon` is counted on every step, as stated |
| Box values under the pattern (`cap_pattern_verdicts.csv`) against iteration 2's own 29.99 % run | cells 51.4163 (iteration 2: 51.43), main-bay air 51.4576 (51.46), PETG face 55.5286 (55.56), PA-bay air 58.2017 (58.21) C | Within 0.03 K, as the author says. The small offset is the 0.4 / 0.6 s gap phasing |
| HDT thresholds, by hand from `cap_pattern_verdicts.csv` | 55.5286 + 5 = 60.53, rounded up to **60.6 C**; 55.5286 + 4.0722 + 5 = 64.60, rounded up to **64.7 C**. At 35 %: 61.83 → 61.9, 65.85 → 65.9 C | agrees with sections 6, 7 and 8 item 4 |
| Cap rule at 35 % | PETG 56.8291 + 4.0227 = 60.85 C against 60 C: OPEN by 0.85 K. Cells 52.1480 + 2.8644 = 55.012 C: OPEN by 0.012 K | The 35 % exclusion rests on the PETG face. The cells OPEN is correct under the rule but marginal. The note's wording ("both OPEN") is accurate, so no finding |
| **Inhibit re-arm hysteresis swept over its whole range**, governing state at 71 C, key held 60 min, dt 0.1 s | Junction 107.946 C at 3 C, **107.951 C at 3.5 C** (the maximum), 107.619 at 5 C, 106.385 at 10 C. Case maximum 82.411 C at 3 C, falling to 80.743 C at 10 C. 2 C (outside the range) gives 107.666 C | The effect is not strictly monotonic: 3.25 to 3.5 C sit up to 0.005 K above the 3 C end. With the +0.59 K band the governing value is at most 108.54 C, 1.46 K inside 110 C. So "holds for any re-arm hysteresis of 3 C or more" is true. Observation only: the screen takes ends, as limitation 7 says |
| Same sweep on the every-input stack at 71 C (the reviewer rebuilt it: the governing stack plus the adverse end of every band input whose screen rise is above 1e-3 K, 25 overrides) | 109.256 C at 3 C (the note: 109.26 C), 109.168 at 3.5 C, 108.663 at 5 C, 107.171 at 10 C | Monotonic. 3 C is the adverse end. The note's 109.3 C is reproduced |
| Every-input stack, setpoint bracket | 71.7 C: 109.932 C (holds); 71.8 C: 110.029 C (fails) | The note's 71.7 C is reproduced, as are the iteration 2 estimate (71.6 to 71.7 C) and the proposal of 71 C |
| Governing state at 71 C, time step halved to 0.05 s | 107.927 C against 107.946 C at 0.1 s | The numerical setting is adequate |
| Governing state at 71 C, flange-NTC fraction f above its 0.40 end (the finding-22 check, repeated at the new setpoint) | f = 0.5: 108.56 C (109.15 C with the band); f = 0.6: 109.25 C (109.84 C); f = 0.65: 109.59 C (110.18 C) | At 71 C the setpoint holds up to about f = 0.62. The finding-22 dependence remains, with a little more room than at 72 C (about 0.55) |

### Inputs checked against their sources (CK-ANA-A3, A4: the inputs the delta uses at new ends)

| Input | Note value | Source checked | Agreement |
|---|---|---|---|
| REQ-SYS-118 re-arm hysteresis `inh_hyst` | 5 C (3 to 10), E, not set; stacked at 3 C | `thermal_model.py` line 186: `Param(5.0, 3.0, 10.0, "C", "E", "REQ-SYS-118 recovery hysteresis (value not yet set)")`; `inputs.csv` row 113; `protection_screen.csv` row `inhibit,stacked,inh_hyst`, adverse end 3.0, rise 0.0959 K (junction plus case) | agrees |
| REQ-SYS-118 statement | no hysteresis term today; the note asks CR-018 (Q-1) and WP-PDR-35 (Q-3) to carry "at least 3 C" | `requirements.json` REQ-SYS-118: "cease RF output within 100 ms (TBR) after its PA temperature sensor reads above 85 C +/-3 C (TBR)" | The note does not edit the requirement. The new condition is routed as a request (CK-ANA-A6) |
| REQ-SYS-055 key-down length used by the pattern | 13 s key-downs re-keyed after 0.5 s | REQ-SYS-055: "7.5 s to 13 s (TBR) into any continuous key-down" | The pattern's longest key-down is 13.0 s on the step grid |
| Duty-cap definition (L-1) | 3.0 min of key-down time in any 10 min window | Note section 2 and the proposed requirement text of section 9 | Met exactly by the new pattern (rolling-window check above) |
| Governing stack of the inhibit | `a5_rjc2` 2.64, `a5_rjc1` 4.95, `a5_p1` 1.2, `a5_bond` 7.5e-05, `k_tim` 0.6, `r_spread_x` 0.3, `r_feed` 0, `inh_hyst` 3 | `results.md`; `protection_screen.csv` (9 stacked rows; `a5_idd` screened with 0 rise because its nominal is already its adverse end, so not stacked; iteration 2 recorded this) | agrees |

### Numbers in the note against the run (CK-ANA-D2, delta)

Cross-checked against `results.md`, `inhibit.csv` and `cap_pattern_verdicts.csv`. All agree, rounded up toward the limit:
- inhibit table: 93.01 → 93.1, 72.82 → 72.9, 68.30 → 68.3; 95.96 → 96.0, 75.77 → 75.8, 71.21 → 71.3; 97.43 → 97.5, 77.24 → 77.3, 72.61 → 72.7; 107.95 + 0.59 → 108.0 +0.6, 82.41 + 0.58 → 82.5 +0.6, 71.22 + 0.72 → 71.3 +0.8; 109.26 → 109.3, 83.64 → 83.7, 72.19 → 72.2;
- junction minus case 107.95 - 82.41 = 25.5 K; first trip 143.3 s = 2.4 min; LM2940 at most 73.77 → 73.8 C; PA-bay air under the inhibit at most 55.78 → 55.8 C (61.12 → 61.2 C with every input adverse at once); inhibit upper edge 71 + 3 = 74 C;
- pattern lifts over steady at the cap: PA-bay air 2.54, PETG face 1.59, main-bay air 1.01, cells 0.18 K (note: 2.5, 1.6, 1.0, 0.2 K); junction 107.39 → 107.4 C and case 87.18 → 87.2 C; at 35 %: 110.81 → 110.9 C and 90.59 → 90.6 C;
- usability 15.97 → 16.0 % and 13.33 → 13.3 %.

Two statements were not updated: section 7 item (1) and request Q-2 still give the cells as 51.3 C "under the worst cap pattern" (now 51.5 C). This is finding-23, Minor: the verdicts are unchanged.

### Checklist answers (delta scope)

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Sections 9, 10 and 16 name REQ-SYS-055, 112, 118 and 181, HZ-003, WP-PDR-35 and CR-018. Every id exists |
| CK-ANA-A2 | Yes | AT RISK row unchanged: CR-003 revision 4 and CR-018 are not dispositioned |
| CK-ANA-A3, A4 | Yes | Table above |
| CK-ANA-A5 | Yes | Both iteration 2 gaps are now bounded. (a) The pattern holds exactly the key-down time the cap allows, in every rolling window. (b) The hysteresis is taken at its adverse end, and the lower bound of 3 C is stated as a condition on WP-PDR-35 (Q-3), CR-018 (Q-1), D-6 and section 9. The f dependence stays as finding-22 (Minor, not in this delta) |
| CK-ANA-A6 | Yes | The new condition (hysteresis at least 3 C) goes to its writers as requests Q-1 and Q-3. No requirement file is edited |
| CK-ANA-B4 | Yes | dt halving at 71 C moves C13 by -0.02 K |
| CK-ANA-B5 | Yes | Independent step count of the pattern key and of the rolling windows; hand check of the HDT thresholds; the hysteresis sweep; the every-input setpoint bracket (table above) |
| CK-ANA-B6 | Yes | C13 to C15 keep their band (+0.59 / +0.58 / +0.72 K), now screened in the governing state with the hysteresis stacked. C22 to C25 keep the steady band |
| CK-ANA-C1 to C5 | Yes | Re-run result above. Developer evidence stated. LTspice through the wrapper |
| CK-ANA-D2 | Yes, one Minor | Cross-check above. finding-23 (two stale cell values in section 7 item (1) and Q-2) |
| CK-ANA-D3 | Yes | Values rounded up toward the limit. The setpoint is floored (71.7 → 71) |
| CK-ANA-E2, E3 | Yes | C13 margin 2.05 K, 1.46 K after its band; C14 7.59 K, 7.01 K after its band; C24 4.47 K, 0.40 K after its band. All above zero |
| CK-ANA-E4 | Yes | `--check` compares both generated blocks, which carry the new C13 to C15 and C22 to C25 values and verdicts, and exits 1 on any difference |
| CK-ANA-E5 | Yes | Section 9 and the section 6 block give REQ-SYS-118 as 71 C +/-3 C with the hysteresis condition, its basis (C13, C14, the every-input stack) and the plan step (the ADR and the TBR close in the same CR). The HDT thresholds are 60.6 / 64.7 C with their basis (C24). The duty cap is 30 %, and the cap rule is shown at 30 % and 35 % |
| CK-ANA-E7 | Yes | No credit is claimed |
| CK-ANA-F1, F2 | Yes | Unchanged cases: key held at 45 C for the inhibit; worst allowed pattern for the box |
| CK-ANA-F3 | Yes | The worst case of both delta items is now taken. The pattern holds exactly the cap. The hysteresis sits at its adverse end in the governing state and in the every-input stack, confirmed over the whole range by the sweep |
| CK-ANA-F4 | Yes | `cl_protection_screen.png` now shows `inh_hyst` among the stacked inputs with its screen rise |
| CK-ANA-G3-1, G3-4 | Yes | Transient closed-loop runs for the inhibit and the pattern. The steady band is used only as the band of the pattern |
| CK-ANA-H1, H2 | Yes | Q-2 (HZ-003 K2 at 71 C +/-3 C) and Q-6 are updated. HZ-007 in Q-2 carries the stale 51.3 C (finding-23) |
| CK-ANA-H3 | Yes, one Minor | Change-log row 2 and section 16 name revision 2 and its reason. The change-log rows are in the order 0, 2, 1 (part of finding-23) |
| CK-ANA-I1 | Yes | 8 of 8 cited renders opened with the Read tool at `d8dfb26` |
| CK-ANA-I2 | Yes | `cl_cap_pattern.png`: the top title now reads "3.0 min of key-down time (one 186.4 s burst of held key)", and the middle title reads "key-down fraction after 1 h 30.00 %, the cap". The bottom panel shows PETG 55.5 C +4.1 K = 59.6 C PASS at 30 % and 56.8 C +4.0 K = 60.9 C OPEN at 35 %. `cl_inhibit_backstop.png`: legend 107.9 C +0.6 K band, own largest setpoint 72.5 C, every input 109.3 C and 71.7 C, trip at the +3 C edge 74.0 C, first trip at 2.4 min. `cl_protection_screen.png`: "STACKED inh_hyst [E] -> 3", title at 71.0 C. The legends round to the nearest 0.1 while the blocks round up, as iteration 1 recorded |
| CK-ANA-J1 | Yes | Unchanged: LTspice accredited; the Python stack marked developer evidence |
| CK-ANA-J2 | Yes | swe-134 7.1 tasks 1 and 6. The REQ-SYS-118 threshold, the HZ-003 K2 control, now holds its limit for every re-arm hysteresis the SW-SAFE unit may set (3 C or more), and the note tells WP-PDR-35 that a lower value needs a re-run. REQ-SYS-181 still acts above REQ-SYS-118: the inhibit's upper edge is 74 C at the flange, and the sink peaks at 71.3 C +0.8 K against the 89 C lower edge (C15) |
| CK-ANA-J3 | Yes | The tasks are listed in the front matter |

ITEMS N/A:
- CK-ANA-B2: no vendor model.
- CK-ANA-E6: no TPM.
- CK-ANA-G1-2 to G1-4: the deck is unchanged (same blob as r2).
- G2, G4, G5, G6: not this analysis kind.

### Per-case results (delta cases, A5-CL, 45 C; margin = limit - result)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C13 | Inhibit at 71 C +/-3 C (trip at 74 C), key held 60 min, governing state with the re-arm hysteresis at 3 C | REQ-SYS-112: 110 C junction | 107.95 C | +2.05 K (+1.46 K after the band) | +0.59 K band | Re-run: see above. Hysteresis 3 to 10 C: at most 107.951 C; dt 0.05 s: 107.927 C | none |
| C14 | same | Case guidance 90 C (p.8) | 82.41 C | +7.59 K (+7.01 K after the band) | +0.58 K | Hysteresis sweep: at most 82.411 C | none |
| C15 | same | Sink against the proposed REQ-SYS-181 lower edge, 89 C | 71.22 C | +17.78 K | +0.72 K | Re-run | none |
| Every-input stack | 71 C, every swept input adverse at once, hysteresis 3 C (information) | 110 C junction | 109.26 C | +0.74 K (value only, as the note states) | not banded, by the note's rule | Reviewer rebuild: 109.256 C; 71.7 C holds (109.932 C), 71.8 C fails (110.029 C) | none |
| C22 | Worst 30 % cap pattern, exactly 180.0 s of key-down in every window, inhibit not counted, last hour of 4 h | Cells 55 C | 51.42 C | +3.58 K (+1.05 K after the band) | +2.54 K | Independent pattern count: 180.0 s in every rolling window | finding-23 (wording only) |
| C23 | same | Main-bay air 55 C | 51.46 C | +3.54 K (+1.08 K after the band) | +2.46 K | Re-run | none |
| C24 | same | PETG 60 C (TS-012 7.3 (c)) | 55.53 C | +4.47 K (+0.40 K after the band) | +4.07 K | HDT thresholds by hand: 60.6 / 64.7 C | none |
| C25 | same | Relay ambient 65 C | 58.20 C | +6.80 K (+2.15 K after the band) | +4.65 K | Re-run | none |
| Cap step | 35 %, exactly 210.0 s in every window, inhibit not counted | PETG 60 C; cells 55 C | PETG 56.83 C; cells 52.15 C | PETG +3.17 K, -0.85 K after the band; cells +2.85 K, -0.01 K after the band: neither shown to pass, so 35 % is excluded | +4.02 K; +2.86 K | Re-run | none |
| Usability | 30 % pattern with the inhibit at 71 C, sensor nominal and at its -3 C edge, hysteresis 5 C | information | 15.97 % and 13.33 % key-down | n/a | n/a | Re-run | none |

### Iteration 2 Major findings: disposition check

| Finding | What was asked (iteration 2) | What revision 2 does | Reviewer check | State |
|---|---|---|---|---|
| finding-20 | Make the "worst pattern the cap allows" hold the key-down time the cap allows (3.0 min in 10 min), not 3.0 min of elapsed time; redo the 35 % step; regenerate the blocks, the HDT thresholds and the plots; correct the `cl_cap_pattern.png` title | `pattern_key` holds exactly duty x window of RF-on time, counted on the solver's 0.2 s steps: 180.0 s, burst 186.4 s; 210.0 s at 35 %. The key-down fraction is counted on every step (`kon`): 30.00 % and 35.00 %. C22 to C25 at 51.5, 51.5, 55.6 and 58.3 C, all PASS. At 35 %, PETG and cells OPEN, so the cap stays 30 %. HDT thresholds 60.6 / 64.7 C. Plot titles corrected | The step count and the rolling-window count confirm 180.0 s in every 600 s window, with key-downs of at most 13.0 s. The step the key is counted on is the step the solver applies it on. The iteration 2 reviewer run is matched within 0.03 K. The HDT arithmetic checks. The author's reason for not using the 13.5/13 recipe is correct (180.4 s) | **Verified** |
| finding-21 | Either (a) stack the re-arm hysteresis at 3 C in the protection cases and re-derive the setpoint, or (b) keep 72 C and state a hysteresis of at least 5 C as a condition | Option (a): `INH_PROT` adds `inh_hyst` to the screened and stacked set; its adverse end is 3 C. Governing plus band holds to 72.5 C; the every-input stack needs 71.7 C; the proposal is **71 C +/-3 C** (C13 108.0 +0.6 C, C14 82.5 +0.6 C, C15 71.3 +0.8 C, PASS). A hysteresis of at least 3 C is written into the requests to CR-018 (Q-1) and WP-PDR-35 (Q-3), D-6 and section 9. Usability at 45 C: 13.3 to 16.0 % | The code applies the stacked hysteresis to every inhibit run (`run_inhibit` reads `v["inh_hyst"]` from the override set). A sweep over 3 to 10 C confirms the claim "any hysteresis of 3 C or more" in both the governing state and the every-input stack (largest governing value 107.951 C, 1.46 K inside the limit with the band). 71.7 C and 109.26 C are reproduced | **Verified** |

### Findings

Current state of every finding of this record. finding-12 to finding-19 were never issued: iteration 2 numbered its findings from 20 without the iteration 1 text.

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer (iteration 1) | Major | CK-ANA-F3, E3 | Note section 4.2 (revision 0) | REQ-SYS-181 backstop-alone adverse case incomplete and unbanded; duration not quantified. Fixed in revision 1 (C16 to C21; 92 C +/-3 C proposed; duration stated). Verified in iteration 2; revision 2 does not change it | Verified | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer (iteration 1) | Major | CK-ANA-E3, E5, J2 | Note sections 4.2 and 8 (revision 0) | REQ-SYS-118 setpoint on the sensor-adverse case alone, 0.07 K margin, no band. Fixed in revision 1 (governing state with band). Verified in iteration 2; its residual finding-21 is now also Verified | Verified | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer (iteration 1) | Major | CK-ANA-F3, D2 | Note sections 4.1 and 6 (revision 0) | Worst cap pattern run with the inhibit cutting it. Fixed in revision 1 (inhibit not counted; cap 30 %). Verified in iteration 2; its residual finding-20 is now also Verified | Verified | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer (iteration 1) | Minor | CK-ANA-A3, A4 | Note section 3 row "LM2940 operating junction" | The LM2940CT-5.0 is the LM2940C grade (SNVS769J p.4: 0 to 125 C), not the -40 to 125 C LM2940-N row. The 125 C limit is the same; no number changes. Not addressed (Minor, rule C1) | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer (iteration 1) | Minor | CK-ANA-A4, B6 | Note section 3 rows "LM2940 RthJC(bot)" and "LM2940 tab to sink" | SNVS769J p.19 (10.3.1) suggests RθJC 3 C/W and RθCS 0.5 to 2.5 C/W for heatsinking; the note uses 1.1 C/W and 0.4 to 1.0 K/W. About +2.8 K on the LM2940 junction only; no verdict changes (C18, C21 margins above 25 K). Not addressed | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer (iteration 1) | Minor | CK-ANA-D2 | Note sections 2 (L-2 row) and 4.1 ("0.8 W") | The model moves 0.726 W, not 0.8 W. Not addressed | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer (iteration 1) | Minor | CK-ANA-C3, D2 | Note section 2 (revision 0 "At 40 % ... author exploration") | Banded 40 % results were not produced by the runner. Revision 1 replaced the 40 % basis with the 35 % step run by the runner (C22 to C25 and the step rows of `cap_pattern_verdicts.csv`), so the text cited is gone; the lead SE may mark it Verified on re-reading section 2 | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer (iteration 1) | Minor | CK-ANA-A6 | Note section 10 D-19, Q-5 | No local temperature bound or rating request for the LM2940 output capacitor next to the sink web. Not addressed | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer (iteration 1) | Minor | CK-ANA-E3 | Note sections 6 and 8 item 1 (now 8.80 and 7.27 K/W) | The bench acceptance values have no guard band for the bench's own measurement uncertainty. Not addressed | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer (iteration 1) | Minor | CK-ANA-B4 | Note sections 2 and 13 | The numerical settings of the closed-loop and periodic cases are not stated in the note. The reviewers' dt halvings (iterations 1 to 3) show no result moves. Not addressed | Open | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer (iteration 1) | Minor | CK-ANA-A6 | Note sections 1 ("Not in scope") and 10 | The WP-PDR-28 outputs "firmware thermal fold-back requirement (G-14)" and "A11 stop criterion input" are neither answered nor assigned to 28b. Not addressed | Open | Pending | |
| <a id="finding-20"></a>finding-20 | reviewer (iteration 2) | Major | CK-ANA-F3, A5, E5 | `a5_closure.py` `pattern_key`, `pattern_run`, `closed_loop` (`kon`); note sections 2, 4.1, 5 (C22 to C25), 6, 7, 8 item 4, 16 | Worst cap pattern held 29.15 %, not 30 %. Fixed in revision 2: exactly 180.0 s of key-down in every 10 min window (checked in every rolling window), 30.00 %; HDT thresholds 60.6 / 64.7 C; titles corrected (disposition table above) | Verified | Pending | |
| <a id="finding-21"></a>finding-21 | reviewer (iteration 2) | Major | CK-ANA-F3, A5, E5, J2 | `a5_closure.py` `INH_PROT`, `inhibit_study`; note sections 1 to 4.2, 5 (C13 to C15), 6, 7, 8 item 2, 9, 10, 11 item 7, 16 | Inhibit re-arm hysteresis held at 5 C. Fixed in revision 2: stacked at 3 C, proposal 71 C +/-3 C, lower bound of 3 C stated for WP-PDR-35 and CR-018; confirmed over 3 to 10 C by the reviewer sweep (disposition table above) | Verified | Pending | |
| <a id="finding-22"></a>finding-22 | reviewer (iteration 2) | Minor | CK-ANA-A5, B6 | Note section 8 item 2 ("This step does not measure f, and no setpoint rule depends on f"); section 4.2; section 11 item 2 | The setpoint depends on f being at most 0.40, an unmeasured class E upper end. At the revision 2 setpoint of 71 C (governing state with band): f = 0.5 gives 109.15 C, f = 0.6 gives 109.84 C, f = 0.65 gives 110.18 C, so it holds to about f = 0.62 (at 72 C it was about 0.55). State the dependence and its margin. No number changes. Not addressed (Minor, rule C1) | Open | Pending | |
| <a id="finding-23"></a>finding-23 | reviewer (iteration 3) | Minor | CK-ANA-D2, H3 | Note section 7 item (1) ("51.3 C, band +2.6 K, PASS at the 30 % cap, steady and under the worst cap pattern"); section 10 Q-2 ("HZ-007 C5 and K5: cells 51.3 C at the cap with L-2, also under the worst cap pattern"); change log | After the finding-20 fix, the cells under the worst cap pattern are 51.5 C (C22; 51.42 C), not 51.3 C, which is the steady value. Both sentences say 51.3 C also holds under the pattern. The verdict (PASS) and the HZ-007 routing are unchanged. Also, the change-log rows are in the order 0, 2, 1. Fix: give the steady and the pattern values separately (51.3 C steady, 51.5 C under the pattern) in section 7 item (1) and Q-2, and order the change log. Raised after the reviewer's first APPROVED verdict: a lien due at the CDR readiness declaration (rule C1) | Open | Pending | |

### Values proposed (rule C10)

- **REQ-SYS-112, 30 % in 13 s key-downs at 45 C: supported.** C01 is 97.2 C with a +10.7 K band (unchanged). The junction is also bounded by the inhibit (C13).
- **New duty-cap requirement, at most 30 % key-down time in any rolling 10 min window at the 5 W step: supported.** The worst pattern now holds exactly the cap, in every rolling window. Every box criterion is PASS with its band. At 35 % the PETG face (and the cells, by 0.01 K) are not shown to pass.
- **REQ-SYS-118, 71 C +/-3 C at the flange NTC, 100 ms, with a re-arm hysteresis of at least 3 C: supported.** C13 is 108.0 C +0.6 K and C14 82.5 C +0.6 K, both PASS. The every-input stack gives 109.3 C, inside 110 C. The value holds over the whole 3 to 10 C hysteresis range. It depends on f being at most about 0.6, which the bench does not measure (finding-22, Minor).
- **REQ-SYS-181, 92 C +/-3 C and 100 ms on the sink (a change from 95 C): supported.** Not in this delta; iteration 2 verified it, and revision 2 does not change it.
- **PETG heat-deflection temperature, at least 60.6 C (64.7 C with the band): supported.**
- **REQ-SYS-113 48 C, bench sink acceptance 8.80 / 7.27 K/W, D-6 alternative S 79.2 C:** not in the delta, unchanged (same blobs as r2). finding-9 (Minor) stays on the bench values.
- Usability at 45 C, 13.3 to 16.0 % key-down: information for the owner. It is correct as computed.

These values go to the owner at S1 in CR-018 only once the lead SE sets the record verdict to APPROVED (rule C10). The owner rules the values; this record does not.

### Record verdict and liens

- **Reviewer verdict: APPROVED.** finding-20 and finding-21 are Verified. No Major finding is open (rule C1, iteration 3 of 3: no escalation needed).
- **Liens (Minor, open):** finding-4 to finding-11 (iteration 1), finding-22 (iteration 2) and finding-23 (raised here). Under rule C1 they are liens due at the CDR readiness declaration, listed in package section 15. finding-7 looks resolved by revision 1; the lead SE may verify it on re-reading.
- **Record verdict held at NEEDS CHANGES by the lead SE.** This is the INSP-112 precedent: the applied analysis template is still only on `cr/CR-012-pdr-checklist-templates` (blob `0386cc6e`). The lead SE sets `verdict: APPROVED` once CR-012 merges and that blob is unchanged, or rules otherwise.

```
VERDICT: APPROVED
PRODUCT: docs/design/analysis/thermal-budget.md@5dfa85e0, hardware/sim/thermal/a5_closure.py@6d8b23cf (run 2026-09-29-a5-closure-r3) at d8dfb26
FINDINGS:
- [Major] finding-20 CK-ANA-F3/A5/E5: Verified. The pattern holds exactly 180.0 s of key-down in every rolling 10 min window; 30.00 %; HDT 60.6 / 64.7 C.
- [Major] finding-21 CK-ANA-F3/A5/E5/J2: Verified. Hysteresis stacked at 3 C; 71 C +/-3 C; holds for any hysteresis of 3 C or more (sweep 3 to 10 C).
- [Minor] finding-23 CK-ANA-D2/H3: section 7 item (1) and Q-2 give 51.3 C for the cells "also under the worst cap pattern" (now 51.5 C); change-log order 0, 2, 1. Lien.
- [Minor] finding-4 to finding-11, finding-22: open, not in the delta (rule C1). Liens.
ITEMS N/A: CK-ANA-B2, E6, G1-2 to G1-4 (deck unchanged), G2, G4, G5, G6
VALUES PROPOSED: REQ-SYS-112 30 % corner (supported); duty cap 30 % of any 10 min (supported); REQ-SYS-118 71 C +/-3 C with hysteresis >= 3 C (supported); REQ-SYS-181 92 C +/-3 C (supported, not in the delta); PETG HDT >= 60.6 / 64.7 C (supported); REQ-SYS-113 48 C, bench 8.80 / 7.27 K/W, S 79.2 C (not in the delta, unchanged)
MEASUREMENTS: size=10 delta cases (C13 to C15, every-input stack, C22 to C25, cap step, usability); inputs_checked=5; renders=8; turns=40; minutes=80; major=0 new (2 verified); minor=1 new
```
