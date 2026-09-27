---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-27 shielding and
# bond analysis note, record path as PDR work plan WP-PDR-27 names it. Iteration 1 at freeze F0 (rule C2,
# freeze commit 70a3a33).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Submitted, not merged).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-design revision B (section J, enclosure; SEMP section 7.2 design analyses) and
# checklist_analysis records the template actually applied, as INSP-056 and the WP-PDR-33 analysis record
# did. The delta iteration after CR-012 merges switches the field to peer-review-checklist-analysis.
id: INSP-083
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-shielding-estimate.md
product: docs/design/analysis/shielding-estimate.md
# product_commit (iteration 2): 70d11ef, the WP-PDR-27 revision 1 commit that fixes finding-1 (re-freeze F0,
# rule C2). Every blob below equals git rev-parse 70d11ef:<path>, HEAD:<path> and git hash-object at HEAD d1148c2;
# all are on main. product_files_iteration_1 keeps the 70a3a33 blobs.
product_commit: "70d11ef54a5bc477cda9e9fa01e7295e1365f147"
product_files: ["docs/design/analysis/shielding-estimate.md@57bb7ba55bb4fcf2e482e1b5a4e87403ea47ba1b", "hardware/sim/enclosure/shielding_estimate.py@eb20c66932aa713becff2ea46a47fce33787609f", "hardware/sim/enclosure/out/shielding.csv@0005f90864b8cce33e87b6bfc3bd1187604c66af", "hardware/sim/enclosure/out/shielding-sources.csv@b01ea4208df24424df0cd4f377d262422c187888", "hardware/sim/enclosure/out/bond.csv@7af39c6bc5d525f4485db1fb111a6f2a156003e6", "docs/reviews/PDR/figures/shielding-estimate.png@8f7aef711b529fa10e606538f7f472374e9c690e"]
product_files_iteration_1: ["docs/design/analysis/shielding-estimate.md@e600e9ee005978f36d2f88c402df5ca6b428c58d", "hardware/sim/enclosure/shielding_estimate.py@3cc126cb05b96bf03d58b149863e1818cbe15f2b", "hardware/sim/enclosure/out/shielding.csv@023cb5c89e2fee02c2c3800f59d2349661232b4a", "hardware/sim/enclosure/out/bond.csv@7af39c6bc5d525f4485db1fb111a6f2a156003e6", "docs/reviews/PDR/figures/shielding-estimate.png@3370418db7029defa93a6f4c3f5d99dcd84f7daf"]
analysis_kind: [other, worst-case]
product_size: 4 options x 9 frequencies x 2 readings plus 2 variants (36 CSV rows); 8 bond cases; 1 checker; 1 plot
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; numpy 2.5.3 and matplotlib 3.11.2 are class B entries of tools/toolchain.lock.md section 2 without a TV record; no TV record covers hardware/sim/enclosure/*.py; developer evidence per 05 section 9.1)"]
values_proposed: ["REQ-SYS-177: 20 dB (keep), with the owner's choice of scope (a), (b) or (c) and the not-shown cases named in the PCR-9 ruling (revision 1; the 12.5 MHz to 1.5 GHz pass of C1 and D is not supported with a plug inserted: finding-5)", "REQ-SYS-109: 0.1 ohm (keep), with coating Rs <= 0.03 ohm/sq and two bond points per coated part (supported, AT RISK on CR-003 revision 3; finding-3)"]
renders_inspected: 2
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-analysis-shielding-iter1 (independent; authored no part of WP-PDR-27); iteration 2 by reviewer:WP-PDR-27-analysis-shielding-iter2 (independent; authored no part of WP-PDR-27 and no part of its revision 1)"
# criticality: a hardware enclosure analysis; it sets no value of a 07 section 14.1 component
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
# reviewer_verdict (iteration 2): NEEDS CHANGES; finding-1 (Major) Verified; new finding-5 (Major) Open: the rule O2
# jack-collar credit that the fix relies on does not hold with a plug inserted; findings 2 to 4 and 6 Minor, Open
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 3
findings_open: 4
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-A5, CK-ANA-B1, CK-ANA-B3, CK-ANA-E5, CK-ANA-F1]
effort_turns: 55
effort_minutes: 85
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: shielding and bond estimate (INSP-083, iteration 1)

**Product:** `docs/design/analysis/shielding-estimate.md` (`e600e9ee`) with its model and checker `hardware/sim/enclosure/shielding_estimate.py` (`3cc126cb`), outputs `out/shielding.csv` (`023cb5c8`) and `out/bond.csv` (`7af39c6b`), and the figure `docs/reviews/PDR/figures/shielding-estimate.png` (`3370418d`), at freeze commit `70a3a33` (rule C2). Every blob equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at `HEAD` `4ef04ee` on 2026-09-27. No product blob lives on a `cr/` branch. AT RISK on CR-003 revision 3 (REQ-SYS-109 as the bond requirement; the note's header says so).

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter comment). `analysis_kind` other (shielding) and worst-case: sections A to F, G7, H, I. G1 to G6 and J are N/A (no deck; not a budget, thermal, RF exposure, cascade or timing analysis; criticality neither).

**Acceptance criteria (rule C7, every case the governing clauses enumerate):**
- REQ-SYS-177 (`requirements.json`): "digital and switching-converter fundamentals and harmonics radiated from its enclosure at least 20 dB (TBR) below their board-level near-field levels". Its closing case TC-SYS-107 (`test_cases.json`): "every clock and switching-converter fundamental and its harmonics to 1.5 GHz", every aperture and seam, with the worst-case corner of every toleranced input.
- The REQ-SYS-177 `tbr.plan`: "The enclosure and clock-plan design at PDR confirms the shielding figure".
- REQ-SYS-109 as CR-003 revision 3 words it: every conductive enclosure part at most 0.1 ohm (TBR) from the jack shell, at the farthest point of every part.
- Plan WP-PDR-27 output: "`docs/design/analysis/shielding-estimate.md` (REQ-SYS-177 20 dB by coating sheet resistance, apertures, seams)"; bond resistance (REQ-SYS-109).
- Every option the note evaluates (A, B, C1, D) and both readings it defines (plane wave and H field).

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (analysis checklist, 47 CFR 15.23, switcher frequencies, TC-SYS-107) preceded every `grep`; `grep` only pinned lines in the research reports and CR-003. The rustos tree was not read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-F1, E3, E5 | note section 2 row "Source frequencies" ("1 GHz (upper edge of the evaluated range, author choice)"); sections 4.2, 5, 7 items 1 and 3, 9; checker `SOURCES`, `EXPECTED` | The governing closing case TC-SYS-107 names every fundamental and harmonic to 1.5 GHz. The note stops at 1 GHz by author choice, states its pass as "12 to 600 MHz", and proposes to keep 20 dB. The reviewer ran the note's own model at the harmonics above 1 GHz (min of plane wave and H field, rules applied): 1050 MHz (7th of 150 MHz) A 18.8, B 19.0, C1 19.8, D 19.8 dB; 1200 MHz A 17.7, B 17.9, C1 18.7, D 18.8 dB; 1500 MHz A 15.9, B 16.1, C1 17.0, D 17.0 dB. So by the note's model every option, the CNC fallback included, is below 20 dB from about 1 GHz to 1.5 GHz. Section 7 item 3 calls 1 GHz "marginal" and closes it by "the birdie survey at TRR and the near-field probe measurement", but REQ-SYS-177 is an Analysis requirement closed by TC-SYS-107 on the CDR design data (04 section 5.1 item 5), so a TRR measurement cannot close it. The proposed value is therefore not supported over the requirement's scope (E5). In addition, the 12 MHz (+4.5 dB) and 600 MHz (+3.9 dB) cases pass by less than the stated uncertainty of about +/-6 dB and are reported as passing (E3: a margin below its uncertainty is not reported as a pass). Fix: extend the source list to every harmonic to 1.5 GHz of every clock of the WP-PDR-20 clock plan and the converter harmonics between 1.5 and 12 MHz; report the cases below 20 dB; give the opening design rules that recover them (the largest common openings, USB 15.6 mm and the jack holes, set the total) or put the scope question to the owner with the 1.5 and 2.2 MHz one (PCR-9); and mark every case whose margin is below its uncertainty as not shown | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-ANA-A5 | note section 1 (H reading "source r = 10 mm from the wall, the front-stack clearance ... rounded up"); section 8 item 2; checker `R_SRC = 0.010` | Rounding the source distance up raises the H-field shielding, so it is not conservative. At r = 5 mm the note's formula gives 6.0 dB at 1.5 MHz (reviewer run) against 9.5 dB at 10 mm. Section 8 states that a closer source lowers the result, but not that the chosen value was rounded in the unfavourable direction for the margin; a converter inductor near the back wall of the heat-sink pocket or under the front wall can be closer than 10 mm (`board-outline.json` Z stack: top-side zone to 28.0 mm in a 30 mm case). Fix: state the direction, and take r from the WP-PDR-37 floorplan or bound it at the smallest wall clearance | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-B1 | note section 3 "Bond" and section 6; checker `bond_r` | The bond model is two circular contacts on an infinite sheet. A coated part is a finite strip or box face (for example a side wall about 30 mm deep and 140 mm long), where the current is confined and the resistance is higher: a 70 mm run on a 30 mm wide strip adds about Rs x L / W = 0.03 x 70 / 30 = 0.07 ohm before the contact constriction terms. With two bond points in parallel the result stays near 0.07 to 0.08 ohm, still under 0.1 ohm, so the value stands, but the stated "factor of 2 margin" is not shown. Fix: compute the bond on the narrowest coated part of the C1 model, or state the infinite-sheet result as a lower bound | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-B3 | note section 3 | No validation evidence for the model is given (a known answer or a published comparison for the slab and the slot-aperture terms). The reviewer's hand checks agree (section B5 below), so no number is in doubt, but B3 asks the note to show one. Fix: add two known answers, for example the thin-film limit 20 log10(1 + Z0 / (2 Rs)) and the 20 log10(lambda / (2 L)) slot term, each against the checker at one frequency | Open | Pending | |

One Major finding is open, so the reviewer verdict is NEEDS CHANGES. The note's treatment of the 1.5 and 2.2 MHz H-field shortfall is sound and is clearly put to the owner; the Major is about the frequency range above 1 GHz that the closing case covers, and about how near-limit cases are reported.

### Per-case results (section F; one row per case REQ-SYS-177, TC-SYS-107 and REQ-SYS-109 name)

| Case | Condition | Governing id and limit | Result (checker output or reviewer run of the same model) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | 1.5 MHz charger fundamental, H field, rules applied | REQ-SYS-177: 20 dB | A 69.6, B 48.2, C1 9.5, D 9.5 dB | A +49.6; C1 and D -10.5 dB | +/-2 dB (Rs) | hand: C1 wall 20 log10(1 + 0.118 / 0.06) = 9.4 dB; re-run same | none (shortfall stated, owner question) |
| C-2 | 2.2 MHz buck fundamental, H field | REQ-SYS-177: 20 dB | A 66.3, B 51.9, C1 11.8, D 11.8 dB | C1 and D -8.2 dB | +/-2 dB | re-run: same | none (stated) |
| C-3 | 1.5 and 2.2 MHz, plane wave | REQ-SYS-177: 20 dB | 71.8 to 76.4 dB, all options | +51.8 dB or more | +/-6 dB | hand: 20 log10(1 + 376.7 / 0.06) = 76.0 dB, C1 wall | none |
| C-4 | Converter harmonics between 1.5 and 12 MHz | REQ-SYS-177 | not listed; the H-field total of C1 and D rises with frequency and crosses 20 dB near 8 MHz (plot, right panel) | C1 and D negative below about 8 MHz | +/-2 dB | read from the plot | finding-1 |
| C-5 | 12 MHz crystal | REQ-SYS-177 | C1 24.5 dB (H), 59.1 dB (plane) | +4.5 dB | +/-6 dB | re-run: same | finding-1 (margin below uncertainty) |
| C-6 | 48, 144, 150, 300 MHz | REQ-SYS-177 | lowest C1 28.5 dB at 300 MHz; lowest A 27.7 dB | +7.7 dB or more | +/-6 dB | re-run: same | none |
| C-7 | 600 MHz | REQ-SYS-177 | A 23.0, B 23.1, C1 23.9, D 23.9 dB | +3.0 to +3.9 dB | +/-6 dB | re-run: same | finding-1 |
| C-8 | 750 and 900 MHz (5th and 6th of 150 MHz) | REQ-SYS-177 | A 21.3 and 20.0 dB; C1 22.3 and 21.0 dB | 0.0 to +2.3 dB | +/-6 dB | reviewer run of `total_se` | finding-1 |
| C-9 | 1000 MHz | REQ-SYS-177 | A 19.1, C1 20.2 dB | -0.9 to +0.2 dB | +/-6 dB | re-run: same | finding-1 |
| C-10 | 1050 to 1500 MHz (7th to 10th of 150 MHz; the 48 MHz harmonics above 1 GHz) | TC-SYS-107: every harmonic to 1.5 GHz | at 1050 / 1200 / 1500 MHz: A 18.8 / 17.7 / 15.9 dB; C1 19.8 / 18.7 / 17.0 dB | A -1.2 to -4.1 dB; C1 -0.2 to -3.0 dB | +/-6 dB | reviewer run of `total_se` | finding-1 |
| C-11 | Window without film; screw-only joints (variants) | REQ-SYS-177 design rules | below 20 dB at 600 MHz, and from about 300 MHz | negative | +/-6 dB | re-run: same | none (rules adopted) |
| C-12 | Bond at 0.03 ohm/sq, one and two bond points, farthest point 140 and 70 mm | REQ-SYS-109 (CR-003): 0.1 ohm | 0.0545 and 0.0479 ohm | +0.046 and +0.052 ohm | contact 0.010 ohm (Low); part geometry | hand: 0.03 / (2 pi) x (ln 20 + ln 140) + 0.010 = 0.0479 ohm | finding-3 |
| C-13 | Bond at 0.1 and 0.7 ohm/sq | REQ-SYS-109 | 0.136 to 1.05 ohm | negative | as above | re-run: same | none (sets the bound near 0.07 ohm/sq) |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse 70a3a33:<path>` | Yes | 5 of 5 equal, and equal at `HEAD` `4ef04ee` |
| R2 | The checker runs by the one command the note names and exits as stated | Yes | Scratchpad export of `70a3a33`: `.venv/bin/python hardware/sim/enclosure/shielding_estimate.py --check` exit 0, `CHECK PASS` |
| R3 | `validate_docs.py` on a JSON product | N/A | No JSON product under a schema |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary item 2 (shielding) and note sections 1 to 9 |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note; REQ-SYS-177 and REQ-SYS-109 named with their TBR |
| R6 | Every render the note cites exists | Yes | `docs/reviews/PDR/figures/shielding-estimate.png` present |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Header row "Serves": REQ-SYS-177, REQ-SYS-109, TS-011 M5 and C4, TC-SYS-107 and TC-SYS-075; each id exists (`requirements.json`, `test_cases.json`) |
| CK-ANA-A2 | Yes | Design data: `board-outline.json` (openings, wall depths), TS-011 section 8 rules 7 and 8, ICD-CTL-USB 3.2.2; AT RISK on CR-003 revision 3 stated in the header |
| CK-ANA-A3 | Yes | Input table (section 2): every row has a source and confidence. Switcher frequencies checked against `docs/research/power-tree-and-charging.md` F19 (TPS62913 "2.2 MHz or 1 MHz fixed frequency") and R-PWR-03 ("The 5 V buck (2.2 MHz), the charger boost (1.5 MHz)"); coating values recalled and labelled Low |
| CK-ANA-A4 | Yes | Every input that sets a result was checked: frequencies (above); 6061 conductivity 2.5e7 S/m (about 40 % IACS, textbook); wall thicknesses against `board-outline.json` (`wall_thickness_printed` 2.0, `wall_thickness_cnc_fallback` 1.5); openings (USB 12 x 10 mm gives the 15.6 mm diagonal; jack 9.0 mm and encoder 8.5 mm against the tolerance note S2 and S3; the checker uses 8.4 mm for the encoder holes, 0.1 mm under S3, which changes no total by more than 0.1 dB); window 24 x 24 mm (34 mm diagonal); seam lengths (Low). No disagreement that changes a result |
| CK-ANA-A5 | No | Assumptions stated; the direction of the source-distance rounding is not (finding-2) |
| CK-ANA-A6 | Yes | Consequences routed: the owner question (a), (b), (c) and PCR-9; design rules to TS-011 rules 7 and 8, WP-PDR-39 and WP-PDR-25; no requirement edited |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Slab, slot and power-sum model stated with its simplifications (section 3; section 8 item 1); the bond model's infinite-sheet simplification is not stated with its effect (finding-3) |
| CK-ANA-B2 | N/A | No vendor model |
| CK-ANA-B3 | No | No validation evidence in the note (finding-4) |
| CK-ANA-B4 | Yes | Closed form; frequency points are the named sources plus a 300-point log sweep for the plot |
| CK-ANA-B5 | Yes | Reviewer hand checks: H-field wave impedance at 1.5 MHz and r = 10 mm, 2 pi x 1.5e6 x 4 pi e-7 x 0.01 = 0.118 ohm, thin-film SE 20 log10(1 + 0.118 / 0.06) = 9.4 dB (checker 9.47); plane-wave thin film 20 log10(1 + 376.7 / 0.06) = 76.0 dB (CSV wall 76); slot term at 600 MHz for the 15.6 mm USB opening, 2 x 0.0156 / 0.5 = 0.0624, that is 24.1 dB before the depth term; bond 0.0479 ohm (C-12). All agree |
| CK-ANA-B6 | Yes | Uncertainty stated: about +/-6 dB for the aperture and joint terms, +/-2 dB from Rs for the wall term (section 5 table, section 8) |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | venv Python 3.13.5, numpy 2.5.3, matplotlib 3.11.2 named in the header, as `tools/toolchain.lock.md` section 2 lists them |
| CK-ANA-C2 | Yes | No TV record covers the script; the note marks every number developer evidence and holds the values as proposals until this record is APPROVED (header "Evidence status") |
| CK-ANA-C3 | Yes | One headless command, named in section 3 |
| CK-ANA-C4 | Yes | Re-run on a scratchpad export of `70a3a33`: exit 0; the regenerated `shielding.csv`, `bond.csv` and `shielding-estimate.png` hash to the frozen blobs (byte-identical) |
| CK-ANA-C5 | N/A | No TV record, so no stated tool limitation |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | dB, ohm/sq, ohm, MHz and m used consistently in the note, CSV and checker |
| CK-ANA-D2 | Yes | Section 4.1 table equals `shielding.csv` (every row compared); section 6 table equals `bond.csv`; the plot annotation (9.5 and 11.8 dB) equals the CSV; TS-011 section 4 quotes the same values |
| CK-ANA-D3 | Yes | Values rounded to 0.1 dB; no rounding changes a verdict |
| CK-ANA-D4 | Yes | `SE_REQ = 20.0` with the comment "REQ-SYS-177 (TBR)"; bond limit 0.1 in `meets_0p1` and `EXPECTED_BOND` |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | 20 dB and 0.1 ohm quoted with their ids; REQ-SYS-109 from CR-003 revision 3 (AT RISK) |
| CK-ANA-E2 | Yes | Section 5 margins, convention result minus limit, signs right |
| CK-ANA-E3 | No | Margins below the stated uncertainty reported as passing (finding-1) |
| CK-ANA-E4 | Yes | `--check` asserts the stated verdict set per option (five booleans) and four bond cases and exits 1 on any difference. It asserts verdicts, not a value per frequency, which is adequate for a screen |
| CK-ANA-E5 | No | REQ-SYS-177: the value (keep 20 dB) is not supported over the TC-SYS-107 range (finding-1). REQ-SYS-109: supported, with the design value Rs <= 0.03 ohm/sq and its coupon check |
| CK-ANA-E6 | N/A | No TPM estimate proposed |
| CK-ANA-E7 | Yes | No credit claimed: developer evidence on pre-build design data; TC-SYS-107 closes at CDR |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Per-case table above: the harmonics above 1 GHz (C-10) and the converter harmonics between 1.5 and 12 MHz (C-4) are not analysed (finding-1) |
| CK-ANA-F2 | Yes | Off-nominal variants analysed: window without film, screw-only joints, coating classes 0.01 to 20 ohm/sq |
| CK-ANA-F3 | Yes | The worst combination is stated: the lower of plane wave and H field at each frequency, with the largest common openings setting the total above 12 MHz |
| CK-ANA-F4 | Yes | Near-limit cases show the sensitivity to the two largest inputs: Rs (coating sweep, section 4.3) and the openings (window and joint variants) |

## G7. Worst-case

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Method stated: power (random-phase) sum, with its limitation (section 8 item 1) |
| CK-ANA-G7-2 | N/A | No component tolerance, temperature coefficient or ageing inputs of the derating kind |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes | REQ-SYS-109 carries HZ-009 (bond, arcing); the note changes no control and routes the bond value through TS-011 and CR-003 |
| CK-ANA-H2 | Yes | The low-frequency shielding risk is submitted through TS-011 section 7 (new, CR-003 candidate (a)) to the WP-PDR-18 writer |
| CK-ANA-H3 | N/A | Revision 0 at its first freeze; the note has no change history section, which revision 1 should add |

## I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | `docs/reviews/PDR/figures/shielding-estimate.png` opened with the Read tool (1 render) |
| CK-ANA-I2 | Yes | Left panel: wall-only shielding against frequency for five coating classes (H field) and the plane wave at 0.03 ohm/sq, the 20 dB line labelled "REQ-SYS-177: 20 dB (TBR)", axes with units, 6061 noted as off scale in the legend. Right panel: totals per option, solid plane wave and dashed H field, window and joint variants, source frequencies as grey lines, the C1 and D annotation at 1.5 MHz. The plot runs to 1.5 GHz and shows every total at or below 20 dB at the right edge, the case of finding-1. The plotted values agree with the CSV at the marked points |

## Items N/A

CK-ANA-G1 to G6 (not a deck, budget, thermal, RF exposure, cascade or timing analysis), CK-ANA-J1 to J3 (criticality neither), CK-ANA-B2, C5, E6, G7-2, H3, readiness R3.

## Cross items for the lead SE (not findings on the note)

- **X-1.** The checklist field names `peer-review-checklist-design` because the analysis template is on the CR-012 branch only (front matter comment); switch it at the delta iteration after CR-012 merges.
- **X-2.** TS-011 M5 (INSP-081 finding-3) depends on the disposition of finding-1.
- **X-3.** TC-SYS-107's `automation_ref` is `tools/budgets/enclosure_shielding.py` (planned), while the analysis model is `hardware/sim/enclosure/shielding_estimate.py`; the test-case writer should reconcile the path when the case is updated under CR-003 (its section 1.6 row TC-SYS-107).

## Commands

- `git rev-parse 70a3a33:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` at `4ef04ee` for the 5 product files: equal.
- Scratchpad export of `70a3a33`: `shielding_estimate.py --check` exit 0; outputs byte-identical.
- Reviewer run of the note's own functions (`total_se`, `slab_se`, `zw_h`) at 750, 900, 1050, 1200 and 1500 MHz and at r = 5 mm: values in the per-case table and in finding-1 and finding-2.
- `.venv/bin/python tools/validate_docs.py`: this record passes.

## Measurements (SWE-089)

Items checked 40 (A1 to A6, B1 to B6, C1 to C5, D1 to D4, E1 to E7, F1 to F4, G7-1, G7-2, H1 to H3, I1, I2) plus readiness 6; items answered No 6; findings 1 Major, 3 Minor; fixed 0, deferred 0; iteration 1; renders inspected 1; inputs checked 11; effort about 30 turns and 45 minutes (session shared with INSP-081, 072, 074).

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, HEAD `d1148c2`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fix of finding-1 only. Findings 2 to 4 (Minor) were not addressed by the author (note change log, revision 1 row) and are not re-reviewed. Product: the 6 blobs of front matter `product_files`, committed as `70d11ef` (note revision 1, re-freeze F0). Each equals `git rev-parse 70d11ef:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (6 of 6). `git log 70d11ef..HEAD` shows no later change to any product file. No blob is on a `cr/` branch. Checklist as iteration 1: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` at `7784672` (not merged at `d1148c2`).

**Independence (rule C4).** This invocation authored no part of WP-PDR-27 and no part of revision 1. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. `grep` then only pinned lines in known paths (the note, the script, `docs/design/analysis/clock-plan.md`). The rustos tree was not read.

**Reproduction.** On a `git archive 70d11ef` export in the scratchpad: `shielding_estimate.py --check` exit 0, `CHECK PASS`; the regenerated `shielding.csv`, `shielding-sources.csv`, `bond.csv` and `shielding-estimate.png` hash to the frozen blobs (4 of 4 byte-identical). Reviewer runs of the note's own `total_se` (lower of plane wave and H field) at 600, 900, 1050, 1200 and 1500 MHz for A and C1 with the `rev0` and `rev1` opening sets reproduce the section 4.1 table to 0.1 dB, and C1 `rev1` gives 24.5 dB at 12 MHz, 22.2 dB at 9 MHz, 20.0 dB at 6.8 MHz and 19.0 dB at 6 MHz, as the note states. Hand check of the rule O1 to O3 terms at 1.5 GHz (lambda 200 mm): USB mouth 7.5 mm with 5 mm depth 40.7 dB; jack collar 9 mm with 8 mm depth 45.2 dB; encoder contact slot 3 mm with 2 mm depth 48.7 dB; against 19.6 dB for the revision 0 USB opening (15.6 mm, 2 mm). The 8 to 9 dB recovery at 1.5 GHz follows.

### Verification of finding-1, case by case (rule C7)

| # | Case the finding named | Check | Result |
|---|---|---|---|
| 1 | Every harmonic to 1.5 GHz of every clock of the WP-PDR-20 clock plan | Section 2 source row and `CLOCK_SOURCES`: 19 sources, checked against `clock-plan.md` revision 2 (`4153acf`) section 2 (every row whose status is fixed, proposed, option, tx-only, off in operation or boot) and section 2.1 (R-1 to R-5). The rejected rows (TCXO 26 and 27 MHz, SPI d 26 to 48, audio PWM 146.484 kHz, free-running buck, PCM1808 12.288 MHz) are correctly left out. Tolerance band ends taken (for example ROSC 14.3 MHz +/-67.8 % gives 4.6 to 24.0 MHz; R-4 0.377 MHz +/-5.3 % gives 357 to 397 kHz). Harmonics to 1500 MHz at the nominal and both band ends (`per_source`) | Yes (allowed-but-unproposed divisors: observation O-1 below) |
| 2 | The converter harmonics between 1.5 and 12 MHz | In the set through the harmonics of the buck, charger, R-1 to R-5, PWM and ROSC; section 4.2 gives the fail spans (for example charger boost 1.35 to 6.75 MHz) | Yes |
| 3 | Report every case below 20 dB | Section 4.1 bold cells; section 4.2 per-source verdicts (9 sources fail for C1 and D from 0.03 to 6.8 MHz; B fails R-5); section 4.3 checker verdicts; section 5 status column; the revision 0 "marginal" statement withdrawn | Yes |
| 4 | Opening design rules that recover the upper range, or the scope question to the owner | Rules O1 to O3 (section 7 item 2; TS-011 rule 16) and the owner question (section 7 item 3, options (a) to (c), with the finding that board shield cans alone no longer close it), plus the 1.5 GHz edge to the CDR analysis or a named acceptance (item 4) | Yes, for the unplugged state (the plug-inserted state: new finding-5, Major) |
| 5 | A margin below its uncertainty reported as not shown (E3) | Section 3 verdict rule with 6 dB; `per_source` applies it per harmonic; section 5 status column; XOSC, QSPI 12.5 MHz, PCM1808 and BFO "not shown" for C1 and D; every source "not shown" for A and B at 1.5 GHz. The 6 dB covers the H-field wall term at a 5 mm source (reviewer: 24.2 dB at 12 MHz for r = 10 mm against 18.9 dB for 5 mm, a 5.3 dB shift) | Yes |
| 6 | TC-SYS-107 is closed on CDR design data, not a TRR measurement | Section 7 item 4 says so and puts the near-field probe measurement as supporting data | Yes |

**Result: finding-1 Verified** for what it asked. The rule that carries its upper-range result has a defect in the plug-inserted state, raised as finding-5.

### Findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-F1, E3, E5 | note sections 2 to 5, 7, 9; script `CLOCK_SOURCES`, `per_source` | See iteration 1 | Verified (iteration 2, revision 1 at 70d11ef) | n/a | |
| finding-2 | reviewer | Minor | CK-ANA-A5 | note section 1 | Not in the delta (section 3 now cites it for the 6 dB uncertainty; the direction of the rounding is still not stated in section 1) | Open | Pending | CDR readiness declaration (lien) |
| finding-3 | reviewer | Minor | CK-ANA-B1 | note section 6 | Not in the delta | Open | Pending | CDR readiness declaration (lien) |
| finding-4 | reviewer | Minor | CK-ANA-B3 | note section 3 | Not in the delta | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-5"></a>finding-5 | reviewer | Major | CK-ANA-F1, E5 | note section 2 row "Other openings" (revision 1 set), section 7 item 2 rule O2 and the item 2 conclusion "C1 and D pass from 12.5 MHz to 1.5 GHz"; section 4.2 "pass" rows; script `OPENINGS["rev1"]` (jack holes `(0.009, depth + 0.006)`); TS-011 rule 16 and the M5 cells | **The rule O2 below-cutoff credit does not hold with a plug in the jack, which is the operating state.** O2 gives each 9 mm jack opening 8 mm of waveguide-below-cutoff depth (27.3 x 8 / 9 = 24.3 dB). Below-cutoff attenuation exists only for an empty opening. With a 3.5 mm plug inserted, its metal sleeve runs through the collar into the jack and is connected to board ground at the jack's sleeve contact, so the collar and the sleeve form a coaxial line, which has no cutoff. The key jack holds the key or paddle plug in every transmit and receive state, and REQ-SYS-117 itself names the "plugs inserted" state; TC-SYS-107 covers "every aperture" at the worst-case corner. The reviewer ran the note's own `total_se` with the O1 and O3 terms kept and the two jack terms changed: with the depth credit removed (9 mm, no depth) C1 gives 21.3 dB at 900 MHz, 20.1 at 1050, 19.1 at 1200 and 17.3 dB at 1500 MHz (A 21.1, 20.0, 19.0, 17.2 dB); with the wall depth only (2 mm) C1 gives 22.0 dB at 1500 MHz (A 20.7). So with a plug in, every source whose harmonics reach about 1.1 GHz is a fail or at best not shown, not the "pass" of section 4.2, and a coaxial penetration can leak more than this aperture estimate. That changes the answer the owner gets at PCR-9: under option (a), C1 and D do not meet 20 dB from 10 MHz up with the key plugged in, and under option (c) A does not either. **Why Major:** the proposed REQ-SYS-177 ruling (rule C10) and TS-011 M5 and condition 3 rest on a pass that does not hold in the operating state (E5), and a case TC-SYS-107 names is not analysed (F1). **Fix:** add the plug-inserted state as a case for both jacks (and the USB with a cable, whose plug shell mates the O1-bonded receptacle shell, which the note should state). Either give a rule that closes the penetration at the wall (for example the jack's sleeve contact, or a metal-bodied panel jack, bonded all round to the collar or coating; or a filtered, grounded entry) and credit it by a stated model, or report the plug-inserted cases as fail or not shown and carry them by name into the PCR-9 question and TS-011 M5 and condition 3 | Open | Pending | |

One Major finding is open, so the reviewer verdict is NEEDS CHANGES (iteration 3 is a delta on finding-5; rule C1 allows it).

### Observation (not a finding)

- O-1. The clock plan also allows SPI SCK = 150 / d for every even d from 2 to 24 and QSPI SCK = 150 / CLKDIV for CLKDIV 1 to 24 ("allowed (clear set)"); only the proposed values are modelled. An allowed divisor below about 7 MHz (SPI d 22 or 24, 6.8 and 6.25 MHz; QSPI CLKDIV 22 to 24) would fail in C1 and D like the other sources below 7 MHz; above it every allowed value falls in the band the note already covers. No verdict changes; the note could say the model covers the proposed values and name the bound.

### Visual closure (iteration 2)

`docs/reviews/PDR/figures/shielding-estimate.png` (revised, three panels) opened with the Read tool. Left: wall-only shielding against frequency from 0.02 MHz for five coating classes (H field) and 6061, with the 0.03 ohm/sq plane-wave line and the labelled 20 dB line. Middle: the total (lower of plane wave and H field) for A and C1 with the revision 0 openings (dotted) and rules O1 to O3 (solid), 0.02 to 1500 MHz, with the fail band below 20 dB and the not-shown band 20 to 26 dB shaded and labelled; the C1 curve crosses 20 dB near 7 MHz and ends near 26 dB; the revision 0 curves end near 16 to 17 dB. Right: per-source lowest totals for C1 (plain) and A (hatched) coloured by verdict, with values and verdicts written at each bar; the values match section 4.2 (for example C1 8.9 fail for the charger boost, 26.2 pass for clk_sys, A 25.4 not shown). Long source names are cut at 38 characters on the axis ("R-3 TPA6130A2 charge pump 300 to 500 k"), cosmetic. The plug-inserted state of finding-5 is not shown in the figure.

### Cross items (iteration 2, returned to Claude)

- X-4. INSP-081 (TS-011) iteration 2 carries finding-5 as its cross item X-5: TS-011 section 1 finding 3, the M5 cells and condition 3 change with the fix.
- X-5. The `checklist` field still names `peer-review-checklist-design` (X-1 of iteration 1); switch it after CR-012 merges.
- X-3 of iteration 1 (TC-SYS-107 `automation_ref`) still applies.

### Completion criteria (SWE-088), iteration 2

Not met on the reviewer side: finding-5 (Major) is open. `reviewer_verdict: NEEDS CHANGES`; record `verdict: NEEDS CHANGES`. Findings 2 to 4 are Minor liens due at the CDR readiness declaration (plan rule C1).

```
ITERATION 2 (2026-09-27, HEAD d1148c2, product commit 70d11ef): REVIEWER VERDICT: NEEDS CHANGES; RECORD VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] finding-1: Verified (19 clock-plan sources with every harmonic to 1.5 GHz and the band ends; cases below 20 dB reported; rules O1 to O3 and the PCR-9 question; not-shown rule at 6 dB).
- [Major] finding-5 (new): the rule O2 jack-collar below-cutoff credit does not hold with a plug inserted; C1 17.3 dB at 1.5 GHz without it (Open).
- [Minor] finding-2 to finding-4: Open, not in the delta (liens).
MEASUREMENTS: blobs equal HEAD 6/6; checker CHECK PASS exit 0; outputs byte-identical 4/4; cases 6 (6 Yes, 1 with a new Major); reviewer model runs 5 frequencies x 2 options x 4 opening sets; renders inspected 1; major open=1; minor open=3; turns=25; minutes=40 (cumulative 55 and 85); iteration=2
```
