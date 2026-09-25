# Reference documents

PDFs are not committed (see .gitignore); markdown conversions under `md/` are the working corpus and are vector-indexed.

| Document | Source | Conversion |
|---|---|---|
| NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 | https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf | `tools/refs/se_handbook_to_md.py` (pdftotext) |
| NPR 7123.1D, NASA Systems Engineering Processes and Requirements | https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D | `tools/refs/nodis_to_md.py N_PR_7123_001D_ npr-7123-1d "NPR 7123.1D" Preface Chapter1 ... AppendixK` |
| NPR 7150.2D, NASA Software Engineering Requirements | https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D | `tools/refs/npr7150_to_md.py` |
| NASA-HDBK-2203, NASA Software Engineering Handbook (SWEHB Ver D) | https://swehb.nasa.gov/display/SWEHBVD | `tools/refs/swehb_scrape.py` (paced page-view scrape) |
