"""Known-answer tests for tools/check_commit_msg.py (TV-019; CM plan 05 section 4.5 "Commit message",
"Merges to main" and "Checks").

Fixture: the git repository built by tools/tests/fixtures/csa/build_repo.py (shared with TV-018) and
the per-commit answers of tools/tests/fixtures/csa/expected.json block "check_commit_msg", derived
by hand from the commit plan before the first run.

Fixture-only classes (the validation):
  RangeTests         audit mode over baseline/srr..HEAD: every commit's FAIL and WARN rules equal the
                     expected ones; exit 1 because FAIL findings exist; exit 0 on a clean range
  HookTests          hook mode in a clone: staged files and HEAD as parent; a bad message fails with
                     REFS_MISSING and CR_TRAILER_MISSING, a good one passes; comment lines ignored;
                     a message whose Refs line git does not read as a trailer fails
  SubjectTests       every 05 section 4.5 type passes, others fail; merge type only on merges
  RefsTests          recognized identifier kinds, and a Refs of only unrecognized tokens
  UsageTests         every usage error and a git failure exit 2
Repository-content check, recorded separately (lock section 1.1):
  RepositoryTests    baseline/srr..9fd0962: exactly the three commits the hand CSA issue 1 names in
                     its trailer metric (1535cd5, 1fe9c1a, 9fd0962) fail REFS_MISSING

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_check_commit_msg.py -v
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "check_commit_msg.py")
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "csa")
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, FIXTURE)
import build_repo  # noqa: E402
import check_commit_msg  # noqa: E402
import csa  # noqa: E402

with open(os.path.join(FIXTURE, "expected.json")) as _fh:
    EXP = json.load(_fh)["check_commit_msg"]
with open(os.path.join(FIXTURE, "cm-plan-05.md")) as _fh:
    TABLE = csa.parse_table41(_fh.read())


def run(*args, cwd=None):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True, cwd=cwd)


class FixtureRepo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.repo = os.path.join(cls.tmp.name, "repo")
        cls.shas = build_repo.build(cls.repo)
        cls.label = {v[:7]: k for k, v in cls.shas.items()}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()


class RangeTests(FixtureRepo):
    def test_every_commit(self):
        r = run("--root", self.repo, "--range", "baseline/srr..HEAD")
        self.assertEqual(r.returncode, 1, r.stderr)
        got = {}
        for line in r.stdout.splitlines():
            m = re.match(r"^(FAIL|WARN|PASS)(?: (\w+))? ([0-9a-f]{7})", line)
            if m:
                got.setdefault(self.label[m.group(3)], [])
                if m.group(1) != "PASS":
                    got[self.label[m.group(3)]].append([m.group(1), m.group(2)])
        self.assertEqual(got, EXP)
        self.assertIn("15 commit(s) in baseline/srr..HEAD; FAIL", r.stdout)

    def test_clean_range_exit_0(self):
        r = run("--root", self.repo, "--range", f"{self.shas['c2']}..{self.shas['c4']}")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("2 commit(s)", r.stdout)

    def test_check_commit_api_matches_cli(self):
        ctx = check_commit_msg.Context(self.repo, TABLE)
        info = check_commit_msg.check_commit(self.repo, self.shas["c7"], TABLE, ctx)
        self.assertEqual(info["rows"], [5])
        self.assertEqual([f["rule"] for f in info["findings"]], ["CR_TRAILER_MISSING"])
        merge = check_commit_msg.check_commit(self.repo, self.shas["merge"], TABLE, ctx)
        self.assertEqual((merge["rows"], merge["findings"]), ([2], []))


class HookTests(FixtureRepo):
    def setUp(self):
        self.clone = os.path.join(self.tmp.name, f"clone-{self._testMethodName}")
        subprocess.run(["git", "clone", "-q", self.repo, self.clone], check=True, capture_output=True)
        with open(os.path.join(self.clone, "docs", "requirements", "sys", "requirements.md"), "a") as fh:
            fh.write("hook change\n")
        subprocess.run(["git", "-C", self.clone, "add", "-A"], check=True)
        self.msg = os.path.join(self.tmp.name, f"MSG-{self._testMethodName}")

    def hook(self, text):
        with open(self.msg, "w") as fh:
            fh.write(text)
        return run(self.msg, cwd=self.clone)

    def test_bad_message_fails(self):
        r = self.hook("docs(requirements): change\n")
        self.assertEqual(r.returncode, 1)
        self.assertIn("FAIL REFS_MISSING", r.stdout)
        self.assertIn("FAIL CR_TRAILER_MISSING", r.stdout)

    def test_good_message_passes(self):
        r = self.hook("docs(requirements): change\n\nRefs: CR-002\nCR: CR-002\n")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("PASS MSG-test_good_message_passes: rows 2; Refs: CR-002", r.stdout)

    def test_comment_lines_ignored(self):
        r = self.hook("docs(requirements): change\n\nRefs: CR-002\nCR: CR-002\n# Please enter the commit message\n# Changes:\n")
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_refs_separated_by_blank_line_is_not_a_trailer(self):
        r = self.hook("docs(requirements): change\n\nRefs: CR-002\nCR: CR-002\n\nCo-Authored-By: A <a@example.invalid>\n")
        self.assertEqual(r.returncode, 1)
        self.assertIn("FAIL REFS_MISSING", r.stdout)

    def test_message_file_mode(self):
        with open(self.msg, "w") as fh:
            fh.write("chore(tools): lock\n\nRefs: TV-001\n")
        r = run("--root", self.repo, "--message-file", self.msg, "--files", "tools/toolchain.lock.md", "--parent", self.shas["c1"])
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("WARN MIXED_ROW", r.stdout)


class SubjectTests(FixtureRepo):
    def evaluate(self, subject, is_merge=None):
        ctx = check_commit_msg.Context(self.repo, TABLE)
        return [f["rule"] for f in check_commit_msg.evaluate(ctx, subject + "\n", [], self.shas["c1"], is_merge)["findings"]]

    def test_types(self):
        for t in check_commit_msg.TYPES:
            if t != "merge":
                with self.subTest(type=t):
                    self.assertEqual(self.evaluate(f"{t}(scope): summary"), [])
        for bad in ("Docs(x): y", "docs: no scope", "docs(x):missing space", "wip(x): y", "docs( x): y", "Status note"):
            with self.subTest(subject=bad):
                self.assertEqual(self.evaluate(bad), ["SUBJECT"])

    def test_merge_type(self):
        self.assertEqual(self.evaluate("merge(CR-002): title", is_merge=True), [])
        self.assertEqual(self.evaluate("merge(slug): title", is_merge=False), ["SUBJECT"])
        self.assertEqual(self.evaluate("docs(x): title", is_merge=True), ["SUBJECT"])


class RefsTests(unittest.TestCase):
    def test_recognized_kinds(self):
        for token in ("REQ-SYS-001", "REQ-SW-KEYER-012", "TC-SW-TOOL-001", "ICD-CTL-SW", "ADR-018", "TS-003", "RSK-009",
                      "HZ-001", "NCR-001", "RFA-SRR-003", "RID-TRR-D2-001", "SI-027", "TV-015", "CR-007", "INSP-038",
                      "MSR-02", "OQ-VV-001", "ACC-LTSPICE-001", "WP-SW-08", "SW-01-keyer", "FW-v0.9.0-rc1",
                      "HW-MB-revA-1", "ME-ENC-revA-1", "CWHT-A-001", "SRR", "PDR", "TRR-D1", "TPM-003", "MOE-001"):
            with self.subTest(token=token):
                self.assertTrue(check_commit_msg.RECOGNIZED.match(token))
        for token in ("WP-PDR-07", "RSK ids", "CR-7", "baseline/srr"):
            with self.subTest(token=token):
                self.assertFalse(check_commit_msg.RECOGNIZED.match(token))


class UsageTests(FixtureRepo):
    def test_usage_errors_exit_2(self):
        msg = os.path.join(self.tmp.name, "m.txt")
        with open(msg, "w") as fh:
            fh.write("docs(x): y\n")
        cases = [
            ("--root", self.repo),                                              # no mode
            ("--root", self.repo, msg, "--range", "HEAD~1..HEAD"),              # two modes
            ("--root", self.repo, msg, "--files", "a"),                         # --files without --message-file
            ("--root", self.repo, os.path.join(self.tmp.name, "absent.txt")),   # unreadable message file
            ("--root", self.repo, "--range", "nope..HEAD"),                     # git failure
            ("--bogus",),
        ]
        for args in cases:
            with self.subTest(args=args):
                self.assertEqual(run(*args).returncode, 2)


class RepositoryTests(unittest.TestCase):
    """Repository content: the trailer metric of the hand CSA issue 1 (b790eaa) at 9fd0962."""

    def test_hand_csa_trailer_metric(self):
        r = run("--root", ROOT, "--range", "baseline/srr..9fd0962")
        missing = sorted(set(re.findall(r"^FAIL REFS_MISSING ([0-9a-f]{7})", r.stdout, re.M)))
        self.assertEqual(missing, ["1535cd5", "1fe9c1a", "9fd0962"])
        self.assertNotIn("CR_TRAILER_MISSING", r.stdout)


if __name__ == "__main__":
    unittest.main()
