# Research report: built-in keyer, straight-key and iambic-paddle interfaces

**Assignment key:** keyer. **Date:** 2026-09-25. **Author:** research agent (independent invocation). **Status:** input to SRR requirements work; not a baseline.

Owner direction relayed by the harness (verbatim intent): the radio *must support both straight keys and iambic paddles*. This report treats that as a Level-1 stakeholder need and derives candidate L2 requirements for the SW keyer module (`REQ-SW-KEY-*` candidates) and the controller/interface hardware (`REQ-CTL-*` candidates), plus the UI decisions the owner has to make.

## 1. Question

What does the built-in electronic keyer of cwht have to do, with numbers, so that a straight key, a single-lever paddle or a dual-lever iambic paddle plugged into a 3.5 mm jack "just works" at first power-on: jack conventions, key-type selection or auto-detection, iambic A/B semantics (Curtis heritage), PARIS element timing, weighting/ratio/compensation, speed range and adjustment UX, contact debounce, sidetone norms, QSK/semi-break-in/hang timing, keying envelope shaping to avoid clicks, ESD and abuse-voltage protection of the key inputs, and which open-source implementations (K3NG, OpenCW Keyer, YACK, WinKeyer protocol) are worth using as references.

## 2. Method

1. Read the charter `docs/process/00-charter.md` sections 1, 9 and 11 (Class A rigor, V&V classes Analysis / HostUnit / Emulation / Inspection / Bench / OnAir, "evidence not assertion").
2. Web search and fetch of primary sources: Curtis 8044 application note (1992), K1EL WinKeyer3 IC datasheet rev 1.3 (2019) and WKUSB Rev C manual v1.4 (2023), Elecraft KX2 owner's manual rev A8 and KX3 straight-key operating note, Icom IC-705 basic and advanced manuals, QRP Labs QCX (fw 1.07) and QMX (fw 1.02) operating manuals, Ultra PicoKeyer manual (fw 2.2), K3NG keyer wiki and `keyer_settings.h`, YACK manual, ITU-R M.1677-1, 47 CFR 97.307 and 97.119 (LII mirror because ecfr.gov redirected the fetcher), RP2350 datasheet (electrical tables and erratum RP2350-E9), Ganssle debouncing study, W8JI and IVARC key-click papers, Nexperia PESD3V3L2BT page.
3. PDFs that the fetcher returned as binary were converted locally with `pdftotext -layout` into the session scratchpad and grepped; quotations below come from that text. The RP2350 datasheet (7.9 MB) and the IC-705 advanced manual (31 MB) were downloaded with `curl` into the scratchpad only.
4. Timing table computed locally (command and output):

```
$ python3 - <<'EOF'
for w in (5,10,13,15,18,20,25,30,35,40,45,50,60):
    d=1200.0/w; print(w, round(d,1), round(3*d,1), round(7*d,1), round(8*d,1), round(6.1*d,1), round(100*10/d,1), round(100*3/d,1))
EOF
WPM  dit_ms  dah_ms  word_sp  hang8dit_ms  hang6.1dit_ms  5ms_ramp_pct_of_dit  3ms_debounce_pct_of_dit
  5   240.0   720.0   1680.0      1920.0         1464.0                  4.2                     1.2
 10   120.0   360.0    840.0       960.0          732.0                  8.3                     2.5
 13    92.3   276.9    646.2       738.5          563.1                 10.8                     3.2
 15    80.0   240.0    560.0       640.0          488.0                 12.5                     3.8
 20    60.0   180.0    420.0       480.0          366.0                 16.7                     5.0
 25    48.0   144.0    336.0       384.0          292.8                 20.8                     6.2
 30    40.0   120.0    280.0       320.0          244.0                 25.0                     7.5
 40    30.0    90.0    210.0       240.0          183.0                 33.3                    10.0
 50    24.0    72.0    168.0       192.0          146.4                 41.7                    12.5
 60    20.0    60.0    140.0       160.0          122.0                 50.0                    15.0
Pull-up current when contact closed, 3.3 V: 4.7k -> 0.70 mA, 8.2k -> 0.40 mA, 10k -> 0.33 mA
Contact-closed pad voltage with 100 ohm contact and 4.7k pull-up: 0.069 V (VIL max 0.8 V)
TVS clamp 26 V through 1k series: transient pad current approx 22.7 mA
```
("5ms_ramp_pct_of_dit" is rise plus fall, 10 ms total, as a fraction of one dit.)

## 3. Findings

### F1. Jack and plug conventions (3.5 mm TRS)

- De facto convention for paddles: dit on the tip, dah on the ring, common on the sleeve. DX Engineering: "Thumb paddle contact for 'dit' to the stereo plug Tip, the index finger paddle contact for 'dah' goes to the plug Ring, and the base or common is connected to the Sleeve". Straight keys and bugs are "Usually wired Tip to insulated contact and Sleeve to the base common (ground), with no connection to Ring on 3-conductor radios". Source: https://dxengineering.wordpress.com/2016/09/01/tech-tip-hooking-up-a-keyer-paddle/
- Hermes Lite 2 Plus documents the same: "Tip = Dot, Ring = Dash, Sleeve = Ground". Source: https://www.hermeslite2plus.com/p/using-straight-key-or-external-keyer.html
- Elecraft KX2 manual: "KEY Jack: This jack can be used with any hand key, keyer paddle, or other keying device, as configured by the CW KEY1 menu entry. A stereo plug is required at the KEY jack, even if only the tip contact is being used." Menu `CW KEY1 TIP=DOT` "Specifies whether the left keyer paddle (tip contact on the KEY jack) is DOT or DASH. A third selection, HAND, allows either tip or ring to function as a hand key, or as an input for an external keying device (keyer, computer, etc.)." Source: https://ftp.elecraft.com/KX2/Manuals%20Downloads/E740282%20-%20KX2%20Owner's%20Man%20A8.pdf
- The mono-plug trap is documented by two vendors. Elecraft KX3 note: "Attempting to use a Mono 1/8" plug will result in the rig going into 'Key Down' mode with the transmitter being engaged if VOX is turned on." Source: https://ftp.elecraft.com/KX3/Mod%20Notes%20Alerts/Using%20a%20Straight%20Key%20with%20the%20KX3.pdf. QRP Labs QCX menu 4.10 "Strght mode" (tip / ring / both): "If a 3.5mm mono plug was used with the QCX+, the longer ground barrel shorted the ring to ground causing continuous keying. This configuration menu is the solution to that problem." Source: https://qrp-labs.com/images/qcxp/firmware/1.07/OpMan107.pdf (same text in the QMX manual, https://qrp-labs.com/images/qmx/manuals/operation_1_02_002.pdf).
- Consequence: a TS (mono) plug in a TRS jack grounds the dah line permanently. In iambic mode that is a continuous string of dahs; in a naive straight-key mode wired to "either contact" it is continuous key-down. This is a hazard (unintended transmission), not just an annoyance.

### F2. How existing radios select the key type (menu, shortcut, or auto-detect)

- Menu only: Elecraft KX2 `CW KEY1` = TIP=DOT / TIP=DASH / HAND (source F1). Icom IC-705 `Key Type` = "Straight, Bug, or Paddle" (default Paddle), with the note "When using an external Elec-keyer, select 'Straight.'", plus `Paddle Polarity` Normal ("Right = dash, Left = dot") or Reverse. Source: IC-705 Advanced Manual, https://icomuk.co.uk/files/icom/PDF/advancedManuals/IC-705_ENG_Advanced_1a.pdf (CW-KEY SET). uSDX menu 2.6 "Type of keyer (Iambic-A, -B, Straight)" and 2.7 swap. Source: https://raw.githubusercontent.com/threeme3/usdx/master/README.md
- Menu plus a speed shortcut: QCX/QMX keyer mode list is Straight / IAMBIC A / IAMBIC B / Ultimatic, `Keyer swap` YES/NO, and "Setting speed to 0 enables 'Straight' Key mode regardless of the keyer mode setting; this is useful for quickly being able to key down for antenna tuning purposes ... The normal configured keyer mode is automatically restored when you increase the speed above zero." (QCX §3.2, QMX §4.5).
- Automatic detection (the only primary example found): Ultra PicoKeyer: "During its power-on program, the PicoKeyer checks to see if either paddle input is grounded. If one input is shorted, the other input is assumed to be a straight key. This way you can plug in a straight key wired to a mono plug and use it without any changes or adjustments." Re-scan on demand: "press buttons 2 and 3 ... you will hear 'P' if a paddle or no key is detected, or 'K' if a straight key is detected". Its FAQ documents the failure mode when detection is skipped: "Q: When I plug in a straight key, I just get dashes!". Source: https://wd8rif.com/radio_manuals/pdf/Ultra-PicoKeyer-20170127.pdf
- K3NG: straight-key pass-through by holding the right paddle during startup, or a separate straight-key input "in parallel with paddle operation". Source: https://github.com/k3ng/k3ng_cw_keyer/wiki/400-Operating-Modes
- KX3 note also documents the "cootie"/sideswiper option: `CW KEY2 = HAND` makes "both the left and right paddles ... function like a hand key", "similar to the well-known Sideswiper or Cootie keying technique".
- Plug-detection precedent for safety: QMX "GPS protection: If QMX detects a GPS receiver has been plugged into the paddle port, it will automatically set up a temporary 'Practice mode' ... so that the radio is not" keyed by the GPS serial data.

### F3. Iambic mode A vs mode B, memories, switchpoint (Curtis heritage)

- Curtis 8044 application note (1992): mode A is "the original Curtis method"; "In the original Curtis method, when a squeeze is released, the element underway is completed and nothing else follows." Mode B: "In type 'B' iambic, a squeeze released during an element (dot or dash) will cause another alternate element to follow the one being produced." Timing consequence: "The window for action on the 'B' type is one-half that on the 'A' type." Lineage: "Keyers such as the AccuKeyer, AEA, Heath, Nye, MFJ memory keyer and Ten-Tec use method 'B'. Of course, all keyers using the Curtis original 8044 are type 'A'. About 80-90% of Curtis consumer sales are type 'A'". The 8044ABM (20-pin, 1986) made A/B switchable. "Dot memory is absolutely essential in any serious electronic keyer" and "For true iambic operation, both dot and dash memories are required". Self-completing elements and non-shortening spaces are also required. Source: https://users.ox.ac.uk/~malcolm/radio/8044print.pdf
- WinKeyer3 states the same semantics compactly: "In either iambic mode, alternating dits and dahs are sent while both paddles are held closed. In mode B an extra alternate dit or dah is sent after both paddles are released. In Ultimatic mode when both paddles are pressed the keyer will send a continuous stream of whichever paddle was last pressed." Bug mode: "WK3 sends the dits and you manually send the dahs. You also can use bug mode to operate in straight key mode or if you want to key through WK3 with a different keyer, simply set bug mode and use the dah input to key WK3." Source: WK3 datasheet rev 1.3 (mirrored at https://www.k1elsystems.com/files/WK3_Datasheet_v1.3.pdf).
- Paddle switchpoint (the tunable that decides how early a paddle press is latched into memory): WK3 `Set Paddle Switchpoint <12><nn>`, 10..90 %, default 50; "controls when WK3 will start looking for a new paddle press after sensing the current one. If there is not enough delay, the keyer could send unwanted dits or dahs. If there is too much delay, the operator is held back"; `DELAY_TIME = (SWITCHPOINT x DIT_TIME)/50`; "If the paddle sensitivity is set to zero, dit and dah paddle memory is disabled." K3NG's equivalent is "CMOS Super Keyer Iambic B Timing": "Setting the timing percent to 0 (zero) is essentially pure Iambic B and 100 is pure Iambic A." Source: WK3 datasheet; https://github.com/k3ng/k3ng_cw_keyer/wiki/400-Operating-Modes
- Defaults differ across vendors: KX2 default A ("a little more forgiving for first-time operators"; both modes "provide dot- and dash-memories"); QMX default Iambic A; WKUSB and YACK default Iambic B ("Iambic B is the most often used so that is the default", WKUSB manual). Ultimatic: invented 1955 by W6SRY, "last paddle pressed wins" (https://morsecode.world/iambic.html, secondary). WK3 PINCFG adds Ultimatic dit- or dah-priority variants.

### F4. Element timing standard and PARIS speed

- ITU-R M.1677-1 (10/2009) §2 "Spacing and length of the signals": "2.1 A dash is equal to three dots. 2.2 The space between the signals forming the same letter is equal to one dot. 2.3 The space between two letters is equal to three dots. 2.4 The space between two words is equal to seven dots." Source: https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
- PARIS convention: "PARIS " is 50 dot units, so dit(ms) = 1200 / WPM. QMX manual: "a standard Morse dit length is defined as 1200 / Keyer Speed where Keyer speed is in Words Per Minute (wpm) and the resulting dit length is in milliseconds." Secondary explainer: https://morsecode.world/international/timing/ . Table in §2 gives 240 ms at 5 WPM down to 20 ms at 60 WPM.
- Regulatory timing constraint on automatic sending: 47 CFR 97.119(b)(1) "By a CW emission. When keyed by an automatic device used only for identification, the speed must not exceed 20 words per minute." and 97.119(a) ID "at the end of each communication, and at least every 10 minutes during a communication." Source: https://www.law.cornell.edu/cfr/text/47/97.119

### F5. Weighting, ratio, compensation, spacing options (definitions and ranges in the field)

- WinKeyer3 (host command set, exact ranges): `Set WPM Speed <02>` 5..99 WPM; `Set Weighting <03>` 10..90 %, 50 = none, "any increase in keyed time is subtracted from spacing time" so speed is unchanged, "Since weighting tracks speed, a given weighting will sound the same at all speeds"; `Set Dit/Dah Ratio <17>` 33..66 with `DAH/DIT = 3*(nn/50)` (33 = 2:1, 66 = 4:1), "Any value other than 50 causes distortion of the Morse waveform"; `Set Key Comp <11>` 0..250 ms fixed addition to every element (speed independent, for T/R systems that shorten elements); `Set 1 Extension <10>` 0..250 ms added to the first element after a T/R changeover, "usually only a noticeable problem at higher CW speeds >25 WPM"; Autospace ("If you pause for more than one dit time between a dit or dah, WK3 will interpret this as a letter-space"); Contest spacing (6-dit word space); Letterspace 0..62 % of a word space; Paddle watchdog "disables the key output after 128 consecutive dits or dahs ... Sidetone remains on to alert the user." Source: WK3 datasheet rev 1.3; WKUSB Rev C manual v1.4 App. D, https://www.k1elsystems.com/files/WKUSB_Manual_C_R00.pdf
- K3NG defaults (`keyer_settings.h`): `initial_speed_wpm 26`, `wpm_limit_low 5`, `wpm_limit_high 60`, `initial_sidetone_freq 600`, `sidetone_hz_limit_low 299`, `sidetone_hz_limit_high 2001`, `initial_dah_to_dit_ratio 300`, `default_weighting 50`, `initial_ptt_lead_time_tx1 0`, `initial_ptt_tail_time_tx1 10`, `default_ptt_hang_time_wordspace_units 0.0`, `default_keying_compensation 0`, `default_first_extension_time 0`, `default_length_wordspace 7`. Source: https://raw.githubusercontent.com/k3ng/k3ng_cw_keyer/master/k3ng_keyer/keyer_settings.h ; https://github.com/k3ng/k3ng_cw_keyer/wiki/410-Timing-Adjustments
- QCX/QMX `Keyer Weight` 050..950 (5 to 95 %), default 500 = 50 % duty of a dit stream; lengthening dit and dah "by the SAME amount" and taking it from the gaps; "The keyer speed is unchanged by altering the weight parameter."
- Icom IC-705 `Dot/Dash Ratio` "1:1:2.8 ~ 1:1:4.5 in 0.1 steps", default 1:1:3.0. KX2 `CW WGHT` default 1.25 ("element/space timing ratio").
- Curtis note warns about a weight control "turned to maximum and forgotten" and observes weighting helps below about 15 WPM and hurts above 20 WPM; the 8044's 3:1 ratio was fixed in silicon.

### F6. Speed ranges and adjustment UX

- Ranges in shipping products: WK3 5..99 WPM; K3NG 1..999 (build limits 5..60); Icom IC-705 "6 and 48 Words Per Minute" (Basic manual p. 44, https://www.manualslib.com/manual/1875929/Icom-Ic-705.html?page=44); Ultra PicoKeyer 5..60 with a pot window (default 5..30) and "Dual-Set Speed"; uSDX 1..35; QCX/QMX default 12; YACK default 12 WPM. Curtis: "Normally about 6 to 50 wpm", "Most commercial keyers are made to go to 50 wpm."
- UX patterns: KX2 dedicates a knob ("In CW mode, KYR-SPT/MIC sets the keyer speed (in WPM)"); QCX/QMX use one click of Select to show "Speed 12" then the rotary encoder, and the radio stays operable while the speed screen is up; YACK uses command-key plus paddles (dit down, dah up); PicoKeyer announces speed in sidetone Morse. QCX/QMX speed 0 = straight-key tune shortcut (F2).
- Practice/spot: KX2 PTT-CW ("hitting the key without first tapping XMIT will generate only a sidetone. This is useful for code practice or keyer speed adjustment"); QCX/QMX Practice mode shows "P" on the LCD and "never sends any RF power to the antenna"; IC-705 lets you hear sidetone with break-in OFF.

### F7. Contact bounce and debounce

- Curtis: "All mechanical switches, with the exception of the mercury type, will bounce slightly on both make and break ... The result is unwanted elements and can render an otherwise good design worthless." "The bounce is usually on the order of 5-10 milliseconds. While this may seem short, it begins to approach the length of a dot at high speeds. Dot length, at 50 wpm, is only 24 ms. The debouncing must not be so sluggish that it slows an operator trying to send at high speeds." The 8044 used 1 MΩ / 0.01 µF RC filters on the paddle lines.
- Ganssle measured 18 switches: average bounce 1557 µs, maximum 6200 µs (two outliers: 157 ms on opening, 11.3 ms to close); "Assume things are worse than shown". Part 2 recommends a timer tick of "One to five msec" for the debouncer and a UI-button debounce of "20 to 50 msec", which is far too slow for a paddle (at 40 WPM a 20 ms debounce is 67 % of a dit). Sources: https://www.ganssle.com/debouncing.htm , https://www.ganssle.com/debouncing-pt2.htm
- Practical conclusion (derived): a keyer does not need a long debounce because the element engine already ignores paddle chatter while an element is in progress; what matters is (a) a short glitch filter of 2 to 5 ms on each contact at 1 kHz or faster sampling, and (b) the WK3-style switchpoint lockout that stops looking for a "new" press for a fraction of a dit after one is sensed. Straight-key mode has no element engine, so it needs a slightly longer filter (default 5 ms, well under the 48 ms dit at 25 WPM).

### F8. Sidetone norms

- KX2: `PITCH 0.60` kHz default, "500-700 Hz is typically used with headphones", level via MON, and "This is also the pitch of CW signals when centered in the receiver's passband."
- Icom IC-705: "set the CW pitch to between 300 and 900 Hz (in 5 Hz steps)"; `Side Tone Level` 0..100 %, plus a `Side Tone Level Limit` ON/OFF.
- QCX/QMX: default 700 Hz, minimum 350 Hz, volume 0..99 (QCX) or 0..? default 70 with `Sidetone abs/rel` (QMX: Relative tracks the main volume, Absolute is fixed); "It is strongly recommended to leave the Sidetone frequency set to the same frequency as the CW Offset frequency ... When you transmit you will also be netted accurately to his frequency." QCX also documents that the sidetone injection must not shift the audio DC bias, otherwise a click is heard at RX/TX changeover.
- K3NG default 600 Hz (limits 299..2001); YACK default 800 Hz; WK3 500..4000 Hz (`62500/frequency`), with "paddle only sidetone" option.
- Norm for cwht: 600 to 700 Hz default, 300 to 1000 Hz adjustable, tied to the receiver's CW offset so that zero-beat equals netting.

### F9. Break-in: full QSK, semi break-in, hang time, PTT lead/tail

- QCX/QMX: Full QSK: "after the delay time for RF envelope shaping, the Transmit/Receive switch is set to 'Receive' shortly after key-up." Semi QSK delay options: "Auto: Delay is set to 8 dit lengths automatically ... slightly longer than the standard 7 dits length of an inter-word spacing"; "Contest: Delay is set to 6.1 dit lengths ... slightly longer than the 6 dit length inter-word spacing used in N1MM logger software"; Custom dits / decidits / ms; "in all cases, the delay is constrained to the range 1-999 milliseconds." QMX also has `PTT to TX delay` (ms) and a `TX->RX hang time` (display only).
- WinKeyer3: PTT `Lead-In` 0..250 ms in 10 ms steps ("PTT will be asserted first and then, after the Lead-In delay expires, the key output will be asserted"); `Tail` for machine-sent CW: `Tail Delay = Three Dit Times + (Tail Setting x 10 ms)`; for paddle-sent CW a speed-proportional `Hang Time` in PINCFG: "00 Wait 1 wordspace + 1 dit / 01 + 2 dits / 10 + 4 dits / 11 + 8 dits before ending paddle insertion"; rationale: a fixed tail "will hold too long after keying stops" at higher speed and "drop out between letters at a slower speed".
- K3NG: PTT lead (ms), tail (ms, automatic sending) and hang time in word-space units (paddle sending); "if you activate PTT lead time, you should activate tail time as well, otherwise PTT lead time will be invoked before each dit or dah, significantly slowing down the sending speed." Source: https://github.com/k3ng/k3ng_cw_keyer/wiki/225-Sidetone,-PTT,-and-TX-Key-Lines
- Elecraft KX2: `VOX DLY 0.00 (CW)` "recovery time from transmit to receive ... the default delay (0.00) also turns on the QSK icon, indicating the fastest possible break-in"; `TX DLY NOR 005` "Varies the delay in milliseconds between key-down and RF output ... NOR (5 ms) is recommended in most cases. A delay of up to 20 ms can be set, but use the smallest delay possible since longer delays can add some timing variation in CW mode at higher code speeds."
- Icom IC-705: semi break-in returns to receive "after a preset time after you stop keying" (rotary setting); full break-in "immediately returns to receive after keying up". (Numeric BK-IN delay range was not present in the text layer of the advanced manual; see Open items.)

### F10. Keying envelope, key clicks, regulatory basis

- 47 CFR 97.307(a): "No amateur station transmission shall occupy more bandwidth than necessary for the information rate and emission type being transmitted, in accordance with good amateur practice." (b): "Emissions outside the necessary bandwidth must not cause splatter or keyclick interference to operations on adjacent frequencies." (e) for 30-225 MHz: spurious "at least 60 dB below the mean power of the fundamental. For a transmitter having a mean power of 25 W or less, the mean power of any spurious emission supplied to the antenna transmission line must not exceed 25 µW and must be at least 40 dB below". Source: https://www.law.cornell.edu/cfr/text/47/97.307
- ARRL guidance as reported: "The ARRL recommends a 5 mS rise and 5 mS fall time for CW" (W8JI, https://www.w8ji.com/what_causes_clicks.htm); IVARC paper citing the ARRL Handbook: "for a keying speed of 30wpm on a communications circuit with fading, a rise time of about 5ms is adequate and that for a good, non-fading circuit, 10ms is satisfactory." W8JI: rise times faster than "2 or 3 milliseconds will cause a bandwidth problem"; shape matters: rectangular worst, single-pole RC better, "multi-pole filtered ... sine-shaped or raised-cosine" best.
- IVARC calculations (30 WPM dot stream, -60 dB bandwidth criterion): square keying reaches -60 dB only at about 12.5 kHz (25 kHz bandwidth); a 5 ms linear ramp improves by 20 dB at 500 Hz; a raised cosine whose maximum slope equals the 5 ms ramp "is reached at just under 300Hz, giving a transmitted bandwidth of 600Hz"; a 4-pole "transitional Gaussian to 6dB" low-pass (f3dB = 70 Hz) approximating the raised cosine gives "below -60dB above 230Hz, which gives a transmitted bandwidth of 460Hz"; at 20 WPM or less the shaping filter can be slowed to about 35 Hz. Source: http://www.ivarc.org.uk/uploads/1/2/3/8/12380834/keyclicks_version_1.pdf
- Field practice: Icom IC-705 `Rise Time` "2, 4, 6, or 8 milliseconds", default 4 ms. Elecraft KX2 key-down to RF delay 5 ms nominal (F9).
- Speed interaction (computed): a 5 ms rise plus 5 ms fall is 17 % of a dit at 20 WPM, 33 % at 40 WPM and 50 % at 60 WPM; above about 40 WPM the envelope shape starts to define the element, which is the argument for a speed-adaptive shaper (longer at slow speed, never below 4 ms).

### F11. Key inputs on the RP2350: electrical facts, erratum E9, ESD

- RP2350 datasheet (Bank 0 GPIO are "Digital IO (FT) ... These pins have enhanced ESD protection"): absolute maximum `VPIN_FT` at IOVDD = 3.3 V is -0.5 V to +5.5 V ("IOVDD must be present"); standard pins -0.5 to IOVDD + 0.5 V. ESD: HBM 2 kV (all pins), 4 kV "Digital (FT) pins only", CDM 500 V. DC thresholds at 3.3 V: VIH min 2.0 V, VIL max 0.8 V, Schmitt hysteresis 0.2 V. Internal pull-up 32..86 kΩ, pull-down 36..113 kΩ at 3.3 V. Source: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf (§14.9.1, 14.9.2, DC characteristics; erratum RP2350-E9).
- Erratum RP2350-E9 (affects A2): "Increased leakage current on Bank 0 GPIO when pad input is enabled" when the pad is "somewhere between VIL and VIH", "typically around 120μA", holding the pad "at around 2.2 V"; "The pad pull-down (if enabled) is significantly weaker than the leakage current"; "Driving / pulling the pad input low with a low impedance source of 8.2 kΩ or less will overcome the erroneous leakage"; "The pad pull-up still works." A key input is a switch to ground with a pull-up, so it is on the safe side of E9, but a slow RC edge through the undefined region will source 120 µA, and any design relying on internal pull-downs is affected. Raspberry Pi's A4 stepping (Product Change Note 2025-07-29) fixes E9; software can read `CHIP_ID.REVISION`. Source: https://hackaday.com/2025/07/31/raspberry-pi-rp2350-a4-stepping-addresses-e9-current-leakage-bug/ and https://hackaday.com/2024/09/20/raspberry-pi-rp2350-e9-erratum-redefined-as-input-mode-leakage-current/
- Curtis on paddle-line protection (CMOS inputs): "We now believe the series resistors in the paddle and manual key lines are the best form of static discharge protection. For maximum protection, series resistors of from 470 Ohms to 1K added to the dot, dash and manual key input lines are now recommended to limit input currents from external voltages." External silicon diodes "provide no protection" next to the internal ones (lower-Vf devices or series resistance are needed).
- Off-the-shelf ESD parts: Nexperia PESD3V3L2BT (SOT23, two bidirectional lines): "IEC 61000-4-2, level 4 (ESD)", "ESD protection up to 30 kV", "IRM = 90 nA", "VCL = 26 V", PPPM 350 W. IEC 61000-4-2 level 4 is 8 kV contact / 15 kV air. Source: https://www.nexperia.com/product/PESD3V3L2BT , https://en.wikipedia.org/wiki/IEC_61000-4-2 . A 26 V clamp through a 1 kΩ series resistor limits the pad transient to about 23 mA, which the internal FT-pad diodes absorb; a lower-clamp TVS or a series resistor is mandatory either way (computed in §2).
- External keying devices seen on this jack: passive key contacts; keyer outputs that are open-collector/MOSFET switches to ground (WK3 "high true TTL" key outputs are the exception and would need a level adapter; PicoKeyer "Dual MOSFET keying circuit will key transmitters up to 60 V, positive or negative"). A 3.3 V pull-up of 4.7 to 8.2 kΩ (0.4 to 0.7 mA closed) sinks correctly through any of them; a 100 Ω dirty contact still reads 0.07 V (computed).

### F12. Open-source references worth reusing (behaviour, not code)

- K3NG Arduino CW Keyer, GPL v3 ("GNU General Public License ... version 3 of the License, or (at your option) any later version", `k3ng_keyer.ino` header). Feature set: "Iambic A and B modes", single lever paddle mode, "Straight key support", "Ultimatic mode", "Bug mode", "CMOS Super Keyer Iambic B Timing", "Paddle reverse", "CW speed adjustable from 1 to 999 WPM", "Dah to Dit Ratio adjustment", weighting, keying compensation, first extension, "Autospace", "Optional PTT outputs with configurable lead, tail, and hang times", "Adjustable frequency sidetone", "K1EL Winkey 1.0 and 2.0 interface" emulation, memories. Sources: https://github.com/k3ng/k3ng_cw_keyer , https://github.com/k3ng/k3ng_cw_keyer/wiki
- OpenCW Keyer MK2 / MK3 (OK1CDJ): open hardware around K3NG firmware; MK3 is based on the Seeed XIAO RP2040, so it is a directly comparable RP2 keyer platform. Source: https://github.com/ok1cdj/OpenCWKeyerMK2
- YACK "Yet Another CW Keyer" (DK3LJ, ATtiny45, 4 kB flash): modes IAMBIC A, IAMBIC B (default), Ultimatic, "DAH Priority"; default 12 WPM, 800 Hz sidetone; speed by command key plus paddles. A compact state machine that is a good model for a `no_std` Rust port. Source: https://yack.sourceforge.net/
- WinKeyer3 host protocol (K1EL): command bytes 0x00..0x1F (`<00>` Admin, `<01>` sidetone, `<02>` speed, `<03>` weight, `<04>` PTT lead/tail, `<05>` speed pot, `<09>` PINCFG, `<0B>` key immediate, `<0E>` mode register with bits for paddle watchdog, paddle echo, key mode 00=B 01=A 10=Ultimatic 11=Bug, paddle swap, serial echo, autospace, contest spacing; `<10>` first extension, `<11>` key comp, `<12>` switchpoint, `<14>` software paddle, `<15>` status, `<17>` ratio, buffered `<18>`..`<1F>`). Supported by mainstream logging software (N1MM+, fldigi, HRD, AC Log per the WKUSB manual). Source: WK3 datasheet rev 1.3.
- Rust: `radio-utils-keyer` crate exists (https://docs.rs/radio-utils-keyer/latest/radio_utils_keyer/); other RP2040 keyers found are MicroPython/CircuitPython (ukagit/iambic-keyer, xiaoKey). Not evaluated for quality; treat as reading material only.

## 4. Implications for cwht

Tags: **REQ-candidate** (proposed L2 requirement text with numbers), **RISK-candidate**, **DECISION-needed** (owner UI/design choice), **ACTION** (work to do). Verification method suggested in brackets per charter §9.

### 4.1 Interface (CTL) candidates

1. **REQ-candidate CTL-KEY-01 Jack.** The KEY jack shall be a 3.5 mm 3-conductor (TRS) jack wired tip = dit/hand-key, ring = dah, sleeve = signal ground, matching F1. [Inspection]
2. **REQ-candidate CTL-KEY-02 Two independent inputs.** Tip and ring shall be sensed as two independent logic inputs so that simultaneous closure (squeeze) is observable; each input shall be sampled at >= 1 kHz or edge-timestamped with <= 1 ms resolution. [HostUnit + Bench]
3. **REQ-candidate CTL-KEY-03 Contact sensing.** Each input shall register closed at a contact resistance <= 500 Ω and open at >= 100 kΩ, using an external pull-up of 4.7 to 8.2 kΩ to 3.3 V (erratum E9 bound, F11) with the RP2350 Schmitt input enabled; closed-contact current <= 0.8 mA per input. [Analysis + Bench]
4. **REQ-candidate CTL-KEY-04 Abuse and ESD protection.** Each key input shall withstand IEC 61000-4-2 level 4 discharges (8 kV contact, 15 kV air) at the jack and continuous applied voltages of at least -5 V to +12 V (owner to confirm) without damage, via series resistance >= 1 kΩ plus a TVS/clamp, so that pad voltage stays within -0.5 V to +5.5 V (RP2350 FT absolute maximum). [Analysis + Inspection; Bench with ESD gun only if available]
5. **REQ-candidate CTL-KEY-05 RF immunity.** Key inputs shall not produce a false state change while the transmitter delivers 5 W at 144 MHz into the antenna with a 1 m unshielded key cable attached (RC low-pass >= 10 µs on each input and ferrite if needed). [Bench: memory-sent CW while monitoring inputs]
6. **REQ-candidate CTL-KEY-06 Cross-plugging survivability.** Both 3.5 mm jacks (key and headphones) shall survive a key plugged into the headphone jack (output shorted to ground indefinitely) and headphones or an audio source plugged into the key jack (AC into the key input) without damage or unintended transmission. [Analysis + Bench] **RISK-candidate:** identical connectors on a pocket radio make this likely in the field.
7. **REQ-candidate CTL-KEY-07 Independent key-down watchdog.** A hardware or independent-timer mechanism shall remove PA drive if a key-down condition persists longer than T_max (owner: 10 to 60 s; the QCX tune use-case needs several seconds) irrespective of firmware state (SWE-134 provision for keying). [Emulation + Bench]
8. **REQ-candidate CTL-KEY-08 Key envelope actuator.** The hardware shall accept a firmware-generated amplitude envelope (DAC or filtered PWM to the PA driver/bias) capable of a 2 to 10 ms raised-cosine rise and fall, rather than a hard on/off key line. [Analysis (LTspice) + Bench]

### 4.2 Software (SW-KEY) candidates

9. **REQ-candidate SW-KEY-01 Key types.** The keyer shall provide the modes Straight (hand key or external keyer on tip; options tip / ring / both), Iambic A, Iambic B, Ultimatic, and Bug, plus a paddle-swap option, with dit and dah memories in the iambic modes (F2, F3). [HostUnit with golden paddle-sequence vectors; Demonstration]
10. **REQ-candidate SW-KEY-02 Element timing.** With speed S in WPM, dit = 1200/S ms, dah = 3 dits, intra-character space = 1 dit, inter-character space = 3 dits, inter-word space = 7 dits (ITU-R M.1677-1 §2, PARIS), each element and space accurate to within +/-1 ms or +/-2 % of a dit, whichever is larger, at every supported speed. [HostUnit + Emulation (timestamped key line)]
11. **REQ-candidate SW-KEY-03 Speed.** Speed adjustable from 5 to 50 WPM in 1 WPM steps (owner may extend to 60), default 15 to 20 WPM, stored non-volatile, changeable while sending; the current WPM shall be visible on the LCD while adjusting. [Demonstration]
12. **REQ-candidate SW-KEY-04 Mode A/B semantics.** In Iambic A, releasing both paddles completes the element in progress and sends nothing more; in Iambic B, if the opposite paddle was pressed during the current element (after the switchpoint), one alternate element follows the release (F3). Switchpoint adjustable 10 to 90 % of a dit, default 50 %. [HostUnit; the test vectors for "N", "C", "period", "AR" from the Curtis note]
13. **REQ-candidate SW-KEY-05 Weighting and ratio.** Weighting adjustable 25 to 75 % (default 50, no change to overall speed), dah:dit ratio adjustable 2.5:1 to 4.0:1 in 0.1 steps (default 3.0), keying compensation 0 to 25 ms (default 0), first-element extension 0 to 25 ms (default 0); autospace and contest (6-dit) spacing optional. Ranges are deliberately narrower than WK3/K3NG (F5) to avoid the Curtis "forgotten weight" failure; a non-default weight/ratio shall be indicated on the display. [HostUnit]
14. **REQ-candidate SW-KEY-06 Debounce.** Each paddle contact shall be filtered so that a state change is accepted only after 3 consecutive identical 1 ms samples (3 ms), configurable 1 to 10 ms, and the keyer shall ignore re-closures of the same contact within the switchpoint lockout; in Straight mode the filter default is 5 ms (1 to 20 ms). The filter shall never exceed 25 % of a dit at the maximum speed (F7). [HostUnit with injected bounce patterns of 0.1 to 10 ms]
15. **REQ-candidate SW-KEY-07 Sidetone.** Sidetone frequency 300 to 1000 Hz in 10 Hz steps, default equal to the receiver CW offset (600 or 700 Hz, DECISION), level 0 to 99 with Relative/Absolute behaviour relative to the main volume, onset within 1 ms of key-down, with a 3 to 5 ms audio envelope and no DC step (no click). Sidetone-only Practice mode shall exist and be indicated on the LCD (F6, F8). [HostUnit + Bench]
16. **REQ-candidate SW-KEY-08 Break-in.** Full QSK: receiver re-enabled within 1 dit at the current speed after the RF envelope has decayed; Semi break-in: hang time selectable Auto = 8 dits, Contest = 6.1 dits, or custom 1 to 999 ms; PTT/T-R lead-in 0 to 50 ms (default per PA switching analysis) and key-down-to-RF delay <= 5 ms (F9). [Emulation + Bench with oscilloscope on key, T/R and RF envelope]
17. **REQ-candidate SW-KEY-09 Envelope.** RF rise and fall shaped as a raised cosine (or 4-pole Gaussian-to-6 dB equivalent) with 10-90 % time of 5 ms +/-1 ms at speeds >= 25 WPM; the shaping may lengthen to 8 ms below 15 WPM (DECISION). Keying sidebands of a 30 WPM dit stream shall be <= -60 dBc at |offset| >= 500 Hz (IVARC figures give 300 to 230 Hz for ideal shapes, so 500 Hz leaves margin for the PA) (F10; 97.307(a),(b)). [Analysis (FFT of modelled envelope) + Bench with SDR receiver]
18. **REQ-candidate SW-KEY-10 Safety interlocks.** (a) If any key input is closed at power-on, the keyer shall not transmit and shall show a "key closed / check plug" message until both inputs have been seen open (mitigates the mono-plug hazard, F1); (b) a paddle watchdog shall stop transmission after 128 consecutive identical elements while keeping sidetone (WK3 pattern), and Straight mode shall stop after T_max (shared with CTL-KEY-07); (c) any automatic message or CW ID shall be limited to 20 WPM when used for identification (97.119(b)(1)). [HostUnit + Emulation]
19. **REQ-candidate SW-KEY-11 Key-type selection.** The user shall be able to select the key type from a menu; optionally the firmware shall detect at power-on and on demand that one paddle input is permanently grounded (mono plug) and offer Straight mode on the other input, confirmed on the LCD (PicoKeyer pattern, F2). Speed = 0 (or a dedicated TUNE action) shall give momentary straight-key keying for tuning. [Demonstration]
20. **REQ-candidate SW-KEY-12 Determinism.** Element timing shall be produced by a hardware timer/PIO path independent of the UI loop, so that display or menu activity does not perturb timing beyond SW-KEY-02 (the WK3 design rationale: host latency "results in wrongly timed dits, dahs"). [Emulation with UI load]

### 4.3 Decisions needed (UI and design options for the owner)

- **DECISION-needed D1:** Default iambic mode (A per Elecraft/QRP Labs, B per K1EL/YACK) and whether Ultimatic and Bug are exposed or hidden.
- **DECISION-needed D2:** Key-type selection strategy: menu only (KX2/IC-705/QCX), power-on and on-demand auto-detection (PicoKeyer), or a jack with a mechanical insertion switch; and what happens when detection is ambiguous (single-lever paddle held at boot).
- **DECISION-needed D3:** Speed range top (40, 50, 60 WPM) and the speed UX (press-and-turn of the tuning encoder vs. a menu item; sidetone Morse announcement of speed).
- **DECISION-needed D4:** Sidetone default pitch (600 vs 700 Hz) and whether it is locked to the receiver CW offset; Relative vs Absolute level default.
- **DECISION-needed D5:** Default break-in (full QSK vs semi with 8-dit hang) given the 2 m T/R architecture and receiver recovery time.
- **DECISION-needed D6:** Envelope 4 vs 5 ms default and whether shaping is speed-adaptive.
- **DECISION-needed D7:** Which timing tunables (weight, ratio, compensation, first extension, switchpoint, autospace) appear in the user menu vs remain build-time defaults; Class A rigor argues for fewer exposed knobs.
- **DECISION-needed D8:** Offer a WinKeyer-compatible USB serial interface (large software ecosystem, F12) and/or message memories, beacon and CW ID (with the 20 WPM ID limit).
- **DECISION-needed D9:** ESD/abuse targets (IEC 61000-4-2 level 4; +/- voltage bound) and whether to accept a slightly higher pad current for the simpler TVS.
- **DECISION-needed D10:** Watchdog thresholds T_max for straight-key key-down and consecutive-element count.
- **DECISION-needed D11:** Physical disambiguation of the key and headphone jacks (position, colour, marking) versus relying on electrical survivability alone.

### 4.4 Risks

- **RISK-candidate R1 (hazard):** mono plug or stuck contact causes unintended continuous transmission at power-on (documented by Elecraft and QRP Labs). Controls: SW-KEY-10(a), CTL-KEY-07.
- **RISK-candidate R2:** RP2350-E9 on A2 silicon: designs relying on internal pulls or slow edges misbehave; mitigation: external pull-ups <= 8.2 kΩ, read `CHIP_ID.REVISION` at bring-up, prefer A3/A4 silicon.
- **RISK-candidate R3:** RF pickup on the key cable at 5 W / 144 MHz produces phantom elements; controls: CTL-KEY-05, bench test with cable attached.
- **RISK-candidate R4:** Timing jitter from UI or radio-control tasks degrades CW at >30 WPM; control: SW-KEY-12 and emulation with load.
- **RISK-candidate R5:** Iambic B behaviour varies between implementations (switchpoint); the owner's paddle habit may not match; control: switchpoint tunable, owner validation session in ConOps.
- **RISK-candidate R6:** Key clicks from a PA that does not follow the drive envelope linearly; control: LTspice of the PA with shaped drive, bench spectrum check (the owner's listed bench kit has no spectrum analyzer; an SDR receiver is needed).
- **RISK-candidate R7:** ESD at the exposed jack on a handheld; control: CTL-KEY-04.
- **RISK-candidate R8:** Debounce too long (UI-style 20 to 50 ms) swallows elements at speed; control: SW-KEY-06 numbers.

### 4.5 Actions

- **ACTION A1:** Write `docs/requirements/sw/sw-keyer` and CTL entries from the candidates above with rationale fields citing this report; assign verification methods as bracketed.
- **ACTION A2:** Create golden test vectors for Iambic A/B from the Curtis note examples (N, C, period, AR, AA, R, A) and the WK3 semantics; encode as HostUnit tests with a simulated 1 kHz sampler.
- **ACTION A3:** Trade study TS: key-type detection strategy (D2) and TS: envelope shaping method (D6), each with the numbers in F2/F10.
- **ACTION A4:** ICD-CTL-KEY: pin map, pull-up value, series R, TVS part, RC values, jack part number, mechanical position relative to the headphone jack.
- **ACTION A5:** Add hazard HZ candidate "unintended transmission from key input fault" to the hazard analysis with controls R1.
- **ACTION A6:** Acquire or borrow an SDR receiver for keying-sideband bench verification (R6).

## 5. Confidence

| Finding | Confidence | Note |
|---|---|---|
| F1 jack convention and mono-plug trap | High | Two vendor primary sources plus retailer guidance |
| F2 selection practice, PicoKeyer auto-detect | High | Vendor manuals quoted verbatim |
| F3 A/B semantics and switchpoint | High | Curtis note and WK3 datasheet are the defining sources |
| F4 ITU timing, PARIS | High | ITU-R M.1677-1 text; 1200/WPM stated by QRP Labs |
| F5 weighting/ratio/comp ranges | High | WK3, K3NG, QCX, Icom primary docs |
| F6 speed ranges/UX | High (ranges) / Medium (UX norms are conventions) | KX2 speed range not extracted |
| F7 debounce numbers | Medium | Curtis 5-10 ms vs Ganssle 1.5 ms avg; the 3 ms / 5 ms proposal is derived |
| F8 sidetone norms | High | Four vendor sources agree on 500 to 800 Hz typical |
| F9 break-in timing | High for QRP Labs/K1EL/Elecraft numbers; Low for Icom numeric range | Icom range not in text layer |
| F10 envelope | High for 5 ms guidance and CFR text; Medium for the -60 dBc / 500 Hz proposal | IVARC is an amateur analysis, internally consistent |
| F11 RP2350 electricals and E9 | High | Datasheet tables quoted; A4 stepping via Hackaday (secondary) |
| F12 open-source references | High (existence, licenses, features) / Low (Rust crate quality) | Not code-reviewed |

## 6. Open items

1. Icom IC-705 numeric break-in delay range and the KX2 keyer speed range were not in the extracted text; confirm from the manuals' figures if those benchmarks are wanted (they do not change the candidates).
2. Which RP2350 stepping the owner's Pico 2 modules carry (A2 vs A3/A4); read `CHIP_ID.REVISION` at first bring-up; CTL-KEY-03 keeps the design safe either way.
3. Owner's own key and paddle inventory (single-lever? contact material?) to set validation scenarios and to measure real bounce with a logic analyzer before freezing SW-KEY-06.
4. T/R switching architecture and PA recovery time (RX subsystem research) are needed before the full-QSK numbers in SW-KEY-08 can be finalized.
5. Whether a WinKeyer-compatible USB interface is in scope (D8); it drives USB CDC requirements and the cybersecurity tailoring note in the charter ("command injection via the key input").
6. Bench capability for keying-sideband measurement (SDR receiver) is not in the owner's listed kit.
7. Decide whether "external keyer on the tip" (Icom "select Straight" advice) is documented as a supported use case in the ConOps.

## 7. Sources

- Curtis 8044 Series Keyer-on-a-Chip Application Note (1992): https://users.ox.ac.uk/~malcolm/radio/8044print.pdf
- K1EL WinKeyer3 IC datasheet rev 1.3 (2019-03-19): https://www.k1elsystems.com/files/WK3_Datasheet_v1.3.pdf
- K1EL WKUSB Rev C manual v1.4 (2023-09-02): https://www.k1elsystems.com/files/WKUSB_Manual_C_R00.pdf
- Elecraft KX2 Owner's Manual rev A8: https://ftp.elecraft.com/KX2/Manuals%20Downloads/E740282%20-%20KX2%20Owner's%20Man%20A8.pdf
- Elecraft, Using a Straight Key with the KX3 (2012): https://ftp.elecraft.com/KX3/Mod%20Notes%20Alerts/Using%20a%20Straight%20Key%20with%20the%20KX3.pdf
- Icom IC-705 Basic Manual pp. 44-45: https://www.manualslib.com/manual/1875929/Icom-Ic-705.html?page=44 ; Advanced Manual: https://icomuk.co.uk/files/icom/PDF/advancedManuals/IC-705_ENG_Advanced_1a.pdf
- QRP Labs QCX operating manual fw 1.07: https://qrp-labs.com/images/qcxp/firmware/1.07/OpMan107.pdf ; QMX operating manual fw 1.02: https://qrp-labs.com/images/qmx/manuals/operation_1_02_002.pdf
- Ultra PicoKeyer manual fw 2.2 (2017): https://wd8rif.com/radio_manuals/pdf/Ultra-PicoKeyer-20170127.pdf
- K3NG keyer: https://github.com/k3ng/k3ng_cw_keyer ; wiki pages 400, 410, 225, 835; `keyer_settings.h`
- OpenCW Keyer MK2/MK3: https://github.com/ok1cdj/OpenCWKeyerMK2
- YACK manual: https://yack.sourceforge.net/
- uSDX README: https://raw.githubusercontent.com/threeme3/usdx/master/README.md
- ITU-R M.1677-1 (10/2009): https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
- 47 CFR 97.307: https://www.law.cornell.edu/cfr/text/47/97.307 ; 47 CFR 97.119: https://www.law.cornell.edu/cfr/text/47/97.119
- RP2350 Datasheet: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
- Hackaday on RP2350-E9 (2024-09-20) and A4 stepping (2025-07-31): https://hackaday.com/2024/09/20/raspberry-pi-rp2350-e9-erratum-redefined-as-input-mode-leakage-current/ ; https://hackaday.com/2025/07/31/raspberry-pi-rp2350-a4-stepping-addresses-e9-current-leakage-bug/
- Ganssle, A Guide to Debouncing: https://www.ganssle.com/debouncing.htm ; https://www.ganssle.com/debouncing-pt2.htm
- W8JI, What creates CW key clicks: https://www.w8ji.com/what_causes_clicks.htm
- IVARC, Key-clicks and CW Waveform shaping: http://www.ivarc.org.uk/uploads/1/2/3/8/12380834/keyclicks_version_1.pdf
- DX Engineering, Hooking up a Keyer Paddle: https://dxengineering.wordpress.com/2016/09/01/tech-tip-hooking-up-a-keyer-paddle/
- Hermes Lite 2 Plus straight key page: https://www.hermeslite2plus.com/p/using-straight-key-or-external-keyer.html
- Morse Code World, Iambic and Ultimatic: https://morsecode.world/iambic.html ; Timing: https://morsecode.world/international/timing/
- Nexperia PESD3V3L2BT: https://www.nexperia.com/product/PESD3V3L2BT ; IEC 61000-4-2 overview: https://en.wikipedia.org/wiki/IEC_61000-4-2
- radio-utils-keyer crate: https://docs.rs/radio-utils-keyer/latest/radio_utils_keyer/
