"""Serie: "Your boss parks in your reserved spot every day... so you call a tow truck"."""
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
HOOK_BASE = ["POV: Your boss parks in your reserved spot", "every day... so you call a tow truck"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
AVA = Look(shirt=(0.25, 0.60, 0.50), skin=(0.70, 0.52, 0.40), iris=(0.22, 0.14, 0.08), hair="long", hair_color=(0.20, 0.12, 0.08),
           outfit="blouse", shoes=True, lashes=True)
REX = Look(shirt=(0.15, 0.15, 0.18), skin=SKIN, iris=(0.30, 0.50, 0.75), hair="sidepart", hair_color=(0.92, 0.80, 0.45),
           outfit="suit", tie_color=(0.85, 0.15, 0.20), shoes=True, glasses=True)
MIKE = Look(shirt=(0.95, 0.55, 0.15), skin=(0.85, 0.68, 0.55), iris=(0.3, 0.3, 0.3), hair="bald", hair_color=(0.4, 0.3, 0.2),
            beard=(0.35, 0.25, 0.18), cap=True, outfit="hoodie", shoes=True)
SATO = Look(shirt=(0.20, 0.25, 0.40), skin=(0.93, 0.84, 0.70), iris=(0.2, 0.12, 0.08), hair="bob", hair_color=(0.08, 0.07, 0.08),
            outfit="suit", tie_color=(0.9, 0.9, 0.9), shoes=True, lashes=True)
BEN = Look(shirt=(0.55, 0.35, 0.70), skin=SKIN, iris=(0.3, 0.5, 0.3), hair="curly", hair_color=(0.45, 0.28, 0.15), outfit="hoodie", shoes=True)

CHARS = {
    "A": dict(voice="en-US-MichelleNeural", el_voice="EXAVITQu4vr4xnSDxMaL", look=AVA),        # Sarah
    "R": dict(voice="en-US-AndrewMultilingualNeural", el_voice="pNInz6obpgDQGcFmaJgB", look=REX),  # Adam
    "K": dict(voice="en-US-ChristopherNeural", el_voice="pqHfZKP75CvOlQylNhV4", look=MIKE),    # Bill
    "S": dict(voice="en-US-AriaNeural", el_voice="Xb7hH8MSUJpSbSDYk0k2", look=SATO),           # Alice
    "B": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=BEN),          # Will
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ Parkplatz
def lot(rain=False):
    def make():
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
        cr = cairo.Context(s)
        g = cairo.LinearGradient(0, 0, 0, 1000)
        if rain:
            g.add_color_stop_rgb(0, *rgb("#5E6B78")); g.add_color_stop_rgb(1, *rgb("#9AA6B2"))
        else:
            g.add_color_stop_rgb(0, *rgb("#8FD0F5")); g.add_color_stop_rgb(1, *rgb("#E3F4FB"))
        cr.set_source(g); cr.paint()
        # Gebäude
        cr.rectangle(0, 380, 1080, 820); cr.set_source_rgb(*rgb("#D7DCE2")); cr.fill()
        _text(cr, "NOVA DYNAMICS", 540, 470, 60, rgb("#2C4A6E"))
        for r in range(3):
            for c in range(6):
                cr.rectangle(60 + c * 170, 520 + r * 150, 130, 110)
                cr.set_source_rgb(*rgb("#9FC7DD" if not rain else "#7E97A8")); cr.fill_preserve()
                cr.set_source_rgb(*rgb("#5E6A78")); cr.set_line_width(4); cr.stroke()
        # Eingang
        cr.rectangle(420, 980, 240, 220); cr.set_source_rgb(*rgb("#B9D8EA")); cr.fill_preserve(); stroke_black(cr, 5)
        cr.move_to(540, 980); cr.line_to(540, 1200); stroke_black(cr, 4)
        # Asphalt
        cr.rectangle(0, 1200, 1080, 720); cr.set_source_rgb(*rgb("#4A4F57" if not rain else "#3E434A")); cr.fill()
        cr.rectangle(0, 1200, 1080, 26); cr.set_source_rgb(*rgb("#B8BEC6")); cr.fill()
        for x in (0, 360, 720, 1080):
            cr.move_to(x, 1260); cr.line_to(x - 60, 1700)
        cr.set_source_rgb(1, 1, 1); cr.set_line_width(8); cr.stroke()
        # Schild
        cr.move_to(900, 1260); cr.line_to(900, 1060); stroke_black(cr, 8)
        rrect(cr, 790, 880, 220, 190, 10); fill_stroke(cr, (1, 1, 1), 5, rgb("#1F3B63"))
        _text(cr, "RESERVED", 900, 930, 34, rgb("#1F3B63"))
        _text(cr, "Employee of", 900, 972, 24, rgb("#1B1F27"), bold=False)
        _text(cr, "the Year", 900, 1002, 24, rgb("#1B1F27"), bold=False)
        _text(cr, "Violators towed", 900, 1046, 20, rgb("#B3261E"))
        s.flush()
        return s
    return make


def car(cr, x, y, col, plate=None, tilt=0.0, scale=1.0, sporty=True):
    """Seitenansicht, x/y = Mitte unten (Räder auf y)."""
    cr.save(); cr.translate(x, y); cr.rotate(tilt); cr.scale(scale, scale)
    if sporty:
        cr.move_to(-220, -40); cr.line_to(-210, -95); cr.curve_to(-120, -110, -80, -170, 10, -172)
        cr.curve_to(90, -172, 130, -120, 220, -105); cr.line_to(230, -40); cr.close_path()
    else:
        cr.move_to(-210, -40); cr.line_to(-205, -110); cr.line_to(-120, -115); cr.line_to(-80, -185); cr.line_to(110, -185)
        cr.line_to(150, -115); cr.line_to(215, -105); cr.line_to(220, -40); cr.close_path()
    fill_stroke(cr, rgb(col), 5)
    cr.move_to(-70, -118); cr.line_to(-30, -160); cr.line_to(80, -160); cr.line_to(110, -118); cr.close_path()
    cr.set_source_rgb(*rgb("#BFE3F2")); cr.fill_preserve(); stroke_black(cr, 3)
    for wx in (-130, 140):
        cr.arc(wx, -40, 42, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#1B1B1D")); cr.fill()
        cr.arc(wx, -40, 18, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#C9CED4")); cr.fill()
    if plate:
        rrect(cr, 150, -82, 80, 30, 4); fill_stroke(cr, (1, 1, 1), 2)
        _text(cr, plate, 190, -60, 18, rgb("#1B1F27"))
    cr.restore()


def red_car(cr, tilt=0.0, x=830, y=1500):
    car(cr, x, y, "#D7262E", "BOSS 1", tilt)


def ava_car(cr):
    car(cr, -60, 1830, "#5B8CFF", "AVA", 0, 0.8, sporty=False)


TOW_START = 1.0


def tow_truck(cr, x, y, lift=0.0):
    cr.save(); cr.translate(x, y); cr.scale(1.15, 1.15)
    rrect(cr, -380, -220, 200, 180, 14); fill_stroke(cr, rgb("#F2B705"), 5)
    cr.rectangle(-360, -200, 120, 80); cr.set_source_rgb(*rgb("#BFE3F2")); cr.fill_preserve(); stroke_black(cr, 3)
    cr.rectangle(-180, -110, 300, 70); fill_stroke(cr, rgb("#E2A100"), 5)
    _text(cr, "BIG MIKE'S TOWING", -40, -62, 26, rgb("#1B1F27"))
    cr.move_to(80, -110); cr.line_to(80 + 120 * math.cos(-0.6 - lift * 0.4), -110 + 120 * math.sin(-0.6 - lift * 0.4))
    stroke_black(cr, 12)
    cr.arc(-120, -40, 46, 0, 2 * math.pi); cr.arc(60, -40, 46, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#1B1B1D")); cr.fill()
    on = int(bgm.CLOCK["t"] * 4) % 2 == 0
    rrect(cr, -330, -250, 100, 26, 8); cr.set_source_rgb(*(rgb("#FF9F1A") if on else rgb("#8A5A00"))); cr.fill()
    cr.restore()


def hooked(cr, tx, lift):
    """Abschleppwagen bei tx + Auto am Haken (Heck angehoben, Drehpunkt Vorderrad)."""
    tow_truck(cr, tx, 1720)
    ang = 0.26 * lift
    fx = tx + 560
    rear_x = fx - 360 * math.cos(ang)
    rear_y = 1720 - 60 - 360 * math.sin(ang)
    bx, by = tx + 205, 1515
    cr.move_to(bx, by); cr.line_to(rear_x + 10, rear_y)
    cr.set_source_rgb(0.1, 0.1, 0.1); cr.set_line_width(5); cr.stroke()
    cr.save(); cr.translate(fx, 1720 - 2); cr.rotate(ang)
    car(cr, -140, 0, "#D7262E", "BOSS 1", 0)
    cr.restore()


def towing(cr, t):
    l = lt()
    lift = max(0.0, min(1.0, (l - TOW_START) / 1.5))
    drive = max(0.0, (l - 6.5) / 4.0)
    hooked(cr, 420 - drive * 1300, lift)


def cold_tow(cr, t):
    l = lt()
    hooked(cr, 380, max(0.0, min(1.0, l / 1.2)))
    if l > 1.0:
        anim.actor(cr, "R", REX, -120 + min(l - 1.0, 2.8) * 150, 1900, 0.72, 1, pose="panic", emotion="shocked", t=t,
                   walk=(l * 9))


def rain_fx(cr, t):
    random.seed(4)
    cr.set_source_rgba(0.85, 0.9, 1, 0.55); cr.set_line_width(3)
    for k in range(120):
        x = random.uniform(0, 1100); sp = random.uniform(900, 1300)
        y = (random.uniform(0, 1920) + t * sp) % 1920
        cr.move_to(x, y); cr.line_to(x - 10, y + 40)
    cr.stroke()


def stamp(s):
    def fn(cr, t):
        MU.stamp(cr, s)
    return fn


def lobby_room():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#E6E2DA"), rgb("#9A8C7E"), tiles="wood")
    B.window_city(cr, 60, 470, 520, 640)
    B.sun_beams(cr, 70, 480, 500, 640)
    B.plant(cr, 900, 1240, 0.9)
    s.flush()
    return s


BG = {"lot": lot(False), "rain": lot(True), "office": B.boss_office, "lobby": lobby_room}

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def lot_one(cid, x=300, facing=1, carfn=red_car, bg="lot", after=None):
    d = dict(bg=bg, layers=[("fn", carfn), ("char", cid, x, Y1, S1, facing)])
    if after:
        d["front"] = after
    return d


def lot_two(a, b_, carfn=red_car, bg="lot"):
    return dict(bg=bg, layers=[("fn", carfn), ("char", a, 180, Y2, 0.95, 1), ("char", b_, 450, Y2, 0.95, -1)])


def one(b, cid, x=540, facing=1, front=None, opts=None):
    return dict(bg=b, layers=[("char", cid, x, Y1, S1, facing, opts or {})] + ([("fn", front)] if front else []))


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])


SHOTS = {
    "cold": dict(bg="lot", overlays=[cold_tow], layers=[]),
    "earlier": dict(bg="lot", layers=[("fn", red_car)], front=[stamp("2 WEEKS EARLIER")]),
    "lot_A": lot_one("A"),
    "lot_AB": lot_two("B", "A"),
    "lot_AR": lot_two("R", "A"),
    "lot_R": lot_one("R"),
    "rain_A": dict(bg="rain", layers=[("fn", ava_car), ("char", "A", 600, Y1, S1, -1)], front=[rain_fx]),
    "lot_A_phone": lot_one("A"),
    "tow_AK": dict(bg="lot", layers=[("fn", red_car), ("char", "K", 180, Y2, 0.95, 1), ("char", "A", 450, Y2, 0.95, -1)]),
    "towing": dict(bg="lot", overlays=[towing], layers=[]),
    "tow_RK": dict(bg="lot", overlays=[lambda cr, t: hooked(cr, 380, 1.0)],
                   layers=[("char", "K", 130, Y2, 0.85, 1), ("char", "R", 370, Y2, 0.85, -1)]),
    "tow_R": dict(bg="lot", overlays=[lambda cr, t: hooked(cr, 380, 1.0)],
                  layers=[("char", "R", 260, Y1, 1.15, 1)]),
    "tow_K": dict(bg="lot", overlays=[lambda cr, t: hooked(cr, 380, 1.0)],
                  layers=[("char", "K", 260, Y1, 1.15, 1)]),
    "empty_R": dict(bg="lot", layers=[("char", "R", 540, Y1, S1, 1)]),
    "empty_RS": dict(bg="lot", layers=[("char", "R", 300, Y2, S2, 1), ("char", "S", 780, Y2, S2, -1)]),
    "empty_RA": dict(bg="lot", layers=[("fn", ava_car), ("char", "R", 300, Y2, S2, 1), ("char", "A", 780, Y2, S2, -1)]),
    "lobby_RA": two("lobby", "R", "A"),
    "lobby_SA": two("lobby", "A", "S"),
    "lobby_S": one("lobby", "S", 600, -1),
    "lobby_A": one("lobby", "A", 600, -1),
    "lobby_R": one("lobby", "R", 480, 1),
    "lobby_RSA": dict(bg="lobby", layers=[("char", "R", 210, Y2, 0.9, 1), ("char", "A", 545, Y2, 0.9, -1), ("char", "S", 875, Y2, 0.9, -1)]),
}
