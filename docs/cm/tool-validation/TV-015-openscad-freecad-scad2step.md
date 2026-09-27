# TV-015: OpenSCAD 2021.01 and FreeCAD 1.1.3 through tools/scad2step.py (git blob d0277ec8)

| Field | Value |
|---|---|
| Record | TV-015 |
| Status | **Validated** 2026-09-27 (known-answer run 2 at commit `989d257`, 28 tests passed, 0 skipped, with the C4 and C6 seeded faults added for INSP-088 finding-1; run 1 at `0743499`, 22 tests; reproducibility passed in both). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | A, product-generating (CM plan section 9.1: OpenSCAD 2021.01 CSG and FreeCAD 1.1.3 `freecadcmd` with `tools/scad2step.py` STEP, the files of the enclosure release package) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8) through CM plan section 9; CM plan section 8.2 step 3; ADR-008 (restricted OpenSCAD dialect, STEP acceptance checks) |
| Due | PDR (CM plan section 13 PDR row). First cited use: the enclosure concept model of WP-PDR-39 (PDR work plan); the release use is the CDR procurement package (CM plan section 8.2 step 1 requires the tool Accredited) |
| Lock rows | `tools/toolchain.lock.md` section 1 rows OpenSCAD and FreeCAD (headless); section 1.1 row "OpenSCAD + FreeCAD with tools/scad2step.py"; section 1.2 row `tools/scad2step.py`; section 1.4 findings 3 and 4; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 1a) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/scad2step.py` | git blob `d0277ec8d89967576869be95ee5d0300e1f6af51`, SHA-256 `004c0b3f82ad03165f633947eeb380c53ca7b77e3f56f1cc1d97bcd715dd2952`, 314 lines | committed in `86ff3b0` (see the note below); equal at `0743499` |
| `tools/tests/test_scad2step.py` | git blob `bd38fe2b5cf7cf75aac65d6f19d2c96633b56119`, SHA-256 `78c7480b528e4d9645fedb9e1d53467856f32b39b840bb6bfd6846da60b1e316`, 28 tests | committed in `989d257` (class `ApiDoubleTests` added to the `d9dd7bb` version, blob `2e2fc392`, 22 tests, which run 1 tested) |
| `tools/tests/fixtures/openscad/` | 15 tracked files, git tree `35e89b482be8449c31385e3712aa42268477955a`, digest `72b0ab2d9f590ee625441380371420faf7b9d30f3e714c2adc80cce37e36d58e` (SHA-256 of the sorted `shasum -a 256` list, in the run 2 transcript; run 1: 11 files, tree `d9ab4c7d`, digest `55ff76df...`) | `cube.scad` (2026-09-25, unchanged); `known-answers.json` (block `scad2step` added, `d9dd7bb`; block `scad2step.api_double` added, `989d257`); `smoke-shell.scad`, `two-roots.scad`, `two-solids.scad`, `nonuniform-scale.scad`, `twist.scad`, `taller.scad`; the test doubles `fake/freecadcmd-silent`, `fake/freecadcmd-hang`, `fake/openscad-other-version` and `fake/freecadcmd-api-double` (mode 100755) and the stand-in modules `fake/freecad_api/FreeCAD.py`, `Part.py`, `importCSG.py` (`989d257`) |
| OpenSCAD | `OpenSCAD version 2021.01` (`/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD --version`, x86_64 under Rosetta) | lock section 1 |
| FreeCAD | `1.1.3` (`defaults read /Applications/FreeCAD.app/Contents/Info.plist CFBundleVersion`; inside FreeCAD mode `FreeCAD.Version()` gives `1.1.3`, check C1) | lock section 1 |
| Runtime | TV-001 interpreter (Python 3.13.5) for the driver and the test module, standard library only; the FreeCAD bundle's own Python for FreeCAD mode | TV-001; bundle |

**Install source:** OpenSCAD 2021.01 macOS bundle and FreeCAD 1.1.3 Homebrew cask (SI-032), lock section 7 (no installer checksum is recorded there for either; the bundle version strings are the substitute identity); the script from the repository (CM plan Table 4-1 row 28).

**Commit note.** The five WP-PDR-07 tools were staged on 2026-09-27 and committed in `86ff3b0` by a concurrent session whose commit message describes its own change (a CR-011 review) and carries no `Refs:` for them; the content is exactly what was staged. The provenance is recorded in the message of `c90df2d`. Every identity above is the blob, which is what this record validates.

## 2. Purposes covered

1. Convert an OpenSCAD source written in the ADR-008 restricted dialect to a CSG file with OpenSCAD 2021.01 at an absolute output path, and the CSG to a STEP file of exactly one valid solid through `freecadcmd` (the FreeCAD OpenSCAD workbench import with placeholders disabled, `removeSplitter`, the one-solid `Compound` unwrap of lock section 1.4 finding 4), printing the solid count, validity, face types and the shape, STEP and mesh volumes on one `SCAD2STEP KAT` line.
2. Refuse, with exit 1 and no STEP file left, a result with more than one top-level object (C2), a non-solid or invalid result (C3), more than one solid (C4), a BSpline face (C5), a STEP read-back that differs from the exported solid (C6: no file written, not exactly one valid solid, or a volume more than 1e-6 relative from the exported shape), or a STEP volume more than 0.5 % from the OpenSCAD mesh volume (C7). C2, C3, C5 and C7 are validated with FreeCAD 1.1.3; C4 and C6 are validated against the FreeCAD API test double, which runs the tool's own check code on stand-in shapes (limitation 2).
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

**C4 and C6 through the FreeCAD API test double** (class `ApiDoubleTests`; `known-answers.json` block `scad2step.api_double`; INSP-088 finding-1). No source in the dialect makes FreeCAD 1.1.3 return a CompSolid of more than one solid or a STEP read-back that differs from the exported solid, so these branches are reached with `fake/freecadcmd-api-double`. The driver runs it as `freecadcmd` (hook `CWHT_FREECADCMD`); it executes `tools/scad2step.py` under the test interpreter with the stand-in `FreeCAD`, `Part` and `importCSG` modules of `fake/freecad_api/`, so FreeCAD mode runs its own C1 to C7 code on the shape named by `CWHT_FAKE_FREECAD_CASE`. The exported shape is 6000 mm^3 in every case, the hand volume of the 30 x 20 x 10 mm box mesh the test writes. The C6 tolerance is 1e-6 x 6000 = 0.006 mm^3. Each expected marker is the format string of the tool's raise statement, filled in by hand. The double logs each export to `CWHT_FAKE_FREECAD_LOG`, so "no STEP" after an export shows a removal.

| Case | Stand-in shape | Expected |
|---|---|---|
| `control` | one valid Solid, 6 planar faces; STEP written; read back one valid solid of 6000.003 mm^3 (5e-7 relative) | exit 0, marker `SCAD2STEP PASS wrote <step>`, KAT `root=Solid solids=1 valid=True faces=6 cylinders=0 bspline=0 volume=6000.000 step_volume=6000.003 stl_volume=6000.000 stl_facets=12 freecad=1.1.3`, STEP present (shows that the double passes when no fault is seeded) |
| `c4-compsolid` | a valid CompSolid of 2 solids; a stale STEP placed at `--step` before the run | exit 1, marker `SCAD2STEP FAIL C4: STEP must hold exactly one solid, got 2`, no STEP (the stale file removed), no export |
| `c6-no-file` | as control; the export writes no file | exit 1, marker `SCAD2STEP FAIL C6: FreeCAD wrote no STEP file`, no STEP |
| `c6-two-solids` | as control; the read-back holds 2 solids | exit 1, marker `SCAD2STEP FAIL C6: STEP read back holds 2 solid(s), valid True`, export logged, no STEP |
| `c6-invalid` | as control; the read-back is one solid, not valid | exit 1, marker `SCAD2STEP FAIL C6: STEP read back holds 1 solid(s), valid False`, export logged, no STEP |
| `c6-volume` | as control; the read-back is 6000.012 mm^3 (2e-6 relative) | exit 1, marker `SCAD2STEP FAIL C6: STEP volume 6000.012000 differs from the shape volume 6000.000000`, export logged, no STEP |

Author mutation check (2026-09-27, scratch copies of the tool, not a validation run): removing the C4 check, each of the three C6 checks, or the `isValid()` operand of the second C6 check, and changing `REREAD_TOLERANCE` to 1e-5 or 1e-7, each made at least one `ApiDoubleTests` case fail.

**Run command** (the procedure, which also records identities and versions and runs part D):

```
bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-015 > docs/cm/tool-validation/evidence/scad2step-<date>-run<N>.log.txt
```

Its part C is `.venv/bin/python -m unittest discover -v -s tools/tests -p test_scad2step.py` from the repository root. Part D converts `cube.scad` twice, 2 s apart, and compares the STEP files after replacing the `FILE_NAME` time stamp with `perl` (independent of the tool).

**Pass criteria:** part C exits 0 with 28 tests run and passed and none skipped (`ApiDoubleTests` 6, `ConversionTests` 9, `DoubleTests` 5, `MeshVolumeTests` 3, `ReproducibilityTests` 1, `SeededCsgTests` 2, `SmokeShellTests` 1, `UsageTests` 1); part D prints `RESULT normalized STEP identical`; part A shows every file "unchanged from HEAD" and 0 untracked or modified fixture files.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 12:51 | `0743499` (tool `d0277ec8`, test module `2e2fc392`, fixture tree `d9ab4c7d`, every identity "unchanged from HEAD") | **Pass.** 22 tests, 22 passed, 0 skipped (31.9 s); part D: raw SHA-256 `32d33dc7...eacc2` and `49b4bfa6...defe4` (time stamps 12:52:19 and 12:52:22), normalized SHA-256 `f2b3afbf...6c6362` in both, `RESULT normalized STEP identical`; KAT line of the cube `root=Compound solids=1 valid=True faces=7 cylinders=1 bspline=0 volume=5717.257 step_volume=5717.257 stl_volume=5717.711 stl_error_pct=0.0079 freecad=1.1.3`. Transcript `evidence/scad2step-2026-09-27-run1.log.txt` |
| 2 | 2026-09-27 13:48 | `989d257` (tool `d0277ec8`, unchanged; test module `bd38fe2b`; fixture tree `35e89b48`, 15 files, digest `72b0ab2d...`; every identity "unchanged from HEAD", 0 untracked or modified fixture files) | **Pass.** 28 tests, 28 passed, 0 skipped (32.3 s), among them the six `ApiDoubleTests` cases (C4, C6 and the control); OpenSCAD `OpenSCAD version 2021.01`, FreeCAD bundle `1.1.3`; part D: raw SHA-256 `ecff2249...52473` and `77f74ce1...24f19` (time stamps 13:48:56 and 13:48:59), normalized SHA-256 `f2b3afbf...6c6362` in both, equal to run 1, `RESULT normalized STEP identical`; cube KAT line equal to run 1. Run for INSP-088 finding-1. Transcript `evidence/scad2step-2026-09-27-run2.log.txt` |

Development observations (not a validation run, 2026-09-27 12:24 to 12:31 on the working tree): the cube and the smoke shell gave the KAT values of section 3 on the first run (smoke shell volume 24721.221 mm^3 against the hand value 24721.22), and each seeded file failed at the check stated.

### 4.1 Findings of this validation

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | The research B2 half-shell source has two top-level objects (the shell and the boss loop), so the CM plan step 3 flow with C2 rejects it as written. | development run; `smoke-shell.scad` header | The fixture wraps it in `union()`. The enclosure model (WP-PDR-39) keeps one top-level object; this is a modelling rule for `hardware/enclosure/*.scad`, reported to the ME designer as a cross item |
| 2 | A non-uniform `scale` makes FreeCAD 1.1.3 keep the unscaled primitive as a second root besides the BSpline `Matrix_Deformation`, so the run stops at C2, not C5. | `nonuniform-scale.scad` case; development debug listing of the roots | The source is refused either way; C5 is exercised by `twist.scad`, the other dialect breach that yields BSpline faces with one root |
| 3 | The 2026-09-25 lock finding 4 (`freecadcmd` exits 0 when the script raises) is reproduced by the CM plan form without environment. | `ConversionTests.test_freecad_mode_missing_environment` | The driver is the entry point for release packages: it turns the marker into the exit status |

## 5. Reproducibility

Class A (CM plan section 9.2 step 1). Run 2 part D gave the same normalized SHA-256 as run 1 (section 4). Run 1 part D: two conversions of `cube.scad` give STEP files whose SHA-256 differ (`32d33dc757332c73e61b6d907f8a9be023a4ac36e494c01d525255743a8eacc2` and `49b4bfa6524e8ab1c863bdc85db188d3c40eaf7495215fb0ee91fff085ddefe4`) and whose content after the `FILE_NAME` time stamp is replaced is identical (`f2b3afbfa36fae7343e06d227a1acff88b30506245b945648597e796b96c6362` in both runs). `ReproducibilityTests` asserts the same inside the module. The normalization used is the STEP row of the CM plan section 8.2 table, applied by `perl` here and by a regular expression in the test; `tools/normalize_fab.py` (TV-016) applies the same rule to release packages.

## 6. Limitations

1. The known answers cover `cube`, `cylinder`, `difference`, `union`, `translate`, `linear_extrude` and `offset` (planes and cylinders). `rotate_extrude`, `sphere`, `polyhedron`, `intersection`, `mirror` and uniform `scale` are in the ADR-008 dialect without a known answer; a model that uses them is converted and checked by C2 to C7 but its face types and volume have not been validated against a hand value. The enclosure model's own analysis record confirms its volume and bounding box.
2. C4 and C6 are validated against the FreeCAD API test double only (section 3, `ApiDoubleTests`): the known answer shows that the tool's own check code refuses a CompSolid of several solids and each kind of differing read-back with exit 1 and no STEP file left. It does not show that FreeCAD 1.1.3 can produce such a result, or that the stand-in reproduces how FreeCAD reports one; no source in the dialect made FreeCAD 1.1.3 produce either. The stand-in implements only the FreeCAD attributes the tool uses, so a later tool change that uses another attribute fails the control case, and a change of those attributes in FreeCAD is caught by the real-FreeCAD cases, not by the double.
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

Proposed scope statement **ACC-SCAD2STEP-001**: "Accredited for purposes 1 to 4 for `tools/scad2step.py` at git blob `d0277ec8d89967576869be95ee5d0300e1f6af51`, run through its driver (`.venv/bin/python tools/scad2step.py`) without test hooks, with OpenSCAD 2021.01 and FreeCAD 1.1.3 at their locked paths, for sources in the ADR-008 restricted dialect with one top-level object, within the limitations of section 6. For purpose 2, the C2, C3, C5 and C7 refusals are validated with FreeCAD 1.1.3; the C4 and C6 refusals are validated as check logic against the FreeCAD API test double only (limitation 2)."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after the section 8 review is APPROVED) | | |
