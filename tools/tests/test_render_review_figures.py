"""Known-answer tests for tools/render_review_figures.py (SWE-136 tool validation).

The fixture tools/tests/fixtures/review_figures/ is a miniature repository with an
SRR package (entrance section 4, requirements section 8 with the functional-group
table, success section 20), five SYS requirements (one retired, two KDR, one open
TBR), two hazards, four risks (one closed, one Red only by the safety override),
three TPMs (one Red by the status rule, one with an SRR history entry, one not
reported) and a ConOps with one nominal and one off-nominal scenario. FIXTURE_SET
below is the figure set for that fixture. The tests check every value the figures
draw against hand-computed answers, every cross-check that stops a run, the exit
statuses, that a failed check writes nothing, and the pixel size of every render.

The RepositoryTests class checks repository content, not the tool: the SRR figure
set run with --check on the repository completes with exit 0 or 1 and no
traceback (05 section 9.2 keeps such checks out of the accreditation run).

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import dataclasses
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import render_review_figures as rrf  # noqa: E402

FIXTURE = TOOLS / "tests" / "fixtures" / "review_figures"
TOOL = TOOLS / "render_review_figures.py"

FIXTURE_SET = rrf.FigureSet(
    review="SRR",
    figures=("entrance", "success", "requirements", "kdr", "hazards", "risk", "tpm", "conops", "concept"),
    entrance_labels={"S1": "Agenda agreed", "S4": "Traceability passes", "1": "Stakeholders", "2": "Goals"},
    entrance_overrides={"2": ("Partially met", "fixture re-rating")},
    tool_run_rows=frozenset({"S4"}),
    entrance_notes={"Met": "dagger: fixture note"},
    success_labels={"4.4-1": "L1 responds to NGOs", "4.4-4": "Interfaces identified", "C1": "Gate criteria"},
    success_overrides={"4.4-4": ("Not met", "no lien may touch interfaces"), "C1": ("Met", "already Met")},
    success_footer=("Fixture footer line 1.", "Fixture footer line 2."),
    group_labels={"Transmitter": "Transmitter", "Receiver": "Receiver"},
    kdr_text=(("Transmitter", (("001", "Carrier 144.001 to 147.999 MHz"),)), ("Receiver", (("004", "MDS at most -140 dBm"),))),
    kdr_columns=((0,), (1,)),
    tpm_rows=(("001", "Mass margin", "no estimate at SRR", "status rule"), ("002", "PA efficiency", "58 % (target 60 %)", ""), ("003", "RX MDS", "no estimate", "")),
    status_rule_red=frozenset({"001"}),
    tpm_footer="Fixture TPM footer.",
    nominal=(("001", "First power-on"),),
    off_nominal=(("002", "Stuck key"),),
    concept=rrf.srr_concept,
)

SIZES = {
    "entrance-checklist.png": (1760, 850),
    "success-criteria.png": (1760, 790),
    "requirements-by-group.png": (1760, 830),
    "kdr-map.png": (1760, 720),
    "hazard-matrix.png": (1030, 740),
    "risk-matrix.png": (1760, 830),
    "tpm-status.png": (1760, 780),
    "conops-modes-scenarios.png": (1760, 830),
    "concept-block-diagram.png": (1760, 860),
}


def context(root: Path = FIXTURE, spec: rrf.FigureSet = FIXTURE_SET) -> rrf.Context:
    return rrf.Context(root=root, spec=spec, package=rrf.Package(root / "docs/reviews/SRR/package.md"))


def png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    assert header[:8] == b"\x89PNG\r\n\x1a\n", path
    return struct.unpack(">II", header[16:24])


def copy_fixture(tmp: str) -> Path:
    root = Path(tmp) / "p"
    shutil.copytree(FIXTURE, root)
    return root


class ParserTests(unittest.TestCase):
    def test_section_stops_at_same_or_higher_heading(self) -> None:
        section = context().package.section("8. Requirements and traceability status")
        self.assertIn("L1 requirements by functional group (fixture grouping):", section)
        self.assertNotIn("## 20. Success criteria self-assessment", section)
        self.assertIn("### 8.1 Following subsection", section, "a lower-level heading stays inside the section")

    def test_missing_section(self) -> None:
        with self.assertRaises(rrf.FigureDataError):
            context().package.section("99. No such section")

    def test_missing_package(self) -> None:
        with self.assertRaises(rrf.FigureDataError):
            rrf.Package(FIXTURE / "docs/reviews/PDR/package.md")

    def test_md_rows_first_table_only(self) -> None:
        rows = rrf.md_rows(["text", "| a | b |", "|---|:---:|", "| 1 | 2 |", "| 3 | 4 |", "", "| x | y |", "|---|---|", "| 5 | 6 |"])
        self.assertEqual([["1", "2"], ["3", "4"]], rows)

    def test_status_of(self) -> None:
        self.assertEqual("Not met", rrf.status_of("**Not met** (awaiting)"))
        self.assertEqual("Partially met", rrf.status_of("Partially met"))
        self.assertEqual("Partially met", rrf.status_of("Partial"))
        self.assertEqual("Met with lien not allowed", rrf.status_of("Met with lien not allowed (interfaces)"))
        self.assertEqual("Met", rrf.status_of("Met (content)"))
        with self.assertRaises(rrf.FigureDataError):
            rrf.status_of("Pending")

    def test_apply_overrides(self) -> None:
        log: list[str] = []
        result = rrf.apply_overrides("row", {"a": "Met", "b": "Not met"}, {"a": ("Partially met", "why"), "b": ("Not met", "same")}, log)
        self.assertEqual({"a": "Partially met", "b": "Not met"}, result)
        self.assertEqual(["row a: package reads Met; figure shows Partially met (why)", "row b: override redundant (package already reads Not met); remove it"], log)
        with self.assertRaises(rrf.FigureDataError):
            rrf.apply_overrides("row", {"a": "Met"}, {"z": ("Met", "unknown row")}, [])

    def test_risk_bands(self) -> None:
        self.assertEqual("Red", rrf.risk_band(2, 5, 5))  # safety override
        self.assertEqual("Yellow", rrf.risk_band(1, 5, 5))  # likelihood 1: no override, score 5
        self.assertEqual("Red", rrf.risk_band(3, 4, 0))
        self.assertEqual("Yellow", rrf.risk_band(2, 3, 0))
        self.assertEqual("Green", rrf.risk_band(1, 4, 0))


class DataKnownAnswerTests(unittest.TestCase):
    def test_entrance(self) -> None:
        ctx = context()
        lanes = rrf.entrance_data(ctx)
        self.assertEqual(
            {
                "Not met": [("S1", "Agenda agreed", "Hard")],
                "Partially met": [("1", "Stakeholders", "Hard"), ("2", "Goals", "Soft")],
                "Met": [("S4†", "Traceability passes", "Hard")],
            },
            lanes,
        )
        self.assertEqual(["entrance row 2: package reads Met; figure shows Partially met (fixture re-rating)"], ctx.log)

    def test_entrance_labels_must_match_the_package(self) -> None:
        spec = dataclasses.replace(FIXTURE_SET, entrance_labels={"S1": "x", "S4": "y", "1": "z"})
        with self.assertRaisesRegex(rrf.FigureDataError, r"entrance rows and figure-set labels differ: \['2'\]"):
            rrf.entrance_data(context(spec=spec))

    def test_success(self) -> None:
        ctx = context()
        lanes = rrf.success_data(ctx)
        self.assertEqual({"Not met": [("4.4-1", "L1 responds to NGOs"), ("4.4-4", "Interfaces identified")], "Partially met": [], "Met": [("C1", "Gate criteria")]}, lanes)
        self.assertIn("success criterion C1: override redundant (package already reads Met); remove it", ctx.log)

    def test_a_status_without_a_lane_stops_the_run(self) -> None:
        spec = dataclasses.replace(FIXTURE_SET, success_overrides={})
        with self.assertRaisesRegex(rrf.FigureDataError, "4.4-4: status 'Met with lien not allowed' has no lane"):
            rrf.success_data(context(spec=spec))

    def test_requirements(self) -> None:
        data = rrf.requirements_data(context())
        self.assertEqual([("Transmitter", 3, 1, 1, 1, 0, 0, 1, 1), ("Receiver", 2, 0, 0, 0, 1, 1, 1, 0)], data["groups"])
        self.assertEqual((5, 4, 1), (data["total"], data["live"], data["tbr"]))
        self.assertEqual({"Test": 1, "Analysis": 1, "Inspection": 1, "Demonstration": 1}, dict(data["methods"]))

    def test_requirements_package_row_must_equal_the_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_fixture(tmp)
            path = root / "docs/requirements/sys/requirements.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["requirements"][1]["verification_method"] = "Inspection"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(rrf.FigureDataError, r"package group 'Transmitter': package \(3, 1, 1, 1, 0, 0, 1, 1\) differs"):
                rrf.requirements_data(context(root))

    def test_requirement_in_no_group_stops_the_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_fixture(tmp)
            path = root / "docs/requirements/sys/requirements.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["requirements"].append(dict(data["requirements"][1], id="REQ-SYS-006"))
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(rrf.FigureDataError, r"REQ-SYS-006"):
                rrf.requirements_data(context(root))

    def test_kdr(self) -> None:
        data = rrf.kdr_data(context())
        self.assertEqual(2, data["count"])
        self.assertEqual(
            [("Transmitter", [("001", "Carrier 144.001 to 147.999 MHz", "Test", True)]), ("Receiver", [("004", "MDS at most -140 dBm", "Inspection", False)])],
            data["groups"],
        )

    def test_kdr_set_must_equal_the_file(self) -> None:
        spec = dataclasses.replace(FIXTURE_SET, kdr_text=(("Transmitter", (("001", "Carrier"),)),), kdr_columns=((0,),))
        with self.assertRaisesRegex(rrf.FigureDataError, r"\['REQ-SYS-004'\]"):
            rrf.kdr_data(context(spec=spec))

    def test_kdr_columns_place_every_group_once(self) -> None:
        spec = dataclasses.replace(FIXTURE_SET, kdr_columns=((0, 1), (1,)))
        with self.assertRaises(rrf.FigureDataError):
            rrf.kdr_data(context(spec=spec))

    def test_hazards(self) -> None:
        data = rrf.hazards_data(context())
        self.assertEqual({("Catastrophic", "B"): ["001"], ("Marginal", "C"): ["002"]}, dict(data["cells"]["initial"]))
        self.assertEqual({("Catastrophic", "D"): ["001"], ("Marginal", "E"): ["002"]}, dict(data["cells"]["residual"]))
        self.assertEqual("0.1.0-fixture", data["version"])

    def test_hazard_matrix_level_must_be_known(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_fixture(tmp)
            path = root / "docs/safety/hazards.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["scales"]["risk_matrix"]["Critical"]["E"] = "Tolerable"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(rrf.FigureDataError, "Critical.*E.*Tolerable"):
                rrf.hazards_data(context(root))

    def test_risk(self) -> None:
        data = rrf.risk_data(context())
        self.assertEqual(3, data["active"], "the Closed risk is excluded")
        self.assertEqual({"Red": 2, "Green": 1}, dict(data["bands"]))
        self.assertEqual({(2, 5): ["RSK-002"]}, dict(data["overridden"]))
        self.assertEqual({(4, 4): ["001"], (2, 5): ["002"], (1, 2): ["003"]}, dict(data["cells"]))

    def test_tpm(self) -> None:
        self.assertEqual(
            [
                ("001", "Mass margin", "no estimate at SRR", "Red", "status rule"),
                ("002", "PA efficiency", "58 % (target 60 %)", "Yellow", ""),
                ("003", "RX MDS", "no estimate", "Not reported", ""),
            ],
            rrf.tpm_data(context()),
        )

    def test_tpm_text_must_carry_the_cbe(self) -> None:
        rows = (FIXTURE_SET.tpm_rows[0], ("002", "PA efficiency", "57 % (target 60 %)", ""), FIXTURE_SET.tpm_rows[2])
        with self.assertRaisesRegex(rrf.FigureDataError, "TPM-002.*cbe 58.0"):
            rrf.tpm_data(context(spec=dataclasses.replace(FIXTURE_SET, tpm_rows=rows)))

    def test_tpm_rows_must_equal_the_file(self) -> None:
        with self.assertRaisesRegex(rrf.FigureDataError, r"\['003'\]"):
            rrf.tpm_data(context(spec=dataclasses.replace(FIXTURE_SET, tpm_rows=FIXTURE_SET.tpm_rows[:2])))

    def test_conops(self) -> None:
        self.assertEqual({"nominal": [("001", "First power-on")], "off_nominal": [("002", "Stuck key")]}, rrf.conops_data(context()))

    def test_conops_scenarios_must_equal_the_file(self) -> None:
        spec = dataclasses.replace(FIXTURE_SET, off_nominal=(("002", "Stuck key"), ("003", "Outside section 6")))
        with self.assertRaisesRegex(rrf.FigureDataError, "off-nominal"):
            rrf.conops_data(context(spec=spec))


class RunTests(unittest.TestCase):
    def test_usage_errors_exit_two(self) -> None:
        self.assertEqual(2, rrf.run("PDR", FIXTURE)[0], "no PDR figure set yet")
        self.assertEqual(2, rrf.run("QDR", FIXTURE)[0], "not a review token")
        self.assertEqual(2, rrf.run("SRR", FIXTURE, figures=["nope"], figure_sets={"SRR": FIXTURE_SET})[0])

    def test_check_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "figures"
            status, lines = rrf.run("SRR", FIXTURE, out=out, check=True, figure_sets={"SRR": FIXTURE_SET})
            self.assertFalse(out.exists())
        self.assertEqual(0, status, lines)
        self.assertIn("  entrance counts {'Not met': 1, 'Partially met': 2, 'Met': 1}", lines)
        self.assertIn("  risks 3 active, bands {'Red': 2, 'Green': 1}, safety override ['RSK-002']", lines)
        self.assertEqual("render_review_figures: SRR check passed for 9 figure(s); nothing written", lines[-1])

    def test_a_disagreement_exits_one_and_writes_nothing(self) -> None:
        spec = dataclasses.replace(FIXTURE_SET, nominal=(("009", "Wrong"),))
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "figures"
            status, lines = rrf.run("SRR", FIXTURE, out=out, figure_sets={"SRR": spec})
            self.assertFalse(out.exists(), "the concept and every figure before conops are not written either")
        self.assertEqual(1, status)
        self.assertTrue(lines[0].endswith("nothing written"), lines)

    def test_render_every_figure_at_its_slide_size(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "figures"
            status, lines = rrf.run("SRR", FIXTURE, out=out, figure_sets={"SRR": FIXTURE_SET})
            self.assertEqual(0, status, lines)
            self.assertEqual(sorted(SIZES), sorted(p.name for p in out.iterdir()))
            for name, size in SIZES.items():
                self.assertEqual(size, png_size(out / name), name)

    def test_default_output_is_the_review_figures_folder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_fixture(tmp)
            status, _ = rrf.run("SRR", root, figures=["hazards"], figure_sets={"SRR": FIXTURE_SET})
            self.assertEqual(0, status)
            self.assertEqual(["hazard-matrix.png"], [p.name for p in (root / "docs/reviews/SRR/figures").iterdir()])

    def test_srr_set(self) -> None:
        self.assertEqual(("entrance", "success", "requirements", "kdr", "hazards", "tpm", "conops"), rrf.SRR.figures,
                         "risk and concept have generators of their own in docs/reviews/SRR/figures/ (see the SRR comment)")
        self.assertTrue(set(rrf.SRR.figures) <= set(rrf.FIGURES))
        self.assertEqual(["SRR"], sorted(rrf.FIGURE_SETS))
        self.assertEqual(2, rrf.run("SRR", FIXTURE, figures=["risk"])[0], "a figure outside the SRR set is a usage error")

    def test_cli(self) -> None:
        pdr = subprocess.run([sys.executable, str(TOOL), "--review", "PDR", "--root", str(FIXTURE)], capture_output=True, text=True, check=False)
        self.assertEqual(2, pdr.returncode, pdr.stdout + pdr.stderr)
        self.assertIn("no figure set is defined for PDR", pdr.stderr)
        srr = subprocess.run([sys.executable, str(TOOL), "--review", "SRR", "--root", str(FIXTURE), "--check"], capture_output=True, text=True, check=False)
        self.assertEqual(1, srr.returncode, "the SRR set's labels do not match the fixture package")
        self.assertIn("nothing written", srr.stderr)
        self.assertNotIn("Traceback", srr.stderr)
        self.assertFalse((FIXTURE / "docs/reviews/SRR/figures").exists())


class RepositoryTests(unittest.TestCase):
    """Repository content, not the tool: the SRR set's --check completes on the repository."""

    def test_repository_check_completes(self) -> None:
        result = subprocess.run([sys.executable, str(TOOL), "--review", "SRR", "--check"], capture_output=True, text=True, check=False)
        self.assertIn(result.returncode, (0, 1), result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
