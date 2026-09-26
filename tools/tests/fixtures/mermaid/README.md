# mermaid-cli known-answer fixture

Sanity check of the mermaid-cli row of `tools/toolchain.lock.md` (charter section 8; CM plan section 9.2 step 2). It renders the Mermaid sources of `docs/conops/figures/*.mmd`.

| Case | Command (from this directory; `<out>` is an absolute path outside the repository) | Expected |
|---|---|---|
| Known answer | `/opt/homebrew/bin/mmdc -i known-answer.mmd -o <out>/known-answer.png -b white` | exit 0; a PNG showing the start marker, the states Off, Receive and Transmit, and the transitions labelled "T01 switch on", "T10 key down" and "T11 hang expires"; inspected by eye (visual closure, charter section 11 rule 3) |
| Seeded fault | `/opt/homebrew/bin/mmdc -i seeded-syntax-error.mmd -o <out>/seeded.png` | exit 1 with "Parse error on line 2"; no PNG written |

First run 2026-09-26 by Claude (integrator) at `HEAD` 28e49e6 with this fixture untracked: both cases as expected; the known-answer render was opened and matched the description above.
