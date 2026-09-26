# ADR-003: True CW (A1A) emission at 5 W nominal output

| Field | Value |
|---|---|
| ID | ADR-003 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-001, HZ-003, HZ-004, HZ-006, HZ-008 and HZ-012, and the `SW-TXSEQ` and `SW-KEYER` components of `docs/process/07-software-engineering-plan.md` section 14.1). Owner-directed (SI-003, SI-004). Trade study: TS-001 (Draft) sub-decision P for the PA device-and-supply concept, and TS-003 at PDR for the line-up. No trade study for the emission type and the 5 W ceiling: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision fixes the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02, F-03 and F-04 (the section 4.1 tolerance row, erratum E-11) against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

Most 2 m handhelds send "CW" as a tone on an FM carrier (MCW). The owner wants an on-off keyed unmodulated carrier (emission A1A) for its narrow bandwidth and propagation advantage (SI-004), at 5 W for useful simplex range (SI-003). The power level fixes the binding spurious limit of 47 CFR 97.307(e), the RF exposure evaluation, the PA device class, the battery budget and the thermal path, so nothing downstream can start until it is recorded.

- Driving inputs and expectations: SI-003, SI-004, SI-001, SI-005 (headphones and key, tune and chat), SI-014 (Part 97)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-001 (RF exposure at 5 W within centimeters of the body), HZ-003 (PA heating at 5 W in an aluminum pocket radio), HZ-004 (stuck transmission), HZ-006 (bystander exposure at 5 W), HZ-008 (REQ-SYS-012, which cites this ADR, carries it; the 25 uW cap binds at 5 W) and HZ-012 (RF burn at 5 W)
- Research consulted: `docs/research/part97-regulatory-basis.md` F1 (A1A permitted on all of 144 to 148 MHz; 144.000 to 144.100 MHz is CW-only), F2 (at 5 W the 25 uW cap binds: 53.0 dB), F3 (97.313(a) minimum power necessary; 1.5 kW ceiling irrelevant), F6 to F8 (exposure evaluation mandatory for a 5 W handheld); `docs/research/regulatory-corpus-and-operators.md` F6 (necessary bandwidth of A1A: 208HA1A at 50 WPM, K = 5), F7 (26 dB bandwidth 226 to 292 Hz at 50 WPM with 5 ms edges; hard keying 7 to 8 times wider); `docs/research/pa-device-candidates.md` F18 (2.4 to 3.2 dB output spread over 6.0 to 8.4 V), F19 (11.4 W DC at 5 W; 1.5 h continuous key-down from a 3000 mAh pack), F20 (ALC options); `docs/research/rf-exposure-evaluation.md` F2, F7 (time-averaged power per step; 5 W continuous CW is 17.5 percent of the occupational SAR limit under the high analogy)
- Guidance consulted: 47 CFR 97.305, 97.307(a), (b), (e), 97.313(a), 97.3(a)(8) (eCFR 2026-09-23); 47 CFR 2.202 (necessary bandwidth); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. A turnkey-stocked device delivers 5 W from 6.0 to 8.4 V (TS-001 sub-decision P recommends PD54008L-E). Confirmed by TS-003 at PDR and the CDR stock check.
  2. The RF Exposure Evaluation supports 5 W under the occupational tier. Confirmed at PDR (REQ-SYS-121).
  3. The thermal path carries continuous key-down at 5 W. Confirmed by the thermal budget at PDR (REQ-SYS-112).

## 2. Decision

The transmitter produces only emission A1A: an on-off keyed unmodulated carrier with a shaped envelope. No tone, FM or other modulation is applied to the carrier; the sidetone is an audio-only path to the headphones. Nominal output is 5.0 W into 50 ohms at the antenna port. The declared necessary bandwidth for documentation is 208HA1A (A1A at 50 WPM, K = 5). Operator-selectable power steps below 5 W (proposed 0.5, 1, 2, 5 W within plus or minus 1 dB, default 1 W at first boot, deliberate action to select 5 W) are requirement proposals pending the owner's decision at SRR and are not decided by this ADR; the 5 W ceiling is.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | True A1A at 5.0 W nominal | Owner direction (SI-003, SI-004); permitted on the whole band; narrowest emission; 53 dB spurious requirement is achievable with a 7th-order filter |
| B | MCW (tone-modulated FM) | Rejected by SI-004: an F2A or F3E emission is 10 to 16 kHz wide and is not a CW emission for the 144.000 to 144.100 MHz segment |
| C | 1 to 2 W QRP | Rejected: the owner chose 5 W for simplex range; 2 W would ease exposure and battery but the owner set the target |
| D | 10 W or more | Rejected: the 25 uW cap then needs 56 dB or more (F2 arithmetic), the 2S pack and pocket enclosure cannot dissipate it (F19), and exposure distances grow |

No trade study: the owner fixed emission type and power; the alternatives are recorded per SE HB §6.8.1.2.2.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-001 (A1A emission only), REQ-TX-001 (keying envelope as the only carrier modulation) | allocated; both cite this ADR | Verification: Inspection of the design, Bench spectrum shows a single carrier under key-down |
| REQ-SYS-012 (rated output power with level control, TBR) | allocated; cites this ADR and ADR-012; hazards HZ-001, HZ-003, HZ-008 | REQ-SYS-012: within plus or minus 1 dB (TBR, closing at PDR); plus or minus 0.5 dB is the ALC design target (HZ-001 K4, HZ-003 K4, HZ-008 K3). The PA trade (PDR) fixes the ALC topology |
| REQ-SYS-017 and REQ-TX-007 (spurious emission absolute limit; cite ADR-021), REQ-SYS-018 and REQ-TX-008 (spurious emission design margin, TBR; cite ADR-022) | allocated, regulatory 97.307(e) |  |
| REQ-SYS-014 (keying envelope, TBR), REQ-SYS-015 (occupied bandwidth, TBR), REQ-TX-005 (keying envelope reproduction, TBR), REQ-TX-006 (keying sideband level, TBR) | allocated, regulatory 97.307(a), (b); REQ-SYS-014, REQ-TX-005 and REQ-TX-006 cite ADR-023; REQ-SYS-015 and REQ-TX-006 cite ADR-024 | Values per ADR-023 and ADR-024 |
| REQ-SYS-011 (selectable power steps below 5 W, TBR), REQ-SYS-063 (deliberate selection of 5 W), REQ-SYS-064 (default power step, TBR), REQ-TX-004 (reduced power steps, TBR) | allocated; none cites this ADR | Supports 97.313(a) and control K1 of HZ-001 and HZ-006; proposed values pending SRR |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT` (5 W rating of the connector path)
- Design elements created or changed: PA line-up, envelope shaper, harmonic LPF, T/R element (all PDR trade studies, class 1 (a) and (b) of 06 section 14.1)
- New `SW-<SUB>` modules created by this ADR: none (the keyer and TX sequencer modules are named by the architecture ADR at PDR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN for emission type (Inspection, Bench), output power (Bench with the RF detector or a borrowed wattmeter; a wattmeter is not on the bench, `pa-device-candidates.md` implication 1), spurious (ADR-021 instrument)
- Evidence class implications: Bench spurious measurement needs the tinySA Ultra (ADR-021); the keying bandwidth close-in remains Analysis
- Hazard analysis update required: yes (HZ-001, HZ-003, HZ-004, HZ-006, HZ-008 and HZ-012 all scale with the 5 W level)
- Safety-critical software scope changed: no (already includes keying and PA enable)

### 4.4 Cost, schedule, risk

- BOM impact: a 5 W-class PA device and a 7th-order or elliptic LPF; thermal path through the enclosure
- Gate affected: PDR (PA, LPF, ALC trades)
- Risks opened, closed or re-scored: RSK-001 (PA instability or model infidelity), RSK-006 (thermal path), RSK-011 (spurious measurement) remain open and are driven by this decision
- TPMs affected: TPM-004 (PA efficiency at rated output), TPM-007 (spurious margin), TPM-002 (power margin by mode)

## 5. Compliance and tailoring

none (the regulatory requirements replace the spectrum-manager items marked NA in 01 section 3.5)

## 6. Decision record

> Owner (2026-09-25, SI-003): "5 W transmit power, chosen for useful simplex range."

> Owner (2026-09-25, SI-004): "Narrow-bandwidth true CW (not tone-modulated FM) for propagation advantage."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: TS-001 (concept-level receiver and PA trade, Draft, sub-decision P) and TS-003 (PA device and line-up) with TS-006 (ALC and envelope topology) at PDR, `docs/design/concept.md` section 11.2 (TS-003 and TS-006 are the proposed numbers of that section, confirmed when each file is created), which record the device that delivers 5 W; no TS for the emission type (section 1, Decision class row)
- Review where presented: SRR
- Revisit conditions: the RF exposure evaluation (Analysis, PDR) shows 5 W cannot meet the general-population posture the ConOps needs (then power steps and operating rules, not the 5 W ceiling, are the first lever); the PA trade finds no turnkey-stocked 5 W device (ADR-012)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03); trade study references resolved to TS-001 and the proposed TS-003 and TS-006 (F-03, erratum E-9); the section 4.1 tolerance row now states the REQ-SYS-012 value with the ALC design target (F-04, erratum E-11). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
