# <REVIEW> Review Package

Template: `docs/templates/review-package.md`. Copy to `docs/reviews/<REVIEW>/package.md`. Replace every `<...>` token and delete no section; write "None" where a section is empty. Every claim links to a repository artifact with its commit hash (charter section 11 rule 2). Process: `docs/process/01-lifecycle-and-reviews.md`, called "the review process" below.

The package is the record of evidence. The review is presented from the deck `docs/reviews/<REVIEW>/slides/<review>.adoc` (charter section 4 item 2; review process sections 3.1 item 4 and 3.4). The deck is written from this file after it is complete, cites its sections, and never carries a claim this file lacks.

| Field | Value |
|---|---|
| Review | `<SRR / PDR / CDR / TRR / SAR / TRR-Dn>` |
| Package revision | `<1, 2, ...>` (incremented on re-review) |
| Package date | `<YYYY-MM-DD>` (the `T` of the review-trend computation, review process section 11) |
| Repository commit | `<full hash of the commit this package describes>` |
| Chair, Decision Authority, Technical Authorities | Robin |
| Presenter | Claude (main session) |
| Slide deck | `docs/reviews/<REVIEW>/slides/<review>.adoc` at commit `<hash>`; `<n>` slides rendered to `slides/png/slide-01.png` to `slide-<NN>.png` (details in the "Slide deck" block of section 2) |
| Independent reviewer records | `<n>` records, `<m>` open findings. Each record is the filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md` with front matter `id: INSP-NNN` (charter section 5; review process section 13; there is no `peer-reviews/` folder) |
| Prior review | `<REVIEW or None>`, dispositioned `<disposition>` on `<date>` (`docs/reviews/<PRIOR>/decision-memo.md`, `signed` key) |

## 1. Agenda

The review is presented slide by slide in this order (review process section 3.4). The minutes follow the slide numbers.

| # | Item | Package section | Slides | Presenter | Chair decision needed |
|---|---|---|---|---|---|
| 1 | Title, agenda, purpose and scope | 1 | `<01 to 02>` | Claude | Confirm agenda |
| 2 | Readiness declaration, roles and entrance checklist | 2, 3, 4 | `<NN to NN>` | Claude | Confirm |
| 3 | Changes since the last review | 5 | | Claude | Note |
| 4 | Product summaries and figures | 6, 7 | | Claude | Questions, RIDs, RFAs |
| 5 | Requirements and traceability status | 8 | | Claude | Questions, RIDs, RFAs |
| 6 | Hazards and safety | 9 | | Claude | Questions, RIDs, RFAs |
| 7 | TPM, margins, risks | 10, 11 | | Claude | Accept residual risk |
| 8 | Milestone and procurement status | 12 | | Claude | Note |
| 9 | TBD/TBR list and open decisions | 13 | | Claude | Accept plans; decide open items |
| 10 | Prior RFA/RID trend | 14 | | Claude | Accept plans |
| 11 | Independent reviewer findings awaiting adoption | 15 | | Claude | Adopt as RID / RFA / No action |
| 12 | Software status | 16 | | Claude | Note SA findings |
| 13 | Proposed tailoring, compliance summary, lessons learned | 17, 18, 19 | | Claude | Approve rows |
| 14 | Success criteria self-assessment and proposed liens | 20 | | Claude | Rule Met / Met with lien / Not met |
| 15 | Requested disposition | 21 | | Robin | Approved / Approved with liens / Not approved |

Success criteria for this gate are in review process section `<4.4 / 5.4 / 6.4 / 7.4 / 8.4>`, plus section 3.3. Purpose of the gate: `<one sentence from review process section n.1>`.

### 1.1 Slide map (charter section 4 item 2 minimum slide set)

Every entry has at least one slide. Every slide names the package section it summarizes (review process 3.2 S11).

| # | Minimum slide (charter section 4 item 2) | Package section(s) | Slide number(s) |
|---|---|---|---|
| 1 | Title and agenda | 1 | `<01>` |
| 2 | Purpose, scope and entrance-criteria status | 1, 2, 4 | |
| 3 | Products with evidence links and counts | 6, 7 | |
| 4 | Requirements and traceability status | 8 | |
| 5 | Hazards and safety | 9 | |
| 6 | Risks and TPMs | 10, 11 | |
| 7 | TBD/TBR and open decisions with recommendations | 13 | |
| 8 | RFA/RID trend from prior reviews | 14 | |
| 9 | Proposed tailoring and liens | 17, 20 (and the proposed liens of section 2) | |
| 10 | Requested disposition | 21 | |

## 2. Readiness declaration

- Traceability report: `docs/reviews/<REVIEW>/traceability-report.md` at commit `<hash>`, written by the command in review process section 3.1 item 2: `<PASS / FAIL>`.
- Review-trend TPM: zone `<Green / Yellow / Red>`, from `tools/review_trend.py --date <T> --package <REVIEW> --write` (review process section 3.1 item 3), exit status `<0 / 1>`; values in section 14.
- Hard entrance criteria not met: `<None / list>`.
- Soft entrance criteria not met and proposed as liens: `<None / RFA ids raised per review process section 3.1 item 5>`.
- Owner confirmation (transcribed verbatim): "`<wording>`" on `<YYYY-MM-DD>`.
- Delta TRR only (`TRR-Dn`): trigger per review process section 7.6 `<a / b / c>`; rows changed since `<TRR or TRR-Dn-1>`: `<list>`; unchanged rows are carried by reference.

**Slide deck** (review process section 3.1 item 4):

| Field | Value |
|---|---|
| Source | `docs/reviews/<REVIEW>/slides/<review>.adoc` |
| Render command | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/slides/render_deck.py /Users/robinonsay/rust/cwht/docs/reviews/<REVIEW>/slides/<review>.adoc` (exit `<0>`) |
| Outputs | `slides/<review>.html`; `slides/png/slide-01.png` to `slide-<NN>.png` (`<n>` slides; `slides/reveal.js/` is git-ignored) |
| Render commit | `<hash>` |
| Every PNG inspected (legible, nothing clipped, figures readable) | `<yes>`, on `<YYYY-MM-DD>` |
| Every slide claim present in this package | `<yes>` |

## 3. Roles

Mandatory for TRR and every `TRR-Dn` (review process 7.3 row 6). For other gates, write "Review process section 1 item 6 applies".

| Role | Who | Responsibilities in this review or campaign |
|---|---|---|
| Chair, Decision Authority, ETA, SMA TA; test director and bench operator (TRR) | Robin | `<chairs; dispositions; operates the bench and reads instruments>` |
| Presenter, package and deck author; test conductor (TRR) | Claude (main session) | `<presents; directs each step from the written procedure; records and evaluates>` |
| Independent reviewers and software assurance | Reviewer agent invocations `<ids>` | `<records listed in section 15>` |
| Rule | | No test step is executed without the written procedure (TRR) |

## 4. Entrance-criteria checklist

Standing criteria (review process section 3.2), followed by the gate table (section `<4.3 / 5.3 / 6.3 / 7.3 / 8.3>`).

| # | Criterion (short) | Gate | Evidence artifact | Commit | Status | Note or proposed lien id |
|---|---|---|---|---|---|---|
| S1 | Agenda and success criteria agreed | Hard | this file section 1 | `<hash>` | `<Met / Not met>` | |
| S2 | Prior RFAs and RIDs closed or on plan (every prior review) | Hard | `docs/reviews/*/rfa-rid-log.json` | `<hash>` | | |
| S3 | Independent review records complete | Hard | `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (front matter `id: INSP-NNN`) | `<hash>` | | |
| S4 | Traceability report passes | Hard | `docs/reviews/<REVIEW>/traceability-report.md` | `<hash>` | | |
| S5 | TBD/TBR list complete | Hard | section 13 | `<hash>` | | |
| S6 | Proposed tailoring listed | Hard | section 17 | `<hash>` | | |
| S7 | Risk register current | Hard | `docs/risk/register.json` | `<hash>` | | |
| S8 | TPM status current | `<Hard / Soft>` | `docs/plan/tpm.json` | `<hash>` | | |
| S9 | Visual products rendered and inspected | Hard | `docs/reviews/<REVIEW>/figures/` | `<hash>` | | |
| S10 | Lessons learned reviewed | Soft | section 19; `docs/lessons-learned.md` | `<hash>` | | |
| S11 | Review deck rendered and inspected; no slide claim absent from this package | Hard | `docs/reviews/<REVIEW>/slides/`; section 1.1; section 2 "Slide deck" | `<hash>` | | |
| 1 | `<gate row 1>` | `<Hard / Soft>` | `<path>` | `<hash>` | | |
| ... | | | | | | |

## 5. Changes since the last review

| CR or item | Product | Summary | Impact assessed (cost, schedule, margins, safety, interfaces, verification) | Owner approval |
|---|---|---|---|---|
| `<CR-NNN>` | `<path>` | `<one line>` | `<yes, link>` | `<date>` |

Approved products changed without a CR (editorial log, `Editorial:` trailer): `<None / list>`.

## 6. Product summaries

One block per product in the entrance table.

### 6.<n> `<Product name>`

- Path: `<path>` at `<hash>`. Maturity entering the review: `<Preliminary / Initial / Baseline / Approved / Updated / Final>`, using the review process section 1 item 5 terms. "Baseline" here means the entrance expectation: a final draft, ready to baseline.
- Independent review record: `docs/reviews/<REVIEW>/checklists/<slug>.md` (`id: INSP-NNN`); verdict `<APPROVED / NEEDS CHANGES>`; findings: `<n>` raised, `<m>` open (open ones listed in section 15).
- Summary (what it contains, what changed, what is open): `<3 to 8 lines>`.
- Key numbers (with units and margins): `<table or None>`.
- Requirements or items covered: `<ids>`.

## 7. Rendered figures

Every visual product cited above, embedded with its path. Claude inspected each figure before including it (charter section 11 rule 3).

| Figure | Path | Source artifact | Inspected on |
|---|---|---|---|
| `<title>` | `docs/reviews/<REVIEW>/figures/<file>.png` | `<hardware/kicad/... / hardware/sim/... / hardware/enclosure/...>` | `<date>` |

![<title>](figures/<file>.png)

## 8. Requirements and traceability status

Source: `docs/reviews/<REVIEW>/traceability-report.md` (review process section 3.1 item 2) at commit `<hash>`.

| Module | Requirements | Draft | Active | Verified | Closed | of which retired (tag `retired`) | With open TBR | Without verification case |
|---|---|---|---|---|---|---|---|---|
| `<SYS / RX / TX / PWR / CTL / ME / SW-<SUB>>` | | | | | | | | |
| Total | | | | | | | | |

Report summary: violations `<0 / n>`; warnings `<n>`; orphan requirements `<n>`; requirements without a parent or self-derived rationale `<n>`; verification cases citing no requirement `<n>`; hazards whose `requirement_ids` are not all traced `<n>`.

Verification method coverage (Test / Analysis / Inspection / Demonstration): `<n / n / n / n>`. Evidence-class coverage by credited report: `<Simulation n, HostUnit n, Emulation n, Inspection n, Bench n, OnAir n>`.

Requirements volatility since the last review (SWE-200, `TPM-012`): `<n changed / n total>`.

## 9. Hazards and safety

Source: `docs/safety/hazards.json` and `docs/safety/hazard-analysis.md` at commit `<hash>`.

| Hazard | Title | Severity, likelihood (initial risk) | Controls (`control_req_ids`) | Control verification cases | Verification status | Residual risk | Safety-critical software components (`firmware_role.components`) |
|---|---|---|---|---|---|---|---|
| `<HZ-NNN>` | | `<Critical, C (Serious)>` | `<REQ-...>` | `<TC-...>` | `<Planned / Active / Passed>` | | `<SW-SAFE / none>` |

Single point failures: `<n>` listed (hazard analysis SPF section); new since the last review: `<ids or None>`. Hazard changes since the last review: `<None / list>`. RF exposure evaluation (`docs/design/analysis/rf-exposure-evaluation.md`, HZ-001): `<status>`.

## 10. TPM and margin status

| TPM | Measure | Target | Threshold | Current | Margin | Trend vs last review | Zone |
|---|---|---|---|---|---|---|---|
| `<TPM-NNN>` | `<mass margin / power margin / flash / RAM / CPU / PA thermal / harmonic suppression / battery life / review trend>` | | | | | | `<Green / Yellow / Red>` |

The required leading indicators are mass margin `TPM-001` (SE-62), power margin `TPM-002` (SE-63) and review trend `TPM-003` (SE-64). They are always listed, from PDR with trend plots (review process 5.3 row 4).

## 11. Risk status

Rendered 5x5 matrix: `docs/reviews/<REVIEW>/figures/risk-matrix.png`.

| Risk | Statement (if ... then ...) | L | C | Mitigation | Trigger | Owner | Change since last review |
|---|---|---|---|---|---|---|---|
| `<RSK-NNN>` | | | | | | | `<new / up / down / closed>` |

Residual risks the owner is asked to accept at this gate: `<ids or None>`.

## 12. Milestone and procurement status

This is a fixed agenda item of every package (RMM row SWE-018 as tailored; review process section 2.1). It is judged for success criteria G-5 s14, G-6 s21 and G-7 s20 (procurement and supply chain risk management consistent with the development schedule), and at CDR also for G-7 s14 (EEE parts selected; planned delivery supports the build schedule).

| Milestone (`docs/plan/schedule.md`) | Planned trigger or date | Actual | Slip cause | Recovery |
|---|---|---|---|---|
| `<next gate / vendor order / delivery / firmware release>` | | `<date or pending>` | `<None / one line>` | `<None / one line>` |

Procurement (`hardware/bom/`): BOM lines `<n>`, in stock at DigiKey `<n>`, with approved alternate `<n>`, unresolved `<n>` (each unresolved line is a risk id or RFA id); PCBWay capability check `<done / pending>`; longest lead time `<n>` days against the milestone list.

## 13. TBD/TBR list and open decisions

TBDs in items to be baselined: must be zero.

| Item | Field | TBR value or range | Owner | Closure plan | Close by |
|---|---|---|---|---|---|
| `<REQ-...>` | | | | | `<PDR / CDR / TRR / SAR>` |

Open decisions for the owner, with recommendations:

| Id | Question | Options | Recommendation and rationale | Needed by | Owner ruling (filled at review) |
|---|---|---|---|---|---|
| `<OQ-<AREA>-NNN>` | | | | `<gate or date>` | |

## 14. Prior RFA/RID trend

One block per prior review, from `docs/reviews/*/rfa-rid-log.json` (review process section 3.2 S2; values and zone from `tools/review_trend.py`, review process section 11).

| Review | Type | Severity | Raised | Open | Verified pending | Closed | Withdrawn | Overdue |
|---|---|---|---|---|---|---|---|---|
| `<SRR>` | RID | Major | | | | | | |
| | RID | Minor | | | | | | |
| | RFA | Blocking | | | | | | |
| | RFA | Routine | | | | | | |

Review-trend TPM `TPM-003`, computed at `T` = package date: zone `<...>` (decided by rule `<1 / 2 / 3 / 4>` of review process section 11); closure_fraction_at_gate `<value at the <next gate> memo / undefined>`; age_open median `<n>` and max `<n>` days; age_closed median `<n>` days.

![Review trend](figures/review-trend.png)

Open items with closure plans (each carries `lien: true` in its log and is listed in the prior memo's liens table):

| Id | State | Assignee | Due | Plan | Evidence so far |
|---|---|---|---|---|---|
| `<RFA-SRR-003>` | | | | | |

## 15. Independent reviewer findings awaiting owner adoption

| Record and finding | Finding | Product | Proposed handling | Owner ruling (filled at review) |
|---|---|---|---|---|
| `checklists/<slug>.md#finding-<n>` (`INSP-NNN`) | `<one line>` | `<path or id>` | `<Adopt as RID Major / Minor / Adopt as RFA / No action>` | |

Claude records each ruling against the finding's `#finding-<n>` entry in its record (review process section 10.1).

## 16. Software status

SWE table for this gate: review process section `<4.6 / 5.6 / 6.6 / 7.5 / 8.6>` (the cwht customization of the SWEHB Topic 7.09 criteria, review process section 3.3 C5).

| SWE | Product or evidence | Artifact | Status | SA reviewer record |
|---|---|---|---|---|
| `<SWE-NNN>` | | `<path>` | `<Done / Partial / Open>` | `checklists/<slug>.md` (`INSP-NNN`) |

Metrics (source: `docs/plan/measurements.json`):

- requirements volatility since the last review (SWE-200, `TPM-012`): `<n changes / n requirements>`;
- static analysis findings: `<n>`;
- unit tests: `<n passed / n>`;
- coverage: `<value>`;
- MC/DC for safety-critical components: `<value>`;
- maximum cyclomatic complexity: `<value>`;
- open nonconformances by severity: `<...>`.

### 16.1 Software assurance findings

Every package carries the open software assurance findings and their state (`docs/process/07-software-engineering-plan.md` section 15).

| Finding | Product | Severity | State (Open / Fixed / Verified / Deferred) | Record |
|---|---|---|---|---|
| `<one line>` | `<path or id>` | `<Major / Minor>` | | `checklists/<slug>.md#finding-<n>` (`INSP-NNN`) |

## 17. Proposed tailoring

| Matrix | Row (SE-NN or SWE-NNN) | Proposed disposition (FC / T / NA) | Rationale | Preserved intent | Owner decision (filled at review) |
|---|---|---|---|---|---|
| `<rmm.json / se-compliance-matrix.json>` | | | | | |

## 18. Compliance summary

| Matrix | FC | T | NA | Proposed | Rows citing this review |
|---|---|---|---|---|---|
| `docs/process/se-compliance-matrix.json` | | | | | |
| `docs/process/rmm.json` | | | | | |

Cross-document actions of review process section 15 (SRR package; later packages list only those still open): `<item n: closed at <hash> / open, lien RFA id>`.

Deferred capabilities and descope options (`docs/conops/conops.md`): `<list or None>`.

## 19. Lessons learned since the last review

Source: `docs/lessons-learned.md` (review process 3.2 S10).

| Entry | Date | Lesson | Action taken or planned |
|---|---|---|---|
| `<entry id or heading>` | `<YYYY-MM-DD>` | `<one line>` | `<one line>` |

## 20. Success criteria self-assessment

| # | Success criterion (short) | Evidence | Presenter assessment | Chair ruling (filled at review) | Lien id |
|---|---|---|---|---|---|
| C1 | | | `<Met / Met with lien / Not met>` | | |
| ... | | | | | |

A *Met with lien* ruling names the Routine RFA raised for it (review process section 3.1 item 5 and section 12.2).

## 21. Disposition block (filled at the review)

- Session date(s): `<YYYY-MM-DD>`; minutes: `docs/reviews/<REVIEW>/minutes.md` (in slide order).
- Items raised this review: RIDs `<n>` (Major `<n>`, Minor `<n>`), RFAs `<n>` (Blocking `<n>`, Routine `<n>`); log: `docs/reviews/<REVIEW>/rfa-rid-log.json`.
- Disposition: `<Approved / Approved with liens / Not approved>`.
- Liens (id, owner, due, `blocks-order` for CDR; every item of this review still Open, Answered or Verified at signing, review process section 12.2): `<table or None>`.
- On-air delta TRR only: OnAir authorization recorded in decision memo section 9 (`docs/process/04-verification-and-validation.md` section 6.3): `<yes / not applicable>`.
- Owner statement (verbatim, with time): "`<wording>`".
- Decision memo: `docs/reviews/<REVIEW>/decision-memo.md`; baseline tag: `<baseline/<review> or none>`.
