#!/usr/bin/env python3
"""Bidirectional traceability checker and report generator for cwht.

Loads every requirement file, the stakeholder inputs and expectations, the
ConOps scenarios, the test cases, the hazards, the measures, the verification
reports and the nonconformance reports. Of the six Class A rows of NPR 7150.2D
section 3.12.1 Table 1 (SWE-052) that docs/process/00-charter.md section 7
adopts, it enforces rows 1 (higher-level to software requirements), 5
(requirements to verifications) and 6 (requirements to nonconformances), row 2
(requirements to hazards) in part, and not yet rows 3 (requirements to design
components) and 4 (design components to code); SWE052_COVERAGE below, printed
as report section 1.4, states the codes enforced and planned per row with
their gates (docs/process/03-software-classification-and-rmm.md section 8).
It also applies the requirement-side rules of
docs/process/02-requirements-and-traceability.md section 8.2 and the
evidence-side rules of docs/process/04-verification-and-validation.md
section 7.3 as far as CHECK_CATALOGUE lists them, including the two rules due
before SRR at their plain-run severity Warning: T-21 STAKEHOLDERS_MISSING (the
stakeholders array of expectations.json) and T-18 SYS_UNALLOCATED (every Draft
or Active SYS requirement names a receiving L2 module through child_ids or the
preliminary docs/design/allocation.json), and writes
docs/vv/traceability-report.md containing a
Requirements Verification Matrix (SE HB Appendix D, Table D-1) and a
Validation Matrix (SE HB Appendix E, Table E-1), plus the machine-readable
docs/vv/traceability.json with the MSR-01, MSR-03, MSR-04 and MSR-23
measurements of docs/process/07-software-engineering-plan.md section 11.

Findings have two severities:

    VIOLATION  a traceability or writing-rule defect; exit status 1 unless
               --report-only is given
    WARNING    an item that cannot be checked yet (missing upstream file), a
               rule whose plain-run severity is W in 02 section 8.2, or a
               quality hint; never changes the exit status

Retirement uses the interim markers of 02 section 11.3 until a schema CR adds
a Retired status: a requirement with status Closed and tag retired, a test
case with status Blocked whose setup begins 'Retired by '. With --render the
tool first writes expectations.md beside expectations.json and requirements.md
beside every requirements.json (02 section 8.1); RENDER_STALE warns when a
rendered file is absent, hand-made or out of date.

The check catalogue is printed at the end of the report and, with
tools/README.md "Rule coverage", is the statement of what the tool enforces;
docs/process/02-requirements-and-traceability.md section 8.5,
docs/process/03-software-classification-and-rmm.md section 8 and
docs/process/04-verification-and-validation.md section 7.4 bind the codes to
their rules. The tool is not yet accredited (SWE-136; TV record due SRR per
tools/toolchain.lock.md section 1.2), so its output is developer evidence only
until the TV record exists. The unit tests in tools/tests/ run this tool on the
seeded fixtures under tools/tests/fixtures/ (SWE-136 known-answer test):

    .venv/bin/python -m unittest discover -s tools/tests

Usage:
    .venv/bin/python tools/traceability.py [--root PATH] [--output PATH] [--json PATH] [--report-only] [--quiet] [--render]
    .venv/bin/python tools/traceability.py --regression DESIGN_REF [DESIGN_REF ...]
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_docs  # noqa: E402

yaml = validate_docs.yaml  # PyYAML when installed (tools/requirements.txt); None selects the subset parser

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = Path("docs/vv/traceability-report.md")
DEFAULT_JSON_NAME = "traceability.json"

# Repository artifacts consumed (relative to root; charter section 5).
REQ_SCHEMA = Path("docs/requirements/schema.json")
TC_SCHEMA = Path("docs/test_cases/schema.json")
EXPECTATIONS_SCHEMA = Path("docs/requirements/l0-stakeholder/schema.json")
HAZARDS_SCHEMA = Path("docs/safety/schema.json")
RISKS_SCHEMA = Path("docs/risk/schema.json")
REQUIREMENTS_GLOB = "docs/requirements/**/requirements.json"
TEST_CASES_GLOB = "docs/test_cases/**/test_cases.json"
STAKEHOLDER_INPUTS = Path("docs/requirements/l0-stakeholder/stakeholder-inputs.md")
EXPECTATIONS = Path("docs/requirements/l0-stakeholder/expectations.json")
CONOPS = Path("docs/conops/conops.md")
HAZARDS = Path("docs/safety/hazards.json")
RISKS = Path("docs/risk/register.json")
MEASURES = Path("docs/plan/tpm.json")
REGULATORY_DIR = Path("docs/references/md/regulatory")
NCR_DIR = Path("docs/vv/ncr")
REPORTS_DIR = Path("docs/vv/reports")
ADR_DIR = Path("docs/decisions/adr")
TRADE_STUDY_DIR = Path("docs/decisions/trade-studies")
SAR_DECISION_MEMO = Path("docs/reviews/SAR/decision-memo.md")
ALLOCATION = Path("docs/design/allocation.json")  # preliminary at SRR (02 section 2.3, T-18), baselined at PDR
SEMP = Path("docs/plan/semp.md")
ICD_GLOB = "docs/icd/ICD-*.md"
EXPECTATION_TEXT_FIELDS = ("title", "statement", "rationale", "success_criterion")

# Identifier schemes (charter section 6). Requirement and test case patterns are
# read from the schemas at run time; these are the fallbacks if a schema is absent.
DEFAULT_REQ_ID_PATTERN = r"^REQ-[A-Z][A-Z0-9]*(-[A-Z][A-Z0-9]*)*-[0-9]{3}$"
DEFAULT_TC_ID_PATTERN = r"^TC-[A-Z][A-Z0-9]*(-[A-Z][A-Z0-9]*)*-[0-9]{3}$"
SI_ID = re.compile(r"^SI-[0-9]{3}$")
NGO_ID = re.compile(r"^NGO-[0-9]{3}$")
MOE_ID = re.compile(r"^MOE-[0-9]{3}$")
CON_ID = re.compile(r"^CON-[0-9]{3}$")
OPS_ID = re.compile(r"^OPS-[0-9]{3}$")
ADR_ID = re.compile(r"^ADR-[0-9]{3}$")
TS_ID = re.compile(r"^TS-[0-9]{3}$")
HZ_ID = re.compile(r"^HZ-[0-9]{3}$")
RSK_ID = re.compile(r"^RSK-[0-9]{3}$")
NCR_ID = re.compile(r"^NCR-[0-9]{3}$")
MOP_ID = re.compile(r"^MOP-[0-9]{3}$")
TPM_ID = re.compile(r"^TPM-[0-9]{3}$")
ICD_ID = re.compile(r"^ICD-[A-Z][A-Z0-9]*-[A-Z][A-Z0-9]*$")
L0_SOURCE_ID = re.compile(r"^(NGO|MOE|CON|OPS)-[0-9]{3}$")
DECISION_SOURCE_ID = re.compile(r"^(ADR|TS)-[0-9]{3}$")
# 47 CFR clause of Part 1, 2, 15 or 97 (charter section 1; 02 section 3.4), e.g. 47CFR97.307(e)
# or 47CFR1.1310; group 1 is <part>.<section>, the key of the corpus file. A corpus file
# 47cfr-<part>.<section>.md, or an extract 47cfr-<part>.<section>-<slug>.md such as
# 47cfr-2.106-harmonic-bands.md, resolves the section.
REGULATION_PARTS = ("1", "2", "15", "97")
REGULATION_ID = re.compile(r"^47CFR((?:1|2|15|97)\.[0-9]+)(\([a-z0-9]+\))*$")
REGULATION_FILE = re.compile(r"^47cfr-((?:1|2|15|97)\.[0-9]+)(?:-[a-z0-9-]+)?\.md$")
SI_ROW = re.compile(r"^\|\s*(SI-[0-9]{3})\s*\|.*$", re.MULTILINE)
OPS_HEADING = re.compile(r"^#{1,6}\s+(OPS-[0-9]{3})\b", re.MULTILINE)
OPS_TITLE = re.compile(r"^#{1,6}\s+(OPS-[0-9]{3})\b[ \t:.-]*(.*)$", re.MULTILINE)
VALIDATION_TARGET = re.compile(r"\b(?:OPS|MOE)-[0-9]{3}\b")  # non-capturing: findall must return whole ids
VALIDATES_CLAUSE = re.compile(r"Validates:\s*([^.;\n]*)")
PHASE_CLAUSE = re.compile(r"Phase:\s*(SRR|PDR|CDR|TRR(?:-D[0-9]+)?|SAR|Ops)\b")
REPORT_FILE = re.compile(r"^(TC-[A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-[0-9]{3})-r([0-9]+)\.md$")
VALIDATION_MODULE = "VAL"
ACCEPTANCE_MODULE = "ATP"
# 04 section 7.1 "Recurring acceptance?" (SE HB App. D "Preflight Acceptance?"): a TC-ATP case
# repeated at every pre-operation or recurring acceptance of a unit carries 'Recurring: yes' in setup.
RECURRING_CLAUSE = re.compile(r"\bRecurring:\s*(yes|no)\b", re.IGNORECASE)

# Charter section 6 module sets. Requirement modules: SYS, RX, TX, PWR, CTL, ME and SW-<SUB>
# (plain SW is admitted too: charter sections 5 and 7 list docs/requirements/sw/requirements.json;
# the owner's decision on it is a charter issue); VER is reserved and unused. Test-only modules
# (04 section 1): VAL, ATP, SW-COV, SW-REG, SW-TOOL.
REQUIREMENT_MODULES = ("SYS", "RX", "TX", "PWR", "CTL", "ME", "SW")
L2_MODULES = tuple(m for m in REQUIREMENT_MODULES if m != "SYS")  # plus SW-<SUB> (is_l2_module)
TEST_ONLY_MODULES = ("VAL", "ATP", "SW-COV", "SW-REG", "SW-TOOL")
SW_SUB_MODULE = re.compile(r"^SW-[A-Z][A-Z0-9]*$")

TBD_WORD = re.compile(r"\bTBD\b")
# A Markdown product may name the policy terms without holding a placeholder: "TBD and TBR",
# "TBD/TBR", "`TBD`", "no TBD". These mentions are removed before TBD_WORD is applied to
# ICD, ConOps and SEMP lines; JSON text fields get no exemption.
TBD_MENTION = re.compile(r"`TBD`|\bTBDs?\s*(?:/|,|\band\b|\bor\b)\s*TBRs?\b|\bTBRs?\s*(?:/|,|\band\b|\bor\b)\s*TBDs?\b|\b[Nn]o TBDs?\b")
TBR_WORD = re.compile(r"\bTBR\b")
TBR_MARK = "(TBR)"
SHALL_WORD = re.compile(r"\bshall\b", re.IGNORECASE)
SELF_DERIVED = re.compile(r"self-derived", re.IGNORECASE)
SELF_DERIVED_PREFIX = "Self-derived:"
RETIRED_PREFIX = "Retired by "
HAZARD_ANALYSIS_NOTE = re.compile(r"^Analysis accepted per (RSK-[0-9]{3})")
SOFTWARE_MODULE = re.compile(r"^SW(-[A-Z][A-Z0-9]*)*$")
RETIRED = "Retired"
RETIRED_TAG = "retired"  # charter section 6: status Closed plus tag retired until the schemas carry Retired
BLOCKED = "Blocked"  # 02 section 11.3: a test case is retired by status Blocked plus setup starting 'Retired by '
SUPERSEDED_BY_CASE = re.compile(r"\bsuperseded by (TC-[A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-[0-9]{3})\b")
TBR_FINAL_STATUSES = ("Verified", "Closed", RETIRED)
EVIDENCE_STATUSES = ("Verified", "Closed")
ACTIVE_OR_LATER = ("Active", "Verified", "Closed")
TAG_SAFETY = "safety"
TAG_REGULATORY = "regulatory"
TAG_INTERFACE = "interface"
# 02 section 3.0 and T-21: the stakeholders array holds at least one entry of each of these roles.
REQUIRED_STAKEHOLDER_ROLES = ("customer", "user", "regulator")
EXPECTATION_STATUS_BASELINED = "Baselined"
NGO_KINDS = ("Need", "Goal", "Objective")


def _word_list_pattern(words: Iterable[str]) -> re.Pattern[str]:
    """Whole-word, case-insensitive alternation with the WR-07 boundary (?<![\\w-])word(?![\\w-])."""
    alternation = "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))
    return re.compile(rf"(?<![\w-])(?:{alternation})(?![\w-])", re.IGNORECASE)


# docs/process/02-requirements-and-traceability.md section 4.2 rule WR-07: the single
# banned-word list of the project, copied verbatim (rule T-17). Group A: modal verbs
# other than shall (violation MODAL_IN_DESCRIPTION). Group B: unverifiable or ambiguous
# words (warning UNVERIFIABLE_WORD in a plain run).
WR07_GROUP_A = ("will", "should", "must", "may", "can", "might")
WR07_GROUP_B = (
    "flexible", "easy", "easily", "sufficient", "safe", "ad hoc", "adequate", "adequately",
    "accommodate", "user-friendly", "usable", "when required", "if required", "as required",
    "if possible", "to the extent practicable", "appropriate", "as appropriate", "approximately",
    "fast", "portable", "light-weight", "small", "large", "maximize", "minimize", "robust",
    "quickly", "clearly", "etc.", "and/or", "but not limited to", "support", "TBD",
)
MODAL_WORDS = _word_list_pattern(WR07_GROUP_A)
UNVERIFIABLE_WORDS = _word_list_pattern(WR07_GROUP_B)
MAX_DESCRIPTION_WORDS = 25
ARTIFACT_STRING = re.compile(r"^(?P<path>\S+)\s+sha256=(?P<sha256>[0-9a-fA-F]{64})$")
BENCH_SETUP_LINES = ("Article:", "Configuration:", "Safety:", "Environment:")
BENCH_TYPES = ("Bench", "OnAir")

# 02 section 4.4: evidence classes (test case type) admitted for each verification method.
TYPES_FOR_METHOD: dict[str, tuple[str, ...]] = {
    "Test": ("HostUnit", "Emulation", "Bench"),
    "Demonstration": ("Emulation", "Bench", "OnAir"),
    "Analysis": ("Simulation",),
    "Inspection": ("Inspection",),
}
# 04 section 7.1: facility derived from the evidence class.
FACILITY_FOR_TYPE: dict[str, str] = {
    "Bench": "owner bench",
    "HostUnit": "host",
    "Emulation": "emulator",
    "Simulation": "simulation",
    "OnAir": "on air",
    "Inspection": "inspection",
}
OWNER_PERFORMED_TYPES = ("Bench", "OnAir")

REQ_STATUSES_NEEDING_TC = ("Draft", "Active")
L1_MODULE = "SYS"
TBR_CLOSE_BY_L1 = ("SRR", "PDR")  # charter section 7: all L1 TBRs close by PDR
TBR_CLOSE_BY_L2 = ("SRR", "PDR", "CDR")  # all L2 TBRs close by CDR
NCR_CLOSED = "Closed"
NCR_SEVERITIES = ("S1", "S2", "S3", "S4")  # 04 section 10.3 (SWE-202 severity levels)
NCR_STATUSES = ("Open", "Analysis", "Dispositioned", "Retest", "Closed")  # 04 section 10.7
NCR_CLASSIFICATIONS = ("product", "procedure")  # docs/templates/ncr.md
NCR_NO_REQUIREMENT_SEVERITY = "S4"  # 04 section 10.3: an S4 NCR cites a requirement only when the defect affects it
ON_TARGET_TYPES = ("Bench", "OnAir")  # 01 section 8.6 SWE-192: tested on the target

VIOLATION = "VIOLATION"
WARNING = "WARNING"

CHECK_CATALOGUE: tuple[tuple[str, str, str], ...] = (
    ("SCHEMA_MISSING", VIOLATION, "docs/requirements/schema.json or docs/test_cases/schema.json is absent"),
    ("SCHEMA_ID_PATTERN_MISSING", WARNING, "docs/requirements/schema.json or docs/test_cases/schema.json exists but defines no id pattern, so the fallback pattern of charter section 6 is used"),
    ("SCHEMA_INVALID", VIOLATION, "a requirements, expectations, test case, hazards or risk register file (docs/risk/register.json against docs/risk/schema.json) fails its JSON Schema or is not valid JSON (same check as validate_docs.py; 02 T-01)"),
    ("ID_FORMAT", VIOLATION, "requirement or test case id does not match the id pattern of its schema"),
    ("ID_DUPLICATE", VIOLATION, "an id is defined more than once: REQ, TC and NCR across all files; NGO, MOE and CON within expectations.json; HZ within hazards.json; RSK within register.json; MOP and TPM within tpm.json; an OPS-NNN heading repeated in conops.md; two ADR-NNN or two TS-NNN files with the same number. The first definition is kept (charter sections 6 and 7: ids are never reused and are unique; 02 T-03)"),
    ("MODULE_MISMATCH", VIOLATION, "module field differs from the directory name, or an id is not exactly <REQ|TC>-<module>-NNN for the file's module (V&V 7.3 rule 1; 02 T-02)"),
    ("MODULE_UNKNOWN", VIOLATION, "a requirements file declares a module outside SYS, RX, TX, PWR, CTL, ME, SW and SW-<SUB> (SW-COV, SW-REG and SW-TOOL are test-only; VER is reserved and unused), or a test case file declares a module outside those and VAL, ATP, SW-COV, SW-REG, SW-TOOL (charter section 6; 04 section 1)"),
    ("MODULE_DUPLICATE", VIOLATION, "two files of the same kind declare the same module"),
    ("RATIONALE_EMPTY", VIOLATION, "rationale is empty (charter section 7: rationale mandatory)"),
    ("L1_PARENT_NOT_NULL", VIOLATION, "a SYS requirement has a non-null parent_id (02 section 2.3, T-05: L1 traces to L0 through source_ids)"),
    ("PARENT_UNRESOLVED", VIOLATION, "parent_id names a requirement that does not exist, or the requirement itself"),
    ("PARENT_MISSING", VIOLATION, "an L2 requirement has parent_id null and its rationale does not say self-derived (SE HB 6.2.1.2.3; 02 T-05)"),
    ("SELF_DERIVED_UNSUPPORTED", VIOLATION, "an L2 requirement with parent_id null says self-derived but the rationale does not begin 'Self-derived:', or it has neither an ADR-/TS- source id nor a hazard id (02 section 2.3, T-05)"),
    ("PARENT_CYCLE", VIOLATION, "the parent chain loops"),
    ("CHILD_INVERSE", VIOLATION, "child_ids is not the exact inverse of parent_id (02 T-06)"),
    ("CHILD_AHEAD_OF_PARENT", VIOLATION, "a requirement with status Active, Verified or Closed has a parent with status Draft (02 T-11)"),
    ("SOURCE_UNRESOLVED", VIOLATION, "a source id of a requirement (SI, NGO, MOE, CON, OPS, ADR, TS, 47 CFR Part 1, 2, 15 or 97 clause) or of an expectations.json entry (SI, 47 CFR clause) does not exist in its upstream artifact (02 section 3.4, T-07)"),
    ("SOURCE_L0_MISSING", VIOLATION, "a SYS requirement has no source id or, while expectations.json exists, no NGO-, MOE-, CON- or OPS- source id (02 section 2.3, T-07)"),
    ("SAFETY_TAG_NO_HAZARD", VIOLATION, "a requirement tagged safety has an empty hazard_ids (02 section 2.3, T-08)"),
    ("REGULATORY_TAG_NO_CLAUSE", VIOLATION, "a requirement tagged regulatory cites no 47 CFR clause (Part 1, 2, 15 or 97) in source_ids (02 section 2.3)"),
    ("HAZARD_ID_FORMAT", VIOLATION, "a hazard id does not match HZ-NNN"),
    ("HAZARD_UNRESOLVED", VIOLATION, "a hazard id is not defined in docs/safety/hazards.json, or hazards.json names a requirement (requirement_ids or a control's control_req_ids) that does not exist"),
    ("HAZARD_REQ_NOT_TESTED", VIOLATION, "a hazard-tracing requirement (its own hazard_ids, or named by a hazard's requirement_ids or a control's control_req_ids in docs/safety/hazards.json; 04 section 3) has no closing case of method Test. Modules SW and SW-<SUB>: SWE-192, no exception. Other modules: 04 rule 7.3.6 (project extension of SWE-192 to every hazard-control requirement), which also accepts method Analysis with a verification_note beginning 'Analysis accepted per RSK-NNN' naming a risk in docs/risk/register.json"),
    ("HAZARD_CONTROL_UNTRACED", VIOLATION, "a requirement of module SW or SW-<SUB> is named by a hazard of docs/safety/hazards.json (requirement_ids or a control's control_req_ids) but its hazard_ids does not list that hazard (SWE-052 Table 1 row 2 is bidirectional; 02 section 2.3 tag obligations)"),
    ("HAZARD_REQ_NOT_ON_TARGET", VIOLATION, "a hazard-tracing requirement of module SW or SW-<SUB> has status Closed but no Passed closing case of type Bench or OnAir with a credited report citing it (SWE-192 as 01 section 8.6 applies it at SAR: verified through test on the target; Closed is reached only at SAR, charter section 9)"),
    ("REQ_UNVERIFIED", VIOLATION, "a Draft or Active requirement has no test case citing it (orphan requirement; 02 T-09)"),
    ("REQ_NO_CLOSING_CASE", VIOLATION, "a requirement has test cases but none with the same verification_method (V&V 7.3 rule 2)"),
    ("VERIFIED_WITHOUT_EVIDENCE", VIOLATION, "a Verified or Closed requirement has a live closing case that is not Passed (or none), is cited by a Failed case, or has a Passed closing case without a report with credit true and result Pass citing it (V&V 7.3 rule 4; 02 T-11)"),
    ("VERIFIED_WITH_OPEN_NCR", VIOLATION, "a Verified or Closed requirement is cited by an NCR whose status is not Closed (V&V 7.3 rule 4)"),
    ("CLOSED_WITHOUT_SAR", VIOLATION, "a Closed requirement exists while docs/reviews/SAR/decision-memo.md is absent, or a validation row that depends on it is not Validated (04 section 5.3; 02 T-11)"),
    ("RETIRED_INCONSISTENT", VIOLATION, "a retired requirement (status Retired, or status Closed with tag retired until the schema carries Retired, charter section 6) has a child or a citing test case that is not retired or a rationale that does not begin 'Retired by ' (its tbr object is reported as TBR_ON_FINAL_STATUS); the tag retired sits on a status other than Closed; or a retired test case (status Retired, or status Blocked with setup beginning 'Retired by ', 02 section 11.3) has a setup that does not begin 'Retired by ', or cites a live requirement without naming its superseding case ('superseded by TC-...') (02 T-19, T-10)"),
    ("TC_REQ_UNRESOLVED", VIOLATION, "a test case cites a requirement id that does not exist (orphan test case; 02 T-10)"),
    ("TC_TYPE_METHOD", VIOLATION, "a test case type is not an evidence class of its verification_method: Test = HostUnit, Emulation, Bench; Demonstration = Emulation, Bench, OnAir; Analysis = Simulation; Inspection = Inspection (02 section 4.4, T-10)"),
    ("TC_STATUS_EVIDENCE", VIOLATION, "a Passed test case has no report with credit true and result Pass, or a Failed test case has no report with result Fail, while docs/vv/reports exists (V&V section 9; 02 T-11)"),
    ("TC_SETUP_INCOMPLETE", VIOLATION, "a Bench or OnAir case lacks instruments or a setup with Article:, Configuration:, Safety: and Environment: (V&V 7.3 rule 7)"),
    ("VAL_TARGET_MISSING", VIOLATION, "a TC-VAL case names no OPS-NNN or MOE-NNN after 'Validates:' in its setup, or none of the named targets exists (V&V 7.3 rule 5)"),
    ("VAL_TARGET_UNRESOLVED", VIOLATION, "a TC-VAL case names, next to an existing target, an OPS-NNN or MOE-NNN after 'Validates:' that does not exist in docs/conops/conops.md or expectations.json (V&V 7.3 rule 5)"),
    ("EXPECTATIONS_INCONSISTENT", VIOLATION, "expectations.json does not have exactly one Need, a Goal's parent is not the Need, an Objective's parent is not a Goal, an MOE ngo_ids entry is not a Goal or Objective, or an ops_ids entry is not a heading of docs/conops/conops.md (02 T-21)"),
    ("TBD_PRESENT", VIOLATION, "the word TBD appears in a requirement or test case text field, an expectations.json entry, a table row of docs/icd/ICD-*.md, a table row or OPS-NNN scenario section of docs/conops/conops.md, or a table row of docs/plan/semp.md; in Markdown a mention of the policy terms ('TBD and TBR', 'TBD/TBR', '`TBD`', 'no TBD') is not a placeholder (charter section 7: no TBD in a baselined document; 01 section 12.2; 02 T-14)"),
    ("TBR_UNDOCUMENTED", VIOLATION, "the word TBR appears in a requirement without a tbr object"),
    ("TBR_UNMARKED", VIOLATION, "a tbr object is present but the description does not carry '(TBR)' after the estimated value (02 rule WR-12, T-14)"),
    ("TBR_ON_FINAL_STATUS", VIOLATION, "a tbr object is present while status is Verified, Closed or Retired (02 rule T-14; a Draft or Active requirement may carry an open TBR, charter section 7)"),
    ("TBR_CLOSE_BY", VIOLATION, "tbr.close_by is later than PDR for SYS or later than CDR for other modules (charter section 7)"),
    ("SHALL_COUNT", VIOLATION, "a requirement description does not contain exactly one shall (SE HB Appendix C; 02 T-17)"),
    ("MODAL_IN_DESCRIPTION", VIOLATION, "a requirement description contains a WR-07 group A modal verb (will, should, must, may, can, might); goals belong in the rationale"),
    ("SHALL_IN_TITLE", VIOLATION, "a requirement title contains shall (02 rule WR-14, T-17)"),
    ("NCR_FRONT_MATTER", VIOLATION, "an NCR file has no YAML front matter or no id"),
    ("NCR_ID_FORMAT", VIOLATION, "an NCR id does not match NCR-NNN or differs from its file name"),
    ("NCR_UNRESOLVED", VIOLATION, "an NCR cites a requirement, test case or hazard that does not exist (V&V 7.3 rule 8)"),
    ("NCR_ARTIFACT", VIOLATION, "an artifact listed in an NCR is missing, malformed or its SHA-256 differs (V&V 7.3 rule 8)"),
    ("NCR_NO_REQUIREMENT", VIOLATION, "an NCR with classification product (or no classification) and severity other than S4 cites no requirement in requirement_ids; the message lists the requirements of its test cases (SWE-052 Table 1 row 6; 04 section 10.3: an S4 NCR cites a requirement only when the defect affects it)"),
    ("NCR_FIELD_INVALID", VIOLATION, "an NCR severity is not S1, S2, S3 or S4 (SWE-202; 04 section 10.3), its status is not Open, Analysis, Dispositioned, Retest or Closed (04 section 10.7), or its classification is not product or procedure (docs/templates/ncr.md)"),
    ("REPORT_FRONT_MATTER", VIOLATION, "a report file has no YAML front matter or no test_case"),
    ("REPORT_ID_FORMAT", VIOLATION, "a report file name is not <test_case>-r<run>.md for its front matter"),
    ("REPORT_UNRESOLVED", VIOLATION, "a report cites a test case, requirement, validation target or NCR that does not exist or is not cited by its case (V&V 7.3 rule 8)"),
    ("REPORT_ARTIFACT", VIOLATION, "an artifact listed in a report is missing, malformed or its SHA-256 differs (V&V 7.3 rule 8)"),
    ("SOURCE_FILE_MISSING", WARNING, "an upstream artifact (stakeholder inputs, expectations, ConOps, ADRs, trade studies, regulatory corpus, tpm.json) is absent, so its ids cannot be resolved yet"),
    ("HAZARD_FILE_MISSING", WARNING, "docs/safety/hazards.json is absent, so hazard ids cannot be resolved yet"),
    ("RISK_FILE_MISSING", WARNING, "docs/risk/register.json is absent, so the RSK-NNN named by an 'Analysis accepted per RSK-NNN' note cannot be resolved yet"),
    ("REPORTS_DIR_MISSING", WARNING, "docs/vv/reports is absent, so Passed, Failed and Verified statuses are checked against case status only"),
    ("SOURCE_FORMAT_UNKNOWN", WARNING, "a source id or measure id matches no known identifier scheme"),
    ("STAKEHOLDERS_MISSING", WARNING, "expectations.json has no stakeholders array or an empty one, no entry of role customer, user or regulator, a stakeholder name used twice, or a stakeholder source_ids entry that does not resolve (02 section 3.0; T-21 and the stakeholder part of T-03; plain-run Warning before SRR, Error under --gate; the schema requires the array once baseline is set)"),
    ("SYS_UNALLOCATED", WARNING, "a Draft or Active SYS requirement names no receiving L2 module: no child_ids entry or parent_id child is a live requirement of an L2 module (RX, TX, PWR, CTL, ME, SW, SW-<SUB>), and docs/design/allocation.json lists it under no L2 module; each gap is listed for the reviewer to confirm or correct in V6 (02 section 2.3, T-18: Warning at SRR, Error from PDR under --gate)"),
    ("MOP_UNRESOLVED", WARNING, "a mop_ids entry names no id in docs/plan/tpm.json mops[] or tpms[] (02 T-16; Error from PDR under --gate)"),
    ("INTERFACE_TAG_NO_ICD", WARNING, "a requirement tagged interface has no ICD-<A>-<B> id in design_refs (02 section 3.5, T-22; Error from PDR under --gate)"),
    ("DESCRIPTION_LENGTH", WARNING, "a requirement description exceeds 25 words"),
    ("UNVERIFIABLE_WORD", WARNING, "a requirement description uses a WR-07 group B word (unverifiable or ambiguous; SE HB Appendix C)"),
    ("FAILED_TC_WITHOUT_NCR", WARNING, "a Failed test case has no NCR citing it (charter section 9)"),
    ("HAZARD_INVERSE", WARNING, "hazards.json and a requirement disagree about which requirements control a hazard, or a hazard's requirement_ids is not the union of its controls' control_req_ids"),
    ("MOE_WITHOUT_OPS", WARNING, "an MOE has no ops_ids entry while docs/conops/conops.md exists (02 T-20)"),
    ("CORE_SI_UNCOVERED", WARNING, "a bold (core) SI row is cited by no SYS requirement; evaluated once at least one requirement exists (02 section 3.1, T-20)"),
    ("OBJECTIVE_UNCOVERED", WARNING, "a Baselined Objective is cited by no SYS requirement and no MOE; evaluated once at least one requirement exists (02 T-20)"),
    ("RENDER_STALE", WARNING, "a rendered expectations.md or requirements.md beside its JSON is absent, was not generated by --render, or differs from the rendering of the current JSON (02 section 8.1; charter section 5 rendered .md)"),
    ("OPS_UNCITED", WARNING, "an OPS-NNN heading is cited by no requirement source_ids and no TC-VAL case; evaluated once at least one requirement exists (02 T-20)"),
)

ENFORCED = "Enforced"
PARTIAL = "Partial"
NOT_ENFORCED = "Not enforced"
ADD = "add"
PROMOTE = "promoted to VIOLATION"


@dataclass(frozen=True)
class TraceRow:
    """One Class A row of NPR 7150.2D section 3.12.1 Table 1 (SWE-052) and what this tool does for it."""

    row: int
    relationship: str
    forward: str
    backward: str
    enforced: tuple[str, ...]
    planned: tuple[tuple[str, str, str], ...]  # (code, action ADD or PROMOTE, gate and source)
    note: str = ""

    @property
    def state(self) -> str:
        if not self.enforced:
            return NOT_ENFORCED
        return PARTIAL if self.planned else ENFORCED


# Report section 1.4. The planned codes and gates are those of
# docs/process/03-software-classification-and-rmm.md section 8; a test checks this
# table against CHECK_CATALOGUE (enforced codes exist, planned additions do not yet).
SWE052_COVERAGE: tuple[TraceRow, ...] = (
    TraceRow(
        1, "Higher-level requirements to the software requirements",
        "parent_id and source_ids of each requirement", "child_ids of the parent",
        ("PARENT_MISSING", "PARENT_UNRESOLVED", "PARENT_CYCLE", "CHILD_INVERSE", "SELF_DERIVED_UNSUPPORTED", "L1_PARENT_NOT_NULL", "SOURCE_UNRESOLVED", "SOURCE_L0_MISSING"),
        (),
    ),
    TraceRow(
        2, "Software requirements to the system hazards",
        "hazard_ids of each requirement", "docs/safety/hazards.json requirement_ids and each control's control_req_ids",
        ("HAZARD_ID_FORMAT", "HAZARD_UNRESOLVED", "HAZARD_CONTROL_UNTRACED", "SAFETY_TAG_NO_HAZARD", "HAZARD_REQ_NOT_TESTED", "HAZARD_REQ_NOT_ON_TARGET"),
        (
            ("HAZARD_UNCONTROLLED", ADD, "before PDR (03 section 8)"),
            ("HAZARD_INVERSE", PROMOTE, "PDR (03 section 8; 04 section 7.3 rule 6 asks for every gate)"),
        ),
        "HAZARD_INVERSE is a warning in a plain run; for SW and SW-<SUB> requirements the hazards.json-to-requirement direction is the violation HAZARD_CONTROL_UNTRACED",
    ),
    TraceRow(
        3, "Software requirements to the software design components",
        "design_refs of each REQ-SW-*", "docs/design/allocation.json element requirement lists",
        (),
        (
            ("DESIGN_REF_UNRESOLVED", ADD, "before PDR (03 section 8; 02 T-15)"),
            ("DESIGN_REF_MISSING", ADD, "before PDR (03 section 8; 02 T-15)"),
            ("DESIGN_ELEMENT_ORPHAN", ADD, "before PDR (03 section 8; 02 T-15)"),
        ),
        "design_refs is read into the data model; only INTERFACE_TAG_NO_ICD (T-22) reads it today",
    ),
    TraceRow(
        4, "Software design components to the software code",
        "design_refs Rust unit paths", "@design, @req and @verify tags in firmware/**/*.rs (07 CS-24)",
        (),
        (
            ("TAG_UNRESOLVED", ADD, "before CDR (03 section 8; 02 T-15)"),
            ("REQ_UNTAGGED", ADD, "before CDR (03 section 8; 02 T-15)"),
            ("DESIGN_ELEMENT_UNIMPLEMENTED", ADD, "before CDR (03 section 8)"),
        ),
        "no firmware scan exists",
    ),
    TraceRow(
        5, "Software requirements to the software verification(s)",
        "requirement_ids of each test case", "report section 3 verification matrix",
        ("REQ_UNVERIFIED", "REQ_NO_CLOSING_CASE", "TC_REQ_UNRESOLVED", "TC_TYPE_METHOD", "VERIFIED_WITHOUT_EVIDENCE", "TC_STATUS_EVIDENCE", "REPORT_UNRESOLVED"),
        (),
    ),
    TraceRow(
        6, "Software requirements to the software non-conformances",
        "requirement_ids of each docs/vv/ncr/NCR-NNN.md", "report section 10.2 requirement-to-NCR list",
        ("NCR_FRONT_MATTER", "NCR_ID_FORMAT", "NCR_UNRESOLVED", "NCR_NO_REQUIREMENT", "NCR_FIELD_INVALID", "VERIFIED_WITH_OPEN_NCR"),
        (),
        "03 section 8 plans NCR_BLOCKS_VERIFIED before TRR; VERIFIED_WITH_OPEN_NCR already blocks Verified for an open NCR of any severity",
    ),
)


# ----------------------------------------------------------------------------
# Data model
# ----------------------------------------------------------------------------


@dataclass
class Finding:
    severity: str
    code: str
    location: str
    message: str


@dataclass
class Requirement:
    id: str
    module: str
    file: str
    title: str
    description: str
    rationale: str
    verification_method: str
    verification_note: str
    status: str
    parent_id: str | None
    child_ids: list[str]
    source_ids: list[str]
    hazard_ids: list[str]
    design_refs: list[str]
    tbr: dict[str, Any] | None
    priority: str
    tags: list[str] = field(default_factory=list)
    mop_ids: list[str] = field(default_factory=list)

    @property
    def is_retired(self) -> bool:
        """Status Retired, or the charter section 6 interim form: status Closed with tag retired."""
        return self.status == RETIRED or (self.status == "Closed" and RETIRED_TAG in self.tags)


@dataclass
class TestCase:
    id: str
    module: str
    file: str
    title: str
    requirement_ids: list[str]
    verification_method: str
    type: str
    status: str
    setup: str
    acceptance_criteria: str
    instruments: list[str]
    automation_ref: str | None
    text_fields: dict[str, str]

    @property
    def validation_targets(self) -> list[str]:
        """OPS/MOE ids named after 'Validates:' in setup (V&V section 7.2)."""
        clause = VALIDATES_CLAUSE.search(self.setup)
        return sorted(set(VALIDATION_TARGET.findall(clause.group(0)))) if clause else []

    @property
    def phase(self) -> str:
        """Phase named after 'Phase:' in setup (V&V section 7.2), or '' when absent."""
        match = PHASE_CLAUSE.search(self.setup)
        return match.group(1) if match else ""

    @property
    def is_retired(self) -> bool:
        """Status Retired, or the 02 section 11.3 interim form: status Blocked with setup starting 'Retired by '."""
        return self.status == RETIRED or (self.status == BLOCKED and self.setup.lstrip().startswith(RETIRED_PREFIX))

    @property
    def is_recurring(self) -> bool:
        """'Recurring: yes' in setup: the case is repeated at recurring or pre-operation acceptance (04 section 7.1)."""
        match = RECURRING_CLAUSE.search(self.setup)
        return bool(match) and match.group(1).lower() == "yes"


@dataclass
class Hazard:
    id: str
    title: str
    requirement_ids: list[str] | None
    control_req_ids: list[str] | None = None


@dataclass
class Expectation:
    """One NGO-, MOE- or CON- entry of expectations.json (02 section 3.2)."""

    id: str
    kind: str  # Need, Goal, Objective, MOE, CON
    status: str
    title: str
    parent_id: str | None
    ngo_ids: list[str]
    ops_ids: list[str]
    source_ids: list[str]
    text_fields: dict[str, str] = field(default_factory=dict)


@dataclass
class Ncr:
    id: str
    file: str
    title: str
    status: str
    severity: str
    requirement_ids: list[str]
    test_case_ids: list[str]
    hazard_ids: list[str]
    artifacts: list[Any] = field(default_factory=list)
    classification: str = ""


@dataclass
class Report:
    file: str
    test_case: str
    run: str
    requirement_ids: list[str]
    validates: list[str]
    credit: bool
    result: str
    date: str
    ncr_ids: list[str]
    artifacts: list[Any]

    @property
    def is_credit_pass(self) -> bool:
        return self.credit and self.result == "Pass"


@dataclass
class Project:
    root: Path
    requirements: dict[str, Requirement] = field(default_factory=dict)
    requirement_files: list[str] = field(default_factory=list)
    test_cases: dict[str, TestCase] = field(default_factory=dict)
    test_case_files: list[str] = field(default_factory=list)
    hazards: dict[str, Hazard] = field(default_factory=dict)
    hazards_present: bool = False
    risks: set[str] | None = None
    ncrs: dict[str, Ncr] = field(default_factory=dict)
    reports: list[Report] = field(default_factory=list)
    reports_present: bool = False
    stakeholder_inputs: set[str] | None = None
    core_inputs: set[str] = field(default_factory=set)
    expectations: set[str] | None = None
    expectation_entries: dict[str, Expectation] = field(default_factory=dict)
    conops_scenarios: set[str] | None = None
    adrs: set[str] | None = None
    trade_studies: set[str] | None = None
    measures: set[str] | None = None
    regulations: set[str] | None = None
    sar_memo_present: bool = False
    allocation_present: bool = False
    allocation_error: str | None = None
    allocation_modules: dict[str, set[str]] = field(default_factory=dict)  # requirement id -> modules named in allocation.json
    icd_tables: dict[str, list[tuple[int, str]]] = field(default_factory=dict)
    baselined_lines: dict[str, list[tuple[int, str]]] = field(default_factory=dict)
    conops_titles: dict[str, str] = field(default_factory=dict)
    expectations_raw: dict[str, Any] | None = None
    requirement_raw: dict[str, dict[str, Any]] = field(default_factory=dict)
    req_id_re: re.Pattern[str] = re.compile(DEFAULT_REQ_ID_PATTERN)
    tc_id_re: re.Pattern[str] = re.compile(DEFAULT_TC_ID_PATTERN)
    findings: list[Finding] = field(default_factory=list)

    def violation(self, code: str, location: str, message: str) -> None:
        self.findings.append(Finding(VIOLATION, code, location, message))

    def warning(self, code: str, location: str, message: str) -> None:
        self.findings.append(Finding(WARNING, code, location, message))

    @property
    def violations(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == VIOLATION]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == WARNING]

    def ordered_requirements(self) -> list[Requirement]:
        return sorted(self.requirements.values(), key=lambda r: (r.module != L1_MODULE, r.module, r.id))

    def live_requirements(self) -> list[Requirement]:
        """Every requirement whose status is not Retired (04 section 7.1; 02 section 11.3 rule 4)."""
        return [r for r in self.ordered_requirements() if not r.is_retired]

    def ordered_test_cases(self) -> list[TestCase]:
        return sorted(self.test_cases.values(), key=lambda t: t.id)

    def live_test_cases(self) -> list[TestCase]:
        return [tc for tc in self.ordered_test_cases() if not tc.is_retired]

    def tcs_for(self, req_id: str) -> list[TestCase]:
        """Every case citing the requirement, retired cases included."""
        return sorted((tc for tc in self.test_cases.values() if req_id in tc.requirement_ids), key=lambda tc: tc.id)

    def live_tcs_for(self, req_id: str) -> list[TestCase]:
        """Cases citing the requirement that are not retired (02 section 11.3): the ones that count for coverage."""
        return [tc for tc in self.tcs_for(req_id) if not tc.is_retired]

    def closing_cases(self, req: Requirement) -> list[TestCase]:
        """Live cases citing req whose verification_method equals the requirement's (V&V 7.1)."""
        return [tc for tc in self.live_tcs_for(req.id) if tc.verification_method == req.verification_method]

    def is_software(self, req: Requirement) -> bool:
        """True for module SW and every SW-<SUB> firmware module (SWE-192 scope)."""
        return bool(SOFTWARE_MODULE.match(req.module))

    def hazards_naming(self, req_id: str) -> list[str]:
        """Hazards of hazards.json that name the requirement in requirement_ids or a control's control_req_ids."""
        return sorted(h.id for h in self.hazards.values() if req_id in (h.requirement_ids or []) or req_id in (h.control_req_ids or []))

    def hazard_trace(self, req: Requirement) -> list[str]:
        """04 section 3: a requirement traces to a hazard through its own hazard_ids or through hazards.json."""
        return sorted(set(req.hazard_ids) | set(self.hazards_naming(req.id)))

    def supporting_cases(self, req: Requirement) -> list[TestCase]:
        return [tc for tc in self.live_tcs_for(req.id) if tc.verification_method != req.verification_method]

    def acceptance_cases(self, req: Requirement) -> list[TestCase]:
        return [tc for tc in self.live_tcs_for(req.id) if tc.module == ACCEPTANCE_MODULE]

    def children_of(self, req_id: str) -> list[Requirement]:
        return sorted((r for r in self.requirements.values() if r.parent_id == req_id), key=lambda r: r.id)

    def ncrs_for(self, req_id: str) -> list[Ncr]:
        return sorted((n for n in self.ncrs.values() if req_id in n.requirement_ids), key=lambda n: n.id)

    def reports_for(self, tc_id: str) -> list[Report]:
        return sorted((r for r in self.reports if r.test_case == tc_id), key=lambda r: (r.date, r.file))

    def validation_cases(self) -> list[TestCase]:
        return [tc for tc in self.ordered_test_cases() if tc.module == VALIDATION_MODULE]

    def validation_targets(self) -> list[str]:
        """Every OPS-NNN heading, then every MOE-NNN (one validation row each)."""
        return sorted(self.conops_scenarios or set()) + sorted(e.id for e in self.expectation_entries.values() if e.kind == "MOE")

    def validation_row(self, target: str) -> tuple[list[TestCase], str]:
        """The TC-VAL cases naming the target and the row status (04 section 7.2)."""
        matching = [tc for tc in self.validation_cases() if target in tc.validation_targets]
        if not matching:
            return matching, "No case"
        if all(tc.status == "Passed" for tc in matching):
            return matching, "Validated"
        return matching, "Open"

    def expectations_of_kind(self, kind: str) -> list[Expectation]:
        return sorted((e for e in self.expectation_entries.values() if e.kind == kind), key=lambda e: e.id)

    def child_modules(self, req: Requirement) -> list[str]:
        """Modules of the live L2 requirements named by child_ids or whose parent_id is req (02 section 2.3, T-18)."""
        ids = set(req.child_ids) | {c.id for c in self.children_of(req.id)}
        found = {self.requirements[i].module for i in ids if i in self.requirements and not self.requirements[i].is_retired}
        return sorted(m for m in found if is_l2_module(m))

    def allocated_modules(self, req_id: str) -> list[str]:
        """L2 modules under which docs/design/allocation.json lists the requirement (02 section 2.3, T-18)."""
        return sorted(m for m in self.allocation_modules.get(req_id, set()) if is_l2_module(m))

    def receiving_modules(self, req: Requirement) -> list[str]:
        """Every L2 module that receives the requirement, through children or allocation.json."""
        return sorted(set(self.child_modules(req)) | set(self.allocated_modules(req.id)))


# ----------------------------------------------------------------------------
# Loading helpers
# ----------------------------------------------------------------------------


def is_l2_module(module: str) -> bool:
    """RX, TX, PWR, CTL, ME, SW or SW-<SUB>: the L2 requirement modules of charter section 6."""
    return module in L2_MODULES or bool(SW_SUB_MODULE.match(module))


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def as_str(value: Any) -> str:
    return value if isinstance(value, str) else ""


def as_str_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    if isinstance(value, str) and value and value.lower() != "none":
        return [value]
    return []


def collect_ids(obj: Any, pattern: re.Pattern[str]) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Every dict anywhere in obj whose 'id' matches pattern, in document order.

    The first definition of an id is kept; every later one is returned in the
    duplicate list (charter section 6: ids are unique and never reused).
    """
    found: dict[str, dict[str, Any]] = {}
    duplicates: list[str] = []

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            ident = node.get("id")
            if isinstance(ident, str) and pattern.match(ident):
                if ident in found:
                    duplicates.append(ident)
                else:
                    found[ident] = node
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for item in node:
                visit(item)

    visit(obj)
    return found, duplicates


def report_duplicates(project: Project, location: Path, duplicates: Iterable[str]) -> None:
    for ident in duplicates:
        project.violation("ID_DUPLICATE", f"{location} {ident}", f"id defined more than once in {location}; the first definition is kept")


def schema_id_pattern(root: Path, schema_rel: Path, list_key: str, fallback: str, project: Project) -> re.Pattern[str]:
    """Read properties.<list_key>.items.properties.id.pattern from a schema."""
    schema_path = root / schema_rel
    if not schema_path.is_file():
        project.violation("SCHEMA_MISSING", str(schema_rel), f"schema not found; using fallback id pattern {fallback}")
        return re.compile(fallback)
    schema, error = validate_docs.load_json(schema_path)
    if error is not None:
        project.violation("SCHEMA_MISSING", str(schema_rel), error)
        return re.compile(fallback)
    try:
        return re.compile(schema["properties"][list_key]["items"]["properties"]["id"]["pattern"])
    except (KeyError, TypeError, re.error):
        project.warning("SCHEMA_ID_PATTERN_MISSING", str(schema_rel), f"no id pattern in schema; using fallback {fallback}")
        return re.compile(fallback)


def validate_against(project: Project, document: Path, schema_rel: Path, cache: dict[Path, Any], convention: str) -> None:
    """SCHEMA_INVALID for every schema error of document when its schema exists (02 T-01)."""
    schema = project.root / schema_rel
    if not schema.is_file():
        return
    result = validate_docs.validate_document(document, schema, cache, convention)
    for error in result.errors:
        project.violation("SCHEMA_INVALID", rel(document, project.root), error)


# ----------------------------------------------------------------------------
# YAML front matter (docs/templates/ncr.md and verification-report.md): the
# parser lives in tools/validate_docs.py and is shared by every tool.
# ----------------------------------------------------------------------------

FM_KEY = validate_docs.FM_KEY
split_front_matter = validate_docs.split_front_matter
parse_front_matter = validate_docs.parse_front_matter
parse_front_matter_subset = validate_docs.parse_front_matter_subset


# ----------------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------------


def module_known(module: str, list_key: str) -> bool:
    """Charter section 6: requirement modules, plus the test-only modules for test case files."""
    if module in TEST_ONLY_MODULES:
        return list_key == "test_cases"
    return module in REQUIREMENT_MODULES or bool(SW_SUB_MODULE.match(module))


def expected_module_for(document: Path) -> str:
    """Directory name of a requirements/test case file, upper-cased: sw-keyer -> SW-KEYER."""
    return document.parent.name.upper()


def load_module_file(
    project: Project, document: Path, schema: Path, list_key: str, id_re: re.Pattern[str], id_prefix: str, modules_seen: dict[str, str], known: dict[str, Any], cache: dict[Path, Any]
) -> tuple[str, str, list[tuple[str, dict[str, Any]]]]:
    """Shared loader for requirements.json and test_cases.json: schema, module and id checks.

    Returns (location, module, [(id, raw item)]) for the items that carry a new id.
    """
    root = project.root
    location = rel(document, root)
    result = validate_docs.validate_document(document, root / schema, cache, list_key)
    for error in result.errors:
        project.violation("SCHEMA_INVALID", location, error)
    data, error = validate_docs.load_json(document)
    if error is not None or not isinstance(data, dict):
        return location, "", []
    if list_key == "requirements":
        project.requirement_raw[location] = data
    module = as_str(data.get("module"))
    expected = expected_module_for(document)
    if module and module != expected:
        project.violation("MODULE_MISMATCH", location, f"module '{module}' but directory implies '{expected}'")
    if module and not module_known(module, list_key):
        allowed = "SYS, RX, TX, PWR, CTL, ME, SW, SW-<SUB>" + (" and the test-only VAL, ATP, SW-COV, SW-REG, SW-TOOL" if list_key == "test_cases" else " (SW-COV, SW-REG, SW-TOOL are test-only)")
        project.violation("MODULE_UNKNOWN", location, f"module '{module}' is not a module of charter section 6 ({allowed}; VER is reserved and unused)")
    if module in modules_seen:
        project.violation("MODULE_DUPLICATE", location, f"module '{module}' also declared in {modules_seen[module]}")
    elif module:
        modules_seen[module] = location
    items = data.get(list_key)
    accepted: list[tuple[str, dict[str, Any]]] = []
    seen_here: dict[str, str] = {}
    if not isinstance(items, list):
        return location, module, accepted
    for index, raw in enumerate(items):
        if not isinstance(raw, dict):
            continue
        ident = as_str(raw.get("id"))
        where = f"{location} {ident or f'{list_key}[{index}]'}"
        if not ident:
            project.violation("ID_FORMAT", where, "item has no string id")
            continue
        if not id_re.match(ident):
            project.violation("ID_FORMAT", where, f"id does not match {id_re.pattern}")
        elif module and not re.fullmatch(rf"{id_prefix}-{re.escape(module)}-[0-9]{{3}}", ident):
            project.violation("MODULE_MISMATCH", where, f"id is not {id_prefix}-{module}-NNN for module '{module}'")
        if ident in known:
            project.violation("ID_DUPLICATE", where, f"id already defined in {known[ident].file}")
            continue
        if ident in seen_here:
            project.violation("ID_DUPLICATE", where, f"id already defined earlier in {seen_here[ident]}")
            continue
        seen_here[ident] = location
        accepted.append((ident, raw))
    return location, module, accepted


def load_requirements(project: Project, cache: dict[Path, Any]) -> None:
    modules_seen: dict[str, str] = {}
    for document in sorted(project.root.glob(REQUIREMENTS_GLOB)):
        location, module, items = load_module_file(project, document, REQ_SCHEMA, "requirements", project.req_id_re, "REQ", modules_seen, project.requirements, cache)
        project.requirement_files.append(location)
        for ident, raw in items:
            tbr = raw.get("tbr")
            project.requirements[ident] = Requirement(
                id=ident,
                module=module,
                file=location,
                title=as_str(raw.get("title")),
                description=as_str(raw.get("description")),
                rationale=as_str(raw.get("rationale")),
                verification_method=as_str(raw.get("verification_method")),
                verification_note=as_str(raw.get("verification_note")),
                status=as_str(raw.get("status")),
                parent_id=raw.get("parent_id") if isinstance(raw.get("parent_id"), str) else None,
                child_ids=as_str_list(raw.get("child_ids")),
                source_ids=as_str_list(raw.get("source_ids")),
                hazard_ids=as_str_list(raw.get("hazard_ids")),
                design_refs=as_str_list(raw.get("design_refs")),
                tbr=tbr if isinstance(tbr, dict) else None,
                priority=as_str(raw.get("priority")),
                tags=as_str_list(raw.get("tags")),
                mop_ids=as_str_list(raw.get("mop_ids")),
            )


def load_test_cases(project: Project, cache: dict[Path, Any]) -> None:
    modules_seen: dict[str, str] = {}
    for document in sorted(project.root.glob(TEST_CASES_GLOB)):
        location, module, items = load_module_file(project, document, TC_SCHEMA, "test_cases", project.tc_id_re, "TC", modules_seen, project.test_cases, cache)
        project.test_case_files.append(location)
        for ident, raw in items:
            setup = as_str(raw.get("setup"))
            acceptance = as_str(raw.get("acceptance_criteria"))
            automation_ref = raw.get("automation_ref")
            project.test_cases[ident] = TestCase(
                id=ident,
                module=module,
                file=location,
                title=as_str(raw.get("title")),
                requirement_ids=as_str_list(raw.get("requirement_ids")),
                verification_method=as_str(raw.get("verification_method")),
                type=as_str(raw.get("type")),
                status=as_str(raw.get("status")),
                setup=setup,
                acceptance_criteria=acceptance,
                instruments=as_str_list(raw.get("instruments")),
                automation_ref=automation_ref if isinstance(automation_ref, str) else None,
                text_fields={
                    "title": as_str(raw.get("title")),
                    "setup": setup,
                    "acceptance_criteria": acceptance,
                    "procedure": " ".join(as_str_list(raw.get("procedure"))),
                },
            )


def load_expectations(project: Project, cache: dict[Path, Any]) -> None:
    """expectations.json: NGO/MOE/CON ids, entry kinds and links (02 section 3.2, T-03, T-21)."""
    path = project.root / EXPECTATIONS
    if not path.is_file():
        return
    data, error = validate_docs.load_json(path)
    if error is not None:
        project.violation("SCHEMA_INVALID", str(EXPECTATIONS), f"{error}; no L0 id can be resolved and the L0 rules (T-07, T-20, T-21) and RENDER_STALE are not evaluated until it parses")
        return
    validate_against(project, path, EXPECTATIONS_SCHEMA, cache, "expectations")
    if isinstance(data, dict):
        project.expectations_raw = data
    if not (isinstance(data, dict) and isinstance(data.get("ngos"), list)):
        # Structure other than the L0 schema: collect the ids only.
        ids: set[str] = set()
        for pattern in (NGO_ID, MOE_ID, CON_ID):
            found, duplicates = collect_ids(data, pattern)
            report_duplicates(project, EXPECTATIONS, duplicates)
            ids |= set(found)
        project.expectations = ids
        return
    for list_key, fixed_kind in (("ngos", None), ("moes", "MOE"), ("constraints", "CON")):
        entries = data.get(list_key)
        if not isinstance(entries, list):
            continue
        for index, raw in enumerate(entries):
            if not isinstance(raw, dict):
                continue
            ident = as_str(raw.get("id"))
            if not ident:
                continue  # the schema reports the missing id
            where = f"{EXPECTATIONS} {ident}"
            if ident in project.expectation_entries:
                project.violation("ID_DUPLICATE", where, f"id already defined earlier in {EXPECTATIONS} ({list_key}[{index}])")
                continue
            project.expectation_entries[ident] = Expectation(
                id=ident,
                kind=fixed_kind or as_str(raw.get("kind")),
                status=as_str(raw.get("status")),
                title=as_str(raw.get("title")),
                parent_id=raw.get("parent_id") if isinstance(raw.get("parent_id"), str) else None,
                ngo_ids=as_str_list(raw.get("ngo_ids")),
                ops_ids=as_str_list(raw.get("ops_ids")),
                source_ids=as_str_list(raw.get("source_ids")),
                text_fields={name: as_str(raw.get(name)) for name in EXPECTATION_TEXT_FIELDS},
            )
    project.expectations = set(project.expectation_entries)


def load_allocation(project: Project) -> None:
    """docs/design/allocation.json (02 section 2.3, T-18): the modules each requirement id is allocated to.

    Three record forms allocate, wherever they sit in the file:

    1. an object with a requirement_ids list allocates those ids to the module named
       by its own module field or, when it has none, by the nearest enclosing object
       that has one (elements[] entries: id, module, requirement_ids, code; 02
       section 7 rows 3 and 4);
    2. an entry of a list under the key modules whose id is a string is the record of
       that module (modules[] entries: id RX, requirement_ids; the reading of 02
       section 2.3 "lists the SYS id in requirement_ids under the receiving module");
    3. an object with a requirement_id string and a modules list allocates that id to
       each listed module (per-requirement allocations[] entries).

    A requirement_ids list with no module above it allocates nothing, so lists such
    as functions[] or gaps[] do not count. Whether a module is an L2 module is
    decided by the check (is_l2_module). Validation of the file against
    docs/design/allocation.schema.json belongs to validate_docs.py.
    """
    path = project.root / ALLOCATION
    if not path.is_file():
        return
    project.allocation_present = True
    data, error = validate_docs.load_json(path)
    if error is not None:
        project.allocation_error = error
        return

    def allocate(req_id: Any, module: str) -> None:
        if isinstance(req_id, str) and module:
            project.allocation_modules.setdefault(req_id, set()).add(module)

    def visit(node: Any, module: str | None, in_modules_list: bool = False) -> None:
        if isinstance(node, dict):
            own = node.get("module")
            if isinstance(own, str) and own:
                current: str | None = own
            elif in_modules_list and isinstance(node.get("id"), str):
                current = node["id"]
            else:
                current = module
            ids = node.get("requirement_ids")
            if isinstance(ids, list) and current:
                for req_id in ids:
                    allocate(req_id, current)
            single, modules = node.get("requirement_id"), node.get("modules")
            if isinstance(single, str) and isinstance(modules, list):
                for listed in modules:
                    if isinstance(listed, str):
                        allocate(single, listed)
            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    visit(value, current, key == "modules" and isinstance(value, list))
        elif isinstance(node, list):
            for item in node:
                visit(item, module, in_modules_list)

    visit(data, None)


def load_upstream(project: Project, cache: dict[Path, Any]) -> None:
    """Stakeholder inputs, expectations, ConOps scenarios, ADRs, trade studies, risks, measures, regulations."""
    root = project.root
    inputs = root / STAKEHOLDER_INPUTS
    if inputs.is_file():
        project.stakeholder_inputs = set()
        for match in SI_ROW.finditer(inputs.read_text(encoding="utf-8")):
            project.stakeholder_inputs.add(match.group(1))
            if "**" in match.group(0):
                project.core_inputs.add(match.group(1))
    load_expectations(project, cache)
    conops = root / CONOPS
    if conops.is_file():
        conops_text = conops.read_text(encoding="utf-8")
        headings = [(conops_text.count("\n", 0, m.start()) + 1, m.group(1)) for m in OPS_HEADING.finditer(conops_text)]
        first_line: dict[str, int] = {}
        for number, ops_id in headings:
            if ops_id in first_line:
                project.violation("ID_DUPLICATE", f"{CONOPS}:{number} {ops_id}", f"scenario heading {ops_id} repeated; first defined at line {first_line[ops_id]}")
            else:
                first_line[ops_id] = number
        project.conops_scenarios = set(first_line)
        project.conops_titles = {}
        for m in OPS_TITLE.finditer(conops_text):
            project.conops_titles.setdefault(m.group(1), m.group(2).strip())
        project.baselined_lines[str(CONOPS)] = conops_scan_lines(conops_text)
    semp = root / SEMP
    if semp.is_file():
        project.baselined_lines[str(SEMP)] = table_lines(semp.read_text(encoding="utf-8"))
    project.adrs = numbered_files(project, root / ADR_DIR, "ADR", ADR_DIR)
    project.trade_studies = numbered_files(project, root / TRADE_STUDY_DIR, "TS", TRADE_STUDY_DIR)
    risks = root / RISKS
    if risks.is_file():
        data, error = validate_docs.load_json(risks)
        if error is None:
            validate_against(project, risks, RISKS_SCHEMA, cache, "risk_register")
            ids, duplicates = collect_ids(data, RSK_ID)
            report_duplicates(project, RISKS, duplicates)
            project.risks = set(ids)
        else:
            project.violation("SCHEMA_INVALID", str(RISKS), error)
    measures = root / MEASURES
    if measures.is_file():
        data, error = validate_docs.load_json(measures)
        if error is None:
            mops, mop_duplicates = collect_ids(data, MOP_ID)
            tpms, tpm_duplicates = collect_ids(data, TPM_ID)
            report_duplicates(project, MEASURES, mop_duplicates + tpm_duplicates)
            project.measures = set(mops) | set(tpms)
        else:
            project.violation("SCHEMA_INVALID", str(MEASURES), error)
    regulatory = root / REGULATORY_DIR
    if regulatory.is_dir():
        project.regulations = set()
        for path in regulatory.glob("*.md"):
            match = REGULATION_FILE.match(path.name)
            if match:
                project.regulations.add(match.group(1))
    project.sar_memo_present = (root / SAR_DECISION_MEMO).is_file()
    load_allocation(project)
    for icd in sorted(root.glob(ICD_GLOB)):
        # Only definition-table rows are scanned for TBD: the template's instruction
        # sentence "No TBD anywhere" is prose, and every ICD value sits in a table (02 section 3.5).
        project.icd_tables[rel(icd, root)] = table_lines(icd.read_text(encoding="utf-8"))


def table_lines(text: str) -> list[tuple[int, str]]:
    """Numbered Markdown table rows (lines starting with '|')."""
    return [(n, line) for n, line in enumerate(text.splitlines(), start=1) if line.lstrip().startswith("|")]


def conops_scan_lines(text: str) -> list[tuple[int, str]]:
    """ConOps lines checked for TBD: every table row, and every line of an OPS-NNN scenario section.

    A scenario section runs from its OPS-NNN heading to the next heading of the
    same or a higher level. Prose outside the scenarios (the document's own
    instructions) is not scanned, as for ICDs (02 section 3.5).
    """
    lines = text.splitlines()
    selected: dict[int, str] = {}
    level: int | None = None
    for number, line in enumerate(lines, start=1):
        heading = re.match(r"^(#{1,6})\s", line)
        if heading:
            depth = len(heading.group(1))
            if OPS_HEADING.match(line):
                level = depth
            elif level is not None and depth <= level:
                level = None
        if level is not None or line.lstrip().startswith("|"):
            selected[number] = line
    return sorted(selected.items())


def numbered_files(project: Project, directory: Path, prefix: str, location: Path) -> set[str] | None:
    """ADR-NNN or TS-NNN ids from file name prefixes; two files with one number are ID_DUPLICATE."""
    if not directory.is_dir():
        return None
    width = len(prefix) + 4
    by_id: dict[str, list[str]] = defaultdict(list)
    for path in sorted(directory.glob(f"{prefix}-[0-9][0-9][0-9]*.md")):
        by_id[path.name[:width]].append(path.name)
    for ident, names in sorted(by_id.items()):
        if len(names) > 1:
            project.violation("ID_DUPLICATE", f"{location} {ident}", f"{len(names)} files carry {ident}: {', '.join(names)}; the first is kept")
    return set(by_id)


def load_hazards(project: Project, cache: dict[Path, Any]) -> None:
    path = project.root / HAZARDS
    if not path.is_file():
        return
    data, error = validate_docs.load_json(path)
    if error is not None:
        project.violation("SCHEMA_INVALID", str(HAZARDS), error)
        return
    validate_against(project, path, HAZARDS_SCHEMA, cache, "hazards")
    project.hazards_present = True
    hazard_ids, duplicates = collect_ids(data, HZ_ID)
    report_duplicates(project, HAZARDS, duplicates)
    for ident, raw in hazard_ids.items():
        req_ids = raw.get("requirement_ids")
        controls = raw.get("controls")
        control_req_ids: list[str] | None = None
        if isinstance(controls, list):
            control_req_ids = []
            for control in controls:
                if isinstance(control, dict):
                    control_req_ids.extend(as_str_list(control.get("control_req_ids")))
        project.hazards[ident] = Hazard(
            id=ident,
            title=as_str(raw.get("title")),
            requirement_ids=as_str_list(req_ids) if isinstance(req_ids, list) else None,
            control_req_ids=control_req_ids,
        )


def load_ncrs(project: Project) -> None:
    ncr_dir = project.root / NCR_DIR
    if not ncr_dir.is_dir():
        return
    for path in sorted(ncr_dir.glob("NCR-*.md")):
        location = rel(path, project.root)
        front = parse_front_matter(path.read_text(encoding="utf-8"))
        if front is None or not isinstance(front.get("id"), str):
            project.violation("NCR_FRONT_MATTER", location, "missing YAML front matter with an id field")
            continue
        ident = front["id"]
        if not NCR_ID.match(ident):
            project.violation("NCR_ID_FORMAT", location, f"id '{ident}' does not match NCR-NNN")
        elif path.stem != ident:
            project.violation("NCR_ID_FORMAT", location, f"id '{ident}' differs from file name")
        if ident in project.ncrs:
            project.violation("ID_DUPLICATE", location, f"id already defined in {project.ncrs[ident].file}")
            continue
        test_case_ids = as_str_list(front.get("test_case")) + as_str_list(front.get("test_case_ids"))
        test_case_ids += as_str_list(front.get("retest_cases")) + as_str_list(front.get("regression_cases"))
        project.ncrs[ident] = Ncr(
            id=ident,
            file=location,
            title=as_str(front.get("title")) or first_heading(path),
            status=as_str(front.get("status")),
            severity=as_str(front.get("severity")),
            requirement_ids=as_str_list(front.get("requirement_ids")),
            test_case_ids=sorted(set(test_case_ids)),
            hazard_ids=as_str_list(front.get("hazard_ids")),
            artifacts=artifact_entries(front),
            classification=as_str(front.get("classification")),
        )


def artifact_entries(front: dict[str, Any]) -> list[Any]:
    """The 'artifacts' list of a report or NCR front matter: string or flat-map entries."""
    raw = front.get("artifacts")
    if not isinstance(raw, list):
        return []
    return [a for a in raw if isinstance(a, (str, dict))]


def artifact_path_and_hash(entry: Any) -> tuple[str, str] | None:
    """Split an artifact entry into (path, sha256).

    Accepts the documented string form '<repo-relative path> sha256=<64 hex>'
    (docs/templates/verification-report.md, ncr.md; V&V section 7.4 format
    decision) and the flat-map form {path: ..., sha256: ...}. Returns None when
    the entry is malformed.
    """
    if isinstance(entry, str):
        match = ARTIFACT_STRING.match(entry.strip())
        return (match.group("path"), match.group("sha256").lower()) if match else None
    if isinstance(entry, dict):
        path = as_str(entry.get("path"))
        digest = as_str(entry.get("sha256")).lower()
        return (path, digest) if path else None
    return None


def check_artifacts(project: Project, code: str, where: str, artifacts: list[Any]) -> None:
    """Every artifact entry names an existing file whose SHA-256 equals the listed hash."""
    for entry in artifacts:
        parsed = artifact_path_and_hash(entry)
        if parsed is None:
            project.violation(code, where, f"artifact entry {entry!r} is not '<path> sha256=<64 hex>' or a path/sha256 map")
            continue
        path, expected = parsed
        file = project.root / path
        if not file.is_file():
            project.violation(code, where, f"artifact '{path}' does not exist")
            continue
        actual = hashlib.sha256(file.read_bytes()).hexdigest()
        if expected != actual:
            project.violation(code, where, f"artifact '{path}' SHA-256 is {actual[:12]}..., front matter says {expected[:12] or '(none)'}...")


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def load_reports(project: Project) -> None:
    reports_dir = project.root / REPORTS_DIR
    if not reports_dir.is_dir():
        return
    project.reports_present = True
    for path in sorted(reports_dir.glob("TC-*.md")):
        location = rel(path, project.root)
        front = parse_front_matter(path.read_text(encoding="utf-8"))
        if front is None or not isinstance(front.get("test_case"), str):
            project.violation("REPORT_FRONT_MATTER", location, "missing YAML front matter with a test_case field")
            continue
        run = str(front.get("run", ""))
        expected_name = f"{front['test_case']}-r{run}.md"
        if not REPORT_FILE.match(path.name) or path.name != expected_name:
            project.violation("REPORT_ID_FORMAT", location, f"file name should be {expected_name}")
        artifacts = artifact_entries(front)
        project.reports.append(
            Report(
                file=location,
                test_case=front["test_case"],
                run=run,
                requirement_ids=as_str_list(front.get("requirement_ids")),
                validates=as_str_list(front.get("validates")),
                credit=front.get("credit") is True,
                result=as_str(front.get("result")),
                date=str(front.get("date") or ""),
                ncr_ids=as_str_list(front.get("ncr_ids")),
                artifacts=artifacts,
            )
        )


def load_project(root: Path) -> Project:
    project = Project(root=root)
    project.req_id_re = schema_id_pattern(root, REQ_SCHEMA, "requirements", DEFAULT_REQ_ID_PATTERN, project)
    project.tc_id_re = schema_id_pattern(root, TC_SCHEMA, "test_cases", DEFAULT_TC_ID_PATTERN, project)
    cache: dict[Path, Any] = {}
    load_requirements(project, cache)
    load_test_cases(project, cache)
    load_upstream(project, cache)
    load_hazards(project, cache)
    load_ncrs(project)
    load_reports(project)
    return project


# ----------------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------------


def resolve_source(project: Project, source_id: str) -> bool | None:
    """True if the id exists upstream, False if it does not, None if it cannot be checked."""
    lookups: tuple[tuple[re.Pattern[str], set[str] | None], ...] = (
        (SI_ID, project.stakeholder_inputs),
        (NGO_ID, project.expectations),
        (MOE_ID, project.expectations),
        (CON_ID, project.expectations),
        (OPS_ID, project.conops_scenarios),
        (ADR_ID, project.adrs),
        (TS_ID, project.trade_studies),
    )
    for pattern, universe in lookups:
        if pattern.match(source_id):
            return None if universe is None else source_id in universe
    regulation = REGULATION_ID.match(source_id)
    if regulation:
        return None if project.regulations is None else regulation.group(1) in project.regulations
    return None


def upstream_name(source_id: str) -> str:
    if SI_ID.match(source_id):
        return str(STAKEHOLDER_INPUTS)
    if NGO_ID.match(source_id) or MOE_ID.match(source_id) or CON_ID.match(source_id):
        return str(EXPECTATIONS)
    if OPS_ID.match(source_id):
        return str(CONOPS)
    if ADR_ID.match(source_id):
        return str(ADR_DIR)
    if TS_ID.match(source_id):
        return str(TRADE_STUDY_DIR)
    if REGULATION_ID.match(source_id):
        return str(REGULATORY_DIR)
    return ""


def check_parents(project: Project) -> None:
    reqs = project.requirements
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        if req.parent_id is not None:
            if req.module == L1_MODULE:
                project.violation("L1_PARENT_NOT_NULL", where, f"SYS requirement has parent_id '{req.parent_id}'; L1 requirements trace to L0 through source_ids and carry parent_id null")
            if req.parent_id == req.id:
                project.violation("PARENT_UNRESOLVED", where, "parent_id refers to itself")
            elif req.parent_id not in reqs:
                project.violation("PARENT_UNRESOLVED", where, f"parent_id '{req.parent_id}' does not exist")
            else:
                parent = reqs[req.parent_id]
                if req.id not in parent.child_ids:
                    project.violation("CHILD_INVERSE", where, f"parent {req.parent_id} does not list {req.id} in child_ids")
                if req.status in ACTIVE_OR_LATER and parent.status == "Draft":
                    project.violation("CHILD_AHEAD_OF_PARENT", where, f"status {req.status} but parent {parent.id} is Draft")
        elif req.module != L1_MODULE and not req.is_retired:
            if not SELF_DERIVED.search(req.rationale):
                project.violation("PARENT_MISSING", where, "parent_id is null and the rationale does not say self-derived; an L2 requirement is allocated from a parent or is self-derived (02 section 2.3)")
            else:
                problems: list[str] = []
                if not req.rationale.startswith(SELF_DERIVED_PREFIX):
                    problems.append(f"rationale does not begin with '{SELF_DERIVED_PREFIX}'")
                if not any(DECISION_SOURCE_ID.match(s) for s in req.source_ids) and not req.hazard_ids:
                    problems.append("neither an ADR-/TS- source id nor a hazard id records the derivation")
                if problems:
                    project.violation("SELF_DERIVED_UNSUPPORTED", where, "; ".join(problems))
        for child_id in req.child_ids:
            if child_id not in reqs:
                project.violation("CHILD_INVERSE", where, f"child_ids names '{child_id}', which does not exist")
            elif reqs[child_id].parent_id != req.id:
                project.violation("CHILD_INVERSE", where, f"child {child_id} has parent_id '{reqs[child_id].parent_id}', not {req.id}")
        seen = {req.id}
        cursor = req.parent_id
        while cursor is not None and cursor in reqs:
            if cursor in seen:
                project.violation("PARENT_CYCLE", where, f"parent chain revisits {cursor}")
                break
            seen.add(cursor)
            cursor = reqs[cursor].parent_id


def check_sources(project: Project) -> None:
    unresolvable: dict[str, list[str]] = defaultdict(list)
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        for source_id in req.source_ids:
            resolved = resolve_source(project, source_id)
            if resolved is False:
                hint = "; add the section to the corpus or correct the clause" if REGULATION_ID.match(source_id) else ""
                project.violation("SOURCE_UNRESOLVED", where, f"source id '{source_id}' not found in {upstream_name(source_id)}{hint}")
            elif resolved is None:
                upstream = upstream_name(source_id)
                if upstream:
                    unresolvable[upstream].append(f"{req.id}:{source_id}")
                else:
                    project.warning("SOURCE_FORMAT_UNKNOWN", where, f"source id '{source_id}' matches no known scheme")
        if req.module == L1_MODULE and not req.is_retired:
            if not req.source_ids:
                project.violation("SOURCE_L0_MISSING", where, "SYS requirement has no source id (02 section 2.3: at least one L0 source)")
            elif project.expectations is not None and not any(L0_SOURCE_ID.match(s) for s in req.source_ids):
                project.violation("SOURCE_L0_MISSING", where, f"SYS requirement cites no NGO-, MOE-, CON- or OPS- id although {EXPECTATIONS} exists")
        for mop_id in req.mop_ids:
            if not (MOP_ID.match(mop_id) or TPM_ID.match(mop_id)):
                project.warning("SOURCE_FORMAT_UNKNOWN", where, f"mop_ids entry '{mop_id}' matches neither MOP-NNN nor TPM-NNN")
            elif project.measures is None:
                unresolvable[str(MEASURES)].append(f"{req.id}:{mop_id}")
            elif mop_id not in project.measures:
                project.warning("MOP_UNRESOLVED", where, f"mop_ids entry '{mop_id}' is not in {MEASURES} mops[] or tpms[]")
    for entry in sorted(project.expectation_entries.values(), key=lambda e: e.id):
        # L0 entries cite SI-NNN and 47 CFR clauses (docs/requirements/l0-stakeholder/schema.json); T-07 resolution applies.
        for source_id in entry.source_ids:
            resolved = resolve_source(project, source_id)
            if resolved is False:
                project.violation("SOURCE_UNRESOLVED", f"{EXPECTATIONS} {entry.id}", f"source id '{source_id}' not found in {upstream_name(source_id)}")
            elif resolved is None and upstream_name(source_id):
                unresolvable[upstream_name(source_id)].append(f"{entry.id}:{source_id}")
    for name, source_id in stakeholder_sources(project):
        # T-21: stakeholder sources that cannot be checked join the same one-per-file warning.
        if resolve_source(project, source_id) is None and upstream_name(source_id):
            unresolvable[upstream_name(source_id)].append(f"{name}:{source_id}")
    for upstream, refs in sorted(unresolvable.items()):
        project.warning("SOURCE_FILE_MISSING", upstream, f"absent; {len(refs)} reference(s) not checked: {', '.join(refs)}")


def stakeholder_sources(project: Project) -> list[tuple[str, str]]:
    """(name, source id) of every stakeholders entry of expectations.json (02 section 3.0)."""
    data = project.expectations_raw
    entries = data.get("stakeholders") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        return []
    return [(as_str(e.get("name")) or f"stakeholders[{i}]", s) for i, e in enumerate(entries) if isinstance(e, dict) for s in as_str_list(e.get("source_ids"))]


def check_tags(project: Project) -> None:
    """Tags with obligations (02 section 2.3): safety, regulatory, interface."""
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        if TAG_SAFETY in req.tags and not req.hazard_ids:
            project.violation("SAFETY_TAG_NO_HAZARD", where, "tag safety but hazard_ids is empty")
        if TAG_REGULATORY in req.tags and not any(REGULATION_ID.match(s) for s in req.source_ids):
            project.violation("REGULATORY_TAG_NO_CLAUSE", where, "tag regulatory but no 47 CFR clause (Part 1, 2, 15 or 97) in source_ids")
        if TAG_INTERFACE in req.tags and not any(ICD_ID.match(d) for d in req.design_refs):
            project.warning("INTERFACE_TAG_NO_ICD", where, "tag interface but no ICD-<A>-<B> id in design_refs")


def check_hazards(project: Project) -> None:
    """02 T-08 and 04 rule 7.3.6 on the hazard trace of 04 section 3.

    A requirement traces to a hazard through its own hazard_ids or through
    docs/safety/hazards.json (a hazard's requirement_ids or a control's
    control_req_ids; charter section 7). The verification rule runs on that
    union, so a one-directional trace cannot skip SWE-192.
    """
    unresolvable: list[str] = []
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        for hz_id in req.hazard_ids:
            if not HZ_ID.match(hz_id):
                project.violation("HAZARD_ID_FORMAT", where, f"hazard id '{hz_id}' does not match HZ-NNN")
                continue
            if not project.hazards_present:
                unresolvable.append(f"{req.id}:{hz_id}")
            elif hz_id not in project.hazards:
                project.violation("HAZARD_UNRESOLVED", where, f"hazard '{hz_id}' not defined in {HAZARDS}")
            else:
                listed = project.hazards[hz_id].requirement_ids
                if listed is not None and req.id not in listed:
                    project.warning("HAZARD_INVERSE", where, f"{hz_id} does not list {req.id} in its requirement_ids")
        if req.is_retired:
            continue
        untraced = [hz for hz in project.hazards_naming(req.id) if hz not in req.hazard_ids]
        if untraced and project.is_software(req):
            project.violation("HAZARD_CONTROL_UNTRACED", where, f"named by {', '.join(untraced)} in {HAZARDS} but hazard_ids does not list {'it' if len(untraced) == 1 else 'them'}; a software hazard control carries the hazard id (SWE-052 Table 1 row 2, bidirectional)")
        trace = project.hazard_trace(req)
        if trace:
            check_hazard_verification(project, req, where, trace)
    if unresolvable:
        project.warning("HAZARD_FILE_MISSING", str(HAZARDS), f"absent; {len(unresolvable)} hazard reference(s) not checked: {', '.join(unresolvable)}")
    for hazard in sorted(project.hazards.values(), key=lambda h: h.id):
        where = f"{HAZARDS} {hazard.id}"
        for req_id in hazard.requirement_ids or []:
            req = project.requirements.get(req_id)
            if req is None:
                project.violation("HAZARD_UNRESOLVED", where, f"requirement_ids names '{req_id}', which does not exist")
            elif hazard.id not in req.hazard_ids and not (project.is_software(req) and not req.is_retired):
                # For SW and SW-<SUB> the same disagreement is the violation HAZARD_CONTROL_UNTRACED.
                project.warning("HAZARD_INVERSE", where, f"{req_id} does not list {hazard.id} in hazard_ids")
        if hazard.control_req_ids is not None:
            for req_id in sorted(set(hazard.control_req_ids)):
                if req_id not in project.requirements:
                    project.violation("HAZARD_UNRESOLVED", where, f"a control's control_req_ids names '{req_id}', which does not exist")
            if hazard.requirement_ids is not None and set(hazard.control_req_ids) != set(hazard.requirement_ids):
                project.warning("HAZARD_INVERSE", where, "requirement_ids is not the union of the controls' control_req_ids")


def on_target_cases(project: Project, req: Requirement) -> list[TestCase]:
    """Passed closing cases of type Bench or OnAir with a credited report citing req (01 section 8.6)."""
    cases = [tc for tc in project.closing_cases(req) if tc.type in ON_TARGET_TYPES and tc.status == "Passed"]
    if project.reports_present:
        cases = [tc for tc in cases if credit_reports_for(project, req, tc)]
    return cases


def check_hazard_verification(project: Project, req: Requirement, where: str, trace: list[str]) -> None:
    """04 rule 7.3.6: a hazard-tracing requirement closes by Test.

    Software modules (SW, SW-<SUB>): SWE-192, no exception, and a Closed
    requirement also has on-target (Bench or OnAir) evidence. Any other module
    (04 rule 7.3.6, the project extension of SWE-192) may use method Analysis
    when its verification_note begins 'Analysis accepted per RSK-NNN' and that
    risk exists in docs/risk/register.json.
    """
    hazards = ", ".join(trace)
    software = project.is_software(req)
    basis = "SWE-192" if software else "04 rule 7.3.6, the project extension of SWE-192 to every hazard-control requirement"
    closing_tests = [tc for tc in project.closing_cases(req) if tc.verification_method == "Test"]
    if software and req.status == "Closed" and not on_target_cases(project, req):
        project.violation("HAZARD_REQ_NOT_ON_TARGET", where, f"traces to {hazards}, status Closed, but no Passed closing case of type Bench or OnAir with a credited report cites it (SWE-192 as 01 section 8.6 applies it at SAR: test on the target)")
    if req.verification_method == "Test":
        if not closing_tests:
            project.violation("HAZARD_REQ_NOT_TESTED", where, f"traces to {hazards} with method Test but no closing case of method Test cites it ({basis})")
        return
    if software:
        project.violation("HAZARD_REQ_NOT_TESTED", where, f"software requirement traces to {hazards} but has method {req.verification_method or '(unset)'}; SWE-192 requires Test with no exception")
        return
    note = HAZARD_ANALYSIS_NOTE.match(req.verification_note)
    if req.verification_method != "Analysis" or note is None:
        project.violation("HAZARD_REQ_NOT_TESTED", where, f"traces to {hazards} but has method {req.verification_method or '(unset)'} and no verification_note beginning 'Analysis accepted per RSK-NNN' with method Analysis ({basis})")
        return
    risk_id = note.group(1)
    if project.risks is None:
        project.warning("RISK_FILE_MISSING", str(RISKS), f"absent; {req.id} cites {risk_id} for the Analysis exception and it cannot be resolved yet")
    elif risk_id not in project.risks:
        project.violation("HAZARD_REQ_NOT_TESTED", where, f"traces to {hazards} by Analysis accepted per {risk_id}, but {risk_id} does not exist in {RISKS} ({basis})")


def credit_reports_for(project: Project, req: Requirement, tc: TestCase) -> list[Report]:
    return [r for r in project.reports_for(tc.id) if r.is_credit_pass and req.id in r.requirement_ids]


def check_verification(project: Project) -> None:
    needs_reports = False
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        if req.is_retired:
            continue  # T-19: retired requirements are checked by check_retired only
        tcs = project.live_tcs_for(req.id)
        closing = project.closing_cases(req)
        if req.status in REQ_STATUSES_NEEDING_TC and not tcs:
            project.violation("REQ_UNVERIFIED", where, f"status {req.status} but no live test case cites this requirement")
        elif tcs and not closing:
            project.violation("REQ_NO_CLOSING_CASE", where, f"no citing case has verification_method {req.verification_method or '(unset)'}; all {len(tcs)} are supporting only")
        if req.status in EVIDENCE_STATUSES and not req.is_retired:
            needs_reports = True
            passed = [tc for tc in closing if tc.status == "Passed"]
            not_passed = [f"{tc.id} ({tc.status or 'status unset'})" for tc in closing if tc.status != "Passed"]
            failed = [tc.id for tc in tcs if tc.status == "Failed"]
            if not passed:
                project.violation("VERIFIED_WITHOUT_EVIDENCE", where, f"status {req.status} but no Passed closing case with verification_method {req.verification_method or '(unset)'}")
            else:
                if not_passed:
                    project.violation("VERIFIED_WITHOUT_EVIDENCE", where, f"status {req.status} but closing case(s) not Passed: {', '.join(not_passed)} (every closing case is Passed, 02 T-11; 04 rule 7.3.4)")
                uncredited = [tc.id for tc in passed if not credit_reports_for(project, req, tc)]
                if project.reports_present and uncredited:
                    project.violation("VERIFIED_WITHOUT_EVIDENCE", where, f"status {req.status} but no report under {REPORTS_DIR} with credit true and result Pass cites this requirement for closing case(s) {', '.join(uncredited)}")
            if failed:
                project.violation("VERIFIED_WITHOUT_EVIDENCE", where, f"status {req.status} but cited by Failed case(s): {', '.join(failed)}")
            open_ncrs = [n.id for n in project.ncrs_for(req.id) if n.status != NCR_CLOSED]
            if open_ncrs:
                project.violation("VERIFIED_WITH_OPEN_NCR", where, f"status {req.status} but cited by non-Closed NCR(s): {', '.join(open_ncrs)}")
        if req.status == "Closed" and not req.is_retired:
            check_closed(project, req, where)
    for tc in project.ordered_test_cases():
        where = f"{tc.file} {tc.id}"
        for req_id in tc.requirement_ids:
            if req_id not in project.requirements:
                project.violation("TC_REQ_UNRESOLVED", where, f"requirement '{req_id}' does not exist")
        if tc.is_retired:
            continue
        allowed = TYPES_FOR_METHOD.get(tc.verification_method)
        if allowed is not None and tc.type and tc.type not in allowed:
            project.violation("TC_TYPE_METHOD", where, f"type {tc.type} is not an evidence class of method {tc.verification_method} ({', '.join(allowed)})")
        if tc.status == "Passed":
            needs_reports = True
            if project.reports_present and not any(r.is_credit_pass for r in project.reports_for(tc.id)):
                project.violation("TC_STATUS_EVIDENCE", where, f"status Passed but no report under {REPORTS_DIR} with credit true and result Pass")
        if tc.status == "Failed":
            needs_reports = True
            if project.reports_present and not any(r.result == "Fail" for r in project.reports_for(tc.id)):
                project.violation("TC_STATUS_EVIDENCE", where, f"status Failed but no report under {REPORTS_DIR} with result Fail names this case")
            if not any(tc.id in ncr.test_case_ids for ncr in project.ncrs.values()):
                project.warning("FAILED_TC_WITHOUT_NCR", where, "status Failed but no NCR cites this test case")
        if tc.type in BENCH_TYPES:
            missing = [line for line in BENCH_SETUP_LINES if line not in tc.setup]
            if not tc.instruments or missing:
                detail = []
                if not tc.instruments:
                    detail.append("instruments is empty")
                if missing:
                    detail.append("setup lacks " + ", ".join(missing))
                project.violation("TC_SETUP_INCOMPLETE", where, f"{tc.type} case: " + "; ".join(detail))
        if tc.module == VALIDATION_MODULE:
            check_validation_targets(project, tc, where)
    if needs_reports and not project.reports_present:
        project.warning("REPORTS_DIR_MISSING", str(REPORTS_DIR), "absent; Passed and Failed cases and Verified requirements are checked against case status only")


def check_closed(project: Project, req: Requirement, where: str) -> None:
    """04 section 5.3: Closed needs the SAR decision memo and Validated dependent rows."""
    if not project.sar_memo_present:
        project.violation("CLOSED_WITHOUT_SAR", where, f"status Closed but {SAR_DECISION_MEMO} does not exist")
    dependent = sorted({target for tc in project.live_tcs_for(req.id) if tc.module == VALIDATION_MODULE for target in tc.validation_targets})
    not_validated = [target for target in dependent if project.validation_row(target)[1] != "Validated"]
    if not_validated:
        project.violation("CLOSED_WITHOUT_SAR", where, f"status Closed but dependent validation row(s) not Validated: {', '.join(not_validated)}")


def check_validation_targets(project: Project, tc: TestCase, where: str) -> None:
    """04 rule 7.3.5: every target after 'Validates:' exists, and at least one is named."""
    targets = tc.validation_targets
    if not targets:
        project.violation("VAL_TARGET_MISSING", where, "setup names no OPS-NNN or MOE-NNN after 'Validates:'")
        return
    resolved = {t: resolve_source(project, t) for t in targets}
    missing = [t for t, known in resolved.items() if known is False]
    if missing and not any(known for known in resolved.values()):
        project.violation("VAL_TARGET_MISSING", where, f"none of {', '.join(targets)} exists in {CONOPS} or {EXPECTATIONS}")
        return
    for target in missing:
        project.violation("VAL_TARGET_UNRESOLVED", where, f"validation target '{target}' after 'Validates:' does not exist in {upstream_name(target)}; it would drop out of the validation matrix")


def check_retired(project: Project) -> None:
    """02 T-19 and T-10: retired items keep their id and nothing live depends on them."""
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        if RETIRED_TAG in req.tags and req.status not in ("Closed", RETIRED):
            project.violation("RETIRED_INCONSISTENT", where, f"tag {RETIRED_TAG} on status {req.status or '(unset)'}; retirement is status Closed with tag {RETIRED_TAG} (02 section 11.3)")
        if not req.is_retired:
            continue
        label = "status Retired" if req.status == RETIRED else f"status Closed with tag {RETIRED_TAG}"
        if not req.rationale.startswith(RETIRED_PREFIX):
            project.violation("RETIRED_INCONSISTENT", where, f"{label} but rationale does not begin '{RETIRED_PREFIX}'")
        live_children = [c.id for c in project.children_of(req.id) if not c.is_retired]
        if live_children:
            project.violation("RETIRED_INCONSISTENT", where, f"{label} but child(ren) not retired: {', '.join(live_children)}")
        live_cases = [tc.id for tc in project.tcs_for(req.id) if not tc.is_retired]
        if live_cases:
            project.violation("RETIRED_INCONSISTENT", where, f"{label} but cited by case(s) not retired: {', '.join(live_cases)}")
    for tc in project.ordered_test_cases():
        if not tc.is_retired:
            continue
        where = f"{tc.file} {tc.id}"
        if not tc.setup.lstrip().startswith(RETIRED_PREFIX):
            project.violation("RETIRED_INCONSISTENT", where, f"status {tc.status} (retired) but setup does not begin '{RETIRED_PREFIX}'")
        live = [rid for rid in tc.requirement_ids if rid in project.requirements and not project.requirements[rid].is_retired]
        successor = SUPERSEDED_BY_CASE.search(tc.setup)
        if live and successor is None:
            project.violation("RETIRED_INCONSISTENT", where, f"retired case cites live requirement(s) {', '.join(live)} and names no superseding case ('superseded by TC-...') in setup")
        elif live and successor is not None and successor.group(1) not in project.test_cases:
            project.violation("RETIRED_INCONSISTENT", where, f"superseding case {successor.group(1)} named in setup does not exist")


def check_text_rules(project: Project) -> None:
    for req in project.ordered_requirements():
        where = f"{req.file} {req.id}"
        fields = {"title": req.title, "description": req.description, "rationale": req.rationale, "verification_note": req.verification_note}
        if req.tbr is not None:
            fields["tbr.plan"] = as_str(req.tbr.get("plan"))
        for name, text in fields.items():
            if TBD_WORD.search(text):
                project.violation("TBD_PRESENT", where, f"'TBD' in {name}")
        if req.tbr is None and any(TBR_WORD.search(text) for text in fields.values()):
            project.violation("TBR_UNDOCUMENTED", where, "'TBR' appears in text but there is no tbr object")
        if req.tbr is not None:
            if TBR_MARK not in req.description:
                project.violation("TBR_UNMARKED", where, f"tbr object present but description lacks '{TBR_MARK}' after the estimated value")
            if req.status in TBR_FINAL_STATUSES:
                project.violation("TBR_ON_FINAL_STATUS", where, f"tbr object present while status is {req.status}")
            close_by = as_str(req.tbr.get("close_by"))
            allowed = TBR_CLOSE_BY_L1 if req.module == L1_MODULE else TBR_CLOSE_BY_L2
            if close_by and close_by not in allowed:
                project.violation("TBR_CLOSE_BY", where, f"tbr.close_by {close_by} is later than allowed for module {req.module} ({'/'.join(allowed)})")
        if not req.rationale.strip():
            project.violation("RATIONALE_EMPTY", where, "rationale is empty")
        shall_count = len(SHALL_WORD.findall(req.description))
        if req.description and shall_count != 1:
            project.violation("SHALL_COUNT", where, f"description contains {shall_count} 'shall' (exactly one required)")
        modal = sorted({m.group(0).lower() for m in MODAL_WORDS.finditer(req.description)})
        if modal:
            project.violation("MODAL_IN_DESCRIPTION", where, f"description uses WR-07 group A word(s): {', '.join(modal)}")
        if SHALL_WORD.search(req.title):
            project.violation("SHALL_IN_TITLE", where, "'shall' in title")
        words = len(req.description.split())
        if words > MAX_DESCRIPTION_WORDS:
            project.warning("DESCRIPTION_LENGTH", where, f"description has {words} words (limit {MAX_DESCRIPTION_WORDS})")
        weak = sorted({m.group(0).lower() for m in UNVERIFIABLE_WORDS.finditer(req.description)})
        if weak:
            project.warning("UNVERIFIABLE_WORD", where, f"description uses: {', '.join(weak)}")
    for tc in project.ordered_test_cases():
        where = f"{tc.file} {tc.id}"
        for name, text in tc.text_fields.items():
            if TBD_WORD.search(text):
                project.violation("TBD_PRESENT", where, f"'TBD' in {name}")
    for entry in sorted(project.expectation_entries.values(), key=lambda e: e.id):
        for name, text in entry.text_fields.items():
            if TBD_WORD.search(text):
                project.violation("TBD_PRESENT", f"{EXPECTATIONS} {entry.id}", f"'TBD' in {name}")
    for location, rows in sorted(project.icd_tables.items()):
        for number, line in rows:
            if tbd_placeholder(line):
                project.violation("TBD_PRESENT", f"{location}:{number}", "'TBD' in a definition-table row; write the estimate with '(TBR)' and a TBR table row (02 section 3.5)")
    for location, rows in sorted(project.baselined_lines.items()):
        for number, line in rows:
            if tbd_placeholder(line):
                project.violation("TBD_PRESENT", f"{location}:{number}", "'TBD' in a product of the functional baseline (charter section 3); no TBD in a baselined document and a TBD is never a lien (charter section 7; 01 section 12.2): state the value, or an estimate marked (TBR) with owner, plan and close-by")


def tbd_placeholder(line: str) -> bool:
    """True when a Markdown line holds TBD as a placeholder, not as a mention of the policy terms."""
    return bool(TBD_WORD.search(TBD_MENTION.sub(" ", line)))


def check_expectations(project: Project) -> None:
    """02 T-21 (structure of expectations.json) and the MOE part of T-20."""
    if not project.expectation_entries:
        return
    where_file = str(EXPECTATIONS)
    entries = project.expectation_entries
    needs = project.expectations_of_kind("Need")
    if len(needs) != 1:
        project.violation("EXPECTATIONS_INCONSISTENT", where_file, f"{len(needs)} entries of kind Need ({', '.join(n.id for n in needs) or 'none'}); exactly one is required")
    need_id = needs[0].id if len(needs) == 1 else None
    unresolved_ops: list[str] = []
    for entry in sorted(entries.values(), key=lambda e: e.id):
        where = f"{where_file} {entry.id}"
        parent = entries.get(entry.parent_id) if entry.parent_id else None
        if entry.kind == "Goal":
            if entry.parent_id is None or (need_id is not None and entry.parent_id != need_id) or (parent is not None and parent.kind != "Need"):
                project.violation("EXPECTATIONS_INCONSISTENT", where, f"Goal parent_id '{entry.parent_id}' is not the Need")
        elif entry.kind == "Objective":
            if parent is None or parent.kind != "Goal":
                project.violation("EXPECTATIONS_INCONSISTENT", where, f"Objective parent_id '{entry.parent_id}' is not a Goal")
        elif entry.kind == "MOE":
            for ngo_id in entry.ngo_ids:
                target = entries.get(ngo_id)
                if target is None or target.kind not in ("Goal", "Objective"):
                    project.violation("EXPECTATIONS_INCONSISTENT", where, f"ngo_ids entry '{ngo_id}' is not a Goal or Objective")
            if project.conops_scenarios is not None and not entry.ops_ids:
                project.warning("MOE_WITHOUT_OPS", where, f"MOE has no ops_ids entry although {CONOPS} exists")
        for ops_id in entry.ops_ids:
            if project.conops_scenarios is None:
                unresolved_ops.append(f"{entry.id}:{ops_id}")
            elif ops_id not in project.conops_scenarios:
                project.violation("EXPECTATIONS_INCONSISTENT", where, f"ops_ids entry '{ops_id}' is not a heading of {CONOPS}")
    if unresolved_ops:
        project.warning("SOURCE_FILE_MISSING", str(CONOPS), f"absent; {len(unresolved_ops)} ops_ids reference(s) not checked: {', '.join(unresolved_ops)}")


def check_stakeholders(project: Project) -> None:
    """02 T-21, stakeholder part, with the stakeholder-name part of T-03 (plain-run severity Warning).

    02 section 3.0: the stakeholders array of expectations.json exists, holds at least
    one entry of role customer, user and regulator, keys its entries by unique name,
    and every source_ids entry resolves. Not evaluated while expectations.json is
    absent or does not parse (SCHEMA_INVALID reports the latter). The schema itself
    requires the array once baseline is set; the Error severity of the gate column
    comes with --gate.
    """
    data = project.expectations_raw
    if not isinstance(data, dict):
        return
    where_file = f"{EXPECTATIONS} stakeholders"
    entries = data.get("stakeholders")
    if not isinstance(entries, list) or not entries:
        state = "absent" if entries is None else ("empty" if isinstance(entries, list) else "not an array")
        project.warning(
            "STAKEHOLDERS_MISSING", where_file,
            f"stakeholders array {state}; 02 section 3.0 requires the identified stakeholders with at least one entry of role "
            f"{', '.join(REQUIRED_STAKEHOLDER_ROLES)}, and the schema requires the array once baseline is set",
        )
        return
    roles: set[str] = set()
    first_index: dict[str, int] = {}
    for index, raw in enumerate(entries):
        if not isinstance(raw, dict):
            continue  # the schema reports a malformed entry
        name, role = as_str(raw.get("name")), as_str(raw.get("role"))
        where = f"{where_file}[{index}] {name or '(no name)'}"
        roles.add(role)
        if name in first_index:
            project.warning("STAKEHOLDERS_MISSING", where, f"name already used by stakeholders[{first_index[name]}]; entries are keyed by unique name (02 section 3.0; T-03)")
        elif name:
            first_index[name] = index
        for source_id in as_str_list(raw.get("source_ids")):
            resolved = resolve_source(project, source_id)
            upstream = upstream_name(source_id)
            if resolved is False:
                project.warning("STAKEHOLDERS_MISSING", where, f"source id '{source_id}' not found in {upstream}")
            elif resolved is None and not upstream:
                project.warning("STAKEHOLDERS_MISSING", where, f"source id '{source_id}' matches no known scheme")
            # resolved None with a known upstream: the file is absent; check_sources reports SOURCE_FILE_MISSING
    missing = [r for r in REQUIRED_STAKEHOLDER_ROLES if r not in roles]
    if missing:
        project.warning("STAKEHOLDERS_MISSING", where_file, f"no entry of role {', '.join(missing)}; 02 section 3.0 requires at least one of each of {', '.join(REQUIRED_STAKEHOLDER_ROLES)}")


def check_allocation(project: Project) -> None:
    """02 T-18 at SRR (plain-run severity Warning; Error from PDR under --gate, not yet implemented).

    Every Draft or Active SYS requirement names at least one receiving L2 module
    through child_ids (or a child's parent_id) naming a live L2 requirement, or
    through a docs/design/allocation.json record that lists it under an L2 module
    (02 section 2.3). Each gap is one finding on the requirement; the reviewer
    confirms or corrects it in V6. Retired requirements are excluded (T-19).
    """
    if project.allocation_error is not None:
        project.warning("SYS_UNALLOCATED", str(ALLOCATION), f"{project.allocation_error}; no allocation record is read, so only child_ids count for T-18")
    for req in project.live_requirements():
        if req.module != L1_MODULE or req.status not in REQ_STATUSES_NEEDING_TC:
            continue
        if project.receiving_modules(req):
            continue
        named = sorted(set(req.child_ids) | {c.id for c in project.children_of(req.id)})
        parts = ["no child is a live L2 requirement" + (f" (children named: {', '.join(named)})" if named else " (child_ids empty)")]
        listed = sorted(project.allocation_modules.get(req.id, set()))
        if not project.allocation_present:
            parts.append(f"{ALLOCATION} is absent")
        elif project.allocation_error is not None:
            parts.append(f"{ALLOCATION} does not parse")
        elif listed:
            parts.append(f"{ALLOCATION} lists it only under {', '.join(listed)}, not an L2 module")
        else:
            parts.append(f"{ALLOCATION} lists it under no module")
        project.warning(
            "SYS_UNALLOCATED", f"{req.file} {req.id}",
            f"{req.status} SYS requirement names no receiving L2 module: {'; '.join(parts)}; the reviewer confirms or corrects the gap in V6 (02 section 2.3, T-18)",
        )


def check_l0_coverage(project: Project) -> None:
    """02 T-20 (plain-run severity W): core inputs, Baselined Objectives and scenarios are covered.

    Evaluated once at least one requirement exists; an empty requirement set
    has nothing to cover yet.
    """
    reqs = project.live_requirements()
    if not reqs:
        return
    sys_sources = {s for r in reqs if r.module == L1_MODULE for s in r.source_ids}
    all_sources = {s for r in reqs for s in r.source_ids}
    for si_id in sorted(project.core_inputs):
        if si_id not in sys_sources:
            project.warning("CORE_SI_UNCOVERED", f"{STAKEHOLDER_INPUTS} {si_id}", "core (bold) stakeholder input is cited by no SYS requirement")
    moe_ngo_ids = {n for e in project.expectations_of_kind("MOE") for n in e.ngo_ids}
    for objective in project.expectations_of_kind("Objective"):
        if objective.status == EXPECTATION_STATUS_BASELINED and objective.id not in sys_sources and objective.id not in moe_ngo_ids:
            project.warning("OBJECTIVE_UNCOVERED", f"{EXPECTATIONS} {objective.id}", "Baselined Objective is cited by no SYS requirement and no MOE")
    val_targets = {t for tc in project.validation_cases() for t in tc.validation_targets}
    for ops_id in sorted(project.conops_scenarios or set()):
        if ops_id not in all_sources and ops_id not in val_targets:
            project.warning("OPS_UNCITED", f"{CONOPS} {ops_id}", "scenario is cited by no requirement source_ids and no TC-VAL case")


def check_ncrs(project: Project) -> None:
    """04 rule 7.3.8, SWE-052 Table 1 row 6 and the SWE-202 severity levels of 04 section 10.3."""
    for ncr in sorted(project.ncrs.values(), key=lambda n: n.id):
        where = f"{ncr.file} {ncr.id}"
        if ncr.severity not in NCR_SEVERITIES:
            project.violation("NCR_FIELD_INVALID", where, f"severity '{ncr.severity or '(unset)'}' is not one of {', '.join(NCR_SEVERITIES)} (SWE-202; 04 section 10.3)")
        if ncr.status not in NCR_STATUSES:
            project.violation("NCR_FIELD_INVALID", where, f"status '{ncr.status or '(unset)'}' is not one of {', '.join(NCR_STATUSES)} (04 section 10.7)")
        if ncr.classification and ncr.classification not in NCR_CLASSIFICATIONS:
            project.violation("NCR_FIELD_INVALID", where, f"classification '{ncr.classification}' is not product or procedure (docs/templates/ncr.md)")
        if ncr.classification != "procedure" and ncr.severity != NCR_NO_REQUIREMENT_SEVERITY and not ncr.requirement_ids:
            derived = sorted({rid for tc_id in ncr.test_case_ids if tc_id in project.test_cases for rid in project.test_cases[tc_id].requirement_ids})
            hint = f"; its test cases cite {', '.join(derived)}" if derived else ""
            project.violation("NCR_NO_REQUIREMENT", where, f"product NCR of severity {ncr.severity or '(unset)'} cites no requirement in requirement_ids{hint} (SWE-052 Table 1 row 6)")
        for req_id in ncr.requirement_ids:
            if req_id not in project.requirements:
                project.violation("NCR_UNRESOLVED", where, f"requirement '{req_id}' does not exist")
        for tc_id in ncr.test_case_ids:
            if tc_id not in project.test_cases:
                project.violation("NCR_UNRESOLVED", where, f"test case '{tc_id}' does not exist")
        for hz_id in ncr.hazard_ids:
            if project.hazards_present and hz_id not in project.hazards:
                project.violation("NCR_UNRESOLVED", where, f"hazard '{hz_id}' does not exist")
        check_artifacts(project, "NCR_ARTIFACT", where, ncr.artifacts)


def check_reports(project: Project) -> None:
    for report in sorted(project.reports, key=lambda r: r.file):
        where = report.file
        tc = project.test_cases.get(report.test_case)
        if tc is None:
            project.violation("REPORT_UNRESOLVED", where, f"test case '{report.test_case}' does not exist")
        else:
            for req_id in report.requirement_ids:
                if req_id not in tc.requirement_ids:
                    project.violation("REPORT_UNRESOLVED", where, f"requirement '{req_id}' is not cited by {tc.id}")
            for target in report.validates:
                if target not in tc.validation_targets:
                    project.violation("REPORT_UNRESOLVED", where, f"validation target '{target}' is not named after 'Validates:' in {tc.id}")
        for ncr_id in report.ncr_ids:
            if ncr_id not in project.ncrs:
                project.violation("REPORT_UNRESOLVED", where, f"NCR '{ncr_id}' does not exist")
        check_artifacts(project, "REPORT_ARTIFACT", where, report.artifacts)


def run_checks(project: Project) -> None:
    check_parents(project)
    check_sources(project)
    check_tags(project)
    check_hazards(project)
    check_verification(project)
    check_retired(project)
    check_text_rules(project)
    check_expectations(project)
    check_stakeholders(project)
    check_allocation(project)
    check_l0_coverage(project)
    check_ncrs(project)
    check_reports(project)
    check_rendered(project)
    project.findings.sort(key=lambda f: (f.severity != VIOLATION, f.code, f.location, f.message))


# ----------------------------------------------------------------------------
# Rendering (02 section 8.1 --render): expectations.md and requirements.md
# ----------------------------------------------------------------------------

RENDER_COMMAND = ".venv/bin/python tools/traceability.py --render"
RENDER_MARK = "by `tools/traceability.py --render` (02 section 8.1)"


def md_text(value: Any) -> str:
    """A JSON value as one Markdown table cell or line."""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) or "-"
    if value is None or value == "":
        return "-"
    return cell(str(value))


def generated_line(json_rel: str, baseline: str | None = None) -> str:
    line = f"Generated from `{json_rel}` {RENDER_MARK}. Do not edit this file; edit the JSON and re-render with `{RENDER_COMMAND}`."
    if baseline is not None:
        line += f" Baseline: `{baseline}`."
    return line


def status_text(entry: dict[str, Any]) -> str:
    status = as_str(entry.get("status")) or "(unset)"
    retired_by = as_str(entry.get("retired_by"))
    return f"{status} (retired by {retired_by})" if retired_by else status


def render_expectations(project: Project) -> str | None:
    """expectations.md from expectations.json and the ConOps headings; None when the JSON is absent."""
    data = project.expectations_raw
    if not isinstance(data, dict) or not isinstance(data.get("ngos"), list):
        return None
    ngos = [e for e in data.get("ngos", []) if isinstance(e, dict)]
    moes = [e for e in data.get("moes", []) if isinstance(e, dict)]
    constraints = [e for e in data.get("constraints", []) if isinstance(e, dict)]
    everything = ngos + moes + constraints
    baseline = data.get("baseline")
    by_kind: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in ngos:
        by_kind[as_str(entry.get("kind"))].append(entry)
    moes_for: dict[str, list[str]] = defaultdict(list)
    for moe in moes:
        for ngo_id in as_str_list(moe.get("ngo_ids")):
            moes_for[ngo_id].append(as_str(moe.get("id")))
    cited: dict[str, list[str]] = defaultdict(list)
    for entry in everything:
        for source_id in as_str_list(entry.get("source_ids")):
            cited[source_id].append(as_str(entry.get("id")))
    statuses = counts_by_key(everything, "status")
    out = [
        "# cwht Stakeholder Expectations (L0)",
        "",
        generated_line(str(EXPECTATIONS), baseline if isinstance(baseline, str) else "none (pre-SRR)"),
        "",
        "Entries (02 section 3.2; SE HB 4.1.1.2.3, 4.1.1.2.6, 4.2.1.2.1): one Need; Goals that elaborate it; Objectives that set measurable targets for a Goal; "
        "Measures of Effectiveness stated from the owner's point of view; Constraints not open to trade. Expectations are not requirements and carry no `shall`. "
        f"`SI-NNN` ids are rows of `{STAKEHOLDER_INPUTS}`, `47CFR<part>.<section>` ids are clauses of the corpus `{REGULATORY_DIR}/`, and `OPS-NNN` ids are headings of `{CONOPS}`.",
        "",
        "## 1. Summary",
        "",
    ]
    out += table(
        ["Entry", "Count"],
        [
            ["Need", str(len(by_kind["Need"]))],
            ["Goals", str(len(by_kind["Goal"]))],
            ["Objectives", str(len(by_kind["Objective"]))],
            ["MOEs", str(len(moes))],
            ["Constraints", str(len(constraints))],
            *[[f"Entries with status {status}", str(n)] for status, n in statuses.items()],
            ["Distinct stakeholder inputs cited", str(sum(1 for s in cited if SI_ID.match(s)))],
            ["Distinct 47 CFR clauses cited", str(sum(1 for s in cited if REGULATION_ID.match(s)))],
        ],
    )
    out += ["", "## 2. Need, Goals and Objectives", ""]
    for need in by_kind["Need"] + by_kind["Goal"]:
        ident = as_str(need.get("id"))
        out += [
            f"### {ident} ({as_str(need.get('kind'))}): {as_str(need.get('title'))}",
            "",
            f"**Statement.** {as_str(need.get('statement'))}",
            "",
            f"**Rationale.** {as_str(need.get('rationale'))}",
            "",
            f"**Parent:** {md_text(need.get('parent_id'))}. **Sources:** {md_text(as_str_list(need.get('source_ids')))}. **MOEs:** {md_text(moes_for.get(ident, []))}. **Status:** {status_text(need)}.",
            "",
        ]
        objectives = [o for o in by_kind["Objective"] if o.get("parent_id") == ident]
        if need.get("kind") == "Goal":
            out += [f"Objectives under {ident}:", ""]
            out += table(
                ["ID", "Title", "Statement", "Rationale", "Sources", "MOEs", "Status"],
                ([as_str(o.get("id")), as_str(o.get("title")), as_str(o.get("statement")), as_str(o.get("rationale")), md_text(as_str_list(o.get("source_ids"))), md_text(moes_for.get(as_str(o.get("id")), [])), status_text(o)] for o in objectives),
            )
            out += [""]
    known_parents = {as_str(g.get("id")) for g in by_kind["Goal"]}
    stray = [o for o in by_kind["Objective"] if o.get("parent_id") not in known_parents]
    other_kinds = [e for e in ngos if as_str(e.get("kind")) not in NGO_KINDS]
    if stray or other_kinds:
        out += ["### Entries without a Goal parent or with an unknown kind", "", "Listed for completeness; `tools/traceability.py` reports them as EXPECTATIONS_INCONSISTENT (T-21).", ""]
        out += table(["ID", "Kind", "Parent", "Title", "Status"], ([as_str(e.get("id")), as_str(e.get("kind")), md_text(e.get("parent_id")), as_str(e.get("title")), status_text(e)] for e in stray + other_kinds))
        out += [""]
    out += ["## 3. Measures of Effectiveness", ""]
    out += table(
        ["ID", "Title", "Statement", "Success criterion", "Rationale", "NGOs", "Scenarios", "Sources", "Status"],
        ([as_str(m.get("id")), as_str(m.get("title")), as_str(m.get("statement")), as_str(m.get("success_criterion")), as_str(m.get("rationale")), md_text(as_str_list(m.get("ngo_ids"))), md_text(as_str_list(m.get("ops_ids"))), md_text(as_str_list(m.get("source_ids"))), status_text(m)] for m in moes),
    )
    out += ["", "## 4. Constraints", ""]
    out += table(
        ["ID", "Kind", "Title", "Statement", "Rationale (who imposes it, what relief exists)", "Sources", "Status"],
        ([as_str(c.get("id")), as_str(c.get("kind")), as_str(c.get("title")), as_str(c.get("statement")), as_str(c.get("rationale")), md_text(as_str_list(c.get("source_ids"))), status_text(c)] for c in constraints),
    )
    out += ["", "## 5. Cross-reference: sources to expectations", ""]
    out += table(["Source", "Cited by"], ([source, ", ".join(sorted(ids))] for source, ids in sorted(cited.items(), key=lambda kv: source_sort_key(kv[0]))))
    out += ["", "## 6. Cross-reference: ConOps scenarios to MOEs", ""]
    scenario_moes: dict[str, list[str]] = defaultdict(list)
    for moe in moes:
        for ops_id in as_str_list(moe.get("ops_ids")):
            scenario_moes[ops_id].append(as_str(moe.get("id")))
    scenarios = sorted(set(project.conops_titles) | set(scenario_moes))
    out += table(["Scenario", "Title", "MOEs judged there"], ([ops, project.conops_titles.get(ops, "(not a heading of conops.md)"), ", ".join(sorted(scenario_moes.get(ops, []))) or "-"] for ops in scenarios))
    out += ["", "## 7. Stakeholders", ""]
    stakeholders = data.get("stakeholders")
    if isinstance(stakeholders, list) and stakeholders:
        out += [
            "The identified stakeholders of 02 section 3.0 (SE HB 4.1.1.2.1), keyed by name; `represented_by` names who speaks for each in "
            "validation step V2. `tools/traceability.py` checks the array with STAKEHOLDERS_MISSING (T-21).",
            "",
        ]
        out += table(
            ["Name", "Role", "Interests", "Represented by (V2)", "Sources", "Note"],
            (
                [as_str(e.get("name")), as_str(e.get("role")), as_str(e.get("interests")), as_str(e.get("represented_by")), md_text(as_str_list(e.get("source_ids"))), md_text(e.get("note"))]
                for e in stakeholders
                if isinstance(e, dict)
            ),
        )
    else:
        out += ["The `stakeholders` array is absent or empty; `tools/traceability.py` reports STAKEHOLDERS_MISSING (T-21, 02 section 3.0)."]
    out += [""]
    return "\n".join(out)


def source_sort_key(source_id: str) -> tuple[int, str]:
    """SI first, then 47 CFR clauses, then anything else, each alphabetically."""
    if SI_ID.match(source_id):
        return (0, source_id)
    if REGULATION_ID.match(source_id):
        return (1, source_id)
    return (2, source_id)


def counts_by_key(entries: Iterable[dict[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for entry in entries:
        counts[as_str(entry.get(key)) or "(unset)"] += 1
    return dict(sorted(counts.items()))


REQUIREMENT_FIELDS: tuple[tuple[str, str], ...] = (
    ("description", "Statement"),
    ("rationale", "Rationale"),
    ("verification_method", "Verification method"),
    ("verification_note", "Verification note"),
    ("status", "Status"),
    ("priority", "Priority"),
    ("parent_id", "Parent"),
    ("child_ids", "Children"),
    ("source_ids", "Sources"),
    ("hazard_ids", "Hazards"),
    ("design_refs", "Design references"),
    ("mop_ids", "Measures"),
    ("tags", "Tags"),
)


def render_requirements(location: str, data: dict[str, Any]) -> str:
    """requirements.md for one requirements.json: a pure function of the file (02 section 8.1)."""
    module = as_str(data.get("module")) or "(unset)"
    items = [r for r in data.get("requirements", []) if isinstance(r, dict)] if isinstance(data.get("requirements"), list) else []
    level = "L1 system requirements" if module == L1_MODULE else "L2 requirements"
    out = [
        f"# Requirements: module {module}",
        "",
        generated_line(location),
        "",
        f"{level} (charter section 7; 02 section 2). The verification matrix, coverage and findings for these requirements are in `{DEFAULT_REPORT}`.",
        "",
        "## 1. Summary",
        "",
    ]
    out += table(
        ["Item", "Count"],
        [
            ["Requirements", str(len(items))],
            *[[f"Status {k}", str(v)] for k, v in counts_by_key(items, "status").items()],
            *[[f"Method {k}", str(v)] for k, v in counts_by_key(items, "verification_method").items()],
            *[[f"Priority {k}", str(v)] for k, v in counts_by_key(items, "priority").items()],
            ["Open TBR", str(sum(1 for r in items if isinstance(r.get("tbr"), dict)))],
            ["Tagged retired", str(sum(1 for r in items if RETIRED_TAG in as_str_list(r.get("tags"))))],
        ],
    )
    out += ["", "## 2. Index", ""]
    out += table(["ID", "Title", "Method", "Status", "Parent"], ([as_str(r.get("id")), as_str(r.get("title")), as_str(r.get("verification_method")), as_str(r.get("status")) + (" (TBR)" if isinstance(r.get("tbr"), dict) else ""), md_text(r.get("parent_id"))] for r in items))
    out += ["", "## 3. Requirements", ""]
    for req in items:
        out += [f"### {as_str(req.get('id'))}: {as_str(req.get('title'))}", ""]
        rows = [[label, md_text(req.get(key))] for key, label in REQUIREMENT_FIELDS if key in req]
        tbr = req.get("tbr")
        if isinstance(tbr, dict):
            rows.append(["TBR", f"owner: {as_str(tbr.get('owner'))}; plan: {as_str(tbr.get('plan'))}; close by: {as_str(tbr.get('close_by'))}"])
        out += table(["Field", "Value"], rows)
        out += [""]
    return "\n".join(out)


def rendered_targets(project: Project) -> list[tuple[Path, str]]:
    """Every rendered file with its expected content (relative path, text)."""
    targets: list[tuple[Path, str]] = []
    expectations = render_expectations(project)
    if expectations is not None:
        targets.append((EXPECTATIONS.with_suffix(".md"), expectations))
    for location, data in sorted(project.requirement_raw.items()):
        targets.append((Path(location).with_suffix(".md"), render_requirements(location, data)))
    return targets


def check_rendered(project: Project) -> None:
    """RENDER_STALE: the rendered .md beside a JSON is absent, hand-made, or older than the JSON's content."""
    for path, expected in rendered_targets(project):
        file = project.root / path
        if not file.is_file():
            project.warning("RENDER_STALE", str(path), f"absent; run {RENDER_COMMAND}")
            continue
        actual = file.read_text(encoding="utf-8")
        if RENDER_MARK not in "\n".join(actual.splitlines()[:5]):
            project.warning("RENDER_STALE", str(path), f"not generated by tools/traceability.py --render (interim or hand-written file); run {RENDER_COMMAND}")
        elif actual != expected:
            project.warning("RENDER_STALE", str(path), f"differs from the rendering of its JSON (edited by hand or not re-rendered); run {RENDER_COMMAND}")


def write_rendered(project: Project) -> list[Path]:
    written: list[Path] = []
    for path, text in rendered_targets(project):
        file = project.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8")
        written.append(path)
    return written


# ----------------------------------------------------------------------------
# Regression set (V&V section 10.5)
# ----------------------------------------------------------------------------


def design_ref_matches(touched: str, design_ref: str) -> bool:
    """A design ref is touched when equal to, or a path prefix of / prefixed by, a touched element."""
    a, b = touched.rstrip("/"), design_ref.rstrip("/")
    return a == b or b.startswith(a + "/") or a.startswith(b + "/")


def regression_set(project: Project, touched: Iterable[str]) -> list[str]:
    """Passed Bench cases whose requirements' design_refs intersect touched, plus every TC-ATP case."""
    touched = list(touched)
    affected = {r.id for r in project.requirements.values() if any(design_ref_matches(t, d) for t in touched for d in r.design_refs)}
    cases = {tc.id for tc in project.test_cases.values() if tc.status == "Passed" and tc.type == "Bench" and set(tc.requirement_ids) & affected}
    cases |= {tc.id for tc in project.test_cases.values() if tc.module == ACCEPTANCE_MODULE and not tc.is_retired}
    return sorted(cases)


# ----------------------------------------------------------------------------
# Derived matrix columns (04 sections 7.1 and 7.2)
# ----------------------------------------------------------------------------


def facility_for(types: Iterable[str]) -> str:
    names = sorted({FACILITY_FOR_TYPE.get(t, t) for t in types if t})
    return ", ".join(names)


def credit_phase(project: Project, req: Requirement, closing: list[TestCase]) -> str:
    """Credit event per 04 section 5.2: CDR, receipt, release, TRR, TRR-Dn, SAR."""
    method = req.verification_method
    types = {tc.type for tc in closing}
    if method == "Analysis":
        return "CDR"
    if method == "Inspection":
        return "CDR/receipt"
    if method == "Test":
        phases = {"release" if t in ("HostUnit", "Emulation") else "TRR" for t in types if t in ("HostUnit", "Emulation", "Bench")}
        return "/".join(sorted(phases)) if phases else ("release" if project.is_software(req) else "TRR")
    if method == "Demonstration":
        phases = {"TRR-Dn" if t == "OnAir" else "TRR" for t in types if t in ("Bench", "OnAir", "Emulation")}
        return "/".join(sorted(phases)) if phases else "TRR"
    return "-"


def performer_for(types: Iterable[str]) -> str:
    return "owner" if any(t in OWNER_PERFORMED_TYPES for t in types) else "claude"


# ----------------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------------


def cell(text: str) -> str:
    """Escape a value for a Markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ").strip() or "-"


def table(headers: list[str], rows: Iterable[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    count = 0
    for row in rows:
        lines.append("| " + " | ".join(cell(c) for c in row) + " |")
        count += 1
    if count == 0:
        lines.append("| " + " | ".join(["(none)"] + ["" for _ in headers[1:]]) + " |")
    return lines


def pct(part: int, whole: int) -> str:
    return "n/a" if whole == 0 else f"{100.0 * part / whole:.0f} %"


def modules_in_order(project: Project) -> list[str]:
    """SYS first, then the remaining modules alphabetically."""
    return sorted({r.module for r in project.requirements.values()}, key=lambda m: (m != L1_MODULE, m))


def counts_by(items: Iterable[Any], attribute: str) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for item in items:
        counts[getattr(item, attribute) or "(unset)"] += 1
    return dict(sorted(counts.items()))


def describe_case(tc: TestCase) -> str:
    detail = f"{tc.status}; {tc.type}"
    if tc.automation_ref:
        detail += f"; {tc.automation_ref}"
    return f"{tc.id} ({detail})"


def describe_report(report: Report) -> str:
    return f"{report.file} ({report.result}{'; credit' if report.credit else ''})"


def results_for(project: Project, req: Requirement) -> str:
    """Latest credited report citing the requirement, then every NCR citing it (04 section 7.1 Results)."""
    credited = [r for tc in project.tcs_for(req.id) for r in project.reports_for(tc.id) if r.credit and req.id in r.requirement_ids]
    parts: list[str] = []
    if credited:
        parts.append(describe_report(max(credited, key=lambda r: (r.date, r.file))))
    for ncr in project.ncrs_for(req.id):
        parts.append(f"{ncr.id} ({ncr.status or 'status unset'})")
    return "; ".join(parts)


def evidence_for(project: Project, req: Requirement) -> str:
    """Every case, report and NCR touching the requirement (used by the JSON output)."""
    parts: list[str] = [describe_case(tc) for tc in project.tcs_for(req.id)]
    for tc in project.tcs_for(req.id):
        for report in project.reports_for(tc.id):
            if req.id in report.requirement_ids:
                parts.append(describe_report(report))
    for ncr in project.ncrs_for(req.id):
        parts.append(f"{ncr.id} ({ncr.status or 'status unset'})")
    return "; ".join(parts)


def parent_and_sources(req: Requirement) -> str:
    parts: list[str] = []
    if req.parent_id:
        parts.append(f"parent {req.parent_id}")
    if req.source_ids:
        parts.append(", ".join(req.source_ids))
    if req.parent_id is None and not req.source_ids:
        parts.append("self-derived" if SELF_DERIVED.search(req.rationale) else "(no trace)")
    return "; ".join(parts)


def upstream_status(project: Project) -> list[list[str]]:
    def describe(universe: set[str] | None) -> str:
        return "absent" if universe is None else f"{len(universe)} ids"

    return [
        ["Stakeholder inputs (SI)", str(STAKEHOLDER_INPUTS), describe(project.stakeholder_inputs) + (f", {len(project.core_inputs)} core" if project.stakeholder_inputs is not None else "")],
        ["Expectations (NGO, MOE, CON)", str(EXPECTATIONS), describe(project.expectations)],
        ["ConOps scenarios (OPS)", str(CONOPS), describe(project.conops_scenarios)],
        ["Hazards (HZ)", str(HAZARDS), f"{len(project.hazards)} ids" if project.hazards_present else "absent"],
        ["Risks (RSK)", str(RISKS), describe(project.risks)],
        ["Measures (MOP, TPM)", str(MEASURES), describe(project.measures)],
        ["Regulatory corpus (47 CFR Parts 1, 2, 15, 97 sections)", str(REGULATORY_DIR), describe(project.regulations)],
        ["Decision records (ADR)", str(ADR_DIR), describe(project.adrs)],
        ["Trade studies (TS)", str(TRADE_STUDY_DIR), describe(project.trade_studies)],
        ["Verification reports", str(REPORTS_DIR), f"{len(project.reports)} files" if project.reports_present else "absent"],
        ["Nonconformances (NCR)", str(NCR_DIR), f"{len(project.ncrs)} files" if (project.root / NCR_DIR).is_dir() else "absent"],
        ["SAR decision memo", str(SAR_DECISION_MEMO), "present" if project.sar_memo_present else "absent"],
        ["Allocation (preliminary at SRR)", str(ALLOCATION), allocation_state(project)],
    ]


def allocation_state(project: Project) -> str:
    if not project.allocation_present:
        return "absent"
    if project.allocation_error is not None:
        return "does not parse"
    return f"{len(project.allocation_modules)} requirement ids allocated"



def verification_row(project: Project, req: Requirement) -> list[str]:
    """One App. D row (04 section 7.1 columns)."""
    closing = project.closing_cases(req)
    supporting = project.supporting_cases(req)
    closing_types = [tc.type for tc in closing]
    atp = project.acceptance_cases(req)
    acceptance = "Yes" if atp else "No"
    recurring = "Yes" if any(tc.is_recurring for tc in atp) else "No"
    return [
        req.id,
        f"`{req.file}`" + (f"; {parent_and_sources(req)}" if parent_and_sources(req) else ""),
        req.description,
        "; ".join(tc.acceptance_criteria for tc in closing if tc.acceptance_criteria),
        req.verification_method,
        ", ".join(sorted(set(closing_types))),
        ", ".join(describe_case(tc) for tc in closing),
        ", ".join(describe_case(tc) for tc in supporting),
        facility_for(closing_types),
        credit_phase(project, req, closing),
        acceptance,  # initial acceptance of each unit: a TC-ATP case cites it (SE HB App. D "Acceptance Requirement?")
        recurring,  # recurring or pre-operation acceptance: a citing TC-ATP case says 'Recurring: yes' (App. D "Preflight Acceptance?")
        performer_for(closing_types),
        results_for(project, req),
        req.status + (" (TBR)" if req.tbr is not None else ""),
    ]


def validation_rows(project: Project) -> list[list[str]]:
    """One row per OPS-NNN and MOE-NNN (SE HB Appendix E, Table E-1; V&V section 7.2)."""
    rows: list[list[str]] = []
    for target in project.validation_targets():
        matching, status = project.validation_row(target)
        results = [describe_case(tc) for tc in matching]
        for tc in matching:
            results += [describe_report(r) for r in project.reports_for(tc.id) if target in r.validates or not r.validates]
        types = [tc.type for tc in matching]
        rows.append(
            [
                target,
                "; ".join(f"{tc.id}: {tc.title}" for tc in matching),
                "; ".join(tc.acceptance_criteria for tc in matching),
                ", ".join(sorted({tc.verification_method for tc in matching})),
                facility_for(types),
                ", ".join(sorted({tc.phase for tc in matching if tc.phase})),
                ("owner and friends" if "OnAir" in types else "owner") if matching else "",
                ", ".join(sorted({rid for tc in matching for rid in tc.requirement_ids})),
                "; ".join(results),
                status,
            ]
        )
    return rows


def tree_lines(project: Project) -> list[str]:
    """Indented requirements tree from the roots (02 section 8.1 planned section)."""
    lines: list[str] = []

    def walk(req: Requirement, depth: int, seen: set[str]) -> None:
        marker = f"{req.id} [{req.status}] {req.title}".rstrip()
        lines.append("  " * depth + "- " + marker)
        if req.id in seen:
            return
        seen.add(req.id)
        for child in project.children_of(req.id):
            walk(child, depth + 1, seen)

    roots = [r for r in project.ordered_requirements() if r.parent_id is None or r.parent_id not in project.requirements]
    for root in roots:
        walk(root, 0, set())
    return lines or ["(no requirements)"]


def coverage_rows(project: Project) -> list[list[str]]:
    reqs = project.live_requirements()

    def coverage_row(label: str, group: list[Requirement]) -> list[str]:
        with_tc = [r for r in group if project.live_tcs_for(r.id)]
        with_closing = [r for r in group if project.closing_cases(r)]
        done = [r for r in group if r.status in EVIDENCE_STATUSES]
        return [
            label,
            str(len(group)),
            str(len(with_tc)),
            pct(len(with_tc), len(group)),
            str(len(with_closing)),
            pct(len(with_closing), len(group)),
            str(len(done)),
            pct(len(done), len(group)),
            str(sum(1 for r in group if project.children_of(r.id))),
            str(sum(1 for r in group if r.tbr is not None)),
        ]

    rows = [coverage_row(module, [r for r in reqs if r.module == module]) for module in modules_in_order(project)]
    if reqs:
        rows.append(coverage_row("**All**", reqs))
    return rows


def coverage_summary() -> str:
    """The SWE-052 Table 1 rows by state, e.g. 'rows 1, 5, 6 enforced; row 2 enforced in part; rows 3, 4 not yet enforced'."""
    groups = ((ENFORCED, "enforced"), (PARTIAL, "enforced in part"), (NOT_ENFORCED, "not yet enforced"))
    parts = []
    for state, label in groups:
        rows = [str(r.row) for r in SWE052_COVERAGE if r.state == state]
        if rows:
            parts.append(f"{'rows' if len(rows) > 1 else 'row'} {', '.join(rows)} {label}")
    return "; ".join(parts)


def coverage_rows_swe052() -> list[list[str]]:
    return [
        [
            str(r.row), r.relationship, r.forward, r.backward,
            ", ".join(r.enforced) or "none",
            "; ".join(f"{code} {action}, {gate}" if action == PROMOTE else f"{code}, {gate}" for code, action, gate in r.planned) or "none",
            r.state, r.note,
        ]
        for r in SWE052_COVERAGE
    ]


def build_report(project: Project, today: dt.date | None = None) -> str:
    today = today or dt.date.today()
    reqs = project.live_requirements()
    retired = [r for r in project.ordered_requirements() if r.is_retired]
    tcs = project.live_test_cases()
    violations, warnings = project.violations, project.warnings
    covered = [r for r in reqs if project.live_tcs_for(r.id)]
    verified = [r for r in reqs if r.status in EVIDENCE_STATUSES]
    verdict = "PASS" if not violations else "FAIL"
    out: list[str] = [
        "# Traceability report",
        "",
        f"Generated by `tools/traceability.py` on {today.isoformat()}. Result: **{verdict}** ({len(violations)} violation(s), {len(warnings)} warning(s)).",
        "",
        "Of the six Class A rows of NPR 7150.2D section 3.12.1 Table 1 (SWE-052) that `docs/process/00-charter.md` section 7 adopts, "
        f"the state of this tool is: {coverage_summary()}. Section 1.4 lists the codes enforced and planned per row with their gates. "
        "It also applies the rules of `docs/process/02-requirements-and-traceability.md` section 8.2 and "
        "`docs/process/04-verification-and-validation.md` section 7.3 that section 11 lists. "
        "Section 3 is the Requirements Verification Matrix of SE HB Appendix D (Table D-1) and section 4 the Validation Matrix of "
        "SE HB Appendix E (Table E-1); together they are Appendices C and D of the V&V plan outline (SE HB Appendix I). "
        "Regenerate with `.venv/bin/python tools/traceability.py`; do not edit by hand.",
        "",
        "## 1. Summary",
        "",
    ]
    out += table(
        ["Item", "Count"],
        [
            ["Requirement files", str(len(project.requirement_files))],
            ["Requirements (not Retired)", str(len(reqs))],
            ["Requirements Retired", str(len(retired))],
            *[[f"Requirements with status {status}", str(n)] for status, n in counts_by(project.ordered_requirements(), "status").items()],
            ["Requirements with at least one verification case", f"{len(covered)} of {len(reqs)} ({pct(len(covered), len(reqs))})"],
            ["Requirements Verified or Closed", f"{len(verified)} of {len(reqs)} ({pct(len(verified), len(reqs))})"],
            ["Requirements with open TBR (MSR-04)", str(sum(1 for r in reqs if r.tbr is not None))],
            ["Key driving requirements (KDR)", str(sum(1 for r in reqs if r.priority == "KDR"))],
            ["Test case files", str(len(project.test_case_files))],
            ["Test cases (not Retired)", str(len(tcs))],
            *[[f"Test cases with status {status}", str(n)] for status, n in counts_by(project.ordered_test_cases(), "status").items()],
            *[[f"Test cases of class {kind}", str(n)] for kind, n in counts_by(tcs, "type").items()],
            ["Verification reports", str(len(project.reports))],
            ["Hazards", str(len(project.hazards))],
            ["Expectations (NGO, MOE, CON)", str(len(project.expectations or ()))],
            ["ConOps scenarios", str(len(project.conops_scenarios or ()))],
            ["Nonconformance reports", str(len(project.ncrs))],
            *[[f"NCRs with status {status}", str(n)] for status, n in counts_by(project.ncrs.values(), "status").items()],
            *[[f"NCRs with severity {severity}", str(n)] for severity, n in counts_by(project.ncrs.values(), "severity").items()],
            ["Violations", str(len(violations))],
            ["Warnings", str(len(warnings))],
        ],
    )
    out += ["", "### 1.1 Upstream artifacts consulted", ""]
    out += table(["Artifact", "Path", "State"], upstream_status(project))
    out += ["", "### 1.2 Open TBR list", "", "Every requirement carrying a `tbr` object (02 section 9 rule 3; NPR 7123.1D App. G Tables G-4, G-6 and G-7: TBD and TBR items identified with plans).", ""]
    out += table(
        ["ID", "Module", "Status", "Owner", "Plan", "Close by"],
        ([r.id, r.module, r.status, as_str((r.tbr or {}).get("owner")), as_str((r.tbr or {}).get("plan")), as_str((r.tbr or {}).get("close_by"))] for r in reqs if r.tbr is not None),
    )
    out += ["", "### 1.3 Key driving requirements", "", "Requirements with `priority: KDR` (02 section 6; T-16 requires an MOP or TPM per KDR from PDR).", ""]
    out += table(["ID", "Title", "Status", "Measures (mop_ids)"], ([r.id, r.title, r.status, ", ".join(r.mop_ids)] for r in reqs if r.priority == "KDR"))
    out += [
        "",
        "### 1.4 SWE-052 Table 1 coverage",
        "",
        "One row per Class A row of NPR 7150.2D section 3.12.1 Table 1 (charter section 7). Codes planned and their gates are those of "
        "`docs/process/03-software-classification-and-rmm.md` section 8. A row that is Partial or Not enforced is checked by the product "
        "reviewer with the checklist for that product until its codes exist.",
        "",
    ]
    out += table(["Row", "Relationship", "Forward link", "Backward link", "Codes enforced", "Codes planned (gate)", "State", "Note"], coverage_rows_swe052())

    out += ["", "## 2. Findings", "", "### 2.1 Violations", ""]
    out += table(["Code", "Location", "Message"], ([f.code, f.location, f.message] for f in violations))
    out += ["", "### 2.2 Warnings", ""]
    out += table(["Code", "Location", "Message"], ([f.code, f.location, f.message] for f in warnings))

    out += [
        "",
        "## 3. Requirements verification matrix (SE HB Appendix D)",
        "",
        "One table per requirements document, as Appendix D permits; Retired requirements are omitted (04 section 7.1). "
        "Closing cases share the requirement's verification method; supporting cases (V&V 7.3 rule 3) cite the requirement with another method. "
        "Success criteria are the acceptance criteria of the closing cases. Facility, phase (credit event of 04 section 5.2) and performer "
        "derive from the closing cases' evidence class. Acceptance? is Yes when a `TC-ATP` case cites the requirement (initial acceptance of each unit, 04 section 11.1); "
        "Recurring acceptance? is Yes only when such a case carries `Recurring: yes` in its setup (SE HB App. D Preflight Acceptance?). "
        "Results list the latest credited report and every NCR citing the requirement.",
    ]
    headers = [
        "ID", "Source", "Shall statement", "Success criteria", "Method", "Evidence class", "Closing cases", "Supporting cases",
        "Facility", "Phase", "Acceptance?", "Recurring acceptance?", "Performer", "Results", "Status",
    ]
    for index, module in enumerate(modules_in_order(project), start=1):
        module_reqs = [r for r in reqs if r.module == module]
        files = sorted({r.file for r in project.ordered_requirements() if r.module == module})
        out += ["", f"### 3.{index} Module {module} (`{'`, `'.join(files)}`)", ""]
        out += table(headers, (verification_row(project, r) for r in module_reqs))

    out += ["", "## 4. Validation matrix (SE HB Appendix E)", ""]
    if project.conops_scenarios is None and project.expectations is None:
        out += [f"`{CONOPS}` and `{EXPECTATIONS}` are absent; no validation targets to list."]
    else:
        out += [
            "One row per `OPS-NNN` heading and per `MOE-NNN`; activities are the `TC-VAL` cases whose setup names the target after `Validates:`; "
            "the phase is the token after `Phase:` in the case setup (04 section 7.2). Row status is Validated when every case is Passed.",
            "",
        ]
        out += table(
            ["Validation product", "Activity", "Objective", "Method", "Facility", "Phase", "Performer", "Requirements exercised", "Results", "Row status"],
            validation_rows(project),
        )

    out += ["", "## 5. Orphan requirements", "", "Draft or Active requirements with no verification case citing them.", ""]
    out += table(
        ["ID", "Status", "Method", "File"],
        ([r.id, r.status, r.verification_method, r.file] for r in reqs if r.status in REQ_STATUSES_NEEDING_TC and not project.live_tcs_for(r.id)),
    )

    out += ["", "## 6. Orphan test cases", "", "Test cases citing at least one requirement id that does not exist.", ""]
    out += table(
        ["ID", "Unresolved requirement ids", "File"],
        (
            [tc.id, ", ".join(rid for rid in tc.requirement_ids if rid not in project.requirements), tc.file]
            for tc in project.ordered_test_cases()
            if any(rid not in project.requirements for rid in tc.requirement_ids)
        ),
    )

    out += ["", "## 7. Parent coverage", "", "### 7.1 Requirements without a parent", ""]
    out += table(
        ["ID", "Module", "Justification"],
        (
            [r.id, r.module, ("traces to " + ", ".join(r.source_ids)) if r.source_ids else ("self-derived (rationale)" if SELF_DERIVED.search(r.rationale) else "none")]
            for r in reqs
            if r.parent_id is None
        ),
    )
    out += [
        "",
        "### 7.2 Allocation to children",
        "",
        "Rule T-18 (02 section 8.2) applies from SRR: every Draft or Active SYS requirement names at least one receiving L2 module, "
        f"through `child_ids` naming a live L2 requirement or through a preliminary `{ALLOCATION}` record that lists it under an L2 module "
        "(02 section 2.3). At SRR each gap is a `SYS_UNALLOCATED` warning in section 2.2, which the reviewer confirms or corrects in V6; "
        "from PDR it is an Error under `--gate`, and every Active SYS requirement then needs a child or the tag `leaf`. "
        "Receiving L2 modules are the modules of the live L2 children and of the allocation records.",
        "",
    ]
    out += table(
        ["ID", "Module", "Children", "Child ids", "Receiving L2 modules"],
        (
            [r.id, r.module, str(len(project.children_of(r.id))), ", ".join(c.id for c in project.children_of(r.id)), ", ".join(project.receiving_modules(r))]
            for r in project.ordered_requirements()
        ),
    )
    out += ["", "### 7.3 Requirements tree", "", "Roots are requirements with `parent_id` null; each line is `id [status] title`.", ""]
    out += tree_lines(project)

    out += ["", "## 8. Per-module coverage", ""]
    out += table(["Module", "Requirements", "With any case", "Coverage", "With closing case", "Closing coverage", "Verified or Closed", "Closure", "With children", "Open TBR"], coverage_rows(project))

    out += ["", "## 9. Hazard traceability", ""]
    if project.hazards_present:
        out += [
            "Requirements controlling each hazard (the union of their own `hazard_ids` and the hazard's `requirement_ids` and controls' "
            "`control_req_ids`, 04 section 3), the verification cases that cite them (SWE-052, software requirements to hazards), and the "
            "live software requirements that do not yet have a Passed, credited Bench or OnAir closing case (SWE-192 at SAR, 01 section 8.6).",
            "",
        ]
        hazard_rows = []
        for hazard in sorted(project.hazards.values(), key=lambda h: h.id):
            controlling = sorted(r.id for r in project.ordered_requirements() if not r.is_retired and hazard.id in project.hazard_trace(r))
            cases = sorted({tc.id for rid in controlling for tc in project.tcs_for(rid)})
            off_target = [rid for rid in controlling if project.is_software(project.requirements[rid]) and not on_target_cases(project, project.requirements[rid])]
            hazard_rows.append([hazard.id, hazard.title, ", ".join(controlling), ", ".join(cases), ", ".join(off_target)])
        out += table(["Hazard", "Title", "Controlling requirements", "Verification cases", "Software requirements not yet tested on target"], hazard_rows)
    else:
        out += [f"`{HAZARDS}` is absent; hazard traceability not evaluated."]

    out += ["", "## 10. Nonconformance traceability", ""]
    if project.ncrs:
        out += ["### 10.1 Nonconformances", "", "From the front matter of `docs/vv/ncr/NCR-NNN.md`.", ""]
        out += table(
            ["NCR", "Status", "Severity", "Requirements", "Test cases", "Title"],
            ([n.id, n.status, n.severity, ", ".join(n.requirement_ids), ", ".join(n.test_case_ids), n.title] for n in sorted(project.ncrs.values(), key=lambda n: n.id)),
        )
        out += ["", "### 10.2 Requirements to nonconformances (SWE-052)", ""]
        out += table(
            ["Requirement", "Status", "NCRs"],
            ([r.id, r.status, ", ".join(f"{n.id} ({n.status or 'status unset'})" for n in project.ncrs_for(r.id))] for r in project.ordered_requirements() if project.ncrs_for(r.id)),
        )
    else:
        out += [f"No nonconformance reports under `{NCR_DIR}`."]

    out += ["", "## 11. Checks performed", ""]
    out += table(["Code", "Severity", "Rule"], ([code, severity, rule] for code, severity, rule in CHECK_CATALOGUE))
    out += [""]
    return "\n".join(out)


# ----------------------------------------------------------------------------
# Machine-readable output (docs/vv/traceability.json; 07 section 11 measurements)
# ----------------------------------------------------------------------------


def measurements(project: Project) -> dict[str, Any]:
    """MSR-01, MSR-03, MSR-04 and MSR-23 of 07 section 11.2 as the tool can measure them today."""
    reqs = project.live_requirements()
    by_level: dict[str, dict[str, int]] = {"L1": defaultdict(int), "L2": defaultdict(int)}
    for req in project.ordered_requirements():
        by_level["L1" if req.module == L1_MODULE else "L2"][req.status or "(unset)"] += 1
    software = [r for r in reqs if project.is_software(r)]
    codes = defaultdict(int)
    for finding in project.findings:
        codes[finding.code] += 1
    tcs = project.live_test_cases()
    return {
        "MSR-01": {
            "name": "Software requirements count by level and status",
            "by_level": {level: dict(sorted(counts.items())) for level, counts in by_level.items()},
            "software_by_status": counts_by(software, "status"),
        },
        "MSR-03": {
            "name": "Traceability gaps",
            "requirements_without_parent": codes["PARENT_MISSING"] + codes["SELF_DERIVED_UNSUPPORTED"] + codes["PARENT_UNRESOLVED"],
            "requirements_without_verification_case": codes["REQ_UNVERIFIED"],
            "design_units_without_design_tag": None,
            "functions_without_req_tag": None,
            "note": "the firmware tag scan (02 T-15) is a PDR/CDR tool task; null until it exists",
        },
        "MSR-04": {
            "name": "Open TBR count",
            "software_requirements": sum(1 for r in software if r.tbr is not None),
            "all_requirements": sum(1 for r in reqs if r.tbr is not None),
        },
        "MSR-23": {
            "name": "Test counts by status and class",
            "by_status": counts_by(tcs, "status"),
            "by_class": counts_by(tcs, "type"),
            "by_class_and_status": {
                kind: counts_by([tc for tc in tcs if tc.type == kind], "status") for kind in sorted({tc.type for tc in tcs})
            },
        },
    }


def build_json(project: Project, today: dt.date | None = None) -> dict[str, Any]:
    today = today or dt.date.today()
    reqs = project.live_requirements()
    return {
        "generated": today.isoformat(),
        "tool": "tools/traceability.py",
        "result": "PASS" if not project.violations else "FAIL",
        "violations": len(project.violations),
        "warnings": len(project.warnings),
        "counts": {
            "requirements": len(reqs),
            "requirements_retired": sum(1 for r in project.requirements.values() if r.is_retired),
            "requirements_covered": sum(1 for r in reqs if project.live_tcs_for(r.id)),
            "requirements_verified_or_closed": sum(1 for r in reqs if r.status in EVIDENCE_STATUSES),
            "test_cases": len(project.live_test_cases()),
            "reports": len(project.reports),
            "hazards": len(project.hazards),
            "ncrs": len(project.ncrs),
            "expectations": len(project.expectations or ()),
            "conops_scenarios": len(project.conops_scenarios or ()),
        },
        "coverage_by_module": {
            row[0].strip("*"): {"requirements": int(row[1]), "with_any_case": int(row[2]), "with_closing_case": int(row[4]), "verified_or_closed": int(row[6]), "with_children": int(row[8]), "open_tbr": int(row[9])}
            for row in coverage_rows(project)
        },
        "measurements": measurements(project),
        "swe052_coverage": [
            {"row": r.row, "relationship": r.relationship, "state": r.state, "enforced": list(r.enforced), "planned": [{"code": c, "action": a, "gate": g} for c, a, g in r.planned]}
            for r in SWE052_COVERAGE
        ],
        "validation_rows": {target: project.validation_row(target)[1] for target in project.validation_targets()},
        "findings": [{"severity": f.severity, "code": f.code, "location": f.location, "message": f.message} for f in project.findings],
    }


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------


def print_findings(project: Project, quiet: bool) -> None:
    for finding in project.findings:
        if finding.severity == WARNING and quiet:
            continue
        print(f"{finding.severity:9s} {finding.code:26s} {finding.location}: {finding.message}")


def run(root: Path, output: Path, report_only: bool = False, quiet: bool = False, today: dt.date | None = None, json_output: Path | None = None, render: bool = False) -> int:
    project = load_project(root)
    if render:
        for path in write_rendered(project):
            if not quiet:
                print(f"rendered  {path}")
    run_checks(project)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_report(project, today), encoding="utf-8")
    json_path = json_output if json_output is not None else output.parent / DEFAULT_JSON_NAME
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(build_json(project, today), indent=2) + "\n", encoding="utf-8")
    print_findings(project, quiet)
    violations, warnings = len(project.violations), len(project.warnings)
    if not quiet:
        print(
            f"traceability: {len(project.requirements)} requirements, {len(project.test_cases)} test cases, "
            f"{violations} violation(s), {warnings} warning(s); report written to {rel(output, root)}, data to {rel(json_path, root)}"
        )
    return 1 if violations and not report_only else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root (default: the parent of tools/)")
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT, help=f"report path, relative to root unless absolute (default: {DEFAULT_REPORT})")
    parser.add_argument("--json", type=Path, default=None, help=f"machine-readable output path (default: {DEFAULT_JSON_NAME} beside the report)")
    parser.add_argument("--report-only", action="store_true", help="write the report and exit 0 even when violations exist")
    parser.add_argument("--quiet", action="store_true", help="print violations only; suppress warnings and the summary line")
    parser.add_argument("--render", action="store_true", help="also write expectations.md beside expectations.json and requirements.md beside each requirements.json (02 section 8.1), then run the checks")
    parser.add_argument("--regression", nargs="+", metavar="DESIGN_REF", help="print the regression set for the touched design elements (V&V section 10.5) and exit; no report is written")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    if args.regression:
        project = load_project(root)
        for case_id in regression_set(project, args.regression):
            print(case_id)
        return 0
    output = args.output if args.output.is_absolute() else root / args.output
    json_output = None if args.json is None else (args.json if args.json.is_absolute() else root / args.json)
    return run(root, output, args.report_only, args.quiet, json_output=json_output, render=args.render)


if __name__ == "__main__":
    sys.exit(main())
