"""Checker for the WP-PDR-33 keyer host study (docs/design/analysis/keyer-host-study.md).

Run from the repository root:
    .venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py

It recomputes every number the note states, asserts each acceptance value, writes
keyer-host-study-results.json and the three plots beside this file, and exits 1 on any failed
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
        span, cnt, t_trip, cause = m.paddle_watchdog(stream, w, m.gap_rule_proposed)
        fault.append({"wpm": w, "squeeze_trip_s": round(lim_s, 3),
                      "baseline_trip_s": SQUEEZE_LIMIT_BASELINE_S,
                      "nogap_trip_s": t_trip, "nogap_cause": cause})
        check(lim_s < NOGAP_WINDOW_S and lim_s < HW_CUTOFF_MIN_S,
              f"squeeze fault at {w} WPM stops at {lim_s:.2f} s, before the 30 s window")
    results["squeeze_fault_stop"] = fault

    # ---- 5. Paddle watchdog on correct sending and on fault streams -----------------------
    profiles = {"nominal 3/7": (3.0, 7.0), "short word 3/6": (3.0, 6.0),
                "short word 3/5": (3.0, 5.0), "fast 2.5/5": (2.5, 5.0),
                "spread 4.5/10": (4.5, 10.0)}
    nogap = {}
    for rule_name, rule in (("current", m.gap_rule_current), ("proposed", m.gap_rule_proposed)):
        nogap[rule_name] = {}
        for pname, (ls, ws) in profiles.items():
            rows = []
            for w in SPEEDS_ALL:
                qso = m.key_stream(m.CORPUS_QSO, w, ls, ws)
                stress = m.key_stream(m.CORPUS_STRESS, w, ls, ws)
                s1, c1, t1, _ = m.paddle_watchdog(qso, w, rule)
                s2, c2, t2, _ = m.paddle_watchdog(stress, w, rule)
                rows.append({"wpm": w, "qso_max_span_s": round(s1, 3), "qso_max_count": c1,
                             "qso_trip": t1 is not None, "stress_max_span_s": round(s2, 3),
                             "stress_max_count": c2, "stress_trip": t2 is not None})
            nogap[rule_name][pname] = rows
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
    prop_any = [(p, r["wpm"]) for p, rows in nogap["proposed"].items() for r in rows
                if r["qso_trip"] or r["stress_trip"]]
    check(not prop_any, "proposed 2-dit gap rule trips no corpus sending, every profile, 5 to 50 WPM")
    prop_max_span = max(max(r["qso_max_span_s"], r["stress_max_span_s"])
                        for rows in nogap["proposed"].values() for r in rows)
    prop_max_count = max(max(r["qso_max_count"], r["stress_max_count"])
                         for rows in nogap["proposed"].values() for r in rows)
    cur_max_count = max(max(r["qso_max_count"], r["stress_max_count"])
                        for rows in nogap["current"].values() for r in rows)
    results["nogap_proposed_max_span_s"] = prop_max_span
    results["nogap_proposed_max_count"] = prop_max_count
    results["nogap_current_max_count"] = cur_max_count
    check(prop_max_span < NOGAP_WINDOW_S / 5, f"proposed rule: longest span {prop_max_span} s < 6 s")
    check(cur_max_count < NOGAP_COUNT / 2 and prop_max_count < NOGAP_COUNT / 2,
          f"identical-element count in the corpus {cur_max_count} (current), {prop_max_count} "
          f"(proposed) is below 64, half of 128")

    faults = []
    for w in (5, 15, 25, 50):
        for rule_name, rule in (("current", m.gap_rule_current), ("proposed", m.gap_rule_proposed)):
            for fname, stream in (
                ("held dit", m.fault_stream_held(w, 200, "dit")),
                ("held dah", m.fault_stream_held(w, 200, "dah")),
                ("alternating", m.fault_stream_alternating(w, 200)),
                ("alternating, 2.5-dit gap every 25 s", m.stream_with_gap_every(w, 200, 25, 2.5)),
                ("alternating, 7.5-dit gap every 25 s", m.stream_with_gap_every(w, 200, 25, 7.5)),
            ):
                span, cnt, t_trip, cause = m.paddle_watchdog(stream, w, rule)
                faults.append({"wpm": w, "rule": rule_name, "stream": fname,
                               "trip_s": None if t_trip is None else round(t_trip, 3),
                               "cause": cause})
    results["nogap_fault_streams"] = faults
    for f in faults:
        if f["stream"] in ("held dit", "held dah", "alternating"):
            check(f["trip_s"] is not None and f["trip_s"] <= NOGAP_WINDOW_S + 0.5,
                  f"{f['rule']} rule stops '{f['stream']}' at {f['wpm']} WPM by {f['trip_s']} s")
        if f["stream"] == "alternating, 7.5-dit gap every 25 s":
            check(f["trip_s"] is None, f"{f['rule']} rule keeps keying a stream with a 7.5-dit gap "
                                       f"every 25 s at {f['wpm']} WPM (REQ-SYS-054 note case)")
        if f["stream"] == "alternating, 2.5-dit gap every 25 s" and f["rule"] == "proposed":
            check(f["trip_s"] is None, f"proposed rule keeps keying a stream with a 2.5-dit gap "
                                       f"every 25 s at {f['wpm']} WPM")

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
    for rule, prof, style, col in (("current", "nominal 3/7", "-", "tab:blue"),
                                   ("current", "short word 3/6", "--", "tab:blue"),
                                   ("current", "fast 2.5/5", ":", "tab:blue"),
                                   ("proposed", "nominal 3/7", "-", "tab:green"),
                                   ("proposed", "fast 2.5/5", ":", "tab:green")):
        rows = ng[rule][prof]
        ax.plot([r["wpm"] for r in rows],
                [max(r["qso_max_span_s"], r["stress_max_span_s"]) for r in rows], style,
                color=col, lw=1.8, label=f"{rule} gap rule, spacing {prof} (letter/word dits)")
    ax.axhline(NOGAP_WINDOW_S, color="red", lw=2.0, label="REQ-SYS-054 window 30 s")
    ax.text(15.5, 32.5, "Current-rule curves that leave the top of the plot have no\n"
            "qualifying gap at all: a 6-dit word space is under the threshold\n"
            "above 14.4 WPM, a 5-dit one above 12 WPM, so the span grows\n"
            "with the whole corpus (hundreds of seconds)", fontsize=7.5)
    ax.set_xlabel("Keyer speed (WPM)")
    ax.set_ylabel("Longest time without a qualifying gap (s)")
    ax.set_title("REQ-SYS-054: correct sending (QSO and stress corpus) vs the 30 s no-gap window")
    ax.set_xlim(5, 50)
    ax.set_ylim(0, 60)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7.5, loc="upper right")
    fig.tight_layout()
    fig.savefig(HERE / "keyer-nogap-vs-speed.png")
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
