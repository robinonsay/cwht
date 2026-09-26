#!/usr/bin/env python3
"""Validate the cwht risk register and render it to Markdown.

Standard library only; run it with the project interpreter so that the JSON
Schema check also runs (jsonschema is installed in .venv only):

    /Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py
        validate, then write docs/risk/register.md
    /Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/render_risk.py --check
        validate and confirm docs/risk/register.md equals a fresh render (exit 1 on any error)
    ... --gate <SRR|PDR|CDR|TRR|TRR-Dn|SAR>
        review-package run: every active risk assessed at that gate, REQ/HZ link rule from PDR,
        plan approval of Red risks carried over from an earlier gate
    ... --hazards docs/safety/hazards.json
        hazard link rule cross-check (coverage, back-links, safety at least the mapped severity)
    ... --register PATH --output PATH
        alternative input and rendered file (used by the known-answer tests)

The register is docs/risk/register.json (schema: docs/risk/schema.json). The
scales, bands and rules implemented here are those of
docs/process/06-risk-and-decision-analysis.md sections 3 to 12 and 16; if that
document changes, change this file and tools/tests/test_render_risk.py in the
same commit. Review points are Pre-SRR, SRR, PDR, CDR, TRR, a delta TRR written
TRR-Dn, SAR and Ops.

Without the optional `jsonschema` package the built-in structural checks still
run (they cover every rule the process document states) and a warning is printed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
REGISTER = REPO / "docs" / "risk" / "register.json"
SCHEMA = REPO / "docs" / "risk" / "schema.json"
OUTPUT = REPO / "docs" / "risk" / "register.md"

STALE_MESSAGE = "register.md is stale; run without --check"

DIMS = ["safety", "first_power_on", "cost", "schedule", "performance_margin"]
DIM_LABEL = {
    "safety": "Safety",
    "first_power_on": "First power-on",
    "cost": "Cost",
    "schedule": "Schedule",
    "performance_margin": "Performance margin",
}
LIKELIHOOD_NAME = {1: "Very unlikely", 2: "Unlikely", 3: "Possible", 4: "Likely", 5: "Near certain"}
CONSEQUENCE_NAME = {1: "Negligible", 2: "Minor", 3: "Moderate", 4: "Major", 5: "Critical"}
BAND_ORDER = {"Red": 0, "Yellow": 1, "Green": 2}
BAND_MARK = {"Red": "R", "Yellow": "Y", "Green": "G"}
GATES = ["SRR", "PDR", "CDR", "TRR", "SAR", "Ops"]
REVIEW_POINTS = ["Pre-SRR"] + GATES
CATEGORIES = ["safety", "technical", "software", "cost", "schedule", "programmatic", "process"]
STATUSES = ["Proposed", "Open", "Mitigating", "Watch", "Accepted", "Realized", "Closed", "Retired"]
TRENDS = ["New", "Increasing", "Stable", "Decreasing", "Closed"]
STRATEGIES = ["Mitigate", "Watch", "Accept", "Research", "Elevate"]
RED_STRATEGIES = {"Mitigate", "Research", "Elevate"}
STEP_STATUSES = ["Planned", "InProgress", "Done", "Dropped"]
CONFIDENCE = ["Low", "Medium", "High"]
OWNERS = ["Robin", "Claude"]
INACTIVE = {"Closed", "Retired"}
PLAN_EXEMPT = {"Accepted", "Closed", "Retired"}
DISPOSITIONS = ["Entered", "Merged", "Declined"]
# Hazard severity (docs/safety/hazards.json scales.severity) to the minimum register safety level
# (hazard link rule, process section 1: Catastrophic 5, Critical 4, Marginal 3 or 2, Negligible 1).
SEVERITY_MIN_SAFETY = {"Catastrophic": 5, "Critical": 4, "Marginal": 2, "Negligible": 1}
HAZARD_CONTROLLED = {"Controls verified", "Accepted", "Retired"}

RE_ID = re.compile(r"^RSK-[0-9]{3}$")
RE_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
RE_STEP = re.compile(r"^S[0-9]{1,2}$")
RE_DELTA_TRR = re.compile(r"^TRR-D[1-9][0-9]?$")  # delta TRR (charter section 3, 01 section 7.6)
RE_TAG = re.compile(r"^[a-z][a-z0-9-]*$")
# Step artifacts that make a risk a software risk (process section 5).
RE_SW_ARTIFACT = re.compile(r"(?<![\w/.-])(docs/requirements/sw/|docs/test_cases/sw-|firmware/)")
RE_RELATED = {
    "requirement_ids": re.compile(r"^REQ-[A-Z][A-Z0-9]*(-[A-Z][A-Z0-9]*)*-[0-9]{3}$"),
    "hazard_ids": re.compile(r"^HZ-[0-9]{3}$"),
    "adr_ids": re.compile(r"^ADR-[0-9]{3}$"),
    "trade_study_ids": re.compile(r"^TS-[0-9]{3}$"),
    "tpm_ids": re.compile(r"^TPM-[0-9]{3}$"),
    "ncr_ids": re.compile(r"^NCR-[0-9]{3}$"),
    "cr_ids": re.compile(r"^CR-[0-9]{3}$"),
    "stakeholder_input_ids": re.compile(r"^SI-[0-9]{3}$"),
    "risk_ids": re.compile(r"^RSK-[0-9]{3}$"),
}
REQUIRED_RELATED = ["requirement_ids", "hazard_ids", "adr_ids", "trade_study_ids", "stakeholder_input_ids", "risk_ids"]

REQUIRED_RISK_KEYS = [
    "id", "title", "statement", "category", "likelihood", "likelihood_rationale",
    "consequence", "consequence_rationale", "score", "assessment_confidence",
    "owner", "source", "opened", "horizon", "last_assessed", "mitigation",
    "status", "trend", "related", "closure_criteria", "history",
]


def is_review_point(value) -> bool:
    """Named review point or a delta TRR token TRR-Dn."""
    return isinstance(value, str) and (value in REVIEW_POINTS or bool(RE_DELTA_TRR.match(value)))


def review_rank(value: str) -> int:
    """Life-cycle order of a review point; a delta TRR ranks with TRR (after CDR, before SAR)."""
    if RE_DELTA_TRR.match(value):
        return REVIEW_POINTS.index("TRR")
    return REVIEW_POINTS.index(value)


def is_gate_choice(value: str) -> bool:
    """Review points for which a review package is prepared (--gate)."""
    return value in ("SRR", "PDR", "CDR", "TRR", "SAR") or bool(RE_DELTA_TRR.match(value))


# ---------------------------------------------------------------------------
# Scoring rules (process document sections 7 and 8)
# ---------------------------------------------------------------------------

def max_consequence(risk: dict) -> int:
    return max(risk["consequence"][d] for d in DIMS)


def driving_dimensions(risk: dict) -> list[str]:
    m = max_consequence(risk)
    return [d for d in DIMS if risk["consequence"][d] == m]


def band(likelihood: int, consequence: int, safety: int) -> str:
    """Band of a cell. Safety override: safety consequence 5 is Red at any likelihood of 2 or more."""
    score = likelihood * consequence
    if safety == 5 and likelihood >= 2:
        return "Red"
    if score >= 12:
        return "Red"
    if score >= 5:
        return "Yellow"
    return "Green"


def cell_band(likelihood: int, consequence: int) -> str:
    """Band of a matrix cell without the safety override (used for the cell label)."""
    return band(likelihood, consequence, 0)


def risk_band(risk: dict) -> str:
    return band(risk["likelihood"], max_consequence(risk), risk["consequence"]["safety"])


def red_by_override(risk: dict) -> bool:
    """Red only because of the safety override (the cell band alone is not Red)."""
    return risk_band(risk) == "Red" and cell_band(risk["likelihood"], max_consequence(risk)) != "Red"


def is_software_risk(risk: dict) -> bool:
    """SWE-086 population: category software or tag software (process section 5)."""
    return risk.get("category") == "software" or "software" in risk.get("tags", [])


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.aggregate_checks: list[tuple[str, int, list[str]]] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def _is_int_level(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 5


def _valid_decision_record(rec) -> bool:
    return (
        isinstance(rec, dict)
        and isinstance(rec.get("decision_memo"), str)
        and len(rec["decision_memo"].strip()) >= 5
        and RE_DATE.match(rec.get("date", "") or "") is not None
    )


def validate_risk(risk: dict, rep: Report, all_ids: set[str], gate: str | None = None) -> None:
    rid = risk.get("id", "<no id>")
    tag = f"{rid}: "
    missing = [key for key in REQUIRED_RISK_KEYS if key not in risk]
    for key in missing:
        rep.error(tag + f"missing required field '{key}'")
    if missing:
        return  # cannot check the rest consistently

    if not RE_ID.match(rid):
        rep.error(tag + "id does not match RSK-NNN")
    if len(risk["title"]) > 80:
        rep.error(tag + "title longer than 80 characters")

    st = risk["statement"]
    for part in ["condition", "departure", "asset", "consequence"]:
        if not isinstance(st.get(part), str) or not st[part].strip():
            rep.error(tag + f"statement.{part} missing or empty")

    if risk["category"] not in CATEGORIES:
        rep.error(tag + f"category '{risk['category']}' not in {CATEGORIES}")
    tags = risk.get("tags", [])
    if not isinstance(tags, list) or any(not isinstance(t, str) or not RE_TAG.match(t) for t in tags):
        rep.error(tag + "tags must be a list of lowercase tokens matching ^[a-z][a-z0-9-]*$")
        tags = []
    elif len(set(tags)) != len(tags):
        rep.error(tag + "tags has duplicates")
    if not _is_int_level(risk["likelihood"]):
        rep.error(tag + "likelihood must be an integer 1..5")
    for d in DIMS:
        if not _is_int_level(risk["consequence"].get(d)):
            rep.error(tag + f"consequence.{d} must be an integer 1..5")
    if any(e.startswith(tag) and ("likelihood must" in e or "consequence." in e) for e in rep.errors):
        return

    expected = risk["likelihood"] * max_consequence(risk)
    if risk["score"] != expected:
        rep.error(tag + f"score {risk['score']} != likelihood x max(consequence) = {expected}")
    if risk["assessment_confidence"] not in CONFIDENCE:
        rep.error(tag + "assessment_confidence not in Low/Medium/High")
    if risk["owner"] not in OWNERS:
        rep.error(tag + f"owner not in {OWNERS}")
    if not RE_DATE.match(risk["opened"]):
        rep.error(tag + "opened is not YYYY-MM-DD")
    if risk["horizon"] not in GATES:
        rep.error(tag + f"horizon not in {GATES}")
    la = risk["last_assessed"]
    la_ok = RE_DATE.match(la.get("date", "")) is not None and is_review_point(la.get("review"))
    if not la_ok:
        rep.error(tag + "last_assessed needs a date and a review point (Pre-SRR, SRR, PDR, CDR, TRR, TRR-Dn, SAR, Ops)")

    # Mitigation plan
    mit = risk["mitigation"]
    strategy = mit.get("strategy")
    if strategy not in STRATEGIES:
        rep.error(tag + f"mitigation.strategy not in {STRATEGIES}")
    steps = mit.get("steps", [])
    step_ids = set()
    for s in steps:
        sid = s.get("id", "?")
        if not RE_STEP.match(sid):
            rep.error(tag + f"step id '{sid}' does not match S<n>")
        if sid in step_ids:
            rep.error(tag + f"duplicate step id '{sid}'")
        step_ids.add(sid)
        if s.get("due") not in GATES:
            rep.error(tag + f"step {sid} due gate not in {GATES}")
        if s.get("status") not in STEP_STATUSES:
            rep.error(tag + f"step {sid} status not in {STEP_STATUSES}")
        if s.get("status") == "Done" and not s.get("evidence"):
            rep.error(tag + f"step {sid} is Done without evidence")
        for f in ["action", "artifact"]:
            if not s.get(f):
                rep.error(tag + f"step {sid} missing '{f}'")
    triggers = mit.get("triggers", [])
    for i, t in enumerate(triggers, 1):
        if not t.get("condition") or not t.get("response"):
            rep.error(tag + f"trigger {i} needs condition and response")
    if not mit.get("fallback"):
        rep.error(tag + "mitigation.fallback missing")
    if "plan_approval" in mit and not _valid_decision_record(mit["plan_approval"]):
        rep.error(tag + "mitigation.plan_approval needs decision_memo and date")

    # Software tag rule (process section 5)
    if risk["category"] != "software" and "software" not in tags:
        if any(RE_SW_ARTIFACT.search(s.get("artifact", "") or "") for s in steps):
            rep.error(tag + "a step artifact is under docs/requirements/sw/, docs/test_cases/sw-* or firmware/ but the risk has neither category software nor tag software (process section 5)")

    # Status, band and plan sufficiency (process document sections 3, 8 and 9)
    status = risk["status"]
    if status not in STATUSES:
        rep.error(tag + f"status not in {STATUSES}")
    b = risk_band(risk)
    active_steps = [s for s in steps if s.get("status") != "Dropped"]
    if status not in INACTIVE and len(triggers) < 1:
        rep.error(tag + "risk needs at least 1 trigger (process section 8)")
    if status not in PLAN_EXEMPT:
        if b == "Red" and len(active_steps) < 2:
            rep.error(tag + "Red risk needs at least 2 active mitigation steps (process section 8)")
        if b == "Red" and strategy in STRATEGIES and strategy not in RED_STRATEGIES:
            rep.error(tag + f"Red risk needs strategy Mitigate, Research or Elevate, not {strategy} (process section 8)")
        if b == "Red" and status == "Watch":
            rep.error(tag + "Red risk cannot have status Watch (process section 9)")
    if status == "Accepted":
        acc = risk.get("acceptance")
        if not _valid_decision_record(acc) or not _is_int_level_score(acc.get("residual_score")):
            rep.error(tag + "Accepted risk needs acceptance.decision_memo, acceptance.date and acceptance.residual_score")
        elif acc["residual_score"] != risk["score"]:
            rep.error(tag + f"acceptance.residual_score {acc['residual_score']} != score {risk['score']}")
    rel = risk["related"]
    if status == "Realized" and not rel.get("ncr_ids") and not rel.get("cr_ids"):
        rep.error(tag + "Realized risk needs related.ncr_ids or related.cr_ids (process section 3)")
    if strategy == "Accept" and status not in {"Accepted", "Proposed", "Open"}:
        rep.warn(tag + "strategy Accept but status is neither Accepted nor awaiting the owner's decision")
    if risk["assessment_confidence"] == "Low" and strategy != "Research":
        has_reassess = any("re-assess" in (t.get("response", "") or "").lower() for t in triggers)
        has_ha = any("hazard analysis" in (s.get("action", "") or "").lower() for s in steps)
        if not has_reassess and not has_ha:
            rep.error(tag + "Low confidence without a Research strategy, a re-assessment trigger or a hazard-analysis step (process section 3)")

    # Trend and history consistency
    hist = risk["history"]
    if not hist:
        rep.error(tag + "history must have at least one entry")
    else:
        last = hist[-1]
        for h in hist:
            if not RE_DATE.match(h.get("date", "")) or not is_review_point(h.get("review")):
                rep.error(tag + "history entry needs date and review point")
            if not _is_int_level(h.get("likelihood")) or not _is_int_level(h.get("consequence")):
                rep.error(tag + "history entry likelihood/consequence must be 1..5")
            elif h.get("score") != h["likelihood"] * h["consequence"]:
                rep.error(tag + f"history entry {h.get('date')} score != likelihood x consequence")
            if "safety" in h and not _is_int_level(h.get("safety")):
                rep.error(tag + "history entry safety must be 1..5")
            if h.get("status") not in STATUSES:
                rep.error(tag + "history entry status invalid")
        if (last.get("likelihood"), last.get("consequence"), last.get("score"), last.get("status")) != (
            risk["likelihood"], max_consequence(risk), risk["score"], status
        ):
            rep.error(tag + "last history entry must equal the current likelihood, max consequence, score and status")
        if last.get("safety") != risk["consequence"]["safety"]:
            rep.error(tag + "last history entry must carry safety equal to consequence.safety")
        if la.get("date") != last.get("date"):
            rep.error(tag + "last_assessed.date must equal the date of the last history entry")
        if la.get("review") != last.get("review"):
            rep.error(tag + "last_assessed.review must equal the review of the last history entry")
        dates = [h.get("date", "") for h in hist]
        if dates != sorted(dates):
            rep.error(tag + "history entries must be in date order")
        reviews = [h.get("review") for h in hist if is_review_point(h.get("review"))]
        if [review_rank(r) for r in reviews] != sorted(review_rank(r) for r in reviews):
            rep.error(tag + "history review points must not go back in the life cycle")
        trend = risk["trend"]
        if trend not in TRENDS:
            rep.error(tag + f"trend not in {TRENDS}")
        elif status in INACTIVE:
            if trend != "Closed":
                rep.error(tag + "Closed/Retired risk must have trend Closed")
        elif len(hist) == 1:
            if trend != "New":
                rep.error(tag + "a risk with one history entry must have trend New")
        else:
            prev, cur = hist[-2]["score"], hist[-1]["score"]
            want = "Increasing" if cur > prev else "Decreasing" if cur < prev else "Stable"
            if trend != want:
                rep.error(tag + f"trend should be {want} (score {prev} -> {cur})")

    # Related identifiers
    for key in REQUIRED_RELATED:
        if key not in rel:
            rep.error(tag + f"related.{key} missing (use an empty list)")
    for key, values in rel.items():
        pat = RE_RELATED.get(key)
        if pat is None:
            rep.error(tag + f"unknown related key '{key}'")
            continue
        for v in values:
            if not pat.match(v):
                rep.error(tag + f"related.{key} entry '{v}' has the wrong format")
        if len(set(values)) != len(values):
            rep.error(tag + f"related.{key} has duplicates")
    for v in rel.get("risk_ids", []):
        if v == rid:
            rep.error(tag + "risk lists itself in related.risk_ids")
        elif v not in all_ids:
            rep.error(tag + f"related.risk_ids refers to unknown {v}")

    # Gate rules (process sections 8, 10 and 11)
    if la_ok and status not in INACTIVE:
        at_or_after_pdr = review_rank(la["review"]) >= REVIEW_POINTS.index("PDR")
        if gate is not None:
            at_or_after_pdr = at_or_after_pdr or review_rank(gate) >= REVIEW_POINTS.index("PDR")
            if review_rank(la["review"]) < review_rank(gate):
                rep.error(tag + f"last assessed at {la['review']}, before the {gate} Track pass (process section 10)")
            if b == "Red" and status not in PLAN_EXEMPT and "plan_approval" not in mit:
                earlier_gate = any(
                    is_review_point(h.get("review"))
                    and REVIEW_POINTS.index("SRR") <= review_rank(h["review"]) < review_rank(gate)
                    for h in hist
                )
                if earlier_gate:
                    rep.error(tag + "Red risk assessed at an earlier gate review has no mitigation.plan_approval (process section 8)")
        if b == "Red" and at_or_after_pdr and not rel.get("requirement_ids") and not rel.get("hazard_ids"):
            rep.error(tag + "Red risk has no REQ or HZ link at PDR or later (process section 11)")

    # Aggregate risks: likelihood equals the maximum of the children (process section 16 item 8).
    if "aggregate" in tags and rel.get("risk_ids"):
        rep.aggregate_checks.append((rid, risk["likelihood"], list(rel["risk_ids"])))

    if len(risk.get("closure_criteria", "")) < 20:
        rep.error(tag + "closure_criteria too short")


def _is_int_level_score(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 25


def validate_candidates(register: dict, rep: Report, by_id: dict[str, dict]) -> None:
    """Candidate disposition record (process section 9, Identify)."""
    cands = register.get("candidates", [])
    if not isinstance(cands, list):
        rep.error("register.candidates must be a list")
        return
    seen: set[str] = set()
    for c in cands:
        cid = c.get("id", "<no id>")
        tag = f"candidate {cid}: "
        if cid in seen:
            rep.error(tag + "duplicate candidate id")
        seen.add(cid)
        for key in ["source_artifact", "summary", "disposition", "date"]:
            if not c.get(key):
                rep.error(tag + f"missing '{key}'")
        disp = c.get("disposition")
        if disp and disp not in DISPOSITIONS:
            rep.error(tag + f"disposition not in {DISPOSITIONS}")
        if c.get("date") and not RE_DATE.match(c["date"]):
            rep.error(tag + "date is not YYYY-MM-DD")
        if disp in ("Merged", "Declined") and len(c.get("rationale", "") or "") < 20:
            rep.error(tag + f"{disp} candidate needs a rationale of at least 20 characters")
        if disp in ("Entered", "Merged"):
            risk_id = c.get("risk_id")
            if not risk_id:
                rep.error(tag + f"{disp} candidate needs risk_id")
            elif risk_id not in by_id:
                rep.error(tag + f"risk_id {risk_id} is not in the register")
            elif not re.search(r"(?<![\w-])" + re.escape(cid) + r"(?![\w-])", by_id[risk_id].get("source", "")):
                rep.error(tag + f"{risk_id}.source does not name the candidate")
        if disp == "Declined" and c.get("risk_id"):
            rep.error(tag + "Declined candidate must not name a risk_id")


def validate(register: dict, rep: Report, gate: str | None = None, hazards: dict | None = None) -> None:
    missing = [key for key in ["version", "updated", "risks"] if key not in register]
    for key in missing:
        rep.error(f"register missing top-level '{key}'")
    if missing or not isinstance(register.get("risks"), list):
        if not missing:
            rep.error("register.risks must be a list")
        return
    if gate is not None and not is_gate_choice(gate):
        rep.error(f"--gate {gate} is not one of SRR, PDR, CDR, TRR, TRR-Dn, SAR")
        gate = None
    if not RE_DATE.match(register["updated"]):
        rep.error("register.updated is not YYYY-MM-DD")
    ids = [r.get("id") for r in register["risks"]]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    for d in dup:
        rep.error(f"duplicate risk id {d}")
    all_ids = set(ids)
    for risk in register["risks"]:
        validate_risk(risk, rep, all_ids, gate)
    by_id = {r.get("id"): r for r in register["risks"]}
    for rid, likelihood, children in rep.aggregate_checks:
        active_children = [by_id[c] for c in children if c in by_id and by_id[c].get("status") not in INACTIVE]
        if active_children:
            want = max(int(c.get("likelihood", 0)) for c in active_children)
            if likelihood != want:
                rep.error(f"{rid}: aggregate likelihood {likelihood} != max of children {want}")
    validate_candidates(register, rep, by_id)
    dates = [h.get("date", "") for r in register["risks"] for h in r.get("history", [])]
    dates += [c.get("date", "") for c in register.get("candidates", []) if isinstance(c, dict)]
    latest = max(dates, default="")
    if latest and latest > register["updated"]:
        rep.error(f"register.updated {register['updated']} is older than the latest history or candidate entry {latest}")
    if hazards is not None:
        check_hazards(register, hazards, rep)


def check_hazards(register: dict, hazards: dict, rep: Report) -> None:
    """Hazard link rule (process section 1): coverage, two-way link, safety at least the mapped severity."""
    hz = {h.get("id"): h for h in hazards.get("hazards", []) if isinstance(h, dict)}
    risks = [r for r in register["risks"] if r.get("status") not in INACTIVE]
    carried: dict[str, list[str]] = {}
    for r in risks:
        for hid in r.get("related", {}).get("hazard_ids", []):
            carried.setdefault(hid, []).append(r["id"])
            h = hz.get(hid)
            if h is None:
                rep.error(f"{r['id']}: related.hazard_ids names {hid}, which is not in the hazard list")
                continue
            minimum = SEVERITY_MIN_SAFETY.get(h.get("severity"))
            if minimum is None:
                rep.error(f"{hid}: severity '{h.get('severity')}' not in {sorted(SEVERITY_MIN_SAFETY)}")
            elif r["consequence"]["safety"] < minimum:
                rep.error(f"{r['id']}: safety {r['consequence']['safety']} below the minimum {minimum} for {hid} ({h.get('severity')}; hazard link rule)")
            if r["id"] not in (h.get("related_risk_ids") or []):
                rep.error(f"{hid}: related_risk_ids does not name {r['id']}, which carries it (hazard link rule back-link)")
    for hid in sorted(hz):
        h = hz[hid]
        if h.get("status") not in HAZARD_CONTROLLED and hid not in carried:
            rep.error(f"{hid}: hazard with unverified controls is carried by no active risk (hazard link rule)")
        for rid in h.get("related_risk_ids") or []:
            if rid not in carried.get(hid, []):
                rep.error(f"{hid}: related_risk_ids names {rid}, which is not an active risk naming {hid}")


def validate_with_jsonschema(register: dict, rep: Report) -> bool:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return False
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(register), key=lambda e: list(e.path)):
        path = "/".join(str(p) for p in err.path) or "<root>"
        rep.error(f"schema: {path}: {err.message}")
    return True


# ---------------------------------------------------------------------------
# Measures (SE HB 6.4.1.1 technical risk status measurements; process section 12)
# ---------------------------------------------------------------------------

def _entry_band(h: dict) -> tuple[str, bool]:
    """Band of a history entry; second value False when the entry lacks safety (override not evaluated)."""
    if "safety" in h:
        return band(h["likelihood"], h["consequence"], h["safety"]), True
    return band(h["likelihood"], h["consequence"], 0), False


def _prepared_gate_rank(review: str) -> int:
    """Rank of the gate a review point prepares: Pre-SRR prepares SRR; a gate or TRR-Dn prepares itself."""
    return max(review_rank(review), REVIEW_POINTS.index("SRR"))


def measures(register: dict) -> list[dict]:
    """One row per review point present in any history entry, in life-cycle order."""
    points = {h["review"] for r in register["risks"] for h in r["history"]}
    ordered = sorted(points, key=lambda p: (review_rank(p), p))
    latest = ordered[-1] if ordered else None
    rows = []
    for p in ordered:
        rank = review_rank(p)
        row = {"review": p, "Red": 0, "Yellow": 0, "Green": 0, "active": 0, "opened": 0,
               "closed": 0, "accepted": 0, "override_unevaluated": False, "due_open": None, "overdue": None}
        for r in register["risks"]:
            hist = r["history"]
            upto = [h for h in hist if review_rank(h["review"]) <= rank]
            if not upto:
                continue
            h = upto[-1]
            if hist[0]["review"] == p:
                row["opened"] += 1
            at = [i for i, e in enumerate(hist) if e["review"] == p]
            for i in at:
                prev = hist[i - 1]["status"] if i > 0 else None
                if hist[i]["status"] in INACTIVE and prev not in INACTIVE:
                    row["closed"] += 1
                if hist[i]["status"] == "Accepted" and prev != "Accepted":
                    row["accepted"] += 1
            if h["status"] in INACTIVE:
                continue
            row["active"] += 1
            b, evaluated = _entry_band(h)
            row[b] += 1
            if not evaluated:
                row["override_unevaluated"] = True
        if p == latest:
            prepared = _prepared_gate_rank(p)
            due_open = overdue = 0
            for r in register["risks"]:
                if r["status"] in INACTIVE:
                    continue
                for s in r["mitigation"]["steps"]:
                    if s["status"] not in ("Planned", "InProgress"):
                        continue
                    due = review_rank(s["due"])
                    if due == prepared:
                        due_open += 1
                    elif due < prepared:
                        overdue += 1
            row["due_open"], row["overdue"] = due_open, overdue
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def statement_sentence(risk: dict) -> str:
    s = risk["statement"]
    return (
        f"Given {s['condition']}, there is a possibility of {s['departure']} "
        f"adversely impacting {s['asset']}, leading to {s['consequence']}."
    )


def sort_key(risk: dict):
    """Band; within a band, safety consequence 5 first (safety override); then score, safety, likelihood, id."""
    return (
        BAND_ORDER[risk_band(risk)],
        0 if risk["consequence"]["safety"] == 5 else 1,
        -risk["score"],
        -risk["consequence"]["safety"],
        -risk["likelihood"],
        risk["id"],
    )


def next_step(risk: dict) -> str:
    gates_idx = {g: i for i, g in enumerate(GATES)}
    pending = [s for s in risk["mitigation"]["steps"] if s["status"] in ("Planned", "InProgress")]
    if not pending:
        return "none open"
    s = min(pending, key=lambda x: (gates_idx[x["due"]], x["id"]))
    return f"{s['id']} by {s['due']}"


def render_matrix(active: list[dict]) -> list[str]:
    cells: dict[tuple[int, int], list[str]] = {}
    for r in active:
        label = r["id"] + (" (R by safety override)" if red_by_override(r) else "")
        cells.setdefault((r["likelihood"], max_consequence(r)), []).append(label)
    lines = []
    header = "| Likelihood \\ Consequence | " + " | ".join(
        f"{c} {CONSEQUENCE_NAME[c]}" for c in range(1, 6)
    ) + " |"
    lines.append(header)
    lines.append("|---|" + "---|" * 5)
    for l in range(5, 0, -1):
        row = [f"**{l} {LIKELIHOOD_NAME[l]}**"]
        for c in range(1, 6):
            ids = sorted(cells.get((l, c), []))
            mark = BAND_MARK[cell_band(l, c)]
            content = f"{mark} ({l * c})"
            if ids:
                content += "<br>" + "<br>".join(ids)
            row.append(content)
        lines.append("| " + " | ".join(row) + " |")
    return lines


def render_measures(register: dict) -> list[str]:
    rows = measures(register)
    out = [
        "## Risk status measures by review",
        "",
        "Technical risk status measurements (SE HB 6.4.1.1) computed from the history entries: for each review point, the risks "
        "active at it with the band of their last assessment at or before it, the risks opened, closed or retired and accepted at it, "
        "and, for the latest review point only, the open mitigation steps due at the gate it prepares (Pre-SRR prepares SRR) and those "
        "due at an earlier gate (overdue). n/r = not recorded: step status is kept for the current assessment only. "
        "The review package plots this table under `docs/reviews/<REVIEW>/figures/`.",
        "",
        "| Review | Active | Red | Yellow | Green | Opened | Closed or retired | Accepted | Open steps due at the gate prepared | Open steps overdue |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    note = False
    for m in rows:
        mark = " (a)" if m["override_unevaluated"] else ""
        note = note or m["override_unevaluated"]
        due = "n/r" if m["due_open"] is None else str(m["due_open"])
        over = "n/r" if m["overdue"] is None else str(m["overdue"])
        out.append(
            f"| {m['review']}{mark} | {m['active']} | {m['Red']} | {m['Yellow']} | {m['Green']} | {m['opened']} | "
            f"{m['closed']} | {m['accepted']} | {due} | {over} |"
        )
    if note:
        out.append("")
        out.append("(a) At least one history entry counted in this row has no `safety` value, so the safety override was not applied to it.")
    out.append("")
    return out


def render_candidates(register: dict) -> list[str]:
    cands = register.get("candidates", [])
    if not cands:
        return []
    out = [
        "## Candidate risk dispositions",
        "",
        "Candidate risks named in other artifacts and their disposition (process section 9, Identify).",
        "",
        "| Candidate | Named in | Summary | Disposition | Risk | Rationale | Date |",
        "|---|---|---|---|---|---|---|",
    ]
    for c in sorted(cands, key=lambda x: (x["source_artifact"], x["id"])):
        risk = c.get("risk_id", "")
        link = f"[{risk}](#{risk.lower()})" if risk else "none"
        out.append(
            f"| {md_escape(c['id'])} | `{md_escape(c['source_artifact'])}` | {md_escape(c['summary'])} | {c['disposition']} | "
            f"{link} | {md_escape(c.get('rationale', '') or 'n/a')} | {c['date']} |"
        )
    counts = {d: sum(1 for c in cands if c["disposition"] == d) for d in DISPOSITIONS}
    out.append("")
    out.append(f"Totals: Entered {counts['Entered']}, Merged {counts['Merged']}, Declined {counts['Declined']}.")
    out.append("")
    return out


def render(register: dict) -> str:
    risks = register["risks"]
    active = [r for r in risks if r["status"] not in INACTIVE]
    inactive = [r for r in risks if r["status"] in INACTIVE]
    ordered = sorted(active, key=sort_key)

    out: list[str] = []
    out.append("# cwht Risk Register (rendered)")
    out.append("")
    out.append(
        f"Generated by `tools/render_risk.py` from `docs/risk/register.json` "
        f"(version {register['version']}, updated {register['updated']}). Do not edit this file; edit the JSON and re-run the tool. "
        "Scales and bands: `docs/process/06-risk-and-decision-analysis.md` sections 6 to 8."
    )
    out.append("")
    counts = {b: sum(1 for r in active if risk_band(r) == b) for b in ["Red", "Yellow", "Green"]}
    status_counts: dict[str, int] = {}
    for r in risks:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
    out.append("## Summary")
    out.append("")
    out.append("| Metric | Value |")
    out.append("|---|---|")
    out.append(f"| Active risks | {len(active)} |")
    out.append(f"| Red / Yellow / Green | {counts['Red']} / {counts['Yellow']} / {counts['Green']} |")
    out.append(f"| Closed or Retired | {len(inactive)} |")
    out.append("| By status | " + ", ".join(f"{k} {v}" for k, v in sorted(status_counts.items())) + " |")
    safety_override = [r["id"] for r in active if red_by_override(r)]
    if safety_override:
        out.append("| Red by safety override | " + ", ".join(safety_override) + " |")
    software_cat = [r["id"] for r in active if r["category"] == "software"]
    software_tag = [r["id"] for r in active if r["category"] != "software" and "software" in r.get("tags", [])]
    out.append(
        "| Software risks (SWE-086 record: category software or tag software) | "
        + (", ".join(sorted(software_cat + software_tag)) if software_cat or software_tag else "none")
        + f" ({len(software_cat)} category software, {len(software_tag)} tagged software) |"
    )
    tag_index: dict[str, list[str]] = {}
    for r in active:
        for t in r.get("tags", []):
            tag_index.setdefault(t, []).append(r["id"])
    for t in sorted(tag_index):
        out.append(f"| Tagged `{t}` | " + ", ".join(tag_index[t]) + " |")
    out.append("")

    out.extend(render_measures(register))

    out.append("## 5x5 matrix (active risks)")
    out.append("")
    out.append(
        "Cell label: band letter (R = Red, Y = Yellow, G = Green) and likelihood x consequence. "
        "A risk sits in the cell of its likelihood and its maximum consequence dimension. "
        "Risks with safety consequence 5 and likelihood 2 or more are Red regardless of the cell band (safety override) "
        "and are marked \"(R by safety override)\" in their cell."
    )
    out.append("")
    out.extend(render_matrix(active))
    out.append("")

    out.append("## Ranked list (active risks)")
    out.append("")
    out.append(
        "Sorted by band; within a band, risks with safety consequence 5 first (the safety override of process section 7), "
        "then by score, safety consequence, likelihood and id."
    )
    out.append("")
    out.append("| Rank | ID | Title | Category | L | C (driving dimension) | Score | Band | Status | Trend | Owner | Next step |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(ordered, 1):
        driving = ", ".join(DIM_LABEL[d] for d in driving_dimensions(r))
        band_text = risk_band(r) + (" (safety override)" if red_by_override(r) else "")
        out.append(
            f"| {i} | [{r['id']}](#{r['id'].lower()}) | {md_escape(r['title'])} | {r['category']} | {r['likelihood']} | "
            f"{max_consequence(r)} ({driving}) | {r['score']} | {band_text} | {r['status']} | {r['trend']} | {r['owner']} | {next_step(r)} |"
        )
    out.append("")

    out.extend(render_candidates(register))

    out.append("## Risk details")
    out.append("")
    for r in ordered:
        out.extend(render_risk(r))
    if inactive:
        out.append("## Closed and retired risks")
        out.append("")
        out.append("| ID | Title | Status | Last score | Closure note |")
        out.append("|---|---|---|---|---|")
        for r in sorted(inactive, key=lambda x: x["id"]):
            out.append(f"| {r['id']} | {md_escape(r['title'])} | {r['status']} | {r['score']} | {md_escape(r['history'][-1]['note'])} |")
        out.append("")
        for r in sorted(inactive, key=lambda x: x["id"]):
            out.extend(render_risk(r))
    return "\n".join(out).rstrip() + "\n"


def render_risk(r: dict) -> list[str]:
    out: list[str] = []
    b = risk_band(r)
    out.append(f"### {r['id']}")
    out.append("")
    out.append(f"**{md_escape(r['title'])}**")
    out.append("")
    out.append(f"{statement_sentence(r)}")
    out.append("")
    out.append("| Field | Value |")
    out.append("|---|---|")
    out.append(f"| Category | {r['category']}" + (f" (tags: {', '.join(r['tags'])})" if r.get("tags") else "") + " |")
    out.append(f"| Likelihood | {r['likelihood']} ({LIKELIHOOD_NAME[r['likelihood']]}) |")
    cons = " / ".join(f"{DIM_LABEL[d]} {r['consequence'][d]}" for d in DIMS)
    out.append(f"| Consequence by dimension | {cons} |")
    driving = ", ".join(DIM_LABEL[d] for d in driving_dimensions(r))
    out.append(f"| Consequence (max) | {max_consequence(r)} ({CONSEQUENCE_NAME[max_consequence(r)]}); driving: {driving} |")
    out.append(f"| Score / band | {r['score']} / {b}" + (" (safety override)" if red_by_override(r) else "") + " |")
    out.append(f"| Assessment confidence | {r['assessment_confidence']} |")
    out.append(f"| Status / trend | {r['status']} / {r['trend']} |")
    out.append(f"| Owner | {r['owner']} |")
    out.append(f"| Opened / horizon | {r['opened']} / {r['horizon']} |")
    out.append(f"| Last assessed | {r['last_assessed']['date']} ({r['last_assessed']['review']}) |")
    out.append(f"| Source | {md_escape(r['source'])} |")
    out.append(f"| Strategy | {r['mitigation']['strategy']} |")
    if r["mitigation"].get("plan_approval"):
        pa = r["mitigation"]["plan_approval"]
        out.append(f"| Plan approval | {pa['date']}, memo {md_escape(pa['decision_memo'])} |")
    elif risk_band(r) == "Red" and r["status"] not in PLAN_EXEMPT:
        out.append("| Plan approval | pending (owner approves Red plans at the next review, process section 8) |")
    if r.get("acceptance"):
        a = r["acceptance"]
        out.append(f"| Acceptance | {a['date']}, residual score {a['residual_score']}, memo {md_escape(a['decision_memo'])} |")
    out.append("")
    out.append(f"**Likelihood rationale.** {r['likelihood_rationale']}")
    out.append("")
    out.append(f"**Consequence rationale.** {r['consequence_rationale']}")
    out.append("")
    out.append("**Mitigation steps**")
    out.append("")
    if r["mitigation"]["steps"]:
        out.append("| Step | Action | Artifact | Due | Status |")
        out.append("|---|---|---|---|---|")
        for s in r["mitigation"]["steps"]:
            ev = f" ({md_escape(s['evidence'])})" if s.get("evidence") else ""
            out.append(f"| {s['id']} | {md_escape(s['action'])} | {md_escape(s['artifact'])} | {s['due']} | {s['status']}{ev} |")
    else:
        out.append("None (strategy " + r["mitigation"]["strategy"] + ").")
    out.append("")
    out.append("**Triggers**")
    out.append("")
    if r["mitigation"]["triggers"]:
        out.append("| Condition | Response |")
        out.append("|---|---|")
        for t in r["mitigation"]["triggers"]:
            out.append(f"| {md_escape(t['condition'])} | {md_escape(t['response'])} |")
    else:
        out.append("None.")
    out.append("")
    out.append(f"**Fallback.** {r['mitigation']['fallback']}")
    out.append("")
    rel = r["related"]
    rel_parts = []
    for key in ["requirement_ids", "hazard_ids", "adr_ids", "trade_study_ids", "tpm_ids", "ncr_ids", "cr_ids", "stakeholder_input_ids", "risk_ids"]:
        vals = rel.get(key, [])
        if vals:
            rel_parts.append(f"{key.replace('_ids', '').replace('_', ' ')}: {', '.join(vals)}")
    out.append("**Related.** " + ("; ".join(rel_parts) if rel_parts else "none yet"))
    out.append("")
    out.append(f"**Closure criteria.** {r['closure_criteria']}")
    out.append("")
    out.append("**History**")
    out.append("")
    out.append("| Date | Review | L | C | Safety | Score | Status | Note |")
    out.append("|---|---|---|---|---|---|---|---|")
    for h in r["history"]:
        out.append(
            f"| {h['date']} | {h['review']} | {h['likelihood']} | {h['consequence']} | {h.get('safety', 'n/r')} | "
            f"{h['score']} | {h['status']} | {md_escape(h['note'])} |"
        )
    out.append("")
    if r.get("notes"):
        out.append(f"**Notes.** {r['notes']}")
        out.append("")
    return out


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate and render the cwht risk register.")
    ap.add_argument("--register", type=Path, default=REGISTER, help="path to register.json")
    ap.add_argument("--output", type=Path, default=OUTPUT, help="path of the rendered Markdown")
    ap.add_argument("--check", action="store_true", help="validate and compare the rendered file with a fresh render; write nothing")
    ap.add_argument("--gate", help="review package being prepared: SRR, PDR, CDR, TRR, TRR-Dn or SAR")
    ap.add_argument("--hazards", type=Path, help="docs/safety/hazards.json for the hazard link rule cross-check")
    ap.add_argument("--quiet", action="store_true", help="print errors and warnings only")
    args = ap.parse_args(argv)

    try:
        register = json.loads(args.register.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {args.register}: {exc}", file=sys.stderr)
        return 1
    hazards = None
    if args.hazards is not None:
        try:
            hazards = json.loads(args.hazards.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot read {args.hazards}: {exc}", file=sys.stderr)
            return 1

    rep = Report()
    used_schema = validate_with_jsonschema(register, rep)
    if not used_schema:
        rep.warn("jsonschema not importable: JSON Schema validation skipped; run with /Users/robinonsay/rust/cwht/.venv/bin/python")
    validate(register, rep, gate=args.gate, hazards=hazards)

    text = None
    if not rep.errors:
        text = render(register)
        if args.check:
            current = args.output.read_text(encoding="utf-8") if args.output.exists() else None
            if current != text:
                rep.error(STALE_MESSAGE)

    for w in rep.warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    for e in rep.errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if rep.errors:
        print(f"{len(rep.errors)} error(s); nothing written.", file=sys.stderr)
        return 1

    if not args.quiet:
        n = len(register["risks"])
        c = len(register.get("candidates", []))
        extras = []
        if args.gate:
            extras.append(f"gate {args.gate}")
        if hazards is not None:
            extras.append("hazard cross-check")
        print(
            f"register OK: {n} risks, {c} candidates, {len(rep.warnings)} warning(s), "
            f"jsonschema {'used' if used_schema else 'not available (structural checks only)'}"
            + (f", {', '.join(extras)}" if extras else "")
        )
    if args.check:
        if not args.quiet:
            print(f"{args.output} is current")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    if not args.quiet:
        print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
