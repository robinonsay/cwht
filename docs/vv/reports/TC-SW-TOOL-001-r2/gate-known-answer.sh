#!/bin/sh
# Known-answer runs KA-0 to KA-8 of tools/sw_gate.sh on seeded copies of the firmware workspace
# (TC-SW-TOOL-001 step 7, run 2). Usage: gate-known-answer.sh <scratch-dir>
# Each copy holds the gate, the lock and the three R3 scripts (tools/measurements.py,
# tools/unsafe_audit.py, tools/complexity_gate.py) and tools/emu_run.sh, so the copy's gate takes
# the same paths as the repository gate (G2 and G3 through measurements.py, no INTERIM line).
# rustos is linked read only; nothing is downloaded (the gate exports RUSTUP_AUTO_INSTALL=0).
SP=$1; SRC=/Users/robinonsay/rust/cwht
[ -n "$SP" ] || { echo "usage: gate-known-answer.sh <scratch-dir>"; exit 2; }
echo "# gate-known-answer.sh (run 2) $(date '+%Y-%m-%d %H:%M %Z'); tools/sw_gate.sh sha256 $(shasum -a 256 "$SRC/tools/sw_gate.sh" | cut -d' ' -f1)"
mk() {
  d="$SP/ka-r2/$1"; rm -rf "$d"; mkdir -p "$d/cwht/tools"
  ln -sfn /Users/robinonsay/rust/rustos "$d/rustos"
  ln -sfn "$SRC/.venv" "$d/cwht/.venv"
  cp "$SRC/tools/sw_gate.sh" "$SRC/tools/toolchain.lock.md" "$SRC/tools/measurements.py" \
     "$SRC/tools/unsafe_audit.py" "$SRC/tools/complexity_gate.py" "$SRC/tools/emu_run.sh" "$d/cwht/tools/"
  rsync -a --exclude target "$SRC/firmware/" "$d/cwht/firmware/"
  echo "$d/cwht"
}
run() {
  name=$1; expect=$2; root=$3; mode=${4:---quick}
  out=$("$root/tools/sw_gate.sh" "$mode" 2>&1); code=$?
  first_fail=$(printf '%s\n' "$out" | grep -m1 '^FAIL' || echo "no FAIL line")
  interim=$(printf '%s\n' "$out" | grep -c '^INTERIM')
  verdict=MATCH; [ "$code" = "$expect" ] || verdict=MISMATCH
  echo "$name: exit $code (expected $expect) $verdict; mode $mode; INTERIM lines $interim; first FAIL line: $first_fail"
  printf '%s\n' "$out" > "$root/../gate-output.txt"
}
r=$(mk ka0); run "KA-0 unmodified copy" 0 "$r"
r=$(mk ka1); printf '\n/// Seeded defect.\n#[must_use]\npub fn seeded() -> u8 {\n    Some(1_u8).unwrap()\n}\n' >> "$r/firmware/cwht-core/src/heartbeat.rs"; run "KA-1 seeded unwrap in cwht-core" 1 "$r"
r=$(mk ka2); printf '\n/// Seeded format defect.\npub const  SEEDED: u8 = 1;\n' >> "$r/firmware/cwht-core/src/heartbeat.rs"; run "KA-2 seeded formatting defect" 1 "$r"
r=$(mk ka3); sed -i '' 's/assert_eq!(calls, count);/assert_eq!(calls, count.saturating_add(1));/' "$r/firmware/cwht-core/tests/heartbeat.rs"; run "KA-3 seeded failing host test" 1 "$r"
r=$(mk ka4); printf '\n/// Seeded unsafe.\n#[must_use]\npub fn seeded() -> u8 {\n    // SAFETY: seeded defect for the known-answer test.\n    unsafe { core::mem::transmute::<i8, u8>(-1) }\n}\n' >> "$r/firmware/cwht-core/src/heartbeat.rs"; run "KA-4 seeded unsafe block in cwht-core" 1 "$r"
r=$(mk ka5); sed -i '' 's/`rustc 1.98.0 (88d9e12ae 2026-08-18)`/`rustc 1.98.1 (0000000 2026-09-01)`/' "$r/tools/toolchain.lock.md"; run "KA-5 lock rustc row differs from installed rustc" 1 "$r"
r=$(mk ka6); sed -i '' 's/let mut heartbeat = Heartbeat::new();/let mut heartbeat = Heartbeat::new();\n    let _seed = Some(1_u8).unwrap();/' "$r/firmware/cwht-app/src/main.rs"; run "KA-6 seeded unwrap in cwht-app (target clippy)" 1 "$r"
r=$(mk ka7); sed -i '' 's|println!("cargo:rerun-if-changed=build.rs");|println!("cargo:rerun-if-changed=build.rs");\n    println!("cargo:warning=seeded build warning (KA-7)");|' "$r/firmware/cwht-app/build.rs"; run "KA-7 seeded cargo:warning in cwht-app/build.rs" 1 "$r"
# KA-8: stale identical JUnit copies from an earlier invocation plus a failing host test, --keep-going.
r=$(mk ka8); mkdir -p "$r/firmware/target/nextest"
printf '<?xml version="1.0"?>\n<testsuites><testsuite name="stale"><testcase classname="stale" name="stale_case"/></testsuite></testsuites>\n' > "$r/firmware/target/nextest/run1-junit.xml"
cp "$r/firmware/target/nextest/run1-junit.xml" "$r/firmware/target/nextest/run2-junit.xml"
sed -i '' 's/assert_eq!(calls, count);/assert_eq!(calls, count.saturating_add(1));/' "$r/firmware/cwht-core/tests/heartbeat.rs"
run "KA-8 stale JUnit copies with a failing host test" 1 "$r" --keep-going
g3=$(grep -m1 'G3 identical result sets' "$r/../gate-output.txt" | grep -E '^(PASS|FAIL)' || echo "no G3 comparison result line")
stale=absent; [ -f "$r/firmware/target/nextest/run1-junit.xml" ] && stale=present
echo "KA-8 G3 comparison line: $g3; run1-junit.xml after the run: $stale"
