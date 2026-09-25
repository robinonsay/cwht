#!/bin/bash
# Monte Carlo batch for docs/research/cw-selectivity-options.md (headless LTspice 26.x via bundled wine).
# Usage: mc_batch.sh [design_bw_500 ] [runs]
# Spread assumptions (see report, Finding on crystal tolerances):
#   catalogue  : frequency uniform +/-30 ppm (ECS HC-49US, Abracon ABLS code 4)
#   tight      : frequency uniform +/-10 ppm (Abracon ABLS code 1)
#   same-lot   : frequency gaussian sigma 4 ppm truncated +/-15 ppm (Land Boards 50-crystal IQD batch: sigma 36 Hz, range +/-137 Hz)
#   Cm         : gaussian sigma 3 %, truncated +/-10 % (WA5BDU: measurement methods agree within 5 %; QEX 2009: varies batch to batch)
#   Rs         : uniform 8 to 30 ohm (K8IQY 13 ohm example; datasheet max 60 ohm handled as a separate nominal case)
#   C0         : uniform 3.5 to 5.5 pF (K8IQY 3.5 pF estimate; WA5BDU C0 = 220 Cm; datasheet max 7 pF)
#   capacitors : uniform +/-2 % (C0G); resistors +/-1 %
set -u
cd "$(dirname "$0")"
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
BW4=${1:-540}      # 4-pole design bandwidth giving about 500 Hz at -3 dB after finite-Q shrinkage
BW6=${3:-660}      # 6-pole design bandwidth giving about 500 Hz at -3 dB after finite-Q shrinkage
RUNS=${2:-200}
COMMON="--runs $RUNS --cm-sigma-pct 3 --cm-trunc-pct 10 --rs-min 8 --rs-max 30 --c0-min-pf 3.5 --c0-max-pf 5.5 --cap-pct 2 --res-pct 1 --rs 15 ${EXTRA:-}"
# EXTRA="--reuse-raw" re-parses existing out/*.raw files (same random draws) instead of simulating again.
LOG=out/mc_batch.log
mkdir -p out
echo "=== batch start $(date) design_bw4=$BW4 design_bw6=$BW6 runs=$RUNS ===" | tee -a $LOG
run() { echo "--- $* ---" | tee -a $LOG; $PY xtal_ladder_mc.py "$@" 2>&1 | grep -v '^{' | grep -v '^ "' | grep -v '^ }' | grep -v '^}' | tee -a $LOG; }
# 500 Hz CW filters
run --case mc_4p_500_catalogue30 --poles 4 --bw $BW4 --bw-target 500 --f-ppm 30 --f-dist flat $COMMON --fspan 6000 --points 6001
run --case mc_6p_500_catalogue30 --poles 6 --bw $BW6 --bw-target 500 --f-ppm 30 --f-dist flat $COMMON --fspan 6000 --points 6001
run --case mc_4p_500_tight10     --poles 4 --bw $BW4 --bw-target 500 --f-ppm 10 --f-dist flat $COMMON --fspan 6000 --points 6001
run --case mc_6p_500_tight10     --poles 6 --bw $BW6 --bw-target 500 --f-ppm 10 --f-dist flat $COMMON --fspan 6000 --points 6001
run --case mc_4p_500_samelot4    --poles 4 --bw $BW4 --bw-target 500 --f-ppm 4 --f-dist gauss --f-trunc-ppm 15 $COMMON --fspan 6000 --points 6001
run --case mc_6p_500_samelot4    --poles 6 --bw $BW6 --bw-target 500 --f-ppm 4 --f-dist gauss --f-trunc-ppm 15 $COMMON --fspan 6000 --points 6001
# 2.4 kHz roofing filter for the DSP architecture (Chebyshev 0.1 dB)
run --case mc_4p_2400_catalogue30 --poles 4 --bw 2400 --bw-target 2400 --proto chebyshev --ripple 0.1 --f-ppm 30 --f-dist flat $COMMON --fspan 15000 --points 6001
run --case mc_6p_2400_catalogue30 --poles 6 --bw 2400 --bw-target 2400 --proto chebyshev --ripple 0.1 --f-ppm 30 --f-dist flat $COMMON --fspan 15000 --points 6001
# 1 kHz CW compromise
run --case mc_4p_1000_catalogue30 --poles 4 --bw 1060 --bw-target 1000 --f-ppm 30 --f-dist flat $COMMON --fspan 8000 --points 6001
echo "=== batch end $(date) ===" | tee -a $LOG
