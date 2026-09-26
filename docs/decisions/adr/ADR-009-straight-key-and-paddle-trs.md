# ADR-009: Straight key and iambic paddle on one 3.5 mm TRS jack with a built-in keyer

| Field | Value |
|---|---|
| ID | ADR-009 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-001, HZ-004, HZ-010, HZ-014 and the `SW-KEYER` component of 07 section 14.1). Owner-directed (SI-018, SI-034). Trade study: the key-type detection and envelope shaping study at PDR (section 7). No trade study for the jack and key interface: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision fixes a core requirement of the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

The owner's core requirement is that the radio support both a straight key and iambic paddles with a built-in electronic keyer (SI-018). The owner's own key and paddle use standard 3.5 mm TRS plugs, brands unknown (SI-034). The industry convention (tip = dit or hand key, ring = dah, sleeve = ground) and a documented hazard (a mono TS plug grounds the ring and causes continuous keying) fix the jack, the two independent inputs, the power-on interlock and the input protection network. The keyer is firmware, so `SW-KEYER` exists from SRR (02 section 2.2).

- Driving inputs and expectations: SI-018, SI-034, SI-005, SI-019 (friends' keys may use mono plugs), SI-033 (speed range, ADR-024), SI-036 (semi break-in, ADR-010)
- Requirements that constrain the decision: none yet (this ADR is the source of the key-interface requirements)
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-004 (unintended or stuck transmission from a key input fault), HZ-001, HZ-010 (ESD and RF pickup on the key inputs: REQ-SW-KEYER-019, REQ-SYS-047 to REQ-SYS-051) and HZ-014 (key-closed interlock re-run after every reset: REQ-SW-KEYER-022, control K6)
- Research consulted: `docs/research/keyer-and-key-interfaces.md` F1 (TRS convention; mono-plug trap documented by Elecraft and QRP Labs), F2 (key-type selection strategies), F3 (iambic A versus B), F7 (contact bounce), F11 (RP2350 input facts, E9, ESD), D2, D8, D11; `docs/research/keyer-verification-and-key-input-network.md` F2 to F5 (input network derived once: 10 kOhm pull-up, 1 kOhm series, 4.7 nF, TPD2E2U06 clamp, BAT54S at the pad), F6 (debounce 2 ms close, 5 ms open, TBR), F11 (hand-key semantics through the sequencer), F13 (stuck-key and mono-plug controls: interlock, firmware timeouts, independent hardware cutoff), F14 (reconciled numbers), D-KN8 (interlock plus menu, no automatic mode change); `docs/research/display-and-ui-parts.md` F17 to F19 (Same Sky SJ1-3535N switched TRS jack; ring switch as plug detect); `docs/research/rustos-toolchain-proof.md` F11 (no internal pull-downs), F13 (host-testable key logic)
- Guidance consulted: SWE-134 (keying is safety-critical, 03 section 4.3); SE HB App. C (one requirement per key type, 02 section 4.6 worked example); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The owner's key and paddle are wired tip = dit (SI-034). Confirmed by the plug check at the PDR HITL session.
  2. The debounce and network values (TBR) suit the owner's contacts. Confirmed by the bounce capture before the TBR closes at PDR.
  3. Menu-only key-type selection is acceptable. Confirmed in the HITL session at PDR.

## 2. Decision

The radio has one KEY jack: a 3.5 mm three-conductor (TRS) panel jack (Same Sky SJ1-3535N class with tip and ring switches, proposed part), wired tip = dit and hand key, ring = dah, sleeve = signal ground. Tip and ring are sensed as two independent inputs sampled at 1 kHz so a squeeze is observable. The key type is selected by menu (Straight on tip by default with "ring" and "both" options; Iambic A default; Iambic B, Ultimatic and Bug available); there is no automatic key-type detection in rev A. Every key input carries the network 10 kOhm pull-up to 3.3 V, 1.0 kOhm series, 4.7 nF at the pad, a TPD2E2U06 clamp at the jack and a BAT54S at the pad (proposed values, TBR closing at PDR), with the RP2350 pad configured input-enabled, Schmitt on, internal pulls off (RP2350-E9). At power-on the keyer arms only after both inputs have been open for at least 500 ms; otherwise the display shows a key-closed message (mono-plug and stuck-key control). The built-in keyer is the `SW-KEYER` firmware module with host-tested timing logic. Both key types produce the same A1A envelope through the same sequencer and shaper.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | One TRS jack, tip dit and hand key, ring dah; menu-selected key type; interlock at power-on | Matches the owner's plugs (SI-034) and the field convention (F1); one hole in a pocket radio; interlock removes the mono-plug hazard |
| B | Two jacks, one per key type | Rejected: second panel hole and jack for no electrical gain; hand keys still need TRS wiring |
| C | 6.35 mm jack | Rejected: pocket radio panel; the owner's plugs are 3.5 mm |
| D | Automatic key-type detection at power-on (PicoKeyer pattern) | Deferred to rev B: ambiguous with a single-lever paddle held at boot; Class A rigor argues for fewer automatic mode changes (D-KN8) |
| E | Jack with mechanical insertion switch selecting the type | Rejected: the switched jack's contacts serve as plug detect, not type detect; a TRS plug cannot signal its wiring |

No trade study: SI-018 and SI-034 fixed the interface; the input network and debounce values are class 2 and carry TBRs.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-038 (straight-key keying), REQ-SYS-039 (iambic paddle keying) | allocated, one per key type (02 section 4.6); both cite this ADR | KDR candidates |
| REQ-SYS-174 (key jack wiring) | allocated at L1; cites this ADR | The CTL L2 pin-out requirement (candidate CTL-KEY-01, `interface` tag, `design_refs` ICD-CTL-KEY) is created at PDR |
| Two independent inputs at 1 kHz, contact sensing thresholds, input network values, ESD and abuse bounds (candidates CTL-KEY-02 to CTL-KEY-05) | REQ-SYS-047 to REQ-SYS-051 at L1 (HZ-010); REQ-SW-KEYER-019 (key input sampling period; cites this ADR); REQ-CTL at PDR | Values TBR close at PDR |
| Modes Straight, Iambic A default, Iambic B, Ultimatic, Bug; key-type by menu; power-on interlock 500 ms; stuck-key timeouts | REQ-SW-KEYER-001 to REQ-SW-KEYER-005, REQ-SW-KEYER-019, REQ-SW-KEYER-022, REQ-SW-KEYER-024 and REQ-SW-KEYER-038 cite this ADR (HZ-004 on REQ-SW-KEYER-002, 019, 022 and 024); REQ-SW-KEYER-006 to REQ-SW-KEYER-012 and REQ-SW-KEYER-026; REQ-SYS-040, REQ-SYS-052, REQ-SYS-053, REQ-SYS-054, REQ-SYS-056 | Safety-critical (SWE-134) |
| Independent hardware PA-enable cutoff, T_max 10 s, 7.5 to 13 s | REQ-SYS-055 (hardware transmit cutoff, TBR) at L1, HZ-004 control K5; REQ-CTL at PDR | Proposed, pending owner decision at SRR (D-KN2) |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-CTL-KEY` (external stub before SRR: pin-out, pull-up, series R, TVS, RC, jack part, position relative to the headphone jack), `ICD-CTL-PHONES` (same jack family; cross-plugging survivability)
- Design elements created or changed: key input network, `SW-KEYER` module (`docs/requirements/sw/sw-keyer/`, `docs/test_cases/sw-keyer/`), TX sequencer and envelope shaper (named by the architecture ADR)
- New `SW-<SUB>` modules created by this ADR: `SW-KEYER` (exists from SRR per 02 section 2.2; this ADR is its origin record)
- ICDs created by this ADR: none (the stub is created by the ICD process before SRR)

### 4.3 Verification and safety

- Verification cases to add or change: TC-SW-KEYER-NNN (golden paddle vectors for A and B, HostUnit with a simulated 1 kHz sampler and clock), TC-SW-KEYER-NNN (interlock and timeouts, HostUnit and Bench), TC-CTL-NNN (contact thresholds and network, Analysis and Bench multimeter), TC-CTL-NNN (mono plug inserted produces no transmission, Bench), TC-VAL-NNN (owner QSO with straight key and with paddle, Demonstration)
- Evidence class implications: HostUnit is primary for the keyer logic (ADR-011); Bench logic capture with a second Pico 2 (sigrok-pico, proposed) for timing; an ESD gun is not on the bench, so CTL-KEY-04 closes by Analysis and Inspection
- Hazard analysis update required: yes (HZ-004 causes and controls: mono plug, stuck contact, interlock, firmware timeouts, hardware cutoff; HZ-010 controls K1 to K3; HZ-014 control K6)
- Safety-critical software scope changed: no (keyer and PA enable already in scope)

### 4.4 Cost, schedule, risk

- BOM impact: one jack (shared BOM line with the headphone jack), TVS, diodes, passives
- Gate affected: SRR (`SW-KEYER` requirements drafted), PDR (network values, cutoff)
- Risks opened, closed or re-scored: RSK-012 (keying wrong or unusable on the built radio) stays open; HITL session at PDR exposes switchpoint and debounce defaults
- TPMs affected: TPM-013 (keyer element timing accuracy and key-to-RF latency)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-018): "Core requirement: the radio shall support both a straight key and iambic paddles (built-in electronic keyer)."

> Owner (2026-09-25, SI-034, first sentence): "Owner's straight key and paddle both use standard 3.5 mm TRS (aux) plugs; brands unknown."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: key-type detection strategy and envelope shaping method TS at PDR (`keyer-and-key-interfaces.md` A3), which may revisit alternative D
- Review where presented: SRR
- Revisit conditions: the owner's HITL session rejects menu-only key-type selection; the bounce capture (TC-KEY-BOUNCE) moves the debounce TBR; a plug convention other than tip dit appears on a friend's paddle (then paddle-swap in the menu, already planned)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
