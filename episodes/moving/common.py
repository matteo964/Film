"""Serie: "Your boss's 'mandatory team building' is actually... his moving day"."""
import math
import random

import cairo
import anim
import backgrounds as bgm
import backgrounds_v2 as B
import mailui as MU
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect, stroke_black

GAP = 0.15
HOOK_BASE = ["POV: Your boss's \"mandatory team building\"", "is actually... his moving day"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
ROSA = Look(shirt=(0.90, 0.45, 0.35), skin=(0.82, 0.64, 0.48), iris=(0.25, 0.17, 0.10), hair="curly", hair_color=(0.10, 0.07, 0.06),
            outfit="hoodie", shoes=True, lashes=True)
KAI = Look(shirt=(0.30, 0.55, 0.85), skin=SKIN, iris=(0.30, 0.55, 0.85), hair="spiky", hair_color=(0.92, 0.80, 0.45),
           outfit="hoodie", shoes=True)
CRAIG = Look(shirt=(0.95, 0.95, 0.90), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="sidepart", hair_color=(0.35, 0.22, 0.12),
             outfit="blouse", shirt_inner=(0.30, 0.65, 0.95), shoes=True, glasses=True)
PATEL = Look(shirt=(0.18, 0.20, 0.28), skin=(0.66, 0.48, 0.35), iris=(0.2, 0.12, 0.08), hair="buzz", hair_color=(0.75, 0.75, 0.78),
             beard=(0.75, 0.75, 0.78), outfit="suit", tie_color=(0.20, 0.55, 0.45), shoes=True)
MOM = Look(shirt=(0.70, 0.45, 0.70), skin=SKIN, iris=(0.3, 0.4, 0.6), hair="bob", hair_color=(0.85, 0.85, 0.88),
           outfit="blouse", shoes=True, lashes=True, glasses=True)

CHARS = {
    "R": dict(voice="en-US-EmmaMultilingualNeural", el_voice="FGY2WhTYpPnrIDTdsKH5", look=ROSA),    # Laura
    "K": dict(voice="en-US-AndrewNeural", el_voice="IKne3meq5aSn9XLyUdCD", look=KAI),               # Charlie
    "C": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal", look=CRAIG),  # Eric
    "P": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=PATEL),        # Brian
    "M": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX", look=MOM),             # Matilda
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ Haus
def house(banner=True):
    def make():
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
        cr = cairo.Context(s)
        g = cairo.LinearGradient(0, 0, 0, 1100)
        g.add_color_stop_rgb(0, *rgb("#7EC8F2")); g.add_color_stop_rgb(1, *rgb("#DDF3FB"))
        cr.set_source(g); cr.paint()
        cr.arc(900, 400, 70, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#FFE58A")); cr.fill()
        # Haus
        cr.rectangle(120, 760, 700, 500); fill_stroke(cr, rgb("#F1E1C6"), 6)
        cr.move_to(80, 770); cr.line_to(470, 470); cr.line_to(860, 770); cr.close_path(); fill_stroke(cr, rgb("#8E3B2E"), 6)
        for (x, y) in ((180, 860), (620, 860)):
            cr.rectangle(x, y, 140, 120); fill_stroke(cr, rgb("#BFE3F2"), 5)
            cr.move_to(x + 70, y); cr.line_to(x + 70, y + 120); stroke_black(cr, 3)
        cr.rectangle(410, 1010, 120, 250); fill_stroke(cr, rgb("#5E3D24"), 5)
        cr.arc(505, 1140, 7, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#E5B94E")); cr.fill()
        # Rasen + Weg
        cr.rectangle(0, 1250, 1080, 670); cr.set_source_rgb(*rgb("#7CC35A")); cr.fill()
        cr.move_to(420, 1260); cr.line_to(520, 1260); cr.line_to(640, 1920); cr.line_to(300, 1920); cr.close_path()
        cr.set_source_rgb(*rgb("#D9CBB3")); cr.fill()
        # Briefkasten
        cr.move_to(90, 1420); cr.line_to(90, 1250); stroke_black(cr, 8)
        rrect(cr, 30, 1180, 140, 80, 20); fill_stroke(cr, rgb("#2F4F8F"), 4)
        _text(cr, "C. DUNN", 100, 1232, 22, (1, 1, 1))
        if banner:
            rrect(cr, 150, 640, 640, 90, 10); fill_stroke(cr, rgb("#FFE14D"), 4)
            _text(cr, "MANDATORY TEAM BUILDING", 470, 700, 38, rgb("#B3261E"))
        s.flush()
        return s
    return make


def truck(cr):
    cr.rectangle(780, 900, 300, 370); fill_stroke(cr, (1, 1, 1), 5)
    _text(cr, "U-MOVE", 930, 1010, 44, rgb("#E2572B"))
    cr.rectangle(800, 1060, 260, 200); cr.set_source_rgb(*rgb("#3A3F48")); cr.fill()
    for (x, y, w, h) in ((815, 1150, 90, 100), (915, 1180, 70, 70), (995, 1120, 60, 130)):
        cr.rectangle(x, y, w, h); fill_stroke(cr, rgb("#C9A27A"), 3)
    cr.arc(840, 1280, 34, 0, 2 * math.pi); cr.arc(1040, 1280, 34, 0, 2 * math.pi); cr.set_source_rgb(0.1, 0.1, 0.1); cr.fill()


def boxes(cr, n=5, x0=620, y0=1560):
    random.seed(2)
    for k in range(n):
        x = x0 + (k % 3) * 120 - 40 * (k // 3)
        y = y0 - (k // 3) * 90
        cr.rectangle(x, y - 90, 110, 90); fill_stroke(cr, rgb("#C9A27A"), 4)
        cr.move_to(x + 55, y - 90); cr.line_to(x + 55, y - 60); cr.set_source_rgb(*rgb("#8C6A4F")); cr.set_line_width(4); cr.stroke()


def couch(cr, x, y, w=330):
    rrect(cr, x - w / 2, y - 80, w, 80, 16); fill_stroke(cr, rgb("#5C86C8"), 5)
    rrect(cr, x - w / 2, y - 140, w, 70, 16); fill_stroke(cr, rgb("#4F78B8"), 5)


def lawn_chair(cr, x=200, y=1700):
    cr.move_to(x - 90, y); cr.line_to(x + 60, y - 160); cr.move_to(x + 90, y); cr.line_to(x - 60, y - 160)
    stroke_black(cr, 6)
    rrect(cr, x - 100, y - 200, 200, 40, 10); fill_stroke(cr, rgb("#F7A1B5"), 4)


def lemonade(cr, x, y):
    cr.move_to(x - 18, y - 60); cr.line_to(x + 18, y - 60); cr.line_to(x + 14, y); cr.line_to(x - 14, y); cr.close_path()
    cr.set_source_rgba(1, 0.92, 0.4, 0.9); cr.fill_preserve(); stroke_black(cr, 2)


def carry_scene(cr, t, x_start=-300, speed=180, y=1750, with_boss=True, struggle=False):
    l = lt()
    x = x_start + l * speed
    ph = l * 7
    if with_boss:
        lawn_chair(cr, 880, 1840)
        anim.actor(cr, "C", CRAIG, 860, 1980, 0.8, -1, pose="mug", emotion="smug", t=t, sit=True, prop="mug")
    anim.actor(cr, "K", KAI, x, y, 0.85, 1, pose="carry", emotion="worried" if struggle else "annoyed", t=t, walk=ph,
               shiver=0.5 if struggle else 0.0)
    anim.actor(cr, "R", ROSA, x + 340, y, 0.85, 1, pose="carry", emotion="annoyed", t=t, walk=ph + math.pi)
    couch(cr, x + 170, y - 440 + (math.sin(l * 12) * 10 if struggle else 0), 380)


def cold(cr, t):
    carry_scene(cr, t)


def stamp(s_):
    return lambda cr, t: MU.stamp(cr, s_)


BG = {"house": house(True), "house_plain": house(False), "office": B.boss_office, "open": B.open_office}

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def h1(cid, x=540, facing=1, bg="house", extra=None, after=None):
    d = dict(bg=bg, layers=[("fn", truck), ("fn", lambda cr: boxes(cr, 3, 640, 1560)), ("char", cid, x, Y1, S1, facing)] + (extra or []))
    if after:
        d["front"] = after
    return d


def h2(a, b_, bg="house"):
    return dict(bg=bg, layers=[("fn", truck), ("char", a, 230, Y2, S2, 1), ("char", b_, 560, Y2, S2, -1)])


def h3(a, m, c, bg="house"):
    return dict(bg=bg, layers=[("fn", truck), ("char", a, 150, Y2, 0.9, 1), ("char", m, 430, Y2, 0.9, -1), ("char", c, 700, Y2, 0.9, -1)])


SHOTS = {
    "cold": dict(bg="house", overlays=[cold], layers=[("fn", truck)]),
    "earlier": dict(bg="open", layers=[], front=[stamp("3 DAYS EARLIER")]),
    "open_C": dict(bg="open", layers=[("char", "C", 540, Y1, S1, 1)]),
    "open_RK": dict(bg="open", layers=[("char", "K", 300, Y2, S2, 1), ("char", "R", 780, Y2, S2, -1)]),
    "open_CRK": dict(bg="open", layers=[("char", "C", 210, Y2, 0.9, 1), ("char", "R", 545, Y2, 0.9, -1), ("char", "K", 875, Y2, 0.9, -1)]),
    "arrive_RK": h2("K", "R"),
    "house_C": h1("C", 380, 1),
    "house_R": h1("R", 380, 1),
    "house_K": h1("K", 380, 1),
    "house_CR": h2("C", "R"),
    "house_CK": h2("C", "K"),
    "carry": dict(bg="house", overlays=[lambda cr, t: carry_scene(cr, t, -350, 160, with_boss=True, struggle=True)], layers=[("fn", truck)]),
    "house_M": h1("M", 380, 1),
    "house_CM": h2("C", "M"),
    "house_P": h1("P", 380, 1),
    "house_CP": h2("C", "P"),
    "house_CPM": h3("C", "P", "M"),
    "house_PRK": h3("P", "R", "K"),
    "plain_CP": h2("C", "P", bg="house_plain"),
    "end": dict(bg="house_plain", overlays=[lambda cr, t: (anim.actor(cr, "C", CRAIG, 300, 1760, 0.9, 1, pose="carry", emotion="worried",
                                                                      t=t, shiver=0.8), couch(cr, 420 + math.sin(t * 10) * 6, 1290))],
                layers=[("fn", truck), ("char", "R", 780, Y2, 0.95, -1)]),
}
