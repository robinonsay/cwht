# TV-014: LTspice 26.0.2 through tools/ltspice-batch.sh (git blob 102b93d4, commit b41e544)

| Field | Value |
|---|---|
| Record | TV-014 |
| Status | **Not yet validated.** Known-answer run 2 (2026-09-27 11:03, commit `b41e544`) passed the 18 cases that stop before LTspice runs; the 11 cases that run LTspice and procedure part D are blocked because the bottle `LTspice.ini` lost `CaptureAnalytics=false` during development (finding 2; owner action OA-TV014-1). Run 3 follows the owner's restore. Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: LTspice through the CrossOver wrapper, Analysis-class simulation evidence) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6, validated and accredited simulation tools) through CM plan section 9; ADR-018 (telemetry opt-out) |
| Due | PDR (CM plan section 13 PDR row). It blocks every LTspice result cited as evidence (`docs/plan/pdr-work-plan.md` WP-PDR-07, WP-PDR-19 to 26 and 28) until accredited (owner decision OD-24b) |
| Lock rows | `tools/toolchain.lock.md` section 1 rows LTspice and LTspice Wine layer; section 1.1 row LTspice; section 1.2 row `tools/ltspice-batch.sh`; section 1.4 findings 12 to 14; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 0) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/ltspice-batch.sh` | git blob `102b93d49a01b31d91088f0e2c5a23c2e7a6eddc`, SHA-256 `a6acffa675e007481d7b37a1b5ce5150a1d236ed2cab78bf4d964c9219265152`, mode 100755 | committed in `b41e544` (first version, blob `884df077`, in `41d150e`; changed for finding 3) |
| `tools/tests/test_ltspice_batch.py` | git blob `c44104477c05eeb36493da9f35e3b75e2e241eb7`, SHA-256 `841a3b931688f33a0f67025e0b358cd3f8c488d4cb3409117aa75069f3750a32` | committed in `b41e544` (first version, blob `220db90b`, in `41d150e`) |
| `tools/tests/fixtures/ltspice/` | 12 files, tree digest `069f03eed71724c5312ad51f1c40ec032023258ee38a5fcf7a57caf7a0992835` (SHA-256 of the sorted `shasum -a 256` list; the list is in the run 1 and run 2 transcripts) | committed in `41d150e` (the three 2026-09-25 decks unchanged; `known-answers.json` gained the `wrapper` block, its earlier blocks unchanged) |
| LTspice program | `26.0.2` (`tools/ltspice-batch.sh -version`; bare command `wine --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' -version`, 2026-09-25) | lock section 1 |
| LTspice bundle | `26.0.2.1` (`defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString`, 2026-09-27) | lock section 1 |
| `LTspice.exe` in the bottle | SHA-256 `a94eb1789084db9f46375cce05110e03578f9cdb931867a0faaca5b200793f06` (`drive_c/Program Files/ADI/LTspice/LTspice.exe`, 2026-09-27; RSK mitigation step S1 asks for this pin) | recorded here first; lock section 1 row |
| CrossOver Wine layer | `"Version" = "25.0.1.38665"` (`cxbottle.conf`) | lock section 1 |
| Runtime of the wrapper | `/bin/bash` 3.2.57 (macOS), `iconv`, `/usr/bin/lockf`, `pgrep`, `pkill`, `shasum`, `defaults`, `getconf` (macOS 26.6.2) | not separately locked (OS tools) |
| Runtime of the test module | TV-001 interpreter (Python 3.13.5), standard library only | TV-001 |

**Install source:** LTspice from the Analog Devices macOS package, unversioned URL, no checksum published (lock section 7); the wrapper from the repository (CM plan Table 4-1 row 28). Commands for the identities: `git hash-object`, `shasum -a 256` (procedure part A and B).

## 2. Purposes covered

1. Run a committed netlist (`.net`, `.cir`, `.sp`) or schematic (`.asc`) deck headless with `-b` (optionally `-ascii`) and deliver its `.log`, `.raw` and `.op.raw` beside the deck or in `-o OUTDIR`, for Analysis-class evidence whose pass or fail is judged by the deck's own checker.
2. Netlist a schematic with `-netlist` and reject any floating `NC_` net (research F9).
3. Never report a run as passed when LTspice did not complete it: exit non-zero on a missing telemetry opt-out before or after the run, a program or bundle version other than the lock, a deck error in the log or a non-zero LTspice exit, a missing log or raw output, a floating net, a time-out (the run's own processes killed), a relative include outside the deck directory, and a Windows path of 260 characters or more.
4. Record the provenance of each run on stderr: log version line, deck SHA-256, LTspice exit status, elapsed time, outputs.

Not covered: the validity of device models (vendor or behavioural) and of convergence options in a deck; statistics of `.step` or Monte Carlo runs beyond what the deck's checker verifies; the numeric solver beyond the linear AC and transient known answers of section 3 (limitation 1).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/ltspice/` with `known-answers.json` (block `wrapper`; expected values written before the validation run). Circuits and analytic answers:

| Deck | Circuit | Known answer |
|---|---|---|
| `rc-lowpass.asc` (2026-09-25, unchanged) | V1 AC 1, R1 1 k, C1 159.155 nF, `.ac`, `.meas f3db` | f(-3 dB) = 1/(2 pi R C) = 999.9996 Hz within 1 % (the lock criterion); netlist lines of block `netlist`, no `NC_` |
| `rc-step-tran.net` (new) | 0 to 1 V step (1 ns ramp) into R1 1 k, C1 1 uF, `.tran 0 5m 0 1u uic` | V(out) at t = tau = 1 ms equals 1 - e^-1 = 0.6321206 V within 0.1 %; V(out) = 0.5 V at tau ln 2 = 0.6931472 ms within 0.1 % |
| `rc-include.net` with `sub/rc-parts.inc` (new) | the low-pass with R1 and C1 in a relative include | f(-3 dB) as above, proving the include was carried into the run directory |

Seeded faults, each with its expected exit status (section of `known-answers.json` in brackets):

| Seeded fault | Expected |
|---|---|
| `rc-seeded-error.net`: second analysis (`seeded_deck_error`) | exit 1, "More than one analysis specified." |
| `rc-nc-error.asc`: wire from R1 pin 2 removed (`seeded_floating_net`) | exit 1 with `NC_01` for `-netlist` and for `-b` (LTspice itself exits 0 and simulates) |
| `rc-include-escape.net`: include path with `..` (`seeded_include_escape`) | exit 2, nothing run |
| deck name of 215 characters (`seeded_long_path`) | exit 2, "limit 259" |
| `CWHT_LTSPICE_VERSION=26.1.1` (`seeded_version`) | exit 4 |
| `CWHT_LTSPICE_SUPPORT=/nonexistent` (`seeded_not_installed`) | exit 3, "not installed" |
| `CWHT_LTSPICE_INI_CHECK` naming `ini-without-key.ini`, `ini-ascii-key.ini` (the 8-bit line the withdrawn research precondition would have appended) or an absent file (`seeded_ini`) | exit 3 each; with `ini-with-key.ini` exit 0 |
| lock held by the test (`seeded_busy`, `CWHT_LTSPICE_LOCK_WAIT=2`) | exit 5 after waiting about 2 s |
| `rc-hang-error.asc` with `-t 15` (`timeout_guard`) | exit 124 between 15 and 30 s, "none left", no LTspice process of a wrapper run directory remains, a sentinel process whose command line names another `cwht-lts.*` directory survives |
| planted `rc-step-tran.op.raw` and `rc-step-tran.plt` in the output directory (`stale_outputs`) | the stale `.op.raw` removed, the user's `.plt` kept |

Plus usage cases (no arguments, mode without deck, unknown argument, bad `-t`, two modes, `-ascii` with `-netlist`: exit 2) and `-o` placing the outputs outside the deck directory.

**Run command** (the procedure, which also records identities, versions and the bottle state, and runs part D):

```
bash docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27.sh > docs/cm/tool-validation/evidence/ltspice-batch-<date>-run<N>.log.txt
```

Its part C is `CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py` from the repository root. Part D runs the bare `wine` command (under the wrapper's lock) on the transient deck placed at a Windows path of 262 characters, expecting exit 0 with no `.raw` and "Could not open" in the log (finding 1), then the wrapper on the same deck, expecting PASS (its run directory is short).

**Pass criteria:** part C exits 0 with 28 of the 29 tests run and passed: `UsageTests` 6, `HygieneTests` 5, `InstallAndVersionTests` 2, `LockTests` 1, `PreconditionTests` 3, `LTspiceRunTests` 10, `TimeoutGuardTests` 1. The only permitted skip is `PreconditionTests.test_bottle_without_key`, which runs only while the bottle lacks the key and is skipped by design once it is present; any other skip means the case was not run. Part D as stated; part B shows the locked versions and the key present (count 1).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 10:57 | HEAD `e119181` with the wrapper (blob `884df077`), test module (blob `220db90b`) and fixtures unchanged from `41d150e` | Superseded by run 2 (the wrapper changed for finding 3). **Blocked, not a pass.** 29 tests, 18 passed (`UsageTests` 6, `HygieneTests` 5, `InstallAndVersionTests` 2, `LockTests` 1, `PreconditionTests` 4 including `test_bottle_without_key`, which ran because the bottle ini lacks the key), 11 skipped (`LTspiceRunTests` 10, `TimeoutGuardTests` 1: "bottle precondition not met"); part B: key count 0 in the bottle ini (420 bytes, modified 10:50); part D not run. Transcript `evidence/ltspice-batch-2026-09-27-run1.log.txt` |
| 2 | 2026-09-27 11:03 | HEAD `b41e544`, every identity of section 1 "unchanged from HEAD" | **Blocked, not a pass.** Same outcome as run 1: 29 tests, 18 passed, 11 skipped (bottle precondition not met); part B key count 0; part D not run. Transcript `evidence/ltspice-batch-2026-09-27-run2.log.txt` |
| 3 | after OA-TV014-1 | to be recorded | pending |

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

## 7. Re-validation triggers

- Any change of `tools/ltspice-batch.sh`, `tools/tests/test_ltspice_batch.py` or `tools/tests/fixtures/ltspice/` (CM plan section 9.2 step 4).
- A change of the LTspice bundle version, of the `LTspice.exe` SHA-256, of the CrossOver layer version or a rebuild of the bottle; a macOS major version change.
- A change of the interpreter (TV-001) for the test module.
- A defect found in the wrapper or in LTspice (an NCR per SWE-201), including any run that loses the bottle key again.

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (one record for TV-014 to TV-019, one section per tool; `docs/plan/pdr-work-plan.md` WP-PDR-07), with the code checklist and the tool-validation checklist of WP-PDR-03. The reviewer re-runs the procedure after run 3 (or reads the run 3 transcript), recomputes the analytic answers of section 3 from the circuit values, and checks each seeded fault against the wrapper code.

## 9. Accreditation (owner)

Proposed scope statement **ACC-LTSPICE-001**: "Accredited for purposes 1 to 4 for `tools/ltspice-batch.sh` at git blob `102b93d49a01b31d91088f0e2c5a23c2e7a6eddc` (commit `b41e544`) with LTspice 26.0.2 (bundle 26.0.2.1, `LTspice.exe` SHA-256 `a94eb178...793f06`) in the CrossOver bottle 25.0.1.38665, within the limitations of section 6."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, OD-24b at B0, after run 3 passes and the section 8 review is APPROVED) | | |
