#!/bin/sh
# TC-SW-TOOL-001 run 3, steps 1 to 6 and 8 to 10 (step 7 is gate-known-answer.sh).
# Usage: run3.sh <scratch-dir> <report-artifact-dir>
# Layout built in <scratch-dir>/r3 (removed by the caller afterwards):
#   r3/cwht    git archive of cwht HEAD (committed content only), .venv linked
#   r3/rustos  symbolic link to the rustos worktree /Users/robinonsay/rust/rustos-wp-sw-licence
#              (branch cwht/wp-sw-licence-manifest-safety); firmware/Cargo.toml is unchanged, its
#              ../../rustos path dependency resolves through the link
#   r3/cwht/tools/toolchain.lock.md: the rustos row names the branch commit instead of the pin
#              (temporary copy only; the repository lock is not changed; deviation D12)
# No download: RUSTUP_AUTO_INSTALL=0, CARGO_NET_OFFLINE=true, MIRI_AUTO_OPS=no, and a rustup shim
# first on PATH that refuses component add, toolchain install and self update (deviation D13).
set -u
SP=$1; OUT=$2
SRC=/Users/robinonsay/rust/cwht
WT=/Users/robinonsay/rust/rustos-wp-sw-licence
GUARD="$SP/guard"
export PATH="$GUARD:$PATH" RUSTUP_AUTO_INSTALL=0 CARGO_NET_OFFLINE=true MIRI_AUTO_OPS=no CARGO_TERM_COLOR=never
TGT=thumbv8m.main-none-eabihf
R="$SP/r3"; C="$R/cwht"; FW="$C/firmware"
BRANCH_COMMIT=$(git -C "$WT" rev-parse HEAD)
PIN=$(git -C /Users/robinonsay/rust/rustos rev-parse HEAD)
mkdir -p "$OUT"

# ------------------------------------------------------------------ layout
rm -rf "$R"; mkdir -p "$C"
git -C "$SRC" archive HEAD | tar -x -C "$C"
ln -s "$SRC/.venv" "$C/.venv"
ln -s "$WT" "$R/rustos"
sed -i '' "s/\`$PIN\` (\`c54d35a\`, \"Fix build\")/\`$BRANCH_COMMIT\` (\`$(echo $BRANCH_COMMIT | cut -c1-7)\`, branch cwht\/wp-sw-licence-manifest-safety, TC-SW-TOOL-001 run 3 temporary copy)/" "$C/tools/toolchain.lock.md"

# ------------------------------------------------------------------ step 1
{
echo "# TC-SW-TOOL-001 run 3: configuration record ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "## cwht (git archive of HEAD into the temporary layout; committed content only)"
git -C "$SRC" rev-parse HEAD
echo "## blobs as run (git rev-parse HEAD:<path>)"
for p in tools/sw_gate.sh tools/measurements.py tools/unsafe_audit.py tools/complexity_gate.py tools/emu_run.sh tools/toolchain.lock.md docs/test_cases/sw-tool/test_cases.json firmware/Cargo.toml firmware/Cargo.lock firmware/deny.toml firmware/rust-toolchain.toml firmware/cwht-app/src/main.rs firmware/unsafe-audit.md; do
  echo "$(git -C "$SRC" rev-parse HEAD:$p)  $p"
done
echo "## temporary lock copy: the only difference from HEAD (the rustos row, deviation D12)"
git -C "$SRC" show HEAD:tools/toolchain.lock.md | diff - "$C/tools/toolchain.lock.md"
echo "(diff exit $?)"
echo "## rustos: $R/rustos -> $(readlink "$R/rustos")"
echo "branch $(git -C "$WT" rev-parse --abbrev-ref HEAD), HEAD $BRANCH_COMMIT; parent $(git -C "$WT" rev-parse HEAD~1) (the lock pin $PIN)"
echo "status of api/ firmware/ Cargo.toml Cargo.lock .cargo LICENSE (empty = clean):"
git -C "$WT" status --porcelain -- api firmware Cargo.toml Cargo.lock .cargo LICENSE
echo "(end of status)"
echo "owner checkout /Users/robinonsay/rust/rustos: HEAD $PIN (unchanged; its working tree not read or written)"
echo "## toolchain in firmware/ (firmware/rust-toolchain.toml pin 1.98.0, installed under SRR decision 109)"
(cd "$FW" && rustup show active-toolchain && rustc --version && cargo --version && cargo clippy --version && rustfmt --version)
rustup --version 2>/dev/null
rustup toolchain list
rustup target list --installed --toolchain 1.98.0
echo "## 1.98.0 components"; rustup component list --installed --toolchain 1.98.0
echo "## nightly-2026-08-24 components"; rustup component list --installed --toolchain nightly-2026-08-24
echo "## cargo tools"
cargo nextest --version | head -1; cargo llvm-cov --version; cargo audit --version; cargo deny --version; cargo geiger --version; cargo size --version
rust-code-analysis-cli --version
echo "## RustSec databases"
git -C "$HOME/.cargo/advisory-db" log -1 --format='~/.cargo/advisory-db %H %cI'
for d in "$HOME"/.cargo/advisory-dbs/*/; do git -C "$d" log -1 --format="$d %H %cI"; done
echo "## picotool"; picotool version
} > "$OUT/versions.txt" 2>&1

# ------------------------------------------------------------------ steps 2 and 3
{
echo "# host build and test, run 3 ($(date '+%Y-%m-%d %H:%M %Z')), firmware/ of the temporary layout"
echo '$ cargo build'; (cd "$FW" && cargo build 2>&1); echo "exit=$?"
echo '$ cargo test'; (cd "$FW" && cargo test 2>&1); echo "exit=$?"
} > "$OUT/host-build-test.txt" 2>&1

# ------------------------------------------------------------------ audit list for the branch (CS-07)
{
echo "# unsafe audit list regenerated for the branch in the temporary layout ($(date '+%Y-%m-%d %H:%M %Z'))"
echo '$ tools/unsafe_audit.py --check   (committed list, before regeneration)'
(cd "$C" && .venv/bin/python tools/unsafe_audit.py --check 2>&1); echo "exit=$?"
echo '$ tools/unsafe_audit.py --write'
(cd "$C" && .venv/bin/python tools/unsafe_audit.py --write 2>&1); echo "exit=$?"
echo '$ tools/unsafe_audit.py --check'
(cd "$C" && .venv/bin/python tools/unsafe_audit.py --check 2>&1); echo "exit=$?"
echo "## regenerated firmware/unsafe-audit.md (temporary copy; git hash-object $(git hash-object "$FW/unsafe-audit.md"))"
cat "$FW/unsafe-audit.md"
} > "$OUT/unsafe-audit.txt" 2>&1

# ------------------------------------------------------------------ step 6 (steps 4 and 5 inside)
(cd "$C" && sh tools/sw_gate.sh; echo "sw_gate exit status: $?") > "$OUT/sw-gate-full.txt" 2>&1
(cd "$C" && sh tools/sw_gate.sh --keep-going; echo "sw_gate exit status: $?") > "$OUT/sw-gate-keep-going.txt" 2>&1
cp "$FW/target/$TGT/release/cwht-app" "$OUT/cwht-app.elf"
cp "$FW/target/$TGT/release/cwht-app.map" "$OUT/cwht-app.map"

# ------------------------------------------------------------------ step 4 identity (D9 of run 2)
{
echo "# cwht-app rebuild identity, run 3 ($(date '+%Y-%m-%d %H:%M %Z'))"
for n in 1 2; do
  echo "## Clean build $n: CARGO_TARGET_DIR=<scratch>/cwht-app-t$n cargo build -p cwht-app --release --target $TGT"
  rm -rf "$SP/cwht-app-t$n"
  (cd "$FW" && CARGO_TARGET_DIR="$SP/cwht-app-t$n" cargo build -p cwht-app --release --target $TGT 2>&1); echo "exit=$?"
done
echo "## SHA-256 (clean build 1, clean build 2, gate G2 build, run 2 cwht-app.elf)"
shasum -a 256 "$SP/cwht-app-t1/$TGT/release/cwht-app" "$SP/cwht-app-t2/$TGT/release/cwht-app" "$FW/target/$TGT/release/cwht-app" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app.elf" | sed "s|$SP|<scratch>|; s|$SRC/||"
echo "## Loadable sections: rust-objcopy -O binary, then SHA-256 (gate build of run 3, and run 2)"
for s in .vector_table .boot_info .text .rodata .data; do
  a=$(rust-objcopy -O binary --only-section=$s "$FW/target/$TGT/release/cwht-app" "$SP/a.bin" && shasum -a 256 "$SP/a.bin" | cut -d' ' -f1)
  b=$(rust-objcopy -O binary --only-section=$s "$SRC/docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app.elf" "$SP/b.bin" && shasum -a 256 "$SP/b.bin" | cut -d' ' -f1)
  eq=differ; [ "$a" = "$b" ] && eq=identical
  echo "$s run3 $a run2 $b $eq"
done
echo "## rust-size -A (gate build of run 3)"
rust-size -A "$FW/target/$TGT/release/cwht-app" | sed "s|$FW/||"
} > "$OUT/cwht-app-build.txt" 2>&1

# ------------------------------------------------------------------ step 8
B="$SP/rustos-blinky-r3"; rm -rf "$B"; cp -R "$WT/templates/pico2" "$B"
sed -i '' 's/{{project-name}}/blinky/' "$B/Cargo.toml"
sed -i '' "s|api = { git = \"https://github.com/robinonsay/rustos\" }|api = { path = \"$WT/api\" }|; s|pico2 = { git = \"https://github.com/robinonsay/rustos\" }|pico2 = { path = \"$WT/firmware/pico2\" }|" "$B/Cargo.toml"
{
echo "# Fresh rustos blinky build, run 3 ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "Source: $WT/templates/pico2 at branch commit $BRANCH_COMMIT, copied to a scratch directory; CARGO_NET_OFFLINE=true."
echo "## Template diff (package name and the two dependency lines, git form replaced by the local path form of templates/README.md, pointed at the worktree)"
diff "$WT/templates/pico2/Cargo.toml" "$B/Cargo.toml"; echo "(diff exit $?)"
echo "## rustc (default toolchain, no pin in the template):"; (cd "$B" && rustc --version)
for n in 1 2; do
  echo "## Build $n: cargo build --release --target-dir target-r$n"
  (cd "$B" && cargo build --release --target-dir "target-r$n" 2>&1); echo "exit=$?"
done
echo "## SHA-256 (build 1, build 2, run 2 rustos-blinky.elf)"
shasum -a 256 "$B/target-r1/$TGT/release/blinky" "$B/target-r2/$TGT/release/blinky" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r2/rustos-blinky.elf" | sed "s|$SP|<scratch>|; s|$SRC/||"
echo "## Loadable sections against run 2"
for s in .vector_table .boot_info .text .rodata .data; do
  a=$(rust-objcopy -O binary --only-section=$s "$B/target-r1/$TGT/release/blinky" "$SP/a.bin" && shasum -a 256 "$SP/a.bin" | cut -d' ' -f1)
  b=$(rust-objcopy -O binary --only-section=$s "$SRC/docs/vv/reports/TC-SW-TOOL-001-r2/rustos-blinky.elf" "$SP/b.bin" && shasum -a 256 "$SP/b.bin" | cut -d' ' -f1)
  eq=differ; [ "$a" = "$b" ] && eq=identical
  echo "$s run3 $a run2 $b $eq"
done
} > "$OUT/blinky-build.txt" 2>&1
cp "$B/target-r1/$TGT/release/blinky" "$OUT/rustos-blinky.elf"

# ------------------------------------------------------------------ step 9
{
echo "# UF2 conversion and file inspection, run 3 ($(date '+%Y-%m-%d %H:%M %Z')); picotool $(picotool version)"
for n in rustos-blinky cwht-app; do
  echo "## $n: picotool uf2 convert $n.elf $n.uf2 --family rp2350-arm-s"
  (cd "$OUT" && picotool uf2 convert "$n.elf" "$n.uf2" --family rp2350-arm-s 2>&1); echo "exit=$?"
  echo "## $n: picotool info -a $n.uf2"
  (cd "$OUT" && picotool info -a "$n.uf2" 2>&1); echo "exit=$?"
done
echo "## SHA-256 of the run 3 UF2 files and the run 2 UF2 files"
shasum -a 256 "$OUT/rustos-blinky.uf2" "$OUT/cwht-app.uf2" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r2/rustos-blinky.uf2" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app.uf2" | sed "s|$SRC/||"
} > "$OUT/uf2-info.txt" 2>&1

# ------------------------------------------------------------------ step 10
{
echo "# Blink-rate prediction, run 3 ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "The run 2 prediction (docs/vv/reports/TC-SW-TOOL-001-r2/blink-rate-prediction.txt) holds for run 3 when the"
echo "executable bytes are unchanged. .text of both images against run 2 (from cwht-app-build.txt and blinky-build.txt):"
grep '^\.text ' "$OUT/cwht-app-build.txt" | sed 's/^/cwht-app /'
grep '^\.text ' "$OUT/blinky-build.txt" | sed 's/^/rustos-blinky /'
echo "## delay loops (rust-objdump -d, spin_loop call sites), run 3"
for e in cwht-app rustos-blinky; do
  echo "### $e"; rust-objdump -d --no-show-raw-insn "$OUT/$e.elf" | grep -B2 -A2 -i 'yield\|spin' | head -30
done
} > "$OUT/blink-rate-prediction.txt" 2>&1
echo "run3.sh done $(date '+%H:%M:%S')"
