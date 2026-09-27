"""Known-answer tests for tools/ltspice-batch.sh (TV-014; CM plan section 9.2; lock section 1.1 LTspice row).

Every case reads its expected value from tools/tests/fixtures/ltspice/known-answers.json ("wrapper"
block) and runs the wrapper on a temporary copy of the fixture directory, because LTspice writes
beside its deck.

Classes that never start LTspice (they stop at a check that precedes the run):
  UsageTests, HygieneTests, InstallAndVersionTests, LockTests, PreconditionTests.
Classes that run LTspice: LTspiceRunTests. They are skipped, with the reason, when the bottle
precondition (CaptureAnalytics=false in the bottle LTspice.ini) is not met; the TV-014 procedure
counts a skip as "not run", never as a pass.
TimeoutGuardTests (about 20 s) runs only with CWHT_LTSPICE_SLOW=1 and the bottle precondition met.

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -v
    CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -v
"""
from __future__ import annotations

import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "ltspice-batch.sh")
FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "ltspice")
KA = json.load(open(os.path.join(FIXTURE, "known-answers.json")))["wrapper"]
EXIT = KA["exit_codes"]
INI = os.path.expanduser(
    "~/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini")
WINE = "/Applications/LTspice.app/Contents/SharedSupport/ltspice/bin/wine"


def bottle_ready() -> bool:
    """True when LTspice is installed and the bottle ini carries the telemetry opt-out (read only)."""
    if not os.access(WINE, os.X_OK) or not os.path.isfile(INI):
        return False
    try:
        text = open(INI, "rb").read().decode("utf-16-le", errors="replace")
    except OSError:
        return False
    return any(line.strip("﻿\r") == "CaptureAnalytics=false" for line in text.split("\n"))


READY = bottle_ready()
NOT_READY = ("bottle precondition not met (LTspice absent or CaptureAnalytics=false missing from the bottle "
             "LTspice.ini); owner action, ADR-018")


def lockfile() -> str:
    d = subprocess.run(["getconf", "DARWIN_USER_TEMP_DIR"], capture_output=True, text=True).stdout.strip()
    return (d or tempfile.gettempdir() + "/") + "cwht-ltspice.lock"


def meas(log_text: str, name: str) -> float:
    """Value of a .meas line: 'name: ... AT <x>' gives x; 'name: expr=<v> at <t>' gives v."""
    for line in log_text.splitlines():
        if not line.lower().startswith(name.lower() + ":"):
            continue
        m = re.search(r"=\s*([-+0-9.eE]+)\s+at\s", line)
        if m and " AT " not in line:
            return float(m.group(1))
        m = re.search(r"\bAT\s+([-+0-9.eE]+)", line)
        if m:
            return float(m.group(1))
    raise AssertionError(f"measurement {name} not found in log")


class WrapperCase(unittest.TestCase):
    """Runs the wrapper in a temporary copy of the fixture directory."""

    def setUp(self) -> None:
        self.tmp = tempfile.mkdtemp(prefix="kat-lts.")
        self.work = os.path.join(self.tmp, "fx")
        shutil.copytree(FIXTURE, self.work)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_tool(self, *args: str, env: dict | None = None, timeout: int = 180) -> subprocess.CompletedProcess:
        e = dict(os.environ)
        e.pop("CWHT_LTSPICE_INI_CHECK", None)
        e.pop("CWHT_LTSPICE_VERSION", None)
        e.pop("CWHT_LTSPICE_SUPPORT", None)
        e.update(env or {})
        return subprocess.run(["/bin/bash", TOOL, *args], cwd=self.work, capture_output=True, text=True,
                              env=e, timeout=timeout)

    def read(self, name: str) -> str:
        with open(os.path.join(self.work, name), encoding="utf-8", errors="replace") as f:
            return f.read()


class UsageTests(WrapperCase):
    def test_no_arguments(self) -> None:
        self.assertEqual(self.run_tool().returncode, EXIT["usage_or_hygiene"])

    def test_mode_without_deck(self) -> None:
        self.assertEqual(self.run_tool("-b").returncode, EXIT["usage_or_hygiene"])

    def test_unknown_argument(self) -> None:
        r = self.run_tool("-run", "rc-lowpass.asc")
        self.assertEqual(r.returncode, EXIT["usage_or_hygiene"])
        self.assertIn("unknown argument", r.stderr)

    def test_bad_timeout(self) -> None:
        for t in ("x", "0", ""):
            with self.subTest(t=t):
                self.assertEqual(self.run_tool("-t", t, "-version").returncode, EXIT["usage_or_hygiene"])

    def test_two_modes(self) -> None:
        self.assertEqual(self.run_tool("-version", "-b", "rc-step-tran.net").returncode, EXIT["usage_or_hygiene"])

    def test_ascii_with_netlist_mode(self) -> None:
        self.assertEqual(self.run_tool("-ascii", "-netlist", "rc-lowpass.asc").returncode, EXIT["usage_or_hygiene"])


class HygieneTests(WrapperCase):
    def test_missing_deck(self) -> None:
        r = self.run_tool("-b", "absent.net")
        self.assertEqual(r.returncode, EXIT["usage_or_hygiene"])
        self.assertIn("deck not found", r.stderr)

    def test_wrong_extension(self) -> None:
        r = self.run_tool("-b", "known-answers.json")
        self.assertEqual(r.returncode, EXIT["usage_or_hygiene"])

    def test_netlist_mode_needs_schematic(self) -> None:
        r = self.run_tool("-netlist", "rc-step-tran.net")
        self.assertEqual(r.returncode, EXIT["usage_or_hygiene"])

    def test_include_escape_refused(self) -> None:
        case = KA["seeded_include_escape"]
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.work, "rc-include-escape.log")))

    def test_long_path_refused(self) -> None:
        case = KA["seeded_long_path"]
        name = "a" * case["deck_name_length"] + ".net"
        shutil.copy(os.path.join(self.work, "rc-step-tran.net"), os.path.join(self.work, name))
        r = self.run_tool("-b", name)
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)


class InstallAndVersionTests(WrapperCase):
    def test_not_installed(self) -> None:
        case = KA["seeded_not_installed"]
        r = self.run_tool("-version", env=case["env"])
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)

    @unittest.skipUnless(os.access(WINE, os.X_OK), "LTspice not installed")
    def test_version_other_than_lock(self) -> None:
        case = KA["seeded_version"]
        r = self.run_tool("-version", env=case["env"])
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn("is not the locked version", r.stderr)


class LockTests(WrapperCase):
    def test_busy_when_lock_held(self) -> None:
        case = KA["seeded_busy"]
        with open(lockfile(), "w") as f:
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                self.skipTest("another LTspice run holds the lock now")
            try:
                t0 = time.time()
                r = self.run_tool("-version", env=case["env"])
                waited = time.time() - t0
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn("busy", r.stderr)
        self.assertGreaterEqual(waited, 1.5)


@unittest.skipUnless(os.access(WINE, os.X_OK), "LTspice not installed")
class PreconditionTests(WrapperCase):
    def _expect_precondition_failure(self, ini: str) -> None:
        path = os.path.join(self.work, ini)
        r = self.run_tool("-version", env={"CWHT_LTSPICE_INI_CHECK": path})
        self.assertEqual(r.returncode, EXIT["precondition"], r.stderr)
        if READY:
            self.assertIn("CWHT_LTSPICE_INI_CHECK file " + path, r.stderr)
        else:
            self.assertIn("not found in the bottle LTspice.ini", r.stderr)

    def test_ini_without_key(self) -> None:
        self._expect_precondition_failure(KA["seeded_ini"]["without_key"])

    def test_ascii_appended_key_not_accepted(self) -> None:
        self._expect_precondition_failure(KA["seeded_ini"]["ascii_appended"])

    def test_missing_extra_ini(self) -> None:
        self._expect_precondition_failure("no-such.ini")

    @unittest.skipIf(READY, "the bottle ini carries the key; this case records the bottle-failure message only")
    def test_bottle_without_key(self) -> None:
        r = self.run_tool("-version")
        self.assertEqual(r.returncode, EXIT["precondition"], r.stderr)
        self.assertIn("never append", r.stderr)


@unittest.skipUnless(READY, NOT_READY)
class LTspiceRunTests(WrapperCase):
    def test_version(self) -> None:
        r = self.run_tool("-version")
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        self.assertEqual(r.stdout.strip(), KA["locked_version"])

    def test_extra_ini_with_key_passes(self) -> None:
        r = self.run_tool("-version", env={"CWHT_LTSPICE_INI_CHECK": os.path.join(self.work, KA["seeded_ini"]["with_key"])})
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)

    def test_netlist(self) -> None:
        r = self.run_tool("-netlist", "rc-lowpass.asc")
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        net = self.read("rc-lowpass.net")
        ref = json.load(open(os.path.join(FIXTURE, "known-answers.json")))["netlist"]
        for s in ref["must_contain"]:
            self.assertIn(s, net)
        for s in ref["must_not_contain"]:
            self.assertNotIn(s, net)

    def test_ac_known_answer(self) -> None:
        case = KA["ac"]
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        log = self.read("rc-lowpass.log")
        self.assertEqual(log.splitlines()[0].strip(), KA["log_first_line"])
        f = meas(log, case["meas"])
        self.assertLessEqual(abs(f - case["expected_hz"]) / case["expected_hz"], case["tolerance_fraction"], f)
        self.assertIn("sha256=", r.stderr)
        for out in ("rc-lowpass.raw", "rc-lowpass.net"):
            self.assertTrue(os.path.exists(os.path.join(self.work, out)), out)

    def test_transient_known_answer(self) -> None:
        case = KA["transient"]
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        log = self.read("rc-step-tran.log")
        v = meas(log, case["vtau"]["meas"])
        t = meas(log, case["thalf"]["meas"])
        self.assertLessEqual(abs(v - case["vtau"]["expected_v"]) / case["vtau"]["expected_v"],
                             case["vtau"]["tolerance_fraction"], v)
        self.assertLessEqual(abs(t - case["thalf"]["expected_s"]) / case["thalf"]["expected_s"],
                             case["thalf"]["tolerance_fraction"], t)

    def test_relative_include_is_copied(self) -> None:
        case = KA["include"]
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        f = meas(self.read("rc-include.log"), case["meas"])
        self.assertLessEqual(abs(f - case["expected_hz"]) / case["expected_hz"], case["tolerance_fraction"], f)

    def test_seeded_deck_error(self) -> None:
        case = KA["seeded_deck_error"]
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)

    def test_seeded_floating_net(self) -> None:
        case = KA["seeded_floating_net"]
        r = self.run_tool("-netlist", case["deck"])
        self.assertEqual(r.returncode, case["netlist_exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, case["simulate_exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)

    def test_output_directory(self) -> None:
        out = os.path.join(self.tmp, "out")
        r = self.run_tool("-o", out, "-b", "rc-step-tran.net")
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        self.assertTrue(os.path.exists(os.path.join(out, "rc-step-tran.raw")))
        self.assertFalse(os.path.exists(os.path.join(self.work, "rc-step-tran.raw")))

    def test_stale_outputs_removed(self) -> None:
        case = KA["stale_outputs"]
        for name in case["planted"]:
            with open(os.path.join(self.work, name), "w") as f:
                f.write("planted by the test\n")
        r = self.run_tool("-b", case["deck"])
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        for name in case["removed"]:
            self.assertFalse(os.path.exists(os.path.join(self.work, name)), name)
        for name in case["kept"]:
            self.assertTrue(os.path.exists(os.path.join(self.work, name)), name)


@unittest.skipUnless(READY, NOT_READY)
@unittest.skipUnless(os.environ.get("CWHT_LTSPICE_SLOW") == "1", "set CWHT_LTSPICE_SLOW=1 to run the time-out guard (about 20 s)")
class TimeoutGuardTests(WrapperCase):
    def test_hang_is_killed_and_only_this_run(self) -> None:
        case = KA["timeout_guard"]
        sentinel_dir = os.path.join(tempfile.gettempdir(), "cwht-lts.SENTINEL")
        sentinel = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)",
                                     os.path.join(sentinel_dir, case["deck"])])
        try:
            t0 = time.time()
            r = self.run_tool("-t", str(case["timeout_s"]), "-b", case["deck"], timeout=case["timeout_s"] + 60)
            elapsed = time.time() - t0
            self.assertEqual(r.returncode, case["exit"], r.stderr)
            self.assertIn(case["stderr_must_contain"], r.stderr)
            self.assertGreaterEqual(elapsed, case["timeout_s"])
            self.assertLess(elapsed, case["timeout_s"] + 15)
            self.assertIsNone(sentinel.poll(), "the sentinel process was killed")
            # Processes of any wrapper run directory (runs are serialized by the lock, so while this
            # test's run held it, only this run could have started LTspice through the wrapper).
            left = subprocess.run(["pgrep", "-f", "LTspice\\.exe.*cwht-lts\\.[A-Za-z0-9]{6}/"],
                                  capture_output=True, text=True).stdout.split()
            self.assertEqual(left, [], "LTspice processes of a wrapper run survive")
            self.assertFalse(os.path.exists(os.path.join(self.work, "rc-hang-error.log")))
        finally:
            sentinel.kill()
            sentinel.wait()


if __name__ == "__main__":
    unittest.main()
