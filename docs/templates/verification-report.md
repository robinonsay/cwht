---
# Verification / validation report front matter. Copy this file to docs/vv/reports/<TC-ID>-r<N>.md.
# Governing process: docs/process/04-verification-and-validation.md sections 7.3, 7.4, 9 and 15.
# Machine reading: tools/traceability.py reads this front matter today (process section 7.4,
# rules 7.3.4 and 7.3.8) for the keys test_case, run, requirement_ids, validates, credit,
# result, date, ncr_ids and artifacts; the procedure reviewer checks every other field and
# the body against this template (process section 9).
# Parser: tools/validate_docs.py parse_front_matter (PyYAML safe_load, with the subset parser
# as fallback). Stay inside the subset: scalars, inline [a, b] lists and "- item" block lists
# of scalar strings only; quote hashes and versions. Keep comments on their own lines and
# delete every comment line before filing, so that both parser paths give identical values.
# Every field below is required unless marked optional.
#
# test_case: exactly one case ID from docs/test_cases/**/test_cases.json
test_case: TC-MOD-NNN
# run: run number N for this case; never reused
run: 1
# requirement_ids: subset of the case's requirement_ids that this run addresses
requirement_ids: [REQ-MOD-NNN]
# validates: TC-VAL only, OPS-NNN and MOE-NNN this run validates (subset of the case's
# "Validates:" tokens); [] otherwise
validates: []
# verification_method: Test | Analysis | Inspection | Demonstration (equals the case's)
verification_method: Test
# type: Simulation | HostUnit | Emulation | Inspection | Bench | OnAir (equals the case's)
type: Bench
# credit: true = run for the record per process section 5; false = risk reduction only
credit: true
# result: Pass | Fail | Blocked
result: Pass
date: 2026-MM-DD
# conductor: claude | owner
conductor: claude
# witness: owner for Bench and OnAir; none for automated classes
witness: owner
# article: unit serial CWHT-A-NNN, or host, emulator, "design data <git tag>", or
# pico2-devboard-N for a dev-board case (then credit: false; process section 4)
article: CWHT-A-001
# firmware_version: "vX.Y.Z+<short SHA>" of the release tag release/FW-vX.Y.Z (or
# release/FW-vX.Y.Z-rcN) named in firmware/releases/VDD-vX.Y.Z.md (CM plan section 4.3);
# "n/a" for hardware-only runs. Quoted: values with + or leading zeros must stay strings.
firmware_version: "v0.0.0+0000000"
# source_commit: full SHA of the source commit S the release tag names,
# git rev-parse release/FW-vX.Y.Z^{commit} (CM plan sections 2, 7.3 item 1 and FCA-03); its first
# seven digits equal the SHA part of firmware_version. "n/a" when firmware_version is "n/a". Quoted.
source_commit: "0000000000000000000000000000000000000000"
# firmware_elf_sha256: SHA-256 of cwht-FW-vX.Y.Z.elf, copied from the ELF line of
# firmware/releases/vX.Y.Z/SHA256SUMS (CM plan section 7.3 item 1; FCA-03); "n/a" when
# firmware_version is "n/a". Quoted.
firmware_elf_sha256: "0000000000000000000000000000000000000000000000000000000000000000"
# requirements_baseline: git tag of the requirements set used (baseline/srr, baseline/pdr, ...);
# for a TC-VAL run the same tag also identifies the stakeholder expectations
# (docs/requirements/l0-stakeholder/expectations.json) and ConOps (docs/conops/conops.md)
# version used (SE HB §5.4.1.2.4); "none (pre-SRR)" for a run made before the first baseline tag
requirements_baseline: baseline/pdr
# procedure_commit: git commit at which the test_cases.json that was run was read (quoted: hex
# hashes stay strings)
procedure_commit: "0000000"
# procedure_blob: blob hash of that test_cases.json at procedure_commit, from
# git rev-parse <procedure_commit>:docs/test_cases/<module>/test_cases.json (CM plan section 7.3
# item 1; FCA-04 compares it with the baselined blob). Required for every run. Quoted.
procedure_blob: "0000000000000000000000000000000000000000"
# toolchain_lock: commit of the accredited tool list
toolchain_lock: "tools/toolchain.lock.md@0000000"
# harness_versions: HostUnit and Emulation runs only, the test-harness and emulator versions as
# tools/toolchain.lock.md records them, "<tool> <version>" entries joined by "; " (for example
# "cargo 1.98.0; cargo-nextest 0.9.100"; CM plan section 7.3 item 1); "n/a" for Simulation,
# Inspection, Bench and OnAir runs. Quoted.
harness_versions: "n/a"
# instruments: Bench and OnAir only, one string per instrument in the form
#   "<name>; <model>; <range and points>; <accuracy source>; <calibration performed this session>"
# [] for automated classes
instruments:
  - "NanoVNA; NanoVNA-H4; 144-148 MHz 201 points; accuracy per datasheet page cited in section 3; SOL at cable end verified on dummy load 2026-MM-DD"
# ncr_ids: NCR-NNN opened or cited by this run; [] if none
ncr_ids: []
# artifacts: every file cited in sections 4, 5 and 6, one string per file in the form
#   "<repo-relative path> sha256=<64 hex>"; the tool verifies existence and hash (rule 7.3.8)
artifacts:
  - "docs/vv/reports/TC-MOD-NNN-r1/serial-stage5.txt sha256=0000000000000000000000000000000000000000000000000000000000000000"
# mop_values: optional, one string per MOP in the form "MOP-NNN=<value> <unit>", copied by
# Claude into docs/plan/tpm.json the same day; [] if the requirement carries no mop_ids
mop_values: []
---

# Verification report: TC-MOD-NNN run N

Template implements the report column of SE HB Table 5.3-1 and the report content of SE HB §5.3.1.2.3 and §5.4.1.2.4. Delete the guidance in parentheses when filling in. Keep every heading, writing "None" where a section has nothing to report.

## 1. Objectives and degree to which they were met

(Restate the case title and the requirement shall statements verbatim, with IDs. State for each requirement: met, not met, or partially met, and the process section 5.2 credit row key that applies (the case's `Credit row:` line). For a `TC-VAL` case, name the `OPS-NNN` and `MOE-NNN`, the `Phase:` token, and whether the owner judged the expectation satisfied.)

| Requirement | Shall statement | Acceptance criterion | Measured or observed | Met? |
|---|---|---|---|---|
| REQ-MOD-NNN | | | | |

## 2. Description of the activity and deviations

(What was done, in one paragraph. Then every deviation from the `Active` procedure: skipped, reordered or redlined steps, unplanned pauses, restarts. Each deviation says whether it affects credit. If any discrepancy occurred, say at which step and name the NCR.)

## 3. Configuration under test and differences from the operational configuration

- Article and serial: (as front matter `article`; for hardware add enclosure state, lid on or off, PA jumper state)
- Firmware: (release as front matter `firmware_version`, source commit S as `source_commit`, ELF SHA-256 as `firmware_elf_sha256`; release tag `release/FW-vX.Y.Z`; build command; the ELF hash equals the ELF line of `firmware/releases/vX.Y.Z/SHA256SUMS` and the VDD: yes or no; "n/a" for a hardware-only run)
- Test harness and emulator: (as front matter `harness_versions`, each present in `tools/toolchain.lock.md` at `toolchain_lock`; "n/a" for Simulation, Inspection, Bench and OnAir runs)
- Requirements baseline, procedure commit and procedure blob: (as front matter `requirements_baseline`, `procedure_commit` and `procedure_blob`; for a `TC-VAL` run also state the version of the stakeholder expectations `expectations.json` and of the ConOps `conops.md` used, identified by the same tag or, before SRR, by commit, SE HB §5.4.1.2.4)
- Differences from operational configuration: (dummy load instead of antenna, bench supply instead of battery, USB serial attached, fixtures, mocked HAL, emulator model limits)
- Instruments: (model, range, accuracy with datasheet reference, calibration performed this session and how it was verified; same content as the front matter `instruments` entries, expanded)
- Tools: (name and version for every tool used, each present in `tools/toolchain.lock.md` at the commit in the front matter)
- Environment: (room temperature, supply voltage and current limit, antenna or load, key type connected: straight key or iambic paddles)

## 4. Results of each step

(One row per procedure step. The Observation column contains the reading or event with units. The Artifact column names the file that supports the row, listed in the front matter `artifacts` with its hash.)

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 | | | | | |

## 5. Analysis of results

(Calculations from the raw data to the acceptance criterion: RF probe voltage to power, currents to consumption, log timestamps to element timing, coverage numbers to targets. Show the formula, inputs, result and uncertainty. For Analysis-method cases this section is the analysis itself or links the analysis report. Compare against the pre-build prediction where one exists and explain any difference beyond the stated uncertainty.)

## 6. Data tables, plots and pictures

(Embed or link plots (`.png`, `.svg`), CSV summaries, photographs of the setup and readings, serial captures. Every file appears in the front matter `artifacts` list.)

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

(Also list procedure or conduct discrepancies that did not become product NCRs, with their `Procedure-correction` NCR IDs.)

## 8. Status of enabling equipment after the run

(Instruments, fixtures, dummy load, bench supply, emulator and host rig: any damage, drift, or change that affects later runs. "No change" is a valid entry.)

## 9. Conclusions and recommendations

(Verdict per requirement, matching front matter `result`. Whether the requirement status may move to `Verified` under process section 5.3 (a software requirement becomes `Closed` only later, in the commit that records the signed SAR decision memo, and only when the PCA-05 line of the unit's `as-built.md` names this release; process section 5.3). Recommendations: procedure edits (become CRs or editorial fixes), risk register updates, lessons learned, follow-up runs.)

## 10. As-run procedure

(Copy of the `procedure` array as executed, with redlines marked `[redline: ...]`. If the run was fully automated, link the log that shows each step and its timestamp.)

## 11. Authentication and authorization

- Results authenticated by (conductor): claude, date
- Witnessed by: owner, date (Bench and OnAir; "not required" for automated classes)
- Authorization of acceptability (owner): Approved / Approved with liens (list) / Not approved, date. (Transcribed from the owner's chat approval per charter section 2.)
