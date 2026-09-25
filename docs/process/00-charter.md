# cwht Engineering Process Charter

**Status:** Baseline draft for SRR. **Owner:** Robin (Project Manager, Decision Authority, Technical Authority, customer, review chair). **Author:** Claude (lead systems engineer, software lead, design engineering, review presenter).

This charter is the single source of truth for *how* the cwht project is engineered. Every other process document in `docs/process/` expands a section of this charter and must not contradict it. Where a detail is not covered here, the governing documents below apply as written.

## 1. Governing documents and applicability

| Document | Role on cwht | Corpus location |
|---|---|---|
| NASA/SP-2016-6105 Rev 2, *NASA Systems Engineering Handbook* (SE HB) | Practices for the 17 common technical processes, requirements writing (App. C), V&V matrices (App. D/E/I), SEMP (App. J), ConOps (App. S), CM (App. M) | `docs/references/md/nasa-se-handbook/` |
| NPR 7123.1D, *NASA Systems Engineering Processes and Requirements* | The SE requirements (SE-NN), life-cycle review entrance/success criteria (App. G), compliance matrix (App. H) | `docs/references/md/npr-7123-1d/` |
| NPR 7150.2D, *NASA Software Engineering Requirements* | Software requirements (SWE-NNN), classification (App. D), Requirements Mapping Matrix (App. C) | `docs/references/md/npr-7150-2d/` |
| NASA-HDBK-2203 (SWEHB Ver D) | Guidance, rationale and small-project tailoring per SWE | `docs/references/md/swehb/` (scrape in progress) |
| 47 CFR Part 97 | Regulatory constraints on the transmitter (emission limits §97.307, permitted emissions §97.305) | to be added under `docs/references/md/regulatory/` |

**Owner direction (2026-09-25):** apply the rigor of **Class A software** (NPR 7150.2D App. D) and a **Criticality-1** system for requirements, bidirectional traceability, verification and validation, configuration management and reviews. Honest classification note: by the letter of App. D a hobby transceiver would fall in Class D/E; the owner *elects* Class A applicability. This election is recorded in `docs/process/03-software-classification-and-rmm.md` and cannot be silently relaxed.

**Tailoring vs customization.** Per NPR 7150.2D §2.2 and NPR 7123.1D §3.11: *tailoring* (relief from a requirement) is recorded row-by-row in the Requirements Mapping Matrix (RMM) and the NPR 7123.1 compliance matrix with rationale and owner approval; *customization* (combining reviews, consolidating documents, adjusting formality) needs no waiver and is recorded in the SEMP. Requirements that presuppose NASA institutions (Centers, contracts, CMMI appraisals, IV&V, spectrum managers) are marked Not Applicable with the institutional reason, and the *intent* is preserved where a project-scale equivalent exists.

## 2. Roles and independence

- **Owner (Robin):** project manager and Decision Authority; Engineering Technical Authority and SMA Technical Authority; customer and end user; chair of every life-cycle review. Approvals are recorded as decision memos in the repo; an approval in chat is transcribed into the memo.
- **Claude (main session):** lead systems engineer; prepares all products, runs analyses, presents reviews, maintains baselines.
- **Independent agents:** author, reviewer and test-author roles are always *separate invocations* (mirrors `rustos/docs/sdp/methodology.md` and IEEE 1012 independence). A product is not "reviewed" until an agent other than its author has reviewed it against a checklist and the result is recorded.
- **Software assurance function:** performed by independent reviewer agents using the SWEHB software-assurance tabs and checklists; findings are reported to the owner at each review.

## 3. Customized life cycle and review gates

The project runs the NPR 7120.5 project life cycle in condensed form. Reviews are **event-based**: they are held when entrance criteria are met, not on calendar dates (NPR 7123.1D §5.1.5).

| Phase | Work | Gate | Baseline set at gate |
|---|---|---|---|
| Pre-A / A — Formulation | Stakeholder expectations (NGOs, MOEs), ConOps, L1 system requirements, SEMP, CM plan, risk plan, V&V approach, software classification + RMM, preliminary hazard analysis, technology/heritage assessment, toolchain proof | **SRR** (absorbs MCR: MCR products are SRR entrance products) | Functional baseline: NGOs, MOEs, ConOps, L1 requirements, SEMP |
| B — Preliminary design | Architecture and trade studies, requirement allocation to subsystems (L2 specs), ICDs, MOPs/TPMs, preliminary design with simulation evidence, V&V plan, integration plan, updated risks/hazards | **PDR** (absorbs SDR/MDR: architecture, allocation and TPM definitions are PDR entrance products) | Allocated baseline: L2 specs, ICDs, architecture, V&V plan |
| C — Final design | Detailed schematic and PCB, enclosure CAD, firmware design, full analysis package, build-to specifications, BOM, fabrication/assembly package, test procedures, acceptance criteria | **CDR** = procurement release: approval authorizes the PCBWay (fab + assembly + CNC) and DigiKey orders | Product baseline: design data package, BOM, procedures |
| D — Realization | Vendor fabrication; firmware implementation, host tests, emulation; receipt inspection; test readiness; V&V execution; operations handbook | **TRR** before any powered bench test; **SAR** (absorbs ORR) for acceptance and hand-over | As-built baseline: as-built records, V&V report, version description |
| E / F — Operations, closeout | On-air use by owner and friends, anomaly reports, lessons learned, rev B formulation | Periodic status; DR/DRR not applicable beyond archiving | — |

Entrance and success criteria for SRR, PDR, CDR, TRR and SAR are tailored from NPR 7123.1D App. G Tables G-4, G-6, G-7, G-10 and G-11, with the minimum products of NPR 7123.1D §5.2.2.2 (SE-38/39/66, SE-45/67/68, SE-46, SE-48, SE-53/54) mapped to project artifacts. The tailored criteria live in `docs/process/01-lifecycle-and-reviews.md`.

## 4. Review conduct, RFAs and RIDs

1. **Package.** Before a review, Claude assembles `docs/reviews/<REVIEW>/package.md`: agenda, entrance-criteria checklist with evidence links, product summaries, rendered figures (schematics, layouts, CAD renders, plots), TPM status, risk status, open TBD/TBR list, RFA/RID burndown from prior reviews, proposed tailoring. Every claim links to an artifact in the repo.
2. **Presentation.** Claude presents the package in conversation, section by section, and answers questions.
3. **Disposition.** The owner records one of: *Approved*, *Approved with liens* (open items with closure plan and dates), or *Not approved* (re-review required). The owner may raise:
   - **RFA** (Request for Action): a question, analysis or plan the owner wants performed; ID `RFA-<REVIEW>-NNN`.
   - **RID** (Review Item Discrepancy): a specific defect in a reviewed product; ID `RID-<REVIEW>-NNN`; carries severity (Major = blocks baseline; Minor = fix before next review).
   Both are logged in `docs/reviews/<REVIEW>/rfa-rid-log.json` with originator, product, description, assignee, due, disposition, closure evidence.
4. **Completion** (NPR 7123.1D §5.2.3.1): all RIDs/RFAs dispositioned or on an agreed closure plan; review minutes and decision memo written (`docs/reviews/<REVIEW>/decision-memo.md`); baseline tagged in git (`baseline/srr`, `baseline/pdr`, …).
5. **Trend.** RFA/RID open/closed counts per review are a required TPM (NPR 7123.1D SE-64) and are plotted in each subsequent package.

## 5. Document tree and repository map

| Product (NASA name) | cwht artifact |
|---|---|
| Systems Engineering Management Plan | `docs/plan/semp.md` (this charter is its core; App. J outline) |
| Stakeholder expectations: Needs, Goals, Objectives; MOEs; success criteria | `docs/requirements/l0-stakeholder/expectations.json` + rendered `.md` |
| Concept of Operations (App. S) | `docs/conops/conops.md` with scenarios `OPS-NNN` (nominal and off-nominal) |
| System Requirements Document (L1) | `docs/requirements/sys/requirements.json` |
| Subsystem specifications (L2) | `docs/requirements/{rx,tx,pwr,ctl,me,sw}/requirements.json` |
| Software Requirements Specification | `docs/requirements/sw/` (module-level files, e.g. `sw-keyer`) |
| Interface Requirements / Control Documents (App. L) | `docs/icd/ICD-<A>-<B>.md` (pin maps, connectors, register maps, mechanical envelopes) |
| Architecture, logical decomposition, allocation | `docs/design/architecture.md`, `docs/design/allocation.json` |
| Trade studies and decision reports (SE HB §6.8, Table 6.8-1) | `docs/decisions/trade-studies/TS-NNN-*.md` |
| Architecture Decision Records | `docs/decisions/adr/ADR-NNN-*.md` |
| Risk register (5×5) | `docs/risk/register.json` + rendered matrix |
| Hazard analysis, safety-critical determination | `docs/safety/hazard-analysis.md`, `docs/safety/hazards.json` |
| Software classification record + Requirements Mapping Matrix | `docs/process/03-software-classification-and-rmm.md`, `docs/process/rmm.json` |
| NPR 7123.1 compliance matrix (App. H) | `docs/process/se-compliance-matrix.json` |
| V&V Plan (App. I), verification matrix (App. D), validation matrix (App. E) | `docs/vv/plan.md`; matrices generated by `tools/traceability.py` from requirements + test cases |
| Test cases / procedures / reports | `docs/test_cases/<module>/test_cases.json`; reports in `docs/vv/reports/` |
| Configuration Management Plan (App. M) | `docs/process/05-configuration-and-data-management.md` |
| Software Development / Management Plan (NPR 7150.2D Ch. 6) | `docs/process/07-software-engineering-plan.md` |
| Review packages, RFA/RID logs, decision memos | `docs/reviews/<REVIEW>/` |
| TPMs and leading indicators | `docs/plan/tpm.json` + plots |
| Version description documents | `firmware/releases/VDD-<version>.md` |
| Nonconformance reports | `docs/vv/ncr/NCR-NNN.md` |
| Lessons learned | `docs/lessons-learned.md` |
| Research reports grounding decisions | `docs/research/` |

## 6. Identifier schemes

`NGO-NNN` need/goal/objective · `MOE-NNN` · `MOP-NNN` · `TPM-NNN` · `OPS-NNN` ConOps scenario · `REQ-<MOD>-NNN` requirement (modules: SYS, RX, TX, PWR, CTL, ME, SW-<sub>) · `TC-<MOD>-NNN` test/verification case · `ICD-<A>-<B>` interface · `ADR-NNN` decision record · `TS-NNN` trade study · `RSK-NNN` risk · `HZ-NNN` hazard · `NCR-NNN` nonconformance · `CR-NNN` change request · `RFA-<REV>-NNN` / `RID-<REV>-NNN`. IDs are never reused; retired items keep their ID with status *Retired* and a rationale.

## 7. Requirements and bidirectional traceability

- **Levels.** L0 stakeholder expectations (NGOs, MOEs) → L1 system requirements (SYS) → L2 subsystem requirements (RX, TX, PWR, CTL, ME, SW) → design elements (architecture blocks, schematic sheets, Rust modules) → code → verification cases. Hazards trace to requirements (controls) and to verification.
- **Writing rules** (SE HB App. C): one "shall" per statement, active voice, quantified with units and tolerances, implementation-free, no unverifiable words (e.g. *adequate, robust, minimize*), rationale mandatory, verification method assigned at definition time. Schema: `docs/requirements/schema.json`.
- **Validation of requirements** before SRR follows the six steps of SE HB §4.2.1.2.4 (format, stakeholder satisfaction, technical correctness, feasibility, verifiability, non-redundancy); each L1 requirement is checked by an independent reviewer agent.
- **Traceability set** (NPR 7150.2D §3.12.1 Table 1, Class A): higher-level → software requirements; software requirements → hazards; software requirements → design components; design components → code; requirements → verification; requirements → nonconformances. `tools/traceability.py` enforces: unique IDs, every requirement has a parent or a documented self-derived rationale, every requirement has ≥1 verification case, every verification case cites ≥1 requirement, statuses are consistent. Its report is an entrance product of every review.
- **TBD/TBR.** No TBDs in a baselined document. TBRs are permitted with owner, closure plan and target review; all L1 TBRs close by PDR, all L2 TBRs by CDR.
- **Change control.** After SRR the requirements are under configuration control; changes go through a Change Request (`CR-NNN`) with impact assessment (cost, schedule, performance margins, safety, interfaces, verification) and owner approval acting as the Configuration Control Board. Requirements volatility is tracked (SWE-200).

## 8. Baselines and configuration management

- Configuration items: everything in §5 plus schematics, PCB, enclosure CAD, BOM, firmware source, simulation decks and checkers, tool versions (`tools/toolchain.lock.md`), scripts.
- Baselines: functional (SRR), allocated (PDR), product (CDR), as-built (SAR); each is a signed git tag plus a baseline record listing CI versions.
- Changes after a baseline require a `CR-NNN`; minor editorial changes are logged, not boarded.
- Configuration audits: a functional and a physical configuration audit are performed at SAR (as-built matches product baseline; firmware hash matches version description).
- Tool validation and accreditation (SWE-136): every analysis or build tool is listed with version and a documented sanity check (e.g. LTspice batch reproduces a known filter response; kicad-cli DRC reproduces a seeded violation).

## 9. Verification and validation philosophy

- Every requirement is verified by **Test, Analysis, Inspection or Demonstration**, chosen when the requirement is written. Pre-power-on evidence classes: *Analysis* (LTspice, budgets, S-parameter models, Python checks), *HostUnit* (cargo test of application logic running on a host implementation of the rustos `api` traits with injected device models; the primary software evidence per SI-026), *Emulation* (optional, secondary: whole-binary scenarios on an RP2350 emulator for event ordering only, never timing), *Inspection* (ERC/DRC, schema and traceability checks, rendered-image review, and driver-to-datasheet traceability: every register access in a rustos driver cites the RP2350 datasheet or Cortex-M33 documentation section it implements). Post-build classes: *Bench* (owner's NanoVNA, tinySA Ultra with attenuator, dummy load, bench supply, multimeter, Pico-based logic capture) and *OnAir* demonstration. Hardware integration is verified on real hardware.
- "Run for the record" verification is performed on the delivered unit; pre-build analyses reduce risk but do not by themselves close a requirement unless the method is Analysis.
- Validation is against the ConOps scenarios and MOEs, with the owner as the user (SE HB §5.4).
- The V&V plan is baselined at PDR (SE-68) and updated at CDR; a TRR precedes bench testing; a nonconformance report is opened for any discrepancy (severity levels per SWE-202).

## 10. Software engineering commitments (NPR 7150.2D, Class A)

Detailed in `docs/process/07-software-engineering-plan.md`. Non-negotiables: recorded architecture and design (SWE-057/058); Rust coding standard with static analysis (clippy, unsafe audit, complexity) (SWE-061/135); unit tests that are repeatable with measured coverage (SWE-062/186/189/190); regression testing (SWE-191); safety-critical design provisions of SWE-134 a–l applied to keying, PA enable, charging and thermal control; MC/DC coverage target of 100 % for safety-critical components (SWE-219) with cyclomatic complexity ≤ 15 (SWE-220); independent peer review with checklists of requirements, plans, design, code and test procedures (SWE-087/088/089); version description for every release (SWE-063); nonconformance tracking (SWE-201–204); bidirectional traceability (SWE-052).

## 11. Working rules for Claude and every agent

1. **Search before reading.** Use the Claude Context vector index over the repo and `docs/references/md/` to retrieve exact guidance; cite it as `SE HB §x.y`, `NPR 7123.1D App. G Table G-6`, `SWE-134`, `SE-39`.
2. **Evidence, not assertion.** A review claim without a linked artifact is not a claim.
3. **Visual closure.** Every visual product (schematic, layout, CAD, plot) is rendered to an image and inspected before it is called done; the render is attached to the review package.
4. **Independence.** Author, reviewer and test author are different agent invocations; reviewers use the checklist for the product type.
5. **No silent scope changes.** Requirements, interfaces and baselines change only through the CR process; tailoring only through the RMM/compliance matrix.
6. **Record decisions.** Any choice that constrains later work becomes an ADR or a trade study the same day.
7. **Token economy.** Agents receive briefs that point to files and searches, not pasted documents; they return structured results.
8. **Headless only.** No agent uses screen capture, AppleScript/System Events, or any GUI automation, and none requests macOS privacy permissions. Every tool runs from the command line (LTspice batch, kicad-cli, OpenSCAD CLI, cargo). If a headless path does not exist, the agent stops and reports it as an open item for the owner instead of driving the desktop.

## 12. Tailoring register (summary; full detail in the RMM and compliance matrix)

| Area | Disposition | Rationale |
|---|---|---|
| Assembly model (SI-031) | Customized | PCBWay assembles surface-mount parts; the owner hand-solders through-hole parts and modules with exposed pads (Pico 2 castellations, 18650 holders, jacks, encoder, RF module if one is chosen). The product baseline states which parts are in each category. |
| Contracted-effort requirements (NPR 7123.1D SE-24 … SE-31) | Not applicable | No contracts; vendors (PCBWay, DigiKey) supply catalog services under standard terms. Vendor deliverables are received and inspected under the Product Implementation process. |
| CMMI rating (SWE-032), IV&V (SWE-141, 131, 178, 179), Center repositories and reporting (SWE-006, 091, 092, 094, 142, 144, 174) | Not applicable | Presuppose NASA institutions. Intent preserved by independent agent review and a repo-local measurements file. |
| Software cost estimation (SWE-015, 151) | Tailored | Replaced by a labor-free cost model: BOM, fabrication, assembly, enclosure and shipping estimates with contingency, updated at each review. |
| Schedules (SWE-016, 018, 046) | Tailored | Milestone list keyed to review gates and vendor lead times; no calendar commitments beyond those. |
| Spectrum manager concurrence (NPR 7123.1D App. G, NPD 2570.5) | Not applicable | Owner is the FCC licensee; replaced by explicit Part 97 compliance requirements and verification. |
| Human Systems Integration (SE-65/66) | Customized | HSI approach is a section of the SEMP covering controls, display, audio, key/paddle ergonomics and RF-exposure safety. |
| Cybersecurity (SWE-154, 156, 157, 159, 185, 207, 210) | Tailored | The radio has no network interface; the assessment covers USB firmware loading and command injection via the key input; secure-coding practices retained. |
| Reuse cataloging and Government rights (SWE-147, 148, 214–217) | Not applicable | Open personal project; license recorded in the repo. |
