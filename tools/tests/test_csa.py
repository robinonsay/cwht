"""Known-answer tests for tools/csa.py (TV-018; CM plan 05 section 6, Table 4-1 and section 4.2).

Fixture-only classes (the validation):
  Table41ParseTests     the Table 4-1 reader on tools/tests/fixtures/csa/cm-plan-05.md (pathspecs in
                        parentheses ignored, row without a pathspec) and its failures
  MatchRuleTests        the 05 section 4.2 matching rule on hand-written tables: an explicit path
                        or file-name pattern wins over a directory prefix, the longest prefix wins,
                        * matches /, [...] classes, ties and unmatched paths
  FrontMatterTests      the front-matter reader on CR and record headers
  FixtureRepoTests      every section of the report on the fixture repository of build_repo.py
                        against the hand-derived answers of expected.json
  CliTests              --write/--output/--check/--json/--strict and the exit statuses 0, 1, 2
Repository-content check, recorded separately (lock section 1.1):
  HandCsaTests          at 9fd0962 the derivable values equal the hand CSA issue 1 (b790eaa):
                        tracked files, per-row file counts, hashes and last commits, the unmatched
                        files, the change log (rows touched and Refs) and the commits lacking
                        trailers (tools/tests/fixtures/csa/hand-csa-9fd0962.json)

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_csa.py -v
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
TOOL = os.path.join(ROOT, "tools", "csa.py")
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "csa")
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, FIXTURE)
import build_repo  # noqa: E402
import csa  # noqa: E402

with open(os.path.join(FIXTURE, "expected.json")) as _fh:
    EXP = json.load(_fh)
with open(os.path.join(FIXTURE, "cm-plan-05.md")) as _fh:
    PLAN = _fh.read()


def run(*args):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True)


class Table41ParseTests(unittest.TestCase):
    def test_fixture_table(self):
        rows = csa.parse_table41(PLAN)
        self.assertEqual([r.num for r in rows], list(range(1, 18)))
        self.assertEqual(rows[4].specs, ["tools/"])            # `ignored.py` in parentheses is not a pathspec
        self.assertEqual(rows[11].specs, [])                   # row 12: none (outside the repository)
        self.assertEqual(rows[12].specs, [".gitignore", "*.gitkeep"])
        self.assertEqual(rows[2].cr_from, "SRR (cases citing L1 requirements); PDR (all other cases)")
        self.assertEqual(rows[3].cls, "Mixed")

    def test_real_cm_plan_parses_55_rows_or_more(self):
        with open(os.path.join(ROOT, csa.CM_PLAN)) as fh:
            rows = csa.parse_table41(fh.read())
        self.assertGreaterEqual(len(rows), 55)
        self.assertEqual(rows[27].specs[0], "tools/")          # row 28
        self.assertNotIn("package.json", rows[27].specs)       # inside parentheses

    def test_missing_table_is_an_error(self):
        with self.assertRaises(csa.CsaError):
            csa.parse_table41("# no table here\n")

    def test_misnumbered_table_is_an_error(self):
        with self.assertRaises(csa.CsaError):
            csa.parse_table41(PLAN.replace("| 3 | Test cases", "| 30 | Test cases"))


class MatchRuleTests(unittest.TestCase):
    def table(self, *specs_per_row):
        return [csa.CiRow(i + 1, f"row {i + 1}", list(specs), "Log", "n/a", "") for i, specs in enumerate(specs_per_row)]

    def test_explicit_beats_prefix(self):
        t = self.table(["docs/reviews/"], ["docs/reviews/*/baseline-record.md"])
        self.assertEqual(csa.match_row("docs/reviews/SRR/baseline-record.md", t), (2, []))
        self.assertEqual(csa.match_row("docs/reviews/SRR/minutes.md", t), (1, []))

    def test_longest_prefix_wins(self):
        t = self.table(["tools/"], ["tools/refs/"])
        self.assertEqual(csa.match_row("tools/refs/convert.py", t), (2, []))
        self.assertEqual(csa.match_row("tools/csa.py", t), (1, []))

    def test_star_matches_slash_and_classes(self):
        t = self.table(["docs/*schema.json"], ["docs/process/0[124-8]-*.md"], ["*.gitkeep"], ["hardware/kicad/"])
        self.assertEqual(csa.match_row("docs/templates/rfa-rid-log.schema.json", t)[0], 1)
        self.assertEqual(csa.match_row("docs/process/04-verification.md", t)[0], 2)
        self.assertEqual(csa.match_row("docs/process/03-software.md", t)[0], None)
        self.assertEqual(csa.match_row("hardware/kicad/.gitkeep", t)[0], 3)

    def test_ties_and_unmatched(self):
        t = self.table(["docs/a.md"], ["docs/*.md"], ["x/"], ["x/"])
        self.assertEqual(csa.match_row("docs/a.md", t), (1, [1, 2]))
        self.assertEqual(csa.match_row("x/y", t), (3, [3, 4]))
        self.assertEqual(csa.match_row("z/y", t), (None, []))


class FrontMatterTests(unittest.TestCase):
    def test_cr_and_record_fields(self):
        fm = csa.front_matter(build_repo.cr(7, "T", "Submitted", None, [2, 31], None))
        self.assertEqual((fm["id"], fm["status"], fm["affected_cis"], fm["disposition"], fm["date_opened"]),
                         ("CR-007", "Submitted", [2, 31], None, "2026-09-26"))
        rec = csa.front_matter(build_repo.record("INSP-009", "APPROVED", "a.md", ["a.md", "b.md"]))
        self.assertEqual(rec["id"], "INSP-009")
        self.assertEqual([p.split("@")[0] for p in rec["product_files"]], ["a.md", "b.md"])
        self.assertEqual(csa.front_matter("no front matter"), {})

    def test_block_list_and_directory_product(self):
        text = ("---\nid: INSP-016\nproduct: firmware/ (FW-B0 workspace), tools/sw_gate.sh, docs/a.md (delta)\n"
                "product_files:\n  - docs/b.md@1234\n  - \"docs/c.md@5678\"\nverdict: APPROVED\n---\n")
        fm = csa.front_matter(text)
        self.assertEqual(fm["product_files"], ["docs/b.md@1234", "docs/c.md@5678"])
        rec = {"named": {"tools/sw_gate.sh", "docs/a.md", "docs/b.md", "docs/c.md"}, "prefixes": ["firmware/"]}
        self.assertTrue(csa.names_any(rec, ["firmware/cwht-core/src/lib.rs"]))
        self.assertTrue(csa.names_any(rec, ["docs/c.md"]))
        self.assertFalse(csa.names_any(rec, ["docs/d.md", "firmwarex/a"]))


class FixtureRepoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.repo = os.path.join(cls.tmp.name, "repo")
        cls.shas = build_repo.build(cls.repo)
        cls.short = {k: v[:7] for k, v in cls.shas.items()}
        cls.label = {v[:7]: k for k, v in cls.shas.items()}
        cls.json_path = os.path.join(cls.tmp.name, "model.json")
        cls.r = run("--root", cls.repo, "--date", EXP["csa"]["date"], "--json", cls.json_path)
        with open(cls.json_path) as fh:
            cls.m = json.load(fh)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", "-C", self.repo, *args], capture_output=True, text=True, check=True).stdout.strip()

    def test_exit_and_header(self):
        self.assertEqual(self.r.returncode, 0, self.r.stderr)
        self.assertEqual(self.m["tracked_files"], EXP["csa"]["tracked_files"])
        self.assertEqual(self.m["since"], "baseline/srr")
        self.assertIn(f"| Tracked files | {EXP['csa']['tracked_files']} ", self.r.stdout)

    def test_rows(self):
        got = {r["num"]: r for r in self.m["rows"]}
        for num, level, files, records, applied, pending in EXP["csa"]["rows"]:
            with self.subTest(row=num):
                r = got[num]
                self.assertTrue(r["level"].startswith(level), r["level"])
                self.assertEqual((r["files"], r["records"], r["applied_crs"], r["pending_crs"]), (files, records, applied, pending))

    def test_last_commits(self):
        got = {r["num"]: r for r in self.m["rows"]}
        for num, label in EXP["csa"]["last_commit_label"].items():
            with self.subTest(row=num):
                self.assertTrue(got[int(num)]["last_commit"].startswith(f"`{self.short[label]}`"), got[int(num)]["last_commit"])

    def test_hashes_equal_git(self):
        got = {r["num"]: r for r in self.m["rows"]}
        for num, tree in EXP["csa"]["tree_rows"].items():
            self.assertIn(f"tree `{self.git('rev-parse', 'HEAD:' + tree)[:12]}`", got[int(num)]["hash"])
        self.assertIn(self.git("rev-parse", "HEAD:docs/process/00-charter.md")[:12], got[1]["hash"])
        self.assertIn(self.git("rev-parse", "HEAD:.gitignore")[:12], got[13]["hash"])
        self.assertIn(self.git("rev-parse", "HEAD:hardware/kicad/.gitkeep")[:12], got[13]["hash"])

    def test_unmatched_and_ties(self):
        self.assertEqual(self.m["unmatched"], EXP["csa"]["unmatched"])
        self.assertEqual(self.m["ties"], [])

    def test_baseline(self):
        (b,) = self.m["baselines"]
        self.assertEqual((b["name"], b["commit"]), (EXP["csa"]["baseline"]["name"], self.shas[EXP["csa"]["baseline"]["commit_label"]]))
        self.assertIn("| no | not checked (run with --remote) |", self.r.stdout)

    def test_cr_register(self):
        self.assertEqual([c["id"] for c in self.m["crs"]], ["CR-001", "CR-002", "CR-004"])
        self.assertEqual(self.m["missing_cr_numbers"], EXP["csa"]["missing_cr_numbers"])

    def test_change_log_editorial_and_lacking(self):
        self.assertEqual(len(self.m["commits"]), 15)
        ed = [self.label[c["short"]] for c in self.m["commits"] if c["editorial"]]
        self.assertEqual(ed, EXP["csa"]["editorial_labels"])
        self.assertEqual([self.label[s] for s in self.m["lacking_trailers"]], EXP["csa"]["lacking_trailer_labels"])
        self.assertIn("| Commits lacking mandatory trailers (REFS_MISSING or CR_TRAILER_MISSING) | 3: ", self.r.stdout)

    def test_metrics(self):
        self.assertRegex(self.r.stdout, r"\| Requirements volatility \(`MSR-02`\) \| 12\.5 % .* \| " + EXP["csa"]["msr02_state"] + r" \|")
        self.assertIn("| Open CRs and their age | 2: CR-002 (Submitted, 6 d), CR-004 (Draft, 6 d) |", self.r.stdout)

    def test_items_11_to_13(self):
        self.assertIn("| 1 | 2026-09-26 | 05 section 5.2 | CR-001 dispositioned before its impact review |", self.r.stdout)
        self.assertEqual([list(w) for w in self.m["waivers"]], EXP["csa"]["waivers"])
        tbrs = {p: c["by_close_by"] for _k, p, c in self.m["tbrs"]}
        for path, counts in EXP["csa"]["tbrs"].items():
            self.assertEqual(tbrs[path], counts, path)
        self.assertEqual([i["id"] for i in self.m["open_log_items"]], EXP["csa"]["open_log_items"])

    def test_release_and_audit_none(self):
        self.assertIn("## 7. Release register\n\nNone:", self.r.stdout)
        self.assertIn("## 8. Audit register\n\nNone:", self.r.stdout)

    def test_rev_and_since_options(self):
        r = run("--root", self.repo, "--rev", self.shas["c3"], "--since", self.shas["c1"], "--date", "2026-10-02",
                "--json", os.path.join(self.tmp.name, "m2.json"))
        self.assertEqual(r.returncode, 0, r.stderr)
        with open(os.path.join(self.tmp.name, "m2.json")) as fh:
            m2 = json.load(fh)
        self.assertEqual([self.label[c["short"]] for c in m2["commits"]], ["c2", "c3"])
        self.assertEqual(m2["tracked_files"], 22)

    def test_output_is_reproducible(self):
        a = run("--root", self.repo, "--date", "2026-10-02").stdout
        b = run("--root", self.repo, "--date", "2026-10-02").stdout
        self.assertEqual(a, b)


class CliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.repo = os.path.join(cls.tmp.name, "repo")
        build_repo.build(cls.repo)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_write_then_check_pass_and_fail(self):
        os.makedirs(os.path.join(self.repo, "docs", "process"), exist_ok=True)
        r = run("--root", self.repo, "--date", "2026-10-02", "--write")
        self.assertEqual(r.returncode, 0, r.stderr)
        path = os.path.join(self.repo, csa.CSA_PATH)
        self.assertEqual(run("--root", self.repo, "--date", "2026-10-02", "--check", path).returncode, 0)
        with open(path, "a") as fh:
            fh.write("hand edit\n")
        r = run("--root", self.repo, "--date", "2026-10-02", "--check", path)
        self.assertEqual(r.returncode, 1)
        self.assertIn("CHECK FAIL", r.stderr)
        os.remove(path)

    def test_output_path(self):
        out = os.path.join(self.tmp.name, "csa.md")
        self.assertEqual(run("--root", self.repo, "--date", "2026-10-02", "--output", out).returncode, 0)
        with open(out) as fh:
            self.assertTrue(fh.read().startswith("# cwht Configuration Status Accounting Report"))

    def test_strict_fails_on_unmatched(self):
        r = run("--root", self.repo, "--date", "2026-10-02", "--strict")
        self.assertEqual(r.returncode, 1)
        self.assertIn("STRICT FAIL: 1 file(s) in no row, 0 in two rows", r.stderr)

    def test_usage_and_git_errors_exit_2(self):
        cases = [
            ("--root", self.repo, "--date", "2 Oct"),
            ("--root", self.repo, "--rev", "no-such-rev"),
            ("--root", self.tmp.name, "--date", "2026-10-02"),                 # not a git repository
            ("--root", self.repo, "--write", "--output", "x"),                  # exclusive options
            ("--root", self.repo, "--check", os.path.join(self.tmp.name, "absent.md")),
            ("--bogus",),
        ]
        for args in cases:
            with self.subTest(args=args):
                self.assertEqual(run(*args).returncode, 2)

    def test_revision_without_table_exit_2(self):
        first = subprocess.run(["git", "-C", self.repo, "rev-list", "--max-parents=0", "HEAD"], capture_output=True, text=True).stdout.strip()
        with tempfile.TemporaryDirectory() as t:
            other = os.path.join(t, "r")
            os.makedirs(other)
            build_repo.git(other, "init", "-q")
            with open(os.path.join(other, "a.txt"), "w") as fh:
                fh.write("a\n")
            build_repo.git(other, "add", "-A")
            build_repo.git(other, "commit", "-q", "-m", "chore(x): no plan", date="2026-10-01T00:00:00-05:00")
            r = run("--root", other, "--date", "2026-10-02")
            self.assertEqual(r.returncode, 2)
            self.assertIn("not found", r.stderr)
        self.assertTrue(first)


class HandCsaTests(unittest.TestCase):
    """Repository content: the derivable values at 9fd0962 equal the hand CSA issue 1 (b790eaa)."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(FIXTURE, "hand-csa-9fd0962.json")) as fh:
            cls.hand = json.load(fh)
        cls.tmp = tempfile.TemporaryDirectory()
        path = os.path.join(cls.tmp.name, "m.json")
        cls.r = run("--root", ROOT, "--rev", cls.hand["rev"], "--since", cls.hand["since"], "--date", "2026-09-27", "--json", path)
        with open(path) as fh:
            cls.m = json.load(fh)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_tracked_files(self):
        self.assertEqual(self.r.returncode, 0, self.r.stderr)
        self.assertEqual(self.m["tracked_files"], self.hand["tracked_files"])

    def test_rows_counts_hashes_last_commits(self):
        got = {r["num"]: r for r in self.m["rows"]}
        for num, h in self.hand["rows"].items():
            r = got[int(num)]
            with self.subTest(row=num):
                self.assertEqual(r["files"], h["files"])
                if int(num) == 26:     # no pathspec: the hand CSA gives the rustos pin from the lock
                    continue
                tool_hashes = set(re.findall(r"`([0-9a-f]{12})`", r["hash"]))
                self.assertTrue(tool_hashes <= set(h["hashes"]), f"tool {sorted(tool_hashes)} hand {h['hashes']}")
                if h["last_commits"]:
                    self.assertIn(r["last_commit"].split("`")[1], h["last_commits"], f"{r['last_commit']} vs {h['last_commits']}")

    def test_unmatched(self):
        self.assertEqual(sorted(self.m["unmatched"]), self.hand["unmatched"])

    def test_change_log(self):
        got = [(c["short"], c["rows"], c["refs"]) for c in self.m["commits"]]
        self.assertEqual([g[0] for g in got], [c["short"] for c in self.hand["change_log"]])
        for (short, rows, refs), h in zip(got, self.hand["change_log"]):
            with self.subTest(commit=short):
                self.assertEqual(rows, h["rows"])
                text = h["refs_text"]
                if text.startswith(("**missing**", "none", "**not parsed**")):
                    self.assertEqual(refs, [])
                elif text == "RSK ids":
                    self.assertTrue(any(r.startswith("RSK-") for r in refs))
                else:
                    self.assertEqual(refs, [t.strip() for t in text.split(",")])

    def test_lacking_trailers(self):
        self.assertEqual(self.m["lacking_trailers"], self.hand["lacking_trailers"])


if __name__ == "__main__":
    unittest.main()
