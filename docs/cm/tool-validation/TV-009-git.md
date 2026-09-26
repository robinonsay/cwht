# TV-009: git 2.50.1 (Apple Git-155)

| Field | Value |
|---|---|
| Record | TV-009 |
| Status | **Validated** (2026-09-25). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: object hashes, `git fsck`, tags cited in baseline records, FCA-03, FCA-04, PCA-07) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; SWE-081 (section 5.1.4) |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1 row `git`, section 1.1 row `git`, section 4 (remote, tag signing), section 7 row `git 2.50.1, shasum 6.04` |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| Item | Value | Command |
|---|---|---|
| Version string | `git version 2.50.1 (Apple Git-155)` | `git --version` (also `/usr/bin/git --version`) |
| Binary run | `/usr/bin/git` is the Xcode shim; it runs `/Library/Developer/CommandLineTools/usr/bin/git`, SHA-256 `be4afb2b003904725826250de9fb76567bbacf82323457b5a1ec26706b66bcae` | `xcrun --find git`; `shasum -a 256` |
| Install source | Xcode Command Line Tools, package `com.apple.pkg.CLTools_Executables` version `26.6.0.0.1781586589` | `pkgutil --pkg-info=com.apple.pkg.CLTools_Executables` |
| Installer URL and SHA-256 | Provided by Apple with the OS tools; not archived separately (lock section 7); the binary SHA-256 above identifies the installed version | lock section 7 |
| Repository object format | `sha1` | `git rev-parse --show-object-format` |
| Test module | `tools/tests/test_git_known_answer.py`, git blob `cd8389823bdc34889edc7fc680f1bd8ae4c928a9`, SHA-256 `a588f2d2...42385f`, untracked on 2026-09-25 | `git hash-object` |
| Fixture | `tools/tests/fixtures/git/` (`hello.txt`, `known-answers.json`), 2 files, tree digest `bfc6387c2a299cd20f59ae8718f466896142a1c173d73374c18df18c7e657238`, untracked | TV-002 section 1 digest |

## 2. Purposes covered

1. Compute the blob object id of a file (`git hash-object`), equal to the SHA-1 of `blob <size>\0<content>`.
2. Record a file in a commit so that `git ls-tree` names the same blob, and produce tree and commit ids that are a deterministic function of content, identity and dates (`git rev-parse HEAD^{tree} HEAD`).
3. Detect object corruption: `git fsck --full` exits 0 on a sound repository and non-zero, naming the object, after one byte of a loose object is changed.
4. Report its version (`git --version`) for comparison with the lock.

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/git/hello.txt` and `known-answers.json` (blob `d184c9289729acfe155b2ec99b566eba8063e0ba`, tree `bf3b5c844f9a90e68baee93aa79dba453ac531ab` and commit `779d21e2b520a0b8dd6c60b7106cd68d84645bb9` of a one-file commit with the identity `cwht-kat <kat@cwht.invalid>`, date 2026-09-25T00:00:00+0000, message `known answer`; computed with git 2.50.1 and the blob cross-checked in Python by SHA-1 of the blob header and content).

**Run command** (repository root): `.venv/bin/python -m unittest discover -v -s tools/tests -p test_git_known_answer.py`

The test isolates git from the user's configuration (`GIT_CONFIG_GLOBAL=/dev/null`, `GIT_CONFIG_NOSYSTEM=1`, a temporary `HOME`, fixed author and committer identity and dates), works in temporary repositories, and does not skip when git is absent.

**Pass criteria:** 6 tests pass: the stored blob id equals the Python SHA-1 of the blob object; `git hash-object` on the fixture equals it; `ls-tree HEAD -- hello.txt` in the temporary repository reads `100644 blob <id>\thello.txt`; tree and commit ids equal the stored values; `fsck --full` exits 0, then non-zero with the blob id in its output after one byte of the zlib stream of the loose object is inverted; `git --version` equals the observed version in the lock's git row.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `HEAD` `28e49e6`; test and fixture untracked, identities of section 1 | 6, 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same, after the lock edit of 2026-09-25 (the git row's version cell unchanged) | 6, 0 skipped | pass |

Output excerpt (run 2): `Ran 6 tests; failures+errors 0; skipped 0; per class {'GitKnownAnswerTests': 6}; PASS`. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`.

## 5. Reproducibility

Not required for class B. The tree and commit known answers are themselves a reproducibility check: identical content, identity and dates gave identical ids in both runs.

## 6. Limitations

1. Covered: loose objects, one blob, one tree, one commit, SHA-1 object format. Not covered: packed objects (`git gc` output), annotated tag creation and `git verify-tag` (the baseline mechanism, charter section 8; tags are unsigned until the owner configures a key, lock section 4), `git ls-remote` and push to `origin`, the SHA-256 object format. Baseline records that cite these operations cite developer evidence until this record is extended; the owner may extend purposes before `baseline/srr` is tagged.
2. The test and fixture are untracked on 2026-09-25; the result carries to a commit only if they are committed unchanged.
3. `test_version_equals_the_lock` reads `tools/toolchain.lock.md`; a lock edit that changes the git row's format fails the test without a git change.
4. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the git version or binary SHA-256 (an Xcode Command Line Tools update, `softwareupdate`), or of the macOS major version (CM plan section 9.2 step 4).
- A change of the test module or fixture.
- A change of the repository object format.
- A defect found in git's output (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-GIT-001**: "Accredited for purposes 1 to 4 at git 2.50.1 (Apple Git-155), binary SHA-256 `be4afb2b...66bcae`, SHA-1 object format, loose objects; tags, packs and remotes excluded (limitation 1)."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
