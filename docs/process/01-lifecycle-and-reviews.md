# cwht Life Cycle, Review Gates and RFA/RID Process

**Status:** Draft for SRR. **Expands:** charter (`docs/process/00-charter.md`) sections 3 and 4, including section 4 item 2 (every gate is a presented review from a controlled slide deck). **Owner of this document:** Robin (approves). **Author:** Claude (lead systems engineer). **Governing text:** NPR 7123.1D Chapter 5 and App. G; SE HB §3.11 and §6.7; NPR 7150.2D Chapters 3 to 5; SWEHB Topic 7.09 (software entrance and exit criteria, customized in section 3.3 C5).

This document is the cwht review plan required by NPR 7123.1D SE-32 and the customized entrance and success criteria required by SE-34. Where this document and the charter differ, the charter wins and this document is corrected.

---

## 1. Scope and conventions

1. The project holds five life-cycle reviews: **SRR, PDR, CDR, TRR, SAR**. Each is a control gate: work of the next phase does not start until the gate is dispositioned *Approved* or *Approved with liens* (section 12).
2. Reviews are **event-based** (NPR 7123.1D §5.1.5): a review is convened when every *Hard* entrance criterion in its table is met, never on a calendar date.
3. Combining reviews is *customization*, not tailoring; not holding a review is *tailoring* and needs a waiver or deviation for that review's minimum products (NPR 7123.1D §5.2.2.2; SE HB §3.11.4.3). The combinations below are recorded in the SEMP (`docs/plan/semp.md`) and in the compliance matrix (`docs/process/se-compliance-matrix.json`) as "FC, customized"; the two reviews not held are recorded there as T:
   - MCR is absorbed into SRR (its SE-35/36/37 products are SRR entrance products).
   - MDR/SDR is absorbed into PDR (its SE-40/41/42/43 products are PDR entrance products; SE-44 concerns programs other than single-project programs and is NA in the compliance matrix by the NPR's own Table H-1 rationale).
   - SIR is absorbed into TRR (SE-47 updated integration plan and SE-48 initial V&V results are TRR entrance products; the G-9 items carried are listed in the heading of section 7.3).
   - ORR is held, combined with SAR (customization; SE-69 preliminary V&V results are superseded by the full results). The ORR minimum products SE-51 (baselined decommissioning plans) and SE-52 (baselined disposal plans) are therefore due at SAR and are delivered there as the end-of-life section of `docs/ops/operations-handbook.md`. Putting them in a handbook section instead of stand-alone plans is customization (SE HB §3.11.4.2). They stay T in the compliance matrix (charter section 12) because the section is scoped down: it omits plan content that App. G Tables G-17 and G-18 expect. The relief is stated in section 3.5.
   - FRR is combined into SAR (customization under NPR 7123.1D §5.2.2.2, no waiver): its minimum products SE-53 baseline V&V results and SE-54 final certification for use are delivered at SAR as the V&V report and the acceptance plus Part 97 compliance statements; there is no separate flight event. Recorded FC in the compliance matrix.
   - **DR and DRR are not held** (charter section 3). SE-55 (DR: updated decommissioning plans) and SE-56 (DRR: updated disposal plans) are therefore T with relief type deviation in the compliance matrix: NPR 7123.1D §5.2.2.2 requires a waiver or deviation when a review is not held, and the relief is a deviation because it is approved before the matrix is baselined. The owner approves it as Engineering Technical Authority (SE-06) in the SRR decision memo. The substitute practice is in section 3.5.
4. **Review identifiers.** `SRR`, `PDR`, `CDR`, `TRR`, `SAR`. A delta review (section 7.6) is `TRR-D1`, `TRR-D2`, and so on. The identifier is the `<REVIEW>` token in `docs/reviews/<REVIEW>/` and in `RFA-<REVIEW>-NNN` / `RID-<REVIEW>-NNN`.
5. **Maturity terms** follow NPR 7123.1D App. F and map to repository states as follows.

| App. F term | Meaning on cwht | Repository evidence |
|---|---|---|
| Preliminary | Content exists and is under development; not yet under configuration control | File present; `status` fields `Draft`; no baseline tag includes it |
| Initial | First instance of a product that is continually developed and updated as the project matures (App. F F.1.a) | First values or plots in the package; later values appended to `history` in `docs/plan/tpm.json` or to `docs/vv/reports/` |
| Baseline (as an entrance expectation) | At least a final draft entering the review; baselined after review comments, RIDs and RFAs are incorporated (NPR 7123.1D §5.2.2.4) | Independent review record `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (front matter `id: INSP-NNN`) exists; no TBD; TBRs carry owner, plan and `close_by` |
| Baseline (after the gate) | Under configuration control; changes only by `CR-NNN` | Included in git tag `baseline/<review>`; listed in `docs/reviews/<REVIEW>/baseline-record.md` |
| Approved | Not under classic configuration control, but every change from the approved version is recorded at the next update (MOEs, TPM definitions, ConOps) | Listed as "Approved" in the decision memo; later changes listed in the next package section 5 "Changes since the last review" |
| Updated | Baselined item changed since the previous gate | Change set of `CR-NNN` identifiers listed in the package |
| Final | Exists once in final form | Minutes, decision memo, test reports |

6. **Roles at every review** (charter section 2): chair and Decision Authority and both Technical Authorities: Robin; presenter, package author and deck author: Claude (main session); independent product reviewers and the software assurance function: separate reviewer agent invocations. Before the review is convened, each reviewer files one record per product (charter sections 5 and 6): the filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md`. It is the single peer-review record, and its front matter carries `id: INSP-NNN` (fields in section 13). There is no `peer-reviews/` folder, and `tools/validate_docs.py` fails if one exists.
7. **App. G citation notation.** `G-n i` is Table G-n entrance item i; `G-n i.j` is sub-item j of entrance item i; `G-n sN` is success criterion N of Table G-n; "G-n item i" means the same as `G-n i`. Example: `G-6 6.26` is PDR entrance item 6, sub-item 26 (list of potential single point failures). App. G footnote markers are read per table. In Tables G-1 to G-7, G-9, G-12, G-13, G-17 and G-18, `*` marks a product required for programs and projects covered by NPR 7120.5, `**` a product required per NPR 7123.1 (the SE-NN minimum products) and `***` an item required per NPD 2570.5. In Tables G-8, G-10, G-11, G-14, G-15 and G-19, `*` marks an item required per NPD 2570.5. Section 3.5 applies these markers.

## 2. Life cycle

| Phase | Gate | Baseline set | Git tag | Authorizes |
|---|---|---|---|---|
| Pre-A / A Formulation | SRR | Functional: NGOs, MOEs, ConOps, L1 requirements, SEMP | `baseline/srr` | Phase B preliminary design; requirements enter change control (charter section 7) |
| B Preliminary design | PDR | Allocated: L2 specifications, ICDs, architecture, V&V plan, integration plan | `baseline/pdr` | Phase C detailed design |
| C Final design | CDR | Product: design data package, BOM, procedures, build-to specifications | `baseline/cdr` | **Procurement release**: PCBWay fabrication, assembly and CNC orders and the DigiKey order. No order is placed before the CDR decision memo is committed |
| D Realization | TRR | No baseline; confirms test configuration is under control | none (release tag `release/FW-vX.Y.Z`, or `release/FW-vX.Y.Z-rcN` for a candidate, referenced; identifiers per `05-configuration-and-data-management.md` section 4.3) | First powered bench test and the bench campaign; a delta TRR authorizes the on-air series |
| D Realization | SAR | As-built: as-built records, V&V report, version description | `baseline/sar` | Acceptance and hand-over to the owner and to friends (SI-019); start of Phase E |
| E / F Operations, closeout | Periodic status. DR and DRR are not held (SE-55 and SE-56 T, section 1 item 3 and section 3.5) | none | none | Anomaly reports as `NCR-NNN`; lessons learned; rev B formulation re-enters at SRR; archiving the repository is the final `CR-NNN` (section 3.5) |

Baseline tags are annotated git tags that Claude creates after the owner's approval is transcribed into the decision memo and the memo is committed. The procedure is `05-configuration-and-data-management.md` section 4.4 steps 1 to 6 and is not restated here. It commits the baseline record as commit R with the trailer `Refs: <REVIEW>` (the record's section 1 "Decision memo" row carries the memo commit hash), has the independent reviewer check the record at R, tags R with the message `cwht <name> baseline; decision memo docs/reviews/<REVIEW>/decision-memo.md at <memo commit>`, verifies the tag with `git tag -v` or `git cat-file -p`, pushes with `git push origin main --follow-tags`, confirms with `git ls-remote --tags origin baseline/<review>` (charter section 8: every baseline tag is pushed to `origin`), and writes the fill-once fields, the verification output and the approvals in a post-tag record commit with the trailer `Refs: <REVIEW>`. Tags are signed once the owner has configured a signing key (charter section 8); until then the record states `signed: false`.

### 2.1 Technical reviews between gates (SE-32, SE-57)

Between life-cycle reviews the technical effort is monitored through the technical reviews below (NPR 7123.1D §5.2.2.7, SE-57; planned here as SE-32 requires). None is a control gate and none creates a baseline. Findings from all of them enter the RFA/RID log only through owner adoption (section 10.1).

| Review | When | Criteria | Record | Findings |
|---|---|---|---|---|
| Sprint-closure technical review | Phase 5 of every software sprint (`07-software-engineering-plan.md` section 3.4) | Gate G1 to G6 exit 0; assurance verdict recorded; measurements of 07 section 11 appended; every TPM in `docs/plan/tpm.json` touched by the sprint (flash, RAM, CPU time, coverage, complexity, requirements volatility) reported with margin | `docs/sprints/SW-NN-<module>.md` (gate log, reviewer verdicts, measurements, owner status summary); `docs/plan/measurements.json` | Reviewer findings stay in the filled checklists (`INSP-NNN` records); an item that needs an owner decision is presented in the next package and becomes an RFA or RID only when the owner adopts it |
| Milestone status (SWE-018 as tailored in the RMM) | Every package, including delta TRRs | Milestone list of `docs/plan/schedule.md` against actual dates and vendor lead times; every slipped milestone has a cause and a recovery; procurement availability from `hardware/bom/` | Package section 12 "Milestone and procurement status" | Owner raises RFAs at the review |
| Independent peer review or inspection | Before any product is cited as review evidence (3.2 S3); every merged firmware change (07 section 10.1) | App. G Table G-19 entrance items 1 to 4: (1) the product is identified and made available; (2) "peer reviewers independent from the project" are selected for their technical background, customized on cwht as a separate agent invocation that did not author the product plus the software assurance review (3.5 row "Peer reviewer independence"); (3) agenda, success criteria and instructions are agreed; (4) rules for consistency among reviewers are established. G-19 success items 1 to 3: integrity evaluated, defects characterized, results communicated. Checklists `docs/templates/peer-review-checklist-{requirements,design,code,test}.md` (SWE-087 a to e, SWE-088, SWE-089). G-19 entrance item 5 and success item 4 (spectrum, marked as required per NPD 2570.5) are Customized (NA) per 3.5 | `docs/reviews/<REVIEW>/checklists/<product-slug>.md` with front matter `id: INSP-NNN` (section 13) | Findings live in the record with state Open, Fixed, Verified or Deferred; owner adoption per 10.1 |
| Software architecture review (SWE-143 as tailored in the RMM) | Before the PDR readiness declaration | Design checklist applied by an independent reviewer agent to the SWE-057 content (structure, qualities, interfaces, states) | `docs/reviews/PDR/checklists/<product-slug>.md` (slug `design-architecture`, front matter `id: INSP-NNN`); listed in 5.6 | Findings the owner adopts become RIDs (10.1), as the `rmm.json` SWE-143 implementation also states |
| Phase E periodic status | After SAR, on any anomaly and at the owner's request | Anomalies as `NCR-NNN`; lessons learned; rev B backlog | `docs/vv/ncr/`; `docs/lessons-learned.md` | n/a |

## 3. Rules common to every gate

### 3.1 Readiness declaration

1. Claude fills the entrance checklist in `docs/reviews/<REVIEW>/package.md` (template: `docs/templates/review-package.md`). Every row cites the artifact path and the commit hash of the evidence.
2. Claude runs `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --output docs/reviews/<REVIEW>/traceability-report.md` and attaches the report; a failing report blocks readiness for every gate. `docs/vv/traceability-report.md` (the tool's default output) is the working copy refreshed at any time; the per-review file is the frozen record that the package cites and that the baseline record hashes.
3. Claude runs the review-trend computation (section 11): `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/review_trend.py --date <T> --package <REVIEW> --write`. This writes `docs/reviews/<REVIEW>/figures/review-trend.png` and the `TPM-003` history entries. Claude attaches the plot in package section 14. A Red zone (exit status 1) is handled per section 11.
4. Claude writes the review deck from the completed package (charter section 4 item 2):
   - Source: `docs/reviews/<REVIEW>/slides/<review>.adoc`, with the review token in lower case (`srr.adoc`, `trr-d1.adoc`).
   - Content: at least one slide per entry of the charter's minimum slide set, mapped to package sections in the package "Slide map" (package section 1.1). Each slide names the package section it summarizes.
   - Render: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/slides/render_deck.py /Users/robinonsay/rust/cwht/docs/reviews/<REVIEW>/slides/<review>.adoc`. Exit 0 is required. The command writes `slides/<review>.html`, the git-ignored runtime copy `slides/reveal.js/`, and one `slides/png/slide-NN.png` per slide.
   - Inspection (charter section 11 rule 3): Claude opens every PNG and checks that text is legible, nothing is clipped, figures are readable and the slide count matches the source. On any defect, fix and re-render.
   - Speaker narrative: the narrative Claude presents with each slide (3.4) is the `[.notes]` block of that slide in `<review>.adoc`. It is written before the render, committed with the deck and never improvised: what is said at the review is the committed notes block, so the narrative is a controlled part of the deck (charter section 4 item 2).
   - Claims: Claude confirms that every claim on a slide and in its `[.notes]` block is present in `package.md`. A claim absent from the package is a defect, fixed before readiness by adding the evidence to the package or removing the claim.
   - Record: the deck source, HTML and PNGs are committed with the package. The package "Slide deck" block records the slide count, the render commit and the inspection date.
5. The owner confirms readiness in conversation; Claude transcribes the confirmation (date, wording) into the package "Readiness declaration" block. A *Hard* criterion that is not met blocks the declaration. A *Soft* criterion that is not met is listed as a proposed lien with owner, closure plan and due event; the owner accepts or rejects each proposed lien in the readiness confirmation. An accepted unmet Soft criterion is recorded at that confirmation as a Routine RFA raised by the owner (Claude transcribes it into the log with `lien: true`); a success-criterion shortfall ruled *Met with lien* at the review is recorded the same way at the review; a TBR lien uses its `REQ-<MOD>-NNN` id. That id is the lien id in the decision memo (section 12.2).

### 3.2 Standing entrance criteria (every gate)

| # | Criterion | Source | Evidence artifact | Shown in package as | Gate |
|---|---|---|---|---|---|
| S1 | Agenda, success criteria and board instructions agreed by presenter and chair before the review | G-3 1; G-4, G-5, G-6, G-7, G-9, G-11 item 2; G-10 1; project extension for G-12 | `docs/reviews/<REVIEW>/package.md` section 1; success criteria in this document | Agenda table; owner confirmation transcribed | Hard |
| S2 | Every RFA and RID from every prior review is Closed or Withdrawn, or is open with `lien: true`, an owner-accepted closure plan and a due event or date later than this gate (section 12.2). A Minor RID's due is never later than the readiness declaration of the gate that follows the review that raised it (10.2), so at that gate it is Closed or Withdrawn or it is a missed lien handled under 12.2. At SAR every prior RFA and RID is Closed or Withdrawn (G-11 item 1) | G-3 2; G-4, G-5, G-6, G-7, G-9, G-11 item 1; project extension for G-10 and G-12 | `docs/reviews/*/rfa-rid-log.json` (every prior review's log) | Burndown table and plot (section 11) | Hard |
| S3 | Every product listed in the gate's entrance table has an independent reviewer record with all findings dispositioned | App. G "peer reviews" items; Table G-19; charter section 2; SWE-087 | `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, front matter `id: INSP-NNN` (the single record, charter section 5) | Record index with finding counts | Hard |
| S4 | Traceability report passes (unique IDs, parents, verification coverage, status consistency) | charter section 7; SWE-052 | `docs/reviews/<REVIEW>/traceability-report.md` written by the command in 3.1 item 2 | Report summary and link | Hard |
| S5 | TBD/TBR list complete: zero TBDs in any item to be baselined; every TBR has owner, plan and `close_by` | App. G success criteria "TBD and TBR items" | requirements files `tbr` objects; package section 13 | Table | Hard |
| S6 | Proposed tailoring is listed with rationale for every new RMM or compliance-matrix row | App. G success criteria "Proposed tailoring is appropriate" | `docs/process/rmm.json`, `docs/process/se-compliance-matrix.json` (proposed rows flagged) | Tailoring table | Hard |
| S7 | Risk register current: every risk has likelihood, consequence, mitigation, owner and trigger; top risks named | App. G "risk assessment and mitigations" | `docs/risk/register.json` + rendered matrix | 5x5 matrix render and top-N table | Hard |
| S8 | TPM status current (section 11 and `docs/plan/tpm.json`), including the review-trend TPM | SE-60/61, SE-64 | `docs/plan/tpm.json`; `docs/reviews/<REVIEW>/figures/` | TPM table with margins and alert colour | Hard from PDR; Soft at SRR |
| S9 | Every visual product cited is rendered to an image and inspected (charter section 11.3) | charter | `docs/reviews/<REVIEW>/figures/*.png` or `.svg` | Embedded figures | Hard |
| S10 | Lessons learned reviewed and new entries recorded | App. G success criteria "Lessons Learned" | `docs/lessons-learned.md` | Package section 19 "Lessons learned since the last review" | Soft |
| S11 | Review deck ready: `slides/<review>.adoc` covers the minimum slide set of charter section 4 item 2; `tools/slides/render_deck.py` exited 0; every `slides/png/slide-NN.png` inspected; every slide names the package section it summarizes and carries no claim absent from `package.md` (3.1 item 4) | charter section 4 item 2; charter section 11 rules 2 and 3 | `docs/reviews/<REVIEW>/slides/` (`<review>.adoc`, `<review>.html`, `png/`) | Package section 1.1 "Slide map" and the "Slide deck" block of section 2 | Hard |

### 3.3 Standing success criteria (every gate)

| # | Criterion | Judged from |
|---|---|---|
| C1 | The gate-specific success criteria in sections 4 to 8 are met, or each shortfall has an accepted lien | Decision memo success-criteria table |
| C2 | The project demonstrates compliance with the charter, the SEMP, the RMM and the compliance matrix as tailored | Compliance summary in package; independent reviewer records |
| C3 | TBD and TBR items are identified with acceptable plans and closure events | Package TBD/TBR table |
| C4 | Proposed tailoring is appropriate and recorded row-by-row with rationale | Package tailoring table; owner decision recorded in memo |
| C5 | Software components meet the criteria for their life-cycle point (gate-specific SWE lists in sections 4.6, 5.6, 6.6, 7.5 and 8.6) | Software status table; SA reviewer record |
| C6 | Risks are identified, assessed and mitigated with owner-accepted residual risk | Risk section; memo |

**C5 basis.** App. G asks for "Software criteria and products, per NASA-HDBK-2203" at entrance and for "Software components meet the success criteria defined in NASA-HDBK-2203" at success (for example G-4 6.23 and G-4 s9). The software tables in sections 4.6, 5.6, 6.6, 7.5 and 8.6 are the cwht customization of the SWEHB Topic 7.09 entrance and exit criteria (`docs/references/md/swehb/7-09-entrance-and-exit-criteria.md`). Topic 7.09 says that decisions to tailor and customize life-cycle review criteria are justified to both the Engineering TA and the SMA TA; on cwht both are the owner, who approves these tables with this document at SRR. The per-review Process Asset Template checklists that Topic 7.09 provides are MS Word downloads and are not in the corpus. Checking the tables against them is an RSK-009 item: the independent reviewer of this document records the check as done, or as not possible, in its checklist record before the SRR readiness declaration.

### 3.4 Package, presentation, disposition, completion

Follow charter section 4. File locations:

- Package: `docs/reviews/<REVIEW>/package.md` (template `docs/templates/review-package.md`).
- Deck: `docs/reviews/<REVIEW>/slides/<review>.adoc`, rendered per 3.1 item 4.
- Minutes: `docs/reviews/<REVIEW>/minutes.md`.
- RFA/RID log: `docs/reviews/<REVIEW>/rfa-rid-log.json` (schema `docs/templates/rfa-rid-log.schema.json`).
- Decision memo: `docs/reviews/<REVIEW>/decision-memo.md` (template `docs/templates/decision-memo.md`).
- Baseline record: `docs/reviews/<REVIEW>/baseline-record.md` (template `docs/templates/baseline-record.md`), listing every configuration item and its commit hash or file hash.
- Figures: `docs/reviews/<REVIEW>/figures/`.

**Presentation (charter section 4 item 2).** Every gate, including each `TRR-Dn`, is conducted slide by slide from the rendered deck:

- Claude presents one slide per message: the rendered `slides/png/slide-NN.png` and the speaker narrative, which is the committed `[.notes]` block of that slide in `<review>.adoc` (3.1 item 4) and cites the package section.
- Claude then waits for the owner's questions, RFAs and RIDs, and advances only when the owner says to continue.
- Every question, answer, RFA and RID is recorded in the minutes against its slide number (`slide NN`). The creating `history` entry of each log item carries the note `Raised at <REVIEW> session <n>, slide NN`.
- The deck is not edited during a session. A defect found in a slide is a RID against the deck or against the package section it cites.
- For a re-review (12.1), the deck is revised, re-rendered and re-inspected per 3.1 item 4 before the new session.
- The minutes follow the slide order (section 9 row b).

Between gates (charter section 4.4): the decision memo for a change is the disposition block of its `CR-NNN` (`docs/cm/cr/CR-NNN-<slug>.md`), and the decision memo for a design decision is the decision section of its `ADR-NNN` (`docs/decisions/adr/ADR-NNN-*.md`). Approvals given in chat are transcribed into them in the same session. Delta TRRs (section 7.6) use their own folder `docs/reviews/TRR-Dn/` with package, deck, log and decision memo and no baseline tag.

### 3.5 App. G items customized or tailored at every gate

These items appear in several App. G tables. They are decided here once, since this document is the review plan (SE-32), and summarized in the SEMP. They are not repeated in the gate tables. The basis depends on the item's App. G marker (notation in section 1 item 7):

- **Unmarked items.** These are recommended best practices (App. G, G.1.1). Leaving one out or replacing it is customization (SE HB §3.11.4.3); no waiver is needed.
- **Items marked as required by NPR 7120.5 or NPD 2570.5.** The marker is `*` or `***` in Tables G-3 to G-7, G-9 and G-12, and `*` in Tables G-8, G-10, G-11 and G-19. Neither document governs cwht: charter section 1 lists the governing set, and charter section 3 borrows only the shape of the NPR 7120.5 life cycle. SE HB §3.11.4.3 routes departures from review elements required by other NPRs to tailoring of those documents. Because those documents do not apply, the departure is institutional non-applicability (charter section 1, "Tailoring vs customization"), recorded here as Customized (NA). Starred items that cwht performs anyway, such as the updated risk assessment (G-6 6.5) and the updated safety analyses (G-6 6.11), stay in the gate tables as project choices.
- **Items marked `**` (required per NPR 7123.1).** These are the SE-NN minimum products. They are dispositioned in `docs/process/se-compliance-matrix.json`, and a row below names the SE id wherever one is affected. The compliance matrix holds: SE-44 NA (programs other than single-project programs); SE-51 and SE-52 T (relief type deviation, scope relief; row "Decommissioning and disposal plans"); SE-55 and SE-56 T (relief type deviation, review not held; row "Decommissioning Review and Disposal Readiness Review").
- **NPR 7123.1D §5.2.2.6.** This body text, not App. G, asks projects with RF requirements to include spectrum-manager success criteria in every life-cycle and technical review, with certification per NPD 2570.5 and NPR 2570.1. It is dispositioned in the first row below.

Disposition vocabulary, as used in charter section 12:

- **Customized (NA):** the item is omitted for an institutional or physical reason, and any preserved intent is named.
- **Customized (substitute):** the item is replaced by the named project practice.
- **T:** relief from an SE-NN requirement, recorded row by row in the compliance matrix with the owner's approval.

| App. G item | Disposition | Reason and preserved intent |
|---|---|---|
| Spectrum: Center spectrum manager data and concurrence, Stage 1, 2 and 4 spectrum certification, NTIA signature and RF authorizations (NPD 2570.5 items in G-3, G-4, G-5, G-6, G-7, G-10, G-11, G-12; G-19 5 and s4); spectrum-manager success criteria of NPR 7123.1D §5.2.2.6 | Customized (NA) | NPD 2570.5 and NPR 2570.1 do not govern cwht, and there is no NASA spectrum manager. The owner is the FCC licensee (SI-014) and operates under 47 CFR Part 97. Intent preserved by: the Part 97 requirements (`REQ-TX-*` tagged `regulatory`, citing §97.305 and §97.307) with their verification cases; transmitting only into the dummy load until those cases pass (section 7); and the Part 97 compliance statement at SAR (8.3 row 7) |
| Programmatic products at NPR 7120.5 maturity: Life-Cycle Cost, IMS, Basis of Estimate, JCL (starred items, for example G-4 6.14 and 6.15, G-6 6.6) | Customized (NA) for JCL, LCC, IMS and Basis of Estimate; Customized (substitute) for cost and schedule | Not an NPR 7120.5 project. The substitutes are the labor-free cost model `docs/plan/cost-estimate.md` and the milestone list `docs/plan/schedule.md`, keyed to gates and vendor lead times. The software rows SWE-015, SWE-016 and SWE-151 are T in the RMM (charter section 12) |
| Integrated Logistics Support Plan (G-5 6.8, G-6 6.7, G-7 6.22; starred) | Customized (NA) | One to a few units for personal use. Intent preserved by a spares and consumables list in `hardware/bom/` and a maintenance section in `docs/ops/operations-handbook.md` |
| Human Rating Certification Package (G-4 6.19, G-5 6.10, G-6 6.21, G-7 6.19, G-12 9.7; starred) | Customized (NA) | Not a crewed space system. Operator safety (RF exposure, battery, thermal, hearing) is handled in `docs/safety/hazard-analysis.md` |
| Project Protection Plan (G-6 6.8, G-7 6.23, G-12 9.2; starred) | Customized (NA) | No mission assets to protect against hostile threats. Cybersecurity is tailored per charter section 12 (USB loading, key-input command injection) |
| System Security Plan (G-4 6.25, G-5 6.18, G-6 6.24, G-7 6.30; starred) | Customized (substitute) | No network interface. The substitute is the cybersecurity assessment, section 16 of `docs/process/07-software-engineering-plan.md`; the SWE-154, 156, 157, 159 and 210 rows are T in the RMM (charter section 12) |
| Launch site operations plan, checkout at launch site, preliminary certification for flight, mission operations plans (G-7 6.11, G-9 15.6, G-12 9.6) | Customized (NA) | No launch. "Certification for use" is the SAR acceptance statement plus the Part 97 compliance statement (SE-54, 8.5), which supersede the preliminary certification of G-12 9.6 |
| Program-level SEMP (SE-44) | NA in the compliance matrix | The Table H-1 rationale for SE-44 makes it Not Applicable to projects and single-project programs; the cwht SEMP is baselined at SRR under SE-38 |
| Decommissioning and disposal plans (SE-51, SE-52; G-6 6.16, G-7 6.13, G-9 15.7 and 15.8, G-12 8.2 and 8.3) | T (scope relief) | The ORR is held, combined with SAR (section 1 item 3), so SE-51 and SE-52 are due at SAR. **Location (customization, SE HB §3.11.4.2):** the plans are the end-of-life section of `docs/ops/operations-handbook.md`, not stand-alone documents. **Relief (the reason for T; SE HB §3.11.4 "scaling the requirement" and §3.11.4.2 "some relief on the scope"):** the section covers only the retirement steps and disposal route of a consumer handheld. It omits the plan content that App. G Tables G-17 and G-18 expect: resources, budget and staffing (G-17 3 and s4; G-18 3 and s11); personnel training and transition (G-17 s6 and s13; G-18 s5); decommissioning and disposal operations plans with contingencies (G-17 s3; G-18 s3); and spectrum-manager concurrence (G-17 s14; G-18 s14). **Content kept:** how a unit is retired (cells removed and recycled, unit serial `CWHT-A-NNN` marked retired in its as-built record, version record archived, repository tag kept) and the disposal route (lithium cells to a battery recycler, board and enclosure as electronic waste, no hazardous materials beyond the cells). The section is reviewed by an independent agent and baselined at SAR with the as-built baseline. The owner's approval of the compliance matrix and of the SAR decision memo records the tailoring (charter section 12; section 15 item 2 corrects the charter's stated basis) |
| Decommissioning Review and Disposal Readiness Review (Tables G-17 and G-18; SE-55, SE-56) | T (review not held, deviation) | NPR 7123.1D §5.2.2.2 and SE HB §3.11.4.3 require a waiver or deviation when a review is not held. The relief is a deviation, as the compliance matrix records it, because it is approved before the matrix is baselined; the owner approves it as Engineering Technical Authority (SE-06) in the SRR decision memo. **Substitute practice:** the end-of-life section of `docs/ops/operations-handbook.md` (row above) stays under configuration control (CR class) until the repository is archived. Any change to it after SAR is a `CR-NNN` and replaces the "updated plans" of SE-55 and SE-56. Archiving the repository is recorded as the final `CR-NNN`, which cites the handbook section and the SAR baseline |
| Higher- and lower-level life-cycle reviews (G-3 2; G-4 3; G-5 3; G-6 3; G-7 3) | Customized (substitute) | Single product layer with subsystems. The independent reviewer records of section 3.2 S3 are the lower-level reviews |
| Review board instructions (S1 sources) | Customized (substitute) | The board is the owner; the instructions are this document |
| Peer reviewer independence (G-19 2: "Peer reviewers independent from the project") | Customized (substitute) | There are no reviewers outside the project. Independence is a separate agent invocation that did not author the product, plus the software assurance review for software products (charter section 2; charter section 11 rule 4). The owner rules on every finding at the review (10.1) |
| Health and medical, planetary protection, orbital debris, contamination control plan, environments control plan, payload-to-carrier integration plan (G-6 6.9 examples; G-7 s13 contamination) | Customized (NA) | Not present in a handheld ground radio. RF exposure and hearing protection remain as hazards |
| Material properties tests, loads, stress, fracture control (G-7 s13) | Customized (NA) | No flight or structural loads. Enclosure adequacy is shown by CAD fit-check and a printed prototype (SI-012) |
| EEE parts program, GIDEP, counterfeit avoidance audits (G-6 6.25, G-7 6.31, G-7 s14) | Customized (substitute) | Catalog parts are bought from DigiKey (authorized distributor) only, with no screening. Availability and lead time are checked at CDR (6.3 row 20) |
| Supply Chain Risk Management (SCRM) audits (G-6 6.25, G-7 6.31, G-9 15.10; G-5 s14, G-6 s21, G-7 s20) | Customized (substitute) | Reduced to vendor capability checks (PCBWay rules) and single-source part risks in the register |
| Other safety and mission assurance products (G-6 s8, G-7 s9: PRA, failure modes and effects analysis, maintainability, quality verification, SMA plan G-4 6.20 and G-5 6.13) | Customized (substitute) | PRA: Customized (NA), since no probabilistic risk requirement governs cwht and the 5x5 register of `06-risk-and-decision-analysis.md` is the risk method. FMEA: replaced by the hazard analysis and the single point failure list with effects and acceptance rationale (G-6 6.26, G-7 6.32). Maintainability: the maintenance and support concept (SRR row 27) and the handbook maintenance section. Quality controls and verification: receipt inspection reports and the independent-review rule. SMA plan: the hazard analysis plus charter section 2 (4.7) |
| Personnel training records (G-10 8, G-10 s10, G-12 6) | Customized (substitute) | The owner is the only test operator. The safety notes in each bench procedure and the operations handbook walkthrough (OPS scenario) replace training records |
| Results of SARs at major suppliers (G-11 3.1) | Customized (substitute) | Replaced by receipt inspection reports `docs/vv/reports/receipt-inspection-<n>.md` for the PCBWay and DigiKey deliveries |
| Final Certification Package (G-11 3.7) | Customized (substitute) | The acceptance data package of section 8.5. It contains the Part 97 compliance statement `docs/vv/reports/part97-compliance.md` and the SAR acceptance statement, which are the SE-54 products (8.3 row 7) |
| Production Readiness Review (G-8) | Customized (NA) | App. G §G.9 (Table G-8) applies to projects developing or acquiring multiple systems or units. cwht builds at most five complete units (SI-035, ADR-025) in one vendor batch from the single CDR release, with no qualification unit followed by a production run, so the project determines that no PRR is held and carries its intent in CDR (SEMP section 3.4): production design documentation and the BOM with critical parts and alternates (6.3 rows 3 and 4), procurement status with qualified suppliers and lead times (6.3 row 20), design-for-manufacturing checks (6.3 row 23), and in-process and end-item inspection by the receipt inspection and first-power-on stages of 04 section 11.2. PRR carries no SE-NN minimum product |

---

## 4. System Requirements Review (SRR)

### 4.1 Purpose

Confirm that the functional and performance requirements for the radio respond to the owner's expectations (NGOs, MOEs, ConOps) and can be achieved within the project's means, that the concept is feasible, and that the plans (SEMP, CM, risk, V&V approach, software plans) are sufficient to begin preliminary design. The SRR also serves as the MCR (App. G Table G-3 products).

### 4.2 Trigger

Convened when the Hard rows of 3.2 and 4.3 are met. Expected sequence: stakeholder inputs logged, NGOs and MOEs drafted, ConOps with nominal and off-nominal scenarios, L1 requirements written and independently validated against SE HB §4.2.1.2.4, preliminary hazard list, software classification and RMM, toolchain proof, then readiness declaration.

### 4.3 Entrance criteria (tailored from Tables G-3 and G-4)

| # | Criterion | Source | Evidence artifact | Shown in package as | Gate |
|---|---|---|---|---|---|
| 1 | Stakeholders identified; stakeholder expectations defined and ready to baseline | G-3 3.1; SE-35 | `docs/requirements/l0-stakeholder/stakeholder-inputs.md` (SI-NNN), `docs/requirements/l0-stakeholder/expectations.json` and rendered `.md` | Table of NGOs with source SI ids | Hard |
| 2 | Goals and objectives ready to baseline | G-3 5.1 | `expectations.json` NGO entries | Same table | Hard |
| 3 | MOEs and success criteria defined and ready to approve | G-3 3.3; SE-37 | `expectations.json` MOE entries with target values and units | MOE table | Hard |
| 4 | Concept developed to a level that demonstrates technical feasibility, ready to baseline | G-3 3.2; SE-36 | `docs/conops/conops.md`; feasibility research in `docs/research/` | Concept summary, block sketch render | Hard |
| 5 | Alternative concepts analyzed | G-3 5.2 | At least one concept-level `docs/decisions/trade-studies/TS-NNN-*.md` (receiver architecture family, PA topology) and the ADR recording the owner-directed RP2350/Rust choice (SI-007) | Trade summary with criteria and scores | Hard |
| 6 | Descope options identified | G-3 5.4 | `docs/conops/conops.md` section "Deferred capabilities" (70 cm path, SI-002) | List | Soft |
| 7 | L1 system requirements ready to baseline; preliminary allocation to L2 performed | G-4 5.1; SE-39 | `docs/requirements/sys/requirements.json` (all `status` Active or Draft with reviewer record), `docs/design/allocation.json` (preliminary) | Requirements count by module, allocation table, validation summary per SE HB §4.2.1.2.4 | Hard |
| 8 | Every L1 requirement has a verification method and a preliminary verification note | G-4 6.8; G-3 5.6 | `verification_method`, `verification_note` fields; traceability report | Coverage table by method | Hard |
| 9 | SEMP ready to baseline, including the HSI section. NPR 7123.1D §5.2.1.3 strongly recommends a stand-alone HSI Plan for Category 1 and Class A programs and projects. cwht is neither an NPR 7120.5 Category 1 project nor an NPR 8705.4 Class A payload: its Class A election is the NPR 7150.2D software class (charter section 1). Section 5.2.1.3 leaves the location to the project manager, and the owner, as project manager, has chosen a SEMP section (charter section 12) | G-4 5.2, 5.3; SE-38, SE-65, SE-66; NPR 7123.1D §5.2.1.3; charter section 12 | `docs/plan/semp.md` (charter is its core), HSI section covering controls, display, audio, straight key and iambic paddle ergonomics (SI-018), RF exposure | SEMP outline against SE HB App. J | Hard |
| 10 | ConOps updated with nominal and off-nominal scenarios | G-4 6.2; SE-36 | `docs/conops/conops.md` with `OPS-NNN` scenarios incl. straight-key and paddle operation, headphone use, tuning, charging, high-SWR and stuck-key cases | Scenario list with MOE links | Hard |
| 11 | Risk management approach ready to baseline; risk assessment with mitigations | G-4 6.4, 6.5; G-3 5.5 | `docs/plan/semp.md` risk section; `docs/risk/register.json` + rendered matrix | 5x5 render, top risks | Hard |
| 12 | Configuration management plan ready to baseline | G-4 6.6 | `docs/process/05-configuration-and-data-management.md` | Summary of CIs, baselines, CR flow | Hard |
| 13 | Document tree defined | G-4 6.7 | charter section 5; `docs/` layout | Tree with existence status | Hard |
| 14 | Preliminary system safety analysis and safety-critical software determination | G-4 6.9; SWE-205 | `docs/safety/hazard-analysis.md`, `docs/safety/hazards.json` (HZ-NNN for RF exposure, battery charging, PA thermal, hearing, stuck key) | Hazard list with preliminary controls | Hard |
| 15 | Single point failure and fault tolerance philosophy stated | G-3 5.10; G-4 s14 | `docs/safety/hazard-analysis.md` section "Fault tolerance philosophy" (keying, PA enable, charging, thermal) | Paragraph and requirement ids | Hard |
| 16 | Product acceptance data requirements identified | G-4 6.10 | `docs/plan/semp.md` V&V section listing the acceptance data package contents (section 8.5) | List | Soft |
| 17 | External interfaces identified with preliminary definitions | G-4 6.11 | `docs/icd/ICD-*.md` stubs: key or paddle jack, headphone jack, antenna connector, USB, charger and battery | ICD list with maturity | Hard |
| 18 | Preliminary MOPs, TPMs and key driving requirements | G-4 6.12 | `docs/plan/tpm.json` (preliminary); requirements with `priority: KDR` | TPM definition table | Hard |
| 19 | Cost estimate and basis (tailored) | G-4 6.14, 6.15 | `docs/plan/cost-estimate.md` (BOM, fabrication, assembly, CNC, shipping, contingency) | Cost table | Soft |
| 20 | Technology readiness and heritage assessment, including toolchain proof | G-4 6.16, 6.17; G-3 5.9; charter section 3 | `docs/plan/technology-assessment.md` (RP2350, rustos heritage, RF parts, KiCad, LTspice, emulator); `tools/toolchain.lock.md` | TRL-style table; toolchain sanity-check results | Hard |
| 21 | Engineering development assessment and technical plan for Phase B | G-4 6.22 | `docs/plan/semp.md` Phase B section; `docs/plan/schedule.md` | Milestone list to PDR | Soft |
| 22 | Software classification record and RMM | G-4 6.23; SWE-020, SWE-125, SWE-139 | `docs/process/03-software-classification-and-rmm.md`, `docs/process/rmm.json` | Class election statement; RMM row counts by disposition | Hard |
| 23 | Software plans (preliminary) covering the life cycle with approved tailoring | SWE-013; SWE-033; SWE-037 | `docs/process/07-software-engineering-plan.md` | Plan outline; acquisition-vs-development record; software review milestones | Hard |
| 24 | NPR 7123.1 compliance matrix populated | G-4 s7, s12; SE HB §3.11.3 | `docs/process/se-compliance-matrix.json` | Counts FC / T / NA; proposed rows | Hard |
| 25 | Regulatory constraints captured as requirements | replaces G-4 6.24 | `REQ-TX-*` tagged `regulatory` citing 47 CFR §97.305 and §97.307 from the published CFR text (SEMP section 2.0; 02 section 3.4) | Requirement ids and the clause each cites | Hard |
| 26 | Preliminary V&V approach for the concept (evidence classes, run-for-record policy) | G-3 5.6; charter section 9 | `docs/plan/semp.md` V&V section | Table of evidence classes by requirement type | Hard |
| 27 | Preliminary maintenance and support concept | G-4 6.18 | `docs/conops/conops.md` support section (charging, firmware update, cleaning) | Paragraph | Soft |
| 28 | Regulatory corpus present so that Part 97 clauses are cited from the repository | SEMP section 2.0 (due before PDR) | `docs/references/md/regulatory/` (47 CFR Part 97 text converted by `tools/refs/`) | Corpus file list, or the lien with its PDR due event | Soft (Hard at PDR, section 5.3 row 12) |

### 4.4 Success criteria

| # | Criterion | Source | Judged from |
|---|---|---|---|
| 1 | L1 requirements respond to the NGOs, MOEs and ConOps, reflect intended use, and are achievable within the project's means | G-4 s1 | Traceability report (every REQ-SYS has `source_ids`); validation records |
| 2 | Requirements definition and plans are mature enough to begin Phase B | G-4 s2 | Entrance rows 7 to 13 met without Major RIDs |
| 3 | The allocation and control process is sound: change control via `CR-NNN` starts at this gate; plan to complete L2 by PDR exists | G-4 s3 | CM plan; milestone list |
| 4 | External and major internal interfaces identified, including the USB and key-input security expectations | G-4 s4 | ICD list |
| 5 | Verification and validation approach determined for every requirement | G-4 s5 | Method coverage table |
| 6 | Major risks identified, assessed, with viable mitigations | G-4 s6 | Register |
| 7 | Mission objectives clear, unambiguous, internally consistent; the need is stated; the concept satisfies the expectations and is feasible | G-3 s1, s2, s3, s5 | NGO/MOE table; concept summary; feasibility research |
| 8 | Concept evaluation criteria identified and prioritized; existing assets (rustos, catalog modules) considered | G-3 s4, s9 | Trade study |
| 9 | Technical planning sufficient for Phase B, covering hardware, software, human systems and data deliverables | G-3 s10 | SEMP |
| 10 | HSI aspects included in planning and sufficient for the next phase (straight key and paddle use, controls, audio) | G-4 s10 | SEMP HSI section |
| 11 | Fault tolerance philosophy is reflected in requirements | G-4 s14 | Requirement ids cited by hazard analysis |
| 12 | Software components meet the SRR-point criteria in 4.6 | G-4 s9 | SA reviewer record |

### 4.5 Minimum products (NPR 7123.1D §5.2.2.2)

| SE id | Product | cwht artifact | Maturity leaving SRR |
|---|---|---|---|
| SE-35 | Stakeholder identification and expectation definitions | `docs/requirements/l0-stakeholder/` | Baselined |
| SE-36 | Concept definition | `docs/conops/conops.md` | Baselined |
| SE-37 | MOE definition | `expectations.json` MOE entries | Approved |
| SE-38 | SEMP | `docs/plan/semp.md` + charter | Baselined |
| SE-39 | Requirements | `docs/requirements/sys/requirements.json` | Baselined |
| SE-66 | HSI approach | SEMP HSI section | Baselined |

### 4.6 Software products required by SRR (NPR 7150.2D, Class A as elected)

| SWE | Product or evidence at SRR | Artifact |
|---|---|---|
| SWE-020, SWE-176 | Classification record (Class A elected; letter-of-App.-D note) and the independent classification concurrence (03 section 3.3, checks CL-1 to CL-9) | `docs/process/03-software-classification-and-rmm.md`; `docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm.md` (checklist `docs/templates/peer-review-checklist-classification.md`, front matter `id: INSP-NNN`) |
| SWE-205 | Safety-critical determination per component (keyer, PA enable, charging, thermal) | `docs/safety/hazard-analysis.md` |
| SWE-125, SWE-139 | Requirements Mapping Matrix with tailoring rows | `docs/process/rmm.json` |
| SWE-013 | Software plans (preliminary), including the tailored security section | `docs/process/07-software-engineering-plan.md` |
| SWE-033 | Acquisition versus development assessment (rustos reuse, crates) | `docs/process/07-software-engineering-plan.md` or `ADR-NNN` |
| SWE-034 | Acceptance criteria (preliminary) | SEMP V&V section |
| SWE-037 | Software review milestones (this document's gates plus code peer reviews) | `docs/process/07-software-engineering-plan.md` |
| SWE-079, SWE-081 | Software CM plan and CI list (within the CM plan) | `docs/process/05-configuration-and-data-management.md` |
| SWE-086 | Software risks in the register | `docs/risk/register.json` |
| SWE-050 | Software-related L1 requirements captured; SRS preliminary | `docs/requirements/sys/`, `docs/requirements/sw/` (Draft) |
| SWE-052 | Traceability L0 to L1 and L1 to hazards | traceability report |
| SWE-136 | Tool list with sanity checks (preliminary); a `TV-NNN` record for every tool whose output is already cited as evidence | `tools/toolchain.lock.md`; `docs/cm/tool-validation/TV-NNN-<tool>.md` |
| SWE-087 a, SWE-088 | Peer review of the software-related L1 requirements (`REQ-SYS-*` allocated to SW in `docs/design/allocation.json`) and of any Draft SRS file cited as SRR evidence, with `docs/templates/peer-review-checklist-requirements.md` (07 section 10.1 row a) | `docs/reviews/SRR/checklists/requirements-sys.md` and `docs/reviews/SRR/checklists/requirements-sw-<sub>.md` (front matter `id: INSP-NNN`) |
| SWE-087 b, SWE-088 | Peer review of the software plans, including cybersecurity: `docs/process/07-software-engineering-plan.md` (section 16 included) and the software part of the V&V approach, with `docs/templates/peer-review-checklist-requirements.md` section G (items CK-REQ-G1 to G8; 07 section 10.1 row b, "Before SRR") | `docs/reviews/SRR/checklists/plan-07-software-engineering-plan.md` and one `plan-<document-stem>.md` per other plan reviewed |
| SWE-089 | Peer review measurements recorded in each record and rolled up | record front matter (`findings_*`, `effort_*`); `docs/plan/measurements.json` |

### 4.7 Not Applicable at SRR (in addition to 3.5)

| App. G item | Reason |
|---|---|
| G-4 6.3 "Updated parent requirements" | No parent program; NGOs are the parent (rows 1 to 3) |
| G-4 6.13 "Other specialty discipline analyses" | None identified beyond safety and RF; revisit at PDR |
| G-4 6.20 "System safety and mission assurance plan" | Customized: SMA content is the hazard analysis plus the independent-review rule of charter section 2 |
| G-3 5.8 "Technology Development Plan" | No technology below TRL 6 is planned; the technology assessment (row 20) records this; if a gap appears it becomes a risk and a research report |
| G-3 5.12 "Conceptual life-cycle support strategies (logistics, supply chain, manufacturing)" | Customized into rows 6 and 27 and the vendor choice (SI-008, SI-009) |

---

## 5. Preliminary Design Review (PDR)

### 5.1 Purpose

Show that the architecture and preliminary design meet every L1 and L2 requirement with acceptable risk and margin, that requirements are allocated to subsystems and interfaces are defined, that the V&V and integration plans are ready to baseline, and that detailed design can start. The PDR also serves as the MDR/SDR (Table G-5 products).

### 5.2 Trigger

Convened when SRR is complete (section 9), all L1 TBRs are closed (charter section 7), and the Hard rows of 3.2 and 5.3 are met.

### 5.3 Entrance criteria (tailored from Tables G-5 and G-6)

| # | Criterion | Source | Evidence artifact | Shown in package as | Gate |
|---|---|---|---|---|---|
| 1 | Architecture defined with major trade-offs, ready to baseline | G-5 5.1; SE-41 | `docs/design/architecture.md`; `docs/decisions/trade-studies/TS-NNN-*.md`; `docs/decisions/adr/ADR-NNN-*.md` | Block diagram render; trade summary | Hard |
| 2 | Allocation of L1 requirements to L2 subsystems ready to baseline; L2 specifications ready to baseline with supporting trades | G-5 5.2; G-6 6.1; SE-42 | `docs/design/allocation.json`; `docs/requirements/{rx,tx,pwr,ctl,me}/requirements.json` and `docs/requirements/sw/*/requirements.json` (charter section 6) | Allocation matrix; L2 counts and validation summary | Hard |
| 3 | MOPs, TPMs and key driving requirements ready to approve | G-5 5.3; SE-40 | `docs/plan/tpm.json` with target, threshold, current estimate, margin | TPM definition table | Hard |
| 4 | Status of TPMs and initial trends of the required leading indicators: mass margin (SE-62, `TPM-001`) and power margin (SE-63, `TPM-002`), required by NPR 7123.1D §6.2.8, plus the review trend (SE-64, `TPM-003`, §6.2.9), and memory and RF budget margins; resolution of SRR discrepancies | G-5 5.4; G-6 6.2; SE-43; NPR 7123.1D §6.2.8, §6.2.9 | `docs/plan/tpm.json` history; `docs/reviews/SRR/rfa-rid-log.json` | TPM trend plots; burndown | Hard |
| 5 | Preliminary design shown to meet all requirements and performance measures, or with recorded waivers | G-6 5.1; SE-45 | `hardware/kicad/` preliminary schematics; `hardware/sim/` LTspice decks and results; `docs/design/architecture.md` firmware architecture; `docs/design/budgets.md` | Schematic sheet renders; simulation plots; compliance matrix design-to-requirement | Hard |
| 6 | Integration plan ready to baseline | G-6 5.2; SE-67; SE HB App. H | `docs/plan/integration-plan.md` (board bring-up order, firmware load, enclosure fit, test points) | Sequence table | Hard |
| 7 | V&V plan ready to baseline; verification and validation matrices generated | G-6 5.3, 6.14; SE-68; SE HB App. D, E, I | `docs/vv/plan.md`; matrices from `tools/traceability.py` | Matrix summaries by method and evidence class | Hard |
| 8 | ICDs ready to baseline | G-6 6.13; G-5 6.11 | `docs/icd/ICD-*.md` with pin maps, connectors, levels, timing (key and paddle input debouncing and keyer timing included) | ICD table with maturity | Hard |
| 9 | Technical resource estimates and margins: mass (SE-62, `TPM-001`, provisional allocation 350 g per charter section 12), power (SE-63, `TPM-002`), battery life, thermal, flash, RAM, CPU time, PCB area, enclosure volume, RF link budget | G-6 6.17; G-5 6.12; NPR 7123.1D §6.2.8 | `docs/design/budgets.md`; `docs/plan/tpm.json` | Margin table with alert colours | Hard |
| 10 | Hazard analysis updated: each hazard has controls allocated to L2 requirements; safety-critical software components and SWE-134 provisions identified | G-6 6.11; G-5 6.15; SWE-134, SWE-184 | `docs/safety/hazard-analysis.md`, `hazards.json`; `REQ-SW-*` with `hazard_ids` | Hazard-to-requirement table | Hard |
| 11 | List of potential single point failures | G-6 6.26 | `docs/safety/hazard-analysis.md` SPF section | Table | Hard |
| 12 | Regulatory compliance approach: Part 97 spurious and harmonic limits shown by analysis plan; the regulatory corpus present so every `REQ-TX-*` clause citation resolves to `docs/references/md/regulatory/` (SRR row 28 closed) | G-6 6.15; SEMP section 2.0 | `docs/vv/plan.md` regulatory section; `hardware/sim/` filter response; `docs/references/md/regulatory/` | Plot against §97.307 limit line; corpus file list | Hard |
| 13 | ConOps baselined (approved) and consistent with the design | G-6 6.18; G-5 6.14 | `docs/conops/conops.md` | Changes since SRR | Hard |
| 14 | Design standards identified and incorporated: Rust coding standard and static analysis set, KiCad DRC rules set to PCBWay capabilities, Part 97 limits | G-6 6.10; SWE-061, SWE-135 | `docs/process/07-software-engineering-plan.md` coding standard section; `hardware/kicad/` DRC rule file | List with paths | Hard |
| 15 | Preliminary design data package index (drawing tree equivalent) | G-6 6.12 | `docs/design/architecture.md` section "Design data package index" | Tree | Soft |
| 16 | Technology readiness and heritage assessment updated | G-6 6.3; G-5 6.6; G-6 s16 | `docs/plan/technology-assessment.md` | Delta table | Soft |
| 17 | Cost estimate and milestone list updated (tailored) | G-6 6.6; G-5 6.7 | `docs/plan/cost-estimate.md`, `docs/plan/schedule.md` | Tables | Soft |
| 18 | Applicable technical plans: EMI/EMC approach (shielding, filtering, layout rules), parts approach (DigiKey catalog, alternates), producibility (PCBWay assembly constraints) | G-6 6.9 | `docs/plan/semp.md` sections | Paragraphs | Soft |
| 19 | SEMP updated | G-6 6.19; G-5 6.2 | `docs/plan/semp.md` | Change list | Soft |
| 20 | HSI approach updated: control layout, display legibility, audio level limits, straight-key and iambic-paddle ergonomics and keyer settings | G-6 6.20; G-5 6.9 | SEMP HSI section; `docs/conops/conops.md` | Front-panel render | Hard |
| 21 | Procurement status: part availability and lead times; single-source parts in the risk register | G-6 6.25 | `hardware/bom/` (preliminary BOM with alternates) | Availability table | Soft |
| 22 | Software products at PDR (see 5.6) | G-6 6.22; G-5 6.16 | see 5.6 | Software status table | Hard |
| 23 | Supporting analyses: functional and timing descriptions (keyer timing, T/R switching sequence, receiver mute), allocation of functions to architecture elements | G-5 6.1; SE HB §4.3 (Logical Decomposition). SE HB App. F was removed in Rev 2, and the NASA Expanded Guidance App. F it points to is not in the corpus | `docs/design/architecture.md` functional and timing section | Timing diagram render | Hard |
| 24 | Manufacturability assessed: PCBWay fabrication and assembly capability check, enclosure machinability | G-6 s17 | `docs/research/` vendor capability notes; DRC rule file | Checklist | Soft |
| 25 | All L1 TBRs closed | charter section 7 | requirements files | TBD/TBR table | Hard |

### 5.4 Success criteria

| # | Criterion | Source | Judged from |
|---|---|---|---|
| 1 | Top-level requirements, MOEs, TPMs and owner constraints are agreed, final, clear and consistent with the preliminary design | G-6 s1 | Requirement changes since SRR (CR list); TPM table |
| 2 | Flow-down of verifiable requirements to L2 is complete and traceable to L1 and to NGOs | G-6 s2; G-5 s4 | Traceability report (no orphan L2, every L1 allocated) |
| 3 | Preliminary design expected to meet requirements at acceptable risk | G-6 s4 | Design compliance matrix; simulation results |
| 4 | Interface definitions consistent with maturity; interface risks acceptable | G-6 s5 | ICD table |
| 5 | No new technology required, or backup options exist | G-6 s6; G-5 s7 | Technology assessment |
| 6 | Risks credibly assessed with plans and resources | G-6 s7; G-5 s6 | Register |
| 7 | Safety and mission assurance addressed in the preliminary design (G-6 s8 lists safety, reliability, maintainability, quality controls, quality verifications, supplier risk management and EEE parts): safety by the hazard analysis at PDR maturity with controls allocated to L2 requirements; reliability by the derating and thermal analysis approach planned for CDR (6.3 row 16); maintainability by the maintenance and support concept (4.3 row 27); quality by the receipt inspection plan and the independent-review rule; supplier risk and EEE parts by DigiKey-only sourcing and single-source risks in the register; PRA, FMEA and the SMA plan as customized in 3.5 | G-6 s8 | Hazard table; 3.5 row "Other safety and mission assurance products"; row 21 |
| 8 | Adequate technical margins exist (power, thermal, memory, RF) | G-6 s9 | Budgets table, all margins above threshold or with lien |
| 9 | ConOps technically sound, includes human systems, and its requirements are flowed down | G-6 s10; G-5 s8 | ConOps-to-requirement trace |
| 10 | Trade studies mostly complete; remaining ones identified with closure plans | G-6 s11; G-5 s5 | Trade study status table |
| 11 | Preliminary analysis of each subsystem complete with margin challenges highlighted; modelling results considered | G-6 s14, s15 | Simulation summaries per subsystem |
| 12 | Heritage designs assessed (rustos, reference circuits) | G-6 s16 | Technology assessment |
| 13 | Manufacturability included in design | G-6 s17 | Row 24 |
| 14 | Architecture credible and responsive to requirements and constraints; all requirements allocated to architectural elements | G-5 s1, s4 | Allocation matrix |
| 15 | Architecture supports the fault tolerance requirements | G-5 s15 | SPF list and controls |
| 16 | Procurement approach consistent with the milestone list | G-5 s14; G-6 s21 | Row 21 |
| 17 | Software components meet the PDR-point criteria in 5.6 | G-6 s18 | SA reviewer record |
| 18 | HSI sufficient to proceed | G-6 s19 | Row 20 |

### 5.5 Minimum products (NPR 7123.1D §5.2.2.2)

| SE id | Product | cwht artifact | Maturity leaving PDR |
|---|---|---|---|
| SE-40 | TPM definitions | `docs/plan/tpm.json` | Approved |
| SE-41 | Architecture definition | `docs/design/architecture.md` | Baselined |
| SE-42 | Allocation of requirements to next lower level | `docs/design/allocation.json`; L2 requirement files | Baselined |
| SE-43 | Initial trend of leading indicators | `docs/plan/tpm.json` history; package plots | Initial |
| SE-45 | Preliminary design solution definition | `hardware/kicad/`, `hardware/sim/`, `docs/design/` | Preliminary |
| SE-67 | Integration plan | `docs/plan/integration-plan.md` | Baselined |
| SE-68 | V&V plan | `docs/vv/plan.md` | Baselined |

### 5.6 Software products required by PDR

| SWE | Product or evidence at PDR | Artifact |
|---|---|---|
| SWE-050, SWE-184 | Software requirements baselined, including safety constraints, controls and assumptions between hardware, operator and software | `docs/requirements/sw/*/requirements.json` |
| SWE-057 | Software architecture recorded | `docs/design/architecture.md` software section |
| SWE-052 | Traceability: L1 to software requirements, software requirements to hazards, software requirements to architecture elements | traceability report |
| SWE-013, SWE-024 | Software plans updated; actuals tracked against plan | `docs/process/07-software-engineering-plan.md`; package software status |
| SWE-065 a | Software test plan (part of V&V plan) | `docs/vv/plan.md` software section |
| SWE-061, SWE-135 | Coding standard selected; static analysis tool set named with versions | `docs/process/07-software-engineering-plan.md`; `tools/toolchain.lock.md` |
| SWE-134, SWE-023 (as tailored in the RMM) | Safety-critical software components identified; the SWE-134 a to l provisions allocated to design elements | `docs/safety/hazard-analysis.md`; `docs/design/architecture.md` |
| SWE-136, SWE-070 | Tool validation status for the build chain, the simulation tools and, if used, the emulator | `tools/toolchain.lock.md`; `docs/cm/tool-validation/TV-NNN-<tool>.md` |
| SWE-200 | Requirements volatility metric since SRR | package software status |
| SWE-087 a, c, SWE-088, SWE-089 | Peer review records for the software requirements (SRS files) and the software architecture, with measurements | `docs/reviews/PDR/checklists/requirements-sw-<sub>.md` and `docs/reviews/PDR/checklists/design-architecture.md` (front matter `id: INSP-NNN`) |
| SWE-143 (as tailored in the RMM) | Software architecture review by an independent reviewer agent against the design checklist (section 2.1) | `docs/reviews/PDR/checklists/design-architecture.md` for the `docs/design/architecture.md` software section |

### 5.7 Not Applicable at PDR (in addition to 3.5)

| App. G item | Reason |
|---|---|
| G-6 6.4, G-5 6.5 "Technology Development Plan" | No technology maturation planned (SRR row 20) |
| G-6 6.16 "Preliminary Disposal Plan" | Covered by SE-52, T per 3.5 (scope relief): the end-of-life section of the operations handbook, baselined at SAR |
| G-6 6.9 reliability program plan, quality assurance plan | Customized: reliability is a derating and thermal analysis at CDR (section 6.3 row 16); quality is receipt inspection and the independent-review rule |
| G-5 6.8 "Preliminary ILSP", G-5 6.10 "Human Rating" | Customized (NA) per 3.5 |

---

## 6. Critical Design Review (CDR)

### 6.1 Purpose

Show that the detailed design meets every requirement with adequate margin, that the design data package is complete enough to fabricate, assemble, machine and program the radio, that test procedures and acceptance criteria are ready, and that safety and regulatory obligations are covered. **CDR approval is the procurement release** (charter section 3): the owner places the PCBWay and DigiKey orders only after the CDR decision memo is committed and every lien tagged `blocks-order` in the memo is Closed. Claude prepares the release package `hardware/releases/HW-MB-rev<X>-<n>/` (fabrication, assembly and CNC files, plus the SMT versus hand-solder split `cwht-MB-rev<X>-hand-assembly.csv`, SI-031) and never places an order. The owner files the PCBWay and DigiKey order confirmations in the same folder (charter section 5; release identifiers per `05-configuration-and-data-management.md` Table 4-1 row 37).

### 6.2 Trigger

Convened when PDR is complete, all L2 TBRs are closed, DRC and ERC are clean, every schematic sheet, PCB layer view, 3D board render and enclosure render has been produced and inspected, and the Hard rows of 3.2 and 6.3 are met.

### 6.3 Entrance criteria (tailored from Table G-7)

| # | Criterion | Source | Evidence artifact | Shown in package as | Gate |
|---|---|---|---|---|---|
| 1 | Detailed design ready to baseline and shown to meet all requirements and performance measures, or with recorded waivers | G-7 5; SE-46 | `hardware/kicad/` (schematics, PCB), `hardware/enclosure/` (OpenSCAD), `docs/design/software-design.md`, `docs/design/budgets.md` | Design-to-requirement compliance matrix; renders of every sheet, layer view, 3D board, enclosure | Hard |
| 2 | Build-to specifications with supporting trades ready to baseline | G-7 6.1 | `docs/design/build-to-specification.md` (stackup, finish, assembly side, CNC material and tolerances, firmware release id) | Table | Hard |
| 3 | Fabrication, assembly, integration and test plans and procedures ready to baseline | G-7 6.2; charter section 12 "Assembly model (SI-031)" | Hardware release package `hardware/releases/HW-MB-rev<X>-<n>/` (gerbers, drill, BOM, CPL, CNC drawings, exported headlessly by `kicad-cli` and the OpenSCAD CLI from `hardware/`; `cwht-MB-rev<X>-hand-assembly.csv` listing every part the owner hand-solders, SI-031), `docs/plan/integration-plan.md` (updated), `docs/test_cases/**/test_cases.json` (all Bench and OnAir cases `Active`) | Release package checklist; procedure counts by type | Hard |
| 4 | Technical data package: integrated schematics, BOM with alternates and spares, ICDs, engineering analyses, specifications | G-7 6.3 | `hardware/kicad/`, `hardware/bom/`, `docs/icd/`, `docs/design/analysis/` (RF chain, filter, PA thermal, power, derating, timing) | Package index | Hard |
| 5 | TPM status, margins and resolution of PDR discrepancies | G-7 6.4 | `docs/plan/tpm.json`; PDR log | Trend plots; burndown | Hard |
| 6 | Operational limits and constraints defined (duty cycle, temperature, battery voltage window, SWR limit, RF exposure distance) | G-7 6.5 | `docs/conops/conops.md` limits section; requirements | Table | Hard |
| 7 | Technical resource utilization and margins updated | G-7 6.6 | `docs/design/budgets.md` | Margin table | Hard |
| 8 | Acceptance plan and acceptance criteria ready to baseline | G-7 6.7; SWE-034 | `docs/vv/plan.md` acceptance section | Criteria table | Hard |
| 9 | Command and telemetry list equivalent: front-panel control map, display states, USB serial command set and status messages | G-7 6.8 | `docs/icd/ICD-CTL-SW.md`, `docs/icd/ICD-SW-HOST.md` | Tables | Hard |
| 10 | V&V plan updated | G-7 6.9 | `docs/vv/plan.md` | Change list | Hard |
| 11 | Integration plan updated | G-7 6.10 | `docs/plan/integration-plan.md` | Change list | Hard |
| 12 | Checkout and activation plan (first power-on and bring-up sequence) | G-7 6.12 | `docs/vv/plan.md` bring-up section; `docs/test_cases/sys/test_cases.json` first-power-on case | Sequence | Hard |
| 13 | Risk assessment and mitigation updated | G-7 6.16 | `docs/risk/register.json` | Render | Hard |
| 14 | SEMP updated | G-7 6.17 | `docs/plan/semp.md` | Change list | Soft |
| 15 | HSI updated with printed facade and knob fit-check (SI-012) | G-7 6.18 | SEMP HSI section; `docs/reviews/CDR/figures/` fit-check photos | Photos | Soft |
| 16 | Reliability analyses: component derating (voltage, current, power, temperature), PA thermal analysis, battery and charger safety analysis | G-7 6.20 | `docs/design/analysis/` | Derating table; thermal result | Hard |
| 17 | Cost updated with vendor quotes (tailored) | G-7 6.21 | `docs/plan/cost-estimate.md` with PCBWay and DigiKey quotes | Table | Hard |
| 18 | Subsystem-level and operations safety analyses; system safety analysis with associated verifications ready to baseline | G-7 6.24, 6.26 | `docs/safety/hazard-analysis.md`, `hazards.json`: every HZ has controls as requirements and each control has a `TC-*` | Hazard-control-verification table | Hard |
| 19 | Software products at CDR (see 6.6) | G-7 6.27 | see 6.6 | Software status table | Hard |
| 20 | Procurement status: every BOM line in stock at DigiKey or with an approved alternate; PCBWay capability confirmed; lead times in the milestone list | G-7 6.31 | `hardware/bom/`; `docs/plan/schedule.md` | Availability table | Hard |
| 21 | List of all single point failures with effects and acceptance rationale | G-7 6.32 | `docs/safety/hazard-analysis.md` SPF section | Table | Hard |
| 22 | Tool validation records for every tool that produces build or analysis outputs (kicad-cli, LTspice batch, cargo toolchain, OpenSCAD, emulator if used) | SWE-136, SWE-070; charter section 8 | `docs/cm/tool-validation/TV-NNN-<tool>.md`, summarized in `tools/toolchain.lock.md` | Table with sanity-check results | Hard |
| 23 | Manufacturability: DRC clean against the PCBWay rule set; assembly constraints met; enclosure machinability and tolerance stack checked | G-7 s16 | DRC report in `docs/reviews/CDR/`; `hardware/enclosure/` tolerance note | DRC summary | Hard |
| 24 | Engineering model or simulation evidence per plan: LTspice for every analog stage; HostUnit runs for firmware and, where used, Emulation runs (charter section 9) | G-7 s12 | `hardware/sim/`; `docs/vv/reports/` pre-power reports | Result summaries | Hard |
| 25 | All L2 TBRs closed | charter section 7 | requirements files | TBD/TBR table | Hard |

### 6.4 Success criteria

| # | Criterion | Source | Judged from |
|---|---|---|---|
| 1 | Detailed design expected to meet requirements with adequate margins | G-7 s1, s7 | Compliance matrix; budgets |
| 2 | ICDs mature enough to fabricate, assemble, integrate and test; open items managed | G-7 s2 | ICD table (all Baseline or Updated) |
| 3 | High confidence in the product baseline; documentation sufficient to proceed to fabrication and assembly | G-7 s4 | Order package checklist complete |
| 4 | Verification and validation requirements and plans complete | G-7 s5 | Every requirement has at least one `Active` test case; matrices |
| 5 | Testing approach comprehensive; assembly, integration and test planning sufficient for Phase D | G-7 s6 | Integration plan; procedure counts |
| 6 | Risks to safety and mission success understood and managed | G-7 s8 | Register |
| 7 | Safety and mission assurance addressed in the system and operational design (G-7 s9 lists safety, reliability, maintainability, quality controls, SCRM, QA and EEE parts, and system security residual risk): safety by the hazard analysis at CDR maturity with verifications assigned (row 18); reliability by the derating, PA thermal and battery analyses (row 16); maintainability by the spares list and handbook maintenance section; quality controls and QA by the receipt inspection procedure and the independent-review rule; SCRM and EEE parts by DigiKey-only sourcing with approved alternates (row 20); system security by the cybersecurity assessment (3.5 row "System Security Plan"); PRA, FMEA and the SMA plan as customized in 3.5 | G-7 s9 | Rows 16, 18, 20; 3.5 |
| 8 | Engineering models and simulations developed and exercised per plan | G-7 s12 | Row 24 |
| 9 | Parts selected; availability supports the milestone list | G-7 s14 | Row 20 |
| 10 | ConOps at CDR detail and considered in test planning | G-7 s15 | ConOps scenarios referenced by OnAir and Bench cases |
| 11 | Manufacturability included | G-7 s16 | Row 23 |
| 12 | Software components meet the CDR-point criteria in 6.6 | G-7 s17 | SA reviewer record |
| 13 | HSI sufficient to proceed | G-7 s18 | Row 15 |
| 14 | Cost within the owner's stated envelope | G-7 s3 (tailored) | Row 17; owner statement in memo |

### 6.5 Minimum products (NPR 7123.1D §5.2.2.2)

| SE id | Product | cwht artifact | Maturity leaving CDR |
|---|---|---|---|
| SE-46 | Detailed design | `hardware/kicad/`, `hardware/enclosure/`, `hardware/bom/`, `docs/design/`, `docs/test_cases/` | Baselined (product baseline) |

### 6.6 Software products required by CDR

| SWE | Product or evidence at CDR | Artifact |
|---|---|---|
| SWE-058 | Software design describing units to be coded and tested | `docs/design/software-design.md` |
| SWE-052 | Traceability extended: design components to code modules; requirements to test cases | traceability report |
| SWE-060, SWE-061, SWE-135 | Code to date follows the coding standard; static analysis (clippy, unsafe audit, complexity) results recorded | `firmware/`; CI or script output filed under `docs/reviews/CDR/` |
| SWE-062, SWE-186, SWE-189, SWE-190 | Unit tests exist for implemented units; results repeatable; coverage measured and reported | `docs/vv/reports/` |
| SWE-065 b, c | Software test procedures and test code | `docs/test_cases/sw-*/test_cases.json`; `firmware/` test code |
| SWE-071 | Test plan and procedures consistent with the software requirements | traceability report |
| SWE-134, SWE-219, SWE-220 | SWE-134 a to l provisions implemented in design for safety-critical components; MC/DC target and complexity limit planned with tooling named | `docs/design/software-design.md`; `docs/process/07-software-engineering-plan.md` |
| SWE-087 c, d, SWE-088, SWE-089 | Peer reviews of the software design and of code to date, with measurements | `docs/reviews/CDR/checklists/design-software-design.md` and `docs/reviews/CDR/checklists/code-<module>.md` (front matter `id: INSP-NNN`) |
| SWE-087 e, SWE-088, SWE-089 | Peer review of the test procedures: every `TC-SW-*` case and every Bench and OnAir case set to `Active` for CDR row 3, and the test code written to date, with `docs/templates/peer-review-checklist-test.md` (07 section 10.1 row e, "before CDR") | `docs/reviews/CDR/checklists/test-<module>.md` (front matter `id: INSP-NNN`) |
| SWE-136 | Tool validation of the build chain and, if used, the emulator | `docs/cm/tool-validation/TV-NNN-<tool>.md`; `tools/toolchain.lock.md` |
| SWE-201, SWE-202 | Nonconformance tracking active with severity levels | `docs/vv/ncr/` |
| SWE-024, SWE-200 | Actuals against plan; requirements volatility | package software status |

### 6.7 Not Applicable at CDR (in addition to 3.5)

| App. G item | Reason |
|---|---|
| G-7 6.11 "Preliminary launch site operations plan" | No launch |
| G-7 6.13 "Preliminary disposal plan" | Covered by SE-52, T per 3.5 (scope relief) |
| G-7 6.14, 6.15 "Technology readiness", "Technology Development Plan" | No technology maturation planned; a delta is reported only if the assessment changed |
| G-7 6.22, 6.23 "Updated ILSP", "Updated Project Protection Plan" | Customized (NA) per 3.5 |
| G-7 6.25 "Systems and subsystem certification plans" | Customized: the only certification is Part 97 compliance, verified through `REQ-TX-*` cases |
| G-7 6.28, 6.29 NTIA Stage 2 and Stage 4 data | Customized (NA) per 3.5 (spectrum row) |

---

## 7. Test Readiness Review (TRR)

### 7.1 Purpose

Confirm that the test article (assembled board, enclosure, firmware release), the bench environment, the procedures, the instruments and the operator are ready for the powered bench campaign, that pre-power evidence is complete, and that safety planning covers the campaign. No powered test of the delivered hardware occurs before TRR approval (charter section 3 and 9). The TRR also serves as the SIR (SE-47/48 products). Runs on a bare Pico 2 development board before hardware arrives are recorded as Bench evidence with `credit: false` and need no TRR; the TRR gates the delivered unit (charter section 3).

### 7.2 Trigger

Convened when the vendor deliveries have been received and inspected, the firmware release for run-for-record is tagged with a version description, HostUnit run-for-record reports exist (and Emulation reports where Emulation is used; charter section 9), and the Hard rows of 3.2 and 7.3 are met.

### 7.3 Entrance criteria (tailored from Table G-10, plus SIR Table G-9 items 3.1, 3.2 and 8)

| # | Criterion | Source | Evidence artifact | Shown in package as | Gate |
|---|---|---|---|---|---|
| 1 | Test objectives defined and documented for the campaign | G-10 2 | `docs/vv/plan.md` bench campaign section: objectives, sequence, pass criteria | Objective table | Hard |
| 2 | Approved test plan, procedures, environment and test-item configuration available | G-10 3; SWE-065 | `docs/vv/plan.md`; `docs/test_cases/**` (`Active`); bench setup description with photos | Procedure list in execution order | Hard |
| 3 | Test interfaces under configuration control; version descriptions for test and support systems available | G-10 4; SWE-063, SWE-187 | `firmware/releases/VDD-vX.Y.Z.md`; git tag `release/FW-vX.Y.Z` (or `release/FW-vX.Y.Z-rcN`; `05-configuration-and-data-management.md` section 4.3); `tools/toolchain.lock.md`; bench fixture list | VDD summary; hash table | Hard |
| 4 | Known discrepancies identified and dispositioned per plan | G-10 5; SWE-201 | `docs/vv/ncr/NCR-NNN.md` from receipt inspection and pre-power testing | NCR table with disposition | Hard |
| 5 | Test resources identified and available: test director (owner), instruments (NanoVNA, tinySA Ultra with attenuator, dummy load, bench supply, multimeter, Pico-based logic capture; charter section 9 and SI-013), test article, straight key, iambic paddle, headphones, cables, fixtures | G-10 6 | Instrument list cross-checked against every Bench case `instruments` field | Resource table with availability | Hard |
| 6 | Roles and responsibilities defined: owner operates the bench and reads instruments; Claude directs, records and evaluates; no test step is executed without the written procedure | G-10 7 | Package section 3 "Roles" (mandatory for TRR and every `TRR-Dn`) | Table | Hard |
| 7 | Test safety planning complete: RF only into the dummy load until Part 97 cases pass; PA thermal limit; battery and charger handling; headphone level limit; stuck-key abort | G-10 8 | `docs/safety/hazard-analysis.md` test section; safety notes in each procedure | Safety table | Hard |
| 8 | Spectrum considerations addressed (tailored): the bench campaign transmits only into the dummy load; the §97.305 and §97.307 emission cases (`TC-TX-*`, method Test on the tinySA Ultra with attenuator, or Analysis where `04-verification-and-validation.md` section 6.3 permits) are scheduled in the campaign and their pre-power Analysis evidence (LTspice filter response plus the NanoVNA-measured filter S21) is complete; antenna-connected transmission waits for the on-air delta TRR (7.6 c) | G-10 9 | `docs/vv/plan.md` regulatory section; `docs/vv/reports/` pre-power analysis; `TC-TX-*` regulatory cases `Active` | Result against the limit line; campaign slot for each case | Hard |
| 9 | As-built documentation released and under configuration control: PCB revision, assembly photos, BOM as delivered, firmware hash, fixtures | G-10 10; SWE-077 | `docs/vv/reports/receipt-inspection-<n>.md`; `docs/reviews/TRR/test-configuration-record.md` (test article and support configuration; it is the input from which `docs/vv/adp/CWHT-A-NNN/as-built.md` is written before SAR, 8.3 row 8) | As-built table | Hard |
| 10 | Integration plan updated to the as-received hardware | G-9 3.1; SE-47 | `docs/plan/integration-plan.md` | Change list | Hard |
| 11 | Initial V&V results: all Simulation, HostUnit, Emulation and Inspection cases executed for the record on the tagged release (evidence classes of 04 section 4) | G-9 3.2; SE-48; SWE-066, SWE-068 | `docs/vv/reports/` with test evaluations; test case `status` Passed, or Failed or Blocked with an open `NCR-NNN` | Pass/fail counts by class | Hard |
| 12 | CDR liens closed, or open liens shown not to affect the campaign | S2 | `docs/reviews/CDR/rfa-rid-log.json`; memo | Burndown | Hard |
| 13 | Code coverage and complexity results for safety-critical components reported | SWE-189, SWE-190, SWE-219, SWE-220 | `docs/vv/reports/` coverage report | Coverage table | Hard |
| 14 | Regression test results on the release | SWE-191 | `docs/vv/reports/` | Summary | Hard |
| 15 | Lessons-learned capture plan for the campaign (where anomalies and observations are written) | G-10 s7 | `docs/lessons-learned.md`; NCR process | One paragraph | Soft |
| 16 | Board-level mechanical and electrical interfaces checked against the ICDs before integration, unpowered, on receipt: every connector pinout and the key, paddle, headphone, antenna, USB and battery interfaces against their `ICD-*` pin maps (continuity); no rail shorted to ground or to another rail (resistance per the integration plan); board outline and mounting holes against the mechanical-envelope ICD between the board and the enclosure. Every failed check is an `NCR-NNN`. Rail voltages are powered checks, so they are the first steps of the bring-up case after TRR approval (7.1), not an entrance item | G-9 8 | `docs/vv/reports/receipt-inspection-<n>.md` interface-check section; `docs/icd/ICD-*.md`; `docs/plan/integration-plan.md` bring-up sequence | Check table by ICD with result | Hard |

### 7.4 Success criteria

| # | Criterion | Source | Judged from |
|---|---|---|---|
| 1 | Test plans complete and approved for the system under test | G-10 s1 | Row 2 |
| 2 | Test resources identified and coordinated | G-10 s2 | Row 5 |
| 3 | Risks identified, assessed, mitigated; residual risk accepted by the owner | G-10 s5, s6 | Register; memo |
| 4 | Objectives defined; review of plans, procedures, environment and configuration gives a reasonable expectation the objectives will be met | G-10 s8 | Rows 1 to 3 |
| 5 | Test cases analyzed and consistent with plans and objectives | G-10 s9 | Traceability report (every Bench case cites requirements; every requirement with method Test or Demonstration has a case) |
| 6 | Operator prepared: safety notes read and acknowledged in the readiness confirmation | G-10 s10 (customized) | Readiness declaration |
| 7 | Lessons-learned capture planned | G-10 s7 | Row 15 |
| 8 | Previous component and software test results form a satisfactory basis for proceeding | G-9 s2 | Row 11 |
| 9 | Integration plans and procedures are on track for completion and approval to support integration: the updated integration plan (row 10) and the bring-up case of `docs/test_cases/sys/test_cases.json` are `Active` and peer-reviewed | G-9 s1 | Rows 2 and 10; `docs/reviews/TRR/checklists/test-sys.md` |
| 10 | Integration procedures and workflow are defined and documented: the bring-up sequence (firmware load, power rails, RF chain, enclosure fit) names each step's procedure, instrument and pass criterion | G-9 s7 | `docs/plan/integration-plan.md` sequence table |
| 11 | The review of the integration plan, procedures, environment and configuration of the items to be integrated gives a reasonable expectation that integration will succeed: unpowered interface checks passed (row 16), known discrepancies dispositioned (row 4), configuration recorded (rows 3 and 9) | G-9 s8 | Rows 3, 4, 9 and 16 |

### 7.5 Minimum products

| SE id | Product | cwht artifact | Maturity leaving TRR |
|---|---|---|---|
| SE-47 | Updated integration plan | `docs/plan/integration-plan.md` | Updated |
| SE-48 | Initial V&V results | `docs/vv/reports/` | Initial |

Software products required by TRR:

| SWE | Product or evidence at TRR | Artifact |
|---|---|---|
| SWE-063 | Version description for the run-for-record release | `firmware/releases/VDD-vX.Y.Z.md`; tag `release/FW-vX.Y.Z` or `release/FW-vX.Y.Z-rcN` |
| SWE-187 | Configuration control before test per `05-configuration-and-data-management.md` section 7.3 (tests run on a tagged release with a VDD; every report records, in the front matter of `docs/templates/verification-report.md`, the release `firmware_version`, the source commit `source_commit`, the ELF SHA-256 `firmware_elf_sha256`, the harness and emulator versions `harness_versions`, the toolchain lock commit `toolchain_lock` and the `test_cases.json` blob hash `procedure_blob` at `procedure_commit`) and the interim configuration check of 05 section 7.4 by the independent reviewer (tags present and pushed, CSA current, firmware hash matches the VDD) | `docs/reviews/TRR/test-configuration-record.md`, whose section "Interim configuration check" is written by the independent reviewer agent (invocation named, commands and outputs pasted; 05 section 7.4 findings become RIDs only on owner adoption, 10.1) |
| SWE-087 e, SWE-088, SWE-089 | Peer review of every test procedure used for the record in the campaign before its first run for the record: Bench and OnAir cases and any `TC-SW-*` case changed since CDR (G-10 3; SWE-088 b readiness criteria) | `docs/reviews/TRR/checklists/test-<module>.md` (front matter `id: INSP-NNN`) |
| SWE-065 d | Test reports for the pre-power classes | `docs/vv/reports/` |
| SWE-066, SWE-068 | Execution on the tagged release and evaluation of results | `docs/vv/reports/` |
| SWE-073 | Not a TRR product: SWE-073 is met on the target platform (8.6; 04 section 17; `rmm.json` row SWE-073). The HostUnit and Emulation reports presented at TRR are pre-target risk reduction and supporting evidence (Emulation for event order only, ADR-011), and the target-platform validation runs in the Bench and OnAir series on `CWHT-A-001` | HostUnit and Emulation reports in `docs/vv/reports/` (supporting) |
| SWE-189, SWE-190, SWE-219, SWE-220 | Coverage and complexity for safety-critical components | `docs/vv/reports/TC-SW-COV-001-r<N>.md` |
| SWE-191 | Regression results on the release | `docs/vv/reports/` |
| SWE-192 | Hazard-tracing requirements tested | traceability report; `docs/vv/reports/` |
| SWE-201, SWE-202 | Nonconformances tracked with severity levels | `docs/vv/ncr/` |
| SWE-203 | Reuse assessment for the release: advisories and upstream issues of the rustos drivers and every pinned crate reviewed (07 section 17.1) | VDD reuse-assessment section (RMM SWE-203); resulting nonconformances as `docs/vv/ncr/NCR-NNN.md` tagged `reuse` |

SWE-084 (configuration audits) is a SAR product (section 8.6, `05-configuration-and-data-management.md` section 7) and is not attributed to TRR.

### 7.6 Delta TRRs

A delta TRR (`TRR-D1`, `TRR-D2`, ...) is held, with a package limited to the changed rows of 3.2 and 7.3, before every new run-for-record series (charter section 3): (a) run-for-record on a new firmware release or release candidate, or on a newly delivered unit `CWHT-A-NNN`; (b) any change to the bench configuration or procedures, including a new instrument or fixture, and any resumption of testing after an S1 or S2 NCR (`04-verification-and-validation.md` section 10.3); (c) the start of the on-air series (antenna connected), which additionally requires every regulatory `REQ-TX-*` emission case (47 CFR §97.305, §97.307) to be Passed and whose decision memo carries the OnAir authorization section (`04-verification-and-validation.md` section 6.3). A delta TRR produces its own package, deck, log and decision memo in `docs/reviews/TRR-Dn/` and no baseline tag. It is presented like every gate (3.4) from `docs/reviews/TRR-Dn/slides/trr-dn.adoc` (for example `trr-d1.adoc`), which covers the full minimum slide set of charter section 4 item 2. A slide whose content is unchanged since `TRR` or `TRR-Dn-1` says so and cites that package section. Development-board runs (7.1) are not a run-for-record series and need no delta TRR.

### 7.7 Not Applicable at TRR (in addition to 3.5)

| App. G item | Reason |
|---|---|
| G-10 s11 spectrum manager concurrence | Customized (NA) per 3.5 (spectrum row); intent carried by 7.3 row 8 |
| G-9 10, 11, 14 integration facilities, trained support personnel, quality control organization | Customized: the bench is the owner's desk; roles in row 6 |
| G-9 15.5, 15.6 transportation criteria, mission operations plans | Customized (NA): no transport campaign beyond the vendor delivery (receipt inspection covers it) and no mission operations; 15.6 per 3.5 launch row |
| G-9 15.7, 15.8 decommissioning and disposal plans | Covered by SE-51 and SE-52, T per 3.5 (scope relief) |
| G-9 6, 7, 9, 12, 13 integration procedures scheduled, components available, unit-level testing done, handling and safety documented, discrepancies dispositioned | Carried by 7.3 rows 2, 4, 7, 10 and 11 and 7.4 rows 9 to 11; no separate entry |

---

## 8. System Acceptance Review (SAR)

### 8.1 Purpose

Verify that the delivered radio and its firmware satisfy every requirement (verification) and the owner's expectations in the ConOps scenarios (validation), that the acceptance criteria are met, that the as-built configuration matches the product baseline (functional and physical configuration audits), and that the operations handbook and enabling products allow the owner and friends to operate the radio. The SAR also serves as the ORR (Table G-12 operations items) and closes SE-53/54.

### 8.2 Trigger

Convened when every Bench and OnAir case is Passed or dispositioned by an accepted NCR, the operations handbook has been walked through as an OPS scenario, the FCA and PCA are done, and the Hard rows of 3.2 and 8.3 are met.

### 8.3 Entrance criteria (tailored from Table G-11 plus Table G-12 items 1 to 3, 5 to 7, 9.3 to 9.5 and 12)

| # | Criterion | Source | Evidence artifact | Shown in package as | Gate |
|---|---|---|---|---|---|
| 1 | All planned bench and on-air testing complete | G-12 1 | `docs/test_cases/**` statuses; `docs/vv/reports/` | Completion table by class | Hard |
| 2 | Product verification results: every requirement Verified, or dispositioned by NCR with owner acceptance. Each `REQ-SW-*` verified by HostUnit or Emulation is Verified on a `credit: true` report against the tagged release; it becomes Closed in the commit that records the signed SAR decision memo, and only when PCA-05 (row 9; 04 section 5.3) has confirmed that release is installed on the delivered unit (charter section 9) | G-11 3.2; SE-53 | Verification matrix from `tools/traceability.py`; `docs/vv/reports/vv-report.md` | Matrix summary; exceptions table | Hard |
| 3 | Product validation results: every OPS scenario demonstrated; every MOE assessed against target | G-11 3.3; SE HB §5.4 | Validation matrix; `docs/vv/reports/vv-report.md` validation section | MOE table with achieved values | Hard |
| 4 | Compliance with the acceptance criteria documented | G-11 3.4; SWE-034 | `docs/vv/plan.md` acceptance section with results | Criteria table with pass/fail | Hard |
| 5 | Performance in the expected operational environment documented: on-air contacts, battery endurance, temperature range covered | G-11 3.5; G-12 s7 | OnAir reports; environment cases | Results | Hard |
| 6 | Technical data package updated with all test results | G-11 3.6 | `docs/design/`, `hardware/`, `docs/vv/reports/` | Package index with commits | Hard |
| 7 | Certification for use (customized): Part 97 compliance statement listing each regulatory requirement, its verification case and result, and the owner's licence class; it is part of the acceptance data package of 8.5 | G-11 3.7 via 8.5; SE-54 | `docs/vv/reports/part97-compliance.md` | Statement | Hard |
| 8 | As-built hardware and software documentation baselined: per-unit as-built record, VDD, firmware hash, BOM as built, PCB revision, enclosure revision | G-11 3.8; G-12 9.3; SWE-063, SWE-077 | `docs/vv/adp/CWHT-A-NNN/as-built.md` (one per unit); `docs/reviews/SAR/baseline-record.md`; `firmware/releases/VDD-<version>.md` | As-built table per unit | Hard |
| 9 | Functional and physical configuration audits complete | charter section 8; SWE-084 | `docs/reviews/SAR/configuration-audit.md` (as-built vs product baseline; firmware hash vs VDD) | FCA/PCA result table | Hard |
| 10 | Test anomalies resolved; results, mitigations and work-arounds incorporated into the operations handbook | G-12 2 | `docs/vv/ncr/`; `docs/ops/operations-handbook.md` | NCR closure table | Hard |
| 11 | Risk assessment updated; residual risks stated for operations | G-11 3.9 | `docs/risk/register.json` | Render | Hard |
| 12 | Safety, handling, checkout and operational procedures written and verified: operations handbook with nominal and contingency procedures (high SWR, over-temperature, low battery, stuck key, RF exposure distance) and the end-of-life section (3.5, SE-51/52) | G-11 3.10; G-12 5, 7, 9.4, 9.5 | `docs/ops/operations-handbook.md` | Table of contents; contingency list | Hard |
| 13 | Operational enabling products delivered: charger, USB cable, firmware loading tool and instructions, key and paddle cable pinout, headphone spec | G-12 3 | `docs/ops/operations-handbook.md` kit list; `docs/icd/` | Kit list | Hard |
| 14 | Operators prepared (customized): the owner performs the handbook walkthrough as a Demonstration case; friends receive the handbook with the radio | G-12 6 | `TC-SYS-*` walkthrough case Passed | Result | Soft |
| 15 | Software products at SAR (see 8.6) | G-11 3.11 | see 8.6 | Software status table | Hard |
| 16 | Sustaining plan: maintenance section, spares, firmware update path, rev B backlog | G-11 3.13 | `docs/ops/operations-handbook.md`; `docs/lessons-learned.md` | Paragraph and backlog list | Soft |
| 17 | Single point failure list updated with test evidence | G-11 3.14; G-12 12 | `docs/safety/hazard-analysis.md` | Table | Soft |
| 18 | Lessons learned captured for the project and for operations | G-11 s6; G-12 s2 | `docs/lessons-learned.md` | Entries | Hard |
| 19 | All TBRs resolved; no TBDs | G-11 s4 | requirements files | TBD/TBR table (must be empty) | Hard |
| 20 | Receipt inspection reports for all vendor deliveries | G-11 3.1 (customized) | `docs/vv/reports/receipt-inspection-<n>.md` | Table | Hard |

### 8.4 Success criteria

| # | Criterion | Source | Judged from |
|---|---|---|---|
| 1 | Required tests and analyses complete; system will perform in the operational environment | G-11 s1; G-12 s7 | Rows 1 to 5 |
| 2 | Risks mitigated to acceptable levels; residual risk accepted by the owner | G-11 s2; G-12 s6 | Row 11; memo |
| 3 | System meets the acceptance criteria | G-11 s3 | Row 4 |
| 4 | TBD and TBR items resolved | G-11 s4 | Row 19 |
| 5 | Acceptance data package complete and reflects the delivered system, including the PCA-05 installed-release line for the delivered unit, so that every `REQ-SW-*` verified by HostUnit or Emulation is Verified with PCA-05 confirmed and is set to Closed in the commit that records the signed SAR decision memo (04 section 5.3; `tools/traceability.py` rule `CLOSED_WITHOUT_SAR`) | G-11 s5 | Rows 2 and 6 to 9 |
| 6 | Lessons learned captured | G-11 s6 | Row 18 |
| 7 | Hardware, software, documentation and enabling products complete and ready for acceptance | G-11 s9; G-12 s1, s4 | Rows 8, 12, 13 |
| 8 | All waivers, liens and anomalies closed or accepted with rationale in the memo | G-12 s3 | RFA/RID logs; NCRs |
| 9 | Software components meet the SAR-point criteria in 8.6 | G-11 s7 | SA reviewer record |
| 10 | HSI operational capability established: controls, display, audio and keying usable as intended by the owner in the walkthrough | G-12 s13 | Row 14 |

### 8.5 Minimum products and the acceptance data package

| SE id | Product | cwht artifact | Maturity leaving SAR |
|---|---|---|---|
| SE-53 | Baseline V&V results (FRR product delivered at SAR; customization, FC) | `docs/vv/reports/vv-report.md`; matrices | Baselined (as-built baseline) |
| SE-54 | Final certification for use (FRR product delivered at SAR; customization, FC) | SAR decision memo acceptance statement; `docs/vv/reports/part97-compliance.md` | Final |
| SE-69 | Preliminary V&V results | superseded by SE-53 | n/a |
| SE-51, SE-52 | Decommissioning and disposal plans (ORR products, due at SAR because the ORR is combined with SAR) | T (scope relief, 3.5); location customized: the end-of-life section of `docs/ops/operations-handbook.md` (cells to recycler, board and enclosure as e-waste, unit `CWHT-A-NNN` marked retired in its as-built record `docs/vv/adp/CWHT-A-NNN/as-built.md`) | Baselined (as-built) |
| SE-55, SE-56 | Updated decommissioning and disposal plans (DR and DRR products) | T (review not held, 3.5): the same handbook section under CR control until the repository is archived; the archive action is the final `CR-NNN` | n/a (no DR or DRR) |

The acceptance data package for unit `CWHT-A-NNN` is indexed from `docs/vv/adp/CWHT-A-NNN/` (charter section 5) and is the set: per-unit as-built record `as-built.md`, the SAR baseline record, VDD, V&V report with matrices, Part 97 compliance statement, NCR closure list, operations handbook, configuration audit record, receipt inspection reports, kit list.

### 8.6 Software products required by SAR

| SWE | Product or evidence at SAR | Artifact |
|---|---|---|
| SWE-063 | Version description for the accepted release | `firmware/releases/VDD-<version>.md` |
| SWE-194 | Pre-delivery verification: every software requirement met or dispositioned, approved changes implemented, defects designated for resolution resolved | `docs/vv/reports/vv-report.md` software section |
| SWE-077 | Software delivered with as-built records | `docs/vv/adp/CWHT-A-NNN/as-built.md`; `docs/reviews/SAR/baseline-record.md` |
| SWE-068, SWE-065 d | Test evaluations and reports for all classes | `docs/vv/reports/` |
| SWE-073 | Validation on the target platform (bench and on-air) | OnAir and Bench reports |
| SWE-084, SWE-083 | Configuration audit and status records | `docs/reviews/SAR/configuration-audit.md`; `docs/process/configuration-status.md` (generated) |
| SWE-085 | Release, storage and delivery procedure followed (firmware image, loader instructions) | `docs/ops/operations-handbook.md`; `docs/process/05-configuration-and-data-management.md` |
| SWE-189, SWE-190 | Final code coverage results for the accepted release, with every shortfall dispositioned per 07 section 9.5 | `docs/vv/reports/TC-SW-COV-001-r<N>.md` |
| SWE-219 (as tailored in the RMM) | MC/DC target of 100 % for safety-critical components shown by independently reviewed decision tables and independence-pair tests (07 section 9.6); the MSR-14 nightly branch and condition measure is attached as a non-credit supporting measure (charter section 10). **Relief of a shortfall (single statement; proposed here, decided by the owner at SRR and listed in the SRR package proposed-tailoring section):** the RMM row SWE-219 (disposition T) is the relief for the method and is not reopened by a shortfall. The NPR 7150.2D §3.7.4 note to SWE-219 says that any deviation from 100 percent should be reviewed and waived with rationale by the Technical Authorities' approval, so a shortfall against 100 percent in the tailored method is a product waiver (05 section 2) that the owner as Technical Authority approves with rationale as a numbered item `W<n>` in the CDR, TRR or SAR decision memo; it is entered in CSA item 12 and listed in VDD section 7. It is distinct from an SWE-220 complexity exceedance waiver, which cites SWE-220's own clause | `docs/vv/reports/TC-SW-COV-001-r<N>.md` MC/DC table; decision memo waiver entry `W<n>` |
| SWE-220 | Cyclomatic complexity of 15 or lower for every safety-critical component; any exceedance is reviewed and waived with rationale by the owner as project manager and technical approval authority, as SWE-220 provides, and listed in the VDD | coverage report complexity section; decision memo waiver entry |
| SWE-192 | Every software requirement that traces to a hazardous event, cause or mitigation technique verified through test on the target: the Bench and OnAir reports for the `REQ-SW-*` listed in the `control_req_ids` of `docs/safety/hazards.json` | `docs/vv/reports/` Bench and OnAir reports; traceability report hazard section |
| SWE-201, SWE-202, SWE-204 | Nonconformances tracked with severities and closed or accepted; process assessments for every S1 and S2 nonconformance recorded | `docs/vv/ncr/` |
| SWE-203 | Assessment of every reported nonconformance in reused or external software (rustos drivers, crates listed in the third-party notice file of 07 section 17.1) for the accepted release | `docs/vv/ncr/` entries tagged `reuse`; VDD reuse-assessment section |
| SWE-087 d, e, SWE-088, SWE-089 | Peer review records for the final code of the accepted release and for any test procedure changed since TRR (earlier procedure reviews are the CDR and TRR records, 6.6 and 7.5) | `docs/reviews/SAR/checklists/code-<module>.md` and `docs/reviews/SAR/checklists/test-<module>.md` (front matter `id: INSP-NNN`) |
| SWE-195 | Maintenance under the same class and processes committed | `docs/process/07-software-engineering-plan.md` maintenance section |
| SWE-052 | Full traceability set including requirements to nonconformances | traceability report |

### 8.7 Not Applicable at SAR (in addition to 3.5)

| App. G item | Reason |
|---|---|
| G-11 3.12, G-12 10, 11 NTIA Stage 4 certification and RF authorizations | Customized (NA) per 3.5 (spectrum row); the owner's amateur licence (SI-014) is the authorization, referenced in row 7 |
| G-12 8.2, 8.3 decommissioning and disposal plans | T per 3.5 (SE-51, SE-52, scope relief): end-of-life section of the operations handbook, baselined at SAR (8.5) |
| G-12 9.1, 9.2 cost and schedule, Project Protection Plan | Cost and schedule: Customized (substitute), final actuals in `docs/plan/cost-estimate.md` and `docs/plan/schedule.md` (3.5 programmatic row); PPP: Customized (NA) per 3.5 |
| G-12 9.6, 9.7 preliminary certification for flight, Human Rating | Customized (NA) per 3.5 (launch and human-rating rows) |

---

## 9. Review completion checklist (NPR 7123.1D §5.2.3.1)

A review is complete, and the next phase may start, only when every row is done and recorded in `docs/reviews/<REVIEW>/decision-memo.md`.

| §5.2.3.1 | Completion item | cwht action | Record |
|---|---|---|---|
| a | Agreement on the disposition of all RIDs and RFAs | Every item in the log is Closed or Withdrawn, or carries `lien: true` with an owner-accepted closure plan and due event (section 12.2); Major RIDs and Blocking RFAs are Closed | `rfa-rid-log.json`; memo section "RFA/RID summary" |
| b | Review board report and minutes complete and distributed | `minutes.md` written in slide order (attendance, slide number, questions and answers, decisions, RFAs and RIDs raised against each slide, 3.4); committed | `docs/reviews/<REVIEW>/minutes.md` |
| c | Agreement on a plan for insufficient performance against success criteria | Each success criterion marked Met, Met with lien (lien id), or Not met; Not met forces disposition *Not approved* | memo success-criteria table |
| d | Agreement on a plan for actions from the review | Each RFA has assignee and due event; actions that change a baseline reference a `CR-NNN` | log; memo liens table |
| e | Liens closed or on an adequate and timely plan | Liens table complete (section 12) | memo |
| f | Differences of opinion resolved or on a plan | Presenter dissent, if any, recorded with the owner's ruling | memo "Dissent" block |
| g | Chair report to management | The chair is the owner and Decision Authority; the memo is the report | memo |
| h | Procedures and controls to follow actions to closure | Open items carried in the next package's burndown; review-trend TPM updated | next `package.md`; `docs/plan/tpm.json` |
| i | Decision Authority signs the decision memo | Owner's approval wording transcribed with date; memo committed; for SRR, PDR, CDR and SAR the baseline procedure of `05-configuration-and-data-management.md` section 4.4 runs (steps 1 to 6, section 2), ending with the post-tag record commit whose `pushed_hash` key records the `git ls-remote --tags origin baseline/<review>` hash | memo signature block; baseline record; git tag on `origin` |

Additional cwht completion items:

- Baseline record written (`baseline-record.md`, template `docs/templates/baseline-record.md`), listing every CI with its hash and stating that the tag was pushed.
- Approved tailoring rows moved from "proposed" to "approved" in `rmm.json` and `se-compliance-matrix.json`.
- New ADRs written for any decision taken at the review (charter section 11.6).
- This document and the SEMP review schedule updated with the review's results (NPR 7123.1D §5.2.1.2): new or changed criteria, customizations learned at the review, and the next gate's trigger. After SRR this is done by `CR-NNN`, raised within the same working session as the memo commit.

## 10. RFA and RID process

### 10.1 Definitions

NPR 7123.1D App. A defines RFAs and RIDs as the comment forms reviewers submit during life-cycle reviews to capture comments, concerns and issues, with the disposition process defined locally. On cwht (charter section 4.3):

- **RFA, Request for Action** `RFA-<REVIEW>-NNN`: a question to answer, an analysis to perform, or a plan to produce. It does not by itself assert a defect. Answering an RFA may create RIDs, CRs, ADRs or risks.
- **RID, Review Item Discrepancy** `RID-<REVIEW>-NNN`: a specific defect in a reviewed product: a wrong, missing, unverifiable or inconsistent statement, figure, value, interface or design element, identified by product path and element id.
- **Independent reviewer findings** (from the `docs/reviews/<REVIEW>/checklists/<product-slug>.md` records, front matter `id: INSP-NNN`, section 13) are not RIDs until the owner adopts them at the review. Claude presents every open finding in package section 15. The owner marks each finding *Adopt as RID*, *Adopt as RFA* or *No action*, and the ruling is recorded against the finding's `#finding-<n>` entry in its record. This rule applies to every technical review of section 2.1, including the SWE-143 architecture review.
- **Not RFAs or RIDs:** defects found in delivered hardware or in firmware behaviour during testing are `NCR-NNN` (charter section 9); changes to a baselined item are `CR-NNN`. A RID against a baselined item is closed by a CR, and the log records the CR id as evidence (`kind: cr`). The only exception is a fix that is an editorial change as `05-configuration-and-data-management.md` section 2 defines it (no technical meaning altered); it is a commit carrying the `Editorial:` trailer and is recorded as `kind: commit` with the note `Editorial` (10.5). Adding or changing a scenario step, a displayed message, a value or a "shall" is never editorial.

### 10.2 Severity

| Type | Severity | Meaning | Closure deadline |
|---|---|---|---|
| RID | Major | Blocks the baseline: a requirement, interface, hazard control, safety-critical design element or regulatory item is wrong or missing, or a Hard entrance criterion was met only apparently | Closed before the decision memo is signed and the baseline tag is created; a Major RID is never a lien |
| RID | Minor | Editorial, clarity, consistency, or a defect with a contained fix that does not change the baseline's meaning | Closed before the next gate's readiness declaration |
| RFA | Blocking | The answer may change the baseline or the disposition | Closed before the decision memo is signed; a Blocking RFA is never a lien |
| RFA | Routine | Answer needed for the next phase | Closed before the next gate's readiness declaration, or by the `due_date` set by the owner |

The owner sets severity when raising the item. Claude may propose a change of severity with rationale; the owner accepts or rejects it, and an accepted change is logged as a same-state `history` entry (10.3).

### 10.3 States and transitions

| State | Entered when | Who | Required fields |
|---|---|---|---|
| Open | Item raised before or during the review, or during package review | Originator (owner; or Claude on the owner's instruction) | `id`, `type`, `severity`, `review`, `originator`, `opened`, `product`, `description`, `assignee`, `due_review` or `due_date` |
| Answered | Assignee delivers the fix, answer, analysis or plan with evidence | Assignee (Claude by default) | `response`, `evidence[]` (at least one), `answered` |
| Verified | Evidence checked against the item: for a RID, by an independent reviewer agent that is not the author of the fix; for an RFA, by the owner | Reviewer agent (RID) or owner (RFA) | `verification` (`role`, `date`, `result` = Verified; for RIDs, `record` is mandatory: the path of the verifying reviewer's filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, whose front matter carries `id: INSP-NNN`, charter section 5) |
| Open (from Answered) | Verifier records `verification.result` Rejected: the evidence does not close the item | Reviewer agent (RID) or owner (RFA) | `verification` (`role`, `date`, `result` = Rejected, `note` with the reason); `history` entry from Answered to Open carrying the rejection note |
| Open (from Verified) | Owner declines closure of a Verified item (for example, the fix is correct but incomplete for the owner's intent) | Owner | `history` entry from Verified to Open with the owner's reason in `note`; the `verification` object is kept as the record of the earlier check and is overwritten only by the next verification |
| Closed | Owner accepts closure; allowed from Verified only | Owner | `closed`, `closed_by`, `disposition` |
| Withdrawn | Originator withdraws (duplicate, overtaken by events, raised in error); allowed from Open or Answered only | Originator | `closed`, `disposition` = Withdrawn, `withdrawal_reason` |

Rules:

- No state is skipped. Closed and Withdrawn are terminal, and a Closed or Withdrawn item is never reopened.
- An Answered item returns to Open only through a Rejected verification. A Verified item returns to Open only when the owner declines closure.
- A recurrence after closure is a new item whose `supersedes` field names the old id (charter section 6: IDs are never reused).
- Every transition appends a `history` entry (`date`, `from`, `to`, `by`, `note`).
- An event that changes no state appends a `history` entry with `from` equal to `to`, by the actor who made it, and a `note` naming its record. Two events do this:
  - Lien acceptance at signing: note `Lien accepted in docs/reviews/<REVIEW>/decision-memo.md`, by `owner`, dated the memo's `signed` date.
  - Owner-accepted severity change (10.2): note `Severity <old> to <new>: <rationale>`.
- `tools/review_trend.py` reads states from the history, so same-state entries do not change any count.

### 10.4 Ownership

- **Originator:** the owner. Reviewer agents originate findings, not RIDs (10.1).
- **Assignee:** Claude (main session) unless the owner assigns the item to himself (a decision he must make) or to a named agent role.
- **Verifier:** for RIDs an independent reviewer agent (product reviewer or software assurance role) that did not author the fix, using the checklist for the product type; for RFAs the owner.
- **Closer:** the owner, in conversation, transcribed into the log and the memo by Claude.
- **Log keeper:** Claude. On every change to a log and before every readiness declaration, Claude runs two checks and both must exit 0:
  1. `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`. This runs the schema. It also checks that the log's `review` equals its folder name, and that every `verification.record` exists.
  2. The item check below. It confirms that every item's `review` equals the log's `review` and that every id starts with `<type>-<review>-`. The schema cannot enforce the exact `n` of a `TRR-Dn` log: a `TRR-D1` log holding `RID-TRR-D2-001` passes the schema but fails this check.

```
/Users/robinonsay/rust/cwht/.venv/bin/python -c 'import json,sys,pathlib; p=pathlib.Path(sys.argv[1]); d=json.load(open(p)); r=d["review"]; bad=[i["id"] for i in d["items"] if i["review"]!=r or not i["id"].startswith(i["type"]+"-"+r+"-")]; assert r==p.parent.name, "review "+r+" but folder "+p.parent.name; assert not bad, "items of another review: "+", ".join(bad); print("ok")' /Users/robinonsay/rust/cwht/docs/reviews/<REVIEW>/rfa-rid-log.json
```

### 10.5 Closure evidence

Each `evidence` entry has `kind`, `ref`, `note`. Accepted kinds and what they must point to:

| kind | ref | Accepted for |
|---|---|---|
| commit | git commit hash containing the fix | Any RID whose product is not yet baselined (Minor RIDs against unbaselined items; Major RIDs, which always close before the baseline tag, 10.2); a RID against a baselined item only when the fix is editorial per 05 section 2 (commit trailer `Editorial:`, evidence `note` `Editorial`, 10.1) |
| cr | `CR-NNN` approved by the owner (`docs/cm/cr/CR-NNN-<slug>.md`) | Every non-editorial fix to a baselined item, including a lien closed after the gate's baseline tag (10.1; 12.2; 05 section 5.1) |
| tool-validation | `TV-NNN` (`docs/cm/tool-validation/TV-NNN-<tool>.md`) | RFAs and RIDs about the credibility of a tool's output (SWE-136) |
| adr | `ADR-NNN` | RFAs answered by a decision |
| trade-study | `TS-NNN` | RFAs answered by analysis with alternatives |
| analysis | path under `docs/design/analysis/`, `hardware/sim/` or `docs/research/` | RFAs answered by analysis |
| test-case | `TC-<MOD>-NNN`, or its verification report id `TC-<MOD>-NNN-rN` (charter section 6) when a run is the evidence | RIDs about verification coverage |
| report | path under `docs/vv/reports/` | RFAs and RIDs about results |
| figure | path under `docs/reviews/<REVIEW>/figures/` | RIDs about visual products |
| traceability-report | `docs/reviews/<REVIEW>/traceability-report.md` of a passing run (3.1 item 2) | RIDs about traceability |
| ncr | `NCR-NNN` | Items transferred to nonconformance handling |
| risk | `RSK-NNN` | RFAs whose answer is a new or changed risk |
| requirement | `REQ-<MOD>-NNN` (new or changed) | RIDs about requirements |
| memo | `docs/reviews/<REVIEW>/decision-memo.md` | Owner decisions recorded at the review |

The schema enforces one `ref` pattern per kind (identifier form or path prefix as listed), so an evidence entry with the wrong reference form fails validation.

### 10.6 Log file

One log per review: `docs/reviews/<REVIEW>/rfa-rid-log.json`, schema `docs/templates/rfa-rid-log.schema.json`, example `docs/templates/rfa-rid-log.example.json`. Validate with the project validator, which covers every `docs/reviews/*/rfa-rid-log.json` against this schema together with the other structured files and the template example:

```
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py
```

Fallback when only one log is to be checked (schema only; the folder and record-existence checks of `validate_docs.py` do not run):

```
/Users/robinonsay/rust/cwht/.venv/bin/python -c "import json,jsonschema,sys; s=json.load(open('/Users/robinonsay/rust/cwht/docs/templates/rfa-rid-log.schema.json')); d=json.load(open(sys.argv[1])); jsonschema.Draft7Validator(s).validate(d); print('ok')" /Users/robinonsay/rust/cwht/docs/reviews/<REVIEW>/rfa-rid-log.json
```

Numbering: `NNN` starts at 001 per review and per type and never restarts within a review folder (delta reviews have their own folder and sequence). The checks are split as follows:

- The schema rejects an item whose id or `review` names a fixed review token (SRR, PDR, CDR, TRR, SAR) other than the log's own.
- For a delta TRR log, the schema checks only the `TRR-Dn` form. The exact `n` is checked by the item check of 10.4.
- `tools/validate_docs.py` checks that the log's `review` names its own folder.
- The schema also rejects a Major RID or Blocking RFA with `lien: true` (10.2).

## 11. Review-trend TPM (NPR 7123.1D SE-64)

SE-64 (NPR 7123.1D §6.2.9) requires a set of review trends that is created and maintained and that covers closure of review action documentation (RIDs, RFAs, action items). SE-60 and SE-61 (§6.2.6, §6.2.7) require TPMs that track current state against plan and are reported at an agreed interval.

On cwht the review trend is the TPM `TPM-003` (key `review-trend`) in `docs/plan/tpm.json`. It is reported at every gate (SE-61) and computed by `tools/review_trend.py`, which is listed in `docs/process/README.md`, in `08-agent-briefing.md` section 1 and in SEMP section 4.3. The tool is validated per charter section 8 by `tools/tests/test_review_trend.py`. The test runs the tool on the fixture `tools/tests/fixtures/review_trend/`, which holds a copy of `docs/templates/rfa-rid-log.example.json` and an SRR memo with `signed: 2026-10-05`, and compares the output with the hand-computed values below. Its test `test_fixture_log_is_the_template` also requires the fixture log to equal the template example.

**Inputs.** Every value is reproducible from the repository alone, because the tool reads only these three sources:

- Every `docs/reviews/*/rfa-rid-log.json`.
- The package date `T`, passed as `--date YYYY-MM-DD` and defaulting to the current date.
- The gate dates: the `signed` front-matter key of every `docs/reviews/*/decision-memo.md` (template `docs/templates/decision-memo.md`).

`signed` is set only when the owner's wording approves the review (*Approved* or *Approved with liens*). It stays `null` for a *Not approved* session and while the memo is unsigned. A review is dispositioned at `T` when its memo carries a `signed` date on or before `T`. A memo with `signed: null` is not a gate date, so the tool ignores it for overdue and closure-fraction purposes.

**Command** (3.1 item 3):

```
/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/review_trend.py --date <T> --package <REVIEW> --write
```

`--package` names the review whose package is being built. With `--write`, the tool:

- writes the plot to `docs/reviews/<REVIEW>/figures/review-trend.png`;
- appends one history entry per logged review to `TPM-003` in `docs/plan/tpm.json`. It replaces any entry from an earlier run for the same package and date, and changes only that history array. Claude does not hand-edit `TPM-003` history.

Without `--write`, the tool prints the text summary (or JSON with `--json`) and writes nothing. Exit status: 0 when every zone is Green or Yellow, 1 when any zone is Red, 2 on invalid input.

**Measures.** Every state is evaluated at `T` from the item's `history`. Measures are computed per review `R`, per type (RFA, RID) and per severity (all, Major, Minor, Blocking, Routine):

| Measure | Definition |
|---|---|
| raised | items of `R` opened on or before `T` |
| open | items in state Open or Answered at `T` |
| verified_pending | items in state Verified at `T` |
| closed | items in state Closed at `T` |
| withdrawn | items in state Withdrawn at `T` |
| overdue | open or verified_pending items whose `due_date` is earlier than `T`, or whose `due_review` has a memo signed earlier than `T` |
| next gate of `R` | the first review after `R`, in the order SRR, PDR, CDR, TRR, TRR-D1, TRR-D2, ..., SAR, whose memo is signed on or before `T` |
| closure_fraction_at_gate | closed / (raised - withdrawn) for `R`, evaluated at the signed date of the next gate of `R`. It is **undefined** until that memo is signed, and when raised equals withdrawn |
| age_open (median, max) | `T - opened` in days over open items |
| age_closed (median) | days from `opened` to the date the item entered Closed, over closed items |

**Burndown series per review.** The series has one point for every date on which an item of `R` was raised, closed or withdrawn, that is, every date on which cumulative raised or cumulative closed-plus-withdrawn changes. Each point carries cumulative raised and cumulative closed plus withdrawn. Dates on which an item only moved between Open, Answered and Verified are not points, because neither plotted line moves on them. The series is plotted as two step lines with the signed gate dates marked, and the figure is included in package section 14.

**Alert zones** (SE HB §6.7.1.2.1 colour coding). A zone is computed for each review `R` at `T` using `R`'s own measures and `R`'s own closure_fraction_at_gate. The rules are applied in this order, and the first that matches decides:

| Order | Zone | Condition |
|---|---|---|
| 1 | Red | `R` is dispositioned and a Major RID or Blocking RFA of `R` is in state Open, Answered or Verified; or closure_fraction_at_gate is defined and below 0.8; or overdue > 3 |
| 2 | Green | overdue == 0 |
| 3 | Yellow | overdue is 1 to 3, every overdue item is a Minor RID or a Routine RFA, and closure_fraction_at_gate is 0.8 or more or is undefined (an undefined fraction is not evaluated) |
| 4 | Red | any other case (an overdue Major RID or Blocking RFA) |

Every case falls under exactly one row. The package zone is the worst zone over all reviews, and it is Green when no log exists. A Red package zone at the readiness declaration blocks the declaration until the owner records one of two things in the package: an accepted closure plan for each item that caused it, or a decision to re-review.

**Known-answer values** that the unit test targets. They are computed by hand from `docs/templates/rfa-rid-log.example.json` at `T` = 2026-10-12, with the SRR memo `signed: 2026-10-05` and no later memo:

| Review | Type | Severity | raised | open | verified_pending | closed | withdrawn | overdue |
|---|---|---|---|---|---|---|---|---|
| SRR | RID | all | 3 | 1 | 0 | 1 | 1 | 0 |
| SRR | RID | Major | 1 | 0 | 0 | 1 | 0 | 0 |
| SRR | RID | Minor | 2 | 1 | 0 | 0 | 1 | 0 |
| SRR | RFA | all | 2 | 1 | 0 | 1 | 0 | 0 |
| SRR | RFA | Blocking | 1 | 0 | 0 | 1 | 0 | 0 |
| SRR | RFA | Routine | 1 | 1 | 0 | 0 | 0 | 0 |

Derived values at the same `T`:

- age_open: median 9 days, max 9 days (RID-SRR-002 and RFA-SRR-002, opened 2026-10-03).
- age_closed: median 2 days (RID-SRR-001 and RFA-SRR-001).
- closure_fraction_at_gate: undefined, because no PDR memo is signed.
- overdue: 0, because both open items are due at PDR and no PDR memo is signed.
- Zone: Green (row 2).
- Burndown series: 2026-10-03 raised 5, closed plus withdrawn 1; 2026-10-05 raised 5, closed plus withdrawn 3.

The state changes of 2026-10-04 (two items Open to Answered) and 2026-10-09 (RID-SRR-002 Open to Answered) are not burndown points, because neither plotted count changes on those dates. `tools/review_trend.py` reproduced every value above on 2026-09-25, run with `--root tools/tests/fixtures/review_trend --date 2026-10-12`.

## 12. Dispositions and liens

### 12.1 Dispositions

| Disposition | Meaning | Effects |
|---|---|---|
| Approved | Every success criterion Met; zero RFAs or RIDs of this review still Open, Answered or Verified at signing | Baseline tag created; next phase starts |
| Approved with liens | Success criteria Met or Met with lien; every lien has owner, closure plan and due event or date | Baseline tag created; next phase starts; liens are the only permitted open work against the baseline other than approved CRs |
| Not approved | Any success criterion Not met without an acceptable lien, or any Major RID or Blocking RFA not Closed at the time of signing, or any Hard entrance criterion found unmet during the review | No tag. The memo front-matter keys `signed` and `disposition` stay `null`; the session and its outcome are recorded in memo section 2, and `tools/review_trend.py` does not treat the memo as a gate date (section 11). Re-review uses the same `docs/reviews/<REVIEW>/` folder with the `package.md` revision incremented and the deck re-rendered; the log continues. The memo is amended, never rewritten: `signed` and `disposition` are set once, by the session that approves |

For CDR, the memo additionally lists which liens are tagged `blocks-order`; the vendor orders are placed only when those are Closed.

### 12.2 Liens

SE HB App. B defines liens as requirements or tasks not satisfied that must be resolved within an assigned time to allow passage through a control gate.

**What may be a lien:** a Minor RID; a Routine RFA; a Soft entrance criterion not met; a TBR with owner, plan and `close_by`; a success criterion Met with lien where the shortfall does not touch safety, regulatory compliance, interfaces or traceability.

**What may never be a lien:** an open Major RID; an unmet Hard entrance criterion; a hazard without an allocated control requirement (PDR onward); a failing traceability report; a TBD in a product to be baselined; a safety-critical software component without recorded SWE-134 provisions (CDR onward); a regulatory `REQ-TX-*` without a Passed verification case (SAR; and before the on-air delta TRR); a cost above the owner's stated envelope at CDR.

**How a shortfall gets an id:** an unmet Soft entrance criterion accepted at the readiness confirmation, and a success criterion ruled *Met with lien* at the review, are each recorded as a Routine RFA raised by the owner (3.1 item 5); a TBR lien is identified by its `REQ-<MOD>-NNN` id. There is no lien without an id.

**One rule at signing:** every RFA or RID of this review still Open, Answered or Verified when the memo is signed carries `lien: true` and appears in the memo liens table; *Approved* means zero such items; *Approved with liens* means every such item has owner, plan and due event or date. Major RIDs and Blocking RFAs are Closed before signing (10.2), so they can never be in this set.

**Lien record:** each lien is an RFA, RID or TBR id listed in the decision memo liens table with `owner`, `plan`, `due` (event or ISO date), and for CDR the `blocks-order` flag. The log item carries `lien: true`.

**Closing a lien:** follows section 10.3. If closure changes a baselined item, a `CR-NNN` is raised and referenced as evidence (`kind: cr`), unless the change is editorial per 05 section 2 (10.1). The example log shows the pattern: RID-SRR-002 changes the baselined ConOps after `baseline/srr` and cites `CR-001`.

**Missed lien date:** Claude reports the miss to the owner in the next working session, citing the lien id. The owner chooses one of the options below. The choice is appended to memo section 13 and recorded in the item's `history` as a same-state entry (10.3):

- **Extend.** Allowed only for a Routine RFA, and for a TBR within the closure limits of charter section 7 (L1 by PDR, L2 by CDR). The new due is recorded with its rationale.
- **Convert.** The lien becomes a `CR-NNN` or an `RSK-NNN`. The item passes through Answered (the response names the new id; evidence `kind: cr` or `kind: risk`) and Verified, then is Closed with disposition Transferred. No state is skipped (10.3).
- **Re-severitize.** The owner changes the item's severity with rationale (10.2), for example a Minor RID raised to Major. The item then follows the deadline of its new severity.
- **Revoke.** The disposition reverts to *Not approved* and the re-review is scheduled. The memo front matter gets `revoked: <YYYY-MM-DD>`. The keys `signed`, `disposition` and `baseline_tag` keep the original approval, because tags are never moved (05 section 4.4). The re-review's approval is recorded as a memo section 13 amendment with the owner's wording.

A Minor RID that misses its gate may only be converted or re-severitized, never extended, because its deadline is fixed by 10.2.

## 13. Records

| Record | Path | Written by | When |
|---|---|---|---|
| Review package | `docs/reviews/<REVIEW>/package.md` | Claude | Before readiness declaration; revised for re-review |
| Peer review record (one per product; the filled checklist) | `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (charter sections 5 and 6; no `peer-reviews/` folder). The file is a copy of the `docs/templates/peer-review-checklist-*.md` template, with every item answered Yes, No or N/A and its evidence. The slug is `<type>-<product-stem>`, lower case: `requirements-<module>`, `plan-<document-stem>`, `design-<document-stem>`, `code-<module>`, `test-<module>`, `cr-NNN`, `classification-03-software-classification-and-rmm` (the independent classification assessment, 03 section 3.3, checklist `peer-review-checklist-classification`), `risk-register` and `ts-nnn-<slug>` (06 section 16, checklist `peer-review-checklist-risk`). Front matter: this row is the single field list, copied from `PEER_REVIEW_RECORD_SCHEMA` in `tools/validate_docs.py`; 08 section 3.2 and SEMP section 5.16 point here. Required: `id` (`INSP-NNN`, unique across all reviews), `checklist` (`peer-review-checklist-<type>` or a hyphenated stem such as `peer-review-checklist-visual-product`, naming an existing file in `docs/templates/`), `product` (path or `CR-NNN`), `product_commit` (7 to 40 hex digits, quoted), `verdict` (`APPROVED` or `NEEDS CHANGES`), `author_agent`, `reviewer_agent` (never the author), `iteration` (1 to 3), `date` (ISO), `readiness_met` (boolean), and the SWE-089 integers `findings_major`, `findings_minor`, `findings_fixed`, `findings_deferred`, `effort_turns`, `effort_minutes`. Required for the products of 07 sections 2.1.1 and 14.1: `assurance_reviewer_agent`, distinct from author and reviewer. Optional: `checklist_revision`; `checklist_file`, which when present equals the record's own path. The templates carry further fields for the software lead (`reviewer_verdict`, `assurance_verdict`, finding states, `deferred_rids`, `record_status`), which the validator does not check. The body lists each finding with an anchor `#finding-<n>`, its severity, its state (Open, Fixed, Verified or Deferred) and, after the review, the owner's adoption ruling (10.1). Findings are cited as `checklists/<slug>.md#finding-<n>` | Reviewer agents | Before readiness declaration |
| Per-unit as-built record and acceptance data package index | `docs/vv/adp/CWHT-A-NNN/as-built.md` | Claude | Before SAR |
| Decision memo between gates | `docs/cm/cr/CR-NNN-<slug>.md` disposition block; `docs/decisions/adr/ADR-NNN-*.md` decision section | Claude, owner wording transcribed | At CR disposition; at ADR acceptance |
| Traceability report | `docs/reviews/<REVIEW>/traceability-report.md` | `tools/traceability.py` | At package build |
| Figures | `docs/reviews/<REVIEW>/figures/` | Claude | At package build |
| Review deck source | `docs/reviews/<REVIEW>/slides/<review>.adoc` (controlled review product, charter section 4 item 2) | Claude | After the package is complete, before the readiness declaration (3.1 item 4); revised for re-review |
| Review deck HTML | `docs/reviews/<REVIEW>/slides/<review>.html` (generated by `tools/slides/render_deck.py`; committed) | `render_deck.py` | Same |
| Slide renders | `docs/reviews/<REVIEW>/slides/png/slide-NN.png` (generated, committed; the record of what was presented; each inspected, charter section 11 rule 3) | `render_deck.py`; inspected by Claude | Same |
| reveal.js runtime copy | `docs/reviews/<REVIEW>/slides/reveal.js/` (git-ignored, regenerated by `render_deck.py`; not a record) | `render_deck.py` | Same |
| RFA/RID log | `docs/reviews/<REVIEW>/rfa-rid-log.json` | Claude (owner dictates) | From first item to last closure |
| Minutes | `docs/reviews/<REVIEW>/minutes.md`, in slide order with the slide number against every question, RFA and RID (3.4) | Claude | Same session as the review |
| Decision memo | `docs/reviews/<REVIEW>/decision-memo.md` | Claude, signed by owner transcription | At disposition and at every lien change |
| Baseline record | `docs/reviews/<REVIEW>/baseline-record.md` (template `docs/templates/baseline-record.md`; Record class, 05 Table 4-1 row 32); its section 1 records the memo commit hash, and the pushed tag hash is a fill-once field (section 2) | Claude; checked at R by the independent reviewer | Committed as commit R immediately before the tag with trailer `Refs: <REVIEW>` (SRR, PDR, CDR, SAR); the fill-once fields (`commit`, `tag_object`, `signed`, `signature_verified`, `pushed_hash`), section 8a and section 9 written once by the post-tag record commit with trailer `Refs: <REVIEW>` (05 section 4.4 steps 3 and 6) |
| Test configuration record | `docs/reviews/TRR/test-configuration-record.md` (and `TRR-Dn/`) | Claude | Before the TRR readiness declaration |
| Configuration audit | `docs/reviews/SAR/configuration-audit.md` | Claude, verified by reviewer agent | Before SAR |
| Baseline tag | `baseline/<review>`, annotated, message `cwht <name> baseline; decision memo docs/reviews/<REVIEW>/decision-memo.md at <memo commit>`, verified and pushed to `origin` (05 section 4.4 step 5) | Claude | On the baseline-record commit R, after the memo commit |

All records are Markdown or JSON in the repository; no record lives only in conversation.

## 14. Compliance hooks

| NPR 7123.1D requirement | Where satisfied |
|---|---|
| SE-32 review plans | This document |
| SE-33 participation in reviews | Section 1 roles; every gate |
| SE-34 entrance and success criteria | Sections 3 to 8 |
| SE-35 to SE-37 | Section 4.5 |
| SE-38, SE-39, SE-66 | Section 4.5 |
| SE-40 to SE-43 | Section 5.5 (SE-44 NA per `se-compliance-matrix.json`) |
| SE-45, SE-67, SE-68 | Section 5.5 |
| SE-46 | Section 6.5 |
| SE-47, SE-48 | Section 7.5 |
| SE-53, SE-54, SE-69 | Section 8.5 (customization: FRR and ORR products delivered at SAR, FC in the compliance matrix) |
| SE-51, SE-52 | Sections 1 item 3, 3.5 and 8.5: T (scope relief) in `se-compliance-matrix.json`; delivered at SAR as the operations-handbook end-of-life section |
| SE-55, SE-56 | Sections 1 item 3, 3.5 and 8.5: T in `se-compliance-matrix.json`, relief type deviation (DR and DRR not held; approved by the owner as ETA, SE-06, in the SRR memo) |
| SE-57 periodic technical reviews | Section 2.1 (sprint-closure technical reviews, milestone status, Table G-19 peer reviews, SWE-143 architecture review, Phase E periodic status) |
| SE-60, SE-61, SE-62, SE-63, SE-64 (NPR 7123.1D §6.2.6 to §6.2.9) | Section 11 and `docs/plan/tpm.json` (SE-62 mass margin: FC, `TPM-001` key `mass-margin`; SE-63 power margin: `TPM-002`; SE-64 review trend: `TPM-003`) |
| §5.2.1.2 review plan updated with each review's results | Section 9, additional completion items |
| §5.2.1.3 HSI documentation location | Section 4.3 row 9 |
| §5.2.2.6 spectrum-manager success criteria | Section 3.5, first row (Customized (NA), Part 97 substitute) |
| §5.2.3.1 completion | Section 9 |

The compliance matrix rows for these identifiers cite this document by section.

## 15. Cross-document actions raised by this document

This document may not edit other process documents (charter section 11 rule 5). Each difference below is therefore an action on another author. Each closes before the SRR readiness declaration, and the SRR package lists it in section 18 (compliance summary) with its closing commit (a file cannot carry the hash of the commit that adds it, so the package records it). An action still open at that point is a Soft-criterion lien under 3.1 item 5. Status verified by the integrating session on 2026-09-25 by reading each target file and running `tools/render_compliance.py --check`, `tools/render_rmm.py --check`, `tools/validate_docs.py` and the unit-test suite; every target file is still untracked at commit b8214ca, so each Resolved item is confirmed by the commit that brings its file under version control.

| # | Owner of the action | Document and location | Change | Reason | Status |
|---|---|---|---|---|---|
| 1 | Compliance-matrix author | `docs/process/se-compliance-matrix.json` rows SE-51, SE-52, SE-55, SE-56 | SE-55 and SE-56: T (review not held). SE-51 and SE-52: the ORR is combined with SAR and the relief is the plan content omitted relative to App. G Tables G-17 and G-18 (3.5) | NA is circular when the review is simply not held; SE-51 and SE-52 are ORR products and the ORR is held with SAR | Resolved: the matrix records all four rows T with relief type deviation and `render_compliance.py --check` exits 0 |
| 2 | Owner (charter) | `docs/process/00-charter.md` section 3 row "E / F", the combined-review sentence, and section 12 row on App. G guidance items | Section 3 E / F row: "DR and DRR not held; SE-55, SE-56 tailored by deviation (compliance matrix)". Combined-review sentence: "SAR carries the ORR and FRR products SE-69, SE-51, SE-52, SE-53, SE-54". Section 12: the SE-51 and SE-52 basis "no decommissioning review" becomes "ORR combined with SAR; scope relief of the operations-handbook end-of-life section relative to App. G Tables G-17 and G-18". Change vehicle: an owner-approved commit before `baseline/srr` (05 section 4.2, pre-gate Log control), a `CR-NNN` after it | Charter section 12 cites the review that owns SE-55 as the basis for SE-51 and SE-52, and charter section 3 omits SE-51 and SE-52 from the products SAR carries | Open: owner decision, carried as a charter issue in the SRR package proposed-tailoring section |
| 3 | RMM author | `docs/process/rmm.json` SWE-143 `implementation` and `residual_risk` | "findings the owner adopts become RIDs (01 section 10.1)"; residual risk cites the independent PDR architecture review | 10.1 adoption rule | Resolved: the row reads so; `render_rmm.py --check` exits 0 |
| 4 | V&V author (04) and tools owner | 04 sections 5.2 and 5.3; the planned `tools/traceability.py` check | Verified on the credited report against the tagged release; PCA-05 and the signed SAR memo are conditions of Closed; the planned check is named `CLOSED_NOT_INSTALLED` everywhere | Charter section 9 as amended in b8214ca | Resolved: 04 sections 5.2 and 5.3 follow charter section 9, and 02, 04, 05 and `tools/README.md` use `CLOSED_NOT_INSTALLED` (implementation due CDR, 04 section 7.4) |
| 5 | CM author (05), software plan author (07), checklist template author, baseline-record template author | 05 section 4.1; 07 sections 1.2, 1.4, 3.4, 10.2 and 22; the four `docs/templates/peer-review-checklist-*.md`; `docs/templates/baseline-record.md` section 2 | One record per product: `docs/reviews/<REVIEW>/checklists/<product-slug>.md` with `id: INSP-NNN`; no `peer-reviews/` folder; `checklist_file` optional and, when present, the record's own path | Charter section 5 as amended in b8214ca; `tools/validate_docs.py` rejects a `peer-reviews/` folder | Resolved: every named location uses the single record; section 13 is the single front-matter field list |
| 6 | CM author (05) | 05 section 3 software assurance row, section 7.4 last sentence, section 4.4 step 5 tag message | "findings the owner adopts become RIDs (01 section 10.1)"; tag message ends "at <memo commit>" | 10.1 adoption rule; the tag message cites the memo commit | Resolved: 05 reads so, and section 2 of this document points to 05 section 4.4 as the single baseline procedure |
| 7 | Tools owner | `tools/tests/fixtures/review_trend/docs/reviews/SRR/rfa-rid-log.json` | Re-copy the fixture log and schema from the revised templates | Keep the fixture a copy of the example | Resolved: the fixture equals `docs/templates/rfa-rid-log.example.json` and `test_fixture_log_is_the_template` passes |
