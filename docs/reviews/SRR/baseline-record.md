---
baseline: functional
review: SRR
tag: baseline/srr
date: 2026-09-26
decision_memo: docs/reviews/SRR/decision-memo.md
disposition: Approved with liens
previous_baseline: none
# Fill-once fields (CM plan Table 4-1 row 32): each holds "pending (§8a)" in the tagged commit R
# and is written exactly once in the post-tag record commit (CM plan §4.4 step 6).
commit: pending (§8a)                 # SHA of the tagged commit R, `git rev-parse baseline/srr^{commit}`
tag_object: pending (§8a)             # SHA of the tag object, `git rev-parse baseline/srr`
signed: pending (§8a)                 # false expected: no signing key is configured (charter §8; SRR decision 15 sets signing before baseline/pdr)
signature_verified: pending (§8a)     # n/a expected (unsigned annotated tag)
pushed_hash: pending (§8a)            # hash returned by `git ls-remote --tags origin baseline/srr`
---

# Baseline record: functional baseline (`baseline/srr`)

Template: `docs/templates/baseline-record.md`. Procedure: `docs/process/05-configuration-and-data-management.md` §4.4. Location: `docs/reviews/SRR/baseline-record.md`. Class: Record (CM plan Table 4-1 row 32). Prepared by Claude (CM function, integrator) on 2026-09-26 under the owner's SRR approval ("I approve of this and the SRR.", `docs/reviews/SRR/minutes.md`) and the sequencing of decision memo section 9: the post-ruling work R16 is verified by the reviewers, and only then is `baseline/srr` created.

## 0. Record status: prepared, tag held

This revision is the prepared record, **not commit R**. The tag `baseline/srr` is not applied on this commit, because the preconditions of decision memo section 9 (conditions 2 and 3) and of CM plan §4.4 step 1 are not all met on 2026-09-26. Each open precondition is listed below with its owner and closure path; none is hidden and none is converted into a lien, because memo section 9 condition 2 says the open Major findings close before the tag and are never liens. Because this revision is not R, it confers no level: the CIs of §2a reach L2 only when R is committed and tagged (CM plan §4.1 L2 is read here with the §4.4 step 3 meaning of "committed baseline record"), and the "Level after tag" column states the level they will then hold.

| # | Precondition (source) | State on 2026-09-26 at `be270f1` | Closure path and owner |
|---|---|---|---|
| P1 | No open Major finding in the SRR records (memo §9 condition 2; §4.4 step 1 L1 rule) | **Not met.** Three records hold an open Major: INSP-002 (`checklists/conops-and-concept.md`, NEEDS CHANGES at `7c7959f`: finding-23 ConOps bench-test mode scope against REQ-SYS-187 and 188, and finding-24 `docs/design/concept.md` not updated for decisions 25, 37 and 38 to 41); INSP-009 (`checklists/classification-03-software-classification-and-rmm.md`, NEEDS CHANGES at `bb28ed6`: finding-11, `render_rmm.py --check` failed on SWE-033); INSP-016 (`checklists/fw-b0-toolchain-proof.md`, NEEDS CHANGES at `f6e167c`: F-01, FW-B0 gate does not exit 0) | INSP-009 finding-11: author fix applied at `7d735e5` (SWE-033 In place, SRR decision 107); `render_rmm.py --check` now exits 0; the INSP-009 reviewer delta-verifies. INSP-002 finding-23 and finding-24: ConOps and concept author edits, then INSP-002 delta re-issue. INSP-016 F-01: see P6 |
| P2 | The five Major findings that waited on the rulings are closed (memo §9 condition 2) | **4 of 5 closed.** INSP-003 finding-6 Verified (`401b01d`, decision 30); INSP-011 F-01 and F-04 Closed (`f058c58`, decisions 106 and 47); INSP-016 F-02 Closed (`f6e167c`, decision 108). INSP-016 F-01 stays Open | P6 |
| P3 | `tools/validate_docs.py` exit 0 and the unit tests passing (Table 4-2 rows 9 and 53) | **Not met.** 45 of 50 pass. Five APPROVED records name product blobs that R16 changed (record drift rule): INSP-017 (rmm.json, rmm.md), INSP-006 (rmm.json), INSP-018 (07), INSP-013 and INSP-027 (TS-002 Status line, decision 107). Unit tests: 400 run, 1 failure (`test_repository_exit_zero`, the same cause) | Each record's reviewer delta-verifies the changed blob and re-issues; the integrator does not edit a reviewer's `product_files` (charter §2 independence) |
| P4 | `tools/traceability.py` passes (§4.4 step 1; §1 row below) | **Not met.** 4 violations, all `HAZARD_REQ_NOT_TESTED` on REQ-SYS-122, 124, 137 and 138, which now carry method Inspection under CR-002 (SRR decision 113). CR-002 step 5 (the tool accepts the Inspection route) is scheduled before the PDR readiness declaration (CR-002 section 4, Schedule), and 04 §7.4 row 7.3.6 requires a manual check until then; INSP-008 recorded that check (each has method Inspection, the CR-002 note and a closing Inspection case) | Owner choice (see P9): either a numbered departure in `docs/cm/deviations.md` for §4.4 step 1 on these four requirements only, citing the INSP-008 manual check, or CR-002 step 5 performed now with the TV-002 re-validation, the INSP-015, INSP-017 and INSP-020 delta re-issues (they cite the `tools/traceability.py` blob) and an extension of ACC-TRACE-001 by the owner |
| P5 | Every CI holds its Table 4-2 admission evidence | **Partly met.** See §2a column "Admission". Open: row 2 (07 through INSP-018 drift; 05 through INSP-006 drift), row 3 (03 and rmm.json through INSP-009 NEEDS CHANGES and INSP-017 drift; SRR decision 1 approves each plan only when its record is APPROVED with no open Major), rows 6 and 52 (INSP-002 NEEDS CHANGES), row 9 and 53 (P3), row 17 (P4). Met: rows 1, 5, 7, 27, 51 | As P1, P3, P4 |
| P6 | Hard entrance row 20 (FW-B0 toolchain proof) Met (memo §9 condition 2) | **Not met.** OA-1 and OA-2 were performed with the owner on 2026-09-26 and passed (minutes, "OA-1 and OA-2 performed (deferral reversed)"), so the owner part is done; the raw outputs are not yet filed (`docs/vv/reports/TC-SW-TOOL-001-r4.md` does not exist). The gate `tools/sw_gate.sh` does not exit 0: at the rustos pin `c54d35a` cargo deny and the unsafe audit fail; on the decision 110 branch complexity and Miri fail | Owner merges the rustos branch `cwht/wp-sw-licence-manifest-safety` (`2ec64c0`) and approves the CR that moves the pin; `tools/sw_gate.sh` fix (INSP-016 F-14: one `--paths` per path); 07 owner rules the CC counting convention and CR-001 step 3 lands; owner approves the rust-src and Miri sysroot download (not covered by decision 109); a gate run exits 0 and is filed as run 4 with the OA-1 and OA-2 raw outputs; INSP-016 iteration 4 |
| P7 | The functional baseline content carries the rulings (memo §9 condition 3) | **Not met for two CIs.** `docs/requirements/l0-stakeholder/expectations.json` (row 5): 23 "owner decision pending at SRR" phrases remain, and NGO-021 and the MOE-012 success criterion predate SRR decision 37 (no-gap watchdog, 2 s squeeze limit). `docs/design/concept.md` (row 52): INSP-002 finding-24 | L0 author edit citing decision 37 and the ruled decisions, then INSP-001 delta re-issue; concept author edit, then INSP-002 delta |
| P8 | Repository protection in place before the tag (SRR decision 15; OQ-CM-001) | **Not observed.** `gh` is not installed on this machine, so the GitHub branch and tag protection could not be read | Owner enables branch protection on `main` and tag protection for `baseline/*` and `release/*` on github.com/robinonsay/cwht and confirms in chat; Claude transcribes it |
| P9 | L1 requirement status Draft to Active at the baseline (08 §3.1 Status: L1 moves to Active on the owner's baseline decision memo) | **Not done.** 188 L1 requirements are Draft (2 Closed are retired items) | Claude makes the status change in the commit before R, and the INSP-003 reviewer re-issues on the status-only delta |
| P10 | `main` pushed with the tag (charter §8; §4.4 step 5) | Local `main` at `be270f1` is 31 commits ahead of `origin/main` (`7647516`); nothing has been pushed since the minutes | At step 5, after the owner's go-ahead |

Owner decisions needed before R (also listed in §5): the P4 route; the rust-src and Miri download (P6); the rustos branch merge and pin CR (P6); the 07 CC counting convention (P6); repository protection (P8); the route for decision 18 in ADR-014 (Accepted ADR, 05 Table 4-1 row 13) and the charter section 2 capacities of decision 7 and wording items of decision 10 (the charter is owner-controlled).

When P1 to P9 are met, Claude refreshes §2 with the hashes of the parent of R, sets §0 to "commit R", and commits the record as R with message `baseline(srr): record functional baseline` and trailer `Refs: SRR` (§4.4 step 3).

### 0.1 Status update, 2026-09-26 at `2f619f8`

Status line, 2026-09-26 (Claude, integrator and CM function): preconditions re-checked at HEAD `2f619f8` after the R16 delta re-issues and the owner's close-out rulings (minutes, "Close-out decisions (after the first close-out run)", `dd39332`: items 1 to 12 ruled as recommended, CR-004 approved). **The tag stays held: P1, P2, P3, P4, P5, P6, P7, P8, P9 and P10 are not all met.** `baseline_tag` in the decision memo stays `null`; no tag is applied. The table above is kept as the record of the state at `be270f1`; this table gives the state at `2f619f8` and supersedes it for current status. The §2 hashes are still those of `be270f1` and are refreshed only on the parent of R (§0 last paragraph).

Tool results at `2f619f8` (2026-09-26): `tools/validate_docs.py` exit 1, 49 of 50 pass; `tools/traceability.py --report-only` 245 requirements, 173 test cases, 4 violations, 2 warnings (process exit 0; rendered files restored with `git checkout`); `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0 (65 risks, 159 candidates, 0 warnings, `register.md` current); `tools/render_rmm.py --check` exit 0 (100 rows, `rmm.md` current); `tools/render_compliance.py --check` exit 0 (62 rows, rendered file current); `python -m unittest discover -s tools/tests` 400 run, 1 failure (`test_repository_exit_zero`).

| # | Precondition | State on 2026-09-26 at `2f619f8` | Evidence | Remaining closure path and owner |
|---|---|---|---|---|
| P1 | No open Major finding in the SRR records | **Not met.** Two records hold an open Major: INSP-001 (`checklists/expectations.md`, NEEDS CHANGES at `e88823f`: finding-14, MOE-006 still judges the band edge at the pre-decision-25 guard limits 144.001 and 147.999 MHz, against NGO-011, REQ-SYS-008 and ConOps section 3.5 after SRR decision 25 (a)); INSP-016 (`checklists/fw-b0-toolchain-proof.md`, NEEDS CHANGES at `f6e167c`: F-01, FW-B0 gate does not exit 0). Closed since `be270f1`: INSP-002 finding-23 and finding-24 (APPROVED at `1cb8b12` on `dd3372c`); INSP-009 finding-11 (APPROVED at `b54064b` on `7d735e5`). The other 28 SRR records are APPROVED | `verdict` of all 30 records in `docs/reviews/SRR/checklists/` at `2f619f8` | INSP-001 finding-14: L0 author edit of MOE-006 (SRR decision 25 (a)), then INSP-001 delta re-issue. INSP-016 F-01: see P6 |
| P2 | The five Major findings that waited on the rulings are closed | **4 of 5 closed** (unchanged). INSP-016 F-01 stays Open | As at `be270f1`; INSP-016 not re-issued since `f6e167c` | P6 |
| P3 | `tools/validate_docs.py` exit 0 and the unit tests passing | **Not met.** Exit 1, 49 of 50 pass. One FAIL: INSP-015 (`checklists/tool-validation-tv-001-to-tv-010.md`, APPROVED, `product_commit` `7c7959f`) record drift on `tools/toolchain.lock.md`: reviewed blob `5c04ea9e`, HEAD blob `dfc8a415` (changed at `37ae576`, TC-SW-TOOL-001 run 4: picotool `verify` rows and the `tools/sw_gate.sh` row). One note, not a failure: INSP-016 (NEEDS CHANGES) names `tools/sw_gate.sh@54b13800`, HEAD `52b9f803` (F-14 fix at `37ae576`). Unit tests: 400 run, 1 failure, `test_repository_exit_zero`, the same cause. The five drift failures of `be270f1` (INSP-017, INSP-006, INSP-018, INSP-013, INSP-027) are cleared by their re-issues (`c92c6f6`, `d8df6a9`, `183aa88`, `ab38255`, `bec5c34`) | `validate_docs.py` and unittest runs at `2f619f8` | INSP-015 reviewer delta-verifies `tools/toolchain.lock.md` and re-issues; because CR-004 (P6) changes the same file again, the re-issue is best made after the CR-004 commit. The integrator does not edit a reviewer's `product_files` (charter §2) |
| P4 | `tools/traceability.py` passes | **Not met.** 4 violations, unchanged: `HAZARD_REQ_NOT_TESTED` on REQ-SYS-122, 124, 137 and 138. The route is now ruled: close-out item 5 (update `tools/traceability.py` now under CR-002 step 5, re-validate and re-accredit; no deviation). Not yet done: `tools/traceability.py` last changed at `1d423e5` | `traceability.py --report-only` at `2f619f8`; minutes `dd39332` item 5 | Tool owner: CR-002 step 5 change to `tools/traceability.py`; TV-002 re-validation; independent review of the validation record, then the owner extends ACC-TRACE-001 (minutes: "their accreditations are extended once the independent review of each validation record is complete"); INSP-015, INSP-017 and INSP-020 delta re-issues on the new tool blob. Note for the tool owner: the `--report-only` run exits 0 with 4 violations |
| P5 | Every CI holds its Table 4-2 admission evidence | **Partly met.** Now met: row 1 (charter at `6ea6b1d` carries SRR decisions 7 and 10 (a), (b); memo amendment A-5 at `7d37d18`; INSP-027 and INSP-030 re-issued on it); row 2 (05 at `0834da2`: INSP-006 `d8df6a9`, INSP-030 `ff0a610`; 07: INSP-018 `183aa88`; schedule rebaseline at `d4c9366`: INSP-023 `2f619f8`); row 3 (INSP-009 `b54064b`, INSP-017 `c92c6f6`); rows 6 and 52 (INSP-002 `1cb8b12`); ADR-014 erratum for decision 18 at `5122a6b` (INSP-011 `877ffac`). Open: row 5 (INSP-001 NEEDS CHANGES, P1); rows 9 and 53 (P3); row 17 (P4); row 28 `tools/toolchain.lock.md` (INSP-015 drift, P3) | Record verdicts and commits above | As P1, P3, P4 |
| P6 | Hard entrance row 20 (FW-B0 toolchain proof) Met | **Not met.** Done: OA-1 and OA-2 raw outputs filed as TC-SW-TOOL-001 run 4 (`docs/vv/reports/TC-SW-TOOL-001-r4.md`, `37ae576`; steps 11, 12 and OA-2 Pass, run result Blocked, `credit: false`); `tools/sw_gate.sh` F-14 fix (one `--paths` per path, blob `52b9f803`, `37ae576`); owner merged the rustos branch (rustos `master` at `2ec64c0`, minutes `dd39332`); owner ruled close-out items 1, 2 and 4 and approved CR-004. Not done: CR-004 not applied (the `tools/toolchain.lock.md` §3 pin still reads `c54d35a` while the rustos checkout is at `2ec64c0`, so gate G0 fails; `firmware/unsafe-audit.md` not regenerated); the `rust-src` and Miri sysroot download of item 2 not yet made (lock row `nightly-2026-08-24` has no `rust-src`); the item 4 CC-convention CR is not written (only CR-001 and CR-002 exist in `docs/cm/cr/`) and `tools/complexity_gate.py` is unchanged; no gate run exits 0 | Run 4 report; `tools/toolchain.lock.md` §3 at `2f619f8`; `git -C ../rustos rev-parse HEAD` = `2ec64c0`; minutes `dd39332` | Claude (tool owner): CR-004 commit (pin to `2ec64c0` and `unsafe_audit.py --write` in one commit); the approved item 2 download; the item 4 CR, `tools/complexity_gate.py` change (+1 per `let ... else`, CS-38 allowance for the two CS-19 halt loops) and TV-012 re-validation with independent review; a full gate run with exit 0 filed as TC-SW-TOOL-001 run 5; then INSP-016 iteration re-issue (F-01, F-14) |
| P7 | The functional baseline content carries the rulings | **Not met for one CI.** `docs/design/concept.md` (row 52) met at `dd3372c` (INSP-002 APPROVED `1cb8b12`). `docs/requirements/l0-stakeholder/expectations.json` (row 5) carries the rulings at `d4c9366` (0 "owner decision pending at SRR" phrases; NGO-021 and MOE-012 match SRR decision 37) except MOE-006 (INSP-001 finding-14, decision 25 (a)) | INSP-001 at `e88823f`; INSP-002 at `1cb8b12` | As P1 |
| P8 | Repository protection in place before the tag | **Not met (ruled, not confirmed).** Close-out item 6 rules the form: a ruleset on `main` blocking force-push and deletion, and a tag ruleset on `baseline/*` and `release/*` blocking update and deletion, no pull-request requirement. The owner has not yet confirmed it is done; `gh` is still not installed, so the settings were not read | Minutes `dd39332` item 6 ("The tag waits for the owner to confirm it is done") | Owner sets the rulesets on github.com/robinonsay/cwht and confirms in chat; Claude transcribes the confirmation into the minutes |
| P9 | L1 requirement status Draft to Active at the baseline | **Not done.** 188 L1 requirements Draft, 2 Closed (`docs/requirements/sys/requirements.json` at `2f619f8`) | Status count at `2f619f8` | Claude makes the status-only change in the commit before R, after P1 and P7 close; INSP-003 re-issues on the status-only delta |
| P10 | `main` pushed with the tag | **Not done.** Local `main` at `2f619f8` is 51 commits ahead of `origin/main` (`7647516`, confirmed by `git ls-remote origin refs/heads/main`) | `git rev-list --count origin/main..HEAD` = 51 | At §4.4 step 5, after the owner's go-ahead and P8 |

Close-out confirmations that do not block the tag (minutes `dd39332` items 3 and 7 to 12), state at `2f619f8`: item 12 done (`brew list --pinned` shows `python@3.13`); item 3 partly observed (rustup reports 1.29.1; the `auto-self-update disable` setting was not read); item 8 not yet done (no RFA for the CR-002 independent impact review in `docs/reviews/SRR/rfa-rid-log.json`, last changed at `0bcea39`); items 7, 9, 10 and 11 are confirmations with no repository action required by this record.

## 1. Baseline definition

| Field | Value |
|---|---|
| Baseline | Functional baseline per SE HB §6.5.1.2.2, set at SRR per charter §3 and CM plan §4.4 (SRR combined with MCR, customization in CM plan §1) |
| Contents | Table 4-1 rows 1, 2, 3, 5, 6, 7, 9, 17 (cases citing L1 requirements), 27, 51, 52, 53 (CR class); informational rows 14 and 15; row 28 (tools with a TV record by SRR) as controlled items outside the baseline set. Charter §3 core: NGOs, MOEs, ConOps, L1 requirements, SEMP |
| Decision memo | `docs/reviews/SRR/decision-memo.md`, disposition Approved with liens, signed 2026-09-26; memo commit `0bcea39554d684ba28d6680208a523fd79a8ebba` (the commit that set `signed`; later commits append amendments in its section 13 only) |
| Review package | `docs/reviews/SRR/package.md` revision 8 final at `a6d0959`; deck `docs/reviews/SRR/slides/srr.adoc` at `64e53ee` |
| Traceability report at this commit | Review evidence: `docs/reviews/SRR/traceability-report.md` (package revision, PASS, 0 violations, 3 warnings), kept as the SRR evidence and not regenerated after the review (Table 4-1 row 18). Run on 2026-09-26 at `be270f1` (`tools/traceability.py --render --output <scratchpad>`, which left every rendered file unchanged): 245 requirements, 173 test cases, **4 violations** (P4), 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and 148). Result: **not clean**; `docs/vv/traceability-report.md` is regenerated at R |
| `git fsck --full` on the parent of R | Run 2026-09-26 at `be270f1`: exit 0 (three dangling blobs, no errors). Re-run at R |
| Table 4-1 match check (`git ls-files` against the Table 4-1 pathspecs) | 1108 tracked files at `be270f1`; the row match is not automated (no `tools/csa.py`) and is performed at R by the 05 §7.4 interim check |

## 2. Configuration items

Hash from `git rev-parse be270f1:<path>` (blob for files, tree for directories), `be270f1` being the parent of this record commit. Peer review = the filled checklist `docs/reviews/SRR/checklists/<product-slug>.md` (id `INSP-NNN`). "Admission" states the Table 4-2 evidence at `be270f1`.

### 2a. CIs in this baseline (class CR)

| Row (Table 4-1) | CI | Path | Hash | Level after tag | Peer review record (`INSP-NNN`, checklist path) | Admission (Table 4-2) |
|---|---|---|---|---|---|---|
| 1 | Process charter | `docs/process/00-charter.md` | `131608b78e178432e34f8eb9fc385dae07020c6d` | L2 | none (owner direction; Table 4-2 row 1) | Met: SRR decision 1 approves the charter by name (memo §8.0.1 row 1); last changed at `4e3f891`. Pending owner edits: decision 7 capacities and decision 10 items (a) to (c) |
| 2 | 01 Life cycle and reviews | `docs/process/01-lifecycle-and-reviews.md` | `eabbbd57953c84164e848f36dc327542ac015c00` | L2 | INSP-019 `process-01-lifecycle-and-reviews.md` | Met: APPROVED, blob current |
| 2 | 02 Requirements and traceability | `docs/process/02-requirements-and-traceability.md` | `fcdc544555477f0115535348f8ce388453a9034f` | L2 | INSP-020 `process-02-requirements-and-traceability.md` | Met: APPROVED, blob current |
| 2 | 04 Verification and validation | `docs/process/04-verification-and-validation.md` | `0b197bba692237ed9860ba49c4422f12fa8512dc` | L2 | INSP-021 `process-04-verification-and-validation.md` | Met: APPROVED (post-ruling delta `a8d3166`, CR-002 step 1) |
| 2 | 05 Configuration and data management | `docs/process/05-configuration-and-data-management.md` | `63ed566240ffc7f055b65f93f579a6bb1498e9f1` | L2 | INSP-006 `cm-plan-05.md` with INSP-030 `cm-plan-05-software-assurance.md` | Not met: INSP-006 fails the drift rule on `rmm.json` (P3) |
| 2 | 06 Risk and decision analysis | `docs/process/06-risk-and-decision-analysis.md` | `7a92d21f24a1733d70ae083576e708274bfd1a6d` | L2 | INSP-007 `risk-register-06.md` | Met: APPROVED with liens (`a50aba8`) |
| 2 | 07 Software engineering plan | `docs/process/07-software-engineering-plan.md` | `37d472b501578504b7fa23422c4f74193647e458` | L2 | INSP-010 `software-plan-07.md` with INSP-018 `software-plan-07-software-assurance.md` | Not met: INSP-010 APPROVED with liens (`6136712`); INSP-018 fails the drift rule (CR-001 at `4364ebb`, P3) |
| 2 | 08 Agent briefing | `docs/process/08-agent-briefing.md` | `01a36bac8d5f133dadd5b384f92f95f225371663` | L2 | INSP-022 `process-08-agent-briefing.md` | Met: APPROVED, blob current |
| 2 | Process index | `docs/process/README.md` | `3664073bc2563f604fb7b1c639a2689a20fb0e6a` | L2 | none (index; §7.4 interim check) | Check at R |
| 2 | SEMP | `docs/plan/semp.md` | `ccfdecf98a6e2dc1371eb057e6aa37903b672de1` | L2 | INSP-005 `semp.md` | Met: APPROVED with liens (`1e56df4`) |
| 2 | Schedule | `docs/plan/schedule.md` | `53de92ae211105127f56103d26884d14342190d0` | L2 | INSP-023 `schedule-and-cost-estimate.md` | Met: APPROVED. The owner approved a rebaseline in the minutes (PDR about Tue 2026-09-29); the file still carries the earlier dates and is updated with an INSP-023 delta (minutes, "Schedule and enclosure inputs") |
| 2 | Cost estimate | `docs/plan/cost-estimate.md` | `0dda83cbd5ada9474562cc1741df67a31e1a7ffb` | L2 | INSP-023 `schedule-and-cost-estimate.md` | Met: APPROVED |
| 3 | Software classification record | `docs/process/03-software-classification-and-rmm.md` | `ed270f443e2ab648480017df8ad3d0221400cf4c` | L2 | INSP-009 `classification-03-software-classification-and-rmm.md` with INSP-017 (assurance) | Not met: INSP-009 NEEDS CHANGES (finding-11); INSP-017 drift (P1, P3) |
| 3 | Requirements Mapping Matrix | `docs/process/rmm.json` | `e326ddd1b7296d7d7fe172be6f33535cee3192d7` | L2 | INSP-009, INSP-017 | Tool part met: `render_rmm.py --check` exit 0 at `be270f1` (after `7d735e5`); record part not met (as above) |
| 3 | RMM rendering | `docs/process/rmm.md` | `54e351f4df231d1a1e74e6eef4bd07db9a408fa0` | L2 | rendered | Met: `render_rmm.py --check` exit 0 |
| 3 | Compliance matrix | `docs/process/se-compliance-matrix.json` | `790d256214e07beb736f2f414a8eaf384ecf2440` | L2 | INSP-024 `compliance-matrix.md` | Met: APPROVED; `render_compliance.py --check` exit 0 |
| 3 | Compliance matrix rendering | `docs/process/se-compliance-matrix.md` | `09426930b27e3b51182ab28086c6c73000f274d9` | L2 | rendered | Met: `render_compliance.py --check` exit 0 |
| 5 | Stakeholder expectations (30 NGOs, 13 MOEs, 28 constraints, 10 stakeholders) | `docs/requirements/l0-stakeholder/expectations.json` | `59e7efba9e64da33285e4f780b2a3bae2753f45c` | L2 | INSP-001 `expectations.md` | Record met (APPROVED, blob current); content not yet aligned to the rulings (P7) |
| 5 | Expectations rendering | `docs/requirements/l0-stakeholder/expectations.md` | `3ac5617dc1c2933eed86c1f88c7bb88286b3f866` | L2 | rendered | Met: `traceability.py --render` leaves it unchanged |
| 6 | ConOps (directory) | `docs/conops/` | tree `35843619b929521cba035cd91856b65696438ba6` | L2 | INSP-002 `conops-and-concept.md` | Not met: NEEDS CHANGES (finding-23) |
| 6 | ConOps revision 3 | `docs/conops/conops.md` | `36f0eb9ecb3059a6c556a4c367a1f8f940c6aa06` | L2 | INSP-002 | as above |
| 6 | ConOps figures | `docs/conops/figures/conops-context.mmd`, `.png`; `conops-modes.mmd`, `.png` | `55ebae2e15589bf9951456dc04400b7ccb96ea27`, `2e4647f81c61a1d2df05637efa3ee3d71a506e09`; `829a46f800db84ae5196cf3946d4376eb813fc0f`, `b3a08b6770c7c019b67e4b19cd2cdcbba3e8ce6c` | L2 | INSP-002 | as above |
| 7 | L1 requirements (directory) | `docs/requirements/sys/` | tree `5b4fbadb43ca656d383152515b9ededfc36873d5` | L2 | INSP-003 `requirements-sys.md` | Met: APPROVED with liens (`401b01d`, blobs at `ebe5873` current) |
| 7 | L1 requirements (190 items: 188 Draft, 2 Closed retired) | `docs/requirements/sys/requirements.json` | `52768afc4f5c3948ca4a2c93be6fd6b9de1c0d33` | L2 | INSP-003 | as above; status change at the baseline pending (P9) |
| 7 | L1 rendering | `docs/requirements/sys/requirements.md` | `21d25ea38766d079f188555061b8372a5b0c977c` | L2 | rendered | Met |
| 9 | Schemas | `docs/design/allocation.schema.json`; `docs/plan/measurements.schema.json`; `docs/plan/tpm.schema.json`; `docs/process/rmm.schema.json`; `docs/process/se-compliance-matrix.schema.json`; `docs/requirements/l0-stakeholder/schema.json`; `docs/requirements/schema.json`; `docs/risk/schema.json`; `docs/safety/schema.json`; `docs/templates/rfa-rid-log.schema.json`; `docs/test_cases/schema.json` | `c17e011ba352839fd8c816a9ef5daf978757dfe2`; `c30b7f3e7466bf4e4474afd031c2c9c91db42be8`; `df3bd894ffec8841245617d0b0c7be6457ddd632`; `ae2f87dd97c7dc9b0e9e4fd5eccbdf35db69e13b`; `ef156b0fcfaaca3b44543154a454b0a965e72a2c`; `d0a79903f8952ed75cf421ff2a73d068f6a32b29`; `ca049dfb0a4480f8de889fe112add0a2e893915f`; `473cd797db582ae2dc4ed14fa83213c3bf2a6d09`; `e96accaad02dcb33a3dfdbcc8da11fd4f28bed84`; `38898b0c260c3292fbc65c59d632790ad4e650f7`; `d4b70163ca13c6263147a49a39f602b88a81517a` | L2 | none (no checklist for schemas) | Not met: `validate_docs.py` exit 1 and 1 unit-test failure (P3); every schema-governed data file itself passes; TV-001 and TV-003 Accredited (ACC-PYJS-001, ACC-VALDOCS-001 at blob `3aa03681`, the current blob) |
| 17 | Test cases citing L1 requirements (113 TC-SYS cases) | `docs/test_cases/sys/test_cases.json` | `a18824aaf62d5139cdc558e52174726bd5d2f673` | L2 | INSP-025 `test-cases-sys.md` | Record met (APPROVED, post-ruling delta `08e5c9b`); tool part not met (P4) |
| 17 | TC-SYS rendering | `docs/test_cases/sys/test_cases.md` | `45e7ca5101b2def1a1f9f7d7ea5e2aa3e851e21a` | L2 | rendered | Met |
| 27 | Toolchain lock | `tools/toolchain.lock.md` | `5c04ea9e04a0d59a563708ca51e3dacdb7384661` | L2 | INSP-015 `tool-validation-tv-001-to-tv-010.md` (review of the lock rows with TV-001 to TV-010) | Met: TV-001 to TV-010 Accredited (SRR decision 114); lock §1.1 sanity checks recorded |
| 27 | Venv pins | `tools/requirements.txt` | `ef9820618aafd7fb8d62a24fda4f029a3ffdeb62` | L2 | none | Met: AL-4 comparison at `be270f1`: the 35 pins equal `.venv/bin/pip freeze` (pinned at `be270f1`, 05 §14.1 item AL-4) |
| 51 | Technology and heritage assessment | `docs/plan/technology-assessment.md` | `d46abde01adf320630dc317d0a80aa6f197181e5` | L2 | INSP-014 `technology-assessment.md` | Met: APPROVED, blob current |
| 52 | Design concept | `docs/design/concept.md` | `729190a21066f27525fe5d6e5160e3fa4d22e21b` | L2 | INSP-002 `conops-and-concept.md` | Not met: finding-24 (P1, P7) |
| 53 | Templates and peer-review checklists (21 files; the schema in the folder is row 9) | `docs/templates/` | tree `e94d4ce59c8b62879a1627950eca953281415c03` | L2 | none (Table 4-2 row 53: validation by tools; each checklist admitted at the revision cited by the SRR records) | Not met until P3 closes (the example files validate) |

### 2b. Informational items (recorded, not yet CR-controlled)

| Row | CI | Path | Hash | Current level |
|---|---|---|---|---|
| 14 | Risk register (65 risks) | `docs/risk/register.json`, `docs/risk/register.md` | `0c25c0c5b6ca801b02e47c29c19bb8ed44aa5c79`, `a3a983e5cdf7e769666fab26d5f2e7f3b373db1f` | L1 (INSP-007 APPROVED with liens); `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0 |
| 15 | Preliminary hazard analysis 0.5.0-pha | `docs/safety/hazard-analysis.md`, `docs/safety/hazards.json` | `52c8ce16856499afc1b701e1ddb103788fcb1af9`, `81cacde47d4f2066ecac3947f3acf65e646b1ad0` | L1 (INSP-008 APPROVED with liens, `8fc3402`); CR-controlled from PDR |
| 8 | Early L2 requirements: REQ-TX (16) and REQ-SW-KEYER (39) | `docs/requirements/tx/requirements.json`, `docs/requirements/sw/sw-keyer/requirements.json` | `8b9d81e8d0f8f605427ef5876adc0f891585a569`, `f9141160c4d92ad80ae91144c2499b22292d4b16` | L1 (INSP-004 APPROVED with liens `216098e`; INSP-026 APPROVED `ccf742c`); allocated baseline at PDR |
| 17 | Test cases of the early L2 and tool modules (TC-TX, TC-SW-KEYER, TC-SW-TOOL) | `docs/test_cases/tx/test_cases.json`, `docs/test_cases/sw-keyer/test_cases.json`, `docs/test_cases/sw-tool/test_cases.json` | `3528d0626e450345a79c9865780db0938b8cff05`, `2716ca3f53d349c84f2a4a717a3b7daa1566792f`, `fee1e7246af59d5e8a43ed1b9cdf483854053fdc` | CR-controlled from PDR (Table 4-1 row 17, "all other cases") |
| 4 | Stakeholder inputs log (Record, SI-001 to SI-037) | `docs/requirements/l0-stakeholder/stakeholder-inputs.md` | `bcc2ec9f0822b3b3866b10329fe1ce4ddc9e7841` | Record (append-only) |

### 2c. Controlled items outside the baseline set

| Row | CI | Path or pin | Hash or commit | CR-from event and date | TV record (row 28) |
|---|---|---|---|---|---|
| 28 | Traceability checker | `tools/traceability.py` | `0a867523f78c224afdaa938735911b5df8f2920c` | TV-002 accreditation, 2026-09-26 | TV-002, ACC-TRACE-001 (at this blob) |
| 28 | Document validator | `tools/validate_docs.py` | `3aa0368147b9af3e6e1546f808afb7aedf7f2226` | TV-003 accreditation, 2026-09-26 | TV-003, ACC-VALDOCS-001 (extension at this blob, commit `96af250`) |
| 28 | RMM renderer | `tools/render_rmm.py` | `2386a37fbfb9d7d06c333e0f00981b6fc67e1f27` | TV-004, 2026-09-26 | TV-004, ACC-RMM-001 |
| 28 | Compliance renderer | `tools/render_compliance.py` | `d67d6b5e601a64b013b64e8de3cd0fc3deb96ffa` | TV-005, 2026-09-26 | TV-005, ACC-COMPL-001 |
| 28 | Risk renderer | `tools/render_risk.py` | `d38ba1dd25ac8ef5ecb04ce5b1ea907bb60eee8c` | TV-006, 2026-09-26 | TV-006, ACC-RISK-001 |
| 28 | Review trend | `tools/review_trend.py` | `04493157ae1c3245ca600bf1c29069dfe3192810` | TV-007, 2026-09-26 | TV-007, ACC-TREND-001 |
| 28 | Deck renderer | `tools/slides/render_deck.py` | `b42425e9e9d2ca2b860284914b78ccbabecd38a0` | TV-008, 2026-09-26 | TV-008, ACC-DECK-001 |
| 28 | Review figures | `tools/render_review_figures.py` | `6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e` | TV-010, 2026-09-26 | TV-010, ACC-FIGS-001 |
| 28 | Unsafe audit, complexity gate, measurements | `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e`, `9214fefb76f95f0494f906607ef06428260d1c75`, `abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a` | Not yet: Log class until accreditation (TV-011 due CDR, TV-012 due CDR, TV-013 due PDR) | TV-011, TV-012, TV-013 (Validated, not accredited) |
| 26 | External `rustos` (informational until the first `release/FW-*` tag) | `/Users/robinonsay/rust/rustos`, lock §3 | pin `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (unchanged); the SRR decision 110 work item is on branch `cwht/wp-sw-licence-manifest-safety` at `2ec64c0`, not merged, not pushed | First release tag (not yet); the pin moves only when the owner merges the branch and a CR moves lock §3 | n/a |
| 25 | Firmware source (informational until the first `release/FW-*` tag) | `firmware/` | not fixed by this baseline | First release tag (not yet) | n/a |

Each row-28 blob above was compared on 2026-09-26 with the blob named in its TV record section 9 accreditation (TV-002 to TV-008, TV-010) and is equal; TV-011 to TV-013 are not accredited.

## 3. Approved changes and waivers since the previous baseline

No previous baseline exists. The changes approved at the SRR before the tag:

| CR | Title | Class | Closed | Merge SHA | CIs affected |
|---|---|---|---|---|---|
| CR-001 | CS-11 and CS-38 admit driver-construction failure arms (SRR decision 108) | II | no (Dispositioned, Approved 2026-09-26; step 2 comment in `firmware/cwht-app/src/main.rs` and step 3 complexity allowance open) | null | row 2 (07, applied at `4364ebb`), row 25 |
| CR-002 | Admit Inspection for hazard-tracing requirements that state a documentary or physical property (SRR decision 113) | I (proposed; class confirmation pending, CR-002 section 7) | no (Dispositioned, Approved 2026-09-26; steps 1 to 4 applied at `d992052`, `cd61450`, `ebe5873`, `bfea9c7`; step 5 tool change open, P4; independent review of section 4 pending, `docs/cm/deviations.md` entry 1) | null | rows 2, 7, 15, 17, 28 |

| Waiver id | Requirement or target | Approving memo or CR | Status |
|---|---|---|---|
| `docs/reviews/SRR/decision-memo.md#W1` | INSP-016 readiness condition R3 ("the design unit is Active and named in `// @design`") for the FW-B0 product only (07 §10.2) | SRR decision 115 (b), owner ruling 2026-09-26; memo §8.2, numbered W1 by memo amendment A-1 | In force for FW-B0 only; lapses for FW-B1 onward |

Requirements volatility over the interval (CM plan §5.4): not applicable to a first baseline; the R16 changes before the tag are the ruled content of the baseline itself (L1: 7 added, REQ-SYS-184 to 190, and edits under the rulings; no L1 requirement retired).

## 4. Editorial changes to controlled CIs since the previous baseline

None (first baseline).

## 5. Liens, open RIDs/RFAs and TBRs carried forward

| Item | Type (lien / RID / RFA / TBR) | Owner | Closure plan | Target review |
|---|---|---|---|---|
| RFA-SRR-001 (L-1) | Lien, RFA Routine | Robin (Claude produces the evidence) | The TBRs carried to PDR decided on Claude's evidence per each `tbr` plan | PDR readiness declaration |
| RFA-SRR-002 (L-2) | Lien, RFA Routine | Claude | Mass and envelope estimates for TPM-001 and TPM-016 | PDR readiness declaration |
| RFA-SRR-003 (L-3) | Lien, RFA Routine | Claude | Create `docs/lessons-learned.md` with the ten package section 19 entries | PDR readiness declaration |
| RFA-SRR-004 (L-4) with RID-SRR-001, 002, 004 to 014 | Lien, RFA Routine and RIDs Minor | Claude | Package-level Minor items fixed in their products and independently verified (memo §6 closure plans) | PDR readiness declaration |
| RID-SRR-003 | RID Minor (R16 requirement edit) | Claude | REQ-SYS-054 rewritten to the no-gap form at `cd61450` (decision 37) and REQ-SYS-184 added, verified by INSP-003 at `401b01d`; the citing cases updated at `ebe5873` (INSP-025 `08e5c9b`); ConOps Table 3.4-4 row 3 aligned at `bfea9c7` (INSP-002 found the decision 37 group correct) | Log state update to Verified by the RFA/RID owner before the tag |
| RFA-SRR-005 (L-5) | Lien, RFA Routine | Claude | Cross-document items due at PDR | PDR readiness declaration |
| RFA-SRR-006 (L-6) | Lien, RFA Routine | Claude | Minor findings of the 30 SRR records ("Lien: fix before PDR"), including the Minors raised in the R16 delta re-issues (for example INSP-003 finding-27 to 31, INSP-008 finding-15 to 21, INSP-009 finding-10, INSP-016 F-13 and F-14) | PDR readiness declaration |
| RFA-SRR-007 (L-7) | Lien, RFA Routine | Claude | Package-level Routine items carried from revision 3 | PDR readiness declaration |
| L1 TBRs (109) | TBR | Robin decides on Claude's evidence | Each `tbr` object, `close_by: PDR`: the 101 of memo §6, plus REQ-SYS-180, 181 and 182 (values ratified by decisions 38 to 40, kept TBR with a PDR confirmation plan in their `tbr` objects; memo §8.3 lists them as closed, see note) and REQ-SYS-184, 185, 186, 188 and 189 (added by R16 under decisions 37, 41 and 42) | PDR |
| L2 TBRs (25) | TBR | Robin decides on Claude's evidence | REQ-TX-002 to 006, 008 to 016 (14); REQ-SW-KEYER-009, 014, 017, 018, 020, 021, 022, 026, 032, 036, 039 (11); `close_by: PDR` (charter §7 allows CDR) | PDR |

Note on REQ-SYS-180 to 182: memo §8.3 records these three TBRs as closed with their ruled values; the requirement file keeps their `tbr` objects with a PDR confirmation plan (monostable timing simulation; PDR thermal analysis; counter design), and INSP-003 approved that state at `401b01d`. Carrying them as TBR with `close_by: PDR` is the conservative reading; the PDR memo closes them. A memo amendment records the difference (amendment A-2).

## 6. Releases included (product and as-built baselines only)

Not applicable to the functional baseline. The FW-B0 images of TC-SW-TOOL-001 runs 1 to 3 are development evidence (`credit: false`), not releases.

## 7. Tool accreditation state at this baseline

| Tool | Version (from `tools/toolchain.lock.md`) | Class | TV record | Status |
|---|---|---|---|---|
| venv Python with jsonschema | Python 3.13.5, jsonschema 4.26.0 | B | TV-001 | Accredited 2026-09-26 (ACC-PYJS-001, SRR decision 114) |
| `tools/traceability.py` | blob `0a867523` | B | TV-002 | Accredited (ACC-TRACE-001) |
| `tools/validate_docs.py` | blob `3aa03681` | B | TV-003 | Accredited (ACC-VALDOCS-001 with extension) |
| `tools/render_rmm.py` | blob `2386a37f` | B | TV-004 | Accredited (ACC-RMM-001) |
| `tools/render_compliance.py` | blob `d67d6b5e` | B | TV-005 | Accredited (ACC-COMPL-001) |
| `tools/render_risk.py` | blob `d38ba1dd` | B | TV-006 | Accredited (ACC-RISK-001) |
| `tools/review_trend.py` | blob `04493157` | B | TV-007 | Accredited (ACC-TREND-001) |
| `tools/slides/render_deck.py` with the Chromium headless shell 1223 | blob `b42425e9`; Chrome for Testing 148.0.7778.96 | B | TV-008 | Accredited (ACC-DECK-001) |
| git | 2.50.1 (Apple Git-155) | B | TV-009 | Accredited (ACC-GIT-001) |
| `tools/render_review_figures.py` | blob `6f3018fd` | B | TV-010 | Accredited (ACC-FIGS-001) |
| `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` | blobs `cc3aaa2a`, `9214fefb`, `abe25acb` | B | TV-011, TV-012, TV-013 | Validated, not accredited (TV-012 end-to-end check fails on the CC counting convention) |
| rustc, cargo (pinned `1.98.0`), picotool 2.3.0, rust-code-analysis-cli 0.0.25, cargo-audit 0.22.2, cargo-deny 0.20.2, cargo-llvm-cov 0.9.1, cargo-nextest 0.9.146, cargo-geiger 0.13.0, cargo-binutils 0.4.0, nightly-2026-08-24 (non-credit), kicad-cli 10.0.6, LTspice 26.0.2, OpenSCAD 2021.01, FreeCAD 1.1.3, shasum 6.04 | as lock §1 | A or B | TV pending (due PDR or CDR per CM plan §13) | Not yet validated; developer evidence only |

## 7a. Archive (SAR and closeout only; CM plan §8.4)

Not applicable at SRR.

## 8. Tag creation and verification commands

To be run by Claude on R once §0 P1 to P9 are met (unsigned annotated tag; charter §8, SRR decision 15):

```
git tag -a baseline/srr <R> -m "cwht functional baseline; decision memo docs/reviews/SRR/decision-memo.md at 0bcea39554d684ba28d6680208a523fd79a8ebba"
git cat-file -p baseline/srr          # unsigned tag: tagger, date, message, target commit
git push origin main --follow-tags
git ls-remote --tags origin baseline/srr
git ls-remote origin refs/heads/main  # remote sync observation (CM plan §10.4)
```

## 8a. Post-tag verification (fill-once, written in the post-tag record commit)

Output of `git cat-file -p baseline/srr`, verbatim:

```
pending (§8a)
```

Remote push: pending (§8a).

## 9. Approvals (fill-once, written in the post-tag record commit)

| Step | By | Date | Result |
|---|---|---|---|
| Baseline record prepared (commit R) | Claude | pending | This revision is the prepared record, not R (§0) |
| Record checked against the repository at R (every hash by `git ls-tree R -- <path>`) | independent reviewer agent | pending | |
| Baseline approved (decision memo) | Owner | 2026-09-26 | Approved with liens ("I approve of this and the SRR.") |

## 10. Corrections (append only)

| Date | Correction | Reference (CR or `Editorial:` commit) |
|---|---|---|
| none yet | | |
