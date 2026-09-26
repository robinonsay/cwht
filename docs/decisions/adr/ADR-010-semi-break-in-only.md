# ADR-010: Semi break-in only; full QSK excluded from rev A

| Field | Value |
|---|---|
| ID | ADR-010 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (a) T/R architecture class; (c) HZ-004, HZ-005, HZ-008 and the `SW-TXSEQ` and `SW-KEYER` components of 07 section 14.1). Owner-directed (SI-036). Trade study: the T/R element study at PDR (section 7). No trade study for the break-in mode: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr`. ADR-026 (Proposed, package decision 47) restates this decision with the requirement values and supersedes it on acceptance |
| Decision authority | Robin (owner; the decision fixes a functional-baseline behaviour and the T/R architecture class) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-03 and F-04 (hazard line re-derived as for F-02) against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

Break-in behaviour decides the T/R architecture. Full QSK (hearing the band between elements) needs a solid-state switch that changes state within tens of microseconds, receiver mute and AGC recovery within about 1 ms, a second receiver-protection stage and a diode bias network; a relay in full QSK would wear out in 24 to 794 hours of keying. Semi break-in (receiver returns after a hang time) tolerates a relay with a 3 to 5 ms operate time. The trade was explained to the owner on 2026-09-25 (SI-035) and the owner decided: semi break-in only, full QSK explicitly not wanted (SI-036).

- Driving inputs and expectations: SI-036, SI-035, SI-018 (paddles at speed), SI-033 (50 WPM), SI-005
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-004 (the sequencer that implements break-in also gates PA enable), HZ-005 (control K4: receive audio held muted through transmit and the hang, REQ-SYS-157) and HZ-008 (cause C3, a PIN T/R switch after the filter regenerating harmonics, does not apply to the relay baseline this decision permits); the same set as ADR-026 section 1
- Research consulted: `docs/research/tr-switch-candidates.md` F4 (listening window versus switching time; semi break-in hang 8 dits is 384 ms at 25 WPM, 192 ms at 50 WPM), F5 (relay life: full QSK exhausts a G6Z in 24 to 79 h and an HF3 in 238 to 794 h of keying; semi break-in gives thousands of hours), implications TR-01 to TR-08, D-TR-1 to D-TR-4, "Recommendation for rev A" (PIN switch P1 recommended for QSK; TE Axicom HF3 54 named as the element if the owner chooses semi break-in only); `docs/research/keyer-and-key-interfaces.md` F9 (semi break-in conventions: Auto 8 dits, Contest 6.1 dits, custom ms; PTT lead-in), D5; `docs/research/keyer-verification-and-key-input-network.md` F11 (hand-key timeline for semi break-in: T_lead 5 ms, first-element extension, key-up overhang equals full fall plus 1 ms, hang 8 dits of the displayed WPM), D-KN4; `docs/research/2m-cw-transceiver-reference-designs.md` F28 to F31 (T/R and envelope precedents)
- Guidance consulted: 47 CFR 97.307(b) (no key clicks; the sequencer never opens the T/R switch under RF); SWE-134; SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. A relay-class T/R element meets the 12 ms lead-in with operate plus bounce time. Confirmed by the T/R element trade study at PDR from datasheet timing, then by Bench logic capture at TRR (REQ-SYS-161 TBR closes at PDR).
  2. The hang keeps the relay closed within a character at every speed from 5 to 50 WPM. The hang values of section 2 differ from REQ-SYS-044 and REQ-SW-KEYER-032 (3 to 30 dits, TBR); ADR-026 carries the requirement values and its assumption 2 (INSP-011 F-04, package decision 47). Confirmed in the owner's HITL session on the dev board at PDR.
  3. The owner and friends accept an audible relay click in semi break-in. Confirmed in the HITL session at PDR; if not, the PIN switch used only in semi break-in becomes the T/R trade study outcome within this ADR's scope.

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
| REQ-SYS-044 (semi break-in hang time, TBR) | allocated; cites this ADR | Value differs from section 2: 3 to 30 dits (TBR), no fixed-millisecond option; REQ-SYS-136 (configuration defaults) keeps the 8-dit default. ADR-026 (Proposed) adopts the requirement values (package decision 47; INSP-011 F-04) |
| REQ-SYS-160 (straight-key contact to RF latency, TBR), REQ-SYS-161 (constant lead-in over an over, TBR) | allocated; both cite this ADR | REQ-SYS-161 applies the 12 ms lead-in to every element of an over, not only the first (ADR-026) |
| REQ-TX T/R sequencing (cold switching, lead-in, envelope complete before T/R release), fail-safe receive state, LPF at the antenna port after the T/R node, LNA supply off in transmit (candidates TR-02 to TR-05) | not created: the TX L2 file has no T/R sequencing requirement yet; allocated with the T/R element trade study at PDR | HZ-008 control K1 already records the filter position at the antenna port; full-QSK clause of candidate TR-08 removed |
| REQ-SW-KEYER-018 (straight-key closure latency, TBR), REQ-SW-KEYER-032 (semi break-in hang, TBR) | allocated; both cite this ADR | REQ-SW-KEYER-032 value differs from section 2 as REQ-SYS-044 does; see ADR-026 |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT`; an internal T/R sequencer ICD (timing table per element, bias, GPIO polarity, fail-safe state) created by the architecture ADR at PDR
- Design elements created or changed: T/R block (relay class), TX sequencer, envelope shaper; receiver mute path
- New `SW-<SUB>` modules created by this ADR: none (a `SW-TXSEQ` module is named by the architecture ADR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-TX-NNN (sequencer ordering, Emulation with logged GPIO timestamps for ordering and Bench logic capture for durations), TC-TX-NNN (relay operate and release within datasheet, Bench), TC-SW-KEYER-NNN (hang time at 5, 15, 25, 50 WPM, HostUnit), TC-VAL-NNN (owner paddle QSO: the delay is acceptable, Demonstration)
- Evidence class implications: no oscilloscope; T/R timing by Emulation (ordering) plus Analysis (relay datasheet) plus Bench logic capture (04 section 6 instrument table)
- Hazard analysis update required: yes (HZ-004: sequencer and relay fail-safe state as controls; HZ-005 control K4)
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

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged; its hang values still differ from REQ-SYS-044 and REQ-SW-KEYER-032, so F-04 for this ADR closes only on package decision 47 (ADR-026 supersedes this ADR on acceptance). Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
