# LTspice 26.0.2 headless batch simulation on macOS: hands-on proof

**Assignment key:** ltspice. **Date:** 2026-09-25. **Author:** Claude (research subagent). **Status:** draft for owner review.
**Machine:** Apple M4 Pro (arm64), Darwin 25.6.0, Rosetta 2 present (`arch -x86_64 true` succeeds). LTspice.app 26.0.2.1 at `/Applications/LTspice.app`. Project venv Python 3.13.5.
**Cross-reference:** `docs/research/verification-tooling-inventory.md` F12 identified the CrossOver wrapper but did not confirm batch mode. This report confirms it and gives the working command lines.

## Question

Does LTspice 26.0.2 at `/Applications/LTspice.app` run in batch mode on macOS? Build a trivial RC low-pass netlist (`.net` with `.ac` and `.tran`) and a matching `.asc`, try `/Applications/LTspice.app/Contents/MacOS/LTspice -b file.net` and the `-Run` and `-ascii` variants, check for `.raw` and `.log` outputs, parse the `.raw` in Python (`ltspice` or `PyLTSpice` installed into `.venv`) and print the -3 dB frequency versus the analytic value. Record how to write `.asc` schematics programmatically, whether encrypted or vendor models load, and Homebrew availability of ngspice as a fallback. Deliver the exact working command lines and a minimal Python checker skeleton.

## Method

1. Read charter sections 1, 9, 11 (`docs/process/00-charter.md`): Analysis evidence class includes LTspice and Python checks; every visual product is rendered and inspected; evidence, not assertion.
2. Inspected the app bundle (`file`, `plutil -p Info.plist`, `find` for `.exe`, `drive_c`, `cxbottle.conf`), the CrossOver scripts (`bin/run_ltspice`, `bin/wine --help`) and the user bottle created on first launch under `~/Library/Application Support/LTspice/Bottles/ltspice`.
3. Authored decks in `/private/tmp/cwht-ltspice/` (RC low-pass R = 1 kOhm, C = 159.155 nF, so fc = 1/(2 pi R C) = 1000.000 Hz and tau = R C = 159.155 us): `rc_lowpass.net` (both analyses, deliberately), `rc_ac.net`, `rc_tran.net`, a hand-written `rc_lowpass.asc`, and `opamp_models.net` (encrypted `AD8065.sub` and plain-text `LTC.lib`).
4. Ran the official launcher, the bundled `run_ltspice` script and the bottle's `wine` directly, with POSIX and `Z:\` paths, with CrossOver tracing (`CX_LOG`, `CX_DEBUGMSG=+process,+file,+dialog,+win`) to find why runs produced nothing; extracted the UTF-16 string table of `LTspice.exe` with Python to identify the blocking dialog and the `LTspice.ini` key that suppresses it.
5. Tested switches `-b`, `-ascii -b`, `-netlist`, `-Run -b`, `-b` on `.asc`, `-version`, `-ini`, two concurrent runs, and a timeout-kill path.
6. `pip install ltspice PyLTSpice` into `/Users/robinonsay/rust/cwht/.venv` (authorized by the assignment); parsed the binary and ASCII `.raw` files with both packages; compared to analytic values.
7. Read the bundled help (`LTspiceHelp/commandlineswitches.htm`, `internetoptions.htm`, `runningunderlinux.htm`) and `LTspiceChangeLog.txt`; `brew info ngspice`, `brew info libngspice`, `brew info --cask ltspice` (no installs); fetched `ltspice.analog.com/download/updates.txt` and the Homebrew cask source; EngineerZone pages timed out three times and are cited from search results only.

Writes outside the allowed locations: one settings file inside the LTspice CrossOver bottle, `~/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini`, now contains `CaptureAnalytics=false` (the privacy-preserving answer to the first-run telemetry prompt, see F4). The original two-line file is kept beside it as `LTspice.ini.orig`; LTspice itself also left two timestamped copies (`LTspice_20260925_160323.ini`, `LTspice_20260925_161420.ini`) in the same folder while rewriting the file during the `-ini` experiments. Nothing else outside `docs/research/` and `/private/tmp/cwht-ltspice/` was modified.

## Findings

### F1. LTspice 26.0.2 for macOS is the Windows binary inside a CodeWeavers CrossOver (Wine) bundle, running x86-64 under Rosetta 2

- `file /Applications/LTspice.app/Contents/MacOS/LTspice` -> `Mach-O 64-bit executable x86_64` (on an arm64 M4 Pro, so Rosetta 2 is required).
- `Info.plist`: `CFBundleShortVersionString = 26.0.2.1`, `CFBundleIconFile = CrossOverOEM`, `NSPrincipalClass = CXApplication`, copyright Analog Devices 2025.
- The Windows program: `/Applications/LTspice.app/Contents/SharedSupport/ltspice/support/ltspice/drive_c/Program Files/ADI/LTspice/LTspice.exe` -> `PE32+ executable (GUI) x86-64, for MS Windows`, 68,247,664 bytes, dated May 4 (2026).
- Wine tooling: `SharedSupport/ltspice/bin/{wine,wineloader,wineserver,run_ltspice,cxstart,...}`; template bottle `SharedSupport/ltspice/support/ltspice` (`cxbottle.conf`: `WineArch = win64`, `Template = win10_64`, CrossOver `Version = 25.0.1.38665`).
- First launch (25 s) creates the user bottle `~/Library/Application Support/LTspice/Bottles/ltspice/` (symlinks into `BuiltinBottles/default`), with drives `c:` (bottle), `y:` -> `/Users/robinonsay`, `z:` -> `/`, plus `~/Library/Preferences/com.analog.ltspice.plist` (`FirstRunDate`). Component libraries live at `.../Bottles/ltspice/drive_c/users/crossover/AppData/Local/LTspice/lib/{cmp,sub,sym}` (3,084 files in `sub`) and examples beside them.
- The bundled `LTspice.json` still names `LTspice_Mac 17.2.4` (the old native macOS build) and the changelog entry for 26.0.0 (12/1/2025) says "Parallel release on MacOS and Windows" and "Add support for ARM processors" (the ARM support is the Windows build; the macOS wrapper is x86-64 only, see F13).

### F2. The documented launcher form `LTspice -b file.net` does not work in 26.0.2: the wrapper cannot resolve `LTspice.exe` and silently exits 0

Command and result (after the bottle existed):

```
$ cd /private/tmp/cwht-ltspice && /Applications/LTspice.app/Contents/MacOS/LTspice -b rc_lowpass.net ; echo exit=$?
exit=0            # 6 s, no .raw, no .log
```

CrossOver trace (`CX_LOG`) shows the launcher forwards the arguments to `bin/run_ltspice`, whose last line is
`wine --enable-alt-loader=macdrv --wait-children --bottle=default --workdir 'C:/Program Files/ADI/LTspice' LTspice.exe ${LT_APP_ARGS:-"$@"}`,
and Wine then fails:

```
0024:trace:process:CreateProcessInternalW app (null) cmdline L"LTspice.exe -b Z:\\private\\tmp\\cwht-ltspice\\rc_lowpass.net"
0024:trace:process:find_exe_file looking for L"LTspice.exe" in L"Z:\\Applications\\LTspice.app\\...\\lib\\wine\\x86_64-windows;C:\\windows\\system32;..."
winewrapper.exe:error: cannot execute L"LTspice.exe -b Z:\\private\\tmp\\cwht-ltspice\\rc_lowpass.net"
```

`run_ltspice` (direct) and `LT_APP_ARGS="-b ..." run_ltspice` fail the same way with exit 1; the GUI launcher masks it with exit 0 and prints only `The primary OEM task just exited. Time to close down.` The relative `LTspice.exe` is never searched in the `--workdir`. The GUI launch path (no arguments) is not affected by this (not tested here, but the same script is used; an owner GUI launch is a cheap confirmation).

### F3. Working invocation: call the bottle's `wine` with the full Windows path of `LTspice.exe`

```
$ /Applications/LTspice.app/Contents/SharedSupport/ltspice/bin/wine --bottle=ltspice --wait-children \
    'C:\Program Files\ADI\LTspice\LTspice.exe' -b /private/tmp/cwht-ltspice/rc_ac.net
$ ls
rc_ac.log  rc_ac.net  rc_ac.op.raw  rc_ac.raw          # 2 to 4 s wall time, 0.069 s simulation
```

POSIX paths are converted to `Z:\...` by the CrossOver `wine` Perl script (`--no-convert` disables that); `'Z:\private\tmp\...\rc_ac.net'` works identically. Outputs land beside the deck. `rc_ac.log`:

```
LTspice 26.0.2 for MacOS
Circuit: /private/tmp/cwht-ltspice/rc_ac.net
Start Time: Fri Sep 25 11:01:07 2026
solver = Normal
Maximum thread count: 14
tnom = 27
temp = 27
method = trap
.OP point found by inspection.
Total elapsed time: 0.069 seconds.
```

`wine` returns LTspice's exit status (0 on success, 1 on the F6 deck error). Stderr carries about 130 lines of MoltenVK chatter (`[mvk-info] ...`, `VK_KHR_...`) that the wrapper below filters. A `wineserver` process lingers for a few seconds after each run; that is normal.

### F4. First-run blocker: the "Anonymously Share LTspice Usage Data" consent dialog is shown even in `-b` mode and blocks forever; `CaptureAnalytics=false` in the bottle's `LTspice.ini` suppresses it

Symptom: with the F3 command the process sat at 0 % CPU indefinitely (killed after 5 min), no outputs; only `drive_c/users/crossover/AppData/Roaming/LTspice.ini` was written (`[Options]` / `UUID=<20 digits>`). `CX_DEBUGMSG=+dialog,+win` showed a 291 x 120 DLU dialog with controls `Msg`, `Msg2`, `Option 1`, `Option 2`, `OK`. The UTF-16 string table of `LTspice.exe` (extracted with Python) contains, contiguously at 0x2920ba2: `Anonymously Share LTspice Usage Data`, `Yes, send my anonymous usage data to the LTspice team`, `No, do not send my usage data`, `This can be changed at any time in LTspice Settings`, `Internet`; and the telemetry endpoint `https://api.telemetry.analogtools.io/v1/logs` (0x2917e4a) with JSON keys `appId`, `event`, `LTspiceVersion`, `UUID`, `session`. The `[Options]` key table (0x291ed60 to 0x291fb30) contains `CaptureAnalytics` immediately before `UUID`. The bundled help `internetoptions.htm` documents the setting as "Send my anonymous usage data to the LTspice team" and `LTspiceChangeLog.txt` lists "Optionally share anonymous usage analytics" under the 24.0 release notes.

Fix (verified; both `false` and `0` work):

```
$ cat "$HOME/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini"
[Options]
UUID=17053081613026259276
CaptureAnalytics=false
```

With this file in place the F3 command completed in 4 s. Removing the key (restoring the UUID-only file) reproduced the hang within 15 s on every attempt. This edit is the same as answering "No" once in the GUI (Settings > Internet). LTspice leaves the file unchanged on later runs.

### F5. `-ini <file>` cannot be used to carry the consent in a project file (26.0.2)

All five variants prompted the dialog and were killed on timeout: project ini without the key; with `UUID=1` + `CaptureAnalytics=false`; with the real UUID + key; both the bottle ini and the project ini seeded; project ini given as a `Z:\` path. LTspice did use the `-ini` file (it appended a fresh `UUID=` to it when absent), so the switch works for settings but the first-run analytics check is not satisfied through it. Root cause unknown (possibly a first-run flag keyed to something outside `[Options]`). Practical rule: the consent must be in the default `%APPDATA%\LTspice.ini` of the bottle.

### F6. One analysis per deck; the log names the error and the exit code is 1

`rc_lowpass.net` with both `.ac` and `.tran` produced only `rc_lowpass.log`:

```
LTspice 26.0.2 for MacOS
Circuit: /private/tmp/cwht-ltspice/rc_lowpass.net
Start Time: Fri Sep 25 10:59:09 2026
More than one analysis specified.
```

Also note LTspice source syntax: `V1 in 0 PULSE(0 1 0 1n 1n 5m 10m) AC 1` (transient function first, `AC` after) is what LTspice itself emits from the schematic; `V1 in 0 AC 1` alone is fine for an AC-only deck.

### F7. Switches verified on this build

| Switch | Command | Result |
|---|---|---|
| `-b deck.net` | F3 | binary `deck.raw` 39,286 B, `deck.op.raw`, `deck.log` |
| `-ascii -b deck.net` | same with `-ascii` first | text `.raw` 113,784 B, header `Title: ... Flags: complex forward log`, parses with both Python packages |
| `-netlist sch.asc` | `... LTspice.exe -netlist /path/rc_lowpass.asc` | writes `rc_lowpass.net` ("* Generated by LTspice 26.0.2 for MacOS.") |
| `-Run -b sch.asc` | | netlists and simulates, `rc_lowpass.raw` written |
| `-b sch.asc` | | same as above (`-Run` not needed with `-b`) |
| `-version` | | prints `26.0.2` to stdout, exit 0 |
| `-ini file` | | honoured for settings, does not clear the F4 prompt |
| two runs concurrently | two wrapper invocations in background | both exit 0, 4 s total, results identical to serial runs |
| hung process | `pkill -f 'LTspice\\LTspice.exe'` | wine exits 143, prints `wineserver crashed, please enable coredumps`; the next run works normally |

The bundled `commandlineswitches.htm` lists: `-alt -ascii -b -big -encrypt -FastAccess -FixUpSchematicFonts -FixUpSymbolFonts -ini <path> -I<path> -max -netlist -norm -PCBnetlist -Run -sync -version`, and says `-ini` overrides `%APPDATA%\LTspice.ini`. Changelog 24.0.3 (12/06/23): "Command line batch mode sync (-b -sync) writes to stdout instead of showing dialog"; 24.0.x: "Added -version command line option". `-encrypt`, `-sync`, `-alt`, `-I` were not exercised.

### F8. Python parsing: both `ltspice` 1.0.6 and `PyLTSpice` 6.0.1 (spicelib 1.6.3) parse the 26.0.2 `.raw`; the -3 dB point matches the analytic 1000.000 Hz

```
$ .venv/bin/python -m pip install ltspice PyLTSpice     # installs numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2, spicelib 1.6.3
$ .venv/bin/python check_rc.py rc_ac.raw rc_tran.raw
analytic fc = 1000.000 Hz, tau = 159.155 us
[ltspice   ] f(-3dB) = 1000.000 Hz  (401 pts)  err = +0.000 %
[spicelib  ] f(-3dB) = 1000.000 Hz  (401 pts)  err = +0.000 %  traces=['frequency', 'V(in)', 'V(out)', 'I(C1)', 'I(R1)', 'I(V1)']
[spicelib  ] tau(63.2%) = 159.155 us  err = +0.000 %
PASS
```

The `.raw` header is UTF-16LE text (`T\0i\0t\0l\0e\0:` ...) followed by binary doubles (LTspice XVII and later format); with `-ascii` it is plain text. Both packages handle both. `ltspice` exposes `get_frequency()` and `get_data('V(out)')`; spicelib exposes `RawRead(path).get_trace('V(out)').get_wave()` and `get_trace_names()`. spicelib's own `LTspice` simulator class does not know the 26.x CrossOver layout: on macOS it looks for `~/.wine/drive_c/...` or the old native `/Applications/LTspice.app/Contents/MacOS/LTspice` (`spicelib/simulators/ltspice_simulator.py` lines 36 to 121), so drive the simulator with the project's own wrapper and use spicelib for parsing only (or `LTspice.create_from('<wrapper>')`, untested).

### F9. Authoring `.asc` schematics programmatically works; validate every generated file with `-netlist` and reject `NC_` nets

Format (verified by reading shipped examples and by LTspice accepting my hand-written file): plain text, ASCII, either CRLF (Windows examples, my file) or LF (files written by the old native Mac build) line endings; header `Version 4` then `SHEET 1 880 680`; `WIRE x1 y1 x2 y2`; `FLAG x y <net>` (`0` is ground); `SYMBOL <lib\name> x y R0|R90|R180|R270|M0|M90...`; optional `WINDOW` lines; `SYMATTR InstName R1`, `SYMATTR Value 1k`, `SYMATTR Value2 AC 1` (second value field of sources), `SYMATTR SpiceLine`, `SYMATTR SpiceModel`; `TEXT x y Left 2 !.ac dec 100 10 100k` (leading `!` = directive, `;` = comment). Grid pitch is 16 units and pins must be hit exactly. Pin offsets from `lib/sym/*.asy` (unrotated): `res` and `ind` (16,16) and (16,96); `cap` (16,0) and (16,64); `voltage` (0,16) and (0,96); `current` (0,0) and (0,80); op-amp symbols in `sym/OpAmps` carry `PINATTR SpiceOrder` (In+ In- V+ V- OUT) and `SYMATTR SpiceModel <file>`.

My first draft ended the capacitor's ground wire 16 units short; `-netlist` exposed it immediately:

```
C1 out NC_01 159.155n          # dangling pin becomes an NC_nn net
```

After changing `WIRE 272 240 272 208` to `WIRE 272 240 272 192` the generated netlist reads `C1 out 0 159.155n`, and `-b rc_lowpass.asc` gives f(-3dB) = 1000.000 Hz. So the check `grep -q ' NC_' generated.net && fail` is a cheap, decisive inspection step for any generated schematic. The final `rc_lowpass.asc` (650 bytes) is in `/private/tmp/cwht-ltspice/`.

### F10. Encrypted and plain-text ADI models load by bare `.lib` filename from the built-in library

`opamp_models.net` (unity-gain buffers on +/-5 V, `.lib AD8065.sub`, `.lib LTC.lib`, `.ac dec 20 10 100Meg`) ran in 3 s with `Direct Newton iteration succeeded`; the log's `Files loaded:` lists both `.../AppData/Local/LTspice/lib/sub/AD8065.sub` and `.../lib/sub/LTC.lib`. `file AD8065.sub` reports `data` (LTspice-encrypted; hundreds of ADI `.sub` files are, e.g. the AD35xx/AD40xx families), while `LTC.lib` is ISO-8859 text with 179 `.subckt`s (LT1001 is `.subckt LT1001 1 2 3 4 5`). Parsed results: AD8065 buffer 0.000 dB at 1 kHz and flat to 100 MHz on this sweep; LT1001 buffer -3 dB near 1.41 MHz. Vendor models placed outside the library must be referenced by absolute path or through `-I<path>` (not tested).

### F11. ngspice is available from Homebrew as a fallback (not installed)

```
$ brew info ngspice
==> ngspice: stable 47 (bottled), HEAD ... Not installed
Required (11): fftw, freetype, libngspice, libx11, libxaw, libxt, readline, libice, libsm, libxext, libxmu
Caveats: If you need the graphical plotting functions you need to install X11 with: brew install --cask xquartz
$ brew info libngspice
==> libngspice: stable 47 (bottled) ... Spice circuit simulator as shared library ... Not installed
$ brew info --cask ltspice
==> ltspice (LTspice): 26.0.2 ... Not installed   (cask source: url "https://ltspice.analog.com/software/LTspice_#{version.major}.pkg", sha256 :no_check, depends_on macos: :sonoma, livecheck skipped "Blocked by upstream bot protection")
```

ngspice would run arm64-native and needs no Wine, but cannot read LTspice-encrypted vendor models (F10) and lacks LTspice's `A`-device behavioral primitives used inside `LTC.lib` (`A1 ... OTA g=150u ...`).

### F12. Version state (2026-09-25)

`https://ltspice.analog.com/download/updates.txt`: `LTspice 26.1.1`, `ProductVersion = 26.1.1.0`, `ReleaseDate = 23/09/2026`, Windows `LTspice64.msi`; changelog dates 26.1.1 9/20/26, 26.1.0 8/3/26, 26.0.2 5/6/26. The macOS package (cask and this machine) is still 26.0.2, so the Mac build lags the Windows build by two releases. Every `.log` starts with the version string (`LTspice 26.0.2 for MacOS`), which is the right thing to record in analysis reports.

### F13. Platform notes from the web (not fetched directly, EngineerZone timed out)

- EngineerZone Q&A title: "LTspice v17.2.4 for macOS is 'Apple Silicon default', while LTspice v26 is Intel x86-64 only. WHY?" (search result summary: v26 requires Rosetta 2 on Apple silicon). Consistent with F1.
- AppleInsider (2026-07-31) and TUAW (2026-08-02): CodeWeavers is testing an Apple-silicon-native CrossOver; CrossOver 27 (native, Intel dropped) planned for early 2027. Whether ADI will rebase the LTspice bundle on it is unknown.
- spicelib docs ("Installing LTspice"): "It is recommended to use wine to run the windows version of LTspice on MacOS" and the library "will try to use the wine version if it is installed, even if the MacOS native version is installed."

## Deliverable: exact working command lines

Precondition (once per machine, or click "No" once in the GUI):

```
INI="$HOME/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini"
# create the bottle if it does not exist yet: open /Applications/LTspice.app once and quit, or run the wrapper once
iconv -f UTF-16LE -t UTF-8 "$INI" | /usr/bin/grep -q '^CaptureAnalytics=false' || { echo 'CaptureAnalytics not set: click No once in the GUI consent dialog, then re-check; never append to the UTF-16LE ini'; exit 1; }
```

**Correction 2026-09-26 (integrator; tools/toolchain.lock.md section 1.4 items 1 and 2).** The earlier form of this precondition, `grep -q CaptureAnalytics "$INI" || printf 'CaptureAnalytics=false\r\n' >> "$INI"`, is withdrawn: the ini is UTF-16LE, so `/usr/bin/grep` never matches it (it matched in the agent zsh only because `grep` there is a shell function), and the append would write an ASCII line into the UTF-16 file and corrupt it. The check above reads the file through `iconv` and never writes it. Also recorded there: `-b` on an `.asc` schematic that carries a deck error hangs with no log, while the same error in a `.net` netlist exits 1 with the error in the log; decks for the record are netlists, and a time-out guard kills only the run's own processes.

Wrapper `tools/ltspice-batch.sh` (tested as `/private/tmp/cwht-ltspice/ltspice-batch.sh`):

```bash
#!/bin/bash
# Run the Windows LTspice.exe shipped inside LTspice.app (26.x CrossOver bottle). POSIX or Z:\ paths accepted.
# usage: ltspice-batch.sh [-ascii] -b deck.net | -netlist sch.asc | -b sch.asc | -version
S=/Applications/LTspice.app/Contents/SharedSupport/ltspice
exec "$S/bin/wine" --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' "$@" \
  2> >(grep -v -E 'mvk-info|^\s+(VK_|GPU|macOS GPU|Metal|model:|type:|vendorID|deviceID|pipelineCache|supports|The following)' >&2)
```

```
tools/ltspice-batch.sh -b sim/rc_ac.net              # -> sim/rc_ac.raw sim/rc_ac.op.raw sim/rc_ac.log
tools/ltspice-batch.sh -ascii -b sim/rc_ac.net       # ASCII raw
tools/ltspice-batch.sh -netlist sim/rc_lowpass.asc   # -> sim/rc_lowpass.net (then: grep -q ' NC_' && fail)
tools/ltspice-batch.sh -b sim/rc_lowpass.asc         # netlist + simulate a schematic
tools/ltspice-batch.sh -version                      # 26.0.2
timeout 120 tools/ltspice-batch.sh -b deck.net || pkill -f 'LTspice\\LTspice.exe'   # guard against modal dialogs
```

## Deliverable: minimal Python checker skeleton (tested)

`/private/tmp/cwht-ltspice/ltspice_check.py`, run as `.venv/bin/python ltspice_check.py rc_ac.net` -> `LTspice 26.0.2 for MacOS | f(-3dB) = 1000.000 Hz | analytic 1000.000 Hz | err +0.000 %`, exit 0; on the two-analysis deck it prints `SIM FAIL: LTspice rc=1 ... More than one analysis specified.` and exits 2.

```python
#!/usr/bin/env python3
"""Run an LTspice deck headless (LTspice 26.x CrossOver bundle on macOS), parse the .raw with spicelib,
assert a measured quantity against an analytic value. Exit 0 pass, 1 check failed, 2 simulation failed."""
import math, subprocess, sys, time
from pathlib import Path
import numpy as np
from spicelib import RawRead            # pip install PyLTSpice

WINE = "/Applications/LTspice.app/Contents/SharedSupport/ltspice/bin/wine"
LTSPICE_EXE = r"C:\Program Files\ADI\LTspice\LTspice.exe"
NOISE = ("mvk-info", "VK_", "GPU", "Metal", "model:", "type:", "vendorID", "deviceID", "pipelineCache", "supports", "The following")

def run_ltspice(deck: Path, timeout_s: float = 120, extra=()) -> tuple[Path, Path]:
    cmd = [WINE, "--bottle=ltspice", "--wait-children", LTSPICE_EXE, *extra, "-b", str(deck.resolve())]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
    except subprocess.TimeoutExpired:
        subprocess.run(["pkill", "-f", r"LTspice\\LTspice.exe"])
        raise RuntimeError(f"LTspice timed out after {timeout_s}s (modal dialog?): {deck}")
    err = "\n".join(l for l in p.stderr.splitlines() if not any(n in l for n in NOISE))
    raw, log = deck.with_suffix(".raw"), deck.with_suffix(".log")
    if p.returncode != 0 or not raw.exists():
        raise RuntimeError(f"LTspice rc={p.returncode} in {time.time()-t0:.1f}s\n{err}\n"
                           f"{log.read_text(errors='replace') if log.exists() else ''}")
    return raw, log

def f_minus3db(raw: Path, trace="V(out)") -> float:
    r = RawRead(str(raw))
    f = np.real(r.get_trace("frequency").get_wave())
    db = 20 * np.log10(np.abs(r.get_trace(trace).get_wave()))
    return float(np.interp(-3.0103, db[::-1], f[::-1]))      # monotonic low-pass response

if __name__ == "__main__":
    deck = Path(sys.argv[1]); R, C = 1e3, 159.155e-9; fc = 1 / (2 * math.pi * R * C)
    try:
        raw, log = run_ltspice(deck)
    except RuntimeError as e:
        print("SIM FAIL:", e); sys.exit(2)
    ver = next((l for l in log.read_text(errors="replace").splitlines() if l.startswith("LTspice")), "?")
    f3 = f_minus3db(raw); err = (f3 - fc) / fc
    print(f"{ver} | f(-3dB) = {f3:.3f} Hz | analytic {fc:.3f} Hz | err {100*err:+.3f} %")
    sys.exit(0 if abs(err) < 0.01 else 1)
```

Test decks (in `/private/tmp/cwht-ltspice/`): `rc_ac.net` = `V1 in 0 AC 1 / R1 in out 1k / C1 out 0 159.155n / .ac dec 100 10 100k / .end`; `rc_tran.net` = `V1 in 0 PULSE(0 1 0 1n 1n 5m 10m) / R1 in out 1k / C1 out 0 159.155n / .tran 0 2m 0 1u / .end`; `rc_lowpass.asc` as described in F9; `opamp_models.net` as in F10; `check_rc.py` (parser comparison, both packages).

## Implications for cwht

- REQ-candidate (SEMP / V&V plan, Analysis evidence class): "Every LTspice analysis cited as verification evidence shall be reproducible headless by `tools/ltspice-batch.sh` from a committed deck, and its report shall record the `LTspice <version> for MacOS` line of the `.log`, the deck hash and the checker output." Basis: F3, F8, F12.
- REQ-candidate (tools): "Analysis decks shall contain exactly one analysis directive; multi-analysis studies are split into one deck per analysis (or use `.step`)." Basis: F6.
- REQ-candidate (tools): "Generated `.asc` files shall be netlisted with `-netlist` and rejected if the netlist contains any `NC_` net." Basis: F9.
- REQ-candidate (tools): "Batch runs shall be wrapped in a timeout that kills `LTspice.exe` and reports failure, so a modal dialog can never stall a verification run." Basis: F4, F7.
- RISK-candidate: toolchain fragility. The macOS build is a Rosetta-dependent CrossOver bundle whose launcher argument path is broken in 26.0.2 (F2); the working path depends on internal bundle layout (`SharedSupport/ltspice/bin/wine`, bottle name `ltspice`, exe path) that ADI or CodeWeavers may change (F13). Mitigation: pin `LTspice.app 26.0.2.1` and the `LTspice.exe` SHA-256 in the toolchain record; run the RC smoke test (`ltspice_check.py`) at every TRR-style checkpoint and after any LTspice or macOS update.
- RISK-candidate: hidden modal prompts. Besides the telemetry prompt (F4), the string table contains an update nag ("The last time your installation was updated was %d days ago. Do you want to update now?"), keyboard-shortcut migration prompts and first-use library unpack steps; any of them would hang a batch run. Mitigation: the timeout wrapper, the seeded ini, and a documented list of ini keys as they are discovered (`CaptureAnalytics`, possibly `LastWebUpdateTime`).
- RISK-candidate: version lag (macOS 26.0.2 vs Windows 26.1.1) means convergence or model fixes in newer releases are unavailable on the analysis machine; results are still self-consistent because the version is logged (F12).
- RISK-candidate (privacy/process): telemetry is opt-in and now declined on this machine by a settings edit made by an agent (F4). Owner to confirm the choice; it can be changed in Settings > Internet.
- DECISION-needed: adopt LTspice 26.0.2 (CrossOver) as the primary Analysis simulator, with ngspice 47 (Homebrew) only as a vendor-model-free fallback. Recommendation: LTspice primary, because ADI encrypted models and `A`-device macromodels only run there (F10, F11); revisit if the PA and RF stages use only plain-text third-party models.
- DECISION-needed: whether the project drives LTspice through spicelib's `SimRunner` (needs `LTspice.create_from(wrapper)`, untested) or through the small subprocess helper above (tested). Recommendation: the tested helper; spicelib for `RawRead` only (F8).
- ACTION: add `tools/ltspice-batch.sh`, `tools/ltspice_check.py` (generalised: deck, trace, measurement, expected, tolerance from a JSON test-case record) and the RC smoke decks to the repo; add `PyLTSpice==6.0.1`, `spicelib==1.6.3`, `ltspice==1.0.6` to `tools/requirements.txt` (coordinate with `verification-tooling-inventory.md`).
- ACTION: record the bottle precondition (`CaptureAnalytics=false`) and the broken-launcher workaround in the toolchain proof for SRR; consider reporting the `run_ltspice`/`--workdir` defect to ADI EngineerZone.
- ACTION: when authoring review-package schematics, generate `.asc` from the same Python model that emits the netlist, then render through LTspice only if a rendered image is needed (LTspice has no headless image export; KiCad remains the schematic-rendering tool per the tooling inventory).

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 CrossOver/x86-64 wrapper, bottle layout | High | direct inspection, file and plist output |
| F2 launcher `-b` broken, silent exit 0 | High | reproduced 4 times, Wine trace shows the failing exec |
| F3 working wine invocation, outputs, timing | High | dozens of runs, outputs parsed |
| F4 telemetry dialog blocks batch; `CaptureAnalytics=false` fixes it | High | dialog template trace, exe string table, key toggled on/off 6 times with consistent behaviour |
| F5 `-ini` cannot carry the consent | High that it fails in 26.0.2; Low on the reason | 5 variants, all hung |
| F6 one analysis per deck | High | log text |
| F7 switch matrix | High for rows tested; `-encrypt`, `-sync`, `-alt`, `-I` untested | |
| F8 parsers and -3 dB result | High | two independent parsers agree to the printed precision |
| F9 `.asc` format and NC_ check | High for the constructs used; Medium for non-ASCII text and other symbols | one hand-written file, one shipped example set |
| F10 encrypted and plain models load | High | log "Files loaded", plausible gains |
| F11 ngspice availability | High | brew output |
| F12 versions | High | updates.txt fetched, changelog read |
| F13 platform notes | Medium | search summaries only, pages timed out |

## Open items

1. Why `-ini` does not satisfy the analytics first-run check (F5); retest on the next macOS release (26.1.x) and, if fixed, move the consent into a project-controlled ini.
2. Key(s) that suppress the periodic update prompt in batch mode (`LastWebUpdateTime`, `LastWebUpdateQuery` are candidates from the key table); not exercised because the installation is new.
3. Owner confirmation of the `CaptureAnalytics=false` setting written into the bottle (backup `LTspice.ini.orig`).
4. Confirm the GUI launch (no arguments) works on this machine and report the `run_ltspice` `--workdir` defect to ADI.
5. spicelib `SimRunner` with `LTspice.create_from(wrapper)` not tested end to end; `-I<path>` for project-local model directories not tested; `-encrypt` not tested.
6. `.asc` handling of non-ASCII characters (micro sign, Omega) and of hierarchical sheets not tested.
7. Dependence on Rosetta 2 and on CodeWeavers' CrossOver 27 (native Apple silicon, early 2027) roadmap; whether ADI will ship an arm64 bundle.
8. Bottle hygiene after forced kills: "wineserver crashed" was harmless here, but a corrupted bottle would need `rm -rf ~/Library/Application Support/LTspice/Bottles/ltspice` and a re-run (the bottle is rebuilt from the app's template in about 25 s); verify that recovery path once.

## Sources

- Bundled help: `LTspiceHelp/commandlineswitches.htm`, `internetoptions.htm`, `runningunderlinux.htm` (inside `LTspice.app`, copyright 1998-2026 Analog Devices).
- Bundled `LTspiceChangeLog.txt` (26.0.2 dated 4/29/26; 24.0.3 dated 12/06/23).
- https://ltspice.analog.com/download/updates.txt (fetched 2026-09-25: LTspice 26.1.1, ReleaseDate 23/09/2026).
- https://raw.githubusercontent.com/Homebrew/homebrew-cask/HEAD/Casks/l/ltspice.rb (version 26.0.2, `depends_on macos: :sonoma`).
- https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/n/ngspice.rb via `brew info ngspice` (stable 47).
- https://spicelib.readthedocs.io/en/latest/varia/LTSpice.html (macOS: prefer the Windows build under wine).
- https://ez.analog.com/design-tools-and-calculators/ltspice/f/q-a/606235/ltspice-v17-2-4-for-macos-is-apple-silicon-default-while-ltspice-v26-is-intel-x86-64-only-why/605458 (title and search summary only).
- https://ez.analog.com/design-tools-and-calculators/ltspice/f/q-a/588074/send-my-anonymous-usage-data-to-the-ltspice-team (search summary only).
- https://ez.analog.com/design-tools-and-calculators/ltspice/f/q-a/574563/macos-version-ignores--i-and--alt-command-line-options (old native macOS build; search summary only).
- https://appleinsider.com/articles/26/07/31/first-apple-silicon-native-crossover-build-in-testing-as-rosettas-end-nears and https://www.tuaw.com/2026/08/02/crossover-goes-native-on-apple-silicon/ (CrossOver 27 roadmap; search summaries).
- https://pypi.org/project/spicelib (spicelib 1.6.3), PyPI `PyLTSpice` 6.0.1, PyPI `ltspice` 1.0.6 (versions as installed by pip on 2026-09-25).
- Local evidence files: `/private/tmp/cwht-ltspice/` (decks, `.raw`, `.log`, `cx.log`, `cx2.log`, `cx3.log` traces, `ltspice-batch.sh`, `ltrun.sh`, `check_rc.py`, `ltspice_check.py`, `rc_lowpass.asc`).
