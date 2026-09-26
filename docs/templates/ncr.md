---
# Non-conformance report front matter. Copy to docs/vv/ncr/NCR-NNN.md. IDs are never reused
# (charter section 6). Governing process: docs/process/04-verification-and-validation.md section 10.
# Machine reading: tools/traceability.py (load_ncrs) reads these keys today (process section 7.4,
# rule 7.3.8): id, title, status, severity, requirement_ids, test_case_ids, retest_cases,
# regression_cases, hazard_ids, artifacts. It checks NCR_FRONT_MATTER (front matter with an id),
# NCR_ID_FORMAT (NCR-NNN equal to the file name), ID_DUPLICATE, NCR_UNRESOLVED (every
# requirement, test case and hazard id exists) and NCR_ARTIFACT (every artifact exists with its
# SHA-256), and uses status for VERIFIED_WITH_OPEN_NCR (rule 7.3.4). Every other key is checked
# by the reviewer against this template (process sections 10.3 and 10.7).
# Parser: tools/validate_docs.py parse_front_matter (PyYAML safe_load, with the subset parser
# as fallback). Stay inside the subset: scalars, inline [a, b] lists and "- item" block lists
# of scalar strings only. Keep comments on their own lines and delete every comment line before
# filing, so that both parser paths give identical values.
id: NCR-NNN
title: (one-line title)
# status: Open | Analysis | Dispositioned | Retest | Closed (lifecycle in process section 10.7)
status: Open
# severity: S1 (safety or regulatory) | S2 (mission) | S3 (workaround) | S4 (other); process section 10.3
severity: S2
# severity_confirmed_by: independent software-assurance reviewer invocation for firmware NCRs;
# owner for every other NCR (process section 10.3); none until confirmed
severity_confirmed_by: none
date_opened: 2026-MM-DD
# opened_by: claude | owner | <friend name> (Phase E anomaly)
opened_by: claude
# source: test | inspection | receipt | operations | tool | review
source: test
# test_case_ids: cases in which the discrepancy was observed; [] for operations or review
test_case_ids: [TC-MOD-NNN]
# report: report of the run in which it was observed; none if not from a run
report: docs/vv/reports/TC-MOD-NNN-r1.md
# requirement_ids: requirements affected (NPR 7150.2D §3.12.1 Table 1, requirements to
# non-conformances)
requirement_ids: [REQ-MOD-NNN]
# hazard_ids: HZ-NNN if an affected requirement controls a hazard; [] otherwise
hazard_ids: []
# configuration_items: one string per item, for example "firmware v0.3.0+0abc123",
# "hardware/kicad/cwht.kicad_sch@0abc123", "CWHT-A-001"; [] if none yet
configuration_items: []
# classification: product | procedure (procedure, conduct, fixture or tool discrepancy; product conforms)
classification: product
# disposition: none | Rework | Repair | Use-as-is | Scrap | Return-to-vendor | Procedure-correction | Design-change
disposition: none
# cr_ids: CR-NNN required by the disposition (Repair, Use-as-is, Design-change); [] otherwise
cr_ids: []
# risk_ids: RSK-NNN opened or updated; [] otherwise
risk_ids: []
# retest_cases: cases to rerun for credit; [] until Dispositioned
retest_cases: []
# regression_cases: case ids printed by tools/traceability.py --regression <touched design_refs>
# (process section 10.5, rule 7.3.10), plus TC-SW-REG-001 when firmware changes; [] until
# Dispositioned
regression_cases: []
# process_assessment_required: true for S1 and S2 (SWE-204)
process_assessment_required: true
# cots_assessment_required: true when the root cause is in a reused component listed in process
# section 10.4 (rustos, a crate, the toolchain, generators, emulator, LTspice, KiCad), or when
# the NCR records an upstream-reported defect reachable from cwht code (release review, SWE-203)
cots_assessment_required: false
# artifacts: every evidence file under docs/vv/ncr/NCR-NNN/ cited in the body, one string per
# file in the form "<repo-relative path> sha256=<64 hex>"; the tool verifies existence and hash
# (rule 7.3.8)
artifacts:
  - "docs/vv/ncr/NCR-NNN/step6-readings.jpg sha256=0000000000000000000000000000000000000000000000000000000000000000"
date_closed: null
---

# NCR-NNN: (one-line title, equal to the front matter title)

Template implements SE HB §5.3.1.2.2 and §5.3.1.2.3 (stop, discrepancy report, nonconformance analysis and closure) and NPR 7150.2D SWE-201 to SWE-204. Keep every heading; write "None" or "Not applicable" rather than deleting.

## 1. Observation

- **Where and when:** case, run, step number, date, article, firmware version (from the report).
- **Expected:** the acceptance criterion or expected outcome, verbatim.
- **Observed:** the reading, event or condition, with units, instrument and its accuracy. Attach photographs, logs and captures under `docs/vv/ncr/NCR-NNN/` and list each one in the front matter `artifacts` with its SHA-256.
- **Immediate action taken:** activity stopped at step N; setup left intact / powered down (state why); powered testing halted (S1).

## 2. Severity rationale

(Why the severity in the front matter applies, using the process section 10.3 table: name the hazard, regulation clause, requirement priority (`KDR`, `Baseline`, `Goal`) or scenario `OPS-NNN` that decides it. Record the reviewer's confirmation or the owner's change of severity with rationale.)

## 3. Analysis

- **Classification:** product non-conformance, or procedure/conduct/fixture/tool discrepancy, and the evidence for that call (SE HB §5.3.1.2.3).
- **Events leading to the discrepancy:** sequence, including instrument calibration state, configuration differences, prior runs.
- **Root cause:** stated as a single sentence of the form "X because Y", with the design element, code path (`design_refs`), part, or procedure step named. If not yet known, the analysis plan with owner and date.
- **Extent:** other requirements, cases, units or components that share the cause; other passed runs that are invalidated (list their reports).
- **COTS, OSS and reused component assessment (SWE-203):** component, version, upstream issue link, whether the component stays in the build, workaround; "Not applicable" if the cause is project-authored.
- **Code audit performed (SWE-203 note; required for S1 and S2 NCRs in a reused component, found by the project or reported upstream, process section 10.4):** reviewer invocation, audited commit or version, component paths audited (functions, register sequences or generator templates reached from cwht code), defects found, date; "Not applicable" otherwise.

## 4. Disposition

| Field | Entry |
|---|---|
| Disposition (process section 10.4) | |
| Rationale | |
| Change requests required | CR-NNN or none |
| Design or procedure change summary | |
| Impact on requirements, interfaces, safety, verification | |
| Approved by owner on | date, transcribed from chat (required for every disposition, including `Procedure-correction`, process section 10.7) |

## 5. Corrective action and retest

| Action | Owner | Due (gate) | Done |
|---|---|---|---|
| Implement disposition | | | |
| Re-run analysis if an analyzed value changed (process section 5.1 principle 5) | | | |
| Retest: cases listed in front matter | | | |
| Regression: cases listed in front matter (SWE-191) | | | |
| Update cases, plan or toolchain lock (SWE-071) | | | |
| Risk register update | | | |

## 6. Process assessment (S1 and S2, SWE-204)

(Which process step let the defect reach this point: requirement writing, review checklist, analysis assumption, procedure review, tool accreditation, CM. What changes in the process, or a statement that none is needed and why. Changes to the process document go by CR.)

## 7. Closure

(Closure evidence per disposition is the table of process section 10.6: for example a `Use-as-is` NCR closes on the approved CR and, where the CR changes the requirement, a re-evaluated report; a `Scrap` NCR closes on the replacement's receipt inspection and retest, or on the CR that removes the unit or part. Write "Not applicable" in a line below that the disposition does not need.)

- Retest report(s) with `credit: true` and `result: Pass`: (paths)
- Regression evidence: (paths or gate log)
- CRs approved: (IDs)
- Lessons learned entry: `docs/lessons-learned.md` section (or none)
- Owner closure statement: "Closed", date, transcribed from chat; front matter `status: Closed` and `date_closed` set the same day.
