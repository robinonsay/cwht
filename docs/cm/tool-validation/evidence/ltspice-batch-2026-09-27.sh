#!/bin/bash
# TV-014 section 3 procedure: known-answer test of tools/ltspice-batch.sh (record of what was run, not a
# controlled tool). Headless only. Run from anywhere; writes the transcript to stdout.
#   bash docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27.sh > <transcript>
# Part A: identities. Part B: versions and bottle state (read only). Part C: the unit-test module with
# the slow time-out case (every case must run; a skip is "not run"). Part D: finding 1 (a Windows path
# of 260 characters or more makes the bare LTspice command exit 0 without simulating), run with the
# bare wine command under the wrapper's lock so that no wrapper run overlaps it.
set -u
R=/Users/robinonsay/rust/cwht
PY=$R/.venv/bin/python
S=/Applications/LTspice.app/Contents/SharedSupport/ltspice
INI="$HOME/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini"
LOCKFILE="$(getconf DARWIN_USER_TEMP_DIR)cwht-ltspice.lock"

echo "# TV-014 procedure, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm), macOS $(sw_vers -productVersion)"
echo "# repository HEAD $(git -C $R rev-parse HEAD)"
echo
echo "## A. identities (git blob of the working-tree file; SHA-256; state against HEAD)"
for f in tools/ltspice-batch.sh tools/tests/test_ltspice_batch.py; do
  blob=$(git -C $R hash-object "$R/$f"); head_blob=$(git -C $R rev-parse "HEAD:$f" 2>/dev/null || echo none)
  state=$([ "$blob" = "$head_blob" ] && echo "unchanged from HEAD" || echo "differs from HEAD (HEAD: $head_blob)")
  echo "$f blob $blob sha256 $(shasum -a 256 "$R/$f" | cut -d ' ' -f 1) $state"
done
tree_digest=$(cd $R/tools/tests/fixtures/ltspice && find . -type f ! -name '.*' | LC_ALL=C sort | xargs shasum -a 256 | shasum -a 256 | cut -d ' ' -f 1)
fx_state=$(git -C $R status --porcelain -- tools/tests/fixtures/ltspice | wc -l | tr -d ' ')
echo "tools/tests/fixtures/ltspice/ tree digest (sha256 of the sorted 'shasum -a 256' list) $tree_digest; files differing from HEAD or untracked: $fx_state"
(cd $R/tools/tests/fixtures/ltspice && find . -type f ! -name '.*' | LC_ALL=C sort | xargs shasum -a 256)
echo
echo "## B. versions and bottle state (read only)"
echo "\$ defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString"; defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString
echo "\$ grep '\"Version\"' cxbottle.conf"; grep '"Version"' $S/support/ltspice/cxbottle.conf
echo "\$ shasum -a 256 LTspice.exe"; shasum -a 256 "$HOME/Library/Application Support/LTspice/Bottles/ltspice/drive_c/Program Files/ADI/LTspice/LTspice.exe" 2>/dev/null || echo "LTspice.exe not found at the bottle path"
echo "\$ ls -l <bottle LTspice.ini>"; ls -l "$INI"
echo "\$ iconv -f UTF-16LE -t UTF-8 <bottle LTspice.ini> | grep -c '^CaptureAnalytics=false\$'"
iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | /usr/bin/grep -c '^CaptureAnalytics=false$'
echo "\$ bash --version"; /bin/bash --version | head -1
echo "\$ $PY --version"; $PY --version
echo
echo "## C. unit-test module, slow case included"
echo "\$ CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py"
(cd $R && CWHT_LTSPICE_SLOW=1 $PY -m unittest discover -v -s tools/tests -p test_ltspice_batch.py 2>&1)
C_RC=$?
echo "exit=$C_RC"
echo
echo "## D. finding 1: bare LTspice command on a deck whose Windows output path is 260 characters or more"
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-lts-long.XXXXXX")
W=$(cd "$W" && pwd -P)
pad=$(( 242 - ${#W} ))
D="$W/$(printf 'd%.0s' $(seq 1 $pad))"
mkdir -p "$D"
cp $R/tools/tests/fixtures/ltspice/rc-step-tran.net "$D/rc-step-tran.net"
P="Z:$D/rc-step-tran.net"
echo "Windows path of the input deck: ${#P} characters"
echo "\$ lockf -k <wrapper lock> wine --bottle=ltspice --wait-children LTspice.exe -b <long path>/rc-step-tran.net"
if iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | /usr/bin/grep -q '^CaptureAnalytics=false$'; then
  /usr/bin/lockf -k -t 600 "$LOCKFILE" "$S/bin/wine" --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' -b "$D/rc-step-tran.net" >/dev/null 2>&1
  echo "exit=$?"
  echo "files written: $(cd "$D" && ls | tr '\n' ' ')"
  [ -f "$D/rc-step-tran.log" ] && { echo "log (NUL and CR bytes removed):"; LC_ALL=C tr -d '\000\r\377\376' < "$D/rc-step-tran.log"; echo; }
  echo "\$ tools/ltspice-batch.sh -b <same deck>   (the wrapper's own run directory is short, so the deck path does not matter)"
  $R/tools/ltspice-batch.sh -b "$D/rc-step-tran.net" 2>&1 | tail -1; echo "exit=${PIPESTATUS[0]}"
else
  echo "not run: the bottle precondition is not met (part B)"
fi
rm -rf "$W"
echo
echo "## result"
echo "unit-test module exit=$C_RC (a pass needs exit 0 and no skipped test in part C)"
