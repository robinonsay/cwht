# TV-011: tools/unsafe_audit.py (git blob cc3aaa2a, working tree on 400e59d)

| Field | Value |
|---|---|
| Record | TV-011 |
| Status | **Validated** (2026-09-26) on the working-tree file identified in section 1, not yet committed. Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: gate G5 output, MSR-11, `firmware/unsafe-audit.md`) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; implements 07 CS-05 to CS-07 enforcement "G" |
| Due | CDR (CM plan section 13 CDR row); filed at SRR because the gate run of TC-SW-TOOL-001-r2 (SRR package item R3, entrance row 20) cites its output before CDR (CM plan section 9.1: a TV record before the first cited use) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/unsafe_audit.py`; section 1.2 |
| Author | Claude, tool maintainer (SRR package item R3) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `400e59d` |
|---|---|---|---|
| `tools/unsafe_audit.py` | `cc3aaa2ad82a52a63615c6af082567007b2d7e6e` | `08a9030a42a5aa63551b73e59400863e4f36bfe09dbc9131095c1efb127a8941` | untracked (new) |
| `tools/tests/test_unsafe_audit.py` | `5fadacd26d32b3d440e79edbfb67ecaa7e6b197d` | `d65fe91328db74f2828a525ff37242d2e01fe153110a96aa9c8e2b4bfd197895` | untracked |
| `tools/tests/fixtures/unsafe_audit/` (`audited/src/lib.rs`, `forbidden/src/main.rs`, `clean/src/lib.rs`) | 3 files, tree digest `0c8cb73502c08f990c8b540cee895da27553b32404a1bf206e7206089f81c8f5` | | untracked |

Commands and digest as in TV-002 section 1 (procedure `evidence/python-tools-2026-09-26-r5.py`, functions `ident` and `tree`). **Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 interpreter, standard library only.

## 2. Purposes covered

1. Find every `unsafe` keyword in Rust sources outside comments, string, raw-string and character literals, skipping `target/` directories, and classify it as block, fn, impl, trait, extern block, unsafe attribute or other; an `unsafe fn(..)` pointer type is not a site. Name the enclosing item (fn for a block, the item for a fn, attribute or impl).
2. For the audited roots (default rustos `api` and `firmware/pico2`): report every site without a `// SAFETY:` comment in the comment block directly above it (attribute lines skipped) as a failure (07 CS-06); for the forbidden roots (default `firmware/`): report every site as a failure (CS-05).
3. Generate the audit list `firmware/unsafe-audit.md` (`--write`, CS-07; 05 Table 4-1 row 46) with file, line, kind, item and SAFETY text, keeping each Reviewer and Date signature while the site's file, kind, item and SAFETY text are unchanged and appending the signature of a changed or removed site to the "Superseded signatures" section, which is never shortened.
4. `--check` (gate G5): fail on purpose 2 findings, an absent or stale audit list, or a malformed signature (Reviewer not `INSP-NNN`, Date not `YYYY-MM-DD`, one without the other); report unsigned entries, failing on them only with `--gate CDR`, `TRR` or `SAR` (07 section 8.2 Security row); print the MSR-11 counts (per kind, total, without SAFETY, unsigned, in forbidden crates), or JSON with `--json`.
5. Exit 0 with no failure, 1 on any failure, 2 on a usage error.

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/unsafe_audit/`. `audited/src/lib.rs` holds nine sites whose lines, kinds, items and SAFETY texts were written down by reading the file (lines 19 block, 26 fn, 28 block, 32 impl, 36 block without SAFETY (seeded CS-06 fault), 40 attribute, 44 extern block, 50 block, 55 attribute) and decoys that are not sites: a doc comment, a nested block comment, a string, a raw string with an embedded quote, two character literals (`'"'` and `'\''`), a lifetime and an `unsafe extern "C" fn()` pointer type. `forbidden/src/main.rs` holds one site in a `#![forbid(unsafe_code)]` crate (seeded CS-05 fault); `clean/src/lib.rs` one site with its SAFETY comment. A `target/` file is created by the test in a temporary copy (the repository ignores `target/`).

**Run command** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_unsafe_audit.py
```

**Pass criteria:** all 14 tests pass, none skipped: `LexerTests` 3 (masking keeps offsets and line count; escaped quote, raw string with hashes, lifetime), `ScanKnownAnswerTests` 4 (the nine sites exactly; the forbidden site; `target/` not scanned; the MSR-11 counts block 4, fn 1, impl 1, attribute 2, extern 1, total 9, without SAFETY 1, forbidden 1, unsigned 9), `CheckTests` 4 (no list fails; `--write` then `--check` reports exactly the two seeded faults and the note "9 unsigned entries"; a clean list passes before CDR, fails at `--gate CDR` with "1 unsigned entry", passes at `--gate SAR` once signed, and fails on the malformed Reviewer `INSP-42`; a site moved by one line makes the list stale in both directions), `SignatureTests` 2 (a signature follows a moved site, moves to the superseded section when the SAFETY text changes and is kept on a later rewrite; render and parse round-trip with `|` and `\` in the text), `UsageTests` 1 (unknown gate, missing scan root, no mode: exit 2).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-26 02:32 | working tree on `400e59d`, identities of section 1 | 14 (`CheckTests` 4, `LexerTests` 3, `ScanKnownAnswerTests` 4, `SignatureTests` 2, `UsageTests` 1), 0 skipped | pass |
| Gate integration | 2026-09-26 02:37 | working tree on `400e59d`; rustos `c54d35a` | `tools/sw_gate.sh --keep-going` step G5 unsafe audit | FAIL as specified: 37 sites in rustos `api` and `pico2` (block 16, fn 11, impl 1, extern 3, attribute 6), 36 without a SAFETY comment, `firmware/unsafe-audit.md` absent; 0 sites in the cwht crates |

Evidence: `evidence/python-tools-2026-09-26-r5-worktree.log.txt` (run 1); `evidence/sw-gate-2026-09-26.log.txt` (gate integration). The gate result is a finding against the rustos sources and the absent list, not a tool defect: CS-06 requires the SAFETY comments (rustos work, owner) and CS-07 the generated list.

## 5. Reproducibility

Not required for class B. The output is a deterministic function of the sources (sorted file walk).

## 6. Limitations

1. The lexer is written for the constructs listed in section 3; it does not parse Rust. A `unsafe` token produced by a macro expansion is invisible (only source text is scanned); a site inside a `macro_rules!` body is found and needs its SAFETY comment like any other.
2. "Immediately above" is the contiguous comment block above the line holding the site, attribute lines skipped; a SAFETY comment separated by a blank line or a code line does not count, and a trailing comment on the site's own line does not count.
3. The item of a block is the innermost enclosing `fn` by brace matching on the masked text; closures and blocks at module level are reported as the enclosing fn or "(module level)".
4. The SAFETY argument itself is judged by the code reviewer (CK-CODE-B2), not by this tool; the tool only checks presence and that the audit list quotes it.
5. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, its test module or its fixture (CM plan section 9.2 step 4).
- A Rust edition or language change that adds a place for `unsafe` (for example new unsafe attributes).
- A change of the interpreter (TV-001).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer re-runs section 3 and re-counts the fixture sites by reading `audited/src/lib.rs`. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-UNSAFE-001**: "Accredited for purposes 1 to 5 for `tools/unsafe_audit.py` at the git blob committed from working-tree blob `cc3aaa2ad82a52a63615c6af082567007b2d7e6e`, under the TV-001 interpreter."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8; due CDR, CM plan section 13) | | |
