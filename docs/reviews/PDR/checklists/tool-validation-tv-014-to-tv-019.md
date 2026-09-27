---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/05-configuration-and-data-management.md section 9.2 step 3; docs/process/08-agent-briefing.md
# section 3.2). Single record for TV-014 to TV-019 (PDR work plan WP-PDR-07, "one record, one section per
# tool"). Iteration 1 covers TV-014 only: TV-015 to TV-019 are wave 1a work not yet filed (section "TV-015 to
# TV-019").
# Checklists applied: docs/templates/peer-review-checklist-tool-validation.md revision A (blob 7be809d4, CR-012
# branch cr/CR-012-pdr-checklist-templates at 7784672; INSP-033) for the validation, and
# docs/templates/peer-review-checklist-code.md revision B for the wrapper source (03 section 6.1.1 row "Peer
# review"; appended section "Code review"). The checklist field names the code checklist because the tool
# validation template is not yet on main (CR-012 Submitted) and tools/validate_docs.py requires the named
# template to exist in docs/templates/; switch the field to peer-review-checklist-tool-validation at the delta
# re-issue after CR-012 merges (cross item X-5).
id: INSP-038
checklist: peer-review-checklist-code
checklist_revision: B
checklist_tool_validation: "docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md
product: docs/cm/tool-validation/TV-014-ltspice-batch.md
# product_commit: iteration 3 re-issue 3 (the second delta of the owner's route (1) fix loop, on the finding-21 fix)
# reviews bd78bd5 (the author's run 6 record commit): wrapper 88b71475 and test module e90b0ef1 of 45531ac, fixture
# tree f1497c52, run 6 procedure 72dfa2d7 and transcript f87f8fac, TV-014 9c6d477a, lock be96420b, TV README
# f4757da2, tools/README.md a5e9cab6; every product blob is unchanged at HEAD 7126a80 (the one later commit touches
# WP-PDR-27 only). Iteration 3 re-issue 2 reviewed f47360a (the author's run 5 record commit): wrapper bdc4513f (b893382
# finding-20 fix plus the d1148c2 session end), test module 6c4e00e5, fixture tree 61c74693, run 5 procedure
# 4f61ee30 and transcript aa6d45ea; every product blob is unchanged at HEAD c0f5244 (later commits touch other
# work packages only). Iteration 3 re-issue 1 reviewed HEAD d9c7f69
# (run 4). Wrapper, test module, fixture and procedure blobs unchanged since c9d2c54; TV-014, lock and the new
# run 4 transcript from d9c7f69; the two READMEs changed through other work packages (drift rule only).
# Earlier: iteration 3 (delta) reviewed the blobs at HEAD dfde624. No product blob changed since the
# aa746f0 freeze of iteration 2 except the TV README (87fb1e8c) and the lock (b45c8654), which c827202
# (WP-PDR-08) changed on rows other than LTspice. Iteration 2 reviewed aa746f0 and iteration 1 b362395 (blobs
# in the front matter of dfde624 and 3e9d30f)
product_commit: "bd78bd586fb9fe873d67bb1418217fddaa6cdec4"
product_files: ["tools/ltspice-batch.sh@88b71475464bf97ff4e21ec188443edd9c74837b", "tools/tests/test_ltspice_batch.py@e90b0ef1468c4118d6b5116a68e19c6bd2b50a54", "tools/tests/fixtures/ltspice/known-answers.json@84ecdd0ab4773e4be4871cff6f14860fd170f608", "tools/tests/fixtures/ltspice/fake-support/bin/wine@42177aad7ef4ab945c870836c93e7735e5c4f350", "tools/tests/fixtures/ltspice/fake-support/bin/wineserver@6d853df3c6e169d489e38deb281685261b900282", "tools/tests/fixtures/ltspice/rc-step-tran.net@bd19be4123841c512402ffec3009d815ded2de02", "docs/cm/tool-validation/TV-014-ltspice-batch.md@9c6d477af267f9595b7850e9cf8c8f8aec25f2df", "docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27-run6.sh@72dfa2d7395ee6c31b38db7859036da3edbcea1b", "docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27-run6.log.txt@f87f8fac8c22aff08e425174296fee11d50178d5", "docs/cm/tool-validation/README.md@f4757da23bcd4f8220e51de21cc76321cf33fb94", "tools/toolchain.lock.md@be96420b699fe659e7360194d2ce054263121915", "tools/README.md@a5e9cab6415d6d94a33fef03a18f4a408fc4ca29"]
fixture_trees: ["tools/tests/fixtures/ltspice@f1497c5258ed078d44ccc7bb0d4ef95573c871ee"]
tv_ids: [TV-014]
tool_class: B
# tool_kind: the wrapper is a repository tool (G1) around an external tool (G2); both subsections answered
tool_kind: repository-tool
acc_proposed: [ACC-LTSPICE-001]
product_size: 1 record (TV-014), 4 purposes, 46 known-answer tests, 14 fixture files, 465-line wrapper
sprint: PDR-prep
author_agent: "author:WP-PDR-07 (Claude as tool owner)"
tool_author_agent: "author:WP-PDR-07 (Claude as tool owner)"
reviewer_agent: "reviewer:WP-PDR-07-tool-validation-iter6 (independent; authored no part of WP-PDR-07, TV-014, the wrapper, the tests, the doubles, runs 5 and 6, the finding-20 or finding-21 fix or earlier iterations; iteration 3 re-issue 2 by reviewer:WP-PDR-07-tool-validation-iter5; iteration 3 re-issue 1 by reviewer:WP-PDR-07-tool-validation-iter4; iteration 1 by reviewer:WP-PDR-07-tool-validation-iter1, iteration 2 by reviewer:WP-PDR-07-tool-validation-iter2, iteration 3 by reviewer:WP-PDR-07-tool-validation-iter3)"
# criticality: neither (03 sections 4.3.1 and 6.1.1: no tool is a safety-critical or mission-critical
# component). 07 section 2.1.1: code of a "Neither" component needs no assurance review unless the file holds
# unsafe (a shell script has none); the tool validation template has no 2.1.1 row. The swe-136 and swe-070
# section 7.1 tasks are answered in section H by this reviewer as the assurance function (charter section 2)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
# iteration: stays 3 (the schema maximum); the owner-authorized iteration 4 of rule C1 route (1) is recorded as
# "iteration 3 re-issue 1" (precedent INSP-009); the delta after the owner's route (1) decision (status note section 9,
# "with a fix loop") is "iteration 3 re-issue 2", and its second delta, on the finding-21 fix, "iteration 3 re-issue 3"
iteration: 3
# readiness_met: false at iteration 3 re-issue 3: R2 is met (run 6 and the reviewer re-run at 14:59 CDT: 46 run, 45
# passed, only the permitted skip) and no Major is open, but R3 is not: validate_docs.py exits 1 on the same 10 other
# records (record drift after other work packages, finding-17 class; this record PASS) and the everyday suite fails
# only test_validate_docs.RepositoryTests.test_repository_exit_zero for that reason. At iteration 3 re-issue 2: R2 is now met (run 5 and the reviewer re-run at 14:30 CDT: 43 run,
# 42 passed, only the permitted skip), but R3 is not (validate_docs.py exits 1 on 10 other records, finding-17 class,
# not attributable to this record) and Major finding-21 is Open. At iteration 3 re-issue 1: R2 is not met: run 4 is not a pass (busy-lock case skipped, part D
# not completed) and the reviewer re-run at 13:37 CDT fails 20 of 35 cases with exit 5 because the wrapper lock is
# held by orphaned Wine services (finding-20). Earlier (iteration 3): R2 not met in substance: the author made no run 4, and the reviewer re-run at
# 12:08 CDT exits 0 with 35 run, 22 passed, 13 skipped, because the bottle ini still lacks CaptureAnalytics=false
# (420 bytes, modified 10:50, key count 0). R3 is not met: validate_docs.py exits 1 on INSP-015 drift
# (finding-17). Iteration 3 is the last iteration; finding-1 stays Open, so the record is escalated to the owner
# (rule C1; 07 sections 3.4 phase 3 and 10.2)
readiness_met: false
# reviewer_verdict: APPROVED at iteration 3 re-issue 3 (finding-21 Verified; finding-1 and finding-20 re-checked on
# run 6 and held Verified; no Major open). The 14 open Minor findings become liens under rule C1, owner the tool owner
# (WP-PDR-07), due at the CDR readiness declaration unless fixed before
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES only because readiness R3 does not hold (validate_docs.py exits 1 on 10 other
# records; tools/validate_docs.py refuses an APPROVED verdict with readiness_met false). The lead SE sets verdict
# APPROVED, with readiness_met true, in the commit that makes validate_docs.py exit 0 (or the commit right after it),
# provided no product blob has changed; OD-24b (accreditation) may go to the owner on the reviewer verdict
verdict: NEEDS CHANGES
findings_major: 5
findings_minor: 17
findings_open: 14
findings_fixed: 0
findings_verified: 8
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [R3, TV-A1, TV-C2, TV-D1, TV-E1, TV-F1, TV-F3, TV-G1-2, TV-G2-2, CK-CODE-C2]
effort_turns: 36
effort_minutes: 40
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-038: tool validation TV-014 (LTspice through tools/ltspice-batch.sh), WP-PDR-07, iterations 1 to 3, iteration 3 re-issue 1 (owner-authorized iteration 4), iteration 3 re-issue 2 (delta on run 5) and iteration 3 re-issue 3 (delta on the finding-21 fix and run 6)

**Products:** `docs/cm/tool-validation/TV-014-ltspice-batch.md` (blob `246877af`) and every file it validates or cites as evidence, at commit `b362395` (`product_files`; each blob recomputed with `git rev-parse b362395:<path>` and `git rev-parse HEAD:<path>` at HEAD `091bceb`: all equal). Fixture tree `b9f9eca1` at `41d150e`, `b41e544`, `b362395` and HEAD (unchanged since it was committed). **Checklists:** the tool validation checklist of WP-PDR-03 (revision A, blob `7be809d4`, CR-012 branch; applied item by item below) and the code checklist revision B for the wrapper source (section "Code review"). **Acceptance criteria (rule C7):** every clause of 05 section 9.2 step 1 (the TV record fields) and the LTspice row of the 05 section 9.2 known-answer table (stored -3 dB frequency within 1 %, `.log` first line names the version, seeded-error netlist exits 1, `rc-hang-error.asc` time-out guard that kills only its own processes, the `iconv` precondition never appended to); 05 section 9.1 class B (known answer with a seeded fault, TV record before first cited use); 05 section 9.2 steps 3 to 5; every item of the tool validation checklist for `tool_kind` repository-tool plus G2; the INSP-015 finding classes F-01, F-02, F-04, F-05.

**Independence (rule C4):** this invocation authored no part of WP-PDR-07, of TV-014 or of the wrapper, and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "WP-PDR-07 reviewer checklist tool validation record TV-014 ltspice batch"; "uses of tools/ltspice-batch.sh LTspice simulation deck run for Analysis evidence hardware/sim checker"); `grep -n` and `git grep -n` afterwards only pinned lines. **Headless:** no GUI, no LTspice run (the bottle precondition fails, so no LTspice process was started by this review); the bottle ini was read only through `iconv` and `ls`. Reviewer runs that reached the wrapper stopped at its precondition (exit 3) or at a usage refusal (exit 2); three hygiene checks ran on a scratch copy of the fixture with `CWHT_LTSPICE_KEEP=1`, and the kept run directories were deleted afterwards.

## Iteration 1 (2026-09-27)

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | TV-C5, TV-D1, TV-C2, TV-C4; R2 | TV-014 section 4 rows 1 to 3 (lines 79 to 81); `evidence/ltspice-batch-2026-09-27-run2.log.txt` part C | No known-answer result exists for the committed wrapper (blob `102b93d4`): every case that runs LTspice (`LTspiceRunTests` 10 and `TimeoutGuardTests` 1) was skipped in runs 1 and 2, and procedure part D was not run. These cases carry purpose 1, purpose 2, the LTspice clauses of purposes 3 and 4, and every clause of the 05 section 9.2 LTspice row (f(-3 dB) within 1 %, log version line, seeded-error netlist exit 1, time-out guard). The development observations of TV-014 section 4 ran on draft blobs without the lock and before finding 3, so they are not a result for this blob. The reviewer's re-run at 11:38 CDT (bottle ini still 420 bytes, modified 10:50, key count 0) reproduced run 2 exactly: 29 run, 18 passed, 11 skipped. Fix: owner action OA-TV014-1 (see finding-14), then run 3 of the section 3 procedure on the committed blobs with 28 of 29 passed and only `test_bottle_without_key` skipped, part D as stated, recorded in TV-014 section 4 and lock section 1.1; then a delta iteration of this record | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | TV-B3, TV-C2 (INSP-015 F-01 class) | TV-014 section 2 purpose 1 (line 31); `tools/ltspice-batch.sh` lines 9, 91, 228; `tools/tests/test_ltspice_batch.py` (no `-ascii -b` case; line 122 only checks the usage refusal with `-netlist`) | Purpose 1 claims "optionally `-ascii`" delivery of the raw output, but no known answer runs `-ascii -b` or checks an ASCII raw file, so accreditation would cover a behaviour no test exercises. Fix: add a known answer (for example `-ascii -b rc-step-tran.net` with the raw file checked to be ASCII and the V(out) value at 1 ms read from it within 0.1 %), or drop `-ascii` from purpose 1 and from the usage text | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | TV-B3, TV-F1 (INSP-015 F-01 class) | TV-014 purpose 3 (line 33) and section 9 scope (line 122); `tools/ltspice-batch.sh` lines 206 to 212 and 293 to 298; `known-answers.json` `seeded_version` | Purpose 3 claims a non-zero exit on "a program or bundle version other than the lock", and ACC-LTSPICE-001 names bundle 26.0.2.1 and the `LTspice.exe` SHA-256. The wrapper accepts any bundle `26.0.2` or `26.0.2.*` (line 209, prefix match), never checks the `LTspice.exe` SHA-256, and passes a `-b` run whose log has no first line of the form "LTspice ... for MacOS" (line 296 ignores it). The only seeded fault (`CWHT_LTSPICE_VERSION=26.1.1`) exercises a different minor version, not a different bundle build of 26.0.2, a changed `LTspice.exe` or a log without a version line. A silent LTspice update inside 26.0.2.x would therefore run under the accreditation. Fix: either compare the bundle exactly with the locked `26.0.2.1`, check the `LTspice.exe` SHA-256 before each run and fail `-b` when the log carries no version line, each with a seeded fault; or narrow purpose 3 to what is checked and move the bundle and SHA-256 conditions into the scope statement as conditions verified by lock re-observation, with that check named in section 7 | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | TV-C2, TV-D1 | `tools/tests/test_ltspice_batch.py` lines 192 to 199; TV-014 section 4 rows 1 and 2; lock section 1.1 LTspice row | While the bottle lacks the key, the three `PreconditionTests` that name the ini fixtures (`test_ini_without_key`, `test_ascii_appended_key_not_accepted`, `test_missing_extra_ini`) pass on the bottle failure (line 199 asserts the bottle message), so the seeded ini fixtures were not exercised in runs 1 and 2. TV-014 and the lock count them among "18 passed" without saying so. Fix: state in section 4 that these three cases exercised only the bottle refusal in runs 1 and 2; run 3 exercises the fixtures | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | TV-C1, TV-D1 | `evidence/ltspice-batch-2026-09-27.sh` lines 42 to 44 and 69; test module lines 9 to 12; `tools/README.md` LTspice paragraph | A blocked run reports success: `unittest` prints "OK (skipped=11)" and exits 0, the procedure prints `exit=0`, and the repository suite (`unittest discover -s tools/tests`, readiness R3 and gate runs) stays green while no LTspice case ran. The pass criterion lives only in prose. Fix: have the procedure compute the verdict (fail when any test other than `test_bottle_without_key` is skipped or when part D did not run) and print PASS or FAIL with a non-zero exit on FAIL | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-CODE-C2 (error handling) | `tools/ltspice-batch.sh` lines 313 to 326 | The output copy ignores failures: `cp` at lines 321 and 323 has no status check (`set -u` only, no `set -e`), so a full disk or an unwritable OUTDIR still ends in "result: PASS" with missing or stale-free but absent outputs. Fix: check each copy and fail with exit 1 naming the file | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | TV-G1-2 (INSP-015 F-05 class) | `tools/ltspice-batch.sh` line 138 versus header lines 46 to 50; TV-014 section 2 | The INT and TERM trap exits 130, a status the header, the `exit_codes` block and TV-014 do not document and no test covers. Fix: document 130 (interrupted, run killed) in the header, the fixture and the record, and add a known answer (send SIGTERM to a wrapper running `rc-hang-error.asc` and check exit 130 and no survivor) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | TV-E1 (INSP-015 F-04 class), TV-C2 | TV-014 limitation 4 (line 103); `tools/ltspice-batch.sh` lines 220 to 222 and 248 to 252 | Limitation 4 says the post-run key check cannot be exercised without editing the owner's ini. The existing test hook can carry it: if the wrapper also re-checks `CWHT_LTSPICE_INI_CHECK` after the run, a test can swap that file to `ini-without-key.ini` while a run is in progress (for example during the time-out case) and expect exit 3 with no outputs copied. Fix: add the post-run check of the hook file and the seeded case, or state in limitation 4 why the hook is not used | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer | Minor | TV-E1, TV-G2-2 | `tools/ltspice-batch.sh` lines 255 to 260; TV-014 limitation 6 (line 105) | After a time-out with survivors (exit 124, "processes of this run survive") the wrapper exits and the kernel releases the lock while the surviving `LTspice.exe` may later exit and rewrite the ini during the next run, the mechanism TV-014 finding 2 names. Limitation 6 does not state this, and the message does not tell the user to stop LTspice work. Fix: state it in limitation 6 and in the survivor message ("stop all LTspice work and report to the owner", as the post-run key message does) | Open | Pending | |
| <a id="finding-10"></a>finding-10 | reviewer | Minor | TV-E1, TV-D1 | TV-014 section 4.1 finding 2 (line 90); `evidence/ltspice-batch-2026-09-27-development.log.txt` section 5 | The truncated ini holds two recent-file entries that name a 2026-09-25 sanity-check directory (`kat-ltspice.p0JfEq`), not any 10:50 run directory, which the concurrent-exit explanation does not account for; the cause is inferred, not shown, and the lock is therefore an unconfirmed mitigation. Fix: record the cause as probable with this observation, and have run 3 log the ini SHA-256 before and after each LTspice case so that the record shows the key survives serialized runs | Open | Pending | |
| <a id="finding-11"></a>finding-11 | reviewer | Minor | TV-F1, CK-CODE-G1 | `tools/ltspice-batch.sh` lines 52 to 56, 59, 64, 206; provenance line 328 | The test hooks `CWHT_LTSPICE_VERSION` and `CWHT_LTSPICE_SUPPORT` can waive the lock check (a different locked version; with `CWHT_LTSPICE_SUPPORT` set the bundle check is skipped entirely), the header claims only that `CWHT_LTSPICE_INI_CHECK` cannot waive a check, and the provenance line does not record any override. Fix: print every `CWHT_LTSPICE_*` override in the provenance line and state in the scope statement that runs for the record have none set | Open | Pending | |
| <a id="finding-12"></a>finding-12 | reviewer | Minor | TV-F3, TV-D2 | `tools/toolchain.lock.md` line 265 (section 5 TV-014 row) | The next-step column still reads "pending: run 2, independent review ..." although run 2 is recorded (line 70 and TV-014 section 4); it should name run 3 after OA-TV014-1 | Open | Pending | |
| <a id="finding-13"></a>finding-13 | reviewer | Minor | TV-A2 | `tools/toolchain.lock.md` line 313 (section 7 LTspice row); TV-014 section 1 install source (line 27) | Lock section 7 says the SHA-256 substitute for the unversioned installer is "recorded when the tarball is made at the LTspice TV (due PDR)"; TV-014 records the `LTspice.exe` SHA-256 only and neither makes the tarball nor says the lock commitment is replaced. Fix: record the tarball and its SHA-256 in TV-014 section 1, or state that the `LTspice.exe` SHA-256 is the accepted substitute and update the section 7 row | Open | Pending | |
| <a id="finding-14"></a>finding-14 | reviewer | Minor | TV-F4, R5 | TV-014 lines 6, 81, 90; `docs/cm/tool-validation/README.md` line 38; `docs/plan/pdr-work-plan.md` section 6.1 | Owner action OA-TV014-1, on which run 3 and the whole record depend, is named but defined nowhere (`git grep OA-TV014-1` finds only these mentions): no steps, no check, no entry in the plan's owner-action list or in the README common owner actions. Fix: define it in TV-014 (or the README owner-action list): open LTspice once from the Finder, answer No in the consent dialog, quit; confirm with the `iconv` precondition command (count 1); no agent LTspice run in between; and register it with the lead SE for plan section 6.1 (B0 session) | Open | Pending | |
| <a id="finding-15"></a>finding-15 | reviewer | Minor | TV-G2-2, TV-A6 | `evidence/ltspice-batch-2026-09-27.sh` lines 55 to 58 | Part D runs the bare `wine` command under the lock with no time-out guard and no post-run key check, while 05 section 9.2 requires a time-out guard on every run and `tools/README.md` calls the wrapper the only permitted way to run LTspice. Fix: bound part D with the same time-out and kill-by-directory guard and re-check the key after it (or state in TV-014 why this single bare run is exempt) | Open | Pending | |
| <a id="finding-16"></a>finding-16 | reviewer | Minor | TV-C1 | `tools/tests/fixtures/ltspice/rc-include-escape.net` line 1 | The header comment names the block `known-answers.json "wrapper.include_escape"`; the block is `wrapper.seeded_include_escape` | Open | Pending | |
| <a id="finding-17"></a>finding-17 | reviewer | Minor | R3, TV-F3 | `tools/validate_docs.py` at HEAD `091bceb`: FAIL on `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` (INSP-015); `test_validate_docs.RepositoryTests.test_repository_exit_zero` fails | The WP-PDR-07 commits `573f9f5` and `b362395` (with `71bf509` of WP-PDR-08 and `495a0c3`) changed `docs/cm/tool-validation/README.md` and `tools/toolchain.lock.md`, which the APPROVED INSP-015 names at blobs `22f7b2bf` and `04819139`, with no delta re-issue of INSP-015, so the record drift rule fails and `validate_docs.py` exits 1 (readiness R3 of this checklist). Fix: request an INSP-015 delta re-issue at the current README and lock blobs (the SRR re-issue pattern), or record the drift as an accepted deviation; route through the lead SE | Open | Pending | |

### Per-record results

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-014 | LTspice 26.0.2 (bundle 26.0.2.1, `LTspice.exe` `a94eb178...793f06`, CrossOver 25.0.1.38665) through `tools/ltspice-batch.sh` blob `102b93d4` | B | `b41e544` (run 2); record at `b362395` | `CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py` at HEAD (identities equal to `b362395`), 11:38 CDT: exit 0, 29 run, 18 passed, 11 skipped (bottle precondition not met): same as run 2; `tools/ltspice-batch.sh -version`: exit 3 (precondition); fixture digest recomputed `069f03ee...0992835`, equal to the record | R2, R3, TV-A1, TV-B3, TV-C2, TV-C5, TV-D1, TV-D2, TV-E1, TV-F1, TV-F3, TV-G1-2, TV-G2-2 | finding-1 to finding-17 |

### Per-purpose results

| TV record | Purpose | Known answer that exercises it | Seeded fault (class B) | Cited uses of the purpose in the project | Finding ids |
|---|---|---|---|---|---|
| TV-014 | 1: run a deck headless with `-b` (optionally `-ascii`) and deliver `.log`, `.raw`, `.op.raw` beside the deck or in `-o` | `test_ac_known_answer`, `test_transient_known_answer`, `test_relative_include_is_copied`, `test_output_directory`, `test_stale_outputs_removed` (all skipped in runs 1 and 2); no `-ascii -b` case | `rc-seeded-error.net` exit 1; `rc-include-escape.net` exit 2; long name exit 2 | 05 section 9.1 (Analysis class); 04 section 4 Simulation row; lock section 1 LTspice row; TC-TX envelope case and TC-SYS selectivity case (Simulation); WP-PDR-19 to 26 and 28 (plan section 3.6); `docs/research/ltspice-batch-macos.md` REQ-candidates | finding-1, finding-2 |
| TV-014 | 2: `-netlist` a schematic and reject any `NC_` net | `test_netlist` (skipped) | `rc-nc-error.asc` exit 1 for `-netlist` and `-b` (`test_seeded_floating_net`, skipped) | research F9 REQ-candidate; lock section 1 row | finding-1 |
| TV-014 | 3: never report a pass LTspice did not complete (key before and after, version, deck error or exit, missing log or raw, floating net, time-out, include escape, path of 260 or more) | usage, hygiene, version, lock and precondition cases (passed); LTspice cases (skipped) | `seeded_version` exit 4; `seeded_not_installed` exit 3; `seeded_ini` exit 3; `seeded_busy` exit 5; `seeded_include_escape` and `seeded_long_path` exit 2; `seeded_deck_error` and `seeded_floating_net` exit 1 (skipped); `timeout_guard` exit 124 (skipped); post-run key: inspection only | 05 section 9.2 LTspice row; ADR-018; lock section 1.4 findings 1, 2, 12 to 14 | finding-1, finding-3, finding-4, finding-8, finding-11 |
| TV-014 | 4: record provenance on stderr (version line, deck SHA-256, exit, elapsed, outputs) | `test_ac_known_answer` asserts `sha256=` in stderr (skipped); no test asserts the version line, exit or outputs fields | none | research REQ-candidate "report shall record the version line, the deck hash and the checker output" | finding-1, finding-11 |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Everything committed; `product_files` lists every blob; `fixture_trees` gives the tree | Yes | `git ls-tree -r HEAD tools/tests/fixtures/ltspice/` lists the 12 files at the blobs above; `git rev-parse b362395:tools/tests/fixtures/ltspice` = `b9f9eca1`; `git status --short` empty at start |
| R2 | The section 3 known-answer command runs and exits 0 on the committed state | No | It exits 0 only because 11 cases skip; the record's own pass criterion (28 of 29 run and passed) is not met (finding-1, finding-5) |
| R3 | `unittest discover -s tools/tests` passes and `validate_docs.py` exits 0 | No | 453 tests: FAILED (failures=1, skipped=11), the failure is `test_repository_exit_zero`; `validate_docs.py`: 52 passed, 2 failed (INSP-015 drift, finding-17; `risk-register-06.md` drift from another WP) |
| R4 | Lock rows (sections 1, 1.1, 5) and the README index row exist | Yes | lock lines 12, 14, 70, 123, 171 to 173, 265; README line 38 |
| R5 | Author return lists purposes, cited uses, tests, runs with commits, proposed scope | Yes, except the owner action | author summary in the brief; OA-TV014-1 undefined (finding-14) |

## A. Identification

| Id | Answer | Evidence |
|---|---|---|
| TV-A1 | No (partly) | Bundle `26.0.2.1` (`defaults read`, re-run 11:38), Wine layer `25.0.1.38665` (`cxbottle.conf`) and `LTspice.exe` SHA-256 `a94eb178...793f06` reproduced; the program version `26.0.2` cannot be re-observed because `-version` stops at the precondition (exit 3); it rests on the 2026-09-25 bare-command observation (finding-1) |
| TV-A2 | No (Minor) | Installer URL unversioned, no vendor checksum (TV-014 line 27; lock line 313); substitute not reconciled with lock section 7 (finding-13) |
| TV-A3 | Yes | Wrapper blob `102b93d4`, SHA-256 `a6acffa6...265152`; test module `c4410447`, `841a3b93...0a32`; fixture digest `069f03ee...0992835` recomputed at HEAD, all equal to TV-014 section 1 |
| TV-A4 | Yes | Run 1: HEAD `e119181` with identities "unchanged from HEAD" (wrapper `884df077`); run 2: HEAD `b41e544`, identities equal; `git ls-tree b41e544` gives `102b93d4` and `c4410447` |
| TV-A5 | Yes | Class B (TV-014 line 7): output cited as Analysis evidence, never part of a release (05 section 9.1 row B names "LTspice through the CrossOver wrapper") |
| TV-A6 | Yes | Wrapper and procedure are shell and Python only; no GUI step; OA-TV014-1 is an owner GUI step outside the agent's run (charter section 11 rule 8), see finding-14; part D exception in finding-15 |

## B. Purposes

| Id | Answer | Evidence |
|---|---|---|
| TV-B1 | Yes | Four one-line purposes, each stating inputs, outputs and exit behaviour (TV-014 lines 31 to 34) |
| TV-B2 | Yes, with cross items | Vector search for the wrapper and LTspice uses: every cited use is running a committed deck for Analysis evidence (purpose 1) with the checker judging the numbers; the TC-SYS cases, ADR-018 and 04 section 4 name the wrapper as `tools/run_sim.py`, a path that does not exist (cross item X-2); `docs/design/concept.md` line 359 claims a Monte Carlo batch "already ran through it", a `.step` use outside limitation 1 (cross item X-4) |
| TV-B3 | No | `-ascii` in purpose 1 has no known answer (finding-2); purpose 3 claims bundle-version rejection the wrapper does not perform (finding-3) |

## C. Known-answer test

| Id | Answer | Evidence |
|---|---|---|
| TV-C1 | Yes (Minor comment error) | Fixture root `tools/tests/fixtures/ltspice/`, expected values in `known-answers.json` block `wrapper`, run command and numeric criteria in TV-014 section 3; finding-5 (verdict not computed), finding-16 |
| TV-C2 | No | Every purpose has cases and seeded faults are defined, but none of the LTspice cases has run on the committed blob (finding-1); `-ascii` has none (finding-2); the ini fixtures were not exercised (finding-4); the post-run key check has no seeded fault (finding-8) |
| TV-C3 | Yes | Reviewer recomputation: 1/(2 pi 1000 159.155e-9) = 999.99964 Hz (stored 999.9996); 1 - e^-1 = 0.63212056 V (stored 0.6321206); 1 ms ln 2 = 0.69314718 ms (stored 0.6931472 ms). Values come from the circuit equations, not from LTspice; the 2026-09-25 observed value is stored separately as `observed_2026_09_25_hz` |
| TV-C4 | Yes as designed, not yet met | 05 section 9.2 LTspice row: f(-3 dB) within 1 % (`test_ac_known_answer`, tolerance 0.01), log first line (`log_first_line`), seeded-error netlist exit 1 (`test_seeded_deck_error`), time-out guard (`TimeoutGuardTests`), precondition by `iconv` without write (wrapper line 217). All implemented, none executed on blob `102b93d4` (finding-1) |
| TV-C5 | No | Reviewer re-run reproduces the blocked run 2, not a pass (per-record table; finding-1) |

## D. Results and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| TV-D1 | No | Rows 1 and 2 carry date, commit, counts, excerpt and committed transcripts, but both are blocked and row 3 is empty (finding-1); the "18 passed" wording overstates the ini cases (finding-4) |
| TV-D2 | No (Minor) | Lock section 1.1 line 70 records runs 1 and 2 with commits; section 5 row still names run 2 as pending (finding-12) |
| TV-D3 | N/A | Class B; repeat f(-3 dB) values reported in TV-014 section 5 |

## E. Limitations and re-validation triggers

| Id | Answer | Evidence |
|---|---|---|
| TV-E1 | No (Minor) | Confirmed by code: limitation 2 (include scan regex, wrapper line 171; reviewer check: `.include`, upper-case `.INCLUDE "..."` copied, a backslash path `sub\rc-parts.inc` not copied, which then fails in LTspice as the limitation says), limitation 7 (`getconf`, `lockf`, `defaults`). Contradicted or incomplete: limitation 4 (finding-8), limitation 6 (finding-9), finding 2 cause (finding-10) |
| TV-E2 | Yes | TV-014 section 7: wrapper, test module and fixture changes; bundle, `LTspice.exe` SHA-256, Wine layer, bottle rebuild, macOS major version; interpreter; defects with NCR (SWE-201); class A expiry not applicable |

## F. Accreditation readiness, schedule and indexes

| Id | Answer | Evidence |
|---|---|---|
| TV-F1 | No | ACC-LTSPICE-001 names purposes 1 to 4, blob, versions and limitations, but covers `-ascii` and bundle-build rejection that no known answer checks (finding-2, finding-3) and does not require the test hooks unset (finding-11) |
| TV-F2 | Yes | Due PDR (05 section 13 PDR row); no product cites a wrapper result yet (WP-PDR-19 to 28 not started); header says it blocks them |
| TV-F3 | No (Minor) | README line 38, lock line 265 and the header agree on "Not yet validated" and PDR; lock next step stale (finding-12); validate_docs drift (finding-17) |
| TV-F4 | Yes | Section 9 leaves the decision to the owner (OD-24b) and limitation 8 states developer evidence until then |
| TV-F5 | N/A | First TV record for the tool; no accredited version exists |

## G1. Repository tool

| Id | Answer | Evidence |
|---|---|---|
| TV-G1-1 | Yes | The module has no repository-content test; it reads only the fixture and the machine state (bottle), and the machine-state dependence is stated in its docstring |
| TV-G1-2 | No (Minor) | Exit statuses 2, 3, 4, 5 have passing cases; 0, 1, 124 have cases that did not run (finding-1); 130 is undocumented and untested (finding-7) |
| TV-G1-3 | Yes | Code review appended below at blob `102b93d4` |

## G2. External tool

| Id | Answer | Evidence |
|---|---|---|
| TV-G2-1 | Yes | The wrapper runs the lock section 1 `wine` command (line 230) and checks the precondition exactly as lock line 12 states (`iconv`, `tr -d '\r'`, `^CaptureAnalytics=false$`, never written, line 217); tools/README and lock line 12 make the wrapper the only permitted path. 05 section 9.2 and 08 still print the pre-wrapper form (cross items X-1, X-6) |
| TV-G2-2 | No (Minor) | Wrapper guard kills by the unique directory name in either path form (lines 234 to 244, 255 to 265), reviewer-verified by reading; not yet exercised (finding-1); lock release with survivors (finding-9); part D unguarded (finding-15) |
| TV-G2-3 | Yes | No download or install was made for TV-014 (TV-014 section 1; lock history rows of 2026-09-27 name none) |

## G3, G4

N/A: not an emulator and not instrument firmware.

## H. Software assurance tasks

| Id | Answer | Evidence |
|---|---|---|
| TV-H1 | N/A | swe-136 7.1 task 1 applied: the wrapper does not build or check firmware, so no 07 section 8.4 gate step cites it; the task's result for this tool is carried by TV-H2 |
| TV-H2 | No (open) | swe-070 7.1 task 1 (`docs/references/md/swehb/swe-070-models-simulations-tools.md` line 721, "Confirm that the software models, simulations, and analysis tools used to achieve the qualification ... have been validated and accredited"): not yet confirmable, TV-014 is not validated (finding-1). Model validity is correctly pushed to each analysis record (limitation 1; `peer-review-checklist-analysis.md` item CK-ANA-C2) |
| TV-H3 | Yes | `assurance_tasks_applied` lists both tasks |

## Code review of tools/ltspice-batch.sh (peer-review-checklist-code.md revision B, blob 102b93d4, 334 lines)

The code checklist is written for Rust firmware; for a bash tool the reviewer applied the language-neutral intent of each item and lists the Rust-specific items as N/A. Criticality neither; no `unsafe` (07 section 2.1.1: no assurance review).

| Id | Answer | Evidence |
|---|---|---|
| R1 to R6 | N/A for Rust gates; file length measured | `wc -l` 334 lines; the largest block (arguments to hygiene) is straight-line shell; no `cargo` gate applies |
| CK-CODE-A1 to A3, B1 to B8, C5 to C7, D1, D3, D5, D6, D8, D9, E3, E4, E7, E8, F1 to F3, G2 to G5, H3, I1 to I3, J1, J2 | N/A | Rust, firmware, register, keyer, safe-state, MC/DC and traceability-tag items do not apply to a host shell tool |
| CK-CODE-C1 | Yes | No unchecked abort paths: every refusal goes through `die` with an exit code (lines 77, 99 to 102, 142 to 175, 198 to 221) |
| CK-CODE-C2 | No (Minor) | Every documented failure maps to an exit code, but the output copy ignores `cp` failures (finding-6) |
| CK-CODE-C3 | Yes | Each failure class maps to one exit (1, 2, 3, 4, 5, 124) with the first failure kept (`fail`, line 280) |
| CK-CODE-C4 | Yes | Integer arithmetic only on seconds (lines 235, 247) after the numeric checks at lines 99 and 197 |
| CK-CODE-D2 | Yes | Loops are bounded: the include queue terminates because each relative path is recorded in `.done` (line 169 to 170); the wait loop ends at the time-out; `kill_tree` recursion follows the finite process tree |
| CK-CODE-D4 | Yes | No variable shadows another in a way that changes meaning; `f` is reused in two separate loops (lines 168, 316) without overlap |
| CK-CODE-D7 | Yes | Nesting at most 3 levels; the file is 334 lines |
| CK-CODE-E1 | Yes | Behaviour matches the header steps 1 to 7 and TV-014 section 2, except the claims of finding-2 and finding-3 |
| CK-CODE-E2 | Yes | Constants named: `TIMEOUT` 120 s, `LOCK_WAIT` 600 s, MAX_PATH limit 260 with the reason at line 158 |
| CK-CODE-E5 | Yes | Prerequisites in the designed order: hygiene, lock, installation and version, key, run, post-run key, result checks (lines 124 to 308) |
| CK-CODE-E6 | Yes | Output read-back: `.log`, raw and netlist existence checked before PASS (lines 284 to 308); the key is re-read after the run (lines 248 to 252) |
| CK-CODE-E9 | Yes | No dead code; every helper is called |
| CK-CODE-G1 | Yes, with finding-11 | Inputs validated at the boundary: mode, deck extension, white space, `..` includes, path length, numeric `-t` and wait; the environment hooks are not recorded (finding-11) |
| CK-CODE-H1, H2 | Yes | The tool is testable through its hooks without editing the owner's files; the test module is by the same author (a tool known-answer module, not an independent firmware test; 05 section 9.2 step 3 makes this review the independent check) |
| CK-CODE-I4 | Yes | Comments state why (MAX_PATH, ini rewrite, Windows path form); no commented-out code |
| CK-CODE-J3 | Yes | "Refuse and do not run" conditions are all checked before LTspice starts; the only after-the-fact check is the post-run key, which withholds the outputs (line 251) |
| CK-CODE-J4 | Yes | Measured with `wc -l`, not estimated |

Observations with no finding: the lock works across shells (reviewer test in the scratch directory: a second shell got `lockf -t 0` busy, then acquired after the first released); the child `wine` is started with fd 9 closed (line 230), so LTspice never holds the lock; the run directory resolves under `/private/var/folders/...` and the length check uses that resolved form (line 159), which is the path LTspice receives.

## TV-015 to TV-019

Not filed at this iteration (`tools/scad2step.py`, `tools/normalize_fab.py`, `tools/render_tpm.py`, `tools/csa.py`, `tools/check_commit_msg.py` are wave 1a work, plan section 5.2). Each gets its own section in a later iteration of this record, with `tv_ids` and `product_files` extended.

## Cross items (not findings against TV-014; routed to the named owner)

| Id | Item | Owner |
|---|---|---|
| X-1 | 05 section 9.2 LTspice row prints the precondition as `iconv ... \| /usr/bin/grep -q '^CaptureAnalytics=false$'` without `tr -d '\r'`; on the CRLF ini that command never matches (lock line 12 and wrapper line 217 carry the correct form). A baselined item: Log or Class II CR per 05 | CM plan owner (configuration manager, WP-PDR-05) |
| X-2 | `docs/test_cases/sys/test_cases.json` (9 occurrences), `docs/process/04-verification-and-validation.md` line 97 area, `docs/templates/test_cases.example.json` and ADR-018 lines 31 and 55 name the LTspice wrapper `tools/run_sim.py`, which does not exist; TV-014 accredits only `tools/ltspice-batch.sh` | WP-PDR-11 (TC-SYS), lead SE (04, template, ADR-018) |
| X-3 | `docs/process/configuration-status.md` (hand CSA) lists the wrapper at blob `884df077` with "no record file at HEAD" | WP-PDR-05 |
| X-4 | `docs/design/concept.md` line 359 names `tools/ltspice_check.py` and says the cw-selectivity Monte Carlo batch "already ran through it"; `.step` statistics are outside TV-014 limitation 1, so the analyses of WP-PDR-19 to 28 that use `.step` or tolerance corners must validate that use in their own records | WP-PDR-31 (concept) and the analysis WPs |
| X-5 | The tool validation checklist is not on `main` (CR-012 Submitted), so this record's `checklist` field names the code checklist; switch it at the delta re-issue after CR-012 merges | Lead SE (CR-012 disposition) |
| X-6 | 08 briefing COMMANDS LTspice line (line 55) still gives the bare `wine` command with a manual 120 s kill as the primary form; with the wrapper committed it should give the wrapper command | Lead SE (08 owner) |
| X-7 | Software assurance pair: not required. 07 section 2.1.1 gives No for code of a "Neither" component without `unsafe`, and the tool validation template sets `assurance_required: false`. The plan gives WP-PDR-06 an SA pair "(tool used for credit)" but names none for WP-PDR-07; if the lead SE applies the same rule to the LTspice wrapper (its output will verify HZ-008 through the TC-TX envelope case), an SA pair must be dispatched separately | Lead SE |

## Verdict

```
VERDICT: NEEDS CHANGES
PRODUCT: TV-014 at b3623951de027a0a0b00f4a3bb7dea3aec390fb9 (wrapper blob 102b93d4, test module c4410447, fixture tree b9f9eca1)
FINDINGS:
- [Major] finding-1 TV-C5/TV-D1: no known-answer result for blob 102b93d4; all 11 LTspice cases skipped in runs 1, 2 and the reviewer re-run.
- [Major] finding-2 TV-B3: purpose 1 claims -ascii with no known answer.
- [Major] finding-3 TV-B3/TV-F1: purpose 3 and ACC-LTSPICE-001 claim bundle and exe identity checks the wrapper does not make (prefix match line 209; no exe SHA-256; log without version line passes).
- [Minor] finding-4 to finding-17 (see table).
ITEMS N/A: TV-D3 (class B), TV-F5 (first record), TV-G3, TV-G4, TV-H1; Rust-specific code items listed above
RE-RUN: CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py; exit 0; 29 tests, 18 passed, 11 skipped; same as run 2
MEASUREMENTS: size=1 record, 4 purposes, 29 tests, 12 fixture files, 334 LOC; turns=42; minutes=70; major=3; minor=14; unsafe_sites=0
```

Owner action needed before iteration 2: OA-TV014-1 (restore `CaptureAnalytics=false` by answering No once in the LTspice consent dialog; the reviewer did not touch the ini). Iteration 2 is a delta that verifies finding-1 to finding-3 on the fixed blobs and run 3; Minor findings not fixed by then become liens under rule C1 only after a first APPROVED verdict.

## Iteration 2: delta verification of finding-1 to finding-3 (Major) (2026-09-27)

**Scope (rule C1).** A delta that verifies the three Major fixes only. Products, frozen at `aa746f0` (rule C2) and each equal to the blob the brief names (`git rev-parse aa746f0:<path>`): wrapper `tools/ltspice-batch.sh` `64e1c723` (360 lines), test module `c75cb7b3` (35 cases), `known-answers.json` `8ec25d71`, new test double `fake-support/bin/wine` `acd2ec5c` (mode 100755), `rc-step-tran.net` `bd19be41` (unchanged), fixture tree `8feee9d0` (13 files), all from `c9d2c54`; TV-014 `6204bd78`, run 3 transcript `bc806dae`, TV README `98969f41` and lock `9aca88d3` from `aa746f0`; procedure `f9fea642` and `tools/README.md` `54f97c64` unchanged since iteration 1. At review time HEAD was `c827202`: every listed blob equals HEAD except the README (`87fb1e8c`) and the lock (`b45c8654`), which `c827202` (WP-PDR-08) changed on rows other than LTspice (`git diff aa746f0 HEAD` on both files: no LTspice or TV-014 line changed). The iteration 1 blobs are in the front matter of `3e9d30f`. The change was read as `git diff 102b93d4 64e1c723`, `git diff c4410447 c75cb7b3`, `git show c9d2c54 -- tools/tests/fixtures/ltspice/` and `git diff --word-diff b362395 aa746f0` on TV-014, README and lock. The iteration 1 checklist answers stand except where this section changes them.

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, TV-014, the wrapper, the tests or iteration 1 of this record, and edited no product file.

**Search first (charter section 11 rule 1).** One `grep -n "WP-PDR-07"` over the plan file (a known path) and one `ls` of the checklists directory ran before the search tool was loaded; recorded here as a deviation from the rule's order. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` then ran before every other manual search (queries: "INSP-038 tool validation TV-014 ltspice-batch review record iteration 1 findings"; "validate_docs peer review record findings table state values latest_iteration_section counts"). `grep -n` afterwards only pinned lines.

**Headless and bottle safety.** No LTspice process was started (`pgrep -fl LTspice`: none after the checks). The bottle ini was read only with `ls` and `iconv` (12:00 CDT: 420 bytes, modified 10:50, key count 0). Reviewer mutation runs used a scratch copy of wrapper blob `64e1c723` (hash re-checked with `git hash-object`) and a `git archive` copy of the fixture; every run either stopped at the identity check before LTspice (mode `-version`) or ran a test double in place of the bundle's `wine`.

### Verification of the Major findings

**finding-3 (identity checks): Verified.**

| Element of the iteration 1 fix | Result | Evidence |
|---|---|---|
| Bundle build compared exactly with the locked `26.0.2.1` | Yes | Wrapper lines 219 to 229: the prefix match is kept as a first check, then `must_equal "LTspice bundle build" "$BUNDLE" "$LOCK_BUNDLE"` with the constant `LOCK_BUNDLE="26.0.2.1"` (line 73), not taken from the environment. Reviewer mutation M1 (constant set to `26.0.2.2` in the scratch copy): exit 4, "LTspice bundle build is 26.0.2.1, expected 26.0.2.2" |
| `LTspice.exe` SHA-256 checked before each run | Yes | Lines 231 to 236: `shasum -a 256` of the bottle `LTspice.exe` against `LOCK_EXE_SHA256` (line 74, equal to TV-014 section 1 and run 3 part B `a94eb178...793f06`), for every mode including `-version`, after the lock is taken and before the precondition. A missing file exits 3. Mutation M2 (constant's last digit `6` to `7`): exit 4, "LTspice.exe SHA-256 is a94eb178...f06, expected ...f07" |
| A `-b` log with no version line fails | Yes | Lines 317 to 324: any first line other than "LTspice 26.0.2 for MacOS" now fails with exit 4 (another version) or exit 4 "not a version line"; an error log keeps its earlier exit 1 because `fail` keeps the first status and the failure-string check runs first (line 311). Mutation M3 (scratch wrapper with `INI` pointed at `ini-with-key.ini`, `CWHT_LTSPICE_SUPPORT=fake-support`): exit 4, "log first line is not a version line ... (got 'Circuit: ...')". Control with a double that writes "LTspice 26.0.2 for MacOS": exit 0, PASS; with "LTspice 26.0.3 for MacOS": exit 4 |
| Each check has a seeded fault | Yes, with finding-18 | `seeded_bundle_build` and `seeded_exe_sha256` (`InstallAndVersionTests`, pass without the bottle key; reviewer re-run 12:00: ok) and `seeded_no_version_line` (`OutputCheckTests`, skipped until the key is restored; exercised above by M3). The two identity faults seed the expected side through add-only hooks, so they do not detect removal of the locked comparison itself (finding-18) |
| Hooks cannot waive the locked values | Yes | `CWHT_LTSPICE_EXPECT_BUNDLE` and `CWHT_LTSPICE_EXPECT_EXE_SHA256` add a second `must_equal` after the locked one (lines 227 to 236); the test base class pops both (test lines 146 to 147). `CWHT_LTSPICE_SUPPORT` still skips the bundle check (iteration 1 finding-11, now stated in TV-014 limitation 9) but not the `LTspice.exe` check, which reads the bottle path, not the hook path |
| Record and scope match the code | Yes, with finding-19 | TV-014 purpose 3, the seeded-fault table, limitation 9 (Wine layer covered by the bundle build and part B) and ACC-LTSPICE-001 now name exactly what the wrapper checks. The scope statement names blob `64e1c723` "or the blob of the validation run if a later fix changes it" (finding-19) |

**finding-2 (`-ascii` known answer): Fixed, not yet verified.** The fix is present and correct by inspection: `test_ascii_raw_known_answer` runs `-ascii -b rc-step-tran.net`, parses the raw file with `read_ascii_raw` (rejects a `Binary:` section, requires `Variables:` and `Values:`, checks the point count and index order, accepts 8-bit or UTF-16LE headers) and compares V(out) at 1 ms, interpolated with `value_at` on |t|, with 0.6321206 V within 0.1 %. Reviewer recomputation: 1 - e^-1 = 0.63212056; with the deck's 1 us maximum step the linear interpolation error is below 1e-6 relative, well inside 0.1 %. `AsciiRawReaderTests` (2) pass in the reviewer re-run. The case itself is in `LTspiceRunTests` and was skipped in run 3 and in the reviewer re-run, so no result exists yet that LTspice 26.0.2 writes the raw file in the layout the reader accepts. Verification moves to run 4 with finding-1.

**finding-1 (no known-answer result): Open, blocked on the owner.** Run 3 (`c9d2c54`, 11:56, transcript `bc806dae`) is recorded truthfully in TV-014 section 4 as blocked: 35 run, 22 passed, 13 skipped, part D not run. Reviewer re-run at 12:00 CDT (`CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py`): exit 0, 35 run, OK (skipped=13), identical. The bottle ini is unchanged since 10:50 (key count 0). The fix needs owner action OA-TV014-1, then run 4 on the committed blobs with the TV-014 section 3 pass criterion (34 of 35 passed, only `test_bottle_without_key` skipped, part D as stated), then iteration 3 of this record. The run 3 transcript's closing line still reads "a pass needs exit 0 and no skipped test in part C", which differs from the section 3 criterion (the procedure blob `f9fea642` is unchanged; iteration 1 finding-5 covers the computed verdict).

### Reviewer re-runs (commands, exits)

| Command | Exit | Result |
|---|---|---|
| `CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py` | 0 | 35 run, 22 passed, 13 skipped (same as run 3) |
| `.venv/bin/python -m unittest discover -s tools/tests` | 1 | 461 run, failures=1 (`test_repository_exit_zero`, finding-17), skipped=13 |
| `.venv/bin/python tools/validate_docs.py` (before this record) | 1 | 65 passed, 1 failed: INSP-015 drift on README and lock (finding-17) |
| `bash <scratch>/w.sh -version` (blob `64e1c723`) | 3 | precondition refusal, LTspice not started |
| M1, M2, M3 and controls (above) | 4, 4, 4, 0, 4 | as expected |
| M4: locked bundle comparison line deleted, `CWHT_LTSPICE_EXPECT_BUNDLE=26.0.2.2` | 4 | the seeded case still passes without the locked check (finding-18) |
| M5: locked `LTspice.exe` comparison line deleted, `CWHT_LTSPICE_EXPECT_EXE_SHA256` = seeded hash | 4 | same (finding-18) |

### Findings (iteration 2 state)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-C5, TV-D1, TV-C2, TV-C4; R2 | TV-014 section 4 rows 3 and 4 | No known-answer result for the committed wrapper; run 3 blocked as runs 1 and 2 were (see above) | Open (blocked on OA-TV014-1) | Pending | |
| finding-2 | reviewer | Major | TV-B3, TV-C2 | `test_ltspice_batch.py` `test_ascii_raw_known_answer`; `known-answers.json` block `ascii` | `-ascii` known answer added and correct by inspection; not executed | Fixed (verification at run 4) | Pending | |
| finding-3 | reviewer | Major | TV-B3, TV-F1 | wrapper lines 71 to 74, 216 to 236, 317 to 324; TV-014 purpose 3, section 9 | Exact bundle build, `LTspice.exe` SHA-256 and version-line checks, each confirmed by reviewer mutation and seeded faults | Verified | Pending | |
| finding-4 | reviewer | Minor | TV-C2, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-5 | reviewer | Minor | TV-C1, TV-D1 | as iteration 1; run 3 closing line | Not re-checked (delta); the run 3 closing line shows the same prose-only criterion | Open | Pending | |
| finding-6 | reviewer | Minor | CK-CODE-C2 | wrapper lines 339 to 350 at `64e1c723` | Not re-checked (delta); `cp` status still unchecked | Open | Pending | |
| finding-7 | reviewer | Minor | TV-G1-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-8 | reviewer | Minor | TV-E1, TV-C2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-9 | reviewer | Minor | TV-E1, TV-G2-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-10 | reviewer | Minor | TV-E1, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-11 | reviewer | Minor | TV-F1, CK-CODE-G1 | wrapper provenance line; TV-014 limitation 9 | Limitation 9 now states that runs for the record are made without `CWHT_LTSPICE_SUPPORT`; the provenance line still records no override | Open | Pending | |
| finding-12 | reviewer | Minor | TV-F3, TV-D2 | `tools/toolchain.lock.md` section 5 TV-014 row at `9aca88d3` | Next step now reads "pending: run 4" (changed incidentally with the run 3 update) | Verified | Pending | |
| finding-13 | reviewer | Minor | TV-A2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-14 | reviewer | Minor | TV-F4, R5 | as iteration 1 | Not re-checked (delta); OA-TV014-1 is still named without steps in TV-014 | Open | Pending | |
| finding-15 | reviewer | Minor | TV-G2-2, TV-A6 | procedure `f9fea642` part D | Not re-checked (delta); procedure unchanged | Open | Pending | |
| finding-16 | reviewer | Minor | TV-C1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-17 | reviewer | Minor | R3, TV-F3 | INSP-015 record drift | Still failing at HEAD `c827202` (README `87fb1e8c`, lock `b45c8654`) | Open | Pending | |
| <a id="finding-18"></a>finding-18 | reviewer | Minor | TV-C2 (seeded fault), CK-CODE-H1 | `test_ltspice_batch.py` `test_bundle_build_other_than_lock`, `test_exe_sha256_other_than_lock`; `known-answers.json` `locked_bundle`, `locked_exe_sha256` | The two identity seeded faults exercise the add-only hooks, not the locked comparison: with the `LOCK_BUNDLE` or `LOCK_EXE_SHA256` comparison line deleted, both cases still exit 4 and pass (mutations M4, M5), and no test reads `locked_bundle` or `locked_exe_sha256` from the fixture. A later edit that drops or changes a locked constant would pass the known answer (only positive runs at the right identities would still pass, which a dropped check does not disturb). Fix: add a case that asserts the wrapper constants equal `locked_bundle` and `locked_exe_sha256`, and a mutation case that runs a temporary copy of the wrapper with a changed constant and expects exit 4 (as M1 and M2 did) | Open | Pending | |
| <a id="finding-19"></a>finding-19 | reviewer | Minor | TV-F1 | TV-014 section 9 scope statement (line 130) | ACC-LTSPICE-001 names blob `64e1c723` "or the blob of the validation run if a later fix changes it", so the proposed scope does not name one fixed blob. Fix: when run 4 is recorded, state the single blob of the validation run in the scope statement and drop the alternative | Open | Pending | |

### Checklist items changed at this iteration

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| TV-B3 | Yes | Purpose 1 `-ascii` has a known answer (finding-2 Fixed); purpose 3 claims only checks the wrapper makes (finding-3 Verified) |
| TV-C2 | No | Seeded faults now cover every purpose 3 identity clause, but the LTspice cases have still not run (finding-1) and the identity faults do not detect removal of the locked comparison (finding-18) |
| TV-D2 | Yes | Lock section 1.1 records run 3 with its commit; section 5 names run 4 (finding-12 Verified) |
| TV-F1 | No (Minor) | Scope now matches the checks (finding-3 Verified); open Minors finding-11 and finding-19 |
| TV-G1-2 | No (Minor) | Exit 4 has three new passing or reviewer-executed cases; 0, 1, 124 still not run (finding-1); 130 undocumented (finding-7) |

### Cross items

X-1 to X-7 of iteration 1 stand. X-5: the tool validation template is still not on `main` at `c827202` (`git rev-parse HEAD:docs/templates/peer-review-checklist-tool-validation.md` fails), so the `checklist` field keeps the code checklist. X-7 (SA pair) is unchanged: not required by 07 section 2.1.1 for a "Neither" tool without `unsafe`; the lead SE's decision on it is still open.

### Verdict (iteration 2)

```
VERDICT: NEEDS CHANGES
PRODUCT: TV-014 at aa746f054914d93124dbe3c516848bc9af60c89b (wrapper blob 64e1c723, test module c75cb7b3, fixture tree 8feee9d0)
FINDINGS:
- [Major] finding-1 Open: no known-answer result; run 3 and the reviewer re-run blocked by the bottle precondition (OA-TV014-1).
- [Major] finding-2 Fixed, not verified: -ascii known answer present and correct by inspection; executes at run 4.
- [Major] finding-3 Verified: exact bundle build, LTspice.exe SHA-256 and log version-line checks confirmed by mutation (M1 to M3).
- [Minor] finding-18 (new): identity seeded faults do not detect removal of the locked comparison (M4, M5).
- [Minor] finding-19 (new): ACC-LTSPICE-001 scope names an alternative blob.
- [Minor] finding-12 Verified; finding-4 to finding-11 and finding-13 to finding-17 carried Open (not re-checked, rule C1).
RE-RUN: CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py; exit 0; 35 run, 22 passed, 13 skipped; same as run 3
MEASUREMENTS: size=1 record, 4 purposes, 35 tests, 13 fixture files, 360 LOC; turns=24; minutes=45; major=3; minor=16; unsafe_sites=0
```

Next: owner action OA-TV014-1 (answer No once in the LTspice consent dialog, then confirm key count 1 with the `iconv` command), then run 4 by the author, then iteration 3 of this record (a delta on finding-1 and finding-2). Iteration 3 is the last before escalation to the owner (rule C1; 07 section 10.2). Minor findings become liens due at the CDR readiness declaration only after a first APPROVED verdict.

## Iteration 3: delta on finding-1 and finding-2 (Major), no product change (2026-09-27)

**Scope (rule C1).** The delta that iteration 2 named: verify finding-1 and finding-2 on run 4. The author returned no change and no commit (author summary of 2026-09-27: finding-1 blocked on OA-TV014-1, finding-2 verifiable only by run 4, no Minor touched under rule C1). Products at HEAD `dfde624`, each checked with `git rev-parse HEAD:<path>` against `git rev-parse aa746f0:<path>`: wrapper `64e1c723`, test module `c75cb7b3`, `known-answers.json` `8ec25d71`, `fake-support/bin/wine` `acd2ec5c`, `rc-step-tran.net` `bd19be41`, fixture tree `8feee9d0`, TV-014 `6204bd78`, procedure `f9fea642`, run 3 transcript `bc806dae` and `tools/README.md` `54f97c64` are equal at both commits. The TV README (`87fb1e8c`) and the lock (`b45c8654`) differ from `aa746f0` only through `c827202` (WP-PDR-08); `git diff aa746f0 HEAD` on both files changes no line that names LTspice or TV-014. `git diff --stat aa746f0 HEAD` over the wrapper, the test module, the fixture tree, TV-014 and the evidence directory shows only two WP-PDR-08 evidence files (`measurements-2026-09-27-r3.log.txt`, `rust-tv-2026-09-27-r3.log.txt`); no LTspice run 4 transcript exists. The freeze therefore still holds (rule C2) and this iteration reviews the same content as iteration 2.

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, TV-014, the wrapper, the tests or iterations 1 and 2 of this record, and edited no product file.

**Search first (charter section 11 rule 1).** One `grep -n "WP-PDR-07"` over the plan file (a known path) ran before the search tool was loaded; recorded here as a deviation from the rule's order, as in iteration 2. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` then ran before every other manual search (query: "INSP-038 iteration 2 TV-014 finding-1 known answer run 4 OA-TV014-1"). `grep -n` afterwards only pinned lines in known files.

**Headless and bottle safety.** No LTspice process was started (`pgrep -fl LTspice`: none). The bottle ini was read only with `ls` and `iconv` at 12:07 CDT: 420 bytes, modified 10:50, `iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | grep -c '^CaptureAnalytics=false$'` returns 0. The reviewer did not edit the ini (ADR-018; 08 briefing: the key is owner-ratified).

### Verification of the Major findings

| Finding | Iteration 3 state | Evidence |
|---|---|---|
| finding-1 | **Open, not fixed.** Escalated to the owner (below) | No run 4 exists. The bottle precondition still fails (key count 0), so run 4 cannot be made headless. Reviewer re-run at 12:08 CDT (`CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py`): exit 0, 35 run, OK (skipped=13), identical to run 3 and to the iteration 2 re-run. The author's decision not to edit the ini or start the GUI is correct: 08 section 5 (LTspice command line) says to stop and report when the key check fails, and charter section 11 rule 8 forbids GUI steps by an agent |
| finding-2 | **Fixed, not verified.** Carried to run 4 | `test_ascii_raw_known_answer` (in `LTspiceRunTests`) is still skipped by the precondition; the fix itself is unchanged (`c75cb7b3`, `8ec25d71`) and stays correct by the iteration 2 inspection. `AsciiRawReaderTests` (2) pass in the re-run |
| finding-3 | Verified (iteration 2) | Products unchanged, so the iteration 2 mutations M1 to M3 stand |

### Escalation to the owner (rule C1; 07 section 10.2 and section 3.4 phase 3)

This is the third author-review iteration of INSP-038 and one Major (finding-1) remains Open, with a second (finding-2) unverifiable for the same reason. Rule C1 allows no fourth iteration without the owner. The block is not an author defect: every case that needs LTspice is gated on the bottle key `CaptureAnalytics=false`, which only the owner can restore (OA-TV014-1). The reviewer asks the owner to choose one of:

1. **Restore and authorize one more delta (recommended).** The owner does OA-TV014-1 (open LTspice once, answer No to the analytics consent dialog, quit), then confirms the key count is 1 with the `iconv` command above. The owner then authorizes iteration 4 of INSP-038 as a delta on finding-1 and finding-2 only. The author makes run 4 with the TV-014 section 3 procedure on the frozen blobs: pass criterion 34 of 35 passed, only `test_bottle_without_key` skipped, part D run as stated. The result goes into TV-014 section 4 and lock section 1.1, and the scope statement of ACC-LTSPICE-001 then names one blob (finding-19).
2. **Hold TV-014 unaccredited.** WP-PDR-19 to 26 and 28 then cite no LTspice result as evidence until the owner acts (05 section 9.1; plan WP-PDR-07 "Blocks"). OD-24b at B0 is deferred.

TV-014 cannot be accredited (OD-24b) until finding-1 is Verified; the record gives the owner no basis to accredit it on the current evidence.

### Findings (iteration 3 state)

Only the state of finding-1 and finding-2 was re-checked; every other row is as in iteration 2 (rule C1: no Minor is re-checked before a first APPROVED verdict).

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-C5, TV-D1, TV-C2, TV-C4; R2 | TV-014 section 4 rows 3 and 4 | No known-answer result for the committed wrapper; no run 4; reviewer re-run at 12:08 identical to run 3 (key count 0) | Open (escalated to the owner; blocked on OA-TV014-1) | Pending | |
| finding-2 | reviewer | Major | TV-B3, TV-C2 | `test_ltspice_batch.py` `test_ascii_raw_known_answer`; `known-answers.json` block `ascii` | `-ascii` known answer present and correct by inspection; still not executed | Fixed (verification at run 4) | Pending | |
| finding-3 | reviewer | Major | TV-B3, TV-F1 | wrapper lines 71 to 74, 216 to 236, 317 to 324 | As iteration 2 | Verified | Pending | |
| finding-4 | reviewer | Minor | TV-C2, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-5 | reviewer | Minor | TV-C1, TV-D1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-6 | reviewer | Minor | CK-CODE-C2 | wrapper lines 339 to 350 at `64e1c723` | Not re-checked (delta) | Open | Pending | |
| finding-7 | reviewer | Minor | TV-G1-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-8 | reviewer | Minor | TV-E1, TV-C2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-9 | reviewer | Minor | TV-E1, TV-G2-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-10 | reviewer | Minor | TV-E1, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-11 | reviewer | Minor | TV-F1, CK-CODE-G1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-12 | reviewer | Minor | TV-F3, TV-D2 | lock section 5 TV-014 row | As iteration 2 (the TV-014 row is unchanged in `b45c8654`) | Verified | Pending | |
| finding-13 | reviewer | Minor | TV-A2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-14 | reviewer | Minor | TV-F4, R5 | as iteration 1 | Not re-checked (delta); the steps of OA-TV014-1 are written in the escalation above but not yet in TV-014 | Open | Pending | |
| finding-15 | reviewer | Minor | TV-G2-2, TV-A6 | procedure `f9fea642` part D | Not re-checked (delta) | Open | Pending | |
| finding-16 | reviewer | Minor | TV-C1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-17 | reviewer | Minor | R3, TV-F3 | INSP-015 record drift | Still failing at HEAD `dfde624` (see re-runs) | Open | Pending | |
| finding-18 | reviewer | Minor | TV-C2, CK-CODE-H1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-19 | reviewer | Minor | TV-F1 | TV-014 section 9 scope statement | Not re-checked (delta); fix due with run 4 | Open | Pending | |

### Reviewer re-runs (commands, exits)

| Command | Exit | Result |
|---|---|---|
| `CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py` | 0 | 35 run, 22 passed, 13 skipped (same as run 3) |
| `.venv/bin/python tools/validate_docs.py` (with this record) | 1 | 65 passed, 1 failed: this record PASS; the failure is INSP-015 drift on the README and lock (finding-17), not attributable to this record |

### Cross items

X-1 to X-7 stand. X-5: `git rev-parse HEAD:docs/templates/peer-review-checklist-tool-validation.md` still fails at `dfde624`, so the `checklist` field keeps the code checklist. X-7 (SA pair): not required by 07 section 2.1.1 for a "Neither" tool without `unsafe`; the lead SE's decision is still open. X-8 (new): OA-TV014-1 is not in the plan section 6 owner-action list or in `docs/plan/status/status-2026-09-27.md`; the lead SE should add it to the B0 owner session with OD-24b.

### Verdict (iteration 3)

```
VERDICT: NEEDS CHANGES (escalated to the owner, rule C1)
PRODUCT: TV-014 at dfde62480a56d8258742d47715af5b1ceaf43c19 (wrapper blob 64e1c723, test module c75cb7b3, fixture tree 8feee9d0; content unchanged since aa746f0)
FINDINGS:
- [Major] finding-1 Open: no run 4; bottle key count 0 at 12:07; reviewer re-run 35 run, 22 passed, 13 skipped.
- [Major] finding-2 Fixed, not verified: executes only at run 4.
- [Major] finding-3 Verified (iteration 2).
- [Minor] finding-12 Verified; finding-4 to finding-11 and finding-13 to finding-19 Open (not re-checked, rule C1).
RE-RUN: CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py; exit 0; 35 run, 22 passed, 13 skipped; same as run 3
MEASUREMENTS: size=1 record, 4 purposes, 35 tests, 13 fixture files, 360 LOC; turns=12; minutes=20; major=3; minor=16; unsafe_sites=0
```

Next: the owner decides between the two options of the escalation above. With option 1, iteration 4 is a delta on finding-1 and finding-2 on run 4.

## Iteration 3 re-issue 1: the owner-authorized iteration 4 (rule C1 route (1)), delta on finding-1 and finding-2 on run 4 (2026-09-27)

**Authority and scope (rule C1).** The owner performed OA-TV014-1 ("I did the LT spice step now", status note `docs/plan/status/status-2026-09-27.md` section 7), which the status note and TV-014 section 8 read as route (1) of the iteration 3 escalation: run 4 on the frozen blobs, then this delta on finding-1 and finding-2 only. TV-014 and the status note call it iteration 4; the front matter keeps `iteration: 3` because the record schema allows at most 3 (precedent INSP-009, "iteration 3 re-issue 1"). No Minor is re-checked (rule C1); one new Major is raised because it is the cause of finding-1 staying Open.

**Products (rule C2).** HEAD `d9c7f69` (the author's run 4 commit). Wrapper `64e1c723`, test module `c75cb7b3`, `known-answers.json` `8ec25d71`, `fake-support/bin/wine` `acd2ec5c`, fixture tree `8feee9d0`, procedure `f9fea642` and run 3 transcript `bc806dae` equal the iteration 2 and 3 blobs (`git rev-parse HEAD:<path>`; `git hash-object` of the working-tree wrapper and test module gives the same values; `git status` shows no change under `tools/`). Changed by `d9c7f69`: TV-014 `c0c0edf8`, lock `83bc0520`, new run 4 transcript `a8c7270e`; the TV README (`763f1082`) and `tools/README.md` (`053e6df2`) changed through other work packages since iteration 3 and are carried in `product_files` for the drift rule only.

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, TV-014, the wrapper, the tests, run 4 or iterations 1 to 3 of this record, and edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-038 TV-014 LTspice batch wrapper run 4 finding-1 finding-2"; "validate_docs peer review record findings counts latest iteration section front matter check"). `grep -n` and `git grep -n` afterwards only pinned lines in known files.

**Headless and bottle safety.** LTspice was reached only through `tools/ltspice-batch.sh` (the lock section 1.2 command); no GUI, AppleScript, System Events or screen capture; no process was stopped or signalled by the reviewer. Key check before the reviewer runs (13:35:40 and 13:37:06 CDT): bottle `LTspice.ini` 11620 bytes, modified 13:19, SHA-256 `efdb1839...8cf2` (equal to the run 4 post-run value), line 3 `CaptureAnalytics=false`, `iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | grep -c '^CaptureAnalytics=false$'` = 1, no `LTspice.exe` process. After the runs (13:39:09): the same size, time, line 3 and count 1, no `LTspice.exe` process. No reviewer run started LTspice (every one stopped at the lock, below), so the ini was not touched by this review.

### Verification of the Major findings

| Finding | Iteration 4 state | Evidence |
|---|---|---|
| finding-2 | **Verified** (on the run 4 transcript; the reviewer re-run could not reach LTspice) | Run 4 part C (`a8c7270e`, 13:17 to 13:19, part A identities equal to the frozen blobs, part B key count 1): `test_ascii_raw_known_answer ... ok`. The case runs `-ascii -b rc-step-tran.net`, parses the raw file with `read_ascii_raw` (rejects `Binary:`) and compares V(out)(1 ms) with 1 - e^-1 = 0.6321206 V within 0.1 % (analytic value recomputed: 0.63212056); `AsciiRawReaderTests` 2 ok in run 4 and in the reviewer re-run. So LTspice 26.0.2 writes an ASCII raw file the reader accepts and the value is within the criterion on the frozen blobs. TV-014 section 8 permits the transcript as the reviewer's evidence; the reviewer re-run of the same case was blocked by the lock (finding-20) |
| finding-1 | **Open (partly addressed)** | Run 4 is the first result for blob `64e1c723` with LTspice running: 33 of 35 passed, including every `LTspiceRunTests` case (AC f(-3 dB) within 1 %, transient, include, `-ascii`, netlist without `NC_`, seeded deck error exit 1, seeded floating net, output directory, stale outputs, extra ini, `-version` 26.0.2), `OutputCheckTests` 1 (log without version line, exit 4), `PreconditionTests` 3 on the fixture inis and `TimeoutGuardTests` 1 (exit 124, no survivor of this run). It is **not a pass** of the TV-014 section 3 criterion: `LockTests.test_busy_when_lock_held` skipped (not a permitted skip) and part D not completed (bare command `lockf` exit 75 after 600 s; wrapper exit 5). TV-014 section 4 row 4 and section 4.1 finding 5 record this truthfully. Reviewer re-run at 13:37:27 to 13:39:09 (below): 35 run, 13 passed, 20 failed, 2 skipped, every failure exit 5 "busy", so the reviewer could not reproduce any LTspice case. The lock stays held by the seven processes of TV-014 finding 5 (reviewer `lsof` 13:35: PIDs 10645, 10647, 10655, 10659, 10669, 10709, 10727, each `10w` on the lock inode 61434187; `lockf -s -t 0` exit 75). A passing run needs finding-20 fixed first (see below), which changes the wrapper blob and re-opens the validation (TV-014 section 7) |
| finding-3 | Verified (iteration 2) | Wrapper blob unchanged. Run 4 also passed `test_bundle_build_other_than_lock`, `test_exe_sha256_other_than_lock` and `test_log_without_version_line` with LTspice installed and the key present |

### New finding: the cause of TV-014 finding 5 is a wrapper defect

TV-014 section 4.1 finding 5 says how the lock descriptor reached the Wine services "is not established". The reviewer established it on a scratch script, with no LTspice run. `/bin/bash` 3.2.57, which runs the wrapper, applies the redirection `9>&-` of `exec "$WINE" ... 9>&-` (wrapper line 254) by first saving fd 9 to fd 10, and the saved descriptor is not close-on-exec, so the exec'd program inherits the lock file as fd 10. Script: `exec 9>"$D/lk"; ( cd "$D" && exec /bin/sh -c 'lsof -p $$ -a -d 0-20' 9>&- ) > "$D/.stdout" 2> "$D/.stderr" &`: the child holds `10w` on the inode of `$D/lk`. With the close done as its own command (`( exec 9>&-; cd "$D" && exec /bin/sh -c ... )`) the child holds only fds 0 to 2. So every `wine` child of the wrapper holds the lock (fd 10 is a duplicate of fd 9 and shares its flock), and any Wine service it starts (`services.exe` and the rest, which outlive the run: sets from 2026-09-25 are still running) keeps it after the wrapper exits. This matches every observation of finding 5: the holders have fd 10 (not 9), their fd 2 was the `.stderr` of a wrapper run directory, and they started during the run 4 LTspice cases. The header claim at lines 205 and 206 ("The lock is released by the kernel when this shell exits, so a killed wrapper leaves no stale lock") is false whenever the run starts Wine services.

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-20"></a>finding-20 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | `tools/ltspice-batch.sh` blob `64e1c723` line 254 and header lines 204 to 206; TV-014 section 4.1 finding 5, limitation 5; lock section 1.4 finding 15 | The wrapper leaks its lock to LTspice: bash 3.2 saves fd 9 to fd 10 without close-on-exec when it applies `9>&-` to `exec`, so `wine`, `LTspice.exe` and every Wine service they start inherit the lock as fd 10. Wine services outlive the run, so after the first run that starts them the lock is never released and every later wrapper run exits 5 (run 4 part D; the reviewer re-run, 20 of 20 lock-taking cases). Run 5 on this blob would hit it again as soon as its first LTspice case starts a new set of services, so finding-1 cannot be closed on blob `64e1c723`. Fix: close fd 9 as a separate command in the subshell (`( exec 9>&-; cd "$RUN" && exec "$WINE" ... )`; reviewer check above), add a known answer with the `fake-support` wine double that fails when the child holds any descriptor on the lock file (for example the double lists `/dev/fd` or runs `lsof -p $$` into its log and the test asserts no lock inode), correct the header lines 204 to 206 and TV-014 finding 5 and lock finding 15 with the cause, and re-validate (TV-014 section 7; ACC-LTSPICE-001 re-issued with the new blob). The owner or lead SE ends the seven holders (PIDs 10645 to 10727) before run 5; the reviewer did not, as they are not the reviewer's processes | Open | Pending | |

### Other observations of this delta (not findings; for the author and lead SE)

1. The `test_busy_when_lock_held` skip and the part C contention came from unit-test suites of other sessions running `unittest discover -s tools/tests` (which includes the LTspice module) during run 4; the reviewer saw four such suites still waiting on the lock at 13:35 (PIDs 4723, 11530, 16852, 21448, each with a queued wrapper and `lockf` child). Run 5 needs a window with no other session running the repository suite, or the repository suite must not run the LTspice cases by default (a lead SE decision; related to finding-5).
2. Seven orphaned `/usr/bin/lockf -s -t 600 9` helpers (parent `launchd`: PIDs 20503, 21030, 21243, 24640, 24724, 25163, 25432) held waiting descriptors at 13:35. They end after their 600 s wait and do not hold the lock, but they show that a killed wrapper leaves its `lockf` child behind (part of the finding-20 fix, or an NCR note).
3. The run 4 procedure still prints "a pass needs exit 0 and no skipped test in part C", which differs from the TV-014 section 3 criterion (finding-5, carried).
4. TV-014 finding 19 fix (scope names one blob) is present in `c0c0edf8`; it will be re-issued with the finding-20 blob, so it is marked Fixed, not Verified.

### Reviewer re-runs (commands, exits)

| Command | Exit | Result |
|---|---|---|
| `/usr/bin/lockf -s -t 0 "$(getconf DARWIN_USER_TEMP_DIR)cwht-ltspice.lock" true` (13:35:40) | 75 | lock held; `lsof` names the seven Wine processes (fd 10w) and waiting wrappers and helpers only |
| `CWHT_LTSPICE_LOCK_WAIT=5 tools/ltspice-batch.sh -version` (13:37:06) | 5 | "busy: another LTspice run held the lock for more than 5 s"; LTspice not started |
| `CWHT_LTSPICE_LOCK_WAIT=5 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py` (13:37:27 to 13:39:09; the module passes `CWHT_LTSPICE_LOCK_WAIT` through to the wrapper, so each lock-taking case waits 5 s instead of 600 s) | 1 | 35 run, 13 passed (`UsageTests` 6, `HygieneTests` 5, `AsciiRawReaderTests` 2), 20 failed, 2 skipped (`test_busy_when_lock_held` "another LTspice run holds the lock now", `test_bottle_without_key` permitted); a single failing case re-run from `tools/tests` shows `AssertionError: 5 != 0 ... busy: another LTspice run held the lock for more than 2 s` |
| bash 3.2 descriptor check on a scratch file (defect and fix, above) | 0 | child holds `10w` on the lock inode with `exec ... 9>&-`; only fds 0 to 2 with `exec 9>&-;` first |
| `.venv/bin/python tools/validate_docs.py` (with this record) | 1 | this record PASS; the 8 failures are other records (`cm-plan-05-software-assurance`, `configuration-status`, `lessons-learned`, `adrs-001-to-025`, `process-02-requirements-and-traceability`, `tool-validation-tv-001-to-tv-010`, `trade-studies-ts-001-ts-002`, `trade-study-ts-002-software-assurance`: record drift after other work packages), present before this record was edited and not attributable to it |

### Findings (iteration 4 state)

Only finding-1, finding-2 and the new finding-20 were checked; every other row is as in iteration 3 (rule C1).

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-C5, TV-D1, TV-C2, TV-C4; R2 | TV-014 section 4 row 4; run 4 transcript `a8c7270e` | Run 4: every LTspice case passed but the busy-lock case skipped and part D did not complete; reviewer re-run blocked (exit 5) by finding-20 | Open (needs finding-20 fixed, then a passing run on the new blob) | Pending | |
| finding-2 | reviewer | Major | TV-B3, TV-C2 | `test_ascii_raw_known_answer`; `known-answers.json` block `ascii` | `-ascii -b` known answer passed in run 4 on the frozen blobs | Verified | Pending | |
| finding-3 | reviewer | Major | TV-B3, TV-F1 | wrapper lines 71 to 74, 216 to 236, 317 to 324 | As iteration 2 | Verified | Pending | |
| finding-4 | reviewer | Minor | TV-C2, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-5 | reviewer | Minor | TV-C1, TV-D1 | as iteration 2; run 4 closing line | Not re-checked (delta) | Open | Pending | |
| finding-6 | reviewer | Minor | CK-CODE-C2 | wrapper lines 339 to 350 at `64e1c723` | Not re-checked (delta) | Open | Pending | |
| finding-7 | reviewer | Minor | TV-G1-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-8 | reviewer | Minor | TV-E1, TV-C2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-9 | reviewer | Minor | TV-E1, TV-G2-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-10 | reviewer | Minor | TV-E1, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-11 | reviewer | Minor | TV-F1, CK-CODE-G1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-12 | reviewer | Minor | TV-F3, TV-D2 | lock section 5 TV-014 row | As iteration 2 | Verified | Pending | |
| finding-13 | reviewer | Minor | TV-A2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-14 | reviewer | Minor | TV-F4, R5 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-15 | reviewer | Minor | TV-G2-2, TV-A6 | procedure `f9fea642` part D | Not re-checked (delta) | Open | Pending | |
| finding-16 | reviewer | Minor | TV-C1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-17 | reviewer | Minor | R3, TV-F3 | INSP-015 record drift | Not re-checked (delta) | Open | Pending | |
| finding-18 | reviewer | Minor | TV-C2, CK-CODE-H1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-19 | reviewer | Minor | TV-F1 | TV-014 section 9 scope statement at `c0c0edf8` | One blob named (`64e1c723`); to be re-issued with the finding-20 blob | Fixed (`d9c7f69`), not verified | Pending | |
| finding-20 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | wrapper line 254, header lines 204 to 206 | Lock descriptor leaked to Wine as fd 10 (see above) | Open | Pending | |

### Escalation (rule C1)

This was the one extra delta the owner authorized, and two Majors are Open after it (finding-1, and finding-20, which blocks it). Rule C1 allows no further iteration without the owner. The reviewer asks the owner to choose:

1. **Fix and re-validate (recommended).** The author fixes finding-20 (one-line change at line 254, a descriptor known answer with the test double, header and record text); the owner or lead SE ends the seven holders PIDs 10645 to 10727 (they are Wine service processes with no `LTspice.exe` and no `wineserver`, so they do not write the ini); run 5 on the new blob in a window with no other session running the repository suite, with the TV-014 section 3 criterion; then one more delta of this record on finding-1 and finding-20.
2. **Hold TV-014 unaccredited** (as iteration 3 option 2): WP-PDR-19 to 26 and 28 cite no LTspice result as evidence; OD-24b deferred.

TV-014 cannot be accredited (OD-24b) on the current evidence. Minor findings become liens only after a first APPROVED verdict, so none is a lien yet.

### Verdict (iteration 4, recorded as iteration 3 re-issue 1)

```
VERDICT: NEEDS CHANGES (escalated to the owner again, rule C1)
PRODUCT: TV-014 at d9c7f698f16064249bb6ab9e93dfefa8a2c18be8 (wrapper blob 64e1c723, test module c75cb7b3, fixture tree 8feee9d0; run 4 transcript a8c7270e)
FINDINGS:
- [Major] finding-1 Open: run 4 33 of 35 passed with every LTspice case, but busy-lock skipped and part D not completed; reviewer re-run 13 passed, 20 failed (exit 5, lock held).
- [Major] finding-2 Verified: test_ascii_raw_known_answer passed in run 4 on the frozen blobs.
- [Major] finding-3 Verified (iteration 2).
- [Major] finding-20 (new) Open: wrapper line 254 leaks the lock to Wine as fd 10 (bash 3.2 saved descriptor), so orphaned Wine services hold it forever; cause of TV-014 finding 5.
- [Minor] finding-19 Fixed, not verified; finding-12 Verified; finding-4 to finding-11 and finding-13 to finding-18 Open (not re-checked, rule C1).
RE-RUN: CWHT_LTSPICE_LOCK_WAIT=5 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py; exit 1; 35 run, 13 passed, 20 failed (busy, exit 5), 2 skipped
KEY CHECK: CaptureAnalytics=false on line 3, count 1, before (13:37:06) and after (13:39:09) the reviewer runs; ini unchanged (11620 bytes, 13:19)
MEASUREMENTS: size=1 record, 4 purposes, 35 tests, 13 fixture files, 360 LOC; turns=22; minutes=35; major=4; minor=16; unsafe_sites=0
```

## Iteration 3 re-issue 2: delta on finding-1 and finding-20 (Major) on run 5, with the session end and the test gating (2026-09-27)

**Authority and scope (rule C1).** The owner rejected route (2) of the iteration 3 re-issue 1 escalation and chose route (1): "No, that is unacceptable. We need to actually run the circuit simulations of the amplifiers and filters in LT Spice. So uh, how can we fix this?" (status note `docs/plan/status/status-2026-09-27.md` section 9, which records route (1) as fix, regression test, session end, test gating, run 5, then "the INSP-038 delta with a fix loop", then OD-24b). This delta verifies finding-1 and finding-20 and reviews the two changes made with them: the Wine session end (wrapper step 5a) and the `CWHT_LTSPICE_INTEGRATION=1` gating of the real-LTspice tests. The front matter keeps `iteration: 3` (schema maximum; precedent INSP-009). No Minor was re-checked except finding-15 and finding-19, whose fixes lie inside the reviewed change.

**Products (rule C2).** Commit `f47360a` (the author's run 5 record commit); every product blob is unchanged at HEAD `c0f5244` (`git rev-parse HEAD:<path>` equals each `product_files` blob; the commits after `f47360a` touch other work packages only). Wrapper `bdc4513f` (435 lines: the `b893382` launch-line fix `d5d38767` plus the `d1148c2` session end), test module `6c4e00e5` (43 cases), fixture tree `61c74693` (14 files, new `fake-support/bin/wineserver` `6d853df3`, changed `fake-support/bin/wine` `512487a9` and `known-answers.json` `61cdbf6d`), run 5 procedure `4f61ee30` and transcript `aa6d45ea`, TV-014 `af545923`, lock `00f60986`, TV README `dbce2cf3`, `tools/README.md` `59f86b76`. The working-tree wrapper and test module hash to the same blobs (`git hash-object`).

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, TV-014, the wrapper, the tests, the doubles, run 5, the finding-20 fix or any earlier iteration of this record, and edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-038 TV-014 ltspice-batch finding-20 lock descriptor inherited"; "finding severity definition Major Minor peer review rule C1 liens after APPROVED"). `grep -n` afterwards only pinned lines in known files.

**Headless and bottle safety.** LTspice was reached only through `tools/ltspice-batch.sh`; no GUI, AppleScript, System Events or screen capture; no process was signalled by the reviewer except the reviewer's own test-double processes in scratch copies (a `/bin/sleep` stand-in and the reviewer's bystander `/bin/sleep`, below). Before the first run (14:26:43 CDT): no `LTspice.exe`, no Wine or wineserver process (`pgrep -fl 'LTspice|wine'`: none), no process of the bottle's Wine session (the test module's `session_pids(BOTTLE)`: `[]`), no other session running `unittest` or the wrapper, lock free. Key check `iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | grep -c '^CaptureAnalytics=false$'` = 1 with line 3 `CaptureAnalytics=false` at 14:26:43 (ini 12414 bytes, modified 14:20), 14:29:30 and 14:29:51 (before and after the default suite), 14:30:20 (before the integration run), 14:32:38 (after it; ini 12418 bytes, modified 14:31: LTspice rewrote its recent-file list, key kept), 14:33:27 and 14:33:50 (before and after the direct wrapper runs; ini 12416 bytes, modified 14:33). Deviation: the first lock probe (14:26:43) was `lockf -s -t 0 <lock> true` without `-k`, which removes the lock file after the command; the lock was free (exit 0, no holder), so no run was affected and the next wrapper run re-created the file; every later probe used `-k`.

### Verification of the Major findings

| Finding | State | Evidence |
|---|---|---|
| finding-1 | **Verified** | Run 5 (`aa6d45ea`, 14:19:26 to 14:22, HEAD `d1148c2`, part A: wrapper `bdc4513f`, test module `6c4e00e5`, fixture tree `61c74693` "unchanged from HEAD", 0 fixture files differing) meets every clause of the TV-014 section 3 pass criterion: part C exit 0, 43 run, 42 passed, the one skip `test_bottle_without_key` (permitted), `LockTests.test_busy_when_lock_held` ran and passed; part D wrapper exit 0 on a deck at a 262-character Windows path with `.raw` beside the deck; part E no bottle-session process, no `LTspice.exe` and only the part E `lockf` on the lock file 10 s after the last run, lock free afterwards; part F exit 1; key count 1 in part B and after parts C, D and E. **Reviewer reproduction:** `CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py` (14:30:20 to 14:32:38): exit 0, 43 run in 137.6 s, 42 passed, 1 skipped (`test_bottle_without_key`, permitted); every `LTspiceRunTests` case (AC f(-3 dB) within 1 %, transient, include, `-ascii`, netlist, seeded deck error, floating net, output directory, stale outputs, extra ini, version), `WineSessionIntegrationTests`, `TimeoutGuardTests` and the busy-lock case passed. Direct wrapper runs on scratch copies of the fixture (14:33:27 to 14:33:40): `-b rc-lowpass.asc` exit 0 PASS (the RC low-pass filter, `f3db ... AT 999.999642341`), `-b rc-step-tran.net` exit 0 PASS (`vtau` 0.632120367773 V, `thalf` 0.693147653 ms), `-b rc-seeded-error.net` exit 1 ("More than one analysis specified."); each printed "Wine session of the bottle ended (wineserver -k), no process of it left". Analytic answers recomputed: 1/(2 pi 1 k 159.155 nF) = 999.99964 Hz (LTspice error -9.5e-11), 1 - e^-1 = 0.63212056 V (error -3.0e-7), 1 ms ln 2 = 0.69314718 ms (error 6.8e-7), each inside its criterion (1 %, 0.1 %, 0.1 %) |
| finding-20 | **Verified** | Code: wrapper line 327 `( exec 9>&-; cd "$RUN" && exec "$WINE" ... ) > ... &`, the close is its own command, as the iteration 3 re-issue 1 fix asked; header step 5 and the section 2 comment corrected (the header lines 204 to 206 claim now holds). TV-014 finding 5 and lock section 1.4 finding 15 name the cause. **Regression case on the old blob (reviewer, scratch copies, test doubles only, 14:27:30):** test module `6c4e00e5` and fixture tree `61c74693` with the wrapper of `b893382^` (`8abb467`, blob `64e1c723`, `git show` into the copy, `git hash-object` rechecked): `test_child_holds_no_lock_descriptor` FAIL, "the wine child holds the lock file open" (the double's PID in the lock holders); with the `b893382` wrapper (`d5d38767`) and with `bdc4513f`: ok. A direct run of each wrapper with `CWHT_FAKE_WINE_FDLOG` shows why: on `64e1c723` both the double and its stand-in service hold `f10` on `cwht-ltspice.lock` (the bash 3.2 saved descriptor); on `bdc4513f` the lock holders are the wrapper and one short-lived wrapper child, and neither the double nor the service has a descriptor on the lock file. So the test fails on the defect and passes on the fix, and it tests the real old blob, not only the reconstructed line of run 5 part F. After each case the lock was free (`lockf -k -s -t 0` exit 0) and no stand-in survived (the test's tearDown SIGKILLs it). The lock stayed free throughout this review (no stale holder) |

### Review of the session end (step 5a) and the test gating

**Does the default suite ever start the real LTspice? No.** By code: without `CWHT_LTSPICE_INTEGRATION=1` the only cases that launch anything are `OutputCheckTests` and `WineSessionDoubleTests`, and both set `CWHT_LTSPICE_SUPPORT` to the fixture's `fake-support`, so `WINE`, `WINESERVER` and `PREFIX` are the doubles and `fake-support/prefix` (wrapper lines 80 to 88); every other case that runs the wrapper on the real bundle stops before step 5 (usage and hygiene exit 2, identity exit 4, not-installed and precondition exit 3, busy exit 5). By observation: the default suite (`env -u CWHT_LTSPICE_INTEGRATION -u CWHT_LTSPICE_SLOW .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -v`, 14:29:30, exit 0, 43 run in 21.1 s, 29 passed, 14 skipped, each integration skip with its reason) was sampled every 0.2 s for `LTspice.exe`, the bundle's `wine`, `wineserver` and the Wine service names: the only hits were the wrapper's `shasum -a 256 .../LTspice.exe` (step 3) and the test's simulated foreign process whose argument is `C:\Program Files\ADI\LTspice\LTspice.exe`; no Wine process ran. Residual exposure (observation, not a finding): the real-bundle cases rely on their check firing before the launch; a regression in one of those checks would make the default suite launch the real LTspice, which the case would then report as a failure.

**Does the session end touch a process it did not start? Yes, in one path (finding-21).** What holds: `wineserver -k` is sent with `WINEPREFIX` set to the ltspice bottle (or the double's prefix under `CWHT_LTSPICE_SUPPORT`, so no test double reaches the real bottle); it is skipped when a process of the session existed at the launch (`SESSION_BEFORE`) or an `LTspice.exe` not naming this run's directory is open; it runs at most once (`SESSION_DONE`), after the launch only (`LAUNCHED`), on the normal, error, time-out, INT and TERM paths, while the lock is held. What does not hold: session membership is decided only by the current directory (`session_pids`, lines 154 to 161: any process of this user whose cwd is inside the bottle or is its wineserver directory), and after the 5 s wait every member still present is sent SIGKILL (line 190) with no check that it is a Wine process. A non-Wine process of the user that enters the bottle directory after the launch (for example a shell that runs `cd` into `~/Library/Application Support/LTspice/Bottles/ltspice` to inspect the ini, in the owner's terminal or in another session) is not a Wine client, survives `wineserver -k`, and is SIGKILLed. Reviewer check with the doubles (scratch copy of `bdc4513f`, `CWHT_FAKE_WINE_HANG=1`, `-t 4`): a bystander `/bin/sleep 120` started 1.5 s after the launch with its cwd in `fake-support/prefix/drive_c/users` ended with wait status 137 (SIGKILL), and the wrapper printed "Wine session of the bottle ended (wineserver -k), no process of it left" (exit 124 for the time-out itself), so the kill is not reported. The same code path applies to the real bottle. This contradicts the step 5a header ("only when this run started the session") and the acceptance clause that a guard kills only its own processes (05 section 9.2 LTspice row), and none of the six session tests has a bystander that is not a Wine stand-in.

The reverse case is conservative but degrades the fix (finding-22): a non-Wine process parked in the bottle before the launch counts as a running session, and any command line containing `LTspice.exe` (for example another session's `shasum` or `grep` of `.../LTspice.exe`, or the simulated foreign process of `test_foreign_ltspice_exe_leaves_session` while another session runs the everyday suite) counts as the owner's LTspice; either one skips the session end and the Wine services outlive the run again (now without the lock, but TV-014 finding 5's leak and a failed integration case in a TV run).

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-21"></a>finding-21 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | `tools/ltspice-batch.sh` blob `bdc4513f` lines 154 to 161 (`session_pids`) and 186 to 199 (SIGKILL fallback and message); header step 5a (lines 38 to 48); `WineSessionDoubleTests` | The session end SIGKILLs every process of the user whose current directory is inside the bottle (or its wineserver directory) and that is still present 5 s after `wineserver -k`, whether or not it is a Wine process; a non-Wine process that entered the bottle directory after the launch is therefore killed, and the message still says "no process of it left" (reviewer check above: bystander `/bin/sleep`, wait status 137). The wrapper thus can kill a process it did not start, contrary to its header and to the "kills only its own processes" clause of the 05 section 9.2 LTspice row. Fix: count as members (for the SIGKILL fallback, and for `SESSION_BEFORE`) only Wine processes of the bundle, for example those whose `ps -o command=` is a Windows path ending in `.exe` or whose executable lies under `$SUPPORT/` (the bundle's `wine`, preloader and `wineserver`), confirmed on the real session the author observed at 13:56; name every PID and command sent SIGKILL in the message; add a double case with a non-Wine bystander in the prefix started after the launch (expected: it survives, and the session end is still done or reported); then re-run the TV-014 procedure on the new blob (section 7) | Open | Pending | |
| <a id="finding-22"></a>finding-22 | reviewer | Minor | TV-E1, TV-C2 | wrapper lines 162 to 167 (`foreign_ltspice`) and 169 to 184 (`SESSION_BEFORE` test); TV-014 limitation list | False positives of the two guards skip the session end: any command line containing `LTspice.exe` (a `shasum` or `grep` of the file, or the everyday suite's simulated foreign process in another session) counts as the owner's LTspice, and a non-Wine process parked in the bottle before the launch counts as a running session. The Wine services then outlive the run (TV-014 finding 5's leak without the lock) and a concurrent everyday suite can make a TV run's integration case fail. Fix: match `LTspice.exe` as the executable of a Wine process (not any argument), apply the finding-21 membership rule to `SESSION_BEFORE`, and state the residual case in TV-014 section 6 | Open | Pending | |

### Minor findings whose fix lies in the reviewed change

- **finding-15: Verified.** Run 5 procedure `4f61ee30` part D runs the long-path deck through the wrapper (time-out guard, lock, key check before and after, session end); the bare `wine` command is gone, and TV-014 section 3 says why.
- **finding-19: Verified.** TV-014 section 9 ACC-LTSPICE-001 names one wrapper blob, `bdc4513f` (commit `d1148c2`), the blob of run 5. It must be re-issued again with the finding-21 blob.

### Other observations (not findings; for the author and lead SE)

1. The wrapper's own short-lived children in the wait loop (`sleep`, `date`, `kill -0` helpers) inherit fd 9 (a second, transient lock holder in the reviewer's descriptor check on `bdc4513f`). A SIGKILLed wrapper can leave one for at most its sleep interval; this is not the finding-20 leak and needs no change unless the loop gains a long-lived child.
2. The test module's `session_pids` mirrors the wrapper's rule, so `WineSessionIntegrationTests` and part E cannot detect a Wine process of the bottle whose current directory lies outside it. The reviewer's name-based check after the direct runs (`pgrep -fl` on `LTspice.exe`, the bundle's `bin`, `wineserver`, `services.exe`, `winedevice`, `plugplay`, `svchost`, `explorer.exe`, `rpcss`, 14:33:50, holding the lock 10 s after the last run) also found none, so the rule is adequate for the session the author observed. The finding-21 fix is a chance to use the same executable rule in the test.
3. finding-5 (the procedure prints a closing line instead of computing PASS or FAIL) is still open; run 5's closing line lists each part's exit, which made this delta's check quick.

### Reviewer re-runs (commands, exits)

| Command | Exit | Result |
|---|---|---|
| lock and process probe (14:26:43): `lockf -s -t 0 <lock> true`; `pgrep -fl 'LTspice\|wine'`; `session_pids(BOTTLE)` | 0 | lock free; no Wine or LTspice process; session `[]` |
| scratch copies (test module `6c4e00e5`, fixture tree `61c74693`) with the wrapper of `b893382^` (`64e1c723`), of `b893382` (`d5d38767`) and of HEAD (`bdc4513f`): `.venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -k test_child_holds_no_lock_descriptor -v` (14:27:30) | 1, 0, 0 | FAIL on `64e1c723` ("the wine child holds the lock file open"), ok on the two fixed blobs; lock free and no stand-in left after each |
| direct runs of `64e1c723` and `bdc4513f` with the doubles and `CWHT_FAKE_WINE_FDLOG` | 0, 0 | `64e1c723`: double and service hold `f10` on the lock file; `bdc4513f`: neither holds it, "Wine session of the bottle ended" |
| bystander check on a scratch copy of `bdc4513f` with the doubles, `CWHT_FAKE_WINE_HANG=1 -t 4`, a `/bin/sleep 120` started in the fake prefix 1.5 s after the launch | 124 | bystander killed (wait status 137); message "no process of it left" (finding-21) |
| default suite with a 0.2 s process monitor (14:29:30) | 0 | 43 run, 29 passed, 14 skipped (13 integration, 1 permitted); no Wine process started |
| `CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py` (14:30:20 to 14:32:38) | 0 | 43 run, 42 passed, 1 skipped (`test_bottle_without_key`, permitted) |
| `tools/ltspice-batch.sh -b` on scratch copies of `rc-lowpass.asc`, `rc-step-tran.net`, `rc-seeded-error.net` (14:33:27 to 14:33:40) | 0, 0, 1 | PASS, PASS, FAIL "More than one analysis specified."; each ended the Wine session |
| `lockf -k -t 600 <lock>` holding 10 s, then `pgrep -fl` on the Wine and LTspice names and `session_pids(BOTTLE)` (14:33:50) | 0 | no Wine or LTspice process, session `[]`; lock free afterwards (`lockf -k -s -t 0` exit 0) |
| `.venv/bin/python tools/validate_docs.py` (with this record) | 1 | this record PASS; the 10 failures are other records (record drift after other work packages: `cm-plan-05-software-assurance`, `configuration-status`, `lessons-learned`, `tool-validation-tv-015-to-tv-019`, `ts-004-board-thickness-and-panelization`, `adrs-001-to-025`, `process-02-requirements-and-traceability`, `tool-validation-tv-001-to-tv-010`, `trade-studies-ts-001-ts-002`, `trade-study-ts-002-software-assurance`), present before this record was edited |

No process of the ltspice bottle's Wine session and no `LTspice.exe` remained after the reviewer's runs (14:33:50).

### Findings (iteration 3 re-issue 2 state)

Only finding-1, finding-20, finding-15, finding-19 and the new finding-21 and finding-22 were checked; every other row is as in iteration 3 re-issue 1 (rule C1).

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-C5, TV-D1, TV-C2, TV-C4; R2 | TV-014 section 4 row 5; run 5 transcript `aa6d45ea` | Run 5 meets the section 3 pass criterion; reviewer re-run 42 of 43 passed, only the permitted skip | Verified | Pending | |
| finding-2 | reviewer | Major | TV-B3, TV-C2 | `test_ascii_raw_known_answer` | As iteration 3 re-issue 1; passed again in run 5 and in the reviewer re-run | Verified | Pending | |
| finding-3 | reviewer | Major | TV-B3, TV-F1 | wrapper identity checks | As iteration 2 | Verified | Pending | |
| finding-4 | reviewer | Minor | TV-C2, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-5 | reviewer | Minor | TV-C1, TV-D1 | run 5 procedure closing line | Not re-checked (delta) | Open | Pending | |
| finding-6 | reviewer | Minor | CK-CODE-C2 | wrapper output copy | Not re-checked (delta) | Open | Pending | |
| finding-7 | reviewer | Minor | TV-G1-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-8 | reviewer | Minor | TV-E1, TV-C2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-9 | reviewer | Minor | TV-E1, TV-G2-2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-10 | reviewer | Minor | TV-E1, TV-D1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-11 | reviewer | Minor | TV-F1, CK-CODE-G1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-12 | reviewer | Minor | TV-F3, TV-D2 | lock section 5 TV-014 row | As iteration 2 | Verified | Pending | |
| finding-13 | reviewer | Minor | TV-A2 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-14 | reviewer | Minor | TV-F4, R5 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-15 | reviewer | Minor | TV-G2-2, TV-A6 | run 5 procedure `4f61ee30` part D | Part D runs through the wrapper | Verified | Pending | |
| finding-16 | reviewer | Minor | TV-C1 | as iteration 1 | Not re-checked (delta) | Open | Pending | |
| finding-17 | reviewer | Minor | R3, TV-F3 | INSP-015 record drift | Not re-checked (delta) | Open | Pending | |
| finding-18 | reviewer | Minor | TV-C2, CK-CODE-H1 | as iteration 2 | Not re-checked (delta) | Open | Pending | |
| finding-19 | reviewer | Minor | TV-F1 | TV-014 section 9 at `af545923` | One blob named (`bdc4513f`); re-issue with the finding-21 blob | Verified | Pending | |
| finding-20 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | wrapper line 327 at `bdc4513f`; `test_child_holds_no_lock_descriptor` | Lock descriptor closed before exec; regression case fails on `64e1c723` and passes on the fix | Verified | Pending | |
| finding-21 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | wrapper lines 154 to 161 and 186 to 199 | Session end SIGKILLs any user process with its cwd in the bottle, not only Wine processes, and does not report it (see above) | Open | Pending | |
| finding-22 | reviewer | Minor | TV-E1, TV-C2 | wrapper lines 162 to 184 | Guard false positives skip the session end (see above) | Open | Pending | |

### Next step (fix loop, owner route (1))

The owner's route (1) includes a fix loop for this delta (status note section 9), so no new escalation is needed. The author fixes finding-21 (membership restricted to Wine processes of the bundle, SIGKILLed PIDs named, a bystander double case), fixes finding-22 with it or states it as a limitation, re-runs the TV-014 procedure on the new blob with the section 3 criterion (plus the new case), re-issues ACC-LTSPICE-001 with that blob, and asks for one more delta of this record on finding-21 (and finding-22 if fixed). Until then LTspice results stay developer evidence (TV-014 limitation 8); they can be produced now, since run 5 and this re-run show the wrapper computes the known answers correctly, and the owner can be told that the defect lies only in the post-run cleanup, not in the simulation results. Minor findings become liens only after a first APPROVED verdict, so none is a lien yet.

### Verdict (iteration 3 re-issue 2)

```
VERDICT: NEEDS CHANGES (fix loop under the owner's route (1), status note section 9)
PRODUCT: TV-014 at f47360aa74a71011b3759e20a7f66d7cd14ac381 (wrapper blob bdc4513f, test module 6c4e00e5, fixture tree 61c74693; run 5 procedure 4f61ee30, transcript aa6d45ea); blobs unchanged at HEAD c0f5244
FINDINGS:
- [Major] finding-1 Verified: run 5 meets the section 3 criterion; reviewer re-run 43 run, 42 passed, only the permitted skip.
- [Major] finding-20 Verified: fd 9 closed before exec; test_child_holds_no_lock_descriptor fails on b893382^ (64e1c723) and passes on d5d38767 and bdc4513f.
- [Major] finding-21 (new) Open: the step 5a SIGKILL fallback kills any user process whose cwd is in the bottle, not only Wine processes, and does not report it (bystander killed, status 137).
- [Minor] finding-22 (new) Open: guard false positives (any "LTspice.exe" command line; a non-Wine process in the bottle) skip the session end.
- [Major] finding-2, finding-3 Verified; [Minor] finding-12, finding-15, finding-19 Verified; finding-4 to finding-11, finding-13, finding-14, finding-16 to finding-18 Open (not re-checked, rule C1).
GATING: the default suite never starts the real LTspice (code, and a 0.2 s process monitor over the whole suite).
RE-RUN: CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py; exit 0; 43 run, 42 passed, 1 skipped (permitted); direct wrapper runs rc-lowpass.asc 0, rc-step-tran.net 0, rc-seeded-error.net 1; no bottle Wine process and no LTspice.exe 10 s after the last run
KEY CHECK: CaptureAnalytics=false on line 3, count 1, before (14:26:43, 14:30:20, 14:33:27) and after (14:29:51, 14:32:38, 14:33:50) every reviewer run
MEASUREMENTS: size=1 record, 4 purposes, 43 tests, 14 fixture files, 435 LOC; turns=34; minutes=45; major=5; minor=17; unsafe_sites=0
```

## Iteration 3 re-issue 3: delta on finding-21 (Major) on run 6, with finding-1 and finding-20 re-checked (2026-09-27)

**Authority and scope (rule C1).** Second delta of the fix loop the owner chose with route (1) ("No, that is unacceptable. We need to actually run the circuit simulations of the amplifiers and filters in LT Spice. So uh, how can we fix this?"; status note `docs/plan/status/status-2026-09-27.md` section 9). The iteration 3 re-issue 2 next step asked for one more delta on finding-21 (and finding-22 if fixed). This delta verifies finding-21 on the fix commit `45531ac` and run 6, re-checks finding-1 (run 6 meets the section 3 criterion) and finding-20 (the lock is not inherited; the regression case fails on the old blob), and reviews the changed session end and the test gating. The front matter keeps `iteration: 3` (schema maximum; precedent INSP-009). Of the Minor findings only finding-19 (the ACC-LTSPICE-001 blob) and finding-22 (partly addressed by the fix) were re-checked.

**Products (rule C2).** Commit `bd78bd5` (the author's run 6 record commit) on the fix `45531ac`: wrapper `88b71475` (465 lines, SHA-256 `6b66ad75...f280`), test module `e90b0ef1` (46 cases, SHA-256 `68095b07...92ea`), fixture tree `f1497c52` (14 files; `known-answers.json` `84ecdd0a`, `fake-support/bin/wine` `42177aad`), run 6 procedure `72dfa2d7` and transcript `f87f8fac`, TV-014 `9c6d477a`, lock `be96420b`, TV README `f4757da2`, `tools/README.md` `a5e9cab6`. Every blob recomputed with `git rev-parse HEAD:<path>` at HEAD `7126a80` equals `bd78bd5` (the one later commit touches WP-PDR-27 only); the working-tree wrapper and test module hash to the same blobs (`git hash-object`, `shasum -a 256`).

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, TV-014, the wrapper, the tests, the doubles, runs 5 and 6, the finding-20 or finding-21 fix, or any earlier iteration of this record, and edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-038 finding-21 session end SIGKILL non-Wine process bottle"; "LTspice amplifier or filter deck netlist hardware/sim checker"; "rule C1 review verdict APPROVED Minor findings become liens record_status readiness_met"). `grep -n` afterwards only pinned lines in known files.

**Headless and bottle safety.** LTspice was reached only through `tools/ltspice-batch.sh`; no GUI, AppleScript, System Events or screen capture; nothing was downloaded. Before the first run (14:55:42 CDT): no `LTspice.exe`, no Wine-named process and no process with its current directory in the bottle or its wineserver directory (reviewer probe below), no other session running the wrapper or `test_ltspice_batch`, lock free (`lockf -k -s -t 0` exit 0, no holder). Key check `iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | grep -c '^CaptureAnalytics=false$'` = 1 (line 3) at 14:55:42 (ini 12418 bytes, modified 14:48), 14:58:04 and 14:58:42 (before and after the default suite), 14:59:11 (before the integration run), 15:01:49 (after it; ini 12422 bytes, modified 15:00: LTspice rewrote its recent-file list, key kept), 15:02:32 and 15:02:50 (before and after the first direct runs), 15:03:00 and 15:03:13 (before and after the second), 15:03:37 (final). The reviewer signalled one process only: its own `/usr/bin/tail -f /dev/null` bystander (PID 67807, parent launchd, name checked with `ps -o comm=` first), ended with SIGTERM after the double check below; every other reviewer bystander was a `/bin/sleep` of 25 s or 40 s that expired by itself. Deviation: in the first direct-run loop the exit status was lost to the shell (`PIPESTATUS` under zsh); the three decks were run again at 15:03:00 to record it (same PASS, PASS, FAIL).

**Reviewer probe (read only, scratchpad `probe.sh` and `mon2.sh`).** Lists every process of the user whose current directory is in the ltspice bottle or its wineserver directory `/private/tmp/.wine-501/server-<dev>-<inode>` whatever its name (`lsof -d cwd`, then `ps -o comm=`), every process whose executable name is a Windows path or lies under `/Applications/LTspice.app`, and every command line naming `LTspice.exe` or the bundle's `SharedSupport/ltspice`. It is wider than the wrapper's rule on purpose.

### Verification of the Major findings

| Finding | State | Evidence |
|---|---|---|
| finding-21 | **Verified** | **Code** (`88b71475` lines 159 to 186 and 196 to 229): membership is now `session_pids` = `bottle_pids` (current directory in the bottle or its wineserver directory, unchanged) filtered by `is_wine` (`ps -o comm=` is a Windows path ending in `.exe`, case-insensitive, or starts with the bundle directory `$SUPPORT/` or its physical path). The same `session_pids` feeds `SESSION_BEFORE` (line 356), the wait loop and the SIGKILL fallback; the SIGKILLed PIDs are named with their executable name before the signal ("SIGKILL sent to the Wine processes of the session still present 5 s after wineserver -k: PID (name)"); the "no Wine process of it left" line no longer claims the whole bottle; non-Wine processes in the bottle are only listed in a note, never passed to `kill`. `wineserver -k` itself reaches only clients of the bottle's Wine server, that is Wine processes. Header step 5a, `tools/README.md` and TV-014 limitation 10 state the rule. **Regression cases on the old blob** (reviewer, scratch copies of the HEAD test module `e90b0ef1` and fixture tree, test doubles only, 14:56:25 to 14:56:58): with the wrapper of `d1148c2` (`bdc4513f`, `git cat-file`, `git hash-object` rechecked) `test_non_wine_bystander_after_launch_survives` FAIL ("the non-Wine bystander was ended (status -9)", message "no process of it left") and `test_non_wine_bystander_before_launch_does_not_stop_session_end` FAIL ("was running before this run", session end skipped), `test_standin_is_counted_as_wine` ok; with `88b71475` all three ok. This reproduces run 6 part G. **Independent reviewer check with the doubles** (fresh fixture copy, `CWHT_FAKE_WINE_SERVICE=1 CWHT_FAKE_WINE_HANG=1 CWHT_FAKE_WINESERVER_NOOP=1`, `-t 3`, 14:57:29), with bystanders the author's cases do not use: a `/bin/bash -c 'sleep 25; :'` (a shell and its child) in `fake-support/prefix/drive_c/windows`, the stand-in service's own directory, and a `/usr/bin/tail -f /dev/null` in `drive_c/users`, both started 1 s after the launch: exit 124; "SIGKILL sent ... 67799 (C:\windows\system32\services.exe)" (the stand-in only); "no Wine process of it left"; note "... left running (never signalled): 67805 (/bin/bash) 67807 (/usr/bin/tail) 67809 (sleep)"; bash and tail alive afterwards, the stand-in gone, one `-k` call with `WINEPREFIX` equal to the double's prefix. **Real bottle** (15:02:32 to 15:02:50): a `/bin/sleep 40` with its current directory in the ltspice bottle's `drive_c/users` started 0.5 s before the launch and a second one 1 s after it, then `tools/ltspice-batch.sh -b rc-step-tran.net`: exit 0, PASS, "Wine session of the bottle ended (wineserver -k), no Wine process of it left", note naming both sleeps; both still running afterwards (they expired at 40 s), so neither the check at the launch nor the session end treated them as Wine. **Basis of the rule on the real session**: the reviewer's sampler (every 0.3 s through the 158 s integration run) saw in the bottle or its wineserver directory only `.../SharedSupport/ltspice/lib/wine/../../bin/wineserver`, `.../SharedSupport/ltspice/bin/wineserver`, `C:\windows\system32\` `services.exe`, `winedevice.exe`, `plugplay.exe`, `svchost.exe`, `explorer.exe`, `rpcss.exe`, `wineboot.exe` and `C:\Program Files\ADI\LTspice\LTspice.exe`, each matched by the rule, plus 13 single-sample PIDs that had ended before `ps` read their name (transient, for example the wrapper's own `cd "$PREFIX"` command substitution; never signalled, since an empty name is not Wine); outside the bottle `.../bin/wineloader`, `.../x86_64-windows/winewrapper.exe` and `C:\windows\system32\winemenubuilder.exe`, also matched by the rule and covered by the integration check's "anywhere" list. This confirms the author's 14:39 observation independently |
| finding-1 | **Verified** (held) | Run 6 (`f87f8fac`, 14:46:59 to 14:51, HEAD `45531ac`, part A every identity "unchanged from HEAD", 0 fixture files differing) meets the TV-014 section 3 criterion as revised for 46 cases: part C exit 0, 46 run, 45 passed, the one skip `test_bottle_without_key` (permitted), `LockTests.test_busy_when_lock_held` ran, the three finding-21 cases ran; part D exit 0 at a 262-character Windows path with the `.raw` beside the deck; part E nothing in the bottle, no Wine process of the bundle, no `LTspice.exe`, only the part E `lockf` on the lock file, lock free after; part F exit 1; part G exit 1; key count 1 in part B and after C, D and E. **Reviewer reproduction:** `CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py` (14:59:11 to 15:01:49): exit 0, 46 run in 157.9 s, 45 passed, 1 skipped (`test_bottle_without_key`, permitted); every `LTspiceRunTests` case, `WineSessionIntegrationTests`, `TimeoutGuardTests`, the busy-lock case and the ten `WineSessionDoubleTests` passed. Direct wrapper runs on scratch copies of the fixture decks (15:03:00 to 15:03:13): `-b rc-lowpass.asc` (the RC low-pass filter) exit 0 PASS, `f3db ... AT 999.999642341`; `-b rc-step-tran.net` exit 0 PASS, `vtau` 0.632120367773 V, `thalf` 0.693147653313 ms; `-b rc-seeded-error.net` exit 1 "More than one analysis specified."; each printed "no Wine process of it left". The values equal those whose analytic answers re-issue 2 recomputed (1/(2 pi R C) = 999.99964 Hz, 1 - e^-1 = 0.63212056 V, 1 ms ln 2 = 0.69314718 ms), each inside its criterion |
| finding-20 | **Verified** (held) | Launch line unchanged since `b893382` (`( exec 9>&-; cd "$RUN" && exec "$WINE" ... )`, line 357 of `88b71475`). **Regression case on the old blob with the current test module** (scratch copy, test doubles only, 14:56:25): wrapper of `b893382^` (`64e1c723`, `git cat-file`, `git hash-object` rechecked) with test module `e90b0ef1` and fixture tree `f1497c52`: `test_child_holds_no_lock_descriptor` FAIL, "'65890' unexpectedly found in ['65845', '65890', ...] : the wine child holds the lock file open"; with `88b71475`: ok. Lock free after each case (`lockf -k -s -t 0` exit 0), no stand-in or bystander left (`pgrep`) |

### Review of the session end (step 5a) and the test gating

**Does the default suite ever start the real LTspice? No.** By code: the three new cases use the doubles only (`WrapperCase.env` sets `CWHT_LTSPICE_SUPPORT` to the work copy's `fake-support`; `test_standin_is_counted_as_wine` runs no wrapper), and `wine_pids_anywhere` is called only from `assert_no_bottle_session_after`, which only the integration classes use. By observation: the default suite (`env -u CWHT_LTSPICE_INTEGRATION -u CWHT_LTSPICE_SLOW .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -v`, 14:58:04 to 14:58:42, exit 0, 46 run, 32 passed, 14 skipped, 13 with the integration reason and the permitted one) was sampled every 0.2 s for any process whose executable name lies under `/Applications/LTspice.app` and any command line naming the bundle's `SharedSupport/ltspice/bin/wine`: none. The only Windows-named processes seen were the doubles' stand-ins (`C:\windows\system32\services.exe`, 9 PIDs; `/bin/sleep` under `exec -a`, current directory in the work copies' fake prefix).

**Does the cleanup ever touch a Wine process it did not start, or any non-Wine process? No non-Wine process; a foreign Wine process only in the residual race below.** Non-Wine processes: no path of `end_session` passes a PID to `kill` that is not in `session_pids`, and each such PID is re-read from `ps` just before the signal; shown on the doubles and on the real bottle above. Wine processes it did not start: the session end is skipped when a Wine process of the bottle existed at the launch (`SESSION_BEFORE`, now Wine processes only, so a parked shell no longer suppresses it) or when any command line naming `LTspice.exe` other than this run's is present at the end (`foreign_ltspice`, unchanged). The test doubles never reach the real bottle (`PREFIX` is `<CWHT_LTSPICE_SUPPORT>/prefix` whenever the hook is set). The integration and direct runs of this delta left nothing: 10 s after the last run, holding the lock (15:03:25 to 15:03:35), the reviewer probe found no process in the bottle or its wineserver directory under any name, no Wine-named or bundle process anywhere and no `LTspice.exe`; the test module's `session_pids`, `bottle_pids` and `wine_pids_anywhere` all `[]`; the lock file open only by the probe's `lockf`, free afterwards (exit 0).

**finding-22: partly fixed, stays Open (Minor).** The `SESSION_BEFORE` half is fixed by the finding-21 rule (the before-launch bystander case and the reviewer's real-bottle check). The `foreign_ltspice` half is unchanged (`pgrep -f 'LTspice\.exe'` on any command line), and TV-014 limitation 10 now states the residual (it can only skip a session end, never signal a process). Remaining fix: match `LTspice.exe` as the executable name of a Wine process (`is_wine` plus `comm` ending in `LTspice.exe`) rather than any argument.

### Other observations (not findings; for the author and lead SE)

1. Residual race, inherent to `wineserver -k`: if the owner opens LTspice from the Finder while a wrapper run is in progress and its `LTspice.exe` does not yet exist when `foreign_ltspice` runs (the GUI's start-up, or the sub-second gap between that check and `-k`), `wineserver -k` ends the owner's starting session. Nothing is lost but the start; the owner's ini write is the TV-014 finding 2 mechanism the lock already addresses for wrapper runs. Worth one sentence in TV-014 limitation 10 ("do not open the LTspice GUI while a wrapper run is in progress").
2. The integration check's `wine_pids_anywhere` counts the everyday suite's stand-ins (`/bin/sleep` named `C:\windows\system32\services.exe`) of another session as Wine processes, so an everyday suite run by another session during a TV run can fail `WineSessionIntegrationTests` or part E. The error is fail-safe (a false failure, never a false pass) and the procedure already asks for no other LTspice work in the window; the finding-22 fix could also check the stand-ins' executable path (`/bin/sleep`) out of the rule in the test helper, or TV-014 section 3 can say that a TV run needs no concurrent `tools/tests` suite.
3. `is_wine` would count a non-Wine process that sets its argv[0] to a Windows `.exe` path and sits in the bottle (TV-014 limitation 10 says so: deliberate imitation only). Accepted.
4. finding-5 (the procedure prints the parts' exits instead of computing PASS or FAIL) stays open; run 6's closing line again made the check quick.

### Reviewer re-runs (commands, exits)

| Command | Exit | Result |
|---|---|---|
| pre-run probe (14:55:42): key check; `ps` for LTspice or Wine names; `pgrep` for wrapper or test runs; `lockf -k -s -t 0 <lock> true`; `probe.sh` | 0 | key count 1 (line 3); no LTspice, Wine or bottle process; no other run; lock free |
| scratch copies (test module `e90b0ef1`, fixture tree `f1497c52`) with wrapper `64e1c723` (`b893382^`) and `88b71475`: `-k test_child_holds_no_lock_descriptor` (14:56:25) | 1, 0 | FAIL on `64e1c723` ("the wine child holds the lock file open"); ok on HEAD |
| same copies with wrapper `bdc4513f` (`d1148c2`) and `88b71475`: `-k bystander -k standin` (14:56:30 to 14:56:58) | 1, 0 | `bdc4513f`: both bystander cases FAIL (bystander status -9; session end skipped), stand-in rule ok; HEAD: 3 ok |
| wrapper `88b71475` on a fixture copy with the doubles, `-t 3`, NOOP wineserver, bash, sleep and tail bystanders in the fake prefix 1 s after the launch (14:57:29) | 124 | stand-in SIGKILLed and named; three bystanders named in the note and alive; one `-k` |
| default suite with a 0.2 s process monitor (14:58:04 to 14:58:42) | 0 | 46 run, 32 passed, 14 skipped (13 integration, 1 permitted); no process of the LTspice bundle started |
| `CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py` with a 0.3 s bottle sampler (14:59:11 to 15:01:49) | 0 | 46 run, 45 passed, 1 skipped (`test_bottle_without_key`, permitted); every sampled bottle process with a name matched the Wine rule |
| `tools/ltspice-batch.sh -b` on scratch copies of `rc-lowpass.asc`, `rc-step-tran.net`, `rc-seeded-error.net` (15:02:32 to 15:02:45, again 15:03:00 to 15:03:13 for the exits) | 0, 0, 1 | PASS (f3db 999.999642341 Hz), PASS (vtau 0.632120367773 V), FAIL "More than one analysis specified."; each "no Wine process of it left" |
| real-bottle bystanders: `/bin/sleep 40` in the bottle's `drive_c/users` before and 1 s after the launch of `-b rc-step-tran.net` (15:02:45 to 15:02:50) | 0 | PASS; session ended; both sleeps named in the note and alive afterwards |
| `lockf -k -t 600 <lock>` holding 10 s, then `probe.sh` and `lsof <lock>`; test helpers `session_pids`, `bottle_pids`, `wine_pids_anywhere` (15:03:25 to 15:03:37) | 0 | nothing in the bottle or its wineserver directory, no Wine-named or bundle process, no `LTspice.exe`; helpers `[]`; lock free afterwards (`lockf -k -s -t 0` exit 0); key count 1 |
| `env -u CWHT_LTSPICE_INTEGRATION -u CWHT_LTSPICE_SLOW .venv/bin/python -m unittest discover -s tools/tests` (15:04:46 to 15:06:42) | 1 | 596 run, 1 failure (`test_validate_docs.RepositoryTests.test_repository_exit_zero`, the whole-repository `validate_docs.py` case), 14 skipped |
| `.venv/bin/python tools/validate_docs.py` (with this record) | 1 | this record PASS; the same 10 other records FAIL on record drift as at re-issue 2 (`cm-plan-05-software-assurance`, `configuration-status`, `lessons-learned`, `tool-validation-tv-015-to-tv-019`, `ts-004-board-thickness-and-panelization`, `adrs-001-to-025`, `process-02-requirements-and-traceability`, `tool-validation-tv-001-to-tv-010`, `trade-studies-ts-001-ts-002`, `trade-study-ts-002-software-assurance`), present before this record was edited |

No process of the ltspice bottle, no Wine process of the bundle anywhere and no `LTspice.exe` remained after the reviewer's runs (15:03:35); the reviewer's scratch copies and fixture work directories were deleted.

### Findings (iteration 3 re-issue 3 state)

Only finding-1, finding-20, finding-21, finding-19 and finding-22 were checked; every other row is as in iteration 3 re-issue 2 (rule C1).

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | TV-C5, TV-D1, TV-C2, TV-C4; R2 | TV-014 section 4 row 6; run 6 transcript `f87f8fac` | Run 6 meets the section 3 pass criterion (46 run, 45 passed, only the permitted skip, parts D to G as expected); reviewer re-run 45 of 46 passed | Verified | Pending | |
| finding-2 | reviewer | Major | TV-B3, TV-C2 | `test_ascii_raw_known_answer` | As iteration 3 re-issue 2; passed again in run 6 and in the reviewer re-run | Verified | Pending | |
| finding-3 | reviewer | Major | TV-B3, TV-F1 | wrapper identity checks | As iteration 2 | Verified | Pending | |
| finding-4 | reviewer | Minor | TV-C2, TV-D1 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-5 | reviewer | Minor | TV-C1, TV-D1 | run 6 procedure closing line | Not re-checked (delta); lien | Open | Pending | |
| finding-6 | reviewer | Minor | CK-CODE-C2 | wrapper output copy | Not re-checked (delta); lien | Open | Pending | |
| finding-7 | reviewer | Minor | TV-G1-2 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-8 | reviewer | Minor | TV-E1, TV-C2 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-9 | reviewer | Minor | TV-E1, TV-G2-2 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-10 | reviewer | Minor | TV-E1, TV-D1 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-11 | reviewer | Minor | TV-F1, CK-CODE-G1 | as iteration 2 | Not re-checked (delta); lien | Open | Pending | |
| finding-12 | reviewer | Minor | TV-F3, TV-D2 | lock section 5 TV-014 row | As iteration 2 | Verified | Pending | |
| finding-13 | reviewer | Minor | TV-A2 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-14 | reviewer | Minor | TV-F4, R5 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-15 | reviewer | Minor | TV-G2-2, TV-A6 | run 6 procedure part D | Part D runs through the wrapper (unchanged from run 5) | Verified | Pending | |
| finding-16 | reviewer | Minor | TV-C1 | as iteration 1 | Not re-checked (delta); lien | Open | Pending | |
| finding-17 | reviewer | Minor | R3, TV-F3 | INSP-015 record drift | Not re-checked (delta); `validate_docs.py` still fails on `tool-validation-tv-001-to-tv-010` among 10 records; lien | Open | Pending | |
| finding-18 | reviewer | Minor | TV-C2, CK-CODE-H1 | as iteration 2 | Not re-checked (delta); lien | Open | Pending | |
| finding-19 | reviewer | Minor | TV-F1 | TV-014 section 9 at `9c6d477a` | ACC-LTSPICE-001 names the one run 6 blob `88b71475` (commit `45531ac`), test module `e90b0ef1`, fixture tree `f1497c52`; lock section 5 and the TV README name the same blob | Verified | Pending | |
| finding-20 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | wrapper line 357 at `88b71475`; `test_child_holds_no_lock_descriptor` | Lock descriptor closed before exec; regression case fails on `64e1c723` with the current test module and passes on HEAD | Verified | Pending | |
| finding-21 | reviewer | Major | CK-CODE-C2, TV-G1-2, TV-E1, TV-C2 | wrapper `88b71475` lines 159 to 186 and 196 to 229; `WineSessionDoubleTests` | Session membership is Wine processes of the bundle only; SIGKILLed PIDs named; non-Wine processes never signalled and named in a note; bystander cases fail on `bdc4513f` and pass on HEAD; reviewer checks on the doubles and on the real bottle | Verified | Pending | |
| finding-22 | reviewer | Minor | TV-E1, TV-C2 | wrapper `foreign_ltspice` (lines 187 to 192) | `SESSION_BEFORE` half fixed by the finding-21 rule; the `LTspice.exe` guard still matches any command line (skips a session end, never signals); stated in TV-014 limitation 10; lien | Open | Pending | |

### Liens (rule C1)

The 14 open Minor findings (finding-4 to finding-11, finding-13, finding-14, finding-16 to finding-18 and finding-22) become liens with this first APPROVED reviewer verdict: owner the tool owner (WP-PDR-07), due at the CDR readiness declaration, each closed by a delta of this record on its fix or by an owner deferral. finding-17 is also the reason the record verdict is held (readiness R3), so its route (an INSP-015 delta re-issue through the lead SE) gates the record verdict, not the accreditation.

### Next step

OD-24b (accreditation of ACC-LTSPICE-001 at wrapper blob `88b71475`) can go to the owner on this reviewer verdict: TV-014 section 9 names the blob of run 6 and of this re-run. The record `verdict` is set APPROVED by the lead SE, with `readiness_met: true`, when `validate_docs.py` exits 0 and no product blob has changed (else a delta of this record on the changed blobs). Until OD-24b is recorded, LTspice output stays developer evidence (TV-014 limitation 8), but the simulations of the amplifiers and filters can be run now through the wrapper: the known answers pass, and the post-run cleanup ends only the Wine session the run started.

### Verdict (iteration 3 re-issue 3)

```
VERDICT: APPROVED (reviewer verdict; record verdict held at NEEDS CHANGES for readiness R3 only: validate_docs.py exits 1 on 10 other records)
PRODUCT: TV-014 at bd78bd586fb9fe873d67bb1418217fddaa6cdec4 (wrapper blob 88b71475 of 45531ac, test module e90b0ef1, fixture tree f1497c52; run 6 procedure 72dfa2d7, transcript f87f8fac); blobs unchanged at HEAD 7126a80
FINDINGS:
- [Major] finding-21 Verified: members of the session are Wine processes of the bundle only (cwd in the bottle and Windows .exe or bundle executable name); SIGKILLed PIDs named; non-Wine processes never signalled. Bystander cases fail on bdc4513f, pass on 88b71475; reviewer bash/tail bystanders (doubles) and /bin/sleep bystanders in the real bottle survived and were named.
- [Major] finding-1 Verified (held): run 6 meets the 46-case criterion; reviewer re-run 46 run, 45 passed, only the permitted skip.
- [Major] finding-20 Verified (held): test_child_holds_no_lock_descriptor fails on b893382^ (64e1c723) with the current test module and passes on 88b71475.
- [Minor] finding-19 Verified (ACC-LTSPICE-001 names 88b71475); finding-22 partly fixed, stays Open.
- [Major] finding-2, finding-3 Verified; [Minor] finding-12, finding-15 Verified; finding-4 to finding-11, finding-13, finding-14, finding-16 to finding-18, finding-22 Open: liens under rule C1 (tool owner, CDR readiness declaration).
GATING: the default suite never starts the real LTspice (code, and a 0.2 s monitor over the whole suite: no bundle process).
CLEANUP: never signals a non-Wine process (code, doubles, real bottle); a foreign Wine session is left when it ran at launch or its LTspice.exe is open at the end (residual start-up race: observation 1).
RE-RUN: CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py; exit 0; 46 run, 45 passed, 1 skipped (permitted); direct wrapper runs rc-lowpass.asc 0, rc-step-tran.net 0, rc-seeded-error.net 1; nothing of the bottle, no Wine process of the bundle and no LTspice.exe 10 s after the last run
KEY CHECK: CaptureAnalytics=false on line 3, count 1, before (14:55:42, 14:58:04, 14:59:11, 15:02:32, 15:03:00) and after (14:58:42, 15:01:49, 15:02:50, 15:03:13, 15:03:37) every reviewer run
MEASUREMENTS: size=1 record, 4 purposes, 46 tests, 14 fixture files, 465 LOC; turns=36; minutes=40; major=5; minor=17; unsafe_sites=0
```
