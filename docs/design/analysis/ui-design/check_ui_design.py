"""Checker for the WP-PDR-33 UI design analysis (docs/design/analysis/ui-design.md).

Run from the repository root:
    .venv/bin/python docs/design/analysis/ui-design/check_ui_design.py

Recomputes every number the note states, asserts each acceptance value, writes
ui-design-results.json and ui-tuning-step-law.png beside this file and the display layout
renders docs/reviews/PDR/figures/display-layout-*.png, and exits 1 on any failed assertion.
Pass --no-plots to skip the plot and the renders.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIG = ROOT / "docs" / "reviews" / "PDR" / "figures"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "keyer-host-study"))

import ui_model as u  # noqa: E402
import keyer_model as km  # noqa: E402

FAILS: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


# Acceptance constants traced to their governing text (note section 4)
CHAR_HEIGHT_MM = 4.0          # REQ-SYS-061 "at least 4.0 mm (TBR)"
VIEW_MM = 500.0               # REQ-SYS-165 "legible at 0.5 m"
LUX_FLOOR = 300.0             # REQ-SYS-165 "300 lux (TBR)"
MENU_LEVELS = 2               # REQ-SYS-062 "within two menu levels (TBR)"
STEP_MIN_HZ, STEP_MAX_HZ = 10, 10_000   # REQ-SYS-058 "from 10 Hz to 10 kHz (TBR)"
CROSS_S, CROSS_REV_S = 30.0, 2.0        # REQ-SYS-164 "within 30 s (TBR) at ... 2 revolutions per second"
FAULT_S = 1.0                 # REQ-SYS-067 "within 1 s (TBR)"
ID_NOMINAL_S, ID_TOL_S = 540.0, 5.0     # REQ-SYS-068 "9 min 00 s +/-5 s (TBR)"
LOAD_FPS, LOAD_DPS = 50.0, 50.0         # REQ-SW-KEYER-014 "50 display frames/s and 50 detents/s per encoder (TBR)"
# Assumed legibility criteria (note section 4.3, A-U1 to A-U3; the source standards are not in the corpus)
SUBTENSE_MIN_ARCMIN = 20.0
L_BACKGROUND_MIN = 3.0        # cd/m2
CR_MIN = 3.0


def main(plots: bool = True) -> int:
    res: dict = {}

    # ---- Character height and legibility (REQ-SYS-061, REQ-SYS-165) ------------------------
    c = u.screen_receive()
    f = u.fmt_freq(146_520_000)
    res["freq_string"] = f
    res["freq_width_dots"] = u.Canvas.freq_width(f)
    res["digit_height_dots"] = u.DIG_H
    h_mm = u.DIG_H * u.PITCH_MM
    res["digit_height_mm"] = round(h_mm, 3)
    res["digit_subtense_arcmin_0p5m"] = round(u.subtense_arcmin(h_mm, VIEW_MM), 2)
    res["req_subtense_arcmin_0p5m"] = round(u.subtense_arcmin(CHAR_HEIGHT_MM, VIEW_MM), 2)
    check(h_mm >= CHAR_HEIGHT_MM, f"frequency digit height {h_mm:.2f} mm >= 4.0 mm (23 dots x 0.18 mm)")
    check(res["freq_width_dots"] <= u.W - 4, f"frequency string {f} is {res['freq_width_dots']} dots wide, "
                                              f"fits 124 dots")
    check(res["req_subtense_arcmin_0p5m"] >= SUBTENSE_MIN_ARCMIN,
          f"4.0 mm at 0.5 m subtends {res['req_subtense_arcmin_0p5m']} arcmin >= 20 arcmin (A-U1)")
    # measured from the frame buffer: rows occupied by the frequency digits
    rows = [y for y in range(20, 20 + u.DIG_H + 2) if any(c.px[y][x] for x in range(u.W))]
    res["freq_rows_measured"] = [min(rows), max(rows)]
    check(max(rows) - min(rows) + 1 == u.DIG_H, "rendered digits occupy exactly 23 dot rows")

    leg = {}
    for name, kw in (("no lens", {"with_lens": False}),
                     ("plain lens, white surround in the specular direction", {}),
                     ("plain lens, room surround reflectance 0.3", {"surround_rho": 0.3}),
                     ("AR-coated lens, 0.5 percent per surface", {"R_override": 0.005})):
        r = u.legibility(LUX_FLOOR, **kw)
        leg[name] = {k: round(v, 4) for k, v in r.items()}
    res["legibility_300lux"] = leg
    for name, r in leg.items():
        check(r["Lb"] >= L_BACKGROUND_MIN, f"{name}: background {r['Lb']:.2f} cd/m2 >= 3 cd/m2 at 300 lux")
    check(leg["no lens"]["CR"] >= CR_MIN and leg["AR-coated lens, 0.5 percent per surface"]["CR"] >= CR_MIN
          and leg["plain lens, room surround reflectance 0.3"]["CR"] >= CR_MIN,
          "contrast ratio >= 3:1 without a lens, with an AR lens, and with a plain lens in a room surround")
    check(leg["plain lens, white surround in the specular direction"]["CR"] < CR_MIN,
          f"plain lens with a white surround in the specular direction falls to "
          f"{leg['plain lens, white surround in the specular direction']['CR']:.2f}:1 (limitation L-U2)")
    T = leg["plain lens, white surround in the specular direction"]["T_display_path"]
    e_min = u.illuminance_for_background(L_BACKGROUND_MIN, T=T)
    res["lux_for_3cd_with_lens"] = round(e_min, 1)
    res["lux_floor_margin_factor"] = round(LUX_FLOOR / e_min, 2)
    check(LUX_FLOOR / e_min >= 3.0, f"300 lux is {LUX_FLOOR / e_min:.2f} times the {e_min:.1f} lux luminance floor")

    # ---- Menu depth (REQ-SYS-062) ----------------------------------------------------------
    depths = u.menu_depths()
    res["menu"] = {k: {"depth": v[0], "kind": v[1], "source": v[2]} for k, v in depths.items()}
    res["menu_item_count"] = len(depths)
    check(all(v[0] <= MENU_LEVELS for v in depths.values()),
          f"every one of {len(depths)} operator settings, actions and views is within 2 levels")
    needed = ["REQ-SYS-040", "REQ-SYS-041", "REQ-SYS-044", "REQ-SYS-045", "REQ-SYS-048",
              "REQ-SYS-162", "REQ-SW-KEYER-009", "REQ-SYS-063", "REQ-SYS-014", "REQ-SYS-006",
              "REQ-SYS-074", "REQ-SYS-170", "REQ-SYS-171", "REQ-SYS-179", "REQ-SYS-136",
              "REQ-SYS-058", "REQ-SYS-059", "REQ-SYS-066", "PRACTICE", "paddle swap", "T12"]
    srcs = " ".join(v[2] for v in depths.values())
    missing = [n for n in needed if n not in srcs]
    check(not missing, f"every operator setting source named in the note is placed (missing: {missing})")
    per_screen = max(len(v) for v in u.MENU_TREE.values())
    res["max_items_per_category"] = per_screen

    # ---- Tuning law and band crossing (REQ-SYS-058, REQ-SYS-164) --------------------------
    steps = [s for _, s in u.STEP_TABLE]
    check(min(steps) == STEP_MIN_HZ and max(steps) == STEP_MAX_HZ,
          f"step table runs from {min(steps)} Hz to {max(steps)} Hz")
    cross = {}
    for rev in (0.5, 0.75, 0.83, 0.84, 1.0, 1.5, 2.0, 3.0):
        t, n = u.crossing_time(rev)
        cross[str(rev)] = {"time_s": round(t, 3), "detents": n}
    res["crossing"] = cross
    t2 = cross["2.0"]["time_s"]
    check(t2 <= CROSS_S, f"144.000 to 148.000 MHz at 2 rev/s in {t2} s <= 30 s (margin {CROSS_S - t2:.1f} s)")
    ur = u.usability_run(146_520_000, 144_057_300)
    res["usability_run"] = ur
    check(ur["error_hz"] == 0, f"scripted operator lands exactly on 144.057.30 MHz in {ur['total_s']} s, "
                               f"{ur['detents']} detents")
    ur2 = u.usability_run(144_000_000, 147_999_990)
    res["usability_run_full_band"] = ur2
    check(ur2["error_hz"] == 0, f"scripted operator crosses the band and lands on 147.999.99 MHz in "
                                f"{ur2['total_s']} s")
    # decode capacity of the 1 kHz sampler (equal quadrature spacing, A-U8)
    state_ms_at_load = 1000.0 / (4 * LOAD_DPS)
    res["encoder_state_ms_at_50dps"] = state_ms_at_load
    check(state_ms_at_load >= 2.0, f"at 50 detents/s each quadrature state lasts {state_ms_at_load} ms "
                                   f">= 2 samples")

    # ---- Status set and message table (REQ-SYS-060, REQ-SYS-067) ---------------------------
    need060 = {"frequency", "power step", "key mode", "keyer speed", "battery state", "transmit state"}
    check(all(u.SCREEN_FIELDS[k] >= need060 for k in ("receive", "transmit", "tune")),
          "receive, transmit and tune screens carry the six REQ-SYS-060 fields")
    lines = [m[2] for m in u.MESSAGE_TABLE]
    res["message_table"] = [{"row": r, "conops": t, "display": list(d)} for r, t, d in u.MESSAGE_TABLE]
    check(len(set(lines)) == len(lines), f"all {len(lines)} fault and inhibit messages are distinct")
    check(all(len(x) <= 10 for d in lines for x in d),
          "every message line fits 10 characters at the 2x font (118 dots)")
    check(sorted({r for r, _, _ in u.MESSAGE_TABLE}) == list(range(1, 20)),
          "every cause row 1 to 19 of ConOps Table 3.4-4 with a display text has a message")

    # ---- Fault message latency (REQ-SYS-067) ----------------------------------------------
    items, total = u.fault_latency_budget()
    res["fault_latency_items_ms"] = items
    res["fault_latency_total_ms"] = total
    check(total <= FAULT_S * 1000.0, f"fault message worst latency {total:.1f} ms <= 1000 ms "
                                     f"(margin {FAULT_S * 1000 - total:.1f} ms)")

    # ---- Identification reminder (REQ-SYS-068) ---------------------------------------------
    early, late = u.id_reminder_error_s()
    res["id_reminder_error_s"] = {"early": round(early, 4), "late": round(late, 4)}
    check(early <= ID_TOL_S and late <= ID_TOL_S, f"reminder error -{early:.3f} s / +{late:.3f} s within 5 s")
    lead_min = 600.0 - (ID_NOMINAL_S + ID_TOL_S)
    stream = km.key_stream("DE N0CALL N0CALL", 5)
    id_s = stream[-1][1] / 1e6
    res["id_lead_min_s"] = lead_min
    res["id_send_time_5wpm_s"] = round(id_s, 2)
    check(id_s < lead_min, f"'DE N0CALL N0CALL' at 5 WPM takes {id_s:.1f} s < {lead_min:.0f} s minimum lead")

    # ---- Defaults (REQ-SYS-136) -------------------------------------------------------------
    defaults = {"mode": "Iambic A", "wpm": 15, "sidetone_hz": 600, "hang_dits": 8, "envelope_ms": 5}
    ranges = {"wpm": (5, 50, 1, "REQ-SYS-041"), "sidetone_hz": (300, 1000, 10, "REQ-SYS-045"),
              "hang_dits": (3, 30, 1, "REQ-SYS-044"), "envelope_ms": (3, 8, None, "REQ-SYS-014")}
    res["defaults"] = defaults
    for k, (lo, hi, step, src) in ranges.items():
        v = defaults[k]
        ok = lo <= v <= hi and (step is None or (v - lo) % step == 0)
        check(ok, f"default {k} = {v} lies on the {src} range {lo} to {hi}")
    check(defaults["mode"] in ("Straight", "Iambic A", "Iambic B", "Ultimatic", "Bug"),
          "default mode Iambic A is one of the REQ-SYS-040 modes")
    hang_ms = defaults["hang_dits"] * 1200 / defaults["wpm"]
    res["default_hang_ms"] = hang_ms
    check(hang_ms > 7 * 1200 / defaults["wpm"],
          f"default hang {hang_ms:.0f} ms exceeds a 7-dit word space at 15 WPM (stays in transmit "
          f"between words)")

    # ---- Keyer timing load values (REQ-SW-KEYER-014) ---------------------------------------
    max_fps = 1000.0 / u.FULL_FRAME_MS
    res["display_max_fps_at_1p1MHz"] = round(max_fps, 2)
    res["load_bus_duty"] = round(LOAD_FPS * u.FULL_FRAME_MS / 1000.0, 3)
    check(LOAD_FPS >= 2 * u.UI_MAX_FPS and LOAD_FPS <= max_fps,
          f"50 frames/s load is at least twice the 25 frames/s design limit and within the "
          f"{max_fps:.1f} frames/s bus maximum")
    check(LOAD_DPS >= CROSS_REV_S * 24, "50 detents/s covers 2 rev/s of a 24-detent encoder (48/s)")

    out = HERE / "ui-design-results.json"
    out.write_text(json.dumps(res, indent=1, sort_keys=True) + "\n")
    print(f"wrote {out.relative_to(ROOT)}")

    if plots:
        FIG.mkdir(parents=True, exist_ok=True)
        for name, fn in u.SCREENS.items():
            path = FIG / f"display-layout-{name}.png"
            u.render_png(fn(), path, scale=4,
                         caption=f"display-layout-{name}: LS013B7DH03 128 x 128 dots, 0.18 mm pitch, "
                                 f"shown at 4x (WP-PDR-33)")
            print(f"wrote {path.relative_to(ROOT)}")
        make_plot(res)

    print(f"\n{len(FAILS)} failed assertion(s)")
    return 1 if FAILS else 0


def make_plot(res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.0, 4.2), dpi=120)
    rates = [x / 10.0 for x in range(1, 601)]
    a1.step(rates, [u.step_for_rate(r) for r in rates], where="post", lw=2)
    a1.set_yscale("log")
    a1.set_xlabel("Detent rate (detents/s); 24 detents per revolution")
    a1.set_ylabel("Frequency step per detent (Hz)")
    a1.set_title("REQ-SYS-058 step table (proposed)")
    a1.axvline(48, color="red", ls="--", lw=1.2)
    a1.text(49, 20, "2 rev/s", color="red", fontsize=8)
    a1.grid(True, which="both", alpha=0.3)
    revs = [x / 100.0 for x in range(40, 301, 2)]
    times = [u.crossing_time(r)[0] for r in revs]
    a2.plot(revs, times, lw=2, label="144.000 to 148.000 MHz")
    a2.axhline(CROSS_S, color="red", lw=1.6, label="REQ-SYS-164: 30 s")
    a2.axvline(CROSS_REV_S, color="0.4", ls="--", lw=1.0)
    a2.plot([2.0], [res["crossing"]["2.0"]["time_s"]], "o", color="green",
            label=f"2 rev/s: {res['crossing']['2.0']['time_s']:.1f} s")
    a2.set_yscale("log")
    a2.set_xlabel("Steady rotation (rev/s)")
    a2.set_ylabel("Band crossing time (s)")
    a2.set_title("REQ-SYS-164 band crossing time")
    a2.grid(True, which="both", alpha=0.3)
    a2.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(HERE / "ui-tuning-step-law.png")
    plt.close(fig)
    print("wrote docs/design/analysis/ui-design/ui-tuning-step-law.png")


if __name__ == "__main__":
    sys.exit(main(plots="--no-plots" not in sys.argv))
