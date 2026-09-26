"""Known-answer tests for tools/measurements.py (SWE-136 tool validation; 07 sections 8.4, 9.2 and 11; MSR-13, 14, 18, 19).

Fixture tools/tests/fixtures/measurements/ (valid.json and invalid.json there belong to the
schema test of test_tools.py and are not used here):
  linkmap/cwht-app.map, link.ld  the committed FW-B0 map of docs/vv/reports/TC-SW-TOOL-001-r1/ and the
                                 rustos pico2 link.ld at the locked commit c54d35a; known answer
                                 FLASH 1608 B and RAM 8200 B, the values the SRR seed records MSR-18
                                 and MSR-19 transcribed from the gate log of TC-SW-TOOL-001-r1
  linkmap/over-red-line.map, small.ld  1 KiB regions; hand-computed FLASH 0x310 = 784 B (76.56 %,
                                 above the 70 % red line) and RAM 0x100 = 256 B (25 %)
  junit/                         run1 = run2-same (3 passed cases); run2-diff has one seeded failure;
                                 empty.xml has no case
  lcov/                          hand-counted totals per crate and an llvm-cov JSON export
  records/records.json           five records: a supersedes re-key, a Not yet measured record retired
                                 by the first Measured record, MSR-18 and MSR-19 citing the map

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_measurements.py
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import measurements as ms  # noqa: E402

FIXTURE = TOOLS / "tests" / "fixtures" / "measurements"
TOOL = TOOLS / "measurements.py"
GIT_ENV = {
    "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Fixture", "GIT_AUTHOR_EMAIL": "fixture@example.invalid", "GIT_AUTHOR_DATE": "2026-09-26T00:00:00+00:00",
    "GIT_COMMITTER_NAME": "Fixture", "GIT_COMMITTER_EMAIL": "fixture@example.invalid", "GIT_COMMITTER_DATE": "2026-09-26T00:00:00+00:00",
}


def run_cli(*args: str, root: Path | None = None) -> subprocess.CompletedProcess:
    env = dict(os.environ, **GIT_ENV)
    return subprocess.run([sys.executable, str(TOOL), "--root", str(root or TOOLS.parent), *args], capture_output=True, text=True, check=False, env=env)


def git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, env=dict(os.environ, **GIT_ENV))


def records_repo(tmp: str) -> Path:
    """A git repository holding the records fixture and its evidence, committed together."""
    root = Path(tmp) / "repo"
    (root / "docs/plan").mkdir(parents=True)
    (root / "evidence").mkdir()
    shutil.copy(FIXTURE / "records/records.json", root / "docs/plan/measurements.json")
    shutil.copy(FIXTURE / "linkmap/cwht-app.map", root / "evidence/cwht-app.map")
    shutil.copy(FIXTURE / "linkmap/link.ld", root / "link.ld")
    git(root, "init", "-q", "-b", "main")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "fixture")
    return root


class LinkMapTests(unittest.TestCase):
    def test_fw_b0_map_reproduces_the_seed_records(self) -> None:
        usage = ms.link_map_usage((FIXTURE / "linkmap/cwht-app.map").read_text(encoding="utf-8"), (FIXTURE / "linkmap/link.ld").read_text(encoding="utf-8"))
        self.assertEqual((1608, 4194304, 8200, 532480), (usage["FLASH"]["used"], usage["FLASH"]["length"], usage["RAM"]["used"], usage["RAM"]["length"]))
        self.assertEqual(
            {"MSR-18": {"bytes": 1608, "percent_of_4MB": 0.04, "assessment": "Green"}, "MSR-19": {"bytes": 8200, "percent_of_520KB": 1.54, "assessment": "Green"}},
            ms.msr_18_19(usage),
        )

    def test_red_line(self) -> None:
        result = run_cli("--link-map", str(FIXTURE / "linkmap/over-red-line.map"), "--link-ld", str(FIXTURE / "linkmap/small.ld"))
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertEqual(
            ["FAIL FLASH used 784 B of 1024 B = 76.56 % (red line 70.0 % used, TPM-010)", "PASS RAM used 256 B of 1024 B = 25.00 % (red line 75.0 % used, TPM-011)"],
            result.stdout.splitlines()[:2],
        )

    def test_pass_on_the_fw_b0_map(self) -> None:
        result = run_cli("--link-map", str(FIXTURE / "linkmap/cwht-app.map"), "--link-ld", str(FIXTURE / "linkmap/link.ld"))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("MSR-18 bytes 1608, percent_of_4MB 0.04, assessment Green", result.stdout)

    def test_assessment_rules(self) -> None:
        self.assertEqual(["Green", "Yellow", "Red"], [ms.assess(p, ms.MSR18_RULE) for p in (25.0, 25.01, 50.01)])
        self.assertEqual(["Green", "Yellow", "Red"], [ms.assess(p, ms.MSR19_RULE) for p in (40.0, 40.5, 60.5)])

    def test_missing_map_or_region_is_a_usage_error(self) -> None:
        self.assertEqual(2, run_cli("--link-map", str(FIXTURE / "linkmap/none.map"), "--link-ld", str(FIXTURE / "linkmap/small.ld")).returncode)
        with self.assertRaises(ms.UsageError):
            ms.link_map_usage("", (FIXTURE / "linkmap/small.ld").read_text(encoding="utf-8"))


class DiffRunsTests(unittest.TestCase):
    def test_identical_runs_pass(self) -> None:
        result = run_cli("--diff-runs", str(FIXTURE / "junit/run1.xml"), str(FIXTURE / "junit/run2-same.xml"))
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual("run 1: 3 cases, run 2: 3 cases, passed in both: 3", result.stdout.splitlines()[0])

    def test_seeded_difference_fails(self) -> None:
        result = run_cli("--diff-runs", str(FIXTURE / "junit/run1.xml"), str(FIXTURE / "junit/run2-diff.xml"))
        self.assertEqual(1, result.returncode)
        self.assertIn("DIFF run 1 only ('cwht-core::heartbeat', 'spin_wait_counts', 'passed')", result.stdout)
        self.assertIn("DIFF run 2 only ('cwht-core::heartbeat', 'spin_wait_counts', 'failure')", result.stdout)

    def test_empty_run_fails(self) -> None:
        result = run_cli("--diff-runs", str(FIXTURE / "junit/empty.xml"), str(FIXTURE / "junit/empty.xml"))
        self.assertEqual(1, result.returncode)
        self.assertIn("FAIL run 1 holds no test case", result.stdout)


class CoverageTests(unittest.TestCase):
    def test_totals(self) -> None:
        result = run_cli("--coverage", str(FIXTURE / "lcov/lcov.info"), "--branch-condition", str(FIXTURE / "lcov/branch-condition.json"))
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(
            [
                "MSR-13 cwht-core: lines 23/24 = 95.83 %, functions 4/4 = 100.00 %, branches 0/0 = n/a (regions: cargo llvm-cov report)",
                "MSR-13 cwht-hal-mock: lines 5/10 = 50.00 %, functions 1/2 = 50.00 %, branches 2/4 = 50.00 % (regions: cargo llvm-cov report)",
                "MSR-13 rustos/pico2: lines 0/0 = n/a, functions 0/0 = n/a, branches 0/0 = n/a (regions: cargo llvm-cov report)",
                "MSR-14 branches: 6/8 = 75.00 %",
                "MSR-14 functions: 5/6 = 83.33 %",
                "MSR-14 lines: 28/34 = 82.35 %",
                "emulation report NOT PRODUCED (no --emu): tools/emu_run.sh prints SKIP until the PDR emulator ADR",
            ],
            result.stdout.splitlines(),
        )

    def test_optional_inputs_not_produced_and_lcov_required(self) -> None:
        result = run_cli("--coverage", str(FIXTURE / "lcov/lcov.info"), "--branch-condition", "/nonexistent/branch.json", "--emu", "/nonexistent/emu.json")
        self.assertEqual(0, result.returncode)
        self.assertIn("MSR-14 NOT PRODUCED (/nonexistent/branch.json)", result.stdout)
        self.assertEqual(2, run_cli("--coverage", "/nonexistent/lcov.info").returncode)


class RecordsTests(unittest.TestCase):
    def test_committed_records_pass_and_values_are_rederived(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = records_repo(tmp)
            result = run_cli("--check-records", "--link-ld", "link.ld", root=root)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("value re-derived from evidence/cwht-app.map: {'bytes': 1608, 'percent_of_4MB': 0.04, 'assessment': 'Green'}", result.stdout)
        self.assertIn("value re-derived from evidence/cwht-app.map: {'bytes': 8200, 'percent_of_520KB': 1.54, 'assessment': 'Green'}", result.stdout)
        self.assertIn("NOTE 2 evidence hash(es) checked", result.stdout)

    def test_seeded_record_faults(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = records_repo(tmp)
            path = root / "docs/plan/measurements.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["records"][2]["value"]["bytes"] = 1609  # edits a committed record: append-only and re-derivation both fail
            extra = dict(data["records"][3], id="MSR-29", date="2026-09-24", scope="new scope", supersedes={"id": "MSR-29", "scope": "none", "date": "2026-09-01"})
            data["records"].append(extra)
            path.write_text(json.dumps(data), encoding="utf-8")
            (root / "evidence/cwht-app.map").write_text("changed\n", encoding="utf-8")
            result = run_cli("--check-records", "--link-ld", "link.ld", root=root)
        fails = [line for line in result.stdout.splitlines() if line.startswith("FAIL")]
        self.assertEqual(1, result.returncode)
        self.assertEqual(
            [
                "FAIL records[5] MSR-29 'new scope': id is not in the 07 section 11.2 catalog MSR-01 to MSR-28",
                "FAIL records[5] MSR-29 'new scope': date 2026-09-24 is earlier than the record before it (2026-09-26); records are appended (07 section 11.1)",
                "FAIL records[5] MSR-29 'new scope': supersedes MSR-29 'none' 2026-09-01, which is not an earlier record",
                "FAIL records differ from HEAD at index 2: records are appended, never edited or deleted (07 section 11.1)",
                "FAIL records[2] MSR-18 'cwht-app release image (thumbv8m.main-none-eabihf)' 2026-09-25: evidence evidence/cwht-app.map sha256 differs at the working tree (record not yet committed); at HEAD: equal to the record (07 section 11.1 evidence preservation)",
                "FAIL records[5] MSR-29 'new scope' 2026-09-24: evidence evidence/cwht-app.map sha256 differs at the working tree (record not yet committed); at HEAD: equal to the record (07 section 11.1 evidence preservation)",
            ],
            fails,
        )
        # The edited records[2] is in no commit, so its evidence is checked in the working tree, where the map
        # changed; the unedited records[3] is checked at the fixture commit and passes.
        self.assertFalse(any("records[3]" in f for f in fails))

    def test_rederivation_mismatch_in_a_commit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = records_repo(tmp)
            path = root / "docs/plan/measurements.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["records"][3]["value"]["bytes"] = 8199
            path.write_text(json.dumps(data), encoding="utf-8")
            git(root, "commit", "-q", "-am", "edit")
            result = run_cli("--check-records", "--link-ld", "link.ld", root=root)
        self.assertEqual(1, result.returncode)
        self.assertIn("re-derived value differs from the record: {'bytes': (8199, 8200)}", result.stdout)

    def test_git_rules_not_applied_outside_a_work_tree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "plain"
            (root / "docs/plan").mkdir(parents=True)
            shutil.copy(FIXTURE / "records/records.json", root / "docs/plan/measurements.json")
            data = json.loads((root / "docs/plan/measurements.json").read_text(encoding="utf-8"))
            data["updated"] = "2026-09-25"
            (root / "docs/plan/measurements.json").write_text(json.dumps(data), encoding="utf-8")
            result = run_cli("--check-records", root=root)
        self.assertEqual(1, result.returncode)
        self.assertIn("FAIL updated is 2026-09-25 but the latest record date is 2026-09-26 (07 section 11.1)", result.stdout)
        self.assertIn("is not the top of a git work tree", result.stdout)

    def test_analyze_current_records(self) -> None:
        result = run_cli("--analyze", "--file", "records/records.json", root=FIXTURE)
        self.assertEqual(0, result.returncode, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(
            [
                "MSR-17 | firmware workspace and rustos api, pico2 | Not yet measured | null | Not assessed | 2026-09-26",
                'MSR-18 | cwht-app release image (thumbv8m.main-none-eabihf) | Measured | {"bytes":1608,"percent_of_4MB":0.04} | Green | 2026-09-25',
                'MSR-19 | cwht-app release image (thumbv8m.main-none-eabihf) | Measured | {"bytes":8200,"percent_of_520KB":1.54} | Green | 2026-09-25',
                "current records: Green 2, Not assessed 1; 3 of 5 records are current",
            ],
            lines,
        )


class UsageTests(unittest.TestCase):
    def test_usage_errors_exit_two(self) -> None:
        self.assertEqual(2, run_cli().returncode, "a mode is required")
        self.assertEqual(2, run_cli("--analyze", "--diff-runs", "a", "b").returncode, "modes are exclusive")
        self.assertEqual(2, run_cli("--analyze", "--file", "none.json", root=FIXTURE).returncode)


if __name__ == "__main__":
    unittest.main()
