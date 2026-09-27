#!/bin/sh
# Known-answer runs 3 and 4 of TV-020 (rustc, cargo, clippy 1.98.0) and TV-021 (cargo-llvm-cov),
# WP-PDR-08, after review INSP-040 iteration 1 (docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md).
# A record of what was run, not a controlled tool (docs/cm/tool-validation/README.md "Evidence").
# Derived from rust-tv-2026-09-27.sh (runs 1 and 2) sections 0 to 8; changes:
#   section 0  also prints the blob of pdr-known-answers.json (changed for findings 1 and 2);
#   sections 4 and 5  (K20-4, K20-5; INSP-040 finding-1) the pass criteria are mechanical: two clean
#              builds at one absolute path give byte-identical ELF files and loadable images (cmp),
#              printed as PASS or FAIL lines; the layout B build and the reference are compared and
#              reported as OBSERVATION lines (loadable image, rust-size -A section table), never as a
#              pass criterion;
#   section 7  (K21-4; INSP-040 finding-2) the lcov export of cov-kat --features seeded-gap is checked
#              against the stored answer of pdr-known-answers.json cov-kat.seeded-gap-lcov, and read
#              by tools/measurements.py --coverage.
# Sections 9 to 14 of the first procedure (TV-022, TV-023) are not repeated: their triggers name only
# the harness-seeded, cond-kat and miri-kat sections of pdr-known-answers.json, which did not change.
#
# Usage: rust-tv-2026-09-27-r3.sh <scratch-dir> <guard-dir> <commit>
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
# Mechanical pass criterion (INSP-040 finding-1): PASS only when both files exist, are non-empty and cmp equal.
chk() { if [ -s "$2" ] && [ -s "$3" ] && cmp -s "$2" "$3"; then echo "$1 PASS"; else echo "$1 FAIL"; fi; }
# Observation, never a pass criterion: equal or differs.
obs() { if cmp -s "$2" "$3"; then echo "OBSERVATION $1: equal"; else echo "OBSERVATION $1: differs"; fi; }
# Allocated sections (name and size; address non-zero) of an ELF, by rust-size -A.
sect() { rust-size -A "$1" | awk 'NF == 3 && $3 ~ /^[0-9]+$/ && $3 != 0 { print $1, $2 }'; }

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
for p in kat-target kat-host cov-kat cond-kat miri-kat harness-seeded known-answers.json pdr-known-answers.json; do
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

hr "4. TV-020 rustos blinky (07 sections 8.3 and 17.3): templates/pico2 of the pin, two clean builds at one absolute path (pass criterion), a build at a second path and the reference (observations)"
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
BREF="$W/blinky-reference.elf"; cp "$A/cwht/docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf" "$BREF"
sha "$W/b1/$TGT/release/blinky" "$W/b2/$TGT/release/blinky" "$W/b3/$TGT/release/blinky" "$BREF"
echo "loadable image (rust-objcopy -O binary; SHA-256 and size in bytes):"
for f in "$W/b1/$TGT/release/blinky" "$W/b2/$TGT/release/blinky" "$W/b3/$TGT/release/blinky" "$BREF"; do
  rust-objcopy -O binary "$f" "$f.bin"; echo "$(sha "$f.bin")  $(wc -c < "$f.bin" | tr -d ' ') B"
done
echo "pass criteria (same absolute path, layout A, target directories b1 and b2):"
chk "K20-4a same-path ELF byte-identical" "$W/b1/$TGT/release/blinky" "$W/b2/$TGT/release/blinky"
chk "K20-4b same-path loadable image byte-identical" "$W/b1/$TGT/release/blinky.bin" "$W/b2/$TGT/release/blinky.bin"
echo "observations (not pass criteria; TV-020 limitation 1):"
for f in "$W/b1/$TGT/release/blinky" "$W/b3/$TGT/release/blinky" "$BREF"; do sect "$f" > "$f.sect"; done
echo "  allocated sections of the layout A build (rust-size -A):"; sed 's/^/    /' "$W/b1/$TGT/release/blinky.sect"
obs "K20-4 layout B loadable image against layout A" "$W/b1/$TGT/release/blinky.bin" "$W/b3/$TGT/release/blinky.bin"
obs "K20-4 reference loadable image against layout A" "$W/b1/$TGT/release/blinky.bin" "$BREF.bin"
obs "K20-4 layout B section table against layout A" "$W/b1/$TGT/release/blinky.sect" "$W/b3/$TGT/release/blinky.sect"
obs "K20-4 reference section table against layout A" "$W/b1/$TGT/release/blinky.sect" "$BREF.sect"

hr "5. TV-020 MSR-28 (07 section 11.2): cwht-app release, two clean builds at one absolute path (pass criterion), a build at a second path and the reference (observations)"
( cd "$A/cwht/firmware" && run cargo +1.98.0 build -p cwht-app --release --locked --target $TGT --target-dir "$W/a1" 2>&1 | grep -E "Finished|warning: unused|error|^exit" | san
  run cargo +1.98.0 build -p cwht-app --release --locked --target $TGT --target-dir "$W/a2" 2>&1 | grep -E "Finished|error|^exit" | san )
( cd "$B/cwht/firmware" && run cargo +1.98.0 build -p cwht-app --release --locked --target $TGT --target-dir "$W/a3" 2>&1 | grep -E "Finished|error|^exit" | san )
AREF="$W/cwht-app-reference.elf"; cp "$A/cwht/docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf" "$AREF"
sha "$W/a1/$TGT/release/cwht-app" "$W/a2/$TGT/release/cwht-app" "$W/a3/$TGT/release/cwht-app" "$AREF"
echo "firmware/ differences between the r3 build commit 0bcea39 and the commit tested:"
git -C "$REPO" diff --stat 0bcea39 "$COMMIT" -- firmware | tail -3
echo "loadable image (rust-objcopy -O binary; SHA-256 and size in bytes):"
for f in "$W/a1/$TGT/release/cwht-app" "$W/a2/$TGT/release/cwht-app" "$W/a3/$TGT/release/cwht-app" "$AREF"; do
  rust-objcopy -O binary "$f" "$f.bin"; echo "$(sha "$f.bin")  $(wc -c < "$f.bin" | tr -d ' ') B"
done
echo "pass criteria (same absolute path, layout A, target directories a1 and a2):"
chk "K20-5a same-path ELF byte-identical" "$W/a1/$TGT/release/cwht-app" "$W/a2/$TGT/release/cwht-app"
chk "K20-5b same-path loadable image byte-identical" "$W/a1/$TGT/release/cwht-app.bin" "$W/a2/$TGT/release/cwht-app.bin"
echo "observations (not pass criteria; TV-020 limitation 1):"
for f in "$W/a1/$TGT/release/cwht-app" "$W/a3/$TGT/release/cwht-app" "$AREF"; do sect "$f" > "$f.sect"; done
echo "  allocated sections of the layout A build (rust-size -A):"; sed 's/^/    /' "$W/a1/$TGT/release/cwht-app.sect"
obs "K20-5 layout B loadable image against layout A" "$W/a1/$TGT/release/cwht-app.bin" "$W/a3/$TGT/release/cwht-app.bin"
obs "K20-5 reference loadable image against layout A" "$W/a1/$TGT/release/cwht-app.bin" "$AREF.bin"
obs "K20-5 layout B section table against layout A" "$W/a1/$TGT/release/cwht-app.sect" "$W/a3/$TGT/release/cwht-app.sect"
obs "K20-5 reference section table against layout A" "$W/a1/$TGT/release/cwht-app.sect" "$AREF.sect"
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
hr "7. TV-021 cargo-llvm-cov (stable 1.98.0, llvm-tools of the pin): cov-kat 100 percent, then seeded-gap (text and lcov)"
( cd "$A/cwht/$FX/cov-kat" && export CARGO_TARGET_DIR="$W/cv"
  run cargo +1.98.0 llvm-cov --locked --summary-only --fail-under-lines 100 --fail-under-regions 100 2>&1 | tail -3 | tr -s ' ' | san
  run cargo +1.98.0 llvm-cov --locked --features seeded-gap --text --fail-under-lines 100 --fail-under-regions 100 2>&1 | grep -E "^ +[0-9]+\| +0\||error|^exit" | head -8 | san
  echo "---- K21-4 (INSP-040 finding-2): lcov export of the seeded gap"
  run cargo +1.98.0 llvm-cov --locked --features seeded-gap --lcov --output-path "$W/cov-gap.info" 2>&1 | grep -E "error|^exit" | san )
echo "lcov records (SF path reduced to the fixture-relative path):"
sed -e "s|^SF:.*/cov-kat/|SF:<export>/cov-kat/|" "$W/cov-gap.info" | grep -E "^(SF|DA|LF|LH|FNF|FNH):" | sed 's/^/  /'
echo "tools/measurements.py --coverage on it (TV-013, developer evidence until ACC-MEASURE-001):"
$PY "$A/cwht/tools/measurements.py" --coverage "$W/cov-gap.info" > "$W/cov-gap.msr" 2>&1; echo "exit=$?"
sed 's/^/  /' "$W/cov-gap.msr" | san
$PY - "$A/cwht/$FX/pdr-known-answers.json" "$W/cov-gap.info" "$W/cov-gap.msr" <<'EOF'
import json, sys
k = json.load(open(sys.argv[1]))["cov-kat"]["seeded-gap-lcov"]
lcov = [l.strip() for l in open(sys.argv[2])]
msr = open(sys.argv[3]).read()
lf = [int(l[3:]) for l in lcov if l.startswith("LF:")]
lh = [int(l[3:]) for l in lcov if l.startswith("LH:")]
zero = [l for l in lcov if l.startswith("DA:") and l.endswith(",0")]
checks = [
    ("K21-4a zero-count DA lines equal to the stored list " + str(k["da_zero"]), zero == k["da_zero"]),
    (f"K21-4b LF equal to the stored {k['lf']}", lf == [k["lf"]]),
    (f"K21-4c LH equal to the stored {k['lh']}", lh == [k["lh"]]),
    (f"K21-4d measurements.py --coverage prints '{k['measurements_line_contains']}'", k["measurements_line_contains"] in msr),
]
for name, ok in checks:
    print(f"{name} {'PASS' if ok else 'FAIL'}")
EOF

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
hr "end $(date '+%H:%M:%S')"
