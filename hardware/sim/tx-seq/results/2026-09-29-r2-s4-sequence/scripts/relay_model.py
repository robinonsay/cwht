"""Reduced-order electromechanical model of the Omron G5V-2 T/R relay (WP-PDR-23a).

Analysis record: docs/design/analysis/sequencer-timing.md (section 3.3). This is an analysis model, not
design data: every parameter the datasheet does not give is an engineering estimate (class E) and is
swept over a band; the model is anchored to the datasheet values that exist (class D):
  - must-operate voltage at most 75 % of rated at a coil temperature of 23 C (both coils);
  - operate time at most 7 ms and release time at most 3 ms (rated voltage, 23 C);
  - coil resistance +/-10 % at 23 C (5 VDC standard 50 ohm, 5 VDC high-sensitivity 166.7 ohm).

Model (one magnetic circuit, lumped):
  flux linkage  lam = L(g) i,   L(g) = Lc / (1 + (rho - 1) g / D)     (g = armature gap, D = full gap)
  circuit       d lam / dt = v_drive(i) - R(T) i                        (diode freewheel at turn-off)
  force         Fm = 1/2 i^2 |dL/dg|                                    (co-energy, no saturation)
  spring        Fs(g) = F0 (1 + sigma (D - g) / D)                      (preload plus a rising load line)
  motion        m d2g/dt2 = Fs - Fm, with stops at g = 0 (contact made) and g = D (at rest)
Anchors: F0 is set so that the armature starts to move at the must-operate current Ipu = 0.75 Vr / R23;
m is solved so that the operate time at rated voltage and 23 C equals the datasheet 7 ms (a relay at both
datasheet limits at once: the worst-case unit). The release time with no diode (current removed at once)
must then be at most the datasheet 3 ms; a parameter set that fails this second anchor is rejected.
Temperature (revision 1, sequencer-timing.md revision 1, finding-2 of its review). The coil resistance rises
by the copper coefficient ALPHA_CU. In revision 0 the must-operate current was held constant, so the
must-operate voltage rose at ALPHA_CU (0.393 %/K). The datasheet graph "Ambient Temperature vs. Must Operate or
Must Release Voltage" (G5V-2-H1, 10 samples) shows a steeper rise, 0.48 to 0.51 %/K (class DD, graph read;
seq_run.py takes 0.48 %/K from 23 C and 0.51 %/K from 20 C, i.e. up to 0.5347 %/K from 23 C). The model takes a must-operate voltage slope s_mo per relay: the must-operate voltage at a
coil temperature T is V_mo23 (1 + s_mo (T - 23)), so the must-operate current is Ipu (1 + s_mo (T - 23)) / k(T),
with k(T) the copper ratio. The spring force (preload and load line) is scaled by the square of that current
ratio, so the pick-up and the release currents scale together (the graph's must-release line rises with it).
s_mo = None keeps the revision 0 law (s_mo = ALPHA_CU, constant must-operate current).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ALPHA_CU = 0.00393       # 1/K, annealed copper resistance coefficient at 20 C (class R, handbook value)
GAP = 0.4e-3             # m; the value is arbitrary: the dynamics depend on m * GAP^2, and m is solved
T_REF = 23.0             # C, the datasheet's coil temperature for the operating characteristics
T_OP_DS = 7.0e-3         # s, datasheet operate time maximum
T_REL_DS = 3.0e-3        # s, datasheet release time maximum
VPU_FRAC = 0.75          # datasheet must-operate voltage, maximum, fraction of rated

COILS = {
    # name: rated voltage, R at 23 C nominal, tolerance (datasheet ratings table)
    "std": {"v_rated": 5.0, "r23": 50.0, "tol": 0.10, "label": "G5V-2 DC5 (standard, 100 mA, 50 ohm)"},
    "h1": {"v_rated": 5.0, "r23": 166.7, "tol": 0.10, "label": "G5V-2-H1 DC5 (high-sensitivity, 30 mA, 166.7 ohm)"},
}


def k_temp(t_coil_c: float) -> float:
    """Coil resistance ratio R(T) / R(23 C)."""
    return 1.0 + ALPHA_CU * (t_coil_c - T_REF)


@dataclass
class Params:
    tau_o: float     # s, open-gap time constant L_open / R23
    rho: float       # L_closed / L_open
    sigma: float     # spring load-line rise from open to closed, fraction of F0

    def key(self) -> str:
        return f"tau{self.tau_o * 1e3:.1f}_rho{self.rho:g}_sig{self.sigma:g}"


def k_mo(t_coil_c: float, s_mo: float | None) -> float:
    """Must-operate voltage ratio V_mo(T) / V_mo(23 C); s_mo None = copper (revision 0 law)."""
    return k_temp(t_coil_c) if s_mo is None else 1.0 + s_mo * (t_coil_c - T_REF)


def force_scale(t_coil_c: float, s_mo: float | None) -> float:
    """Spring-force scale at coil temperature T: (I_mo(T) / I_mo(23 C))**2 (1 for the revision 0 law)."""
    return (k_mo(t_coil_c, s_mo) / k_temp(t_coil_c)) ** 2


class Relay:
    def __init__(self, coil: str, r23: float, p: Params, m: float = 1e-3, s_mo: float | None = None):
        c = COILS[coil]
        self.coil, self.r23, self.p = coil, r23, p
        self.s_mo = s_mo
        self.v_rated = c["v_rated"]
        self.lo = p.tau_o * r23
        self.lc = p.rho * self.lo
        self.ipu = VPU_FRAC * self.v_rated / r23
        self.f0 = 0.5 * self.ipu ** 2 * self.dldg(GAP)
        self.m = m

    # magnetic circuit
    def ind(self, g: float) -> float:
        return self.lc / (1.0 + (self.p.rho - 1.0) * g / GAP)

    def dldg(self, g: float) -> float:
        return self.lc * (self.p.rho - 1.0) / GAP / (1.0 + (self.p.rho - 1.0) * g / GAP) ** 2

    def fspring(self, g: float) -> float:
        return self.f0 * (1.0 + self.p.sigma * (GAP - g) / GAP)

    def i_release(self, t_coil_c: float = T_REF) -> float:
        """Current below which the closed armature is released (magnetic force = spring force at g = 0)."""
        return math.sqrt(2.0 * self.fspring(0.0) * force_scale(t_coil_c, self.s_mo) / self.dldg(0.0))

    def i_pickup(self, t_coil_c: float = T_REF) -> float:
        """Must-operate current of this (worst-case) unit at coil temperature T."""
        return self.ipu * math.sqrt(force_scale(t_coil_c, self.s_mo))

    # dynamics
    def operate(self, v_supply: float, v_drop, t_coil_c: float = T_REF, tmax: float = 0.1,
                move: bool = True, i0: float = 0.0):
        """Time from the drive step to contact make (g = 0). v_drop(i) is the driver's drop.
        Returns (t_make or inf, t_pickup (current reaches Ipu) or inf, solution)."""
        r = self.r23 * k_temp(t_coil_c)
        kf = force_scale(t_coil_c, self.s_mo)

        def f(t, y):
            lam, g, v = y
            i = lam / self.ind(g)
            dlam = v_supply - v_drop(i) - r * i
            if not move:
                return [dlam, 0.0, 0.0]
            net = 0.5 * i * i * self.dldg(g) - kf * self.fspring(g)
            if g >= GAP and net <= 0.0 and v >= 0.0:
                return [dlam, 0.0, 0.0]
            return [dlam, v, -net / self.m]

        def made(t, y):
            return y[1]
        made.terminal, made.direction = True, -1

        ipu_t = self.ipu * math.sqrt(kf)

        def pick(t, y):
            return y[0] / self.ind(y[1]) - ipu_t
        pick.terminal, pick.direction = (not move), 1

        sol = solve_ivp(f, [0.0, tmax], [i0 * self.ind(GAP), GAP, 0.0], events=[made, pick],
                        max_step=1e-5, rtol=1e-8, atol=1e-13, dense_output=False)
        t_make = float(sol.t_events[0][0]) if sol.t_events[0].size else math.inf
        t_pick = float(sol.t_events[1][0]) if sol.t_events[1].size else math.inf
        return t_make, t_pick, sol

    def release(self, i_hold: float, t_coil_c: float = T_REF, diode: tuple | None = (0.0, 0.0),
                tmax: float = 0.3):
        """Time from drive off to the armature back at rest (NC contact made).
        diode = (Is, n*Vt, Rs) Shockley freewheel parameters, or None for no freewheel path
        (current removed at once, the datasheet's test condition)."""
        r = self.r23 * k_temp(t_coil_c)
        kf = force_scale(t_coil_c, self.s_mo)
        lam0 = i_hold * self.ind(0.0) if diode is not None else 0.0

        def vd(i):
            if diode is None or i <= 0.0:
                return 0.0
            is_, nvt, rs = diode
            return nvt * math.log1p(i / is_) + rs * i

        def f(t, y):
            lam, g, v = y
            i = max(lam / self.ind(g), 0.0)
            dlam = -(r * i + vd(i)) if diode is not None else 0.0
            net = kf * self.fspring(g) - 0.5 * i * i * self.dldg(g)
            if g <= 0.0 and net <= 0.0 and v <= 0.0:
                return [dlam, 0.0, 0.0]
            return [dlam, v, net / self.m]

        def rest(t, y):
            return y[1] - GAP
        rest.terminal, rest.direction = True, 1

        def leave(t, y):
            return y[1] - 1e-9
        leave.terminal, leave.direction = False, 1

        sol = solve_ivp(f, [0.0, tmax], [lam0, 0.0, 0.0], events=[rest, leave], max_step=1e-5,
                        rtol=1e-8, atol=1e-14)
        t_rest = float(sol.t_events[0][0]) if sol.t_events[0].size else math.inf
        t_leave = float(sol.t_events[1][0]) if sol.t_events[1].size else math.inf
        return t_rest, t_leave, sol


def no_drop(i: float) -> float:
    return 0.0


def calibrate(coil: str, p: Params, r23: float | None = None) -> Relay | None:
    """Solve m so that the operate time at rated voltage, 23 C, equals 7 ms. None if no m does
    (the electrical rise alone is too slow, or the armature stalls)."""
    r23 = COILS[coil]["r23"] if r23 is None else r23
    vr = COILS[coil]["v_rated"]

    def err(logm):
        rl = Relay(coil, r23, p, m=10.0 ** logm)
        t, _, _ = rl.operate(vr, no_drop)
        return (t if math.isfinite(t) else 1.0) - T_OP_DS

    lo, hi = -9.0, 1.0
    try:
        if err(lo) > 0 or err(hi) < 0:
            return None
        logm = brentq(err, lo, hi, xtol=1e-7)
    except ValueError:
        return None
    return Relay(coil, r23, p, m=10.0 ** logm)


def band() -> list[Params]:
    """Class E band of the three unknown parameters (section 3.3 of the record)."""
    out = []
    for tau in (0.6e-3, 1.2e-3, 2.4e-3):
        for rho in (2.0, 3.0, 4.0):
            for sig in (0.5, 1.0, 2.0):
                out.append(Params(tau, rho, sig))
    return out


NOMINAL = Params(1.2e-3, 3.0, 1.0)


def fit_ok(rl: Relay) -> tuple[bool, float]:
    """Second anchor: release with no freewheel path at most 3 ms (datasheet)."""
    t, _, _ = rl.release(rl.v_rated / rl.r23, diode=None)
    return (t <= T_REL_DS), t


if __name__ == "__main__":
    for coil in ("std", "h1"):
        for p in band():
            rl = calibrate(coil, p)
            if rl is None:
                print(coil, p.key(), "no calibration")
                continue
            ok, trel = fit_ok(rl)
            print(coil, p.key(), f"m={rl.m:.3e} rel0={trel * 1e3:.2f} ms ok={ok} irel/ipu={rl.i_release() / rl.ipu:.2f}")
