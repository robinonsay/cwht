---
test_case: TC-SW-TOOL-001
run: 4
requirement_ids: [REQ-SYS-127, REQ-SYS-133]
validates: []
verification_method: Demonstration
type: Bench
credit: false
result: Blocked
date: 2026-09-26
conductor: claude
witness: owner
article: pico2-devboard-1
firmware_version: "n/a"
source_commit: "0bcea39554d684ba28d6680208a523fd79a8ebba"
firmware_elf_sha256: "388d1d16dae55d33fcc0c69d33689abcf6d056bcc16e44a18abab2ac2300a5bf"
requirements_baseline: "none (SRR approved with liens 2026-09-26; baseline/srr not yet tagged)"
procedure_commit: "7647516"
procedure_blob: "fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
toolchain_lock: "tools/toolchain.lock.md blob 0ad60317be7e509c1e1968d2d9f4813f3904253f at 7647516 (HEAD during the owner steps; picotool row 2.3.0)"
harness_versions: "n/a"
instruments:
  - "Host USB port; owner's Mac (macOS 26.6.2, arm64) with picotool v2.3.0 at /opt/homebrew/bin/picotool (tools/toolchain.lock.md picotool row); USB 5 V supply and BOOTSEL load path only; no calibration applicable"
  - "Stopwatch; owner's phone clock; 60 s count window; not a credited instrument (credit false); no calibration applicable"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step11-info.txt sha256=48ad52739fbb949255596d3cce41ec344132f1bf87e0b27bd5af385dfbb9e747"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step11-load.txt sha256=6d65db16522fac21256d16f852c072f7913e76c3dd4ac099f53b137db7c9f325"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step11-observation.txt sha256=48f8e5411ed9f12ca81ade3593a15a2e0e6e8b41b19fc71b5e7675d04c0af217"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step12-load.txt sha256=a76298f0f62e335f7a568f3d4f6d04adf14fe860b20124c82fbdea8398f00d30"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/step12-observation.txt sha256=eb79cf6fddcf3717b3d57243cb7b7f231c66ae498fd1e45153f731469a0e8aab"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/kat-target.elf sha256=3201d382b9b1e32ec69da84ae966fd40671ecd820e32de6ef3135fb69f66df7d"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/kat-target.uf2 sha256=f8ef643e2f4cb15a3a6bdc2c3a913d1f741381c3fea84179e2df2617973ec093"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/kat-target-1byte.elf sha256=a669b565b9a3cf9f40b3e21758613ac1f4c494ed8da1cf460a798b61fc076b73"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/oa2-verify.txt sha256=5cbb3c3aaf36ce1a94319fd843170f1e64224a022d5bd2f97b5e2fc80721336b"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/oa2-observation.txt sha256=779a70226b38e4bb95a9ea972ec9377851b824af1d9aebcde37e7b0288403b13"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/image-identity.txt sha256=bbe83968119a2e18268944537f6c8d2f34295ecfe095e57b1b4ef3eae20c8039"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/complexity-invocation-check.sh sha256=6d0ced0172872c5eb426f2b96b6ab72cdf54db86c40a27f652035ae8b113a9de"
  - "docs/vv/reports/TC-SW-TOOL-001-r4/complexity-invocation-check.txt sha256=06291c458696d58c0906c44c06dde8105c8391ff283792bbaa0448838a749e08"
mop_values: []
---

# Verification report: TC-SW-TOOL-001 run 4

**Status of this run: Blocked (the case); every step run in it passes.** Run 4 is the owner-step subset of the case. It holds steps 11 and 12 (package opening action OA-1) and the OA-2 `picotool verify` known-answer check. Claude ran these with the owner on 2026-09-26 between 19:17 and 19:23 CDT, during the SRR session, and ran every command. All three pass (section 4). The case result stays Blocked because its acceptance needs `tools/sw_gate.sh` to exit 0 in step 6. That is not met in any run yet: run 3 has 2 FAIL (G5 complexity and G5 Miri). Gate steps G0 to G6 are not part of run 4. They run as run 5 (section 9). This is a dev-board case: `credit: false`, credit row `SUPPORT`. It changes the status of no requirement (docs/process/04-verification-and-validation.md section 4, rule 7.3.12). Runs 1 to 3 are not edited.

**Where the raw outputs come from.** The outputs were written during the session to Claude's scratch directory (`flash-run/`). The SRR minutes, "OA-1 and OA-2 performed" (commit `0a6f461`), file them with this run. Every file of that directory is copied here unchanged (`cmp` against the scratch copies, exit 0 for all ten), with its SHA-256 in the front matter.

## 1. Objectives and degree to which they were met

The case, its objective and its requirements are unchanged (case blob `fee1e724`, the same at `7647516`, during the run, and at the time of filing). Run 4 covers the on-board part of the FW-B0 exit criterion of docs/process/07-software-engineering-plan.md section 3.2 (SRR package item H12, entrance row 20 owner part, post-ruling item R16 (a)). It also covers the `verify` part of the picotool sanity check of `tools/toolchain.lock.md` section 1.1 (package OA-2).

| Requirement | Acceptance criterion (this case) | Measured or observed, run 4 | Met? |
|---|---|---|---|
| REQ-SYS-127 | Rust workspace builds for `thumbv8m.main-none-eabihf` against rustos by path; image runs on a Pico 2 | `cwht-app.uf2` (the run 3 image, byte for byte) loaded and verified by `picotool load -v`; after `picotool reboot` the LED blinked 18 times in 60 s (window 3 to 45). The build part is run 3 | Partially (supporting only; closes by Inspection, row I) |
| REQ-SYS-133 | `picotool load -v` of both UF2 images succeeds and the images run | Both loads report "Verifying Flash ... OK", exit 0. Both reboots exit 0. Blinky 60 to 63 cycles in 60 s (window 10 to 120); cwht-app 18 cycles in 60 s (window 3 to 45) | Met for this case (supporting only; closes by Demonstration on the delivered unit, row D) |

REQ-SYS-128 (host build and test) is not addressed by run 4. Run 3 records it.

## 2. Description of the activity and deviations

The owner brought the Pico 2 during the SRR session (minutes, owner statement, verbatim: "I grabbed the pico so I'm ready to test the flash whenever you are."). This reversed the deferral of OA-1 and OA-2 to PDR recorded earlier in the same minutes. Order of execution, from the time stamps in the raw outputs:

- step 11 `picotool info -d` 19:17:51 (`step11-info.txt`);
- step 11 `picotool load -v` and `picotool reboot` 19:18:04 (`step11-load.txt`);
- owner count transcribed 19:20:04 (`step11-observation.txt`);
- step 12 `picotool info -d`, `load -v` and `reboot` 19:20:35 (`step12-load.txt`);
- owner count transcribed 19:22:34 (`step12-observation.txt`);
- OA-2 `picotool uf2 convert` of the fixture ELF (19:22 file times), then `info -d`, `load`, `verify` of the true ELF and `verify` of the altered copy, 19:23:35 (`oa2-verify.txt`, `oa2-observation.txt`).

Board: bare Pico 2 marked "1" by the owner (article `pico2-devboard-1`); chip id `0xf9c6e0eff60605d1`, RP2350, package QFN60, 4096K flash, secure boot 0 (all three `info -d` outputs agree). picotool v2.3.0 at `/opt/homebrew/bin/picotool`, the lock row.

Deviations from the case, and from runs 1 to 3 (none affects credit, because the run carries none):

- D16 (new). **Artifact names.** The case's `expected_artifacts` name `flash-rustos-blinky.txt` and `flash-cwht-app.txt`. Run 4 files the raw outputs as written during the session, unchanged. Step 11 is in `step11-info.txt`, `step11-load.txt` and `step11-observation.txt`. Step 12 is in `step12-load.txt` (the `info -d` output included) and `step12-observation.txt`. The content is what the two named artifacts describe: `info -d`, `load -v` and `reboot` output, and the owner's 60 s count.
- D17 (new). **Images loaded from the run 1 paths.** Steps 11 and 12 name `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2` and `.../cwht-app.uf2`, and those paths were loaded, as the case says. They are byte-identical to the run 2 and run 3 files (section 3), so run 4 binds the result to the run 3 build (`source_commit` `0bcea39`, `firmware_elf_sha256` of the run 3 `cwht-app.elf`).
- D18 (new). **OA-2 loads the UF2.** Package OA-2 says to load `kat-target.elf`. The run converted the fixture ELF with `picotool uf2 convert --family rp2350-arm-s`, checked the result against the known-answer UF2 SHA-256, and loaded that UF2. It then ran `picotool verify` against the ELF. The verify comparison is the same either way, and the UF2 check adds the `uf2 convert` known answer on the image actually loaded.
- D19 (new). **Owner steps filed apart from the gate steps.** Run 3 (19:28 to 19:41) started after these owner steps. It recorded steps 11 and 12 as not run in run 3 and named run 4 for their raw outputs. Steps 1 to 10 are not repeated in run 4.
- Step 12 of the case has the owner unplug the board and re-enter BOOTSEL. `step12-load.txt` shows the device listed by `picotool info -d` in BOOTSEL mode before the load, which is the observable result of that action.

## 3. Configuration under test and differences from the operational configuration

- Article: `pico2-devboard-1`, a bare Raspberry Pi Pico 2 with nothing connected except its micro-USB cable to the owner's Mac.
- Images: `rustos-blinky.uf2` and `cwht-app.uf2`. `image-identity.txt` shows the identity with the run 3 artifacts:
  - The SHA-256 recorded at load time (`step11-load.txt`, `step12-load.txt`) equals the SHA-256 now, and both equal the run 2 and run 3 files. Blinky `c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3` (`c45b5268...08d3`). cwht-app `4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529` (`4e0bd133...3529`). Both equal the run 3 front matter.
  - `cmp` of the run 1 file against the run 3 file exits 0 for both images.
  - The git blobs of the run 1 and run 3 files are the same (`f0e9fb34` blinky, `640951c4` cwht-app) and equal `HEAD`.

  The run 3 UF2 files were built from cwht `0bcea39` against the rustos branch commit `2ec64c0` (run 3 section 3). Their loadable content equals runs 1 and 2, because the rustos work item added comment lines only.
- OA-2 fixture: `kat-target.elf` equals `tools/tests/fixtures/picotool/kat-target.elf` (committed in `1d423e5`): SHA-256 `3201d382...df7d`, `cmp` exit 0. That equals the `elf.sha256` of `known-answers.json` (blob `b0cf4540`). `kat-target.uf2` from `picotool uf2 convert` has SHA-256 `f8ef643e...c093`, which equals the `uf2_convert.sha256` known answer. `kat-target-1byte.elf` differs from the true ELF in exactly one byte (`cmp -l`: file offset `0x1002f`, octal 253 to 124, `0xab` to `0x54`), which maps to flash address `0x1000002f`.
- Host: picotool v2.3.0 (Darwin, AppleClang-21.0.0.21000099, Release), equal to the lock row. `shasum` (lock row) and the macOS `cmp` made the hash and byte comparisons. picotool is not yet Accredited (TV due CDR), so its outputs are developer evidence (CM plan section 9.1). The run carries `credit: false` in any case.
- Differences from the operational configuration: as run 1 section 3 (dev board, not the delivered unit; no RF, keyer or display hardware; ring oscillator clock, no configured clock tree).

## 4. Results of each step

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 to 10 | Configuration, builds, lint, gate, known-answer runs, blinky build, UF2 conversion, blink-rate prediction | as the case | **Not in run 4** (D19). Run 3 records them; the gate steps run again as run 5 | run 3 | Not run |
| 11 | Flash and observe the rustos blinky: `picotool info -d`, `picotool load -v docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2`, `picotool reboot`; owner counts off-to-on transitions for 60 s | device listed in BOOTSEL; load verified; reboot exit 0; 10 to 120 cycles in 60 s | `info -d`: RP2350, chip id `0xf9c6e0eff60605d1`, 4096K flash, exit 0. `load -v`: "Loading into Flash ... 100%", "Verifying Flash ... 100%", "OK", exit 0. `reboot`: "The device was rebooted into application mode.", exit 0. Owner statement, verbatim (minutes): "On/Off time looks about equal and it blinked about 60-63 times in 60s. It's not exactly 1 second but its close". Count 60 to 63, inside the window 10 to 120 and the step 10 prediction window 13 to 114 (about 63 predicted); duty about equal | `step11-info.txt`, `step11-load.txt`, `step11-observation.txt` | Pass |
| 12 | Flash and observe cwht-app: re-enter BOOTSEL; `picotool info -d`, `picotool load -v docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2`, `picotool reboot`; owner counts for 60 s | device listed in BOOTSEL; load verified; reboot exit 0; 3 to 45 cycles in 60 s | `info -d`: the same board (chip id `0xf9c6e0eff60605d1`), exit 0. `load -v`: "Verifying Flash ... 100%", "OK", exit 0. `reboot`: exit 0. Owner statements, verbatim (minutes): "Yes that looks correct", then, asked for the timed count, "18 in 60s". Count 18, inside the window 3 to 45 and the prediction window 5 to 39 (about 16 predicted) | `step12-load.txt`, `step12-observation.txt` | Pass |
| OA-2 | picotool `verify` known answer (lock section 1.1 picotool row): convert the fixture ELF, load it, verify the true ELF (expect pass), verify a copy with one byte changed (expect fail) | UF2 equals the known answer; true ELF verify OK, exit 0; altered copy reports a mismatch at the altered address, non-zero exit | `uf2 convert` output `f8ef643e...c093` equals the known answer. `load` exit 0. `verify kat-target.elf`: "OK", exit 0. `verify kat-target-1byte.elf`: "First mismatch at 0x1000002f", the row at `0x10000020` showing `54` against `ab` in its last column, "ERROR: The device contents did not match the file", exit 245. No owner observation needed (minutes: "none needed") | `oa2-verify.txt`, `oa2-observation.txt`, `kat-target.elf`, `kat-target.uf2`, `kat-target-1byte.elf`, `image-identity.txt` | Pass |
| 13 | Record versions, commits, blob and hashes | recorded | this report and its front matter; `image-identity.txt` | this file | Pass |
| 14 | Stop rule | NCR on discrepancy | no discrepancy in the steps run | none | n/a |

## 5. Analysis of results

- **Both images load and run over the USB bootrom.** `picotool load -v` read back and compared every flashed byte ("Verifying Flash ... OK") for both images, and each image ran after `reboot`. The rustos blinky and cwht-app both start from the RP2350 boot path and toggle the LED. This is the observable FW-B0 result on the target.
- **The counts fall inside the predicted windows.** Blinky: 60 to 63 against about 63 predicted. cwht-app: 18 against about 16 predicted. The ratio is about 3.4, against the predicted 3.8 of the loop analysis (run 1 section 5), so neither image runs from a clock wrong by a large factor. The owner counted by eye against the phone clock over 60 s. The count is a coarse check, as the case intends (run 1 section 5). It gives no timing claim.
- **The verify decision discriminates.** The true image verifies (exit 0). A copy that differs in one byte fails at exactly that address (exit 245). This closes the `verify` part of the picotool sanity check, which was blocked since 2026-09-25 for want of a device (lock section 1.4 finding 6). The picotool TV record remains due CDR.
- **Identity.** The images loaded are byte-identical to the run 3 artifacts. The OA-2 inputs are byte-identical to the committed fixture and its known answers (section 3). The run 4 results therefore apply to the run 3 build without a rebuild.

## 6. Data tables, plots and pictures

All data are text logs and binaries in `docs/vv/reports/TC-SW-TOOL-001-r4/`, listed with SHA-256 in the front matter. No plot or photograph was taken. The owner reported the counts by voice and Claude transcribed them in the `*-observation.txt` files. `image-identity.txt` holds the hash and byte comparisons of section 3.

| Item | Window | Prediction (step 10, run 1) | Observed | Result |
|---|---|---|---|---|
| Blinky cycles in 60 s | 10 to 120 | 13 to 114, about 63 | 60 to 63 | Pass |
| cwht-app cycles in 60 s | 3 to 45 | 5 to 39, about 16 | 18 | Pass |
| `verify` true image | exit 0 | | exit 0, OK | Pass |
| `verify` one-byte-altered copy | non-zero, mismatch at `0x1000002f` | | exit 245, "First mismatch at 0x1000002f" | Pass |

`complexity-invocation-check.sh` and `complexity-invocation-check.txt` are not case steps. They are the tool maintainer's check of the `tools/sw_gate.sh` fix for INSP-016 finding-14 (run 3 item B8, section 7). They are filed here as run 3 filed `complexity-diagnostic.txt`, because run 5 is the next gate run that uses the fix.

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

Status of the run 3 blocking items. The owner's close-out decisions are those of the SRR minutes, "Close-out decisions (after the first close-out run)": owner statement, verbatim, "I concur with your recommendations", with items 1 to 12 ruled as recommended.

| # | Gate line or item | Status after run 4 | Closes on | Owner |
|---|---|---|---|---|
| B1, B2 | `G5 cargo deny`, `G5 unsafe audit` | The owner merged the rustos branch (fast-forward `c54d35a` to `2ec64c0`, minutes). CR-004 (lock pin to `2ec64c0`, with `firmware/unsafe-audit.md` regenerated in the same commit) is approved under close-out decision 1. The lock section 3 pin still reads `c54d35a` at the time of filing | the CR-004 commit, then run 5 | CR-004 implementer |
| B7 | steps 11 and 12 | **Closed by this run** (Pass) | closed | none |
| B8 | `G5 complexity` (invocation) | **Fixed.** `tools/sw_gate.sh` blob `52b9f803` passes one `--paths` per path (INSP-016 finding-14). The gate's own G5 complexity block, run outside the gate on `git archive` layouts, reads all three roots (20 files, 52 functions) and reaches `tools/complexity_gate.py`. The superseded form reproduces the argument error (`complexity-invocation-check.txt`; lock section 1.2 `tools/sw_gate.sh` row) | gate integration in run 5 | none |
| B9 | `G5 complexity` (convention) | The owner ruled close-out decision 4: the analyzer's counts are the measure, `tools/complexity_gate.py` adds one per `let ... else`, the two CS-19 halt loops get a +1 CS-38 allowance by the CR-001 mechanism, and the limit stays 15. It is applied by a CR. Until then the block reports the one CS-38 failure `safe_state_halt` CC 2, as in run 3 | that CR, the `tools/complexity_gate.py` change and the TV-012 re-validation, then run 5 | 07 owner (Claude) |
| B10 | `G5 Miri` | The owner approved the `rust-src` component on `nightly-2026-08-24` and the Miri sysroot crate download (close-out decision 2). The download is not made yet | the approved download, recorded in the lock, then run 5 | tool owner (Claude) |

## 8. Status of enabling equipment after the run

- Board `pico2-devboard-1`: last loaded with `kat-target.uf2` (OA-2). It holds no project image. The next dev-board run reloads its image by the case procedure.
- picotool 2.3.0, unchanged. `brew pin picotool` has not been run: the lock proposes it at the picotool TV.
- cwht repository: unchanged by the owner steps. After them, this filing changed `tools/sw_gate.sh` (B8) and `tools/toolchain.lock.md` (the picotool and gate rows).
- rustos: the owner's checkout `/Users/robinonsay/rust/rustos` is at `2ec64c0` on `master`. It was fast-forwarded by the owner at 20:45:59 CDT (reflog). The repository gate's G0 compares this with the lock pin `c54d35a`, so it stops at G0 until CR-004 moves the pin. The run 4 check did not use the checkout: it read rustos only through `git archive` of `c54d35a` and `2ec64c0`.

## 9. Conclusions and recommendations

Verdict: Blocked (the case). Steps 11 and 12 and the OA-2 `verify` known answer pass on the owner's Pico 2 with images byte-identical to run 3. This closes run 3 item B7, the owner part of SRR entrance row 20, and the `verify` part of the picotool sanity check (lock section 1.1, now passed; `tools/toolchain.lock.md` updated). The FW-B0 exit criterion, gate exit 0, is still not met. No requirement status changes (dev-board case, `credit: false`).

Recommendations:

1. CR-004 implementer: move the lock section 3 pin to `2ec64c0` and regenerate `firmware/unsafe-audit.md` in the same commit (close-out decision 1; B1, B2).
2. Tool owner (Claude): make the approved `rust-src` and Miri sysroot download and record it in the lock (close-out decision 2; B10). Also accept rustup 1.29.1 and run `rustup set auto-self-update disable` (close-out decision 3; lock section 1.4 finding 7).
3. 07 owner (Claude): apply the complexity convention of close-out decision 4 by its CR. Change `tools/complexity_gate.py` (one per `let ... else`, the halt-loop allowance), and re-validate TV-012 with `rca.json` re-derived from real analyzer output (B9).
4. Claude: after items 1 to 3, run run 5. That is the gate part of the case, steps 1 to 10 and 13 (steps 6 and 7 are the full gate and KA-0 to KA-8 on the pinned rustos), with `rust-src` installed under close-out decision 2. The expected result is gate exit 0, which meets the FW-B0 exit criterion. Proposed: run 5 cites run 4 for steps 11 and 12 when its UF2 files are byte-identical to the run 3 files; if they differ, the owner steps run again.
5. Owner of `tools/tests/fixtures/picotool/known-answers.json`: change its `verify.status` from "blocked" to the run 4 result, and add the `verify` known answer (exit 0 for the true ELF; "First mismatch at 0x1000002f", exit 245 for the one-byte change at file offset `0x1002f`) (cross item).

Deferrals FD-1 and FD-2 of run 1 stand unchanged.

## 10. As-run procedure

Steps 11 and 12 as written in `docs/test_cases/sw-tool/test_cases.json` (blob `fee1e724`, unchanged), with deviations D16 to D19 of section 2. OA-2 as package section 2.2 row OA-2 and the lock section 1.1 picotool row, with deviation D18. Claude ran every command. The owner handled the board and counted the LED cycles.

## 11. Answers to INSP-016 findings (author response for the reviewer's next iteration)

The reviewer, not the author, changes the record (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`).

| Finding | Severity | Author response | What closes it |
|---|---|---|---|
| finding-1 (F-01) | Major | The owner part is done: OA-1 (steps 11 and 12) and OA-2 pass (this run). B8 is fixed (F-14). The owner has ruled B1, B2, B9 and B10 (close-out decisions 1, 2 and 4). Their application and run 5 remain | CR-004, the approved download, the convention CR, then run 5 with gate exit 0 |
| finding-14 (F-14) | Minor (lien) | `tools/sw_gate.sh:316` now passes one `--paths` per path (blob `52b9f803`). The known-answer check shows the step reaches `tools/complexity_gate.py` on all three roots. It reproduces the old error with the old form, and it catches a seeded CC 17 function under each root (`complexity-invocation-check.txt`) | reviewer verification of the change and the check; gate integration in run 5 |

## 12. Authentication and authorization

- Results authenticated by (conductor): claude, 2026-09-26
- Witnessed by: owner, 2026-09-26 19:17 to 19:23 CDT (steps 11 and 12 performed by the owner's hands and counted by the owner; statements transcribed verbatim in `docs/reviews/SRR/minutes.md`, "OA-1 and OA-2 performed")
- Authorization of acceptability (owner): accepted 2026-09-27. Owner statement, verbatim: "yes I approve the results" (`docs/reviews/SRR/minutes.md`, "Run 4 acceptance and repository protection detail"). Transcribed by Claude (lead SE).
