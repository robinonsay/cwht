# cwht Engineering Process Charter

**Status:** Baseline draft for SRR. **Owner:** Robin (Project Manager, Decision Authority, Technical Authority, customer, review chair). **Author:** Claude (lead systems engineer, software lead, design engineering, review presenter).

This charter is the single source of truth for *how* the cwht project is engineered. Every other process document in `docs/process/` expands a section of this charter and must not contradict it. Where a detail is not covered here, the governing documents below apply as written.

## 1. Governing documents and applicability

| Document | Role on cwht | Corpus location |
|---|---|---|
| NASA/SP-2016-6105 Rev 2, *NASA Systems Engineering Handbook* (SE HB) | Practices for the 17 common technical processes, requirements writing (App. C), V&V matrices (App. D/E/I), SEMP (App. J), ConOps (App. S), CM (App. M) | `docs/references/md/nasa-se-handbook/` |
| NPR 7123.1D, *NASA Systems Engineering Processes and Requirements* | The SE requirements (SE-NN), life-cycle review entrance/success criteria (App. G), compliance matrix (App. H) | `docs/references/md/npr-7123-1d/` |
| NPR 7150.2D, *NASA Software Engineering Requirements* | Software requirements (SWE-NNN), classification (App. D), Requirements Mapping Matrix (App. C) | `docs/references/md/npr-7150-2d/` |
| NASA-HDBK-2203 (SWEHB Ver D) | Guidance, rationale, small-project tailoring and software-assurance tabs per SWE | `docs/references/md/swehb/` (268 pages, complete) |
| 47 CFR Parts 1, 2, 15 and 97 | Regulatory constraints: emission limits §97.307, permitted emissions §97.305, operator rules §97.7/103/105/115, RF exposure §1.1307/1.1310/2.1093, necessary bandwidth §2.202, allocations §2.106 | `docs/references/md/regulatory/` (verbatim, eCFR issue 2026-09-23) |
| NPR 8000.4, NASA/SP-2011-3422, NASA-STD-8739.8, NASA-STD-8739.9 | Not adopted; not in the corpus. Risk scales are project-defined in `docs/process/06-risk-and-decision-analysis.md`; safety-critical determination uses the criteria NPR 7150.2D itself states. The owner may obtain NASA-STD-8739.8 and direct a CR to map it. | none |

**Owner direction (2026-09-25):** apply the rigor of **Class A software** (NPR 7150.2D App. D) and a **Criticality-1** system for requirements, bidirectional traceability, verification and validation, configuration management and reviews. Honest classification note: by the letter of App. D a hobby transceiver would fall in Class D/E; the owner *elects* Class A applicability. This election is recorded in `docs/process/03-software-classification-and-rmm.md` and cannot be silently relaxed.

**Tailoring vs customization.** Per NPR 7150.2D §2.2, NPR 7123.1D §2.2 (2.2.1 tailoring, 2.2.2 customizing) and SE HB §3.11: *tailoring* (relief from a requirement) is recorded row-by-row in the Requirements Mapping Matrix (RMM) and the NPR 7123.1 compliance matrix with rationale and owner approval; *customization* (combining reviews, consolidating documents, adjusting formality) needs no waiver and is recorded in the SEMP. Requirements that presuppose NASA institutions (Centers, contracts, CMMI appraisals, IV&V, spectrum managers) are marked Not Applicable with the institutional reason, and the *intent* is preserved where a project-scale equivalent exists.

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

Entrance and success criteria for SRR, PDR, CDR, TRR and SAR are tailored from NPR 7123.1D App. G Tables G-4, G-6, G-7, G-10 and G-11, with the minimum products of NPR 7123.1D §5.2.2.2 mapped to project artifacts as customization of combined reviews: SRR carries SE-38/39/66 plus the MCR products SE-35/36/37; PDR carries SE-45/67/68 plus the SDR products SE-40/41/42/43; CDR carries SE-46; TRR carries the SIR products SE-47/48; SAR carries the ORR and FRR products SE-69, SE-53/54. SE-44, SE-51 and SE-52 are dispositioned in the compliance matrix. A **delta TRR** (`TRR-Dn`) precedes every new run-for-record series, including the first on-air series, which requires all Part 97 emission cases passed. Runs on a bare Pico 2 development board before hardware arrives are recorded as Bench evidence with `credit: false`; TRR gates the delivered unit. The tailored criteria live in `docs/process/01-lifecycle-and-reviews.md`.

## 4. Review conduct, RFAs and RIDs

1. **Package.** Before a review, Claude assembles `docs/reviews/<REVIEW>/package.md`: agenda, entrance-criteria checklist with evidence links, product summaries, rendered figures (schematics, layouts, CAD renders, plots), TPM status, risk status, open TBD/TBR list, RFA/RID burndown from prior reviews, proposed tailoring. Every claim links to an artifact in the repo.
2. **Presentation.** Claude presents the package in conversation, section by section, and answers questions.
3. **Disposition.** The owner records one of: *Approved*, *Approved with liens* (open items with closure plan and dates), or *Not approved* (re-review required). The owner may raise:
   - **RFA** (Request for Action): a question, analysis or plan the owner wants performed; ID `RFA-<REVIEW>-NNN`; severity Blocking (closed before the decision memo is signed) or Routine.
   - **RID** (Review Item Discrepancy): a specific defect in a reviewed product; ID `RID-<REVIEW>-NNN`; carries severity (Major = blocks baseline; Minor = fix before next review).
   Both are logged in `docs/reviews/<REVIEW>/rfa-rid-log.json` with originator, product, description, assignee, due, disposition, closure evidence.
4. **Completion** (NPR 7123.1D §5.2.3.1): all RIDs/RFAs dispositioned or on an agreed closure plan; review minutes and decision memo written (`docs/reviews/<REVIEW>/decision-memo.md`); baseline tagged in git (`baseline/srr`, `baseline/pdr`, …). Delta reviews use the token `TRR-Dn` (folder `docs/reviews/TRR-Dn/`, no baseline tag). Between reviews, an approved Change Request's disposition block and an ADR's decision section are the decision memos for that change or decision; chat approvals are transcribed into them.
5. **Trend.** RFA/RID open/closed counts per review are a required TPM (NPR 7123.1D SE-64), registered in `docs/plan/tpm.json` as the review-trend TPM, computed by `tools/review_trend.py`, and plotted in each subsequent package under `docs/reviews/<REVIEW>/figures/`.

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
| Process documents (this set) | `docs/process/00-charter.md`, `01-lifecycle-and-reviews.md`, `02-requirements-and-traceability.md`, `03-software-classification-and-rmm.md`, `04-verification-and-validation.md`, `05-configuration-and-data-management.md`, `06-risk-and-decision-analysis.md` (also the Risk Management Plan and Decision Analysis process), `07-software-engineering-plan.md`, `08-agent-briefing.md` |
| Hazard analysis process | SEMP §7.1 (`docs/plan/semp.md`) until a dedicated safety process document is written |
| Technology and heritage assessment | `docs/plan/technology-assessment.md` |
| Integration plan (SE-67) | `docs/plan/integration-plan.md` |
| Schedule and milestones (tailored SWE-016) | `docs/plan/schedule.md` |
| Cost model (tailored SWE-015/151) | `docs/plan/cost-estimate.md` |
| Budgets (link, noise, power, mass, thermal, spurious) | `docs/design/budgets.md` |
| Software architecture and design (SWE-057/058) | `docs/design/architecture.md`, `docs/design/software-design.md` |
| Build-to specifications and analyses | `docs/design/build-to-specification.md`, `docs/design/analysis/` |
| Operations handbook and user documentation | `docs/ops/operations-handbook.md` |
| Change requests | `docs/cm/cr/CR-NNN-<slug>.md` (disposition block = decision memo) |
| Tool validation and accreditation records (SWE-136) | `docs/cm/tool-validation/TV-NNN-<tool>.md`, summarized in `tools/toolchain.lock.md` |
| Configuration status accounting (SWE-083) | `docs/process/configuration-status.md` (generated) |
| Configuration audits (SWE-084) | `docs/reviews/SAR/configuration-audit.md` |
| Per-review working files | `docs/reviews/<REVIEW>/{minutes.md, checklists/, figures/, traceability-report.md, baseline-record.md, peer-reviews/INSP-NNN.md}` |
| Test configuration record, receipt inspections, V&V report, Part 97 compliance report | `docs/reviews/TRR/test-configuration-record.md`, `docs/vv/reports/receipt-inspection-<n>.md`, `docs/vv/reports/vv-report.md`, `docs/vv/reports/part97-compliance.md` |
| Unit as-built records and acceptance data packages | `docs/vv/adp/CWHT-A-NNN/as-built.md` |
| Hardware release packages (fab, assembly, CNC, order confirmations) | `hardware/releases/` |
| Software sprint records and measurements (SWE-090) | `docs/sprints/SW-NN-<module>.md`, `docs/plan/measurements.json` |
| Additional ICDs | `docs/icd/ICD-CTL-SW.md`, `docs/icd/ICD-SW-HOST.md` |

## 6. Identifier schemes

`NGO-NNN` need/goal/objective · `CON-NNN` stakeholder constraint · `SI-NNN` stakeholder input · `MOE-NNN` · `MOP-NNN` · `TPM-NNN` · `OPS-NNN` ConOps scenario · `REQ-<MOD>-NNN` requirement (modules: SYS, RX, TX, PWR, CTL, ME, SW-<sub>) · `TC-<MOD>-NNN` test/verification case · `ICD-<A>-<B>` interface · `ADR-NNN` decision record · `TS-NNN` trade study · `RSK-NNN` risk · `HZ-NNN` hazard · `NCR-NNN` nonconformance · `CR-NNN` change request · `RFA-<REV>-NNN` / `RID-<REV>-NNN` where `<REV>` is SRR, PDR, CDR, TRR, TRR-Dn or SAR · `TV-NNN` tool validation record · `INSP-NNN` peer review record · `MSR-NN` software measurement · `CS-NN` coding standard rule · `WP-SW-NN` rustos driver work package · `SW-NN-<module>` software sprint · `OQ-<AREA>-NNN` open question · `CWHT-A-NNN` unit serial · `<TC-ID>-rN` verification report. Requirement modules are SYS, RX, TX, PWR, CTL, ME and SW-<SUB> laid out as `docs/requirements/sw/<sub>/requirements.json`; VER is reserved and unused. IDs are never reused; a retired item keeps its ID with status *Closed*, tag `retired` and a rationale until a schema change adds a Retired status.

## 7. Requirements and bidirectional traceability

- **Levels.** L0 stakeholder expectations (NGOs, MOEs) → L1 system requirements (SYS) → L2 subsystem requirements (RX, TX, PWR, CTL, ME, SW) → design elements (architecture blocks, schematic sheets, Rust modules) → code → verification cases. Hazards trace to requirements (controls) and to verification.
- **Writing rules** (SE HB App. C): one "shall" per statement, active voice, quantified with units and tolerances, implementation-free, no unverifiable words (e.g. *adequate, robust, minimize*), rationale mandatory, verification method assigned at definition time. Schema: `docs/requirements/schema.json`.
- **Validation of requirements** before SRR follows the six steps of SE HB §4.2.1.2.4 (format, stakeholder satisfaction, technical correctness, feasibility, verifiability, non-redundancy); each L1 requirement is checked by an independent reviewer agent.
- **Traceability set** (NPR 7150.2D §3.12.1 Table 1, Class A): higher-level → software requirements; software requirements → hazards; software requirements → design components; design components → code; requirements → verification; requirements → nonconformances. `tools/traceability.py` enforces: unique IDs, every requirement has a parent or a documented self-derived rationale, every Draft or Active requirement has ≥1 verification case, every verification case cites ≥1 requirement, statuses are consistent. Hazards list their controlling requirements in `control_req_ids`. Its report is an entrance product of every review.
- **TBD/TBR.** No TBDs in a baselined document. TBRs are permitted with owner, closure plan and target review; all L1 TBRs close by PDR, all L2 TBRs by CDR.
- **Change control.** After SRR the requirements are under configuration control; changes go through a Change Request (`CR-NNN`) with impact assessment (cost, schedule, performance margins, safety, interfaces, verification) and owner approval acting as the Configuration Control Board. Requirements volatility is tracked (SWE-200).

## 8. Baselines and configuration management

- Configuration items: everything in §5 plus schematics, PCB, enclosure CAD, BOM, firmware source, simulation decks and checkers, tool versions (`tools/toolchain.lock.md`), scripts.
- Baselines: functional (SRR), allocated (PDR), product (CDR), as-built (SAR); each is an annotated git tag (`baseline/<review>`) pushed to `origin` (github.com/robinonsay/cwht, MIT) plus a baseline record listing CI versions. Tag signing is optional until the owner configures a signing key.
- Changes after a baseline require a `CR-NNN`; editorial changes, as defined in `docs/process/05-configuration-and-data-management.md`, are logged with an `Editorial:` commit trailer, not boarded.
- Configuration audits: a functional and a physical configuration audit are performed at SAR (as-built matches product baseline; firmware hash matches version description).
- Tool validation and accreditation (SWE-136): every analysis or build tool is listed with version and a documented sanity check (e.g. LTspice batch reproduces a known filter response; kicad-cli DRC reproduces a seeded violation).

## 9. Verification and validation philosophy

- Every requirement is verified by **Test, Analysis, Inspection or Demonstration**, chosen when the requirement is written. Pre-power-on evidence classes (the `type` values of `docs/test_cases/schema.json`; *Analysis* is a verification method, not a class): *Simulation* (LTspice, budgets, S-parameter models, Python checks), *HostUnit* (cargo test of application logic running on a host implementation of the rustos `api` traits with injected device models; the primary software evidence per SI-026), *Emulation* (optional, secondary: whole-binary scenarios on an RP2350 emulator for event ordering only, never timing), *Inspection* (ERC/DRC, schema and traceability checks, rendered-image review, and driver-to-datasheet traceability: every register access in a rustos driver cites the RP2350 datasheet or Cortex-M33 documentation section it implements). Post-build classes: *Bench* (owner's NanoVNA, tinySA Ultra with attenuator, dummy load, bench supply, multimeter, Pico-based logic capture) and *OnAir* demonstration. Hardware integration is verified on real hardware.
- "Run for the record" verification is performed on the delivered unit; pre-build simulations reduce risk but do not by themselves close a requirement unless the method is Analysis. Software requirements verified by HostUnit or Emulation take credit from a run on the tagged release binary and become Verified only when that release is installed on the delivered unit.
- Validation is against the ConOps scenarios and MOEs, with the owner as the user (SE HB §5.4).
- The V&V plan is baselined at PDR (SE-68) and updated at CDR; a TRR precedes bench testing; a nonconformance report is opened for any discrepancy (severity levels per SWE-202).

## 10. Software engineering commitments (NPR 7150.2D, Class A)

Detailed in `docs/process/07-software-engineering-plan.md`. Non-negotiables: recorded architecture and design (SWE-057/058); Rust coding standard with static analysis (clippy, unsafe audit, complexity) (SWE-061/135); unit tests that are repeatable with measured coverage (SWE-062/186/189/190); regression testing (SWE-191); safety-critical design provisions of SWE-134 a–l applied to keying, PA enable, charging supervision, thermal protection, audio output limiting and the shared safe-state manager, and to mission-critical frequency control and configuration load; MC/DC target of 100 % for safety-critical components (SWE-219) shown by independently reviewed decision tables and independence-pair tests plus tool-measured branch and condition coverage, because rustc has no MC/DC instrumentation (tailoring recorded in the RMM); cyclomatic complexity ≤ 15 (SWE-220); independent peer review with checklists of requirements, plans, design, code and test procedures (SWE-087/088/089); version description for every release (SWE-063); nonconformance tracking (SWE-201–204); bidirectional traceability (SWE-052).

## 11. Working rules for Claude and every agent

1. **Search first (HARD RULE, owner directive 2026-09-25).** Before any manual search of the repository or the corpus (grep, rg, find, glob, `ls` used as a search, or the Grep/Glob tools), Claude and every agent run the Claude Context vector search (`mcp__claude-context__search_code`, path `/Users/robinonsay/rust/cwht`) over the repo and `docs/references/md/`. Manual search is permitted only afterwards, to pin the exact line a semantic hit pointed at, or when the search tool is unavailable and the agent says so in its return. Reading a file at a known path is not a search. Cite retrieved guidance as `SE HB §x.y`, `NPR 7123.1D App. G Table G-6`, `SWE-134`, `SE-39`. A brief, workflow prompt or agent that skips this step is non-compliant and the product is returned for rework.
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
| CMMI rating (SWE-032), IV&V (SWE-141, 131, 178, 179), Center reporting (SWE-094, 174), joint audits (SWE-045), architecture review board (SWE-143) | Not applicable or tailored as recorded in the RMM | Presuppose NASA institutions. Intent preserved by independent agent review and a repo-local measurements file. Chapter-2 Center Director requirements (SWE-006, 091, 092, 142, 144, 214 to 217) have no project row in App. C and are institutional, outside the RMM. |
| Software assurance and safety standards (SWE-022, SWE-023, SWE-017 training) | Tailored | NASA-STD-8739.8 is not in the corpus; the safety-critical determination uses NPR 7150.2D's own criteria and SWEHB software-assurance tabs; training is the owner's and Claude's familiarization records. |
| Off-the-shelf components (SWE-027) | Tailored | IP counsel sub-item replaced by the MIT license and a third-party notice file; V&V of any external crate or model to the same level as developed code is retained. |
| MC/DC coverage (SWE-219) | Tailored | No Rust MC/DC instrumentation exists; see section 10. |
| Software cost estimation (SWE-015, 151) | Tailored | Replaced by a labor-free cost model: BOM, fabrication, assembly, enclosure and shipping estimates with contingency, updated at each review. |
| Schedules (SWE-016, 018, 046) | Tailored | Milestone list keyed to review gates and vendor lead times; no calendar commitments beyond those. |
| Spectrum manager concurrence, JCL, ILSP, human rating, project protection plan, launch-site items (NPR 7123.1D App. G guidance rows) | Customized (SE HB §3.11.4.3) | App. G rows are guidance, not SE-NN requirements; their omission is recorded in the review plan and SEMP. Owner is the FCC licensee; Part 97 compliance requirements replace spectrum-manager items. Compliance-matrix rows are needed only for SE-44, SE-51, SE-52 (tailored) and SE-62 (mass margin, fully compliant: a handheld carries a mass TPM, provisional allocation 350 g). |
| Human Systems Integration (SE-65/66) | Customized | HSI approach is a section of the SEMP covering controls, display, audio, key/paddle ergonomics and RF-exposure safety. |
| Cybersecurity assessment and mitigations (SWE-154, 156, 157, 159, 210) | Tailored | The radio has no network interface; the assessment covers USB firmware loading and command injection via the key input. |
| Secure coding and static analysis (SWE-185, 207) | Fully compliant | Retained in full; clippy and the coding standard. |
| Reuse cataloging and Government rights (SWE-147, 148, 214–217) | Not applicable | Open personal project; license recorded in the repo. |
