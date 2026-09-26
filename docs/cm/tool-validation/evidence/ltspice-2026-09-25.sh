#!/bin/bash
# LTspice sanity check runner (scratch procedure; transcript kept as evidence). Headless: CrossOver wine, no GUI.
S=/Applications/LTspice.app/Contents/SharedSupport/ltspice
INI="$HOME/Library/Application Support/LTspice/Bottles/ltspice/drive_c/users/crossover/AppData/Roaming/LTspice.ini"
FX=/Users/robinonsay/rust/cwht/tools/tests/fixtures/ltspice
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-ltspice.XXXXXX")
lt() {  # run LTspice.exe with a guard (LIMIT s, default 120); kills only processes whose command line holds this run's unique directory
  echo "\$ $S/bin/wine --bottle=ltspice --wait-children 'C:\\Program Files\\ADI\\LTspice\\LTspice.exe' $*"
  "$S/bin/wine" --bottle=ltspice --wait-children 'C:\Program Files\ADI\LTspice\LTspice.exe' "$@" > "$W/stdout.txt" 2> "$W/stderr.txt" &
  pid=$!; n=0; lim=${LIMIT:-120}
  while kill -0 $pid 2>/dev/null; do sleep 1; n=$((n+1)); if [ $n -eq $lim ]; then pkill -f "$W"; echo "TIMEOUT after $lim s, killed (pkill -f <unique run directory>)"; fi; done
  wait $pid; rc=$?
  cat "$W/stdout.txt"; grep -v -E 'mvk-info|^\s+(VK_|GPU|macOS GPU|Metal|model:|type:|vendorID|deviceID|pipelineCache|supports|The following)' "$W/stderr.txt" | head -5
  echo "exit=$rc (${n} s)"; LASTRC=$rc
}
echo "# LTspice sanity check, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm)"
echo "# repository HEAD $(git -C /Users/robinonsay/rust/cwht rev-parse HEAD)"
(cd $FX && shasum -a 256 rc-lowpass.asc rc-seeded-error.net rc-hang-error.asc known-answers.json)
echo "\$ defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString"; defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString
echo "\$ grep '\"Version\"' $S/support/ltspice/cxbottle.conf"; grep '"Version"' $S/support/ltspice/cxbottle.conf
echo "\$ file <bottle LTspice.ini>"; file -b "$INI"
echo "\$ /usr/bin/grep -c CaptureAnalytics <bottle LTspice.ini>   (byte grep on the UTF-16LE file: expected 0, informative)"; /usr/bin/grep -c CaptureAnalytics "$INI"
echo "\$ iconv -f UTF-16LE -t UTF-8 <bottle LTspice.ini> | /usr/bin/grep '^CaptureAnalytics='"; iconv -f UTF-16LE -t UTF-8 "$INI" | tr -d '\r' | /usr/bin/grep '^CaptureAnalytics=false$' || { echo "precondition FAILED: CaptureAnalytics=false missing; stop"; exit 2; }
cp $FX/rc-lowpass.asc $FX/rc-seeded-error.net $FX/rc-hang-error.asc $FX/known-answers.json $W/; cd $W
lt -version; V_RC=$LASTRC; cp stdout.txt version.txt
lt -netlist $W/rc-lowpass.asc; N_RC=$LASTRC
echo "## rc-lowpass.net"; cat rc-lowpass.net | tr -d '\r'
lt -b $W/rc-lowpass.asc; B_RC=$LASTRC
echo "## rc-lowpass.log"; tr -d '\r\000' < rc-lowpass.log
lt -b $W/rc-seeded-error.net; E_RC=$LASTRC
echo "## rc-seeded-error.log"; tr -d '\r\000' < rc-seeded-error.log
LIMIT=30 lt -b $W/rc-hang-error.asc; H_RC=$LASTRC
echo "## rc-hang-error outputs"; ls rc-hang-error.* 2>&1
echo "## outputs"; ls -la
echo "## comparison against known-answers.json"
$PY - "$W" "$V_RC" "$N_RC" "$B_RC" "$E_RC" "$H_RC" <<'PYEOF'
import json, re, sys, pathlib
w = pathlib.Path(sys.argv[1]); v_rc, n_rc, b_rc, e_rc, h_rc = map(int, sys.argv[2:7]); k = json.loads((w / 'known-answers.json').read_text()); ok = True
def rd(p):
    b = (w / p).read_bytes()
    t = b.decode('utf-16-le') if b[:2] == b'\xff\xfe' or (len(b) > 1 and b[1] == 0) else b.decode('latin-1')
    return t.replace('\r', '').replace('\x00', '').lstrip('\ufeff')
def check(name, cond, detail):
    global ok
    ok = ok and cond; print(('PASS ' if cond else 'FAIL ') + name + ': ' + detail)
ver = rd('version.txt').strip()
check('version', v_rc == 0 and ver == k['version']['stdout'], f'exit {v_rc}, stdout {ver!r}')
net = rd('rc-lowpass.net')
check('netlist', n_rc == 0 and all(s in net for s in k['netlist']['must_contain']) and not any(s in net for s in k['netlist']['must_not_contain']), f'exit {n_rc}')
log = rd('rc-lowpass.log'); first = log.splitlines()[0].strip()
m = re.search(r'f3db:.*?\bAT\s+([-0-9.eE+]+)', log, re.I)
f = float(m.group(1)) if m else float('nan'); exp = k['simulation']['f3db_hz']; err = abs(f - exp) / exp
check('log first line', first == k['simulation']['log_first_line'], repr(first))
check('f3db', b_rc == 0 and err <= k['simulation']['f3db_tolerance_fraction'], f'exit {b_rc}, f3db {f} Hz, expected {exp} Hz, error {err*100:.4f} %')
elog = rd('rc-seeded-error.log')
check('seeded error', e_rc == k['seeded_error']['exit'] and k['seeded_error']['log_must_contain'] in elog, f'exit {e_rc}')
check('hang case', h_rc == 143 and not (w / 'rc-hang-error.log').exists(), f'exit {h_rc}, log present {(w / "rc-hang-error.log").exists()}')
print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
PYEOF
echo "exit=$?"
sleep 3; echo "## processes of this run still alive (expected none)"; pgrep -fl "$W" || echo none
cd /; rm -rf "$W"
