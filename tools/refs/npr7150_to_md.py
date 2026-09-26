#!/usr/bin/env python3
"""Fetch NPR 7150.2D (NASA Software Engineering Requirements) from NODIS and write
per-chapter Markdown under docs/references/md/npr-7150-2d/."""
import pathlib, re, sys, requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/references/md/npr-7150-2d"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name="
PAGES = ["Preface", "Chapter1", "Chapter2", "Chapter3", "Chapter4", "Chapter5", "Chapter6",
         "AppendixA", "AppendixB", "AppendixC", "AppendixD", "AppendixE"]
UA = {"User-Agent": "Mozilla/5.0 (cwht reference corpus builder)"}

index = ["# NPR 7150.2D — NASA Software Engineering Requirements (Markdown conversion)", "",
         "Source: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D",
         "Converted with `tools/refs/npr7150_to_md.py`. Cite as `NPR 7150.2D §3.1.3` or by `SWE-NNN` number.", "",
         "| File | Page |", "|---|---|"]
for n, name in enumerate(PAGES):
    r = requests.get(BASE + name, headers=UA, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    for t in soup(["script", "style", "nav", "header", "footer", "form"]):
        t.decompose()
    # NODIS wraps the document body in the largest content block; take body and let
    # markdownify flatten it, then trim site chrome heuristically.
    body = soup.body or soup
    text = md(str(body), heading_style="ATX", strip=["img"])
    text = re.sub(r"\n{3,}", "\n\n", text)
    # trim chrome: keep from the first occurrence of the document title / page heading
    m = re.search(r"(?m)^#+ .*(Preface|Chapter\s*\d|Appendix\s*[A-E]).*$", text)
    if m and m.start() < 8000:
        text = text[m.start():]
    tail = re.search(r"(?m)^.*(This document does not bind the public|Print Page|DISTRIBUTION:).*$", text)
    if tail and tail.start() > len(text) * 0.5:
        text = text[:tail.start()]
    title = soup.title.get_text(strip=True) if soup.title else name
    fname = f"{n:02d}-{name.lower()}.md"
    header = (f"# NPR 7150.2D — {name}\n\n> Source: {BASE}{name}\n> Page title: {title}\n> "
              f"Machine conversion; tables may be flattened. SWE-NNN identifiers are authoritative.\n\n")
    (OUT / fname).write_text(header + text.strip() + "\n")
    index.append(f"| [{fname}]({fname}) | {name} |")
    print(f"{name}: {len(text)} chars", file=sys.stderr)
(OUT / "README.md").write_text("\n".join(index) + "\n")
