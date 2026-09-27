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
commit: 779f93fd7214617a08e868cde0e5fafd9b9e848a  # SHA of the tagged commit R, `git rev-parse baseline/srr^{commit}`
tag_object: fed29c6ec11a0407bc64935c9c277a49135f4de8  # SHA of the tag object, `git rev-parse baseline/srr`
signed: false                         # false expected: no signing key is configured (charter §8; SRR decision 15 sets signing before baseline/pdr)
signature_verified: n/a               # n/a expected (unsigned annotated tag)
pushed_hash: fed29c6ec11a0407bc64935c9c277a49135f4de8  # hash returned by `git ls-remote --tags origin baseline/srr`
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

### 0.2 Status update, 2026-09-26 at `f3e8801` (integrator and CM, candidate for commit R)

Status line, 2026-09-26 (Claude, integrator and CM function): preconditions re-checked at HEAD `f3e880155e2c222803c3c05e81ea405db5165f86` after the close-out work that applies the owner's rulings of minutes `dd39332` (items 1 to 12, CR-004) and the reviewer delta re-issues that followed. This table supersedes §0.1 for current status; §0 and §0.1 stay as the record of the earlier states. §1, §2, §3, §5 and §7 are refreshed to `f3e8801` in this revision.

**Which commit is R.** This commit was prepared as the candidate for R, but it is **not R**, and `baseline/srr` must not be applied to it. P1, P2, P6, P8 and P9 are not met (table below), and the unlogged CR-004 departure below also blocks the tag (CM plan §4.4 step 1: "nothing is tagged on an unlogged departure"). Decision memo section 9 condition 2 does not allow an open Major finding to become a lien, so none of these is converted into one. R is the later commit that holds this record after those items close. In that commit Claude re-checks every §2 hash against its parent, sets §0 to "commit R", and commits with message `baseline(srr): record functional baseline` and trailer `Refs: SRR` (§4.4 step 3). `baseline_tag` in the decision memo stays `null`. Claude applies the tag on R only (§8).

Tool results at `f3e8801` (2026-09-26), each run by the integrator from the repository root:
- `tools/validate_docs.py`: exit 0, 50 of 50 pass.
- `tools/traceability.py --report-only`: exit 0, 245 requirements, 173 test cases, **0 violations**, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148). The rendered files were restored with `git checkout`.
- `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0 (65 risks, 159 candidates, 0 warnings, `register.md` current).
- `tools/render_rmm.py --check`: exit 0 (100 rows, `rmm.md` current).
- `tools/render_compliance.py --check`: exit 0 (62 rows, rendered file current).
- `python -m unittest discover -s tools/tests`: 415 run, OK.
- `git fsck --full`: exit 0 (6 dangling blobs and 1 dangling commit, no errors).
- AL-4: the 35 pins of `tools/requirements.txt` equal `.venv/bin/pip freeze`.
- The working tree is clean.

| # | Precondition | State on 2026-09-26 at `f3e8801` | Evidence | Remaining closure path and owner |
|---|---|---|---|---|
| P1 | No open Major finding in the SRR records | **Not met.** Three records hold an open Major. All three wait on owner decisions, not on author work. INSP-010 (`checklists/software-plan-07.md`, NEEDS CHANGES at `2c4f4da` on `3b45ed7`: finding-21) and INSP-018 (`checklists/software-plan-07-software-assurance.md`, NEEDS CHANGES at `ab494e9` on `3b45ed7`: finding-10) raise the same defect. 07 CS-19 and §1.2 require the main loop in the target-only `cwht-app::main`, but CS-38 as amended by CR-005 gives that loop no allowance, so gate G5 complexity fails (run 5 item B9; CR-005 section 9; TV-012 limitation 8). INSP-016 (`checklists/fw-b0-toolchain-proof.md`, NEEDS CHANGES at `c4b21f8` on `3b45ed7`: F-01) stays open because the gate exits 1 (B9 and B11, see P6). Closed since `2f619f8`: INSP-001 finding-14 (APPROVED at `511c0ca` on `b087a9f`, MOE-006 at the decision 25 (a) guard limits). The other 27 records are APPROVED | `verdict` of all 30 records in `docs/reviews/SRR/checklists/` at `f3e8801` | Owner decision B9: how CS-38 treats the CS-19 main loop of `cwht-app::main` (CR-005 section 9). The ruled route is applied by a CR to 07 and `tools/complexity_gate.py`, with a TV-012 re-validation and its independent review. Owner decision B11: the scope of the G5 Miri command (see P6). Then a TC-SW-TOOL-001 run with gate exit 0, followed by the INSP-010, INSP-018 and INSP-016 delta re-issues |
| P2 | The five Major findings that waited on the rulings are closed | **4 of 5 closed** (unchanged). INSP-016 F-01 stays Open | INSP-016 at `c4b21f8` | As P1 and P6 |
| P3 | `tools/validate_docs.py` exit 0 and the unit tests passing | **Met.** Exit 0, 50 of 50 pass. Unit tests: 415 run, OK. Both drift failures reported since `2f619f8` were cleared by re-issues: INSP-015 on `tools/toolchain.lock.md` (re-issue 3 at `26011f1`, lock blob `8ab0218a` of `eb52766`), and INSP-021 on the CR-002 blob changed by `bf654e6` (delta at `f3e8801`) | Tool runs above | None. Re-run at R |
| P4 | `tools/traceability.py` passes | **Met.** 0 violations, 2 warnings (the warnings do not fail the check). Close-out item 5 is applied. The CR-002 step 5 change to `tools/traceability.py` is blob `12de3545` at `c774851`. TV-002 run 5 is at `bf654e6`. INSP-015 re-issue 3 (`26011f1`) is the independent review that makes the ACC-TRACE-001 extension effective for blob `12de3545`. INSP-017 (`af03338`) and INSP-020 (`6257cfe`) were re-issued on the new tool blob | `traceability.py --report-only` at `f3e8801`; INSP-015 "Accreditation extensions made effective by this review" | None. The traceability report is regenerated at R (§1) |
| P5 | Every CI holds its Table 4-2 admission evidence | **Met except row 2, 07.** 07 (`a9f92d82`, last changed at `e34a27b`) is not admitted, because INSP-010 and INSP-018 are NEEDS CHANGES (P1). Met since `2f619f8`: row 5 (INSP-001 `511c0ca`); rows 9 and 53 (P3); row 17 (P4); row 27 `tools/toolchain.lock.md` (INSP-015 re-issue 3, `26011f1`). Every other CI keeps the evidence §0.1 recorded; §2a gives the per-CI state | §2a "Admission" column at `f3e8801` | As P1 |
| P6 | Hard entrance row 20 (FW-B0 toolchain proof) Met | **Not met.** Done since `2f619f8`: <br>- CR-004 applied at `5792350`: lock §3 pin `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`, `firmware/unsafe-audit.md` regenerated (blob `18ef484b`, 37 sites, 0 without SAFETY). <br>- Close-out items 2, 3 and 12 performed, recorded in the lock at `eb52766`. <br>- CR-005 applied at `e34a27b`; TV-012 run 2 at `fb22b7a`; ACC-COMPLEXITY-001 effective for `tools/complexity_gate.py` blob `9cdc9195` (INSP-015 re-issue 3). <br>- TC-SW-TOOL-001 run 5 filed at `3b45ed7`: `result: Blocked`, `credit: false`, gate exit 1 with 2 FAIL and 0 MISSING. The UF2 files are byte-identical to runs 1 to 4, so steps 11 and 12 stand on run 4. <br>The two FAIL results: <br>- B9: G5 complexity, CS-38 `cwht-app::main` CC 4 > 3. CS-17 passes (52 functions, max CC 5, mean 1.46). <br>- B11: G5 Miri. `pico2` does not compile for the aarch64-apple-darwin host (`invalid Mach-O section specifier` at `.boot_info` and `.vector_table`), so the gate command is wider than the host scope that 07 §8.1 gives Miri. <br>INSP-016 remains NEEDS CHANGES at `c4b21f8` | `docs/vv/reports/TC-SW-TOOL-001-r5.md`; `tools/toolchain.lock.md` §3 at `f3e8801`; `git -C /Users/robinonsay/rust/rustos rev-parse master` = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (ref read only, no working-tree source read) | Owner decisions B9 (as P1) and B11. Claude as tool owner applies the ruled routes. Then a full gate run with exit 0 on a clean `git archive` export of cwht and of rustos `2ec64c0`, filed as TC-SW-TOOL-001 run 6, followed by the INSP-016 delta re-issue |
| P7 | The functional baseline content carries the rulings | **Met.** `docs/requirements/l0-stakeholder/expectations.json` (blob `52b6cf5e`, `b087a9f`): 0 "owner decision pending at SRR" phrases, and MOE-006 judges the band edge at the guard limits 144.0012 and 147.9988 MHz (decision 25 (a)). INSP-001 APPROVED at `511c0ca`. `docs/design/concept.md` met (INSP-002 `1cb8b12`) | INSP-001, INSP-002 | None |
| P8 | Repository protection in place before the tag | **Not met: pending the owner's confirmation in chat.** Close-out item 6 rules the form. `main` gets a ruleset blocking force-push and deletion. `baseline/*` and `release/*` get a tag ruleset blocking update and deletion. No pull-request requirement. The minutes (last changed at `dd39332`) hold no confirmation. `gh` is not installed, so the settings were not read | Minutes `dd39332` item 6 | Owner sets the rulesets on github.com/robinonsay/cwht and confirms in chat. Claude transcribes the confirmation verbatim into the minutes |
| P9 | L1 requirement status Draft to Active at the baseline | **Not done.** 188 L1 requirements are Draft and 2 are Closed (`docs/requirements/sys/requirements.json` blob `52768afc`, unchanged since `cd61450`). INSP-003 has no status-only re-issue | Status count at `f3e8801` | Claude makes the status-only change in the commit before R, after P1 closes. INSP-003 then re-issues on the status-only delta |
| P10 | `main` pushed with the tag | **Not done.** Local `main` at `f3e8801` is 69 commits ahead of the local tracking ref `origin/main` (`7647516`). No network command was run in this check | `git rev-list --count origin/main..HEAD` = 69 | Claude pushes after the tag (§4.4 step 5, `git push origin main --follow-tags`), with the owner's go-ahead and after P8 |

**Unlogged departure for CR-004 (blocks the tag; CM plan §4.4 step 1).** CR-004 is proposed Class I. Its §6 states that the independent review of its impact assessment is required but not yet performed. The owner ruled close-out item 1 before the CR file existed, so CR-004 reached Dispositioned without passing through Assessed. This is the same departure from 05 §5.2 that `docs/cm/deviations.md` entry 1 records for CR-002. At `f3e8801` the deviations log holds entry 1 only, and CR-004 §6 names the matching entry as a cross item for the deviations log owner. Closure path, either of: (a) the deviations log owner enters CR-004 as a numbered departure before the tag, or (b) the independent review of CR-004 §4 is performed and recorded in CR-004 §6.

**Pending class confirmation.** Neither the CR-004 nor the CR-005 ruling named a class, so each CR's §7 reads "Class confirmed: Pending". CR-004 is proposed Class I. CR-005 is proposed Class II, and INSP-015 re-issue 3 cross item 3 argues that the CR-005 reasoning points to Class I, which would require an independent impact review. The owner confirms both classes. If CR-005 becomes Class I, it has the same Dispositioned-before-Assessed departure as CR-004.

**Close-out confirmations (minutes `dd39332`) at `f3e8801`:**
- Item 3: observed. `rustup 1.29.1 (d95a37b6a 2026-08-13)`, and `~/.rustup/settings.toml` holds `auto_self_update = "disable"`.
- Item 12: observed. `brew list --pinned` shows `python@3.13`.
- Item 2: performed. See the raw log `closeout-installs-2026-09-26.txt` cited in memo §13.2 and in the lock at `eb52766`.
- Item 7: CR-002 front matter reads `class: I`.
- Item 8: done. RFA-SRR-008 was raised at `4b6c96c`. It is an open item with a closure plan, not a memo §6 lien (memo amendment A-6).
- Item 9: its wording lien is in §5.
- Items 10 and 11: confirmations. The TBR count is unchanged (§5).

**RFA/RID log at `f3e8801` (last changed at `4b6c96c`):**
- RID-SRR-010 is Answered.
- RID-SRR-003 is still Open, although §5 plans its move to Verified before the tag. That move is a cross item for the RFA/RID owner and does not block the tag: the item is a Minor lien.

### 0.3 Status update, 2026-09-27 at `49104a5` (integrator and CM, candidate for commit R)

Status line, 2026-09-27 (Claude, integrator and CM function): preconditions re-checked at HEAD `49104a5d9429b7e78fbd3a33471b76976996eddb` after the owner's rulings on SRR close-out items A to C and the owner's confirmation of repository protection (`docs/reviews/SRR/minutes.md` section "Close-out decisions A to C and repository protection", `786822a`, owner statement verbatim "Done and added. I approve the other recommendations"; section "Run 4 acceptance and repository protection detail", `2ee4868`), decision memo amendment A-7 (`305a11e`), and the work and reviewer re-issues that followed (19 commits `f3e8801..49104a5`). This section supersedes §0.2 for current status and, for current values, §1, §2, §3, §5 and §7. §0, §0.1, §0.2 and §1 to §7 are kept unchanged as the record of the state at `f3e8801` and earlier. The independent baseline check `docs/reviews/SRR/baseline-check.md` (`a048fdb`, NOT READY FOR TAG at `e49a5a8`) listed defects 1 to 5; §0.3.2 states each one's state now. Its observation OBS-1 (the §0.2 "Which commit is R" list omitted P5) is answered here by listing every precondition that is not met; §0.2 is not rewritten.

**Which commit is R.** This commit is **not R**, and `baseline/srr` must not be applied to it. P1 to P4 and P6 to P9 are met. **P5 is not met for one CI, 07**: the record face of INSP-010 (`checklists/software-plan-07.md`, last changed at `c8a5143`) still reads `verdict: NEEDS CHANGES` and `assurance_verdict: NEEDS CHANGES`, although its `reviewer_verdict` is APPROVED, its finding-21 (Major) is Closed by `106bc3a` and no Major is open in it. The record says why (its "Completion criteria at the delta" and cross item X-9): 07 §2.1.1 and §10.2 forbid a record verdict of APPROVED until the paired assurance record is APPROVED, and INSP-018 read NEEDS CHANGES when INSP-010 was re-issued. INSP-018 has since been re-issued APPROVED with liens (delta 2 at `738da03` on `68a44ed`), so the gap is only the copy that X-9 names. Table 4-2 row 2 admits 07 on its `INSP-NNN` record, and SRR decision 1 approves each plan only when its record is APPROVED with no open Major, so the integrator does not treat a record that reads NEEDS CHANGES as admission evidence, and does not edit a reviewer's record (charter §2). Decision memo §9 condition 2 does not allow the gap to become a lien. `baseline_tag` in the decision memo stays `null`, and Claude applies the tag on R only (§8).

**Gaps to R, with owner.**
1. INSP-010 re-issue by copy (its cross item X-9): the INSP-010 reviewer, as a new invocation, reads INSP-018 at HEAD (`assurance_verdict: APPROVED`, delta 2 `738da03`), copies it into `assurance_verdict`, sets `verdict: APPROVED` (with its liens, including finding-22), re-checks that every `product_files` blob equals `git rev-parse HEAD:<path>` (at `49104a5`: 07 `bfe05f43`, CR-001 `0f4cca4c`, CR-005 `9b0129ef`, all equal), and commits the record alone. No further product review is needed (X-9).
2. Then Claude re-runs the TOOLS set and `git fsck --full`, re-takes every §0.3.3 hash against the parent of R, sets the record to "commit R", and commits it alone with message `baseline(srr): record functional baseline` and trailer `Refs: SRR` (CM plan §4.4 step 3).
3. The independent baseline check is repeated at R, with every hash taken by `git ls-tree R -- <path>` (CM plan §4.4 step 4; §9 row 2; `baseline-check.md` OBS-2). Then Claude applies the tag with the §8 commands and pushes (P10).

#### 0.3.1 Tool results at `49104a5` (2026-09-27, run by the integrator from the repository root)

| Check | Command | Result |
|---|---|---|
| Document validation | `.venv/bin/python tools/validate_docs.py` | exit 0, 50 passed, 0 failed, 50 checked |
| Traceability | `.venv/bin/python tools/traceability.py --report-only`, then `git checkout -- docs/vv/traceability-report.md docs/vv/traceability.json` | exit 0; 245 requirements, 173 test cases, **0 violations**, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, Active SYS requirements that name no receiving L2 module; the V6 reviewer confirms or corrects them, 02 §2.3 T-18). Rendered files restored |
| Risk register | `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | exit 0; 65 risks, 159 candidates, 0 warnings, `register.md` current |
| RMM | `.venv/bin/python tools/render_rmm.py --check` | exit 0; 100 rows (FC 75, T 17, NA 8), `rmm.md` current |
| Compliance matrix | `.venv/bin/python tools/render_compliance.py --check` | exit 0; 62 rows (FC 49, T 4, NA 9), validation passed, rendered file current |
| Tool unit tests | `.venv/bin/python -m unittest discover -s tools/tests` | exit 0; 424 tests run, OK |
| Object store | `git fsck --full` | exit 0; 6 dangling blobs and 4 dangling commits, no errors |
| AL-4 venv pins | `tools/requirements.txt` (comments and blank lines removed, sorted) against `.venv/bin/pip freeze` (sorted) | identical, 35 pins |
| Working tree | `git status --short` after the runs | clean |
| Tracked files | `git ls-files \| wc -l` | 1177 (1147 at `f3e8801`) |

#### 0.3.2 Preconditions at `49104a5`

| # | Precondition | State on 2026-09-27 at `49104a5` | Evidence |
|---|---|---|---|
| P1 | No open Major finding in the SRR records (memo §9 condition 2; CM plan §4.4 step 1) | **Met.** None of the 30 records in `docs/reviews/SRR/checklists/` holds an open Major; all 30 have `reviewer_verdict: APPROVED` and `readiness_met: true`. Closed since `f3e8801`: INSP-010 finding-21 (Verified closed by `106bc3a`, CR-005 amendment 1, close-out item A; INSP-010 delta `c8a5143`); INSP-018 finding-10 (delta 2 `738da03`, APPROVED with liens finding-8, finding-9, finding-11); INSP-016 F-01 (delta 2 `6a969b9`, APPROVED with liens F-13, F-16, F-17 and L-016-6). 29 records read `verdict: APPROVED`; INSP-010 reads NEEDS CHANGES only by the pairing copy (P5) | Front matter of the 30 records at `49104a5`; `baseline-check.md` defect 1 cleared |
| P2 | The five Major findings that waited on the rulings are closed (memo §9 condition 2) | **Met, 5 of 5.** INSP-016 F-01 Closed (Verified) on TC-SW-TOOL-001 run 6 and the reviewer's reproduction (`6a969b9`); the other four as in §0.2 | INSP-016 delta 2 verdict line; memo §13.3 |
| P3 | `tools/validate_docs.py` exit 0 and the unit tests passing (Table 4-2 rows 9 and 53) | **Met.** 50 of 50; 424 tests OK. The INSP-021 drift on the CR-002 blob (`c007177f`, changed by `8b86c16`) was cleared by the INSP-021 close-out item C delta (`49104a5`) | §0.3.1 |
| P4 | `tools/traceability.py` passes | **Met.** 0 violations, 2 warnings; tool blob `12de3545` unchanged since `c774851` (ACC-TRACE-001 extension, effective on INSP-015 re-issue 3 `26011f1`) | §0.3.1 |
| P5 | Every CI holds its Table 4-2 admission evidence | **Not met for row 2, 07 only.** 07 blob `bfe05f43` (revision A.7, `106bc3a`): INSP-018 is APPROVED with liens on it (`738da03`, product commit `68a44ed`), INSP-010 `reviewer_verdict: APPROVED` on it (`c8a5143`) but record `verdict: NEEDS CHANGES` pending the X-9 copy (gap 1 above). Row 27 `tools/toolchain.lock.md` (blob `04819139`, changed at `495a0c3`) is admitted by INSP-015 re-issue 4 (`0359409`, APPROVED with liens F-07 to F-13; its `product_files` name `04819139`). Row 7 (P9 status change) is admitted by INSP-003 P9 status delta (`08922d9`). Every other CI keeps the evidence of §0.2 and §2a, with its blob unchanged (§0.3.3) | §0.3.3 "Admission" column |
| P6 | Hard entrance row 20 (FW-B0 toolchain proof) Met | **Met.** TC-SW-TOOL-001 run 6 (`68a44ed`, `docs/vv/reports/TC-SW-TOOL-001-r6.md` blob `8d12b383`): `result: Pass`, `credit: false`, `tools/sw_gate.sh` exit 0 in both modes on clean exports of cwht `bb2485e` and rustos `2ec64c0` (G0 on the run 5 D20 local clone at `2ec64c0`), no download. B9 closed by close-out item A (CR-005 amendment 1 `106bc3a`, `tools/complexity_gate.py` blob `ddf10798`, TV-012 run 3 `0da559a`); B11 closed by close-out item B (`tools/sw_gate.sh` `495a0c3`, G5 Miri `-p api`). Steps 11 and 12 stand on run 4 (byte-identical UF2), accepted by the owner (minutes `2ee4868`). INSP-016 APPROVED with liens at `6a969b9` | Run 6 report; INSP-016 delta 2; memo §13.3 |
| P7 | The functional baseline content carries the rulings | **Met.** No change since §0.2 to `expectations.json` (`52b6cf5e`) or `concept.md` (`6f026f92`); 07 carries close-out item A (A.7); the lock carries close-out item B (`495a0c3`) | §0.3.3 |
| P8 | Repository protection in place before the tag (SRR decision 15; close-out item 6) | **Met.** The owner confirms that the protection of close-out item 6 is in place (minutes `786822a`, "Recorded": "The owner confirms that the repository protection of close-out item 6 is in place (precondition P8)") and keeps it as set (minutes `2ee4868`: "I think the github settings are fine and yes I approve the results"). The presenter's anonymous GitHub REST API check (2026-09-27) shows branch `main` `protected: true`; rulesets are not visible without authentication, so the `baseline/*` and `release/*` tag rule rests on the owner's confirmation (memo §13.3) | Minutes `786822a`, `2ee4868`; memo A-7 |
| P9 | L1 requirement status Draft to Active at the baseline | **Met.** `docs/requirements/sys/requirements.json` blob `f128235e` (`61a3cb7`): 190 items, 188 Active, 2 Closed (retired), 0 Draft. INSP-003 P9 status delta (`08922d9`, product `61a3cb7`) verified the change as status-only, APPROVED with liens, readiness met | Status count at `49104a5`; INSP-003 |
| P10 | `main` pushed with the tag (charter §8; CM plan §4.4 step 5) | **Not done (post-tag step).** Local `main` at `49104a5` is 88 commits ahead of the local tracking ref `origin/main` (`7647516`); no network command was run in this check. Claude pushes after the tag with `git push origin main --follow-tags` (§8), P8 being met | `git rev-list --count origin/main..HEAD` = 88 |

**CR-004 departure and the other Dispositioned-before-Assessed departures (`baseline-check.md` defect 3).** **Closed.** Under close-out item C, `docs/cm/deviations.md` logs CR-004 and CR-005 as entries 2 and 3 and brings CR-002 (entry 1) under RFA-SRR-008 by correction entry 4 (`31272e0`). The independent Class I impact reviews of CR-002, CR-004 and CR-005 (as amended under item A) are recorded in each CR's section 6 at `8b86c16` by a separate reviewer agent that authored none of the three CRs; each concurs Class I with comments, and no finding changes the owner's basis, so no CR returns to Submitted. Entries 1 to 4 are closed at `bb2485e`. The deviations log holds no open entry, so CM plan §4.4 step 1 ("nothing is tagged on an unlogged departure") no longer blocks the tag.

**RFA/RID log at `49104a5`** (`docs/reviews/SRR/rfa-rid-log.json` blob `906d4a19`, last changed at `305a11e`): RFA-SRR-008 Answered (2026-09-27, on the CR-002 impact review; Verified waits for the owner, 01 §10.3; not a memo §6 lien, does not block the tag). RID-SRR-010 Answered. The other 20 items (RID-SRR-001 to 009, 011 to 014; RFA-SRR-001 to 007) are Open liens with their memo §6 closure plans, due PDR. RID-SRR-003 is still Open; its move to Verified is a cross item for the RFA/RID owner and does not block the tag.

#### 0.3.3 Configuration items at `49104a5`

Each hash is `git rev-parse 49104a5:<path>` (a blob for a file, a tree for a directory). `49104a5` is the parent of this record commit. "Changed since `f3e8801`" names the commit that changed the item; every other hash equals the §2 value. Because this commit is not R, every hash is re-taken against the parent of R.

| Row (Table 4-1) | CI | Path | Hash at `49104a5` | Changed since `f3e8801` | Peer review record | Admission (Table 4-2) |
|---|---|---|---|---|---|---|
| 1 | Process charter | `docs/process/00-charter.md` | `41575d218c2228825704ce0b080a967c890fe43f` | no | none (owner direction) | Met (SRR decision 1) |
| 2 | 01 | `docs/process/01-lifecycle-and-reviews.md` | `eabbbd57953c84164e848f36dc327542ac015c00` | no | INSP-019 | Met: APPROVED (`119cb36`) |
| 2 | 02 | `docs/process/02-requirements-and-traceability.md` | `fcdc544555477f0115535348f8ce388453a9034f` | no | INSP-020 | Met: APPROVED (`6257cfe`) |
| 2 | 04 | `docs/process/04-verification-and-validation.md` | `0b197bba692237ed9860ba49c4422f12fa8512dc` | no | INSP-021 | Met: APPROVED with liens (close-out item C delta `49104a5` at `08922d9`) |
| 2 | 05 | `docs/process/05-configuration-and-data-management.md` | `f8de2081f7542ed0bbe47897d8b63e845b8c3114` | no | INSP-006 with INSP-030 | Met: APPROVED (`d8df6a9`, `ff0a610`) |
| 2 | 06 | `docs/process/06-risk-and-decision-analysis.md` | `7a92d21f24a1733d70ae083576e708274bfd1a6d` | no | INSP-007 | Met: APPROVED with liens (`a50aba8`) |
| 2 | 07 (revision A.7) | `docs/process/07-software-engineering-plan.md` | `bfe05f4327e79fa15c24d2cf8c14249804f946a8` | `106bc3a` (CR-005 amendment 1, close-out item A) | INSP-010 with INSP-018 | **Not met (gap 1).** INSP-018 APPROVED with liens (`738da03`); INSP-010 `reviewer_verdict` APPROVED, record `verdict` NEEDS CHANGES pending the X-9 copy (`c8a5143`) |
| 2 | 08 | `docs/process/08-agent-briefing.md` | `01a36bac8d5f133dadd5b384f92f95f225371663` | no | INSP-022 | Met: APPROVED (`119cb36`) |
| 2 | Process index | `docs/process/README.md` | `3664073bc2563f604fb7b1c639a2689a20fb0e6a` | no | none (§7.4 interim check) | Check at R |
| 2 | SEMP | `docs/plan/semp.md` | `ccfdecf98a6e2dc1371eb057e6aa37903b672de1` | no | INSP-005 | Met: APPROVED with liens (`1e56df4`) |
| 2 | Schedule | `docs/plan/schedule.md` | `82b44894a7613459e41d6827f181d13172390539` | no | INSP-023 | Met: APPROVED (`2f619f8`) |
| 2 | Cost estimate | `docs/plan/cost-estimate.md` | `0dda83cbd5ada9474562cc1741df67a31e1a7ffb` | no | INSP-023 | Met: APPROVED |
| 3 | Classification record | `docs/process/03-software-classification-and-rmm.md` | `ed270f443e2ab648480017df8ad3d0221400cf4c` | no | INSP-009 with INSP-017 | Met: APPROVED (`b54064b`); APPROVED with liens (`af03338`) |
| 3 | RMM | `docs/process/rmm.json` | `e326ddd1b7296d7d7fe172be6f33535cee3192d7` | no | INSP-009, INSP-017 | Met; `render_rmm.py --check` exit 0 |
| 3 | RMM rendering | `docs/process/rmm.md` | `54e351f4df231d1a1e74e6eef4bd07db9a408fa0` | no | rendered | Met |
| 3 | Compliance matrix | `docs/process/se-compliance-matrix.json` | `790d256214e07beb736f2f414a8eaf384ecf2440` | no | INSP-024 | Met: APPROVED; `render_compliance.py --check` exit 0 |
| 3 | Compliance rendering | `docs/process/se-compliance-matrix.md` | `09426930b27e3b51182ab28086c6c73000f274d9` | no | rendered | Met |
| 5 | Stakeholder expectations | `docs/requirements/l0-stakeholder/expectations.json` | `52b6cf5e8f7b4b9fec7ed4c6aa68313967d7104c` | no | INSP-001 | Met: APPROVED (`511c0ca`) |
| 5 | Expectations rendering | `docs/requirements/l0-stakeholder/expectations.md` | `f460c1fb300a29533cf7abdd19ae768130299a5f` | no | rendered | Met |
| 6 | ConOps (directory) | `docs/conops/` | tree `0b04e66c5bed4ea55df42c65ae91fc1e3189b167` | no | INSP-002 | Met: APPROVED (`1cb8b12`) |
| 6 | ConOps revision 3 | `docs/conops/conops.md` | `6c3fbb2be814f5d0a5b2979968e309f6a846445a` | no | INSP-002 | Met |
| 6 | ConOps figures | `docs/conops/figures/conops-context.mmd`, `.png`; `conops-modes.mmd`, `.png` | `55ebae2e15589bf9951456dc04400b7ccb96ea27`, `2e4647f81c61a1d2df05637efa3ee3d71a506e09`; `829a46f800db84ae5196cf3946d4376eb813fc0f`, `b3a08b6770c7c019b67e4b19cd2cdcbba3e8ce6c` | no | INSP-002 | Met |
| 7 | L1 requirements (directory) | `docs/requirements/sys/` | tree `86ea40ebafc0b5de4c773acf78d91b6a55a1efc4` | `61a3cb7` (P9) | INSP-003 | Met: APPROVED with liens (P9 status delta `08922d9`) |
| 7 | L1 requirements (190: 188 Active, 2 Closed retired) | `docs/requirements/sys/requirements.json` | `f128235ee109cdc325e37c32000ebf9d6027454d` | `61a3cb7` (P9, status only) | INSP-003 | Met |
| 7 | L1 rendering | `docs/requirements/sys/requirements.md` | `553f7f48aaaea5934f73e59a64d0e0d3b9a7ba5d` | `61a3cb7` | rendered | Met |
| 9 | Schemas (the 11 files of §2a row 9, same order) | `docs/design/allocation.schema.json`; `docs/plan/measurements.schema.json`; `docs/plan/tpm.schema.json`; `docs/process/rmm.schema.json`; `docs/process/se-compliance-matrix.schema.json`; `docs/requirements/l0-stakeholder/schema.json`; `docs/requirements/schema.json`; `docs/risk/schema.json`; `docs/safety/schema.json`; `docs/templates/rfa-rid-log.schema.json`; `docs/test_cases/schema.json` | `c17e011ba352839fd8c816a9ef5daf978757dfe2`; `c30b7f3e7466bf4e4474afd031c2c9c91db42be8`; `df3bd894ffec8841245617d0b0c7be6457ddd632`; `ae2f87dd97c7dc9b0e9e4fd5eccbdf35db69e13b`; `ef156b0fcfaaca3b44543154a454b0a965e72a2c`; `d0a79903f8952ed75cf421ff2a73d068f6a32b29`; `ca049dfb0a4480f8de889fe112add0a2e893915f`; `473cd797db582ae2dc4ed14fa83213c3bf2a6d09`; `e96accaad02dcb33a3dfdbcc8da11fd4f28bed84`; `38898b0c260c3292fbc65c59d632790ad4e650f7`; `d4b70163ca13c6263147a49a39f602b88a81517a` | no | none | Met: validate 50 of 50, 424 tests OK (P3); TV-001, TV-003 Accredited |
| 17 | TC-SYS cases (113) | `docs/test_cases/sys/test_cases.json` | `a18824aaf62d5139cdc558e52174726bd5d2f673` | no | INSP-025 | Met: APPROVED (`08e5c9b`); 0 violations |
| 17 | TC-SYS rendering | `docs/test_cases/sys/test_cases.md` | `45e7ca5101b2def1a1f9f7d7ea5e2aa3e851e21a` | no | rendered | Met |
| 27 | Toolchain lock | `tools/toolchain.lock.md` | `04819139c8a10cc6a970d7d08684f7487bf968bb` | `495a0c3` (close-out item B: dated `tools/sw_gate.sh` row entry, Miri scope evidence) | INSP-015 | Met: APPROVED with liens F-07 to F-13 (re-issue 4 `0359409`, which names blob `04819139`); rustos pin `2ec64c0` (CR-004) unchanged |
| 27 | Venv pins | `tools/requirements.txt` | `ef9820618aafd7fb8d62a24fda4f029a3ffdeb62` | no | none | Met: AL-4, 35 pins equal |
| 51 | Technology assessment | `docs/plan/technology-assessment.md` | `d46abde01adf320630dc317d0a80aa6f197181e5` | no | INSP-014 | Met: APPROVED |
| 52 | Design concept | `docs/design/concept.md` | `6f026f92ae4f090dc85e94e554a0845514adbce9` | no | INSP-002 | Met: APPROVED (`1cb8b12`) |
| 53 | Templates and checklists (22 entries: 21 files plus the row 9 schema) | `docs/templates/` | tree `e94d4ce59c8b62879a1627950eca953281415c03` | no | none | Met (P3) |

Informational items (§2b rows 14, 15, 8, 17, 4), all unchanged since `f3e8801`: `docs/risk/register.json` `0c25c0c5b6ca801b02e47c29c19bb8ed44aa5c79`, `docs/risk/register.md` `a3a983e5cdf7e769666fab26d5f2e7f3b373db1f`; `docs/safety/hazard-analysis.md` `52c8ce16856499afc1b701e1ddb103788fcb1af9`, `docs/safety/hazards.json` `81cacde47d4f2066ecac3947f3acf65e646b1ad0`; `docs/requirements/tx/requirements.json` `8b9d81e8d0f8f605427ef5876adc0f891585a569` (16 Draft), `docs/requirements/sw/sw-keyer/requirements.json` `f9141160c4d92ad80ae91144c2499b22292d4b16` (39 Draft); `docs/test_cases/tx/test_cases.json` `3528d0626e450345a79c9865780db0938b8cff05`, `docs/test_cases/sw-keyer/test_cases.json` `2716ca3f53d349c84f2a4a717a3b7daa1566792f`, `docs/test_cases/sw-tool/test_cases.json` `fee1e7246af59d5e8a43ed1b9cdf483854053fdc`; `docs/requirements/l0-stakeholder/stakeholder-inputs.md` `362250fbaa62c937ffc391477ff9c71f1d41514c`.

Controlled items outside the baseline set (§2c, row 28, 26 and 25) at `49104a5`:

| Row | CI | Path or pin | Hash at `49104a5` | Changed since `f3e8801` | TV record and accreditation |
|---|---|---|---|---|---|
| 28 | Traceability checker | `tools/traceability.py` | `12de354531f27afd59e9a18798516d218821d6c0` | no | TV-002, ACC-TRACE-001 extended to this blob (TV-002 run 5 `bf654e6`; effective on INSP-015 re-issue 3 `26011f1`) |
| 28 | Document validator | `tools/validate_docs.py` | `3aa0368147b9af3e6e1546f808afb7aedf7f2226` | no | TV-003, ACC-VALDOCS-001 |
| 28 | RMM renderer | `tools/render_rmm.py` | `2386a37fbfb9d7d06c333e0f00981b6fc67e1f27` | no | TV-004, ACC-RMM-001 |
| 28 | Compliance renderer | `tools/render_compliance.py` | `d67d6b5e601a64b013b64e8de3cd0fc3deb96ffa` | no | TV-005, ACC-COMPL-001 |
| 28 | Risk renderer | `tools/render_risk.py` | `d38ba1dd25ac8ef5ecb04ce5b1ea907bb60eee8c` | no | TV-006, ACC-RISK-001 |
| 28 | Review trend | `tools/review_trend.py` | `04493157ae1c3245ca600bf1c29069dfe3192810` | no | TV-007, ACC-TREND-001 |
| 28 | Deck renderer | `tools/slides/render_deck.py` | `b42425e9e9d2ca2b860284914b78ccbabecd38a0` | no | TV-008, ACC-DECK-001 |
| 28 | Review figures | `tools/render_review_figures.py` | `6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e` | no | TV-010, ACC-FIGS-001 |
| 28 | Complexity gate | `tools/complexity_gate.py` | `ddf1079847046d52a268e48a6c82180bd84cca6f` | `106bc3a` (CR-005 amendment 1, close-out item A) | TV-012, ACC-COMPLEXITY-001 extended to this blob by TV-012 run 3 (`0da559a`, record blob `bd99a11d`) and effective from 2026-09-27 on INSP-015 re-issue 4 (`0359409`); liens F-11, F-13. Earlier accredited blob `9cdc9195` |
| 28 | Unsafe audit, measurements | `tools/unsafe_audit.py`, `tools/measurements.py` | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e`, `abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a` | no | TV-011, TV-013: Validated, not accredited (due CDR, PDR) |
| 28 | Software gate | `tools/sw_gate.sh` | `29a37127312e242bce2aa8f41602e3bcd4360f2f` | `495a0c3` (close-out item B, G5 Miri `-p api`) | No TV record yet (due CDR); the change is recorded in the lock §1.1 row and checked by INSP-015 re-issue 4 and INSP-016 delta 2 |
| 26 | External rustos | lock §3 | pin `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (CR-004, `5792350`) | no | `git -C /Users/robinonsay/rust/rustos rev-parse master` = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` at this check (ref read only; the owner's rustos working tree was neither read nor modified) |
| 25 | Firmware source | `firmware/` | tree `de1c87cb4190121b965dcc0ae59f3e590421fee9`; `firmware/unsafe-audit.md` `18ef484bf050797e9493d68071efdc0259d423a6` | no | informational until the first `release/FW-*` tag |

Records cited by this revision, at `49104a5`: decision memo `4c09ef559326951fd9fd2a269e03ec7709aa1441` (A-7 at `305a11e`; signing commit `0bcea39` unchanged); minutes `5a5f4ed611f3aeb86d47a610a65ee6d4e9384518` (`786822a`, `2ee4868`); RFA/RID log `906d4a19e188285e23e942201e9a01f08aca3ad7`; deviations log `bcb91b5c9a267ead07c910e5daf503fc0808ee64` (`31272e0`, `bb2485e`); TC-SW-TOOL-001 run 6 `8d12b38333b4ae863dc8689eed39658dcc276e68`.

**Tool accreditation state (supersedes §7 for two rows).** TV-001 and TV-003 to TV-010: Accredited, blobs unchanged. TV-002: Accredited, ACC-TRACE-001 at blob `12de3545` (unchanged since §0.2). TV-012: Accredited, ACC-COMPLEXITY-001 at blob `ddf10798`, purposes 1 to 5 with purpose 3 as amended (CS-19 main-loop allowance of `cwht-app::main`), effective 2026-09-27 on INSP-015 re-issue 4 (the only accreditation extended by that review). The TV-012 status line and section 8 still read "pending, the INSP-015 delta" (INSP-015 re-issue 4 cross item 1, a tool-owner transcription); the accreditation stands on the review record. `tools/sw_gate.sh` (blob `29a37127`) has no TV record (due CDR). TV-011 and TV-013 are not accredited.

#### 0.3.4 Change requests at `49104a5` (supersedes the §3 CR table for current state)

| CR | Class | State | Blob at `49104a5` | Change since §0.2 |
|---|---|---|---|---|
| CR-001 | II (decision 108) | Dispositioned, Approved 2026-09-26; not closed (`merge_sha: null`). Steps 1 to 3 applied (`4364ebb`, `93d019b`, CR-005 `e34a27b`); the step table still shows steps 2 and 3 open (cross item for the CR owner; CR-005 impact review finding-2) | `0f4cca4cb1e2562af05a7c435f41e6ba82d17f26` | none |
| CR-002 | I (close-out item 7) | Dispositioned, Approved 2026-09-26; not closed. Steps 1 to 5 applied. Independent Class I impact review recorded in section 6 at `8b86c16`: concur with comments, findings 1 to 3 Minor (liens due PDR). Deviations entries 1 and 4 closed at `bb2485e` | `c007177f7c3a50bc9ad2f0e4fcdeb798f530c045` | impact review (`8b86c16`) |
| CR-003 | not yet proposed | Number reserved for the enclosure CR (REQ-SYS-109 solution-neutral, REQ-SYS-124 amendment; SI-037), raised after `baseline/srr` is tagged so the tag carries exactly what was approved at SRR. **Not part of this baseline** | n/a | none |
| CR-004 | I (confirmed by the owner under close-out item C, `786822a`; recorded at `31272e0`) | Dispositioned, Approved 2026-09-26; not closed. Applied at `5792350`. Independent Class I impact review at `8b86c16`: concur with comments, findings 1 and 2 Minor (liens due PDR). Deviations entry 2 closed at `bb2485e` | `b9fc951091280e1c4e30c5fc0b81a1aae7483aa0` | class confirmed; impact review |
| CR-005 | I (confirmed by the owner under close-out item C; recorded at `106bc3a`) | Dispositioned, Approved 2026-09-26, amended 2026-09-27 under close-out item A (amendment 1 at `106bc3a`: +1 CS-38 allowance for all three CS-19 loops; 07 A.7; `tools/complexity_gate.py` `ddf10798`; TV-012 run 3 `0da559a`); not closed. Independent Class I impact review of the amended CR at `8b86c16`: concur with comments, findings 1 and 2 Minor (liens due PDR). Deviations entry 3 closed at `bb2485e`. The CR-005 section 9 owner decision (B9) is resolved by item A | `9b0129efd09e75170a4542d011ff6b1298ad2820` | amendment 1; class confirmed; impact review |

Deviations (`docs/cm/deviations.md`): entries 1 to 4 all Closed at `bb2485e` (§0.3.2); no open entry. Waiver W1 (memo §8.2, FW-B0 readiness R3) stays in force for FW-B0 only. Requirements volatility: no L1 requirement was added, retired or reworded since `f3e8801`; the only L1 change is the P9 status change at `61a3cb7`.

#### 0.3.5 Liens and TBRs carried forward (adds to §5; §5 rows stand unless stated)

| Item | Type | Owner | Closure plan | Due |
|---|---|---|---|---|
| Close-out item B: `pico2` host-compilable for G5 Miri (INSP-016 lien L-016-6; memo §13.3) | Lien (added after signing, A-7) | Robin (rustos maintainer), then the `tools/sw_gate.sh` maintainer (Claude) | `cfg_attr` on the two target-only `link_section` attributes, pin CR, `-p pico2` returned to G5 Miri with a known-answer run | FW-B1 |
| RFA-SRR-008 | RFA Routine, Answered | Owner verifies (01 §10.3) | Answered 2026-09-27 on the CR-002 impact review (`8b86c16`, `bb2485e`); the owner's statement moves it to Verified | PDR readiness declaration (does not block the tag) |
| CR impact review findings | Minor liens | CR owners (Claude) | CR-002 finding-1 to 3, CR-004 finding-1 and 2, CR-005 finding-1 and 2 (memo §13.3 table) | PDR |
| INSP-016 F-13, F-16, F-17 | Minor liens | Claude | F-17: owner authorization of run 6 section 12 | PDR |
| INSP-018 finding-8, 9, 11; INSP-010 finding-22 | Minor liens | 07 author (Claude) | As each record states | PDR |
| INSP-015 F-07 to F-13 (F-12 scope widened by re-issue 4) and its cross item 1 (TV-012 section 8 transcription) | Minor liens | Tool owner (Claude) | As INSP-015 re-issue 4 states | PDR |
| `baseline-check.md` OBS-1 | Minor (record) | Baseline record author | Answered by §0.3 (every unmet precondition listed); §0.2 kept as history | done in this revision |
| RID-SRR-003 log state | RID Minor | RFA/RID owner | Move to Verified (§5 row) | before the tag (cross item; does not block) |
| L1 TBRs | TBR | Robin on Claude's evidence | **109**, every one `close_by: PDR` (recounted at `49104a5`, unchanged; the P9 change touched status only) | PDR |
| L2 TBRs | TBR | Robin on Claude's evidence | **25**: REQ-TX 14, REQ-SW-KEYER 11 (recounted at `49104a5`, unchanged) | PDR |

### 0.4 Record status, 2026-09-27 at `824a362`: commit R

Status line, 2026-09-27 (Claude, integrator and CM function): preconditions re-checked at HEAD `824a3624980db067853e2438ac4f56b53cf554ad`, the parent of this commit, after the INSP-010 X-9 copy delta (`824a362`). That delta closes the only gap that section 0.3 and the independent baseline check 2 (`docs/reviews/SRR/baseline-check.md`, `61ab1d7`, NOT READY FOR TAG on P5 only) left open. This section supersedes §0.3 for current status and, for current values, §1, §2, §3, §5 and §7. §0, §0.1, §0.2, §0.3 and §1 to §7 are kept unchanged as the record of the earlier states.

**This commit is R.** P1 to P9 are met (§0.4.2). P10 is pending: it is the post-tag step. This commit changes one file only, this record; every hash in §0.4.3 is `git rev-parse 824a362:<path>`, so it equals the blob or tree at R. Claude applies `baseline/srr` to this commit with the §8 commands only after the independent baseline check is repeated at R, with every hash taken by `git ls-tree R -- <path>` (CM plan §4.4 step 4; §9 row 2), and reads READY FOR TAG. Claude then pushes (P10). `baseline_tag` in the decision memo stays `null` until Claude tags. The fill-once fields of the front matter, §8a and §9 are written in the post-tag record commit (CM plan §4.4 step 6).

#### 0.4.1 Tool results at `824a362` (2026-09-27, run by the integrator from the repository root)

| Check | Command | Result |
|---|---|---|
| Document validation | `.venv/bin/python tools/validate_docs.py` | exit 0, 50 passed, 0 failed, 50 checked |
| Traceability | `.venv/bin/python tools/traceability.py --report-only`, then `git checkout -- docs/vv/traceability-report.md docs/vv/traceability.json` | exit 0; 245 requirements, 173 test cases, **0 violations**, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, as recorded in §0.3.1). Rendered files restored |
| Risk register | `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | exit 0; 65 risks, 159 candidates, 0 warnings, `register.md` current |
| RMM | `.venv/bin/python tools/render_rmm.py --check` | exit 0; 100 rows (FC 75, T 17, NA 8), `rmm.md` current |
| Compliance matrix | `.venv/bin/python tools/render_compliance.py --check` | exit 0; 62 rows (FC 49, T 4, NA 9), validation passed, rendered file current |
| Tool unit tests | `.venv/bin/python -m unittest discover -s tools/tests` | exit 0; 424 tests run, OK |
| Object store | `git fsck --full` | exit 0; 6 dangling blobs and 4 dangling commits, no errors |
| AL-4 venv pins | `tools/requirements.txt` (comments and blank lines removed, sorted) against `.venv/bin/pip freeze` (sorted) | identical, 35 pins |
| Working tree | `git status --short` after the runs | clean |
| Tracked files | `git ls-files \| wc -l` | 1177 (unchanged since `49104a5`) |
| Change since §0.3 | `git diff --stat 49104a5 824a362` | 3 files, all records: `baseline-record.md` (§0.3, `4c4e0d1`), `baseline-check.md` (check 2, `61ab1d7`), `checklists/software-plan-07.md` (INSP-010 X-9 copy delta, `824a362`). No CI, informational item or controlled tool changed |

#### 0.4.2 Preconditions at `824a362`

| # | Precondition | State on 2026-09-27 at `824a362` | Evidence |
|---|---|---|---|
| P1 | No open Major finding in the SRR records (memo §9 condition 2; CM plan §4.4 step 1) | **Met.** None of the 30 records in `docs/reviews/SRR/checklists/` holds an open Major. All 30 read `verdict: APPROVED`, `reviewer_verdict: APPROVED` and `readiness_met: true` | Front matter of the 30 records at `824a362`; baseline check 2 D11 for the Major rows |
| P2 | The five Major findings that waited on the rulings are closed (memo §9 condition 2) | **Met, 5 of 5**, unchanged since §0.3.2 | INSP-016 delta 2 (`6a969b9`); memo §13.3 |
| P3 | `tools/validate_docs.py` exit 0 and the unit tests passing (Table 4-2 rows 9 and 53) | **Met.** 50 of 50; 424 tests OK. The record drift rule passes for every record, including INSP-010 after its X-9 copy delta | §0.4.1 |
| P4 | `tools/traceability.py` passes | **Met.** 0 violations, 2 warnings; tool blob `12de3545` unchanged | §0.4.1 |
| P5 | Every CI holds its Table 4-2 admission evidence | **Met.** The row 2 gap for 07 is closed by the INSP-010 X-9 copy delta (`824a362`, record blob `e7b16d25`): `assurance_verdict: APPROVED` copied from INSP-018 at `738da03` (record unchanged since, blob `9076d5a2`, `verdict: APPROVED` with liens finding-8, finding-9, finding-11; finding-10 Verified closed by `106bc3a`), `reviewer_verdict: APPROVED` and `readiness_met: true` unchanged, `verdict: APPROVED` with liens finding-14 to finding-18, finding-20, finding-22. The integrator re-checked all seven INSP-010 `product_files` against `git rev-parse 824a362:<path>`: 07 `bfe05f43`, CR-001 `0f4cca4c`, CR-005 `9b0129ef`, `docs/plan/measurements.json` `5e2d1755`, `docs/plan/measurements.schema.json` `c30b7f3e`, `tools/tests/fixtures/measurements/valid.json` `3938cd57` and `invalid.json` `15231171`, all equal (the X-9 delta re-checked the first three; the other four are checked here). Both INSP-018 `product_files` (07 `bfe05f43`, `measurements.json` `5e2d1755`) are equal. Every other CI keeps the evidence of §0.3.3 with its blob unchanged | §0.4.3 "Admission" column |
| P6 | Hard entrance row 20 (FW-B0 toolchain proof) Met | **Met**, unchanged since §0.3.2: TC-SW-TOOL-001 run 6 (`8d12b383`, `result: Pass`, gate exit 0); INSP-016 APPROVED with liens (`6a969b9`) | Run 6 report; INSP-016 delta 2 |
| P7 | The functional baseline content carries the rulings | **Met**, unchanged since §0.3.2 (no CI changed since `49104a5`) | §0.4.3 |
| P8 | Repository protection in place before the tag (SRR decision 15; close-out item 6) | **Met**, unchanged since §0.3.2: the owner's confirmation is transcribed in the minutes (`786822a`, `2ee4868`; minutes blob `5a5f4ed6` unchanged) | Minutes |
| P9 | L1 requirement status Draft to Active at the baseline | **Met.** `docs/requirements/sys/requirements.json` blob `f128235e`: 188 Active, 2 Closed (retired), 0 Draft; INSP-003 P9 status delta (`08922d9`) APPROVED with liens | Status count at `824a362` |
| P10 | `main` pushed with the tag (charter §8; CM plan §4.4 step 5) | **Pending (post-tag step).** Local `main` at `824a362` is 91 commits ahead of the local tracking ref `origin/main` (`7647516`); R makes it 92. No network command was run. After the independent check at R reads READY FOR TAG, Claude tags R and pushes with `git push origin main --follow-tags` (§8) | `git rev-list --count origin/main..HEAD` = 91 |

Deviations, CRs and the RFA/RID log are unchanged since §0.3: `docs/cm/deviations.md` blob `bcb91b5c` (entries 1 to 4 closed, no open entry, so CM plan §4.4 step 1 does not block the tag); CR-001 `0f4cca4c`, CR-002 `c007177f`, CR-004 `b9fc9510`, CR-005 `9b0129ef` (the §0.3.4 states stand); `docs/reviews/SRR/rfa-rid-log.json` `906d4a19` (the §0.3 states stand). The decision memo (`4c09ef55`, last changed at `305a11e`) reads `baseline_tag: null`. The §0.3.5 liens and TBRs are carried forward unchanged; INSP-010 adds no new lien (its liens finding-14 to finding-18, finding-20 and finding-22 are under L-6, RFA-SRR-006, due PDR).

#### 0.4.3 Configuration items at `824a362` (the parent of R)

Each hash is `git rev-parse 824a362:<path>` (a blob for a file, a tree for a directory), re-taken on 2026-09-27 by a script over every path and hash pair of §0.3.3 (68 pairs, 0 differ) plus direct reads of the firmware tree, `firmware/unsafe-audit.md` and the cited records. Because R changes only this record, each hash is also the hash at R.

| Row (Table 4-1) | CI | Path | Hash at `824a362` | Changed since `49104a5` | Peer review record | Admission (Table 4-2) |
|---|---|---|---|---|---|---|
| 1 | Process charter | `docs/process/00-charter.md` | `41575d218c2228825704ce0b080a967c890fe43f` | no | none (owner direction) | Met (SRR decision 1) |
| 2 | 01 | `docs/process/01-lifecycle-and-reviews.md` | `eabbbd57953c84164e848f36dc327542ac015c00` | no | INSP-019 | Met: APPROVED (`119cb36`) |
| 2 | 02 | `docs/process/02-requirements-and-traceability.md` | `fcdc544555477f0115535348f8ce388453a9034f` | no | INSP-020 | Met: APPROVED (`6257cfe`) |
| 2 | 04 | `docs/process/04-verification-and-validation.md` | `0b197bba692237ed9860ba49c4422f12fa8512dc` | no | INSP-021 | Met: APPROVED with liens (close-out item C delta `49104a5` at `08922d9`) |
| 2 | 05 | `docs/process/05-configuration-and-data-management.md` | `f8de2081f7542ed0bbe47897d8b63e845b8c3114` | no | INSP-006 with INSP-030 | Met: APPROVED (`d8df6a9`, `ff0a610`) |
| 2 | 06 | `docs/process/06-risk-and-decision-analysis.md` | `7a92d21f24a1733d70ae083576e708274bfd1a6d` | no | INSP-007 | Met: APPROVED with liens (`a50aba8`) |
| 2 | 07 (revision A.7) | `docs/process/07-software-engineering-plan.md` | `bfe05f4327e79fa15c24d2cf8c14249804f946a8` | no | INSP-010 with INSP-018 | Met: INSP-010 APPROVED with liens finding-14 to finding-18, finding-20, finding-22 (X-9 copy delta `824a362`; `reviewer_verdict` APPROVED at `c8a5143`); INSP-018 APPROVED with liens finding-8, finding-9, finding-11 (delta 2 `738da03`) |
| 2 | 08 | `docs/process/08-agent-briefing.md` | `01a36bac8d5f133dadd5b384f92f95f225371663` | no | INSP-022 | Met: APPROVED (`119cb36`) |
| 2 | Process index | `docs/process/README.md` | `3664073bc2563f604fb7b1c639a2689a20fb0e6a` | no | none (§7.4 interim check) | Met: 05 §7.4 interim check at `824a362`: the index names all 11 other tracked `docs/process/*.md` files (00 to 08, `rmm.md`, `se-compliance-matrix.md`); blob unchanged since `f3e8801` |
| 2 | SEMP | `docs/plan/semp.md` | `ccfdecf98a6e2dc1371eb057e6aa37903b672de1` | no | INSP-005 | Met: APPROVED with liens (`1e56df4`) |
| 2 | Schedule | `docs/plan/schedule.md` | `82b44894a7613459e41d6827f181d13172390539` | no | INSP-023 | Met: APPROVED (`2f619f8`) |
| 2 | Cost estimate | `docs/plan/cost-estimate.md` | `0dda83cbd5ada9474562cc1741df67a31e1a7ffb` | no | INSP-023 | Met: APPROVED |
| 3 | Classification record | `docs/process/03-software-classification-and-rmm.md` | `ed270f443e2ab648480017df8ad3d0221400cf4c` | no | INSP-009 with INSP-017 | Met: APPROVED (`b54064b`); APPROVED with liens (`af03338`) |
| 3 | RMM | `docs/process/rmm.json` | `e326ddd1b7296d7d7fe172be6f33535cee3192d7` | no | INSP-009, INSP-017 | Met; `render_rmm.py --check` exit 0 |
| 3 | RMM rendering | `docs/process/rmm.md` | `54e351f4df231d1a1e74e6eef4bd07db9a408fa0` | no | rendered | Met |
| 3 | Compliance matrix | `docs/process/se-compliance-matrix.json` | `790d256214e07beb736f2f414a8eaf384ecf2440` | no | INSP-024 | Met: APPROVED; `render_compliance.py --check` exit 0 |
| 3 | Compliance rendering | `docs/process/se-compliance-matrix.md` | `09426930b27e3b51182ab28086c6c73000f274d9` | no | rendered | Met |
| 5 | Stakeholder expectations | `docs/requirements/l0-stakeholder/expectations.json` | `52b6cf5e8f7b4b9fec7ed4c6aa68313967d7104c` | no | INSP-001 | Met: APPROVED (`511c0ca`) |
| 5 | Expectations rendering | `docs/requirements/l0-stakeholder/expectations.md` | `f460c1fb300a29533cf7abdd19ae768130299a5f` | no | rendered | Met |
| 6 | ConOps (directory) | `docs/conops/` | tree `0b04e66c5bed4ea55df42c65ae91fc1e3189b167` | no | INSP-002 | Met: APPROVED (`1cb8b12`) |
| 6 | ConOps revision 3 | `docs/conops/conops.md` | `6c3fbb2be814f5d0a5b2979968e309f6a846445a` | no | INSP-002 | Met |
| 6 | ConOps figures | `docs/conops/figures/conops-context.mmd`, `.png`; `conops-modes.mmd`, `.png` | `55ebae2e15589bf9951456dc04400b7ccb96ea27`, `2e4647f81c61a1d2df05637efa3ee3d71a506e09`; `829a46f800db84ae5196cf3946d4376eb813fc0f`, `b3a08b6770c7c019b67e4b19cd2cdcbba3e8ce6c` | no | INSP-002 | Met |
| 7 | L1 requirements (directory) | `docs/requirements/sys/` | tree `86ea40ebafc0b5de4c773acf78d91b6a55a1efc4` | no | INSP-003 | Met: APPROVED with liens (P9 status delta `08922d9`) |
| 7 | L1 requirements (190: 188 Active, 2 Closed retired) | `docs/requirements/sys/requirements.json` | `f128235ee109cdc325e37c32000ebf9d6027454d` | no | INSP-003 | Met |
| 7 | L1 rendering | `docs/requirements/sys/requirements.md` | `553f7f48aaaea5934f73e59a64d0e0d3b9a7ba5d` | no | rendered | Met |
| 9 | Schemas (the 11 files of §2a row 9, same order) | `docs/design/allocation.schema.json`; `docs/plan/measurements.schema.json`; `docs/plan/tpm.schema.json`; `docs/process/rmm.schema.json`; `docs/process/se-compliance-matrix.schema.json`; `docs/requirements/l0-stakeholder/schema.json`; `docs/requirements/schema.json`; `docs/risk/schema.json`; `docs/safety/schema.json`; `docs/templates/rfa-rid-log.schema.json`; `docs/test_cases/schema.json` | `c17e011ba352839fd8c816a9ef5daf978757dfe2`; `c30b7f3e7466bf4e4474afd031c2c9c91db42be8`; `df3bd894ffec8841245617d0b0c7be6457ddd632`; `ae2f87dd97c7dc9b0e9e4fd5eccbdf35db69e13b`; `ef156b0fcfaaca3b44543154a454b0a965e72a2c`; `d0a79903f8952ed75cf421ff2a73d068f6a32b29`; `ca049dfb0a4480f8de889fe112add0a2e893915f`; `473cd797db582ae2dc4ed14fa83213c3bf2a6d09`; `e96accaad02dcb33a3dfdbcc8da11fd4f28bed84`; `38898b0c260c3292fbc65c59d632790ad4e650f7`; `d4b70163ca13c6263147a49a39f602b88a81517a` | no | none | Met: validate 50 of 50, 424 tests OK (P3); TV-001, TV-003 Accredited |
| 17 | TC-SYS cases (113) | `docs/test_cases/sys/test_cases.json` | `a18824aaf62d5139cdc558e52174726bd5d2f673` | no | INSP-025 | Met: APPROVED (`08e5c9b`); 0 violations |
| 17 | TC-SYS rendering | `docs/test_cases/sys/test_cases.md` | `45e7ca5101b2def1a1f9f7d7ea5e2aa3e851e21a` | no | rendered | Met |
| 27 | Toolchain lock | `tools/toolchain.lock.md` | `04819139c8a10cc6a970d7d08684f7487bf968bb` | no | INSP-015 | Met: APPROVED with liens F-07 to F-13 (re-issue 4 `0359409`, which names blob `04819139`); rustos pin `2ec64c0` (CR-004) unchanged |
| 27 | Venv pins | `tools/requirements.txt` | `ef9820618aafd7fb8d62a24fda4f029a3ffdeb62` | no | none | Met: AL-4, 35 pins equal |
| 51 | Technology assessment | `docs/plan/technology-assessment.md` | `d46abde01adf320630dc317d0a80aa6f197181e5` | no | INSP-014 | Met: APPROVED |
| 52 | Design concept | `docs/design/concept.md` | `6f026f92ae4f090dc85e94e554a0845514adbce9` | no | INSP-002 | Met: APPROVED (`1cb8b12`) |
| 53 | Templates and checklists (22 entries: 21 files plus the row 9 schema) | `docs/templates/` | tree `e94d4ce59c8b62879a1627950eca953281415c03` | no | none | Met (P3) |

Controlled items outside the baseline set (§2c; rows 28, 26 and 25) at `824a362`:

| Row | CI | Path or pin | Hash at `824a362` | Changed since `49104a5` | TV record and accreditation |
|---|---|---|---|---|---|
| 28 | Traceability checker | `tools/traceability.py` | `12de354531f27afd59e9a18798516d218821d6c0` | no | TV-002, ACC-TRACE-001 extended to this blob (TV-002 run 5 `bf654e6`; effective on INSP-015 re-issue 3 `26011f1`) |
| 28 | Document validator | `tools/validate_docs.py` | `3aa0368147b9af3e6e1546f808afb7aedf7f2226` | no | TV-003, ACC-VALDOCS-001 |
| 28 | RMM renderer | `tools/render_rmm.py` | `2386a37fbfb9d7d06c333e0f00981b6fc67e1f27` | no | TV-004, ACC-RMM-001 |
| 28 | Compliance renderer | `tools/render_compliance.py` | `d67d6b5e601a64b013b64e8de3cd0fc3deb96ffa` | no | TV-005, ACC-COMPL-001 |
| 28 | Risk renderer | `tools/render_risk.py` | `d38ba1dd25ac8ef5ecb04ce5b1ea907bb60eee8c` | no | TV-006, ACC-RISK-001 |
| 28 | Review trend | `tools/review_trend.py` | `04493157ae1c3245ca600bf1c29069dfe3192810` | no | TV-007, ACC-TREND-001 |
| 28 | Deck renderer | `tools/slides/render_deck.py` | `b42425e9e9d2ca2b860284914b78ccbabecd38a0` | no | TV-008, ACC-DECK-001 |
| 28 | Review figures | `tools/render_review_figures.py` | `6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e` | no | TV-010, ACC-FIGS-001 |
| 28 | Complexity gate | `tools/complexity_gate.py` | `ddf1079847046d52a268e48a6c82180bd84cca6f` | no | TV-012, ACC-COMPLEXITY-001 extended to this blob by TV-012 run 3 (`0da559a`, record blob `bd99a11d`) and effective from 2026-09-27 on INSP-015 re-issue 4 (`0359409`); liens F-11, F-13. Earlier accredited blob `9cdc9195` |
| 28 | Unsafe audit, measurements | `tools/unsafe_audit.py`, `tools/measurements.py` | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e`, `abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a` | no | TV-011, TV-013: Validated, not accredited (due CDR, PDR) |
| 28 | Software gate | `tools/sw_gate.sh` | `29a37127312e242bce2aa8f41602e3bcd4360f2f` | no | No TV record yet (due CDR); the change is recorded in the lock §1.1 row and checked by INSP-015 re-issue 4 and INSP-016 delta 2 |
| 26 | External rustos | lock §3 | pin `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (CR-004, `5792350`) | no | `git -C /Users/robinonsay/rust/rustos rev-parse master` = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` on 2026-09-27 (ref read only; the owner's rustos working tree was neither read nor modified) |
| 25 | Firmware source | `firmware/` | tree `de1c87cb4190121b965dcc0ae59f3e590421fee9`; `firmware/unsafe-audit.md` `18ef484bf050797e9493d68071efdc0259d423a6` | no | informational until the first `release/FW-*` tag |

Informational items (§2b rows 14, 15, 8, 17, 4), all unchanged since `f3e8801` and equal at `824a362`: `docs/risk/register.json` `0c25c0c5b6ca801b02e47c29c19bb8ed44aa5c79`, `docs/risk/register.md` `a3a983e5cdf7e769666fab26d5f2e7f3b373db1f`; `docs/safety/hazard-analysis.md` `52c8ce16856499afc1b701e1ddb103788fcb1af9`, `docs/safety/hazards.json` `81cacde47d4f2066ecac3947f3acf65e646b1ad0`; `docs/requirements/tx/requirements.json` `8b9d81e8d0f8f605427ef5876adc0f891585a569`, `docs/requirements/sw/sw-keyer/requirements.json` `f9141160c4d92ad80ae91144c2499b22292d4b16`; `docs/test_cases/tx/test_cases.json` `3528d0626e450345a79c9865780db0938b8cff05`, `docs/test_cases/sw-keyer/test_cases.json` `2716ca3f53d349c84f2a4a717a3b7daa1566792f`, `docs/test_cases/sw-tool/test_cases.json` `fee1e7246af59d5e8a43ed1b9cdf483854053fdc`; `docs/requirements/l0-stakeholder/stakeholder-inputs.md` `362250fbaa62c937ffc391477ff9c71f1d41514c`.

Records cited by this section, at `824a362`: INSP-010 `docs/reviews/SRR/checklists/software-plan-07.md` `e7b16d253bca68be38bf049b6fb2a596f8b91ee2` (X-9 copy delta `824a362`); INSP-018 `docs/reviews/SRR/checklists/software-plan-07-software-assurance.md` `9076d5a2d59a827d869057f00b40c8644274de02` (delta 2 `738da03`); `docs/reviews/SRR/baseline-check.md` `7d1eb0896d7f97450395345fdddc9bbe8abf2986` (check 2, `61ab1d7`); decision memo `4c09ef559326951fd9fd2a269e03ec7709aa1441`; minutes `5a5f4ed611f3aeb86d47a610a65ee6d4e9384518`; RFA/RID log `906d4a19e188285e23e942201e9a01f08aca3ad7`; deviations log `bcb91b5c9a267ead07c910e5daf503fc0808ee64`; TC-SW-TOOL-001 run 6 `8d12b38333b4ae863dc8689eed39658dcc276e68`; CR-001 `0f4cca4cb1e2562af05a7c435f41e6ba82d17f26`, CR-002 `c007177f7c3a50bc9ad2f0e4fcdeb798f530c045`, CR-004 `b9fc951091280e1c4e30c5fc0b81a1aae7483aa0`, CR-005 `9b0129efd09e75170a4542d011ff6b1298ad2820`.

**Tool accreditation state.** Unchanged since §0.3.3: TV-001 to TV-010 and TV-012 Accredited on the blobs above (TV-002 at `12de3545`, TV-012 at `ddf10798`); TV-011 and TV-013 Validated, not accredited; `tools/sw_gate.sh` (`29a37127`) has no TV record (due CDR).

**Next steps (Claude, after this commit).**
1. The independent baseline check is repeated at R by a reviewer agent that did not author this record, with every hash taken by `git ls-tree R -- <path>` (CM plan §4.4 step 4; §9 row 2).
2. If it reads READY FOR TAG, Claude runs the §8 commands on R (unsigned annotated tag `baseline/srr`), pushes `main` with the tag (P10), and writes the fill-once fields, §8a and §9 in the post-tag record commit, with the decision memo `baseline_tag` set by amendment (memo section 13).

## 1. Baseline definition

| Field | Value |
|---|---|
| Baseline | Functional baseline per SE HB §6.5.1.2.2, set at SRR per charter §3 and CM plan §4.4 (SRR combined with MCR, customization in CM plan §1) |
| Contents | Table 4-1 rows 1, 2, 3, 5, 6, 7, 9, 17 (cases citing L1 requirements), 27, 51, 52, 53 (CR class); informational rows 14 and 15; row 28 (tools with a TV record by SRR) as controlled items outside the baseline set. Charter §3 core: NGOs, MOEs, ConOps, L1 requirements, SEMP |
| Decision memo | `docs/reviews/SRR/decision-memo.md`, disposition Approved with liens, signed 2026-09-26; memo commit `0bcea39554d684ba28d6680208a523fd79a8ebba` (the commit that set `signed`; later commits append amendments in its section 13 only) |
| Review package | `docs/reviews/SRR/package.md` revision 8 final at `a6d0959`; deck `docs/reviews/SRR/slides/srr.adoc` at `64e53ee` |
| Traceability report at this commit | Review evidence: `docs/reviews/SRR/traceability-report.md` (package revision, PASS, 0 violations, 3 warnings), kept as the SRR evidence and not regenerated after the review (Table 4-1 row 18). Run on 2026-09-26 at `f3e8801` (`tools/traceability.py --report-only`, rendered files restored with `git checkout`): 245 requirements, 173 test cases, **0 violations**, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and 148), tool blob `12de3545` (ACC-TRACE-001 extension). Result: **clean** (P4 met). `docs/vv/traceability-report.md` is regenerated at R. (Earlier run at `be270f1`: 4 violations.) |
| `git fsck --full` on the parent of R | Run 2026-09-26 at `f3e8801`: exit 0 (6 dangling blobs, 1 dangling commit, no errors). Re-run at R. (Earlier run at `be270f1`: exit 0, three dangling blobs.) |
| Table 4-1 match check (`git ls-files` against the Table 4-1 pathspecs) | 1147 tracked files at `f3e8801` (1108 at `be270f1`). The row match is not automated (no `tools/csa.py`), so it is performed at R by the 05 §7.4 interim check |

## 2. Configuration items

Each hash is from `git rev-parse f3e8801:<path>` (a blob for a file, a tree for a directory). `f3e880155e2c222803c3c05e81ea405db5165f86` is the parent of this record commit and was HEAD on 2026-09-26 when this revision was prepared (§0.2). This commit is not R, so every hash is checked again against the parent of R when R is committed, and any hash that differs is refreshed then. The hashes of the earlier revision (parent `be270f1`) are kept in this file's git history. "Peer review" is the filled checklist `docs/reviews/SRR/checklists/<product-slug>.md` (id `INSP-NNN`). "Admission" states the Table 4-2 evidence at `f3e8801`. "Changed since `be270f1`" names the commit that last changed the item, where it did change.

### 2a. CIs in this baseline (class CR)

| Row (Table 4-1) | CI | Path | Hash | Level after tag | Peer review record (`INSP-NNN`, checklist path) | Admission (Table 4-2) |
|---|---|---|---|---|---|---|
| 1 | Process charter | `docs/process/00-charter.md` | `41575d218c2228825704ce0b080a967c890fe43f` | L2 | none (owner direction; Table 4-2 row 1) | Met. SRR decision 1 approves the charter by name (memo §8.0.1 row 1). Changed since `be270f1` at `6ea6b1d`, which applies SRR decisions 7 and 10 (a) and (b) (memo amendment A-5; INSP-027 and INSP-030 re-issued on it) |
| 2 | 01 Life cycle and reviews | `docs/process/01-lifecycle-and-reviews.md` | `eabbbd57953c84164e848f36dc327542ac015c00` | L2 | INSP-019 `process-01-lifecycle-and-reviews.md` | Met: APPROVED (`119cb36`), blob current |
| 2 | 02 Requirements and traceability | `docs/process/02-requirements-and-traceability.md` | `fcdc544555477f0115535348f8ce388453a9034f` | L2 | INSP-020 `process-02-requirements-and-traceability.md` | Met: APPROVED (close-out delta `6257cfe`), blob current |
| 2 | 04 Verification and validation | `docs/process/04-verification-and-validation.md` | `0b197bba692237ed9860ba49c4422f12fa8512dc` | L2 | INSP-021 `process-04-verification-and-validation.md` | Met: APPROVED with liens (delta `f3e8801` on the CR-002 blob of `bf654e6`) |
| 2 | 05 Configuration and data management | `docs/process/05-configuration-and-data-management.md` | `f8de2081f7542ed0bbe47897d8b63e845b8c3114` | L2 | INSP-006 `cm-plan-05.md` with INSP-030 `cm-plan-05-software-assurance.md` | Met: INSP-006 APPROVED (`d8df6a9`) and INSP-030 APPROVED (`ff0a610`), both on `0834da2` (changed since `be270f1` at `0834da2`) |
| 2 | 06 Risk and decision analysis | `docs/process/06-risk-and-decision-analysis.md` | `7a92d21f24a1733d70ae083576e708274bfd1a6d` | L2 | INSP-007 `risk-register-06.md` | Met: APPROVED with liens (`a50aba8`) |
| 2 | 07 Software engineering plan | `docs/process/07-software-engineering-plan.md` | `a9f92d8268deed6a38a677c3a324a9ea99e602aa` | L2 | INSP-010 `software-plan-07.md` with INSP-018 `software-plan-07-software-assurance.md` | **Not met.** INSP-010 is NEEDS CHANGES at `2c4f4da` (finding-21, Major) and INSP-018 is NEEDS CHANGES at `ab494e9` (finding-10, Major). Both are on `3b45ed7` and concern the CS-19 main loop, which has no CS-38 allowance (P1, owner decision B9). Changed since `be270f1` at `e34a27b` (CR-005, 07 revision A.6) |
| 2 | 08 Agent briefing | `docs/process/08-agent-briefing.md` | `01a36bac8d5f133dadd5b384f92f95f225371663` | L2 | INSP-022 `process-08-agent-briefing.md` | Met: APPROVED (`119cb36`), blob current |
| 2 | Process index | `docs/process/README.md` | `3664073bc2563f604fb7b1c639a2689a20fb0e6a` | L2 | none (index; §7.4 interim check) | Check at R |
| 2 | SEMP | `docs/plan/semp.md` | `ccfdecf98a6e2dc1371eb057e6aa37903b672de1` | L2 | INSP-005 `semp.md` | Met: APPROVED with liens (`1e56df4`) |
| 2 | Schedule | `docs/plan/schedule.md` | `82b44894a7613459e41d6827f181d13172390539` | L2 | INSP-023 `schedule-and-cost-estimate.md` | Met: APPROVED (delta `2f619f8` on the owner-approved rebaseline at `d4c9366`; SI-038) |
| 2 | Cost estimate | `docs/plan/cost-estimate.md` | `0dda83cbd5ada9474562cc1741df67a31e1a7ffb` | L2 | INSP-023 `schedule-and-cost-estimate.md` | Met: APPROVED |
| 3 | Software classification record | `docs/process/03-software-classification-and-rmm.md` | `ed270f443e2ab648480017df8ad3d0221400cf4c` | L2 | INSP-009 `classification-03-software-classification-and-rmm.md` with INSP-017 (assurance) | Met: INSP-009 APPROVED (`b54064b`); INSP-017 APPROVED with liens (`af03338`) |
| 3 | Requirements Mapping Matrix | `docs/process/rmm.json` | `e326ddd1b7296d7d7fe172be6f33535cee3192d7` | L2 | INSP-009, INSP-017 | Met: records as above; `render_rmm.py --check` exit 0 at `f3e8801` |
| 3 | RMM rendering | `docs/process/rmm.md` | `54e351f4df231d1a1e74e6eef4bd07db9a408fa0` | L2 | rendered | Met: `render_rmm.py --check` exit 0 |
| 3 | Compliance matrix | `docs/process/se-compliance-matrix.json` | `790d256214e07beb736f2f414a8eaf384ecf2440` | L2 | INSP-024 `compliance-matrix.md` | Met: APPROVED; `render_compliance.py --check` exit 0 |
| 3 | Compliance matrix rendering | `docs/process/se-compliance-matrix.md` | `09426930b27e3b51182ab28086c6c73000f274d9` | L2 | rendered | Met: `render_compliance.py --check` exit 0 |
| 5 | Stakeholder expectations (30 NGOs, 13 MOEs, 28 constraints, 10 stakeholders) | `docs/requirements/l0-stakeholder/expectations.json` | `52b6cf5e8f7b4b9fec7ed4c6aa68313967d7104c` | L2 | INSP-001 `expectations.md` | Met: APPROVED (`511c0ca` on `b087a9f`). Content carries the rulings (P7). Changed since `be270f1` at `d4c9366` and `b087a9f` |
| 5 | Expectations rendering | `docs/requirements/l0-stakeholder/expectations.md` | `f460c1fb300a29533cf7abdd19ae768130299a5f` | L2 | rendered | Met: `traceability.py --report-only` 0 violations; rendered with the JSON at `b087a9f` |
| 6 | ConOps (directory) | `docs/conops/` | tree `0b04e66c5bed4ea55df42c65ae91fc1e3189b167` | L2 | INSP-002 `conops-and-concept.md` | Met: APPROVED (`1cb8b12` on `dd3372c`) |
| 6 | ConOps revision 3 | `docs/conops/conops.md` | `6c3fbb2be814f5d0a5b2979968e309f6a846445a` | L2 | INSP-002 | as above (changed since `be270f1` at `dd3372c`) |
| 6 | ConOps figures | `docs/conops/figures/conops-context.mmd`, `.png`; `conops-modes.mmd`, `.png` | `55ebae2e15589bf9951456dc04400b7ccb96ea27`, `2e4647f81c61a1d2df05637efa3ee3d71a506e09`; `829a46f800db84ae5196cf3946d4376eb813fc0f`, `b3a08b6770c7c019b67e4b19cd2cdcbba3e8ce6c` | L2 | INSP-002 | as above |
| 7 | L1 requirements (directory) | `docs/requirements/sys/` | tree `5b4fbadb43ca656d383152515b9ededfc36873d5` | L2 | INSP-003 `requirements-sys.md` | Met: APPROVED with liens (`401b01d`, blobs at `ebe5873` current) |
| 7 | L1 requirements (190 items: 188 Draft, 2 Closed retired) | `docs/requirements/sys/requirements.json` | `52768afc4f5c3948ca4a2c93be6fd6b9de1c0d33` | L2 | INSP-003 | As above. The status change at the baseline is pending (P9), so this hash changes before R |
| 7 | L1 rendering | `docs/requirements/sys/requirements.md` | `21d25ea38766d079f188555061b8372a5b0c977c` | L2 | rendered | Met (changes with P9) |
| 9 | Schemas | `docs/design/allocation.schema.json`; `docs/plan/measurements.schema.json`; `docs/plan/tpm.schema.json`; `docs/process/rmm.schema.json`; `docs/process/se-compliance-matrix.schema.json`; `docs/requirements/l0-stakeholder/schema.json`; `docs/requirements/schema.json`; `docs/risk/schema.json`; `docs/safety/schema.json`; `docs/templates/rfa-rid-log.schema.json`; `docs/test_cases/schema.json` | `c17e011ba352839fd8c816a9ef5daf978757dfe2`; `c30b7f3e7466bf4e4474afd031c2c9c91db42be8`; `df3bd894ffec8841245617d0b0c7be6457ddd632`; `ae2f87dd97c7dc9b0e9e4fd5eccbdf35db69e13b`; `ef156b0fcfaaca3b44543154a454b0a965e72a2c`; `d0a79903f8952ed75cf421ff2a73d068f6a32b29`; `ca049dfb0a4480f8de889fe112add0a2e893915f`; `473cd797db582ae2dc4ed14fa83213c3bf2a6d09`; `e96accaad02dcb33a3dfdbcc8da11fd4f28bed84`; `38898b0c260c3292fbc65c59d632790ad4e650f7`; `d4b70163ca13c6263147a49a39f602b88a81517a` | L2 | none (no checklist for schemas) | Met: `validate_docs.py` exit 0 (50 of 50) and the unit tests pass (415, OK) at `f3e8801` (P3). TV-001 and TV-003 are Accredited (ACC-PYJS-001; ACC-VALDOCS-001 at blob `3aa03681`, the current blob) |
| 17 | Test cases citing L1 requirements (113 TC-SYS cases) | `docs/test_cases/sys/test_cases.json` | `a18824aaf62d5139cdc558e52174726bd5d2f673` | L2 | INSP-025 `test-cases-sys.md` | Met: APPROVED (post-ruling delta `08e5c9b`); `tools/traceability.py` 0 violations (P4) |
| 17 | TC-SYS rendering | `docs/test_cases/sys/test_cases.md` | `45e7ca5101b2def1a1f9f7d7ea5e2aa3e851e21a` | L2 | rendered | Met |
| 27 | Toolchain lock | `tools/toolchain.lock.md` | `8ab0218a195f05685cc60a3d35af23f7f1f6e24f` | L2 | INSP-015 `tool-validation-tv-001-to-tv-010.md` (review of the lock rows with the TV records) | Met: INSP-015 APPROVED with liens (re-issue 3 at `26011f1`, which reviewed the lock of `37ae576`, CR-004 at `5792350` and `eb52766`). TV-001 to TV-010 are Accredited (SRR decision 114). The lock §1.1 sanity checks are recorded. Changed since `be270f1` at `37ae576`, `5792350` and `eb52766` |
| 27 | Venv pins | `tools/requirements.txt` | `ef9820618aafd7fb8d62a24fda4f029a3ffdeb62` | L2 | none | Met. AL-4 comparison at `f3e8801`: the 35 pins equal `.venv/bin/pip freeze` (05 §14.1 item AL-4) |
| 51 | Technology and heritage assessment | `docs/plan/technology-assessment.md` | `d46abde01adf320630dc317d0a80aa6f197181e5` | L2 | INSP-014 `technology-assessment.md` | Met: APPROVED, blob current |
| 52 | Design concept | `docs/design/concept.md` | `6f026f92ae4f090dc85e94e554a0845514adbce9` | L2 | INSP-002 `conops-and-concept.md` | Met: APPROVED (`1cb8b12` on `dd3372c`; finding-24 closed) |
| 53 | Templates and peer-review checklists (21 files; the schema in the folder is row 9) | `docs/templates/` | tree `e94d4ce59c8b62879a1627950eca953281415c03` | L2 | none (Table 4-2 row 53: validation by tools; each checklist admitted at the revision cited by the SRR records) | Met: `validate_docs.py` exit 0 and the unit tests pass at `f3e8801` (P3) |

### 2b. Informational items (recorded, not yet CR-controlled)

| Row | CI | Path | Hash | Current level |
|---|---|---|---|---|
| 14 | Risk register (65 risks) | `docs/risk/register.json`, `docs/risk/register.md` | `0c25c0c5b6ca801b02e47c29c19bb8ed44aa5c79`, `a3a983e5cdf7e769666fab26d5f2e7f3b373db1f` | L1 (INSP-007 APPROVED with liens); `render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` exit 0 |
| 15 | Preliminary hazard analysis 0.5.0-pha | `docs/safety/hazard-analysis.md`, `docs/safety/hazards.json` | `52c8ce16856499afc1b701e1ddb103788fcb1af9`, `81cacde47d4f2066ecac3947f3acf65e646b1ad0` | L1 (INSP-008 APPROVED with liens, `8fc3402`); CR-controlled from PDR. The OQ-SAF-027 status change and the debounce wording of close-out item 9 are hazard-author edits due PDR (§5) |
| 8 | Early L2 requirements: REQ-TX (16) and REQ-SW-KEYER (39) | `docs/requirements/tx/requirements.json`, `docs/requirements/sw/sw-keyer/requirements.json` | `8b9d81e8d0f8f605427ef5876adc0f891585a569`, `f9141160c4d92ad80ae91144c2499b22292d4b16` | L1 (INSP-004 APPROVED with liens `216098e`; INSP-026 APPROVED `ccf742c`); allocated baseline at PDR |
| 17 | Test cases of the early L2 and tool modules (TC-TX, TC-SW-KEYER, TC-SW-TOOL) | `docs/test_cases/tx/test_cases.json`, `docs/test_cases/sw-keyer/test_cases.json`, `docs/test_cases/sw-tool/test_cases.json` | `3528d0626e450345a79c9865780db0938b8cff05`, `2716ca3f53d349c84f2a4a717a3b7daa1566792f`, `fee1e7246af59d5e8a43ed1b9cdf483854053fdc` | CR-controlled from PDR (Table 4-1 row 17, "all other cases") |
| 4 | Stakeholder inputs log (Record, SI-001 to SI-038) | `docs/requirements/l0-stakeholder/stakeholder-inputs.md` | `362250fbaa62c937ffc391477ff9c71f1d41514c` | Record (append-only); SI-038, the owner's schedule approval, added at `d4c9366` |

### 2c. Controlled items outside the baseline set

| Row | CI | Path or pin | Hash or commit | CR-from event and date | TV record (row 28) |
|---|---|---|---|---|---|
| 28 | Traceability checker | `tools/traceability.py` | `12de354531f27afd59e9a18798516d218821d6c0` (commit `c774851`, CR-002 step 5) | TV-002 accreditation, 2026-09-26; extension to this blob effective 2026-09-26 | TV-002, ACC-TRACE-001, extended to this blob by TV-002 run 5 (`bf654e6`) and made effective by INSP-015 re-issue 3 (`26011f1`; SRR close-out items 5 and 7). Earlier accredited blob: `0a867523` |
| 28 | Document validator | `tools/validate_docs.py` | `3aa0368147b9af3e6e1546f808afb7aedf7f2226` | TV-003 accreditation, 2026-09-26 | TV-003, ACC-VALDOCS-001 (extension at this blob, commit `96af250`) |
| 28 | RMM renderer | `tools/render_rmm.py` | `2386a37fbfb9d7d06c333e0f00981b6fc67e1f27` | TV-004, 2026-09-26 | TV-004, ACC-RMM-001 |
| 28 | Compliance renderer | `tools/render_compliance.py` | `d67d6b5e601a64b013b64e8de3cd0fc3deb96ffa` | TV-005, 2026-09-26 | TV-005, ACC-COMPL-001 |
| 28 | Risk renderer | `tools/render_risk.py` | `d38ba1dd25ac8ef5ecb04ce5b1ea907bb60eee8c` | TV-006, 2026-09-26 | TV-006, ACC-RISK-001 |
| 28 | Review trend | `tools/review_trend.py` | `04493157ae1c3245ca600bf1c29069dfe3192810` | TV-007, 2026-09-26 | TV-007, ACC-TREND-001 |
| 28 | Deck renderer | `tools/slides/render_deck.py` | `b42425e9e9d2ca2b860284914b78ccbabecd38a0` | TV-008, 2026-09-26 | TV-008, ACC-DECK-001 |
| 28 | Review figures | `tools/render_review_figures.py` | `6f3018fdffe25107247f5ef9d010c5cc7d1aaf3e` | TV-010, 2026-09-26 | TV-010, ACC-FIGS-001 |
| 28 | Complexity gate | `tools/complexity_gate.py` | `9cdc91959b06ca3f39142b0afcf85b9a64f719b1` (commit `e34a27b`, CR-005) | ACC-COMPLEXITY-001 effective 2026-09-26 | TV-012, ACC-COMPLEXITY-001: re-validated by TV-012 run 2 (`fb22b7a`, SRR close-out item 4) and made effective by INSP-015 re-issue 3 (`26011f1`), with the liens F-11 and F-13. The run 5 CS-38 failure on `cwht-app::main` is TV-012 limitation 8 and the CR-005 section 9 owner decision, not a tool defect |
| 28 | Unsafe audit, measurements, software gate | `tools/unsafe_audit.py`, `tools/measurements.py`, `tools/sw_gate.sh` | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e`, `abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a`, `52b9f80361939c9c13e76a806264db1b722abefe` (`37ae576`, INSP-016 F-14 fix) | Not yet: Log class until accreditation (TV-011 due CDR, TV-013 due PDR; `tools/sw_gate.sh` has no TV record yet, due CDR) | TV-011, TV-013 (Validated, not accredited) |
| 26 | External `rustos` (informational until the first `release/FW-*` tag) | `/Users/robinonsay/rust/rustos`, lock §3 | pin `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`, set by CR-004 at `5792350` (SRR close-out item 1). The owner fast-forward merged `cwht/wp-sw-licence-manifest-safety` into rustos `master` (minutes `dd39332`); `git -C /Users/robinonsay/rust/rustos rev-parse master` gives this commit at `f3e8801`. Superseded pin: `c54d35a`. The owner's rustos working tree holds uncommitted work of the owner's own, so every build, audit and gate reads a `git archive` export of `2ec64c0`, never the working tree (lock §3) | First release tag (not yet); the next pin move is a CR (Table 4-1 row 26) | n/a |
| 25 | Firmware source (informational until the first `release/FW-*` tag) | `firmware/` | not fixed by this baseline; `firmware/unsafe-audit.md` blob `18ef484b` regenerated by CR-004 (37 sites, 0 without SAFETY) | First release tag (not yet) | n/a |

On 2026-09-26 at `f3e8801`, each accredited row-28 blob above was compared with the blob named in its accreditation. TV-002 and TV-012 were compared with the extensions made effective by INSP-015 re-issue 3. TV-003 to TV-008 and TV-010 were compared with section 9 of their TV records. Every blob is equal. The status lines and section 8 of TV-002 and TV-012 do not yet record that review (INSP-015 re-issue 3 cross item 1, a tool-owner transcription). The accreditation stands on the review record itself. TV-011 and TV-013 are not accredited.

## 3. Approved changes and waivers since the previous baseline

No previous baseline exists. The changes approved at the SRR before the tag:

| CR | Title | Class | Closed | Merge SHA | CIs affected |
|---|---|---|---|---|---|
| CR-001 | CS-11 and CS-38 admit driver-construction failure arms (SRR decision 108) | II | no. Dispositioned, Approved 2026-09-26. Step 1 applied to 07 at `4364ebb`. The step 2 comment is in `firmware/cwht-app/src/main.rs` (since `93d019b`). The step 3 per-file allowance is implemented in `tools/complexity_gate.py` by CR-005 at `e34a27b`. The CR-001 step table still shows steps 2 and 3 open (cross item for the CR owner), and their verification is at the FW-B1 code review | null | row 2 (07), row 25, row 28 |
| CR-002 | Admit Inspection for hazard-tracing requirements that state a documentary or physical property (SRR decision 113) | I (confirmed by SRR close-out item 7) | no. Dispositioned, Approved 2026-09-26. Steps 1 to 4 applied at `d992052`, `cd61450`, `ebe5873` and `bfea9c7`. Step 5, the tool change, is at `c774851` (close-out item 5), with TV-002 run 5 and the step 5 record at `bf654e6`. The independent review of section 4 is still pending: `docs/cm/deviations.md` entry 1, carried by RFA-SRR-008 (close-out item 8, due before the PDR readiness declaration) | null | rows 2, 7, 15, 17, 28 |
| CR-003 | Make REQ-SYS-109 (enclosure) solution-neutral and amend REQ-SYS-124 (SI-037; minutes, "Schedule and enclosure inputs") | not yet proposed | Not raised before the tag. By the lead SE disposition in the minutes, it goes to the owner after `baseline/srr` is tagged, so that the tag carries exactly what was approved at SRR. It is **not** part of this baseline, and its number is reserved | n/a | row 7 after the tag |
| CR-004 | Move the rustos lock pin from `c54d35a` to `2ec64c0` and regenerate the unsafe audit list (SRR close-out item 1) | I (proposed; "Class confirmed: Pending", CR-004 section 7) | no. Dispositioned, Approved 2026-09-26. Applied at `5792350`, with `tools/toolchain.lock.md` §3 and `firmware/unsafe-audit.md` changed in the same commit. The independent review of section 4 is required but not performed. No deviations-log entry exists for this departure, which blocks the tag (§0.2) | null | row 26, row 27, row 25 |
| CR-005 | CS-17 and CS-38 complexity counting convention and the CS-19 halt-loop allowance (SRR close-out item 4) | II (proposed; "Class confirmed: Pending", CR-005 section 7; INSP-015 re-issue 3 cross item 3 argues for Class I) | no. Dispositioned, Approved 2026-09-26. Steps 1 to 3 applied at `e34a27b` (07 revision A.6, `tools/complexity_gate.py`). Step 4 is TV-012 run 2 at `fb22b7a`. The gate CS-38 result on `cwht-app::main` is an open owner decision (CR-005 section 9, run 5 B9) | null | row 2 (07), row 28 |

| Waiver id | Requirement or target | Approving memo or CR | Status |
|---|---|---|---|
| `docs/reviews/SRR/decision-memo.md#W1` | INSP-016 readiness condition R3 ("the design unit is Active and named in `// @design`") for the FW-B0 product only (07 §10.2) | SRR decision 115 (b), owner ruling 2026-09-26; memo §8.2, numbered W1 by memo amendment A-1 | In force for FW-B0 only; lapses for FW-B1 onward |

Requirements volatility over the interval (CM plan §5.4): not applicable to a first baseline; the R16 changes before the tag are the ruled content of the baseline itself (L1: 7 added, REQ-SYS-184 to 190, and edits under the rulings; no L1 requirement retired). The close-out changes after the first close-out run (CR-004, CR-005, CR-002 step 5) change no L1 requirement: `docs/requirements/sys/requirements.json` is unchanged since `cd61450`.

## 4. Editorial changes to controlled CIs since the previous baseline

None (first baseline).

## 5. Liens, open RIDs/RFAs and TBRs carried forward

| Item | Type (lien / RID / RFA / TBR) | Owner | Closure plan | Target review |
|---|---|---|---|---|
| RFA-SRR-001 (L-1) | Lien, RFA Routine | Robin (Claude produces the evidence) | The TBRs carried to PDR decided on Claude's evidence per each `tbr` plan | PDR readiness declaration |
| RFA-SRR-002 (L-2) | Lien, RFA Routine | Claude | Mass and envelope estimates for TPM-001 and TPM-016 | PDR readiness declaration |
| RFA-SRR-003 (L-3) | Lien, RFA Routine | Claude | Create `docs/lessons-learned.md` with the ten package section 19 entries | PDR readiness declaration |
| RFA-SRR-004 (L-4) with RID-SRR-001, 002, 004 to 014 | Lien, RFA Routine and RIDs Minor | Claude | Package-level Minor items fixed in their products and independently verified (memo §6 closure plans). RID-SRR-010 is Answered at `4b6c96c` (ADR-014 erratum `5122a6b`, INSP-011 `877ffac`). It moves to Verified only when a record whose `product` is the ADR-014 file verifies it (memo §13.2) | PDR readiness declaration |
| RID-SRR-003 | RID Minor (R16 requirement edit) | Claude | REQ-SYS-054 rewritten to the no-gap form at `cd61450` (decision 37) and REQ-SYS-184 added, verified by INSP-003 at `401b01d`; the citing cases updated at `ebe5873` (INSP-025 `08e5c9b`); ConOps Table 3.4-4 row 3 aligned at `bfea9c7` (INSP-002 found the decision 37 group correct) | Log state update to Verified by the RFA/RID owner before the tag |
| RFA-SRR-005 (L-5) | Lien, RFA Routine | Claude | Cross-document items due at PDR | PDR readiness declaration |
| RFA-SRR-006 (L-6) | Lien, RFA Routine | Claude | Minor findings of the 30 SRR records ("Lien: fix before PDR"), including the Minors raised in the R16 delta re-issues (for example INSP-003 finding-27 to 31, INSP-008 finding-15 to 21, INSP-009 finding-10, INSP-016 F-13 and F-14) | PDR readiness declaration |
| RFA-SRR-007 (L-7) | Lien, RFA Routine | Claude | Package-level Routine items carried from revision 3 | PDR readiness declaration |
| RFA-SRR-008 | Open item, RFA Routine (not a memo §6 lien: raised after signing, memo amendment A-6) | Claude (lead SE); originated by the owner, SRR close-out item 8 | Independent Class I impact review of CR-002 section 4 by the INSP-003 reviewer, recorded in CR-002 section 6. If the review changes the owner's basis, CR-002 returns to Submitted. This closes `docs/cm/deviations.md` entry 1 | PDR readiness declaration |
| Close-out item 9 wording | Lien (memo §13.2 item 9) | Hazard author (Claude); owning reviewer verifies | OQ-SAF-027 closes on the decision 48 clarification. The product wording that still names the debounce as user-exposed (for example `docs/safety/hazard-analysis.md`, "Rulings at SRR (0.5.0-pha)") is fixed and verified | PDR readiness declaration |
| L1 TBRs (109; counted at `f3e8801`, every one `close_by: PDR`) | TBR | Robin decides on Claude's evidence | Each `tbr` object, `close_by: PDR`: the 101 of memo §6, plus REQ-SYS-180, 181 and 182 (values ratified by decisions 38 to 40, kept TBR with a PDR confirmation plan in their `tbr` objects; memo §8.3 lists them as closed, see note) and REQ-SYS-184, 185, 186, 188 and 189 (added by R16 under decisions 37, 41 and 42). SRR close-out item 10 confirms the 4.35 V bound of REQ-SYS-185 and the 10 kohm fault resistance of REQ-SYS-186 as TBR to PDR, and item 11 places REQ-SYS-189 under decision 41. The count is unchanged | PDR |
| L2 TBRs (25; counted at `f3e8801`) | TBR | Robin decides on Claude's evidence | REQ-TX-002 to 006, 008 to 016 (14); REQ-SW-KEYER-009, 014, 017, 018, 020, 021, 022, 026, 032, 036, 039 (11); `close_by: PDR` (charter §7 allows CDR) | PDR |

Note on REQ-SYS-180 to 182: memo §8.3 records these three TBRs as closed with their ruled values; the requirement file keeps their `tbr` objects with a PDR confirmation plan (monostable timing simulation; PDR thermal analysis; counter design), and INSP-003 approved that state at `401b01d`. Carrying them as TBR with `close_by: PDR` is the conservative reading; the PDR memo closes them. A memo amendment records the difference (amendment A-2).

## 6. Releases included (product and as-built baselines only)

Not applicable to the functional baseline. The FW-B0 images of TC-SW-TOOL-001 runs 1 to 5 are development evidence (`credit: false`), not releases. The run 5 UF2 files are byte-identical to runs 1 to 4.

## 7. Tool accreditation state at this baseline

| Tool | Version (from `tools/toolchain.lock.md`) | Class | TV record | Status |
|---|---|---|---|---|
| venv Python with jsonschema | Python 3.13.5, jsonschema 4.26.0 | B | TV-001 | Accredited 2026-09-26 (ACC-PYJS-001, SRR decision 114) |
| `tools/traceability.py` | blob `12de3545` (`c774851`, CR-002 step 5) | B | TV-002 | Accredited (ACC-TRACE-001, extended to blob `12de3545` by TV-002 run 5 at `bf654e6`, effective on INSP-015 re-issue 3 at `26011f1`; SRR close-out items 5 and 7) |
| `tools/validate_docs.py` | blob `3aa03681` | B | TV-003 | Accredited (ACC-VALDOCS-001 with extension) |
| `tools/render_rmm.py` | blob `2386a37f` | B | TV-004 | Accredited (ACC-RMM-001) |
| `tools/render_compliance.py` | blob `d67d6b5e` | B | TV-005 | Accredited (ACC-COMPL-001) |
| `tools/render_risk.py` | blob `d38ba1dd` | B | TV-006 | Accredited (ACC-RISK-001) |
| `tools/review_trend.py` | blob `04493157` | B | TV-007 | Accredited (ACC-TREND-001) |
| `tools/slides/render_deck.py` with the Chromium headless shell 1223 | blob `b42425e9`; Chrome for Testing 148.0.7778.96 | B | TV-008 | Accredited (ACC-DECK-001) |
| git | 2.50.1 (Apple Git-155) | B | TV-009 | Accredited (ACC-GIT-001) |
| `tools/render_review_figures.py` | blob `6f3018fd` | B | TV-010 | Accredited (ACC-FIGS-001) |
| `tools/complexity_gate.py` fed by `rust-code-analysis-cli` 0.0.25 | blob `9cdc9195` (`e34a27b`, CR-005) | B | TV-012 | Accredited (ACC-COMPLEXITY-001, purposes 1 to 5 under the CR-005 convention; TV-012 run 2 at `fb22b7a`, effective on INSP-015 re-issue 3 at `26011f1`; SRR close-out item 4; liens F-11 and F-13). Limitation 8 (the CS-19 main loop of `cwht-app::main`) waits on the CR-005 section 9 owner decision |
| `tools/unsafe_audit.py`, `tools/measurements.py` | blobs `cc3aaa2a`, `abe25acb` | B | TV-011, TV-013 | Validated, not accredited (TV-011 due CDR, TV-013 due PDR) |
| `tools/sw_gate.sh` | blob `52b9f803` (`37ae576`) | B | none yet (due CDR) | Not validated. The F-14 change is re-checked in lock §1.2, and gate known answers KA-0 to KA-8 MATCH in run 5 |
| rustc, cargo (pinned `1.98.0`), picotool 2.3.0, rust-code-analysis-cli 0.0.25, cargo-audit 0.22.2, cargo-deny 0.20.2, cargo-llvm-cov 0.9.1, cargo-nextest 0.9.146, cargo-geiger 0.13.0, cargo-binutils 0.4.0, nightly-2026-08-24 with `rust-src` and the Miri sysroot (non-credit; SRR close-out item 2), rustup 1.29.1 with auto-self-update disabled (close-out item 3), kicad-cli 10.0.6, LTspice 26.0.2, OpenSCAD 2021.01, FreeCAD 1.1.3, shasum 6.04 | as lock §1 | A or B | TV pending (due PDR or CDR per CM plan §13) | Not yet validated; developer evidence only |

## 7a. Archive (SAR and closeout only; CM plan §8.4)

Not applicable at SRR.

## 8. Tag creation and verification commands

To be run by Claude on R, and not on the §0.2 candidate commit, once the §0.2 preconditions P1 to P9 are met and the CR-004 departure is logged or closed (unsigned annotated tag; charter §8, SRR decision 15):

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
object 779f93fd7214617a08e868cde0e5fafd9b9e848a
type commit
tag baseline/srr
tagger Robin Onsay <hello@robinonsay.com> 1790518158 -0500

cwht functional baseline; decision memo docs/reviews/SRR/decision-memo.md at 0bcea39554d684ba28d6680208a523fd79a8ebba
```

Signed: false (unsigned annotated tag; no signing key configured, charter §8; SRR decision 15 sets signing before `baseline/pdr`). Signature verification: n/a.

Remote push, 2026-09-27: `git push origin main --follow-tags` pushed `7647516..1535cd5 main -> main` and `[new tag] baseline/srr -> baseline/srr`. GitHub reported "Bypassed rule violations for refs/heads/main: Changes must be made through a pull request." The push was made with the owner's account, which the repository protection lets bypass its pull-request rule; this is recorded for the owner (P8).

`git ls-remote --tags origin baseline/srr`:

```
fed29c6ec11a0407bc64935c9c277a49135f4de8	refs/tags/baseline/srr
```

`git ls-remote origin refs/heads/main` (remote sync, CM plan §10.4):

```
1535cd56eda879d1caa86ad81cc9623fca992c03	refs/heads/main
```

CSA (CM plan §4.4 step 6, §6): `docs/process/configuration-status.md` does not exist yet and `tools/csa.py` is due at PDR (CM plan §13). The first CSA report, written by hand from the §6 sources, is the first CM action of the PDR phase and is listed with the SRR liens in the decision memo, amendment A-8.

## 9. Approvals (fill-once, written in the post-tag record commit)

| Step | By | Date | Result |
|---|---|---|---|
| Baseline record prepared (commit R) | Claude | 2026-09-27 | R = `779f93fd7214617a08e868cde0e5fafd9b9e848a` (section 0.4) |
| Record checked against the repository at R (every hash by `git ls-tree R -- <path>`) | independent reviewer agent | 2026-09-27 | READY FOR TAG on R (`docs/reviews/SRR/baseline-check.md`, "Independent baseline check 3", commit `1535cd5`; Minor observations OBS-1 and OBS-2, OBS-2 resolved by this commit) |
| Baseline approved (decision memo) | Owner | 2026-09-26 | Approved with liens ("I approve of this and the SRR.") |

## 10. Corrections (append only)

| Date | Correction | Reference (CR or `Editorial:` commit) |
|---|---|---|
| none yet | | |
| 2026-09-27 | **C-1 (PDR work plan carried item C-094).** §2 and §7 are kept "unchanged as the record of the earlier states" (§0.4 status line), and several of their hash cells are not the hashes at R `779f93f`. (a) The C-094 item: §2c row 28 "Complexity gate" and the §7 row for `tools/complexity_gate.py` (TV-012) give blob `9cdc9195` (commit `e34a27b`, CR-005), with ACC-COMPLEXITY-001 effective on INSP-015 re-issue 3 (`26011f1`). At R the blob is `ddf1079847046d52a268e48a6c82180bd84cca6f` (commit `106bc3a`, CR-005 amendment 1, SRR close-out item A), as `git ls-tree 779f93f tools/complexity_gate.py` prints. For that blob, TV-012 run 3 (`0da559a`; TV-012 record blob `bd99a11d` at that commit) extended ACC-COMPLEXITY-001. The extension is effective from 2026-09-27 on INSP-015 re-issue 4 (`0359409`), with liens F-11 and F-13. (b) The same two sections give `tools/sw_gate.sh` blob `52b9f803` (`37ae576`). At R the blob is `29a37127312e242bce2aa8f41602e3bcd4360f2f` (commit `495a0c3`, SRR close-out item B, G5 Miri `-p api`); it has no TV record (due CDR). (c) §2a, whose hashes were taken at `f3e8801` and marked for re-taking at R (§2 lead), differs from R in five rows: 07 `a9f92d82` (R: `bfe05f4327e79fa15c24d2cf8c14249804f946a8`); `docs/requirements/sys/` tree `5b4fbadb` (R: `86ea40ebafc0b5de4c773acf78d91b6a55a1efc4`); `requirements.json` `52768afc` (R: `f128235ee109cdc325e37c32000ebf9d6027454d`); `requirements.md` `21d25ea3` (R: `553f7f48aaaea5934f73e59a64d0e0d3b9a7ba5d`); `tools/toolchain.lock.md` `8ab0218a` (R: `04819139c8a10cc6a970d7d08684f7487bf968bb`). Every R value above is the value §0.4.3 gives, and §0.4 supersedes §2 and §7 for current values, so neither the baseline content nor the tag changes. This entry lets a reader who starts at §2 or §7 find the R value. Method: on 2026-09-27 a script compared every path that a §2a, §2b, §2c or §7 row names with `git rev-parse 779f93f:<path>`. No other named path differs. | Record-class correction (05 Table 4-1 row 32, "Corrections: dated entries in §10"), committed on `main` with trailer `Refs: SRR, WP-PDR-15`. No CR, because no CI, blob or baseline content changes. No `Editorial:` trailer, because this record is not a class-CR CI. |
