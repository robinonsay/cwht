# TV-014: LTspice 26.0.2 through tools/ltspice-batch.sh (git blob 64e1c723, commit c9d2c54)

| Field | Value |
|---|---|
| Record | TV-014 |
| Status | **Not yet validated.** Revision of 2026-09-27 for the Major findings 2 and 3 of review INSP-038 iteration 1: the wrapper now checks the bundle build and the `LTspice.exe` SHA-256 exactly and requires the log version line (purpose 3), and `-ascii` has a known answer (purpose 1). Known-answer run 3 (2026-09-27 11:56, commit `c9d2c54`) passed the 22 cases that do not need the bottle precondition, including the new identity faults; the 13 cases that need it (12 run LTspice, 1 runs a test double) and procedure part D are blocked because the bottle `LTspice.ini` lost `CaptureAnalytics=false` during development (finding 2; owner action OA-TV014-1). Run 4, the validation run, follows the owner's restore (INSP-038 finding-1). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: LTspice through the CrossOver wrapper, Analysis-class simulation evidence) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6, validated and accredited simulation tools) through CM plan section 9; ADR-018 (telemetry opt-out) |
| Due | PDR (CM plan section 13 PDR row). It blocks every LTspice result cited as evidence (`docs/plan/pdr-work-plan.md` WP-PDR-07, WP-PDR-19 to 26 and 28) until accredited (owner decision OD-24b) |
| Lock rows | `tools/toolchain.lock.md` section 1 rows LTspice and LTspice Wine layer; section 1.1 row LTspice; section 1.2 row `tools/ltspice-batch.sh`; section 1.4 findings 12 to 14; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 0) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/ltspice-batch.sh` | git blob `64e1c7230278363bca85542f410da5a0853a42f2`, SHA-256 `115b81c1b5974d20b9b599d86d05788f837433955bf2f2c98d2eb5ca7410f90a`, mode 100755, 360 lines | committed in `c9d2c54` (INSP-038 finding-3: exact bundle build, `LTspice.exe` SHA-256, log version line). Earlier blobs: `884df077` in `41d150e`; `102b93d4` in `b41e544` (finding 3 of section 4.1), tested in runs 1 and 2 |
| `tools/tests/test_ltspice_batch.py` | git blob `c75cb7b3568b46d478ab710dd0f5f81ff3df8049`, SHA-256 `ba1d8c114e1a2bf812d9103ab9fe3904cbd17ad8921204552253e4bff173c113`, 35 cases | committed in `c9d2c54` (INSP-038 findings 2 and 3). Earlier blobs: `220db90b` in `41d150e`; `c4410447` in `b41e544` (29 cases, runs 1 and 2) |
| `tools/tests/fixtures/ltspice/` | 13 files, git tree `8feee9d0`, tree digest `b9f7ed3c98a598c84e95690ba17c37719ef7564ea7772851d79bf3796aa576cb` (SHA-256 of the sorted `shasum -a 256` list; the list is in the run 3 transcript) | committed in `c9d2c54`: `known-answers.json` block `wrapper` gained `locked_bundle`, `locked_exe_sha256`, `ascii`, `seeded_bundle_build`, `seeded_exe_sha256` and `seeded_no_version_line`, and `fake-support/bin/wine` (a test double, mode 100755) was added. Earlier: 12 files, digest `069f03ee...0992835`, tree `b9f9eca1`, committed in `41d150e` (runs 1 and 2); the three 2026-09-25 decks and the earlier blocks of `known-answers.json` are unchanged |
| LTspice program | `26.0.2` (`tools/ltspice-batch.sh -version`; bare command `wine --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' -version`, 2026-09-25) | lock section 1 |
| LTspice bundle | `26.0.2.1` (`defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString`, 2026-09-27) | lock section 1 |
| `LTspice.exe` in the bottle | SHA-256 `a94eb1789084db9f46375cce05110e03578f9cdb931867a0faaca5b200793f06` (`drive_c/Program Files/ADI/LTspice/LTspice.exe`, 2026-09-27; RSK mitigation step S1 asks for this pin) | recorded here first; lock section 1 row |
| CrossOver Wine layer | `"Version" = "25.0.1.38665"` (`cxbottle.conf`) | lock section 1 |
| Runtime of the wrapper | `/bin/bash` 3.2.57 (macOS), `iconv`, `/usr/bin/lockf`, `pgrep`, `pkill`, `shasum`, `defaults`, `getconf` (macOS 26.6.2) | not separately locked (OS tools) |
| Runtime of the test module | TV-001 interpreter (Python 3.13.5), standard library only | TV-001 |

**Install source:** LTspice from the Analog Devices macOS package, unversioned URL, no checksum published (lock section 7); the wrapper from the repository (CM plan Table 4-1 row 28). Commands for the identities: `git hash-object`, `shasum -a 256` (procedure part A and B).

## 2. Purposes covered

1. Run a committed netlist (`.net`, `.cir`, `.sp`) or schematic (`.asc`) deck headless with `-b`, or with `-ascii -b` for a raw file in text form, and deliver its `.log`, `.raw` and `.op.raw` beside the deck or in `-o OUTDIR`, for Analysis-class evidence whose pass or fail is judged by the deck's own checker.
2. Netlist a schematic with `-netlist` and reject any floating `NC_` net (research F9).
3. Never report a run as passed when LTspice did not complete it, or when the LTspice that ran is not the locked one: exit non-zero on a missing telemetry opt-out before or after the run; a bundle version that does not start with the locked program version `26.0.2`, a bundle build other than exactly `26.0.2.1`, or an `LTspice.exe` SHA-256 in the bottle other than the locked value (both checked before every run); a `-b` log whose first line is not `LTspice 26.0.2 for MacOS` (another version, or no version line); `-version` output other than `26.0.2`; a deck error in the log or a non-zero LTspice exit; a missing log or raw output; a floating net; a time-out (the run's own processes killed); a relative include outside the deck directory; and a Windows path of 260 characters or more.
4. Record the provenance of each run on stderr: log version line, deck SHA-256, LTspice exit status, elapsed time, outputs.

Not covered: the validity of device models (vendor or behavioural) and of convergence options in a deck; statistics of `.step` or Monte Carlo runs beyond what the deck's checker verifies; the numeric solver beyond the linear AC and transient known answers of section 3 (limitation 1).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/ltspice/` with `known-answers.json` (block `wrapper`; expected values written before the validation run). Circuits and analytic answers:

| Deck | Circuit | Known answer |
|---|---|---|
| `rc-lowpass.asc` (2026-09-25, unchanged) | V1 AC 1, R1 1 k, C1 159.155 nF, `.ac`, `.meas f3db` | f(-3 dB) = 1/(2 pi R C) = 999.9996 Hz within 1 % (the lock criterion); netlist lines of block `netlist`, no `NC_` |
| `rc-step-tran.net` (new) | 0 to 1 V step (1 ns ramp) into R1 1 k, C1 1 uF, `.tran 0 5m 0 1u uic` | V(out) at t = tau = 1 ms equals 1 - e^-1 = 0.6321206 V within 0.1 %; V(out) = 0.5 V at tau ln 2 = 0.6931472 ms within 0.1 % |
| `rc-include.net` with `sub/rc-parts.inc` (new) | the low-pass with R1 and C1 in a relative include | f(-3 dB) as above, proving the include was carried into the run directory |
| `rc-step-tran.net` with `-ascii -b` (block `ascii`) | the step response above | the raw file is an ASCII raw file (a `Values:` section of decimal numbers, no `Binary:` section; header in 8-bit text or UTF-16LE, research F7 and F8) and V(out) at t = 1 ms, interpolated linearly between the two stored points around 1 ms, equals 0.6321206 V within 0.1 %. The reader (`read_ascii_raw` in the test module) is itself checked on a stored sample in both encodings and rejects a `Binary:` section and a truncated file (`AsciiRawReaderTests`) |

Seeded faults, each with its expected exit status (section of `known-answers.json` in brackets):

| Seeded fault | Expected |
|---|---|
| `rc-seeded-error.net`: second analysis (`seeded_deck_error`) | exit 1, "More than one analysis specified." |
| `rc-nc-error.asc`: wire from R1 pin 2 removed (`seeded_floating_net`) | exit 1 with `NC_01` for `-netlist` and for `-b` (LTspice itself exits 0 and simulates) |
| `rc-include-escape.net`: include path with `..` (`seeded_include_escape`) | exit 2, nothing run |
| deck name of 215 characters (`seeded_long_path`) | exit 2, "limit 259" |
| `CWHT_LTSPICE_VERSION=26.1.1` (`seeded_version`) | exit 4 |
| `CWHT_LTSPICE_EXPECT_BUNDLE=26.0.2.2` (`seeded_bundle_build`): another bundle build of 26.0.2, which the prefix match of blob `102b93d4` accepted | exit 4, "LTspice bundle build is 26.0.2.1, expected 26.0.2.2" |
| `CWHT_LTSPICE_EXPECT_EXE_SHA256` = the locked hash with its last digit changed (`seeded_exe_sha256`) | exit 4, "LTspice.exe SHA-256 is ... expected ..." |
| `CWHT_LTSPICE_SUPPORT=<fixture>/fake-support` (`seeded_no_version_line`): a wine test double writes a `.log` without the version line and a `.raw`, exit 0 | exit 4, "not a version line" |
| `CWHT_LTSPICE_SUPPORT=/nonexistent` (`seeded_not_installed`) | exit 3, "not installed" |
| `CWHT_LTSPICE_INI_CHECK` naming `ini-without-key.ini`, `ini-ascii-key.ini` (the 8-bit line the withdrawn research precondition would have appended) or an absent file (`seeded_ini`) | exit 3 each; with `ini-with-key.ini` exit 0 |
| lock held by the test (`seeded_busy`, `CWHT_LTSPICE_LOCK_WAIT=2`) | exit 5 after waiting about 2 s |
| `rc-hang-error.asc` with `-t 15` (`timeout_guard`) | exit 124 between 15 and 30 s, "none left", no LTspice process of a wrapper run directory remains, a sentinel process whose command line names another `cwht-lts.*` directory survives |
| planted `rc-step-tran.op.raw` and `rc-step-tran.plt` in the output directory (`stale_outputs`) | the stale `.op.raw` removed, the user's `.plt` kept |

Plus usage cases (no arguments, mode without deck, unknown argument, bad `-t`, two modes, `-ascii` with `-netlist`: exit 2) and `-o` placing the outputs outside the deck directory.

The installed bundle and `LTspice.exe` cannot be changed for a seeded fault (they are the owner's installation). The two identity faults therefore seed the expected side through add-only hooks: `CWHT_LTSPICE_EXPECT_BUNDLE` and `CWHT_LTSPICE_EXPECT_EXE_SHA256` name a second value that must also match, and neither can replace the locked constants `LOCK_BUNDLE` and `LOCK_EXE_SHA256` of the wrapper. The same exact comparison (`must_equal`) serves the locked value and the hook, so the seeded fault shows that any difference fails with exit 4, and every case that reaches the precondition or LTspice (`PreconditionTests`, `LTspiceRunTests`, `OutputCheckTests`, `TimeoutGuardTests`) shows that the installed identities equal the locked ones.

**Run command** (the procedure, which also records identities, versions and the bottle state, and runs part D):

```
bash docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27.sh > docs/cm/tool-validation/evidence/ltspice-batch-<date>-run<N>.log.txt
```

Its part C is `CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py` from the repository root. Part D runs the bare `wine` command (under the wrapper's lock) on the transient deck placed at a Windows path of 262 characters, expecting exit 0 with no `.raw` and "Could not open" in the log (finding 1), then the wrapper on the same deck, expecting PASS (its run directory is short).

**Pass criteria:** part C exits 0 with 34 of the 35 tests run and passed: `UsageTests` 6, `HygieneTests` 5, `InstallAndVersionTests` 4, `LockTests` 1, `PreconditionTests` 3, `AsciiRawReaderTests` 2, `LTspiceRunTests` 11, `OutputCheckTests` 1, `TimeoutGuardTests` 1. The only permitted skip is `PreconditionTests.test_bottle_without_key`, which runs only while the bottle lacks the key and is skipped by design once it is present; any other skip means the case was not run. Part D as stated; part B shows the locked versions and the key present (count 1).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 10:57 | HEAD `e119181` with the wrapper (blob `884df077`), test module (blob `220db90b`) and fixtures unchanged from `41d150e` | Superseded by run 2 (the wrapper changed for finding 3). **Blocked, not a pass.** 29 tests, 18 passed (`UsageTests` 6, `HygieneTests` 5, `InstallAndVersionTests` 2, `LockTests` 1, `PreconditionTests` 4 including `test_bottle_without_key`, which ran because the bottle ini lacks the key), 11 skipped (`LTspiceRunTests` 10, `TimeoutGuardTests` 1: "bottle precondition not met"); part B: key count 0 in the bottle ini (420 bytes, modified 10:50); part D not run. Transcript `evidence/ltspice-batch-2026-09-27-run1.log.txt` |
| 2 | 2026-09-27 11:03 | HEAD `b41e544`, every identity of section 1 "unchanged from HEAD" | **Blocked, not a pass.** Same outcome as run 1: 29 tests, 18 passed, 11 skipped (bottle precondition not met); part B key count 0; part D not run. Transcript `evidence/ltspice-batch-2026-09-27-run2.log.txt` |
| 3 | 2026-09-27 11:56 | HEAD `c9d2c54` (wrapper `64e1c723`, test module `c75cb7b3`, fixture digest `b9f7ed3c...76cb`), every identity "unchanged from HEAD" | **Blocked, not a pass.** 35 tests, 22 passed (`UsageTests` 6, `HygieneTests` 5, `InstallAndVersionTests` 4 including the new `test_bundle_build_other_than_lock` and `test_exe_sha256_other_than_lock`, `LockTests` 1, `PreconditionTests` 4 including `test_bottle_without_key`, `AsciiRawReaderTests` 2), 13 skipped (`LTspiceRunTests` 11 including `test_ascii_raw_known_answer`, `OutputCheckTests` 1, `TimeoutGuardTests` 1: "bottle precondition not met"); part B: bundle `26.0.2.1`, Wine layer `25.0.1.38665`, `LTspice.exe` SHA-256 equal to section 1, key count 0 (ini 420 bytes, modified 10:50); part D not run. Transcript `evidence/ltspice-batch-2026-09-27-run3.log.txt` |
| 4 | after OA-TV014-1 | to be recorded (the committed blobs of run 3 unless a later fix changes them) | pending; the validation run INSP-038 finding-1 asks for |

Development observations on draft wrapper blobs (not a validation run): the AC, transient and include known answers passed on 2026-09-27 at 10:49 (f(-3 dB) 999.999642341 Hz; V(out)(tau) 0.632120367773 V, error 3.0e-7; t(0.5 V) 0.693147653 ms, error 6.8e-7), and the seeded deck error, floating net, include escape, ini and version faults gave the expected exits (`evidence/ltspice-batch-2026-09-27-development.log.txt` section 2). The 2026-09-25 sanity check of the bare command (lock section 1.1) reproduced the same f(-3 dB) value.

### 4.1 Findings of this validation

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | LTspice 26.0.2 under CrossOver exits 0 and writes only a log ("Could not open input deck for reading") when a Windows path it must open or write reaches 260 characters (MAX_PATH): the netlist of a schematic under the session scratchpad (`Z:\private\tmp\claude-501\...\rc-lowpass.net`, 264 characters) was never written and nothing was simulated. An exit status of 0 therefore does not prove a run | `evidence/ltspice-batch-2026-09-27-development.log.txt` section 1; procedure part D (run 3) | The wrapper runs every deck in a short directory under `getconf DARWIN_USER_TEMP_DIR`, refuses a run whose longest output path would reach 260 characters, requires a `.raw` or `.op.raw` after `-b`, and fails on "Could not open" in the log. Lock section 1.4 finding 12 |
| 2 | LTspice rewrites its whole `LTspice.ini` when it exits. Four wrapper runs started at the same moment (draft without a lock, 10:50) left the ini truncated to two recent-file entries: the `[Options]` section with `CaptureAnalytics=false` (the owner-ratified opt-out of ADR-018) was lost. Sequential runs had kept the key. The two hung 2026-09-25 processes of finding 3 were running throughout, during the sequential runs as well, so the concurrent exits are the only observed difference | `evidence/ltspice-batch-2026-09-27-development.log.txt` sections 3 to 5 and 7; runs 1 and 2 part B | The wrapper holds an flock(2) lock for the whole run, so runs through it never overlap, and re-checks the key after each run (exit 3, outputs not copied). The author did not edit the ini (08 briefing: if the key check fails, stop and report). No LTspice process has run since the loss, so no consent dialog was raised and no usage data sent. Owner action OA-TV014-1 restores the key; RSK cross item (the risk of a silent telemetry re-enable by a concurrent or crashed run). Lock section 1.4 finding 13 |
| 3 | `LTspice.exe` shows its deck as a Windows path (`Z:\var\folders\...\<dir>\rc-hang-error.asc`), so a time-out guard that matches the POSIX run directory with `pkill -f` or `pgrep -f` misses it. The 2026-09-25 hang checks used that match: two `LTspice.exe` processes they started (23:21:10 and 23:22:13, directories `kat-ltspice.RZ63Eg` and `kat-ltspice.lCte06`, parent `launchd`) were still running, hung, at 2026-09-27 11:02, and the transcript line "processes of this run still alive (expected none): none" was a false negative. The first wrapper blob `884df077` had the same defect | `evidence/ltspice-batch-2026-09-27-development.log.txt` section 7 | The wrapper (blob `102b93d4`) matches the unique directory name, which both path forms carry, and fails with exit 124 naming any survivor after SIGKILL; the time-out test looks for survivors in either form. The two orphans were terminated by PID at 11:02 (`kill`, SIGTERM), the bottle ini unchanged (SHA-256 before and after). The lock section 1.1 LTspice row statement "killed at 30 s" for 2026-09-25 is corrected by lock section 1.4 finding 14 |
| 4 | LTspice `-b` on a schematic that carries a deck error does not exit (2026-09-25, lock section 1.4 finding 2) | lock section 1.1 LTspice row | Covered by the time-out guard case; decks for the record remain netlists or are netlisted first |

## 5. Reproducibility

Not required for class B. Observed: the f(-3 dB) value 999.999642341 Hz was identical in the 2026-09-25 runs 3 and 4, the 2026-09-27 sequential run and each of the four concurrent runs (development log sections 2 and 3). Run 3 records whether it repeats.

## 6. Limitations

1. Solver validation is limited to linear first-order RC circuits (AC magnitude and transient step). Nonlinear devices, vendor models, noise, FFT and `.step` statistics are not validated by this record; each analysis record validates its own models (for example against a datasheet curve) and cites this record only for the run itself.
2. The include scan follows `.include`, `.inc` and `.lib` directives written on one line (also inside a schematic `TEXT ... !` directive). Files named in other ways (a `PWL file=`, `.wave`, a `.lib` inside a multi-line schematic directive) are not copied; LTspice then fails on the missing file, which the failure strings catch, so the result is a refusal, not a wrong answer.
3. The failure-string list of the wrapper (header, `FAIL_STRINGS`) is empirical. A deck's checker must still confirm that every measurement it needs is present in the log or the raw file.
4. The post-run key check cannot be exercised by a seeded fault without editing the owner's bottle ini; it is verified by inspection of the code and by the observed incident of finding 2.
5. The lock covers runs made through the wrapper. A bare `wine` run (the pre-wrapper command of the 08 briefing) bypasses it; from this commit every LTspice run is made through the wrapper (08 briefing COMMANDS line; lock section 1 row).
6. The time-out kill matches the run's unique directory name and then the launcher's process tree. A process LTspice might start without the name in its command line and outside that tree would survive; the wrapper then reports it and fails, but does not kill it.
7. The wrapper runs on macOS only (`getconf DARWIN_USER_TEMP_DIR`, `/usr/bin/lockf`, `defaults`).
8. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).
9. The per-run identity check covers the bundle build (`CFBundleShortVersionString`, exact) and `LTspice.exe` in the bottle (SHA-256). The CrossOver Wine layer ships inside the bundle and is covered by the exact bundle build; it is not hashed per run, and a change of it or of another bottle file is caught by the section 7 triggers through the lock re-observation of procedure part B (`cxbottle.conf` version). With `CWHT_LTSPICE_SUPPORT` set (a test hook) the bundle check is skipped; runs for the record are made without it.

## 7. Re-validation triggers

- Any change of `tools/ltspice-batch.sh`, `tools/tests/test_ltspice_batch.py` or `tools/tests/fixtures/ltspice/` (CM plan section 9.2 step 4).
- A change of the LTspice bundle version, of the `LTspice.exe` SHA-256, of the CrossOver layer version or a rebuild of the bottle; a macOS major version change.
- A change of the interpreter (TV-001) for the test module.
- A defect found in the wrapper or in LTspice (an NCR per SWE-201), including any run that loses the bottle key again.

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (one record for TV-014 to TV-019, one section per tool; `docs/plan/pdr-work-plan.md` WP-PDR-07), with the code checklist and the tool-validation checklist of WP-PDR-03. The reviewer re-runs the procedure after run 3 (or reads the run 3 transcript), recomputes the analytic answers of section 3 from the circuit values, and checks each seeded fault against the wrapper code.

## 9. Accreditation (owner)

Proposed scope statement **ACC-LTSPICE-001**: "Accredited for purposes 1 to 4 for `tools/ltspice-batch.sh` at git blob `64e1c7230278363bca85542f410da5a0853a42f2` (commit `c9d2c54`, or the blob of the validation run if a later fix changes it) with LTspice 26.0.2 (bundle build 26.0.2.1 and `LTspice.exe` SHA-256 `a94eb178...793f06`, both checked by the wrapper before every run) in the CrossOver bottle 25.0.1.38665 (covered by the bundle build and re-observed by procedure part B), within the limitations of section 6."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, OD-24b at B0, after run 3 passes and the section 8 review is APPROVED) | | |
