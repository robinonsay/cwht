# ADR-015: Operator model OPS-A (each licensee operates the loaned unit as their own station) with a receive-only guest lock

| Field | Value |
|---|---|
| ID | ADR-015 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-26 (SRR decision 17, owner ruling) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): touches HZ-006, whose controls K3 (receive-only guest lock) and K8 (operator model OPS-A) this ADR proposes, and the receive-only guest lock of `SW-TXSEQ` in `docs/process/07-software-engineering-plan.md` section 14.1). No TS: a proposal from research, recorded by this ADR alone under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), which customizes 06 section 14.1, item (ii) (ruling R-2 of `reconciliation-srr.md` section 7, adopted by the owner as SRR decision 106 on 2026-09-26), applied by the owner's disposition of SRR decision 17 (section 6) |
| Decision authority | Robin (owner; the decision fixes ConOps scenarios and a firmware function in the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 to 3 (2026-09-25 and 2026-09-26); iteration 3 verdict NEEDS CHANGES only on the owner rulings of F-01 (SRR decision 106), both ruled on 2026-09-26, with liens F-11 and F-13 against this file; this post-ruling revision applies the rulings and the two liens; verification of the revision by the reviewer is pending (package item R16) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: ConOps, L1) |
| Change request | none (pre-baseline) |

## 1. Context

With licensed friends operating loaned units (ADR-014), three lawful configurations exist: OPS-A, each friend operates the unit as their own station under 97.5(c) and the 97.103(b) presumption, with their own call sign and full responsibility; OPS-B, the friend is a designated control operator of the owner's station, identifying with the owner's call sign, with a dated designation note in the owner's records and both parties equally responsible; OPS-C, an unlicensed guest as a supervised third party. The ConOps must pick a default because OPS-B is what applies by default when nobody has thought about it, and it carries a records duty. Independently, a unit handed around at a gathering can be keyed by an unlicensed person without a licensee at that unit; a licensee-settable receive-only lock removes that pathway for a few lines of firmware.

- Driving inputs and expectations: SI-019, SI-030, SI-014, SI-025 (open design: the model must work for any licensee)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.3-pha): HZ-006 (RF exposure of bystanders, household members and non-licensee holders: control K3 is the receive-only guest lock and K8 the operator model OPS-A; REQ-SYS-065, REQ-SYS-066 and REQ-TX-003 cite this ADR and carry HZ-006); HZ-008 (REQ-TX-003, RF isolation with PA enable deasserted, cites this ADR and carries HZ-008). Unlicensed transmission itself is a regulatory and mission harm handled as a requirement
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F2 (control operator rules), F4 (unlicensed person: may listen, may key only as a supervised third party, may never operate alone), F5 (OPS-A recommended default; OPS-B records duty; OPS-C bounded), REQ-candidates OPS-02, OPS-03, FW-03 (guest lock), FW-04 (per-unit call sign, auto-ID at most 20 WPM), DOC-02 (operator rules card), RISK REG-4, REG-7, DECISION-6, DECISION-7; `docs/research/part97-regulatory-basis.md` F10 (97.119(b)(1): automatic identification at most 20 WPM)
- Guidance consulted: 47 CFR 97.5(c), 97.103(a) and (b), 97.105(b), 97.115(b)(1), 97.119(a), (b)(1) and (e) (eCFR 2026-09-23); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Every friend who operates a unit holds a current license of Technician class or higher (ADR-014) and accepts station responsibility under 47 CFR 97.5(c) and 97.103(b). Confirmed by the handbook hand-over walkthrough with a licensed friend (Demonstration) at SAR.
  2. The guest lock can be released only by a deliberate action that a guest cannot perform by accident (SWE-134 item d, two independent operator actions). Confirmed when the L2 `SW-TXSEQ` requirements are reviewed at PDR.
  3. No FCC or ARRL interpretation narrows third-party participation (ACTION-7 of `regulatory-corpus-and-operators.md`). Re-checked at each review; a change is a revisit condition (section 7).

## 2. Decision

The ConOps default is OPS-A: each cwht unit is the amateur station of the licensee holding it; that licensee is station licensee and control operator, identifies with their own call sign, and is responsible for the unit's compliance including RF exposure. OPS-B remains a documented alternative: when a unit is operated as the owner's station with a designated control operator, a dated designation note is kept in the owner's station records and identification follows 97.119(a) and (e). Unlicensed guests follow OPS-C (ADR-014). The firmware provides a licensee-settable receive-only guest lock that inhibits the transmitter (key, keyer and any memory) until released by a deliberate action, so a unit can be handed to a guest with no risk of unlicensed transmission; the lock state is shown on the display. Each unit stores its operator's call sign, shows it on the display, and uses it for any automatic identification memory at not more than 20 WPM; an empty call sign disables automatic identification rather than sending a default. The handbook carries a one-page operator rules card.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | OPS-A default; OPS-B documented alternative; guest lock; per-unit call sign | No records burden; each licensee already qualifies for the controlled-environment exposure treatment; the lock closes the main unlicensed-keying pathway |
| B | OPS-B default (owner's station, designated control operators) | Not recommended: owner's call sign on every unit, owner and friend equally responsible, records duty; 97.119(e) indicator when the friend's class exceeds General |
| C | No guest lock; rely on operator discipline | Not recommended: a unit set down at a gathering is the foreseeable REG-4 case; the lock costs a menu item and a stored flag |
| D | Receive-only units for friends | Rejected: contradicts SI-019 (friends operate) |

No trade study: the rule text and the owner's population (ADR-014) leave A and B as live options; the ADR presents both for the owner. The choice is class 1 (header); the ADR without a TS stands under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), which customizes 06 section 14.1, item (ii) (SRR decision 106), and the owner chose A at SRR (SRR decision 17, section 6).

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| ConOps text (OPS-A default, OPS-B records duty; candidate OPS-02) | not created as a requirement: ConOps scenario text and the handbook content of REQ-SYS-122 (HZ-006 control K8) | Inspection of ConOps and handbook |
| REQ-SYS-065 (guest lock transmit inhibit) and REQ-SYS-066 (guest lock set and release); candidate FW-03 | allocated at L1, cite this ADR; hazard HZ-006 | HostUnit (key events in guest mode produce no PA enable), Bench |
| REQ-TX-003 (RF isolation with PA enable deasserted) | allocated at L2, cites this ADR and ADR-023; hazards HZ-006, HZ-008 | |
| REQ-SYS-006 (operator call sign shown after every power-on); candidate FW-04, stored call sign and display | allocated at L1, cites this ADR | HostUnit, Inspection |
| Automatic identification at most 20 WPM, and an empty call sign disables it (rest of candidate FW-04) | not created: the rev A L1 set has no automatic identification memory; REQ-SYS-068 (identification reminder) covers identification | If PDR adds a message memory, the 47 CFR 97.119(b)(1) limit is written with it |
| Handbook operator rules card (candidate DOC-02) | covered by REQ-SYS-122 (operations handbook safety content) | Inspection |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: ConOps scenarios (licensed friend as own station; supervised guest; unit handed to a guest under lock); UI menu items (guest lock, call sign entry); non-volatile storage of the call sign and lock flag (rustos NV work package, ADR-019)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SW-NNN (guest lock inhibits every transmit path, HostUnit; Bench on the unit), TC-SW-NNN (auto-ID speed cap and empty-call-sign behaviour, HostUnit), TC-VAL-NNN (a licensed friend operates a loaned unit with their own call sign following the handbook, Demonstration)
- Evidence class implications: none new
- Hazard analysis update required: yes (HZ-006 controls K3 and K8 implement this proposal; cross item to the hazard analysis author: name ADR-015 in the HZ-006 sources when the owner decides)
- Safety-critical software scope changed: no; the receive-only guest lock is already part of `SW-TXSEQ` in 07 section 14.1, which closes the question this line carried in the previous revision

### 4.4 Cost, schedule, risk

- Cost: none in parts
- Gate affected: SRR (ConOps), PDR (SW requirements)
- Risks opened, closed or re-scored: proposed risk "unlicensed operation by a guest" (REG-4) is mitigated by OPS-A, the lock and the rules card; proposed risk "interpretation of third-party keying" (REG-7) is carried
- TPMs affected: none

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-26, SRR session, `docs/reviews/SRR/minutes.md` section "Rulings"): "I concur with your recommendations for the key decisions."

Recorded ruling (minutes, same section): key decision K5 of package section 13.1.1, which contains SRR decision 17, is ruled as recommended; the ruling text is the "Recommendation" cell of decision 17 in `docs/reviews/SRR/decisions-for-owner.md` Part 1: "OPS-A default, OPS-B only by a dated record; accept ADR-015."

> Owner (2026-09-26, SRR disposition, `docs/reviews/SRR/minutes.md` section "Disposition"): "I approve of this and the SRR."

Class 1 without a trade study: recorded by this ADR alone under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), which customizes 06 section 14.1, item (ii) (SRR decision 106, owner ruling 2026-09-26), applied by the disposition above, so no TS section 10 is cited. The SRR decision memo carries the same ruling.

The ruling adopts section 2 as written: OPS-A is the ConOps default and OPS-B is permitted only with a dated designation record in the owner's station records. The proposed memo wording of the previous revision was: "Operator model OPS-A is the ConOps default; OPS-B is permitted with records; the receive-only guest lock and per-unit call sign are baselined as L1 requirements." The guest-lock release is option a of SRR decision 19 (two-step release), ruled in the same key decision K5.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none (see the Decision class row)
- Review where presented: SRR, decided 2026-09-26 (SRR decision 17, key decision K5); INSP-011 findings F-01 to F-03 applied in the 2026-09-25 revision, liens F-11 and F-13 in the 2026-09-26 revision
- Revisit conditions: an FCC or ARRL interpretation on third-party participation (ACTION-7 of the corpus report); the owner prefers OPS-B; a unit is transferred rather than lent (then that unit is simply the new owner's station under OPS-A and the design is unchanged)

## 8. Change log

- 2026-09-26 (after the SRR rulings): Status set to Accepted and section 6 filled with the owner's disposition under SRR decision 17 (owner ruling 2026-09-26, key decision K5, accept ADR-015); the Decision class row and the section 3 closing paragraph cite SEMP customization 11 item (ii) of 06 section 14.1 adopted as SRR decision 106 (owner ruling 2026-09-26), which also clears INSP-011 lien F-11 for this file; the reviewer row names INSP-011 iteration 3 and the hazard line cites `hazards.json` 0.4.3-pha, whose HZ-006 controls K3 and K8 and the hazard ids of REQ-SYS-065, REQ-SYS-066 and REQ-TX-003 were re-checked on 2026-09-26 and agree (INSP-011 lien F-13). The decision text of section 2 is unchanged apart from its heading. Author: Claude (ADR author invocation, SRR post-ruling work R16).
- 2026-09-27 (PDR errata, WP-PDR-14; SRR liens L-6 and, where named, L-4 and L-7): Independent reviewer row names the one ruling (SRR decision 106) where the text said "both", and names the post-SRR-ruling delta as the verification of the R16 revision (F-16); hazard line stamp 0.4.3-pha changed to 0.5.0-pha, the version at HEAD, after re-checking the line against it (F-13; for ADR-015, 022, 023 and 026 also SRR lien L-7); section 4.3 placeholders replaced by TC-SYS-006, TC-SYS-047 and TC-TX-003, the SW L2 and validation cases stated as allocated, the auto-ID case stated as not created (F-14). RID-SRR-005 (SRR lien L-4; SRR decisions 17 and 19 option a): section 2 is not edited. Its clause "so a unit can be handed to a guest with no risk of unlicensed transmission" overstates the lock and is read as: so a unit handed to a guest cannot transmit by accident; releasing the lock is a deliberate licensee action under the operator rules card (the two-step release of SRR decision 19 option a, whose claims are limited to "no transmission by accident"). The lock removes the accidental keying pathway; it does not replace the supervising licensee of an unlicensed guest (OPS-C, ADR-014; ConOps OPS-019). This reading governs wherever section 2 is cited. Route: the SRR decision memo carries these findings as liens to be fixed in the product before the PDR readiness declaration (RFA-SRR-006: "Fix each finding in its product"); they are applied by the ADR correction route the owner approved as SRR decision 105 (corrections outside section 2, each logged in this section), as the README paragraph "PDR errata" records. The decision of section 2 is unchanged. Author: Claude (ADR author invocation, WP-PDR-14).
- 2026-09-27 (correction of the WP-PDR-14 entry above; INSP-053 finding-1, `docs/reviews/PDR/checklists/adrs-001-to-027.md`): the entry above records edits in place of 3 lines outside section 8 made after the `baseline/srr` tag, which 05 Table 4-1 row 13, the Record class of 05 section 4.2 and README rule 2 do not allow. Its "Route" sentence is withdrawn: the SRR lien direction (RFA-SRR-006) does not amend row 13, and the decision 105 route was the exception before the tag only. Those 3 lines are restored to their `baseline/srr` text, and each change the entry above lists is carried here as a reading of the restored line, which governs wherever that line is cited (finding ids as in the entry above, with SRR lien L-7 for the hazard stamp): (1) header row "Independent reviewer", read as "INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 to 3 (2026-09-25 and 2026-09-26); iteration 3 verdict NEEDS CHANGES only on the owner ruling of F-01 (SRR decision 106, ruled on 2026-09-26), with liens F-11 and F-13 against this file; the post-ruling revision (package item R16) applied the ruling and the two liens and was verified at the INSP-011 post-SRR-ruling delta (2026-09-26, APPROVED with liens; delta 2 the same). The liens against this file are fixed by the 2026-09-27 errata of section 8, verified at the next INSP-011 delta iteration. That record, not this row, carries every later result"; (2) section 1, line "Hazards in play", for the stamp "0.4.3-pha" read "0.5.0-pha": the line was re-checked against `hazards.json` 0.5.0-pha on 2026-09-27 and its hazard list and every control and cause id it cites hold at that version unchanged; (3) section 4.3, line "Verification cases to add or change", read as "Verification cases to add or change: guest lock TC-SYS-047 (Bench, REQ-SYS-065 and REQ-SYS-066); call sign after power-on TC-SYS-006 (Bench, REQ-SYS-006); RF isolation with PA enable deasserted TC-TX-003 (Bench); the SW L2 guest-lock case (every transmit path, HostUnit) is allocated with the SW L2 requirements at PDR; no auto-ID case exists because rev A has no identification memory (section 4.1); the licensed-friend demonstration is allocated with the validation cases of the V&V plan (no id yet)". Every other statement of the entry above stands as written. The decision of section 2 is unchanged, and `git diff baseline/srr` of this file shows added lines only. Verification: the next INSP-053 iteration. Author: Claude (ADR author invocation, WP-PDR-14).
