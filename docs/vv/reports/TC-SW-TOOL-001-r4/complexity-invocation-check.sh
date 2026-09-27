#!/bin/sh
# G5 complexity invocation check after the INSP-016 finding-14 fix of tools/sw_gate.sh
# (TC-SW-TOOL-001 run 3 item B8; tools/toolchain.lock.md section 1.4 finding 10).
# Runs only the G5 complexity block of tools/sw_gate.sh, extracted verbatim from the working
# tree, outside the gate: no cargo, no rustup, no Miri, no network. Sources are git archives
# (committed content only): cwht HEAD firmware/ and the complexity tools, and rustos api/ and
# firmware/pico2 at the lock pin c54d35a and at 2ec64c0 (SRR decision 110 branch commit).
# Usage: complexity-invocation-check.sh <new scratch directory>
set -u
S=${1:?usage: complexity-invocation-check.sh <new scratch directory>}
CWHT=/Users/robinonsay/rust/cwht
RUSTOS_REPO=/Users/robinonsay/rust/rustos
PY=$CWHT/.venv/bin/python
[ -e "$S" ] && { echo "scratch directory exists: $S"; exit 2; }
mkdir -p "$S"

echo "== $(date '+%Y-%m-%dT%H:%M:%S%z') configuration"
echo "cwht HEAD $(git -C "$CWHT" rev-parse HEAD)"
echo "tools/sw_gate.sh working tree: git blob $(git -C "$CWHT" hash-object tools/sw_gate.sh); HEAD blob $(git -C "$CWHT" rev-parse HEAD:tools/sw_gate.sh)"
echo "tools/complexity_gate.py HEAD blob $(git -C "$CWHT" rev-parse HEAD:tools/complexity_gate.py); working tree $(git -C "$CWHT" hash-object tools/complexity_gate.py)"
echo "tools/unsafe_audit.py HEAD blob $(git -C "$CWHT" rev-parse HEAD:tools/unsafe_audit.py)"
echo "$(rust-code-analysis-cli --version) at $(command -v rust-code-analysis-cli)"
echo "python $($PY --version 2>&1)"
echo "diff of tools/sw_gate.sh against HEAD:"
git -C "$CWHT" diff HEAD -- tools/sw_gate.sh

# The G5 complexity block of the gate, verbatim (from "if command -v rust-code-analysis-cli"
# to the closing "fi" at column 0).
BLOCK="$S/g5-complexity-block.sh"
sed -n '/^if command -v rust-code-analysis-cli/,/^fi$/p' "$CWHT/tools/sw_gate.sh" > "$BLOCK"
echo "== extracted block ($(wc -l < "$BLOCK" | tr -d ' ') lines):"
cat "$BLOCK"

layout() { # $1 layout dir, $2 rustos commit
    mkdir -p "$1/cwht" "$1/rustos"
    git -C "$CWHT" archive HEAD firmware tools/complexity_gate.py tools/unsafe_audit.py | tar -x -C "$1/cwht"
    git -C "$RUSTOS_REPO" archive "$2" api firmware/pico2 | tar -x -C "$1/rustos"
}

run_block() { # $1 layout dir; runs the gate block with the gate's variable names
    ROOT="$1/cwht" FW="$1/cwht/firmware" RUSTOS="$1/rustos" PY="$PY" BLOCK="$BLOCK" sh -c '
        pass() { echo "PASS $1"; }
        fail() { echo "FAIL $1"; }
        missing() { echo "MISSING $1"; }
        . "$BLOCK"'
    echo "block exit $?"
}

per_root() { # $1 layout dir; analyzer output with the fixed form, counted per root
    rust-code-analysis-cli --metrics --output-format json \
        --paths "$1/cwht/firmware" --paths "$1/rustos/api" --paths "$1/rustos/firmware/pico2" \
        > "$1/rca.json" 2> "$1/rca.err"
    echo "analyzer exit $?; bytes $(wc -c < "$1/rca.json" | tr -d ' '); stderr lines $(wc -l < "$1/rca.err" | tr -d ' ')"
    "$PY" - "$1" <<'EOF'
import json, sys
root = sys.argv[1]
text = open(root + "/rca.json").read()
dec = json.JSONDecoder(); i = 0; objs = []
while i < len(text):
    while i < len(text) and text[i].isspace(): i += 1
    if i >= len(text): break
    o, i = dec.raw_decode(text, i); objs.append(o)
def funcs(s):
    n = 1 if s.get("kind") == "function" else 0
    return n + sum(funcs(c) for c in s.get("spaces", []))
for label, pre in (("firmware", "/cwht/firmware/"), ("rustos api", "/rustos/api/"), ("rustos firmware/pico2", "/rustos/firmware/pico2/")):
    sel = [o for o in objs if o["name"].startswith(root + pre)]
    print(f"  {label}: {len(sel)} files, {sum(funcs(o) for o in sel)} function spaces")
print(f"  total: {len(objs)} files, {sum(funcs(o) for o in objs)} function spaces")
EOF
}

seed() { # $1 layout dir; a CC 17 function (16 if) in a new file under each of the three roots
    for pair in "cwht/firmware/cwht-core/src:seed_ka_core" "rustos/api/src:seed_ka_api" "rustos/firmware/pico2/src:seed_ka_pico2"; do
        dir=${pair%%:*}; name=${pair#*:}
        {
            echo "pub fn $name(x: u32) -> u32 {"
            k=1; while [ $k -le 16 ]; do echo "    if x == $k { return $k; }"; k=$((k + 1)); done
            echo "    0"
            echo "}"
        } > "$1/$dir/seed_ka.rs"
    done
}

for C in c54d35aa8e7f9ad30f6508bca458a59c1fc009db 2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c; do
    L="$S/layout-$(printf %.7s "$C")"
    layout "$L" "$C"
    echo "== $(date '+%Y-%m-%dT%H:%M:%S%z') layout $L (rustos $C)"
    echo "-- A. superseded form, three values after one --paths (reproduces finding-14):"
    rust-code-analysis-cli --metrics --output-format json --paths "$L/cwht/firmware" "$L/rustos/api" "$L/rustos/firmware/pico2" \
        > "$L/old.json" 2> "$L/old.err"
    echo "analyzer exit $?; bytes $(wc -c < "$L/old.json" | tr -d ' '); stderr first line: $(head -1 "$L/old.err")"
    echo "-- B. the gate block as fixed (verbatim from tools/sw_gate.sh):"
    run_block "$L"
    echo "-- C. analyzer input read per root (fixed form):"
    per_root "$L"
    echo "-- D. seeded known answer: one CC 17 function added under each of the three roots:"
    seed "$L"
    run_block "$L"
done
echo "== $(date '+%Y-%m-%dT%H:%M:%S%z') end; scratch layouts removed"
rm -rf "$S"
