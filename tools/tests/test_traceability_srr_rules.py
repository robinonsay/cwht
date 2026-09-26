"""Known-answer tests for the two rules of tools/traceability.py due before SRR
(docs/process/02-requirements-and-traceability.md section 8.5 rows T-18 and T-21;
SWE-136 tool validation):

    STAKEHOLDERS_MISSING  T-21, stakeholder part (with the stakeholder-name part
                          of T-03): the stakeholders array of expectations.json
                          exists, holds the roles customer, user and regulator,
                          has unique names and resolving source_ids (02 section
                          3.0). Plain-run severity Warning before SRR.
    SYS_UNALLOCATED       T-18 at SRR: every Draft or Active SYS requirement names
                          a receiving L2 module through child_ids or a preliminary
                          docs/design/allocation.json record (02 section 2.3).
                          Plain-run severity Warning; Error from PDR under --gate.

The fixtures are tools/tests/fixtures/valid_project (both rules satisfied: three
stakeholders, two SYS requirements allocated by SW-KEYER children and three by
allocation.json, one through each record form the tool reads: modules[],
elements[] and allocations[], with functions[] and gaps[] entries that allocate
nothing) and tools/tests/fixtures/invalid_project (no stakeholders array;
REQ-SYS-007 and REQ-sys-004 without children and without allocation.json).
Variants run on in-memory projects or temporary copies, so the seeded sets of
test_traceability.py stay unchanged.

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import traceability  # noqa: E402

FIXTURES = TOOLS / "tests" / "fixtures"
VALID = FIXTURES / "valid_project"
INVALID = FIXTURES / "invalid_project"
TOOL = TOOLS / "traceability.py"
ALLOCATION = "docs/design/allocation.json"
EXPECTATIONS = "docs/requirements/l0-stakeholder/expectations.json"


def checked(project: traceability.Project) -> traceability.Project:
    project.findings = []
    traceability.run_checks(project)
    return project


def load(root: Path) -> traceability.Project:
    return checked(traceability.load_project(root))


def of(project: traceability.Project, code: str) -> list[traceability.Finding]:
    return [f for f in project.findings if f.code == code]


def copy_valid(tmp: str) -> Path:
    root = Path(tmp) / "p"
    shutil.copytree(VALID, root)
    return root


def run_cli(root: Path, tmp: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), "--root", str(root), "--output", str(Path(tmp) / "out" / "r.md")],
        capture_output=True, text=True, check=False,
    )


class CatalogueTests(unittest.TestCase):
    def test_both_codes_are_catalogued_as_warnings(self) -> None:
        catalogue = {code: severity for code, severity, _ in traceability.CHECK_CATALOGUE}
        self.assertEqual(traceability.WARNING, catalogue["STAKEHOLDERS_MISSING"])
        self.assertEqual(traceability.WARNING, catalogue["SYS_UNALLOCATED"])

    def test_required_roles(self) -> None:
        self.assertEqual(("customer", "user", "regulator"), traceability.REQUIRED_STAKEHOLDER_ROLES)

    def test_l2_modules(self) -> None:
        for module in ("RX", "TX", "PWR", "CTL", "ME", "SW", "SW-KEYER"):
            self.assertTrue(traceability.is_l2_module(module), module)
        for module in ("SYS", "VAL", "ATP", "VER", "sw-keyer", ""):
            self.assertFalse(traceability.is_l2_module(module), module)


class StakeholdersKnownAnswerTests(unittest.TestCase):
    """T-21 STAKEHOLDERS_MISSING (02 section 3.0)."""

    def mutate(self, change) -> traceability.Project:
        project = traceability.load_project(VALID)
        change(project.expectations_raw["stakeholders"])
        return checked(project)

    def test_valid_fixture_passes(self) -> None:
        project = load(VALID)
        self.assertEqual([], of(project, "STAKEHOLDERS_MISSING"))
        self.assertEqual(3, len(project.expectations_raw["stakeholders"]))

    def test_invalid_fixture_reports_the_absent_array_once(self) -> None:
        hits = of(load(INVALID), "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertEqual(f"{EXPECTATIONS} stakeholders", hits[0].location)
        self.assertIn("stakeholders array absent", hits[0].message)
        self.assertEqual(traceability.WARNING, hits[0].severity)

    def test_empty_array(self) -> None:
        project = traceability.load_project(VALID)
        project.expectations_raw["stakeholders"] = []
        hits = of(checked(project), "STAKEHOLDERS_MISSING")
        self.assertEqual(["stakeholders array empty"], [h.message.split(";")[0] for h in hits])

    def test_not_an_array(self) -> None:
        project = traceability.load_project(VALID)
        project.expectations_raw["stakeholders"] = {"name": "x"}
        hits = of(checked(project), "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertIn("not an array", hits[0].message)

    def test_missing_role_is_named(self) -> None:
        project = self.mutate(lambda entries: entries.pop(2))  # the regulator
        hits = of(project, "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertTrue(hits[0].message.startswith("no entry of role regulator;"), hits[0].message)

    def test_two_missing_roles(self) -> None:
        project = self.mutate(lambda entries: [entries.pop(1), entries.pop(0)])
        hits = of(project, "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertTrue(hits[0].message.startswith("no entry of role customer, user;"), hits[0].message)

    def test_other_roles_do_not_satisfy_the_rule(self) -> None:
        def change(entries: list) -> None:
            entries[2]["role"] = "public"
        hits = of(self.mutate(change), "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertIn("regulator", hits[0].message)

    def test_duplicate_name(self) -> None:
        def change(entries: list) -> None:
            entries.append(dict(entries[0], role="user"))
        hits = of(self.mutate(change), "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertEqual(f"{EXPECTATIONS} stakeholders[3] Owner (customer)", hits[0].location)
        self.assertIn("already used by stakeholders[0]", hits[0].message)

    def test_unresolved_source(self) -> None:
        def change(entries: list) -> None:
            entries[1]["source_ids"].append("SI-099")
        hits = of(self.mutate(change), "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertEqual(f"{EXPECTATIONS} stakeholders[1] Owner (operator)", hits[0].location)
        self.assertIn("'SI-099' not found in docs/requirements/l0-stakeholder/stakeholder-inputs.md", hits[0].message)

    def test_unknown_source_scheme(self) -> None:
        def change(entries: list) -> None:
            entries[0]["source_ids"] = ["STK-001"]
        hits = of(self.mutate(change), "STAKEHOLDERS_MISSING")
        self.assertEqual(1, len(hits))
        self.assertIn("'STK-001' matches no known scheme", hits[0].message)

    def test_sources_unchecked_while_stakeholder_inputs_are_absent(self) -> None:
        project = traceability.load_project(VALID)
        project.stakeholder_inputs = None
        checked(project)
        self.assertEqual([], of(project, "STAKEHOLDERS_MISSING"))
        missing = [f for f in of(project, "SOURCE_FILE_MISSING") if "stakeholder-inputs.md" in f.location]
        self.assertEqual(1, len(missing), "one warning per absent file, stakeholder sources included")
        self.assertIn("Federal Communications Commission:SI-014", missing[0].message)
        self.assertIn("CON-001:SI-014", missing[0].message)

    def test_not_evaluated_without_expectations(self) -> None:
        project = traceability.load_project(VALID)
        project.expectations_raw = None
        self.assertEqual([], of(checked(project), "STAKEHOLDERS_MISSING"))

    def test_warning_only_exit_zero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            path = root / EXPECTATIONS
            data = json.loads(path.read_text(encoding="utf-8"))
            del data["stakeholders"]
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            result = run_cli(root, tmp)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("WARNING   STAKEHOLDERS_MISSING", result.stdout)

    def test_render_lists_the_stakeholders(self) -> None:
        text = traceability.render_expectations(traceability.load_project(VALID))
        section = text.split("## 7. Stakeholders")[1]
        self.assertIn("| Name | Role | Interests | Represented by (V2) | Sources | Note |", section)
        self.assertIn("| Federal Communications Commission | regulator |", section)
        self.assertIn("| SI-014 | Fixture entry for the T-21 known-answer test |", section)
        rendered = (VALID / "docs/requirements/l0-stakeholder/expectations.md").read_text(encoding="utf-8")
        self.assertEqual(text, rendered, "re-render the fixture (tools/README.md, last paragraph)")

    def test_render_states_an_absent_array(self) -> None:
        project = traceability.load_project(VALID)
        del project.expectations_raw["stakeholders"]
        text = traceability.render_expectations(project)
        self.assertIn("The `stakeholders` array is absent or empty", text.split("## 7. Stakeholders")[1])


class AllocationKnownAnswerTests(unittest.TestCase):
    """T-18 SYS_UNALLOCATED at SRR (02 section 2.3)."""

    def test_valid_fixture_passes_with_the_known_modules(self) -> None:
        project = load(VALID)
        self.assertEqual([], of(project, "SYS_UNALLOCATED"))
        reqs = project.requirements
        self.assertEqual(
            {
                "REQ-SYS-001": ["SW-KEYER"],
                "REQ-SYS-002": ["SW-KEYER"],
                "REQ-SYS-003": [],
                "REQ-SYS-004": ["CTL"],
                "REQ-SYS-005": ["PWR"],
                "REQ-SYS-006": ["ME", "TX"],
            },
            {rid: project.receiving_modules(reqs[rid]) for rid in sorted(reqs) if rid.startswith("REQ-SYS-")},
        )
        self.assertTrue(project.allocation_present)
        self.assertIsNone(project.allocation_error)

    def test_each_record_form_is_read(self) -> None:
        project = traceability.load_project(VALID)
        self.assertEqual(
            {"REQ-SYS-004": {"CTL"}, "REQ-SYS-005": {"PWR"}, "REQ-SYS-006": {"TX", "ME"}},
            project.allocation_modules,
            "modules[] id (CTL, TX), elements[] module (ME), allocations[] modules (PWR); functions[] and gaps[] allocate nothing",
        )

    def test_invalid_fixture_lists_exactly_the_two_gaps(self) -> None:
        hits = of(load(INVALID), "SYS_UNALLOCATED")
        self.assertEqual(
            ["docs/requirements/sys/requirements.json REQ-SYS-007", "docs/requirements/sys/requirements.json REQ-sys-004"],
            sorted(h.location for h in hits),
        )
        for hit in hits:
            self.assertEqual(traceability.WARNING, hit.severity)
            self.assertIn("Draft SYS requirement names no receiving L2 module", hit.message)
            self.assertIn("docs/design/allocation.json is absent", hit.message)
            self.assertIn("V6", hit.message)

    def test_verified_requirement_without_children_is_not_listed(self) -> None:
        project = load(INVALID)
        self.assertEqual("Verified", project.requirements["REQ-SYS-003"].status)
        self.assertEqual([], project.receiving_modules(project.requirements["REQ-SYS-003"]))
        self.assertFalse([f for f in of(project, "SYS_UNALLOCATED") if "REQ-SYS-003" in f.location])

    def test_absent_allocation_lists_every_unchilded_draft_or_active_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / ALLOCATION).unlink()
            project = load(root)
            result = run_cli(root, tmp)
        hits = of(project, "SYS_UNALLOCATED")
        self.assertEqual(["REQ-SYS-004", "REQ-SYS-005", "REQ-SYS-006"], sorted(h.location.split()[-1] for h in hits))
        self.assertIn("Active SYS requirement", [h for h in hits if h.location.endswith("REQ-SYS-005")][0].message)
        self.assertEqual(0, result.returncode, "a Warning never changes the exit status")
        self.assertIn("WARNING   SYS_UNALLOCATED", result.stdout)

    def test_allocation_to_a_non_l2_module_does_not_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / ALLOCATION).write_text(json.dumps({"elements": [
                {"id": "B12", "module": "CTL", "requirement_ids": ["REQ-SYS-004"]},
                {"id": "B19", "module": "PWR", "requirement_ids": ["REQ-SYS-005"]},
                {"id": "X01", "module": "SYS", "requirement_ids": ["REQ-SYS-006"]},
            ]}), encoding="utf-8")
            hits = of(load(root), "SYS_UNALLOCATED")
        self.assertEqual(1, len(hits))
        self.assertTrue(hits[0].location.endswith("REQ-SYS-006"))
        self.assertIn("lists it only under SYS, not an L2 module", hits[0].message)

    def test_requirement_absent_from_allocation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / ALLOCATION).write_text(json.dumps({"elements": [
                {"id": "B12", "module": "CTL", "requirement_ids": ["REQ-SYS-004", "REQ-SYS-006"]},
            ]}), encoding="utf-8")
            hits = of(load(root), "SYS_UNALLOCATED")
        self.assertEqual(1, len(hits))
        self.assertTrue(hits[0].location.endswith("REQ-SYS-005"))
        self.assertIn("lists it under no module", hits[0].message)

    def test_unparsable_allocation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / ALLOCATION).write_text("{ not json", encoding="utf-8")
            project = load(root)
        hits = of(project, "SYS_UNALLOCATED")
        self.assertEqual(4, len(hits))
        file_hits = [h for h in hits if h.location == ALLOCATION]
        self.assertEqual(1, len(file_hits))
        self.assertIn("only child_ids count", file_hits[0].message)
        for hit in hits:
            if hit.location != ALLOCATION:
                self.assertIn("does not parse", hit.message)
        self.assertIsNotNone(project.allocation_error)

    def test_nested_module_records_and_module_less_lists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / ALLOCATION).write_text(json.dumps({
                "modules": [
                    {"module": "PWR", "elements": [{"id": "B19", "requirement_ids": ["REQ-SYS-005"]}]},
                    {"module": "TX", "elements": [{"id": "B01", "requirement_ids": ["REQ-SYS-006"]}, {"id": "B12", "module": "CTL", "requirement_ids": ["REQ-SYS-006"]}]},
                ],
                "unassigned": {"requirement_ids": ["REQ-SYS-004"]},
            }), encoding="utf-8")
            project = load(root)
        self.assertEqual({"REQ-SYS-005": {"PWR"}, "REQ-SYS-006": {"TX", "CTL"}}, project.allocation_modules)
        hits = of(project, "SYS_UNALLOCATED")
        self.assertEqual(["REQ-SYS-004"], [h.location.split()[-1] for h in hits])

    def test_child_through_parent_id_counts(self) -> None:
        project = traceability.load_project(VALID)
        project.requirements["REQ-SYS-001"].child_ids = []
        checked(project)
        self.assertFalse([f for f in of(project, "SYS_UNALLOCATED") if f.location.endswith("REQ-SYS-001")])
        self.assertTrue([f for f in of(project, "CHILD_INVERSE") if "REQ-SW-KEYER-001" in f.location])

    def test_retired_child_does_not_count(self) -> None:
        project = traceability.load_project(VALID)
        child = project.requirements["REQ-SW-KEYER-001"]
        child.status, child.tags = "Closed", child.tags + ["retired"]
        checked(project)
        hits = [f for f in of(project, "SYS_UNALLOCATED") if f.location.endswith("REQ-SYS-001")]
        self.assertEqual(1, len(hits))
        self.assertIn("children named: REQ-SW-KEYER-001", hits[0].message)

    def test_child_of_another_sys_requirement_does_not_count(self) -> None:
        project = traceability.load_project(INVALID)
        checked(project)
        self.assertEqual(["PWR", "RX"], project.receiving_modules(project.requirements["REQ-SYS-001"]), "REQ-SYS-007 in child_ids is not L2")

    def test_retired_sys_requirement_is_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / ALLOCATION).unlink()
            project = traceability.load_project(root)
            req = project.requirements["REQ-SYS-004"]
            req.status, req.tags, req.rationale = "Closed", req.tags + ["retired"], "Retired by INSP-001: test."
            checked(project)
        self.assertEqual(["REQ-SYS-005", "REQ-SYS-006"], sorted(f.location.split()[-1] for f in of(project, "SYS_UNALLOCATED")))

    def test_report_states_the_srr_rule(self) -> None:
        project = load(VALID)
        report = traceability.build_report(project)
        section = report.split("### 7.2 Allocation to children")[1].split("### 7.3")[0]
        self.assertNotIn("applies from PDR", report)
        self.assertIn("Rule T-18 (02 section 8.2) applies from SRR", section)
        self.assertIn("| ID | Module | Children | Child ids | Receiving L2 modules |", section)
        self.assertIn("| REQ-SYS-006 | SYS | 0 | - | ME, TX |", section)
        self.assertIn("| Allocation (preliminary at SRR) | docs/design/allocation.json | 3 requirement ids allocated |", report)


class FixtureSchemaTripwireTests(unittest.TestCase):
    """The expectations schema copy used by T-21 carries the repository constraints."""

    @staticmethod
    def constraints(path: Path) -> object:
        def strip(node: object) -> object:
            if isinstance(node, dict):
                return {k: strip(v) for k, v in node.items() if k != "description"}
            if isinstance(node, list):
                return [strip(v) for v in node]
            return node
        return strip(json.loads(path.read_text(encoding="utf-8")))

    def test_expectations_schema_copy(self) -> None:
        relative = "docs/requirements/l0-stakeholder/schema.json"
        self.assertEqual(self.constraints(traceability.REPO_ROOT / relative), self.constraints(VALID / relative),
                         f"re-copy {relative} into tools/tests/fixtures/valid_project, re-render, and re-run the suite")


class RepositoryAllocationTests(unittest.TestCase):
    """Repository content, not the tool (05 section 9.2 keeps these apart from the accreditation run).

    When docs/design/allocation.json carries per-requirement allocations[] records, the
    requirements the tool reads as allocated to an L2 module are exactly those records'
    requirements with an L2 module, so the tool and the file agree on T-18.
    """

    def test_tool_reading_agrees_with_the_allocation_records(self) -> None:
        path = traceability.REPO_ROOT / ALLOCATION
        if not path.is_file():
            self.skipTest("docs/design/allocation.json is absent")
        data = json.loads(path.read_text(encoding="utf-8"))
        records = data.get("allocations") if isinstance(data, dict) else None
        if not isinstance(records, list):
            self.skipTest("docs/design/allocation.json has no allocations[] list")
        expected = {r["requirement_id"] for r in records if isinstance(r, dict) and any(traceability.is_l2_module(m) for m in r.get("modules", []))}
        project = traceability.load_project(traceability.REPO_ROOT)
        read = {rid for rid, modules in project.allocation_modules.items() if any(traceability.is_l2_module(m) for m in modules)}
        self.assertEqual(sorted(expected), sorted(r for r in read if r.startswith("REQ-SYS-")))


if __name__ == "__main__":
    unittest.main()
