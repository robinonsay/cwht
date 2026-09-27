# TV-018: tools/csa.py (git blob dd9b6fed, commit b308f8c)

| Field | Value |
|---|---|
| Record | TV-018 |
| Status | **Validated** 2026-09-27 (known-answer run 1 at commit `b308f8c`: 33 tests passed, 0 skipped, the hand CSA comparison included). Independent review and owner accreditation pending (sections 8 and 9). Until accredited, the CSA stays hand-written (05 section 6) and this tool's output is developer evidence |
| Class | B, evidence-generating (CM plan section 9.1: the CSA is audit and review evidence, SWE-083) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8) through CM plan section 9; SWE-083 through CM plan section 6 (items 1 to 13, Table 6-1); the Table 4-1 matching rule of section 4.2 and the levels of section 4.1 |
| Due | PDR (CM plan section 13 PDR row). First cited use: the PDR CSA issue in the PDR package (WP-PDR-48) if the owner accredits before then; otherwise the hand issue |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/csa.py`; section 1.2 row `tools/csa.py`; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 1a) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/csa.py` | git blob `dd9b6fede610f61d033d88222450981315559ed5`, SHA-256 `919d3d560d9d7811ca24c6cf6e18b4ca0e4f9298669916a813fe6f59d003f42c`, 810 lines | committed in `b308f8c` (first blob in `86ff3b0`, commit note of TV-015 section 1; the `b308f8c` change reads YAML block lists and directory products of INSP records) |
| `tools/check_commit_msg.py` (imported for item 6 and the trailer metric; TV-019) | git blob `5488dd98b21220261835a74112b49a508865c346` | committed in `86ff3b0` |
| `tools/tests/test_csa.py` | git blob `58672f3ac0b09aadcdabad0ef9d9f28c55ddf041`, SHA-256 `a805a681f271c8f58ca002d60c5d245a40535b6f51b3852bfb8ca29cceea9b68`, 33 tests | committed in `b308f8c` |
| `tools/tests/fixtures/csa/` | 4 files (`build_repo.py`, `cm-plan-05.md`, `expected.json`, `hand-csa-9fd0962.json`), git tree `92fd0e50c0d61bf2c8e71b9e6b7dc518c6733d30`, digest `cdc66c09e8b6857543abf762ff462fe7584dab42514ff80d97ef5e9cc06ba872` | committed in `86ff3b0`; shared with TV-019 |
| Read by `HandCsaTests` (repository content) | the repository at `9fd0962` and the hand CSA issue 1 at `b790eaa`, transcribed into `hand-csa-9fd0962.json` | immutable commits |
| Runtime | TV-001 interpreter (Python 3.13.5), standard library; git 2.50.1 (TV-009) | lock sections 1 and 2 |

**Install source:** the repository (CM plan Table 4-1 row 28).

## 2. Purposes covered

1. Parse 05 Table 4-1 at a revision (backticked pathspecs outside parentheses; a row without a pathspec; class and CR-from cells) and assign every tracked file of that revision to one row by the 05 section 4.2 rule (explicit path or file-name pattern over directory prefix, longest prefix, `*` across `/`), listing the files of no row and of two equal rows.
2. Report per row, at the revision: the file count, the blob (one file) or tree (a covering directory) hash, the last commit touching the row's files, the CRs whose `affected_cis` list the row (applied: disposition Approved; pending: Draft, Submitted, Assessed, Deferred), the INSP records naming the row's files (`product_files` inline or block list, `product` items, directory products), and the level by the rule of the tool docstring.
3. Report items 1, 3 to 13 of 05 section 6 from their sources at the revision: header (revision, tracked files, latest reachable `baseline/*` tag, merged CRs, class-CR changes since the tag); baselines (tag object, commit, date, memo present, signature present; pushed only with `--remote`); the CR register from front matter with the missing numbers; the editorial log and the change log of `<since>..<rev>` with rows touched, the `Refs:` trailer and the TV-019 findings; release and audit registers; the tool-validation index copied; the Table 6-1 metrics (MSR-02 copied and banded 10 and 20 %, open CRs and ages, cycle time, commits lacking trailers); the deviations tables copied; waivers (`<a id="W<n>">` anchors and CRs "Approved (waiver)"); open `tbr` objects by `close_by` and open RFA/RID items.
4. Write the report to standard output, a file or `docs/process/configuration-status.md`, or `--check` it against a stored file (exit 1 on a difference), reproducibly (the same revision and date give the same bytes); `--strict` fails (exit 1) on files of no row or two rows; usage errors, an unknown revision, a revision without the CM plan or Table 4-1 exit 2.

Not covered: the judgement a hand CSA adds (sub-row levels such as row 17 "L2 for `sys/`", free-text notes, the "at risk" readings of item 10); `git tag -v` signature verification (only presence is shown); the pushed state without `--remote` (no network command by default).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/csa/`: `build_repo.py` builds a git repository deterministically (fixed names, e-mail and dates; no signing, no hooks, no user configuration) with a 17-row Table 4-1 (`cm-plan-05.md`: a split CR-from row, two Mixed rows, a tools row under accreditation control, a release-gated row, a row without a pathspec), base content tagged `baseline/srr`, 13 commits each exercising a stated case, a branch commit and a `--no-ff` merge; `expected.json` block `csa` holds the answers derived by hand from that plan before the first run; `hand-csa-9fd0962.json` holds the values of the hand CSA issue 1 (`b790eaa`), transcribed by parsing its tables, not by this tool.

| Class | Known answer |
|---|---|
| `Table41ParseTests` (4) | the fixture table: 17 rows, `ignored.py` in parentheses not a pathspec, row 12 without pathspec, row 13's two specs, the split CR-from text, a Mixed class; the real CM plan parses 55 rows or more with `tools/` first in row 28 and no `package.json`; a missing table and a misnumbered table raise the parse error |
| `MatchRuleTests` (4) | explicit pattern over prefix (`docs/reviews/*/baseline-record.md`), longest prefix (`tools/refs/`), `*` across `/`, `[124-8]` class, `*.gitkeep` over `hardware/kicad/`, a tie between two explicit rows and between two equal prefixes, an unmatched path |
| `FrontMatterTests` (2) | CR and record headers; the INSP-016 form (directory product, block list of `product_files`) |
| `FixtureRepoTests` (13) | tracked files 26; the 17 rows (level prefix, file count, records, applied and pending CRs) of `expected.json`; the last commit of 16 rows by commit label; tree and blob hashes equal to `git rev-parse`; the unmatched status note; the baseline row (unsigned, "not checked"); CR-001, CR-002, CR-004 with CR-003 missing; the editorial log (c4); commits lacking trailers c2, c7, c13; MSR-02 12.5 % Yellow; open CRs with ages 6 d; the deviation row; the waiver `#W1`; TBR counts (requirements CDR 1 and PDR 2, TPM PDR 1, hazard controls PDR 1); open log items RID-SRR-001 and RFA-SRR-001 (Answered is open); release and audit registers "None"; `--rev`/`--since` giving 2 commits and 22 files; two runs byte-identical |
| `CliTests` (5) | `--write` then `--check` exit 0, a hand edit then `--check` exit 1 "CHECK FAIL"; `--output`; `--strict` exit 1 "1 file(s) in no row"; exit 2 for a bad date, an unknown revision, a directory that is not a repository, exclusive options, an unreadable `--check` file, an unknown option, and a revision without the CM plan |
| `HandCsaTests` (5, repository content) | at `9fd0962` since `baseline/srr`: 1217 tracked files; for each of the 55 rows the file count equal to the hand value, the tool's hashes a subset of the hand hashes (the hand adds sub-tree hashes for rows 17 and 33; row 26 has no pathspec), the last commit one of the hand's; the two unmatched files; the 26 change-log commits with the hand's rows touched and `Refs:` values; the commits lacking trailers `1535cd5`, `1fe9c1a`, `9fd0962` |

The seeded faults of class B are the `--check` hand edit (exit 1), the `--strict` unmatched file (exit 1), the fixture commits that the change log must flag (c2, c7, c13) and must not flag (c3, c4, c8, c11), and the parse errors.

**Run command:** `bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-018 > docs/cm/tool-validation/evidence/csa-<date>-run<N>.log.txt`; part C is `.venv/bin/python -m unittest discover -v -s tools/tests -p test_csa.py`.

**Pass criteria:** 33 tests run and passed, none skipped (28 fixture tests and the 5 `HandCsaTests`); part A shows every file "unchanged from HEAD" and 0 untracked or modified fixture files.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 12:58 | `b308f8c` (tool `dd9b6fed`, `check_commit_msg.py` `5488dd98`, module `58672f3a`, fixture tree `92fd0e50`, every identity "unchanged from HEAD") | **Pass.** 33 of 33 in 21.4 s, 0 skipped. Transcript `evidence/csa-2026-09-27-run1.log.txt` |

Author's smoke run at `HEAD` `b308f8c` (not a validation run; output kept in the session scratchpad only): 1355 tracked files, 87 commits since `baseline/srr`, the two unmatched plan files of the hand CSA, no ties, 34 commits lacking a mandatory trailer (REFS_MISSING or CR_TRAILER_MISSING), CR-014 missing from the register.

### 4.1 Findings of this validation

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | The level rule differs from the hand issue 1 on 13 rows at `9fd0962`: rows 4, 11, 19, 31, 33, 40, 42, 45, 46, 54 are L1 by the tool (an APPROVED INSP record names a file of the row in `product` or `product_files`) and L0 by hand; row 17 is "L2 (split CR-from)" against the hand's sub-row levels; row 26 has no pathspec (tool "n/a", hand L0 informational); row 35 was absent at `9fd0962` (tool "none (absent)", hand "0 before this issue"). Records list their inputs in `product_files` as well as their products, so a named file is not always a reviewed product. | `HandCsaTests` excludes levels; comparison of the `--json` model with `hand-csa-9fd0962.json` `level_text` (author's development run) | Levels are outside the proposed scope (section 9) until the owner rules which reading 05 section 4.1 intends; the CM function keeps writing levels by hand. Cross item for the lead SE (a record field separating inputs from products, or a 05 amendment) |
| 2 | The hand issue's `Refs:` column is reproduced for all 26 commits, including `9fd0962`, whose `Refs:` line git does not read as a trailer. The count of commits lacking trailers at `b308f8c` is 34 of 87, against a Table 6-1 threshold of 0. | `HandCsaTests.test_change_log`; smoke run above | Reported to the lead SE for the PDR package (05 Table 6-1: each such commit is a RID candidate); `tools/check_commit_msg.py` as a hook (TV-019) prevents new ones |

## 5. Reproducibility

Not required for class B. `FixtureRepoTests.test_output_is_reproducible` shows two runs at the same revision and date give identical output.

## 6. Limitations

1. Levels are rule-derived (finding 1) and are not validated against the hand CSA.
2. Row 28's CR-from event is per tool; the tool marks the row "split" and does not give per-tool levels (item 9 copies the TV index instead).
3. Hazard-control TBRs are counted per control holding a `tbr` field; TBR marks written only in statement text (the hand CSA counted 17 items in 16 controls at `9fd0962`) are not counted. L0 TBRs in statement text (MOE-010) likewise.
4. A CR's cycle time is measured from `date_opened`, because the front matter has no submission date.
5. Signature verification (`git tag -v`) and the remote state are not checked by default.
6. The front-matter reader handles the flat keys, inline lists and block lists used by CR files and records; nested YAML is ignored.
7. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1); hand edits of the generated file are prohibited only from that point (05 section 6).

## 7. Re-validation triggers

- Any change of `tools/csa.py`, `tools/check_commit_msg.py`, `tools/tests/test_csa.py` or `tools/tests/fixtures/csa/` (CM plan section 9.2 step 4).
- A change of the format of 05 Table 4-1 (columns, pathspec notation), of the CR front matter, of the record front matter or of the source files of items 9 to 13.
- A version change of git (TV-009) or of the TV-001 interpreter; a macOS major version change.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (PDR work plan WP-PDR-07).

## 9. Accreditation (owner)

Proposed scope statement **ACC-CSA-001**: "Accredited for purposes 1 to 4 for `tools/csa.py` at git blob `dd9b6fede610f61d033d88222450981315559ed5` with `tools/check_commit_msg.py` at blob `5488dd98b21220261835a74112b49a508865c346`, the TV-001 interpreter and git 2.50.1, except the Level column of item 2 (finding 1), within the limitations of section 6."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after the section 8 review is APPROVED) | | |
