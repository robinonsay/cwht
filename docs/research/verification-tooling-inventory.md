# Verification tooling inventory and proposed tools environment

**Assignment key:** tooling. **Date:** 2026-09-25. **Author:** Claude (research subagent). **Status:** draft for owner review.
**Machine:** Apple Silicon Mac (arm64, Mac16,8, 14 CPU, 24 GB), macOS 26.6.2, Rosetta 2 active (oahd running).

## Question

Inventory and verify, read-only, the verification toolchain present on this Mac and propose the cwht project tools environment: KiCad 10.0.6 `kicad-cli` capabilities and exact flags, the bundled KiCad Python (`pcbnew` import), kiutils and kicad-skip for programmatic `.kicad_sch` generation, the OpenSCAD CLI, Python libraries for RF (scikit-rf), SPICE parsing (PyLTSpice/spicelib), plotting (matplotlib) and schema validation (jsonschema), and Rust coverage/complexity tooling (cargo-llvm-cov, cargo-geiger, rust-code-analysis) via crates.io. Deliver pinned `tools/requirements.txt` additions, a one-command setup script outline, and a tool table with a known-answer verification (accreditation) for each tool.

## Method

1. Read charter sections 1, 9, 11 (`docs/process/00-charter.md`): evidence classes Analysis / HostUnit / Emulation / Inspection; visual closure rule; Class A software commitments including MC/DC (SWE-219) and cyclomatic complexity <= 15 (SWE-220).
2. Ran version and help commands for every tool found under `/Applications`, `/opt/homebrew`, `~/.cargo`, and the project `.venv`. Note: `kicad-cli <leaf> --help` prints the top-level usage; `-h` on the leaf works. zsh does not word-split unquoted variables, so `for s in "pcb drc"; do kicad-cli $s` fails; leaf commands were re-run literally.
3. Built known-answer inputs in the session scratch directory (`/private/tmp/claude-501/.../scratchpad/ka`): a `pcbnew`-generated 100 x 50 mm board with one 10 mm track; a hand-built two-resistor schematic using the library `Device:R` symbol; a 10 mm OpenSCAD cube; a 10 k / 10 k SPICE divider netlist; a Rust file with known decision structure.
4. Ran `kicad-cli` ERC, DRC, netlist, BOM, SVG, PDF, Gerber, drill, position, STEP, stats and 3D render on those inputs and checked the results against expected values.
5. Created a throwaway venv in the scratch directory (not the project `.venv`, which the assignment did not authorize me to modify) and installed the proposed pins on Python 3.13.5 to accredit each library with a known answer.
6. Queried PyPI JSON (`pypi.org/pypi/<pkg>/json`) and the crates.io API (`crates.io/api/v1/crates/<crate>`) for versions, upload dates, `requires_python` and MSRV; queried Homebrew cask/formula metadata.
7. Fetched primary documentation: docs.kicad.org (kicad-cli 10.0), dev-docs.kicad.org (SWIG deprecation, IPC API), rustc unstable book and rust-lang/rust PR #144999 (MC/DC removal), cargo-llvm-cov README and CHANGELOG, clippy lint index, openscad.org downloads, ltwiki LTspice command-line switches, spicelib source, kiutils and kicad-skip repositories.

No files were written outside `docs/research/` and the scratch directory. No system packages were installed. The `cargo install` candidates were checked on crates.io only.

## Findings

### F1. KiCad 10.0.6 and kicad-cli are installed, arm64-native, with the full 10.0 command tree

Command: `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli version --format about`

Output (excerpt): `Application: kicad-cli arm64 on arm64 / Version: 10.0.6, release build / Build Info: Date: Aug 28 2026 / wxWidgets 3.2.8 / Boost 1.90.0 / OCC 7.9.3 / ngspice: 45.2 / KICAD_IPC_API=ON`. `file kicad-cli` reports a universal binary (x86_64 + arm64).

Top-level commands: `fp {export,upgrade}`, `jobset {run}`, `pcb {drc,export,import,render,upgrade}`, `sch {erc,export,upgrade}`, `sym {export,upgrade}`, `version`. The docs confirm the macOS path: "On macOS, the kicad-cli executable is located at /Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli" (https://docs.kicad.org/10.0/en/cli/cli.html). Homebrew cask `kicad` is also at 10.0.6.

Quirk: on 10.0.6 `kicad-cli sch erc --help` prints the top-level usage; `kicad-cli sch erc -h` prints the leaf usage. Scripts should use `-h` or run the command with no arguments to see usage.

### F2. Exact sch flags in 10.0.6 (verified from `-h` output)

- `sch erc [-o OUT] [-D KEY=VALUE]... [--format json|report] [--units in|mm|mils] [--severity-all|--severity-error|--severity-warning|--severity-exclusions] [--exit-code-violations] INPUT`
- `sch export svg [-o OUT_DIR] [--drawing-sheet PATH] [-D ...] [--variant NAME]... [-t THEME] [-b|--black-and-white] [-e|--exclude-drawing-sheet] [--default-font NAME] [--draw-hop-over] [-n|--no-background-color] [--pages LIST] INPUT`
- `sch export pdf [-o OUT_FILE] ... same as svg plus [--exclude-pdf-property-popups] [--exclude-pdf-hierarchical-links] [--exclude-pdf-metadata]`
- `sch export netlist [-o OUT] [--variant NAME]... [--format kicadsexpr|kicadxml|cadstar|orcadpcb2|spice|spicemodel|pads|allegro] INPUT` (default kicadsexpr)
- `sch export bom [-o OUT] [--variant]... [--preset P] [--format-preset F] [--fields LIST] [--labels LIST] [--group-by LIST] [--sort-field F] [--sort-asc true|false] [--filter S] [--exclude-dnp] [--field-delimiter] [--string-delimiter] [--ref-delimiter] [--ref-range-delimiter] [--keep-tabs] [--keep-line-breaks] INPUT` (default fields `Reference,Value,Footprint,QUANTITY,DNP`; `--include-excluded-from-bom` is deprecated, no effect)
- `sch export dxf|hpgl|ps|python-bom`, `sch upgrade` also present.

### F3. Exact pcb flags in 10.0.6 (verified from `-h` output)

- `pcb drc [-o OUT] [-D ...] [--format json|report] [--all-track-errors] [--schematic-parity] [--units] [--severity-*] [--exit-code-violations] [--refill-zones] [--save-board] INPUT`
- `pcb export gerbers [-o OUT_DIR] [-l|--layers LIST] [--cl|--common-layers LIST] [--drawing-sheet] [-D] [--erd|--exclude-refdes] [--ev|--exclude-value] [--ibt|--include-border-title] [--sp] [--hdnp] [--sdnp] [--cdnp] [--no-x2] [--no-netlist] [--subtract-soldermask] [--disable-aperture-macros] [--use-drill-file-origin] [--precision 5|6] [--no-protel-ext] [--check-zones] [--variant]... [--board-plot-params] INPUT`
- `pcb export drill [-o OUT_DIR] [--format excellon|gerber] [--drill-origin absolute|plot] [--excellon-zeros-format decimal|suppressleading|suppresstrailing|keep] [--excellon-oval-format route|alternate] [-u in|mm] [--excellon-mirror-y] [--excellon-min-header] [--excellon-separate-th] [--generate-map] [--generate-report] [--report-path] [--generate-tenting] [--map-format pdf|gerberx2|ps|dxf|svg] [--gerber-precision 5|6] INPUT`
- `pcb export pos [-o OUT] [--side front|back|both] [--format ascii|csv|gerber] [--units in|mm] [--bottom-negate-x] [--use-drill-file-origin] [--smd-only] [--exclude-fp-th] [--exclude-dnp] [--gerber-board-edge] [--variant]... INPUT` (default units are inches)
- `pcb export svg [-o OUT] [-l LIST] [--cl LIST] [--drawing-sheet] [-D] [--subtract-soldermask] [-m|--mirror] [-t THEME] [-n|--negative] [--black-and-white] [--sp/--hdnp/--sdnp/--cdnp] [--page-size-mode 0|1|2] [--fit-page-to-board] [--exclude-drawing-sheet] [--drill-shape-opt 0|1|2] [--mode-single|--mode-multi] [--scale S] [--check-zones] [--variant]... INPUT`. Running without a mode prints: "This command has deprecated behavior as of KiCad 9.0 ... The new behavior will match --mode-multi". Always pass a mode.
- `pcb export step [-o OUT] [-D] [-f|--force] [--no-unspecified] [--no-dnp] [--variant]... [--grid-origin] [--drill-origin] [--subst-models] [--board-only] [--cut-vias-in-body] [--no-board-body] [--no-components] [--component-filter] [--include-tracks] [--include-pads] [--include-zones] [--include-inner-copper] [--include-silkscreen] [--include-soldermask] [--fuse-shapes] [--fill-all-vias] [--no-extra-pad-thickness] [--min-distance] [--net-filter] [--no-optimize-step] [--user-origin] INPUT`
- `pcb export stats [-o OUT] [--format json|report] [--units in|mm] [--exclude-footprints-without-pads] [--subtract-holes-from-board] [--subtract-holes-from-copper] INPUT`
- `pcb export ipcd356 [-o OUT] INPUT`; other exporters present: `3dpdf brep dxf gencad glb ipc2581 odb pdf ply ps stl stpz u3d vrml xao` (`hpgl` reports "No longer supported as of KiCad 10.0").
- `pcb render [-o OUT.png|.jpg] [-D] [--variant]... [-w W] [-h H] [--side top|bottom|left|right|front|back] [--background default|transparent|opaque] [--quality basic|high|user|job_settings] [--preset NAME] [--use-board-stackup-colors] [--floor] [--perspective] [--zoom Z] [--pan X,Y,Z] [--pivot X,Y,Z] [--rotate X,Y,Z] [--light-top|--light-bottom|--light-side|--light-camera COLOR] [--light-side-elevation DEG] INPUT`
- `jobset run [--stop-on-error] [-f|--file JOBSET] [--output NAME] INPUT_PROJECT`; `fp export svg [-o] [-l] [-D] [-t] [--fp NAME] ... LIB_DIR`; `sym export svg [-o] [-t] [-s SYMBOL] [--black-and-white] [--include-hidden-pins] [--include-hidden-fields] LIB`.

### F4. kicad-cli PCB known-answer run: deterministic, machine-readable, exit codes usable as gates

Board generated by `pcbnew` (F8): 100 x 50 mm Edge.Cuts rectangle, one 0.25 mm F.Cu track from (10,10) to (20,10) mm, no net.

- `pcb drc --format json --severity-all --exit-code-violations -o ka_drc.json ka.kicad_pcb` printed `Found 1 violations / Found 0 unconnected items`, exit code 5. JSON: one violation `track_dangling`, severity `warning`, "Track has unconnected end". Expected: exactly that one violation. PASS.
- `pcb export stats --format json` reported `"width": "100.0000 mm", "height": "50.0000 mm", "area": "5000.00 mm²", "min_track_width": "0.2500 mm", "board_thickness": "1.6000 mm"`. PASS.
- `pcb export gerbers -o gerb/ --layers F.Cu,Edge.Cuts --no-protel-ext` wrote `ka-F_Cu.gbr`, `ka-Edge_Cuts.gbr`, `ka-job.gbrjob`, exit 0.
- `pcb export drill -o gerb/ --format excellon --generate-map --map-format pdf` wrote `ka.drl` and `ka-drl_map.pdf`, exit 0.
- `pcb export pos --format csv --units mm --side both` wrote a CSV with header `Ref,Val,Package,PosX,PosY,Rot,Side` (no footprints, so header only). PASS.
- `pcb export svg --layers F.Cu,Edge.Cuts --page-size-mode 2` wrote a 38 kB SVG.
- `pcb render -o ka_render.png -w 640 -h 480 --side top` produced a PNG in 0.29 s wall time (basic quality).
- `pcb export step --no-dnp` produced `ka.step` (8.8 kB) in 0.007 s.

### F5. kicad-cli schematic known-answer run: ERC count is deterministic and matches design intent

Schematic: two `Device:R` symbols (R1 10k, R2 4k7, footprint `Resistor_SMD:R_0603_1608Metric`) on the 1.27 mm grid at (101.6, 101.6) and (121.92, 101.6) with one wire joining their pin 1s; pin 2 of each left open. Expected ERC: exactly two `pin_not_connected` errors.

- With project-local library tables (F6): `sch erc --format json --severity-all -o erc.json ka2.kicad_sch` printed `Found 2 violations`; JSON counter `{('pin_not_connected','error'): 2}`. PASS. With `--exit-code-violations` the exit code is 5; without it, 0.
- Off-grid placement (first attempt at y = 96.19 mm) added three `endpoint_off_grid` warnings; this is a useful ERC check to keep enabled for generated schematics.
- Without library tables the same file yields 6 violations: the 2 errors plus `footprint_link_issues` x2 ("The current configuration does not include the footprint library 'Resistor_SMD'") and `lib_symbol_issues` x2 ("... symbol library 'Device'").
- `sch export netlist --format spice` produced: `R1 Net-_R1-Pad1_ unconnected-_R1-Pad2_ 10k` and `R2 Net-_R1-Pad1_ unconnected-_R2-Pad2_ 4.7k` (KiCad normalised `4k7` to `4.7k`). PASS.
- `sch export netlist` (kicadsexpr) contains 3 `(net` blocks; `--format kicadxml` contains 2 `<comp` entries. PASS.
- `sch export bom -o ka_bom.csv --fields "Reference,Value,Footprint,${QUANTITY}" --group-by Value` produced two rows with quantity 1 each. PASS.
- `sch export svg -o dir/ -e -n` and `sch export pdf -o ka_sch.pdf` produced a 6.6 kB SVG and a 26 kB `%PDF-1.5` file.

### F6. Headless library configuration: the GUI first-run has not created global library tables; project-local tables fix it

`~/Library/Preferences/kicad/10.0/` contains `kicad_common.json`, `eeschema.json`, `pcbnew.json` etc. but no `sym-lib-table` or `fp-lib-table`. kicad-cli therefore emits `lib_symbol_issues` / `footprint_link_issues` warnings for every standard-library symbol.

Verified recipe: place next to the schematic a `sym-lib-table` with `(lib (name "Device")(type "KiCad")(uri "${KICAD10_SYMBOL_DIR}/Device.kicad_sym")...)`, an `fp-lib-table` with `(uri "${KICAD10_FOOTPRINT_DIR}/Resistor_SMD.pretty")`, and a `<same-basename>.kicad_pro`. kicad-cli then resolves `KICAD10_SYMBOL_DIR` to `/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols` (224 libraries) and `KICAD10_FOOTPRINT_DIR` to `.../footprints` (155 libraries) and the warnings disappear (F5). The project file must share the schematic's basename: the same file copied as `rt.kicad_sch` without `rt.kicad_pro` regained the 4 warnings; adding `rt2.kicad_pro` removed them.

kicad-cli also prints a harmless Fontconfig cache warning on every run on this Mac (`We will not regenerate the cache because some cache files were generated by a newer version...`); wrappers should filter stderr for `Fontconfig`.

### F7. ERC/DRC JSON reports validate against KiCad's published schema; the published DRC schema is invalid JSON

Reports carry `"$schema": "https://schemas.kicad.org/erc.v1.json"` and `.../drc.v1.json`; those URLs redirect (HTTP 200 after redirect) to `https://gitlab.com/kicad/code/kicad/-/raw/master/resources/schemas/{erc,drc}.v1.json` (draft-07, `additionalProperties: false`). The KiCad.app bundle's `SharedSupport/schemas/` contains only `api.v1`, `pcm.v1/v2` and remote-library schemas, not erc/drc.

- `jsonschema.validate(erc.json, erc.v1.json)` with jsonschema 4.26.0: VALID.
- `drc.v1.json` (both `master` and the `10.0` branch, 4470 bytes) fails `json.load`: "Illegal trailing comma before end of array: line 92 column 23" (a trailing comma after `"coordinate_units",` in the `required` array). After removing the trailing comma the DRC report validates. The report itself (`ka_drc.json`) is valid JSON.

### F8. Bundled KiCad Python 3.9.13 with SWIG pcbnew works; SWIG is deprecated and leaves in KiCad 11

`/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/3.9/bin/python3` is Python 3.9.13 (universal). `import pcbnew; pcbnew.GetBuildVersion()` returns `10.0.6`; `pcbnew.py` and `_pcbnew.so` live in its `site-packages`. Bundled packages: wxPython 4.2.2a1, requests 2.32.5, sip 6.8.3, attrdict, pip 22.0.4; no numpy. `kipy` is not bundled.

Known answer: built a board in memory (4 Edge.Cuts segments + one track), `SaveBoard`, `LoadBoard`, then `ToMM(track.GetLength()) == 10.0`, one track, `GetBoardEdgesBoundingBox()` = 100.1 x 50.1 mm (outline plus 0.1 mm line width). PASS. The saved file has `(version 20260206) (generator "pcbnew")`. A harmless `wxWidgets assert "traits" failed ... create wxApp before calling this` is printed when running outside the GUI.

Primary sources: "The SWIG-based Python bindings in KiCad are deprecated as of KiCad 9.0 ... The current plan is to remove the SWIG bindings in KiCad 11.0" (https://dev-docs.kicad.org/en/apis-and-binding/pcbnew/index.html). IPC API: "The IPC API in KiCad 9 and 10 has no support for plotting or exporting files ... Users of previous versions may make use of kicad-cli"; "only supports communication with a running instance of the KiCad GUI"; "KiCad 9 and 10 only support IPC API plugins in the PCB Editor" (https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/index.html). `kicad-python` 0.8.0 (PyPI, 2026-08-30, requires Python >= 3.9) imports on Python 3.13 and raises `ConnectionError` without a running KiCad, as documented.

Consequence: Python 3.9 cannot run the modern numeric stack (numpy 2.5.3 requires >= 3.12), so board-side `pcbnew` scripts must run under KiCad's interpreter, separate from the project venv (3.13.5).

### F9. kiutils 1.4.8 reads KiCad 10 files; schematic write survives ERC; board write is broken for KiCad 10

PyPI: kiutils 1.4.8 uploaded 2024-02-02, requires Python >= 3.7, "Simple and SCM-friendly KiCad file parser for KiCad 6.0 and up". Open issues include #113 "Broken as of KiCAD 8?" (2024-02-29) and #120 "kiutils (v1.4.8) doesnt save KiCad Schematic properly" (2024-09-18) (https://github.com/mvnmgrx/kiutils/issues).

Empirical (scratch venv, Python 3.13.5):
- `Schematic.from_file` on the `(version 20250114)` schematic: OK, 2 symbols, 1 lib symbol, 1 wire. `to_file` round-trip dropped tokens `exclude_from_sim`, `embedded_fonts`, `generator_version`, `hide`, `do_not_autoplace`, `duplicate_pin_numbers_are_jumpers`, yet kicad-cli ERC on the output (with matching `.kicad_pro`) gave the identical 2 `pin_not_connected` errors and nothing else. Usable for schematics if kicad-cli validates the result.
- `Board.from_file` on the `(version 20260206)` board: OK (1 trace, 4 shapes), but `to_file` emitted `(segment ... (net ) (tstamp ))` and dropped ~10 setup tokens; kicad-cli then fails: "Failed to load board: Expecting net name. Got '')'' in 'kiutils_roundtrip.kicad_pcb', line 78". Not usable for writing KiCad 10 boards.

### F10. kicad-skip 0.2.5 edits KiCad 10 schematics and its output passes kicad-cli

PyPI: kicad-skip 0.2.5 uploaded 2024-02-16, requires Python >= 3.8, depends on sexpdata (1.0.2, 2024-01-09); 22 open issues, latest activity 2026-05-13 (https://github.com/psychogenic/kicad-skip/issues). Empirical: `Schematic('ka2.kicad_sch')` loaded 2 symbols, read `R1.property.Value.value == '10k'`, set it to `22k`, `write()`; kicad-cli ERC on the output: 2 `pin_not_connected` errors only; BOM shows `R1,22k`. PASS. The library prints debug noise (`Passed key  -- can't parsy`) on load. Element creation from scratch is limited ("it is possible to go beyond cloning and create elements using new()" for wires, labels, text), so it is a clone-and-edit tool, not a from-scratch generator.

### F11. OpenSCAD 2021.01 is installed (Intel binary under Rosetta); CLI known answer passes; a universal 2026.09.23 snapshot exists

`/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD --version` prints `OpenSCAD version 2021.01`; `file` reports `Mach-O 64-bit executable x86_64` (Rosetta). `--info`: CGAL 4.14.3, Boost 1.74, Qt 5.9.9, lib3mf 1.8.1. CLI: `-o FILE` (stl, off, amf, 3mf, csg, dxf, svg, pdf, png, echo, ast, term, nef3), `--export-format asciistl|binstl`, `-D var=val`, `-p/-P` customizer sets, `--camera`, `--autocenter`, `--viewall`, `--imgsize`, `--render`, `--projection`, `--colorscheme`, `-d` deps file, `--hardwarnings`, `-q`.

Known answer: `cube(10)` exported as ASCII STL in 0.67 s wall time: 12 triangles; volume by divergence theorem = 1000.000000 mm^3. PASS. `-o cube.echo` captured `ECHO: version = [2021, 1, 0]` and `ECHO: vol = 1000`. `-o cube.png --render --imgsize=320,240 --autocenter --viewall` produced a PNG. numpy-stl `get_mass_properties()` on the same file: volume 1000.0. PASS.

Release status: Wikipedia infobox and Homebrew cask `openscad` both give stable 2021.01 (2021-01-31). Homebrew cask `openscad@snapshot` is 2026.09.23 and `https://files.openscad.org/snapshots/.snapshot_macos.js` lists `OpenSCAD-2026.09.23.dmg` (70 MB, universal). The downloads page states the snapshot supports "Intel and Apple Silicon" and that "the new Manifold geometry engine" can be enabled (https://openscad.org/downloads.html).

### F12. LTspice 26.0.2.1 is installed as a CrossOver (Wine) wrapped Windows build; batch mode not confirmed by this assignment

`/Applications/LTspice.app/Contents/Info.plist`: `CFBundleShortVersionString 26.0.2.1`, `CFBundleGetInfoString "26.0.2.1, Copyright 2025 Analog Devices, Inc."`, `CFBundleIconFile CrossOverOEM`. The bundle contains `Contents/SharedSupport/ltspice/lib/wine/...` and `bin/wine`; the launcher `Contents/MacOS/LTspice` is an x86_64 Mach-O. A Wine bottle exists at `~/Library/Application Support/LTspice/Bottles/`. Homebrew cask `ltspice` is 26.0.2.

Documented switches (https://ltwiki.org/LTspiceHelp/LTspiceHelp/Command_Line_Switches.htm): `-b` "Run in batch mode ... will leave the data in file deck.raw", `-Run`, `-ascii`, `-netlist` "Batch conversion of a schematic to a netlist", `-encrypt`, `-FastAccess`, `-wine/-nowine`. spicelib 1.6.3 (`spicelib/simulators/ltspice_simulator.py`) searches `/Applications/LTspice.app/Contents/MacOS/LTspice`, uses `['-Run','-b']` by default and only `-b` for the native Mac build, and carries the caveats "macOS native LTspice accepts no command line switches (yet)" and "cannot run simulations on '.asc' files"; on this machine `LTspice.is_available()` returns True with `spice_exe = ['/Applications/LTspice.app/Contents/MacOS/LTspice']`. Those caveats were written for the discontinued native build, not the CrossOver build.

My probe `LTspice -b ltdiv.net` (10 k / 10 k divider) via the app launcher exited without producing `.log` or `.raw` within 60 s. The process table showed another agent session concurrently driving the same bottle with `SharedSupport/ltspice/bin/wine --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' -b 'Z:\private\tmp\cwht-ltspice\...net'` and collecting CrossOver debug logs, so my result is inconclusive and this item is deferred to the SPICE assignment. Only one Wine bottle exists, so batch runs must be serialised.

### F13. No ngspice CLI; KiCad ships libngspice 45.2 as a library only

`ngspice` is not on PATH. KiCad bundles `Contents/Frameworks/libngspice.0.dylib` and `Contents/PlugIns/sim/libngspice.dylib` plus a `PlugIns/sim/ngspice/` directory of code models (not an executable). Homebrew formula `ngspice` 47 is available but not installed. PySpice 1.5 (PyPI) could drive the shared library, but the project already standardises on LTspice.

### F14. Project Python: 3.13.5 venv with only scraping dependencies

`/Users/robinonsay/rust/cwht/.venv/bin/python --version` = Python 3.13.5 (Homebrew `python@3.13`, arm64). `tools/requirements.txt` currently lists `beautifulsoup4 markdownify jsonschema requests lxml` unpinned; installed: beautifulsoup4 4.15.0, markdownify 1.2.3, jsonschema 4.26.0, requests 2.34.2, lxml 6.1.3. None of numpy, scipy, matplotlib, skrf, PyLTSpice, kiutils, skip, pytest, yaml import. `/usr/bin/python3` is Apple's 3.9.6. `uv` and `pipx` are absent.

### F15. Proposed Python pins install cleanly on 3.13.5 arm64 and pass known answers (scratch venv)

PyPI metadata (2026-09-25) and results:

| Package | Pin | Uploaded | requires_python | Known answer |
|---|---|---|---|---|
| numpy | 2.5.3 | 2026-09-06 | >= 3.12 | imported; used by all below |
| scipy | 1.18.1 | 2026-08-21 | >= 3.12 | imported |
| matplotlib | 3.11.2 | 2026-09-11 | >= 3.11 | Agg backend wrote a 17.5 kB PNG of a 144 MHz low-pass response |
| scikit-rf | 2.1.0 | 2026-08-13 | >= 3.10 | `DefinedGammaZ0(z0=50).resistor(100)` at 144 MHz: abs(S11) = 0.500000 (theory R/(R+2Z0) = 0.5). PASS |
| PyLTSpice | 6.0.1 | 2026-06-19 | >= 3.10 | imports; wraps spicelib |
| spicelib | 1.6.3 | 2026-07-21 | >= 3.10, < 4 | `SpiceEditor('ltdiv.net').get_component_value('R1') == '10k'`, components `['V1','R1','R2']`. PASS |
| kiutils | 1.4.8 | 2024-02-02 | >= 3.7 | see F9 (read OK; sch write OK; board write FAIL) |
| kicad-skip | 0.2.5 | 2024-02-16 | >= 3.8 | see F10. PASS |
| sexpdata | 1.0.2 | 2024-01-09 | >= 3.7 | dependency of kicad-skip |
| kicad-python | 0.8.0 | 2026-08-30 | >= 3.9 | imports; ConnectionError without GUI (expected) |
| jsonschema | 4.26.0 | 2026-01-07 | >= 3.10 | validated ERC report against erc.v1.json (F7). PASS |
| pytest | 9.1.1 | 2026-06-19 | >= 3.10 | imports |
| PyYAML | 6.0.3 | 2025-09-25 | >= 3.8 | imports |
| lizard | 1.24.0 | 2026-08-19 | unspecified | `lizard -l rust ccn.rs`: `classify` CCN 5, `trivial` CCN 1; rustos `api/src` AvgCCN 1.2 over 4 functions |
| pymupdf | 1.28.2 | 2026-08-06 | >= 3.10 | A4 schematic PDF page at 150 dpi -> 1754 x 1241 px (expected 1754 x 1240, rounding); SVG -> PNG 788 x 394 |
| numpy-stl | 4.0.1 | 2026-09-07 | >= 3.10 | cube volume 1000.0. PASS |

Not recommended: `ltspice` 1.0.6 (last upload 2022-10-04, no `requires_python`); spicelib's `RawRead` covers `.raw` parsing.

### F16. Rust toolchain state

- rustup 1.29.0; default `stable-aarch64-apple-darwin` = rustc/cargo 1.98.0 (2026-08-18, LLVM 22.1.8); components: cargo, clippy (0.1.98), rust-docs, rust-src, rust-std (host and `thumbv8m.main-none-eabihf`), rustc, rustfmt 1.9.0.
- nightly 1.100.0-nightly (e7769602a 2026-08-24, LLVM 23.1.0) installed with cargo/clippy/rust-docs/rust-std(host)/rustc/rustfmt; no `thumbv8m` target, no `rust-src`, no `llvm-tools`.
- `llvm-tools` component is available for both toolchains but not installed (`rustup component list | grep llvm-tools`).
- cargo-binutils 0.4.0 proxies are installed (`cargo size`, `cargo cov`, `cargo profdata`, `cargo objdump`...). `cargo cov -- --version` panics inside clap_builder 4.6.6 (`arg no-default-features's ArgAction should be one of SetTrue, SetFalse`), and it would need `llvm-tools` in any case.
- Xcode Command Line Tools with Apple clang 21.0.0; git 2.50.1; GNU make 3.81; cmake present; ninja and pkg-config absent.
- `picotool v2.3.0` (Homebrew) present; rustos `templates/pico2/.cargo/config.toml` sets `runner = "picotool load -u -x -t elf"` and `-C link-arg=-Tlink.ld`. Not installed: probe-rs, elf2uf2-rs, cargo-nextest, cargo-audit, cargo-deny, cargo-binstall, cargo-embed, cargo-flash. No RP2350 emulator (qemu-system-arm, renode) found.

### F17. crates.io status of the requested Rust tools (API queried 2026-09-25)

| Crate | Latest | Released | MSRV | Notes |
|---|---|---|---|---|
| cargo-llvm-cov | 0.9.1 | 2026-09-06 | 1.87 | README: `cargo +stable install cargo-llvm-cov --locked`; outputs `--json --lcov --cobertura --codecov --text --html`; `--branch` "unstable", `--mcdc` "unstable"; doc tests need nightly |
| cargo-geiger | 0.13.0 | 2025-08-31 | 1.85 | counts unsafe usage per crate; `--output-format json`; README: "this tool is not meant to advise directly whether the code ultimately is truly insecure" |
| rust-code-analysis-cli | 0.0.25 | 2023-01-13 | none stated | no release in 3.7 years; repo not archived; computes cyclomatic, cognitive, Halstead, MI, LOC, nargs, nexits for Rust |
| cargo-tarpaulin | 0.37.4 | 2026-09-21 | none stated | alternative coverage tool |
| cargo-nextest | 0.9.146 | 2026-09-21 | 1.91 | test runner with JUnit output |
| cargo-audit | 0.22.2 | 2026-06-05 | 1.88 | RustSec advisories |
| cargo-deny | 0.20.2 | 2026-07-09 | 1.88.0 | licenses, bans, advisories |
| cargo-mutants | 27.1.0 | 2026-06-02 | 1.88 | mutation testing |
| probe-rs-tools | 0.32.0 | 2026-07-22 | 1.89 | debug probe tooling (RP2350 supported upstream) |
| elf2uf2-rs | 2.2.0 | 2025-10-06 | none stated | UF2 conversion (picotool already covers this) |
| defmt-print | 1.1.0 | 2026-05-12 | 1.83 | defmt log decoding |

Sources: `https://crates.io/api/v1/crates/<name>`; https://github.com/taiki-e/cargo-llvm-cov ; https://github.com/rust-secure-code/cargo-geiger ; https://github.com/mozilla/rust-code-analysis.

### F18. MC/DC instrumentation has been removed from rustc; the installed nightly rejects it

- rust-lang/rust PR #144999 "Remove MC/DC" (rollup merge commit 562222b, August 2025): the unstable `-Zcoverage-options=mcdc` implementation was removed because it "has proven itself to be a major burden on overall maintenance of coverage instrumentation" (https://github.com/rust-lang/rust/pull/144999). The Rust project goal "Implement and Maintain MC/DC Coverage Support" (https://github.com/rust-lang/goals/issues/638) proposes re-implementing DC and MC/DC with AdaCore maintenance in 2026; nothing has landed in the toolchain on this machine.
- Unstable book (nightly, fetched 2026-09-25) lists only `block`, `branch`, `condition` for `-Z coverage-options` (https://doc.rust-lang.org/nightly/unstable-book/compiler-flags/coverage-options.html).
- Local test with `rustup run nightly rustc -Z coverage-options=<opt> -C instrument-coverage --crate-type lib --emit=obj ccn.rs`: `block`, `branch`, `condition` compile; `mcdc` and `no-mcdc` fail with `error: incorrect value 'mcdc' for unstable option 'coverage-options' - 'block' | 'branch' | 'condition' was expected`.
- Stable 1.98.0: `-C instrument-coverage` compiles a host object (region coverage); `-Z coverage-options` is refused ("only accepted on the nightly compiler").
- cargo-llvm-cov CHANGELOG: `--mcdc` added in 0.6.11 (2024-07-18) and 0.6.14 (2024-10-12); the flag remains documented as "unstable" in 0.9.1 but cannot work on current nightlies.

### F19. Complexity measurement options

- clippy `cognitive_complexity`: group `restriction`, default `allow`, configured by `cognitive-complexity-threshold` (default 25) in `clippy.toml`; its past name was `cyclomatic_complexity`; the docs say "The true Cognitive Complexity of a method is not something we can calculate" and point to `too_many_lines` (https://rust-lang.github.io/rust-clippy/master/index.html#cognitive_complexity). It is not a McCabe cyclomatic number.
- lizard 1.24.0 (Python, maintained, Rust supported) reports McCabe CCN per function and can gate with `-C 15` (verified output in F15).
- rust-code-analysis-cli 0.0.25 reports cyclomatic and more but is stale (F17); whether it builds on rustc 1.98 was not tested.

### F20. Rendering for the charter's visual-closure rule needs no extra system packages

Available: `kicad-cli sch export pdf|svg`, `kicad-cli pcb export svg`, `kicad-cli pcb render` (PNG/JPEG direct), OpenSCAD `-o file.png`. Conversion to PNG for review packages: macOS built-in `sips -s format png ka_sch.pdf --out ka_sch.png` produced an 842 x 595 RGBA PNG (72 dpi, first page); `pymupdf` gives dpi control and SVG rasterisation. Not present: ImageMagick, Inkscape, rsvg-convert, Ghostscript, cairo (so `cairosvg` would need `brew install cairo`; avoid).

### F21. Homebrew and misc

Homebrew 6.0.20; formulae installed include `python@3.13`, `node` (v25.9.0, npx 11.12.1, used by the `.mcp.json` claude-context server); `/usr/bin/jq` present. Casks available (not necessarily installed via brew): `kicad 10.0.6`, `openscad 2021.01`, `openscad@snapshot 2026.09.23`, `ltspice 26.0.2`; formula `ngspice 47`.

## Tool table (found, purpose, accreditation)

| Tool | Version found | Path | Purpose on cwht | Known-answer verification (accreditation idea) | Result |
|---|---|---|---|---|---|
| kicad-cli | 10.0.6 (arm64) | /Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli | ERC/DRC (Inspection), Gerber/drill/pos/STEP exports, SVG/PDF/PNG renders, netlist and BOM for traceability | 2-resistor schematic -> exactly 2 `pin_not_connected`; dangling-track board -> exactly 1 `track_dangling`; stats area 5000 mm^2; SPICE netlist text; BOM rows; exit code 5 with `--exit-code-violations` | PASS |
| KiCad Python (pcbnew, SWIG) | Python 3.9.13, pcbnew 10.0.6 | .../Frameworks/Python.framework/Versions/3.9/bin/python3 | Programmatic board construction/inspection (Rev A only; gone in KiCad 11) | Build board, save, reload: 1 track of 10.000 mm, outline 100.1 x 50.1 mm | PASS |
| kicad-python (kipy, IPC) | 0.8.0 | project venv (proposed) | Live GUI automation only (KiCad 9/10) | import OK; ConnectionError without GUI | PASS (as designed) |
| kiutils | 1.4.8 | venv (proposed) | Read `.kicad_sch/.kicad_pcb` for traceability checks; generate schematics with kicad-cli validation | Parse KiCad 10 sch and pcb; sch round-trip ERC identical; pcb round-trip unloadable | PARTIAL (read OK, board write FAIL) |
| kicad-skip | 0.2.5 | venv (proposed) | Clone-and-edit schematic generation | Edit R1 to 22k, write; kicad-cli ERC 2 errors, BOM shows 22k | PASS |
| OpenSCAD | 2021.01 (x86_64 via Rosetta) | /Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD | Enclosure CAD, STL/3MF/STEP-via-DXF exports, PNG renders for review | `cube(10)` STL: 12 facets, volume 1000.000 mm^3; echo version [2021,1,0]; PNG render | PASS |
| LTspice | 26.0.2.1 (CrossOver/Wine, x86_64) | /Applications/LTspice.app | SPICE analysis (Analysis evidence class) | 10k/10k divider `-b` batch run should yield V(out)=5.000 V in `.raw`; not reproduced here (see F12) | INCONCLUSIVE, deferred |
| libngspice (KiCad) | 45.2 | .../Frameworks/libngspice.0.dylib | Optional second engine via KiCad GUI or PySpice | none run (no CLI) | N/A |
| Python venv | 3.13.5 (arm64) | /Users/robinonsay/rust/cwht/.venv | All project scripts | version check | present, missing packages |
| numpy / scipy / matplotlib | 2.5.3 / 1.18.1 / 3.11.2 | venv (proposed) | Budgets, filters, plots | matplotlib Agg PNG written | PASS |
| scikit-rf | 2.1.0 | venv (proposed) | S-parameter models, matching networks, NanoVNA Touchstone import | abs(S11) of 100 ohm series in 50 ohm = 0.5 | PASS |
| PyLTSpice / spicelib | 6.0.1 / 1.6.3 | venv (proposed) | Netlist editing, LTspice batch driving, `.raw` parsing, pass/fail checks | SpiceEditor reads R1=10k; LTspice detected | PASS (parser); runner deferred |
| jsonschema | 4.26.0 | venv (present) | Validate requirements.json, ERC/DRC JSON, tool reports | ERC report valid vs erc.v1.json | PASS |
| pymupdf | 1.28.2 | venv (proposed) | PDF/SVG -> PNG for review packages | A4 at 150 dpi -> 1754 x 1241 px | PASS |
| numpy-stl | 4.0.1 | venv (proposed) | STL volume/bounding-box checks on enclosure exports | cube volume 1000.0 | PASS |
| lizard | 1.24.0 | venv (proposed) | Cyclomatic complexity gate (SWE-220) for Rust | known function CCN 5, trivial CCN 1 | PASS |
| pytest / PyYAML | 9.1.1 / 6.0.3 | venv (proposed) | Test harness for tools; config | import | PASS |
| rustc / cargo (stable) | 1.98.0, LLVM 22.1.8 | ~/.cargo/bin | Firmware build (thumbv8m target installed), host unit tests | `-C instrument-coverage` object emitted | PASS |
| rustc nightly | 1.100.0-nightly 2026-08-24 | rustup | Branch/condition coverage only | `-Z coverage-options=branch|condition` accepted; `mcdc` rejected | PASS / MC/DC unavailable |
| clippy / rustfmt | 0.1.98 / 1.9.0 | rustup | Static analysis, formatting (SWE-135) | version | present |
| llvm-tools component | not installed | rustup | Required by cargo-llvm-cov | none | MISSING |
| cargo-binutils | 0.4.0 | ~/.cargo/bin | size/objdump of firmware ELF | `cargo cov -- --version` panics (clap bug) | BROKEN |
| picotool | 2.3.0 | /opt/homebrew/bin/picotool | Flash/UF2/ELF inspection for RP2350 | version | present |
| cargo-llvm-cov | 0.9.1 on crates.io | not installed | Coverage (SWE-189/190) | install then `cargo llvm-cov --lcov` on a crate with one covered and one uncovered function | to do |
| cargo-geiger | 0.13.0 on crates.io | not installed | Unsafe audit (SWE-135) | run on a crate with a single `unsafe` block, expect count 1 | to do |
| rust-code-analysis-cli | 0.0.25 (2023) on crates.io | not installed | Cyclomatic metrics | superseded by lizard unless it builds | not recommended |
| sips | macOS built-in | /usr/bin/sips | Quick PDF -> PNG | 842 x 595 PNG | PASS |
| jq | macOS built-in | /usr/bin/jq | JSON in shell wrappers | used in this study | PASS |

## Implications for cwht

1. **REQ-candidate (tools baseline).** The project shall record a tools manifest (`tools/manifest.json`) with pinned versions: KiCad 10.0.6, OpenSCAD (2021.01 or 2026.09.23, see decision 12), LTspice 26.0.2.1, Python 3.13.5, rustc 1.98.0 stable (plus the nightly date if used for branch coverage), and every Python package pin; `tools/check_env.py` shall fail when a version differs. This is the SE HB tool-control analogue for Class A.
2. **REQ-candidate (tool accreditation).** Every tool used to produce verification evidence shall pass a known-answer suite (`tools/accredit/`) before its output is admitted as evidence, using the cases in the table above; results are attached to the review package.
3. **REQ-candidate (Inspection gates).** ERC and DRC shall be run headless with `--format json --severity-all --exit-code-violations`, validated against the KiCad schema, with zero errors and all warnings either fixed or excluded with a recorded rationale; `pcb drc --schematic-parity --refill-zones` shall be used for the release baseline.
4. **REQ-candidate (generated artefacts).** Any schematic or board produced or edited by Python shall be re-validated by kicad-cli (ERC, netlist, BOM for schematics; DRC, stats for boards) before commit; writer libraries are not trusted (F9).
5. **RISK-candidate (MC/DC).** rustc cannot instrument MC/DC today (F18). The charter's SWE-219 target of 100 percent MC/DC for safety-critical components cannot be measured by the toolchain. Options: (a) tailor SWE-219 in the RMM to "condition coverage (`-Z coverage-options=condition`, nightly) plus manually derived MC/DC test matrices for each safety-critical decision, kept in `docs/test_cases/`"; (b) constrain safety-critical decisions to at most 2 or 3 conditions so manual MC/DC is tractable; (c) re-evaluate when rust-lang/goals#638 lands. DECISION-needed at the SEMP/RMM level.
6. **RISK-candidate (SWIG removal).** `pcbnew` scripting disappears in KiCad 11 and the IPC API in 9/10 needs the GUI and cannot export. Rev A shall pin KiCad 10.0.x; board automation shall prefer kicad-cli, use `pcbnew` only where unavoidable, and be isolated in `tools/kicad_py/` so it can be migrated.
7. **RISK-candidate (two Pythons).** Board-side scripts run on KiCad's Python 3.9 (no numpy 2.x); analysis scripts run on 3.13. Wrappers shall pass data between them as JSON files, never import across.
8. **RISK-candidate (LTspice under CrossOver).** Batch invocation from scripts is unconfirmed (F12) and the single Wine bottle forbids parallel simulations. Until the SPICE assignment confirms a working command, Analysis evidence generation is blocked; fallback is Homebrew `ngspice` 47 with KiCad-exported SPICE netlists.
9. **RISK-candidate (kiutils board writer).** kiutils 1.4.8 cannot write loadable KiCad 10 boards and drops newer tokens from schematics. Use it read-only, or only for schematics with mandatory kicad-cli validation (implication 4).
10. **RISK-candidate (stale libraries).** kiutils (2024-02), kicad-skip (2024-02), sexpdata (2024-01) and rust-code-analysis (2023-01) have no recent releases. Either accept with accreditation tests on every KiCad point release, or write a small in-house S-expression emitter for the few constructs needed.
11. **RISK-candidate (upstream schema defect).** KiCad's published `drc.v1.json` is invalid JSON (F7). Keep a patched copy in `tools/schemas/` with a note; ACTION: report to the KiCad issue tracker.
12. **DECISION-needed (OpenSCAD build).** Stable 2021.01 runs under Rosetta with 2021 CGAL; the 2026.09.23 snapshot is universal with Manifold and much faster CSG. Recommendation: adopt the snapshot only if pinned by exact date in the manifest and accredited by the cube and a representative enclosure model; otherwise stay on 2021.01.
13. **DECISION-needed (coverage stack).** Recommend cargo-llvm-cov 0.9.1 (+ `rustup component add llvm-tools`) with cargo-nextest 0.9.146 for JUnit output, region coverage on stable for the record and branch/condition coverage on the pinned nightly as supplementary evidence; cargo-tarpaulin as the fallback.
14. **DECISION-needed (complexity metric).** Recommend lizard 1.24.0 `-l rust -C 15` as the SWE-220 cyclomatic gate plus `clippy.toml` `cognitive-complexity-threshold = 15` and `too-many-lines-threshold` as supporting lints; record the CCN counting convention in the coding standard (lizard gave CCN 5 for two `if`, one `&&` and a 3-arm `match`).
15. **DECISION-needed (unsafe audit).** cargo-geiger 0.13.0 for counts plus a manual review list of every `unsafe` block (geiger's README states it does not judge safety).
16. **ACTION.** Create `hardware/kicad/sym-lib-table`, `fp-lib-table` and the `.kicad_pro` with the standard library entries so headless ERC/DRC does not emit library warnings (F6).
17. **ACTION.** Add `tools/requirements.txt` pins (below), `tools/setup.sh`, `tools/env.sh`, `tools/accredit/`, and filter Fontconfig noise in kicad-cli wrappers; always pass `--mode-single` or `--mode-multi` to `pcb export svg`.
18. **ACTION (owner approval needed).** `rustup component add llvm-tools` and `cargo install --locked cargo-llvm-cov@0.9.1 cargo-nextest@0.9.146 cargo-geiger@0.13.0 cargo-audit@0.22.2 cargo-deny@0.20.2`; add `thumbv8m.main-none-eabihf` and `rust-src` to the nightly toolchain if nightly coverage of target-specific code is wanted. Fix or drop cargo-binutils (F16).
19. **ACTION.** Position files for PCBWay assembly must be exported with `--units mm` (default is inches) and the drill/place origin choice recorded in the ICD.

## Proposed `tools/requirements.txt` (pinned; Python 3.13.5, macOS arm64)

```
# cwht tools environment. Interpreter: Homebrew python@3.13 (3.13.5), arm64.
# Existing scraping dependencies, now pinned to the installed versions
beautifulsoup4==4.15.0
markdownify==1.2.3
requests==2.34.2
lxml==6.1.3
jsonschema==4.26.0
# Numerics and plotting (Analysis evidence, budgets, plots for review packages)
numpy==2.5.3
scipy==1.18.1
matplotlib==3.11.2
# RF (S-parameters, matching, Touchstone import from NanoVNA)
scikit-rf==2.1.0
# SPICE automation and .raw parsing (LTspice batch runs, pass/fail checks)
PyLTSpice==6.0.1
spicelib==1.6.3
# KiCad file handling. Read with kiutils; clone-and-edit with kicad-skip;
# every generated file is re-validated with kicad-cli (ERC/DRC/netlist/BOM).
kiutils==1.4.8
kicad-skip==0.2.5
sexpdata==1.0.2
# KiCad IPC API client (needs a running KiCad 9/10 GUI; optional)
kicad-python==0.8.0
# Enclosure export checks (STL volume, bounding box)
numpy-stl==4.0.1
# Rendering for visual closure (PDF/SVG -> PNG at controlled dpi)
pymupdf==1.28.2
# Cyclomatic complexity for Rust (SWE-220 gate)
lizard==1.24.0
# Test harness and config
pytest==9.1.1
PyYAML==6.0.3
```

Once the pins are accepted, generate a hash-locked file (`pip hash` / `pip-compile --generate-hashes`) and install with `--require-hashes` for a reproducible Class A tools baseline.

## One-command setup script outline (`tools/setup.sh`)

```
#!/bin/zsh
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)

# 1. Preconditions (fail fast, print remedy; never install GUI apps silently)
[[ $(uname -m) == arm64 ]] || echo "warning: expected Apple Silicon"
xcode-select -p >/dev/null || { echo "install Xcode CLT: xcode-select --install"; exit 1; }
KICAD_CLI=/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
KICAD_PY=/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/3.9/bin/python3
OPENSCAD=/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD   # or the pinned snapshot
LTSPICE=/Applications/LTspice.app/Contents/MacOS/LTspice
for t in "$KICAD_CLI" "$KICAD_PY" "$OPENSCAD" "$LTSPICE"; do
  [[ -x $t ]] || { echo "missing $t (brew install --cask kicad openscad ltspice)"; exit 1; }
done
"$KICAD_CLI" version | grep -q '^10.0.6' || { echo "KiCad 10.0.6 required"; exit 1; }
"$OPENSCAD" --version 2>&1 | grep -q '2021.01' || echo "warning: OpenSCAD version differs from manifest"

# 2. Python environment (project venv, pinned)
/opt/homebrew/bin/python3.13 -m venv "$ROOT/.venv"
"$ROOT/.venv/bin/python" -m pip install --upgrade pip
"$ROOT/.venv/bin/python" -m pip install -r "$ROOT/tools/requirements.txt"   # later: --require-hashes

# 3. Rust toolchain (rust-toolchain.toml pins stable 1.98.0 and the target)
rustup show active-toolchain
rustup target add thumbv8m.main-none-eabihf
rustup component add clippy rustfmt llvm-tools
# optional pinned nightly for branch/condition coverage:
# rustup toolchain install nightly-2026-08-24 --component llvm-tools --target thumbv8m.main-none-eabihf

# 4. Cargo tools (pinned; requires network; owner approval recorded in ADR)
cargo install --locked cargo-llvm-cov@0.9.1 cargo-nextest@0.9.146 cargo-geiger@0.13.0 cargo-audit@0.22.2 cargo-deny@0.20.2

# 5. Environment file consumed by every tools/ script
cat > "$ROOT/tools/env.sh" <<ENV
export KICAD_CLI="$KICAD_CLI" KICAD_PY="$KICAD_PY" OPENSCAD="$OPENSCAD" LTSPICE="$LTSPICE"
export KICAD10_SYMBOL_DIR=/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols
export KICAD10_FOOTPRINT_DIR=/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints
export KICAD10_3DMODEL_DIR=/Applications/KiCad/KiCad.app/Contents/SharedSupport/3dmodels
ENV

# 6. Accreditation: known-answer suite writes tools/accredit/report.json and fails on any mismatch
"$ROOT/.venv/bin/python" "$ROOT/tools/accredit/run_all.py"
```

`tools/accredit/run_all.py` cases (from this study): kicad-cli ERC 2-resistor (expect 2 `pin_not_connected`), DRC dangling track (expect 1 `track_dangling`), stats area 5000 mm^2, SPICE netlist text, BOM rows; pcbnew 10 mm track; OpenSCAD cube volume 1000; LTspice divider V(out)=5.000 V (once the batch command is confirmed); scikit-rf abs(S11)=0.5; spicelib R1=10k; jsonschema ERC report valid; pymupdf 150 dpi page size; numpy-stl volume; lizard CCN of the reference file; cargo-llvm-cov on a two-function crate (one covered) expecting 50 percent function coverage; cargo-geiger on a one-`unsafe` crate expecting count 1. Each case records tool version, input hash, expected and observed values.

## Confidence

| Finding | Confidence | Basis |
|---|---|---|
| F1 to F5 kicad-cli commands, flags, known answers | High | run locally on 10.0.6 |
| F6 headless library tables | High | reproduced both failure and fix |
| F7 schema validation and upstream defect | High | validated locally; defect present in master and 10.0 branch on 2026-09-25 |
| F8 pcbnew works; SWIG removal in 11 | High | local run; dev-docs statement |
| F9 kiutils behaviour | High for the observed cases; Medium as a general statement (one schematic, one board) | local round-trips |
| F10 kicad-skip behaviour | Medium | one edit case; library unmaintained since 2024 |
| F11 OpenSCAD | High (installed) / Medium (snapshot suitability untested) | local run; openscad.org and Homebrew metadata |
| F12 LTspice batch | Low | inconclusive probe, concurrent session; deferred |
| F13 ngspice | High | file inspection |
| F14, F15 Python pins and accreditation | High | installed and exercised in scratch venv on 3.13.5 |
| F16 Rust toolchain state | High | rustup and cargo output |
| F17 crates.io status | High | API responses 2026-09-25 |
| F18 MC/DC removed | High | rustc error text locally; PR #144999; unstable book |
| F19 complexity options | Medium | clippy docs; lizard run; rust-code-analysis not built |
| F20 rendering path | High | sips and pymupdf runs |
| F21 Homebrew | High | brew metadata |

## Open items

1. Confirm the LTspice 26.0.2.1 batch command on macOS (launcher `-b` vs direct `SharedSupport/ltspice/bin/wine --bottle=ltspice ... LTspice.exe -b Z:\path.net`), its runtime, and whether `.asc` to `.net` conversion (`-netlist`) works under CrossOver; owned by the SPICE assignment. Decide the serialisation policy for the single Wine bottle.
2. Decide the SWE-219 MC/DC tailoring (implication 5) and record it in the RMM before PDR.
3. Choose OpenSCAD 2021.01 vs snapshot 2026.09.23 (implication 12) and accredit the chosen build with a representative enclosure model.
4. Test whether rust-code-analysis-cli 0.0.25 builds on rustc 1.98; if not, drop it in favour of lizard.
5. Install and accredit cargo-llvm-cov, cargo-nextest, cargo-geiger, cargo-audit, cargo-deny (owner approval; network).
6. Investigate or remove the panicking cargo-binutils proxies; `cargo size`/`objdump` are useful for firmware footprint evidence.
7. RP2350 emulation tool for the Emulation evidence class is absent (no qemu or renode); separate study required.
8. Report the `drc.v1.json` trailing-comma defect upstream and track the fix.
9. Plan the KiCad 11 migration (IPC headless via kicad-cli, SWIG removal) so Rev B is not blocked; watch for KiCad 11 headless export in the IPC API.
10. Decide whether to write a minimal in-house `.kicad_sch` emitter (sexpdata based) instead of relying on kiutils/kicad-skip, given their 2024 release dates.
11. Generate the hash-locked requirements file once pins are approved.

## Sources

- https://docs.kicad.org/10.0/en/cli/cli.html
- https://dev-docs.kicad.org/en/apis-and-binding/pcbnew/index.html
- https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/index.html
- https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/
- https://schemas.kicad.org/erc.v1.json and https://schemas.kicad.org/drc.v1.json (redirect to gitlab.com/kicad/code/kicad raw)
- https://github.com/mvnmgrx/kiutils and https://github.com/mvnmgrx/kiutils/issues
- https://github.com/psychogenic/kicad-skip and https://github.com/psychogenic/kicad-skip/issues
- https://pypi.org/pypi/<package>/json for numpy, scipy, matplotlib, scikit-rf, PyLTSpice, spicelib, ltspice, kiutils, kicad-skip, kicad-python, jsonschema, pytest, PyYAML, lizard, pymupdf, numpy-stl, trimesh, sexpdata
- https://crates.io/api/v1/crates/<crate> for cargo-llvm-cov, cargo-geiger, rust-code-analysis-cli, cargo-tarpaulin, cargo-nextest, cargo-audit, cargo-deny, probe-rs-tools, elf2uf2-rs, cargo-binutils, defmt-print, cargo-mutants
- https://github.com/taiki-e/cargo-llvm-cov (README and CHANGELOG)
- https://github.com/rust-secure-code/cargo-geiger
- https://github.com/mozilla/rust-code-analysis
- https://github.com/rust-lang/rust/pull/144999 and https://github.com/rust-lang/goals/issues/638
- https://doc.rust-lang.org/nightly/unstable-book/compiler-flags/coverage-options.html
- https://doc.rust-lang.org/nightly/rustc/instrument-coverage.html
- https://rust-lang.github.io/rust-clippy/master/index.html#cognitive_complexity
- https://openscad.org/downloads.html and https://files.openscad.org/snapshots/.snapshot_macos.js
- https://en.wikipedia.org/wiki/OpenSCAD
- https://ltwiki.org/LTspiceHelp/LTspiceHelp/Command_Line_Switches.htm
- https://raw.githubusercontent.com/nunobrum/spicelib/master/spicelib/simulators/ltspice_simulator.py
- Local commands recorded in the Findings; scratch artefacts under the session scratchpad `ka/` directory (not retained in the repo).
