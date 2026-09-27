# Independent baseline check: `docs/reviews/SRR/baseline-record.md`

**Verdict: NOT READY FOR TAG.** The record is accurate against the repository. Every hash, path, tool result and state it reports reproduces. But the record itself states, correctly, that the tag preconditions are not met, and this check confirms that the blockers still stand.

| Field | Value |
|---|---|
| Date | 2026-09-26 |
| Checker | Independent reviewer agent (baseline check role). It did not author the baseline record, edited no product and no record, and wrote only this file (charter section 2 and section 11 rule 4; CM plan 05 section 4.4 step 4) |
| HEAD checked | `e49a5a873bfa7457511848e0013d73faff86a3a8` ("docs(srr): baseline record status at f3e8801, candidate for R, tag held"). This commit changes only `docs/reviews/SRR/baseline-record.md` against `f3e8801` (`git diff --stat f3e8801 HEAD`: 1 file) |
| Record revision checked | Section 0.2 (candidate for R at `f3e880155e2c222803c3c05e81ea405db5165f86`), which supersedes sections 0 and 0.1 for current status |
| rustos | `git -C /Users/robinonsay/rust/rustos rev-parse master` = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (ref read only). Sources were read only from a clean `git archive 2ec64c0` export in the session scratchpad; the owner's rustos working tree was not read or modified |
| Search first | `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: baseline record independent check, `git ls-tree`, readiness_met, verdict, SRR checklists) ran before any `grep`. `grep` was used afterwards only to pin lines |
| Downloads or installs | None. Every command below is read-only or writes to the scratchpad. `RUSTUP_AUTO_INSTALL=0` and `HOMEBREW_NO_AUTO_UPDATE=1` were set for the rustup and brew observations |

This is a pre-R check. CM plan 05 section 4.4 step 4 and record section 9 require the check again at R, with every hash taken by `git ls-tree R -- <path>`.

## 1. Checks, commands and results

| # | Check | Command | Result | Pass |
|---|---|---|---|---|
| C1 | Every CI path in sections 2a, 2b and 2c exists, and each recorded hash equals `git rev-parse <commit>:<path>` at the stated commit `f3e8801` and at HEAD | A Python loop over 68 path and hash pairs, running `git rev-parse f3e8801:<path>` and `git rev-parse HEAD:<path>` | 68 of 68 exist and equal at both commits. That covers 60 blobs and 3 trees in section 2a (`docs/conops/`, `docs/requirements/sys/`, `docs/templates/`), 10 blobs in section 2b, and 11 tool blobs in section 2c. The short blobs agree too: `firmware/unsafe-audit.md` `18ef484b` and `expectations.json` `52b6cf5e` | Yes |
| C2 | Cited commits exist, and the "last changed at" claims hold | `git cat-file -e <c>^{commit}` for 21 cited commits; `git log -1 --format=%h -- <path>` for 13 paths | All 21 commits exist. The last changes match the record: 07 `e34a27b`, charter `6ea6b1d`, 05 `0834da2`, lock `eb52766`, unsafe audit `5792350`, L1 `cd61450`, `traceability.py` `c774851`, `complexity_gate.py` `e34a27b`, `sw_gate.sh` `37ae576`, expectations `b087a9f`, ConOps and concept `dd3372c`. `5792350` changes the lock and `firmware/unsafe-audit.md` in one commit, as CR-004 requires | Yes |
| C3 | Section 1 counts | `git ls-tree -r --name-only f3e8801 \| wc -l`; `git ls-tree f3e8801 docs/templates/`; JSON counts | 1147 tracked files. `docs/templates/` has 22 entries (21 files plus the row 9 schema). There are 190 L1 requirements (188 Draft, 2 Closed) and 113 TC-SYS cases | Yes |
| C4 | Decision memo row | `grep` of the memo front matter; `git show 0bcea39` | `signed: 2026-09-26` is added at `0bcea39`, and later memo commits (`ffd4b97`, `7d37d18`, `4b6c96c`) only amend. `disposition: Approved with liens`; `baseline_tag: null` | Yes |
| C5 | `validate_docs.py` | `.venv/bin/python tools/validate_docs.py` | exit 0, 50 passed, 0 failed | Yes |
| C6 | `traceability.py` | `.venv/bin/python tools/traceability.py --report-only`, then `git checkout -- docs/vv/traceability-report.md docs/vv/traceability.json` | exit 0; 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148). The rendered files were restored and the working tree is clean | Yes |
| C7 | `render_risk.py` | `cd /Users/robinonsay/rust/cwht && .venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | exit 0; 65 risks, 159 candidates, 0 warnings, `register.md` current | Yes |
| C8 | `render_rmm.py` | `.venv/bin/python tools/render_rmm.py --check` | exit 0; 100 rows, `rmm.md` current | Yes |
| C9 | `render_compliance.py` | `.venv/bin/python tools/render_compliance.py --check` | exit 0; validation passed, rendered file current | Yes |
| C10 | Tool unit tests | `cd /Users/robinonsay/rust/cwht && .venv/bin/python -m unittest discover -s tools/tests` | 415 tests run, OK | Yes |
| C11 | `git fsck` | `git fsck --full` | exit 0 | Yes |
| C12 | AL-4 venv pins | `tools/requirements.txt` (sorted, comments removed) diffed against `.venv/bin/pip freeze` (sorted) | Identical: 35 pins | Yes |
| C13 | SRR records: `readiness_met` and open Majors | The front matter of all 30 files in `docs/reviews/SRR/checklists/`, read by regex; for each APPROVED record, every table row with a Major finding marked Open, followed to its later closure | 30 records, all with `readiness_met: true`. 27 are APPROVED, and each Major marked Open in an earlier iteration table is closed by a later section. Pinned examples: INSP-009 finding-11 (line 451), INSP-002 finding-23 and finding-24 (lines 536 and 537), INSP-001 finding-14 (line 520), INSP-003 finding-4 and finding-6 (lines 761 and 781), INSP-015 F-02 (line 608). **3 records are NEEDS CHANGES, each with an open Major:** INSP-010 finding-21 (`software-plan-07.md` line 551, Open, owner decision B9), INSP-018 finding-10 (`software-plan-07-software-assurance.md` line 489), and INSP-016 F-01 (`fw-b0-toolchain-proof.md` line 525, Open) | **No** (the repository fails the check; the record reports it correctly) |
| C14 | The lock pins rustos `2ec64c0` | `grep -n` of `tools/toolchain.lock.md` (blob `8ab0218a`) | Section 3 rustos row (line 215) reads `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`. Change-log line 283 records the move from `c54d35a` (CR-004). This equals rustos `master` | Yes |
| C15 | `firmware/unsafe-audit.md` matches a fresh `tools/unsafe_audit.py` run on a clean export of rustos `2ec64c0` | `git -C /Users/robinonsay/rust/rustos archive 2ec64c0 \| tar -x -C <scratch>/bcheck/rustos`; `git -C /Users/robinonsay/rust/cwht archive HEAD \| tar -x -C <scratch>/bcheck/cwht`; in the cwht export, `tools/unsafe_audit.py --check`, then `--write --audit-file <scratch>/bcheck/fresh-audit.md`; `diff` against the committed file | `--check` exit 0: 37 sites, 0 without SAFETY, 0 in forbidden crates, 37 unsigned (a note, not a failure before CDR). `--write` exit 0. The fresh list is byte-identical to the committed one: sha256 `7d15d8aa...ab8b08` for both, and `git hash-object` of the fresh file = `18ef484bf050797e9493d68071efdc0259d423a6`, the HEAD blob | Yes |
| C16 | TC-SW-TOOL-001-r5 artifact integrity | Python: sha256 of every `artifacts:` entry in the run 5 front matter, compared with the recorded value; `firmware_elf_sha256` compared with `cwht-app.elf`; a directory listing for unlisted files | 20 of 20 artifacts exist and every sha256 matches. `firmware_elf_sha256` equals `cwht-app.elf`. No file in the directory is unlisted | Yes |
| C17 | TC-SW-TOOL-001-r5 records a gate exit 0 | The front matter, and the tail of `sw-gate-full.txt` and `sw-gate-keep-going.txt` | **Gate exit 1.** `result: Blocked`, `credit: false`. `sw-gate-full.txt` line 128: `sw_gate exit status: 1` (FAIL at G5 complexity). `sw-gate-keep-going.txt` lines 222 and 223: 2 steps failed (B9 G5 complexity CS-38 `cwht-app::main`; B11 G5 Miri), exit status 1. `docs/vv/reports/` holds runs r1 to r5 only, so no run with exit 0 exists | **No** (the repository fails the check; the record reports it correctly) |
| C18 | P8 repository protection confirmed | `git log -1 -- docs/reviews/SRR/minutes.md`; `grep -n -i 'ruleset\|protection'` of the minutes | The minutes were last changed at `dd39332`. The only ruleset line is the item 6 ruling (line 122), and no owner confirmation is transcribed. `gh` was not used | **No** |
| C19 | P9 L1 status | JSON count over `docs/requirements/sys/requirements.json` | 188 Draft, 2 Closed. The status change has not been made | **No** |
| C20 | P10 push state | `git rev-list --count origin/main..f3e8801` and `..HEAD` | 69 at `f3e8801`, as the record states, and 70 at HEAD. The local `origin/main` is `7647516`. No network command was run | Not done; this is a post-tag step, correctly recorded |
| C21 | Unlogged CR-004 departure and class confirmations | `docs/cm/deviations.md` entries; front matter and sections 6 and 7 of CR-004 and CR-005 | The deviations log holds entry 1 only (CR-002, last changed at `d992052`), and `CR-004` appears 0 times in it. CR-004 is `status: Dispositioned`, `class: I`. Its section 6 reads "Required (Class I). Not yet performed" (line 97), and its section 7 reads "Class confirmed: Pending" (line 110). CR-005 has `class: II` and "Class confirmed: Pending" (line 93) | **No** (the departure is unlogged, as the record states) |
| C22 | RFA/RID states named in section 0.2 | `docs/reviews/SRR/rfa-rid-log.json` (last changed at `4b6c96c`) | RID-SRR-003 Minor, Open. RID-SRR-010 Minor, Answered. RFA-SRR-008 Routine, Open | Yes (these match the record, and none blocks the tag) |
| C23 | Close-out items 2, 3 and 12 | `rustup --version`; `grep auto_self_update ~/.rustup/settings.toml`; `rustup component list --toolchain nightly-2026-08-24 --installed`; `brew list --pinned`; the raw log in the scratchpad | rustup 1.29.1 (`d95a37b6a 2026-08-13`); `auto_self_update = "disable"`; `rust-src` and `miri-aarch64-apple-darwin` are installed on `nightly-2026-08-24`; `python@3.13` is pinned; `closeout-installs-2026-09-26.txt` exists (4131 B) | Yes |

## 2. Precondition status confirmed at HEAD `e49a5a8`

| # | Record claim (section 0.2) | Confirmed state | Agrees |
|---|---|---|---|
| P1 | Not met: INSP-010, INSP-018 and INSP-016 hold open Majors | Not met (C13) | Yes |
| P2 | 4 of 5 closed; INSP-016 F-01 Open | INSP-016 F-01 Open (C13, line 525) | Yes |
| P3 | Met: validate 50 of 50, 415 tests OK | Met (C5, C10) | Yes |
| P4 | Met: 0 violations, 2 warnings | Met (C6) | Yes |
| P5 | Met except row 2, 07 (INSP-010 and INSP-018 NEEDS CHANGES) | Not met for 07 (C13) | Yes |
| P6 | Not met: CR-004 applied; run 5 gate exit 1 (B9, B11) | Not met (C14, C15, C16, C17) | Yes |
| P7 | Met | No product change since the records' APPROVED re-issues. The blobs agree (C1) | Yes |
| P8 | Not met: owner confirmation pending | Not met (C18) | Yes |
| P9 | Not done: 188 Draft | Not done (C19) | Yes |
| P10 | Not done: 69 ahead | 69 at `f3e8801`, 70 at HEAD (C20) | Yes |
| CR-004 departure | Unlogged; blocks the tag | Unlogged (C21) | Yes |

## 3. Defects blocking the tag (repository state; the record reports each one)

1. **P1 and P5: three open Major findings.** INSP-010 finding-21 and INSP-018 finding-10 raise the same 07 defect: the CS-19 main loop of `cwht-app::main` has no CS-38 allowance after CR-005. INSP-016 F-01 is the FW-B0 gate not exiting 0. Decision memo section 9 condition 2 forbids converting these into liens. Closure: the owner decides B9 (CR-005 section 9) and B11 (the G5 Miri scope); the ruled CR is applied, with a TV-012 re-validation and its independent review; then the INSP-010, INSP-018 and INSP-016 delta re-issues.
2. **P2 and P6: no TC-SW-TOOL-001 run with gate exit 0.** Run 5 exits 1 (C17). A full gate run with exit 0 on clean `git archive` exports of cwht and rustos `2ec64c0` is required, filed as run 6 with sha256 artifacts.
3. **CR-004 departure unlogged (CM plan 05 section 4.4 step 1: "nothing is tagged on an unlogged departure").** Closure: either a numbered `docs/cm/deviations.md` entry by the deviations log owner, or the independent review of CR-004 section 4 recorded in CR-004 section 6. In addition, the owner confirms the classes of CR-004 and CR-005. If CR-005 becomes Class I, it carries the same departure.
4. **P8: repository protection not confirmed.** The owner sets the item 6 rulesets and confirms in chat, and Claude transcribes the confirmation into the minutes.
5. **P9: L1 status change not made.** 188 L1 requirements are Draft. The status-only change and the INSP-003 re-issue come in the commit before R, after P1 closes.

## 4. Observations on the record itself (not tag blockers; Minor, lien under the convergence rule, charter section 4 item 3)

- **OBS-1 (Minor).** The paragraph "Which commit is R" in section 0.2 lists "P1, P2, P6, P8 and P9" as not met. It omits P5, which the section 0.2 table itself rates "Met except row 2, 07", so P5 is not met. The table is correct and the list is incomplete. The fix belongs to the record author at R.
- **OBS-2 (information).** At R, every section 2 hash must be re-taken against the parent of R, and this check must be repeated by `git ls-tree R -- <path>` (record section 9 row 2). At least `docs/requirements/sys/requirements.json`, `requirements.md` and the `docs/requirements/sys/` tree will change with P9, and 07 and `tools/complexity_gate.py` will change with the B9 route.

No hash, path, tool result or count in the record was found wrong.

## 5. Verdict

**NOT READY FOR TAG.** The record at HEAD `e49a5a8` agrees with the repository in every checked hash, path, tool result and count. The tag is still blocked by defects 1 to 5 of section 3: open Majors INSP-010 finding-21, INSP-018 finding-10 and INSP-016 F-01; no gate exit 0 (TC-SW-TOOL-001 run 5 exits 1); the unlogged CR-004 departure; P8 unconfirmed; and P9 not done. `baseline/srr` must not be applied until these close and this check is repeated at R.

---

# Independent baseline check 2, 2026-09-27: `docs/reviews/SRR/baseline-record.md` section 0.3

**Verdict: NOT READY FOR TAG.** Section 0.3 of the record agrees with the repository in every hash, path, tool result, count and state checked below. Defects 1 to 5 of the first check (2026-09-26, above) are cleared. One precondition stays unmet, exactly as section 0.3 itself states: P5 for 07, because the INSP-010 record still reads `verdict: NEEDS CHANGES` and `assurance_verdict: NEEDS CHANGES`. HEAD `4c4e0d1` is not R, and no commit is R yet. The first check above is kept unchanged as history.

| Field | Value |
|---|---|
| Date | 2026-09-27 |
| Checker | Independent reviewer agent (baseline check role, a new invocation). It did not author the baseline record, edited no product and no record, and wrote only this section (charter section 2 and section 11 rule 4; CM plan 05 section 4.4 step 4) |
| HEAD checked | `4c4e0d16c7cd7f9f5e61a723bca657a93f16a26a` ("docs(srr): baseline record section 0.3 at 49104a5, not R ..."). `git diff --stat 49104a5 HEAD` shows 1 file, `docs/reviews/SRR/baseline-record.md` (+136 lines). So every product blob at HEAD equals its blob at `49104a5`, the commit section 0.3 names |
| Record revision checked | Section 0.3 (status at `49104a5d9429b7e78fbd3a33471b76976996eddb`, candidate for R). It supersedes section 0.2 for current status |
| rustos | `git -C /Users/robinonsay/rust/rustos rev-parse master` = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (ref read only). Sources were read only from a clean `git archive 2ec64c0` export in the session scratchpad (`.../scratchpad/bc3/rustos`). The owner's rustos working tree was neither read nor modified |
| Search first | `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: INSP-010 software plan 07 record verdict, assurance_verdict, X-9 copy) ran before any `grep`. `grep` was used afterwards only to pin lines |
| Downloads or installs | None. Every command was read-only or wrote only to the scratchpad. `docs/vv/traceability-report.md` and `docs/vv/traceability.json` were restored with `git checkout` after the `--report-only` run, and `git status --short` was clean afterwards |

## 1. Checks, commands and results

| # | Check | Command | Result | Pass |
|---|---|---|---|---|
| D1 | Every CI path in section 0.3.3 exists, and each recorded hash equals `git rev-parse <commit>:<path>` at the stated commit `49104a5` and at HEAD | A Python loop in the scratchpad (`bc3/hashes.py`) parses every table row of section 0.3.3 and the informational paragraph, then runs `git rev-parse 49104a5:<path>` and `git rev-parse HEAD:<path>`. The firmware row, both split rows and the cited records were checked by direct `git rev-parse` | 68 of 68 parsed pairs are equal at both commits. They cover the rows for 1 to 3, 5 to 7, 9 (11 schemas), 17, 27, 51, 52 and 53, which include the trees `docs/conops/`, `docs/requirements/sys/` and `docs/templates/`, the 10 informational items, and the 12 controlled tool blobs of row 28. Firmware tree `de1c87cb` and `firmware/unsafe-audit.md` `18ef484b` are equal. So are the records section 0.3.3 cites: decision memo `4c09ef55`, minutes `5a5f4ed6`, RFA/RID log `906d4a19`, deviations log `bcb91b5c` and TC-SW-TOOL-001-r6 `8d12b383` | Yes |
| D2 | Short blobs and "changed at" claims in sections 0.3.2 to 0.3.4 | `git rev-parse HEAD:<path>` and `git log -1 --format=%h -- <path>` for each cited file | 07 `bfe05f43` at `106bc3a`; CR-001 `0f4cca4c` at `4364ebb`; CR-002 `c007177f`, CR-004 `b9fc9510` and CR-005 `9b0129ef`, each last changed at `8b86c16`; `tools/complexity_gate.py` `ddf10798` at `106bc3a`; lock `04819139` and `tools/sw_gate.sh` `29a37127` at `495a0c3`; `tools/traceability.py` `12de3545` at `c774851`; the TV-012 record at `0da559a` hashes to `bd99a11d`; L1 at `61a3cb7`; the run 6 report at `68a44ed`; the deviations log at `bb2485e` (preceded by `31272e0`); the RFA/RID log at `305a11e`. All 33 cited commits exist (`git cat-file -e <c>^{commit}`), and `f3e8801..49104a5` has 19 commits, as stated | Yes |
| D3 | `validate_docs.py` | `.venv/bin/python tools/validate_docs.py` | exit 0; 50 passed, 0 failed, 50 checked | Yes |
| D4 | `traceability.py` | `.venv/bin/python tools/traceability.py --report-only`, then `git checkout -- docs/vv/traceability-report.md docs/vv/traceability.json` | exit 0; 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148). The rendered files were restored | Yes |
| D5 | `render_risk.py` | `cd /Users/robinonsay/rust/cwht && .venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | exit 0; 65 risks, 159 candidates, 0 warnings, `register.md` current | Yes |
| D6 | `render_rmm.py` | `.venv/bin/python tools/render_rmm.py --check` | exit 0; 100 rows (FC 75, T 17, NA 8), `rmm.md` current | Yes |
| D7 | `render_compliance.py` | `.venv/bin/python tools/render_compliance.py --check` | exit 0; validation passed, rendered file current | Yes |
| D8 | Tool unit tests | `cd /Users/robinonsay/rust/cwht && .venv/bin/python -m unittest discover -s tools/tests` | 424 tests run, OK | Yes |
| D9 | `git fsck` | `git fsck --full` | exit 0; 6 dangling blobs and 4 dangling commits, no errors | Yes |
| D10 | AL-4 venv pins and tracked files | `tools/requirements.txt` (comments and blank lines removed, sorted) diffed against `.venv/bin/pip freeze` (sorted); `git ls-files \| wc -l` | Identical, 35 pins; 1177 tracked files | Yes |
| D11 | SRR records: `readiness_met` and open Majors | Front matter of all 30 files in `docs/reviews/SRR/checklists/`, read by regex. Then `grep -n -E '\| *Major *\| *(Open\|Reopened)'` over the records, and each hit followed to its later state | 30 records; all 30 have `readiness_met: true` and `reviewer_verdict: APPROVED`. The 7 table rows that read Major Open are each closed by a later section: INSP-009 finding-11 (`classification-03-...md` line 418, Verified), INSP-001 finding-14 (`expectations.md` line 520, Verified), INSP-002 finding-23 and finding-24 (`conops-and-concept.md` lines 536 and 537), INSP-010 finding-21 (`software-plan-07.md` line 677, Verified by `106bc3a`), INSP-015 F-02 (`tool-validation-tv-001-to-tv-010.md` line 702, Closed). INSP-016 F-01 is Closed (Verified) in delta 2 (`fw-b0-toolchain-proof.md` lines 614 and 657). INSP-018 finding-10 is closed by `106bc3a` (`software-plan-07-software-assurance.md` line 619). **No open Major.** 29 records read `verdict: APPROVED`. **INSP-010 reads `verdict: NEEDS CHANGES` and `assurance_verdict: NEEDS CHANGES`** (last changed at `c8a5143`). Its completion criteria hold the record verdict until the paired INSP-018 is APPROVED, and its cross item X-9 names the copy. INSP-018 now reads `verdict: APPROVED` and `assurance_verdict: APPROVED` (`738da03`) | **No** (the P5 gap, as the record states) |
| D12 | The lock pins rustos `2ec64c0` | `sed -n 215p tools/toolchain.lock.md` (blob `04819139`) | The section 3 rustos row carries `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`, which equals rustos `master`. Change-log line 283 records the CR-004 move from `c54d35a` | Yes |
| D13 | `firmware/unsafe-audit.md` equals a fresh `tools/unsafe_audit.py --write` on a clean export of rustos `2ec64c0` | `git -C /Users/robinonsay/rust/rustos archive 2ec64c0 \| tar -x -C <scratch>/bc3/rustos`; `git archive HEAD \| tar -x -C <scratch>/bc3/cwht`; in the cwht export, `tools/unsafe_audit.py --check`, then `rm firmware/unsafe-audit.md` and `tools/unsafe_audit.py --write` (default roots `../rustos/api` and `../rustos/firmware/pico2`, resolved to the export); `cmp` against the committed file | `--check` exit 0: 37 sites, 0 without SAFETY, 0 in forbidden crates, 37 unsigned (a note, not a failure before CDR). `--write` exit 0. The regenerated file is byte-identical to the committed one: sha256 `7d15d8aa...5ab8b08` for both, and `git hash-object` = `18ef484bf050797e9493d68071efdc0259d423a6` | Yes |
| D14 | TC-SW-TOOL-001-r6 records a gate exit 0, and its artifacts match their sha256 | Python: sha256 of every `artifacts:` entry in the run 6 front matter against the recorded value; `firmware_elf_sha256` against `cwht-app.elf`; a directory listing for unlisted files; `grep` of the tail of both gate logs | `result: Pass`, `credit: false`, `source_commit: bb2485e`, lock blob `04819139`. 22 of 22 artifacts exist and every sha256 matches. `firmware_elf_sha256` equals `cwht-app.elf`. No file in the directory is unlisted (22 tracked). `sw-gate-full.txt` lines 205 and 206: `sw_gate: PASS (G0 to G6)`, `sw_gate exit status: 0`. `sw-gate-keep-going.txt` lines 191 and 192: the same | Yes |
| D15 | `docs/cm/deviations.md` has no open entry without a closure or an RFA | Read of the log (blob `bcb91b5c`) | 4 entries. Entries 2 to 4 cite RFA-SRR-008, and correction entry 4 brings entry 1 under RFA-SRR-008. The Closures table closes entries 1 to 4 on 2026-09-27, citing CR section 6 at `8b86c16`. No entry is open | Yes |
| D16 | CR states in section 0.3.4 | Front matter, section 6 and section 7 of CR-001, CR-002, CR-004 and CR-005 | CR-001 `class: II`. CR-002, CR-004 and CR-005 have `class: I`, `status: Dispositioned`, and section 6 "Concur with comments", with Minor findings only. The section 7 "Class confirmed" rows for CR-004 (line 110) and CR-005 (line 107) cite the owner's item C at `786822a` | Yes |
| D17 | The L1 requirements are Active (P9) | JSON count over `docs/requirements/sys/requirements.json` (blob `f128235e`, last changed at `61a3cb7`) | 190 items: 188 Active, 2 Closed (retired), 0 Draft. INSP-003 reads APPROVED on the P9 status delta (`08922d9`) | Yes |
| D18 | P8 repository protection confirmed | `grep -n` of `docs/reviews/SRR/minutes.md` (last changed at `2ee4868`, after `786822a`) | Line 151 holds the owner's verbatim statement "Done and added. I approve the other recommendations". Line 155 reads "The owner confirms that the repository protection of close-out item 6 is in place (precondition P8)". Line 164 holds the owner's statement that the GitHub settings are fine. `gh` and the network were not used | Yes |
| D19 | RFA/RID states and the memo | JSON read of `rfa-rid-log.json` (`state` field); decision memo front matter | RFA-SRR-008 Routine is Answered and RID-SRR-010 Minor is Answered. The other 20 items are Open liens: RID-SRR-001 to 009 and 011 to 014, all Minor, and RFA-SRR-001 to 007, all Routine. None is Blocking or Major. Memo: `disposition: Approved with liens`, `signed: 2026-09-26`, `baseline_tag: null` | Yes |
| D20 | P10 push state | `git rev-list --count origin/main..HEAD`; `git rev-parse --short origin/main` | 89 at HEAD, which is the record's 88 at `49104a5` plus the record commit. Local `origin/main` is `7647516`. No network command was run | Not done; this is a post-tag step, correctly recorded |

## 2. Precondition status confirmed at HEAD `4c4e0d1`

| # | Record claim (section 0.3.2) | Confirmed state | Agrees |
|---|---|---|---|
| P1 | Met: no open Major in 30 records | Met (D11) | Yes |
| P2 | Met, 5 of 5 | Met: INSP-016 F-01 Closed (Verified) (D11) | Yes |
| P3 | Met: 50 of 50, 424 tests OK | Met (D3, D8) | Yes |
| P4 | Met: 0 violations, 2 warnings | Met (D4) | Yes |
| P5 | Not met for row 2, 07 only (INSP-010 verdict copy, X-9) | Not met for 07 (D11). Every other CI's admission evidence holds, and its blob is unchanged (D1) | Yes |
| P6 | Met: run 6 gate exit 0 | Met (D12, D13, D14) | Yes |
| P7 | Met | No change to `expectations.json` `52b6cf5e` or `concept.md` `6f026f92` (D1) | Yes |
| P8 | Met: owner confirmation transcribed | Met (D18) | Yes |
| P9 | Met: 188 Active, 0 Draft | Met (D17) | Yes |
| P10 | Not done: 88 ahead at `49104a5` (post-tag) | 89 at HEAD (D20) | Yes |
| Deviations and CR departures (first check, defect 3) | Closed: entries 1 to 4 closed at `bb2485e` | Closed (D15, D16) | Yes |

First-check defects: defect 1 (open Majors) is cleared (D11); defect 2 (no gate exit 0) is cleared (D14); defect 3 (unlogged CR-004 departure) is cleared (D15, D16); defect 4 (P8) is cleared (D18); defect 5 (P9) is cleared (D17). OBS-1 is answered by the record's section 0.3, which lists every unmet precondition.

## 3. Defect blocking the tag (repository state; the record reports it)

1. **P5, Table 4-2 row 2, 07: the INSP-010 record verdict is NEEDS CHANGES.** `docs/reviews/SRR/checklists/software-plan-07.md` (last changed at `c8a5143`) reads `verdict: NEEDS CHANGES` and `assurance_verdict: NEEDS CHANGES`, although `reviewer_verdict` is APPROVED and no Major is open. SRR decision 1 approves each plan only when its record is APPROVED with no open Major. 07 sections 2.1.1 and 10.2 keep the record verdict until the paired assurance record reads APPROVED, and INSP-018 now does (`738da03`). Decision memo section 9 condition 2 does not allow this gap to become a lien. **Closure:** the INSP-010 reviewer, in a new invocation, performs cross item X-9. It copies INSP-018 `assurance_verdict: APPROVED`, sets `verdict: APPROVED` with its liens (finding-14 to 18, 20, 22), re-checks that its `product_files` blobs equal HEAD (07 `bfe05f43`, CR-001 `0f4cca4c` and CR-005 `9b0129ef` are all equal at `4c4e0d1`), and commits the record alone. Then the integrator commits R per record section 0.3 gap 2, and this check is repeated at R, with every hash taken by `git ls-tree R -- <path>` (CM plan 05 section 4.4 step 4; record section 9 row 2).

No hash, path, tool result, count or state in section 0.3 was found wrong. No new observation is raised. The P10 count differs from the record by one commit only because the record commit itself follows `49104a5`.

## 4. Verdict

**NOT READY FOR TAG.** No commit R exists. Section 0.3 of the record, at HEAD `4c4e0d1`, agrees with the repository in every checked item, and the first check's defects 1 to 5 are cleared. The tag is blocked only by the P5 gap for 07: the INSP-010 record verdict is NEEDS CHANGES, pending the X-9 copy. `baseline/srr` must not be applied until INSP-010 reads APPROVED, R is committed, and this check is repeated at R and reads READY FOR TAG.

# Independent baseline check 3, 2026-09-27: `docs/reviews/SRR/baseline-record.md` section 0.4 at R

**Verdict: READY FOR TAG on R = `779f93fd7214617a08e868cde0e5fafd9b9e848a`.** Section 0.4 of the record agrees with the repository at R in every hash, path, tool result, count and state checked below, and preconditions P1 to P9 hold at R. The P5 gap of check 2 is closed by the INSP-010 X-9 copy delta (`824a362`). P10 (push) is the post-tag step and is correctly recorded as pending. Two Minor observations on the record and one CI are listed in section 3; neither blocks the tag. Checks 1 and 2 above are kept unchanged as history.

| Field | Value |
|---|---|
| Date | 2026-09-27 |
| Checker | Independent reviewer agent (baseline check role, a new invocation). It did not author the baseline record, edited no product and no record, and wrote only this section (charter section 2 and section 11 rule 4; CM plan 05 section 4.4 step 4; record section 9 row 2) |
| Commit checked (R) | `779f93fd7214617a08e868cde0e5fafd9b9e848a`, message `baseline(srr): record functional baseline`, trailer `Refs: SRR` plus the Co-Authored-By line. Parent `824a3624980db067853e2438ac4f56b53cf554ad`. `git diff --numstat 824a362 R`: 1 file, `docs/reviews/SRR/baseline-record.md`, 107 added, 0 deleted (no historical line rewritten). `git diff --stat 824a362 R` outside the record: empty. HEAD equals R and `git status --short` was empty, so the tools were run on the checkout |
| Tag and push state | `git tag` holds no `baseline/srr`; the decision memo at R reads `baseline_tag: null`. No push and no network command was run |
| rustos | `git -C /Users/robinonsay/rust/rustos rev-parse master` = `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (ref read only). rustos sources were read only from a clean `git archive 2ec64c0` export in the session scratchpad (`.../scratchpad/bc4/rustos`). The owner's rustos working tree was neither read nor modified |
| Search first | `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: SRR baseline record section 0.4 configuration items preconditions P1 to P9) ran before any `grep`. `grep` was used afterwards only to pin lines |
| Downloads or installs | None. Every command was read-only or wrote only to the scratchpad. `docs/vv/traceability-report.md` and `docs/vv/traceability.json` were restored with `git checkout` after the `--report-only` run, and `git status --short` was clean afterwards |

## 1. Checks, commands and results

| # | Check | Command | Result | Pass |
|---|---|---|---|---|
| E1 | Every CI path in section 0.4.3 exists at R and its recorded hash equals `git ls-tree R -- <path>` (and `git rev-parse 824a362:<path>`) | Python loop in the scratchpad (`bc4/hashes.py`) that reads section 0.4.3 from `git show R:docs/reviews/SRR/baseline-record.md`, parses every table row (the ConOps figure row and the firmware row split into their four and two paths), the informational paragraph and the path-named records of the "Records cited" paragraph, and compares each hash with `git ls-tree R -- <path>` and `git rev-parse 824a362:<path>` | 73 of 73 pairs equal at R and at the parent, 0 differ. They cover rows 1 to 3, 5 to 7, 9 (11 schemas), 17, 27, 51, 52 and 53, the trees `docs/conops/` `0b04e66c`, `docs/requirements/sys/` `86ea40eb`, `docs/templates/` `e94d4ce5` and `firmware/` `de1c87cb`, `firmware/unsafe-audit.md` `18ef484b`, the 12 row 28 tool blobs, the 10 informational items, and INSP-010 `e7b16d25`, INSP-018 `9076d5a2`, `baseline-check.md` `7d1eb089` | Yes |
| E2 | Records and short blobs cited without a path in sections 0.4.2 and 0.4.3 | `git ls-tree R -- <path>` for each | Decision memo `4c09ef55`, minutes `5a5f4ed6`, RFA/RID log `906d4a19`, deviations log `bcb91b5c`, TC-SW-TOOL-001-r6 `8d12b383`, CR-001 `0f4cca4c`, CR-002 `c007177f`, CR-004 `b9fc9510`, CR-005 `9b0129ef`, and the four INSP-010 `product_files` the integrator re-checked (`docs/plan/measurements.json` `5e2d1755`, `measurements.schema.json` `c30b7f3e`, fixtures `valid.json` `3938cd57` and `invalid.json` `15231171`): all 13 equal. rustos pin `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` equals rustos `master` | Yes |
| E3 | Cited commits exist and "last changed" claims | `git cat-file -e <c>^{commit}` for 31 cited commits; `git log -1 --format=%h R -- <path>` | All 31 exist. INSP-018 last changed at `738da03`, INSP-010 at `824a362`, INSP-016 at `6a969b9`, INSP-003 at `08922d9`, memo at `305a11e`, minutes at `2ee4868`, L1 at `61a3cb7`, deviations at `bb2485e`, lock at `495a0c3`, `tools/traceability.py` at `c774851`, 07 and `tools/complexity_gate.py` at `106bc3a`. Memo commit `0bcea39` is the commit that adds `signed: 2026-09-26` (`git log -S`). `git diff --stat 49104a5 824a362` shows the 3 record files section 0.4.1 names | Yes |
| E4 | `validate_docs.py` | `.venv/bin/python tools/validate_docs.py` | exit 0; 50 passed, 0 failed, 50 checked | Yes |
| E5 | `traceability.py` | `.venv/bin/python tools/traceability.py --report-only`, then `git checkout -- docs/vv/traceability-report.md docs/vv/traceability.json` | exit 0; 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148). Rendered files restored; tree clean | Yes |
| E6 | `render_risk.py` | `cd /Users/robinonsay/rust/cwht && .venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | exit 0; 65 risks, 159 candidates, 0 warnings, `register.md` current | Yes |
| E7 | `render_rmm.py` | `.venv/bin/python tools/render_rmm.py --check` | exit 0; 100 rows (FC 75, T 17, NA 8), `rmm.md` current | Yes |
| E8 | `render_compliance.py` | `.venv/bin/python tools/render_compliance.py --check` | exit 0; rows 62 (FC 49, T 4, NA 9), validation passed, rendered file current | Yes |
| E9 | Tool unit tests | `cd /Users/robinonsay/rust/cwht && .venv/bin/python -m unittest discover -s tools/tests` | exit 0; 424 tests run, OK | Yes |
| E10 | `git fsck` | `git -C /Users/robinonsay/rust/cwht fsck --full` | exit 0; 6 dangling blobs and 4 dangling commits, no errors | Yes |
| E11 | AL-4 venv pins, tracked files, working tree | `tools/requirements.txt` (comments and blank lines removed, sorted) diffed against `.venv/bin/pip freeze` (sorted); `git ls-tree -r R \| wc -l`; `git status --short` | Identical, 35 pins; 1177 files at R (equal to `git ls-files`); tree clean | Yes |
| E12 | SRR records: `readiness_met`, verdicts and open Majors (P1, P2) | Python front-matter read (`bc4/records.py`) of every `.md` in `git ls-tree R docs/reviews/SRR/checklists/`; `findings_open:` of each; `grep -n -E '\| *Major *\| *(Open\|Reopened)'` and each hit followed to its later state | 30 records. All 30 read `verdict: APPROVED`, `reviewer_verdict: APPROVED`, `readiness_met: true` and `findings_open: 0`. Every `assurance_verdict` is APPROVED or `not-required`; INSP-010 now reads `assurance_verdict: APPROVED` and `verdict: APPROVED` (X-9 copy delta, `824a362`). The 7 Major Open table rows are each closed later in the same record: INSP-009 finding-11 (Verified at `7d735e5`), INSP-001 finding-14 (Verified on `b087a9f`), INSP-002 finding-23 and finding-24 (Closed at `dd3372c`), INSP-010 finding-21 (Verified, `106bc3a`), INSP-015 F-02 (Closed, iteration 3). INSP-016 F-01 is Closed (Verified) in delta 2 and INSP-018 finding-10 is Closed by `106bc3a`. **No open Major** | Yes |
| E13 | The X-9 copy delta is a copy only | `git diff 61ab1d7 824a362 -- docs/reviews/SRR/checklists/software-plan-07.md` | Two front-matter values change (`assurance_verdict`, `verdict`, NEEDS CHANGES to APPROVED) with comment lines, and an appended "X-9 copy delta" section; no earlier line of the record is removed except the two replaced values. The paired INSP-018 at `738da03` reads `assurance_verdict: APPROVED`, `verdict: APPROVED` | Yes |
| E14 | The lock pins rustos `2ec64c0` | `sed -n 215p tools/toolchain.lock.md` at R (blob `04819139`) | The section 3 rustos row carries `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (equal to rustos `master`); `c54d35a` appears on the row only as the superseded pin | Yes |
| E15 | `firmware/unsafe-audit.md` equals a fresh `tools/unsafe_audit.py --write` on clean exports | `git -C /Users/robinonsay/rust/rustos archive 2ec64c0 \| tar -x -C <scratch>/bc4/rustos`; `git archive R \| tar -x -C <scratch>/bc4/cwht`; in the cwht export `tools/unsafe_audit.py --check`, then `rm firmware/unsafe-audit.md` and `tools/unsafe_audit.py --write` (default roots resolve to the rustos export); `cmp` against `git show R:firmware/unsafe-audit.md` | `--check` exit 0: 37 sites, 0 without SAFETY, 0 in forbidden crates, 37 unsigned (a note before CDR). `--write` exit 0. Byte-identical: sha256 `7d15d8aaecf00d69e267a056c491bd7efa823af1608006a5151a9fdaa5ab8b08` for both; `git hash-object` = `18ef484bf050797e9493d68071efdc0259d423a6` | Yes |
| E16 | TC-SW-TOOL-001-r6 records gate exit 0 and its artifacts match their sha256 (P6) | Python (`bc4/r6b.py`): sha256 of each `artifacts:` entry read from `git show R:<path>` against the recorded value; `firmware_elf_sha256` against `cwht-app.elf`; `git ls-tree` of the run directory for unlisted files; `tail -2` of both gate logs | `result: Pass`, `credit: false`, `source_commit: bb2485e...`, `toolchain_lock` names blob `04819139` with rustos `2ec64c0`. 22 of 22 artifacts match; `firmware_elf_sha256` `14e43149...b2f6a9` equals `cwht-app.elf`; 22 tracked files, none unlisted. `sw-gate-full.txt` and `sw-gate-keep-going.txt` both end `sw_gate: PASS (G0 to G6)` and `sw_gate exit status: 0` | Yes |
| E17 | Deviations closed | Read of `docs/cm/deviations.md` at R (blob `bcb91b5c`) | 4 entries; the Closures table closes entries 1 to 4 on 2026-09-27 (CR section 6 at `8b86c16`). No open entry | Yes |
| E18 | CR states | Front matter of CR-001, CR-002, CR-004 and CR-005 at R | CR-001 `class: II`, CR-002, CR-004 and CR-005 `class: I`; all four `status: Dispositioned` | Yes |
| E19 | L1 Active (P9) | JSON count over `docs/requirements/sys/requirements.json` (blob `f128235e`) | 190 items: 188 Active, 2 Closed, 0 Draft | Yes |
| E20 | P8 repository protection | `grep -n` of `docs/reviews/SRR/minutes.md` at R (blob `5a5f4ed6`) | Line 155: the owner confirms the close-out item 6 repository protection is in place (precondition P8); line 167: the owner keeps it as set | Yes |
| E21 | RFA/RID states and memo | JSON read of `rfa-rid-log.json`; memo front matter | 22 items: RFA-SRR-008 (Routine) and RID-SRR-010 (Minor) Answered; the other 20 Open liens are Minor or Routine only. Memo: `disposition: Approved with liens`, `signed: 2026-09-26`, `baseline_tag: null` | Yes |
| E22 | Table 4-1 match of every tracked file at R (CM plan 4.4 step 1 and 7.4; record section 1 names this check "performed at R") | Python (`bc4/t41.py`): reads Table 4-1 from `git show R:docs/process/05-...md`, applies its matching rule (explicit path or pattern over directory prefix, longest prefix wins, `*` matches `/`) to `git ls-tree -r --name-only R` | 1177 of 1177 files match exactly one row; 0 unmatched, 0 ambiguous. Row 53 holds 21 files plus the row 9 schema, as section 0.4.3 states | Yes |
| E23 | Process index (row 2, Table 4-2) | Each tracked `docs/process/*.md` other than `README.md` searched in `git show R:docs/process/README.md` | All 11 named (00 to 08, `rmm.md`, `se-compliance-matrix.md`), as section 0.4.3 states. See observation OBS-1 | Yes |
| E24 | P10 push state | `git rev-list --count origin/main..824a362` and `..R`; `git rev-parse --short origin/main` | 91 at `824a362` and 92 at R, as recorded; local `origin/main` is `7647516`. No network command was run | Not done; post-tag step, correctly recorded |

## 2. Precondition status confirmed at R `779f93f`

| # | Record claim (section 0.4.2) | Confirmed state at R | Agrees |
|---|---|---|---|
| P1 | Met: no open Major in 30 records | Met (E12) | Yes |
| P2 | Met, 5 of 5 | Met (E12) | Yes |
| P3 | Met: 50 of 50, 424 tests OK | Met (E4, E9) | Yes |
| P4 | Met: 0 violations, 2 warnings, tool blob `12de3545` | Met (E1, E5) | Yes |
| P5 | Met: INSP-010 X-9 copy delta closes the row 2 gap for 07 | Met (E1, E2, E12, E13); every CI blob equals the blob of its admission evidence | Yes |
| P6 | Met: run 6 gate exit 0 | Met (E14, E15, E16) | Yes |
| P7 | Met: no CI changed since `49104a5` | Met (E1, E3) | Yes |
| P8 | Met: owner confirmation transcribed | Met (E20) | Yes |
| P9 | Met: 188 Active, 0 Draft | Met (E19) | Yes |
| P10 | Pending, post-tag: 91 ahead at `824a362`, 92 at R | 92 at R (E24) | Yes |
| Deviations | Entries 1 to 4 closed, no open entry | Closed (E17, E18) | Yes |

Check 2 defect 1 (P5, INSP-010 record verdict) is cleared (E12, E13).

## 3. Observations (not tag blockers; Minor, for the integrator to answer or carry as liens under the convergence rule, charter section 4 item 3)

1. **OBS-1, Table 4-2 row 2 criterion for `docs/process/README.md`.** CM plan 05 line 177 reads that the section 7.4 interim check "confirms that it names every file of rows 1 to 3 and nothing else". The index names every file of rows 1 to 3, but it also names files of other rows (for example `rmm.schema.json` and `se-compliance-matrix.schema.json` of row 9, `configuration-status.md` of row 35, `docs/plan/tpm.json` of row 34, `docs/plan/technology-assessment.md` of row 51). Section 0.4.3 records the narrower check ("names all 11 other tracked `docs/process/*.md` files"). These entries are pointers, not technical content, so the admission intent holds; the literal "nothing else" wording does not. Recommendation: the CM function states in the post-tag record commit how "nothing else" is read, or raises a Class II CR to reword Table 4-2 row 2.
2. **OBS-2, record section 9 row 1.** At R the "Baseline record prepared (commit R)" row still reads "This revision is the prepared record, not R (§0)" with date `pending`. Section 0.4 states that the section 9 fields are fill-once and written in the post-tag record commit, so this is expected; that commit should record R `779f93f` in this row, and this check's result (READY FOR TAG, 2026-09-27) in row 2.

No hash, path, tool result, count or state in section 0.4 was found wrong.

## 4. Verdict

**READY FOR TAG on R = `779f93fd7214617a08e868cde0e5fafd9b9e848a`.** Every section 0.4.3 hash equals `git ls-tree R -- <path>`, preconditions P1 to P9 hold at R, every tracked file matches one Table 4-1 row, and no Major is open. The integrator may apply `baseline/srr` to R with the record section 8 commands, then push (P10) and write the post-tag record commit (CM plan 05 section 4.4 steps 5 and 6), answering OBS-1 and OBS-2 there.
