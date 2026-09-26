import sys, uuid
lib = open('/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols/Device.kicad_sym').read()
i = lib.find('(symbol "R"\n'); d = 0
for j in range(i, len(lib)):
    if lib[j] == '(': d += 1
    elif lib[j] == ')':
        d -= 1
        if d == 0: break
sym = lib[i:j+1].replace('(symbol "R"\n', '(symbol "Device:R"\n', 1)
sym = '\n'.join('\t' + l for l in sym.split('\n'))
def u(name):  # deterministic uuids so the fixture is reproducible
    return str(uuid.uuid5(uuid.NAMESPACE_URL, 'cwht-kicad-fixture/' + name))
def sch(project, seeded):
    root = u(project + '/root')
    nc = [f'\t(no_connect\n\t\t(at 101.6 97.79)\n\t\t(uuid "{u(project+"/nc1")}")\n\t)']
    if not seeded:
        nc.append(f'\t(no_connect\n\t\t(at 101.6 105.41)\n\t\t(uuid "{u(project+"/nc2")}")\n\t)')
    def prop(name, val, at, hide=False):
        h = '\n\t\t\t\t(hide yes)' if hide else ''
        return f'\t\t(property "{name}" "{val}"\n\t\t\t(at {at})\n\t\t\t(effects\n\t\t\t\t(font\n\t\t\t\t\t(size 1.27 1.27)\n\t\t\t\t){h}\n\t\t\t)\n\t\t)'
    body = f'''(kicad_sch
\t(version 20250114)
\t(generator "eeschema")
\t(generator_version "9.0")
\t(uuid "{root}")
\t(paper "A4")
\t(lib_symbols
{sym}
\t)
\t(symbol
\t\t(lib_id "Device:R")
\t\t(at 101.6 101.6 0)
\t\t(unit 1)
\t\t(exclude_from_sim no)
\t\t(in_bom yes)
\t\t(on_board yes)
\t\t(dnp no)
\t\t(uuid "{u(project+"/R1")}")
{prop("Reference","R1","104.14 101.6 90")}
{prop("Value","10k","101.6 101.6 90")}
{prop("Footprint","Resistor_SMD:R_0603_1608Metric","99.822 101.6 90",True)}
{prop("Datasheet","~","101.6 101.6 0",True)}
{prop("Description","Resistor","101.6 101.6 0",True)}
\t\t(pin "1"
\t\t\t(uuid "{u(project+"/R1/1")}")
\t\t)
\t\t(pin "2"
\t\t\t(uuid "{u(project+"/R1/2")}")
\t\t)
\t\t(instances
\t\t\t(project "{project}"
\t\t\t\t(path "/{root}"
\t\t\t\t\t(reference "R1")
\t\t\t\t\t(unit 1)
\t\t\t\t)
\t\t\t)
\t\t)
\t)
{chr(10).join(nc)}
\t(sheet_instances
\t\t(path "/"
\t\t\t(page "1")
\t\t)
\t)
\t(embedded_fonts no)
)
'''
    return body
out = sys.argv[1]
open(out + '/clean.kicad_sch', 'w').write(sch('clean', False))
open(out + '/seeded.kicad_sch', 'w').write(sch('seeded', True))
