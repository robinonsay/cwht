"""cwht keyer host study: reference keyer, debounce, interlock and safe-state monitor model.

WP-PDR-33 (docs/plan/pdr-work-plan.md section 3.7). Analysis note:
docs/design/analysis/keyer-host-study.md. This module is the host timing model of the keyer
(SEMP section 7.3.1 "keyer timing model on the host"). It is an analysis model, not the flight
code: the flight keyer is the cwht-core keyer of WP-PDR-41 and its HostUnit cases. Results
from this model are developer evidence (docs/process/05-configuration-and-data-management.md
section 9.1) until a TV record covers it.

Semantics are those of docs/research/keyer-verification-and-key-input-network.md:
  F6 debounce (make 2 samples, break 5 samples at 1 kHz, sample k at t = k ms),
  F7 reference keyer semantics rules 1 to 6 (Iambic A, Iambic B with switchpoint S),
  F13 interlock (500 consecutive open samples), manual-closure timeout, paddle watchdog,
  F14 reconciled number set (ratio 3.0, weight 50 percent, key compensation 0).
Ultimatic and Bug semantics are stated in the note, section 3.2.

Time base: integer milliseconds for input samples; element and space boundaries in
microseconds (float), so element timing is exact to below 1 us (F8: TIMER0 has 1 us resolution).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------------------------
# Morse table. ITU-R M.1677-1 section 1 characters (letters, figures, punctuation and the
# service signals), transcribed by the author; the corpus has no copy of the standard (note
# section 2, input I-12). EXTRA marks common amateur characters that ITU-R M.1677-1 does not
# list; they are kept because amateurs send them and they include the longest alternating run.
# ---------------------------------------------------------------------------------------------
ITU = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    ".": ".-.-.-", ",": "--..--", ":": "---...", "?": "..--..", "'": ".----.", "-": "-....-",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", '"': ".-..-.", "=": "-...-", "+": ".-.-.",
    "@": ".--.-.",
    # ITU-R M.1677-1 service signals, written here with a token in angle brackets
    "<UNDERSTOOD>": "...-.", "<ERROR>": "........", "<WAIT>": ".-...", "<SK>": "...-.-",
    "<CT>": "-.-.-",
}
EXTRA = {";": "-.-.-.", "!": "-.-.--", "$": "...-..-", "_": "..--.-"}
MORSE = {**ITU, **EXTRA}

MODES_PADDLE = ("A", "B", "U")  # Iambic A, Iambic B, Ultimatic (REQ-SYS-184 scope)


def dit_us(wpm: float) -> float:
    """PARIS dit length in microseconds (F7, F14: dit = 1200/WPM ms)."""
    return 1_200_000.0 / wpm


# ---------------------------------------------------------------------------------------------
# Debounce (F6): confirmed closed after n_make consecutive closed samples, confirmed open after
# n_break consecutive open samples.
# ---------------------------------------------------------------------------------------------
@dataclass
class Debouncer:
    n_make: int = 2
    n_break: int = 5
    state: bool = False
    run: int = 0

    def update(self, raw: bool) -> bool:
        if raw == self.state:
            self.run = 0
            return self.state
        self.run += 1
        if (raw and self.run >= self.n_make) or ((not raw) and self.run >= self.n_break):
            self.state = raw
            self.run = 0
        return self.state


def closed_at(intervals, k_ms: int) -> bool:
    """Raw contact state at sample k: closed if a <= k < b for any interval (a, b) in ms."""
    for a, b in intervals:
        if a <= k_ms < b:
            return True
    return False


# ---------------------------------------------------------------------------------------------
# Keyer engine (F7 rules 1 to 6; Ultimatic and Bug as in the note section 3.2).
# ---------------------------------------------------------------------------------------------
@dataclass
class KeyerResult:
    elements: list = field(default_factory=list)  # (start_us, end_us, 'dit'|'dah')
    deb_dit: list = field(default_factory=list)   # debounced change times (ms, state)
    deb_dah: list = field(default_factory=list)

    def pattern(self) -> str:
        return "".join("." if e[2] == "dit" else "-" for e in self.elements)

    def intervals_ms(self):
        return [(round(s / 1000.0, 3), round(e / 1000.0, 3)) for s, e, _ in self.elements]


def simulate(mode: str, wpm: float, dit_iv, dah_iv, duration_ms: int, switchpoint: float = 0.5,
             debounce: bool = True, ratio: float = 3.0) -> KeyerResult:
    """Run the reference keyer on raw paddle closure intervals (ms, half-open).

    mode: 'A' Iambic A, 'B' Iambic B with switchpoint S, 'U' Ultimatic. Bug and Straight are
    analysed without this engine (note section 3.2). Returns the key-down elements and the
    debounced traces.
    Tie rule: at an instant where a sample and an element boundary coincide, the sample is
    processed first (note section 3.2).
    """
    dit = dit_us(wpm)
    dah = ratio * dit
    db_dit = Debouncer() if debounce else None
    db_dah = Debouncer() if debounce else None
    res = KeyerResult()
    st = {"dit": False, "dah": False}
    state = "IDLE"           # IDLE, ELEMENT, SPACE
    etype = None
    e_start = e_end = s_end = 0.0
    alt_latch = rep_latch = False
    last_closed = None       # Ultimatic

    def length(t):
        return dit if t == "dit" else dah

    def start_element(t, when):
        nonlocal state, etype, e_start, e_end, s_end, alt_latch, rep_latch
        state = "ELEMENT"
        etype = t
        e_start = when
        e_end = when + length(t)
        s_end = e_end + dit
        alt_latch = rep_latch = False
        res.elements.append([when, e_end, t])

    def decide(when):
        nonlocal state, etype
        opp = "dah" if etype == "dit" else "dit"
        if mode in ("A", "B"):
            if alt_latch or st[opp]:
                start_element(opp, when)
            elif rep_latch or st[etype]:
                start_element(etype, when)
            else:
                state = "IDLE"
                etype = None
        elif mode == "U":
            if st["dit"] and st["dah"]:
                start_element(last_closed, when)
            elif alt_latch or st[opp]:
                start_element(opp, when)
            elif rep_latch or st[etype]:
                start_element(etype, when)
            else:
                state = "IDLE"
                etype = None

    def process_transitions(until_us, inclusive):
        nonlocal state
        while True:
            if state == "ELEMENT":
                t_next = e_end
            elif state == "SPACE":
                t_next = s_end
            else:
                return
            if t_next < until_us or (inclusive and abs(t_next - until_us) < 1e-6):
                if state == "ELEMENT":
                    state = "SPACE"
                else:
                    decide(t_next)
            else:
                return

    for k in range(duration_ms + 1):
        t = k * 1000.0
        process_transitions(t, inclusive=False)
        raw_d = closed_at(dit_iv, k)
        raw_h = closed_at(dah_iv, k)
        prev = dict(st)
        st["dit"] = db_dit.update(raw_d) if debounce else raw_d
        st["dah"] = db_dah.update(raw_h) if debounce else raw_h
        rise = {p: (st[p] and not prev[p]) for p in st}
        for p, lst in (("dit", res.deb_dit), ("dah", res.deb_dah)):
            if st[p] != prev[p]:
                lst.append((k, st[p]))
        if rise["dit"] and rise["dah"]:
            last_closed = "dit" if last_closed is None else last_closed
        elif rise["dit"]:
            last_closed = "dit"
        elif rise["dah"]:
            last_closed = "dah"

        if state == "IDLE":
            if st["dit"]:
                start_element("dit", t)
            elif st["dah"]:
                start_element("dah", t)
        if state in ("ELEMENT", "SPACE"):
            opp = "dah" if etype == "dit" else "dit"
            if rise[opp]:
                alt_latch = True
            if mode == "B" and st["dit"] and st["dah"] and t >= e_start + switchpoint * length(etype) \
                    and t < s_end:
                alt_latch = True
            if state == "SPACE" and rise[etype]:
                rep_latch = True
        process_transitions(t, inclusive=True)
    res.elements = [tuple(e) for e in res.elements]
    return res


# ---------------------------------------------------------------------------------------------
# Golden vectors of F6 (debounce) and F7 (iambic), used as known answers (note section 5.1).
# ---------------------------------------------------------------------------------------------
GOLDEN_F7 = [
    # id, dit intervals, dah intervals, mode, S, expected key-down intervals (ms)
    ("V1", [(0, 10)], [], "A", 0.5, [(0, 60)]),
    ("V1", [(0, 10)], [], "B", 0.5, [(0, 60)]),
    ("V2", [], [(0, 10)], "A", 0.5, [(0, 180)]),
    ("V3", [(0, 250)], [], "A", 0.5, [(0, 60), (120, 180), (240, 300)]),
    ("V4", [(30, 40)], [(0, 50)], "A", 0.5, [(0, 180), (240, 300)]),
    ("V5", [(0, 20)], [(15, 30)], "A", 0.5, [(0, 60), (120, 300)]),
    ("V6A", [(0, 390)], [(5, 390)], "A", 0.5, [(0, 60), (120, 300), (360, 420)]),
    ("V6B", [(0, 390)], [(5, 390)], "B", 0.0, [(0, 60), (120, 300), (360, 420), (480, 660)]),
    ("V7A", [(0, 430)], [(5, 430)], "A", 0.5, [(0, 60), (120, 300), (360, 420)]),
    ("V7B", [(0, 430)], [(5, 430)], "B", 0.0, [(0, 60), (120, 300), (360, 420), (480, 660)]),
    ("V8A", [(5, 450)], [(0, 450)], "A", 0.5, [(0, 180), (240, 300), (360, 540)]),
    ("V8B", [(5, 450)], [(0, 450)], "B", 0.0, [(0, 180), (240, 300), (360, 540), (600, 660)]),
    ("V9", [(5, 380)], [(0, 380)], "B", 0.5, [(0, 180), (240, 300), (360, 540)]),
    ("V9b", [(5, 380)], [(0, 380)], "B", 0.0, [(0, 180), (240, 300), (360, 540), (600, 660)]),
    ("V10A", [(0, 1000)], [(0, 1000)], "A", 0.5,
     [(0, 60), (120, 300), (360, 420), (480, 660), (720, 780), (840, 1020)]),
    ("V10B", [(0, 1000)], [(0, 1000)], "B", 0.0,
     [(0, 60), (120, 300), (360, 420), (480, 660), (720, 780), (840, 1020), (1080, 1140)]),
    ("V11", [(0, 10), (70, 80)], [], "A", 0.5, [(0, 60), (120, 180)]),
    ("V12", [(0, 10), (30, 40)], [], "A", 0.5, [(0, 60)]),
    ("V13", [(0, 750)], [(5, 750)], "B", 0.0,
     [(0, 60), (120, 300), (360, 420), (480, 660), (720, 780), (840, 1020)]),
]

GOLDEN_F6 = [
    # id, raw closed intervals (ms), expected confirmed events (sample, state)
    ("D1", [(0, 100)], [(1, True), (104, False)]),
    ("D2", [(0, 1), (2, 100)], [(3, True), (104, False)]),
    ("D3", [(0, 100), (102, 105)], [(1, True), (109, False)]),
    ("D4", [(0, 100), (101, 107)], [(1, True), (111, False)]),
    ("D5", [(50, 51)], []),
]


def run_golden():
    """Return a list of (id, ok, got, expected) for every F6 and F7 golden vector."""
    out = []
    for vid, div, hiv, mode, s, exp in GOLDEN_F7:
        r = simulate(mode, 20, div, hiv, 1400, switchpoint=s, debounce=False)
        got = [(int(round(a)), int(round(b))) for a, b in r.intervals_ms()]
        out.append((vid, got == exp, got, exp))
    for vid, iv, exp in GOLDEN_F6:
        db = Debouncer()
        ev = []
        for k in range(0, 200):
            before = db.state
            now = db.update(closed_at(iv, k))
            if now != before:
                ev.append((k, now))
        out.append((vid, ev == exp, ev, exp))
    return out


# ---------------------------------------------------------------------------------------------
# Squeeze study (REQ-SYS-184).
# ---------------------------------------------------------------------------------------------
def alt_pattern(first: str, k: int) -> str:
    s, t = [], first
    for _ in range(k):
        s.append("." if t == "dit" else "-")
        t = "dah" if t == "dit" else "dit"
    return "".join(s)


def both_closed_max_ms(res: KeyerResult) -> float:
    """Longest continuous interval with both debounced contacts closed (ms)."""
    ev = sorted([(k, "dit", s) for k, s in res.deb_dit] + [(k, "dah", s) for k, s in res.deb_dah])
    st = {"dit": False, "dah": False}
    since, best = None, 0.0
    for k, p, s in ev:
        st[p] = s
        both = st["dit"] and st["dah"]
        if both and since is None:
            since = k
        elif (not both) and since is not None:
            best = max(best, k - since)
            since = None
    return best


def iambic_run_script(first: str, k: int, mode: str, t1: int):
    """Operator script for an alternating run of k elements with a squeeze released at t1 (raw ms).

    The first paddle closes at raw 0 ms; the second at raw 0 ms when the run starts with a dit
    (both in one sample: dit first, F7 rule 1) or at raw 1 ms when it starts with a dah.
    Both paddles open at raw t1 (the latest-release search varies t1).
    """
    t0 = 0 if first == "dit" else 1
    if first == "dit":
        return [(0, t1)], [(t0, t1)]
    return [(t0, t1)], [(0, t1)]


def ultimatic_script(x: str, b: int, t1: int):
    """Ultimatic squeeze: paddle x closes at raw 0 ms, paddle y at raw 1 ms; both open at t1."""
    if x == "dit":
        return [(0, t1)], [(1, t1)]
    return [(1, t1)], [(0, t1)]


def element_units(pattern: str, ratio: float = 3.0):
    return [1.0 if c == "." else ratio for c in pattern]


def analytic_window_dits(kind: str, first: str, n: int, mode: str, s: float = 0.5,
                         ratio: float = 3.0):
    """Release window (debounced release instant relative to the first element start, dits).

    kind 'iambic': alternating run of n elements. kind 'ult': x then y repeated n times.
    Returns (earliest, latest): the operator's debounced release must fall in (earliest, latest].
    """
    if kind == "iambic":
        pat = alt_pattern(first, n)
    else:
        y = "." if first == "dah" else "-"
        pat = ("." if first == "dit" else "-") + y * n
    L = element_units(pat, ratio)
    starts, t = [], 0.0
    for li in L:
        starts.append(t)
        t += li + 1.0
    se = [st + li + 1.0 for st, li in zip(starts, L)]
    if kind == "iambic" and mode == "B":
        return starts[-2] + s * L[-2], starts[-1] + s * L[-1]
    return se[-2], se[-1]


def squeeze_search(kind: str, first: str, n: int, mode: str, wpm: float, s: float = 0.5,
                   ratio: float = 3.0, span_ms: int = 12):
    """Find the correct-release window by simulation near the analytic boundaries.

    Returns dict with the target pattern, earliest and latest correct raw release (ms), the
    longest debounced both-closed time among correct sendings (ms), the analytic latest
    boundary (ms, debounced), and whether a release beyond the window was shown to be wrong.
    """
    dit = dit_us(wpm) / 1000.0
    if kind == "iambic":
        target = alt_pattern(first, n)
        offset_first = 1.0  # first element starts at 1 ms (make debounce)
    else:
        y = "." if first == "dah" else "-"
        target = ("." if first == "dit" else "-") + y * n
        offset_first = 1.0
    ea, la = analytic_window_dits(kind, first, n, mode, s, ratio)
    lat_ms = offset_first + la * dit  # debounced release instant, ms
    ear_ms = offset_first + ea * dit
    total_ms = int(offset_first + (sum(element_units(target, ratio)) + len(target) + 6) * dit) + 60

    def run(t1):
        if kind == "iambic":
            dv, hv = iambic_run_script(first, n, mode, t1)
        else:
            dv, hv = ultimatic_script(first, n, t1)
        r = simulate(mode, wpm, dv, hv, total_ms, switchpoint=s, ratio=ratio)
        return r

    # debounced release = raw t1 + 4 ms (5 open samples); search raw t1 around the boundaries
    correct = []
    wrong_beyond = False
    for base in (ear_ms - 4, lat_ms - 4):
        for t1 in range(int(math.floor(base)) - span_ms, int(math.ceil(base)) + span_ms + 1):
            r = run(t1)
            ok = r.pattern() == target
            if ok:
                correct.append((t1, both_closed_max_ms(r)))
            elif t1 > lat_ms:
                wrong_beyond = True
    mid = int(round((ear_ms + lat_ms) / 2.0 - 4))
    rm = run(mid)
    mid_ok = rm.pattern() == target
    if not correct:
        return {"target": target, "ok": False}
    t1s = [c[0] for c in correct]
    return {
        "target": target,
        "ok": True,
        "mid_ok": mid_ok,
        "mid_both_ms": both_closed_max_ms(rm),
        "earliest_t1": min(t1s),
        "latest_t1": max(t1s),
        "max_both_ms": max(c[1] for c in correct),
        "analytic_latest_ms": lat_ms,
        "analytic_earliest_ms": ear_ms,
        "wrong_beyond": wrong_beyond,
    }


def runs_of_char(code: str):
    """Maximal alternating runs (length >= 2) of a Morse pattern: list of (first, length)."""
    out, i, n = [], 0, len(code)
    while i < n - 1:
        j = i
        while j + 1 < n and code[j + 1] != code[j]:
            j += 1
        if j > i:
            out.append(("dit" if code[i] == "." else "dah", j - i + 1))
            i = j
        else:
            i += 1
    return out


def identical_runs(code: str):
    """Runs of identical elements: list of (element char, length)."""
    out = []
    for c in code:
        if out and out[-1][0] == c:
            out[-1] = (c, out[-1][1] + 1)
        else:
            out.append((c, 1))
    return out


def worst_squeeze_dits(code: str, mode: str, s: float = 0.5, ratio: float = 3.0):
    """Longest both-closed interval (dits, debounce excluded) of any correct sending of a char.

    Iambic A and B: the operator squeezes over every maximal alternating run; Ultimatic: the
    previous paddle stays held over every later run of identical elements (note section 3.3).
    """
    best, where = 0.0, None
    if mode in ("A", "B"):
        for first, n in runs_of_char(code):
            ea, la = analytic_window_dits("iambic", first, n, mode, s, ratio)
            if la > best:
                best, where = la, (first, n)
    else:
        runs = identical_runs(code)
        for i in range(1, len(runs)):
            x = "dit" if runs[i - 1][0] == "." else "dah"
            ea, la = analytic_window_dits("ult", x, runs[i][1], mode, s, ratio)
            if la > best:
                best, where = la, (x, runs[i][1])
    return best, where


# ---------------------------------------------------------------------------------------------
# TX_KEY stream from text and the paddle watchdog (REQ-SYS-054).
# ---------------------------------------------------------------------------------------------
def key_stream(text: str, wpm: float, letter_space: float = 3.0, word_space: float = 7.0,
               ratio: float = 3.0):
    """Key-down intervals (us) and element types for correctly sent text.

    Tokens in angle brackets are single service signals. Spaces separate words.
    """
    dit = dit_us(wpm)
    t = 0.0
    out = []
    words = text.split()
    for wi, w in enumerate(words):
        chars = []
        i = 0
        while i < len(w):
            if w[i] == "<":
                j = w.index(">", i)
                chars.append(w[i:j + 1])
                i = j + 1
            else:
                chars.append(w[i])
                i += 1
        for ci, ch in enumerate(chars):
            code = MORSE[ch]
            for ei, c in enumerate(code):
                L = dit if c == "." else ratio * dit
                out.append((t, t + L, "dit" if c == "." else "dah"))
                t += L
                if ei < len(code) - 1:
                    t += dit
            if ci < len(chars) - 1:
                t += letter_space * dit
        if wi < len(words) - 1:
            t += word_space * dit
    return out


def gap_rule_current(dit: float) -> float:
    """REQ-SYS-054 as baselined: qualifying gap of 7 dit times or 500 ms, whichever is shorter."""
    return min(7.0 * dit, 500_000.0)


def gap_rule_proposed(dit: float) -> float:
    """Proposed (note section 6.3): qualifying gap of 2 dit times at the selected speed."""
    return 2.0 * dit


def paddle_watchdog(stream, wpm: float, gap_rule, window_s: float = 30.0, count_limit: int = 128):
    """Apply the no-gap watchdog to a key-down stream.

    Returns (max_span_s, max_count, trip_time_s or None, trip_cause). The span is the time from
    the end of the last qualifying gap (or the first element) to the end of the current element.
    The identical-element count resets on a different element or on a qualifying gap.
    """
    dit = dit_us(wpm)
    thr = gap_rule(dit)
    win = window_s * 1e6
    wstart = None
    count, prev_type = 0, None
    max_span, max_count = 0.0, 0
    trip = None
    prev_end = None
    for s, e, typ in stream:
        qualifying = prev_end is None or (s - prev_end) >= thr - 1e-6
        if qualifying:
            wstart = s
            count = 0
            prev_type = None
        if typ == prev_type:
            count += 1
        else:
            count = 1
        prev_type = typ
        span = e - wstart
        max_span = max(max_span, span)
        max_count = max(max_count, count)
        if trip is None:
            if count >= count_limit:
                trip = (e / 1e6, "count")
            elif span >= win:
                trip = (max(s, wstart + win) / 1e6, "window")
        prev_end = e
    return max_span / 1e6, max_count, (trip[0] if trip else None), (trip[1] if trip else None)


def fault_stream_alternating(wpm: float, seconds: float, ratio: float = 3.0):
    """Squeeze stream (both contacts held, Iambic A): dit dah dit dah ... with 1-dit spaces."""
    dit = dit_us(wpm)
    t, out, typ = 0.0, [], "dit"
    while t < seconds * 1e6:
        L = dit if typ == "dit" else ratio * dit
        out.append((t, t + L, typ))
        t += L + dit
        typ = "dah" if typ == "dit" else "dit"
    return out


def fault_stream_held(wpm: float, seconds: float, typ: str, ratio: float = 3.0):
    """A held lever: identical elements with 1-dit spaces."""
    dit = dit_us(wpm)
    L = dit if typ == "dit" else ratio * dit
    t, out = 0.0, []
    while t < seconds * 1e6:
        out.append((t, t + L, typ))
        t += L + dit
    return out


def stream_with_gap_every(wpm: float, seconds: float, every_s: float, gap_dits: float):
    """Alternating fault stream that has one gap of gap_dits dits every every_s seconds."""
    dit = dit_us(wpm)
    t, out, typ, next_gap = 0.0, [], "dit", every_s * 1e6
    while t < seconds * 1e6:
        L = dit if typ == "dit" else 3.0 * dit
        out.append((t, t + L, typ))
        t += L + dit
        if t >= next_gap:
            t += (gap_dits - 1.0) * dit
            next_gap += every_s * 1e6
        typ = "dah" if typ == "dit" else "dit"
    return out


# ---------------------------------------------------------------------------------------------
# Interlock (REQ-SYS-052, REQ-SW-KEYER-022) and manual-closure timeout (REQ-SYS-053,
# REQ-SW-KEYER-026).
# ---------------------------------------------------------------------------------------------
def interlock_arm_time(raw_closed_intervals_per_input, n_open: int = 500, horizon_ms: int = 5000):
    """First sample (ms) at which every used input has read open for n_open consecutive samples.

    Any closed sample of any used input restarts the count (REQ-SW-KEYER-022). None: never.
    """
    run = 0
    for k in range(horizon_ms + 1):
        closed = any(closed_at(iv, k) for iv in raw_closed_intervals_per_input)
        run = 0 if closed else run + 1
        if run >= n_open:
            return k
    return None


def manual_timeout_end(closure_ms: float, timeout_ms: float, n_make: int = 2, n_break: int = 5):
    """Key-down interval (ms) produced by one continuous manual closure starting at raw 0 ms.

    Key-down starts at the confirmed make (n_make - 1 ms) and ends at the confirmed break, or at
    the timeout measured from the confirmed make, whichever is first. Returns (end_ms, timed_out).
    """
    make = n_make - 1
    brk = closure_ms + n_break - 1
    if brk - make > timeout_ms:
        return make + timeout_ms, True
    return brk, False


# ---------------------------------------------------------------------------------------------
# Synthetic sending corpus (author-written; note section 3.4). Call signs use the N0CALL
# placeholder, never a real station.
# ---------------------------------------------------------------------------------------------
CORPUS_QSO = (
    "CQ CQ CQ DE N0CALL N0CALL K "
    "N0CALL DE N0CALL/P N0CALL/P <CT> "
    "N0CALL/P DE N0CALL GM TNX FER CALL UR RST 599 5NN 599 = NAME IS ROBIN ROBIN = "
    "QTH NR CHICAGO = HW? + N0CALL/P DE N0CALL KN "
    "R R TNX ROBIN = UR RST 579 579 = OP HERE ED ED = QTH GRID FN42AB = RIG HOMEBREW 5W "
    "ANT VERTICAL WHIP = WX SUNNY ES WARM ABT 72F = HW CPY? + N0CALL DE N0CALL/P KN "
    "FB ED TNX FER NICE QSO ES HPE CUAGN SN = 73 ES GL <SK> N0CALL/P DE N0CALL TU "
    "QRL? QRL? DE N0CALL QRZ? 1234567890 . , : ? ' - / ( ) \" = + @ ; ! "
    "<UNDERSTOOD> <ERROR> <WAIT> <SK> <CT> HH HH 55555 00000 EEEEE IIIII SSSSS"
)

# Stress tokens: the longest tokens an amateur operator plausibly sends without a word space.
CORPUS_STRESS = (
    "INTERNATIONALIZATION VE3/N0CALL/QRP 1234567890 0000000000 JUXTAPOSITION "
    "N0CALL/MM/QRP/P"
)
