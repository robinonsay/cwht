# ADR-026: Semi break-in only, with a 3 to 30 dit hang and a constant lead-in (supersedes ADR-010)

| Field | Value |
|---|---|
| ID | ADR-026 |
| Status | Proposed, pending owner decision at SRR |
| Date proposed | 2026-09-25 |
| Date decided | pending (SRR; package decision 47 of `docs/reviews/SRR/decisions-for-owner.md`) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (a) architecture choice: the T/R architecture class; (c) touches HZ-004, HZ-005 and HZ-008 and the components `SW-TXSEQ` and `SW-KEYER` of `docs/process/07-software-engineering-plan.md` section 14.1). No TS for the break-in mode, which the owner fixed in SI-036; admitted without a TS only under the customization of 06 section 14.1 proposed in `reconciliation-srr.md` section 6, otherwise a TS-NNN is required. The T/R element is class 1 (a) and (b) and goes through the T/R element TS at PDR |
| Decision authority | Robin (owner; the decision fixes a functional-baseline behaviour and the T/R architecture class) |
| Author | Claude (ADR author invocation applying INSP-011, 2026-09-25) |
| Independent reviewer | Pending: INSP-011 iteration 2 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`, re-review of the ADR set including this ADR) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

ADR-010 (Accepted) records the owner's semi break-in decision (SI-036) and adds hang and lead-in values that the requirement authors have since replaced. ADR-010 section 2 gives a hang default of 8 dits with 6.1 dits and a fixed 50 to 2500 ms selectable, and a first-element lead-in of at most 12 ms. REQ-SYS-044 and REQ-SW-KEYER-032 give an operator-set hang of 3 to 30 dits (TBR) at the displayed speed, REQ-SYS-136 keeps 8 dits as the default, and REQ-SYS-161 gives the same lead-in of at most 12 ms (TBR) for every element of an over. The fixed-millisecond floor would release the relay between elements below 24 WPM, which is the full QSK behaviour SI-036 excludes (REQ-SYS-044 rationale; `docs/research/tr-switch-candidates.md` F5). The independent review INSP-011 (finding F-04) recorded the conflict. An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), so the aligned decision is this new ADR. It restates all of ADR-010 with the aligned values.

- Driving inputs and expectations: SI-036, SI-035, SI-018 (paddles at speed), SI-033 (50 WPM), SI-005; NGO-003, NGO-014, MOE-005, CON-021; OPS-004, OPS-005
- Requirements that constrain the decision: REQ-SYS-041 (5 to 50 WPM, ADR-024), which spans the hang in milliseconds; REQ-SYS-157 (receive audio held muted through transmit and the hang)
- Hazards in play (`docs/safety/hazards.json` 0.3.0-pha): HZ-004 (the sequencer that implements break-in also gates PA enable; `SW-TXSEQ` in 07 section 14.1); HZ-005 (control K4: receive audio held muted through transmit and the hang, REQ-SYS-157); HZ-008 (cause C3, a PIN T/R switch after the filter regenerating harmonics, does not apply to the relay baseline this decision permits)
- Research consulted: `docs/research/tr-switch-candidates.md` F4 (listening window versus switching time; hang 8 dits is 384 ms at 25 WPM, 192 ms at 50 WPM), F5 (relay life: full QSK exhausts a G6Z in 24 to 79 h and an HF3 in 238 to 794 h of keying), implications TR-01 to TR-08, D-TR-1 to D-TR-4, "Recommendation for rev A"; `docs/research/keyer-and-key-interfaces.md` F9 (semi break-in conventions), D5; `docs/research/keyer-verification-and-key-input-network.md` F11 (hand-key timeline for semi break-in; hang in dits of the displayed WPM in every mode), D-KN4; `docs/research/2m-cw-transceiver-reference-designs.md` F28 to F31 (T/R and envelope precedents)
- Guidance consulted: 47 CFR 97.307(b) (corpus: 47cfr-97.307.md, eCFR issue 2026-09-23; no key clicks, so the sequencer never opens the T/R switch under RF); SWE-134; SE HB §6.8.1.2.2
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. A relay-class T/R element meets the 12 ms lead-in with operate plus bounce time. Confirmed by the T/R element TS at PDR from datasheet timing, then by Bench logic capture at TRR (REQ-SYS-161 TBR closes at PDR).
  2. A 3-dit floor keeps the relay closed within a character at every speed from 5 to 50 WPM. Shown by the REQ-SYS-044 rationale arithmetic; confirmed in the owner's HITL session on the dev board at PDR (07 section 3.1 PDR row).
  3. The owner and friends accept an audible relay click in semi break-in. Confirmed in the HITL session at PDR; if not, the PIN switch used only in semi break-in becomes the T/R TS outcome within this ADR's scope.

## 2. Decision (proposed)

Rev A implements semi break-in only. While sending, the operator hears the sidetone and not the band. After the last key-up the radio returns to receive after an operator-set hang time of 3 to 30 dits (TBR) at the displayed speed, default 8 dits (REQ-SYS-044, REQ-SYS-136). The hang counts in dits of the displayed WPM in every keyer mode, Straight included. There is no fixed-millisecond hang option and no 6.1-dit preset. Full QSK is excluded from rev A and is not a configuration option. The T/R element may therefore be a sequenced RF relay (TE Axicom HF3 class, 1 Form C, normally-closed contact to the receiver so the unpowered state is receive), with cold switching enforced by the sequencer: T/R to transmit, wait for operate plus bounce, PA bias on, raised-cosine rise; on key-up the envelope falls completely, bias off, guard, T/R to receive after the hang. Every radiated element of an over is delayed by the same lead-in of at most 12 ms (TBR) after the receive-to-transmit changeover (REQ-SYS-161), and the RF rise begins within 15 ms (TBR) of each straight-key contact closure (REQ-SYS-160). The harmonic low-pass filter sits at the antenna port after the T/R node, and the LNA supply is off during transmit. The T/R element itself (HF3 versus other relays versus a PIN switch used only in semi break-in) is chosen by the T/R element trade study at PDR within this scope.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (proposed) | Semi break-in only; hang 3 to 30 dits, default 8; constant lead-in of at most 12 ms; relay-class T/R permitted | Owner decision on the mode (SI-036); the dit-referenced floor keeps the relay closed within a character; values match REQ-SYS-044, REQ-SYS-136, REQ-SYS-160, REQ-SYS-161 and package decision 47 |
| B | ADR-010 values: default 8 dits, 6.1 dits and a fixed 50 to 2500 ms selectable; first-element lead-in only | Not recommended: a 50 ms fixed hang releases the relay between elements below 24 WPM, which is per-element switching that SI-036 excludes and the relay wear case of `tr-switch-candidates.md` F5 |
| C | Full QSK with a PIN quarter-wave switch (research recommendation P1) | Rejected by the owner (SI-036); adds a bias network, a second protection stage, LPF ordering constraints and a 1 ms receiver recovery requirement |
| D | QSK-capable hardware with semi break-in as the firmware default | Rejected: pays the hardware cost of C for a feature the owner explicitly does not want |
| E | Relay operated in full QSK | Rejected: relay life 24 to 794 h of keying (F5) |

No trade study for the break-in mode: the owner's direction leaves option A as the only viable mode, and the alternatives are recorded per SE HB §6.8.1.2.2. The class 1 status of this choice is stated in the header; the T/R element trade at PDR is class 1 (a) and (b).

## 4. Consequences

### 4.1 Requirements created or changed

Requirement ids below are those allocated by the requirement authors (`source_ids` of `docs/requirements/sys/requirements.json` and `docs/requirements/sw/sw-keyer/requirements.json` on 2026-09-25). When this ADR is Accepted, each requirement that cites ADR-010 adds ADR-026 to `source_ids` (cross item to the requirement authors).

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-044 (semi break-in hang, 3 to 30 dits, TBR) | allocated, cites ADR-010; value adopted by this ADR | TBR closes at PDR (sequencer timing table against relay timing) |
| REQ-SYS-136 (configuration defaults, 8-dit hang) | allocated; default adopted by this ADR | |
| REQ-SYS-160 (straight-key contact to RF within 15 ms, TBR) | allocated, cites ADR-010 | TBR closes with the T/R element TS at PDR |
| REQ-SYS-161 (constant lead-in of at most 12 ms, TBR) | allocated, cites ADR-010; replaces the ADR-010 "first-element" wording | TBR closes with the T/R element TS at PDR |
| REQ-SW-KEYER-018 (straight-key closure latency) | allocated, cites ADR-010 | |
| REQ-SW-KEYER-032 (end of over after a 3 to 30 dit hang, TBR) | allocated, cites ADR-010; value adopted by this ADR | |
| REQ-TX T/R sequencing, fail-safe receive state, LPF after the T/R node, LNA off in transmit (candidates TR-02 to TR-05) | not created: the TX L2 file has no T/R sequencing requirement yet; allocated with the T/R element TS at PDR | HZ-008 control K1 already records the filter position at the antenna port |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT`; an internal T/R sequencer ICD (timing table per element, bias, GPIO polarity, fail-safe state) created by the architecture ADR at PDR
- Design elements created or changed: T/R block (relay class), TX sequencer, envelope shaper; receiver mute path
- New `SW-<SUB>` modules created by this ADR: none (`SW-TXSEQ` is named in 07 section 14.1; the architecture ADR at PDR fixes its units)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: the closing cases named in the `verification_note` of each requirement in section 4.1 (for example TC-SW-KEYER-032, hang settings 3, 8 and 30 dits at 5, 15 and 50 WPM, HostUnit); T/R sequencer ordering by Emulation with logged GPIO timestamps and durations by Bench logic capture; relay operate and release by Bench; owner paddle QSO by Demonstration
- Evidence class implications: no oscilloscope; T/R timing by Emulation (ordering) plus Analysis (relay datasheet) plus Bench logic capture (04 section 6 instrument table)
- Hazard analysis update required: yes. HZ-004: the sequencer and the relay fail-safe state are controls. HZ-005: K4 holds receive audio muted through the hang, so the hang range bounds the mute duration. HZ-008: cause C3 is recorded as not applicable to the relay baseline. Cross item to the hazard analysis author: add ADR-026 to the sources of HZ-004 and HZ-005
- Safety-critical software scope (SWE-134 provisions) changed: no (`SW-TXSEQ` and `SW-KEYER` are already in 07 section 14.1)

### 4.4 Cost, schedule, risk

- BOM impact: one RF relay (HF3 class about 15 x 7 x 10 mm, 2.5 g, 6 V coil from the pack, about 23 mA during transmit) instead of PIN diodes and bias parts
- Gate affected: SRR (value decision 47), PDR (T/R element trade)
- Risks opened, closed or re-scored: relay-wear risk in QSK is retired before it is opened; the proposed risks "relay lifecycle and stock unverified" and "audible relay click disliked by friends" of ADR-010 carry over; RSK-012 unchanged
- TPMs affected: TPM-013 sub-measure (b): the provisional key-to-RF latency of 5 ms or less is not reachable with a relay lead-in of 8 to 12 ms; the TPM owner is asked to restate (b) as the REQ-SYS-161 constant lead-in of at most 12 ms when the TBR closes at PDR (unchanged from ADR-010)

## 5. Compliance and tailoring

none

## 6. Decision record

Pending. Proposed wording for the SRR decision memo (package decision 47): "Semi break-in only (SI-036). Hang 3 to 30 dits at the displayed speed, default 8 dits, replacing the 6.1-dit and 50 to 2500 ms options; the same lead-in of at most 12 ms for every element of an over. ADR-026 is Accepted and ADR-010 becomes Superseded by ADR-026." The owner's statement of the mode is already on record:

> Owner (2026-09-25, SI-036): "Break-in: semi break-in only. The operator hears their own sidetone while sending and the radio returns to receive after an adjustable hang time; full QSK (hearing between elements) is explicitly not wanted. Closes the open item in SI-035."

The owner's disposition of decision 47 will be transcribed here verbatim with its date. Until then this ADR is Proposed and ADR-010 stays Accepted.

## 7. Related

- Supersedes: ADR-010 (on acceptance; ADR-010's Status then reads "Superseded by ADR-026")
- Superseded by: none
- Trade study: none for the mode (see header); T/R element TS at PDR (relay candidates and a PIN switch used only in semi break-in), scoped by this ADR, id allocated at creation
- Review where presented: SRR (decision 47 requested); INSP-011 finding F-04 is the origin of this ADR
- Revisit conditions: the owner asks for QSK after on-air use (rev B; a superseding ADR and a new T/R trade); the T/R trade finds no relay with verified stock and lifecycle by CDR (then a PIN switch in semi break-in, same ADR intent); the PDR sequencer timing table shows the 3-dit floor releases the relay within a character at some speed (then the floor rises by CR)
