#!/bin/bash
# OpenSCAD 2021.01 + FreeCAD 1.1.3 sanity check runner (scratch procedure; transcript kept as evidence). Headless CLI only.
OS=/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD
FCC=/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd
FX=/Users/robinonsay/rust/cwht/tools/tests/fixtures/openscad
EVD=/Users/robinonsay/rust/cwht/docs/cm/tool-validation/evidence
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-openscad.XXXXXX")
run() { echo "\$ $*"; "$@" > "$W/out.txt" 2>&1; rc=$?; grep -v '^\s*$' "$W/out.txt" | tail -${TAILN:-15}; echo "exit=$rc"; LASTRC=$rc; }
echo "# OpenSCAD + FreeCAD sanity check, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm)"
echo "# repository HEAD $(git -C /Users/robinonsay/rust/cwht rev-parse HEAD)"
(cd $FX && shasum -a 256 cube.scad known-answers.json); shasum -a 256 "$SCAD2STEP"
cp $FX/cube.scad $FX/known-answers.json $W/; cp "$SCAD2STEP" $W/scad2step_research.py; cd $W
run $OS --version; OV=$(tail -1 out.txt)
run defaults read /Applications/FreeCAD.app/Contents/Info.plist CFBundleVersion; FV=$(tail -1 out.txt)
run $OS -o cube.csg cube.scad; C=$LASTRC
echo "## cube.csg"; cat cube.csg
run $OS --render --imgsize=800,600 --viewall --autocenter -o cube.png cube.scad; P=$LASTRC
run $OS -o cube.step cube.scad; S=$LASTRC; [ -e cube.step ] && echo "cube.step WRITTEN" || echo "no cube.step written"; STEPX=$([ -e cube.step ] && echo 1 || echo 0); rm -f cube.step
TAILN=30 CWHT_CSG=cube.csg CWHT_STEP=cube.step run env CWHT_CSG=cube.csg CWHT_STEP=cube.step $FCC $W/scad2step_research.py; F=$LASTRC; cp out.txt fcc.txt
echo "## comparison against known-answers.json"
$PY - "$W" "$OV" "$FV" "$C $P $S $STEPX $F" <<'PYEOF'
import json, re, struct, sys, pathlib, zlib
w = pathlib.Path(sys.argv[1]); ov, fv = sys.argv[2:4]; c, p, s, stepx, f = map(int, sys.argv[4].split())
k = json.loads((w / 'known-answers.json').read_text()); ok = True
def check(name, cond, detail):
    global ok
    ok = ok and cond; print(('PASS ' if cond else 'FAIL ') + name + ': ' + detail)
check('versions', ov == k['openscad_version'] and fv == k['freecad_version'], f'{ov} | FreeCAD {fv}')
csg = (w / 'cube.csg').read_text(); miss = [m for m in k['csg_export']['must_contain'] if m not in csg]
check('CSG export', c == 0 and not miss, f'exit {c}, missing {miss}')
png = (w / 'cube.png').read_bytes() if (w / 'cube.png').exists() else b''
wh = struct.unpack('>II', png[16:24]) if png[:8] == b'\x89PNG\r\n\x1a\n' else None
check('PNG render', p == 0 and wh == tuple(k['png_render']['size_px']), f'exit {p}, size {wh}')
check('STEP refused by OpenSCAD', s != 0 and stepx == 0, f'exit {s}, file written {bool(stepx)}')
m = re.search(r'KAT solids=(\d+) valid=(\w+) faces=(\d+) cylinders=(\d+) bspline=(\d+) volume=([0-9.]+) step_reread_solids=(\d+) step_reread_volume=([0-9.]+)', (w / 'fcc.txt').read_text())
e = k['step_export']
if not m:
    check('FreeCAD STEP export', False, f'exit {f}, no KAT line')
else:
    sol, val, nf, cyl, bs, vol, rsol, rvol = int(m[1]), m[2] == 'True', int(m[3]), int(m[4]), int(m[5]), float(m[6]), int(m[7]), float(m[8])
    check('FreeCAD STEP export', f == 0 and sol == e['solids'] and val == e['valid'] and bs == e['bspline_faces'] and nf == e['faces'] and cyl == e['cylindrical_faces'], f'exit {f}, solids {sol}, valid {val}, faces {nf}, cylinders {cyl}, bspline {bs}')
    check('volume', abs(vol - e['volume_mm3']) / e['volume_mm3'] <= e['volume_tolerance_fraction'] and rsol == 1 and abs(rvol - vol) / vol <= 1e-6, f'shape {vol:.3f} mm^3, STEP re-read {rvol:.3f} mm^3 ({rsol} solid), expected {e["volume_mm3"]} mm^3, error {abs(vol - e["volume_mm3"]) / e["volume_mm3"] * 100:.4f} %')
    step = (w / 'cube.step').read_text()
    cp = {g[0]: tuple(float(x) for x in g[1:]) for g in re.findall(r"#(\d+)\s*=\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*\)", step)}
    pts = [cp[i] for i in re.findall(r"VERTEX_POINT\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*\)", step)]
    box = {a: [min(q[i] for q in pts), max(q[i] for q in pts)] for i, a in enumerate('xyz')} if pts else {}
    tol = e['bounding_box_tolerance_mm']; exp = e['bounding_box_mm']
    check('STEP bounding box', bool(pts) and all(abs(box[a][j] - exp[a][j]) <= tol for a in 'xyz' for j in (0, 1)), f'{len(pts)} vertices, box {box}')
    print('STEP header:', re.search(r"FILE_SCHEMA\s*\(\s*\(\s*'([^']+)'", step)[1] if re.search(r"FILE_SCHEMA\s*\(\s*\(\s*'([^']+)'", step) else 'n/a')
print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
PYEOF
echo "exit=$?"
[ -n "$KEEP_PNG" ] && cp cube.png "$KEEP_PNG"
cd /; rm -rf "$W"
