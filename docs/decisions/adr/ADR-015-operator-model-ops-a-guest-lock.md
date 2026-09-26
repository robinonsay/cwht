# ADR-015: Operator model OPS-A (each licensee operates the loaned unit as their own station) with a receive-only guest lock

| Field | Value |
|---|---|
| ID | ADR-015 |
| Status | Proposed, pending owner decision at SRR |
| Date proposed | 2026-09-25 |
| Date decided | pending (SRR) |
| Decision authority | Robin (owner; the decision fixes ConOps scenarios and a firmware function in the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: ConOps, L1) |
| Change request | none (pre-baseline) |

## 1. Context

With licensed friends operating loaned units (ADR-014), three lawful configurations exist: OPS-A, each friend operates the unit as their own station under 97.5(c) and the 97.103(b) presumption, with their own call sign and full responsibility; OPS-B, the friend is a designated control operator of the owner's station, identifying with the owner's call sign, with a dated designation note in the owner's records and both parties equally responsible; OPS-C, an unlicensed guest as a supervised third party. The ConOps must pick a default because OPS-B is what applies by default when nobody has thought about it, and it carries a records duty. Independently, a unit handed around at a gathering can be keyed by an unlicensed person without a licensee at that unit; a licensee-settable receive-only lock removes that pathway for a few lines of firmware.

- Driving inputs and expectations: SI-019, SI-030, SI-014, SI-025 (open design: the model must work for any licensee)
- Requirements that constrain the decision: none yet
- Hazards in play: none for personal safety; regulatory exposure (unlicensed transmission) is a mission and compliance hazard, handled as a requirement, not an HZ
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F2 (control operator rules), F4 (unlicensed person: may listen, may key only as a supervised third party, may never operate alone), F5 (OPS-A recommended default; OPS-B records duty; OPS-C bounded), REQ-candidates OPS-02, OPS-03, FW-03 (guest lock), FW-04 (per-unit call sign, auto-ID at most 20 WPM), DOC-02 (operator rules card), RISK REG-4, REG-7, DECISION-6, DECISION-7; `docs/research/part97-regulatory-basis.md` F10 (97.119(b)(1): automatic identification at most 20 WPM)
- Guidance consulted: 47 CFR 97.5(c), 97.103(a) and (b), 97.105(b), 97.115(b)(1), 97.119(a), (b)(1) and (e) (eCFR 2026-09-23); SE HB §6.8

## 2. Decision (proposed)

The ConOps default is OPS-A: each cwht unit is the amateur station of the licensee holding it; that licensee is station licensee and control operator, identifies with their own call sign, and is responsible for the unit's compliance including RF exposure. OPS-B remains a documented alternative: when a unit is operated as the owner's station with a designated control operator, a dated designation note is kept in the owner's station records and identification follows 97.119(a) and (e). Unlicensed guests follow OPS-C (ADR-014). The firmware provides a licensee-settable receive-only guest lock that inhibits the transmitter (key, keyer and any memory) until released by a deliberate action, so a unit can be handed to a guest with no risk of unlicensed transmission; the lock state is shown on the display. Each unit stores its operator's call sign, shows it on the display, and uses it for any automatic identification memory at not more than 20 WPM; an empty call sign disables automatic identification rather than sending a default. The handbook carries a one-page operator rules card.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (proposed) | OPS-A default; OPS-B documented alternative; guest lock; per-unit call sign | No records burden; each licensee already qualifies for the controlled-environment exposure treatment; the lock closes the main unlicensed-keying pathway |
| B | OPS-B default (owner's station, designated control operators) | Not recommended: owner's call sign on every unit, owner and friend equally responsible, records duty; 97.119(e) indicator when the friend's class exceeds General |
| C | No guest lock; rely on operator discipline | Not recommended: a unit set down at a gathering is the foreseeable REG-4 case; the lock costs a menu item and a stored flag |
| D | Receive-only units for friends | Rejected: contradicts SI-019 (friends operate) |

No trade study: the rule text and the owner's population (ADR-014) leave A and B as live options; the ADR presents both for the owner.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN or ConOps text (OPS-A default, OPS-B records duty; candidate OPS-02; L1 author allocates) | new, traces to SI-019, SI-030, this ADR supporting | Inspection |
| REQ-SW-NNN (receive-only guest lock; candidate FW-03) | new, traces to SI-019; candidate for SWE-134 scoping alongside the transmit inhibit | HostUnit (key events in guest mode produce no PA enable), Bench |
| REQ-SW-NNN (per-unit stored call sign, display, auto-ID at most 20 WPM, empty call sign disables auto-ID; candidate FW-04) | new | HostUnit, Inspection |
| Handbook item (operator rules card; candidate DOC-02) | new | Inspection |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: ConOps scenarios (licensed friend as own station; supervised guest; unit handed to a guest under lock); UI menu items (guest lock, call sign entry); non-volatile storage of the call sign and lock flag (rustos NV work package, ADR-019)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SW-NNN (guest lock inhibits every transmit path, HostUnit; Bench on the unit), TC-SW-NNN (auto-ID speed cap and empty-call-sign behaviour, HostUnit), TC-VAL-NNN (a licensed friend operates a loaned unit with their own call sign following the handbook, Demonstration)
- Evidence class implications: none new
- Hazard analysis update required: no
- Safety-critical software scope changed: pending: if the owner scopes the guest lock with the transmit inhibit under SWE-134, the lock joins the safety-critical set and gets MC/DC coverage

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
- Trade study: none
- Review where presented: SRR (decision requested)
- Revisit conditions: an FCC or ARRL interpretation on third-party participation (ACTION-7 of the corpus report); the owner prefers OPS-B; a unit is transferred rather than lent (then that unit is simply the new owner's station under OPS-A and the design is unchanged)
