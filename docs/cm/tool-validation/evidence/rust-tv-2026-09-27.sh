#!/bin/sh
# Known-answer runs of TV-020 (rustc, cargo, clippy 1.98.0), TV-021 (cargo-llvm-cov), TV-022
# (cargo-nextest and the HostUnit harness, 03 section 6.5 item X10) and TV-023 (nightly-2026-08-24:
# MSR-14 branch and condition coverage, Miri), WP-PDR-08. A record of what was run, not a
# controlled tool (docs/cm/tool-validation/README.md "Evidence").
#
# Usage: rust-tv-2026-09-27.sh <scratch-dir> <guard-dir> <commit>
#   <guard-dir> holds the rustup shim of TC-SW-TOOL-001 run 3 deviation D13 (refuses component
#   add, toolchain install and self update), put first on PATH so no check can download.
#   <commit>    the cwht commit to test; everything runs on `git archive <commit>` exports.
# Layouts (clean-export rule of tools/toolchain.lock.md section 3; the owner's rustos working tree
# is never read: rustos is exported from its committed pin object):
#   <scratch>/A/cwht, <scratch>/A/rustos    layout A
#   <scratch>/B/x/cwht, <scratch>/B/x/rustos layout B (a second, deeper directory, for MSR-28)
set -u
SP=$1; GUARD=$2; COMMIT=$3
REPO=${REPO:-/Users/robinonsay/rust/cwht}   # a scratch clone may be named for a dry run
RUSTOS_GIT=/Users/robinonsay/rust/rustos
PIN=2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c
PY=/Users/robinonsay/rust/cwht/.venv/bin/python   # the TV-001 interpreter (Accredited, ACC-PYJS-001)
export PATH="$GUARD:$PATH" RUSTUP_AUTO_INSTALL=0 CARGO_NET_OFFLINE=true MIRI_AUTO_OPS=no CARGO_TERM_COLOR=never
unset RUSTFLAGS CARGO_TARGET_DIR
TGT=thumbv8m.main-none-eabihf
NIGHTLY=nightly-2026-08-24
W="$SP/tv"; rm -rf "$W"; mkdir -p "$W"
A="$W/A"; B="$W/B/x"
FX=tools/tests/fixtures/rust
hr() { echo; echo "================================================================ $*"; }
run() { echo "\$ $*"; "$@"; echo "exit=$?"; }
san() { sed "s|$W|<scratch>|g"; }
sha() { shasum -a 256 "$@" | san; }

for L in "$A" "$B"; do
  mkdir -p "$L/cwht" "$L/rustos"
  git -C "$REPO" archive "$COMMIT" | tar -x -C "$L/cwht"
  git -C "$RUSTOS_GIT" archive "$PIN" | tar -x -C "$L/rustos"
done

# ------------------------------------------------------------------------------------------------
hr "0. identity $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "cwht commit tested: $(git -C "$REPO" rev-parse "$COMMIT")"
echo "rustos pin exported: $(git -C "$RUSTOS_GIT" rev-parse "$PIN^{commit}") (lock section 3; git archive of the commit object)"
echo "fixture tree digests (git rev-parse <commit>:<path>):"
for p in kat-target kat-host cov-kat cond-kat miri-kat harness-seeded known-answers.json; do
  echo "  $(git -C "$REPO" rev-parse "$COMMIT:$FX/$p")  $FX/$p"
done
for p in firmware/Cargo.toml firmware/Cargo.lock firmware/rust-toolchain.toml firmware/.config/nextest.toml firmware/clippy.toml; do
  echo "  $(git -C "$REPO" rev-parse "$COMMIT:$p")  $p"
done
rustup --version 2>/dev/null
(cd "$A/cwht/firmware" && rustup show active-toolchain)
rustc +1.98.0 --version; cargo +1.98.0 --version; cargo +1.98.0 clippy --version
rustc +1.98.0 -vV | sed -n '/commit-hash/p;/LLVM/p'
rustc +$NIGHTLY --version; cargo +$NIGHTLY miri --version
cargo llvm-cov --version; cargo nextest --version | head -1
T1=$HOME/.rustup/toolchains/1.98.0-aarch64-apple-darwin; TN=$HOME/.rustup/toolchains/$NIGHTLY-aarch64-apple-darwin
echo "binary SHA-256:"
shasum -a 256 "$T1/bin/rustc" "$T1/bin/cargo" "$T1/bin/clippy-driver" "$T1/bin/cargo-clippy" \
  "$TN/bin/rustc" "$TN/bin/cargo" "$TN/bin/miri" "$TN/bin/cargo-miri" \
  "$HOME/.cargo/bin/cargo-llvm-cov" "$HOME/.cargo/bin/cargo-nextest" | sed "s|$HOME|~|"
echo "installed channel manifests:"
shasum -a 256 "$T1/lib/rustlib/multirust-channel-manifest.toml" "$TN/lib/rustlib/multirust-channel-manifest.toml" | sed "s|$HOME|~|"
echo "llvm-tools used by cargo-llvm-cov:"
shasum -a 256 "$T1/lib/rustlib/aarch64-apple-darwin/bin/llvm-cov" "$T1/lib/rustlib/aarch64-apple-darwin/bin/llvm-profdata" \
  "$TN/lib/rustlib/aarch64-apple-darwin/bin/llvm-cov" "$TN/lib/rustlib/aarch64-apple-darwin/bin/llvm-profdata" | sed "s|$HOME|~|"
"$T1/lib/rustlib/aarch64-apple-darwin/bin/llvm-cov" --version | sed -n '/LLVM version/p'
"$TN/lib/rustlib/aarch64-apple-darwin/bin/llvm-cov" --version | sed -n '/LLVM version/p'
echo "cargo install metadata (~/.cargo/.crates2.json):"
$PY - <<'EOF'
import json, os
d = json.load(open(os.path.expanduser("~/.cargo/.crates2.json")))
for k, v in sorted(d["installs"].items()):
    if k.startswith(("cargo-llvm-cov ", "cargo-nextest ")):
        print(" ", k, "profile", v.get("profile"), "target", v.get("target"), "built by", v.get("rustc", "").splitlines()[0])
EOF

# ------------------------------------------------------------------------------------------------
hr "1. TV-020 rustc and cargo: fixture kat-target, three release builds, ELF SHA-256 identical and equal to the stored value"
( cd "$A/cwht/$FX/kat-target"
  run cargo +1.98.0 build --release --locked --target-dir "$W/k1" 2>&1 | tail -2 | san
  run cargo +1.98.0 build --release --locked --target-dir "$W/k2" 2>&1 | tail -2 | san )
( cd "$B/cwht/$FX/kat-target" && run cargo +1.98.0 build --release --locked --target-dir "$W/k3" 2>&1 | tail -2 | san )
sha "$W/k1/$TGT/release/kat-target" "$W/k2/$TGT/release/kat-target" "$W/k3/$TGT/release/kat-target"
echo "stored elf_sha256: $($PY -c "import json;print(json.load(open('$A/cwht/$FX/known-answers.json'))['target_build']['elf_sha256'])")"

hr "2. TV-020 cargo test (reference runner): kat-host clean, then seeded-fail"
( cd "$A/cwht/$FX/kat-host"
  run cargo +1.98.0 test --locked --target-dir "$W/h" 2>&1 | grep -E "test result|^exit"
  run cargo +1.98.0 test --locked --features seeded-fail --target-dir "$W/h" 2>&1 | grep -E "test result|seeded_failure|^exit" | head -6 )

hr "3. TV-020 clippy: kat-host clean, seeded-lint (clippy::correctness), seeded-unwrap (project lint table in force)"
( cd "$A/cwht/$FX/kat-host"
  run cargo +1.98.0 clippy --locked --all-targets --target-dir "$W/h" -- -D warnings 2>&1 | grep -E "^error|^exit"
  run cargo +1.98.0 clippy --locked --all-targets --features seeded-lint --target-dir "$W/h" -- -D warnings 2>&1 | grep -E "^error|clippy::|^exit" | head -6
  run cargo +1.98.0 clippy --locked --all-targets --features seeded-unwrap --target-dir "$W/h" -- -D warnings 2>&1 | grep -E "^error|clippy::|^exit" | head -6 )

hr "4. TV-020 rustos blinky (07 sections 8.3 and 17.3): templates/pico2 of the pin, two clean builds in two directories, against docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf"
for L in "$A" "$B"; do
  BL="$L/blinky"; mkdir -p "$BL"; cp -R "$L/rustos/templates/pico2/." "$BL/"
  sed -i '' -e 's/^name = "{{project-name}}"/name = "blinky"/' \
    -e "s|^api = { git = \"https://github.com/robinonsay/rustos\" }|api = { path = \"$L/rustos/api\" }|" \
    -e "s|^pico2 = { git = \"https://github.com/robinonsay/rustos\" }|pico2 = { path = \"$L/rustos/firmware/pico2\" }|" "$BL/Cargo.toml"
done
echo "template diff (layout A; the same three lines as TC-SW-TOOL-001-r3 blinky-build.txt, paths into the export):"
diff "$A/rustos/templates/pico2/Cargo.toml" "$A/blinky/Cargo.toml" | san; echo "(diff exit $?)"
( cd "$A/blinky" && run cargo +1.98.0 build --release --target-dir "$W/b1" 2>&1 | grep -E "Finished|error|^exit" | san
  run cargo +1.98.0 build --release --target-dir "$W/b2" 2>&1 | grep -E "Finished|error|^exit" | san )
( cd "$B/blinky" && run cargo +1.98.0 build --release --target-dir "$W/b3" 2>&1 | grep -E "Finished|error|^exit" | san )
sha "$W/b1/$TGT/release/blinky" "$W/b2/$TGT/release/blinky" "$W/b3/$TGT/release/blinky" "$A/cwht/docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf"
echo "loadable image (rust-objcopy -O binary):"
for f in "$W/b1/$TGT/release/blinky" "$W/b3/$TGT/release/blinky" "$A/cwht/docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf"; do
  rust-objcopy -O binary "$f" "$f.bin"; sha "$f.bin"
done

hr "5. TV-020 MSR-28 (07 section 11.2): cwht-app release, clean builds in layouts A (twice) and B, against docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf"
( cd "$A/cwht/firmware" && run cargo +1.98.0 build -p cwht-app --release --locked --target $TGT --target-dir "$W/a1" 2>&1 | grep -E "Finished|warning: unused|error|^exit" | san
  run cargo +1.98.0 build -p cwht-app --release --locked --target $TGT --target-dir "$W/a2" 2>&1 | grep -E "Finished|error|^exit" | san )
( cd "$B/cwht/firmware" && run cargo +1.98.0 build -p cwht-app --release --locked --target $TGT --target-dir "$W/a3" 2>&1 | grep -E "Finished|error|^exit" | san )
sha "$W/a1/$TGT/release/cwht-app" "$W/a2/$TGT/release/cwht-app" "$W/a3/$TGT/release/cwht-app" "$A/cwht/docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf"
echo "firmware/ differences between the r3 build commit 0bcea39 and the commit tested:"
git -C "$REPO" diff --stat 0bcea39 "$COMMIT" -- firmware | tail -3
echo "loadable image (rust-objcopy -O binary):"
for f in "$W/a1/$TGT/release/cwht-app" "$W/a3/$TGT/release/cwht-app" "$A/cwht/docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf"; do
  rust-objcopy -O binary "$f" "$f.bin"; sha "$f.bin"
done
echo "debug sections naming a build path (layout A build 1):"
strings -a "$W/a1/$TGT/release/cwht-app" | grep -c "$W" | sed 's/^/  strings containing the scratch path: /'

hr "6. TV-020 HostUnit suite twice (07 section 17.3; SWE-186): firmware workspace, cargo nextest --profile ci and cargo test, layout A"
NX="$A/cwht/firmware/target/nextest"
for n in 1 2; do
  ( cd "$A/cwht/firmware" && run cargo +1.98.0 nextest run --locked --workspace --exclude cwht-app --profile ci 2>&1 | grep -E "Summary|FAIL|^exit" )
  cp "$NX/ci/junit.xml" "$W/hostunit-run$n-junit.xml"
done
$PY - "$W/hostunit-run1-junit.xml" "$W/hostunit-run2-junit.xml" <<'EOF'
import sys, xml.etree.ElementTree as ET
def triples(p):
    out = set()
    for tc in ET.parse(p).getroot().iter("testcase"):
        o = "failed" if (tc.find("failure") is not None or tc.find("error") is not None) else ("skipped" if tc.find("skipped") is not None else "passed")
        out.add((tc.get("classname"), tc.get("name"), o))
    return out
a, b = triples(sys.argv[1]), triples(sys.argv[2])
print(f"independent comparison (stdlib XML): run1 {len(a)} triples, run2 {len(b)} triples, identical {a == b}, all passed {all(t[2] == 'passed' for t in a | b)}")
for t in sorted(a): print("  ", *t)
EOF
echo "tools/measurements.py --diff-runs (TV-013, developer evidence until ACC-MEASURE-001):"
$PY "$A/cwht/tools/measurements.py" --diff-runs "$W/hostunit-run1-junit.xml" "$W/hostunit-run2-junit.xml" 2>&1 | san; echo "exit=$?"
for n in 1 2; do
  ( cd "$A/cwht/firmware" && cargo +1.98.0 test --locked --workspace --exclude cwht-app 2>&1 | grep -E "^test |test result" | sort > "$W/cargo-test-run$n.txt"; echo "cargo test run $n: $(grep -c '^test ' "$W/cargo-test-run$n.txt") test lines" )
done
cmp -s "$W/cargo-test-run1.txt" "$W/cargo-test-run2.txt" && echo "cargo test run 1 and run 2 sorted outputs identical" || echo "cargo test outputs DIFFER"
grep -E "test result" "$W/cargo-test-run1.txt" | sort | uniq -c

# ------------------------------------------------------------------------------------------------
hr "7. TV-021 cargo-llvm-cov (stable 1.98.0, llvm-tools of the pin): cov-kat 100 percent, then seeded-gap"
( cd "$A/cwht/$FX/cov-kat" && export CARGO_TARGET_DIR="$W/cv"
  run cargo +1.98.0 llvm-cov --locked --summary-only --fail-under-lines 100 --fail-under-regions 100 2>&1 | tail -3 | tr -s ' ' | san
  run cargo +1.98.0 llvm-cov --locked --features seeded-gap --text --fail-under-lines 100 --fail-under-regions 100 2>&1 | grep -E "^ +[0-9]+\| +0\||error|^exit" | head -8 | san )

hr "8. TV-021 firmware workspace coverage twice (the G6 MSR-13 command), lcov identical"
for n in 1 2; do
  ( cd "$A/cwht/firmware" && run cargo +1.98.0 llvm-cov nextest --locked --workspace --exclude cwht-app --profile ci \
      --lcov --output-path "$W/lcov-run$n.info" --fail-under-lines 100 --fail-under-regions 100 2>&1 | grep -E "Summary|error|^exit" | san )
done
sed "s|$A/cwht/||" "$W/lcov-run1.info" > "$W/lcov-run1.rel"; sed "s|$A/cwht/||" "$W/lcov-run2.info" > "$W/lcov-run2.rel"
cmp -s "$W/lcov-run1.rel" "$W/lcov-run2.rel" && echo "lcov run 1 and run 2 identical" || echo "lcov runs DIFFER"
$PY - "$W/lcov-run1.rel" <<'EOF'
import sys, collections
tot = collections.defaultdict(lambda: [0, 0, 0, 0])
cur = None
for line in open(sys.argv[1]):
    line = line.strip()
    if line.startswith("SF:"):
        p = line[3:]; cur = p.split("/")[1] if p.startswith("firmware/") else p.split("/")[0]
    elif line.startswith("LF:"): tot[cur][0] += int(line[3:])
    elif line.startswith("LH:"): tot[cur][1] += int(line[3:])
    elif line.startswith("FNF:"): tot[cur][2] += int(line[4:])
    elif line.startswith("FNH:"): tot[cur][3] += int(line[4:])
for k in sorted(tot):
    lf, lh, fnf, fnh = tot[k]
    print(f"  {k}: lines {lh} of {lf}, functions {fnh} of {fnf}")
EOF

# ------------------------------------------------------------------------------------------------
hr "9. TV-022 cargo-nextest: kat-host seeded-fail names the test and exits non-zero; clean exit 0 with the stored count"
( cd "$A/cwht/$FX/kat-host"
  run cargo +1.98.0 nextest run --locked --target-dir "$W/tn" --features seeded-fail 2>&1 | grep -E "FAIL \[|Summary|^exit"
  run cargo +1.98.0 nextest run --locked --target-dir "$W/tn" 2>&1 | grep -E "Summary|^exit" )

hr "10. TV-022 X10 harness self-test (03 section 6.5 item X10): harness-seeded against the real cwht-core and cwht-hal-mock"
junit() {
  $PY - "$1" <<'EOF'
import sys, xml.etree.ElementTree as ET
r = ET.parse(sys.argv[1]).getroot()
tcs = list(r.iter("testcase"))
failed = sorted(tc.get("name") for tc in tcs if tc.find("failure") is not None or tc.find("error") is not None)
print(f"  JUnit: {len(tcs)} testcases, failed {len(failed)}: {failed}")
EOF
}
HS="$A/cwht/$FX/harness-seeded"
for feat in none seeded-pair seeded-mock-fault seeded-pair,seeded-mock-fault; do
  if [ "$feat" = none ]; then F=""; else F="--features $feat"; fi
  echo "---- features: $feat"
  ( cd "$HS" && run cargo +1.98.0 nextest run --locked --profile ci --target-dir "$W/hs" $F 2>&1 | grep -E "FAIL \[|Summary|^exit" )
  junit "$HS/target/nextest/ci/junit.xml"   # nextest keeps its store under the workspace target/, not --target-dir
done
echo "---- reference runner: cargo test --features seeded-pair"
( cd "$HS" && run cargo +1.98.0 test --locked --target-dir "$W/hs" --features seeded-pair 2>&1 | grep -E "FAILED|test result|^exit" | head -4 )
echo "---- the harness fixture test build prints no warning (informational)"
( cd "$HS" && run cargo +1.98.0 build --locked --tests --target-dir "$W/hs" 2>&1 | grep -E "^warning|^error|^exit" | head -4 )

# ------------------------------------------------------------------------------------------------
hr "11. TV-023 MSR-14 on $NIGHTLY (non-credit): cond-kat seeded unexercised condition outcome, then complete"
( cd "$A/cwht/$FX/cond-kat" && export CARGO_TARGET_DIR="$W/tc" RUSTFLAGS=-Zcoverage-options=condition
  run cargo +$NIGHTLY llvm-cov --locked --branch --text 2>&1 | grep -E "Branch|Condition|MC/DC|^exit|error" | head -8
  run cargo +$NIGHTLY llvm-cov --locked --branch --text --features complete 2>&1 | grep -E "Branch|Condition|^exit|error" | head -8 )

hr "12. TV-023 MSR-14 on the firmware workspace (the G6 command), twice"
for n in 1 2; do
  ( cd "$A/cwht/firmware" && RUSTFLAGS=-Zcoverage-options=condition run cargo +$NIGHTLY llvm-cov nextest --locked --workspace \
      --exclude cwht-app --profile ci --branch --json --output-path "$W/bc-run$n.json" 2>&1 | grep -E "Summary|error|^exit" | san )
done
$PY - "$W/bc-run1.json" "$W/bc-run2.json" <<'EOF'
import json, sys
def tot(p):
    t = json.load(open(p))["data"][0]["totals"]
    return {k: (t[k]["covered"], t[k]["count"]) for k in ("branches", "lines", "regions", "functions") if k in t}
a, b = tot(sys.argv[1]), tot(sys.argv[2])
print("  run 1 totals (covered, count):", a)
print("  run 2 totals equal to run 1:", a == b)
EOF

hr "13. TV-023 Miri (MSR-08, CS-03; non-credit): miri-kat clean, then seeded-oob"
( cd "$A/cwht/$FX/miri-kat"
  run cargo +$NIGHTLY miri test --locked --target-dir "$W/mi" 2>&1 | grep -E "test result|^exit" | tail -3
  run cargo +$NIGHTLY miri test --locked --features seeded-oob --target-dir "$W/mi" 2>&1 | grep -E "Undefined Behavior:|test tests::|error: test failed|^exit" | head -6 )

hr "14. TV-023 Miri on the gate G5 scope (rustos api host tests, cargo +$NIGHTLY miri test -p api --lib, layout A)"
( cd "$A/cwht/firmware" && run cargo +$NIGHTLY miri test --locked -p api --lib 2>&1 | grep -E "test result|error|^exit" | san )

hr "end $(date '+%H:%M:%S')"
