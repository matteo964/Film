"""Serie: "Your wife goes into labor... and your boss says you can't leave the meeting"."""
import math

import cairo
import backgrounds as bgm
import backgrounds_v2 as B
import mailui as MU
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect, stroke_black

GAP = 0.15
HOOK_BASE = ["POV: Your wife goes into labor... and your", "boss says you can't leave the meeting"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
ETHAN = Look(shirt=(0.30, 0.45, 0.65), skin=(0.78, 0.60, 0.45), iris=(0.25, 0.17, 0.10), hair="buzz", hair_color=(0.10, 0.08, 0.07),
             outfit="suit", tie_color=(0.85, 0.85, 0.88), shoes=True)
MIA = Look(shirt=(0.75, 0.88, 0.92), skin=SKIN, iris=(0.30, 0.50, 0.30), hair="long", hair_color=(0.70, 0.45, 0.22),
           outfit="blouse", shoes=True, lashes=True)
DOUG = Look(shirt=(0.40, 0.18, 0.18), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="bald", hair_color=(0.45, 0.35, 0.25),
            moustache=True, outfit="suit", tie_color=(0.15, 0.15, 0.18), shoes=True)
TANAKA = Look(shirt=(0.12, 0.18, 0.30), skin=(0.93, 0.84, 0.70), iris=(0.2, 0.12, 0.08), hair="updo", hair_color=(0.75, 0.75, 0.78),
              outfit="suit", tie_color=(0.85, 0.20, 0.25), shoes=True, lashes=True, glasses=True)

CHARS = {
    "E": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=ETHAN),         # Will
    "W": dict(voice="en-US-AvaNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=MIA),              # Jessica
    "D": dict(voice="en-US-ChristopherNeural", el_voice="N2lVS1w4EtoT3dr4eOWO", look=DOUG),     # Callum
    "T": dict(voice="en-US-MichelleNeural", el_voice="hpp4J3VqNfWAUOO0d1Us", look=TANAKA),      # Bella
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ Handy-Chat
def chat_phone(msgs, title="Mia", start=0.0, per=1.1, typing_after=True):
    """msgs: Liste (text, von_mir?, rot?)."""
    def fn(cr, t):
        l = lt()
        cr.set_source_rgb(*rgb("#11151C")); cr.paint()
        x, y, w, h = 190, 450, 700, 1140
        rrect(cr, x, y, w, h, 60); cr.set_source_rgb(*rgb("#1B1F27")); cr.fill()
        rrect(cr, x + 22, y + 22, w - 44, h - 44, 44); cr.set_source_rgb(*rgb("#F4F6F8")); cr.fill()
        cr.rectangle(x + 22, y + 60, w - 44, 100); cr.set_source_rgb(*rgb("#E9EDF2")); cr.fill()
        cr.arc(x + 100, y + 110, 34, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#F7A1B5")); cr.fill()
        _text(cr, title[0], x + 100, y + 124, 36, (1, 1, 1))
        _text(cr, title, x + 160, y + 124, 36, rgb("#1B1F27"), center=False)
        n = max(0, min(len(msgs), int((l - start) / per) + 1)) if l >= start else 0
        yy = y + 210
        for text, mine, urgent in msgs[:n]:
            cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            cr.set_font_size(34)
            tw = min(500, cr.text_extents(text).x_advance + 50)
            bx = x + w - 60 - tw if mine else x + 60
            rrect(cr, bx, yy, tw, 76, 30)
            cr.set_source_rgb(*(rgb("#2F7BF6") if mine else (rgb("#E23B3B") if urgent else rgb("#E1E5EA")))); cr.fill()
            _text(cr, text, bx + 25, yy + 50, 34, (1, 1, 1) if (mine or urgent) else rgb("#1B1F27"), center=False)
            yy += 100
        if typing_after and n == len(msgs) and int(t * 3) % 2 == 0:
            rrect(cr, x + 60, yy, 120, 60, 30); cr.set_source_rgb(*rgb("#E1E5EA")); cr.fill()
            for k in range(3):
                cr.arc(x + 92 + k * 28, yy + 30, 8, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#6E7A88")); cr.fill()
    return fn


COLD_MSGS = [("My water just broke.", False, True), ("Contractions every 5 min", False, False), ("Ethan??", False, False),
             ("COME NOW", False, True)]
FIRED_MSGS = [("From: Doug", False, False), ("Leave = you're fired.", False, True), ("Return your laptop Monday.", False, False)]


# ------------------------------------------------------------------ Sets
def meeting_room():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#E6E2DA"), rgb("#9A8C7E"), tiles="wood")
    B.window_city(cr, 820, 470, 230, 640)
    sx, sy, sw, sh = 100, 450, 680, 420
    rrect(cr, sx, sy, sw, sh, 12); fill_stroke(cr, rgb("#1B1F27"), 8)
    cr.rectangle(sx + 18, sy + 18, sw - 36, sh - 36); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.rectangle(sx + 18, sy + 18, sw - 36, 64); cr.set_source_rgb(*rgb("#8E1F2F")); cr.fill()
    _text(cr, "TANAKA FOODS · PARTNERSHIP", sx + sw / 2, sy + 62, 28, (1, 1, 1))
    _text(cr, "Our values:", sx + sw / 2, sy + 180, 40, rgb("#1B1F27"))
    _text(cr, "FAMILY FIRST", sx + sw / 2, sy + 260, 60, rgb("#8E1F2F"))
    rrect(cr, 60, 1300, 960, 44, 12); fill_stroke(cr, rgb("#F2F2F2"), 5, rgb("#6E6E6E"))
    cr.rectangle(120, 1344, 840, 120); cr.set_source_rgba(0, 0, 0, 0.08); cr.fill()
    s.flush()
    return s


def hospital():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#CFE8E4"), rgb("#D9DEE4"), tiles="tile")
    B.window_city(cr, 700, 480, 330, 520)
    B.sun_beams(cr, 710, 490, 320, 520, ang=-0.45, alpha=0.18)
    # Monitor
    rrect(cr, 90, 560, 200, 150, 12); fill_stroke(cr, rgb("#1B1F27"), 5)
    cr.move_to(110, 650); cr.line_to(150, 650); cr.line_to(165, 600); cr.line_to(185, 690); cr.line_to(200, 650); cr.line_to(270, 650)
    cr.set_source_rgb(*rgb("#5BEA8B")); cr.set_line_width(5); cr.stroke()
    cr.move_to(190, 710); cr.line_to(190, 1250); stroke_black(cr, 6)
    s.flush()
    return s


def bed_back(cr):
    rrect(cr, 120, 1030, 70, 330, 20); fill_stroke(cr, rgb("#B8C4CF"), 5)


def bed_front(cr):
    rrect(cr, 150, 1300, 640, 90, 20); fill_stroke(cr, (1, 1, 1), 5, rgb("#8C96A3"))
    cr.move_to(330, 1300); cr.curve_to(450, 1250, 650, 1250, 790, 1300); cr.line_to(790, 1390); cr.line_to(330, 1390); cr.close_path()
    fill_stroke(cr, rgb("#9FC8F0"), 4)
    cr.rectangle(180, 1390, 20, 170); cr.rectangle(740, 1390, 20, 170); cr.set_source_rgb(*rgb("#8C96A3")); cr.fill()


def baby(cr, x, y, s=1.0):
    cr.save(); cr.translate(x, y); cr.scale(s, s)
    cr.save(); cr.scale(70, 42); cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
    fill_stroke(cr, rgb("#FFF2B3"), 4)
    cr.arc(-48, -6, 26, 0, 2 * math.pi); fill_stroke(cr, rgb("#F6DCC4"), 3)
    for dx in (-56, -42):
        cr.arc(dx, -10, 3, 0, 2 * math.pi); cr.set_source_rgb(0.1, 0.1, 0.1); cr.fill()
    cr.restore()


def with_baby(x, y, s=1.0):
    return lambda cr: baby(cr, x, y, s)


def stamp(s_):
    return lambda cr, t: MU.stamp(cr, s_)


BG = {"meet": meeting_room, "hosp": hospital, "dark": None, "hall": None}


def _dark():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    c = cairo.Context(s); c.set_source_rgb(*rgb("#11151C")); c.paint(); s.flush()
    return s


def _hall():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#CFE8E4"), rgb("#D9DEE4"), tiles="tile")
    _text(cr, "MATERNITY WARD", 540, 520, 54, rgb("#2F7D6F"))
    for x in (120, 760):
        rrect(cr, x, 640, 200, 600, 8); fill_stroke(cr, rgb("#F4F6F8"), 5, rgb("#8C96A3"))
    s.flush()
    return s


BG["dark"] = _dark
BG["hall"] = _hall

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def one(b, cid, x=540, facing=1, opts=None, front=None, after=None):
    d = dict(bg=b, layers=[("char", cid, x, Y1, S1, facing, opts or {})] + ([("fn", front)] if front else []))
    if after:
        d["front"] = after
    return d


def two(b, left, right, front=None):
    return dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)] + ([("fn", front)] if front else []))


def three(b, a, m, c):
    return dict(bg=b, layers=[("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, -1), ("char", c, 875, Y2, 0.9, -1)])


def bed_scene(extra=(), baby_on=False):
    layers = [("fn", bed_back), ("char", "W", 300, 1560, 1.0, 1, dict(sit=True)), ("fn", bed_front)]
    if baby_on:
        layers.append(("fn", with_baby(420, 1120, 1.0)))
    layers += list(extra)
    return dict(bg="hosp", layers=layers)


SHOTS = {
    "cold": dict(bg="dark", overlays=[chat_phone(COLD_MSGS, start=0.2, per=1.0)], layers=[]),
    "meet_DE": two("meet", "D", "E"),
    "meet_D": one("meet", "D", 880, -1),
    "meet_E": one("meet", "E", 880, -1),
    "meet_T": one("meet", "T", 880, -1),
    "meet_DET": three("meet", "D", "E", "T"),
    "meet_DT": two("meet", "D", "T"),
    "hall_E": one("hall", "E", 540, 1, opts=dict()),
    "bed_EW": bed_scene([("char", "E", 820, Y2, S2, -1)]),
    "fired": dict(bg="dark", overlays=[chat_phone(FIRED_MSGS, title="Doug (Boss)", start=0.2, per=1.0, typing_after=False)], layers=[]),
    "bed_W": bed_scene(),
    "baby_EW": bed_scene([("char", "E", 820, Y2, S2, -1), ("fn", with_baby(720, 1180, 0.9))]),
    "baby_TE": bed_scene([("char", "T", 640, Y2, 0.9, -1), ("char", "E", 880, Y2, 0.9, -1), ("fn", with_baby(790, 1240, 0.8))]),
    "baby_DE": bed_scene([("char", "D", 640, Y2, 0.9, 1), ("char", "E", 900, Y2, 0.9, -1), ("fn", with_baby(820, 1240, 0.8))]),
    "hosp_T": one("hosp", "T", 880, -1),
    "hosp_D": one("hosp", "D", 880, -1),
    "hosp_E": one("hosp", "E", 880, -1, front=with_baby(800, 1110, 1.1)),
}
