# TV-012: tools/complexity_gate.py (git blob 9cdc9195, commit e34a27b; earlier blob 9214fefb, working tree on 400e59d)

| Field | Value |
|---|---|
| Record | TV-012 |
| Status | **Validated** (2026-09-26) on the working-tree file identified in section 1, not yet committed, for its own logic on analyzer output in the documented format; the analyzer `rust-code-analysis-cli` is not installed (lock section 1.1), so the end-to-end check of limitation 1 is open. Independent review and owner accreditation pending (sections 8 and 9). Update 2026-09-26: the analyzer is installed (SRR decision 109); the end-to-end check ran and failed on the CC counting convention (section 4, limitation 1), so limitation 1 stays open. Update 2026-09-26 21:22 (CR-005; SRR close-out item 4, owner concurrence "I concur with your recommendations", `docs/reviews/SRR/minutes.md` commit `dd39332`): the tool changed to blob `9cdc9195` in commit `e34a27b` (the CR-005 counting convention: analyzer count plus one per `let ... else`; the CS-38 per-file allowance of CR-001 and CR-005); **re-validated** by run 2 of section 4 on an export of `e34a27b`, with `rca.json` now real `rust-code-analysis-cli` 0.0.25 output and the end-to-end check passing, so limitations 1 and 2 are closed (section 6). Independent review of this re-validation (INSP-015 delta) pending; ACC-COMPLEXITY-001 takes effect for blob `9cdc9195` when that review is APPROVED (section 9). The gate run on the firmware and rustos `2ec64c0` fails CS-38 on `cwht-app` `main` by its CS-19 main loop, which the ruled allowance does not cover (section 4 run 2 gate row; limitation 8) |
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

**Identities for run 2** (2026-09-26, CR-005; every file read from an export of commit `e34a27b`, `git archive e34a27b | tar -x`, so each equals the committed blob):

| File | Git blob | SHA-256 | Change against the run 1 identities above |
|---|---|---|---|
| `tools/complexity_gate.py` | `9cdc91959b06ca3f39142b0afcf85b9a64f719b1` | `2ef89914293cae42e7ba1b50f946c1979d0b293e590371b3083bb6b8acff8669` | changed in `e34a27b` from blob `9214fefb` (CR-005 section 1 item 4: `let_else_sites`, `own_lines`, `is_admitted_arm`, `is_panic_handler`, `allowances`; CS-38 allowance per function; COUNT and ALLOWANCE lines; `cs_38_allowances` in `--json`) |
| `tools/unsafe_audit.py` (imported: `mask_rust`, TV-011) | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e` | `08a9030a42a5aa63551b73e59400863e4f36bfe09dbc9131095c1efb127a8941` | equal |
| `tools/tests/test_complexity_gate.py` | `1b6039418d5bc72393319a2b1856404e1248af66` | `ab6c04db98a47887e49afac015b06af46626a43ebb1c6afae458a051cecc7764` | changed in `e34a27b` from blob `a3b0661b`: known answers of the new fixture; classes `AnalyzerEndToEndTests`, `LetElseTests`, `AllowanceTests` |
| `tools/tests/fixtures/complexity_gate/` (same 5 files) | 5 files, tree digest `7f44cdda7ce020cd6bbe95b566ad944ad773f8a888b1e4818478fa9073bdb11c` | | changed in `e34a27b`: `src/core.rs`, `src/app.rs` rewritten; `rca.json` (blob `36f84b8b`) is the analyzer's output on them; `waivers.json` and the memo equal |

Tree digest computed with function `tree` of `evidence/python-tools-2026-09-25.py`. Analyzer: `rust-code-analysis-cli --version` prints `rust-code-analysis-cli 0.0.25` (lock row; installed under SRR decision 109).

**Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 interpreter, standard library only. **Upstream tool:** `rust-code-analysis-cli`, not installed (installing it is an owner-approved download, decision 109).

## 2. Purposes covered

1. Read the JSON of `rust-code-analysis-cli --metrics --output-format json` (a stream of per-file objects or an array) and derive each function's own cyclomatic complexity as its `metrics.cyclomatic.sum` less the sums of its direct child spaces (a plain number is taken as the function's own value); stop with exit 2 on input that is not JSON, holds no function space, names a source file that cannot be read, or gives an own value below 1 or not an integer.
2. CS-17 (SWE-220): fail every function above `--max` (15) unless a waiver of 07 section 14.3 covers it; report functions above `--yellow` (12). A waiver (`--waivers` JSON: id `W<n>`, file, function, cc, memo) is honoured only when the memo exists and names the id.
3. CS-38: in a file with the line `// @target-only`, fail every function above CC 1 plus one per `::take()` call in its body (the CS-11 board take).
4. CS-19: report, never fail, every cycle of the name-based call graph of the analysed functions.
5. Print the MSR-17 measures (functions, max, mean, above 12, above 15, above yellow, above max, target-only above 1), or JSON with `--json`; exit 0 with no failure, 1 on a CS-17 or CS-38 failure, 2 on a usage or input error.

From blob `9cdc9195` (CR-005, SRR close-out item 4), purposes 1 and 3 read:

- Purpose 1: as before, and the CC of each function is its own analyzer value plus one for each `let ... else` statement credited to it: a statement-initial `let` whose statement reaches an `else` at bracket depth 0 before its `;`, where that `else` is not directly preceded by `}`, found in the comment- and literal-masked source and credited to the innermost function space whose line range holds the `let` line (a line that is the first or last line of a nested space counts for both spaces).
- Purpose 3: CS-38: in a file with the line `// @target-only`, fail every function above CC 1 plus its share of the per-file allowance of CR-001 and CR-005: one for each CS-11 failure arm in its body (`let Some(..) = ..::take() else { safe_state_halt() }` or `let Ok(..) = .. else { safe_state_halt() }`, the else block holding nothing else) and one for a bare `loop` in the body of the `#[panic_handler]` function or of `safe_state_halt`; print the file's allowance (`ALLOWANCE` line, `cs_38_allowances` in `--json`) and each let-else addition (`COUNT` line).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/complexity_gate/`. `rca.json` is hand-written in the analyzer's FuncSpace format for the two source files (own CC straight 1, branchy 5, at_limit 15, over_limit 16, with_closure 2 with a closure of 2 nested in it (function sum 4), ping 2, pong 1, fact 2, uses_string 1; in the `@target-only` file main 2 (one `Board::take()`), halt 1, extra 2). The expected answers were computed by hand from those values: 13 functions, sum 52, mean 4.0, max 16, two above 12, one above 15, two target-only functions above 1; CS-17 fails `over_limit`; CS-38 fails `extra` only (main is allowed 2); CS-19 cycles `fact -> fact` and `ping -> pong -> ping`, and none from the call written in a comment of `ping` or in the string of `uses_string`. `waivers.json` holds W1 (named in the fixture memo) and W2 (not named).

**Run command** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_complexity_gate.py
```

**Pass criteria:** all 9 tests pass, none skipped: `ParseKnownAnswerTests` 3 (the 13 own values; the array and plain-number forms; empty input, non-JSON input and an own value of -1 are input errors), `GateKnownAnswerTests` 5 (the exact FAIL, YELLOW, REPORT and MSR-17 lines; W1 waives `over_limit` and W2 is reported not honoured; a pass on standard input with exit 0; the board-take allowances main 2, halt 1, extra 1; the JSON form), `UsageTests` 1 (missing `--max`, `--yellow` above `--max`, an empty pipe and an unreadable source file exit 2).

From run 2 (CR-005), the fixture and the known answers are:

**Fixture (run 2):** `src/core.rs` (host code) and `src/app.rs` (`// @target-only`); `rca.json` is the output of `rust-code-analysis-cli --metrics --output-format json --paths src/core.rs --paths src/app.rs` run in the fixture folder, not a hand-written value. The expected answers are derived by hand from the sources under the CR-005 convention (analyzer: 1, plus one per `if` and `else if`, per `match` arm with `_` included, per `loop`, `while` and `for`; the tool adds one per `let ... else`) and match the analyzer's values function by function:

| Function (file) | Analyzer own CC | `let ... else` | Tool CC | CS-38 allowance | Expected result |
|---|---|---|---|---|---|
| `main` (app) | 1 | 2 (board take, driver construction, both `safe_state_halt()`) | 3 | 1 + 2 arms = 3 | pass |
| `safe_state_halt` (app) | 2 (bare `loop`) | 0 | 2 | 1 + 1 halt loop = 2 | pass |
| `panic` (app, `#[panic_handler]`) | 2 (bare `loop`) | 0 | 2 | 2 | pass |
| `spin` (app) | 2 (bare `loop`) | 0 | 2 | 1 | CS-38 fail (a loop outside the two halt functions) |
| `wrong_arm` (app) | 1 | 1 (else block `return 0`) | 2 | 1 | CS-38 fail (not an admitted arm) |
| `extra` (app) | 2 | 0 | 2 | 1 | CS-38 fail |
| `straight`, `branchy`, `pong`, `uses_string` (core) | 1, 5, 1, 1 | 0 | same | none | pass |
| `at_limit` (core) | 15 (14 arms) | 0 | 15 | none | YELLOW |
| `over_limit` (core) | 16 (15 arms) | 0 | 16 | none | CS-17 fail (W1 waives it) |
| `let_else_limit` (core) | 15 (14 arms) | 1 | 16 | none | CS-17 fail: the analyzer alone would pass it |
| `with_closure` and its closure `<anonymous>` (core) | 2 and 2 (sum 4) | 0 and 1 (the let-else is the closure's) | 2 and 3 | none | pass |
| `not_let_else` (core) | 3 (an `if` initializer, an `if let`) | 0 | 3 | none | pass |
| `ping`, `fact` (core) | 2, 2 | 0 (the let-else in the comment of `ping` and the string of `uses_string` are masked) | 2, 2 | none | pass; CS-19 cycles `fact -> fact`, `ping -> pong -> ping` |

Totals: 18 functions, CC sum 80, mean 4.44, max 16, three above 12, two above 15, six target-only above 1; file allowance of `src/app.rs` 4 (2 CS-11 failure arms, 2 CS-19 halt loops); five failures (CS-38 `spin`, `wrong_arm`, `extra`; CS-17 `over_limit`, `let_else_limit`).

**Pass criteria (run 2):** all 18 tests pass, none skipped: `ParseKnownAnswerTests` 3 (the 18 analyzer own values; the array and plain-number forms; input errors), `AnalyzerEndToEndTests` 2 (the analyzer version is 0.0.25; the analyzer's output on the fixture sources equals `rca.json`), `LetElseTests` 5 (the five fixture sites; tool CC = analyzer + let-else; forms that are not let-else: `if` initializer, `if let`, `while let`, let chain, comment, string, `==` and `match` initializers; forms that are: multi-line initializer, closure in the initializer, attribute before `let`, tuple pattern; a let-else on a line shared with a nested space counts for both), `AllowanceTests` 3 (the six `app.rs` allowances and the file allowance; admitted and rejected arm forms; the halt-loop allowance needs both the function (`#[panic_handler]` on its own line or on the `fn` line, or `safe_state_halt`) and a bare `loop` in it), `GateKnownAnswerTests` 4 (the exact FAIL, COUNT, YELLOW, ALLOWANCE, REPORT, MSR-17 and summary lines; W1 waives `over_limit` only and W2 is not honoured; a pass on standard input with `main`, `safe_state_halt` and `panic`; the JSON form), `UsageTests` 1. `AnalyzerEndToEndTests` skips only where the analyzer is absent; a skip is a failed run 2 criterion on the validation machine.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-26 02:32 | working tree on `400e59d`, identities of section 1 | 9 (`GateKnownAnswerTests` 5, `ParseKnownAnswerTests` 3, `UsageTests` 1), 0 skipped | pass |
| Gate integration | 2026-09-26 02:37 | working tree on `400e59d` | `tools/sw_gate.sh --keep-going` step G5 complexity | MISSING: `rust-code-analysis-cli` not installed; the gate no longer reports `tools/complexity_gate.py` missing |
| End-to-end check (limitation 1) | 2026-09-26 19:44 | HEAD `bfea9c7`, tool blob `9214fefb` (committed in `3de1e2d`, unchanged); `rust-code-analysis-cli` 0.0.25, installed 2026-09-26 under SRR decision 109 (owner ruling 2026-09-26) | the analyzer run on a scratch copy of `tools/tests/fixtures/complexity_gate/src/`, own CC of each function through this tool compared with the hand-computed values of `rca.json`, plus three scratch functions (bare `loop`, one `if`, one `while`) | **fail**: the format is understood (no input error; closures and nested spaces handled; 9 of 13 functions agree), but the analyzer's counting convention differs from the hand-computed one in 4 functions: a `match` counts every arm, `_` included (`at_limit` 16 against 15, `over_limit` 17 against 16); a bare `loop` counts as a decision (`halt` 2 against 1; scratch `bare_loop` 2); a `let ... else` does not count (`main` 1 against 2) |
| Gate integration, TC-SW-TOOL-001 run 3 | 2026-09-26 19:28 | HEAD `0bcea39` (git archive), rustos branch `2ec64c0` | `tools/sw_gate.sh` step G5 complexity | FAIL: the gate passes three paths to one `--paths` option, which 0.0.25 rejects (`Found argument ... which wasn't expected`), so this tool read empty input and exited 2 (input error); with one `--paths` per path (diagnostic, outside the gate) this tool reports one CS-38 failure, `safe_state_halt` CC 2 (its bare `loop`), MSR-17 functions 52, max CC 5 |
| 2 | 2026-09-26 21:22 | `e34a27b` (CR-005): an export of the commit (`git archive e34a27b`), the run 2 identities of section 1; TV-001 interpreter (Python 3.13.5) | 18 (`ParseKnownAnswerTests` 3, `AnalyzerEndToEndTests` 2, `LetElseTests` 5, `AllowanceTests` 3, `GateKnownAnswerTests` 4, `UsageTests` 1), 0 skipped | pass |
| End-to-end check (limitation 1), run 2 | 2026-09-26 21:22 | export of `e34a27b`; `rust-code-analysis-cli` 0.0.25 | `rust-code-analysis-cli --metrics --output-format json --paths src/core.rs --paths src/app.rs` in the fixture folder, compared with `rca.json`; the hand-derived values of section 3 compared with the tool's values | **pass**: the output is byte-identical to `rca.json` (`cmp` exit 0; six repeated runs give one SHA-256), and all 18 functions agree with the hand-derived analyzer, let-else and tool values of section 3 |
| Gate run on the firmware and rustos, run 2 | 2026-09-26 21:22 | export of `e34a27b` (`firmware/`) and a clean export of rustos `2ec64c0` (`git -C /Users/robinonsay/rust/rustos archive 2ec64c0`, as TC-SW-TOOL-001 run 3; the owner's rustos working tree not read) | `rust-code-analysis-cli --metrics --output-format json --paths <cwht>/firmware --paths <rustos>/api --paths <rustos>/firmware/pico2` (one `--paths` per root, as `tools/sw_gate.sh` blob `52b9f803`) piped to `tools/complexity_gate.py --max 15` | analyzer exit 0; tool exit 1. **CS-17: no failure** (52 functions, max CC 5, none above 12). **CS-38: one failure**, `cwht-app/src/main.rs:30 main` CC 4 (analyzer 2, of which 1 is the CS-19 main `loop`, plus 2 `let ... else`) against its allowance 3 (1 + 2 CS-11 failure arms). `safe_state_halt` CC 2 passes on its halt-loop allowance; `panic` CC 1 (it calls `safe_state_halt` and holds no loop). File allowance 3 (2 arms, 1 halt loop). See limitation 8 |

Evidence: `evidence/python-tools-2026-09-26-r5-worktree.log.txt`; `evidence/sw-gate-2026-09-26.log.txt`. End-to-end check: `evidence/rust-tools-2026-09-26.log.txt` section 2 (procedure `evidence/rust-tools-2026-09-26.sh`). Run 3 gate: `docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-full.txt`, `sw-gate-keep-going.txt`, `complexity-diagnostic.txt`.

Output excerpt (run 2 gate row; paths shortened to the export roots):

```
FAIL CS-38 <cwht e34a27b>/firmware/cwht-app/src/main.rs:30 main CC 4 > 3 in a // @target-only file (straight-line target-only code; allowance 2 CS-11 failure arm(s) and 0 CS-19 halt loop(s), CR-001 and CR-005)
COUNT <cwht e34a27b>/firmware/cwht-app/build.rs:11 main CC 3 = analyzer 1 + 2 let ... else (CR-005)
COUNT <cwht e34a27b>/firmware/cwht-app/src/main.rs:30 main CC 4 = analyzer 2 + 2 let ... else (CR-005)
ALLOWANCE CS-38 <cwht e34a27b>/firmware/cwht-app/src/main.rs: 3 (2 CS-11 failure arm(s), 1 CS-19 halt loop(s); CR-001, CR-005)
MSR-17 functions 52, max_cc 5, mean_cc 1.46, above_12 0, above_15 0, above_yellow 0, above_max 0, target_only_above_1 2
complexity_gate: FAIL (1 failure(s), 0 CS-19 report(s))
```

Mutation check (run 2): the run 2 test module against the previous tool blob `9214fefb` fails 13 of 18 tests (3 failures, 10 errors). Four single-rule mutants of blob `9cdc9195` each fail tests: no let-else addition (5 tests), no halt-loop allowance (5), any else block admitted as a CS-11 arm (4), child-space lines not excluded from the parent (2). The known answers discriminate each CR-005 rule.

Observation (analyzer probe on scratch functions, 2026-09-26, outside the fixture): the analyzer also counts each `while`, `for`, `if let`, `&&`, `||` and `?` as one decision, as the textbook count does; `let ... else` alone is missed, which the tool adds.

## 5. Reproducibility

Not required for class B. Deterministic function of the input.

## 6. Limitations

1. **Analyzer format and counting unverified end to end.** The input format and the own-CC derivation follow the rust-code-analysis FuncSpace serialization as documented in the tool header; no real analyzer output has been read yet. Before any output is cited for the record, the 07 section 8.3 sanity check runs: `rust-code-analysis-cli` on five reference functions with hand-computed CC 1, 2, 5, 15 and 16 must give those values through this tool, which also settles whether the analyzer counts a bare `loop` (the CS-19 halt loops of `cwht-app`) as a decision; that result decides whether CS-38 needs a rule for halt loops (cross item to the 07 owner). **Result 2026-09-26** (section 4, end-to-end check): the check fails on counting convention, not on format: rust-code-analysis-cli 0.0.25 counts every `match` arm (so a 15-arm match is CC 16, not 15), counts a bare `loop` as a decision (so the CS-19 halt loops are CC 2 and fail CS-38 as written) and does not count `let ... else`. Until the 07 owner fixes the CC convention for CS-17 and CS-38 (accept the analyzer's counts, or have this tool normalize them) and `rca.json` is re-derived from real analyzer output, analyzer-fed results of this tool are not cited for the record, and the limitation stays open. **Closed 2026-09-26** (run 2, section 4): the owner fixed the convention (CR-005, SRR close-out item 4: the analyzer's counts are the measure, plus one per `let ... else`, which this tool adds); `rca.json` is now the analyzer's own output on the fixture and the end-to-end check passes.
2. The CS-38 allowance recognizes the board take by the text `::take()` in the function body; the driver-construction arms that CR-001 proposes (INSP-016 finding-2) have no allowance and fail until a waiver or a CS-38 change exists. **Closed 2026-09-26** (blob `9cdc9195`, CR-001 implementation step 3 with CR-005): the admitted arms are recognized as `let ... else { safe_state_halt() }` statements (`Some` with a `::take()` initializer, or `Ok`) and counted against the per-file allowance; the independent code reviewer still checks that an `Ok` arm constructs a rustos driver (CR-001 section 5).
3. CS-19 is name-based: two functions with one name are one node (a false cycle is possible), and a cycle through a function pointer, trait object or macro is not seen. It reports only; the reviewer decides (CS-19 enforcement R).
4. A waiver is matched by function name and file suffix; the memo check is textual (the id as a word in the memo).
5. Output is developer evidence until section 9 records the accreditation.
6. The `let ... else` recognition is textual on the masked source (section 2, purpose 1 from blob `9cdc9195`), at line granularity: a let-else on a line shared by a function and a nested space is counted for both (over-count, never under-count); a `let` inside a macro body is counted like any other.
7. A CS-11 failure branch written as a two-arm `match` (which 07 CS-11 admits) is not recognized as an admitted arm; the analyzer counts both arms, so the function fails CS-38 (fails closed). `cwht-app` uses the `let ... else` form.
8. **Open, for the owner (2026-09-26):** the ruled allowance (CR-005 section 1 item 2) covers the two CS-19 halt loops but not the third unbounded loop CS-19 names, the main loop of `cwht-app::main`; the analyzer counts it, so `main` is CC 4 against allowance 3 and gate G5 fails (section 4, run 2 gate row). The tool applies the ruling as written and credits each item to its own function; under a pooled per-file reading with an unconditional +1 for the panic handler (which holds no loop in the FW-B0 code), the file would pass only because the panic handler's unused allowance covers the main loop, which this tool does not do. The resolution is an owner decision (section 9 note).
9. `AnalyzerEndToEndTests` needs `rust-code-analysis-cli` on `PATH`; where it is absent the class skips, and the run 2 pass criterion then fails.

## 7. Re-validation triggers

- Any change of the tool, of `tools/unsafe_audit.py` (`mask_rust`), of the test module or of the fixture (CM plan section 9.2 step 4).
- Installation or any version change of `rust-code-analysis-cli` (limitation 1 check first).
- A change of the interpreter (TV-001).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer re-runs section 3 and re-derives the fixture's expected answers from `rca.json`. Reviewer invocation, date and result are recorded here.

Re-validation review of run 2 (CR-005): pending, the INSP-015 delta. The reviewer re-runs section 3 on an export of the committed files, re-derives the run 2 expected answers from `src/core.rs` and `src/app.rs` under the CR-005 convention, confirms that the analyzer's output on the fixture equals `rca.json`, and checks the run 2 gate row. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-COMPLEXITY-001**: "Accredited for purposes 1 to 5 for `tools/complexity_gate.py` at the git blob committed from working-tree blob `9214fefb76f95f0494f906607ef06428260d1c75`, fed by `rust-code-analysis-cli` at the version recorded in the lock after the limitation 1 check passes, under the TV-001 interpreter."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8 and limitation 1; due CDR, CM plan section 13) | | |
| Not decided at SRR: SRR decision 114 (owner ruling 2026-09-26) covers TV-001 to TV-010 only, and this record has no independent review yet (section 8). The accreditation stays pending to its due gate; until then this tool's output is developer evidence (CM plan section 9.1). | 2026-09-26 | Claude (software lead and tool owner) |
| Extended per the owner's close-out concurrence (SRR close-out item 4, `docs/reviews/SRR/minutes.md` commit `dd39332`, owner statement "I concur with your recommendations"; recorded: "Under items 4 and 5, the changed tools are re-validated, and their accreditations are extended once the independent review of each validation record is complete."): ACC-COMPLEXITY-001 covers purposes 1 to 5 for `tools/complexity_gate.py` at git blob `9cdc91959b06ca3f39142b0afcf85b9a64f719b1` (commit `e34a27b`), fed by `rust-code-analysis-cli` 0.0.25 under the CR-005 convention, under the TV-001 interpreter. **Effective on the APPROVED independent review of this re-validation (INSP-015 delta, section 8)**; until then the output stays developer evidence. This record had no earlier accreditation (row above), so the concurrence is the accreditation decision for this blob. Limitation 8 is not a tool defect: the tool applies the ruled allowance, and the `cwht-app::main` result waits on the owner. | 2026-09-26 | Claude (software lead and tool owner) |
