"""Checker for the WP-PDR-33 keyer host study (docs/design/analysis/keyer-host-study.md).

Run from the repository root:
    .venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py

It recomputes every number the note states, asserts each acceptance value, writes
keyer-host-study-results.json and the four plots beside this file, and exits 1 on any failed
assertion (08 section 3.4). Pass --no-plots to skip the plots.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import keyer_model as m  # noqa: E402

FAILS: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


# Acceptance constants, each traced to its governing text (note section 4).
SQUEEZE_LIMIT_BASELINE_S = 2.0        # REQ-SYS-184 as baselined: "more than 2 s (TBR)"
SQUEEZE_CR_BRANCH_DITS = 16.0         # REQ-SYS-184 tbr.plan: "the longer of 2 s and 16 dit times"
SQUEEZE_PROPOSED_DITS = 20.0          # proposed in the note section 6.1
NOGAP_WINDOW_S = 30.0                 # REQ-SYS-054: "30 s (TBR)"
NOGAP_COUNT = 128                     # REQ-SYS-054: "128 consecutive identical elements"
INTERLOCK_MS = 500                    # REQ-SYS-052 "500 ms (TBR)"; REQ-SW-KEYER-022 "500 consecutive samples (TBR)"
MANUAL_TIMEOUT_S = 5.0                # REQ-SYS-053, REQ-SW-KEYER-026 "5 s (TBR)"
MANUAL_RANGE_S = (2.0, 6.0)           # REQ-SYS-053 tbr.plan "configurable range (2 to 6 s)"
HW_CUTOFF_MIN_S = 7.5                 # REQ-SYS-055 "7.5 s to 13 s (TBR)"
WATCHDOG_RESET_S = 2.0                # REQ-SYS-131 "within 2 s (TBR)"
BENCH_MODE_S = 120.0                  # REQ-SYS-188 "at most 120 s (TBR)"
BACKSTOP_MIN_S = 150.0                # REQ-SYS-180 "150 s to 180 s (TBR)"
TONE_S = 60.0                         # REQ-SYS-189 "at most 60 s (TBR)"
TIMING_TOL = 0.005                    # REQ-SW-KEYER-013: +/-0.5 percent or 0.2 ms
DEBOUNCE_EXTRA_MS = 3.0               # F6: break 5 samples minus make 2 samples

SPEEDS_SEARCH = (5, 10, 15, 25, 50)
SPEEDS_ALL = tuple(range(5, 51))
SWITCHPOINTS = (0.0, 0.5, 0.9)        # REQ-SW-KEYER-009 range 0 to 90 percent, default 50 percent


def main(plots: bool = True) -> int:
    results: dict = {}

    # ---- 1. Model validation: golden vectors (F6, F7) ------------------------------------
    g = m.run_golden()
    for vid, ok, got, exp in g:
        check(ok, f"golden vector {vid} reproduced (got {got})")
    results["golden_vectors"] = {"count": len(g), "passed": sum(1 for x in g if x[1])}

    # ---- 2. Squeeze windows by simulation against the analytic boundary ------------------
    table = []
    cases = []
    for first in ("dit", "dah"):
        for k in range(2, 7):
            for mode, s in (("A", 0.5), ("B", 0.0), ("B", 0.5), ("B", 0.9)):
                cases.append(("iambic", first, k, mode, s))
    for x in ("dit", "dah"):
        for b in range(1, 5):
            cases.append(("ult", x, b, "U", 0.5))
    for kind, first, n, mode, s in cases:
        for w in SPEEDS_SEARCH:
            r = m.squeeze_search(kind, first, n, mode, w, s)
            dit_ms = m.dit_us(w) / 1000.0
            ok = r["ok"]
            agree = ok and abs((r["latest_t1"] + 4) - r["analytic_latest_ms"]) <= 1.0 + 1e-9
            check(ok and agree and r["mid_ok"] and r["wrong_beyond"],
                  f"squeeze window {kind} {r['target']} mode {mode} S={s} {w} WPM: latest correct "
                  f"release {r.get('latest_t1')} ms raw (analytic {r['analytic_latest_ms']:.1f} ms "
                  f"debounced), mid-window correct, later release wrong")
            table.append({
                "kind": kind, "pattern": r["target"], "mode": mode, "switchpoint": s, "wpm": w,
                "latest_raw_release_ms": r.get("latest_t1"),
                "analytic_latest_debounced_ms": round(r["analytic_latest_ms"], 3),
                "max_both_closed_ms": r.get("max_both_ms"),
                "max_both_closed_dits": round(r.get("max_both_ms", 0.0) / dit_ms, 3),
                "mid_window_both_closed_ms": r.get("mid_both_ms"),
            })
    results["squeeze_windows"] = table

    # ---- 3. Worst squeeze per character and mode (dits) -----------------------------------
    worst = {}
    for label, mode, s in (("A", "A", 0.5), ("B S=0", "B", 0.0), ("B S=0.5", "B", 0.5),
                           ("B S=0.9", "B", 0.9), ("U", "U", 0.5)):
        per_char = {}
        for ch, code in m.MORSE.items():
            d, where = m.worst_squeeze_dits(code, mode, s)
            per_char[ch] = d
        top = max(per_char.values())
        worst[label] = {"max_dits": round(top, 3),
                        "chars": sorted([c for c, v in per_char.items() if abs(v - top) < 1e-9]),
                        "C": per_char["C"], "K": per_char["K"], "Q": per_char["Q"],
                        "period": per_char["."]}
        itu_top = max(v for c, v in per_char.items() if c in m.ITU)
        worst[label]["max_dits_itu_only"] = round(itu_top, 3)
    results["worst_squeeze_by_mode"] = worst
    check(abs(worst["A"]["max_dits"] - 18.0) < 1e-9, "Iambic A worst correct squeeze is 18 dits")
    check(abs(worst["U"]["max_dits"] - 18.0) < 1e-9, "Ultimatic worst correct squeeze is 18 dits")
    for lab, full, itu in (("B S=0", 16.0, 14.0), ("B S=0.5", 16.5, 15.5), ("B S=0.9", 16.9, 16.7)):
        check(abs(worst[lab]["max_dits"] - full) < 1e-9 and abs(worst[lab]["max_dits_itu_only"] - itu) < 1e-9,
              f"Iambic {lab} worst is {full} dits (semicolon), {itu} dits over the ITU set (period)")
    check(abs(worst["A"]["C"] - 12.0) < 1e-9, "letter C worst squeeze in Iambic A is 12 dits")

    # Direct whole-character cross-checks (runs inside a character behave as isolated runs).
    # Each case: character, mode, and the operator script as a function of the release t1 (raw ms)
    # of the squeeze; the other contact timings are fixed inside the correct window (note 3.3).
    cross = []
    w = 5
    d = m.dit_us(w) / 1000.0
    composite = (
        # SK ...-.- : dit held throughout; dah closed after the third dit starts; both open at t1
        ("<SK>", "A", 0.5, lambda t1: ([(0, t1)], [(int(math.ceil(1 + 4 * d)) + 1, t1)]), 16.0),
        # Y -.-- : dah held until inside the fourth element; dit closed at raw 1 ms, opened at t1
        ("Y", "A", 0.5, lambda t1: ([(1, t1)], [(0, int(1 + 13 * d))]), 10.0),
        # ' .----. in Ultimatic: dit held until inside the final dit; dah closed at raw 1 ms, opened at t1
        ("'", "U", 0.5, lambda t1: ([(0, int(1 + 19 * d))], [(1, t1)]), 18.0),
    )
    for ch, mode, s, script, end_dits in composite:
        code = m.MORSE[ch]
        best, where = m.worst_squeeze_dits(code, mode, s)
        total = int((end_dits + 10) * d)
        found = None
        for t1 in range(int(1 + (end_dits + 3) * d), int(1 + (end_dits - 5) * d), -1):
            dv, hv = script(t1)
            r = m.simulate(mode, w, dv, hv, total, switchpoint=s)
            if r.pattern() == code:
                found = (t1, m.both_closed_max_ms(r) / d)
                break
        cross.append({"char": ch, "mode": mode, "analytic_run_bound_dits": best,
                      "sim_latest_raw_release_ms": found[0] if found else None,
                      "sim_max_both_dits": round(found[1], 3) if found else None})
        check(found is not None and found[1] <= best + 0.01 and found[1] >= best - 0.5,
              f"whole-character check {ch} mode {mode} at 5 WPM: simulated longest correct squeeze "
              f"{round(found[1], 3) if found else None} dits within 0.5 dit below the run bound {best} dits")
    results["whole_character_checks"] = cross

    # ---- 4. Limits against correct sending, 5 to 50 WPM -----------------------------------
    def limit_ms(option: str, w: float) -> float:
        dit_ms = m.dit_us(w) / 1000.0
        if option == "baseline":
            return SQUEEZE_LIMIT_BASELINE_S * 1000.0
        if option == "cr16":
            return max(SQUEEZE_LIMIT_BASELINE_S * 1000.0, SQUEEZE_CR_BRANCH_DITS * dit_ms)
        return max(SQUEEZE_LIMIT_BASELINE_S * 1000.0, SQUEEZE_PROPOSED_DITS * dit_ms)

    trip = {}
    for option in ("baseline", "cr16", "proposed"):
        trip[option] = {}
        for label in worst:
            speeds = []
            for w in SPEEDS_ALL:
                dit_ms = m.dit_us(w) / 1000.0
                # conservative squeeze seen by the monitor: debounce offset and +0.5 % timing
                seen = worst[label]["max_dits"] * dit_ms * (1 + TIMING_TOL) + DEBOUNCE_EXTRA_MS
                if seen > limit_ms(option, w):
                    speeds.append(w)
            trip[option][label] = speeds
        trip[option]["C_modeA"] = [w for w in SPEEDS_ALL
                                   if 12.0 * m.dit_us(w) / 1000.0 * (1 + TIMING_TOL)
                                   + DEBOUNCE_EXTRA_MS > limit_ms(option, w)]
    results["squeeze_trip_speeds_wpm"] = trip
    check(trip["baseline"]["A"] == list(range(5, 11)),
          f"baseline 2 s trips correct Iambic A sending at 5 to 10 WPM (got {trip['baseline']['A']})")
    check(trip["baseline"]["C_modeA"] == list(range(5, 8)),
          f"baseline 2 s trips a squeezed C in Iambic A at 5 to 7 WPM (got {trip['baseline']['C_modeA']})")
    check(trip["cr16"]["A"] == list(range(5, 11)),
          f"tbr CR branch 'longer of 2 s and 16 dits' still trips Iambic A at 5 to 10 WPM "
          f"(got {trip['cr16']['A']})")
    check(all(not v for v in trip["proposed"].values()),
          "proposed 'longer of 2 s and 20 dit times' trips no correct sending at 5 to 50 WPM")
    min_margin = min(limit_ms("proposed", w) - (18.0 * m.dit_us(w) / 1000.0 * (1 + TIMING_TOL)
                                                + DEBOUNCE_EXTRA_MS) for w in SPEEDS_ALL)
    results["squeeze_proposed_min_margin_ms"] = round(min_margin, 1)
    check(min_margin > 0, f"proposed squeeze limit minimum margin {min_margin:.1f} ms > 0")

    # REQ-SYS-184 verification-note cases: holds of 1.9, 2.1 and 60 s after boot, and the
    # squeezed C, K and Q at 5 WPM, against the baselined and the proposed limit
    cases184 = []
    for w in (5, 25, 50):
        for hold in (1.9, 2.1, 60.0):
            seen_ms = hold * 1000.0 + DEBOUNCE_EXTRA_MS
            cases184.append({"case": f"both closed {hold} s", "wpm": w,
                             "baseline_trips": seen_ms > limit_ms("baseline", w),
                             "proposed_trips": seen_ms > limit_ms("proposed", w),
                             "proposed_limit_s": round(limit_ms("proposed", w) / 1000.0, 3)})
    for ch in ("C", "K", "Q"):
        for label in ("A", "B S=0.5", "U"):
            dits = worst[label][ch]
            w = 5
            seen_ms = dits * m.dit_us(w) / 1000.0 * (1 + TIMING_TOL) + DEBOUNCE_EXTRA_MS
            cases184.append({"case": f"squeezed {ch}, worst correct release, mode {label}", "wpm": w,
                             "both_closed_s": round(dits * m.dit_us(w) / 1e6, 3),
                             "baseline_trips": seen_ms > limit_ms("baseline", w),
                             "proposed_trips": seen_ms > limit_ms("proposed", w)})
    results["req_sys_184_cases"] = cases184
    check(all(not c["proposed_trips"] for c in cases184 if c["case"].startswith("squeezed")),
          "no squeezed C, K or Q at 5 WPM trips the proposed limit")
    check(all(c["proposed_trips"] for c in cases184 if c["case"] == "both closed 60.0 s"),
          "a 60 s squeeze trips the proposed limit at 5, 25 and 50 WPM")
    check(not any(c["proposed_trips"] or c["baseline_trips"] for c in cases184
                  if c["case"] == "both closed 1.9 s"), "a 1.9 s squeeze trips neither limit")

    # Fault: both contacts closed after boot (headphones or shorted TRS), stream stopped at limit
    fault = []
    for w in (5, 10, 15, 25, 50):
        lim_s = limit_ms("proposed", w) / 1000.0
        stream = m.fault_stream_alternating(w, 60.0)
        span, cnt, t_trip, cause = m.watchdog_relative(stream)
        fault.append({"wpm": w, "squeeze_trip_s": round(lim_s, 3),
                      "baseline_trip_s": SQUEEZE_LIMIT_BASELINE_S,
                      "nogap_trip_s": t_trip, "nogap_cause": cause})
        check(lim_s < NOGAP_WINDOW_S and lim_s < HW_CUTOFF_MIN_S,
              f"squeeze fault at {w} WPM stops at {lim_s:.2f} s, before the 30 s window")
    results["squeeze_fault_stop"] = fault

    # Speed source of the squeeze limit (INSP-075 finding-2): SW-SAFE takes the dit length from the
    # configuration-guarded speed value; a complement mismatch or a value outside 5 to 50 WPM is
    # replaced by 50 WPM. The limit then lies in [2.00 s, 4.80 s] whatever the stored value.
    src = []
    for stored, comp in ((0, True), (1, True), (4, True), (5, True), (12, True), (15, True),
                         (50, True), (51, True), (99, True), (255, True), (-1, True), (None, True),
                         (15, False), (5, False)):
        lim = m.squeeze_limit_monitor_ms(stored, comp) / 1000.0
        src.append({"stored_wpm": stored, "complement_ok": comp, "limit_s": round(lim, 3)})
    results["squeeze_speed_source"] = src
    lims = [x["limit_s"] for x in src]
    results["squeeze_limit_bounds_s"] = [min(lims), max(lims)]
    check(min(lims) >= SQUEEZE_LIMIT_BASELINE_S - 1e-9 and max(lims) <= 4.8 + 1e-9,
          f"squeeze limit with the guarded speed lies in {min(lims)} to {max(lims)} s for every stored "
          f"value, range end and complement failure")
    # A monitor value above the true stream speed shortens the limit (earlier stop, nuisance side);
    # a value below it lengthens the limit, at most to 4.80 s (5 WPM)
    mism = []
    for true_w in (5, 10, 20, 50):
        for mon_w in (5, 10, 20, 50):
            lim = m.squeeze_limit_monitor_ms(mon_w) / 1000.0
            worst_ok = worst["A"]["max_dits"] * m.dit_us(true_w) / 1e6 * (1 + TIMING_TOL) + DEBOUNCE_EXTRA_MS / 1000.0
            mism.append({"stream_wpm": true_w, "monitor_wpm": mon_w, "fault_stop_s": round(lim, 3),
                         "correct_squeeze_cut": worst_ok > lim})
    results["squeeze_speed_mismatch"] = mism
    check(all(x["fault_stop_s"] <= 4.8 + 1e-9 for x in mism),
          "every monitor and stream speed pair stops a squeeze fault by 4.80 s")
    check(all(not x["correct_squeeze_cut"] for x in mism if x["monitor_wpm"] <= x["stream_wpm"]),
          "a monitor speed at or below the stream speed never cuts a correct squeeze")

    # ---- 5. Paddle watchdog (REQ-SYS-054): correct sending in every key mode --------------
    # Three rules are compared (note section 6.2): "current" (baselined 7 dits or 500 ms at the
    # selected speed), "rev1" (2 dit times at the selected speed, the revision 1 proposal) and "rev2"
    # (the self-referenced rule of revision 2, keyer_model.watchdog_relative, no keyer parameter).
    def run_rule(rule: str, stream, sel_wpm: float):
        if rule == "current":
            return m.paddle_watchdog(stream, sel_wpm, m.gap_rule_current)
        if rule == "rev1":
            return m.paddle_watchdog(stream, sel_wpm, m.gap_rule_proposed)
        return m.watchdog_relative(stream)

    RULES = ("current", "rev1", "rev2")
    profiles = {"nominal 3/7": (3.0, 7.0), "short word 3/6": (3.0, 6.0),
                "short word 3/5": (3.0, 5.0), "fast 2.5/5": (2.5, 5.0),
                "spread 4.5/10": (4.5, 10.0)}
    # 5a. Corpus P: keyer-timed paddle sending (Iambic A, Iambic B, Ultimatic), every speed
    nogap = {}
    for rule in RULES:
        nogap[rule] = {}
        for pname, (ls, ws) in profiles.items():
            rows = []
            for w in SPEEDS_ALL:
                qso = m.key_stream(m.CORPUS_QSO, w, ls, ws)
                stress = m.key_stream(m.CORPUS_STRESS, w, ls, ws)
                s1, c1, t1, _ = run_rule(rule, qso, w)
                s2, c2, t2, _ = run_rule(rule, stress, w)
                rows.append({"wpm": w, "qso_max_span_s": round(s1, 3), "qso_max_count": c1,
                             "qso_trip": t1 is not None, "stress_max_span_s": round(s2, 3),
                             "stress_max_count": c2, "stress_trip": t2 is not None})
            nogap[rule][pname] = rows
    results["nogap_corpus"] = nogap
    cur_nom = nogap["current"]["nominal 3/7"]
    cur_trip_speeds = [r["wpm"] for r in cur_nom if r["stress_trip"]]
    results["nogap_current_nominal_stress_trip_wpm"] = cur_trip_speeds
    check(bool(cur_trip_speeds),
          f"current 7-dit/500 ms rule trips on the stress tokens with nominal spacing at "
          f"{cur_trip_speeds} WPM")
    check(not any(r["qso_trip"] for r in cur_nom),
          "current rule does not trip on the QSO corpus with nominal ITU spacing")
    short_trip = sorted({r["wpm"] for p in ("short word 3/6", "short word 3/5", "fast 2.5/5")
                         for r in nogap["current"][p] if r["qso_trip"]})
    results["nogap_current_short_spacing_qso_trip_wpm"] = short_trip
    check(bool(short_trip),
          f"current rule trips the QSO corpus when word spaces are shorter than 7 dits, at "
          f"{short_trip[:3]}...{short_trip[-3:] if short_trip else ''} WPM")

    def corpus_max(rows_by_profile, key_a, key_b):
        return max(max(r[key_a], r[key_b]) for rows in rows_by_profile.values() for r in rows)

    for rule in ("rev1", "rev2"):
        bad = [(p, r["wpm"]) for p, rows in nogap[rule].items() for r in rows
               if r["qso_trip"] or r["stress_trip"]]
        check(not bad, f"{rule} rule trips no paddle corpus sending, every profile, 5 to 50 WPM")
    results["nogap_paddle_max_span_s"] = {r: corpus_max(nogap[r], "qso_max_span_s", "stress_max_span_s")
                                          for r in RULES}
    results["nogap_paddle_max_count"] = {r: corpus_max(nogap[r], "qso_max_count", "stress_max_count")
                                         for r in RULES}

    # 5b. Corpus B: Bug-mode sending. Automatic dits at the selected speed, manual dahs of 3 or 6
    # Bug dits or drawn from 2.5 to 6, operator spacing in the unit k x Bug dit (note section 3.4)
    BUG_K = (0.75, 1.0, 1.5, 2.0)
    BUG_SPACING = {"3/7": (3.0, 7.0), "3/5": (3.0, 5.0), "2.5/5": (2.5, 5.0), "4.5/10": (4.5, 10.0)}
    BUG_DAHS = {"dah 3": 3.0, "dah 6": 6.0, "dah 2.5 to 6": (2.5, 6.0)}
    SPEEDS_HAND = (5, 6, 7, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50)
    bug = {r: {"max_span_s": 0.0, "max_count": 0, "trips": []} for r in RULES}
    n_bug = 0
    for k in BUG_K:
        for sp_name, (ls, ws) in BUG_SPACING.items():
            for dah_name, dah in BUG_DAHS.items():
                for w in SPEEDS_HAND:
                    for seed in (1, 2):
                        for cname, txt in (("qso", m.CORPUS_QSO), ("stress", m.CORPUS_STRESS)):
                            st = m.key_stream_bug(txt, w, k, ls, ws, dah, seed=seed)
                            n_bug += 1
                            for rule in RULES:
                                span, cnt, t, _ = run_rule(rule, st, w)
                                b = bug[rule]
                                b["max_span_s"] = max(b["max_span_s"], round(span, 3))
                                b["max_count"] = max(b["max_count"], cnt)
                                if t is not None:
                                    b["trips"].append({"k": k, "spacing": sp_name, "dah": dah_name,
                                                       "wpm": w, "seed": seed, "corpus": cname,
                                                       "trip_s": round(t, 2)})
    for rule in RULES:
        bug[rule]["n_trips"] = len(bug[rule]["trips"])
        bug[rule]["trips"] = bug[rule]["trips"][:12]
    results["nogap_bug"] = {"streams": n_bug, **bug}
    check(bug["rev2"]["n_trips"] == 0,
          f"rev2 rule trips none of the {n_bug} Bug-mode streams (dahs up to 6 dits, k 0.75 to 2)")
    check(bug["rev1"]["n_trips"] > 0,
          f"rev1 2-dit rule trips {bug['rev1']['n_trips']} Bug-mode streams (operator spacing "
          f"faster than the Bug dits), so revision 1 does not hold for Bug sending")

    # 5c. Corpus S: Straight-key sending, every element and space hand-timed. The current and rev1
    # rules use the selected keyer speed, which has no relation to the hand speed; the worst
    # setting is the slowest (5 WPM), the INSP-071 finding-1 counter-example
    hand = {r: {"max_span_s": 0.0, "max_count": 0, "trips_same_speed": 0, "trips_keyer_5wpm": 0}
            for r in RULES}
    n_hand = 0
    for pname in m.HAND_PROFILES:
        for w in SPEEDS_HAND:
            for seed in (1, 2, 3):
                for txt in (m.CORPUS_QSO, m.CORPUS_STRESS):
                    st = m.key_stream_hand(txt, w, pname, seed=seed)
                    n_hand += 1
                    for rule in RULES:
                        span, cnt, t, _ = run_rule(rule, st, w)
                        h = hand[rule]
                        h["max_span_s"] = max(h["max_span_s"], round(span, 3))
                        h["max_count"] = max(h["max_count"], cnt)
                        h["trips_same_speed"] += t is not None
                        if rule != "rev2":
                            h["trips_keyer_5wpm"] += run_rule(rule, st, 5)[2] is not None
    results["nogap_straight"] = {"streams": n_hand, **hand}
    check(hand["rev2"]["trips_same_speed"] == 0,
          f"rev2 rule trips none of the {n_hand} Straight-key streams (5 hand profiles, 5 to 50 WPM)")
    cx = m.key_stream(m.CORPUS_QSO, 20)
    cx_rows = {}
    for rule in RULES:
        span, cnt, t, cause = run_rule(rule, cx, 5)
        cx_rows[rule] = {"trip_s": None if t is None else round(t, 2), "cause": cause}
    results["nogap_insp071_counterexample"] = {"text": "QSO corpus hand-sent at 20 WPM, keyer set to 5 WPM",
                                               **cx_rows}
    check(cx_rows["current"]["trip_s"] == 30.24 and cx_rows["rev1"]["trip_s"] == 30.24,
          "INSP-071 counter-example reproduced: current and rev1 trip at 30.24 s")
    check(cx_rows["rev2"]["trip_s"] is None, "rev2 rule does not trip the INSP-071 counter-example")
    rev2_span = max(results["nogap_paddle_max_span_s"]["rev2"], bug["rev2"]["max_span_s"],
                    hand["rev2"]["max_span_s"])
    rev2_count = max(results["nogap_paddle_max_count"]["rev2"], bug["rev2"]["max_count"],
                     hand["rev2"]["max_count"])
    results["nogap_rev2_max_span_s"] = rev2_span
    results["nogap_rev2_max_count"] = rev2_count
    check(rev2_span < NOGAP_WINDOW_S / 2,
          f"rev2 rule: longest span without a qualifying gap over P, B and S is {rev2_span} s, "
          f"under half the 30 s window")
    check(rev2_count < NOGAP_COUNT / 2,
          f"rev2 rule: largest count over P, B and S is {rev2_count}, below 64, half of 128")

    # ---- 5d. Fault side (INSP-075 finding-1): keyer-fault streams under the three rules ----
    import random
    rng = random.Random(7)
    catalogue = []
    for f in (1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0):
        catalogue.append(("uniform", f"held dit, space {f:g} dits", [(1.0, f)]))
        catalogue.append(("uniform", f"held dah, space {f:g} dits", [(3.0, f)]))
        catalogue.append(("uniform", f"alternating, space {f:g} dits", [(1.0, f), (3.0, f)]))
    for ratio in (1.0, 2.0, 4.0, 6.0):
        catalogue.append(("uniform", f"alternating, ratio {ratio:g}", [(1.0, 1.0), (ratio, 1.0)]))
    for dlt in (-0.5, 0.5, 0.9):
        catalogue.append(("uniform", f"alternating, weight shift {dlt:+g} dit",
                          [(1.0 + dlt, 1.0 - dlt), (3.0 + dlt, 1.0 - dlt)]))
    catalogue.append(("uniform", "stuck element timer (continuous key-down)", [(None, None)]))
    catalogue.append(("uniform", "random dit/dah order, 1-dit spaces",
                      [(rng.choice((1.0, 3.0)), 1.0) for _ in range(997)]))
    catalogue.append(("equal elements", "dits, spaces randomly 1 or 3 dits",
                      [(1.0, rng.choice((1.0, 3.0))) for _ in range(997)]))
    for f in (2.0, 3.0, 4.0, 7.0):
        catalogue.append(("periodic", f"dit-dah pairs, spaces 1 and {f:g} dits", [(1.0, 1.0), (3.0, f)]))
        catalogue.append(("periodic", f"dit pairs, spaces 1 and {f:g} dits", [(1.0, 1.0), (1.0, f)]))
        catalogue.append(("periodic", f"dah pairs, spaces 1 and {f:g} dits", [(3.0, 1.0), (3.0, f)]))
    catalogue.append(("periodic", "repeated S, spaces 1, 1, 3 dits", [(1.0, 1.0), (1.0, 1.0), (1.0, 3.0)]))
    catalogue.append(("periodic", "repeated K, spaces 1, 1, 3 dits", [(3.0, 1.0), (1.0, 1.0), (3.0, 3.0)]))
    catalogue.append(("text-like", "random elements, spaces randomly 1 or 3 dits",
                      [(rng.choice((1.0, 3.0)), rng.choice((1.0, 3.0))) for _ in range(997)]))
    HORIZON_S = 300.0
    faults = []
    for cls, name, cyc in catalogue:
        for w in (5, 15, 25, 50):
            dit_s = m.dit_us(w) / 1e6
            period_s = (0.0 if cyc[0][0] is None else max(e + g for e, g in cyc)) * dit_s
            max_gap_s = 0.0 if cyc[0][0] is None else max(g for _e, g in cyc) * dit_s
            row = {"class": cls, "stream": name, "wpm": w, "max_gap_s": round(max_gap_s, 3)}
            for rule in RULES:
                st = m.fault_stream_cycle(w, HORIZON_S, cyc)
                _s, _c, t, cause = run_rule(rule, st, w)
                st2, t0 = m.with_lead_in(lambda t0, cyc=cyc, w=w: m.fault_stream_cycle(w, HORIZON_S, cyc, t0),
                                         w, m.CORPUS_QSO, 15.0)
                _s, _c, t2, cause2 = run_rule(rule, st2, w)
                row[rule] = {"from_idle_s": None if t is None else round(t, 2), "cause": cause,
                             "after_sending_s": None if t2 is None else round(t2 - t0 / 1e6, 2),
                             "cause_after_sending": cause2}
            row["cycle_s"] = round(period_s, 3)
            faults.append(row)
    results["nogap_fault_catalogue"] = faults
    ref_bound = NOGAP_WINDOW_S + m.REF_WINDOW_S
    for r in faults:
        rv = r["rev2"]
        if r["class"] == "uniform" and r["max_gap_s"] < m.ABS_GAP_S:
            check(rv["from_idle_s"] is not None and rv["from_idle_s"] <= NOGAP_WINDOW_S + r["cycle_s"] + 0.01
                  and rv["after_sending_s"] is not None
                  and rv["after_sending_s"] <= ref_bound + r["cycle_s"] + 0.01,
                  f"rev2 stops '{r['stream']}' at {r['wpm']} WPM: {rv['from_idle_s']} s from idle, "
                  f"{rv['after_sending_s']} s after correct sending (bound 30 s, 40 s plus one cycle)")
        if r["class"] in ("equal elements", "periodic") and r["max_gap_s"] < m.ABS_GAP_S:
            check(rv["from_idle_s"] is not None and rv["after_sending_s"] is not None
                  and rv["cause"] in ("count", "period", "window"),
                  f"rev2 stops '{r['stream']}' at {r['wpm']} WPM by {rv['cause']}: "
                  f"{rv['from_idle_s']} s from idle")
        if r["class"] == "text-like":
            check(rv["from_idle_s"] is None,
                  f"rev2 does not stop the text-like stream at {r['wpm']} WPM within {HORIZON_S:g} s "
                  f"(residual, note section 6.2; current rule: {r['current']['from_idle_s']} s)")
    uniform_rev1_missed = sorted({(r["stream"], r["wpm"]) for r in faults
                                  if r["class"] == "uniform" and r["rev1"]["from_idle_s"] is None})
    uniform_cur_missed = sorted({(r["stream"], r["wpm"]) for r in faults
                                 if r["class"] == "uniform" and r["current"]["from_idle_s"] is None})
    uniform_rev2_missed = sorted({(r["stream"], r["wpm"]) for r in faults
                                  if r["class"] == "uniform" and r["rev2"]["from_idle_s"] is None})
    results["nogap_fault_missed"] = {"current": len(uniform_cur_missed), "rev1": len(uniform_rev1_missed),
                                     "rev2": len(uniform_rev2_missed)}
    check(not uniform_rev2_missed, "rev2 misses no uniform fault stream of the catalogue")
    check(len(uniform_rev1_missed) > 0 and len(uniform_cur_missed) > 0,
          f"uniform streams missed: current {len(uniform_cur_missed)}, rev1 {len(uniform_rev1_missed)} "
          f"(the INSP-075 finding-1 streams)")
    slow = [r for r in faults if r["class"] in ("equal elements", "periodic") and r["max_gap_s"] < m.ABS_GAP_S]
    results["nogap_rev2_periodic_worst_s"] = max(r["rev2"]["from_idle_s"] for r in slow)

    # REQ-SYS-054 verification-note cases under rev2 (revised case wording in note section 7)
    note_cases = []
    for w in (5, 25, 50):
        for name, st in (("held dit lever", m.fault_stream_held(w, 200, "dit")),
                         ("held dah lever", m.fault_stream_held(w, 200, "dah")),
                         ("alternating, no qualifying gap", m.fault_stream_alternating(w, 200)),
                         ("alternating, 7.5-dit gap every 25 s", m.stream_with_gap_every(w, 200, 25, 7.5)),
                         ("random order, 7.5-dit gap every 25 s", m.stream_random_with_gap_every(w, 200, 25, 7.5))):
            _s, _c, t, cause = m.watchdog_relative(st)
            note_cases.append({"wpm": w, "stream": name, "trip_s": None if t is None else round(t, 2),
                               "cause": cause})
    results["req_sys_054_cases_rev2"] = note_cases
    for c in note_cases:
        if c["stream"] in ("held dit lever", "held dah lever", "alternating, no qualifying gap"):
            check(c["trip_s"] is not None and c["trip_s"] <= NOGAP_WINDOW_S + 0.5,
                  f"rev2 stops '{c['stream']}' at {c['wpm']} WPM by {c['trip_s']} s ({c['cause']})")
        if c["stream"] == "random order, 7.5-dit gap every 25 s":
            check(c["trip_s"] is None, f"rev2 keeps keying a non-repeating stream with a qualifying "
                                       f"gap every 25 s at {c['wpm']} WPM (window restart)")

    # ---- 6. Interlock (REQ-SYS-052, REQ-SW-KEYER-022) --------------------------------------
    il = []
    chatter_patterns = {
        "clean release at 1000 ms": [(0, 1000)],
        "F6 D2 make bounce then release": [(0, 1), (2, 1000)],
        "release with 6.2 ms chatter": [(0, 1000), (1001, 1003), (1004, 1007)],
        "release with 10 ms chatter": [(0, 1000), (1002, 1004), (1006, 1008), (1009, 1010)],
        "open 499 ms then reclose (intermittent short)": [(0, 1000), (1499, 5001)],
    }
    for name, iv in chatter_patterns.items():
        last_closed = max(b for a, b in iv) - 1
        t = m.interlock_arm_time([iv], INTERLOCK_MS, horizon_ms=5000)
        expect = None if "intermittent" in name else last_closed + INTERLOCK_MS
        il.append({"case": name, "arm_ms": t, "expected_ms": expect})
        check(t == expect, f"interlock {name}: arms at {t} ms (expected {expect})")
    ring = [(0, 100000)]
    t_paddle = m.interlock_arm_time([[], ring], INTERLOCK_MS, horizon_ms=10000)
    t_tip_only = m.interlock_arm_time([[]], INTERLOCK_MS, horizon_ms=10000)
    il.append({"case": "mono plug, paddle mode (ring used)", "arm_ms": t_paddle, "expected_ms": None})
    il.append({"case": "mono plug, Straight-on-tip (tip only)", "arm_ms": t_tip_only, "expected_ms": 499})
    check(t_paddle is None, "mono plug in a paddle mode never arms within 10 s")
    check(t_tip_only == 499, "Straight-on-tip with the tip open arms at 499 ms (500th open sample)")
    results["interlock"] = il
    longest_bounce_ms = 10.0  # F6: Curtis 5 to 10 ms, Ganssle maximum 6.2 ms
    results["interlock_margin_factor_over_bounce"] = INTERLOCK_MS / longest_bounce_ms
    check(INTERLOCK_MS / longest_bounce_ms >= 10, "interlock is at least 10 times the longest bounce")

    # ---- 7. Manual-closure timeout (REQ-SYS-053, REQ-SW-KEYER-026) ------------------------
    mt = []
    for hold_s in (4.9, 5.0, 5.1, 60.0):
        end, to = m.manual_timeout_end(hold_s * 1000.0, MANUAL_TIMEOUT_S * 1000.0)
        mt.append({"hold_s": hold_s, "key_down_end_ms": end, "timed_out": to})
    results["manual_timeout_cases"] = mt
    check(not mt[0]["timed_out"], "4.9 s closure does not time out")
    check(mt[2]["timed_out"] and mt[3]["timed_out"], "5.1 s and 60 s closures time out at 5 s")
    legit = []
    for w in (5, 10, 15, 25, 50):
        d = m.dit_us(w) / 1000.0
        # heaviest legitimate manual dah: 2 x nominal (6 dits) for a heavy straight-key or Bug fist,
        # and the F13 figure of 4.5 dits (ratio 4:1 with 75 percent weight)
        legit.append({"wpm": w, "dah_6dit_ms": 6 * d, "dah_f13_ms": 4.5 * d})
    results["manual_legit_closures"] = legit
    longest_legit_s = max(x["dah_6dit_ms"] for x in legit) / 1000.0
    results["manual_longest_legit_s"] = longest_legit_s
    check(longest_legit_s < MANUAL_RANGE_S[0],
          f"longest legitimate manual closure {longest_legit_s:.2f} s < 2 s range floor")
    check(MANUAL_RANGE_S[1] < HW_CUTOFF_MIN_S,
          f"range ceiling {MANUAL_RANGE_S[1]} s < hardware cutoff floor {HW_CUTOFF_MIN_S} s")
    results["manual_margins_s"] = {"default_over_legit": MANUAL_TIMEOUT_S - longest_legit_s,
                                   "floor_over_legit": MANUAL_RANGE_S[0] - longest_legit_s,
                                   "cutoff_over_ceiling": HW_CUTOFF_MIN_S - MANUAL_RANGE_S[1],
                                   "cutoff_over_default": HW_CUTOFF_MIN_S - MANUAL_TIMEOUT_S}

    # ---- 8. CPU watchdog period (REQ-SYS-131) ---------------------------------------------
    flash_erase_max_s = 0.400     # assumption A-7: Winbond W25Q-family 4 KB sector erase maximum
    flash_program_s = 2 * 0.003   # two 256-byte pages at 3 ms maximum each (assumption A-7)
    flash_verify_s = 0.001        # read-back of 512 bytes, bounded at 1 ms (assumption A-7)
    longest_unkicked_s = flash_erase_max_s + flash_program_s + flash_verify_s
    t_wd = 1.0                    # proposed watchdog load (note section 6.5)
    boot_to_selftest_s = 0.1      # assumption A-8: bootrom plus runtime start-up to Self-test entry
    worst_reset_s = t_wd + boot_to_selftest_s
    results["watchdog"] = {"longest_unkicked_s": longest_unkicked_s, "t_wd_s": t_wd,
                           "ratio": t_wd / longest_unkicked_s, "hang_to_selftest_s": worst_reset_s,
                           "margin_s": WATCHDOG_RESET_S - worst_reset_s}
    check(t_wd >= 2 * longest_unkicked_s,
          f"watchdog load {t_wd} s is at least twice the longest unkicked interval "
          f"{longest_unkicked_s:.3f} s")
    check(worst_reset_s <= WATCHDOG_RESET_S - 0.5,
          f"hang to Self-test {worst_reset_s:.2f} s within 2 s with at least 0.5 s margin")

    # ---- 9. Bench test-mode timeouts (REQ-SYS-188, REQ-SYS-189) ----------------------------
    paris = m.key_stream("PARIS", 5)
    paris_word_s = (paris[-1][1] + 7 * m.dit_us(5)) / 1e6
    longest_keyed_step_s = 60.0   # REQ-SYS-188 rationale: element timing at 5 WPM, about 60 s
    longest_tone_step_s = 30.0    # assumption A-9: one level reading within one tone start
    results["bench_mode"] = {"paris_word_5wpm_s": paris_word_s,
                             "paris_words_in_60s": 60.0 / paris_word_s,
                             "mode_s": BENCH_MODE_S, "longest_keyed_step_s": longest_keyed_step_s,
                             "margin_to_backstop_s": BACKSTOP_MIN_S - BENCH_MODE_S,
                             "tone_s": TONE_S, "longest_tone_step_s": longest_tone_step_s}
    check(abs(paris_word_s - 12.0) < 1e-6, f"PARIS word at 5 WPM lasts {paris_word_s} s (50 dits)")
    check(BENCH_MODE_S >= 2 * longest_keyed_step_s, "120 s covers twice the longest keyed step")
    check(BACKSTOP_MIN_S - BENCH_MODE_S >= 20, "120 s ends at least 20 s before the backstop floor")
    check(TONE_S >= 2 * longest_tone_step_s, "60 s covers twice the longest tone reading")

    # ---- 10. Plug presence (REQ-SW-KEYER-036) truth table (F19 circuit) --------------------
    rows = []
    for plug in (False, True):
        for tip_short in (False, True):
            for ring_short in (False, True):
                # F19: no plug -> KEY_DET tied to the ring node through the shunt; plug -> 100 k
                # pull-down reads low. A shorted input reads closed (low).
                ring_low = ring_short
                tip_low = tip_short
                det_high = (not plug) and (not ring_low)
                no_plug_read = det_high
                any_closed = tip_low or ring_low
                withheld = any_closed and no_plug_read
                rows.append({"plug": plug, "tip_short": tip_short, "ring_short": ring_short,
                             "KEY_DET_reads_no_plug": no_plug_read, "any_input_closed": any_closed,
                             "withheld_by_036": withheld})
    results["plug_presence"] = rows
    r_tip = [r for r in rows if not r["plug"] and r["tip_short"] and not r["ring_short"]][0]
    r_ring = [r for r in rows if not r["plug"] and r["ring_short"] and not r["tip_short"]][0]
    check(r_tip["withheld_by_036"], "tip short with no plug is withheld by REQ-SW-KEYER-036")
    check(not r_ring["withheld_by_036"],
          "ring short with no plug reads as plug present: REQ-SW-KEYER-036 cannot see it "
          "(coverage limit stated in the note)")

    out = HERE / "keyer-host-study-results.json"
    out.write_text(json.dumps(results, indent=1, sort_keys=True) + "\n")
    print(f"wrote {out.relative_to(HERE.parents[3])}")

    if plots:
        make_plots(results, worst)

    print(f"\n{len(FAILS)} failed assertion(s)")
    return 1 if FAILS else 0


def make_plots(results: dict, worst: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    w = list(SPEEDS_ALL)
    dit_s = [1.2 / x for x in w]

    # Plot 1: worst correct squeeze against the limit options
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=120)
    for label, style in (("A", "-"), ("U", "--"), ("B S=0.9", "-."), ("B S=0.5", ":")):
        ax.plot(w, [worst[label]["max_dits"] * d for d in dit_s], style, lw=1.8,
                label=f"worst correct squeeze, {label} ({worst[label]['max_dits']:g} dits)")
    ax.plot(w, [12.0 * d for d in dit_s], color="0.5", lw=1.2,
            label="squeezed C, Iambic A (12 dits)")
    ax.plot(w, [2.0] * len(w), color="red", lw=2.0, label="REQ-SYS-184 as baselined: 2 s")
    ax.plot(w, [max(2.0, 16 * d) for d in dit_s], color="orange", lw=2.0,
            label="tbr CR branch: longer of 2 s and 16 dits")
    ax.plot(w, [max(2.0, 20 * d) for d in dit_s], color="green", lw=2.4,
            label="proposed: longer of 2 s and 20 dits")
    ax.set_xlabel("Keyer speed (WPM)")
    ax.set_ylabel("Both paddle contacts closed (s)")
    ax.set_title("REQ-SYS-184: longest correct squeeze vs squeeze limit options (5 to 50 WPM)")
    ax.set_xlim(5, 50)
    ax.set_ylim(0, 5.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7.5, loc="upper right")
    fig.tight_layout()
    fig.savefig(HERE / "keyer-squeeze-vs-speed.png")
    plt.close(fig)

    # Plot 2: longest time without a qualifying gap, current and proposed rules
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=120)
    ng = results["nogap_corpus"]
    for rule, prof, style, col, lab in (
            ("current", "nominal 3/7", "-", "tab:blue", "current (7 dits or 500 ms)"),
            ("current", "short word 3/6", "--", "tab:blue", "current (7 dits or 500 ms)"),
            ("current", "fast 2.5/5", ":", "tab:blue", "current (7 dits or 500 ms)"),
            ("rev1", "fast 2.5/5", "-.", "tab:orange", "revision 1 (2 dits at the selected speed; under the green curves)"),
            ("rev2", "nominal 3/7", "-", "tab:green", "revision 2 (2 x reference interval)"),
            ("rev2", "fast 2.5/5", ":", "tab:green", "revision 2 (2 x reference interval)")):
        rows = ng[rule][prof]
        ax.plot([r["wpm"] for r in rows],
                [max(r["qso_max_span_s"], r["stress_max_span_s"]) for r in rows], style,
                color=col, lw=1.8, label=f"{lab}, spacing {prof}")
    ax.axhline(NOGAP_WINDOW_S, color="red", lw=2.0, label="REQ-SYS-054 window 30 s")
    ax.text(15.5, 32.5, "Current-rule curves that leave the top of the plot have no\n"
            "qualifying gap at all: a 6-dit word space is under the threshold\n"
            "above 14.4 WPM, a 5-dit one above 12 WPM, so the span grows\n"
            "with the whole corpus (hundreds of seconds)", fontsize=7.5)
    ax.set_xlabel("Keyer speed (WPM)")
    ax.set_ylabel("Longest time without a qualifying gap (s)")
    ax.text(5.5, 12.0, f"Revision 2 over all three corpora (paddle, Bug {results['nogap_bug']['streams']} streams,\n"
            f"Straight {results['nogap_straight']['streams']} streams): longest span "
            f"{results['nogap_rev2_max_span_s']:.2f} s, no trip", fontsize=7.5, color="tab:green")
    ax.set_title("REQ-SYS-054: paddle corpus, longest time without a qualifying gap vs the 30 s window",
                 fontsize=10)
    ax.set_xlim(5, 50)
    ax.set_ylim(0, 60)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7.5, loc="upper right")
    fig.tight_layout()
    fig.savefig(HERE / "keyer-nogap-vs-speed.png")
    plt.close(fig)

    # Plot 4: fault side (INSP-075 finding-1): stop time of keyer-fault streams with stretched spaces
    fc = results["nogap_fault_catalogue"]
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6), dpi=120, sharey=True)
    for ax, w in zip(axes, (15, 50)):
        for rule, col, mk, lab in (("current", "tab:blue", "o", "current (7 dits or 500 ms)"),
                                   ("rev1", "tab:orange", "s", "revision 1 (2 dits)"),
                                   ("rev2", "tab:green", "^", "revision 2 (self-referenced)")):
            for stream_kind, ls in (("alternating", "-"), ("held dit", "--")):
                rows = [r for r in fc if r["wpm"] == w and r["stream"].startswith(stream_kind + ", space")]
                xs = [float(r["stream"].split("space ")[1].split(" ")[0]) for r in rows]
                ys = [r[rule]["after_sending_s"] for r in rows]
                yp = [y if y is not None else 62.0 for y in ys]
                ax.plot(xs, yp, ls, color=col, marker=mk, ms=4, lw=1.3,
                        label=f"{lab}, {stream_kind}" if w == 15 else None)
        ax.axhline(NOGAP_WINDOW_S, color="0.4", lw=1.0, ls=":")
        ax.axhline(NOGAP_WINDOW_S + m.REF_WINDOW_S, color="0.4", lw=1.0, ls=":")
        ax.text(1.05, NOGAP_WINDOW_S + 0.6, "30 s window", fontsize=7)
        ax.text(1.05, NOGAP_WINDOW_S + m.REF_WINDOW_S + 0.6, "30 s + 10 s reference aging", fontsize=7)
        ax.text(1.05, 63.2, "plotted at 62 s: not stopped by K4 (K12 backstop at 150 to 180 s)", fontsize=7)
        ax.set_title(f"{w} WPM, fault starting after 15 s of correct sending", fontsize=9)
        ax.set_xlabel("Space after every element (dit times)")
        ax.set_xlim(0.8, 8.2)
        ax.set_ylim(0, 68)
        ax.grid(True, alpha=0.3)
    axes[0].set_ylabel("Time from fault start to K4 stop (s)")
    axes[0].legend(fontsize=6.5, loc="lower right")
    fig.suptitle("REQ-SYS-054 fault side: keyer-fault streams with stretched spaces under the three rules",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(HERE / "keyer-nogap-fault-coverage.png")
    plt.close(fig)

    # Plot 3: timeline of a squeezed period in Iambic A at 5 WPM with the latest correct release
    wpm = 5
    d = m.dit_us(wpm) / 1000.0
    t1 = int(1 + 18 * d) - 4
    r = m.simulate("A", wpm, [(0, t1)], [(0, t1)], int(24 * d), switchpoint=0.5)
    fig, ax = plt.subplots(figsize=(9.0, 3.6), dpi=120)

    def step(ev, y0, label, col):
        xs, ys, s = [0.0], [y0], False
        for k, st in ev:
            xs += [k / 1000.0, k / 1000.0]
            ys += [y0 + (0.6 if s else 0), y0 + (0.6 if st else 0)]
            s = st
        xs.append(24 * d / 1000.0)
        ys.append(y0 + (0.6 if s else 0))
        ax.plot(xs, ys, color=col, lw=1.6)
        ax.text(-0.05, y0 + 0.2, label, ha="right", fontsize=8)

    step(r.deb_dit, 2.0, "dit contact", "tab:blue")
    step(r.deb_dah, 1.0, "dah contact", "tab:orange")
    for s0, e0, typ in r.elements:
        ax.add_patch(plt.Rectangle((s0 / 1e6, 0.0), (e0 - s0) / 1e6, 0.6, color="k"))
    ax.text(-0.05, 0.2, "TX_KEY", ha="right", fontsize=8)
    for sec, col, lab in ((2.0, "red", "2 s (baselined)"), (16 * d / 1000.0, "orange", "16 dits"),
                          (20 * d / 1000.0, "green", "20 dits (proposed)")):
        ax.axvline(sec, color=col, lw=1.4, ls="--")
        ax.text(sec + 0.03, 2.75, lab, color=col, fontsize=7.5)
    ax.set_xlim(-0.1, 24 * d / 1000.0)
    ax.set_ylim(-0.2, 3.0)
    ax.set_yticks([])
    ax.set_xlabel("Time from first contact closure (s)")
    ax.set_title("Squeezed period (.-.-.-) in Iambic A at 5 WPM, released at the latest correct instant "
                 f"(both closed {m.both_closed_max_ms(r) / 1000.0:.2f} s)", fontsize=9)
    fig.tight_layout()
    fig.savefig(HERE / "keyer-squeeze-timeline.png")
    plt.close(fig)


if __name__ == "__main__":
    sys.exit(main(plots="--no-plots" not in sys.argv))
