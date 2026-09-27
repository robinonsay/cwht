"""Builds the fixture git repository of the tools/csa.py and tools/check_commit_msg.py known answers
(TV-018, TV-019) in a directory given by the caller. Deterministic: fixed author and committer
names, e-mail and dates, no signing, no hooks, no user or system git configuration read.

The commit plan (COMMITS) is the input the expected answers in expected.json were derived from by
hand. Each commit states which rules of tools/check_commit_msg.py it exercises.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))

README_TV = """# Tool validation records (fixture)

## Index

| Record | Tool and version | Class | Due (CM plan section 13) | Status |
|---|---|---|---|---|
| [TV-001](TV-001-trace.md) | `tools/trace.py` (blob fixture) | B | SRR | Validated; reviewed and **Accredited** 2026-09-26 |
| [TV-002](TV-002-newtool.md) | `tools/newtool.py` | B | PDR | Validated; review pending |

## Evidence

Nothing.
"""

DEVIATIONS = """# CM deviations log (fixture)

## Entries

| # | Date | Procedure departed from | Departure | RFA raised | Closure plan | Status |
|---|---|---|---|---|---|---|
| 1 | 2026-09-26 | 05 section 5.2 | CR-001 dispositioned before its impact review | RFA-SRR-001 | review | Closed |

## Closures

| Entry | Date | Evidence |
|---|---|---|
| 1 | 2026-09-27 | Closed at the fixture commit |
"""


def cr(num: int, title: str, status: str, disposition: str | None, cis: list[int], disp_date: str | None) -> str:
    return (f"---\nid: CR-{num:03d}\ntitle: {title}\nstatus: {status}\nclass: I\noriginator: Claude\ndate_opened: 2026-09-26\n"
            f"affected_cis: [{', '.join(map(str, cis))}]\ntarget_release: none\ndisposition: {disposition or 'null'}\n"
            f"disposition_date: {disp_date or 'null'}\nmerge_sha: null\ndate_closed: null\n---\n\n# CR-{num:03d}: {title}\n")


def record(insp: str, verdict: str, product: str, files: list[str]) -> str:
    pf = ", ".join(f'"{f}@0000000000000000000000000000000000000000"' for f in files)
    return (f"---\n# fixture record\nid: {insp}\nchecklist: peer-review-checklist-code\nproduct: {product}\n"
            f"product_files: [{pf}]\nverdict: {verdict}\n---\n\n# Record {insp}\n")


BASE = {
    "docs/process/00-charter.md": "# Charter (fixture)\n",
    "docs/process/05-configuration-and-data-management.md": None,  # copied from cm-plan-05.md
    "docs/requirements/sys/requirements.json": json.dumps({"module": "SYS", "requirements": [
        {"id": "REQ-SYS-001", "tbr": {"owner": "o", "plan": "p", "close_by": "PDR"}},
        {"id": "REQ-SYS-002", "tbr": {"owner": "o", "plan": "p", "close_by": "PDR"}},
        {"id": "REQ-SYS-003", "tbr": {"owner": "o", "plan": "p", "close_by": "CDR"}},
        {"id": "REQ-SYS-004"}]}, indent=1) + "\n",
    "docs/test_cases/sys/test_cases.json": "{}\n",
    "tools/toolchain.lock.md": "# Lock (fixture)\n",
    "tools/trace.py": "print('trace')\n",
    "docs/cm/tool-validation/README.md": README_TV,
    "docs/cm/cr/CR-001-firmware.md": cr(1, "Firmware arms", "Dispositioned", "Approved", [11], "2026-09-26"),
    "docs/reviews/SRR/checklists/requirements.md": record("INSP-001", "APPROVED", "docs/requirements/sys/requirements.json",
                                                          ["docs/requirements/sys/requirements.json"]),
    "docs/reviews/SRR/checklists/firmware.md": record("INSP-002", "NEEDS CHANGES", "firmware/src/main.rs", ["firmware/src/main.rs"]),
    "docs/reviews/SRR/decision-memo.md": "# Memo\n\n| Date | Item | Text |\n|---|---|---|\n"
                                         "| 2026-09-26 | A-1 | <a id=\"W1\"></a>Waiver of readiness R3 for FW-B0 | \n",
    "docs/reviews/SRR/rfa-rid-log.json": json.dumps({"review": "SRR", "items": [
        {"id": "RID-SRR-001", "state": "Open", "title": "Open item"},
        {"id": "RID-SRR-002", "state": "Closed", "title": "Closed item"},
        {"id": "RFA-SRR-001", "state": "Answered", "title": "Answered item"}]}, indent=1) + "\n",
    "docs/reviews/SRR/baseline-record.md": "# Baseline record (fixture)\n",
    "firmware/src/main.rs": "fn main() {}\n",
    ".gitignore": ".venv/\n",
    "hardware/kicad/.gitkeep": "",
    "docs/cm/deviations.md": DEVIATIONS,
    "docs/plan/tpm.json": json.dumps({"tpms": [{"id": "TPM-001", "tbr": {"owner": "o", "plan": "p", "close_by": "PDR"}},
                                                {"id": "TPM-002"}]}, indent=1) + "\n",
    "docs/plan/measurements.json": json.dumps({"records": [
        {"id": "MSR-02", "state": "Not yet measured", "value": None, "unit": "%", "date": "2026-09-25"},
        {"id": "MSR-02", "state": "Measured", "value": 12.5, "unit": "%", "date": "2026-10-01"}]}, indent=1) + "\n",
    "docs/safety/hazards.json": json.dumps({"hazards": [{"id": "HZ-001", "controls": [
        {"id": "K1", "tbr": {"owner": "o", "plan": "p", "close_by": "PDR"}}, {"id": "K2"}]}]}, indent=1) + "\n",
}

# (subject and trailers, {path: content or None to delete}, note). Dates: 2026-10-01T10:MM:00-05:00.
COMMITS = [
    ("docs(cm): submit CR-002\n\nRefs: CR-002\n", {"docs/cm/cr/CR-002-typo.md": cr(2, "Requirement typo", "Submitted", None, [2], None)},
     "PASS: Record row with Refs"),
    ("docs(requirements): fix a typo\n", {"docs/requirements/sys/requirements.md": "typo fixed\n"},
     "REFS_MISSING and CR_TRAILER_MISSING: row 2 after baseline/srr"),
    ("docs(requirements): apply CR-002\n\nRefs: CR-002\nCR: CR-002\n", {"docs/requirements/sys/requirements.md": "applied\n"},
     "PASS: CR trailer"),
    ("editorial(requirements): spelling\n\nRefs: SRR\nEditorial: spelling only\n", {"docs/requirements/sys/requirements.md": "spelt\n"},
     "PASS with an Editorial trailer (editorial log)"),
    ("docs(test_cases): add a case\n\nRefs: TC-SYS-001\n", {"docs/test_cases/sys/test_cases.json": "{\"a\": 1}\n"},
     "WARN SPLIT_CR_FROM: row 3"),
    ("chore(tools): lock re-observation\n\nRefs: TV-001\n", {"tools/toolchain.lock.md": "# Lock (fixture) observed\n"},
     "WARN MIXED_ROW: row 4"),
    ("tool(trace): change an accredited tool\n\nRefs: TV-001\n", {"tools/trace.py": "print('trace 2')\n"},
     "CR_TRAILER_MISSING: row 5, accredited tools/trace.py"),
    ("tool(newtool): add a tool without accreditation\n\nRefs: TV-002\n", {"tools/newtool.py": "print('new')\n"},
     "PASS: row 5 file not accredited"),
    ("Status note\n", {"docs/plan/status/status-2026-10-01.md": "note\n"},
     "SUBJECT only: the file matches no row, so no Refs is required"),
    ("docs(reviews): add a record\n\nRefs: WP-PDR-99\n", {"docs/reviews/PDR/checklists/x.md": "x\n"},
     "REFS_UNRECOGNIZED"),
    ("fix(firmware): change code before any release tag\n\nRefs: CR-001\n", {"firmware/src/main.rs": "fn main() { }\n"},
     "PASS: row 11 CR-from event (release/FW-*) has not occurred"),
    ("docs(cm): bad CR trailer\n\nRefs: CR-002\nCR: 12\n", {"docs/cm/cr/CR-004-other.md": cr(4, "Other", "Draft", None, [7], None)},
     "CR_ID_BAD"),
    ("docs(requirements): refs line not a trailer\n\nRefs: CR-002\n\nCo-Authored-By: Claude <noreply@anthropic.com>\n",
     {"docs/requirements/sys/requirements.md": "blank line\n"},
     "REFS_MISSING and CR_TRAILER_MISSING: git does not read the Refs line as a trailer"),
]
BRANCH_COMMIT = ("docs(requirements): CR-002 product change on its branch\n\nRefs: CR-002\nCR: CR-002\n",
                 {"docs/requirements/sys/requirements.md": "branch change\n"})
MERGE_SUBJECT = "merge(CR-002): apply the requirement typo fix\n\nRefs: CR-002\n"


def git(dest: str, *args: str, date: str | None = None) -> str:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": dest, "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_CONFIG_GLOBAL": os.devnull, "GIT_AUTHOR_NAME": "Fixture", "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
           "GIT_COMMITTER_NAME": "Fixture", "GIT_COMMITTER_EMAIL": "fixture@example.invalid", "TZ": "UTC"}
    if date:
        env.update({"GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date})
    r = subprocess.run(["git", "-C", dest, "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false",
                        "-c", "core.hooksPath=/dev/null", "-c", "init.defaultBranch=main", *args],
                       capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr}")
    return r.stdout.strip()


def write(dest: str, files: dict) -> None:
    for path, content in files.items():
        full = os.path.join(dest, path)
        if content is None:
            os.remove(full)
            continue
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(content)


def build(dest: str) -> dict:
    """Create the repository in dest (which must not exist) and return {label: sha}."""
    os.makedirs(dest)
    git(dest, "init", "-q")
    base = dict(BASE)
    with open(os.path.join(HERE, "cm-plan-05.md"), encoding="utf-8") as fh:
        base["docs/process/05-configuration-and-data-management.md"] = fh.read()
    write(dest, base)
    git(dest, "add", "-A")
    shas = {}
    git(dest, "commit", "-q", "-m", "docs(process): fixture baseline content\n\nRefs: SRR\n", date="2026-09-30T09:00:00-05:00")
    shas["base"] = git(dest, "rev-parse", "HEAD")
    git(dest, "tag", "-a", "baseline/srr", "-m", "SRR baseline (fixture)", date="2026-09-30T09:30:00-05:00")
    for i, (message, files, _note) in enumerate(COMMITS, 1):
        write(dest, files)
        git(dest, "add", "-A")
        git(dest, "commit", "-q", "-m", message, date=f"2026-10-01T10:{i:02d}:00-05:00")
        shas[f"c{i}"] = git(dest, "rev-parse", "HEAD")
    git(dest, "checkout", "-q", "-b", "cr/CR-002-typo")
    write(dest, BRANCH_COMMIT[1])
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", BRANCH_COMMIT[0], date="2026-10-01T11:00:00-05:00")
    shas["branch"] = git(dest, "rev-parse", "HEAD")
    git(dest, "checkout", "-q", "main")
    git(dest, "merge", "-q", "--no-ff", "-m", MERGE_SUBJECT, "cr/CR-002-typo", date="2026-10-01T11:30:00-05:00")
    shas["merge"] = git(dest, "rev-parse", "HEAD")
    return shas


if __name__ == "__main__":
    import sys
    out = sys.argv[1]
    if os.path.exists(out):
        shutil.rmtree(out)
    print(json.dumps(build(out), indent=1))
