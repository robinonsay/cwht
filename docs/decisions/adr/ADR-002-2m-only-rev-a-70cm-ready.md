# ADR-002: 2 m band only in rev A with a 70 cm-ready architecture

| Field | Value |
|---|---|
| ID | ADR-002 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 2 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2: the band scope is a stakeholder expectation, NGO-008 and CON-022, and the meaning of "70 cm-ready" is a recorded convention; no class 1 item). Decision authority stays Robin because the decision scopes the baseline |
| Decision authority | Robin (owner; the decision fixes the functional baseline scope) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

The owner wants a pocket CW handheld for the 2 m band first, with 70 cm deferred to a later revision but "keep the path open" (SI-002). A dual-band rev A would double the RF hardware (PA, low-pass filter, LNA, T/R switching), the regulatory verification (47 CFR 97.307(e) at two fundamentals) and the RF exposure evaluation, on a schedule that releases procurement within two days. Without a recorded scope the L1 requirements could not fix frequency coverage, and "70 cm-ready" would mean whatever each author assumed.

- Driving inputs and expectations: SI-002, SI-001 (pocket form factor), SI-024 (full 2 m band), SI-006 (band control listed as "future")
- Requirements that constrain the decision: none yet; the requirements schema already carries the tag `70cm-ready` (`docs/requirements/schema.json`, `tags` description)
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): none new. HZ-001, HZ-006 and HZ-008 are evaluated for 144 to 148 MHz only (HZ-001 scales with band; the third harmonic of 2 m falls in the 70 cm band, HZ-008)
- Research consulted: `docs/research/part97-regulatory-basis.md` F1 (A1A permitted on the entire 2 m band), F2 (third harmonic 432 to 444 MHz falls in the 70 cm band); `docs/research/regulatory-corpus-and-operators.md` F9 (US allocations at each 2 m harmonic; 70 cm shared with Federal radiolocation); `docs/research/2m-cw-transceiver-reference-designs.md` F16, F20 (synthesizer ranges: Si5351A to 200 MHz, LMX2571 to 1344 MHz), Table 1 (single-band reference designs); `docs/research/pa-device-candidates.md` F17 (LPF goal 35 dB at 432 to 444 MHz, the 70 cm band, for rev A)
- Guidance consulted: 47 CFR 97.301(a) and 97.305 (eCFR 2026-09-23); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The five-point meaning of "70 cm-ready" in section 2 is what the owner intends. Confirmed by the owner at SRR (README open item 2).
  2. The 70 cm enhancing criterion adds no rev A cost beyond the synthesizer choice. Checked in the synthesizer and reference trade study at PDR against TPM-009.

## 2. Decision

Rev A transmits and receives on 2 m only (144.000 to 148.000 MHz, ADR-016). "70 cm-ready" means, for rev A: (1) the control architecture is band-agnostic: frequency plan, band edges, guard, power steps and tuning limits are data, not code paths, and the UI reserves a band control (SI-006) that rev A does not expose; (2) requirements that rev B would inherit unchanged are tagged `70cm-ready`, and band-specific requirements are tagged `revA`; (3) the synthesizer trade (ADR-013) carries "LO coverage for a 430 to 450 MHz plan" as an enhancing criterion, never a mandatory one; (4) the antenna port is a stainless SMA jack usable on both bands; (5) the band-specific blocks (PA and driver, harmonic low-pass filter, LNA and front-end filter, T/R element) are documented as replaceable modules in the architecture with their interfaces to the common blocks (control, power, audio, keyer) in ICDs, so rev B is a new RF board section and firmware data, not a new radio. Rev A carries no 70 cm hardware, no dual-band antenna requirement and no 70 cm verification.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 2 m only in rev A; architecture and requirement tagging keep the 70 cm path open | Owner direction (SI-002); fits the two-day procurement release; halves RF verification |
| B | Dual-band 144/430 MHz rev A | Rejected: two PA line-ups or a broadband PA with two filters, two exposure evaluations, two 97.307(e) campaigns; pocket volume and battery (SI-001, SI-034) do not absorb it on this schedule |
| C | 2 m only with no provision for 70 cm | Rejected by the owner's "keep the path open" |
| D | 70 cm first | Not requested; 2 m CW has the weak-signal segment and the owner's operating interest |

No trade study: the owner's direction fixed the band; the meaning of "70 cm-ready" is a recorded convention (06 section 14.1 class 2 content, decided by the owner because it scopes the baseline).

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-008 (transmit frequency range with band-edge guard, TBR), REQ-SYS-021 (receive frequency range), REQ-TX-002 (transmit carrier frequency range, TBR) | allocated; they cite ADR-016, not this ADR | See ADR-016 for the band-edge consequences |
| REQ-SYS-145 (band-dependent functions partitioned), REQ-SYS-146 (reserved band control) | allocated; REQ-SYS-145 cites this ADR; REQ-SYS-146 implements point (1) of section 2 without citing it |  |
| tagging rule: `revA` for band-specific, `70cm-ready` for band-independent requirements | not a requirement: a tagging convention | Reviewer checks the tag at requirements validation |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT` (external stub before SRR; SMA jack common to both bands)
- Design elements created or changed: architecture (PDR) partitions band-specific modules (PA, LPF, LNA, T/R) from common modules; frequency plan held as data in `cwht-core`
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none (internal ICDs between band-specific and common blocks are created by the architecture ADR at PDR, 02 section 3.5)

### 4.3 Verification and safety

- Verification cases to add or change: none for 70 cm in rev A; every `regulatory` case is written for 144 to 148 MHz
- Evidence class implications: none
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact: none in rev A; the synthesizer choice may cost more if 70 cm coverage is weighted (ADR-013)
- Gate affected: PDR (architecture partition), rev B SRR (re-entry)
- Risks opened, closed or re-scored: new risk proposed to the register author: "70 cm-ready provisions grow rev A scope (board area TPM-009, synthesizer cost) without a rev B commitment"; mitigated by the enhancing-criterion rule above
- TPMs affected: TPM-009 (PCB area utilization), watched for provision creep

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-002): "2 m band for the first iteration; 70 cm deferred to a later revision but keep the path open."

Transcribed from chat into `stakeholder-inputs.md`. The five-point meaning of "70 cm-ready" in section 2 is Claude's interpretation and is presented for confirmation at SRR; the band decision itself is the owner's.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none (the receiver architecture and synthesizer trade studies at PDR carry the 70 cm enhancing criterion)
- Review where presented: SRR
- Revisit conditions: rev B formulation; a synthesizer or antenna choice that cannot reach 70 cm at similar cost (then the enhancing criterion is dropped by a superseding ADR, not silently)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
