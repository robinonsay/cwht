#!/bin/bash
# picotool sanity check runner (scratch procedure; transcript kept as evidence). File operations only; no device.
FX=/Users/robinonsay/rust/cwht/tools/tests/fixtures/picotool
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-picotool.XXXXXX")
run() { echo "\$ $*"; "$@" > "$W/out.txt" 2>&1; rc=$?; cat "$W/out.txt"; echo "exit=$rc"; LASTRC=$rc; }
echo "# picotool sanity check, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm)"
echo "# repository HEAD $(git -C /Users/robinonsay/rust/cwht rev-parse HEAD)"
(cd $FX && shasum -a 256 kat-target.elf known-answers.json)
cp $FX/kat-target.elf $FX/known-answers.json $W/; cd $W
run which picotool
run picotool version; V=$(picotool version)
run picotool uf2 convert kat-target.elf kat-target.uf2 --family rp2350-arm-s; U=$LASTRC
run shasum -a 256 kat-target.uf2
run picotool info -a kat-target.elf; I1=$LASTRC; cp out.txt info-elf.txt
run picotool info -a kat-target.uf2; I2=$LASTRC; cp out.txt info-uf2.txt
echo "## comparison against known-answers.json"
$PY - "$W" "$V" "$U $I1 $I2" <<'PYEOF'
import json, struct, hashlib, sys, pathlib
w = pathlib.Path(sys.argv[1]); ver = sys.argv[2]; u, i1, i2 = map(int, sys.argv[3].split())
k = json.loads((w / 'known-answers.json').read_text()); ok = True
def check(name, cond, detail):
    global ok
    ok = ok and cond; print(('PASS ' if cond else 'FAIL ') + name + ': ' + detail)
elf = (w / 'kat-target.elf').read_bytes()
check('version', ver == k['picotool_version'], ver)
check('fixture ELF', hashlib.sha256(elf).hexdigest() == k['elf']['sha256'], hashlib.sha256(elf).hexdigest())
# independent UF2 reconstruction from the ELF program headers
phoff, = struct.unpack_from('<I', elf, 0x1C); phentsize, phnum = struct.unpack_from('<HH', elf, 0x2A); pages = {}
for i in range(phnum):
    p_type, p_offset, p_vaddr, p_paddr, p_filesz, *_ = struct.unpack_from('<8I', elf, phoff + i * phentsize)
    if p_type != 1 or p_filesz == 0: continue
    for n, b in enumerate(elf[p_offset:p_offset + p_filesz]):
        a = p_paddr + n; pages.setdefault(a & ~0xFF, bytearray(256))[a & 0xFF] = b
recon = b''.join(struct.pack('<8I', 0x0A324655, 0x9E5D5157, 0x00002000, pg, 256, no, len(pages), 0xE48BFF59) + bytes(pages[pg]) + bytes(220) + struct.pack('<I', 0x0AB16F30) for no, pg in enumerate(sorted(pages)))
uf2 = (w / 'kat-target.uf2').read_bytes(); c = k['uf2_convert']
print('reconstruction sha256', hashlib.sha256(recon).hexdigest(), 'pages', [hex(p) for p in sorted(pages)])
check('uf2 convert', u == c['exit'] and len(uf2) == c['size_bytes'] and hashlib.sha256(uf2).hexdigest() == c['sha256'] and uf2 == recon, f'exit {u}, {len(uf2)} B, sha256 {hashlib.sha256(uf2).hexdigest()}, equals stored and reconstruction: {hashlib.sha256(uf2).hexdigest() == c["sha256"]} / {uf2 == recon}')
for name, rc, f in (('info ELF', i1, 'info-elf.txt'), ('info UF2', i2, 'info-uf2.txt')):
    txt = (w / f).read_text(); miss = [s for s in k['info']['must_contain'] if s not in txt.splitlines()]
    check(name, rc == 0 and not miss, f'exit {rc}, missing {miss}')
print('NOT RUN verify:', k['verify']['status'])
print('RESULT', 'PASS (convert, info); verify blocked' if ok else 'FAIL'); sys.exit(0 if ok else 1)
PYEOF
echo "exit=$?"
cd /; rm -rf "$W"
