---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2
# and 15). This is the paired software assurance record (07 section 10.2 Record row) of the trade-study
# review INSP-110 (docs/reviews/PDR/checklists/ts-012-design-to-cost.md, reviewer APPROVED at iteration 3
# re-issue 1, committed 22e7d74), at the path INSP-110 names in assurance_reviewer_agent and cross items X-2,
# X-5, X-9 and X-12. Dispatch: 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a
# safety-critical or mission-critical component"; rules C4 and C9 of the PDR work plan.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not
# merged: git merge-base --is-ancestor 7784672 main is false on 2026-09-28). tools/validate_docs.py fails a
# record whose `checklist` names a template absent from main, so the `checklist` field names
# peer-review-checklist-risk revision A, the checklist INSP-110 applied (section B, trade studies), and
# `assurance_checklist` names the template actually applied (the INSP-074 and INSP-087 form). The product
# blob is on main; only the template is branch-only.
# id: INSP-118, pre-assigned by the lead SE brief; not used on main at HEAD 79795e4 (highest INSP-117) or on
# any cr/ branch (git grep "id: INSP-118", checked 2026-09-28).
# Filed by the lead SE on 2026-09-28 from the reviewer's record_text (the harness does not let subagents create new
# record files). Content verbatim; id INSP-118 was pre-assigned in the reviewer's brief.
id: INSP-118
checklist: peer-review-checklist-risk
checklist_revision: A
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md
product: docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md
# product_commit and product_files (iteration 2, rule C2 re-freeze): TS-012 revision 6, committed on its own at
# 3b93de1 (the only commit after 37d5824 that touches the file). The blob equals git rev-parse 3b93de1:<path>,
# git rev-parse HEAD:<path> and git hash-object <path> at HEAD 123f048 (checked 2026-09-29); it is on main.
# Iteration 1 reviewed revision 5 at 37d5824, blob 731ba0eb (product_files_iteration_1), the product_files entry of
# INSP-110 iteration 3 re-issue 1. INSP-110 iteration 3 re-issue 2 (17b6865) names the same revision 6 blob 0c9fcb96
product_commit: "3b93de11d52c17fa17e7a304656a2e8ff635efce"
product_blob: 0c9fcb9649d3fbf7a1eae3de43d10f05abe1632b
product_files: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@0c9fcb9649d3fbf7a1eae3de43d10f05abe1632b"]
product_files_iteration_1: ["docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@731ba0ebe494c1d970b3b1ba0cac4304ebbab412"]
product_commit_iteration_1: "37d5824e30348728142f74dbb7ddf45939c2b60b"
# inputs read (not reviewed), blobs at HEAD 79795e4
input_files: ["docs/reviews/PDR/checklists/ts-012-design-to-cost.md@4cbe7505 (INSP-110)", "docs/design/analysis/thermal-ts012.md@81592c34 (sections 4.1, 8, 9)", "hardware/sim/thermal/results/2026-09-28-ts012-r2/summary.csv@33b9ee3a", "hardware/sim/thermal/results/2026-09-28-ts012-r2/inhibit.csv@0e3210da", "hardware/sim/thermal/results/2026-09-28-ts012-r2/trips.csv@168adde3", "docs/design/analysis/keying-ts012.md@5121cc90 (sections 3, 4.5, 8)", "docs/design/analysis/pa-drive-ts012.md@02852058 (section 5)", "docs/design/analysis/frequency-budget.md@79d47fbb (sections 3.3, 4, 5)", "docs/process/07-software-engineering-plan.md@bfe05f43 (sections 2.1.1, 14.1, 14.2, 15)", "docs/safety/hazards.json@81cacde4 (HZ-003, HZ-004)", "docs/requirements/sys/requirements.json@f128235e (REQ-SYS-055, 063, 112, 118, 120, 155, 156, 163, 181, 182, 183)", "docs/requirements/tx/requirements.json@8b9d81e8 (REQ-TX-014)", "docs/plan/pdr-work-plan.md@bf0c9b66 (rule C1, WP-PDR-36a)", "docs/references/md/swehb/ (swe-022, 027, 033, 039, 057, 070, 080, 081, 086, 087, 089, 134, 136, 205 section 7.1)", "docs/research/rustos-toolchain-proof.md F14 and docs/research/power-tree-and-charging.md F14 (Pico 2 ADC pins)", "git log -1 --format=%B for 5c16930, eca24fa, d5a3058, 7d0d450, 37d5824 (trailers)"]
# inputs read at iteration 2 (not reviewed), blobs at HEAD 123f048
input_files_iteration_2: ["hardware/sim/freq/freq_budget.py (functions healthy_disagreement, undetected_bound, min_154_limit, fc0_accuracy_ceiling, tx_detection_time, changeover_time; re-run in the scratchpad)", "docs/design/analysis/frequency-budget.md@79d47fbb (sections 3.3, 5)", "hardware/sim/thermal/results/2026-09-28-ts012-r2/inhibit.csv@0e3210da (A4-DC rows)", "hardware/sim/thermal/results/2026-09-28-ts012-r2/summary.csv@33b9ee3a (A4-DC row)", "NXP (Freescale) AFT05MS004N datasheet Rev. 0, 7/2014, the PDF of SHA-256 84cd9fae494c628310d79f8e7381af8c39769d65fdb79acdaad17466df6dd036 that TS-012 cites (local scratchpad copy; pages 2 and 4 read with pdftotext)", "docs/design/analysis/keying-ts012.md (section 4.5 line 393, the 2 ms backwave before each element)", "docs/reviews/PDR/checklists/ts-012-design-to-cost.md (INSP-110 front matter: paired_record and assurance_verdict still pending)", "git log -1 --format=%B 3b93de1 and tools/check_commit_msg.py on it"]
paired_record: INSP-110
product_type: trade-study-or-adr
# criticality: safety-critical. TS-012 decides the hardware of the REQ-SYS-118 thermal inhibit and the
# REQ-SYS-181 cut-off (07 section 14.1 "Thermal protection", SW-SAFE thermal unit with SW-TXSEQ actuation,
# HZ-003), the REQ-SYS-120 permit and TX_KEY drive gating (SW-TXSEQ and the SW-SAFE PA-permit flag, HZ-004),
# the REQ-SYS-182 prescaler and counter (frequency verification unit, HZ-008), and the Morse menu override
# command path (07 section 14.1, Proposed). INSP-110 sets the same criticality with the same basis
criticality: safety-critical
product_size: "iteration 2: 1 trade study (1248 lines, revision 6; 373 changed lines against revision 5, 18 design items); delta on 3 Major findings (REQ-SYS-182 and 154, REQ-SYS-181, REQ-SYS-120 with D-11, D-17, D-18 and REQ-TX-014) and the changed text. Iteration 1: 1 trade study (1133 lines, revision 5; 6 alternatives, 2 finalists, 13 criteria, about 90 requirement deltas, 16 design items); assurance lens on 9 safety controls or functions (REQ-SYS-118, 120, 155, 156, 181, 182, REQ-TX-014, the keying loop tables, the Morse menu override path) and the RP2350 pin and ADC budget"
sprint: PDR-prep
author_agent: "author:TS-012 (Claude as trade-study author, invocation of 2026-09-27)"
reviewer_agent: "sa-reviewer:TS-012-design-to-cost"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:TS-012-design-to-cost (software assurance function; paired file review INSP-110 by reviewer:TS-012-iter1 to reviewer:TS-012-iter4)"
iteration: 2
# readiness_met: R1 to R4 hold at iteration 2 (R1: revision 6 committed and frozen at 3b93de1; its equality with the
# paired record's product_files holds since INSP-110 iteration 3 re-issue 2 (17b6865, blob 0c9fcb96). R3:
# validate_docs.py 109 passed, 8 failed, the 8 records unrelated to TS-012; traceability.py 0 violations).
# Iteration 1: R1 to R4 held on revision 5
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 2 (rule C1): finding-1 to finding-3 (Major) Verified on
# revision 6; finding-4 to finding-8 (Minor) and the new finding-9 (Minor) are liens, owner the TS-012 author with
# the work packages named in each, due at the CDR readiness declaration. Iteration 1: NEEDS CHANGES (3 Major open)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES although both reviews are APPROVED:
# (a) CR-012 is not merged (7784672 is not an ancestor of main on 2026-09-29; the template blob 5b135285 is unchanged
# on the branch), lead SE convention of 2026-09-27; (b) INSP-110 (17b6865) carries paired_record INSP-118 but still
# copies assurance_verdict NEEDS CHANGES from iteration 1; it takes APPROVED from this iteration (cross item X-1)
verdict: NEEDS CHANGES
findings_major: 3
# findings (iteration 2): 3 Major and 6 Minor raised in all (finding-9 new at iteration 2); verified: finding-1 to 3;
# open as liens (rule C1): finding-4 to 9. Iteration 1: 3 Major and 5 Minor, all open
findings_minor: 6
findings_open: 6
findings_fixed: 0
findings_verified: 3
findings_deferred: 0
assurance_findings_major: 3
assurance_findings_minor: 6
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-086 7.1 task 1", "swe-087 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
# items_no (iteration 2): items still No on a lien (finding-4 to 9); swe-039 t4, swe-057 t2, SA-C-h, SA-C-i and SA-D6
# become Yes with finding-1 to 3 Verified; SA-C-a becomes No on the new finding-9
items_no: ["swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-080 7.1 task 1", "swe-080 7.1 task 2", SA-C-a, SA-C-d, SA-C-f, SA-C-g, SA-C-j, SA-E3]
items_no_iteration_1: ["swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-080 7.1 task 1", "swe-080 7.1 task 2", SA-C-d, SA-C-f, SA-C-g, SA-C-h, SA-C-i, SA-C-j, SA-D6, SA-E3]
# effort: iteration 1 48 turns, 95 minutes; iteration 2 32 turns, 70 minutes
effort_turns: 80
effort_minutes: 165
record_status: Open
date: 2026-09-28
date_closed: null
---

# Peer review record INSP-118: software assurance pair of INSP-110, TS-012 design-to-cost architecture

**Product.** `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` blob `731ba0eb` at commit `37d5824` (revision 5, Proposed; A4 315 recommended over A5 270). The blob is equal at `37d5824`, at `HEAD` (`79795e4`) and in the working tree. It is the `product_files` entry of INSP-110 iteration 3 re-issue 1. **Paired record:** INSP-110 (`ts-012-design-to-cost.md`), reviewer verdict APPROVED on revision 5 with three Major findings Verified and Minor liens finding-19 to finding-23; record verdict held for this pair (its cross items X-2, X-5, X-9, X-12).

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`): readiness R1 to R4, sections A to F, the section B row `trade-study-or-adr` and the row "Every product type", plus the section 7.1 tasks of the other SWEs the study touches. The template is branch-only; the front matter explains the `checklist` field.

**Assurance lens (the brief).** The safety-critical hardware controls and firmware functions the study decides or depends on: the REQ-SYS-118 PA thermal inhibit and the REQ-SYS-181 cut-off (HZ-003 K2, K9); the REQ-SYS-120 second TX-permit condition and the D-11 CLK1 and bias gating (HZ-004 K8, INSP-110 finding-23); REQ-TX-014; the REQ-SYS-182 frequency verification (HZ-008 K7); the keying loop ramp and feed-forward tables (D-10); the Morse menu override path; the RP2350 GPIO and ADC budget; 07 section 14.1 component criticality; whether each finalist's safety controls can be implemented and verified in software on the Pico 2; and whether A4 over A5 holds from the assurance side.

**Acceptance criteria (rule C7).**
- Every task of the section B rows `trade-study-or-adr` and "Every product type" is in the task table, with the tasks of the other SWEs the study touches: it is the risk-driven decision of RSK-002, RSK-006 and RSK-038 (software-tagged risks among them, SWE-086), a hardware change that feeds safety-critical units (SWE-080 task 1), and it creates Record-class items (SWE-080 task 2, SWE-081 task 2).
- Every SWE-134 item that 07 section 14.2 allocates to the units the study constrains is checked at trade-study maturity (the recommendation neither precludes nor weakens the provision): `SW-SAFE` thermal unit (a, d, g, h, j, k, l), `SW-TXSEQ` and the PA-permit flag (a to l), the frequency verification unit (a, b, f, g, h, i, k, l), the menu override command path (a, d, e, g, i, k), `SW-TXSEQ` units `envelope` and `alc` (b, g, h, k), and the configuration guard's field list (f, g).
- Each control the recommended A4 relies on is checked for the single-fault argument of 07 section 14.2 row i and against the cited analysis record, not against the study's summary of it.
- HZ-003, HZ-004 and HZ-008 software contributions are checked by action, inaction and incorrect action (SWEHB `swe-205` 7.1 task 1).

**Independence (rule C4).** This invocation authored no part of TS-012 (revisions 0 to 5), of the six analysis records it cites, of their review records, or of INSP-110. It is not the file reviewer of any of them. It edited no product file and no record.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: the software assurance pair records of trade studies; the Pico 2 ADC channel and pin budget; the frequency-verification gate and the pre-`PA_EN` check. `grep`, `awk`, `git grep` and short Python reads of the JSON files were used afterwards only to pin lines, extract the SWEHB section 7.1 task lists and read REQ-SYS-055, 063, 112, 118, 120, 155, 156, 163, 181, 182, 183, REQ-TX-014, HZ-003 and HZ-004. The rustos repository was not read. LTspice was not run. Nothing was downloaded.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | `swe-039 7.1 task 4`, `swe-057 7.1 task 2`, `swe-080 7.1 task 1`, SA-C-h, SA-C-g | TS-012 section 8.10 row REQ-SYS-182 (line 818); section 7.1 A4 30 ppm row (line 354); section 7.3 key-down sequence (line 446); section 8.1 block diagram ("PWM edge counter <- /8 divider"); section 8.13 Q1 and follow-on decision 6; section 8.4 AB2 | **REQ-SYS-182 cannot be met as written by the recommended A4 (no TCXO), and the study's budget contradicts the reviewed frequency-verification analysis.** Section 8.10 keeps REQ-SYS-182 at 10 kHz with a budget of "2.5 ppm (TCXO) + 30 ppm (Pico 2 crystal, recalled, Low) = 4.8 kHz ... plus 0.16 kHz gate quantization (50 ms gate, /8): 5.0 kHz inside 10 kHz. A4: 9.0 kHz, 1 kHz margin". The reviewed WP-PDR-20 note `docs/design/analysis/frequency-budget.md` section 3.3 (INSP-056 APPROVED; TS-012 does not cite it) differs on four points. (a) The RP2350 crystal is +/-30 ppm tolerance, +/-30 ppm stability and +/-5 ppm aging (datasheet Table 596), 65 ppm in all, not a recalled 30 ppm. (b) The counter accuracy over the interval available before RF (FC0 interval 12, 4 ms: 500 Hz at the /8 input, 4 kHz at the carrier) is a term of the budget. (c) The measured threshold must satisfy both d < T and T + d <= 10 kHz (INSP-056 finding-1), so the healthy disagreement d must stay under 5 kHz. (d) On the raw crystal timebase (route R1) d is 13.99 kHz even with a 2.5 ppm TCXO, so REQ-SYS-182 at 10 kHz and REQ-SYS-154 fail; only route R3 meets them: the TCXO is counted on a second GPIN in receive and the XOSC/TCXO ratio cancels the reference error. For A4 the reference is the Adafruit 2045 module's own 25 MHz crystal, which has no output the RP2350 can count independently of the synthesizer programming, so R3 is not available. On R1 with a 30 ppm reference, d is about 4.0 + (65 + 30) ppm x 148 MHz = 18.1 kHz at interval 12, 16.1 kHz at interval 13 (reviewer arithmetic on the note's formula). REQ-SYS-182 would then need a window of about 16 to 18 kHz and REQ-SYS-154 a true-error limit above about 32 kHz, both by CR. **Timing.** 07 section 14.2 rows a and h make the counted agreement a prerequisite before `PA_EN`, and TC-SYS-110 injects the fault "before a key-down" and requires no carrier before transmit. TS-012's own sequence enables CLK1 at t0 + 8 ms and starts the ramp at t0 + 10 ms. The keying note (section 4.5) confirms CLK1 runs "for 2 ms before every element". That 2 ms window holds neither the note's 6.0 ms changeover check (C-14: 4 ms FC0 + 2 ms software) nor TS-012's 50 ms gate. **Why Major:** a safety requirement of HZ-008 K7 (Critical) is presented to the owner as kept with margin for the recommended alternative. The owner is offered the TCXO (AB2) only as an optional buy against the 30 ppm Red (Q1: "only if you want the 30 ppm reference Red retired"). In fact, for A4 the TCXO decides whether REQ-SYS-182 and REQ-SYS-154 hold as written. The owner would decide Q1 on a wrong basis. The SWE-134 h provision (frequency-verified prerequisite) is also not provided by the study's counter and sequence. **Fix:** (1) Replace the section 8.10 REQ-SYS-182 budget with the `frequency-budget.md` method: route, counter (FC0 on a GPIN, or show the PWM edge counter meets the same terms), interval, d, T and margins, per finalist. (2) For A4, either put AB2 in the baseline with route R3 (TCXO into XA and to a second GPIN), or record the REQ-SYS-182 and REQ-SYS-154 deltas with their values in section 8.10 and put them to the owner with Q1. Also route R3's second GPIN for A5, which the section 8.1 diagram does not show. (3) Restate the key-down sequence so that CLK1 (with the drive held off) runs long enough before `PA_EN` for the pre-transmit check inside the 12 ms lead-in of REQ-SYS-161, consistent with D-11 (finding-3). (4) Add the matching requests to WP-PDR-20, WP-PDR-35 and WP-PDR-16b (HZ-008 K7 wording) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Major | `swe-134 7.1 task 6`, `swe-057 7.1 task 2`, `swe-080 7.1 task 1`, SA-C-i, SA-D6 | TS-012 section 4.1 row A4 M4 ("pass (both controls restored ...)"); section 4.2 C8-A4 ("the 95 C sink cut-off never acts at 45 C"); section 8.14 D-6 ("REQ-SYS-181 kept as the backstop"); section 8.10 REQ-SYS-112 row ("REQ-SYS-181: the sensor location ... is referred"); `thermal-ts012.md` sections 4.1, 8 change 6, 9.2, request R-3 | **For the recommended A4, the firmware-independent cut-off K9 (REQ-SYS-181) does not bound the junction in the thermistor-failure branch of HZ-003, and the study counts it as the backstop.** 07 section 14.2 row i says the thermistor-failure branch "is bounded only by the hardware PA over-temperature cut-off (REQ-SYS-181, 95 C)". The thermal record TS-012 cites shows the following for A4-DC at the 45 C corner (`summary.csv`, `trips.csv`): with the K2 inhibit defeated (HZ-003 C4, "sensor reading cold"), the sink settles at 84.6 C and the 95 C sink cut-off "never" acts, and the junction settles at 122.6 C (band 107.9 to 142.9 C). The adverse-dissipation case of `inhibit.csv` is 6.86 W (50 % hand match). There the sink reaches about 45 + 6.86 x 7.13 = 93.9 C, still under the trip, and the junction about 45 + 6.86 x 13.98 = 140.9 C before its band (reviewer arithmetic on the lumped resistances of `summary.csv`, Low). At the point HZ-003 K9 and TS-011 rule 14 name ("a second NTC at the PA", on the tab copper), the nominal steady reading is about 98.2 - 4.5 = 93.7 C, under the 95 C trip. In the adverse case it trips with the junction at about 130 to 139 C. No record carries the AFT05MS004N maximum junction rating: TS-012, `thermal-ts012.md` (its inputs row carries only RthJC 4.4 K/W) and `pa-device-candidates.md` all lack it. So the bound cannot be judged against the device. For A5, the same cut-off on the sink acts with the channel at about 120 C (123 C at the 98 C edge), against the 175 C channel rating that INSP-112 finding-12 reads. TS-012 discloses the A4 fact only inside the C8-A4 evidence cell. It then passes A4 on M4 ("every hardware hazard control adopted at SRR (... 181 ...) is implemented") and adopts D-6 with "REQ-SYS-181 kept as the backstop" for both finalists. **Why Major:** the control that is the only bound of a Critical hazard branch (SWE-134 i) is shown by the study's own evidence not to act for the recommended design, and the M4 pass rests on it. This is the INSP-087 finding-1 pattern. The location question is already routed (thermal R-3), but the study does not say what it means for A4. **Fix:** (1) In section 8.14 D-6 and the section 8.10 REQ-SYS-181 row, state per finalist where the REQ-SYS-181 sensor sits and the junction at which it trips: for A4, NTC-2 on the tab copper (TS-011 rule 14 point), since the sink location never acts. (2) Read the AFT05MS004N maximum junction rating from its datasheet into section 7.3 and show the trip junction below it with margin. If it is not, propose the REQ-SYS-181 threshold delta for A4. (3) Mark the A4 M4 cell conditional on (1) and (2) until they are stated. (4) Add the A4 values to the thermal R-3 request to WP-PDR-16b and the REQ-SYS-181 writer | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance (severity raised from INSP-110 finding-23, Minor) | Major | `swe-134 7.1 task 6`, `swe-057 7.1 task 2`, SA-C-i, SA-D6 | TS-012 section 7.3 ("CLK1 enable is the second, independent condition of REQ-SYS-120", line 446); section 8.10 rows REQ-SYS-055, 120, 180, 181, 092 ("with CLK1 enable as the second condition", line 834) and REQ-SYS-014, 015 (REQ-TX-014); section 8.14 D-11; section 7.1 revision 5 row "A4 New: REQ-TX-014"; section 8.13 follow-on decision 4 | **As written, the recommended design has no separately maintained PA permit, so the SWE-134 item i provision for HZ-004 is absent.** INSP-110 finding-23 raised the conflict: D-11 makes CLK1 enable follow TX_KEY, while section 7.3 and 8.10 name CLK1 enable as the second condition of REQ-SYS-120. This record raises its severity under the assurance lens (template rule: a SWE-134 item that 07 section 14.2 allocates has no provision at the product's maturity). 07 section 14.2 row i and HZ-004 K8 require "a keyer key-down AND the separately maintained PA-permit flag of the safe-state manager", so that "a single GPIO write or a single corrupted flag cannot produce RF". TS-012 revision 5 names no `PA_EN` line and no permit anywhere (`grep` finds `TX_KEY` only in D-11 and `PA_EN` nowhere). The hardware clamps act on the envelope reference and VGG node, and REQ-SYS-055's monostable is itself triggered by TX_KEY (HZ-004 K5). With D-11, the drive (GVA-84+ bias and CLK1) and the ramp would all follow TX_KEY. A single stuck-high TX_KEY write would then produce RF, bounded only by the 7.5 to 13 s cutoff. The study also does not say whether D-11's gating is hardware on the TX_KEY line (GVA-84+ bias switch and the Si5351 output enable) or an I2C write. If it is an I2C write, it is a firmware action, not a hardware condition. A4 depends on D-11 more than A5: without it A4 fails REQ-TX-014 by 7 to 11 dB (keying note section 4.5), and D-11 is counted as retiring A4's REQ-TX-014 Red at no cost. REQ-TX-014 is the "transmitter half of the two conditions of REQ-SYS-120" (its rationale), and follow-on decision 4 asks the owner to restate its condition with no safety note. **Fix:** (1) In section 7.3 and the section 8.10 REQ-SYS-120 row, name the `PA_EN` (permit) line and what it gates in hardware independently of TX_KEY, for example the release of the VGG or gate-bias clamp or the TX 5 V switch, so that RF needs both. (2) State whether the D-11 gating is hardware on TX_KEY or firmware. (3) Put the REQ-TX-014 restatement to the owner with an HZ-004 note from WP-PDR-16 and 17, or keep option (b), the series drive switch, as a cost line for A4. (4) Reconcile D-11 with the pre-`PA_EN` frequency check (finding-1 part 3) | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-134 7.1 task 4`, SA-C-g | TS-012 section 8.1 block diagram ("ADC: ALC, pot x2, AGC env, cells, NTC x2"); section 8.7 (two pots on ADC inputs); section 8.14 D-6 and D-10 ("needs one ADC channel ... (WP-PDR-20 pin map)"); row E5 | **The study adds analog inputs past the Pico 2's three external ADC channels without counting them or stating the safety effect of the fix.** Section 8.1 and D-10 name at least eight analog signals: the ALC detector (REQ-SYS-156), two potentiometers, the AGC envelope, the cells (pack and mid-tap for the per-cell REQ-SYS-097 check), two NTCs (REQ-SYS-118 and the sink or duty-limit NTC) and the trim-integrator output. The Pico 2 exposes GPIO26 to GPIO28 as ADC inputs; GPIO29 is the on-board VSYS/3 (`rustos-toolchain-proof.md` F14, `power-tree-and-charging.md` F14). Route R3 of finding-1 also needs two GPIN pins. The plan already expects a shortfall (WP-PDR-36a: "ADC allocation with the shortfall resolved"). But the study that creates it carries no multiplexer or external ADC in row E5, and it does not note the safety effect. A multiplexer puts the REQ-SYS-118 thermistor, the REQ-SYS-156 detector and the cell readings behind one channel-select path shared with non-safety inputs (the pots and the AGC). A wrong select gives a plausible wrong value that the REQ-SYS-155 range check does not catch (SWE-134 g, task 4 b). The ranking is unaffected (both finalists have the same inputs). **Fix:** count the analog inputs and GPIN pins per finalist in section 8.1 or 8.14. Carry the multiplexer (or an I2C ADC) as an estimated line. Send WP-PDR-36a and WP-PDR-35 a provision: a channel-identity check (a reference channel read per scan), safety channels on direct ADC pins where possible, and the scan time against the 20 Hz thermistor rate and the per-element trim capture | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | `swe-134 7.1 task 6`, SA-C-j | TS-012 section 4.2 C8-A4; section 8.10 REQ-SYS-112 row ("enforced by the REQ-SYS-118 inhibit"); section 8.13 follow-on decision 1; section 8.14 D-6; `thermal-ts012.md` section 4.1 table and section 9.1 item 4; `inhibit.csv` | **Under the proposed REQ-SYS-112 delta, the safety-critical thermal unit becomes the control that holds the KDR. For A4 its setpoint is not bounded until the match run.** Follow-on decision 1 and D-6 give the REQ-SYS-118 setpoint as "about 77 C (A4) or 81 C (A5)". The thermal record's all-adverse case gives 60.0 C for A4 and 71.7 C for A5 (`inhibit.csv`), and it adds "A 60 C setpoint at 45 C ambient would leave A4 little transmit time; that duty was not computed". For A4 the governing input is the AFT05 drain efficiency, which only the WP-PDR-21 match run bounds (thermal section 9.1 item 4). D-6 also offers a firmware duty limit that "refuses a new key-down" above S as the alternative. That changes REQ-SYS-118 ("cease RF output within 100 ms") and the `SW-SAFE` thermal unit provision j of 07 section 14.2 ("a reading above 85 C ends RF within 100 ms"), and section 8.10 lists no restatement for it. The safety conclusion holds, because a lower setpoint is on the safe side. But the owner is not told that A4's usable transmit time at 45 C may be set by a safety threshold that is not yet known, and the one available cannot be traced to a requirement. **Fix:** in section 8.10 (REQ-SYS-118 row) and follow-on decision 1, give the setpoint range per finalist with the all-adverse value, tie A4's value to the match run, and state which form (inhibit or duty limit) is proposed, with the REQ-SYS-118 wording the duty limit needs. Thermal request R-5 to WP-PDR-35 then carries the chosen form | Open | Pending | |
| <a id="finding-6"></a>finding-6 | assurance | Minor | SA-C-d, `swe-205 7.1 task 3` | TS-012 section 8.7 (ALT-hold rule; sequence steps 3 to 6; "The menu override command path stays safety-critical"); section 8.10 REQ-SYS-163 row | **One override path of the Morse menu has no confirmation, and the decoder that generates override events is not placed in the Proposed safety-critical path.** 07 section 14.2 row d, and HZ-004 K2 for Straight-on-tip, require "any other key-input mode change" to need "a menu action (or the held combination) followed by a separate confirmation, never a single knob or key gesture". Section 8.7 has "holding ALT for 2 s steps the key mode ... and the radio announces the new mode", with no confirmation. The REQ-SYS-052 interlock re-run of REQ-SYS-163 still keeps transmit disarmed until the new mode's inputs read open, so the hazard stays controlled. But the item d provision is not met by the path as written. Second, the 5 W step (REQ-SYS-063) and the guest lock take their confirmation "R" from the adaptive straight-key decoder ("the highest firmware risk"). So the decoder units that emit the action and the R are the generating side of the menu override command path (07 section 14.1, Proposed; items a, d, e, g, i, k). The receiving-side rule of row d ("two distinct operator events that it validates itself from the debounced input samples") needs a Morse-specific definition. The study names neither. **Fix:** add a confirmation press to the ALT-hold path (for example ALT or MENU within a window after the announced mode; buttons only, so it still works with a key reading closed). State in section 8.7 that the decoder units emitting override events are in the Proposed path, and route the Morse form of the row d validation to WP-PDR-35 and 41 and to the WP-PDR-16 and 17 determination | Open | Pending | |
| <a id="finding-7"></a>finding-7 | assurance | Minor | SA-C-f, `swe-205 7.1 task 1`, `swe-080 7.1 task 1` | TS-012 section 8.14 D-9, D-10; section 7.3 table R5-2 row 6 (A4 "Not assessed"); `keying-ts012.md` section 3 (the A4 gate bias "driven by the same closed envelope loop") | **The keying-loop items add persisted, safety-relevant data and firmware authority over the PA gate bias that the study does not classify, and A4's open-loop case is not assessed.** D-10 adds a per-unit feed-forward VGG (A5) or VGS (A4) table, a stored trim restored at power-on, a per-over zero calibration and NTC compensation. The feed-forward PWM sets the gate bias directly. None of these values is in the configuration guard's list of safety-relevant fields in 07 section 14.1 ("power step, tune level, guest lock, frequency calibration, thermal thresholds, keyer mode, debounce"; SWE-134 f, g). A corrupted table entry or a PWM stuck at full duty is an incorrect action that raises gate bias and dissipation. That is HZ-003 cause C3 ("PA gate-bias fault raising dissipation"), classed Hardware in `hazards.json`, and an HZ-008 over-drive case. 07 section 14.1 classes the `envelope` and `alc` units mission-critical on the basis that "a fault raises harmonics by at most 3 dB". That basis does not cover a gate-bias command. For A5 the hardware VGG clamp (3.46 V; D-9 pack-dependent) and REQ-SYS-156 bound the open-loop case. For A4 no gate-bias clamp is stated, and row 6 ("open-loop output at 8.4 V at most 8 W") is "Not assessed". **Fix:** list the feed-forward table, the stored trim, the calibration and the NTC coefficients as guarded safety-relevant fields with range limits (request to WP-PDR-35). State A4's hardware gate-bias ceiling and run A4's open-loop case in WP-PDR-22. Request WP-PDR-16b to add the firmware incorrect-action path to HZ-003 C3, and ask for the `envelope` and `alc` classification to be re-run at the PDR determination (03 section 4.1 step 5) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | assurance | Minor | `swe-080 7.1 task 2`, SA-E3 | Commits `5c16930`, `eca24fa`, `d5a3058`, `7d0d450`, `37d5824` | Every commit that creates or revises TS-012 (05 Table 4-1 row 12, Record class) lacks the `Refs:` trailer that 05 section 4.5 requires; each carries only `Co-Authored-By` (`git log -1 --format=%B`). `37d5824` also uses the type `ts`, which is not one of the eleven types of 05 section 4.5. `tools/check_commit_msg.py --range <c>^..<c>` reports `REFS_MISSING` for all five and `SUBJECT` for `37d5824` (TV-019 Validated, accreditation pending, so the messages themselves are the evidence). No `CR:` trailer was needed (Record class). This is the INSP-074 finding-4 and INSP-087 finding-3 pattern. **Fix:** history is not rewritten. The lead SE lists the five commits in the `configuration-status.md` change log as RID candidates for the PDR, and the revision 6 commit carries `Refs: TS-012, INSP-110, INSP-118` with a 05 type (`docs`) | Open | Pending | |

Three Major findings are open, so the assurance verdict is NEEDS CHANGES (rule C1). None of them reverses the ranking, and each has a no-cost or low-cost fix. But in each case the recommended A4 is shown passing a safety requirement or a SWE-134 provision that its own evidence, or a reviewed analysis, does not support. Findings 1 and 2 bear on the A4 and A5 comparison and are weighed in the section "Effect on the A4 and A5 choice".

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product that 07 section 2.1.1 routes (row "Trade studies and ADRs", safety-critical column Yes) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 section 15) with this template. The NASA-STD-8739.8 part is relieved (next column) | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | No software make-or-buy option arises. The decision buys hardware (modules with pin headers or castellations, discrete parts, boards), and the firmware runtime make/buy stays TS-002's (07 section 17.2). The COTS charger (XTAR MC1) is equipment outside the radio. Its HZ-002 re-scope is a hazard-analysis matter routed in section 8.12 (WP-PDR-16, 17) | | none |
| swe-033 7.1 task 2 | SC | Yes | No software acquisition activity exists, so no software requirement flows to a supplier | | none |
| swe-033 7.1 task 3 | | Yes | Section 7.1 assesses the finalists' risks. No software acquisition risk exists. The assurance risk goes to SA-F1 | | none |
| swe-039 7.1 task 4 | | No | Trade study and source data assessed against the six analysis records it cites and the reviewed `frequency-budget.md`. The REQ-SYS-182 budget uses a recalled crystal value against a datasheet value in a reviewed record, and it omits the counter term (finding-1). The AFT05 junction rating that the thermal bound needs is in no record (finding-2). The thermal figures used by findings 2 and 5 were read from `summary.csv`, `trips.csv` and `inhibit.csv` and agree with `thermal-ts012.md` section 4.1 | | finding-1, finding-2 |
| swe-057 7.1 task 2 | | No | The architecture the study fixes does not show REQ-SYS-182 (finding-1), REQ-SYS-181 as the thermistor-failure bound for A4 (finding-2) or REQ-SYS-120 (finding-3) met | | finding-1, finding-2, finding-3 |
| swe-134 7.1 task 4 | SC | No | Isolation of safety-critical data from non-safety inputs: the ADC shortfall puts safety readings behind a channel-select path shared with the pots and the AGC, and the study does not state the provision (finding-4). Otherwise the decision adds no software component that changes the 07 section 5 item 5 isolation | | finding-4 |
| swe-134 7.1 task 6 | SC | No | Consistency with the hazard analysis: HZ-003 K9 does not bound A4's thermistor-failure branch as the study places it (finding-2); HZ-004 K8 has no permit line (finding-3); HZ-003 K2's setpoint for A4 is not bounded and its duty-limit form is untraced (finding-5) | | finding-2, finding-3, finding-5 |
| swe-027 7.1 task 1 | | N/A | Condition not met: no COTS, GOTS, MOTS, OSS or reused software is acquired (07 section 17.1 register unchanged; the Pico 2 bootrom stays under TS-002) | Conditional task of the section B row ("reused or OSS component chosen"); 07 section 17.1 | none |
| swe-136 7.1 task 1 | | N/A | Condition not met: the decision selects no software tool. LTspice is accredited (ACC-LTSPICE-001), and the analysis checkers are stated as developer evidence (section 6 item 8). The thermocouple thermometer of D-16 is an instrument with its own TV record (thermal section 9.1 item 2) | Conditional task of the section B row ("when the decision selects a tool"); 07 section 17.3 | none |
| swe-070 7.1 task 1 | | N/A | As swe-136: no model or simulation qualifies flight software or equipment here; the analyses are decision support | Conditional task of the section B row; 07 section 17.3 | none |
| swe-205 7.1 task 1 | SC | Yes | `hazards.json` names the component-level contributions: HZ-003 `firmware_role` ("Firmware sets the PA bias and power ... reads the PA thermistor, folds back power, inhibits"), C4; HZ-004 C4, K8. The decision adds mechanisms under them, not new contributions: feed-forward gate-bias tables (incorrect action, finding-7), drive gating on TX_KEY (action, finding-3), a firmware duty limit (inaction, finding-5), decoded override events (incorrect action, finding-6). Each is carried by its finding with a request to WP-PDR-16b | | none |
| swe-205 7.1 task 3 | SC | Yes | The decision moves component scope. `SW-PWR` loses charger supervision (D2, D14). The Morse decoder joins the override generating side. The thermal unit may take a duty limit. Section 8.12 routes "HZ-002 re-scoped ... the Morse menu command path in the safety-critical determination" to WP-PDR-16 and 17. The additions of findings 6 and 7 and the `SW-PWR` change go to the same re-run (cross item X-4) | | none |
| swe-080 7.1 task 1 | SC | No | The hardware changes that feed safety-critical units (PA device, synthesizer reference, sensor placement, drive gating, ADC inputs) are not analysed for their software safety impact in findings 1 to 5 and 7 | | finding-1, finding-2, finding-3, finding-5, finding-7 |
| swe-080 7.1 task 2 | | No | Change route of the Record-class TS-012: five commits without `Refs:` (finding-8) | | finding-8 |
| swe-081 7.1 task 2 | SC | Yes | TS-012 and the six analysis records are committed on main. `hazards.json` is row-controlled with the single writer WP-PDR-16b (plan section 5.3) | | none |
| swe-086 7.1 task 1 | | Yes | The study serves RSK-002, RSK-006, RSK-038 and RSK-052 and sends its revision 5 risk rows to the register writer (section 7.1 "Would be entered as"). The SA-F1 assurance risk goes the same way | | none |
| swe-087 7.1 task 2 | | Yes | INSP-110 findings 1 to 18 are Verified with evidence. Findings 19 to 23 are liens with owners. Finding-23 is raised here as finding-3 at Major severity | | none |
| swe-089 7.1 task 1 | | Yes | INSP-110 carries the SWE-089 measurements (front matter and its Measurements sections); this record carries its own | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes | `git rev-parse 37d5824:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>`: `731ba0eb`, equal to INSP-110 `product_files` and `product_blob`. TS-012 history: `5c16930`, `eca24fa`, `d5a3058`, `7d0d450`, `37d5824`; no later commit touches it |
| R2 | Product type and criticality identified | Yes | 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical ... component" (`trade-study-or-adr`). Safety-critical by the 07 section 14.1 rows "Thermal protection", "PA enable and TX sequencer", "Safe-state manager", "Frequency verification unit" and "Menu override command path", the same as INSP-110 |
| R3 | `validate_docs.py` on the product's files; `traceability.py --report-only --output <scratch>` clean for the ids the product touches | Yes | `traceability.py --report-only --output` to the scratchpad: exit 0, "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and 148, not touched by TS-012); `git status docs/vv` clean. `validate_docs.py`: 108 passed, 8 failed; `ts-012-design-to-cost.md` PASS; the 8 failures are records unrelated to TS-012 (the INSP-110 R1 situation) |
| R4 | Paired file review filed under its own invocation; this reviewer is neither author nor file reviewer | Yes | INSP-110 `author_agent` "author:TS-012 ...", `reviewer_agent` reviewer:TS-012-iter1 to iter4; this record `reviewer_agent` "sa-reviewer:TS-012-design-to-cost" |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row 3, safety-critical column Yes; the components of R2 |
| SA-A2 | Yes | Three distinct invocations (author, four file-review invocations, this assurance invocation). INSP-110 names this pair as a separate invocation in `assurance_reviewer_agent` "pending (separate invocation; paired record docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md)" |
| SA-A3 | Yes | Same product, same blob `731ba0eb`, same commit `37d5824` |
| SA-A4 | Yes | INSP-110 applied `peer-review-checklist-risk.md` section B (trade studies, 08 section 3.5). It answered B1 to B10 at four iterations with evidence and tracked 23 findings with state. `swe-088` 7.1 task 1, criteria a to d: checklist used, readiness recorded, findings tracked, measurements recorded |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds every task of the rows `trade-study-or-adr` and "Every product type", plus swe-205 task 1, swe-080 tasks 1 and 2, swe-081 task 2, swe-086 task 1, swe-087 task 2 and swe-089 task 1. `assurance_tasks_applied` lists the 17 Yes and No rows |
| SA-B2 | Yes | The three N/A rows (swe-027, swe-136, swe-070) are conditional tasks whose condition is not met, each with its 07 section. No SC task is N/A |
| SA-B3 | Yes | Each No row cites a finding |

## C. SWE-134 items a to l (trade-study maturity: the recommendation neither precludes nor weakens the 07 section 14.2 provision)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | The hardware clamps are "on at reset" (section 7.3), and TX_KEY and `PA_EN` pull-downs plus the relay's receive default hold RF off before firmware runs. The D-11 gating follows TX_KEY, which is pulled down at reset. The thermal prerequisite starts false. The pre-`PA_EN` frequency check after reset is finding-1 (row h) |
| SA-C-b | Yes | The key-down sequence (relay, settle, drive, ramp; key-up in reverse) is defined in section 7.3 with its times. It adds no mode to the ConOps set |
| SA-C-c | Yes | Every ended or inhibited state has CLK1 off, GVA-84+ unpowered and VGG at 0 V (section 7.3 "RF off"). The first `safe_state()` action, `PA_EN` low, needs the line of finding-3 |
| SA-C-d | No | The ALT-hold key-mode change has no confirmation (finding-6). The 5 W step and the guest lock have two operator events |
| SA-C-e | Yes | The sequence rejects a ramp before the relay settles (10 ms), and the mid-ramp plausibility check catches a late contact (section 7.3). No out-of-sequence command path is added |
| SA-C-f | No | New persisted safety-relevant data (feed-forward tables, stored trim, calibration) are not in the guard's field list (finding-7) |
| SA-C-g | No | A multiplexed ADC path for the thermistor, detector and cells lacks a channel-identity check (finding-4). The counter plausibility of the frequency verification depends on the route of finding-1 |
| SA-C-h | No | The frequency-verified prerequisite before `PA_EN` has no window in the study's sequence and gate (finding-1). The temperature, VBUS and low-voltage prerequisites are not affected |
| SA-C-i | No | The thermistor-failure branch is not bounded by K9 for A4 (finding-2). The two-condition argument has no permit line under D-11 (finding-3) |
| SA-C-j | No | The inhibit setpoint that makes the 100 ms response sufficient is not bounded for A4, and the duty-limit alternative changes the response (finding-5). The 100 ms figures themselves are unaffected |
| SA-C-k | Yes | Sensor, ADC and counter errors still degrade to inhibit in both finalists. The multiplexer fault mode is under row g (finding-4) |
| SA-C-l | Yes | The operator power switch removes power from the rail gates (section 8.10 REQ-SYS-101 row), and `safe_state()` stays reachable from every state; no change from the decision |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | Component-level contributions are in `hazards.json` (task table, swe-205 task 1). SWEHB `swe-205` section 7.7.2 walked. **Control of safety-critical hardware:** gate bias by a feed-forward PWM table (finding-7). **Interlocks:** the REQ-SYS-120 permit (finding-3) and the REQ-SYS-052 key-closed interlock behind REQ-SYS-163 (holds). **Inhibits:** thermal (findings 2, 5), frequency (finding-1), VBUS (unchanged). **Cautions and warnings:** Morse fault announcements within 1 s and LED codes (REQ-SYS-067, section 8.7). **Stored sequences:** the key-down timing (finding-1 part 3). **Common-cause faults:** one ADC select path for three safety readings (finding-4); K2 and K9 at one node for A4 if both sit on the tab (the TS-011 rule 14 common cause, covered there by the via inspection and the TRR key-down test). **Operator disabling of controls:** none in rev A (section 8.7 "the menu never clears a hardware clamp"). The mechanism-level additions go to WP-PDR-16b with findings 3, 5 and 7 |
| SA-D2 | Yes | The components the decision constrains are in 07 section 14.1 with their criteria. The scope changes (charger supervision out of `SW-PWR`; the decoder in the override path; the duty limit) are routed to the PDR re-run by section 8.12 and cross item X-4 |
| SA-D3 | Yes | `traceability.py`: 0 violations, including zero `HAZARD_CONTROL_UNTRACED` and `HAZARD_INVERSE` for the ids TS-012 touches (R3) |
| SA-D4 | N/A | No safety-tagged software requirement is written by this product |
| SA-D5 | N/A | No hazard-tracing software requirement is written by this product |
| SA-D6 | No | The software safety analysis rests on K9 bounding the HZ-003 thermistor branch, K8's two conditions and K7's pre-transmit check. The study changes all three for the recommended A4 and sends no update request for K7 or K8 (findings 1, 2, 3). The thermal note's R-1 to R-3 cover K2 and the K9 location |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-110 findings 1 to 18 Verified at iterations 2 to 4. Finding-19 to 23 are liens with owners. Finding-23 is carried here at Major (finding-3) |
| SA-E2 | Yes | Both records carry the SWE-089 fields |
| SA-E3 | No | Five commits without `Refs:`; one non-05 type (finding-8) |
| SA-E4 | N/A | Test and code rows only |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | One assurance concern that is not a product defect goes to the register writer WP-PDR-18, as a member of RSK-006 (tag `software`) with tag `assurance`: "Given that the safety thresholds and control implementations of the chosen finalist (the REQ-SYS-118 setpoint, the REQ-SYS-181 sensing point, the REQ-SYS-182 counting route and the REQ-SYS-120 permit line) rest on lumped estimates, on analysis records three of which are still under re-review, and on an AFT05 rating not yet read, there is a possibility that the PDR values of the `SW-SAFE` thermal unit, the frequency verification unit and the PA-permit logic are set on a design the built unit does not have, adversely impacting the SWE-134 h, i and j provisions of 07 section 14.2 for HZ-003, HZ-004 and HZ-008, leading to a re-derivation of safety-critical thresholds after CDR and a re-run of TC-SYS-081, TC-SYS-109 and TC-SYS-110." The lead SE forwards it (cross item X-3) |
| SA-F2 | Yes | Front matter: findings by severity and state, `assurance_findings_major` 3, `assurance_findings_minor` 5, `items_no`, effort |
| SA-F3 | Yes | The package "Software assurance findings" section can take from this record: assurance verdict NEEDS CHANGES; three Major and five Minor findings, all Open; 17 tasks applied, 3 N/A with their conditions; SWE-022 relief used |

## Effect on the A4 and A5 choice (assurance side)

A4 over A5 holds from the assurance side. It depends on three conditions, all cheap, and the owner should see them with Q1:
- **finding-1 makes the TCXO a safety condition for A4.** Without AB2, A4 cannot hold REQ-SYS-182 and REQ-SYS-154 as written. With AB2 (and route R3) it can, as A5 can. TS-012 section 6 item 3 scores A4 with the ring and the TCXO (U2 and U3) at 300 against A5's 270: 30 points, over the 25-point rule of 06 section 14.5. The cost is USD 4.15 capped (reviewer arithmetic: planning about 207.48, worst about 270.44 with U3, inside the USD 300 maximum). The alternative is a REQ-SYS-182 and REQ-SYS-154 delta by CR. The gross error that HZ-008 C7 names (150 to 174 MHz) is caught on either route.
- **finding-2 is the one point in A5's favour.** On the sink, K9 bounds A5's channel at about 120 to 123 C against a 175 C rating, and it never acts for A4. For A4 the fix costs nothing (NTC-2 on the tab, TS-011 rule 14), but it only works if the AFT05 junction rating, still unread, exceeds the tab-trip junction of about 130 to 139 C in the adverse case. If the rating were lower, A4 would need a lower REQ-SYS-181 threshold (a value delta, no cost). That does not reverse the choice.
- **finding-3 is common to both.** It costs nothing if the `PA_EN` line gates the VGG or bias clamp. A4 leans on D-11 more (REQ-TX-014). Its fallback, option (b), is a small cost line.

No finding moves a matrix score by itself. Findings 4 to 8 do not discriminate between the finalists.

## Cross items for the lead SE (not findings on TS-012)

- **X-1.** INSP-110 reads `assurance_reviewer_agent: "pending (...)"` and `assurance_verdict: pending`, and it has no `paired_record`. Its reviewer updates it to `paired_record: INSP-118`, names this reviewer and copies `assurance_verdict: NEEDS CHANGES` (07 section 10.2 Record row). The record verdicts then follow rule C1 and the lead SE convention for the branch-only template.
- **X-2.** Owner timing. B1a is proposed for 2026-09-29. Findings 1 and 2 change what Q1 should say: that AB2 is needed for A4 to hold REQ-SYS-182 as written, and that A4's K9 must sit at the tab with the AFT05 rating read. If revision 6 is not issued before B1a, the lead SE puts both in the Q1 presentation, as INSP-110 X-16 does for finding-19 and finding-20. A revision 6 of TS-012 needs a delta iteration of INSP-110 (its fifth pass, rule C1 escalation to the owner, INSP-110 X-14) and iteration 2 of this record.
- **X-3.** The SA-F1 risk request goes to WP-PDR-18, the register's single writer (plan section 5.3).
- **X-4.** The PDR re-run of the safety-critical determination (03 section 4.1 step 5; WP-PDR-16 and 17) should take, beyond the TS-012 section 8.12 items: `SW-PWR` without charger supervision (D2, D14); the Morse decoder units that emit override events (finding-6); the `envelope` and `alc` classification under feed-forward gate-bias authority (finding-7); the frequency verification unit's counting route and second GPIN (finding-1).
- **X-5.** Requests to writers that the findings imply, each routed by the lead SE with the TS-012 revision: WP-PDR-16b (HZ-008 K7 route wording, HZ-004 K8 permit line, HZ-003 C3 firmware path, the A4 values of thermal R-3); WP-PDR-20 (REQ-SYS-182 budget for the chosen finalist); WP-PDR-35 (guarded fields, the Morse row d form, the thermal unit form); WP-PDR-36a (ADC and GPIN allocation with the channel-identity provision); WP-PDR-22 (A4 open-loop case and gate-bias ceiling).
- **X-6.** The frequency-budget note (`79d47fbb`) was written for the TS-007 line-up. Its method carries over, but its numbers assume a TCXO. If A4 without AB2 is chosen, WP-PDR-20 re-runs it at the Si5351 crystal's tolerance.

## Commands

- `git rev-parse 37d5824:<path>`, `git rev-parse HEAD:<path>`, `git hash-object <path>` for TS-012: `731ba0eb` each; `git log --oneline -- <path>`: five commits, the last `37d5824`.
- `.venv/bin/python` JSON reads of `requirements.json` (sys, tx) and `hazards.json` for the ids listed in `input_files`.
- `grep -n -E "PA_EN|permit|TX_KEY"` on TS-012: `TX_KEY` at line 962 (D-11) only; no `PA_EN` or permit.
- Thermal figures: `summary.csv` rows A4-DC and A5-DC (`p_pa_W`, `tj_ss45`, `case_ss45`, `sink_ss45`), `trips.csv` (`hw_sink` nan for A4, 120.16 C for A5-DC), `inhibit.csv` (setpoints 77.1 / 60.0 C A4-DC, 80.9 / 71.7 C A5-DC; adverse A4 dissipation 6.8561 W). Reviewer arithmetic in finding-2 uses the lumped resistances (Tj - 45) / P = 13.98 K/W, (sink - 45) / P = 7.13 K/W, (Tj - case) / P = 4.40 K/W.
- `docs/design/analysis/frequency-budget.md` section 3.3 read for the R1 and R3 formulas; finding-1 arithmetic: 4 000 Hz + 95 ppm x 147.9988 MHz = 18.06 kHz (interval 12), 16.06 kHz (interval 13).
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/traceability-report.md`: exit 0, 0 violations; `docs/vv/` unchanged.
- `.venv/bin/python tools/validate_docs.py`: 108 passed, 8 failed (none TS-012 related). This record's front matter was checked with the same validator's parser and `PEER_REVIEW_RECORD_SCHEMA` on a scratch copy at the record path: PASS.
- `.venv/bin/python tools/check_commit_msg.py --range <c>^..<c>` for the five TS-012 commits: `REFS_MISSING` each; `SUBJECT` for `37d5824`.
- `git grep -n "id: INSP-118"` on main and every `cr/` branch: no match.

## Visual closure

Two figures of the record TS-012 cites for the thermal controls were opened with the Read tool:
- `hardware/sim/thermal/results/2026-09-28-ts012-r2/tj_vs_time_45C.png` (`37d978cc`). The lower right panel labels both A4 sink curves "never reaches 95 C". The A4-DC PA-case NTC reading levels off just under the 95 C line, consistent with finding-2. The A5-DC sink crosses 95 C at 9.6 min (circle marker).
- `hardware/sim/thermal/results/2026-09-28-ts012-r2/inhibit_bound.png` (`e1642788`). The A4-DC panel legend gives setpoints for 110 C of 80.3 / 77.3 / 77.1 / 60.0 C across the four cases. The all-adverse trace saw-tooths to about 132 C at the 85 C setpoint, consistent with finding-5.

## Measurements (SWE-089)

Tasks in the table: 20 (17 applied, 3 N/A). Tasks answered No: 6. Checklist items answered No: 8 (SA-C-d, f, g, h, i, j, SA-D6, SA-E3). SWE-134 items checked: 12. Findings: 3 Major and 5 Minor, all Open (one Major raised in severity from INSP-110 finding-23). Iteration 1. Renders inspected: 2. Effort: 48 turns, about 95 minutes.

## Verdict (returned by the assurance reviewer)

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@731ba0eb at 37d5824; PAIRED RECORD: INSP-110
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
FINDINGS:
- [Major] swe-039 t4, swe-057 t2, SA-C-h: REQ-SYS-182 budget contradicts frequency-budget.md; A4 without TCXO cannot hold 10 kHz (route R1 d about 16 to 18 kHz); no pre-PA_EN window (CLK1 2 ms before ramp) (finding-1).
- [Major] swe-134 t6, SA-C-i: K9 on the sink never acts for A4; thermistor-failure branch unbounded; AFT05 rating unread; M4 pass and D-6 "backstop" unsupported (finding-2).
- [Major] swe-134 t6, SA-C-i: no PA_EN permit line in the design; D-11 makes CLK1 follow TX_KEY; REQ-SYS-120 and HZ-004 K8 not provided (finding-3; INSP-110 finding-23 raised).
- [Minor] swe-134 t4, SA-C-g: at least 8 analog inputs against 3 Pico 2 ADC pins; mux channel identity (finding-4).
- [Minor] SA-C-j: A4 inhibit setpoint 77 to 60 C unbounded until the match run; duty-limit form untraced (finding-5).
- [Minor] SA-C-d: ALT-hold key-mode change without confirmation; decoder in the override path (finding-6).
- [Minor] SA-C-f: feed-forward tables and stored trim not guarded; A4 open loop not assessed (finding-7).
- [Minor] SA-E3: five TS-012 commits without Refs:; type 'ts' (finding-8).
TASKS APPLIED: swe-134 t5, swe-022 t1, swe-033 t1-3, swe-039 t4, swe-057 t2, swe-134 t4, t6, swe-205 t1, t3, swe-080 t1, t2, swe-081 t2, swe-086 t1, swe-087 t2, swe-089 t1
TASKS N/A (relief): swe-027 t1 (07 section 17.1), swe-136 t1 and swe-070 t1 (07 section 17.3); swe-022 standard part (rmm.json SWE-022 T)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l
MEASUREMENTS: size=1 trade study, 9 controls; tasks=20; tasks_no=6; turns=48; minutes=95; major=3; minor=5
```

## Iteration 2: delta verification of finding-1 to finding-3 (Major) on TS-012 revision 6 (2026-09-29, HEAD `123f048`)

**Scope (rule C1).** Iteration 2 is a delta. It verifies the fixes of finding-1, finding-2 and finding-3 (Major) and scans the text that revision 6 changed for defects that revision 6 introduced, under the same assurance lens. finding-4 to finding-8 (Minor) were not addressed by revision 6 (TS-012 table R6-1 names them liens), except for finding-8's own product-side part, so they get a status line only. Owner authorization: `docs/plan/status/status-2026-09-29.md` section 2 ("Yes both recs sound good").

**Product.** `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` revision 6, blob `0c9fcb96`, committed on its own at `3b93de1` (1248 lines; `git diff --stat 37d5824 3b93de1`: 244 insertions, 129 deletions). The blob equals `git rev-parse 3b93de1:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` at HEAD `123f048`. `git log 3b93de1..HEAD -- <path>` is empty; the two later commits (`63122e7`, `123f048`) touch only the receiver analysis and its review record. The product is on `main`. Checklist as iteration 1: `peer-review-checklist-software-assurance.md` revision A, blob `5b135285`, still only on `cr/CR-012-pdr-checklist-templates` (head `7784672`, not an ancestor of `main`).

**Independence (rule C4).** This invocation authored no part of TS-012 revision 6 or of any earlier revision, of the analysis records it cites, of their review records, or of INSP-110. It edited no product file. It changed only this record.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-118 TS-012 design-to-cost software assurance review findings"; "rule C1 reviewer verdict APPROVED when no Major finding open, Minor liens, iteration limit escalation"). `grep`, `sed`, `awk` and short Python reads then only pinned lines in known files (TS-012, `freq_budget.py`, `frequency-budget.md`, `inhibit.csv`, `summary.csv`, `keying-ts012.md`, INSP-110, `validate_docs.py`). The rustos repository was not read. LTspice was not run. Nothing was downloaded: the AFT05MS004N PDF was read from the scratchpad copy whose SHA-256 equals the one TS-012 cites.

### Verification of finding-1 (Major), fix part by part

| Fix part | Revision 6 location | Reviewer check | Result |
|---|---|---|---|
| (1) Budget on the `frequency-budget.md` method, per finalist | Section 7.3 "Revision 6: frequency verification"; section 8.10 row REQ-SYS-182, REQ-SYS-154; D-17 | Counter is FC0 on GPIN0 (not a PWM edge counter), interval 12 (4 ms, 500 Hz at the /8 input) before `PA_EN` and 13 during transmission; XOSC 65 ppm (30 + 30 + 5, Table 596); the rule d < T and T + d <= 10 kHz stated. Re-run of the committed `freq_budget.py` functions (scratch script importing the module unchanged): R3 d = 4 517.996 Hz at interval 12 and 2 517.996 Hz at 13; margin to T = 5.0 kHz 482.004 and 2 482.004 Hz; undetected bound 9 517.996 Hz (12) and 7 517.996 Hz (13), T + d inside 10 kHz; `tx_detection_time(13)` = 46 ms; `fc0_accuracy_ceiling(12)` = 560.25 Hz; plausibility bound 67.5 ppm. R1 with a 30 ppm reference (A4 without the TCXO): d = 18 059.9 Hz (12) and 16 059.9 Hz (13), smallest REQ-SYS-154 limit 31 679.8 and 27 679.8 Hz; R1 with the TCXO: d 11 989.9 Hz and limit 23 609.8 Hz at 13. TS-012's 16.1 / 27.7 kHz and 12.0 / 23.7 kHz are these values rounded up at 0.1 kHz. `freq_budget.py` itself exits 0 | **Verified** |
| (2) TCXO for A4 in the baseline with route R3, or the deltas to the owner; GPIN1 for A5 | D-17; section 4.1 M3 and M4 rows; section 8.1 diagram (GPIN1 from the TCXO buffer, "A4 the same"); Q1 and Q5; follow-on decision 6; E5 (g); section 10 revisit condition "the TCXO becomes unavailable at the gate" | The TCXO is a required A4 item with its cost in the roll-ups (TS-012 row 29, USD 3.61, and the buffer in E5 (g)); AB2 and guard G5 are withdrawn; the R1 deltas are stated with their values and marked not proposed; Q1 no longer offers the TCXO as optional; the A5 diagram now shows the second GPIN | **Verified** |
| (3) Key-down sequence with the check before `PA_EN`, inside the REQ-SYS-161 lead-in, consistent with D-11 | Section 7.3 "Revision 6: key-down sequence, frequency check and PA permit" | t0 + 1 ms (I2C writes and PLL relock allocation) + 4 ms (interval 12) + 2 ms (software) = t0 + 7 ms, then `PA_EN`; `TX_KEY` at t0 + 8 ms; ramp at t0 + 10 ms; 1 + 2 + 10 = 13 ms against REQ-SYS-160's 15 ms; lead-in 10 ms against 12 ms. `changeover_time("A1", 12)` gives 6 ms without the retune, so the 7 ms is that plus the 1 ms allocation. The 1 ms relock allocation has no source (TS-012 says so, table R5-3 carries it as open, section 10 makes it a revisit condition, WP-PDR-32 confirms). Its failure direction is safe: a PLL still settling gives a count outside T or a lock-status fault, so `PA_EN` is not set (a lost element, not RF at a wrong frequency). While CLK1 runs with `PA_EN` low the driver is unpowered and the bias clamped, so the check window emits at most the key-up level (about -67 dBm A4, -61 dBm A5 by the study's estimate), under REQ-SYS-183's -57 dBm, subject to finding-9. The prescaler supply is switched by firmware outside the D-18 gate, so the check can run before `PA_EN` | **Verified** |
| (4) Requests to WP-PDR-20, WP-PDR-35, WP-PDR-16b (K7) | Section 7.3 "Requests"; section 8.12 rows WP-PDR-16, 17 and WP-PDR-35, 41 | WP-PDR-20 (R3 and the TCXO buffer in the clock plan), WP-PDR-35 (threshold 5.0 kHz, ratio refresh and plausibility, DIED as disagreement, lock-status read before `PA_EN`), WP-PDR-36a (two GPIN pins and the `PA_EN` pin), WP-PDR-16b (HZ-008 K7 wording for R3) | **Verified** |

Observation (not a finding): during an over the XOSC/TCXO ratio is the last receive refresh, because the TCXO buffer is off in transmission. At interval 13 the slack left in T + d <= 10 kHz is 2 482 Hz, about 16.8 ppm of XOSC drift at 148 MHz (reviewer arithmetic), against the 1 ppm allocation. A larger drift first erodes the no-false-trip margin, which fails toward Fault-safe. TS-012 routes it to WP-PDR-20 and 32 and makes it a revisit condition.

### Verification of finding-2 (Major), fix part by part

| Fix part | Revision 6 location | Reviewer check | Result |
|---|---|---|---|
| (1) Sensing point and trip junction per finalist | D-6 revision 6; section 8.10 row "REQ-SYS-181 (revision 6)"; section 7.3 "Revision 6: the REQ-SYS-181 cut-off for A4" | A4: NTC-2 on the AFT05 tab copper (TS-011 rule 14), its own comparator (LM393 #1), routed apart from the ADC path; A5: on the sink, channel about 120 to 123 C at the trip against 175 C | **Verified** |
| (2) AFT05MS004N maximum junction rating read; trip junction below it with margin | Section 7.3 (datasheet paragraph and arithmetic); table R5-3 row "REQ-SYS-181 cut-off for A4" | **Datasheet citation checked by the reviewer.** The scratchpad PDF has SHA-256 `84cd9fae494c628310d79f8e7381af8c39769d65fdb79acdaad17466df6dd036`, the hash TS-012 cites (prefix and suffix). Page 1: "Document Number: AFT05MS004N, Rev. 0, 7/2014", Freescale. Page 2, Table 1: operating junction temperature range -40 to +150 C (notes 1 and 2; note 1 is the MTTF sentence TS-012 quotes), case operating temperature -40 to +150 C, 28 W at TC = 25 C derated 0.23 W/C. Table 2: RthJC 4.4 C/W at case 79 C, 4.0 W CW, 7.5 Vdc, IDQ 100 mA, 520 MHz. Page 4, Figure 3: MTTF against TJ, axis 90 to 160 C. Every value TS-012 cites agrees. **Arithmetic** from `inhibit.csv` A4-DC: nominal offset 4.5009 K at 5.5506 W, so 95 + 4.5009 + 5.5506 x 4.4 = 123.92 C; all-adverse row (`a4_rjc=4.84`, offset 10.4355 K, 6.8561 W), so 98 + 10.4355 + 6.8561 x 4.84 = 141.62 C, 8.38 K under 150 C; revisit limit 150 - 98 - 33.18 = 18.8 K. The bound uses only the trip reading, the sensor offset, the dissipation and RthJC, so it holds whatever the case-to-ambient path does, as TS-012 says. The 10.4 K offset comes from the inhibit run's first-off event, a transient with sensor lag; in the thermistor-failure branch the tab heats toward steady state more slowly, so the lag part should be smaller (reviewer judgement, Low). The bench NTC-offset measurement governs through the section 10 revisit condition | **Verified** |
| (3) A4 M4 cell conditional on (1) and (2) | Section 4.1 table, row A4, M4 | "pass on the revision 6 conditions (INSP-118 findings 1 to 3)", naming D-17, D-6 and D-18; the revision 5 pass "is withdrawn" | **Verified** |
| (4) A4 values to thermal R-3, WP-PDR-16b and the REQ-SYS-181 writer | Section 8.10 REQ-SYS-181 row; section 8.12 row WP-PDR-16, 17; follow-on decision 7 | HZ-003 K9 names the A4 sensing point with the 123.9 to 141.6 C trip junction against 150 C; the REQ-SYS-181 wording delta is a follow-on decision | **Verified** |

The common cause of NTC-1 and NTC-2 on the same tab copper is stated with its controls (routing apart, the via-array inspection RSK-006 S5, the TRR key-down test), which is the TS-011 rule 14 argument SA-D1 accepted at iteration 1.

### Verification of finding-3 (Major), fix part by part

| Fix part | Revision 6 location | Reviewer check | Result |
|---|---|---|---|
| (1) A named `PA_EN` line gating, in hardware and independently of TX_KEY, a point that RF needs | Section 7.3 revision 6 (bullets 1 and 2); section 8.10 row REQ-SYS-055, 120, 180, 181, 092; D-18; section 8.1 diagram | `PA_EN` is a GPIO with a 4.7 kohm pull-down, written only by SW-SAFE from its separately maintained PA-permit flag, set only when every 07 section 14.2 prerequisite holds (including the counted agreement) and cleared by `safe_state()`. A 3-input NAND of TX_KEY, `PA_EN` and the monostable Q drives a clamp FET on the VGG or gate-bias node and the gate of the GVA-84+ supply P-FET. Truth table: the output is low (drive powered, clamp released) only with all three high. A stuck-high TX_KEY with `PA_EN` low gives clamp on and driver off; within an over the monostable still ends RF in 7.5 to 13 s and SW-SAFE can clear `PA_EN`. A stuck-high `PA_EN` or a corrupted permit flag still needs TX_KEY. So no single line or flag produces RF, the 07 section 14.2 row i and HZ-004 K8 provision, at trade-study maturity. How the gate's output levels are made is finding-9 | **Verified** |
| (2) Whether the D-11 gating is hardware on TX_KEY or firmware | D-11 revision 6; section 7.3 "D-11 restated" | The GVA-84+ supply following TX_KEY is the D-18 hardware gate; CLK1 enable is a firmware I2C write, a sequencing action, "no longer called the second condition of REQ-SYS-120"; revision 5's wording is withdrawn in section 8.10 | **Verified** |
| (3) REQ-TX-014 restatement with an HZ-004 note, or option (b) as a cost line | Section 8.10 row REQ-SYS-014, 015 (REQ-TX-014 paragraph); follow-on decision 4; section 7.1 risk row (A4 REQ-TX-014 from 12 Red to 6 Yellow) | The proposed text keeps the condition "PA_EN asserted and the synthesizer's transmit output running" with TX_KEY deasserted, so the key-up test is still made with CLK1 on: not a relaxation. The HZ-004 note is sound. TX_KEY low removes both the drive supply and the gate bias in hardware; the `PA_EN` half gates the same two points through the same gate; REQ-TX-014 stays the transmitter half of REQ-SYS-120. Its precondition is that the gate's outputs actually reach their off states (finding-9). Routed to WP-PDR-16 and 17 and to this iteration, as asked | **Verified** |
| (4) D-11 reconciled with the pre-`PA_EN` check | Section 7.3 sequence; section 8.1 diagram lines 20 to 22 | The prescaler's transmit-only supply is switched by firmware at the changeover, outside the gate, so the count runs with the driver unpowered and the bias clamped | **Verified** |

### Minor findings not addressed in revision 6 (status only)

- **finding-4** (ADC count, channel identity): unchanged, lien. Revision 6 adds the GPIN1 pin and the `PA_EN` pin to the WP-PDR-36a request. It also adds firmware-driven lines the pin count must hold (the TCXO buffer supply and the prescaler supply switch), which WP-PDR-36a should count with the same request.
- **finding-5** (A4 inhibit setpoint, duty-limit form): unchanged, lien. D-6 revision 6 moves A4's duty-limit option to the tab NTC; the setpoint is still tied to the WP-PDR-28 bench measurement.
- **finding-6** (ALT-hold confirmation; decoder in the override path): unchanged, lien.
- **finding-7** (feed-forward tables as guarded fields; A4 open loop): unchanged, lien. WP-PDR-22 now also reruns the key-up case with the D-18 gate.
- **finding-8** (commit trailers): the product-side part is done. `3b93de1` uses the 05 type `docs` and carries `Refs: TS-012, INSP-110, INSP-118`; `tools/check_commit_msg.py --range 3b93de1^..3b93de1` prints "PASS 3b93de1: rows 12; Refs: TS-012, INSP-110, INSP-118". The lead SE part (the five earlier commits as RID candidates in the configuration status change log) is not found in `docs/cm` or `docs/plan` by `grep` for the five hashes. Lien, owner the lead SE (cross item X-9).

### New findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-9"></a>finding-9 | assurance (introduced by revision 6) | Minor | SA-C-a, `swe-080 7.1 task 1` | TS-012 D-18; section 7.3 revision 6, bullet "Hardware gate (D-18)" and the interval-13 fallback sentence; section 8.1 diagram ("GVA-84+ (supply P-FET on the NAND output)", "3rd DMP3099L -> TX 5 V"); E5 (g) | **The D-18 gate's logic levels and unpowered state are not stated, and as drawn the P-FET that unpowers the GVA-84+ is not guaranteed to turn off.** The NAND output drives the gate of the GVA-84+ supply P-FET directly (section 8.1). That P-FET's source is on the 5 V TX rail (the DMP3099L of row 23, which E5 (g) prices). TX_KEY and `PA_EN` are 3.3 V RP2350 GPIOs. (a) With the NAND on 3.3 V, its high output leaves the P-FET at VGS of about -1.7 V, which does not guarantee it is off. With the NAND on 5 V, a 3.3 V GPIO does not guarantee an input high for a 5 V-supplied 74LVC part (input high about 0.7 VCC). Neither the DMP3099L threshold nor the 74LVC1G10 thresholds were read (Low); the point is that the study states neither the gate's rail nor a level interface. If the P-FET stays on with TX_KEY low, the revision 5 leakage path returns between elements (A4 about -23 to -19 dBm, keying note section 4.5), and REQ-TX-014 fails again. The HZ-004 note's "-67 dBm" and "driver unpowered" rest on this interface. The clamp FET (an N-channel 2N7002 class, driven high) still holds the gate bias at 0 V, so no RF at power results and the hazard stays controlled. Hence Minor. (b) The permit state of the gate is its output low. An unpowered NAND drives no defined level, so with the NAND rail down (or at brown-out) and the 5 V TX rail up, the clamp and P-FET gates are left to the rest of the circuit. "So the gate bias is held at 0 V at reset" assumes the NAND is powered first (SA-C-a). (c) In the interval-13 fallback (check ends at t0 + 11 ms, ramp at 11.5 ms), `PA_EN` rises after TX_KEY's usual rise at 2 ms before the ramp. The driver then powers up 0.5 ms before the ramp, against 2 ms in the nominal sequence, and the study does not assess this. **Fix:** in D-18, state the gate's supply rail and a level interface that takes the P-FET gate to its source rail and the clamp FET gate to full drive (for example a TTL-input NAND on the 5 V bus, or a level-shifting stage; values from the part's datasheet). Add bias resistors so that an unpowered or floating gate output leaves the clamp on and the P-FET off, and give the power-up order of the NAND rail and the TX 5 V rail. State the fallback's driver power-up time. Route these to WP-PDR-22 (hardware cutoff node; the key-up case with the D-18 gate is already requested) and WP-PDR-16b (HZ-004 K8 names the gate's safe unpowered state). Cost: cents, inside E5 (g) | Open (lien, rule C1; owner the TS-012 author with WP-PDR-22 and WP-PDR-16b; due at the CDR readiness declaration) | Pending | |

No other defect was found in the revision 6 text under the lens: the sections checked were 1 (summary bullets), 4.1 (M3, M4), 7.1 (risk rows REQ-TX-014 and the TCXO), 7.3 (the three revision 6 blocks and tables R5-2 row 2 and R5-3), 8.1, 8.4 (G5 and AB2 withdrawn), 8.10 (REQ-SYS-008 to 010, 182, 154, 014, 015, 055, 120, 181, 112, 118), 8.12, 8.13 (Q1, Q5, follow-on decisions 4, 6 and 7), 8.14 (D-6, D-11, D-17, D-18), 10 (revision 6 revisit conditions) and table R6-1.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State at iteration 2 | Evidence |
|---|---|---|---|
| finding-1 | Major | **Verified** | Section "Verification of finding-1", parts (1) to (4) |
| finding-2 | Major | **Verified** | Section "Verification of finding-2", parts (1) to (4); datasheet read by the reviewer |
| finding-3 | Major | **Verified** | Section "Verification of finding-3", parts (1) to (4); its interface detail is finding-9 |
| finding-4 | Minor | Open, lien | Not addressed in revision 6 (pin request extended) |
| finding-5 | Minor | Open, lien | Not addressed |
| finding-6 | Minor | Open, lien | Not addressed |
| finding-7 | Minor | Open, lien | Not addressed |
| finding-8 | Minor | Open, lien (product part done at `3b93de1`) | Lead SE part open (X-9) |
| finding-9 | Minor | Open, lien (new) | Table above |

Liens (rule C1): finding-4 to finding-9, owner the TS-012 author with the work packages named in each (finding-8: the lead SE), due at the CDR readiness declaration, each closed by a delta of this record on its fix or by an owner deferral.

### Task table and checklist items changed at iteration 2

| Id | Iteration 1 | Iteration 2 | Evidence |
|---|---|---|---|
| swe-039 7.1 task 4 | No | Yes | The REQ-SYS-182 budget now uses the reviewed note and the datasheet values (finding-1); the AFT05 rating is read and checked (finding-2) |
| swe-057 7.1 task 2 | No | Yes | The architecture shows REQ-SYS-182, REQ-SYS-181 (A4 at the tab) and REQ-SYS-120 (`PA_EN`, D-18) met at trade-study maturity |
| swe-134 7.1 task 6 | No | No | Findings 2 and 3 Verified; finding-5 remains (lien) |
| swe-080 7.1 task 1 | No | No | Findings 1 to 3 Verified; findings 5, 7 and 9 remain (liens) |
| SA-C-a | Yes | No | finding-9 (b): the gate's unpowered state is not stated |
| SA-C-h | No | Yes | The frequency prerequisite is known at t0 + 7 ms, before `PA_EN` (finding-1 part 3) |
| SA-C-i | No | Yes | K9 bounds A4's thermistor-failure branch at the tab, 8.4 K under 150 C (finding-2); two independent lines in hardware (finding-3) |
| SA-C-c | Yes | Yes | The first `safe_state()` action, `PA_EN` low, now has its line (D-18) |
| SA-D6 | No | Yes | Requests for HZ-008 K7, HZ-004 K8 and HZ-003 K9 are in section 8.12 (WP-PDR-16b) |
| SA-E3 | No | No | finding-8 lien (lead SE part) |

Other rows and items keep their iteration 1 answers.

### Readiness (iteration 2)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes | Revision 6 committed and frozen at `3b93de1`, blob `0c9fcb96`, equal at HEAD and in the working tree. INSP-110 iteration 3 re-issue 2, committed at `17b6865` while this delta was being filed, names the same blob in `product_files` and `product_blob` |
| R2 | Yes | Unchanged: `trade-study-or-adr`, safety-critical |
| R3 | Yes | `validate_docs.py`: 109 passed, 8 failed, before and after this edit. The 8 are `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md` (PDR) and `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md` (SRR), none related to TS-012. `traceability.py --report-only --output <scratchpad>`: exit 0, "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and 148) |
| R4 | Yes | Unchanged: separate invocation from the author and the INSP-110 reviewers |

### Effect on the A4 and A5 choice (iteration 2, assurance side)

Revision 6 lands where iteration 1 said it would. The recommended A4 with the TCXO and the ring scores 300 against A5's 270, 30 points, and both finalists now carry the same frequency check (route R3) and the same permit gate (D-18). The one assurance difference left is the REQ-SYS-181 margin to the device rating at the all-adverse corner: about 8 K for A4, about 52 K for A5. Q1 shows it to the owner, with the bench NTC-offset measurement as the revisit condition. A4 over A5 holds from the assurance side. A2 (305, not analysed) is presented in Q1 as finding-19 of INSP-110 asked. From the assurance side, A2 would bring the Catastrophic HZ-002 charger chain into the box, and none of the six safety-relevant analyses covers it. Its safety controls are therefore not shown, which supports keeping it out of the choice set unless its analysis is run. The robustness verdict itself belongs to INSP-110.

### Cross items (iteration 2, returned to Claude as lead SE)

- **X-1 (in part).** INSP-110 at `17b6865` now carries `paired_record: INSP-118` and names this reviewer in `assurance_reviewer_agent`. It still reads `assurance_verdict: NEEDS CHANGES`, the iteration 1 value; it takes `APPROVED` from this iteration 2 (`dd39a64` and the follow-up commit).
- **X-7 (closed).** INSP-110's delta on revision 6 (iteration 3 re-issue 2, `17b6865`) names blob `0c9fcb96`, so readiness R1's equality holds for the pair. Once X-1 is complete and CR-012 merges with template blob `5b135285` unchanged, the software lead can set this record's `verdict` to APPROVED.
- **X-11.** This delta's first commit `dd39a64` uses the subject type `review`, which is not a 05 section 4.5 type: `check_commit_msg.py --range dd39a64^..dd39a64` reports `SUBJECT` (its `Refs:` trailer passes). Another agent's commit (`17b6865`) already sits on top of it, so history is not rewritten. The follow-up commit that records this uses `docs`. The lead SE lists `dd39a64` with the finding-8 commits (X-9); `123f048` and `17b6865` use the same type.
- **X-8.** finding-9's requests go to WP-PDR-22 and WP-PDR-16b together with the D-18 requests of section 8.12.
- **X-9.** finding-8's lead SE part: list `5c16930`, `eca24fa`, `d5a3058`, `7d0d450` and `37d5824` in the configuration status change log as PDR RID candidates.
- **X-10.** TS-012 cites the AFT05MS004N datasheet by hash only, from a web-fetch cache. The copy this review read sits in a session scratchpad. Record the source URL and the hash in the reference corpus index (`docs/references/`), so that a later review can re-read the same file without the scratchpad.

### Commands (iteration 2)

- `git rev-parse 3b93de1:<path>`, `git rev-parse HEAD:<path>`, `git hash-object <path>` for TS-012: `0c9fcb96` each. `git log --oneline 37d5824..3b93de1 -- <path>`: `3b93de1` only. `git log 3b93de1..HEAD -- <path>`: empty.
- `git diff --word-diff=plain 37d5824 3b93de1 -- <path>` to a scratchpad file, and `sed -n` over the TS-012 sections listed above.
- Scratch script importing `hardware/sim/freq/freq_budget.py` unchanged: `healthy_disagreement`, `undetected_bound`, `min_154_limit` for R1 and R3 at intervals 12 and 13, and the R1 case with a 30 ppm reference computed from the same terms; `tx_detection_time(13)`, `fc0_accuracy_ceiling(12)`, `TCXO_PLAUS_PPM`, `changeover_time("A1", 12)`. Values in the finding-1 table. `.venv/bin/python hardware/sim/freq/freq_budget.py`: exit 0.
- `shasum -a 256` on the scratchpad copy of the AFT05MS004N PDF: `84cd9fae...6dd036`. `pdftotext -layout -f 1 -l 4` for Tables 1 and 2, note 1 and Figure 3.
- `grep "A4-DC"` on `inhibit.csv` and `summary.csv` for the offsets, dissipations, `a4_rjc` and the steady junction; the arithmetic in the finding-2 table.
- `.venv/bin/python tools/check_commit_msg.py --range 3b93de1^..3b93de1`: PASS. `grep` for the five iteration 1 hashes in `docs/cm` and `docs/plan`: only CR-012 listing references, no configuration status entry.
- `git merge-base --is-ancestor 7784672 main`: false. `git rev-parse cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md`: `5b135285`.
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/trace-insp118-it2.md`: exit 0, 0 violations. `.venv/bin/python tools/validate_docs.py`: 109 passed, 8 failed, before and after the edit; this record PASS.

### Visual closure (iteration 2)

No figure changed between revisions 5 and 6 of the records this delta relies on (the thermal run `2026-09-28-ts012-r2` and the frequency-budget note are unchanged). The two figures inspected at iteration 1 still apply. The finding-2 arithmetic was checked against the CSV values behind them, not against a new render.

### Measurements (iteration 2)

Delta scope: 3 Major findings, 14 fix parts checked (4 + 4 + 4, plus the finding-3 part (4) sequence reconciliation and the D-6 common cause). Datasheet values checked: 7. Budget values recomputed: 18. Findings: 3 Major Verified; 5 Minor liens unchanged; 1 new Minor (finding-9). Checklist and task rows re-answered: 10 (5 to Yes, 1 to No, 4 unchanged with new evidence). Effort for iteration 2: 32 turns, about 70 minutes (cumulative 80 turns, 165 minutes).

### Verdict (iteration 2)

```
ASSURANCE VERDICT: APPROVED (iteration 2; record verdict held, see front matter)
PRODUCT: docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@0c9fcb96 at 3b93de1 (revision 6); PAIRED RECORD: INSP-110
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
FINDINGS:
- [Major] finding-1 Verified: route R3 for both finalists, T 5.0 kHz, d 4518 Hz, margin 482 Hz (re-run); TCXO required in A4 (D-17); check done at t0 + 7 ms before PA_EN; 1 ms relock allocation open, fails safe.
- [Major] finding-2 Verified: AFT05MS004N Rev. 0 page 2 TJ max 150 C and Table 2 RthJC 4.4 C/W read by the reviewer; NTC-2 on the A4 tab trips at 123.9 C nominal, 141.6 C all-adverse (8.4 K margin); M4-A4 conditional; revisit on the bench NTC offset (18.8 K).
- [Major] finding-3 Verified: PA_EN from SW-SAFE only; NAND(TX_KEY, PA_EN, Q) clamps the bias and unpowers the GVA-84+ (D-18); D-11 restated; REQ-TX-014 restatement with a sound HZ-004 note.
- [Minor] finding-4 to finding-8: liens (finding-8 product part done at 3b93de1).
- [Minor, new] finding-9: D-18 gate rail, level interface to the 5 V P-FET and unpowered state not stated; the interval-13 fallback powers the driver 0.5 ms before the ramp (lien; WP-PDR-22, WP-PDR-16b).
TASKS APPLIED: as iteration 1 (17); No at iteration 2: swe-134 t4, t6, swe-080 t1, t2 (liens)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l
MEASUREMENTS: iteration 2 turns=32; minutes=70; major=3 (verified 3); minor=6 (liens 6)
```
