#!/bin/bash
# kicad-cli sanity check runner (scratch; transcript kept as evidence)
K=/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
FX=/Users/robinonsay/rust/cwht/tools/tests/fixtures/kicad
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-kicad.XXXXXX")
run() { echo "\$ $*"; "$@"; echo "exit=$?"; }
echo "# kicad-cli sanity check, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm)"
echo "# repository HEAD $(git -C /Users/robinonsay/rust/cwht rev-parse HEAD); fixture tree $(cd $FX && shasum -a 256 clean.* seeded.* sym-lib-table fp-lib-table known-answers.json expected/* | shasum -a 256 | cut -c1-16) (sha256 of the file list below)"
(cd $FX && shasum -a 256 clean.* seeded.* sym-lib-table fp-lib-table known-answers.json expected/*)
cp -R $FX/. $W/; cd $W; mkdir out out2
run $K version
for f in clean seeded; do run $K sch erc --format json --severity-all --exit-code-violations -o $f-erc.json $f.kicad_sch; done
for f in clean seeded; do run $K pcb drc --format json --severity-all --exit-code-violations -o $f-drc.json $f.kicad_pcb; done
run $K pcb export drill -o out/ --format excellon --drill-origin plot --excellon-units mm --excellon-zeros-format decimal --excellon-oval-format route --excellon-separate-th --generate-map --map-format pdf --generate-report --report-path out/clean-drill-report.rpt clean.kicad_pcb
run $K pcb export pos -o out/clean-cpl.csv --format csv --units mm --use-drill-file-origin --side both --smd-only --exclude-dnp clean.kicad_pcb
run $K sch export bom -o out/clean-bom.csv clean.kicad_sch
run $K pcb export step --board-only --drill-origin -o out/clean.step clean.kicad_pcb
echo "## drill report"; cat out/clean-drill-report.rpt
echo "## CPL"; cat out/clean-cpl.csv; echo "## BOM"; cat out/clean-bom.csv
echo "## comparison against known-answers.json"
$PY - "$W" <<'PYEOF'
import json, re, sys, pathlib
w = pathlib.Path(sys.argv[1]); k = json.loads((w / 'known-answers.json').read_text()); ok = True
def check(name, cond, detail):
    global ok
    ok = ok and cond
    print(('PASS ' if cond else 'FAIL ') + name + ': ' + detail)
for f in ('clean', 'seeded'):
    d = json.loads((w / f'{f}-erc.json').read_text())
    got = [[v['type'], v['severity']] + [i['description'] for i in v['items']] for s in d['sheets'] for v in s['violations']]
    check(f'ERC {f}', got == k['erc'][f]['violations'], str(got))
    d = json.loads((w / f'{f}-drc.json').read_text())
    got = [[v['type'], v['severity'], v['description']] + [i['description'] for i in v['items'] if i['description'].startswith('Pad')] for v in d['violations']]
    check(f'DRC {f}', got == k['drc'][f]['violations'] and len(d['unconnected_items']) == k['drc'][f]['unconnected_items'], f"{got}; unconnected {len(d['unconnected_items'])}")
rpt = (w / 'out' / 'clean-drill-report.rpt').read_text()
print('drill files:', sorted(p.name for p in (w / 'out').glob('*.drl')))
pth = (w / 'out' / 'clean-PTH.drl').read_text(); npth = (w / 'out' / 'clean-NPTH.drl').read_text()
hits = lambda t: len(re.findall(r'^X-?[0-9.]+Y-?[0-9.]+$', t, re.M))
tools_ = lambda t: re.findall(r'^T\d+C([0-9.]+)', t, re.M)
check('drill PTH', hits(pth) == k['drill']['plated_holes'] and [float(x) for x in tools_(pth)] == [k['drill']['plated_diameter_mm']], f'hits {hits(pth)}, tools {tools_(pth)}')
check('drill NPTH', hits(npth) == k['drill']['non_plated_holes'] and [float(x) for x in tools_(npth)] == [k['drill']['non_plated_diameter_mm']], f'hits {hits(npth)}, tools {tools_(npth)}')
for key in ('cpl', 'bom'):
    got = (w / 'out' / f'clean-{key}.csv').read_text().splitlines(); exp = (w / k[key]['expected_file']).read_text().splitlines()
    check(key.upper(), got == exp, f'{len(got)} lines vs {len(exp)} stored')
step = (w / 'out' / 'clean.step').read_text()
cp = {m.group(1): tuple(float(x) for x in m.groups()[1:]) for m in re.finditer(r"#(\d+)\s*=\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*,\s*([-0-9.Ee+]+)\s*\)", step)}
pts = [cp[m.group(1)] for m in re.finditer(r"VERTEX_POINT\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*\)", step)]
box = {a: [min(p[i] for p in pts), max(p[i] for p in pts)] for i, a in enumerate('xyz')}
tol = k['step']['tolerance_mm']; exp = k['step']['bounding_box_mm']
check('STEP box', all(abs(box[a][j] - exp[a][j]) <= tol for a in 'xyz' for j in (0, 1)), f'{len(pts)} vertices, box {box}')
print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
PYEOF
echo "exit=$?"
echo "## reproducibility (informative): two drill and CPL exports, raw SHA-256"
sleep 2
$K pcb export drill -o out2/ --format excellon --drill-origin plot --excellon-units mm --excellon-zeros-format decimal --excellon-oval-format route --excellon-separate-th --generate-map --map-format pdf --generate-report --report-path out2/clean-drill-report.rpt clean.kicad_pcb >/dev/null
$K pcb export pos -o out2/clean-cpl.csv --format csv --units mm --use-drill-file-origin --side both --smd-only --exclude-dnp clean.kicad_pcb >/dev/null
$K pcb export step --board-only --drill-origin -o out2/clean.step clean.kicad_pcb >/dev/null
for f in clean-PTH.drl clean-NPTH.drl clean-drill-report.rpt clean-cpl.csv clean.step; do a=$(shasum -a 256 out/$f | cut -c1-16); b=$(shasum -a 256 out2/$f | cut -c1-16); echo "$f run1 $a run2 $b $([ "$a" = "$b" ] && echo identical || echo differs)"; done
echo "## diff of differing text files (time stamps expected)"; for f in clean-PTH.drl clean-drill-report.rpt clean.step; do diff out/$f out2/$f | head -8; done
rm -rf "$W"
