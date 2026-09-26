# ADR-021: Purchase of a tinySA Ultra as the spurious-emission verification instrument

| Field | Value |
|---|---|
| ID | ADR-021 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-008, whose control K5 is spurious verification with this instrument; the purchase avoids the class 1 (g) trade). Owner-directed (SI-034). No trade study for the purchase: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision spends money and fixes the verification method of regulatory requirements) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01 and F-02 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | none directly; the V&V plan (PDR baseline) names the instrument |
| Change request | none |

## 1. Context

The owner's bench has a NanoVNA, a 50 ohm dummy load, an adjustable supply and a multimeter, but no oscilloscope or spectrum analyzer (SI-013). 47 CFR 97.307(e) sets an absolute 25 uW ceiling on each spurious emission at the antenna port, which at 5 W means 53 dB of suppression; without an analyzer the regulatory requirement could only close by Analysis or on a borrowed instrument, and 06 section 14.1 class 1 (g) makes substituting Analysis for Test on a regulatory requirement a formal trade. SI-021 recorded the purchase as an open decision; SI-034 closed it: the owner will buy a tinySA Ultra.

- Driving inputs and expectations: SI-034 (third sentence), SI-021, SI-013, SI-014 (Part 97), SI-010 (proof before first on-air)
- Requirements that constrain the decision: the spurious-emission requirement (ADR-022, proposed) and the band-edge requirement (ADR-016, ADR-023)
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-008 (REQ-SYS-017 and REQ-TX-007 cite this ADR and carry it; control K5 names the instrument)
- Research consulted: `docs/research/part97-regulatory-basis.md` F2 (measurement at the antenna connector into 50 ohms; span 9 kHz to 1.5 GHz by analogy with 2.1057; -16.0 dBm limit, -23 dBm target), ACTION-3 (bench procedure); `docs/research/regulatory-corpus-and-operators.md` REQ-candidate RF-10 (report 2f, 3f, 7f individually), ACTION-9 (tinySA minimum RBW for the band-edge and keying-spectrum measurements unverified, Low confidence); `docs/research/pa-device-candidates.md` risk 10 (the tinySA purchase becomes the verification instrument for one-lot vendor harmonic data); `docs/research/keyer-verification-and-key-input-network.md` R-KN6 (the tinySA cannot verify the close-in keying sideband number; that closure is Analysis); `docs/research/tr-switch-candidates.md` action 23 (tinySA harmonics at 5 W into the dummy load with and without the LPF); `docs/plan/cost-estimate.md` (tinySA Ultra line: USD 120 to 160); `docs/plan/tpm.json` TPM-007 (data source names the tinySA if approved; open question OQ-VV-001 in 04)
- Guidance consulted: 47 CFR 97.307(e), 47 CFR 2.1057 (eCFR 2026-09-23); SWE-136 (instrument accreditation by known answer, 04 section 4); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The tinySA RBW is adequate for the band-edge measurement, or the Analysis path stands. Confirmed when the RBW is verified on receipt (ACTION-9).
  2. A calibrated 30 to 40 dB attenuator rated for 5 W is obtained. Confirmed by the cost model line and receipt inspection before TRR.
  3. The known-answer check passes. Confirmed by the instrument's tool-validation record before TRR.

## 2. Decision

The owner buys a tinySA Ultra. It is the Bench instrument for: (1) the 47 CFR 97.307(e) spurious and harmonic measurement at the antenna port, through a calibrated attenuator into the 50 ohm dummy load, span 9 kHz to 1.5 GHz, reporting 2f, 3f and 7f individually against the -16.0 dBm limit and the -23 dBm design target (ADR-022); (2) the band-edge power check at 144.000 and 148.000 MHz at the narrowest available RBW; (3) transmitter output power as a secondary check with the RF detector; (4) receiver birdie and clock-harmonic scans with a near-field probe. The close-in keying spectrum (26 dB bandwidth, -60 dB sideband offsets) remains Analysis on the simulated and captured envelope, with an OnAir listening check by the second station, unless the instrument's RBW is shown adequate. The instrument is accredited before credit (04 section 4): its version and firmware are recorded in `tools/toolchain.lock.md`, the attenuator's loss is measured on the NanoVNA (S21 at 144 to 1500 MHz), and a known-answer check (the tinySA's internal calibration output read within its stated tolerance, and a level check against the NanoVNA's generator output through the measured attenuator) is filed as a tool-validation record. `OQ-VV-001` closes; TPM-007's data source becomes definite.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Buy a tinySA Ultra (USD 120 to 160) | Owner decision (SI-034); repeatable Test on every unit and every regression; span covers the tenth harmonic |
| B | Borrow a laboratory analyzer | Rejected: availability and repeatability for the ATP on each unit and for regression after any PA change |
| C | Analysis only (LTspice harmonics plus NanoVNA S21 of the filter) | Rejected: substituting Analysis for Test on a regulatory requirement is a class 1 (g) trade and leaves RSK-011 open; the NanoVNA measures the filter, not the transmitter |
| D | SDR receiver as a relative spectrum monitor | Rejected: no absolute level; useful only as a listening aid |

No trade study: the owner decided the purchase; the instrument was the research recommendation in three reports.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-017, REQ-TX-007 (spurious emission absolute limit) | allocated; both cite this ADR; hazard HZ-008 | The spurious, band-edge and power requirements (ADR-003, ADR-016, ADR-022, ADR-023) gain the Bench method with this instrument named in `verification_note`; expectations MOE-006 and MOE-010 also name this ADR |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: bench fixture list in `docs/vv/fixtures/` (attenuator, cable adapters), `tools/toolchain.lock.md` instrument entry, `docs/cm/tool-validation/TV-NNN-tinysa.md`
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-TX-NNN (97.307(e) spurious at every power step across the band, Bench), TC-TX-NNN (band-edge power, Bench), TC-SYS-002 class fixture characterization (attenuator S21 on the NanoVNA), the TRR bench procedure of ACTION-3
- Evidence class implications: Bench Test becomes available for the regulatory `REQ-TX-*`; RSK-011's consequence drops; the keying-bandwidth number stays Analysis
- Hazard analysis update required: yes (HZ-008 control K5 names the instrument)
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Cost: USD 120 to 160 plus a calibrated 30 to 40 dB attenuator rated for 5 W or more (to be added to the cost model)
- Gate affected: TRR (instrument accredited before the first spurious run)
- Risks opened, closed or re-scored: RSK-011 (spurious emissions cannot be measured on the owner's bench) moves to Mitigating with this purchase as the step; new risk proposed: "tinySA RBW too coarse for the band-edge measurement" (ACTION-9), control: verify RBW on receipt and keep the Analysis path
- TPMs affected: TPM-007 (data source definite)

## 5. Compliance and tailoring

none (the instrument is accredited under SWE-136 as applied to bench tools in 04 section 4)

## 6. Decision record

> Owner (2026-09-25, SI-021): "Open owner decision: purchase of a tinySA Ultra spectrum analyzer for spurious-emission verification (otherwise spurious compliance rests on analysis or a borrowed instrument)."

> Owner (2026-09-25, SI-034, third sentence): "Owner will purchase a tinySA Ultra spectrum analyzer."

Transcribed from chat into `stakeholder-inputs.md`; SI-034 closes the SI-021 item.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none (the Analysis-for-Test trade of 06 section 14.1 class 1 (g) is avoided by this purchase)
- Review where presented: SRR
- Revisit conditions: the instrument fails its known-answer check or its RBW is inadequate for the band-edge case (then a borrowed instrument for that case only, recorded in the TRR package)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
