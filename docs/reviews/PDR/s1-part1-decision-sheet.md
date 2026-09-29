# First decisions, part 1

Prepared 2026-09-29 for the owner (PDR session S1, items ready now; plan `docs/plan/pdr-work-plan.md` revision 7 section 6.0). Answers are transcribed verbatim into the dated status note.

**Decision needed: 12 items that are ready now.** You may reply "all as recommended", or answer item by item by number. Items 5 and 10 need your own words: for item 5 you may reply "5: use the suggested wording"; for item 10, tell us what you have.

On 2026-09-29 you told us to start work as soon as it can start. So this sheet has only the items of your first session that are ready now. Part 2 comes when its reviews finish, no earlier than Thursday 10-01 in the plan. Reading time: about 20 minutes (estimated).

A yes to all items spends no money and orders nothing. It allows the downloads in items 7, 8, 9 and 11. Claude tells you each size before it downloads. If a site blocks an automated download, Claude stops and you download that file in your browser instead. Items 3 and 7 each start a change request that you decide at your second session.

| # | Item | Recommended answer |
|---|---|---|
| 1 | Secure boot | Off for the first build |
| 2 | How the build ties the firmware to one rustos version | Keep today's method |
| 3 | Where the boot report goes | Serial test pads in the first build, by a change request; USB at the second build |
| 4 | Proof tool and register layer | 4A: proof tool as extra evidence for the keyer and transmit sequencer. 4B: register layer only in safety-critical drivers |
| 5 | Dated statement on exposure limits for friends who run your station | Give it (suggested wording in the item) |
| 6 | How to measure key bounce | Development-board route |
| 7 | Four NASA document downloads | Yes |
| 8 | Three FCC rule texts for our library | Yes; Claude takes the screenshots |
| 9 | Emulator and two Python tool downloads | Yes to both; you make the GitHub copy, or let Claude |
| 10 | Your soldering bench | Tell us three facts |
| 11 | FCC exposure files, terrain program, check of five table rows | 11A yes; 11B yes; 11C Claude does it |
| 12 | Process slips | One formal action request for three open slips |

---

## Item 1. Secure boot: off for the first build

**What we ask.** Should the first build turn on secure boot? Secure boot: the RP2350 runs only firmware signed with a private key. It is set in the chip's one-time memory, so it can never be undone on that chip.

**Options.**
1. Off (recommended). No money or time. Risk: a person holding the radio could load other firmware over USB. You accepted this risk at the requirements review, because the radio has no remote command path. The radio still checks its firmware at every boot, and a failed check keeps the transmitter off.
2. On. No money. Time: a change request before any unit is programmed (signing key custody, handbook procedure, new acceptance tests). Risk: permanent on every chip.

**Our recommendation:** Off, because it cannot be undone, and the boot check already keeps a bad image from transmitting.

**What a yes commits you to:** The software design record states secure boot is off for the first build. Turning it on later needs a change request first.

**What a yes does not do:** It does not change the boot check. It does not turn on the separate permanent debug lock, which also stays off.

**Reply:** "1 yes" for off, or "1 on".

References: OD-13; RSK-015.

---

## Item 2. How the build ties the firmware to one rustos version

**What we ask.** Keep today's method? The build reads rustos from its folder on your Mac. The exact rustos commit is recorded in the tool lock file and every release note. Record builds use a clean export of that commit, and the build check stops on a mismatch.

**Options.**
1. Keep today's method (recommended). No money or time. Risk: Cargo's own lock file does not hold the commit; our records and the build check do.
2. Switch to a git link, so Cargo's lock file holds the commit. No money. Time: a change request to the build files and the configuration plan. Risk: changing build steps that work today.

**Our recommendation:** Keep it, because every build already uses it and the build check catches a wrong commit.

**What a yes commits you to:** The design record adopts today's method. A new rustos commit after the first release still needs a change request.

**What a yes does not do:** It does not move the recorded commit or change rustos.

**Reply:** "2 yes", or "2 git".

References: OD-14; OQ-CM-005.

---

## Item 3. Where the boot report goes in the first build

Boot report: at every start, the radio sends its firmware version, an image fingerprint and its self-test results. The requirement sends it as text over USB. That needs a USB serial driver in rustos, which the software plan rates a large effort and advises against for the first build.

**What we ask.** Choose the route for the first build.

**Options.**
1. By a change request, send the report to the serial test pads the board already has for telemetry; add USB at the second build (recommended). No money. Time: one change request, drafted after this session, checked by an independent reviewer, and decided by you at your second session. Risk: three documents that depend on it are marked "at risk" until then. To read the report you connect to the pads, not just a USB cable (our reading of the requirement).
2. Keep USB in the first build. No money. Time: one more rustos driver, rated a large effort. Risk: more driver work on the schedule.

Serial test pads: two small pads that carry a simple 3.3 V serial signal.

**Our recommendation:** Option 1, because it avoids a large driver job and uses pads the board already has.

**What a yes commits you to:** You approve or reject the change request at your second session.

**What a yes does not do:** It does not change the requirement today. If you reject the change request, the requirement stays, and the USB driver becomes an open item for the critical design review.

**Reply:** "3 yes", or "3 USB".

References: OD-15; REQ-SYS-143; PCR-7.

---

## Item 4. Proof tool and register layer

Two parts. Please answer each.

**4A. Kani, a proof tool.** Kani checks that a stated rule in the code holds for every possible input within set limits. We ask: use it on the keyer and the transmit sequencer, two safety-critical parts, as extra evidence that does not count for credit?
1. Yes, as extra evidence (recommended). No money. Time: Claude writes and runs the proofs; not yet estimated. Kani must be installed. That is a download; file name, source and size not recorded; Claude checks them and tells you before downloading. Risk: none to the test plan, since no credit depends on it.
2. No. No money or time. Those two parts rely only on the planned tests.

**4B. The register layer in the rustos Pico 2 drivers.** Every hardware register read and write goes through a thin layer. On the Mac, a fake register set stands in for the chip, so a driver is tested without hardware. The layer stays inside the Pico 2 driver code; the public rustos traits do not change. We ask you, as rustos maintainer: which drivers use it?
1. Only drivers for safety-critical parts (recommended). No money or time now. The five drivers already written use it: timer, input sampling, PWM, interrupts and clocks. Other drivers keep direct register access and are tested on the board.
2. All drivers. No money. Time: more driver work, not yet estimated.
3. None. No money. Time: the five written drivers go back to direct access, and their register steps are checked only on the board.

**Our recommendation:** 4A yes, because it adds an independent check on the two parts that key the transmitter at no cost to the test plan. 4B option 1, because the drivers safety depends on get tested on the Mac, and it matches the five already written.

**What a yes commits you to:** The design records adopt both. The Kani install comes to you as its own download request.

**What a yes does not do:** Kani replaces no test, and its results do not count as formal verification. The layer adds no driver and changes no public rustos trait.

**Reply:** "4A yes, 4B yes". Other answers: "4A no", "4B all", "4B none".

References: OD-16; ADR-051.

---

## Item 5. Dated statement: exposure limits for friends who run your station

By default, a friend runs one of your radios as their own station, under their own call sign; this item does not affect that. Or the friend runs it as your station, as its designated control operator, with a dated note in your records.

In that second case, the friend is neither the station licensee nor in your household. The FCC rule that lets you use the higher occupational limits for yourself and your household does not cover them; it judges other nearby people against the lower general-public limits. The FCC guidance for amateurs (OET Bulletin 65, Supplement B) treats amateur licensees as in a "controlled environment". The rules also allow occupational limits for a person who knows about the exposure and can control it.

Until you give a dated statement of that basis, radios lent that way stay at the 0.5 W and 1 W steps, where the general-public limits are met in every position, even at the face.

**What we ask.** Give a dated statement in chat that friends who run your station this way are in a controlled environment.

**Options.**
1. Give it (recommended). No money or time. Risk: the basis rests on the FCC guidance and the awareness rule, not the household rule. It is your statement about how you lend radios, so it must match what you will do.
2. Do not give it. Radios lent that way stay at 0.5 W and 1 W. If you will not lend radios this way, this costs nothing.

**Our recommendation:** Give it, because the RF exposure evaluation then has a clear, dated basis for these friends.

**What a yes commits you to:** Claude copies your words exactly into the dated status note. The RF exposure evaluation then judges the 2 W and 5 W steps for these friends against the occupational limits. When you lend a radio this way, you brief the friend as your statement says.

**What a yes does not do:** It raises no power step by itself; the evaluation still decides what each step allows. It does not change the default way.

**Suggested wording (edit as you like):**

> "On [date of my reply], I confirm the following. When I lend a cwht radio to a licensed amateur friend who operates it as the designated control operator of my station, I treat that friend as being in a controlled environment for RF exposure. Before they transmit, I make sure they have read the radio's RF exposure guidance and know how to limit their own exposure. On that basis, the occupational/controlled exposure limits of OET Bulletin 65, Supplement B, apply to them."

**Reply:** "5:" and your statement, "5: use the suggested wording", or "5 no".

References: OD-17; SRR decision 18; 47 CFR 97.13(c)(1), 1.1310(e)(2).

---

## Item 6. How to measure key bounce

Key bounce: a key or paddle contact chatters briefly when it closes. The measured bounce sets the firmware's debounce time.

**What we ask.** Choose how to record bounce at the bench session.

**Options.**
1. Development-board route (recommended). The Pico 2 board samples the contacts 100,000 times a second or faster and sends the samples to the Mac over USB. No money. Time: inside the bench session. Risk: a development check; it guides design values but is not formal verification.
2. Logic-analyzer route: a second Pico 2 with free logic-analyzer firmware, read by the sigrok program on the Mac. Money: about USD 5. Time: a sigrok install first, a download whose size is not recorded; Claude checks it and tells you before downloading. Risk: more setup before the session.

**Our recommendation:** Option 1, because it needs no new parts or downloads.

**What a yes commits you to:** At the bench session you work your key and paddle while the board records. Claude puts the recording mode into the bench firmware (our reading of the plan).

**What a yes does not do:** It does not rule out sigrok. The formal timing tests before the test readiness review still use a second Pico 2, and the sigrok install is decided by the critical design review.

**Reply:** "6 yes", or "6 sigrok".

References: OD-19.

---

## Item 7. Four NASA document downloads

**What we ask.** Permission for Claude to download the NASA Software Assurance and Software Safety Standard and three checklists from the NASA software handbook. Today we use the standard's definition of safety-critical software, from the handbook, but not its full list of requirements, because the file is not in our library. So two software requirements are tailored: software assurance under the standard, and its safety-critical requirements.

| File | Source site | Size |
|---|---|---|
| NASA-STD-87398-Revision-B.pdf (the standard) | standards.nasa.gov | Not recorded |
| Design Practices for Safety.docx | swehb.nasa.gov | Not recorded |
| PAT-007 - Checklist for General Software Safety Requirements.docx | swehb.nasa.gov | Not recorded |
| PAT-071 Preliminary Design Milestone Review.docx | swehb.nasa.gov | Not recorded |

Size not recorded; Claude checks it and tells you before downloading. If a site blocks Claude, you download that file in your browser instead.

**Options.**
1. Permit (recommended). No money. Time: Claude maps the standard row by row and runs the review checklist on the software products.
2. Do not permit. The two requirements stay tailored, and the design review record states the gap as an open risk.

**Our recommendation:** Permit, so we can aim for full compliance instead of stating a gap at the review.

**What a yes commits you to:** Claude downloads the files after telling you their sizes, then drafts a change request that updates the two tailored requirements. You decide on it at your second session.

**What a yes does not do:** It changes no requirement or tailoring today.

**Reply:** "7 yes", or "7 no".

References: OD-21; SWE-022, SWE-023.

---

## Item 8. Three FCC rule texts for our library

**What we ask.** Approve adding three FCC rule texts to our library of regulations.
1. The allocation table from 150.8 to 174 MHz, with footnotes. A transmission outside the 2 m band could land in the public-safety and marine services there, and the hazard analysis needs these rules word for word. The table exists only as page images, which Claude's download tool could not fetch. So someone takes screenshots on the official eCFR page (ecfr.gov): you, or Claude in its own built-in browser. The footnotes come as text from ecfr.gov (562 kB when fetched on 2026-09-25).
2. The marine rule that sets 156.800 MHz as the distress, safety and calling channel, as text from ecfr.gov.
3. The FCC marketing rule (47 CFR 2.803) and its 2026-09-11 amendment, from ecfr.gov and federalregister.gov. Our five-unit build limit rests on the home-built device rule, which depends on what "marketing" means.

For texts 2 and 3: size not recorded; Claude checks it and tells you before downloading. If a site blocks Claude, you download that file in your browser instead.

**Options.**
1. Approve; Claude takes the screenshots (recommended). No money. Risk: if the site shows Claude a robot check, Claude stops and asks you.
2. Approve; you take the screenshots. Time: a few minutes of yours (estimated).
3. Do not approve. The hazard analysis lacks the exact text, and the build-limit reading stays on the older text.

**Our recommendation:** Option 1, because it saves you time.

**What a yes commits you to:** Claude adds each text to the library with its source and date.

**What a yes does not do:** It changes no requirement. If a text changes a requirement's basis, Claude brings you a change request.

**Reply:** "8 yes", "8 yes, I take the screenshots", or "8 no".

References: OD-24a; owner action pack section 7.

---

## Item 9. Emulator and two Python tool downloads

Two parts; "9 yes" answers both.

**9A. The emulator.** An emulator runs the radio firmware on the Mac as if it were the Pico 2 chip. We use it only to check the order of events, never timing. The candidate is rp2350js, a free project with one maintainer. We ask permission to download and test it; which emulator to use is decided at your second session.

**9B. Two Python tools.** ruff checks the project's Python tools for defects, unsafe code and too much complexity. coverage.py measures how much of each tool its tests exercise. We ask permission to download both.

| File | Source site | Size |
|---|---|---|
| rp2350js source code at commit af0114cb | github.com (c1570/rp2350js) | Not recorded |
| Its locked JavaScript packages (428 in the earlier research install) | npm registry (npmjs.com) | Not recorded |
| ruff, current release on the day you permit | pypi.org | Not recorded |
| coverage, current release on the day you permit | pypi.org | Not recorded |

Size not recorded; Claude checks it and tells you before downloading. If a site blocks Claude, you download that file in your browser instead.

The emulator also needs a GitHub copy of the project under your account, so the code cannot disappear. This is your action, from the requirements review decisions. You make it with the Fork button on GitHub. Or you may let Claude make it with the GitHub command-line tool, if that tool is signed in on this Mac; Claude checks first and makes no copy without your yes.

**Options.**
1. Permit both (recommended). No money. Time: Claude runs known-answer checks. Risk: low; the emulator never touches the radio's firmware image.
2. Refuse 9A: the planned emulator checks move to bench tests on real hardware, by a change request.
3. Refuse 9B: the Python tool check stays open, and the design review record states the gap.

**Our recommendation:** Permit both, because each unblocks a planned check at no cost.

**What a yes commits you to:** Claude downloads these into project folders, not the whole Mac (our reading of the plan). You make the GitHub copy, unless you let Claude. The emulator choice and the tools' approval come at your second session.

**What a yes does not do:** It does not choose the emulator or approve the tools.

**Reply:** "9 yes" (you make the copy), or "9 yes, Claude makes the copy". Or "9A yes, 9B no".

References: OD-25; TV-024; SRR decision 102.

---

## Item 10. Your soldering bench

You will solder the boards at home, and the hazard analysis needs your bench tools confirmed. The main dangers are a fire from a hot iron left off its stand, burns, flux fumes and eye injury.

On 2026-09-27 you said: "I don't have like a very sophisticated soldering setup. I have a heat gun um, I have solder I have flux". So the heat gun, solder and flux are confirmed.

**What we ask.** Three facts:
1. Your soldering iron: make and model, if known. Does it have temperature control, a stand, and auto-sleep or auto-off? Is the tip grounded?
2. Fume extraction: a fume extractor or a fan that pulls fumes away?
3. Eye protection: safety glasses?

**Options, for any gap.**
1. Buy it inside your USD 300 cap on new equipment, after Claude compares models and prices (recommended). Money: not yet estimated. The cap is tight: the four test items you need are estimated at USD 242 to 339, so a new iron may push a lower item out, to be borrowed or deferred.
2. Borrow it.

**Our recommendation:** For any gap, buy inside the cap after Claude's comparison, because a temperature-controlled iron with auto-sleep guards against the worst bench danger, a fire.

**What a yes commits you to:** Claude records your tools in the hazard analysis. For a gap, Claude sends a short comparison with prices, and you decide whether to buy, keeping the total at or below USD 300.

**What a yes does not do:** It buys nothing. A missing tool is needed only before you solder the first board.

**Reply:** "10: iron [make and model], temperature control yes or no, stand yes or no, auto-sleep yes or no, grounded tip yes, no or unknown; fume extraction yes or no; eye protection yes or no."

References: OD-32; owner action pack section 6.

---

## Item 11. FCC exposure files, terrain program, check of five table rows

Three parts. Please answer each.

**11A. FCC exposure guidance and two SAR test reports.** SAR (specific absorption rate): how much radio energy the body absorbs. Our RF exposure evaluation now takes its SAR data from two ARRL articles. These files give primary data (measured SAR, power, duty, test positions), and the evaluation cites them. Recommended: permit. If you do not, the evaluation keeps resting on the two articles.

| File | Source site | Size |
|---|---|---|
| KDB 447498 D01, current version (RF exposure of mobile and portable devices) | fcc.gov/kdb (files on apps.fcc.gov) | Not recorded |
| KDB 643646 D01 (SAR tests for push-to-talk radios) | fcc.gov/kdb (files on apps.fcc.gov) | Not recorded |
| SAR report, FCC ID AZ489FT4948 (Motorola VHF handheld, 136 to 174 MHz) | FCC equipment authorization database | Not recorded |
| SAR report, FCC ID AZ489FT7098 (Motorola VHF handheld, 136 to 174 MHz) | FCC equipment authorization database | Not recorded |

Size not recorded; Claude checks it and tells you before downloading. Earlier automated fetches of these files were refused. If a site blocks Claude, you download that file in your browser instead.

**11B. SPLAT!, a terrain program (optional).** SPLAT! is a free program that predicts radio range over real terrain. It installs through Homebrew; size not recorded; Claude checks it and tells you before downloading. It needs the locations of the sites you and your friends plan to use. Recommended: install it, as the requirements review recommended, so the range goals get an analysis for your actual sites. If the install fails, the range estimates fall back to the standard Egli formula for VHF paths, and range is still checked on the air.

**11C. Check of five rows of the FCC allocation table.** Our copy of the rows for the 2nd, 3rd, 4th, 5th and 7th harmonics of 144 to 148 MHz comes from the FCC's 2022 text table plus later amendments. It is medium confidence until checked against the current eCFR page images. Recommended: Claude checks the rows in its own browser, to save you time; if the site blocks it, Claude asks you. Otherwise you view the rows and send screenshots.

**Cost of all three:** no money.

**What a yes commits you to:** Claude downloads the FCC files and SPLAT! after telling you their sizes. Claude checks the five rows and records the result.

**What a yes does not do:** It changes no requirement or power step. If a check shows a difference, Claude reports it, with a change request if a requirement is affected.

**Reply:** "11A yes, 11B yes, 11C Claude". Other answers: "11A no", "11B no", "11C I do it".

References: OD-39; SRR decision 82.

---

## Item 12. Process slips: one formal action request

Our deviation log lists times we did not follow our own process. Four recent slips:
- Slip 1 (closed): a change request was approved before one required review. The review was done on 2026-09-29 and changed nothing in your approval. The rule that requires this review already existed. A new check point that stops it happening again is in the approved rule-book change, which merges at your second session.
- Slip 2 (open): large simulation files (238 files, 1.17 GB) were committed to git against the configuration plan. You chose to push as is.
- Slip 3 (open): an agent rewrote its own unpushed commit to fix the message. The rule forbids rewriting commits on the main branch, pushed or not. No pushed history changed.
- Slip 4 (open): eight commits fail the project's message-format checker, mostly because a blank line cuts the labels off. The history is kept as made. Each merge commit carries the right labels, so each change is still identified.

A formal corrective-action request is a tracked action with an owner, a due date and a check at closure.

**What we ask.** Raise one request covering slips 2, 3 and 4, and none for slip 1. Its actions:
- Slip 2 closes when the file storage rules you approved on 2026-09-29 merge, at your second session.
- Slips 3 and 4 close when every agent brief states the commit rules and the commit-message checker runs at every commit. Turning the checker on at every commit comes with its tool approval in part 2, as the tool's own record says.

**Options.**
1. One request for slips 2, 3 and 4 (recommended). No money. Time: small (estimated); Claude does the actions.
2. No request. Our indicator for process slips shows red for the three open slips until they close.
3. One request per slip. No money. Time: three items to track instead of one.

**Our recommendation:** One request, because our indicator for process slips turns red for any open slip without a request, and the first four log entries were handled the same way, with one request.

**What a yes commits you to:** One more item on the list you check at the design review, where you confirm its answer.

**What a yes does not do:** It rewrites no history and turns on no checker now.

**Reply:** "12 yes". Other answers: "12 no" or "12 separate".

References: deviations log entries 5 to 8 (slips 1 to 4); TPM-018.
