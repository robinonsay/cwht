# TS-NNN: <Decision title as a noun phrase>

<!--
Template for a cwht trade study (decision report). Content follows SE HB Table 6.8-1
(Typical Information to Capture in a Decision Report) and the process in
docs/process/06-risk-and-decision-analysis.md sections 13 and 14.
Copy to docs/decisions/trade-studies/TS-NNN-<slug>.md, take the next free TS number,
replace every <placeholder>, delete every comment. Keep the section numbers: the
reviewer checklist (process section 16) refers to them. A decided study is immutable
(05 Table 4-1 row 12): reopening it opens a new TS-NNN that cites this one, and the
only later edit to this file is its Status line (process section 14.6).
-->

| Field | Value |
|---|---|
| ID | TS-NNN |
| Status | Draft / In review / Recommended / Decided / Superseded by TS-MMM |
| Decision class trigger | <which item of process section 14.1 makes this study mandatory: (a) to (h); (h) makes this report the NPR 7150.2D section 6.1 item t make/buy record> |
| Decision maker | Robin (owner, Decision Authority) |
| Recommender | Claude (author) |
| Independent reviewer | INSP-NNN in docs/reviews/<REVIEW>/checklists/ts-nnn-<slug>.md, lower case (for example `ts-003-pa-topology.md`; 01 section 13 slug rule), filled from docs/templates/peer-review-checklist-risk.md section B (charter section 5; <REVIEW> is the next gate) |
| Decide by | <gate: SRR / PDR / CDR / TRR / SAR> because <what the gate baselines> |
| Related risks | <RSK-NNN that motivated the study or that the alternatives carry> |
| Related requirements and hazards | <REQ-*, HZ-NNN, SI-NNN> |
| Resulting ADR | ADR-NNN (filled when decided) |
| Dates | opened <YYYY-MM-DD>; recommended <YYYY-MM-DD>; decided <YYYY-MM-DD> |

## 1. Executive summary

- **Recommendation (one sentence):** <Alternative X because ...>
- **Problem requiring a decision (one sentence):** <...>
- **Robustness verdict (section 6):** Robust / Not robust
- **Owner's decision (section 10):** <pending / Alternative X on YYYY-MM-DD>

## 2. Problem and decision context

<!-- SE HB Table 6.8-1 "Problem/Issue Description": background, history, decision maker, team. -->

- **Mission and system context:** <which subsystem, which ConOps scenario OPS-NNN, which MOE or requirement is affected>
- **Decision needed and intended outcome:** <what will be true after the decision>
- **Constraints:** <imposed by SI-NNN, REQ-*, cost model, Part 97, owner's bench (SI-013), vendor capabilities>
- **Prior related decisions and lessons learned:** <ADR-NNN, TS-NNN, docs/lessons-learned.md entries, rustos experience>
- **Research consulted:** <docs/research/*.md, datasheets, references>

## 3. Decision matrix setup and rationale

<!-- SE HB Table 6.8-1 "Decision Matrix Setup Rationale": criteria, options, weights, evaluation methods, plus a copy of the setup matrix. -->

### 3.1 Criteria and operational definitions

Mandatory criteria are pass or fail; an alternative that fails any of them is dropped before scoring (SE HB §6.8.1.2.1). Enhancing criteria are scored 1 to 5 against the anchors below; every anchor is a repeatable, measurable quantity (SE HB §6.8.1.2.4).

| ID | Criterion | Type | Operational definition (what is measured, unit, method) | Scale anchors (1 / 3 / 5) | Weight |
|---|---|---|---|---|---|
| M1 | <e.g. Complies with 47 CFR 97.307(e)> | Mandatory | <pass if simulated margin >= 10 dB> | pass / fail | n/a |
| M2 | <e.g. No Red safety risk that no step reduces to Yellow (process section 13)> | Mandatory | <register scales> | pass / fail | n/a |
| C1 | <e.g. Performance margin> | Enhancing | <e.g. output power margin at 146 MHz, dB, LTspice> | <1: < 0 dB / 3: 1 dB / 5: >= 3 dB> | <w1> |
| C2 | <e.g. Unit cost> | Enhancing | <USD per unit at quantity 5, DigiKey query on date> | <1: > 40 / 3: 20 / 5: < 10> | <w2> |
| C3 | <e.g. Availability> | Enhancing | <stock at two distributors divided by project quantity> | <1: < 1x / 3: 3x / 5: >= 10x with an alternate> | <w3> |
| C4 | <e.g. Schedule impact> | Enhancing | <weeks added to the next gate> | <1: > 6 / 3: 2 / 5: 0> | <w4> |
| C5 | <e.g. First-power-on confidence> | Enhancing | <evidence class available before build: Simulation, HostUnit, Emulation, dev-board Bench (credit: false)> | <1: analysis only / 3: validated tool / 5: measured on hardware> | <w5> |
| | | | | **Sum of weights** | **100** |

Criteria considered (mandatory line, process section 13 item 1): safety <used as Cn / omitted because ...>; first power-on <used as Cn / omitted because ...>; cost <...>; schedule <...>; performance margin <...>; system security, cybersecurity per 07 section 16.2 attack surfaces <used as Cn / omitted because ...>.

Other criteria considered and not used, with reason: <list or "none">.

### 3.2 Alternatives

Alternatives cover the decision space (SE HB §6.8.1.2.2). The current baseline or do-nothing alternative is included, or its absence is explained.

| ID | Alternative | Description | Source (datasheet, reference design, research report) |
|---|---|---|---|
| A0 | <Do nothing / current baseline> | <...> | <...> |
| A1 | <...> | <...> | <...> |
| A2 | <...> | <...> | <...> |

Alternatives pruned before scoring (trade tree), with reason: <A3 ... because ...>.

### 3.3 Weight rationale

<Why each weight; which stakeholder input or requirement drives it. Weights are integers summing to 100. Name any weight the owner set directly.>

### 3.4 Evaluation methods

| Criterion | Method | Tool and version (tools/toolchain.lock.md) | Evidence artifact |
|---|---|---|---|
| C1 | <simulation / budget analysis / datasheet comparison / cost query / dev-board prototype / owner review> | <...> | <path> |
| C2 | <...> | <...> | <path> |

### 3.5 Setup matrix (before scoring)

| Criterion | Weight | A0 | A1 | A2 |
|---|---|---|---|---|
| M1 | n/a | | | |
| M2 | n/a | | | |
| C1 | <w1> | | | |
| C2 | <w2> | | | |
| C3 | <w3> | | | |
| C4 | <w4> | | | |
| C5 | <w5> | | | |

## 4. Scoring rationale

<!-- SE HB Table 6.8-1 "Decision Matrix Scoring Rationale": how each score was obtained. -->

Mandatory screening:

| Alternative | M1 | M2 | Result |
|---|---|---|---|
| A0 | pass / fail | pass / fail | kept / dropped |
| A1 | | | |
| A2 | | | |

Enhancing scores, one row per cell, with evidence link and confidence (Low / Medium / High):

| Criterion | Alternative | Measured value | Score (1 to 5) | Confidence | Evidence |
|---|---|---|---|---|---|
| C1 | A0 | <value and unit> | <n> | <L/M/H> | <path or URL with date> |
| C1 | A1 | | | | |
| ... | | | | | |

## 5. Final decision matrix

<!-- SE HB Table 6.8-1 "Final Decision Matrix". Weighted score = weight x score; total maximum = 500; percent = total / 5. -->

| Criterion | Weight | A0 score | A0 weighted | A1 score | A1 weighted | A2 score | A2 weighted |
|---|---|---|---|---|---|---|---|
| C1 | <w1> | | | | | | |
| C2 | <w2> | | | | | | |
| C3 | <w3> | | | | | | |
| C4 | <w4> | | | | | | |
| C5 | <w5> | | | | | | |
| **Total** | **100** | | **<T0>** | | **<T1>** | | **<T2>** |
| **Percent of maximum** | | | <T0/5> % | | <T1/5> % | | <T2/5> % |
| **Rank** | | | | | | | |

## 6. Uncertainty and sensitivity statement

<!-- Mandatory content per process section 14.4. Fill every line. -->

1. **Weight sensitivity.** Each weight moved by +10 and -10 points, clamped at 0, with the other weights rescaled proportionally to keep the sum at 100 (non-integer weights allowed for this run only): top rank changes for <none / criterion Cn at +10 / ...>.
2. **Score sensitivity.** Each Low-confidence cell moved by +1 and -1: top rank changes for <none / cell Cn-Am ...>.
3. **Assumptions and their evidence:** <list each assumption behind a score and what supports it>
4. **Robustness verdict:** Robust / Not robust because <...>.
5. **Value of information (if not robust):** <analysis or measurement that would raise the Low-confidence scores, its duration, the gate it must precede, and whether it was performed before the recommendation>.
6. **Limitations of the evaluation methods and tools (SE HB section 6.8.1.2.5):** <model fidelity, tool accreditation status per tools/toolchain.lock.md, datasheet-only evidence, anything the methods cannot show>.

## 7. Risks and benefits of the surviving alternatives

<!-- SE HB Table 6.8-1 "Risk/Benefits". Risks in the four-part format on the register scales (process sections 4, 6, 7). -->

| Alternative | Risk statement (Given ..., there is a possibility of ..., adversely impacting ..., leading to ...) | L | C (driving dimension) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| A1 | <...> | <1-5> | <1-5 (dimension)> | <n / Red, Yellow, Green> | RSK-NNN if selected |
| A2 | <...> | | | | |

| Alternative | Benefits beyond the scored criteria |
|---|---|
| A1 | <...> |
| A2 | <...> |

Aggregate risk per alternative (maximum score): A1 <n>, A2 <n>.

## 8. Recommendation

<!-- SE HB Table 6.8-1 "Recommendation and/or Final Decision" (recommendation part). -->

- **Recommended alternative:** <A1> with total <T1> (<percent> %).
- **Rationale:** <why; if not the highest total, the explanation required by process section 14.5 and the criteria revision agreed with the owner>.
- **Closely ranked alternatives presented for the owner's choice (if the verdict is Not robust or two totals differ by less than 25 points, 5 % of the 500 maximum):** <A2 ...> or none.
- **Impacts of adopting the recommendation:** requirements to derive or change <REQ-*>, interfaces <ICD-*>, cost model delta <USD>, schedule delta <weeks>, verification cases to add <TC-*>.
- **Corrective actions if the recommendation is adopted late:** <...>

## 9. Dissent

<!-- SE HB Table 6.8-1 "Dissent": recorded by the independent reviewer agent or the owner. Write "None recorded" if there is none; never delete the section. -->

| Who | Date | Dissent (criteria, weights, scores or recommendation) | How it was addressed |
|---|---|---|---|
| <reviewer, INSP-NNN> | <YYYY-MM-DD> | <...> | <matrix revised / risk added / owner informed / not accepted because ...> |

## 10. Decision

<!-- Filled only by transcription of the owner's decision (charter section 2). Left empty until then. -->

- **Decision:** <Alternative X / a different alternative / more alternatives requested>
- **Decided by:** Robin, on <YYYY-MM-DD>, <at review REVIEW / in chat, transcribed here and into ADR-NNN>
- **Rationale as stated by the owner:** <...>
- **Records produced:** ADR-NNN; decision memo <docs/reviews/<REVIEW>/decision-memo.md or "this ADR serves as memo">; register entries opened <RSK-NNN>; register entries updated <RSK-NNN>; CR-NNN if a baseline changed.
- **Revisit conditions:** <triggers per process section 14.6; a revisit opens a new TS-NNN>
- **Lessons learned (SE HB sections 6.8.1.2.7 and 6.8.1.3.1):** <entry appended to docs/lessons-learned.md, or none>

## 11. References

<!-- SE HB Table 6.8-1 "References". -->

- <SE HB, NPR, datasheet, research report docs/research/*.md, regulation clause, with version or date>

## Appendix A. Supporting analysis

<!-- SE HB Table 6.8-1 "Appendices": literature search results, lessons learned, previous related decisions and dissent, detailed data and risk analysis, decision metrics. -->

- **Literature and research search:** <what was searched, where (Claude Context queries, corpus sections), what was found>
- **Previous related decisions and dissent:** <ADR-NNN, TS-NNN>
- **Detailed analysis:** <simulation decks under hardware/sim/..., budget analyses under docs/design/analysis/, scripts with versions (tools/toolchain.lock.md), plots rendered into docs/reviews/<REVIEW>/figures/ and inspected (charter section 11 rule 3)>
- **Decision metrics:** <time from open to decision, number of alternatives, number of criteria revisions>

## Change log

Revisions before the decision only; after the decision the file is immutable except for the Status line (process section 14.6).

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | <YYYY-MM-DD> | Initial | |
