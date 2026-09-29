#!/usr/bin/env python3
"""D-18 PA-permit gate: level interface, unpowered states and the A5 key-up case (WP-PDR-22).

cwht, hardware/sim/tx-pa-permit. Analysis record: docs/design/analysis/pa-permit-gate-d18.md.

Closes, as analysis, the D-18 lien of TS-012 revision 7 (INSP-118 finding-9, INSP-110 finding-24): as drawn,
a 3.3 V 74LVC1G10 NAND drives the gate of the DMP3099L P-FET that supplies the GVA-84+ from the 5 V bus, so
the P-FET sees VGS of about -1.7 V when it should be off; the gate's rail, level interface and unpowered state
are not stated; and the key-up level of REQ-TX-014 rests on the driver being unpowered.

Design analysed here (record section 3, "D18-2B"):
  U1 74LVC1G11 3-input AND on the Pico 2 3V3 rail; inputs TX_KEY and PA_EN (RP2350 GPIO, 4.7 k pull-downs) and
  the cutoff monostable Q (LM393 open collector, 10 k pull-up to the 5 V bus). The output is high only when
  all three are high ("permit").
  Branch P (driver supply): U1 -> 10 k -> 2N3904 Q2 base (100 k base to ground); Q2 collector -> 1 k -> gate of
  the DMP3099L Q1, whose gate has 10 k to its source; Q1 source on the F3 node (5 V bus -> ferrite bead ->
  22 uF), drain = TX5 (100 nF, 2.2 k bleed) -> choke -> GVA-84+ pin 3.
  Branch C (VGG clamp): U1 -> 10 k -> 2N3904 Q3 base (100 k to ground); Q3 collector = clamp gate node with
  10 k to the 5 V bus -> gate of the 2N7002 clamp Q4 on the VGG node.
  Not permitted, or U1 unpowered or open: both 2N3904 off, so the P-FET gate is at its source (VGS = 0) and
  the clamp gate at the 5 V bus (full drive).

Revision 1 (record revision 1, the two Major findings of the review of revision 0; runs 2026-09-29-d18r1-*):
  - the open-collector cutoffs that TS-012 section 8.1 wires onto the VGG node (REQ-SYS-180 backstop, REQ-SYS-181
    95 C trip, cell 60 C trip, REQ-SYS-092 VBUS inhibit) sit on the Q node under its 10 k pull-up instead, so
    each one takes U1's output low and unpowers the driver as well as clamping VGG; one 1N5711W D1 from the VGG
    node (anode) to the Q node (cathode) keeps a VGG path from every cutoff that does not pass through U1;
  - the REQ-SYS-183 level (-57 dBm, the RF-off level of REQ-SYS-120) is reported in every state with fewer than
    both conditions asserted, CLK1 running and the relay in transmit (key-up deck state windows), and in the
    cutoff and U1-stuck-high cases of the sequencing deck; the verdicts are expected states (not design
    criteria), so the exit status says whether they are as the record states.
  The as-drawn run 2026-09-29-d18-asis (revision 0 script, in its run folder) is not rerun: its deck is unchanged.

Stages (each writes results/<run-id>/: deck, LTspice .log/.raw, wrapper.txt, result.json, result.csv, plots,
this script as run):
  keyup    d18_keyup.cir: one element and the key-up window with PA_EN asserted and CLK1 running (the REQ-TX-014
           condition), 52 corner cases (5 V bus, 3V3 and GPIO high level, P-FET threshold including the hot
           estimate, 2N3904 beta, loop nominal or wound to the rail, and the interval-13 fallback timing of
           finding-9 (c)); the antenna level from the simulated driver supply and VGG for four isolation cases
  asis     d18_asis.cir: the gate as TS-012 revision 7 draws it (3.3 V NAND output straight to the P-FET gate and
           the clamp gate), 36 cases: shows the defect of finding-9 (a) and its REQ-TX-014 consequence
  seq      d18_seq.cir: power-up orders, brown-outs, single-line faults and single component faults, 13 cases
  summary  summary.json, level_cases.png: steady key-up level per isolation case and the break-even isolation
  replot STAGE   re-analyse an existing run (the generated deck must equal the run's copy)

Exit status: 0 when every criterion the design must pass passes and every expected state (as-drawn defect,
component-fault cases) is as the record states; 3 otherwise (printed and in result.json); 2 on a tool error.
Every LTspice run goes through tools/ltspice-batch.sh (ACC-LTSPICE-001).

Class of every model number: D datasheet value, DD derived from a datasheet (graph read, arithmetic),
E estimate. They are listed in MODEL and in the record section 4.
"""
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from spicelib import RawRead  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
WRAPPER = REPO / "tools" / "ltspice-batch.sh"
RESULTS = HERE / "results"
PADATA = REPO / "hardware" / "sim" / "tx-pa" / "data"
DATE = "2026-09-29"
REV = "d18r1"                  # revision 1 of this script; revision 0 runs are 2026-09-29-d18-* (own script copy)
ASIS_RUN = "2026-09-29-d18-asis"   # unchanged deck, not rerun in revision 1

# ------------------------------------------------------------------------------------------ model inputs
MODEL = {
    "dmp3099l": dict(cls="D", src="Diodes DMP3099L DS36081 Rev. 5-2 (May 2025), page 2 and Figure 7",
                     vgs_th_min=-1.0, vgs_th_max=-2.1, rds_on_4v5=0.099, idss_na=800, ciss_pf=563, crss_pf=41,
                     rg=10.3, idm_a=11.0,
                     vgs_th_hot_min=-0.73,
                     vgs_th_hot_note="DD/E: Figure 7 (typical, -250 uA) falls from about 1.76 V at 25 C to 1.57 V at "
                                     "100 C and 1.35 V at 150 C, about -2.6 mV/K; applied to the -1.0 V minimum: "
                                     "-0.81 V at 100 C, -0.73 V at 125 C"),
    "2n3904": dict(cls="D", src="onsemi 2N3903/D Rev. 9 (Aug 2021): hFE min 40 at 0.1 mA, 70 at 1 mA; VCE(sat) "
                               "0.2 V max and VBE(sat) 0.65 to 0.85 V at 10 mA / 1 mA; ICEX 50 nA max at 30 V; ts 200 "
                               "ns. SPICE model: the widely published Fairchild/onsemi 2N3904 model, BF stepped",
                   hfe_min_0ma1=40, hfe_min_1ma=70, vce_sat=0.2, vbe_sat_max=0.85, icex_na=50, beta_cases=(70, 416)),
    "2n7002": dict(cls="D", src="Nexperia 2N7002 Rev. 7 (8 Sep 2011) Table 6",
                   vgs_th=(1.0, 2.0, 2.5), vgs_th_cold_max=2.75, vgs_th_hot_min=0.6, rds_on_4v5_max=5.3,
                   idss_150c_ua=10),
    "74lvc1g11": dict(cls="D", src="Nexperia 74LVC1G11 Rev. 13.1 (15 Aug 2023) Tables 6 to 8",
                      vih=2.0, vil=0.8, voh_100ua="VCC-0.1", vi_max=5.5, ioff_ua=2, tpd_max_ns=4.9,
                      note="inputs 5 V tolerant at any VCC (VI 0 to 5.5 V); IOFF partial power-down"),
    "rp2350": dict(cls="D", src="RP2350 datasheet Table 1436 as quoted in docs/research/keyer-verification-and-"
                                "key-input-network.md: VOH min 2.62 V, VOL max 0.5 V; erratum E9 pad leakage about "
                                "120 uA (typical, A2 stepping)", voh_min=2.62, vol_max=0.5, e9_ua=120),
    "lm393": dict(cls="D", src="TI LM393 SLCS005AH (Apr 2025): VOL 400 mV max at 4 mA (25 C), 700 mV full range; "
                               "IOH 0.1 nA typ at 5 V", vol_max_4ma=0.7),
    "gva84": dict(cls="D", src="Mini-Circuits GVA-84+ Rev. F: fixed +5 V operation, device 4.8/5.0/5.2 V, "
                               "85/108/130 mA, 0.058 mA/mV, gain 22.9/24.1/25.3 dB at 0.1 GHz, input max +13 dBm, "
                               "Darlington (transient protected)",
                  i_typ=0.108, di_dv=0.058, v_cut=3.14,
                  v_cut_note="E: I(V) = 0.058 A/V x (V - 3.14 V), the datasheet slope at 5 V extrapolated to zero "
                             "current (3.14 V, about two InGaP base-emitter drops plus the internal resistors); "
                             "soft-plus below"),
    "1n5711w": dict(cls="D", src="Diodes 1N5711W DS11015 Rev. 15-2 (Aug 2022), Electrical Characteristics: VF "
                                 "0.41 V max at 1 mA, 1.00 V max at 15 mA; IR 200 nA max at 50 V; V(BR)R 70 V min; IFM "
                                 "15 mA; CT 2.0 pF max. BOM row 14 part",
                    vf_1ma=0.41, vf_15ma=1.00, ir_na_50v=200, ifm_ma=15,
                    fit="DD: SPICE diode through both VF maxima (Is 1.07 nA, N 1.05, Rs 36.9 ohm), a maximum-VF model; "
                        "hot reverse leakage x 64 at about +60 K (E), 12.8 uA, taken analytically"),
    "cutoff_sinks": dict(cls="E", src="TS-012 section 8.1: the REQ-SYS-055 monostable, the REQ-SYS-180 backstop, the "
                                      "REQ-SYS-181 95 C trip and the cell 60 C trip are LM393 open-collector outputs "
                                      "(VOL 0.7 V max full range at 4 mA, IOH-LKG 20 nA); the REQ-SYS-092 VBUS inhibit "
                                      "is an open-collector or open-drain pull whose part the TS-005 remnant sets, "
                                      "modelled here as a 2N7002-class open drain (5.3 ohm, IDSS 10 uA hot)"),
    "lm2940_bus": dict(cls="E", src="LM2940-5 as a 5.0 V source, 4.75 to 5.25 V (TI SNVS769J 6.5 as TS-012 "
                                    "quotes it); 50 mohm and 5 uH for the regulator's loop response, 22 uF output "
                                    "capacitor (E)"),
    "f3": dict(cls="E", src="spurs-ts012.md F3: GVA-84+ supply through a ferrite bead and 22 uF; here placed "
                            "upstream of the P-FET (bead 0.2 ohm + 1 uH, 22 uF, 10 mohm ESR)"),
}

VBUS_NOM = 5.0
PA_EN_T = 7e-3          # TS-012 section 7.3 revision 6: PA_EN at t0 + 7 ms
TXK_T = 8e-3            # TX_KEY at t0 + 8 ms
RAMP_T = 10e-3          # ramp start at t0 + 10 ms
PA_EN_T_FB = 11e-3      # interval-13 fallback (finding-9 (c)): check ends t0 + 11 ms
RAMP_T_FB = 11.5e-3     # ramp at 11.5 ms
T1090 = 5e-3            # 5 ms setting
TFULL = T1090 / 0.5903  # raised cosine 0-to-100 % duration for a 10-to-90 % time
HOLD = 16e-3            # ramp start to fall start
PA_EN_OFF = 60e-3       # end of the over: SW-SAFE clears PA_EN
T_END = 65e-3
VGG_DIV = 5.1 / (2.7 + 5.1)
VGG_TOP = 2.75           # E: open-loop element top, about 5 W from the A5 table at 7.9 V drain (not a keying result)

# key-up cases: (label, vbus, v33, vgpio_high, p-fet vto, 2n3904 bf, loop stuck, fallback)
def keyup_cases():
    rows = []
    for vb in (4.75, 5.25):
        for v33, vg in ((3.0, 2.62), (3.6, 3.6)):
            for vto in (-0.73, -1.0, -2.1):
                for bf in (70, 416):
                    for ls in (0, 1):
                        rows.append(dict(vbus=vb, v33=v33, vgp=vg, vtop=vto, bf=bf, ls=ls, fb=0))
    for vb in (4.75, 5.25):
        for vto in (-0.73, -2.1):
            rows.append(dict(vbus=vb, v33=3.0, vgp=2.62, vtop=vto, bf=70, ls=0, fb=1))
    for i, r in enumerate(rows, 1):
        r["case"] = i
        r["label"] = (f"VBUS {r['vbus']:.2f} V, 3V3 {r['v33']:.1f} V, GPIO {r['vgp']:.2f} V, P-FET Vth "
                      f"{r['vtop']:.2f} V, beta {r['bf']}, loop {'wound to rail' if r['ls'] else 'nominal'}"
                      f"{', interval-13 fallback' if r['fb'] else ''}")
    return rows


def asis_cases():
    rows = []
    for vb in (4.75, 5.0, 5.25):
        for v33 in (3.0, 3.3, 3.6):
            for vto in (-0.73, -1.0, -1.55, -2.1):
                rows.append(dict(vbus=vb, v33=v33, vtop=vto))
    for i, r in enumerate(rows, 1):
        r["case"] = i
        r["label"] = f"VBUS {r['vbus']:.2f} V, NAND rail {r['v33']:.1f} V, P-FET Vth {r['vtop']:.2f} V"
    return rows


# ------------------------------------------------------------------------------------------ isolation cases
G0_DB = 24.1                      # D: GVA-84+ gain typ at 0.1 GHz
G_MIN_DB = 22.5                   # pa-drive-ts012.md lowest corner (gain at 148 MHz, min part)
P_MOD_IN_MAX_DBM = 10 * math.log10(26.5)   # pa-drive-ts012.md s1: in-service drive at most 26.5 mW
OUT_PAD_DB = 3.00                 # A5 output pad 300/18/300 ohm (pa-drive-ts012.md)
LPF_RELAY_DB = 0.5                # keying-ts012.md section 3.1
P_GVA_IN_SOT = P_MOD_IN_MAX_DBM + OUT_PAD_DB - G_MIN_DB           # select-on-test design basis
# bound: the highest level ahead of the drive pad in pa-drive d4 (48.6 mW at the module with the 18.42 dB fixed
# pad and 25.3 dB gain) with the smallest pad of the select-on-test set (13.48 dB)
PRE_PAD_MAX_DBM = 10 * math.log10(48.6) + OUT_PAD_DB - 25.3 + 18.42
P_GVA_IN_BOUND = PRE_PAD_MAX_DBM - 13.48
_Gl = 10 ** (G0_DB / 20)
RF_EST = 50 * (1 + _Gl)           # matched shunt-feedback Darlington: |S21| ~ Rf/Z0 - 1
ISO_GVA_EST = -20 * math.log10(100 / (100 + RF_EST))   # unpowered: Rf in series between two 50 ohm ports
ISO_CASES = {
    "L1": dict(name="estimates (GVA-84+ unpowered {:.1f} dB, module VGG-off 30 dB)".format(ISO_GVA_EST),
               pin=P_GVA_IN_SOT, iso_g=ISO_GVA_EST, iso_m=30.0),
    "L2": dict(name="GVA-84+ passive bound (0 dB), module 30 dB", pin=P_GVA_IN_SOT, iso_g=0.0, iso_m=30.0),
    "L3": dict(name="estimate, module at the datasheet 'up to 60 dB'", pin=P_GVA_IN_SOT, iso_g=ISO_GVA_EST,
               iso_m=60.0),
    "L4": dict(name="drive bound (smallest pad, highest pre-pad level), GVA-84+ 0 dB, module 30 dB",
               pin=P_GVA_IN_BOUND, iso_g=0.0, iso_m=30.0),
}
REQ_TX_014_DBM = -30.0
REQ_SYS_183_DBM = -57.0
# revision 1: states with fewer than both REQ-SYS-120 conditions asserted, CLK1 running and the relay in transmit
# (key-up deck windows). REQ-SYS-120 defines RF off as the REQ-SYS-183 level, so each is compared with -57 dBm.
OFF_STATES = {
    "lead": "lead-in before either line (t0 + 1 ms, CLK1 on, to the first of PA_EN and TX_KEY)",
    "one": "one line only (PA_EN only 7 to 8 ms; TX_KEY only 8 to 11 ms in the interval-13 fallback)",
    "keyup": "TX_KEY low, PA_EN high: between elements and through the hang time (REQ-TX-014 state)",
    "end": "PA_EN cleared at the end of the over, CLK1 still on, relay not yet released",
}
# expected REQ-SYS-183 verdicts in those states (the record's statement; not design criteria): margin shown on the
# estimates L1 and on L3, not shown on the passive bound L2 and the drive bound L4
REQ183_EXPECTED = {"L1": "PASS", "L2": "FAIL", "L3": "PASS", "L4": "FAIL"}

# ------------------------------------------------------------------------------------------ PA table (A5)
def _a5_table():
    a = np.loadtxt(PADATA / "ra07_pout_vs_vgg_135.csv", delimiter=",", skiprows=1)
    b = np.loadtxt(PADATA / "ra07_pout_vs_vgg_155.csv", delimiter=",", skiprows=1)
    vv = np.round(np.arange(2.32, 3.90001, 0.02), 2)
    w = 0.5 * (np.interp(vv, a[:, 0], a[:, 1]) + np.interp(vv, b[:, 0], b[:, 1]))
    cs = [np.loadtxt(PADATA / f"ra07_pout_vs_vdd_{f}.csv", delimiter=",", skiprows=1) for f in (135, 155)]
    sc = float(np.mean([np.interp(7.9, c[:, 0], c[:, 1]) / np.interp(7.2, c[:, 0], c[:, 1]) for c in cs]))
    return vv, w * sc


PA_V, PA_W = _a5_table()
SUBTH_DB_PER_V = 100.0  # E, as keying-ts012.md


def pa_out_dbm(vgg):
    vgg = np.asarray(vgg, float)
    p = np.interp(np.clip(vgg, PA_V[0], PA_V[-1]), PA_V, PA_W)
    dbm = 10 * np.log10(p * 1e3)
    below = vgg < PA_V[0]
    dbm = np.where(below, 10 * np.log10(PA_W[0] * 1e3) - SUBTH_DB_PER_V * (PA_V[0] - vgg), dbm)
    return dbm


def gva_gain_db(v, iso_g):
    """E: gain of the GVA-84+ against its supply: -iso_g (unpowered) at or below the zero-current point 3.14 V,
    G0 at 4.8 V (datasheet minimum device voltage) and above, linear in dB between."""
    x = np.clip((np.asarray(v, float) - MODEL["gva84"]["v_cut"]) / (4.8 - MODEL["gva84"]["v_cut"]), 0, 1)
    return -iso_g + (G0_DB + iso_g) * x


def antenna_dbm(vtx5, vgg, case):
    """Level at the antenna port: module output from VGG (A5 table at 7.9 V drain, drive changes 1:1 with the
    driver gain) plus the leakage path (drive into the GVA-84+, its supply-dependent gain, 3 dB pad, module
    VGG-off isolation), less the LPF and relay loss."""
    g = gva_gain_db(vtx5, case["iso_g"])
    pa = pa_out_dbm(vgg) + (g - G0_DB)
    leak = case["pin"] + g - OUT_PAD_DB - case["iso_m"]
    tot = 10 * np.log10(10 ** (pa / 10) + 10 ** (leak / 10)) - LPF_RELAY_DB
    return tot


# ------------------------------------------------------------------------------------------ netlist parts
MODELS = """* --- device models ---------------------------------------------------------------------------------
* DMP3099L (D: DS36081 Rev. 5-2): VGS(th) -1.0 to -2.1 V at -250 uA (stepped; hot estimate -0.73 V), RDS(on)
* 99 mohm max at -4.5 V, Ciss 563 pF, Crss 41 pF, RG 10.3 ohm. VDMOS fit: Kp 5.6 A/V^2 with Rd + Rs 25 mohm gives
* 99 mohm at -4.5 V with the -2.1 V threshold; sub-threshold slope 0.04 V (E, about 92 mV/decade).
.model DMP3099L VDMOS(pchan Vto={VTOP} Kp=5.6 Rd=20m Rs=5m Rg=10.3 Cgdmax=300p Cgdmin=41p Cgs=520p Cjo=100p Is=1e-12 Rb=20m ksubthres=0.04)
* 2N7002 clamp (D: Nexperia Rev. 7): VGS(th) 1.0 / 2.0 / 2.5 V, 2.75 V max at -55 C (used: worst for the clamp),
* RDS(on) 5.3 ohm max at 4.5 V; Ciss 50 pF max.
.model N2N7002 VDMOS(Vto=2.75 Kp=0.2 Rd=1.5 Rs=0.5 Rg=10 Cgdmax=10p Cgdmin=3.5p Cgs=40p Cjo=10p Is=1e-14 ksubthres=0.04)
* 2N3904: the widely published Fairchild/onsemi SPICE model; BF stepped 70 (hFE min at 1 mA) and 416 (model).
.model Q2N3904X NPN(IS=6.734f XTI=3 EG=1.11 VAF=74.03 BF={BFX} NE=1.259 ISE=6.734f IKF=66.78m XTB=1.5 BR=.7371 NC=2 ISC=0 IKR=0 RC=1 CJC=3.638p MJC=.3085 VJC=.75 FC=.5 CJE=4.493p MJE=.2593 VJE=.75 TR=239.5n TF=301.2p ITF=.4 VTF=4 XTF=2 RB=10)
* 74LVC1G11/74LVC1G10 output: 25 ohm while VCC > 1.2 V, high impedance below (IOFF partial power-down).
.model SWVCC SW(Ron=25 Roff=1e9 Vt=1.2 Vh=0.1)
.model SWQ SW(Ron=100 Roff=1e10 Vt=0.5 Vh=0.05)
* revision 1: LM393 cutoff output at its VOL maximum (switch to a 0.7 V source), VBUS inhibit open drain (5.3 ohm)
.model SWK SW(Ron=1 Roff=1e10 Vt=0.5 Vh=0.05)
.model SWB SW(Ron=5.3 Roff=1e10 Vt=0.5 Vh=0.05)
* 1N5711W (D: Diodes DS11015 Rev. 15-2): fit through VF max 0.41 V at 1 mA and 1.00 V at 15 mA (maximum-VF model)
.model D1N5711W D(Is=1.07n N=1.05 Rs=36.9 Cjo=2p BV=70 Ibv=10u)
"""

SUPPLY = """* --- 5 V bus: LM2940-5 (E: 50 mohm and 5 uH for its loop, 22 uF output capacitor) -------------------------
BLDO ldo 0 V={VBUSX}
LLDO ldo busi 5u Rser=50m
CBUS busi 0 22u Rser=20m
RBUSM busi bus 1m
* F3 (spurs-ts012.md): ferrite bead and 22 uF, upstream of the P-FET (E: 0.2 ohm, 1 uH)
LB bus nb 1u Rser=0.2
CF3 nb 0 22u Rser=10m
"""

GVA_LOAD = """* --- GVA-84+ supply node TX5 and the device (E: I = 0.058 A/V x (V - 3.14 V), soft-plus below) ---------
C5B tx5 0 100n Rser=10m
LCH tx5 gvaf 1u Rser=0.5
BGVA gvaf 0 I=0.058*0.05*ln(1+exp((V(gvaf)-3.14)/0.05))
"""

VGG_NODE = """* --- VGG node: error-amplifier output (MCP6002 on the 5 V bus) through the 0.654 divider -----------------
BOA oa 0 V=min(V(bus),max(0,V(bus)*if(LS>0.5,1,ATOP)*{ENV}))
RD1 oa vgg 2.7k
RD2 vgg 0 5.1k
CVG vgg 0 10n
"""


def gpio(name, node, en_expr, v_expr):
    """RP2350 GPIO pad: driven through 50 ohm when en = 1, high impedance when en = 0; 4.7 k pull-down (TS-012
    D-18) and the E9 pad leakage (120 uA, into the pad) in every case."""
    return (f"B{name} 0 {node} I=({en_expr})*(({v_expr})-V({node}))/50\n"
            f"R{name}PD {node} 0 4.7k\n"
            f"I{name}E9 0 {node} {{IE9}}\n")


def and_gate(inv=False, vcc="v33", out="y"):
    th = f"if(V({vcc})>2.7,1.4,0.5*V({vcc}))"
    s = lambda n: f"1/(1+exp(-(V({n})-{th})/0.02))"  # noqa: E731
    prod = f"{s('tk')}*{s('pe')}*{s('q')}"
    val = f"V({vcc})*(1-{prod})" if inv else f"V({vcc})*{prod}"
    return (f"BU1 u1i 0 V={val}\n"
            f"SU1 u1i u1o {vcc} 0 SWVCC\n"
            f"RU1O u1o {out} {{RUOPEN}}\n")


def fixed_gate():
    return """* --- D18-2B level interface --------------------------------------------------------------------------
* branch P: U1 -> 10 k -> Q2 base (100 k to ground); Q2 collector -> 1 k -> P-FET gate; 10 k gate to source
RB1 y b1 10k
RBE1 b1 0 100k
Q2 c1 b1 0 Q2N3904X
RQ2F c1 0 {RQ2SH}
RG1 c1 gp 1k
RPU1 gp nb {RPU1V}
M1 tx5 gp nb nb DMP3099L
RBL tx5 0 2.2k
* branch C: U1 -> 10 k -> Q3 base (100 k to ground); Q3 collector = clamp gate, 10 k to the 5 V bus
RB2 y b2 10k
RBE2 b2 0 100k
Q3 nc b2 0 Q2N3904X
RQ3F nc 0 {RQ3SH}
RPU2 nc bus {RPU2V}
M4 vgg nc 0 0 N2N7002
"""


def cutoffs_r1(qcut="0", qvb="0", vcut="0"):
    """Revision 1: the wired-OR cutoffs on the Q node, D1 from VGG to the Q node, and the fault hooks.
    QCUT: an LM393 cutoff (REQ-SYS-180, 181, cell 60 C) pulls Q to its 0.7 V VOL maximum; QVB: the VBUS inhibit
    (REQ-SYS-092) pulls Q through 5.3 ohm; VCUT: the same LM393 pull on the VGG node, as TS-012 section 8.1 draws
    it (comparison case only); RD1SER: D1 in circuit (1 mohm) or open; RU1STK: U1 output shorted to 3V3."""
    return ("* --- revision 1: cutoffs on the Q node, D1 VGG -> Q, fault hooks ------------------------------------------\n"
            "VOLX volx 0 0.7\n"
            f"BCQ cq 0 V={qcut}\n"
            "SCQ q volx cq 0 SWK\n"
            f"BCB cb 0 V={qvb}\n"
            "SCB q 0 cb 0 SWB\n"
            f"BCV cv 0 V={vcut}\n"
            "SCV vgg volx cv 0 SWK\n"
            "D1 vgg d1k D1N5711W\n"
            "RD1S d1k q {RD1SER}\n"
            "RSTK y v33 {RU1STK}\n")


def asis_gate():
    return """* --- as drawn in TS-012 revision 7: NAND output straight to the P-FET gate and the clamp gate -----------
RG1 y gp 100
M1 tx5 gp nb nb DMP3099L
RG4 y nc 100
M4 vgg nc 0 0 N2N7002
"""


def monostable(expired_expr="0"):
    return (f"* --- cutoff monostable output Q: LM393 open collector, 10 k pull-up to the 5 V bus --------------------\n"
            f"RQPU q bus 10k\n"
            f"BQC qc 0 V={expired_expr}\n"
            f"SQ q 0 qc 0 SWQ\n")


def env_expr(fb_param=True):
    trs = "TRS"
    return (f"if(time<{trs},0,if(time<{trs}+{TFULL:.6e},0.5-0.5*cos(pi*(time-{trs})/{TFULL:.6e}),"
            f"if(LS>0.5,1,if(time<TFA,1,if(time<TFA+{TFULL:.6e},0.5+0.5*cos(pi*(time-TFA)/{TFULL:.6e}),0)))))")


def table(param, rows, key):
    pts = ",".join(f"{r['case']},{r[key]:g}" for r in rows)
    return f".param {param}=table(CASE,{pts})\n"


SAVE = ".save V(tx5) V(gp) V(nb) V(bus) V(vgg) V(nc) V(y) V(tk) V(pe) V(q) V(v33) Id(M1) I(D1)\n"


def gen_keyup():
    rows = keyup_cases()
    n = len(rows)
    s = ["* d18_keyup.cir: D-18 gate D18-2B, A5 key-up case with PA_EN asserted and CLK1 running (REQ-TX-014)\n",
         "* generated by hardware/sim/tx-pa-permit/d18_run.py; one element (5 ms setting), key-up window to 60 ms,\n",
         "* PA_EN cleared at 60 ms (end of the over). Cases: see result.json.\n",
         f".step param CASE 1 {n} 1\n"]
    for p, k in (("VBUSX", "vbus"), ("V33X", "v33"), ("VGPX", "vgp"), ("VTOP", "vtop"), ("BFX", "bf"),
                 ("LS", "ls"), ("FB", "fb")):
        s.append(table(p, rows, k))
    s.append(f".param TPE=if(FB>0.5,{PA_EN_T_FB:g},{PA_EN_T:g}) TRS=if(FB>0.5,{RAMP_T_FB:g},{RAMP_T:g})\n")
    s.append(f".param TFA=TRS+{HOLD:g} TKF=TFA+{TFULL:.6e}+1m\n")
    s.append(".param IE9=120u RUOPEN=1m RQ2SH=1e12 RQ3SH=1e12 RPU1V=10k RPU2V=10k RD1SER=1m RU1STK=1e12\n")
    s.append(f".param ATOP={VGG_TOP:g}/({VGG_DIV:.6f}*VBUSX)\n")
    s.append(MODELS + SUPPLY)
    s.append("V33 v33 0 {V33X}\n")
    s.append(gpio("TK", "tk", "1", f"VGPX*(time>{TXK_T:g})*(time<TKF)"))
    s.append(gpio("PE", "pe", "1", f"VGPX*(time>TPE)*(time<{PA_EN_OFF:g})"))
    s.append(monostable("0"))
    s.append(and_gate(False))
    s.append(fixed_gate() + cutoffs_r1() + GVA_LOAD + VGG_NODE.replace("{ENV}", env_expr()))
    s.append(SAVE)
    s.append(f".tran 0 {T_END:g} 0 20u\n.options plotwinsize=0\n.end\n")
    return "d18_keyup.cir", "".join(s), rows


def gen_asis():
    rows = asis_cases()
    n = len(rows)
    s = ["* d18_asis.cir: D-18 gate as TS-012 revision 7 draws it (74LVC1G10 NAND on 3.3 V driving the DMP3099L\n",
         "* gate and the 2N7002 clamp gate directly); element and key-up with PA_EN asserted. Generated by d18_run.py\n",
         f".step param CASE 1 {n} 1\n"]
    for p, k in (("VBUSX", "vbus"), ("V33X", "v33"), ("VTOP", "vtop")):
        s.append(table(p, rows, k))
    s.append(f".param BFX=100 LS=0 TPE={PA_EN_T:g} TRS={RAMP_T:g} TFA=TRS+{HOLD:g} TKF=TFA+{TFULL:.6e}+1m\n")
    s.append(".param IE9=120u RUOPEN=1m\n")
    s.append(f".param ATOP={VGG_TOP:g}/({VGG_DIV:.6f}*VBUSX)\n")
    s.append(MODELS + SUPPLY)
    s.append("V33 v33 0 {V33X}\n")
    s.append(gpio("TK", "tk", "1", f"V33X*(time>{TXK_T:g})*(time<TKF)"))
    s.append(gpio("PE", "pe", "1", f"V33X*(time>TPE)*(time<{PA_EN_OFF:g})"))
    s.append(monostable("0").replace("RQPU q bus 10k", "RQPU q v33 10k"))
    s.append(and_gate(True))
    s.append(asis_gate() + GVA_LOAD + VGG_NODE.replace("{ENV}", env_expr()))
    s.append(SAVE)
    s.append(f".tran 0 {T_END:g} 0 20u\n.options plotwinsize=0\n.end\n")
    return "d18_asis.cir", "".join(s), rows


# power sequencing and fault cases: every waveform is a time table; P = permit window where the design must
# power the driver and release the clamp; the rest must be off. 'expect' names cases whose component fault
# defeats one output (the analysis states the consequence).
T_SEQ = 40e-3


def seq_cases():
    up = [(0, 0), (1e-3, 0), (1.1e-3, 1)]            # rail up at 1 ms (100 us ramp)
    on = [(0, 1)]
    c = []

    def row(tag, desc, bus, v33, en, tk, pe, qexp="0", permit=(), expect=None, faults=None, onwin=None,
            qcut="0", qvb="0", vcut="0"):
        # permit: windows in which the gate may power the driver (the off criteria apply outside them);
        # onwin: windows in which it must (default: the permit windows); qcut, qvb, vcut: revision 1 cutoff pulls
        c.append(dict(tag=tag, desc=desc, bus=bus, v33=v33, en=en, tk=tk, pe=pe, qexp=qexp, permit=list(permit),
                      onwin=list(onwin if onwin is not None else permit), expect=expect or {},
                      faults=faults or {}, qcut=qcut, qvb=qvb, vcut=vcut))

    row("S1", "5 V bus first (1 ms), 3V3 at 6 ms (1 ms soft start), GPIOs high impedance with the pull-downs and "
        "E9 leakage until 12 ms, then driven; permit 20 to 30 ms",
        up, [(0, 0), (6e-3, 0), (7e-3, 1)], [(0, 0), (12e-3, 0), (12.001e-3, 1)],
        [(0, 0), (20e-3, 0), (20.00001e-3, 1), (30e-3, 1), (30.00001e-3, 0)],
        [(0, 0), (19.9e-3, 0), (19.90001e-3, 1)], permit=[(20e-3, 30e-3)])
    row("S2", "3V3 first (USB), GPIOs driven low from 3 ms, 5 V bus at 8 ms; permit 20 to 30 ms",
        [(0, 0), (8e-3, 0), (8.1e-3, 1)], up, [(0, 0), (3e-3, 0), (3.001e-3, 1)],
        [(0, 0), (20e-3, 0), (20.00001e-3, 1), (30e-3, 1), (30.00001e-3, 0)],
        [(0, 0), (19.9e-3, 0), (19.90001e-3, 1)], permit=[(20e-3, 30e-3)])
    row("S3", "3V3 brown-out while permitted: 3V3 falls 3.3 to 0 V from 20 to 21 ms; the GPIO highs follow it",
        on, [(0, 1), (20e-3, 1), (21e-3, 0)], on, [(0, 0), (5e-3, 0), (5.00001e-3, 1)],
        [(0, 0), (4.9e-3, 0), (4.90001e-3, 1)], permit=[(5e-3, 21e-3)], onwin=[(5e-3, 20e-3)])
    row("S4", "5 V bus collapse while permitted: bus falls to 0 from 20 to 21 ms (Q follows through its pull-up)",
        [(0, 1), (20e-3, 1), (21e-3, 0)], on, on, [(0, 0), (5e-3, 0), (5.00001e-3, 1)],
        [(0, 0), (4.9e-3, 0), (4.90001e-3, 1)], permit=[(5e-3, 21e-3)], onwin=[(5e-3, 20e-3)])
    row("L1", "monostable expires (Q low) at 20 ms with TX_KEY and PA_EN high",
        on, on, on, [(0, 0), (5e-3, 0), (5.00001e-3, 1)], [(0, 0), (4.9e-3, 0), (4.90001e-3, 1)],
        qexp="(time>20m)", permit=[(5e-3, 20e-3)])
    row("L2", "SW-SAFE clears PA_EN at 20 ms with TX_KEY stuck high",
        on, on, on, [(0, 0), (5e-3, 0), (5.00001e-3, 1)],
        [(0, 0), (4.9e-3, 0), (4.90001e-3, 1), (20e-3, 1), (20.00001e-3, 0)], permit=[(5e-3, 20e-3)])
    row("L3", "TX_KEY stuck high, PA_EN never set (a single stuck line)",
        on, on, on, on, [(0, 0)])
    row("L4", "PA_EN stuck high (or a corrupted permit flag), TX_KEY never set",
        on, on, on, [(0, 0)], on)
    row("F1", "U1 output open (lifted pin or missing part) with all three inputs high",
        on, on, on, [(0, 0), (5e-3, 0), (5.00001e-3, 1)], [(0, 0), (4.9e-3, 0), (4.90001e-3, 1)],
        faults=dict(RUOPEN="1e12"))
    row("F2", "branch P pull-up (10 k gate to source) open: permit 5 to 20 ms, then TX_KEY falls",
        on, on, on, [(0, 0), (5e-3, 0), (5.00001e-3, 1), (20e-3, 1), (20.00001e-3, 0)],
        [(0, 0), (4.9e-3, 0), (4.90001e-3, 1)], permit=[(5e-3, 20e-3)],
        expect=dict(driver_after_permit="on (P-FET gate holds its charge)", clamp="on"),
        faults=dict(RPU1V="1e12"))
    row("F3", "Q2 collector-emitter short (1 ohm): no permit at any time",
        on, on, on, [(0, 0)], [(0, 0)], expect=dict(driver="on", clamp="on"), faults=dict(RQ2SH="1"))
    row("F4", "branch C pull-up (10 k to the 5 V bus) open: no permit at any time",
        on, on, on, [(0, 0)], [(0, 0)], expect=dict(driver="off", clamp="off"), faults=dict(RPU2V="1e12"))
    row("F5", "Q3 collector-emitter short (1 ohm): no permit at any time",
        on, on, on, [(0, 0)], [(0, 0)], expect=dict(driver="off", clamp="off"), faults=dict(RQ3SH="1"))
    # revision 1 (finding-1 of the SA review): the wired-OR cutoffs on the Q node, D1, and the U1 stuck-high cases
    pk = [(0, 0), (5e-3, 0), (5.00001e-3, 1)]
    pp = [(0, 0), (4.9e-3, 0), (4.90001e-3, 1)]
    row("C1", "REQ-SYS-180 backstop (LM393 #1, at its 0.7 V VOL maximum) pulls the Q node at 20 ms with TX_KEY and "
        "PA_EN high and the monostable retriggered (its own output high); stands for the REQ-SYS-181 95 C trip and "
        "the cell 60 C trip, the same LM393 output on the same node",
        on, on, on, pk, pp, qcut="(time>20m)", permit=[(5e-3, 20e-3)])
    row("C2", "REQ-SYS-092 VBUS inhibit held from power-up: USB first (3V3 at 1 ms), inhibit on from 1 ms, a fault "
        "build drives TX_KEY and PA_EN high from 3 ms, cells in (5 V bus) at 8 ms; never permitted",
        [(0, 0), (8e-3, 0), (8.1e-3, 1)], up, [(0, 0), (3e-3, 0), (3.001e-3, 1)],
        [(0, 0), (3e-3, 0), (3.001e-3, 1)], [(0, 0), (3e-3, 0), (3.001e-3, 1)], qvb="(time>1m)")
    row("C3", "REQ-SYS-092 VBUS inhibit arrives at 20 ms (USB plugged in during an over), TX_KEY and PA_EN high",
        on, on, on, pk, pp, qvb="(time>20m)", permit=[(5e-3, 20e-3)])
    row("C4", "D1 open (single fault) and the backstop pulls Q at 20 ms: U1 still acts",
        on, on, on, pk, pp, qcut="(time>20m)", permit=[(5e-3, 20e-3)], faults=dict(RD1SER="1e12"))
    row("A1", "as TS-012 section 8.1 draws it: the backstop pull on the VGG node (not on Q), D1 absent, at 20 ms with "
        "TX_KEY, PA_EN and Q high (the finding's case)",
        on, on, on, pk, pp, vcut="(time>20m)", permit=[(5e-3, 20e-3)],
        expect=dict(driver="on", vgg="under the dead zone"), faults=dict(RD1SER="1e12"))
    row("F6", "U1 output shorted to 3V3 (stuck high) and the backstop pulls Q at 20 ms",
        on, on, on, pk, pp, qcut="(time>20m)", permit=[(5e-3, 20e-3)],
        expect=dict(driver="on", vgg="under the dead zone"), faults=dict(RU1STK="1"))
    row("F7", "U1 output shorted to 3V3 (stuck high) and the monostable expires at 20 ms (the 10 s cutoff)",
        on, on, on, pk, pp, qexp="(time>20m)", permit=[(5e-3, 20e-3)],
        expect=dict(driver="on", vgg="under the dead zone"), faults=dict(RU1STK="1"))
    for i, r in enumerate(c, 1):
        r["case"] = i
    return c


def _tab(pts, scale):
    return "table(time," + ",".join(f"{t:.8g},{v * 1:.6g}" for t, v in pts) + f")*{scale}"


def _sel(rows, key, scale):
    expr = "0"
    for r in reversed(rows):
        expr = f"if(CASE=={r['case']},{_tab(r[key], scale)},{expr})"
    return expr


def gen_seq():
    rows = seq_cases()
    n = len(rows)
    s = ["* d18_seq.cir: D-18 gate D18-2B, power-up orders, brown-outs, single-line and single-component faults.\n",
         "* Generated by hardware/sim/tx-pa-permit/d18_run.py. The error amplifier is wound to the 5 V rail in every\n",
         "* case (worst for the clamp). Cases: see result.json.\n",
         f".step param CASE 1 {n} 1\n",
         ".param VBUSX=5.0 V33X=3.3 VTOP=-0.73 BFX=70 IE9=120u LS=1 TRS=0 TFA=1 ATOP=1\n"]
    for key, default in (("RUOPEN", "1m"), ("RPU1V", "10k"), ("RPU2V", "10k"), ("RQ2SH", "1e12"),
                         ("RQ3SH", "1e12"), ("RD1SER", "1m"), ("RU1STK", "1e12")):
        vals = []
        for r in rows:
            v = r["faults"].get(key, default)
            vals.append(f"{r['case']},{v}")
        s.append(f".param {key}=table(CASE,{','.join(vals)})\n")
    s.append(MODELS + SUPPLY.replace("BLDO ldo 0 V={VBUSX}", "BLDO ldo 0 V=VBUSX*" + _sel(rows, "bus", 1)))
    s.append("BV33 v33 0 V=V33X*" + _sel(rows, "v33", 1) + "\n")
    # GPIO high level follows the 3V3 rail (IOVDD); enable per case
    s.append(gpio("TK", "tk", _sel(rows, "en", 1), "V(v33)*" + _sel(rows, "tk", 1)))
    s.append(gpio("PE", "pe", _sel(rows, "en", 1), "V(v33)*" + _sel(rows, "pe", 1)))
    qexp = "0"
    for r in reversed(rows):
        qexp = f"if(CASE=={r['case']},{r['qexp']},{qexp})"
    s.append(monostable(qexp))
    s.append(and_gate(False))

    def cexp(key):
        e = "0"
        for r in reversed(rows):
            e = f"if(CASE=={r['case']},{r[key]},{e})"
        return e
    s.append(fixed_gate() + cutoffs_r1(cexp("qcut"), cexp("qvb"), cexp("vcut")) + GVA_LOAD
             + VGG_NODE.replace("{ENV}", "1"))
    s.append(SAVE)
    s.append(f".tran 0 {T_SEQ:g} 0 20u\n.options plotwinsize=0\n.end\n")
    return "d18_seq.cir", "".join(s), rows


# ------------------------------------------------------------------------------------------ run and read
def run_deck(name, text, run_id, rerun):
    rundir = RESULTS / run_id
    rundir.mkdir(parents=True, exist_ok=True)
    (HERE / name).write_text(text)
    if rerun:
        cmd = [str(WRAPPER), "-t", "1800", "-o", str(rundir), "-b", str(HERE / name)]
        p = subprocess.run(cmd, capture_output=True, text=True)
        (rundir / "wrapper.txt").write_text(p.stderr[-4000:])
        print(p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "(no wrapper output)")
        if p.returncode != 0:
            print(f"LTspice run failed ({p.returncode})", file=sys.stderr)
            sys.exit(2)
        shutil.copy(HERE / name, rundir / name)
    elif (HERE / name).read_bytes() != (rundir / name).read_bytes():
        print("replot refused: the generated deck differs from the deck of the run", file=sys.stderr)
        sys.exit(2)
    shutil.copy(Path(__file__), rundir / Path(__file__).name)
    return rundir


def read_steps(rundir, name):
    raw = RawRead(str(rundir / (Path(name).stem + ".raw")))
    steps = raw.get_steps()
    out = []
    names = ["V(tx5)", "V(gp)", "V(nb)", "V(bus)", "V(vgg)", "V(nc)", "V(y)", "V(tk)", "V(pe)", "V(q)",
             "V(v33)", "Id(M1)", "I(D1)"]
    for st in steps:
        t = np.abs(raw.get_trace("time").get_wave(st))
        d = {"t": t}
        for n in names:
            d[n] = raw.get_trace(n).get_wave(st)
        out.append(d)
    return out


def win(d, t0, t1):
    m = (d["t"] >= t0) & (d["t"] <= t1)
    return m


def first_after(d, t0, cond):
    idx = np.where((d["t"] >= t0) & cond)[0]
    return float(d["t"][idx[0]]) if len(idx) else float("nan")


# ------------------------------------------------------------------------------------------ criteria
CRIT = {
    "t_on_ms": dict(limit=0.25, sense="<=", text="driver supply within 50 mV of its source after the later of "
                    "PA_EN and TX_KEY (budget: 2 ms nominal lead, 0.5 ms in the interval-13 fallback; limit half "
                    "of the fallback lead)"),
    "clamp_release_ms": dict(limit=0.25, sense="<=", text="clamp gate at most 0.3 V after the later of PA_EN "
                             "and TX_KEY (before the ramp)"),
    "vgs_on_v": dict(limit=-4.0, sense="<=", text="P-FET VGS while permitted (RDS(on) is specified at -4.5 V; "
                     "-4.0 V keeps it at least 1.9 V beyond the -2.1 V threshold)"),
    "drop_mv": dict(limit=30.0, sense="<=", text="P-FET drop at the GVA-84+ current while permitted"),
    "inrush_a": dict(limit=11.0, sense="<=", text="P-FET peak current at turn-on (DMP3099L IDM 11 A, pulse <= "
                     "10 us)"),
    "bus_dip_mv": dict(limit=100.0, sense="<=", text="5 V bus dip at driver turn-on (Q, error amplifier and "
                       "monostables on the bus)"),
    "vgs_off_v": dict(limit=-0.3, sense=">=", text="P-FET VGS in the key-up window (at most 0.3 V, against the "
                      "lowest threshold magnitude 0.73 V, hot estimate)"),
    "vtx5_keyup_mv": dict(limit=50.0, sense="<=", text="driver supply in the key-up window (GVA-84+ draws no "
                          "current below about 3.1 V)"),
    "t_off_ms": dict(limit=1.0, sense="<=", text="driver supply below 0.1 V after TX_KEY falls"),
    "clamp_gate_keyup_v": dict(limit=4.0, sense=">=", text="clamp gate in the key-up window (RDS(on) specified "
                               "at 4.5 V; threshold at most 2.75 V)"),
    "vgg_keyup_mv": dict(limit=50.0, sense="<=", text="VGG in the key-up window, error amplifier wound to the rail "
                         "in half the cases (module dead zone to about 2.3 V)"),
    "pre_permit_off": dict(limit=0.05, sense="<=", text="driver supply (V) while only one of PA_EN and TX_KEY "
                           "is high (7 to 8 ms; 8 to 11 ms in the fallback): a single line does not power the "
                           "driver"),
}
for k in ISO_CASES:
    CRIT[f"keyup_dbm_{k}"] = dict(limit=REQ_TX_014_DBM, sense="<=",
                                  text=f"REQ-TX-014 level in the key-up window, {ISO_CASES[k]['name']}")


def ok(val, key):
    c = CRIT[key]
    return val <= c["limit"] if c["sense"] == "<=" else val >= c["limit"]


def analyse_keyup(steps, rows, asis=False):
    res = []
    for d, r in zip(steps, rows):
        fb = r.get("fb", 0)
        tpe = PA_EN_T_FB if fb else PA_EN_T
        trs = RAMP_T_FB if fb else RAMP_T
        tfa = trs + HOLD
        tkf = tfa + TFULL + 1e-3
        t_perm = max(tpe, TXK_T)
        t = d["t"]
        vtx, vnb, vgp, vnc, vgg, vbus = d["V(tx5)"], d["V(nb)"], d["V(gp)"], d["V(nc)"], d["V(vgg)"], d["V(bus)"]
        m = {}
        on_cond = vtx >= vnb - 0.05
        m["t_on_ms"] = (first_after(d, t_perm, on_cond) - t_perm) * 1e3
        m["clamp_release_ms"] = (first_after(d, t_perm, vnc <= 0.3) - t_perm) * 1e3
        hold = win(d, trs, tfa)
        m["vgs_on_v"] = float(np.max((vgp - vnb)[hold]))
        m["drop_mv"] = float(np.max((vnb - vtx)[hold])) * 1e3
        w_on = win(d, t_perm, t_perm + 0.2e-3)
        m["inrush_a"] = float(np.max(np.abs(d["Id(M1)"][w_on])))
        pre = win(d, t_perm - 0.5e-3, t_perm - 1e-6)
        m["bus_dip_mv"] = float(np.max(vbus[pre]) - np.min(vbus[w_on])) * 1e3
        ku = win(d, tkf + 2e-3, PA_EN_OFF - 1e-6)
        m["vgs_off_v"] = float(np.min((vgp - vnb)[ku]))
        m["vtx5_keyup_mv"] = float(np.max(vtx[ku])) * 1e3
        m["t_off_ms"] = (first_after(d, tkf, vtx <= 0.1) - tkf) * 1e3
        m["clamp_gate_keyup_v"] = float(np.min(vnc[ku]))
        m["vgg_keyup_mv"] = float(np.max(vgg[ku])) * 1e3
        pp = win(d, min(tpe, TXK_T) + 0.2e-3, t_perm - 1e-6)   # one line high, the other still low
        m["pre_permit_off"] = float(np.max(vtx[pp])) if np.any(pp) else 0.0
        wins = dict(lead=win(d, 1.0e-3, min(tpe, TXK_T) - 1e-6), one=pp, keyup=ku,
                    end=win(d, PA_EN_OFF + 0.3e-3, T_END))
        for k, c in ISO_CASES.items():
            lev = antenna_dbm(vtx, vgg, c)
            m[f"keyup_dbm_{k}"] = float(np.max(lev[ku]))
            for w, mk in wins.items():
                m[f"off_{w}_dbm_{k}"] = float(np.max(lev[mk])) if np.any(mk) else float("nan")
        m["vgg_top_v"] = float(np.max(vgg[hold]))
        passed = {k: bool(ok(m[k], k)) if not math.isnan(m[k]) else False for k in CRIT}
        res.append(dict(case=r["case"], label=r["label"], params={k: r[k] for k in r if k not in ("case", "label")},
                        metrics=m, passed=passed, _d=d))
    return res


def analyse_seq(steps, rows):
    res = []
    for d, r in zip(steps, rows):
        t = d["t"]
        vtx, vgg, vnc, vnb = d["V(tx5)"], d["V(vgg)"], d["V(nc)"], d["V(nb)"]
        perm = np.zeros_like(t, bool)
        for (a, b) in r["permit"]:
            perm |= (t >= a) & (t <= b)
        # settle allowance after each permit edge only (not after rail ramps)
        settle = np.zeros_like(t, bool)
        for (a, b) in r["permit"]:
            settle |= (t >= a) & (t <= a + 0.3e-3)
            settle |= (t >= b) & (t <= b + 1.0e-3)
        off = ~perm & ~settle
        onw = np.zeros_like(t, bool)
        for (a, b) in r["onwin"]:
            onw |= (t >= a + 0.3e-3) & (t <= b)
        bus_ok = d["V(bus)"] >= 4.0          # the clamp is fully driven only with the bus up (else see ramp)
        ramp = ~bus_ok & off
        m = dict(vtx5_off_max_v=float(np.max(vtx[off])),
                 vgg_off_max_v=float(np.max(vgg[off & bus_ok])) if np.any(off & bus_ok) else 0.0,
                 vgg_ramp_max_v=float(np.max(vgg[ramp])) if np.any(ramp) else 0.0,
                 vtx5_on_min_margin_v=float(np.min((vtx - vnb)[onw])) if np.any(onw) else None,
                 clamp_gate_on_max_v=float(np.max(vnc[onw])) if np.any(onw) else None,
                 vtx5_end_v=float(vtx[-1]), vgg_end_v=float(vgg[-1]))
        # revision 1: antenna level (CLK1 assumed running, relay in transmit) at the end of the case and, for the
        # design cases, the highest level while not permitted with the bus up
        for k, cse in ISO_CASES.items():
            m[f"level_end_dbm_{k}"] = float(antenna_dbm(np.array([vtx[-1]]), np.array([vgg[-1]]), cse)[0])
            sel = off & bus_ok
            m[f"level_off_max_dbm_{k}"] = float(np.max(antenna_dbm(vtx[sel], vgg[sel], cse))) if np.any(sel) else None
        # the D1 current trace rings sample to sample around its value (trapezoidal integration of the diode's
        # 2 pF with the node voltages steady), so the metric is its mean over the last 5 ms
        m["d1_current_end_ma"] = float(np.mean(d["I(D1)"][t >= t[-1] - 5e-3])) * 1e3
        m["q_end_v"] = float(d["V(q)"][-1])
        state_driver = "on" if m["vtx5_end_v"] > 2.5 else "off"
        state_clamp = "on" if m["vgg_end_v"] < 0.3 else "off"
        state_vgg = ("clamped" if m["vgg_end_v"] < 0.3 else
                     "under the dead zone" if m["vgg_end_v"] <= 2.0 else "free")
        if r["expect"]:
            exp = r["expect"]
            got = {}
            if "driver" in exp:
                got["driver"] = state_driver
            if "driver_after_permit" in exp:
                got["driver_after_permit"] = "on (P-FET gate holds its charge)" if state_driver == "on" else "off"
            if "clamp" in exp:
                got["clamp"] = state_clamp
            if "vgg" in exp:
                got["vgg"] = state_vgg
            passed = {"as_expected": got == exp}
            m["state"] = got
        else:
            # off: driver supply at most 0.1 V whenever not permitted; VGG at most 0.1 V with the bus up, and at
            # most 2.0 V while a rail ramps (under the module's dead zone to about 2.3 V; driver unpowered)
            passed = {"off_when_not_permitted": m["vtx5_off_max_v"] <= 0.1 and m["vgg_off_max_v"] <= 0.1
                      and m["vgg_ramp_max_v"] <= 2.0}
            if r["permit"]:
                passed["on_when_permitted"] = (m["vtx5_on_min_margin_v"] >= -0.05 and m["clamp_gate_on_max_v"] <= 0.3)
        res.append(dict(case=r["case"], tag=r["tag"], desc=r["desc"], permit=r["permit"], expect=r["expect"],
                        faults=r["faults"], metrics=m, passed=passed, _d=d))
    return res


# ------------------------------------------------------------------------------------------ plots
def plot_keyup(rundir, res, fname="keyup_timeline.png", picks=None, title=""):
    picks = picks or [res[0], res[-1]]
    fig, axs = plt.subplots(5, 1, figsize=(11, 13), sharex=True)
    for i, r in enumerate(picks):
        d = r["_d"]
        t = d["t"] * 1e3
        col = f"C{i}"
        lab = f"case {r['case']}: {r['label']}"
        axs[0].plot(t, d["V(tk)"] + 0.04 * i, lw=1, color=col)
        axs[0].plot(t, d["V(pe)"] + 0.04 * i + 0.02, lw=1, ls="--", color=col)
        axs[1].plot(t, d["V(tx5)"], lw=1.2, label=lab, color=col)
        axs[2].plot(t, d["V(gp)"] - d["V(nb)"], lw=1.2, color=col)
        axs[3].plot(t, d["V(vgg)"], lw=1.2, color=col)
        axs[3].plot(t, d["V(nc)"], lw=0.8, ls=":", color=col)
        for k, ls in (("L1", "-"), ("L4", "--")):
            axs[4].plot(t, antenna_dbm(d["V(tx5)"], d["V(vgg)"], ISO_CASES[k]), lw=1.1, ls=ls, color=col)
    axs[0].set_ylabel("TX_KEY (solid)\nPA_EN (dashed) V")
    axs[1].set_ylabel("driver supply\nTX5 (V)")
    axs[1].legend(fontsize=7, loc="upper right")
    axs[2].set_ylabel("P-FET VGS (V)")
    axs[2].axhline(-0.73, color="r", lw=0.8, ls=":")
    axs[2].text(61, -0.9, "lowest |Vth| (hot) 0.73 V", fontsize=7, color="r", ha="right")
    axs[3].set_ylabel("VGG (solid)\nclamp gate (dotted) V")
    axs[4].set_ylabel("antenna (dBm)")
    axs[4].axhline(REQ_TX_014_DBM, color="r", lw=1)
    axs[4].text(64, REQ_TX_014_DBM + 1.5, "REQ-TX-014 -30 dBm", color="r", fontsize=8, ha="right")
    axs[4].set_ylim(-80, 45)
    axs[4].text(1, -77, "solid: isolation case L1 (estimates); dashed: L4 (drive bound, GVA-84+ 0 dB).\nThe element top "
                "is an open-loop VGG ramp to 2.75 V (about 5 W), or the rail when the loop is wound; not a keying "
                "result (keying-ts012.md)", fontsize=6.5)
    axs[4].set_xlabel("time from the changeover t0 (ms)")
    for a in axs:
        a.grid(alpha=0.3)
    fig.suptitle(title or "D-18 gate D18-2B: one element and the key-up window with PA_EN asserted (A5)")
    fig.tight_layout()
    fig.savefig(rundir / fname, dpi=110)
    plt.close(fig)


def plot_keyup_zoom(rundir, res):
    fig, axs = plt.subplots(2, 2, figsize=(12, 7))
    for r in res:
        d = r["_d"]
        fb = r["params"]["fb"]
        tpe = PA_EN_T_FB if fb else PA_EN_T
        t_perm = max(tpe, TXK_T)
        tkf = (RAMP_T_FB if fb else RAMP_T) + HOLD + TFULL + 1e-3
        t = d["t"]
        a = (t >= t_perm - 0.05e-3) & (t <= t_perm + 0.3e-3)
        col = "C1" if fb else "C0"
        axs[0, 0].plot((t[a] - t_perm) * 1e6, d["V(tx5)"][a], lw=0.7, color=col)
        axs[0, 1].plot((t[a] - t_perm) * 1e6, d["Id(M1)"][a] * -1, lw=0.7, color=col)
        b = (t >= tkf - 0.05e-3) & (t <= tkf + 1.2e-3)
        axs[1, 0].plot((t[b] - tkf) * 1e3, d["V(tx5)"][b], lw=0.7, color=col)
        axs[1, 1].plot((t[b] - tkf) * 1e3, d["V(vgg)"][b], lw=0.7, color=col)
    axs[0, 0].set_title("turn-on: driver supply (all 52 cases)", fontsize=9)
    axs[0, 0].set_xlabel("us after the later of PA_EN and TX_KEY")
    axs[0, 0].axvline(250, color="r", lw=0.8)
    axs[0, 0].text(245, 0.5, "limit 0.25 ms", color="r", fontsize=7, ha="right")
    axs[0, 1].set_title("turn-on: P-FET current (A)", fontsize=9)
    axs[0, 1].set_xlabel("us after the later of PA_EN and TX_KEY")
    axs[1, 0].set_title("key-up: driver supply after TX_KEY falls", fontsize=9)
    axs[1, 0].set_xlabel("ms after TX_KEY falls")
    axs[1, 0].axvline(1.0, color="r", lw=0.8)
    axs[1, 0].axhline(0.1, color="r", lw=0.8, ls=":")
    axs[1, 1].set_title("key-up: VGG after TX_KEY falls (loop wound to the rail in half the cases)", fontsize=9)
    axs[1, 1].set_xlabel("ms after TX_KEY falls")
    for a in axs.flat:
        a.grid(alpha=0.3)
    axs[0, 0].plot([], [], color="C0", label="TS-012 sequence")
    axs[0, 0].plot([], [], color="C1", label="interval-13 fallback")
    axs[0, 0].legend(fontsize=7)
    fig.suptitle("D18-2B switching edges over every key-up corner")
    fig.tight_layout()
    fig.savefig(rundir / "keyup_edges.png", dpi=110)
    plt.close(fig)


def plot_metrics(rundir, res, keys, fname, title):
    n = len(keys)
    fig, axs = plt.subplots((n + 2) // 3, 3, figsize=(13, 3.0 * ((n + 2) // 3)))
    axs = np.atleast_1d(axs).flat
    for ax, k in zip(axs, keys):
        vals = [r["metrics"][k] for r in res]
        cols = ["C2" if r["passed"].get(k, True) else "C3" for r in res]
        ax.scatter([r["case"] for r in res], vals, c=cols, s=12)
        ax.axhline(CRIT[k]["limit"], color="r", lw=1)
        ax.set_title(f"{k} (limit {CRIT[k]['sense']} {CRIT[k]['limit']:g})", fontsize=8)
        ax.set_xlabel("case", fontsize=7)
        ax.grid(alpha=0.3)
    for ax in list(axs):
        ax.axis("off")
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(rundir / fname, dpi=110)
    plt.close(fig)


def plot_asis(rundir, res):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))
    for vb, mk in ((4.75, "v"), (5.0, "o"), (5.25, "^")):
        for v33, col in ((3.0, "C0"), (3.3, "C1"), (3.6, "C2")):
            sel = [r for r in res if r["params"]["vbus"] == vb and r["params"]["v33"] == v33]
            x = [r["params"]["vtop"] for r in sel]
            axs[0].plot(x, [r["metrics"]["vtx5_keyup_mv"] / 1e3 for r in sel], marker=mk, color=col, lw=0.8,
                        label=f"bus {vb} V, NAND {v33} V")
            axs[1].plot(x, [r["metrics"]["keyup_dbm_L1"] for r in sel], marker=mk, color=col, lw=0.8)
    axs[0].set_xlabel("DMP3099L VGS(th) (V): datasheet -1.0 to -2.1, hot estimate -0.73")
    axs[0].set_ylabel("driver supply in the key-up window (V)")
    axs[0].axhline(3.14, color="k", lw=0.6, ls=":")
    axs[0].text(-2.05, 3.25, "GVA-84+ conducts above about 3.1 V (E)", fontsize=7)
    axs[0].legend(fontsize=6)
    axs[1].set_xlabel("DMP3099L VGS(th) (V)")
    axs[1].set_ylabel("key-up antenna level (dBm), isolation case L1")
    axs[1].axhline(REQ_TX_014_DBM, color="r", lw=1)
    axs[1].text(-2.05, REQ_TX_014_DBM + 1, "REQ-TX-014 -30 dBm", color="r", fontsize=7)
    for a in axs:
        a.grid(alpha=0.3)
        a.invert_xaxis()
    fig.suptitle("D-18 as TS-012 revisions 7 and 8 draw it (3.3 V NAND on the 5 V P-FET gate): key-up with PA_EN asserted")
    fig.tight_layout()
    fig.savefig(rundir / "asis_keyup.png", dpi=110)
    plt.close(fig)


def plot_seq(rundir, res):
    n = len(res)
    fig, axs = plt.subplots((n + 2) // 3, 3, figsize=(14, 2.6 * ((n + 2) // 3)), sharex=True)
    for ax, r in zip(axs.flat, res):
        d = r["_d"]
        t = d["t"] * 1e3
        ax.plot(t, d["V(bus)"], lw=0.8, color="0.6", label="5 V bus")
        ax.plot(t, d["V(v33)"], lw=0.8, color="0.3", ls="--", label="3V3")
        ax.plot(t, d["V(tx5)"], lw=1.3, color="C0", label="driver supply")
        ax.plot(t, d["V(vgg)"], lw=1.3, color="C3", label="VGG")
        ax.plot(t, d["V(y)"] * 0.5 - 1.2, lw=0.8, color="C2", label="U1 out (x0.5, -1.2)")
        for (a, b) in r["permit"]:
            ax.axvspan(a * 1e3, b * 1e3, color="C2", alpha=0.08)
        verdict = "PASS" if all(r["passed"].values()) else "FAIL"
        ax.set_title(f"{r['tag']}: {verdict}" + (" (fault case, as expected)" if r["expect"] and verdict == "PASS"
                                                   else ""), fontsize=8)
        ax.text(0.5, 5.6, r["desc"][:95] + ("..." if len(r["desc"]) > 95 else ""), fontsize=5.5)
        ax.set_ylim(-1.5, 6.4)
        ax.grid(alpha=0.3)
    for ax in list(axs.flat)[n:]:
        ax.axis("off")
    axs.flat[0].legend(fontsize=5.5, loc="center right")
    for ax in axs[-1]:
        ax.set_xlabel("time (ms)")
    fig.suptitle("D18-2B power-up orders, brown-outs, single-line and single-component faults "
                 "(error amplifier wound to the rail; green: permit window)")
    fig.tight_layout()
    fig.savefig(rundir / "seq_cases.png", dpi=110)
    plt.close(fig)


def req183_table(res):
    """Worst level over the corners in each OFF_STATES window, per isolation case, against REQ-SYS-183."""
    states = {}
    for w in OFF_STATES:
        row = {}
        for k in ISO_CASES:
            vals = [r["metrics"][f"off_{w}_dbm_{k}"] for r in res if not math.isnan(r["metrics"][f"off_{w}_dbm_{k}"])]
            worst = max(vals)
            row[k] = dict(worst_dbm=worst, margin_db=REQ_SYS_183_DBM - worst,
                          verdict="PASS" if worst <= REQ_SYS_183_DBM else "FAIL", n_cases=len(vals))
        states[w] = row
    as_exp = all(states[w][k]["verdict"] == REQ183_EXPECTED[k] for w in states for k in ISO_CASES)
    return dict(limit_dbm=REQ_SYS_183_DBM, state_text=OFF_STATES, expected=REQ183_EXPECTED, states=states,
                as_expected=as_exp)


def plot_off_states(rundir, r183):
    fig, ax = plt.subplots(figsize=(12, 5.5))
    names = list(ISO_CASES)
    ws = list(OFF_STATES)
    bw = 0.2
    for j, k in enumerate(names):
        xs = np.arange(len(ws)) + (j - 1.5) * bw
        vals = [r183["states"][w][k]["worst_dbm"] for w in ws]
        ax.bar(xs, np.array(vals) + 100, bottom=-100, width=bw * 0.9, color=f"C{j}", alpha=0.8,
               label=f"{k}: {ISO_CASES[k]['name']}")
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.0, f"{v:.1f}\n({REQ_SYS_183_DBM - v:+.1f})", ha="center", fontsize=6.5)
    ax.axhline(REQ_SYS_183_DBM, color="m", lw=1.3)
    ax.text(3.55, REQ_SYS_183_DBM + 1, "REQ-SYS-183 -57 dBm\n(RF off of REQ-SYS-120)", color="m", fontsize=7,
            ha="right")
    ax.axhline(REQ_TX_014_DBM, color="r", lw=1, ls="--")
    ax.text(3.55, REQ_TX_014_DBM + 1, "REQ-TX-014 -30 dBm (keyup state only)", color="r", fontsize=7, ha="right")
    ax.set_xticks(np.arange(len(ws)))
    ax.set_xticklabels(["\n".join(_wrap(OFF_STATES[w], 30)) for w in ws], fontsize=7)
    ax.set_ylabel("worst antenna level over the 52 corners (dBm); (margin to -57 dBm, dB)")
    ax.set_ylim(-100, -10)
    ax.grid(alpha=0.3, axis="y")
    ax.legend(fontsize=6.5, loc="upper left")
    ax.set_title("A5 with D18-2B: antenna level in the states with fewer than both REQ-SYS-120 conditions "
                 "(CLK1 running, relay in transmit)", fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "off_states.png", dpi=110)
    plt.close(fig)


def plot_cutoff_levels(rundir, res):
    tags = ["L1", "C1", "C3", "C4", "A1", "F6", "F7"]
    sel = [r for t in tags for r in res if r["tag"] == t]
    fig, ax = plt.subplots(figsize=(12, 5.5))
    names = list(ISO_CASES)
    bw = 0.2
    for j, k in enumerate(names):
        xs = np.arange(len(sel)) + (j - 1.5) * bw
        vals = [r["metrics"][f"level_end_dbm_{k}"] for r in sel]
        ax.bar(xs, np.array(vals) + 100, bottom=-100, width=bw * 0.9, color=f"C{j}", alpha=0.8,
               label=f"{k}: {ISO_CASES[k]['name']}")
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.0, f"{v:.1f}", ha="center", fontsize=6)
    ax.axhline(REQ_SYS_183_DBM, color="m", lw=1.3)
    ax.text(len(sel) - 0.45, REQ_SYS_183_DBM + 1, "REQ-SYS-183 -57 dBm", color="m", fontsize=7, ha="right")
    ax.set_xticks(np.arange(len(sel)))
    ax.set_xticklabels([f"{r['tag']}\n" + "\n".join(_wrap(r["desc"], 26)[:5]) for r in sel], fontsize=5.8)
    ax.set_ylabel("antenna level at the end of the case (dBm)\nCLK1 running, relay in transmit")
    ax.set_ylim(-100, 5)
    ax.grid(alpha=0.3, axis="y")
    ax.legend(fontsize=6.5, loc="upper left")
    ax.set_title("After a cutoff with TX_KEY and PA_EN high: fixed design (L1, C1, C3, C4), as drawn in TS-012 (A1), "
                 "U1 stuck high (F6, F7)", fontsize=9.5)
    fig.tight_layout()
    fig.savefig(rundir / "cutoff_levels.png", dpi=110)
    plt.close(fig)


def plot_level_cases(rundir, keyres):
    fig, ax = plt.subplots(figsize=(11, 5))
    names = list(ISO_CASES)
    worst = [max(r["metrics"][f"keyup_dbm_{k}"] for r in keyres) for k in names]
    best = [min(r["metrics"][f"keyup_dbm_{k}"] for r in keyres) for k in names]
    x = np.arange(len(names))
    ax.bar(x, np.array(worst) - (-100), bottom=-100, color="C0", alpha=0.7, width=0.5)
    for i, (w, b) in enumerate(zip(worst, best)):
        ax.text(i, w + 1.5, f"{w:.1f} dBm\n(margin {REQ_TX_014_DBM - w:.1f} dB)", ha="center", fontsize=8)
    ax.axhline(REQ_TX_014_DBM, color="r", lw=1.2)
    ax.text(-0.45, REQ_TX_014_DBM + 1, "REQ-TX-014 -30 dBm", color="r", fontsize=8, ha="left")
    ax.axhline(REQ_SYS_183_DBM, color="m", lw=1, ls="--")
    ax.text(1.5, REQ_SYS_183_DBM - 3.5, "REQ-SYS-183 -57 dBm: the RF-off level of REQ-SYS-120 in this same state "
            "(off_states.png)", color="m", fontsize=7, ha="center")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{k}\n" + "\n".join(_wrap(ISO_CASES[k]["name"], 34)) for k in names], fontsize=7)
    ax.set_ylabel("steady key-up level at the antenna (dBm), worst of 52 corners")
    ax.set_ylim(-100, 0)
    ax.grid(alpha=0.3, axis="y")
    ax.set_title("A5 key-up with the D18-2B gate: TX_KEY low, PA_EN asserted, CLK1 running")
    fig.tight_layout()
    fig.savefig(rundir / "level_cases.png", dpi=110)
    plt.close(fig)


def _wrap(s, n):
    out, line = [], ""
    for w in s.split():
        if len(line) + len(w) + 1 > n:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    out.append(line)
    return out


# ------------------------------------------------------------------------------------------ stages
def dump(rundir, run_id, name, res, extra):
    clean = [{k: v for k, v in r.items() if k != "_d"} for r in res]
    allpass = {k: all(r["passed"].get(k, True) for r in clean) for k in clean[0]["passed"]}
    fails = {k: [r["case"] for r in clean if not r["passed"].get(k, True)] for k in clean[0]["passed"]}
    out = dict(run_id=run_id, deck=name, script=Path(__file__).name, model=MODEL, criteria=CRIT,
               isolation_cases=ISO_CASES, all_cases_pass=allpass, failing_cases=fails, cases=clean, **extra)
    (rundir / "result.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    keys = list(clean[0]["metrics"].keys())
    with open(rundir / "result.csv", "w") as f:
        f.write("case," + ",".join(keys) + ",all_pass\n")
        for r in clean:
            vals = []
            for k in keys:
                v = r["metrics"][k]
                vals.append(f"{v:.6g}" if isinstance(v, (int, float)) and v is not None else json.dumps(v))
            f.write(f"{r['case']}," + ",".join(vals) + f",{all(r['passed'].values())}\n")
    return allpass, fails


def stage_keyup(rerun=True):
    name, text, rows = gen_keyup()
    run_id = f"{DATE}-{REV}-keyup"
    rundir = run_deck(name, text, run_id, rerun)
    res = analyse_keyup(read_steps(rundir, name), rows)
    allpass, fails = dump(rundir, run_id, name, res, dict(
        derived=dict(p_gva_in_sot_dbm=P_GVA_IN_SOT, p_gva_in_bound_dbm=P_GVA_IN_BOUND, rf_est_ohm=RF_EST,
                     iso_gva_est_db=ISO_GVA_EST,
                     breakeven_iso_sum_db={"sot": P_GVA_IN_SOT - OUT_PAD_DB - LPF_RELAY_DB - REQ_TX_014_DBM,
                                           "bound": P_GVA_IN_BOUND - OUT_PAD_DB - LPF_RELAY_DB - REQ_TX_014_DBM})))
    fbw = [r for r in res if r["params"]["fb"]]
    wound = [r for r in res if r["params"]["ls"] and r["params"]["vbus"] == 5.25 and r["params"]["vtop"] == -0.73]
    plot_keyup(rundir, res, picks=[res[8], wound[0], fbw[-1]])
    plot_keyup_zoom(rundir, res)
    plot_metrics(rundir, res, [k for k in CRIT if not k.startswith("keyup_dbm")], "keyup_metrics.png",
                 "D18-2B key-up deck: every criterion over the 52 corners (green pass, red fail)")
    plot_level_cases(rundir, res)
    r183 = req183_table(res)
    plot_off_states(rundir, r183)
    rj = json.loads((rundir / "result.json").read_text())
    rj["req_sys_183_off_states"] = r183
    (rundir / "result.json").write_text(json.dumps(rj, indent=2, default=float) + "\n")
    bad = [k for k, v in allpass.items() if not v]
    print(f"{run_id}: {len(res)} cases; criteria failing: {bad or 'none'}")
    for w, row in r183["states"].items():
        print(f"  REQ-SYS-183 {w}: " + ", ".join(f"{k} {v['worst_dbm']:.1f} dBm ({v['margin_db']:+.1f} dB, "
                                                   f"{v['verdict']})" for k, v in row.items()))
    print(f"  REQ-SYS-183 verdicts as the record states: {r183['as_expected']}")
    if not r183["as_expected"]:
        bad.append("req_sys_183_expected_states")
    for k in ISO_CASES:
        w = max(r["metrics"][f"keyup_dbm_{k}"] for r in res)
        print(f"  key-up {k}: worst {w:.1f} dBm (margin {REQ_TX_014_DBM - w:.1f} dB)")
    for k in ("t_on_ms", "clamp_release_ms", "vgs_on_v", "drop_mv", "inrush_a", "bus_dip_mv", "vgs_off_v",
              "vtx5_keyup_mv", "t_off_ms", "clamp_gate_keyup_v", "vgg_keyup_mv", "pre_permit_off"):
        vals = [r["metrics"][k] for r in res]
        print(f"  {k}: {min(vals):.4g} .. {max(vals):.4g}")
    return 3 if bad else 0


def stage_asis(rerun=True):
    name, text, rows = gen_asis()
    run_id = f"{DATE}-{REV}-asis"
    rundir = run_deck(name, text, run_id, rerun)
    res = analyse_keyup(read_steps(rundir, name), [dict(r, fb=0, label=r["label"]) for r in rows], asis=True)
    # expected (finding-9 (a)): the P-FET is not held off in some cases, and REQ-TX-014 then fails
    n_on = sum(r["metrics"]["vtx5_keyup_mv"] > 3140 for r in res)
    n_fail = sum(r["metrics"]["keyup_dbm_L1"] > REQ_TX_014_DBM for r in res)
    expected = dict(driver_not_off_in_some_cases=n_on > 0, req_tx_014_fails_in_some_cases=n_fail > 0)
    dump(rundir, run_id, name, res, dict(expected_defect=expected, n_driver_powered=n_on, n_req_tx_014_fail=n_fail))
    plot_asis(rundir, res)
    plot_keyup(rundir, res, fname="asis_timeline.png", picks=[r for r in res if r["params"]["vbus"] == 5.25 and
                                                               r["params"]["v33"] == 3.0][:4],
               title="As drawn in TS-012 revisions 7 and 8: 3.3 V NAND on the P-FET gate (VBUS 5.25 V, NAND 3.0 V)")
    print(f"{run_id}: {len(res)} cases; driver powered at key-up in {n_on}; REQ-TX-014 (L1) fails in {n_fail}")
    return 0 if all(expected.values()) else 3


def stage_seq(rerun=True):
    name, text, rows = gen_seq()
    run_id = f"{DATE}-{REV}-seq"
    rundir = run_deck(name, text, run_id, rerun)
    res = analyse_seq(read_steps(rundir, name), rows)
    allpass, fails = dump(rundir, run_id, name, res, {})
    plot_seq(rundir, res)
    plot_cutoff_levels(rundir, res)
    bad = [r["tag"] for r in res if not all(r["passed"].values())]
    for r in res:
        print(f"  {r['tag']}: {'PASS' if all(r['passed'].values()) else 'FAIL'} {r['metrics']}")
    print(f"{run_id}: {len(res)} cases; not as required: {bad or 'none'}")
    return 3 if bad else 0


def static_checks():
    """Datasheet-limit arithmetic of the D18-2B interface (record section 5.2). Each row: value, limit, margin,
    pass. Voltages in V, currents in A."""
    rows = []

    def add(name, value, limit, sense, basis):
        margin = (limit - value) if sense == "<=" else (value - limit)
        rows.append(dict(check=name, value=value, limit=limit, sense=sense, margin=margin, passed=margin >= 0,
                         basis=basis))

    vih, vil = MODEL["74lvc1g11"]["vih"], MODEL["74lvc1g11"]["vil"]
    add("GPIO high at U1 input (RP2350 VOH min)", 2.62, vih, ">=", "RP2350 Table 1436 VOH 2.62 V; 74LVC1G11 VIH 2.0 V")
    add("GPIO driven low at U1 input (RP2350 VOL max)", 0.5, vil, "<=", "VOL 0.5 V; VIL 0.8 V")
    add("GPIO high impedance (reset, boot): 4.7 k pull-down x E9 leakage 120 uA", 4.7e3 * 120e-6, vil, "<=",
        "RP2350-E9 about 120 uA (typical, A2 stepping); break-even leakage 170 uA")
    add("Q high at U1 input: 5 V bus min less 10 k x (LM393 IOH 20 nA + U1 II 1 uA)", 4.75 - 10e3 * 1.02e-6, vih, ">=",
        "LM2940 4.75 V; LM393 IOH-LKG 20 nA max at 5 V; 74LVC1G11 II +/-1 uA")
    add("Q high at U1 input does not exceed VI max (5 V bus max)", 5.25, MODEL["74lvc1g11"]["vi_max"], "<=",
        "74LVC1G11 VI 0 to 5.5 V at any VCC (5 V tolerant input, IOFF at VCC 0)")
    add("Q low at U1 input (LM393 VOL max, full range, at 4 mA; here 0.53 mA)", 0.7, vil, "<=", "TI SLCS005AH")
    voh = 2.3   # 74LVC1G11 VOH min at VCC 3.0 V and 24 mA (the 0.5 mA load is lighter)
    vbe = 0.85  # 2N3904 VBE(sat) max at 10 mA / 1 mA (D: onsemi 2N3903/D Rev. 9)
    ib = (voh - vbe) / 10e3 - vbe / 100e3
    add("2N3904 base current, U1 high at its guaranteed minimum", ib, 0.1e-3, ">=", "(2.3 - 0.85) / 10 k - 0.85 / 100 k")
    ic_p = (5.25 - 0.0) / 11e3
    ic_c = 5.25 / 10e3
    add("Forced beta, branch P (collector current / base current)", ic_p / ib, 40.0, "<=",
        "2N3904 hFE min 40 at 0.1 mA, 70 at 1 mA (onsemi 2N3903/D Rev. 9)")
    add("Forced beta, branch C", ic_c / ib, 40.0, "<=", "as above")
    vce = 0.2
    add("P-FET VGS permitted, 5 V bus 4.75 V less the bead drop (magnitude)", (4.75 - 0.03 - vce) * 10 / 11, 4.0, ">=",
        "10 k / 1 k divider from the 2N3904 VCE(sat) 0.2 V; DMP3099L RDS(on) 99 mohm specified at -4.5 V")
    add("P-FET VGS not permitted: 10 k x 2N3904 collector leakage (ICEX 50 nA max at 25 C, x 100 hot, E)",
        10e3 * 5e-6, 0.73, "<=",
        "DMP3099L |VGS(th)| min 1.0 V at 25 C, 0.73 V at 125 C (Figure 7 slope, DD/E)")
    add("Driver node not permitted: 2.2 k bleed x DMP3099L IDSS (800 nA at 25 C x 64 for +60 K, E)",
        2.2e3 * 0.8e-6 * 64, 3.14, "<=", "GVA-84+ conducts above about 3.1 V (E)")
    add("Clamp gate not permitted: 5 V bus min less 10 k x (2N3904 5 uA hot + 2N7002 IGSS 0.1 uA)",
        4.75 - 10e3 * 5.1e-6, 4.5, ">=", "2N7002 RDS(on) 5.3 ohm max specified at 4.5 V")
    add("Clamp gate permitted: 2N3904 VCE(sat) max against the 2N7002 VGS(th) min at 150 C", 0.2, 0.6, "<=",
        "Nexperia 2N7002 VGS(th) 0.6 V min at 150 C")
    r_on_hot = 5.3 * 9.25 / 5.0
    add("VGG clamped, error amplifier at 5.25 V, 2N7002 RDS(on) at 150 C (scaled from the 10 V ratio)",
        5.25 * r_on_hot / (2.7e3 + r_on_hot), 0.05, "<=", "module dead zone to about 2.3 V")
    # revision 1: the shared Q node
    i_d1_hot = MODEL["1n5711w"]["ir_na_50v"] * 1e-9 * 64
    i_leak_q = 4 * 20e-9 + 10e-6 + 1e-6 + i_d1_hot   # 4 LM393 outputs, VBUS open drain hot, U1 II, D1 hot
    add("Rev 1: Q high with every cutoff off: 4.75 V less 10 k x (4 LM393 x 20 nA + VBUS open drain 10 uA hot + U1 "
        "1 uA + D1 12.8 uA hot)", 4.75 - 10e3 * i_leak_q, vih, ">=",
        "LM393 IOH-LKG 20 nA; 2N7002 IDSS 10 uA at 150 C; 1N5711W IR 200 nA at 50 V x 64 (E)")
    add("Rev 1: Q low, one LM393 cutoff on (VOL max full range at 4 mA)", 0.7, vil, "<=",
        "TI SLCS005AH; load 0.53 mA from the pull-up, D1 not conducting while U1 clamps VGG")
    vgg_u1 = 1.1   # iterate VGG with U1 stuck high: amplifier at 5.25 V through 2.7 k, 5.1 k to ground, D1 to Q
    for _ in range(50):
        i_d = (5.25 - vgg_u1) / 2.7e3 - vgg_u1 / 5.1e3
        vf = 1.05 * 0.02585 * math.log(i_d / 1.07e-9 + 1) + i_d * 36.9
        vgg_u1 = 0.7 + vf
    add("Rev 1: LM393 sink current with U1 stuck high (pull-up + D1) within the 4 mA VOL test point",
        0.525e-3 + i_d, 4e-3, "<=", "VOL 0.7 V max is specified at 4 mA")
    add("Rev 1: VGG through D1 with U1 stuck high, amplifier at 5.25 V (VOL 0.7 V + VF max model)", vgg_u1, 2.0, "<=",
        "module dead zone to about 2.3 V; 1N5711W VF 0.41 V at 1 mA, 1.00 V at 15 mA (maximum-VF fit)")
    add("Rev 1: Q low, VBUS inhibit on (open drain 5.3 ohm x (pull-up + D1 current))", 5.3 * (0.525e-3 + i_d), vil,
        "<=", "2N7002-class open drain (E, part set by the TS-005 remnant)")
    add("Rev 1: VGG raised by D1 hot leakage while clamped (12.8 uA x 9.8 ohm)", i_d1_hot * r_on_hot, 0.05, "<=",
        "key-up VGG criterion 50 mV")
    return rows


def _delta_rev0(k):
    """Largest change of each revision 0 key-up metric in the revision 1 run (D1 and the cutoff pulls added)."""
    k0 = json.loads((RESULTS / f"{DATE}-d18-keyup" / "result.json").read_text())
    out = {}
    for m in k0["cases"][0]["metrics"]:
        out[m] = max(abs(c1["metrics"][m] - c0["metrics"][m]) for c0, c1 in zip(k0["cases"], k["cases"]))
    return out


def stage_summary():
    run_id = f"{DATE}-{REV}-summary"
    rundir = RESULTS / run_id
    rundir.mkdir(parents=True, exist_ok=True)
    k = json.loads((RESULTS / f"{DATE}-{REV}-keyup" / "result.json").read_text())
    a = json.loads((RESULTS / ASIS_RUN / "result.json").read_text())
    s = json.loads((RESULTS / f"{DATE}-{REV}-seq" / "result.json").read_text())
    lev = {c: dict(name=ISO_CASES[c]["name"], pin_dbm=ISO_CASES[c]["pin"], iso_gva_db=ISO_CASES[c]["iso_g"],
                   iso_mod_db=ISO_CASES[c]["iso_m"],
                   steady_analytic_dbm=ISO_CASES[c]["pin"] - ISO_CASES[c]["iso_g"] - OUT_PAD_DB - ISO_CASES[c]["iso_m"]
                   - LPF_RELAY_DB,
                   worst_sim_dbm=max(r["metrics"][f"keyup_dbm_{c}"] for r in k["cases"]))
           for c in ISO_CASES}
    out = dict(run_id=run_id, keyup_all_pass=k["all_cases_pass"], keyup_failing=k["failing_cases"],
               asis_expected_defect=a["expected_defect"], asis_n_driver_powered=a["n_driver_powered"],
               asis_n_req_tx_014_fail=a["n_req_tx_014_fail"], asis_cases=len(a["cases"]),
               seq=[dict(tag=c["tag"], passed=c["passed"], state=c["metrics"].get("state")) for c in s["cases"]],
               levels=lev, derived=k["derived"],
               req_sys_183_margin_db={c: REQ_SYS_183_DBM - lev[c]["steady_analytic_dbm"] for c in lev},
               req_sys_183_off_states=k["req_sys_183_off_states"],
               seq_cutoff_levels={c["tag"]: {kk: c["metrics"][f"level_end_dbm_{kk}"] for kk in ISO_CASES}
                                  for c in s["cases"]},
               asis_run=ASIS_RUN,
               keyup_max_abs_delta_vs_rev0=_delta_rev0(k),
               static_checks=static_checks())
    (rundir / "summary.json").write_text(json.dumps(out, indent=2, default=float) + "\n")
    shutil.copy(Path(__file__), rundir / Path(__file__).name)
    for c, v in lev.items():
        print(f"  {c}: analytic {v['steady_analytic_dbm']:.1f} dBm, simulated worst {v['worst_sim_dbm']:.1f} dBm")
    print(f"  break-even isolation sum (GVA-84+ unpowered + module VGG-off): {k['derived']['breakeven_iso_sum_db']}")
    for r in out["static_checks"]:
        print(f"  static: {r['check']}: {r['value']:.4g} {r['sense']} {r['limit']:g} "
              f"({'PASS' if r['passed'] else 'FAIL'}, margin {r['margin']:.3g})")
    ok_all = all(k["all_cases_pass"].values()) and all(a["expected_defect"].values()) and \
        all(all(c["passed"].values()) for c in s["cases"]) and all(r["passed"] for r in out["static_checks"]) and \
        k["req_sys_183_off_states"]["as_expected"]
    print(f"{run_id}: {'every criterion as required' if ok_all else 'NOT as required'}")
    return 0 if ok_all else 3


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    st, rest = argv[0], argv[1:]
    if st == "replot":
        return {"keyup": stage_keyup, "asis": stage_asis, "seq": stage_seq}[rest[0]](rerun=False)
    if st == "summary":
        return stage_summary()
    if st == "gen":
        for g in (gen_keyup, gen_asis, gen_seq):
            name, text, _ = g()
            (HERE / name).write_text(text)
            print("wrote", name)
        return 0
    return {"keyup": stage_keyup, "asis": stage_asis, "seq": stage_seq}[st]()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
