---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-20 transmit clock
# spur plan for the TS-012 finalists (the pre-order item added by TS-012 revision 4, adversarial R-3). Iteration 1
# at freeze commit 09fae14 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates, blob 0386cc6e; CR-012 Approved 2026-09-28, merge held, template not on
# main). tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-design revision B (SEMP section 7.2 design analyses) and checklist_analysis records
# the template actually applied, as INSP-056, INSP-071 and INSP-083 did. The delta iteration after CR-012 merges
# switches the field to peer-review-checklist-analysis.
# id: the brief assigned no id. INSP-113 is the next id above every id on main (HEAD 09fae14) and on every cr/
# branch (highest INSP-111) at the time of filing.
# Filed by the lead SE on 2026-09-28 from the reviewer's own text: the harness refused the reviewer's Write of this
# new file ("Subagents should return findings as text"). Content is verbatim except the id, reassigned from
# INSP-112 to INSP-113 because three parallel reviewers (review:spurs-1 among them) each took INSP-112 as the next free id.
# Iteration 2 (delta, rule C1) at 5a36ecd by review:spurs-2; the harness refused that reviewer's Write, so the lead SE
# filed it from the returned text (front matter changes and the section below verbatim; its superseded early Write,
# which treated the record as unfiled, was not used).
id: INSP-113
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch)"
checklist_file: docs/reviews/PDR/checklists/analysis-spurs-ts012.md
product: docs/design/analysis/spurs-ts012.md
# product_commit: 09fae14, the author's commit of the note, decks, checker and run txspur-20260928-01. Every blob
# below equals git rev-parse 09fae14:<path> and git rev-parse HEAD:<path> at HEAD 09fae14 on 2026-09-28. The run
# copies of the decks and the script in results/txspur-20260928-01/ are byte-identical to the block copies (cmp).
product_commit: "5a36ecdd98aae78cd8c228ebabd368f50d632e11"
product_files: ["docs/design/analysis/spurs-ts012.md@3fc2ec4bff5e94d86c2db3ca22c76442ac83aa81", "hardware/sim/freq/tx_spur_plan.py@d123168d8bf4d198fee2a26060efaa33df00778f", "hardware/sim/freq/tx_spur_filters.cir@c647c60aafb0ad53f742f151f0442a698b6d671d", "hardware/sim/freq/tx_spur_bpf_tol.cir@b0f27d7a5990cc2ca086b3fb10e26620108d6e42", "hardware/sim/freq/tx_spur_c7_tap.cir@f68aa95f433a54a44078aa59b1cb6c09af40757d", "hardware/sim/freq/tx_spur_c7_iso.cir@ae5990f64ad6c0d0eb8be669fbe8bda1f62adfde", "hardware/sim/freq/tx_spur_trap.cir@d7f58e40eae198490a3a549fa4f9e03f5aebc15c", "hardware/sim/freq/README.md@4ebdde90fe8908d09c691eef5f782373f2633619", "hardware/sim/freq/results/txspur-20260928-02/results.json@3ce6186f5186f682e31daae862c6ea9410942227", "hardware/sim/freq/results/txspur-20260928-02/lines.csv@0af7ceb34eb987372a99eacc19f5a3c20fd56da6", "hardware/sim/freq/results/txspur-20260928-02/checker-output.txt@63990681082ceca38cfec978c1f91edf8089fa86", "hardware/sim/freq/results/txspur-20260928-02/spectrum-gva-A5-144.050.png@d30eac14a45e0b043409451fdf3b99fde29995f0", "hardware/sim/freq/results/txspur-20260928-02/spectrum-gva-A4-144.050.png@3c324558c7aa1cd186cf59e19558cb93390c931e", "hardware/sim/freq/results/txspur-20260928-02/antenna-P-PB-144.050.png@a0c398597e384768d969113df624435eefea8589", "hardware/sim/freq/results/txspur-20260928-02/antenna-P-PB-147.950.png@4978b0957baf504cf05c4ef48136d83941ad0b7b", "hardware/sim/freq/results/txspur-20260928-02/worst-line-vs-carrier.png@b8b78226c4361764d4717860a3868b29b51ae885", "hardware/sim/freq/results/txspur-20260928-02/filters.png@d5fb6ac9532e2dd8063db429a30f8a4aed8435f8", "hardware/sim/freq/results/txspur-20260928-02/c10-tolerance.png@6089d2710a2d811c5326dea001bcbe9ea2b5c955", "hardware/sim/freq/results/txspur-20260928-02/c7-prescaler-tap.png@9d8a247d55fd01b6a431e81322151812488edf75", "hardware/sim/freq/results/txspur-20260928-02/t1-trap.png@f2f2e13965933a97cc6babe0e9e368a012a3c265"]
product_files_iteration_1: ["docs/design/analysis/spurs-ts012.md@da3b058a9bd259fff3be8e49146bb6953670083f", "hardware/sim/freq/README.md@a64704b0fa562737fea91479cd0599e91c3eef29", "hardware/sim/freq/tx_spur_plan.py@b6432663bc287423466f573f3409b65203da3efc", "hardware/sim/freq/tx_spur_filters.cir@c647c60aafb0ad53f742f151f0442a698b6d671d", "hardware/sim/freq/tx_spur_bpf_tol.cir@b0f27d7a5990cc2ca086b3fb10e26620108d6e42", "hardware/sim/freq/results/txspur-20260928-01/results.json@b80df7b71106018d1b0a2f149cc47816a9454344", "hardware/sim/freq/results/txspur-20260928-01/lines.csv@79c6a473c8e98171ebdef05e3643b59b370f0395", "hardware/sim/freq/results/txspur-20260928-01/spectrum-gva-A5-144.050.png@3c90224f94a8ac09375d4a9629a4a790e921c840", "hardware/sim/freq/results/txspur-20260928-01/spectrum-gva-A4-144.050.png@bcbb4b8f8726c9dd886b7d34c7f039dec911e887", "hardware/sim/freq/results/txspur-20260928-01/antenna-PB-144.050.png@712902bf36bafe38622953a5cb377e30c3b23605", "hardware/sim/freq/results/txspur-20260928-01/antenna-PB-147.950.png@44b6cda6e4e01df333a591749448b142300e12d4", "hardware/sim/freq/results/txspur-20260928-01/worst-line-vs-carrier.png@98d9ac60caeeaced3ae1053ff80e7d0ace3a2b3b", "hardware/sim/freq/results/txspur-20260928-01/filters.png@d5fb6ac9532e2dd8063db429a30f8a4aed8435f8", "hardware/sim/freq/results/txspur-20260928-01/c10-tolerance.png@6089d2710a2d811c5326dea001bcbe9ea2b5c955"]
analysis_kind: [simulation-deck, budget, worst-case, other]
product_size: 1 note (248 lines, 10 sections), 2 LTspice decks (5 filter circuits; 25 tolerance corners), 1 checker (899 lines), 4 plans x 2 finalists x 3 carriers plus a 200-carrier sweep, 1739 CSV rows, 7 plots
tools_used: ["LTspice 26.0.2 through tools/ltspice-batch.sh blob 88b71475 (TV-014, accredited ACC-LTSPICE-001; .log first line 'LTspice 26.0.2 for MacOS')", "venv Python 3.13.5 with numpy 2.5.3, matplotlib 3.11.2, spicelib 1.6.3 (class B lock entries; TV-001 does not cover hardware/sim/freq/tx_spur_plan.py; developer evidence per 05 section 9.1, as the note states)", "LTspice decks tx_spur_c7_tap, tx_spur_c7_iso, tx_spur_trap (revision 1)"]
# values_proposed: the note proposes no TBR value of a REQ-, TPM- or HZ- id. It proposes derived design limits
# (Si5351 150.000 MHz line at most -60 dBc at the CLK1 pin; VGG PWM ripple at most 3.3 mV peak) and design changes
# C1 to C10, T1, L1 to L5, F1, F3 as requests to other WPs (note sections 6 and 9); they are not TBR values.
values_proposed: []
renders_inspected: 9
sprint: PDR-prep
author_agent: "author:WP-PDR-20 transmit clock spur plan (Claude as analysis author, commit 09fae14)"
reviewer_agent: "reviewer:WP-PDR-20-spurs-ts012-iter1 (independent; authored no part of the note, its decks, its checker, TS-012 or ADR-031); iteration 2 by reviewer:WP-PDR-20-spurs-ts012-iter2 (review:spurs-2; independent; authored no part of revision 0 or 1, TS-012, ADR-031 or the WP-PDR-21 notes)"
# criticality: a transmitter spur analysis on preliminary design data. It sets no value of a 07 section 14.1
# component: the firmware clock settings C1 to C6 are routed as requests to WP-PDR-32 and WP-PDR-35 (note
# section 9 item 3), where they are reviewed with the component they constrain
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
# reviewer_verdict: NEEDS CHANGES, two Major findings (finding-1, finding-2) open (plan rule C1: Majors block)
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict held at NEEDS CHANGES only until the CR-012 merge (lead SE convention of 2026-09-27)
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 10
findings_open: 10
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A4, CK-ANA-A6, CK-ANA-D2, CK-ANA-D3, CK-ANA-F3, CK-ANA-G1-3, CK-ANA-G1-4, CK-ANA-G7-1, CK-ANA-H1, CK-ANA-H2, CK-ANA-I2]
effort_turns: 100
effort_minutes: 145
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record INSP-113: transmit clock spur plan for the TS-012 finalists (iteration 1)

**Product.** `docs/design/analysis/spurs-ts012.md` (`da3b058a`) with the block README (`a64704b0`), the checker `hardware/sim/freq/tx_spur_plan.py` (`b6432663`), the LTspice decks `tx_spur_filters.cir` (`c647c60a`) and `tx_spur_bpf_tol.cir` (`b0f27d7a`), the run `hardware/sim/freq/results/txspur-20260928-01/` (`results.json` `b80df7b7`, `lines.csv` `79c6a473`, seven PNG files), all at freeze commit `09fae14` on `main` (rule C2). Every blob equals `git rev-parse HEAD:<path>` at `HEAD` `09fae14`. No product blob lives on a `cr/` branch. The note is AT RISK on TS-012 revision 4 and ADR-031 (both Proposed), as its header says.

**Checklist.** The item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` simulation-deck (the two filter decks), budget (the spur budget per line), worst-case (the C10 tolerance corners) and other (the line inventory): sections A to F, G1, G2, G7, H, I. G3 to G6 and J are N/A.

**Governing criterion and cases (rule C7).**
- TS-012 revision 4 section 7.3 (`7d0d450`), pre-order check (WP-PDR-20 transmit clock-plan item): "list every clock running in transmit with its lines from 118 to 175 MHz ...; reconcile the transmit clk_sys with ADR-031 (125 against 150 MHz ...); choose how the ADC runs in transmit ...; and give each line an estimated coupled level at the GVA-84+ input. **Pass: every line at most -68 dBm at the GVA-84+ input (estimate), or a layout, clock or firmware change named for it.**" A4 "has the same clock plan and takes the same item".
- Budget figures quoted from the same paragraph: 25 uW is -16 dBm at the SMA; about 45 dB from the GVA-84+ input to the SMA; limits about -61 and -68 dBm at the GVA-84+ input.
- REQ-SYS-017 (`docs/requirements/sys/requirements.md`): "every antenna-port spurious emission at most 25 uW at all power steps, carrier frequencies and 6.4 to 8.4 V pack voltages"; verification carriers 144.05, 146.00 and 147.95 MHz. REQ-SYS-018: "at least 60 dB (TBR) below the mean carrier power at the 5 W step". 47 CFR 97.307(e) as REQ-SYS-017's rationale quotes it (25 uW and 40 dB for 25 W or less, 30 to 225 MHz; 25 uW is the tighter bound at 5 W).

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (analysis checklist and rule C1; REQ-SYS-017 spurious limit) preceded every `grep`; `grep` only pinned lines in TS-012, the INSP-110 record, the toolchain lock and TV-014. The rustos tree was not read. External reads (2026-09-28, public pages, no login or form): the Nexperia 74LVC1G80 datasheet Rev. 17 (12 November 2024) at https://assets.nexperia.com/documents/data-sheet/74LVC1G80.pdf (read through the web-fetch tool, which cached the PDF; pages 5 to 9 inspected); the pico-sdk register header https://raw.githubusercontent.com/raspberrypi/pico-sdk/master/src/rp2350/hardware_regs/include/hardware/regs/clocks.h; https://www.pa3fwm.nl/technotes/tn42b-si5351-analysis.html; https://github.com/pavelmc/arduino-arcs/blob/master/Si5351_issues.md; a web search for the Coilcraft 1812SMS-47N tolerance codes (https://www.coilcraft.com/en-us/products/rf/air-core-inductors/midi-spring/1812sms/1812sms-47n/, Mouser 1812SMS-47NGLB listing).

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-E3, CK-ANA-E4 | note sections 4.2 (table, TS-012 criterion column), 5 (verdict per finalist), 6 row T1; `tx_spur_plan.py` lines 182 to 199 (`CHANGE`), 824 to 856 (`unnamed`, `ts012_criterion`) | The note reports "PASS on the TS-012 7.3 criterion" for A5 and A4 (plans P and PB), and the checker exits 0, while its own high estimates leave 4 to 6 lines (PB) and 8 to 10 lines (P) over the 60 dBc target and 1 (PB) or 2 (P) lines over the 25 uW legal limit (150.000 MHz at -12.1 dBm in PB; 125.000 and 150.000 MHz up to -11.2 dBm in P). The margins run from -4 to +22 dB against a 20 to 50 dB estimate range. The criterion is met only by its wording "a change named for it", and the checker counts any non-empty change string with kind "level" as a named change. For the residual lines the named change does not lower the estimate: "ref" reads "cannot be moved ... F1 ... tinySA sweep" (F1's effect "not quantified", note 6); "frac" names C5, which fixes the spur offset (at least 50 kHz from the carrier) but not its level; L4 treats only the TCXO lead, not the on-die feedthrough that the note calls dominant. The one fallback that could hold 150 MHz, trap T1, is not shown to be feasible. Reviewer hand calculation (series-LC shunt trap at 150 MHz on a 50 ohm drive-chain node, inductor Q 60 to 100, L 20 nH to 2.2 uH): the 11 dB at 150 MHz needed to bring -12.1 dBm to -23 dBm costs 4.0 to 4.1 dB of carrier at 147.99 MHz (L = 1 uH, C = 1.13 pF, impractical values). Even the 4 dB needed for 25 uW costs about 1.7 to 1.9 dB (L = 2.2 uH). Both fall inside the 0.4 dB drive window of finding-5, so T1 is not a usable fallback as sized. Checklist rule E3: a case whose margin is not larger than its uncertainty must not be reported as passing. **Fix:** (a) report the TS-012 7.3 result per finalist as "criterion met by wording only: named changes lower or move every line except N residual lines (listed), which are not shown against 60 dBc (and one against 25 uW) and rest on the bench sweep". Do not write PASS. (b) In the checker, separate "moves or lowers, credited in the numbers" from "named but not credited", and make the exit status and `results.json` report the residual lines. (c) Either size T1 with its carrier loss at 147.99 MHz against the module drive window, or withdraw it as the fallback and say that the 150 MHz line has no pre-built fallback. (d) Carry the residual lines to section 8 as open items for the owner's order decision. | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-A4, CK-ANA-A6, CK-ANA-B1, CK-ANA-F4 | note section 6 row C7; `tx_spur_plan.py` lines 394 to 401 (`iso = db20((330.0 + 25.0) / 25.0)`) | C7 (330 ohm in series after the 100 pF tap) earns the 23 dB kickback credit that takes plan P from B0's -0.4 dBm to -11.2 dBm. The note does not check that the 74LVC1G80 still receives a valid clock through 330 ohm. Nexperia 74LVC1G80 Rev. 17, Table 7 at VCC 2.7 to 3.6 V: VIH at least 2.0 V, VIL at most 0.8 V, so a swing of at least 1.2 V (0.6 V peak) centred on the bias is needed; CI is 5 pF typical. fmax 160 MHz is specified with a rail-to-rail CP input (Fig. 5, Table 9). Reviewer hand calculation: CLK1 fundamental 0.89 to 1.05 V peak (+9 to +10.4 dBm into 50 ohm, TS-012 7.3). Through 330 ohm and 100 pF into 5 to 6 pF (CI plus pad and trace), the input sees 0.48 to 0.55 of that, so 0.43 to 0.58 V peak, under the 0.6 V peak minimum at every corner. The present plain tap gives about 0.84 to 0.99 V peak. C7 as proposed therefore risks the REQ-SYS-182 counter. The P result depends on it: re-running the checker at `09fae14` without the C7 credit (reviewer scratch copy) gives a P worst line of -3.9 dBm for A5 and for A4 (126.044 MHz, 7/8 fc), against -11.2 and -11.7 dBm. PB moves only from -12.1 to -11.7 dBm, because C10 rejects 7/8 fc; 9/8 fc at 162 MHz then leads. **Fix:** size the series element (value, or a buffer or attenuator plus comparator) against the 74LVC1G80 input thresholds and fmax conditions at the low CLK1 corner, credit only the isolation that design gives, and send the prescaler input-level check to WP-PDR-21 with REQ-SYS-182 named as the affected requirement. State P's sensitivity to C7 (F4). | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-A4 | note section 3 row "Si5351 PLL spurs"; `tx_spur_plan.py` line 365 | The source quoted for the fractional-spur range (-80 to -60 dBc, "PA3FWM tn42b: about -80 dBc in theory") does not apply as used. The page derives about 80 dB from a 3.125 ps multisynth phase-interpolation error at a 30 MHz output (VCO 625 MHz) and says lower output frequencies do better. By the same method, a 144 MHz output is about 20 log(144/30) = 13.6 dB worse, near -66 dBc. The design uses an integer divide-by-6 multisynth with a fractional PLL (TS-012 7.3 "Frequency plan"), a spur mechanism the page does not quantify, and it gives no bound for "significantly worse" in practice. The high end of -60 dBc therefore has no source. It decides whether fc +/- 0.5 MHz sits "at the limit" (-23.0 dBm) and whether PB has one or more lines over 25 uW. **Fix:** state the corrected basis, label the high end as unbounded by any source (or widen it with a stated reason), and add the close-in fractional spurs to the residual list of finding-1. The derived -60 dBc bound at the CLK1 pin (note 4.2) already covers them. | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-G7-1, CK-ANA-G1-4 | `tx_spur_bpf_tol.cir` lines 3 to 7 and 11 to 12; `tx_spur_plan.py` lines 689 to 692, 681 to 682; note section 6 row C10; README line 38 | (a) The tolerance deck scales every inductor by one kl and every capacitor by one kc, so it never detunes one resonator against the other or moves the coupling capacitor on its own. (b) "2 % C0G" cannot be bought for 2.4 pF and 7.5 pF parts, which are sold with absolute tolerances (B +/-0.1 pF, C +/-0.25 pF). The 1812SMS-47N is sold in G (2 %) and J (5 %) tolerance (Coilcraft product page), so the inductor premise holds. (c) The checker assumes `.step` order "kl outer, kc inner", but LTspice steps kl fastest: the raw file's step 2 is `{'kl': 0.98, 'kc': 0.95}` (spicelib `raw.steps`), which `results.json` labels kl 0.95, kc 0.98. Every asymmetric corner label is transposed. The 2 % set is symmetric, so pass or fail is unchanged. (d) A missing `tx_spur_bpf_tol.raw` is skipped silently with the overall result still PASS, and no raw file is checked for staleness against its deck. (e) The README says "nine tolerance corners"; the deck runs 25. (f) The note says C10 is centred "at about 146 MHz"; its nominal peak is at 148.0 MHz and its 3 dB band is 137.7 to 158.6 MHz (reviewer ABCD calculation, which matches LTspice). **Reviewer independent check (ABCD, all seven parts independent at their extremes, 128 corners):** L 2 %, 16 pF 2 %, 7.5 pF and 2.4 pF +/-0.1 pF: passband deviation 0.83 dB, 125 MHz rejection 14.5 dB; the same with +/-0.25 pF: 1.46 dB and 13.1 dB; with +/-0.1 pF and 0.3 pF of pad capacitance per resonator: 0.72 dB and 13.7 dB. The C10 conclusion holds. **Fix:** independent corners (or a seeded Monte Carlo) in the deck; purchase tolerances as sold (for example 2.4 pF B, 7.5 pF B, 16 pF G); read the step values from `raw.steps`; fail on a missing or stale raw file; correct the README and the centre-frequency wording. | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-A6 | note sections 2 item 3 ("drive filter and 18 dB pad 19.6 dB"), 6 row C10 ("the module drive is unchanged"); `tx_spur_bpf_tol.cir` lines 6 to 8 | The note's own figure of 19.6 dB for the drive filter and pad (LTspice: the 3-pole Butterworth loses 1.4 to 1.6 dB at 144 to 148 MHz) differs from TS-012 7.3's module-drive derivation. That derivation counts only the 18 dB pad and gives 10.5 to 14.4 dBm (11 to 28 mW). With 19.6 dB the low corner is 9 - 19.6 + 22.5 - 3 = 8.9 dBm (7.8 mW), under the module's 10 mW stability condition, before any C10 tolerance. At the 25 ohm corner the high end is 15.3 dBm (34 mW). The C10 deck's criterion ("within 3 dB of nominal, so the module drive stays inside 10 to 30 mW after the pad trim") therefore has no margin behind it. Section 8 item 3 does send the 10 to 30 mW check to WP-PDR-21, but the note does not tell WP-PDR-21 or the TS-012 author that the drive window, as the note's own numbers give it, is already short at the low corner. **Fix:** state this as a request to WP-PDR-21 and to the TS-012 author (section 9), and derive the C10 passband criterion from the window WP-PDR-21 sets. | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-D2, CK-ANA-D3 | note sections 3 (PWM row), 4.2, 6 (C10 row and derived requirement), 2 item 3; README line 37; `tx_spur_plan.py` lines 90, 412, 417 | Numbers that do not equal the checker output or are rounded away from the limit: (a) "passband within 0.7 dB" (C10, 2 % corners): the checker gives 0.73 dB. (b) "agree ... to within 0.003 dB": 0.0034 dB (harmonic LPF). (c) "76.0 dB at 432 MHz": 75.96 dB, and TS-012 quotes 75.9. (d) VGG ripple "0.23 to 0.84 mV": the code computes 2.1 V / (150/1)^2 = 0.093 mV at the low end. The dBc figures (-97 to -72) use 0.093 mV, so the text is wrong and the numbers are right. (e) A4 G_eff "GVA-84+ at its P1dB of +19.4 to +20.4 dBm, 21.5 to 24 dB compressed gain" gives a carrier of -4.6 to -1.1 dBm at the GVA-84+ input (G_eff 38.1 to 41.6 dB), while the code uses -5 to -2 dBm (39.0 to 42.0 dB). The high end is 0.4 dB conservative and the low end not as stated. None changes a verdict. **Fix:** quote the checker values and correct the text or the constant. | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-G1-3 | `tx_spur_filters.cir` lines 16 to 19, 24 to 28; TS-012 8.3 row 5 | The harmonic low-pass is synthesized from the 0.1 dB prototype (series inductors 68.6, 75.9, 68.6 nH), while the design data of record, the TS-012 8.3 BOM, buys 68, 82, 68 nH. The drive low-pass is synthesized at 93.6 nH against the BOM's 82 nH. Limitation 7 names WP-PDR-21 as superseding, but the note does not say that its filters differ from the BOM values. The in-window correction dH_LPF is small, so no verdict moves. **Fix:** state the difference in limitation 7, or run the BOM values. | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-I2, CK-ANA-E1, CK-ANA-F1 | `antenna-PB-*.png`, `worst-line-vs-carrier.png`, `c10-tolerance.png`, `filters.png`; note sections 1 and 3 | (a) The limit lines carry values but not their ids ("-16 dBm (25 uW)", "-23 dBm (60 dBc at 5 W)"). REQ-SYS-017 / 97.307(e) and REQ-SYS-018 should label them. The 288 and 432 MHz markers on `filters.png` need their REQ-SYS-018 allocation. `c10-tolerance.png` does not draw its 10 dB rejection criterion at 125 MHz. (b) 47 CFR 97.307(e) is cited without the corpus form `47 CFR 97.307(e) (corpus: <file>, eCFR issue 2026-09-23)`. (c) REQ-SYS-017 names every power step and the 6.4 to 8.4 V pack; the note evaluates 5 W only and does not argue why 5 W is the worst case for the absolute limit. That argument is short for the CLK1-net and GVA-input lines, which scale with the chain gain. It does not cover the VGG sidebands, whose relative slope rises at lower steps (roughly 2 per volt near 0.5 W against 0.6 per volt at 5 W, from the TS-012 7.3 graph points). The derived 3.3 mV ripple limit is for 5 W only. **Fix:** label the limits with their ids, use the corpus citation, and add a paragraph on power step and pack voltage. | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-ANA-H1, CK-ANA-H2 | note sections 5 (re-score sentence), 9 | The note names neither HZ-008 (spurious emissions; REQ-SYS-017 control, and the hazard TS-012 7.1 names for this risk) nor a request to the risk register writer (WP-PDR-18), although it recommends re-scoring the TS-012 7.1 non-harmonic spur rows after the tinySA sweep and finds that B0 and B1 fail. **Fix:** name HZ-008 and add a WP-PDR-18 request to section 9 (the residual 150 MHz line and the C7 dependency as risk inputs). | Open | Pending | |

### Per-case results (section F; the TS-012 7.3 item for each finalist, the REQ-SYS-017 verification carriers, and the supporting checks)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | A5, plan PB, 5 W, 144.050 MHz | TS-012 7.3: each line at most -68 dBm at the GVA-84+ input, or a named change; REQ-SYS-017 -16 dBm; REQ-SYS-018 -23 dBm at the SMA | worst 150.000 MHz -37.9 to -12.1 dBm at the SMA; 5 lines over -23 dBm, 1 over -16 dBm at the high estimate | -3.9 dB (25 uW) and -10.9 dB (60 dBc) at the high estimate; +21.9 and +14.9 dB at the low estimate | line estimates span 20 to 50 dB (note 7 item 1) | re-run: identical `results.json`, `lines.csv` and PNGs | finding-1, finding-3 |
| C-2 | A5, plan PB, 147.950 MHz | as C-1 | worst -12.1 dBm (150.000 MHz); 5 lines over -23 dBm | as C-1 | as C-1 | re-run: same | finding-1 |
| C-3 | A5, plan PB, 146.000 MHz and the 144.010 to 147.990 MHz sweep | as C-1 | worst over the band -12.1 dBm; 4 to 6 lines over -23 dBm | -3.9 dB (25 uW, high estimate) | as C-1 | re-run: same | finding-1 |
| C-4 | A4, plan PB, 144.050, 146.000, 147.950 MHz and the sweep | as C-1 | worst -12.7 dBm (150.000 MHz); 4 to 6 lines over -23 dBm; 1 over -16 dBm | -3.3 dB (25 uW, high estimate) | as C-1 | re-run: same | finding-1 |
| C-5 | A5 and A4, plan P, the three carriers and the sweep | as C-1 | worst -11.2 dBm (A5, 125.000 MHz), -11.7 dBm (A4); 8 to 10 lines over -23 dBm; 2 over -16 dBm | -4.8 dB (A5, 25 uW, high estimate) | as C-1 | re-run: same; without the C7 credit the worst becomes -3.9 dBm (margin -12.1 dB) | finding-1, finding-2 |
| C-6 | A5 and A4, plans B0 and B1 (TS-012 revision 4 as written, ADR-031 values) | as C-1 | worst -0.4 dBm over the band (7/8 fc, /8 prescaler); 16 to 19 lines over -23 dBm; 10 to 11 over -16 dBm | -15.6 dB (25 uW, high estimate) | as C-1 | re-run: same | none |
| C-7 | clk_sys reconciliation (TS-012 7.3 item) and ADR-031 receive re-check of 96 MHz | ADR-031 rules 1, 3, 4: no clear-class line in 144.010 to 147.999 MHz at 65 ppm | clk_sys 96 MHz: no line; PWM TOP+1 640, coherent; SPI 96/24 and QSPI CLKDIV 13, 15, 17, 19, 21, 23, 24 excluded | met (clear sets stated) | exact (rational arithmetic) | re-run: same; hand check 96/640 = 150 kHz, 144000/150 = 960; 148 / (96/24) = 37 | none |
| C-8 | ADC clock in transmit (TS-012 7.3 item) | RP2350 clk_adc 48 MHz | C2: CLK_ADC_CTRL AUXSRC 0x1 (PLL_SYS) / 2 = 48 MHz, bursts; C3 PLL_USB off | met (configuration exists) | not a level | pico-sdk `clocks.h`: `CLOCKS_CLK_ADC_CTRL_AUXSRC_VALUE_CLKSRC_PLL_SYS _u(0x1)`, ENABLE "Starts and stops the clock generator cleanly", `CLK_ADC_DIV_INT_BITS 0x000f0000` | none |
| C-9 | Harmonic LPF deck against the adversarial C8 figures | TS-012 7.3: ideal 47.9 dB at 288 MHz, 75.9 dB at 432 MHz | LTspice ideal 47.91 dB, 75.96 dB; analytic difference 0.0034 dB max, 100 to 500 MHz | +0.01 and +0.06 dB against the quoted figures | numerical, under 0.01 dB | re-run through the wrapper: identical `.meas` values | finding-6, finding-7 |
| C-10 | Option C10 tolerance corners | note's own criterion: 144 and 148 MHz within 3 dB of nominal at 146 MHz; 125 MHz rejection at least 10 dB, at every 2 % corner | 0.73 dB, 14.6 dB (correlated corners): PASS; 5 % corners 3.73 dB, 9.0 dB: fail | +2.27 dB and +4.6 dB | corner method (finding-4) | independent ABCD with 128 independent corners: 0.83 dB, 14.5 dB (+/-0.1 pF small C); 1.46 dB, 13.1 dB (+/-0.25 pF) | finding-4, finding-5 |

## Readiness criteria

| # | Criterion | Evidence |
|---|---|---|
| R1 | Yes | Every `product_files` blob equals `git rev-parse 09fae14:<path>` and `HEAD:<path>` (HEAD `09fae14`, 2026-09-28). Working-tree changes on `main` touch only other products (keyer host study, other `hardware/sim/` blocks). |
| R2 | Yes | `tools/ltspice-batch.sh -o <scratch> -b hardware/sim/freq/tx_spur_filters.cir`: `result: PASS ... sha256=2e3ffa7d... version_line='LTspice 26.0.2 for MacOS' ltspice_exit=0`; the same for `tx_spur_bpf_tol.cir` (`sha256=55dd7273...`). `.venv/bin/python hardware/sim/freq/tx_spur_plan.py --run-id <scratch run>` in a scratch copy of the tree: exit 0, "overall": "PASS", as the note states. |
| R3 | N/A | no JSON under a schema in the product |
| R4 | Yes | Author return (brief): question, method, four plans, results, the 150.000 MHz residual, LTspice status and developer-evidence status. It lists no `values_proposed` (none are TBR values). |
| R5 | Yes | No `TBD` in the note, README, checker or decks (grep after vector search). REQ-SYS-018's TBR is named as such. |
| R6 | Yes | The seven PNGs the note and README cite exist in `results/txspur-20260928-01/`. |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Section 1 quotes TS-012 7.3 and names REQ-SYS-017, REQ-SYS-018 (TBR), WP-PDR-20. The ids exist. |
| CK-ANA-A2 | Yes | TS-012 revision 4 (`7d0d450`) and ADR-031 are named, AT RISK stated. No schematic exists; the design data are the TS-012 7.3, 8.1 and 8.3 texts. |
| CK-ANA-A3 | Yes | Every input row has a source or an ESTIMATE (Low) label (section 3). |
| CK-ANA-A4 | No | Checked against sources: CLK1 +9.0 to +10.4 and +12.9 dBm (TS-012 7.3: agrees); GVA-84+ 22.5 to 25 dB and P1dB +19.4 to +20.4 dBm (agrees); 7-pole 0.1 dB Chebyshev 165 MHz and C8 figures (agrees, finding-6 rounding); 12 MHz XOSC, 25 MHz reference (TS-012 8.3 row 29: TG2520SMN 25.000M; agrees); 8 MHz BFO (TS-012 7.3; agrees); RP2350 clk_adc register values (pico-sdk header: agrees); PLL_SYS FBDIV 120, POSTDIV 5 and 3 gives 1440 / 15 = 96 MHz, VCO within 750 to 1600 MHz (agrees); pavelmc crosstalk "about -35 dB" worst and "below 50dB" with measures (agrees with the -35 to -50 dBc reading); 74LVC1G80 input thresholds (not used by the note: finding-2); PA3FWM theory figure (misapplied: finding-3); VGG slope 0.6 per volt from 4 W at 3.0 V and 7 W at 3.5 V (hand check: 0.5 x 6 W/V / 5 W = 0.6 per volt; agrees); 97.307(e) and REQ-SYS-017 (agree). |
| CK-ANA-A5 | Yes | Flat gain (conservative), mirror at -6 dB (stated as crude, limitation 3), amplitude sum of coincident lines (worst phase), geometry ranges pending layout: each stated with its direction. |
| CK-ANA-A6 | No | Section 9 carries requests to WP-PDR-41, 20, 32, 35, 21, 22, 24 and the TS-012 author. Missing: the REQ-SYS-182 consequence of C7 (finding-2) and the drive-window consequence of the 19.6 dB filter-and-pad figure (finding-5). |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Physics checked: the CLK1-net lines keep their dBc through a gain-controlled chain; the GVA-input lines take G_eff = 37 dBm minus the carrier at the GVA-84+ input (conservative for a compressed chain); a PFD spur keeps its 25 MHz offset through the divide-by-6 and falls by 15.6 dB (correct); /8 products at 7/8 and 9/8 fc and the /4 products at 3/4 and 5/4 fc (correct); the kickback isolation 20 log(355/25) = 23 dB is close to the 22.3 dB that includes the 100 pF reactance. Not modelled: whether the prescaler still clocks after C7 (finding-2). |
| CK-ANA-B2 | N/A | No vendor model is used (ideal parts, series-R inductor Q; limitation 7). |
| CK-ANA-B3 | Yes | The ideal LTspice filters agree with the analytic Butterworth (0.0001 dB) and Chebyshev (0.0034 dB) over 100 to 500 MHz (`results.json` `filter_check`). This covers TV-014 limitation 1 (solver known answers only for first-order RC) for these linear AC decks. |
| CK-ANA-B4 | Yes | `.ac lin 1601 100e6 500e6` (0.25 MHz) and `lin 401 100e6 200e6`; lines are interpolated. The nearest limit-deciding values (the 150 MHz line) sit in a flat part of both responses. |
| CK-ANA-B5 | Yes | Independent method: an ABCD cascade of circuit B in Python reproduces LTspice at 125, 144, 175 MHz (-36.99, -19.71, -30.96 dB against LTspice -36.99, -19.72, -30.96 dB as S21). Hand check of the kickback isolation, the VGG ripple limit (3.33 mV for -60 dBc: 0.6 x 3.33 mV / 2 = 1e-3), the PWM TOP+1 (640) and the A5 G_eff (37 - (9 - 19.6) = 47.6 dB). |
| CK-ANA-B6 | Yes | Low/high estimate ranges per line; limitation 1 states 20 to 50 dB widths. |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | `.log` first line "LTspice 26.0.2 for MacOS" (lock row); venv Python 3.13.5, numpy 2.5.3, matplotlib 3.11.2, spicelib 1.6.3 equal `tools/toolchain.lock.md` section 2. |
| CK-ANA-C2 | Yes | LTspice through the accredited wrapper (TV-014, ACC-LTSPICE-001, blob `88b71475` checked by `git hash-object`). The checker has no TV record: the note marks developer evidence, and nothing closes a requirement. |
| CK-ANA-C3 | Yes | Netlist decks, one `.ac` each; three commands in the README reproduce everything. |
| CK-ANA-C4 | Yes | Reviewer re-run (scratch copy of `09fae14`): both LTspice decks re-run through the wrapper; the `.meas` lines are identical to the committed logs (only the temporary path differs). `results.json` and `lines.csv` are identical after replacing the run id, and all seven PNGs are byte-identical (`cmp`). |
| CK-ANA-C5 | Yes | TV-014 section 2 "Not covered: ... statistics of `.step`": the corner values are read per step by the checker; limitation 1 is met by C-9. |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | dBm/dBc/dB conversions and V peak to dBm (`dbm_from_vpk`) checked. |
| CK-ANA-D2 | No | finding-6 (text against checker values); finding-4 (e) README corner count. Spot checks that agree: B0 144.000 MHz -26.9 dBm, B1 -22.9 dBm, P -34.8 dBm; PB fc - 0.5 MHz -23.1 dBm and fc + 2 MHz -21.5 dBm at 144.050 MHz; worst-line table of 4.2 against `results.json` `criterion`. |
| CK-ANA-D3 | No | finding-6 (a), (b), (c). |
| CK-ANA-D4 | Yes | `LIM_LEGAL_ANT = -16.0` (97.307(e), REQ-SYS-017) and `LIM_TARGET_ANT = 37 - 60` (REQ-SYS-018) with comments; inclusive comparison `<=`. The TS-012 acceptance ("or a change named") is where finding-1 lies. |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Limits quoted with ids and the 97.307(e) basis; corpus citation form missing (finding-8 (b), Minor). |
| CK-ANA-E2 | Yes | Limit minus high estimate reported per line (`lines.csv`); no TPM thresholds apply (TPM-007 is measured at the bench). |
| CK-ANA-E3 | No | finding-1. |
| CK-ANA-E4 | No | finding-1 (b): the exit status counts named strings, not the limits. |
| CK-ANA-E5 | N/A | No TBR value proposed. |
| CK-ANA-E6 | N/A | No TPM estimate proposed. |
| CK-ANA-E7 | Yes | No credit claimed; developer evidence; closure at the bench (TC-SYS-014). |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | Yes | The TS-012 7.3 item: both finalists, the line list, the clk_sys reconciliation, the ADC choice, levels at the GVA-84+ input: all present (C-1 to C-8). The REQ-SYS-017 verification carriers 144.05, 146.00, 147.95 MHz and a 20 kHz sweep are present. Power steps and pack voltage are not argued (finding-8 (c), Minor: no verdict moves, see its text). |
| CK-ANA-F2 | Yes | The fault-bounding cases do not apply; the key-up backwave is in TS-012 7.3. |
| CK-ANA-F3 | Yes | Coincident lines summed in amplitude for the high estimate; worst phase stated. |
| CK-ANA-F4 | No | Margins within twice the uncertainty everywhere in P and PB; the sensitivity to the two largest inputs (Si5351 feedthrough level; the C7 and C10 credits) is not shown. finding-2. |

## G1. Simulation decks and checkers

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G1-1 | Yes | `hardware/sim/freq/`, run directory with plots, deck and script copies. |
| CK-ANA-G1-2 | Yes | One `.ac` per deck; the wrapper's NC_ net check passed. |
| CK-ANA-G1-3 | No | 50 ohm source and load (correct for the drive chain and the LPF); values differ from the BOM (finding-7). |
| CK-ANA-G1-4 | No | Reads `.raw` through spicelib; fails on a missing filter raw (exit 2) but not on a missing or stale tolerance raw; step order hard-coded (finding-4). |

## G2. Budgets (spurious)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G2-1 | Yes | Every line carries its basis and ESTIMATE label (`lines.csv` basis column). |
| CK-ANA-G2-2 | Yes | Recomputed by the re-run (identical) and by the reviewer's variant runs. |
| CK-ANA-G2-3 | N/A | No allocation or `budgets.md` line feeds this estimate. |
| CK-ANA-G2-4 | Yes | Transmit only, by the question; receive is covered by the ADR-031 re-check (C-7). |

## G7. Worst-case, tolerance

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | No | Correlated extreme-value corners only; finding-4. |
| CK-ANA-G7-2 | Yes | Initial tolerance only. C0G and air-core drift over temperature is small against 2 %; not stated, and no finding is raised on it. |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | No | finding-9. |
| CK-ANA-H2 | No | finding-9. |
| CK-ANA-H3 | Yes | Change log revision 0, 2026-09-28. |

## I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | The seven PNGs were opened with the Read tool: `spectrum-gva-A5-144.050.png`, `spectrum-gva-A4-144.050.png`, `antenna-PB-144.050.png`, `antenna-PB-147.950.png`, `worst-line-vs-carrier.png`, `filters.png`, `c10-tolerance.png`. |
| CK-ANA-I2 | No | Axes labelled with units, legends present, and plotted values agree with `lines.csv` at the labelled lines (150.000 MHz at -57.1 dBm referred and -12.1 dBm at the SMA; 126.044 MHz at -45.6 dBm in B0). Limit ids missing and the C10 rejection criterion not drawn (finding-8 (a)). |

## Items N/A

CK-ANA-B2 (no vendor model), CK-ANA-E5, CK-ANA-E6 (no TBR or TPM value proposed), CK-ANA-G2-3, CK-ANA-G3 to G6 (not thermal, RF exposure, cascade or timing), CK-ANA-J1 to J3 (criticality neither), readiness R3.

## Cross items for the lead SE

- **X-1 (checklist field).** As INSP-056 X-1: the field names `peer-review-checklist-design` revision B, and `checklist_analysis` records the template applied. It is switched at the delta iteration after CR-012 merges.
- **X-2 (owner visibility).** The owner approves what he can see. The plots show the residual lines over both limits at the high estimate. The note's word PASS does not match those plots (finding-1), and the owner should not read the per-finalist verdict as "the spur plan is closed". The discrimination statement (A4 and A5 within 1 dB; no reason to change the TS-012 ranking) is supported by the re-run and is unaffected by the findings: finding-2 and finding-5 apply to both finalists alike.
- **X-3 (tinySA).** The note rests the residual lines on the tinySA sweep before first on-air use. The status note of 2026-09-28 records that the owner buys the tinySA later. That is consistent with the note (bench check before on-air use), but the parts order will be placed before the 150 MHz line can be measured.
- **X-4 (id).** INSP-113 was the next free id at filing; a parallel reviewer filing at the same time must take another.

## Verdict

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/spurs-ts012.md@da3b058a, hardware/sim/freq/README.md@a64704b0, hardware/sim/freq/tx_spur_plan.py@b6432663, hardware/sim/freq/tx_spur_filters.cir@c647c60a, hardware/sim/freq/tx_spur_bpf_tol.cir@b0f27d7a, results/txspur-20260928-01 results.json@b80df7b7, lines.csv@79c6a473 and 7 PNGs at 09fae14
FINDINGS:
- [Major] CK-ANA-E3/E4 finding-1: "PASS" per finalist while residual lines stay over 60 dBc and 25 uW at the high estimate; the named changes do not lower them; T1 infeasible as sized (4 dB carrier loss at 147.99 MHz for 11 dB at 150 MHz).
- [Major] CK-ANA-A4/A6/B1/F4 finding-2: C7 (330 ohm series tap) leaves the 74LVC1G80 clock under its VIH/VIL swing (0.43 to 0.58 V peak against 0.6 V); P's worst line is -3.9 dBm without the C7 credit.
- [Minor] CK-ANA-A4 finding-3: fractional-spur source misapplied (30 MHz multisynth theory; 144 MHz integer MS with fractional PLL).
- [Minor] CK-ANA-G7-1/G1-4 finding-4: correlated tolerance corners, 2 % C0G not purchasable for 2.4 and 7.5 pF, step labels transposed, silent skip of a missing raw; conclusion holds on independent corners.
- [Minor] CK-ANA-A6 finding-5: the note's 19.6 dB drive loss puts the module low corner at 7.8 mW; not sent to WP-PDR-21 or the TS-012 author.
- [Minor] CK-ANA-D2/D3 finding-6: text values against checker values (0.7 vs 0.73 dB, 0.003 vs 0.0034 dB, 76.0 vs 75.96 dB, 0.23 vs 0.093 mV, A4 G_eff derivation).
- [Minor] CK-ANA-G1-3 finding-7: LPF inductors synthesized, not the BOM values.
- [Minor] CK-ANA-I2/E1/F1 finding-8: limit ids on plots, corpus citation, power-step and pack argument.
- [Minor] CK-ANA-H1/H2 finding-9: HZ-008 and the WP-PDR-18 request missing.
ITEMS N/A: CK-ANA-B2, E5, E6, G2-3, G3 to G6, J1 to J3, R3
VALUES PROPOSED: none
MEASUREMENTS: size=24 plan-finalist-carrier cases plus sweep; inputs_checked=16; renders=7; turns=45; minutes=70; major=2; minor=7
```

## Iteration 2: delta verification on revision 1 (2026-09-28, HEAD 5a36ecd)


**Scope (rule C1):** verify the finding-1 and finding-2 fixes; raise new findings only where revision 1 introduced them or made an existing defect decide a reported result.

**Independence:** this invocation authored no product file and edited none.

**Search first:** mcp__claude-context__search_code ran on /Users/robinonsay/rust/cwht before any grep; grep then only pinned lines in the PDR plan, validate_docs, toolchain.lock, TS-012 and the 47cfr-97.307 corpus.

**R1:** 20 of 20 blobs equal. The run-directory copies of the decks and script are cmp-equal to the block copies.

**R2 / C4 re-run:** the five decks were run through the wrapper into scratch. Each gave PASS with exit 0 and deck SHA-256 equal to the committed *.wrapper.txt:
- filters 2e3ffa7d
- bpf_tol 55dd7273
- c7_tap e783220b (70 s)
- c7_iso 028b3196
- trap 9fbd9488
The checker from a git archive of 5a36ecd (script blob d123168d) exits 1: 'RESIDUAL (TS-012 7.3 met by wording only...)'. results.json has 0 differences (run_id excluded) and lines.csv is identical.

**B5 independent checks:**
- C7 isolation by closed form: 47 ohm 0.40 to 1.13 dB, 330 ohm 5.50 to 9.07 dB, equal to LTspice.
- T1 by closed form: 47 nH Q100 35.18 / 26.01 / 9.17 dB; 1 uH Q100 11.25 / 3.96 / 7.29 dB (10.51 dB at 144.050 MHz); 2.2 uH Q100 6.87 / 1.66 / 5.21 dB; 1 uH Q60 8.27 / 4.11 / 4.16 dB.
- PB 9/8 fc: -45 dBc - 0.4 dB (C7) - 4.9 dB (C10) at 37 dBm gives about -13.4 dBm, summed with the trace and mirror terms to -12.1 dBm.
- P 7/8 fc: about -8.1 dBm alone, -4.3 dBm with the coherent 9/8 fc mirror.
- 148 MHz period 6.76 ns; 3.13 ns against tW 2.5 ns; fmax margin 8 %.

**Inputs:**
- 74LVC1G80 Rev. 17 Tables 6 to 9: equal.
- TS-012 7.3 criterion: verbatim (TS-012 line 378 at 7d0d450).
- 97.307(e) (corpus: docs/references/md/regulatory/47cfr-97.307.md): 25 uW = -16 dBm.
- REQ-SYS-017 and REQ-SYS-018 (TBR): quoted correctly.
- C7 source and drive network: equal to pa-drive-ts012.md run d2.

**I1/I2:** 9 PNGs opened (spectrum A5 and A4, antenna P-PB 144.050 and 147.950, worst-line-vs-carrier, filters, c10-tolerance, c7-prescaler-tap, t1-trap). Values agree with results.json at the labelled points.

**Per-case rows (iteration 2):**

| Case | Condition | Worst line (high estimate) | Lines over | Margin | Finding |
|---|---|---|---|---|---|
| C-11 | PB A5 144.050 MHz | -12.1 dBm | 3 over 25 uW | -3.9 dB | finding-10 |
| C-12 | PB A5 146.000 MHz | -12.0 dBm (3 coincident at 150.000 MHz) | 3 over 25 uW | -4.0 dB | finding-11 |
| C-13 | PB A5 147.950 MHz | -12.2 dBm | 3 over 25 uW | -3.8 dB | |
| C-14 | PB A4 144.050 / 146.000 / 147.950 MHz | -12.1 / -12.6 / -12.9 dBm | | -3.9 / -3.4 / -3.1 dB | |
| C-15 | PB sweep | -12.1 dBm | 6 to 8 over 60 dBc | | finding-11 |
| C-16 | P, both finalists | -4.3 dBm | 10 to 12 residual; 4 over 25 uW | -11.7 dB | |
| C-17 | B0/B1 | -0.4 dBm | 16 to 19 residual; 10 over 25 uW over the sweep, 11 at 146.000 MHz | | finding-11 |
| C-18 | TS-012 wording | met only by named changes; residual_without_any_named_change 0 | | | |
| C-19 | C7 47 ohm margin | worst corner | | +0.229 V against a 0.10 V criterion | |
| C-20 | C7 47 ohm tW / slew / fmax | 3.13 ns / 1.86 ns/V / 148 MHz | | | |
| C-21 | T1 at 60 dBc | best 9.15 dB against 11.0 dB | | -1.85 dB | finding-11 |
| C-22 | T1 at 25 uW | 5.21 dB at 1.66 dB carrier loss | | | |

**Findings table update:**
- finding-1: Verified.
- finding-2: Verified.
- finding-3 to finding-9: Open (liens due at the CDR readiness declaration).
- New findings finding-10, 11, 12 as stated above, each Minor, Open (lien), owner ruling Pending. Owner of all three: the WP-PDR-20 spur plan author, next revision, at the latest the CDR readiness declaration; finding-10 before section 8 item 4 is used at the bench.

**Items N/A:** as iteration 1.

**Verdict block:**
```
VERDICT: APPROVED (reviewer, iteration 2); record held at NEEDS CHANGES until the CR-012 merge
PRODUCT: spurs-ts012.md@3fc2ec4b, tx_spur_plan.py@d123168d, 5 decks, README@4ebdde90, run txspur-20260928-02 at 5a36ecd
FINDINGS: [Major] finding-1 Verified; [Major] finding-2 Verified; [Minor] finding-10 CK-ANA-F3; [Minor] finding-11 CK-ANA-D2; [Minor] finding-12 CK-ANA-A6; finding-3 to 9 Open liens
VALUES PROPOSED: none
MEASUREMENTS: size=12 cases (iteration 2); inputs_checked=12; renders=9; turns=55; minutes=75; major=0 new (2 verified); minor=3 new
```

**Iteration 2 findings (verbatim from the reviewer):**

- [Major, iteration 1] finding-1: Verified. (a) Revision 1 reports the TS-012 7.3 criterion two ways, 'not met: residual lines' and 'met by wording only: N residual lines, M over 25 uW, closing at the bench', in sections 1, 4.2, 5 and 8 and in README run 02. PASS now appears only for the filter cross-check and the C10 2 % check. (b) The CHANGE table in tx_spur_plan.py carries credited and named lists. results.json cases.<plan>/<fin>/<fc>.residual_lines and the lines.csv columns credited_in_numbers and named_not_credited list them. Exit codes: 0 = pass in the numbers, 1 = residual, 3 = a residual line with no named change; the re-run gives 1, and residual_without_any_named_change is 0 in every case. (c) T1 is sized in tx_spur_trap.cir, confirmed by closed form, and withdrawn: best 9.2 dB against 11.0 dB needed at 147.990 MHz; the 25 uW trap costs 1.66 dB of carrier. (d) The section 8 residual table agrees with results.json (PB: 7 at each carrier, 6 to 8 over the sweep, 3 over 25 uW; P: 10 to 11 at the carriers, 10 to 12 over the sweep, 4 over 25 uW).

- [Major, iteration 1] finding-2: Verified. The 74LVC1G80 limits match Nexperia Rev. 17 (see summary). tx_spur_c7_tap.cir runs 144 corners; its source and drive network match pa-drive-ts012.md run d2, the bias is 1.42 V, the clamp is to ground only, the maximum step is 20 ps and settling is 2.9 us. Re-run results: 47 ohm has a worst margin of +0.229 V (low source, 50 ohm, 3 pF), tW 3.13 ns and 1.86 ns/V; 100 ohm gives +0.099 V (fails the 0.10 V criterion); 330 ohm gives -0.255 V. The isolation physics is sound: the kickback source impedance is CI itself, so a series resistor only divides against about 200 ohm. Only 0.4 dB is credited, and the /8 kickback lines become residual lines. The iteration 1 cross-check agrees: P without the C7 credit was -3.9 dBm, and with 0.4 dB it is -4.3 dBm. One requested element is not done: REQ-SYS-182 is not named against C7 in section 8 item 3. The root defect (an invalid clock) is fixed, so this is recorded without a new finding.

- [Minor, iteration 1] finding-3 to finding-9 stay Open as liens due at the CDR readiness declaration (rule C1). Revision 1 fixed the Majors only. At 5a36ecd the section 3 fractional-spur basis is unchanged (finding-3), the deck and the README 'nine tolerance corners' are unchanged (finding-4), the '76.0 dB', '0.003 dB', '0.7 dB' and '0.23 to 0.84 mV' texts are unchanged (finding-6), there are no limit ids on the plots and 5 W is still the only power step (finding-8), and HZ-008 and the WP-PDR-18 request are still missing (finding-9). Revision 1 widens finding-9: the /8 kickback is now a second Red-level cause (note section 5), and section 9 still sends nothing to WP-PDR-18.

- [Minor, new] finding-10 (CK-ANA-F3), note sections 4.2 and 8 item 4, c10_tolerance. Revision 1 made C10's rejection at 7/8 fc and 9/8 fc set 2 of the 3 PB lines over 25 uW, but the tolerance check still tests only the passband and the 125 MHz rejection, and PB uses the nominal C10. From the re-run tx_spur_bpf_tol.raw, 2 % corners against nominal, relative to the carrier:
- 144.050 MHz: 9/8 fc -4.88 to -2.37 dB (+2.5), 7/8 fc -16.17 to -13.53 dB (+2.6), 150 MHz +0.12 to +0.77 dB (+0.65).
- 146.000 MHz: +2.2, +2.9 and +0.3 dB.
- 147.950 MHz: +1.9, +3.3 and +0.15 dB.
So the PB /8 lines can be 2 to 3 dB higher (9/8 fc about -9.6 dBm, ESTIMATE). The derived requirement of about 55 dBc at 9/8 fc, which section 8 item 4 also uses as the CLK1-pin bench alternative, becomes about 57.5 dBc. Iteration 1 finding-4 (b) also applies: 2.4 and 7.5 pF parts are sold with absolute tolerances, so the real spread can be wider. No count over 25 uW changes, and the SMA sweep still governs on air. Fix: report the C10 relative rejection at 7/8 fc, 9/8 fc and 150 MHz at the tolerance corners and carry the worst case into PB, and word item 4 against the measured, as-built C10 or the worst-corner value.

- [Minor, new] finding-11 (CK-ANA-D2), note sections 4.2 and 4.5, SWEEP. The sweep grid 144.010 + 0.020 k MHz never reaches 146.000 MHz (k = 99.5) or other exact-coincidence carriers. At 146.000 MHz the 150 MHz line picks up the 2 x 2 MHz switcher sideband, so the numbers disagree:
- PB worst over the band is reported as -12.1 dBm, but cases.PB/A5/146.000 gives -12.0 dBm.
- B0 and B1 show 10 lines over 25 uW over the band but 11 at 146.000 MHz.
Revision 1's new section 4.5 says the 150 MHz line 'is -12.1 dBm ... needs 11.0 dB'. -12.1 dBm needs 10.9 dB; the checker's 11.0 dB comes from -12.0 dBm (t1_trap.line_150_ant_hi_dBm_PB). No verdict moves. Fix: add the named and the coincidence carriers (fc = 12n +/- 2k MHz) to the sweep, and quote -12.0 dBm with 11.0 dB.

- [Minor, new] finding-12 (CK-ANA-A6), note section 9. Revision 1 turned the result from 'P and PB PASS' into '60 dBc not shown for 6 to 8 lines', but it does not route the consequence for REQ-SYS-018. That requirement is TBR, close_by PDR, and its tbr.plan reads 'show the margin is achievable, else the target is revised by CR'. The note should state that this is evidence for that ruling (non-harmonic spurs) and add a request to the L1 requirements writer / TBR ruling (rule C10). Fix: one request row in section 9.

- Observations (no finding):
- O-1: the C7 tap loads CLK1 more than WP-PDR-21's 5 pF tap. The re-run minimum is 2.15 Vpp at 0 ohm and 2.04 Vpp at 47 ohm, against 2.22 V, so section 4.4 is wrong to call it 'consistent'. About 0.7 dB of swing is lost on a drive chain already short at 60 of 270 corners. Section 8 item 3 (the WP-PDR-21 re-run with C7) covers it and should be treated as required.
- O-2: in t1-trap.png the 'needed for 25 uW: 4.0 dB' label is partly under the legend (still readable).
- O-3: exit status 1 covers both 'residual lines' and 'filter check failed'; the overall string tells them apart.
- O-4 (lead SE): this record was harvested from the transcripts after the Write refusals. Because of the harness block, every PDR reviewer delta will need the same lead-SE filing step.
