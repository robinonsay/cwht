# ADR-017: Open-source publication of the whole design under the MIT license

| Field | Value |
|---|---|
| ID | ADR-017 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the license of every configuration item) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | all baselines (license applies to every CI) |
| Change request | none (pre-baseline) |

## 1. Context

The owner publishes the project at https://github.com/robinonsay/cwht under the MIT license so anyone may use it (SI-025). Publication interacts with the regulatory posture (an amateur-built transceiver needs no equipment authorization, but marketing or a kit would change that), with part selection (a published baseline should name parts others can buy), and with the NPR 7150.2D rows on reuse cataloging and Government rights, which presuppose NASA institutions.

- Driving inputs and expectations: SI-025, SI-028 (buyable parts), SI-019 (units lent, not sold), SI-007 (rustos is the owner's separate repository)
- Requirements that constrain the decision: none
- Hazards in play: none
- Research consulted: `docs/research/part97-regulatory-basis.md` F9 (no FCC equipment authorization for an amateur-built transceiver; 97.315 reaches only external amplifiers; 15.23 covers the digital section; the unit must not be marketed), constraints; `docs/research/pcbway-export-and-vendor-questions.md` F21 (15.23(a) text: not marketed, not constructed from a kit, five or fewer for personal use; 2.803(a) marketing definition), F23 (legal caveat, Low confidence); `docs/research/pa-device-candidates.md` implication 6 (an EOL device must not become the published baseline unless the primary channel fails)
- Guidance consulted: 47 CFR 15.23, 47 CFR 97.315 (eCFR 2026-09-23); NPR 7150.2D SWE-147, SWE-148 (reuse and rights rows, NA per charter section 12), SWE-027 c (license review, tailored to owner review); SE HB §6.8

## 2. Decision

Every configuration item authored for cwht (requirements, process documents, KiCad schematics and layouts, OpenSCAD sources, BOMs, firmware crates `cwht-core`, `cwht-app`, `cwht-hal-mock`, emulation scenarios, tools, test cases and reports) is published in the public repository under the MIT license, recorded in `LICENSE` at the repository root and in the README. Third-party material keeps its own terms: rustos is consumed under the rustos repository license; vendor datasheets are cited by URL and not redistributed; regulatory text (eCFR) and the NASA handbooks and NPRs are public documents reproduced as reference corpus with their source URLs. The repository states that cwht is a personal amateur-built design: units are not marketed, sold or offered as kits by the owner; anyone building from the design is responsible for their own Part 97 and Part 15 posture. Published part selections favour catalog-stocked devices (ADR-012) so the design stays buildable by others, and any EOL part in the baseline is named with its substitution path.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | MIT for everything authored here; third-party terms preserved | Owner direction (SI-025); permissive, compatible with the owner's rustos and with the permissive dev-tool licenses (07 section 17.1) |
| B | Hardware under CERN-OHL or TAPR, firmware under MIT | Rejected: the owner named MIT for the project; split licensing adds compliance text for no benefit to a personal design |
| C | Private repository until SAR | Rejected by SI-025 (open from the start) |
| D | Copyleft (GPL) | Rejected: the owner chose MIT |

No trade study: license choice is the owner's.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | Licensing is a repository and CM property, not a system requirement; the published-design buildability appears through ADR-012's sourcing constraint |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: `LICENSE` (MIT), README license and "not for sale, personal amateur-built" statements; source-file headers optional (MIT does not require per-file notices)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: none; the CM plan's configuration audit at SAR checks that `LICENSE` and third-party attributions are present
- Evidence class implications: none
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Cost: none
- Gate affected: none
- Risks opened, closed or re-scored: new risk proposed: "publishing an EOL PA baseline makes the open design unbuildable by others" (control: ADR-012 substitution path); the 15.23 "personal use" reading for lent units is Low confidence and is carried in ADR-025
- TPMs affected: none

## 5. Compliance and tailoring

RMM rows SWE-147, SWE-148 and the reuse and Government-rights rows (SWE-214 to SWE-217) are NA per charter section 12 ("Open personal project; license recorded in the repo"); SWE-027 item c is tailored to owner license review (07 section 17.1). This ADR is the license record those rows cite.

## 6. Decision record

> Owner (2026-09-25, SI-025): "The project is open source under the MIT license at https://github.com/robinonsay/cwht; anyone may use it."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR
- Revisit conditions: the owner wants to sell or kit units (then 15.23 no longer applies and a separate regulatory assessment precedes any change); a third-party component with an incompatible license is proposed (CR with a trade study per 07 section 17.1)
