---
id: INSP-007
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/SRR/checklists/risk-register-06.md
product: docs/risk/register.json
# product_commit: the WP-PDR-18 Track pass commit at iteration 3 re-issue 3 (finding-18 delta, 2026-09-27); re-issue 2 baseline was ebe5873; re-issue 1 baseline was adcfe09; iteration 1 and 2 base commit was 28e49e6
product_commit: "4df6606ec6f32c1865a9d3e695c2629e1100e58d"
# product_files: committed blobs reviewed at iteration 3 re-issue 3 (git rev-parse 4df6606:<path>, identical at HEAD 5dc09ba, 2026-09-27; 06 unchanged);
# iteration 3 re-issue 2 blobs (ebe5873): register.json 0c25c0c5, register.md a3a983e5, 06 7a92d21f;
# iteration 3 re-issue 1 blobs (adcfe09): register.json 57f64995, register.md 77b864a0, 06 7a92d21f;
# iteration 2 working-tree blobs: register.json 2903601e, register.md 761f3731, 06 7a92d21f (06 unchanged)
product_files: ["docs/risk/register.json@6685aa0eadc9e8bd806f1920e20d2209e8ae130e", "docs/risk/register.md@f8c28b363035cc3ce4cb15a5f7c0056f95febbf7", "docs/process/06-risk-and-decision-analysis.md@7a92d21f24a1733d70ae083576e708274bfd1a6d"]
product_size: 65 active risks and 159 candidates; plan 06 (17 sections) (iteration 1: 59 and 130)
sprint: SRR-prep
author_agent: "author:risk-manager (Claude main session, lead SE and risk manager; register 0.5.1-pre-srr, SRR readiness items H9 and F6)"
reviewer_agent: "reviewer:risk"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
# finding-17 is new at iteration 3, finding-18 at iteration 3 re-issue 2 and Fixed at re-issue 3; findings_deferred counts the two remaining liens (finding-16, finding-17: Lien, fix before PDR)
findings_major: 4
findings_minor: 14
findings_open: 0
findings_fixed: 16
findings_verified: 0
findings_deferred: 2
deferred_rids: []
# iteration 3 re-issue 3 answers (re-issue 2: CK-RSK-A2, CK-REQ-G1; re-issue 1: CK-REQ-G1; iteration 2: CK-RSK-A10, CK-REQ-G1; iteration 1: CK-RSK-A1, A2, A3, A4, A7, A8, A10, A11, CK-REQ-G1, G2, G4, G6)
items_no: [CK-REQ-G1]
effort_turns: 124
effort_minutes: 180
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-007: risk register and Risk Management Plan (06)

**Products reviewed (working tree of 2026-09-25, identified by git blob hash):**

| File | Blob (`git hash-object`) | Base commit | State |
|---|---|---|---|
| `docs/risk/register.json` (version 0.5.1-pre-srr) | `2fd2377b6b4ccffccbabc13ed5221aa2ef66b7e4` | `28e49e6` (blob there `69c6357b`) | modified, uncommitted |
| `docs/risk/register.md` (rendered) | `b29463877cf213edc88c63b421544df3045be4ba` | `28e49e6` | modified, uncommitted; `render_risk.py --check` reports it current |
| `docs/process/06-risk-and-decision-analysis.md` | `9dd468853c94cf51805176aa6a8bfbc412d35952` | `4e3f891` (identical blob) | committed |

`product_commit` names the base commit; the reviewed register content is the blob above (package item H17: the products are not yet committed).

**Checklists applied.** `docs/templates/peer-review-checklist-risk.md` revision A section A (CK-RSK-A1 to A11, the register items of 06 section 16), and for the plan document 06 the plan items of `docs/templates/peer-review-checklist-requirements.md` revision C section G (CK-REQ-G1 to G8), which 08 section 3.1 names for "plans and process documents". Section B (trade study) is N/A. **Minimum content judged:** the Risk Management Plan and register (06) and SRR entrance row 11 (`docs/process/01-lifecycle-and-reviews.md` section 4.3: "Risk management approach ready to baseline; risk assessment with mitigations", NPR 7123.1D App. G Table G-4 items 6.4 and 6.5, Table G-3 item 5.5) together with success row 6 (G-4 s6) and the 06 Table 10-1 SRR rows.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: register record checklist and plan items; 07 section 22 RSK-009 closure evidence; cargo-llvm-cov TV schedule; SE-19 and NPR 8000.4; SWE-086 and SWE-154). `grep -n` and read-only Python over the JSON were used afterwards only to pin the lines the hits pointed at.

**Independence.** The reviewer did not author any register entry, the render, or 06, and edited none of them.

## Findings

Severity: Major blocks the baseline; Minor is fixed before the next review. State at iteration 1 was Open for all; at iteration 2 a closed finding is set to Fixed (Verified and `record_status: Closed` are set by the software lead) and the Disposition column gives the reviewer's evidence. The Owner ruling column is filled at the review (01 section 10.1).

| Finding | Severity | Item | Location | Description and expected fix | State | Disposition (iteration 2, 2026-09-25) | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>F-01 (finding-1) | Major | CK-RSK-A1, CK-RSK-A7 | `docs/safety/hazards.json` HZ-015 `related_risk_ids` (outside the product) | The mandatory package check `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exits 1: `ERROR: HZ-015: related_risk_ids does not name RSK-034, which carries it (hazard link rule back-link)`. The register side is correct (RSK-034 `related.hazard_ids` = [HZ-015], safety 5 = Catastrophic). 06 section 12 makes this command mandatory from the SRR readiness declaration. Fix (hazard analysis author): set HZ-015 `related_risk_ids` to [RSK-034], then re-run the command to exit 0. | Fixed | Closed (author dispute accepted as to ownership: the fix belongs to the hazard analysis author and is applied). `docs/safety/hazards.json` (blob `98ee9d16`) HZ-015 `related_risk_ids` = [RSK-034]; `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0 ("hazard cross-check"). | | |
| <a id="finding-2"></a>F-02 (finding-2) | Major | CK-RSK-A4, CK-RSK-A2 | `likelihood`, `likelihood_rationale` of RSK-007, RSK-025, RSK-039, RSK-040, RSK-041, RSK-043, RSK-045, RSK-046, RSK-048, RSK-052 | The recorded level disagrees with the 06 section 6 anchor that the rationale itself describes, and no probability-band argument is given in its place. Level 4 anchor "No analysis yet": RSK-007 ("the design does not exist yet", recorded 2, confidence Low so the anchor decides), RSK-025 ("no load analysis exists", recorded 3), RSK-039 ("short-circuit and cross-plug cases have no analysis"), RSK-040 ("has no analysis yet"), RSK-041 ("no driver has been designed yet"), RSK-043 ("no tolerance analysis or fit-check exists yet"), RSK-048 ("No isolation or fault-case analysis exists yet"), RSK-052 ("No quote exists"), each recorded 3. Level 3 anchor "margin below 2x": RSK-045 recorded 2 with a computed 26 dB bandwidth of 226 to 292 Hz against 350 Hz (`docs/research/regulatory-corpus-and-operators.md` line 194, F7), a margin of 1.2x to 1.5x, with the PA not selected. Family worst member (06 section 4): RSK-046 recorded 2 "for the edge cases" while its rationale says "the software fault path is unverified" (hazard-analysis section 8.2 row 4). At the anchor levels the scores become RSK-007 20, RSK-025 16, RSK-039 12, RSK-040 12, RSK-043 12, RSK-048 12, RSK-052 12, RSK-041 8, RSK-045 12, RSK-046 12 (at least): seven risks move from Yellow to Red, which changes the Red list the owner is asked to approve (package decision 14, "24 Red risks") and the 06 section 8 minimums they must meet. Fix: re-level each to its anchor with a history entry, or record the band argument and evidence that justifies the lower level (06 section 6 "the anchor decides when the band is uncertain"), with `assessment_confidence` set accordingly; re-render and update package section 11. | Fixed | Closed. All ten re-levelled with a dated SRR `history` entry citing this finding: RSK-007 4 (20, confidence Low), RSK-025 4 (16), RSK-039 4 (12), RSK-040 4 (12), RSK-041 4 (8), RSK-043 4 (12), RSK-045 3 (12), RSK-046 4 at its worst member (16), RSK-048 4 (12), RSK-052 4 (12); each rationale names 06 section 6 case (a). Scripted check over all 65: every case (a) rationale's anchor equals the recorded level and none claims anchor 1 or 2. Red count now 32 (register.md SRR measures row); the package side is F-09. | | |
| <a id="finding-3"></a>F-03 (finding-3) | Major | CK-RSK-A11, CK-RSK-A10 | Register population against `docs/process/07-software-engineering-plan.md` sections 16.2 and 21; `docs/decisions/adr/ADR-011*.md` section 4.4; 06 section 15 SWE-154 row | Not all software risks of 07 are in the register (SWE-086 "all of the software risks"; SWE-154 3.11.3). 07 section 16.2 lists six asset rows and says "Residual risks are entries in `docs/risk/register.json` tagged `cyber`", but only RSK-015 (image and configuration) and RSK-022 (debug access) exist: the rows "Keying and control inputs" command injection (L1, C4; this surface is in the tailored SWE-154 scope of charter section 12, "command injection via the key input"), "Diagnostic interface" (L1, C2) and "Build and supply chain" (L1, C4) have no entry and no candidate disposition. 07 section 21 row "Host mock diverges from silicon (proposed by ADR-011 section 4.4)" and ADR-011 section 4.4 ("new risk proposed: host mock diverges from silicon behaviour") have neither a risk nor a candidate disposition, although HostUnit is the primary software evidence (charter section 9). Fix: open the four risks (tag `software`, and `cyber` for the three 16.2 rows) or record Merged or Declined candidate dispositions with rationale, and correct the 06 section 15 SWE-154 row and the section 17 "All seven rows" row. | Fixed | Closed. RSK-060 (keying and control inputs, tag `cyber`), RSK-061 (diagnostic interface, `cyber`), RSK-062 (build and supply chain, `cyber`), RSK-063 (host mock diverges from silicon, category software, Red 12 with three active steps) opened with sources naming 07 sections 16.2 and 21 and ADR-011 section 4.4; candidates SEP16-IMG to SEP16-SUPPLY, SEP21-MCDC to SEP21-MAINT and ADR011-R1 all Entered against existing risks (tool check). 06 section 15 SWE-154 row and section 17 07-section-21 row corrected (nine rows, all registered). | | |
| <a id="finding-4"></a>F-04 (finding-4) | Major | CK-RSK-A3 (plan part of section 9), register consistency | `mitigation.steps[].artifact` of RSK-001 S1 and S7, RSK-024 S6, RSK-027 S1 and S5, RSK-035 S1, RSK-036 S1, RSK-037 S2, RSK-041 S1, RSK-045 S1, RSK-046 S2, RSK-047 S1, RSK-055 S1, RSK-058 S2 | Step artifacts name trade-study ids that now identify other products or conflict with each other: `TS-001-cw-selectivity.md` and `TS-002-synthesizer.md`, while `docs/decisions/trade-studies/` (untracked, 2026-09-25) holds `TS-001-receiver-and-pa-concept.md` (covering receiver, CW selectivity and PA device) and `TS-002-firmware-runtime-make-buy.md`; RSK-001 S1 names `TS-NNN-pa-device.md` and S7 names `TS-003-pa-device.md` for the same study, which TS-001 sub-decision P now covers. Charter section 6: ids are never reused. Also TS-001 lists 13 related risks and TS-002 seven, none of which carries a `related.trade_study_ids` entry (06 sections 13 item 3 and 14.2 require the link at decision; state it now or say it follows the decision). Fix: re-point the selectivity and PA-device steps to TS-001-receiver-and-pa-concept, replace the pre-assigned numbers of unwritten studies (synthesizer, ALC envelope, USB input) with `TS-NNN` until created, or have the TS author renumber; agree which side changes with Claude (cross). | Fixed | Closed. No `TS-001-cw-selectivity`, `TS-002-synthesizer`, `TS-003` or `TS-NNN-pa-device` string remains in `register.json`; selectivity and PA-device steps point to `TS-001-receiver-and-pa-concept.md` (sub-decisions P and R2); unwritten studies are `TS-NNN-<slug>` "number assigned at creation"; `related.trade_study_ids` equals the "Related risks" rows of TS-001 (13 risks) and TS-002 (7 risks) exactly. 06 section 13 item 3 now states the rule. One `TS-005` remains in RSK-055 `history[1]` (append-only, historic; accepted). | | |
| <a id="finding-5"></a>F-05 (finding-5) | Minor | CK-RSK-A8 | RSK-008 `related.risk_ids` and first trigger | The aggregate's child list omits RSK-025, whose driving dimension is first_power_on 4 ("PCB damage at the connector stops the TX function and the owner cannot rework it", a second spin by the 06 section 7 scale). The first trigger names 9 of the 11 listed children (omits RSK-043 and RSK-049). Likelihood is unaffected (RSK-025 is 3, or 4 under F-02, equal to the aggregate's 4). Fix: add RSK-025 as a child with a history note; make the trigger say "any child risk in `related.risk_ids`". | Fixed | Closed. RSK-008 `related.risk_ids` now 13 children including RSK-025 (and new RSK-064); first trigger reads "Any child risk named in related.risk_ids is Red at CDR"; likelihood 4 equals the child maximum (script). | | |
| <a id="finding-6"></a>F-06 (finding-6) | Minor | CK-RSK-A3 | `statement.condition` of RSK-009, RSK-013, RSK-023 | The condition must be a fact true today (06 section 4). RSK-009 still says the scrape "has not been checked page by page for completeness of the guidance, small-project and software-assurance sections", which the S1 check (Done; reproduced by the reviewer: 100 of 100 RMM rows pass, smallest sections 6056, 3283 and 6407 non-space characters, exact match) now contradicts; the remaining gap is content fidelity (S2). RSK-013 ("twelve rustos driver work packages (WP-SW-01 to WP-SW-12, 07 section 19)") and RSK-023 ("the twelve driver work packages of 07 section 19") disagree with 07 section 19, which has WP-SW-01 to WP-SW-13, with 07 section 21 ("Thirteen work packages") and with RSK-013's own S1 evidence (WP-SW-01 to WP-SW-13). Fix: restate the three conditions. | Fixed | Closed. RSK-009 condition records the S1 structural check as done and reproduced by INSP-007, and names the remaining content-fidelity gap (S2); RSK-013 and RSK-023 now say thirteen work packages (WP-SW-01 to WP-SW-13, WP-SW-13 optional), matching 07 section 19. | | |
| <a id="finding-7"></a>F-07 (finding-7) | Minor | CK-RSK-A5 (band minimums, Green row), CK-RSK-A10 | RSK-030 `mitigation.strategy` and S1; package section 13.1 decision 32 | RSK-030 has strategy Accept while Proposed and without an acceptance record; the schema description reads "Accept = owner accepts residual (needs acceptance...)" and the 06 section 8 Green row calls for Watch with closure criteria. S1 schedules the acceptance "with the RF Exposure Evaluation approval at PDR", while package decision 32 and package section 11 ask the owner to accept RSK-030 in the SRR memo. Fix: set Watch (or keep Accept and state the rule in 06, F-11) and align the acceptance gate with decision 32. | Fixed | Closed. RSK-030 keeps *Accept*, which the new 06 section 8 strategy table now allows for Yellow and Green with a step due at the named gate whose artifact is the decision memo; S1 is due SRR, artifact `docs/reviews/SRR/decision-memo.md`, and names package decision 32, so the gate agrees with the package. | | |
| <a id="finding-8"></a>F-08 (finding-8) | Minor | CK-RSK-A7, CK-RSK-A3 | RSK-046 `related.hazard_ids`; `docs/safety/hazards.json` HZ-008 `related_risk_ids` | RSK-046's condition and source name the HZ-008 C7 out-of-band fundamental cause (hazard-analysis section 12 row HZ-008 action), and it scores safety 4, but `related.hazard_ids` is empty "until the hazard analysis author adds RSK-046" (last history entry). The tool passes only because the link is absent on both sides. Fix in one pass with the hazard analysis author: RSK-046 `hazard_ids` [HZ-008] and HZ-008 `related_risk_ids` adds RSK-046; the optional HZ-006 link for RSK-028 is decided in the same pass. | Fixed | Closed. RSK-046 `related.hazard_ids` = [HZ-008] with history note; `hazards.json` HZ-008 `related_risk_ids` = [RSK-001, RSK-011, RSK-046]; safety 4 meets Critical; `--hazards` check exit 0. RSK-028 not linked to HZ-006, decided in RSK-028 history (RSK-016 carries HZ-006). | | |
| <a id="finding-9"></a>F-09 (finding-9) | Minor | CK-RSK-A10 | `docs/reviews/SRR/package.md` section 11 and section 13.1 decision 14 (outside the product); 07 section 22 row "RSK-009 closure evidence" | The package risk section no longer matches the register history: it says "7 open steps due at SRR" and lists RSK-009 S1, RSK-010 S1, RSK-013 S1 and RSK-016 S3 as open, while the register measures table gives 3 (RSK-012 S5, RSK-028 S2, RSK-046 S1) after S1 Done (RSK-009, RSK-013), S3 Done (RSK-016) and S1 re-planned to PDR (RSK-010). Decision 14 recommends "close RSK-009 on the recorded check", and 07 section 22 says "the owner closes RSK-009 at SRR", while the register records that closure criteria are not met (S2 due PDR). Fix (package author, 07 author): refresh section 11 from the register; reword decision 14 to approve the Red plans only (with the F-02 Red list) and keep RSK-009 open to PDR. | Fixed | Iteration 3: Closed (`package.md` blob `9042d945` lines 436 and 764, `07` blob `d0f8baf6` line 866). Iteration 2: Open (author dispute not accepted: it concerns ownership, not substance, and the defect persists). Register side done (RSK-009 open to PDR, S2 to S4 due PDR). `docs/reviews/SRR/package.md` line 348 still says "7 open steps due at SRR" and SRR 59 active, Red 24 (register.md SRR row now 65 active, Red 32, Yellow 25, Green 8, 4 open steps due); line 447 still lists RSK-009 S1, RSK-010 S1, RSK-013 S1, RSK-016 S3 as open; line 620 decision 14 still asks to approve "24 Red" plans and "close RSK-009"; 07 line 820 still says "the owner closes RSK-009 at SRR". Owners: package author and 07 author (cross). | | |
| <a id="finding-10"></a>F-10 (finding-10) | Minor | CK-REQ-G1 | 06 section 17 rows "268 pages scraped", "Software risks opened ... at SRR", "Hazard related_risk_ids back-links" | Alignment rows are stale: charter section 1 now reads "scraped 2026-09-25: 267 files, 130 of them SWE pages" (the row still reports a 268 charter issue); 07 section 21 now has nine rows, including RSK-015 and the unregistered host-mock row (the row says "All seven rows are in the register. No difference"); the back-link actions listed are done except HZ-015 (F-01). Fix: update the three rows with the date and the evidence. | Fixed | Closed. 06 section 17 rows updated 2026-09-25: 07 section 21 nine rows all registered; SWEHB count row matches charter section 1 ("267 files, 130 of them SWE pages") and records the remaining 08 section 1 "268 pages scraped" difference (confirmed at 08 line 30) as an action; back-link row lists HZ-015 done. The hazard row has since gone stale on one clause, recorded as F-16. | | |
| <a id="finding-11"></a>F-11 (finding-11) | Minor | CK-REQ-G2 | 06 sections 8 and 9 (Plan step "Choose strategy") | The five strategy values Mitigate, Watch, Accept, Research and Elevate are defined only in the `docs/risk/schema.json` description, not in the plan; 06 gives no rule for choosing Accept before the owner's acceptance, or Elevate. Fix: add a strategy table to section 8 or 9 (definition, band where allowed, what it requires). | Fixed | Closed. 06 section 8 "Strategies" table defines Mitigate, Research, Elevate, Watch and Accept with bands allowed and what each requires, including Accept before the owner's ruling and Elevate; Yellow and Green rows reference it; section 9 Plan step points to it. | | |
| <a id="finding-12"></a>F-12 (finding-12) | Minor | CK-REQ-G2, CK-RSK-A4 | 06 section 6; `likelihood_rationale` of RSK-015, RSK-020, RSK-022, RSK-030, RSK-042, RSK-054, RSK-057 | Anchor 1 needs a Test on the delivered unit or heritage with two analyses; anchor 2 needs analysis "performed with a validated tool (SWE-136)". No TV record exists (`docs/cm/` absent; package H12), so no risk meets anchor 1 or 2 at SRR, and 06 does not say how a procedural, threat or programmatic risk is anchored (RSK-034's rationale notes "No design-analysis anchor applies"). The seven risks listed claim "Anchor level 1" or "Anchor level 2" without that evidence (for example RSK-022: "recorded on that assessment until S1 is verified"). Fix: in 06 section 6, state that before the anchors are reachable the level rests on the probability band with named evidence and a stated confidence; restate the seven rationales on that basis or re-level them. | Fixed | Closed. 06 section 6 "Anchor availability and the band argument" states that anchors 1 and 2 are unreachable on 2026-09-25 and defines cases (a), (b), (c) with level and confidence rules; section 16 item 4 updated. RSK-015, 020, 022, 042, 057 restated as case (c), RSK-030 as case (b) (anchor 2 explicitly not claimed), RSK-054 as case (a) at 3; scripted check: no rationale over the 65 claims anchor 1 or 2, every rationale names an anchor or a band case. | | |
| <a id="finding-13"></a>F-13 (finding-13) | Minor | CK-REQ-G2 | 06 section 9, candidate disposition rule and its Status sentence | The listed candidate sources (ConOps section 8, research risk lists, hazard analysis linkage table, minutes, RFA answers) omit the "Risks opened, closed or re-scored" field of ADRs and the risk tables of plan documents (07 sections 16.2 and 21), which is how the F-03 candidates were missed. Fix: add ADRs, trade studies and plan risk tables to the source list and to the pre-readiness pass. | Fixed | Closed. 06 section 9 candidate rule now lists ADR section 4.4 fields, trade-study "Related risks" rows, 07 sections 16.2 and 21, technology assessment section 7 and plan risk-opening rules; Status records the plan-table pass (15 candidates) and ADR pass (14 candidates); the remaining SEMP and 01 to 05 pass is scheduled before the readiness declaration. | | |
| <a id="finding-14"></a>F-14 (finding-14) | Minor | CK-REQ-G6 | 06 section 12, measures table | The per-review measures (active by band, opened, closed, accepted, open steps due, overdue) have a source (history) and storage (`register.md`, package figures) but no threshold or analysis rule (for example: any overdue step at a gate becomes a RID; a rising Red count between gates is reported with its cause). Fix: add a threshold and response for each measure. | Fixed | Closed. 06 section 12 "Measure thresholds and responses" gives a threshold and a response for overdue steps, steps due at the gate, Red count rise, Red at CDR, late-opened risks, closures and acceptances. | | |
| <a id="finding-15"></a>F-15 (finding-15) | Minor | CK-REQ-G4 | 06 section 15, rows SWE-154 and SWE-086 | 06 relies on SWE-154, which `docs/process/rmm.json` dispositions T (Tailored: "firmware image tampering, malformed configuration data, debug port access"), but 06 does not mirror the disposition or its scope; the charter section 12 tailoring also names "command injection via the key input", which neither the RMM row nor the register covers (see F-03). Fix: state the RMM disposition of SWE-154 (T) and SWE-086 (FC) in the 06 section 15 rows and align the scope with charter section 12. | Fixed | Closed. 06 section 15 rows state SWE-086 FC and SWE-154 T with the tailoring scope, including charter section 12 "command injection via the key input" (RMM rows confirmed: SWE-086 FC, SWE-154 T). The RMM SWE-154 implementation text still lists three surfaces only; 06 records it as a cross item to the RMM author (outside this product). | | |
| <a id="finding-16"></a>F-16 (finding-16) | Minor | CK-REQ-G1 | 06 section 17 row "Hazard `related_risk_ids` back-links" (new at iteration 2) | The row says the hazard analysis author "adds RSK-046 to HZ-008 `related_risk_ids`; until then `render_risk.py --check --gate SRR --hazards` exits 1 on that back-link only". HZ-008 now carries RSK-046 and the command exits 0 (Tool runs, iteration 2), so the listed action is done and the row reports a failure that no longer occurs. Fix: restate the row as resolved with the date and the exit code. | Lien | Iteration 3: Lien: fix before PDR (06 blob `7a92d21f` unchanged; line 423 still reports the exit 1). Iteration 2: new. | | PDR |
| <a id="finding-17"></a>F-17 (finding-17) | Minor | CK-REQ-G1, CK-REQ-G4 | 06 section 15 row SWE-154 (line 371); section 17 rows "Cyber risks of the 07 section 16.2 assessment" (line 420) and "SWEHB page count" (line 422) (new at iteration 3) | The rows report two cross-item actions as still open that are done at HEAD `adcfe09`: the RMM SWE-154 implementation text "names the first three surfaces only" (lines 371, 420), while `docs/process/rmm.json` SWE-154 `implementation` now names RSK-015, RSK-022, RSK-060, RSK-061 and RSK-062; and "the 08 section 1 repo map still says 268 pages scraped" (line 422), while `08-agent-briefing.md` line 30 reads "267 files, 130 of them SWE pages". Fix: restate the three rows as resolved with the date and the evidence. | Lien | Iteration 3: Lien: fix before PDR (new). | | PDR |

### Risks passing the Analyze check (section A only)

Checked against 06 sections 4 to 8 (statement parts and family rule, category, likelihood anchor, five consequence levels and the driving dimension, score and band, section 8 minimums for the band, the Low-confidence rule). "Yes" with a finding id means the Analyze content passes and the finding concerns a step artifact only. Families admitted by the section 4 rule on this check (recorded here as the first check): RSK-001, RSK-015, RSK-022, RSK-025, RSK-034 (three safety members), RSK-037, RSK-044, RSK-045, RSK-049, RSK-056; RSK-046 is admitted only when scored at its worst member (F-02).

| Risk | Passes (Yes or No) | Finding ids |
|---|---|---|
| RSK-001 | Yes | F-04 |
| RSK-002 | Yes | none |
| RSK-003 | Yes | none |
| RSK-004 | Yes | none |
| RSK-005 | Yes | none |
| RSK-006 | Yes | none |
| RSK-007 | No | F-02 |
| RSK-008 | No | F-05 |
| RSK-009 | No | F-06 |
| RSK-010 | Yes | none |
| RSK-011 | Yes | none |
| RSK-012 | Yes | none |
| RSK-013 | No | F-06 |
| RSK-014 | Yes | none |
| RSK-015 | No | F-12 |
| RSK-016 | Yes | none |
| RSK-017 | Yes | none |
| RSK-018 | Yes | none |
| RSK-019 | Yes | none |
| RSK-020 | No | F-12 |
| RSK-021 | Yes | none |
| RSK-022 | No | F-12 |
| RSK-023 | No | F-06 |
| RSK-024 | Yes | F-04 |
| RSK-025 | No | F-02 |
| RSK-026 | Yes | none |
| RSK-027 | Yes | F-04 |
| RSK-028 | Yes | none |
| RSK-029 | Yes | none |
| RSK-030 | No | F-07, F-12 |
| RSK-031 | Yes | none |
| RSK-032 | Yes | none |
| RSK-033 | Yes | none |
| RSK-034 | Yes | none |
| RSK-035 | Yes | F-04 |
| RSK-036 | Yes | F-04 |
| RSK-037 | Yes | F-04 |
| RSK-038 | Yes | none |
| RSK-039 | No | F-02 |
| RSK-040 | No | F-02 |
| RSK-041 | No | F-02, F-04 |
| RSK-042 | No | F-12 |
| RSK-043 | No | F-02 |
| RSK-044 | Yes | none |
| RSK-045 | No | F-02, F-04 |
| RSK-046 | No | F-02, F-04, F-08 |
| RSK-047 | Yes | F-04 |
| RSK-048 | No | F-02 |
| RSK-049 | Yes | none |
| RSK-050 | Yes | none |
| RSK-051 | Yes | none |
| RSK-052 | No | F-02 |
| RSK-053 | Yes | none |
| RSK-054 | No | F-12 |
| RSK-055 | Yes | F-04 |
| RSK-056 | Yes | none |
| RSK-057 | No | F-12 |
| RSK-058 | Yes | F-04 |
| RSK-059 | Yes | none |

Result: 38 of 59 pass; 21 do not. No risk leaves *Proposed* on this record until its findings are Verified (06 section 9 status transitions).

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 | Not met (failure outside the product) | Before this record: `validate_docs: 15 passed, 1 failed, 16 checked`, exit 1; the only failure is `docs/design/allocation.json` "schema not found: docs/design/allocation.schema.json" (cross item). `register.json` passes its schema. After this record: see Tool runs. |
| R2 | `tools/render_risk.py --check` exits 0 | Met | `register OK: 59 risks, 130 candidates, 0 warning(s), jsonschema used`; `register.md is current`; exit 0 |
| R3 | Section B trade study sections | N/A | Product is the register |
| R4 | Author return lists risks added, re-scored or proposed for closure | Met | Author summary for H9 and F6: the seven SRR-due steps (RSK-009 S1, RSK-010 S1, RSK-012 S5, RSK-013 S1, RSK-016 S3, RSK-028 S2, RSK-046 S1) with dispositions; each has a matching history entry dated 2026-09-25 (SRR) |

`readiness_met: false` records R1.

## A. Risk register (06 section 16 items 1 to 11)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-A1 | No | `cd /Users/robinonsay/rust/cwht && .venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: `ERROR: HZ-015: related_risk_ids does not name RSK-034, which carries it (hazard link rule back-link)` / `1 error(s); nothing written.`, exit 1 (F-01). Without `--hazards`: `--check --gate SRR` exit 0. |
| CK-RSK-A2 | No | All 59 risks are *Proposed* (Counter over `status`). This record is their Analyze check: 38 pass, 21 do not (table above; F-02, F-05, F-06, F-07, F-12). |
| CK-RSK-A3 | No | Statements checked over all 59 (condition cited or dated, one departure or an admitted family, no solution language in departure or consequence; titles 80 characters or fewer). Defects: stale conditions RSK-009, RSK-013, RSK-023 (F-06); RSK-046 family scored below its worst member (F-02); step artifact id collisions (F-04). |
| CK-RSK-A4 | No | Every likelihood rationale names an anchor level and every consequence rationale names the driving dimension (scripted check over 59: no miss). The named anchor disagrees with the rationale's own facts for ten risks (F-02, Major) and cannot be met at SRR for seven (F-12). |
| CK-RSK-A5 | Yes | 24 Red risks (score 12 or more, or safety 5 at likelihood 2 or more: RSK-007, RSK-034). Each has strategy Mitigate, at least three active steps with artifact and due gate (minimum: RSK-026 and RSK-028, 3), at least one trigger whose response names an actor with timing in the response or condition (scripted check: all 24 pass), and a fallback. `plan_approval` is absent on all 24; SRR is their first gate review and the approval is requested as package decision 14, so the item is met at this point and becomes a `--gate PDR` error if the SRR memo does not record it. The Red list changes under F-02. |
| CK-RSK-A6 | N/A (from PDR) | Advisory: ten Red risks have no REQ or HZ link today (RSK-002, 003, 004, 005, 008, 012, 014, 027, 028, 029); RSK-012 can link `docs/requirements/sw/sw-keyer/requirements.json`, which now exists, and RSK-027 a REQ-SYS output-power requirement. |
| CK-RSK-A7 | No | Two-way check over the 15 hazards (all status *Controls proposed*): 14 correct both ways, safety at or above the mapped severity; HZ-015 back-link missing (F-01); RSK-046 carries HZ-008 in substance with no link on either side (F-08). |
| CK-RSK-A8 | No | RSK-008 is the only `aggregate`; likelihood 4 equals the maximum of its 11 active children (RSK-003 and RSK-014 at 4); the child list is incomplete (RSK-025) and the first trigger names 9 of 11 (F-05). |
| CK-RSK-A9 | Yes | Low confidence: RSK-007 (S1 hazard-analysis step Done; S2 trade study, Research-type step; re-assessment trigger) and RSK-034 (HZ-015 hazard steps S1 to S4); the tool's Low-confidence rule passes. |
| CK-RSK-A10 | No | Candidates: 130 (Entered 63, Merged 48, Declined 19), matching the package table by source (22 research reports, 17 ConOps section 8 items folded in); every Entered or Merged candidate names an existing risk whose `source` holds it (tool). Missing dispositions: ADR-011 section 4.4 and 07 sections 16.2 and 21 candidates (F-03). Package section 11 counts and the decision 14 and 32 wording do not match the register history (F-07, F-09). |
| CK-RSK-A11 | No | Software-risk list (register.md SWE-086 row, confirmed by script): 26 risks, 10 category software (RSK-003, 010, 012, 013, 015, 019, 020, 021, 022, 023) and 16 tagged software (RSK-002, 006, 007, 009, 016, 017, 024, 028, 032, 033, 037, 041, 042, 046, 051, 056). Six steps: record, analysis, plan and tracking evidenced for each in `register.json` (history, last_assessed SRR); control decision pending the SRR memo (all Proposed); communication in package section 11 (stale, F-09). 07 section 21 rows: RSK-010, RSK-003, RSK-019 (complexity), RSK-013, RSK-020 (toolchain), RSK-021 (flash), RSK-015, RSK-023 (rustos maintainer) present; "Host mock diverges from silicon" absent. 07 section 16.2 rows: image and configuration (RSK-015), debug (RSK-022) present; keying-input injection, diagnostic interface, build and supply chain absent (F-03). Process audit against 06: the six steps, the SWE-086 record row and the software-tag rule (tool-enforced) are in place; the population is incomplete. Measures (register.md, SRR row): active 59; Red 24, Yellow 30, Green 5; opened 25; closed or retired 0; accepted 0; open steps due at SRR 3; overdue 0. |

### RSK-009 S1 check reproduced (evidence for H9)

Independent read-only re-run over `docs/process/rmm.json` (100 rows) and `docs/references/md/swehb/` (267 files, 130 `swe-` pages) with the S1 criteria recorded in the RSK-009 history (exactly one `swe-NNN-*.md` page; `# 3. Guidance`, `# 4. Small Projects`, `# 7. Software Assurance` each with at least 200 non-space characters; no U+FFFD): miss list empty; minima 6056, 3283 and 6407. The author's figures are confirmed exactly.

### SRR-due steps verified

| Step | Register state | Reviewer check |
|---|---|---|
| RSK-009 S1 | Done | Reproduced (above). Closure not claimed; S2 due PDR. |
| RSK-010 S1 | Re-planned to PDR | 05 section 13 PDR row lists `cargo-llvm-cov` with llvm-tools; `tools/toolchain.lock.md` cargo-llvm-cov row "TV pending (due PDR, before FW-B0 coverage is cited)". Confirmed. |
| RSK-012 S5 | Planned, due SRR | `docs/icd/` holds no ICD-CTL-KEY (H11). Correctly open. |
| RSK-013 S1 | Done | 07 section 19 table WP-SW-01 to WP-SW-13; technology assessment section 3.18 titled "WP-01 to WP-10" and citing WP-01 to WP-04, WP-10, WP-13, a different numbering (the author's cross item is confirmed). |
| RSK-016 S3 | Done | ConOps sections 3.6 (P1 primary, antenna 20 cm or more; 0.6 m keying, 1.0 m tune; non-licensees not above 1 W) and 3.7 (OPS-A default), scenarios OPS-018 and OPS-019 present; matches HZ-001 K6, HZ-006 K4 and K8 texts. Confirmed. |
| RSK-028 S2 | InProgress | ADR-015 exists; decision 17 in package section 13.1. Correct. |
| RSK-046 S1 | InProgress | Decisions 9 and 40 in package section 13.1. Correct. |

## Plan items for 06 (peer-review-checklist-requirements section G)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | 06 expands charter sections 3, 5, 6, 9, 11 rule 6 and agrees with the SE-19 and SE-23 matrix rows (`render_compliance.py --check` exit 0). Stale alignment rows in section 17 (F-10). The record path rule (06 section 16, template, 01 section 13: `checklists/risk-register.md`) differs from this assigned path (charter issue in the return). |
| CK-REQ-G2 | No | Steps name artifacts and id schemes (sections 9, 11, 12, 14.3); no TBD, no "as appropriate". Gaps: strategy definitions (F-11), anchors unreachable before TV records and no rule for non-design risks (F-12), candidate sources (F-13). |
| CK-REQ-G3 | Yes | Section 2 roles table; owner approval points: header (ETA approval), section 8 (Red plan approval, acceptance), section 9 transitions, section 14.5. Independence: section 2 reviewer row. |
| CK-REQ-G4 | No | NPR 8000.4, SP-2011-3422 and SP-2010-576 non-adoption stated in the header, consistent with charter section 1. SWE-154 is Tailored in the RMM but not mirrored (F-15). |
| CK-REQ-G5 | N/A | 06 is not the cybersecurity plan; it points to 07 section 16.2 (section 15 SWE-154 row). The incomplete cyber population is F-03. |
| CK-REQ-G6 | No | Section 12 measures table: source and storage named, no threshold or analysis rule (F-14). |
| CK-REQ-G7 | Yes | `tools/render_risk.py` has `validate_risk` (line 194), `validate_candidates` (412), `validate` (447), `check_hazards` (484); `tools/tests/fixtures/risk/` holds `valid.json`, `valid.md`, `stale.md`, `faults.json`, `hazards.json`; lock row present (`tools/toolchain.lock.md` line 81); the section 12 statement that no TV record exists yet is true (`docs/cm/` absent). |
| CK-REQ-G8 | Yes | Pinned in the corpus: SE-19 at NPR 7123.1D 3.2.14.1 and 3.2.14.2 naming NPR 8000.4 and SP-2011-3422 (`03-chapter3.md` lines 188 to 190); SE-23 at 3.2.18.1 (line 224) and 3.2.18.2 (line 226); SWE-086 at 5.2.1 (`swehb/swe-086-continuous-risk-management.md`); SWE-154 at 3.11.3; SWE-033 at 3.1.2 (`npr-7150-2d/03-chapter3.md` line 13); NPR 7150.2D 6.1 items r and t (`06-chapter6.md` lines 47 and 51); SE HB 6.4.1.1 and Figure 6.4-3 (`18-6-4-technical-risk-management.md` lines 78 to 111, technical risk status measurements); SE HB 6.8.1.2.1 to 6.8.1.2.7, 6.8.1.3.1 and Table 6.8-1 (`22-6-8-decision-analysis.md`); App. G Tables G-3 5.5 and s11, G-4 6.4, 6.5, s6 and s14, G-7 6.32 and s9, G-11 3.14, G-12 12 and s6, G-13 10, s8 and s10 (`13-appendixg.md`); SWEHB SWE-086 tab 7 tasks 1 and 2 present. No misquotation found. |

## Section B (trade study)

CK-RSK-B1 to CK-RSK-B10: N/A (product is the register).

## Tool runs (2026-09-25)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` | 1 | 15 passed, 1 failed (`docs/design/allocation.json`, schema not found; outside scope) |
| `.venv/bin/python tools/render_risk.py --check` | 0 | 59 risks, 130 candidates, 0 warnings; render current |
| `.venv/bin/python tools/render_risk.py --check --gate SRR` | 0 | |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 1 | HZ-015 back-link (F-01) |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 231 requirements, 108 test cases, 82 violations, 43 warnings (none on RSK ids) |
| `.venv/bin/python tools/render_rmm.py --check` | 1 | SWE-051 status Planned with every path existing (outside scope) |
| `.venv/bin/python tools/render_compliance.py --check` | 0 | passed, render current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 331 tests, 1 failure: `test_repository_exit_zero` (the allocation.json schema failure) |

## Participants and measurements (SWE-089)

Author agent `author:risk-manager` (not present). Reviewer agent `reviewer:risk` (this record). Software assurance reviewer: not required for the register (template `assurance_required: false`); the SWE-086 tab 7 audit is CK-RSK-A11 above. Owner: disposition of the findings at the review. Items: 11 register items and 8 plan items answered, 10 section B items N/A; answered No: 12; findings Major 4, Minor 11; fixed 0; deferred 0; iteration 1.

## Closure (iteration 2, 2026-09-25)

**Re-review scope.** `reviewer:risk`, new invocation of the same role, independent of the author, edited none of the product. The author reported F-02 to F-08 and F-10 to F-15 fixed, disputed F-01 (already applied by the hazard analysis author) and F-09 (outside the author's scope). Products re-opened in the working tree: `docs/risk/register.json` 0.6.0-pre-srr (blob `2903601e26a5a2acce1a7f8fb29fdea048942358`), `docs/risk/register.md` (blob `761f3731bb54ede888c3d55b407671ab131a2159`, reported current by the tool), `docs/process/06-risk-and-decision-analysis.md` (blob `7a92d21f24a1733d70ae083576e708274bfd1a6d`, the `git diff` against `4e3f891` read in full), and, for F-01 and F-08, `docs/safety/hazards.json` (blob `98ee9d1646ba32e004b78ab90d64bb158fce958c`). Read-only Python over the JSON checked each fix and the whole population (likelihood rationale against the 06 section 6 cases, Red minimums over the 32 Red risks, trade-study links, candidate dispositions, the six new risks RSK-060 to RSK-065). The 47 CFR 15.23(a) text that RSK-065 cites was confirmed at `docs/references/md/regulatory/47cfr-15.23.md` line 17. No em dash and no bare TBD in the register or 06. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: peer review record closure block re-review disposition) ran before any `grep`; `grep -n` then pinned lines in `package.md`, 07, 08 and the trade studies.

| Disposition | Count | Findings |
|---|---|---|
| Closed (fix verified in the product or, for F-01 and F-08, in `hazards.json`) | 14 (Major 4, Minor 10) | finding-1 to finding-8, finding-10 to finding-15 |
| Disputed accepted | 1 (within the Closed count) | finding-1: the author is right that the HZ-015 back-link is already set and that the fix was the hazard analysis author's; the defect is gone, so it is Closed |
| Open | 2 (Minor) | finding-9 (dispute not accepted: the package and 07 section 22 text is still wrong; owners package author and 07 author); finding-16 (new: 06 section 17 hazard row reports an exit 1 that no longer occurs) |

Major findings not closed: 0. Verdict NEEDS CHANGES: no Major finding remains, and on the product alone the two open Minor findings would ride with APPROVED (08 section 3.2), but `readiness_met` stays false for R1 (`validate_docs.py` exits 1 on two files outside the product, `docs/design/allocation.json` and `docs/plan/measurements.json`, schema not found), and `tools/validate_docs.py` rejects APPROVED while `readiness_met` is false (SWE-088 b). The register and this record pass their own checks. The verdict becomes APPROVED on a re-run once R1 is met, with finding-9 and finding-16 carried as Minor.

**Iteration 2 answers** (items answered No at iteration 1; items not listed keep their iteration 1 answer).

| Item | Answer | Evidence |
|---|---|---|
| CK-RSK-A1 | Yes | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: `register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check`, exit 0 |
| CK-RSK-A2 | Yes | All 65 still *Proposed*; the Analyze check of this record now passes all 65 (the 21 of iteration 1 through F-02, F-05, F-06, F-07, F-12; RSK-060 to RSK-065 checked for statement parts, consequence dimensions, triggers with actor and timing, steps, fallback and closure criteria). They may move to *Open* when the software lead sets the findings Verified |
| CK-RSK-A3 | Yes | F-02, F-04, F-06 closed |
| CK-RSK-A4 | Yes | Scripted over 65: every rationale names an anchor level or a band-argument case; every case (a) anchor equals the recorded level; none claims anchor 1 or 2; band arguments carry confidence Medium or Low |
| CK-RSK-A5 | Yes | 32 Red (register.md SRR row); scripted: each has strategy Mitigate, Research or Elevate, at least two active steps with artifact and due gate, triggers and a fallback |
| CK-RSK-A7 | Yes | F-01, F-08 closed; tool hazard cross-check exit 0 |
| CK-RSK-A8 | Yes | F-05 closed |
| CK-RSK-A10 | No | Candidates 159, all dispositioned, Entered and Merged names checked by the tool; the package section 11 counts and decision 14 wording still disagree with the register (F-09) |
| CK-RSK-A11 | Yes | 07 sections 16.2 (six rows) and 21 (nine rows) all registered; software population now includes RSK-060 to RSK-063. Measures (register.md SRR row): active 65; Red 32, Yellow 25, Green 8; opened 31; closed or retired 0; accepted 0; open steps due at SRR 4; overdue 0 |
| CK-REQ-G1 | No | F-10 closed; F-16 open |
| CK-REQ-G2 | Yes | F-11, F-12, F-13 closed |
| CK-REQ-G4 | Yes | F-15 closed |
| CK-REQ-G6 | Yes | F-14 closed |

**Tool runs (iteration 2, 2026-09-25).**

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` | 1 | 30 passed, 2 failed (`docs/design/allocation.json`, `docs/plan/measurements.json`: schema not found; outside scope); `PASS docs/reviews/SRR/checklists/risk-register-06.md` |
| `.venv/bin/python tools/render_risk.py --check` | 0 | 65 risks, 159 candidates, 0 warnings; render current |
| `.venv/bin/python tools/render_risk.py --check --gate SRR` | 0 | |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | hazard cross-check passes |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 231 requirements, 167 test cases, 0 violations, 2 warnings (none on RSK ids) |
| `.venv/bin/python tools/render_rmm.py --check` | 0 | 100 rows; render current |
| `.venv/bin/python tools/render_compliance.py --check` | 0 | passed, render current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 331 tests, 1 failure: `test_repository_exit_zero` (the two schema-not-found failures above) |

**Cross items (outside the product; for Claude to route).** (1) `docs/reviews/SRR/package.md` section 11 and section 13.1 decision 14: refresh the measures and open-step list from register.md (65 active, Red 32, 4 open steps due at SRR) and reword decision 14 to approve the 32 Red plans and keep RSK-009 open to PDR (finding-9). (2) `docs/process/07-software-engineering-plan.md` section 22 row "RSK-009 closure evidence": "RSK-009 closes on its closure criteria (target PDR)" (finding-9). (3) `docs/process/rmm.json` SWE-154 implementation text: add RSK-060 to RSK-062 surfaces (recorded in 06 section 17). (4) `docs/process/08-agent-briefing.md` section 1 line 30 "268 pages scraped" to 267 files, 130 SWE pages (recorded in 06 section 17). (5) Schemas for `docs/design/allocation.json` and `docs/plan/measurements.json` (R1).

The record can close when finding-9 and finding-16 are fixed or deferred by the owner with a decision reference and a gate.

## Iteration 3 (2026-09-26, committed products at HEAD `adcfe09`; SRR package item R8)

**Scope and independence.** `reviewer:risk`, a new invocation of the reviewer role, independent of the author; it edited no file of the product and wrote only this record. Iterations 1 and 2 reviewed working-tree blobs that are not in the object store (package section 2.3). This iteration reviews the committed blobs named in `product_files` (`git rev-parse HEAD:<path>` at `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`): `register.json` `57f64995` (0.6.0-pre-srr, updated 2026-09-26), `register.md` `77b864a0`, 06 `7a92d21f` (the same blob as iteration 2). The register changed after iteration 2 in commit `08d1496` only; that commit message names RSK-012 S5 Done and the RSK-013 rationale, both re-read here, and the whole population checks of iteration 2 were re-run by read-only Python on the committed blob. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: package risk status, open steps due at SRR, decision 14, RSK-009 closure) ran before any `grep`; `grep -n` then pinned lines in `package.md`, 06, 07 and 08. The convergence rule of 2026-09-26 applies (charter section 4 item 3): only Major findings change products in this round, and every Minor finding is "Lien: fix before PDR".

| Finding | Severity | Check at HEAD `adcfe09` | Disposition |
|---|---|---|---|
| finding-1 to finding-8, finding-10 to finding-15 | Major 4, Minor 10 | Closed at iteration 2 on working-tree blobs; re-checked on the committed blob: `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0 (hazards.json `37d6cc83`, 0.4.2-pha); scripted over 65 risks: every likelihood rationale names an anchor level or a section 6 case, no anchor-level mismatch, no claim of anchor 1 or 2, every score equals likelihood times the maximum consequence; 32 Red, each with strategy Mitigate, Research or Elevate, at least two active steps, triggers and a fallback; 159 candidates (Entered 81, Merged 56, Declined 22); no `TS-001-cw-selectivity`, `TS-002-synthesizer` or `TS-003` step artifact; no em dash, no bare TBD in `register.json`, `register.md` or 06 | Closed (unchanged) |
| finding-9 | Minor | `docs/reviews/SRR/package.md` (blob `9042d945`) line 436: SRR 65 active, Red 32, Yellow 25, Green 8, open steps due at SRR 3 (RSK-028 S2, RSK-030 S1, RSK-046 S1), matching `register.md` "Risk status measures by review" SRR row; line 764 decision 14: "Approve the mitigation plans of the 32 Red risks ... and keep RSK-009 open to PDR"; no "24 Red", "7 open steps" or "close RSK-009" string remains; `07-software-engineering-plan.md` (blob `d0f8baf6`) line 866: "RSK-009 stays open until its closure criteria are met (S2 to S4 due PDR)" | Closed |
| finding-16 | Minor | 06 blob unchanged; line 423 still says the hazard analysis author adds RSK-046 to HZ-008 and "until then ... exits 1", while HZ-008 carries RSK-046 and the command exits 0 | Lien: fix before PDR |
| finding-17 (new) | Minor | 06 lines 371, 420 and 422 report the RMM SWE-154 text and the 08 "268 pages" count as open actions; both are done at HEAD (`rmm.json` SWE-154 implementation names RSK-060 to RSK-062; 08 line 30 "267 files, 130 of them SWE pages") | Lien: fix before PDR |

**Changed register text re-read (commit `08d1496`).** RSK-012 S5 is Done with evidence `docs/icd/ICD-CTL-KEY.md`, which exists at HEAD, with a dated history entry and an unchanged score; the SRR measures row now gives 3 open steps due at SRR, consistent with the step states. RSK-013 likelihood rationale no longer claims an on-board rustos run ("no on-board run is recorded in the repository", TC-SW-TOOL-001-r1) and keeps anchor level 3, which the 07 section 19 gap list (S1 Done) supports. No new Major defect was found.

**Citations re-pinned.** SWE-154 at NPR 7150.2D 3.11.3 (`npr-7150-2d/03-chapter3.md` line 299); SWE-086 (`npr-7150-2d/05-chapter5.md` line 41).

**Readiness.** R1 Met: `tools/validate_docs.py` exit 0 (37 passed, 0 failed). R2 Met: `render_risk.py --check` exit 0, register.md current. R3 N/A. R4 Met (iteration 1). `readiness_met: true`.

**Iteration 3 answers** (items not listed keep their iteration 2 answer).

| Item | Answer | Evidence |
|---|---|---|
| CK-RSK-A10 | Yes | finding-9 closed; package section 11 counts (159: 81, 56, 22) and decision 14 agree with the register |
| CK-REQ-G1 | No | finding-16 and finding-17 (Minor, liens) |

**Lien table.**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-16 | Minor | Lien: fix before PDR | Risk manager (06 author) | PDR readiness declaration |
| finding-17 | Minor | Lien: fix before PDR | Risk manager (06 author) | PDR readiness declaration |

**Counts after iteration 3.** 17 findings: Closed 15 (Major 4, Minor 11), Lien 2 (Minor), none open. Verdict APPROVED with liens under the convergence rule.

**Tool runs (iteration 3, 2026-09-26, HEAD `adcfe09`).**

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` | 0 | 37 passed, 0 failed (record drift rule applied) at the start of the iteration; after this record was written: `PASS docs/reviews/SRR/checklists/risk-register-06.md`, with one failure outside this record (the classification software assurance record, being edited in the working tree by another reviewer invocation at the same time) |
| `.venv/bin/python tools/render_risk.py --check` | 0 | 65 risks, 159 candidates, 0 warnings; register.md current |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | hazard cross-check passes |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148; none on RSK ids) |
| `.venv/bin/python tools/render_rmm.py --check` | 0 | 100 rows; render current |
| `.venv/bin/python tools/render_compliance.py --check` | 0 | passed, render current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 0 | 392 tests OK |

**Cross items (outside the product).** None new. Iteration 2 cross items (1) to (5) are done at HEAD.

## Post-SRR-ruling delta (iteration 3 re-issue 2, independent reviewer, 2026-09-26)

**Scope and independence.** `reviewer:risk`, a new invocation of the reviewer role; it authored no register entry, no R16 edit and no part of 06, and it edited no product file (this record only). Trigger: the owner approved the SRR on 2026-09-26, disposition Approved with liens L-1 to L-7 (`docs/reviews/SRR/minutes.md` line 47, "I approve of this and the SRR."), and ruled every key decision K1 to K17 and every consent-agenda decision as recommended (minutes line 21; `docs/reviews/SRR/decisions-for-owner.md`, the Recommendation cell is the ruling). Package item R16 (`docs/reviews/SRR/package.md` section 2.1) applies the rulings. Review baseline: HEAD `ebe5873`. `git log adcfe09..HEAD -- docs/risk/register.json docs/risk/register.md docs/process/06-risk-and-decision-analysis.md` lists one commit, `9bdf33c`, which moves `register.json` from blob `57f64995` to `0c25c0c5b6ca801b02e47c29c19bb8ed44aa5c79` and `register.md` from `77b864a0` to `a3a983e5cdf7e769666fab26d5f2e7f3b373db1f`; 06 is unchanged (blob `7a92d21f`). Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: SRR decision, Red plan approval, `plan_approval`, risk register owner ruling) ran before any `grep -n`, which then only pinned lines in the decision memo, the minutes, 06 and ADR-015. Convergence rule of 2026-09-26 (charter section 4 item 3): a new Minor is a lien fixed before PDR and does not block the baseline.

**Delta verification of `9bdf33c` (the register hunks only; the `semp.md` and `rmm.json` hunks belong to INSP-005 and the classification records).**

| Change | Ruling cited | Checked against | Result |
|---|---|---|---|
| `mitigation.plan_approval` = {`decision_memo`: `docs/reviews/SRR/decision-memo.md`, `date`: 2026-09-26} added to 32 risks; no other field of `register.json` changed (the diff has 32 hunks, each the `fallback` line plus the new `plan_approval` line) | SRR decision 14 (K4, owner ruling 2026-09-26): "Approve all 32 plans; RSK-009 closes on its closure criteria (target PDR)" | Read-only Python over the HEAD blob: the 32 approved risks are exactly the active Red set (score 12 or more, or safety 5 at likelihood 2 or more), no Yellow or Green risk carries an approval; the memo exists and its section 8.4 row 14 (line 374) names this record; `docs/risk/schema.json` `plan_approval` requires `decision_memo` and `date`, both present; `render_risk.py --check --gate PDR` reports no `plan_approval` error (its 76 errors are the expected pre-PDR Track pass and REQ/HZ link errors of 06 sections 10 and 11) | Correct and complete |
| RSK-009 left open, S2 to S4 due PDR, closure criteria unchanged | SRR decision 14 (RSK-009 part) | RSK-009 status Proposed, strategy Mitigate, S1 Done, S2 to S4 Planned PDR | Correct |
| `register.md` re-rendered: 32 "Plan approval" rows change from "pending (owner approves Red plans at the next review, process section 8)" to "2026-09-26, memo docs/reviews/SRR/decision-memo.md" (32 insertions, 32 deletions) | SRR decision 14 | `render_risk.py --check`: "register.md is current", exit 0 | Correct |

New-defect scan of the `9bdf33c` hunks: no em dash in `register.json` or `register.md` (count 0); no history entry rewritten (every risk has the same number of `history` entries as at `adcfe09`); `last_assessed` unchanged, consistent with the last `history` entry (tool). No new Major defect.

**Rulings that touch the register but were not applied at HEAD.** Checked against the decision memo line 378 ("Residual risks accepted by the owner") and the register steps whose output is a ruling of the SRR board (06 section 12, "Open steps due at the gate being prepared"):

| Decision (owner ruling 2026-09-26) | Register at HEAD `ebe5873` | Expected by 06 or by the step's own text |
|---|---|---|
| 32 (K4): accept SAR by analogy, record RSK-030 as an accepted risk | RSK-030 status *Proposed*, strategy *Accept*, no `acceptance` record; S1 (due SRR) *InProgress*; last `history` entry 2026-09-25 | S1 action: "On acceptance Claude sets this risk Accepted with the acceptance record (docs/reviews/SRR/decision-memo.md, the date, residual score 4)"; 06 section 8 strategy table, *Accept* row: "after the decision, status *Accepted* with the acceptance record" |
| 17 (K5): accept ADR-015 (ADR-015 Status row "Accepted" at HEAD, commit `2362183`) | RSK-028 S2 "Owner decision on ADR-015 at SRR recorded in the decision memo", due SRR, *InProgress*; RSK-016 rationale still says "owner decision 17 disposes ADR-015 (RSK-028 S2)" in the future tense | S2 Done with the memo as evidence and a dated `history` entry |
| 9 and 40 (K1): frequency control safety-critical (OQ-SAF-014); adopt REQ-SYS-182, independent frequency verification (HZ-008 K7, OQ-SAF-013) | RSK-046 S1 "Owner decisions at SRR on ..." due SRR, *InProgress*; rationale still frames decision 40 as a recommendation | S1 Done with the memo as evidence; RSK-046 re-assessed on the adopted control with a `history` entry |
| 11 (K4): accept hardware TRL 3 at the CDR procurement release as a recorded residual of RSK-008 | RSK-008 has no `history` entry or note recording the accepted residual | A dated `history` note naming decision 11 and the memo (RSK-008 stays Red under *Mitigate*, so no *Accepted* status) |
| 6 and 8 (K3): SWE-219 relief, RSK-010 carries the residual | RSK-010 condition already reads "approved by the owner at SRR" | Consistent; no change needed |
| 55, 66, 68, 85, 95 (consent and K8): RSK-058, RSK-039 S1, RSK-040, RSK-059, RSK-015 and RSK-022 as the carriers named in the rulings | Carriers exist; their steps are due PDR or later and already state the recommended direction | Consistent; no change needed |

<a id="finding-18"></a>**finding-18 (new), Minor, Lien: fix before PDR.** Items CK-RSK-A2, CK-RSK-A10. Location: RSK-030 (`status`, `acceptance`, S1), RSK-028 S2, RSK-046 S1 and its likelihood rationale, RSK-016 likelihood rationale, RSK-008 `history`; all 65 risks' `status`. Description: `9bdf33c` applies decision 14 only. (a) Decision 32 accepted RSK-030's residual (memo line 378), but the risk is not *Accepted* and has no `acceptance` record, which its own S1 and the 06 section 8 *Accept* row require after the decision. (b) The three steps whose output is an SRR ruling (RSK-028 S2 on decision 17, RSK-030 S1 on decision 32, RSK-046 S1 on decisions 9 and 40) are still *InProgress* and due SRR after the ruling was recorded; by the 06 section 12 threshold "Open steps overdue (due at an earlier gate)" they become RIDs at PDR, Major for RSK-046 (Red, carries HZ-008) and RSK-030 (carries HZ-001). (c) Decision 11's accepted residual is not noted on RSK-008. (d) All 65 risks remain *Proposed* although this record's Analyze check has passed all 65 since iteration 2 (06 section 9, Analyze row: "status moves *Proposed* to *Open* when the reviewer's filled checklist ... records the risk as passing"; 06 section 16 item 2). Why Minor, not Major: the rulings themselves are recorded with authority in the signed decision memo (charter section 4 item 4), no score, band, plan or hazard link is wrong, and `render_risk.py --gate SRR --hazards` passes; the defect is a register record lagging its approving record, fixed by a Track pass before the PDR readiness declaration. Fix (risk manager): one SRR Track pass that sets RSK-030 *Accepted* with `acceptance` {decision memo, 2026-09-26, residual score 4}; sets RSK-028 S2, RSK-030 S1 and RSK-046 S1 Done with the memo as evidence; re-assesses RSK-046 on the adopted REQ-SYS-182 control; adds a decision 11 note to RSK-008; restates the RSK-016 and RSK-046 rationales in the past tense; moves the risks that pass this record from *Proposed* to *Open* (06 section 9; the software lead sets the findings Verified first, as iteration 2 recorded); each change with a dated `history` entry citing its decision number.

**Findings closed by the rulings.** None was open: finding-1 to finding-4 (the four Major findings) were Closed at iteration 2 and re-checked on committed blobs at iteration 3; the `9bdf33c` hunks touch only the `plan_approval` field and re-open none of finding-1 to finding-15. The rulings resolve no lien: finding-16 and finding-17 concern 06 section 15 and 17 rows, and 06 is unchanged (blob `7a92d21f`), so both remain liens due PDR. Decision 14 completes the CK-RSK-A5 condition recorded at iteration 1 ("becomes a `--gate PDR` error if the SRR memo does not record it"): every Red risk now carries `plan_approval`.

**Re-issue 2 answers** (items not listed keep their iteration 3 re-issue 1 answer).

| Item | Answer | Evidence |
|---|---|---|
| CK-RSK-A1 | Yes | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: "register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check", exit 0 (hazards.json at HEAD, 0.5.0-pha, `bfea9c7`) |
| CK-RSK-A2 | No | All 65 risks still *Proposed* after the SRR (finding-18 (d)) |
| CK-RSK-A5 | Yes | 32 Red, each with `plan_approval` naming the SRR decision memo and 2026-09-26 (decision 14); the iteration 2 minimums re-checked on the HEAD blob |
| CK-RSK-A10 | Yes (with finding-18) | 9bdf33c changes only `plan_approval`, which needs no candidate disposition; package section 11 still matches the register counts (65 active, Red 32); the unapplied ruling records are finding-18 |
| CK-REQ-G1 | No | finding-16 and finding-17 (liens, unchanged) |

**Lien table (re-issue 2).**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-16 | Minor | Lien: fix before PDR (unchanged) | Risk manager (06 author) | PDR readiness declaration |
| finding-17 | Minor | Lien: fix before PDR (unchanged) | Risk manager (06 author) | PDR readiness declaration |
| finding-18 | Minor | Lien: fix before PDR (new) | Risk manager (register author) | PDR readiness declaration, and before any PDR RID count of overdue steps |

**Counts after re-issue 2.** 18 findings: Closed 15 (Major 4, Minor 11), Lien 3 (Minor), none open. Open Major 0. Verdict APPROVED with liens under the convergence rule.

**Tool runs (re-issue 2, 2026-09-26, HEAD `ebe5873`).**

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` | 1 | Before this record: 34 passed, 16 failed; the failures are record drift of other records whose products R16 changed (ADR, ConOps, hazard analysis, `rmm.json` records being re-issued by other reviewer invocations in this run) and this record (drift on `register.json` and `register.md`). After this record: `PASS docs/reviews/SRR/checklists/risk-register-06.md` (see the note below) |
| `.venv/bin/python tools/render_risk.py --check` | 0 | 65 risks, 159 candidates, 0 warnings; register.md current |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | hazard cross-check passes |
| `.venv/bin/python tools/render_risk.py --check --gate PDR` | 1 | 76 errors, none on `plan_approval`: 65 "last assessed at SRR, before the PDR Track pass", 11 "Red risk has no REQ or HZ link at PDR or later" (expected before PDR; iteration 1 advisory CK-RSK-A6) |
| `.venv/bin/python tools/traceability.py --report-only` | 1 | 245 requirements, 173 test cases, 4 violations (REQ-SYS-122, 124, 137, 138 `HAZARD_REQ_NOT_TESTED`, the Inspection method of CR-002 and decision 113 not yet accepted by the tool; none on RSK ids), 2 warnings; report files restored with `git checkout` |
| `.venv/bin/python tools/render_rmm.py --check` | 1 | SWE-033 status Planned with every path existing (outside the product) |
| `.venv/bin/python tools/render_compliance.py --check` | 0 | passed, render current |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 400 tests, 1 failure: `test_repository_exit_zero` (the repository-wide `validate_docs.py` failures above) |

**Cross items (outside the product; for Claude to route).** (1) `tools/traceability.py` rule `HAZARD_REQ_NOT_TESTED` against the CR-002 (decision 113) Inspection method for documentary hazard controls (REQ-SYS-122, 124, 137, 138). (2) `docs/process/rmm.json` SWE-033 status (render_rmm check). (3) The register Track pass of finding-18 should precede the INSP-008 and hazard analysis re-check of the HZ-001 and HZ-008 risk links, since RSK-030 moves to *Accepted*, which the hazard link rule no longer counts as carrying HZ-001 (RSK-016 and others still carry it; `--hazards` to be re-run after the pass).

## Finding-18 delta (iteration 3 re-issue 3, independent reviewer, 2026-09-27)

**Scope and independence.** `reviewer:WP-PDR-18-risk-register`, a new invocation that authored no register entry, no part of the Track pass and no part of 06, and edited no product file. Trigger: `docs/plan/pdr-work-plan.md` WP-PDR-18 names an "INSP-007 delta for the SRR liens" beside the PDR record. The Track pass commit `4df6606` (Log class, 05 Table 4-1 row 14) moved `register.json` from `0c25c0c5` to `6685aa0e` and `register.md` from `a3a983e5` to `f8c28b36`; 06 is unchanged (blob `7a92d21f`). The full check of that commit is `docs/reviews/PDR/checklists/risk-register.md` (INSP-036, iteration 1, APPROVED with five Minor liens); this delta records only what it means for the liens of this record. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep -n`.

| Finding | Re-issue 3 result | Evidence | State |
|---|---|---|---|
| finding-18 (a) RSK-030 | *Accepted*, `acceptance` {decision memo, 2026-09-26, residual score 4}, S1 Done, citation clause moved to S3 (due PDR) | INSP-036 rule C7 table | Fixed |
| finding-18 (b) SRR-due steps | RSK-028 S2, RSK-030 S1, RSK-046 S1 Done with the memo as evidence; no step due SRR is Planned or InProgress in the register | INSP-036 rule C7 table | Fixed |
| finding-18 (c) RSK-008 | Dated note and condition clause for decision 11 | INSP-036 rule C7 table | Fixed |
| finding-18 RSK-016, RSK-046 wording | RSK-046 rationale re-assessed on REQ-SYS-182 in the past tense; the RSK-016 wording this record quoted sits in a 2026-09-25 history note, and the Track entry records decisions 17 to 20 in the past tense (history is append-only) | INSP-036 rule C7 table | Fixed |
| finding-18 (d) statuses | 0 Proposed; 55 Open, 9 Mitigating, 1 Accepted; INSP-036 re-performs the Analyze check at the 06 section 9 path and passes all 65 | INSP-036 CK-RSK-A2 | Fixed |
| finding-16, finding-17 | 06 unchanged (blob `7a92d21f`); C-140 and C-141 are WP-PDR-18 final-pass outputs | `git log 4df6606^..HEAD -- docs/process/06-risk-and-decision-analysis.md` empty | Lien (unchanged) |

Cross item (3) of re-issue 2 is answered: *Accepted* is an active status for the hazard link rule (`tools/render_risk.py` line 67, `INACTIVE = {"Closed", "Retired"}`), and `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exits 0 on the Track pass blob.

**Re-issue 3 answers** (items not listed keep their earlier answer).

| Item | Answer | Evidence |
|---|---|---|
| CK-RSK-A1 | Yes | `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: "register OK: 65 risks, 159 candidates, 0 warning(s), jsonschema used, gate SRR, hazard cross-check", exit 0 |
| CK-RSK-A2 | Yes | No risk is *Proposed* (finding-18 (d) Fixed) |
| CK-RSK-A10 | Yes | The rulings named in finding-18 are transcribed with dated `history` entries citing their decision numbers |
| CK-REQ-G1 | No | finding-16 and finding-17 (liens, unchanged) |

**Lien table (re-issue 3).**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-16 | Minor | Lien: fix before PDR (unchanged) | Risk manager (06 author) | PDR readiness declaration (WP-PDR-18 final pass, C-140, C-141) |
| finding-17 | Minor | Lien: fix before PDR (unchanged) | Risk manager (06 author) | PDR readiness declaration (WP-PDR-18 final pass, C-140, C-141) |

**Counts after re-issue 3.** 18 findings: Closed or Fixed 16 (Major 4, Minor 12), Lien 2 (Minor), none open. Open Major 0. Verdict APPROVED with liens under the convergence rule. The software lead sets the Fixed findings Verified and closes the record after finding-16 and finding-17 are fixed.

## Verdict (returned by the reviewer)

```
ITERATION 1 (2026-09-25): VERDICT: NEEDS CHANGES. Major 4, Minor 11, all Open.
ITERATION 2 (2026-09-25): VERDICT: NEEDS CHANGES (readiness R1 not met, outside the product). Closed 14, all four Major among them; the first finding closed with the author's dispute accepted. Still open: 2 Minor (finding-9 package and 07 text, dispute not accepted; finding-16 new, 06 section 17 hazard row). No Major remains.
ITERATION 3 (2026-09-26): VERDICT: APPROVED (with liens). Committed blobs register.json 57f64995, register.md 77b864a0, 06 7a92d21f. finding-9 Closed; Liens 2 (finding-16, finding-17 new: 06 stale alignment rows, fix before PDR). No Major remains; readiness met.
ITERATION 3 RE-ISSUE 2 (2026-09-26, post-SRR-ruling delta at HEAD ebe5873): VERDICT: APPROVED (with liens). Committed blobs register.json 0c25c0c5, register.md a3a983e5, 06 7a92d21f. Delta 9bdf33c applies SRR decision 14 correctly (plan_approval on exactly the 32 Red risks). finding-18 new Minor: rulings 32, 17, 9 and 40, 11 not yet transcribed into the register and the 65 risks still Proposed; Lien: fix before PDR. Liens 3 (finding-16, 17, 18). Open Major 0.
ITERATION 3 RE-ISSUE 3 (2026-09-27, finding-18 delta on the WP-PDR-18 Track pass 4df6606): VERDICT: APPROVED (with liens). Committed blobs register.json 6685aa0e, register.md f8c28b36, 06 7a92d21f. finding-18 Fixed (full check in INSP-036). Liens 2 (finding-16, 17). Open Major 0.
```
