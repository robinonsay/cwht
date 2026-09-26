"""Known-answer runs of the project Python tools for TV-002 to TV-010 (procedure revision 2026-09-26: TV-003 adds UsageErrorTests and TV-008 its SeededFailures class, INSP-015 finding-5; transcript kept as evidence).
Runs from the repository root with the venv Python; records the identity (git blob, SHA-256, tracked state) of every
tool, test module and fixture tree; runs the fixture-only classes of each tool as tools/toolchain.lock.md section 1.1
names them, then the repository-content classes separately, then the full directory. A skipped test is a failure."""
import datetime, hashlib, os, re, subprocess, sys
from pathlib import Path
ROOT = Path('/Users/robinonsay/rust/cwht'); PY = str(ROOT / '.venv/bin/python')
def sh(*a, **k): return subprocess.run(a, cwd=ROOT, capture_output=True, text=True, **k)
def ident(path):
    p = ROOT / path
    blob = sh('git', 'hash-object', path).stdout.strip(); sha = hashlib.sha256(p.read_bytes()).hexdigest()
    tracked = sh('git', 'ls-files', '--error-unmatch', path).returncode == 0
    state = ('unchanged from HEAD' if sh('git', 'diff', '--quiet', 'HEAD', '--', path).returncode == 0 else 'modified in the working tree') if tracked else 'untracked'
    return f'{path}: git blob {blob}; sha256 {sha}; {state}'
def tree(path):
    files = sorted(f for f in (ROOT / path).rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.name != '.DS_Store')
    lines = ''.join(f'{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.relative_to(ROOT)}\n' for f in files)
    untracked = sum(1 for f in files if sh('git', 'ls-files', '--error-unmatch', str(f.relative_to(ROOT))).returncode != 0)
    return f'{path}: {len(files)} files, tree digest sha256 {hashlib.sha256(lines.encode()).hexdigest()} (SHA-256 of the sorted "sha256  path" list); untracked files {untracked}'
RUNS = [
  ('TV-002 traceability.py', ['tools/traceability.py', 'tools/validate_docs.py'], ['tools/tests/fixtures/valid_project', 'tools/tests/fixtures/invalid_project'], [
     ('test_traceability.py', ['ValidProjectTests', 'InvalidProjectTests', 'WordListTests']),
     ('test_traceability_srr_rules.py', ['CatalogueTests', 'StakeholdersKnownAnswerTests', 'AllocationKnownAnswerTests']),
     ('test_tools.py', [])]),
  ('TV-003 validate_docs.py', ['tools/validate_docs.py'], ['tools/tests/fixtures/valid_project', 'tools/tests/fixtures/invalid_project'], [
     ('test_validate_docs.py', ['ValidProjectTests', 'InvalidProjectTests', 'PeerReviewRecordTests', 'UsageErrorTests']),
     ('test_tools.py', [])]),
  ('TV-004 render_rmm.py', ['tools/render_rmm.py'], ['tools/tests/fixtures/rmm'], [('test_render_rmm.py', [])]),
  ('TV-005 render_compliance.py', ['tools/render_compliance.py'], ['tools/tests/fixtures/compliance'], [('test_render_compliance.py', ['CorpusParseTests', 'ValidFixtureTests', 'SeededFaultTests'])]),
  ('TV-006 render_risk.py', ['tools/render_risk.py'], ['tools/tests/fixtures/risk'], [('test_render_risk.py', [])]),
  ('TV-007 review_trend.py', ['tools/review_trend.py'], ['tools/tests/fixtures/review_trend'], [('test_review_trend.py', [])]),
  ('TV-008 render_deck.py + Chromium headless shell', ['tools/slides/render_deck.py', 'tools/slides/package.json', 'tools/slides/package-lock.json'], ['tools/tests/fixtures/slides'], [('test_render_deck.py', [])]),
  ('TV-009 git', [], ['tools/tests/fixtures/git'], [('test_git_known_answer.py', [])]),
  ('TV-010 render_review_figures.py', ['tools/render_review_figures.py'], ['tools/tests/fixtures/review_figures'], [('test_render_review_figures.py', ['ParserTests', 'DataKnownAnswerTests', 'RunTests'])]),
  ('Repository-content checks (not a tool accreditation)', [], [], [
     ('test_traceability.py', ['RepositoryTests']), ('test_validate_docs.py', ['RepositoryTests']),
     ('test_traceability_srr_rules.py', ['FixtureSchemaTripwireTests', 'RepositoryAllocationTests']),
     ('test_render_compliance.py', ['ProjectMatrixTests']), ('test_render_review_figures.py', ['RepositoryTests'])]),
]
def run_module(mod, classes):
    cmd = [PY, '-m', 'unittest', 'discover', '-v', '-s', 'tools/tests', '-p', mod] + [x for c in classes for x in ('-k', c)]
    r = sh(*cmd, timeout=1800)
    out = r.stdout + r.stderr
    m = re.search(r'^Ran (\d+) tests? in ([0-9.]+)s', out, re.M); n = int(m.group(1)) if m else 0
    skipped = len(re.findall(r'\.\.\. skipped', out)); failed = len(re.findall(r'\.\.\. (FAIL|ERROR)$', out, re.M))
    per_class = {}
    for cls in re.findall(r'^\S+ \(\S*?\.?(\w+)\.\w+\) \.\.\. ', out, re.M) or re.findall(r'^test\w* \((?:[\w]+\.)?(\w+)\.test\w*\)', out, re.M):
        per_class[cls] = per_class.get(cls, 0) + 1
    ok = r.returncode == 0 and skipped == 0 and failed == 0 and n > 0
    shown = ' '.join(("'" + c + "'") if ' ' in c else c for c in cmd[1:]).replace(PY, '.venv/bin/python')
    return ok, n, skipped, failed, per_class, f'.venv/bin/python {shown}', out
print(f'# Project Python tool known-answer runs, {datetime.datetime.now().astimezone():%Y-%m-%d %H:%M:%S %Z}, host {os.uname().sysname} {os.uname().release} {os.uname().machine}')
print(f'# repository HEAD {sh("git", "rev-parse", "HEAD").stdout.strip()}; python {sh(PY, "--version").stdout.strip()}; git {sh("git", "--version").stdout.strip()} at {sh("which", "git").stdout.strip()}')
all_ok = True
for title, tools, fixtures, mods in RUNS:
    print(f'\n## {title}')
    for t in tools: print('  tool    ' + ident(t))
    for m, _ in mods: print('  test    ' + ident('tools/tests/' + m))
    for f in fixtures: print('  fixture ' + tree(f))
    total = 0; t_ok = True
    for mod, classes in mods:
        ok, n, skipped, failed, per_class, cmd, out = run_module(mod, classes)
        total += n; t_ok = t_ok and ok
        print(f'  $ {cmd}')
        print(f'    Ran {n} tests; failures+errors {failed}; skipped {skipped}; per class {per_class}; {"PASS" if ok else "FAIL"}')
        if not ok: print('    ' + out[-3000:].replace('\n', '\n    '))
    print(f'  RESULT {title}: {"PASS" if t_ok else "FAIL"} ({total} tests)')
    all_ok = all_ok and t_ok
print('\n## Full directory, for information')
r = sh(PY, '-m', 'unittest', 'discover', '-s', 'tools/tests', timeout=3600)
tail = (r.stdout + r.stderr).strip().splitlines()[-3:]
print('  $ .venv/bin/python -m unittest discover -s tools/tests'); print('    ' + ' | '.join(tail) + f'; exit {r.returncode}')
print('\nOVERALL', 'PASS' if all_ok else 'FAIL'); sys.exit(0 if all_ok else 1)
