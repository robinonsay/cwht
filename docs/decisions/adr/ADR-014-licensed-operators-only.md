# ADR-014: Licensed operators only; occupational exposure tier for operators, general population for everyone else

| Field | Value |
|---|---|
| ID | ADR-014 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-001, HZ-006). Owner-directed (SI-030). No trade study for the operator population, where the rule text leaves one lawful configuration: this ADR alone records it under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), which customizes 06 section 14.1, item (i) (ruling R-2 of `reconciliation-srr.md` section 7, adopted by the owner as SRR decision 106 on 2026-09-26) |
| Decision authority | Robin (owner; the decision fixes the ConOps population and the exposure evaluation regime) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: ConOps and L1) |
| Change request | none (pre-baseline) |

## 1. Context

The owner wants to hand finished radios to friends so several people can operate together (SI-019). Part 97 requires a control operator with a license for every transmission, and RF exposure rules evaluate the licensee and household at occupational limits while everyone else is general population. A 5 W handheld used within 20 cm of the body has no exemption and its general-population SAR margin at 5 W is thin or negative under the only available analogy. The owner ruled that all operators hold at least a Technician license, that occupational limits apply to operators, and that bystander limits still apply to non-operators (SI-030).

- Driving inputs and expectations: SI-030, SI-019, SI-014 (owner holds General), SI-003 (5 W)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-001 (RF exposure) and HZ-006 (general-population tier for everyone who is not the operating licensee); REQ-SYS-121 and REQ-SYS-171, which cite this ADR, carry them. REQ-SYS-122 (operations handbook safety content), which also cites this ADR, carries the handbook controls of HZ-001 to HZ-007, HZ-009 and HZ-011 to HZ-013; this ADR changes none of those other causes or controls
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F2 (control operator framework: 97.7, 97.3, 97.5, 97.103, 97.105, 97.109, 97.119), F3 (third-party framework: 97.115), F4 (what an unlicensed friend may and may not do), F5 (OPS-A, OPS-B, OPS-C configurations); `docs/research/rf-exposure-evaluation.md` F1 (which limits apply to whom), F2 (time-averaged power per step), F3 (MPE distances: 0.58 m at 5 W continuous CW, 0.91 m for a carrier), F5, F6 (SAR situation within 20 cm), F7 (consequences of SI-030 and SI-034: occupational tier presupposes information and training; 5 W continuous CW is 17.5 percent of the occupational SAR limit; a non-licensee holding the radio at 5 W is at or above the general-population limit), F8; `docs/research/part97-regulatory-basis.md` F6 to F8, RISK REG-1, REG-2
- Guidance consulted: 47 CFR 97.7, 97.5, 97.103, 97.105, 97.109, 97.115, 97.119, 97.13(c)(1), 1.1310(e)(2), 2.1093(d)(3) and (d)(4) (eCFR 2026-09-23); OET 65 Supplement B (extracts in the corpus); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Every operator is licensed and has the handbook exposure information. Confirmed by the handbook walkthrough with a licensed friend at SAR.
  2. The OET 65 Supplement B method with the SAR analogy is an adequate evaluation. Confirmed by the RF Exposure Evaluation at PDR, updated with measured antenna gain at CDR and measured power at TRR.
- Erratum (2026-09-26, SRR decision 18; RID-SRR-010; ConOps Appendix D item D15): section 2 evaluates operators "as licensees under 97.13(c)(1)". That basis holds under OPS-A, where each operator is the station licensee of the unit they hold. Under OPS-B (a friend as designated control operator of the owner's station, ADR-015) the friend is neither the station licensee nor a member of the owner's household, so the household clause of 47 CFR 97.13(c)(1) does not cover them; their occupational tier rests on the OET 65 Supplement B controlled-environment statement that "occupational/controlled exposure limits apply to amateur licensees and members of their immediate household" (OET Bulletin 65 Supplement B, Edition 97-01, 1997; corpus: `docs/references/md/regulatory/oet65-supplement-b-extracts.md` lines 126 to 127, section "Controlled environment: amateur licensees and household members"), the guidance that 47 CFR 97.13(c)(1) names (corpus: 47cfr-97.13.md, eCFR issue 2026-09-23), together with the 47 CFR 1.1310(e)(2) awareness condition. By SRR decision 18 (owner ruling 2026-09-26), a unit lent under OPS-B is operated at the 0.5 W and 1 W steps only until a dated owner record confirms the controlled-environment basis (`docs/conops/conops.md` section 3.7 and Appendix C row "OPS-B exposure tier"). Section 2 is unchanged.

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
| REQ-SYS-121 (RF exposure evaluation) | allocated; cites this ADR; hazards HZ-001, HZ-006 | Candidate RFX-01; verification: Inspection of the Analysis at TRR |
| REQ-SYS-011 (power steps, TBR), REQ-SYS-063, REQ-SYS-064 (TBR), REQ-SYS-122 (operations handbook safety content), REQ-SYS-171 (key-down time display, TBR), REQ-SYS-172 (delivered antenna gain, TBR) | allocated; REQ-SYS-122 and REQ-SYS-171 cite this ADR | Candidate RFX-02. Whether the key-down accumulator is safety-critical is DECISION-5 of `part97-regulatory-basis.md`, pending SRR; HZ-006 control K5 records it as a convenience function |
| Operators licensed; unlicensed persons receive-only or supervised third parties (candidates OPS-02, OPS-03, DOC-02) | ConOps text and REQ-SYS-122, REQ-SYS-124 (enclosure legend); guest lock REQ-SYS-065, REQ-SYS-066 (cite ADR-015) | Inspection of ConOps and handbook |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: operations handbook exposure section; ConOps scenarios OPS-NNN (licensed friend, supervised guest, bystanders)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (exposure evaluation reviewed, Inspection), TC-SW-NNN (key-down time windows, HostUnit), TC-VAL-NNN (hand-over walkthrough with a licensed friend using the handbook alone, Demonstration)
- Evidence class implications: the exposure evaluation is Analysis (no SAR measurement path exists); measured antenna gain at CDR and measured power at TRR update it
- Hazard analysis update required: yes (HZ-001 and HZ-006 exposed population and controls)
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

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
- 2026-09-26 (after the SRR rulings): Decision class row updated under SRR decision 106 (owner ruling 2026-09-26), which adopts ruling R-2 of `reconciliation-srr.md` section 7 as SEMP customization 11 of 06 section 14.1 (`docs/plan/semp.md` section 9.0): the class 1 owner-directed choice of this ADR is recorded by this ADR alone under item (i); the implementing design choices stay class 1 and go through the trade study the row names. The correction entry above now rests on SRR decision 105 (owner ruling 2026-09-26, R-1 option (A) approved) and on the 05 Table 4-1 row 13 sentence, which is in place. The decision of section 2 is unchanged. Author: Claude (ADR author invocation, SRR post-ruling work R16).
- 2026-09-26 (SRR decision 18): erratum line added at the end of section 1, citing the OET 65 Supplement B controlled-environment statement as the OPS-B exposure tier basis and the decision 18 limit of 0.5 W and 1 W for OPS-B units (RID-SRR-010; ConOps Appendix D item D15). Made under the pre-baseline correction allowance of `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (an errata line, before the `baseline/srr` tag, section 2 untouched), with the owner's approval in the SRR decision memo (decision 105, R-1 option (A); decision 18). The citation was verified against the corpus extract `docs/references/md/regulatory/oet65-supplement-b-extracts.md`. The decision of section 2 is unchanged. Author: Claude (ADR author invocation, SRR post-ruling work R16).
