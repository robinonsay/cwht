---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-19 receiver band-pass
# filter, image, half-IF and cascade analysis for the TS-012 finalists A4 and A5, iteration 1 at freeze commit
# 7200be7 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Approved 2026-09-28, merge held, template not
# on main). tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-design revision B and checklist_analysis records the template actually applied, as
# INSP-056, INSP-113 and INSP-114 did. The delta iteration after CR-012 merges switches the field.
# id: the brief assigned no id. INSP-117 is the next id above every id on main (HEAD 7200be7), on every cr/ branch
# and in the working tree at the time of filing (highest in use INSP-114); the lead SE reassigns it if a parallel
# review (for example of the WP-PDR-21 LPF or WP-PDR-22 keying notes) took the same number.
# Filing: the harness refused the reviewer's Write of this new file ("Subagents should return findings as text");
# the reviewer returned this text for the lead SE to file.
# Filed by the lead SE on 2026-09-28 from the reviewer's own final text (its validated scratch copy; the harness refused
# the reviewer's Write of this new file, "Subagents should return findings as text"). Content is verbatim except the
# id, reassigned from INSP-115 (already taken by the LPF record, 06b91e3) to INSP-117.
id: INSP-117
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-rx-bpf-ts012.md
product: docs/design/analysis/rx-bpf-ts012.md
# product_commit: 7200be7, the WP-PDR-19 rx-frontend commit. Every blob below equals git rev-parse 7200be7:<path>,
# git rev-parse HEAD:<path> and git hash-object <path> at HEAD 7200be7 on 2026-09-28 (76 files). The run copies of
# the scripts in results/*/scripts/ are byte-identical to the block scripts (cmp). The .raw and .log files are
# reviewed through the reviewer re-run and are not listed.
product_commit: "7200be7f96662c0f987fb1cd8ec8f6df1a1a1b8d"
product_files: ["docs/design/analysis/rx-bpf-ts012.md@5c60b9670c2c54c0565cb9d0c4c5d73acfa517e4", "hardware/sim/rx-frontend/README.md@a1f72599fa13ab35c57b2aa02a78519450130ad7", "hardware/sim/rx-frontend/bpf_design.py@bb3e7e566f8146a5d53a295f5788f8ceac7297cb", "hardware/sim/rx-frontend/make_decks.py@293a310000eb31e3da7904086253dc6818c76244", "hardware/sim/rx-frontend/run_sims.py@557ad0ee0d8e4a9e358e140b2397c6427cf80940", "hardware/sim/rx-frontend/check_bpf.py@962ebe124747d0cdfbb45e6b3c6a05b9d68128a2", "hardware/sim/rx-frontend/check_halfif.py@63fd8097850bada6a42f82b18f0c919e58d43ac5", "hardware/sim/rx-frontend/cascade.py@159485a56f23f892ea093d70b8e6465bcbebc577", "hardware/sim/rx-frontend/explore.py@dda9fea4c5a94337296cad834bda67cad9837145", "hardware/sim/rx-frontend/decks/bpf_2p3_bw5.net@99948f4c82e4a968993709a393b17d4abf1c7b4f", "hardware/sim/rx-frontend/decks/bpf_2p3_bw6.net@15df381df011be8532c8d8a9623411ca9004c8ec", "hardware/sim/rx-frontend/decks/bpf_2p3_bw6_mcA.net@d6fa27f573c00d1f801e75b2488ed6d51aee1046", "hardware/sim/rx-frontend/decks/bpf_2p3_bw6_mcA_draws.npz@c4a0ec937444e7cf1817cb623e64350abe836eac", "hardware/sim/rx-frontend/decks/bpf_2p3_bw6_mcB.net@ca849d69a042602384a09a0ef0fbc53405057fa3", "hardware/sim/rx-frontend/decks/bpf_2p3_bw6_mcB_draws.npz@27e31c15408fcbd668cf42e5ba54da161d20ac4e", "hardware/sim/rx-frontend/decks/bpf_2p3p2_bw6.net@75046cc0b0eaf92a878208a7e7e180218670af19", "hardware/sim/rx-frontend/decks/bpf_2p3p2_bw6_mcA.net@02e9ce359f7ea3d8ee453294e7f7717f04e902fd", "hardware/sim/rx-frontend/decks/bpf_2p3p2_bw6_mcA_draws.npz@95bcc3050ecff88d2314a73b43bb26135c9c3614", "hardware/sim/rx-frontend/decks/bpf_2p3p2_bw6_mcB.net@98bb095311e742ff86e50a62670c2ab58c7ffcba", "hardware/sim/rx-frontend/decks/bpf_2p3p2_bw6_mcB_draws.npz@a893d508560a808517e04d3084c3423de38d2ea7", "hardware/sim/rx-frontend/decks/bpf_2p3p3_bw6.net@6d270dfa36a6124b6284c3ef8a53cd2d6bd5faa9", "hardware/sim/rx-frontend/decks/bpf_2p3p3_bw6_leak.net@3636f754b8e190e9b79d72f36b82590ec8b8496a", "hardware/sim/rx-frontend/decks/bpf_2p3p3_bw6_mcA.net@bf8502681d737c0227a8150652a0b00a3c5a0f14", "hardware/sim/rx-frontend/decks/bpf_2p3p3_bw6_mcA_draws.npz@c4373edfbad7f088867707c5e122efdb3738d486", "hardware/sim/rx-frontend/decks/bpf_2p3p3_bw6_mcB.net@46184fc91fe01a306868313bafa3744a6936b272", "hardware/sim/rx-frontend/decks/bpf_2p3p3_bw6_mcB_draws.npz@c240494fe42716567da1d5e314360fbe758eaa57", "hardware/sim/rx-frontend/decks/halfif_jfet_c01.net@83c98fb779acf74b56b9319d14e6db7249143d22", "hardware/sim/rx-frontend/decks/halfif_jfet_c02.net@f2bf12a4960d2dbc7ec22b3806eff6ddcf9789c6", "hardware/sim/rx-frontend/decks/halfif_jfet_c03.net@9ceeb00d39ed686ad18010ef2d7a73dd728f232c", "hardware/sim/rx-frontend/decks/halfif_jfet_c04.net@1ab8155aba61e432812e167d68a980f9b5dd0473", "hardware/sim/rx-frontend/decks/halfif_jfet_c05.net@48694d796c2f32ea194c2f65796ad992fce11df1", "hardware/sim/rx-frontend/decks/halfif_jfet_c06.net@1331b31999c693419869908a97e28050c75969ed", "hardware/sim/rx-frontend/decks/halfif_jfet_c07.net@c7b85d986db1b8ff991a544e9e41238a092f0b9c", "hardware/sim/rx-frontend/decks/halfif_jfet_c08.net@cc17e2f8b2325167cc833495c44ac612dd91a61b", "hardware/sim/rx-frontend/decks/halfif_jfet_c09.net@c10783021019e28dec4909f6d70c5e9dba12db3d", "hardware/sim/rx-frontend/decks/halfif_jfet_c10.net@7d30447ef87848162d7191fd3af3a086ff555eb1", "hardware/sim/rx-frontend/decks/halfif_jfet_c11.net@3a03c1b89b3e085cd6fc2afbb1594219bf1e50f2", "hardware/sim/rx-frontend/decks/halfif_jfet_c12.net@c8d09ed825df65d90dfc96b26a219a4d06a5fe22", "hardware/sim/rx-frontend/decks/halfif_jfet_c13.net@b79668cefdb181c7523dc634f0bbd92a6d4c5fb0", "hardware/sim/rx-frontend/decks/halfif_jfet_c14.net@36ba23fae364cf050cc3220fb8dcb2554145a900", "hardware/sim/rx-frontend/decks/halfif_jfet_c15.net@d5087731b5fe8c0b1dd81db5d02788d186ef900e", "hardware/sim/rx-frontend/decks/halfif_jfet_c16.net@c94e3149de3e29dc1e93685d98e023545d36f235", "hardware/sim/rx-frontend/decks/halfif_jfet_cases.json@dd2ceb4b103c98ef3bbdd1832d575cfce135d983", "hardware/sim/rx-frontend/decks/halfif_ring.net@675ae78064e7d750c7907524bc68ebae793831fe", "hardware/sim/rx-frontend/decks/halfif_ring_cases.json@be6c1ea444c469b558577b3ac36ca155b93ca791", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/bpf_2p3_bw5_passband.png@5a2e0de713d7f5995059e3bc7296b08706d85792", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/bpf_2p3_bw5_s21_image.png@5d691941c874bc377032ade939f5138dd51bbac4", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/bpf_2p3_bw6_mcA_montecarlo.png@65577576725a1e83c63ee2d893b374a986ef2fc1", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/bpf_2p3_bw6_mcB_montecarlo.png@5b94943252505c25b0e9f7dc9fe92ce5cafa7ed6", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/bpf_2p3_bw6_passband.png@4fd1b8448883f24f6e51bb781516eb1e67d3cfd8", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/bpf_2p3_bw6_s21_image.png@fb15271a75894e403d2e21f116bfb1c1981dfd89", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/result.json@4cc92fbafb5ca1514b5815629bee26e4a173b557", "hardware/sim/rx-frontend/results/2026-09-28-r01-bpf-ts012-baseline/result.md@4118b478345ff429b3eaf16c11d86493137ff1f8", "hardware/sim/rx-frontend/results/2026-09-28-r02-bpf-three-section/bpf_2p3p2_bw6_passband.png@50aedec433fecca488caea7dcc45944df4475dc1", "hardware/sim/rx-frontend/results/2026-09-28-r02-bpf-three-section/bpf_2p3p2_bw6_s21_image.png@edef2e5d7a708ba829bde57f91449fa04ded6486", "hardware/sim/rx-frontend/results/2026-09-28-r02-bpf-three-section/bpf_2p3p3_bw6_passband.png@b1b019f4a43b2bd085e1a268d74089bccbbcf521", "hardware/sim/rx-frontend/results/2026-09-28-r02-bpf-three-section/bpf_2p3p3_bw6_s21_image.png@e6cd45b306594f0ab9961c7f7ef302cbd3f004c4", "hardware/sim/rx-frontend/results/2026-09-28-r02-bpf-three-section/result.json@7b746f48a58ad38859953150ea0866b04f1967b3", "hardware/sim/rx-frontend/results/2026-09-28-r02-bpf-three-section/result.md@455963c8d84aba072b896e38e6aa91c675b35490", "hardware/sim/rx-frontend/results/2026-09-28-r03-bpf-three-section-mc/bpf_2p3p2_bw6_mcA_montecarlo.png@a500d819937037d040160a0c44859483d0824435", "hardware/sim/rx-frontend/results/2026-09-28-r03-bpf-three-section-mc/bpf_2p3p2_bw6_mcB_montecarlo.png@ba8d6abebf14753ab7eea5974a0367b1247bfbb4", "hardware/sim/rx-frontend/results/2026-09-28-r03-bpf-three-section-mc/bpf_2p3p3_bw6_mcA_montecarlo.png@f5bd6580c5e3312d67e355ce07f5f1a1466682d6", "hardware/sim/rx-frontend/results/2026-09-28-r03-bpf-three-section-mc/bpf_2p3p3_bw6_mcB_montecarlo.png@2d700ffccd9900d865e1175b0c4b32300af5e24f", "hardware/sim/rx-frontend/results/2026-09-28-r03-bpf-three-section-mc/result.json@8afeb989c1e7bb8b489e3938a7c6d2c0be3b943f", "hardware/sim/rx-frontend/results/2026-09-28-r03-bpf-three-section-mc/result.md@3042e9771f89375a4d08d04b889d08f8c8a340bd", "hardware/sim/rx-frontend/results/2026-09-28-r04-bpf-leakage/bpf_2p3p3_bw6_leak_leakage.png@a960f59f4c51b179c87008197c8ce9d46596ee17", "hardware/sim/rx-frontend/results/2026-09-28-r04-bpf-leakage/result.json@46133f741f7081e3fbd914292d54ce28fee5360b", "hardware/sim/rx-frontend/results/2026-09-28-r04-bpf-leakage/result.md@2881e480ba6044dbb40bb48102cf1c61923249c2", "hardware/sim/rx-frontend/results/2026-09-28-r05-halfif-mixers/halfif_jfet_halfif.png@c4d7ed75e5cc209f460426cf57a331dc8c13dd3a", "hardware/sim/rx-frontend/results/2026-09-28-r05-halfif-mixers/halfif_ring_halfif.png@e164b2f23c2973b5070cbcb19b4e11fb19670f8d", "hardware/sim/rx-frontend/results/2026-09-28-r05-halfif-mixers/result.json@f43b886eebfd649c965095426e461221a163f991", "hardware/sim/rx-frontend/results/2026-09-28-r05-halfif-mixers/result.md@55eea70e23339af093cdd946441a6b18ce421179", "hardware/sim/rx-frontend/results/2026-09-28-r06-cascade/cascade_nf_gain.png@9d374f5668b926aaa91c0307704f410ea66c7835", "hardware/sim/rx-frontend/results/2026-09-28-r06-cascade/cascade_verdicts.png@a2da702aad59f95bf823f9ee9cdcea032a5ad86f", "hardware/sim/rx-frontend/results/2026-09-28-r06-cascade/result.json@d663ddba0ad4d2a5b0bb8a58418cf4009c427afa", "hardware/sim/rx-frontend/results/2026-09-28-r06-cascade/result.md@8613b02b0fc1a9123ca6cba5a55c8512ec540a86"]
analysis_kind: [simulation-deck, cascade, worst-case]
product_size: 1 note (267 lines, 7 sections); 7 scripts; 29 LTspice decks (4 Q-sweep, 6 Monte Carlo of 200 runs, 1 leakage of 8 steps, 1 ring of 21 steps, 16 JFET cases); 6 runs; 19 renders (11 cited); 14 input rows
tools_used: ["LTspice 26.0.2 for MacOS through tools/ltspice-batch.sh blob 88b71475 (TV-014, Accredited, ACC-LTSPICE-001)", "venv Python 3.13.5 (TV-001 accredits the interpreter); numpy 2.5.3, scipy 1.18.1, spicelib 1.6.3, matplotlib 3.11.2 (class B entries of tools/toolchain.lock.md section 2 without a TV record); no TV record covers hardware/sim/rx-frontend/*.py: developer evidence per 05 section 9.1, as the note says"]
# values_proposed: note section 5 "Requirement change": REQ-SYS-033 kept at 70 dB (TBR); the 45 dB relaxation is
# named only as the consequence of declining BPF3 and is not recommended. The replacement TS-012 criteria and the
# 85 dB isolation are TS-012 and PCB design inputs, not requirement or TPM values.
values_proposed: ["REQ-SYS-033: 70 dB"]
renders_inspected: 19
sprint: PDR-prep
author_agent: "author:WP-PDR-19 rx-frontend (Claude as analysis author, TS-012 discriminating analyses; commit 7200be7)"
reviewer_agent: "reviewer:WP-PDR-19-analysis-rx-bpf-iter1 (independent; authored no part of the note, decks, scripts, TS-012 or the other TS-012 analyses)"
# criticality: a hardware-only receive analysis; it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
# verdict (rule C1, iteration 1): three Major findings are open, so NEEDS CHANGES. Iteration 2 is a delta that
# verifies the Major fixes only; Minor findings raised after the first APPROVED verdict become liens due at the CDR
# readiness declaration.
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 7
findings_open: 10
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A1, CK-ANA-A2, CK-ANA-A3, CK-ANA-A5, CK-ANA-B1, CK-ANA-B2, CK-ANA-B6, CK-ANA-D2, CK-ANA-D3, CK-ANA-D4, CK-ANA-E2, CK-ANA-E3, CK-ANA-E4, CK-ANA-E5, CK-ANA-F1, CK-ANA-F3, CK-ANA-G1-3, CK-ANA-G7-1, CK-ANA-G7-2, CK-ANA-H2, CK-ANA-H3, CK-ANA-I2]
effort_turns: 60
effort_minutes: 110
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
