# TV-012: tools/complexity_gate.py (git blob 9214fefb, working tree on 400e59d)

| Field | Value |
|---|---|
| Record | TV-012 |
| Status | **Validated** (2026-09-26) on the working-tree file identified in section 1, not yet committed, for its own logic on analyzer output in the documented format; the analyzer `rust-code-analysis-cli` is not installed (lock section 1.1), so the end-to-end check of limitation 1 is open. Independent review and owner accreditation pending (sections 8 and 9). Update 2026-09-26: the analyzer is installed (SRR decision 109); the end-to-end check ran and failed on the CC counting convention (section 4, limitation 1), so limitation 1 stays open |
| Class | B, evidence-generating (CM plan section 9.1: gate G5 output, MSR-17, SWE-220 evidence) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; implements 07 CS-17, CS-19 (reporting) and CS-38 enforcement "G" and the waiver rule of 07 section 14.3 |
| Due | CDR, with `rust-code-analysis-cli` (CM plan section 13 CDR row); filed at SRR with the gate scripts of SRR package item R3 |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/complexity_gate.py`; section 1.2; the `rust-code-analysis-cli` row |
| Author | Claude, tool maintainer (SRR package item R3) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `400e59d` |
|---|---|---|---|
| `tools/complexity_gate.py` | `9214fefb76f95f0494f906607ef06428260d1c75` | `e14a4c3bf98aed410c24d87ef5632d56a04b7d1ba14e5f87dfc2699722fd820c` | untracked (new) |
| `tools/unsafe_audit.py` (imported: `mask_rust`, the comment and literal masker, TV-011) | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e` | `08a9030a...efb127a8941` | untracked |
| `tools/tests/test_complexity_gate.py` | `a3b0661b4967377a5d49f8b54cc0ec6b380bb947` | `f93002021217bbad167e44d79ce7bf071b2237589f4f97fa75be37c54b861e03` | untracked |
| `tools/tests/fixtures/complexity_gate/` (`src/core.rs`, `src/app.rs`, `rca.json`, `waivers.json`, `docs/reviews/CDR/decision-memo.md`) | 5 files, tree digest `021a012766cfd784490eee7d7574c4e17f431269b804f76ecdcd4b50cd454067` | | untracked |

**Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 interpreter, standard library only. **Upstream tool:** `rust-code-analysis-cli`, not installed (installing it is an owner-approved download, decision 109).

## 2. Purposes covered

1. Read the JSON of `rust-code-analysis-cli --metrics --output-format json` (a stream of per-file objects or an array) and derive each function's own cyclomatic complexity as its `metrics.cyclomatic.sum` less the sums of its direct child spaces (a plain number is taken as the function's own value); stop with exit 2 on input that is not JSON, holds no function space, names a source file that cannot be read, or gives an own value below 1 or not an integer.
2. CS-17 (SWE-220): fail every function above `--max` (15) unless a waiver of 07 section 14.3 covers it; report functions above `--yellow` (12). A waiver (`--waivers` JSON: id `W<n>`, file, function, cc, memo) is honoured only when the memo exists and names the id.
3. CS-38: in a file with the line `// @target-only`, fail every function above CC 1 plus one per `::take()` call in its body (the CS-11 board take).
4. CS-19: report, never fail, every cycle of the name-based call graph of the analysed functions.
5. Print the MSR-17 measures (functions, max, mean, above 12, above 15, above yellow, above max, target-only above 1), or JSON with `--json`; exit 0 with no failure, 1 on a CS-17 or CS-38 failure, 2 on a usage or input error.

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/complexity_gate/`. `rca.json` is hand-written in the analyzer's FuncSpace format for the two source files (own CC straight 1, branchy 5, at_limit 15, over_limit 16, with_closure 2 with a closure of 2 nested in it (function sum 4), ping 2, pong 1, fact 2, uses_string 1; in the `@target-only` file main 2 (one `Board::take()`), halt 1, extra 2). The expected answers were computed by hand from those values: 13 functions, sum 52, mean 4.0, max 16, two above 12, one above 15, two target-only functions above 1; CS-17 fails `over_limit`; CS-38 fails `extra` only (main is allowed 2); CS-19 cycles `fact -> fact` and `ping -> pong -> ping`, and none from the call written in a comment of `ping` or in the string of `uses_string`. `waivers.json` holds W1 (named in the fixture memo) and W2 (not named).

**Run command** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_complexity_gate.py
```

**Pass criteria:** all 9 tests pass, none skipped: `ParseKnownAnswerTests` 3 (the 13 own values; the array and plain-number forms; empty input, non-JSON input and an own value of -1 are input errors), `GateKnownAnswerTests` 5 (the exact FAIL, YELLOW, REPORT and MSR-17 lines; W1 waives `over_limit` and W2 is reported not honoured; a pass on standard input with exit 0; the board-take allowances main 2, halt 1, extra 1; the JSON form), `UsageTests` 1 (missing `--max`, `--yellow` above `--max`, an empty pipe and an unreadable source file exit 2).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-26 02:32 | working tree on `400e59d`, identities of section 1 | 9 (`GateKnownAnswerTests` 5, `ParseKnownAnswerTests` 3, `UsageTests` 1), 0 skipped | pass |
| Gate integration | 2026-09-26 02:37 | working tree on `400e59d` | `tools/sw_gate.sh --keep-going` step G5 complexity | MISSING: `rust-code-analysis-cli` not installed; the gate no longer reports `tools/complexity_gate.py` missing |
| End-to-end check (limitation 1) | 2026-09-26 19:44 | HEAD `bfea9c7`, tool blob `9214fefb` (committed in `3de1e2d`, unchanged); `rust-code-analysis-cli` 0.0.25, installed 2026-09-26 under SRR decision 109 (owner ruling 2026-09-26) | the analyzer run on a scratch copy of `tools/tests/fixtures/complexity_gate/src/`, own CC of each function through this tool compared with the hand-computed values of `rca.json`, plus three scratch functions (bare `loop`, one `if`, one `while`) | **fail**: the format is understood (no input error; closures and nested spaces handled; 9 of 13 functions agree), but the analyzer's counting convention differs from the hand-computed one in 4 functions: a `match` counts every arm, `_` included (`at_limit` 16 against 15, `over_limit` 17 against 16); a bare `loop` counts as a decision (`halt` 2 against 1; scratch `bare_loop` 2); a `let ... else` does not count (`main` 1 against 2) |
| Gate integration, TC-SW-TOOL-001 run 3 | 2026-09-26 19:28 | HEAD `0bcea39` (git archive), rustos branch `2ec64c0` | `tools/sw_gate.sh` step G5 complexity | FAIL: the gate passes three paths to one `--paths` option, which 0.0.25 rejects (`Found argument ... which wasn't expected`), so this tool read empty input and exited 2 (input error); with one `--paths` per path (diagnostic, outside the gate) this tool reports one CS-38 failure, `safe_state_halt` CC 2 (its bare `loop`), MSR-17 functions 52, max CC 5 |

Evidence: `evidence/python-tools-2026-09-26-r5-worktree.log.txt`; `evidence/sw-gate-2026-09-26.log.txt`. End-to-end check: `evidence/rust-tools-2026-09-26.log.txt` section 2 (procedure `evidence/rust-tools-2026-09-26.sh`). Run 3 gate: `docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-full.txt`, `sw-gate-keep-going.txt`, `complexity-diagnostic.txt`.

## 5. Reproducibility

Not required for class B. Deterministic function of the input.

## 6. Limitations

1. **Analyzer format and counting unverified end to end.** The input format and the own-CC derivation follow the rust-code-analysis FuncSpace serialization as documented in the tool header; no real analyzer output has been read yet. Before any output is cited for the record, the 07 section 8.3 sanity check runs: `rust-code-analysis-cli` on five reference functions with hand-computed CC 1, 2, 5, 15 and 16 must give those values through this tool, which also settles whether the analyzer counts a bare `loop` (the CS-19 halt loops of `cwht-app`) as a decision; that result decides whether CS-38 needs a rule for halt loops (cross item to the 07 owner). **Result 2026-09-26** (section 4, end-to-end check): the check fails on counting convention, not on format: rust-code-analysis-cli 0.0.25 counts every `match` arm (so a 15-arm match is CC 16, not 15), counts a bare `loop` as a decision (so the CS-19 halt loops are CC 2 and fail CS-38 as written) and does not count `let ... else`. Until the 07 owner fixes the CC convention for CS-17 and CS-38 (accept the analyzer's counts, or have this tool normalize them) and `rca.json` is re-derived from real analyzer output, analyzer-fed results of this tool are not cited for the record, and the limitation stays open.
2. The CS-38 allowance recognizes the board take by the text `::take()` in the function body; the driver-construction arms that CR-001 proposes (INSP-016 finding-2) have no allowance and fail until a waiver or a CS-38 change exists.
3. CS-19 is name-based: two functions with one name are one node (a false cycle is possible), and a cycle through a function pointer, trait object or macro is not seen. It reports only; the reviewer decides (CS-19 enforcement R).
4. A waiver is matched by function name and file suffix; the memo check is textual (the id as a word in the memo).
5. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, of `tools/unsafe_audit.py` (`mask_rust`), of the test module or of the fixture (CM plan section 9.2 step 4).
- Installation or any version change of `rust-code-analysis-cli` (limitation 1 check first).
- A change of the interpreter (TV-001).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer re-runs section 3 and re-derives the fixture's expected answers from `rca.json`. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-COMPLEXITY-001**: "Accredited for purposes 1 to 5 for `tools/complexity_gate.py` at the git blob committed from working-tree blob `9214fefb76f95f0494f906607ef06428260d1c75`, fed by `rust-code-analysis-cli` at the version recorded in the lock after the limitation 1 check passes, under the TV-001 interpreter."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8 and limitation 1; due CDR, CM plan section 13) | | |
| Not decided at SRR: SRR decision 114 (owner ruling 2026-09-26) covers TV-001 to TV-010 only, and this record has no independent review yet (section 8). The accreditation stays pending to its due gate; until then this tool's output is developer evidence (CM plan section 9.1). | 2026-09-26 | Claude (software lead and tool owner) |
