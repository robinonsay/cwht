---
id: ICD-<A>-<B>
title: <interface title, noun phrase, under 80 characters>
side_a: <A>                 # module token: RX | TX | PWR | CTL | ME | SW (02 section 3.5, charter order)
side_b: <B>                 # module token after <A> in charter order, or external token: KEY | PHONES | ANT | USB | CELL | HOST
owner: <author of side A: Claude or author agent invocation>
status: Draft               # Draft | Baselined | Superseded by ICD-<X>-<Y>
baseline: null              # baseline/pdr once approved; later changes by CR-NNN
revision: A
date: YYYY-MM-DD
requirements_a: []          # REQ ids of side A tagged interface that cite this ICD (02 rule T-22)
requirements_b: []          # REQ ids of side B (empty for an external interface)
requirements_other: []      # REQ ids of any other module citing this ICD in design_refs (not a side)
hazard_ids: []
tbr_open: 0
---

# ICD-<A>-<B>: <title>

<!--
Interface Control Document template. Process: docs/process/02-requirements-and-traceability.md
section 3.5 (identity, order, owner, creation, pairing, baseline). Outline: SE HB Appendix L
(Interface Requirements Document Outline), sections 1.1 to 3.2.8, plus cwht sections 4 to 7.
Copy to docs/icd/ICD-<A>-<B>.md. Fill every section; a section that does not apply reads
"Not applicable: <reason>" and is never deleted, so a reviewer can see it was considered.
No TBD anywhere; an estimated value is written with "(TBR)" and a row in section 6.
The two Security expectations rows (sections 3.2.5 and 3.2.6; 02 section 3.5 Content
row) are never deleted: ICD-CTL-KEY fills the 3.2.5 row, ICD-CTL-USB and ICD-SW-HOST fill
the 3.2.6 row, and every other ICD marks each row Not applicable with its reason.
Front matter is YAML in the parser subset of 04 section 7.4 (scalars and inline lists only;
comments on their own lines once the file is filled).
Every physical interface carries at least one rendered figure (charter section 11 rule 3).
Delete the comments when the file is filled.
-->

## 1. Scope (App. L 1.1 to 1.3)

### 1.1 Purpose and scope

This ICD defines and controls the interface between `<A>` (<subsystem name as in docs/design/architecture.md>) and `<B>` (<subsystem name, or the external item: key or paddle plug, headphones, antenna, USB host or charger, 18650 cells, host computer>). It covers: <list the interface types of section 3.2 that apply, e.g. connector, electrical levels, timing, mechanical envelope>.

### 1.2 Precedence

Order of precedence in a conflict: `docs/process/00-charter.md`; the requirement files of both sides (`docs/requirements/<a>/requirements.json`, `docs/requirements/<b>/requirements.json`); this ICD; `docs/design/architecture.md`; part datasheets in `docs/research/`. A conflict found is a finding against the newer document and is resolved by CR after PDR.

### 1.3 Responsibility and change authority

| Item | Value |
|---|---|
| Owner (writes and maintains) | Author of side `<A>` (02 section 3.5) |
| Concurring side | Author of side `<B>` (or, for an external interface, the SI or constraint that defines the external item: SI-NNN, CON-NNN) |
| Independent reviewer | Reviewer agent invocation and date, checklist `docs/templates/peer-review-checklist-design.md` |
| Approval | Robin, PDR decision memo (allocated baseline, charter section 3; 05 Table 4-1 row 10) |
| Change authority after PDR | `CR-NNN`, Class I for any definition-table change, Class II otherwise (02 section 10.2); Robin as CCB |

## 2. Documents (App. L 2.1, 2.2)

### 2.1 Applicable documents (binding)

| Document | What it imposes here |
|---|---|
| `docs/requirements/<a>/requirements.json` REQ-<A>-NNN ... | side A interface requirements |
| `docs/requirements/<b>/requirements.json` REQ-<B>-NNN ... | side B interface requirements |
| `docs/safety/hazards.json` HZ-NNN | hazards controlled at this interface |
| 47 CFR 97.NNN (when the interface is the antenna port or an RF path) | emission limits |
| CON-NNN | constraint that fixes part of this interface (e.g. SI-022 single micro-USB) |

### 2.2 Reference documents

| Document | Use |
|---|---|
| `docs/decisions/adr/ADR-NNN-*.md` | decision that created or shaped this interface |
| `docs/research/<file>.md` | datasheets, standards (e.g. 3.5 mm jack dimensions, USB 2.0 electrical) |
| `docs/conops/conops.md` OPS-NNN | scenarios that exercise the interface |

## 3. Interface (App. L 3.0)

### 3.1 General (App. L 3.1)

#### 3.1.1 Interface description

<One paragraph and one figure: what crosses the plane, in which direction, under which conditions. Figure: `docs/icd/figures/ICD-<A>-<B>-plane.png` (or .svg) rendered from KiCad, OpenSCAD or a drawn block diagram; inspected per charter section 11 rule 3.>

![Interface plane](figures/ICD-<A>-<B>-plane.png)

#### 3.1.2 Interface responsibilities

| Item at the plane | Provided by | Accepted by | Defined in |
|---|---|---|---|
| <connector, receptacle side> | `<A>` | `<B>` | 3.2.2 |
| <signal, supply, mechanical feature> | | | 3.2.x |

For an external interface, the `<B>` column names the external item and the SI, constraint or standard that fixes its side (e.g. "two-conductor 3.5 mm plug, SI-018").

#### 3.1.3 Coordinate systems

<Mechanical interfaces only: origin and axes used for the envelope and mounting dimensions (enclosure origin per `hardware/enclosure/`). Otherwise: Not applicable: no mechanical content.>

#### 3.1.4 Engineering units, tolerances and conversion

SI units with the amateur-radio conventions of the requirement files (W, dBm, dBc, Hz, ms, µs, WPM, mV, °C). Every value in section 3.2 carries a tolerance or bound. No unit conversion tables are used.

### 3.2 Interface definition (App. L 3.2)

<Each subsection is a definition table. The value that both sides depend on is stated once here; each side's requirement (section 4) states what that side delivers or accepts, with the value, so it is verifiable alone. A change here and in the paired requirements travels in one CR.>

#### 3.2.1 Mass properties

<Mass of the item crossing the plane (cells, antenna) with tolerance, or: Not applicable.>

#### 3.2.2 Structural and mechanical

| Feature | Value | Tolerance | Side responsible | Source |
|---|---|---|---|---|
| Connector type and part | | | | |
| Mounting, envelope, keep-out | | | | |
| Insertion force, retention, cycles | | | | |

#### 3.2.3 Fluid

Not applicable on cwht (no fluid interfaces).

#### 3.2.4 Electrical (power)

| Line | Nominal | Range | Current (max) | Sequencing and protection | Side responsible |
|---|---|---|---|---|---|
| | | | | | |

#### 3.2.5 Electronic (signal)

| Pin or line | Name | Direction (A to B, B to A) | Level (V) | Timing (edge, debounce, rate) | Termination, ESD | Side responsible |
|---|---|---|---|---|---|---|
| | | | | | | |

<Security expectations for a signal line that could carry an injected command (02 section 3.5 Content row; 07 section 16.2). ICD-CTL-KEY fills this row here, because its key line is a signal interface and is the command-injection surface of the 07 section 16.2 row "Keying and control inputs". Every other ICD keeps the row and writes "Not applicable: " followed by the reason, for example "no signal line at this plane is read as data or commands", or writes "Stated in section 3.2.6" when the interface has a data path.>

| Item | Definition | Side responsible |
|---|---|---|
| Security expectations | **Accepts:** <what each side accepts at the plane, with its bound; for ICD-CTL-KEY, tip and ring contact closures read as a two-bit signal that feeds only the keyer state machine (CS-30), debounced and rate-limited (CS-29)>. **Rejects:** <each input the side refuses and the response it takes, with the time limit; for ICD-CTL-KEY, no key-line gesture changes configuration or state outside the keyer (CS-30); a stuck closure ends at the key-down timeout (SWE-134 g, j)>. **Logs:** <the event-log entry each rejection or anomaly writes (07 section 16.5; SWE-210 as tailored), or "none" with the reason>. **Basis:** <07 section 16.2 row; `RSK-NNN` tagged `cyber`; the `REQ-` ids of section 4 that implement each statement> | <A>, and <B> for any statement about what the external side delivers |

#### 3.2.6 Software and data

| Item | Definition | Side responsible |
|---|---|---|
| Register or GPIO map | | |
| Protocol, framing, rate | | |
| Message or command set | | |
| Timing (latency, period) | | |
| Error detection and response | | |
| Initialization and status | | |
| Security expectations | **Accepts:** <the images, commands or data each side accepts and the check each passes, for example only a release image from `firmware/releases/` whose CRC-32 trailer verifies at boot before any safety-critical output (CS-32), or only the read-only diagnostic commands plus `reboot` (CS-33)>. **Rejects:** <each input the side refuses, with the response and the state it leaves the unit in, for example an image whose trailer fails is not run and the unit stays in its safe state>. **Logs:** <the event-log entry each rejection writes (07 section 16.5; SWE-210 as tailored), or "none" with the reason>. **Basis:** <07 section 16.2 row (asset and surface); `RSK-NNN` tagged `cyber`; the `REQ-` ids of section 4 that implement each statement> | <A>, and <B> for any statement about what the other side delivers |

<Security expectations row (02 section 3.5 Content row; NPR 7123.1D App. G Table G-4 success criterion 4, system security expectations of external interfaces; charter section 12; 07 section 16.2). Required and filled in ICD-CTL-USB (firmware loading over the USB bootrom loader) and ICD-SW-HOST (bootloader and serial command set). ICD-CTL-KEY fills the row of section 3.2.5 and writes "Stated in section 3.2.5" here. Every other ICD keeps the row and writes "Not applicable: " followed by the reason, for example "the interface carries no data or command path". A row with an estimated value carries "(TBR)" and a section 6 row; no TBD.>

#### 3.2.7 Environments

##### 3.2.7.1 Electromagnetic effects (EMC, EMI, grounding, bonding, cable and wire)

<Grounding scheme at the plane, shielding, filter requirements, RF exposure at an external port; or: Not applicable.>

##### 3.2.7.2 Acoustic

<Headphone interface only: level range and limiter; or: Not applicable.>

##### 3.2.7.3 Structural loads

<Mated loads the connector or mount withstands (handheld drop, antenna lever load); or: Not applicable.>

##### 3.2.7.4 Vibroacoustics

Not applicable on cwht unless the hazard analysis names a vibration case.

##### 3.2.7.5 Human operability

<Operator-facing aspects of the plane: plug insertion by feel, polarity cues, control reach (HSI, SEMP section 7.3.1); or: Not applicable.>

#### 3.2.8 Other interface definitions

<Thermal path across the plane, RF exposure, anything not covered above; or: Not applicable.>

## 4. Requirements on each side (cwht addition; 02 section 3.5 pairing rule)

| Side | Requirement | Statement (verbatim `description`) | Section 3.2 rows it depends on | Verification method |
|---|---|---|---|---|
| A `<A>` | REQ-<A>-NNN | | | |
| B `<B>` | REQ-<B>-NNN (external interface: the external item's defining SI/CON/standard instead) | | | |
| other | REQ-<MOD>-NNN | | | |

The lists here equal the front matter `requirements_a`, `requirements_b`, `requirements_other` and are checked by T-22 against `design_refs`.

## 5. Verification (cwht addition; SE HB §6.3.1.2.3)

| Case | Verifies | Method and evidence class | Level |
|---|---|---|---|
| TC-<MOD>-NNN | REQ-<A>-NNN | | |

## 6. TBR items

| Value (section, row) | Current estimate | Owner | Plan | close_by |
|---|---|---|---|---|
| | | | | CDR at the latest (SEMP section 5.12) |

## 7. Change history

| Revision | Date | CR or review | Change |
|---|---|---|---|
| A | YYYY-MM-DD | none (pre-baseline draft) or RID-<REVIEW>-NNN | Created |
