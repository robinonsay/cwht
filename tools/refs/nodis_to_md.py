#!/usr/bin/env python3
"""Fetch a NASA directive from NODIS and write per-page Markdown.

usage: nodis_to_md.py <Internal_ID> <out-subdir> <cite-label> <page> [<page> ...]
e.g.   nodis_to_md.py N_PR_7123_001E_ npr-7123-1e "NPR 7123.1E" Preface Chapter1 ... AppendixK
"""
import pathlib, re, sys, requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = pathlib.Path(__file__).resolve().parents[2]
internal_id, subdir, label, *pages = sys.argv[1:]
OUT = ROOT / "docs/references/md" / subdir
OUT.mkdir(parents=True, exist_ok=True)
BASE = f"https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID={internal_id}&page_name="
UA = {"User-Agent": "Mozilla/5.0 (cwht reference corpus builder)"}
index = [f"# {label} — Markdown conversion", "", f"Source: {BASE}Preface",
         "Converted with `tools/refs/nodis_to_md.py`. Machine conversion; tables may be flattened.", "",
         "| File | Page |", "|---|---|"]
for n, name in enumerate(pages):
    r = requests.get(BASE + name, headers=UA, timeout=60); r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    for t in soup(["script", "style", "nav", "header", "footer", "form"]):
        t.decompose()
    text = md(str(soup.body or soup), heading_style="ATX", strip=["img"])
    text = re.sub(r"\n{3,}", "\n\n", text)
    m = re.search(r"(?m)^#+ .*(Preface|Chapter\s*\d|Appendix\s*[A-Z]|Change Log).*$", text)
    if m and m.start() < 8000:
        text = text[m.start():]
    fname = f"{n:02d}-{name.lower()}.md"
    header = f"# {label} — {name}\n\n> Source: {BASE}{name}\n> Machine conversion; tables may be flattened.\n\n"
    (OUT / fname).write_text(header + text.strip() + "\n")
    index.append(f"| [{fname}]({fname}) | {name} |")
    print(f"{name}: {len(text)} chars", file=sys.stderr)
(OUT / "README.md").write_text("\n".join(index) + "\n")
