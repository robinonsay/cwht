# Fixture CM plan (tools/csa.py and tools/check_commit_msg.py known answers, TV-018 and TV-019)

Only Table 4-1 is read by the tools. Row 12 has no pathspec (outside the repository), row 3 has a
split CR-from event, row 4 and row 15 are Mixed, row 5 is the tools row whose files come under CR
control with their accreditation, and row 11 starts at the first release/FW-* tag.

### 4.2 Configuration item list (Table 4-1)

| # | CI | Pathspec | ID scheme | Class | CR from | Notes |
|---|---|---|---|---|---|---|
| 1 | Charter | `docs/process/00-charter.md` | n/a | CR | SRR | |
| 2 | L1 requirements | `docs/requirements/sys/` | REQ-SYS-NNN | CR | SRR | |
| 3 | Test cases | `docs/test_cases/` | TC-<MOD>-NNN | CR | SRR (cases citing L1 requirements); PDR (all other cases) | |
| 4 | Toolchain lock | `tools/toolchain.lock.md` | n/a | Mixed | SRR | |
| 5 | Tools | `tools/` (every file not in row 4; examples `ignored.py`) | TV-NNN | CR | date of the tool's TV record | |
| 6 | Tool validation records | `docs/cm/tool-validation/` | TV-NNN | Record | n/a | |
| 7 | Change requests | `docs/cm/cr/` | CR-NNN | Record | n/a | |
| 8 | Review records | `docs/reviews/` | INSP-NNN | Record | n/a | |
| 9 | Baseline records | `docs/reviews/*/baseline-record.md` | n/a | Record | n/a | |
| 10 | CM plan | `docs/process/05-*.md` | n/a | CR | SRR | |
| 11 | Firmware source | `firmware/` | FW-vX.Y.Z | CR | first `release/FW-*` tag | |
| 12 | External library | none (outside the repository) | commit SHA | CR | first `release/FW-*` tag | |
| 13 | Repository configuration | `.gitignore`, `*.gitkeep` | n/a | Log | n/a | |
| 14 | Deviations log | `docs/cm/deviations.md` | n/a | Record | n/a | |
| 15 | TPMs | `docs/plan/tpm.json` and its plots | TPM-NNN | Mixed | PDR | |
| 16 | Measurements | `docs/plan/measurements.json` | MSR-NN | Record | n/a | |
| 17 | Hazards | `docs/safety/hazards.json` | HZ-NNN | CR | PDR | |

Text after the table ends it.
