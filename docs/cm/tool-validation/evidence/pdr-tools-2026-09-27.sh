#!/bin/bash
# Known-answer procedure of TV-015 to TV-019 (WP-PDR-07, wave 1a; CM plan section 9.2 steps 1 and 2).
# A record of what was run, not a controlled tool. Headless; no network; writes only under a
# temporary directory and, for TV-017, the inspected renders named below in this evidence folder.
#
#   bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-0NN > docs/cm/tool-validation/evidence/<log>
#
# Part A: identities of every file validated (git blob, SHA-256, equal to HEAD or not) and of each
# fixture directory (git tree at HEAD and the digest of the sorted shasum list of its tracked files).
# Part B: versions of the external programs and the interpreter. Part C: the known-answer module(s)
# with -v. Part D (TV-015 only): two conversions of cube.scad and the normalized STEP hashes
# (reproducibility, class A). Part E (TV-017 only): the fixture renders copied here for inspection.
set -u
R=/Users/robinonsay/rust/cwht
PY=$R/.venv/bin/python
EVD=$R/docs/cm/tool-validation/evidence
TV=${1:?usage: pdr-tools-2026-09-27.sh TV-015|TV-016|TV-017|TV-018|TV-019}
cd "$R" || exit 2

ident() {
  for f in "$@"; do
    b=$(git hash-object "$f"); h=$(git rev-parse "HEAD:$f" 2>/dev/null || echo none)
    s=$(shasum -a 256 "$f" | cut -c1-64)
    printf '%s blob %s sha256 %s %s\n' "$f" "$b" "$s" "$([ "$b" = "$h" ] && echo 'unchanged from HEAD' || echo 'DIFFERS FROM HEAD')"
  done
}
fixture() {
  d=$1
  echo "$d git tree at HEAD $(git rev-parse "HEAD:$d")"
  git ls-files -- "$d" | while read -r f; do shasum -a 256 "$f"; done | sort -k2 > /tmp/.pdr-tools-list.$$
  echo "$d tracked files $(wc -l < /tmp/.pdr-tools-list.$$ | tr -d ' '), digest (sha256 of the sorted shasum list) $(shasum -a 256 < /tmp/.pdr-tools-list.$$ | cut -c1-64)"
  cat /tmp/.pdr-tools-list.$$
  rm -f /tmp/.pdr-tools-list.$$
  echo "$d untracked or modified files: $(git status --porcelain -- "$d" | wc -l | tr -d ' ')"
}
kat() {
  echo "\$ .venv/bin/python -m unittest discover -v -s tools/tests -p $1"
  "$PY" -m unittest discover -v -s tools/tests -p "$1" 2>&1
  echo "exit=$?"
}

echo "# $TV known-answer run, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm), macOS $(sw_vers -productVersion)"
echo "# repository HEAD $(git rev-parse HEAD) ($(git log -1 --format=%s HEAD | cut -c1-80))"
echo "## A. identities"
case "$TV" in
  TV-015) ident tools/scad2step.py tools/tests/test_scad2step.py; fixture tools/tests/fixtures/openscad ;;
  TV-016) ident tools/normalize_fab.py tools/tests/test_normalize_fab.py tools/tests/test_kicad_cli.py; fixture tools/tests/fixtures/kicad ;;
  TV-017) ident tools/render_tpm.py tools/tests/test_render_tpm.py docs/plan/tpm.json; fixture tools/tests/fixtures/render_tpm ;;
  TV-018) ident tools/csa.py tools/check_commit_msg.py tools/tests/test_csa.py docs/process/05-configuration-and-data-management.md; fixture tools/tests/fixtures/csa ;;
  TV-019) ident tools/check_commit_msg.py tools/csa.py tools/tests/test_check_commit_msg.py docs/process/05-configuration-and-data-management.md; fixture tools/tests/fixtures/csa ;;
  *) echo "unknown record $TV"; exit 2 ;;
esac
echo "## B. versions"
echo "interpreter: $("$PY" --version 2>&1) ($PY); git: $(git --version)"
case "$TV" in
  TV-015) echo "OpenSCAD: $(/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD --version 2>&1 | tail -1)"
          echo "FreeCAD bundle CFBundleVersion: $(defaults read /Applications/FreeCAD.app/Contents/Info.plist CFBundleVersion)" ;;
  TV-016) echo "kicad-cli: $(/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli version)"; echo "perl (expected-list generator only): $(perl -e 'print $^V')" ;;
  TV-017) echo "matplotlib: $("$PY" -c 'import matplotlib; print(matplotlib.__version__)'); pillow: $("$PY" -c 'import PIL; print(PIL.__version__)')" ;;
esac
echo "## C. known-answer module(s)"
case "$TV" in
  TV-015) kat test_scad2step.py ;;
  TV-016) kat test_normalize_fab.py; kat test_kicad_cli.py ;;
  TV-017) kat test_render_tpm.py ;;
  TV-018) kat test_csa.py ;;
  TV-019) kat test_check_commit_msg.py ;;
esac
if [ "$TV" = TV-015 ]; then
  echo "## D. reproducibility (class A): two conversions of cube.scad, STEP hashes raw and with the FILE_NAME time stamp normalized"
  W=$(mktemp -d "${TMPDIR:-/tmp}/tv015.XXXXXX")
  for i in 1 2; do
    mkdir "$W/run$i"
    "$PY" tools/scad2step.py --scad tools/tests/fixtures/openscad/cube.scad --step "$W/run$i/cube.step" > "$W/run$i/out.txt" 2>&1
    echo "run $i exit=$? $(grep '^SCAD2STEP KAT' "$W/run$i/out.txt")"
    echo "run $i raw sha256 $(shasum -a 256 < "$W/run$i/cube.step" | cut -c1-64); FILE_NAME line: $(grep -m1 'FILE_NAME' "$W/run$i/cube.step")"
    perl -0777 -pe "s/(FILE_NAME\s*\(\s*'(?:[^']|'')*'\s*,\s*)'(?:[^']|'')*'/\$1'normalized'/s" "$W/run$i/cube.step" > "$W/run$i/norm.step"
    echo "run $i normalized sha256 $(shasum -a 256 < "$W/run$i/norm.step" | cut -c1-64)"
    sleep 2
  done
  cmp -s "$W/run1/norm.step" "$W/run2/norm.step" && echo "RESULT normalized STEP identical" || echo "RESULT normalized STEP DIFFERS"
  rm -r "$W"
fi
if [ "$TV" = TV-017 ]; then
  echo "## E. fixture renders for inspection (visual closure)"
  W=$(mktemp -d "${TMPDIR:-/tmp}/tv017.XXXXXX")
  "$PY" tools/render_tpm.py --review PDR --tpm tools/tests/fixtures/render_tpm/tpm.json --out "$W" --date 2026-10-06 2>&1
  echo "exit=$?"
  cp "$W/tpm-status.png" "$EVD/render-tpm-fixture-tpm-status.png"
  cp "$W/tpm-trend-own-yellow-after-status-note.png" "$EVD/render-tpm-fixture-trend-own-yellow-after-status-note.png"
  echo "copied tpm-status.png and tpm-trend-own-yellow-after-status-note.png to $EVD with the prefix render-tpm-fixture-"
  shasum -a 256 "$EVD/render-tpm-fixture-tpm-status.png" "$EVD/render-tpm-fixture-trend-own-yellow-after-status-note.png"
  rm -r "$W"
fi
echo "# end $(date '+%H:%M:%S %Z')"
