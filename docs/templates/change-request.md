---
id: CR-NNN
title: <short imperative title, under 80 characters>
status: Draft            # Draft | Submitted | Assessed | Dispositioned | Deferred | Implemented | Verified | Closed | Withdrawn
class: I                 # proposed by Claude, confirmed by the owner in section 7: I (major) or II (minor), CM plan section 2
originator: <Owner | Claude | agent role>
date_opened: YYYY-MM-DD
phase: <Pre-A/A | B | C | D | E>                  # life-cycle phase in which the change was requested (SWEHB 5.01 item 5)
configuration_at_origination: <baseline tag or commit SHA, release id if a release is affected>   # SWEHB 5.01 item 12
baseline_affected: baseline/<srr|pdr|cdr|sar>
affected_cis: [<Table 4-1 row numbers>]          # e.g. [7, 17]
affected_paths: [<repo paths>]                    # e.g. [docs/requirements/sys/requirements.json]
affected_ids: [<REQ/TC/ICD/HZ/RSK/NCR/RID/TPM/OPS ids>]
related: [<other CR/NCR/RID/RFA/ADR ids>]
target_release: <FW-vX.Y.Z | HW-MB-rev<X>-<n> | ME-ENC-rev<X>-<n> | none>
branch: cr/CR-NNN-<slug>                          # carries only the product changes; this file is committed on main
disposition: null        # Approved | Approved with conditions | Approved (waiver) | Rejected | Deferred
disposition_date: null
relook_trigger: null     # Deferred only: the event or date that reopens the CR
relook_by: null          # Deferred only: the review by which the CR is re-dispositioned
merge_sha: null          # n/a for a Rejected CR and for a waiver that changes no artifact
date_closed: null
---

# CR-NNN: <title>

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. File location: `docs/cm/cr/CR-NNN-<slug>.md`, committed on `main` with the trailer `Refs: CR-NNN` at every state change (CM plan §5.2); the branch `cr/CR-NNN-<slug>` carries only the product changes. Fill every field; write "None: <reason>" where there is no impact. Blank cells are not accepted (CM plan §5.3). Machine-read fields live in the front matter and are parsed by `tools/csa.py`; keep them valid YAML.

## 1. Description of the change

<What changes, stated precisely: before and after text for each requirement or ICD clause, the schematic or layout change, the code change, the document change. Reference IDs and paths. For a waiver request: the requirement or SWE-219/SWE-220 target, the module, the measured shortfall or exceedance.>

## 2. Reason

<Why the change is needed: the RID, NCR, test result, vendor DFM comment, analysis, stakeholder input (SI-NNN) or research report that motivates it. Workaround available while the change is developed (SWEHB 5.01 item 13), or None.>

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | |
| <alternative> | |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | <TPM/MOP ids; value and margin before and after; budgets touched> |
| Safety | <HZ ids affected; every module of the safety-critical and mission-critical tables of 07 §14.1 that changes, by module id, or None; hazard analysis re-issue yes/no; RF exposure evaluation change yes/no> |
| Risk | <RSK ids added, closed or re-scored, with likelihood and consequence before and after> |
| Software classification and tailoring | <classification record, rmm.json rows or compliance-matrix rows changed, or None> |
| Interfaces | <ICD ids affected; external-interface change yes/no> |
| Operations and ConOps | <OPS ids affected; operator procedures, operations handbook or maintenance instructions changed yes/no (yes makes the CR Class I)> |
| Cybersecurity | <USB firmware-load path or key-input command path changed yes/no (charter §12; 07 §16); mitigations affected> |
| Verification | <TC ids invalidated, added, modified; evidence class; re-test scope; decision tables and independence-pair tests affected for safety-critical modules (07 §9.6)> |
| Cost | <BOM delta, re-fabrication or re-machining, shipping, contingency> |
| Schedule | <vendor lead time, gate affected, dependent CRs> |
| Requirements and traceability | <REQ ids added, modified, deleted, retired by level; parents and children affected; volatility contribution> |
| Regulatory | <47 CFR Part 97 clauses (and Parts 1, 2, 15 where relevant) affected, or None> |
| Documentation | <every document that must change, including VDD or package manifest> |
| Released units | <unit serials CWHT-A-NNN needing rework, re-flash or recall, or None> |

Classification rationale: <why Class I or Class II. The classes are adapted from the SE HB §6.5.1.2.3 major and minor changes; Class I and Class II are project labels defined in CM plan §2.>

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | | | |

Verification of the implementation (what the independent reviewer will check, which TCs run, which analyses rerun):

## 6. Independent review of the impact assessment

Required for Class I, and for Class II when requirements, ICDs, hazards or test cases are affected; otherwise write "Not required: Class II, no requirement/ICD/hazard/test impact".

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| | | | | |

Reviewer concurrence: <Concur | Concur with comments | Object>.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | <Approved, Approved with conditions, Approved (waiver), Rejected or Deferred> |
| Class confirmed | <I or II> |
| Date | YYYY-MM-DD |
| Conditions | <conditions that must be met before merge, or None> |
| Rationale | |
| Waiver scope (if Approved (waiver)) | <requirement or target waived, module, releases affected, end condition> |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | <chat transcription by Claude on YYYY-MM-DD, or edited directly by owner> |

Disposition history (append only; a CR targeted at a release is left out of it only by an owner re-disposition recorded here before the release's source commit, CM plan §5.1 and §8.1 step 1):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-NNN` present) |
|---|---|---|
| | | |

Traceability report after implementation: <path or link>; renders regenerated: <paths>.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| | | | |

Independent verifier (agent invocation): <name>, date, result <Pass | Fail>.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | <date, source; n/a for Rejected> |
| Merge commit | <SHA> (`merge(CR-NNN): <title>`), or n/a (Rejected; waiver without artifact change) |
| Waiver entered in CSA item 12 and affected VDDs | <yes, date; n/a if not a waiver> |
| CSA regenerated | <date> |
| Date closed | YYYY-MM-DD |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| YYYY-MM-DD | Draft | | | Created |
