# ADR-018: LTspice batch runs with usage telemetry disabled

| Field | Value |
|---|---|
| ID | ADR-018 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 2 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2: tool configuration, as section 3 states). Decision authority: Robin ratified it because it touches privacy |
| Decision authority | Robin (owner; ratified a tool configuration touching privacy; no baseline changed, no money spent) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | none (tool configuration; recorded in `tools/toolchain.lock.md`) |
| Change request | none |

## 1. Context

LTspice 26.0.2 for macOS is the Windows binary inside a CrossOver bottle. On first run, even in batch mode, it shows an "Anonymously Share LTspice Usage Data" consent dialog that blocks forever under the charter's headless rule (no GUI automation). The binary's string table names a telemetry endpoint (api.telemetry.analogtools.io) and the `[Options]` key `CaptureAnalytics`. Writing `CaptureAnalytics=false` into the bottle's `LTspice.ini` suppresses the dialog and is the same as answering "No" once in the GUI. The owner ratified the opt-out (SI-027).

- Driving inputs and expectations: SI-027, SI-010 (SPICE analysis before power-on), SI-016 (renders inspected), charter section 11 rule 8 (headless only)
- Requirements that constrain the decision: none
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): none
- Research consulted: `docs/research/ltspice-batch-macos.md` F1 (CrossOver bundle under Rosetta), F2 (the documented `LTspice -b` launcher form does not work in 26.0.2), F3 (working invocation via the bottle's `wine` and the Windows path of `LTspice.exe`), F4 (consent dialog blocks `-b`; `CaptureAnalytics=false` fix verified; telemetry endpoint and JSON keys), F5 (`-ini` cannot carry the consent), F6 (one analysis per deck), F8 (Python parsing of `.raw`), F10 (encrypted ADI models load), F11 (ngspice fallback), F12 (version state); `docs/research/verification-tooling-inventory.md` F12, F13
- Guidance consulted: SWE-136 (tool accreditation), 05 section 9.2 (tool validation records `TV-NNN`); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The `CaptureAnalytics` key persists across LTspice updates. The wrapper checks it before every run; a toolchain change triggers re-accreditation.

## 2. Decision

LTspice 26.0.2 is run in batch mode through the bottle's `wine` with the Windows path of `LTspice.exe`, and the bottle's `LTspice.ini` carries `CaptureAnalytics=false` under `[Options]` (the `UUID` line is left as LTspice wrote it). No usage data is sent. The project wrapper (`tools/ltspice-batch.sh` or `tools/run_sim.py`, to be committed) checks for the key before every run and fails with a message if it is absent, so a bottle rebuild cannot silently re-enable telemetry or re-introduce the blocking dialog. The setting, the LTspice version, the CrossOver bottle path and the known-answer check (RC low-pass -3 dB point at 1000.000 Hz) are recorded in `tools/toolchain.lock.md` and in the LTspice tool-validation record. ngspice 47 (Homebrew) is the fallback only for decks without ADI encrypted models.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | `CaptureAnalytics=false` in the bottle's ini; wrapper enforces it | Owner ratification (SI-027); headless; no data leaves the machine; identical to the GUI "No" |
| B | Accept telemetry (answer "Yes" or leave default) | Rejected: sends session data about the owner's machine to a third party for no project benefit; still needs a GUI click once |
| C | Answer "No" once in the GUI | Rejected as procedure: violates the headless rule for agents (11.8); the owner could do it, but the ini key is the durable, checkable record of the same choice |
| D | ngspice only | Rejected: ADI encrypted models and `A`-device macromodels run only in LTspice (F10, F11) |

No trade study: a tool-configuration choice (06 section 14.1 class 2), ratified by the owner because it touches privacy.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | Tooling rule recorded in `tools/toolchain.lock.md` and the CM plan's tool-validation record |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: `tools/ltspice-batch.sh` (from the report's deliverable), `tools/run_sim.py`, `tools/toolchain.lock.md` entry, `docs/cm/tool-validation/TV-NNN-ltspice.md`
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: none; the Simulation evidence class depends on this configuration being in place (04 section 4 tool accreditation)
- Evidence class implications: Simulation (LTspice batch with checker scripts) becomes runnable headlessly; every Simulation report cites the toolchain lock entry
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Cost: none
- Gate affected: PDR (first Simulation cases active)
- Risks opened, closed or re-scored: none; a tool-validation failure or toolchain change is a register trigger (06 section 10)
- TPMs affected: none

## 5. Compliance and tailoring

none (engineering tools are Class E by App. D; accreditation under SWE-136)

## 6. Decision record

> Owner (2026-09-25, SI-027): "LTspice telemetry opt-out (CaptureAnalytics=false in the LTspice settings) ratified by the owner."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR (toolchain proof)
- Revisit conditions: an LTspice update changes the ini key or the batch invocation (toolchain change trigger; re-accreditation); the owner chooses ngspice as primary

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
