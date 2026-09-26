---
baseline: <functional | allocated | product | as-built>
review: <SRR | PDR | CDR | SAR>
tag: baseline/<srr|pdr|cdr|sar>
date: YYYY-MM-DD
decision_memo: docs/reviews/<REVIEW>/decision-memo.md
disposition: <Approved | Approved with liens>
previous_baseline: <baseline/<...> | none>
# Fill-once fields (CM plan Table 4-1 row 32): each holds "pending (§8a)" in the tagged commit R
# and is written exactly once in the post-tag record commit (CM plan §4.4 step 6).
commit: pending (§8a)                 # SHA of the tagged commit R, `git rev-parse baseline/<review>^{commit}`
tag_object: pending (§8a)             # SHA of the tag object, `git rev-parse baseline/<review>`
signed: pending (§8a)                 # true | false; false is compliant until the owner configures a key (charter §8, CM plan §4.4)
signature_verified: pending (§8a)     # true | false | n/a (unsigned tag), from `git tag -v`
pushed_hash: pending (§8a)            # hash returned by `git ls-remote --tags origin baseline/<review>`
---

# Baseline record: <name> baseline (`baseline/<review>`)

Template: `docs/templates/baseline-record.md`. Procedure: `docs/process/05-configuration-and-data-management.md` §4.4. Location: `docs/reviews/<REVIEW>/baseline-record.md`. Class: Record (CM plan Table 4-1 row 32). This file is committed on `main` as commit R (§4.4 step 3) and the tag is created on R, so the tag points at the commit that contains the record. Data known only after tagging (the tagged commit's own SHA, the tag object hash, the verification output, the push hash, the reviewer and approval rows) is written exactly once in §8a, §9 and the fill-once front-matter fields by the post-tag record commit `baseline(<review>): record tag verification` with trailer `Refs: <REVIEW>` (§4.4 step 6). Nothing else in the file changes after R; corrections are dated entries in §10.

## 1. Baseline definition

| Field | Value |
|---|---|
| Baseline | <name> baseline per SE HB §6.5.1.2.2, set at <review> per charter §3 and CM plan §4.4 (customizations in CM plan §1) |
| Contents | Table 4-1 rows: <list, from CM plan §4.4> |
| Decision memo | `docs/reviews/<REVIEW>/decision-memo.md`, disposition <Approved, or Approved with liens>, date; memo commit `<hash>` (the commit that set `signed` in the memo front matter, `git log -1 --format=%H -- docs/reviews/<REVIEW>/decision-memo.md` before R; CM plan §4.4 step 2) |
| Review package | `docs/reviews/<REVIEW>/package.md` |
| Traceability report at this commit | `docs/reviews/<REVIEW>/traceability-report.md`; result: clean |
| `git fsck --full` on the parent of R | <result line; exit 0 required> |
| Table 4-1 match check (`git ls-files` against the Table 4-1 pathspecs) | <n files, 0 unmatched> |

## 2. Configuration items

Hash from `git ls-tree HEAD -- <path>` on the parent of R (blob for files, tree for directories). Peer review = the filled checklist `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (id `INSP-NNN`) required for level L1 (CM plan §4.1; charter §5). There is no `peer-reviews/` folder.

### 2a. CIs in this baseline (class CR)

| Row (Table 4-1) | CI | Path | Hash | Level after tag | Peer review record (`INSP-NNN`, checklist path) | Notes |
|---|---|---|---|---|---|---|
| 1 | Process charter | `docs/process/00-charter.md` | | L2 | | |
| | | | | | | |

### 2b. Informational items (recorded, not yet CR-controlled; e.g. preliminary design data at PDR)

| Row | CI | Path | Hash | Current level |
|---|---|---|---|---|
| | | | | |

### 2c. Controlled items outside the baseline set (rows 25, 26 and 28 after their CR-from event)

| Row | CI | Path or pin | Hash or commit | CR-from event and date | TV record (row 28) |
|---|---|---|---|---|---|
| | | | | | |

## 3. Approved changes and waivers since the previous baseline

| CR | Title | Class | Closed | Merge SHA | CIs affected |
|---|---|---|---|---|---|
| | | | | | |

| Waiver id (`CR-NNN` or `<memo path>#W<n>`) | Requirement or target | Approving memo or CR | Status |
|---|---|---|---|
| | | | |

Requirements volatility over the interval (CM plan §5.4): L1 <n/N>, L2 <n/N>.

## 4. Editorial changes to controlled CIs since the previous baseline

| Commit | Path | Reason (from `Editorial:` trailer) | Sampled by reviewer |
|---|---|---|---|
| | | | |

## 5. Liens, open RIDs/RFAs and TBRs carried forward

| Item | Type (lien / RID / RFA / TBR) | Owner | Closure plan | Target review |
|---|---|---|---|---|
| | | | | |

## 6. Releases included (product and as-built baselines only)

| Release ID | Tag | Directory | `SHA256SUMS` hash (and `SHA256SUMS.normalized` for hardware) | Vendor records / VDD |
|---|---|---|---|---|
| | | | | |

At SAR the technical data package updated with all test results (NPR 7123.1D App. G Table G-11 entrance item 3, sub-item 6; CM plan §10.6) is this record plus the unit acceptance data packages: list every credited report in `docs/vv/reports/` with its hash in the table below.

| Report | Hash | Unit or release |
|---|---|---|
| | | |

## 7. Tool accreditation state at this baseline

| Tool | Version (from `tools/toolchain.lock.md`) | Class | TV record | Status |
|---|---|---|---|---|
| | | | | |

## 7a. Archive (SAR and closeout only; CM plan §8.4)

| Archived file (in `/Users/robinonsay/rust/cwht-archive/<gate>/`) | SHA-256 | Source (lock §7) |
|---|---|---|
| `cwht-<date>.bundle` | | `git bundle create ... --all` |
| | | |

Off-machine location (OQ-CM-007): <owner's choice>; copied on YYYY-MM-DD.

## 8. Tag creation and verification commands

```
git tag -a baseline/<review> <R> -m "cwht <name> baseline; decision memo docs/reviews/<REVIEW>/decision-memo.md at <memo commit>"   # -s instead of -a once tag.gpgSign is configured (CM plan §4.4 step 5); <memo commit> is the §1 "Decision memo" hash
git tag -v baseline/<review>          # signed tag
git cat-file -p baseline/<review>     # unsigned tag: tagger, date, message, target commit
git push origin main --follow-tags
git ls-remote --tags origin baseline/<review>
git ls-remote origin refs/heads/main  # remote sync observation (CM plan §10.4)
```

## 8a. Post-tag verification (fill-once, written in the post-tag record commit)

Output of `git tag -v` (signed) or `git cat-file -p` (unsigned), verbatim:

```
<output>
```

Remote push: `git push origin main --follow-tags` on YYYY-MM-DD; `git ls-remote --tags origin baseline/<review>` returned `<hash>`; `git ls-remote origin refs/heads/main` returned `<hash>` (equal to local `main`: yes/no). If the push failed: bundle `<path>` SHA-256 `<hash>`, deviation logged in CSA item 11, push completed on YYYY-MM-DD (CM plan §10.4).

## 9. Approvals (fill-once, written in the post-tag record commit)

| Step | By | Date | Result |
|---|---|---|---|
| Baseline record prepared (commit R) | Claude | | |
| Record checked against the repository at R (every hash by `git ls-tree R -- <path>`) | <independent reviewer agent> | | |
| Baseline approved (decision memo) | Owner | | |

## 10. Corrections (append only)

| Date | Correction | Reference (CR or `Editorial:` commit) |
|---|---|---|
| | | |
