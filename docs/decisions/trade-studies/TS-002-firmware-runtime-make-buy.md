# TS-002: Firmware runtime and HAL make/buy (SWE-033)

| Field | Value |
|---|---|
| ID | TS-002 |
| Status | Draft, revision 1 (findings F-08 to F-10 of INSP-013 applied; awaiting the reviewer's verification of the fixes) |
| Decision class trigger | 06 section 14.1 class 1 item (h), a software acquisition-versus-development decision (SWE-033) for the runtime, HAL and PAC crates; this report is the NPR 7150.2D section 6.1 item t make/buy record (`docs/process/07-software-engineering-plan.md` section 1.3 row t). Also item (c): the runtime drivers GPIO, TIMER, PWM, ADC, watchdog, critical section and clocks are in the safety-critical call path listed in 07 section 14.1 |
| Decision maker | Robin (owner, Decision Authority; also SMA Technical Authority for the software assurance concurrence) |
| Recommender | Claude (trade study author invocation, 2026-09-25) |
| Independent reviewer | INSP-013 in `docs/reviews/SRR/checklists/trade-studies-ts-001-ts-002.md`, one record for TS-001 and TS-002 (design checklist sections A, B and H plus the 06 section 16 trade-study items); iteration 1 NEEDS CHANGES with 3 Minor findings on this study, applied in revision 1. Software assurance review: not dispatched (`assurance_required: false` in INSP-013), because the dispatch table of 07 section 2.1.1 has no trade-study row. The author asks for one, since the runtime drivers are in the call path of the 07 section 14.1 components and SWEHB `swe-033` section 7.1 assigns tasks 1 to 3 to software assurance; whether it is required is referred to Claude (INSP-013 finding-9) |
| Decide by | SRR, because the software plan enters SRR with its acquisition-versus-development record (07 section 3.1 SRR row; `docs/process/01-lifecycle-and-reviews.md` section 4.3 row 23; SRR package item H14). FW-B0 and the rustos work packages of FW-B1 start on this decision |
| Related risks | RSK-003, RSK-010, RSK-013, RSK-015, RSK-020, RSK-021, RSK-023 |
| Related requirements and hazards | REQ-SYS-128 (KDR), REQ-SYS-129; hazards reached through the components of 07 section 14.1: HZ-001, HZ-002, HZ-003, HZ-004, HZ-005, HZ-007, HZ-014; SI-007, SI-015, SI-025, SI-026, SI-033 |
| Resulting ADR | ADR-NNN, the next free number at decision time (ADR-027 or later, because ADR-026 is the proposed successor of ADR-010; `docs/decisions/adr/README.md` rule 1), recording the runtime and HAL decision and citing ADR-004 and ADR-019. It is a new ADR because Accepted ADRs are not edited (README rule 2) and every trade study produces exactly one ADR (06 section 14.2) |
| Dates | opened 2026-09-25; recommended: on filing of the independent review record; decided: at SRR |

## 1. Executive summary

- **Recommendation (one sentence):** build the firmware on the owner's rustos (`api` traits plus the `pico2` runtime and HAL), extended upstream by the work packages of 07 section 19. The alternatives are `rp235x-hal` with `cortex-m-rt`, Embassy and RTIC. rustos totals 400 of 500 (80 %) against 265 (53 %), 220 (44 %) and 220 (44 %), so the owner's direction (SI-007, SI-033) and the technical ranking agree.
- **Problem requiring a decision (one sentence):** which runtime and hardware-abstraction layer the cwht image is built on. The layer must be verified at Class A rigor (charter section 1), tested host-first through dependency injection (SI-026, REQ-SYS-128), and fit the single-priority, SIO-only design rules (REQ-SYS-129; 07 section 7.7).
- **Robustness verdict (section 6):** Robust.
- **Owner's decision (section 10):** pending. The owner rules it in the SRR decision memo (section 8).

## 2. Problem and decision context

- **Mission and system context:** software item `pico2` (runtime and HAL) and `api` (portable traits) of 07 section 1.2, under every `cwht-core` module. That includes the safety-critical modules SW-KEYER, SW-TXSEQ, SW-PWR, SW-SAFE, SW-AUDIO, SW-BOOT and SW-SCHED (07 section 14.1). ConOps: every operating scenario, since every one runs on this layer. MOE-003 (first power-on) and MOE-005 (keying feel and timing) are the measures most exposed.
- **Decision needed and intended outcome:** after the decision, the image's non-application code is fixed, and so is the set of work packages that FW-B1 must deliver before PDR (07 section 3.2). The verification level each piece of that code needs is also fixed: SWE-027 item e and SWE-211 require OTS and OSS components to be verified to the level of developed code.
- **Constraints:**
  - SI-007: "firmware in Rust built on the owner's `rustos`".
  - SI-033: new peripheral drivers are developed upstream in rustos, not in a cwht-local crate; ADR-019.
  - SI-026 and ADR-011: host-first testing through the rustos `api` traits; drivers traced to the RP2350 datasheet.
  - SI-015 and ADR-001: Class A rigor.
  - SI-025 and ADR-017: MIT.
  - CS-02: zero external runtime crates in the image.
  - CS-03: stable rustc 1.98.0, target `thumbv8m.main-none-eabihf`.
  - CS-34 to CS-38: target platform rules.
  - 07 section 17.4 and RMM row SWE-146: no SVD-generated PAC.
  - Charter section 12: SWE-027 tailored only in its IP-counsel item, with V&V of external crates to developed-code level retained; SWE-211 relief proposed for Rust `core` only.
- **Prior related decisions and lessons learned:**
  - ADR-004 (Pico 2 module; "the firmware is Rust on `rustos` with zero external runtime crates").
  - ADR-011 (host-first verification and the firmware design rules).
  - ADR-019 (drivers upstream in rustos; it defers the make/buy assessment to this study, its section 3 row C and section 7).
  - The rustos methodology heritage of `docs/plan/technology-assessment.md`.
  - `docs/lessons-learned.md` does not exist yet, so there are no lessons-learned entries to cite.
- **Research consulted:**
  - `docs/research/rustos-toolchain-proof.md` (F1 to F16, driver extension map, work-package table, implications);
  - `docs/research/emulator-accreditation-and-timer-irq.md` (F5 to F9, F12, F13);
  - `docs/research/rp2350-emulation-options.md` (recommendation);
  - rustos's own documentation: `/Users/robinonsay/rust/rustos/README.md` (lines 44 to 47, "No external embedded crates (`cortex-m`, `cortex-m-rt`, `rp-hal`, `embassy`, ...) are used") and `/Users/robinonsay/rust/rustos/docs/tutorials/rp2350_baremetal/02_linker_scripts.md` section 2.8 ("What the ecosystem does instead": `cortex-m-rt` ships `link.x`; `rp235x-hal` ships that plus the `IMAGE_DEF` handling).

  **No `docs/research/` report characterizes `rp235x-hal`, Embassy or RTIC** (dependency trees, unsafe counts, stable-toolchain status, licenses). Their cells are therefore scored from the rustos documentation, the cwht process documents and general engineering knowledge of these projects, and carry Low confidence unless stated. Their top-level licenses were read from crates.io metadata in revision 1 (section 4, M3). Section 6 shows the ranking does not depend on them.

**SWE-033 options covered.** The SWE-033 note in NPR 7150.2D section 3.1.2 and SWEHB `swe-033-acquisition-vs-development-assessment.md` section 1.1 list options a to f.

| SWE-033 option | cwht instance | Where assessed |
|---|---|---|
| a. Acquire an off-the-shelf product | No commercial RP2350 Rust runtime or HAL with Class A or equivalent qualification evidence was found. Ferrocene is a qualified toolchain, not a runtime, and is recorded in 07 section 17.3 | Not a runtime alternative; toolchain choice stays in 07 section 17.3 |
| b. Develop internally | The drivers of 07 section 19, written in rustos under this plan | A0 |
| c. Develop through contract | Not applicable: no contracts (charter section 12, SE-24 to SE-31 row) | none |
| d. Enhance an existing product | Extend rustos `api` and `pico2` upstream (ADR-019) | A0 |
| e. Reuse an existing product | Reuse the owner's rustos (A0) or an OSS HAL or framework (A1 to A3) | A0 to A3 |
| f. Source code available external to NASA | `rp235x-hal`, Embassy, RTIC (open source) | A1 to A3 |

**Component-level make/buy disposition** (RMM row SWE-033 asks for every firmware component). Only the runtime and HAL row is a class 1 decision under 06 section 14.1 (h) and is scored below. The other rows are dispositioned by existing policy and recorded here so the SWE-033 record is complete.

| Component | Disposition | Basis |
|---|---|---|
| Runtime, boot, vector table, HAL, register layouts | **This study** | 06 section 14.1 (h) |
| Application logic in `cwht-core` (keyer, sequencer, safety manager, audio limiter, UI, configuration store, scheduler, CRC-32, synthesizer register computation, DSP if TS-001 candidate B returns) | Make | CS-02 (zero external runtime crates); 07 section 1.2; keyer semantics taken as heritage references only, with golden vectors (`docs/plan/technology-assessment.md` heritage table) |
| LCD driver | Make, against `bus::SpiTx`; the `sharp-memory-display` crate is used as an interface reference only | `docs/plan/technology-assessment.md` heritage table row "Sharp memory LCD"; CS-02 |
| Rust `core` library | Buy (ships with the locked rustc); SWE-211 structural-coverage relief proposed | 07 section 17.1 row 1; charter section 12 row SWE-211 |
| Toolchain (rustc, cargo, clippy, llvm-tools) | Buy (upstream stable), accredited by tests; Ferrocene recorded as an option | 07 sections 8.1, 17.3; RSK-020 |
| Host-side test and analysis crates (`cargo-llvm-cov`, `cargo-nextest`, `cargo-geiger`, `cargo-deny`, `cargo-audit`) | Buy (OSS dev tools, not in the image) | 07 section 17.1 |
| RP2350 emulator | Buy or reuse (OSS dev tool), selected by the PDR emulator ADR (`ACC-EMU-001` candidate) | ADR-011; `emulator-accreditation-and-timer-irq.md` F13 |

## 3. Decision matrix setup and rationale

### 3.1 Criteria and operational definitions

Mandatory criteria are pass or fail; an alternative that fails any of them is dropped before scoring (SE HB §6.8.1.2.1). Enhancing criteria are scored 1 to 5 against the anchors. Intermediate scores are interpolated between anchors, and an estimated range is scored at its midpoint (SE HB §6.8.1.2.4).

| ID | Criterion | Type | Operational definition (what is measured, unit, method) | Scale anchors (1 / 3 / 5) | Weight |
|---|---|---|---|---|---|
| M1 | Locked toolchain | Mandatory | Builds with stable rustc 1.98.0 for `thumbv8m.main-none-eabihf` and yields an `rp2350-arm-s` image (CS-03) | pass / fail | n/a |
| M2 | Host-first dependency injection | Mandatory | Application logic builds and runs unmodified on a macOS or Linux host against injected trait implementations (SI-026; REQ-SYS-128) | pass / fail | n/a |
| M3 | License | Mandatory | License terms permit redistribution in an MIT-licensed design (SI-025; ADR-017; SWE-027 item c as tailored) | pass / fail | n/a |
| M4 | No unreducible Red safety risk | Mandatory | 06 section 13 item 2 | pass / fail | n/a |
| C1 | Class A V&V burden of non-project image code | Enhancing | External crates compiled into the image, each needing verification to developed-code level (SWE-027 item e; SWE-211); count from the dependency tree or project documentation | 1: >= 10 crates / 3: 4 crates / 5: none (only Rust `core`) | 20 |
| C2 | Register-level auditability | Enhancing | How register accesses are written and traced to the RP2350 datasheet (charter section 9 driver-to-datasheet Inspection; SI-026) | 1: in third-party code without datasheet citations / 3: through an SVD-generated PAC, traceable to the SVD, no section citations / 5: hand-written in project-controlled code, each citing its datasheet section | 10 |
| C3 | Driver effort to cwht needs | Enhancing | Work packages cwht must write to reach the peripheral set of 07 section 19, count | 1: >= 11 / 3: 6 / 5: <= 2 | 20 |
| C4 | Unsafe surface to audit | Enhancing | Lines containing `unsafe` in image code that the unsafe audit of CS-07 must sign, estimated at CDR | 1: > 500 or macro-generated / 3: 300 / 5: < 100, all in project-controlled code | 10 |
| C5 | Host testability | Enhancing | Demonstrated maturity of host tests of application logic through injected traits | 1: needs structural workarounds (host executor, macro-bound task code) / 3: supported by ecosystem traits and mock crates, not shown in this project / 5: shown working in this project | 15 |
| C6 | Fit with the design rules and emulator scope | Enhancing | Mechanisms the runtime relies on against CS-34 (one NVIC priority, run to completion), CS-35 (SIO only, timer-sampled inputs, no IO_BANK0 edge interrupts) and the `ACC-EMU-001` credit exclusions (GPIO edge interrupts, NVIC priorities, GPIOC; emulator F7, F8, F9, F13) | 1: the runtime's core mechanism is outside the rules / 3: a default outside the rules that can be configured off / 5: nothing outside the rules | 15 |
| C7 | Change control and continuity | Enhancing | Who controls changes to the layer and how it is pinned (SWE-027 item d; RSK-023) | 1: one external maintainer or unpinned / 3: active multi-maintainer external project, pinned by version and lock file / 5: owner-controlled, commit pinned in every VDD, changes under the cwht CR process | 10 |
| | | | | **Sum of weights** | **100** |

**Criteria considered** (06 section 13 item 1):

- **Safety:** used as M4 and through C6, because the runtime mechanisms carry the SWE-134 provisions of 07 section 14.2.
- **First power-on:** used as C5 and C6. HostUnit and credited emulation are the pre-build evidence (ADR-011), and MOE-003 depends on them.
- **Cost:** omitted. There is no part cost, all alternatives are free of charge, and labor is outside the cost model (charter section 12, SWE-015 tailored). The labor cost appears as schedule in C3 and as verification effort in C1.
- **Schedule:** used as C3 (RSK-013) and, through verification effort, C1.
- **Performance margin:** used as C6. The design rules exist to protect keyer timing (REQ-SYS-042, KDR) and the evidence scope.
- **System security:** used through C1, where supply-chain exposure grows with the external crate count and is checked by `cargo-deny` and `cargo-audit` (07 section 17.1). Otherwise omitted: the choice does not change the attack surfaces of 07 section 16.2 (USB firmware load, key input).

**Owner direction.** 07 section 17.2 lists SI-007 among the scoring items. SI-007 and SI-033 are instead applied as the decision rule of section 8, so the matrix shows the technical cost of the direction, which 07 section 17.2 says the study must record. Scoring the direction would only widen A0's lead.

Other criteria considered and not used, with reason:

- Flash and RAM footprint (TPM-010, TPM-011): the rustos blinky uses 2,008 B of flash and 8,200 B of RAM of 4 MB and 520 KB (`rustos-toolchain-proof.md` F4). No candidate threatens the budget, so the criterion does not discriminate.
- Async ergonomics: a benefit of Embassy recorded in section 7. The design rules (single priority, run to completion, polled inputs) do not use it.

### 3.2 Alternatives

A pure do-nothing alternative is rustos as it stands: boot, vector table and a GPIO driver only, with no interrupt path, clock bring-up, timer, PWM, ADC, I2C, SPI, watchdog or flash store (`rustos-toolchain-proof.md` F7, F8). It cannot meet REQ-SYS-042 or any timed requirement. The current baseline is therefore A0, rustos extended upstream as ADR-019 records.

| ID | Alternative | Description | Source |
|---|---|---|---|
| A0 | rustos (current baseline) | `api` portable traits and the `pico2` runtime and HAL, extended upstream by WP-SW-01 to WP-SW-12 of 07 section 19. Hand-written registers with datasheet citations; zero external crates | ADR-004, ADR-019; `rustos-toolchain-proof.md` F7, F8, F13, work-package table; 07 sections 17.1, 19 |
| A1 | `rp235x-hal` with `cortex-m-rt` | The rp-rs community HAL for RP2350 over an SVD-generated PAC, with the `cortex-m-rt` runtime (vector table, `link.x`) and `embedded-hal` traits. Application logic in `cwht-core` against `embedded-hal` traits | rustos tutorial 02 section 2.8; `rustos-toolchain-proof.md` F8 item 1 (the `cortex-m-rt` pattern) |
| A2 | Embassy | `embassy-rp` HAL with `embassy-executor` (async tasks) and `embassy-time`. Drivers complete on interrupts through async wakers | rustos README lines 44 to 47 (named as excluded); general knowledge (Low) |
| A3 | RTIC 2 over `rp235x-hal` | The RTIC framework (tasks bound to interrupts, priority-based preemption under the stack resource policy, `rtic-monotonics` for time) over the A1 HAL | 07 section 17.2; general knowledge (Low) |

Alternatives pruned before scoring, with reason:

- **A cwht-local `pico2-ext` crate:** excluded by SI-033 and rejected in ADR-019 option B (two HALs for one chip).
- **An own HAL over an `svd2rust` PAC:** rejected in ADR-019 option D and by 07 section 17.4; the SVD would be an unreviewed generated input under SWE-146.
- **RTIC over rustos `pico2`:** RTIC's `#[app(device = ...)]` expects a device crate in the `svd2rust` convention (interrupt enumeration and priority-bit constant), which brings back the previous pruned item (Low confidence on the exact interface).
- **The pico-sdk in C through FFI:** SI-007 fixes Rust. The SDK's default GPIO-coprocessor code also produces no pin activity in the `ACC-EMU-001` candidate (`emulator-accreditation-and-timer-irq.md` F7).
- **A C RTOS (FreeRTOS, Zephyr):** SI-007; a second language and coding standard under Class A.

### 3.3 Weight rationale

| Criterion | Weight | Driver |
|---|---|---|
| C1 V&V burden | 20 | Class A election (charter section 1; SI-015). SWE-027 item e and SWE-211 require bought code to be verified to the level of developed code, and charter section 12 retains that clause. This is the largest effort difference between making and buying |
| C2 auditability | 10 | Charter section 9 makes driver-to-datasheet traceability an Inspection evidence item; SI-026 last clause. Weighted below C1 because it measures traceability, not effort |
| C3 driver effort | 20 | Schedule. RSK-013; FW-B1 must deliver the keyer prototype before PDR (07 section 3.2); 07 section 21 "rustos driver effort" |
| C4 unsafe surface | 10 | CS-05 to CS-07; SWE-185 and SWE-207 retained in full (charter section 12) |
| C5 host testability | 15 | SI-026; REQ-SYS-128 (KDR); ADR-011 (HostUnit is the primary software evidence) |
| C6 design-rule fit | 15 | REQ-SYS-129; CS-34, CS-35; the emulator credit scope; the SWE-134 provisions of 07 section 14.2 rest on these mechanisms |
| C7 change control | 10 | SWE-027 item d (future support); RSK-023; the configuration-item pinning of 05 and 07 section 13 |

The owner set no weight directly.

### 3.4 Evaluation methods

| Criterion | Method | Tool and version | Evidence artifact |
|---|---|---|---|
| M1, M2 for A0 | Build and host test executed by the research agent | rustc 1.98.0, cargo 1.98.0, picotool 2.3.0 (`tools/toolchain.lock.md`; TV records pending, package H12) | `rustos-toolchain-proof.md` F1, F3, F4, F13 |
| M1, M2 for A1 to A3 | Documentation review; not built | none | rustos README and tutorial 02 section 2.8; general knowledge (Low) |
| M3 for A1 to A3 | License field of the crates.io metadata of each top-level crate, 2026-09-25 (revision 1) | curl and the project venv Python, reading JSON only | Appendix A; section 4 M3 cells |
| C1 | Dependency listing: A0 from the build log; A1 to A3 estimated | cargo (A0) | `rustos-toolchain-proof.md` F4; CS-02 |
| C2 | Source and house-style inspection | none | ADR-019 section 2; `rustos-toolchain-proof.md` F8; 07 section 17.4 |
| C3 | Count against the 07 section 19 table | none | 07 section 19; `rustos-toolchain-proof.md` work-package table |
| C4 | `grep -c unsafe` on rustos (A0) by the research agent; estimate for the rest | grep | `rustos-toolchain-proof.md` F6 |
| C5 | Proof crate on the host (A0) | cargo test | `rustos-toolchain-proof.md` F13 |
| C6 | Rule-by-rule comparison with CS-34, CS-35 and the emulator credit scope | none | 07 section 7.7; `emulator-accreditation-and-timer-irq.md` F7, F8, F9, F12, F13 |
| C7 | Governance review | none | 07 sections 17.1, 21; RSK-023 |
| Sensitivity | Recomputation under the 06 section 14.4 perturbations | Python 3 script in TS-001 Appendix A.3 (matrix `wF`, `sF`, `lowF`) | TS-001 Appendix A.3 |

### 3.5 Setup matrix (before scoring)

| Criterion | Weight | A0 | A1 | A2 | A3 |
|---|---|---|---|---|---|
| M1 | n/a | | | | |
| M2 | n/a | | | | |
| M3 | n/a | | | | |
| M4 | n/a | | | | |
| C1 | 20 | | | | |
| C2 | 10 | | | | |
| C3 | 20 | | | | |
| C4 | 10 | | | | |
| C5 | 15 | | | | |
| C6 | 15 | | | | |
| C7 | 10 | | | | |

## 4. Scoring rationale

Mandatory screening:

| Alternative | M1 | M2 | M3 | M4 | Result |
|---|---|---|---|---|---|
| A0 | pass: `cargo pico2` builds dev and release, and an application links offline against the local checkout (`rustos-toolchain-proof.md` F3, F4; High) | pass: a `no_std` crate depending only on `api` passes host tests with a mock GPIO and cross-builds unchanged (F13; High) | pass, with an owner action. No `LICENSE` file exists in rustos at `c54d35a`, but every line is the owner's; `OQ-SW-001` adds the license by PDR (07 section 17.1 row `api`) | pass | kept |
| A1 | pass (Low): the owner's tutorial names `rp235x-hal` and `cortex-m-rt` as the ecosystem path for RP2350 (tutorial 02 section 2.8); a stable-toolchain build has not been done in this project | pass (Low): `embedded-hal` traits are host-compilable; not shown in this project | pass (High for the crates read): crates.io metadata gives `rp235x-hal` 0.4.0, `cortex-m-rt` 0.7.7, `cortex-m` 0.7.9, `embedded-hal` 1.0.0 and `critical-section` 1.3.0 as "MIT OR Apache-2.0", and `rp235x-pac` 0.2.0 as BSD-3-Clause; all are in the permissive set of RMM row SWE-027 and of `firmware/deny.toml`. Transitive support crates were not read (Appendix A) | pass | kept |
| A2 | pass (Low): as A1 | pass (Low): logic written against `embedded-hal` or `embedded-hal-async` traits; async code needs a host executor | pass (High for the crates read): `embassy-rp` 0.10.0, `embassy-executor` 0.10.0 and `embassy-time` 0.5.1 are "MIT OR Apache-2.0", over the A1 PAC and `cortex-m` crates above | pass | kept |
| A3 | pass (Low): as A1 | pass (Low): task bodies must be factored out of the `#[app]` module | pass (High for the crates read): `rtic` 2.3.1 and `rtic-monotonics` 2.2.1 are "MIT OR Apache-2.0", over the A1 stack | pass | kept |

Enhancing scores (evidence cited as `docs/research/rustos-toolchain-proof.md` F<n> unless another file is named):

| Criterion | Alt. | Measured value and unit | Score | Confidence | Evidence |
|---|---|---|---|---|---|
| C1 | A0 | 0 external crates: the application build compiles only `pico2`, `api` and the application | 5 | High | F4; CS-02; ADR-004; rustos README lines 44 to 47 |
| C1 | A1 | 10 or more estimated: HAL, PAC, `cortex-m`, `cortex-m-rt`, `embedded-hal` family, `critical-section` and support crates | 1 | Low (not measured) | tutorial 02 section 2.8; general knowledge |
| C1 | A2 | 10 or more estimated: `embassy-rp`, `embassy-executor`, `embassy-time`, `embassy-sync`, HAL-internal crates, PAC, `cortex-m`, `cortex-m-rt`, `critical-section`, support crates | 1 | Low | general knowledge |
| C1 | A3 | 10 or more estimated: RTIC crates plus the A1 stack | 1 | Low | general knowledge |
| C2 | A0 | Hand-written `#[repr(C)]` register layouts with a datasheet citation per access (house style); the existing GPIO driver is written this way | 5 | High | F8; ADR-019 section 2; charter section 9; CS-08 |
| C2 | A1 | Register access through an SVD-generated PAC inside a third-party HAL; no section citations | 2 | Medium (the generated-PAC practice is recorded in ADR-019 option D and 07 section 17.4) | ADR-019 section 3 row D; 07 section 17.4 |
| C2 | A2 | Same as A1 (generated PAC under `embassy-rp`) | 2 | Medium | as A1 |
| C2 | A3 | Same as A1 | 2 | Medium | as A1 |
| C3 | A0 | 12 work packages (WP-SW-01 to WP-SW-12; WP-SW-13 optional) before CDR, 9 of them before PDR | 1 | High | 07 section 19; F7, F8; work-package table |
| C3 | A1 | About 3: trait adapters and host mocks for the HAL's drivers, the flash record store, CRC-32 | 4 | Low | tutorial 02 section 2.8; 07 section 19 |
| C3 | A2 | About 3 (as A1) | 4 | Low | general knowledge |
| C3 | A3 | About 3 (as A1, since the A1 HAL supplies the drivers) | 4 | Low | general knowledge |
| C4 | A0 | 53 lines mention `unsafe` today (`api` 11, `pico2` 42); an estimated 150 to 250 once the twelve work packages add their register access, all in owner-controlled code | 4 | Medium (growth estimated) | F6; 07 section 19 |
| C4 | A1 | More than 500 estimated across PAC, HAL and runtime, partly macro-generated | 1 | Low | general knowledge |
| C4 | A2 | More than 500 estimated (PAC, HAL, executor) | 1 | Low | general knowledge |
| C4 | A3 | More than 500 estimated, including RTIC macro-generated code | 1 | Low | general knowledge |
| C5 | A0 | Shown in this project: mock GPIO, two host tests pass, same crate cross-builds; a portable `time` trait is the one addition needed for keyer timing | 5 | High | F13 |
| C5 | A1 | Supported by `embedded-hal` traits and mock crates in the ecosystem; not shown in this project | 3 | Low | general knowledge |
| C5 | A2 | Async driver traits need a host executor and a mock time driver for `embassy-time` | 2 | Low | general knowledge |
| C5 | A3 | Task code lives in the `#[app]` module with macro-generated contexts; logic must be factored into plain functions to test on the host | 2 | Low | general knowledge |
| C6 | A0 | The rules were written for it: one NVIC priority with no priority writes, run-to-completion handlers, SIO-only GPIO, 1 kHz timer-sampled inputs, PWM slices 0 to 7 | 5 | High | 07 section 7.7 (CS-34 to CS-37); ADR-011 section 2 |
| C6 | A1 | Blocking HAL with interrupts chosen by the application, which can meet CS-34 and CS-35. Whether its GPIO path uses SIO or the GPIO coprocessor, which the emulator cannot model (F7 there: "possibly future Rust HALs"), is unverified | 4 | Low | `emulator-accreditation-and-timer-irq.md` F7 |
| C6 | A2 | Drivers complete on interrupts through async wakers. GPIO edge waits use IO_BANK0 edge interrupts, which CS-35 forbids and `ACC-EMU-001` cannot credit (F8 there). Priority-level executors conflict with CS-34 | 2 | Low | `emulator-accreditation-and-timer-irq.md` F8, F9, F13; 07 section 7.7 |
| C6 | A3 | RTIC's scheduling value is priority-based preemption; REQ-SYS-129 and CS-34 allow one priority, and the emulator has no priority model (F9 there) | 2 | Medium | REQ-SYS-129; `emulator-accreditation-and-timer-irq.md` F9 |
| C7 | A0 | Owner-controlled, commit pinned in the lock file and every VDD, changes by reviewed pull request under ADR-019. Single maintainer (07 section 21), so below the 5 anchor | 4 | Medium | 07 sections 17.1, 21; ADR-019; RSK-023 |
| C7 | A1 | Active multi-maintainer community project, pinned by version and `Cargo.lock` | 3 | Low | general knowledge |
| C7 | A2 | As A1 | 3 | Low | general knowledge |
| C7 | A3 | As A1 | 3 | Low | general knowledge |

## 5. Final decision matrix

| Criterion | Weight | A0 score | A0 weighted | A1 score | A1 weighted | A2 score | A2 weighted | A3 score | A3 weighted |
|---|---|---|---|---|---|---|---|---|---|
| C1 | 20 | 5 | 100 | 1 | 20 | 1 | 20 | 1 | 20 |
| C2 | 10 | 5 | 50 | 2 | 20 | 2 | 20 | 2 | 20 |
| C3 | 20 | 1 | 20 | 4 | 80 | 4 | 80 | 4 | 80 |
| C4 | 10 | 4 | 40 | 1 | 10 | 1 | 10 | 1 | 10 |
| C5 | 15 | 5 | 75 | 3 | 45 | 2 | 30 | 2 | 30 |
| C6 | 15 | 5 | 75 | 4 | 60 | 2 | 30 | 2 | 30 |
| C7 | 10 | 4 | 40 | 3 | 30 | 3 | 30 | 3 | 30 |
| **Total** | **100** | | **400** | | **265** | | **220** | | **220** |
| **Percent of maximum** | | | 80 % | | 53 % | | 44 % | | 44 % |
| **Rank** | | | 1 | | 2 | | 3 (tie) | | 3 (tie) |

## 6. Uncertainty and sensitivity statement

Computed with the script of TS-001 Appendix A.3 (matrices `wF`, `sF`, `lowF`).

1. **Weight sensitivity.** Each weight was moved by +10 and -10 points, clamped at 0, with the others rescaled proportionally. No perturbation changes the top rank. The smallest remaining lead of A0 is 80.6 points, at C3 (driver effort) +10.
2. **Score sensitivity.** Every Low-confidence cell was moved by +1 and -1: cells C1, C3, C4, C5, C6 and C7 of A1 and A2, and C1, C3, C4, C5 and C7 of A3. No change of top rank; smallest lead 115 points. As an additional check beyond 06 section 14.4, all those cells were moved in favor of the alternatives at once: A0 400, A1 355, A2 310, A3 295, so A0 stays first by 45 points.
3. **Assumptions and their evidence:**
   - A1 to A3 build on the locked stable toolchain and pull ten or more crates into the image. Neither was measured in this project; the source is general knowledge and the rustos documentation. Their licenses were read from crates.io metadata for the top-level crates (section 4, M3; revision 1, INSP-013 finding-8); the transitive support crates were not read, which leaves M3 unassessed for them. This has no effect on the ranking: the three alternatives pass the screen and lose on the enhancing criteria.
   - A0's unsafe count grows to 150 to 250 lines by CDR, estimated from F6 and the twelve work packages.
   - A1's driver coverage leaves about three work packages to cwht.
   - The C3 count for A0 is the plan's own list (07 section 19; High).
4. **Robustness verdict:** Robust. A0 leads under every perturbation.

   The one criterion on which the bought alternatives lead is C3, driver effort (A0 scores 1, the others 4). It cannot close the gap, for two reasons:
   - Class A verification of the bought code (C1) moves the same effort into verification rather than removing it (SWE-027 item e, SWE-211).
   - The design-rule fit (C6) and the demonstrated host testing (C5) favor the code written for the rules.
5. **Value of information:** not required, since the verdict is Robust. An optional confirmation would replace the Low C1, C3 and C4 cells with measured values: a skeleton crate per alternative built on rustc 1.98.0, then `cargo tree -e normal` and `grep -c unsafe` over the resolved sources. It takes about one hour, but fetching those crates from crates.io needs the owner's approval of the download. It is not needed before SRR, and the recommendation does not wait for it.
6. **Limitations of the evaluation methods and tools (SE HB §6.8.1.2.5):**
   - No `docs/research/` report covers the three bought alternatives, so their cells rest on documentation and general knowledge and carry Low confidence.
   - The A0 build and host-test evidence was produced by a research agent on tools without TV records (package H12), and the FW-B0 toolchain proof (`TC-SW-TOOL-001-r1`) is not yet filed.
   - The emulator findings used in C6 are from one commit of the `ACC-EMU-001` candidate (`af0114cb`).

## 7. Risks and benefits of the surviving alternatives

Scales of `docs/process/06-risk-and-decision-analysis.md` sections 6 to 8.

| Alternative | Risk statement | L | C (driving dimension) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| A0 | Given cwht needs twelve rustos work packages, nine of them before PDR (07 section 19), there is a possibility of the drivers not being demonstrated on hardware before CDR, adversely impacting the keyer prototype and the procurement release, leading to a PDR lien or a CDR slip | 3 | 3 (schedule) | 9 / Yellow | RSK-013 (history entry naming TS-002) |
| A0 | Given rustos is changed by its single maintainer for other users as well (07 section 21; ADR-019), there is a possibility of an upstream change breaking a cwht contract undetected, adversely impacting the firmware release, leading to a regression found late | 4 | 2 (schedule) | 8 / Yellow | RSK-023 (history entry naming TS-002) |
| A0 | Given rustos today has zero `api` unit tests, 13 clippy warnings in `pico2` and 71 rustfmt hunks (F2, F6), there is a possibility of the `-D warnings` gate failing at FW-B0, adversely impacting the toolchain proof, leading to a hygiene work package ahead of WP-SW-01 | 5 | 1 (schedule) | 5 / Yellow | new RSK-NNN, or a step of RSK-013 (the research WP-13) |
| A1 | Given SWE-027 item e and SWE-211 require the HAL, PAC and runtime crates to be verified to the level of developed code and charter section 12 retains that clause, there is a possibility of the verification of ten or more external crates exceeding the effort of writing the drivers, adversely impacting the FW-B1 and FW-B2 schedule, leading to a tailoring request or a slip | 4 | 3 (schedule) | 12 / Red | new RSK-NNN if selected |
| A1 | Given the PAC is generated from an SVD file that is not reviewed against the datasheet (07 section 17.4), there is a possibility of a register description error reaching a safety-critical driver, adversely impacting the SW-TXSEQ and SW-SAFE outputs, leading to a latent fault found on the bench | 2 | 3 (safety) | 6 / Yellow | new RSK-NNN if selected |
| A2 | As the A1 verification-effort risk, applied to the Embassy crates | 4 | 3 (schedule) | 12 / Red | new RSK-NNN if selected |
| A2 | Given async GPIO waits use IO_BANK0 edge interrupts that the emulator mis-decodes (`emulator-accreditation-and-timer-irq.md` F8), there is a possibility of the key and paddle paths falling outside every credited Emulation scenario, adversely impacting the evidence plan of ADR-011, leading to Bench-only evidence for the input path | 4 | 2 (schedule) | 8 / Yellow | RSK-003 |
| A3 | As the A1 verification-effort risk, applied to the RTIC and HAL crates | 4 | 3 (schedule) | 12 / Red | new RSK-NNN if selected |
| A3 | Given REQ-SYS-129 permits one NVIC priority, there is a possibility of RTIC's macro-generated scheduling code adding audit and MC/DC scope without its preemption benefit, adversely impacting SWE-219 evidence for SW-SCHED, leading to added manual decision tables | 4 | 2 (schedule) | 8 / Yellow | RSK-010 |

Aggregate risk per alternative (maximum score): A0 9, A1 12, A2 12, A3 12. No alternative carries a Red safety risk.

**Evidence offered for the software assurance tasks** (SWEHB `swe-033-acquisition-vs-development-assessment.md` section 7.1). These tasks are confirmations by the software assurance function (charter section 2), not by the author; the confirmation, if Claude dispatches an assurance review (header row "Independent reviewer"), is recorded in the assurance reviewer's record, not here (revision 1, INSP-013 finding-9).

- **Task 1** (confirm that the options were evaluated): evidence offered in sections 2 to 5, which cover SWE-033 options a to f and the component-level disposition.
- **Task 2** (confirm the flow-down of software engineering, assurance and safety requirements to acquisition): evidence offered for A1 to A3 in SWE-027 items a to f and SWE-211, which would apply to every crate, and for A0 in this plan's full process applied to every work package (07 sections 3.4, 19).
- **Task 3** (assess the risks of the acquisition versus development decision): evidence offered in the risk table above.

| Alternative | Benefits beyond the scored criteria |
|---|---|
| A0 | One HAL and one audit trail shared with the owner's other rustos work (ADR-019; the Juno planning baseline in the rustos README). The tutorial-grade documentation doubles as the developer's manual (07 section 1.3 row w). The image contains no code the owner has not reviewed |
| A1 | Broad, community-reviewed RP2350 driver coverage, including PIO, which TS-001 candidate B would need |
| A2 | Async task structure and a broad driver set, including PIO and DMA helpers |
| A3 | Compile-time checked resource sharing and deadlock freedom under the stack resource policy |

## 8. Recommendation

- **Recommended alternative:** A0, rustos (`api` plus `pico2`) extended upstream per ADR-019, total 400 (80 %).
- **Rationale:** A0 is the highest total and the ranking is robust.
  - Under Class A, buying the runtime moves effort from writing drivers into verifying ten or more external crates to developed-code level, with register accesses the project cannot trace to the datasheet.
  - A0 is the only alternative whose host testing through injected traits is already demonstrated here (F13).
  - A0 is the only alternative whose mechanisms are exactly those the design rules and the emulator credit scope allow.
  - The owner's direction (SI-007, SI-033) fixes rustos, and this study records what that costs: twelve work packages carried by RSK-013, a single maintainer carried by RSK-023, and a hygiene pass on the current rustos tree before FW-B0.
- **Closely ranked alternatives presented for the owner's choice:** none. The second total (A1, 265) is 135 points behind.
- **Owner decision requested at SRR:** approve A0 as the firmware runtime and HAL in `docs/reviews/SRR/decision-memo.md`. The approval closes the SWE-033 shortfall of SRR package item H14 (trade study part) together with the independent review record.
- **Impacts of adopting the recommendation:**
  - **Requirements:** no new requirement beyond those ADR-019 section 4.1 already names: a REQ-SW-NNN that drivers live in rustos `pico2` behind `api` traits with no cwht-local register access, verified by Inspection (`cargo tree`); and the REQ-SW-HAL-* trait contracts written with each work package at PDR.
  - **Interfaces:** `ICD-CTL-SW` (pin map and peripheral allocation, PDR) and the rustos `docs/icd/rp2350/` extractions for TIMER, PWM, ADC, WATCHDOG and QMI (ADR-019 section 4.2).
  - **Cost model:** no delta.
  - **Schedule:** as already planned in 07 sections 3.2 and 19.
  - **Verification cases:** the contract tests and dev-board checks of 07 section 19 per work package, with the hygiene item (`rustos-toolchain-proof.md` work package WP-13) first so the `-D warnings` gate of FW-B0 can pass.
  - **RMM:** row SWE-033 implementation text can cite `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` once the owner approves (RMM owner).
- **Corrective actions if the recommendation is adopted late:** FW-B0 cannot close without the runtime decision (07 section 3.2). A decision after SRR moves the toolchain proof and the start of WP-SW-01 by the same delay; RSK-013 is re-scored at that point.
- **Proposed revisit triggers** for the owner to adopt, or amend, with the decision (06 section 14.6); moved here from section 10 in revision 1 (INSP-013 finding-10):
  - the owner as rustos maintainer declines an `api` addition a work package needs (the ADR-019 revisit condition);
  - RSK-013 turns Red at a gate;
  - a qualified Rust runtime or HAL for Cortex-M33 with Class A-grade evidence becomes available;
  - the owner directs a CR that relaxes CS-02.

## 9. Dissent

| Who | Date | Dissent (criteria, weights, scores or recommendation) | How it was addressed |
|---|---|---|---|
| reviewer:trades (INSP-013 dissent D-2) | 2026-09-25 | C1 (external crate count), C2 (register auditability) and C4 (unsafe surface) all grow with the amount of third-party code in the image and together carry 40 of the 100 weight points; the study does not discuss this dependence. With C2 and C4 removed and the rest rescaled: A0 387.5, A1 293.8 | Accepted as a limitation: the three criteria are correlated through the amount of bought code, though each measures a distinct obligation (SWE-027 item e verification, charter section 9 datasheet traceability, CS-07 unsafe audit). The reviewer's recomputation leaves A0 first by 93.7 points, so the recommendation stands. No software assurance review has run (header) |

## 10. Decision

Empty until the owner decides (06 section 14.5; charter section 2).

- **Decision:**
- **Decided by:**
- **Rationale as stated by the owner:**
- **Records produced:**
- **Revisit conditions:**
- **Lessons learned (SE HB sections 6.8.1.2.7 and 6.8.1.3.1):**

## 11. References

- NPR 7150.2D §3.1.2 [SWE-033], §3.1.14 [SWE-027] items a to f, §3.8.1 [SWE-146], §4.5.14 [SWE-211] (`docs/references/md/npr-7150-2d/03-chapter3.md`, `04-chapter4.md`)
- SWEHB `docs/references/md/swehb/swe-033-acquisition-vs-development-assessment.md` sections 1.1 (options a to f) and 7.1 (software assurance tasks 1 to 3); `docs/references/md/swehb/7-03-acquisition-guidance.md` (make-or-buy study planning)
- NASA/SP-2016-6105 Rev 2 (SE HB) §6.8.1.2.1 to §6.8.1.2.7, Table 6.8-1 (`docs/references/md/nasa-se-handbook/22-6-8-decision-analysis.md`)
- `docs/process/00-charter.md` sections 1, 9, 10, 12; `docs/process/06-risk-and-decision-analysis.md` sections 13, 14; `docs/process/07-software-engineering-plan.md` sections 1.2, 1.3, 3.1, 3.2, 7.1, 7.2, 7.7, 14.1, 17.1 to 17.4, 19, 21; `docs/process/01-lifecycle-and-reviews.md` section 4.3 row 23
- `docs/reviews/SRR/package.md` section 2 item H14 and section 16
- ADR-001, ADR-004, ADR-011, ADR-017, ADR-019 (`docs/decisions/adr/`)
- `docs/research/rustos-toolchain-proof.md` (2026-09-25); `docs/research/emulator-accreditation-and-timer-irq.md` (2026-09-25)
- rustos `/Users/robinonsay/rust/rustos/README.md`; `/Users/robinonsay/rust/rustos/docs/tutorials/rp2350_baremetal/02_linker_scripts.md` section 2.8
- `docs/requirements/sys/requirements.json` (REQ-SYS-128, REQ-SYS-129); `docs/requirements/l0-stakeholder/stakeholder-inputs.md` (SI-007, SI-015, SI-025, SI-026, SI-033); `docs/risk/register.json` (RSK ids above)

## Appendix A. Supporting analysis

- **Literature and research search:** Claude Context searches over `/Users/robinonsay/rust/cwht` (2026-09-25) were run before any manual search. Queries: "Firmware runtime and HAL make/buy trade study rustos versus Embassy RTIC rp-hal section 17.2"; "rp235x-hal embassy-rp RTIC cortex-m-rt dependency count unsafe comparison rustos"; "Embassy async executor RTIC framework rp235x-hal crate third-party HAL research finding"; "SWE-033 assess options for software acquisition versus development NPR 7150.2D 3.1.2". A query over `/Users/robinonsay/rust/rustos` ("why not Embassy or RTIC or rp-hal; rationale for own OS") found the README and tutorial passages cited. The searches confirmed that no `docs/research/` report covers the bought alternatives. SWE-033, SWE-027, SWE-146 and SWE-211 were pinned by `grep` in `docs/references/md/npr-7150-2d/`. The local cargo registry holds none of the bought crates, so no dependency tree could be measured without a download. License metadata (revision 1): the crates.io API record of each top-level crate (`https://crates.io/api/v1/crates/<name>`, newest version, field `license`) was read on 2026-09-25 for `rp235x-hal`, `rp235x-pac`, `cortex-m-rt`, `cortex-m`, `embedded-hal`, `critical-section`, `embassy-rp`, `embassy-executor`, `embassy-time`, `rtic` and `rtic-monotonics`; this reads JSON metadata only and downloads no crate. Results are in section 4, M3.
- **Previous related decisions and dissent:** ADR-004, ADR-011, ADR-019; none dissented.
- **Detailed analysis:** totals and sensitivity by the script of TS-001 Appendix A.3; results row "TS-002" of its table.
- **Decision metrics:**
  - Time from open to recommendation: same day (2026-09-25).
  - Alternatives: 4 scored and 5 pruned.
  - Criteria: 4 mandatory and 7 enhancing.
  - Criteria revisions: 0 (revision 1 changed evidence and wording, not criteria or weights).

## Change log

Revisions before the decision only; after the decision the file is immutable except for the Status line (06 section 14.6).

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-25 | Initial | SRR package item H14 (SWE-033; 01 section 4.3 row 23) |
| 1 | 2026-09-25 | M3 for A1 to A3 evidenced from crates.io license metadata (transitive crates recorded as not assessed, no effect on the ranking); software assurance tasks reworded as evidence offered, with the assurance-review question referred to Claude; proposed revisit triggers moved from section 10 to section 8; reviewer dissent D-2 recorded | INSP-013 findings F-08 to F-10 |
