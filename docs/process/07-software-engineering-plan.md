# cwht Software Development and Management Plan

**Status:** Draft for SRR (SWE-013 plan; re-approved at every gate). **Owner:** Robin (Project Manager, Decision Authority, Engineering Technical Authority, SMA Technical Authority). **Author:** Claude (software lead). **Expands:** charter section 10; also implements charter sections 2, 7, 8, 9, 11 and 12 for the firmware. **Aligned to:** charter at commit `b8214ca`. **Governing:** NPR 7150.2D at Class A rigor by owner election (`docs/process/03-software-classification-and-rmm.md`), with tailoring recorded row by row in `docs/process/rmm.json`; NPR 7150.2D Chapter 6 record content; NASA-HDBK-2203 (SWEHB Ver D) in `docs/references/md/swehb/`. Charter section 1 records 268 pages scraped with per-SWE completeness tracked by RSK-009; the directory holds 267 files, and the per-SWE page with its `# 7. Software Assurance` section is present for all 130 SWEs (checked 2026-09-25 by this plan's author with a directory count and a heading search; closure of RSK-009 in section 22). The SWEHB pages this plan uses are named where they are used: `5-08` (SDP/SMP minimum content, mapped in section 1.4), `5-16` (VDD minimum content, section 13), `5-17` and `5-18` (software assurance and software safety plan minimum content, section 15), `7-02` (classification and safety criticality), and the `# 7. Software Assurance` section of each `swe-NNN-*.md` page, which the software assurance reviewer applies to the product under review (section 15).

This document is the Software Development Plan and Software Management Plan: it holds NPR 7150.2D §6.1 items a, j, k, l and the u concept; items b, c, t and the u baseline are in the files named in section 1.3. It is also the Rust coding standard (SWE-061), the static analysis and test policy (SWE-135, SWE-062, SWE-186, SWE-189 to SWE-191), the peer review procedure (SWE-087 to SWE-089), the measurement plan (SWE-090, SWE-093, SWE-199, SWE-200), the software cybersecurity assessment (SWE-154, SWE-156, SWE-157, SWE-159, SWE-185, SWE-207, SWE-210), the third-party software register (SWE-027, SWE-033, SWE-203, SWE-211) and the version description content definition (SWE-063). Where this plan and `docs/process/rmm.json` disagree, the RMM row approved by the owner governs and this plan is corrected by `CR-NNN`. Where this plan and `docs/process/04-verification-and-validation.md` disagree on evidence, credit or nonconformance rules, that document governs.

Conventions: "shall" is used only in requirements files; this plan states what is done in the imperative. Paths are repository-relative. Software module identifiers are `SW-<SUB>` (for example `SW-KEYER`), requirement ids `REQ-SW-<SUB>-NNN`, verification cases `TC-SW-<SUB>-NNN`, sprints `SW-NN-<module>`, peer review records `INSP-NNN`, coding standard rules `CS-NN`, measurements `MSR-NN`, driver work packages `WP-SW-NN`. Acronyms and plan-specific terms are in Annex D.

---

## 1. Purpose, scope and software items

### 1.1 Scope

The software of cwht is the firmware of the RP2350 controller on the radio board: everything compiled into the flashed image plus the host-side tests, mocks, emulation scenarios and scripts that produce its evidence. There is no ground software, no network stack, no over-the-air update and no user-installable application. Firmware loading is by the RP2350 bootrom over USB (UF2 drag-and-drop or `picotool`).

### 1.2 Software items (configuration items, charter section 8)

| Item | Kind | Location | Depends on | Ships in image |
|---|---|---|---|---|
| `cwht-app` | Binary crate, `#![no_std]`, `#![no_main]`, target only; composition root: board take, driver construction, the main loop that calls the `SW-SCHED` dispatcher of `cwht-core`, safe-state entry. Holds no decision logic other than the board `take()` match of CS-11 (CS-38) | `firmware/cwht-app/` | `cwht-core`, `pico2`, `api` | yes |
| `cwht-core` | Library crate, `#![no_std]`, `#![forbid(unsafe_code)]`; all application logic behind `api` traits: keyer (straight and iambic), tuning and display logic, transmit sequencer with the keying envelope and ALC set-point units, safety manager with the thermal path and the configuration guard, audio limiter and sidetone generation, configuration store logic, power and thermal monitors, boot sequencing, and the scheduler dispatcher (`SW-SCHED`: task table, tick accounting, overrun detection, watchdog-kick decision) | `firmware/cwht-core/` | `api` | yes |
| `api` | rustos portable trait crate (host-compilable) | `/Users/robinonsay/rust/rustos/api/` (path dependency `../rustos/api`) | none | yes (traits only, zero-sized) |
| `pico2` | rustos RP2350 runtime and HAL: boot metadata, vector table, reset handler, linker script, drivers; the only crate permitted to contain `unsafe`; decisions of safety-critical drivers live in host-compilable functions (CS-38) | `/Users/robinonsay/rust/rustos/firmware/pico2/` (path dependency) | `api` | yes |
| `cwht-hal-mock` | Host-only library implementing the `api` traits with recorded, scriptable state and a mock clock (0.1 ms resolution, ADR-011) | `firmware/cwht-hal-mock/` | `api` | no (dev-dependency) |
| Emulation scenarios | Scenario definitions (timestamped stimuli and the expected event order) for the optional Emulation class; harness, vendoring form and file format fixed by the emulator ADR due at PDR (section 9.4) | `firmware/emu/` | the emulator selected by the PDR ADR (section 17.1) | no |
| Build and quality configuration | `firmware/Cargo.toml` (workspace, `[workspace.lints]`), `firmware/rust-toolchain.toml`, `firmware/.cargo/config.toml`, `firmware/.config/nextest.toml` (profile `ci`, JUnit output, section 8.4), `firmware/rustfmt.toml`, `firmware/clippy.toml`, `firmware/deny.toml` | `firmware/` | | no |
| Scripts | `tools/sw_gate.sh` (the gate, section 8.4), `tools/complexity_gate.py`, `tools/unsafe_audit.py`, `tools/measurements.py`, `tools/emu_run.sh` (emulation scenario runner: written by the software lead in FW-B0 as a stub that prints the `SKIP` line of section 8.4, completed once the PDR emulator ADR is Accepted), `tools/release.sh` with `tools/image_trailer.py` (section 13; `docs/process/05-configuration-and-data-management.md` section 8.1), `tools/traceability.py` (shared) | `tools/` | Python venv `.venv` | no |
| Records | `firmware/releases/VDD-vX.Y.Z.md` and `firmware/releases/vX.Y.Z/` (`cwht-FW-vX.Y.Z.elf`, `cwht-FW-vX.Y.Z.uf2`, `firmware.map`, `picotool-info.txt`, `SHA256SUMS`; layout of 05 section 8.1), `firmware/unsafe-audit.md`, `docs/sprints/SW-NN-<module>.md` and `docs/sprints/index.md`, the peer review records `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (one file per review: the filled checklist is the single record and carries `id: INSP-NNN` in its front matter, charter section 5; section 10.2), `docs/plan/measurements.json`, `docs/vv/reports/TC-SW-COV-001-r<N>.md` (05 Table 4-1 rows 19, 33, 36, 44 to 46) | as listed | | no |

`cwht-core` holds every decision, including the `SW-SCHED` dispatcher, and is the unit under test on the host. `cwht-app` (`#![no_main]`) and the MMIO, boot and vector-table code of `pico2` do not run on the host; they carry no decisions beyond the board `take()` match (CS-38) and are covered by the target-only disposition of section 9.5 (dev-board checks and Bench cases, with emulation event-order scenarios as supporting evidence). The split makes the charter's HostUnit evidence class (`docs/process/04-verification-and-validation.md` section 4) cover all decision logic, including every safety-critical decision.

### 1.3 Software records and deliverables (SWE-036; NPR 7150.2D §6.1)

| NPR 7150.2D 6.1 record | cwht artifact | Produced by | Gate where first required | Owner action on receipt |
|---|---|---|---|---|
| a. Software Development/Management Plan | this file | Claude | SRR | approve (decision memo) |
| b. Software schedule | `docs/plan/schedule.md` (milestones keyed to gates; tailored per charter section 12) | Claude | SRR | note |
| c. Software cost estimate | `docs/plan/cost-estimate.md` (labor-free model; SWE-015/151 tailored) | Claude | SRR | note |
| d. Software CM plan | `docs/process/05-configuration-and-data-management.md` | Claude | SRR | approve |
| e. Software change reports | `CR-NNN` records per the CM plan | Claude | after SRR | approve each CR (CCB) |
| f. Software test plan | `docs/vv/plan.md` software section | Claude | PDR | approve |
| g. Software test procedures | `docs/test_cases/sw-<sub>/test_cases.json` | test-author agent | CDR (`Active`) | note; disposition RIDs |
| h. Software test reports | `docs/vv/reports/<TC-ID>-r<N>.md`, including the coverage report `docs/vv/reports/TC-SW-COV-001-r<N>.md` and the regression report `docs/vv/reports/TC-SW-REG-001-r<N>.md` (04 sections 10.5 and 12) | Claude | TRR | witness Bench, approve results |
| i. Software version description | `firmware/releases/VDD-<version>.md` | Claude | TRR | approve release for test; approve accepted release at SAR |
| j. Software maintenance plan | section 20 of this file | Claude | SAR | approve |
| k. Software assurance plan | section 15 of this file | Claude | SRR | approve |
| l. Software safety plan | section 14 of this file plus `docs/safety/hazard-analysis.md` | Claude | SRR (preliminary) | approve |
| m. Software Requirements Specification | `docs/requirements/sw/requirements.json` (firmware-wide L2) and `docs/requirements/sw/sw-<sub>/requirements.json` (module files; L2 software module files in the charter's numbering, `docs/process/02-requirements-and-traceability.md` section 2.1) | author agent | PDR (baselined) | approve baseline |
| n. Software data dictionary | `docs/design/software-design.md` section "Data dictionary" (configuration record fields, event log record, keyer parameters) | author agent | CDR | note |
| o. Software and interface design description (architecture) | `docs/design/architecture.md` software section; `docs/icd/ICD-CTL-SW.md` (pin map, peripheral allocation, register-level use) | author agent | PDR | approve baseline |
| p. Software design description | `docs/design/software-design.md` | author agent | CDR | approve baseline |
| q. Software user's manual | `docs/ops/operations-handbook.md` (menus, keyer settings, flashing procedure, fault codes) | Claude | SAR | approve |
| r. Records of software risk management | `docs/risk/register.json` (`RSK-NNN` tagged `software`) | Claude | SRR | accept residual risk per gate |
| s. Software measurement analysis results | `docs/plan/measurements.json` plus the "Software status" section of each `docs/reviews/<REVIEW>/package.md` | Claude | PDR | note |
| t. Trade-off criteria and assessments (make/buy) | `docs/decisions/trade-studies/TS-NNN-*.md` (runtime and HAL make/buy); the emulator selection is the ADR due at PDR (ADR-011 section 3) | Claude | SRR | approve |
| u. Software acceptance criteria | section 18 of this file (concept) and `docs/vv/plan.md` "Acceptance" section (baselined) | Claude | SRR concept, PDR baseline | approve |
| v. Software status reports | "Software status" section of each review package; `docs/sprints/SW-NN-<module>.md` closure records | Claude | PDR | note |
| w. Programmer's/developer's manual | rustos `README.md`, `rustos/docs/tutorials/rp2350_baremetal/`, `cargo doc` output of the workspace, section 7 of this file | Claude | CDR | note |
| x. Software reuse report | section 17.1 (third-party software register) and the VDD "Reused components" section | Claude | SRR | note |
| y. Model and simulation data, including V&V and credibility | `firmware/emu/` scenarios and the emulator accreditation record `ACC-EMU-001` (adopted by the PDR emulator ADR as the emulator's TV record, credit scope summarized in `tools/toolchain.lock.md`; section 9.4) | Claude | PDR | approve accreditation |

### 1.4 SWEHB 5.08 minimum content mapped to this plan

NASA-HDBK-2203 topic 5.08 lists 25 minimum content items for a Software Development/Management Plan (`docs/references/md/swehb/5-08-sdp-smp-software-development-management-plan.md`, section 1). Each is satisfied here or in the named document:

| 5.08 item | Where |
|---|---|
| 1 Organizational structure and authorities | Section 2.1 (roles), charter section 2 |
| 2 Safety-critical determination and classification | Section 14.1; `docs/process/03-software-classification-and-rmm.md` sections 3 and 4 |
| 3 Tailored requirements mapping matrix | `docs/process/rmm.json`; mirror in section 22 |
| 4 Engineering environment (tools, test environment, standards) | Sections 7, 8, 9.1, 9.4; `tools/toolchain.lock.md` |
| 5 Work breakdown, products, size, schedule | Sections 1.2, 3.1, 3.2, 19; `docs/plan/schedule.md`; `docs/plan/cost-estimate.md` (tailored SWE-015/016) |
| 6 Management of quality characteristics | Sections 7, 8.2, 9.5, 11 |
| 7 Management of safety, security, privacy and other critical requirements | Section 14 (safety), section 16 (security), section 16.6 (privacy) |
| 8 Subcontractor management | Not applicable: no subcontractor (charter section 12) |
| 9 Verification methods, products, environments, records | Sections 9, 10; records in `docs/vv/reports/` and `docs/reviews/<REVIEW>/checklists/` |
| 10 Validation methods, products, environments, records | Section 18 item 9; `docs/process/04-verification-and-validation.md` section 7.2; `TC-VAL-*` reports |
| 11 Project involvement | Section 2.1 (owner insight, SWE-039) |
| 12 User involvement | Section 18 item 9 and section 3.2 FW-B1 (owner HSI verdict) |
| 13 Risk management | Section 21; `docs/process/06-risk-and-decision-analysis.md` |
| 14 Security policy | Section 16 |
| 15 Approvals, licensing, ownership | Sections 1.3 (owner action column), 17.1; repository `LICENSE` (MIT) |
| 16 Scheduling, tracking and reporting | Sections 3.3, 11.3, 23 |
| 17 Training | Section 2.2 (SWE-017 as tailored) |
| 18 Life cycle model, integration, delivery, maintenance | Sections 3, 9.1 (integration levels), 13, 20 |
| 19 Configuration management | `docs/process/05-configuration-and-data-management.md`; section 13 |
| 20 Document deliverables | Section 1.3 |
| 21 Peer review and inspection process | Section 10 and Annex A |
| 22 Early identification of design-driving test requirements | Section 3.1 (PDR row: keyer prototype and emulator characterization before design), section 9.4 (emulator ADR at PDR), section 14.2 (time budgets fixed at PDR) |
| 23 Software metrics | Section 11 |
| 24 Content of software documentation | Section 1.3 (artifact per record), section 13 (VDD content), section 5 (design content) |
| 25 COTS, GOTS, MOTS, reused and open-source approach | Section 17 |

---

## 2. Roles, independence and required reading

### 2.1 Roles (charter section 2; SEMP section 4.1)

| Role | Holder | Software responsibilities |
|---|---|---|
| Project manager, Decision Authority, Engineering TA, SMA TA, customer, CCB | Owner (Robin) | Approves this plan, the RMM tailoring, every CR, every release for test, the accepted release; confirms or raises NCR severity; witnesses Bench and OnAir runs; performs physical actions (flashing, cabling, keying). Insight per SWE-039: may audit any sprint record, gate log or agent transcript at any time. |
| Software lead | Claude (main session) | Writes this plan, briefs, integrates, runs `tools/sw_gate.sh`, maintains baselines, releases and VDDs, tracks actuals against plan (SWE-024), reports status, sets the record `verdict` and closes peer review records (section 10.2). Never reviews its own authored file. |
| Author agent | Independent invocation | Produces exactly one file per brief (source module, design section, requirement file, scenario). |
| Reviewer agent | Independent invocation, never the author of the file | Reviews one file against the checklist for its type (section 10); returns `APPROVED` or `NEEDS CHANGES` with `file:line` findings and severities; copies the checklist template into the record and fills it. |
| Test-author agent | Independent invocation, never the implementation author | Writes `TC-SW-*` cases and the host tests or scenarios that automate them, from the requirements and the design, before or in parallel with implementation (test as independent specification, IEEE 1012 intent). |
| Software assurance reviewer | Independent invocation, distinct from the file reviewer | Second review of every product the table of section 2.1.1 marks Yes, written into the same record (section 10.2); confirms NCR severity for every NCR touching firmware (`docs/process/04-verification-and-validation.md` section 10.3); verifies sprint acceptance criteria before closure (section 3.4 Phase 4). |

#### 2.1.1 When the software assurance review is required

This table is the single rule for dispatching the software assurance reviewer; every checklist header and Participants line cites it. Criticality is that of the component the product belongs to (section 14.1). "Yes" means the record's `assurance_verdict` must be `APPROVED` before the software lead sets the record `verdict` to `APPROVED` (section 10.2).

| Product type (checklist) | Safety-critical component | Mission-critical component | Neither |
|---|---|---|---|
| Software requirement files and CRs touching them (`peer-review-checklist-requirements.md` A to F): module files `docs/requirements/sw/sw-<sub>/requirements.json`; the firmware-wide file `docs/requirements/sw/requirements.json` is Yes as a whole because it carries safety-critical rows | Yes | Yes | No |
| Software plans (`peer-review-checklist-requirements.md` G): this plan (it is the software assurance plan and software safety plan, §6.1 items k and l), the software section of `docs/vv/plan.md`, `docs/process/03-software-classification-and-rmm.md` (SWE-205 determination) | Yes | Yes | Yes |
| Other process documents (`docs/process/0N-*.md` except 03 and this plan), ConOps, expectations, technology assessment | No | No | No |
| Design: software section of `docs/design/architecture.md` (Yes as a whole, it carries the safety-critical component list); module sections of `docs/design/software-design.md` or `docs/design/sw/<module>.md` (`peer-review-checklist-design.md`) | Yes | Yes | No |
| Code (`peer-review-checklist-code.md`) | Yes | Yes | No, except Yes for every file that contains `unsafe` |
| Test cases, test code, emulation scenarios, dev-board checks (`peer-review-checklist-test.md`) | Yes | Yes | No |
| NCR touching firmware (severity confirmation, 04 section 10.3) | Yes | Yes | Yes |
| MC/DC tables of `TC-SW-COV-001-r<N>` and the unsafe audit list at CDR and SAR | Yes | not applicable | not applicable |

Basis: SWEHB `swe-134-*.md` section 7.1 task 2 (source code satisfies items a to l "for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone") and task 5 (participate in reviews affecting safety-critical software products), and SWEHB `swe-205-*.md` section 7 task 1 (software contributions by action, inaction or incorrect action).

### 2.2 Required reading per role (SWE-017 as tailored: briefs replace training)

Every brief lists these files; an agent that has not been pointed at them is re-briefed, not corrected after the fact.

| Role | Required reading before starting |
|---|---|
| All agents | `docs/process/00-charter.md` sections 6, 7, 11; `docs/process/08-agent-briefing.md`; the checklist for the product type in `docs/templates/`; `docs/lessons-learned.md` entries tagged `software` |
| Author (Rust) | Section 7 of this file (coding standard); `rustos/README.md` ("The API: invariants at compile time"); the design section for the module; the `api` trait docs (`cargo doc`); the RP2350 ICD pages under `rustos/docs/icd/rp2350/` for any register touched; ADR-011 section 2 (target platform rules) |
| Author (requirements) | SE HB App. C checklists C.1 to C.4; `docs/requirements/schema.json`; section 14.2 of this file (SWE-134 flow-down) |
| Test author | `docs/process/04-verification-and-validation.md` sections 4, 5.2 and 8; `docs/test_cases/schema.json`; section 9 of this file; ADR-011 |
| Reviewer | The product-type checklist; the brief of the author (to know the acceptance criteria); section 10 of this file |
| Software assurance reviewer | Sections 2.1.1, 14 and 15 of this file; `docs/safety/hazard-analysis.md` and `docs/safety/hazards.json`; NPR 7150.2D §3.7 (corpus `npr-7150-2d/03-chapter3.md`); the `# 7. Software Assurance` section of the SWEHB page for each SWE the product implements (`docs/references/md/swehb/swe-NNN-*.md`, for example `swe-134-*.md` section 7.1 tasks 1 to 6); SWEHB topics `6-1` (design for safety checklist), `6-2` (general software safety requirements checklist), `8-01` (off-nominal testing) and `8-15` (SA tasking checklist tool) |

---

## 3. Software life cycle and build plan (SWE-013, SWE-037)

### 3.1 Alignment to the gates (charter section 3; `docs/process/01-lifecycle-and-reviews.md`)

| Phase and gate | Software work | Software products entering the gate (see `01-lifecycle-and-reviews.md` sections 4.6, 5.6, 6.6, 7.5, 8.6) | Build increment |
|---|---|---|---|
| Pre-A/A, **SRR** | This plan; classification and RMM; make/buy trade study (SWE-033); safety-critical determination input; software-related L1 requirements; toolchain proof: `firmware/` workspace builds for host and `thumbv8m.main-none-eabihf`, rustos blinky flashed on a bare Pico 2, `tools/sw_gate.sh` runs end to end, `tools/toolchain.lock.md` updated with the tool versions actually installed (section 8.1) | Plan (this file), RMM, TS, toolchain proof report `docs/vv/reports/TC-SW-TOOL-001-r1.md` (case `TC-SW-TOOL-001` in `docs/test_cases/sw-tool/test_cases.json`, test-only module `SW-TOOL` of `docs/process/04-verification-and-validation.md` section 1; `credit: false`) | **FW-B0 toolchain proof** |
| B, **PDR** | L2 `SW` requirements and the `sw-<sub>` module requirement files; software architecture (states, modes, components, interfaces, quality attributes); `ICD-CTL-SW`; SWE-134 provisions allocated to components; rustos driver work packages WP-SW-01 to WP-SW-07, WP-SW-09 and WP-SW-11 implemented with host mocks and dev-board checks (WP-SW-08, WP-SW-10 and WP-SW-12 follow in FW-B2); keyer prototype on the dev board with PWM sidetone for the owner's HSI evaluation of straight key and paddles (SI-018); the ACC-EMU-001 candidate emulator boots the blinky and reproduces its known answers KA-1 to KA-3 as input to the emulator ADR (`credit: false`) | Requirements (baselined), architecture, test plan section of `docs/vv/plan.md`, coding standard (section 7) and tool set (section 8) named with versions, coverage plan, emulator ADR | **FW-B1 drivers and keyer prototype** |
| C, **CDR** | Detailed design per module; `cwht-core` implemented and host-tested with coverage; `cwht-app` composition root; emulation event-order scenarios for every `OPS-NNN` (if an emulator is accepted); all `TC-SW-*` cases `Active`; first coverage report; complexity and unsafe audit; peer reviews of design and code to date | `docs/design/software-design.md`, test procedures, coverage report, static analysis results, VDD-0.9.0-rc1 (internal) | **FW-B2 core logic** |
| D during fabrication, **TRR** | Integration on the dev board (and on the emulator for event order); regression suite green on the tagged release; hazard-tracing tests executed (SWE-192); acceptance tests for loaded data (SWE-193); VDD for the run-for-record release; delta TRR for each new release | `release/FW-v0.9.x-rcN` tagged release candidate (identifiers per 05 section 4.3), VDD, HostUnit and Emulation reports, coverage report, regression report | **FW-B3 integration release** |
| D, **SAR** | Bench and OnAir verification on `CWHT-A-001`, including every timing requirement with the Pico-based logic capture; NCR fixes through CR and regression; final coverage; configuration audit (image hash equals VDD; PCA-05 installed-release line) | `release/FW-v1.0.0`, VDD, V&V report software section, configuration audit, handbook | **FW-B4 accepted release** |
| E/F | Anomalies from use become NCRs; maintenance releases follow section 20; Rev B formulation | NCRs, VDDs | maintenance |

### 3.2 Build increments and their exit criteria

| Increment | Content | Exit criterion (all must hold) |
|---|---|---|
| FW-B0 | Workspace skeleton (`cwht-app`, `cwht-core`, `cwht-hal-mock`, `firmware/emu/` placeholder), lints and rustfmt configured, `sw_gate.sh` with every tool of section 8 installed and versioned (including the pinned nightly with `miri` and `llvm-tools`, CS-03, and `rust-code-analysis-cli`), blinky on the cwht pin map flashed and observed on a bare Pico 2 | `tools/sw_gate.sh` exits 0 on the skeleton (G6 emulation step prints its `SKIP` line); `tools/toolchain.lock.md` lists every tool with version and sanity-check result; toolchain proof report filed |
| FW-B1 | rustos work packages of section 19 done to the `api` trait boundary with host mocks; keyer prototype (`SW-KEYER` state machines) host-tested; dev-board demonstration of straight key and iambic paddles with sidetone | Every WP row of section 19 marked done with its dev-board check report; owner records the HSI verdict on the keyer feel (dit/dah timing, weighting, iambic mode A/B) in `docs/reviews/PDR/decision-memo.md` |
| FW-B2 | All `cwht-core` modules per the software design; `cwht-app` composition; all `TC-SW-*` HostUnit tests implemented; emulation event-order scenarios for every `OPS-NNN` if an emulator is accepted; first coverage and complexity report | 100 percent of HostUnit cases pass twice in a row; coverage per section 9.5 targets or dispositioned; complexity limit met; unsafe audit signed; every module peer-reviewed with record `verdict: APPROVED` |
| FW-B3 | Release candidate `release/FW-v0.9.0-rc1`; regression suite; Emulation ordering scenarios run for the record (peripherals inside ACC-EMU-001 only); VDD | Gate exits 0 on the tagged commit; every HostUnit and Emulation case run for credit on the tag; VDD approved by the owner for test |
| FW-B4 | `release/FW-v1.0.0` after Bench and OnAir NCR closure | Every `REQ-SW-*` is `Verified` on the credited report of `release/FW-v1.0.0` and moves to `Closed` at SAR after the PCA-05 line of `docs/vv/adp/CWHT-A-001/as-built.md` names that release and the owner accepts (charter section 9; 04 section 5.3), or is dispositioned by an approved CR; every approved CR allocated to the release is implemented and listed in the VDD Changes section (SWE-194); zero open S1 or S2 NCR; flashed image hash equals VDD hash |

### 3.3 Milestones for progress review and audit (SWE-037)

The milestones are the five gates and the closure of every sprint (section 3.4 Phase 5). At each, the owner may audit: the sprint record, the gate log, any reviewer transcript, `docs/plan/measurements.json`. The planned versus actual comparison required by SWE-024 is the "Software status" section of every review package: increments planned and reached, sprints closed, requirements implemented against baselined, tests passed against defined, coverage against target, open NCRs by severity, corrective actions with their closure state.

### 3.4 Sprint structure (adapted from `rustos/docs/sdp/methodology.md` sections 2 to 9)

A sprint delivers one module (or one rustos work package) and is recorded in `docs/sprints/SW-NN-<module>.md`. Phases in order; none is skipped.

| Phase | Actor | Steps | Produces |
|---|---|---|---|
| 0 Pre-flight | Software lead | Read predecessor sprint record and `docs/lessons-learned.md`; confirm predecessors closed; run `.venv/bin/python tools/traceability.py` and `tools/sw_gate.sh --quick` to capture the baseline counts | Sprint record header with baseline counts |
| 1 Author fan-out | Author agents (one file each, dispatched in one message) | Files per the inventory of section 3.5; each author self-checks against the code checklist and states which `REQ-SW-*` ids each function implements (`// @req` tags, CS-24) | Files in the working tree |
| 2 Test-author fan-out | Test-author agents (never the author of the same module) | `TC-SW-<SUB>-NNN` cases in `docs/test_cases/sw-<sub>/test_cases.json` and the host test file or scenario that automates them, with `automation_ref` filled | Test cases and test code |
| 3 Reviewer fan-out | Reviewer agents (one file each; never the author), then the software assurance reviewer where section 2.1.1 says Yes | Verdict `APPROVED` or `NEEDS CHANGES` with `file:line` findings and severity Major or Minor against the checklist; up to three author-review iterations per file, then the software lead halts the sprint and escalates to the owner | One `INSP-NNN` record per reviewed file: the filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (section 10.2) |
| 4 Gate and assurance | Software lead runs `tools/sw_gate.sh`; software assurance reviewer verifies acceptance criteria | Gate G1 to G6 (section 8.4) exit 0; assurance verdict `PASS` or `FAIL` with reasons | Gate log in the sprint record |
| 5 Closure | Software lead | Write the sprint record; append measurements (section 11) to `docs/plan/measurements.json`; add lessons learned; mark sprint closed in `docs/sprints/index.md` | Closed sprint |

### 3.5 File inventory per sprint

| Sprint kind | Files (one author each) | Test author files |
|---|---|---|
| `cwht-core` module | `firmware/cwht-core/src/<module>/mod.rs` (public API and types), `firmware/cwht-core/src/<module>/<unit>.rs` per design unit (one file per unit, at most 500 lines) | `firmware/cwht-core/tests/<module>_test.rs` (integration-style host tests through the public API); unit tests inside a unit file are permitted only for private helpers and are also test-author files |
| rustos driver work package | `rustos/api/src/<periph>/mod.rs` (trait), `rustos/firmware/pico2/src/<periph>/mod.rs` and `<periph>.rs` (implementation with datasheet citations; decision functions host-compilable per CS-38), `firmware/cwht-hal-mock/src/<periph>.rs` (mock) | `rustos/api/tests/<periph>_contract.rs` (trait contract tests run against the mock), dev-board check binary `firmware/devcheck/src/bin/<periph>_check.rs` |
| Emulation scenario | `firmware/emu/scenarios/ops_<nnn>` (file format fixed by the PDR emulator ADR) | The scenario is itself test code; its reviewer is the test reviewer |
| Design | `docs/design/software-design.md` section per module (written as separate files `docs/design/sw/<module>.md` and included by the index if the file would exceed 500 lines) | none |
| Requirements | `docs/requirements/sw/sw-<sub>/requirements.json` (L2 software module files in the charter's numbering) | `TC-SW-<SUB>-*` in `docs/test_cases/sw-<sub>/test_cases.json` drafted by the test author at the same time |

---

## 4. Software requirements (SWE-050, SWE-051, SWE-053, SWE-054, SWE-055, SWE-184)

Requirements are governed by charter section 7 and `docs/process/02-requirements-and-traceability.md`; this section adds the software specifics.

1. **Levels.** `REQ-SYS-*` (L1) allocate to `REQ-SW-NNN` (firmware-wide L2, `docs/requirements/sw/requirements.json`) which allocate to the module files `REQ-SW-<SUB>-NNN` in `docs/requirements/sw/sw-<sub>/requirements.json` (L2 software module files in the charter's numbering, charter sections 5 and 6, `docs/process/02-requirements-and-traceability.md` section 2.1; called module files below). A module file exists for each module of the architecture; the candidate module list confirmed by the architecture ADR at PDR (`docs/process/02-requirements-and-traceability.md` section 2.2 creates the directories in the same commit) is `SW-BOOT`, `SW-KEYER`, `SW-DISPLAY`, `SW-SYNTH`, `SW-TXSEQ`, `SW-SAFE`, `SW-PWR`, `SW-AUDIO` (sidetone generation, audio output level clamp, ramps and fault mute), `SW-CFG`, `SW-SCHED`, `SW-DIAG`, plus `SW-HAL` for the rustos driver behaviors cwht relies on. Section 14.1 classifies each module and unit as safety-critical, mission-critical or neither.
2. **Derivation (SWE-051).** Every module-file requirement carries `parent_id` (a `REQ-SW-NNN` or `REQ-SYS-*`), or `source_ids` naming the hazard (`HZ-NNN`), ICD, ADR or SWE-134 item it derives from, with the derivation stated in `rationale`.
3. **Safety constraints in the SRS (SWE-184).** The module `SW-SAFE` requirement file records every constraint, control, mitigation and assumption between hardware, operator and software: the hardware interlocks assumed (PA bias needs both `PA_EN` and RF drive; charger IC limits independent of software; hardware PA-enable cutoff), the operator actions assumed (TX-arm gesture), and the software controls. Section 14.2 lists the SWE-134 provisions to be written as `REQ-SW-SAFE-001` to `REQ-SW-SAFE-012`.
4. **Validation (SWE-055).** Independent reviewer against `docs/templates/peer-review-checklist-requirements.md` (SE HB §4.2.1.2.4 six checks and Appendix C); ConOps scenario coverage is checked by mapping each `OPS-NNN` to at least one `REQ-SW-*`.
5. **Change and inconsistency (SWE-053, SWE-054).** After PDR, `CR-NNN` only; `tools/traceability.py`, schema validation and reviewer findings detect inconsistencies between requirements, this plan, design and code, and each is logged as a RID or CR and tracked to closure in the RFA/RID log or the CR log.
6. **Traceability tags in code (SWE-052 design-to-code):** CS-24 (section 7).
7. **Target platform rules as requirements (ADR-011 section 4.1).** The design rules of ADR-011 (single NVIC priority; PWM slices 0 to 7; GPIO via SIO; TICKS enabled explicitly; bounded XOSC and PLL waits with a fault path; emulation scenarios assert ordering only) are written as `REQ-SW-NNN` rows of the firmware-wide file by the requirements author in the PDR sprint and are enforced in code by CS-34 to CS-37.

---

## 5. Software architecture and design (SWE-057, SWE-058, SWE-143)

1. **Architecture** (`docs/design/architecture.md`, software section; PDR): component decomposition (the modules above); the execution model of ADR-011 and CS-34 to CS-37: single core, one NVIC priority level with run-to-completion handlers feeding a main-loop queue, keyer element timing from TIMER0 ALARM0 and 1 kHz input sampling (key, paddles, encoder, buttons, jack detect) from TIMER0 ALARM1 through SIO, both independent of the cooperative main loop that `SW-SCHED` dispatches on the ALARM1 1 ms tick; states and modes (Boot, SafeState, Receive, TxPending, Transmit, Fault, ChargeInhibited; the valid and invalid transitions per NPR 7150.2D §4.2.2 g); external interfaces (key/paddle jack, encoder, buttons, LCD, synthesizer, PA control, T/R control, ADC channels, USB bootloader) via `ICD-CTL-SW`; internal interfaces (the `api` traits each module consumes); quality attributes with numbers (key-to-RF latency budget, element timing jitter budget, boot-to-safe-state budget, resource budgets); and the safety-critical component list of section 14.1.
2. **Architecture review (SWE-143 as tailored):** an independent reviewer agent reviews the architecture at PDR against `docs/templates/peer-review-checklist-design.md`, with the software assurance second review (section 2.1.1); findings become `RID-PDR-NNN`.
3. **Detailed design** (`docs/design/software-design.md`; CDR): per module the purpose, public API (signatures as they will be written), state machines as tables (state, event, guard, action, next state), timing (periods, deadlines, worst-case paths), data (types, ranges, units, invariants), resource use, error taxonomy and handling, the `REQ-SW-*` implemented, the `HZ-NNN` controlled, the criticality of each unit (section 14.1, fixed by code unit as 03 section 4.3 does for the configuration guard), and for safety-critical units the decision table of every boolean decision (section 9.6). The design cites design units that map one-to-one onto Rust files (section 3.5), which is how design components trace to code.
4. **Design constraints from safety (SWE-134):** section 14.2 provisions are architecture constraints from PDR; the design shows where each is implemented.

---

## 6. Software implementation (SWE-060)

Implementation follows the sprint structure. A module is implemented only from an `Active` design section and baselined requirements; a change discovered necessary during implementation is a CR (design) or a RID (design defect), never a silent deviation. Every function that implements a requirement carries the CS-24 tag. Register-level code lives only in `pico2` and cites the RP2350 datasheet section and page, as the existing rustos GPIO driver does.

---

## 7. Rust coding standard (SWE-061, SWE-207)

The standard is normative for `cwht-app`, `cwht-core`, `cwht-hal-mock`, the rustos crates as used by cwht, and any Rust code of the emulation harness (rules marked "flight" apply only to code in the image). Enforcement column: **L** enforced by lint configuration (`[workspace.lints]` in `firmware/Cargo.toml` and `firmware/clippy.toml`), **G** by a gate script, **R** by the code review checklist. Rules are numbered `CS-NN` and cited in review findings.

### 7.1 Environment and dependencies

| Rule | Statement | Enforcement |
|---|---|---|
| CS-01 | Image crates are `#![no_std]`; `cwht-app` is also `#![no_main]`. The `alloc` crate is not linked; no heap, no allocator, no dynamic dispatch through `Box`. | L (`clippy::std_instead_of_core`, `clippy::alloc_instead_of_core`), G (link map shows no allocator symbol) |
| CS-02 | Zero external runtime crates: `Cargo.lock` for the image contains only workspace crates and rustos path crates (section 17). Dev-dependencies may use pinned OSS crates listed in the third-party register. | G (`cargo tree -e normal` on `cwht-app` lists only workspace and rustos crates), `cargo deny check bans` |
| CS-03 | Stable toolchain pinned by `firmware/rust-toolchain.toml` to `1.98.0` (`rustc 1.98.0 (88d9e12ae 2026-08-18)`, the lock's rustc row) with components `rustfmt`, `clippy`, `llvm-tools` and target `thumbv8m.main-none-eabihf`. No nightly toolchain is used for any release build or credit-bearing evidence build (`tools/toolchain.lock.md` section 1). One dated nightly is pinned for exactly two analyses, both labelled nightly in their reports and neither closing a requirement by itself: Miri undefined-behavior detection (MSR-08, section 8.1) and the branch and condition coverage measurement (MSR-14, section 9.6). The pin is `nightly-2026-08-24`, identified by `rustc 1.100.0-nightly (fb6531d55 2026-08-23)` as read with `rustc +nightly-2026-08-24 --version` on 2026-09-25; that toolchain was installed on 2026-09-25 by a review check with the default profile and has neither `miri` nor `llvm-tools`. The floating `nightly` channel also installed (`rustc 1.100.0-nightly (e7769602a 2026-08-24)`) is a different compiler and is never invoked. In FW-B0 the software lead runs `rustup toolchain install nightly-2026-08-24 --component miri --component llvm-tools` (installing it again if absent) and records name, commit hash and components in the lock; if rustup reports either component unavailable for that date, the software lead pins the nearest later dated nightly on which both install, records its `rustc --version` line in the lock and corrects this rule and every `+nightly-2026-08-24` invocation of this plan in the same commit. | G (`rustc --version` and `rustc +nightly-2026-08-24 --version` compared to the lock hashes before use; the gate refuses a nightly for any other step) |
| CS-04 | Profiles: `panic = "abort"`, `overflow-checks = true`, `debug-assertions = false` in release, `lto = "fat"`, `codegen-units = 1`, `opt-level = "s"` or `2` as decided by the flash TPM; the same profile is used for release and for run-for-record tests. | R, G (profile printed in the VDD) |

### 7.2 Unsafe code

| Rule | Statement | Enforcement |
|---|---|---|
| CS-05 | `#![forbid(unsafe_code)]` in `cwht-app`, `cwht-core`, `cwht-hal-mock` and any Rust crate of the emulation harness. `unsafe` is confined to rustos `pico2` (register access, boot, vector table) and `api` (handle constructors), which carry `#![deny(unsafe_op_in_unsafe_fn)]`. | L, G (`cargo geiger --forbid-only`) |
| CS-06 | Every `unsafe` block and `unsafe fn` in `pico2` and `api` has a `// SAFETY:` comment immediately above it stating the invariant relied on and why it holds at that site, citing the datasheet section for MMIO. | G (`tools/unsafe_audit.py` fails on an `unsafe` without `SAFETY`), R |
| CS-07 | The unsafe audit list `firmware/unsafe-audit.md` is generated by `tools/unsafe_audit.py` (file, line, kind, SAFETY text, reviewer id, date) and every entry is signed by a reviewer `INSP-NNN` before CDR and re-signed at SAR for entries that changed. | G, R |
| CS-08 | MMIO only through `read_volatile` and `write_volatile` on `#[repr(C)]` register layout structs addressed from `pico2::common::reg::RegAddr`; no integer-to-pointer arithmetic outside that module; atomic aliases (`+0x1000`, `+0x2000`, `+0x3000`) used for shared register fields touched from more than one context. | R, L (`clippy::ptr_as_ptr`, `clippy::cast_ptr_alignment`) |
| CS-09 | No `static mut`. Shared state uses `core::sync::atomic` types or a critical-section cell provided by `pico2` whose implementation is the only place interrupts are masked. | L (`static_mut_refs` deny), R |
| CS-10 | No `core::mem::transmute`, no `union`, no inline assembly outside `pico2` boot code; forbidden functions listed in `firmware/clippy.toml` `disallowed-methods` and `disallowed-types`. | L |

### 7.3 Panics, errors and arithmetic (flight)

| Rule | Statement | Enforcement |
|---|---|---|
| CS-11 | No panic path in flight code: `clippy::unwrap_used`, `expect_used`, `panic`, `unreachable`, `todo`, `unimplemented`, `indexing_slicing`, `panic_in_result_fn`, `exit` denied. Use `get`, `checked_*`, `match`, `?`. The single permitted `Option` unwrap-equivalent is the board `take()` in `cwht-app::main`, written as a `match` whose `None` arm calls `safe_state_halt()`. | L, R |
| CS-12 | The `#[panic_handler]` (in `pico2`, invoked by `cwht-app`'s configuration) writes the safe-state registers directly (PA off, T/R to receive, key output idle, charge inhibit asserted), records a panic marker in the persistent event log, and requests a watchdog reset. It calls no code that can itself panic. | R, Emulation event-order scenario `TC-SW-SAFE-*` (supporting unless inside ACC-EMU-001), Bench |
| CS-13 | Every fallible function returns `Result<T, E>` where `E` is a module-specific `enum` (no integers, no strings); infallible operations use `core::convert::Infallible`; every `Result` is handled or propagated (`#[must_use]` respected; `clippy::let_underscore_must_use` denied). | L, R |
| CS-14 | Arithmetic is explicit: `clippy::arithmetic_side_effects` denied in `cwht-core`; use `checked_`, `saturating_`, `wrapping_` with the choice justified in a comment for timer wrap-around. `overflow-checks = true` remains on in release. | L, R |
| CS-15 | No `as` numeric casts (`clippy::as_conversions` denied); use `From`, `TryFrom` and `u32::from(x)`; truncation is written as `TryFrom` with an error arm. | L |
| CS-16 | No floating point in safety-critical components and units (section 14.1); fixed-point integer arithmetic with documented scaling. Floating point elsewhere requires a design note on the FPU use and no `f32` comparison for equality. | L (`clippy::float_cmp`), R |

### 7.4 Structure and complexity (MISRA intent adapted to Rust)

| Rule | Statement | Enforcement |
|---|---|---|
| CS-17 | Cyclomatic complexity of every function is 15 or lower (SWE-220 applied to all flight code, not only safety-critical); yellow at 12 for the design reviewer's attention. Measured with `rust-code-analysis-cli` (section 8). | G (`tools/complexity_gate.py`) |
| CS-18 | Function length at most 60 lines of code; file length at most 500 lines; nesting depth at most 4. | L (`clippy::too_many_lines` = 60), G (`wc`), R |
| CS-19 | No recursion (direct or indirect). Loops have a bound visible in the source: iteration over a finite range or slice, or a counter with a compile-time maximum; the only unbounded loops are the main loop in `cwht-app::main` and the halt loop in the panic handler and `safe_state_halt`. | R, G (call-graph check in `tools/complexity_gate.py` reports cycles) |
| CS-20 | `match` on enums is exhaustive without wildcard arms in `cwht-core` (`clippy::wildcard_enum_match_arm` denied); state machines are `enum` typed and transitions are a single `match (state, event)`. | L, R |
| CS-21 | No shadowing (`clippy::shadow_unrelated`, `shadow_reuse`, `shadow_same` denied); no `#[allow]` or `#[expect]` without a trailing comment `// CS-NN waiver: <reason> (INSP-NNN)`. `#[expect]` is preferred so a stale waiver becomes a build error. | L, R |
| CS-22 | Interrupt handlers (all at the single priority of CS-34) do only: read the cause, timestamp, sample the SIO inputs (ALARM1 handler), push to a lock-free queue or set an atomic flag, re-arm the alarm, and acknowledge; no loops over data, no register writes to safety-critical outputs except the safe-state path. Worst-case handler duration recorded in the design and measured at Bench with a GPIO marker captured by the Pico-based logic capture (MSR-26). | R, Bench |
| CS-23 | Single core: core 1 stays in its bootrom wait state in Rev A (ADR at PDR records the decision). No use of the second core without a CR. | R |

### 7.5 Documentation, traceability and style

| Rule | Statement | Enforcement |
|---|---|---|
| CS-24 | Traceability tags: `// @req REQ-SW-<SUB>-NNN[, ...]` on the line above each function that implements a requirement; `// @verify REQ-SW-<SUB>-NNN[, ...]` above each test function and each emulation scenario entry point; `// @design <module>/<unit>` on each unit file header. `tools/traceability.py` parses these for the design-to-code and requirement-to-verification links. | G |
| CS-25 | `#![deny(missing_docs)]` on all image crates; every `pub` item documented; register-touching functions cite the RP2350 datasheet section and page in the doc comment (rustos house style). | L, R |
| CS-26 | `rustfmt` with `firmware/rustfmt.toml` (`edition = "2024"`, `max_width = 100`); `cargo fmt --check` is gate G1. | G |
| CS-27 | Clippy configuration: `-D warnings`, `-W clippy::pedantic`, `-W clippy::nursery` promoted to deny in the gate, plus the restriction lints named in CS-11, CS-14, CS-15, CS-20, CS-21 denied, and `clippy::cognitive_complexity` with threshold 15 as a second opinion on CS-17. Configuration lives in `[workspace.lints]` so it is versioned with the code. | L, G |
| CS-28 | Names: types `UpperCamelCase`, functions and fields `snake_case`, constants `SCREAMING_SNAKE_CASE`, register block and field names match the datasheet exactly (with `#[allow(non_camel_case_types)]` waiver per CS-21 where needed), units in identifiers where a value has one (`dot_len_us`, `vbat_mv`, `pa_temp_dc`). | R |

### 7.6 Secure coding practices (SWE-207; charter section 12 retains these in full)

| Rule | Statement | Enforcement |
|---|---|---|
| CS-29 | Every external input is validated at the boundary before use: key and paddle samples are debounced with the make and open times of `REQ-SW-KEYER` (HZ-010: 2 ms make, 5 ms open, TBR) and rate-limited; encoder deltas are range-checked; ADC readings are range-checked against physical limits and flagged if implausible; every I2C/SPI response is length- and value-checked; configuration records are CRC-32 checked and range-checked field by field. | R, `TC-SW-*` off-nominal cases |
| CS-30 | No interpreter, parser of free-form data, or command channel exists in the image other than the bootrom's USB loader (which runs before the image). The key input is a two-bit signal to the keyer state machine and nothing else; menu gestures are fixed sequences on the buttons and encoder, never on the key line. | R, design inspection |
| CS-31 | Buffers are fixed-size arrays with explicit capacity constants; no unbounded copies; `clippy::indexing_slicing` (CS-11) forces bounds handling. Stack depth budget per task recorded in the design and checked by the stack watermark measurement (MSR-16). | L, G |
| CS-32 | Integrity: the image carries a CRC-32 trailer written by the release script and verified at boot before any safety-critical output is enabled; configuration in flash is stored as two copies with CRC-32 and a sequence number; the RAM copy of safety-critical flags is stored with its complement (section 14.2 f). | R, `TC-SW-CFG-*`, `TC-SW-BOOT-*` |
| CS-33 | Diagnostics do not leak control: the event log is read-only over the diagnostic serial interface; no command on that interface can change state other than `reboot`. | R |

### 7.7 Target platform rules (ADR-011 section 2 and section 4.1)

| Rule | Statement | Enforcement |
|---|---|---|
| CS-34 | Interrupt model: every enabled interrupt runs at one NVIC priority level (no priority is ever written, so no handler preempts another); handlers run to completion; no nesting. The emulators characterized for ADR-011 do not model NVIC priorities, and silicon then behaves as the design states. | R, Inspection (grep for NVIC priority register writes: none), `TC-SW-HAL-*` dev-board check |
| CS-35 | GPIO through SIO only (`GPIO_IN`, `GPIO_OUT`, `GPIO_OE` set, clear and xor aliases), never the GPIO coprocessor instructions; no IO_BANK0 edge interrupts: key, paddle, encoder and button inputs are sampled at 1 kHz from the TIMER0 ALARM1 handler and edges are derived in `cwht-core` from consecutive samples carrying the sample timestamp. | R, Inspection |
| CS-36 | PWM uses slices 0 to 7 only, each enabled through its own slice CSR enable bit. | R, Inspection against `ICD-CTL-SW` |
| CS-37 | The clock driver enables `TICKS.TIMER0` and `TICKS.WATCHDOG` explicitly from `clk_ref` with `CYCLES` matching the reference frequency before any TIMER0 or watchdog use, and bounds every XOSC `STABLE` and PLL `LOCK` wait with a TIMER0-independent loop-count timeout that returns a clock fault; the fault path leaves the safe outputs of section 14.2 a asserted. | R, HostUnit (decision function per CS-38), dev-board check |
| CS-38 | Target-only code holds no decision: in `cwht-app` and in the MMIO, boot and vector-table code of `pico2`, functions are straight-line (cyclomatic complexity 1) except the board `take()` match of CS-11. Every decision of a `pico2` driver used by a safety-critical component (section 14.1), including the CS-37 timeout decisions, is a host-compilable function (no MMIO access, register values passed in and out) exercised by HostUnit tests with MC/DC independence pairs (section 9.6). | G (`tools/complexity_gate.py` reports CC above 1 in files tagged `// @target-only`), R |

---

## 8. Static analysis toolchain (SWE-135, SWE-185, SWE-136)

### 8.1 What exists for Rust on macOS as of 2026-09-25 (verified)

| SWE-135 item | Tool | Status verified | Notes and limits |
|---|---|---|---|
| Defects | `cargo clippy` (ships with rustup toolchain) | Installed with `rustc 1.98.0` | Lint sets per CS-27. `cognitive_complexity` is a nursery lint that replaced clippy's old cyclomatic lint and measures a related but different quantity; it is a cross-check, not the SWE-220 measure. |
| Defects (undefined behavior in `unsafe`) | Miri (`cargo miri`; a nightly-only rustup component) | Not installed: `rustup component list --installed` shows no `miri` on `nightly-aarch64-apple-darwin` or on `nightly-2026-08-24-aarch64-apple-darwin`; the `cargo-miri` proxy in `~/.cargo/bin` has no tool behind it (verified 2026-09-25). To be installed in FW-B0 per CS-03 | Runs, as `cargo +nightly-2026-08-24 miri test` (CS-03), the host tests of `api` and of the host-compilable `pico2` decision functions (CS-38) under the UB detector; the result is analysis evidence (MSR-08), never a credit-bearing build. Miri cannot execute volatile MMIO or the boot path; those are covered by dev-board checks, Bench cases and driver-to-datasheet Inspection. |
| Security (advisories) | `cargo audit` (RustSec, `rustsec/rustsec`, active) | Installed: `cargo-audit` 0.22.2 (verified 2026-09-25) | Trivial for a zero-dependency image; still run on the whole workspace because dev-dependencies exist. |
| Security (licenses, bans, sources) | `cargo deny` (`EmbarkStudios/cargo-deny`, active) | Installed: `cargo-deny` 0.20.2 (verified 2026-09-25) | `firmware/deny.toml`: allow-list of licenses (MIT, Apache-2.0, BSD-3-Clause, Unicode-3.0), `bans` deny everything not in the third-party register, `sources` allow only crates.io and the rustos path. |
| Security (unsafe quantity) | `cargo geiger` 0.13.0 (`rust-secure-code/cargo-geiger`, crates.io release 2025-08-31) | Installed: `cargo-geiger` 0.13.0 (verified 2026-09-25) | `--forbid-only` mode confirms `#![forbid(unsafe_code)]` on the image crates; full mode counts `unsafe` in `pico2` and `api`. Known: crashes on some complex workspaces; the cwht workspace is small. Complemented by `tools/unsafe_audit.py` (CS-06, CS-07). |
| Coverage (line, region, function) | `cargo llvm-cov` (`taiki-e/cargo-llvm-cov`, 0.9.1 released 2026-09-06) on stable `-C instrument-coverage` | Installed: `cargo-llvm-cov` 0.9.1 (verified 2026-09-25) | Credit-bearing coverage measure. Supports `--fail-under-lines`, `--fail-uncovered-lines`, `nextest` integration, `lcov` and `json` output. |
| Coverage (branch, condition) | `cargo +nightly-2026-08-24 llvm-cov --branch` with `-Z coverage-options=branch` and `-Z coverage-options=condition` | Nightly `nightly-2026-08-24` present without `llvm-tools` (verified 2026-09-25); `llvm-tools` to be installed in FW-B0 per CS-03 | Unstable; the nightly unstable book lists `block`, `branch` and `condition` levels. Required at every release (MSR-14): with the reviewed independence-pair tables and the stable region coverage it is the third element of the SWE-219 showing that charter section 10 requires (section 9.6). Labelled nightly; never a release build and never by itself closing a requirement (`tools/toolchain.lock.md` section 1). |
| Coverage (MC/DC) | none available | Verified 2026-09-25 | rustc's earlier `-Z coverage-options=mcdc` instrumentation was removed in late 2025 (rust-lang commit 562222b; reasons given: maintenance burden, incomplete, blocked other coverage work). A 2026 Rust project goal ("Implement and Maintain MC/DC Coverage Support", rust-lang/goals issue 638, owner Dorian Péron, AdaCore maintenance commitment, compiler champion David Wood) plans decision coverage first and MC/DC after, as unstable nightly support, with nothing usable at this date. `cargo llvm-cov` still lists an unstable `--mcdc` flag, which has no effect without compiler support. See section 9.6 for the tailoring. |
| Complexity (cyclomatic) | `rust-code-analysis-cli` 0.0.25 (`mozilla/rust-code-analysis`; crates.io release 2023-01-13, repository not archived, last push 2026-04) | Not installed; `cargo install rust-code-analysis-cli --locked` in FW-B0 | Computes cyclomatic complexity (CC), cognitive complexity, Halstead, LLOC and others per function for Rust, output as JSON: `rust-code-analysis-cli --metrics --output-format json --paths firmware/`. `tools/complexity_gate.py` reads the JSON and fails on CC > 15 (CS-17) and on CC > 1 in target-only files (CS-38). Risk: stale release; mitigation: the tool is pinned, its output is sanity-checked at accreditation on a reference function set with hand-computed CC. |
| Test runner (repeatability) | `cargo nextest` (`nextest-rs/nextest`, active) | Installed: `cargo-nextest` 0.9.146 (2026-09-21; verified 2026-09-25) | Profile `ci` in `firmware/.config/nextest.toml` (`retries = 0`, `fail-fast = false`, `[profile.ci.junit] path = "junit.xml"`) writes JUnit to `firmware/target/nextest/ci/junit.xml` (path confirmed on a scratch crate on 2026-09-25). The JUnit files carry a run uuid, timestamps and durations, so the gate compares the set of (classname, test name, outcome) triples of two runs, not the bytes (SWE-186); the two files are kept as regression report artifacts (section 9.3). |
| Mutation testing (optional, not gated) | `cargo mutants` 27.1.0 (`sourcefrog/cargo-mutants`, crates.io 2026-06-02) | Optional; not installed | Mutation score reported as MSR-12 from FW-B2; used to strengthen tests of safety-critical modules; no threshold. |
| Model checking (optional) | Kani (`model-checking/kani`, active) | Decision at PDR (ADR) | Candidate for bounded proofs of `SW-KEYER` and `SW-TXSEQ` invariants; adopted only if the PDR ADR says so. |
| Qualified toolchain (option) | Ferrocene (Ferrous Systems): `thumbv8m.main-none-eabihf` is a "Supported" (not "Qualified") target; `aarch64-apple-darwin` host is "Quality Managed"; certified `core` subset exists | Option, not adopted for Rev A | A commercial subscription; the Cortex-M33 target is not in Ferrocene's qualified tier, so it would not by itself qualify the cwht build. Recorded as an option in the toolchain accreditation ADR; Rev A accredits upstream stable rustc per section 17.3. |
| Flashing and image tools | `picotool` 2.x (Homebrew) | Installed (v2.3.0 verified by rustos) | `picotool uf2 convert`, `picotool load`, `picotool verify`, `picotool info` used by the release and flashing procedures. |

Versions marked "verified 2026-09-25" were read on the owner's machine (`cargo <tool> --version`, `rustup component list --installed --toolchain <t>`) and checked against crates.io the same day. `tools/toolchain.lock.md` rows 21 to 25 already list `cargo-llvm-cov`, `cargo-audit`, `cargo-deny`, `cargo-geiger` and `cargo-nextest` with these versions. The lock still lacks the pinned nightly with its components (its nightly row names only the floating `nightly-aarch64-apple-darwin` and permits coverage only, and its `cargo-miri` row says "Not permitted (would need CR)"); the software lead adds the `nightly-2026-08-24` row with `miri` and `llvm-tools`, the Miri use and the `rust-code-analysis-cli` version in FW-B0. Change class: the lock is 05 Table 4-1 row 27, class CR from SRR; before SRR a CR-class item is at L0/L1 and its changes are Log-controlled, a commit with a `Refs:` trailer (05 section 4.2 preamble), which is how the FW-B0 edits are made; after SRR a version change of a listed tool, or permitting a new use such as Miri, is a `CR-NNN` with a new `TV-NNN` (05 section 5.1), while a row for a newly installed tool stays Log-class until that tool has a TV record (lock header). Every tool marked Installed receives a `TV-NNN` record before its first use for the record (section 8.3).

### 8.2 Measurement of each SWE-135 item

| Item | Measure recorded (MSR id) | Threshold (gate fails when) | Where recorded |
|---|---|---|---|
| Defects | MSR-07 clippy warnings with the CS-27 set; MSR-08 Miri failures | any warning; any Miri failure | gate log, VDD |
| Security | MSR-09 advisories from `cargo audit`; MSR-10 `cargo deny` violations; MSR-11 unsafe count (blocks, fns, impls) in `pico2` and `api` from `cargo geiger` and `tools/unsafe_audit.py`; unsigned audit entries | any advisory without a recorded disposition; any deny violation; any unsigned unsafe entry at CDR or SAR | gate log, `firmware/unsafe-audit.md`, VDD |
| Coverage | MSR-13 line and region coverage per crate (stable toolchain; credit-bearing); MSR-14 branch and condition coverage (pinned nightly; required element of the SWE-219 record, section 9.6); MSR-15 MC/DC analysis completeness for safety-critical decisions | MSR-13, MSR-14 or MSR-15 below the section 9.5 targets without a disposition table | `docs/vv/reports/TC-SW-COV-001-r<N>.md` (04 section 12) |
| Complexity | MSR-17 max CC, mean CC, count of functions with CC > 12 and > 15, and target-only functions with CC > 1 | any function with CC > 15 without an owner waiver in the latest decision memo; any target-only function with CC > 1 other than the CS-11 board take | gate log, `docs/plan/measurements.json`, VDD |

### 8.3 Accreditation of the tools (SWE-136, SWE-070)

Each class A or B tool (05 section 9.1: product-generating or evidence-generating) gets a tool validation record `docs/cm/tool-validation/TV-NNN-<tool>.md` (charter section 5; content per 05 section 9.2 step 1: exact version string and the command that produced it, install source, class, purposes covered, known-answer test with fixtures under `tools/tests/fixtures/<tool>/`, result with date, reproducibility result, reviewer check, owner accreditation decision). `tools/toolchain.lock.md` summarizes for each tool: name, exact version, command, date, class, TV record and accreditation status. Sanity checks (the known-answer tests of the TV records): rustc builds and links the rustos blinky and the ELF hash matches the committed `blinky.elf` (rustos verified this on 2026-08-30); clippy reports a seeded `unwrap` in a scratch crate; Miri reports a seeded out-of-bounds read; `cargo llvm-cov` reports 100 percent on a fully exercised reference crate and reports a seeded uncovered branch; `rust-code-analysis-cli` returns CC values equal to hand-computed values for five reference functions (CC 1, 2, 5, 15, 16); `cargo geiger` counts the known number of `unsafe` sites in `pico2`; `cargo audit` and `cargo deny` flag a seeded yanked or GPL dev-dependency in a scratch workspace; `picotool verify` detects a one-byte change to an image; the emulator is accredited by `ACC-EMU-001` for register-visible event order only, never timing (section 9.4 item 4). The owner records each accreditation decision in the TV file (05 section 9.2 step 3); the Rust toolchain, coverage and static analysis tools and the emulator are accredited by PDR, `picotool` and `cargo-binutils` by CDR (`tools/toolchain.lock.md` section 5), every class A tool re-runs its known-answer test at each new baseline (05 section 9.2 step 4), and the lock is re-checked at each TRR (`docs/process/04-verification-and-validation.md` section 4). Until a tool is Accredited its output is developer evidence only. A tool version change after PDR is a CR against the lock (Class I when the tool can change a released image: `rustc`, linker, `picotool`).

### 8.4 The gate script `tools/sw_gate.sh`

Runs from the repository root on macOS with the pinned toolchain; each gate prints `PASS` or `FAIL` and the script exits non-zero on the first failure. `--quick` runs G1 to G3 only.

| Gate | Command (abridged) | Passes when |
|---|---|---|
| G1 Format and lint | `cargo fmt --check`; `cargo clippy --workspace --all-targets -- -D warnings`; `cargo clippy -p cwht-app --target thumbv8m.main-none-eabihf -- -D warnings` | no diff, no warning |
| G2 Build | `cargo build -p cwht-app --release --target thumbv8m.main-none-eabihf`; link map parsed for flash and RAM (MSR-18, MSR-19) and absence of allocator symbols | builds; usage below TPM-010/011 red lines |
| G3 Host tests | `cargo nextest run --workspace --profile ci` twice, each JUnit file copied to `firmware/target/nextest/run1-junit.xml` and `run2-junit.xml`; `tools/measurements.py --diff-runs` compares the (classname, name, outcome) sets | all pass both times; identical result sets; both JUnit files kept (release: copied into `docs/vv/reports/TC-SW-REG-001-r<N>/`) |
| G4 Traceability | `.venv/bin/python tools/traceability.py` | exit 0; every `REQ-SW-*` in scope has `@req` and `@verify` tags |
| G5 Static analysis | `cargo audit`; `cargo deny check`; `cargo geiger --forbid-only`; `tools/unsafe_audit.py --check`; `rust-code-analysis-cli` piped to `tools/complexity_gate.py --max 15`; `cargo +nightly-2026-08-24 miri test -p api -p pico2 --lib` (MSR-08, CS-03) | no advisory, no violation, no unsigned unsafe, no CC > 15, no target-only CC > 1, no Miri failure |
| G6 Coverage and emulation (release gates and CDR onward) | `cargo llvm-cov nextest --workspace --profile ci --lcov --output-path ...` (stable, MSR-13); `cargo +nightly-2026-08-24 llvm-cov nextest --workspace --profile ci --branch --json ...` with `RUSTFLAGS=-Zcoverage-options=condition` (MSR-14); `tools/emu_run.sh --all --report firmware/target/emu-report.json` (event-order scenarios on the emulator of the PDR ADR; prints `SKIP emulation: no accepted emulator ADR` and exits 0 until that ADR is Accepted) | coverage per section 9.5 or a disposition table present; MSR-14 report produced; every emulation scenario passes, or the `SKIP` line before PDR |

---

## 9. Software testing (SWE-062, SWE-065, SWE-066, SWE-068, SWE-071, SWE-073, SWE-186, SWE-187, SWE-189 to SWE-193, SWE-211)

Test plan (SWE-065 a) is the software section of `docs/vv/plan.md`; procedures (b) are `docs/test_cases/sw-<sub>/test_cases.json`; tests (c) are the host test files and emulation scenarios named in each case's `automation_ref`; reports (d) are `docs/vv/reports/`. Evidence classes and credit rules are those of `docs/process/04-verification-and-validation.md` sections 4 and 5.2 and ADR-011; this section states the software policy inside them. SWE-073 (validation on the target platform or a high-fidelity simulation) is met on the target: dev-board checks (risk reduction) before the unit exists, and Bench and OnAir on `CWHT-A-001`; Emulation is not a SWE-073 high-fidelity simulation (04 section 4).

### 9.1 Levels

| Level | Environment | What it verifies | Class (`type`) | Credit |
|---|---|---|---|---|
| Unit and module | Host, `cwht-core` against `cwht-hal-mock`, mock clock (0.1 ms resolution) | Every `REQ-SW-*` that is platform-independent logic, including its timing on the mock clock: keyer element timing and iambic modes A and B, straight-key debounce, weighting, speed range 5 to 50 WPM (SI-033; dot = 1200/WPM ms), menu and tuning-step logic, sequencing guards (SWE-134 e, h), configuration CRC and range checks, fault taxonomy, the `SW-SCHED` dispatch, overrun and watchdog-kick decisions, and the host-compilable `pico2` decision functions (CS-38) | HostUnit | Yes, under the 04 section 5.2 row for software platform-independent logic |
| Trait contract | Host, each rustos driver's `api` trait exercised against the mock; the same contract checks on the dev board | The contract every implementation must satisfy | HostUnit (mock); Bench `credit: false` (dev board) | Supporting |
| Integration (whole image), optional | The emulator selected by the PDR emulator ADR running the release image with scripted stimuli on SIO GPIO, UART0, I2C0, SPI0 and ADC plumbing; captured register-visible and pin event sequences | Event order only: safe outputs asserted before any other initialization after reset, T/R command before `PA_EN` rises, `PA_EN` low before T/R returns to receive, panic and watchdog paths reaching the safe-state pin sequence, image CRC rejection sequence, the event sequences of each `OPS-NNN` scenario | Emulation | Closing only for requirements that state only an event order and whose peripherals are inside `ACC-EMU-001`; otherwise supporting (04 section 5.2; section 9.4) |
| Dev-board checks | Bare Pico 2 board flashed with `firmware/devcheck` binaries; the owner observes LED, sidetone and serial output; Pico-based logic capture once its TV record exists | Driver bring-up, reference register sequences for `ACC-EMU-001`, owner HSI evaluation of the keyer, early timing measurements | recorded as `type: Bench`, `article: pico2-devboard-1`, `credit: false` (the dev-board rule of 04 section 4, Bench row) | Risk reduction only |
| Target timing | Delivered unit `CWHT-A-001` after TRR, Pico-based logic capture (04 section 6.1) | Every requirement that states a duration, latency, rate or timeout: key-to-`PA_EN` latency, keyer element and gap lengths, debounce make and open times, boot-to-safe-state time, watchdog period, the detection-to-`PA_EN`-low budgets of section 14.2 j, tick overruns and handler duration markers | Bench | Yes, under the 04 section 5.2 row for software that depends on target timing, peripherals or interrupts |
| System | Delivered unit `CWHT-A-001` after TRR | Everything else, including run-for-record confirmation | Bench, OnAir | Yes, per 04 |

### 9.2 Repeatability (SWE-186)

Tests use the mock clock and injected inputs only: no wall-clock reads, no `std::thread::sleep`, no real I/O, no environment variables; any pseudo-random input is seeded from a constant in the test and the seed is printed on failure; tests are independent of execution order (nextest runs each test in its own process); the toolchain and `Cargo.lock` are pinned; the gate runs the suite twice and fails on any difference in the set of passed and failed tests (G3). A test that fails intermittently is an NCR against the test (`Procedure-correction`) and blocks the release until fixed.

### 9.3 Regression (SWE-191)

On every change to `firmware/` or to the rustos crates, and before every tag: G1 to G6 in full, including the cybersecurity cases (section 16.4) so that a security regression cannot pass unnoticed. The regression report for a release is the gate log filed as `docs/vv/reports/TC-SW-REG-001-r<N>.md` with the two JUnit files of G3 and the coverage artifacts in `docs/vv/reports/TC-SW-REG-001-r<N>/`. A release with any failing automated case is not tagged (04 section 10.5).

### 9.4 Whole-binary emulation (ADR-011; 04 sections 4 and 5.2)

Emulation is optional and secondary (charter section 9, SI-026, ADR-011). The RP2350 emulators available do not model seconds, GPIO edge interrupts or NVIC priorities at the characterized commit (ADR-011 section 1; `docs/research/emulator-accreditation-and-timer-irq.md` F5, F8, F9), so Emulation is not a SWE-073 high-fidelity simulation (04 section 4) and never carries timing credit.

1. **Selection.** The emulator is chosen by the emulator ADR due at PDR (ADR-011 section 3): c1570/rp2350js in ARM mode at commit `af0114cb`, the `ACC-EMU-001` candidate, or Renode as the fallback. The same ADR fixes the vendoring form (the accreditation study proposes a git submodule under `tools/emu/` with a mirror fork), the harness and the scenario file format under `firmware/emu/`. Until the ADR is Accepted, emulation runs are `credit: false` and G6 prints its `SKIP` line.
2. **What a scenario may assert.** Only event order: which register-visible write, pin transition or serial byte precedes which. Time appears only in TIMER0 microseconds as a sequence key, never as a duration, frequency or timeout; a scenario that asserts a duration is a `Procedure-correction` NCR against the case (04 section 5.2).
3. **Credit.** An Emulation case closes a requirement only when the requirement states only an event order and every peripheral the scenario relies on is inside the `ACC-EMU-001` scope named in ADR-011 section 2 (boot, Cortex-M33 execution, TIMER0 alarms and NVIC entry, SIO GPIO, UART0, I2C0 and SPI0 byte streams, ADC plumbing, PWM slices 0 to 7, ordering); otherwise the case is supporting and the closing case is HostUnit or Bench (04 section 5.2).
4. **Accreditation scope.** `ACC-EMU-001` (`docs/research/emulator-accreditation-and-timer-irq.md` F13; adopted by the PDR emulator ADR as the emulator's TV record `docs/cm/tool-validation/TV-NNN-<emulator>.md`, credit scope summarized in `tools/toolchain.lock.md`) accredits register-visible sequence agreement only: for each in-scope peripheral, the `firmware/devcheck` binary of its work package (section 19) produces the same ordered sequence of register-visible events on the dev board and in the emulator, and the known answers KA-1 to KA-3 reproduce with their stored hashes. No timing tolerance is accredited.
5. **No timing credit.** Every requirement that states a duration, latency, rate, frequency or timeout (key-to-`PA_EN` latency, element timing, boot-to-safe-state time, watchdog period, the section 14.2 j budgets, tick overruns) is verified by HostUnit on the mock clock for its logic and closed at Bench with the Pico-based logic capture on `CWHT-A-001` (04 section 5.2 target-timing row; 04 section 6.1).
6. **Fallback.** If no emulator is accepted at PDR, or the selected one fails `ACC-EMU-001` on SIO GPIO or TIMER0 alarms, the fallback of RSK-003 (`docs/risk/register.json`, emulator mis-models a peripheral or cannot boot the image) applies: HostUnit plus dev-board checks and Bench; every Emulation case is re-typed Bench by CR and emulation runs stay `credit: false` (04 section 5.2). The decision is recorded in the PDR decision memo.

### 9.5 Coverage targets and dispositions (SWE-189, SWE-190)

The rules are those of `docs/process/04-verification-and-validation.md` section 12, scoped as follows.

1. **Host-compilable code.** 100 percent statement (line and region) coverage from HostUnit execution of `cwht-core`, the host-compilable parts of `api` (types, default methods, contract helpers), the host-compilable decision functions of `pico2` (CS-38) and `cwht-hal-mock`. Every uncovered line in that scope is dispositioned as requirement missing (becomes a CR), test missing (becomes a case), dead code (removed) or deactivated code (listed with its activating configuration) (SWE-189 note).
2. **Target-only code.** `cwht-app` (`#![no_main]`) and the MMIO, boot and vector-table code of `pico2` do not compile for the host. Each such line is listed line by line in `TC-SW-COV-001-r<N>` with the disposition `target-only: verified by <TC-ID>`, naming the dev-board check (`credit: false`), the Bench case or the emulation event-order scenario that executes it, plus the driver-to-datasheet Inspection for each register access. This is the complementary inspection and test that the SWE-190 note and 04 section 12 ("Analysis of results") admit where execution cannot reach 100 percent; the reviewer who signs the report signs the list.
3. **Safety-critical components** additionally show 100 percent MC/DC by the analysis of section 9.6 on their host-compilable decision code. CS-38 keeps every decision of a safety-critical component out of target-only code, so no safety-critical decision falls under item 2; the one exception, the board `take()` match of CS-11, is listed in the MC/DC table with its `None` arm dispositioned `target-only: Inspection`. The credit-bearing measurement is stable-toolchain region coverage of the independence-pair tests (MSR-13); tool-measured branch and condition coverage (MSR-14, pinned nightly) is attached to the same report at every release as the third element of the SWE-219 showing (charter section 10) and never by itself closes a requirement.
4. **Source of the numbers.** Coverage is computed only from the tests executed on the tagged release (`cargo llvm-cov` over the nextest run), never from a development build. Emulation coverage is reported as "not measured" unless the emulator exports it. Report: `docs/vv/reports/TC-SW-COV-001-r<N>.md` (`test_case: TC-SW-COV-001`, `firmware_version` carrying the release) with raw `lcov.info` and the MC/DC tables in `docs/vv/reports/TC-SW-COV-001-r<N>/` (04 sections 12 and 15).

### 9.6 MC/DC for safety-critical components (SWE-219) as achievable today

Tool-instrumented MC/DC is not available for Rust at this date (section 8.1). The 04 section 12 fallback is therefore the baseline method for Rev A, not a contingency, and SWE-219 is dispositioned **T** in `docs/process/rmm.json` (residual risk RSK-010; approved by the owner at SRR):

1. The detailed design lists every boolean decision in safety-critical components and units with its conditions (design "decision table", section 5 item 3); CS-17, CS-20 and CS-38 keep decisions small and host-compilable (at most 4 conditions per decision; more is a design finding).
2. The test author writes, per decision, the MC/DC independence pairs as named test functions (`// @mcdc SW-SAFE/D07 c2`), so that each condition is shown to independently affect the outcome with all other conditions held.
3. Two tool measurements accompany the tables at every release. Stable-toolchain line and region coverage (`cargo llvm-cov`, MSR-13, credit-bearing) confirms that every independence-pair test executed. Branch and condition coverage of the same test run on the pinned nightly (`cargo +nightly-2026-08-24 llvm-cov --branch` with `-Z coverage-options=condition`, MSR-14) confirms that every branch and every condition of each listed decision was exercised in both outcomes; MSR-14 is labelled nightly and never by itself closes a requirement (CS-03; `tools/toolchain.lock.md` section 1). The coverage report `docs/vv/reports/TC-SW-COV-001-r<N>.md` contains the MC/DC table (decision, conditions, test ids per independence pair, MSR-14 branch and condition result per condition, outcome) and an independent reviewer signs it (`INSP-NNN`, with the software assurance review of section 2.1.1); the reviewed table plus MSR-13 plus MSR-14 is the SWE-219 record that charter section 10 describes.
4. A shortfall against 100 percent needs an owner waiver with rationale, as SWE-219's own note provides for deviations: a numbered product waiver `W<n>` in the CDR, TRR or SAR decision memo, entered in CSA item 12 and listed in VDD section 7 (05 section 2). 01 section 8.6 is the single statement of this relief (owner decision at SRR); the RMM SWE-219 row stays the relief for the method.
5. When rustc MC/DC instrumentation returns to nightly (the 2026 project goal), a CR evaluates adopting it; the manual tables remain the record until the tool is accredited.

### 9.7 Hazard-tracing requirements (SWE-192) and loaded data (SWE-193)

Every `REQ-SW-*` with `hazard_ids` has method Test and a closing case with `verification_method` Test (enforced by `tools/traceability.py` check `HAZARD_REQ_NOT_TESTED`, which admits no Analysis exception for `SW` and `SW-<SUB>` modules; 04 section 7.3 rule 6). The closing case is HostUnit for platform-independent logic (including its timing on the mock clock), Bench with the logic capture for target timing, or Emulation only for a requirement that states only an event order (section 9.4 item 3); every hazard-tracing requirement is confirmed at Bench on `CWHT-A-001` before SAR. Acceptance tests for loaded items: firmware image load (valid UF2 accepted and boots; image with a corrupted CRC trailer is refused and the unit enters SafeState with fault code; `picotool verify` matches), persisted configuration (nominal values accepted; out-of-range speed, mode, frequency or calibration rejected and defaults restored; corrupted copy A falls back to copy B; both corrupted gives defaults and a logged event). Cases live in `docs/test_cases/sw-cfg/` and `docs/test_cases/sw-boot/`.

### 9.8 Configuration before test (SWE-187)

Run-for-record tests run only on a tagged commit (`release/FW-vX.Y.Z`, or `release/FW-vX.Y.Z-rcN` for a candidate; 05 section 4.3) whose VDD exists; every report records in its front matter (template `docs/templates/verification-report.md`; 05 section 7.3 item 1) the release and its tag (`firmware_version`), the source commit S (`source_commit`), the image hash (`firmware_elf_sha256`, the ELF line of the release `SHA256SUMS`), the harness and emulator versions (`harness_versions`), the toolchain lock commit (`toolchain_lock`) and the procedure blob (`procedure_blob` at `procedure_commit`), which FCA-03 and FCA-04 check. Test code and mocks are configuration items in the same tag.

### 9.9 Reused component testing (SWE-211)

rustos `api` and `pico2` features used by cwht are enumerated in the third-party register (section 17.1) with the contract tests and dev-board or Bench checks that cover them; a rustos feature not covered is not used.

---

## 10. Software peer reviews and inspections (SWE-087, SWE-088, SWE-089)

### 10.1 Products reviewed

| SWE-087 item | Product | Checklist | When |
|---|---|---|---|
| a. Software requirements | Every `docs/requirements/sw/**/requirements.json` file and every CR touching one | `docs/templates/peer-review-checklist-requirements.md` sections A to F | Before PDR baseline; on each CR |
| b. Software plans including cybersecurity | This plan (section 16 included), `docs/vv/plan.md` software section, every `docs/process/0N-*.md` | `docs/templates/peer-review-checklist-requirements.md` section G (plan items CK-REQ-G1 to G8) | Before SRR; at each re-approval |
| c. Design items | Architecture software section (PDR); every module section of `software-design.md` (CDR) | `docs/templates/peer-review-checklist-design.md` | Before PDR and CDR |
| d. Code | Every file authored or changed in a sprint, before the gate | `docs/templates/peer-review-checklist-code.md` | Every sprint |
| e. Test procedures | Every `TC-SW-*` case before `Active`; every test file and scenario | `docs/templates/peer-review-checklist-test.md` | Every sprint; before CDR |

The software assurance second review of each product follows the table of section 2.1.1.

### 10.2 Procedure (SWE-088)

| Element | Rule |
|---|---|
| Readiness criteria | Author self-check completed and stated in the return; the file parses or compiles (`cargo check`, `jsonschema`); `tools/traceability.py` clean for the ids the file touches; the brief's acceptance criteria listed in the review record; for code, G1 passes on the file's crate |
| Participants | Author agent (absent from the review), reviewer agent (different invocation), software assurance reviewer where the table of section 2.1.1 says Yes, owner for disposition of unresolved Major findings and of deferrals |
| Method | Checklist reading: every checklist item is answered Yes, No or Not applicable with evidence (`file:line` or field name); findings carry severity Major (blocks approval: defect that would make the product wrong, unsafe, untraceable or unverifiable) or Minor (fix before the next gate) |
| Completion criteria | Record `verdict: APPROVED` only when `reviewer_verdict` is `APPROVED` with zero open Major findings, every Minor finding fixed or deferred, and `assurance_verdict` is `APPROVED` where section 2.1.1 says Yes (`not-required` otherwise); `.venv/bin/python tools/validate_docs.py` passes on the record itself; up to three author-review iterations per file, then escalation to the owner (section 3.4) |
| Action tracking (SWE-088 c) | Findings live in the record's findings table with state Open, Fixed, Verified or Deferred; a Deferred finding needs an owner decision (decision memo or CR disposition block) naming the gate. The software lead sets `record_status: Closed` only when every finding is Verified or Deferred. On closure each Deferred finding is entered in `docs/reviews/<REVIEW>/rfa-rid-log.json` of its named gate as `RID-<REVIEW>-NNN`, citing the `INSP-NNN` id and the finding id, and is tracked to closure there (charter section 4); the record lists those RID ids in `deferred_rids` |
| Record | One file per review, the filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, which is the single peer-review record (charter section 5) and carries `id: INSP-NNN` in its front matter; there is no `peer-reviews/` folder. `<REVIEW>` is the next gate the product feeds; slugs follow the pattern `requirements-sw-keyer`, `code-keyer-iambic`, `plan-07-software-engineering-plan`. The reviewer copies the checklist template, whose first lines are the unfenced YAML front matter (`id`, `checklist`, `checklist_revision`, `checklist_file` set to the record's own path, `product`, `product_commit` quoted as a string, `reviewer_verdict`, `assurance_verdict`, `verdict`, finding counts and states, `deferred_rids`, the SWE-089 measurements of section 10.3, `record_status`, `date`), answers every item and fills the findings table; the software assurance reviewer adds its verdict, findings and applied SWEHB tasks (`assurance_findings_major`, `assurance_findings_minor`, `assurance_tasks_applied`) to the same file. `tools/validate_docs.py` enforces the location, the front matter and the unique `INSP-NNN` ids. The gate package lists the records completed since the previous gate |

### 10.3 Measurements (SWE-089)

Per inspection record (front matter): product identity and size (lines, requirements or cases), preparation and review effort (agent turns and wall time), findings by severity from the reviewer and from the assurance reviewer, findings fixed, verified and deferred, iterations to `APPROVED`, checklist items answered No. Rolled up per sprint into `docs/plan/measurements.json` (MSR-20 to MSR-23) and analyzed per section 11.3 (defect density trend, review effectiveness = review-found defects divided by review-found plus test-found and field-found defects).

---

## 11. Measurement (SWE-090, SWE-093, SWE-199, SWE-200)

### 11.1 Storage

`docs/plan/measurements.json`: `{"schema": "cwht-measurements-1", "records": [ {"id": "MSR-13", "name": "...", "value": 98.7, "unit": "%", "scope": "cwht-core", "build": "FW-v0.9.0-rc1", "commit": "<sha>", "date": "YYYY-MM-DD", "source": "cargo llvm-cov 0.9.x", "sprint": "SW-07-keyer", "note": ""} ] }`. Appended by `tools/measurements.py` from gate outputs at every sprint closure and release; never edited by hand. TPM-derived values are copied into `docs/plan/tpm.json` by the same script so the SEMP's TPM reporting (SEMP section 7.4) sees them: TPM-010 flash margin (MSR-18), TPM-011 RAM margin (MSR-19), TPM-012 volatility (MSR-02), TPM-013 keyer timing (MSR-24), TPM-003 RFA/RID burndown, and TPM-017 `safety-critical-coverage` (MOP-020: MSR-13 region coverage of safety-critical components, MSR-14 branch and condition coverage, MSR-15 MC/DC table completeness, MSR-17 complexity).

### 11.2 Measurement catalog

| MSR | Measure | Unit | Source | Collected at | Analysis rule and action |
|---|---|---|---|---|---|
| MSR-01 | Software requirements count by level and status | count | `tools/traceability.py` | every sprint, every gate | Draft count must be 0 at the baselining gate |
| MSR-02 | Requirements volatility (SWE-200; TPM-012): V = (added + modified with a Class I change + retired) / count at the previous baseline, per level and per review interval, TBR closures as their own line (counting rule of `docs/process/02-requirements-and-traceability.md` section 10.4) | % | `tools/traceability.py --volatility --from <baseline tag>` (planned, PDR) appends the record to `docs/plan/measurements.json`; `tools/measurements.py` mirrors it to TPM-012 | every gate | Yellow above 10 percent between gates, red above 20 percent: owner review of requirement quality; red opens an RFA |
| MSR-03 | Traceability gaps: requirements without parent, without verification case, design units without `@design`, functions without `@req` | count | `tools/traceability.py` | every gate | Must be 0 at every gate |
| MSR-04 | Open TBR count in software requirements | count | requirements files | every gate | 0 by PDR (L1) and by CDR (L2, including the module files), charter section 7 |
| MSR-05 | Sprint iterations to `APPROVED` per file | count | sprint records | every sprint | Mean above 2 for a sprint triggers a lessons-learned entry and brief revision |
| MSR-06 | Planned versus completed increments and sprints (SWE-024) | count | sprint index | every gate | Slip reported in the package; corrective action recorded |
| MSR-07 | Clippy warnings under the CS-27 set | count | G1 | every gate run | 0 |
| MSR-08 | Miri failures | count | G5 | every release | 0 |
| MSR-09 | `cargo audit` advisories | count | G5 | every release | 0 without a recorded disposition |
| MSR-10 | `cargo deny` violations | count | G5 | every release | 0 |
| MSR-11 | Unsafe sites (blocks, fns, impls) in `pico2` and `api`; unsigned audit entries | count | `cargo geiger`, `tools/unsafe_audit.py` | every release | Unsigned entries 0 at CDR and SAR; growth explained in the VDD |
| MSR-12 | Mutation score of safety-critical modules (optional) | % | `cargo mutants` | CDR, TRR | Reported; no threshold |
| MSR-13 | Line and region coverage per crate (stable) | % | `cargo llvm-cov` | every release | 100 percent of host-compilable code or dispositioned (section 9.5); mirrored to TPM-017 for safety-critical components |
| MSR-14 | Branch coverage of all host-compilable image code and condition coverage of safety-critical components (pinned nightly; required element of the SWE-219 record, never credit-bearing by itself, section 9.6) | % | `cargo +nightly-2026-08-24 llvm-cov --branch` with `-Z coverage-options=condition` | every release (required) | 100 percent of the branches and conditions of every safety-critical decision, or each gap dispositioned in the coverage report as test missing (becomes an independence-pair test) or infeasible condition (owner waiver `W<n>` in the CDR, TRR or SAR decision memo, 01 section 8.6); reported beside MSR-13 and MSR-15; mirrored to TPM-017 |
| MSR-15 | MC/DC decisions with complete independence pairs divided by decisions | % | coverage report table | CDR, TRR, SAR | 100 percent or owner waiver; mirrored to TPM-017 |
| MSR-16 | Stack high-water mark per task (painted stack) and maximum interrupt nesting | bytes; count | painted-stack high-water mark written by the firmware into the event log and read over the diagnostic interface at Bench (dev board at CDR with `credit: false`; `CWHT-A-001` at TRR); nesting is 0 by CS-34 and checked by Inspection | CDR, TRR | Below the design budget with 50 percent margin; red opens an NCR |
| MSR-17 | Cyclomatic complexity: max, mean, functions above 12 and above 15, target-only functions above 1 | count | `rust-code-analysis-cli` | every gate run | Above 15 (or target-only above 1): gate fails unless waived; mirrored to TPM-017 |
| MSR-18 | Flash usage (TPM-010) | bytes and % of 4 MB | link map | every build | Yellow above 25 percent, red above 50 percent (SWE-199 resource margins) |
| MSR-19 | RAM usage `.data + .bss` plus stack budget (TPM-011) | bytes and % of 520 KB | link map | every build | Yellow above 40 percent, red above 60 percent |
| MSR-20 | Peer review defects by severity per product (reviewer and assurance reviewer) | count | INSP records | every sprint | Trend plotted; a module with more than 5 Major findings gets a design re-review |
| MSR-21 | Peer review effort (agent turns, wall time) | count, min | INSP records | every sprint | Trend |
| MSR-22 | Review effectiveness (review-found / all found) | ratio | INSP and NCR records | every gate | Below 0.6 at CDR triggers checklist revision |
| MSR-23 | Test counts: cases defined, `Active`, `Passed`, `Failed`, `Blocked` by class | count | `tools/traceability.py` | every gate | All `Active` HostUnit and Emulation cases `Passed` before TRR |
| MSR-24 | Keyer element timing error and key-to-`PA_EN` latency (TPM-013) | µs | HostUnit on the mock clock (logic, CDR); Bench logic capture (dev board at CDR with `credit: false`; `CWHT-A-001` at TRR and SAR) | CDR, TRR, SAR | Against `REQ-SW-KEYER-*` values; red opens an NCR |
| MSR-25 | Boot-to-safe-state time; off-nominal detection-to-`PA_EN`-low time (SWE-134 j) | ms | HostUnit on the mock clock for the detection-to-command path (CDR); Bench logic capture of `PA_EN`, `TR_TX` and a boot marker from reset (TRR) | CDR, TRR | Against section 14.2 budgets |
| MSR-26 | Worst-case main-loop time, 1 ms tick overruns and worst-case handler duration | µs, count | overrun counter logic in HostUnit (CDR); Bench logic capture of GPIO loop and handler markers and the overrun counter read from the event log (dev board at CDR with `credit: false`; `CWHT-A-001` at TRR) | CDR, TRR | Overruns 0 |
| MSR-27 | NCRs opened and closed by severity, software-attributed | count | `docs/vv/ncr/` | every gate | 0 open S1 at any gate; 0 open S2 at SAR |
| MSR-28 | Build reproducibility: image hash of a clean rebuild equals the release hash | boolean | release script | every release | Must be true |

### 11.3 Analysis procedure (SWE-093)

At every sprint closure and every gate the software lead runs `tools/measurements.py --analyze`, which prints each MSR against its rule, colors it green, yellow or red, and plots trends into `docs/reviews/<REVIEW>/figures/` for the next review package (SEMP section 7.4; `01-lifecycle-and-reviews.md` section 13). Yellow items are listed in the "Software status" section of the next package with the planned action; red items open a corrective action the same day: an NCR (product), an RFA-style item in the package (process), or a risk (`RSK-NNN`). SWE-199 is satisfied by MSR-16, MSR-18, MSR-19 and MSR-24 to MSR-26 tracked against their budgets from the design (estimated) through HostUnit and the dev board (measured) to Bench on `CWHT-A-001` (confirmed). SWE-094 (access for NASA organizations) is not applicable; the owner reads the repository directly.

---

## 12. Nonconformance handling (SWE-201 to SWE-204)

The procedure is `docs/process/04-verification-and-validation.md` section 10 with the template `docs/templates/ncr.md`; records are `docs/vv/ncr/NCR-NNN.md`. Software-specific rules:

1. **Severity levels (SWE-202)** are those of 04 section 10.3 and are repeated here for the software reader; if the two texts ever differ, 04 governs and this plan is corrected by CR.

| Severity | Software meaning |
|---|---|
| S1 Safety or regulatory | A SWE-134 provision violated in a safety-critical component of section 14.1 (keying, PA enable, charging supervision, thermal protection, audio output limiting, the safe-state manager with the configuration guard, the boot path, the scheduler or the clock driver); unintended transmission; emission outside 47 CFR 97.305 or 97.307 from a software cause; battery or thermal hazard from a software cause |
| S2 Mission | A `KDR` or `Baseline` `REQ-SW-*` not met or an `OPS-NNN` cannot be completed with no workaround (for example, iambic paddles or the straight key do not key correctly, SI-018) |
| S3 Workaround | User-visible deviation with an owner-accepted workaround recorded in the operations handbook |
| S4 Other | Cosmetic, documentation, tool or test-infrastructure defect without product effect |

2. **Tools and reused components (SWE-201, SWE-203).** Defects in rustc, cargo tools, the emulator, rustos or the host mocks are NCRs with `cots_assessment_required: true`; the assessment records version, upstream issue, workaround and whether the component stays in the build. At every release the software lead reviews the rustc release notes for the pinned version, RustSec advisories and the issue trackers of the selected emulator and of `rust-code-analysis`, and records the review in the VDD.
3. **Process assessment (SWE-204).** Every S1 and S2 software NCR records which process step let the defect through (requirement, design review, checklist item, test authoring, tool accreditation, CM) and the process change made or why none is needed, in the NCR section 6 and in `docs/lessons-learned.md`.
4. **Traceability (SWE-052).** Each NCR lists `requirement_ids`; `tools/traceability.py` refuses `Verified` while an NCR citing the requirement is open.

---

## 13. Software version description (SWE-063) and release procedure (SWE-085)

Every release, including internal release candidates, gets `firmware/releases/VDD-vX.Y.Z.md` (`VDD-vX.Y.Z-rcN.md` for a candidate), its skeleton written by the release script `tools/release.sh` and completed by the software lead. Identifiers are those of `docs/process/05-configuration-and-data-management.md` section 4.3 and are not redefined here: release id `FW-vX.Y.Z` (semantic versioning), git tag `release/FW-vX.Y.Z` (candidate `release/FW-vX.Y.Z-rcN`), release directory `firmware/releases/vX.Y.Z/`, report front matter form `vX.Y.Z+<short SHA>`.

| VDD section | Content |
|---|---|
| Identification | Version, git tag, full commit hash, build date, builder (machine and user), release type (internal, for test, accepted) |
| Toolchain | `rustc`, `cargo`, `llvm-tools`, `picotool`, `cargo-llvm-cov`, `rust-code-analysis-cli`, `cargo-geiger`, `cargo-audit`, `cargo-deny`, `cargo-nextest` versions; the pinned nightly name and hash (CS-03); the emulator commit if emulation reports are cited; `tools/toolchain.lock.md` commit |
| Components | rustos `api` and `pico2` commit hashes (path dependencies); `cwht-core`, `cwht-app` versions; profile settings (CS-04) |
| Life-cycle data (SWEHB 5.16 item c) | The requirement baseline tag, the design baseline tag, the test case set commit and the traceability report commit that define this version; the generated tables listed by file and size, with the planned-versus-actual result of section 17.4 item e |
| Image | Build command; `SHA-256` of the ELF and the UF2; CRC-32 trailer value; flash and RAM usage (MSR-18, MSR-19); `picotool info` output |
| Requirements | `REQ-SW-*` implemented in this release with status; requirements deferred to a later release |
| Changes | Every approved CR allocated to this release, with its implementing commit (SWE-194); NCRs fixed |
| Known limitations and open items | Open NCRs by severity; waivers (complexity, coverage) with decision memo references; deactivated code list |
| Verification summary | Gate log reference; test counts by class (MSR-23); coverage (MSR-13 to MSR-15); static analysis summary (MSR-07 to MSR-11, MSR-17); regression report reference |
| Reused components | Third-party register snapshot with the SWE-203 advisory review result |
| Installation and regeneration | Flashing procedure (BOOTSEL and UF2 copy, or `picotool load` and `picotool reboot`), the `picotool verify` step, expected first-boot behavior (SafeState then Receive, fault code display if any); regeneration from source with `tools/release.sh --rebuild-check X.Y.Z` (SWEHB 5.16 item e) |
| Approval | Owner decision memo reference (for test at TRR; accepted at SAR) |

Release procedure (the ten steps of `docs/process/05-configuration-and-data-management.md` section 8.1 govern; summary): `tools/sw_gate.sh` exits 0 on the release commit; `tools/release.sh X.Y.Z` builds with the locked toolchain, writes the CRC-32 trailer into the linker-reserved `.image_trailer` section with `tools/image_trailer.py` (CS-32; verified at boot, SWE-134 f), converts to UF2, computes hashes and writes `firmware/releases/vX.Y.Z/` (`cwht-FW-vX.Y.Z.elf`, `cwht-FW-vX.Y.Z.uf2`, `firmware.map`, `picotool-info.txt`, `SHA256SUMS`) and the VDD skeleton; `tools/release.sh --rebuild-check X.Y.Z` rebuilds from `cargo clean` and compares every hash (MSR-28; also PCA-06 at SAR). The image installed on any unit is verified with `picotool verify` against the released ELF and the hash is recorded in `docs/vv/adp/<unit>/as-built.md` (the PCA-05 line).

---

## 14. Safety-critical software (SWE-205, SWE-023, SWE-134, SWE-219, SWE-220)

### 14.1 Safety-critical components

This list is the single authoritative component list of charter section 10. It is regenerated from `docs/safety/hazards.json` (`firmware_role.components` of each hazard) and `docs/process/03-software-classification-and-rmm.md` section 4.3 at every re-run of the determination (PDR, CDR), with the hazard analysis (`docs/safety/hazard-analysis.md` section 6) as the basis. A component is safety-critical when it is traceable to a hazard and meets at least one criterion of NASA-STD-8739.8B para 3.2 as reproduced in SWEHB `7-02` section 1.2, including criterion a, "Causes or contributes to a system hazardous condition/event"; the SWE-205 software assurance task 1 counts contributions by action, inaction or incorrect action. The **safety-critical** components and the modules and units that implement them are:

| Safety-critical function (03 section 4.3; `hazards.json` component) | Module (unit) | Hazards (`hazards.json`) | Basis |
|---|---|---|---|
| Keyer and keying output: straight-key debounce, iambic paddle decoding (modes A and B, dit and dah memories, weighting), element timing, keying-line drive, sidetone gating, stuck-input detection | `SW-KEYER` | HZ-001, HZ-004, HZ-010 | 03 section 4.3 (criteria a, b, c) |
| PA enable and TX sequencer: T/R switching, bias ramp, `PA_EN` gate with prerequisite checks, TX permit, TX time-out, power-step selection and default, tune-carrier level and timeout, receive-only guest lock, low-voltage TX inhibit, charge de-assert before the T/R sequence | `SW-TXSEQ` | HZ-001, HZ-003, HZ-004, HZ-006, HZ-007, HZ-011, HZ-012 | 03 section 4.3 (criteria a, b, c, e) |
| Battery and charging supervision: charger status, dual dissimilar cell-voltage sensing, temperature window, charge disable, insertion check, discharge thresholds and lock-out, charge inhibit during transmit | `SW-PWR` | HZ-002, HZ-007, HZ-011 | 03 section 4.3 (criteria c, e) |
| Thermal protection: PA temperature acquisition, fold-back and inhibit logic | `SW-SAFE` (thermal unit) with `SW-TXSEQ` (actuation) | HZ-003 | 03 section 4.3 (criteria b, e) |
| Audio limiter: output level clamp, default cap and unlock, start-up and mode-change ramps, sidetone amplitude limit, fault mute | `SW-AUDIO` | HZ-005 | 03 section 4.3 (criteria b, c) |
| Safe-state manager: first-start and restart initialization, watchdog handling, fault-to-safe-state transitions, integrity checks of safety-critical state | `SW-SAFE` | HZ-001, HZ-002, HZ-004, HZ-007, HZ-014 | 03 section 4.3 (criteria a, c, e) |
| Boot path to the safe state and image integrity trailer check before any safety-critical output | `SW-BOOT` | HZ-014 | 03 section 4.3 (criteria a, c, e) |
| Configuration guard: two-copy CRC-32 and sequence check of the persisted record, range check of every safety-relevant field (power step, tune level, guest lock, frequency calibration, thermal thresholds, keyer mode, debounce), safe-default substitution, event report; runs in the boot path before any safety-critical output is enabled and before every configuration write commits | `SW-SAFE` (unit `cfg_guard`, called by `SW-BOOT` at boot and by `SW-CFG` before a write) | HZ-014 | 03 section 4.3 configuration guard decision (HZ-014; criteria a, c, e); SWE-219 and SWE-220 apply |
| Scheduler dispatcher: task table, 1 ms tick accounting, dispatch of the monitor tasks (thermal, TX time-out, battery, integrity), overrun detection, and the watchdog-kick decision that kicks only when every monitor task ran within its period | `SW-SCHED` (dispatch logic in `cwht-core`; the loop in `cwht-app`) | HZ-001, HZ-003, HZ-004 and every hazard whose control is a monitor task | Criterion a by inaction: a missed dispatch of the thermal monitor or the TX time-out contributes to HZ-003 and HZ-001; criterion c: the kick decision is part of the watchdog mitigation (SWE-134 j) |
| Drivers these depend on: GPIO (SIO), TIMER alarms, PWM (sidetone and audio level), ADC, watchdog, critical section, and clocks and PLL (TICKS, XOSC, PLL_SYS: every timing budget depends on them) | `pico2` (WP-SW-01, 02, 03, 04, 07, 09, 11) | as the components they serve | 03 section 4.3 drivers row ("inherited"); WP-SW-11 added here on the same basis |

Safety-critical components and units get: CS-16 (no floating point), CS-38 (decisions host-compilable), the software assurance second review of requirements, design, code and tests (section 2.1.1), 100 percent region coverage on the stable toolchain plus the MC/DC analysis of section 9.6 (SWE-219, tailored), CC limit 15 with no waiver (SWE-220), and Test-method verification of every hazard-tracing requirement (SWE-192). The criticality of each design unit is fixed by code unit in `docs/design/software-design.md` (03 section 4.3), so a mission-critical unit inside a safety-critical module (the configuration store inside `SW-CFG`, the envelope and ALC units inside `SW-TXSEQ`) is named as such in the design.

**Mission-critical** components (NPR 7150.2D App. A definition applied in 03 section 4.3 and its section 9 decision record; SWEHB `swe-134-*.md` section 3.1 states that SWE-134 applies to mission-critical software as well): frequency control (`SW-SYNTH`: synthesizer programming, the transmit carrier limits 144.001 to 147.999 MHz of REQ-SYS-008 and REQ-SYS-009 (TBR; ADR-016, ADR-023), calibration data validation); the ALC set-point and keying envelope shaper (HZ-008; units `envelope` and `alc` of `SW-TXSEQ`, unless the architecture ADR at PDR places them in a module of their own); the configuration store (`SW-CFG`: flash read and write of the record and the load of non-safety fields; the guard is safety-critical, above); frequency display rendering and encoder tuning input (`SW-DISPLAY`); and receive-chain control (allocated at PDR to `SW-TXSEQ` for the T/R receive path and `SW-AUDIO` for muting, unless the architecture ADR creates `SW-RXCTL`). Mission-critical components get SWE-134 items a to l as design constraints (section 14.2, mapped per module), the software assurance second review of their requirements, design, code and tests (section 2.1.1), and the general coverage and complexity rules of sections 9.5 and 7.4; SWE-219 and SWE-220 do not apply to them (03 section 4.3). HZ-008 (harmonic and spurious emissions) has no safety-critical firmware role; its SWE-134 items b, g and h are carried by `SW-SYNTH` and the `SW-TXSEQ` envelope and ALC units as mission-critical provisions.

Neither: menu handling and non-frequency display content, the event log view, the diagnostic serial output (`SW-DIAG`), and the engineering tools.

### 14.2 SWE-134 items a to l as cwht design provisions

Each row is a design constraint from PDR and is written as a requirement `REQ-SW-SAFE-NNN` in `docs/requirements/sw/sw-safe/requirements.json` by the requirements author agent in the PDR sprint (ids reserved below; the wording there follows SE HB App. C). Verification is Test: HostUnit for the logic, including its timing on the mock clock; Bench with the Pico-based logic capture for target timing; Emulation only for event order inside `ACC-EMU-001` (ADR-011; section 9.4).

| SWE-134 | Provision in cwht | Reserved requirement | Verification |
|---|---|---|---|
| a. Initialized at first start and restarts to a known safe state | Hardware: `PA_EN` and `TR_TX` are active-high with pull-down resistors so the reset, bootrom and pre-`main` states are "off" (design constraint flowed to `REQ-TX-*` and `ICD-CTL-SW`). Software: the first statements of `cwht-app::main` after the board `take()` drive `PA_EN` low, `TR_TX` low (receive), keyer output idle, charge-inhibit asserted, audio output muted (PWM idle), then start the watchdog; only then are clocks, peripherals, configuration and the display initialized. The same path runs after a watchdog or panic reset. Budget: safe outputs asserted within 5 ms of reset handler entry (MSR-25). | REQ-SW-SAFE-001 | HostUnit: initialization order on the mock; Emulation event-order scenario: safe outputs before any other peripheral write (supporting unless inside ACC-EMU-001); Bench: logic capture of `PA_EN` and `TR_TX` from power-on against the 5 ms budget, pin levels at power-on with the PA jumper open |
| b. Safe transitions between all predefined known states | State machine Boot, SafeState, Receive, TxPending, Transmit, Fault, ChargeInhibited with a transition table in the design; the only path to Transmit is Receive to TxPending (T/R to TX, synthesizer confirmed, settle time elapsed) to Transmit (`PA_EN` high); leaving Transmit always de-asserts `PA_EN` before T/R returns to receive; illegal (state, event) pairs are rejected and logged (CS-20 exhaustive match) | REQ-SW-SAFE-002 | HostUnit transition table tests (every cell); Emulation event-order scenario for the T/R and `PA_EN` order |
| c. Termination to a known safe state | Every termination path (low battery shutdown, over-temperature, fault escalation, operator power-off, panic handler, watchdog expiry, clock fault of CS-37, scheduler overrun) calls `safe_state()` first: `PA_EN` low, T/R receive, keyer idle, charge inhibit asserted, audio muted, in that order; `safe_state()` is written without any fallible call and without loops over data | REQ-SW-SAFE-003 | HostUnit; Emulation event-order scenarios for forced panic and forced watchdog (pin sequence order); Bench |
| d. Operator overrides require at least two independent actions | Transmit needs two independent operator conditions: a key or paddle contact closure and the radio in TX-armed state, which the operator sets by a distinct control action each power cycle (design decides button or menu at PDR, recorded in `ICD-CTL-SW` and the ConOps); the software checks both plus the hardware interlock state. Overriding a protective lockout (thermal fold-back, battery, TX time-out), if the PDR ADR offers an override at all, requires two independent actions on two different controls (a menu confirmation plus a physical key or button action, 03 section 5 item d), is time-limited, and is logged | REQ-SW-SAFE-004 | HostUnit: key closure alone never enables `PA_EN`; Bench demonstration by the owner |
| e. Rejection of out-of-sequence commands where the sequence matters | `PA_EN` request rejected unless T/R is commanded TX and the settle timer has expired and the synthesizer lock or write-back check passed; charge enable rejected unless battery voltage and temperature prerequisites passed in the last sample; configuration write rejected unless preceded by the unlock gesture within 10 s; rejections are counted in the event log | REQ-SW-SAFE-005 | HostUnit sequence tests, nominal and each permutation |
| f. Detects inadvertent memory modification and recovers | Safety-critical flags in RAM are stored with their bitwise complement and checked before each use and every 1 ms tick; the configuration RAM copy is CRC-32 checked every 100 ms; the image CRC-32 trailer is checked at boot; the `SW-SCHED` task table is a `const` in flash; on any mismatch: `safe_state()`, reload from flash (two copies with CRC), log event, and if the mismatch repeats within one power cycle enter Fault | REQ-SW-SAFE-006 | HostUnit with mocked corruption injection; Emulation memory-poke event-order scenario |
| g. Integrity checks on inputs and outputs | Inputs: key and paddle debounce with the make and open times of `REQ-SW-KEYER` (HZ-010: 2 ms make, 5 ms open, TBR, fixed at PDR) and rate plausibility (an element shorter than the debounce make time or a key-down longer than the TX time-out is treated as a fault or ignored per design), encoder step range, ADC readings against physical ranges with stuck-value detection, I2C/SPI reads verified by length and where the device allows by read-back of written registers. Outputs: `PA_EN` and `TR_TX` pin states read back through SIO after each write and compared to the commanded state; synthesizer frequency registers read back before `PA_EN`; mismatch is a fault | REQ-SW-SAFE-007 | HostUnit off-nominal cases; Emulation with device models returning wrong values (event order); Bench logic capture for the debounce times |
| h. Prerequisite checks before safety-critical commands | Before `PA_EN` high: keyer state valid, carrier frequency inside 144.001 to 147.999 MHz (REQ-SYS-009, TBR), temperature below the PA limit, battery above the transmit minimum, charger not in fault and charge enable de-asserted (HZ-011), T/R in TX and settled, TX-armed, guest lock not set (HZ-006), TX time-out timer not expired, duty-cycle budget not exceeded, no open Fault; the check list is a single function with one decision per prerequisite (MC/DC table) | REQ-SW-SAFE-008 | HostUnit: each prerequisite false alone blocks; all true permits |
| i. No single software event or action initiates a hazard | Two software outputs (`PA_EN` and `TR_TX`) in the correct states and the keyed RF drive are all required for emission, and `PA_EN` itself needs both a keyer key-down event and the separately maintained PA-permit flag of the safe-state manager, each refreshed periodically (03 section 5 item i); a single GPIO write or a single corrupted flag cannot produce RF (fault tree per hazard in the hazard analysis shows at least two independent events). Outside software, the hardware PA-enable cutoff, the external pull-downs and the fail-safe T/R relay bound any software fault (`hazard-analysis.md` section 7 item i). Charging: the charger IC's own voltage, current and temperature limits are independent of software; software can only inhibit. Thermal: the hardware over-temperature cut (if the hazard analysis requires one) is independent of software | REQ-SW-SAFE-009 | Analysis (fault tree) plus HostUnit fault-injection tests; Bench timing of the hardware cutoff |
| j. Responds to off-nominal conditions within the time needed to prevent a hazard | Budgets (initial allocation; the values are confirmed by the thermal and electrical analyses `TS-NNN` at PDR and written into the requirement): PA over-temperature detected and `PA_EN` low within 100 ms of threshold crossing (temperature sampled at 20 Hz); PA over-current or reflected-power fault (if sensed) to `PA_EN` low within 10 ms; key-up to `PA_EN` low within 2 ms; TX time-out at 60 s continuous key-down; battery under-voltage to shutdown within 1 s; watchdog 100 ms, kicked only when every monitor task ran in its period (`SW-SCHED`) | REQ-SW-SAFE-010 | HostUnit on the mock clock for the detection-to-command logic and the kick decision; Bench logic capture on `CWHT-A-001` against each budget (MSR-25), with the dummy load |
| k. Error handling | Every fallible call handled per CS-13 with a documented response class: retry (bounded), degrade (feature off, event logged, display code), safe state (Fault), or reset (watchdog). The error taxonomy and the response per error are a design table; no error is silently discarded | REQ-SW-SAFE-011 | HostUnit: each error variant exercised; review CS-13 |
| l. Can place the system into a safe state | `safe_state()` (PA off, receive, key up, charge off, audio muted) callable from any context (task, interrupt, panic handler); also reachable by the operator by holding the power or a designated control for 2 s; SafeState is displayed as a fault code and left only by operator action (power cycle or acknowledge) | REQ-SW-SAFE-012 | HostUnit from every state; Emulation event-order scenario from each state (supporting); Bench demonstration |

The twelve rows are the shared provisions written into `SW-SAFE`. Each other safety-critical and mission-critical module or unit carries the SWE-134 items below as module requirements in its own file, referencing the `REQ-SW-SAFE-NNN` row it specializes. For hazard-derived rows the items are the union of `swe134_items` of the hazards the module controls (`docs/safety/hazards.json`); for the scheduler, the clock driver and the mission-critical rows they are the items this plan allocates:

| Module or unit | Items applied | Module-specific provision |
|---|---|---|
| `SW-KEYER` (HZ-001, HZ-004, HZ-010) | a, b, c, d, f, g, h, i, j, k, l | Keyer output idle at boot and after any reset (a); straight-key and iambic states as one `match (state, event)` covering both key types (b); every termination path leaves the keying line idle (c); the key contact is one of the two independent transmit conditions (d, i); dit and dah memories and the key-down state stored with their complements (f); debounce with the REQ-SW-KEYER make and open times, stuck-input detection and jack-detect range checks (g, HZ-010); key-down forwarded only when the keyer state is valid (h); key-up to keying-line idle within the REQ-SW-SAFE-010 budget (j); keyer errors force key up (k, l) |
| `SW-TXSEQ` (HZ-001, HZ-003, HZ-004, HZ-006, HZ-007, HZ-011, HZ-012) | a to l | The twelve shared rows, plus: power step defaults to the lowest step at boot and a higher step needs a deliberate action (HZ-006, d); the guest lock blocks `PA_EN` in the prerequisite function (HZ-006, h); low-voltage TX inhibit (HZ-007, h, j); charge enable de-asserted before the T/R changeover (HZ-011, e, j); tune carrier is time-limited (HZ-012, j) |
| `SW-PWR` (HZ-002, HZ-007, HZ-011) | a, b, e, g, h, j, k, l | Charge enable de-asserted at boot (a); charger and cell states as an explicit state machine (b); charge enable refused unless temperature and voltage prerequisites passed (e, h); charger and cell readings range- and plausibility-checked against the charger's own status and the second divider path (g); charge disable within 1 s of a fault and before any T/R-to-TX sequence (j, HZ-011); errors escalate to charge off (k, l) |
| `SW-AUDIO` (HZ-005) | a, b, d, g, j, k, l | Audio output starts muted and ramps up over 50 ms after the first valid state (a); gain and sidetone amplitude are a state machine with a clamp value that no input path can exceed (b, g); raising the level above the default limit needs two actions (d); a PA fault or SafeState mutes within 10 ms (j, l); every audio driver error mutes (k). Budgets confirmed by the audio analysis at PDR. |
| `SW-SAFE` thermal unit (HZ-003) | d, g, h, j, l | Thermal fold-back override only per row d; thermistor reading range- and stuck-checked (g); temperature below the inhibit limit is a `PA_EN` prerequisite (h); detection to `PA_EN` low within 100 ms (j); over-temperature enters SafeState on repeat (l) |
| `SW-SAFE` configuration guard unit `cfg_guard` (HZ-014) | a, b, c, f, g, h, k, l | Safe defaults substituted for any invalid safety-relevant field at boot (a); guard result states (accepted, defaulted, both copies corrupt) as an explicit enum (b); a failed guard at boot ends in SafeState until defaults are loaded (c); two-copy CRC-32 and sequence check (f); range check of every safety-relevant field (g); the guard runs before any safety-critical output is enabled and before every write commits (h); every guard failure is logged and a repeat within one power cycle enters Fault (k, l) |
| `SW-BOOT` (HZ-014) | a, b, c, f, g, h, k, l | Image CRC-32 trailer verified before any safety-critical output is enabled (f, h); the configuration guard runs before any safety-critical output (h); a rejected image enters SafeState with a fault code (c, l) |
| `SW-SCHED` (safety-critical by criterion a, section 14.1) | a, c, f, j, k, l | Dispatch starts only after the row a safe outputs are asserted (a); a scheduler fault terminates through `safe_state()` (c); the task table is a flash `const` and per-task last-run timestamps are complement-stored (f); every monitor task dispatched within its period, and the watchdog kicked only when all ran (j); a tick overrun or a missed monitor deadline is an error with response class safe state (k, l) |
| `pico2` clocks and PLL (WP-SW-11) | a, g, j, k | TICKS enabled explicitly before TIMER0 and watchdog use (a, CS-37); XOSC `STABLE` and PLL `LOCK` status read back (g); waits bounded by a TIMER0-independent timeout (j); timeout returns a clock fault that leaves the safe outputs asserted (k, CS-37) |
| `SW-SYNTH` (mission-critical; HZ-008 items b, g, h) | b, g, h, k | Synthesizer states (unprogrammed, programming, locked, fault) as an explicit state machine (b); registers read back and lock detect checked after every write (g); the transmit carrier limits of REQ-SYS-009 enforced before every synthesizer write and independently of the display (h; ADR-016); every bus error handled and makes the `PA_EN` frequency prerequisite false (k) |
| `SW-TXSEQ` units `envelope` and `alc` (mission-critical; HZ-008 items b, g, h) | b, g, h | Envelope ramp as a state machine that completes the fall before `PA_EN` drops (b); the ALC forward-power reading range- and plausibility-checked (g); the ALC set-point checked against its limits before every write (h) |
| `SW-CFG` configuration store (mission-critical; HZ-014 via the guard) | a, f, k | The store holds no record until the guard accepts one (a); two copies with CRC-32 and a sequence number maintained by the store and checked by the guard (f); flash erase and program errors retried a bounded number of times, then the previous copy is kept and the event logged (k) |
| `SW-DISPLAY` (mission-critical) | g, k | Encoder deltas range-checked; the displayed frequency is rendered from the value written to the synthesizer, never from the tuning request (g); display bus errors handled with a bounded retry and a fault code (k) |

### 14.3 Cyclomatic complexity (SWE-220) and coverage (SWE-219)

Sections 7.4 (CS-17, CS-38) and 9.6. Any exceedance or shortfall on a mission-critical or other component is waived only by the owner in a decision memo and is listed in the VDD; no waiver is planned for a safety-critical component or unit.

---

## 15. Software assurance and safety (SWE-022, SWE-023 as tailored)

Software assurance is performed by the software assurance reviewer role (section 2.1; charter section 2) on the products the table of section 2.1.1 marks Yes, using the four checklists of section 10, the safety items of section 14, and the `# 7. Software Assurance` section (7.1 tasking, 7.2 products) of the SWEHB page for each SWE the product implements (`docs/references/md/swehb/swe-NNN-*.md`; present for all 130 SWEs, checked 2026-09-25). The dedicated checklist `docs/templates/peer-review-checklist-software-assurance.md` that `08-agent-briefing.md` section 3.5 schedules before PDR consolidates those SWEHB tasks; until it exists the assurance reviewer applies the SWEHB sections directly and records which tasks were applied in the `assurance_tasks_applied` field of the product's record (section 10.2).

This section is the software assurance plan (NPR 7150.2D §6.1 item k) and, with section 14 and `docs/safety/hazard-analysis.md`, the software safety plan (item l). SWEHB 5.17 and 5.18 minimum content is satisfied as follows:

| SWEHB 5.17 (SA plan) or 5.18 (safety plan) item | Where |
|---|---|
| 5.17 items 1 to 3, 5.18 item 2.5: assurance activities and methods | Second review of the products of section 2.1.1 written into the product's `INSP-NNN` record; confirmation of every firmware NCR severity (04 section 10.3); verification of sprint acceptance criteria (section 3.4 Phase 4); audit of `firmware/unsafe-audit.md` at CDR and SAR; reading of the gate log to confirm that run-for-record executions used the tagged release; static analysis results review (section 8); hazard-tracing test review (SWE-192); a "Software assurance findings" section in every review package |
| 5.17 items 4, 5, 12, 5.18 items 2.1 to 2.4, 2.6: stakeholders, roles, resources, communication | Sections 2.1 and 2.1.1 (owner as SMA TA; assurance reviewer as an independent invocation distinct from the file reviewer); resources are the corpus, the repository and the tools of section 8; communication is the `INSP-NNN` record and the review package |
| 5.17 item 6, 5.18 item 3: products and storage | The assurance fields of the `INSP-NNN` records, NCR severity confirmations, the "Software assurance findings" package section, the signed MC/DC tables (section 9.6); stored in `docs/reviews/<REVIEW>/checklists/` and `docs/vv/` under configuration control (05), retained for the life of the repository |
| 5.17 item 7: acceptance criteria for SA products | An `INSP-NNN` record is complete per section 10.2; an NCR severity confirmation is recorded in the NCR; a coverage report is signed only with every decision table complete or dispositioned |
| 5.17 items 8, 9, 5.18 item 1: safety-critical assessment and classification | Section 14.1; `docs/process/03-software-classification-and-rmm.md` sections 3 and 4, independent concurrence per its section 3.3, re-run at PDR and CDR |
| 5.17 item 10: risk management of SA-identified risks | Section 21; `docs/risk/register.json` entries opened by the assurance reviewer carry tag `assurance` |
| 5.17 item 11, 5.18 item 5: training | Section 2.2 required reading (SWE-017 as tailored) |
| 5.17 item 13: SA requirements mapping and tasking | `docs/process/rmm.json` rows plus the SWEHB section 7.1 tasks applied per product (`assurance_tasks_applied`); the tailoring of tasks that presuppose Center SMA is recorded in the RMM rows SWE-022 and SWE-023 |
| 5.17 item 14: SA metrics | MSR-20 to MSR-23 and MSR-27 (section 11) |
| 5.17 item 15: issue tracking | Section 12 (NCRs); `INSP-NNN` finding states and the RID entries of deferred findings (section 10.2); RFA/RID logs (charter section 4) |
| 5.17 items 16 and 17, 5.18 items 6 and 7: acronyms and glossary | Annex D of this plan (acronyms and plan-specific terms); SEMP Appendix A (`docs/plan/semp.md`, project glossary) |
| 5.17 items 18 and 19, 5.18 items 4, 8 and 9: change history, schedule, references | Change procedure and history in section 23; assurance activities tied to the gates and sprints (section 3), schedule per `docs/plan/schedule.md`; hazard analysis re-evaluation at PDR and CDR (03 section 4.1 step 5); references in the header, section 1 and charter section 1 |

Software safety analysis is the hazard analysis with software controls traced (`hazard_ids`, `control_req_ids`, SWE-052) and tested (SWE-192), plus the fault trees of section 14.2 item i. NASA-STD-8739.8 itself is not in the corpus; its safety-critical definition is applied through SWEHB `7-02` section 1.2 and its SA tasking through the SWEHB section 7 tabs; the RMM rows SWE-022 and SWE-023 stay dispositioned T until the standard is obtained and mapped (charter section 1).

---

## 16. Cybersecurity (SWE-154, SWE-156, SWE-157, SWE-159, SWE-185, SWE-207, SWE-210; charter section 12 tailoring)

### 16.1 Scope and assumptions

The radio has no network interface, no radio data reception path (CW is decoded by the human operator; the firmware never decodes or acts on received audio), no remote command capability and no user-installable software. Physical possession of the unit is required for every attack surface below. Agency security policies (NPR 2810.1, NASA-STD-1006) presuppose networked or commanded space systems and are tailored to the physical-interface protections here; the owner holds the CIO co-approval role for section 3.11 rows in the RMM.

### 16.2 Assets, attack surfaces, risks and mitigations (SWE-154, SWE-156)

| Asset | Surface | Threat | Likelihood and consequence (5x5 inputs for `RSK-NNN` tagged `cyber`) | Mitigation (design provision and requirement) |
|---|---|---|---|---|
| Firmware image integrity | USB bootrom loader (BOOTSEL, UF2 or `picotool`) | A tampered or wrong image is loaded by someone with physical access, or by the owner by mistake, producing unsafe keying or emission | L2, C4 (S1 outcome possible) | Image CRC-32 trailer verified at boot before any safety-critical output (CS-32); hash published in the VDD and verified with `picotool verify` after every flash; only files from `firmware/releases/` are flashed; RP2350 secure boot (signed images, irreversible OTP) is evaluated in an ADR at PDR and is not enabled in Rev A unless the owner decides otherwise, because it cannot be undone (RSK-015) |
| Persisted configuration and calibration | Flash sectors read at boot | Corrupted or maliciously written values (speed, frequency calibration, TX-arm default) | L2, C3 | Two copies with CRC-32 and sequence number, the configuration guard's field range checks, defaults on double failure, event logged (CS-29, CS-32; SWE-193 cases; RSK-015) |
| Keying and control inputs | Key/paddle jack, encoder, buttons | "Command injection": a crafted signal on the key line causing unintended state change or emission | L1, C4 | The key line feeds only the keyer state machine (CS-30); no gesture on the key line changes configuration; debounce, rate limits and TX time-out (SWE-134 g, j); two independent actions to transmit (SWE-134 d) |
| Debug access | SWD pads on the PCB | Firmware extraction or live modification with physical access | L1, C2 | No SWD header populated in delivered units; the enclosure closes the pads; OTP debug disable is an ADR option (irreversible, off by default for Rev A); event log records unexpected resets |
| Diagnostic interface | UART header (or USB CDC if the PDR ADR selects it) used to read the event log | Injection of commands | L1, C2 | Read-only protocol except `reboot` (CS-33); not populated in delivered units unless the owner requests it |
| Build and supply chain | rustup-distributed toolchain, rustos, dev-tool crates, the vendored emulator | Compromised toolchain or dev dependency inserting code into the image | L1, C4 | Toolchain from rustup with its signed manifests, exact version pinned and hash-checked at accreditation; zero runtime crates (CS-02); `cargo audit` and `cargo deny` on every gate (SWE-185); reproducible build check (MSR-28); rustos is owner-developed and reviewed under this plan; the emulator never touches the image |

Residual risks are entries in `docs/risk/register.json` tagged `cyber`, reviewed at every gate.

### 16.3 Communications protection (SWE-157 as tailored)

cwht's only communications capability is a manually keyed CW transmitter with no command reception; NASA-STD-1006 protections reduce to the physical-interface controls above and the no-remote-command design (CS-30).

### 16.4 Cybersecurity verification (SWE-159, SWE-185)

Cases `TC-SW-BOOT-*` (corrupt image trailer refused; correct image accepted), `TC-SW-CFG-*` (corrupt copy A, corrupt both, out-of-range fields), `TC-SW-KEYER-*` (key-line flood, glitches shorter than the debounce make time, stuck key to time-out), `TC-SW-DIAG-*` (command injection on the diagnostic interface has no effect), and the static analysis gate G5 as the SWE-185 verification of the secure coding rules. These cases are part of the regression set (section 9.3).

### 16.5 Detection data (SWE-210 as tailored)

`SW-DIAG` keeps a persistent event log (ring buffer in flash, CRC-protected records: boot count, reset cause including watchdog and brown-out, image CRC result, configuration load result and copy used, safety rejections per SWE-134 e and h, panic markers, Fault entries with code, the painted-stack high-water mark and the tick overrun counter of MSR-16 and MSR-26). The operator reads it from the display's diagnostic page and, if populated, the diagnostic serial interface; the operations handbook tells the owner how to report anomalies (Phase E NCR).

### 16.6 Privacy (SWEHB 5.08 item 7)

The firmware collects and stores no personal data. The event log holds device events only (the records of section 16.5) and no operator identity, call sign, location, contact log or received content; the configuration record holds radio settings only. No data leaves the unit except over the read-only diagnostic interface to a person holding the unit. A requirement or CR that would add any personal data field (for example a stored call sign) is a Class I change that adds a privacy row to section 16.2 before it is approved.

---

## 17. Third-party software, make/buy, tool accreditation and auto-generated code

### 17.1 Third-party software register (SWE-027 as tailored, SWE-211, SWE-203)

Policy: **zero external crates in the flashed image**. The image consists of `cwht-app`, `cwht-core`, rustos `api` and `pico2`, and Rust `core` (the only non-owner code compiled in). Dev tools may use pinned OSS crates. Every entry below records SWE-027 items a to f; item c (Center IP counsel) is tailored: the owner reviews licenses; all accepted licenses are permissive.

| Component | Version and pin | In image | a. Requirements met | b. Documentation | c. License | d. Support plan | e. V&V to developed-code level | f. Defect assessment |
|---|---|---|---|---|---|---|---|---|
| Rust `core` library (with rustc) | rustc 1.98.0 stable, `rust-toolchain.toml` | yes | Language runtime for all `REQ-SW-*` | rust-lang docs | MIT or Apache-2.0 | Rust project 6-week releases; version change by CR | Compiled into every host test; toolchain accreditation (section 17.3) | rustc release notes and RustSec reviewed per release (VDD) |
| rustos `api` | path `../rustos/api`, commit `c54d35a` at this revision (`tools/toolchain.lock.md` section 3), commit pinned in every VDD | yes | `REQ-SW-HAL-*` trait contracts | rustos `README.md`, `cargo doc` | No `LICENSE` file and no `license` manifest field exist in rustos at `c54d35a` (verified 2026-09-25); every line is the owner's, so cwht's use is unencumbered; the owner adds a license file (open question `OQ-SW-001`, due PDR) and `firmware/THIRD-PARTY-NOTICES.md` records it | Owner-developed; changes by CR and the section 19 work packages under this plan | Contract tests, host tests, dev-board checks | NCRs with `cots_assessment_required` (section 12 item 2) |
| rustos `pico2` | path `../rustos/firmware/pico2`, same commit | yes | boot, vector table, reset, drivers per section 19 | same, plus RP2350 ICDs under `rustos/docs/icd/rp2350/` | same | same | HostUnit on the host-compilable decision functions (CS-38), dev-board checks per peripheral, Bench, driver-to-datasheet Inspection, unsafe audit | same |
| RP2350 emulator (selected by the PDR emulator ADR: c1570/rp2350js ARM mode at `af0114cb`, the `ACC-EMU-001` candidate, or Renode as fallback; ADR-011) | commit pinned by the ADR | no (dev tool) | Emulation evidence class, event order only (section 9.4) | repository README and the accreditation study `docs/research/emulator-accreditation-and-timer-irq.md` | recorded by the PDR emulator ADR before vendoring | Single-maintainer project with no maintenance commitment (candidate); pinned, vendored with a mirror fork per the ADR; fallback in section 9.4 item 6 | `ACC-EMU-001` register-visible sequence agreement per in-scope peripheral (section 9.4 item 4) | Repository issues reviewed per release (section 12 item 2) |
| `cargo-llvm-cov`, `cargo-nextest`, `cargo-geiger`, `cargo-audit`, `cargo-deny`, `rust-code-analysis-cli`, `cargo-mutants` (optional) | versions in `tools/toolchain.lock.md` | no (tools) | SWE-135, SWE-186, SWE-189 measurement | crate docs | MIT or Apache-2.0 | `cargo install --locked`, pinned; change by CR | Sanity checks (section 8.3) | RustSec and release notes per release |
| `picotool` | 2.3.0 (Homebrew) | no (tool) | Image conversion, flashing, verify | Raspberry Pi docs | BSD-3-Clause | Homebrew pin | `verify` detects a seeded byte change | Release notes per release |
| Python venv packages (`jsonschema`, `requests`, `bs4`, `markdownify`, `lxml`) | `tools/requirements.txt` | no (tools) | Document validation and rendering | PyPI docs | MIT, Apache-2.0, BSD | pinned | `tools/validate_docs.py` exits non-zero on seeded faults | PyPI advisories per release |

Any proposal to add a runtime crate is a CR with a trade study; the default answer is to implement the function in `cwht-core` or rustos.

### 17.2 Make/buy assessment (SWE-033)

Recorded as trade study `TS-NNN` "Firmware runtime and HAL" (SRR entrance product): alternatives (owner's rustos; `rp-hal` plus `cortex-m-rt`; Embassy; RTIC) scored on the owner's direction SI-007, auditability of every line (Class A intent), unsafe surface, dependency count, testability through traits on the host, and effort for the missing drivers (section 19). The owner's direction fixes rustos; the trade study records the cost of that choice (the work packages) and the benefits (zero external crates, complete audit).

### 17.3 Toolchain accreditation (SWE-136, SWE-070)

Rev A accredits upstream stable rustc as installed by rustup, at one exact version, by the sanity checks of section 8.3 plus: reproducible rebuild of the release (MSR-28), byte-identical rebuild of the rustos blinky, and the HostUnit suite passing twice with identical results on the release commit; the record is `docs/cm/tool-validation/TV-NNN-rustc.md` (due PDR, `tools/toolchain.lock.md` section 5). Ferrocene is recorded as an option with its target-tier facts (section 8.1) in the accreditation ADR; it is not adopted for Rev A.

### 17.4 Auto-generated code (SWE-146, SWE-206)

No SVD-generated peripheral access crate is used: register layouts are hand-written in `pico2` from the datasheet with citations, as the existing GPIO driver is (the RMM row SWE-146 states the same). The only permitted generation is `build.rs` table generation in `cwht-core` (for example sidetone waveform or timing tables) from owner-written Python or Rust generator scripts committed under `firmware/cwht-core/gen/`: a. generators are validated by a unit test comparing generated tables to hand-computed values; b. and g. generator inputs, scripts and outputs are configuration items; c. scope is limited to constant tables generated from `firmware/cwht-core/gen/`; d. generated code passes the same lints, review and tests; e. at each release the software lead compares the generated files listed in the VDD (file and size) with the item c scope and records the result in the VDD "Life-cycle data" section; any generated file outside that scope (not a constant table, or not produced from `firmware/cwht-core/gen/`) is an NCR; f. manual edits to generated output are prohibited, changes go to the generator. The owner has repository access to all inputs (SWE-206).

---

## 18. Software acceptance criteria concept (SWE-034, SWE-194)

The baselined criteria are the "Acceptance" section of `docs/vv/plan.md` (PDR); the per-requirement criteria are the `acceptance_criteria` fields of the `TC-SW-*` cases. The software is accepted at SAR when all of the following hold on the release installed in `CWHT-A-001` and confirmed by the physical configuration audit:

1. Every `REQ-SW-*` is `Verified` on the credited report of the accepted release and its PCA-05 line (`docs/vv/adp/CWHT-A-001/as-built.md`) names that release, so it moves to `Closed` at SAR with the owner's acceptance (charter section 9; 04 section 5.3); or it is dispositioned by an approved CR (waived or deferred to Rev B with owner memo); `tools/traceability.py` exits 0.
2. Every SWE-134 provision (`REQ-SW-SAFE-001` to `-012`) is `Verified` by Test, with Bench confirmation on the delivered unit.
3. Every approved CR allocated to this release is implemented and listed in the VDD Changes section with its implementing commit (SWE-194 "all approved changes have been implemented").
4. Zero open S1 or S2 software NCRs; every S3 has a handbook workaround; S4 listed in the VDD (SWE-194 defects designated for resolution).
5. Coverage per section 9.5 and 9.6 met, or waived by the owner with rationale in the SAR memo.
6. Static analysis gate G5 clean; unsafe audit fully signed; complexity limit met or waived.
7. Every code file, design section, requirement file and test case has a peer review record with `verdict: APPROVED` (section 10.2).
8. VDD issued for the accepted version; the flashed image hash equals the VDD hash (`picotool verify`).
9. Validation scenarios completed by the owner (SEMP section 5.8: straight-key QSO, paddle QSO at two speeds with the internal keyer, battery-life run, hand-over to a friend using the handbook alone), recorded as `TC-VAL-*` reports.
10. The operations handbook covers flashing, keyer settings, fault codes and anomaly reporting.

---

## 19. rustos driver work packages needed by cwht

rustos today provides boot, vector table, reset handler, linker script, board definition and a GPIO driver (`Rp2350Gpio`, inputs and outputs). cwht needs the following additions, each delivered as a sprint of section 3.4 with the file inventory of section 3.5 (trait in `api`, implementation in `pico2` with datasheet citations and host-compilable decision functions per CS-38, mock in `cwht-hal-mock`, contract tests, dev-board check, and for peripherals inside the `ACC-EMU-001` candidate scope the register-sequence comparison of section 9.4 item 4). Coordination with the owner as rustos maintainer (SI-033, ADR-019): each WP is proposed as an ADR in cwht and merged into rustos on the owner's approval. Every WP follows the target platform rules CS-34 to CS-37.

| WP | Driver | RP2350 block | `api` trait to add | Used by (cwht) | Register ICD available in rustos | Needed by |
|---|---|---|---|---|---|---|
| WP-SW-01 | Time base and alarms | TIMER0 (1 µs tick, 64-bit), alarm interrupts | `Clock` (monotonic `now_us`), `Alarm` (one-shot at absolute time with handler) | keyer element timing (ALARM0), 1 kHz input sampling and the scheduler tick (ALARM1), sequencing delays, watchdog kick cadence | no (extract `rustos/docs/icd/rp2350/timer/` from the datasheet as part of the WP) | FW-B1 |
| WP-SW-02 | GPIO input sampling through SIO | SIO `GPIO_IN` (no IO_BANK0 edge interrupts, CS-35) | `GpioPinIn::read()` exists; add a batched `SioInputs::snapshot()` returning all input levels in one SIO read | key, paddle dit and dah, encoder A/B, buttons, jack detect, sampled at 1 kHz from the ALARM1 handler | yes (`gpio/`) | FW-B1 |
| WP-SW-03 | PWM | PWM slices 0 to 7 and channels (CS-36) | `PwmOutput` (frequency, duty, enable) | sidetone audio, LCD backlight, optional bias or AGC control | no (extract `pwm/`) | FW-B1 |
| WP-SW-04 | ADC | ADC with round-robin and FIFO, temperature sensor | `AdcChannel::read()` with conversion to millivolts and a stuck-value flag | battery voltage, PA temperature, PA current or forward/reflected power (if sensed), VSYS | no (extract `adc/`) | FW-B1 |
| WP-SW-05 | I2C master | I2C0/I2C1 | `I2c` (write, read, write-then-read, with timeout and error enum) | synthesizer or LCD depending on the PDR selection | yes (`i2c/`) | FW-B1 |
| WP-SW-06 | SPI master | SPI0/SPI1 | `Spi` (transfer, write, with chip-select handle) | LCD, synthesizer or DAC per PDR selection | yes (`spi/`) | FW-B1 |
| WP-SW-07 | Watchdog | WATCHDOG (timeout, kick, reset cause), scratch registers | `Watchdog` (start, kick, cause) | SWE-134 a, c, j; reset cause into the event log | no (extract `watchdog/`) | FW-B1 |
| WP-SW-08 | Flash write | QMI/XIP via bootrom flash functions (`flash_range_erase`, `flash_range_program`) with XIP disabled during the operation | `FlashStore` (erase sector, program page, read) | configuration copies A/B, event log ring | no (bootrom API section of the datasheet) | FW-B2 |
| WP-SW-09 | Critical section and NVIC helpers | PRIMASK, NVIC enable (no priority writes, CS-34) | `critical_section::with`, `Interrupt::enable()` with no priority argument: every enabled interrupt keeps the single reset priority | all interrupt-using drivers; CS-09 | partial (vector table in `lib.rs`) | FW-B1 |
| WP-SW-10 | UART | UART0 | `Read<u8>`, `Write<u8>` (already in `api::common`) implementation | diagnostic serial (if the PDR ADR selects UART) | yes (`uart/`) | FW-B2 |
| WP-SW-11 | Clocks and PLL configuration (safety-critical, section 14.1) | CLOCKS, PLL_SYS, XOSC, TICKS | `pico2::clocks::init(config) -> Result<(), ClockFault>` (no trait; boot-time): TICKS enabled explicitly, XOSC and PLL waits bounded with a fault path (CS-37) | system clock at 150 MHz, peripheral clocks for PWM and ADC accuracy, TIMER0 and watchdog ticks | yes (`clocks/`) | FW-B1 |
| WP-SW-12 | CRC-32 | software implementation in `cwht-core` (no DMA sniffer dependency) | none (pure function) | image trailer check, configuration and event log records | not applicable | FW-B2 |
| WP-SW-13 (optional) | USB CDC device | USB controller | `Read<u8>`, `Write<u8>` | diagnostic serial over USB if the PDR ADR selects it instead of UART; large effort, recommended against for Rev A | no | Rev B unless ADR says otherwise |

Every WP row is closed only when: contract tests pass against the mock, the dev-board check report is filed (`credit: false`), the register-sequence comparison for `ACC-EMU-001` is recorded for in-scope peripherals (or the row states the peripheral is outside the scope), the unsafe audit entries are signed, and the `api` docs describe the trait's error type and invariants in the rustos house style.

---

## 20. Operations, maintenance and retirement (SWE-075, SWE-077, SWE-194, SWE-195, SWE-196)

Operations: `docs/ops/operations-handbook.md` (SAR product) covers normal use, keyer settings, fault codes, flashing and verification, anomaly reporting. Delivery (SWE-077): the SAR hand-over package `docs/reviews/SAR/` and per-unit `docs/vv/adp/<unit>/`. Pre-delivery verification (SWE-194): section 18 items 1 (requirements met or dispositioned), 3 (every approved change implemented, listed in the VDD Changes section), 4 (defects designated for resolution resolved) and 8 (released image installed). Maintenance (SWE-195): Phase E changes follow this plan unchanged (CR, sprint, peer review, gate, regression, VDD, delta TRR before bench, owner approval); a friend's anomaly report becomes an NCR filed by the owner. Retirement (SWE-196): the archive is the git repository with its annotated `baseline/*` and `release/*` tags (signed once the owner configures a key, charter section 8), `firmware/releases/`, `tools/toolchain.lock.md` and the rustup toolchain version named so it can be reinstalled; access is repository access; retention for the life of the repository (`docs/process/05-configuration-and-data-management.md`).

---

## 21. Software risks (SWE-086)

Registered in `docs/risk/register.json` by the software lead (ids assigned by the register; rows without an id are opened at SRR), each with a mitigation owner and review gate:

| Risk | Scenario | Mitigation |
|---|---|---|
| MC/DC tooling gap (RSK-010) | No compiler support for MC/DC in Rust; manual tables cost effort and may miss a decision | Section 9.6 method; CS-17, CS-20 and CS-38 keep decisions small and host-compilable; second review of tables; MSR-14 branch and condition coverage as the tool cross-check; re-evaluate at each gate against the 2026 project goal |
| Emulator fidelity (RSK-003) | The `ACC-EMU-001` candidate is a single-maintainer project with known gaps (seconds not modelled, GPIO edge interrupts mis-decoded, NVIC priorities at wrong offsets; ADR-011 section 1) | Ordering-only credit inside `ACC-EMU-001`; HostUnit primary; Bench for every timing requirement; CS-34 and CS-35 keep the firmware inside the modelled scope; fallback in section 9.4 item 6 |
| Complexity tool staleness | `rust-code-analysis-cli` last released 2023-01; may mis-parse Rust 2024 syntax | Accreditation on reference functions; clippy `cognitive_complexity` cross-check; fallback to a project script over `syn` if it fails on the code base (decision at CDR) |
| rustos driver effort (RSK-013) | Thirteen work packages (section 19) before PDR and CDR on the compressed schedule | Ordering by need (section 19); keyer prototype uses only WP-01, 02, 03, 09 and 11; PDR liens permitted per SEMP section 3.4 |
| Toolchain not qualified | Upstream rustc has no safety qualification for Cortex-M33 | Accreditation by tests (section 17.3); Ferrocene recorded as option; reproducible builds |
| Flash write path | Writing configuration via bootrom flash functions with XIP disabled can hang if interrupts touch flash | WP-SW-08 design: interrupts masked, code executing from RAM, bounded duration; dev-board checks |
| Wrong image or configuration accepted (RSK-015) | A corrupt or wrong image or configuration is accepted at boot | CS-32, the configuration guard (section 14.1), SWE-193 cases |
| Host mock diverges from silicon (proposed by ADR-011 section 4.4) | A behavior credited by HostUnit differs on the RP2350 | Contract tests run against the mock and on the dev board; Bench confirmation of every hazard-tracing requirement (section 9.7) |
| Single maintainer of rustos | Changes to rustos core by the owner could break cwht | Path dependency pinned to a commit in the VDD; contract tests run on every rustos change |

---

## 22. Tailoring mirror (SWE-121) and open cross-document items

Rows dispositioned T or NA in `docs/process/rmm.json` that this plan relies on: SWE-015, SWE-151 (cost), SWE-016, SWE-018, SWE-046 (schedule), SWE-017 (training), SWE-022, SWE-023 (NASA-STD-8739.8 not in corpus), SWE-027 c (IP counsel), SWE-032 (CMMI), SWE-141, SWE-131, SWE-178, SWE-179 (IV&V), SWE-143 (software architecture review: NPR 7120.5 Category 1 and 2 applicability; intent kept by the independent PDR architecture review of section 5 item 2), SWE-147, SWE-148 (reuse catalog), SWE-154, SWE-156, SWE-157, SWE-159, SWE-210 (cybersecurity scope), SWE-174, SWE-094, SWE-045 (institutions), SWE-219 (MC/DC by reviewed independence-pair tables plus stable-toolchain region coverage, section 9.6; residual risk RSK-010), SWE-211 (Rust `core` tested at feature level without structural coverage, 04 section 4; proposed at SRR). Their rationale is in the RMM and is not repeated here.

Open items found by a diff of this plan against the charter at `b8214ca` and the process documents present on 2026-09-25. Only unresolved items are listed; each names the document that changes, who changes it and the gate by which it changes. Before SRR these are Log-controlled edits (05 section 4.2 preamble); they are carried in the SRR package.

| Item | Document that changes, by whom | Change | By |
|---|---|---|---|
| Safety-critical list outside this plan | `docs/process/03-software-classification-and-rmm.md` section 4.3 drivers row, 03 author, with owner concurrence as SMA TA | Add the clocks and PLL driver (WP-SW-11), which this plan and `docs/safety/hazard-analysis.md` section 6 list, in the re-transcription of 03 item X13. 04 sections 10.3 and 12 now point to section 14.1 without restating it, and `hazards.json` 0.2.0-pha names the scheduler and runtime and the configuration guard | SRR (owner concurrence in the decision memo) |
| Coverage disposition for target-only code | 04 section 12 "Targets", 04 author | Add the `target-only: verified by <TC-ID>` disposition of section 9.5 item 2 as the SWE-190 complementary evidence | PDR (coverage plan) |
| Toolchain lock rows | `tools/toolchain.lock.md` section 1 and section 1.1, Claude as lock maintainer | Install the components `miri` and `llvm-tools` on `nightly-2026-08-24` and record them in its lock row as a Log change (CS-03). The rows for the nightly (hash `fb6531d55`), `rust-code-analysis-cli` (not installed) and the `tools/render_compliance.py` known-answer test exist as of 2026-09-25 | FW-B0, before SRR |
| RSK-009 closure evidence | `docs/risk/register.json` RSK-009, Claude as risk owner | Record the per-SWE completeness check (267 files; 130 `swe-NNN` pages, each with a `# 7. Software Assurance` section; run 2026-09-25) as closure evidence; the owner closes RSK-009 at SRR on that record | SRR |
| rustos license | rustos repository, owner | Add a license file (`OQ-SW-001`; section 17.1) | PDR |
| Artifacts beyond charter section 5 | Charter section 5, owner (charter issue) | Add `docs/sprints/index.md`, `docs/design/sw/<module>.md`, `firmware/devcheck/`, `firmware/emu/`, `firmware/THIRD-PARTY-NOTICES.md`, `docs/vv/reports/TC-SW-COV-001-r<N>/`, `docs/process/se-compliance-matrix.schema.json`; 05 Table 4-1 rows 3, 11, 25 and 44 to 46 already cover them as configuration items | SRR |

---

## 23. Plan maintenance (SWE-024)

Actuals against this plan are tracked in the "Software status" section of each review package and in `docs/sprints/index.md`. Changes to this plan after SRR are CRs; editorial fixes are logged in the revision table. The plan is re-approved by the owner at every gate (decision memo).

| Revision | Date | Change | Approved |
|---|---|---|---|
| A (draft) | 2026-09-25 | Initial plan for SRR | pending owner decision memo |
| A.1 (draft) | 2026-09-25 | Aligned to charter revision b3d2e13: SWEHB corpus present (sections 1, 2.2, 15 with the 5.08, 5.17 and 5.18 content maps); safety-critical scope extended to audio output limiting, the safe-state manager and the boot path with mission-critical modules named (sections 4, 12, 14); MC/DC record includes tool-measured branch and condition coverage at every release (sections 8, 9.5, 9.6, MSR-14); Miri named as the second nightly analysis (CS-03, G5); installed tool versions recorded (section 8.1); TV records (sections 8.3, 17.3); annotated tags (section 20); rustos license fact (section 17.1); cross-document items table (section 22) | pending owner decision memo |
| A.2 (draft) | 2026-09-25 | Aligned to charter revision b8214ca after independent review: single peer-review record in `checklists/` with front matter (sections 1.2, 1.4, 3.4, 10.2); software assurance table (section 2.1.1) and assurance fields in the record; Emulation for event order only per ADR-011, timing to HostUnit and Bench (sections 1.2, 3, 5, 9.1, 9.4, 11.2, 14.2, 19; CS-12, CS-22; new CS-34 to CS-38); coverage scoped to host-compilable code with the target-only disposition (section 9.5); safety-critical list regenerated from `hazards.json` and 03 section 4.3 with the configuration guard, the scheduler dispatcher and the clock driver (section 14.1) and the second SWE-134 table completed per module (section 14.2); deferred findings to RIDs (section 10.2); Verified versus Closed and SWE-194 changes item (sections 3.2, 18, 20); privacy (section 16.6); SWE-146 e monitoring (section 17.4); nightly pin and tool facts corrected (CS-03, section 8.1); G3 on nextest JUnit (section 8.4, Annex C); TPM-017 mirror (section 11.1); acronyms (Annex D); section 22 rebuilt | pending owner decision memo |

---

## Annex A. Peer review checklists (SWE-088)

| Product type | File |
|---|---|
| Requirements, plans and the other routed product types | `docs/templates/peer-review-checklist-requirements.md` |
| Architecture, design, ICDs and hardware design products | `docs/templates/peer-review-checklist-design.md` |
| Code (Rust) | `docs/templates/peer-review-checklist-code.md` |
| Test cases, test code and scenarios | `docs/templates/peer-review-checklist-test.md` |

## Annex B. Lint configuration to be committed in FW-B0 (`firmware/Cargo.toml`)

```toml
[workspace.lints.rust]
unsafe_code = "forbid"            # overridden to "allow" only in the rustos pico2 and api manifests
missing_docs = "deny"
static_mut_refs = "deny"
unsafe_op_in_unsafe_fn = "deny"

[workspace.lints.clippy]
pedantic = { level = "deny", priority = -1 }
nursery  = { level = "deny", priority = -1 }
unwrap_used = "deny"
expect_used = "deny"
panic = "deny"
unreachable = "deny"
todo = "deny"
unimplemented = "deny"
indexing_slicing = "deny"
panic_in_result_fn = "deny"
exit = "deny"
arithmetic_side_effects = "deny"
as_conversions = "deny"
wildcard_enum_match_arm = "deny"
shadow_unrelated = "deny"
shadow_reuse = "deny"
shadow_same = "deny"
let_underscore_must_use = "deny"
std_instead_of_core = "deny"
alloc_instead_of_core = "deny"
float_cmp = "deny"
too_many_lines = "deny"
cognitive_complexity = "deny"
```

`firmware/clippy.toml`: `too-many-lines-threshold = 60`, `cognitive-complexity-threshold = 15`, `disallowed-methods` and `disallowed-types` listing `core::mem::transmute`, `core::mem::zeroed`, `core::mem::uninitialized`, `core::hint::unreachable_unchecked`, and every `*_unchecked` slice method. Test targets may relax `unwrap_used`, `expect_used` and `arithmetic_side_effects` with `#![cfg_attr(test, allow(...))]` (CS-21 waiver comment required).

`firmware/.config/nextest.toml`:

```toml
[profile.ci]
retries = 0
fail-fast = false

[profile.ci.junit]
path = "junit.xml"   # written to firmware/target/nextest/ci/junit.xml
```

## Annex C. Gate script outline (`tools/sw_gate.sh`)

```sh
#!/bin/sh
# cwht software gate: G1 fmt+clippy, G2 build+map, G3 tests x2, G4 traceability,
# G5 static analysis, G6 coverage+emulation. Exit non-zero on first failure.
set -eu
cd "$(dirname "$0")/.."
QUICK=${1:-}
NX=firmware/target/nextest
( cd firmware && cargo fmt --check && cargo clippy --workspace --all-targets -- -D warnings \
  && cargo clippy -p cwht-app --target thumbv8m.main-none-eabihf -- -D warnings )            # G1
( cd firmware && cargo build -p cwht-app --release --target thumbv8m.main-none-eabihf )       # G2
.venv/bin/python tools/measurements.py --link-map firmware/target/thumbv8m.main-none-eabihf/release/cwht-app.map
( cd firmware && cargo nextest run --workspace --profile ci ) && cp "$NX/ci/junit.xml" "$NX/run1-junit.xml"
( cd firmware && cargo nextest run --workspace --profile ci ) && cp "$NX/ci/junit.xml" "$NX/run2-junit.xml"
.venv/bin/python tools/measurements.py --diff-runs "$NX/run1-junit.xml" "$NX/run2-junit.xml"  # G3
[ "$QUICK" = "--quick" ] && exit 0
.venv/bin/python tools/traceability.py                                                        # G4
( cd firmware && cargo audit && cargo deny check && cargo geiger --forbid-only -p cwht-app -p cwht-core )
.venv/bin/python tools/unsafe_audit.py --check
rust-code-analysis-cli --metrics --output-format json --paths firmware/ ../rustos/api ../rustos/firmware/pico2 \
  | .venv/bin/python tools/complexity_gate.py --max 15
( cd firmware && cargo +nightly-2026-08-24 miri test -p api -p pico2 --lib )                  # G5 (Miri: nightly analysis, MSR-08)
( cd firmware && cargo llvm-cov nextest --workspace --profile ci --lcov --output-path target/lcov.info \
  && RUSTFLAGS=-Zcoverage-options=condition cargo +nightly-2026-08-24 llvm-cov nextest --workspace --profile ci \
       --branch --json --output-path target/branch-condition.json )
tools/emu_run.sh --all --report firmware/target/emu-report.json                               # G6 (SKIP line until the PDR emulator ADR)
.venv/bin/python tools/measurements.py --coverage firmware/target/lcov.info \
  --branch-condition firmware/target/branch-condition.json --emu firmware/target/emu-report.json
```

## Annex D. Acronyms and plan-specific terms (SWEHB 5.17 items 16 and 17)

Project-wide terms are in SEMP Appendix A (`docs/plan/semp.md`); NASA terms carry the meaning of NPR 7123.1D App. A.

| Acronym or term | Meaning in this plan |
|---|---|
| ACC-EMU-001 | Emulator accreditation record proposed in `docs/research/emulator-accreditation-and-timer-irq.md` F13 and named by ADR-011; event-order scope only |
| ADC, ALC | Analog-to-digital converter; automatic level control of the PA drive |
| CC | Cyclomatic complexity (SWE-220) |
| CCB | Configuration Control Board (the owner) |
| CS-NN | Rule of the Rust coding standard of section 7 |
| Dev-board check | Bench run on a bare Pico 2 with `credit: false` (04 section 4) |
| ETA, SMA TA | Engineering Technical Authority; Safety and Mission Assurance Technical Authority (both the owner) |
| FW-Bn | Firmware build increment n (section 3.2) |
| HostUnit | Evidence class: host `cargo test` of `cwht-core` against `cwht-hal-mock` with the mock clock |
| HSI | Human Systems Integration |
| INSP-NNN | Peer review record: the filled checklist in `docs/reviews/<REVIEW>/checklists/` |
| MC/DC | Modified condition/decision coverage (SWE-219) |
| MMIO | Memory-mapped input/output (register access) |
| MSR-NN | Software measurement of section 11 |
| NCR | Nonconformance report |
| NVIC | Nested Vectored Interrupt Controller of the Cortex-M33 |
| PCA-05 | Physical configuration audit line recording the release installed on a unit (04 section 5.3) |
| PLL, XOSC | Phase-locked loop; crystal oscillator of the RP2350 |
| RMM | Requirements Mapping Matrix (`docs/process/rmm.json`) |
| SA | Software assurance |
| SIO | Single-cycle IO block of the RP2350 (GPIO access path, CS-35) |
| Target-only code | Code that cannot run on the host (`cwht-app`, `pico2` MMIO, boot and vector table; section 9.5 item 2) |
| TPM | Technical performance measure (`docs/plan/tpm.json`) |
| TV-NNN | Tool validation record (`docs/cm/tool-validation/`) |
| UB | Undefined behavior (Miri) |
| VDD | Version description document (SWE-063) |
| WP-SW-NN | rustos driver work package of section 19 |
