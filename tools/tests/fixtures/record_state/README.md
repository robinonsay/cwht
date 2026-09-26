# Fixture: record state rule of tools/validate_docs.py

Known answers for the record state rule (module docstring of `tools/validate_docs.py`; SRR package item R18, readiness finding R15-F2), run by `tools/tests/test_validate_docs.py` `RecordStateTests` with `validate_docs.validate_all` on this folder as `--root`. This folder is not a git work tree top, so the record drift rule is not applied.

| Record | Id | Front matter | Latest iteration section | Expected |
|---|---|---|---|---|
| `approved-historical-lines.md` | INSP-101 | APPROVED, readiness met, `findings_open: 0` | iteration 2 table: finding-1 Major Closed, finding-2 Minor Lien; historical lines and the iteration 1 table name finding-1 with Major and Open | PASS |
| `approved-latest-open-major.md` | INSP-102 | APPROVED, readiness met, `findings_open: 1` | iteration 2 table: finding-3 Major Open | FAIL: finding-3 open Major |
| `approved-open-count-unshown.md` | INSP-103 | APPROVED, `findings_open: 1` | every finding Closed | FAIL: findings_open not shown Minor |
| `approved-open-minor.md` | INSP-104 | APPROVED, `findings_open: 1` | finding-2 Minor Open | PASS |
| `approved-superseded-row.md` | INSP-105 | APPROVED, `findings_open: 0` | two iteration 3 blocks: F-01 Major Open, then F-01 Major Closed | PASS (the later row is current) |
| `approved-reviewer-needs-changes.md` | INSP-106 | APPROVED, `reviewer_verdict: NEEDS CHANGES` | every finding Closed | FAIL: reviewer_verdict |
| `needs-changes-open-major.md` | INSP-107 | NEEDS CHANGES | finding-1 Major Open | PASS (the rule applies to APPROVED only) |
