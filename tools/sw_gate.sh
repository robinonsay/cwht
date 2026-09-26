#!/bin/sh
# cwht software gate (docs/process/07-software-engineering-plan.md section 8.4, Annex C).
#
#   G0 toolchain identity   rustc equals the tools/toolchain.lock.md rustc row; rustos commit
#                           equals the lock's rustos row and its code directories are clean
#   G1 format and lint      cargo fmt --check; clippy -D warnings on host and target
#   G2 build                cwht-app release for thumbv8m.main-none-eabihf with no compiler
#                           warning; flash and RAM use taken from the link map against the
#                           TPM-010/TPM-011 red lines; no allocator symbol (CS-01); image
#                           dependency set is workspace plus rustos only (CS-02)
#   G3 host tests x2        cargo nextest --profile ci twice; identical (classname, name,
#                           outcome) sets (SWE-186)
#   G4 traceability         tools/traceability.py (report written under firmware/target, not
#                           over docs/vv/traceability-report.md)
#   G5 static analysis      cargo audit; cargo deny; cargo geiger; unsafe audit; complexity;
#                           Miri (nightly, non-credit, MSR-08)
#   G6 coverage, emulation  cargo llvm-cov (stable, MSR-13, 100 percent lines and regions of
#                           the workspace host crates); branch and condition coverage (nightly,
#                           MSR-14); tools/emu_run.sh (SKIP line until the PDR emulator ADR)
#
# G0 is an addition to 07 section 8.4 and Annex C (a failed identity check makes every later
# result meaningless); --quick includes it (report TC-SW-TOOL-001-r1 deviation D7).
#
# Usage: tools/sw_gate.sh [--quick | --keep-going]
#   --quick       runs G0 to G3
#   --keep-going  runs every step of G1 to G6 past a FAIL and reports every failure
#                 (diagnostic runs; the gate result is still FAIL). A G2 step whose input the
#                 failed build did not produce is reported FAIL without being run. Two kinds of
#                 failure always stop the script, in both modes: setup (the output directory
#                 cannot be created) and any G0 toolchain-identity failure.
# Run from anywhere; macOS host; headless.
#
# Result lines: "PASS <step>", "FAIL <step>", "MISSING <step>: <reason>", "SKIP <step>: <reason>".
# Exit status: 0 every step passed; 1 a step failed (the script stops at the first FAIL unless
# --keep-going is given);
# 3 no step failed but at least one prerequisite tool or script is MISSING, so the gate is
# incomplete and does not meet the FW-B0 exit criterion of 07 section 3.2.
#
# Never downloads: RUSTUP_AUTO_INSTALL=0 stops rustup from installing the pinned toolchain or
# components on its own, cargo audit runs with --no-fetch, and cargo deny's advisories check
# runs only when its database is already present. Installing a toolchain, a component or an
# advisory database is an owner-approved action recorded in tools/toolchain.lock.md.
#
# Scripts of 07 section 1.2 used by the gate (written 2026-09-26, SRR package item R3; TV-011 to
# TV-013): tools/measurements.py (G2 --link-map, G3 --diff-runs, G6 --coverage),
# tools/unsafe_audit.py --check (G5), tools/complexity_gate.py --max 15 (G5, fed by
# rust-code-analysis-cli). The inline Python blocks below are the FW-B0 interim checks; they run
# only if tools/measurements.py is absent and then print INTERIM.

set -u

ROOT=$(cd "$(dirname "$0")/.." && pwd)
FW="$ROOT/firmware"
RUSTOS="$(cd "$ROOT/.." && pwd)/rustos"
PY="$ROOT/.venv/bin/python"
TARGET=thumbv8m.main-none-eabihf
NIGHTLY=nightly-2026-08-24
NX="$FW/target/nextest"
OUT="$FW/target/sw-gate"
LOCK="$ROOT/tools/toolchain.lock.md"
MODE=full
KEEP_GOING=0
case "${1:-}" in
    --quick) MODE=quick ;;
    --keep-going) KEEP_GOING=1 ;;
    "") ;;
    *) echo "usage: tools/sw_gate.sh [--quick | --keep-going]"; exit 2 ;;
esac
MISSING_COUNT=0
FAIL_COUNT=0

export RUSTUP_AUTO_INSTALL=0
export CARGO_TERM_COLOR=never

pass() { echo "PASS $1"; }
fatal() { echo "FAIL $1"; echo "sw_gate: FAIL at $1"; exit 1; }
fail() {
    echo "FAIL $1"
    FAIL_COUNT=$((FAIL_COUNT + 1))
    [ "$KEEP_GOING" -eq 1 ] || { echo "sw_gate: FAIL at $1"; exit 1; }
}
missing() { echo "MISSING $1"; MISSING_COUNT=$((MISSING_COUNT + 1)); }
step() {
    label=$1
    shift
    echo "---- $label: $*"
    if "$@"; then pass "$label"; else fail "$label"; fi
}
fwrun() { (cd "$FW" && "$@"); }

mkdir -p "$OUT" || fatal "setup (mkdir $OUT)"
echo "sw_gate: mode $MODE, $(date -u '+%Y-%m-%dT%H:%M:%SZ'), repo $(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)"

# ---------------------------------------------------------------- G0 toolchain identity
EXPECTED_RUSTC=$(sed -n 's/^| rustc | `rustc --version` | `\(rustc [^`]*\)`.*/\1/p' "$LOCK")
[ -n "$EXPECTED_RUSTC" ] || fatal "G0 rustc row not found in tools/toolchain.lock.md"
PIN=$(sed -n 's/^channel = "\(.*\)"/\1/p' "$FW/rust-toolchain.toml")
[ -n "$PIN" ] || fatal "G0 channel not found in firmware/rust-toolchain.toml"
if rustup toolchain list | grep -q "^$PIN-"; then
    echo "G0 pinned toolchain $PIN installed; firmware/rust-toolchain.toml selects it"
else
    STABLE_RUSTC=$(rustc +stable --version 2>/dev/null || true)
    if [ "$STABLE_RUSTC" = "$EXPECTED_RUSTC" ]; then
        export RUSTUP_TOOLCHAIN=stable
        echo "NOTE G0 pinned toolchain $PIN not installed (installing it downloads; owner approval);"
        echo "NOTE G0 using stable, whose rustc is identical to the lock row: $STABLE_RUSTC"
    else
        fatal "G0 pinned toolchain $PIN absent and stable rustc '$STABLE_RUSTC' differs from the lock '$EXPECTED_RUSTC'"
    fi
fi
ACTUAL_RUSTC=$(fwrun rustc --version)
echo "G0 rustc in firmware/: $ACTUAL_RUSTC"
[ "$ACTUAL_RUSTC" = "$EXPECTED_RUSTC" ] || fatal "G0 rustc '$ACTUAL_RUSTC' differs from the lock '$EXPECTED_RUSTC'"
fwrun cargo --version
fwrun rustup target list --installed | grep -q "^$TARGET\$" || fatal "G0 target $TARGET not installed"
EXPECTED_RUSTOS=$(sed -n 's/^| `rustos` .* | `\([0-9a-f]\{40\}\)` .*/\1/p' "$LOCK")
ACTUAL_RUSTOS=$(git -C "$RUSTOS" rev-parse HEAD 2>/dev/null || echo none)
echo "G0 rustos HEAD $ACTUAL_RUSTOS (lock: ${EXPECTED_RUSTOS:-not found})"
[ "$ACTUAL_RUSTOS" = "$EXPECTED_RUSTOS" ] || fatal "G0 rustos commit differs from tools/toolchain.lock.md"
DIRTY=$(git -C "$RUSTOS" status --porcelain -- api firmware Cargo.toml Cargo.lock .cargo)
[ -z "$DIRTY" ] || { echo "$DIRTY"; fatal "G0 rustos api/firmware have uncommitted changes"; }
pass "G0 toolchain identity"

# ---------------------------------------------------------------- G1 format and lint
# cwht-app is target-only (#![no_main]; pico2 has Arm assembly), so host clippy excludes it
# and the target clippy covers it (07 Annex C lists the abridged commands).
step "G1 cargo fmt --check" fwrun cargo fmt --check
step "G1 clippy host" fwrun cargo clippy --workspace --exclude cwht-app --all-targets -- -D warnings
step "G1 clippy target" fwrun cargo clippy -p cwht-app --target "$TARGET" -- -D warnings

# ---------------------------------------------------------------- G2 build
# The ELF and link-map steps run only when this invocation's build succeeded, so that a FAIL
# under --keep-going never lets them read an ELF or map left by an earlier build.
echo "---- G2 build: cargo build -p cwht-app --release --target $TARGET"
G2_BUILT=0
if fwrun cargo build -p cwht-app --release --target "$TARGET" >"$OUT/g2-build.txt" 2>&1; then
    cat "$OUT/g2-build.txt"
    pass "G2 build"
    G2_BUILT=1
else
    cat "$OUT/g2-build.txt"
    fail "G2 build"
fi
# Any compiler or linker warning fails G2 (no warning is expected: the linker's
# --print-memory-usage is not requested, firmware/.cargo/config.toml).
echo "---- G2 no compiler warning: grep warning $OUT/g2-build.txt"
if grep -E '^warning' "$OUT/g2-build.txt"; then
    fail "G2 no compiler warning"
else
    pass "G2 no compiler warning"
fi
ELF="$FW/target/$TARGET/release/cwht-app"
MAP="$FW/target/$TARGET/release/cwht-app.map"
LINKLD="$RUSTOS/firmware/pico2/link.ld"
if [ "$G2_BUILT" -ne 1 ]; then
    fail "G2 memory use (not run: G2 build failed)"
elif [ ! -f "$MAP" ]; then
    fail "G2 memory use (link map $MAP not written)"
elif [ -f "$ROOT/tools/measurements.py" ]; then
    step "G2 link map (measurements.py)" "$PY" "$ROOT/tools/measurements.py" --link-map "$MAP"
else
    echo "INTERIM G2 tools/measurements.py absent; inline link-map memory-usage check"
    step "G2 memory use within TPM-010/TPM-011 red lines" "$PY" - "$MAP" "$LINKLD" <<'PYEOF'
import re, sys
# Region origin and length from the MEMORY block of rustos pico2 link.ld; use per region from
# the lld link map: the highest end address (LMA for FLASH, VMA for RAM) of any output section
# placed in the region, less the origin, which is the extent the linker's own memory report
# gives. Red lines: TPM-010 flash unused below 30 % and TPM-011 RAM unused below 25 %
# (docs/plan/tpm.json), applied to the link.ld regions until the allocated-region sizes of
# 07 section 19 WP-SW-08 exist.
limits = {"FLASH": 70.0, "RAM": 75.0}
units = {"": 1, "K": 1024, "M": 1024 * 1024}
regions = {}
for m in re.finditer(r"\b(FLASH|RAM)\s*\([a-z]*\)\s*:\s*ORIGIN\s*=\s*(0x[0-9a-fA-F]+)\s*,\s*LENGTH\s*=\s*(\d+)([KM]?)",
                     open(sys.argv[2], encoding="utf-8").read()):
    regions[m.group(1)] = (int(m.group(2), 16), int(m.group(3)) * units[m.group(4)])
# Output-section lines: VMA LMA Size Align, then the section name after one space.
section = re.compile(r"^\s*([0-9a-f]+)\s+([0-9a-f]+)\s+([0-9a-f]+)\s+\d+ (\.[^ ]+)$")
end = {"FLASH": None, "RAM": None}
for line in open(sys.argv[1], encoding="utf-8"):
    m = section.match(line.rstrip("\n"))
    if not m:
        continue
    vma, lma, size = (int(m.group(i), 16) for i in (1, 2, 3))
    for name, addr in (("FLASH", lma), ("RAM", vma)):
        origin, length = regions.get(name, (0, 0))
        if length and origin <= addr < origin + length:
            end[name] = max(end[name] or origin, addr + size)
ok = set(regions) == set(limits) and all(v is not None for v in end.values())
for name in limits:
    if name in regions and end[name] is not None:
        origin, length = regions[name]
        used = end[name] - origin
        pct = 100.0 * used / length
        ok = ok and pct <= limits[name]
        print(f"{name} used {used} B of {length} B = {pct:.2f} % (limit {limits[name]} %)")
    else:
        print(f"{name}: region or sections not found")
sys.exit(0 if ok else 1)
PYEOF
fi
if [ "$G2_BUILT" -ne 1 ]; then
    fail "G2 no allocator symbol (not run: G2 build failed)"
else
    echo "---- G2 no allocator symbol (CS-01): rust-nm $ELF"
    if SYMS=$(fwrun rust-nm -C "$ELF" 2>/dev/null); then
        # Known-answer guard: the symbol list must contain the entry shim, or the check read
        # nothing.
        if ! printf '%s\n' "$SYMS" | grep -q '__rustos_main'; then
            fail "G2 no allocator symbol (rust-nm output lacks __rustos_main)"
        elif printf '%s\n' "$SYMS" | grep -E '__rust_alloc|__rust_dealloc|__rg_alloc|__rdl_alloc|__rust_alloc_error_handler|alloc::alloc'; then
            fail "G2 no allocator symbol (allocator symbol present)"
        else
            pass "G2 no allocator symbol"
        fi
    else
        fail "G2 no allocator symbol (rust-nm could not read the ELF)"
    fi
    shasum -a 256 "$ELF"
fi
echo "---- G2 image dependency set (CS-02): cargo tree -e normal -p cwht-app --target $TARGET"
if TREE=$(fwrun cargo tree -e normal -p cwht-app --target "$TARGET" --prefix none --format '{p}'); then
    printf '%s\n' "$TREE" | sort -u
    EXTRA=$(printf '%s\n' "$TREE" | awk '{print $1}' | sort -u | grep -v -x -E 'cwht-app|cwht-core|api|pico2' || true)
    if [ -z "$EXTRA" ]; then
        pass "G2 image dependency set"
    else
        fail "G2 image dependency set (crates outside the workspace and rustos: $EXTRA)"
    fi
else
    fail "G2 image dependency set (cargo tree failed)"
fi

# ---------------------------------------------------------------- G3 host tests x2
# Both JUnit copies are removed first, so the comparison can only read files this invocation
# wrote; a missing copy fails the comparison without running it.
rm -f "$NX/run1-junit.xml" "$NX/run2-junit.xml"
for run in 1 2; do
    echo "---- G3 host tests run $run: cargo nextest run --workspace --exclude cwht-app --profile ci"
    if fwrun cargo nextest run --workspace --exclude cwht-app --profile ci \
        && cp "$NX/ci/junit.xml" "$NX/run$run-junit.xml"; then
        pass "G3 host tests run $run"
    else
        fail "G3 host tests run $run"
    fi
done
if [ ! -f "$NX/run1-junit.xml" ] || [ ! -f "$NX/run2-junit.xml" ]; then
    fail "G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)"
elif [ -f "$ROOT/tools/measurements.py" ]; then
    step "G3 identical result sets (measurements.py)" "$PY" "$ROOT/tools/measurements.py" --diff-runs "$NX/run1-junit.xml" "$NX/run2-junit.xml"
else
    echo "INTERIM G3 tools/measurements.py absent; inline JUnit comparison"
    step "G3 identical result sets (SWE-186)" "$PY" - "$NX/run1-junit.xml" "$NX/run2-junit.xml" <<'PYEOF'
import sys
import xml.etree.ElementTree as ET

def results(path):
    out = set()
    for case in ET.parse(path).getroot().iter("testcase"):
        tags = {child.tag for child in case}
        outcome = "failure" if tags & {"failure", "rerunFailure", "flakyFailure"} else "error" if "error" in tags else "skipped" if "skipped" in tags else "passed"
        out.add((case.get("classname"), case.get("name"), outcome))
    return out

first, second = results(sys.argv[1]), results(sys.argv[2])
print(f"run 1: {len(first)} cases, run 2: {len(second)} cases, passed in both: {sum(1 for r in first & second if r[2] == 'passed')}")
for row in sorted(first ^ second):
    print("DIFF", row)
sys.exit(0 if first == second and first and all(r[2] == "passed" for r in first) else 1)
PYEOF
fi

if [ "$MODE" = quick ]; then
    [ "$FAIL_COUNT" -eq 0 ] || { echo "sw_gate: FAIL ($FAIL_COUNT step(s) failed)"; exit 1; }
    [ "$MISSING_COUNT" -eq 0 ] || { echo "sw_gate: INCOMPLETE ($MISSING_COUNT missing)"; exit 3; }
    echo "sw_gate: PASS (quick: G0 to G3)"
    exit 0
fi

# ---------------------------------------------------------------- G4 traceability
step "G4 traceability" "$PY" "$ROOT/tools/traceability.py" --output "$OUT/traceability-report.md" --quiet

# ---------------------------------------------------------------- G5 static analysis
if [ -d "$HOME/.cargo/advisory-db" ]; then
    step "G5 cargo audit" fwrun cargo audit --no-fetch
else
    missing "G5 cargo audit: RustSec advisory database absent (~/.cargo/advisory-db); fetching it is an owner-approved download"
fi
step "G5 cargo deny (bans, licenses, sources)" fwrun cargo deny --log-level error check bans licenses sources
if [ -d "$HOME/.cargo/advisory-dbs" ]; then
    step "G5 cargo deny advisories" fwrun cargo deny --log-level error check advisories
else
    missing "G5 cargo deny advisories: advisory database absent (~/.cargo/advisory-dbs); owner-approved download"
fi
# cargo geiger needs an absolute package manifest; --forbid-only scans sources without building
# and exits 0 whatever it finds, so the step checks that each cwht crate is marked ":)" (every
# entry point declares #![forbid(unsafe_code)], CS-05). rustos api and pico2 show "?" (they
# contain unsafe by design; counted by the unsafe audit).
for crate in cwht-app cwht-core cwht-hal-mock; do
    echo "---- G5 cargo geiger --forbid-only $crate"
    GEIGER=$(fwrun cargo geiger --forbid-only --manifest-path "$FW/$crate/Cargo.toml" 2>/dev/null)
    printf '%s\n' "$GEIGER" | grep -E '^(:\)|\?|!)'
    if printf '%s\n' "$GEIGER" | grep -q -E "^:\) $crate "; then
        pass "G5 cargo geiger --forbid-only $crate"
    else
        fail "G5 cargo geiger --forbid-only $crate (entry point without #![forbid(unsafe_code)])"
    fi
done
if [ -f "$ROOT/tools/unsafe_audit.py" ]; then
    step "G5 unsafe audit" "$PY" "$ROOT/tools/unsafe_audit.py" --check
else
    missing "G5 unsafe audit: tools/unsafe_audit.py not written (07 CS-06, CS-07)"
fi
if command -v rust-code-analysis-cli >/dev/null 2>&1 && [ -f "$ROOT/tools/complexity_gate.py" ]; then
    echo "---- G5 complexity: rust-code-analysis-cli | tools/complexity_gate.py --max 15"
    if rust-code-analysis-cli --metrics --output-format json --paths "$FW" "$RUSTOS/api" "$RUSTOS/firmware/pico2" \
        | "$PY" "$ROOT/tools/complexity_gate.py" --max 15; then pass "G5 complexity"; else fail "G5 complexity"; fi
else
    command -v rust-code-analysis-cli >/dev/null 2>&1 || missing "G5 complexity: rust-code-analysis-cli not installed (cargo install is an owner-approved download)"
    [ -f "$ROOT/tools/complexity_gate.py" ] || missing "G5 complexity: tools/complexity_gate.py not written (07 CS-17, CS-38)"
fi
if rustup component list --installed --toolchain "$NIGHTLY" 2>/dev/null | grep -q '^miri'; then
    step "G5 Miri (nightly, non-credit, MSR-08)" fwrun cargo "+$NIGHTLY" miri test -p api -p pico2 --lib
else
    missing "G5 Miri: component miri not installed on $NIGHTLY (07 CS-03; owner-approved download)"
fi

# ---------------------------------------------------------------- G6 coverage and emulation
# The three G6 outputs are removed first, so the G6 measurements step can only read files this
# invocation wrote (an output a MISSING or SKIP step did not write is reported NOT PRODUCED).
rm -f "$FW/target/lcov.info" "$FW/target/branch-condition.json" "$FW/target/emu-report.json"
step "G6 coverage (stable, MSR-13)" fwrun cargo llvm-cov nextest --workspace --exclude cwht-app --profile ci \
    --lcov --output-path "$FW/target/lcov.info" --fail-under-lines 100 --fail-under-regions 100
fwrun cargo llvm-cov report --summary-only 2>/dev/null || true
if rustup component list --installed --toolchain "$NIGHTLY" 2>/dev/null | grep -q '^llvm-tools'; then
    echo "---- G6 branch and condition coverage (nightly, non-credit, MSR-14)"
    if (cd "$FW" && RUSTFLAGS=-Zcoverage-options=condition cargo "+$NIGHTLY" llvm-cov nextest --workspace \
        --exclude cwht-app --profile ci --branch --json --output-path target/branch-condition.json); then
        pass "G6 branch and condition coverage"
    else
        fail "G6 branch and condition coverage"
    fi
else
    missing "G6 branch and condition coverage: llvm-tools not installed on $NIGHTLY (07 CS-03; owner-approved download)"
fi
if [ -x "$ROOT/tools/emu_run.sh" ]; then
    step "G6 emulation" "$ROOT/tools/emu_run.sh" --all --report "$FW/target/emu-report.json"
else
    missing "G6 emulation: tools/emu_run.sh not written (07 section 1.2 stub printing the SKIP line)"
fi
if [ -f "$ROOT/tools/measurements.py" ]; then
    step "G6 measurements" "$PY" "$ROOT/tools/measurements.py" --coverage "$FW/target/lcov.info" \
        --branch-condition "$FW/target/branch-condition.json" --emu "$FW/target/emu-report.json"
else
    missing "G6 measurements: tools/measurements.py not written (07 section 11)"
fi

if [ "$FAIL_COUNT" -gt 0 ]; then
    echo "sw_gate: FAIL ($FAIL_COUNT step(s) failed, $MISSING_COUNT prerequisite(s) missing)"
    exit 1
fi
if [ "$MISSING_COUNT" -gt 0 ]; then
    echo "sw_gate: INCOMPLETE (no step failed; $MISSING_COUNT prerequisite(s) missing)"
    exit 3
fi
echo "sw_gate: PASS (G0 to G6)"
exit 0
