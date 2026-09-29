"""Run every LTspice deck of the rx-frontend block through tools/ltspice-batch.sh (ACC-LTSPICE-001) into its
results/<run-id>/ directory, and copy the deck, its draw or case file and the scripts there so that each run
directory is self-contained. Usage: .venv/bin/python hardware/sim/rx-frontend/run_sims.py [run-id ...]"""
import os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
WRAP = os.path.join(REPO, "tools", "ltspice-batch.sh")
RUNS = {
    "2026-09-28-r01-bpf-ts012-baseline": ["bpf_2p3_bw5.net", "bpf_2p3_bw6.net", "bpf_2p3_bw6_mcA.net", "bpf_2p3_bw6_mcB.net"],
    "2026-09-28-r02-bpf-three-section": ["bpf_2p3p2_bw6.net", "bpf_2p3p3_bw6.net"],
    "2026-09-28-r03-bpf-three-section-mc": ["bpf_2p3p2_bw6_mcA.net", "bpf_2p3p2_bw6_mcB.net", "bpf_2p3p3_bw6_mcA.net", "bpf_2p3p3_bw6_mcB.net"],
    "2026-09-28-r04-bpf-leakage": ["bpf_2p3p3_bw6_leak.net"],
    "2026-09-28-r05-halfif-mixers": ["halfif_ring.net"] + [f"halfif_jfet_c{i:02d}.net" for i in range(1, 17)],
    # revision 2 (review findings 1, 2, 5): decks written by worst_case.py prepare r08 / r09 / r10
    "2026-09-28-r08-bpf-tolerance-corners": [f"bpf_{k}_corners.net" for k in ("2p3_if8", "2p3p3_if8", "2p3p4_if8", "2p3p2_if10")]
        + [f"bpf_2p3p3_if8_mc1000_{a}.net" for a in ("none_A", "at50_A", "at50_B")],
    "2026-09-28-r09-bpf-port-impedance": [f"bpf_{k}_ports.net" for k in ("2p3p3_if8", "2p3p4_if8", "2p3p2_if10")],
    "2026-09-28-r10-bpf-leakage-corner": [f"bpf_{k}_leak_corner.net" for k in ("2p3p3_if8", "2p3p4_if8", "2p3p2_if10")],
    # revision 3 (review iteration 2, finding 6): decks written by worst_case.py prepare r12
    "2026-09-28-r12-bpf-residual-design-input": [f"bpf_{k}_resid.net" for k in ("2p3p3_if8", "2p3p4_if8", "2p3p2_if10")],
    # revision 4 (review iteration 3, finding-7): decks written by worst_case.py prepare r13
    "2026-09-29-r13-bpf-temperature": [f"bpf_{k}_temp.net" for k in ("2p3p4_if8", "2p3p2_if10", "2p3p3_if8")],
}
SCRIPTS = ["bpf_design.py", "make_decks.py", "run_sims.py", "check_bpf.py", "check_halfif.py", "cascade.py", "explore.py",
           "bpf_nodal.py", "tolerance.py", "worst_case.py", "validate_nodal.py"]


def run(run_id):
    failed = []
    out = os.path.join(HERE, "results", run_id)
    os.makedirs(out, exist_ok=True)
    for deck in RUNS[run_id]:
        src = os.path.join(HERE, "decks", deck)
        tmo = "240" if deck.startswith("halfif_jfet") else "600"
        r = subprocess.run([WRAP, "-t", tmo, "-o", out, "-b", src], capture_output=True, text=True)
        sys.stderr.write(r.stderr)
        if r.returncode != 0:
            sys.stderr.write(f"run_sims: {deck}: ltspice-batch exit {r.returncode} (recorded; the checker reports the missing case)\n")
            failed.append(deck)
        shutil.copy2(src, out)
        base = deck.split("_c")[0] if deck.startswith("halfif_jfet_c") else deck.replace(".net", "")
        for side in (deck.replace(".net", "_draws.npz"), base + "_cases.json"):
            p = os.path.join(HERE, "decks", side)
            if os.path.exists(p):
                shutil.copy2(p, out)
    sd = os.path.join(out, "scripts")
    os.makedirs(sd, exist_ok=True)
    for s in SCRIPTS:
        p = os.path.join(HERE, s)
        if os.path.exists(p):
            shutil.copy2(p, sd)
    return failed


if __name__ == "__main__":
    bad = []
    for rid in (sys.argv[1:] or list(RUNS)):
        bad += run(rid)
    # non-zero exit when any deck failed in the wrapper (the r05 JFET non-convergence cases are expected failures)
    sys.exit(1 if bad else 0)
