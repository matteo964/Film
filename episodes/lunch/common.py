"""Gemeinsame Besetzung/Sets: "Someone keeps stealing your lunch... so you set a trap"."""
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
HOOK_BASE = ["POV: Someone keeps stealing your lunch...", "so you set a trap"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
RED = (0.96, 0.42, 0.38)
MILO = Look(shirt=(0.20, 0.55, 0.45), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="spiky", hair_color=(0.10, 0.08, 0.07),
            outfit="hoodie", shoes=True)
JADE = Look(shirt=(0.85, 0.40, 0.55), skin=(0.90, 0.78, 0.62), iris=(0.22, 0.14, 0.08), hair="long", hair_color=(0.06, 0.05, 0.06),
            outfit="blouse", shoes=True, lashes=True, glasses=True)
GARY = Look(shirt=(0.18, 0.22, 0.40), skin=SKIN, iris=(0.35, 0.45, 0.60), hair="sidepart", hair_color=(0.60, 0.60, 0.62),
            outfit="suit", tie_color=(0.95, 0.70, 0.20), shoes=True)
GARY_RED = Look(shirt=(0.18, 0.22, 0.40), skin=RED, iris=(0.35, 0.45, 0.60), hair="sidepart", hair_color=(0.60, 0.60, 0.62),
                outfit="suit", tie_color=(0.95, 0.70, 0.20), shoes=True)
BRENDA = Look(shirt=(0.60, 0.40, 0.75), skin=SKIN, iris=(0.30, 0.50, 0.30), hair="updo", hair_color=(0.75, 0.30, 0.15),
              outfit="blouse", shoes=True, lashes=True)
KEVIN = Look(shirt=(0.40, 0.40, 0.45), skin=(0.70, 0.52, 0.40), iris=(0.22, 0.14, 0.08), hair="buzz", hair_color=(0.06, 0.05, 0.05),
             outfit="hoodie", shoes=True, glasses=True)
ZAC = Look(shirt=(0.95, 0.75, 0.30), skin=SKIN, iris=(0.30, 0.55, 0.85), hair="curly", hair_color=(0.92, 0.80, 0.50),
           outfit="blouse", shoes=True)
CLIENT = Look(shirt=(0.15, 0.15, 0.18), skin=(0.48, 0.33, 0.24), iris=(0.2, 0.12, 0.08), hair="bald", hair_color=(0.2, 0.2, 0.2),
              beard=(0.15, 0.12, 0.10), outfit="suit", tie_color=(0.75, 0.15, 0.20), shoes=True)

CHARS = {
    "M": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=MILO),        # Will
    "J": dict(voice="en-US-AvaNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=JADE),           # Jessica
    "G": dict(voice="en-US-ChristopherNeural", el_voice="cjVigY5qzO86Huf0OWal", look=GARY),   # Eric
    "B": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX", look=BRENDA),    # Matilda
    "K": dict(voice="en-US-AndrewMultilingualNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=KEVIN),  # Liam
    "Z": dict(voice="en-US-AndrewNeural", el_voice="IKne3meq5aSn9XLyUdCD", look=ZAC),         # Charlie
    "C": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=CLIENT), # Brian
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ Küche + Kühlschrank
def kitchen():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#E9F0E6"), rgb("#D7DCE2"), tiles="tile")
    # Hängeschränke
    for k in range(3):
        rrect(cr, 60 + k * 230, 470, 210, 230, 8)
        fill_stroke(cr, rgb("#F7F4EE"), 4, rgb("#9AA6B2"))
        cr.rectangle(150 + k * 230, 660, 30, 8); cr.set_source_rgb(*rgb("#9AA6B2")); cr.fill()
    # Arbeitsplatte
    rrect(cr, 40, 1150, 660, 30, 6); fill_stroke(cr, rgb("#5E6A78"), 4)
    cr.rectangle(60, 1180, 620, 380); fill_stroke(cr, rgb("#F7F4EE"), 4, rgb("#9AA6B2"))
    # Mikrowelle + Kaffeemaschine
    rrect(cr, 90, 1010, 220, 140, 10); fill_stroke(cr, rgb("#2B2F38"), 4)
    rrect(cr, 110, 1030, 140, 100, 6); cr.set_source_rgb(*rgb("#3F4757")); cr.fill()
    rrect(cr, 420, 990, 120, 160, 10); fill_stroke(cr, rgb("#B0302A"), 4)
    s.flush()
    return s


NOTES = {"please": ("PLEASE STOP", "#FFE14D"), "reply": ("Delicious. Thanks :)", "#9BE7FF")}


def fridge(cr, open_=False, lunch=True, note=None, trap=False):
    x, y, w, h = 730, 640, 320, 920
    if open_:
        rrect(cr, x, y, w, h, 16); fill_stroke(cr, rgb("#F4F7FA"), 5, rgb("#8C96A3"))
        cr.rectangle(x + 16, y + 16, w - 32, h - 32); cr.set_source_rgb(*rgb("#EAF6FF")); cr.fill()
        gl = cairo.RadialGradient(x + w / 2, y + 120, 10, x + w / 2, y + 120, 380)
        gl.add_color_stop_rgba(0, 1, 1, 0.9, 0.7); gl.add_color_stop_rgba(1, 1, 1, 0.9, 0)
        cr.set_source(gl); cr.rectangle(x + 16, y + 16, w - 32, h - 32); cr.fill()
        for k in range(4):
            cr.rectangle(x + 20, y + 230 + k * 170, w - 40, 8); cr.set_source_rgb(*rgb("#C9D3E6")); cr.fill()
        for (dx, dy, c) in ((40, 300, "#F2C230"), (200, 120, "#E23B3B"), (60, 470, "#5AC05A")):
            rrect(cr, x + dx, y + dy, 70, 100, 10); fill_stroke(cr, rgb(c), 3)
        if lunch:
            lunchbox(cr, x + 110, y + 560, trap)
        # Tür
        cr.move_to(x, y); cr.line_to(x - 120, y + 60); cr.line_to(x - 120, y + h - 60); cr.line_to(x, y + h); cr.close_path()
        fill_stroke(cr, rgb("#D9DEE4"), 5, rgb("#8C96A3"))
    else:
        rrect(cr, x, y, w, h, 16); fill_stroke(cr, rgb("#E6EAEF"), 5, rgb("#8C96A3"))
        cr.move_to(x, y + 330); cr.line_to(x + w, y + 330); cr.set_source_rgb(*rgb("#8C96A3")); cr.set_line_width(4); cr.stroke()
        for yy in (y + 150, y + 470):
            rrect(cr, x + 26, yy, 18, 140, 8); cr.set_source_rgb(*rgb("#9AA6B2")); cr.fill()
        if note:
            txt, col = NOTES[note]
            cr.save(); cr.translate(x + 170, y + 560); cr.rotate(-0.06)
            cr.rectangle(-120, -90, 240, 180); cr.set_source_rgb(*rgb(col)); cr.fill()
            _text(cr, txt.split(" ")[0] if len(txt) > 12 else txt, 0, -10, 30 if len(txt) <= 12 else 26, rgb("#1B1F27"), font="DejaVu Sans")
            if len(txt) > 12:
                _text(cr, " ".join(txt.split(" ")[1:]), 0, 34, 26, rgb("#1B1F27"), font="DejaVu Sans")
            cr.restore()
        # Kamera oben
        rrect(cr, x + w - 90, y - 50, 70, 40, 8); fill_stroke(cr, rgb("#2B2F38"), 3)
        cr.arc(x + w - 55, y - 30, 10, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#FF3B30")); cr.fill()


def lunchbox(cr, x, y, trap=False):
    rrect(cr, x, y, 120, 80, 12); fill_stroke(cr, rgb("#FFFFFF"), 3)
    cr.rectangle(x + 8, y + 26, 104, 46); cr.set_source_rgb(*(rgb("#C0392B") if trap else rgb("#E58E3A"))); cr.fill()
    rrect(cr, x + 6, y - 22, 108, 26, 6); cr.set_source_rgb(*rgb("#FFE14D")); cr.fill()
    _text(cr, "MILO'S", x + 60, y - 3, 18, rgb("#1B1F27"))


def kit(open_=False, lunch=True, note=None, trap=False):
    return lambda cr: fridge(cr, open_, lunch, note, trap)


# ------------------------------------------------------------------ Kühlschrank-Kamera
def fridgecam(cr, t, blurred=True, time_s="12:31:07", label=None):
    cr.set_source_rgb(*rgb("#0B0E14")); cr.paint()
    x, y, w, h = 30, 470, 1020, 900
    cr.save(); cr.rectangle(x, y, w, h); cr.clip()
    cr.set_source_rgb(*rgb("#3B4A40")); cr.paint()
    # Kühlschrankinneres
    cr.rectangle(x + 120, y + 80, 780, 760); cr.set_source_rgb(*rgb("#6F8072")); cr.fill()
    for k in range(3):
        cr.rectangle(x + 120, y + 300 + k * 180, 780, 10); cr.set_source_rgb(*rgb("#8FA092")); cr.fill()
    rrect(cr, x + 380, y + 400, 240, 150, 14); cr.set_source_rgb(*rgb("#C9CFC9")); cr.fill()
    cr.rectangle(x + 392, y + 356, 216, 46); cr.set_source_rgb(*rgb("#D8D88A")); cr.fill()
    _text(cr, "MILO'S LUNCH", x + 500, y + 390, 30, rgb("#1B1F27"))
    _text(cr, "DO NOT EAT", x + 500, y + 500, 28, rgb("#3A3A3A"))
    # Arm + Hand
    cr.move_to(x + w + 40, y + 300); cr.curve_to(x + 820, y + 360, x + 720, y + 420, x + 640, y + 470)
    cr.set_source_rgb(*rgb("#2F3540")); cr.set_line_width(60); cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
    cr.arc(x + 630, y + 470, 40, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#B8AFA6")); cr.fill()
    # Gesicht am Rand
    fx, fy = x + 900, y + 170
    if blurred:
        random.seed(3)
        for i in range(6):
            for j in range(6):
                cr.rectangle(fx - 120 + i * 40, fy - 120 + j * 40, 40, 40)
                g = random.uniform(0.45, 0.75)
                cr.set_source_rgb(g, g * 0.95, g * 0.9); cr.fill()
    else:
        cr.arc(fx, fy, 115, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#C9C2BA")); cr.fill()
        cr.move_to(fx - 115, fy - 20); cr.curve_to(fx - 110, fy - 140, fx + 60, fy - 150, fx + 115, fy - 60)
        cr.line_to(fx + 30, fy - 70); cr.close_path(); cr.set_source_rgb(*rgb("#8E8E90")); cr.fill()
        for dx in (-40, 20):
            cr.arc(fx + dx, fy, 16, 0, 2 * math.pi); cr.set_source_rgb(1, 1, 1); cr.fill()
            cr.arc(fx + dx - 6, fy, 7, 0, 2 * math.pi); cr.set_source_rgb(0.1, 0.1, 0.1); cr.fill()
        cr.move_to(fx - 40, fy + 60); cr.line_to(fx + 10, fy + 55); cr.set_source_rgb(0.1, 0.1, 0.1); cr.set_line_width(5); cr.stroke()
        cr.move_to(fx - 6, fy + 115); cr.line_to(fx - 10, fy + 230); cr.set_source_rgb(*rgb("#E5A93A")); cr.set_line_width(26); cr.stroke()
    cr.set_source_rgba(0, 0, 0, 0.14)
    for yy in range(int(y), int(y + h), 6):
        cr.rectangle(x, yy, w, 2); cr.fill()
    cr.restore()
    cr.arc(x + 40, y + 40, 12, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#FF3B30")); cr.fill()
    _text(cr, "FRIDGE CAM 01", x + 64, y + 52, 30, (1, 1, 1), font="DejaVu Sans Mono", center=False)
    _text(cr, time_s, x + w - 20 - 18 * len(time_s), y + 52, 30, (1, 1, 1), font="DejaVu Sans Mono", center=False)
    if label:
        rrect(cr, 140, 1270, 800, 80, 14); cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
        _text(cr, label, 540, 1323, 38, (1, 1, 1))


def cold(cr, t):
    fridgecam(cr, t, True, "DAY 23 · 12:31:07", "THE LUNCH THIEF")


def cam_reveal(cr, t):
    fridgecam(cr, t, lt() < 1.6, "DAY 24 · 12:30:52", "UNBLURRED" if lt() >= 1.6 else None)


# ------------------------------------------------------------------ Ermittlungstafel
SUSPECTS = [("BRENDA", "\"on a diet\"", BRENDA), ("KEVIN", "eats everything", KEVIN), ("ZAC", "the intern", ZAC)]


def corkboard(crossed=0):
    def fn(cr, t=0):
        x, y, w, h = 40, 440, 680, 560
        rrect(cr, x - 12, y - 12, w + 24, h + 24, 10); fill_stroke(cr, rgb("#8A6446"), 5)
        cr.rectangle(x, y, w, h); cr.set_source_rgb(*rgb("#C79A6B")); cr.fill()
        _text(cr, "WHO IS THE LUNCH THIEF?", x + w / 2, y + 56, 34, rgb("#1B1F27"), font="DejaVu Sans")
        pts = []
        for k, (name, sub, lk) in enumerate(SUSPECTS):
            px, py = x + 60 + k * 210, y + 120
            cr.rectangle(px, py, 170, 210); cr.set_source_rgb(1, 1, 1); cr.fill()
            cr.save(); cr.rectangle(px + 10, py + 10, 150, 150); cr.clip()
            cr.set_source_rgb(*rgb("#DCE3EA")); cr.paint()
            from stickman import draw_figure, POSES
            draw_figure(cr, lk, px + 85, py + 95 + 770 * 0.55, 0.55, 1,
                        dict(hands=POSES["idle"], emotion="neutral"), 0)
            cr.restore()
            _text(cr, name, px + 85, py + 190, 24, rgb("#1B1F27"))
            _text(cr, sub, px + 85, py + 250, 22, rgb("#3B2A1A"), bold=False)
            cr.arc(px + 85, py - 4, 10, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
            pts.append((px + 85, py - 4))
            if k < crossed:
                cr.move_to(px + 10, py + 10); cr.line_to(px + 160, py + 160)
                cr.move_to(px + 160, py + 10); cr.line_to(px + 10, py + 160)
                cr.set_source_rgb(*rgb("#E23B3B")); cr.set_line_width(12); cr.stroke()
        # Fäden
        q = (x + w / 2, y + 470)
        cr.arc(q[0], q[1], 46, 0, 2 * math.pi); cr.set_source_rgb(1, 1, 1); cr.fill()
        _text(cr, "?", q[0], q[1] + 22, 60, rgb("#E23B3B"))
        for p in pts:
            cr.move_to(*p); cr.line_to(q[0], q[1] - 46)
        cr.set_source_rgb(*rgb("#D0222A")); cr.set_line_width(4); cr.stroke()
    return fn


def day_stamp(s):
    def fn(cr, t):
        import cairo as _c
        cr.select_font_face("Bebas Neue", _c.FONT_SLANT_NORMAL, _c.FONT_WEIGHT_NORMAL)
        cr.set_font_size(96)
        e = cr.text_extents(s)
        rrect(cr, (1080 - e.x_advance) / 2 - 30, 450, e.x_advance + 60, 120, 20)
        cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
        cr.move_to((1080 - e.x_advance) / 2, 545); cr.set_source_rgb(1, 1, 1); cr.show_text(s)
    return fn


def sweat(cr, t):
    """Schweißtropfen + Dampf über Garys Kopf (Einzel-Einstellung rechts, x=880)."""
    for k in range(4):
        ph = (t * 1.3 + k * 0.25) % 1
        x = 760 + k * 70
        y = 620 + ph * 160
        cr.move_to(x, y); cr.curve_to(x - 14, y + 26, x + 14, y + 26, x, y)
        cr.set_source_rgba(0.55, 0.80, 1.0, 1 - ph); cr.fill()
    for k in range(3):
        ph = (t * 0.9 + k / 3) % 1
        cr.arc(820 + k * 60, 520 - ph * 120, 22 + ph * 30, 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, 0.5 * (1 - ph)); cr.fill()


def glass_room():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#DCE3EA"), rgb("#8D9AA8"), tiles="wood")
    rrect(cr, 100, 450, 680, 420, 12); fill_stroke(cr, rgb("#1B1F27"), 8)
    cr.rectangle(118, 468, 644, 384); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.rectangle(118, 468, 644, 60); cr.set_source_rgb(*rgb("#1F3B63")); cr.fill()
    _text(cr, "PARTNERSHIP PROPOSAL · HALE FOODS", 440, 508, 26, (1, 1, 1))
    _text(cr, "Our people come first.", 440, 680, 44, rgb("#1F3B63"))
    rrect(cr, 60, 1300, 960, 44, 12); fill_stroke(cr, rgb("#F2F2F2"), 5, rgb("#6E6E6E"))
    # Wassergläser
    for x in (420, 640):
        cr.move_to(x - 22, 1250); cr.line_to(x + 22, 1250); cr.line_to(x + 16, 1300); cr.line_to(x - 16, 1300); cr.close_path()
        cr.set_source_rgba(0.7, 0.85, 1, 0.8); cr.fill()
    s.flush()
    return s


BG = {"kitchen": kitchen, "open": B.open_office, "glass": glass_room, "dark": lambda: _dark()}


def _dark():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    c = cairo.Context(s); c.set_source_rgb(*rgb("#0B0E14")); c.paint(); s.flush()
    return s


Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def k1(cid, x=380, facing=1, **kw):
    return dict(bg="kitchen", layers=[("char", cid, x, Y1, S1, facing), ("fn", kit(**kw))])


def k2(a, b_, **kw):
    return dict(bg="kitchen", layers=[("char", a, 230, Y2, S2, 1), ("char", b_, 520, Y2, S2, -1), ("fn", kit(**kw))])


SHOTS = {
    "cold": dict(bg="dark", overlays=[cold], layers=[]),
    "day1": dict(bg="kitchen", layers=[("char", "M", 380, Y1, S1, 1), ("fn", kit(open_=True, lunch=False))], front=[day_stamp("DAY 1")]),
    "day7": dict(bg="kitchen", layers=[("char", "M", 380, Y1, S1, 1), ("fn", kit(note="please"))], front=[day_stamp("DAY 7")]),
    "day15": dict(bg="kitchen", layers=[("char", "M", 380, Y1, S1, 1), ("fn", kit(note="reply"))], front=[day_stamp("DAY 15")]),
    "kit_MJ": k2("M", "J"),
    "kit_MJ_trap": k2("M", "J", open_=True, trap=True),
    "board_MJ": dict(bg="open", layers=[("fn", corkboard(0)), ("char", "M", 800, Y2, 0.95, -1), ("char", "J", 960, Y2, 0.95, -1)]),
    "board_M": dict(bg="open", layers=[("fn", corkboard(0)), ("char", "M", 880, Y1, S1, -1)]),
    "gone_M": dict(bg="kitchen", layers=[("char", "M", 380, Y1, S1, 1), ("fn", kit(open_=True, lunch=False))], front=[day_stamp("12:31 PM")]),
    "board1_J": dict(bg="open", layers=[("fn", corkboard(1)), ("char", "J", 880, Y1, S1, -1)]),
    "board2_M": dict(bg="open", layers=[("fn", corkboard(2)), ("char", "M", 880, Y1, S1, -1)]),
    "board3_MJ": dict(bg="open", layers=[("fn", corkboard(3)), ("char", "M", 800, Y2, 0.95, -1), ("char", "J", 960, Y2, 0.95, -1)]),
    "open_JB": dict(bg="open", layers=[("char", "J", 300, Y2, S2, 1), ("char", "B", 780, Y2, S2, -1)]),
    "open_MK": dict(bg="open", layers=[("char", "M", 300, Y2, S2, 1), ("char", "K", 780, Y2, S2, -1)]),
    "open_JZ": dict(bg="open", layers=[("char", "J", 300, Y2, S2, 1), ("char", "Z", 780, Y2, S2, -1)]),
    "glass_GC": dict(bg="glass", layers=[("char", "G", 300, Y2, S2, 1), ("char", "C", 780, Y2, S2, -1)]),
    "glass_G": dict(bg="glass", layers=[("char", "G", 880, Y1, S1, -1)]),
    "glass_C": dict(bg="glass", layers=[("char", "C", 880, Y1, S1, -1)]),
    "red_G": dict(bg="open", layers=[("char", "G", 880, Y1, S1, -1, dict(look=GARY_RED, shiver=0.6))], front=[sweat]),
    "red_GMJ": dict(bg="open", layers=[("char", "G", 210, Y2, 0.9, 1, dict(look=GARY_RED, shiver=0.5)),
                                        ("char", "M", 545, Y2, 0.9, -1), ("char", "J", 875, Y2, 0.9, -1)]),
    "red_GC": dict(bg="glass", layers=[("char", "G", 300, Y2, S2, 1, dict(look=GARY_RED, shiver=0.5)), ("char", "C", 780, Y2, S2, -1)]),
    "cam_reveal": dict(bg="dark", overlays=[cam_reveal], layers=[]),
    "open_M": dict(bg="open", layers=[("char", "M", 880, Y1, S1, -1)]),
    "open_J": dict(bg="open", layers=[("char", "J", 880, Y1, S1, -1)]),
    "end_MG": dict(bg="kitchen", layers=[("char", "G", 230, Y2, S2, 1, dict(look=GARY_RED)), ("char", "M", 520, Y2, S2, -1), ("fn", kit(open_=True, trap=True))]),
}
