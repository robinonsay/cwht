---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/06-risk-and-decision-analysis.md sections 14.3 step 6 and 16). Independent review of TS-007
# with docs/templates/peer-review-checklist-risk.md section B (PDR work plan WP-PDR-20, record path as the
# plan names it). Iteration 1 at freeze F0 (rule C2). The software assurance pair is a separate invocation
# (07 section 2.1.1 row "Trade studies and ADRs", safety-critical component; PDR work plan WP-PDR-20 and
# rule C9), filed as docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference-software-assurance.md.
id: INSP-055
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference.md
product: docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md
# Delta iteration 2 (2026-09-29, supersession): product_commit, product_blob and the TS-007 entry of
# product_files name cfc9111 and blob 3d1e4e59 (Status row only). Iteration 1 values, kept: product_commit
# 9ac2c42d1ff7b82e3734506aba14dec8eadc3923, product_blob 72c47383cbaec09b6d1cc8d9ac8f7912b61c72fb. The checker
# and the figure are unchanged since 9ac2c42.
product_commit: "cfc9111d6cc0ede052f254bececf09d89d0699f3"
product_blob: 3d1e4e59f1109199a378e31da99289f01f3f7e21
product_files: ["docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md@3d1e4e59f1109199a378e31da99289f01f3f7e21", "hardware/sim/freq/ts007_matrix.py@64c8aad44c9c9da777e6be544cb9553478236481", "docs/reviews/PDR/figures/ts-007-sensitivity.png@e0fb0048a8d6c9ba98016ddb892df33677d5b013"]
product_size: 2 scored alternatives (A1, A2; A0 listed, 4 pruned), 8 mandatory and 7 enhancing criteria (Part A); 2 reference candidates and 4 mandatory rules (Part B); 26 sensitivity runs plus 2 variants
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX)"
reviewer_agent: "reviewer:WP-PDR-20-ts-007-iter1 (independent; authored no part of WP-PDR-20)"
# criticality: the study decides the synthesizer that carries the SW-SYNTH transmit frequency-word path and
# the reference that the SW-SAFE frequency verification unit counts against (07 section 14.1, safety-critical
# by SRR decision 9)
criticality: safety-critical
assurance_required: true
# assurance_reviewer_agent, paired_record and assurance_verdict: copied at delta iteration 2 from INSP-074
# (committed 7c05d72, iteration 1, assurance verdict APPROVED on blob 72c47383; 07 section 10.2 Record row).
# Iteration 1 value: "pending (separate invocation; paired record ...-software-assurance.md)"
assurance_reviewer_agent: "sa-reviewer:WP-PDR-20-ts-007 (paired record INSP-074, docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference-software-assurance.md)"
paired_record: INSP-074
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES until the software assurance pair returns APPROVED (07 section 2.1.1;
# rule C9); the lead SE sets it. Delta iteration 2: the reviewer does not set it; see cross item X-4 there
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 5
# findings_open: delta iteration 2 closes all five by supersession (none fixed or verified in TS-007):
# finding-1, finding-2 and finding-5 moot; finding-3 and finding-4 carried to TS-012, which decides them
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
deferred_rids: []
items_no: [CK-RSK-B5]
# effort: cumulative (iteration 1: 44 turns, 70 minutes; delta iteration 2: 22 turns, 30 minutes)
effort_turns: 66
effort_minutes: 100
# record_status: Closed by supersession at delta iteration 2 (06 section 14.6; ADR-056 section 7 "Other
# records"; plan section 3.0a row TS-007 "Superseded outright"). Reopens if the owner does not confirm the
# TS-007 row at PDR session S1 (OD-10 part 1). Iteration 1 value: Open
record_status: Closed
date: 2026-09-27
date_closed: 2026-09-29
---

# Peer review record: TS-007 synthesizer and frequency reference (INSP-055, iteration 1)

**Product:** `docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md` blob `72c47383` at freeze commit `9ac2c42` (freeze F0, PDR work plan rule C2), with its matrix checker `hardware/sim/freq/ts007_matrix.py` (`64c8aad4`) and figure `docs/reviews/PDR/figures/ts-007-sensitivity.png` (`e0fb0048`). The blobs equal `HEAD` on 2026-09-27 (checked at `c90df2d` and again at `9bda072` before commit). No product blob lives on a `cr/` branch.

**Checklist:** `docs/templates/peer-review-checklist-risk.md` revision A, section B (items CK-RSK-B1 to B10, 06 section 16 "Trade study" items 1 to 10). Section A is N/A (the product is a trade study).

**Acceptance criteria (rule C7, every case the governing clauses enumerate):**
- 06 section 14.3 steps 1 to 5 and the template sections 1 to 9 filled, section 10 empty.
- 06 section 13 item 1: each of safety, first power-on, cost, schedule, performance margin and system security used as a criterion or omitted with a reason.
- 06 section 14.4 items 1 to 5: weight +/-10 on each of the 7 criteria (14 runs); +/-1 on each Low-confidence cell (6 cells, 12 runs); robustness verdict; value of information; method limitations.
- 06 section 14.5: single recommendation, or the closely ranked set when totals differ by less than 25 points.
- 06 section 13 item 2: every surviving alternative's risks in the four-part format with scores on the section 6 and 7 scales.
- The ADR-013 cost-band rule (SI-029, SRR decision 56) applied as the study defines it.
- The requirement ids the study claims to serve (REQ-SYS-029, 031, 154 with their `tbr.plan` text) checked against `docs/requirements/sys/requirements.json`.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (checklist templates, record rules, lock detect and REQ-SYS-154, Pico 2 regulators) and on `/Users/robinonsay/rust/rustos` (FC0, I2C timing, core regulator) preceded every `grep`. RP2350 facts were read only with `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md`; the rustos working tree was not read.

## Findings (iteration 1)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | Minor | CK-RSK-B5, B7 | TS-007 section 4 "Mandatory screening, Part A", row A2 columns M3 and M6; section 6 item 4 | A2 passes M6 (3.3 V supply) with no part evidence (Low: "the supply range is not in the corpus") and M3 (5 Hz word error) on a future SW-SYNTH requirement rather than a property of the LMX2571 (its fractional denominator is not in the corpus, `frequency-budget.md` section 3.2). A fail of either mandatory criterion removes the recommended alternative, yet the robustness verdict (section 6 item 4) does not name this condition. Several mandatory cells carry no confidence tag (A1 M2, M5, M7; A2 M2, M5, M7). Fix: tag every mandatory cell, and state in section 6 and section 8 that the recommendation is conditional on value-of-information item 4 confirming M3 and M6 before CDR, with the fallback (A1) if either fails | Open | |
| <a id="finding-2"></a>finding-2 | Minor | CK-RSK-B5 | TS-007 section 3.1 C1 operational definition ("at 10 kHz offset"); section 4 row C1-A2; section 8 "REQ-SYS-031 at 85 dB ... A2 margin 21.5 dB" | The C1 value and the RMDR margin for A2 are taken at 12.5 kHz offset (F20 datasheet point, -133.5 dBc/Hz), while C1 and REQ-SYS-031 are defined at 10 kHz. The checker also prints an in-band model value at 10 kHz (-138.3 dBc/Hz, RMDR 111.3 dB). The score (5) does not change, but the value quoted against REQ-SYS-031 is at the wrong offset. Fix: state the 10 kHz value the study relies on and which model gives it, and quote the REQ-SYS-031 margin at 10 kHz | Open | |
| <a id="finding-3"></a>finding-3 | Minor | CK-RSK-B5 | TS-007 section 3.2 row A1; section 4 rows M2-A1 and C4-A1 | A1 holds PLL A at six times the LO (retuned at every step) and PLL B at six times the TX carrier while receiving. The BFO on CLK2 must then come from one of these moving PLLs through a fractional multisynth divider, which is recomputed and rewritten at each tuning step. M2 ("pass. Three outputs") and C4 ("TX and RX on separate PLLs") do not address the BFO source, its extra I2C writes per step, or its fractional-divider spurs. This only weakens A1 and does not change the recommendation. Fix: state the BFO PLL assignment for A1 and carry its consequence into C4 and the A1 risks | Open | |
| <a id="finding-4"></a>finding-4 | Minor | CK-RSK-B2, B5 | TS-007 header "Related requirements" (REQ-SYS-154); section 3.1 criteria; section 7 safety line | The REQ-SYS-154 `tbr.plan` gives this study the job "(synthesizer and lock detect) fixes the counting tolerance", and 07 section 14.2 (SW-SYNTH row items g and l) requires lock detect after every write and Fault-safe on an unlocked synthesizer. The study does not state how each alternative reports loss of lock (A1: Si5351A status register read over I2C; A2: LMX2571 lock-detect indication, not in the corpus), nor whether the difference bears on M8, C4 or C5. Fix: add the lock-detect mechanism of each alternative to M2 or C5 evidence, and name value-of-information item 4 for the LMX2571 lock-detect output | Open | |
| <a id="finding-5"></a>finding-5 | Minor | CK-RSK-B5 | TS-007 section 3.1 M7; Appendix A F23 hand check; `ts007_matrix.py` line 65 (`KEY = 0.45`) | M7 is defined as the TPM-008 threshold, but the model uses the F23 45 % key-down, while the TPM-008 `definition` and `formula` in `docs/plan/tpm.json` fix 50 % key-down within the transmit minute. Reviewer re-computation with the checker's own model at 50 %: A1 9.52 h, A2 8.69 h (8.88 h and 9.74 h at 45 %). M7 still passes for both and the TPM-008 status (Yellow for A2) is unchanged. Fix: compute M7 and the section 8 TPM-008 estimate on the TPM-008 definition, or state the key-down difference as a limitation | Open | |

No Major finding. The recommendation follows from the evaluation, and the sensitivity statement is complete (CK-RSK-B7, B9).

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | Yes | Run with this record on `9bda072`: the record passes; the 8 failing records are other records (drift of CR-007, ADR and SRR products after their reviews), unchanged by this record |
| R2 | Section A only | N/A | Product is a trade study |
| R3 | Sections 1 to 9 filled, section 10 empty | Yes | TS-007 lines 17 to 315 filled; section 10 (lines 317 to 324) has empty fields |
| R4 | Author's return names the decision need and gate | Yes | Author summary: "TS-007 recommendation ... A2 scores 380 against 295"; TS-007 header "Decide by: PDR, owner session B1a (Tue 2026-09-29)" |

## B. Trade study (06 section 16, items 1 to 10)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B1 | Yes | Header row "Decision class trigger": 06 section 14.1 class 1 items (b) synthesizer and TCXO, (c) HZ-008 and the 07 section 14.1 SW-SYNTH and SW-SAFE components. Decision maker Robin; gate PDR, session B1a. Class 1 (b) names "synthesizer, TCXO" verbatim (06 line 310) |
| CK-RSK-B2 | Yes | Section 3.1: each enhancing criterion C1 to C7 has an operational definition and a 1 to 5 scale with anchors (C7 binary 1 or 5, acceptable as anchors); M1 to M8 and R-M1 to R-M4 pass or fail. "Criteria considered" lines 101 to 107 cover safety (M8), first power-on (C6), cost (band rule plus the section 6 item 7 variant), schedule (C5), performance margin (C1 to C3) and system security (omitted with the reason: internal buses, no 07 section 16.2 surface). Gap on lock detect recorded as finding-4 |
| CK-RSK-B3 | Yes | Weights 35 + 20 + 10 + 10 + 10 + 10 + 5 = 100, integers; rationale section 3.3 per criterion, "No weight was set by the owner directly" |
| CK-RSK-B4 | Yes | A0 (current baseline, no synthesizer) listed with the ADR-013 option D reason for not scoring it; pruned: ADF4351 and MAX2871 (M7 fail, 6.9 h recomputed below), LMX2571 alone (M2), LMX2571 with a fixed BFO oscillator (no catalogue part in the corpus; kept as CDR refinement), fixed 116 MHz LO (TS-001 F-B). Part B: SiT5356, TG2520SMN; pruned ATX-13 (26 MHz), QRP Labs module (R-M4), generic 2.5 ppm (R-M3), crystal only (ADR-023 option C) |
| CK-RSK-B5 | No | Every enhancing cell links evidence (F16, F17, F20, Table 2, 07 sections 14.1 and 19, `clock-plan.md`, `frequency-budget.md`) and carries a confidence. Defects: mandatory cells without confidence, and A2 M3 and M6 passes without part evidence (finding-1); C1-A2 offset (finding-2); A1 BFO source (finding-3); lock detect (finding-4); M7 key-down basis (finding-5) |
| CK-RSK-B6 | Yes | Recomputed by hand: A1 = 2x35 + 5x20 + 1x10 + 3x10 + 5x10 + 3x10 + 1x5 = 70 + 100 + 10 + 30 + 50 + 30 + 5 = 295; A2 = 175 + 40 + 50 + 30 + 30 + 30 + 25 = 380. Checker re-run (exit 0): "A1: 295 (59.0 %) matches study value 295", "A2: 380 (76.0 %) matches study value 380" |
| CK-RSK-B7 | Yes | Section 6 items 1 to 6 follow 06 section 14.4 items 1 to 5: 14 weight runs (C7 -10 clamped at 0), 12 Low-cell runs (A1 C1, C3, C4, C6; A2 C4, C6), verdict Robust, value of information (5 items with gates), method limitations (no 144 MHz measurement, single research report, no TV record for the scripts, research battery model). Reviewer re-checks: weight C2 +10 by hand, A1 = 195 x 70/80 + 30 x 5 = 320.6, A2 = 340 x 0.875 + 30 x 2 = 357.5 (study: 320.6, 357.5); stress case A1 295 + 35 + 10 + 10 + 10 = 360, A2 380 - 10 - 10 = 360 (tie, as stated); cost variant A1 295 x 0.85 + 75 = 325.75, A2 380 x 0.85 + 15 = 338.0 (study: 325.8, 338.0; 12.2 points, under the 25-point closeness threshold of 06 section 14.5, which the study states). The verdict is consistent with the recommendation. The conditional nature of the A2 mandatory passes is not in the statement (finding-1) |
| CK-RSK-B8 | Yes | Section 7: three A1 risks, three A2 risks and one common risk, each "Given ..., there is a possibility of ..., adversely impacting ..., leading to ..." (06 section 4), with L, C and driving dimension; scores checked: 3x3 = 9 Yellow, 2x3 = 6 Yellow, 3x2 = 6 Yellow, 3x3 = 9, 2x3 = 6, 3x1 = 3 Green, 3x3 = 9 (bands per 06 section 8: Yellow 5 to 11, Green 4 or less). Aggregate A1 9, A2 9. Register requests named (RSK-035 re-score, RSK-040 and RSK-041 members, two new entries); the register is written only by WP-PDR-18 (plan section 5.3) |
| CK-RSK-B9 | Yes | Section 8 recommends A2, the highest total (380 against 295, 85 points apart), with the reference class and acceptance test R-M3 for Part B |
| CK-RSK-B10 | Yes | Section 9 Dissent: "None recorded". Section 10 fields empty. The reviewer records no dissent on the recommendation (the findings above are evidence defects, not a disagreement with the ranking) |

## Independent checks (evidence for B5 to B7)

- **Phase noise.** `-135.6 + 20 log10(144/7) = -109.3` dBc/Hz; `-127 + 20 log10(144/19.99) = -109.85`; `-123 + 20 log10(144/480) = -133.46`. RMDR = `-L - 10 log10(500)` = `-L - 26.99`: A1 central -110 gives 83.0 dB; A2 -133.5 gives 106.5 dB. All equal the study and the checker (F17 lines 67; F20 line 73 of `docs/research/2m-cw-transceiver-reference-designs.md`).
- **C1 scores.** Linear between anchors: -110 dBc/Hz lies 3/5 of the way from -107 (1) to -112 (3), score 2.2, recorded 2; -133.5 is past the -125 anchor, score 5. **C2:** 65 mA lies halfway between 80 (1) and 50 (3), score 2; 30 mA scores 5.
- **REQ-SYS-029 limit.** (S+N)/N of a -130 dBm signal over -140 dBm noise = 11 (10.41 dB); after a 3 dB loss the ratio is 5.508, so the reciprocal-mixing noise may be 1.218 N (+0.86 dB), and L(2 kHz) <= -139.14 + 60 - 26.99 = -106.1 dBc/Hz. Equal to the study.
- **Battery life (F23 model as coded).** life = 2.7 Ah / (0.1 I_tx + 0.9 I_rx), I_rx = I_5V x 5 / (7.2 x 0.9), I_tx = I_rx + 0.25 + 0.45 x 1.30. A1 (0.251 A) 9.74 h; A2 (0.286 A) 8.88 h, reported 8.8 h (rounded down, conservative); LMX2571-only reference 9.5 h, which is the TPM-008 SRR `cbe` (history entry 2026-09-25), so the section 8 "moves from 9.5 h to 8.8 h" is consistent. At TPM-008's 50 % key-down: see finding-5.
- **Cost band.** USD 8.75 + 0.30 = 9.05 to USD 14.46 + 0.30 = 14.76, inside USD 15 with 0.24 to spare; the study marks it Low and supplies the cost-weighted variant.
- **Si5351A M1 and M3.** 144.0012 x 6 = 864.0 MHz, 147.9988 x 6 = 888.0 MHz, 133.3 x 6 = 799.8 MHz, 139.0 x 6 = 834.0 MHz, all inside the 600 to 900 MHz VCO range (F16); step 25 MHz / 2^20 / 6 = 3.97 Hz, half-step 1.99 Hz.
- **Checker re-run.** `.venv/bin/python hardware/sim/freq/ts007_matrix.py --plot` on an export of `9ac2c42` (`git archive`) in the scratchpad: exit 0, "VERDICT: Robust (top A2; rank changes: none)"; the regenerated PNG hashes to `e0fb0048`, byte-identical to the frozen figure.

## Visual closure

`docs/reviews/PDR/figures/ts-007-sensitivity.png` opened with the Read tool (1 render). Bars for the 14 weight runs, 12 cell runs, the stress case and the cost variant, with both baseline totals as dotted lines named in the axis label; A2 leads in every run except the stated tie. Values agree with the checker output.

## Items N/A

CK-RSK-A1 to CK-RSK-A11 and readiness R2 (the product is a trade study, not the register).

## Cross items for the lead SE (not findings on TS-007)

- **X-1.** TS-007 depends on `docs/design/analysis/frequency-budget.md` (M3, R-M3, M8 via K4 and K7) and `docs/design/analysis/clock-plan.md` (C4 evidence, R-M1). Their record `analysis-frequency-budget-and-clock-plan.md` (INSP-056) is NEEDS CHANGES with four Major findings. None changes the TS-007 ranking: the REQ-SYS-154 and counter findings apply identically to A1 and A2, and the I2C line finding weakens A1's C4 evidence, not A2's. The owner decision sheet (B1a) should still wait for INSP-056 where it proposes values (rule C10), while TS-007 itself can go on this record plus its SA pair (rule C9).
- **X-2.** ADR-031 (Proposed) is not reviewed here; its record is to be assigned by the lead SE (design checklist A, B, H).
- **X-3.** The software assurance pair is required (07 section 2.1.1; criticality safety-critical). The lead SE sets `verdict` when the pair returns.

## Commands

- `git rev-parse 9ac2c42:<path>` and `HEAD:<path>` for the three product files: equal to the blobs above.
- `.venv/bin/python hardware/sim/freq/ts007_matrix.py --plot` (export of `9ac2c42`): exit 0.
- `.venv/bin/python tools/validate_docs.py`: exit 0 with this record (see the return).

## Measurements (SWE-089)

Items checked 10 (section B) plus readiness 4; items answered No 1 (CK-RSK-B5); findings 0 Major, 5 Minor; fixed 0, deferred 0; iteration 1; renders inspected 1; effort 44 turns, about 70 minutes (shared session with INSP-056).

## Delta iteration 2 (2026-09-29, supersession of TS-007 by TS-012; independent reviewer, new invocation)

**Scope.** TS-007 changed once since iteration 1: `cfc9111` ("docs(decisions): TS-001 and TS-007 status rows superseded by TS-012 (ADR-056)", WP-PDR-54 part 1). The new blob is `3d1e4e59f1109199a378e31da99289f01f3f7e21` (was `72c47383`). `git log --oneline 9ac2c42..HEAD` over the three product files lists `cfc9111` only; `git rev-parse HEAD:<path>` and `git hash-object <path>` give `3d1e4e59` at `HEAD` `f8dcf8c`. The checker `ts007_matrix.py` (`64c8aad4`) and the figure `ts-007-sensitivity.png` (`e0fb0048`) are unchanged. This delta verifies the edit and records how the review ends; it does not re-review the study's content.

**Independence (rule C4).** A new invocation of the independent reviewer role. It authored no part of TS-007, TS-012, ADR-056, the `cfc9111` edit or INSP-074, and it edited no product file.

**Search first (rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: INSP-055 and TS-007 delta records; review records closed by supersession). `git show`, `git diff`, `diff`, `grep` and `sed` were used afterwards only to pin lines and blobs. The rustos repository was not read.

### Verification of the `cfc9111` edit (06 section 14.6)

06 section 14.6: "the only edit to the old file is its Status line, which becomes 'Superseded by TS-MMM'".

| # | Check | Method | Result |
|---|---|---|---|
| V1 | The edit is the Status line only | `git diff --numstat 72c4738 3d1e4e5`: 1 insertion, 1 deletion. `diff` of the two blobs with line 6 removed from each: identical (361 other lines). Line 6 is the header row `\| Status \| ... \|` | Yes |
| V2 | The row reads "Superseded by TS-MMM" | New line 6 opens "**Superseded by TS-012 (ADR-056).**" | Yes |
| V3 | The kept status text is verbatim | Old line 6 is `\| Status \| In review \|`. New line 6 ends "Previous status, kept as written: In review \|": the old value, character for character | Yes |
| V4 | No criterion, weight, score, ranking, recommendation, section 9 Dissent or section 10 Decision changed | Follows from V1; section 10 fields are still empty, so TS-007 carries no owner decision | Yes |
| V5 | The row's factual claims | TS-012 line 6 Status "Decided 2026-09-29: A5, the owner's choice (section 10)"; TS-012 section 8.3 BOM row 9 (Adafruit 2045 Si5351A) and row 29 (TG2520SMN); section 8.1 line 586 "25 MHz crystal removed"; D-17 (line 1053) route R3; ADR-056 section 2 item 2 (line 59) names the same replacement of A2; plan section 3.0a row TS-007 "Superseded outright"; plan WP-PDR-20 split into 20a and 20b with the analyses the row lists; TS-007 line 14 "ADR-030 (provisional number ...)", which the row says is not taken | Correct |
| V6 | The row does not overstate the state | It says ADR-056 records the decision and the owner's confirmation at S1 (OD-10 part 1) is pending. ADR-056 line 6: Proposed, items 2 to 4 for confirmation at S1 | Correct |

Result: the edit is the one 06 section 14.6 allows, and it keeps the prior status verbatim. No new finding.

### Disposition of the iteration 1 findings

TS-007 will not be revised, re-scored or decided (plan section 3.0a "Superseded outright"; ADR-056 section 7 "TS-007's reviews INSP-055 and INSP-074 end with the study superseded (lead SE disposition)"). Each finding is therefore closed without a fix in TS-007. A finding is **moot** when its subject is not part of the chosen design, or when TS-012 does not decide it and it has no TS-007 fix to wait for. It is **carried** when the same question applies to the chosen A5 design and TS-012 decides it.

| Finding | Severity | State | Reason and where it now lives |
|---|---|---|---|
| finding-1 | Minor | Closed (moot by supersession) | Its subject is the A2 (LMX2571) mandatory passes M3 and M6 and the missing confidence tags on mandatory cells. A2 is not taken: TS-012 section 3.2 line 110 prunes the LMX2571 as "reflow-only", and TS-007 is not re-scored, so no cell needs a tag |
| finding-2 | Minor | Closed (moot by supersession) | Its subject is the A2 C1 value at 12.5 kHz instead of 10 kHz. A2 is not taken. For the chosen Si5351A, TS-012 section 7.3 line 553 gives RMDR about 78 to 83 dB, and section 8.10 line 901 proposes the REQ-SYS-031 delta to 78 dB (TBR) at 10 kHz; those figures belong to the TS-012 records (INSP-110, INSP-118), not to this one |
| finding-3 | Minor | Closed (carried to TS-012, decided there) | The BFO PLL assignment on the Si5351A applies to A5. TS-012 section 7.3 line 556: "CLK0 and CLK1 share PLL A in time, BFO on PLL B", and D-12 (line 1048) item C6: "PLL B parked and CLK0 and CLK2 off in transmit, I2C only in the lead-in". The BFO is on a fixed PLL, so the per-step divider rewrite this finding named does not arise. The spur consequence is in `spurs-ts012.md` (INSP-113) |
| finding-4 | Minor | Closed (carried to TS-012, decided there) | Lock detect applies to A5. TS-012 section 7.3 revision 6 (line 491): "SW-SYNTH reads the lock status and SW-SAFE compares the count" before PA_EN is set; section 8.12 row WP-PDR-35, 41 (line 999) lists "the lock-status read before PA_EN"; D-17 gives the independent FC0 check. The remaining Si5351A relock-time read is WP-PDR-20a's analysis (plan section 3.0a), not a TS-007 matter |
| finding-5 | Minor | Closed (moot by supersession) | Its subject is TS-007's M7 battery figure at 45 % key-down against TPM-008's 50 %. TS-007's M7 decides nothing now, and TS-012 does not decide the battery life: section 8.10 line 935 (REQ-SYS-094) gives "8 to 14 h" and hands the budget to WP-PDR-29. The key-down basis is passed to WP-PDR-29 as cross item X-2 |

Counts at this delta: 5 Minor, 0 Major; open 0; fixed 0; verified 0; deferred 0; closed by supersession 5 (moot 3, carried to TS-012 2).

### Readiness (delta iteration 2)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 | Yes | Run with this delta; this record PASS |
| R2 | Section A only | N/A | Trade study |
| R3 | Sections 1 to 9 filled, section 10 empty | Yes | Unchanged by `cfc9111` (V1, V4) |
| R4 | Author's return names the decision need and gate | N/A at this delta | The decision is TS-012's (ADR-056) |

### Pairing

INSP-074 (software assurance pair, `7c05d72`, iteration 1) returned assurance verdict APPROVED on blob `72c47383` with four Minor findings open. This delta copies that verdict into `assurance_verdict` and sets `paired_record: INSP-074` (07 section 10.2 Record row). INSP-074 also names blob `72c47383`, so it drifts from `HEAD`, and its own findings need the same disposition (cross item X-1).

### Cross items (outside this record's scope)

- **X-1.** INSP-074's reviewer writes its own supersession delta: the new blob `3d1e4e59` and the disposition of its four Minor findings. This reviewer did not assess them.
- **X-2.** WP-PDR-29 (budgets and TPMs): compute the TPM-008 battery estimate on the TPM-008 definition (50 % key-down within the transmit minute, `docs/plan/tpm.json`), not the 45 % of the research model (iteration 1 finding-5 arithmetic: 9.52 h and 8.69 h at 50 % against 9.74 h and 8.88 h at 45 %).
- **X-3.** If the owner does not confirm the TS-007 row at S1 (OD-10 part 1), this record reopens and the five findings return to Open.
- **X-4.** Record verdict. The completion criteria of 07 section 10.2 are now met: reviewer verdict APPROVED, assurance verdict APPROVED (INSP-074), no Major finding open, named blobs equal `HEAD`. The lead SE sets `verdict`, as the iteration 1 front matter says.

### Commands (delta iteration 2)

- `git log --oneline 9ac2c42..HEAD -- <three product files>`: `cfc9111` only.
- `git show cfc9111 -- docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md`: one hunk, line 6.
- `git diff --numstat 72c4738 3d1e4e5`: `1 1`; `diff <(git show 72c4738 | sed 6d) <(git show 3d1e4e5 | sed 6d)`: no output.
- `git rev-parse HEAD:<path>` and `git hash-object <path>`: `3d1e4e59`, `64c8aad4`, `e0fb0048`.
- `.venv/bin/python tools/validate_docs.py`: exit 0; this record PASS.

### Measurements (delta iteration 2, SWE-089)

Commits verified 1 (1 hunk); checks 6 (V1 to V6), all Yes or Correct; findings dispositioned 5 (moot 3, carried 2); new findings 0; renders 0 (no figure changed). Effort 22 turns, about 30 minutes (cumulative 66 turns, 100 minutes).

### Verdict (delta iteration 2)

```
DELTA ITERATION 2 (2026-09-29, supersession; HEAD f8dcf8c, product commit cfc9111): VERDICT: APPROVED (reviewer); record CLOSED by supersession
PRODUCT: TS-007@3d1e4e59 (Status row only, 06 section 14.6: verified; prior status "In review" kept verbatim)
FINDINGS: finding-1, finding-2, finding-5 Minor, Closed (moot); finding-3, finding-4 Minor, Closed (carried to TS-012, decided there); open Major 0; new 0
MEASUREMENTS: checks=6; turns=22; minutes=30; cumulative turns=66, minutes=100
```
