#!/bin/sh
# TC-SW-TOOL-001 run 6, section 3 ELF comparison with run 5 (deviation D22).
# Usage: elf-diff.sh <scratch-dir> <report-artifact-dir>
# Supersedes the elf-diff.txt that the ELF block of run6.sh wrote: that block took the section list
# from rust-size -A, which omits .symtab, .shstrtab and .strtab. This script takes every section
# rust-readobj --sections lists (as run 5 did) and adds the .strtab symbol-name difference.
set -u
SP=$1; OUT=$2
R5=/Users/robinonsay/rust/cwht/docs/vv/reports/TC-SW-TOOL-001-r5
sec() { # <elf> <section> -> first 16 hex digits of the section's SHA-256, or none
  rm -f "$SP/r6sec.bin"
  if rust-objcopy --dump-section "$2=$SP/r6sec.bin" "$1" "$SP/r6sec.out" 2>/dev/null && [ -f "$SP/r6sec.bin" ]; then
    shasum -a 256 "$SP/r6sec.bin" | cut -c1-16
  else echo none; fi
}
strtab() { rust-objcopy --dump-section ".strtab=$2" "$1" "$SP/r6sec.out" 2>/dev/null; tr '\0' '\n' < "$2" > "$2.txt"; }
{
echo "# cwht-app.elf and rustos-blinky.elf: run 6 against run 5, per-section comparison ($(date '+%Y-%m-%d %H:%M %Z'))"
echo "Method: rust-objcopy --dump-section <s>=<file> for every section rust-readobj --sections lists (loadable and"
echo "non-loadable), SHA-256 compared (first 16 hex digits); then the absolute directory strings of each file, with the"
echo "session scratch prefix shown as <scratch>; then the .strtab symbol names that differ."
for e in cwht-app rustos-blinky; do
  echo "## $e: whole file run6 $(shasum -a 256 "$OUT/$e.elf" | cut -c1-16) ($(wc -c < "$OUT/$e.elf" | tr -d ' ') B), run5 $(shasum -a 256 "$R5/$e.elf" | cut -c1-16) ($(wc -c < "$R5/$e.elf" | tr -d ' ') B)"
  for s in $(rust-readobj --sections "$OUT/$e.elf" | awk '$1 == "Name:" && $2 ~ /^\./ {print $2}'); do
    a=$(sec "$OUT/$e.elf" "$s"); b=$(sec "$R5/$e.elf" "$s")
    eq=differ; [ "$a" = "$b" ] && eq=identical
    printf '%-18s run6 %s run5 %s %s\n' "$s" "$a" "$b" "$eq"
  done
  for r in 6 5; do
    f="$OUT/$e.elf"; [ $r = 5 ] && f="$R5/$e.elf"
    echo "### r$r: absolute directory strings in the file (strings | grep '^/'), prefix only"
    strings -a "$f" | grep '^/' | sed "s|$SP|<scratch>|g" | sed -E 's|^(<scratch>/r[0-9]/[a-z-]+/[a-z0-9-]+).*|\1|; s|^(/rustc/[0-9a-f]+/[a-z-]*/?[a-z-]*).*|\1|' | sort | uniq -c
  done
  strtab "$OUT/$e.elf" "$SP/r6strtab6"; strtab "$R5/$e.elf" "$SP/r6strtab5"
  echo "### $e .strtab: symbol names that differ (run 6 left, run 5 right; first 6 lines of diff)"
  diff "$SP/r6strtab6.txt" "$SP/r6strtab5.txt" | head -6
  echo "differing symbol lines: $(diff "$SP/r6strtab6.txt" "$SP/r6strtab5.txt" | grep -c '^<'); symbol lines run 6 $(wc -l < "$SP/r6strtab6.txt" | tr -d ' '), run 5 $(wc -l < "$SP/r6strtab5.txt" | tr -d ' ')"
done
} > "$OUT/elf-diff.txt" 2>&1 </dev/null
rm -f "$SP/r6sec.bin" "$SP/r6sec.out" "$SP/r6strtab6" "$SP/r6strtab5" "$SP/r6strtab6.txt" "$SP/r6strtab5.txt"
