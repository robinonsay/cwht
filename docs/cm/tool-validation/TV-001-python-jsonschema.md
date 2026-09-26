# TV-001: venv Python 3.13.5 with jsonschema 4.26.0

| Field | Value |
|---|---|
| Record | TV-001 |
| Status | **Validated** (2026-09-25; re-validated 2026-09-26 with the `minProperties` fault and the keyword survey, INSP-015 finding-1; re-run at commit `400e59d` on 2026-09-26, SRR package item R5). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: "the venv Python with `jsonschema`") |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; SWE-081 (section 5.1.4) for the version record |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1 rows `python3 (system)` and `python (venv)`, section 2 (packages), section 1.1 row `python (venv) + jsonschema` |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| Item | Value | Command |
|---|---|---|
| Interpreter version | `Python 3.13.5` | `/Users/robinonsay/rust/cwht/.venv/bin/python --version` |
| Interpreter binary | `/opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/bin/python3.13`, SHA-256 `a1f6d9dc20d4787a84dc2fe782094a7bac5946f49a962aa0af48a02f0e8d5bc5` | `python -c "import os,sys;print(os.path.realpath(sys.executable))"`; `shasum -a 256` |
| venv | created by `/opt/homebrew/opt/python@3.13/bin/python3.13 -m venv /Users/robinonsay/rust/cwht/.venv`, `include-system-site-packages = false` | `cat .venv/pyvenv.cfg` |
| jsonschema | `4.26.0`; installed `RECORD` SHA-256 `fee4cb8ffbd29704faa7b5af37792afdb75ef8cd4142ed7bd1885a4474a7e6da` | `.venv/bin/python -m pip show jsonschema`; `importlib.metadata` |
| jsonschema dependencies | jsonschema-specifications 2025.9.1 (`RECORD` SHA-256 `81556fd7...cb13cfd`), referencing 0.37.0 (`1f000e19...e7fe68`), rpds-py 2026.6.3 (`70e1b63f...d826b`), attrs 26.1.0 (`d5e36b4e...5d30`) | as above |
| Install source | Homebrew formula `python@3.13` 3.13.5, poured from a bottle on 2025-07-04 13:32 (`INSTALL_RECEIPT.json` in the Cellar directory; `brew info --json=v2 python@3.13`: installed 3.13.5, `poured_from_bottle` true); packages from PyPI through `pip install` | lock sections 1 and 2 |
| Installer URL and SHA-256 | Not recorded for the interpreter: the 3.13.5 bottle is no longer in the Homebrew cache and the formula now offers 3.13.15, whose bottle hash does not identify this install. The interpreter binary hash above identifies it; the SAR archive keeps a tar of `/opt/homebrew/Cellar/python@3.13/3.13.5` (lock section 7). Package wheels are recorded by `pip download` at SAR (lock section 7) | lock section 7 |

## 2. Purposes covered

1. Run the project Python tools (`tools/*.py`, `tools/slides/render_deck.py`, `tools/tests/`) with the Python 3.13.5 standard library.
2. Validate a JSON instance against a JSON Schema draft-07 document with jsonschema 4.26.0 (validator selected by `validators.validator_for` from `$schema`, schema checked with `check_schema`): accept a conforming instance with zero errors and report every violation with its absolute instance path and validator keyword, for the keywords `$ref` (into `definitions`), `allOf`, `anyOf`, `oneOf`, `if`/`then`/`else`, `not`, `const`, `enum`, `pattern`, `required`, `additionalProperties`, `propertyNames`, `minProperties`, `minItems`, `maxItems`, `uniqueItems`, `minLength`, `maxLength`, `minimum`, `maximum` and `type`.

Every keyword that the nine repository schemas use is in this list. Evidence: the keyword survey step of `evidence/python-jsonschema-2026-09-26.sh` walks `docs/**/*schema*.json` (nine files, all declaring `http://json-schema.org/draft-07/schema#`), lists 23 keywords and finds none missing from `keywords.schema.json`; its negative control, the 2026-09-25 fixture without `minProperties`, fails naming that keyword (`evidence/python-jsonschema-2026-09-26.log.txt`, runs 5 and 6). The survey of 2026-09-25 missed `minProperties` (`docs/plan/tpm.schema.json`, `margin_policy`) and wrongly said no schema used `maxItems` (`docs/process/rmm.schema.json` uses it); both were corrected on 2026-09-26 after review INSP-015 finding-1. The keyword lists of `allOf`, `oneOf` and the others in this purpose are the repository set, not a sample.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/schema/`: `known-answers.json` (expected results), case `requirement` (`requirements.schema.json`, a byte copy of `docs/requirements/schema.json` at git blob `ca049dfb`, commit `4e3f891`; `valid-requirement.json`; `invalid-requirement.json` with four seeded faults), case `keywords` (`keywords.schema.json`; `keywords-valid.json`; `keywords-invalid.json` with one seeded fault per keyword, each in its own array element, 19 in all; the `minProperties` fault `entries/16/margins` was added on 2026-09-26, INSP-015 finding-1). The expected errors were written by hand from the seeded faults before the first run.

**Run command** (from `tools/tests/fixtures/schema/`; the full procedure with the negative controls and the keyword survey is `docs/cm/tool-validation/evidence/python-jsonschema-2026-09-26.sh`; the 2026-09-25 version is kept for runs 1 to 4):

```
/Users/robinonsay/rust/cwht/.venv/bin/python -c '<CHECK>'
```

where `<CHECK>` loads `known-answers.json`, and for each case builds the validator class from the schema's `$schema`, runs `check_schema`, and compares the sorted list of `[absolute_path joined by "/", validator]` of `iter_errors` on the valid and on the invalid file with the stored list; it exits 0 only when the class and every list match (the program text is printed in the evidence transcript).

**Pass criteria:** validator class `Draft7Validator` for both schemas; `valid-requirement.json` and `keywords-valid.json` give no error; `invalid-requirement.json` gives exactly `requirements/0/verification_method` enum, `requirements/1/id` pattern, `requirements/2` required, `requirements/3/tbr` additionalProperties; `keywords-invalid.json` gives exactly the 19 stored pairs (`entries/0/id` pattern through `$ref`, `entries/1/kind` enum, `entries/2/version` const, `entries/3/score` maximum, `entries/4/score` minimum, `entries/5/tags` uniqueItems, `entries/6/tags/0` minLength, `entries/7/tags/0` maxLength, `entries/8/note` not, `entries/9/value` oneOf, `entries/10/owner` anyOf, `entries/11` required from `then`, `entries/12/tags` maxItems from `else`, `entries/13` additionalProperties, `entries/14` required, `entries/15/score` type, `entries/16/margins` minProperties, `list` minItems, `meta` pattern from `propertyNames`). **Negative control:** with seeded fault 1 of each case removed from a temporary copy, the check must exit 1. **Keyword survey** (added 2026-09-26): every keyword used by `docs/**/*schema*.json` is used by `keywords.schema.json` (exit 0); with `minProperties` removed from a temporary copy of the fixture schema, the survey must exit 1 naming it.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1, 2 | 2026-09-25 23:34 | `HEAD` `28e49e6`; fixture untracked (case `requirement` only) | pass; negative control exit 1 |
| 3, 4 | 2026-09-25 23:47 | `HEAD` `28e49e6`; fixture untracked (both cases; case `requirement` files unchanged) | pass; negative control exit 1 |
| 5, 6 | 2026-09-26 00:12 | `HEAD` `28e49e6`; fixture untracked (case `keywords` with the `minProperties` fault, 19 faults; procedure `python-jsonschema-2026-09-26.sh` with the keyword survey) | pass; both negative controls exit 1; survey: 9 schemas, 23 keywords, none missing |
| 7, 8 | 2026-09-26 02:31 | `HEAD` `400e59d` (SRR package item R5): an export of the commit (`git archive HEAD`), the fixture equal to `400e59d`; procedure of runs 5 and 6 unchanged (`python-jsonschema-2026-09-26-r5.sh` differs from `python-jsonschema-2026-09-26.sh` only in taking the tree as an argument) | pass; both negative controls exit 1; survey: 11 schemas, none missing |

Output excerpt (run 3):

```
jsonschema 4.26.0
case requirement requirements.schema.json Draft7Validator
  valid valid-requirement.json 0 errors [] MATCH
  invalid invalid-requirement.json 4 errors [...] MATCH
case keywords keywords.schema.json Draft7Validator
  valid keywords-valid.json 0 errors [] MATCH
  invalid keywords-invalid.json 18 errors [...] MATCH
PASS
exit=0
```

Output excerpt (run 5):

```
case keywords keywords.schema.json Draft7Validator
  valid keywords-valid.json 0 errors [] MATCH
  invalid keywords-invalid.json 19 errors [... ['entries/16/margins', 'minProperties'] ...] MATCH
PASS
exit=0
## keyword survey
schemas 9 repository keywords [... 'minProperties' ...]
not in fixture []
PASS
exit=0
## survey negative control
not in fixture ['minProperties']
FAIL
exit=1 (expected 1)
```

Evidence: `docs/cm/tool-validation/evidence/python-jsonschema-2026-09-25.log.txt` (runs 1 to 4, fixture file hashes, negative controls) and `evidence/python-jsonschema-2026-09-26.log.txt` (runs 5 and 6, the revised fixture's hashes, both negative controls, the keyword survey). The interpreter also ran every Python known-answer set of TV-002 to TV-010 (`evidence/python-tools-2026-09-25.log.txt`), which exercises purpose 1.

R5 re-run (2026-09-26, SRR package section 2.1 item R5; INSP-015 finding-2): section 3 run at commit `400e59d` on an export of the commit, so the result is bound to a commit that contains every file tested: every tool, test module and fixture identity line of the transcript reads "equal to HEAD". Evidence `evidence/python-jsonschema-2026-09-26-r5.log.txt` (procedure `evidence/python-jsonschema-2026-09-26-r5.sh`); the fixture file hashes in the transcript equal those of runs 5 and 6.

## 5. Reproducibility

Not required for class B (CM plan section 9.2 step 1). Runs 1 to 4 gave identical results for the fixture of their time, and runs 5 and 6 are identical to each other.

## 6. Limitations

1. Draft-07 only. A schema that declares another draft, or a keyword outside the list of purpose 2 (for example `format`, `dependencies`, `patternProperties`, `contains`, remote `$ref`), is outside the accreditation until this record is extended.
2. The fixture copy `requirements.schema.json` equals `docs/requirements/schema.json` today (checked by `cmp` in every run, informative only); a later edit of the repository schema does not invalidate this record, because the record validates jsonschema, not the schema.
3. The interpreter is a Homebrew install: `brew upgrade` would replace 3.13.5 by 3.13.15 silently. Until the owner runs `brew pin python@3.13` (an owner action, section 9), the lock row and the binary SHA-256 of section 1 are the only guard; each Python run for the record should confirm `Python 3.13.5`.
4. `tools/requirements.txt` is not yet pinned (lock section 2; CM plan AL-4): a rebuilt venv could install other package versions. The versions validated are those of section 1.
5. Purpose 1 is shown by the tools' own known-answer tests running under this interpreter, not by a separate test of the standard library.

## 7. Re-validation triggers

- Any version change of the interpreter, of jsonschema or of its four dependencies; a rebuilt venv (CM plan section 9.2 step 4).
- A macOS major version change (the interpreter binary is platform-specific).
- A change of any fixture file of section 3.
- A repository schema that uses a draft or keyword outside purpose 2 (the survey step of section 3 fails on it when the procedure is re-run).
- A defect found in jsonschema's reporting (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer checks this record against CM plan section 9.2 step 1, re-runs the command of section 3, and checks the fixture (each seeded fault yields exactly one error, the expected list is independent of the tool). Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-PYJS-001**: "Accredited for purposes 1 and 2 at Python 3.13.5 (binary SHA-256 `a1f6d9dc...8d5bc5`) with jsonschema 4.26.0 and the dependency versions of section 1, draft-07 and the 23 keywords of purpose 2 only (`$ref` into `definitions`, `allOf`, `anyOf`, `oneOf`, `if`/`then`/`else`, `not`, `const`, `enum`, `pattern`, `required`, `additionalProperties`, `propertyNames`, `minProperties`, `minItems`, `maxItems`, `uniqueItems`, `minLength`, `maxLength`, `minimum`, `maximum`, `type`)."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |

Owner action proposed with the decision: `brew pin python@3.13` (limitation 3).
