#!/bin/bash
# rustc / cargo / clippy sanity check runner (scratch procedure; transcript kept as evidence).
FX=/Users/robinonsay/rust/cwht/tools/tests/fixtures/rust
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
A=$(mktemp -d "${TMPDIR:-/tmp}/kat-rust-a.XXXXXX"); B=$(mktemp -d "${TMPDIR:-/tmp}/kat-rust-b.XXXXXX")
run() { echo "\$ $*"; "$@" > "$A/out.txt" 2>&1; rc=$?; grep -v '^\s*$' "$A/out.txt" | tail -${TAILN:-12}; echo "exit=$rc"; LASTRC=$rc; }
echo "# rustc/cargo/clippy sanity check, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm)"
echo "# repository HEAD $(git -C /Users/robinonsay/rust/cwht rev-parse HEAD)"
(cd $FX && find . -type f -not -name '*.DS_Store' | LC_ALL=C sort | xargs shasum -a 256)
cp -R $FX/. $A/; cp -R $FX/. $B/
run rustc +stable --version; RV=$(rustc +stable --version)
run cargo +stable --version; CV=$(cargo +stable --version)
run cargo +stable clippy --version; KV=$(cargo +stable clippy --version)
run rustup show active-toolchain
cd $A/kat-target
export CARGO_TARGET_DIR=$A/kat-target/target
run cargo +stable build --release --locked; E1=$LASTRC; H1=$(shasum -a 256 target/thumbv8m.main-none-eabihf/release/kat-target | cut -d' ' -f1); echo "build 1 ELF sha256 $H1"
cp target/thumbv8m.main-none-eabihf/release/kat-target $A/kat-target.elf
run cargo +stable clean
run cargo +stable build --release --locked; E2=$LASTRC; H2=$(shasum -a 256 target/thumbv8m.main-none-eabihf/release/kat-target | cut -d' ' -f1); echo "build 2 ELF sha256 $H2"
cd $B/kat-target; export CARGO_TARGET_DIR=$B/kat-target/target
run cargo +stable build --release --locked; E3=$LASTRC; H3=$(shasum -a 256 target/thumbv8m.main-none-eabihf/release/kat-target | cut -d' ' -f1); echo "build 3 (second directory) ELF sha256 $H3"
cd $A/kat-host; export CARGO_TARGET_DIR=$A/kat-host/target
run cargo +stable test --locked; T0=$LASTRC; cp $A/out.txt $A/test-clean.txt
TAILN=20 run cargo +stable test --locked --features seeded-fail; T1=$LASTRC; cp $A/out.txt $A/test-seeded.txt
run cargo +stable clippy --locked --all-targets -- -D warnings; C0=$LASTRC; cp $A/out.txt $A/clippy-clean.txt
TAILN=14 run cargo +stable clippy --locked --all-targets --features seeded-lint -- -D warnings; C1=$LASTRC; cp $A/out.txt $A/clippy-lint.txt
TAILN=14 run cargo +stable clippy --locked --all-targets --features seeded-unwrap -- -D warnings; C2=$LASTRC; cp $A/out.txt $A/clippy-unwrap.txt
echo "## comparison against known-answers.json"
$PY - "$A" "$RV" "$CV" "$KV" "$E1 $E2 $E3" "$H1 $H2 $H3" "$T0 $T1 $C0 $C1 $C2" <<'PYEOF'
import json, struct, sys, pathlib, re
a = pathlib.Path(sys.argv[1]); rv, cv, kv = sys.argv[2:5]; builds = list(map(int, sys.argv[5].split())); hashes = sys.argv[6].split()
t0, t1, c0, c1, c2 = map(int, sys.argv[7].split())
k = json.loads((a / 'known-answers.json').read_text()); ok = True
def check(name, cond, detail):
    global ok
    ok = ok and cond; print(('PASS ' if cond else 'FAIL ') + name + ': ' + detail)
tc = k['toolchain']
check('versions', rv == tc['rustc_version'] and cv == tc['cargo_version'] and kv == tc['clippy_version'], f'{rv} | {cv} | {kv}')
elf = (a / 'kat-target.elf').read_bytes()
cls, data = elf[4], elf[5]; mach, = struct.unpack_from('<H', elf, 0x12); entry, = struct.unpack_from('<I', elf, 0x18)
shoff, = struct.unpack_from('<I', elf, 0x20); shentsize, shnum, shstrndx = struct.unpack_from('<HHH', elf, 0x2E)
secs = [struct.unpack_from('<10I', elf, shoff + i * shentsize) for i in range(shnum)]
def strtab(off, idx):
    end = elf.index(b'\0', off + idx); return elf[off + idx:end].decode()
symtab = [s for s in secs if s[1] == 2][0]; strsec = secs[symtab[6]]
reset = None
for i in range(symtab[5] // 16):
    st_name, st_value, st_size, st_info, st_other, st_shndx = struct.unpack_from('<IIIBBH', elf, symtab[4] + 16 * i)
    if strtab(strsec[4], st_name) == 'reset': reset = st_value
check('ELF class', elf[:4] == b'\x7fELF' and cls == 1 and data == 1 and mach == 40 and reset is not None and entry == reset | 1, f'class {cls} data {data} e_machine {mach} e_entry {entry:#x} reset {reset:#x}' if reset is not None else 'reset symbol missing')
check('builds exit 0', builds == [0, 0, 0], str(builds))
check('reproducible', len(set(hashes)) == 1, ' '.join(h[:16] for h in hashes))
stored = k['target_build']['elf_sha256']
check('stored ELF hash', stored is None or stored == hashes[0], f'stored {stored}, built {hashes[0]}' + (' (no stored value yet: record it)' if stored is None else ''))
h = k['host_tests']
tc_ = (a / 'test-clean.txt').read_text(); ts = (a / 'test-seeded.txt').read_text()
check('cargo test clean', t0 == h['clean']['exit'] and h['clean']['summary'] in tc_, f'exit {t0}')
check('cargo test seeded', t1 == h['seeded_fail']['exit'] and h['seeded_fail']['summary'] in ts and re.search(r'^    ' + re.escape(h['seeded_fail']['failed_test']) + r'$', ts, re.M) is not None, f'exit {t1}')
c = k['clippy']
check('clippy clean', c0 == c['clean']['exit'], f'exit {c0}')
for key, rc, f in (('seeded_lint', c1, 'clippy-lint.txt'), ('seeded_unwrap', c2, 'clippy-unwrap.txt')):
    txt = (a / f).read_text(); lint = c[key]['lint'].split('::')[1]
    names = sorted(set(re.findall(r'#([a-z_]+)\b', txt)) | set(n.replace('-', '_') for n in re.findall(r'clippy::([a-z_-]+)', txt)))
    check(f'clippy {key}', rc == c[key]['exit'] and names == [lint], f'exit {rc}, lints {names}')
print('RESULT', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
PYEOF
echo "exit=$?"
cd /; rm -rf "$A" "$B"
