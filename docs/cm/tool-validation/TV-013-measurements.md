# TV-013: tools/measurements.py (git blob abe25acb, working tree on 400e59d)

| Field | Value |
|---|---|
| Record | TV-013 |
| Status | **Validated** (2026-09-26) on the working-tree file identified in section 1, not yet committed. Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: gate G2, G3 and G6 steps; MSR-13, MSR-14, MSR-18, MSR-19; the cross-record rules of `docs/plan/measurements.json`) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; the measurement tool of 07 sections 8.4 and 11 (SWE-090, SWE-093, SWE-186) |
| Due | PDR (CM plan section 13 PDR row); filed at SRR because gate steps G2 and G3 of TC-SW-TOOL-001-r2 (SRR package item R3, entrance row 20) use it before PDR (CM plan section 9.1) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/measurements.py`; section 1.2 |
| Author | Claude, tool maintainer (SRR package item R3) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `400e59d` |
|---|---|---|---|
| `tools/measurements.py` | `abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a` | `46f0cf185ea0f941d2cbe3f65cf0c02788d65cee53ddd626e0d7ceb1837701bc` | untracked (new) |
| `tools/tests/test_measurements.py` | `7e7ba2bbdb3569ba42924b6d974bcdb70f69f58b` | `ce1ee1b9edefc3daccb3f90a0fd8f96827778809038f324cacc7b6439a38048a` | untracked |
| `tools/tests/fixtures/measurements/` (`linkmap/`, `junit/`, `lcov/`, `records/`; `valid.json` and `invalid.json` belong to the schema test of `test_tools.py`) | 13 files, tree digest `250e0e1e86fba48494ded9377b21e9d1efad5d8b193fd5582ec59be1dbbe0c23` | | 11 untracked, 2 equal to `400e59d` |

**Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 interpreter, standard library only; `git` (TV-009) for `--check-records`.

## 2. Purposes covered

1. `--link-map`: flash and RAM use from an lld link map and the MEMORY block of the rustos linker script (highest section end in each region, LMA for FLASH, VMA for RAM, less the origin), failing above the TPM-010 and TPM-011 red lines (70 and 75 percent used); print MSR-18 and MSR-19 with their 07 section 11.2 assessment.
2. `--diff-runs`: compare the (classname, name, outcome) sets of two JUnit files; pass only when identical, non-empty and all passed (SWE-186, gate G3).
3. `--coverage`: per-crate line, function and branch totals from lcov (MSR-13), the totals of the llvm-cov JSON export (MSR-14), the emulation report; an optional input not produced is reported NOT PRODUCED.
4. `--check-records`: the 07 section 11.1 rules JSON Schema cannot express: catalog ids, append order of dates, `updated`, `supersedes` resolution, append-only against a revision, evidence hashes at the first commit containing each record (reported, never skipped), and the re-derivation of MSR-18 and MSR-19 from a cited link map.
5. `--analyze`: the current record of each (id, scope) after supersedes resolution, with the count per assessment (07 section 11.3, without plots).
6. Exit 0 pass, 1 on a gate criterion or record rule failure, 2 on a usage error or an unreadable required input. The tool never writes `docs/plan/measurements.json` or `docs/plan/tpm.json`.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/measurements/`: `linkmap/cwht-app.map` (byte copy of `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.map`, SHA-256 `e9ba4361...ee1d1a`) with `linkmap/link.ld` (rustos `firmware/pico2/link.ld` at the locked commit `c54d35a`); known answer FLASH 1608 B and RAM 8200 B, the values the SRR seed records MSR-18 and MSR-19 transcribed from the TC-SW-TOOL-001-r1 gate log, an independent source. `linkmap/over-red-line.map` with `small.ld` (1 KiB regions): hand-computed FLASH 0x310 = 784 B (76.56 percent, above the red line) and RAM 0x100 = 256 B (25 percent). `junit/`: identical runs, a seeded failure, an empty run. `lcov/`: hand-counted per-crate totals and an llvm-cov export. `records/records.json`: five records with a re-key by `supersedes` and a Not yet measured record retired by the first Measured one.

**Run command** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_measurements.py
```

**Pass criteria:** all 16 tests pass, none skipped: `LinkMapTests` 5 (1608 and 8200 B and the MSR values 0.04 and 1.54 percent; the red-line FAIL and PASS lines; exit 0 on the FW-B0 map; the assessment boundaries; missing map and empty map), `DiffRunsTests` 3, `CoverageTests` 2 (the seven stored lines; NOT PRODUCED lines and the required lcov), `RecordsTests` 5 (a temporary git repository with the records and their evidence committed together passes with both re-derivations; the seeded faults give exactly the six stored FAIL lines (catalog id, date order, dangling `supersedes`, an edited committed record, and two evidence hashes checked in the working tree); a committed re-derivation mismatch fails; outside a work tree the git rules are reported not applied and a wrong `updated` fails; `--analyze` gives the three stored current records), `UsageTests` 1.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-26 02:32 | working tree on `400e59d`, identities of section 1 | 16 (`CoverageTests` 2, `DiffRunsTests` 3, `LinkMapTests` 5, `RecordsTests` 5, `UsageTests` 1), 0 skipped | pass |
| Gate integration | 2026-09-26 02:37 | working tree on `400e59d`; rustos `c54d35a` | `tools/sw_gate.sh --keep-going` steps G2 link map, G3 identical result sets, G6 measurements | pass: FLASH 1608 B (0.04 percent), RAM 8200 B (1.54 percent), equal to the TC-SW-TOOL-001-r1 values; G3 run sets identical, all passed; G6 MSR-13 cwht-core lines 17 of 17 and cwht-hal-mock 53 of 53, MSR-14 and the emulation report NOT PRODUCED (nightly components and emulator absent) |
| Repository records | 2026-09-26 | `400e59d`, `docs/plan/measurements.json` | `--check-records` | exit 1: 80 evidence entries of 89 records fail the preservation rule at `1d423e5`, the first commit containing the records: 56 name evidence committed later with the recorded hash (at HEAD "equal to the record"), 24 name evidence whose file changed before or after (at HEAD "differs from the record"). A finding against the records file (07 section 11.1: a record is superseded at the commit when its evidence changes), not a tool defect |

Evidence: `evidence/python-tools-2026-09-26-r5-worktree.log.txt` (run 1); `evidence/sw-gate-2026-09-26.log.txt` (gate integration).

## 5. Reproducibility

Not required for class B. Deterministic function of the inputs; the git rules read committed content only.

## 6. Limitations

1. The append of new records and the TPM mirror of 07 section 11.1 are not implemented (due with the first image that contains application modules, FW-B1); until then `docs/plan/measurements.json` is appended by hand under the 07 section 11.1 rules and this tool checks it.
2. The re-derivation covers MSR-18 and MSR-19 from a cited link map only; the other Measured records are checked by evidence hash, not by value.
3. `--analyze` prints; the trend plots of 07 section 11.3 are not implemented.
4. The lcov summary reports lines, functions and branches; region coverage (MSR-13) is read from `cargo llvm-cov report` in the gate log, and the 100 percent thresholds are enforced by `cargo llvm-cov --fail-under` in the gate, not here.
5. The link-map parser reads the lld map layout (`VMA LMA Size Align Out`); another linker's map is not understood and stops the run (no section in a region).
6. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, its test module or its fixture (CM plan section 9.2 step 4).
- A change of the rustos linker script layout, of the linker (map format) or of the `docs/plan/measurements.json` format `cwht-measurements-1`.
- A change of the interpreter (TV-001) or of git (TV-009).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer re-runs section 3 and recomputes the over-red-line answers from the fixture map. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-MEASURE-001**: "Accredited for purposes 1 to 6 for `tools/measurements.py` at the git blob committed from working-tree blob `abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a`, under the TV-001 interpreter and the TV-009 git."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8; due PDR, CM plan section 13) | | |
