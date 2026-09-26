# ADR-NNN: <decision title, as a noun phrase>

<!--
Architecture Decision Record template (charter section 5: docs/decisions/adr/ADR-NNN-<slug>.md;
charter section 11 rule 6: any choice that constrains later work becomes an ADR or a trade study
the same day). Copy this file to docs/decisions/adr/ADR-NNN-<slug>.md, allocate NNN as
max(existing) + 1, fill every section, delete the comments. An ADR records ONE decision.
A decision that compares alternatives against weighted criteria is a trade study
(docs/decisions/trade-studies/TS-NNN-*.md, SE HB section 6.8); the ADR then records the
chosen option and cites the TS. Accepted ADRs are never edited except to change Status to
Superseded and add the superseding ADR id; a changed decision is a new ADR.
-->

| Field | Value |
|---|---|
| ID | ADR-NNN |
| Status | Proposed \| Accepted \| Superseded by ADR-MMM \| Rejected |
| Date proposed | YYYY-MM-DD |
| Date decided | YYYY-MM-DD |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 1, item (a) to (g) named; trade study TS-NNN required) \| 2 (section 14.1 class 2) |
| Decision authority | Robin, when any of these holds: the choice is class 1 (06 section 14.1 items (a) to (g)); it changes or fixes baseline content, including functional-baseline content before SRR; it spends money; it accepts a risk or approves a Red-risk mitigation plan (06 section 8; charter section 4 item 4) \| Claude, only for a class 2 choice that meets none of these (the owner sees the ADR in the next review package) |
| Author | Claude (or the author agent invocation) |
| Independent reviewer | Reviewer agent invocation and date, with the checklist result (Pass / findings) |
| Life-cycle phase | Pre-A / A / B / C / D |
| Baseline affected | none \| baseline/srr \| baseline/pdr \| baseline/cdr \| baseline/sar |
| Change request | CR-NNN when the decision changes a baselined item, otherwise none |

## 1. Context

<!-- The problem or fork in the road, in at most 200 words. State what forces the decision now,
and what happens if it is not taken. Name the stakeholder inputs and expectations behind it. -->

- Driving inputs and expectations: SI-NNN, NGO-NNN, MOE-NNN, CON-NNN, OPS-NNN
- Requirements that constrain the decision: REQ-<MOD>-NNN (with the constraint each imposes)
- Hazards in play: HZ-NNN (or none)
- Research consulted: `docs/research/<file>.md`
- Guidance consulted: SE HB §x.y, SWE-NNN, SE-NN (only identifiers verified in `docs/references/md/`)
- Assumptions the decision rests on, and how and by when each is confirmed (SE HB §6.8.1.2.7 and §4.2.1.2.7: assumptions are captured with the decision)

## 2. Decision

<!-- One paragraph, active voice, present tense: "The keyer implements iambic mode B ..."
Include the values chosen (numbers with units) and the scope (which modules, which revision). -->

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | | |
| B | | |
| C | | |

<!-- A class 1 choice (06 section 14.1 items (a) to (g)) requires TS-NNN: cite it here and
keep this table to the option names and the one-line outcome. An ADR without a TS is admitted
only for class 2. Fill this table even when only one option is viable, and include "do
nothing" where it is an option (SE HB §6.8.1.2.2: document a decision matrix for a major
decision even if only one alternative is viable). -->

## 4. Consequences

### 4.1 Requirements created or changed

<!-- Every requirement this decision produces cites this ADR: allocated requirements in
source_ids as a supporting source; self-derived requirements (docs/process/02-requirements-and-traceability.md
section 2.3) with rationale starting "Self-derived:" and this ADR in source_ids.
List them so tools/traceability.py can be cross-checked against this table. -->

| Requirement | Relationship | Note |
|---|---|---|
| REQ-<MOD>-NNN | new, self-derived from this ADR | |
| REQ-<MOD>-NNN | value changed (TBR closed) via CR-NNN | before / after |

### 4.2 Interfaces, design and code

- ICDs affected (existing files changed; Class I after PDR): ICD-<A>-<B> (or none)
- Design elements created or changed: element ids in `docs/design/allocation.json`, schematic sheets, Rust module paths
- New `SW-<SUB>` modules created by this ADR (directories `docs/requirements/sw/sw-<sub>/` and `docs/test_cases/sw-<sub>/` are created in the same commit, 02 section 2.2): none \| SW-<SUB>
- ICDs created by this ADR (`docs/icd/ICD-<A>-<B>.md` from `docs/templates/icd.md`, created in the same commit, 02 section 3.5): none \| ICD-<A>-<B>

### 4.3 Verification and safety

- Verification cases to add or change: TC-<MOD>-NNN
- Evidence class implications (Simulation, HostUnit, Emulation, Inspection, Bench, OnAir; the `type` values of `docs/test_cases/schema.json`) and any instrument gap
- Hazard analysis update required: yes (HZ-NNN) \| no
- Safety-critical software scope (SWE-134 provisions) changed: yes \| no

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact
- Gate affected
- Risks opened, closed or re-scored: RSK-NNN
- TPMs affected: TPM-NNN with margin before and after

## 5. Compliance and tailoring

<!-- Does the decision touch an RMM row or the NPR 7123.1 compliance matrix? If yes, name the
row and the CR that records the tailoring. Otherwise write "none". -->

## 6. Decision record (the decision memo for this decision, charter section 4)

<!-- One of the two forms below, matching the Decision authority row. Form 1: Robin's disposition
transcribed verbatim from chat, with date; mandatory whenever the Decision authority row names
Robin (class 1; baseline content changed or fixed; money spent; risk accepted or Red-risk
mitigation plan approved), and for class 1 it cites the TS-NNN whose section 10 records the
same decision. Form 2: recorded by Claude, admitted only for a class 2 choice that meets none
of the Robin conditions, and named in the next review package; the owner may overturn it
there, which produces a superseding ADR. An ADR is Accepted only when this section holds one
of the two forms. -->

> Owner (YYYY-MM-DD): "..." (class 1: decision recorded in TS-NNN section 10)

or

> Recorded by Claude under 06 section 14.1 class 2 on YYYY-MM-DD; not class 1, no baseline content changed or fixed, no money spent, no risk accepted; presented at <SRR | PDR | CDR | TRR | SAR>.

## 7. Related

- Supersedes: ADR-MMM (or none)
- Superseded by: ADR-MMM (filled when Status changes)
- Trade study: TS-NNN (required for class 1; none only for class 2)
- Review where presented: SRR \| PDR \| CDR \| TRR \| SAR, with RFA/RID ids raised against it
