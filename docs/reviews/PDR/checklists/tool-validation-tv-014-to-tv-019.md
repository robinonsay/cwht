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
# product_commit: iteration 2 (delta) reviews the blobs frozen at aa746f0 (wrapper, test module and fixture
# from c9d2c54; TV-014, run 3 evidence, README and lock from aa746f0). Iteration 1 reviewed b362395 (blobs in
# the iteration 1 section). At review time HEAD c827202 (WP-PDR-08) had moved the lock and the README on rows
# other than LTspice; every other listed blob equals HEAD
product_commit: "aa746f054914d93124dbe3c516848bc9af60c89b"
product_files: ["tools/ltspice-batch.sh@64e1c7230278363bca85542f410da5a0853a42f2", "tools/tests/test_ltspice_batch.py@c75cb7b3568b46d478ab710dd0f5f81ff3df8049", "tools/tests/fixtures/ltspice/known-answers.json@8ec25d711978e2dbef33bd23adb5a80cbd70d200", "tools/tests/fixtures/ltspice/fake-support/bin/wine@acd2ec5cf8ef71514b3f50c4b543203c897d6102", "tools/tests/fixtures/ltspice/rc-step-tran.net@bd19be4123841c512402ffec3009d815ded2de02", "tools/tests/fixtures/ltspice@8feee9d0f3eab7dd45ae73ff4437846dd9bddd55", "docs/cm/tool-validation/TV-014-ltspice-batch.md@6204bd78bb67159f0eae634c5a39e46b51ce5153", "docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27.sh@f9fea642a57299fc7d37fb82ea11e5261d1bcb7f", "docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27-run3.log.txt@bc806daeacc9db591731e46b9583edc24ee61f15", "docs/cm/tool-validation/README.md@98969f416e1bdce27135231e3e50a3087db7c8ae", "tools/toolchain.lock.md@9aca88d34a4d41d01cbd50d90152024ab97d9f2d", "tools/README.md@54f97c64f92a0443a82a633e5712d5b6b009b32a"]
fixture_trees: ["tools/tests/fixtures/ltspice@8feee9d0f3eab7dd45ae73ff4437846dd9bddd55"]
tv_ids: [TV-014]
tool_class: B
# tool_kind: the wrapper is a repository tool (G1) around an external tool (G2); both subsections answered
tool_kind: repository-tool
acc_proposed: [ACC-LTSPICE-001]
product_size: 1 record (TV-014), 4 purposes, 35 known-answer tests, 13 fixture files, 360-line wrapper
sprint: PDR-prep
author_agent: "author:WP-PDR-07 (Claude as tool owner)"
tool_author_agent: "author:WP-PDR-07 (Claude as tool owner)"
reviewer_agent: "reviewer:WP-PDR-07-tool-validation-iter2 (independent; authored no part of WP-PDR-07; iteration 1 by reviewer:WP-PDR-07-tool-validation-iter1)"
# criticality: neither (03 sections 4.3.1 and 6.1.1: no tool is a safety-critical or mission-critical
# component). 07 section 2.1.1: code of a "Neither" component needs no assurance review unless the file holds
# unsafe (a shell script has none); the tool validation template has no 2.1.1 row. The swe-136 and swe-070
# section 7.1 tasks are answered in section H by this reviewer as the assurance function (charter section 2)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
# readiness_met: false. R2 is still not met in substance: run 3 (c9d2c54) and the reviewer re-run at 12:00
# CDT exit 0 with 35 run, 22 passed, 13 skipped, because the bottle ini still lacks CaptureAnalytics=false
# (420 bytes, modified 10:50, key count 0). R3 is not met: validate_docs.py exits 1 on INSP-015 drift
# (finding-17) and the full suite fails test_repository_exit_zero. Iteration 3 is the last before escalation
# to the owner (rule C1; 07 section 10.2)
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 3
findings_minor: 16
findings_open: 16
findings_fixed: 1
findings_verified: 2
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [R2, R3, TV-A1, TV-C2, TV-C5, TV-D1, TV-E1, TV-F1, TV-F3, TV-G1-2, TV-G2-2, CK-CODE-C2]
effort_turns: 24
effort_minutes: 45
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-038: tool validation TV-014 (LTspice through tools/ltspice-batch.sh), WP-PDR-07, iterations 1 and 2

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
