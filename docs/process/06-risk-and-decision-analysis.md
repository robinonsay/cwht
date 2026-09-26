# 06 Technical Risk Management and Decision Analysis

**Status:** Draft for SRR (this document is the project Risk Management Plan, an SRR entrance product per NPR 7123.1D App. G Table G-4 item 6.4). **Owner:** Robin (Decision Authority, risk acceptance authority). **Author:** Claude. **Expands:** charter §3 (gates), §5 (risk register, trade studies, ADRs), §6 (`RSK-NNN`, `TS-NNN`, `ADR-NNN`), §9 (V&V philosophy), §11 rule 6 (record decisions).

**Approval (the "ETA-approved" clause of SE-19 and SE-23).** Robin approves this document as Engineering Technical Authority and SMA Technical Authority in `docs/reviews/SRR/decision-memo.md` (pending; charter §2); it is baselined with the functional baseline at tag `baseline/srr` and re-approved in the decision memo of every life-cycle review through SAR, which are the SEMP update points (`docs/plan/semp.md`). **Change control.** Before SRR this document is a Log-class change. After SRR any change to sections 4 to 8, 13 or 14 (statement rules, categories, scales, bands, risk-informed decision rules, decision analysis) goes through a `CR-NNN` (05 Table 4-1 row 2), and the same commit re-scores every affected risk in `docs/risk/register.json` and changes `tools/render_risk.py` and `tools/tests/test_render_risk.py` where the rule is implemented.

This document implements NPR 7123.1D SE-19 (Technical Risk Management process, §3.2.14.1) and SE-23 (Decision Analysis process, §3.2.18.1) and NPR 7150.2D SWE-086 (record, analyze, plan, track, control and communicate all of the software risks and mitigation plans), SWE-154 (cybersecurity risks and their mitigations) and SWE-033 (acquisition versus development) as far as they need a risk or decision record, following the practices of SE HB §6.4 and §6.8. NPR 8000.4 and NASA/SP-2011-3422, which NPR 7123.1D §3.2.14.2 and SE HB §6.4 name as the source documents for risk management, and NASA/SP-2010-576 (RIDM Handbook), which NPR 7123.1D §3.2.18.2 names as guidance for risk-informed decision analysis, are not in the reference corpus; the scales and rules below are therefore defined by this document and nothing in it is a quotation of those three documents.

## 1. Scope

| In scope | Artifact |
|---|---|
| Technical, safety, software, cost, schedule, programmatic and process risks of the cwht project from Formulation through SAR and into operations | `docs/risk/register.json` (source), `docs/risk/register.md` (rendered), `docs/risk/schema.json` |
| Disposition of candidate risks named in other artifacts | `candidates` array of `docs/risk/register.json` (section 9) |
| Risk-informed decision making for every formal trade study | `docs/decisions/trade-studies/TS-NNN-*.md` from `docs/templates/trade-study.md` |
| Architecture Decision Records | `docs/decisions/adr/ADR-NNN-*.md` |
| Rendering and consistency tool and its known-answer tests | `tools/render_risk.py`; `tools/tests/test_render_risk.py` with fixtures in `tools/tests/fixtures/risk/` |

Hazards (`HZ-NNN`, `docs/safety/`) are not risks: a hazard is a condition that can cause harm and is managed by the hazard analysis. The risk register carries the uncertainty that a hazard control will not be achieved, under the hazard link rule:

**Hazard link rule.** Every hazard in `docs/safety/hazards.json` whose status is not *Controls verified*, *Accepted* or *Retired* is carried by at least one active risk whose `related.hazard_ids` names it, and the hazard's `related_risk_ids` names every such risk back (`docs/safety/schema.json`). The risk's safety consequence is at least the register level that the hazard's severity maps to (`scales.severity` of `hazards.json`: Catastrophic 5, Critical 4, Marginal 3 or 2, Negligible 1). The risk closes when the hazard's controls are verified; the hazard record persists. When the hazard analysis adds a hazard, Claude links it to an existing risk or opens one in the same session (section 10.2). `tools/render_risk.py --hazards docs/safety/hazards.json` checks all three conditions (section 12).

## 2. Roles

| Role | Who | Risk management duties | Decision analysis duties |
|---|---|---|---|
| Owner, Decision Authority, ETA and SMA TA | Robin | Approves this process (header); sole authority to set a risk to *Accepted*, to approve the mitigation plan of a Red risk and to retire a risk; dispositions risk status at every review; decides when a trigger response needs money or a purchase | Decides every trade study; may select any alternative or ask for more; approves ADRs that constrain baselines |
| Risk manager, lead systems engineer, software lead | Claude (main session) | Identifies, analyzes, plans, tracks, renders and communicates risks; keeps `register.json` current; runs the section 12 commands before every review package; runs the candidate disposition pass and the trigger poll (sections 9 and 10.3); as software lead opens the software risks that `docs/process/07-software-engineering-plan.md` sections 16.2 and 21 list, with category software or tag software (section 5) | Writes trade studies and ADRs; recommends one alternative; opens the register entries a decision creates |
| Independent reviewer agent | Separate invocation (charter §2) | Checks every new or re-scored risk against sections 4 to 8 before it leaves *Proposed*; reviews the register with the checklist of section 16 before each review; performs the software assurance tasks of the SWEHB SWE-086 tab 7 (section 16 item 11) | Reviews every trade study with the checklist of section 16; records dissent in the trade study when it disagrees with the recommendation |
| Test-author agent | Separate invocation | Writes the verification cases for mitigation steps that become requirements | Writes the verification cases for requirements derived from a decision |

## 3. Definitions

- **Risk** (SE HB §6.4): the potential for a performance shortfall against stated requirements, characterized as a triplet of scenario, likelihood and consequence, with uncertainty on the last two. Domains per SE HB §6.4: safety, technical, cost, schedule, plus programmatic; this project adds software (SWE-086) and process.
- **Issue:** a risk whose departure has occurred. The risk record is set to *Realized* and names in `related.ncr_ids` the `NCR-NNN` (product nonconformance) or in `related.cr_ids` the `CR-NNN` (baseline change) that handles the consequence; the register alone never handles an issue. The schema and the tool reject a *Realized* risk without one of them.
- **Hazard link rule:** section 1.
- **Horizon:** the gate by which the departure would have to occur to matter. Likelihood is assessed against the horizon (default SAR).
- **Assessment confidence:** Low, Medium or High confidence in the likelihood and consequence levels. It records the uncertainty of the assessment; SE HB §6.4 states that uncertainty is included in the evaluation of likelihood and consequence. A Low-confidence risk carries a *Research* strategy, a trigger whose response re-assesses the risk, or a hazard-analysis step; `tools/render_risk.py` rejects a register where it has none of the three.

## 4. Risk statement format

Every risk is written as four stored parts that the renderer composes into one sentence:

> Given **[condition]**, there is a possibility of **[departure]** adversely impacting **[asset]**, leading to **[consequence]**.

| Part | Rule | Register field |
|---|---|---|
| Condition | A fact that is true today. Names the evidence: an `SI-NNN`, `REQ-*`, artifact path or observation with a date. No speculation. | `statement.condition` |
| Departure | Exactly one undesired event, or one failure-mode family admitted by the family rule below. The event may have several causes; they are named in the condition or the likelihood rationale. If two events are plausible and the family rule does not admit them together, write two risks. | `statement.departure` |
| Asset | The element harmed, named from the document tree or product breakdown: RX, TX, PWR, CTL, ME, SW-<sub>, a process artifact, the cost model, the schedule, or a person class (operator, bystanders). | `statement.asset` |
| Consequence | The effect expressed in the consequence dimensions of section 7, quantified where a number exists (USD, weeks, dB, degrees C). | `statement.consequence` |

**Family rule.** A departure may list several failure modes as one family only when every member (a) harms the same asset, (b) shares the family's driving consequence dimension, (c) is addressed by the same mitigation plan, fallback and closure criteria, and (d) is of the same kind: all members are safety departures or all are non-safety departures. A member is a safety departure when it alone would score safety 3 or more or when it is a cause of a hazard in `docs/safety/hazards.json`. The family is scored at its worst member (highest likelihood, highest level in each dimension). The reviewer applies the rule at section 16 item 3; a family admitted by the rule is recorded in the risk's `history` note the first time it is checked. Splitting an existing risk takes new `RSK` ids for the split-off departures, links the parts through `related.risk_ids` and records the split in the `history` of every part.

Rules: no solution language anywhere in the statement (solutions go in the mitigation plan); the condition is a clause ("the PA is verified only by ..."), while the departure and the consequence are noun phrases or gerund clauses ("the PA oscillating ...", "a second board spin that ...") so that the composed sentence reads correctly; the title is a short noun phrase naming the departure; the statement must let a reader who has not seen the project understand what would go wrong and why it matters.

## 5. Categories and tags

| Category | Definition | Typical source |
|---|---|---|
| safety | Departure that can injure a person, start a fire or damage property; includes RF exposure | Hazard analysis, battery, PA thermal |
| technical | Departure in the design, analysis or production of the product itself (SE HB §6.4 technical risk) | Simulation results, margins, vendor capability |
| software | Technical risk whose asset is firmware, host software or the software process (SWE-086) | Toolchain, emulator, coverage, keyer |
| cost | Departure against the cost model (SE HB §6.4 cost risk) | BOM, respin, instruments |
| schedule | Departure against the milestone list (SE HB §6.4 schedule risk) | Vendor lead time, redesign iterations |
| programmatic | Departure caused from outside the project (SE HB §6.4 programmatic risk): part availability, vendor policy, regulation, operators' conduct | Distributor stock, PCBWay terms, eCFR |
| process | Departure in the engineering process or its inputs (corpus, checklists, independence) | Corpus scrape, tool validation |

A risk has exactly one category. When two apply, choose the category of the asset named in the statement. Cross-cutting labels go in the optional `tags` array and never replace the category: `software` (below), `cyber` (cybersecurity risk, `07-software-engineering-plan.md` section 16.2, SWE-154), `hsi` (human-systems integration, SEMP section 7.3), `single-source` (SEMP section 5.13), `regulatory` (47 CFR exposure), `aggregate` (likelihood is the maximum of the active children in `related.risk_ids`, checked by the tool), `cm` (configuration management, `05-configuration-and-data-management.md` section 11), `spf` (an accepted single point failure, section 8).

**Software risk (SWE-086 population).** A software risk is any risk whose cause, control, mitigation step or asset involves firmware, host software or the software process. It is either `category: software` or carries the tag `software`, which is allowed with any category. The tag is required when a risk is not category software and a step artifact is under `docs/requirements/sw/`, `docs/test_cases/sw-*` or `firmware/`; `tools/render_risk.py` rejects a register that breaks this. Where 05 and 07 say "risks tagged software", they mean category software or tag software.

## 6. Likelihood scale

Likelihood is the probability that the departure occurs before the horizon. Each level has a probability band and an evidence anchor; the anchor decides when the band is uncertain.

| Level | Name | Probability before horizon | cwht evidence anchor |
|---|---|---|---|
| 1 | Very unlikely | below 5 % | The relevant requirement is already verified by Test on the delivered unit, or the design element is a heritage design used without change and confirmed by two independent analyses with at least 2x margin |
| 2 | Unlikely | 5 % to 20 % | Analysis with documented margin (at least 6 dB or 2x on the governing parameter) performed with a validated tool (SWE-136), following a vendor reference design |
| 3 | Possible | 20 % to 50 % | A single analysis exists but the tool or model fidelity is unconfirmed, or margin is below 2x, or the design deviates from any reference design |
| 4 | Likely | 50 % to 80 % | No analysis yet, or a known deficiency without a mitigation in progress, or the departure has occurred on a comparable project (for example rustos) |
| 5 | Near certain | above 80 % | The condition has already been observed on this project and only the consequence is pending |

When the author and the independent reviewer disagree by two or more levels, the higher level is recorded and `assessment_confidence` is set to Low.

## 7. Consequence scale

Consequence is scored in five dimensions. The overall consequence is the **maximum** over the dimensions; the renderer records the driving dimension. Every dimension is scored for every risk (1 when it does not apply).

| Level | Name | Safety | First-power-on success (SI-010) | Cost (spend beyond the cost-model contingency) | Schedule (slip of the next gate or of SAR) | Performance margin (against L1/L2 requirements, MOEs and stakeholder inputs) |
|---|---|---|---|---|---|---|
| 1 | Negligible | No credible harm; nuisance only (audible click, cosmetic) | Works at first power-on; any fix is a firmware reflash over USB within one session | below USD 25 | below 1 week | Margin reduced but at least 50 % of the allocated margin remains |
| 2 | Minor | Reversible discomfort, no medical attention; enclosure surface 45 to 55 C; RF exposure within FCC MPE limits with less than 2x margin | Fix by firmware, configuration, a part the owner can print on the H2C (SI-012) or a through-hole part the owner can hand-solder (SI-031); no PCB change | USD 25 to 100 | 1 to 3 weeks | Margin below 50 % of allocation but the requirement is still met |
| 3 | Moderate | First-aid injury (minor burn) or destruction of the unit without fire | One subsystem degraded while the radio still transmits and receives; fix needs vendor rework or a spare board population | USD 100 to 300 | 3 to 6 weeks (one vendor or design iteration) | One Baseline requirement not met but a CR or waiver is acceptable to the owner (for example 4 W instead of 5 W) |
| 4 | Major | Injury needing medical attention, or fire or smoke contained to the unit, or RF exposure above the FCC limit for a bystander, or harmful interference to a safety-of-life or other radio service | A core function (RX, TX, keying or power) does not work; a second board spin is required for full function | USD 300 to 800 (one additional fabrication plus assembly run) | 6 to 12 weeks (a full re-procurement cycle) | A KDR requirement, a regulatory requirement (47 CFR Part 97) or a stakeholder input (`SI-NNN`) is not met |
| 5 | Critical | Life-threatening injury, uncontained fire, or Li-ion venting with flame | Unit unsafe or dead at power-on, or friend units (SI-019) cannot be produced, in addition to a second spin | above USD 800 (respin plus new enclosure CNC, or project abandonment) | above 12 weeks or indefinite | An MOE or NGO is not achievable (the radio cannot make contacts) |

The safety column is aligned with the severity scale of `docs/safety/hazards.json` (Catastrophic 5, Critical 4, Marginal 3 or 2, Negligible 1), so that a risk carrying a hazard scores safety at least at the hazard's mapped level (hazard link rule, section 1). Two rules override the table:

1. **Regulatory rule.** Any departure that could breach the emission limits of 47 CFR §97.307 or the permitted emissions of §97.305 scores at least 4 in performance margin.
2. **Safety override.** A risk with safety consequence 5 is Red at any likelihood of 2 or more and Yellow at likelihood 1, regardless of the cell band in section 8.

## 8. Score, bands and required response

`score = likelihood x max(consequence)`, range 1 to 25. Bands by cell:

| Likelihood \ Consequence | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | Yellow (5) | Yellow (10) | Red (15) | Red (20) | Red (25) |
| **4** | Green (4) | Yellow (8) | Red (12) | Red (16) | Red (20) |
| **3** | Green (3) | Yellow (6) | Yellow (9) | Red (12) | Red (15) |
| **2** | Green (2) | Green (4) | Yellow (6) | Yellow (8) | Yellow (10), Red if safety = 5 |
| **1** | Green (1) | Green (2) | Green (3) | Green (4) | Yellow (5) |

Rule: Red when score is 12 or more; Yellow when score is 5 to 11; Green when score is 4 or less; plus the safety override of section 7. `tools/render_risk.py` implements exactly this rule and rejects a register whose stored `score` disagrees with the computation.

Every risk that is not *Closed* or *Retired* has at least one trigger (this is what `01-lifecycle-and-reviews.md` standing criterion S7 checks). The further minimums by band apply to every risk that is not *Accepted*, *Closed* or *Retired*:

| Band | Required response | Who approves | Review handling |
|---|---|---|---|
| Red | Strategy *Mitigate*, *Research* or *Elevate* (never *Watch* or *Accept* while active); at least two active mitigation steps; at least one trigger; fallback stated; status never *Watch* | Owner approves the plan at the first gate review at which the risk is Red, recorded in that review's `decision-memo.md` and transcribed into `mitigation.plan_approval` (decision memo path and date); between reviews the approval is given in chat and transcribed into the ADR decision section or the CR disposition block of the change that carries the plan (charter §4 item 4), which `plan_approval` then names. `tools/render_risk.py --gate` rejects a Red risk that was assessed at an earlier gate review and has no `plan_approval` | One slide per Red risk at every review with its plan status (section 9, Communicate). A Red risk still open at CDR makes the CDR disposition at most *Approved with liens* unless the owner records acceptance |
| Yellow | At least one trigger; mitigation steps, or strategy *Watch* | Claude plans; owner sees the list at the review | Listed at every review; discussed on request |
| Green | At least one trigger; *Watch* with closure criteria | Claude | Listed at every review |

**Acceptance.** Only the owner sets *Accepted*, and only with an `acceptance` record naming the decision memo, the ADR decision section or the CR disposition block that records the decision (charter §4 item 4), the date, and the residual score, which equals the risk's `score` at acceptance (checked by the tool). Accepted risks keep rendering in the register so that the residual is never hidden (SWE-086 note on residual risk), and keep at least one trigger that re-opens them.

**Single point failures.** At CDR (App. G Table G-7 item 6.32, rationale for acceptance) and at SAR (Table G-11 item 3.14, Table G-12 item 12) every single point failure in the SPF section of `docs/safety/hazard-analysis.md` that the owner accepts is recorded as one risk tagged `spf` with status *Accepted* and an acceptance record; the SPF table row cites that `RSK-NNN`.

## 9. Continuous risk management steps

The six steps are performed for every risk; the table names the artifact each step consumes or produces.

| Step | Activity | Inputs consumed | Output produced | Who | When |
|---|---|---|---|---|---|
| Identify | Write the four-part statement and title; take the next free `RSK-NNN` (never reused, charter §6); set `status: Proposed`, `source`, `opened`, `horizon`, `category`, `tags`. Dispose of every candidate risk named in another artifact (disposition rule below) | Stakeholder inputs `SI-NNN`, requirements and TBR list, hazard analysis, ConOps section 8, research reports in `docs/research/`, trade studies, simulation and analysis reports, vendor DFM reports, tool validation results, RFAs and RIDs, NCRs, lessons learned, review discussions | New entry in `docs/risk/register.json`; `candidates` entries | Claude; any agent may propose a risk in its structured result | Continuously; formally at every review and on every trigger |
| Analyze | Assign likelihood with anchor, five consequence levels with rationale, confidence; compute score; fill `related` ids | Sections 6 and 7; the evidence named in the condition | Populated entry; first `history` record (with `safety`) | Claude, then independent reviewer check; status moves *Proposed* to *Open* when the reviewer's filled checklist `docs/reviews/<REVIEW>/checklists/risk-register.md` (front matter `id: INSP-NNN`, charter §5; `<REVIEW>` is the next gate) records the risk as passing | Same session as Identify; reviewer before the next review |
| Plan | Choose strategy; write steps (action, artifact, due gate, status), triggers (observable condition, response with actor and timing), fallback, closure criteria | Band table of section 8; cost model; milestone list | `mitigation` object; for Red, `plan_approval` after the owner approves | Claude; owner approval for Red plans | Before the next review |
| Track | Re-score, append a `history` entry (with `safety`), update `trend`, `last_assessed`, step statuses; recompute aggregate risks from children | Analysis results, test results, vendor status, TPM data (`docs/plan/tpm.json`), trigger polls (section 10.3) | Updated entry; rendered `docs/risk/register.md` | Claude | At every review and on every trigger (section 10) |
| Control | Decide: continue, change plan, close (closure criteria met), accept, retire, or realize (open `NCR-NNN` or `CR-NNN`, name it in `related`, and add to `docs/lessons-learned.md`) | Tracked status; owner disposition | Status change per the transition table below; for accept, retire or close, a decision memo entry | Owner decides; Claude executes | At every review; between reviews only through a trigger response that the plan already names |
| Communicate | Render the register; include in `docs/reviews/<REVIEW>/package.md` the matrix, the ranked list, the per-review measures table (section 12), changes since the previous review, Red risks with plan status, risks proposed for closure or acceptance, the candidate dispositions since the previous review, and the App. G evidence of section 10.1; present the risk slides in `docs/reviews/<REVIEW>/slides/<review>.adoc` (charter §4 item 2): the matrix, the ranked list, the measures plot and one slide per Red risk with its plan status | Rendered register; previous package | Risk section of the review package; risk slides; owner decisions in `decision-memo.md` | Claude | Every review package (charter §4 item 1 names risk status as package content) |

**Candidate disposition rule (Identify).** Every candidate risk named in another artifact (ConOps section 8, the risk lists of `docs/research/*.md`, the hazard analysis register-linkage table, review minutes, RFA answers) receives exactly one disposition in the `candidates` array of `docs/risk/register.json`: *Entered* (it became a new `RSK-NNN`), *Merged* (it is folded into an existing `RSK-NNN` whose `source` names the candidate id, with a rationale and a `history` note on that risk), or *Declined* (not a risk, with a rationale of at least 20 characters that names the condition that would re-open it). The candidate keeps the id its source artifact gives it. `tools/render_risk.py` checks that every Entered or Merged candidate names an existing risk whose `source` contains the candidate id, and renders the dispositions. Status: the ConOps section 8 pass was completed on 2026-09-25 (17 candidates: 6 Entered, 8 Merged, 3 Declined); Claude runs the pass over the risk lists of every report in `docs/research/` and over the hazard analysis section 12 table before the SRR readiness declaration (`01-lifecycle-and-reviews.md` section 3.1), and repeats it for every new research report the day it is committed.

**Status transitions.**

| From | To | Condition | Who |
|---|---|---|---|
| (new) | Proposed | Identify and Analyze done | Claude |
| Proposed | Open | The reviewer's INSP record (Analyze row) passes the risk | Reviewer, then Claude sets the status |
| Open | Mitigating | The first mitigation step is InProgress or Done | Claude |
| Open or Mitigating | Watch | Only when the band is Yellow or Green and the remaining plan is triggers only (the tool rejects a Red risk in *Watch*) | Claude; owner sees it at the next review |
| Watch | Mitigating | A trigger fires and its response starts a step | Claude |
| Any active status | Accepted | Owner decision with an acceptance record (section 8) | Owner |
| Any active status | Realized | The departure occurs; `NCR-NNN` or `CR-NNN` named in `related` | Claude |
| Realized | Closed | The NCR or CR that handles the consequence is closed and the closure criteria are met | Owner at the next review |
| Any active status | Closed | Closure criteria met, recorded in the decision memo | Owner |
| Any status | Retired | The condition no longer applies; owner concurrence and a rationale in the `history` note | Owner |

**Software risks (SWE-086).** Software risks (category software or tag software, section 5) follow the same six steps in the same register. `docs/risk/register.md` lists them in the summary row "Software risks (SWE-086 record)". The register history together with the review packages constitutes the record of continuous risk management for software listed in NPR 7150.2D Chapter 6 (§6.1 item r).

## 10. Cadence, review criteria, triggers and trigger poll

Reviews are event-based (charter §3). The register is updated:

1. **At every life-cycle review.** Full Track and Communicate pass over every active risk, recorded with `review: <REVIEW>` in `history` and `last_assessed` (`tools/render_risk.py --gate <REVIEW>` rejects an active risk last assessed before the gate). The review package states, for each row of Table 10-1 for that gate, which register entries provide the evidence.
   **At every delta TRR** (`TRR-Dn`, charter §3; `01-lifecycle-and-reviews.md` section 7.6): a Track pass limited to the risks whose triggers, steps or closure criteria name the run-for-record series being authorized, recorded with `review: TRR-Dn` in `history` and `last_assessed`. For the on-air delta TRR this includes every risk tagged `regulatory`; the OnAir authorization of `04-verification-and-validation.md` section 6.3 names the residual risk it accepts by `RSK-NNN`.
2. **When a trigger fires** (section 10.2). Claude, in the same working session, re-scores every affected risk, appends a history entry, executes the trigger response named in the plan, and opens new risks as needed. Trigger responses that require money, a purchase or a schedule change are proposed to the owner and executed only after the owner's answer is recorded.
3. **At every trigger poll** (section 10.3).

### 10.1 Review criteria the register evidences

Table 10-1. App. G risk criteria of the five gates and of the reviews they absorb (charter §3: SRR absorbs MCR, PDR absorbs SDR, TRR absorbs SIR, SAR absorbs ORR and FRR). Item numbers follow the notation of `01-lifecycle-and-reviews.md` (entrance `6.4` = item 6 sub-item 4; success `s6`). The criterion column uses the wording of the 01 row where 01 carries the item.

| Gate | App. G criterion | 01 row | Criterion (01 wording) | Register evidence in the package |
|---|---|---|---|---|
| SRR | G-4 6.4, 6.5; G-3 5.5 | 4.3 row 11 | Risk management approach ready to baseline; risk assessment with mitigations | This document approved (header); matrix and ranked list; every active risk with a plan meeting section 8; the `cyber`-tagged list (G-3 5.5 names system security including cybersecurity) |
| SRR | G-4 s6 | 4.4 row 6 | Major risks identified, assessed, with viable mitigations | Every Red and Yellow risk with likelihood and consequence rationale, a plan meeting section 8 and an INSP record from the SRR reviewer; candidate dispositions complete (section 9) |
| SRR | G-3 s11 | not carried by 01 | (project wording) Risk and mitigation strategies identified and acceptable based on technical risk assessments | Same evidence as G-4 s6 plus the owner's plan approvals (`plan_approval`) of every Red risk in the SRR decision memo |
| SRR | G-3 5.10; G-4 s14 | 4.3 row 15; 4.4 row 11 | Single point failure and fault tolerance philosophy stated; reflected in requirements | Hazard analysis fault-tolerance section; every hazard carried by a risk (hazard link rule) |
| PDR | G-5 6.3, 6.4; G-6 6.5 | not carried by 01 (row 19 carries the SEMP update only) | (project wording) Updated risk management plan; updated risk assessment and mitigation | This document re-approved in the PDR decision memo; register rendered with the PDR Track pass |
| PDR | G-6 s7; G-5 s6 | 5.4 row 6 | Risks credibly assessed with plans and resources | Every Red risk Mitigating or with its first step due at PDR InProgress, `plan_approval` present, REQ or HZ link present (section 11); measures table |
| PDR | G-6 s4 | 5.4 row 3 | Preliminary design expected to meet requirements at acceptable risk | Red and Yellow risks against the preliminary design with their analysis steps' status |
| PDR | G-6 s5 | 5.4 row 4 | Interface definitions consistent with maturity; interface risks acceptable | Risks whose asset is an interface (ICD) and every `cyber`-tagged risk (G-6 s5 names system security) |
| PDR | G-6 6.26 | 5.3 row 11 | List of potential single point failures | Hazard analysis SPF list with the risk carrying each hazard |
| PDR | G-6 6.25, s21; G-5 s14 | 5.3 row 21; 5.4 row 16; 3.5 (SCRM customized) | Procurement status: part availability and lead times; single-source parts in the risk register | `single-source`-tagged list with its stock-check steps |
| CDR | G-7 6.16 | 6.3 row 13 | Risk assessment and mitigation updated | Register rendered with the CDR Track pass |
| CDR | G-7 s8 | 6.4 row 6 | Risks to safety and mission success understood and managed | Every Red risk with its plan status and `plan_approval`; every risk carrying a hazard with its verification steps assigned |
| CDR | G-7 s9 | 6.4 row 7 (safety part) | (project wording for the residual-risk clause) Safety, reliability and system security residual risks at an acceptable level | Residual score of every risk tagged `cyber` or carrying a hazard, with the owner's disposition in the CDR decision memo |
| CDR | G-7 6.32 | 6.3 row 21 | List of all single point failures with effects and acceptance rationale | One `spf`-tagged Accepted risk per accepted SPF (section 8) |
| CDR | G-7 6.31, s20 | 6.3 row 20; 3.5 (SCRM customized) | Procurement status: every BOM line in stock at DigiKey or with an approved alternate | `single-source`-tagged risks with the CDR stock re-query step Done |
| TRR | G-10 s5, s6 | 7.4 row 3 | Risks identified, assessed, mitigated; residual risk accepted by the owner | Every risk whose steps or triggers name the campaign; acceptance record for every residual Yellow or Red risk the campaign carries |
| TRR | G-9 s4 | not carried by 01 (row 8 cites G-9 s2 only) | (project wording) Risks identified and accepted by the owner, as required, before integration | Same acceptance records, limited to the integration and bring-up risks (RSK-008 children) |
| SAR | G-11 3.9 | 8.3 row 11 | Risk assessment updated; residual risks stated for operations | Register rendered with the SAR Track pass; every risk with horizon Ops listed with its residual |
| SAR | G-11 s2; G-12 s6 | 8.4 row 2 | Risks mitigated to acceptable levels; residual risk accepted by the owner | Every active risk Closed, or Accepted with an acceptance record in the SAR decision memo |
| SAR | G-11 3.14; G-12 12; G-13 10 | 8.3 row 17 | Single point failure list updated with test evidence | `spf`-tagged Accepted risks updated with the test evidence of their SPF |
| SAR | G-13 s8, s10 | not carried by 01 | (project wording) Residual risk from open items and waivers, and from open safety and mission risk items, deemed acceptable | Acceptance record for every risk tied to an open NCR, waiver or lien, and for every risk carrying a hazard |

### 10.2 Triggers

| Trigger event | Where it is observed |
|---|---|
| A risk-specific trigger condition in `mitigation.triggers` is met | Analysis reports, test logs, procurement checks, trigger polls |
| A new hazard or a changed hazard control | `docs/safety/hazards.json` |
| A change request, or requirements volatility MSR-02 above 10 percent (`07-software-engineering-plan.md` section 11; TPM-012) | `CR-NNN`; `tools/traceability.py --volatility --from <baseline tag>` (planned for PDR, 07 section 11) |
| A nonconformance | `NCR-NNN` |
| A TPM or margin outside its threshold | `docs/plan/tpm.json` |
| A vendor notice (DFM finding, lifecycle change, price or lead-time change) | Procurement records; trigger poll |
| A simulation or analysis result outside the margin required by its requirement | `docs/design/analysis/` |
| A tool validation failure or toolchain change | `tools/toolchain.lock.md`, `docs/cm/tool-validation/TV-NNN-<tool>.md` (05 section 9.2) |
| A RID or RFA whose closure changes a design or plan | `docs/reviews/<REVIEW>/rfa-rid-log.json` |
| A new research report or candidate risk in another artifact | `docs/research/`; the artifact (section 9 disposition rule) |
| The owner names a concern in conversation | Recorded as `source` with the date |

### 10.3 Trigger poll

SE HB §6.4 (Figure 6.4-3) includes monitoring the status of each technical risk periodically. Triggers whose observation point is outside the repository (distributor stock and manufacturer lifecycle status, vendor notices, upstream tool releases and issue trackers, the eCFR and FCC guidance) are polled by Claude at every milestone of `docs/plan/schedule.md` and, from PDR to SAR, at least every 14 days. Each poll appends to every risk with such a trigger a `history` entry with the note `trigger poll: <what was checked, with the date and source>` and `review` set to the last gate passed (Pre-SRR before SRR), and updates `last_assessed`. A trigger found to have fired is handled by item 2 of this section in the same session.

## 11. Register fields

The schema `docs/risk/schema.json` is normative. Field summary:

| Field | Content | Rule |
|---|---|---|
| `id` | `RSK-NNN` | Unique, never reused |
| `title` | Noun phrase, 80 characters or fewer | Names the departure |
| `statement` | `condition`, `departure`, `asset`, `consequence` | Section 4 |
| `category` | One of section 5 | Exactly one |
| `tags` | Optional lowercase labels of section 5 (`software`, `cyber`, `hsi`, `single-source`, `regulatory`, `aggregate`, `cm`, `spf`) | Never replaces `category`; `software` required by the section 5 artifact rule; `aggregate` enables the tool's likelihood check |
| `likelihood`, `likelihood_rationale` | 1 to 5 and the anchor used | Section 6 |
| `consequence`, `consequence_rationale` | Five levels and the reason for the driving dimension | Section 7 |
| `score` | likelihood x max(consequence) | Checked by the tool |
| `assessment_confidence` | Low, Medium, High | Section 3 |
| `owner` | Robin or Claude: who drives the plan | Acceptance is always Robin's |
| `source`, `opened`, `horizon`, `last_assessed` | Provenance and timing; `source` names every merged candidate id; `last_assessed.review` and `history[].review` are Pre-SRR, SRR, PDR, CDR, TRR, `TRR-Dn`, SAR or Ops | Dates YYYY-MM-DD; `last_assessed` equals the date and review of the last `history` entry |
| `mitigation` | `strategy`, `steps[]` (id, action, artifact, due gate, status, evidence), `triggers[]` (condition, response), `fallback`, optional `plan_approval` (decision memo, date) | Section 8 minimums by band; `plan_approval` for Red risks from their first gate review |
| `status` | Proposed, Open, Mitigating, Watch, Accepted, Realized, Closed, Retired | Section 9 transitions; `acceptance` required when Accepted; NCR or CR required when Realized |
| `acceptance` | `decision_memo`, `date`, `residual_score` | Section 8; `residual_score` equals `score` |
| `trend` | New, Increasing, Stable, Decreasing, Closed | Computed from the last two history scores |
| `related` | `requirement_ids`, `hazard_ids`, `adr_ids`, `trade_study_ids`, `tpm_ids`, `ncr_ids`, `cr_ids`, `stakeholder_input_ids`, `risk_ids` | Charter §6 formats; every Red risk has at least one REQ or HZ link by PDR |
| `closure_criteria` | The evidence that closes the risk | Verifiable |
| `history[]` | Append-only assessment log: date, review, likelihood, max consequence, `safety`, score, status, note | Last entry equals current values, including `safety`; review points never go back in the life cycle |
| `candidates[]` (top level) | `id`, `source_artifact`, `summary`, `disposition` (Entered, Merged, Declined), `risk_id`, `rationale`, `date` | Section 9 disposition rule |

## 12. Tooling

`tools/render_risk.py` (standard library; JSON Schema validation added when `jsonschema` is importable, which it is in `.venv`) validates `docs/risk/register.json` and writes `docs/risk/register.md`. It rejects a register with any error of its `validate_risk`, `validate`, `validate_candidates` and `check_hazards` functions: id format and uniqueness, level ranges, score consistency; plan minimums by band, including the Red strategy rule (Mitigate, Research or Elevate), at least two active steps for Red, a trigger on every active risk, no Red risk in *Watch*; the Low-confidence rule of section 3; the software-tag artifact rule of section 5; the acceptance record with `residual_score` equal to `score`; the NCR or CR of a *Realized* risk; trend, history and `last_assessed` consistency (date, review, `safety`); related-id formats; `tags` format; review points including `TRR-Dn`; the aggregate-likelihood rule for risks tagged `aggregate`; the candidate disposition rule; and, for risks last assessed at PDR or later or whenever `--gate` is PDR or later, a Red risk without a REQ or HZ link. With `--gate <REVIEW>` it also rejects an active risk last assessed before that gate and a Red risk assessed at an earlier gate review without `plan_approval`. With `--hazards docs/safety/hazards.json` it applies the hazard link rule of section 1 (coverage of every hazard with unverified controls, the two-way link, safety at least the mapped severity). With `--check` it writes nothing, renders in memory and fails with "register.md is stale; run without --check" when `docs/risk/register.md` differs from the fresh render.

The rendered file carries: the summary with the SWE-086 record row (category software or tag software, section 9) and one row per tag; the per-review measures table (technical risk status measurements, SE HB §6.4.1.1: active risks by band, opened, closed or retired, accepted, open steps due at the gate being prepared and open steps overdue against their due gate), which the review package plots under `docs/reviews/<REVIEW>/figures/`; the 5x5 matrix with `RSK` ids in the cells, safety-override risks marked "(R by safety override)"; the ranked list (band, then safety consequence 5 first within a band, then score); the candidate dispositions; and a detail block per risk. The matrix table is the "rendered matrix" named in charter §5.

Commands (run from any directory; the interpreter must be the project venv so that the schema check runs):

| Purpose | Command | When |
|---|---|---|
| Render after an edit | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py` | Every edit of `register.json`; the render is committed with the JSON |
| Reviewer and CI check | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py --check` | Before every commit and by the reviewer (section 16 item 1) |
| Review package check | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py --check --gate <REVIEW> --hazards /Users/robinonsay/rust/cwht/docs/safety/hazards.json` | Before the readiness declaration of every gate; mandatory from the SRR readiness declaration, by which the hazard analysis back-links of section 17 are complete |
| Known-answer tests | `/Users/robinonsay/rust/cwht/.venv/bin/python -m unittest discover -s /Users/robinonsay/rust/cwht/tools/tests` | Every change of the tool, the schema or this document's rules |

**Tool validation (SWE-136; charter §8).** `tools/render_risk.py` is a class B evidence-generating tool (05 section 9.1). Its known-answer test is `tools/tests/test_render_risk.py` on `tools/tests/fixtures/risk/`: `valid.json` renders to the stored `valid.md` and passes `--check`, `--gate SRR` and `--hazards`; `stale.md` fails with the stale message; band edges (scores 4 and 5, 10 and 12), the safety override at L1 and L2, the aggregate rule, the measures table and the ranking are checked; and each seeded fault of `faults.json` and of the gate and hazard tests fails with exactly its expected error string. The row is in `tools/toolchain.lock.md` section 1.1. The TV record `docs/cm/tool-validation/TV-NNN-render-risk.md` (procedure of 05 section 9.2) is due at SRR together with the other Python tools (RMM row SWE-136); until the owner accredits it, the rendered register is developer evidence only (07 section 8.3).

## 13. Risk-informed decision making

Risk information enters every formal trade study (section 14) in three ways:

1. **Criteria.** Every trade study considers the five consequence dimensions of section 7 (safety, first power-on, cost, schedule, performance margin) and system security (cybersecurity; the attack surfaces of `07-software-engineering-plan.md` section 16.2), which together cover the impacts NPR 7123.1D §3.2.18.2 names (health and medical impacts are carried by the safety dimension). Each is either used as a criterion or recorded in the template's "Criteria considered" line (section 3.1) as omitted, with the reason.
2. **Per-alternative risk assessment.** For every alternative that passes the mandatory criteria, the author lists its risks in the four-part format with likelihood and consequence on the scales of sections 6 and 7. The alternative's aggregate risk is the maximum score among its risks and appears in the Risk and Benefits section of the report. An alternative with a Red safety risk that no identified step reduces to Yellow fails a mandatory criterion.
3. **Register update.** The risks of the selected alternative are entered into the register with `related.trade_study_ids` on the day the decision is recorded (charter §11 rule 6), and any risk that motivated the study gets a history entry naming the `TS-NNN`.

## 14. Decision analysis

### 14.1 Decision classes

| Class | Definition | Record | Decision authority |
|---|---|---|---|
| 1. Formal trade study | Any of: (a) an architecture choice (receiver topology, PA topology, LO scheme, power architecture, firmware task structure, enclosure concept); (b) selection of a single-source or critical part (RF power device, synthesizer, TCXO, CW filter, battery cell and charger, display); (c) any choice touching a hazard in `docs/safety/hazards.json` or a component listed in `docs/process/07-software-engineering-plan.md` section 14.1 (the single authoritative list of safety-critical and mission-critical components, charter §10); (d) the owner asks for one (RFA or in chat); (e) the mitigation approach for a Red risk when more than one candidate exists; (f) a change to a KDR requirement or an MOE; (g) a verification approach that substitutes Analysis for Test on a regulatory requirement; (h) a software acquisition-versus-development decision (SWE-033): the runtime, HAL or PAC crates, and any OTS or OSS component used in a component of 07 section 14.1 | `docs/decisions/trade-studies/TS-NNN-*.md` from the template, followed by one ADR that records the decision; for (h) the report is the NPR 7150.2D §6.1 item t record | Owner |
| 2. ADR only | Any other choice that constrains later work (charter §11 rule 6): selection of a library or crate used outside the components of 07 section 14.1, pin assignment, naming and repository structure, coding-standard details, a component value with one reasonable option, a process convention | `docs/decisions/adr/ADR-NNN-*.md` | Owner when the ADR changes a baseline or spends money; otherwise Claude records and the owner sees it in the next review package |
| 3. No record | A reversible choice with no downstream constraint | none | Claude |

When in doubt between classes 1 and 2, the choice is class 1 if reversing it after CDR would cost more than USD 100 or two weeks.

### 14.2 ADR versus trade study

| Aspect | ADR (`ADR-NNN`) | Trade study (`TS-NNN`) |
|---|---|---|
| Purpose | Record a decision and its rationale so that later work is constrained knowingly | Evaluate alternatives against weighted criteria with uncertainty, and recommend |
| Trigger | Class 2 choice, or the conclusion of a class 1 study | Class 1 choice |
| Length | One page: context, decision, alternatives considered in one line each, consequences, related ids | Full decision report per SE HB Table 6.8-1 (template `docs/templates/trade-study.md`) |
| Analysis content | Rationale; no scoring matrix | Criteria with operational definitions, weights, alternatives, weighted matrix, uncertainty and sensitivity statement, method limitations, per-alternative risks, recommendation, dissent, decision, lessons learned |
| Timing | Written the same day as the choice (charter §11 rule 6) | The `TS-NNN` file is created the same day the decision need is identified (charter §11 rule 6) with sections 1 to 3 drafted; decided before the gate that baselines the affected item |
| Review | Independent reviewer reads it before the next life-cycle review | Independent reviewer checks it before it goes to the owner with `docs/templates/peer-review-checklist-risk.md` section B, recorded in `docs/reviews/<REVIEW>/checklists/ts-nnn-<slug>.md` (lower case per the 01 section 13 slug rule, for example `ts-003-pa-topology.md`; front matter `id: INSP-NNN`; `<REVIEW>` is the next gate); dissent recorded in the report |
| Outcome linkage | May cite a `TS-NNN`; every `TS-NNN` produces exactly one ADR | Never changes a baseline by itself; a post-baseline change also needs a `CR-NNN` |
| Register linkage | `related.adr_ids` on any risk the decision creates or retires | `related.trade_study_ids` on the same |

### 14.3 Process steps

The steps follow SE HB §6.8.1.2.1 to §6.8.1.2.7 and the report content of §6.8.1.3.1; each names its section of the template.

| Step | SE HB | Activity | Template section | Who |
|---|---|---|---|---|
| 1 | §6.8.1.2.1 | State the decision needed, intended outcome, decision maker (owner), the gate by which it must be decided, and the constraints. Define criteria: mandatory (pass or fail) and enhancing, with the "Criteria considered" line of section 13 item 1; give every enhancing criterion an operational definition (a repeatable, measurable quantity) and a 1 to 5 scale with anchors; assign integer weights summing to 100 | 2, 3.1, 3.3 | Claude |
| 2 | §6.8.1.2.2 | Identify alternatives covering the decision space, including the do-nothing or current-baseline alternative when one exists; prune with a trade tree if more than five; record pruned alternatives with the reason | 3.2 | Claude |
| 3 | §6.8.1.2.3 | Select the evaluation method per criterion (simulation, budget analysis, datasheet comparison, cost query, prototype on the Pico 2 board, owner review) | 3.4 | Claude |
| 4 | §6.8.1.2.4 | Score every cell with linked evidence and a confidence (Low, Medium, High); apply mandatory criteria first and drop failing alternatives; compute weighted totals | 4, 5 | Claude |
| 5 | §6.8.1.2.5 | Write the uncertainty and sensitivity statement (section 14.4) and the limitations of the evaluation methods and tools; recommend one alternative, or the closely ranked set when the ranking is not robust; list the risks and benefits of each surviving alternative (section 13) | 6, 7, 8 | Claude |
| 6 | §6.8.1.2.6 | Independent review with `docs/templates/peer-review-checklist-risk.md` section B (the section 16 trade study items), recorded in `checklists/ts-nnn-<slug>.md` (section 14.2); dissent recorded; report presented to the owner in conversation or in the review package | 9 | Reviewer agent, Claude |
| 7 | §6.8.1.2.7 and §6.8.1.3.1 | Owner decides; the decision, its date and rationale are transcribed into the report and into the ADR; register updated. Capture the work products of every study (§6.8.1.2.7: guidelines and approach used, criteria, methods and tools, assumptions, uncertainties, sensitivities, lessons learned): the lessons-learned line of template section 10 names the entry appended to `docs/lessons-learned.md`, or "none" | 10 and the Change log | Owner, Claude |

### 14.4 Uncertainty and sensitivity statement

Every trade study contains the following, computed and stated explicitly:

1. **Weight sensitivity.** For each criterion, move its weight by plus and minus 10 points (clamped at 0) and rescale the other weights proportionally so that the sum stays 100; non-integer weights are allowed for the sensitivity run only. Report whether the top-ranked alternative changes.
2. **Score sensitivity.** For every cell with Low confidence, move the score by plus and minus 1 (within 1 to 5); report whether the top-ranked alternative changes.
3. **Robustness verdict.** *Robust* if no perturbation changes the top rank; otherwise *Not robust*, naming the perturbations that change it.
4. **Value of information.** If not robust: name the analysis or measurement that would raise the Low-confidence scores to Medium or better, its cost in time, and the gate it must precede; then either perform it before recommending or recommend the closely ranked alternatives for the owner's choice (SE HB §6.8.1.2.5).
5. **Method limitations.** State the limitations of the evaluation methods and tools used (model fidelity, tool accreditation status, datasheet-only evidence), as SE HB §6.8.1.2.5 asks the report to document.

### 14.5 Recommendation, dissent and decision

- The recommendation is a single alternative unless the robustness verdict is *Not robust* or two totals differ by less than 25 points (5 % of the 500 maximum); then the closely ranked alternatives are presented together.
- If the recommended alternative is not the highest total, the report explains why and the criteria or weights are revised with the owner's concurrence before the decision (SE HB §6.8.1.2.5).
- The independent reviewer's disagreement with criteria, weights, scores or the recommendation is recorded in the Dissent section with how it was addressed; the owner reads dissent before deciding.
- The owner's decision is recorded in section 10 of the report with date and rationale, in the ADR, and, when made at a review, in that review's `decision-memo.md`. Between reviews the ADR is the decision memo and states that the approval was given in chat and transcribed (charter §2).

### 14.6 Revisiting a decision

A decided trade study is reopened only when: a trigger in the register names it; a `CR-NNN` affects a criterion or a constraint; new information moves a Low-confidence score by two or more levels; or the owner asks. A decided trade study is immutable (05 Table 4-1 row 12): reopening opens a new `TS-NNN` (next free number, charter §6) that cites the superseded one; the only edit to the old file is its Status line, which becomes "Superseded by TS-MMM"; and a superseding ADR records the new decision. The template's Change log records revisions made before the decision only.

## 15. Compliance mapping

| Governing text | Item | Satisfied by |
|---|---|---|
| NPR requirement | NPR 7123.1D SE-19 (§3.2.14.1, ETA-approved Technical Risk Management process) | Sections 1 to 12; ETA approval record: header (approval in `docs/reviews/SRR/decision-memo.md`, re-approval at every gate); `docs/risk/register.json`; `tools/render_risk.py`; review packages |
| NPR requirement | NPR 7123.1D SE-23 (§3.2.18.1, ETA-approved Decision Analysis process) | Sections 13 and 14; ETA approval record: header; `docs/templates/trade-study.md`; `docs/decisions/` |
| NPR requirement | NPR 7150.2D SWE-086 (§5.2.1, all software risks and mitigation plans) | Section 5 (software risk = category software or tag software, enforced by the tool), section 9 (six steps, SWE-086 record row of `register.md`), section 8 (residual and accepted risks stay rendered), section 16 item 11 (software assurance audit) |
| NPR requirement | NPR 7150.2D SWE-154 (§3.11.3, cybersecurity risks and mitigations) | Cyber risks and their mitigations are `RSK` entries tagged `cyber` (RSK-015, RSK-022), mitigations planned as `REQ-SW-*` steps; 07 section 16.2 is the assessment |
| NPR requirement | NPR 7150.2D SWE-033 (§3.1.2, acquisition versus development) as far as a decision record is needed | Section 14.1 class 1 item (h): TS-NNN reports |
| NPR record | NPR 7150.2D §6.1 item r (records of continuous risk management for software) | Register history and review packages (section 9) |
| NPR record | NPR 7150.2D §6.1 item t (record of software engineering trade-off criteria and assessments, make/buy) | TS-NNN reports of section 14.1 class 1 item (h) |
| App. G criteria | NPR 7123.1D App. G Tables G-3, G-4, G-5, G-6, G-7, G-9, G-10, G-11, G-12, G-13 risk and single-point-failure criteria | Section 10.1 Table 10-1; evidence mapping in each review package |
| SE HB guidance | SE HB §6.4 (risk triplet, likelihood and consequence with uncertainty, scenario-based statements, periodic monitoring, technical risk status measurements §6.4.1.1) | Sections 3, 4, 6, 7, 10.3, 12 (measures table) |
| SE HB guidance | SE HB §6.8.1.2 activities, §6.8.1.3.1 report content, Table 6.8-1 | Sections 14.3 to 14.6; template |
| Charter | Charter §5 (register plus rendered matrix), §6 (ids), §8 (tool sanity check), §11 rule 6 (decisions recorded the same day) | Sections 11, 12, 14.1, 14.2 |

## 16. Reviewer checklists

The items below are carried, with the same numbers, as sections A (register, `CK-RSK-A1` to `A11`) and B (trade study, `CK-RSK-B1` to `B10`) of the template `docs/templates/peer-review-checklist-risk.md`, whose stem the record's `checklist` field names. The reviewer records each filled copy as the single peer-review record of its product (charter §5): the register record in `docs/reviews/<REVIEW>/checklists/risk-register.md` and each trade study record in `docs/reviews/<REVIEW>/checklists/ts-nnn-<slug>.md` (lower case, 01 section 13), each with `id: INSP-NNN` in its front matter. A change to an item here is made in the template in the same commit.

**Risk register (run before every review):**

1. `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py --check --gate <REVIEW> --hazards /Users/robinonsay/rust/cwht/docs/safety/hazards.json` exits 0 (validation, stale-render comparison, gate and hazard link rules in one command).
2. Every *Proposed* risk has been checked against sections 4 to 8 and moved to *Open*, or a defect is recorded as a RID.
3. Every statement has one departure or one family admitted by the section 4 family rule, a dated or cited condition, and no solution language.
4. Every likelihood rationale names its anchor; every consequence rationale names the driving dimension.
5. Every Red risk has at least two active steps with artifacts and due gates, one trigger with actor and timing, a fallback, a strategy of Mitigate, Research or Elevate, and, from its first gate review, a `plan_approval` naming the decision memo, ADR or CR that records the owner's approval.
6. Every Red risk has a REQ or HZ link (from PDR on).
7. Every hazard with unverified controls has a linked risk and the link is two-way.
8. Aggregate risks (tagged `aggregate`, with `related.risk_ids` children) have likelihood equal to the maximum of their active children; the tool enforces this, the reviewer confirms the child list is complete.
9. Every risk with a Low confidence has a Research strategy, a re-assessment trigger or a hazard-analysis step.
10. Changes since the previous review are listed in the package and match the history entries; every candidate named in an artifact committed since the previous review has a disposition.
11. **Software assurance audit (SWEHB SWE-086 tab 7, tasks 1 and 2).** The reviewer confirms that every software risk (category or tag software) has all six steps of section 9 evidenced (record, analysis, plan, tracking, control decision, communication in the package), confirms that the software risks of 07 sections 16.2 and 21 are all in the register, audits the risk management process for the software activities against this document, and records the result, including the software-risk list and the measures table, in the INSP record of the register checklist.

**Trade study (run before the report goes to the owner):**

1. The decision class rule of section 14.1 requires a trade study, and the decision maker and gate are stated.
2. Every enhancing criterion has an operational definition and a 1 to 5 scale with anchors; mandatory criteria are pass or fail; the "Criteria considered" line covers safety, first power-on, cost, schedule, performance margin and system security.
3. Weights are integers summing to 100 with a stated rationale.
4. Alternatives cover the decision space; the do-nothing alternative is present or its absence is explained; pruned alternatives are listed.
5. Every score cell links evidence and carries a confidence.
6. The weighted totals recompute correctly.
7. The uncertainty and sensitivity statement follows section 14.4, including method limitations, and its verdict is consistent with the recommendation.
8. Every surviving alternative has its risks listed in the four-part format on the section 6 and 7 scales.
9. The recommendation is the highest total, or the deviation is explained and the criteria revised.
10. The Dissent section is present (even if "none") and the Decision section is empty until the owner decides.

## 17. Alignment with the charter and sibling documents

Statements in other documents that this process relies on, and the reading adopted here (each is either satisfied by this document or listed for the named owner to resolve by the named point):

| Item | Where | Reading adopted or action |
|---|---|---|
| "risks tagged `software`" (record r) and "`RSK-NNN` tagged `cyber`" | 05 section 11 Table 6-1 row r; 07 sections 16.2 and 21 | Category software or tag software (section 5); `cyber` is a `tags` entry. No difference. |
| "the fallback recorded as risk `RSK` 'emulator fidelity'"; "residual risk RSK-010"; "`RSK-NNN` 'Part 97 compliance verified by analysis only'" | 07 section 9.4 item 3; 07 section 9.6 and the RMM row SWE-219; 04 section 6.3 | RSK-003, RSK-010 and RSK-011 respectively. No difference. |
| Software risks "opened in `docs/risk/register.json` at SRR by the software lead" | 07 section 21 | All seven rows are in the register: 'MC/DC tooling gap' RSK-010, 'Emulator fidelity' RSK-003, 'rustos driver effort' RSK-013, 'Complexity tool staleness' RSK-019, 'Toolchain not qualified' RSK-020, 'Flash write path' RSK-021, 'Single maintainer of rustos' RSK-023. No difference. |
| Debug port access as a cyber risk in the register | RMM row SWE-154; 07 section 16.2 row 'Debug access' | RSK-022 (tag `cyber`). No difference. |
| "The corpus is complete (267 pages)"; "Risk owner closes RSK-009 at SRR" | 07 section 22 | Superseded by the lead SE decision in RSK-009's history (2026-09-25): RSK-009 stays open to its PDR horizon, S1 due SRR, S2 and S3 due PDR. Action: 07 author rewords the row to "RSK-009 closes on its closure criteria (target PDR)" in 07's next revision, before the SRR readiness declaration. |
| "268 pages scraped" | Charter §1 row NASA-HDBK-2203 | The directory holds 267 files: 266 SWEHB pages plus the index `README.md` (count of 2026-09-25). Charter issue for the owner: correct §1 to "266 pages" by an editorial change before SRR. |
| Hazard `related_risk_ids` back-links | `docs/safety/hazards.json`; `docs/safety/hazard-analysis.md` section 12 | Action for the hazard analysis author, due before the SRR readiness declaration (then `--hazards` passes): set HZ-001 [RSK-016, RSK-030], HZ-003 [RSK-006, RSK-026], HZ-004 [RSK-024], HZ-005 [RSK-017], HZ-006 [RSK-016], HZ-009 [RSK-025], HZ-010 [RSK-024], HZ-011 [RSK-007, RSK-033], HZ-012 [RSK-016], HZ-013 [RSK-018], HZ-014 [RSK-015]; remove RSK-012 from HZ-004 and HZ-010 (split to RSK-024 on 2026-09-25); HZ-002, HZ-007 and HZ-008 are already correct. Added 2026-09-25 by the integrating session after `hazards.json` 0.2.0-pha: HZ-003 is now Critical, so RSK-006 and RSK-026 carry safety 4 (re-scored with history entries); HZ-015 (new) is carried by RSK-034, and the hazard analysis author sets HZ-015 `related_risk_ids` to [RSK-034], after which the section 12 `--hazards` check exits 0. |
| Standing criterion S7 "every risk has likelihood, consequence, mitigation, owner and trigger" | `01-lifecycle-and-reviews.md` section 3.2 | Section 8 now requires a trigger on every active risk and the tool enforces it. No difference. |
| App. G risk items not carried by 01 | `01-lifecycle-and-reviews.md` sections 4.4 to 8.4 | Table 10-1 carries G-3 s11, G-5 6.3 and 6.4, G-6 6.5, G-7 s9 (residual-risk clause), G-9 s4, G-13 10, s8 and s10 in project wording. Action for the 01 author, before the SRR readiness declaration: add these rows or record them as customized in 01 section 3.5. |
| Implementation references of SE-19 and SE-23 | `docs/process/se-compliance-matrix.json` rows SE-19, SE-23 | Resolved 2026-09-25: both rows name this document and `docs/reviews/SRR/decision-memo.md` as the ETA approval record; `render_compliance.py --check` exits 0. |
| Make/buy record | `docs/process/se-compliance-matrix.json` row SE-11 | Resolved 2026-09-25: SE-11 records the make/buy assessment as trade study TS-NNN 'Firmware runtime and HAL' followed by its ADR (section 14.1 class 1 item (h)). |
| Audio output limiting module | Charter §10 "audio output limiting"; 07 section 14.1 `SW-AUDIO` | RSK-017 and RSK-032 name `docs/requirements/sw/sw-audio/`. No difference. |
| Design-for-debug and producibility rules | Charter §5 names `docs/design/build-to-specification.md` and no separate file | Both live in sections of the build-to specification; procurement records live in `hardware/releases/<RELEASE-ID>/` (05 section 4.3); the cost model is `docs/plan/cost-estimate.md`. No difference. |
