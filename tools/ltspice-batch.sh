#!/bin/bash
# tools/ltspice-batch.sh: headless LTspice 26.0.2 batch runner for cwht (class B tool, TV-014).
#
# Runs the Windows LTspice.exe inside the CrossOver bottle of /Applications/LTspice.app through the
# bottle's own wine (docs/research/ltspice-batch-macos.md F3); the app launcher form
# 'Contents/MacOS/LTspice -b' exits 0 without simulating (F2) and is never used.
#
# Usage (from any directory; paths may be relative or absolute):
#   tools/ltspice-batch.sh [-t SECONDS] [-o OUTDIR] [-ascii] -b DECK.net|DECK.cir|DECK.asc
#   tools/ltspice-batch.sh [-t SECONDS] [-o OUTDIR] -netlist SCHEMATIC.asc
#   tools/ltspice-batch.sh [-t SECONDS] -version
#
# What it does, in order (tools/toolchain.lock.md section 1.4 findings 1 and 2; TV-014):
#  1. Deck hygiene: the deck and every relative .include/.inc/.lib file it names (recursively) are
#     copied into a fresh short run directory under $(getconf DARWIN_USER_TEMP_DIR); a relative path with a '..' component is
#     refused (exit 2); for a schematic, the *.asy symbol files beside it are copied too. The longest
#     Windows path LTspice will write (Z:\<run dir>\<deck>.op.raw) must be under 260 characters, because
#     LTspice exits 0 without simulating when it cannot open a longer path (TV-014 finding 1).
#  2. Serialization: one LTspice run at a time for the user, by an flock(2) lock on
#     $(getconf DARWIN_USER_TEMP_DIR)cwht-ltspice.lock held for the rest of the run (waits up to
#     CWHT_LTSPICE_LOCK_WAIT seconds, default 600). LTspice rewrites its whole ini at exit, and
#     concurrent exits truncated it and removed the telemetry opt-out (TV-014 finding 2).
#  3. Installation and version: the bundle's wine must exist and the bundle version must start with
#     the locked program version (CWHT_LTSPICE_VERSION, default 26.0.2); after a -b run the .log first
#     line must read "LTspice <version> for MacOS"; -version must print exactly that version.
#  4. Precondition: CaptureAnalytics=false in the bottle's UTF-16LE LTspice.ini, read through iconv and
#     never written (SI-027, ADR-018). If CWHT_LTSPICE_INI_CHECK names a file, that file must carry the
#     key as well (a known-answer hook: it can only add a failure, never waive the bottle check).
#  5. Run with a time-out (default 120 s, -t to change). On time-out only this run's processes are
#     killed: those whose command line holds the unique run directory, then the launcher's own process
#     tree; never a machine-wide 'pkill LTspice.exe'.
#  6. Result checks: the bottle ini still holds CaptureAnalytics=false after the run (else exit 3, no
#     outputs copied); LTspice exit status 0; a .log exists (-b); the log carries none of the failure
#     strings below; a -b run wrote <deck>.raw or <deck>.op.raw; no netlist written by the run holds a
#     floating 'NC_' net (research F9).
#  7. Outputs (<deck>.net, .log, .raw, .op.raw and any other <deck>.* file LTspice wrote) are copied
#     to OUTDIR (default: the deck's directory, as LTspice itself would write them) after the .log, .raw,
#     .op.raw and .db (and the .net of a schematic) of any earlier run there are removed; the .log is
#     converted to UTF-8 when LTspice wrote it as UTF-16LE. A provenance line goes to stderr: version
#     line, deck SHA-256, exit status, elapsed seconds, outputs.
#
# The wrapper judges only whether LTspice ran the deck; whether the result meets a requirement is the
# job of the deck's checker (hardware/sim/<block>/), which reads the .raw or the .meas lines of the log.
#
# Exit status: 0 pass; 1 LTspice failed (non-zero exit, no log, failure string in the log, no raw
# output, NC_ net); 2 usage error or deck refused by the hygiene checks; 3 precondition failed
# (LTspice not installed, telemetry opt-out absent before or after the run); 4 version differs from
# the lock; 5 busy (the lock was not free within CWHT_LTSPICE_LOCK_WAIT); 124 time-out (run killed,
# counted as a failure).
#
# Environment: CWHT_LTSPICE_VERSION (locked program version, default 26.0.2); CWHT_LTSPICE_LOCK_WAIT
# (seconds to wait for another run, default 600); CWHT_LTSPICE_INI_CHECK
# (additional ini that must also carry the key; test hook); CWHT_LTSPICE_KEEP=1 keeps the run directory
# for inspection; CWHT_LTSPICE_SUPPORT (bundle SharedSupport/ltspice directory; test hook for the
# not-installed case).
set -u

SUPPORT="${CWHT_LTSPICE_SUPPORT:-/Applications/LTspice.app/Contents/SharedSupport/ltspice}"
APP_PLIST="/Applications/LTspice.app/Contents/Info.plist"
WINE="$SUPPORT/bin/wine"
EXE='C:\Program Files\ADI\LTspice\LTspice.exe'
INI="$HOME/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini"
VERSION="${CWHT_LTSPICE_VERSION:-26.0.2}"
LOCK_WAIT="${CWHT_LTSPICE_LOCK_WAIT:-600}"
TIMEOUT=120
OUTDIR=""
MODE=""
DECK=""
ASCII=""
ME="ltspice-batch"
# Log strings that mean LTspice did not complete the analysis even when it exits 0.
FAIL_STRINGS='Could not open|Fatal Error|Error:|Unknown dot command|Singular matrix|Time step too small|Analysis: .* failed|Missing value|syntax error|Unknown subcircuit|Unknown parameter|More than one analysis specified|Could not find|No analysis|Unable to'
WINE_NOISE='mvk-info|^[[:space:]]+(VK_|GPU|macOS GPU|Metal|model:|type:|vendorID|deviceID|pipelineCache|supports|The following)'

say() { echo "$ME: $*" >&2; }
die() { local code=$1; shift; say "$*"; exit "$code"; }
usage() {
  echo "usage: tools/ltspice-batch.sh [-t SECONDS] [-o OUTDIR] [-ascii] -b DECK" >&2
  echo "       tools/ltspice-batch.sh [-t SECONDS] [-o OUTDIR] -netlist SCHEMATIC.asc" >&2
  echo "       tools/ltspice-batch.sh [-t SECONDS] -version" >&2
  exit 2
}

# --- arguments -------------------------------------------------------------------------------
[ $# -eq 0 ] && usage
while [ $# -gt 0 ]; do
  case "$1" in
    -t) [ $# -ge 2 ] || usage; TIMEOUT="$2"; shift 2 ;;
    -o) [ $# -ge 2 ] || usage; OUTDIR="$2"; shift 2 ;;
    -ascii) ASCII="-ascii"; shift ;;
    -b|-netlist) [ -z "$MODE" ] || usage; [ $# -ge 2 ] || usage; MODE="$1"; DECK="$2"; shift 2 ;;
    -version) [ -z "$MODE" ] || usage; MODE="-version"; shift ;;
    -h|--help) usage ;;
    *) say "unknown argument: $1"; usage ;;
  esac
done
[ -n "$MODE" ] || usage
case "$TIMEOUT" in ''|*[!0-9]*) die 2 "-t needs a whole number of seconds, got '$TIMEOUT'" ;; esac
[ "$TIMEOUT" -ge 1 ] || die 2 "-t must be at least 1 s"
[ "$MODE" = "-netlist" ] && [ -n "$ASCII" ] && die 2 "-ascii applies to -b only"
[ "$MODE" = "-version" ] && [ -n "$OUTDIR" ] && die 2 "-o does not apply to -version"

# --- helpers -------------------------------------------------------------------------------------
to_utf8() {  # print a LTspice text file as UTF-8 without CR or NUL (LTspice writes UTF-16LE or 8-bit)
  local b
  b=$(head -c 2 "$1" | od -An -tx1 | tr -d ' \n')
  case "$b" in
    fffe) tail -c +3 "$1" | iconv -f UTF-16LE -t UTF-8 ;;
    ??00) iconv -f UTF-16LE -t UTF-8 "$1" ;;
    *) cat "$1" ;;
  esac | tr -d '\r\000'
}
kill_tree() {  # $1 = pid; kill the process and its descendants, children first
  local p c
  p=$1
  for c in $(pgrep -P "$p" 2>/dev/null); do kill_tree "$c"; done
  kill "$p" 2>/dev/null
}
abs_path() {  # absolute path of an existing file
  ( cd "$(dirname "$1")" 2>/dev/null && printf '%s/%s\n' "$(pwd -P)" "$(basename "$1")" )
}

# --- 1. deck hygiene and run directory ----------------------------------------------------------
# The run directory lives in the per-user temporary directory (short, /var/folders/.../T/), not in a
# possibly long $TMPDIR, so that the Windows paths stay well inside MAX_PATH.
TMPBASE="$(getconf DARWIN_USER_TEMP_DIR 2>/dev/null)"
[ -n "$TMPBASE" ] && [ -d "$TMPBASE" ] || TMPBASE="${TMPDIR:-/tmp}/"
RUN=$(mktemp -d "${TMPBASE%/}/cwht-lts.XXXXXX") || die 3 "cannot create a run directory"
RUN=$(cd "$RUN" && pwd -P)
cleanup() { [ "${CWHT_LTSPICE_KEEP:-0}" = "1" ] && say "run directory kept: $RUN" || rm -rf "$RUN"; }
trap cleanup EXIT
trap 'pkill -f -- "$RUN" 2>/dev/null; exit 130' INT TERM

BASE=""
if [ "$MODE" != "-version" ]; then
  [ -f "$DECK" ] || die 2 "deck not found: $DECK"
  DECK_ABS=$(abs_path "$DECK") || die 2 "cannot resolve deck path: $DECK"
  DECK_DIR=$(dirname "$DECK_ABS")
  DECK_NAME=$(basename "$DECK_ABS")
  case "$DECK_NAME" in
    *.net|*.cir|*.sp) KIND=netlist ;;
    *.asc) KIND=schematic ;;
    *) die 2 "deck must be a .net, .cir, .sp or .asc file: $DECK_NAME" ;;
  esac
  [ "$MODE" = "-netlist" ] && [ "$KIND" != schematic ] && die 2 "-netlist needs a schematic (.asc)"
  case "$DECK_NAME" in *[[:space:]]*) die 2 "deck file name contains white space: $DECK_NAME" ;; esac
  BASE="${DECK_NAME%.*}"
  [ -z "$OUTDIR" ] && OUTDIR="$DECK_DIR"
  mkdir -p "$OUTDIR" || die 2 "cannot create output directory $OUTDIR"
  OUTDIR=$(cd "$OUTDIR" && pwd -P)

  # Windows path limit: Z:\<run dir>\<base>.op.raw must stay below MAX_PATH (260).
  LONGEST="Z:$RUN/$BASE.op.raw"
  [ ${#LONGEST} -lt 260 ] || die 2 "Windows path of the outputs would be ${#LONGEST} characters (limit 259): shorten the deck name or TMPDIR"

  cp "$DECK_ABS" "$RUN/$DECK_NAME" || die 2 "cannot copy the deck"
  # Copy relative include files, recursively; refuse '..' components; leave absolute paths and
  # names LTspice resolves from its own library (files that do not exist beside the deck).
  QUEUE="$RUN/.queue"; DONE="$RUN/.done"
  echo "$DECK_NAME" > "$QUEUE"; : > "$DONE"
  while [ -s "$QUEUE" ]; do
    f=$(head -n 1 "$QUEUE"); tail -n +2 "$QUEUE" > "$QUEUE.t"; mv "$QUEUE.t" "$QUEUE"
    /usr/bin/grep -qxF -- "$f" "$DONE" && continue
    echo "$f" >> "$DONE"
    to_utf8 "$RUN/$f" | sed -n -E 's/^([[:space:]]*|TEXT[^!]*!)[[:space:]]*\.(inc|include|lib)[[:space:]]+"?([^"[:space:]]+)"?.*$/\3/Ip' > "$RUN/.refs"
    while IFS= read -r ref; do
      [ -z "$ref" ] && continue
      case "$ref" in /*|[A-Za-z]:*) continue ;; esac
      case "/$ref/" in */../*) die 2 "include path with a '..' component refused: $ref (in $f); decks for the record are self-contained below their directory" ;; esac
      src="$(dirname "$DECK_DIR/$f")/$ref"
      [ -f "$src" ] || continue
      rel="$(dirname "$f")/$ref"; rel="${rel#./}"
      mkdir -p "$RUN/$(dirname "$rel")" && cp "$src" "$RUN/$rel" || die 2 "cannot copy include $src"
      echo "$rel" >> "$QUEUE"
    done < "$RUN/.refs"
  done
  rm -f "$QUEUE" "$DONE" "$RUN/.refs"
  if [ "$KIND" = schematic ]; then
    for s in "$DECK_DIR"/*.asy; do [ -f "$s" ] && cp "$s" "$RUN/"; done
  fi
  DECK_SHA=$(shasum -a 256 "$DECK_ABS" | cut -d ' ' -f 1)
fi

# --- 2. one LTspice run at a time on this machine ------------------------------------------------
# LTspice rewrites its whole LTspice.ini (recent-file list) when it exits. On 2026-09-27 four
# concurrent runs truncated the ini to the recent-file list and removed CaptureAnalytics=false
# (TV-014 finding 2), so every run holds an exclusive flock(2) lock, shared by all sessions of the
# user, from before the precondition check until after the post-run ini check. The lock is released
# by the kernel when this shell exits, so a killed wrapper leaves no stale lock.
LOCKFILE="${TMPBASE%/}/cwht-ltspice.lock"
case "$LOCK_WAIT" in ''|*[!0-9]*) die 2 "CWHT_LTSPICE_LOCK_WAIT needs a whole number of seconds" ;; esac
exec 9>"$LOCKFILE" || die 3 "cannot open the lock file $LOCKFILE"
if ! /usr/bin/lockf -s -t 0 9; then
  say "another LTspice run holds $LOCKFILE; waiting up to $LOCK_WAIT s"
  /usr/bin/lockf -s -t "$LOCK_WAIT" 9 || die 5 "busy: another LTspice run held the lock for more than $LOCK_WAIT s"
fi

# --- 3. installation and version against the lock (bundle) -------------------------------------
[ -x "$WINE" ] || die 3 "LTspice not installed: $WINE is not executable (tools/toolchain.lock.md section 1)"
if [ -z "${CWHT_LTSPICE_SUPPORT:-}" ]; then
  BUNDLE=$(defaults read "$APP_PLIST" CFBundleShortVersionString 2>/dev/null || echo unknown)
  case "$BUNDLE" in
    "$VERSION"|"$VERSION".*) ;;
    *) die 4 "LTspice bundle version $BUNDLE is not the locked version $VERSION (tools/toolchain.lock.md section 1; a version change is a CR plus a new TV record)" ;;
  esac
fi

# --- 4. precondition: telemetry opt-out --------------------------------------------------------
ini_has_key() {  # $1 = ini path; UTF-16LE with CRLF line ends (lock section 1.4 finding 1); read only
  [ -f "$1" ] || return 1
  iconv -f UTF-16LE -t UTF-8 "$1" 2>/dev/null | tr -d '\r' | /usr/bin/grep -q '^CaptureAnalytics=false$'
}
ini_has_key "$INI" || die 3 "precondition failed: CaptureAnalytics=false not found in the bottle LTspice.ini (SI-027, ADR-018); answer 'No' once in the LTspice consent dialog, never append to the UTF-16LE file"
if [ -n "${CWHT_LTSPICE_INI_CHECK:-}" ]; then
  ini_has_key "$CWHT_LTSPICE_INI_CHECK" || die 3 "precondition failed: CaptureAnalytics=false not found in CWHT_LTSPICE_INI_CHECK file $CWHT_LTSPICE_INI_CHECK"
fi

# --- 5. run with time-out -----------------------------------------------------------------------
if [ "$MODE" = "-version" ]; then
  set -- -version
else
  set -- $ASCII "$MODE" "$RUN/$DECK_NAME"
fi
( cd "$RUN" && exec "$WINE" --bottle=ltspice --wait-children "$EXE" "$@" 9>&- ) > "$RUN/.stdout" 2> "$RUN/.stderr" &
PID=$!
START=$(date +%s)
TIMED_OUT=0
while kill -0 "$PID" 2>/dev/null; do
  if [ $(( $(date +%s) - START )) -ge "$TIMEOUT" ]; then
    TIMED_OUT=1
    pkill -f -- "$RUN" 2>/dev/null
    kill_tree "$PID"
    sleep 1
    pkill -9 -f -- "$RUN" 2>/dev/null
    break
  fi
  sleep 0.2
done
wait "$PID" 2>/dev/null
RC=$?
ELAPSED=$(( $(date +%s) - START ))
INI_AFTER=ok
ini_has_key "$INI" || INI_AFTER=lost
if [ "$INI_AFTER" = lost ]; then
  die 3 "post-run check failed: the bottle LTspice.ini no longer holds CaptureAnalytics=false after this run (SI-027, ADR-018); stop all LTspice work and report it to the owner; outputs not copied"
fi
/usr/bin/grep -v -E "$WINE_NOISE" "$RUN/.stderr" >&2 || true

if [ "$TIMED_OUT" = 1 ]; then
  sleep 1
  if pgrep -f -- "$RUN" >/dev/null 2>&1; then
    say "time-out after $TIMEOUT s; WARNING: processes of this run survive: $(pgrep -f -- "$RUN" | tr '\n' ' ')"
  else
    say "time-out after $TIMEOUT s; this run's processes killed (matched on $RUN), none left"
  fi
  say "result: FAIL (time-out) deck=${DECK_NAME:-none} sha256=${DECK_SHA:-none} elapsed=${ELAPSED}s"
  exit 124
fi

# --- 6. result checks ---------------------------------------------------------------------------
if [ "$MODE" = "-version" ]; then
  OUT=$(to_utf8 "$RUN/.stdout" | tr -d '\n')
  cat "$RUN/.stdout"
  [ "$RC" -eq 0 ] || die 1 "LTspice -version exited $RC"
  [ "$OUT" = "$VERSION" ] || die 4 "LTspice reports version '$OUT', locked version is $VERSION"
  say "result: PASS version=$OUT elapsed=${ELAPSED}s"
  exit 0
fi

STATUS=0
REASON=""
fail() { [ "$STATUS" = 0 ] && STATUS=$1; REASON="${REASON:+$REASON; }$2"; }

LOG="$RUN/$BASE.log"
VLINE=""
if [ -f "$LOG" ]; then
  to_utf8 "$LOG" > "$RUN/.log.utf8"
  VLINE=$(head -n 1 "$RUN/.log.utf8")
  HIT=$(/usr/bin/grep -E -m 1 -- "$FAIL_STRINGS" "$RUN/.log.utf8" || true)
  [ -n "$HIT" ] && fail 1 "log reports: $HIT"
fi
[ "$RC" -eq 0 ] || fail 1 "LTspice exited $RC"
if [ "$MODE" = "-b" ]; then
  [ -f "$LOG" ] || fail 1 "no log written"
  if [ -f "$LOG" ] && [ "$VLINE" != "LTspice $VERSION for MacOS" ]; then
    case "$VLINE" in
      "LTspice "*" for MacOS") fail 4 "log names '$VLINE', locked version is $VERSION" ;;
      *) : ;;  # an error log may start with the error text; the failure string check covers it
    esac
  fi
  [ -f "$RUN/$BASE.raw" ] || [ -f "$RUN/$BASE.op.raw" ] || fail 1 "no raw output written"
fi
if [ "$MODE" = "-netlist" ] || [ "$KIND" = schematic ]; then
  if [ -f "$RUN/$BASE.net" ]; then
    NC=$(to_utf8 "$RUN/$BASE.net" | /usr/bin/grep -o -E '\bNC_[0-9]+' | sort -u | tr '\n' ' ')
    [ -n "$NC" ] && fail 1 "netlist holds floating nets: $NC(research F9)"
  else
    fail 1 "no netlist written"
  fi
fi

# --- 7. outputs back to OUTDIR -------------------------------------------------------------------
# Remove the outputs of an earlier run first, so that a checker never reads a stale file that this
# run did not write (only LTspice output extensions; the deck and user files such as .plt are kept).
for x in log raw op.raw db; do rm -f "$OUTDIR/$BASE.$x"; done
[ "$KIND" = schematic ] && rm -f "$OUTDIR/$BASE.net"
COPIED=""
for f in "$RUN/$BASE".*; do
  [ -f "$f" ] || continue
  n=$(basename "$f")
  [ "$n" = "$DECK_NAME" ] && continue
  if [ "$n" = "$BASE.log" ]; then
    cp "$RUN/.log.utf8" "$OUTDIR/$n"
  else
    cp "$f" "$OUTDIR/$n"
  fi
  COPIED="$COPIED $n"
done

PROV="deck=$DECK_NAME sha256=$DECK_SHA version_line='${VLINE:-none}' ltspice_exit=$RC elapsed=${ELAPSED}s outputs=[${COPIED# }] outdir=$OUTDIR"
if [ "$STATUS" = 0 ]; then
  say "result: PASS $PROV"
else
  say "result: FAIL ($REASON) $PROV"
fi
exit "$STATUS"
