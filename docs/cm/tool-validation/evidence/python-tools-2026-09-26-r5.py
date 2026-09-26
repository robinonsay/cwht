"""Known-answer runs of the project Python tools, SRR package item R5 (section 3 of TV-002 to TV-010 re-run at HEAD)
and the 2026-09-26 tool changes (TV-003 and TV-010 re-validation; TV-011 to TV-013 first validation).

Usage: <venv python> python-tools-2026-09-26-r5.py ROOT MODE
  ROOT  the tree to test: an export of HEAD (`git archive HEAD | tar -x`) for MODE head, the repository for MODE worktree
  MODE  head      the run commands of section 3 of TV-002 to TV-010 exactly as those records state them
        worktree  the same, with the classes added on 2026-09-26 (TV-003 RecordDriftTests; TV-010 LabelAndDaggerTests and
                  LayoutKnownAnswerTests) and the new records TV-011 (unsafe_audit.py), TV-012 (complexity_gate.py) and
                  TV-013 (measurements.py)
Identity lines give, for every tool, test module and fixture file, the git blob of the tested file and whether it
equals the blob of the same path in the repository HEAD. A skipped test is a failure. A record of what was run, not a
controlled tool (docs/cm/tool-validation/README.md, Evidence).
"""
import datetime, hashlib, os, re, subprocess, sys
from pathlib import Path

REPO = Path('/Users/robinonsay/rust/cwht'); PY = str(REPO / '.venv/bin/python')
ROOT = Path(sys.argv[1]).resolve(); MODE = sys.argv[2]
assert MODE in ('head', 'worktree'), MODE


def git(*a, cwd=REPO):
    return subprocess.run(['git', *a], cwd=cwd, capture_output=True, text=True)


HEAD = git('rev-parse', 'HEAD').stdout.strip()


def ident(path):
    p = ROOT / path
    blob = git('hash-object', str(p)).stdout.strip()
    head = git('rev-parse', f'HEAD:{path}').stdout.strip() if git('cat-file', '-e', f'HEAD:{path}').returncode == 0 else None
    state = 'not in HEAD' if head is None else ('equal to HEAD' if head == blob else f'differs from HEAD blob {head[:8]}')
    return f'{path}: git blob {blob}; sha256 {hashlib.sha256(p.read_bytes()).hexdigest()}; {state}'


def tree(path):
    files = sorted(f for f in (ROOT / path).rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.name != '.DS_Store')
    lines = ''.join(f'{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.relative_to(ROOT)}\n' for f in files)
    differ = []
    for f in files:
        rel = str(f.relative_to(ROOT))
        head = git('rev-parse', f'HEAD:{rel}')
        if head.returncode != 0 or head.stdout.strip() != git('hash-object', str(f)).stdout.strip():
            differ.append(rel)
    return (f'{path}: {len(files)} files, tree digest sha256 {hashlib.sha256(lines.encode()).hexdigest()}; '
            f'{len(files) - len(differ)} equal to HEAD, {len(differ)} not ({", ".join(differ[:6])}{", ..." if len(differ) > 6 else ""})')


W = MODE == 'worktree'
RUNS = [
  ('TV-002 traceability.py', ['tools/traceability.py', 'tools/validate_docs.py'], ['tools/tests/fixtures/valid_project', 'tools/tests/fixtures/invalid_project'], [
     ('test_traceability.py', ['ValidProjectTests', 'InvalidProjectTests', 'WordListTests']),
     ('test_traceability_srr_rules.py', ['CatalogueTests', 'StakeholdersKnownAnswerTests', 'AllocationKnownAnswerTests']),
     ('test_tools.py', [])]),
  ('TV-003 validate_docs.py', ['tools/validate_docs.py'], ['tools/tests/fixtures/valid_project', 'tools/tests/fixtures/invalid_project'], [
     ('test_validate_docs.py', ['ValidProjectTests', 'InvalidProjectTests', 'PeerReviewRecordTests', 'UsageErrorTests'] + (['RecordDriftTests'] if W else [])),
     ('test_tools.py', [])]),
  ('TV-004 render_rmm.py', ['tools/render_rmm.py'], ['tools/tests/fixtures/rmm'], [('test_render_rmm.py', [])]),
  ('TV-005 render_compliance.py', ['tools/render_compliance.py'], ['tools/tests/fixtures/compliance'], [('test_render_compliance.py', ['CorpusParseTests', 'ValidFixtureTests', 'SeededFaultTests'])]),
  ('TV-006 render_risk.py', ['tools/render_risk.py'], ['tools/tests/fixtures/risk'], [('test_render_risk.py', [])]),
  ('TV-007 review_trend.py', ['tools/review_trend.py'], ['tools/tests/fixtures/review_trend'], [('test_review_trend.py', [])]),
  ('TV-008 render_deck.py + Chromium headless shell', ['tools/slides/render_deck.py', 'tools/slides/package.json', 'tools/slides/package-lock.json'], ['tools/tests/fixtures/slides'], [('test_render_deck.py', [])]),
  ('TV-009 git', [], ['tools/tests/fixtures/git'], [('test_git_known_answer.py', [])]),
  ('TV-010 render_review_figures.py', ['tools/render_review_figures.py'], ['tools/tests/fixtures/review_figures'], [
     ('test_render_review_figures.py', ['ParserTests', 'DataKnownAnswerTests', 'RunTests'] + (['LabelAndDaggerTests', 'LayoutKnownAnswerTests'] if W else []))]),
]
if W:
    RUNS += [
      ('TV-011 unsafe_audit.py', ['tools/unsafe_audit.py'], ['tools/tests/fixtures/unsafe_audit'], [('test_unsafe_audit.py', [])]),
      ('TV-012 complexity_gate.py', ['tools/complexity_gate.py', 'tools/unsafe_audit.py'], ['tools/tests/fixtures/complexity_gate'], [('test_complexity_gate.py', [])]),
      ('TV-013 measurements.py', ['tools/measurements.py'], ['tools/tests/fixtures/measurements'], [('test_measurements.py', [])]),
    ]
RUNS += [
  ('Repository-content checks (not a tool accreditation)', [], [], [
     ('test_traceability.py', ['RepositoryTests']), ('test_validate_docs.py', ['RepositoryTests']),
     ('test_traceability_srr_rules.py', ['FixtureSchemaTripwireTests', 'RepositoryAllocationTests']),
     ('test_render_compliance.py', ['ProjectMatrixTests']), ('test_render_review_figures.py', ['RepositoryTests'])]),
]


def run_module(mod, classes):
    cmd = [PY, '-m', 'unittest', 'discover', '-v', '-s', 'tools/tests', '-p', mod] + [x for c in classes for x in ('-k', c)]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=1800)
    out = r.stdout + r.stderr
    m = re.search(r'^Ran (\d+) tests? in ([0-9.]+)s', out, re.M); n = int(m.group(1)) if m else 0
    skipped = len(re.findall(r'\.\.\. skipped', out)); failed = len(re.findall(r'\.\.\. (FAIL|ERROR)$', out, re.M))
    per_class = {}
    for cls in re.findall(r'^\S+ \(\S*?\.?(\w+)\.\w+\) \.\.\. ', out, re.M):
        per_class[cls] = per_class.get(cls, 0) + 1
    ok = r.returncode == 0 and skipped == 0 and failed == 0 and n > 0
    shown = ' '.join(("'" + c + "'") if ' ' in c else c for c in cmd[1:])
    return ok, n, skipped, failed, per_class, f'.venv/bin/python {shown}', out


print(f'# Project Python tool known-answer runs (R5, mode {MODE}), {datetime.datetime.now().astimezone():%Y-%m-%d %H:%M:%S %Z}, host {os.uname().sysname} {os.uname().release} {os.uname().machine}')
print(f'# tree tested {ROOT}; repository HEAD {HEAD}; python {subprocess.run([PY, "--version"], capture_output=True, text=True).stdout.strip()}; {git("--version").stdout.strip()}')
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
        if not ok: print('    ' + out[-2500:].replace('\n', '\n    '))
    print(f'  RESULT {title}: {"PASS" if t_ok else "FAIL"} ({total} tests)')
    if not title.startswith('Repository'):
        all_ok = all_ok and t_ok
print('\n## Full directory, for information')
r = subprocess.run([PY, '-m', 'unittest', 'discover', '-s', 'tools/tests'], cwd=ROOT, capture_output=True, text=True, timeout=3600)
tail = (r.stdout + r.stderr).strip().splitlines()[-3:]
print('  $ .venv/bin/python -m unittest discover -s tools/tests'); print('    ' + ' | '.join(tail) + f'; exit {r.returncode}')
print('\nOVERALL (tool runs; repository-content checks reported separately)', 'PASS' if all_ok else 'FAIL'); sys.exit(0 if all_ok else 1)
