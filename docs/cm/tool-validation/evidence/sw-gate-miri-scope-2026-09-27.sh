#!/bin/sh
# Re-validation of the tools/sw_gate.sh G5 Miri scope change (SRR close-out item B, owner ruling
# 2026-09-27; INSP-016 F-15; TC-SW-TOOL-001 run 5 item B11). Runs ONLY the G5 Miri block of the
# gate, extracted verbatim from the layout's tools/sw_gate.sh, never the full gate.
#
# Layout (commands as run on 2026-09-27; <SP> is the session scratch directory):
#   <SP>/miri-b/cwht    git -C /Users/robinonsay/rust/cwht archive HEAD (31272e0) | tar -x, then the
#                       working-tree tools/sw_gate.sh (the change under check) copied over it
#   <SP>/miri-b/rustos  git -C /Users/robinonsay/rust/rustos archive 2ec64c0 | tar -x (the lock pin,
#                       CR-004; never the owner's working tree)
#   <SP>/miri-b/guard/rustup  docs/vv/reports/TC-SW-TOOL-001-r5/rustup-guard.sh (run 3 guard, D13)
# Runs:
#   clean   the layout as above                               expected PASS, exit 0
#   KA-M1   copy of the layout with a seeded out-of-bounds read test appended to rustos api/src/lib.rs
#           (the seeded check of tools/toolchain.lock.md section 1.1 nightly row)  expected FAIL, exit 1
#   KA-M2   copy of the layout with the superseded HEAD tools/sw_gate.sh (-p api -p pico2)
#           expected FAIL, exit 1 (run 5 B11: invalid Mach-O section specifier)
# Usage: sw-gate-miri-scope-2026-09-27.sh <layout-dir> <guard-dir>
L=$1; G=$2
export PATH="$G:$PATH" CARGO_NET_OFFLINE=true MIRI_AUTO_OPS=no RUSTUP_AUTO_INSTALL=0 CARGO_TERM_COLOR=never
set -u
FW="$L/cwht/firmware"; NIGHTLY=nightly-2026-08-24; KEEP_GOING=1; FAIL_COUNT=0; MISSING_COUNT=0
pass() { echo "PASS $1"; }
fail() { echo "FAIL $1"; FAIL_COUNT=$((FAIL_COUNT + 1)); }
missing() { echo "MISSING $1"; MISSING_COUNT=$((MISSING_COUNT + 1)); }
step() { label=$1; shift; echo "---- $label: $*"; if "$@"; then pass "$label"; else fail "$label"; fi; }
fwrun() { (cd "$FW" && "$@"); }
BLOCK=$(awk '/^if rustup component list --installed --toolchain "\$NIGHTLY" 2>\/dev\/null \| grep -q .\^miri/,/^fi$/' "$L/cwht/tools/sw_gate.sh")
echo "# block extracted from $L/cwht/tools/sw_gate.sh (sha256 $(shasum -a 256 "$L/cwht/tools/sw_gate.sh" | cut -d' ' -f1)):"
printf '%s\n' "$BLOCK"
echo "# which rustup: $(command -v rustup)"
eval "$BLOCK"
echo "# FAIL_COUNT=$FAIL_COUNT MISSING_COUNT=$MISSING_COUNT"
[ "$FAIL_COUNT" -eq 0 ] && [ "$MISSING_COUNT" -eq 0 ]
