# ADR-015: Operator model OPS-A (each licensee operates the loaned unit as their own station) with a receive-only guest lock

| Field | Value |
|---|---|
| ID | ADR-015 |
| Status | Proposed, pending owner decision at SRR |
| Date proposed | 2026-09-25 |
| Date decided | pending (SRR) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): touches HZ-006, whose controls K3 (receive-only guest lock) and K8 (operator model OPS-A) this ADR proposes, and the receive-only guest lock of `SW-TXSEQ` in `docs/process/07-software-engineering-plan.md` section 14.1). No TS: this is a proposal from research, admitted without a TS only if the owner's SRR disposition applies the customization of `reconciliation-srr.md` section 6 item (ii); otherwise a TS-NNN is opened before the decision |
| Decision authority | Robin (owner; the decision fixes ConOps scenarios and a firmware function in the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 iteration 1 (2026-09-25): NEEDS CHANGES, findings F-01, F-02 and F-03 apply; this revision (2026-09-25, ADR author invocation applying INSP-011) carries the fixes; re-review pending in INSP-011 iteration 2 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: ConOps, L1) |
| Change request | none (pre-baseline) |

## 1. Context

With licensed friends operating loaned units (ADR-014), three lawful configurations exist: OPS-A, each friend operates the unit as their own station under 97.5(c) and the 97.103(b) presumption, with their own call sign and full responsibility; OPS-B, the friend is a designated control operator of the owner's station, identifying with the owner's call sign, with a dated designation note in the owner's records and both parties equally responsible; OPS-C, an unlicensed guest as a supervised third party. The ConOps must pick a default because OPS-B is what applies by default when nobody has thought about it, and it carries a records duty. Independently, a unit handed around at a gathering can be keyed by an unlicensed person without a licensee at that unit; a licensee-settable receive-only lock removes that pathway for a few lines of firmware.

- Driving inputs and expectations: SI-019, SI-030, SI-014, SI-025 (open design: the model must work for any licensee)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.3.0-pha): HZ-006 (RF exposure of bystanders, household members and non-licensee holders: control K3 is the receive-only guest lock and K8 the operator model OPS-A; REQ-SYS-065, REQ-SYS-066 and REQ-TX-003 cite this ADR and carry HZ-006); HZ-008 (REQ-TX-003, RF isolation with PA enable deasserted, cites this ADR and carries HZ-008). Unlicensed transmission itself is a regulatory and mission harm handled as a requirement
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F2 (control operator rules), F4 (unlicensed person: may listen, may key only as a supervised third party, may never operate alone), F5 (OPS-A recommended default; OPS-B records duty; OPS-C bounded), REQ-candidates OPS-02, OPS-03, FW-03 (guest lock), FW-04 (per-unit call sign, auto-ID at most 20 WPM), DOC-02 (operator rules card), RISK REG-4, REG-7, DECISION-6, DECISION-7; `docs/research/part97-regulatory-basis.md` F10 (97.119(b)(1): automatic identification at most 20 WPM)
- Guidance consulted: 47 CFR 97.5(c), 97.103(a) and (b), 97.105(b), 97.115(b)(1), 97.119(a), (b)(1) and (e) (eCFR 2026-09-23); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Every friend who operates a unit holds a current license of Technician class or higher (ADR-014) and accepts station responsibility under 47 CFR 97.5(c) and 97.103(b). Confirmed by the handbook hand-over walkthrough with a licensed friend (Demonstration) at SAR.
  2. The guest lock can be released only by a deliberate action that a guest cannot perform by accident (SWE-134 item d, two independent operator actions). Confirmed when the L2 `SW-TXSEQ` requirements are reviewed at PDR.
  3. No FCC or ARRL interpretation narrows third-party participation (ACTION-7 of `regulatory-corpus-and-operators.md`). Re-checked at each review; a change is a revisit condition (section 7).

## 2. Decision (proposed)

The ConOps default is OPS-A: each cwht unit is the amateur station of the licensee holding it; that licensee is station licensee and control operator, identifies with their own call sign, and is responsible for the unit's compliance including RF exposure. OPS-B remains a documented alternative: when a unit is operated as the owner's station with a designated control operator, a dated designation note is kept in the owner's station records and identification follows 97.119(a) and (e). Unlicensed guests follow OPS-C (ADR-014). The firmware provides a licensee-settable receive-only guest lock that inhibits the transmitter (key, keyer and any memory) until released by a deliberate action, so a unit can be handed to a guest with no risk of unlicensed transmission; the lock state is shown on the display. Each unit stores its operator's call sign, shows it on the display, and uses it for any automatic identification memory at not more than 20 WPM; an empty call sign disables automatic identification rather than sending a default. The handbook carries a one-page operator rules card.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (proposed) | OPS-A default; OPS-B documented alternative; guest lock; per-unit call sign | No records burden; each licensee already qualifies for the controlled-environment exposure treatment; the lock closes the main unlicensed-keying pathway |
| B | OPS-B default (owner's station, designated control operators) | Not recommended: owner's call sign on every unit, owner and friend equally responsible, records duty; 97.119(e) indicator when the friend's class exceeds General |
| C | No guest lock; rely on operator discipline | Not recommended: a unit set down at a gathering is the foreseeable REG-4 case; the lock costs a menu item and a stored flag |
| D | Receive-only units for friends | Rejected: contradicts SI-019 (friends operate) |

No trade study: the rule text and the owner's population (ADR-014) leave A and B as live options; the ADR presents both for the owner. The choice is class 1 (header), so the ADR without a TS stands only under the owner's ruling on `reconciliation-srr.md` section 6.

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

Pending. Proposed wording for the SRR decision memo: "Operator model OPS-A is the ConOps default; OPS-B is permitted with records; the receive-only guest lock and per-unit call sign are baselined as L1 requirements." The owner's disposition will be transcribed here verbatim with its date; until then this ADR is Proposed.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none (see the Decision class row)
- Review where presented: SRR (decision requested); INSP-011 findings F-01 to F-03 applied in this revision
- Revisit conditions: an FCC or ARRL interpretation on third-party participation (ACTION-7 of the corpus report); the owner prefers OPS-B; a unit is transferred rather than lent (then that unit is simply the new owner's station under OPS-A and the design is unchanged)
