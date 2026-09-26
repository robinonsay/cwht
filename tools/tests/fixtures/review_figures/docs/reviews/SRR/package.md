# SRR Review Package (fixture for tools/tests/test_render_review_figures.py)

Miniature package with the three sections tools/render_review_figures.py reads; the counts below are the known answers of the test.

## 4. Entrance-criteria checklist

| # | Criterion (short) | Gate | Evidence artifact | Commit | Status | Note or proposed lien id |
|---|---|---|---|---|---|---|
| S1 | Agenda and success criteria agreed | Hard | this file | untracked | Not met (awaiting owner confirmation) | |
| S4 | Traceability report passes | Hard | traceability report | untracked | **Met** (tool rules) | Met on uncredited tool runs |
| 1 | Stakeholders and expectations | Hard | expectations.json | untracked | Partially met | INSP record missing |
| 2 | Goals and objectives | Soft at SRR | expectations.json | untracked | Met (content) | |

## 8. Requirements and traceability status

| Module | Requirements | Draft |
|---|---|---|
| SYS | 5 | 4 |

L1 requirements by functional group (fixture grouping):

| Functional group (REQ-SYS ids) | Requirements | Non-retired (Draft) | Retired (Closed, tag `retired`) | KDR | Goal | With open TBR | Test / Analysis / Inspection / Demonstration (non-retired) | Tagged `safety` | Tagged `regulatory` (non-retired) |
|---|---|---|---|---|---|---|---|---|---|
| Transmitter and emissions (001, 002, 003) | 3 | 2 | 1 | 1 | 0 | 1 | 1 / 1 / 0 / 0 | 0 | 0 |
| Receiver (004, 005) | 2 | 2 | 0 | 1 | 0 | 0 | 0 / 0 / 1 / 1 | 0 | 0 |
| Total | 5 | 4 | 1 | 2 | 0 | 1 | 1 / 1 / 1 / 1 | 0 | 0 |

### 8.1 Following subsection

Text after the grouping table.

## 20. Success criteria self-assessment

| # | Success criterion (short) | Evidence | Presenter assessment | Chair ruling (filled at review) | Lien id |
|---|---|---|---|---|---|
| 4.4-1 | L1 requirements respond to NGOs, MOEs and ConOps | section 8 | Not met until the validation records exist | | |
| 4.4-4 | External interfaces identified | concept | Met with lien not allowed (interfaces) | | |
| C1 | Gate criteria met or on liens | section 4 | Met | | |
