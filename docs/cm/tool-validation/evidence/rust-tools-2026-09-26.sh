#!/bin/sh
# tools/toolchain.lock.md section 1.1 sanity checks run after the SRR decision 109 installs
# (owner ruling 2026-09-26): the rows that were blocked on those installs, plus the rows of the
# other gate tools still reading "not yet run" (INSP-016 finding-1 exit criterion; run 2 report
# recommendation 4). A record of what was run, not a controlled tool (README "Evidence").
# Usage: rust-tools-2026-09-26.sh <scratch-dir> <guard-dir>
#   <guard-dir> holds the rustup shim of TC-SW-TOOL-001 run 3 deviation D13 (refuses component
#   add, toolchain install and self update), put first on PATH so no check can download.
# Every check runs on scratch copies; the repository fixtures are read only. Fixtures that do not
# exist under tools/tests/fixtures/ yet are written by this script into <scratch-dir> (listed
# below); committing them under tools/tests/fixtures/rust/ is the TV record's work (due PDR/CDR).
set -u
SP=$1; GUARD=$2
REPO=/Users/robinonsay/rust/cwht
PY=$REPO/.venv/bin/python
export PATH="$GUARD:$PATH" RUSTUP_AUTO_INSTALL=0 CARGO_NET_OFFLINE=true MIRI_AUTO_OPS=no CARGO_TERM_COLOR=never
TGT=thumbv8m.main-none-eabihf
W="$SP/sanity"; rm -rf "$W"; mkdir -p "$W"
hr() { echo; echo "================================================================ $*"; }
run() { echo "\$ $*"; "$@"; echo "exit=$?"; }

hr "identity $(date '+%Y-%m-%d %H:%M:%S %Z'), cwht HEAD $(git -C $REPO rev-parse HEAD)"
rustup --version 2>/dev/null; rustc +1.98.0 --version; cargo +1.98.0 --version; cargo +1.98.0 clippy --version
rustc +nightly-2026-08-24 --version; rust-code-analysis-cli --version; cargo audit --version; cargo deny --version
cargo llvm-cov --version; cargo nextest --version | head -1; cargo geiger --version; cargo size --version

# ------------------------------------------------------------------------------------------------
hr "1. rustc / cargo and clippy on the pinned toolchain 1.98.0 (lock section 1.3; fixture tools/tests/fixtures/rust/)"
cp -R $REPO/tools/tests/fixtures/rust "$W/rust"
( cd "$W/rust/kat-target"
  for n in 1 2; do run cargo +1.98.0 build --release --locked --target-dir "$W/t$n" 2>&1 | tail -3; done
  shasum -a 256 "$W/t1/$TGT/release/kat-target" "$W/t2/$TGT/release/kat-target" | sed "s|$W|<scratch>|"
  echo "stored elf_sha256: $($PY -c "import json;print(json.load(open('$REPO/tools/tests/fixtures/rust/known-answers.json'))['target_build']['elf_sha256'])")" )
( cd "$W/rust/kat-host"
  run cargo +1.98.0 test --locked --target-dir "$W/th" 2>&1 | grep -E "test result|^exit"
  run cargo +1.98.0 test --locked --features seeded-fail --target-dir "$W/th" 2>&1 | grep -E "test result|FAILED|panicked|^exit|seeded_failure" | head -6
  run cargo +1.98.0 clippy --locked --all-targets --target-dir "$W/th" -- -D warnings 2>&1 | grep -E "^error|^exit"
  run cargo +1.98.0 clippy --locked --all-targets --features seeded-lint --target-dir "$W/th" -- -D warnings 2>&1 | grep -E "^error|clippy::|^exit" | head -6
  run cargo +1.98.0 clippy --locked --all-targets --features seeded-unwrap --target-dir "$W/th" -- -D warnings 2>&1 | grep -E "^error|clippy::|^exit" | head -6 )

# ------------------------------------------------------------------------------------------------
hr "2. rust-code-analysis-cli end to end through tools/complexity_gate.py (07 section 8.3; TV-012 limitation 1)"
echo "Fixture: tools/tests/fixtures/complexity_gate/src (hand-computed CC in rca.json: straight 1, branchy 5,"
echo "at_limit 15, over_limit 16, with_closure, ping, pong, fact; app.rs target-only). Plus a scratch file"
echo "loops.rs for the question of TV-012 limitation 1 (is a bare loop a decision?)."
mkdir -p "$W/cc" && cp -R $REPO/tools/tests/fixtures/complexity_gate/src "$W/cc/src"
cat > "$W/cc/src/loops.rs" <<'EOF'
//! Scratch: bare loop, while loop, and an if for comparison (not a committed fixture).
pub fn bare_loop() -> ! {
    loop {}
}
pub fn one_if(x: u32) -> u32 {
    if x > 1 { 1 } else { 0 }
}
pub fn one_while(mut x: u32) -> u32 {
    while x > 1 { x -= 1; }
    x
}
EOF
( cd "$W/cc" && rust-code-analysis-cli --metrics --output-format json --paths src > rca-real.json; echo "rca exit=$?" )
$PY - "$W/cc/rca-real.json" "$REPO/tools/tests/fixtures/complexity_gate/rca.json" <<'EOF'
import sys
sys.path.insert(0, "/Users/robinonsay/rust/cwht/tools")
import complexity_gate as cg
def table(path):
    fs = cg.functions_of(cg.parse_stream(open(path, encoding="utf-8").read()))
    return {(f.file.split("/")[-1], f.name): f.cc for f in fs}
real, stored = table(sys.argv[1]), table(sys.argv[2])
print(f"{'file':10} {'function':14} {'analyzer':>8} {'stored':>7}  agree")
bad = 0
for key in sorted(set(real) | set(stored)):
    r, s = real.get(key), stored.get(key)
    ok = "yes" if r == s else ("n/a (scratch)" if s is None and key[0] == "loops.rs" else "NO")
    bad += ok == "NO"
    print(f"{key[0]:10} {key[1]:14} {str(r):>8} {str(s):>7}  {ok}")
print(f"disagreements with the stored hand-computed values: {bad}")
EOF
( cd "$W/cc" && run $PY $REPO/tools/complexity_gate.py --max 15 --input rca-real.json --root . 2>&1 )

# ------------------------------------------------------------------------------------------------
hr "3. nightly-2026-08-24 (MSR-14, non-credit): branch and condition coverage; Miri"
mkdir -p "$W/cond/src"
cat > "$W/cond/Cargo.toml" <<'EOF'
[package]
name = "cond-kat"
version = "0.0.0"
edition = "2024"
publish = false
[lib]
path = "src/lib.rs"
EOF
cat > "$W/cond/src/lib.rs" <<'EOF'
//! Seeded unexercised condition outcome: in `both`, `b` is never evaluated as false with `a` true.
pub fn both(a: bool, b: bool) -> u8 {
    if a && b { 1 } else { 0 }
}
#[cfg(test)]
mod tests {
    use super::both;
    #[test]
    fn true_true() { assert_eq!(both(true, true), 1); }
    #[test]
    fn false_any() { assert_eq!(both(false, true), 0); }
}
EOF
( cd "$W/cond" && CARGO_TARGET_DIR="$W/tc" RUSTFLAGS=-Zcoverage-options=condition run cargo +nightly-2026-08-24 llvm-cov --branch --text 2>&1 | tail -25 )
echo "Miri: not run. It needs the rust-src component and a sysroot build that fetches std's dependency crates"
echo "(probe of 2026-09-26 19:21, evidence rust-tools-2026-09-26.log.txt section 0); neither is in decision 109."

# ------------------------------------------------------------------------------------------------
hr "4. cargo-audit: seeded advisory lock against a clean lock (offline, --no-fetch)"
mkdir -p "$W/audit"
cat > "$W/audit/seeded.lock" <<'EOF'
version = 3

[[package]]
name = "kat"
version = "0.0.0"
dependencies = ["smallvec"]

[[package]]
name = "smallvec"
version = "1.6.0"
source = "registry+https://github.com/rust-lang/crates.io-index"
EOF
sed 's/version = "1.6.0"/version = "1.13.2"/' "$W/audit/seeded.lock" > "$W/audit/clean.lock"
grep -l 'patched' $HOME/.cargo/advisory-db/crates/smallvec/RUSTSEC-2021-0003.md >/dev/null && sed -n '/^\[versions\]/,/^$/p;/^id = /p;/^package = /p' $HOME/.cargo/advisory-db/crates/smallvec/RUSTSEC-2021-0003.md
( cd "$W/audit" && run cargo audit --no-fetch --no-yanked -f seeded.lock 2>&1 | grep -E "^(ID|Crate|Version|Title|error|warning)|vulnerabilit|^exit" )
( cd "$W/audit" && run cargo audit --no-fetch --no-yanked -f clean.lock 2>&1 | grep -E "^(ID|Crate|error)|vulnerabilit|^exit" )

# ------------------------------------------------------------------------------------------------
hr "5. cargo-deny: a policy allowing MIT only flags the seeded GPL-3.0-only crate and nothing else"
mkdir -p "$W/deny/seeded/src" "$W/deny/clean/src" "$W/deny/src"
cat > "$W/deny/Cargo.toml" <<'EOF'
[package]
name = "deny-kat"
version = "0.0.0"
edition = "2024"
license = "MIT"
publish = false
[dependencies]
seeded = { path = "seeded" }
clean = { path = "clean" }
[workspace]
EOF
for c in seeded clean; do
  l=MIT; [ $c = seeded ] && l=GPL-3.0-only
  printf '[package]\nname = "%s"\nversion = "0.1.0"\nedition = "2024"\nlicense = "%s"\n' $c $l > "$W/deny/$c/Cargo.toml"
  echo "//! $c" > "$W/deny/$c/src/lib.rs"
done
echo "//! root" > "$W/deny/src/lib.rs"
printf '[licenses]\nallow = ["MIT"]\nconfidence-threshold = 0.93\nprivate = { ignore = true }\n' > "$W/deny/deny.toml"
( cd "$W/deny" && cargo +1.98.0 generate-lockfile --offline >/dev/null 2>&1; run cargo deny --log-level error check licenses 2>&1 | grep -E "error\[|rejected|GPL|seeded|clean|^exit" | head -12 )

# ------------------------------------------------------------------------------------------------
hr "6. cargo-llvm-cov on the pinned 1.98.0 with its rustup-tracked llvm-tools: 100 percent, then a seeded uncovered branch"
mkdir -p "$W/cov/src"
printf '[package]\nname = "cov-kat"\nversion = "0.0.0"\nedition = "2024"\npublish = false\n' > "$W/cov/Cargo.toml"
cat > "$W/cov/src/lib.rs" <<'EOF'
//! Known answer: both arms exercised gives 100 percent; feature seeded-gap drops the else-arm test.
pub fn sign(x: i32) -> i32 {
    if x < 0 {
        -1
    } else {
        1
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn negative() { assert_eq!(super::sign(-5), -1); }
    #[cfg(not(feature = "seeded-gap"))]
    #[test]
    fn positive() { assert_eq!(super::sign(5), 1); }
}
EOF
printf '\n[features]\nseeded-gap = []\n' >> "$W/cov/Cargo.toml"
( cd "$W/cov" && export CARGO_TARGET_DIR="$W/tv" && run cargo +1.98.0 llvm-cov --summary-only --fail-under-lines 100 --fail-under-regions 100 2>&1 | tail -4 | tr -s ' ' | sed "s|$W|<scratch>|"
  run cargo +1.98.0 llvm-cov --features seeded-gap --text --fail-under-lines 100 --fail-under-regions 100 2>&1 | grep -E "^ +[0-9]+\| +0\||error|^exit" | head -8 )

# ------------------------------------------------------------------------------------------------
hr "7. cargo-nextest: failing test named, exit non-zero; clean run exit 0 with the stored count (fixture kat-host)"
( cd "$W/rust/kat-host"
  run cargo +1.98.0 nextest run --target-dir "$W/tn" --features seeded-fail 2>&1 | grep -E "FAIL \[|Summary|^exit"
  run cargo +1.98.0 nextest run --target-dir "$W/tn" 2>&1 | grep -E "Summary|^exit" )

# ------------------------------------------------------------------------------------------------
hr "8. cargo-geiger: a crate with one unsafe block reports exactly one unsafe expression and zero unsafe functions"
mkdir -p "$W/geiger/src"
printf '[package]\nname = "geiger-kat"\nversion = "0.0.0"\nedition = "2024"\npublish = false\n[workspace]\n' > "$W/geiger/Cargo.toml"
cat > "$W/geiger/src/lib.rs" <<'EOF'
//! Known answer: one unsafe block holding one unsafe expression (a raw pointer read), no unsafe fn.
pub fn read(x: &u32) -> u32 {
    let p: *const u32 = x;
    // SAFETY: p comes from a live reference.
    unsafe { *p }
}
EOF
( cd "$W/geiger" && cargo +1.98.0 generate-lockfile --offline >/dev/null 2>&1; run cargo +1.98.0 geiger --offline --manifest-path "$W/geiger/Cargo.toml" --output-format Ratio 2>&1 | grep -vE "^\s*$" | tail -12 )

# ------------------------------------------------------------------------------------------------
hr "9. cargo-binutils: cargo size section sizes equal the section sizes of the lld link map (cwht-app of TC-SW-TOOL-001 run 3)"
ELF=$REPO/docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf; MAP=$REPO/docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.map
rust-size -A "$ELF" | awk '$1 ~ /^\.(vector_table|boot_info|text|rodata|data|bss)$/ {print $1, $2}' > "$W/size.txt"
$PY - "$MAP" "$W/size.txt" <<'EOF'
import re, sys
mp = {}
for line in open(sys.argv[1], encoding="utf-8"):
    m = re.match(r"^\s*([0-9a-f]+)\s+([0-9a-f]+)\s+([0-9a-f]+)\s+\d+ (\.[^ ]+)$", line.rstrip("\n"))
    if m and m.group(4) in (".vector_table", ".boot_info", ".text", ".rodata", ".data", ".bss"):
        mp[m.group(4)] = int(m.group(3), 16)
size = dict((l.split()[0], int(l.split()[1])) for l in open(sys.argv[2]))
bad = 0
for k in sorted(mp):
    ok = size.get(k) == mp[k]; bad += not ok
    print(f"{k:14} map {mp[k]:6}  cargo size {size.get(k)!s:6}  {'equal' if ok else 'DIFFER'}")
print(f"sections compared {len(mp)}, differing {bad}")
EOF
hr "end $(date '+%H:%M:%S')"
