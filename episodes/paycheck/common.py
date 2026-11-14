"""Gemeinsame Besetzung/Sets: "You find the new guy's paycheck on the office printer"."""
import math

import cairo
import backgrounds as bgm
import backgrounds_v2 as B
import mailui as MU
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect, stroke_black

GAP = 0.15
HOOK_BASE = ["POV: You find the new guy's paycheck", "on the office printer..."]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
LENA = Look(shirt=(0.25, 0.45, 0.70), skin=SKIN, iris=(0.30, 0.50, 0.30), hair="bob", hair_color=(0.70, 0.25, 0.12),
            outfit="blouse", shoes=True, lashes=True)
DARREN = Look(shirt=(0.30, 0.30, 0.34), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="buzz", hair_color=(0.55, 0.55, 0.58),
              moustache=True, outfit="suit", tie_color=(0.20, 0.45, 0.30), shoes=True)
TYLER = Look(shirt=(0.85, 0.85, 0.88), skin=SKIN, iris=(0.30, 0.55, 0.85), hair="spiky", hair_color=(0.40, 0.25, 0.12),
             outfit="suit", tie_color=(0.20, 0.30, 0.60), shoes=True)
MONICA = Look(shirt=(0.50, 0.20, 0.45), skin=(0.48, 0.33, 0.24), iris=(0.22, 0.14, 0.08), hair="updo", hair_color=(0.08, 0.06, 0.06),
              outfit="suit", tie_color=(0.95, 0.95, 0.95), shoes=True, lashes=True, glasses=True)
RAJ = Look(shirt=(0.90, 0.55, 0.20), skin=(0.66, 0.48, 0.35), iris=(0.22, 0.14, 0.08), hair="curly", hair_color=(0.06, 0.05, 0.05),
           outfit="hoodie", shoes=True, glasses=True)

CHARS = {
    "L": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX", look=LENA),      # Matilda
    "D": dict(voice="en-US-AndrewMultilingualNeural", el_voice="pNInz6obpgDQGcFmaJgB", look=DARREN),  # Adam
    "T": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=TYLER),       # Liam
    "M": dict(voice="en-US-AriaNeural", el_voice="hpp4J3VqNfWAUOO0d1Us", look=MONICA),        # Bella
    "R": dict(voice="en-US-ChristopherNeural", el_voice="bIHbv24MWmeRgasZH58o", look=RAJ),   # Will
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ Gehaltsabrechnung (Cold Open)
def payslip(cr, t):
    l = lt()
    cr.set_source_rgb(*rgb("#11151C")); cr.paint()
    # Drucker oben
    rrect(cr, 190, 440, 700, 190, 24); fill_stroke(cr, rgb("#D9DEE4"), 6, rgb("#5E6A78"))
    cr.rectangle(260, 600, 560, 24); cr.set_source_rgb(*rgb("#2B2F38")); cr.fill()
    cr.arc(820, 490, 12, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#33E07A")); cr.fill()
    # Blatt fährt heraus
    out = min(1.0, l / 1.2)
    y0 = 612
    h = 860 * out
    cr.save(); cr.rectangle(0, y0, 1080, 1300); cr.clip()
    x, y, w = 150, y0 + h - 860, 780
    cr.rectangle(x, y, w, 860); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.rectangle(x, y, w, 90); cr.set_source_rgb(*rgb("#1F3B63")); cr.fill()
    _text(cr, "PAY STATEMENT · CONFIDENTIAL", x + w / 2, y + 58, 32, (1, 1, 1))
    rows = [("Employee", "Tyler Brooks"), ("Position", "Junior Analyst"), ("Start date", "3 weeks ago"), ("Annual salary", "$112,000")]
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    for k, (a, b) in enumerate(rows):
        yy = y + 170 + k * 120
        _text(cr, a, x + 50, yy, 30, rgb("#6E7A88"), bold=False, center=False)
        hl_t = 1.6 + k * 0.9 if k in (0, 2, 3) else None
        cr.set_font_size(46 if k == 3 else 42)
        tw = cr.text_extents(b).x_advance
        if hl_t is not None:
            f = max(0.0, min(1.0, (l - hl_t) / 0.6))
            if f > 0:
                cr.rectangle(x + 46, yy + 16, (tw + 12) * f, 54)
                cr.set_source_rgba(1.0, 0.9, 0.1, 0.85); cr.fill()
        _text(cr, b, x + 50, yy + 58, 46 if k == 3 else 42, rgb("#1B1F27"), center=False)
    cr.restore()
    # eigenes Gehalt
    if l > 6.0:
        rrect(cr, 150, 1500 - 60, 780, 100, 16)
        cr.set_source_rgb(*rgb("#FFE3E3")); cr.fill_preserve(); cr.set_source_rgb(*rgb("#E23B3B")); cr.set_line_width(4); cr.stroke()
        _text(cr, "Lena Park · 8 years · $61,000", 540, 1508, 40, rgb("#B3261E"))


def printer(cr):
    rrect(cr, 640, 1150, 330, 150, 18); fill_stroke(cr, rgb("#D9DEE4"), 5, rgb("#5E6A78"))
    cr.rectangle(690, 1270, 230, 16); cr.set_source_rgb(*rgb("#2B2F38")); cr.fill()
    cr.rectangle(660, 1300, 290, 260); cr.set_source_rgb(*rgb("#C3CAD2")); cr.fill_preserve(); stroke_black(cr, 4)


# ------------------------------------------------------------------ Whiteboard
ENTRIES = [  # (name, jahre, gehalt, zeit-ab-shotstart, neu?)
    ("Lena", "8 yrs", "$61,000", "L"),
    ("Raj", "6 yrs", "$64,000", "R"),
    ("Maya", "5 yrs", "$59,000", "x1"),
    ("Chris", "2 mo", "$105,000", "x2"),
    ("Tyler", "3 wks", "$112,000", "T"),
]


def whiteboard(n_rows=None, wiped=0.0, compact=False):
    def fn(cr, t):
        x, y, w, h = (40, 440, 650, 470) if compact else (110, 440, 860, 470)
        c1, c2, c3, fs = (30, 220, 390, 32) if compact else (50, 330, 560, 36)
        rrect(cr, x - 14, y - 14, w + 28, h + 28, 10); fill_stroke(cr, rgb("#9AA6B2"), 4)
        cr.rectangle(x, y, w, h); cr.set_source_rgb(1, 1, 1); cr.fill()
        _text(cr, "WHAT WE GET PAID", x + w / 2, y + 62, 40 if compact else 44, rgb("#1F3B63"), font="DejaVu Sans")
        n = n_rows(lt()) if callable(n_rows) else (n_rows or 0)
        for k, (name, yrs, sal, who) in enumerate(ENTRIES[:n]):
            yy = y + 130 + k * 68
            new = yrs in ("2 mo", "3 wks")
            col = rgb("#B3261E") if new else rgb("#1F3B63")
            _text(cr, name, x + c1, yy, fs, col, font="DejaVu Sans", center=False)
            _text(cr, yrs, x + c2, yy, fs, col, font="DejaVu Sans", center=False)
            _text(cr, sal, x + c3, yy, fs, col, font="DejaVu Sans", center=False)
        if callable(n_rows) and n >= 5 and lt() > 0:
            pass
        if wiped > 0:
            cr.rectangle(x, y, w * wiped, h); cr.set_source_rgba(0.95, 0.95, 0.95, 0.9); cr.fill()
        # Marker-Ablage
        cr.rectangle(x, y + h + 14, w, 16); cr.set_source_rgb(*rgb("#9AA6B2")); cr.fill()
    return fn


def board_ramp(start_rows, end_rows, per=1.4):
    return lambda l: min(end_rows, start_rows + int(max(0.0, l) / per))


def bands_compact(cr, t):
    cr.save(); cr.translate(40, 450); cr.scale(0.76, 0.76); cr.translate(-110, -450)
    bands_screen(cr, t)
    cr.restore()


def bands_screen(cr, t):
    x, y, w, h = 110, 450, 860, 560
    rrect(cr, x - 14, y - 14, w + 28, h + 28, 10); fill_stroke(cr, rgb("#1B1F27"), 6)
    cr.rectangle(x, y, w, h); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.rectangle(x, y, w, 70); cr.set_source_rgb(*rgb("#1F3B63")); cr.fill()
    _text(cr, "OFFICIAL SALARY BANDS · ANALYST", x + w / 2, y + 46, 30, (1, 1, 1))
    rows = [("Junior (0–2 yrs)", "$70k – $95k"), ("Analyst (3–5 yrs)", "$90k – $120k"), ("Senior (6+ yrs)", "$115k – $150k")]
    for k, (a, b) in enumerate(rows):
        yy = y + 160 + k * 110
        _text(cr, a, x + 50, yy, 36, rgb("#1B1F27"), center=False)
        _text(cr, b, x + 520, yy, 36, rgb("#1F8A47"), center=False)
    _text(cr, "Lena: $61k  →  below the JUNIOR band", x + w / 2, y + 510, 34, rgb("#E23B3B"))


BG = {"office": B.boss_office, "open": B.open_office, "dark": None, "meet": B.meeting2("pitch")}


def _plain_dark():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s); cr.set_source_rgb(*rgb("#11151C")); cr.paint(); s.flush()
    return s


BG["dark"] = _plain_dark


def _plain_room():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#E2E8EE"), rgb("#9AA6B2"), tiles="tile")
    B.window_city(cr, 870, 470, 190, 600)
    B.plant(cr, 990, 1240, 0.7)
    s.flush()
    return s


BG["wall"] = _plain_room

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def one(b, cid, x=540, facing=1, front=None, opts=None, back=None, after=None):
    layers = ([("fn", back)] if back else []) + [("char", cid, x, Y1, S1, facing, opts or {})]
    if front:
        layers.append(("fn", front))
    d = dict(bg=b, layers=layers)
    if after:
        d["front"] = after
    return d


def two(b, left, right, back=None):
    return dict(bg=b, layers=([("fn", back)] if back else []) + [("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])


def three(b, a, m, c, fm=-1, back=None):
    return dict(bg=b, layers=([("fn", back)] if back else []) + [("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, fm),
                                                                ("char", c, 875, Y2, 0.9, -1)])


def wb(n, compact=False):
    return lambda cr: whiteboard(n, compact=compact)(cr, 0)


SHOTS = {
    "cold": dict(bg="dark", overlays=[payslip], layers=[]),
    "printer_L": one("open", "L", 380, 1, front=printer),
    "printer_LR": dict(bg="open", layers=[("char", "R", 200, Y2, 0.95, 1), ("char", "L", 470, Y2, 0.95, -1), ("fn", printer)]),
    "office_D": one("office", "D", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_L": one("office", "L", 600, -1),
    "office_DL": dict(bg="office", layers=[("char", "D", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "L", 820, 1760, 1.0, -1)]),
    "wb1_L": one("wall", "L", 880, -1, back=wb(1, True)),
    "wb_ramp": dict(bg="wall", overlays=[whiteboard(board_ramp(1, 4, 1.6), compact=True)], layers=[("char", "R", 880, Y1, S1, -1)]),
    "wb4_R": one("wall", "R", 880, -1, back=wb(4, True)),
    "wb4_D": one("wall", "D", 880, -1, back=wb(4, True)),
    "wb4_DT": two("wall", "D", "T", back=wb(4)),
    "wb5_T": one("wall", "T", 880, -1, back=wb(5, True)),
    "wb5_DT": two("wall", "D", "T", back=wb(5)),
    "wb5_M": one("wall", "M", 880, -1, back=wb(5, True)),
    "wb5_DMT": three("wall", "D", "M", "T", back=wb(5)),
    "bands_M": dict(bg="wall", overlays=[bands_compact], layers=[("char", "M", 880, Y1, S1, -1)]),
    "bands_D": dict(bg="wall", overlays=[bands_compact], layers=[("char", "D", 880, Y1, S1, -1)]),
    "bands_DM": dict(bg="wall", overlays=[bands_screen], layers=[("char", "D", 300, Y2, S2, 1), ("char", "M", 780, Y2, S2, -1)]),
    "bands_LM": dict(bg="wall", overlays=[bands_screen], layers=[("char", "L", 300, Y2, S2, 1), ("char", "M", 780, Y2, S2, -1)]),
    "wb5_LT": two("wall", "T", "L", back=wb(5)),
    "wb5_L": one("wall", "L", 880, -1, back=wb(5, True)),
}
