---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-19 receiver band-pass
# filter, image, half-IF and cascade analysis for the TS-012 finalists A4 and A5.
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Approved 2026-09-28, merge held at the
# section 9 pre-merge check; the branch head is not an ancestor of main at HEAD c5ccea8). tools/validate_docs.py
# requires the checklist field to name a template that exists on main, so the field names
# peer-review-checklist-design revision B and checklist_analysis records the template actually applied, as INSP-056,
# INSP-083, INSP-114 and INSP-115 did. The delta iteration after CR-012 merges switches the field.
# Iteration history: iteration 1 reviewed revision 1 of the note (commit 7200be7); the lead SE filed that reviewer's
# own record at 30681fc (INSP-117). Iteration 2 is the delta on the Major fixes (rule C1) at d2d89e9.
# Filed by the lead SE on 2026-09-28: the harness refused this iteration 2 reviewer's Write, so its front matter and
# its iteration 2 sections are taken verbatim from its final validated scratch copy (record_final.md). Its own
# "Iteration 1" section, a transcription made because it found no filed record, is omitted: the original
# iteration 1 record text above is kept instead.
# id: the brief assigned no id. INSP-117 is above every id on main at HEAD c5ccea8, on every local branch and in the
# working tree at the time of review (INSP-116 is the highest in use); the lead SE renumbers it if a parallel
# reviewer took the same id.
# Filing: the harness refused the reviewer's Write of this file ("Subagents should return findings as text"); the
# reviewer returned the full text and the lead SE files it verbatim.
# Iteration 3 (rule C1, the last iteration): a delta on note revision 3 at a82f21b (fix of the iteration 2 Major),
# written into this record with the Edit tool by reviewer:WP-PDR-19-analysis-rx-bpf-iter3. It also reconciles the
# finding numbering: the iteration 2 record re-used the labels finding-6 to finding-9, which the iteration 1 record
# (30681fc) had already given to five Minors never relayed to the author. From iteration 3 the record-wide ids are:
# finding-1 to finding-10 as in iteration 1; iteration 2's finding-6, 7, 8, 9 are finding-11, 12, 13, 14; iteration 3
# raises finding-15 and finding-16 and re-classifies finding-7 Major (mapping table in the iteration 3 section; the
# earlier sections stay as filed).
# Iteration 3 re-issue 1 (the owner-authorized fourth iteration, status note 2026-09-29 section 2, "Yes both recs sound
# good"): a delta on note revision 4 at 63122e7 (fix of the escalated Major finding-7), written into this record with
# the Edit tool by reviewer:WP-PDR-19-analysis-rx-bpf-iter4. The schema caps iteration at 3, so it is recorded as
# "Iteration 3 re-issue 1" (precedent INSP-009, INSP-038, INSP-075, INSP-110); the body calls it the fourth iteration.
# It verifies finding-7 and raises finding-17 (Minor).
id: INSP-117
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-rx-bpf-ts012.md
product: docs/design/analysis/rx-bpf-ts012.md
# product_commit (iteration 3 re-issue 1): 63122e7, note revision 4 with run r13 (the delta of rule C1 on the
# escalated finding-7). The blobs below are the files 63122e7 changed or added that the delta reviews, plus the
# unchanged library scripts r13 executes. Each equals git rev-parse 63122e7:<path>, git rev-parse HEAD:<path> at HEAD
# 63122e7 and git hash-object <path> (19 of 19). The r13 scripts/ copies are byte-identical to the frozen scripts;
# LTspice .log and .raw are not listed (the reviewer's re-run regenerated them; every r13 .raw is under 5 MB, so no
# raw.sha256 manifest is due). Iteration 3 listed 19 blobs at a82f21b (note 056d5580, worst_case.py 29bd02fd,
# tolerance.py e77b19ed, README 3fe9b26d, run_sims.py da44cc64, the r12 decks and results); iteration 2 listed 59 at
# d2d89e9 (record at 79795e4).
product_commit: "63122e70b241c1999abf4eafc91e469b2ca982c9"
product_files: ["docs/design/analysis/rx-bpf-ts012.md@11bb983640aa82034c4d31af0915d64c56245353", "hardware/sim/rx-frontend/README.md@f0951ca036c38f2fe12a57f3a23b26a665703ba3", "hardware/sim/rx-frontend/run_sims.py@923aeb147e759b91b075a19106b85b2f832d62b3", "hardware/sim/rx-frontend/worst_case.py@42dd5c11649db1b69b0445786e00061db3799e6b", "hardware/sim/rx-frontend/tolerance.py@64babc73cc15700c42f12dabf43fd5abe7f8b7ae", "hardware/sim/rx-frontend/bpf_nodal.py@f2fbc6c3cba656efd15c6e499351909d23e2b57d", "hardware/sim/rx-frontend/bpf_design.py@bb3e7e566f8146a5d53a295f5788f8ceac7297cb", "hardware/sim/rx-frontend/make_decks.py@f673891014d483a2ccf4c94111b6b909748671e2", "hardware/sim/rx-frontend/decks/bpf_2p3p4_if8_temp.net@4885fee8dce5aee3ed123331ad1b26574fb30d94", "hardware/sim/rx-frontend/decks/bpf_2p3p4_if8_temp_cases.json@2fe40353134402bd7199ba90d33935e00201640a", "hardware/sim/rx-frontend/decks/bpf_2p3p2_if10_temp.net@67d05f25b10e40ce6483d118faaba13abea6f87c", "hardware/sim/rx-frontend/decks/bpf_2p3p2_if10_temp_cases.json@5224758e5d92795cb7187c18376de1d1e03b703b", "hardware/sim/rx-frontend/decks/bpf_2p3p3_if8_temp.net@1866af62822cf9acfc371d6710ddd0197fb17420", "hardware/sim/rx-frontend/decks/bpf_2p3p3_if8_temp_cases.json@2ca4a123c85f69f6516c52a50bde3cad24ecc000", "hardware/sim/rx-frontend/results/2026-09-29-r13-bpf-temperature/prepare.json@2563a8e6ea612afd6ddddc73a6b1c8f65e55eb94", "hardware/sim/rx-frontend/results/2026-09-29-r13-bpf-temperature/result.json@0fd22a5d1c1ae98dc99fbe97be3bb332b3290f13", "hardware/sim/rx-frontend/results/2026-09-29-r13-bpf-temperature/result.md@ee226013035ee0213de4b654259ef491a9f0701e", "hardware/sim/rx-frontend/results/2026-09-29-r13-bpf-temperature/temperature_residual.png@2af3ecde27558b3b0ba086b3ed03879f9acb9566", "hardware/sim/rx-frontend/results/2026-09-29-r13-bpf-temperature/temperature_sweep.png@91e22b28a1eeff8a7a7f85ff06da34b239e9cd44"]
analysis_kind: [simulation-deck, cascade, worst-case]
# product_size: iteration 3 was "1 note (468 lines, revision 3; 45 added, 16 removed); worst_case.py +230, run_sims.py
# +2; README 9 lines; 3 decks of 6 cases (18); run r12 (45 grid points, 9 bisections); 2 new plots"
product_size: "iteration 3 re-issue 1: 1 note (632 lines, revision 4; 210 lines added, 46 removed); 3 scripts changed (worst_case.py +300 -8 for r13, tolerance.py +17 -5, run_sims.py +2); README (+11 -5); 3 new LTspice decks (22 cases); 1 run r13 (99 grid points, 9 bisections, a 33-point board temperature sweep, 3 exact-map room cross-checks, 2 doubled-coefficient cases); 2 new plots, both cited by the note"
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/rx-frontend/*.py, including the numpy nodal solver: developer evidence per 05 section 9.1, as the note says"]
# values_proposed: the note proposes no TBR value (REQ-SYS-033 70 dB and REQ-SYS-022 -140 dBm are kept; the 45 dB
# relaxation is named and not recommended). It reports a TPM-005 current best estimate to the TPM owner (section 8)
# and proposes design inputs (tolerance mode B, re-alignment residual, port VSWR 1.2, 0.03 pF stray) and a TS-012
# criterion replacement, which are not requirement values.
# values_proposed at iteration 3 re-issue 1: revision 4 moves the TPM-005 report to the design filter 2 + 3 + 4
# (iteration 3: CBE -141.2 dBm for A5 with 2 + 3 + 3, A4 -141.5 dBm, Yellow). It also proposes the 2 + 3 + 4
# alignment acceptance +/-0.62 % and a 20 to 30 C alignment temperature as build conditions (design inputs, not
# requirement values)
values_proposed: ["TPM-005: CBE -140.7 dBm (A5, 2 + 3 + 4, nominal cascade at 25 C; A4 -141.1 dBm), Yellow; Red at the TC-SYS-017 filter corner (-134.9 / -136.3 dBm) and at the stack (supported; estimates)"]
# renders_inspected: iteration 3 re-issue 1 opened the 2 new r13 plots the note cites (the committed files) and
# compared the reviewer's regenerated copies pixel for pixel (equal); iteration 3 opened 2 (r12), iteration 2 16
renders_inspected: 2
sprint: PDR-prep
author_agent: "author:WP-PDR-19 rx-frontend (Claude as analysis author, TS-012 discriminating analyses; revision 1 at 7200be7, revision 2 at d2d89e9, revision 3 at a82f21b, revision 4 at 63122e7)"
reviewer_agent: "reviewer:WP-PDR-19-analysis-rx-bpf-iter1 (independent; findings returned as text, record filed by the lead SE at 30681fc); iteration 2 by reviewer:WP-PDR-19-analysis-rx-bpf-iter2 (independent; authored no part of the note, its revisions, the decks, the scripts, the results or TS-012); iteration 3 by reviewer:WP-PDR-19-analysis-rx-bpf-iter3 (independent; authored no part of the note, its revisions or fixes, the decks, the scripts, the results or TS-012); iteration 3 re-issue 1 (the owner-authorized fourth iteration) by reviewer:WP-PDR-19-analysis-rx-bpf-iter4 (independent; authored no part of the note, its revisions or fixes, the decks, the scripts, the results or TS-012, and took no part in iterations 1 to 3)"
# criticality: a hardware-only receiver analysis; it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
# iteration: 3 is the record schema maximum; the owner-authorized fourth iteration is "Iteration 3 re-issue 1"
iteration: 3
# readiness_met (iteration 3 re-issue 1): R1 frozen (19 of 19 blobs equal at 63122e7, HEAD and the working tree), R2
# reproduced from a git archive export, R5 and R6 hold (reviewer re-run section)
readiness_met: true
# reviewer_verdict (iteration 3): NEEDS CHANGES. finding-11 (iteration 2's finding-6) is Verified at a82f21b, but
# finding-7 (iteration 1, REQ-SYS-114 temperature not analysed; Minor then, never relayed to the author) is
# re-classified Major: revision 3 leaves 2 + 3 + 3 0.02 % of residual headroom, and a C0G drift inside its own
# +/-30 ppm/K class moves every resonator 0.03 to 0.05 % down at one end of -10 to +45 C, so the reported 2 + 3 + 3
# image pass is not shown over REQ-SYS-114 (69.93 to 69.75 dB at the +/-0.3 % estimate). Rule C1: this was the last
# iteration, so the open Major escalates to the owner. finding-15 and finding-16 are new Minors.
# reviewer_verdict (iteration 3 re-issue 1, note revision 4 at 63122e7): APPROVED. finding-7 (Major) is Verified: r13
# carries the drift over REQ-SYS-114 per resonator from datasheet classes the reviewer re-read (KEMET C1003_C0G,
# Coilcraft 184-1) and the thermal note's V18 bound; 2 + 3 + 3 is withdrawn as not shown; the design 2 + 3 + 4 holds
# 75.37 dB (+5.37 dB) hot at the estimate, reproduced exactly from a clean export. No Major is open. New finding-17
# (Minor): the +70 C bound is main-bay air, not the resonator part temperature, and the +/-0.62 % acceptance holds
# only to about +73 C. The Minors stay liens (rule C1)
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict (iteration 3 re-issue 1): held at NEEDS CHANGES only because the applied analysis template is still only on
# cr/CR-012 (not on main at 63122e7; lead SE convention of 2026-09-27, INSP-083, as INSP-114 and INSP-116). Iteration 3
# was NEEDS CHANGES on the open Major finding-7. Counts are record-wide on the reconciled numbering (17 findings:
# finding-1 to 10 of iteration 1, finding-11 to 14 of iteration 2, finding-15 and 16 of iteration 3, finding-17 of
# re-issue 1). Verified: finding-1 to 5, finding-7 and finding-11. Open (all Minor, liens): finding-6, 8 to 10, 12 to 17
verdict: NEEDS CHANGES
findings_major: 5
findings_minor: 12
findings_open: 10
findings_fixed: 0
findings_verified: 7
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no (iteration 3 re-issue 1): the items that stay No on the open findings (finding-6: A2, A3, B2; finding-8 and
# 17: A5; finding-8 and 12: F3; finding-8, 14 and 16: D3; finding-9 and 14: D2; finding-9 and 13: I2; finding-10 and
# 16: G7-1; finding-15 and 17: G7-2). A1, E3 and F1 return to Yes with finding-7 Verified. Iteration 3 was
# [A1, A2, A3, A5, B2, D2, D3, E3, F1, F3, G7-1, G7-2, I2]
items_no: [CK-ANA-A2, CK-ANA-A3, CK-ANA-A5, CK-ANA-B2, CK-ANA-D2, CK-ANA-D3, CK-ANA-F3, CK-ANA-G7-1, CK-ANA-G7-2, CK-ANA-I2]
# effort: iteration 3 re-issue 1 only (iteration 3: 45 turns, 95 minutes; iteration 2: 80 turns, 120 minutes;
# iteration 1 effort was not recorded)
effort_turns: 40
effort_minutes: 60
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record: receiver BPF, image, half-IF and cascade, TS-012 finalists A4 and A5 (INSP-117, iteration 1)

**Product:** `docs/design/analysis/rx-bpf-ts012.md` (`5c60b967`) with `hardware/sim/rx-frontend/` (README `a1f72599`; `bpf_design.py` `bb3e7e56`, `make_decks.py` `293a3100`, `run_sims.py` `557ad0ee`, `check_bpf.py` `962ebe12`, `check_halfif.py` `63fd8097`, `cascade.py`, `explore.py`; 29 decks with their draw and case files; runs r01 to r06) at freeze commit `7200be7` (rule C2). Every blob equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at `HEAD` `7200be7`; no product file is modified in the working tree.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck (filter and mixer decks), cascade (receiver NF, gain, image and half-IF referral) and worst-case (Monte Carlo tolerance runs): sections A to F, G1, G5, G7, H and I apply. G2, G3, G4 and G6 are N/A; J is N/A (criticality neither).

**Acceptance criteria (rule C7, every case the governing texts enumerate):**
- REQ-SYS-033 (`docs/requirements/sys/requirements.json`): "The transceiver shall reject image and intermediate-frequency responses by at least 70 dB (TBR) relative to the in-band response." Verification Analysis, closing case TC-SYS-021, whose procedure computes the responses "for tuned frequencies at 100 kHz spacing across the band" and repeats "with every toleranced input at its worst-case corner".
- REQ-SYS-022: "minimum discernible signal of at most -140 dBm (TBR) in a 500 Hz bandwidth", MDS = -147 dBm + NF; `mop_ids` MOP-006 and TPM-005. REQ-SYS-023 (Goal): -142 dBm. TC-SYS-017 evaluates 144.05, 146.00 and 147.95 MHz and a worst-case corner.
- TPM-005 (`docs/plan/tpm.json`, rx-mds): planned -140 dBm; `margin_policy` PDR "cascade noise-figure budget gives <= -142 dBm (2 dB margin on the -140 dBm threshold)"; yellow "worse than the phase margin_policy value but no more than 3 dB worse than -140 dBm"; red "more than 3 dB worse than -140 dBm".
- REQ-SYS-114: -10 C to +45 C ambient, which conditions REQ-SYS-022 and REQ-SYS-033.
- TS-012 revision 4 (commit `7d0d450`) section 7.3, WP-PDR-19: image "BPF1 plus BPF2 with coil Q 100, 20 % coupling-capacitor tolerance and 5 nH ground-via inductance; pass: at least 90 dB at 128 to 132 MHz and at most 3 dB passband loss"; half-IF "front end and ring with a -70 dBm tone at RF - 4 MHz ... against a -140 dBm tone at RF; pass: the RF - 4 MHz tone gives an IF output no higher than the -140 dBm wanted tone ..., with the BPF attenuation at 140 MHz reported".

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query on the INSP id register and the TS-012 analysis records) preceded every `grep`; `grep` only pinned lines in TS-012, INSP-110, the research notes, the status note and the requirement files. The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28).** onsemi MMBFJ309/MMBFJ310 Rev. 1.5, https://www.onsemi.com/pdf/datasheet/mmbfj310-d.pdf (read 2026-09-28, SHA-256 prefix `2e01eca4`, `pdftotext -layout`); Coilcraft Document 184-1 revised 12/02/21, https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf (read 2026-09-28); MACOM 1N5711 Rev. V3, https://cdn.macom.com/datasheets/1N5711.pdf (read 2026-09-28). The Si5351 summary row was not re-read (its values set only the LO duty cases, which the reviewer's re-run reproduces).

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-E3, G7-1, B6, D2 | note sections 3 item 4, 4.2 table and "Best achievable" bullet 2, 5 table row "Image with BPF3" and "Recommended change"; `cascade.py` `pass_70_modeA`; README r03 row | The Monte Carlo minimum of 200 runs is reported as a pass statistic, and the mode A pass it supports does not hold for the population. The note states "REQ-SYS-033's 70 dB is met in every Monte Carlo run by 2 + 3 + 3 at IF 8 MHz in both modes, and by 2 + 3 + 2 at IF 10 MHz", and section 5 reports "PASS: ... 70.6 dB (mode A)". A margin of 0.6 dB on the minimum of 200 draws is inside the sampling scatter of that minimum, and the note gives no uncertainty for it. Reviewer re-draw of the same distributions (mode A: coupling and end capacitors x U(0.8, 1.2), L x U(0.994, 1.006), Q 100, 5 nH, capacitor Q 500) with an independent nodal model that reproduces every LTspice nominal within 0.1 dB, 20,000 runs: 2 + 3 + 3 at IF 8 MHz minimum 65.6 dB, 0.1 % quantile 68.5 dB, 0.32 % of builds below 70 dB (already 68.6 dB minimum in a 200-run draw with another sequence); 2 + 3 + 2 at IF 10 MHz minimum 66.6 dB, 0.04 % below 70 dB. Mode B holds: 2 + 3 + 3 minimum 74.6 dB and 0.1 % quantile 77.3 dB; 2 + 3 + 2 at IF 10 MHz minimum 77.4 dB. TC-SYS-021 asks for "every toleranced input at its worst-case corner", not a sample minimum. Consequence: with the TS-012 20 % capacitors BPF3 does not meet REQ-SYS-033 for every build (about 1 in 300 fails), so the recommended fix depends on the mode B part specification, which the note offers beside the fix rather than as its condition; and the proposed replacement criterion "at least 70 dB in every Monte Carlo run (mode B, coil Q 100)" is sample-size dependent. Fix: report mode A for 2 + 3 + 3 and for 2 + 3 + 2 at IF 10 MHz as not meeting 70 dB for every build (with the fraction), make the mode B tolerances a condition of the BPF3 recommendation, state the Monte Carlo acceptance as a population statistic with N and a confidence (for example the 0.1 % quantile from at least 10,000 runs) or as the TC-SYS-021 worst-case corner, and correct the section 5 table, the author summary and `cascade.py` | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-G1-3, B1, A5, A6 | note section 3 item 2, section 4.2 element table, section 6 bullet 1; `make_decks.py` `ports()`; decks `R<k>s`, `R<k>l` 50 ohm | Every filter section is simulated between 50 ohm resistive ports, and the reported losses, image values and the element values proposed for the build hold only for those ports. In the design the ports are the MMBFJ310 grounded-gate inputs (after BPF1 and BPF2) and the J310 drains (before BPF2 and BPF3). The datasheet the note cites gives common-gate input conductance Re(yig) 12 mmhos typical at 100 MHz (83 ohm) and gfs 8 to 18 mS (56 to 125 ohm), with Csg 4.1 pF typical; the drain side has goss 150 umhos and Cdg 2.0 pF and needs a network to present 50 ohm. The note states "ideally isolated" sections but neither the 50 ohm port assumption nor that the J310 stages must be matched to it, and no TS-012 schematic defines these interfaces. Reviewer sensitivity (same nodal model, coil Q 100, resistive ports only, reactive parts assumed tuned out): BPF1 into 125 ohm worst in-band loss 1.96 to 2.54 dB, which raises the A5 + BPF3 nominal NF from 5.81 to 6.39 dB (MDS -141.2 to -140.6 dBm); BPF2 and BPF3 driven from 200 ohm give 2 + 3 + 3 image rejection 79.2 to 80.6 dB against 86.0 dB, and 1.8 dB more power-wave loss per section. These moves are of the order of the reported margins (1.2 dB MDS nominal, 8.1 dB mode B image). Fix: state 50 ohm ports (with a tolerance) as a design input to the J310 stages, sent to the TS-012 author and the receiver schematic writer (A6), or model the J310 input and output admittances from the datasheet rows; report the sensitivity of the image, the losses and the MDS to the port impedances | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-E3, E2, A1 | note header "Serves" row, section 4.5 table and findings 2, section 5 table row "REQ-SYS-022 MDS"; author summary "MDS about -141.2 dBm nominal (PASS)"; `cascade.py` `mds_pass_nominal` | REQ-SYS-022 is reported as "nominal PASS (1.2 dB)" while the note's own spread (filter corner -139.1 dBm, stack -135.3 dBm, every active stage an estimate of Low confidence) is larger than that margin, and TPM-005, the TPM of REQ-SYS-022, is not named. TPM-005's PDR margin policy is a cascade result of -142 dBm or better (2 dB margin); every configuration misses it (best -141.5 dBm). By the TPM-005 thresholds the proposed A5 + BPF3 line-up is Yellow at nominal and at the filter corner (-139.1 dBm is within 3 dB of -140) and Red at the stack (-135.3 dBm is 4.7 dB worse). The note does say the requirement "stays at risk", but CK-ANA-E3 requires that a case whose margin is below its uncertainty not be reported as passing. Fix: name TPM-005, compare each configuration with its PDR margin policy and thresholds, report REQ-SYS-022 as not shown with margin (nominal +1.2 dB against an uncertainty of several dB), and send the TPM-005 status to the TPM owner and the risk to the WP-PDR-18 risk writer (finding-6) | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-E4, D4 | `check_bpf.py` `__main__`, constant `REQ = 70.0`; `cascade.py` `main()`; `check_halfif.py` | The checkers write pass or fail into `result.json` and `result.md` but always exit 0, including r01 (REQ-SYS-033 FAIL at every step) and r06 (REQ-SYS-022 FAIL at the filter corner); reviewer runs: exit 0 for all four `check_bpf.py` runs and for `cascade.py`. `REQ = 70.0` carries no requirement id in the comment next to it (the docstring names REQ-SYS-033). 08 section 3.4 and CK-ANA-E4 ask for a non-zero exit on a failing case. Fix: exit non-zero on a failing verdict (or a `--check` mode with the expected FAIL states listed in the note) and put the id beside each acceptance constant | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-F3 | note section 4.3 table and the sentence "three sections tolerate per-section strays up to 0.1 pF"; `make_decks.py` `leak_deck` | The leakage run is nominal only, with two leak phases (+1 and -1). Combined with the mode B tolerances and a magnitude-sum bound on the phase, the reviewer's 20,000 runs give 2 + 3 + 3 at 0.1 pF per section a minimum of 69.9 dB (0.01 % below 70 dB, 0.1 % quantile 70.8 dB); with mode A the minimum is 58.9 dB and 8.3 % of builds fall below 70 dB. The conclusion "tolerate ... up to 0.1 pF" therefore holds nominally only. Fix: state the leakage result as nominal, or run it with the tolerance draws and a phase sweep, and carry the combined figure into the 80 dB nominal criterion of section 5 | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A2, A3, B2, E5, H2, H3 | note header, section 2 rows "1N5711 SPICE model" and "Crystal ladder loss", sections 5 and 7 | Traceability gaps that change no number: (i) TS-012 revision 4 is cited without its commit `7d0d450` (A2); (ii) `docs/research/cw-selectivity-options.md` F7 is cited without its confidence tag (High for arithmetic, Medium for nominal Cm and Rs), and the note does not say that F5, F7 and risk item 6 there bound catalogue crystal Rs only at 60 ohm, so the 12 dB ladder corner may be optimistic (reviewer: 16 dB of ladder loss raises the nominal NF by 0.5 dB) (A3); (iii) the 1N5711 model is "for example evenator/LTSpice-Libraries standard.dio", with no file, version, date or hash (B2); (iv) the proposal to keep REQ-SYS-033 at 70 dB does not name the `tbr.plan` step it executes (TS-001 closes the value at PDR, owner approval in the PDR memo) (E5); (v) the TS-012 section 7.1 receiver risk rows (A5 MDS or image 12 Red; A4 JFET mixer 12 Red) are re-quantified here but not sent to the WP-PDR-18 risk writer (H2); (vi) the header says "revision 1" but the note has no change history (H3). Fix: add them | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-F1, A5, G7-2 | note sections 3 and 6 | REQ-SYS-114 (-10 C to +45 C) is not named and temperature is not stated as an assumption. Reviewer bound (estimate): a common-mode resonator shift of 80 ppm/C (air coil plus C0G maximum) from a 25 C alignment gives 2 + 3 + 3 image rejection 87.3 dB at -10 C and 85.3 dB at +45 C and at most 0.12 dB more section loss, inside the +/-0.3 % residual detuning already drawn, so no verdict changes; the device terms (J310 gain and NF, crystal Rs) move the MDS in the direction of the stack corner already reported. Fix: state the temperature assumption and its direction in section 6 | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-F3, A5, D3 | note section 4.4 ("nominal gains (the worst case, since a higher front-end gain raises the product)") and section 4.3 (isolation 84 dB); `cascade.py` J310 gain 12 dB | The half-IF referral and the isolation need use the nominal J310 gain of 12 dB and call it the worst case, but the datasheet common-gate power gain is 16 dB typical at 100 MHz, so the highest-gain case is not analysed. Reviewer arithmetic with 16 dB per J310 (front-end gain 22.5 dB instead of 14.5 dB): A4 half-IF equivalent -147.6 dBm (margin 7.6 dB instead of 16 dB), A5 -169.3 dBm; antenna-to-mixer isolation need 92.5 dB instead of 84 dB, above the 85 dB PCB design input proposed in sections 5 and 7. No half-IF verdict changes. Also 70 + 14.48 = 84.48 dB is reported as 84 dB, rounded away from the conservative side (D3). Fix: analyse the highest front-end gain and set the isolation input from it | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-D2, I2, B1 | note section 4.1 bullet 3, section 3 item 2 against section 6 bullet 3; `results/2026-09-28-r06-cascade/cascade_nf_gain.png`; `check_halfif.py` `axvspan(-58.5, -51.8)` | (i) Section 4.1: "For a 4 MHz band at 146 MHz with Q 100 to 200, every resonator costs about 0.6 to 1.3 dB"; the note's formula gives 0.9 to 1.7 dB for 4 MHz (g about 1.1), and 0.6 to 1.1 dB for the 6 MHz design bandwidth the decks use. (ii) Section 3 models coil loss as a series resistance set at 146 MHz; section 6 calls it "a frequency-proportional series resistance". The decks use a fixed resistance, which gives Q proportional to frequency. (iii) In `cascade_nf_gain.png` the cumulative NF curves of the two two-section chains end at about 5.3 dB (nominal) and 6.5 dB (filter corner) while the panel titles and `result.md` give 5.84 and 7.24 dB (A5) and 5.71 and 7.06 dB (A4): the image-noise term is added after the plotted cascade. (iv) The mixer-input band and limit segment of both half-IF plots are typed constants, not read from r06. Fix: correct (i) and (ii), plot the final NF including the image-noise term, read the plot band from the cascade output | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | CK-ANA-G7-1, G1-3 | note section 4.2 element table; `make_decks.py` `mc_deck` mode B | Mode B draws the end capacitors around the synthesized 4.87 and 4.38 pF, but section 4.2 specifies 4.7 pF and 4.3 pF parts, so the specified parts are partly outside the drawn range (4.45 to 4.95 pF against 4.62 to 5.12 pF drawn for BPF1); and the +/-0.05 pF board stray on the coupling capacitors is drawn symmetric, though pad and trace stray only adds capacitance. Reviewer: with the specified E-series values the nominal image rejection is 88.5 dB (2.5 dB better) and each section loses 0.1 dB more, so the effect found is benign. Fix: draw mode B around the specified parts and make the stray one-sided (for example 0 to +0.1 pF), or state why not | Open | Pending | |

Three Major findings are open, so the reviewer verdict is NEEDS CHANGES. The physics and arithmetic of the note hold: the filter synthesis, every LTspice filter and mixer number, the Chebyshev hand check, the image definition, the half-IF referral and the Friis cascade all reproduce (sections B5 and C4 below). The headline conclusions survive the review: the TS-012 revision 4 filter (2 + 3) fails REQ-SYS-033 by 19 dB nominal; the TS-012 90 dB and 3 dB criterion cannot be met with coils of Q 100 to 200; BPF3 (2 + 3 + 3) meets 70 dB with the mode B part specification (reviewer minimum 74.6 dB in 20,000 runs); and the analysis does not separate A4 from A5 on the image. The Majors concern what the reported passes rest on: a 200-run minimum for the TS-012 tolerance case (finding-1), unstated 50 ohm ports at the J310 stages (finding-2), and an MDS "PASS" that TPM-005's PDR margin policy does not support (finding-3).

### Per-case results (section F; one row per case the governing texts name)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Image, TS-012 2 + 3, 6 MHz design, IF 8 MHz, Q 100, worst tuning 148.000 MHz | REQ-SYS-033: at least 70 dB | 51.3 dB | -18.7 dB (FAIL) | coil Q, ports | LTspice re-run identical; nodal model 51.3 dB | none |
| C-2 | Same, Q 200; 5 MHz design Q 100 to 200 | REQ-SYS-033: 70 dB | 53.5 dB; 58.0 to 60.8 dB | -16.5 to -9.2 dB (FAIL) | as C-1 | re-run identical; nodal 53.5, 58.0, 60.9 dB | none |
| C-3 | 2 + 3, Monte Carlo mode A / mode B, IF 8 MHz | REQ-SYS-033: 70 dB | minimum 38.7 / 46.2 dB (200 runs) | -31.3 / -23.8 dB (FAIL) | sampling | re-run identical; 20,000 runs: 34.9 / 43.3 dB | none |
| C-4 | TS-012 criterion, 2 + 3 | TS-012 7.3: at least 90 dB and at most 3 dB passband loss | 51.3 dB with 6.32 dB chain loss (Q 100) | -38.7 dB (FAIL) | as C-1 | Chebyshev hand check: lossless 2 + 3 at 132 MHz, 5 MHz design, 20.4 + 41.7 = 62.1 dB; one 5-pole 84.5 dB (note: about 62 and 85 dB) | none |
| C-5 | Image, 2 + 3 + 3, IF 8 MHz, Q 100 / 120 / 200 | REQ-SYS-033: 70 dB | 86.0 / 87.3 / 89.8 dB | +16.0 dB at Q 100 | ports, leak | re-run identical; nodal 86.0 / 87.3 / 89.8 dB | finding-2 |
| C-6 | 2 + 3 + 3, Monte Carlo mode A (TS-012 20 % capacitors) | REQ-SYS-033: 70 dB, every build | minimum 70.6 dB of 200 | +0.6 dB (note: PASS) | sampling scatter not stated | 20,000 runs: minimum 65.6 dB, 0.1 % quantile 68.5 dB, 0.32 % below 70 dB (not met for every build) | finding-1 |
| C-7 | 2 + 3 + 3, Monte Carlo mode B (proposed parts) | REQ-SYS-033: 70 dB, every build | minimum 78.1 dB of 200 | +8.1 dB | sampling, ports | 20,000 runs: minimum 74.6 dB, 0.1 % quantile 77.3 dB (met) | finding-1, finding-2, finding-10 |
| C-8 | 2 + 3 + 3 with J310 port impedances | REQ-SYS-033: 70 dB | not analysed | not shown | not stated | reviewer: 79.2 to 85.8 dB (BPF1 load 56 to 125 ohm, BPF2 and BPF3 source 50 or 200 ohm) | finding-2 |
| C-9 | 2 + 3 + 3, stray 0.003 to 0.1 pF per section, worst phase, nominal | REQ-SYS-033: 70 dB | 85.7 to 78.2 dB | +8.2 dB at 0.1 pF | phase set of two | re-run identical; with mode B and a magnitude-sum phase bound: minimum 69.9 dB | finding-5 |
| C-10 | Alternative: 2 + 3 + 2 at IF 10 MHz, nominal Q 100; mode A / B | REQ-SYS-033: 70 dB | 86.7 dB; minimum 70.6 / 80.5 dB | +16.7; +0.6 / +10.5 dB | sampling | nodal 86.8 dB; 20,000 runs 66.6 / 77.4 dB (mode A 0.04 % below 70 dB) | finding-1 |
| C-11 | IF response: 8 MHz at the antenna | REQ-SYS-033: 70 dB | more than 150 dB (ideal model) | more than +80 dB (filter only; leakage-limited) | layout | re-run identical | none |
| C-12 | Half-IF, A5 ring, -70 dBm at f - 4 MHz, worst tuning (0 dB filter attenuation) | TS-012 7.3 / REQ-SYS-033: at most -140 dBm equivalent | -177 dBm (2 + 3 + 3), -174 dBm (2 + 3) | +37 / +34 dB | model balance, floor | re-run identical; hand: 2 x (-55.5) - 51.8 - 14.5 = -177.3 dBm | finding-8 |
| C-13 | Half-IF, A4 JFET mixer (representative) | as C-12 | -156 dBm (2 + 3 + 3), -152 dBm (2 + 3) | +16 / +12 dB | representative circuit, 8 of 16 cases not converged | re-run identical (same 8 cases fail); hand: 2 x (-55.5) - 30.1 - 14.5 = -155.6 dBm; at 16 dB per J310 -147.6 dBm (+7.6 dB) | finding-8 |
| C-14 | MDS, A5 + BPF3, nominal (Q 120, devices nominal), 146 MHz | REQ-SYS-022: at most -140 dBm; TPM-005 PDR policy at most -142 dBm | -141.2 dBm | +1.2 dB to REQ; -0.8 dB to the TPM-005 policy (Yellow) | several dB (stack case) | independent Friis 5.81 dB, -141.20 dBm | finding-3 |
| C-15 | MDS, A5 + BPF3, filter corner (mode B p95 losses) | REQ-SYS-022; TPM-005 | -139.1 dBm | -0.9 dB (FAIL); TPM-005 Yellow | as C-14 | reproduced from the r03 p95 losses | finding-3 |
| C-16 | MDS, A5 + BPF3, stack (every corner at once) | REQ-SYS-022; TPM-005 | -135.3 dBm | -4.7 dB (FAIL); TPM-005 Red | not statistical (stated) | reproduced | finding-3 |
| C-17 | MDS, A5 + BPF3 with BPF1 into 125 ohm (gfs 8 mS) | REQ-SYS-022 | not analysed | not shown | as C-14 | reviewer -140.6 dBm nominal (+0.6 dB) | finding-2 |
| C-18 | MDS, A5 as TS-012 (2 + 3), A4 (2 + 3 and 2 + 3 + 3), IF 10 alternative | REQ-SYS-022; TPM-005 | nominal -141.2 to -141.5 dBm; filter corner -139.1 to -140.1 dBm | +1.2 to +1.5 dB nominal; -0.9 to +0.1 dB corner | as C-14 | independent Friis 5.84 dB for A5 2 + 3 with the image-noise term (5.33 dB without) | finding-3, finding-9 |
| C-19 | Band edges and centre (144.000 to 148.000 MHz, 50 kHz tuning steps) | REQ-SYS-033, TC-SYS-021 | worst tuning 148.000 MHz in every design | as C-1 to C-10 | none | nodal model over the same 81 tunings | none |
| C-20 | -10 C and +45 C ambient | REQ-SYS-114 with REQ-SYS-022 and 033 | not analysed | not shown | not stated | reviewer estimate: image 87.3 / 85.3 dB, loss +0.12 dB at most | finding-7 |
| C-21 | 2 + 3 + 3 with the specified E-series end capacitors (4.7 pF, 4.3 pF) | REQ-SYS-033: 70 dB | not analysed | not shown | none | reviewer 88.5 dB nominal at Q 100 | finding-10 |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse 7200be7:<path>` | Yes | 76 of 76 equal at `7200be7`, at `HEAD` and in the working tree (shell loop over `git rev-parse` and `git hash-object`) |
| R2 | The checkers run by the commands the README names and exit with the stated result; LTspice through the wrapper | Yes | Clean `git archive 7200be7` export to the scratchpad with the author's `results/` moved aside: `make_decks.py`, `run_sims.py`, `check_bpf.py` r01 to r04, `check_halfif.py`, `cascade.py`, all exit 0 (section C4) |
| R3 | `validate_docs.py` on a JSON product | N/A | No JSON product under a schema |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary in the brief; note sections 1 to 7 and header |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note or README; REQ-SYS-022, 023 and 033 named with their TBR |
| R6 | Every cited render exists | Yes | 11 cited renders present, plus 8 further run renders |

## Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

- **Deck generation.** `make_decks.py` in the export: all 29 decks, both case files and the six `*_draws.npz` byte-identical to the committed ones (`diff -r`).
- **Filter re-run.** All 11 filter decks through `tools/ltspice-batch.sh` (11 wrapper result lines PASS, LTspice exit 0, log first line `LTspice 26.0.2 for MacOS`). `check_bpf.py` on r01 to r04: all four `result.md` byte-identical to the committed files and all four `result.json` equal as parsed JSON; exit 0 each (finding-4).
- **Mixer re-run and cascade.** The ring deck PASS through the wrapper; JFET cases 1, 3, 5, 7, 9, 11, 15 and 16 PASS and cases 2, 4, 6, 8, 10, 12, 13 and 14 FAIL on convergence (time step too small or iteration limit), the same eight the note lists. `check_halfif.py` exit 0, r05 `result.md` byte-identical and `result.json` equal (ring Gc -5.14 dB, IIP2 51.8 to 63.6 dBm and the matched-set bound 67.8 dBm; JFET 30.4 and 30.1 dBm). `cascade.py` exit 0, r06 `result.md` byte-identical and `result.json` equal.
- **Independent filter model (B5).** A nodal (MNA) solver written by the reviewer, with the same element values and parasitics (coil series R at 146 MHz, capacitor Q 500, 5 nH per resonator return), evaluated at the exact tuning and image frequencies rather than interpolated: every nominal image, loss and IF 10 MHz value of r01 and r02 reproduced within 0.1 dB (for example 2 + 3 at Q 100: 1.96 and 4.35 dB, 51.3 and 64.8 dB; 2 + 3 + 3 at Q 100: 86.0 and 107.6 dB; 2 + 3 + 2: 67.8 and 86.8 dB). This also covers the `.ac dec 2000` (0.115 % step) and the linear interpolation in dB (B4).
- **Synthesis by hand.** Chebyshev 0.1 dB, n = 3: g = 1.0316, 1.1474, 1.0316; FBW = 6 / 145.99 = 0.0411; k12 = 0.0378; node C = 1 / (w0^2 x 56 nH) = 21.22 pF; coupling 0.802 pF (deck 0.8018 pF); Qe = 25.1, Rp = 1289 ohm, end C 4.380 pF (deck 4.3796 pF). n = 2: k = 0.0568, coupling 1.204 pF, end C 4.866 pF, shunt 21.22 - 1.204 - 4.635 = 15.38 pF (deck 15.3838 pF). The ground via sits in series with the whole resonator, so it does not move the node's parallel resonance.
- **Chebyshev skirt (the note's "about 62 dB against about 85 dB").** At 132 MHz, 5 MHz design: Omega = 5.89; 2 poles 20.4 dB, 3 poles 41.7 dB (sum 62.1 dB); 5 poles 84.5 dB. Confirmed.
- **Large-sample Monte Carlo (finding-1, finding-5).** The same distributions as `mc_deck`, 20,000 runs per case, seed 7; results in the findings and the C-rows.
- **Port sensitivity (finding-2), temperature (finding-7), E-series parts (finding-10).** Same nodal model, stated in the findings.
- **Cascade (B5).** Independent Friis recomputation: A5 + BPF3 nominal 5.81 dB and -141.20 dBm; A5 2 + 3 5.33 dB without and 5.84 dB with the image-noise term F_J2 / G_before_J2 (the term is correct: the J310's image-band output noise replaces the 290 K image termination that the SSB mixer NF assumes). Ladder loss sensitivity: 12 dB 5.91 dB, 16 dB 6.34 dB.
- **Half-IF physics.** No first-order path exists from a 140 MHz tone to 8 MHz with LO harmonics at n x 136 MHz (|140 - 136 n| never equals 8), so the response is at least second order in RF and the slope-2 extrapolation from the valid points is exact or conservative; the fitted slopes below 2 (1.35 to 1.77 for the ring) are consistent with the -77.8 dBc numerical floor adding to the upper points. The floor itself referred to the antenna (-148 dBm) passes, as the note says.

## Inputs checked against their sources (CK-ANA-A4; every input that sets a reported result)

| Note section 2 row | Source read by the reviewer | Agreement |
|---|---|---|
| REQ-SYS-033, REQ-SYS-022, REQ-SYS-023 text and MDS = -147 dBm + NF | `requirements.json` descriptions and verification notes; -174 + 10 log(500) = -147.0 dBm | Yes; TPM-005 not named (finding-3) |
| Frequency plan: IF 8 MHz, LO 136 to 140 MHz low side, image 128 to 132 MHz, half-IF 140 to 144 MHz | TS-012 7.3; image f - 16 MHz, half-IF (2 RF - 2 LO = IF) at f - 4 MHz | Yes |
| Receiver chain | TS-012 8.1 line "Chain: G5V-2 ..." | Yes |
| Coilcraft 1812SMS-56N: 56 nH, Q typ 125, min 100 at 150 MHz; -82N typ 120, min 100 | Document 184-1 revised 12/02/21 table rows for -56N and -82N | Yes |
| Hand-wound coil Q 100 to 200; about 3 turns 24 AWG, 5.5 mm, Wheeler | labelled estimate | Yes (estimate) |
| Capacitor Q 500 | labelled estimate | Yes (estimate) |
| MMBFJ310 Gpg 16 dB typ at 100 MHz; NF 3.0 dB typ at 450 MHz; gfs 8 to 18 mS | onsemi Rev. 1.5 table: Gpg 16 dB at VDS 10 V, ID 10 mA, 100 MHz; NF 3.0 dB at 450 MHz; gfs 8000 to 18000 umhos at 1 kHz | Yes; the same table gives Re(yig) 12 mmhos at 100 MHz (83 ohm input), not used by the note (finding-2), and Gpg 16 dB against the cascade's 12 dB (finding-8) |
| J310 SPICE model (Linear Systems, standard.jft) | deck `.model J310 NJF(... Mfg=Linear_Systems)` | Yes (representative use only) |
| 1N5711 VF 0.41 V max at 1 mA, 1.00 V at 15 mA, C 2.0 pF max at 0 V | MACOM Rev. V3 table rows | Yes |
| 1N5711 SPICE model | "for example" a community library | Not identified (finding-6) |
| Si5351 duty 45 to 55 %, rise 1 ns typ | search summary (not re-read) | Used only as the ring duty cases, which the re-run reproduces |
| Crystal ladder loss 10.7 dB, 6 poles at 9 MHz, Rs 15 ohm | `cw-selectivity-options.md` F7: "10.2 vs 10.7 dB for 6 poles" | Yes; confidence tag missing (finding-6) |
| Anglian MMIC 22 dB, 0.8 dB NF (lever) | `2m-cw-transceiver-reference-designs.md` F6 | Yes |
| KEMET 0805 C0G USD 0.049 at 10, 0.12 at 1 (cost of BPF3) | TS-012 row E2 | Yes; 7 x 0.049 = 0.34 and 7 x 0.12 = 0.84 USD; the E2 part is a 100 pF J-tolerance value, so the B-tolerance sub-pF price is unread, as the note says |
| Owner approval quote and tinySA status | `docs/plan/status/status-2026-09-28.md` lines 15 and 20 | Yes |

## Checklist answers

### A. Question, scope and traceable inputs

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | No | REQ-SYS-022, 023, 033, TC-SYS-017, TC-SYS-021 and the TS-012 criteria named and exist; TPM-005 and REQ-SYS-114 not named (finding-3, finding-7) |
| CK-ANA-A2 | No | TS-012 revision 4 cited without commit `7d0d450`; no receiver schematic exists and the J310 port interfaces are undefined (finding-6, finding-2) |
| CK-ANA-A3 | No | Every row has a source or "estimate"; F7 lacks its confidence tag; the 1N5711 model is not identified (finding-6) |
| CK-ANA-A4 | Yes | Reviewer table above; disagreements listed |
| CK-ANA-A5 | No | The 50 ohm port assumption and temperature are not stated (finding-2, finding-7); the highest-gain direction is misstated (finding-8) |
| CK-ANA-A6 | Yes | The TS-012 revision 5 change, the replacement criteria and the PCB isolation input go to their owners as requests; the missing J310 port request is part of finding-2 |

### B. Model validity

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Simplifications listed in section 6, but not the 50 ohm ports (finding-2); the coil-loss wording contradicts the deck (finding-9) |
| CK-ANA-B2 | No | J310 model identified; 1N5711 community model not identified by file, version or hash (finding-6); the note limits it to balance use and states its 0.02 V VF excess |
| CK-ANA-B3 | Yes | Chebyshev hand check, nodal pre-check, 1N5711 model checked against the MACOM limits, ring numerical floor characterized at 5, 10 and 20 ps |
| CK-ANA-B4 | Yes | `.ac dec 2000` and `lin 361` confirmed by the reviewer's exact-frequency model within 0.1 dB; ring 10 ps with a measured floor and a 10 dB exclusion rule; JFET non-convergence stated |
| CK-ANA-B5 | Yes | Independent nodal model, synthesis by hand, Chebyshev skirt, Friis (above) |
| CK-ANA-B6 | No | Limitations listed, but no uncertainty set against the mode A minimum, the MDS margin or the image margin (findings 1 to 3) |

### C. Tools, validation status and reproducibility

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | Log first line `LTspice 26.0.2 for MacOS`; venv Python 3.13.5, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2, spicelib 1.6.3, as the note says |
| CK-ANA-C2 | Yes | LTspice accredited (TV-014, ACC-LTSPICE-001, wrapper blob `88b71475`); the Python scripts have no TV record and the note marks the result developer evidence |
| CK-ANA-C3 | Yes | README reproduce sequence `make_decks.py`, `run_sims.py`, the two checkers, `cascade.py`; netlists, one analysis per deck |
| CK-ANA-C4 | Yes | Reviewer re-run identical (above) |
| CK-ANA-C5 | Yes | TV-014 limitations respected: short run directory, lock, time-out, no `.asc` runs, exit and log checks by the wrapper |

### D. Units, arithmetic and consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | dB, dBm, dBc, pF, nH and MHz consistent; MDS and IIP2 conversions recomputed |
| CK-ANA-D2 | No | Note numbers equal the checker output throughout; the section 4.1 per-resonator loss figure, the coil-loss wording and the cascade NF plot disagree (finding-9) |
| CK-ANA-D3 | No | Isolation need 84.48 dB reported as 84 dB (finding-8) |
| CK-ANA-D4 | No | `REQ = 70.0` without its id beside it (finding-4); `REQ_MDS` and `GOAL_MDS` carry theirs |

### E. Results, margins, proposed values and credit

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | REQ-SYS-033, 022, 023 and the TS-012 criteria quoted with their ids |
| CK-ANA-E2 | No | Margins have the right sign; TPM-005 thresholds not compared (finding-3) |
| CK-ANA-E3 | No | Mode A reported as a pass at +0.6 dB on a 200-run minimum (finding-1); REQ-SYS-022 "nominal PASS" at +1.2 dB (finding-3) |
| CK-ANA-E4 | No | Exit 0 on FAIL (finding-4) |
| CK-ANA-E5 | No | REQ-SYS-033 kept at 70 dB with its margin (mode B) but the `tbr.plan` step is not named (finding-6); the requirement file is not edited |
| CK-ANA-E6 | N/A | No TPM current best estimate proposed (the missing comparison is finding-3) |
| CK-ANA-E7 | Yes | Both requirements are Analysis-method; the note claims pre-build developer evidence only, no closing credit (04 section 5.1 item 5) |

### F. Every case named

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Band tunings, image, IF and half-IF covered; REQ-SYS-114 temperature not stated (C-20, finding-7, Minor because the reviewer's bound shows no verdict change) |
| CK-ANA-F2 | N/A | No fault state or hazard is bounded by this analysis |
| CK-ANA-F3 | No | Leakage with tolerances and the highest front-end gain not combined (finding-5, finding-8) |
| CK-ANA-F4 | Yes | Sensitivity to coil Q, capacitor tolerance mode, section count, IF and leakage is shown for the image; MDS levers listed |

### G1. Simulation decks and checkers

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | Decks, scripts and plots under `hardware/sim/rx-frontend/`; run-id folders tie them |
| CK-ANA-G1-2 | Yes | Filter decks `.ac` only, mixer decks `.tran` only; the wrapper's `NC_` check passed |
| CK-ANA-G1-3 | No | 50 ohm ports at the J310 interfaces (finding-2); mode B drawn around synthesized, not specified, parts (finding-10) |
| CK-ANA-G1-4 | Yes | Checkers read the `.raw` through spicelib and the `.log` for steps; `check_halfif.py` treats a missing raw or a "Simulation Failed" log as a missing case; the plot constants of finding-9 (iv) are annotations only |

### G5. Cascades

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G5-1 | Yes | Stage table in r06 `result.md` with every stage in order, each sourced or labelled estimate |
| CK-ANA-G5-2 | Yes | Friis recomputed; image-noise term checked (above) |
| CK-ANA-G5-3 | Yes | Image at IF 8 and 10 MHz, half-IF, IF response, every tuning |

### G7. Worst-case and tolerance

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | No | Monte Carlo seed, count and distributions stated, but the 200-run minimum is used as a worst case (finding-1); mode B centre values and stray sign (finding-10) |
| CK-ANA-G7-2 | No | Initial tolerances and a residual alignment error used; temperature coefficients not included (finding-7); ageing N/A |

### H. Hazards, risks and records

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | N/A | No hazard is bounded by the receive filter analysis |
| CK-ANA-H2 | No | The TS-012 7.1 receiver risks are re-quantified but not sent to the risk writer (finding-6) |
| CK-ANA-H3 | No | "Revision 1" with no change history (finding-6) |

### I. Visual closure

| Item | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | The reviewer opened all 11 cited renders and the 8 other run renders (19) with the Read tool |
| CK-ANA-I2 | No | Axes, units, limit lines with ids, legends and case titles present on all; the cascade NF curves stop short of the stated NF for the two-section chains (finding-9). Plotted values agree with the checker at the marked points (for example 51.3 dB at 148 MHz in r01, 86.0 dB in r02, the mode B histogram minimum near 78 dB, the leakage 78.2 dB end point, ring IIP2 bars 51.8 to 63.6 dBm) |

**ITEMS N/A:** CK-ANA-E6, CK-ANA-F2, CK-ANA-H1, CK-ANA-G2 to G4, CK-ANA-G6 (analysis_kind is simulation-deck, cascade and worst-case), CK-ANA-J1 to J3 (criticality neither).

## Cross items (returned to Claude as lead SE)

- **X-1. The recommendation stands on mode B.** With findings 1 and 2 answered, BPF3 is still the cheaper fix: with the mode B part specification the reviewer's 20,000-run minimum is 74.6 dB. The owner decision of note section 7 item 1 should carry the mode B tolerances (B on the 0.8 and 1.2 pF parts, C on the ends) as part of the change, not only as an ordering-gate check, since with 20 % parts about 1 build in 300 misses 70 dB.
- **X-2. PDR readiness.** Finding-3 is a reporting fix, but its substance (TPM-005 Yellow at nominal and at the filter corner for every line-up analysed) is a PDR TPM status the owner should see with the TS-012 decision.

## Commands

- Search: `mcp__claude-context__search_code` path `/Users/robinonsay/rust/cwht`, query "next free INSP id peer-review record analysis TS-012 INSP-114".
- Freeze and blobs: shell loop over `git rev-parse 7200be7:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (76 files); `cmp` of the run script copies.
- Re-run: `git archive 7200be7 tools hardware/sim/rx-frontend docs/design/analysis/rx-bpf-ts012.md | tar -x -C <scratchpad>/rerun`; author results moved to `results_author`; `.venv/bin/python hardware/sim/rx-frontend/make_decks.py`; `run_sims.py` (all runs through the wrapper); `check_bpf.py results/<run>` for r01 to r04; `check_halfif.py results/2026-09-28-r05-halfif-mixers`; `cascade.py`; JSON and Markdown comparisons in Python.
- Independent models: `<scratchpad>/rev/nodal.py`, `validate.py`, `mc.py` (20,000 runs, seed 7), `term.py`, `temp.py`, `extra.py` (scratchpad only, not committed).
- Datasheets: `pdftotext -layout` on the fetched PDFs.
- Record check: `tools/validate_docs.py --root <scratchpad>/vroot` on an export of `HEAD` with this record added (the harness refused the reviewer's write into the repository).

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/rx-bpf-ts012.md@5c60b967, hardware/sim/rx-frontend/ scripts, decks and results as in product_files, at 7200be7
FINDINGS:
- [Major] CK-ANA-E3, G7-1, B6, D2 finding-1: mode A reported as a pass on a 200-run minimum (70.6 dB); 20,000 runs give 65.6 dB minimum and 0.32 % of builds below 70 dB (2 + 3 + 3), 66.6 dB for 2 + 3 + 2 at IF 10; mode B holds (74.6 dB).
- [Major] CK-ANA-G1-3, B1, A5, A6 finding-2: every section between 50 ohm ports; J310 GG input is 56 to 125 ohm (83 typical) and the drain interface is undefined; BPF1 at 125 ohm costs 0.6 dB NF, a 200 ohm drive costs up to 7 dB of image rejection; not stated as a design input.
- [Major] CK-ANA-E3, E2, A1 finding-3: REQ-SYS-022 reported nominal PASS at +1.2 dB against a several-dB spread; TPM-005 not named; its PDR margin policy (-142 dBm) is missed by every configuration (Yellow nominal and filter corner, Red stack).
- [Minor] CK-ANA-E4, D4 finding-4: checkers exit 0 on FAIL; REQ constant without id.
- [Minor] CK-ANA-F3 finding-5: leakage tolerance nominal only; with mode B the 0.1 pF case reaches 69.9 dB.
- [Minor] CK-ANA-A2, A3, B2, E5, H2, H3 finding-6: TS-012 commit, F7 confidence tag and Rs bound, 1N5711 model identity, tbr.plan step, risk request, change history.
- [Minor] CK-ANA-F1, A5, G7-2 finding-7: REQ-SYS-114 not stated; reviewer bound 85.3 to 87.3 dB, no verdict change.
- [Minor] CK-ANA-F3, A5, D3 finding-8: highest J310 gain (16 dB typ) not analysed; isolation need about 92.5 dB, not 84; 84.48 rounded down.
- [Minor] CK-ANA-D2, I2, B1 finding-9: per-resonator loss figure, coil-loss wording, cascade NF plot without the image-noise term, typed plot band.
- [Minor] CK-ANA-G7-1, G1-3 finding-10: mode B drawn around synthesized, not specified, end capacitors; symmetric stray.
ITEMS N/A: CK-ANA-E6, F2, H1, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), CK-ANA-J1 to J3 (criticality neither)
VALUES PROPOSED: REQ-SYS-033: 70 dB (supported with the mode B part specification as a condition of BPF3; not supported with the TS-012 20 % capacitors, finding-1)
MEASUREMENTS: size=29 decks, 6 runs, 21 cases; inputs_checked=14 rows (every input that sets a reported result); renders=19; turns=60; minutes=110; major=3; minor=7
```

## Iteration 2: delta verification of finding-1, finding-2 and finding-3 (Major) (2026-09-28, HEAD `c5ccea8`)

**Scope (rule C1).** A delta that verifies the fixes of the three Major findings, checks the two Minor fixes the author also made, and scans every changed text, script, deck and result of revision 2 for defects the revision introduced. The revision 1 runs r01 to r06 are unchanged and were not re-reviewed beyond the plots the note still cites and the r01 and r04 checker exit statuses. Product: the 59 blobs of `product_files` at `d2d89e9`; `git log d2d89e9..HEAD` is one commit (`c5ccea8`, the LPF review record only).

**Independence (rule C4).** This invocation authored no part of the note, its revisions, the decks, the scripts, the results or TS-012, and edited no product file. It changed only this record.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before every manual search (queries: "rx-bpf analysis review checklist iteration 1 findings receiver bandpass filter TS-012"; "rule C1 review verdict APPROVED NEEDS CHANGES open Major findings"; "rx-bpf review iteration 1 finding mode A 200-run minimum 0.32 % 65.6 dB J310 port impedance"). `grep` then only pinned lines in known files (the note, TS-012, `tools/validate_docs.py`, the README, the block scripts). The rustos tree was not read.

**Sources re-read by the reviewer (2026-09-28, public vendor PDFs through the web-fetch tool, text extracted with `pdftotext -layout`).**
- onsemi (Fairchild) MMBFJ309 / MMBFJ310 Rev. 1.5, https://www.onsemi.com/pdf/datasheet/mmbfj310-d.pdf, Electrical Characteristics: gfs "MMBFJ310 8000 ... 18000" umhos at VDS 10 V, ID 10 mA, 1.0 kHz; Re(yig) 12 mmhos typ at 100 MHz; Csg 4.1 typ, 5.0 max pF and Cdg 2.0 typ, 2.5 max pF at VDS 0, VGS -10 V, 1.0 MHz; gog 150 umhos; Gpg 16 dB at 100 MHz; NF 3.0 dB at 450 MHz. Every value in note section 2 and in `worst_case.py` `J310_IN` and `J310_DR` agrees.
- Coilcraft Document 184-1, revised 12/02/21, https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf: 1812SMS-56N 56 nH, Q typ 125, min 100 at 150 MHz; -82N typ 120, min 100. Agrees with note section 2.
- Requirement and case texts from `docs/requirements/sys/requirements.json` (REQ-SYS-022, 023, 033), `docs/test_cases/sys/test_cases.json` (TC-SYS-017, TC-SYS-021) and `docs/plan/tpm.json` (TPM-005 and `conventions`), and TS-012 revision 4 section 7.3 (`7d0d450`, lines 403 and 404). The note quotes each correctly (details under E1).

### Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

**Reproduction (CK-ANA-C4, readiness R2).** Clean `git archive d2d89e9 hardware/sim/rx-frontend tools` in the scratchpad (`rxbpf_iter2/`), with the committed results and decks copied aside for comparison. Then, with the repo venv and from the export root: `validate_nodal.py` (exit 0, ACCEPTED, 1,189,624 points, largest difference 2.55e-3 dB, `result.md` identical); `worst_case.py prepare r08`, `run_sims.py 2026-09-28-r08-bpf-tolerance-corners`, `worst_case.py check r08` (each exit 0); the same three for r09 and r10 (each exit 0); `cascade.py` (exit 1, "Checker exit status: 1", as the README states). LTspice ran only through `tools/ltspice-batch.sh` (blob `88b71475`), with `CWHT_LTSPICE_LOCK_WAIT=5400` because other sessions held the LTspice lock (the reviewer's first attempt was stopped while it waited for the lock, before any deck ran). 13 wrapper lines "result: PASS ... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0" (7 decks in r08, 3 in r09, 3 in r10); every `.log` first line reads "LTspice 26.0.2 for MacOS"; no warning string in any log.

Against the committed outputs: every regenerated deck and case file is byte-identical (62 of 62 files in `decks/`); r09 11 of 11, r10 10 of 10 and r11 4 of 4 files identical (JSON to 1e-9, PNG pixel arrays equal, Markdown byte for byte); r08 38 of 40 identical, and the other two (`prepare.json`, `result.json`) differ only in the `role` of 2 + 3 + 4 ("proposed" committed, "lever" from the frozen script; no number or verdict changes; finding-9 (c)). LTspice against the numpy prediction: r08 20 corner cases, largest difference 4.2e-4 dB; r09 42 cases, 4.2e-4 dB; r10 15 cases, 4.5e-4 dB (limit 0.01 dB). The three 1,000-step LTspice Monte Carlo decks are compared with numpy on their first 200 steps only (4.6e-4 dB; finding-9 (d)).

**Independent checks (reviewer scripts in the scratchpad `rxbpf_iter2/rev_checks/`, not product).**
- **ABCD cascade of the synthesized sections** (a series and shunt two-port method written by the reviewer from `bpf_design.synth`, not the nodal solver): nominal 2 + 3 + 3 at Q 100, IF 8, worst image rejection 86.04 dB at 148.0 MHz (note 86.0); 2 + 3 51.28 dB (note 51.3); BPF1 worst in-band loss 1.70 dB at Q 120 and 1.96 dB at Q 100 (note 1.70 / 1.96); BPF2 3.76 dB at Q 120 (note 3.76); BPF1 into 125 ohm at Q 100 2.54 dB (note 2.54, +0.58 dB).
- **Friis cascade by hand** of A5 2 + 3 + 3 with the r11 stage values: NF 5.81 / 9.04 / 13.29 dB, MDS -141.2 / -137.97 / -133.72 dBm (nominal, filter corner, stack), equal to r11. kTB in 500 Hz -147.01 dBm.
- **Binomial bounds:** 1 - 0.05^(1/200) = 1.49 %, 1 - 0.05^(1/20000) = 0.0150 %, 1 - 0.05^(1/1000) = 0.30 %; Clopper-Pearson 65 of 20,000: 0.251 to 0.414 %; 4 of 1,000: 0.109 to 1.02 %; 13 of 20,000: 0.035 to 0.111 %. All equal the note. N for 0.1 % with zero failures is 2,995 (ln 0.05 / ln 0.999 = 2994.2), not 2,996 (finding-9).
- **Leak arithmetic (section 4.4):** a worst-phase leak added to a filtered image response 0.2 dB inside the limit keeps 70 dB when it is 32.7 dB below that response (20 log(1 / (10^(0.2/20) - 1)) = 32.7); 9.5 dB for a 2.5 dB margin; up to 6.8 dB above for 10.1 dB. Isolation: 70.2 + 32.7 + 14.5 = 117.4 dB; 72.5 + 9.5 + 16.5 = 98.5 dB; 80.1 - 6.8 + 12.1 = 85.4 dB. All equal the note.
- **Design-input corner against the re-alignment residual** (`check_residual_parts.py`, `check_residual_alt.py`: the frozen `worst_case.chain_corner` with mode B, aligned at 50 ohm, every internal port within VSWR 1.2, 0.03 pF stray per section with the worst-phase bound; numpy search, not re-simulated in LTspice). 2 + 3 + 3 at IF 8: 70.19 dB at +/-0.3 % (the note's 70.2), 70.02 at +/-0.32 %, 69.76 at +/-0.35 %, 69.31 at +/-0.4 %, 68.40 at +/-0.5 %, 65.96 at +/-0.75 %. VSWR 1.2 without stray: 72.07 at +/-0.3 %, 67.56 at +/-0.75 %. 2 + 3 + 4: 80.06 / 77.38 / 73.64 dB at +/-0.3 / 0.5 / 0.75 %. 2 + 3 + 2 at IF 10: 72.48 / 71.23 / 69.53 dB. Basis of finding-6.
- **Stocked end-capacitor values.** The note builds the 4.87 pF and 4.38 pF end capacitors from 4.7 pF and 4.3 pF parts (section 4.2 element table) while the tolerance box is centred on the synthesized value. With the box re-centred on the part value (+/-0.25 pF around 4.7 and 4.3 pF), the 2 + 3 + 3 mode B corner aligned at 50 ohm is 76.42 dB (note 75.6), the design-input corner 70.98 dB (note 70.2) and the 50 ohm loss corner 2.48, 6.18, 6.18 dB (r08: 2.57, 6.24, 6.24). The stocked values do not worsen any verdict; no finding.

### Verification of finding-1 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `d2d89e9` | Result |
|---|---|---|---|
| finding-1 | (i) mode A reported as a pass on a 200-run sample minimum | Withdrawn in sections 0, 4.2 finding 1, 5 and the README r03 row; r01 and r03 `result.md` now read "Sample verdict ... A sample minimum is not a worst case" with the 1 - 0.05^(1/N) bound (`check_bpf.py` `mc_word`). r08: mode A without re-alignment, corner 49.09 dB, 65 of 20,000 below 70 dB (0.325 %, 0.251 to 0.414 %); the LTspice 1,000-run sample has 4 below (0.11 to 1.0 %). The review's 0.32 % is reproduced with another seed | Yes |
| finding-1 | (ii) no worst-case corner (TC-SYS-021 step 4) | `tolerance.py` vertex search per section and tuned frequency (32 to 512 vertices); chain corner as the sum of the independent section minima per tuned frequency, then the minimum over 144.0 to 148.0 MHz at 100 kHz (TC-SYS-021 spacing). Method check: a build fails when any tuned frequency fails, so the worst build is the minimum over f of the sum of per-section minima at f; `chain_corner` computes exactly that. L-BFGS-B polish from the worst vertex and six random interior points: `corner_polished_db` equals `corner_db` to 1e-3 dB in all 16 cases of `result.json`. Every corner re-simulated in LTspice from a deck carrying the corner values; agreement within 4.2e-4 dB (re-run above) | Yes |
| finding-1 | (iii) Monte Carlo acceptance with N and a confidence bound | Section 3 item 6 fixes the acceptance before the runs: the worst-case corner is the acceptance; a Monte Carlo is a yield estimate with 1 - 0.05^(1/N) (zero failures) or Clopper-Pearson (k failures). Arithmetic re-checked above (one Minor slip, finding-9) | Yes |
| finding-1 | Consequence: a tolerance condition for the build | Mode B tolerances and re-alignment made conditions of BPF1, BPF2 and BPF3 (section 5 conditions 1 and 2). The residual limit that revision 2 attaches to condition 2 is inconsistent with the design-input corner: new finding-6 | Yes; see finding-6 |

**Result: finding-1 Verified.**

### Verification of finding-2 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `d2d89e9` | Result |
|---|---|---|---|
| finding-2 | 50 ohm ports stated as a design input | Section 2 paragraph "Design input stated from revision 2", section 4.3 finding 3 and section 5 condition 3: every internal port (both J310 inputs, both drains, the ring RF port) within VSWR 1.2 of 50 ohm over 144 to 148 MHz; the antenna port stays 50 ohm as the REQ-SYS-033 reference. The VSWR sweep (r09) sets the tolerance: 72.1 dB at VSWR 1.2, 69.6 dB at 1.35 (worst of 8 phases around each circle) | Yes |
| finding-2 | MMBFJ310 port impedances from the datasheet | Values re-read (above) and equal. Input 1/gfs 56 to 125 ohm (83 ohm from Re(yig) typ), Csg up to 5 pF; drain port 50 to 200 ohm with Cdg up to 2.5 pF, labelled an estimate because TS-012 does not define it. Observation O-1 on the bias condition. The r09 table in the note equals `result.md` row by row (24 rows for 2 + 3 + 3); 14 named cases per configuration re-simulated in LTspice | Yes |
| finding-2 | BPF1 into the J310 input carried into the cascade | r09: +0.58 dB at Q 100 (1.96 to 2.54 dB), +0.63 dB at Q 120; reviewer ABCD 2.54 dB. The r11 "J310 port" case uses 2.33 dB at Q 120: MDS -140.6 dBm for A5 2 + 3 + 3 | Yes |
| finding-2 | Physics of the port model | Shunt R and C at each port; the transducer gain \|Vout\|^2 RS / RL for a 2 V source holds with a shunt C (it draws no power). The VSWR circle is mapped to an admittance at f0 and held as R and C (a negative C where the circle is inductive), so its frequency dependence at the image is that of a capacitor; the error is small 12 to 20 MHz from f0 and is shared by the LTspice decks, which accept a negative C in `.ac` | Yes |

**Result: finding-2 Verified.**

### Verification of finding-3 (Major), case by case (rule C7)

| Finding | Case the finding named | Check at `d2d89e9` | Result |
|---|---|---|---|
| finding-3 | TPM-005 named and compared with its thresholds | Section 2 input row, section 4.6 table and section 8 quote `tpm.json` TPM-005: planned -140 dBm; PDR margin policy -142 dBm or better; Yellow no more than 3 dB worse than -140 dBm; Red more than 3 dB worse. `cascade.py` `tpm005()`: Green at -142 or better, Yellow to -137, Red worse than -137, which is right. A4 2 + 3 stack -136.95 dBm is Red (worse than -137), as reported | Yes |
| finding-3 | REQ-SYS-022 at the TC-SYS-017 corner, not nominal | Revision 1's "nominal PASS" withdrawn (section 4.6 finding 1, section 5). Filter corner from the mode B vertex box at Q 100 with every internal port within VSWR 1.2 (`cascade.section_losses`): 2.83, 6.72, 6.72 dB; MDS -138.0 dBm for A5 2 + 3 + 3; stack -133.7 dBm. Every configuration fails the corner. The label "TC-SYS-017 corner" for the case that holds the devices nominal is finding-7 (Minor); the conclusion does not change | Yes |
| finding-3 | Status report for the TPM owner and the risk writer | Section 8: previous status (no history), new status Yellow on the CBE and Red at the stack, CBE with evidence path, cause, proposed response, proposed risk with likelihood 4, consequence 4 and a trigger; the author does not edit `tpm.json` or the register (08 section 3.4, PDR work plan section 5.3) | Yes |

**Result: finding-3 Verified.**

### Minor findings of iteration 1 (the author fixed both)

- **finding-4 Verified.** Reviewer runs: `check_bpf.py` exits 1 on r01 (FAIL verdicts), 0 on r04 and 2 with no argument; `validate_nodal.py` exits 0 (accepted); `worst_case.py check` returns non-zero when the proposed configuration fails (`prop_ok and ok_all`) and exited 0 for r08 to r10; `cascade.py` exits 1 (REQ-SYS-022 fails at the corner). Constants carry their ids: `REQ_SYS_033_DB` and `REQ = 70.0` (REQ-SYS-033), `REQ_MDS`, `GOAL_MDS`, `TPM005_PDR`, `TPM005_RED`.
- **finding-5 Verified.** r10: 16 phases, worst taken separately at the tuned and at the image frequency (a bound), at nominal, at the mode B corner and at the design-input corner; 0.1 pF gives 69.9 dB at the mode B corner and 66.4 dB at the design-input corner; the revision 1 statement is withdrawn in section 4.4. The README r04 row still carries the old claim (finding-9).

### New findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-6"></a>finding-6 | reviewer | Major | CK-ANA-E3, D2, F4, B6 | note section 4.2 finding 3 (line 187), section 5 condition 2 (line 353) and verdict table (line 341), section 0 (line 14); `corner_vs_residual.png`; the author's return ("residual at most +/-0.75 %") | The re-alignment residual limit that revision 2 states for the build is not the one its own design-input corner needs, and the 2 + 3 + 3 image PASS rests on a margin smaller than the uncertainty of that residual. Section 4.2 finding 3 says the residual "must be at most +/-0.75 % (71.3 dB)"; that figure is the mode B corner with 50 ohm ports and no stray. At the design-input corner that section 5 relies on (VSWR 1.2 ports and 0.03 pF), the reviewer's run of the frozen `chain_corner` gives 70.19 dB at +/-0.3 %, 70.02 dB at +/-0.32 %, 68.40 dB at +/-0.5 % and 65.96 dB at +/-0.75 %: the stated limit fails by 4.0 dB, and the limit that holds 70 dB is about +/-0.32 %. The same holds for the alternative 2 + 3 + 2 at IF 10 (69.53 dB at +/-0.75 %); 2 + 3 + 4 keeps 73.64 dB. The +/-0.3 % residual is itself an estimate with no procedure yet (section 7 item 3), and the corner moves about 0.9 dB per 0.1 % there, so the 0.2 dB margin lies inside the uncertainty of an input the note labels an estimate, yet section 5 reports the case as "PASS by 0.2 dB". The note does say the 0.2 dB leaves no room for the board leak and that 2 + 3 + 3 is "not a robust basis", but it neither states the margin against this uncertainty nor gives the residual the build must meet. Fix: state the residual limit at the design-input corner (about +/-0.32 %, or re-derive it) in sections 4.2, 5 and 7 item 3 and in the README; show the residual sensitivity at the design-input corner (not only with 50 ohm ports); correct the return to the orchestrator; report 2 + 3 + 3 image as not shown with margin (not PASS) unless the alignment procedure demonstrates a residual with margin to that limit | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-F3, E2 | note sections 0, 3 item 11, 4.6 table and finding 1, 5 table, 8; `cascade.py` `CASES` | TC-SYS-017 procedure step 4 repeats the computation "with every toleranced input at its worst-case corner". The note calls the case with the filter at its corner and every device nominal "the TC-SYS-017 corner" (-138.0 dBm, 2.0 dB short for A5 2 + 3 + 3) and reports the case with every input at its corner separately as the "stack" (-133.7 dBm, 6.3 dB short). As TC-SYS-017 is written, the stack is its worst case. REQ-SYS-022 fails either way, but the shortfall quoted to the owner and the proposed risk trigger ("worse than -140 dBm at the TC-SYS-017 corner") would let a redesign pass with the device corners left out. Fix: name the stack as the TC-SYS-017 worst case, or state why the device corners (estimates) are excluded and carry that exclusion into the risk trigger | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-I2 | r11 `cascade_verdicts.png` y label; r11 `cascade_nf_gain.png` panels "A5 as TS-012 rev 4" and "A4 as TS-012 rev 4"; r09 `bpf1_loss_vs_j310_input.png` | (a) The MDS axis is inverted (-127 at the bottom, -145 at the top) and its label says "lower bar end = more sensitive"; on the plot a bar that ends lower is less sensitive (the Red bars reach down to -129.4 dBm). (b) In the two 2-section panels the cumulative NF curves end at 5.33 / 7.25 / 9.66 dB (A5) and 5.19 / 7.01 / 9.10 dB (A4), while the checker's NF, used in the panel titles, is 5.84 / 8.05 / 10.52 and 5.71 / 7.86 / 10.06 dB: the image-noise term (0.51 to 0.96 dB) is added after the running cascade and not drawn. (c) The BPF1 loss plot draws "proposed BPF1 limit 2.5 dB (rev 1 section 5)", a revision 1 criterion that revision 2 replaces with the cascade judgement (section 5, TS-012 criterion replacement) and that carries no requirement id. Fix: correct the label, draw the image-noise term as a final point or state it on the panel, and drop or relabel the 2.5 dB line | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-D2, D3 | `README.md` runs table, r04 row; note section 3 item 6 (line 71) and `worst_case.py` docstring (line 25); r08 `prepare.json` and `result.json`; note section 4.2 (line 148) | (a) The README r04 row still reads "Worst case 78.2 dB at 0.1 pF per section (PASS 70 dB)", the revision 1 claim at nominal that note section 4.4 finding 1 withdraws (0.1 pF gives 69.9 dB at the mode B corner and 66.4 dB at the design-input corner). (b) N for a 0.1 % bound with zero failures is 2,995 (ln 0.05 / ln 0.999 = 2994.2), not 2,996. (c) The committed r08 `prepare.json` and `result.json` give 2 + 3 + 4 the role "proposed"; the frozen `worst_case.py` gives it "lever", so these two files came from an earlier script version (the reviewer's re-run with the frozen script differs only there); the r08 to r10 run folders also keep older copies of `cascade.py` and `validate_nodal.py` than the frozen ones. (d) "The numpy solver reproduces the same draws to 4.6e-4 dB" (section 4.2): `check_r08` compares only the first 200 of the 1,000 steps of each LTspice Monte Carlo deck. None changes a number or a verdict. Fix: qualify the r04 row and point it to r10; correct the N; re-run r08 with the frozen script (or re-freeze) so the committed JSON matches it; say "first 200 draws" or compare all 1,000 | Open | Pending | |

### Observations (no finding)

- **O-1.** The J310 port values come from datasheet rows at VDS 10 V, ID 10 mA (gfs at 1 kHz; Csg and Cdg at VDS 0, VGS -10 V), while the cascade notes derate the stage for the 5 V rail. At a lower drain current gfs falls and the grounded-gate input resistance rises above 125 ohm, so the bare-port cases of r09 are, if anything, optimistic; their conclusion (bare ports fail, matching networks needed) holds. The VSWR 1.2 design input does not depend on these values.
- **O-2.** `validate_nodal.py` (r07) exercises the solver on 50 ohm ports and real leak phases only. The paths that revision 2 uses for non-50 ohm ports, shunt port capacitance and complex leak phases are checked by the r09 and r10 LTspice re-simulations of named cases (agreement within 4.5e-4 dB), not by r07. The 16-phase grid of the leak bound can miss the worst phase by up to 11.25 degrees (about 2 % in leak amplitude, a few hundredths of a dB here); small against every margin except the 0.2 dB of finding-6.
- **O-3.** The iteration 1 record was never filed. Section 9 of the note is the only copy of the iteration 1 findings, and its rows are the author's summaries. This record now carries them; the lead SE may wish to note the gap in the lessons-learned record.
- **O-4.** The alignment model retunes every coil against its own node with the neighbours shorted, at 50 ohm, and treats the residual of each resonator as independent. The worst corner puts every coil at +0.3 % together (section 6 says so). A procedure that also measures the passband centre of each section (section 7 item 3 asks for it) bounds that common-mode case; finding-6 asks for its limit.

### Per-case results (iteration 2; section F, one row per case the governing texts name)

Values are the checker's (all rest on estimates for coil Q, capacitor Q, residual and device values), from the committed `result.json` files, which the reviewer's re-run reproduced.

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Image, 2 + 3 at IF 8 (TS-012 revision 4), 144.0 to 148.0 MHz at 100 kHz, nominal Q 100 and mode B aligned corner | REQ-SYS-033 / TC-SYS-021: at least 70 dB, nominal and at the corners | 51.3 dB nominal, 45.0 dB corner: FAIL | -18.7 dB, -25.0 dB | coil Q, residual | ABCD 51.28 dB; re-run identical | none |
| C-2 | Image, 2 + 3 + 3 at IF 8, mode A without re-alignment (TS-012 20 % capacitors) | REQ-SYS-033 corner | corner 49.1 dB; 0.32 % of 20,000 below 70 dB: FAIL | -20.9 dB | as C-1 | re-run identical | none |
| C-3 | Image, 2 + 3 + 3 at IF 8, mode B aligned at 50 ohm, 50 ohm ports | REQ-SYS-033 corner | 75.6 dB: PASS | +5.6 dB | residual (about 0.9 dB per 0.1 %) | re-run identical | none |
| C-4 | Image, 2 + 3 + 3, design-input corner (mode B, aligned, VSWR 1.2, 0.03 pF, worst-phase bound) | REQ-SYS-033 corner | 70.2 dB: reported PASS | +0.2 dB | residual: -1.8 dB at +/-0.5 %, -4.2 dB at +/-0.75 % | reviewer 70.19 dB; 65.96 dB at the stated +/-0.75 % limit | finding-6 |
| C-5 | Image, 2 + 3 + 3 with bare J310 ports (125 ohm input, 200 ohm drain), mode B aligned at 50 ohm / in circuit | REQ-SYS-033 corner | 68.0 / 61.3 dB: FAIL | -2.0 / -8.7 dB | drain port an estimate | re-run identical | none |
| C-6 | Image, 2 + 3 + 4 at IF 8, design-input corner | REQ-SYS-033 corner | 80.1 dB: PASS | +10.1 dB | residual: 73.6 dB at +/-0.75 % | reviewer 80.06 dB | none |
| C-7 | Image, 2 + 3 + 2 at IF 10, design-input corner | REQ-SYS-033 corner | 72.5 dB: PASS | +2.5 dB | residual: 69.5 dB at +/-0.75 % | reviewer 72.48 dB | finding-6 |
| C-8 | Whole-chain antenna-to-mixer leak at the image | REQ-SYS-033 (the leak adds to the filtered path) | isolation needed 117 / 85 / 98 dB (2+3+3 / 2+3+4 / 2+3+2); not analysed | not shown | layout | arithmetic re-checked | finding-6 |
| C-9 | IF-frequency response (8 MHz at the antenna) | REQ-SYS-033 | more than 150 dB (ideal filter model); the physical limit is the leak of C-8 | not shown beyond the model | layout | not re-checked (r01 to r04 unchanged) | none |
| C-10 | Half-IF, -70 dBm at RF - 4 MHz, worst tuning, A5 ring and A4 JFET | TS-012 section 7.3 (no higher than the -140 dBm wanted response) | A5 -177 / A4 -156 dBm equivalent (2 + 3 + 3): PASS | +37 / +16 dB | IIP2 extrapolation; JFET partial convergence | r11 referral reproduced by the re-run | none |
| C-11 | MDS, A5 2 + 3 + 3: nominal / J310 port / filter corner / stack, worst tuned frequency (covers 144.05, 146.00, 147.95 MHz) | REQ-SYS-022: at most -140 dBm; REQ-SYS-023: at most -142 dBm (Goal) | -141.2 / -140.6 / -138.0 / -133.7 dBm | REQ-SYS-022 +1.2 / +0.6 / -2.0 / -6.3 dB; REQ-SYS-023 -0.8 dB nominal | every device value an estimate | hand Friis equal | finding-7 |
| C-12 | MDS, A4 2 + 3 + 3, same cases | REQ-SYS-022, 023 | -141.5 / -140.9 / -138.7 / -135.0 dBm | +1.5 / +0.9 / -1.3 / -5.0 dB | JFET mixer (Low) | re-run identical | finding-7 |
| C-13 | TPM-005 current best estimate at PDR | TPM-005 margin policy: -142 dBm or better; Red worse than -137 dBm | CBE -141.2 dBm (A5), -141.5 dBm (A4): Yellow; stack Red | -0.8 dB (A5) to the policy | as C-11 | thresholds re-read | none |
| C-14 | TS-012 criterion: at least 90 dB at 128 to 132 MHz with at most 3 dB passband loss | TS-012 revision 4 section 7.3 | unattainable (section 4.1); replacement proposed | n/a | n/a | unchanged from revision 1 | none |

### Checklist answers (iteration 2, delta)

**A. Question, scope and traceable inputs.** A1 Yes: REQ-SYS-022, 023, 033, TC-SYS-017, 021 and TPM-005 (MOP-006) named and present. A2 Yes: TS-012 revision 4 (`7d0d450`) sections 7.3 and 8.1 are the design data; no schematic exists (stated). A3 Yes: the new inputs (J310 rows, TPM-005 thresholds, TC-SYS-017 and 021 acceptance) are sourced; the drain port range and the residual are labelled estimates. A4 Yes: every datasheet input re-read (above); every requirement and TPM quote equal. A5 Yes, with finding-6 on the residual bound; the direction of every other assumption is stated in section 6. A6 Yes: the design inputs and the risk are requests to the J310 stage design, the layout, the TPM owner and the risk writer; no requirement is edited.

**B. Model validity.** B1 Yes: ports, alignment and the leak bound stated with their effects (O-4). B2 Yes: only standard LTspice elements in r07 to r10; the J310 datasheet validity is O-1. B3 Yes: r07 (1,224 steps, 2.5e-3 dB) and the LTspice re-simulation of every named numpy case. B4 Yes: 100 kHz tuned grid (TC-SYS-021), explicit `.ac` frequency lists mapped point by point, vertex search with interior polish. B5 Yes: reviewer ABCD and Friis checks and the design-input residual runs (above). B6 No: the 0.2 dB design-input margin is not set against the residual uncertainty (finding-6).

**C. Tools.** C1 Yes: every `.log` first line reads "LTspice 26.0.2 for MacOS" (re-run); Python versions as the lock. C2 Yes: developer evidence stated in the note header. C3 Yes: the README gives the command sequence. C4 Yes: re-run above. C5 Yes: the wrapper's path-length, lock and time-out behaviours respected (`run_sims.py` time-outs 240 and 600 s).

**D. Units, arithmetic, consistency.** D1 Yes. D2 No: finding-6 (residual limit), finding-9 (README r04 row, r08 JSON provenance, the 200-draw comparison). D3 No: finding-9 (N = 2,995). D4 Yes (finding-4 Verified).

**E. Results, margins, credit.** E1 Yes: REQ-SYS-033 "reject image and intermediate-frequency responses by at least 70 dB (TBR) relative to the in-band response"; REQ-SYS-022 "at most -140 dBm (TBR) in a 500 Hz bandwidth"; TC-SYS-021 "nominal and at the corners"; TC-SYS-017 worst case "over the three frequencies and all tolerance corners"; TPM-005 margin policy and thresholds as quoted. E2 Yes, with finding-7 on which case is the TC-SYS-017 worst case. E3 No: finding-6. E4 Yes. E5 N/A: no TBR value proposed. E6 Yes: section 8 names TPM-005, the value and the evidence path and leaves `tpm.json` to its owner (no credit claimed). E7 Yes: pre-build analysis on preliminary data, no closing credit claimed.

**F. Every case named.** F1 Yes: the per-case table has a row for each case the governing texts name (TC-SYS-021 tuned grid and corners; TC-SYS-017 three frequencies, covered by the band-worst loss, and corners; TPM-005; the TS-012 criteria). F2 N/A (no hazard bounded). F3 No: finding-7. F4 No: finding-6 (the sensitivity at the design-input corner is not shown).

**G1.** G1-1 Yes. G1-2 Yes: each deck runs one `.ac`; the wrapper's NC_ check passed. G1-3 Yes: ports as the design input; the stocked end capacitors checked (no effect). G1-4 Yes: the checkers read the `.raw` through spicelib and assert the frequency list (`read_cases`).

**G5.** G5-1 Yes: every stage in order with gain, NF and basis (`STAGE_NOTES`). G5-2 Yes: Friis re-computed. G5-3 Yes: image (IF 8 and 10), half-IF and IF responses.

**G7.** G7-1 Yes: extreme value (vertex) with interior polish; Monte Carlo seeds and N stated. G7-2 Yes for the capacitor and coil tolerance boxes as stated; C0G and coil temperature drift are not in the box (the aligned residual is meant to cover them, which the fix of finding-6 sets).

**H.** H1 N/A (no hazard). H2 Yes: section 8 proposes the risk to the risk writer. H3 Yes: section 9 names revision 2, its date and the review findings; the review record did not exist (O-3).

**I.** I1 Yes: 16 renders opened. I2 No: finding-8.

## Verdict (returned by the reviewer)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/rx-bpf-ts012.md@493cf931, hardware/sim/rx-frontend/ scripts, decks and runs r07 to r11 as in product_files, at d2d89e9
VERIFIED: finding-1, finding-2, finding-3 (Major); finding-4, finding-5 (Minor)
FINDINGS:
- [Major] CK-ANA-E3, D2, F4, B6 finding-6: the stated re-alignment limit (+/-0.75 %) fails the design-input corner (65.96 dB; the limit is about +/-0.32 %); the 2 + 3 + 3 image "PASS by 0.2 dB" lies inside the residual uncertainty (about 0.9 dB per 0.1 %).
- [Minor] CK-ANA-F3, E2 finding-7: the filter-only corner is called the TC-SYS-017 corner; TC-SYS-017 step 4 corners every input (the stack, -133.7 dBm).
- [Minor] CK-ANA-I2 finding-8: cascade_verdicts axis label reversed; 2-section NF curves omit the image-noise term; stale 2.5 dB BPF1 line.
- [Minor] CK-ANA-D2, D3 finding-9: README r04 row keeps the withdrawn 0.1 pF PASS; N = 2,995, not 2,996; r08 JSON from an earlier script (role only); Monte Carlo agreement on 200 of 1,000 draws.
ITEMS N/A: CK-ANA-E5, F2, H1, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), J1 to J3 (criticality neither)
VALUES PROPOSED: TPM-005: CBE -141.2 dBm (A5), -141.5 dBm (A4), Yellow (supported, estimates)
MEASUREMENTS: size=13 new decks, 5 runs; inputs_checked=12 rows (J310 datasheet rows, Coilcraft Q, REQ-SYS-022, 023, 033, TC-SYS-017, 021, TPM-005, TS-012 7.3); renders=16; turns=80; minutes=120; major=1 new (3 Verified); minor=3 new (2 Verified)
```

### What the review supports (rule C10)

With finding-6 Open, the 2 + 3 + 3 image verdict of section 5 does not go to the owner as a pass. The review supports: the TS-012 2 + 3 filter fails REQ-SYS-033 at IF 8 MHz (C-1); the TS-012 20 % capacitor condition fails for some builds (C-2); bare J310 ports fail (C-5); 2 + 3 + 4 holds REQ-SYS-033 at the design-input corner with margin, also at a +/-0.75 % residual (C-6); REQ-SYS-022 is not shown at the corner in any configuration and TPM-005 is Yellow on the CBE (C-11 to C-13); the half-IF result favours A5 (C-10); and neither the image nor the MDS result separates A4 from A5.

## Iteration 3: delta on note revision 3 (`a82f21b`), verification of finding-11 and reconciliation of the finding numbering (2026-09-28, HEAD `79795e4`)

**Scope (rule C1; the last iteration).** A delta that verifies the fix of the one Major open after iteration 2 (the residual limit, iteration 2 label finding-6, record id finding-11 below), re-runs r12 (the only new run), opens both new plots, checks every new value against its source (the r12 checker output, the frozen scripts, the iteration 2 reviewer's values), and scans every line revision 3 changed (note 45 lines added and 16 removed, `worst_case.py` +230, `run_sims.py` +2, README +7 and -2) for defects the revision introduced or that now decide a reported result (one such: finding-7, re-classified Major). It also reconciles the findings table of this record. Product: the 19 blobs of `product_files` at `a82f21b`; `git log a82f21b..HEAD` touches neither the note nor `hardware/sim/rx-frontend/` (it adds TS-012 revision 5, the keying note and three review records).

**Independence (rule C4).** This invocation authored no part of the note, its revisions or fixes, the decks, the scripts, the results or TS-012, and took no part in iterations 1 and 2. It edited no product file and changed only this record.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query "rx-bpf TS-012 receiver bandpass filter image rejection half-IF analysis") ran before every manual search; `grep` then only pinned lines in known files (the note, the README, the block scripts, TS-012, `tools/validate_docs.py`, this record). The rustos tree was not read.

**Sources.** Revision 3 adds no external input: the residual stays a labelled estimate, and the design-input conditions (mode B, VSWR 1.2, 0.03 pF, worst-phase bound) are those iteration 2 checked. For finding-7 the reviewer read REQ-SYS-114's range from this record's iteration 1 acceptance criteria and the C0G class coefficient (0 +/- 30 ppm/K, EIA RS-198 / IEC 60384-8) from a secondary source (independent checks below). The reference values are the r12 checker output (reproduced below) and the iteration 2 reviewer's design-input corner values (this record, iteration 2 "Independent checks"). For the finalist question: TS-012 revision 5 (`37d5824`) section 4.2 rows C5 and C8, section 8.3 row E5, section 8.10 row "REQ-SYS-032, 033", section 8.14 row D-15 and section 6 item 2.

### Finding numbering reconciled

The iteration 1 record (filed by the lead SE at `30681fc`) has ten findings: three Major (finding-1 to 3) and seven Minor (finding-4 to 10). Only finding-1 to 5 reached the author (note section 9 lists exactly those five, with the same numbers and content); the iteration 2 reviewer, finding no filed record, worked from that five-row transcription and gave its new findings the next free numbers, finding-6 to 9, which the iteration 1 record had already used. Its front matter therefore counted 4 Major and 5 Minor and left the iteration 1 Minors 6 to 10 out. From this iteration the record uses one numbering; the iteration 1 and 2 sections stay as filed (their `finding-6` to `finding-9` anchors point at the iteration 1 rows).

| Record-wide id | Iteration 1 record (`30681fc`) | Note section 9 and the iteration 2 transcription | Iteration 2 record label (`79795e4`) | Severity |
|---|---|---|---|---|
| finding-1 to finding-5 | finding-1 to 5 (mode A minimum; 50 ohm ports; MDS and TPM-005; checker exits; leakage at nominal) | finding-1 to 5, same content | finding-1 to 5 (Verified at iteration 2) | Major (1 to 3), Minor (4, 5) |
| finding-6 | finding-6: traceability (TS-012 commit, F7 confidence and Rs bound, 1N5711 model identity, `tbr.plan` step, risk request, change history) | not relayed | none (the label was re-used) | Minor |
| finding-7 | finding-7: REQ-SYS-114 temperature not stated | not relayed | none | Minor at iteration 1; Major from iteration 3 (re-classified below) |
| finding-8 | finding-8: highest J310 gain (16 dB) not analysed; isolation 84.48 dB rounded to 84 | not relayed | none | Minor |
| finding-9 | finding-9: per-resonator loss figure, coil-loss wording, cascade NF plot, typed plot band | not relayed | none | Minor |
| finding-10 | finding-10: mode B box centred on synthesized end capacitors; symmetric stray | not relayed | none | Minor |
| finding-11 | none | none | finding-6: the +/-0.75 % residual limit fails the design-input corner | Major |
| finding-12 | none | none | finding-7: filter-only corner called the TC-SYS-017 corner | Minor |
| finding-13 | none | none | finding-8: plot defects (MDS axis label, NF curves without the image-noise term, stale 2.5 dB line) | Minor |
| finding-14 | none | none | finding-9: README r04 row, N = 2,996, r08 JSON provenance, 200-of-1,000 comparison | Minor |
| finding-15, finding-16 | none | none | none (raised at iteration 3) | Minor |

Overlaps, kept as separate findings because each was raised on its own evidence: finding-13 (b) is the same plot defect as finding-9 (iii); finding-14 (a) is the README residue of finding-5. Corrected record-wide counts: to iteration 2, 14 findings (4 Major, 10 Minor), not the 4 Major and 5 Minor of the iteration 2 front matter; after iteration 3, 16 findings, 5 Major (finding-7 re-classified) and 11 Minor. The note's own section 9 table, which carries only finding-1 to 5 and "finding-6 (iteration 2)", uses the iteration 2 labels; the lead SE may wish to send the author this mapping with the liens.

### Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

**Reproduction (readiness R2).** Clean `git archive a82f21b hardware/sim/rx-frontend tools docs/design/analysis/rx-bpf-ts012.md` into the scratchpad (`iter3/`), with the committed r12 folder and the six r12 deck and case files moved aside before the run. From the export root with the repo venv (Python 3.13.5): `worst_case.py prepare r12` (exit 0); `run_sims.py 2026-09-28-r12-bpf-residual-design-input` with `CWHT_LTSPICE_LOCK_WAIT=5400` (another session held the LTspice lock) through `tools/ltspice-batch.sh` blob `88b71475`: three wrapper lines "result: PASS ... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0", `run_sims.py` exit 0, every `.log` first line "LTspice 26.0.2 for MacOS", no warning or error string in any log; `worst_case.py check r12` exit 0, as the README states.

Against the committed outputs: the six deck and case files byte-identical; `prepare.json` and `result.json` equal as parsed JSON to 1e-9; `result.md` byte-identical; both PNG pixel arrays equal; the r12 `scripts/` copies byte-identical to the frozen scripts (the stale-copy defect of finding-14 (c) does not recur in r12). LTspice against numpy: 18 cases, largest difference 3.6e-4 dB (limit 0.01 dB); the grid is monotone in all nine rows.

**Note against the checker.** Every number revision 3 adds equals `result.md` at the note's rounding: the 45 values of the section 4.2 residual table; the nine limits (+/-0.87, 0.51, 0.32 %; above 1.5, above 1.5, 0.97 %; 1.45, 0.98, 0.68 %) and the three design-input slopes (0.87, 1.26, 0.60 dB per 0.1 %); section 4.2 finding 4 (0.89, 0.93 and 0.87 dB per 0.1 % "about 0.9 at all three corners"; 71.87 - 68.40 = 3.47 dB for +/-0.1 to +/-0.5 %; 0.32 - 0.30 = 0.02 %; 0.97 - 0.30 = 0.67 % and 0.68 - 0.30 = 0.38 % of headroom); the LTspice image-phase case 70.105 dB at +/-0.32 %; the MHz conversions (0.32 %, 0.68 % and 0.97 % of 146 MHz: 0.47, 0.99 and 1.42 MHz); the README r12 row and alignment bullet. Revision 2's +/-0.75 % is withdrawn in every place it appeared (sections 0, 4.2 finding 3, 5 condition 2, README), and TS-012 revision 5 section 8.10 already carries "re-alignment to +/-0.32 %".

**Independent checks (reviewer scripts in the scratchpad `iter3/rev/`, not product).**
- **Slope by hand.** For the 132 MHz image of a 148 MHz tuning, f0 146 MHz, 6 MHz design bandwidth: Omega = (146 / 6)(146 / 132 - 132 / 146) = -4.92. Lowering every resonator by 0.1 % (146 kHz) changes Omega by (2 f0 / f)(0.146 / 6) = 0.0538, that is |Omega| by -1.09 %, which costs 20 n log10(1 / 0.989) = 0.095 dB per resonator, 0.76 dB for the eight resonators of 2 + 3 + 3. The remaining 0.1 dB of the 0.87 dB per 0.1 % is the rise of the in-band loss at 148 MHz as the passband moves down. The slope is physical, not a solver artefact.
- **Direction of the worst vertex** (`exact_map.py`, which calls the frozen `chain_corner`): at the stated limit and at the estimate, every coil of every section sits at its high-L bound (resonator frequency low) in all three configurations, worst tuned frequency 148.0 MHz. This agrees with note section 4.2 finding 2.
- **First-order residual map** (`exact_map.py`): `tolerance.py` draws a frequency residual r as L x [1 - 2 r, 1 + 2 r]. With the exact map (L x [(1 + r)^-2, (1 - r)^-2], so that |df / f| is at most r) the design-input corner is 70.181 dB at +/-0.3 % (first-order map 70.193), 70.006 dB at +/-0.32 % (70.019), 69.823 dB for 2 + 3 + 4 at +/-0.97 % (70.063) and 69.977 dB for 2 + 3 + 2 at IF 10 at +/-0.68 % (70.026). Basis of finding-16.
- **Temperature drift after a room-temperature alignment** (`temp_shift.py`, which calls the frozen `chain_corner` with every L bound multiplied by (1 + d)^-2, a common-mode frequency shift d of every resonator; d = 0 reproduces 70.193 dB). Input: C0G is 0 +/- 30 ppm/K (EIA RS-198 and IEC 60384-8 class 1 code C0G / NP0, as tabulated in the Wikipedia article "Ceramic capacitor", read 2026-09-28; a secondary source, the reviewer found no vendor PDF reachable); a free air-wound copper coil about +17 ppm/K from copper expansion (estimate). REQ-SYS-114 is -10 C to +45 C; the alignment is at room temperature (taken as 25 C). With the capacitor alone at a class limit, one end of the range moves every resonator down: +30 ppm/K at +45 C gives d = -0.5 x 30e-6 x 20 = -0.03 %; -30 ppm/K at -10 C gives d = -0.5 x (-30e-6)(-35) = -0.0525 %. With the coil term: -0.047 % at +45 C and -0.022 % at -10 C. So d of -0.03 to -0.05 % lies inside the parts' own class tolerance. Design-input corner, 2 + 3 + 3: at the +/-0.3 % estimate 70.193 / 69.930 / 69.754 / 69.486 dB for d = 0 / -0.03 / -0.05 / -0.08 %; at the stated +/-0.32 % limit 70.019 / 69.755 / 69.577 / 69.307 dB; an upward shift helps (70.624 dB at +0.05 %). 2 + 3 + 2 at IF 10 at the estimate: 72.479 / 72.296 / 72.172 / 71.986 dB; 2 + 3 + 4: 80.060 / 79.676 / 79.416 / 79.019 dB. Basis of the re-classification of finding-7.
- **Measurement resolution against the headroom.** At 146 MHz a 50 kHz sweep step reads a node to about +/-25 kHz, +/-0.017 %; at 0.87 dB per 0.1 % that is 0.15 dB, against the 0.02 dB the design-input corner keeps at +/-0.32 % (r12: 70.02 dB at 0.32 %, 69.76 dB at 0.35 %; about 69.87 dB at 0.337 % by linear interpolation). Basis of finding-15.

### Verification of finding-11 (Major; the re-alignment residual limit), case by case (rule C7)

| Finding | What the fix had to do (iteration 2 finding-6 "Fix") | Check at `a82f21b` | Result |
|---|---|---|---|
| finding-11 | State the residual limit at the design-input corner (about +/-0.32 %, or re-derive it) in sections 4.2, 5 and 7 item 3 and in the README | Re-derived by bisection in r12: +/-0.3222 %, stated +/-0.32 % (rounded down), in sections 0, 2 (residual row), 3 item 6, 4.2 (table and findings 3 and 4), 4.4 finding 2, 5 (table, condition 2, recommendation), 6, 7 item 3 and 9, and in the README (tool row, reproduce line, exit statuses, r12 row, alignment bullet). Reproduced by the re-run; the reviewer's exact-map check keeps +/-0.32 % for 2 + 3 + 3 (70.006 dB). The two alternatives' limits are 0.01 % high (finding-16, Minor) | Yes |
| finding-11 | Show the residual sensitivity at the design-input corner, not only with 50 ohm ports | r12 sweeps +/-0.05 to +/-1.5 % (15 points) at the 50 ohm, VSWR 1.2 and design-input corners for 2 + 3 + 3, 2 + 3 + 4 and 2 + 3 + 2 at IF 10; slope at the estimate by central difference over +/-0.25 and +/-0.35 %; `residual_design_input.png` and `residual_2p3p3_zoom.png` (opened: axes and units labelled, the 70 dB line carries REQ-SYS-033 (TBR), the +/-0.3 % estimate and the withdrawn +/-0.75 % marked, limits as diamonds with their values, LTspice points labelled as model checks at a real SGN; plotted values agree with `result.md` at 70.19 dB / +/-0.3 %, the three limits, 65.96 dB at +/-0.75 %) | Yes |
| finding-11 | Correct the return to the orchestrator | Commit `a82f21b` message and note section 9 withdraw +/-0.75 %; TS-012 revision 5 section 8.10 row "REQ-SYS-032, 033" states "re-alignment to +/-0.32 %", and TS-012 section 1 item 4 "0.2 dB under five build conditions" | Yes |
| finding-11 | Report the 2 + 3 + 3 image as not shown with margin, unless the alignment procedure demonstrates a residual with margin to that limit | The case is now reported as a conditional verdict whose condition is the right one: section 0 makes "a residual of at most +/-0.32 %" one of the conditions; section 5 reads "PASS by 0.2 dB ... with the +/-0.3 % residual estimate; the residual limit is +/-0.32 % (0.87 dB per 0.1 %), so the pass rests on an unmeasured estimate; no allowance left for the whole-chain leak"; section 4.2 finding 4 withdraws revision 2's "the residual is not the driver"; the recommendation calls 2 + 3 + 3 "not a robust basis" and names the configurations with margin; section 7 item 3 makes a measured residual within the limit the build acceptance and replaces the estimate by a first-build measurement. With the residual inside the stated limit the corner is at least 70.0 dB, so the case is no longer a pass resting on an input inside its own uncertainty (CK-ANA-E3). Two Minor residues: the acceptance has no guard band for the reading uncertainty, and "by 0.2 dB" is the margin at the estimate, not under condition 2 (0.02 dB) (finding-15). What the fix could not settle is outside finding-11's scope and pre-dates it: the condition is an alignment outcome at room temperature, and the temperature drift over REQ-SYS-114 that iteration 2 expected the residual to cover (its G7-2 answer) is not in it; with 0.02 % of headroom that now decides the case (finding-7, re-classified Major below) | Yes |
| finding-11 | The same for the alternative 2 + 3 + 2 at IF 10 (69.53 dB at +/-0.75 %) | Limit +/-0.68 % stated; 69.53 dB at +/-0.75 % reported as FAIL; 2 + 3 + 4 limit +/-0.97 % with 73.64 dB at +/-0.75 % | Yes (limits 0.01 % high: finding-16) |

**Result: finding-11 Verified.**

### Finding re-classified at iteration 3 (a defect that now decides a reported result)

The iteration 1 reviewer rated finding-7 Minor because, with the margins of revision 1 (about 86 dB nominal), a temperature bound changed no verdict. The finding was never relayed to the author (O-3 of iteration 2), so no revision answered it. Revision 3 has since made the 2 + 3 + 3 image verdict rest on 0.02 % of residual headroom, and temperature is the one variation of that residual the note neither models nor excludes.

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-7 | reviewer (iteration 1; re-classified at iteration 3) | Major | CK-ANA-F1, A5, G7-2, E3 | note sections 0 bullet 1, 2 (residual row), 5 (table row "Image, 2 + 3 + 3 ... under the five conditions", condition 2), 6, 7 item 3; `tolerance.py` residual box; TS-012 revision 5 sections 1 item 4 and 8.10 (which quote the result) | REQ-SYS-033 is conditioned by REQ-SYS-114 (-10 C to +45 C), and TC-SYS-021 step 4 corners "every toleranced input". The note names neither REQ-SYS-114 nor temperature. Condition 2 and the section 7 item 3 acceptance define the residual as the result of a room-temperature alignment on the NanoVNA, and the +/-0.3 % estimate is an alignment estimate, so drift after alignment is in neither. With the C0G parts inside their own class (0 +/- 30 ppm/K), one end of the REQ-SYS-114 range moves every resonator 0.03 to 0.05 % down (0.047 % at +45 C with a copper-expansion coil term), the direction of the worst vertex. At the design-input corner the frozen model then gives, for 2 + 3 + 3, 69.93 to 69.75 dB at the +/-0.3 % estimate and 69.76 to 69.58 dB at the +/-0.32 % limit: below 70 dB in both. The reported result "2 + 3 + 3 meets REQ-SYS-033 at the corner by 0.2 dB under five conditions" (note section 0 and 5; TS-012 revision 5 section 1 item 4 and 8.10; owner decision option 1 of note section 7) is therefore not shown over the required temperature range; a sixth condition or a smaller alignment acceptance (about +/-0.27 %, below the unmeasured +/-0.3 % estimate) would be needed. 2 + 3 + 4 (79.4 dB at d = -0.05 %) and 2 + 3 + 2 at IF 10 (72.2 dB) keep their pass. The error matters to the owner's choice: the note offers 2 + 3 + 3 as option 1 and gives 2 + 3 + 4 a corner MDS penalty, which pulls towards 2 + 3 + 3. Fix: state REQ-SYS-114 and the temperature assumption; carry the drift over -10 C to +45 C in the residual budget (for example as a common-mode shift of the box, as the reviewer's check does, with the C0G class limits and a coil coefficient); report 2 + 3 + 3 as not shown over REQ-SYS-114 unless the alignment acceptance can be set below the limit less the drift and less the reading uncertainty (finding-15); carry the change into section 0, 5, 7 items 1 and 3 and to the TS-012 author | Open | Pending (escalated to the owner, rule C1) | |

### New findings (iteration 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-15"></a>finding-15 | reviewer | Minor | CK-ANA-G7-2, A6 | note section 7 item 3 (acceptance sentence), section 5 table row "Image, 2 + 3 + 3 at IF 8 MHz, under the five conditions below" and condition 2, section 0 bullet 1 | The build acceptance that revision 3 writes for the alignment residual has no guard band. Section 7 item 3 accepts "every resonator node within the residual limit of the chosen configuration (+/-0.32 %, about +/-0.47 MHz, for 2 + 3 + 3 ...), with a sweep step and a reading uncertainty small against that limit (for 2 + 3 + 3, a 50 kHz step or finer: engineering judgement)". At the limit the design-input corner is 70.02 dB, so the scale that matters is the 0.02 dB left, not the 0.47 MHz limit. A 50 kHz step reads a node to about +/-25 kHz (+/-0.017 % at 146 MHz); at 0.87 dB per 0.1 % a node read at +/-0.32 % may sit at +/-0.337 %, where the corner is about 69.87 dB (r12 interpolation). The acceptance as written can pass a build that misses REQ-SYS-033 at the corner. In the same place, section 5 reports "PASS by 0.2 dB": that is the margin at the +/-0.3 % estimate; under condition 2 as written (residual up to +/-0.32 %) the margin is 0.02 dB. No reported number is wrong, the verdict is stated as conditional and the note already calls 2 + 3 + 3 "not a robust basis", so the finding is Minor. Fix: set the acceptance at the residual limit less the reading uncertainty (for example a reading uncertainty of +/-0.02 % or better with acceptance at +/-0.30 %), or state that a NanoVNA reading cannot demonstrate the 2 + 3 + 3 condition with margin; state the 0.02 dB margin under condition 2 beside the 0.2 dB at the estimate | Open | Pending | |
| <a id="finding-16"></a>finding-16 | reviewer | Minor | CK-ANA-D3, G7-1 | `tolerance.py` `Section.__init__` (L bound `(1 - 2 * res, 1 + 2 * res)`) as used by `worst_case.py` r12; note section 4.2 limit table and finding 3, section 5 table and condition 2, section 7 item 3, README r12 row and alignment bullet | The residual limits are stated "in frequency" but computed on the first-order map L x [1 - 2 r, 1 + 2 r]. Since f ~ L^-1/2, the high-L bound lowers a resonator by 1 - (1 + 2 r)^-1/2 = r - 1.5 r^2 + ..., less than r, and the worst vertex puts every coil at its high-L bound in all three configurations (reviewer check; note section 4.2 finding 2). The bisected limits are therefore limits on L that correspond to smaller frequency errors: 0.3207 % (not 0.3222 %) for 2 + 3 + 3, 0.960 % (not 0.974 %) for 2 + 3 + 4 and 0.677 % (not 0.684 %) for 2 + 3 + 2 at IF 10. With an exact frequency box the design-input corner at the stated limits is 70.006 dB for 2 + 3 + 3 at +/-0.32 % (holds, because of the rounding down), 69.823 dB for 2 + 3 + 4 at +/-0.97 % and 69.977 dB for 2 + 3 + 2 at +/-0.68 % (both below 70 dB). The two alternatives' limits are thus 0.01 % on the unsafe side of r12's own acceptance (a) ("stated rounded down"); +/-0.95 % and +/-0.67 % hold. The +/-0.3 % estimate moves by 0.012 dB. No verdict of the proposed configuration changes; the headroom figures 0.67 % and 0.38 % become 0.65 % and 0.37 %. Fix: draw the residual as an exact frequency box (or state the limits as limits on L), and correct the 2 + 3 + 4 and 2 + 3 + 2 limits and their MHz values (about +/-1.39 and +/-0.98 MHz) | Open | Pending | |

### Status of every finding at iteration 3 (record-wide numbering)

| Finding | Raised | Severity | Item | Subject | State | Evidence at `a82f21b` |
|---|---|---|---|---|---|---|
| finding-1 | iteration 1 | Major | CK-ANA-E3, G7-1, B6, D2 | Mode A reported as a pass on a 200-run minimum | Verified | Iteration 2 verification; unchanged by revision 3 |
| finding-2 | iteration 1 | Major | CK-ANA-G1-3, B1, A5, A6 | 50 ohm ports at the J310 stages not stated | Verified | Iteration 2 verification; unchanged |
| finding-3 | iteration 1 | Major | CK-ANA-E3, E2, A1 | REQ-SYS-022 "nominal PASS"; TPM-005 not named | Verified | Iteration 2 verification; unchanged |
| finding-4 | iteration 1 | Minor | CK-ANA-E4, D4 | Checkers exit 0 on FAIL; constants without ids | Verified | Iteration 2; `worst_case.py check r12` also exits 1 on a failing proposal (`prop_ok and ok_all`) and the new constants use `REQ_SYS_033_DB` |
| finding-5 | iteration 1 | Minor | CK-ANA-F3 | Leakage tolerance at nominal only | Verified | Iteration 2 verification (README residue is finding-14 (a)) |
| finding-6 | iteration 1 | Minor | CK-ANA-A2, A3, B2, E5, H2, H3 | Traceability | Open (lien) | Parts (v) and (vi) are now answered (section 8 proposes the MDS risk to the risk writer; section 9 carries a revision history). Still open: (i) TS-012 revision 4 cited without `7d0d450` (header and section 2 rows); (ii) `cw-selectivity-options.md` F7 cited without its confidence tag and the 60 ohm crystal Rs bound; (iii) the 1N5711 model still "for example evenator/LTSpice-Libraries `standard.dio`" without file, version or hash; (iv) the `tbr.plan` step for keeping REQ-SYS-033 at 70 dB not named. Never relayed to the author |
| finding-7 | iteration 1 (re-classified at iteration 3) | Major | CK-ANA-F1, A5, G7-2, E3 | REQ-SYS-114 temperature not analysed; the 2 + 3 + 3 image pass does not hold over -10 C to +45 C | Open | No mention of REQ-SYS-114 or temperature in the note at `a82f21b`. The iteration 1 nominal bound (85.3 to 87.3 dB) changed no verdict; at the design-input corner a C0G drift inside its class gives 69.93 to 69.75 dB at the +/-0.3 % estimate (re-classification above). Escalated to the owner (rule C1, last iteration) |
| finding-8 | iteration 1 | Minor | CK-ANA-F3, A5, D3 | Highest J310 gain not analysed; 84.48 dB rounded down | Open (lien) | Section 4.5 still "nominal gains (the worst case ...)" and A4 2 + 3 + 3 "16 dB margin"; section 4.4 still "84 dB for 2 + 3 + 3". At 16 dB per J310 the iteration 1 arithmetic gives an A4 half-IF margin of about 7.6 dB (2 + 3 + 3), still a pass |
| finding-9 | iteration 1 | Minor | CK-ANA-D2, I2, B1 | Loss figure, coil-loss wording, NF plot, typed plot band | Open (lien) | (ii) answered (section 6: "series resistance fixed at its 146 MHz value"); (i) section 4.1 still "0.6 to 1.3 dB"; (iii) is finding-13 (b); (iv) `check_halfif.py` line 130 still `axvspan(-58.5, -51.8)` |
| finding-10 | iteration 1 | Minor | CK-ANA-G7-1, G1-3 | Mode B box centred on synthesized end capacitors; symmetric stray | Open (lien) | `tolerance.py` docstring and bounds unchanged. Benign: iteration 2 found the design-input corner 0.8 dB better (70.98 dB) with the box on the stocked 4.7 and 4.3 pF parts |
| finding-11 | iteration 2 (label finding-6) | Major | CK-ANA-E3, D2, F4, B6 | Residual limit at the design-input corner | Verified | Verification above |
| finding-12 | iteration 2 (label finding-7) | Minor | CK-ANA-F3, E2 | Filter-only corner called the TC-SYS-017 corner | Open (lien) | Unchanged in sections 0, 4.6, 5 and 8 |
| finding-13 | iteration 2 (label finding-8) | Minor | CK-ANA-I2 | r11 and r09 plot defects | Open (lien) | r09 and r11 not re-run in revision 3; plots unchanged |
| finding-14 | iteration 2 (label finding-9) | Minor | CK-ANA-D2, D3 | README r04 row; N = 2,996; r08 JSON provenance; 200-of-1,000 comparison | Open (lien) | README r04 row still "Worst case 78.2 dB at 0.1 pF per section (PASS 70 dB)"; section 3 item 6 still "N = 2,996"; (c) and (d) unchanged |
| finding-15 | iteration 3 | Minor | CK-ANA-G7-2, A6 | No guard band in the residual acceptance | Open | New finding above |
| finding-16 | iteration 3 | Minor | CK-ANA-D3, G7-1 | First-order residual map; alternatives' limits 0.01 % high | Open | New finding above |

### Observations (no finding)

- **O-5.** TS-012 revision 5 section 9 table R5-1 says for this analysis "no review record is filed on main at this revision" and "iteration 3 not yet run"; both were true at `37d5824` and are now stale (record at `30681fc` and `79795e4`, this iteration). A TS-012 item for the lead SE, not a defect of the note.
- **O-6.** The r12 corner is a bound over independent per-section vertices with every coil at the same extreme; the note says so (section 6). A measured residual below the limit therefore has more real margin than the bound shows, the same direction as O-4 of iteration 2.

### Per-case results (iteration 3; the cases revision 3 changed, and the temperature case)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-4 | Image, 2 + 3 + 3 at IF 8, design-input corner, residual at the +/-0.3 % estimate / at the stated +/-0.32 % limit / at revision 2's +/-0.75 % | REQ-SYS-033 / TC-SYS-021: at least 70 dB at the corners | 70.19 / 70.02 / 65.96 dB: PASS / PASS / FAIL | +0.19 / +0.02 / -4.04 dB | residual (0.87 dB per 0.1 %), reading uncertainty of the acceptance | re-run identical; exact frequency box 70.18 / 70.006 dB | finding-15 |
| C-6 | Image, 2 + 3 + 4 at IF 8, design-input corner, at +/-0.3 % / stated +/-0.97 % / +/-0.75 % | REQ-SYS-033 corner | 80.06 / 70.06 / 73.64 dB: PASS | +10.06 / +0.06 / +3.64 dB | residual (1.26 dB per 0.1 % at the estimate) | re-run identical; exact frequency box 69.82 dB at +/-0.97 % (limit +/-0.95 %) | finding-16 |
| C-7 | Image, 2 + 3 + 2 at IF 10, design-input corner, at +/-0.3 % / stated +/-0.68 % / +/-0.75 % | REQ-SYS-033 corner | 72.48 / 70.03 / 69.53 dB: PASS / PASS / FAIL | +2.48 / +0.03 / -0.47 dB | residual (0.60 dB per 0.1 %) | re-run identical; exact frequency box 69.98 dB at +/-0.68 % (limit +/-0.67 %) | finding-16 |
| C-4a | 2 + 3 + 3 at the 50 ohm and VSWR 1.2 corners (reference rows) | REQ-SYS-033 corner | limits +/-0.87 % and +/-0.51 % | n/a | as C-4 | re-run identical | none |
| C-20 | Image at the design-input corner over REQ-SYS-114 (-10 C to +45 C) after a room-temperature alignment: 2 + 3 + 3 at the +/-0.3 % estimate / at the +/-0.32 % limit; 2 + 3 + 2 at IF 10 and 2 + 3 + 4 at the estimate | REQ-SYS-033 with REQ-SYS-114; TC-SYS-021 step 4 | not analysed | not shown | C0G class 0 +/- 30 ppm/K; coil coefficient an estimate | reviewer: 69.93 to 69.75 dB / 69.76 to 69.58 dB for a 0.03 to 0.05 % downward drift (below 70 dB); 72.30 to 72.17 dB and 79.68 to 79.42 dB (pass) | finding-7 |

Every other case of the iteration 2 per-case table is unchanged at `a82f21b` (r01 to r11 are not touched by revision 3).

### Checklist answers (iteration 3, delta)

**A.** A1 No: REQ-SYS-114, which conditions REQ-SYS-033, is still not named (finding-7); REQ-SYS-033 and TC-SYS-021 are named for r12. A2 No: finding-6 (i) (TS-012 commit). A3 No: finding-6 (ii), (iii); the residual is labelled an estimate. A4 Yes: no new external input; every r12 value equals the checker. A5 No: finding-7 (temperature, now deciding), finding-8 (highest gain); the residual assumption and its direction are otherwise stated. A6 Yes: the residual limit goes to the build notes (section 7 item 3) and to TS-012 as a design input; the acceptance's guard band is finding-15 (Minor).

**B.** B1 Yes: the nested-box monotonicity argument is stated and checked on the grid. B2 No: finding-6 (iii) (unchanged 1N5711 model; not used by r12). B3 Yes: 18 LTspice cases. B4 Yes: 15-point grid, bisection to 0.0001 %, central-difference slope. B5 Yes: slope by hand, worst-vertex direction and exact-map checks above. B6 Yes: the 2 + 3 + 3 margin is now set against the residual (limit and slope), which finding-11 asked for.

**C.** C1 to C5 Yes: re-run above; the wrapper's lock, time-out and version checks passed.

**D.** D1 Yes. D2 No: finding-9 (i), finding-14 (a) and (d). D3 No: finding-16 (limits rounded down on L, not on frequency), finding-14 (b), finding-8 (84.48 dB). D4 Yes.

**E.** E1 Yes. E2 Yes, with finding-12. E3 No: at room temperature the 2 + 3 + 3 image is a conditional verdict with the condition at its limit and the reliance on the unmeasured estimate stated (finding-11 Verified), but over REQ-SYS-114 the pass lies inside a drift the note does not model (finding-7); the missing guard band is finding-15. E4 Yes: `check r12` exits 1 on a failing proposal. E5 N/A as at iteration 2 (no TBR value proposed; the `tbr.plan` wording of finding-6 (iv) is a traceability lien). E6 Yes (section 8 unchanged). E7 Yes.

**F.** F1 No: finding-7 (the REQ-SYS-114 case C-20 has no row in the note). F2 N/A. F3 No: finding-8, finding-12. F4 Yes: residual sensitivity shown at all three corners (finding-11).

**G1.** G1-1 to G1-4 Yes (r12 decks carry one `.ac` each; the checker reads the `.raw` through spicelib and asserts the frequency list). **G5.** Unchanged, Yes. **G7.** G7-1 No: finding-16 (first-order box), finding-10. G7-2 No: finding-7 (temperature), finding-15 (acceptance without guard band).

**H.** H1 N/A. H2 Yes. H3 Yes: section 9 records revision 3.

**I.** I1 Yes: both new plots opened; regenerated copies pixel-equal. I2 Yes for r12 (labels, units, the limit line with its id, legends); No record-wide on finding-13.

## Verdict (iteration 3, returned by the reviewer)

```
VERDICT: NEEDS CHANGES (reviewer and record); last iteration (rule C1): the open Major escalates to the owner
PRODUCT: docs/design/analysis/rx-bpf-ts012.md@056d5580, hardware/sim/rx-frontend/ worst_case.py, run_sims.py, README, r12 decks and results as in product_files, at a82f21b
VERIFIED: finding-11 (Major; iteration 2 label finding-6). Earlier: finding-1, 2, 3 (Major), finding-4, 5 (Minor)
OPEN MAJOR:
- [Major, re-classified from Minor] CK-ANA-F1, A5, G7-2, E3 finding-7 (iteration 1): REQ-SYS-114 not analysed; after a room-temperature alignment a C0G drift inside its +/-30 ppm/K class moves every resonator 0.03 to 0.05 % down at one end of -10 C to +45 C; 2 + 3 + 3 at the design-input corner falls to 69.93 to 69.75 dB at the +/-0.3 % estimate (69.76 to 69.58 dB at the +/-0.32 % limit), so its reported pass is not shown over REQ-SYS-114; 2 + 3 + 4 (79.4 dB) and 2 + 3 + 2 at IF 10 (72.2 dB) keep theirs
OPEN MINOR:
- finding-6 (iteration 1): TS-012 commit, F7 confidence and Rs bound, 1N5711 model identity, tbr.plan step ((v) and (vi) answered)
- finding-8 (iteration 1): highest J310 gain not analysed (A4 half-IF margin about 7.6 dB, still a pass); 84.48 dB rounded down
- finding-9 (iteration 1): 0.6 to 1.3 dB per resonator; NF plot; typed plot band ((ii) answered)
- finding-10 (iteration 1): mode B box centre and symmetric stray (benign)
- finding-12 (iteration 2 label 7): filter-only corner called the TC-SYS-017 corner
- finding-13 (iteration 2 label 8): r09 and r11 plot defects
- finding-14 (iteration 2 label 9): README r04 row, N = 2,996 (2,995), r08 JSON provenance, 200-of-1,000 comparison
- [new] finding-15: residual acceptance without a guard band (a 50 kHz step is 0.15 dB against 0.02 dB); "by 0.2 dB" is the margin at the estimate, 0.02 dB under condition 2
- [new] finding-16: first-order L map; the 2 + 3 + 4 and 2 + 3 + 2 limits are 0.01 % high (+/-0.95 % and +/-0.67 % hold); 2 + 3 + 3's +/-0.32 % holds (70.006 dB)
ITEMS N/A: CK-ANA-E5, F2, H1, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), J1 to J3 (criticality neither)
VALUES PROPOSED: TPM-005: CBE -141.2 dBm (A5), -141.5 dBm (A4), Yellow (supported, estimates; unchanged by revision 3)
MEASUREMENTS: size=3 new decks (18 cases), 1 run (r12), 61 note lines changed; inputs_checked=r12 checker output, the iteration 2 reviewer values, the C0G temperature class (secondary source); renders=2; turns=45; minutes=95; major=1 re-classified (1 Verified); minor=2 new; record-wide 5 Major, 11 Minor, 6 Verified, 10 open (1 Major, 9 Minor)
```

**Escalation (rule C1).** Iteration 3 is the last; finding-7 is open and Major, so the record goes to the owner. The defect is narrow and its fix is analysis and wording only (no new run is strictly needed: the reviewer's `temp_shift.py` is one way to carry the drift). The owner may rule on it (for example direct the author to report 2 + 3 + 3 as not shown over REQ-SYS-114, or authorize a fourth iteration as for INSP-110), or accept it as a lien against the WP-PDR-19 filter choice, which the note already defers to the front-end redesign. Note that the finding reached the author for the first time through this record: the iteration 1 Minors were never relayed (O-3 of iteration 2).

### What the review supports (rule C10)

With finding-7 open, the 2 + 3 + 3 image result does not go to the owner as a pass. The review supports: the TS-012 revision 4 filter (2 + 3) fails REQ-SYS-033 at IF 8 MHz; the TS-012 20 % capacitor condition fails for some builds; with mode B parts, re-alignment, VSWR 1.2 ports and 0.03 pF stray, 2 + 3 + 3 meets 70 dB at the corner at room temperature only while every resonator stays within +/-0.32 % (0.02 dB at that limit, 0.19 dB at the unmeasured +/-0.3 % estimate), with no room for the whole-chain leak, and not over REQ-SYS-114 (69.93 to 69.75 dB at the estimate with a C0G drift inside its class), so it is not shown; 2 + 3 + 4 holds with margin, also over temperature (79.4 dB) (80.1 dB at the estimate, residual up to +/-0.95 %); 2 + 3 + 2 at IF 10 holds 72.5 dB (residual up to +/-0.67 %; 72.2 dB with the drift); REQ-SYS-022 is not shown at the corner in any configuration and TPM-005 is Yellow; the half-IF result favours A5's ring; and neither the image nor the MDS result separates A4 from A5, because the filters and front end are common to both.

**Effect on the TS-012 finalists.** Nothing TS-012 revision 5 relies on for A4 against A5 changes. Section 4.2 C5 cites from this note only the half-IF margins (A4 12 to 16 dB, Low; A5 34 to 37 dB), which come from r05, r06 and r11 and are untouched by revision 3; the A4 C5 score of 2 rests on the PA terms (no AFT05 harmonic data, low-pack power), and the open lien finding-8 would narrow the A4 half-IF margin to about 7.6 dB without reversing the pass; even an A4 C5 move of -1 leaves A4 at 295 against A5's 270 (TS-012 section 6 item 2). C8 rests on the thermal note, not on this one. Row E5 (a) (third BPF section and J310 port matching, seven to nine 0805 C0G parts in B or C tolerance, coils from owned wire, USD 1.00 to 4.50) is common to both finalists; revision 3 adds no part and no tolerance change (the residual limit is an alignment acceptance at no cost), and finding-16 changes only the alternatives' alignment limits. TS-012 revision 5 already carries the +/-0.32 % limit (section 8.10) and the "0.2 dB under five build conditions" wording (section 1 item 4). That wording is what finding-7 and finding-15 correct: over REQ-SYS-114 2 + 3 + 3 is not shown, so the receiver design item D-15 (section 8.14) points to 2 + 3 + 4 or IF 10 MHz 2 + 3 + 2, both of which keep their pass, unless the author adds a temperature condition that restores 2 + 3 + 3. The change applies equally to A4 and A5, stays inside the E5 (a) range (seven to nine C0G parts, owned wire) and moves no C1, C2, C5 or C8 cell, so the ranking A4 315 against A5 270 and the A4 recommendation stand.

## Commands (iteration 3)

- Search: `mcp__claude-context__search_code` path `/Users/robinonsay/rust/cwht`, query "rx-bpf TS-012 receiver bandpass filter image rejection half-IF analysis".
- Freeze and blobs: shell loop over `git rev-parse a82f21b:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (19 files, all equal); `cmp` of the r12 `scripts/` copies against the frozen scripts.
- Re-run: `git archive a82f21b hardware/sim/rx-frontend tools docs/design/analysis/rx-bpf-ts012.md | tar -x -C <scratchpad>/iter3`; committed r12 folder and r12 decks moved to `author/`; `.venv/bin/python hardware/sim/rx-frontend/worst_case.py prepare r12`; `CWHT_LTSPICE_LOCK_WAIT=5400 .venv/bin/python hardware/sim/rx-frontend/run_sims.py 2026-09-28-r12-bpf-residual-design-input`; `worst_case.py check r12`; JSON (to 1e-9), Markdown (byte) and PNG (pixel array) comparisons in Python.
- Independent checks: `<scratchpad>/iter3/rev/exact_map.py` (worst-vertex direction, exact frequency box at the stated limits); `<scratchpad>/iter3/rev/temp_shift.py` (common-mode temperature drift added to the design-input corner); slope by hand (above). C0G class read with the web-fetch tool from https://en.wikipedia.org/wiki/Ceramic_capacitor (the KEMET C0G datasheet URL returned a redirect to a 404).
- Record check: `.venv/bin/python tools/validate_docs.py` on the repository after the edit.

## Iteration 3 re-issue 1: the owner-authorized fourth iteration, delta on note revision 4 (`63122e7`), verification of finding-7 (2026-09-29, HEAD `63122e7`)

**Authority and scope (rule C1).** Iteration 3 escalated the open Major finding-7 to the owner. Owner statement, verbatim (`docs/plan/status/status-2026-09-29.md` section 2): "Yes both recs sound good", recorded there as "INSP-117 iteration 4 is authorized; the note's revision 4 adopts 2+3+4 and analyses REQ-SYS-114". The schema caps `iteration` at 3, so this fourth iteration is recorded as "Iteration 3 re-issue 1" (precedent INSP-009, INSP-038, INSP-075, INSP-110). It is a delta on the finding-7 fix only: it re-runs the new run r13 from a clean export, checks every temperature input against its source, checks the 2 + 3 + 4, 2 + 3 + 2 and 2 + 3 + 3 margins over -10 C to +45 C ambient (board -10 C to +70 C), opens both new plots, and raises new findings only where revision 4 introduced them (one: finding-17). The Minor findings stay liens (rule C1; the author fixed none, as note section 9 says). Product: the 19 blobs of `product_files` at `63122e7` (the author's commit, 42 files; note 210 lines added and 46 removed, `worst_case.py` +300 -8, `tolerance.py` +17 -5, `run_sims.py` +2, README +11 -5, three decks with case files, run r13). HEAD is `63122e7`, so nothing after it touches the product.

**Independence (rule C4).** This invocation authored no part of the note, its revisions or fixes, the decks, the scripts, the results or TS-012, and took no part in iterations 1 to 3. It edited no product file and changed only this record.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (queries "receiver BPF temperature model r13 bpf temperature 2+3+4 IF 8 MHz tempco" and "thermal model main bay PA bay which parts are in each bay receiver front end relay BPF placement") ran before every manual search; `grep` then only pinned lines in known files (this record, the note, `worst_case.py`, `tolerance.py`, the README, the thermal note, TS-012, `tools/validate_docs.py`, the INSP-110 record for the re-issue precedent). The rustos tree was not read.

### Reviewer re-run (CK-ANA-C4) and independent checks (CK-ANA-B5)

**Freeze (readiness R1).** Shell loop over `git rev-parse 63122e7:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>`: 19 of 19 equal. The eleven `results/2026-09-29-r13-bpf-temperature/scripts/` copies are byte-identical (`cmp`) to the frozen block scripts.

**Reproduction (readiness R2).** `git archive 63122e7 hardware/sim/rx-frontend tools docs/design/analysis/rx-bpf-ts012.md` into the scratchpad (`iter4/`), with the committed r13 folder and the six r13 deck and case files moved to `author/` before the run. From the export root with the repo venv: `worst_case.py prepare r13` exit 0 (18 min 21 s on 14 cores); `CWHT_LTSPICE_LOCK_WAIT=5400 run_sims.py 2026-09-29-r13-bpf-temperature` through `tools/ltspice-batch.sh` blob `88b71475` (equal to the frozen blob): three wrapper lines "result: PASS ... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0", `run_sims.py` exit 0, every `.log` first line "LTspice 26.0.2 for MacOS" with no error or warning string; `worst_case.py check r13` exit 0, as the README states. Against the committed outputs: the six deck and case files byte-identical; `prepare.json` and `result.json` equal as parsed JSON with a largest numeric difference of 0.0; `result.md` byte-identical; both PNG pixel arrays equal. LTspice against numpy: 22 cases, largest difference 3.604e-4 dB (limit 0.01 dB), as the note says. Every regenerated `.raw` is under 5 MB (largest 53,342 bytes), so the raw-file rule needs no manifest.

**Note against the checker.** Every value revision 4 adds equals `result.md` at the note's rounding: sections 0, 4.2.1 (drift table, the 27-cell residual table, the limit table with +/-0.9596, 0.8842, 0.6407 %; 0.6768, 0.5938, 0.3238 %; 0.3205, 0.2389 % and "none"; the 33-cell board sweep), 5 (table rows and conditions 2 and 6), 7 item 3, 8 and 9, and the README r13 row. The MHz conversions are right (0.64 % and 0.62 % of 146 MHz: 0.93 and 0.91 MHz, stated "about +/-0.90"). The isolation re-derivation of section 4.4 is right: with 5.37 dB of margin the worst-phase leak may be 1.35 dB below the filtered image response (20 log(1 + 10^(-x/20)) = 5.37 dB), so 75.37 + 1.35 + 12 dB of front-end gain (r11: 82 - 70) gives 88.7 dB, "about 89 dB"; 2 + 3 + 2 at 0.16 dB needs x = 34.6 dB, 70.16 + 34.6 + 17 = 121.8 dB, "about 122 dB".

**Independent checks (reviewer scripts in the scratchpad `iter4/rev/`, not product).**
- **Drift box from first principles** (`drift_check.py`). f = 1 / (2 pi sqrt(L C)), so after an alignment at T_a each resonator moves by ((1 + aL dT)(1 + aC dT))^-1/2 - 1. With aL in +5 to +70 ppm/K, aC in -40 to +40 ppm/K and T_a in 20 to 30 C: board -10 C gives -0.0699 % to +0.2205 % (first order -0.5 (aL + aC) dT: -0.070 to +0.220 %); board +70 C gives -0.2742 % to +0.0876 % (first order -0.275 to +0.0875 %); doubled classes -0.1396 to +0.4420 % and -0.5469 to +0.1756 %. Hot coil Q: skin resistance goes as the square root of the resistivity, so Q = 100 / sqrt(1 + 0.00393 x 45) = 92.18. Box widening 40 ppm/K x 50 K = 0.20 % hot and x 40 K = 0.16 % cold. All equal the r13 state table.
- **Box semantics** (`drift_check.py`, frozen `tolerance.Section`, BPF3 of four, hot, +/-0.3 %). Every coil bound is L x [((1 + r)(1 + d_hi))^-2, ((1 - r)(1 + d_lo))^-2] = [0.992287, 1.011567], as the exact map requires; every coupling and end capacitor bound is the mode B bound times (1 -/+ 0.002). The alignment (`ns_for`, "at50") re-tunes each coil to the drawn capacitors, so the capacitor drift enters the node frequency once, through d, and the coupling and external-Q change through the widening, as note section 3 item 6 states. Per-resonator drift inside the box is a superset of iteration 3's common-mode shift (every coil at its high-L bound is one vertex).
- **Four-resonator BPF3 synthesis by hand.** Chebyshev 0.1 dB, n = 4: g = 1.1088, 1.3061, 1.7703, 0.8180; FBW 6 / 145.99 = 0.0411; k12 = 0.0411 / sqrt(1.1088 x 1.3061) = 0.0342 and k23 = 0.0270; node C 21.22 pF, so coupling 0.725 and 0.574 pF (synthesis 0.7248, 0.5736 pF); Qe = 26.98, Rp = 1386 ohm, end series C = 4.218 pF (synthesis 4.2185 pF); shunt 21.22 - 0.725 - 4.066 = 16.43 pF and 21.22 - 0.725 - 0.574 = 19.92 pF (synthesis 16.433 and 19.926 pF). The note's element table row agrees.
- **Regression of r12 under the revised `tolerance.py`** (`hot_sens.py`, defaults, first-order map): the 2 + 3 + 3 design-input corner is 70.193 dB at +/-0.3 % and 70.019 dB at +/-0.32 %, the r12 values, so "defaults unchanged, so r08 to r12 reproduce" holds for the case checked.
- **Hot end beyond +70 C and the acceptance** (`hot_sens.py`, frozen `_r13_value`, 2 + 3 + 4). At the +/-0.62 % acceptance: 70.345 dB at +70 C, 70.023 dB at +73 C, 69.808 dB at +75 C, 69.270 dB at +80 C, and 74.362 dB at -10 C. At the +/-0.3 % estimate: 74.372 dB at +80 C, 73.368 dB at +90 C. Worst tuning 148.0 MHz in every case. Basis of finding-17.
- **After-assembly check value.** The frozen solver gives the nominal per-section rejection at 130 MHz relative to 146 MHz, coil Q 100, 50 ohm: 19.47, 39.36 and 58.95 dB for two, three and four resonators (note section 7: "19.5, 39.4 and 59.0 dB"; O-8).

### Temperature inputs checked against their sources (CK-ANA-A4; every input revision 4 adds)

| Note row (section 2) | Source read by the reviewer | Agreement |
|---|---|---|
| REQ-SYS-114 text, -10 C to +45 C (TBR) | `docs/requirements/sys/requirements.md` REQ-SYS-114, statement "The transceiver shall meet its requirements at ambient temperatures from -10 C to +45 C (TBR)." | Yes, quoted exactly |
| C0G: TCC +/-30 ppm/C, -55 to +125 C, from 0.5 pF, B tolerance offered, no small-value exception | KEMET "Surface Mount Multilayer Ceramic Chip Capacitors (SMD MLCCs) C0G Dielectric, 10 - 250 VDC (Commercial Grade)", footer "C1003_C0G 2/20/2025", `https://content.kemet.com/datasheets/kem_c1003_c0g_smd.pdf`, read 2026-09-29 (SHA-256 prefix `02d17991`, `pdftotext -layout`): Electrical Parameters table "Capacitance Change with Reference to +25C and 0 VDC Applied (TCC)" +/-30 ppm/C; operating range -55 to +125 C; "Capacitance offerings ranging from 0.5 pF up to 0.47 uF"; tolerance code B = +/-0.10 pF; 0805 listed; no footnote narrowing the TCC for small values | Yes |
| Coil TCL +5 to +70 ppm/C | Coilcraft Document 184-1 "Revised 12/02/21" (the URL of the coil Q row), read 2026-09-29 (SHA-256 prefix `e8ce1b27`): "Temperature Coefficient of Inductance (TCL) +5 to +70 ppm/C"; ambient -40 to +125 C; 1812SMS-56N Q typ 125, min 100 at 150 MHz | Yes. Applying the class to a hand-wound air coil is labelled an estimate; copper expansion alone (about +17 ppm/K, which scales an air coil's linear dimensions and so its L) lies inside it |
| Board -10 C to +70 C; V18 55.3 to 63.5 C with bands up to +4.8 K, at most 67.4 C (A4-R4) | `docs/design/analysis/thermal-ts012.md` revision 1, verdict table row V18: A5-R4 60.2 +4.6, A5-DC 57.8 +4.8, A4-R4 63.5 +3.9, A4-DC 55.3 +3.5 C; so the largest value plus band is 67.4 C (A4-R4). The receiver is on the main board (TS-012 sections 8.1 and 8.5: the RF board carries the transmit chain and the main board the receiver blocks), whose air is the MAIN node | Yes for the air temperature. The bound is air, not the part temperature on the main board, which carries the LM2940 and feed-part dissipation (finding-17). The thermal note is still under review (INSP-112), as the note says |
| Stray and port capacitance drift +/-10 ppm/K on the node (about 1 pF at up to +/-200 ppm/K) | estimate: 1 pF x 200 ppm/K / 21.2 pF = 9.4 ppm/K | Yes (estimate, labelled) |
| Coil Q falling with temperature, 92.2 at +70 C; not raised below 25 C | copper resistivity coefficient 0.00393 per K (standard value); skin resistance proportional to sqrt(rho) | Yes; holding Q at 100 below 25 C is conservative |
| Alignment at 20 to 30 C | proposed build condition (section 5 condition 6) | Yes (a condition, not an input) |

### Verification of finding-7 (Major), case by case (rule C7)

| Finding | What the fix had to do (iteration 3 "Fix") | Check at `63122e7` | Result |
|---|---|---|---|
| finding-7 | State REQ-SYS-114 and the temperature assumption | Section 2 adds the REQ-SYS-114 row (quoted exactly) and six temperature rows, each with a source read on 2026-09-29 or labelled estimate; section 6 lists the temperature limitations (coil class applied to a hand-wound coil, stray allowance, board bound under review, J310 ports assumed within VSWR 1.2 over temperature, capacitor Q and vias held, steady state, MDS not re-analysed); section 5 condition 3 now holds "over the board temperature range" and condition 6 is new | Yes |
| finding-7 | Carry the drift over -10 C to +45 C in the residual budget, with the C0G class limits and a coil coefficient | r13 draws each resonator's frequency multiplier in [(1 - r)(1 + d_lo), (1 + r)(1 + d_hi)] on the exact map, with the C0G class plus a stray allowance, the Coilcraft class, a 20 to 30 C alignment, the coupling and end capacitor widening and the hot coil Q; board -10 C (soak) to +70 C (+45 C ambient plus the V18 main-bay rise). This is a superset of the reviewer's common-mode shift (iteration 3: -0.03 to -0.05 %); the hot drift reaches -0.274 %. Reproduced exactly; drift, Q and box bounds re-derived by hand; the board sweep confirms the cold and hot cases bound every temperature between | Yes |
| finding-7 | Report 2 + 3 + 3 as not shown over REQ-SYS-114 unless the acceptance can be set below the limit less the drift and the reading uncertainty | 2 + 3 + 3 is reported FAIL and withdrawn in sections 0, 4.2.1 finding 1, 5, 7 item 1 and the README: 69.46 dB cold, 67.00 dB hot at the +/-0.3 % estimate, and no residual holds 70 dB hot (the bisection ends at 0.0 %). Iteration 3's 69.93 to 69.75 dB is confirmed and exceeded | Yes |
| finding-7 | Carry the change into sections 0, 5, 7 items 1 and 3 and to the TS-012 author | The design becomes 2 + 3 + 4 at IF 8 MHz on the owner's authorization: worst case 75.37 dB (+5.37 dB) hot at the estimate, limit over temperature +/-0.64 % (hot +/-0.6407 %, rounded down), acceptance +/-0.62 % after a +/-0.02 % reading allowance, doubled classes 70.99 dB; sections 0, 4.2 finding 6, 4.2.1, 4.4 finding 3, 4.6 finding 5, 5, 6, 7 items 1 to 3 and 8, 8 and 9 revised. Section 7 item 1 hands the change to the TS-012 author (D-15, row E5 (a), section 1 item 4, section 8.10). TS-012 revision 6 (`3b93de1`, committed before this note revision) already adopts 2 + 3 + 4 but quotes r12 and iteration 3 figures (cross item X-R4-1) | Yes |
| finding-7 | (margins asked by this delta) 2 + 3 + 4, 2 + 3 + 2 and 2 + 3 + 3 over -10 to +45 C | See the per-case rows below; all reproduced from the clean export; the margins' sensitivity to the coefficient classes (doubled: 70.99 dB) and to the board bound (finding-17) checked | Yes |

**Result: finding-7 Verified.** The adopted design's pass rests on a stated corner that the reviewer reproduced, with 5.37 dB of margin at the estimate, 0.99 dB with both coefficient classes doubled, and a residual acceptance with a guard band. What stays open is Minor: the hot bound is air, not part temperature, and the acceptance's temperature headroom is about 3 K (finding-17).

### New finding (iteration 3 re-issue 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-17"></a>finding-17 | reviewer | Minor | CK-ANA-A5, G7-2, F1 | note section 2 row "Board temperature (revision 4)", section 5 conditions 2 and 6, section 6 temperature bullet 2, section 7 item 3; `worst_case.py` `T_BOARD` | Revision 4 sets the hot bound at +70 C, the main-bay air of thermal row V18 (A4-R4 63.5 + 3.9 = 67.4 C) rounded up by 2.6 K, and applies it to every resonator part. The resonators sit on the main board, which carries the main-bay heat sources of the thermal note (the LM2940, 0.9 W, at the sink end of the main bay; the feed parts, 1.0 W; the Pico 2 and op-amps, 0.2 W). The thermal model has one MAIN air node and no board node, and no layout places the BPF cells, so a BPF part can run above the air. The note labels the bound an estimate and names a re-run if the thermal review moves the air above 70 C, but not the assumption that the BPF parts are at the air temperature. The verdict at the estimate does not depend on it (reviewer, frozen model at +/-0.3 %: 74.37 dB at +80 C, 73.37 dB at +90 C). The alignment acceptance does: at +/-0.62 % the design-input corner is 70.35 dB at +70 C, 70.02 dB at +73 C, 69.81 dB at +75 C and 69.27 dB at +80 C, so the acceptance keeps about 3 K over the bound. Fix: state the assumption (BPF part temperature equal to the main-bay air) and make it a layout condition (the BPF cells away from the LM2940, the feed parts and the sink end), or add a board-over-air allowance to the hot bound and re-derive the limit and the acceptance from it; send the item to the layout and thermal work packages | Open | Pending | |

### Status of every finding at iteration 3 re-issue 1 (record-wide numbering)

| Finding | Raised | Severity | Item | Subject | State | Evidence at `63122e7` |
|---|---|---|---|---|---|---|
| finding-1 | iteration 1 | Major | CK-ANA-E3, G7-1, B6, D2 | Mode A reported as a pass on a 200-run minimum | Verified | Verified at iteration 2; unchanged by revision 4 |
| finding-2 | iteration 1 | Major | CK-ANA-G1-3, B1, A5, A6 | 50 ohm ports at the J310 stages not stated | Verified | Verified at iteration 2; condition 3 now also holds over temperature |
| finding-3 | iteration 1 | Major | CK-ANA-E3, E2, A1 | REQ-SYS-022 "nominal PASS"; TPM-005 not named | Verified | Verified at iteration 2; section 8 updated for 2 + 3 + 4 (TPM-005 Red at the filter corner) |
| finding-4 | iteration 1 | Minor | CK-ANA-E4, D4 | Checkers exit 0 on FAIL; constants without ids | Verified | `worst_case.py check r13` exits 1 when the design fails (`design_ok and ok_all`) |
| finding-5 | iteration 1 | Minor | CK-ANA-F3 | Leakage tolerance at nominal only | Verified | Unchanged |
| finding-6 | iteration 1 | Minor | CK-ANA-A2, A3, B2, E5, H2, H3 | Traceability | Open (lien) | (i) to (iv) unchanged (TS-012 revision 4 still cited without `7d0d450`; F7 confidence tag; 1N5711 model identity; `tbr.plan` step); the new temperature rows are traced |
| finding-7 | iteration 1 (Major from iteration 3) | Major | CK-ANA-F1, A5, G7-2, E3 | REQ-SYS-114 not analysed; 2 + 3 + 3 not shown over -10 C to +45 C | Verified | Verification above (run r13, 2 + 3 + 3 withdrawn, 2 + 3 + 4 adopted at 75.37 dB) |
| finding-8 | iteration 1 | Minor | CK-ANA-F3, A5, D3 | Highest J310 gain not analysed; 84.48 dB rounded down | Open (lien) | Unchanged; the r13 isolation figures (89 and 122 dB) use the same 12 dB per J310 |
| finding-9 | iteration 1 | Minor | CK-ANA-D2, I2, B1 | Loss figure, NF plot, typed plot band | Open (lien) | Unchanged |
| finding-10 | iteration 1 | Minor | CK-ANA-G7-1, G1-3 | Mode B box centred on synthesized end capacitors; symmetric stray | Open (lien) | Unchanged; revision 4 adds one more instance (O-7) |
| finding-11 | iteration 2 (label finding-6) | Major | CK-ANA-E3, D2, F4, B6 | Residual limit at the design-input corner | Verified | Verified at iteration 3; revision 4 supersedes the 2 + 3 + 4 limit with the r13 values |
| finding-12 | iteration 2 (label finding-7) | Minor | CK-ANA-F3, E2 | Filter-only corner called the TC-SYS-017 corner | Open (lien) | Unchanged in sections 4.6, 5 and 8 |
| finding-13 | iteration 2 (label finding-8) | Minor | CK-ANA-I2 | r09 and r11 plot defects | Open (lien) | Unchanged |
| finding-14 | iteration 2 (label finding-9) | Minor | CK-ANA-D2, D3 | README r04 row; N = 2,996; r08 JSON provenance; 200-of-1,000 comparison | Open (lien) | Unchanged |
| finding-15 | iteration 3 | Minor | CK-ANA-G7-2, A6 | No guard band in the residual acceptance | Open (lien) | Answered in substance for the design: the 2 + 3 + 4 acceptance is the limit less a +/-0.02 % reading allowance (reviewer: 70.35 dB at +/-0.62 % hot). The author keeps it open for the NanoVNA frequency-accuracy statement of the procedure |
| finding-16 | iteration 3 | Minor | CK-ANA-D3, G7-1 | First-order residual map; alternatives' limits 0.01 % high | Open (lien) | Answered in substance for r13 (exact map; room limits +/-0.95 % and +/-0.67 %, the reviewer's values reproduced to 0.001 dB); r12's stated limits (quoted in section 4.2 findings 3 and 4) and the `tolerance.py` default stay first-order, as note section 9 says |
| finding-17 | iteration 3 re-issue 1 | Minor | CK-ANA-A5, G7-2, F1 | Hot bound is main-bay air, not part temperature; acceptance holds to about +73 C | Open | New finding above |

### Observations (no finding)

- **O-7.** The four-resonator BPF3 end capacitor is synthesized at 4.22 pF and specified as a 4.3 pF C-tolerance part (4.05 to 4.55 pF), while the mode B box is centred on 4.22 pF (3.97 to 4.47 pF): one more instance of finding-10's pattern, which iteration 1 found benign (the specified part is nearer the nominal response). No new finding.
- **O-8.** The after-assembly value "59.0 dB" for the four-resonator BPF3 at 130 MHz is not in any committed result file; the reviewer reproduces 58.95 dB with the frozen solver. As an expected nominal ("at least") it is 0.05 dB optimistic by rounding, the same pattern as the 19.47 and 39.36 dB values it sits beside. Supporting check only.
- **O-9.** The 20 C point of the board sweep (79.80 dB) is below the room case (80.04 dB), because a board at 20 C with an alignment anywhere in 20 to 30 C still drifts; the note's "room" case means the board at its own alignment temperature, which the plot's shaded band shows.
- **O-10.** TS-012's revisit condition X-R6-5 ("INSP-117 iteration 4 ... changes an image or MDS figure") is triggered: the over-temperature image figure TS-012 revision 6 quotes changes (cross item X-R4-1). The change is common to A4 and A5.

### Cross items (returned to Claude as lead SE)

- **X-R4-1 (TS-012 author).** TS-012 revision 6 (`3b93de1`) section 8.14 D-15 reads "residual limit +/-0.97 %" and the section 7.1 risk row "Receiver MDS and image" reads "image about 79.4 dB over temperature" (iteration 3's common-mode estimate). Note revision 4 gives the limit over REQ-SYS-114 as +/-0.64 % with an alignment acceptance of +/-0.62 % at 20 to 30 C, the room limit as +/-0.95 % (exact map), and the image worst case as 75.37 dB hot at the estimate. The ranking does not move (the filter is common to A4 and A5, inside row E5 (a)), but the owner-facing figures should be the note's.
- **X-R4-2 (layout and thermal work packages).** finding-17: where the BPF cells sit on the main board relative to the LM2940 and the feed parts, and a board-over-air allowance for the resonator parts.

### Per-case results (iteration 3 re-issue 1; the REQ-SYS-114 cases revision 4 adds)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-20a | Image, 2 + 3 + 4 at IF 8 (design), design-input corner, +/-0.3 % estimate, board -10 C / +70 C | REQ-SYS-033 over REQ-SYS-114; TC-SYS-021 step 4 | 79.03 / 75.37 dB: PASS | +9.03 / +5.37 dB | coefficient classes (doubled: 77.98 / 70.99 dB), board bound, residual estimate | re-run identical; drift by hand; +80 C 74.37 dB, +90 C 73.37 dB | none |
| C-20b | Same, at the stated limit over temperature +/-0.64 % | as C-20a | 74.05 / 70.01 dB: PASS | +4.05 / +0.01 dB | as C-20a | re-run identical; LTspice image-phase case 70.231 dB against the 70.01 dB bound | none |
| C-20c | Same, at the alignment acceptance +/-0.62 % | as C-20a | not tabulated in the note (derived from C-20b) | reviewer +4.36 / +0.35 dB | board bound | reviewer 74.36 / 70.35 dB; 70.02 dB at +73 C, 69.81 dB at +75 C, 69.27 dB at +80 C | finding-17 |
| C-20d | Image, 2 + 3 + 2 at IF 10, at the estimate, -10 C / +70 C | as C-20a | 71.95 / 70.16 dB: PASS | +1.95 / +0.16 dB | as C-20a | re-run identical | none |
| C-20e | Image, 2 + 3 + 3 at IF 8, at the estimate, -10 C / +70 C | as C-20a | 69.46 / 67.00 dB: FAIL; no residual holds hot | -0.54 / -3.00 dB | as C-20a | re-run identical; confirms and exceeds iteration 3's 69.93 to 69.75 dB | none (finding-7 Verified) |
| C-20f | Board sweep -10 to +70 C at the estimate, all three configurations | nesting (acceptance (c)) | minimum at an end in every row | n/a | none | re-run identical | none |
| C-6r | 2 + 3 + 4 at the alignment temperature, exact map: limit | REQ-SYS-033 corner | +/-0.9596 % (stated +/-0.95 %); 69.823 dB at +/-0.97 % | n/a | as C-20a | reviewer's iteration 3 exact-map values reproduced to 0.001 dB (all three configurations) | finding-16 (lien, r12 values) |

Every other case of the iteration 2 and 3 per-case tables is unchanged at `63122e7` (runs r01 to r12 are not touched by revision 4; the r11 cascade rows for 2 + 3 + 4 existed at iteration 2).

### Checklist answers (iteration 3 re-issue 1, delta)

**A.** A1 Yes: REQ-SYS-114 is named and quoted (section 2), with REQ-SYS-033, TC-SYS-021 and TPM-005. A2 No: finding-6 (i). A3 No: finding-6 (ii), (iii); every new temperature row has a source or "estimate". A4 Yes: KEMET, Coilcraft, the thermal note and REQ-SYS-114 re-read (table above). A5 No: finding-8 (highest gain) and finding-17 (BPF parts assumed at the main-bay air); the other temperature assumptions and their directions are stated. A6 Yes: conditions 3 and 6 and the acceptance go to the J310 stages, the layout and the build notes; the TS-012 handoff is stated (cross item X-R4-1).

**B.** B1 Yes: the nesting argument is stated and the board sweep checks it. B2 No: finding-6 (iii) (the 1N5711 model; not used by r13). B3 Yes: 22 LTspice cases. B4 Yes: 11-point residual grid, bisection to 0.0002 %, 11-point board sweep. B5 Yes: drift, Q, box bounds and BPF3 synthesis by hand; r12 regression; hot-end sensitivity. B6 Yes: the design margin is set against doubled coefficient classes and the residual limit.

**C.** C1 to C5 Yes: re-run above; the wrapper's lock, time-out and version checks passed; blob `88b71475` equal.

**D.** D1 Yes. D2 No: finding-9 (i), finding-14 (a) and (d); every revision 4 value equals the checker. D3 No: finding-8, finding-14 (b), finding-16 (r12 limits still quoted in section 4.2); the r13 limits are rounded down. D4 Yes: `REQ_SYS_033_DB`; the new constants carry their sources (`T_BOARD`, `A_C`, `A_L`, `CU_TC`, `READ_UNC`).

**E.** E1 Yes. E2 Yes, with finding-12. E3 Yes: 2 + 3 + 4 passes with 5.37 dB against stated uncertainties (0.99 dB left with doubled classes); 2 + 3 + 2's 0.16 dB is reported as fragile, not as a robust pass; 2 + 3 + 3 is reported FAIL. E4 Yes: `check r13` exits 1 when the design fails. E5 N/A (no TBR value proposed). E6 Yes: section 8 moves the TPM-005 filter corner to Red for 2 + 3 + 4 and states the MDS is not re-analysed over temperature. E7 Yes.

**F.** F1 Yes: the REQ-SYS-114 cases have rows (cold, hot, sweep); the board bound's meaning is finding-17 (Minor). F2 N/A. F3 No: finding-8, finding-12. F4 Yes: the residual sensitivity per temperature case is tabulated and plotted.

**G1.** G1-1 to G1-4 Yes (one `.ac` per deck; the checker reads the `.raw` through spicelib). **G5.** Unchanged, Yes. **G7.** G7-1 No: finding-10, finding-16 (r12). G7-2 No: finding-15 (the procedure's frequency-accuracy statement), finding-17.

**H.** H1 N/A. H2 Yes: section 8 updates the TPM-005 report and the proposed risk. H3 Yes: section 9 records revision 4 and its code changes.

**I.** I1 Yes: both new plots opened (the committed files), regenerated copies pixel-equal. I2 Yes for r13 (axes and units labelled, the 70 dB line carries REQ-SYS-033 (TBR), the +/-0.3 % estimate marked, the limits as diamonds with their values, the alignment band and the above-ambient band shaded and labelled, plotted values equal `result.md`); No record-wide on finding-13.

## Verdict (iteration 3 re-issue 1, returned by the reviewer)

```
VERDICT: APPROVED (reviewer); record verdict held at NEEDS CHANGES only because the applied analysis template is still only on cr/CR-012
PRODUCT: docs/design/analysis/rx-bpf-ts012.md@11bb9836, hardware/sim/rx-frontend/ worst_case.py, tolerance.py, run_sims.py, README, r13 decks and results as in product_files, at 63122e7
VERIFIED: finding-7 (Major; REQ-SYS-114). Earlier: finding-1, 2, 3, 11 (Major), finding-4, 5 (Minor)
OPEN MAJOR: none
OPEN MINOR (liens, rule C1):
- finding-6, 8, 9, 10 (iteration 1), finding-12, 13, 14 (iteration 2), finding-15, 16 (iteration 3; both answered in substance for the design, kept open by the author)
- [new] finding-17: the +70 C hot bound is the main-bay air, not the BPF part temperature on the main board; the +/-0.62 % acceptance holds to about +73 C (70.02 dB), the verdict at the estimate to beyond +90 C
ITEMS N/A: CK-ANA-E5, F2, H1, G2 to G4, G6 (analysis_kind simulation-deck, cascade, worst-case), J1 to J3 (criticality neither)
VALUES PROPOSED: TPM-005: CBE -140.7 dBm (A5, 2 + 3 + 4), -141.1 dBm (A4), Yellow; Red at the TC-SYS-017 filter corner and the stack (estimates)
MEASUREMENTS: size=3 new decks (22 cases), 1 run (r13), 256 note lines changed; inputs_checked=REQ-SYS-114, KEMET C1003_C0G, Coilcraft 184-1, thermal V18, copper resistivity, stray estimate; renders=2; turns=40; minutes=60; major=0 new (1 Verified); minor=1 new; record-wide 5 Major, 12 Minor, 7 Verified, 10 open (0 Major, 10 Minor)
```

### What the review supports (rule C10)

With finding-7 Verified and no Major open, the review supports: the TS-012 revision 4 filter (2 + 3) fails REQ-SYS-033 at IF 8 MHz; the TS-012 20 % capacitor condition fails for some builds; 2 + 3 + 3 does not hold REQ-SYS-033 over REQ-SYS-114 after a room-temperature alignment (69.46 dB cold, 67.00 dB hot at the estimate) and is rightly withdrawn; **2 + 3 + 4 at IF 8 MHz meets REQ-SYS-033 at the design-input corner over REQ-SYS-114, worst case 75.37 dB (+5.37 dB) at +70 C board and 148.0 MHz tuning with the +/-0.3 % residual estimate, under the six conditions of note section 5**, with a residual limit over temperature of +/-0.64 % and an acceptance of +/-0.62 % that holds for a BPF part temperature up to about +73 C (finding-17); 2 + 3 + 2 at IF 10 passes by only 0.16 dB; REQ-SYS-022 is not shown at the corner in any configuration and the design filter moves the TPM-005 filter corner to Red, which the front-end redesign must recover; neither result separates A4 from A5. Every figure rests on developer evidence (numpy solver checked against LTspice) and on labelled estimates (residual, coil class for the hand-wound coil, stray, board bound).

**Effect on the TS-012 finalists.** None on the ranking. The filter, its extra C0G parts (nine, the top of row E5 (a)) and its MDS penalty are common to A4 and A5, and TS-012 revision 6 already adopts 2 + 3 + 4 (D-15). Only the quoted figures need the note's values (cross item X-R4-1).

## Commands (iteration 3 re-issue 1)

- Search: `mcp__claude-context__search_code` path `/Users/robinonsay/rust/cwht`, the two queries named above.
- Freeze: shell loop over `git rev-parse 63122e7:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (19 files, all equal); `cmp` of the r13 `scripts/` copies against the frozen scripts.
- Re-run: `git archive 63122e7 hardware/sim/rx-frontend tools docs/design/analysis/rx-bpf-ts012.md | tar -x -C <scratchpad>/iter4`; committed r13 folder and r13 decks moved to `author/`; `.venv/bin/python hardware/sim/rx-frontend/worst_case.py prepare r13`; `CWHT_LTSPICE_LOCK_WAIT=5400 .venv/bin/python hardware/sim/rx-frontend/run_sims.py 2026-09-29-r13-bpf-temperature`; `worst_case.py check r13`; deck `cmp`, JSON (parsed, numeric difference), Markdown (byte) and PNG (pixel array) comparisons in Python.
- Independent checks: `<scratchpad>/iter4/rev/drift_check.py` (drift box, coil Q, widening, `Section` bounds, BPF3 synthesis values); `<scratchpad>/iter4/rev/hot_sens.py` (frozen `_r13_value` at +/-0.62 % from -10 to +80 C and at the estimate to +90 C; r12 regression with the default map); `<scratchpad>/iter4/rev/s21_130.py` (after-assembly values); Chebyshev n = 4 synthesis and isolation arithmetic by hand.
- Sources: the KEMET C1003_C0G and Coilcraft Document 184-1 PDFs read with the web-fetch tool at the URLs the note cites, then `pdftotext -layout` on the fetched copies (SHA-256 prefixes above).
- Record check: `.venv/bin/python tools/validate_docs.py` on the repository after the edit.
