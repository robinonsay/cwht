import sys, pcbnew
FP = '/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints'
mm = pcbnew.FromMM
def fp(board, lib, name, ref, x, y, value):
    f = pcbnew.FootprintLoad(f'{FP}/{lib}.pretty', name)
    f.SetFPID(pcbnew.LIB_ID(lib, name))
    f.SetReference(ref); f.SetValue(value)
    f.SetPosition(pcbnew.VECTOR2I(mm(x), mm(y)))
    board.Add(f)
    return f
def build(path, y_route):
    b = pcbnew.BOARD()
    b.GetDesignSettings().SetAuxOrigin(pcbnew.VECTOR2I(mm(100), mm(120)))
    sig = pcbnew.NETINFO_ITEM(b, 'SIG'); b.Add(sig)
    oth = pcbnew.NETINFO_ITEM(b, 'OTH'); b.Add(oth)
    # outline 30 x 20 mm
    pts = [(100,100),(130,100),(130,120),(100,120),(100,100)]
    for (x0,y0),(x1,y1) in zip(pts, pts[1:]):
        s = pcbnew.PCB_SHAPE(b); s.SetShape(pcbnew.SHAPE_T_SEGMENT)
        s.SetStart(pcbnew.VECTOR2I(mm(x0),mm(y0))); s.SetEnd(pcbnew.VECTOR2I(mm(x1),mm(y1)))
        s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(mm(0.05)); b.Add(s)
    r1 = fp(b, 'Resistor_SMD', 'R_0603_1608Metric', 'R1', 110, 110, '10k')
    tp = fp(b, 'TestPoint', 'TestPoint_THTPad_D1.5mm_Drill0.7mm', 'TP1', 120, 110, 'TestPoint')
    fp(b, 'MountingHole', 'MountingHole_3.2mm_M3', 'H1', 125, 115, 'MountingHole')
    for p in r1.Pads():
        p.SetNet(sig if p.GetNumber() == '1' else oth)
    for p in tp.Pads():
        p.SetNet(sig)
    route = [(109.175,110),(109.175,y_route),(120,y_route),(120,110)]
    for (x0,y0),(x1,y1) in zip(route, route[1:]):
        t = pcbnew.PCB_TRACK(b); t.SetStart(pcbnew.VECTOR2I(mm(x0),mm(y0))); t.SetEnd(pcbnew.VECTOR2I(mm(x1),mm(y1)))
        t.SetWidth(mm(0.25)); t.SetLayer(pcbnew.F_Cu); t.SetNet(sig); b.Add(t)
    pcbnew.SaveBoard(path, b)
out = sys.argv[1]
build(out + '/clean.kicad_pcb', 108.0)
build(out + '/seeded.kicad_pcb', 109.3)
