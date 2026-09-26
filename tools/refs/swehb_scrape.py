#!/usr/bin/env python3
"""Paced scraper for the NASA Software Engineering Handbook (NASA-HDBK-2203, SWEHB Ver D).

The Confluence REST API on swehb.nasa.gov throttles aggressively (HTTP 429), so this
walks ordinary page views instead: it reads the "C. Project Software Requirements" book
page, collects every child page link, then fetches each page and converts its main
content to Markdown under docs/references/md/swehb/. One request every PACE seconds,
exponential backoff on 429/403. Re-runnable: pages already on disk are skipped.
"""
import pathlib, re, sys, time, requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/references/md/swehb"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "https://swehb.nasa.gov"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"}
PACE = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
BOOKS = ["/display/SWEHBVD/C.+Project+Software+Requirements",
         "/display/SWEHBVD/B.+Institutional+Requirements",
         "/display/SWEHBVD/D.+Topics"]

def get(url):
    delay = PACE
    for attempt in range(10):
        time.sleep(delay)
        r = requests.get(url, headers=UA, timeout=60, allow_redirects=True)
        if r.status_code in (429, 403):
            delay = min(delay * 2, 300)
            print(f"{r.status_code} on {url}, backing off {delay}s", file=sys.stderr)
            continue
        r.raise_for_status()
        return r
    raise RuntimeError(f"gave up on {url}")

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:90]

link_re = re.compile(r'href="(/spaces/SWEHBVD/pages/(\d+)/([^"]+))"')
pages = {}
for book in BOOKS:
    try:
        html = get(BASE + book).text
    except Exception as e:
        print(f"book {book}: {e}", file=sys.stderr); continue
    for href, pid, title in link_re.findall(html):
        title = requests.utils.unquote(title.replace("+", " "))
        pages.setdefault(pid, {"id": pid, "title": title, "href": href})
    print(f"{book}: {len(pages)} pages known so far", file=sys.stderr)

want = sorted(pages.values(), key=lambda p: p["title"])
print(f"fetching {len(want)} pages", file=sys.stderr)
index = ["# NASA Software Engineering Handbook (NASA-HDBK-2203, SWEHB Ver D) — Markdown conversion", "",
         f"Source: {BASE}/display/SWEHBVD . Converted with `tools/refs/swehb_scrape.py` (page views, paced).",
         "Each SWE-NNN page carries tabs: Requirement, Rationale, Guidance, Small Projects, Resources, Lessons Learned, Software Assurance.",
         "", "| File | Title |", "|---|---|"]
for p in want:
    fname = f"{slug(p['title'])}.md"
    path = OUT / fname
    index.append(f"| [{fname}]({fname}) | {p['title']} |")
    if path.exists():
        continue
    try:
        html = get(BASE + p["href"]).text
    except Exception as e:
        print(f"skip {p['title']}: {e}", file=sys.stderr); continue
    soup = BeautifulSoup(html, "lxml")
    main = soup.find(id="main-content") or soup.find("div", class_="wiki-content") or soup.body
    for t in main(["script", "style", "nav"]):
        t.decompose()
    text = md(str(main), heading_style="ATX", strip=["img"])
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    header = (f"# {p['title']}\n\n> NASA Software Engineering Handbook (SWEHB Ver D), page id {p['id']}. "
              f"Source: {BASE}{p['href']}\n\n")
    path.write_text(header + text + "\n")
    print(f"wrote {fname} ({len(text)} chars)", file=sys.stderr)
    (OUT / "README.md").write_text("\n".join(index) + "\n")
(OUT / "README.md").write_text("\n".join(index) + "\n")
print("done", file=sys.stderr)
