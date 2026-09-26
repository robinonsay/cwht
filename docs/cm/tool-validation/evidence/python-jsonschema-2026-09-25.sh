#!/bin/bash
# venv Python + jsonschema sanity check runner (scratch procedure; transcript kept as evidence).
PY=/Users/robinonsay/rust/cwht/.venv/bin/python
FX=/Users/robinonsay/rust/cwht/tools/tests/fixtures/schema
W=$(mktemp -d "${TMPDIR:-/tmp}/kat-jsonschema.XXXXXX")
echo "# venv Python + jsonschema sanity check, $(date '+%Y-%m-%d %H:%M:%S %Z'), host $(uname -srm)"
echo "# repository HEAD $(git -C /Users/robinonsay/rust/cwht rev-parse HEAD)"
(cd $FX && shasum -a 256 *.json)
echo "\$ cmp tools/tests/fixtures/schema/requirements.schema.json docs/requirements/schema.json"; cmp $FX/requirements.schema.json /Users/robinonsay/rust/cwht/docs/requirements/schema.json && echo "identical (informative: the fixture copy still equals the repository schema)"
echo "\$ $PY --version"; $PY --version
echo "\$ $PY -m pip show jsonschema | head -2"; $PY -m pip show jsonschema 2>/dev/null | head -2
CHECK='import json,sys,importlib.metadata as m,jsonschema as j
k=json.load(open("known-answers.json")); ok=True
print("jsonschema", m.version("jsonschema"))
for case in k["cases"]:
    s=json.load(open(case["schema"])); V=j.validators.validator_for(s); V.check_schema(s); ok=ok and V.__name__==case["validator_class"]
    print("case", case["name"], case["schema"], V.__name__)
    for c in ("valid","invalid"):
        got=sorted(["/".join(map(str,e.absolute_path)),e.validator] for e in V(s).iter_errors(json.load(open(case[c]["file"])))); exp=sorted(case[c]["errors"])
        print(" ", c, case[c]["file"], len(got), "errors", got, "MATCH" if got==exp else "MISMATCH, expected "+str(exp)); ok=ok and got==exp
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)'
echo "## known-answer check (run in the fixture directory)"
echo "\$ cd tools/tests/fixtures/schema && $PY -c '<CHECK>'"; echo "CHECK = $CHECK" | sed 's/^/    /'
(cd $FX && $PY -c "$CHECK"); echo "exit=$?"
echo "## negative control: temporary copy with seeded fault 1 of each case removed (must FAIL)"
cp $FX/* $W/
$PY -c 'import json;d=json.load(open("'$W'/invalid-requirement.json"));d["requirements"][0]["verification_method"]="Test";json.dump(d,open("'$W'/invalid-requirement.json","w"))'
$PY -c 'import json;d=json.load(open("'$W'/keywords-invalid.json"));d["entries"][0]["id"]="K-100";json.dump(d,open("'$W'/keywords-invalid.json","w"))'
(cd $W && $PY -c "$CHECK"); echo "exit=$? (expected 1)"
rm -rf "$W"
