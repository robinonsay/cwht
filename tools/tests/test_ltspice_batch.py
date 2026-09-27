"""Known-answer tests for tools/ltspice-batch.sh (TV-014; CM plan section 9.2; lock section 1.1 LTspice row).

Every case reads its expected value from tools/tests/fixtures/ltspice/known-answers.json ("wrapper"
block) and runs the wrapper on a temporary copy of the fixture directory, because LTspice writes
beside its deck.

The everyday suite never starts the real LTspice (so it never holds the wrapper lock for more than a
fraction of a second and never starts a Wine session of the bottle):
  UsageTests, HygieneTests, InstallAndVersionTests, LockTests, PreconditionTests, AsciiRawReaderTests
  stop at a check that precedes the launch, or test the ASCII raw reader on a stored sample;
  OutputCheckTests and WineSessionDoubleTests launch the test doubles of fake-support/bin (wine and
  wineserver) in place of the bundle's, with CWHT_LTSPICE_SUPPORT set, and need the bottle precondition
  (CaptureAnalytics=false in the bottle LTspice.ini, read only) because the wrapper checks it first.
Integration classes run the real LTspice only when CWHT_LTSPICE_INTEGRATION=1 is set (the TV-014
procedure sets it): LTspiceRunTests, WineSessionIntegrationTests and, with CWHT_LTSPICE_SLOW=1 as well,
TimeoutGuardTests (about 45 s). Every skip carries its reason; the TV-014 procedure counts a skip as
"not run", never as a pass.

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -v
    CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -v
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
INTEGRATION = os.environ.get("CWHT_LTSPICE_INTEGRATION") == "1"
NOT_INTEGRATION = ("real-LTspice integration case: set CWHT_LTSPICE_INTEGRATION=1 to run it (the TV-014 procedure "
                   "does; the everyday suite uses the test doubles only)")
BOTTLE = os.path.expanduser("~/Library/Application Support/LTspice/Bottles/ltspice")
LOCK_WAIT_MAX_S = 1800


def lockfile() -> str:
    d = subprocess.run(["getconf", "DARWIN_USER_TEMP_DIR"], capture_output=True, text=True).stdout.strip()
    return (d or tempfile.gettempdir() + "/") + "cwht-ltspice.lock"


def session_pids(prefix: str) -> list[int]:
    """PIDs of this user's processes in the Wine session of the prefix, by the wrapper's rule (step 5a).

    A process belongs to it when its current directory is inside the prefix (the Wine services run in
    C:\\windows) or is the prefix's wineserver directory /tmp/.wine-<uid>/server-<dev>-<inode>.
    """
    try:
        pre = os.path.realpath(prefix)
        st = os.stat(pre)
    except OSError:
        return []
    srv = os.path.join(os.path.realpath("/tmp"), f".wine-{os.getuid()}", f"server-{st.st_dev:x}-{st.st_ino:x}")
    out = subprocess.run(["lsof", "-n", "-w", "-u", str(os.getuid()), "-a", "-d", "cwd", "-F", "pn"],
                         capture_output=True, text=True).stdout
    pids, pid = [], None
    for line in out.splitlines():
        if line.startswith("p"):
            pid = int(line[1:])
        elif line.startswith("n") and pid is not None:
            n = line[1:]
            if (n + "/").startswith(pre + "/") or n == srv:
                pids.append(pid)
    return sorted(set(pids))


def readtext(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    # A zombie is not alive for this purpose (ps shows state Z).
    state = subprocess.run(["ps", "-o", "state=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return bool(state) and not state.startswith("Z")


class HeldLock:
    """Holds the wrapper lock (blocking wait, as a wrapper run would; never a skip)."""

    def __enter__(self) -> "HeldLock":
        self.f = open(lockfile(), "w")
        t0 = time.time()
        while True:
            try:
                fcntl.flock(self.f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.time() - t0 > LOCK_WAIT_MAX_S:
                    self.f.close()
                    raise AssertionError(f"the wrapper lock stayed held for more than {LOCK_WAIT_MAX_S} s")
                time.sleep(0.5)
        self.waited = time.time() - t0
        return self

    def __exit__(self, *exc: object) -> None:
        fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()


def read_ascii_raw(data: bytes) -> dict[str, list[float]]:
    """Traces of an LTspice ASCII raw file (written with -ascii), as {name: values}.

    Fails (AssertionError) when the file is not an ASCII raw file: a 'Binary:' data section, no
    'Variables:' or 'Values:' section, a point count other than 'No. Points:', a point index out of
    order, or a value that is not a decimal number. The header may be UTF-16LE (as in the binary raw
    file, research F8) or 8-bit text; both are accepted.
    """
    if data[:2] == b"\xff\xfe":
        text = data[2:].decode("utf-16-le")
    elif len(data) > 1 and data[1] == 0:
        text = data.decode("utf-16-le")
    else:
        text = data.decode("ascii")
    lines = text.replace("\r", "").split("\n")
    if any(line.startswith("Binary:") for line in lines):
        raise AssertionError("the raw file has a Binary: data section, so it is not an ASCII raw file")
    stripped = [line.strip() for line in lines]
    if "Variables:" not in stripped or "Values:" not in stripped:
        raise AssertionError("the raw file has no Variables: or Values: section")
    iv, ival = stripped.index("Variables:"), stripped.index("Values:")
    names = [line.split()[1] for line in lines[iv + 1:ival] if line.strip()]
    tokens = " ".join(lines[ival + 1:]).split()
    width = len(names) + 1
    if not names or len(tokens) % width:
        raise AssertionError(f"{len(tokens)} value tokens do not form points of {width} tokens")
    points = len(tokens) // width
    for line in lines[:iv]:
        if line.startswith("No. Points:") and int(line.split(":", 1)[1]) != points:
            raise AssertionError(f"header says {line.split(':', 1)[1].strip()} points, the file holds {points}")
    traces: dict[str, list[float]] = {n: [] for n in names}
    for p in range(points):
        row = tokens[p * width:(p + 1) * width]
        if int(row[0]) != p:
            raise AssertionError(f"point index {row[0]} where {p} was expected")
        for name, value in zip(names, row[1:]):
            traces[name].append(float(value))
    return traces


def value_at(xs: list[float], ys: list[float], x: float) -> float:
    """Linear interpolation of ys at x on the ascending axis xs (LTspice may store |t| with a sign flag)."""
    xs = [abs(v) for v in xs]
    for k in range(1, len(xs)):
        if xs[k - 1] <= x <= xs[k]:
            if xs[k] == xs[k - 1]:
                return ys[k]
            return ys[k - 1] + (ys[k] - ys[k - 1]) * (x - xs[k - 1]) / (xs[k] - xs[k - 1])
    raise AssertionError(f"{x} is outside the axis {xs[0]} to {xs[-1]}")


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
        e.pop("CWHT_LTSPICE_EXPECT_BUNDLE", None)
        e.pop("CWHT_LTSPICE_EXPECT_EXE_SHA256", None)
        for k in [k for k in e if k.startswith("CWHT_FAKE_")]:
            e.pop(k)
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

    @unittest.skipUnless(os.access(WINE, os.X_OK), "LTspice not installed")
    def test_bundle_build_other_than_lock(self) -> None:
        case = KA["seeded_bundle_build"]
        r = self.run_tool("-version", env=case["env"])
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn("LTspice bundle build is", r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)

    @unittest.skipUnless(os.access(WINE, os.X_OK), "LTspice not installed")
    def test_exe_sha256_other_than_lock(self) -> None:
        case = KA["seeded_exe_sha256"]
        r = self.run_tool("-version", env=case["env"])
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)
        self.assertIn("expected " + case["env"]["CWHT_LTSPICE_EXPECT_EXE_SHA256"], r.stderr)


class LockTests(WrapperCase):
    def test_busy_when_lock_held(self) -> None:
        # If another run holds the lock, wait for it (HeldLock) instead of skipping (TV-014 run 4).
        case = KA["seeded_busy"]
        with HeldLock():
            t0 = time.time()
            r = self.run_tool("-version", env=case["env"])
            waited = time.time() - t0
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


class AsciiRawReaderTests(unittest.TestCase):
    """The reader of the -ascii known answer, on a stored sample in the LTspice ASCII raw layout."""

    SAMPLE = ("Title: * sample\r\nPlotname: Transient Analysis\r\nFlags: real forward\r\n"
              "No. Variables: 3\r\nNo. Points: 3\r\nVariables:\r\n\t0\ttime\ttime\r\n"
              "\t1\tV(in)\tvoltage\r\n\t2\tV(out)\tvoltage\r\nValues:\r\n"
              "0\t\t0.000000000000000e+000\r\n\t1.0e+000\r\n\t0.0e+000\r\n"
              "1\t\t1.000000000000000e-003\r\n\t1.0e+000\r\n\t6.0e-001\r\n"
              "2\t\t-2.000000000000000e-003\r\n\t1.0e+000\r\n\t8.0e-001\r\n")

    def test_reads_text_and_utf16_forms(self) -> None:
        for data in (self.SAMPLE.encode("ascii"), b"\xff\xfe" + self.SAMPLE.encode("utf-16-le")):
            with self.subTest(utf16=data[:2] == b"\xff\xfe"):
                t = read_ascii_raw(data)
                self.assertEqual(list(t), ["time", "V(in)", "V(out)"])
                self.assertAlmostEqual(value_at(t["time"], t["V(out)"], 0.0015), 0.7, places=12)

    def test_rejects_binary_and_truncated_files(self) -> None:
        with self.assertRaises(AssertionError):
            read_ascii_raw(self.SAMPLE.replace("Values:", "Binary:").encode("ascii"))
        with self.assertRaises(AssertionError):
            read_ascii_raw(self.SAMPLE[:-len("\t8.0e-001\r\n")].encode("ascii"))


@unittest.skipUnless(READY, NOT_READY)
@unittest.skipUnless(INTEGRATION, NOT_INTEGRATION)
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

    def test_ascii_raw_known_answer(self) -> None:
        case = KA["ascii"]
        r = self.run_tool("-ascii", "-b", case["deck"])
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        with open(os.path.join(self.work, case["raw"]), "rb") as f:
            traces = read_ascii_raw(f.read())
        v = value_at(traces["time"], traces[case["trace"]], case["at_s"])
        self.assertLessEqual(abs(v - case["expected_v"]) / case["expected_v"], case["tolerance_fraction"], v)

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
class OutputCheckTests(WrapperCase):
    """Result checks that need an output LTspice does not produce on demand (a test double runs)."""

    def test_log_without_version_line(self) -> None:
        case = KA["seeded_no_version_line"]
        env = {k: os.path.join(self.work, v) for k, v in case["env"].items()}
        r = self.run_tool("-b", case["deck"], env=env)
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        self.assertIn(case["stderr_must_contain"], r.stderr)


@unittest.skipUnless(READY, NOT_READY)
@unittest.skipUnless(os.access(WINE, os.X_OK), "LTspice not installed")
class WineSessionDoubleTests(WrapperCase):
    """Lock descriptor and Wine session end, with the wine and wineserver doubles (never the real LTspice)."""

    def setUp(self) -> None:
        super().setUp()
        self.support = os.path.join(self.work, "fake-support")
        self.prefix = os.path.join(self.support, "prefix")
        self.extra: list[subprocess.Popen] = []

    def tearDown(self) -> None:
        pid_file = os.path.join(self.prefix, "service.pid")
        if os.path.exists(pid_file):
            try:
                os.kill(int(readtext(pid_file).strip()), 9)
            except (ProcessLookupError, ValueError):
                pass
        for p in self.extra:
            p.kill()
            p.wait()
        super().tearDown()

    def env(self, case: dict, **extra: str) -> dict:
        e = {k: (os.path.join(self.work, v) if k == "CWHT_LTSPICE_SUPPORT" else v) for k, v in case["env"].items()}
        e.update(extra)
        return e

    def service_pid(self) -> int:
        return int(readtext(os.path.join(self.prefix, "service.pid")).strip())

    def wineserver_calls(self) -> list[str]:
        path = os.path.join(self.support, "wineserver.log")
        return readtext(path).splitlines() if os.path.exists(path) else []

    def test_child_holds_no_lock_descriptor(self) -> None:
        # INSP-038 finding-20: fails on the line of blob 64e1c723 (the double and its service hold fd 10).
        case = KA["seeded_lock_descriptor"]
        fdlog = os.path.join(self.tmp, "fdlog.txt")
        r = self.run_tool("-b", case["deck"], env=self.env(case, CWHT_FAKE_WINE_FDLOG=fdlog))
        self.assertEqual(r.returncode, case["exit"], r.stderr)
        text = readtext(fdlog)
        head = dict(kv.split("=", 1) for kv in text.splitlines()[0].split())
        holders = text.splitlines()[1].split("=", 1)[1].split()
        self.assertIn(head["wrapper"], holders, "the wrapper does not hold the lock file open during the run")
        self.assertNotIn(head["double"], holders, "the wine child holds the lock file open")
        self.assertNotIn(head["service"], holders, "the Wine service stand-in holds the lock file open")
        self.assertIn("## lsof -p service", text)
        self.assertIn("/.stdout", text, "lsof did not list the double's descriptors")
        self.assertNotIn(case["lock_file_name"], text, "a descriptor on the lock file is open in the child")

    def _run_path(self, name: str) -> None:
        case = KA["wine_session"]
        path = case["paths"][name]
        t0 = time.time()
        r = self.run_tool(*path["args"], "-b", case["deck"], env=self.env(case, **path["env"]))
        self.assertEqual(r.returncode, path["exit"], r.stderr)
        self.assertIn(case["stderr_ended"], r.stderr)
        self.assertFalse(alive(self.service_pid()), "the Wine service stand-in outlived the run")
        self.assertEqual(session_pids(self.prefix), [])
        calls = self.wineserver_calls()
        self.assertEqual(len(calls), 1, calls)
        self.assertTrue(calls[0].startswith("wineserver -k WINEPREFIX="), calls)
        self.assertEqual(os.path.realpath(calls[0].split("WINEPREFIX=", 1)[1]), os.path.realpath(self.prefix))
        self.assertLess(time.time() - t0, 30)

    def test_session_ended_after_normal_run(self) -> None:
        self._run_path("normal")

    def test_session_ended_after_error_exit(self) -> None:
        self._run_path("error")

    def test_session_ended_after_timeout(self) -> None:
        self._run_path("timeout")

    def test_survivor_killed_when_wineserver_leaves_it(self) -> None:
        case = KA["wine_session"]
        r = self.run_tool("-b", case["deck"], env=self.env(case, CWHT_FAKE_WINESERVER_NOOP="1"))
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        self.assertIn(case["stderr_ended"], r.stderr)
        self.assertFalse(alive(self.service_pid()), "the SIGKILL fallback did not end the survivor")
        self.assertEqual(len(self.wineserver_calls()), 1)

    def test_session_running_before_is_left(self) -> None:
        case = KA["wine_session"]
        d = os.path.join(self.prefix, "drive_c")
        os.makedirs(d)
        before = subprocess.Popen(["/bin/sleep", "120"], cwd=d)
        self.extra.append(before)
        time.sleep(0.3)
        r = self.run_tool("-b", case["deck"], env=self.env(case))
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        self.assertIn(case["stderr_before"], r.stderr)
        self.assertIsNone(before.poll(), "a process of a session running before the launch was ended")
        self.assertEqual(self.wineserver_calls(), [])

    def test_foreign_ltspice_exe_leaves_session(self) -> None:
        case = KA["wine_session"]
        foreign = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)",
                                    "C:\\Program Files\\ADI\\LTspice\\LTspice.exe"])
        self.extra.append(foreign)
        time.sleep(0.3)
        r = self.run_tool("-b", case["deck"], env=self.env(case))
        self.assertEqual(r.returncode, EXIT["pass"], r.stderr)
        self.assertIn(case["stderr_foreign"], r.stderr)
        self.assertEqual(self.wineserver_calls(), [])
        self.assertTrue(alive(self.service_pid()), "the session was ended although another LTspice.exe is open")


def assert_no_bottle_session_after(test: unittest.TestCase, what: str) -> None:
    """Holding the wrapper lock (so no other run can start one), wait and require no bottle process."""
    with HeldLock():
        time.sleep(KA["wine_session"]["integration_wait_s"])
        left = session_pids(BOTTLE)
        detail = subprocess.run(["ps", "-o", "pid,ppid,etime,command", "-p", ",".join(map(str, left))],
                                capture_output=True, text=True).stdout if left else ""
    test.assertEqual(left, [], f"processes of the ltspice bottle remain {KA['wine_session']['integration_wait_s']} s "
                               f"after the {what} run:\n{detail}")


@unittest.skipUnless(READY, NOT_READY)
@unittest.skipUnless(INTEGRATION, NOT_INTEGRATION)
class WineSessionIntegrationTests(WrapperCase):
    """Real LTspice: no process of the bottle's Wine session outlives a run (TV-014 finding 5)."""

    def test_no_bottle_process_after_normal_and_error_runs(self) -> None:
        with HeldLock():
            self.assertEqual(session_pids(BOTTLE), [], "a Wine session of the bottle runs before the test")
        for what, deck, code in (("normal", "rc-step-tran.net", EXIT["pass"]),
                                 ("error", KA["seeded_deck_error"]["deck"], KA["seeded_deck_error"]["exit"])):
            with self.subTest(path=what):
                r = self.run_tool("-b", deck)
                self.assertEqual(r.returncode, code, r.stderr)
                self.assertIn(KA["wine_session"]["stderr_ended"], r.stderr)
                assert_no_bottle_session_after(self, what)


@unittest.skipUnless(READY, NOT_READY)
@unittest.skipUnless(INTEGRATION, NOT_INTEGRATION)
@unittest.skipUnless(os.environ.get("CWHT_LTSPICE_SLOW") == "1", "set CWHT_LTSPICE_SLOW=1 to run the time-out guard (about 45 s)")
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
            # LTspice.exe processes of any wrapper run directory, in either path form (the Windows form
            # Z:\\...\\cwht-lts.XXXXXX\\ is what LTspice.exe shows, TV-014 finding 3). Runs are serialized by
            # the lock, so while this test's run held it only this run could have started one.
            left = subprocess.run(["pgrep", "-f", "LTspice\\.exe.*cwht-lts\\.[A-Za-z0-9]{6}"],
                                  capture_output=True, text=True).stdout.split()
            self.assertEqual(left, [], "LTspice processes of a wrapper run survive")
            self.assertFalse(os.path.exists(os.path.join(self.work, "rc-hang-error.log")))
            self.assertIn(KA["wine_session"]["stderr_ended"], r.stderr)
            assert_no_bottle_session_after(self, "time-out")
        finally:
            sentinel.kill()
            sentinel.wait()


if __name__ == "__main__":
    unittest.main()
