#!/usr/bin/env python3
"""Convert the NASA SE Handbook (NASA/SP-2016-6105 Rev 2) into per-section Markdown.

Input : docs/references/nasa_se_handbook_sp2016-6105_rev2.pdf (via pdftotext)
Output: docs/references/md/nasa-se-handbook/<nn>-<slug>.md, one file per
        chapter section / appendix, each with a header citing printed pages.
"""
import pathlib, re, subprocess, sys, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
PDF = ROOT / "docs/references/nasa_se_handbook_sp2016-6105_rev2.pdf"
OUT = ROOT / "docs/references/md/nasa-se-handbook"
OUT.mkdir(parents=True, exist_ok=True)

# (file id, heading text as it appears, printed start page)
SECTIONS = [
    ("1.0", "Introduction", 1),
    ("2.0", "Fundamentals of Systems Engineering", 3),
    ("3.0", "NASA Program/Project Life Cycle", 17),
    ("4.0", "System Design Processes", 43),
    ("4.1", "Stakeholder Expectations Definition", 45),
    ("4.2", "Technical Requirements Definition", 54),
    ("4.3", "Logical Decomposition", 62),
    ("4.4", "Design Solution Definition", 65),
    ("5.0", "Product Realization", 77),
    ("5.1", "Product Implementation", 78),
    ("5.2", "Product Integration", 83),
    ("5.3", "Product Verification", 88),
    ("5.4", "Product Validation", 99),
    ("5.5", "Product Transition", 106),
    ("6.0", "Crosscutting Technical Management", 113),
    ("6.1", "Technical Planning", 113),
    ("6.2", "Requirements Management", 130),
    ("6.3", "Interface Management", 135),
    ("6.4", "Technical Risk Management", 138),
    ("6.5", "Configuration Management", 143),
    ("6.6", "Technical Data Management", 151),
    ("6.7", "Technical Assessment", 155),
    ("6.8", "Decision Analysis", 160),
    ("A", "Acronyms", 173),
    ("B", "Glossary", 176),
    ("C", "How to Write a Good Requirement", 197),
    ("D", "Requirements Verification Matrix", 201),
    ("E", "Creating the Validation Plan with a Validation Requirements Matrix", 203),
    ("F", "Functional, Timing, and State Analysis", 205),
    ("G", "Technology Assessment/Insertion", 206),
    ("H", "Integration Plan Outline", 214),
    ("I", "Verification and Validation Plan Outline", 216),
    ("J", "SEMP Content Outline", 223),
    ("K", "Technical Plans", 235),
    ("L", "Interface Requirements Document Outline", 236),
    ("M", "CM Plan Outline", 239),
    ("N", "Guidance on Technical Peer Reviews/Inspections", 240),
    ("O", "Reserved", 241),
    ("P", "SOW Review Checklist", 242),
    ("Q", "Reserved", 243),
    ("R", "HSI Plan Content Outline", 244),
    ("S", "Concept of Operations Annotated Outline", 251),
    ("T", "Systems Engineering in Phase E", 254),
    ("REF", "References Cited", 260),
    ("BIB", "Bibliography", 270),
]

def pdftotext(mode):
    args = ["pdftotext"] + (["-layout"] if mode == "layout" else []) + [str(PDF), "-"]
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout.split("\f")

layout_pages = pdftotext("layout")
flow_pages = pdftotext("flow")
assert len(layout_pages) == len(flow_pages)

# --- map printed page numbers to pdf page indexes using footers -------------
footer_re = re.compile(r"NASA SYSTEMS ENGINEERING HANDBOOK")
num_re = re.compile(r"(?<![\d.])(\d{1,3})(?![\d.])")
printed_to_idx = {}
for idx, page in enumerate(layout_pages):
    lines = [l for l in page.splitlines() if l.strip()]
    for l in lines[-3:]:
        if footer_re.search(l):
            nums = [int(n) for n in num_re.findall(l)]
            if len(nums) == 1:
                printed_to_idx.setdefault(nums[0], idx)
            break
# sanity: offset should be constant for the body
offsets = collections.Counter(idx - p for p, idx in printed_to_idx.items())
offset, votes = offsets.most_common(1)[0]
print(f"footer-derived pages: {len(printed_to_idx)}, dominant offset {offset} ({votes} votes)", file=sys.stderr)
def idx_of(printed):
    return printed_to_idx.get(printed, printed + offset)

# --- verify anchors ----------------------------------------------------------
for sid, title, p in SECTIONS:
    head = f"{sid} {title}" if re.match(r"\d", sid) else f"Appendix {sid}"
    if head.split()[0] in ("REF", "BIB"):
        head = title
    txt = flow_pages[idx_of(p)] + flow_pages[min(idx_of(p) + 1, len(flow_pages) - 1)]
    if title.split()[0] not in txt:
        print(f"WARNING: anchor '{head}' not found near printed page {p}", file=sys.stderr)

# --- build markdown ----------------------------------------------------------
running_headers = set()
for _sid, _title, _p in SECTIONS:
    if re.match(r"\d", _sid):
        running_headers.add(f"{_sid} {_title}")
        if _sid.endswith(".0"):
            running_headers.add(f"{_sid} {_title}")
    elif len(_sid) == 1:
        running_headers.add(f"Appendix {_sid}: {_title}")
        running_headers.add(f"Appendix {_sid}: {_title}\u2014 Checklist")
running_headers |= {"How to Write a Good Requirement\u2014 Checklist", "Appendix C: How to Write a Good Requirement\u2014 Checklist"}
heading_re = re.compile(r"^\s*(\d\.\d(?:\.\d)?(?:\.\d)?)\s+([A-Z][^\n]{2,90})$")
def to_markdown(text):
    out, para = [], []
    def flush():
        if para:
            out.append(" ".join(s.strip() for s in para))
            para.clear()
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush(); out.append(""); continue
        if footer_re.search(line) and len(line) < 80:
            continue
        if line.strip() in running_headers or re.fullmatch(r"\s*\d{1,3}\s*", line):
            continue
        line = re.sub(r"[\uf000-\uf8ff]", "- ", line)  # checkbox / bullet glyphs from symbol fonts
        line = re.sub(r"^(\s*)(- )+", r"\1- ", line)
        if re.match(r"^\s*- \S", line):
            flush(); out.append("- " + line.split("- ", 1)[1].strip()); continue
        m = heading_re.match(line)
        if m and not line.strip().endswith((".", ",", ";")):
            flush()
            depth = m.group(1).count(".") + 1
            out.append("#" * min(depth + 1, 5) + f" {m.group(1)} {m.group(2).strip()}")
            out.append("")
            continue
        if re.match(r"^\s*[•\-•]\s+", line):
            flush(); out.append("- " + re.sub(r"^\s*[•\-•]\s+", "", line)); continue
        para.append(line)
    flush()
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

index_lines = ["# NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2) — Markdown conversion",
               "",
               "Source PDF: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf",
               "Converted with `tools/refs/se_handbook_to_md.py` (pdftotext). Page numbers are the",
               "handbook's printed page numbers; cite as `SE HB §4.2, p. 54`.", "",
               "| File | Section | Printed pages |", "|---|---|---|"]
for n, (sid, title, p) in enumerate(SECTIONS):
    nxt = SECTIONS[n + 1][2] if n + 1 < len(SECTIONS) else 297 - offset
    start, end = idx_of(p), idx_of(nxt)
    if end <= start:
        end = start + 1
    body = "".join(flow_pages[start:end])
    # trim text belonging to the previous section on the first page
    anchor = re.search(re.escape(title.split(",")[0].split("/")[0][:30]), body)
    if anchor and anchor.start() < 3000:
        body = body[anchor.start():]
    label = f"{sid} {title}" if re.match(r"\d", sid) else (f"Appendix {sid}: {title}" if len(sid) == 1 else title)
    fname = f"{n:02d}-{slug(label)}.md"
    header = (f"# {label}\n\n"
              f"> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages {p}–{nxt - 1}. "
              f"Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §{sid}`.\n\n")
    (OUT / fname).write_text(header + to_markdown(body))
    index_lines.append(f"| [{fname}]({fname}) | {label} | {p}–{nxt - 1} |")
(OUT / "README.md").write_text("\n".join(index_lines) + "\n")
print(f"wrote {len(SECTIONS)} sections to {OUT}", file=sys.stderr)
