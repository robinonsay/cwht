#!/bin/bash
# Provenance of expected/clean-SHA256SUMS.normalized (TV-016; CM plan section 8.2 step 2 and the
# normalization table of section 8.2). Written by the TV-016 author on 2026-09-27 from the CM plan
# table alone, independently of tools/normalize_fab.py: the date lines are removed with grep -v and
# the date fields replaced with perl, then every file is hashed with shasum -a 256. The known-answer
# test compares tools/normalize_fab.py on a fresh export (taken at another time) with this list.
#
# Run from the repository root:  bash tools/tests/fixtures/kicad/make_expected_normalized.sh
# It writes tools/tests/fixtures/kicad/expected/clean-SHA256SUMS.normalized and prints the raw
# hashes and the normalized hashes of the export it made. Headless; kicad-cli 10.0.6 (lock section 1).
set -euo pipefail
K=/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
FX="$(cd "$(dirname "$0")" && pwd)"
[ "$("$K" version)" = "10.0.6" ] || { echo "kicad-cli is not 10.0.6" >&2; exit 3; }
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-normalized.XXXXXX")
cp "$FX"/clean.kicad_pcb "$FX"/clean.kicad_pro "$FX"/clean.kicad_sch "$FX"/fp-lib-table "$FX"/sym-lib-table "$W"/
cd "$W"
mkdir out
# The four export commands of CM plan section 8.2 step 2 (F3, F6, F7) on the fixture board, and the
# STEP and BOM exports of the kicad-cli known answer (known-answers.json blocks step and bom).
"$K" pcb export gerbers -o out/ -l "F.Cu,In1.Cu,In2.Cu,B.Cu,F.Mask,B.Mask,F.Silkscreen,B.Silkscreen,F.Paste,B.Paste,Edge.Cuts" --no-x2 --no-netlist --no-protel-ext --use-drill-file-origin --subtract-soldermask --check-zones --precision 6 clean.kicad_pcb
"$K" pcb export drill -o out/ --format excellon --drill-origin plot --excellon-units mm --excellon-zeros-format decimal --excellon-oval-format route --excellon-separate-th --generate-map --map-format pdf --generate-report --report-path out/clean-drill-report.rpt clean.kicad_pcb
"$K" pcb export pos -o out/clean-cpl.csv --format csv --units mm --use-drill-file-origin --side both --smd-only --exclude-dnp clean.kicad_pcb
"$K" pcb export step --board-only --drill-origin -o out/clean.step clean.kicad_pcb
"$K" sch export bom -o out/clean-bom.csv clean.kicad_sch
echo "## raw SHA-256 of the export"
(cd out && shasum -a 256 *)
mkdir norm
for f in out/*; do
  b=$(basename "$f")
  case "$b" in
    *.gbr) grep -v -E '^%TF\.CreationDate,|^G04 #@! TF\.CreationDate,|^G04 Created by KiCad .* date ' "$f" > "norm/$b" || true ;;
    *.drl) grep -v -E '^; DRILL file .* date |^; #@! TF\.CreationDate,' "$f" > "norm/$b" || true ;;
    *.rpt) grep -v -E '^Created on ' "$f" > "norm/$b" || true ;;
    *.gbrjob) perl -0777 -pe 's/("CreationDate"\s*:\s*)"[^"]*"/$1"normalized"/g' "$f" > "norm/$b" ;;
    *.step|*.stp) perl -0777 -pe "s/(FILE_NAME\s*\(\s*'(?:[^']|'')*'\s*,\s*)'(?:[^']|'')*'/\$1'normalized'/s" "$f" > "norm/$b" ;;
    *.pdf) perl -0777 -pe 's{(/(?:CreationDate|ModDate)\s*\(D:)([^)]*)(\))}{my ($a,$d,$c)=($1,$2,$3); $d=~tr/0-9/0/; "$a$d$c"}ge' "$f" > "norm/$b" ;;
    *.csv) cp "$f" "norm/$b" ;;
    *) echo "no rule for $b" >&2; exit 1 ;;
  esac
done
echo "## normalized SHA-256"
(cd norm && shasum -a 256 *) | tee "$FX/expected/clean-SHA256SUMS.normalized"
cd /
rm -r "$W"
