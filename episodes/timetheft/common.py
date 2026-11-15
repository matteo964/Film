"""Gemeinsame Besetzung/Sets: "Your boss accuses you of time theft... for going to the bathroom"."""
import math

import cairo
import backgrounds as bgm
import backgrounds_v2 as B
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect, stroke_black, draw_figure, POSES

GAP = 0.15
HOOK_BASE = ["POV: Your boss accuses you of time theft...", "for going to the bathroom"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
NORA = Look(shirt=(0.30, 0.62, 0.70), skin=(0.88, 0.74, 0.60), iris=(0.25, 0.17, 0.10), hair="bob", hair_color=(0.35, 0.22, 0.12),
            outfit="blouse", shoes=True, lashes=True)
TRENT = Look(shirt=(0.55, 0.55, 0.60), skin=SKIN, iris=(0.30, 0.55, 0.85), hair="spiky", hair_color=(0.80, 0.35, 0.12),
             beard=(0.75, 0.32, 0.12), outfit="suit", tie_color=(0.10, 0.20, 0.45), shoes=True)
PAM = Look(shirt=(0.45, 0.20, 0.30), skin=SKIN, iris=(0.35, 0.30, 0.20), hair="updo", hair_color=(0.80, 0.80, 0.82),
           outfit="blouse", shoes=True, lashes=True, glasses=True)
OKONJO = Look(shirt=(0.12, 0.12, 0.15), skin=(0.42, 0.29, 0.21), iris=(0.2, 0.12, 0.08), hair="bald", hair_color=(0.1, 0.1, 0.1),
              outfit="suit", tie_color=(0.85, 0.65, 0.20), shoes=True)
LEO = Look(shirt=(0.95, 0.55, 0.25), skin=(0.62, 0.45, 0.33), iris=(0.22, 0.14, 0.08), hair="curly", hair_color=(0.06, 0.05, 0.05),
           outfit="hoodie", shoes=True)

CHARS = {
    "N": dict(voice="en-US-MichelleNeural", el_voice="EXAVITQu4vr4xnSDxMaL", look=NORA),       # Sarah
    "T": dict(voice="en-US-AndrewMultilingualNeural", el_voice="IKne3meq5aSn9XLyUdCD", look=TRENT),  # Charlie
    "P": dict(voice="en-US-AriaNeural", el_voice="Xb7hH8MSUJpSbSDYk0k2", look=PAM),            # Alice
    "O": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=OKONJO),  # Brian
    "L": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=LEO),          # Will
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ WorkWatch-UI
def _cam_thumb(cr, x, y, w, h, look=None, label="", empty_tint=False):
    rrect(cr, x, y, w, h, 10); cr.set_source_rgb(*rgb("#2E3A48")); cr.fill()
    cr.save(); rrect(cr, x, y, w, h, 10); cr.clip()
    # Stuhllehne
    rrect(cr, x + w * 0.3, y + h * 0.45, w * 0.4, h * 0.6, 14); cr.set_source_rgb(*rgb("#1B2230")); cr.fill()
    if look is not None:
        sc = h / 420.0
        draw_figure(cr, look, x + w / 2, y + h * 0.42 + 770 * sc, sc, 1, dict(hands=POSES["idle"], emotion="neutral"), 0)
    cr.set_source_rgba(0, 0, 0, 0.12)
    for yy in range(int(y), int(y + h), 5):
        cr.rectangle(x, yy, w, 2); cr.fill()
    cr.restore()
    _text(cr, label, x + 10, y + h - 10, 18, (1, 1, 1), font="DejaVu Sans Mono", center=False)


def dashboard(name, look, segments, alert=None, thumbs=(), stat=None):
    """segments: Liste (anteil, farbe) – Aktivitäts-Zeitleiste."""
    def fn(cr, t):
        cr.set_source_rgb(*rgb("#0F141C")); cr.paint()
        x, y, w, h = 30, 450, 1020, 1000
        rrect(cr, x, y, w, h, 18); cr.set_source_rgb(*rgb("#F4F6F8")); cr.fill()
        rrect(cr, x, y, w, 76, 18); cr.set_source_rgb(*rgb("#5B2BD9")); cr.fill()
        cr.rectangle(x, y + 40, w, 36); cr.fill()
        _text(cr, "WorkWatch  ·  Employee Monitor", x + 30, y + 50, 30, (1, 1, 1), center=False)
        _text(cr, name, x + 30, y + 140, 40, rgb("#1B1F27"), center=False)
        if stat:
            _text(cr, stat[0], x + w - 40 - 22 * len(stat[0]), y + 140, 40, rgb(stat[1]), center=False)
        _text(cr, "Activity today", x + 30, y + 200, 26, rgb("#6E7A88"), bold=False, center=False)
        bx, bw = x + 30, w - 60
        cx = bx
        for frac, col in segments:
            cr.rectangle(cx, y + 220, bw * frac, 46); cr.set_source_rgb(*rgb(col)); cr.fill()
            cx += bw * frac
        for k, lab in enumerate(("9:00", "12:00", "15:00", "18:00", "21:00")):
            _text(cr, lab, bx + k * bw / 4 - (50 if k == 4 else 0), y + 300, 20, rgb("#6E7A88"), bold=False, center=(0 < k < 4))
        _text(cr, "Webcam snapshots (every 5 min)", x + 30, y + 360, 26, rgb("#6E7A88"), bold=False, center=False)
        for k, (lk, lab) in enumerate(thumbs):
            _cam_thumb(cr, x + 30 + k * 330, y + 380, 310, 230, lk, lab)
        if alert:
            on = int(bgm.CLOCK["t"] * 2.5) % 2 == 0
            rrect(cr, x + 30, y + 660, w - 60, 140, 16)
            cr.set_source_rgb(*(rgb("#E23B3B") if on else rgb("#B3261E"))); cr.fill()
            _text(cr, alert[0], x + w / 2, y + 720, 42, (1, 1, 1))
            _text(cr, alert[1], x + w / 2, y + 775, 32, (1, 1, 1), bold=False)
    return fn


NORA_SEG = [(0.32, "#33C46A"), (0.03, "#E23B3B"), (0.65, "#33C46A")]
NORA_LATE = [(0.32, "#33C46A"), (0.03, "#E23B3B"), (0.45, "#33C46A"), (0.20, "#2E8B57")]
TRENT_SEG = [(1.0, "#33C46A")]

COLD = dashboard("Nora Kim · Data Analyst", NORA, NORA_SEG, ("TIME THEFT DETECTED", "11:42 – 11:53 · 11 min idle"),
                 ((NORA, "11:40"), (None, "11:45"), (None, "11:50")))
LATE = dashboard("Nora Kim · Logged out 21:14", NORA, NORA_LATE, None,
                 ((NORA, "19:30"), (NORA, "20:45"), (NORA, "21:10")), ("+3h 14m", "#1F8A47"))
TRENT_DASH = dashboard("Trent Walsh · Team Manager", TRENT, TRENT_SEG, None,
                       ((None, "10:00"), (None, "13:00"), (None, "16:00")), ("100% active", "#1F8A47"))


# ------------------------------------------------------------------ Trents Schreibtisch mit Maus-Jiggler
def jiggler_desk(cr, t=None):
    t = bgm.CLOCK["t"] if t is None else t
    # leerer Stuhl (hinter dem Tisch)
    rrect(cr, 150, 1040, 200, 260, 34); fill_stroke(cr, rgb("#2E3440"), 4)
    # Monitor
    rrect(cr, 280, 820, 520, 340, 14); fill_stroke(cr, rgb("#15181F"), 6)
    cr.rectangle(300, 840, 480, 300); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.rectangle(300, 840, 480, 40); cr.set_source_rgb(*rgb("#2B579A")); cr.fill()
    _text(cr, "Quarterly_Report.docx", 320, 868, 22, (1, 1, 1), center=False)
    n = int(t * 14) % 156
    line = "a" * 26
    for k in range(min(6, n // 26 + 1)):
        _text(cr, line if k < n // 26 else "a" * (n % 26), 320, 920 + k * 34, 26, rgb("#1B1F27"), font="DejaVu Sans Mono", center=False)
    # Cursor wandert
    cxp = 520 + math.sin(t * 2.3) * 160
    cyp = 1000 + math.cos(t * 1.7) * 80
    cr.move_to(cxp, cyp); cr.line_to(cxp, cyp + 34); cr.line_to(cxp + 10, cyp + 24); cr.line_to(cxp + 24, cyp + 24); cr.close_path()
    cr.set_source_rgb(0, 0, 0); cr.fill()
    rrect(cr, 520, 1160, 40, 30, 4); cr.set_source_rgb(*rgb("#15181F")); cr.fill()
    # Tisch
    rrect(cr, 120, 1290, 840, 36, 8); fill_stroke(cr, rgb("#7A5233"), 5)
    cr.rectangle(150, 1326, 780, 240); fill_stroke(cr, rgb("#6A4529"), 5)
    # Jiggler + Maus
    rrect(cr, 640, 1250, 120, 40, 8); fill_stroke(cr, rgb("#E9EDF2"), 3)
    dx = math.sin(t * 9) * 14
    cr.save(); cr.translate(700 + dx, 1238); cr.scale(36, 22); cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
    cr.set_source_rgb(*rgb("#2B2F38")); cr.fill()
    # Golf-Zettel
    cr.save(); cr.translate(860, 1180); cr.rotate(0.1)
    cr.rectangle(-70, -60, 140, 110); cr.set_source_rgb(*rgb("#FFE14D")); cr.fill()
    _text(cr, "Tee time", 0, -10, 24, rgb("#1B1F27"), font="DejaVu Sans")
    _text(cr, "1:00 PM", 0, 24, 24, rgb("#1B1F27"), font="DejaVu Sans")
    cr.restore()


# ------------------------------------------------------------------ Firmenbericht
def report(cr, t):
    l = lt()
    x, y, w, h = 90, 440, 900, 520
    rrect(cr, x - 14, y - 14, w + 28, h + 28, 10); fill_stroke(cr, rgb("#1B1F27"), 6)
    cr.rectangle(x, y, w, h); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.rectangle(x, y, w, 64); cr.set_source_rgb(*rgb("#5B2BD9")); cr.fill()
    _text(cr, "WORKWATCH · COMPANY REPORT · ALL USERS", x + w / 2, y + 44, 28, (1, 1, 1))
    rows = [("Nora Kim", "112%", "+14h unpaid overtime", "#1F8A47"), ("Leo Mendes", "98%", "", "#1F8A47"),
            ("Trent Walsh", "100%", "", "#1F8A47")]
    for k, (a, b, c, col) in enumerate(rows):
        yy = y + 140 + k * 80
        _text(cr, a, x + 40, yy, 34, rgb("#1B1F27"), center=False)
        _text(cr, b, x + 380, yy, 34, rgb(col), center=False)
        _text(cr, c, x + 520, yy, 24, rgb("#1F8A47"), bold=False, center=False)
    if bgm.CLOCK["t"] > 27.0:
        for k in range(3):
            _cam_thumb(cr, x + 40 + k * 280, y + 370, 260, 130, None, ("13:05", "14:30", "16:10")[k])
        rrect(cr, x + 480, y + 278, 400, 52, 10); cr.set_source_rgb(*rgb("#FFE3E3")); cr.fill()
        _text(cr, "chair empty 6h · mouse jiggler", x + 680, y + 314, 24, rgb("#B3261E"))


def report_compact(cr, t):
    cr.save(); cr.translate(30, 440); cr.scale(0.74, 0.74); cr.translate(-90, -440)
    report(cr, t)
    cr.restore()


BG = {"office": B.boss_office, "open": B.open_office, "dark": None, "meet": B.meeting2("pitch")}


def _dark():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    c = cairo.Context(s); c.set_source_rgb(*rgb("#0F141C")); c.paint(); s.flush()
    return s


def _wall():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#DCE3EA"), rgb("#8D9AA8"), tiles="wood")
    B.window_city(cr, 1000, 470, 70, 600)
    rrect(cr, 60, 1300, 960, 44, 12); fill_stroke(cr, rgb("#F2F2F2"), 5, rgb("#6E6E6E"))
    s.flush()
    return s


BG["dark"] = _dark
BG["wall"] = _wall

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def one(b, cid, x=540, facing=1, front=None, opts=None, overlays=None):
    d = dict(bg=b, layers=[("char", cid, x, Y1, S1, facing, opts or {})] + ([("fn", front)] if front else []))
    if overlays:
        d["overlays"] = overlays
    return d


def two(b, left, right, overlays=None, xl=300, xr=780):
    d = dict(bg=b, layers=[("char", left, xl, Y2, S2, 1), ("char", right, xr, Y2, S2, -1)])
    if overlays:
        d["overlays"] = overlays
    return d


def three(b, a, m, c, overlays=None):
    d = dict(bg=b, layers=[("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, -1), ("char", c, 875, Y2, 0.9, -1)])
    if overlays:
        d["overlays"] = overlays
    return d


SHOTS = {
    "cold": dict(bg="dark", overlays=[COLD], layers=[]),
    "late": dict(bg="dark", overlays=[LATE], layers=[]),
    "trent_dash": dict(bg="dark", overlays=[TRENT_DASH], layers=[]),
    "office_T": one("office", "T", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_N": one("office", "N", 600, -1),
    "office_TN": dict(bg="office", layers=[("char", "T", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "N", 820, 1760, 1.0, -1)]),
    "office_TNP": dict(bg="office", layers=[("char", "T", 230, 1720, 0.9, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                            ("char", "N", 640, 1760, 0.9, -1), ("char", "P", 900, 1760, 0.9, -1)]),
    "office_P": one("office", "P", 600, -1),
    "open_TL": two("open", "T", "L"),
    "open_T": one("open", "T", 480, 1),
    "open_L": one("open", "L", 600, -1),
    "open_NL": two("open", "L", "N"),
    "jiggle": dict(bg="open", layers=[("fn", lambda cr: jiggler_desk(cr))]),
    "jiggle_NL": dict(bg="open", layers=[("fn", lambda cr: jiggler_desk(cr)), ("char", "L", 120, Y2, 0.9, 1), ("char", "N", 960, Y2, 0.9, -1)]),
    "rep_O": one("wall", "O", 900, -1, overlays=[report_compact]),
    "rep_T": one("wall", "T", 900, -1, overlays=[report_compact]),
    "rep_N": one("wall", "N", 900, -1, overlays=[report_compact]),
    "rep_OT": two("wall", "T", "O", overlays=[report]),
    "rep_ONT": three("wall", "T", "N", "O", overlays=[report]),
}
