---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.2 and 3.4). Independent review of the WP-PDR-33 keyer host
# study at the record path PDR work plan WP-PDR-33 "Records" names. Iteration 1 at freeze F0 (rule C2).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Submitted, not merged).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-design revision B (the software design checklist, nearest main template for a
# keyer timing design analysis) and checklist_analysis records the template actually applied (the INSP-038
# and INSP-050 form); the delta after CR-012 merges switches the field.
# The software assurance pair is a separate invocation, filed as
# docs/reviews/PDR/checklists/analysis-keyer-host-study-software-assurance.md (PDR work plan WP-PDR-33
# "SA for the keyer safety values"; the note sets values of safety-critical SW-KEYER and SW-SAFE, 07
# section 14.1).
id: INSP-071
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-keyer-host-study.md
product: docs/design/analysis/keyer-host-study.md
# product_commit (iteration 2): 8c12b5a, the WP-PDR-33 revision 2 commit that fixes the Major findings of
# iteration 1 (freeze F0 again, rule C2). The 8 blobs below equal git rev-parse 8c12b5a:<path>, HEAD:<path> and
# git hash-object at HEAD 1bde213; all are on main. product_files_iteration_1 keeps the 82cf086 blobs.
product_commit: "8c12b5ad9134ce7f3b2605be4a61dc3fac392807"
product_files: ["docs/design/analysis/keyer-host-study.md@1dd0fb7d4c047e54e6bfabf73145ff1cd4c97590", "docs/design/analysis/keyer-host-study/keyer_model.py@d28613af318d2d7e0160973329512e2b88b71d98", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@f72f3a6ac5a6684f8a1b793a954dfb1f8b6ad524", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@7f4f0afdc013ffa43c124ff36c4d87de74a0ec97", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@e9d3687accd75b5821b351e606922630d6ae5325", "docs/design/analysis/keyer-host-study/keyer-nogap-fault-coverage.png@63395cf1c0eb4b9341f13f3259f00acba876091a", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103"]
product_files_iteration_1: ["docs/design/analysis/keyer-host-study.md@39b43044230ce9513b525e6b4417b722d1eebe6d", "docs/design/analysis/keyer-host-study/keyer_model.py@39e6f92cffd45c9aa60d29fdd485633a6b77f748", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@0fda48d9630b4d85d90d6f5b17f3c67b277ae4c2", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@ef3d199da4f4bbb771de55e911f788b4ed024282", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@514851a41e0b6f599bad00a350be87e3a4f44f3a", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103"]
analysis_kind: [timing, worst-case]
# product_size: iteration 1 text first; iteration 2 (8c12b5a): note 339 lines, model 894 lines, checker 751 lines and
# 555 assertions, 4 plots
product_size: 1 note (276 lines, 12 sections), 1 model (631 lines), 1 checker (522 lines, 348 assertions), 1 results file, 3 plots; 10 requirement values (G13 9 TBRs plus REQ-SW-KEYER-036), 25 per-case rows in this record
tools_used: ["venv Python 3.13.5 (TV-001, accredited for schema validation only; not for this model)", "keyer_model.py and check_keyer_host_study.py at 82cf086 (iteration 1) and 8c12b5a (iteration 2) (no TV record)", "matplotlib 3.11.2 (plots only, no TV record)"]
values_proposed: ["REQ-SYS-052: 500 ms (unchanged)", "REQ-SW-KEYER-022: 500 consecutive samples (unchanged)", "REQ-SYS-053: 5 s, build range 2 to 6 s (unchanged)", "REQ-SW-KEYER-026: 5 s (unchanged)", "REQ-SYS-054 (revision 2): in every key mode on the TX_KEY read-back, 128 consecutive equal elements with no word gap or 128 elements repeating with a period of 1 to 6, or 30 s without a qualifying gap (at least 2 x the shortest key-up interval of the preceding 10 s, or 2 s) (gap and count definitions changed, CR, PCR-9)", "REQ-SYS-184: the longer of 2 s and 20 dit times at the configuration-guarded selected speed, 50 WPM on a guard failure (changed, CR, PCR-8)", "REQ-SYS-131: 2 s (unchanged), design watchdog load 1.0 s", "REQ-SYS-188: 120 s (unchanged)", "REQ-SYS-189: 60 s (unchanged)", "REQ-SW-KEYER-036: unchanged, no plug = detect input reads high"]
renders_inspected: 4
sprint: PDR-prep
author_agent: "author:WP-PDR-33 wave 1a (Claude as software lead, keyer)"
reviewer_agent: "reviewer:WP-PDR-33-keyer-host-study-iter1 (independent; authored no part of WP-PDR-33); iteration 2 by reviewer:WP-PDR-33-keyer-host-study-iter2 (independent; authored no part of WP-PDR-33 and no part of its revision 2)"
# criticality: the note sets values of the safety-critical keyer (SW-KEYER) and safe-state manager
# (SW-SAFE) monitors, 07 section 14.1
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-33-keyer-host-study (paired record INSP-075, docs/reviews/PDR/checklists/analysis-keyer-host-study-software-assurance.md; 07 section 2.1.1)"
paired_record: INSP-075
iteration: 2
readiness_met: true
# reviewer_verdict (iteration 2): APPROVED; finding-1 (Major) Verified; findings 2 to 4 and the new finding-5 are
# Minor and Open (liens due at the CDR readiness declaration, plan rule C1)
reviewer_verdict: APPROVED
# assurance_verdict: copied from the paired record INSP-075 (iteration 1, NEEDS CHANGES, 2 Major); its iteration 2
# delta is a separate invocation and has not yet run
assurance_verdict: NEEDS CHANGES
# verdict: held at NEEDS CHANGES until INSP-075 is APPROVED (07 sections 2.1.1 and 10.2) and, per the lead SE
# convention of 2026-09-27, until CR-012 merges with the analysis template blob 0386cc6e unchanged
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 4
findings_open: 4
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 2
assurance_findings_minor: 3
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-F1, CK-ANA-A5, CK-ANA-B3]
effort_turns: 84
effort_minutes: 130
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: keyer host study (INSP-071, iteration 1)

**Product:** `docs/design/analysis/keyer-host-study.md` blob `39b43044` at freeze commit `82cf086` (freeze F0, PDR work plan rule C2), with its model `keyer_model.py` (`39e6f92c`), checker `check_keyer_host_study.py` (`0fda48d9`), results `keyer-host-study-results.json` (`ef3d199d`) and plots `keyer-squeeze-vs-speed.png` (`010c2daf`), `keyer-nogap-vs-speed.png` (`514851a4`), `keyer-squeeze-timeline.png` (`e474a5ca`). Every blob equals `git rev-parse 82cf086:<path>` and `HEAD:<path>` on 2026-09-27. No product blob lives on a `cr/` branch, so the lead SE convention for unmerged blobs does not apply.

**Checklist:** `docs/templates/peer-review-checklist-analysis.md` revision A (CR-012 branch blob `0386cc6e`), sections R, A to F, G6, G7, H, I, J (analysis_kind timing and worst-case; criticality safety-critical). Sections J1 to J3 are answered here as evidence for the software assurance pair, which gives the assurance verdict.

**Acceptance criteria (rule C7, every case the governing clauses enumerate).** The G13 TBRs of plan section 10.2 (REQ-SYS-052, 053, 054, 131, 184, 188, 189; REQ-SW-KEYER-022, 026) and REQ-SW-KEYER-036 (G14, placed in this note), each with the cases its `description`, `tbr.plan` and `verification_note` name at `docs/requirements/sys/requirements.json` blob `f128235e` and `docs/requirements/sw/sw-keyer/requirements.json` blob `f9141160`; the WP-PDR-33 output list (synthetic 5 to 50 WPM corpus with Bug dahs and squeezed characters; the REQ-SYS-184 2.64 s case and the "longer of 2 s and 16 dits" branch; the REQ-SYS-054 no-gap watchdog; the watchdog period against the longest loop); the "TBR finding 7 check" (REQ-SYS-054 wording, SRR `requirements-sys.md` finding-28); the HZ-004 K4 `tbr` plans in `docs/safety/hazards.json` blob `81cacde4`; both key types where keying matters (CK-ANA-F1).

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (record rules and validator, TBR finding 7, watchdog mode scope, RF exposure separation values, 07 section 2.1.1) preceded every `grep`, which only pinned lines of files the search returned or of known paths. No rustos file was read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-F1, CK-ANA-A5 | Note section 3.2 ("Bug and Straight are not simulated"), section 3.4, section 6.2, section 7 row "Correct sending 5 to 50 WPM never trips", section 8 row REQ-SYS-054 | The REQ-SYS-054 `tbr.plan` asks that "no legitimate sending at 5 to 50 WPM" reaches the watchdog, and the WP-PDR-33 output list names a corpus "with Bug dahs". The corpus is keyer-timed paddle sending only. HZ-004 K4 (i) and (ii) run on the TX_KEY read-back "whatever the element pattern", and the note does not state in which key modes they run. In Bug mode the dahs and every letter and word space are operator-timed, so A-6 (letter spaces of at least 2 dits of the selected speed) is not shown for Bug sending. If K4 (ii) also runs in Straight mode, "dit times at the selected speed" has no defined relation to hand-sent spacing. Reviewer run with the frozen model: the QSO corpus hand-sent at 20 WPM with the keyer speed set to 5 WPM trips both rules at 30.24 s (proposed gap 480 ms, word space 420 ms). So the proposed gap value is not shown to meet its own acceptance criterion for every key type. Fix: state the key modes in which REQ-SYS-054 (i) and (ii) run and the dit length used in each. Add Bug-mode sending (manual dah lengths up to the note's 6 dits, operator spacing profiles referred to the Bug dit speed) to the corpus and the per-case table. Then show the proposed rule trips none of it, or restrict the proposed CR wording to the modes analysed | Verified (iteration 2, revision 2 at 8c12b5a) | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-ANA-F1 | Note section 7 (claims "Every case the governing requirement text or its verification note names") | Two named sub-cases have no row and no result. First, the REQ-SYS-054 verification note "then release of one lever and of both", with keying resuming only after both contacts read open. Second, the REQ-SYS-184 verification note "stays ended until a contact opens" and its rationale "Keying resumes once either contact opens". Neither sets a TBR value, and the note already raises the either-or-both conflict with ConOps Table 3.4-4 row 3 as request R-6. Fix: add the rows, marked "behaviour, no value; HostUnit on the flight keyer (WP-PDR-41)", or reword the section 7 claim | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-A5, CK-ANA-F4 | Note section 6.4 ("The longest legitimate manual closure is taken as a 6-dit dah at 5 WPM, 1.44 s"); section 4 | This value sets both margins of REQ-SYS-053: default 3.56 s, and 0.56 s at the 2 s range floor. It is written inline, not as a numbered assumption with direction and invalidation. The note shows no sensitivity for a hand key sent slower than 5 WPM: a 6-dit dah reaches the 2 s floor at 3.6 WPM, and the floor margin is within twice any plausible spread of hand timing. Fix: add it as assumption A-10 (slowest hand-sending speed, longest dah in dits) with its direction and what would invalidate it, and state the floor margin's sensitivity to it | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-B3 | Note section 5.1 item 1 ("all 19 iambic golden vectors of F7 (V1 to V13 with the A and B variants)"); `keyer_model.py` lines 218 to 242 | `docs/research/keyer-verification-and-key-input-network.md` F7 lists V2, V3, V4, V5, V11 and V12 for modes "A, B". The model runs them in mode A only, and B only for V1, V6 to V10 and V13. The reviewer ran those six in mode B at S = 0 and S = 0.5 with the frozen model, and all 12 match the expected intervals, so no result changes. Fix: add the six B variants to `GOLDEN_F7`, or state the count exactly (19 runs covering 13 vectors, B variants of V1, V6 to V10, V13) | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer (iteration 2) | Minor | CK-ANA-A5, CK-ANA-F1 | Note section 4 row A-5 ("the revision 2 rule does not depend on it"); section 6.2 "Correct sending under revision 2" and its bold "Confirmed for every key mode"; section 3.4 corpus texts | The revision 2 count (i-a) is not reset by a letter space, and the period count (i-b) matches a character repeated with letter spaces. So revision 2 does depend on A-5: a run of identical characters sent without a word space trips it once it holds 128 elements. Reviewer runs of the frozen `watchdog_relative`, paddle timing, nominal 3/7 spacing: 40 x V trips by the period count at 92.4 s (5 WPM), 23.1 s (20 WPM) and 9.24 s (50 WPM); 30 x 5 by the count at 73.2, 18.3 and 7.32 s; 30 x 0 at 134.6, 33.7 and 13.5 s; 40 x H at 76.1, 19.0 and 7.61 s; 50 x R by the period count at 102.5, 25.6 and 10.2 s. Hand-sent (H1, seed 1) runs of 5 and R also trip at 5 and 20 WPM, and of 0 at 5, 20 and 50 WPM. The baselined rule trips none of the V and R runs at any of these speeds, and none of these runs at 5 WPM. The corpus stops at 10 repeats (`0000000000`, 50 elements), and A-5 (20 characters) keeps every one of these runs below 128. So the value is sound for the corpus, but the note's statement that the rule does not depend on A-5 is wrong, and a continuous run of V test signals (33 V or more at 20 WPM) now trips where it did not before. Minor, because the trip is on the nuisance side, the runs are outside the stated corpus, and 20 x V (80 elements) and "VVV" groups with word spaces do not trip. Fix: correct the A-5 direction column (revision 2 depends on A-5 through items (i-a) and (i-b)); state the longest same-character run the rule admits (reviewer run at 20 WPM, nominal spacing: the first trip is at 26 x 5 or 26 x 0, 32 x H, 33 x V and 43 x R without a word space) as a limit of "legitimate sending" for the owner's ruling; add a repeated-character run to the corpus or the per-case table; the R-7 recording, if made, includes a test-signal run | Open | Pending | |

One Major finding: `reviewer_verdict` NEEDS CHANGES (07 section 10.2; PDR work plan rule C1). The squeeze, interlock, manual-timeout, hang-recovery, bench-timeout and plug-presence results were re-checked and stand. The REQ-SYS-054 count (128) and window (30 s) stand for paddle sending. Finding-1 bounds only the proposed gap value.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen blobs | Yes | `git rev-parse 82cf086:<path>` equals every `product_files` blob; HEAD equals them too |
| R2 | Checker runs by one command with the stated result | Yes | `git archive 82cf086` exported to the scratchpad; `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py`: 348 PASS, "0 failed assertion(s)", exit 0, 29.9 s |
| R3 | validate_docs on JSON under a schema | N/A | The results file has no schema |
| R4 | Author return states question, assumptions, inputs, results, limitations, values, tools | Yes | Note sections 1, 2, 4, 6, 8, 10, 11; author summary in the reviewer brief |
| R5 | No TBD; TBRs named | Yes | No "TBD" string in the note; every TBR named by id with its `tbr.plan` (section 1 table) |
| R6 | Every cited render exists beside its source | Yes | The three PNGs are in `docs/design/analysis/keyer-host-study/` |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Section 1 names REQ-SYS-052, 053, 054, 131, 184, 188, 189, REQ-SW-KEYER-022, 026, 036, HZ-004 K1, K3, K4, K7, K9, K13, HZ-005 K9, NGO-021, MOE-012. All exist, and the `tbr.plan` texts quoted in section 1 match the files at `f128235e` and `f9141160` |
| CK-ANA-A2 | Yes | Design data are named by blob: requirements `f128235e`, `f9141160`; hazards `81cacde4`; ConOps `6c3fbb2b`; expectations `52b6cf5e`; research `53345cb1`, `11c497ba`, `74e5363f`; ICD-CTL-KEY `5e9f1888`. Each equals HEAD. No AT RISK dependency (CR-003 and CR-006 do not touch keying) |
| CK-ANA-A3 | Yes | Input table I-1 to I-14 sources each value. I-12 (character set) and I-13 (flash times) are labelled as the author's transcription and as assumption A-7 |
| CK-ANA-A4 | Yes | Checked every input that sets a result. I-1 dit 1200/WPM ms, PARIS 50 dits (re-computed 12.0 s at 5 WPM). I-2 F7 rules against research lines 126 to 157. I-5 debounce 2/5 samples against F6 D1 to D5 (research lines 118 to 122). I-8 7.5 s and I-9 150 s against REQ-SYS-055 and REQ-SYS-180. I-10 60 s against the REQ-SYS-188 rationale. I-12 Morse codes: all 49 codes in `keyer_model.py` lines 32 to 46 checked by the reviewer against the ITU-R M.1677-1 table as commonly published, and all are correct. I-11 F19 circuit reading as stated in section 6.7. No disagreement |
| CK-ANA-A5 | No | Assumptions A-1 to A-9 are stated with direction and invalidation, but two gaps remain. The key-mode scope of the watchdog and the Bug-mode spacing are unstated (finding-1), and the longest manual closure is not a numbered assumption (finding-3) |
| CK-ANA-A6 | Yes | No requirement, hazard or interface file is edited (commit `82cf086` adds only the 19 WP-PDR-33 product files; `git show --stat 82cf086`). Consequences go out as requests R-1 to R-7 to named WPs, and as the PCR-8 and PCR-9 triggers of plan section 6.2 |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | Yes | Section 3 states the model structure, the ms sampling and us element time base, the tie rule, the operator model for squeezes (A-1, conservative) and the corpus basis. Ultimatic semantics are stated from the REQ-SYS-184 rationale |
| CK-ANA-B2 | N/A | No vendor or third-party model |
| CK-ANA-B3 | No | 24 of 24 golden vectors (F6 D1 to D5; F7) reproduced, re-run by the reviewer. The 240 analytic-versus-simulated window checks all agree within 1 ms. Three whole-character checks. The coverage statement for the F7 B variants overstates what the model runs (finding-4, Minor; the reviewer's own run of the missing B variants passes) |
| CK-ANA-B4 | Yes | Numerical settings: 1 ms sampling and exact us element boundaries (section 3.1). The squeeze search spans +/-12 ms around each analytic boundary. The windows agree within the 1 ms sampling step at every speed searched |
| CK-ANA-B5 | Yes | Reviewer hand calculations. Period in Iambic A: element sum 12 dits plus 6 one-dit spaces = 18 dits, 4.32 s at 5 WPM. Semicolon in Iambic B, S = 0.5: start of element 6 at 16 dits plus 0.5 x 1 = 16.5 dits. Figure 1 in Ultimatic: 1 + 1 + 4 x (3 + 1) = 18 dits. Proposed-limit margin at 12 WPM: 2000 - (18 x 100 x 1.005 + 3) = 188 ms. At 5 WPM: 4800 - (4320 x 1.005 + 3) = 455 ms. 16-dit branch crossover: 16 dits = 2 s at 9.6 WPM; 18 dits = 2 s at 10.8 WPM. Current gap thresholds: 3 dits < 500 ms above 7.2 WPM; 7 dits < 500 ms above 16.8 WPM. Figure 0 at 5 WPM = 19 dits = 4.56 s. Watchdog: 0.400 + 0.006 + 0.001 = 0.407 s; 1.0/0.407 = 2.46. All agree with the note |
| CK-ANA-B6 | Yes | Section 5.2 lists sampling, element tolerance, semantics, operator spacing and flash timing with their effects. The checker carries +0.5 percent and the 3 ms debounce offset into every squeeze margin |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | Python 3.13.5 and matplotlib 3.11.2 equal `tools/toolchain.lock.md` lines 37 and 197 and the reviewer's `import` check |
| CK-ANA-C2 | Yes | No TV record covers the model; TV-001 is accredited for schema validation only. Section 10 marks every result developer evidence (05 section 9.1). The values do not close a requirement and do not go to the owner until a TV record covers the model or the owner rules on developer evidence. This record flags that condition for the lead SE (cross item X-1) |
| CK-ANA-C3 | Yes | One headless command (header row "Reproduce") |
| CK-ANA-C4 | Yes | Reviewer re-run on an export of `82cf086`: exit 0, 348 PASS. The regenerated `keyer-host-study-results.json` and all three PNGs are byte-identical to the frozen blobs (`cmp`) |
| CK-ANA-C5 | N/A | No TV record, so no stated limitation to respect |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | Every quantity is in ms, s, dits or WPM, and conversions use 1200/WPM ms. No unit error found |
| CK-ANA-D2 | Yes | Numbers in sections 5 to 8 were compared with the results file: worst squeeze by mode, trip speeds per option, `squeeze_proposed_min_margin_ms` 188.0, fault stop 4.8/2.4/2.0 s, the no-gap table, max count 55 (current) and 8 (proposed), max span 4.56 s, interlock arm times, and watchdog ratio 2.457. The hazard-analysis figures 20.5 s and 6.1 s are explained (the end of the 128th element against 128 periods) |
| CK-ANA-D3 | Yes | Squeeze results carry +0.5 percent and +3 ms toward the limit. The 188 ms margin is not rounded up |
| CK-ANA-D4 | Yes | Checker lines 32 to 47 hold each acceptance constant with its requirement id in a comment. Comparisons are "more than" for REQ-SYS-184 (`seen > limit`, the requirement's "more than 2 s") and "at least" for the gap (section 3.4) |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Each value is quoted from the requirement text with its id (section 1 table; checker constants) |
| CK-ANA-E2 | Yes | Margins are limit minus result, positive. No TPM applies (section 8, last line) |
| CK-ANA-E3 | Yes | Each margin exceeds the stated uncertainty, which is already included in the squeeze margins. Where the baselined values fail (2 s, the 16-dit branch, the current gap rule), the note reports the failure and triggers the CR branch; it does not report a pass |
| CK-ANA-E4 | Yes | `check()` records each failure and `main` returns 1 on any. 348 assertions cover every section 6 value |
| CK-ANA-E5 | Yes | Section 8 gives id, value, supporting section, `tbr.plan` branch and margin for all 10 values. It marks both "else a CR" branches triggered (PCR-8 with 20 dits in place of 16; PCR-9 REQ-SYS-054 gap). No requirement file is edited. TBR finding 7: section 1 reads the baselined gap as the minimum of 7 dits and 500 ms, the reading of SRR `requirements-sys.md` finding-28 and CR-008. The proposed single gap removes the ambiguity. Checked, no residue. The proposed gap value is not accepted until finding-1 is fixed |
| CK-ANA-E6 | N/A | No TPM value proposed |
| CK-ANA-E7 | Yes | Section 10: REQ-SYS-052 to 054, 131, 184, 188 and 189 are Test-method requirements, and this analysis is supporting evidence only. REQ-SW-KEYER-022, 026 and 036 close by HostUnit on the `cwht-core` keyer (WP-PDR-41), not by this model |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Per-case table below: every case is covered except the key types of REQ-SYS-054 (finding-1) and the release sub-cases (finding-2) |
| CK-ANA-F2 | Yes | Fault streams of HZ-004 rows 4 to 8 and 10 (held dit, held dah, alternating, gap every 25 s, continuous) and the headphone or shorted-TRS squeeze (row 5) are bounded in sections 6.1 and 6.2. Row 7 (PARIS) and row 8 (pin map) are routed to K13 and K12 |
| CK-ANA-F3 | Yes | Worst combinations are stated: slowest speed with the longest alternating run per mode; highest switchpoint for Iambic B; the latest correct release; debounce and timing offsets added together |
| CK-ANA-F4 | Yes, except finding-3 | The only margin within twice its uncertainty is the 0.56 s manual-timeout floor margin, which has no sensitivity statement (finding-3). The 188 ms squeeze margin exceeds its 24 ms total offset by a factor of 7 |

### Per-case results

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Inputs closed at boot, reset or mode change, released at 1000 ms, clean | REQ-SYS-052, REQ-SW-KEYER-022: 500 ms / 500 samples | arms at 1499 ms | not applicable | 1 ms sampling | re-run: same | none |
| C-2 | Release with 6.2 ms and 10 ms chatter; make bounce (F6 D2) | same | arms 500 samples after the last closed sample (1506, 1509, 1499 ms) | 50 x the longest bounce | 1 ms | re-run: same | none |
| C-3 | Intermittent short open 499 ms | same | never arms | not applicable | 1 ms | re-run: same | none |
| C-4 | Closure durations 0 to 2 s | same | arm time equals last closed sample plus 500 for any closure, by construction of `interlock_arm_time` | not applicable | 1 ms | hand check of the counter logic | none |
| C-5 | Mono plug, paddle mode; Straight-on-tip | REQ-SYS-052 | never arms; arms at 499 ms | not applicable | 1 ms | re-run: same | none |
| C-6 | Straight tip, ring, both; Bug dah; held 4.9, 5.0, 5.1, 60 s | REQ-SYS-053, REQ-SW-KEYER-026: 5 s | 4.9 s follows the contact; 5.0 s and longer end at 5.0 s after the confirmed make | +3.56 s over the longest legitimate closure | assumption of finding-3 | hand check | finding-3 |
| C-7 | Range 2 to 6 s against the 7.5 s cutoff floor | REQ-SYS-053 `tbr.plan`; REQ-SYS-055 | 6 s ceiling | +1.5 s | none | hand check | none |
| C-8 | Held dit lever to the 128th element at 5, 25, 50 WPM | REQ-SYS-054: 128 or 30 s | 5 WPM 30.0 s (window); 25 WPM 12.24 s; 50 WPM 6.12 s (count) | not applicable | none | re-run: same | none |
| C-9 | Held dah lever at 5, 25, 50 WPM | REQ-SYS-054 | 30.0 s; 24.53 s; 12.26 s | not applicable | none | re-run: same | none |
| C-10 | Alternating stream, no qualifying gap | REQ-SYS-054: 30 s | 30.0 s at every speed, both rules | not applicable | none | re-run: same | none |
| C-11 | Qualifying gap every 25 s (7.5 dits; 2.5 dits for the proposed rule) | REQ-SYS-054 | keeps keying, both rules | +5 s | none | re-run: same | none |
| C-12 | Release of one lever, then of both | REQ-SYS-054 verification note | no row | not stated | not applicable | not re-checked (no model) | finding-2 |
| C-13 | Correct paddle sending, QSO and stress corpus, 5 profiles, 5 to 50 WPM | REQ-SYS-054 `tbr.plan` | current rule trips (section 6.2 table); proposed: never, longest span 4.56 s, count 8 | +25.4 s | operator spacing A-6 | re-run; figure 0 at 5 WPM hand-checked | none |
| C-14 | Correct Bug-mode sending (manual dahs and spacing) | REQ-SYS-054 `tbr.plan`; WP-PDR-33 output "Bug dahs" | not analysed | not stated | not stated | not re-checked (no Bug corpus) | finding-1 |
| C-15 | Straight-mode sending, if K4 (ii) runs in Straight | REQ-SYS-054; HZ-004 K4 | mode scope not stated | not stated | not stated | reviewer run: trips at 30.24 s, keyer 5 WPM, hand 20 WPM | finding-1 |
| C-16 | Both contacts closed 1.9, 2.1, 60 s at 5, 25, 50 WPM, A, B, Ultimatic | REQ-SYS-184 | 1.9 s trips neither; 2.1 s trips proposed at 25 and 50 WPM only; 60 s trips all | not applicable | 3 ms | re-run: same | none |
| C-17 | Squeezed C, K, Q at 5 WPM, A, B (S = 0.5), Ultimatic | REQ-SYS-184 | trip 2 s (C in A and B; K, Q in A); never the proposed limit | at least +8 dits | +0.5 percent, 3 ms | hand check C in A = 12 dits | none |
| C-18 | Every character of I-12, every mode and switchpoint 0, 0.5, 0.9, 5 to 50 WPM | REQ-SYS-184 proposed limit | never tripped | +188 ms minimum (12 WPM); +455 ms at 5 WPM | included | hand check | none |
| C-19 | Baselined 2 s and the 16-dit branch against correct sending | REQ-SYS-184 `tbr.plan` | 2 s trips 5 to 10 WPM; 16 dits trips 5 to 10 WPM (A, S = 0.9, U) | negative (fails) | included | hand check crossovers 9.6 and 10.8 WPM | none |
| C-20 | Contacts open after the squeeze stop | REQ-SYS-184 verification note | no row | not stated | not applicable | not re-checked | finding-2 |
| C-21 | Headphones or shorted TRS after boot | REQ-SYS-184; HZ-004 row 5 | stops at 4.80 s (5 WPM), 2.40 s (10 WPM), 2.00 s (12 WPM and above) | +25.2 s to the window at 5 WPM | none | hand check | none |
| C-22 | Hang in receive and while keyed | REQ-SYS-131: 2 s | Self-test by 1.1 s | +0.9 s | A-7, A-8 | hand check | none |
| C-23 | Each keying sub-mode left running | REQ-SYS-188: 120 s | ends at 120 s; covers 2 x 60 s; ends 30 s before the 150 s floor | +30 s | none | hand check | none |
| C-24 | Full-scale tone left running | REQ-SYS-189: 60 s | ends at 60 s; 2 x the 30 s reading (A-9) | 2 x | A-9 | hand check | none |
| C-25 | No plug with tip, ring, both closed; plug present | REQ-SW-KEYER-036 | tip withheld; ring short reads "plug present" (coverage limit, routed as R-4) | not applicable | F19 Medium | truth table re-derived by hand from I-11 | none |

## G6. Timing

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G6-1 | Yes | Time base: 1 kHz sampling, TIMER0 1 us (F8), and the +/-0.5 percent element tolerance of REQ-SW-KEYER-013. A crystal error of about 50 ppm is four orders of magnitude below the smallest margin (188 ms of 2 s) and is dominated by I-6 |
| CK-ANA-G6-2 | Yes | The squeeze and gap monitors act on debounced states and TX_KEY. The worst path adds the debounce offset. The watchdog path takes the longest interval without a feed (flash sector update with interrupts masked, section 6.5) |
| CK-ANA-G6-3 | Yes | No duration comes from Emulation. The model is a host timing model of platform-independent logic |
| CK-ANA-G6-4 | Yes | Sections 6.1 and 6.2 compare each stop time with the next control (the 30 s window, the 7.5 s cutoff floor, the 150 s backstop) and name HZ-004 K4, K12, K13 |

## G7. Worst-case

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme-value method: latest correct release, slowest speed, extreme switchpoint, all offsets added (section 3.3, checker section 4) |
| CK-ANA-G7-2 | N/A | No component tolerance, temperature coefficient or ageing enters these firmware timing values beyond the element tolerance I-6 |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes | HZ-004 and HZ-005 controls are named. R-4 and R-5 go to WP-PDR-16 (the hazards.json writer, plan section 5.3), not edited here |
| CK-ANA-H2 | Yes | The note raises no new risk. Using developer evidence for safety values is a process condition, carried as cross item X-1 |
| CK-ANA-H3 | Yes | Section 12, revision 1 for the F0 freeze |

## I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | All three renders opened with the Read tool (renders_inspected 3), and each regenerates byte-identically |
| CK-ANA-I2 | Yes | `keyer-squeeze-vs-speed.png`: axes "Keyer speed (WPM)" and "Both paddle contacts closed (s)"; limits labelled with REQ-SYS-184; legend; curves meet the 2 s line near 10 to 11 WPM as the table says. `keyer-nogap-vs-speed.png`: axes with units; 30 s window labelled REQ-SYS-054; the current nominal curve peaks near 32.6 s at 8 WPM as section 6.2 states; the proposed curves stay under 5 s. `keyer-squeeze-timeline.png`: the period with six elements, contacts released at 4.32 s, 2 s, 16-dit and 20-dit markers labelled |

## J. Software assurance items (evidence for the assurance pair)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-J1 | No accredited tool | The model is not validated and accredited (CK-ANA-C2). SWEHB `swe-070` section 7.1 task 1 is therefore not met for credit, and the note says so. The assurance reviewer confirms whether developer evidence may support the owner ruling |
| CK-ANA-J2 | Yes, subject to finding-1 | The values agree with HZ-004 K1, K3, K4, K7 and K13 and with the 07 section 14.2 SW-KEYER row item (g) stuck-input checks, and each stop time precedes the next control. The proposed gap value is conditional on finding-1 |
| CK-ANA-J3 | For the assurance pair | `assurance_tasks_applied` is left empty for the assurance reviewer (paired record) |

## Items N/A

CK-ANA-B2, C5, E6, G7-2; sections G1 to G5 (analysis_kind is timing and worst-case).

## Cross items for the lead SE (not findings on the note)

- X-1. Rule C10 and CK-ANA-C2. The values rest on a model with no TV record. The note's own condition holds that they go to the owner only once a TV record covers `keyer_model.py`, or the owner rules on developer evidence. The author's return proposes that owner action. It is not yet in plan section 6.1.
- X-2. SA pair. The record is held until `analysis-keyer-host-study-software-assurance.md` returns (PDR work plan WP-PDR-33 "SA for the keyer safety values").
- X-3. The PCR-8 row of plan section 6.2 names "16 dits"; the note proposes 20. The CR text and the register row follow the ruled value.

## Commands

- `git rev-parse 82cf086:<path>` and `HEAD:<path>` for each product file: all equal.
- `git archive 82cf086 | tar -x` into the scratchpad, then `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py`: exit 0, 348 PASS, 0 failed. `cmp` of the regenerated results and PNGs: identical.
- Reviewer scripts against the frozen `keyer_model.py`: B variants of V2 to V5, V11 and V12 at S = 0 and 0.5 (12 of 12 match); `analytic_window_dits` hand-check cases; the Straight-scope counter-example of finding-1.
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`: run on the record before its commit.

## Measurements (SWE-089)

Items checked 46 (R1 to R6, A1 to A6, B1 to B6, C1 to C5, D1 to D4, E1 to E7, F1 to F4, G6-1 to G6-4, G7-1, G7-2, H1 to H3, I1, I2, J1 to J3); items answered No 3 (CK-ANA-A5, B3, F1); findings 1 Major, 3 Minor; fixed 0; deferred 0; iteration 1; effort 48 turns, about 75 minutes; renders inspected 3; per-case rows 25; inputs checked 14.

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, HEAD `1bde213`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix only. Findings 2 to 4 (Minor) were not touched by the author (note header "Status") and are not re-reviewed. Product: the 8 blobs of front matter `product_files`, committed as `8c12b5a` (WP-PDR-33 revision 2). Each one equals `git rev-parse 8c12b5a:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `1bde213` (script, 8 of 8). `git log 8c12b5a..HEAD` shows no later change to any product file. All blobs are on main, so the lead SE convention for branch-only blobs concerns only the checklist template: `docs/templates/peer-review-checklist-analysis.md` revision A, still blob `0386cc6e` on `cr/CR-012-pdr-checklist-templates` at `7784672` (`git merge-base --is-ancestor` with main: false). The same template as iteration 1 is applied. Revision 2 also answers INSP-075 findings 1 and 2 (the paired SA record). Those fixes are verified by the INSP-075 iteration 2 delta, a separate invocation. This record checks them only where they change the finding-1 result (the revision 2 gap rule replaced the revision 1 rule that finding-1 bounded).

**Independence (rule C4).** This invocation authored no part of WP-PDR-33, no part of revision 2, and no part of INSP-075. It did not edit any product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: the WP-PDR-33 records and findings; the frequency reference calibration trim (for INSP-072). `grep` then only pinned lines of known paths (the plan, 08, the note, the checker, the ConOps). No rustos file was read.

**Reproduction.** `git archive 8c12b5a` of `docs/design/analysis`, `docs/reviews/PDR/figures` and the input folders, into the scratchpad. Then `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py`: 555 PASS, "0 failed assertion(s)", exit 0, 39.4 s. `cmp` of the regenerated `keyer-host-study-results.json` and the four PNGs with the frozen blobs: identical.

### Verification of finding-1, case by case (rule C7)

The cases are the elements of the finding-1 expected fix, and the defects it names.

| # | Case | Check | Result |
|---|---|---|---|
| 1 | State the key modes in which REQ-SYS-054 (i) and (ii) run | Note section 3.5 table: every key mode (Straight, Straight-on-tip, Iambic A, Iambic B, Ultimatic, Bug) on the TX_KEY read-back. This matches HZ-004 K4 "whatever the element pattern" (`hazards.json` blob `81cacde4`). Section 9 first bullet carries "items (i) and (ii) run in every key mode" into the CR | Yes |
| 2 | State the dit length each monitor uses | Section 3.5: none for REQ-SYS-054 (the reference interval is measured on TX_KEY); the configuration-guarded selected speed for REQ-SYS-184, which runs in Iambic A, Iambic B and Ultimatic only (its statement); none for REQ-SYS-053. In `keyer_model.py` `watchdog_relative` reads no speed argument, and the element type label is unused (`for s, e, _typ in stream`), so the monitor sees only TX_KEY edges | Yes |
| 3 | Add Bug-mode sending: manual dahs up to 6 dits, operator spacing referred to the Bug dit speed | Section 3.4 corpus B (`key_stream_bug`): automatic dits and dit-to-dit spaces, manual dahs of 3 or 6 Bug dits or drawn from 2.5 to 6, every other space in the operator unit k x Bug dit with k = 0.75, 1, 1.5, 2, four spacing profiles, +/-15 percent jitter on every manual length, 15 speeds, 2 seeds, both texts: 2880 streams. The builder code agrees with the section 3.4 text (reviewer read of lines 724 to 762). A-10 states the bounds with direction and invalidation | Yes |
| 4 | Straight sending, since K4 (ii) runs in Straight | Section 3.4 corpus S (`key_stream_hand`): five hand profiles with independent jitter, 15 speeds, 3 seeds, both texts: 450 streams, run with the keyer set to the hand speed and to 5 WPM for the current and revision 1 rules. A-11 states the bounds | Yes |
| 5 | Add the rows to the per-case table | Section 7 rows "Correct Bug sending (corpus B)", "Correct Straight sending (corpus S)" and "INSP-071 counter-example" | Yes |
| 6 | Show that the proposed rule trips none of it | `nogap_bug` rev2 `n_trips` 0 of 2880, `max_span_s` 9.908; `nogap_straight` rev2 0 trips in both keyer settings, `max_span_s` 6.837; corpus P rev2 0 trips, 4.56 s. The checker asserts each result. Reviewer checks: (a) an independent brute-force implementation of the section 6.2 definitions agrees with `watchdog_relative` on span, count, trip time and cause for 15 streams (corpora P, B, S and two fault streams at 5, 20, 50 WPM; 15 of 15); (b) corpus S with 10 more seeds (4 to 13) and the jitter widened to +/-25 percent: 2000 streams, 0 trips, longest span 10.22 s (H5, 5 WPM); (c) corpus B with 6 more seeds (3 to 8), dahs drawn from 2.5 to 6: 720 streams, 0 trips, longest span 12.52 s (k = 0.75, 2.5/5 profile, 5 WPM). The 9.91 s corpus maximum is seed-dependent, but every reviewer run keeps more than 17 s to the 30 s window | Yes |
| 7 | The reviewer counter-example (QSO text at 20 WPM, keyer at 5 WPM) | `nogap_insp071_counterexample`: current and revision 1 trip at 30.24 s (window), revision 2 does not trip. Reviewer run on the export, same result. A hand-jittered variant (H1, seed 1) trips the current and revision 1 rules at 30.27 s, and revision 2 not at all (longest span 1.21 s) | Yes |
| 8 | Withdraw or restrict the revision 1 gap value | Section 6.2 "Revision 1 proposal ... does not hold": it trips 228 of 450 Straight streams with the keyer at 5 WPM and 15 Bug streams (reviewer check of `nogap_bug.rev1.trips`, which lists 12 of the 15: all at k = 0.75 with the 2.5/5 profile, 5 to 7 WPM). Revision 1 is withdrawn; sections 8 and 9 carry only revision 2 | Yes |
| 9 | The changed REQ-SYS-054 rows of iteration 1 (C-8 to C-11) under revision 2 | `req_sys_054_cases_rev2` matches section 7: held dit 30.0 s (5 WPM, window), 12.24 s and 6.12 s (count); held dah 30.0, 24.53, 12.26 s; alternating 30.0 s, then 18.48 s and 9.24 s (period); the random-order stream with a 7.5-dit gap every 25 s keeps keying at 5, 25 and 50 WPM. The alternating stream with a gap every 25 s now stops at 25 and 50 WPM by the period count. The note states this as intended and moves the restated case into the CR (cross item X-5) | Yes |
| 10 | Whether the new rule creates a nuisance trip that iteration 1 did not have, on legitimate sending outside the corpus | Reviewer runs of same-character strings without word spaces: the count and the period count trip them (finding-5, Minor). No sending in corpora P, B or S is affected | See finding-5 |

**Result: finding-1 Verified.** The key-mode scope and the dit length of each monitor are stated. Bug and Straight sending are in the corpus and the per-case table. The proposed rule is now independent of the selected speed, and it trips none of the 3790 streams, the counter-example or the reviewer's 2720 extra streams. The assumption that carries the result is A-6 (letter spaces at least twice the shortest recent key-up interval), which is stated with its invalidation and replaced by a recorded sending if one is made (R-7).

### Re-checks outside the finding (no new finding)

- The fault-side table of section 6.2 (INSP-075 finding-1) was spot-checked against the independent implementation: alternating with 3-dit spaces at 50 WPM 15.384 s (period), "AAAA" at 5 WPM 123.12 s and at 50 WPM 12.312 s. Both implementations agree, and the values agree with the table. The coverage conclusion and its residual are for the INSP-075 delta.
- The squeeze-limit speed source (section 6.1; INSP-075 finding-2) does not change the REQ-SYS-184 correct-sending results of iteration 1 (C-16 to C-19), which the checker still asserts. `squeeze_speed_source` gives 2.00 to 4.80 s for every stored value, as stated.
- `keyer-squeeze-vs-speed.png` and `keyer-squeeze-timeline.png` are unchanged blobs.

### finding-5 (new, Minor)

<a id="finding-5"></a>**finding-5, Minor, Open.** See the findings table. Revision 2 counts equal elements across letter spaces and matches repeated character patterns. So a same-character run without a word space trips it once the run holds 128 elements, and the note's A-5 row says the opposite. Minor: the trip is on the nuisance side, the stated corpus does not reach it, and the owner can rule the limit. **Citation:** REQ-SYS-054 `tbr.plan` ("no legitimate sending at 5 to 50 WPM reaches them"); CK-ANA-A5 (assumption direction stated correctly).

### Visual closure (iteration 2)

All four plots were opened with the Read tool (renders_inspected 4). `keyer-nogap-vs-speed.png` (changed): axes with units, the 30 s window labelled REQ-SYS-054, the current-rule curves leave the plot above 12 and 14.4 WPM with an annotation that explains why, the revision 1 curve lies under the revision 2 curves as its legend says, and the revision 2 annotation gives 9.91 s over the three corpora. `keyer-nogap-fault-coverage.png` (new): two panels (15 and 50 WPM, fault after 15 s of correct sending), stop time against space length for the three rules, the 30 s window and the "30 s + 10 s reference aging" line labelled, not-stopped streams plotted at 62 s with a label. The values match the section 6.2 table (for example 50 WPM, alternating, 3-dit spaces, 15.4 s). The two unchanged plots were re-opened and show what iteration 1 recorded.

### Cross items (iteration 2, returned to Claude)

- X-4. The record `verdict` stays held for two reasons: the INSP-075 iteration 2 delta (a separate SA invocation) and the CR-012 merge of the template (lead SE convention of 2026-09-27).
- X-5. The REQ-SYS-054 CR (PCR-9) restates a verification-note case (an alternating stream with a gap every 25 s now stops by the period count at 25 and 50 WPM) and adds the section 6.2 residual. Its section 6 impact review (rule C6) should check TC-SYS-038 and the NGO-021 and MOE-012 mirrors against the revision 2 wording.
- X-6. Rule C10 and X-1 still hold: the values rest on developer evidence (no TV record for `keyer_model.py`).

### Completion criteria (SWE-088), iteration 2

Reviewer side met: no Major is open, readiness is met (R1 to R6 re-checked at `8c12b5a`: blobs frozen, one-command checker exit 0, no TBD, every render beside its source), and findings 2 to 5 are Minor liens due at the CDR readiness declaration (plan rule C1; PDR package section 15). `reviewer_verdict: APPROVED`. The record `verdict` is held at NEEDS CHANGES until INSP-075 is APPROVED (07 sections 2.1.1 and 10.2) and CR-012 merges.

```
ITERATION 2 (2026-09-27, HEAD 1bde213, product commit 8c12b5a): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held for the SA pair INSP-075 and the CR-012 merge)
FINDINGS:
- [Major] finding-1: Verified (key-mode scope stated; Bug corpus 2880 and Straight corpus 450 streams; revision 2 trips none of 3790 streams, the counter-example, or 2720 reviewer streams; independent implementation agrees 15 of 15).
- [Minor] finding-2, finding-3, finding-4: Open, not in the delta (liens).
- [Minor] finding-5 (new): revision 2 depends on A-5; same-character runs without a word space trip it (26 x 5, 33 x V at 20 WPM) (lien).
MEASUREMENTS: blobs equal HEAD 8/8; checker 555 PASS exit 0; outputs byte-identical 5/5; cases 10 (9 Yes, 1 to finding-5); renders inspected 4; major open=0; minor open=4; turns=36; minutes=55 (cumulative 84 and 130); iteration=2
```
