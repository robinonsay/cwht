# ADR-010: Semi break-in only; full QSK excluded from rev A

| Field | Value |
|---|---|
| ID | ADR-010 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes a functional-baseline behaviour and the T/R architecture class) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

Break-in behaviour decides the T/R architecture. Full QSK (hearing the band between elements) needs a solid-state switch that changes state within tens of microseconds, receiver mute and AGC recovery within about 1 ms, a second receiver-protection stage and a diode bias network; a relay in full QSK would wear out in 24 to 794 hours of keying. Semi break-in (receiver returns after a hang time) tolerates a relay with a 3 to 5 ms operate time. The trade was explained to the owner on 2026-09-25 (SI-035) and the owner decided: semi break-in only, full QSK explicitly not wanted (SI-036).

- Driving inputs and expectations: SI-036, SI-035, SI-018 (paddles at speed), SI-033 (50 WPM), SI-005
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-004 (the sequencer that implements break-in also gates PA enable)
- Research consulted: `docs/research/tr-switch-candidates.md` F4 (listening window versus switching time; semi break-in hang 8 dits is 384 ms at 25 WPM, 192 ms at 50 WPM), F5 (relay life: full QSK exhausts a G6Z in 24 to 79 h and an HF3 in 238 to 794 h of keying; semi break-in gives thousands of hours), implications TR-01 to TR-08, D-TR-1 to D-TR-4, "Recommendation for rev A" (PIN switch P1 recommended for QSK; TE Axicom HF3 54 named as the element if the owner chooses semi break-in only); `docs/research/keyer-and-key-interfaces.md` F9 (semi break-in conventions: Auto 8 dits, Contest 6.1 dits, custom ms; PTT lead-in), D5; `docs/research/keyer-verification-and-key-input-network.md` F11 (hand-key timeline for semi break-in: T_lead 5 ms, first-element extension, key-up overhang equals full fall plus 1 ms, hang 8 dits of the displayed WPM), D-KN4; `docs/research/2m-cw-transceiver-reference-designs.md` F28 to F31 (T/R and envelope precedents)
- Guidance consulted: 47 CFR 97.307(b) (no key clicks; the sequencer never opens the T/R switch under RF); SWE-134; SE HB §6.8

## 2. Decision

Rev A implements semi break-in only. While sending, the operator hears the sidetone and not the band; after the last element the radio returns to receive after an adjustable hang time (default 8 dits of the displayed speed; 6.1 dits and a fixed 50 to 2500 ms selectable). Full QSK is excluded from rev A and is not a configuration option. Consequently the T/R element may be a sequenced RF relay (TE Axicom HF3 class, 1 Form C, normally-closed contact to the receiver so the unpowered state is receive), with cold switching enforced by the sequencer: T/R to transmit, wait for operate plus bounce, PA bias on, raised-cosine rise; on key-up the envelope falls completely, bias off, guard, T/R to receive after the hang. The harmonic low-pass filter sits at the antenna port after the T/R node; the LNA supply is off during transmit. The first-element lead-in after a changeover is at most 12 ms and the hang reference is the displayed WPM in every keyer mode, including Straight. The T/R element itself (HF3 versus other relays versus a PIN switch used only in semi break-in) is chosen by the T/R trade study at PDR within this scope.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Semi break-in only; relay-class T/R permitted | Owner decision (SI-036): hearing between elements is not wanted; simplest RF path, 80 dB isolation without a second stage, no diode distortion, thousands of hours of relay life at the owner's duty |
| B | Full QSK with a PIN quarter-wave switch (research recommendation P1) | Rejected by the owner; would add a bias network, a second protection stage, LPF ordering constraints and a 1 ms receiver recovery requirement |
| C | QSK-capable hardware with semi break-in as the firmware default | Rejected: pays the hardware cost of B for a feature the owner explicitly does not want |
| D | Relay operated in full QSK | Rejected: relay life 24 to 794 h of keying (F5) |

No trade study for the break-in mode (owner decision after the explained trade); the T/R element trade at PDR is class 1 (a).

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (semi break-in with adjustable hang; sidetone while sending; L1 author allocates) | new, traces to SI-036 | |
| REQ-TX-NNN (T/R sequencing: cold switching, lead-in at most 12 ms, envelope complete before T/R release; candidate TR-03) | new at PDR, hazard HZ-004 link | Full-QSK clause of candidate TR-08 removed |
| REQ-TX-NNN (fail-safe receive: unpowered T/R state connects antenna to receiver; candidate TR-04) | new at PDR | |
| REQ-TX-NNN (LPF at the antenna port after the T/R node; LNA supply off in TX; candidates TR-02, TR-05) | new at PDR | |
| REQ-SW-KEYER-NNN (hang time default 8 dits of displayed WPM; 6.1 dits or 50 to 2500 ms selectable; first-element extension; key-up overhang) | new, parent the L1 requirement | `keyer-verification-and-key-input-network.md` implication 4 |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT`; an internal T/R sequencer ICD (timing table per element, bias, GPIO polarity, fail-safe state) created by the architecture ADR at PDR
- Design elements created or changed: T/R block (relay class), TX sequencer, envelope shaper; receiver mute path
- New `SW-<SUB>` modules created by this ADR: none (a `SW-TXSEQ` module is named by the architecture ADR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-TX-NNN (sequencer ordering, Emulation with logged GPIO timestamps for ordering and Bench logic capture for durations), TC-TX-NNN (relay operate and release within datasheet, Bench), TC-SW-KEYER-NNN (hang time at 5, 15, 25, 50 WPM, HostUnit), TC-VAL-NNN (owner paddle QSO: the delay is acceptable, Demonstration)
- Evidence class implications: no oscilloscope; T/R timing by Emulation (ordering) plus Analysis (relay datasheet) plus Bench logic capture (04 section 6 instrument table)
- Hazard analysis update required: yes (HZ-004: sequencer and relay fail-safe state as controls)
- Safety-critical software scope changed: no (PA enable and bias sequencing already in scope)

### 4.4 Cost, schedule, risk

- BOM impact: one RF relay (HF3 class about 15 x 7 x 10 mm, 2.5 g, 6 V coil from the pack, about 23 mA during transmit) instead of PIN diodes and bias parts
- Gate affected: PDR (T/R trade)
- Risks opened, closed or re-scored: relay-wear risk in QSK is retired before it is opened; new risks proposed: "relay lifecycle and stock unverified" (TE HF3 lifecycle to be verified before CDR), "audible relay click accepted by the owner but disliked by friends"; RSK-012 unchanged
- TPMs affected: TPM-013 sub-measure (b): the provisional key-to-RF latency of 5 ms or less is not reachable with a relay lead-in of 8 to 12 ms on the first element; the TPM owner is asked to restate (b) as "first-element lead-in at most 12 ms; later elements per the envelope" when the TBR closes at PDR

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-036): "Break-in: semi break-in only. The operator hears their own sidetone while sending and the radio returns to receive after an adjustable hang time; full QSK (hearing between elements) is explicitly not wanted. Closes the open item in SI-035."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none (SI-035 recorded the open question)
- Superseded by: none
- Trade study: T/R element TS at PDR (relay candidates and a PIN switch used only in semi break-in), scoped by this ADR
- Review where presented: SRR
- Revisit conditions: the owner asks for QSK after on-air use (rev B; a superseding ADR and a new T/R trade); the T/R trade finds no relay with verified stock and lifecycle by CDR (then a PIN switch in semi break-in, same ADR intent)
