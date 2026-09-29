---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-21 harmonic low-pass
# filter analysis for the TS-012 finalists A4 and A5, iteration 1 at freeze commit 6bff79c (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Approved 2026-09-28, merge held at the
# section 9 pre-merge check). tools/validate_docs.py requires the checklist field to name a template that exists
# on main, so the field names peer-review-checklist-design revision B and checklist_analysis records the template
# actually applied, as INSP-056, INSP-083 and INSP-114 did. The delta iteration after CR-012 merges switches the field.
# id: the brief assigned no id. INSP-115 is above every id on main at HEAD 9182ff2 (INSP-114 is the highest in use);
# the lead SE renumbers it if a parallel reviewer took the same id.
# Filed by the lead SE on 2026-09-28 from the reviewer's own text: the harness refused the reviewer's Write of this
# new file ("Subagents should return findings as text"). Content is verbatim; the parallel keying review that also
# chose INSP-115 is filed as INSP-116.
id: INSP-115
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-lpf-ts012.md
product: docs/design/analysis/lpf-ts012.md
# product_commit: 6bff79c, the WP-PDR-21 tx-lpf commit. Every blob below equals git rev-parse 6bff79c:<path> and
# HEAD:<path> at HEAD 9182ff2 (44 files, no drift).
product_commit: "6bff79c9d650fd4c8eeceb0cdd01d05578dd32a1"
product_files: ["docs/design/analysis/lpf-ts012.md@d59a99b512c8cba879c66ebf16ff5be28e8a132f", "hardware/sim/tx-lpf/README.md@956c548695a7f962674ccba19093f0ae478fede1", "hardware/sim/tx-lpf/lpf_model.py@e7c98d37905ed0e8de25ddd58c2537de3da8dced", "hardware/sim/tx-lpf/run_lpf.py@db36b9d86537cb194b877cab58806540ef4f6f44", "hardware/sim/tx-lpf/retune_screen.py@042e1657a51ecaaf2085d660577eec082ddb9718", "hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/il_nominal_passband.png@fca276a7a1a3e8f05eb4038bf7e06c62770c0868", "hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/lpf_r1.cir@3fee749cf2f3a65826f1f41edd5ba6a8a3bc359f", "hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/result.json@ae05c7c6eb84aa052e791499fa590e61fc754fc1", "hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/rl_nominal_passband.png@74a36e29fce9632a207067e021caca10a3884a72", "hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/s21_nominal_wide.png@a228cce52894ec664211ba504f537632696e9973", "hardware/sim/tx-lpf/results/2026-09-28-r2-mc-1812sms/il_mc_passband.png@03ea84601e9b4368cbc7a2325e9966e7d3473f0a", "hardware/sim/tx-lpf/results/2026-09-28-r2-mc-1812sms/lpf_r2.cir@655d514ebc4c980aa9bec2c152ec61f0522ebe2f", "hardware/sim/tx-lpf/results/2026-09-28-r2-mc-1812sms/mc_histograms.png@1addb57274b105ea3ecae06cac4d2df4f742f518", "hardware/sim/tx-lpf/results/2026-09-28-r2-mc-1812sms/mc_values.csv@c551e7b62e244e68ff224cb20030c241980db2f5", "hardware/sim/tx-lpf/results/2026-09-28-r2-mc-1812sms/result.json@ea33626f68b5d15253968449dc8f526c9e690965", "hardware/sim/tx-lpf/results/2026-09-28-r2-mc-1812sms/s21_mc_wide.png@09024a39aee02e742635be1afe0aee42a41cfecc", "hardware/sim/tx-lpf/results/2026-09-28-r3-mc-air-aswound/il_mc_passband.png@332b0cc9f3b4126759825768d9b2cef0339a7dd3", "hardware/sim/tx-lpf/results/2026-09-28-r3-mc-air-aswound/lpf_r3.cir@130912aae02d23915eee51f908dcb23003fae475", "hardware/sim/tx-lpf/results/2026-09-28-r3-mc-air-aswound/mc_histograms.png@03b174cf484d8f25416023d6de3b7b03440c193f", "hardware/sim/tx-lpf/results/2026-09-28-r3-mc-air-aswound/mc_values.csv@cac7db6d5e289cef4e070d551ad20c05dd29010f", "hardware/sim/tx-lpf/results/2026-09-28-r3-mc-air-aswound/result.json@be1cc70be7ab4b39eb9bb16614779c552f6358b6", "hardware/sim/tx-lpf/results/2026-09-28-r3-mc-air-aswound/s21_mc_wide.png@03dd06a168ca524571ac3c7779a5ca23b56ae960", "hardware/sim/tx-lpf/results/2026-09-28-r4-mc-air-aligned/il_mc_passband.png@2fe4def27a176972b1b560cb256d47bbe08582a6", "hardware/sim/tx-lpf/results/2026-09-28-r4-mc-air-aligned/lpf_r4.cir@03c3854c7bf426ae4d578d55d3aadb6f36e374de", "hardware/sim/tx-lpf/results/2026-09-28-r4-mc-air-aligned/mc_histograms.png@0853e1b665159df1c427d5978ecba54d0504d93c", "hardware/sim/tx-lpf/results/2026-09-28-r4-mc-air-aligned/mc_values.csv@631808125fddceebb17a54ab132359971617fe0b", "hardware/sim/tx-lpf/results/2026-09-28-r4-mc-air-aligned/result.json@0b41a0e4a24f06699e6239f344c84f4ac2957af7", "hardware/sim/tx-lpf/results/2026-09-28-r4-mc-air-aligned/s21_mc_wide.png@8cdd1bc00e2643f41c8420127284a78d278a96b2", "hardware/sim/tx-lpf/results/2026-09-28-r5-harmonic-budget/harmonic_budget.png@8e8ecdef3596c781d97c56d2d164542fa8bc6078", "hardware/sim/tx-lpf/results/2026-09-28-r5-harmonic-budget/result.json@2e4e56d013c0940fd7553b185ef59fb5bcee975b", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/il_mc_passband.png@3e9542f15fcd2dc9949a0bae24fcb4833583ea0c", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/lpf_r6.cir@03223c6806cae9830fd31049b09148e0519a5532", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/mc_histograms.png@e06fc5149c77f33b0d09b22bef0d7febe0f28246", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/mc_values.csv@c869b6d73016d83e5c383c58312626b5beee418a", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/result.json@fb09bcd176349f085bcc86346ba1c8bc366a4e54", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/retune_screen.json@e705bfa2d3ffe08101797adc287d6617ff108ebe", "hardware/sim/tx-lpf/results/2026-09-28-r6-mc-1812sms-retuned/s21_mc_wide.png@5afed8ab4ee568b8e7b9a8594baa8cc52549289a", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/il_mc_passband.png@63794fa7b8e8140150ae5f9b8262db6e63d8fece", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/lpf_r7.cir@5fea061414147f48f98b6154e7788ce001250ecf", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/mc_histograms.png@3094c1f4579f7d14e8fd04c1afeb75497f3f9125", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/mc_values.csv@a0f342f506aafed5be99d2bc55640c904d46bb33", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/result.json@3bebe014149cbac5b84d32f4dac4982f1172f8f5", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/retune_screen.json@8188fa77ae06333c9c95dc8a8c4a378047371753", "hardware/sim/tx-lpf/results/2026-09-28-r7-mc-air-aligned-retuned/s21_mc_wide.png@b98347062cc30e3071a1e66a178d26d5cfb1481e"]
analysis_kind: [simulation-deck, worst-case]
product_size: 1 note; 6 LTspice decks (1 nominal with 6 variants, 5 Monte Carlo of 252 steps); 1 checker; 1 value screen; 1 budget run; 19 renders; 28 input rows
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, matplotlib 3.11.2, spicelib 1.6.3 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/tx-lpf/*.py: developer evidence per 05 section 9.1, as the note says"]
# values_proposed: section 7 items 2 and 5 of the note. Support stated per value in the record body (section E5).
values_proposed: ["REQ-TX-009: 40 dB (keep; not supported for A4, finding-2; for A5 supported with 0.2 to 1.4 dB extreme-corner margin on the retuned values, finding-1)", "REQ-TX-010: 35 dB (keep; not supported for A4, finding-2; supported for A5)", "REQ-TX-011: 40 dB (keep; supported, Monte Carlo worst 65.8 dB on estimated layout leakage, limitation 4 of the note)", "WP-PDR-21 passband-loss criterion: 0.75 dB worst case (TBR) (not supported: extreme corners 0.81 to 0.90 dB for the proposed retuned 1812SMS build, finding-1)"]
renders_inspected: 19
sprint: PDR-prep
author_agent: "author:WP-PDR-21 tx-lpf (Claude as analysis author, TS-012 discriminating analyses; commit 6bff79c)"
reviewer_agent: "reviewer:WP-PDR-21-analysis-lpf-iter1 (independent; authored no part of the note, the decks, the checker, the value screen or TS-012)"
# criticality: a hardware-only transmit filter analysis; it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
# verdict (rule C1, iteration 1): three Major findings are open, so NEEDS CHANGES. Iteration 2 is a delta that verifies
# the Major fixes only; Minor findings raised after the first APPROVED verdict become liens due at the CDR
# readiness declaration.
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 6
findings_open: 9
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A1, CK-ANA-A5, CK-ANA-A6, CK-ANA-B1, CK-ANA-B3, CK-ANA-B6, CK-ANA-D2, CK-ANA-E3, CK-ANA-E4, CK-ANA-E5, CK-ANA-F1, CK-ANA-F3, CK-ANA-F4, CK-ANA-G7-1, CK-ANA-H1, CK-ANA-I2]
effort_turns: 55
effort_minutes: 80
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record: harmonic low-pass filter, TS-012 finalists A4 and A5 (INSP-115, iteration 1)

**Product:** `docs/design/analysis/lpf-ts012.md` (`d59a99b5`) with `hardware/sim/tx-lpf/` (README `956c5486`; model `lpf_model.py` `e7c98d37`; deck writer, runner and checker `run_lpf.py` `db36b9d8`; value screen `retune_screen.py` `042e1657`; decks, results, Monte Carlo value tables and 19 renders of runs r1 to r7) at freeze commit `6bff79c` (rule C2). Every blob equals `git rev-parse HEAD:<path>` at `HEAD` `9182ff2`. No product blob lives on a `cr/` branch. The per-run script snapshots in each results folder are byte-identical to the three scripts at the block root (checked with `cmp`).

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck and worst-case (Monte Carlo and tolerance corners): sections A to F, G1, G7, H and I apply. G2 to G6 are N/A (the harmonic budget of run r5 is a single-formula combination reviewed under E and F, not a line-item budget); J is N/A (criticality neither).

**Acceptance criteria (rule C7, every case the governing texts enumerate):**
- REQ-TX-009 (`docs/requirements/tx/requirements.md`): "attenuate every signal from 288 MHz to 296 MHz by at least 40 dB (TBR) between its PA output and antenna port". Rationale: "K1 sets 40 dB at the filter's own terminals so that the raw harmonic levels of the HZ-008 K2 PA meet the 60 dB target of REQ-TX-008". TBR plan: TS-003 supplies the raw 2f level "and the filter simulation confirms 40 dB".
- REQ-TX-010: 432 to 444 MHz, at least 35 dB (TBR), same basis. REQ-TX-011: 576 MHz to 1.5 GHz, at least 40 dB (TBR), "or a lower one with the REQ-TX-008 margin shown".
- REQ-TX-007 and REQ-SYS-017: every antenna-port spurious emission at most 25 uW "at every power step, 144.0012-147.9988 MHz and 6.4-8.4 V supply" (REQ-SYS-017: "at all power steps, carrier frequencies and 6.4 to 8.4 V pack voltages").
- REQ-TX-008 and REQ-SYS-018: every spurious emission at least 60 dB (TBR) below the mean carrier power at the 5 W step. REQ-SYS-018 rationale allocates "harmonic low-pass filter at least 40 dB at 288 MHz and 35 dB at 432 MHz with at most 0.5 dB insertion loss".
- REQ-SYS-011 (0.5, 1, 2 W within +/-1 dB) and REQ-SYS-012 (5 W within +/-1 dB), both "at 6.4-8.4 V pack".
- 47 CFR 97.307(e) (corpus `47cfr-97.307.md`, eCFR issue 2026-09-23): for 25 W or less, "must not exceed 25 uW and must be at least 40 dB below the mean power of the fundamental emission, but need not be reduced below the power of 10 uW". The note quotes it correctly.
- TS-012 revision 4 section 7.3 (commit `7d0d450`), WP-PDR-21 LPF check: "the LPF with Coilcraft 1812SMS SRF and Q models, 1206 pad and via parasitics; pass: at least 40 dB at 288 to 296 MHz, 35 dB at 432 to 444 MHz, passband loss at most 0.5 dB."
- TPM-007 (`docs/plan/tpm.json`, key spurious-margin): margin = achieved dBc minus 53 at the 5 W step, 2f to 10f, 144.05, 146.00 and 147.95 MHz.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (harmonic filter analysis; REQ-TX-009 attenuation requirement; analysis checklist template and rule C1) preceded every `grep`; `grep` only pinned lines in the requirements, TS-012, the research report and the INSP register. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).** Coilcraft Document 184-1 and 184-2, revised 12/02/21 (https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf, read through WebFetch, both pages rendered and read); `docs/research/pa-device-candidates.md` F4, F8, F16, F17; 47 CFR 97.307 corpus; TS-012 sections 7.1, 7.3 and 8.3 rows 4, 5 and E1; REQ-TX-007 to 012, REQ-SYS-011, 012, 017, 018; TPM-007; HZ-008.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-G7-1, F3, F4, B6, E3, E5 | Note sections 2 item 1, 4.2, 4.3, 5, 7 items 2, 4 and 5; `run_lpf.py` `write_mc_deck`; `lpf_model.py` `sample_filter`, `K_1812`, `K_AIR` | The "worst" of every build is the largest of 252 samples in which every parameter of every part is drawn independently, and the two "corners" move only L and C with nominal parasitics. Board thickness and via count are one board-level choice that sets every Lvia and Cpad together (the note's own ranges are "one via, 1.6 mm" to "two vias, 0.8 mm"), ESR, ESL and tolerance come from one reel, and the coupling K is sampled positive only although its sign follows winding sense and orientation. The note calls the sample maximum "worst case" and proposes a "0.75 dB worst case" criterion on it. Reviewer extreme-value corners inside the note's own ranges (LTspice through the wrapper, 48 corners; section "Reviewer re-run and independent checks"): retuned 1812SMS passband loss 0.81 to 0.90 dB (note 0.71), 2f 41.4 dB (note 44.8); retuned aligned air coils 0.74 to 0.86 dB (note 0.65), 2f 40.2 dB (note 43.8); BOM 1812SMS 1.94 dB (note 1.21), 2f 48.9 dB (note 54.4). Consequences: the proposed 0.75 dB criterion is not met by the build the note recommends; REQ-TX-009 margin of the retuned builds is 0.2 to 1.4 dB, not 3.8 to 4.8 dB; A4 97.307(e) margin with the retuned values is 1.2 to 2.4 dB, not 4.8 to 5.8 dB; the A5 REQ-SYS-012 margin at 6.4 V with the retuned 1812SMS build becomes -0.49 to +0.11 dB, not -0.30 to +0.30 dB; the layout rule "two ground vias per shunt capacitor" (section 7 item 4) is the corner of lowest 2f attenuation, which the note does not say. **Fix:** add an extreme-value (or board-correlated) corner analysis with the board choice as one factor and K of both signs, report worst case from it, restate every margin, the proposed criterion and the REQ-TX-009 support on it, and state the Lvia trade of the two-via rule | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-E5, A6 | Note section 7 item 5; section 4.3 first paragraph | Item 5 says the analysis "supports keeping 40 dB, 35 dB and 40 dB as the filter allocations", without condition. REQ-TX-009 and 010 are allocated so that the PA's raw harmonics "meet the 60 dB target of REQ-TX-008". Section 4.3 of the same note says A4 needs 45 dB at 2f and 40 dB at 3f for the 60 dBc target under its -15 and -20 dBc assumption. A filter that meets 40 and 35 dB exactly leaves A4 at 55 dBc at 2f and 3f, 5 dB short of REQ-TX-008 and REQ-SYS-018. The proposed values are therefore finalist-dependent: supported for A5 (needs 35 and 30 dB), not for A4 (needs 45 and 40 dB). **Fix:** state the proposal per finalist; for A4 propose 45 and 40 dB (or a CR on REQ-SYS-018), and say which branch of the TBR plan each finalist triggers | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-F1, A5, E3 | Note sections 1 item 2, 2 item 5, 3 rows "A5 PA harmonics" and "Power steps", 5 (A5 bullets) | REQ-SYS-017 and REQ-TX-007 name the 6.4 and 8.4 V supply extremes; REQ-SYS-012 holds the 5 W step over 6.4 to 8.4 V. Neither extreme appears in the note, and the PA harmonic ratio is used as if supply-independent without saying so. At 8.4 V the module gives about 10.5 W at full drive (F8), so the 5 W step is a VGG back-off state about 3 dB below saturation, outside the datasheet guarantee condition (6 W at 7.2 V, VGG adjusted). The note's own convention applies a back-off ratio of -17 dBc below the 5 W step, yet it checks REQ-SYS-018 at 5 W only with the -25 dBc guarantee and reports A5 "PASS ... on the guaranteed maxima". Under the note's convention the A5 60 dBc margin at 5 W and 8.4 V becomes +1.8 dB (retuned 1812SMS) and +0.8 dB (retuned air) on the Monte Carlo worst, and -1.6 and -2.8 dB on the finding-1 corners. F4 (gate sweep at 135 MHz, about -29.5 dBc at 3.7 W) suggests the real ratio at 3 dB back-off is better than -17 dBc, so the case may pass, but the note must show it. **Fix:** add the 6.4 and 8.4 V cases for every step, state and bound the A5 harmonic ratio at the 5 W step at 8.4 V (with its source and confidence), and restate the A5 verdict and the "guaranteed data" discriminator accordingly | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-B1, D1 | Note section 2 item 5; `run_lpf.py` `do_r5` lines 566 to 577, `required_att` | The spur at the antenna is computed as carrier at the antenna + PA ratio - harmonic attenuation. The carrier at the PA output is higher than at the antenna by the passband loss of the same filter, so the spur is under-stated, and the 60 dBc ratio over-stated, by the passband loss of that instance (0.2 to 0.4 dB at the reviewer's worst-2f corners; up to the build's worst loss, 0.65 to 1.30 dB, as a bound). No pass or fail changes on the note's own numbers. **Fix:** add the passband loss (and the relay loss) to the spur, or state the omission and its size | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-E4 | `run_lpf.py` lines 652 to 658; README "Runs" | The checker computes every verdict but always exits 0 (reviewer re-run: exit 0 with the passband criterion failing in every build); a failed known answer (`ka["pass"]`) or a failed log cross-check (`echo_check_L4_pass`) would also exit 0. 08 section 3.4 asks for a checker that exits non-zero on a failing case. **Fix:** exit non-zero on any failed known answer or cross-check, and on any failed criterion unless the note records the failure as the expected result (for example a list of expected FAIL keys) | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-D2 | Note section 1 last sentence; r5 `result.md` and `run_lpf.py` line 634; `run_lpf.py` docstring | (a) "the 10 uW floor binds only below 0.25 W" is wrong: from 0.25 W down to 0.1 W the 40 dB clause binds (for example 20 uW at 0.2 W); the floor binds below 0.1 W. `limit_97307e_w` computes it correctly. (b) The r5 `result.md` text says the attenuation comes from "runs r2 to r4"; it uses r2, r3, r4, r6 and r7. (c) The `run_lpf.py` docstring lists r1 to r5 only and "a copy of the two scripts"; three are copied. **Fix:** correct the three texts | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-B3, A5 | Note section 3 rows "Air-coil Q and SRF" and "Node pad capacitance"; `lpf_model.py` `air_coil`, `pad_cap` | (a) The hand-wound coil Q (217 and 223 at 146 MHz; nominal 0.8 x in r1 and Monte Carlo 0.6 to 1.0 x) has no heritage comparison. The Coilcraft 1812SMS, an air-core spring coil of the same 3.56 mm diameter, is specified at Q typical 120, minimum 100 at 150 MHz (Document 184-1). The model's nominal (about 175) is 1.45 times that typical value, and the effect of the bottom ground pour under the coil on Q is not stated. The r7 alternative ("median 0.42 dB, at no parts cost") rests on it. (b) The pad capacitance is parallel-plate only; the fringe field of 1206 and coil pads over 0.8 to 1.6 mm FR4 adds a fraction of the plate value, which lowers the cut-off further and raises the passband loss. **Fix:** compare the air-coil Q with a measured or catalog coil of similar geometry and state the direction of the ground-pour effect; add a fringe allowance or state its direction | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-A1, A6, H1 | Note header "Serves", section 7 item 2, section 8 | (a) The note does not name TPM-007 (the spurious-margin TPM that run r5 computes at the 5 W step), MOP-009, REQ-TX-007 or REQ-TX-008 (the transmitter-level parents of the filter allocations). (b) The proposed restatement of the passband criterion to 0.75 dB conflicts with the REQ-SYS-018 rationale ("with at most 0.5 dB insertion loss") and with the HZ-008 description in `docs/safety/hazards.json` ("at most 0.5 dB loss at 148 MHz"); no request to the requirement writer or the hazards writer is recorded (PDR plan section 5.3). **Fix:** name the ids and add the two writer requests | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-I2 | `s21_nominal_wide.png` and the five `s21_mc_wide.png` | The REQ-TX-009 and REQ-TX-010 mask segments are 8 and 12 MHz wide and sit under the finalist markers at -39 and -34 dB, so the 40 dB and 35 dB limits at 2f and 3f cannot be seen; only the REQ-TX-011 segment is visible. **Fix:** draw the two masks as a visible bar or annotation (for example a thicker segment with a label) | Open | Pending | |

### Per-case results (section F; one row per case the governing texts name)

"MC" is the note's 252-step worst; "corner" is the reviewer's extreme-value corner inside the note's own ranges (finding-1).

| Case | Condition (mode, power step, frequency, temperature, supply, key type) | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check (re-run, hand calculation or not re-checked) | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Filter 2f, 288 to 296 MHz, every build | REQ-TX-009: at least 40 dB | MC: r2 54.4, r3 50.8, r4 51.9, r6 44.8, r7 43.8 dB | +3.8 (r7) to +14.4 dB | corner: r6 41.4, r7 40.2, r2 48.9 dB | re-run: identical; corners by reviewer deck | finding-1, finding-2 |
| C-2 | Filter 3f, 432 to 444 MHz | REQ-TX-010: at least 35 dB | MC worst 68.0 dB (r7) | +33.0 dB | corner lowest 65.4 dB (air, K negative) | re-run: identical; corners by reviewer deck | finding-2 |
| C-3 | Filter 576 MHz to 1.5 GHz | REQ-TX-011: at least 40 dB | MC worst 65.8 dB (r3) | +25.8 dB | layout leakage and coupling estimates (note limitation 4); corners not run above 900 MHz | re-run: identical | none |
| C-4 | Passband 144 to 148 MHz loss | TS-012 7.3 WP-PDR-21: at most 0.5 dB | MC worst: r2 1.21, r3 1.30, r4 0.99, r6 0.71, r7 0.65 dB | -0.15 (r7) to -0.80 dB (r3) | corner: r6 0.90, r7 0.86, r2 1.94 dB; ESR estimate about 0.1 dB | re-run: identical; reviewer ABCD per step within 0.07 dB | finding-1 |
| C-5 | Proposed passband criterion, retuned 1812SMS | note section 7 item 2: at most 0.75 dB (TBR) | MC worst 0.71 dB | +0.04 dB | corner 0.81 to 0.90 dB, that is -0.06 to -0.15 dB | reviewer deck | finding-1 |
| C-6 | A5, 0.5, 1, 2 and 5 W steps at +1 dB, 2f to 10f, 50 ohm | 97.307(e) and REQ-SYS-017: 25 uW (-16.0 dBm) | min margin 10.8 dB (r7, 2 W, 2f) | +10.8 to +21.4 dB | back-off ratio estimate (-17 dBc); corner 2f lowers r7 to +7.2 dB | hand: 34.0 - 17 - 43.8 = -26.8 dBm, margin 10.8 | finding-1, finding-4 |
| C-7 | A4, same steps and orders | 97.307(e) and REQ-SYS-017: 25 uW | min margin 4.8 dB (r7, 5 W, 2f) | +4.8 to +15.4 dB | no vendor data; corner r7 +1.2 dB, r6 +2.4 dB | hand: 38.0 - 15 - 43.8 = -20.8 dBm | finding-1, finding-4 |
| C-8 | Keying ramp, every instant 1 mW to 6.3 W | 97.307(e) at each instantaneous level | A5 min 7.8 dB, A4 min 4.8 dB | +4.8 to +18.4 dB | as C-6 and C-7 | hand: A5 r7 at 4.99 W: 37.0 - 17 - 43.8 = -23.8 dBm, margin 7.8 | finding-6 |
| C-9 | A5, 5 W step, 6 W guarantee ratio | REQ-SYS-018 and REQ-TX-008: 60 dBc | min 8.8 dB (r7, 2f) | +8.8 to +19.4 dB | corner r7 +5.2 dB | hand: 43.8 - 35 = 8.8 | finding-4 |
| C-10 | A4, 5 W step | REQ-SYS-018 and REQ-TX-008: 60 dBc | BOM builds +5.8 to +9.4 dB; retuned -0.2 (r6) and -1.2 dB (r7) | -1.2 to +9.4 dB | assumption only; corner r6 -3.6 dB | hand: 44.8 - 45 = -0.2 | finding-1, finding-2 |
| C-11 | Supply 6.4 V and 8.4 V at every step (A5 5 W step at 8.4 V is VGG back-off) | REQ-SYS-017, REQ-TX-007 (25 uW); REQ-SYS-018 (60 dBc) | not analysed | not stated; reviewer, note's own -17 dBc convention: 60 dBc +1.8 (r6) and +0.8 dB (r7) MC, -1.6 and -2.8 dB corner | ratio at back-off unbounded | hand calculation | finding-3 |
| C-12 | Carrier 144.0012 to 147.9988 MHz | REQ-SYS-017 carrier frequencies | harmonic bands n x 144 to n x 148 MHz, band edges on the grid | covered | 2 MHz grid in Monte Carlo | re-run | none |
| C-13 | 7f, 1008 to 1036 MHz (aeronautical, HZ-008) | 97.307(e): 25 uW | A4 at most -63.8 dBm, A5 -72.8 dBm | +47.8 dB | leakage estimate | hand: 38.0 - 20 - 81.8 = -63.8 | none |
| C-14 | Ambient -10 to +45 C | REQ-SYS-114 | stated negligible (note limitation 7) | not stated | reviewer: 1812SMS TCL +5 to +70 ppm/C gives at most 0.4 % over 55 K; C0G about 0.2 %; both small against 5 % | hand calculation | none |
| C-15 | A5 REQ-SYS-012 at the 6.4 V pack end with the filter loss | REQ-SYS-012: 3.97 W at the SMA | retuned 1812SMS median/worst 0.52/0.71 dB: -0.30 to +0.49 dB | -0.30 to +0.49 dB | corner 0.90 dB: -0.49 to +0.11 dB | hand: 4.46 x 10^(-0.081) = 3.70 W | finding-1 |

## Readiness criteria

| # | Criterion | Evidence |
|---|---|---|
| R1 | Frozen blobs | Python loop over `git rev-parse 6bff79c:<path>` and `HEAD:<path>` for the 44 `product_files`: all equal at `HEAD` `9182ff2` |
| R2 | One command reproduces | README names `run_lpf.py all`; the note names the script but not the command. Reviewer re-run exit 0 with the values the note states; the exit status does not carry the verdicts (finding-5). Treated as met for the review |
| R3 | validate_docs for a JSON product | N/A: no JSON under a schema in the product |
| R4 | Author return | The author summary states the question, models, inputs with sources and estimates, results, known answers and the pre-order items; tools and TV status are in the note header |
| R5 | No TBD; TBR ids named | `grep -n TBD` on the note, the scripts and the README: none. REQ-TX-009, 010 and 011 carry `tbr` objects (owner Robin, plan, close by PDR) |
| R6 | Renders exist | 19 PNG files beside their decks; all cited in the note exist |

## Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

1. **Re-run.** `git archive 6bff79c | tar -x -C <scratchpad>/rv-lpf-ts012/x`, then `/Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-lpf/run_lpf.py all` from the export: exit 0, all seven runs. Every LTspice run went through `tools/ltspice-batch.sh` (wrapper result PASS, version line `LTspice 26.0.2 for MacOS`). Every deck is byte-identical to the committed deck (wrapper SHA-256 prefixes e557c8f1, e63dbd46, 1d7d1d50, 6c6bea4e, 57f0fbdc, ca32268e equal the committed `ltspice_provenance.txt`); every `result.md`, `mc_values.csv` and `retune_screen.json` is byte-identical; every numeric field of the seven `result.json` files is equal (field walk, relative tolerance 1e-9, `ltspice` and `scripts_sha256` excluded). The known answer (0.00045 dB) and the L4 echo and 288 MHz cross-checks reproduce.
2. **Analytic known answer (hand).** Chebyshev 0.1 dB, n = 7: g1 = 1.1811, g2 = 1.4228, g3 = 2.0966, g4 = 1.5733 give 22.79 pF, 68.62 nH, 40.45 pF, 75.88 nH at 165 MHz and 50 ohm (note 22.8, 68.6, 40.4, 75.9). Attenuation 10 log(1 + 0.023293 cosh^2(7 arccosh(f/165))) gives 47.96 dB at 288 MHz and 75.93 dB at 432 MHz (note 47.9 and 76.0; LTspice 47.916 and 75.967). Return loss at 0.1 dB ripple 16.43 dB (note 16.4).
3. **Independent ABCD model** (reviewer code, not `retune_screen.py`) on the r1 nominal parameters: 1812SMS build -0.631, -0.668, -0.717 dB at 144, 146, 148 MHz against LTspice -0.621, -0.656, -0.699 dB; air build -0.489 against -0.464 dB at 146 MHz. At 2f the two agree within 0.7 dB; at 3f the ABCD model (no coupling or leakage) gives 99.7 dB against LTspice 87.0 dB, which confirms the note's statement that coupling and leakage set the floor from 3f up.
4. **Per-step binding check** (answers TV-014 limitation 1, `.step` not validated by the TV record): the reviewer ABCD model on every row of `mc_values.csv` against the LTspice `.raw` of the same step agrees within 0.057, 0.025 and 0.063 dB at 146 MHz and 0.072, 0.026, 0.067 dB at 148 MHz for r2, r6 and r7 (252 steps each), so every table-bound parameter reached its step, not only L4. At 290 MHz the difference reaches 4.3 dB in r7 on steps near 45 dB, from the positive coil coupling that the ABCD model omits, which shows how much the estimated K moves the 2f result for air coils.
5. **Extreme-value corners** (reviewer decks `rv_corners.cir`, 24 steps with K at its minimum and maximum, and a second deck with K at both signs; run through the wrapper, PASS, SHA-256 prefixes c488cef7 and 77badde9; `.raw` read with spicelib). Board as one factor (0.8 mm with two vias: Lvia 0.27 nH, Cpad 0.34 and 0.53 pF; 1.6 mm with one via: 1.30 nH, 0.17 and 0.27 pF, from the note's own formulas); loss corner all L and C at +tol, ESR 0.4 ohm, ESL 1.2 nH, Q and SRF at their minimum, fringe and trace L at their maximum; 2f corner the opposite. Results: passband loss 1812SMS retuned 0.81 (0.8 mm) to 0.86 dB (1.6 mm), 0.90 dB with negative K; air retuned 0.70 to 0.74 dB, 0.86 dB with negative K; 1812SMS BOM 1.54 to 1.94 dB. 2f: 1812SMS retuned 41.4 dB, air retuned 40.2 dB (0.8 mm, K +0.03), 1812SMS BOM 48.9 dB. A two-level factorial of the same ten factors in the reviewer ABCD model found the same corners.
6. **Coilcraft data.** Document 184-1 (revised 12/02/21): 1812SMS-68N Q typ 120 min 100 at 150 MHz, SRF min 1.5 GHz, Irms 2.5 A; -82N 120/100, 1.3 GHz, 2.5 A; -47N 135/100, 2.1 GHz; -56N 125/100, 1.5 GHz; tolerance J 5 %, G 2 %; TCL +5 to +70 ppm/C; 184-2 coil diameter D 3.56 mm. All equal `lpf_model.COILCRAFT` and the note.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a reported result)

| Input | Note value | Source read | Agreement |
|---|---|---|---|
| BOM values | 22, 68, 39, 82, 39, 68, 22 | TS-012 8.3 rows 4 (C1206C220J1GACTU x2), 5 (1812SMS-68NJLC x2, -82NJLC x2 incl. drive LPF), E1 (C1206C390J1GACTU x2) | yes |
| 1812SMS Q and SRF | Q 100 min, 120 typ; SRF 1.5 and 1.3 GHz | Coilcraft 184-1 table | yes |
| C0G tolerance | J, 5 % | part numbers | yes |
| ESR, ESL | 0.1 to 0.4 ohm, 0.6 to 1.2 nH | labelled estimate (E) | stated as E; not verifiable (finding none; limitation 1) |
| Via inductance | 0.27 to 1.30 nH | reviewer: 0.2 h (ln(4h/d) + 1) with h 1.6, d 0.3 gives 1.30 nH; h 0.8 halved gives 0.27 nH | yes |
| Pad capacitance | 0.17 to 0.53 pF | reviewer: 6.76 mm2 over 1.6 mm, er 4.5 gives 0.168 pF; 10.64 mm2 over 0.8 mm gives 0.530 pF | yes (fringe omitted, finding-7) |
| Air coil L | 69.6 and 84.5 nH | reviewer: Nagaoka 0.81 at D/l 0.527 gives 68.4 nH sheet, Rosa -1.6 nH, leads +2.9 nH: 69.7 nH | yes |
| Air coil Q, SRF | 217, 1.46 GHz (68 nH) | reviewer: skin depth 5.46 um, R 0.160 ohm x 1.8 = 0.288 ohm, Q 216.6; Medhurst 0.4896 pF/cm x 0.356 cm = 0.174 pF, SRF 1.463 GHz | arithmetic yes; plausibility finding-7 |
| A5 harmonics | 2f -25, 3f -30 dBc at 6 W | F8: "2fo -25 dBc max and 3fo -30 dBc max at Pout 6 W (VGG adjusted)" | yes |
| A5 back-off | -17 dBc (2f), -25 dBc (3f up) | F4: -17.4 dBc at 0.3 W, 135 MHz; worst 3fo -50 dBc | yes (conservative; the 135 MHz point is outside the band) |
| A4 harmonics | -15 and -20 dBc | F17 assumption, Low | yes |
| 97.307(e) | 25 uW, 40 dB, 10 uW floor | corpus line 25 | yes (finding-6 on one sentence) |
| Power steps | 0.5, 1, 2, 5 W at +1 dB | REQ-SYS-011, 012 | yes; supply range not carried (finding-3) |
| A5 module power at 6.4 V | 4.46 to 5.13 W | TS-012 7.3 | yes (table 4.4 recomputed: every entry within 0.01 W and 0.01 dB) |

## Checklist answers

### A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | No | Question and ids stated; TPM-007, MOP-009, REQ-TX-007 and REQ-TX-008 not named (finding-8) |
| CK-ANA-A2 | Yes | TS-012 revision 4 commit `7d0d450`, sections 7.3 and 8.3 rows named; no CR dependency |
| CK-ANA-A3 | Yes | Every row of note section 3 carries D, C or E; estimates labelled |
| CK-ANA-A4 | Yes | Table above; every input that sets a result was checked |
| CK-ANA-A5 | No | Supply-independence of the PA ratio and positive-only coupling are unstated assumptions with unstated direction (findings 1 and 3); air-coil Q basis (finding-7) |
| CK-ANA-A6 | No | Filter criterion and requirement consequences not routed to the requirement and hazards writers (finding-8); REQ-TX-009/010 proposal not conditioned per finalist (finding-2) |

### B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Topology and parasitics stated; the harmonic budget omits the passband-loss term (finding-4); coupling sign not bounded (finding-1). Fixed series R with rising Q at the harmonics is stated in limitation 2 |
| CK-ANA-B2 | Yes | No vendor SPICE or S-parameter model used (limitation 2 says so); the datasheet table is the model basis and is identified by document and revision |
| CK-ANA-B3 | No | Known answers for the ideal filter and the log cross-checks quantified; no heritage or measurement comparison for the air-coil Q (finding-7) |
| CK-ANA-B4 | Yes | 0.5 MHz grid (r1), 2 MHz grid (MC) with 144, 146, 148, 288, 296, 432, 444 MHz on the grid; reviewer 1 MHz grid corner decks agree in trend |
| CK-ANA-B5 | Yes | Reviewer hand known answer, independent ABCD model, per-step binding check and corner decks (section above); the corner results disagree with the reported worst by more than the stated uncertainty (finding-1) |
| CK-ANA-B6 | No | Limitations listed, but no combined uncertainty on each margin; the MC spread is presented as the bound (finding-1) |

### C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | `.log` first line `LTspice 26.0.2 for MacOS`; wrapper blob `88b71475` equals HEAD and `git hash-object`; Python stack as in the lock |
| CK-ANA-C2 | Yes | LTspice Accredited (ACC-LTSPICE-001); Python scripts without TV record, result marked developer evidence in the note header |
| CK-ANA-C3 | Yes | `run_lpf.py all`; netlists (`.cir`), one `.ac` per deck |
| CK-ANA-C4 | Yes | Reviewer re-run identical (section above) |
| CK-ANA-C5 | Yes | TV-014 limitation 1 (`.step` statistics not validated): the note's L4 echo plus the reviewer per-step check cover the binding; limitation 3: the checker confirms the `.meas` values it needs exist |

### D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | dBm, dBc, W, uW conversions correct (38.0 dBm at 6.3 W; 34.0 dBm at 2.52 W; -16.0 dBm at 25 uW); the missing loss term is under B1 (finding-4) |
| CK-ANA-D2 | No | Note tables equal `result.json` to the stated precision (every row of 4.1, 4.2, 4.3, 4.4 cross-checked); three text errors (finding-6) |
| CK-ANA-D3 | Yes | 0.01 to 0.1 dB precision; no rounding away from a limit found |
| CK-ANA-D4 | Yes | `REQ_TX` constants carry the ids, `IL_MAX_DB` cites TS-012 7.3 and F17, `limit_97307e_w` cites the corpus; inclusive comparisons match "at least" and "at most" |

### E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | 97.307(e) quoted verbatim with corpus and issue date; REQ-TX values match the requirement statements |
| CK-ANA-E2 | Yes | Margins limit minus result in dB, sign correct; TPM-007 not referenced (finding-8) |
| CK-ANA-E3 | No | REQ-TX-009 retuned margin and A5 60 dBc at 8.4 V are within their uncertainty and reported as passing (findings 1 and 3) |
| CK-ANA-E4 | No | Checker exits 0 on failing criteria (finding-5) |
| CK-ANA-E5 | No | Proposed REQ-TX-009 and 010 values not supported for A4 (finding-2); proposed 0.75 dB criterion not met at the extreme corners (finding-1); the note does not edit any requirement file |
| CK-ANA-E6 | Yes | No TPM CBE proposed; `tpm.json` not edited |
| CK-ANA-E7 | Yes | "Developer evidence", "pre-build supporting evidence"; no closing credit claimed; REQ-TX-009 to 011 are Test-method requirements |

### F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Supply extremes 6.4 and 8.4 V missing (finding-3); all other named cases present (per-case table) |
| CK-ANA-F2 | Yes | Keying ramp instants covered; fault states of HZ-008 (gross frequency error) are outside the filter question |
| CK-ANA-F3 | No | Worst combination not analysed; tolerance corners use nominal parasitics (finding-1) |
| CK-ANA-F4 | No | A4 retuned and A5 retuned 2f margins are within twice their uncertainty without a sensitivity to the two largest inputs (board choice and coupling) (finding-1) |

### G1. Simulation decks and checkers

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | `hardware/sim/tx-lpf/`, results per run with deck, log, raw and plots |
| CK-ANA-G1-2 | Yes | One `.ac` per deck; generated netlists, no `NC_` nets |
| CK-ANA-G1-3 | Yes | 50 ohm source and load (antenna port ICD); BOM values equal TS-012; parasitics stated; non-50-ohm harmonic terminations stated as limitation 5 |
| CK-ANA-G1-4 | Yes | Reads `.raw` with spicelib and `.log` `.meas`; wrapper failure or a missing `.raw` stops the run |

### G7. Worst-case and tolerance

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | No | Monte Carlo with seed, count and uniform distribution stated, but independence of board-level and lot-level parameters is not argued and the sample maximum is reported as worst case (finding-1) |
| CK-ANA-G7-2 | Yes | Initial tolerances; temperature coefficients small and stated (per-case C-14); no derating question in this analysis (power handling in limitation 7: 0.36 A rms against 2.5 A Irms; 25 V peak against 100 V) |

### H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | HZ-008 K1 named; the HZ-008 description's "0.5 dB loss" is not sent to the hazards writer (finding-8) |
| CK-ANA-H2 | Yes | The A5 harmonic risk (TS-012 7.1, 8 Yellow) and the A4 Red (16) are addressed in section 5 as evidence for TS-012, with no re-score claimed ("It moves no score") |
| CK-ANA-H3 | Yes | Change log revision 1, 2026-09-28 |

### I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | All 19 renders opened with the Read tool: r1 `s21_nominal_wide`, `il_nominal_passband`, `rl_nominal_passband`; r2, r3, r4, r6, r7 `s21_mc_wide`, `il_mc_passband`, `mc_histograms`; r5 `harmonic_budget` |
| CK-ANA-I2 | No | Axes, units, legends, titles and the 0.5 dB, 25 uW and 60 dBc lines are drawn; plotted values agree with the checker at the marked points (for example A4 retuned 2f at about -21 and -22 dBm against the -22 dBm line); REQ-TX-009 and 010 masks hidden (finding-9) |

**ITEMS N/A:** CK-ANA-G2 to G6 (analysis_kind is simulation-deck and worst-case), CK-ANA-J1 to J3 (criticality neither).

## Cross items (returned to Claude as lead SE)

- **X-1.** The design change the note proposes for A5 (BOM rows 4 and E1 to 18 and 33 pF) trades about 10 dB of 2f attenuation for 0.2 to 0.5 dB of loss. With finding-1 and finding-3 the 2f margin of that set is thin; TS-012 should carry the choice with the corrected margins, not the Monte Carlo ones.
- **X-2.** INSP-114 finding-5 raised the same exit-status defect in `run_pa.py` at Minor; finding-5 here is kept at the same severity for consistency.

## Commands

- Freeze and blobs: Python loop over `git rev-parse 6bff79c:<path>` and `git rev-parse HEAD:<path>` (44 files).
- Re-run: `git archive 6bff79c | tar -x -C <scratchpad>/rv-lpf-ts012/x`; `cd <scratchpad>/rv-lpf-ts012/x && /Users/robinonsay/rust/cwht/.venv/bin/python hardware/sim/tx-lpf/run_lpf.py all` (exit 0); `cmp` and a JSON field walk against the committed results.
- Independent checks: `<scratchpad>/rv-lpf-ts012/indep_abcd.py`, `corners.py`, `corners2.py`, `perstep.py` (scratchpad only, not committed).
- Corner decks: `tools/ltspice-batch.sh -t 600 -o <scratchpad>/rv-lpf-ts012/corner_run -b rv_corners.cir` and the same in `corner_neg` (both PASS, exit 0).
- Datasheet: WebFetch of the Coilcraft PDF URL the note cites; pages 1 and 2 read.
- Record check: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`.

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/lpf-ts012.md@d59a99b5, hardware/sim/tx-lpf/run_lpf.py@db36b9d8, lpf_model.py@e7c98d37, retune_screen.py@042e1657, decks and results as in product_files, at 6bff79c
FINDINGS:
- [Major] CK-ANA-G7-1, F3, F4, B6, E3, E5 finding-1: the Monte Carlo sample maximum is reported as worst case; extreme corners inside the note's own ranges (board choice as one factor, K of both signs) give retuned 1812SMS 0.81 to 0.90 dB and 2f 41.4 dB, retuned air 0.74 to 0.86 dB and 2f 40.2 dB, BOM 1812SMS 1.94 dB; the proposed 0.75 dB criterion fails and several margins shrink.
- [Major] CK-ANA-E5, A6 finding-2: "keep 40 and 35 dB" for REQ-TX-009 and 010 is not supported for A4, which needs 45 and 40 dB for the 60 dBc target under the note's own assumption.
- [Major] CK-ANA-F1, A5, E3 finding-3: the 6.4 and 8.4 V cases of REQ-SYS-017 and REQ-TX-007 are missing; the A5 5 W step at 8.4 V is a VGG back-off state outside the datasheet guarantee, and under the note's own back-off convention its 60 dBc margin is +0.8 to +1.8 dB (Monte Carlo) and negative at the extreme corners.
- [Minor] CK-ANA-B1, D1 finding-4: spur formula omits the passband loss (0.2 to 1.3 dB optimistic).
- [Minor] CK-ANA-E4 finding-5: checker exits 0 on failing criteria, known answer or cross-check.
- [Minor] CK-ANA-D2 finding-6: 10 uW floor sentence; r5 "runs r2 to r4"; docstring.
- [Minor] CK-ANA-B3, A5 finding-7: air-coil Q has no heritage check (1812SMS of the same diameter: Q typ 120); pad fringe omitted.
- [Minor] CK-ANA-A1, A6, H1 finding-8: TPM-007, MOP-009, REQ-TX-007, 008 not named; 0.75 dB proposal not routed against REQ-SYS-018 rationale and HZ-008 text.
- [Minor] CK-ANA-I2 finding-9: REQ-TX-009 and 010 masks hidden under markers.
ITEMS N/A: CK-ANA-G2 to G6 (analysis_kind simulation-deck, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: REQ-TX-009 40 dB (not supported for A4; A5 supported with 0.2 to 1.4 dB corner margin); REQ-TX-010 35 dB (not supported for A4); REQ-TX-011 40 dB (supported); WP-PDR-21 loss criterion 0.75 dB worst case (not supported)
MEASUREMENTS: size=6 decks, 1266 LTspice steps plus 48 reviewer corners; inputs_checked=14 rows (every input that sets a reported result); renders=19; turns=55; minutes=80; major=3; minor=6
```
