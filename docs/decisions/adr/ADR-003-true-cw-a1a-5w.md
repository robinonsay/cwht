# ADR-003: True CW (A1A) emission at 5 W nominal output

| Field | Value |
|---|---|
| ID | ADR-003 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

Most 2 m handhelds send "CW" as a tone on an FM carrier (MCW). The owner wants an on-off keyed unmodulated carrier (emission A1A) for its narrow bandwidth and propagation advantage (SI-004), at 5 W for useful simplex range (SI-003). The power level fixes the binding spurious limit of 47 CFR 97.307(e), the RF exposure evaluation, the PA device class, the battery budget and the thermal path, so nothing downstream can start until it is recorded.

- Driving inputs and expectations: SI-003, SI-004, SI-001, SI-005 (headphones and key, tune and chat), SI-014 (Part 97)
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-001 (RF exposure at 5 W within centimeters of the body), HZ-003 (PA heating at 5 W in an aluminum pocket radio), HZ-004 (stuck transmission)
- Research consulted: `docs/research/part97-regulatory-basis.md` F1 (A1A permitted on all of 144 to 148 MHz; 144.000 to 144.100 MHz is CW-only), F2 (at 5 W the 25 uW cap binds: 53.0 dB), F3 (97.313(a) minimum power necessary; 1.5 kW ceiling irrelevant), F6 to F8 (exposure evaluation mandatory for a 5 W handheld); `docs/research/regulatory-corpus-and-operators.md` F6 (necessary bandwidth of A1A: 208HA1A at 50 WPM, K = 5), F7 (26 dB bandwidth 226 to 292 Hz at 50 WPM with 5 ms edges; hard keying 7 to 8 times wider); `docs/research/pa-device-candidates.md` F18 (2.4 to 3.2 dB output spread over 6.0 to 8.4 V), F19 (11.4 W DC at 5 W; 1.5 h continuous key-down from a 3000 mAh pack), F20 (ALC options); `docs/research/rf-exposure-evaluation.md` F2, F7 (time-averaged power per step; 5 W continuous CW is 17.5 percent of the occupational SAR limit under the high analogy)
- Guidance consulted: 47 CFR 97.305, 97.307(a), (b), (e), 97.313(a), 97.3(a)(8) (eCFR 2026-09-23); 47 CFR 2.202 (necessary bandwidth); SE HB §6.8

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
| REQ-SYS-NNN (emission type A1A only; L1 author allocates) | new, traces to SI-004, this ADR supporting | Verification: Inspection of the design, Bench spectrum shows a single carrier under key-down |
| REQ-SYS-NNN (output power 5.0 W nominal at the antenna port; tolerance proposed plus or minus 0.5 dB with ALC across 6.4 to 8.4 V) | new, traces to SI-003; tolerance value carries a `tbr` object closing at PDR | The PA trade (PDR) fixes the ALC topology |
| REQ-SYS-NNN (spurious emissions per 97.307(e)) | new, regulatory; values per ADR-022 (proposed) | |
| REQ-SYS-NNN (keying envelope and 26 dB bandwidth) | new, regulatory 97.307(a), (b); values per ADR-023 and ADR-024 | |
| REQ-SYS-NNN (power steps and default power) | new, proposed values pending SRR | Supports 97.313(a) and HZ-001 mitigation |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT` (5 W rating of the connector path)
- Design elements created or changed: PA line-up, envelope shaper, harmonic LPF, T/R element (all PDR trade studies, class 1 (a) and (b) of 06 section 14.1)
- New `SW-<SUB>` modules created by this ADR: none (the keyer and TX sequencer modules are named by the architecture ADR at PDR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN for emission type (Inspection, Bench), output power (Bench with the RF detector or a borrowed wattmeter; a wattmeter is not on the bench, `pa-device-candidates.md` implication 1), spurious (ADR-021 instrument)
- Evidence class implications: Bench spurious measurement needs the tinySA Ultra (ADR-021); the keying bandwidth close-in remains Analysis
- Hazard analysis update required: yes (HZ-001, HZ-003, HZ-004 severity depends on 5 W)
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
- Trade study: PA device and topology TS at PDR (records the device that delivers 5 W); no TS for the emission type
- Review where presented: SRR
- Revisit conditions: the RF exposure evaluation (Analysis, PDR) shows 5 W cannot meet the general-population posture the ConOps needs (then power steps and operating rules, not the 5 W ceiling, are the first lever); the PA trade finds no turnkey-stocked 5 W device (ADR-012)
