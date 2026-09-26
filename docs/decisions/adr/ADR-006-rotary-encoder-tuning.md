# ADR-006: Rotary encoder tuning and a minimal control set

| Field | Value |
|---|---|
| ID | ADR-006 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the human interface of the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

The owner wants minimal controls: band (future), volume and tuning, a small LCD, and tuning by a knob, accepting a rotary encoder in place of a potentiometer (SI-006). A synthesized radio has no analog tuning voltage, so a potentiometer would need an ADC and would give no repeatable frequency; an encoder gives digital steps, a push switch and a firmware-defined feel. The choice fixes two GPIO inputs per encoder, the debounce and input-network design, the front panel layout and the HSI section of the SEMP.

- Driving inputs and expectations: SI-006, SI-005 (tune to a frequency and chat), SI-012 (printed knobs), SI-001 (pocket size)
- Requirements that constrain the decision: none yet
- Hazards in play: none (tuning is mission-critical, not safety-critical, 03 section 4.3)
- Research consulted: `docs/research/display-and-ui-parts.md` F12 (Bourns PEC11R: 24 detents, 24 pulses, push switch, 2 ms bounce, 30,000 cycles, M7 bushing, wave solder only), F14 (Alps EC11E alternative), F15 (volume options: pot limited to -10 C; second encoder with firmware volume), F16 (Omron B3F buttons, 5 ms bounce), D-UI-03, D-UI-04, D-UI-07, D-UI-08 (recommendations); `docs/research/rustos-toolchain-proof.md` F11 (RP2350-E9: external pull-ups, no internal pull-downs), DECISION (1 kHz timer-sampled polling recommended over edge IRQ or PIO)
- Guidance consulted: SE HB App. R (HSI) via SEMP section 7.3; SE HB §6.8

## 2. Decision

Tuning is by a detented rotary encoder with a push switch (Bourns PEC11R-4215F-S0024 class, 24 detents and 24 pulses, proposed part), decoded in firmware with a velocity-dependent step size. Volume is a second encoder of the same part with the volume law in firmware (proposed; D-UI-04), which also gives sidetone relative-to-volume behaviour and transmit mute for free. Two tactile buttons (Omron B3F-1052 class, proposed) provide menu and function. The LCD is a small reflective memory LCD (Sharp LS013B7DH03 128 x 128, proposed, no backlight in rev A). Knobs are printed on the owner's H2C (SI-012). Encoder and button inputs are switch-to-ground with external pull-ups (RP2350-E9), sampled at 1 kHz from the timer alarm (proposed) rather than by edge interrupts. A band control is reserved in the UI design but not exposed in rev A (ADR-002).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Detented encoder with push for tuning; second encoder for volume; two buttons | Owner accepted the encoder (SI-006); repeatable digital steps; one BOM line for both knobs |
| B | Potentiometer tuning (owner's original wording) | Rejected: incompatible with a synthesizer; no repeatable frequency display; ADC noise |
| C | Analog volume pot (PTV09A) | Not chosen for the baseline: -10 C lower temperature limit, loses firmware sidetone and mute behaviour; kept as alternate if the audio chain becomes fully analog |
| D | Keypad or touchscreen | Rejected: violates the minimal-controls direction |
| E | Non-detented encoder with velocity tuning only | Rejected: detents give the tactile step the owner expects from a knob |

No trade study: the owner accepted the encoder; part-level choices are class 2 and are recorded here as proposals for the PDR UI design.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (controls: tuning knob, volume, display; L1 author allocates) | new, traces to SI-006 | |
| REQ-CTL-NNN (encoder electrical interface: switch-to-ground, external pull-up, sample rate, bounce tolerance 2 ms) | new at PDR | Candidate from `display-and-ui-parts.md` |
| REQ-SW-NNN (tuning step and velocity law; frequency display resolution) | new at PDR | Ties to ADR-016 and ADR-023 (10 Hz BFO steps) |

### 4.2 Interfaces, design and code

- ICDs affected: none external
- Design elements created or changed: front panel layout (two M7 bushings, two buttons, display window), UI firmware module, input sampling design (shared with the key inputs, ADR-009)
- New `SW-<SUB>` modules created by this ADR: none (a `SW-UI` module is named by the architecture ADR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SW-NNN (quadrature decode and velocity law, HostUnit with golden vectors), TC-CTL-NNN (bounce immunity, Bench), TC-VAL-NNN (owner tunes to a given frequency within a time limit, Demonstration)
- Evidence class implications: HostUnit covers decoding; Bench covers feel
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- BOM impact: two encoders about USD 3 each, two buttons, display about USD 20 to 30 class
- Gate affected: PDR (UI design, panel layout)
- Risks opened, closed or re-scored: none
- TPMs affected: none directly; four GPIO for encoders and two for buttons within the pin budget (F14)

## 5. Compliance and tailoring

Human Systems Integration is customized as a SEMP section (charter section 12); this ADR is an input to it. No RMM row.

## 6. Decision record

> Owner (2026-09-25, SI-006): "Controls kept minimal: band (future), volume, tuning; a small LCD; tuning via a knob (rotary encoder accepted in place of a potentiometer)."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none (display and headphone-amplifier choices belong to the audio and display trades at PDR)
- Review where presented: SRR
- Revisit conditions: the owner's HITL session at PDR rejects the encoder feel (then detent count or velocity law changes, not the encoder); board area (TPM-009) forces a single shared encoder with a mode press
