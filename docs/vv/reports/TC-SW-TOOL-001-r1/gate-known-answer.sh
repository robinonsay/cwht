#!/bin/sh
# Known-answer runs of tools/sw_gate.sh --quick on seeded copies of the firmware workspace.
SP=$1; SRC=/Users/robinonsay/rust/cwht
mk() {
  d="$SP/ka-final/$1"; mkdir -p "$d/cwht/tools"
  ln -sfn /Users/robinonsay/rust/rustos "$d/rustos"
  ln -sfn "$SRC/.venv" "$d/cwht/.venv"
  cp "$SRC/tools/sw_gate.sh" "$SRC/tools/toolchain.lock.md" "$d/cwht/tools/"
  rsync -a --exclude target "$SRC/firmware/" "$d/cwht/firmware/"
  echo "$d/cwht"
}
run() {
  name=$1; expect=$2; root=$3
  out=$("$root/tools/sw_gate.sh" --quick 2>&1); code=$?
  first_fail=$(printf '%s\n' "$out" | grep -m1 '^FAIL' || echo "no FAIL line")
  verdict=MATCH; [ "$code" = "$expect" ] || verdict=MISMATCH
  echo "$name: exit $code (expected $expect) $verdict; first FAIL line: $first_fail"
}
r=$(mk ka0); run "KA-0 unmodified copy" 0 "$r"
r=$(mk ka1); printf '\n/// Seeded defect.\n#[must_use]\npub fn seeded() -> u8 {\n    Some(1_u8).unwrap()\n}\n' >> "$r/firmware/cwht-core/src/heartbeat.rs"; run "KA-1 seeded unwrap in cwht-core" 1 "$r"
r=$(mk ka2); printf '\n/// Seeded format defect.\npub const  SEEDED: u8 = 1;\n' >> "$r/firmware/cwht-core/src/heartbeat.rs"; run "KA-2 seeded formatting defect" 1 "$r"
r=$(mk ka3); sed -i '' 's/assert_eq!(calls, count);/assert_eq!(calls, count.saturating_add(1));/' "$r/firmware/cwht-core/tests/heartbeat.rs"; run "KA-3 seeded failing host test" 1 "$r"
r=$(mk ka4); printf '\n/// Seeded unsafe.\n#[must_use]\npub fn seeded() -> u8 {\n    // SAFETY: seeded defect for the known-answer test.\n    unsafe { core::mem::transmute::<i8, u8>(-1) }\n}\n' >> "$r/firmware/cwht-core/src/heartbeat.rs"; run "KA-4 seeded unsafe block in cwht-core" 1 "$r"
r=$(mk ka5); sed -i '' 's/`rustc 1.98.0 (88d9e12ae 2026-08-18)`/`rustc 1.98.1 (0000000 2026-09-01)`/' "$r/tools/toolchain.lock.md"; run "KA-5 lock rustc row differs from installed rustc" 1 "$r"
r=$(mk ka6); sed -i '' 's/let mut heartbeat = Heartbeat::new();/let mut heartbeat = Heartbeat::new();\n    let _seed = Some(1_u8).unwrap();/' "$r/firmware/cwht-app/src/main.rs"; run "KA-6 seeded unwrap in cwht-app (target clippy)" 1 "$r"
