#!/bin/sh
# TC-SW-TOOL-001 run 6, steps 1 to 6 and 8 to 10 (step 7 is gate-known-answer.sh).
# Usage: run6.sh <scratch-dir> <report-artifact-dir> <cwht-commit>
# Layout built in <scratch-dir>/r6 (removed by the caller afterwards):
#   r6/cwht            git archive of cwht <cwht-commit> (committed content only), .venv linked
#   r6/rustos-export   git archive of rustos 2ec64c0 (the clean export of CR-004 and the lock row)
#   r6/rustos          local clone of the owner's rustos repository (objects only, --no-hardlinks),
#                      checked out detached at 2ec64c0; its tree is compared with r6/rustos-export
#                      (diff -r, .git excluded) and must be identical. The clone gives gate G0 the
#                      commit identity it reads with git rev-parse HEAD (deviation D20).
#   firmware/Cargo.toml is unchanged; its ../../rustos path dependency resolves to r6/rustos.
# The lock copy is the committed lock (its rustos row is 2ec64c0 from CR-004); no temporary edit.
# No download: RUSTUP_AUTO_INSTALL=0, CARGO_NET_OFFLINE=true, MIRI_AUTO_OPS=no, stdin from
# /dev/null, and the run 3 rustup shim first on PATH (rustup-guard.sh, deviation D13 of run 3).
set -u
SP=$1; OUT=$2; COMMIT=$3
SRC=/Users/robinonsay/rust/cwht
OWNER_RUSTOS=/Users/robinonsay/rust/rustos
PIN=2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c
GUARD="$SP/guard6"
mkdir -p "$GUARD"; cp "$OUT/rustup-guard.sh" "$GUARD/rustup"; chmod +x "$GUARD/rustup"
export PATH="$GUARD:$PATH" RUSTUP_AUTO_INSTALL=0 CARGO_NET_OFFLINE=true MIRI_AUTO_OPS=no CARGO_TERM_COLOR=never
TGT=thumbv8m.main-none-eabihf
R="$SP/r6"; C="$R/cwht"; FW="$C/firmware"; RO="$R/rustos"
R3="$SRC/docs/vv/reports/TC-SW-TOOL-001-r3"
R5="$SRC/docs/vv/reports/TC-SW-TOOL-001-r5"
mkdir -p "$OUT"

# ------------------------------------------------------------------ layout
rm -rf "$R"; mkdir -p "$C" "$R/rustos-export"
git -C "$SRC" archive "$COMMIT" | tar -x -C "$C"
ln -s "$SRC/.venv" "$C/.venv"
git -C "$OWNER_RUSTOS" archive "$PIN" | tar -x -C "$R/rustos-export"
git clone --quiet --no-hardlinks --no-checkout "$OWNER_RUSTOS" "$RO"
git -C "$RO" checkout --quiet --detach "$PIN"

# ------------------------------------------------------------------ step 1
{
echo "# TC-SW-TOOL-001 run 6: configuration record ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "## cwht (git archive of $COMMIT into the layout; committed content only)"
echo "$COMMIT"
echo "## blobs as run (git rev-parse $COMMIT:<path>)"
for p in tools/sw_gate.sh tools/measurements.py tools/unsafe_audit.py tools/complexity_gate.py tools/emu_run.sh tools/toolchain.lock.md docs/test_cases/sw-tool/test_cases.json firmware/Cargo.toml firmware/Cargo.lock firmware/deny.toml firmware/rust-toolchain.toml firmware/cwht-app/src/main.rs firmware/unsafe-audit.md; do
  echo "$(git -C "$SRC" rev-parse $COMMIT:$p)  $p"
done
echo "## lock copy in the layout against the commit (no temporary edit; empty diff expected)"
git -C "$SRC" show $COMMIT:tools/toolchain.lock.md | diff - "$C/tools/toolchain.lock.md"
echo "(diff exit $?)"
echo "## lock rustos row: the pinned commit G0 reads"
sed -n 's/^| `rustos` .* | `\([0-9a-f]\{40\}\)` .*/\1/p' "$C/tools/toolchain.lock.md"
echo "## rustos"
echo "owner repository $OWNER_RUSTOS: rev-parse master $(git -C "$OWNER_RUSTOS" rev-parse master) (its working tree neither read nor written)"
echo "export: git -C $OWNER_RUSTOS archive $PIN | tar -x -C <scratch>/r6/rustos-export"
echo "clone:  git clone --no-hardlinks --no-checkout $OWNER_RUSTOS <scratch>/r6/rustos; checkout --detach $PIN"
echo "clone HEAD $(git -C "$RO" rev-parse HEAD); parent $(git -C "$RO" rev-parse HEAD~1)"
echo "clone status of api/ firmware/ Cargo.toml Cargo.lock .cargo LICENSE (empty = clean):"
git -C "$RO" status --porcelain -- api firmware Cargo.toml Cargo.lock .cargo LICENSE
echo "(end of status)"
echo "## clone tree against the export (diff -r, .git excluded; empty = identical)"
diff -r -x .git "$RO" "$R/rustos-export"
echo "(diff exit $?)"
echo "files in export: $(cd "$R/rustos-export" && find . -type f | wc -l | tr -d ' '); files in clone outside .git: $(cd "$RO" && find . -path ./.git -prune -o -type f -print | wc -l | tr -d ' ')"
echo "## toolchain in firmware/ (firmware/rust-toolchain.toml pin 1.98.0, SRR decision 109)"
(cd "$FW" && rustup show active-toolchain && rustc --version && cargo --version && cargo clippy --version && rustfmt --version)
rustup --version 2>/dev/null
echo "auto-self-update (close-out item 3): $(grep -s auto_self_update "$HOME/.rustup/settings.toml" || echo 'not set in settings.toml')"
rustup toolchain list
rustup target list --installed --toolchain 1.98.0
echo "## 1.98.0 components"; rustup component list --installed --toolchain 1.98.0
echo "## nightly-2026-08-24 components (rust-src from close-out item 2)"; rustup component list --installed --toolchain nightly-2026-08-24
echo "## Miri sysroot (close-out item 2)"; ls -d "$HOME/Library/Caches/org.rust-lang.miri"/* 2>&1
echo "## cargo tools"
cargo nextest --version | head -1; cargo llvm-cov --version; cargo audit --version; cargo deny --version; cargo geiger --version; cargo size --version
rust-code-analysis-cli --version
cargo +nightly-2026-08-24 miri --version
echo "## RustSec databases"
git -C "$HOME/.cargo/advisory-db" log -1 --format='~/.cargo/advisory-db %H %cI'
for d in "$HOME"/.cargo/advisory-dbs/*/; do git -C "$d" log -1 --format="$d %H %cI"; done
echo "## picotool"; picotool version
echo "## python (close-out item 12: brew pin python@3.13)"; "$C/.venv/bin/python" --version; brew list --pinned 2>/dev/null
} > "$OUT/versions.txt" 2>&1 </dev/null

# ------------------------------------------------------------------ steps 2 and 3
{
echo "# host build and test, run 6 ($(date '+%Y-%m-%d %H:%M %Z')), firmware/ of the layout"
echo '$ cargo build'; (cd "$FW" && cargo build 2>&1); echo "exit=$?"
echo '$ cargo test'; (cd "$FW" && cargo test 2>&1); echo "exit=$?"
} > "$OUT/host-build-test.txt" 2>&1 </dev/null

# ------------------------------------------------------------------ committed audit list against the pin (CR-004)
{
echo "# unsafe audit of the committed firmware/unsafe-audit.md against rustos $PIN ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "committed list blob $(git -C "$SRC" rev-parse $COMMIT:firmware/unsafe-audit.md); layout copy hash-object $(git hash-object "$FW/unsafe-audit.md")"
echo '$ tools/unsafe_audit.py --check'
(cd "$C" && .venv/bin/python tools/unsafe_audit.py --check 2>&1); echo "exit=$?"
echo '$ tools/unsafe_audit.py --check --gate SRR'
(cd "$C" && .venv/bin/python tools/unsafe_audit.py --check --gate SRR 2>&1); echo "exit=$?"
} > "$OUT/unsafe-audit.txt" 2>&1 </dev/null

# ------------------------------------------------------------------ step 6 (steps 4 and 5 inside)
(cd "$C" && sh tools/sw_gate.sh; echo "sw_gate exit status: $?") > "$OUT/sw-gate-full.txt" 2>&1 </dev/null
cp "$FW/target/$TGT/release/cwht-app" "$OUT/cwht-app.elf"
cp "$FW/target/$TGT/release/cwht-app.map" "$OUT/cwht-app.map"
(cd "$C" && sh tools/sw_gate.sh --keep-going; echo "sw_gate exit status: $?") > "$OUT/sw-gate-keep-going.txt" 2>&1 </dev/null
cmp "$FW/target/$TGT/release/cwht-app" "$OUT/cwht-app.elf" > "$OUT/.elf-cmp" 2>&1; echo "cmp gate-full ELF vs keep-going ELF exit $?" >> "$OUT/.elf-cmp"

# ------------------------------------------------------------------ step 4 identity (D9)
{
echo "# cwht-app rebuild identity, run 6 ($(date '+%Y-%m-%d %H:%M %Z'))"
cat "$OUT/.elf-cmp"
for n in 1 2; do
  echo "## Clean build $n: CARGO_TARGET_DIR=<scratch>/r6-app-t$n cargo build -p cwht-app --release --target $TGT"
  rm -rf "$SP/r6-app-t$n"
  (cd "$FW" && CARGO_TARGET_DIR="$SP/r6-app-t$n" cargo build -p cwht-app --release --target $TGT 2>&1); echo "exit=$?"
done
echo "## SHA-256 (clean build 1, clean build 2, gate G2 build (stopping run), run 5 cwht-app.elf)"
shasum -a 256 "$SP/r6-app-t1/$TGT/release/cwht-app" "$SP/r6-app-t2/$TGT/release/cwht-app" "$OUT/cwht-app.elf" "$R5/cwht-app.elf" | sed "s|$SP|<scratch>|; s|$SRC/||"
echo "## Loadable sections: rust-objcopy -O binary, then SHA-256 (gate build of run 6, and run 5)"
for s in .vector_table .boot_info .text .rodata .data; do
  a=$(rust-objcopy -O binary --only-section=$s "$OUT/cwht-app.elf" "$SP/r6a.bin" && shasum -a 256 "$SP/r6a.bin" | cut -d' ' -f1)
  b=$(rust-objcopy -O binary --only-section=$s "$R5/cwht-app.elf" "$SP/r6b.bin" && shasum -a 256 "$SP/r6b.bin" | cut -d' ' -f1)
  eq=differ; [ "$a" = "$b" ] && eq=identical
  echo "$s run6 $a run5 $b $eq"
done
echo "## cmp of the run 6 and run 5 ELF files (first differences, if any)"
cmp -l "$OUT/cwht-app.elf" "$R5/cwht-app.elf" | head -5; echo "(cmp listing end)"
echo "## rust-size -A (gate build of run 6)"
rust-size -A "$OUT/cwht-app.elf" | sed "s|$OUT/||"
} > "$OUT/cwht-app-build.txt" 2>&1 </dev/null
rm -f "$OUT/.elf-cmp"

# ------------------------------------------------------------------ step 8
B="$SP/r6-blinky"; rm -rf "$B"; cp -R "$RO/templates/pico2" "$B"
sed -i '' 's/{{project-name}}/blinky/' "$B/Cargo.toml"
sed -i '' "s|api = { git = \"https://github.com/robinonsay/rustos\" }|api = { path = \"$RO/api\" }|; s|pico2 = { git = \"https://github.com/robinonsay/rustos\" }|pico2 = { path = \"$RO/firmware/pico2\" }|" "$B/Cargo.toml"
{
echo "# Fresh rustos blinky build, run 6 ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "Source: templates/pico2 of the rustos layout at $PIN (tree identical to the git archive export, versions.txt), copied to a scratch directory; CARGO_NET_OFFLINE=true."
echo "## Template diff (package name and the two dependency lines, git form replaced by the local path form of templates/README.md)"
diff "$RO/templates/pico2/Cargo.toml" "$B/Cargo.toml" | sed "s|$SP|<scratch>|g"; echo "(diff exit end)"
echo "## rustc (default toolchain, no pin in the template):"; (cd "$B" && rustc --version)
for n in 1 2; do
  echo "## Build $n: cargo build --release --target-dir target-r$n"
  (cd "$B" && cargo build --release --target-dir "target-r$n" 2>&1 | sed "s|$SP|<scratch>|g"); echo "exit=$?"
done
echo "## SHA-256 (build 1, build 2, run 5 rustos-blinky.elf)"
shasum -a 256 "$B/target-r1/$TGT/release/blinky" "$B/target-r2/$TGT/release/blinky" "$R5/rustos-blinky.elf" | sed "s|$SP|<scratch>|; s|$SRC/||"
echo "## Loadable sections against run 5"
for s in .vector_table .boot_info .text .rodata .data; do
  a=$(rust-objcopy -O binary --only-section=$s "$B/target-r1/$TGT/release/blinky" "$SP/r6a.bin" && shasum -a 256 "$SP/r6a.bin" | cut -d' ' -f1)
  b=$(rust-objcopy -O binary --only-section=$s "$R5/rustos-blinky.elf" "$SP/r6b.bin" && shasum -a 256 "$SP/r6b.bin" | cut -d' ' -f1)
  eq=differ; [ "$a" = "$b" ] && eq=identical
  echo "$s run6 $a run5 $b $eq"
done
} > "$OUT/blinky-build.txt" 2>&1 </dev/null
cp "$B/target-r1/$TGT/release/blinky" "$OUT/rustos-blinky.elf"

# ------------------------------------------------------------------ step 9
{
echo "# UF2 conversion and file inspection, run 6 ($(date '+%Y-%m-%d %H:%M %Z')); picotool $(picotool version)"
for n in rustos-blinky cwht-app; do
  echo "## $n: picotool uf2 convert $n.elf $n.uf2 --family rp2350-arm-s"
  (cd "$OUT" && picotool uf2 convert "$n.elf" "$n.uf2" --family rp2350-arm-s 2>&1); echo "exit=$?"
  echo "## $n: picotool info -a $n.uf2"
  (cd "$OUT" && picotool info -a "$n.uf2" 2>&1); echo "exit=$?"
done
echo "## SHA-256 of the run 6 UF2 files, the run 3 and run 5 UF2 files, and the run 1 files loaded in run 4 steps 11 and 12"
shasum -a 256 "$OUT/rustos-blinky.uf2" "$OUT/cwht-app.uf2" "$R3/rustos-blinky.uf2" "$R3/cwht-app.uf2" "$R5/rustos-blinky.uf2" "$R5/cwht-app.uf2" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2" | sed "s|$SRC/||"
echo "## Run 4 load-time SHA-256 (docs/vv/reports/TC-SW-TOOL-001-r4/image-identity.txt): blinky c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3, cwht-app 4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529"
for n in rustos-blinky cwht-app; do
  cmp "$OUT/$n.uf2" "$R3/$n.uf2"; echo "cmp run6/$n.uf2 run3/$n.uf2 exit $?"
  cmp "$OUT/$n.uf2" "$R5/$n.uf2"; echo "cmp run6/$n.uf2 run5/$n.uf2 exit $?"
  cmp "$OUT/$n.uf2" "$SRC/docs/vv/reports/TC-SW-TOOL-001-r1/$n.uf2"; echo "cmp run6/$n.uf2 run1/$n.uf2 (loaded in run 4) exit $?"
done
} > "$OUT/uf2-info.txt" 2>&1 </dev/null

# ------------------------------------------------------------------ step 10
{
echo "# Blink-rate prediction, run 6 ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "The run 2 prediction (docs/vv/reports/TC-SW-TOOL-001-r2/blink-rate-prediction.txt, carried by runs 3 to 5) holds for run 6"
echo "when the executable bytes are unchanged. .text of both images against run 5 (from cwht-app-build.txt and blinky-build.txt):"
grep '^\.text ' "$OUT/cwht-app-build.txt" | sed 's/^/cwht-app /'
grep '^\.text ' "$OUT/blinky-build.txt" | sed 's/^/rustos-blinky /'
echo "## delay loops (rust-objdump -d, spin_loop call sites), run 6"
for e in cwht-app rustos-blinky; do
  echo "### $e"; rust-objdump -d --no-show-raw-insn "$OUT/$e.elf" | grep -B2 -A2 -i 'yield\|spin' | head -30
done
} > "$OUT/blink-rate-prediction.txt" 2>&1 </dev/null

# ------------------------------------------------------------------ layout cleanliness after the run
{
echo "# layout state after steps 1 to 10 ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "rustos clone HEAD $(git -C "$RO" rev-parse HEAD); status of api/ firmware/ Cargo.toml Cargo.lock .cargo LICENSE (empty = clean):"
git -C "$RO" status --porcelain -- api firmware Cargo.toml Cargo.lock .cargo LICENSE
echo "(end of status)"
echo "clone tree against the export after the run (diff -r, .git and target excluded):"
diff -r -x .git -x target "$RO" "$R/rustos-export"; echo "(diff exit $?)"
echo "owner repository master $(git -C "$OWNER_RUSTOS" rev-parse master)"
} > "$OUT/layout-after.txt" 2>&1 </dev/null
# ------------------------------------------------------------------ ELF comparison with run 5 (section 3)
sec() { # <elf> <section> -> first 16 hex digits of the section's SHA-256, or none
  rm -f "$SP/r6sec.bin"
  if rust-objcopy --dump-section "$2=$SP/r6sec.bin" "$1" "$SP/r6sec.out" 2>/dev/null && [ -f "$SP/r6sec.bin" ]; then
    shasum -a 256 "$SP/r6sec.bin" | cut -c1-16
  else echo none; fi
}
{
echo "# cwht-app.elf and rustos-blinky.elf: run 6 against run 5, per-section comparison ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "Method: rust-objcopy --dump-section <s>=<file> for every section rust-size -A lists, SHA-256 compared (first 16"
echo "hex digits); then the absolute directory strings of each file, with the session scratch prefix shown as <scratch>."
for e in cwht-app rustos-blinky; do
  echo "## $e: whole file run6 $(shasum -a 256 "$OUT/$e.elf" | cut -c1-16) ($(wc -c < "$OUT/$e.elf" | tr -d ' ') B), run5 $(shasum -a 256 "$R5/$e.elf" | cut -c1-16) ($(wc -c < "$R5/$e.elf" | tr -d ' ') B)"
  for s in $(rust-size -A "$OUT/$e.elf" | awk '$1 ~ /^\./ {print $1}'); do
    a=$(sec "$OUT/$e.elf" "$s"); b=$(sec "$R5/$e.elf" "$s")
    eq=differ; [ "$a" = "$b" ] && eq=identical
    printf '%-18s run6 %s run5 %s %s\n' "$s" "$a" "$b" "$eq"
  done
  for r in 6 5; do
    f="$OUT/$e.elf"; [ $r = 5 ] && f="$R5/$e.elf"
    echo "### r$r: absolute directory strings in the file (strings | grep '^/'), prefix only"
    strings -a "$f" | grep '^/' | sed "s|$SP|<scratch>|g" | sed -E 's|^(<scratch>/r[0-9]/[a-z-]+/[a-z0-9-]+).*|\1|; s|^(/rustc/[0-9a-f]+/[a-z-]*/?[a-z-]*).*|\1|' | sort | uniq -c
  done
done
} > "$OUT/elf-diff.txt" 2>&1 </dev/null
rm -f "$SP/r6sec.bin" "$SP/r6sec.out" "$SP/r6a.bin" "$SP/r6b.bin"

# ------------------------------------------------------------------ no-download check (D13)
{
echo "# download and guard check over the run 6 logs ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "pattern: Downloading|Updating crates|downloading component|rustup-guard|Installing"
for f in versions.txt host-build-test.txt unsafe-audit.txt sw-gate-full.txt sw-gate-keep-going.txt cwht-app-build.txt blinky-build.txt uf2-info.txt; do
  n=$(grep -c -E 'Downloading|Updating crates|downloading component|rustup-guard|Installing' "$OUT/$f")
  echo "$f: $n matching line(s)"
done
} > "$OUT/download-check.txt" 2>&1 </dev/null
echo "run6.sh done $(date '+%H:%M:%S')"
