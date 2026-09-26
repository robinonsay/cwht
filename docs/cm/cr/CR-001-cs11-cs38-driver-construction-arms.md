---
id: CR-001
title: Admit driver-construction failure arms in cwht-app; place the panic handler
status: Submitted
class: II
originator: Claude
date_opened: 2026-09-26
phase: Pre-A/A
configuration_at_origination: 28e49e6 (working tree; FW-B0 workspace first committed with the SRR integration commits of 2026-09-26)
baseline_affected: baseline/srr
affected_cis: [2, 25, 28]
affected_paths: [docs/process/07-software-engineering-plan.md, firmware/cwht-app/src/main.rs]
affected_ids: [CS-11, CS-12, CS-38, TC-SW-TOOL-001]
related: [INSP-016]
target_release: none
branch: cr/CR-001-cs11-cs38-driver-construction-arms
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-001: Admit driver-construction failure arms in cwht-app; place the panic handler

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. The plan text it changes (`docs/process/07-software-engineering-plan.md`, Table 4-1 row 2) is not yet baselined; the CR is raised because the FW-B0 review (INSP-016 finding-2, `docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`) requires an owner-dispositioned record for deviation D8 of `docs/vv/reports/TC-SW-TOOL-001-r1.md` section 2, not a deviation the author declares for itself (charter §11 rule 5).

## 1. Description of the change

1. 07 CS-11, before: "The single permitted `Option` unwrap-equivalent is the board `take()` in `cwht-app::main`, written as a `match` whose `None` arm calls `safe_state_halt()`." After: "The permitted unwrap-equivalents in `cwht-app::main` are the board `take()`, whose `None` arm calls `safe_state_halt()`, and the construction of each rustos driver whose constructor returns `Result`, whose `Err` arm calls `safe_state_halt()`; each is written as `let ... else { safe_state_halt() }` or a two-arm `match`, and no other arm or statement sits in the failure branch."
2. 07 CS-38, before: "functions are straight-line (cyclomatic complexity 1) except the board `take()` match of CS-11." After: "functions are straight-line except the board `take()` and driver-construction failure arms of CS-11; each such arm adds one to the cyclomatic complexity of `main` and `tools/complexity_gate.py` counts them against a per-file allowance equal to the number of those arms."
3. 07 CS-12, before: "The `#[panic_handler]` (in `pico2`, invoked by `cwht-app`'s configuration)". After: "The `#[panic_handler]` (in `cwht-app`, because rustos `pico2` leaves the handler to the application; it calls only the `pico2` safe-state register writes)". The rest of CS-12 is unchanged.
4. `firmware/cwht-app/src/main.rs`: the comment above the `output_from_handle` arm cites CR-001 instead of the pending CR.

## 2. Reason

FW-B0 (`docs/vv/reports/TC-SW-TOOL-001-r1.md` deviation D8): the rustos driver constructor `output_from_handle` returns `Result<_, GpioError>` (rustos `firmware/pico2/src/gpio/gpio.rs`), so a panic-free `cwht-app` needs a second failure arm that CS-11 and CS-38 do not admit. The arm calls the same `safe_state_halt()` that CS-11 prescribes for the `take()` failure. rustos defines no panic handler, and `cwht-app` defines it (`firmware/cwht-app/src/main.rs`), which differs from CS-12. Workaround while the CR is open: the code as built, recorded as deviation D8.

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The image stays in deviation from CS-11 and CS-38, and the review finding stays open. |
| Make the rustos constructor infallible | rustos is read-only to cwht agents (SI-033); the owner may change it upstream, but the error path exists for pins already in use and removing it moves the check to runtime panics. |
| `unwrap` the constructor result | Denied by CS-11 (`clippy::unwrap_used`); a panic path in flight code. |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM or budget changes. |
| Safety | The failure arm enters the same safe state as the `take()` arm (PA off, key idle, T/R receive, audio muted, charging disabled). Safety-critical module affected: the safe-state entry path of the safe-state manager (07 §14.1) through `cwht-app`; behavior unchanged. Hazard analysis re-issue: no. RF exposure evaluation change: no. |
| Risk | None added or re-scored. |
| Software classification and tailoring | None. |
| Interfaces | None. |
| Operations and ConOps | None. |
| Cybersecurity | None: neither the USB load path nor the key-input path changes. |
| Verification | TC-SW-TOOL-001 gate G5 complexity check counts the arms (when `tools/complexity_gate.py` exists); no case invalidated. |
| Cost | None. |
| Schedule | Disposition before FW-B1. |
| Requirements and traceability | None. |
| Regulatory | None. |
| Documentation | 07 CS-11, CS-12, CS-38; `firmware/cwht-app/src/main.rs` comment; `docs/vv/reports/TC-SW-TOOL-001-r1.md` deviation D8 is closed by reference in the next report revision. |
| Released units | None. |

Classification rationale: Class II. The change relaxes the wording of coding-standard rules to match a behavior-preserving failure arm; no requirement, ICD, hazard control or test case changes.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | 07 CS-11, CS-12, CS-38 as in section 1 | Claude (07 author) | |
| 2 | `firmware/cwht-app/src/main.rs` comment cites CR-001 | Claude (software lead) | |
| 3 | `tools/complexity_gate.py` per-file allowance for the admitted arms (when the tool is written) | Claude (tool owner) | |

Verification of the implementation: the independent code reviewer checks that each admitted arm contains only `safe_state_halt()`; `tools/sw_gate.sh` G1 and G5 pass.

## 6. Independent review of the impact assessment

Not required: Class II, no requirement, ICD, hazard or test impact. The code reviewer of FW-B1 checks step 2.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | pending |
| Class confirmed | pending |
| Date | pending |
| Conditions | pending |
| Rationale | pending |
| Waiver scope (if Approved (waiver)) | not applicable |
| Re-look trigger and re-look-by review (if Deferred) | not applicable |
| Source | pending: the owner's ruling, transcribed by Claude |

Disposition history:

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-26 | Submitted for disposition before FW-B1 | none | Claude |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-001` present) |
|---|---|---|
| none yet | | |

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Code comment and rules | Steps 1 and 2 | FW-B1 code review record | pending |

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | pending |
| Merge commit | pending |
| Waiver entered in CSA item 12 and affected VDDs | not applicable |
| CSA regenerated | pending |
| Date closed | pending |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-26 | Submitted | Claude (integrator) | this file's first commit | Created from deviation D8 of TC-SW-TOOL-001-r1 and INSP-016 finding-2 |
