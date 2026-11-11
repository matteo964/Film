"""What if the Moon disappeared?

Quellen: Popular Science / Live Science / Physics World (Sonnengezeiten ~1/3 bis 1/2, Neigung bis >45°),
Science Norway (Effekte über lange Zeiträume), DLR/Knapmeyer (keine Bremsung der Erdrotation),
GBRMPA / National Geographic (Korallenlaichen nach dem Vollmond), Lunar Laser Ranging (~3,8 cm/Jahr).
"""
import math
import random

import cairo
import anim
import explainer_kit as K
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, stroke_black, rrect

GAP = 0.22
HOOK = ["What if the Moon", "disappeared?"]
HOOK_UNTIL = None
CAPTIONS = True

LEO = Look(shirt=(0.15, 0.80, 0.91))
ZOE = Look(shirt=(1.0, 0.55, 0.45), ponytail=True, lashes=True)
CHARS = {
    "N": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=Look()),  # Brian
    "A": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=LEO),  # Will
    "E": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=ZOE),  # Jessica
}


def draw_sea(cr):
    g = cairo.LinearGradient(0, 0, 0, 1920)
    g.add_color_stop_rgb(0, *rgb("#0D5E8C"))
    g.add_color_stop_rgb(1, *rgb("#062B47"))
    cr.set_source(g)
    cr.paint()
    cr.move_to(0, 1600)
    cr.curve_to(300, 1540, 700, 1640, 1080, 1560)
    cr.line_to(1080, 1920); cr.line_to(0, 1920); cr.close_path()
    cr.set_source_rgb(*rgb("#D9C28A")); cr.fill()


BG = dict(K.BGS, sea=K.surface(draw_sea))


def couple(cr, t, emo="neutral", look_up=True, poses=("idle", "idle")):
    ld = (0.5, -0.8) if look_up else (1, 0.05)
    anim.actor(cr, "A", LEO, 380, 1600, 0.85, 1, pose=poses[0], emotion=emo, t=t, look_dir=ld)
    anim.actor(cr, "E", ZOE, 640, 1610, 0.85, -1, pose=poses[1], emotion=emo, t=t, look_dir=(-0.5, -0.8) if look_up else (1, 0.05))


def sc_vanish(cr, t):
    lt = K.lt()
    gone = lt > 3.2
    if not gone:
        K.moon(cr, 760, 760, 90)
        g = cairo.RadialGradient(760, 760, 60, 760, 760, 320)
        g.add_color_stop_rgba(0, 1, 1, 0.9, 0.25); g.add_color_stop_rgba(1, 1, 1, 0.9, 0)
        cr.set_source(g); cr.paint()
    flash = K.ease(1 - abs(lt - 3.2) * 4) if abs(lt - 3.2) < 0.25 else 0
    if flash > 0:
        cr.set_source_rgba(1, 1, 1, flash); cr.paint()
    couple(cr, t, "shocked" if gone else "happy", poses=("point" if gone else "idle", "chest" if gone else "idle"))
    if gone:
        cr.arc(760, 760, 90, 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, 0.25); cr.set_line_width(4); cr.set_dash([14, 12]); cr.stroke(); cr.set_dash([])


def sc_dark(cr, t):
    lt = K.lt()
    d = K.ease(lt / 3.0)
    cr.set_source_rgba(0, 0, 0.02, 0.45 * d); cr.paint()
    random.seed(30)
    for _ in range(120):
        cr.arc(random.uniform(0, 1080), random.uniform(420, 1350), random.uniform(1, 2.8), 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, 0.4 + 0.6 * d * random.random()); cr.fill()
    couple(cr, t, "worried")
    K.label(cr, "Nights get much darker", 540, 600, 40)


def sc_tides(cr, t):
    lt = K.lt()
    moon_on = lt < 4.5
    amp = 170 if moon_on else 60
    level = 1300 + math.sin(lt * 1.6) * amp
    cr.rectangle(0, level, 1080, 1920 - level)
    cr.set_source_rgba(0.18, 0.55, 0.85, 0.85); cr.fill()
    cr.set_source_rgba(1, 1, 1, 0.6); cr.set_line_width(5)
    for x in range(0, 1080, 90):
        cr.move_to(x, level); cr.curve_to(x + 25, level - 12, x + 55, level - 12, x + 90, level)
    cr.stroke()
    # Pegel
    cr.rectangle(940, 1050, 18, 520); cr.set_source_rgb(1, 1, 1); cr.fill()
    for k in range(6):
        cr.rectangle(930, 1080 + k * 90, 38, 6); cr.set_source_rgb(*rgb("#1B1F27")); cr.fill()
    if moon_on:
        K.label(cr, "Tides WITH the Moon", 540, 600, 42, rgb("#FFD45C"))
    else:
        K.label(cr, "Sun only: ~1/3 to 1/2 as strong", 540, 600, 40, rgb("#FFD45C"))


def crab(cr, x, y, s, t, k):
    cr.save(); cr.translate(x, y); cr.scale(s, s)
    cr.save(); cr.scale(1.4, 1); cr.arc(0, 0, 30, 0, 2 * math.pi); cr.restore()
    fill_stroke(cr, rgb("#E2553B"), 4)
    for side in (-1, 1):
        for j in range(3):
            leg = math.sin(t * 12 + j + k) * 6
            cr.move_to(side * 30, 5 + j * 8); cr.line_to(side * (55 + leg), 25 + j * 10)
        cr.move_to(side * 25, -15); cr.line_to(side * 45, -40)
        stroke_black(cr, 4)
        cr.arc(side * 50, -48, 12, 0, 2 * math.pi); fill_stroke(cr, rgb("#E2553B"), 3)
    for dx in (-10, 10):
        cr.move_to(dx, -25); cr.line_to(dx, -45); stroke_black(cr, 3)
        cr.arc(dx, -48, 6, 0, 2 * math.pi); cr.set_source_rgb(1, 1, 1); cr.fill()
    cr.restore()


def sc_crabs(cr, t):
    lt = K.lt()
    for k in range(6):
        x = 150 + k * 160 + math.sin(lt * 1.3 + k * 2) * 60
        y = 1480 + (k % 2) * 90
        crab(cr, x, y, 1.0, t, k)
    K.label(cr, "Tide-pool life loses its rhythm", 540, 600, 40)


def sc_coral(cr, t):
    lt = K.lt()
    no_moon = lt > 4.2
    random.seed(2)
    for k in range(7):
        x = 100 + k * 150
        h = random.uniform(120, 220)
        for j in range(5):
            a = -math.pi / 2 + (j - 2) * 0.35
            cr.move_to(x, 1600); cr.line_to(x + math.cos(a) * h, 1600 + math.sin(a) * h)
        cr.set_source_rgb(*rgb(random.choice(("#FF8A9A", "#FFB36B", "#C78BFF")))); cr.set_line_width(22)
        cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
    if not no_moon:
        K.moon(cr, 860, 700, 60)
        random.seed(5)
        for k in range(60):
            x = random.uniform(60, 1020)
            sp = random.uniform(60, 140)
            y = 1550 - ((lt * sp + random.uniform(0, 700)) % 800)
            cr.arc(x, y, random.uniform(5, 10), 0, 2 * math.pi)
            cr.set_source_rgba(1, 0.75, 0.8, 0.9); cr.fill()
        K.label(cr, "Full moon → mass coral spawning", 540, 600, 38, rgb("#FFD45C"))
    else:
        cr.arc(860, 700, 60, 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, 0.3); cr.set_line_width(4); cr.set_dash([12, 10]); cr.stroke(); cr.set_dash([])
        K.label(cr, "No moon → no signal", 540, 600, 40, rgb("#FF8A8A"))


def sc_spin(cr, t):
    lt = K.lt()
    K.globe(cr, 540, 1000, 260, tilt=0.41, spin=lt * 0.5)
    K.label(cr, "The Moon slowly brakes Earth's spin", 540, 600, 36)
    if lt > 2.5:
        K.label(cr, "Without it: days stop getting longer", 540, 1360, 36, rgb("#FFD45C"))


def sc_tilt(cr, t):
    lt = K.lt()
    amp = 0.41 + K.ease(lt / 6.0) * 0.45
    tilt = math.sin(lt * 1.1) * amp
    K.globe(cr, 540, 1000, 250, tilt=tilt, spin=lt * 0.3)
    deg = abs(tilt) * 57.3
    K.label(cr, f"Tilt: {deg:4.0f}°", 540, 600, 50, rgb("#FFD45C") if deg < 30 else rgb("#FF6B6B"))
    if lt > 3.5:
        # Eis oben / Hitze unten
        cr.arc(540, 760, 60, 0, 2 * math.pi); cr.set_source_rgba(0.85, 0.95, 1, 0.9); cr.fill()
        _text(cr, "ICE AGES", 540, 700, 30, (1, 1, 1))
        _text(cr, "EXTREME SEASONS", 540, 1330, 34, rgb("#FFB36B"))


def sc_end(cr, t):
    lt = K.lt()
    K.moon(cr, 760, 760, 90)
    couple(cr, t, "happy", poses=("shrug", "idle"))
    if lt > 2.0:
        K.label(cr, "Moon drifts away ~3.8 cm per year", 540, 600, 36, rgb("#FFD45C"))


SHOTS = {
    "vanish": dict(bg="hill", overlays=[sc_vanish], layers=[]),
    "dark": dict(bg="hill", overlays=[sc_dark], layers=[]),
    "tides": dict(bg="beach", overlays=[sc_tides], layers=[]),
    "crabs": dict(bg="beach", overlays=[sc_crabs], layers=[]),
    "coral": dict(bg="sea", overlays=[sc_coral], layers=[]),
    "spin": dict(bg="dark", overlays=[sc_spin], layers=[]),
    "tilt": dict(bg="dark", overlays=[sc_tilt], layers=[]),
    "end": dict(bg="hill", overlays=[sc_end], layers=[]),
}

SCRIPT = [
    dict(shot="vanish", s="N", t="Imagine you're looking up at the Moon tonight. And then, in a flash, it's gone.",
         say="[mysterious] Imagine you're looking up at the Moon tonight. And then, in a flash... it's gone."),
    dict(s="A", t="Uh, where did the Moon go?", say="[shocked] Uh... where did the Moon go?", gap=0.3),
    dict(shot="dark", s="N", t="The first thing you'd notice: nights get much darker. The Moon is by far the brightest thing in our night sky.",
         say="[calm] The first thing you'd notice: nights get much darker. The Moon is by far the brightest thing in our night sky."),
    dict(s="E", t="I can't see my own hand.", say="[nervous] I can't see my own hand.", gap=0.3),
    dict(shot="tides", s="N", t="Then, the oceans change. Tides wouldn't stop completely, because the Sun creates tides too.",
         say="[explaining] Then, the oceans change. Tides wouldn't stop completely, because the Sun creates tides too."),
    dict(s="N", t="But they'd shrink to roughly a third to half of what they are today.",
         say="[serious] But they'd shrink to roughly a third to half of what they are today.", gap=0.3),
    dict(shot="crabs", s="N", t="Crabs, snails and countless coastal creatures live by the rhythm of the tides. That rhythm would be thrown off.",
         say="[concerned] Crabs, snails and countless coastal creatures live by the rhythm of the tides. That rhythm would be thrown off."),
    dict(shot="coral", s="N", t="On the Great Barrier Reef, corals release their eggs together, a few nights after the full moon.",
         say="[wonder] On the Great Barrier Reef, corals release their eggs together, a few nights after the full moon."),
    dict(s="N", t="Without the Moon, that signal would be gone.", say="[sad] Without the Moon, that signal would be gone.", gap=0.3),
    dict(shot="spin", s="N", t="The Moon also acts like a brake on Earth's spin. Without it, our days would stop slowly getting longer.",
         say="[explaining] The Moon also acts like a brake on Earth's spin. Without it, our days would stop slowly getting longer."),
    dict(shot="tilt", s="N", t="But the scariest part takes much longer. The Moon keeps Earth's tilt steady at about twenty three degrees.",
         say="[ominous] But the scariest part takes much longer. The Moon keeps Earth's tilt steady at about twenty three degrees."),
    dict(s="N", t="Without it, over hundreds of thousands of years, the tilt could swing wildly. Maybe past forty five degrees.",
         say="[dramatic] Without it, over hundreds of thousands of years, the tilt could swing wildly. Maybe past forty five degrees."),
    dict(s="N", t="That could mean extreme seasons and ice ages.", say="[grim] That could mean extreme seasons and ice ages.", gap=0.3),
    dict(shot="end", s="N", t="The good news? The Moon isn't going anywhere. Well, it is drifting away. About three point eight centimeters a year.",
         say="[relieved, amused] The good news? The Moon isn't going anywhere. Well... it IS drifting away. About three point eight centimeters a year."),
    dict(s="E", t="So we've still got some time.", say="[laughs] So we've still got some time.", gap=0.8),
]
