"""Known-answer tests for tools/unsafe_audit.py (SWE-136 tool validation; 07 CS-05 to CS-07, MSR-11).

Fixture tools/tests/fixtures/unsafe_audit/:
  audited/src/lib.rs   nine unsafe sites (hand-counted lines below) and five decoys that are not
                       sites (doc comment, nested block comment, string, raw string, char literals,
                       a lifetime, an `unsafe extern "C" fn()` pointer type on line 56); one site (line 36, bad_block) has no SAFETY comment (seeded CS-06 fault)
  forbidden/src/main.rs one site in a crate that forbids unsafe (seeded CS-05 fault)
  clean/src/lib.rs     one site with its SAFETY comment
The expected sites were written by reading the fixture, not by running the tool.

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_unsafe_audit.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import unsafe_audit as ua  # noqa: E402

FIXTURE = TOOLS / "tests" / "fixtures" / "unsafe_audit"
TOOL = TOOLS / "unsafe_audit.py"

EXPECTED_AUDITED = [
    (19, "block", "good_block", "SAFETY: p points at a readable 32-bit register (fixture datasheet section 1.1) and is aligned, so a volatile read is sound."),
    (26, "fn", "raw_write", "SAFETY: callers pass an aligned, writable register address (fixture datasheet section 1.2); the function is the only writer."),
    (28, "block", "raw_write", "SAFETY: the caller upholds the contract stated above raw_write."),
    (32, "impl", "impl Send for Handle<'_>", "SAFETY: Handle holds only a shared reference to an immutable register value."),
    (36, "block", "bad_block", ""),
    (40, "attr", "fixture_entry", "SAFETY: the symbol name is unique in the fixture image."),
    (44, "extern", "extern block", "SAFETY: the declared C function has no preconditions."),
    (50, "block", "let_block", "SAFETY: as in good_block."),
    (55, "attr", "TABLE", "SAFETY: the section name is reserved for this table in the fixture link script."),
]


def workspace(tmp: str) -> Path:
    """A repository-shaped copy: <tmp>/repo is the root, fixture crates below it."""
    root = Path(tmp) / "repo"
    shutil.copytree(FIXTURE, root / "fx")
    return root


def run_cli(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TOOL), "--root", str(root), *args], capture_output=True, text=True, check=False)


class LexerTests(unittest.TestCase):
    def test_mask_keeps_offsets_and_hides_comments_and_literals(self) -> None:
        text = 'let s = "unsafe"; // unsafe note\nlet c = \'"\'; /* unsafe /* x */ */ unsafe {}\n'
        code, comments = ua.mask_rust(text)
        self.assertEqual(len(text), len(code))
        self.assertEqual(text.count("\n"), code.count("\n"))
        self.assertEqual(1, len(ua.UNSAFE.findall(code)), code)
        self.assertEqual({0: ["unsafe note"]}, comments)

    def test_escaped_quote_char_and_raw_string(self) -> None:
        code, _ = ua.mask_rust("let a = '\\''; let b = r##\"unsafe \"# still\"##; unsafe fn f() {}")
        self.assertEqual(["unsafe"], ua.UNSAFE.findall(code))
        self.assertEqual("fn", ua.classify(code, code.index("unsafe") + len("unsafe")))

    def test_lifetime_is_not_a_char_literal(self) -> None:
        code, _ = ua.mask_rust("fn f<'a>(x: &'a u8) { unsafe { } }")
        self.assertEqual(1, len(ua.UNSAFE.findall(code)))


class ScanKnownAnswerTests(unittest.TestCase):
    def test_audited_sites(self) -> None:
        sites = ua.scan_file(FIXTURE / "audited/src/lib.rs", "lib.rs", False)
        self.assertEqual(EXPECTED_AUDITED, [(s.line, s.kind, s.item, s.safety) for s in sites])

    def test_forbidden_site(self) -> None:
        sites = ua.scan_file(FIXTURE / "forbidden/src/main.rs", "main.rs", True)
        self.assertEqual([(6, "block", "main", True)], [(s.line, s.kind, s.item, s.forbidden) for s in sites])

    def test_target_directories_are_not_scanned(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = workspace(tmp)
            generated = root / "fx/clean/target/debug/generated.rs"
            generated.parent.mkdir(parents=True)
            generated.write_text("pub fn g() { unsafe { } }\n", encoding="utf-8")
            sites = ua.scan(root, [root / "fx/clean"], [])
        self.assertEqual([("repo/fx/clean/src/lib.rs", 5)], [(s.file, s.line) for s in sites])

    def test_counts(self) -> None:
        sites = ua.scan_file(FIXTURE / "audited/src/lib.rs", "lib.rs", False) + ua.scan_file(FIXTURE / "forbidden/src/main.rs", "main.rs", True)
        c = ua.counts(sites, None)
        self.assertEqual((4, 1, 1, 2, 1, 9, 1, 1, 9), (c["block"], c["fn"], c["impl"], c["attr"], c["extern"], c["total"], c["without_safety"], c["forbidden_sites"], c["unsigned"]))


class CheckTests(unittest.TestCase):
    def test_check_without_audit_list_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = workspace(tmp)
            result = run_cli(root, "--check", "--audited", "fx/clean", "--forbidden", "fx/forbidden")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn("unsafe-audit.md does not exist", result.stdout)
        self.assertIn("in a crate that forbids unsafe code (CS-05)", result.stdout)

    def test_write_then_check_reports_exactly_the_seeded_faults(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = workspace(tmp)
            (root / "firmware").mkdir()
            args = ("--audited", "fx/audited", "--forbidden", "fx/forbidden")
            written = run_cli(root, "--write", *args)
            self.assertEqual(1, written.returncode, "the list is written and the seeded faults still fail")
            self.assertTrue((root / "firmware/unsafe-audit.md").is_file())
            result = run_cli(root, "--check", *args)
        fails = [line for line in result.stdout.splitlines() if line.startswith("FAIL ")]
        self.assertEqual(
            [
                "FAIL repo/fx/audited/src/lib.rs:36 unsafe block (bad_block) without a // SAFETY: comment immediately above (CS-06)",
                "FAIL repo/fx/forbidden/src/main.rs:6 unsafe block in a crate that forbids unsafe code (CS-05)",
            ],
            sorted(fails),
        )
        self.assertIn("NOTE 9 unsigned entries in repo/firmware/unsafe-audit.md", result.stdout)
        self.assertIn("MSR-11 unsafe sites: block 4, fn 1, impl 1, extern 1, attr 2; total 9; without SAFETY 1; unsigned 9; in forbidden crates 1", result.stdout)

    def test_clean_signed_list_passes_and_unsigned_fails_from_cdr(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = workspace(tmp)
            (root / "firmware").mkdir()
            args = ("--audited", "fx/clean", "--forbidden", str(root / "firmware"))
            self.assertEqual(0, run_cli(root, "--write", *args).returncode)
            self.assertEqual(0, run_cli(root, "--check", *args).returncode, "unsigned is a note before CDR")
            self.assertEqual(0, run_cli(root, "--check", "--gate", "PDR", *args).returncode)
            cdr = run_cli(root, "--check", "--gate", "CDR", *args)
            self.assertEqual(1, cdr.returncode)
            self.assertIn("1 unsigned entry", cdr.stdout)
            audit = root / "firmware/unsafe-audit.md"
            audit.write_text(audit.read_text(encoding="utf-8").replace("|  |  |\n", "| INSP-042 | 2026-09-26 |\n"), encoding="utf-8")
            self.assertEqual(0, run_cli(root, "--check", "--gate", "SAR", *args).returncode)
            audit.write_text(audit.read_text(encoding="utf-8").replace("INSP-042", "INSP-42"), encoding="utf-8")
            bad = run_cli(root, "--check", *args)
        self.assertEqual(1, bad.returncode)
        self.assertIn("Reviewer 'INSP-42' is not INSP-NNN", bad.stdout)

    def test_stale_list_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = workspace(tmp)
            (root / "firmware").mkdir()
            args = ("--audited", "fx/clean", "--forbidden", str(root / "firmware"))
            run_cli(root, "--write", *args)
            src = root / "fx/clean/src/lib.rs"
            src.write_text("\n" + src.read_text(encoding="utf-8"), encoding="utf-8")
            result = run_cli(root, "--check", *args)
        self.assertEqual(1, result.returncode)
        self.assertIn("lacks the site repo/fx/clean/src/lib.rs:6 block (read)", result.stdout)
        self.assertIn("lists repo/fx/clean/src/lib.rs:5 block (read)", result.stdout)


class SignatureTests(unittest.TestCase):
    def test_signature_follows_a_moved_site_and_is_superseded_by_a_changed_argument(self) -> None:
        site = ua.Site("a.rs", 5, "block", "read", "SAFETY: x.")
        old = ua.AuditList([ua.Entry("a.rs", 4, "block", "read", "SAFETY: x.", "INSP-001", "2026-09-20")])
        entries, superseded = ua.regenerate([site], old, "2026-09-26")
        self.assertEqual(("INSP-001", "2026-09-20", 5), (entries[0].reviewer, entries[0].date, entries[0].line))
        self.assertEqual([], superseded)
        changed = ua.Site("a.rs", 5, "block", "read", "SAFETY: y.")
        entries, superseded = ua.regenerate([changed], old, "2026-09-26")
        self.assertEqual(("", ""), (entries[0].reviewer, entries[0].date))
        self.assertEqual([["a.rs", "block", "read", "SAFETY: x.", "INSP-001", "2026-09-20", "2026-09-26"]], superseded)
        again, kept = ua.regenerate([changed], ua.AuditList(entries, superseded), "2026-09-27")
        self.assertEqual(superseded, kept, "superseded signatures are never removed")

    def test_render_parse_round_trip_with_pipes(self) -> None:
        entries = [ua.Entry("a.rs", 3, "impl", "impl Tr for S", "SAFETY: a | b \\ c.", "INSP-002", "2026-09-26")]
        superseded = [["a.rs", "block", "f", "SAFETY: old | text.", "INSP-001", "2026-09-01", "2026-09-26"]]
        parsed = ua.parse_audit(ua.render_audit(entries, superseded))
        self.assertEqual(entries, parsed.entries)
        self.assertEqual(superseded, parsed.superseded)


class UsageTests(unittest.TestCase):
    def test_usage_errors_exit_two(self) -> None:
        self.assertEqual(2, run_cli(FIXTURE, "--check", "--gate", "QDR").returncode)
        self.assertEqual(2, run_cli(FIXTURE, "--check", "--audited", "no-such-dir").returncode)
        self.assertEqual(2, run_cli(FIXTURE).returncode, "a mode is required")


if __name__ == "__main__":
    unittest.main()
