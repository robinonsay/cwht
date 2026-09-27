# TV-016: kicad-cli 10.0.6 with tools/normalize_fab.py (git blob f3eaac39)

| Field | Value |
|---|---|
| Record | TV-016 |
| Status | **Validated** 2026-09-27 (known-answer run 1 at commit `c90df2d`: 38 tests passed, 0 skipped). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | A for the kicad-cli exports (Gerber, drill, CPL, BOM and STEP enter the hardware release package), B for kicad-cli ERC and DRC (Inspection evidence) and for `tools/normalize_fab.py` (the `SHA256SUMS.normalized` comparison basis of PCA-01) (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8) through CM plan section 9; CM plan section 8.2 step 2 (the permitted export commands F3, F6, F7) and the section 8.2 normalization table |
| Due | PDR (CM plan section 13 PDR row). First cited use: the ERC and DRC of the preliminary schematic and floorplan (WP-PDR-37); the release use is the CDR procurement package (CM plan section 8.2 step 1 requires `tools/normalize_fab.py` Accredited) |
| Lock rows | `tools/toolchain.lock.md` section 1 row kicad-cli; section 1.1 rows kicad-cli and `tools/normalize_fab.py`; section 1.2 row `tools/normalize_fab.py`; section 1.4 finding 5; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 1a) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/normalize_fab.py` | git blob `f3eaac395b279bceb32fb3ba850632acfe426782`, SHA-256 `f22d843c4c18ab0d4e1242539e3e5cf3d93cb34343aa114fee93b18324ab5f91`, 259 lines | committed in `86ff3b0` (commit note of TV-015 section 1); equal at `c90df2d` |
| `tools/tests/test_normalize_fab.py` | git blob `707a22d594671b9125fd5f8134c57d290121e413`, SHA-256 `4bb1169f1ada082f269534e9165fd1b3fd350c4037fa91f2b0f96a7de18855ec`, 24 tests | committed in `86ff3b0` |
| `tools/tests/test_kicad_cli.py` | git blob `780117af30155408b4c4f56574d72cfd261c0b88`, SHA-256 `377f57a555d2b255728b1b47998ddb8c70bbc8ac844311c2847d105cda3b8473`, 14 tests | committed in `86ff3b0` |
| `tools/tests/fixtures/kicad/` | 15 tracked files, git tree `03063f2a45abd42f532e4b035cfac71fe578de90`, digest `0d9fca9db9e605542dcbe00ea2be37e7db9584fd3c7183e6cc87e9fd41888b1c` (SHA-256 of the sorted `shasum -a 256` list, in the run 1 transcript) | the 2026-09-25 fixture (boards, schematics, library tables, generators, `expected/clean-cpl.csv`, `expected/clean-bom.csv`) unchanged except `known-answers.json` block `normalized_exports` (activated); new `expected/clean-SHA256SUMS.normalized` and its generator `make_expected_normalized.sh` |
| kicad-cli | `10.0.6` (`/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli version`) | lock section 1 |
| Runtime | TV-001 interpreter (Python 3.13.5), standard library only; `perl` v5.40.2 (macOS) and `grep` only in the expected-list generator | TV-001; OS |

**Install source:** KiCad 10.0.6 macOS bundle (lock section 7; no installer checksum recorded, the version string is the substitute identity); the script from the repository (CM plan Table 4-1 row 28).

## 2. Purposes covered

1. kicad-cli 10.0.6 `sch erc` and `pcb drc` (JSON, all severities, `--exit-code-violations`) report exactly the violations present: none and exit 0 on a clean schematic or board, the seeded unconnected pin and the seeded clearance violation (and only those) with exit 5.
2. kicad-cli 10.0.6 runs the CM plan section 8.2 step 2 export commands F3 (Gerber, X2 off, with the 11-layer list), F6 (Excellon drill with map and report) and F7 (CPL), plus `sch export bom` and `pcb export step --board-only`, and their outputs carry the board's content: the Gerber set of the board's layers and the job file, the drill hit counts and diameters in the drill files and the drill report, the CPL and BOM line for line, the STEP bounding box within 0.01 mm.
3. `tools/normalize_fab.py` removes exactly the time stamps of the CM plan section 8.2 table (Gerber, Excellon, Gerber job, drill report, STEP, PDF; CSV unchanged; zip members one by one, the zip itself not listed; other types hashed as they are, reported "raw") and prints, writes (`--sums`) or checks (`--check`) the `<sha256>  <name>` list; two exports of the same board taken at different times give identical lists, and a one-byte change outside the date lines changes the file's hash and fails `--check` with exit 1 naming the file.

Not covered: `tools/kicad_export/pcbway_package.sh` (TV due CDR); the file-count and "Invalid layer name" checks of the CM plan section 8.2 step 2 (they belong to that script); kicad-cli renders (SVG, PDF plots of schematics) for review packages; ERC and DRC rule sets other than the KiCad defaults (limitation 2).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/kicad/` with `known-answers.json`: the 2026-09-25 blocks `erc`, `drc`, `drill`, `cpl`, `bom`, `step` (values derived by hand from the fixture geometry before the first run, provenance in its `description`) and the block `normalized_exports` activated for this record. The stored list `expected/clean-SHA256SUMS.normalized` (18 files) was produced on 2026-09-27 by `make_expected_normalized.sh`: one kicad-cli export of `clean.kicad_pcb`, normalized by `grep -v` and `perl` written from the CM plan table, independently of the tool, then `shasum -a 256`.

| Module and class | Known answer |
|---|---|
| `test_normalize_fab.py` `RuleTests` (10) | one hand-written input per table row with its hand-written normalized form: Gerber (3 date lines removed, also with CRLF), Excellon (2), Gerber job (1 member), drill report (1), STEP (1, also with the header split over lines and a doubled quote), PDF (2 dates zeroed, same length), CSV unchanged, another type "raw" |
| `test_normalize_fab.py` `SeededFaultTests` (4) | one byte changed in a copper coordinate: hash differs; only a time stamp changed: hash equal; a date-like comment outside the table survives; one byte changed in a STEP body: differs |
| `test_normalize_fab.py` `CliTests` (10) | sorted `shasum`-format listing without `SHA256SUMS`, `SHA256SUMS.normalized` and hidden files; `--sums` then `--check` exit 0 ("check PASS: 6 listed"); `--check` exit 1 with `CHANGED`, `ADDED`, `MISSING`; `--check` exit 0 after a time-stamp-only change; zip members listed as `<zip>!<member>`, the zip itself not; `--write` holds the normalized bytes; `--root` names; exit 2 for no path, an unknown option, a missing input, `--sums` with `--check`, an unreadable stored list, a malformed stored line, a broken zip and an empty directory |
| `test_kicad_cli.py` `VersionTests` (1) | `kicad-cli version` prints `10.0.6` |
| `test_kicad_cli.py` `ErcDrcTests` (4) | ERC clean: exit 0, no violation; ERC seeded: exit 5, exactly `["pin_not_connected", "error", "Symbol R1 Pin 2 [Passive, Line]"]`; DRC clean: exit 0, none, 0 unconnected; DRC seeded: exit 5, exactly the 0.1 mm clearance violation against 0.2 mm on R1 pad 2 |
| `test_kicad_cli.py` `ExportTests` (5) | the 9 Gerbers of the 2-layer board plus `clean-job.gbrjob` (In1.Cu and In2.Cu are skipped without a message); PTH 1 hit of 0.7 mm and NPTH 1 hit of 3.2 mm in the drill files and "Total plated holes count 1", "Total unplated holes count 1" in the report; CPL and BOM equal the stored CSVs line for line; STEP box 0..30, 0..20, 0..1.51 mm within 0.01 mm |
| `test_kicad_cli.py` `NormalizedExportTests` (4) | two complete exports at least 1.1 s apart: the same 18 file names, 16 raw files differ (all but the two CSVs); the two normalized lists are equal and hold 18 entries; each export passes `--check` against the stored list; a one-byte change of the first coordinate digit of `clean-F_Cu.gbr` makes `--check` exit 1 with exactly one `CHANGED clean-F_Cu.gbr` |

**Run command:** `bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-016 > docs/cm/tool-validation/evidence/kicad-normalize-fab-<date>-run<N>.log.txt`; its part C runs `.venv/bin/python -m unittest discover -v -s tools/tests -p test_normalize_fab.py` and then `-p test_kicad_cli.py` from the repository root.

**Pass criteria:** both modules exit 0 with 24 and 14 tests run and passed and none skipped (a skip of a `test_kicad_cli.py` class means kicad-cli was absent and the case was not run); part A shows every file "unchanged from HEAD" and 0 untracked or modified fixture files.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 12:49 | `c90df2d` (tool `f3eaac39`, modules `707a22d5` and `780117af`, fixture tree `03063f2a`, every identity "unchanged from HEAD") | **Pass.** `test_normalize_fab.py` 24 of 24 in 0.55 s; `test_kicad_cli.py` 14 of 14 in 6.2 s; 0 skipped. Transcript `evidence/kicad-normalize-fab-2026-09-27-run1.log.txt` |

Development observations (not a validation run, 2026-09-27 12:18 to 12:21): two full exports about ten minutes apart differed raw in 16 of 18 files and were equal after normalization; the tool's list equalled the stored independent list on the earlier export (`check PASS: 18 listed`).

### 4.1 Findings of this validation

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | On a 2-layer board the F3 layer list is accepted: kicad-cli skips `In1.Cu` and `In2.Cu` without a message and exits 0; a misspelt layer prints `Invalid layer name 'F.Cuu'` and is also skipped with exit 0. | development observation; `known-answers.json` `gerber_note` | The CM plan section 8.2 step 2 checks (fail on "Invalid layer name", file counts per F12) must be in `tools/kicad_export/pcbway_package.sh` (TV due CDR); kicad-cli's exit status does not show a skipped layer |
| 2 | kicad-cli ERC and DRC JSON reports carry a `date` member, which the CM plan section 8.2 table does not list; `erc-report.json` and `drc-report.json` are package files that `SHA256SUMS.normalized` covers ("every generated file except the zip"). | `sch erc` and `pcb drc` on the clean fixture, 2026-09-27 12:54: each JSON holds `"date": "2026-09-27T12:54:55"`; CM plan section 8.2 step 2 package list against the normalization table | `tools/normalize_fab.py` applies exactly the table ("nothing else"), so these two files hash raw and differ between exports. A CM plan change (a table row for JSON reports) is proposed to the lead SE as a cross item; until then the PCA-01 comparison excludes the two reports by name |

## 5. Reproducibility

Class A for the exports (CM plan section 9.2 step 1): `NormalizedExportTests` makes two complete exports at least 1.1 s apart; the normalized hashes of all 18 files are identical and equal to the stored list made from a third export (2026-09-27 12:20).

## 6. Limitations

1. The fixture board is 2-layer with three footprints; inner layers, zones, vias, slots and oval holes are not in the known answer. A 4-layer board's Gerber set is checked by the package script's file count (CM plan F12, TV due CDR).
2. ERC and DRC run with the KiCad default severities through the project-local library tables; a project rule file (the DRC rule file of WP-PDR-37) needs its own seeded case before its results are cited.
3. PDF normalization zeroes only `/CreationDate` and `/ModDate`; a PDF that carries XMP metadata or a compressed date elsewhere would not normalize (the drill maps of kicad-cli 10.0.6 carry neither, verified by the equal hashes).
4. The rules match kicad-cli 10.0.6 output; a KiCad version change can add date fields (section 7).
5. JSON reports are hashed raw (finding 2).
6. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).

## 7. Re-validation triggers

- Any change of `tools/normalize_fab.py`, `tools/tests/test_normalize_fab.py`, `tools/tests/test_kicad_cli.py` or `tools/tests/fixtures/kicad/` (CM plan section 9.2 step 4).
- A kicad-cli version change or a KiCad reinstall; a macOS major version change.
- A change of the CM plan section 8.2 table or export commands.
- A change of the TV-001 interpreter.
- Class A expiry of the exports: re-run section 3 at each new baseline.
- A defect found in the tool or in kicad-cli (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (one record for TV-014 to TV-019; PDR work plan WP-PDR-07).

## 9. Accreditation (owner)

Proposed scope statements:

- **ACC-KICAD-001**: "Accredited for purposes 1 and 2 for kicad-cli 10.0.6 at `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`, for the ERC and DRC commands and the CM plan section 8.2 step 2 export commands as written in section 2, with the KiCad default severities, within the limitations of section 6."
- **ACC-NORMFAB-001**: "Accredited for purpose 3 for `tools/normalize_fab.py` at git blob `f3eaac395b279bceb32fb3ba850632acfe426782` with the TV-001 interpreter, for kicad-cli 10.0.6 outputs, within the limitations of section 6."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after the section 8 review is APPROVED) | | |
