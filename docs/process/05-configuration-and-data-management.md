# cwht Configuration Management and Technical Data Management Plan

**Status:** Draft for SRR (functional baseline); revision 2, 2026-09-25 (independent review findings applied). **Expands:** charter §8 (baselines and configuration management), §4 step 4 (baseline tagging), §7 (change control), §11 rule 5. **Owner:** Robin (Decision Authority; Engineering Technical Authority; sole member and chair of the Configuration Control Board). **Author:** Claude (lead systems engineer; performs the CM function). **Governing text:** SE HB §6.5 (five CM functions), SE HB App. M (CM plan outline), SE HB §6.6 (technical data management), NPR 7123.1D §3.2.15 (SE-20) and §3.2.16 (SE-21), NPR 7150.2D §5.1 (SWE-079 through SWE-085), SWE-063, SWE-070, SWE-077, SWE-136, SWE-187, SWE-194, SWE-196, SWE-219, SWE-220. **ETA approval:** SE-20 and SE-21 each require an ETA-approved process; the ETA is the owner (charter §2). ETA approval of this CM process (SE-20) and of this technical data management process (SE-21) is the owner's approval of this plan, recorded in `docs/reviews/SRR/decision-memo.md`. Until that memo is signed both processes are proposed, and this plan is at level L1 at most.

This document is the Configuration Management Plan required by SWE-079 and the technical data management plan called for by SE HB §6.6.1.2.1. It is organised by the topics of SE HB App. M (scope, procedures per CM function, roles and resources, definitions, interfaces, deliverables, supplier flow-down) and by the five CM functions of SE HB §6.5.1.2 (planning, identification, change management, status accounting, verification). Where this plan and the charter disagree, the charter wins and this plan is corrected by a Change Request.

---

## 1. Scope and product definition

| Item | Definition |
|---|---|
| Product | cwht rev A: pocket 2 m true-CW (A1A) 5 W handheld transceiver. One PCB assembly (mainboard, PCBWay fabricated and assembled), one CNC aluminium enclosure (PCBWay), firmware for the Raspberry Pi Pico 2 (RP2350) written in Rust on `rustos`, and the documentation set of charter §5. |
| Configuration items (CIs) | Every artifact in charter §5 plus schematics, PCB layout, enclosure CAD, BOM, firmware source, simulation decks and checkers, tool versions (`tools/toolchain.lock.md`) and scripts (charter §8). The authoritative CI list is Table 4-1 (§4.2); every tracked file matches exactly one row under the matching rule of §4.2, checked at every review (§7.4). |
| Repository | `/Users/robinonsay/rust/cwht`, branch `main`. The repository is the single CM library and the single technical data store. Nothing is a CI unless it is in the repository or is an external item pinned by hash from the repository (Table 4-1 row 26). |
| External dependency | `rustos` (`/Users/robinonsay/rust/rustos`, remote `git@github.com:robinonsay/rustos.git`), consumed by the firmware crate as a Cargo path dependency. It is a CI (row 26): identified by its commit SHA in `tools/toolchain.lock.md` §3 and in every version description. |
| Out of scope | The owner's bench instruments (charter §9): NanoVNA, tinySA Ultra with the 30 to 40 dB attenuator, 50 ohm dummy load, bench supply, multimeter and the Pico-based logic capture. The instruments are not CIs; every test report records each instrument's identity (model and serial or owner label) and firmware version in its `instruments` field (`docs/templates/verification-report.md`). The instrument firmware and host software that produce Bench evidence (tinySA Ultra firmware, sigrok-pico capture firmware, `sigrok-cli`) are class B tools in `tools/toolchain.lock.md` with TV records due TRR (§9.1, §13; `docs/process/04-verification-and-validation.md` §6). Vendor internal processes are not controlled (§12). |

Applicable-document customizations recorded here (charter §1; mirrored in the SEMP, alignment item AL-12):

1. SE HB §6.5.1.2.2 names the fourth baseline *as-deployed* and places it at the ORR. This project names it *as-built* and sets it at SAR, because SAR absorbs ORR (charter §3) and charter §8 uses the name as-built. If the owner prefers the SE HB name, charter §8 changes (charter issue CI-5-1, §14.2).
2. SE HB §6.5.1.2.2 establishes the functional baseline at SDR. This project sets it earlier, at SRR, because the NGOs, MOEs, ConOps and L1 requirements are complete at SRR (charter §3) and configuration control from SRR is more conservative than control from PDR, the gate that absorbs SDR.

The allocated (PDR) and product (CDR) baselines keep their SE HB names and gates.

## 2. Definitions

| Term | Meaning on cwht |
|---|---|
| Configuration item (CI) | A file or set of files under `main` whose content defines, verifies or builds the product, matched by a row of Table 4-1 that gives its control class. |
| CI version | The git blob or tree hash of the CI at a given commit. A document's "version" is `<baseline tag>+<approved CR list>` or, outside a baseline, its last commit SHA. |
| CR-from event | The gate or event in the "CR from" column of Table 4-1 after which a non-editorial change to a class-CR CI needs an approved CR. |
| Baseline | The set of CI versions captured by an annotated git tag `baseline/<review>` (signed once the owner has configured a signing key, charter §8) plus the baseline record `docs/reviews/<REVIEW>/baseline-record.md`. Four baselines: functional (`baseline/srr`), allocated (`baseline/pdr`), product (`baseline/cdr`), as-built (`baseline/sar`). TRR and every delta TRR (`TRR-Dn`) set no baseline (charter §4 step 4). |
| Effective baseline | The most recent baseline tag plus all Change Requests approved and merged since it. `main` always equals the effective baseline plus merged Log-class and Record-class work and class-CR work whose CR-from event has not occurred. |
| Change Request (CR) | `CR-NNN`, file `docs/cm/cr/CR-NNN-<slug>.md` from `docs/templates/change-request.md`. The only vehicle for a non-editorial change to a class-CR CI after its CR-from event (charter §7, §8, §11 rule 5). |
| Configuration Control Board (CCB) | The owner (charter §7). Quorum is the owner. Claude proposes the class (I or II) of every CR and the owner confirms or changes it in the disposition. Dispositions given in chat are transcribed by Claude into the CR file the same session; the disposition block of the CR file is the decision memo for that change (charter §4 item 4). |
| Class I (major) change | Adapted from the SE HB §6.5.1.2.3 *major* change; Class I and Class II are project labels. A change to baseline configuration documentation that affects a baselined requirement or specification, cost, safety, an interface (ICD) or compatibility with interfacing products, verification evidence, or operator or maintenance training (it changes operator procedures, the operations handbook or maintenance instructions), or that requires rework, re-flash or retrofit of delivered products. |
| Class II (minor) change | Adapted from the SE HB §6.5.1.2.3 *minor* change: a change that corrects or modifies configuration documentation or processes without impact to form, fit, function, interchangeability, interfaces, safety, verification evidence or operator procedures. |
| Editorial change | A change that alters no technical meaning: spelling, grammar, formatting, link repair, re-rendering an image from an unchanged source, adding a cross-reference. Never editorial: any change to a "shall" statement, a number, a unit, an ID, a status field, a schema, source code (other than comments and `rustfmt` whitespace), a netlist, a footprint, a BOM line, a CAD dimension. |
| Product waiver | Adapted from the SE HB §6.5.1.2.3 *waiver*: an owner-approved release from meeting a baselined requirement or a SWE-219 or SWE-220 target, with rationale (SWE-220 itself requires any complexity exceedance to be reviewed and waived with rationale by the project manager or technical approval authority; the SWE-219 note says any deviation from 100 percent should be reviewed and waived with rationale by the TAs' approval, the single statement of this relief being `docs/process/01-lifecycle-and-reviews.md` section 8.6). Recorded either in a decision memo (`docs/reviews/<REVIEW>/decision-memo.md`, one numbered item `W<n>` per waiver) or in an approved CR whose disposition is `Approved (waiver)`. An authorized waiver does not change the baseline (SE HB §6.5.1.2.3). Identified by its `CR-NNN` or by `<memo path>#W<n>` (charter issue CI-5-4 proposes a dedicated identifier). Status-accounted in CSA item 12 (§6) and listed in VDD §7 of every release it affects. |
| Plan deviation | A departure from a procedure of this plan (not from a product requirement), recorded in `docs/cm/deviations.md` and CSA item 11 (§6). |
| Tailoring | Relief from a NASA process requirement; neither a product waiver nor a plan deviation. Recorded row by row in the RMM and compliance matrix with owner approval (charter §1). A change to a tailoring row after SRR is itself a CR. |
| Release | A CI set delivered outside the repository: a firmware image flashed to a unit or given to a friend, a fabrication and assembly package uploaded to PCBWay, a CNC package uploaded to PCBWay. Released files are immutable and identified per §4.3. |
| Source commit S, artifacts commit A (firmware) | S is the commit that sets the release version (§8.1 step 2); it is built, embedded in the image as `vX.Y.Z+<short S>`, and tagged `release/FW-vX.Y.Z`. A is the following commit that adds only the release directory and VDD (§8.1 step 7). |
| Configuration status accounting (CSA) | The recording and reporting of CI, baseline, change, waiver, release and audit status (SE HB §6.5.1.2.4, SWE-083), published as `docs/process/configuration-status.md` (§6). |
| FCA / PCA | Functional and Physical Configuration Audit (SE HB App. B; SE HB §6.5.1.2 "Conduct configuration audits"; SWE-084), performed at SAR (§7) and as a delta audit for every post-SAR release delivered to a unit (§8.4). |
| Version description (VDD) | `firmware/releases/VDD-vX.Y.Z.md` from `docs/templates/version-description.md`, one per firmware release including release candidates (SWE-063, charter §5). |
| Tool validation record | `TV-NNN`, file `docs/cm/tool-validation/TV-NNN-<tool>.md`, the SWE-136 evidence that a tool at a locked version is fit for a stated purpose (§9). |
| Unit as-built record | One per physical radio, identified by the unit serial `CWHT-A-NNN` (A = board revision letter, NNN sequential from 001), file `docs/vv/adp/CWHT-A-NNN/as-built.md` inside that unit's acceptance data package (layout set by `docs/process/04-verification-and-validation.md` and `docs/vv/README.md`): PCB release package and batch, enclosure release, firmware version and hash, acceptance test reports, recipient. |

## 3. Organisation, roles, responsibilities, authority and resources (SWE-079, SWE-082 b and c)

| Role | Held by | CM responsibilities and authority |
|---|---|---|
| CCB chair and sole member; change authority; ETA | Owner (Robin) | Dispositions every CR (Approved, Approved with conditions, Approved (waiver), Rejected, Deferred) and confirms its class. Approves every merge to `main` that touches a class-CR CI after its CR-from event. Approves each baseline (decision memo, charter §4) and, as ETA, this plan (SE-20, SE-21). Approves product waivers and tool accreditation (§9). Approves each release. Places vendor orders. Performs the hands-on steps of the PCA (§7) and flashes delivered units. Decides open questions in §14. |
| CM function | Claude (main session) | Maintains Table 4-1, assigns CR and TV numbers and unit serials, proposes CR classes, prepares CR packages, executes approved changes, creates baseline and release tags, writes baseline records and VDDs, generates the CSA, archives release packages, runs the document side of the FCA. |
| Change originator | Owner, Claude, or any agent | Drafts a CR from the template. Agents originate CRs through Claude, who files them. |
| Independent reviewer | A reviewer agent that did not author the change (charter §2, §11 rule 4) | Reviews the impact assessment of every Class I CR and of every Class II CR that touches requirements, ICDs, hazards or test cases before disposition; reviews editorial classification at each life-cycle review by sampling the editorial log; checks every baseline record, VDD and release package; performs the FCA checklist, the document-side PCA checks and every post-SAR delta configuration audit (§8.4). |
| Persons who make changes at each level (SWE-082 c) | Author agents on branches; Claude on `main` | Only Claude (main session) commits to `main` and pushes to `origin`, from this machine using the owner's SSH identity; no other account has push rights. Author agents commit only on `wip/`, `rid/` or `cr/` branches. The owner does no coding or layout (SI-011) and does not commit; the owner may edit stakeholder inputs and decision memos, which Claude then commits. |
| Software assurance | Independent reviewer agents (charter §2) | Check at each review that this plan is being followed: tags present and annotated (signed once the key is configured), CSA current, CR trailers on commits, no unreviewed class-CR merges, Table 4-1 matching every tracked file. Findings the owner adopts become RIDs (01 section 10.1). |

**Resources (SE HB App. M).** (1) Machine: the owner's Mac (macOS 26.6.2, arm64), the only build and CM host; its identity is recorded in `tools/toolchain.lock.md` §4. (2) Repository and remote: the local repository and `origin` (`git@github.com:robinonsay/cwht.git`, public, MIT). (3) Tools: every tool in `tools/toolchain.lock.md`, validated per §9; installers archived per §8.4. (4) People and time: the owner's time for CR dispositions (targets in §5.2), baseline, waiver and release approvals, vendor orders, hands-on PCA and flashing; Claude sessions and agent invocations for all other CM work. A change in any of these resources triggers the re-evaluation of §15.

## 4. Configuration identification (SE HB §6.5.1.2.2, SWE-081, SWE-082 a)

### 4.1 Levels of control

Every CI passes through these levels (SWE-082 a). The level is a property of the CI at a point in time and is reported in the CSA.

| Level | Name | Entry condition | Who may change it, how | Record |
|---|---|---|---|---|
| L0 | Working | File exists on any branch. | Author agent on `wip/<slug>` or `rid/<RID-ID>-<slug>`; Claude merges to `main` with a `Refs:` trailer. | Commit history. |
| L1 | Reviewed | An independent reviewer agent has recorded a checklist review with no open Major findings (charter §2). | Same as L0; a change that invalidates the review resets the CI to L0 and the review is redone before the CI is used as review evidence. | The filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md` carrying `id: INSP-NNN` in its front matter: the single peer-review record, with no separate record file (charter §5; `docs/process/01-lifecycle-and-reviews.md` §13; `tools/validate_docs.py` rejects a `peer-reviews/` folder). |
| L2 | Controlled | The class-CR CI is listed in §2a (CIs in the baseline) or §2c (controlled items outside the baseline set) of a committed baseline record, or its Table 4-1 CR-from event has occurred. Informational items (§2b) stay at L0 or L1. | Non-editorial change: approved CR, then Claude merges. Editorial change: Claude commits with an `Editorial:` trailer. Log and Record class CIs have no L2: they change by `Refs:` commits (Record: append only). | Baseline record, CR file, CSA. |
| L3 | Released | The release tag exists and the content has left the repository (flashed on a unit, uploaded to a vendor, handed over). | Files listed in the release's `SHA256SUMS` are never changed; a correction is a new release with a new identifier (§4.3) and a CR. The append-only parts of a release directory (VDD §9, `vendor/`, `configuration-audit.md`) follow the Record class. | Release directory with `SHA256SUMS`, VDD or package manifest, release tag. |

### 4.2 Configuration item list (Table 4-1)

**Control classes.** **CR**: after the CR-from event every non-editorial change requires an approved `CR-NNN`; before it the CI is at L0 or L1 and changes are Log-controlled. **Log**: never boarded; every change is a commit on `main` with a `Refs:` trailer and appears in the CSA change log. **Record**: append only; entries are added, never edited; corrections are new entries citing the old one; fields the Notes column declares *fill-once* are written exactly once. **Mixed**: the Notes column states which parts are CR and which are Log.

**Matching rule.** Every tracked file (`git ls-files`) matches exactly one row. The Pathspec column holds git pathspecs relative to the repository root: a trailing `/` is a directory prefix; `*` and `[...]` follow git's default fnmatch matching, in which `*` also matches `/`. When two rows match a path, an explicit file path or file-name pattern wins over a directory prefix, and among directory prefixes the longest wins. A rendered figure belongs to the row of the source file named by its file stem (§10.2). Untracked files are not CIs and are never committed unless they match a row.

**Row rules.** Rows are append-only: a row is never renumbered or reused, because CRs cite row numbers in `affected_cis`; a withdrawn row keeps its number with class `Withdrawn` and the CR that withdrew it. Adding, removing or reclassifying a row after SRR is a Class II CR against this plan.

| # | CI | Pathspec | ID scheme | Class | CR from | Notes |
|---|---|---|---|---|---|---|
| 1 | Process charter | `docs/process/00-charter.md` | n/a | CR | SRR | Charter §1: every process document expands it. |
| 2 | Process and planning documents | `docs/process/0[124-8]-*.md`, `docs/process/README.md`, `docs/plan/semp.md`, `docs/plan/schedule.md`, `docs/plan/cost-estimate.md` | n/a | CR | SRR | Includes this plan (05). |
| 3 | Software classification record, RMM, compliance matrix | `docs/process/03-software-classification-and-rmm.md`, `docs/process/rmm.json`, `docs/process/rmm.md`, `docs/process/se-compliance-matrix.json`, `docs/process/se-compliance-matrix.md` | SWE-NNN, SE-NN rows | CR | SRR | Tailoring change = CR with owner approval (charter §1). The two `.md` files are rendered by `tools/render_rmm.py` and `tools/render_compliance.py` and never hand-edited. |
| 4 | Stakeholder inputs log | `docs/requirements/l0-stakeholder/stakeholder-inputs.md` | SI-NNN | Record | n/a | Verbatim, never edited (file header). |
| 5 | Stakeholder expectations, MOEs, constraints | `docs/requirements/l0-stakeholder/expectations.json`, `docs/requirements/l0-stakeholder/expectations.md` | NGO-NNN, MOE-NNN, CON-NNN | CR | SRR | Functional baseline; `.md` rendered. |
| 6 | ConOps | `docs/conops/` | OPS-NNN | CR | SRR | Functional baseline. |
| 7 | L1 system requirements | `docs/requirements/sys/` | REQ-SYS-NNN | CR | SRR | Charter §7: under configuration control after SRR. |
| 8 | L2 subsystem requirements, software requirements | `docs/requirements/rx/`, `docs/requirements/tx/`, `docs/requirements/pwr/`, `docs/requirements/ctl/`, `docs/requirements/me/`, `docs/requirements/sw/` | REQ-<MOD>-NNN | CR | PDR | Allocated baseline. |
| 9 | Schemas | `docs/*schema.json` (every schema under `docs/`; on 2026-09-25: `docs/requirements/schema.json`, `docs/requirements/l0-stakeholder/schema.json`, `docs/test_cases/schema.json`, `docs/risk/schema.json`, `docs/safety/schema.json`, `docs/process/rmm.schema.json`, `docs/process/se-compliance-matrix.schema.json`, `docs/plan/tpm.schema.json`, `docs/templates/rfa-rid-log.schema.json`); schema copies inside the fixture root are fixtures of row 28 | n/a | CR | SRR | Every schema gates validation evidence. A schema change and the data migration it forces are made atomically: one commit (or one CR merge) carries the schema and every data file it affects, with the `tools/validate_docs.py` result and the unit-test count in the commit message. A schema CR lists the re-validation it triggers (`tools/validate_docs.py` over the affected files) and is Class I when it adds or changes a required field or an enum; from SRR, such a Class I CR carries the migration of every affected data file in its implementation. |
| 10 | Interface control documents | `docs/icd/` | ICD-<A>-<B> | CR | PDR | Class I whenever an external interface (key jack, headphone, antenna, USB, battery) changes. |
| 11 | Architecture, allocation, budgets, software design | `docs/design/architecture.md`, `docs/design/allocation.json`, `docs/design/budgets.md`, `docs/design/software-design.md`, `docs/design/sw/` | n/a | CR | PDR (architecture, allocation, budgets); CDR (software design, `docs/design/sw/`) | Software design per `07-software-engineering-plan.md` §3.5 and §5. `docs/design/sw/<module>.md` is not yet in charter §5 (charter issue CI-5-6, carried from 07 §22). |
| 12 | Trade studies | `docs/decisions/trade-studies/` | TS-NNN | Record | n/a | Immutable once the decision is taken; a revisit is a new TS citing the old. |
| 13 | Architecture decision records | `docs/decisions/adr/` | ADR-NNN | Record | n/a | Superseded, never edited; the status field is the only editable line (Accepted, Superseded by ADR-MMM). |
| 14 | Risk register | `docs/risk/register.json`, `docs/risk/register.md` | RSK-NNN | Log | n/a | Updated continuously; reviewed at each gate; `.md` rendered by `tools/render_risk.py`. |
| 15 | Hazard analysis, hazard list | `docs/safety/hazard-analysis.md`, `docs/safety/hazards.json` | HZ-NNN | CR | PDR | Every change is Class I (safety). |
| 16 | V&V plan | `docs/vv/plan.md` | n/a | CR | PDR | Charter §9: baselined at PDR, updated at CDR by CR. |
| 17 | Test cases and procedures | `docs/test_cases/` | TC-<MOD>-NNN | CR | SRR (cases citing L1 requirements); PDR (all other cases) | Under CR control together with the requirements they cite (`docs/process/04-verification-and-validation.md`); procedure steps, setup and instruments complete by CDR. Procedures executed for the record are the baselined version (FCA-04). |
| 18 | Verification matrices, traceability report | `docs/vv/traceability-report.md`, `docs/vv/traceability.json`, `docs/reviews/*/traceability-report.md`, `docs/reviews/*/traceability.json` | n/a | Log | n/a | Generated by `tools/traceability.py`; regenerated before every review and at every baseline; never hand-edited. The per-review report and its data file are written by the command of `docs/process/01-lifecycle-and-reviews.md` section 3.1 item 2 (`--output docs/reviews/<REVIEW>/traceability-report.md`, which writes `traceability.json` beside it), not copied from `docs/vv/`; they are that review's evidence and are not regenerated after the review. |
| 19 | Test reports, receipt inspections, V&V report, Part 97 compliance report | `docs/vv/reports/` | `<TC-ID>-rN` | Record | n/a | Each report names what was tested per §7.3. |
| 20 | Nonconformance reports | `docs/vv/ncr/` | NCR-NNN | Record | n/a | Disposition fields appended; a disposition that changes a controlled CI cites a CR. |
| 21 | Schematics and PCB layout | `hardware/kicad/` | n/a | CR | CDR | Product baseline. Backups and caches are gitignored. |
| 22 | Bill of materials | `hardware/bom/` | n/a | CR | CDR | Part substitutions, including vendor-proposed ones, are CRs (§4.3 package rule). |
| 23 | Enclosure CAD | `hardware/enclosure/` | ME-ENC-rev<X> | CR | CDR | `.scad` is the source; `.csg` and `.step` are exported per §8.2 step 3; `.stl` and `.3mf` are derived and gitignored. |
| 24 | Simulation decks and checkers | `hardware/sim/` | n/a | CR | CDR | Analysis evidence for the product baseline. |
| 25 | Firmware source | `firmware/` (crate sources, `Cargo.toml`, `Cargo.lock`, `.cargo/config.toml`, `rust-toolchain.toml`, linker inputs, `build.rs`, `THIRD-PARTY-NOTICES.md`) | FW-vX.Y.Z | CR | first `release/FW-*` tag, including a release candidate | Under CM (identified, versioned, status-accounted) from its first commit; SWE-187 is met by testing only tagged source commits (§7.3). Listed after its trigger in every baseline record as a controlled item outside the baseline set (§4.4). |
| 26 | External: `rustos` | none (outside the repository; the pinned commit is recorded in row 27, lock §3, and in each VDD) | commit SHA | CR | first `release/FW-*` tag | Moving the pin is a CR listing the `rustos` changes pulled in. Listed after its trigger in every baseline record (§4.4). |
| 27 | Toolchain lock and venv pins | `tools/toolchain.lock.md`, `tools/requirements.txt` | n/a | Mixed | SRR | After SRR a version change of an Accredited tool is a CR (Class I if the tool can change a released image) plus a new TV record; every other change (a new row, a class C tool, an unaccredited tool, a re-observation with no version change, a sanity-check result) is a Log commit with `Refs:` (§9.2 step 5). `tools/requirements.txt` pins exactly the versions of lock §2. |
| 28 | Verification, CM and build tooling | `tools/` (every file not in rows 27, 29 or 40): `tools/traceability.py`, `tools/validate_docs.py`, `tools/render_rmm.py`, `tools/render_compliance.py`, `tools/render_risk.py`, `tools/review_trend.py`, `tools/slides/` (`package.json`, `package-lock.json`, `render_deck.py`), `tools/tests/` (unit tests and the single fixture root `tools/tests/fixtures/`), and the planned tools named with their due gates in §13 | TV-NNN (accreditation) | CR | date of the tool's TV record | Accreditation puts the tool under CR control; before that Log. Each accredited tool is listed after its TV date in every baseline record as a controlled item outside the baseline set (§4.4). `tools/slides/node_modules/` is gitignored and reproduced from `package-lock.json`. |
| 29 | Corpus conversion scripts | `tools/refs/` | n/a | Log | n/a | Not product or evidence generating. |
| 30 | Tool validation records | `docs/cm/tool-validation/` | TV-NNN | Record | n/a | |
| 31 | Change requests | `docs/cm/cr/` | CR-NNN | Record | n/a | Committed on `main` with `Refs: CR-NNN` at every state change (§5.2); state transitions appended in the CR's history section; the `cr/` branch carries only product changes. |
| 32 | Baseline records | `docs/reviews/*/baseline-record.md` | n/a | Record | n/a | Written once per baseline (§4.4 step 2). Fill-once fields: front matter `commit`, `tag_object`, `signed`, `signature_verified`, `pushed_hash`, §8a and the §9 approvals, written in the §4.4 step 6 commit. Corrections: dated entries in §10. |
| 33 | Review records | `docs/reviews/` | RFA-<REV>-NNN, RID-<REV>-NNN, INSP-NNN | Record | n/a | Packages, slide decks (charter §4 item 2), RFA/RID logs, minutes, decision memos, filled peer-review checklists, figures, and the test configuration records `docs/reviews/TRR/test-configuration-record.md` and `docs/reviews/TRR-Dn/test-configuration-record.md` (SWE-187, §7.3). The reveal.js runtime copied beside each deck is gitignored; the PNG renders are the record. |
| 34 | TPMs and leading indicators | `docs/plan/tpm.json` and its plots | TPM-NNN, MOP-NNN | Mixed | PDR | TPM definitions are CR-controlled allocated-baseline content from PDR; measured values are appended (Record). |
| 35 | Configuration status report | `docs/process/configuration-status.md` | n/a | Log | n/a | Generated (§6); never hand-edited once `tools/csa.py` exists. |
| 36 | Firmware releases and VDDs | `firmware/releases/` | FW-vX.Y.Z | Record (level L3) | n/a | Files listed in each `SHA256SUMS` are immutable. Append-only parts: VDD §9 (fill-once, §8.1 step 11) and the post-SAR delta configuration audit `firmware/releases/vX.Y.Z/configuration-audit.md` (§8.4). |
| 37 | Hardware release packages | `hardware/releases/` | HW-MB-rev<X>-<n>, ME-ENC-rev<X>-<n> | Record (level L3) | n/a | Files listed in each `SHA256SUMS` are immutable; vendor records are appended under `vendor/` (§8.2 step 7). |
| 38 | Unit as-built records and acceptance data packages | `docs/vv/adp/` | CWHT-A-NNN | Record | n/a | One per physical radio; layout per `docs/vv/README.md`. |
| 39 | Configuration audit record | `docs/reviews/SAR/configuration-audit.md` | n/a | Record | n/a | FCA and PCA sections; location per the SAR criteria in `docs/process/01-lifecycle-and-reviews.md`. |
| 40 | Research reports, lessons learned, tutorials, README files | `docs/research/`, `docs/lessons-learned.md`, `docs/tutorials/`, `README.md`, `docs/requirements/README.md`, `tools/README.md` | n/a | Log | n/a | |
| 41 | Reference corpus (third-party conversions) | `docs/references/` | n/a | Log | n/a | Source PDFs gitignored; see §10.5. |
| 42 | Repository configuration | `.gitignore`, `.mcp.json`, `*.gitkeep` | n/a | Log | n/a | `.venv/` is not a CI; it is reproduced from row 27 (§9.3). |
| 43 | CM deviations log | `docs/cm/deviations.md` | n/a | Record | n/a | Departures from this plan with date, RFA raised and closure (CSA item 11). |
| 44 | Software sprint records and index | `docs/sprints/` | SW-NN-<module> | Record | n/a | `07-software-engineering-plan.md` §3.4; a closed sprint record is never edited, corrections are new dated entries. |
| 45 | Software measurements | `docs/plan/measurements.json` | MSR-NN | Record | n/a | Appended by `tools/measurements.py` at sprint closure and release (07 §11.1); TPM-derived values mirrored into row 34. |
| 46 | Unsafe audit list | `firmware/unsafe-audit.md` | n/a | Log | n/a | Generated by `tools/unsafe_audit.py` (07 CS-06, CS-07); reviewer signatures (`INSP-NNN`) appended, never removed. |
| 47 | Operations handbook and user documentation | `docs/ops/` | n/a | CR | SAR | SWE-077 delivery record (PCA-10, as-built baseline); Log before SAR. |
| 48 | RF exposure evaluation | `docs/design/analysis/rf-exposure-evaluation.md` | n/a (controls HZ-001) | CR | PDR | Controlled regulatory document (charter §5; 47 CFR 97.13, 1.1307); every change is Class I (safety and regulatory). |
| 49 | Build-to specification and design analyses | `docs/design/build-to-specification.md`, `docs/design/analysis/` | n/a | CR | CDR | Product-baseline build-to data, including design-for-debug and producibility rules (charter §5). |
| 50 | Integration plan | `docs/plan/integration-plan.md` | n/a | CR | PDR | SE-67. |
| 51 | Technology and heritage assessment | `docs/plan/technology-assessment.md` | n/a | CR | SRR | SRR product (charter §3). |
| 52 | Design concept | `docs/design/concept.md` | n/a | Mixed | SRR | CR-controlled from SRR; becomes a Record (frozen) when `baseline/pdr` is tagged, because row 11 supersedes it; after PDR only dated correction notes are appended. |
| 53 | Templates and peer-review checklists | `docs/templates/` (the schema in it belongs to row 9) | n/a | CR | SRR | A checklist change invalidates L1 reviews made against the earlier revision; its CR lists every `INSP-NNN` record to re-run, or to keep with a rationale. Includes this plan's templates (change request, version description, baseline record). |
| 54 | V&V data-package layout | `docs/vv/README.md` | n/a | CR | PDR | Defines the acceptance data package layout this plan uses (row 38, §8.3). |
| 55 | Licence | `LICENSE` | n/a | Record | n/a | MIT (ADR-017, SI-025); a licence change is an ADR decided by the owner. |

### 4.3 Identifiers and version marking

This plan defines the CM identifiers that charter §6 does not (release identifiers and tags) and is subordinate to charter §6 (charter issue CI-5-2 proposes adding them there).

| Object | Identifier | Where marked |
|---|---|---|
| Documents, requirements, tests, decisions, risks, hazards, NCRs, CRs, RFAs, RIDs | Charter §6 schemes. Charter §6 retirement rule, verbatim: "IDs are never reused; a retired item keeps its ID with status *Retired* where its schema has that status, otherwise status *Closed* with tag `retired`, plus a rationale." | In the file; in commit trailers. |
| Tool validation record | `TV-NNN` | `docs/cm/tool-validation/`; referenced from `tools/toolchain.lock.md`. |
| Physical unit | `CWHT-A-NNN` | `docs/vv/adp/CWHT-A-NNN/as-built.md`; written on a label inside the enclosure and in the firmware's stored unit ID if the design provides one (decision at PDR, recorded as an ADR). |
| Firmware release | `FW-vX.Y.Z` (semantic versioning: MAJOR = incompatible operator-facing or hardware-compatibility change, MINOR = new capability, PATCH = defect fix). `X.Y.Z` is the `version` field of the firmware crate's `Cargo.toml`. Candidates: `FW-vX.Y.Z-rcN`. | `Cargo.toml`; tag `release/FW-vX.Y.Z` on the source commit S (§8.1); binary info read by `picotool info` (program name `cwht`, program version `vX.Y.Z+<short S>`, where `<short S>` is printed by `git rev-parse --short=7 HEAD` at S during the build; every later record copies the embedded string and never recomputes it); VDD file name. |
| PCB fabrication and assembly package | `HW-MB-rev<X>-<n>`. `<X>`, the board revision letter printed on the silkscreen, changes for any copper, footprint, outline, drill or silkscreen change. `<n>`, the package sequence for that revision, changes for a re-export after a Class II package fix and for a BOM-only change (a substitution with the same footprint, or a value change of a fitted part); the silkscreen then keeps `rev<X>`. | Silkscreen carries `cwht MB rev<X>`; directory `hardware/releases/HW-MB-rev<X>-<n>/`; tag `release/HW-MB-rev<X>-<n>`; each unit's `as-built.md` names the `-<n>` package it was built from. |
| Enclosure CNC package | `ME-ENC-rev<X>-<n>`. `<X>` changes for any dimension, feature, material or finish change; `<n>` for a re-export or a drawing-only Class II fix. | Directory `hardware/releases/ME-ENC-rev<X>-<n>/` (not yet in charter §5, charter issue CI-5-3); tag `release/ME-ENC-rev<X>-<n>`. |
| Baseline | `baseline/srr`, `baseline/pdr`, `baseline/cdr`, `baseline/sar` | Annotated tag (signed once the key is configured, §4.4); `docs/reviews/<REVIEW>/baseline-record.md`. |
| Release candidate (firmware under formal test before a full release) | `FW-vX.Y.Z-rcN`, tag `release/FW-vX.Y.Z-rcN`, released through §8.1 with its own VDD | Cited in every test report run on it; never flashed on a unit handed to others. |
| CI version | git blob hash (`git ls-tree <tag> -- <path>`) or tree hash for directories | Baseline record, CSA. |

### 4.4 Baselines

| Baseline | Gate | CR-class contents (Table 4-1 rows) | Informational versions (not yet CR-controlled) | Controlled items outside the baseline set | Tag | Record |
|---|---|---|---|---|---|---|
| Functional | SRR | 1, 2, 3, 5, 6, 7, 9, 17 (cases citing L1 requirements), 27, 51, 52, 53 | 14; 15 (preliminary hazard analysis) | 28 (tools with a TV record by SRR) | `baseline/srr` | `docs/reviews/SRR/baseline-record.md` |
| Allocated | PDR | Functional baseline as amended, plus 8, 10, 11 (architecture, allocation, budgets), 15, 16, 17 (all other cases), 34 (definitions), 48, 50, 54 | 21, 23, 24 (preliminary design data) | 25 and 26 once a release tag exists; 28 | `baseline/pdr` | `docs/reviews/PDR/baseline-record.md` |
| Product | CDR | Allocated baseline as amended, plus 11 (software design), 21, 22, 23, 24, 49, and the release packages 37 generated from them (procurement release, charter §3) | none | 25, 26 (the first candidate precedes CDR, 07 §3.1), 28 | `baseline/cdr` | `docs/reviews/CDR/baseline-record.md` |
| As-built | SAR | Product baseline as amended, plus 25 and 26 at the accepted release tag, 36, 37 (with vendor records), 38, 39, 47, and 19 (`docs/vv/reports/vv-report.md` and every credited report) | the SAR archive list (§8.4) | 28 | `baseline/sar` | `docs/reviews/SAR/baseline-record.md` |

Rows 25, 26 and 28 are listed after their CR-from event in §2c of every baseline record, with their hash at the tag, as controlled items outside the baseline set: they are under CR control but a baseline does not fix them.

**Baseline procedure** (executed by Claude after the owner's decision memo records Approved or Approved with liens; charter §4 step 4):

1. Confirm `main` is clean, `tools/traceability.py` passes, `git fsck --full` exits 0, every tracked file matches a Table 4-1 row (§4.2), and every CI listed for the baseline is at L1 (filled checklist with `id: INSP-NNN`) with no open Major RID against it.
2. Write `docs/reviews/<REVIEW>/baseline-record.md` from `docs/templates/baseline-record.md`: the §1 "Decision memo" row with the memo path, disposition, date and memo commit (the commit that set `signed` in the memo, `git log -1 --format=%H -- docs/reviews/<REVIEW>/decision-memo.md`); for each CI, path and hash from `git ls-tree HEAD -- <path>`; approved CRs and waivers since the previous baseline; liens carried; TBR list. Fill-once fields hold the text `pending (§8a)`.
3. Commit the record on `main` as commit R with message `baseline(<review>): record <name> baseline` and trailer `Refs: <REVIEW>`.
4. The independent reviewer checks the record against the repository at R (every hash by `git ls-tree R -- <path>`); the result is written in step 6.
5. Tag R: `git tag -a baseline/<review> <R> -m "cwht <name> baseline; decision memo docs/reviews/<REVIEW>/decision-memo.md at <memo commit>"`, where `<memo commit>` is the hash of the record's §1 "Decision memo" row; when `tag.gpgSign` is configured (below) `git tag -s` replaces `-a`. Verify with `git tag -v baseline/<review>` for a signed tag or `git cat-file -p baseline/<review>` for an unsigned one (tagger, date, message, target commit). Push with `git push origin main --follow-tags` to `origin` (`git@github.com:robinonsay/cwht.git`, charter §8; §10.4) and confirm with `git ls-remote --tags origin baseline/<review>`.
6. Post-tag record: write the fill-once front-matter fields, §8a (verbatim verification output and the `ls-remote` hash) and the §9 approvals (reviewer result from step 4) of the record; commit with message `baseline(<review>): record tag verification` and trailer `Refs: <REVIEW>`; regenerate the CSA (§6 item 3); push again. This commit follows R; the tag stays on R.

**Tag signing (optional until configured, charter §8).** Baseline and release tags are always annotated. Signing is added once the owner configures a key; until then unsigned annotated tags are compliant, the CSA records `signed: no` for them and no deviation is logged. Tags created before the key exists are not re-created. No signing key is configured in this repository as of 2026-09-25 (`git config gpg.format`, `user.signingkey` and `tag.gpgSign` are unset) but `~/.ssh/id_ed25519.pub` exists. Recommended one-time setup (owner action, OQ-CM-002):

```
git -C /Users/robinonsay/rust/cwht config gpg.format ssh
git -C /Users/robinonsay/rust/cwht config user.signingkey ~/.ssh/id_ed25519.pub
git -C /Users/robinonsay/rust/cwht config tag.gpgSign true
mkdir -p /Users/robinonsay/rust/cwht/.git/allowed_signers
printf '%s %s\n' "$(git config user.email)" "$(cat ~/.ssh/id_ed25519.pub)" > /Users/robinonsay/rust/cwht/.git/allowed_signers/file
git -C /Users/robinonsay/rust/cwht config gpg.ssh.allowedSignersFile .git/allowed_signers/file
```

From the first tag created after this setup, every `baseline/*` and `release/*` tag is signed and the CSA records the `git tag -v` result. Tags are never moved, deleted, re-signed or re-created; a wrongly placed tag is recorded in the CSA deviations table and a corrected tag `baseline/<review>-2` is created through a Class II CR.

### 4.5 Branch, commit and merge conventions

| Rule | Statement |
|---|---|
| Trunk | `main` holds the effective baseline (latest `baseline/*` tag plus approved and merged CRs) and merged Log-class and Record-class work. `main` is always buildable and passes `tools/traceability.py`. |
| Branch per change | One branch per CR: `cr/CR-NNN-<slug>`. Work before a CI's CR-from event: `wip/<slug>`. RID closure before the product's CR-from event: `rid/RID-<REV>-NNN-<slug>`. Release preparation: `rel/FW-vX.Y.Z`. Branches are deleted after merge; the merge commit preserves them. |
| Commit message | First line `<type>(<scope>): <summary>` where `type` is one of `feat`, `fix`, `docs`, `test`, `tool`, `hw`, `sim`, `editorial`, `release`, `baseline`, `chore` and `scope` is a module or artifact name. Body explains why. Trailers (one per line, at the end): `Refs: <ID>[, <ID>...]` mandatory whenever a CI is touched (REQ, TC, ICD, ADR, TS, RSK, HZ, NCR, RFA, RID, SI, TV, CR, a release identifier, a unit serial `CWHT-A-NNN` or a review name); `CR: CR-NNN` mandatory for any non-editorial commit that touches a class-CR CI after its CR-from event; `Editorial: <reason>` mandatory for editorial commits to a class-CR CI after its CR-from event; `Co-Authored-By:` naming the agent for agent-authored commits. |
| Merges to `main` | Always `git merge --no-ff` with message `merge(CR-NNN): <title>` or `merge(<slug>): <title>`. A merge that touches a class-CR CI after its CR-from event requires the CR file to show `disposition: Approved` (or `Approved with conditions`, with the conditions satisfied) before the merge; Claude performs the merge and records the merge SHA in the CR. Merges of Log-class and Record-class work are performed by Claude without owner action. |
| History integrity | No force pushes to any branch that has been pushed; no rewriting of `main` history; no `git tag -f`; no `git commit --amend` on `main`. Amending unpushed commits on a `wip/`, `rid/` or `cr/` branch before review is permitted. On `origin` (GitHub) the owner enables branch protection for `main` (block force pushes and deletion) and tag protection for `baseline/*` and `release/*` (OQ-CM-001); until then the rule is enforced by this plan alone and the independent reviewer checks `git reflog show origin/main` for non-fast-forward updates at each review. |
| Applicability | The commit-message and trailer rules apply from the SRR readiness declaration onward; earlier history (Phase A checkpoints) is not re-written and is not a deviation. |
| Generated files | Rendered images, traceability reports and the CSA are committed together with the source change that produced them, in the same commit or merge. |
| Checks | `tools/check_commit_msg.py` runs as a `commit-msg` hook from PDR (class B, TV due PDR, §13). Until then, and at every review afterwards, the independent reviewer runs `git log --format='%h %s%n%(trailers)' <prev-baseline>..HEAD` and raises a RID for any commit touching a class-CR CI after its CR-from event without a `CR:` or `Editorial:` trailer. |

## 5. Configuration change management (SE HB §6.5.1.2.3, SWE-080)

### 5.1 When a CR is required

| Situation | Vehicle |
|---|---|
| Non-editorial change to a class-CR CI after its CR-from event (Table 4-1) | `CR-NNN` |
| Change to a tailoring row (RMM, compliance matrix) after SRR | `CR-NNN` (charter §1); the RMM row cites the CR |
| Vendor-proposed change (PCBWay DFM comment, DigiKey substitution) that alters the product baseline | `CR-NNN`; Class I if electrical, footprint or safety impact, else Class II; a new package per the §4.3 rule |
| NCR disposition "repair" or "use-as-is" that changes a controlled document or requirement | `CR-NNN` cited from the NCR |
| RID against a product after its CR-from event (e.g. an L1 requirement found wrong at PDR) | `CR-NNN`; the RID closure cites the CR |
| RID against a product before its CR-from event | `rid/` branch, no CR |
| Product waiver (release from a baselined requirement or from a SWE-219 or SWE-220 target) | `CR-NNN` with disposition `Approved (waiver)`, or a numbered waiver `W<n>` in a decision memo (§2) |
| A CR targeted at a release is to be left out of it | Owner re-disposition (decision Deferred, new target) recorded in the CR's disposition history before the release's source commit (§8.1 step 1) |
| Moving the `rustos` pin after the first `release/FW-*` tag | `CR-NNN` (row 26) |
| Version change of an Accredited tool after SRR | `CR-NNN` (Class I if the tool can change a released image: `rustc`, `cargo`, linker, `picotool`, `kicad-cli` exports, OpenSCAD, FreeCAD) plus a new `TV-NNN` (§9.2 step 5) |
| New lock row; version change of a class C tool or of a tool not yet Accredited; re-observation with no version change | Log commit with `Refs:` (row 27) |
| Editorial change to a class-CR CI after its CR-from event | Commit with `Editorial:` trailer; logged in the CSA; sampled by the independent reviewer at the next review |
| Change to a Log or Record class CI | Commit with `Refs:` trailer |

### 5.2 CR lifecycle

The CR file is a Record (row 31) committed on `main` with `Refs: CR-NNN` at every state change; the branch `cr/CR-NNN-<slug>` carries only the product changes. Claude proposes the class; the owner confirms or changes it in the disposition.

| State | Entered when | Actor | Artifact and required content |
|---|---|---|---|
| Draft | Originator identifies a needed change. Claude assigns the next `CR-NNN` from the CSA register and creates `docs/cm/cr/CR-NNN-<slug>.md`. | Originator via Claude | Front matter: id, title, status, proposed class, originator, date_opened, phase, baseline affected, affected_cis (Table 4-1 row numbers), affected_paths, affected_ids, target release if any. Sections: description, reason, alternatives. |
| Submitted | Description and impact assessment complete (§5.3). | Claude | Impact assessment table filled with numbers, not adjectives. Branch `cr/CR-NNN-<slug>` may be opened for prototyping; nothing merges. |
| Assessed | Independent reviewer has reviewed the impact assessment (mandatory for Class I; for Class II when requirements, ICDs, hazards or test cases are affected; otherwise marked "Not required"). | Independent reviewer agent | Reviewer section: findings, concurrence or objections. |
| Dispositioned | Owner records Approved, Approved with conditions, Approved (waiver), Rejected or Deferred, and confirms the class. Chat decisions are transcribed the same session. | Owner | Disposition block: decision, class, date, conditions, rationale. |
| Deferred | Disposition Deferred. Held with a re-look trigger (an event or a date) and a re-look-by review. When the trigger fires Claude refreshes the impact assessment and returns the CR to Submitted for a new disposition. | Owner, then Claude | Re-look trigger and date in the disposition block and front matter. |
| Implemented | All commits on `cr/CR-NNN-<slug>` carry `CR: CR-NNN`; every affected artifact updated (requirements, ICDs, design, tests, hazards, VDD or package manifest as applicable); `tools/traceability.py` passes; renders regenerated. An `Approved (waiver)` CR that changes no artifact skips this state and the next. | Claude or author agent | Implementation section: commit list, files changed, traceability report link. |
| Verified | Independent reviewer confirms each impact item was closed as planned (tests re-run and passed, analyses redone, documents consistent). For Class I CRs affecting a released item, the re-verification evidence is a test report in `docs/vv/reports/`. | Independent reviewer agent | Verification section: evidence links, result. |
| Closed (terminal) | Merged: owner approves the merge; Claude merges `--no-ff`, records the merge SHA, regenerates the CSA. Waiver without artifact change: Claude enters the waiver in CSA item 12 and every affected VDD. Rejected: Claude sets `status: Closed`, `merge_sha: n/a` the same session; the CSA shows it as "Closed (Rejected)". | Owner, then Claude | Closure block: merge SHA or `n/a`, date. |
| Withdrawn (terminal) | Originator withdraws before disposition. | Originator | Status set; reason recorded. |

Cycle-time targets (reported in the CSA metrics): Class II dispositioned within one working session of submission; Class I within the next review or two weeks, whichever is earlier. These are targets, not commitments (charter §12 schedules row).

### 5.3 Impact assessment fields (mandatory for every CR)

| Field | What must be stated | Source artifact |
|---|---|---|
| Performance margins | Each MOP/TPM affected: value and margin before and after; any budget (power, thermal, link, spurious emissions, mass, volume) touched, with numbers. | `docs/plan/tpm.json`, analysis files in `hardware/sim/` and `docs/design/analysis/` |
| Safety | Hazards (`HZ-NNN`) affected; every component in the safety-critical and mission-critical tables of `docs/process/07-software-engineering-plan.md` §14.1 that changes, listed by module id (the 07 §14.1 tables are the single authoritative list, charter §10); whether the hazard analysis needs re-issue; whether the RF exposure evaluation (row 48) changes. | `docs/safety/hazards.json`, 07 §14.1 |
| Risk | `RSK-` ids added, closed or re-scored, with likelihood and consequence before and after. | `docs/risk/register.json` |
| Software classification and tailoring | Whether the classification record, any `rmm.json` row or any compliance-matrix row changes (a tailoring change is itself a CR, §5.1). | `docs/process/03-software-classification-and-rmm.md`, `docs/process/rmm.json`, `docs/process/se-compliance-matrix.json` |
| Interfaces | ICDs affected; external-interface change flag (key jack, headphone jack, antenna connector, USB, battery). | `docs/icd/` |
| Operations and ConOps | `OPS-` scenarios affected; operator procedures, operations handbook or maintenance instructions that change (any yes makes the CR Class I, §2). | `docs/conops/conops.md`, `docs/ops/operations-handbook.md` |
| Cybersecurity | Whether the USB firmware-load path or the key-input command path changes (charter §12 cybersecurity row; 07 §16), and the mitigations affected. | 07 §16 |
| Verification | TCs invalidated, TCs to add or modify, evidence class affected (Simulation, HostUnit, Emulation, Inspection, Bench, OnAir; the `type` values of `docs/test_cases/schema.json`), re-test scope, and for safety-critical modules the decision tables and independence-pair tests affected (07 §9.6). | `docs/test_cases/`, `docs/vv/plan.md` |
| Cost | BOM delta (parts and vendor pricing), re-fabrication or re-machining cost, shipping, contingency change. | `hardware/bom/`, `docs/plan/cost-estimate.md` |
| Schedule | Vendor lead time impact, gate affected, dependency on other CRs. | `docs/plan/schedule.md` |
| Requirements and traceability | Requirements added, modified, deleted or retired by ID and level; parents and children affected; volatility contribution (SWE-200). | `docs/requirements/`, traceability report |
| Regulatory | 47 CFR Part 97 clauses affected (emission bandwidth, spurious, power), and Parts 1, 2 and 15 where relevant. | regulatory requirements in `docs/requirements/sys/` |
| Documentation | Every document that must change, including the VDD or package manifest if a release is affected. | Table 4-1 |
| Released units | Whether delivered units need rework, re-flash or recall; unit serials `CWHT-A-NNN`. | `docs/vv/adp/` |

A field with no impact is written "None" with a one-line justification; blank is not accepted.

### 5.4 Requirements volatility (SWE-200)

The metric is defined once, in `docs/process/02-requirements-and-traceability.md` §10.4, and computed by one script into one file: `tools/traceability.py --volatility --from <baseline tag> [--to <ref>]` (planned option, due PDR) reads the requirement files at the two git refs, classifies every difference by the change classes of 02 §10.2, and appends the record `MSR-02` to `docs/plan/measurements.json` (Table 4-1 row 45); `tools/measurements.py` mirrors it to `TPM-012` in `docs/plan/tpm.json` (07 §11.1). Counting rule: V = (A + M + R) / N_start, where A is requirements added, M requirements with at least one Class I change (a requirement counts once; TBR closures are counted and also reported as their own line), R requirements retired, and N_start the count at the previous baseline; reported per level (L1, L2, software modules) and per review interval, with a cumulative value from `baseline/srr`. Thresholds (07 §11.2, MSR-02): 10 % yellow, 20 % red; red opens an RFA at the next review and a risk per `docs/process/06-risk-and-decision-analysis.md`. The CSA (§6 item 10) copies the latest `MSR-02` value; `tools/csa.py` does not compute volatility.

## 6. Configuration status accounting (SE HB §6.5.1.2.4, SWE-083)

`docs/process/configuration-status.md` is the CSA report. It is generated by `tools/csa.py` (class B, TV due PDR, §13). Until the tool is accredited, Claude writes the same sections by hand from the same sources before every life-cycle review and after every baseline, release, waiver or CR closure. Hand edits to the generated file are prohibited once the generator is accredited. Content, in order:

| # | Section | Content | Source |
|---|---|---|---|
| 1 | Header | Generation date, `HEAD` SHA, generator version, current effective baseline (tag plus list of merged CRs). | `git rev-parse`, this plan |
| 2 | CI status | One row per Table 4-1 CI: pathspec, class, current level (L0 to L3), current hash, last commit SHA and date, last CR, peer-review record link; plus the list of tracked files that match no row (must be empty). | Table 4-1, `git ls-files`, `git ls-tree`, `git log -1 -- <path>` |
| 3 | Baselines | Tag, tag object hash, tagged commit, date, decision memo link, signed (yes or no), `git tag -v` result for signed tags, `git ls-remote --tags origin` hash (pushed: yes or no). | `git for-each-ref refs/tags/baseline/*`, `git ls-remote` |
| 4 | CR register | Every CR: id, title, class, status (Closed (Rejected) shown as such), originator, dates (opened, dispositioned, closed), affected CIs and IDs, target release, merge SHA; Deferred CRs with their re-look trigger. Includes Withdrawn. | `docs/cm/cr/*.md` front matter |
| 5 | Editorial log | Commits carrying `Editorial:` that touch class-CR CIs after their CR-from event: SHA, path, reason; reviewer sampling result at the last review. | `git log --format=%(trailers)` |
| 6 | Log-class change log | Commits since the previous baseline touching Log and Record CIs: SHA, first line, `Refs:`. | `git log` |
| 7 | Release register | Firmware: version, tag, source commit S, artifacts commit A, ELF and UF2 SHA-256, VDD link, units flashed, delta configuration audit link (post-SAR). Hardware: release ID, tag, `SHA256SUMS` and `SHA256SUMS.normalized` links, vendor records with their SHA-256, receipt inspection report link and result. | `firmware/releases/`, `hardware/releases/`, `docs/vv/reports/` |
| 8 | Audit register | FCA, PCA and delta audits: date, auditor, result, open discrepancies (NCR or RID IDs). | `docs/reviews/SAR/configuration-audit.md`, `firmware/releases/*/configuration-audit.md` |
| 9 | Tool accreditation | Tool, locked version, class, TV record, accreditation status (Accredited, Expired, Not required, Not yet validated), purposes. | `tools/toolchain.lock.md`, `docs/cm/tool-validation/` |
| 10 | Metrics | Requirements volatility (§5.4: the latest `MSR-02` record copied from `docs/plan/measurements.json`); open CR count and age; CR cycle time; count of commits lacking mandatory trailers. | `docs/plan/measurements.json`; derived |
| 11 | Deviations from this plan | Any departure (a tag left unsigned after the signing key is configured, an unpushed tag at a review, a hand-edited generated file, a merge without recorded approval) with date, RFA raised, closure. | `docs/cm/deviations.md`, copied in |
| 12 | Waivers | Every product waiver: id (`CR-NNN` or `<memo path>#W<n>`), requirement or target waived (REQ id, SWE-219 or SWE-220 with module id), rationale, approving memo or CR, releases affected, status (Active or Closed with the date the waiver stopped applying). | decision memos, CR files |
| 13 | Open items | Open TBRs by target review; liens from decision memos. | requirements files, decision memos |

The CSA is an entrance product of every life-cycle review; at SAR it evidences NPR 7123.1D App. G Table G-11 entrance item 3, sub-item 8 (baselined as-built hardware and software documentation).

## 7. Configuration verification and audits (SE HB §6.5.1.2 "Conduct configuration audits", SE HB App. B, SWE-084)

### 7.1 Functional Configuration Audit (at SAR, before the PCA)

Performed by an independent reviewer agent; result recorded in the FCA section of `docs/reviews/SAR/configuration-audit.md`; every failed item becomes an NCR (product) or RID-SAR (record). The FCA verifies that the as-built product has met, by test results, the requirements of the functional and allocated baselines plus approved changes (SE HB App. B definition).

| ID | Check | Evidence | Pass criterion |
|---|---|---|---|
| FCA-01 | Every requirement in `baseline/cdr` plus Closed CRs has status Verified or Closed, or is dispositioned by an approved CR or product waiver, or has an open NCR with owner disposition. | requirements files, traceability report, CSA item 12 | No requirement in Draft or Active without a CR, waiver or NCR. |
| FCA-02 | Every TC cited as verification evidence has status Passed and a report `docs/vv/reports/<TC-ID>-rN.md` (charter §6). For type HostUnit, Emulation, Bench or OnAir the report names the release tested in `firmware_version` (or, for a hardware-only run, `n/a` with the unit serial and baseline). For type Simulation or Inspection, including Analysis-method cases, the report names the baseline tag in `requirements_baseline` and lists the deck or input it ran on with its hash in `artifacts`. | test cases, reports | 100 % of cited TCs. |
| FCA-03 | For each HostUnit, Emulation, Bench or OnAir report: `source_commit` equals `git rev-parse release/FW-vX.Y.Z^{commit}` (the source commit S) and the SHA part of `firmware_version` is its prefix, and `firmware_elf_sha256` equals the ELF line of `firmware/releases/vX.Y.Z/SHA256SUMS`. | `git rev-parse`, report front matter, `SHA256SUMS` | Both equal. |
| FCA-04 | Test procedures executed equal the baselined version: `procedure_blob` in the report equals `git rev-parse <procedure_commit>:docs/test_cases/<module>/test_cases.json` and equals the blob of the same file in the baseline named by `requirements_baseline` (`git ls-tree <baseline tag> -- docs/test_cases/<module>/test_cases.json`). | `git rev-parse`, `git ls-tree`, report front matter | Hashes equal, or a CR explains the difference. |
| FCA-05 | Every Closed CR since `baseline/cdr` has its verification section complete with evidence links. | CR files | 100 %. |
| FCA-06 | Every NCR is dispositioned; "use-as-is" NCRs are approved by the owner and cited by the acceptance criteria. | NCR files | 100 %. |
| FCA-07 | Traceability report shows zero orphan requirements, zero unverified requirements, zero test cases without requirements. | `tools/traceability.py` output | Report clean. |
| FCA-08 | Safety-critical components of 07 §14.1: SWE-219 as tailored in the RMM (07 §9.5, §9.6: independently reviewed decision tables and independence-pair tests, with stable-toolchain region coverage MSR-13 as the credit measure and pinned-nightly branch and condition coverage MSR-14 as the labelled non-credit measure) and cyclomatic complexity ≤ 15 (SWE-220) evidenced for the released firmware. | `docs/vv/reports/TC-SW-COV-001-r<N>.md` with its MC/DC tables and `INSP-NNN` signature; complexity report | Evidence complete and targets met; any SWE-219 shortfall (SWE-219 note; 01 section 8.6) or SWE-220 exceedance waived with rationale by the owner as a numbered waiver `W<n>` in the CDR, TRR or SAR decision memo (07 §9.6 item 4, §14.3; the SAR decision memo for the accepted release), entered in CSA item 12 and listed in the VDD §7 waivers table. |
| FCA-09 | All TBRs closed (charter §7). | requirements files | Zero TBR. |
| FCA-10 | Requirements volatility and CR metrics reported in the SAR package. | CSA item 10 | Present. |

### 7.2 Physical Configuration Audit (at SAR, after the FCA)

Document-side checks by the independent reviewer agent; hands-on checks by the owner, guided by Claude, with photos attached. Result in the PCA section of `docs/reviews/SAR/configuration-audit.md`; failures become NCRs. The PCA verifies that the as-built configuration matches the product baseline plus approved changes.

| ID | Check | Method | Pass criterion |
|---|---|---|---|
| PCA-01 | The fabrication and assembly package `hardware/releases/HW-MB-rev<X>-<n>/` regenerates from its release tag: run `tools/kicad_export/pcbway_package.sh` at `release/HW-MB-rev<X>-<n>` with the locked `kicad-cli` into a scratch directory, normalize with `tools/normalize_fab.py` (§8.2) and compare with `SHA256SUMS.normalized`; confirm the committed upload zip with `shasum -a 256 -c SHA256SUMS`. | package script, `tools/normalize_fab.py`, `shasum` | Normalized hashes equal for every generated file and the raw check passes; any difference explained by a Closed CR and a `-<n+1>` package. |
| PCA-02 | PCBWay order confirmation references the same package (order number, file name, quantity, stack-up, finish, assembly side); the DigiKey order lines equal the hand-assembly list. | `vendor/order-confirmation.pdf`, `vendor/digikey-order-confirmation.pdf` in the release directory | Matches manifest. |
| PCA-03 | Assembled board: revision silkscreen equals `HW-MB-rev<X>`; every line of the assembly BOM and of the hand-assembly list (charter §12, SI-031) of the `-<n>` package the unit was built from (named in its `as-built.md`) visually confirmed (marking or package) on at least one unit; polarised parts oriented per assembly drawing. | Owner photo inspection against `assembly-drawing.pdf`, `cwht-MB-rev<X>-bom.csv` and `cwht-MB-rev<X>-hand-assembly.csv` | Zero unresolved discrepancies. |
| PCA-04 | Enclosure: critical dimensions (PCB pocket, connector cut-outs, antenna bore, lid fit) measured against the drawing tolerances in `hardware/releases/ME-ENC-rev<X>-<n>/drawing.pdf`. | Owner measurement with calipers; PCB fit check | Within tolerance. |
| PCA-05 | Firmware image on each delivered unit matches the VDD: `picotool info -a` shows program name `cwht` and version `vX.Y.Z+<short S>`; `picotool verify firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf` reports a match; the unit's `as-built.md` holds the §8.3 step 2 line. | Owner runs picotool in BOOTSEL mode | Match on every unit. PCA-05 records the installed-release line only (the unit's `as-built.md` line of §8.3 step 2, confirmed by the picotool output); it changes no requirement status. The Verified to Closed move of each `REQ-SW-*` whose closing case is HostUnit or Emulation and whose credited report names this release is made in the commit that records the signed SAR decision memo (01 section 8.4 row 5; charter §9; `docs/process/04-verification-and-validation.md` §5.3), after the FCA and PCA are complete. For a post-SAR delivery the delta configuration audit (§8.4) records the installed-release line of the new release in the same way, with `Refs: FW-vX.Y.Z`. |
| PCA-06 | Release image reproducibility at the source commit S: `git switch --detach release/FW-vX.Y.Z`, then `tools/release.sh --rebuild-check X.Y.Z` (build, CRC-32 trailer, UF2 conversion, hashes; §8.1 steps 3 to 6), which reads the expected hashes from `git show <A>:firmware/releases/vX.Y.Z/SHA256SUMS` (A from the tag message), then `git switch main`. | release script at S | Every hash equal; if not, NCR against the toolchain lock. |
| PCA-07 | VDD complete per `docs/templates/version-description.md`; the `Cargo.lock` blob hash and `rustos` commit in the VDD equal those at S. | file inspection, `git ls-tree` | Complete and equal. |
| PCA-08 | `tools/toolchain.lock.md` at S lists every tool used to build and verify the release, each with an Accredited TV record. | lock file, TV records | 100 %. |
| PCA-09 | Every unit has an acceptance data package with `as-built.md`: PCB release package and batch, enclosure release, firmware version and hash, ATP report list, recipient, date. | `docs/vv/adp/CWHT-A-NNN/` | 100 %. |
| PCA-10 | Delivery records for operations and maintenance exist (SWE-077): operations handbook (row 47), VDD, this plan, open NCR list, hand-over pack (§8.3 step 4). | as-built baseline list | Present. |

### 7.3 Configuration control before testing (SWE-187)

Any test whose result is intended as verification evidence runs on configuration-controlled inputs, as the credit rules of `docs/process/04-verification-and-validation.md` require:

1. HostUnit, Emulation, Bench and OnAir runs use a tagged release: the source commit S of `release/FW-vX.Y.Z-rcN` (candidate) or `release/FW-vX.Y.Z`, each with a VDD. The report front matter (`docs/templates/verification-report.md`) records the release (`firmware_version`), S (`source_commit`), the firmware ELF SHA-256 (`firmware_elf_sha256`), the emulator or test-harness tool versions from `tools/toolchain.lock.md` (`harness_versions`), the toolchain lock commit (`toolchain_lock`), and the commit at which the procedure was read (`procedure_commit`) with the blob hash of `test_cases.json` at that commit (`procedure_blob`). Keys that do not apply to a run carry `n/a`, as the template states.
2. Simulation and Inspection runs, including Analysis-method cases, record the baseline tag (`requirements_baseline`) and the hash of every deck or input file (`artifacts`), so that each run is reproducible from committed content.
3. Support software used for testing (emulator, mocks, scripts, checkers) is in Table 4-1 row 25 or 28 or is pinned in the lock.
4. Before the run-for-record series authorized by TRR, and before each series authorized by a delta TRR, Claude writes the test configuration record `docs/reviews/TRR/test-configuration-record.md` (charter §5) or `docs/reviews/TRR-Dn/test-configuration-record.md`: release tag, S, image hashes, unit serial and its `-<n>` hardware package, enclosure release, instrument identities and firmware versions, toolchain lock commit, and the baseline tag of the procedures.

A commit that is not tagged produces developer evidence only and cannot close a requirement.

### 7.4 Interim configuration checks

At SRR, PDR, CDR, TRR and every `TRR-Dn` the independent reviewer performs the record-side checks only: tags present, annotated and pushed (signed and verified once the key is configured), CSA current, CR trailer compliance, waiver register (CSA item 12) consistent with the decision memos, and every path of `git ls-files` at the review commit matching exactly one Table 4-1 row (CSA item 2; by hand until `tools/csa.py` is accredited). Findings the owner adopts become RIDs (01 section 10.1).

## 8. Storage, handling, release, delivery and maintenance (SWE-085, SWE-077, SWE-194, SWE-196)

### 8.1 Firmware release procedure

Executed by Claude on branch `rel/FW-vX.Y.Z` cut from `main`; the owner acts at steps 9 and 12. Three commits are distinguished: the source commit S (built, embedded, tagged), the artifacts commit A (release directory and VDD only) and the post-tag record commit.

1. Preconditions (SWE-194, all three parts, checked on the head of `rel/FW-vX.Y.Z`):
   - (a) Requirements: every `REQ-SW-*` allocated to this release (listed in VDD §6) is Verified or Closed, or dispositioned by an approved CR (deferred to a named later release, or waived), shown by `tools/traceability.py` run on `rel/FW-vX.Y.Z`. For a release candidate, which is never delivered (§8.3 step 3), the condition is that every allocated requirement is implemented and its HostUnit cases pass at developer level; credit comes from runs on the candidate itself.
   - (b) Changes: every CR targeted at this release is Closed, or the owner has re-dispositioned it out of this release (§5.1) before step 2.
   - (c) Defects: every NCR designated for resolution before this release is Closed.
   - (d) Gate: `tools/sw_gate.sh` exits 0 (07 §8.4, gates G1 to G6).
2. Source commit S: set `version = "X.Y.Z"` in the firmware crate `Cargo.toml`; commit `release(fw): prepare FW-vX.Y.Z` with `Refs:` to the CRs and NCRs included. S is `git rev-parse HEAD`.
3. Build at S from the repository root with `tools/release.sh X.Y.Z`. The script refuses to run unless `git diff --quiet HEAD` holds and `git status --porcelain` lists nothing outside `firmware/releases/vX.Y.Z/` and `firmware/releases/VDD-vX.Y.Z.md`, and unless `rustup show active-toolchain` run in `firmware/` prints the line recorded in `tools/toolchain.lock.md` §1. It sets `CWHT_BUILD_ID=vX.Y.Z+$(git rev-parse --short=7 HEAD)`, which `build.rs` embeds as the picotool program version, and runs `cargo build --release --locked --target thumbv8m.main-none-eabihf -p cwht-app` in `firmware/`, then the steps of item 4. The script prints every command it runs; VDD §4 copies them.
4. The script writes the deliverables to `firmware/releases/vX.Y.Z/`: (a) `cwht-FW-vX.Y.Z.elf`, copied from `firmware/target/thumbv8m.main-none-eabihf/release/cwht-app`, then completed by `tools/image_trailer.py write cwht-FW-vX.Y.Z.elf`, which computes the CRC-32 (IEEE 802.3 polynomial, as Python `zlib.crc32`) over the flash image bytes preceding the trailer and writes magic word and CRC into the 8-byte `.image_trailer` section that the rustos linker script reserves at the end of the image (07 CS-32, WP-SW-12; the firmware verifies the same value at boot before enabling any safety-critical output, SWE-134 f); the script prints the CRC value and VDD §2 records it; (b) `cwht-FW-vX.Y.Z.uf2` from the trailer-complete ELF (`picotool uf2 convert cwht-FW-vX.Y.Z.elf cwht-FW-vX.Y.Z.uf2 --family rp2350-arm-s`); (c) `firmware.map`; (d) `picotool-info.txt` (`picotool info -a cwht-FW-vX.Y.Z.elf`); (e) `SHA256SUMS` (`shasum -a 256 *.elf *.uf2 *.map picotool-info.txt > SHA256SUMS`, run inside the release directory). Because the trailer lives in a linker-reserved section, `picotool load` and `picotool verify` on the ELF (§8.3, PCA-05) carry and check it. Files under 5 MB are committed directly; the ELF, UF2 and map are well under this (a `rustos` blinky ELF is 132 kB, its UF2 8 kB). If any release file exceeds 5 MB the owner decides on git LFS (OQ-CM-006).
5. The script writes the skeleton of `firmware/releases/VDD-vX.Y.Z.md` from `docs/templates/version-description.md` (identification with `commit: <S>`, file inventory with hashes and the CRC value, build commands, environment settings); Claude completes VDD sections 1 to 8.
6. Reproducibility check at S: `tools/release.sh --rebuild-check X.Y.Z` confirms `HEAD` equals S, runs `cargo clean`, repeats steps 3 and 4 into a scratch directory outside the repository and compares every hash with `SHA256SUMS` (07 §13). A mismatch is an NCR against the toolchain lock and blocks the release. PCA-06 (§7.2) re-runs the same command at SAR.
7. Artifacts commit A: commit only `firmware/releases/vX.Y.Z/` and `firmware/releases/VDD-vX.Y.Z.md`, message `release(fw): artifacts FW-vX.Y.Z`, trailer `Refs: FW-vX.Y.Z`. `tools/release.sh --check-artifacts X.Y.Z` prints `git diff --name-only <S> HEAD` and fails if it lists any other path, so A cannot change what S built.
8. The independent reviewer checks the VDD and the release directory at A against the template checklist; the result is written in step 11.
9. The owner approves the release (for a candidate: approves it for test). Claude merges `rel/FW-vX.Y.Z` into `main` with `--no-ff` (`merge(FW-vX.Y.Z): release`).
10. Tag S: `git tag -a release/FW-vX.Y.Z <S> -m "cwht firmware vX.Y.Z; source <S>; artifacts <A>; VDD firmware/releases/VDD-vX.Y.Z.md"` (`-s` once signing is configured, §4.4); verify as in §4.4 step 5; `git push origin main --follow-tags` (S is reachable from `main` after the merge); confirm with `git ls-remote --tags origin release/FW-vX.Y.Z`.
11. Post-tag record: write VDD §9 once (reviewer result from step 8, owner approval transcription with date and source, verification output and `ls-remote` hash from step 10, the artifacts commit A) and commit on `main` as `release(fw): record approval and tag verification FW-vX.Y.Z` with `Refs: FW-vX.Y.Z`; update the CSA (item 7); push.
12. Flash and deliver (§8.3).

Release candidates follow the same twelve steps with version `X.Y.Z-rcN`, tag `release/FW-vX.Y.Z-rcN`, directory `firmware/releases/vX.Y.Z-rcN/` and VDD `firmware/releases/VDD-vX.Y.Z-rcN.md`; the owner's approval at step 9 is an approval to test, not to deliver. Candidate directories are kept, never pruned, so that credit runs stay reproducible.

### 8.2 Hardware release procedure (PCBWay fabrication, assembly and CNC)

Executed by Claude after the CDR decision memo authorises procurement (charter §3); the owner uploads and orders.

1. Preconditions: `baseline/cdr` tagged; ERC and DRC clean with the locked `kicad-cli` (`kicad-cli sch erc`, `kicad-cli pcb drc`), reports saved; all CDR Major RIDs closed; `tools/kicad_export/pcbway_package.sh`, `tools/normalize_fab.py`, `tools/scad2step.py` and the redaction check (§10.3) Accredited (§13).
2. PCB package: `tools/kicad_export/pcbway_package.sh` writes `hardware/releases/HW-MB-rev<X>-<n>/` using exactly the kicad-cli 10.0.6 commands verified in `docs/research/pcbway-export-and-vendor-questions.md` and its wrapper outline F12, which are the only permitted export commands: F3 (Gerber RS-274X with X2 attributes off: `pcb export gerbers -l "F.Cu,In1.Cu,In2.Cu,B.Cu,F.Mask,B.Mask,F.Silkscreen,B.Silkscreen,F.Paste,B.Paste,Edge.Cuts" --no-x2 --no-netlist --no-protel-ext --use-drill-file-origin --subtract-soldermask --check-zones --precision 6`; PCBWay rejects X2, F5), F6 (Excellon drill: `pcb export drill --format excellon --drill-origin plot --excellon-units mm --excellon-zeros-format decimal --excellon-oval-format route --excellon-separate-th --generate-map --map-format pdf --generate-report`), F7 (pick and place: `pcb export pos --format csv --units mm --use-drill-file-origin --side both --smd-only --exclude-dnp`; never `--exclude-fp-th`, which drops the Pico module, and never `--bottom-negate-x`) and F9 (assembly BOM: `sch export bom` with the PCBWay column order of F9 and the DNP to DNS post-processing). The script fails on any `Invalid layer name` warning (F2) and when the file counts differ from F12 (11 Gerbers, 1 job file, 2 drill files). Package contents: `gerbers/`, `cwht-MB-rev<X>-cpl.csv`, `cwht-MB-rev<X>-bom.csv` (surface-mount parts PCBWay assembles), `cwht-MB-rev<X>-hand-assembly.csv` (parts the owner solders after delivery per charter §12 and SI-031: through-hole parts and modules with exposed pads such as the Pico 2, 18650 holders, jacks, encoder and any RF module; same columns plus orientation note; the two lists together equal the design BOM in `hardware/bom/`, checked at step 4), `assembly-drawing.pdf` (both sides, polarity marks, hand-assembled parts outlined), `cwht-MB-rev<X>.step`, `erc-report.json`, `drc-report.json`, `stackup-and-finish.md`, `manifest.md` (source tag and commit, `kicad-cli` version, the exact export commands, file list), the zip actually uploaded (`cwht-MB-rev<X>-<n>.zip`), `SHA256SUMS` (raw SHA-256 of every file above including the zip: the identity of what was uploaded) and `SHA256SUMS.normalized` (SHA-256 of every generated file except the zip after `tools/normalize_fab.py`; the comparison basis for PCA-01 and for the kicad-cli known-answer test).
3. Enclosure package `hardware/releases/ME-ENC-rev<X>-<n>/`: CSG export with OpenSCAD 2021.01 (`/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD -o cwht-ENC-rev<X>.csg hardware/enclosure/<file>.scad`), then STEP export with `/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd tools/scad2step.py` (the script of `docs/research/enclosure-cnc-and-openscad-pipeline.md` step 3: one valid solid, no BSpline faces, STEP volume within 0.5 % of the STL mesh volume, ADR-008). OpenSCAD 2021.01 cannot write STEP (verified 2026-09-25: `-o cube.step` is rejected for its suffix and no file is written). Contents: `cwht-ENC-rev<X>.csg`, `cwht-ENC-rev<X>.step`, `drawing.pdf` (dimensioned, tolerances, material 6061-T6 or as specified in the ME requirements, finish, thread specs), `manifest.md`, the upload zip, `SHA256SUMS` and `SHA256SUMS.normalized`.
4. The independent reviewer checks each package against the CDR data (assembly BOM plus hand-assembly list equal the design BOM line for line, designator count against the schematic, drill count against the drill report, STEP bounding box against the ME requirement).
5. Commit each package on `main` (`hw(release): HW-MB-rev<X>-<n>`, `Refs: HW-MB-rev<X>-<n>`) and tag that commit `release/HW-MB-rev<X>-<n>` and `release/ME-ENC-rev<X>-<n>` (annotated; signed once configured, §4.4) before anything is uploaded; update the CSA; push with `--follow-tags`.
6. The owner uploads exactly the tagged zip files and places the PCBWay order (fabrication, assembly, CNC) and the DigiKey order for the hand-assembly parts (charter §3: CDR approval authorises both). The content is at L3 from the upload.
7. Vendor records go in the package's `vendor/` subfolder, outside `SHA256SUMS`: `order-confirmation.pdf` (PCBWay), `digikey-order-confirmation.pdf`, `dfm-feedback.md`, and the PCBWay test report when it arrives, each redacted of payment and address details (§10.3). Each is added by a Log commit with `Refs: HW-MB-rev<X>-<n>` (or the ME-ENC identifier), never edited afterwards, and its SHA-256 is entered in the CSA release register. A DFM comment that changes the design is a CR (§5.1) and a new package per §4.3.
8. Receipt: on delivery the owner performs receipt inspection (quantity, visual, PCBWay test report, photos) recorded in `docs/vv/reports/receipt-inspection-<n>.md` (`n` = vendor delivery number; `04-verification-and-validation.md` §11.2 stage 0, `01-lifecycle-and-reviews.md` §7.3); the report is linked from the CSA release register and from each unit's `as-built.md`, not from the tagged `manifest.md`; discrepancies become NCRs.

**Fabrication-file normalization (`tools/normalize_fab.py`, class B, TV due PDR with kicad-cli).** kicad-cli 10.0.6 writes the export time into its outputs, so byte hashes of two exports of the same board never match. Verified 2026-09-25 by the CM author on the KiCad template `RaspberryPi-HAT.kicad_pcb`: two exports 3 s apart differed only in the lines and fields below, and after removing them every file (11 Gerber layers, 2 drill files, 2 drill maps, the job file, the drill report, the CPL and the STEP) hashed identically. The tool applies exactly these rules and nothing else:

| File type | Normalization |
|---|---|
| Gerber `*.gbr` | Delete lines matching `^%TF\.CreationDate,.*`, `^G04 #@! TF\.CreationDate,.*` and `^G04 Created by KiCad .* date .*` |
| Excellon `*.drl` | Delete lines matching `^; DRILL file .* date .*` and `^; #@! TF\.CreationDate,.*` |
| Gerber job `*.gbrjob` | Replace the value of the `"CreationDate"` member with `"normalized"` |
| Drill report `*.rpt` | Delete lines matching `^Created on .*` |
| STEP `*.step`, `*.stp` | Replace the time-stamp argument of `FILE_NAME(` with `'normalized'` |
| PDF | Replace the digits of `/CreationDate (D:...)` and `/ModDate (D:...)` with zeros of the same length |
| CSV (CPL, BOM) | None (the CPL contains no date; verified) |
| Zip | Not normalized: the raw hash is the upload identity; the members are extracted and normalized one by one |

### 8.3 Flashing, handling and delivery of units

1. Each physical radio receives the next unit serial `CWHT-A-NNN` at receipt inspection; Claude creates `docs/vv/adp/CWHT-A-NNN/as-built.md` (package layout per `docs/vv/README.md`) with: serial, PCB release package (`HW-MB-rev<X>-<n>`) and batch or serial mark, enclosure release, firmware version and hash, ATP reports, receipt inspection report, recipient, date, open NCRs affecting the unit.
2. Flashing (owner): BOOTSEL mode, then `picotool load -u -x -t elf firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf` (or copy the UF2 to the mass-storage volume). Verify: `picotool verify firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf` after re-entering BOOTSEL; `picotool info -a` output pasted into `as-built.md`. The same day Claude appends to `as-built.md` the line `Installed release: vX.Y.Z+<short S>; picotool verify match; YYYY-MM-DD` (the version string copied from the `picotool info -a` output, the date of flashing), which `tools/traceability.py` reads (04 §5.2, rule 7.3.4) and PCA-05 checks.
3. Only released images (`release/FW-*` without `-rc`) are flashed on units handed to others (SI-019). Release candidates are flashed only on the owner's bench unit.
4. Hand-over pack per unit: printed or PDF operations handbook, VDD, open NCR list, and the anomaly contact rule of §8.4. The recipient's name and call sign are recorded in `as-built.md`; postal addresses are not stored in the repository.

### 8.4 Maintenance and retirement (SWE-195, SWE-196)

**Maintenance.** Post-SAR changes follow this plan: anomaly reports become NCRs; fixes are CRs; firmware fixes are PATCH releases through §8.1 with VDDs; a hardware fix is a new board revision letter through a CR and a CDR delta review decided by the owner.

**Anomaly contact rule** (in every hand-over pack): a recipient reports any anomaly, with the unit serial and the firmware version string (`picotool info -a` or the version shown by the radio), to the owner through the owner's own contact channel, which is not recorded in the repository. The owner, or Claude from the owner's report, files `NCR-NNN` in the same session.

**Delta configuration audit (SWE-084, SWE-194).** Every post-SAR release delivered to a unit gets a delta configuration audit by an independent reviewer agent before the owner flashes a unit handed to others: FCA-01 to FCA-03 and FCA-05 to FCA-07 for the requirements and CRs the release changes, plus PCA-05 to PCA-08, recorded at `firmware/releases/vX.Y.Z/configuration-audit.md` (Table 4-1 row 36, append-only) and entered in the CSA audit register.

**Retirement archive (SWE-196).** Records and tools to archive: the whole repository with all tags (`git bundle create <archive>/cwht-<date>.bundle --all`), which carries the release directories, `tools/toolchain.lock.md`, the TV records and their fixtures; plus the tool installers of `tools/toolchain.lock.md` §7 with their SHA-256. Claude assembles the archive directory `/Users/robinonsay/rust/cwht-archive/<gate>/` (bundle, installers or bundle tarballs, `SHA256SUMS`) at SAR and at project closeout; the owner copies it to a location outside the machine (OQ-CM-007), and the SAR baseline record names every archived file with its SHA-256. Installers that the vendor no longer serves (LTspice serves only its current macOS package) are archived as a tarball of the installed application. Access procedure: `git clone <bundle>` or clone the remote; reinstall tools from the archived installers at the versions in the lock.

## 9. Tool validation and accreditation (SWE-136, SWE-070; SWE-081 note on tools)

SWE-070 requires validated and accredited models, simulations and analysis tools for qualification; on cwht that is met by the class B validation of §9.1 and the procedure of §9.2 (LTspice, the emulator, the Python checkers and every other evidence-generating tool).

### 9.1 Scope and classes

| Class | Definition | Validation required | Tools (full list and versions in `tools/toolchain.lock.md`) |
|---|---|---|---|
| A: product-generating | Output becomes part of a release or of a design CI. | Known-answer test plus reproducibility check; TV record before first use for the record. | `rustc`/`cargo` (firmware image), `tools/release.sh` with `tools/image_trailer.py`, `picotool` (UF2 conversion, load), `kicad-cli` exports with `tools/kicad_export/pcbway_package.sh`, OpenSCAD 2021.01 (CSG), FreeCAD 1.1.3 `freecadcmd` with `tools/scad2step.py` (STEP). |
| B: evidence-generating | Output is cited as verification, inspection, audit or review evidence but does not enter the product. | Known-answer test with a seeded fault; TV record before first cited use. | LTspice through the CrossOver wrapper (Analysis); `kicad-cli` ERC and DRC (Inspection); `cargo test`, `clippy`, `cargo-llvm-cov` with llvm-tools, `cargo-nextest`, `cargo-audit`, `cargo-deny`, `cargo-geiger`, `cargo-binutils`, `rust-code-analysis-cli` with `tools/complexity_gate.py`, `tools/unsafe_audit.py`, `tools/sw_gate.sh` (HostUnit and static analysis); the date-pinned `nightly-2026-08-24` toolchain (MSR-14, non-credit measure only); `picotool verify` and `info` (PCA-05); the RP2350 emulator (Emulation); the venv Python with `jsonschema`; `tools/validate_docs.py`, `tools/traceability.py`, `tools/render_rmm.py`, `tools/render_compliance.py`, `tools/render_risk.py`, `tools/render_tpm.py`, `tools/review_trend.py`, `tools/measurements.py`, `tools/csa.py`, `tools/check_commit_msg.py`, the redaction check, `tools/normalize_fab.py`; `tools/slides/render_deck.py` with the Chromium headless shell (its PNGs are the record of the presented review, charter §4 item 2); `git` (object hashes, `git fsck`, tags cited in baseline records, FCA-03, FCA-04, PCA-07); `shasum` (`SHA256SUMS`); instrument firmware and host software for Bench evidence (tinySA Ultra firmware, sigrok-pico capture firmware, `sigrok-cli`). |
| C: informational | Output supports work but is never cited as evidence. | None; version recorded only. | `pdftotext` and `tools/refs/*` (corpus conversion), Ollama and Claude Context (search), Docker (container host; class B if it ever hosts the emulator), `cargo-generate`, `rustfmt`, Node.js and npm, the Asciidoctor.js converter packages and reveal.js (the HTML deck is regenerated; the PNGs are the record). |

### 9.2 Procedure

1. Claude creates `docs/cm/tool-validation/TV-NNN-<tool>.md` with: tool name, exact version string and the command that produced it, install source with installer URL and SHA-256 (lock §7), class, purposes (each purpose is one line and is what accreditation covers), known-answer test description, fixture paths under `tools/tests/fixtures/<tool>/` (the single fixture root; inputs and expected outputs committed), run command, pass criteria, result with date, commit SHA tested and output excerpt, reproducibility result (run twice, identical output hash, normalized per §8.2 where the tool writes time stamps) for class A, limitations, re-validation triggers.
2. The known-answer tests are those of the table below; `tools/toolchain.lock.md` §1.1 records each run with its date and the commit tested.
3. The independent reviewer checks the TV record and the fixture; the owner records the accreditation decision in the TV file ("Accredited for purposes 1 to n at version v") and the tool is entered as Accredited in `tools/toolchain.lock.md`.
4. Re-validation triggers: any version change of the tool, of the OS major version, or of a fixture; a defect found in the tool (also an NCR per SWE-201, which covers tool defects); expiry at each new baseline for class A tools (re-run the known-answer test and append the result; no new TV number unless the version changed).
5. Lock changes follow one rule (Table 4-1 row 27): after SRR, a version change of an Accredited tool is a CR (Class I if the tool can change a released image, e.g. `rustc`, linker, `picotool`) plus a new TV record; adding a tool row, changing a class C tool, changing a tool not yet Accredited, or re-observing with no version change is a Log commit with `Refs:` until that tool's first TV record.

| Tool | Known-answer test (pass criterion) |
|---|---|
| `rustc`/`cargo` | Build `tools/tests/fixtures/rust/` (a fixed crate for `thumbv8m.main-none-eabihf`) twice after `cargo clean` and compare ELF hashes; a test crate with one deliberately failing test makes `cargo test` exit non-zero. |
| `kicad-cli` (TV due PDR, with `tools/normalize_fab.py`) | ERC on `tools/tests/fixtures/kicad/seeded.kicad_sch` reports exactly the seeded violation (one unconnected pin) and ERC on `clean.kicad_sch` reports none; DRC on `seeded.kicad_pcb` reports exactly the seeded clearance violation and DRC on `clean.kicad_pcb` none; the §8.2 step 2 exports of `clean.kicad_pcb` match the stored `SHA256SUMS.normalized`; PTH and NPTH hit counts in the drill report equal the stored counts; the CPL and BOM CSVs equal the stored CSVs line for line; the STEP bounding box equals the stored box within 0.01 mm. |
| `tools/kicad_export/pcbway_package.sh` (TV due CDR) | On the fixture board of `docs/research/pcbway-export-and-vendor-questions.md` F12: 12 Gerber-set names, 7 PTH and 5 NPTH hits, 6 CPL rows, 7 BOM rows, designator cross-check `MATCH`; a misspelt layer name makes the script fail. |
| `tools/normalize_fab.py` (TV due PDR) | Two exports of the fixture board taken at different times normalize to identical hashes; a one-byte change to a copper layer outside the date lines changes the normalized hash. |
| LTspice (TV due PDR) | `tools/tests/fixtures/ltspice/rc-lowpass.asc` run as `/Applications/LTspice.app/Contents/SharedSupport/ltspice/bin/wine --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' -b <deck>` (the headless form of `docs/research/ltspice-batch-macos.md` F3; the app launcher `Contents/MacOS/LTspice -b` exits 0 with no output, F2, and is not permitted) reproduces the stored -3 dB frequency within 1 %; the `.log` first line names the version; a deck with a seeded error makes the wrapper exit 1 (F6). Precondition: `CaptureAnalytics=false` in the bottle's `LTspice.ini` (F4, SI-027). |
| OpenSCAD + FreeCAD with `tools/scad2step.py` (TV due PDR) | CSG export of `tools/tests/fixtures/openscad/cube.scad` with OpenSCAD 2021.01, then `freecadcmd tools/scad2step.py` gives a STEP with one valid solid and the stored bounding box. |
| `picotool` (TV due CDR) | `uf2 convert` of the stored fixture ELF equals the stored UF2 SHA-256; `info` reads back the program name; `verify` detects a one-byte change to an image (07 §8.3). |
| `tools/release.sh`, `tools/image_trailer.py` (TV before the first release candidate, §13) | The trailer written into the fixture ELF equals the stored CRC-32; `--rebuild-check` on the fixture reports identical ELF, UF2, map and info hashes; `--check-artifacts` fails when a source file is in the artifacts commit. |
| `shasum` (TV due CDR) | `shasum -a 256 -c SHA256SUMS` passes on `tools/tests/fixtures/shasum/` and fails on a temporary copy with one byte changed. |
| `git` (TV due SRR) | `git hash-object tools/tests/fixtures/git/hello.txt` equals the stored blob hash; in a temporary repository created by the test, committing the fixture gives the same hash from `git ls-tree HEAD -- hello.txt`, `git fsck --full` exits 0, and after one byte of that loose object is overwritten `git fsck --full` exits non-zero naming the object. |
| Python venv + `jsonschema` (TV due SRR) | `jsonschema` rejects `tools/tests/fixtures/schema/invalid-requirement.json` with the expected error path and accepts the valid one. |
| `tools/traceability.py`, `tools/validate_docs.py` (TV due SRR) | The fixture-only test classes pass: `.venv/bin/python -m unittest discover -s tools/tests -p 'test_traceability.py' -k ValidProjectTests -k InvalidProjectTests -k WordListTests`, the same for `test_validate_docs.py` with `-k ValidProjectTests -k InvalidProjectTests -k PeerReviewRecordTests`, and `-p 'test_tools.py'`: `valid_project` exits 0 with zero findings and `invalid_project` exits 1 with exactly the seeded codes. The `RepositoryTests` classes check repository content, not the tools, and are recorded separately as a repository check (lock §1.1). |
| `tools/render_rmm.py` (TV due SRR) | `-p 'test_render_rmm.py'` passes (03 §6.1 seeded faults). |
| `tools/render_compliance.py`, `tools/render_risk.py` (TV due SRR) | `--check` exits 0 on a valid fixture and the rendered Markdown equals the stored file; each seeded fault (fault list fixed in the TV record) exits non-zero; fixtures `tools/tests/fixtures/compliance/` and `tools/tests/fixtures/risk/`, modules `tools/tests/test_render_compliance.py` and `tools/tests/test_render_risk.py`, written before the SRR readiness declaration. |
| `tools/review_trend.py` (TV due SRR) | `-p 'test_review_trend.py'` passes: the hand-computed counts of 01 §11 for `docs/templates/rfa-rid-log.example.json`. |
| `tools/slides/render_deck.py` with the Chromium headless shell (TV due SRR) | `-p 'test_render_deck.py'` passes: the fixture deck renders exactly four non-blank PNGs of the requested size. |
| Instrument firmware and host software (TV due TRR, 04 §6) | Logic capture: a capture by `sigrok-cli` through the sigrok-pico firmware of a reference square wave of stored period (a PWM output of a second Pico 2 running the fixture image in `tools/tests/fixtures/logic-capture/`) reproduces the stored period within one sample period. tinySA Ultra: the instrument's internal calibration output measured through the attenuator reproduces the stored frequency and the stored level within the instrument's ±2 dB level accuracy. |
| Emulator (TV due PDR) | A stored scenario reproduces a stored trace. |

### 9.3 Toolchain lock

`tools/toolchain.lock.md` records every tool with the version observed on the build machine, the command used to observe it, the date, class, TV record, accreditation status and installer source (§7 of the lock). It is regenerated by re-running the listed commands (a later tool `tools/toolchain_lock.py` may automate this; its output format is the current file). The venv is reproduced with `python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt`, and `tools/requirements.txt` pins with `==` every package of lock §2 (AL-4, an SRR readiness prerequisite). The firmware crate pins its compiler with `firmware/rust-toolchain.toml` (content and the expected `rustup show active-toolchain` line are in lock §1), so that `cargo` in `firmware/` cannot select another toolchain.

## 10. Technical data management (SE HB §6.6, SE-21)

### 10.1 Data inventory and control

| Data class | Examples | Where | Who may change | Controlled by |
|---|---|---|---|---|
| Configuration items | Table 4-1 | repo | per Table 4-1 | this plan §4 to §7 |
| Records (append-only) | stakeholder inputs, TS, ADR, CR, NCR, test reports, RFA/RID logs, decision memos, TV, unit as-built records, audits, receipt inspections | repo | Claude appends; owner text transcribed by Claude | §4.2 Record class |
| Derived data | rendered figures, traceability report, CSA, `.stl`, `target/`, LTspice `.raw`/`.log` outside `docs/vv/`, KiCad backups | repo (figures, reports, CSA) or gitignored (the rest) | regenerated by tools; never hand-edited | regenerate from source at each review |
| Vendor data | order confirmations, DFM feedback, PCBWay test reports, DigiKey invoices | `hardware/releases/<ID>/vendor/`, redacted | Claude files, owner supplies | §8.2 step 7, §10.3 |
| Reference corpus | NASA handbook and NPR conversions, regulatory text | `docs/references/md`, `txt` | Claude via `tools/refs/*` | §10.5 |
| Personal data | recipients' names and call signs, owner's licence details | unit as-built records; never addresses, payment data or credentials | owner consent | §10.3 |
| Session and search data | Claude Context index, Ollama models, Milvus store | outside repo | n/a | not managed; rebuildable; never a record |

### 10.2 Naming, format and exchange conventions

| Rule | Statement |
|---|---|
| File names | kebab-case, ASCII, no spaces; ID-bearing files start with the ID: `CR-012-pa-bias-resistor.md`, `TV-003-kicad-cli.md`, `VDD-v1.0.0.md`, `docs/vv/adp/CWHT-A-001/as-built.md`. Dates in file names or fields are ISO 8601 (`2026-09-25`). |
| Authoritative formats | Markdown (documents), JSON validated by the row 9 schemas (requirements, tests, registers), KiCad native files (design), `.asc` plus CSV expected results (simulation), `.scad` plus `.csg` and `.step` (mechanical), Rust source with `Cargo.lock` (firmware), PNG or SVG (renders), PDF (vendor documents, drawings). JSON is UTF-8, two-space indent, trailing newline. |
| Exchange formats to vendors | RS-274X Gerber with X2 attributes off (attributes carried as `G04 #@!` comments; PCBWay rejects X2, `docs/research/pcbway-export-and-vendor-questions.md` F5), Excellon drill (metric, decimal, separate PTH and NPTH, F6), CSV BOM and CPL in PCBWay column order (F7, F9), STEP AP214 from FreeCAD for CNC (§8.2 step 3), PDF drawings. |
| Metadata | Every Markdown product starts with a status line (Status, Owner, Author, applicable baseline) as this plan does; JSON registers carry `module` and per-item `status`. Every figure file name encodes its source: `<source-file-stem>-<view>.png`. |
| Cross-references | Always by ID, never by page or section number alone; repo paths are given relative to the repository root. |
| Units and numbers | SI units with a space between value and unit; tolerances stated explicitly; no unit-less requirements (charter §7). |

### 10.3 Access, rights and protection

- Access: the owner and Claude sessions have write access to the working copy; Claude (main session) pushes to `origin` from this machine using the owner's SSH identity, and no other account has push rights. The repository is public (SI-025), so anyone may read it. Friends receiving units get the hand-over pack (§8.3) and the repository URL.
- Public release and distribution limits: all repository content is for public release. Export-controlled data, data under a non-disclosure agreement and proprietary vendor data (for example PCBWay or DigiKey material not published for redistribution, or a datasheet marked confidential) are never committed. When Claude is unsure whether an item may be published, the owner decides before the commit, and the decision is recorded in the commit body.
- Rights: MIT licence in `LICENSE` at the repository root, stated in `README.md` (ADR-017, SI-025, charter §12 reuse row). Third-party content: NASA documents are US Government works reproduced for reference; KiCad, LTspice, PCBWay templates and DigiKey data retain their owners' terms and are not redistributed beyond the repository's needs.
- Protection: no credentials, API keys, payment details, postal addresses or account numbers are ever committed. Vendor documents are redacted before filing. The redaction check (`tools/redaction_check.py`, class B, a `pre-commit` hook that scans staged files for card-number, account-number, e-mail-address and postal-address patterns) is accredited before the CDR procurement release (§13); until then Claude inspects each vendor file before committing.
- Integrity: `SHA256SUMS` (and `SHA256SUMS.normalized` for fabrication packages) in every release directory; `git fsck --full` run and its result recorded in each baseline record.

### 10.4 Storage, backup and remote

- Primary store: the local repository. Backup and publication: the remote `origin` = `git@github.com:robinonsay/cwht.git` (charter §8; public under MIT per SI-025). Observed 2026-09-25: `git ls-remote origin refs/heads/main` returns the local `main` commit; the observation is refreshed at each SRR-type readiness declaration and at every baseline (baseline record §8a). Claude pushes `main` with `--follow-tags` after every merge to `main` and after every tag, and pushes every open `wip/`, `rid/`, `cr/` or `rel/` branch at the end of each session. A push that fails (no network) is retried in the same session; if it still fails at a baseline or release, Claude creates `git bundle create /Users/robinonsay/rust/cwht-backup/cwht-<date>.bundle --all`, records the bundle's SHA-256 in the CSA deviations table and pushes at the next opportunity. Owner action (OQ-CM-001): enable GitHub branch protection on `main` (block force pushes and deletion) and tag protection rules for `baseline/*` and `release/*`.
- Long-term archive: at SAR and at project closeout, the archive of §8.4 (bundle and tool installers) is copied by the owner to a location outside the machine (OQ-CM-007, recorded in the SAR baseline record).
- Retention: indefinite for baselines, releases, records and CRs; derived data is not retained beyond the review that used it; the reference corpus is retained with the repository. NPR 1441.1 retention schedules (cited by NPR 7123.1D §3.2.15.2 e and SE HB §6.6) are Not applicable as an institution; the intent is met by indefinite retention.

### 10.5 Reference corpus handling

Source PDFs are gitignored (`docs/references/*.pdf`) and the `.gitignore` comment points to `docs/references/README.md`, which lists every source URL and the conversion script per document so the corpus is reproducible (OQ-CM-008 closed). Conversions are regenerated only through `tools/refs/*` and committed as Log-class changes with `Refs:` to the tool script; hand edits to converted files are prohibited so that citations remain traceable to the source.

### 10.6 Access and search

Claude and every agent find technical data in this order (charter §11 rule 1, hard rule): (1) the Claude Context vector search (`mcp__claude-context__search_code`, path `/Users/robinonsay/rust/cwht`), always first; its index is rebuildable and is never a record; (2) the README index files (`README.md`, `docs/process/README.md`, `docs/requirements/README.md`, `docs/vv/README.md`, `docs/references/README.md`) and the traceability report and CSA as generated indexes of requirements, tests, CIs, waivers and releases; (3) only after a vector search, to pin the exact line a hit pointed at: ID-first file names (§10.2), so that `git ls-files '*CR-012*'` finds an item by ID, and `git grep -n <ID>` for every occurrence of an ID. If the search tool is unavailable, the agent says so in its return before any manual search. Other readers of the public repository (the owner, friends) use items 2 and 3 directly.

At SAR, the technical data package updated with all test results (NPR 7123.1D App. G Table G-11 entrance item 3, sub-item 6) is the as-built baseline record `docs/reviews/SAR/baseline-record.md`, which lists every credited report in `docs/vv/reports/` with its hash, together with each unit's acceptance data package `docs/vv/adp/CWHT-A-NNN/`.

## 11. Mapping of NPR 7150.2D Chapter 6 records to repository artifacts

NPR 7150.2D §6.1 lists typical software engineering products a to y. Their cwht equivalents, with Table 4-1 rows:

| §6.1 item | Record | cwht artifact | Row |
|---|---|---|---|
| a | Software Development / Management Plan | `docs/process/07-software-engineering-plan.md` | 2 |
| b | Software Schedule | `docs/plan/schedule.md`: milestone list keyed to gates (charter §12: tailored) | 2 |
| c | Software Cost Estimate | `docs/plan/cost-estimate.md`: labor-free cost model (charter §12: tailored) | 2 |
| d | Software Configuration Management Plan | This document | 2 |
| e | Software Change Reports | `docs/cm/cr/CR-NNN-*.md`; CSA item 4 register | 31, 35 |
| f | Software Test Plans | `docs/vv/plan.md` | 16 |
| g | Software Test Procedures | `docs/test_cases/<module>/test_cases.json` (procedure arrays) | 17 |
| h | Software Test Reports | `docs/vv/reports/` | 19 |
| i | Software Version Description Reports | `firmware/releases/VDD-vX.Y.Z.md` | 36 |
| j | Software Maintenance Plan | §8.4 of this plan and 07 §20 | 2 |
| k | Software Assurance Plan(s) | Independent-reviewer checklists and 07 §15 (charter §2) | 2, 53 |
| l | Software Safety Plan | `docs/safety/hazard-analysis.md` software section and SWE-134 provisions in 07 §14 | 15, 2 |
| m | Software Requirements Specification | `docs/requirements/sw/` | 8 |
| n | Software Data Dictionary | Register maps and message definitions in `docs/icd/`; type definitions in firmware source | 10, 25 |
| o | Software and Interface Design Description (Architectural Design) | `docs/design/architecture.md` (software section), `docs/icd/` | 11, 10 |
| p | Software Design Description | `docs/design/software-design.md` and `docs/design/sw/` per 07 | 11 |
| q | Software User's Manual | `docs/ops/operations-handbook.md` | 47 |
| r | Records of Continuous Risk Management for Software | `docs/risk/register.json` (software risks tagged) | 14 |
| s | Software Measurement Analysis Results | CSA item 10, `docs/plan/measurements.json`, `docs/plan/tpm.json`, coverage and complexity reports in `docs/vv/reports/` | 35, 45, 34, 19 |
| t | Record of Software Engineering Trade-off Criteria and Assessments | `docs/decisions/trade-studies/TS-NNN-*.md`, ADRs | 12, 13 |
| u | Software Acceptance Criteria and Conditions | Acceptance criteria in `docs/vv/plan.md` and in each TC's `acceptance_criteria` | 16, 17 |
| v | Software Status Reports | Review packages `docs/reviews/<REVIEW>/package.md` and the CSA | 33, 35 |
| w | Programmer's / Developer's Manual | `README.md`, build and flash instructions in 07 and each VDD | 40, 36 |
| x | Software Reuse Report | Reused software is reported in VDD §3 (the `rustos` row and one row per third-party crate, with the SWE-203 advisory review result) and in the third-party register of 07 §17.1 (SWE-027 as tailored, SWE-211); the `rustos` pin is row 26 | 26, 36, 2 |
| y | Software Model and Simulation Data and Documentation, including V&V and credibility | LTspice decks and checkers, emulator scenarios, their TV records | 24, 28, 30 |

## 12. Programmatic and organisational interfaces (SE HB App. M)

| Interface | CM relationship |
|---|---|
| Requirements Management (SE-17, charter §7) | Produces CRs for requirement changes after their CR-from event; consumes the effective baseline. Volatility metric per §5.4. |
| Interface Management (SE-18) | ICD changes are CRs from PDR; external-interface changes are Class I. |
| Technical Risk Management | Risk register is Log class; CR impact includes risk (§5.3); risks about CM (unprotected remote branches, an unaccredited tool used for the record, an unpinned venv) are entered by Claude as `RSK-NNN`. |
| Safety | Hazard analysis and the RF exposure evaluation are CR-controlled from PDR and every change is Class I; the CR Safety field names the 07 §14.1 modules affected. |
| Technical Assessment and reviews (charter §3 and §4) | Baselines are set only at gate completion; the CSA and baseline record are entrance products; CM record checks are part of every review (§7.4). |
| Product Verification and Validation (charter §9) | Tests run only on configuration-controlled inputs (§7.3); NCRs may spawn CRs; FCA consumes test reports; PCA-05 records the installed-release line, and host-verified software moves from Verified to Closed in the commit that records the signed SAR decision memo (PCA-05 pass criterion, §7.2). |
| Product Implementation and Transition | Hardware release packages and firmware releases (§8) are the transition products; receipt inspection records are Records. |
| Operations | The operations handbook (row 47) is controlled from SAR; operator-procedure changes are Class I. |
| Vendors (PCBWay, DigiKey) | Catalog services under standard terms (charter §12). No CM flow-down. Vendor-driven changes enter through CRs; vendor documents are filed redacted in the package's `vendor/` folder. |
| Supplier flow-down (App. M topic) | Not applicable: no subcontracts. |

## 13. Deliverables and milestones (SE HB App. M)

This table is the single authoritative schedule of CM deliverables and TV records; `tools/toolchain.lock.md` §5 cites it. A tool used for the record before its gate still needs its TV record before that first cited use (§9.1).

| Gate | CM deliverables that must exist for the gate to be complete |
|---|---|
| SRR | This plan at L1 (independently reviewed) and, for ETA approval (SE-20, SE-21), approved by the owner in `docs/reviews/SRR/decision-memo.md`; this plan, `tools/toolchain.lock.md` and the three templates committed on `main` with `Refs: SRR` before the independent L1 record is filed, so that the record cites a `product_commit`; every tracked file matching a Table 4-1 row (§7.4); `tools/requirements.txt` pinned to lock §2 (AL-4); TV records, each reviewed and accredited, for: the venv Python with `jsonschema`, `tools/traceability.py`, `tools/validate_docs.py`, `tools/render_rmm.py`, `tools/render_compliance.py`, `tools/render_risk.py`, `tools/review_trend.py`, `tools/slides/render_deck.py` with the Chromium headless shell, and `git`; tags annotated and pushed to `origin` (signed once the key is configured, §4.4); first CSA issued; `docs/templates/change-request.md`, `version-description.md`, `baseline-record.md` present; `baseline/srr` tag and baseline record after the decision memo. |
| PDR | TV records for LTspice through the CrossOver wrapper (`tools/ltspice-batch.sh`), `kicad-cli` (ERC, DRC and exports) with `tools/normalize_fab.py`, OpenSCAD 2021.01 and FreeCAD 1.1.3 with `tools/scad2step.py`, the emulator, the Rust toolchain (`rustc`, `cargo`, `clippy`, `cargo-llvm-cov` with llvm-tools, `cargo-nextest`, and `nightly-2026-08-24` for the non-credit MSR-14 measure), `tools/render_tpm.py`, `tools/measurements.py`, `tools/csa.py` and `tools/check_commit_msg.py` (installed as the `commit-msg` hook); CR register in use; volatility metric reported; `baseline/pdr`. |
| CDR | TV records for `tools/release.sh` and `tools/image_trailer.py` before the first release candidate (`release/FW-v0.9.0-rc1`, 07 §3.1 FW-B2), `tools/sw_gate.sh`, `picotool`, `shasum`, `cargo-binutils`, `cargo-audit`, `cargo-deny`, `cargo-geiger`, `rust-code-analysis-cli` with `tools/complexity_gate.py`, `tools/unsafe_audit.py`, `tools/kicad_export/pcbway_package.sh`, and the redaction check before the procurement release; hardware release packages generated per §8.2 and reviewed; `baseline/cdr`; procurement authorised in the decision memo. |
| TRR | Release-candidate procedure (§8.1) exercised at least once with a VDD; TV records for the tinySA Ultra firmware, the sigrok-pico capture firmware and `sigrok-cli` (04 §6); test harness and emulator versions locked; test configuration record `docs/reviews/TRR/test-configuration-record.md` (§7.3 item 4; each delta TRR writes its own); CSA current. |
| SAR | Configuration audit record (FCA and PCA sections); VDD for the released firmware; unit as-built records; release tags; `baseline/sar`; archive bundle and tool installers (§8.4) with their SHA-256 in the SAR baseline record. |

## 14. Open questions for the owner

IDs follow the charter §6 scheme `OQ-<AREA>-NNN` with area `CM`. Closed questions keep their row with the closure fact.

| ID | Question | Needed by | Default if undecided |
|---|---|---|---|
| OQ-CM-001 | Enable GitHub branch protection on `main` (block force pushes and deletion) and tag protection for `baseline/*` and `release/*` on `github.com/robinonsay/cwht` (§4.5, §10.4). The remote exists and `main` equals `origin/main` (observed 2026-09-25 with `git ls-remote`); only the protection rules are open. | SRR | Rules enforced by this plan and the reviewer's `reflog` check only; risk `RSK-NNN` entered by Claude. |
| OQ-CM-002 | Configure the SSH tag-signing key per §4.4. Charter §8 makes signing optional until this is done. | Owner's choice; recommended before `baseline/pdr` | Tags stay annotated and unsigned; CSA records `signed: no`; no deviation. |
| OQ-CM-003 | Licence for the repository. | SRR | Closed 2026-09-25: `LICENSE` (MIT) exists at the repository root and `README.md` states it (SI-025, ADR-017). |
| OQ-CM-004 | Install and lock a headless enclosure CAD path. | PDR | Closed 2026-09-25: OpenSCAD 2021.01 at `/Applications/OpenSCAD-2021.01.app` for CSG plus FreeCAD 1.1.3 `freecadcmd` for STEP (SI-032, ADR-008), both recorded in `tools/toolchain.lock.md`; TV records due PDR (§13). |
| OQ-CM-005 | `rustos` pinning method: keep the path dependency with the commit recorded in the lock and VDD (this plan's default), or convert to a git dependency or submodule so `Cargo.lock` pins it. | PDR (ADR) | Path dependency plus recorded commit. |
| OQ-CM-006 | Storage for release binaries above 5 MB (git LFS or external store). | CDR | Commit directly; all expected files are far below the limit. |
| OQ-CM-007 | Off-machine archive location for the SAR and closeout archives (§8.4, §10.4). | SAR | Owner's choice; recorded in the SAR baseline record. |
| OQ-CM-008 | Add `docs/references/README.md` listing corpus sources (referenced by `.gitignore`). | SRR | Closed 2026-09-25: the file exists and lists source URL and conversion script per document. |

### 14.1 Cross-document alignment items (for the integrating session, not the owner)

Found on 2026-09-25 by comparing this plan with the process documents written in parallel. This plan is authoritative for CM identifiers not in charter §6 (`FW-vX.Y.Z`, `HW-MB-rev<X>-<n>`, `ME-ENC-rev<X>-<n>`, `release/*` and `baseline/*` tags) and for CM record locations not fixed by charter §5; it is subordinate to charter §5 and §6. The other document is corrected by its author, or this plan is, before SRR.

| # | Other document | Statement there | This plan | Resolution |
|---|---|---|---|---|
| AL-1 | `docs/process/06-risk-and-decision-analysis.md` (trigger table), `docs/risk/register.json` mitigation artifacts | Tool validation records at `docs/vv/tool-validation/<tool>.md` | `docs/cm/tool-validation/TV-NNN-<tool>.md` (§9.2) | Done 2026-09-25: 06 §10 and the register artifacts use the TV-NNN path. |
| AL-2 | `docs/process/01-lifecycle-and-reviews.md`, `docs/process/07-software-engineering-plan.md`, `docs/templates/peer-review-checklist-test.md` CK-TEST-A4 | Firmware release tag `fw/v<version>`; release files `firmware/releases/cwht-<version>.uf2` | `release/FW-vX.Y.Z` and `firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.*` (§4.3, §8.1) | Done 2026-09-25. |
| AL-3 | `docs/process/08-agent-briefing.md` | Templates `docs/templates/vdd.md`; V&V plan named `06-verification-and-validation.md` | `docs/templates/version-description.md`; V&V plan is `04-verification-and-validation.md` | Done. |
| AL-4 | `tools/requirements.txt` | Nine unpinned package names while the venv holds 36 packages (lock §2) | §9.3 and the lock require exact pins reproducing the venv | SRR readiness prerequisite: Claude pins all 36 packages with `==` exactly as in lock §2 (for example from `.venv/bin/pip freeze`), in the same session that creates the venv TV record, and the commit carries `Refs:` with that TV id. |
| AL-5 | `docs/process/04-verification-and-validation.md`, `docs/vv/README.md` | Unit serial `CWHT-A-NNN`, acceptance data package `docs/vv/adp/<unit-serial>/` | Adopted (row 38, §8.3) | None; consistent. |
| AL-6 | `docs/process/01-lifecycle-and-reviews.md` | Audit record `docs/reviews/SAR/configuration-audit.md` | Adopted (row 39, §7) | None; consistent. |
| AL-7 | Charter §5 (b8214ca), 01 §13 | The filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md` with `id: INSP-NNN` is the single peer-review record; no `peer-reviews/` folder | Adopted (§4.1 L1, baseline-record template §2) | Resolved (verified 2026-09-25 by the integrating session): 01, 05, 07, 08, the SEMP and the templates `review-package.md`, `decision-memo.md`, `baseline-record.md` and the four peer-review checklists name only the single record; 03 section 6.5 item X4 is resolved; `tools/validate_docs.py` rejects a `peer-reviews/` folder. |
| AL-8 | `docs/process/07-software-engineering-plan.md` §13 | VDD toolchain row names `llvm-tools`, `cargo-llvm-cov`, `rust-code-analysis-cli`, `cargo-geiger`, `cargo-audit`, `cargo-deny`, `cargo-nextest` | Lock §1 records each with its observed version or "not installed"; VDD template §4 lists the same rows | None. The lock is updated when 07's FW-B0 install step runs, as a Log commit (§9.2 step 5: new rows and tools not yet Accredited). |
| AL-9 | `docs/templates/rfa-rid-log.schema.json` | `verification.record` pattern required `peer-reviews/INSP-NNN.md` | Record path of §4.1 L1 | Done 2026-09-25 by another session: the pattern is `^docs/reviews/(SRR\|PDR\|CDR\|TRR\|SAR\|TRR-D[1-9][0-9]?)/checklists/[a-z0-9][a-z0-9._-]*\.md$`; `.venv/bin/python -m unittest discover -s tools/tests` re-run after this revision passes (lock §1.1). |
| AL-10 | `docs/process/02-requirements-and-traceability.md` §10.3 item 4 and 02 AL-8 | Risk, software classification and RMM, and ConOps impacts written into other rows until 05 §5.3 gains them | §5.3 now has the rows Risk, Software classification and tailoring, Operations and ConOps, and Cybersecurity; the CR template §4 has the same rows | 02 author replaces item 4's interim mapping with a pointer to these rows and closes 02 AL-8. |
| AL-11 | 04 §5.2 (HostUnit credit row) and §5.3 (status semantics); `tools/traceability.py` rule 7.3.4 | The PCA-05 installed-release line is a condition for `Verified` | Charter §9 (b8214ca): HostUnit- or Emulation-verified software requirements are `Verified` on a credited report and `Closed` after PCA-05; PCA-05 here follows the charter | Resolved (verified 2026-09-25): 04 sections 5.2 and 5.3 make the PCA-05 line and the signed SAR memo conditions of `Closed`; PCA-05 (§7.2) records the installed-release line only; the planned tool check is `CLOSED_NOT_INSTALLED` (04 section 7.4, due CDR). |
| AL-12 | `docs/plan/semp.md` §5.14 | Baselines listed without the customizations | §1 customizations 1 and 2; the single CR trigger (CR-from event); product waivers | SEMP author mirrors the two customizations (charter §1) and cites §2 for waivers. |
| AL-13 | 07 §8.3 | Static analysis tools accredited by PDR | §13 accredits `clippy` with the Rust toolchain at PDR and `cargo-audit`, `cargo-deny`, `cargo-geiger`, `rust-code-analysis-cli` with `tools/complexity_gate.py` at CDR, their first cited use (07 §3.1 CDR row) | 07 author aligns 07 §8.3 with §13; the owner may move the dates earlier by CR. |
| AL-14 | Repository root (untracked) | `result.json` (a Bambu Studio CLI result) and `reveal.js/` (a reveal.js copy written outside any deck folder) | Match no Table 4-1 row | Never committed. Prevention done 2026-09-25: `tools/slides/render_deck.py` exits 2, writing nothing, for a deck outside `docs/reviews/<REVIEW>/slides/` (known-answer test `tools/tests/test_render_deck.py` class `LocationGuard`), so no new stray `reveal.js/` copy can be made. Removal open: the owner confirms SEMP OQ-SE-007 and Claude deletes the two untracked root items before the SRR readiness declaration. |

### 14.2 Charter issues raised by this plan (carried in the SRR package)

| # | Charter section | Issue | Proposal |
|---|---|---|---|
| CI-5-1 | §8 | The charter names the fourth baseline as-built; SE HB §6.5.1.2.2 names it as-deployed and places it at ORR. | No change unless the owner prefers the SE HB name; §1 records the customization. |
| CI-5-2 | §6 | No identifiers for releases (`FW-vX.Y.Z`, `HW-MB-rev<X>-<n>`, `ME-ENC-rev<X>-<n>`) or for `release/*` and `baseline/*` tags. | Add them to §6, citing 05 §4.3. |
| CI-5-3 | §5 | The hardware release packages row names only `hardware/releases/HW-MB-rev<X>-<n>/`; the CNC package needs `hardware/releases/ME-ENC-rev<X>-<n>/`, and vendor records now sit in each package's `vendor/` folder. | Extend the row with both. |
| CI-5-4 | §6 | No identifier for product waivers; this plan uses the `CR-NNN` or `<memo path>#W<n>`. | Add `WVR-NNN` if the owner wants a register identifier; otherwise no change. |
| CI-5-5 | §5 | The test configuration record is named for TRR only; this plan also writes one per delta TRR in `docs/reviews/TRR-Dn/`. | State it in the §5 row. |
| CI-5-6 | §5 | `docs/design/sw/<module>.md` (per-module software design) is not in the document tree (carried from 07 §22). | Add it to the software architecture and design row. |

## 15. Plan maintenance

This plan is re-evaluated at every life-cycle review and on any of the SE HB App. M trigger events: vendor change, part obsolescence, tool change, change in the owner's resources (§3), change of product scope (e.g. rev B start). Changes after SRR are CRs (Table 4-1 row 2).

## 16. Compliance summary

| Requirement | Where satisfied |
|---|---|
| SE-20 (NPR 7123.1D §3.2.15.1: ETA-approved CM process) | ETA approval: the owner's approval of this plan in `docs/reviews/SRR/decision-memo.md` (status line). Purposes of the SE-20 process, NPR 7123.1D §3.2.15.2 a to e: a §4.2; b §4.3, §4.4; c §5; d §4.5, §10.3; e §10.4. |
| SE-21 (NPR 7123.1D §3.2.16.1: ETA-approved technical data management process) | ETA approval: the same memo. Process: §10; SE HB §6.6.1.2.1 topics: control procedures §10.1, access and search §10.6, exchange formats §10.2, rights and distribution limits §10.3, storage and master lists §10.4 and Table 4-1. |
| SWE-079 (SCM plan: functions, responsibilities, authority) | This plan; §3 |
| SWE-080 (track and evaluate changes) | §5, §6 |
| SWE-081 (identify CIs and versions, including tools) | §4.2, §4.3, §9.3, VDD §4 environment settings |
| SWE-082 a, b, c (levels of control; who authorises; who changes) | §4.1, §3, §4.5 |
| SWE-083 (configuration status records) | §6 |
| SWE-084 (configuration audits) | §7; delta audits §8.4 |
| SWE-085 (storage, handling, delivery, release, maintenance) | §8 |
| SWE-045 (joint NASA/developer audits) | Not applicable: no NASA counterpart; recorded in the RMM. |
| SWE-042 (electronic access to modifiable source) | The repository itself; §10.3 |
| SWE-063 (version description per release) | §8.1, `docs/templates/version-description.md` |
| SWE-070 (validated and accredited models, simulations and analysis tools) | §9.1 class B, §9.2 |
| SWE-077 (deliver with as-built records) | §8.3, PCA-10 |
| SWE-136 (tool validation and accreditation) | §9 |
| SWE-187 (CM before testing) | §7.3 |
| SWE-194 (pre-delivery verification of requirements, changes, defects) | §8.1 step 1 (a), (b), (c); FCA-01, FCA-05, FCA-06; §8.4 delta audit |
| SWE-196 (records and tools archived for retirement) | §8.4, §10.4, lock §7 |
| SWE-200 (requirements volatility) | §5.4 |
| SWE-201 (tool defects tracked) | §9.2 step 4 |
| SWE-219, SWE-220 (MC/DC as tailored; complexity with waiver) | FCA-08, §2 product waiver, CSA item 12, VDD §3 and §7 |
| NPR 7123.1D App. G Table G-11 entrance item 3, sub-items 6 and 8 | Sub-item 6: §10.6 (SAR baseline record and ADPs); sub-item 8: §4.4 as-built baseline, §6, §7 |
| SE HB §6.5.1.2.3 change types (major, minor, waiver) | §2, §5 |
| SE HB §6.5.1.2.4 CSA content (including waivers) | §6 |
| SE HB App. M topics | §1 scope; §4 to §10 procedures per function; §3 roles and resources; §2 definitions; §12 interfaces; §13 deliverables; §12 flow-down (N/A) |
| NPR 7150.2D §6.1 records | §11 |
