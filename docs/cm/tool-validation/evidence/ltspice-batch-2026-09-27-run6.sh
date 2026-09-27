#!/bin/bash
# TV-014 section 3 procedure from run 6 on (record of what was run, not a controlled tool). Headless only;
# LTspice runs only through tools/ltspice-batch.sh. Run from anywhere; writes the transcript to stdout.
#   bash docs/cm/tool-validation/evidence/ltspice-batch-2026-09-27-run6.sh > <transcript>
# Part A: identities. Part B: versions, bottle state and Wine session state (read only). Part C: the
# unit-test module with the real-LTspice integration cases (CWHT_LTSPICE_INTEGRATION=1) and the slow
# time-out case (CWHT_LTSPICE_SLOW=1); every case must run (a skip is "not run"). Part D: finding 1 (the
# long-path check) through the wrapper: a deck whose Windows path is 260 characters or more. Part E:
# state after the run, 10 s later, while this procedure holds the wrapper lock (no other run can start):
# no process of the bottle's Wine session, no holder of the lock, key present. Part F: the regression
# case of INSP-038 finding-20 fails on a scratch copy of the wrapper with the launch line of blob 64e1c723.
# Changed from ltspice-batch-2026-09-27.sh (runs 1 to 4): part C sets CWHT_LTSPICE_INTEGRATION=1; part D
# no longer runs the bare wine command (LTspice is run only through the wrapper, which also ends the Wine
# session; LTspice's own MAX_PATH behaviour is TV-014 finding 1, development log section 1); parts E, F new.
# Changed from ltspice-batch-2026-09-27-run5.sh (run 5): part B and E list the processes in the bottle with
# their executable name and mark the Wine processes (the wrapper's rule after INSP-038 finding-21), and list
# Wine processes of the bundle anywhere; part G (new) runs the finding-21 bystander cases on a scratch copy
# with the wrapper of blob bdc4513f (run 5), where they must fail.
set -u
R=/Users/robinonsay/rust/cwht
PY=$R/.venv/bin/python
S=/Applications/LTspice.app/Contents/SharedSupport/ltspice
BOTTLE="$HOME/Library/Application Support/LTspice/Bottles/ltspice"
INI="$BOTTLE/drive_c/users/crossover/AppData/Roaming/LTspice.ini"
LOCKFILE="$(getconf DARWIN_USER_TEMP_DIR)cwht-ltspice.lock"

keycount() { iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | /usr/bin/grep -c '^CaptureAnalytics=false$'; }
wine_name() {  # $1 = executable name; exit 0 when it is a Wine process of the bundle (wrapper step 5a rule)
  case "$1" in [A-Za-z]:\\*.[eE][xX][eE]|"$S"/*) return 0 ;; esac; return 1
}
session() {  # every process with its cwd in the bottle or its wineserver directory, marked WINE or other
  local pre srv
  pre=$(cd "$BOTTLE" && pwd -P)
  srv="$(cd /tmp && pwd -P)/.wine-$(id -u)/server-$(printf '%x-%x' $(stat -f '%d %i' "$pre"))"
  lsof -n -w -u "$(id -u)" -a -d cwd -F pn 2>/dev/null | awk -v pre="$pre/" -v srv="$srv" '
    /^p/ { pid = substr($0, 2) }
    /^n/ { n = substr($0, 2); if (index(n "/", pre) == 1 || n == srv) print pid }' |
    while read -r p; do c=$(ps -o comm= -p "$p"); if wine_name "$c"; then k=WINE; else k=other; fi
      echo "$k $(ps -o pid=,ppid=,etime=,command= -p "$p")"; done
}
wine_anywhere() {  # Wine processes of the bundle whatever their cwd (executable name rule)
  ps -U "$(id -u)" -o pid= | while read -r p; do c=$(ps -o comm= -p "$p" 2>/dev/null) || continue
    wine_name "$c" && ps -o pid=,ppid=,etime=,command= -p "$p"; done
}

echo "# TV-014 procedure (run 6 form), $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm), macOS $(sw_vers -productVersion)"
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
echo "tools/tests/fixtures/ltspice/ git tree $(git -C $R rev-parse HEAD:tools/tests/fixtures/ltspice), tree digest (sha256 of the sorted 'shasum -a 256' list) $tree_digest; files differing from HEAD or untracked: $fx_state"
(cd $R/tools/tests/fixtures/ltspice && find . -type f ! -name '.*' | LC_ALL=C sort | xargs shasum -a 256)
echo
echo "## B. versions, bottle state and Wine session state (read only)"
echo "\$ defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString"; defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString
echo "\$ grep '\"Version\"' cxbottle.conf"; grep '"Version"' $S/support/ltspice/cxbottle.conf
echo "\$ shasum -a 256 LTspice.exe"; shasum -a 256 "$BOTTLE/drive_c/Program Files/ADI/LTspice/LTspice.exe" 2>/dev/null || echo "LTspice.exe not found at the bottle path"
echo "\$ shasum -a 256 <bundle>/bin/wineserver (the session end of step 5a)"; shasum -a 256 "$S/bin/wineserver"
echo "\$ ls -l <bottle LTspice.ini>"; ls -l "$INI"
echo "\$ iconv -f UTF-16LE -t UTF-8 <bottle LTspice.ini> | grep -c '^CaptureAnalytics=false\$'"; keycount
echo "\$ pgrep -fl 'LTspice\\.exe' (an LTspice.exe open before the run)"; pgrep -fl 'LTspice\.exe' || echo "none"
echo "\$ processes with their current directory in the bottle or its wineserver directory (WINE: a Wine process of the bundle)"; B_SESSION=$(session); echo "${B_SESSION:-none}"
echo "\$ Wine processes of the bundle anywhere (executable name a Windows .exe path or under the bundle)"; B_ANY=$(wine_anywhere); echo "${B_ANY:-none}"
echo "\$ lockf -s -t 0 <wrapper lock> true"; /usr/bin/lockf -s -t 0 "$LOCKFILE" true; echo "exit=$? (0 free, 75 held by another run: the procedure then waits in part C)"
echo "\$ bash --version"; /bin/bash --version | head -1
echo "\$ $PY --version"; $PY --version
echo
echo "## C. unit-test module with the integration cases and the slow case"
echo "\$ CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 .venv/bin/python -m unittest discover -v -s tools/tests -p test_ltspice_batch.py"
C_T0=$(date +%s)
(cd $R && CWHT_LTSPICE_INTEGRATION=1 CWHT_LTSPICE_SLOW=1 $PY -m unittest discover -v -s tools/tests -p test_ltspice_batch.py 2>&1)
C_RC=$?
echo "exit=$C_RC elapsed=$(( $(date +%s) - C_T0 ))s key_count=$(keycount) at $(date '+%H:%M:%S')"
echo
echo "## D. finding 1 (long-path check) through the wrapper: a deck whose Windows path is 260 characters or more"
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-lts-long.XXXXXX")
W=$(cd "$W" && pwd -P)
pad=$(( 242 - ${#W} ))
D="$W/$(printf 'd%.0s' $(seq 1 $pad))"
mkdir -p "$D"
cp $R/tools/tests/fixtures/ltspice/rc-step-tran.net "$D/rc-step-tran.net"
P="Z:$D/rc-step-tran.net"
echo "Windows path of the input deck: ${#P} characters; of its .op.raw beside it: $(( ${#P} - 4 + 7 )) characters"
echo "\$ tools/ltspice-batch.sh -b <long path>/rc-step-tran.net   (the wrapper runs it in its short run directory)"
echo "key_count before: $(keycount)"
$R/tools/ltspice-batch.sh -b "$D/rc-step-tran.net" 2>&1; D_RC=$?
echo "exit=$D_RC"
echo "key_count after: $(keycount)"
echo "files beside the deck: $(cd "$D" && ls | tr '\n' ' ')"
[ -f "$D/rc-step-tran.log" ] && { echo "log:"; cat "$D/rc-step-tran.log"; }
rm -rf "$W"
echo
echo "## E. state 10 s after the last run, holding the wrapper lock (no other run can start meanwhile)"
echo "\$ lockf -k -t 1800 <wrapper lock> <sleep 10; list the session; lsof the lock file>"
export BOTTLE LOCKFILE S; export -f session wine_name wine_anywhere
/usr/bin/lockf -k -t 1800 "$LOCKFILE" /bin/bash -c '
  sleep 10
  echo "time $(date "+%H:%M:%S")"
  echo "processes in the bottle or its wineserver directory:"; s=$(session); echo "${s:-none}"
  echo "Wine processes of the bundle anywhere:"; a=$(wine_anywhere); echo "${a:-none}"
  echo "pgrep -fl LTspice\\.exe:"; pgrep -fl "LTspice\.exe" || echo none
  echo "lsof on the lock file (expected: only the lockf holder and this shell):"; lsof -n -w "$LOCKFILE"
' 2>&1
E_RC=$?
echo "exit=$E_RC"
echo "\$ lockf -s -t 0 <wrapper lock> true (after release)"; /usr/bin/lockf -s -t 0 "$LOCKFILE" true; echo "exit=$?"
echo "key_count $(keycount) at $(date '+%H:%M:%S'); ls -l ini: $(ls -l "$INI")"
echo
echo "## F. regression case of INSP-038 finding-20 on the old launch line (scratch copy; test doubles only)"
F=$(mktemp -d "${TMPDIR:-/tmp}/kat-lts-f20.XXXXXX")
mkdir -p "$F/tools/tests/fixtures"
cp $R/tools/ltspice-batch.sh "$F/tools/"
cp $R/tools/tests/test_ltspice_batch.py "$F/tools/tests/"
cp -R $R/tools/tests/fixtures/ltspice "$F/tools/tests/fixtures/"
/usr/bin/sed -i '' 's|^( exec 9>&-; cd "\$RUN" \&\& exec "\$WINE" --bottle=ltspice --wait-children "\$EXE" "\$@" ) >|( cd "$RUN" \&\& exec "$WINE" --bottle=ltspice --wait-children "$EXE" "$@" 9>\&- ) >|' "$F/tools/ltspice-batch.sh"
echo "\$ diff <frozen wrapper> <scratch copy>"; diff $R/tools/ltspice-batch.sh "$F/tools/ltspice-batch.sh"
echo "\$ (cd <scratch copy> && .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -k test_child_holds_no_lock_descriptor -v)"
(cd "$F" && $PY -m unittest discover -s tools/tests -p test_ltspice_batch.py -k test_child_holds_no_lock_descriptor -v 2>&1)
F_RC=$?
echo "exit=$F_RC (expected 1: the case fails on the old line)"
rm -rf "$F"
echo
echo "## G. regression cases of INSP-038 finding-21 on the wrapper of blob bdc4513f (scratch copy; test doubles only)"
G=$(mktemp -d "${TMPDIR:-/tmp}/kat-lts-f21.XXXXXX")
mkdir -p "$G/tools/tests/fixtures"
git -C $R cat-file -p bdc4513ff1b63aa76717e0cf669ae2a08b1b841a > "$G/tools/ltspice-batch.sh"; chmod 755 "$G/tools/ltspice-batch.sh"
cp $R/tools/tests/test_ltspice_batch.py "$G/tools/tests/"
cp -R $R/tools/tests/fixtures/ltspice "$G/tools/tests/fixtures/"
echo "scratch wrapper blob $(git -C $R hash-object "$G/tools/ltspice-batch.sh") (expected bdc4513ff1b63aa76717e0cf669ae2a08b1b841a)"
echo "\$ (cd <scratch copy> && .venv/bin/python -m unittest discover -s tools/tests -p test_ltspice_batch.py -k bystander -v)"
(cd "$G" && $PY -m unittest discover -s tools/tests -p test_ltspice_batch.py -k bystander -v 2>&1)
G_RC=$?
echo "exit=$G_RC (expected 1: both cases fail on blob bdc4513f)"
rm -rf "$G"
echo
echo "## result"
echo "part C unit-test module exit=$C_RC (a pass needs exit 0 and no skip other than the permitted one); part D wrapper exit=$D_RC (expected 0); part E exit=$E_RC (expected 0, no Wine process of the bottle or bundle, lock holder only lockf); part F exit=$F_RC (expected 1); part G exit=$G_RC (expected 1); key_count $(keycount)"
