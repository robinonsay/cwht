"""Known-answer test for git (tools/toolchain.lock.md section 1.1, git row; SWE-136).

git is a class B tool on cwht: blob and tree hashes appear in baseline records,
the configuration status accounting and the FCA and PCA items, and `git fsck
--full` results are recorded at each baseline (docs/process/05-configuration-
and-data-management.md). The lock's pass criterion, verbatim in substance:

    1. `git hash-object tools/tests/fixtures/git/hello.txt` equals the stored
       blob hash (also recomputed here as SHA-1 of "blob <size>\\0<content>");
    2. in a temporary repository created by the test, `git ls-tree HEAD --
       hello.txt` gives the same hash and `git fsck --full` exits 0;
    3. after one byte of that loose object is overwritten, `git fsck --full`
       exits non-zero naming the object.

Added here: the tree and commit hashes of the one-file commit, made with a fixed
identity and dates, equal their stored values (the commit object format is
content-addressed, so any change in how git serializes a tree or a commit shows
up), and `git --version` equals the observed version in the lock's git row, so a
version change cannot pass silently (the lock's change rule then applies).

The test isolates git from the user's configuration (GIT_CONFIG_GLOBAL=/dev/null,
GIT_CONFIG_NOSYSTEM=1, a temporary HOME), so signing or hook settings cannot
change the result. It does not skip when git is absent: a missing git fails.

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests -p 'test_git_known_answer.py'
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
REPO_ROOT = TOOLS.parent
FIXTURE = TOOLS / "tests" / "fixtures" / "git"
LOCK = TOOLS / "toolchain.lock.md"
ANSWERS = json.loads((FIXTURE / "known-answers.json").read_text(encoding="utf-8"))
LOCK_GIT_ROW = re.compile(r"^\|\s*git\s*\|\s*`git --version`\s*\|\s*`([^`]+)`", re.MULTILINE)


def isolated_env(home: Path) -> dict[str, str]:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    commit = ANSWERS["commit"]
    env.update(
        HOME=str(home),
        GIT_CONFIG_GLOBAL=os.devnull,
        GIT_CONFIG_NOSYSTEM="1",
        GIT_AUTHOR_NAME=commit["name"],
        GIT_AUTHOR_EMAIL=commit["email"],
        GIT_AUTHOR_DATE=commit["date"],
        GIT_COMMITTER_NAME=commit["name"],
        GIT_COMMITTER_EMAIL=commit["email"],
        GIT_COMMITTER_DATE=commit["date"],
    )
    return env


def git(args: list[str], cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=cwd, env=env, capture_output=True, text=True, check=False)


class GitKnownAnswerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        base = Path(cls.tmp.name)
        cls.home = base / "home"
        cls.home.mkdir()
        cls.env = isolated_env(cls.home)
        cls.repo = base / "repo"
        cls.repo.mkdir()
        shutil.copy(FIXTURE / ANSWERS["file"], cls.repo / ANSWERS["file"])
        for args in (["init", "-q", "-b", "main", "."], ["add", ANSWERS["file"]], ["commit", "-q", "--no-verify", "-m", ANSWERS["commit"]["message"]]):
            result = git(args, cls.repo, cls.env)
            if result.returncode != 0:
                raise AssertionError(f"git {' '.join(args)} failed: {result.stdout}{result.stderr}")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_stored_blob_hash_is_the_sha1_of_the_blob_object(self) -> None:
        content = (FIXTURE / ANSWERS["file"]).read_bytes()
        self.assertEqual(ANSWERS["blob_sha1"], hashlib.sha1(b"blob %d\0" % len(content) + content).hexdigest())

    def test_hash_object_on_the_fixture_equals_the_stored_hash(self) -> None:
        result = git(["hash-object", "tools/tests/fixtures/git/hello.txt"], REPO_ROOT, self.env)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(ANSWERS["blob_sha1"], result.stdout.strip())

    def test_ls_tree_names_the_same_blob(self) -> None:
        result = git(["ls-tree", "HEAD", "--", ANSWERS["file"]], self.repo, self.env)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(f"100644 blob {ANSWERS['blob_sha1']}\t{ANSWERS['file']}", result.stdout.strip())

    def test_tree_and_commit_hashes(self) -> None:
        result = git(["rev-parse", "HEAD^{tree}", "HEAD"], self.repo, self.env)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual([ANSWERS["tree_sha1"], ANSWERS["commit_sha1"]], result.stdout.split())

    def test_fsck_passes_then_fails_on_one_corrupted_byte(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            shutil.copytree(self.repo, repo)
            clean = git(["fsck", "--full"], repo, self.env)
            self.assertEqual(0, clean.returncode, clean.stdout + clean.stderr)
            blob = ANSWERS["blob_sha1"]
            loose = repo / ".git" / "objects" / blob[:2] / blob[2:]
            self.assertTrue(loose.is_file(), "the blob is a loose object in a fresh repository")
            loose.chmod(0o644)
            data = bytearray(loose.read_bytes())
            data[len(data) // 2] ^= 0xFF  # one byte of the zlib stream
            loose.write_bytes(bytes(data))
            broken = git(["fsck", "--full"], repo, self.env)
        self.assertNotEqual(0, broken.returncode, broken.stdout + broken.stderr)
        self.assertIn(blob, broken.stdout + broken.stderr)

    def test_version_equals_the_lock(self) -> None:
        match = LOCK_GIT_ROW.search(LOCK.read_text(encoding="utf-8"))
        self.assertIsNotNone(match, "tools/toolchain.lock.md has no git row with `git --version`")
        result = git(["--version"], REPO_ROOT, self.env)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(match.group(1), result.stdout.strip(), "git version differs from the lock; the lock change rule applies")


if __name__ == "__main__":
    unittest.main()
