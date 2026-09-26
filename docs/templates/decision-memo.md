---
review: <SRR | PDR | CDR | TRR | SAR | TRR-Dn>
package_revision: <n>
disposition: null            # Approved | Approved with liens. Set only by the session whose owner wording approves; stays null while unsigned and for a Not approved session
signed: null                 # YYYY-MM-DD of the owner's approval wording in section 12. Set only with an approving disposition; null otherwise. tools/review_trend.py reads this key as the gate date and ignores a memo whose value is null (review process section 11)
baseline_tag: null           # baseline/<review> for SRR, PDR, CDR, SAR once tagged; null for TRR, TRR-Dn and while unsigned
revoked: null                # YYYY-MM-DD only if the owner revokes the approval after a missed lien (review process section 12.2); signed, disposition and baseline_tag are then kept unchanged
---

# <REVIEW> Decision Memo

Template: `docs/templates/decision-memo.md`. Copy to `docs/reviews/<REVIEW>/decision-memo.md`. This memo is the review board report and the Decision Authority's decision record required by NPR 7123.1D §5.2.3.1 items b, g and i. It is completed per `docs/process/01-lifecycle-and-reviews.md` section 9, called "the review process" below. Claude writes it, and it is signed by transcribing the owner's approval wording.

The memo is amended, never rewritten: later changes are appended in section 13. The front matter is machine-read:

- `signed` and `disposition` are written once, by the session that approves (*Approved* or *Approved with liens*), in the same commit that fills section 12.
- A *Not approved* session leaves both keys `null` and is recorded only in section 2 and section 9 (review process section 12.1).

## 1. Identification

| Field | Value |
|---|---|
| Review | `<SRR / PDR / CDR / TRR / SAR / TRR-Dn>` |
| Package | `docs/reviews/<REVIEW>/package.md` revision `<n>` at commit `<hash>` |
| Slide deck presented | `docs/reviews/<REVIEW>/slides/<review>.adoc` at commit `<hash>`, `<n>` slides (`slides/png/slide-01.png` to `slide-<NN>.png`), presented slide by slide (review process section 3.4) |
| Minutes | `docs/reviews/<REVIEW>/minutes.md` (in slide order) |
| RFA/RID log | `docs/reviews/<REVIEW>/rfa-rid-log.json`, which passed `tools/validate_docs.py` and the item check of review process section 10.4 on `<date>` |
| Chair and Decision Authority | Robin (also Engineering TA and SMA TA) |
| Presenter | Claude (main session) |
| Purpose of the gate | `<one sentence from review process section n.1>` |

## 2. Sessions

One row per session, including every *Not approved* session. A re-review adds a row; it never edits an earlier row.

| Session | Date | Package revision | Slides presented | Outcome |
|---|---|---|---|---|
| 1 | `<YYYY-MM-DD>` | `<n>` | `<01 to NN>` | `<dispositioned / continued / Not approved, re-review required (front matter unchanged)>` |

## 3. Entrance criteria summary

- Hard criteria: `<n>` of `<n>` met at readiness declaration on `<date>`, including S11 (deck rendered and inspected).
- Soft criteria not met, accepted as liens: `<Routine RFA ids raised per review process section 3.1 item 5, or None>`.
- Hard criteria found unmet during the review (forces *Not approved*): `<None / list>`.

## 4. Success criteria assessment (§5.2.3.1 c)

| # | Success criterion (short) | Ruling | Lien id | Chair note |
|---|---|---|---|---|
| C1 | | `<Met / Met with lien / Not met>` | | |
| `<gate 1>` | | | | |

Every *Met with lien* ruling names the Routine RFA raised for it (review process section 3.1 item 5). A *Not met* ruling forces *Not approved* (review process section 9 row c).

## 5. RFA/RID summary (§5.2.3.1 a, d)

| Type | Severity | Raised | Closed at signing | Verified pending | Answered | Open | Withdrawn |
|---|---|---|---|---|---|---|---|
| RID | Major | | | | | | |
| RID | Minor | | | | | | |
| RFA | Blocking | | | | | | |
| RFA | Routine | | | | | | |

Agreement on disposition of every item: `<yes>`. Major RIDs and Blocking RFAs are all Closed: `<yes / not applicable>`.

Reviewer findings adopted: `<n>` as RIDs, `<n>` as RFAs, `<n>` No action. Each ruling is recorded against the finding's `#finding-<n>` entry in its record `docs/reviews/<REVIEW>/checklists/<product-slug>.md` (front matter `id: INSP-NNN`; review process section 10.1).

## 6. Liens (§5.2.3.1 e)

The rule (review process section 12.2): every RFA or RID of this review still Open, Answered or Verified at signing is a lien. It carries `lien: true` in the log, gets a same-state `history` entry `Lien accepted in docs/reviews/<REVIEW>/decision-memo.md` dated the signing date (review process section 10.3), and appears in this table. *Approved* means this table is empty. Each lien id is an RFA id, a RID id or, for a TBR, the `REQ-<MOD>-NNN` id. A Soft-criterion or *Met with lien* shortfall is identified by the Routine RFA raised for it.

| Lien id | Type | Owner | Closure plan | Due (event or date) | blocks-order (CDR only) | Status at signing |
|---|---|---|---|---|---|---|
| `<RFA-/RID-/REQ- TBR>` | | | | | `<yes / no>` | `<Open / Answered / Verified>` |

Checked that none of the items that may never be liens (review process section 12.2) is present: `<none present>`. Each Minor RID's due is the next gate's readiness declaration, at the latest (review process section 10.2).

## 7. Tailoring approved (success criterion C4; App. G Table G-4 s12 "Proposed tailoring is appropriate"; SE HB §3.11.6 approval via the compliance matrix)

| Matrix | Row | Disposition | Rationale accepted | Recorded in matrix at commit |
|---|---|---|---|---|
| `<rmm.json / se-compliance-matrix.json>` | `<SE-NN / SWE-NNN>` | `<FC / T / NA>` | `<yes>` | `<hash>` |

SRR only: the deviation for the reviews not held, SE-55 and SE-56 (DR and DRR; compliance matrix rows T, relief type deviation), is approved here by the owner as Engineering Technical Authority, per SE-06 and review process sections 1 item 3 and 3.5: `<approved / not approved>`.

### 7.1 RMM approval (SRR; repeated at a later gate only when RMM rows changed)

Per `docs/process/03-software-classification-and-rmm.md` section 9 (decision record and owner signature block):

- `rmm.json` content approved at commit `<hash>`;
- T rows approved: `<SWE ids>`;
- NA rows approved: `<SWE ids>`;
- rows approved with liens: `<RFA / RID ids or None>`.

Each approval in the 03 section 9 signature block has its own line, transcribed from the owner's actual wording:

| Approval (03 section 9) | Owner wording, verbatim | Date |
|---|---|---|
| RMM approval as ETA and SMA TA | "`<owner wording, verbatim>`" | `<YYYY-MM-DD>` |
| Relief for SWE-154, 156, 157, 159 and 210, as CIO/SAISO designee | "`<owner wording, verbatim>`" | `<YYYY-MM-DD>` |
| Health and medical implications of the SWE-022, SWE-023 and SWE-219 tailoring, reviewed as HMTA | "`<owner wording, verbatim>`" | `<YYYY-MM-DD>` |
| Human safety risk of the SWE-022, SWE-023 and SWE-219 tailoring, accepted as the risk taker | "`<owner wording, verbatim>`" | `<YYYY-MM-DD>` |
| Classification and safety-critical determination (03 sections 3 and 4), approved as SMA TA with independent concurrence `INSP-<NNN>` (`docs/reviews/SRR/checklists/classification-03-software-classification-and-rmm.md`, checklist `docs/templates/peer-review-checklist-classification.md`) | "`<owner wording, verbatim>`" | `<YYYY-MM-DD>` |

Note: 03 section 9 suggests wordings such as "Approved as ETA and SMA TA". Transcribe what the owner actually said, not the suggestion (charter section 2). A line the owner did not approve stays empty, and the matching rows are not approved.

## 8. Decisions taken at the review

| Decision | Record | Constrains |
|---|---|---|
| `<one line>` | `<ADR-NNN / TS-NNN / CR-NNN>` | `<phase or product>` |

Residual risks accepted by the owner: `<RSK-NNN list or None>`.

## 9. Disposition

**`<Approved / Approved with liens / Not approved>`**

A *Not approved* disposition is written here and in section 2 only. The front-matter keys `disposition` and `signed` stay `null` until an approving session.

Conditions attached: `<text or None>`. For CDR, the owner places the vendor orders only when the `blocks-order` liens are Closed. For TRR, the first powered test may start only after `<conditions>`.

OnAir authorization (on-air delta TRR only; `docs/process/04-verification-and-validation.md` section 6.3): every regulatory `REQ-TX-*` emission case is `Passed` (`<TC ids and report ids>`); residual risk accepted for `<RSK-NNN, e.g. spurious emissions verified by analysis only / None>`; owner wording: "`<...>`". Delete this block for every other review.

## 10. Baseline

| Field | Value |
|---|---|
| Baseline | `<Functional / Allocated / Product / As-built / none (TRR, TRR-Dn)>` |
| Tag | `baseline/<review>`. It is created on the baseline-record commit R that follows this memo's commit (`docs/process/05-configuration-and-data-management.md` section 4.4 steps 3 and 5), so this memo does not carry the tagged commit hash. The tagged commit, the tag object and the pushed hash are recorded in `docs/reviews/<REVIEW>/baseline-record.md` |
| Baseline record | `docs/reviews/<REVIEW>/baseline-record.md` (template `docs/templates/baseline-record.md`) |
| Items now under change control | `<paths>` |

## 11. Dissent (§5.2.3.1 f)

`<None>`, or: presenter position, owner ruling, plan to resolve, date.

## 12. Approval (§5.2.3.1 i)

Owner statement, transcribed verbatim from the conversation:

> "`<wording>`" - Robin, `<YYYY-MM-DD HH:MM>` local time.

The commit that fills this section sets the front-matter keys `signed` (to this date) and `disposition` (to the approving disposition). The signature of the Decision Authority is this transcription plus that commit; no other signature exists.

This file cannot state its own commit hash. The memo commit is recorded as follows:

- SRR, PDR, CDR and SAR: in the section 1 "Decision memo" row of `docs/reviews/<REVIEW>/baseline-record.md` (`memo commit <hash>`) and in the tag message (`... decision memo docs/reviews/<REVIEW>/decision-memo.md at <memo commit>`), per `docs/process/05-configuration-and-data-management.md` section 4.4 steps 2 and 5.
- TRR and TRR-Dn: in section 13 of this memo, as an amendment row committed with the trailer `Refs: <REVIEW>` immediately after the memo commit (the memo is a Record-class CI, CM plan Table 4-1 row 33, so its commits carry `Refs:`; `Editorial:` applies to class-CR CIs only).

Review complete per §5.2.3.1 items a to i: `<yes>`. Follow-up controls (item h): open items appear in the next package burndown and in the review-trend TPM.

## 13. Amendments

| Date | Item | Change | Rationale | Owner wording | Commit trailer |
|---|---|---|---|---|---|
| `<date>` | `<memo commit (TRR, TRR-Dn)>` | `<memo committed at <hash>>` | Records this file's own commit (section 12) | n/a | `Refs: <REVIEW>` |
| `<date>` | `<lien id>` | `<extended to ... / converted to CR-NNN or RSK-NNN / re-severitized / revoked (front matter revoked set)>` | | "`<...>`" | `Refs:` |
| `<date>` | `<re-review session n>` | `<approved after revocation; package revision n>` | | "`<...>`" | `Refs:` |
