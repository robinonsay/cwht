"""Known-answer tests for the pre-SRR rule set of tools/traceability.py and the
hazards convention of tools/validate_docs.py (SWE-136 tool validation).

Covers the rows of docs/process/02-requirements-and-traceability.md section 8.5
that were open before SRR (T-03, T-05, T-07, T-08, T-16, T-19, T-20, T-21), the
T-10 and T-11 additions (TC_TYPE_METHOD, CHILD_AHEAD_OF_PARENT, CLOSED_WITHOUT_SAR,
Failed case without a report), the App. D and App. E columns of
docs/process/04-verification-and-validation.md sections 7.1 and 7.2, the
machine-readable output with the MSR-01/03/04/23 measurements of
docs/process/07-software-engineering-plan.md section 11, and the PyYAML front
matter path. The second group of classes (from RegulationPartsTests on) covers
the 2026-09-25 additions: 47 CFR Parts 1, 2, 15 and 97 (T-07), the test-case
retirement marker of 02 section 11.3 and the remaining T-19 rules, every
closing case Passed and credited for Verified (T-11, 04 rule 7.3.4), TBD in
expectations and ICD tables (T-14), expectation source resolution, and the
--render option with its RENDER_STALE check (02 section 8.1). The third group
(from HazardTraceUnionTests on) covers the revision after independent review:
the hazard trace union of 04 section 3 (SWE-192, SWE-052 row 2), on-target
evidence at SAR, ID_DUPLICATE for HZ, RSK, MOP, TPM, OPS, ADR and TS, the
charter section 6 module sets, SCHEMA_ID_PATTERN_MISSING and SCHEMA_INVALID for
expectations and the risk register, TBD in the ConOps and SEMP, the NCR fields
of 04 sections 10.3 and 10.7, the SWE-052 coverage table, and the validate_docs
rules for log items and history (01 sections 10.3 and 10.4), peer-review
records (SWE-088, SWE-089), decision memos, review folders, the new
conventions and the schema tripwires. These classes use temporary copies of
valid_project so that the seeded sets of test_traceability.py and
test_validate_docs.py stay unchanged. The fixtures are
tools/tests/fixtures/valid_project (exit 0, zero findings) and
tools/tests/fixtures/invalid_project (exit 1, seeded defects).

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import datetime as dt
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
import validate_docs  # noqa: E402

FIXTURES = TOOLS / "tests" / "fixtures"
VALID = FIXTURES / "valid_project"
INVALID = FIXTURES / "invalid_project"

NEW_CODES = {
    "L1_PARENT_NOT_NULL",
    "SELF_DERIVED_UNSUPPORTED",
    "SOURCE_L0_MISSING",
    "SAFETY_TAG_NO_HAZARD",
    "REGULATORY_TAG_NO_CLAUSE",
    "INTERFACE_TAG_NO_ICD",
    "TC_TYPE_METHOD",
    "CHILD_AHEAD_OF_PARENT",
    "CLOSED_WITHOUT_SAR",
    "RETIRED_INCONSISTENT",
    "MOP_UNRESOLVED",
    "EXPECTATIONS_INCONSISTENT",
    "MOE_WITHOUT_OPS",
    "CORE_SI_UNCOVERED",
    "OBJECTIVE_UNCOVERED",
    "OPS_UNCITED",
}


def checked_project(root: Path) -> traceability.Project:
    project = traceability.load_project(root)
    traceability.run_checks(project)
    return project


def findings_for(project: traceability.Project, code: str, ident: str) -> list[traceability.Finding]:
    return [f for f in project.findings if f.code == code and ident in f.location]


def rerun(project: traceability.Project) -> traceability.Project:
    """Clear and recompute the findings after an in-memory mutation."""
    project.findings = []
    traceability.run_checks(project)
    return project


class CatalogueTests(unittest.TestCase):
    def test_new_codes_are_catalogued_with_the_documented_severity(self) -> None:
        catalogue = {code: severity for code, severity, _ in traceability.CHECK_CATALOGUE}
        self.assertTrue(NEW_CODES <= set(catalogue))
        for code in ("INTERFACE_TAG_NO_ICD", "MOP_UNRESOLVED", "MOE_WITHOUT_OPS", "CORE_SI_UNCOVERED", "OBJECTIVE_UNCOVERED", "OPS_UNCITED"):
            self.assertEqual(traceability.WARNING, catalogue[code], code)
        for code in NEW_CODES - {"INTERFACE_TAG_NO_ICD", "MOP_UNRESOLVED", "MOE_WITHOUT_OPS", "CORE_SI_UNCOVERED", "OBJECTIVE_UNCOVERED", "OPS_UNCITED"}:
            self.assertEqual(traceability.VIOLATION, catalogue[code], code)

    def test_catalogue_codes_are_unique(self) -> None:
        codes = [code for code, _, _ in traceability.CHECK_CATALOGUE]
        self.assertEqual(len(codes), len(set(codes)))


class FrontMatterTests(unittest.TestCase):
    TEXT = (
        "---\n"
        "id: NCR-001  # trailing comment\n"
        "requirement_ids: [REQ-SYS-001, REQ-SYS-002]\n"
        "date: 2026-11-02\n"
        "run: 1\n"
        "credit: true\n"
        "date_closed: null\n"
        "artifacts:\n"
        '  - "docs/vv/ncr/NCR-001/a.csv sha256=0000000000000000000000000000000000000000000000000000000000000000"\n'
        "instruments:\n"
        "  - name: NanoVNA\n"
        "    model: H4\n"
        "---\n"
        "# Body\n"
    )

    def test_split_and_missing_block(self) -> None:
        self.assertIsNone(traceability.parse_front_matter("# No front matter\n"))
        self.assertIsNone(traceability.parse_front_matter("---\nid: X\n"))
        self.assertTrue(traceability.split_front_matter(self.TEXT).startswith("id: NCR-001"))

    def test_subset_parser(self) -> None:
        data = traceability.parse_front_matter_subset(traceability.split_front_matter(self.TEXT))
        self.assertEqual("NCR-001", data["id"])
        self.assertEqual(["REQ-SYS-001", "REQ-SYS-002"], data["requirement_ids"])
        self.assertEqual("2026-11-02", data["date"])
        self.assertEqual(1, data["run"])
        self.assertIs(True, data["credit"])
        self.assertIsNone(data["date_closed"])
        self.assertEqual(1, len(data["artifacts"]))
        self.assertEqual([{"name": "NanoVNA", "model": "H4"}], data["instruments"])

    def test_default_parser_matches_subset_semantics(self) -> None:
        data = traceability.parse_front_matter(self.TEXT)
        self.assertIsNotNone(data)
        self.assertEqual("NCR-001", data["id"])
        self.assertEqual(["REQ-SYS-001", "REQ-SYS-002"], data["requirement_ids"])
        self.assertEqual("2026-11-02", str(data["date"]))
        self.assertEqual("1", str(data["run"]))
        self.assertIs(True, data["credit"])
        self.assertEqual([{"name": "NanoVNA", "model": "H4"}], data["instruments"])

    @unittest.skipIf(traceability.yaml is None, "PyYAML not installed in this interpreter")
    def test_yaml_path_is_used_when_available(self) -> None:
        data = traceability.parse_front_matter("---\nnested:\n  key: value\n---\n")
        self.assertEqual({"nested": {"key": "value"}}, data)


class ExpectationsTests(unittest.TestCase):
    """T-03, T-20 and T-21 on the seeded expectations.json."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.invalid = checked_project(INVALID)
        cls.valid = checked_project(VALID)

    def test_valid_expectations_load_with_kinds(self) -> None:
        entries = self.valid.expectation_entries
        self.assertEqual({"NGO-001", "NGO-002", "NGO-003", "MOE-001", "CON-001"}, set(entries))
        self.assertEqual("Need", entries["NGO-001"].kind)
        self.assertEqual("MOE", entries["MOE-001"].kind)
        self.assertEqual("CON", entries["CON-001"].kind)
        self.assertEqual([], [f for f in self.valid.findings if f.code in ("EXPECTATIONS_INCONSISTENT", "ID_DUPLICATE")])

    def test_two_needs(self) -> None:
        hits = [f for f in findings_for(self.invalid, "EXPECTATIONS_INCONSISTENT", "expectations.json") if "kind Need" in f.message]
        self.assertEqual(1, len(hits))
        self.assertIn("NGO-002", hits[0].message)

    def test_parent_kinds(self) -> None:
        self.assertTrue(any("not the Need" in f.message for f in findings_for(self.invalid, "EXPECTATIONS_INCONSISTENT", "NGO-003")))
        self.assertTrue(any("not a Goal" in f.message for f in findings_for(self.invalid, "EXPECTATIONS_INCONSISTENT", "NGO-004")))
        self.assertEqual([], findings_for(self.invalid, "EXPECTATIONS_INCONSISTENT", "NGO-005"))

    def test_moe_links(self) -> None:
        messages = [f.message for f in findings_for(self.invalid, "EXPECTATIONS_INCONSISTENT", "MOE-001")]
        self.assertTrue(any("NGO-999" in m for m in messages), messages)
        self.assertTrue(any("OPS-999" in m for m in messages), messages)
        self.assertTrue(findings_for(self.invalid, "MOE_WITHOUT_OPS", "MOE-002"))

    def test_duplicate_constraint_id(self) -> None:
        self.assertTrue(findings_for(self.invalid, "ID_DUPLICATE", "CON-001"))
        self.assertEqual("Part 97 applies", self.invalid.expectation_entries["CON-001"].title, "the first definition is kept")

    def test_l0_coverage_warnings(self) -> None:
        self.assertTrue(findings_for(self.invalid, "CORE_SI_UNCOVERED", "SI-018"))
        self.assertTrue(findings_for(self.invalid, "OBJECTIVE_UNCOVERED", "NGO-005"))
        self.assertEqual([], findings_for(self.invalid, "OBJECTIVE_UNCOVERED", "NGO-004"), "cited by MOE-002")
        self.assertTrue(findings_for(self.invalid, "OPS_UNCITED", "OPS-001"))
        self.assertEqual([], [f for f in self.valid.findings if f.code in ("CORE_SI_UNCOVERED", "OBJECTIVE_UNCOVERED", "OPS_UNCITED")])

    def test_l0_coverage_skipped_on_empty_requirement_set(self) -> None:
        project = traceability.load_project(INVALID)
        project.requirements = {}
        traceability.run_checks(project)
        self.assertEqual([], [f for f in project.findings if f.code in ("CORE_SI_UNCOVERED", "OBJECTIVE_UNCOVERED", "OPS_UNCITED")])

    def test_core_inputs_detected_from_bold_rows(self) -> None:
        self.assertEqual({"SI-018"}, self.valid.core_inputs)
        self.assertEqual({"SI-018"}, self.invalid.core_inputs)

    def test_conops_headings_only(self) -> None:
        self.assertEqual({"OPS-001"}, self.invalid.conops_scenarios, "OPS-999 in body text is not a heading")


class ParentRuleTests(unittest.TestCase):
    """T-05 and the T-11 child/parent status rule."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.project = checked_project(INVALID)

    def test_l1_parent_not_null(self) -> None:
        self.assertTrue(findings_for(self.project, "L1_PARENT_NOT_NULL", "REQ-SYS-007"))
        self.assertEqual([], [f for f in self.project.findings if f.code == "L1_PARENT_NOT_NULL" and "REQ-SYS-007" not in f.location])

    def test_l2_without_parent_or_derivation(self) -> None:
        self.assertTrue(findings_for(self.project, "PARENT_MISSING", "REQ-RX-003"))
        self.assertEqual([], findings_for(self.project, "SELF_DERIVED_UNSUPPORTED", "REQ-RX-003"))

    def test_self_derived_needs_prefix_and_decision_or_hazard(self) -> None:
        hits = findings_for(self.project, "SELF_DERIVED_UNSUPPORTED", "REQ-RX-004")
        self.assertEqual(1, len(hits))
        self.assertIn("ADR-/TS-", hits[0].message)
        self.assertEqual([], findings_for(self.project, "SELF_DERIVED_UNSUPPORTED", "REQ-SW-SAFE-001"), "hazard-derived control is admitted")

    def test_valid_self_derived_l2_passes(self) -> None:
        valid = checked_project(VALID)
        req = valid.requirements["REQ-SW-KEYER-003"]
        self.assertIsNone(req.parent_id)
        self.assertTrue(req.rationale.startswith("Self-derived:"))
        self.assertEqual([], [f for f in valid.findings if f.code in ("PARENT_MISSING", "SELF_DERIVED_UNSUPPORTED")])

    def test_child_ahead_of_parent(self) -> None:
        self.assertTrue(findings_for(self.project, "CHILD_AHEAD_OF_PARENT", "REQ-RX-006"))
        self.assertEqual([], findings_for(self.project, "CHILD_AHEAD_OF_PARENT", "REQ-RX-001"), "a Draft child of an Active parent is fine")


class SourceRuleTests(unittest.TestCase):
    """T-07 and T-16."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.invalid = checked_project(INVALID)
        cls.valid = checked_project(VALID)

    def test_sys_needs_an_l0_source_once_expectations_exist(self) -> None:
        self.assertTrue(findings_for(self.invalid, "SOURCE_L0_MISSING", "REQ-SYS-002"))
        self.assertEqual([], findings_for(self.invalid, "SOURCE_L0_MISSING", "REQ-SYS-001"))
        self.assertEqual([], findings_for(self.invalid, "SOURCE_L0_MISSING", "REQ-RX-003"), "L2 requirements are exempt")

    def test_constraint_and_regulation_resolution(self) -> None:
        self.assertIs(True, traceability.resolve_source(self.valid, "CON-001"))
        self.assertIs(False, traceability.resolve_source(self.valid, "CON-002"))
        self.assertIs(True, traceability.resolve_source(self.valid, "47CFR97.313(a)"))
        self.assertIs(False, traceability.resolve_source(self.valid, "47CFR97.307(e)"))
        self.assertIs(None, traceability.resolve_source(self.valid, "TS-001"))
        hits = findings_for(self.invalid, "SOURCE_UNRESOLVED", "REQ-SYS-001")
        self.assertTrue(any("47CFR97.999" in f.message for f in hits), hits)

    def test_regulatory_dir_absent_is_a_warning(self) -> None:
        project = traceability.load_project(VALID)
        project.regulations = None
        traceability.run_checks(project)
        hits = [f for f in project.findings if f.code == "SOURCE_FILE_MISSING" and str(traceability.REGULATORY_DIR) in f.location]
        self.assertEqual(1, len(hits))
        self.assertIn("REQ-SYS-003:47CFR97.313(a)", hits[0].message)

    def test_measures(self) -> None:
        self.assertEqual({"MOP-001", "TPM-001"}, self.valid.measures)
        self.assertEqual([], [f for f in self.valid.findings if f.code == "MOP_UNRESOLVED"])
        self.assertTrue(findings_for(self.invalid, "MOP_UNRESOLVED", "REQ-SYS-001"))

    def test_measures_file_absent_is_a_warning(self) -> None:
        project = traceability.load_project(VALID)
        project.measures = None
        traceability.run_checks(project)
        hits = [f for f in project.findings if f.code == "SOURCE_FILE_MISSING" and str(traceability.MEASURES) in f.location]
        self.assertEqual(1, len(hits))


class TagTests(unittest.TestCase):
    def test_tag_obligations(self) -> None:
        project = checked_project(INVALID)
        self.assertTrue(findings_for(project, "SAFETY_TAG_NO_HAZARD", "REQ-RX-005"))
        self.assertTrue(findings_for(project, "REGULATORY_TAG_NO_CLAUSE", "REQ-RX-005"))
        self.assertTrue(findings_for(project, "INTERFACE_TAG_NO_ICD", "REQ-RX-005"))

    def test_safety_tag_with_hazard_passes(self) -> None:
        project = checked_project(VALID)
        self.assertIn("safety", project.requirements["REQ-SYS-006"].tags)
        self.assertEqual([], [f for f in project.findings if f.code.endswith("_TAG_NO_HAZARD") or f.code.endswith("_TAG_NO_CLAUSE") or f.code.endswith("_TAG_NO_ICD")])


class EvidenceRuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.project = checked_project(INVALID)

    def test_type_method_compatibility(self) -> None:
        hits = findings_for(self.project, "TC_TYPE_METHOD", "TC-SYS-005")
        self.assertEqual(1, len(hits))
        self.assertIn("HostUnit", hits[0].message)
        self.assertEqual({"TC-SYS-005"}, {f.location.split()[-1] for f in self.project.findings if f.code == "TC_TYPE_METHOD"})

    def test_failed_and_passed_cases_need_reports(self) -> None:
        self.assertTrue(any("Failed" in f.message for f in findings_for(self.project, "TC_STATUS_EVIDENCE", "TC-SYS-003")))
        self.assertTrue(any("Passed" in f.message for f in findings_for(self.project, "TC_STATUS_EVIDENCE", "TC-SYS-006")))

    def test_closed_requirement_rules(self) -> None:
        hits = findings_for(self.project, "CLOSED_WITHOUT_SAR", "REQ-SYS-008")
        self.assertEqual(1, len(hits))
        self.assertIn(str(traceability.SAR_DECISION_MEMO), hits[0].message)
        self.assertTrue(findings_for(self.project, "VERIFIED_WITHOUT_EVIDENCE", "REQ-SYS-008"), "Closed carries the Verified evidence rules")

    def test_closed_needs_validated_dependent_rows(self) -> None:
        project = traceability.load_project(VALID)
        project.sar_memo_present = True
        req = project.requirements["REQ-SYS-001"]
        req.status = "Closed"
        traceability.run_checks(project)
        hits = findings_for(project, "CLOSED_WITHOUT_SAR", "REQ-SYS-001")
        self.assertEqual(1, len(hits))
        self.assertIn("MOE-001", hits[0].message)
        self.assertIn("OPS-001", hits[0].message)

    def test_hazard_control_union(self) -> None:
        project = checked_project(VALID)
        self.assertEqual(["REQ-SW-KEYER-001", "REQ-SYS-001"], sorted(project.hazards["HZ-001"].control_req_ids or []))
        self.assertEqual([], [f for f in project.findings if f.code == "HAZARD_INVERSE"])
        project.hazards["HZ-001"].control_req_ids = ["REQ-SYS-001"]
        rerun(project)
        self.assertTrue(any("union" in f.message for f in findings_for(project, "HAZARD_INVERSE", "HZ-001")))


class RetiredTests(unittest.TestCase):
    """T-19 and the T-10 retired-citation rule, exercised in memory because the
    schemas gain the Retired value before SRR (02 section 11.3)."""

    def retire(self) -> traceability.Project:
        project = traceability.load_project(VALID)
        req = project.requirements["REQ-SYS-006"]
        req.status = traceability.RETIRED
        return project

    def test_retired_requirement_without_prefix_or_retired_case(self) -> None:
        project = self.retire()
        traceability.run_checks(project)
        messages = [f.message for f in findings_for(project, "RETIRED_INCONSISTENT", "REQ-SYS-006")]
        self.assertEqual(2, len(messages), messages)
        self.assertTrue(any("Retired by" in m for m in messages))
        self.assertTrue(any("TC-SYS-006" in m for m in messages))
        self.assertEqual([], findings_for(project, "REQ_UNVERIFIED", "REQ-SYS-006"))
        self.assertEqual([], findings_for(project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-006"))

    def test_consistent_retirement_passes_and_leaves_the_matrix(self) -> None:
        project = self.retire()
        req = project.requirements["REQ-SYS-006"]
        req.rationale = "Retired by RID-SRR-001: superseded by REQ-SYS-007. " + req.rationale
        req.tbr = None
        tc = project.test_cases["TC-SYS-006"]
        tc.status = traceability.RETIRED
        tc.setup = "Retired by RID-SRR-001: the requirement was retired. " + tc.setup
        traceability.run_checks(project)
        self.assertEqual([], [f for f in project.findings if f.code == "RETIRED_INCONSISTENT"])
        self.assertNotIn("REQ-SYS-006", [r.id for r in project.live_requirements()])
        report = traceability.build_report(project, dt.date(2026, 9, 25))
        matrix = report.split("## 3. Requirements verification matrix")[1].split("## 4.")[0]
        self.assertNotIn("| REQ-SYS-006 |", matrix)
        self.assertIn("| Requirements Retired | 1 |", report)

    def test_charter_interim_form_closed_with_tag_retired(self) -> None:
        """Charter section 6: status Closed plus tag retired is a retirement, not a closure."""
        project = traceability.load_project(VALID)
        req = project.requirements["REQ-SYS-006"]
        req.status = "Closed"
        req.tags = ["safety", "retired"]
        req.rationale = "Retired by RID-SRR-002: RF exposure moved to the ME module. " + req.rationale
        project.test_cases["TC-SYS-006"].status = traceability.RETIRED
        project.test_cases["TC-SYS-006"].setup = "Retired by RID-SRR-002: requirement retired."
        traceability.run_checks(project)
        self.assertTrue(req.is_retired)
        self.assertEqual([], [f for f in project.findings if f.code in ("CLOSED_WITHOUT_SAR", "VERIFIED_WITHOUT_EVIDENCE", "RETIRED_INCONSISTENT")])
        req.rationale = "Not prefixed."
        rerun(project)
        hits = findings_for(project, "RETIRED_INCONSISTENT", "REQ-SYS-006")
        self.assertEqual(1, len(hits))
        self.assertIn("tag retired", hits[0].message)

    def test_retired_case_setup_prefix(self) -> None:
        project = traceability.load_project(VALID)
        project.test_cases["TC-SYS-003"].status = traceability.RETIRED
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "RETIRED_INCONSISTENT", "TC-SYS-003"))


class MatrixColumnTests(unittest.TestCase):
    """04 sections 7.1 and 7.2 columns on the valid fixture."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.project = checked_project(VALID)
        cls.report = traceability.build_report(cls.project, dt.date(2026, 9, 25))

    def row(self, req_id: str) -> list[str]:
        return traceability.verification_row(self.project, self.project.requirements[req_id])

    def test_bench_test_requirement(self) -> None:
        row = self.row("REQ-SYS-003")
        self.assertEqual("Indicated power between 4.0 W and 6.3 W at each frequency.", row[3])
        self.assertEqual("Bench", row[5])
        self.assertEqual("owner bench", row[8])
        self.assertEqual("TRR", row[9])
        self.assertEqual("owner", row[12])
        self.assertIn("docs/vv/reports/TC-SYS-002-r1.md (Pass; credit)", row[13])
        self.assertIn("NCR-001 (Closed)", row[13])
        self.assertEqual("Verified", row[14])

    def test_software_and_analysis_phases(self) -> None:
        self.assertEqual("release", self.row("REQ-SW-KEYER-001")[9])
        self.assertEqual("claude", self.row("REQ-SW-KEYER-001")[12])
        self.assertEqual("CDR", self.row("REQ-SYS-006")[9])
        self.assertEqual("TRR", self.row("REQ-SYS-004")[9], "Demonstration in Emulation is credited on the delivered unit")

    def test_acceptance_columns_follow_atp_cases(self) -> None:
        """SE HB App. D: Acceptance Requirement? and Preflight Acceptance? are separate columns (04 section 7.1)."""
        self.assertEqual(["No", "No"], self.row("REQ-SYS-003")[10:12], "no TC-ATP case")
        for setup, expected in (
            ("Article: CWHT-A-002. Configuration: c. Safety: s. Environment: e.", ["Yes", "No"]),
            ("Recurring: no. Article: CWHT-A-002. Configuration: c. Safety: s. Environment: e.", ["Yes", "No"]),
            ("Recurring: yes. Article: CWHT-A-002. Configuration: c. Safety: s. Environment: e.", ["Yes", "Yes"]),
        ):
            project = traceability.load_project(VALID)
            tc = project.test_cases["TC-SYS-002"]
            tc.module, tc.setup = traceability.ACCEPTANCE_MODULE, setup
            row = traceability.verification_row(project, project.requirements["REQ-SYS-003"])
            self.assertEqual(expected, row[10:12], setup)

    def test_report_headers(self) -> None:
        self.assertIn("| ID | Source | Shall statement | Success criteria | Method | Evidence class | Closing cases | Supporting cases | Facility | Phase | Acceptance? | Recurring acceptance? | Performer | Results | Status |", self.report)
        self.assertIn("| Validation product | Activity | Objective | Method | Facility | Phase | Performer | Requirements exercised | Results | Row status |", self.report)
        self.assertIn("### 1.2 Open TBR list", self.report)
        self.assertIn("| REQ-SYS-005 | SYS | Active |", self.report)
        self.assertIn("### 1.3 Key driving requirements", self.report)
        self.assertIn("### 7.3 Requirements tree", self.report)
        self.assertIn("  - REQ-SW-KEYER-001 [Active] Straight key debounce", self.report)
        self.assertIn("## 11. Checks performed", self.report)

    def test_validation_row(self) -> None:
        tc = self.project.test_cases["TC-VAL-001"]
        self.assertEqual(["MOE-001", "OPS-001"], tc.validation_targets)
        self.assertEqual("SAR", tc.phase)
        cases, status = self.project.validation_row("OPS-001")
        self.assertEqual(["TC-VAL-001"], [c.id for c in cases])
        self.assertEqual("Open", status)
        self.assertEqual("No case", self.project.validation_row("OPS-002")[1])
        rows = {row[0]: row for row in traceability.validation_rows(self.project)}
        self.assertEqual("on air", rows["OPS-001"][4])
        self.assertEqual("SAR", rows["OPS-001"][5])
        self.assertEqual("owner and friends", rows["OPS-001"][6])
        self.assertEqual("REQ-SYS-001", rows["OPS-001"][7])
        self.assertEqual([], [f for f in self.project.findings if f.code == "VAL_TARGET_MISSING"])

    def test_val_target_missing_when_no_target_exists(self) -> None:
        project = traceability.load_project(VALID)
        project.test_cases["TC-VAL-001"].setup = "Validates: OPS-777, OPS-001. Phase: SAR. Article: a. Configuration: b. Safety: c. Environment: d."
        traceability.run_checks(project)
        self.assertEqual([], findings_for(project, "VAL_TARGET_MISSING", "TC-VAL-001"), "one existing target names the case")
        unresolved = findings_for(project, "VAL_TARGET_UNRESOLVED", "TC-VAL-001")
        self.assertEqual(1, len(unresolved), "the mistyped target is reported, not dropped from the matrix")
        self.assertIn("OPS-777", unresolved[0].message)
        project.test_cases["TC-VAL-001"].setup = "Validates: OPS-777, MOE-777. Article: a. Configuration: b. Safety: c. Environment: d."
        rerun(project)
        self.assertEqual(1, len(findings_for(project, "VAL_TARGET_MISSING", "TC-VAL-001")))
        self.assertEqual([], findings_for(project, "VAL_TARGET_UNRESOLVED", "TC-VAL-001"), "no double report when nothing resolves")


class OutputTests(unittest.TestCase):
    """The CLI writes the Markdown report and the JSON beside it."""

    def test_json_beside_report_and_measurements(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.md"
            result = subprocess.run(
                [sys.executable, str(TOOLS / "traceability.py"), "--root", str(VALID), "--output", str(output)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            data = json.loads((Path(tmp) / traceability.DEFAULT_JSON_NAME).read_text(encoding="utf-8"))
        self.assertEqual("PASS", data["result"])
        self.assertEqual(9, data["counts"]["requirements"])
        self.assertEqual(2, data["measurements"]["MSR-04"]["all_requirements"])
        self.assertEqual(0, data["measurements"]["MSR-04"]["software_requirements"])
        self.assertEqual({"Active": 4, "Draft": 1, "Verified": 1}, data["measurements"]["MSR-01"]["by_level"]["L1"])
        self.assertEqual(1, data["measurements"]["MSR-23"]["by_class"]["HostUnit"])
        self.assertEqual(0, data["measurements"]["MSR-03"]["requirements_without_verification_case"])
        self.assertEqual({"OPS-001": "Open", "OPS-002": "No case", "MOE-001": "Open"}, data["validation_rows"])
        self.assertEqual(9, data["coverage_by_module"]["All"]["requirements"])

    def test_explicit_json_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "r.md"
            json_path = Path(tmp) / "sub" / "t.json"
            result = subprocess.run(
                [sys.executable, str(TOOLS / "traceability.py"), "--root", str(INVALID), "--output", str(output), "--json", str(json_path), "--quiet"],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(1, result.returncode)
            self.assertNotIn("WARNING", result.stdout)
            data = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertEqual("FAIL", data["result"])
        self.assertTrue(data["measurements"]["MSR-03"]["requirements_without_parent"] >= 2)
        self.assertTrue(any(f["code"] == "EXPECTATIONS_INCONSISTENT" for f in data["findings"]))


class ValidateDocsHazardsTests(unittest.TestCase):
    def test_hazards_convention(self) -> None:
        results = {validate_docs.rel(r.document, VALID): r for r in validate_docs.validate_all(VALID)}
        self.assertIn("docs/safety/hazards.json", results)
        self.assertTrue(results["docs/safety/hazards.json"].passed, results["docs/safety/hazards.json"].errors)
        self.assertEqual("docs/safety/schema.json", validate_docs.TEMPLATE_SCHEMA_ALIASES["hazards"])
        self.assertIn("hazards", {c.name for c in validate_docs.CONVENTIONS})


class CrossToolTests(unittest.TestCase):
    """Both tools agree on the fixtures (05 section 9.2 known-answer test)."""

    def run_tool(self, tool: str, root: Path) -> int:
        with tempfile.TemporaryDirectory() as tmp:
            args = [sys.executable, str(TOOLS / tool), "--root", str(root), "--quiet"]
            if tool == "traceability.py":
                args += ["--output", str(Path(tmp) / "r.md")]
            return subprocess.run(args, capture_output=True, text=True, check=False).returncode

    def test_valid_fixture_passes_both(self) -> None:
        self.assertEqual(0, self.run_tool("validate_docs.py", VALID))
        self.assertEqual(0, self.run_tool("traceability.py", VALID))

    def test_invalid_fixture_fails_both(self) -> None:
        self.assertEqual(1, self.run_tool("validate_docs.py", INVALID))
        self.assertEqual(1, self.run_tool("traceability.py", INVALID))


class RegulationPartsTests(unittest.TestCase):
    """T-07: 47CFR<part>.<section> for Parts 1, 2, 15 and 97 resolves to the corpus (02 section 3.4)."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = checked_project(VALID)

    def test_corpus_sections_loaded_for_every_part(self) -> None:
        self.assertEqual({"1.1310", "2.106", "97.7", "97.313"}, self.valid.regulations)

    def test_resolution_by_part(self) -> None:
        self.assertIs(True, traceability.resolve_source(self.valid, "47CFR1.1310"))
        self.assertIs(True, traceability.resolve_source(self.valid, "47CFR2.106(a)"), "an extract file 47cfr-2.106-<slug>.md resolves the section")
        self.assertIs(False, traceability.resolve_source(self.valid, "47CFR15.23"), "Part 15 is admitted, the section is not in this corpus")
        self.assertIsNone(traceability.resolve_source(self.valid, "47CFR73.1"), "Part 73 is not an accepted form")
        self.assertEqual(str(traceability.REGULATORY_DIR), traceability.upstream_name("47CFR1.1310"))

    def test_regulatory_tag_accepts_any_admitted_part(self) -> None:
        project = traceability.load_project(VALID)
        req = project.requirements["REQ-SYS-006"]
        req.tags = ["safety", "regulatory"]
        req.source_ids = ["SI-003", "NGO-002", "47CFR1.1310"]
        traceability.run_checks(project)
        self.assertEqual([], [f for f in project.findings if f.code in ("REGULATORY_TAG_NO_CLAUSE", "SOURCE_UNRESOLVED")])
        req.source_ids = ["SI-003", "NGO-002", "47CFR15.23"]
        rerun(project)
        self.assertTrue(findings_for(project, "SOURCE_UNRESOLVED", "REQ-SYS-006"))


class InterimRetirementTests(unittest.TestCase):
    """02 section 11.3 interim markers and the rest of T-19 on the schema-valid statuses."""

    def retire_sys_006(self) -> traceability.Project:
        project = traceability.load_project(VALID)
        req = project.requirements["REQ-SYS-006"]
        req.status, req.tags = "Closed", ["safety", "retired"]
        req.rationale = "Retired by RID-SRR-002: moved to the ME module. " + req.rationale
        tc = project.test_cases["TC-SYS-006"]
        tc.status, tc.setup = "Blocked", "Retired by RID-SRR-002: the requirement was retired. " + tc.setup
        return project

    def test_blocked_case_with_prefix_is_retired(self) -> None:
        project = self.retire_sys_006()
        self.assertTrue(project.test_cases["TC-SYS-006"].is_retired)
        traceability.run_checks(project)
        self.assertEqual([], [f for f in project.findings if f.code in ("RETIRED_INCONSISTENT", "REQ_UNVERIFIED", "CLOSED_WITHOUT_SAR", "VERIFIED_WITHOUT_EVIDENCE")])
        self.assertNotIn("TC-SYS-006", [tc.id for tc in project.live_test_cases()])

    def test_blocked_case_without_prefix_is_only_blocked(self) -> None:
        project = traceability.load_project(VALID)
        tc = project.test_cases["TC-SYS-005"]
        tc.status = "Blocked"
        self.assertFalse(tc.is_retired)
        traceability.run_checks(project)
        self.assertEqual([], [f for f in project.findings if f.code == "RETIRED_INCONSISTENT"])

    def test_live_requirement_cited_only_by_a_retired_case_is_unverified(self) -> None:
        project = traceability.load_project(VALID)
        tc = project.test_cases["TC-SYS-005"]
        tc.status, tc.setup = "Blocked", "Retired by RID-SRR-003: superseded by TC-SYS-004. " + tc.setup
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "REQ_UNVERIFIED", "REQ-SYS-005"))

    def test_retired_case_citing_a_live_requirement_names_its_successor(self) -> None:
        project = traceability.load_project(VALID)
        tc = project.test_cases["TC-SYS-005"]
        tc.status, tc.setup = "Blocked", "Retired by RID-SRR-003: procedure rewritten. " + tc.setup
        traceability.run_checks(project)
        hits = findings_for(project, "RETIRED_INCONSISTENT", "TC-SYS-005")
        self.assertEqual(1, len(hits))
        self.assertIn("REQ-SYS-005", hits[0].message)
        tc.setup = "Retired by RID-SRR-003: procedure rewritten; superseded by TC-SYS-999. Article: a."
        rerun(project)
        self.assertTrue(any("TC-SYS-999" in f.message for f in findings_for(project, "RETIRED_INCONSISTENT", "TC-SYS-005")))
        tc.setup = "Retired by RID-SRR-003: procedure rewritten; superseded by TC-SYS-001. Article: a."
        rerun(project)
        self.assertEqual([], findings_for(project, "RETIRED_INCONSISTENT", "TC-SYS-005"))

    def test_retired_tag_on_a_live_status(self) -> None:
        project = traceability.load_project(VALID)
        project.requirements["REQ-SYS-002"].tags = ["retired"]
        traceability.run_checks(project)
        hits = findings_for(project, "RETIRED_INCONSISTENT", "REQ-SYS-002")
        self.assertEqual(1, len(hits))
        self.assertIn("status Active", hits[0].message)

    def test_retired_requirement_with_tbr_is_reported_once(self) -> None:
        project = self.retire_sys_006()
        project.requirements["REQ-SYS-006"].tbr = {"owner": "Robin", "plan": "p", "close_by": "PDR"}
        project.requirements["REQ-SYS-006"].description += " (TBR)"
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "TBR_ON_FINAL_STATUS", "REQ-SYS-006"))
        self.assertEqual([], findings_for(project, "RETIRED_INCONSISTENT", "REQ-SYS-006"))


class VerifiedEvidenceTests(unittest.TestCase):
    """02 T-11 and 04 rule 7.3.4: every live closing case is Passed with a credited report."""

    def second_case(self, project: traceability.Project, status: str) -> traceability.TestCase:
        base = project.test_cases["TC-SYS-002"]
        tc = traceability.TestCase(
            id="TC-SYS-007", module="SYS", file=base.file, title="Second power case", requirement_ids=["REQ-SYS-003"],
            verification_method="Test", type="Bench", status=status, setup=base.setup, acceptance_criteria=base.acceptance_criteria,
            instruments=base.instruments, automation_ref=None, text_fields={},
        )
        project.test_cases[tc.id] = tc
        return tc

    def test_valid_verified_requirement_passes(self) -> None:
        project = checked_project(VALID)
        self.assertEqual([], findings_for(project, "VERIFIED_WITHOUT_EVIDENCE", "REQ-SYS-003"))

    def test_closing_case_not_passed(self) -> None:
        project = traceability.load_project(VALID)
        self.second_case(project, "Active")
        traceability.run_checks(project)
        hits = findings_for(project, "VERIFIED_WITHOUT_EVIDENCE", "REQ-SYS-003")
        self.assertEqual(1, len(hits))
        self.assertIn("TC-SYS-007 (Active)", hits[0].message)

    def test_passed_closing_case_without_credited_report(self) -> None:
        project = traceability.load_project(VALID)
        self.second_case(project, "Passed")
        traceability.run_checks(project)
        messages = [f.message for f in findings_for(project, "VERIFIED_WITHOUT_EVIDENCE", "REQ-SYS-003")]
        self.assertTrue(any("closing case(s) TC-SYS-007" in m for m in messages), messages)
        self.assertTrue(findings_for(project, "TC_STATUS_EVIDENCE", "TC-SYS-007"))

    def test_retired_closing_case_does_not_count(self) -> None:
        project = traceability.load_project(VALID)
        tc = self.second_case(project, "Blocked")
        tc.setup = "Retired by RID-SRR-004: duplicate of TC-SYS-002; superseded by TC-SYS-002. " + tc.setup
        traceability.run_checks(project)
        self.assertEqual([], findings_for(project, "VERIFIED_WITHOUT_EVIDENCE", "REQ-SYS-003"))


class TbdScopeTests(unittest.TestCase):
    """02 T-14: no TBD in requirement, expectation, ICD or test files."""

    def test_tbd_in_an_expectation(self) -> None:
        project = traceability.load_project(VALID)
        project.expectation_entries["MOE-001"].text_fields["success_criterion"] = "Range TBD after the antenna trade."
        traceability.run_checks(project)
        hits = findings_for(project, "TBD_PRESENT", "MOE-001")
        self.assertEqual(1, len(hits))
        self.assertIn("success_criterion", hits[0].message)

    def test_tbd_in_an_icd_table_row_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "p"
            shutil.copytree(VALID, root)
            icd = root / "docs/icd/ICD-CTL-KEY.md"
            icd.parent.mkdir(parents=True)
            icd.write_text(
                "# ICD-CTL-KEY\n\nNo TBD anywhere; an estimated value is written with (TBR).\n\n"
                "| Pin | Signal | Level |\n|---|---|---|\n| Tip | DIT | 3.3 V |\n| Ring | DAH | TBD |\n",
                encoding="utf-8",
            )
            project = checked_project(root)
        hits = [f for f in project.findings if f.code == "TBD_PRESENT"]
        self.assertEqual(["docs/icd/ICD-CTL-KEY.md:8"], [f.location for f in hits], "the prose sentence of the template is not a table row")


class ExpectationSourceTests(unittest.TestCase):
    def test_expectation_sources_resolve(self) -> None:
        project = checked_project(VALID)
        self.assertEqual([], [f for f in project.findings if f.code == "SOURCE_UNRESOLVED"])
        project = traceability.load_project(VALID)
        project.expectation_entries["CON-001"].source_ids = ["SI-999", "47CFR97.999"]
        traceability.run_checks(project)
        messages = sorted(f.message for f in findings_for(project, "SOURCE_UNRESOLVED", "CON-001"))
        self.assertEqual(2, len(messages), messages)
        self.assertTrue(all(str(traceability.EXPECTATIONS) in f.location for f in findings_for(project, "SOURCE_UNRESOLVED", "CON-001")))

    def test_absent_stakeholder_inputs_is_one_warning(self) -> None:
        project = traceability.load_project(VALID)
        project.stakeholder_inputs = None
        traceability.run_checks(project)
        hits = [f for f in project.findings if f.code == "SOURCE_FILE_MISSING" and str(traceability.STAKEHOLDER_INPUTS) in f.location]
        self.assertEqual(1, len(hits))
        self.assertIn("CON-001:SI-014", hits[0].message)
        self.assertIn("REQ-SYS-001:SI-018", hits[0].message)


class RenderTests(unittest.TestCase):
    """02 section 8.1 --render: rendered files are a pure function of their JSON and are kept current."""

    def copy(self, tmp: str) -> Path:
        root = Path(tmp) / "p"
        shutil.copytree(VALID, root)
        return root

    def test_fixture_renderings_are_current(self) -> None:
        project = checked_project(VALID)
        self.assertEqual([], [f for f in project.findings if f.code == "RENDER_STALE"])
        targets = {str(path) for path, _ in traceability.rendered_targets(project)}
        self.assertEqual(
            {"docs/requirements/l0-stakeholder/expectations.md", "docs/requirements/sys/requirements.md", "docs/requirements/sw/sw-keyer/requirements.md"},
            targets,
        )

    def test_rendering_content(self) -> None:
        project = traceability.load_project(VALID)
        expectations = traceability.render_expectations(project) or ""
        self.assertIn(traceability.RENDER_MARK, expectations.splitlines()[2])
        self.assertIn("### NGO-002 (Goal): Useful simplex range", expectations)
        self.assertIn("| NGO-003 | 5 km open-ground contact |", expectations)
        self.assertIn("| OPS-001 | Nominal QSO with a straight key | MOE-001 |", expectations)
        self.assertIn("| 47CFR97.7 | CON-001 |", expectations)
        location = "docs/requirements/sys/requirements.json"
        requirements = traceability.render_requirements(location, project.requirement_raw[location])
        self.assertIn("# Requirements: module SYS", requirements)
        self.assertIn("| REQ-SYS-004 | Debug console | Demonstration | Draft (TBR) | - |", requirements)
        self.assertIn("| TBR | owner: Robin; plan: Confirm baud rate against the rustos console driver at PDR.; close by: PDR |", requirements)
        self.assertEqual(requirements, traceability.render_requirements(location, project.requirement_raw[location]), "deterministic")

    def test_stale_absent_and_foreign_renderings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.copy(tmp)
            sys_md = root / "docs/requirements/sys/requirements.md"
            sys_md.write_text(sys_md.read_text(encoding="utf-8") + "\nHand edit.\n", encoding="utf-8")
            (root / "docs/requirements/sw/sw-keyer/requirements.md").unlink()
            (root / "docs/requirements/l0-stakeholder/expectations.md").write_text(
                "# Expectations\n\nGenerated by a renderer script (to be replaced by `tools/traceability.py --render`, process 02 section 8.1).\n", encoding="utf-8"
            )
            project = checked_project(root)
            stale = {f.location: f.message for f in project.findings if f.code == "RENDER_STALE"}
            self.assertEqual(3, len(stale), stale)
            self.assertIn("differs", stale["docs/requirements/sys/requirements.md"])
            self.assertIn("absent", stale["docs/requirements/sw/sw-keyer/requirements.md"])
            self.assertIn("not generated", stale["docs/requirements/l0-stakeholder/expectations.md"])
            result = subprocess.run(
                [sys.executable, str(TOOLS / "traceability.py"), "--root", str(root), "--output", str(Path(tmp) / "r.md"), "--render"],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertIn("rendered  docs/requirements/sys/requirements.md", result.stdout)
            self.assertEqual([], [f for f in checked_project(root).findings if f.code == "RENDER_STALE"])


class CatalogueKnownAnswerTests(unittest.TestCase):
    """One known-answer test for each catalogue code that neither fixture seeds (SWE-136; 02 section 8.1)."""

    def copy(self, tmp: str) -> Path:
        root = Path(tmp) / "p"
        shutil.copytree(VALID, root)
        return root

    def test_schema_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.copy(tmp)
            (root / "docs/requirements/schema.json").unlink()
            project = checked_project(root)
        self.assertTrue(findings_for(project, "SCHEMA_MISSING", "docs/requirements/schema.json"))

    def test_module_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.copy(tmp)
            target = root / "docs/test_cases/archive/sys/test_cases.json"
            target.parent.mkdir(parents=True)
            shutil.copy(root / "docs/test_cases/sys/test_cases.json", target)
            project = checked_project(root)
        self.assertTrue(findings_for(project, "MODULE_DUPLICATE", "docs/test_cases/sys/test_cases.json") or findings_for(project, "MODULE_DUPLICATE", "archive"))

    def test_parent_cycle(self) -> None:
        project = traceability.load_project(VALID)
        a, b = project.requirements["REQ-SW-KEYER-002"], project.requirements["REQ-SW-KEYER-003"]
        a.parent_id, b.parent_id = b.id, a.id
        a.child_ids, b.child_ids = [b.id], [a.id]
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "PARENT_CYCLE", "REQ-SW-KEYER-002"))

    def test_req_no_closing_case(self) -> None:
        project = traceability.load_project(VALID)
        project.requirements["REQ-SYS-002"].verification_method = "Inspection"
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "REQ_NO_CLOSING_CASE", "REQ-SYS-002"))

    def test_verified_with_open_ncr(self) -> None:
        project = traceability.load_project(VALID)
        project.ncrs["NCR-001"].status = "Dispositioned"
        traceability.run_checks(project)
        hits = findings_for(project, "VERIFIED_WITH_OPEN_NCR", "REQ-SYS-003")
        self.assertEqual(1, len(hits))
        self.assertIn("NCR-001", hits[0].message)

    def test_tbr_undocumented(self) -> None:
        project = traceability.load_project(VALID)
        project.requirements["REQ-SYS-001"].rationale += " Latency value is TBR."
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "TBR_UNDOCUMENTED", "REQ-SYS-001"))

    def test_report_front_matter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.copy(tmp)
            (root / "docs/vv/reports/TC-SYS-002-r2.md").write_text("# Report without front matter\n", encoding="utf-8")
            project = checked_project(root)
        self.assertTrue(findings_for(project, "REPORT_FRONT_MATTER", "TC-SYS-002-r2.md"))

    def test_hazard_file_missing(self) -> None:
        project = traceability.load_project(VALID)
        project.hazards, project.hazards_present = {}, False
        traceability.run_checks(project)
        hits = [f for f in project.findings if f.code == "HAZARD_FILE_MISSING"]
        self.assertEqual(1, len(hits))
        self.assertIn("REQ-SYS-006:HZ-002", hits[0].message)

    def test_risk_file_missing(self) -> None:
        project = traceability.load_project(VALID)
        project.risks = None
        traceability.run_checks(project)
        hits = [f for f in project.findings if f.code == "RISK_FILE_MISSING"]
        self.assertEqual(1, len(hits))
        self.assertIn("RSK-001", hits[0].message)

    def test_reports_dir_missing(self) -> None:
        project = traceability.load_project(VALID)
        project.reports, project.reports_present = [], False
        traceability.run_checks(project)
        self.assertEqual(1, len([f for f in project.findings if f.code == "REPORTS_DIR_MISSING"]))
        self.assertEqual([], findings_for(project, "VERIFIED_WITHOUT_EVIDENCE", "REQ-SYS-003"), "checked against case status only")

    def test_description_length(self) -> None:
        project = traceability.load_project(VALID)
        project.requirements["REQ-SYS-001"].description = "The radio shall key the transmitter " + "within five milliseconds " * 8 + "of closure."
        traceability.run_checks(project)
        self.assertTrue(findings_for(project, "DESCRIPTION_LENGTH", "REQ-SYS-001"))

    def test_every_catalogue_code_has_a_known_answer_test(self) -> None:
        sources = "".join(path.read_text(encoding="utf-8") for path in (TOOLS / "tests").glob("test_*.py"))
        seeded = {f.code for f in checked_project(INVALID).findings}
        untested = [code for code, _, _ in traceability.CHECK_CATALOGUE if code not in seeded and f'"{code}"' not in sources]
        self.assertEqual([], untested)


# ----------------------------------------------------------------------------
# Revision after independent review (2026-09-25): hazard trace union, SWE-052
# coverage, duplicate ids, module sets, NCR fields, baselined Markdown TBDs,
# and the validate_docs log, record and memo rules.
# ----------------------------------------------------------------------------


def copy_valid(tmp: str) -> Path:
    root = Path(tmp) / "p"
    shutil.copytree(VALID, root)
    return root


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


class HazardTraceUnionTests(unittest.TestCase):
    """04 section 3 and rule 7.3.6: the hazard trace is hazard_ids plus what hazards.json names (SWE-192, SWE-052 row 2)."""

    def test_control_req_ids_only_software_requirement_is_tested_and_traced(self) -> None:
        """The reviewer's reproduction: a SW requirement named only in hazards.json cannot skip SWE-192."""
        project = traceability.load_project(VALID)
        hazard = project.hazards["HZ-001"]
        hazard.control_req_ids = (hazard.control_req_ids or []) + ["REQ-SW-KEYER-003"]
        hazard.requirement_ids = (hazard.requirement_ids or []) + ["REQ-SW-KEYER-003"]
        project.requirements["REQ-SW-KEYER-003"].verification_method = "Inspection"
        traceability.run_checks(project)
        tested = findings_for(project, "HAZARD_REQ_NOT_TESTED", "REQ-SW-KEYER-003")
        self.assertEqual(1, len(tested))
        self.assertIn("SWE-192", tested[0].message)
        untraced = findings_for(project, "HAZARD_CONTROL_UNTRACED", "REQ-SW-KEYER-003")
        self.assertEqual(1, len(untraced))
        self.assertIn("HZ-001", untraced[0].message)
        self.assertEqual([], [f for f in project.findings if f.code == "HAZARD_INVERSE" and "REQ-SW-KEYER-003" in f.message], "the violation supersedes the warning for SW")
        report = traceability.build_report(project, dt.date(2026, 9, 25))
        self.assertIn("Result: **FAIL**", report)
        section9 = report.split("## 9. Hazard traceability")[1].split("## 10.")[0]
        row = next(line for line in section9.splitlines() if line.startswith("| HZ-001 |"))
        self.assertIn("REQ-SW-KEYER-003", row.split("|")[3], "controlling requirements column uses the union")

    def test_invalid_fixture_seeds_the_union_for_a_non_software_requirement(self) -> None:
        project = checked_project(INVALID)
        hits = findings_for(project, "HAZARD_REQ_NOT_TESTED", "REQ-SYS-005")
        self.assertEqual(1, len(hits), "REQ-SYS-005 has no hazard_ids; HZ-001 names it")
        self.assertIn("04 rule 7.3.6", hits[0].message)
        self.assertEqual([], findings_for(project, "HAZARD_CONTROL_UNTRACED", "REQ-SYS-005"), "the untraced violation is for SW modules")
        self.assertTrue(any("REQ-SYS-005" in f.message for f in findings_for(project, "HAZARD_INVERSE", "HZ-001")))

    def test_swe192_is_cited_only_for_software(self) -> None:
        project = checked_project(INVALID)
        hits = [f for f in project.findings if f.code == "HAZARD_REQ_NOT_TESTED"]
        self.assertTrue(hits)
        for finding in hits:
            if "/sw/" in finding.location:
                self.assertIn("SWE-192", finding.message)
                self.assertNotIn("04 rule 7.3.6", finding.message)
            else:
                self.assertIn("04 rule 7.3.6", finding.message, finding.location)
        rule = {code: text for code, _, text in traceability.CHECK_CATALOGUE}["HAZARD_REQ_NOT_TESTED"]
        self.assertIn("Modules SW and SW-<SUB>: SWE-192", rule)
        self.assertIn("04 rule 7.3.6 (project extension of SWE-192", rule)


class OnTargetTests(unittest.TestCase):
    """HAZARD_REQ_NOT_ON_TARGET: SWE-192 as 01 section 8.6 applies it at SAR (Bench or OnAir evidence)."""

    def test_closed_software_hazard_requirement_needs_bench_evidence(self) -> None:
        project = traceability.load_project(VALID)
        project.sar_memo_present = True
        project.requirements["REQ-SW-KEYER-001"].status = "Closed"
        traceability.run_checks(project)
        hits = findings_for(project, "HAZARD_REQ_NOT_ON_TARGET", "REQ-SW-KEYER-001")
        self.assertEqual(1, len(hits), "closed on a HostUnit case only")
        self.assertIn("Bench or OnAir", hits[0].message)
        base = project.test_cases["TC-SYS-002"]
        bench = traceability.TestCase(
            id="TC-SW-KEYER-002", module="SW-KEYER", file="docs/test_cases/sw-keyer/test_cases.json", title="Key-down limit on the delivered unit",
            requirement_ids=["REQ-SW-KEYER-001"], verification_method="Test", type="Bench", status="Passed", setup=base.setup,
            acceptance_criteria="Keying line released within the limit.", instruments=base.instruments, automation_ref=None, text_fields={},
        )
        project.test_cases[bench.id] = bench
        rerun(project)
        self.assertEqual(1, len(findings_for(project, "HAZARD_REQ_NOT_ON_TARGET", "REQ-SW-KEYER-001")), "a Passed Bench case without a credited report is not evidence")
        project.reports.append(
            traceability.Report(
                file="docs/vv/reports/TC-SW-KEYER-002-r1.md", test_case=bench.id, run="1", requirement_ids=["REQ-SW-KEYER-001"],
                validates=[], credit=True, result="Pass", date="2026-12-01", ncr_ids=[], artifacts=[],
            )
        )
        rerun(project)
        self.assertEqual([], findings_for(project, "HAZARD_REQ_NOT_ON_TARGET", "REQ-SW-KEYER-001"))

    def test_verified_on_host_is_admitted_before_sar_and_listed(self) -> None:
        """Charter section 9: HostUnit evidence makes a SW requirement Verified; the SAR check reads section 9 of the report."""
        project = traceability.load_project(VALID)
        project.requirements["REQ-SW-KEYER-001"].status = "Verified"
        traceability.run_checks(project)
        self.assertEqual([], findings_for(project, "HAZARD_REQ_NOT_ON_TARGET", "REQ-SW-KEYER-001"))
        report = traceability.build_report(project, dt.date(2026, 9, 25))
        row = next(line for line in report.split("## 9. Hazard traceability")[1].splitlines() if line.startswith("| HZ-001 |"))
        self.assertIn("REQ-SW-KEYER-001", row.split("|")[5], "not yet tested on target")


class DuplicateIdTests(unittest.TestCase):
    """ID_DUPLICATE beyond REQ, TC, NCR and L0 (charter sections 6 and 7; 02 T-03)."""

    def test_hazard_and_risk_duplicates_in_the_invalid_fixture(self) -> None:
        project = checked_project(INVALID)
        self.assertTrue(findings_for(project, "ID_DUPLICATE", "docs/safety/hazards.json HZ-001"))
        self.assertTrue(findings_for(project, "ID_DUPLICATE", "docs/risk/register.json RSK-001"))
        self.assertIn("REQ-SYS-555", project.hazards["HZ-001"].requirement_ids or [], "the first definition is kept")

    def test_ops_adr_ts_mop_and_tpm_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            conops = root / "docs/conops/conops.md"
            conops.write_text(conops.read_text(encoding="utf-8") + "\n## OPS-001 Repeated heading\n\nA second definition.\n", encoding="utf-8")
            (root / "docs/decisions/adr/ADR-001-duplicate-number.md").write_text("# ADR-001 duplicate\n", encoding="utf-8")
            studies = root / "docs/decisions/trade-studies"
            studies.mkdir(parents=True)
            (studies / "TS-001-first.md").write_text("# TS-001\n", encoding="utf-8")
            (studies / "TS-001-second.md").write_text("# TS-001 again\n", encoding="utf-8")
            tpm = json.loads((root / "docs/plan/tpm.json").read_text(encoding="utf-8"))
            tpm["mops"].append(dict(tpm["mops"][0]))
            tpm["tpms"].append(dict(tpm["tpms"][0]))
            write_json(root / "docs/plan/tpm.json", tpm)
            project = checked_project(root)
        locations = [f.location for f in project.findings if f.code == "ID_DUPLICATE"]
        for fragment in ("docs/conops/conops.md:", "docs/decisions/adr ADR-001", "docs/decisions/trade-studies TS-001", "docs/plan/tpm.json MOP-001", "docs/plan/tpm.json TPM-001"):
            self.assertTrue(any(fragment in location for location in locations), (fragment, locations))
        self.assertEqual("Nominal QSO with a straight key", project.conops_titles["OPS-001"], "the first heading is kept")


class ModuleRuleTests(unittest.TestCase):
    """MODULE_UNKNOWN (charter section 6 module sets) and the exact id prefix of T-02."""

    def test_module_sets(self) -> None:
        known = traceability.module_known
        for module in ("SYS", "RX", "TX", "PWR", "CTL", "ME", "SW", "SW-KEYER"):
            self.assertTrue(known(module, "requirements"), module)
            self.assertTrue(known(module, "test_cases"), module)
        for module in ("VAL", "ATP", "SW-COV", "SW-REG", "SW-TOOL"):
            self.assertFalse(known(module, "requirements"), module)
            self.assertTrue(known(module, "test_cases"), module)
        for module in ("VER", "FOO", "SW-"):
            self.assertFalse(known(module, "requirements"), module)
            self.assertFalse(known(module, "test_cases"), module)

    def test_unknown_modules_and_longer_module_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            keyer = json.loads((root / "docs/requirements/sw/sw-keyer/requirements.json").read_text(encoding="utf-8"))
            req = dict(keyer["requirements"][1], id="REQ-SW-KEYER-009")
            write_json(root / "docs/requirements/sw/requirements.json", {"module": "SW", "requirements": [req]})
            write_json(root / "docs/requirements/ver/requirements.json", {"module": "VER", "requirements": [dict(req, id="REQ-VER-001")]})
            cases = json.loads((root / "docs/test_cases/sw-keyer/test_cases.json").read_text(encoding="utf-8"))
            case = dict(cases["test_cases"][0], id="TC-SW-COV-001", requirement_ids=["REQ-SW-KEYER-009"])
            write_json(root / "docs/test_cases/sw/test_cases.json", {"module": "SW", "test_cases": [case]})
            write_json(root / "docs/test_cases/foo/test_cases.json", {"module": "FOO", "test_cases": [dict(case, id="TC-FOO-001")]})
            project = checked_project(root)
        unknown = {f.location for f in project.findings if f.code == "MODULE_UNKNOWN"}
        self.assertEqual({"docs/requirements/ver/requirements.json", "docs/test_cases/foo/test_cases.json"}, unknown)
        mismatch = [f for f in project.findings if f.code == "MODULE_MISMATCH"]
        self.assertTrue(any("REQ-SW-KEYER-009" in f.location and "REQ-SW-NNN" in f.message for f in mismatch), mismatch)
        self.assertTrue(any("TC-SW-COV-001" in f.location for f in mismatch), mismatch)


class SchemaFindingTests(unittest.TestCase):
    """SCHEMA_ID_PATTERN_MISSING (one severity per code) and SCHEMA_INVALID for expectations and the risk register."""

    def test_schema_without_id_pattern_is_a_warning_code_of_its_own(self) -> None:
        catalogue = {code: severity for code, severity, _ in traceability.CHECK_CATALOGUE}
        self.assertEqual(traceability.VIOLATION, catalogue["SCHEMA_MISSING"])
        self.assertEqual(traceability.WARNING, catalogue["SCHEMA_ID_PATTERN_MISSING"])
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            schema = json.loads((root / "docs/requirements/schema.json").read_text(encoding="utf-8"))
            del schema["properties"]["requirements"]["items"]["properties"]["id"]["pattern"]
            write_json(root / "docs/requirements/schema.json", schema)
            project = checked_project(root)
        self.assertEqual(["docs/requirements/schema.json"], [f.location for f in project.warnings if f.code == "SCHEMA_ID_PATTERN_MISSING"])
        self.assertEqual([], [f for f in project.findings if f.code == "SCHEMA_MISSING"])

    def test_unparsable_expectations_fails_the_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / "docs/requirements/l0-stakeholder/expectations.json").write_text("{ not json", encoding="utf-8")
            project = checked_project(root)
        hits = findings_for(project, "SCHEMA_INVALID", "expectations.json")
        self.assertEqual(1, len(hits))
        self.assertEqual(traceability.VIOLATION, hits[0].severity)
        self.assertIn("Result: **FAIL**", traceability.build_report(project))

    def test_schema_invalid_risk_register(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            write_json(root / "docs/risk/register.json", {"risks": [{"id": "RSK-001", "statement": "No likelihood or consequence."}]})
            project = checked_project(root)
        self.assertTrue(findings_for(project, "SCHEMA_INVALID", "docs/risk/register.json"))
        self.assertIn("RSK-001", project.risks or set(), "ids are still read for the Analysis exception")


class BaselinedMarkdownTbdTests(unittest.TestCase):
    """TBD_PRESENT in the ConOps and the SEMP (charter sections 3 and 7; 01 section 12.2)."""

    CONOPS = (
        "# Concept of operations (fixture)\n"          # 1
        "\n"                                          # 2
        "Prose outside the scenarios is not scanned: TBD.\n"  # 3
        "\n"                                          # 4
        "## OPS-001 Nominal QSO with a straight key\n"  # 5
        "\n"                                          # 6
        "The operator sends by hand for TBD minutes.\n"  # 7
        "\n"                                          # 8
        "## OPS-002 Nominal QSO with iambic paddles\n"  # 9
        "\n"                                          # 10
        "No TBD and TBR list applies here.\n"         # 11
        "\n"                                          # 12
        "## Glossary\n"                               # 13
        "\n"                                          # 14
        "A TBD in prose outside every scenario.\n"   # 15
        "\n"                                          # 16
        "| Term | Meaning |\n"                        # 17
        "|---|---|\n"                                 # 18
        "| Range | TBD |\n"                           # 19
    )
    SEMP = (
        "# SEMP (fixture)\n"                          # 1
        "\n"                                          # 2
        "| Measure | Target |\n"                      # 3
        "|---|---|\n"                                 # 4
        "| TPM-020 | 0 TBD or TBR at CDR |\n"         # 5
        "| Budget owner | TBD |\n"                    # 6
        "| Token rule | the `TBD` token is banned |\n"  # 7
    )

    def test_conops_scenarios_and_tables_and_semp_tables(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / "docs/conops/conops.md").write_text(self.CONOPS, encoding="utf-8")
            (root / "docs/plan/semp.md").write_text(self.SEMP, encoding="utf-8")
            project = checked_project(root)
        hits = sorted(f.location for f in project.findings if f.code == "TBD_PRESENT")
        self.assertEqual(["docs/conops/conops.md:19", "docs/conops/conops.md:7", "docs/plan/semp.md:6"], hits)

    def test_mentions_are_not_placeholders(self) -> None:
        placeholder = traceability.tbd_placeholder
        self.assertTrue(placeholder("| Range | TBD |"))
        self.assertTrue(placeholder("Wait TBD seconds, then key."))
        for mention in ("| TPM-020 | 0 TBD or TBR at CDR |", "TBD/TBR list", "TBD and TBR count", "the `TBD` token", "No TBD anywhere", "TBDs and TBRs"):
            self.assertFalse(placeholder(mention), mention)


class NcrFieldTests(unittest.TestCase):
    """NCR_FIELD_INVALID (SWE-202 levels, 04 sections 10.3 and 10.7) and NCR_NO_REQUIREMENT (SWE-052 row 6)."""

    def test_severity_status_and_classification(self) -> None:
        project = traceability.load_project(VALID)
        ncr = project.ncrs["NCR-001"]
        ncr.severity, ncr.status, ncr.classification = "Minor", "Pending", "hardware"
        traceability.run_checks(project)
        messages = [f.message for f in findings_for(project, "NCR_FIELD_INVALID", "NCR-001")]
        self.assertEqual(3, len(messages), messages)
        self.assertTrue(any("S1, S2, S3, S4" in m for m in messages))
        self.assertTrue(any("Dispositioned" in m for m in messages))
        self.assertTrue(any("product or procedure" in m for m in messages))

    def test_product_ncr_needs_a_requirement(self) -> None:
        project = traceability.load_project(VALID)
        ncr = project.ncrs["NCR-001"]
        ncr.requirement_ids, ncr.severity = [], "S2"
        traceability.run_checks(project)
        hits = findings_for(project, "NCR_NO_REQUIREMENT", "NCR-001")
        self.assertEqual(1, len(hits))
        self.assertIn("REQ-SYS-003", hits[0].message, "derived from the NCR's test case TC-SYS-002")
        ncr.severity = "S4"
        rerun(project)
        self.assertEqual([], findings_for(project, "NCR_NO_REQUIREMENT", "NCR-001"), "04 section 10.3: S4 cites a requirement only when affected")
        ncr.severity, ncr.classification = "S2", "procedure"
        rerun(project)
        self.assertEqual([], findings_for(project, "NCR_NO_REQUIREMENT", "NCR-001"), "a procedure NCR: the product conforms")


class Swe052CoverageTests(unittest.TestCase):
    """Report section 1.4: what the tool enforces of NPR 7150.2D section 3.12.1 Table 1 (charter section 7)."""

    def test_six_rows_agree_with_the_catalogue(self) -> None:
        rows = traceability.SWE052_COVERAGE
        self.assertEqual([1, 2, 3, 4, 5, 6], [r.row for r in rows])
        catalogue = {code: severity for code, severity, _ in traceability.CHECK_CATALOGUE}
        for row in rows:
            for code in row.enforced:
                self.assertIn(code, catalogue, (row.row, code))
            for code, action, gate in row.planned:
                self.assertTrue(gate, (row.row, code))
                if action == traceability.ADD:
                    self.assertNotIn(code, catalogue, f"row {row.row}: {code} exists; move it to enforced")
                else:
                    self.assertEqual(traceability.WARNING, catalogue.get(code), (row.row, code))
        states = {r.row: r.state for r in rows}
        self.assertEqual({1: "Enforced", 2: "Partial", 3: "Not enforced", 4: "Not enforced", 5: "Enforced", 6: "Enforced"}, states)

    def test_report_states_what_is_enforced(self) -> None:
        project = checked_project(VALID)
        report = traceability.build_report(project, dt.date(2026, 9, 25))
        self.assertIn("### 1.4 SWE-052 Table 1 coverage", report)
        self.assertIn("rows 1, 5, 6 enforced; row 2 enforced in part; rows 3, 4 not yet enforced", report)
        section = report.split("### 1.4 SWE-052 Table 1 coverage")[1].split("## 2. Findings")[0]
        for number in range(1, 7):
            self.assertIn(f"| {number} | ", section)
        self.assertIn("DESIGN_REF_UNRESOLVED, before PDR", section)
        self.assertIn("TAG_UNRESOLVED, before CDR", section)
        self.assertEqual(6, len(traceability.build_json(project)["swe052_coverage"]))

    def test_no_claim_of_the_full_set(self) -> None:
        for path in (TOOLS / "traceability.py", TOOLS / "README.md"):
            text = " ".join(path.read_text(encoding="utf-8").split())
            self.assertNotIn("Enforces the Class A traceability set", text, path)
            self.assertNotIn("enforces the traceability set of NPR 7150.2D", text, path)


class LogItemAndHistoryTests(unittest.TestCase):
    """validate_docs: 01 section 10.4 check 2 and the 01 section 10.3 history rules."""

    LOG = "docs/reviews/SRR/rfa-rid-log.json"

    def log_errors(self, root: Path, relative: str) -> list[str]:
        results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
        return results[relative].errors

    def test_trr_dn_log_holds_only_its_own_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            data = json.loads((root / self.LOG).read_text(encoding="utf-8"))
            item = next(i for i in data["items"] if i["id"] == "RID-SRR-003")
            item = dict(item, id="RID-TRR-D2-001", review="TRR-D2")
            write_json(root / "docs/reviews/TRR-D1/rfa-rid-log.json", dict(data, review="TRR-D1", items=[item]))
            errors = self.log_errors(root, "docs/reviews/TRR-D1/rfa-rid-log.json")
        self.assertTrue(any("items[0] RID-TRR-D2-001: review 'TRR-D2' but the log's review is 'TRR-D1'" in e for e in errors), errors)
        self.assertTrue(any("does not start with 'RID-TRR-D1-'" in e for e in errors), errors)

    def test_history_rules(self) -> None:
        def drop_close(items: list[dict]) -> None:
            items[0]["history"].pop()

        def reopen_state(items: list[dict]) -> None:
            items[0]["state"] = "Open"

        def skip_answered(items: list[dict]) -> None:
            history = items[0]["history"]
            history[1] = dict(history[1], to="Verified")
            del history[2]

        def after_closed(items: list[dict]) -> None:
            items[0]["history"].append({"date": "2026-10-06", "from": "Closed", "to": "Closed", "by": "owner", "note": "Late note."})

        def first_not_null(items: list[dict]) -> None:
            items[0]["history"][0]["from"] = "Open"

        def date_back(items: list[dict]) -> None:
            items[1]["history"][2]["date"] = "2026-10-01"

        def closed_date(items: list[dict]) -> None:
            items[0]["closed"] = "2026-10-06"

        def opened_date(items: list[dict]) -> None:
            items[0]["history"][0]["date"] = "2026-10-02"

        def broken_chain(items: list[dict]) -> None:
            items[0]["history"][2]["from"] = "Open"

        cases = (
            (drop_close, "state is 'Closed' but the history ends in 'Verified'"),
            (reopen_state, "state is 'Open' but the history ends in 'Closed'"),
            (skip_answered, "Open to Verified is not a transition"),
            (after_closed, "follows the terminal state Closed"),
            (first_not_null, "history[0] is from 'Open'"),
            (date_back, "before the previous entry"),
            (closed_date, "closed is '2026-10-06' but the history enters Closed on '2026-10-05'"),
            (opened_date, "but opened is '2026-10-03'"),
            (broken_chain, "is from 'Open' but the previous entry ends in 'Answered'"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            original = (root / self.LOG).read_text(encoding="utf-8")
            self.assertEqual([], self.log_errors(root, self.LOG), "the fixture log is consistent")
            for mutate, fragment in cases:
                data = json.loads(original)
                mutate(data["items"])
                write_json(root / self.LOG, data)
                errors = self.log_errors(root, self.LOG)
                self.assertTrue(any(fragment in e for e in errors), (mutate.__name__, errors))

    def test_review_trend_fixture_log_obeys_the_rules(self) -> None:
        """The fixture copy of docs/templates/rfa-rid-log.example.json (01 section 11 known answers)."""
        path = FIXTURES / "review_trend/docs/reviews/SRR/rfa-rid-log.json"
        result = validate_docs.FileResult("rfa_rid_log", path, path)
        validate_docs.check_rfa_rid_log(result, FIXTURES / "review_trend", template=True)
        self.assertEqual([], result.errors)


class PeerReviewRecordRuleTests(unittest.TestCase):
    """validate_docs: SWE-088 b, c, d and SWE-089 content of the single peer-review record (01 section 13)."""

    BASE = {
        "id": "INSP-009", "checklist": "peer-review-checklist-requirements", "product": "docs/requirements/sys/requirements.json",
        "product_commit": "3f2a9c1", "author_agent": "author-1", "reviewer_agent": "reviewer-1", "iteration": 1, "readiness_met": True,
        "verdict": "APPROVED", "findings_major": 0, "findings_minor": 0, "findings_fixed": 0, "findings_deferred": 0,
        "effort_turns": 3, "effort_minutes": 20, "date": "2026-10-04",
    }

    def record_errors(self, fields: dict, body: str = "", name: str = "requirements-extra.md") -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            front = "\n".join(f"{key}: {yaml_value(key, value)}" for key, value in fields.items())
            path = root / "docs/reviews/SRR/checklists" / name
            path.write_text(f"---\n{front}\n---\n\n# Record\n\n{body}\n", encoding="utf-8")
            results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
            return results[f"docs/reviews/SRR/checklists/{name}"].errors

    def test_complete_record_passes(self) -> None:
        self.assertEqual([], self.record_errors(self.BASE))

    def test_swe089_fields_are_required_and_counts_are_non_negative(self) -> None:
        errors = relative_errors(INVALID, "docs/reviews/SRR/checklists/requirements-sys.md")
        for name in ("findings_major", "findings_minor", "findings_fixed", "findings_deferred", "effort_turns", "effort_minutes", "iteration", "author_agent", "reviewer_agent", "readiness_met", "date"):
            self.assertTrue(any(f"'{name}' is a required property" in e for e in errors), (name, errors))
        errors = self.record_errors(dict(self.BASE, findings_minor=-1))
        self.assertTrue(any("findings_minor: -1 is less than the minimum of 0" in e for e in errors), errors)

    def test_hyphenated_checklist_stem_is_accepted(self) -> None:
        """08 section 3.5: peer-review-checklist-visual-product and -software-assurance are valid stems."""
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / "docs/templates/peer-review-checklist-visual-product.md").write_text("# template\n", encoding="utf-8")
            record = dict(self.BASE, checklist="peer-review-checklist-visual-product")
            front = "\n".join(f"{key}: {yaml_value(key, value)}" for key, value in record.items())
            path = root / "docs/reviews/SRR/checklists/visual-product-srr-deck.md"
            path.write_text(f"---\n{front}\n---\n\n# Record\n", encoding="utf-8")
            results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
            self.assertEqual([], results["docs/reviews/SRR/checklists/visual-product-srr-deck.md"].errors)
        for bad in ("peer-review-checklist-visual-", "peer-review-checklist--visual", "peer-review-checklist-Visual", "peer-review-checklist-visual_product"):
            errors = self.record_errors(dict(self.BASE, checklist=bad))
            self.assertTrue(any("does not match" in e for e in errors), (bad, errors))

    def test_reviewer_is_not_the_author(self) -> None:
        errors = self.record_errors(dict(self.BASE, reviewer_agent="author-1"))
        self.assertTrue(any("is also the author_agent" in e for e in errors), errors)

    def test_assurance_reviewer_for_critical_modules(self) -> None:
        keyer = dict(self.BASE, product="docs/requirements/sw/sw-keyer/requirements.json")
        errors = self.record_errors(keyer, name="requirements-sw-keyer.md")
        self.assertTrue(any("SW-KEYER" in e and "required participant" in e for e in errors), errors)
        errors = self.record_errors(dict(keyer, assurance_reviewer_agent="author-1"), name="requirements-sw-keyer.md")
        self.assertTrue(any("distinct invocation" in e for e in errors), errors)
        self.assertEqual([], self.record_errors(dict(keyer, assurance_reviewer_agent="assurance-1"), name="requirements-sw-keyer.md"))
        self.assertEqual("SW-KEYER", validate_docs.critical_module("firmware/cwht-core/src/keyer/iambic.rs", "code-keyer-iambic"))
        self.assertEqual("SW-CFG", validate_docs.critical_module("docs/test_cases/sw-cfg/test_cases.json", "test-sw-cfg"))
        self.assertIsNone(validate_docs.critical_module("docs/requirements/sw/sw-diag/requirements.json", "requirements-sw-diag"))
        self.assertIsNotNone(validate_docs.assurance_reason("docs/process/07-software-engineering-plan.md", "plan-07-software-engineering-plan"))

    def test_approved_needs_readiness_and_no_open_major_finding(self) -> None:
        errors = self.record_errors(self.BASE, body="| Finding | Severity | State |\n|---|---|---|\n| finding-1 | Major | Open |\n")
        self.assertTrue(any("finding-1 is a Major finding in state Open" in e for e in errors), errors)
        self.assertEqual([], self.record_errors(self.BASE, body="| finding-1 | Major | Verified |\n| finding-2 | Minor | Open |\n"))
        self.assertEqual([], self.record_errors(dict(self.BASE, verdict="NEEDS CHANGES"), body="| finding-1 | Major | Open |\n"))
        errors = self.record_errors(dict(self.BASE, readiness_met=False))
        self.assertTrue(any("readiness_met is not true" in e for e in errors), errors)

    def test_verifying_record_reviews_the_item_product(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            record = root / "docs/reviews/SRR/checklists/requirements-sys.md"
            record.write_text(record.read_text(encoding="utf-8").replace("product: docs/requirements/sys/requirements.json", "product: docs/requirements/rx/requirements.json"), encoding="utf-8")
            results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
        errors = results["docs/reviews/SRR/rfa-rid-log.json"].errors
        self.assertTrue(any("reviews 'docs/requirements/rx/requirements.json', not the item's product" in e for e in errors), errors)


def yaml_value(key: str, value: object) -> str:
    """Front matter scalar as a reviewer writes it: booleans lower case, product_commit quoted."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if key == "product_commit":
        return json.dumps(value)
    return str(value)


def relative_errors(root: Path, relative: str) -> list[str]:
    results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
    return results[relative].errors


class DecisionMemoAndFolderTests(unittest.TestCase):
    """validate_docs: decision memo front matter (01 sections 11, 12.1, 12.2) and review folder tokens."""

    def memo(self, root: Path, folder: str, front: str) -> None:
        path = root / "docs/reviews" / folder / "decision-memo.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\n{front}\n---\n\n# Memo\n", encoding="utf-8")

    def test_fixture_memo_passes(self) -> None:
        memo = FIXTURES / "review_trend/docs/reviews/SRR/decision-memo.md"
        self.assertEqual([], validate_docs.validate_decision_memo(memo, FIXTURES / "review_trend").errors)

    def test_memo_rules(self) -> None:
        cases = {
            "SRR": ("review: PDR\ndisposition: null\nsigned: null", "the memo names its own review"),
            "PDR": ("review: PDR\ndisposition: Approved\nsigned: null", "both are set by the approving session"),
            "CDR": ("review: CDR\ndisposition: Approved\nsigned: 2026-12-01\nrevoked: 2026-11-30", "earlier than signed"),
            "TRR": ("review: TRR\ndisposition: Approved\nsigned: 2027-01-10\nbaseline_tag: baseline/trr", "sets no baseline"),
            "SAR": ("review: SAR\ndisposition: Not approved\nsigned: null", "is not one of"),
            "QDR": ("review: SRR\ndisposition: null\nsigned: null", "'QDR' is not a review token"),
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            for folder, (front, _) in cases.items():
                self.memo(root, folder, front)
            results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
        for folder, (_, fragment) in cases.items():
            errors = results[f"docs/reviews/{folder}/decision-memo.md"].errors
            self.assertTrue(any(fragment in e for e in errors), (folder, errors))
        self.assertNotIn("docs/reviews/QDR", results, "the memo already reports the folder")

    def test_folder_without_log_record_or_memo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            (root / "docs/reviews/QDR").mkdir()
            (root / "docs/reviews/QDR/package.md").write_text("# Package\n", encoding="utf-8")
            (root / "docs/reviews/.cache").mkdir()
            results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
        self.assertIn("holds only review folders", results["docs/reviews/QDR"].errors[0])
        self.assertNotIn("docs/reviews/.cache", results)


class NewConventionTests(unittest.TestCase):
    """validate_docs: tpm.json, the compliance matrix, measurements.json and allocation.json (SEMP section 4.3)."""

    def test_conventions_and_missing_schemas(self) -> None:
        names = {c.name for c in validate_docs.CONVENTIONS}
        self.assertTrue({"tpm", "se_compliance_matrix", "measurements", "allocation"} <= names)
        valid = {validate_docs.rel(r.document, VALID): r for r in validate_docs.validate_all(VALID)}
        self.assertTrue(valid["docs/plan/tpm.json"].passed, valid["docs/plan/tpm.json"].errors)
        with tempfile.TemporaryDirectory() as tmp:
            root = copy_valid(tmp)
            write_json(root / "docs/plan/measurements.json", {"schema": "cwht-measurements-1", "records": []})
            write_json(root / "docs/design/allocation.json", {"elements": []})
            write_json(root / "docs/process/se-compliance-matrix.json", {"rows": []})
            results = {validate_docs.rel(r.document, root): r for r in validate_docs.validate_all(root)}
        for path in ("docs/plan/measurements.json", "docs/design/allocation.json", "docs/process/se-compliance-matrix.json"):
            self.assertTrue(results[path].errors and results[path].errors[0].startswith("schema not found"), (path, results[path].errors))


def without_descriptions(node: object) -> object:
    if isinstance(node, dict):
        return {k: without_descriptions(v) for k, v in node.items() if k != "description"}
    if isinstance(node, list):
        return [without_descriptions(v) for v in node]
    return node


class SchemaTripwireTests(unittest.TestCase):
    """Fixture schema copies carry the repository constraints (a schema change re-validates the fixtures, 05 Table 4-1 row 9)."""

    def assert_same_constraints(self, repository: str, fixtures: tuple[str, ...]) -> None:
        expected = without_descriptions(json.loads((traceability.REPO_ROOT / repository).read_text(encoding="utf-8")))
        for fixture in fixtures:
            actual = without_descriptions(json.loads((FIXTURES / fixture / repository).read_text(encoding="utf-8")))
            self.assertEqual(expected, actual, f"re-copy {repository} into tools/tests/fixtures/{fixture} and re-run the suite")

    def test_rfa_rid_log_schema(self) -> None:
        self.assert_same_constraints("docs/templates/rfa-rid-log.schema.json", ("valid_project", "invalid_project", "review_trend"))

    def test_tpm_schema(self) -> None:
        self.assert_same_constraints("docs/plan/tpm.schema.json", ("valid_project", "invalid_project"))


if __name__ == "__main__":
    unittest.main()
