---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/08-agent-briefing.md section 3.2).
id: INSP-004
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/requirements-tx-and-sw-keyer.md
# product: the early L2 requirement set of SRR item H15, four files reviewed as one product.
# The two requirement files are the requirements product; the two test-case files are their
# Draft closing cases (02 section 4.1 step 7), judged here only as the V5 and CK-REQ-E6 evidence.
product: docs/requirements/tx/requirements.json
# product_commit: HEAD on which the files sit; all four files are untracked at review time, so
# product_files carries the git hash-object blob of each file as reviewed.
# re-issue 2026-09-26 (package item R8): product_commit is the last commit touching the four files, f2e02aa (INSP-026 finding-1)
product_commit: "f2e02aa"
# Iteration 1 blobs: tx req 10507f5d, sw-keyer req b8a301b8, tx tc 5bc1bd74, sw-keyer tc 19186fd3.
# Iteration 2 (2026-09-26) blobs: tx req c0aabfef, sw-keyer req 4a24fed5, tx tc 20e560c5, sw-keyer tc 3c5c5dc1
# (working tree, not in the object store). Iteration 3 (2026-09-26) reviewed the committed blobs
# below, git rev-parse HEAD:<path> at adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1 (files last changed in cb00792).
# Iteration 3 product_files named sw-keyer req db2de344c66ff7caa5e72f922f87686fd3a7ce71 and sw-keyer tc f730056914aedfa003757f94284a020e79c67795.
# Re-issue (2026-09-26, git rev-parse HEAD:<path> at 1af795c): the two TX blobs unchanged; the two SW-KEYER blobs are the f2e02aa fix of
# INSP-026 finding-1, delta-verified at the re-issue (section "Re-issue") and reviewed by INSP-026 iteration 2
product_files: ["docs/requirements/tx/requirements.json@ef206c83ce711d22d37513fa4c37e092abf0dcc2", "docs/requirements/sw/sw-keyer/requirements.json@4d22b399f1647743dd837e731d8c05fa6be7b7bb", "docs/test_cases/tx/test_cases.json@20e560c597bfb165fc3fc805960037f8c14ffeb2", "docs/test_cases/sw-keyer/test_cases.json@d3c0c236651bd41332bac345fd936e199734bfe3"]
product_size: 55 requirements (16 REQ-TX, 39 REQ-SW-KEYER; REQ-SW-KEYER-039 added at f2e02aa); 59 test cases (16 TC-TX, 43 TC-SW-KEYER) at the re-issue (iterations 2 and 3: 54 and 59; iteration 1: 49 and 56)
sprint: SRR-prep
author_agent: "author:requirements-l2 (requirements author, REQ-TX and REQ-SW-KEYER) and test-author:requirements-l2 (independent test author, TC-TX and TC-SW-KEYER)"
reviewer_agent: "reviewer:requirements-l2"
# criticality: SW-KEYER is safety-critical (07 section 14.1); the TX file carries HZ-008 controls
criticality: safety-critical
assurance_required: true
# Re-issue 2026-09-26: the paired software assurance record of the SW-KEYER pair is INSP-026
# (docs/reviews/SRR/checklists/requirements-sw-keyer-software-assurance.md, same SW-KEYER blobs 4d22b399 and d3c0c236,
# paired_record: INSP-004); 01 section 13 paired form (INSP-026 cross item X-1). This reviewer is not the assurance reviewer.
assurance_reviewer_agent: "reviewer:INSP-026 (software assurance function for the SW-KEYER pair; paired record INSP-026; file review by reviewer:requirements-l2)"
paired_record: INSP-026
iteration: 3
# re-issue: readiness R3 Yes on the author self-check filed at 1af795c (package item R7), so readiness_met is true
readiness_met: true
# reviewer_verdict: no open Major finding; APPROVED with liens (finding-17, 18, 20) under the convergence rule of 2026-09-26
reviewer_verdict: APPROVED
# assurance_verdict: equals the verdict of the paired record INSP-026 (01 section 13), APPROVED at its re-issue of 2026-09-26
assurance_verdict: APPROVED
# verdict: APPROVED (with liens finding-17, 18, 20) at the re-issue: reviewer APPROVED, assurance APPROVED, readiness met,
# no Major finding open (07 section 2.1.1; 07 section 10.2)
verdict: APPROVED
# re-issue: finding-20 (Minor) is new, raised from the author's exception E-1
findings_major: 4
findings_minor: 16
# re-issue: 17 Verified (finding-19 on the author self-check), 3 Minor liens (finding-17, 18, 20; fix before PDR) counted as deferred
findings_open: 0
findings_fixed: 0
findings_verified: 17
findings_deferred: 3
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no at iteration 1: R1, R3, CK-REQ-A3, A4, A7, A8, B3, B4, B5, C1, C2, C4, C5, C6, C7, D4, E1, E3, E5, F2
# items_no at iteration 2: R1, R3, CK-REQ-B5
# re-issue: R3 Yes; CK-REQ-A7 No on the liens finding-18 and finding-20
items_no: [CK-REQ-A7]
# effort: iteration 1 48 turns and 75 minutes; iteration 2 30 turns and 45 minutes; iteration 3 25 turns and 40 minutes;
# re-issue 15 turns and 30 minutes
effort_turns: 118
effort_minutes: 190
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-004: early L2 requirements REQ-TX and REQ-SW-KEYER with their Draft closing cases

**Verdict (re-issue of iteration 3, 2026-09-26, package item R8, blobs equal to HEAD `1af795c`): APPROVED with liens finding-17, finding-18 and finding-20.** Readiness R3 is now Yes: the author self-check filed at `1af795c` lists the brief's acceptance criteria and answers checklist sections A to G item by item; finding-19 is Verified. The pairing is met: the SW-KEYER software assurance record INSP-026 is re-issued APPROVED (with liens) on the same SW-KEYER blobs, so `paired_record: INSP-026` and `assurance_verdict: APPROVED` (01 section 13; 07 sections 2.1.1 and 10.2). The SW-KEYER files changed at `f2e02aa` (INSP-026 finding-1); the delta is verified in "Re-issue" and `product_files` names the HEAD blobs `4d22b399` and `d3c0c236`. The author's exception E-1 is raised as finding-20 (Minor, Lien: fix before PDR). No Major finding is open and no finding waits on an owner ruling.

**Product.** The early L2 set that closes SRR readiness item H15 (`docs/reviews/SRR/package.md` section 2; 01 section 4.3 row 25; SWE-050 row of 01 section 4.6; 02 sections 2.2 and 12; `docs/requirements/README.md`), reviewed as one product:

| File | Git blob (hash-object) | State |
|---|---|---|
| `docs/requirements/tx/requirements.json` | `10507f5df1fbbead1f5d1e98bc78445536fae4fd` | untracked on 28e49e6; 16 requirements, all Draft |
| `docs/requirements/sw/sw-keyer/requirements.json` | `b8a301b8d4160d64fbb48fdd81f8b19ca090e636` | untracked on 28e49e6; 33 requirements, all Draft |
| `docs/test_cases/tx/test_cases.json` | `5bc1bd74a2396f2889adbd9805d922484593dfa6` | untracked on 28e49e6; 16 cases, all Draft |
| `docs/test_cases/sw-keyer/test_cases.json` | `19186fd3cc663ff112d2f85e812dfc050624fcfd` | untracked on 28e49e6; 40 cases, all Draft |

**Checklist.** `docs/templates/peer-review-checklist-requirements.md` revision C, product-type row "Requirement files, any level": sections A to F, readiness R1 to R5, one per-requirement validation row per requirement (WR-01 to WR-14, V1 to V6) and the V2 block. Not applicable: G1 to G8 (the product is not a plan), B7 and R5 (not a CR). The two test-case files are judged here only as the closing-case evidence of V5 and CK-REQ-E6; their procedure-level review uses `docs/templates/peer-review-checklist-test.md` in a record of their own (open question 1 below).

**Method.** Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every grep of the repository and corpus (one listing of the known directory `docs/reviews/SRR/checklists/` was made before it, at the start of the review) (queries: SRR readiness H15; class 1 item (g) Analysis for Test; NanoVNA range; PA_EN and TX_KEY signal names); `grep -n` was used only afterwards to pin lines. Each regulatory citation was read in the verbatim corpus `docs/references/md/regulatory/` (eCFR issue 2026-09-23). Every numeric value was recomputed or checked against its cited source: the parent `REQ-SYS-*` entries, `docs/safety/hazards.json` (0.2.0-pha), `docs/safety/hazard-analysis.md` section 8, `docs/design/allocation.json`, `docs/plan/tpm.json`, the ICD stubs `docs/icd/ICD-TX-ANT.md` and `docs/icd/ICD-CTL-KEY.md`, `docs/conops/conops.md`, `docs/process/07-software-engineering-plan.md` sections 14.1, 14.2 and 16, and the research reports `docs/research/regulatory-corpus-and-operators.md` F7, F8 and `docs/research/keyer-verification-and-key-input-network.md` F6, F7, F8, F12, F14.

**Criteria this record judges.**

| Criterion | Result | Evidence |
|---|---|---|
| 01 section 4.3 row 25: `REQ-TX-*` tagged `regulatory` citing 47 CFR 97.305 and 97.307 from the published text | Met in form; one value defect | 97.305: REQ-TX-001 cites 97.305(a) and (c), checked against `47cfr-97.305.md` line 17 (CW on any authorized frequency) and line 58 (2 m row 144.1 to 148.0 MHz for MCW, phone, image, RTTY, data). 97.307: REQ-TX-003, 005, 006, 007, 008, 009, 010, 011, 012, 013 cite 97.307 (a), (b) or (e), checked against `47cfr-97.307.md` lines 17, 19 and 25; 25 uW, 40 dB and 53 dB at 5 W recomputed (10 log(5 W / 25 uW) = 53.0 dB; 1 uW is 14.0 dB below 25 uW). All 16 REQ-TX carry `regulatory`. REQ-TX-006 carries a sideband value that the project's own computation contradicts (finding-1) |
| SWE-050 (NPR 7150.2D 4.1.2, pinned `04-chapter4.md` line 13): software requirements captured; SW-KEYER at Draft with Draft closing cases | Met in form; content gaps | 33 REQ-SW-KEYER at Draft; every one has a Draft closing case of its own method and a closing type for module SW-KEYER (15 hazard-tracing requirements also have a Bench case under `T-SW-TARGET`, SWE-192 line 143 of `04-chapter4.md`); `tools/traceability.py --report-only` reports no violation for the module. SWE-134 provisions of 07 section 14.2 for SW-KEYER are incomplete (finding-2) |

## Record

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Disposition (iteration 2) | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-C1, CK-REQ-D4 (V3, V4) | REQ-TX-006 `description`, `rationale`; TC-TX-006 | The requirement asks for keying sidebands at least 60 dB below the carrier beyond 500 Hz with continuous 50 WPM dits at every envelope setting, and TC-TX-006 tests it at the 3, 5 and 8 ms settings. The project's own computation contradicts it: `docs/research/regulatory-corpus-and-operators.md` F7 gives, for continuous 50 WPM dits with the full Hann transition of the 3 ms 10-to-90 setting (tr = 5 ms), the -60 dB point at 614 Hz, and 735 Hz for tr = 3 ms; REQ-SYS-008 and REQ-TX-006's own rationale state the 614 Hz assumption. The 500 Hz figure of `keyer-verification-and-key-input-network.md` F12 is for a 30 WPM dit stream; the rationale moved it to 50 WPM without new evidence. F7 also measures against total mean power, while REQ-TX-006 measures against the carrier line, which for a 50 percent duty dit stream is about 3 dB lower, so the case is harder still. At the 3 ms setting, and at 2.7 ms (the REQ-TX-005 lower tolerance), the closing case would fail by construction. Fix: restate the offset and condition from F7 (for example -60 dBc beyond 750 Hz (TBR) at 50 WPM at every setting, or 500 Hz at 30 WPM per F12), keep the REQ-SYS-008 guard budget consistent, and align TC-TX-006 | Verified | Closed. REQ-TX-006 now reads 60 dB below total mean power beyond 750 Hz (TBR) with continuous 50 WPM dits; checked against `regulatory-corpus-and-operators.md` F7 table (continuous dits 50 WPM: 614 Hz at tr = 5 ms, the 3 ms 10-to-90 setting; 735 Hz at tr = 3 ms) and F12 (500 Hz is a 30 WPM figure). 750 Hz covers the 2.7 ms tolerance corner (tr about 4.6 ms, between the two rows). TC-TX-006 title, configuration, acceptance and the known-answer step (614 Hz within one 10 Hz cell) match. The REQ-SYS-008 guard gap (630 Hz at +/-370 Hz) is stated in the rationale and TBR plan and routed as a cross item | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-REQ-C4, CK-REQ-B5 (V3) | SW-KEYER file; REQ-SW-KEYER-020, 021, 022, 024, 025, 026, 030 | Safety provisions that 07 section 14.2 (SW-KEYER row, items a to l) and `hazards.json` assign to the keyer are not stated as requirements: (f) the dit and dah memories stored with their complements (REQ-SW-KEYER-030 covers only the key-down state); (g) stuck-input detection and jack-detect range checks (HZ-004 K9; 07 section 14.1 keyer row); HZ-004 K1 sidetone off and the check repeated every sample while the interlock holds (REQ-SW-KEYER-022 states only key-down idle; ConOps OPS-013 step 1 also says sidetone off); HZ-004 K3 the "KEY?" annunciation of a manual-closure timeout (REQ-SW-KEYER-023 reports only the KeyClosed interlock). 07 section 14.2 (d) requires a menu action plus a confirmation for Straight-on-tip after a mono plug, while REQ-SW-KEYER-025, HZ-004 K2 and ConOps OPS-013 require only the explicit menu action: the 07 row and the hazard control disagree (package item H14). Fix: add the missing REQ-SW-KEYER entries (or record for each the SW module that owns it), and reconcile item (d) with the 07 author and the hazard analyst | Verified | Closed. Item (f): REQ-SW-KEYER-034 (paddle memories with complements; 07 line 621 item f) closed by TC-SW-KEYER-041 and on-target TC-SW-KEYER-038. HZ-004 K1 sidetone: REQ-SW-KEYER-035 (ConOps Table 3.4-4 row 1 Sidetone Off, line 216; OPS-013 step 1, line 535) with TC-SW-KEYER-042 and TC-SW-KEYER-034. Item (g): REQ-SW-KEYER-036 (plug-presence range check; `ICD-CTL-KEY` lines 92 and 118, ring switch = plug detect) with TC-SW-KEYER-043 and TC-SW-KEYER-034; the other stuck-input checks are named in its rationale. HZ-004 K3: REQ-SW-KEYER-023 covers both KEY inhibit causes (rows 1 and 2, 'KEY?' line 217) and TC-SW-KEYER-023 has the timeout test. Item (d): the REQ-SW-KEYER-024 rationale records the 07 row (d) versus HZ-004 K2 difference; the keyer statement holds under either reading; reconciliation stays a cross item (07 author, hazard analyst; package H14) | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | WR-13, CK-REQ-C2 (V1, V3 d) | REQ-TX-003, 007, 008, 012, 014, 016; REQ-SW-KEYER-019, 020, 021, 022, 024, 026, 028 | Interface pairing of 02 section 3.5 is not met. `ICD-TX-ANT` is an external interface whose module side is TX, yet no REQ-TX is tagged `interface` with `ICD-TX-ANT` in `design_refs`; the ICD itself records it (`docs/icd/ICD-TX-ANT.md` line 51: "none cites this ICD yet") while its sections 3.2.4 and 3.2.7.1 tabulate the antenna-port values of the six REQ-TX listed. `ICD-CTL-KEY` line 51 and its section 3.2.5 security row name REQ-SW-KEYER-019 to 022, 024, 026 and 028 as the firmware rules applied at the boundary; 02 section 3.5 Owner row requires a third module with requirements against an interface to cite it in `design_refs`, and none of them does. WR-13 is Major per 02 section 4.2. Fix: tag the REQ-TX antenna-port requirements `interface` with `ICD-TX-ANT` (at least one per side as the Pairing row requires) and add `ICD-CTL-KEY` to the `design_refs` of the listed REQ-SW-KEYER entries | Verified | Closed. REQ-TX-003, 007, 008, 012, 014, 016 carry tag `interface` and `ICD-TX-ANT` in `design_refs`; REQ-SW-KEYER-019, 020, 021, 022, 024, 026, 028 (and 036, 038) carry `ICD-CTL-KEY` (read from the JSON). `ICD-TX-ANT` line 51 still says 'none cites this ICD yet': stale text in the ICD, cross item | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-REQ-B5 | every REQ-TX and REQ-SW-KEYER with `hazard_ids` (14 REQ-TX, 15 REQ-SW-KEYER); `docs/safety/hazards.json` | The requirements carry `hazard_ids`, but no control in `hazards.json` lists any REQ-TX or REQ-SW-KEYER in `control_req_ids`, so the hazard-level `requirement_ids` union (charter section 7) omits them: `tools/traceability.py --report-only` prints 40 `HAZARD_INVERSE` warnings for these ids. The software-requirements-to-hazards relation of NPR 7150.2D 3.12.1 (SWE-052, `03-chapter3.md` line 321) is one-directional for this product. The product side is correct; the fix is in `hazards.json` (cross item for the hazard analyst): add each id to the control it implements (for example REQ-TX-009 to REQ-TX-011 under HZ-008 K1, REQ-SW-KEYER-026 under HZ-004 K3, REQ-SW-KEYER-030 under HZ-004 K8) | Verified | Closed. `hazards.json` 0.4.0-pha lists the 40 original ids in `control_req_ids` (`hazard-analysis.md` section 9 item 1); `traceability.py --report-only` shows no `HAZARD_INVERSE` for any of them. The 4 warnings for the new REQ-SW-KEYER-034, 035, 036 are finding-16 | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-REQ-E1, CK-REQ-E3 (V3 g, V5) | REQ-TX-001 (Inspection), REQ-TX-005 and REQ-TX-006 (Analysis) | All three are `regulatory`; 02 section 4.4 makes a regulatory requirement Test on the Bench unless a class 1 trade study decided by Robin (06 section 14.1 item (g)) changes it. The rationales say "Proposed, owner decision pending at SRR under the class 1 trade", but no such trade study exists (`docs/decisions/trade-studies/` holds TS-001 and TS-002 only) and `docs/reviews/SRR/decisions-for-owner.md` lists no item (g) decision. REQ-TX-005 and REQ-TX-006 also carry HZ-008 and cite "Fault tolerance: 8.1 item 7", but the item 7 exception table of `hazard-analysis.md` lists only REQ-SYS-010 for HZ-008, so their Analysis closure is not a recorded exception (CK-REQ-E3). Fix: name the decision item and trade record for the method substitution (with the L1 parents REQ-SYS-001, 014, 015), and have the hazard analyst add the HZ-008 exception rows, or change the method once the tinySA TV record answers ACTION-9 | Verified | Closed. REQ-TX-001, 005, 006 rationales name SRR decision 30 (`decisions-for-owner.md` line 49: the item (g) trade for REQ-SYS-001, 014, 015, 177) and trade record TS-NNN. `hazard-analysis.md` 0.4.0-pha section 8.1 item 7 lists REQ-TX-005 and REQ-TX-006 (line 430, finding-3 of INSP-008) | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-REQ-B3, CK-REQ-A7 (WR-10, V5) | REQ-TX-013; TC-TX-013; REQ-SYS-182 | The frequency sample implements HZ-008 K7, which is REQ-SYS-182 (independent measurement within 10 kHz, `regulatory`, 97.307(b), allocated to TX in `allocation.json`), yet REQ-TX-013 is parented to REQ-SYS-154 and REQ-SYS-182 has no TX child. The rationale names a design solution (a fixed-ratio divided sample) without the `Constraint:` item of 02 section 4.3. TC-TX-013 passes on "agreement within 1 kHz" of the count, a criterion no requirement of the file states. Fix: parent the requirement to REQ-SYS-182 (naming REQ-SYS-154 in `Why:`), add the `Constraint:` item, and either state the sample accuracy in the requirement or move the 1 kHz agreement to the SW requirement that owns the count | Verified | Closed. REQ-TX-013 `parent_id` REQ-SYS-182 (child_ids of REQ-SYS-182 = [REQ-TX-013]; REQ-SYS-154 child_ids empty); `Why:` names REQ-SYS-154 and SRR decision 40 (`decisions-for-owner.md` line 64); the description states the 1 kHz (TBR) accuracy that TC-TX-013 checks; `Constraint:` item present in 02 section 4.3 order; TS-002 reference removed | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-REQ-B3, CK-REQ-B4 | SW-KEYER file; REQ-SYS-051, REQ-SYS-054; OPS-017 | `docs/design/allocation.json` lists SW-KEYER in `sw_modules` of REQ-SYS-051 (key inputs unchanged while transmitting with 1.5 m leads) and REQ-SYS-054 (128-element or 10 s paddle stop), but neither has a REQ-SW-KEYER child and the file does not say which module carries them (HZ-004 K4 places the no-gap watchdog in the safe-state manager, not the keyer). ConOps OPS-017 (RF pickup on key leads) exercises the keyer and no REQ-SW-KEYER cites it. Fix: add the children or correct the allocation, and cite OPS-017 where the debounce and sampling requirements serve it | Verified | Closed. REQ-SW-KEYER-019 rationale states that REQ-SYS-051 is held by the CTL input network (HZ-010 K2, K4) and REQ-SYS-054 by the safe-state manager watchdog (HZ-004 K4); OPS-017 cited in REQ-SW-KEYER-019, 020, 021, 038. `docs/design/allocation.json` still lists SW-KEYER for both: cross item | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-REQ-C4 (V3 a) | REQ-SW-KEYER-020, REQ-SW-KEYER-021 | Two consecutive 1 ms samples reading closed show between 1 and 2 ms of contact, not the "2 ms (TBR) of continuous contact" of the parent REQ-SYS-048; five open samples show 4 to 5 ms against the 5 ms of REQ-SYS-162. The rationales do not state the equivalence. `hazards.json` HZ-004 K9 and HZ-010 K3, and research F6 and F14, make each count configurable 1 to 20 ms; the requirements fix the counts and say nothing of configurability, while the rationale's 25 percent of a 50 WPM dit (6 ms) cap contradicts a 20 ms setting. Fix: state the sample-count to duration convention once (and the parent's wording, cross to the L1 author), and record the decision on configurability in the requirement or in HZ-004 K9 | Verified | Closed. REQ-SW-KEYER-020 and 021 state the sample-count convention (N samples accept every contact of N ms or more, reject every one shorter than N-1 ms; checked: an interval of length L holds at least floor(L) and at most ceil(L) samples) and record the proposed fixed-count decision with its reason. The HZ-004 K9 1 to 20 ms range is a cross item for the hazard analyst | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | CK-REQ-C6, CK-REQ-C7 | REQ-SW-KEYER-009, 015, 024, 032; TC-SW-KEYER-009, 015, 032, 040 | The cases assert behavior no requirement states: TC-SW-KEYER-009 and 015 reject out-of-range settings with the previous value kept, TC-SW-KEYER-032 rejects hang settings outside 3 to 30 dits, and TC-SW-KEYER-040 requires that no key-line stimulus changes speed, switchpoint, hang or the Straight-input setting. REQ-SW-KEYER-009 and 015 only say "accept"; REQ-SW-KEYER-032 names no acceptance or rejection; REQ-SW-KEYER-024 covers the key-input mode only, while 07 section 16 (CS-30) and the `ICD-CTL-KEY` section 3.2.5 security row require that no key-line pattern changes any configuration. Fix: add the rejection response for out-of-range setting commands (undesired event, CK-REQ-C6) and one requirement that the key inputs change no setting (CK-REQ-C7) | Verified | Closed. REQ-SW-KEYER-037 (reject out-of-range speed, switchpoint, hang; keep previous value; parent REQ-SYS-041, whose child_ids list it) and REQ-SW-KEYER-038 (key inputs change no setting; self-derived from ADR-009) added; TC-SW-KEYER-009, 015, 032 cite 037 and TC-SW-KEYER-040 cites 038 | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | V5 | REQ-SW-KEYER-022; TC-SW-KEYER-022 | "until each input the mode uses reads open for 500 ms" does not say whether the 500 ms runs on raw samples or from the debounced opening; the test author had to widen the acceptance to 490 and 510 ms because the requirement "does not fix" the reference points (TC-SW-KEYER-022 acceptance criteria). Fix: state the reference (for example 500 consecutive 1 ms samples reading open) so the case can hold the value within one sample | Verified | Closed. REQ-SW-KEYER-022 reads '500 consecutive samples (TBR)', the rationale says a closed sample restarts the count; TC-SW-KEYER-022 steps and acceptance use 499 against 500 samples on the raw 1 ms samples | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | WR-14, CK-REQ-A8, CK-REQ-C5, CK-REQ-F2 | REQ-SW-KEYER-023 | "KeyClosed interlock state" appears in no other product; ConOps Table 3.4-4 row 1 names this condition the KEY inhibit ("Inhibit (KEY)", message "KEY CLOSED: check plug"), and it is not a state of the architecture list of CK-REQ-C5. Fix: use the ConOps term (or define the keyer state in the glossary and ConOps in one change) | Verified | Closed. No 'KeyClosed' in any of the four files (count 0); REQ-SW-KEYER-023 and TC-SW-KEYER-023, 034 use 'KEY inhibit' (ConOps Table 3.4-4 rows 1 and 2, lines 216 to 217) | Pending | |
| <a id="finding-12"></a>finding-12 | reviewer | Minor | CK-REQ-E5 (V5) | REQ-TX-011; TC-TX-011 | Closing needs NanoVNA S21 from 560 MHz to 1.5 GHz with an isolation floor at or below -50 dB (10 dB below the -40 dB limit). The owner's NanoVNA model and its usable range and dynamic range above 900 MHz are recorded nowhere (04 section 6.1 and `tools/toolchain.lock.md` name only "NanoVNA"), so it is not shown that the case can pass on the owner's instrument. The floor check keeps the case from a false pass, but a Blocked result is likely. Fix: record the model and its verified range in the NanoVNA TV record, or name the 04 section 6.2 alternative (for example the tinySA Ultra with the tracking source) for the span above the NanoVNA's range | Verified | Closed. TC-TX-011 takes the NanoVNA model, verified upper frequency and dynamic range from its TV record, routes any span beyond it to a borrowed VNA under 04 section 6.3, and its acceptance requires every point measured on a covered instrument; REQ-TX-011 verification_note matches. Recording the owner's model in the TV record is a cross item | Pending | |
| <a id="finding-13"></a>finding-13 | reviewer | Minor | V5 (closing-case evidence) | TC-TX-007, TC-TX-012 acceptance criteria | The limit is written "at most -16.0 dBm (25 uW)"; -16.0 dBm is 25.1 uW and 25 uW is -16.02 dBm, so the stated dBm limit is 0.02 dB looser than 47 CFR 97.307(e) (`47cfr-97.307.md` line 25). The added instrument uncertainty makes the practical effect negligible, but a regulatory limit is quoted exactly. Fix: write -16.02 dBm or state the limit in uW (also in 04 section 6.1 and ADR-021, cross) | Verified | Closed. Every limit in TC-TX-007 and TC-TX-012 reads -16.02 dBm (25 uW), matching 47 CFR 97.307(e) (corpus: `47cfr-97.307.md` line 25); no '-16.0 dBm' remains. 04 section 6.1 and ADR-021 stay a cross item | Pending | |
| <a id="finding-14"></a>finding-14 | reviewer | Minor | WR-10, CK-REQ-A7 | REQ-TX-009, 010, 011, 013; REQ-SW-KEYER-030 | 02 section 4.3 fixes the order Why, Assumes, Ops, Depends on, Fault tolerance, Constraint, KDR, TBR. REQ-TX-009 to 011 and REQ-SW-KEYER-030 put `Constraint:` before `Ops:` and `Fault tolerance:`; REQ-TX-013 names a design solution without a `Constraint:` item (see finding-6). Fix: reorder the items | Verified | Closed. Scripted order check of every rationale against Why, Assumes, Ops, Depends on, Fault tolerance, Constraint, KDR, TBR: no violation in the 54 requirements; REQ-TX-013 has its `Constraint:` item | Pending | |
| <a id="finding-15"></a>finding-15 | reviewer | Major | WR-04, CK-REQ-A3, CK-REQ-A4 (V1, V5) | REQ-SW-KEYER-014 | The load condition "while the display and encoders run continuously" has no number: neither the display refresh rate nor the encoder step rate is bounded, and "continuously" is an adverb standing in for them (CK-REQ-A4). TC-SW-KEYER-014 supplies the missing values itself ("the display refreshes at its maximum rate", a fixture turning both encoders at an unstated rate). WR-04 is Major per 02 section 4.2. Fix: state the load, for example "with the display refreshing at its maximum rate and each encoder stepping at 50 steps/s (TBR)" | Verified | Closed. REQ-SW-KEYER-014 states 50 display frames/s and 50 detents/s per encoder (TBR, tbr object, close_by PDR); sources checked: UI-DSP-01 full-frame update <= 20 ms (`display-and-ui-parts.md` line 155) and 24 detents (ADR-006 line 28; 2 rev/s = 48 detents/s). TC-SW-KEYER-014 configuration uses 50 detents/s and its acceptance requires at least 50 full-frame transfers/s and 50 +/-2 detents/s per loaded capture; the test author's open question is gone | Pending | |
| <a id="finding-16"></a>finding-16 | reviewer (iteration 2, new) | Minor | CK-REQ-B5 | REQ-SW-KEYER-034, 035, 036; `docs/safety/hazards.json` | The three hazard-tracing requirements added for finding-2 carry `hazard_ids` (HZ-004; 036 also HZ-010), but no control in `hazards.json` lists them: `tools/traceability.py --report-only` (2026-09-26) prints 4 `HAZARD_INVERSE` warnings (034/HZ-004, 035/HZ-004, 036/HZ-004, 036/HZ-010), which 04 section 7.3 rule 6 counts against gate readiness. The product side is correct; the fix is in `hazards.json` (cross item for the hazard analyst: REQ-SW-KEYER-034 under HZ-004 K8, 035 under HZ-004 K1, 036 under HZ-004 K9 and HZ-010) | Verified (iteration 3) | Open (cross item; the author has no write access to `hazards.json`). Iteration 3: Closed, see the Iteration 3 section | Pending | |
| <a id="finding-17"></a>finding-17 | reviewer (iteration 2, new; present at iteration 1 and missed) | Minor | V5 | REQ-SW-KEYER-016, 017, 026; TC-SW-KEYER-016, 017, 026 | Same class as finding-10: the requirement leaves a reference point open, and the test author recorded it inside the case. TC-SW-KEYER-016 setup: REQ-SW-KEYER-016 "does not say which speed the space after an element in progress uses; open question of the test author". TC-SW-KEYER-017: the 2 ms latency is not bounded "for a bounced closure ... as written; open question of the test author". TC-SW-KEYER-026: the +/-1 ms window exists "because the requirement does not fix which sample starts the count". Fix: state in each requirement the reference (the speed that governs the trailing space; the sample from which latency counts for a bounced closure, for example the sample that completes the make filter; the sample that starts the timeout count) and tighten the three cases | Lien (iteration 3) | Open. Iteration 3: Lien: fix before PDR | Pending | |
| <a id="finding-18"></a>finding-18 | reviewer (iteration 3, new) | Minor | WR-10, CK-REQ-A7 | REQ-TX-002, 003, 006, 007, 008, 011, 012, 015; REQ-SW-KEYER-036 | The rationales carry an item "Hazard controls implemented (docs/safety/hazards.json control_req_ids): ..." that is not one of the labelled items of 02 section 4.3 (lines 246 to 258) and sits after `TBR:`; with it REQ-TX-006 has 127 words and REQ-TX-007 122, above the 120-word limit of 02 section 4.3 line 246. The listed controls match `hazards.json` (scripted check: every listed HZ and K id equals the controls whose `control_req_ids` name the requirement), so the content is correct; only the form breaks WR-10, which 02 section 4.2 line 225 makes Minor. Fix: drop the item (the back-link is in `hazards.json`) or fold the control ids into `Why:`, and bring REQ-TX-006 and 007 to 120 words or fewer | Lien (iteration 3) | Lien: fix before PDR | Pending | |
| <a id="finding-19"></a>finding-19 | reviewer (iteration 3, carried from readiness R3) | Minor | R3 | author returns of `author:requirements-l2` | No requirements-author return with the self-check against checklist sections A to G has reached this reviewer at any iteration (readiness R3 No since iteration 1). Package section 2.1 R7 and decision 115 carry it. Fix: the requirements author files the self-check | Verified (re-issue; Lien at iteration 3) | Re-issue: Closed by the author self-check at `1af795c`, verified in "Re-issue" (iteration 3: Lien: fix before PDR, decision 115) | Not needed | |
| <a id="finding-20"></a>finding-20 | reviewer (re-issue, from author exception E-1) | Minor | WR-10, CK-REQ-A7 | REQ-SW-KEYER-024, 029, 039 `rationale` | Introduced by the `f2e02aa` fix of INSP-026 finding-1. 02 section 4.3 limits `rationale` to 120 words; at blob `4d22b399` REQ-SW-KEYER-024 has 198, 029 has 160 and 039 has 215 (whitespace count; at `db2de344` no SW-KEYER rationale exceeded 120). The content is correct and agrees with 07 section 14.2 row d; only the form breaks WR-10, which 02 section 4.2 makes Minor (the class of finding-18). The same defect is INSP-026 finding-7; one fix closes both. Fix: state the validation rule once (REQ-SW-KEYER-039) and cite it from 024 and 029, bringing each rationale to 120 words or fewer | Lien: fix before PDR (re-issue) | Lien: fix before PDR | Pending | PDR |

### Per-requirement validation (02 sections 4.2 and 5; SE HB §4.2.1.2.4)

Severity and state are kept out of this table (they are in the findings table).

| Requirement | WR failures | V1 | V2 | V3 | V4 | V5 | V6 | CK-REQ items answered No | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| REQ-TX-001 | none | Pass | Ready: customer, user, regulator | Pass | Pass | Fail | Pass | CK-REQ-E1 | iteration 1: finding-5; iteration 2: Pass (all Verified) |
| REQ-TX-002 | none | Pass | Ready: customer, user, regulator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-003 | WR-13 | Fail | Ready: customer, user, guest operator, public, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-004 | none | Pass | Ready: customer, user, guest operator, public, regulator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-005 | none | Pass | Ready: customer, user, regulator | Fail (g) | Pass | Fail | Pass | CK-REQ-B5, CK-REQ-E3 | iteration 1: finding-4, finding-5; iteration 2: Pass (all Verified) |
| REQ-TX-006 | none | Pass | Ready: customer, user, regulator | Fail (a, g) | Fail | Fail | Pass | CK-REQ-B5, CK-REQ-C1, CK-REQ-D4, CK-REQ-E3 | iteration 1: finding-1, finding-4, finding-5; iteration 2: Pass (all Verified) |
| REQ-TX-007 | WR-13 | Fail | Ready: customer, user, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-008 | WR-13 | Fail | Ready: customer, user, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-009 | WR-10 | Fail | Ready: customer, user, regulator | Pass | Pass | Pass | Pass | CK-REQ-A7, CK-REQ-B5 | iteration 1: finding-4, finding-14; iteration 2: Pass (all Verified) |
| REQ-TX-010 | WR-10 | Fail | Ready: customer, user, regulator | Pass | Pass | Pass | Pass | CK-REQ-A7, CK-REQ-B5 | iteration 1: finding-4, finding-14; iteration 2: Pass (all Verified) |
| REQ-TX-011 | WR-10 | Fail | Ready: customer, user, regulator | Pass | Pass | Fail | Pass | CK-REQ-A7, CK-REQ-B5, CK-REQ-E5 | iteration 1: finding-4, finding-12, finding-14; iteration 2: Pass (all Verified) |
| REQ-TX-012 | WR-13 | Fail | Ready: customer, user, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-013 | WR-10 | Fail | Ready: customer, user, regulator | Pass | Pass | Fail | Pass | CK-REQ-A7, CK-REQ-B3, CK-REQ-B5 | iteration 1: finding-4, finding-6; iteration 2: Pass (all Verified) |
| REQ-TX-014 | WR-13 | Fail | Ready: customer, user, guest operator, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-015 | none | Pass | Ready: customer, user, guest operator, public, regulator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-TX-016 | WR-13 | Fail | Ready: customer, user, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-C2 | iteration 1: finding-3; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-001 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-002 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-003 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-004 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-005 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-006 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-007 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-008 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-009 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | CK-REQ-C6 | iteration 1: finding-9; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-010 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-011 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-012 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-013 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-014 | WR-04 | Fail | Ready: customer, user | Pass | Pass | Fail | Pass | CK-REQ-A3, CK-REQ-A4 | iteration 1: finding-15; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-015 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | CK-REQ-C6 | iteration 1: finding-9; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-016 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | iteration 2: finding-17 Open |
| REQ-SW-KEYER-017 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | iteration 2: finding-17 Open |
| REQ-SW-KEYER-018 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-019 | WR-13 | Fail | Ready: customer, user, guest operator | Fail (d) | Pass | Pass | Pass | CK-REQ-B4, CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4, finding-7; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-020 | WR-13 | Fail | Ready: customer, user, guest operator | Fail (a, d) | Pass | Pass | Pass | CK-REQ-B4, CK-REQ-B5, CK-REQ-C2, CK-REQ-C4 | iteration 1: finding-2, finding-3, finding-4, finding-7, finding-8; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-021 | WR-13 | Fail | Ready: customer, user, guest operator | Fail (a, d) | Pass | Pass | Pass | CK-REQ-B4, CK-REQ-B5, CK-REQ-C2, CK-REQ-C4 | iteration 1: finding-2, finding-3, finding-4, finding-7, finding-8; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-022 | WR-13 | Fail | Ready: customer, user, guest operator | Fail (a, d) | Pass | Fail | Pass | CK-REQ-B5, CK-REQ-C2, CK-REQ-C4 | iteration 1: finding-2, finding-3, finding-4, finding-10; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-023 | WR-14 | Fail | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-A8, CK-REQ-B5, CK-REQ-C5, CK-REQ-F2 | iteration 1: finding-4, finding-11; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-024 | WR-13 | Fail | Ready: customer, user, guest operator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2, CK-REQ-C4, CK-REQ-C7 | iteration 1: finding-2, finding-3, finding-4, finding-9; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-025 | none | Pass | Ready: customer, user, guest operator | Fail (a) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C4 | iteration 1: finding-2, finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-026 | WR-13 | Fail | Ready: customer, user, guest operator, public | Fail (a, d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2, CK-REQ-C4 | iteration 1: finding-2, finding-3, finding-4; iteration 2: finding-17 Open, others Verified |
| REQ-SW-KEYER-027 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-028 | WR-13 | Fail | Ready: customer, user, guest operator, regulator | Fail (d) | Pass | Pass | Pass | CK-REQ-B5, CK-REQ-C2 | iteration 1: finding-3, finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-029 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-030 | WR-10 | Fail | Ready: customer, user, guest operator | Fail (a) | Pass | Pass | Pass | CK-REQ-A7, CK-REQ-B5, CK-REQ-C4 | iteration 1: finding-2, finding-4, finding-14; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-031 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-032 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | CK-REQ-C6 | iteration 1: finding-9; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-033 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 1: finding-4; iteration 2: Pass (all Verified) |
| REQ-SW-KEYER-034 | none | Pass | Ready: customer, user, guest operator; self-derived, Robin's concurrence pending (V2 table) | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 2 (new): finding-16 Open |
| REQ-SW-KEYER-035 | none | Pass | Ready: customer, user, guest operator; self-derived, Robin's concurrence pending (V2 table) | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 2 (new): finding-16 Open |
| REQ-SW-KEYER-036 | none | Pass | Ready: customer, user, guest operator; self-derived, Robin's concurrence pending (V2 table) | Pass | Pass | Pass | Pass | CK-REQ-B5 | iteration 2 (new): finding-16 Open |
| REQ-SW-KEYER-037 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | iteration 2 (new): Pass |
| REQ-SW-KEYER-038 | none | Pass | Ready: customer, user, guest operator; self-derived, Robin's concurrence pending (V2 table) | Pass | Pass | Pass | Pass | none | iteration 2 (new): Pass |

The WR to CK-REQ cells of REQ-TX-001 to REQ-SW-KEYER-033 are the iteration 1 answers; the Disposition column gives the iteration 2 result, and the five rows REQ-SW-KEYER-034 to 038 were validated at iteration 2. Rows not named in the findings pass every cell. V1 is `Fail` exactly where WR failures is not `none`. V2 names the `role` values of the stakeholder groups of 02 section 3.0: every requirement serves the customer and user; `regulatory`-tagged ones add the regulator; requirements that control HZ-003, HZ-004, HZ-005, HZ-010, HZ-012 or HZ-014 (hazards to whoever keys the unit) add the guest operator; those that control HZ-001, HZ-006 or HZ-012 (exposure of others) add the public. WR-08: REQ-SW-KEYER-004 ("that no paddle closure shortens") and REQ-SW-KEYER-007 ("send no further element") are admitted, because the Curtis mode semantics they encode are themselves prohibitions with no positive form (research F7 items 2 and 4).

V2 confirmation (Claude transcribes Robin's confirmation at the review):

| Stakeholder group (`name` and `role`) | `represented_by` | Requirements whose V2 cell names the group (count), and those marked `Fail` (ids) | Robin's confirmation (decision memo item and date) |
|---|---|---|---|
| Robin (customer), customer | Robin | 49; none Fail | |
| Robin (operator), user | Robin | 49; none Fail | |
| Friends who receive and operate units, guest operator | Robin, under the 02 section 3.0 representation rule | 19 (guest operator role); none Fail | |
| Unlicensed third parties keying under supervision, guest operator | Robin, as licensee and control operator | 19 (guest operator role, same set); none Fail | |
| Members of the licensee's household, public | Robin as licensee | 4 (public role: REQ-TX-003, 004, 015; REQ-SW-KEYER-026); none Fail | |
| Open-source reusers and bystanders, public | Robin in V2 | 4 (same set); none Fail | |
| Federal Communications Commission, regulator | Verbatim corpus read clause by clause in V3; Robin as licensee in V2 | 17 (16 REQ-TX; REQ-SW-KEYER-028); none Fail in V2; REQ-TX-006 fails V3 and V4 on its value (finding-1) | |
| PCBWay, vendor | Published design rules, checked in V4 | 0 (not a V2 voice; V4 found no fabrication-dependent value in this product) | not required |
| DigiKey and the turnkey distributors, vendor | Catalog availability, checked in V4 | 0 (not a V2 voice; the part-dependent values REQ-TX-003, 009 to 011, 014 are TBR pending TS-003) | not required |
| Claude, supplier | Not a V2 voice | 0 | not required |
| Robin (owner of the parent level), concurrence with the self-derived requirements (02 section 2.3, SE HB §6.2.1.2.3) | Robin | 4: REQ-SW-KEYER-034, 035, 036 (hazard-derived, HZ-004, HZ-010) and REQ-SW-KEYER-038 (ADR-009); each rationale begins `Self-derived:` and says the concurrence is pending here | |

V6 notes (necessity not obvious, and duplications between levels):

| Requirement | Worst outcome if omitted, or the level that keeps a cross-level duplicate (SE HB §6.2.1.2.3) |
|---|---|
| REQ-TX-004, REQ-TX-007, REQ-TX-012 | Same value as the parents REQ-SYS-011, REQ-SYS-017 and REQ-SYS-151. Externally imposed constraint (97.313(a), 97.307(e)): kept at both levels, L1 for system closure (TC-SYS) and L2 for the transmitter's own closure (TC-TX), as the rationales state; WR-09 satisfied |
| REQ-TX-015 | Not a duplicate: REQ-SYS-121 requires the evaluation on record; the 6.3 W ceiling is the input the evaluation assumes. Omitted, the evaluation would rest on an unverified power bound (HZ-001 K4) |
| REQ-TX-016 | Goal child of the Goal parent REQ-SYS-176; omitted, the transmitter share of receive-mode emission has no owner. Kept |
| REQ-SW-KEYER-013 and REQ-SW-KEYER-014 | Same tolerance on the host and on the target; not redundant, because host timing cannot show interrupt contention (the 014 rationale). Both kept |
| REQ-SW-KEYER-017 and REQ-SW-KEYER-018 | Paddle and straight-key latency from different parents (REQ-SYS-043, REQ-SYS-160); SI-018 requires one requirement per key type. Both kept |
| REQ-SW-KEYER-027 | Omitted, a timed-out stuck key would be silent and the operator would not know to open the contact (HZ-004 K3). Kept |
| T-18 listing | The two `SYS_UNALLOCATED` warnings (REQ-SYS-125, REQ-SYS-148) do not concern TX or SW-KEYER. The two SW-KEYER allocations without a child (REQ-SYS-051, REQ-SYS-054) are finding-7 |

## Readiness criteria (all true before the review starts)

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 | No | Exit 1, run three times on 2026-09-25: the failures are `docs/design/allocation.json` and, on the last run, `docs/plan/measurements.json` ("schema not found" for `allocation.schema.json` and `measurements.schema.json`), files outside this product being written concurrently; the four product files PASS against `docs/requirements/schema.json` and `docs/test_cases/schema.json`. Reported as a cross item |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | Yes | `--report-only` exit 0; no VIOLATION line names a REQ-TX, REQ-SW-KEYER, TC-TX or TC-SW-KEYER id; 40 `HAZARD_INVERSE` warnings (finding-4) |
| R3 | The author's return states the self-check against sections A to G and lists the brief's acceptance criteria | Yes (re-issue 2026-09-26); No at iterations 1 to 3 | Re-issue: section "Author self-check" (filed at `1af795c`), verified in "Re-issue"; finding-19 Verified. Iterations 1 to 3: only the test author's summary reached this reviewer; no requirements-author return with the A to G self-check was supplied |
| R4 | Every TBR has `owner`, `plan`, `close_by`; no to-be-determined placeholder | Yes | 14 REQ-TX and 8 REQ-SW-KEYER carry `(TBR)` in `description` if and only if a `tbr` object is present; every object has all three fields with `close_by: PDR`, inside the L2 limit (CDR); a grep for the to-be-determined placeholder counts 0 in all four files |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

## Participants

Author agents (not present): `author:requirements-l2`, `test-author:requirements-l2`. Reviewer: `reviewer:requirements-l2`. Software assurance reviewer (07 section 2.1.1, SW-KEYER is safety-critical): required, not yet dispatched; its verdict and the SWEHB section 7 tasks applied go into this record. Owner: disposition of findings at SRR.

## A. Format and editorial

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 | Yes | Every `description` has exactly one `shall`, active voice, subject "The transmitter" or "The keyer firmware"; no will, should or must (lint of the 49 descriptions) |
| CK-REQ-A2 | Yes | Word counts 13 to 25 (REQ-TX-009 to 012 and REQ-SW-KEYER-006, 014, 022, 032 at 25); lists in REQ-TX-004 (three steps) and REQ-SW-KEYER-013 (dit, dah, space) are one quantity with one tolerance, closed by one case |
| CK-REQ-A3 | No | REQ-SW-KEYER-014 load condition unquantified (finding-15); every other quantity has number, unit and bound |
| CK-REQ-A4 | No | No WR-07 word in any description or title (lint, and T-17 reports none); REQ-SW-KEYER-014 "continuously" stands in for a rate (finding-15) |
| CK-REQ-A5 | Yes | Descriptions name no part or algorithm; the named interface signals PA_EN and TX_KEY are the ICD-TX-ANT and 07 section 14.2 names; REQ-TX-009 to 011 name the PA output and antenna port as the measurement planes with a `Constraint:` reason; REQ-TX-013 names a divided sample (rationale item missing, finding-6) |
| CK-REQ-A6 | Yes | Ids `REQ-TX-001` to `016` and `REQ-SW-KEYER-001` to `033`, contiguous, module matches directory; titles have no shall and are at most 80 characters |
| CK-REQ-A7 | No | Rationales present, at most 120 words, cite sources and explain the value; item order wrong in five requirements (finding-14) |
| CK-REQ-A8 | No | Key types and mode names match REQ-SYS-040 (Straight, Iambic A, Iambic B, Ultimatic, Bug); "KeyClosed interlock state" matches no ConOps term (finding-11) |

## B. Stakeholder satisfaction and traceability

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-B1 | Yes | Every `parent_id` resolves to a Draft REQ-SYS whose `child_ids` names the child (checked for all 49); REQ-TX-013's parent is valid but not the best fit (finding-6) |
| CK-REQ-B2 | Yes | Each child is necessary for its parent; V6 notes record the non-obvious cases |
| CK-REQ-B3 | No | REQ-SYS-182 (TX in `allocation.json`, regulatory) has no TX child (finding-6); REQ-SYS-051 and 054 name SW-KEYER without a child (finding-7). The TX file is by design the regulatory subset for SRR (README row "created before SRR: the regulatory REQ-TX-*"); the 44 other TX-allocated SYS requirements without a TX child are expected to be allocated by PDR and are not a finding here |
| CK-REQ-B4 | No | OPS-004 and OPS-005 (both key types, SI-018), OPS-012, OPS-013, OPS-021 are covered; OPS-017 is not cited (finding-7). TX: OPS-003, 004, 007, 008, 015, 018 to 020, 022 cited |
| CK-REQ-B5 | No | `hazard_ids` present on every hazard-controlling requirement and `safety` tags consistent, but the hazard file does not list them (finding-4) and several keyer software controls have no requirement (finding-2) |
| CK-REQ-B6 | Yes | `safety` on every requirement with `hazard_ids`; `regulatory` on all 16 REQ-TX and on REQ-SW-KEYER-028 (97.109(d)); `revA` throughout; `interface` on REQ-SW-KEYER-001 with an ICD id (T-22) |
| CK-REQ-B7 | N/A | Not a CR |

## C. Technical correctness (SWE-184)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-C1 | No | Band 144.001 to 147.999 MHz matches REQ-SYS-008 and 97.301(a) (`47cfr-97.301.md` line 26, Region 2 144-148); 97.307(e) values correct (25 uW, 53 dB at 5 W; `47cfr-97.307.md` line 25); 6.3 W = 5 W + 1 dB (6.29 W); step bounds of TC-TX-004 recomputed (0.397 to 0.629, 0.794 to 1.259, 1.589 to 2.518 W); dit = 1200/WPM (TC-SW-KEYER-011 counts 3, 9 and 21 dits in 1 s at 5, 20 and 50 WPM recomputed; TC-SW-KEYER-014 and 016 lengths recomputed); harmonic bands 288 to 296, 432 to 444, 576 MHz and 1008 to 1036 MHz match `47cfr-2.106-harmonic-bands.md`. REQ-TX-006 contradicts research F7 (finding-1) |
| CK-REQ-C2 | No | REQ-SW-KEYER-019 to 021 values equal `ICD-CTL-KEY` section 3.2 (1.000 ms +/-0.010 ms; 2 ms and 5 ms TBR); REQ-TX-003 and 014 equal `ICD-TX-ANT` line 145 (1 uW); the pairing and citation rule is not met (finding-3) |
| CK-REQ-C3 | Yes | Every `safety` REQ-SW-KEYER has a `Depends on:` item naming existing hardware requirements (REQ-SYS-047, 051, 055, 071, 119, 174, 179; REQ-TX-003, 014) and OPS actions (SWE-184, `04-chapter4.md` line 19) |
| CK-REQ-C4 | No | Items a, c, h, i, j, k, l are present (REQ-SW-KEYER-022, 026, 030, 031); items d, f, g and HZ-004 K1 and K3 parts are missing or conflicting (finding-2); the debounce parent equivalence is unstated (finding-8) |
| CK-REQ-C5 | No | REQ-TX-016 uses Receive; REQ-SW-KEYER-023 uses a state name absent from the architecture list and the ConOps (finding-11) |
| CK-REQ-C6 | No | Stuck key (026), corrupted key-down state (030), keyer error (031), closed input at boot (022) are specified; out-of-range setting commands have no stated response (finding-9) |
| CK-REQ-C7 | No | No personal data field; the rule that the key line changes no setting is stated for the mode only (finding-9); image and configuration integrity belong to SW-BOOT and SW-CFG (PDR) |
| CK-REQ-C8 | N/A | Loaded data acceptance is SW-CFG and SW-BOOT scope (07 section 14.2); the keyer file loads no data |

## D. Feasibility

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-D1 | Yes | No response is faster than one 1 ms sample period (REQ-SW-KEYER-030, 031, 033 at 1 ms); element timing from TIMER0 ALARM0 at 1 us (07 section 5, research F8) makes +/-0.2 ms achievable; the +/-10 us sampling jitter of REQ-SW-KEYER-019 is ten TIMER ticks with one NVIC priority level (07 section 5), closed at Bench |
| CK-REQ-D2 | N/A | No resource value in this product |
| CK-REQ-D3 | Yes | REQ-SW-KEYER-014 names WP-SW-01 (07 section 19 row WP-SW-01: TIMER0 alarms for keyer timing and 1 kHz sampling) |
| CK-REQ-D4 | No | Tolerances are argued in the rationales (REQ-TX-005 derivation of 325 Hz recomputed: 292 Hz x 3 / 2.7 = 324 Hz; REQ-SW-KEYER-013 floor of two 100 us clock steps); REQ-TX-006 value not defensible against F7 (finding-1) |

## E. Verifiability (SWE-066, SWE-192)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-E1 | No | Methods assigned; REQ-TX-001 Inspection and REQ-TX-005, 006 Analysis on regulatory requirements lack the item (g) decision (finding-5) |
| CK-REQ-E2 | Yes | Every `verification_note` names the pre-build class, the post-build class and the closing case; SW-KEYER notes state platform independence ("the keyer logic sits behind the HAL traits with time from the mock clock"), matching 04 section 5.2 row T-SW-LOGIC and its "keyer element timing" example (04 line 127); no timing requirement names Emulation |
| CK-REQ-E3 | No | Every hazard-tracing REQ-SW-KEYER is Test with a HostUnit case and a Bench case (TC-SW-KEYER-014, 019, 034 to 039); REQ-TX-005 and 006 carry HZ-008 with Analysis and no recorded exception (finding-5) |
| CK-REQ-E4 | Yes | Outputs named are key-down, sidetone gate, end-of-over signal, keyer test point, display interface report; REQ-TX values are at the antenna port or the filter terminals |
| CK-REQ-E5 | No | Bench cases use the 04 section 6.1 instruments (tinySA Ultra through the calibrated attenuator, NanoVNA, diode probe characterized by TC-SYS-010, Pico logic capture), each credit-bearing only with its TV record; NanoVNA range to 1.5 GHz unrecorded (finding-12) |
| CK-REQ-E6 | Yes | Every requirement is cited by a Draft case of the same method with a closing type for its module (script check of all 56 cases: no method mismatch; every setup has a `Credit row:` key, I, A, T-HW, T-SW-LOGIC with its likeness argument, or T-SW-TARGET); every TC-TX has the Part 97 gate line and, where the requirement has a TBR, a TBR line |

## F. Non-redundancy and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-F1 | Yes | No two requirements state the same outcome (V6 notes); same quantities agree across files: 1 uW (REQ-TX-003, 014), 25 uW (007, 012), 1 ms sampling and 2 or 5 samples (REQ-SW-KEYER-017 to 021), 5 s and 7.5 s (REQ-SW-KEYER-026 against REQ-SYS-055) |
| CK-REQ-F2 | No | PA_EN and TX_KEY used consistently; KeyClosed versus the ConOps KEY inhibit (finding-11) |
| CK-REQ-F3 | Yes | No requirement belongs to another module; REQ-SW-KEYER-023 stops at the display interface and leaves rendering to the display module |
| CK-REQ-F4 | Yes | Priorities set: REQ-TX-007, 008 and REQ-SW-KEYER-013, 014 KDR with a `KDR:` item; REQ-TX-016 Goal with "should" in the rationale only; the rest Baseline |

## G. Plans, process documents and decision records

N/A: CK-REQ-G1 to CK-REQ-G8 (the product is a set of requirement files).

## Measurements (SWE-089)

`size=49 requirements (16 TX, 33 SW-KEYER) plus 56 closing and supporting cases read; rows=49; rows_with_wr_failures=20; v_fail=V1:20 V2:0 V3:17 V4:1 V5:7 V6:0; checklist items applicable=34 plus R1 to R4; items answered No=18 checklist items plus R1 and R3; findings major=4 minor=11 fixed=0 deferred=0; iteration=1; turns=48; minutes=75`.

## Cross items for other products (not edited by this reviewer)

| File | Change | Reason |
|---|---|---|
| `docs/safety/hazards.json` | Add the REQ-TX and REQ-SW-KEYER ids to the `control_req_ids` of the controls they implement and to the hazard `requirement_ids` union | finding-4; charter section 7 |
| `docs/safety/hazard-analysis.md` section 8.1 item 7 | Add HZ-008 exception rows for REQ-SYS-014, REQ-SYS-015, REQ-TX-005 and REQ-TX-006, or record that they move to Test | finding-5 |
| `docs/process/07-software-engineering-plan.md` section 14.2 SW-KEYER row (d) | Reconcile "menu action plus a confirmation" with HZ-004 K2 and ConOps OPS-013 | finding-2; package item H14 |
| `docs/design/allocation.json`; `docs/design/allocation.schema.json` | Correct the SW-KEYER allocation of REQ-SYS-051 and 054; add the missing schema so `validate_docs.py` exits 0 | finding-7; R1 |
| `docs/requirements/sys/requirements.json` REQ-SYS-008, 048, 162 | Keep the 614 Hz sideband assumption consistent with the corrected REQ-TX-006; state the sample-count convention of the debounce times | finding-1; finding-8 |
| `docs/process/04-verification-and-validation.md` section 6.1; `ADR-021` | Quote the 97.307(e) limit as 25 uW or -16.02 dBm; name the NanoVNA model and verified range | finding-13; finding-12 |
| `docs/safety/hazards.json` | Add REQ-SW-KEYER-034 (HZ-004 K8), REQ-SW-KEYER-035 (HZ-004 K1) and REQ-SW-KEYER-036 (HZ-004 K9; HZ-010) to `control_req_ids` and the `requirement_ids` union | finding-16 (iteration 2) |
| `docs/safety/hazards.json` HZ-004 K9, HZ-010 K3 | Record that the debounce counts are fixed (2 make, 5 open samples), not configurable 1 to 20 ms, if Robin accepts the REQ-SW-KEYER-020 and 021 proposal at SRR | finding-8 (iteration 2) |
| `docs/requirements/sys/requirements.json` REQ-SYS-008; `docs/decisions/adr/ADR-023-tcxo-and-band-edge-guard.md` | The 1 kHz guard leaves 630 Hz at +/-370 Hz carrier error against the 750 Hz (TBR) of REQ-TX-006; widen the guard or tighten the reference tolerance, closing with the REQ-TX-006 TBR at PDR | finding-1 (iteration 2) |
| `docs/icd/ICD-TX-ANT.md` line 51 | Replace "none cites this ICD yet" now that six REQ-TX carry `ICD-TX-ANT` | finding-3 (iteration 2) |
| `docs/cm/tool-validation/TV-NNN-nanovna.md` (owner input) | Robin records the NanoVNA model; the TV record states its verified upper frequency and S21 dynamic range that TC-TX-011 reads | finding-12 (iteration 2) |

## Completion

`VERDICT: NEEDS CHANGES`. Four Major findings are open (finding-1, finding-2, finding-3, finding-15); readiness R1 and R3 were not met; the software assurance review of the SW-KEYER file is outstanding. Findings stay open until the software lead marks them Verified after re-reading the corrected files.

## Closure (iteration 2, 2026-09-26)

**Re-review scope.** The author reported finding-1 to finding-15 fixed and none disputed. The reviewer (`reviewer:requirements-l2`, a new invocation in the same role) did not edit the product. It re-read the four working-tree blobs named in the front matter (all four files still untracked against `28e49e6`) with Python, and checked each fix against its source, not against the author's change list. Sources: `docs/research/regulatory-corpus-and-operators.md` F7 table and F8; `docs/research/keyer-verification-and-key-input-network.md` F12; `docs/requirements/sys/requirements.json` (REQ-SYS-008, 015, 041, 154, 182 statements and `child_ids`); `docs/reviews/SRR/decisions-for-owner.md` lines 49 and 64 (decisions 30 and 40); `docs/safety/hazard-analysis.md` 0.4.0-pha lines 308 and 430; `docs/process/07-software-engineering-plan.md` line 621 (SW-KEYER row, items a to l); `docs/conops/conops.md` lines 212 to 218 and 535; `docs/icd/ICD-CTL-KEY.md` lines 92, 118, 177; `docs/icd/ICD-TX-ANT.md` line 51; `docs/research/display-and-ui-parts.md` line 155; `docs/decisions/adr/ADR-006-*.md` line 28; the regulatory corpus `47cfr-97.307.md` line 25. Scripted checks over the 54 requirements: one `shall` per description, at most 25 words, rationale at most 120 words, rationale item order of 02 section 4.3, `(TBR)` if and only if a `tbr` object is present. Result: no violation. Across the four files: no em dash and no bare TBD (count 0), and no "KeyClosed" (count 0).

Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`. Queries: "peer review record closure block findings disposition Verified date_closed"; "keying sidebands -60 dB point 614 Hz 735 Hz continuous 50 WPM dits total mean power 10 Hz cells"; "self-derived requirement no parent owner concurrence rule L2 software requirement"; "peer review record front matter schema verdict assurance_verdict pending findings counts validation". `grep -n` then pinned lines only. The tool was available throughout.

**Commands (2026-09-26).** `tools/validate_docs.py`: exit 1, 34 passed, 2 failed. The failures are `docs/design/allocation.json` and `docs/plan/measurements.json` ("schema not found"), as at iteration 1 and outside this product. The four product files and this record PASS. `tools/traceability.py --report-only`: exit 0, no VIOLATION. Its `HAZARD_INVERSE` warnings for this product are the 4 of finding-16; the fifth warning (REQ-SYS-183) is outside it.

**Dispositions.**

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product, state Verified) | 15 (Major 4, Minor 11) | finding-1 to finding-15 |
| Disputed accepted (state Withdrawn) | 0 | none disputed |
| Open | 2 (Minor, new at iteration 2) | finding-16 (4 `HAZARD_INVERSE` warnings for REQ-SW-KEYER-034, 035, 036; fix in `hazards.json`, cross item); finding-17 (REQ-SW-KEYER-016, 017, 026 leave a reference point open, which the test author recorded inside TC-SW-KEYER-016, 017, 026; present at iteration 1 and missed by this reviewer) |

Open Major: 0. Open Minor: 2.

**Notes that are not findings.**
- TC-SW-KEYER-034 checks REQ-SW-KEYER-022 on the target with closures after 490 ms and 510 ms of open time. For a Bench confirmation this window is acceptable: the sampling period tolerance of REQ-SW-KEYER-019 alone allows +/-5 ms over 500 samples. The one-sample check is in TC-SW-KEYER-022.
- REQ-SW-KEYER-034, 035, 036 and 038 are self-derived. Each rationale begins `Self-derived:` and has a hazard id or an ADR source (02 section 2.3), so `SELF_DERIVED_UNSUPPORTED` does not fire. Robin's concurrence goes in the V2 table row added above. Without it the four are retired (02 section 11.3).
- Finding-1 is closed for this product. REQ-TX-006 now agrees with F7. The L1 inconsistency it exposes remains: the REQ-SYS-008 guard holds 630 Hz at +/-370 Hz, against 750 Hz here. The requirement states it, its TBR plan closes it at PDR, and it is carried as a cross item for REQ-SYS-008 and ADR-023.
- Finding-2 is closed for this product. The 07 row (d) text ("a menu action plus a confirmation") and HZ-004 K2 still differ. The keyer statement REQ-SW-KEYER-024 is correct under either reading, and the reconciliation stays with the 07 author and the hazard analyst (package H14).

**Readiness at iteration 2.** R1 is still No: `validate_docs.py` exits 1 on two files outside the product. R3 is still No: the author's return lists its fixes but gives no self-check against sections A to G. R2 and R4 are Yes (R4 re-checked on the 54 requirements).

```
VERDICT (iteration 2): reviewer APPROVED; record verdict NEEDS CHANGES until the SW-KEYER assurance review (07 section 2.1.1) returns and readiness R1 and R3 are met
FINDINGS: open finding-16 (Minor), finding-17 (Minor); finding-1 to finding-15 Verified
MEASUREMENTS: size=54 requirements, 59 cases; rows=54; verified=15; open=2; major_open=0; minor_open=2; iteration=2; turns=30; minutes=45
```

`record_status` stays `Open`. Under 07 section 10.2 the software lead closes the record once every finding is Verified or Deferred and the assurance verdict is in.

## Iteration 3 (2026-09-26, re-review on the committed blobs; SRR package items R8 and H15)

**Scope and independence.** Iteration 2 read working-tree blobs (`c0aabfef`, `4a24fed5`, `20e560c5`, `3c5c5dc1`); three of them are not in the git object store (`git cat-file -e` fails), so the change since iteration 2 cannot be diffed. This iteration therefore re-checked every finding, and re-ran the scripted writing checks over all 54 requirements, on the committed blobs named in `product_files` (HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; the four files were last changed in `cb00792`). The reviewer (`reviewer:requirements-l2`, a new invocation in the same role) did not author the requirements or the cases and edited no product file. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: the record drift rule and `product_files`; the 07 section 2.1.1 assurance gate on the record verdict). `grep -n` then pinned lines only. The tool was available throughout. The convergence rule of 2026-09-26 applies (charter section 4 item 3): in this round only Major findings change products, and every Minor finding is dispositioned "Lien: fix before PDR".

**Commands (2026-09-26).** `tools/traceability.py --report-only`: exit 0, 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, outside this product); no `HAZARD_INVERSE` warning. `tools/validate_docs.py` on the working tree: exit 1, 36 passed, 1 failed; the failures are other records being edited concurrently and uncommitted (`risk-register-06.md`, `classification-03-...-software-assurance.md`), not this product or this record. On an export of HEAD (`git archive HEAD`, `validate_docs.py --root <export>`): exit 0, 37 passed, 0 failed. Scripted checks over the 54 committed requirements: one `shall` per description, at most 25 words, rationale item order of 02 section 4.3, `(TBR)` if and only if a `tbr` object: no violation; rationale word count: REQ-TX-006 127 and REQ-TX-007 122 (finding-18). Across the four files: no em dash, no bare TBD, no "KeyClosed", no "-16.0 dBm" (all counts 0). Citations re-pinned: SWE-050 (`04-chapter4.md` line 13), SWE-052 (`03-chapter3.md` line 321), 47 CFR 97.305(a) (`47cfr-97.305.md` line 17), 97.307(e) (`47cfr-97.307.md` line 25).

**Dispositions at HEAD.**

| Finding | Severity | Check on the committed blob | Disposition |
|---|---|---|---|
| finding-1 | Major | REQ-TX-006: "at least 60 dB below total mean power beyond 750 Hz (TBR) offset with continuous 50 WPM dits"; rationale cites F7 614 Hz and 735 Hz and F12 as a 30 WPM figure; TC-TX-006 title and acceptance use 750 Hz to 50 kHz and the 614 Hz known answer within 10 Hz | Closed |
| finding-2 | Major | REQ-SW-KEYER-034 (memories with complements), 035 (sidetone gate held while the interlock withholds key-down), 036 (plug-presence check), 023 (both KEY inhibit causes, ConOps Table 3.4-4 rows 1 and 2) present; closing cases TC-SW-KEYER-041, 042, 043 cite them | Closed |
| finding-3 | Major | REQ-TX-003, 007, 008, 012, 014, 016 carry `interface` and `ICD-TX-ANT`; REQ-SW-KEYER-019 to 022, 024, 026, 028, 036, 038 carry `ICD-CTL-KEY`; `docs/icd/ICD-TX-ANT.md` line 51 now lists the six REQ-TX as side-A requirements (the iteration 2 cross item is done) | Closed |
| finding-4 | Minor | `traceability.py --report-only`: no `HAZARD_INVERSE` for any REQ-TX or REQ-SW-KEYER | Closed |
| finding-5 | Minor | REQ-TX-001, 005, 006 rationales name SRR decision 30 and trade TS-NNN; REQ-TX-005 and 006 cite 8.1 item 7 | Closed |
| finding-6 | Minor | REQ-TX-013 `parent_id` REQ-SYS-182; `Constraint:` item present; description states 1 kHz (TBR) | Closed |
| finding-7 | Minor | REQ-SW-KEYER-019 rationale assigns REQ-SYS-051 to the CTL network and REQ-SYS-054 to the safe-state manager; `allocation.json` now has `sw_modules` [] for REQ-SYS-051 and [SW-SAFE] for REQ-SYS-054 (the iteration 2 cross item is done) | Closed |
| finding-8 | Minor | REQ-SW-KEYER-020 and 021 state the N-sample convention and the fixed-count proposal | Closed |
| finding-9 | Minor | REQ-SW-KEYER-037 and 038 present; TC-SW-KEYER-009, 015, 032 cite 037 and TC-SW-KEYER-040 cites 038 | Closed |
| finding-10 | Minor | REQ-SW-KEYER-022 reads "500 consecutive samples (TBR)"; TC-SW-KEYER-022 acceptance holds 499 against 500 raw samples | Closed |
| finding-11 | Minor | "KeyClosed" count 0; "KEY inhibit" used | Closed |
| finding-12 | Minor | TC-TX-011 acceptance requires every point from 576 MHz to 1.5 GHz measured on an instrument whose TV record or contingency entry covers it | Closed |
| finding-13 | Minor | "-16.0 dBm" count 0 | Closed |
| finding-14 | Minor | Scripted order check: no violation | Closed |
| finding-15 | Major | REQ-SW-KEYER-014 states 50 display frames/s and 50 detents/s per encoder (TBR); TC-SW-KEYER-014 acceptance checks both loads | Closed |
| finding-16 | Minor | `hazards.json` 0.4.2-pha: REQ-SW-KEYER-034 under HZ-004 K8, 035 under HZ-004 K1, 036 under HZ-004 K9 and HZ-010 K3; no `HAZARD_INVERSE` warning | Closed |
| finding-17 | Minor | TC-SW-KEYER-016, 017 and 026 still carry the test author's open questions (the speed of the trailing space; latency of a bounced closure; the sample that starts the 5 s count) | Lien: fix before PDR |
| finding-18 | Minor (new) | See the findings table | Lien: fix before PDR |
| finding-19 | Minor (new, readiness R3) | See the findings table | Lien: fix before PDR (decision 115) |

**New-defect scan.** Every description, rationale and verification note of the 54 committed requirements and the acceptance criteria of the cases named above were read. No new Major defect was found. The only text not seen in the iteration 2 quotes is the "Hazard controls implemented" rationale item on nine requirements (finding-18); its control ids match `hazards.json`.

**Lien table.**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-17 | Minor | Lien: fix before PDR | Requirements author (REQ-SW-KEYER-016, 017, 026) and test author (TC-SW-KEYER-016, 017, 026) | PDR readiness declaration |
| finding-18 | Minor | Lien: fix before PDR | Requirements author | PDR readiness declaration |
| finding-19 | Minor | Lien: fix before PDR | Requirements author (self-check, decision 115) | PDR readiness declaration |

**Readiness at iteration 3.** R1 Yes (exit 0 on the committed tree). R2 Yes. R3 No (finding-19). R4 Yes (re-checked on the 54 committed requirements). R5 N/A. `readiness_met` stays false. Checklist items answered No at iteration 3: CK-REQ-A7 (finding-18); CK-REQ-B5 is now Yes (finding-16 closed).

**Record verdict.** Reviewer verdict: APPROVED with liens. Every finding is Closed or a Lien, so under the convergence rule the product needs no further change for SRR. The record `verdict` field stays NEEDS CHANGES for one reason only: 07 section 2.1.1 lets the software lead set APPROVED only after `assurance_verdict` is APPROVED, and the SW-KEYER software assurance review has still not been dispatched (package H1 (c), R6). When that review returns APPROVED, the software lead can set `verdict: APPROVED` with the three liens and no further reviewer iteration.

**Cross items still open (not edited by this reviewer).** `docs/requirements/sys/requirements.json` REQ-SYS-008 and `ADR-023` (the 630 Hz guard against 750 Hz, closes with the REQ-TX-006 TBR at PDR); `docs/process/07-software-engineering-plan.md` section 14.2 row (d) versus HZ-004 K2 (package H14); `docs/safety/hazards.json` HZ-004 K9 and HZ-010 K3 configurability wording if Robin accepts the fixed counts; `docs/process/04-verification-and-validation.md` section 6.1 and ADR-021 (-16.02 dBm); the NanoVNA TV record (owner input).

```
ITERATION 3 (2026-09-26): reviewer verdict APPROVED with liens; record verdict NEEDS CHANGES pending the SW-KEYER assurance review only (07 section 2.1.1)
FINDINGS: finding-1 to finding-16 Closed; liens finding-17, finding-18, finding-19 (Minor, fix before PDR); open Major 0
MEASUREMENTS: size=54 requirements, 59 cases; rows=54; verified=16; liens=3; major_open=0; minor_open=0; iteration=3; turns=25; minutes=40
```

## Author self-check (readiness R3; finding-19; package item R7; filed 2026-09-26)

**Written by the L2 requirements author, not the reviewer.** Author: `author:requirements-l2` (Claude in the requirements author role of 08 section 3.1, for REQ-TX and REQ-SW-KEYER; the TC-TX and TC-SW-KEYER cases belong to the independent test author and are not self-checked here). This section is the author's return that readiness R3 of `docs/templates/peer-review-checklist-requirements.md` revision C asks for ("The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"). It is filed in this record because 01 section 13 says no record lives only in conversation and 07 section 10.2 (Readiness criteria row) says the brief's acceptance criteria are listed in the review record. Every other section, the front matter, the R3 answer, finding-19 and `readiness_met` belong to the reviewer and are unchanged; the reviewer answers R3 again when it re-issues the record (package item R8). No product file was changed (convergence rule, charter section 4 item 3).

**Product state checked.** HEAD `5b1f2cf`. `git hash-object` equals the HEAD blob for `tx/requirements.json` (`ef206c83`, as named in `product_files`) and `sw/sw-keyer/requirements.json` (`4d22b399`). The record names SW-KEYER `db2de344`; `4d22b399` is the `f2e02aa` fix of INSP-026 finding-1 (REQ-SW-KEYER-024, 029, new 039), which this self-check covers and which the R8 delta verification of this record will read.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: where an author self-check and readiness R3 are recorded; decision 115 and the self-check location; the requirements author brief). `grep -n` and Python scans on known paths followed, only to pin lines.

**Method.** A Python scan (scratchpad script, not a repository file) over the 16 REQ-TX and 39 REQ-SW-KEYER entries: the WR-01, WR-07 (group A and group B lists of 02 section 4.2, whole-word matching), WR-08, WR-12 and WR-14 tests; `title` form and length; id pattern; rationale first label and the 120-word limit of 02 section 4.3 (whitespace count); parents resolve or `Self-derived:` leads; `hazard_ids` against `docs/safety/hazards.json` 0.4.3-pha in both directions; `safety`, `regulatory` and `interface` tags; `Depends on:` and `Fault tolerance:` on every `safety` software requirement; method and note present; the Analysis-accepted rule of 04 section 3; every `TC-` id in a note exists and cites the requirement; the evidence classes of the cases citing each hazard control; `priority`; `(TBR)` if and only if a complete `tbr` object; status Draft; duplicate descriptions; CamelCase terms in descriptions; `REQ-SW-SAFE` references. Judgment items were answered by re-reading the requirements the scan or the findings named.

### Brief's acceptance criteria

The authoring brief of the two L2 files is not on record. The acceptance criteria below are the ones the requirements row of the 08 section 3.1 author role block names as governing (02, `docs/requirements/schema.json`, checklist sections A to F), with 07 section 14.2 (SW-KEYER row, SWE-134 items), 04 section 5.2 (credit rows) and SRR entrance row 25 (L2 files at Draft, package H15).

| AC | Acceptance criterion | Source | Result | Evidence |
|---|---|---|---|---|
| AC-1 | Both files validate against the requirement schema | 08 section 3.1 | Met | `tools/validate_docs.py`: both PASS |
| AC-2 | No `tools/traceability.py` violation for the ids | readiness R2 | Met, one warning | 0 violations; `HAZARD_INVERSE` REQ-SW-KEYER-039 (HZ-004 does not list it; INSP-026 finding-5, lien; the hazard file is not this author's product) |
| AC-3 | Writing rules WR-01 to WR-14 hold | 02 section 4.2 | Met with liens and exception E-1 | Scan: one `shall`, no group A or B word, at most 25 words, titles clean, ids match, in 55 of 55. Rationale length: REQ-TX-006 (127) and REQ-TX-007 (122) are in finding-18 (lien); REQ-SW-KEYER-024 (198), 029 (160) and 039 (215) exceed 120 words (E-1, new) |
| AC-4 | Every requirement has an L1 parent or a `Self-derived:` rationale | 02 section 2.3 | Met | Every REQ-TX has a parent; REQ-SW-KEYER-034, 035, 036, 038, 039 lead with `Self-derived:` (owner concurrence is package decision 112) |
| AC-5 | Hazard links in both directions; `safety` on every hazard control; SWE-184 items on safety software requirements | charter section 7; 02 T-08; 02 section 4.3 items 4, 5 | Met, except the 039 inverse link | 14 REQ-TX and 19 REQ-SW-KEYER carry `hazard_ids` and `safety`; each `safety` SW-KEYER rationale has `Depends on:` and `Fault tolerance:`; the only one-sided link is AC-2 |
| AC-6 | Interface pairing (02 section 3.5) | WR-13 | Met | REQ-TX-003, 007, 008, 012, 014, 016 and REQ-SW-KEYER-001 tagged `interface`, each naming its ICD (finding-3 Verified) |
| AC-7 | Verification assigned at definition: method, note with classes and closing case; timing requirements do not close on Emulation | WR-11; 02 section 4.4; ADR-011 | Met | Every note names its closing case, which exists and cites the requirement. REQ-SW-KEYER-001, 002 and 013 also name TC-SYS supporting cases that cite the L1 parents, not the L2 id (supporting, not closing). All 39 SW-KEYER are Test |
| AC-8 | Hazard controls are Test, or Analysis accepted per a risk that carries the hazard | 04 section 3; SWE-192 | Met | REQ-TX-005, 006: `Analysis accepted per RSK-011`, which carries HZ-008; all other hazard controls are Test with a Bench case |
| AC-9 | SWE-134 items of the 07 section 14.2 SW-KEYER row present as requirements | 07 section 14.2; CK-REQ-C4 | Met with liens | finding-2 Verified. INSP-026 finding-2 (no `REQ-SW-SAFE-NNN` reference; scan: 0) and finding-4 (item f for the key-input mode) are liens |
| AC-10 | TBR policy; no TBD | charter section 7; WR-12 | Met | 14 REQ-TX and 11 REQ-SW-KEYER TBRs, each complete with `close_by: PDR`; no TBD |
| AC-11 | Every requirement Draft | 08 section 3.1 Status | Met | 55 of 55 |
| AC-12 | No em dash | 08 section 1 | Met | Scan: 0 |

### Self-check against checklist sections A to G

| Item | Author answer | Evidence |
|---|---|---|
| CK-REQ-A1, A2, A4, A6 | Yes | AC-3 |
| CK-REQ-A3 | Yes | finding-15 Verified; REQ-SW-KEYER-039 "300 ms (TBR)" is bounded (its wording is INSP-026 finding-6, lien) |
| CK-REQ-A5 | Yes | CamelCase scan: no part, module or algorithm name in a description |
| CK-REQ-A7 | No (liens and E-1) | finding-18 (label outside 02 section 4.3 order; REQ-TX-006 length), E-1 |
| CK-REQ-A8 | Yes | finding-11 Verified (no "KeyClosed") |
| CK-REQ-B1 | Yes | AC-4 |
| CK-REQ-B2 | Yes | No redundant requirement (no duplicate description) |
| CK-REQ-B3 | Yes | finding-6, 7 Verified |
| CK-REQ-B4 | Yes | Both key types: REQ-SW-KEYER-001 (straight key) and the paddle requirements |
| CK-REQ-B5 | Yes, except AC-2 | AC-5 |
| CK-REQ-B6 | Yes | AC-5; every `47CFR` source tagged `regulatory` |
| CK-REQ-B7 | N/A | Not a CR |
| CK-REQ-C1 | Yes | finding-1 Verified (REQ-TX-006 sideband limit); keyer timing on dot = 1200/WPM ms |
| CK-REQ-C2 | Yes | AC-6 |
| CK-REQ-C3 | Yes | AC-5 (`Depends on:`) |
| CK-REQ-C4 | Yes, with liens | AC-9 |
| CK-REQ-C5 | Yes, with lien | No state name outside the architecture and ConOps list (scan); mode change during key-down is INSP-026 finding-3 (lien) |
| CK-REQ-C6 | Yes | Stuck key (REQ-SW-KEYER-026), corrupted state (030, 034), keyer error (031), closure without plug (036), out-of-range settings (037) |
| CK-REQ-C7 | Yes | REQ-SW-KEYER-038: no command path on the key line |
| CK-REQ-C8 | N/A | No configuration record held by TX or SW-KEYER |
| CK-REQ-D1 | Yes | REQ-SW-KEYER-019 samples at 1.000 ms +/-0.010 ms, the 1 kHz sampling of 07 section 5 |
| CK-REQ-D2, D3 | N/A | No flash, RAM or crate value |
| CK-REQ-D4 | Yes | finding-10, 15 Verified; finding-17 (open reference points in 016, 017, 026) is a lien on V5 |
| CK-REQ-E1, E2, E3, E6 | Yes | AC-7, AC-8 |
| CK-REQ-E4 | Yes | Descriptions name the key line, keyer test point, antenna port or display |
| CK-REQ-E5 | Yes | finding-12 Verified |
| CK-REQ-F1, F2, F3 | Yes | No duplicate description; ConOps spellings; no requirement of another module |
| CK-REQ-F4 | Yes | `priority` set on 55 of 55 (REQ-TX: Baseline 13, KDR 2, Goal 1; REQ-SW-KEYER: Baseline 37, KDR 2); no `should` in a description |
| CK-REQ-G1 to G8 | N/A | Not a plan |

**Author exception E-1 (new, Minor, for the reviewer to disposition).** 02 section 4.3 limits `rationale` to 120 words. The `f2e02aa` fix of INSP-026 finding-1 lengthened REQ-SW-KEYER-024 to 198 words and 029 to 160, and added 039 with 215 (at `db2de344` no SW-KEYER rationale exceeded 120). Proposed fix before PDR, under the convergence rule: move the menu-validation detail into one rationale and cite it from the other two, or record the reason for the length. No product change in this run.

**Author observation O-1 (for the reviewer's evidence, not a product defect).** REQ-SW-KEYER-019 names a supporting HostUnit check of the sampling schedule in its note, but no HostUnit case cites it; its closing case TC-SW-KEYER-019 is Bench (T-SW-TARGET), which satisfies SWE-192 and E3. INSP-026 SA-192-1 (iteration 2) says each of the 19 hazard controls has "a HostUnit and a Bench case"; 18 do.

### Author's statement

The self-check agrees with the reviewer's iteration 3 answers and disputes no finding. It adds one Minor discrepancy (E-1) and one evidence observation (O-1). finding-17 and finding-18 are liens the author fixes before the PDR readiness declaration; finding-19 is answered by this section. Commands: `tools/validate_docs.py` before this section: exit 1, 47 passed, 1 failed, 48 checked; the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift against the hazard files committed at `ade0e09`), outside this record and present before the edit. `tools/traceability.py --report-only` (output to the scratchpad): exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings.

## Re-issue (2026-09-26, SRR package item R8; no further product review)

**Scope and independence.** Written by a new invocation of `reviewer:requirements-l2` in the reviewer role. It did not author the REQ-TX or REQ-SW-KEYER requirements, the TC-TX or TC-SW-KEYER cases, the author self-check above or the assurance record INSP-026, and it edited no product file and no author section. It re-issues this record without a further product review, as package item R8 provides once the author self-check of item R7 exists and the assurance pairing is met, and performs the delta verification of the two SW-KEYER files that R8 names. The convergence rule of 2026-09-26 (charter section 4 item 3) applies: only Major findings change products, and every Minor finding stays a lien, "fix before PDR".

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: peer review record readiness fields R1 to R4 with the author self-check and `readiness_met`; the TC-SYS-060 bracket and INSP-025, for the sibling record). `grep -n` then only pinned lines in `tools/validate_docs.py`, `docs/process/02-requirements-and-traceability.md` and the records.

**Product state.** HEAD `1af795c`. `git rev-parse HEAD:<path>` equals `git hash-object` for all four files. The TX pair equals the iteration 3 blobs (`tx/requirements.json` `ef206c83`, `tx/test_cases.json` `20e560c5`, last changed in `cb00792`). The SW-KEYER pair changed from the reviewed `db2de344` and `f7300569` to `4d22b399` and `d3c0c236`; `git log adcfe09..HEAD` on the four paths shows one commit, `f2e02aa` ("SW-KEYER: override path validated by the keyer per 07 section 14.2 row d (INSP-026 finding-1)"), so that commit is the whole change.

**Delta verification of SW-KEYER `requirements.json` `db2de344` to `4d22b399`** (`git diff --word-diff`: 42 insertions, 8 deletions):
- REQ-SW-KEYER-024 now reads "The keyer firmware shall change its key-input mode only after a mode-selection action and a separate confirmation that it validates as distinct operator events." (24 words, one `shall`). The rationale states the SWE-134 d basis through 07 section 14.2 row d, section 5 item 5, CS-35, CS-39 and `hazard-analysis.md` section 7 row d, and treats a menu output as an untrusted request. Parent (REQ-SYS-056), `hazard_ids`, tags `revA` and `safety`, and `design_refs` (keyer module and `ICD-CTL-KEY`, finding-3 closure) are unchanged. The note names closing case TC-SW-KEYER-024.
- REQ-SW-KEYER-029 now reads "... start its test-mode PARIS generator only after a bench-test-mode selection and a separate confirmation that it validates as distinct operator events." (25 words). Parent REQ-SYS-179 and HZ-004 unchanged; note names TC-SW-KEYER-029.
- REQ-SW-KEYER-039 is new: "The keyer firmware shall accept two operator events as distinct only from different input samples showing different inputs, or a release and 300 ms (TBR)." (25 words, one `shall`); `Self-derived:` rationale (owner concurrence under package decision 112); tags `revA`, `safety`, `hsi`; sources NGO-021, OPS-012, OPS-013; `hazard_ids` HZ-004; `tbr` with owner, plan and close_by PDR; method Test; note names closing cases TC-SW-KEYER-024, 029 (HostUnit) and 034, 037 (Bench, T-SW-TARGET, SWE-192), all of which exist and cite it.
- This record's closed findings hold on the new blob: finding-2 (SWE-134 items present; item d now carried by 024, 029 and 039), finding-3 (interface pairing: `interface` tag on REQ-SW-KEYER-001 and `ICD-CTL-KEY` in `design_refs` of 001, 019 to 022, 024, 026, 028, 036 and 038, unchanged), finding-9 (037 and 038 unchanged), finding-11 (no "KeyClosed"), finding-14 (scripted rationale item order: no violation). Scripted checks over the 39 SW-KEYER entries: one `shall` and at most 25 words in 39 of 39; `(TBR)` exactly when a `tbr` object exists (11); status Draft 39; priorities Baseline 37, KDR 2; no em dash.
- Defects of the delta: (a) REQ-SW-KEYER-039 is not in HZ-004 `requirement_ids` (`HAZARD_INVERSE` warning), and (b) its statement is compressed, with the release and interval bounds only in the rationale; both are raised and dispositioned as liens by the paired assurance record (INSP-026 finding-5 and finding-6), and this record concurs without duplicating them. (c) The rationales of 024, 029 and 039 exceed 120 words: the author's exception E-1, confirmed and raised here as finding-20 (Minor). No Major defect.

**Delta verification of SW-KEYER `test_cases.json` `f7300569` to `d3c0c236`** (`git diff --word-diff`: 35 insertions, 22 deletions): TC-SW-KEYER-024 and 029 (HostUnit) add REQ-SW-KEYER-039 to `requirement_ids`, add the control-input and menu-request mock to `setup` with the 300 ms (TBR) interval and its return-to-Draft rule, and replace the single menu-command test by tests for a validated action and confirmation (two sources; one source with a release and the minimum plus 10 ms), a request alone, a faulty menu from one sample and from one queued event, and a confirmation without its action or closer than the minimum minus 10 ms; the acceptance criteria name each. TC-SW-KEYER-034 and 037 (Bench) add REQ-SW-KEYER-039, a menu-fault injection over the UART test pads through the 3.3 V serial adapter (with the release image restored and checked by `picotool verify`), the adapter in `instruments`, and acceptance clauses for the injected faults. The cases now test the V5 meaning of 024, 029 and 039 with values from the requirement text; the injection build is disclosed as a build flavour of the release commit, as the TC-SW-KEYER-019 instrumented build already is. The 3.3 V adapter is the 04 section 6.1 cross item already recorded against REQ-SYS-150 (INSP-003 finding-15). No new finding against the V5 and CK-REQ-E6 evidence this record judges.

**Readiness R3 against the author self-check.** R3 of `docs/templates/peer-review-checklist-requirements.md` revision C reads "The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria". The section "Author self-check" (filed at `1af795c`) meets it:
- It lists twelve acceptance criteria (AC-1 to AC-12), each with its governing source (08 section 3.1, 02 sections 2.3, 3.5, 4.2 to 4.4, 04 sections 3 and 5.2, 07 section 14.2, charter section 7, SRR entrance row 25), a result and evidence. The authoring brief is not on record; taking the criteria from the documents the 08 section 3.1 requirements row names is acceptable for R3, because every criterion traces to a governing document and none is weaker than the checklist.
- It answers every item of sections A to G (B7, C8, D2, D3 and G1 to G8 as N/A with reasons).
- It names the blobs it checked, the TX blob in `product_files` and the SW-KEYER blob `4d22b399` now named, and says the test-case files belong to the independent test author and are not self-checked, which is correct for a requirements self-check.

**Spot checks of the author's claims at HEAD** (read-only Python over `git show HEAD:<path>`):
- AC-3: one `shall` and at most 25 words in 55 of 55; rationales above 120 words: REQ-TX-006 127, REQ-TX-007 122 (finding-18), REQ-SW-KEYER-024 198, 029 160, 039 215 (E-1). Agrees.
- AC-5: 14 REQ-TX and 19 REQ-SW-KEYER carry `hazard_ids`, each tagged `safety`. Agrees.
- AC-6: `interface` on REQ-TX-003, 007, 008, 012, 014, 016 and REQ-SW-KEYER-001. Agrees.
- AC-10: 14 REQ-TX and 11 REQ-SW-KEYER `tbr` objects. Agrees.
- CK-REQ-F4: REQ-TX Baseline 13, KDR 2, Goal 1; REQ-SW-KEYER Baseline 37, KDR 2. Agrees.
- Observation O-1: of the 19 SW-KEYER hazard controls, only REQ-SW-KEYER-019 has no HostUnit case (its closing case TC-SW-KEYER-019 is Bench). Agrees; SWE-192 and CK-REQ-E3 are met by the Bench case, so it is not a finding here (INSP-026 records the erratum in its own SA-192-1 answer).

**Author exception E-1.** Confirmed against 02 section 4.3 (120-word limit); rated Minor as WR-10 (02 section 4.2), the class of finding-18. Raised as finding-20, "Lien: fix before PDR", owner the requirements author.

**Pairing (01 section 13; 07 sections 2.1.1 and 10.2).** INSP-026 names the same SW-KEYER `product` and the same blobs `4d22b399` and `d3c0c236` and `paired_record: INSP-004`; at its re-issue of 2026-09-26 its verdict is APPROVED (with liens finding-2 to finding-7). This record now carries `paired_record: INSP-026`, names that record in `assurance_reviewer_agent` and copies `assurance_verdict: APPROVED` (INSP-026 cross item X-1 done). The TX files need no assurance record (INSP-026 observation 1).

**Findings at the re-issue.**

| Finding | Severity | State | Closes on |
|---|---|---|---|
| finding-1 to finding-3, finding-15 | Major | Closed (iterations 2 and 3) | |
| finding-4 to finding-14, finding-16 | Minor | Closed (iterations 2 and 3) | |
| finding-19 | Minor | Closed (Verified at this re-issue) | The author self-check at `1af795c` |
| finding-17, finding-18 | Minor | Lien: fix before PDR | Iteration 3 lien table |
| finding-20 | Minor | Lien: fix before PDR (new) | Requirements author: bring the rationales of REQ-SW-KEYER-024, 029 and 039 to 120 words or fewer; PDR readiness declaration; one fix also closes INSP-026 finding-7 |

No Major finding is open, so no finding needs an owner ruling or a package decision number. Package decision 115 (waiver of the self-check) is no longer needed for this record. The owner rulings the package lists for H15 (decisions 104, 112 and 30) govern the baseline status of the Draft L2 files and the REQ-TX method substitutions already recorded in their rationales (finding-5 closure); none holds a finding of this record.

**Answers changed at the re-issue.** R3 changes from No to Yes. CK-REQ-A7 stays No (finding-18 and finding-20, liens). R1, R2 and R4 stay Yes (R2: 0 violations; the one warning naming a product id, `HAZARD_INVERSE` REQ-SW-KEYER-039, is INSP-026 finding-5); R5 stays N/A. `readiness_met: true`.

**Tool runs at the re-issue (2026-09-26, HEAD `1af795c`, repository root, `.venv/bin/python`).** `tools/traceability.py --report-only`: exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings (`HAZARD_INVERSE` REQ-SW-KEYER-039; `SYS_UNALLOCATED` REQ-SYS-125 and 148); the rewritten `docs/vv/traceability-report.md` and `traceability.json` were restored with `git checkout` (outside this scope). `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0. `tools/validate_docs.py` after this re-issue (record drift check included): exit 1, 48 passed, 1 failed, 49 checked; this record PASS with no drift note; the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift against the hazard files committed at `ade0e09`), outside this scope and present before this re-issue. `python -m unittest discover -s tools/tests`: 392 tests, 391 pass; the one failure is `test_validate_docs.RepositoryTests.test_repository_exit_zero` on the same `hazard-analysis.md` drift. HEAD moved to `09d48be` during this re-issue through other reviewers' record commits only (`git diff --name-only 1af795c 09d48be` lists 11 files, all under `docs/reviews/SRR/checklists/`), so the product blobs named here are also the blobs at `09d48be`.

**Editorial change to earlier reviewer text (no content change).** The open-Major rule of `tools/validate_docs.py` (`open_major_findings`, line 664) reads any body line that names a `finding-<n>` and contains both the words "Major" and "Open" as an open Major finding. One narrative line of the iteration 1 Completion paragraph used "Open" as an ordinary word ("Findings stay Open until the software lead marks them Verified"); this re-issue lower-cased that word. No finding state, count or answer changed.

**Measurements (re-issue).** Items re-checked: R1 to R5, the two SW-KEYER deltas (3 requirements, 4 cases), six author claims and the four product blobs; items answered No: 1 (CK-REQ-A7, on liens); new findings: 1 (finding-20, Minor); effort 15 turns, 30 minutes (added to the front matter totals).

```
RE-ISSUE (2026-09-26, HEAD 1af795c, package item R8): VERDICT: APPROVED (with liens finding-17, finding-18, finding-20); reviewer APPROVED; assurance APPROVED (paired record INSP-026)
FINDINGS: finding-1 to finding-16 and finding-19 Closed (Major 4, Minor 13); finding-17, 18, 20 Minor, Lien: fix before PDR; open Major 0
READINESS: R1 Yes, R2 Yes, R3 Yes (author self-check at 1af795c verified), R4 Yes, R5 N/A; readiness_met true
PRODUCTS: tx/requirements.json@ef206c83, tx/test_cases.json@20e560c5 (unchanged since cb00792); sw-keyer/requirements.json@4d22b399, sw-keyer/test_cases.json@d3c0c236 (f2e02aa, delta verified)
MEASUREMENTS: re-issue no=1; new findings=1; turns=15; minutes=30; cumulative turns=118, minutes=190
```

`record_status` stays Open: the liens are neither Verified nor Deferred by an owner decision, and the software lead closes the record (07 section 10.2, action tracking).
