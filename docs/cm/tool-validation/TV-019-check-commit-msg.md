# TV-019: tools/check_commit_msg.py (git blob 5488dd98, commit 86ff3b0)

| Field | Value |
|---|---|
| Record | TV-019 |
| Status | **Validated** 2026-09-27 (known-answer run 1 at commit `b308f8c`: 13 tests passed, 0 skipped). Not installed as the `commit-msg` hook (owner action OA-TV019-1, section 9). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: its findings are review evidence for the 05 section 4.5 "Checks" row and the Table 6-1 trailer metric) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8) through CM plan section 9; CM plan section 4.5 rows "Commit message", "Merges to main" and "Checks"; Table 6-1 row "Commits lacking mandatory trailers" |
| Due | PDR (CM plan section 13 PDR row: "installed as the `commit-msg` hook") |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/check_commit_msg.py`; section 1.2 row `tools/check_commit_msg.py`; section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 1a) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/check_commit_msg.py` | git blob `5488dd98b21220261835a74112b49a508865c346`, SHA-256 `8e7e981d5764f3d21439b849208f7a848706e9a87b788329a5e10eb3dadf412c`, 284 lines | committed in `86ff3b0` (commit note of TV-015 section 1); equal at `b308f8c` |
| `tools/csa.py` (Table 4-1 reader and matching rule; TV-018) | git blob `dd9b6fede610f61d033d88222450981315559ed5` | committed in `b308f8c` |
| `tools/tests/test_check_commit_msg.py` | git blob `d8595b98493088523e448b29e6d99bd2242e9998`, SHA-256 `e87d78dc7a5f83313ffdb5c51484a5d12f7136515222dbeb7e0f71c7aaad2d81`, 13 tests | committed in `86ff3b0` |
| `tools/tests/fixtures/csa/` (shared with TV-018; block `check_commit_msg` of `expected.json`) | git tree `92fd0e50c0d61bf2c8e71b9e6b7dc518c6733d30`, digest `cdc66c09e8b6857543abf762ff462fe7584dab42514ff80d97ef5e9cc06ba872` | committed in `86ff3b0` |
| Runtime | TV-001 interpreter (Python 3.13.5), standard library; git 2.50.1 (TV-009), whose `interpret-trailers --parse` reads the trailers | lock sections 1 and 2 |

**Install source:** the repository (CM plan Table 4-1 row 28).

## 2. Purposes covered

1. Check a commit message's first line against 05 section 4.5: `<type>(<scope>): <summary>` with one of the 11 types, and `merge(...)` exactly on merge commits (rule SUBJECT).
2. Check the trailers as git parses them: `Refs:` present when the commit touches a file of a Table 4-1 row (REFS_MISSING); `Refs:` naming at least one identifier of 05 section 4.5 or charter section 6 (REFS_UNRECOGNIZED); `CR:` values of the form CR-NNN (CR_ID_BAD); `CR:` or `Editorial:` present when the commit touches a class-CR row whose CR-from event (a reachable `baseline/<gate>` or `release/FW-*` tag) occurred before the commit, a `merge(CR-NNN)` subject counting as the CR, and for the tools row the tool files that an Accredited row of the tool-validation index names (CR_TRAILER_MISSING); warnings for Mixed rows (MIXED_ROW) and rows whose CR-from names two gates (SPLIT_CR_FROM).
3. Apply these checks in three modes with exit 0 (no FAIL), 1 (a FAIL) or 2 (usage or git error): hook mode (message file; staged files; Table 4-1 as staged; tags as of HEAD), audit mode (`--range A..B`, every commit against its first parent, Table 4-1 at B) and message-file mode (`--message-file`, `--files`, `--parent`).

Not covered: `Co-Authored-By:` (not decidable from git); whether a `CR:` names an Approved CR (the merge rule of 05 section 4.5 is checked on the CR file by Claude before the merge); the semantic correctness of a Mixed row's parts (a reviewer decides on the WARN).

## 3. Known-answer test

**Fixture:** the repository of `tools/tests/fixtures/csa/build_repo.py` (TV-018 section 3) and the block `check_commit_msg` of `expected.json`: for each of c1 to c13, the branch commit and the merge, the FAIL and WARN rules derived by hand from the commit plan (`build_repo.py` states the case each commit exercises) before the first run.

| Class | Known answer |
|---|---|
| `RangeTests` (3) | `--range baseline/srr..HEAD`: the findings of all 15 commits equal `expected.json` (c2 and c13: REFS_MISSING and CR_TRAILER_MISSING, c13 because its `Refs:` line is separated from the trailer block by a blank line; c5 SPLIT_CR_FROM; c6 MIXED_ROW; c7 CR_TRAILER_MISSING on the accredited `tools/trace.py`; c8 passes on the unaccredited tool; c9 SUBJECT only, its file in no row; c10 REFS_UNRECOGNIZED; c11 passes, no `release/FW-*` tag; c12 CR_ID_BAD; the merge `merge(CR-002)` passes); exit 1; a clean range exits 0; the `check_commit` API gives the same rows and findings |
| `HookTests` (5) | in a clone with a staged change to row 2: no trailers fails (REFS_MISSING, CR_TRAILER_MISSING); `Refs:` with `CR:` passes; comment lines are ignored; a blank line before `Co-Authored-By:` makes the `Refs:` line a non-trailer and fails; message-file mode with `--files` and `--parent` warns MIXED_ROW |
| `SubjectTests` (2) | the 11 types pass; `Docs(x): y`, `docs: no scope`, `docs(x):missing space`, `wip(x): y`, `docs( x): y`, `Status note` fail; `merge(...)` passes on a merge, fails on a non-merge; `docs(...)` fails on a merge |
| `RefsTests` (1) | 29 identifier forms recognized (REQ, TC, ICD, ADR, TS, RSK, HZ, NCR, RFA, RID with TRR-D<n>, SI, TV, CR, INSP, MSR, OQ, ACC, WP-SW, SW-NN sprint, FW-v with rc, HW-MB and ME-ENC releases, CWHT-A, review names, TPM, MOE); `WP-PDR-07`, `RSK ids`, `CR-7`, `baseline/srr` not recognized |
| `UsageTests` (1) | exit 2 for no mode, two modes, `--files` without `--message-file`, an unreadable message file, an unknown revision, an unknown option |
| `RepositoryTests` (1, repository content) | `--range baseline/srr..9fd0962` fails REFS_MISSING on exactly `1535cd5`, `1fe9c1a`, `9fd0962`, the three commits of the hand CSA issue 1 trailer metric (`b790eaa` section 10), and reports no CR_TRAILER_MISSING, as that issue states |

**Run command:** `bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-019 > docs/cm/tool-validation/evidence/check-commit-msg-<date>-run<N>.log.txt`; part C is `.venv/bin/python -m unittest discover -v -s tools/tests -p test_check_commit_msg.py`.

**Pass criteria:** 13 tests run and passed, none skipped (12 fixture tests and the repository test); part A shows every file "unchanged from HEAD".

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 12:58 | `b308f8c` (tool `5488dd98`, `csa.py` `dd9b6fed`, module `d8595b98`, fixture tree `92fd0e50`, every identity "unchanged from HEAD") | **Pass.** 13 of 13 in 8.1 s, 0 skipped. Transcript `evidence/check-commit-msg-2026-09-27-run1.log.txt` |

### 4.1 Findings of this validation

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | The five WP-PDR-07 tools were committed in `86ff3b0` by another session's commit, which took the files staged in the shared git index; that commit's message describes a CR-011 review and has no `Refs:`. The hook, once installed, fails such a commit only for its missing `Refs:`; it cannot see that the staged files belong to another author. | `git show --stat 86ff3b0`; provenance note in the message of `c90df2d` | Concurrent sessions stage and commit with explicit paths (`git commit -o <paths>`, used for every later WP-PDR-07 commit). Cross item for the lead SE: a deviation entry for `86ff3b0` (05 section 4.5 "Commit message") and the rule for parallel workflows |
| 2 | At `b308f8c` the audit mode fails 34 of the 87 commits since `baseline/srr` for a missing trailer (TV-018 finding 2). | TV-018 section 4 smoke run | Hook installation (OA-TV019-1) stops new ones; the existing ones are RID candidates at PDR (05 Table 6-1) |

## 5. Reproducibility

Not required for class B. The fixture repository is built with fixed dates and identities, so the commit hashes, and with them every finding, are the same on every build.

## 6. Limitations

1. Mixed rows and rows with a split CR-from produce warnings, not failures (section 2); a reviewer decides.
2. The accredited-tool list for the tools row is read from the index of `docs/cm/tool-validation/README.md` at the commit's parent (rows whose status holds "**Accredited**", backticked `tools/` paths of the tool column); a tool named only in prose is not seen.
3. Hook mode strips lines starting with `#` as git's default "strip" cleanup does for an editor message; a message given with `-m` that starts a line with `#` keeps it in git but not in this check.
4. The commit being made is compared with HEAD as its parent; for a merge in progress the `MERGE_HEAD` file marks it as a merge, and its files are the staged ones.
5. The hook is not installed by this record; until the owner installs it (OA-TV019-1), the check runs only in audit mode at reviews (05 section 4.5 "Checks").
6. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).

## 7. Re-validation triggers

- Any change of `tools/check_commit_msg.py`, `tools/csa.py`, `tools/tests/test_check_commit_msg.py` or `tools/tests/fixtures/csa/` (CM plan section 9.2 step 4).
- A change of the 05 section 4.5 rules, of the Table 4-1 format, of the charter section 6 identifier schemes, or of the tool-validation index format.
- A version change of git (TV-009; the trailer parser) or of the TV-001 interpreter; a macOS major version change.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (PDR work plan WP-PDR-07).

## 9. Accreditation and hook installation (owner)

Proposed scope statement **ACC-COMMITMSG-001**: "Accredited for purposes 1 to 3 for `tools/check_commit_msg.py` at git blob `5488dd98b21220261835a74112b49a508865c346` with `tools/csa.py` at blob `dd9b6fede610f61d033d88222450981315559ed5`, the TV-001 interpreter and git 2.50.1, within the limitations of section 6."

**Owner action OA-TV019-1 (hook installation; a standing repository configuration, so the owner's to make).** After accreditation, from the repository root:

```
printf '#!/bin/sh\nexec .venv/bin/python tools/check_commit_msg.py "$1"\n' > .git/hooks/commit-msg
chmod 755 .git/hooks/commit-msg
```

The hook then rejects (exit 1) every commit with a FAIL finding, for every session on this machine; `git commit --no-verify` bypasses it and is itself a 05 section 4.5 departure to be logged.

| Decision | Date | Recorded by |
|---|---|---|
| Accreditation: pending (owner, after the section 8 review is APPROVED) | | |
| OA-TV019-1 hook installed: pending | | |
