# ADR-014: Licensed operators only; occupational exposure tier for operators, general population for everyone else

| Field | Value |
|---|---|
| ID | ADR-014 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the ConOps population and the exposure evaluation regime) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: ConOps and L1) |
| Change request | none (pre-baseline) |

## 1. Context

The owner wants to hand finished radios to friends so several people can operate together (SI-019). Part 97 requires a control operator with a license for every transmission, and RF exposure rules evaluate the licensee and household at occupational limits while everyone else is general population. A 5 W handheld used within 20 cm of the body has no exemption and its general-population SAR margin at 5 W is thin or negative under the only available analogy. The owner ruled that all operators hold at least a Technician license, that occupational limits apply to operators, and that bystander limits still apply to non-operators (SI-030).

- Driving inputs and expectations: SI-030, SI-019, SI-014 (owner holds General), SI-003 (5 W)
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-001 (RF exposure)
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F2 (control operator framework: 97.7, 97.3, 97.5, 97.103, 97.105, 97.109, 97.119), F3 (third-party framework: 97.115), F4 (what an unlicensed friend may and may not do), F5 (OPS-A, OPS-B, OPS-C configurations); `docs/research/rf-exposure-evaluation.md` F1 (which limits apply to whom), F2 (time-averaged power per step), F3 (MPE distances: 0.58 m at 5 W continuous CW, 0.91 m for a carrier), F5, F6 (SAR situation within 20 cm), F7 (consequences of SI-030 and SI-034: occupational tier presupposes information and training; 5 W continuous CW is 17.5 percent of the occupational SAR limit; a non-licensee holding the radio at 5 W is at or above the general-population limit), F8; `docs/research/part97-regulatory-basis.md` F6 to F8, RISK REG-1, REG-2
- Guidance consulted: 47 CFR 97.7, 97.5, 97.103, 97.105, 97.109, 97.115, 97.119, 97.13(c)(1), 1.1310(e)(2), 2.1093(d)(3) and (d)(4) (eCFR 2026-09-23); OET 65 Supplement B (extracts in the corpus); SE HB §6.8

## 2. Decision

Every operator of a cwht unit (the owner and each friend) holds a current US amateur license of Technician class or higher and is the control operator of the transmissions they make. Operators are evaluated at the occupational and controlled RF exposure limits of 47 CFR 1.1310 as licensees under 97.13(c)(1), with time averaging permitted, and the operations handbook carries the exposure information that 1.1310(e)(2) presupposes. Everyone who is not the operating licensee (bystanders, household members of a friend, unlicensed guests) is general population: the handbook states the separation distances (proposed: at least 0.6 m from the antenna while keying and at least 1.0 m during a tune carrier, covering every power step with a dipole-equivalent whip) and the evaluation per OET 65 Supplement B is presented as an Analysis product at PDR. An unlicensed person never operates a unit alone; keying by an unlicensed person is only third-party participation under a licensee present at that unit and continuously supervising (97.115(b)(1)), at a reduced power step, and is written as a bounded ConOps scenario, not a design case. The operator model for loaned units (each licensee's own station versus the owner's station with designated control operators) is decided separately in ADR-015.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Licensed operators only; occupational tier for operators; general population for others | Owner direction (SI-030); the only configuration in which a 5 W handheld held at the head has a defensible exposure argument (F7) |
| B | General-population evaluation for everyone | Rejected: a 5 W handheld within 20 cm has no exemption and no measurement path; only the 0.5 W and 1 W steps stay under the limit for a continuous carrier (F7) |
| C | Owner-only operation | Rejected by SI-019 |
| D | Unlicensed friends as routine third-party operators | Rejected: requires a licensee at every unit at all times and puts general-population SAR at the limit; kept only as the bounded OPS-C scenario |

No trade study: the rule text leaves one lawful configuration for the owner's use case.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (RF exposure evaluation deliverable before first on-air; candidate RFX-01; L1 author allocates) | new, traces to SI-030, SI-014; hazard HZ-001 | Verification: Inspection of the Analysis at TRR |
| REQ-SYS-NNN (exposure controls in the product: power steps, key-down time display over 6 and 30 minute windows, handbook distances; candidate RFX-02) | new, hazard HZ-001 | Whether the key-down accumulator is safety-critical is DECISION-5 of `part97-regulatory-basis.md`, pending SRR |
| REQ-SYS-NNN or ConOps text (operators licensed; unlicensed persons receive-only or supervised third parties; candidates OPS-02, OPS-03, DOC-02) | new, traces to SI-030, SI-019 | Inspection of ConOps and handbook |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: operations handbook exposure section; ConOps scenarios OPS-NNN (licensed friend, supervised guest, bystanders)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (exposure evaluation reviewed, Inspection), TC-SW-NNN (key-down time windows, HostUnit), TC-VAL-NNN (hand-over walkthrough with a licensed friend using the handbook alone, Demonstration)
- Evidence class implications: the exposure evaluation is Analysis (no SAR measurement path exists); measured antenna gain at CDR and measured power at TRR update it
- Hazard analysis update required: yes (HZ-001 exposed population and controls)
- Safety-critical software scope changed: pending DECISION-5 (key-down accumulator)

### 4.4 Cost, schedule, risk

- Cost: none in parts
- Gate affected: PDR (exposure Analysis), TRR (updated with measured power), SAR (handbook)
- Risks opened, closed or re-scored: new risks proposed to the register author: "unlicensed operation by a guest" (REG-4), "exposure method gap for VHF portables" (REG-1), "general-population SAR margin at 5 W" (REG-2)
- TPMs affected: none

## 5. Compliance and tailoring

Spectrum-manager items of NPR 7123.1D App. G are NA (01 section 3.5); the Part 97 requirements above preserve the intent. No RMM row.

## 6. Decision record

> Owner (2026-09-25, SI-030): "All operators (owner and friends) hold at least a Technician license; controlled/occupational RF exposure limits apply to operators; bystander (general population) limits still apply to non-operators nearby."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR
- Revisit conditions: an FCC or ARRL interpretation narrows third-party keying (then OPS-C tightens to receive-only; design unchanged); the owner wants unlicensed guests to key routinely (then the power-step and supervision design becomes a requirement set)
