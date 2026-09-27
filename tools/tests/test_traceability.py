"""Known-answer tests for tools/traceability.py (SWE-136 tool validation).

Runs the tool on the two seeded fixtures under tools/tests/fixtures/:

    valid_project    every rule satisfied; exit 0, zero violations, zero warnings;
                     includes an Active requirement with an open TBR (charter
                     section 7), a non-software hazard control closed by
                     'Analysis accepted per RSK-001', a self-derived L2
                     requirement backed by ADR-001, an expectations.json in the
                     real L0 structure, a TC-VAL case, a MOP in tpm.json, a
                     regulatory corpus section, a credited report with a
                     hashed artifact, a stakeholders array with the customer,
                     user and regulator roles (T-21), and a preliminary
                     docs/design/allocation.json that allocates every Draft or
                     Active SYS requirement without an L2 child (T-18)
    invalid_project  one seeded defect per check code: orphan requirement,
                     test case without a requirement, duplicate id (REQ and CON),
                     TBR on a Verified requirement, software hazard control with
                     method Analysis, unresolved RSK-NNN, bad report and NCR
                     artifacts, the writing-rule violations, an L1 requirement
                     with a parent, an L2 requirement without parent or
                     derivation, tags without their obligations, a type that
                     does not match its method, an Active child of a Draft
                     parent, a Closed requirement without the SAR memo, an
                     inconsistent expectations.json without a stakeholders array
                     (STAKEHOLDERS_MISSING, T-21) and two Draft SYS requirements
                     that name no receiving L2 module (SYS_UNALLOCATED, T-18)

    InspectionRouteTests (CR-002 step 5, SRR close-out item 5) holds the known
    answers of the Inspection route of 04 rule 7.3.6 as amended at d992052,
    each built in memory from valid_project so that neither fixture's seeded
    sets change: an accepted SYS control, a missing or misplaced note, a
    missing closing Inspection case, and the excluded SW and SW-<SUB> modules.

    tools/tests/test_tools.py holds the tests added with the pre-SRR rule set
    (02 section 8.5 rows T-03, T-05, T-07, T-08, T-16, T-19, T-20, T-21), and
    tools/tests/test_traceability_srr_rules.py the known-answer tests of
    STAKEHOLDERS_MISSING (T-21) and SYS_UNALLOCATED (T-18).

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

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

EXPECTED_INVALID_VIOLATIONS = {
    "CHILD_AHEAD_OF_PARENT",
    "CHILD_INVERSE",
    "CLOSED_WITHOUT_SAR",
    "EXPECTATIONS_INCONSISTENT",
    "HAZARD_ID_FORMAT",
    "HAZARD_REQ_NOT_TESTED",
    "HAZARD_UNRESOLVED",
    "ID_DUPLICATE",
    "ID_FORMAT",
    "L1_PARENT_NOT_NULL",
    "MODAL_IN_DESCRIPTION",
    "MODULE_MISMATCH",
    "NCR_ARTIFACT",
    "NCR_FRONT_MATTER",
    "NCR_ID_FORMAT",
    "NCR_UNRESOLVED",
    "PARENT_MISSING",
    "PARENT_UNRESOLVED",
    "RATIONALE_EMPTY",
    "REGULATORY_TAG_NO_CLAUSE",
    "REPORT_ARTIFACT",
    "REPORT_ID_FORMAT",
    "REPORT_UNRESOLVED",
    "REQ_UNVERIFIED",
    "SAFETY_TAG_NO_HAZARD",
    "SCHEMA_INVALID",
    "SELF_DERIVED_UNSUPPORTED",
    "SHALL_COUNT",
    "SHALL_IN_TITLE",
    "SOURCE_L0_MISSING",
    "SOURCE_UNRESOLVED",
    "TBD_PRESENT",
    "TBR_CLOSE_BY",
    "TBR_ON_FINAL_STATUS",
    "TBR_UNMARKED",
    "TC_REQ_UNRESOLVED",
    "TC_SETUP_INCOMPLETE",
    "TC_STATUS_EVIDENCE",
    "TC_TYPE_METHOD",
    "VERIFIED_WITHOUT_EVIDENCE",
}

EXPECTED_INVALID_WARNINGS = {
    "CORE_SI_UNCOVERED",
    "FAILED_TC_WITHOUT_NCR",
    "HAZARD_INVERSE",
    "INTERFACE_TAG_NO_ICD",
    "MOE_WITHOUT_OPS",
    "MOP_UNRESOLVED",
    "OBJECTIVE_UNCOVERED",
    "OPS_UNCITED",
    "RENDER_STALE",
    "SOURCE_FILE_MISSING",
    "SOURCE_FORMAT_UNKNOWN",
    "STAKEHOLDERS_MISSING",
    "SYS_UNALLOCATED",
    "UNVERIFIABLE_WORD",
}


def run_cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Run the tool as a subprocess with the report written to a temporary file."""
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "report.md"
        return subprocess.run(
            [sys.executable, str(TOOL), "--root", str(root), "--output", str(output), *args],
            capture_output=True,
            text=True,
            check=False,
        )


def checked_project(root: Path) -> traceability.Project:
    project = traceability.load_project(root)
    traceability.run_checks(project)
    return project


def codes(findings: list[traceability.Finding]) -> set[str]:
    return {f.code for f in findings}


def findings_for(project: traceability.Project, code: str, ident: str) -> list[traceability.Finding]:
    return [f for f in project.findings if f.code == code and ident in f.location]


class ValidProjectTests(unittest.TestCase):
    """The known-good fixture passes every check without warnings."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.project = checked_project(VALID)

    def test_no_violations(self) -> None:
        self.assertEqual([], [f"{f.code} {f.location}: {f.message}" for f in self.project.violations])

    def test_no_warnings(self) -> None:
        self.assertEqual([], [f"{f.code} {f.location}: {f.message}" for f in self.project.warnings])

    def test_cli_exit_zero(self) -> None:
        result = run_cli(VALID)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("0 violation(s), 0 warning(s)", result.stdout)

    def test_active_requirement_with_open_tbr_is_admitted(self) -> None:
        req = self.project.requirements["REQ-SYS-005"]
        self.assertEqual("Active", req.status)
        self.assertIsNotNone(req.tbr)
        self.assertIn("(TBR)", req.description)
        self.assertEqual([], [f for f in self.project.findings if f.code.startswith("TBR_")])

    def test_draft_requirement_with_open_tbr_is_admitted(self) -> None:
        req = self.project.requirements["REQ-SYS-004"]
        self.assertEqual("Draft", req.status)
        self.assertIsNotNone(req.tbr)

    def test_non_software_hazard_control_may_use_analysis_with_existing_risk(self) -> None:
        req = self.project.requirements["REQ-SYS-006"]
        self.assertEqual(["HZ-002"], req.hazard_ids)
        self.assertEqual("Analysis", req.verification_method)
        self.assertIn("RSK-001", self.project.risks or set())
        self.assertEqual([], findings_for(self.project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-006"))

    def test_software_hazard_control_closed_by_test(self) -> None:
        req = self.project.requirements["REQ-SW-KEYER-001"]
        self.assertTrue(self.project.is_software(req))
        self.assertEqual(["TC-SW-KEYER-001"], [tc.id for tc in self.project.closing_cases(req)])

    def test_credited_report_backs_verified_requirement(self) -> None:
        self.assertTrue(self.project.reports_present)
        reports = self.project.reports_for("TC-SYS-002")
        self.assertEqual(1, len(reports))
        self.assertTrue(reports[0].is_credit_pass)
        self.assertEqual("Verified", self.project.requirements["REQ-SYS-003"].status)

    def test_report_verdict_pass(self) -> None:
        report = traceability.build_report(self.project)
        self.assertIn("Result: **PASS**", report)
        self.assertIn("## 11. Checks performed", report)

    def test_regression_set(self) -> None:
        self.assertEqual(["TC-SYS-002"], traceability.regression_set(self.project, ["hardware/kicad/tx-pa.kicad_sch"]))
        self.assertEqual([], traceability.regression_set(self.project, ["hardware/kicad/rx-front-end.kicad_sch"]))
        result = run_cli(VALID, "--regression", "hardware/kicad")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("TC-SYS-002", result.stdout.strip())


class InvalidProjectTests(unittest.TestCase):
    """Every seeded defect is reported with its catalogue code, and nothing else is."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.project = checked_project(INVALID)

    def test_cli_exit_one(self) -> None:
        result = run_cli(INVALID)
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)

    def test_report_only_exits_zero(self) -> None:
        result = run_cli(INVALID, "--report-only")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("VIOLATION", result.stdout)

    def test_violation_codes_exactly_the_seeded_set(self) -> None:
        self.assertEqual(EXPECTED_INVALID_VIOLATIONS, codes(self.project.violations))

    def test_warning_codes_exactly_the_seeded_set(self) -> None:
        self.assertEqual(EXPECTED_INVALID_WARNINGS, codes(self.project.warnings))

    def test_orphan_requirement(self) -> None:
        self.assertTrue(findings_for(self.project, "REQ_UNVERIFIED", "REQ-RX-002"))

    def test_test_case_without_requirement(self) -> None:
        self.assertTrue(findings_for(self.project, "TC_REQ_UNRESOLVED", "TC-SYS-002"))

    def test_duplicate_id_within_one_file(self) -> None:
        self.assertTrue(findings_for(self.project, "ID_DUPLICATE", "REQ-SYS-002"))
        self.assertIsNotNone(self.project.requirements["REQ-SYS-002"].tbr, "the first definition is kept")

    def test_tbr_rules(self) -> None:
        self.assertTrue(findings_for(self.project, "TBR_UNMARKED", "REQ-SYS-002"))
        self.assertTrue(findings_for(self.project, "TBR_CLOSE_BY", "REQ-SYS-002"), "an L1 TBR closing at CDR is later than PDR")
        self.assertTrue(findings_for(self.project, "TBR_ON_FINAL_STATUS", "REQ-SYS-005"))

    def test_software_hazard_control_gets_no_analysis_exception(self) -> None:
        hits = findings_for(self.project, "HAZARD_REQ_NOT_TESTED", "REQ-SW-SAFE-001")
        self.assertEqual(1, len(hits))
        self.assertIn("SWE-192", hits[0].message)

    def test_analysis_exception_needs_existing_risk(self) -> None:
        hits = findings_for(self.project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-006")
        self.assertEqual(1, len(hits))
        self.assertIn("RSK-999", hits[0].message)

    def test_hazard_requirement_with_method_test_needs_closing_test_case(self) -> None:
        self.assertTrue(findings_for(self.project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-003"))

    def test_word_lint(self) -> None:
        self.assertTrue(findings_for(self.project, "MODAL_IN_DESCRIPTION", "REQ-SYS-006"))
        self.assertTrue(findings_for(self.project, "MODAL_IN_DESCRIPTION", "REQ-sys-004"))
        self.assertTrue(findings_for(self.project, "SHALL_IN_TITLE", "REQ-SYS-006"))
        weak = findings_for(self.project, "UNVERIFIABLE_WORD", "REQ-SYS-003")
        self.assertTrue(weak and "adequate" in weak[0].message)

    def test_report_and_ncr_evidence(self) -> None:
        self.assertTrue(findings_for(self.project, "REPORT_ID_FORMAT", "TC-SYS-001-r2.md"))
        self.assertTrue(findings_for(self.project, "REPORT_ARTIFACT", "TC-SYS-001-r2.md"))
        self.assertTrue(findings_for(self.project, "REPORT_UNRESOLVED", "TC-SYS-009-r1.md"))
        self.assertEqual(2, len(findings_for(self.project, "NCR_ARTIFACT", "NCR-001")))

    def test_every_finding_code_is_catalogued(self) -> None:
        catalogue = {code for code, _, _ in traceability.CHECK_CATALOGUE}
        self.assertTrue(codes(self.project.findings) <= catalogue)
        self.assertNotIn("TBR_STATUS", catalogue)
        self.assertNotIn("SHOULD_IN_DESCRIPTION", catalogue)

    def test_report_verdict_fail(self) -> None:
        self.assertIn("Result: **FAIL**", traceability.build_report(self.project))


class InspectionRouteTests(unittest.TestCase):
    """CR-002 step 5: 04 rule 7.3.6 (amended at d992052) admits Inspection for a non-software hazard control.

    The route needs all three of: module other than SW and SW-<SUB>, method
    Inspection with a live closing case of method Inspection, and a
    verification_note beginning 'Inspection accepted per CR-002'. Each case
    starts from valid_project (zero findings) and converts the non-software
    hazard control REQ-SYS-006 (HZ-002) and its case TC-SYS-006, or the
    software hazard control REQ-SW-KEYER-001 (HZ-001) and its case
    TC-SW-KEYER-001, to Inspection in memory.
    """

    NOTE = "Inspection accepted per CR-002 (SRR decision 113): checklist inspection of the controlled document."

    def converted(self, req_id: str, tc_id: str, note: str, case_method: str = "Inspection") -> traceability.Project:
        project = traceability.load_project(VALID)
        req = project.requirements[req_id]
        req.verification_method = "Inspection"
        req.verification_note = note
        case = project.test_cases[tc_id]
        case.verification_method = case_method
        case.type = "Inspection" if case_method == "Inspection" else case.type
        traceability.run_checks(project)
        return project

    def test_accepted_non_software_control(self) -> None:
        project = self.converted("REQ-SYS-006", "TC-SYS-006", self.NOTE)
        self.assertFalse(project.is_software(project.requirements["REQ-SYS-006"]))
        self.assertEqual(["TC-SYS-006"], [tc.id for tc in project.closing_cases(project.requirements["REQ-SYS-006"])])
        self.assertEqual([], [f"{f.code} {f.location}: {f.message}" for f in project.findings], "the converted fixture stays free of findings")

    def test_missing_note_is_rejected(self) -> None:
        for note in ("", "Analysis accepted per RSK-001: far-field calculation.", "Checked by Inspection accepted per CR-002.", "Inspection accepted per CR-0021"):
            with self.subTest(note=note):
                project = self.converted("REQ-SYS-006", "TC-SYS-006", note)
                hits = findings_for(project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-006")
                self.assertEqual(1, len(hits))
                self.assertIn("does not begin 'Inspection accepted per CR-002'", hits[0].message)
                self.assertIn("04 rule 7.3.6", hits[0].message)
                self.assertEqual({"HAZARD_REQ_NOT_TESTED"}, codes(project.findings))

    def test_missing_closing_inspection_case_is_rejected(self) -> None:
        project = self.converted("REQ-SYS-006", "TC-SYS-006", self.NOTE, case_method="Analysis")
        hits = findings_for(project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-006")
        self.assertEqual(1, len(hits))
        self.assertIn("no closing case of method Inspection", hits[0].message)

    def test_excluded_software_module(self) -> None:
        project = self.converted("REQ-SW-KEYER-001", "TC-SW-KEYER-001", self.NOTE)
        req = project.requirements["REQ-SW-KEYER-001"]
        self.assertEqual("SW-KEYER", req.module)
        self.assertTrue(project.is_software(req))
        hits = findings_for(project, "HAZARD_REQ_NOT_TESTED", "REQ-SW-KEYER-001")
        self.assertEqual(1, len(hits), "SWE-192: no Inspection route for SW-<SUB>")
        self.assertIn("SWE-192", hits[0].message)
        self.assertNotIn("04 rule 7.3.6", hits[0].message)

    def test_excluded_module_sw(self) -> None:
        project = traceability.load_project(VALID)
        req = project.requirements["REQ-SW-KEYER-001"]
        req.module = "SW"
        req.verification_method = "Inspection"
        req.verification_note = self.NOTE
        self.assertTrue(project.is_software(req))
        project.findings.clear()
        traceability.check_hazard_verification(project, req, f"{req.file} {req.id}", ["HZ-001"])
        hits = [f for f in project.findings if f.code == "HAZARD_REQ_NOT_TESTED"]
        self.assertEqual(1, len(hits), "SWE-192: no Inspection route for module SW")
        self.assertIn("SWE-192", hits[0].message)

    def test_catalogue_states_the_route(self) -> None:
        rule = {code: text for code, _, text in traceability.CHECK_CATALOGUE}["HAZARD_REQ_NOT_TESTED"]
        self.assertIn("'Inspection accepted per CR-002'", rule)
        self.assertIn("Modules SW and SW-<SUB>: SWE-192, no exception", rule)


class WordListTests(unittest.TestCase):
    """The lint lists are the WR-07 lists of 02 section 4.2, matched on whole words."""

    def test_group_sizes(self) -> None:
        self.assertEqual(6, len(traceability.WR07_GROUP_A))
        self.assertEqual(34, len(traceability.WR07_GROUP_B))

    def test_whole_word_matching(self) -> None:
        self.assertTrue(traceability.MODAL_WORDS.search("The radio must key."))
        self.assertFalse(traceability.MODAL_WORDS.search("The mustard is yellow."))
        self.assertTrue(traceability.UNVERIFIABLE_WORDS.search("The radio shall be safe."))
        self.assertFalse(traceability.UNVERIFIABLE_WORDS.search("The radio shall enter SafeState."))
        self.assertTrue(traceability.UNVERIFIABLE_WORDS.search("Adjust ad hoc as needed."))
        self.assertTrue(traceability.UNVERIFIABLE_WORDS.search("Supports etc. and/or more."))


class RepositoryTests(unittest.TestCase):
    """The tool runs to completion on the repository itself.

    Zero violations on the repository is a gate criterion (the report is an
    entrance product of every review, 01 section 3.1), checked by the plain run
    at the readiness declaration, not by this tool test: while requirements are
    written ahead of their test cases, REQ_UNVERIFIED is the correct result.
    This test asserts that the run completes (exit 0 or 1, never a usage error
    or a crash), writes both outputs, and reports only catalogued codes.
    """

    def test_repository_run_completes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.md"
            result = subprocess.run(
                [sys.executable, str(TOOL), "--root", str(traceability.REPO_ROOT), "--output", str(output)],
                capture_output=True, text=True, check=False,
            )
            self.assertIn(result.returncode, (0, 1), result.stdout + result.stderr)
            self.assertEqual("", result.stderr)
            self.assertTrue(output.is_file())
            self.assertTrue((Path(tmp) / traceability.DEFAULT_JSON_NAME).is_file())
        project = checked_project(traceability.REPO_ROOT)
        catalogue = {code for code, _, _ in traceability.CHECK_CATALOGUE}
        self.assertTrue(codes(project.findings) <= catalogue, codes(project.findings) - catalogue)


if __name__ == "__main__":
    unittest.main()
