"""Gemeinsame Besetzung/Sets (Illustrationsstil): CEO zahlt die Bäckerin der Jubiläumstorte nicht."""
import math

import cairo
import backgrounds as bgm
import backgrounds_v2 as B
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect, stroke_black

GAP = 0.15
HOOK_BASE = ["POV: The CEO refuses to pay the freelance", "baker for his company's anniversary cake"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
ROSA = Look(shirt=(0.98, 0.98, 0.98), skin=(0.82, 0.64, 0.48), iris=(0.28, 0.18, 0.10), hair="long",
            hair_color=(0.12, 0.08, 0.06), outfit="blouse", shirt_inner=(0.85, 0.35, 0.45), apron=True, shoes=True, lashes=True)
HOWARD = Look(shirt=(0.30, 0.18, 0.15), skin=SKIN, iris=(0.40, 0.30, 0.20), hair="buzz", hair_color=(0.70, 0.70, 0.72),
              beard=(0.72, 0.72, 0.74), outfit="suit", tie_color=(0.85, 0.70, 0.25), shoes=True)
CHAD = Look(shirt=(0.40, 0.70, 0.85), skin=SKIN, iris=(0.30, 0.55, 0.85), hair="curly", hair_color=(0.95, 0.85, 0.55),
            outfit="blouse", shirt_inner=(0.98, 0.98, 0.98), shoes=True)
VANCE = Look(shirt=(0.10, 0.35, 0.40), skin=SKIN, iris=(0.30, 0.40, 0.55), hair="updo", hair_color=(0.85, 0.85, 0.88),
             outfit="blouse", shoes=True, lashes=True, glasses=True)

CHARS = {
    "R": dict(voice="en-US-EmmaMultilingualNeural", el_voice="FGY2WhTYpPnrIDTdsKH5", look=ROSA),      # Laura
    "H": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal", look=HOWARD),  # Eric
    "C": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=CHAD),                # Liam
    "V": dict(voice="en-US-AriaNeural", el_voice="Xb7hH8MSUJpSbSDYk0k2", look=VANCE),                 # Alice
}

BG = {"office": B.boss_office, "bakery": B.bakery, "gala": B.reception("gala")}

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


# ------------------------------------------------------------------ Torten
def cart(cr, x, y):
    cr.rectangle(x - 170, y - 20, 340, 24)
    fill_stroke(cr, rgb("#D9D9D9"), 4, rgb("#6E6E6E"))
    for dx in (-150, 150):
        cr.move_to(x + dx, y + 4); cr.line_to(x + dx, y + 150); stroke_black(cr, 6)
        cr.arc(x + dx, y + 160, 12, 0, 2 * math.pi); cr.set_source_rgb(0.1, 0.1, 0.1); cr.fill()


def real_cake(cr, x=300, y=1480):
    cart(cr, x, y)
    tiers = [(300, 110), (250, 100), (200, 95), (150, 90), (105, 80)]
    yy = y - 20
    for (w, h) in tiers:
        rrect(cr, x - w / 2, yy - h, w, h, 10)
        fill_stroke(cr, rgb("#FFFDF8"), 4, rgb("#B8A890"))
        cr.rectangle(x - w / 2, yy - 26, w, 12); cr.set_source_rgb(*rgb("#E5B94E")); cr.fill()
        for k in range(int(w / 40)):
            cr.arc(x - w / 2 + 20 + k * 40, yy - h + 10, 7, 0, math.pi)
            cr.set_source_rgb(*rgb("#F7E7CE")); cr.fill()
        yy -= h
    cr.arc(x, yy - 50, 44, 0, 2 * math.pi)
    cr.set_source_rgb(*rgb("#E5B94E")); cr.set_line_width(7); cr.stroke()
    _text(cr, "25", x, yy - 32, 48, rgb("#E5B94E"))
    for (dx, c) in ((-70, "#F7A1B5"), (70, "#F7A1B5"), (0, "#FFFFFF")):
        cr.arc(x + dx, y - 130, 16, 0, 2 * math.pi); cr.set_source_rgb(*rgb(c)); cr.fill()


def chad_cake(cr, x=300, y=1480, collapse=0.0):
    cart(cr, x, y)
    tiers = [(260, 120, "#8B5A33"), (190, 110, "#8B5A33"), (140, 100, "#6FBF5A")]
    yy = y - 20
    for i, (w, h, col) in enumerate(tiers):
        lean = (0.08 + 0.05 * i) + collapse * (0.5 + 0.4 * i)
        slide = collapse * (90 + 120 * i)
        drop = collapse * (40 * i)
        cr.save()
        cr.translate(x + slide * (1 if i % 2 == 0 else 0.6), yy + drop)
        cr.rotate(lean if i != 1 else -lean * 0.6)
        cr.move_to(-w / 2, 0); cr.line_to(w / 2, 0); cr.line_to(w / 2 - 14, -h); cr.line_to(-w / 2 + 6, -h + 10)
        cr.close_path()
        fill_stroke(cr, rgb(col), 4)
        # Glasur-Tropfen
        for k in range(5):
            dx = -w / 2 + 20 + k * (w - 40) / 4
            cr.move_to(dx - 10, -h + 6); cr.line_to(dx + 10, -h + 6); cr.line_to(dx + 3, -h + 40 + (k % 2) * 30)
            cr.close_path(); cr.set_source_rgb(*rgb("#F2F2F2")); cr.fill()
        if i == 2:
            _text(cr, "HAPY 52", 0, -h + 70, 28, rgb("#E23B3B"))
            for k in range(3):
                cr.move_to(-30 + k * 30, -h); cr.line_to(-36 + k * 34, -h - 50)
                cr.set_source_rgb(*rgb(("#3D8BFF", "#F2C230", "#E23B3B")[k])); cr.set_line_width(8); cr.stroke()
        cr.restore()
        yy -= h * (1 - collapse * 0.6)
    if collapse > 0.85:
        cr.save(); cr.translate(x + 120, y + 30); cr.scale(220, 36); cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
        cr.set_source_rgba(0.45, 0.28, 0.15, 0.85); cr.fill()


def cake_none(cr):
    cart(cr, 300, 1480)


def cake_real(cr):
    real_cake(cr)


def cake_chad(cr):
    chad_cake(cr)


COLLAPSE_AT = 1.2


def cake_collapse(cr):
    lt = bgm.CLOCK["lt"]
    c = max(0.0, min(1.0, (lt - COLLAPSE_AT) / 1.6)) ** 1.6
    chad_cake(cr, collapse=c)


def one(b, cid, x=540, facing=1, front=None, opts=None, back=None):
    layers = ([("fn", back)] if back else []) + [("char", cid, x, Y1, S1, facing, opts or {})]
    if front:
        layers.append(("fn", front))
    return dict(bg=b, layers=layers)


def two(b, left, right, back=None):
    return dict(bg=b, layers=([("fn", back)] if back else []) + [("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])


def gala_side(cid, cake, x=820):
    """Figur rechts, Torte links auf dem Wagen."""
    return dict(bg="gala", layers=[("fn", cake), ("char", cid, x, Y1, S1, -1)])


def gala_pair(a, b_, cake):
    return dict(bg="gala", layers=[("fn", cake), ("char", a, 640, Y2, S2, 1), ("char", b_, 900, Y2, S2, -1)])


SHOTS = {
    "office_H": one("office", "H", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_R": one("office", "R", 600, -1),
    "office_HR": dict(bg="office", layers=[("char", "H", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "R", 820, 1760, 1.0, -1)]),
    "bakery_C": one("bakery", "C", 480, 1),
    "bakery_R": one("bakery", "R", 560, -1),
    "bakery_CR": two("bakery", "C", "R"),
}
for name, cake in (("none", cake_none), ("chad", cake_chad), ("collapse", cake_collapse), ("real", cake_real)):
    for cid in ("H", "C", "V", "R"):
        SHOTS[f"{name}_{cid}"] = gala_side(cid, cake)
    SHOTS[f"{name}_HC"] = gala_pair("H", "C", cake)
    SHOTS[f"{name}_HV"] = gala_pair("H", "V", cake)
    SHOTS[f"{name}_VR"] = gala_pair("V", "R", cake)
    SHOTS[f"{name}_HR"] = gala_pair("H", "R", cake)
