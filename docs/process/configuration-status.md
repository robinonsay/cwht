# cwht Configuration Status Accounting Report

**Status:** Log (Table 4-1 row 35 of `docs/process/05-configuration-and-data-management.md`, called 05 below). Issue 1, the first CSA report, 2026-09-27. **Owner:** Robin. **Author:** Claude (CM function). **Applicable baseline:** `baseline/srr`. **Required by:** 05 §6 (SE HB §6.5.1.2.4; SWE-083); SRR decision memo amendment A-8 and baseline record §8a line "The first CSA report, written by hand from the §6 sources, is the first CM action of the PDR phase"; `docs/plan/pdr-work-plan.md` WP-PDR-05 output 2 (carried item C-089).

**How this issue was produced.** 05 §6: "Until the tool is accredited, Claude writes the same sections by hand from the same sources". `tools/csa.py` does not exist yet (WP-PDR-07; TV record due PDR, 05 §13), so every section below was compiled by the CM function from the §6 sources with read-only commands (`git ls-files`, `git rev-parse HEAD:<path>`, `git log -1 -- <path>`, `git for-each-ref`, `git log --format=%(trailers)`) and by reading the CR, deviation, decision-memo, requirement, hazard, TPM and TV files. The Table 4-1 matching of item 2 applies the 05 §4.2 rule (an explicit path or file-name pattern wins over a directory prefix; among prefixes the longest wins; `*` also matches `/`) to every tracked file. The helper that ran these commands lives in the session scratchpad, is not a CI and generates no evidence; each count here can be re-derived with the command named beside it. Hashes are abbreviated to 12 hexadecimal digits; `git rev-parse HEAD:<path>` at the generation commit gives the full value. The report is regenerated before every life-cycle review and after every baseline, release, waiver or CR closure (05 §6), by `tools/csa.py` once it is accredited.

## 1. Header

| Field | Value |
|---|---|
| Generation date | 2026-09-27 |
| `HEAD` at generation | `9fd09627a07b48cda824341182717fa6775daa4b` (`main`) |
| Generator | By hand (CM function), 05 §6 interim route; no generator version |
| Tracked files | 1217 (`git ls-files \| wc -l`) |
| Current effective baseline | `baseline/srr` (functional; tag object `fed29c6ec11a`, commit `779f93fd7214`) plus merged CRs since the tag: **none**. CR-001, CR-002, CR-004 and CR-005 were dispositioned and applied on `main` before the tag, so their content is inside `baseline/srr`; none is Closed yet (item 4) |
| Functional-baseline content changed since the tag | None. `git diff --stat baseline/srr HEAD` over the paths of the Functional line of 05 §4.4 (rows 1, 2, 3, 5, 6, 7, 9, 17 for `docs/test_cases/`, 27, 51, 52, 53) lists no file |
| Local `main` against `origin` | The local ref `origin/main` is `1ff752b` (the post-tag record push); `main` is 24 commits ahead (`git rev-list --count origin/main..HEAD`). No network command was run for this issue |

## 2. CI status (Table 4-1)

Level legend (05 §4.1): L0 working, L1 reviewed (an `INSP-NNN` record with no open Major finding), L2 controlled, L3 released. Log and Record rows have no L2. "Pending CRs" are Submitted CRs whose proposed change touches the row (item 4); they change nothing until merged. SRR records are in `docs/reviews/SRR/checklists/`.

| Row | CI | Class | CR from | Level | Files | Hash at `HEAD` | Last commit | Last applied CR; pending CRs | Peer-review record |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Process charter | CR | SRR | L2 | 1 | `41575d218c22` | `6ea6b1d` 2026-09-26 | none; none | none (owner direction, 05 Table 4-2 row 1; SRR decision 1) |
| 2 | Process and planning documents | CR | SRR | L2 | 11 | 01 `eabbbd57953c`; 02 `fcdc54455547`; 04 `0b197bba6922`; 05 `f8de2081f754`; 06 `7a92d21f24a1`; 07 `bfe05f4327e7`; 08 `01a36bac8d5f`; README `3664073bc256`; SEMP `ccfdecf98a6e`; schedule `82b44894a761`; cost estimate `0dda83cbd5ad` | `106bc3a` 2026-09-27 (07, CR-005 amendment 1) | CR-001, CR-002, CR-005 (07, 04); pending CR-003, CR-006, CR-007, CR-010 | INSP-019 (01), INSP-020 (02), INSP-021 (04), INSP-006 with INSP-030 (05), INSP-007 (06), INSP-010 with INSP-018 (07), INSP-022 (08), INSP-005 (SEMP), INSP-023 (schedule, cost estimate); README by the §7.4 check |
| 3 | Classification record, RMM, compliance matrix | Mixed | SRR | L2 | 5 | 03 `ed270f443e2a`; `rmm.json` `e326ddd1b729`; `rmm.md` `54e351f4df23`; `se-compliance-matrix.json` `790d256214e0`; `.md` `09426930b27e` | `7d735e5` 2026-09-26 | none; pending CR-003, CR-006, CR-007, CR-010 | INSP-009 with INSP-017; INSP-024 |
| 4 | Stakeholder inputs log | Record | n/a | L0 | 1 | `362250fbaa62` | `d4c9366` 2026-09-26 | n/a | none (verbatim record) |
| 5 | Stakeholder expectations | CR | SRR | L2 | 2 | `expectations.json` `52b6cf5e8f7b`; `.md` `f460c1fb300a` | `b087a9f` 2026-09-26 | none; pending CR-003, CR-006, CR-009 | INSP-001 |
| 6 | ConOps | CR | SRR | L2 | 5 | tree `0b04e66c5bed` | `dd3372c` 2026-09-26 | none; pending CR-003, CR-006, CR-009 | INSP-002 |
| 7 | L1 system requirements | CR | SRR | L2 | 2 | tree `86ea40ebafc0` | `61a3cb7` 2026-09-27 | CR-002; pending CR-003, CR-006 | INSP-003 |
| 8 | L2 subsystem and software requirements | CR | PDR | L1 | 4 | `docs/requirements/tx/` tree `161a21584874`; `docs/requirements/sw/` tree `f6610c4242f1` (rx, pwr, ctl, me absent) | `cd61450` 2026-09-26 | none; none | INSP-004 (TX, SW-KEYER), INSP-026 (SW-KEYER assurance) |
| 9 | Schemas (eleven files) | CR | SRR | L2 | 11 | `allocation.schema.json` `c17e011ba352`; `measurements.schema.json` `c30b7f3e7466`; `tpm.schema.json` `df3bd894ffec`; `rmm.schema.json` `ae2f87dd97c7`; `se-compliance-matrix.schema.json` `ef156b0fcfaa`; `l0-stakeholder/schema.json` `d0a79903f895`; `requirements/schema.json` `ca049dfb0a44`; `risk/schema.json` `473cd797db58`; `safety/schema.json` `e96accaad02d`; `rfa-rid-log.schema.json` `38898b0c260c`; `test_cases/schema.json` `d4b70163ca13` | `08d1496` 2026-09-26 | none; none | none (no checklist; tool runs, 05 Table 4-2 row 9) |
| 10 | ICDs | CR | PDR | L1 | 11 | tree `73ec0d41dba8` | `e597e49` 2026-09-26 | none; pending CR-003 | INSP-012 (external stubs) |
| 11 | Architecture, allocation, budgets, software design | CR | PDR (architecture, allocation, budgets); CDR (software design) | L0 | 1 | `docs/design/allocation.json` `442de2fd078f` (architecture, budgets, software design absent) | `cd61450` 2026-09-26 | none; pending CR-003 | none |
| 12 | Trade studies | Record | n/a | L1 | 2 | tree `acba4fc87886` | `2362183` 2026-09-26 | n/a; pending CR-003 (new study) | INSP-013, INSP-027 (TS-002 assurance) |
| 13 | ADRs | Record | n/a | L1 | 29 | tree `6ceb7a58b22c` | `5122a6b` 2026-09-26 | n/a; pending CR-003, CR-006 (new ADRs) | INSP-011 |
| 14 | Risk register | Log | n/a | L1 | 2 | `register.json` `6685aa0eadc9`; `register.md` `f8c28b363035` | `4df6606` 2026-09-27 (WP-PDR-18 Track pass) | n/a; pending CR-003, CR-006 | INSP-007 |
| 15 | Hazard analysis, hazard list (0.5.0-pha) | CR | PDR | L1 | 2 | `hazard-analysis.md` `52c8ce168564`; `hazards.json` `81cacde47d4f` | `bfea9c7` 2026-09-26 | CR-002; pending CR-003 | INSP-008 |
| 16 | V&V plan | CR | PDR | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 17 | Test cases and procedures | CR | SRR (TC-SYS); PDR (others) | L2 for `sys/`; L1 for `tx/`, `sw-keyer/`, `sw-tool/` | 7 | tree `a944e53f4702`: `sys/` `90827b56cee6`, `tx/` `44e3480e3c34`, `sw-keyer/` `fec5fbfb106c`, `sw-tool/` `13018bbeb443` | `ebe5873` 2026-09-26 | CR-002; pending CR-003, CR-006 | INSP-025 (TC-SYS); INSP-004 and INSP-026 name the TC-TX and TC-SW-KEYER files; INSP-016 (TC-SW-TOOL) |
| 18 | Traceability report and data | Log | n/a | L0 | 4 | `docs/vv/traceability-report.md` `2a3e1d76fedd`; `docs/vv/traceability.json` `16768ed797db`; SRR copies `32c5c4533ee3`, `345fa17b2f5a` | `d4cce27` 2026-09-26 | n/a | generated |
| 19 | Test reports | Record | n/a | L0 | 113 | tree `3909a3daa5f1` | `68a44ed` 2026-09-27 (TC-SW-TOOL-001 run 6) | n/a | INSP-016 covers the TC-SW-TOOL-001 reports |
| 20 | NCRs | Record | n/a | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 21 | Schematics and PCB | CR | CDR | none (absent; `hardware/kicad/.gitkeep` is row 42) | 0 | n/a | n/a | n/a | n/a |
| 22 | BOM | CR | CDR | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 23 | Enclosure CAD | CR | CDR | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 24 | Simulation decks and checkers | CR | CDR | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 25 | Firmware source | CR | first `release/FW-*` tag | L1 (FW-B0) | 20 | tree `de1c87cb4190` | `93d019b` 2026-09-26 | CR-001; none | INSP-016, INSP-028 |
| 26 | External `rustos` | CR | first `release/FW-*` tag | L0 (informational) | 0 | pin `2ec64c0f15c8` (lock §3) | pin set by CR-004 at `5792350` | CR-004; none | n/a |
| 27 | Toolchain lock and venv pins | Mixed | SRR | L2 | 2 | `toolchain.lock.md` `04819139c8a1`; `requirements.txt` `ef9820618aaf` | `495a0c3` 2026-09-27 | CR-004; none | INSP-015 |
| 28 | Verification, CM and build tooling | CR from each tool's TV date | per tool | per tool (item 9) | 252 | tree `a504930a1a41` | `41d150e` 2026-09-27 (`tools/ltspice-batch.sh`, WP-PDR-07) | CR-002 (`traceability.py`), CR-005 (`complexity_gate.py`); pending CR-003 | INSP-015 (TV-001 to TV-010, TV-012) |
| 29 | Corpus conversion scripts | Log | n/a | L0 | 4 | tree `16fcf2114a02` | `4e3f891` 2026-09-25 | n/a | none |
| 30 | Tool validation records | Record | n/a | L1 for TV-001 to TV-010 and TV-012 | 67 | tree `b047647e3b7d` | `d3de579` 2026-09-27 (evidence files of WP-PDR-08) | n/a | INSP-015 |
| 31 | Change requests | Record | n/a | L0 | 9 | tree `ce6fb6c9c95b` | `9fd0962` 2026-09-27 (CR-010) | n/a | CR section 6 reviews (item 4) |
| 32 | Baseline records | Record | n/a | L0 | 1 | `docs/reviews/SRR/baseline-record.md` `b12d961be933` | `1ff752b` 2026-09-27 | n/a | `docs/reviews/SRR/baseline-check.md` (independent check 3) |
| 33 | Review records | Record | n/a | L0 | 97 | tree `8c9210cb45ab` (SRR `94e770abc96b`, PDR `0a07852f3eb3`) | `1fe9c1a`, `e119181` 2026-09-27 (PDR folder) | n/a | n/a |
| 34 | TPMs and leading indicators | Mixed | PDR | L0 | 1 | `docs/plan/tpm.json` `e7f2070d93f4` | `4b6c96c` 2026-09-26 | none; pending CR-003, CR-006 | none as product (SRR records read it as an input); `docs/reviews/PDR/checklists/tpm-definitions.md` planned (WP-PDR-29) |
| 35 | Configuration status report | Log | n/a | L0 | 0 before this issue | this file | this issue | n/a | review record planned: `docs/reviews/PDR/checklists/configuration-status.md` |
| 36 | Firmware releases and VDDs | Record (L3) | n/a | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 37 | Hardware release packages | Record (L3) | n/a | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 38 | Unit as-built records | Record | n/a | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 39 | Configuration audit record | Record | n/a | none (absent; SAR) | 0 | n/a | n/a | n/a | n/a |
| 40 | Research, lessons learned, tutorials, READMEs | Log | n/a | L0 | 125 | `docs/research/` tree `65dc4959a41a` (121 files); `docs/lessons-learned.md` `ec30a264fdef`; `README.md` `9e57b91b3837`; `docs/requirements/README.md` `89bef4fc2a31`; `tools/README.md` `8dc4b3ae02a6` | `e119181` 2026-09-27 (`docs/lessons-learned.md` created) | n/a; pending CR-003 (`README.md`) | review record planned: `docs/reviews/PDR/checklists/lessons-learned.md` |
| 41 | Reference corpus | Log | n/a | L0 | 382 | tree `4874c0c1b451` | `4e3f891` 2026-09-25 | n/a | none |
| 42 | Repository configuration | Log | n/a | L0 | 14 | `.gitignore` `7b3549725973`; `.mcp.json` `1372d7812679`; 12 `.gitkeep` files (empty blob `e69de29bb2d1`) | `e119181` 2026-09-27 (three PDR `.gitkeep`) | n/a; pending CR-003 (`.gitignore`) | none |
| 43 | CM deviations log | Record | n/a | L0 | 1 | `bcb91b5c9a26` | `bb2485e` 2026-09-27 | n/a | none |
| 44 | Sprint records | Record | n/a | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 45 | Software measurements | Record | n/a | L0 | 1 | `docs/plan/measurements.json` `5e2d1755c6ad` | `1d423e5` 2026-09-26 | n/a | none |
| 46 | Unsafe audit list | Log | n/a | L0 | 1 | `firmware/unsafe-audit.md` `18ef484bf050` | `5792350` 2026-09-26 | CR-004 | 37 entries unsigned (a note until CDR) |
| 47 | Operations handbook | CR | SAR | none (absent) | 0 | n/a | n/a | pending CR-003 | n/a |
| 48 | RF exposure evaluation | CR | PDR | none (absent; WP-PDR-30) | 0 | n/a | n/a | pending CR-003 | n/a |
| 49 | Build-to specification, design analyses | CR | CDR | none (absent) | 0 | n/a | n/a | n/a | n/a |
| 50 | Integration plan | CR | PDR | none (absent; WP-PDR-44) | 0 | n/a | n/a | n/a | n/a |
| 51 | Technology assessment | CR | SRR | L2 | 1 | `d46abde01adf` | `12d7bb7` 2026-09-26 | none; pending CR-003 | INSP-014 |
| 52 | Design concept | Mixed | SRR | L2 | 1 | `6f026f92ae4f` | `dd3372c` 2026-09-26 | none; pending CR-003, CR-006, CR-009 | INSP-002 |
| 53 | Templates and checklists (21 files) | CR | SRR | L2 | 21 | tree `e94d4ce59c8b` | `b301df2` 2026-09-26 | none; pending CR-003, CR-007 | none (05 Table 4-2 row 53: tool runs) |
| 54 | V&V data-package layout | CR | PDR | L0 | 1 | `docs/vv/README.md` `878869d346d9` | `4e3f891` 2026-09-25 | none; none | none |
| 55 | Licence | Record | n/a | L0 | 1 | `LICENSE` `0411ad910267` | `7e0f2fe` 2026-09-25 | n/a | n/a (ADR-017) |

**Tracked files that match no row (must be empty): 2.**

| Path | Committed at | Note |
|---|---|---|
| `docs/plan/status/status-2026-09-27.md` | `72e1863` (created), `3d4a74d` (section 4 appended) | INSP-030 finding-5 lien (C-088): its due was "before the first status note is committed if earlier", and the note was committed first |
| `docs/plan/pdr-work-plan.md` | `51600e8` (revision 1), `ab2af2d` (revision 2) | Not named by any row; found by this issue |

CR-007 (Submitted) proposes Table 4-1 row 56 (`docs/plan/status/`, Record) and row 57 (`docs/plan/*-work-plan.md`, Log). Applying the §4.2 rule with those two rows added gives an empty unmatched list at this `HEAD`. No path matches two rows with equal precedence.

**Safety-critical and mission-critical code sub-rows of row 25.** Not yet listable: `docs/design/allocation.json` has no `code` paths for the 07 §14.1 components at this `HEAD`, and 05 does not yet name the map (CR-007 change C4, INSP-030 finding-4). FW-B0 holds no safety-critical component (MSR-12 note, `docs/plan/measurements.json`).

## 3. Baselines

| Tag | Tag object | Tagged commit | Date | Decision memo | Signed | `git tag -v` | Pushed (`git ls-remote --tags origin`) |
|---|---|---|---|---|---|---|---|
| `baseline/srr` | `fed29c6ec11a0407bc64935c9c277a49135f4de8` | `779f93fd7214617a08e868cde0e5fafd9b9e848a` | 2026-09-27 09:09:18 -0500 | `docs/reviews/SRR/decision-memo.md` (disposition Approved with liens, signed 2026-09-26, memo commit `0bcea39554d6`) | no (no signing key configured; OQ-CM-002; SRR decision 15 asks for signing before `baseline/pdr`, owner decision OD-28) | n/a (unsigned) | yes: `fed29c6ec11a0407bc64935c9c277a49135f4de8 refs/tags/baseline/srr`, recorded in `docs/reviews/SRR/baseline-record.md` §8a at `1ff752b`; not re-observed in this issue (no network command) |

Source: `git for-each-ref refs/tags/baseline/`; `git cat-file -p baseline/srr` equals the §8a output. No other `baseline/*` or `release/*` tag exists.

## 4. CR register

Source: the front matter and section 11 of each file in `docs/cm/cr/`. "Applied" means the change was made on `main` before the `baseline/srr` tag (05 Table 4-1 CR-from events had not occurred for the files touched, or the ruling was part of the SRR close-out).

| CR | Title | Class | Status | Originator | Opened | Dispositioned | Closed | Affected CIs (rows) | Target release | Merge SHA | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CR-001 | Admit driver-construction failure arms in cwht-app; place the panic handler | II | Dispositioned (Approved) | Claude | 2026-09-26 | 2026-09-26 (SRR decision 108) | no | 2, 25, 28 | none | null | Applied before the tag; steps 2 and 3 verification at the FW-B1 code review; closure is OD-27 |
| CR-002 | Admit Inspection for hazard-tracing requirements that state a documentary or physical property | I | Dispositioned (Approved) | Claude | 2026-09-26 | 2026-09-26 (SRR decision 113; class confirmed by close-out item 7) | no | 2, 7, 15, 17, 28 | none | null | Applied before the tag (steps 1 to 5); section 6 review recorded at `8b86c16` (deviation entry 1 closed); closure is OD-27 |
| CR-003 | Make the enclosure requirement solution-neutral and the legend process-neutral | I | Submitted (revision 3; re-check of 2026-09-27 at `908cc8b`: 0 Major, 5 Minor) | Claude | 2026-09-27 | not yet (OD-02) | no | 2, 3, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 18, 28, 34, 40, 42, 47, 48, 51, 52, 53 | none | null | Products that depend on it are AT RISK (plan rule C8) |
| CR-004 | Move the rustos lock pin from c54d35a to 2ec64c0 and regenerate the unsafe audit list | I | Dispositioned (Approved) | Claude | 2026-09-26 | 2026-09-26 (SRR close-out item 1; class confirmed by item C) | no | 26, 27, 46 | none | null | Applied at `5792350`; section 6 review at `8b86c16` (deviation entry 2 closed); closure is OD-27 |
| CR-005 | Fix the CS-17 and CS-38 complexity counting convention and the CS-19 halt-loop allowance | I | Dispositioned (Approved; amendment 1 of 2026-09-27) | Claude | 2026-09-26 | 2026-09-26 (close-out item 4; amended by item A, class I by item C) | no | 2, 28 | none | null | Applied at `e34a27b` and `106bc3a`; section 6 review at `8b86c16` (deviation entry 3 closed); closure is OD-27 |
| CR-006 | Build one assembled unit first and decide on further units after its evaluation | I | Submitted (revision 2; round 2 review at `6d8e624`: 0 Major, 4 Minor) | Owner | 2026-09-27 | not yet (OD-03) | no | 2, 3, 5, 6, 7, 13, 14, 17, 18, 34, 52 | none | null | Products that depend on it are AT RISK (plan rule C8) |
| CR-007 | Add the allocated-baseline admission rows to the CM plan and close its SRR liens | II | Submitted (section 6 review pending, plan wave 1a) | Claude | 2026-09-27 | not yet (OD-36, B1a) | no | 2, 3, 53 | none | null | PCR-1 of the PDR plan; blocks the PDR readiness declaration (05 §4.4) |
| CR-008 | none at generation | | | | | | | | | | The number was claimed by a parallel wave 0 work package (commit message of `9fd0962`); no file exists at this `HEAD`. 05 §5.2 assigns the next number from this register; the claim is a cross item for the lead SE |
| CR-009 | Fix the SRR peer review liens of the L0 set, the ConOps and the concept | I | Submitted | Claude | 2026-09-27 | not yet | no | 5, 6, 52 | none | null | WP-PDR-10 |
| CR-010 | Apply SRR decisions 9 and 40 to the classification record, the software plan and the RMM | II | Submitted (prototype on `cr/CR-010-apply-srr-decisions-9-and-40` at `5cd87cf`) | Claude | 2026-09-27 | not yet | no | 2, 3 | none | null | WP-PDR-17; also changes `rmm.json`, as CR-007 does (item 13 note) |

No CR is Deferred, Withdrawn or Closed (Rejected). No CR has a target release.

## 5. Editorial log

Commits in `baseline/srr..HEAD` that carry an `Editorial:` trailer: **none** (`git log --format=%(trailers) baseline/srr..HEAD`). No reviewer sampling has taken place yet; the first sample is at the PDR interim check (05 §7.4).

## 6. Log-class and Record-class change log (since `baseline/srr`)

Every commit in `baseline/srr..HEAD` (26 commits) touches only Log-class or Record-class CIs, or files that match no row; none touches a class-CR CI after its CR-from event. `Refs:` is the parsed git trailer.

| Commit | First line | Rows touched | `Refs:` trailer |
|---|---|---|---|
| `1535cd5` | docs(srr): independent baseline check 3 of baseline-record.md section 0.4 at R 779f93f, READY FOR TAG | 33 | **missing** |
| `1ff752b` | baseline(srr): record tag verification | 32, 33 | SRR |
| `dd54eb1` | docs(cm): submit CR-003 | 31 | CR-003 |
| `4347c68` | docs(cm): record CR-003 independent impact review | 31 | CR-003 |
| `72e1863` | Status note 2026-09-27 | no row (item 2) | CR-003 |
| `cc83c8c` | docs(cm): CR-003 revision 2 | 31 | CR-003 |
| `9373729` | docs(cm): submit CR-006 | 31 | CR-006 |
| `34668e3` | docs(cm): record CR-006 impact review round 1 | 31 | CR-006 |
| `e8f21c9` | docs(cm): record CR-003 revision 2 re-check | 31 | CR-003 |
| `d9a215a` | docs(cm): CR-003 revision 3 | 31 | CR-003 |
| `51600e8` | docs(plan): PDR work plan | no row (item 2) | none |
| `39a6b13` | docs(cm): CR-006 revision 2 | 31 | CR-006 |
| `908cc8b` | docs(cm): record CR-003 revision 3 re-check | 31 | CR-003 |
| `6d8e624` | docs(cm): record CR-006 impact review round 2 | 31 | CR-006 |
| `ab2af2d` | docs(plan): PDR work plan revision 2 | no row (item 2) | none |
| `3d4a74d` | Status note 2026-09-27 section 4 | no row (item 2) | PDR |
| `a3cacee` | test(tools): Rust tool known-answer fixtures (WP-PDR-08) | 28, 30 | TV-020, TV-021, TV-022, TV-023, WP-PDR-08 |
| `d3de579` | test(tools): nextest JUnit store directory (WP-PDR-08) | 30 | TV-022, WP-PDR-08 |
| `4df6606` | docs(risk): register Track pass (WP-PDR-18 wave 0) | 14 | RSK ids |
| `1fe9c1a` | docs(pdr): owner action pack (WP-PDR-04) | 33 | **missing** |
| `1f7d138` | docs(cm): submit CR-009 | 31 | CR-009 |
| `41d150e` | tool(ltspice): headless LTspice batch wrapper (WP-PDR-07) | 28 | TV-014, ADR-018, SI-027 |
| `e119181` | docs(pdr): PDR workspace, lessons-learned file, CR-007 (WP-PDR-05) | 31, 33, 40, 42 | PDR, CR-007, RFA-SRR-003 |
| `1479b30` | docs(cm): CR-009 corrections | 31 | CR-009 |
| `9032a02` | docs(cm): CR-007 row 56 | 31 | CR-007 |
| `9fd0962` | docs(cm): submit CR-010 (WP-PDR-17) | 31 | **not parsed** (a `Refs: CR-010` line is in the body, but a blank line separates it from `Co-Authored-By:`, so git does not read it as a trailer) |

`tools/` files under row 28 whose tool has no TV record yet are Log class until accreditation (row 28 Notes); `tools/ltspice-batch.sh` (`41d150e`) is such a file.

## 7. Release register

None. No `release/FW-*`, `release/HW-MB-*` or `release/ME-ENC-*` tag exists, `firmware/releases/` and `hardware/releases/` do not exist, and no receipt inspection report exists. The FW-B0 images of TC-SW-TOOL-001 are development evidence (`credit: false`), not releases (baseline record §6).

## 8. Audit register

No FCA, PCA or delta configuration audit has been performed (05 §7.1 and §7.2 are SAR activities). Interim configuration checks (05 §7.4): the SRR checks are the independent baseline checks of `docs/reviews/SRR/baseline-check.md` (check 3 READY FOR TAG at R, `1535cd5`), with observations OBS-1 (Table 4-2 row 2 wording; carried by CR-007 change C6) and OBS-2 (answered by the post-tag record). The PDR interim check is due with the PDR records (plan wave 3).

## 9. Tool accreditation

Sources: `tools/toolchain.lock.md` §5 and `docs/reviews/SRR/baseline-record.md` §0.4 at `HEAD`; each accredited blob was compared with `git rev-parse HEAD:<path>` for this issue and is equal. Only TV records committed at `HEAD` count; records being written in the working tree by wave 0 work packages appear in the next issue.

| Tool | Locked version or blob at `HEAD` | Class | TV record | Accreditation status | Purposes |
|---|---|---|---|---|---|
| venv Python with jsonschema | Python 3.13.5, jsonschema 4.26.0 | B | TV-001 | Accredited 2026-09-26 (ACC-PYJS-001, SRR decision 114) | Schema validation, Draft 7 keyword set of TV-001 purpose 2 |
| `tools/traceability.py` | blob `12de3545` | B | TV-002 | Accredited (ACC-TRACE-001, extended to `12de3545`) | Traceability set and writing rules (05 §9.2) |
| `tools/validate_docs.py` | blob `3aa03681` | B | TV-003 | Accredited (ACC-VALDOCS-001 with extension) | Schema and record validation |
| `tools/render_rmm.py` | blob `2386a37f` | B | TV-004 | Accredited (ACC-RMM-001) | RMM check and render |
| `tools/render_compliance.py` | blob `d67d6b5e` | B | TV-005 | Accredited (ACC-COMPL-001) | Compliance-matrix check and render |
| `tools/render_risk.py` | blob `d38ba1dd` | B | TV-006 | Accredited (ACC-RISK-001) | Risk register check and render |
| `tools/review_trend.py` | blob `04493157` | B | TV-007 | Accredited (ACC-TREND-001) | Review-trend TPM-003 |
| `tools/slides/render_deck.py` with the Chromium headless shell | blob `b42425e9` | B | TV-008 | Accredited (ACC-DECK-001) | Review deck PNG renders |
| git | 2.50.1 (Apple Git-155) | B | TV-009 | Accredited (ACC-GIT-001) | Object hashes, `fsck`, tags |
| `tools/render_review_figures.py` | blob `6f3018fd` | B | TV-010 | Accredited (ACC-FIGS-001) | SRR package figures |
| `tools/complexity_gate.py` fed by `rust-code-analysis-cli` 0.0.25 | blob `ddf10798` (CR-005 amendment 1) | B | TV-012 | Accredited (ACC-COMPLEXITY-001, extended to `ddf10798` by TV-012 run 3, effective 2026-09-27 on INSP-015 re-issue 4; liens F-11, F-13) | SWE-220 limit, CS-38, CS-19 report, MSR-17 |
| `tools/unsafe_audit.py` | blob `cc3aaa2a` | B | TV-011 | Validated, not accredited (due CDR) | Unsafe audit list, MSR-11 |
| `tools/measurements.py` | blob `abe25acb` | B | TV-013 | Validated, not accredited (due PDR) | Measurement records |
| Rust toolchain 1.98.0 (`rustc`, `cargo`, `clippy`) | lock §1 | A and B | none committed at `HEAD` (TV-020 in preparation by WP-PDR-08; its fixtures are committed at `a3cacee`) | Not yet validated at `HEAD` (due PDR) | Firmware image; HostUnit and static analysis |
| `cargo-llvm-cov` 0.9.1 with llvm-tools | lock §1 | B | none committed at `HEAD` (TV-021 in preparation by WP-PDR-08) | Not yet validated at `HEAD` (due PDR) | MSR-13 coverage |
| `tools/ltspice-batch.sh` with LTspice 26.0.2 | blob `884df077` (`41d150e`) | B | TV-014 (claimed in `41d150e`; no record file at `HEAD`) | Not yet validated (due PDR, WP-PDR-07) | LTspice batch simulation |
| `tools/sw_gate.sh` | blob `29a37127` | B | none | Not yet validated (due CDR) | Software gate G0 to G6 |
| kicad-cli 10.0.6 with `tools/normalize_fab.py`; OpenSCAD 2021.01 and FreeCAD 1.1.3 with `tools/scad2step.py`; the emulator; `cargo-nextest`; `nightly-2026-08-24`; `tools/render_tpm.py`; `tools/csa.py`; `tools/check_commit_msg.py` | lock §1; the scripts do not exist yet | A or B | none at `HEAD` (TV-015 onward planned, WP-PDR-07, WP-PDR-08, WP-PDR-42) | Not yet validated (due PDR, 05 §13) | 05 §9.1 |
| `picotool` 2.3.0, `shasum`, `cargo-audit`, `cargo-deny`, `cargo-geiger`, `cargo-binutils`, `tools/release.sh`, `tools/image_trailer.py`, `tools/kicad_export/pcbway_package.sh`, the redaction check | lock §1 or not written | A or B | none | Not yet validated (due CDR) | 05 §9.1 |
| tinySA Ultra firmware, sigrok-pico capture firmware, `sigrok-cli` | not received or not installed | B | none | Not yet validated (due TRR) | Bench evidence |

## 10. Metrics (Table 6-1)

| Metric | Value at 2026-09-27 | Threshold | State | Response |
|---|---|---|---|---|
| Requirements volatility (`MSR-02`) | No `MSR-02` value exists: `docs/plan/measurements.json` records `MSR-02` as "Not yet measured", due at PDR by `tools/traceability.py --volatility` (planned). The CSA copies `MSR-02` and does not compute it (05 §5.4). Observation for the reader: `git diff --stat baseline/srr HEAD -- docs/requirements/` is empty, so no requirement has changed in the interval so far | 10 % yellow, 20 % red (07 §11.2) | Not measured | None until measured; the first value is due in the PDR package (05 §13 PDR row "volatility metric reported") |
| Open CRs and their age | 5 open: CR-003 (Submitted, opened 2026-09-27, 0 days), CR-006 (Submitted, 0 days), CR-007 (Submitted, 0 days), CR-009 (Submitted, 0 days), CR-010 (Submitted, 0 days). None Draft, Assessed or Deferred. CR-001, CR-002, CR-004 and CR-005 are Dispositioned and not Closed (not counted by the Table 6-1 definition; their closure is OD-27) | Zero CRs past their §5.2 cycle-time target; zero Deferred past re-look | Green (none past target at generation). **At risk:** CR-007 and CR-010 are Class II (target: one working session from submission); the PDR plan puts their section 6 review first (rule C6), and CR-007's disposition is planned at B1a on 2026-09-29, the second owner session after submission (B0 on 2026-09-28 is the first). CR-003, CR-006 and CR-009 are Class I (target: the next review or 14 days, so by 2026-10-11 or the PDR session, whichever is earlier) | If a CR passes its target, it is listed by id in the PDR package and the owner dispositions or re-defers it there, or an RFA is raised (05 Table 6-1) |
| CR cycle time | No CR has been dispositioned since `baseline/srr`. Before the tag: CR-001 and CR-002 were dispositioned the day they were opened (CR-002 without the Assessed state, deviation entry 1); CR-004 and CR-005 were dispositioned before their files existed (deviation entries 2 and 3) | Class II: one working session; Class I: the next review or 14 days | Not applicable in this interval | None |
| Commits lacking mandatory trailers | 3 in `baseline/srr..HEAD`: `1535cd5` and `1fe9c1a` (no `Refs:`; both touch row 33 records) and `9fd0962` (`Refs:` line not parsed as a trailer, item 6). 0 commits touch a class-CR CI after its CR-from event without a `CR:` or `Editorial:` trailer | 0 (SEMP §5 CM row) | **Red (3 against 0)** | Each commit is a RID candidate at the PDR (05 Table 6-1); none touches a class-CR CI, so no deviation entry is required by that rule |

## 11. Deviations from this plan

Copied from `docs/cm/deviations.md` (blob `bcb91b5c9a26`):

| # | Date | Procedure departed from | Departure (short) | RFA | Status |
|---|---|---|---|---|---|
| 1 | 2026-09-26 | 05 §5.2 (Assessed before Dispositioned) | CR-002 dispositioned before its impact review | RFA-SRR-008 (entry 4) | Closed 2026-09-27 (CR-002 section 6 at `8b86c16`) |
| 2 | 2026-09-27 | 05 §5.2 | CR-004 dispositioned before its impact review | RFA-SRR-008 | Closed 2026-09-27 (CR-004 section 6 at `8b86c16`) |
| 3 | 2026-09-27 | 05 §5.2 | CR-005 dispositioned before its impact review | RFA-SRR-008 | Closed 2026-09-27 (CR-005 section 6 at `8b86c16`) |
| 4 | 2026-09-27 | Correction line for entry 1 | Entry 1 brought under RFA-SRR-008 | RFA-SRR-008 | Closed 2026-09-27 with entry 1 |

**Departure found by this issue, not yet entered in the log.** 05 §4.2: "Untracked files are not CIs and are never committed unless they match a row." Four commits committed or changed files that match no Table 4-1 row: `72e1863` and `3d4a74d` (`docs/plan/status/status-2026-09-27.md`) and `51600e8` and `ab2af2d` (`docs/plan/pdr-work-plan.md`). The CM function proposes it as deviation entry 5 (05 §4.2; RFA to be decided by the owner; closure: CR-007 rows 56 and 57 merged, then this item 2 unmatched list empty). The entry is a cross item for the lead SE, who writes the deviations log in this phase.

## 12. Waivers

| Waiver | Requirement or target waived | Rationale (short) | Approving memo or CR | Releases affected | Status |
|---|---|---|---|---|---|
| `docs/reviews/SRR/decision-memo.md#W1` | INSP-016 readiness condition R3 ("the design unit is Active and named in `// @design`") for the FW-B0 product only (07 §10.2) | FW-B0 precedes the design units of PDR | SRR decision 115 (b), owner ruling 2026-09-26; memo §8.2, numbered W1 by amendment A-1 | none (FW-B0 is not a release) | Active for FW-B0 only; lapses for FW-B1 onward |

No `Approved (waiver)` CR exists.

## 13. Open items

**Open TBRs by target review** (counted from the files at `HEAD`; each `tbr` object's `close_by`):

| Set | Source file | Open TBRs | Target review |
|---|---|---|---|
| L1 requirements | `docs/requirements/sys/requirements.json` (190 requirements: 188 Active, 2 Closed) | 109 | PDR (every one `close_by: PDR`; charter §7: all L1 TBRs close by PDR) |
| L2 requirements, TX | `docs/requirements/tx/requirements.json` (16 Draft) | 14 | PDR (charter §7 allows CDR) |
| L2 requirements, SW-KEYER | `docs/requirements/sw/sw-keyer/requirements.json` (39 Draft) | 11 | PDR (charter §7 allows CDR) |
| TPMs | `docs/plan/tpm.json` | 4 with `close_by: PDR` (TPM-001, 002, 006, 016); TPM-014 keeps a `tbr` object with `close_by: SRR`, although SRR decision 90 ruled its value (cross item for the TPM owner, WP-PDR-29) | PDR |
| Hazard controls | `docs/safety/hazards.json` 0.5.0-pha | 17 items in 16 controls (HZ-001 K2; HZ-002 K4, K5; HZ-003 K1, K2, K9; HZ-004 K4 (two items), K5, K9, K12, K13; HZ-007 K1, K4; HZ-008 K7; HZ-010 K1; HZ-013 K1) | PDR |
| L0 expectations | `docs/requirements/l0-stakeholder/expectations.json` | 0 `tbr` objects; the L0 TBR marks are in statement text (MOE-010 bench part and the mirrors of plan section 10.2), counted by WP-PDR-45 | PDR |

The SRR memo section 6 lists 101 L1 TBR liens; the file holds 109, as the baseline record §5 explains (REQ-SYS-180 to 182 and the five TBRs added by R16). `docs/lessons-learned.md` entry 16 records the lesson.

**Liens and open log items from `docs/reviews/SRR/decision-memo.md` section 6** (state from `docs/reviews/SRR/rfa-rid-log.json`; every due event is the PDR readiness declaration):

| Item | Lien | Subject | State |
|---|---|---|---|
| RFA-SRR-001 | L-1 | TBRs carried to PDR (with the requirement TBR liens) | Open |
| RFA-SRR-002 | L-2 | Mass and envelope estimates for TPM-001 and TPM-016 | Open |
| RFA-SRR-003 | L-3 | Create `docs/lessons-learned.md` with the ten package section 19 entries | Open. The file was created at `e119181` (ten entries plus the seven lessons of the PDR plan section 1.4); the log move to Answered is WP-PDR-15's, after the independent record `docs/reviews/PDR/checklists/lessons-learned.md` |
| RFA-SRR-004 with RID-SRR-001, 002, 004 to 014 | L-4 | Package-level Minor items | Open; RID-SRR-010 Answered |
| RID-SRR-003 | (R16 edit) | REQ-SYS-054 no-gap form | Open |
| RFA-SRR-005 | L-5 | Cross-document items due at PDR | Open |
| RFA-SRR-006 | L-6 | Minor findings of the 30 SRR records (the twelve against 05 are carried by CR-007) | Open |
| RFA-SRR-007 | L-7 | Package-level Routine items (the 05 §9.2 rows are carried by CR-007) | Open |
| RFA-SRR-008 | none | Independent impact reviews of CR-002, CR-004, CR-005 | Answered (reviews at `8b86c16`) |

Other open CM items: the owner's review of the GitHub bypass report of the `baseline/srr` push (baseline record §8a; OD-28); the tag-signing key before `baseline/pdr` (SRR decision 15; OQ-CM-002; OD-28); baseline check 3 OBS-1 (CR-007 change C6).
