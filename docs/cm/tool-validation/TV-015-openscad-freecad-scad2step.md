# TV-015: OpenSCAD 2021.01 and FreeCAD 1.1.3 through tools/scad2step.py (git blob d0277ec8)

| Field | Value |
|---|---|
| Record | TV-015 |
| Status | **Validated** 2026-09-27 (known-answer run 1 at commit `0743499`, 22 tests passed, 0 skipped; reproducibility run passed). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | A, product-generating (CM plan section 9.1: OpenSCAD 2021.01 CSG and FreeCAD 1.1.3 `freecadcmd` with `tools/scad2step.py` STEP, the files of the enclosure release package) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8) through CM plan section 9; CM plan section 8.2 step 3; ADR-008 (restricted OpenSCAD dialect, STEP acceptance checks) |
| Due | PDR (CM plan section 13 PDR row). First cited use: the enclosure concept model of WP-PDR-39 (PDR work plan); the release use is the CDR procurement package (CM plan section 8.2 step 1 requires the tool Accredited) |
| Lock rows | `tools/toolchain.lock.md` section 1 rows OpenSCAD and FreeCAD (headless); section 1.1 row "OpenSCAD + FreeCAD with tools/scad2step.py"; section 1.2 row `tools/scad2step.py`; section 1.4 findings 3 and 4; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 1a) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/scad2step.py` | git blob `d0277ec8d89967576869be95ee5d0300e1f6af51`, SHA-256 `004c0b3f82ad03165f633947eeb380c53ca7b77e3f56f1cc1d97bcd715dd2952`, 314 lines | committed in `86ff3b0` (see the note below); equal at `0743499` |
| `tools/tests/test_scad2step.py` | git blob `2e2fc392ccb5a0cba20e7f519527c2e58134f118`, SHA-256 `88570c4702f6af3f49ec1de5c576a53c49d630e4d9534b155d7ae8ebbc2fa616`, 22 tests | committed in `d9dd7bb` (smoke-shell case added to the `86ff3b0` version) |
| `tools/tests/fixtures/openscad/` | 11 tracked files, git tree `d9ab4c7d7ca8e5adf348b5074f581ef7e9b00b41`, digest `55ff76dfa11e5e873d4d165ffb6038f365705b850fa4c92e4bb9dfa002a9374a` (SHA-256 of the sorted `shasum -a 256` list, in the run 1 transcript) | `cube.scad` (2026-09-25, unchanged); `known-answers.json` (block `scad2step` added, `d9dd7bb`); `smoke-shell.scad`, `two-roots.scad`, `two-solids.scad`, `nonuniform-scale.scad`, `twist.scad`, `taller.scad` and the test doubles `fake/freecadcmd-silent`, `fake/freecadcmd-hang`, `fake/openscad-other-version` (mode 100755) |
| OpenSCAD | `OpenSCAD version 2021.01` (`/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD --version`, x86_64 under Rosetta) | lock section 1 |
| FreeCAD | `1.1.3` (`defaults read /Applications/FreeCAD.app/Contents/Info.plist CFBundleVersion`; inside FreeCAD mode `FreeCAD.Version()` gives `1.1.3`, check C1) | lock section 1 |
| Runtime | TV-001 interpreter (Python 3.13.5) for the driver and the test module, standard library only; the FreeCAD bundle's own Python for FreeCAD mode | TV-001; bundle |

**Install source:** OpenSCAD 2021.01 macOS bundle and FreeCAD 1.1.3 Homebrew cask (SI-032), lock section 7 (no installer checksum is recorded there for either; the bundle version strings are the substitute identity); the script from the repository (CM plan Table 4-1 row 28).

**Commit note.** The five WP-PDR-07 tools were staged on 2026-09-27 and committed in `86ff3b0` by a concurrent session whose commit message describes its own change (a CR-011 review) and carries no `Refs:` for them; the content is exactly what was staged. The provenance is recorded in the message of `c90df2d`. Every identity above is the blob, which is what this record validates.

## 2. Purposes covered

1. Convert an OpenSCAD source written in the ADR-008 restricted dialect to a CSG file with OpenSCAD 2021.01 at an absolute output path, and the CSG to a STEP file of exactly one valid solid through `freecadcmd` (the FreeCAD OpenSCAD workbench import with placeholders disabled, `removeSplitter`, the one-solid `Compound` unwrap of lock section 1.4 finding 4), printing the solid count, validity, face types and the shape, STEP and mesh volumes on one `SCAD2STEP KAT` line.
2. Refuse, with exit 1 and no STEP file left, a result with more than one top-level object (C2), a non-solid or invalid result (C3), more than one solid (C4), a BSpline face (C5), a STEP read-back that differs from the exported solid (C6), or a STEP volume more than 0.5 % from the OpenSCAD mesh volume (C7).
3. Refuse to run on an OpenSCAD other than `OpenSCAD version 2021.01` or a FreeCAD other than 1.1.3 (exit 4), when either is not installed at the locked path (exit 3), when `freecadcmd` returns without the `SCAD2STEP PASS` marker (exit 1, because `freecadcmd` exits 0 when a script raises), and after a time-out that kills only the process group the driver started (exit 124); usage errors exit 2.
4. Produce the same STEP content on every run: two conversions of the same source differ only in the time-stamp argument of `FILE_NAME`.

Not covered: `rotate_extrude`, `sphere`, `polyhedron`, `intersection`, `mirror` and uniform `scale` of the dialect have no known answer of their own (limitation 1); STEP schema options (AP214 or AP242) are FreeCAD's defaults and are not checked; drawings (`drawing.pdf`) are not produced by this tool.

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/openscad/` with `known-answers.json` (blocks `step_export` of 2026-09-25 and `scad2step`; every expected value derived by hand from the geometry before the run, the derivation written in the block's `description`). Module `tools/tests/test_scad2step.py`.

| Case (class) | Input | Known answer |
|---|---|---|
| Cube (`ConversionTests`) | `cube.scad`: 30 x 20 x 10 mm block less a 6 mm hole, `$fn = 64` | exit 0, marker `SCAD2STEP PASS wrote <step>`; root `Compound` unwrapped to 1 valid solid; 7 faces, 1 cylindrical, 0 BSpline; volume 5717.257 mm^3 (30 x 20 x 10 - pi 3^2 10) within 0.5 %; STEP volume equal to the shape; mesh volume 5717.711 mm^3 (64-sided hole: 6000 - 32 sin(2 pi/64) 9 x 10) within 0.01 mm^3; STEP bounding box 0..30, 0..20, 0..10 mm within 0.01 mm from the `VERTEX_POINT` coordinates (read by the test, not by FreeCAD); the CSG holds the three `must_contain` lines |
| CM plan form (`ConversionTests`) | `freecadcmd tools/scad2step.py` with `CWHT_CSG`, `CWHT_STL`, `CWHT_STEP` | the marker and the STEP file; without the environment the marker `SCAD2STEP FAIL usage: ...` and `freecadcmd` exit 0 (lock finding 4 reproduced) |
| Smoke shell (`SmokeShellTests`) | `smoke-shell.scad`: the research B2 half-shell (linear_extrude of offset rounded rectangles, pocket, four holes, four bosses) in one `union()` | exit 0; 1 valid solid; 31 faces (16 cylindrical, 15 planar), 0 BSpline; volume 24721.22 mm^3 within 0.05 mm^3 (hand sum in `known-answers.json`); mesh error at most 0.5 %; bounding box -55..55, -31..31, 0..18 mm |
| Version checks (`ConversionTests`, `DoubleTests`) | `CWHT_SCAD2STEP_EXPECT_FREECAD=1.1.4` (driver bundle check); the same with `CWHT_FREECADCMD` set to the real `freecadcmd` (FreeCAD mode C1); `CWHT_SCAD2STEP_EXPECT_OPENSCAD=OpenSCAD version 2021.02`; `fake/openscad-other-version` | exit 4 each; C1 prints `SCAD2STEP FAIL C1: FreeCAD is 1.1.3, expected 1.1.4` and leaves no STEP |
| Mesh volume reader (`MeshVolumeTests`) | hand-written binary box 30 x 20 x 10 (12 triangles), ASCII unit tetrahedron, truncated binary file | 6000.000 mm^3 and 12 facets; 1/6 and 4 facets; `ValueError` |
| Usage (`UsageTests`) | 8 malformed command lines | exit 2 each |

Seeded faults (class `SeededCsgTests` and `DoubleTests`):

| Seeded fault | Expected |
|---|---|
| `two-roots.scad`: two blocks with no enclosing union | exit 1, marker `SCAD2STEP FAIL C2: expected one top-level object, got 2`, no STEP |
| `two-solids.scad`: two disjoint blocks in one union | exit 1, marker beginning `SCAD2STEP FAIL C3: invalid or non-solid result (ShapeType Compound`, no STEP |
| `nonuniform-scale.scad`: an elliptical hole by `scale([1, 2, 1])` | exit 1, marker `SCAD2STEP FAIL C2: ...got 2` (FreeCAD leaves the unscaled cylinder as a second root, observed; finding 2), no STEP |
| `twist.scad`: a twisted `linear_extrude` | exit 1, marker beginning `SCAD2STEP FAIL C5: ` (4 BSpline faces), no STEP |
| `cube.csg` with the mesh of `taller.scad` (11 mm high, mesh volume 6289.482 mm^3 by hand) | exit 1, marker beginning `SCAD2STEP FAIL C7: `, the KAT line's mesh volume 6289.48 mm^3, no STEP |
| `CWHT_OPENSCAD=/nonexistent/OpenSCAD`; `CWHT_FREECADCMD=/nonexistent/freecadcmd` | exit 3 each, `TEST HOOK` line on stderr |
| `fake/freecadcmd-silent`: exits 0 with no marker | exit 1, `no SCAD2STEP marker`, no STEP |
| `fake/freecadcmd-hang` with `--timeout 3` | exit 124 after 3 to 20 s; no process of the double survives (`pgrep -f`) |

C4 (a CompSolid of more than one solid) and C6 (a read-back mismatch) have no seeded fault: no source in the dialect produces them through FreeCAD 1.1.3 (limitation 2).

**Run command** (the procedure, which also records identities and versions and runs part D):

```
bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-015 > docs/cm/tool-validation/evidence/scad2step-<date>-run<N>.log.txt
```

Its part C is `.venv/bin/python -m unittest discover -v -s tools/tests -p test_scad2step.py` from the repository root. Part D converts `cube.scad` twice, 2 s apart, and compares the STEP files after replacing the `FILE_NAME` time stamp with `perl` (independent of the tool).

**Pass criteria:** part C exits 0 with 22 tests run and passed and none skipped (`ConversionTests` 9, `DoubleTests` 5, `MeshVolumeTests` 3, `ReproducibilityTests` 1, `SeededCsgTests` 2, `SmokeShellTests` 1, `UsageTests` 1); part D prints `RESULT normalized STEP identical`; part A shows every file "unchanged from HEAD" and 0 untracked or modified fixture files.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 12:51 | `0743499` (tool `d0277ec8`, test module `2e2fc392`, fixture tree `d9ab4c7d`, every identity "unchanged from HEAD") | **Pass.** 22 tests, 22 passed, 0 skipped (31.9 s); part D: raw SHA-256 `32d33dc7...eacc2` and `49b4bfa6...defe4` (time stamps 12:52:19 and 12:52:22), normalized SHA-256 `f2b3afbf...6c6362` in both, `RESULT normalized STEP identical`; KAT line of the cube `root=Compound solids=1 valid=True faces=7 cylinders=1 bspline=0 volume=5717.257 step_volume=5717.257 stl_volume=5717.711 stl_error_pct=0.0079 freecad=1.1.3`. Transcript `evidence/scad2step-2026-09-27-run1.log.txt` |

Development observations (not a validation run, 2026-09-27 12:24 to 12:31 on the working tree): the cube and the smoke shell gave the KAT values of section 3 on the first run (smoke shell volume 24721.221 mm^3 against the hand value 24721.22), and each seeded file failed at the check stated.

### 4.1 Findings of this validation

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | The research B2 half-shell source has two top-level objects (the shell and the boss loop), so the CM plan step 3 flow with C2 rejects it as written. | development run; `smoke-shell.scad` header | The fixture wraps it in `union()`. The enclosure model (WP-PDR-39) keeps one top-level object; this is a modelling rule for `hardware/enclosure/*.scad`, reported to the ME designer as a cross item |
| 2 | A non-uniform `scale` makes FreeCAD 1.1.3 keep the unscaled primitive as a second root besides the BSpline `Matrix_Deformation`, so the run stops at C2, not C5. | `nonuniform-scale.scad` case; development debug listing of the roots | The source is refused either way; C5 is exercised by `twist.scad`, the other dialect breach that yields BSpline faces with one root |
| 3 | The 2026-09-25 lock finding 4 (`freecadcmd` exits 0 when the script raises) is reproduced by the CM plan form without environment. | `ConversionTests.test_freecad_mode_missing_environment` | The driver is the entry point for release packages: it turns the marker into the exit status |

## 5. Reproducibility

Class A (CM plan section 9.2 step 1). Run 1 part D: two conversions of `cube.scad` give STEP files whose SHA-256 differ (`32d33dc757332c73e61b6d907f8a9be023a4ac36e494c01d525255743a8eacc2` and `49b4bfa6524e8ab1c863bdc85db188d3c40eaf7495215fb0ee91fff085ddefe4`) and whose content after the `FILE_NAME` time stamp is replaced is identical (`f2b3afbfa36fae7343e06d227a1acff88b30506245b945648597e796b96c6362` in both runs). `ReproducibilityTests` asserts the same inside the module. The normalization used is the STEP row of the CM plan section 8.2 table, applied by `perl` here and by a regular expression in the test; `tools/normalize_fab.py` (TV-016) applies the same rule to release packages.

## 6. Limitations

1. The known answers cover `cube`, `cylinder`, `difference`, `union`, `translate`, `linear_extrude` and `offset` (planes and cylinders). `rotate_extrude`, `sphere`, `polyhedron`, `intersection`, `mirror` and uniform `scale` are in the ADR-008 dialect without a known answer; a model that uses them is converted and checked by C2 to C7 but its face types and volume have not been validated against a hand value. The enclosure model's own analysis record confirms its volume and bounding box.
2. C4 and C6 are checked in code but have no seeded fault (section 3).
3. C7 compares with the OpenSCAD mesh of the same source: an error common to OpenSCAD and FreeCAD (a wrong source) passes. The bounding box against the ME requirement is the reviewer's CM plan section 8.2 step 4 check.
4. The OpenSCAD and FreeCAD versions are checked by their version strings (and FreeCAD also inside FreeCAD mode); the bundles are not hashed. A reinstall of the same version is caught only through the section 7 triggers and the lock re-observation.
5. The test hooks `CWHT_OPENSCAD`, `CWHT_FREECADCMD`, `CWHT_SCAD2STEP_EXPECT_*` are for the known-answer test; runs for the record are made without them (each prints `TEST HOOK`).
6. macOS only (locked application paths, `defaults`).
7. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).

## 7. Re-validation triggers

- Any change of `tools/scad2step.py`, `tools/tests/test_scad2step.py` or `tools/tests/fixtures/openscad/` (CM plan section 9.2 step 4).
- A version change of OpenSCAD or FreeCAD, a reinstall of either bundle, a macOS major version change.
- A change of the TV-001 interpreter.
- Class A expiry: re-run section 3 at each new baseline and append the result (CM plan section 9.2 step 4).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (one record for TV-014 to TV-019, one section per tool; PDR work plan WP-PDR-07), with `peer-review-checklist-tool-validation.md` (CR-012) and the code checklist for the script.

## 9. Accreditation (owner)

Proposed scope statement **ACC-SCAD2STEP-001**: "Accredited for purposes 1 to 4 for `tools/scad2step.py` at git blob `d0277ec8d89967576869be95ee5d0300e1f6af51`, run through its driver (`.venv/bin/python tools/scad2step.py`) without test hooks, with OpenSCAD 2021.01 and FreeCAD 1.1.3 at their locked paths, for sources in the ADR-008 restricted dialect with one top-level object, within the limitations of section 6."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after the section 8 review is APPROVED) | | |
