"""Erklärvideo: What would happen if every man on Earth died?

Quellen: ICAO 2023 / ISWAP (Pilotinnen ~4-6 %); UNODC Global Study on Homicide 2013 (~95 % der Täter männlich);
IPU 2026 (Frauen 27,5 % der Parlamentssitze); UN Women/IPU (~28 Länder von Frauen geführt);
BLS/IWPR 2024 (Elektriker ~3 % Frauen, Bau ~11 % Frauen); Kono et al. 2004 / Li et al. 2018 (Mäuse mit zwei Müttern).
"""
import math
import random

import cairo
import backgrounds as bg
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, stroke_black, rrect

GAP = 0.25
HOOK = ["What would happen if", "every man on Earth died?"]
HOOK_UNTIL = None
CAPTIONS = True

PINK = (1.0, 0.55, 0.65)
BLUE = (0.30, 0.60, 1.0)
CORAL = (1.0, 0.55, 0.45)
PURPLE = (0.55, 0.40, 0.85)

CHARS = {
    "N": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=Look()),  # Erzähler: Brian
    "F": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9",  # Flugbegleiterin: Jessica
              look=Look(shirt=(0.20, 0.30, 0.60), bun=True, lashes=True)),
    "W": dict(voice="en-US-AvaNeural", el_voice="EXAVITQu4vr4xnSDxMaL",  # Ingenieurin: Sarah
              look=Look(shirt=CORAL, ponytail=True, lashes=True)),
}


def lt():
    return bg.CLOCK["lt"]


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def head(cr, x, y, r, col, alpha=1.0):
    cr.arc(x, y, r, 0, 2 * math.pi)
    cr.set_source_rgba(*col, alpha)
    cr.fill_preserve()
    cr.set_source_rgba(0.05, 0.05, 0.06, alpha)
    cr.set_line_width(max(2, r * 0.18))
    cr.stroke()


def title(cr, s, sub=None):
    rrect(cr, 290, 440, 500, 76, 38)
    cr.set_source_rgb(*rgb("#FFD45C"))
    cr.fill()
    _text(cr, s, 540, 492, 40, rgb("#1B1F2E"))
    if sub:
        cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(32)
        w = cr.text_extents(sub).x_advance + 40
        rrect(cr, 540 - w / 2, 532, w, 50, 25)
        cr.set_source_rgba(0.05, 0.07, 0.15, 0.75)
        cr.fill()
        _text(cr, sub, 540, 568, 32, (1, 1, 1), bold=False)


# ------------------------------------------------------------------ Hintergründe
def dark():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    g = cairo.LinearGradient(0, 0, 0, 1920)
    g.add_color_stop_rgb(0, *rgb("#0E1630"))
    g.add_color_stop_rgb(1, *rgb("#1F2D5C"))
    cr.set_source(g)
    cr.paint()
    random.seed(2)
    for _ in range(140):
        cr.arc(random.uniform(0, 1080), random.uniform(0, 1920), random.uniform(1, 2.6), 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, random.uniform(0.2, 0.7))
        cr.fill()
    s.flush()
    return s


def sky():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    g = cairo.LinearGradient(0, 0, 0, 1920)
    g.add_color_stop_rgb(0, *rgb("#4FA3E0"))
    g.add_color_stop_rgb(1, *rgb("#CDEBFA"))
    cr.set_source(g)
    cr.paint()
    random.seed(5)
    for _ in range(9):
        x, y = random.uniform(-50, 1100), random.uniform(650, 1700)
        for dx, dy, r in ((0, 0, 50), (50, -20, 60), (110, 0, 48), (55, 20, 55)):
            cr.arc(x + dx, y + dy, r, 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, 0.85)
        cr.fill()
    s.flush()
    return s


def cabin():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    cr.set_source_rgb(*rgb("#E6E9EE"))
    cr.paint()
    for x in range(60, 1080, 250):
        rrect(cr, x, 700, 130, 170, 60)
        fill_stroke(cr, rgb("#9FD3F5"), 6)
    cr.rectangle(0, 1560, 1080, 360)
    cr.set_source_rgb(*rgb("#5A6270"))
    cr.fill()
    for x in (40, 820):
        rrect(cr, x, 1100, 220, 360, 30)
        fill_stroke(cr, rgb("#2F4F8F"), 5)
    s.flush()
    return s


def site():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    g = cairo.LinearGradient(0, 0, 0, 1560)
    g.add_color_stop_rgb(0, *rgb("#8FD0F5"))
    g.add_color_stop_rgb(1, *rgb("#FDF1D8"))
    cr.set_source(g)
    cr.paint()
    # Kran
    cr.move_to(850, 1560); cr.line_to(850, 620); cr.line_to(250, 620)
    cr.set_source_rgb(*rgb("#F2B705")); cr.set_line_width(22); cr.stroke()
    cr.move_to(450, 620); cr.line_to(450, 900)
    stroke_black(cr, 4)
    cr.rectangle(410, 900, 80, 60)
    fill_stroke(cr, rgb("#8C8C8C"), 4)
    # Rohbau
    for k in range(4):
        cr.rectangle(80, 1560 - (k + 1) * 140, 520, 130)
        fill_stroke(cr, rgb("#D9CBB3"), 4)
    cr.rectangle(0, 1560, 1080, 360)
    cr.set_source_rgb(*rgb("#B89B72"))
    cr.fill()
    s.flush()
    return s


BG = {"dark": dark, "sky": sky, "cabin": cabin, "site": site}


# ------------------------------------------------------------------ Overlays
def ov_earth(cr, t):
    cx, cy, R = 540, 900, 330
    cr.arc(cx, cy, R, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#2F6FB0"), 6, rgb("#9FC8F0"))
    random.seed(4)
    cr.set_source_rgb(*rgb("#5DB870"))
    for (x, y, r) in ((-120, -120, 120), (60, -40, 90), (140, 120, 110), (-90, 140, 80), (-200, 20, 70)):
        cr.arc(cx + x, cy + y, r, 0, 2 * math.pi)
        cr.fill()
    gone = ease((lt() - 2.5) * 1.2)
    for k in range(70):
        a = random.uniform(0, 2 * math.pi)
        d = R * math.sqrt(random.uniform(0, 0.85))
        x, y = cx + d * math.cos(a), cy + d * math.sin(a)
        if k % 2 == 0:
            head(cr, x, y, 14, BLUE, 1 - gone)
        else:
            head(cr, x, y, 14, PINK)
    n = 8.2 - 4.1 * gone
    _text(cr, f"{n:.1f} billion people", 540, 1330, 56, rgb("#FFD45C"))


def ov_plane(cr, t):
    title(cr, "SECOND 1", "~95% of airline pilots are men")
    p = lt()
    tilt = ease((p - 2.5) * 0.5) * 0.35
    x = 540 + math.sin(p * 0.7) * 40
    y = 950 + ease((p - 2.5) * 0.4) * 160
    cr.save(); cr.translate(x, y); cr.rotate(tilt)
    cr.move_to(-330, -35); cr.line_to(230, -35); cr.curve_to(330, -35, 360, 0, 330, 25)
    cr.line_to(-330, 35); cr.close_path()
    fill_stroke(cr, (1, 1, 1), 6)
    cr.move_to(-40, 0); cr.line_to(-160, 190); cr.line_to(-80, 190); cr.line_to(80, 0); cr.close_path()
    fill_stroke(cr, rgb("#D9DEE4"), 5)
    cr.move_to(-280, -30); cr.line_to(-340, -140); cr.line_to(-280, -140); cr.line_to(-220, -30); cr.close_path()
    fill_stroke(cr, rgb("#D9442B"), 5)
    for k in range(9):
        cr.arc(-220 + k * 48, -8, 10, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#7FB2FF"), 3)
    # leeres Cockpit
    cr.move_to(270, -30); cr.line_to(315, -15); cr.line_to(300, 5); cr.line_to(260, 5); cr.close_path()
    fill_stroke(cr, rgb("#1B1F27"), 3)
    cr.restore()
    if p > 1.0:
        _text(cr, "Empty cockpit", 540, 1300, 44, rgb("#D9442B"))


def ov_roads(cr, t):
    title(cr, "MINUTE 1", "millions of cars lose their drivers")
    cr.rectangle(0, 800, 1080, 520)
    cr.set_source_rgb(*rgb("#3A3F48")); cr.fill()
    for y in (930, 1060, 1190):
        for x in range(0, 1080, 120):
            cr.rectangle(x, y, 60, 10)
            cr.set_source_rgb(1, 1, 1); cr.fill()
    random.seed(7)
    stop = ease((lt() - 2.0) * 0.6)
    for k in range(10):
        lane = k % 4
        y = 860 + lane * 130
        sp = random.uniform(160, 260)
        empty = k % 2 == 0
        moving = 1 - (stop if empty else 0.0)
        x = (k * 230 + lt() * sp * (moving if empty else 1)) % 1300 - 150
        rot = (0.4 * stop * (1 if k % 4 == 0 else -1)) if empty else 0
        cr.save(); cr.translate(x, y); cr.rotate(rot)
        rrect(cr, -80, -32, 160, 64, 16)
        fill_stroke(cr, rgb(random.choice(("#E23B3B", "#3D8BFF", "#F2C230", "#33C46A", "#FFFFFF"))), 4)
        cr.rectangle(10, -26, 40, 52)
        cr.set_source_rgb(*rgb("#9FD3F5")); cr.fill()
        if not empty:
            head(cr, 30, 0, 14, PINK)
        cr.restore()
    if stop > 0.3:
        _text(cr, "Traffic chaos everywhere", 540, 1420, 44, (1, 1, 1))


def ov_city(cr, t):
    title(cr, "DAY 1", "power plants & grids run unattended")
    random.seed(11)
    off = ease((lt() - 1.0) * 0.14)
    x = 0
    while x < 1080:
        bw, bh = random.randint(90, 160), random.randint(350, 700)
        cr.rectangle(x, 1400 - bh, bw, bh)
        cr.set_source_rgb(*rgb("#33427A")); cr.fill()
        for yy in range(1400 - bh + 25, 1380, 42):
            for xx in range(x + 14, x + bw - 14, 30):
                lit = random.random() < 0.7 and random.random() > off
                if lit:
                    cr.rectangle(xx, yy, 14, 20)
                    cr.set_source_rgb(*rgb("#FFD86B")); cr.fill()
        x += bw + 8
    _text(cr, "~97% of electricians are men (US)", 540, 650, 38, rgb("#FFD45C"))


def ov_parliament(cr, t):
    title(cr, "WEEK 1", "most governments lose their leaders")
    cx, cy = 540, 1080
    gone = ease((lt() - 1.5) * 1.0)
    k = 0
    for ring in range(5):
        r = 220 + ring * 70
        n = 12 + ring * 4
        for i in range(n):
            a = math.pi + math.pi * (i + 0.5) / n
            woman = (k * 37) % 100 < 27.5
            k += 1
            x, y = cx + r * math.cos(a), cy + r * math.sin(a)
            if woman:
                head(cr, x, y, 18, PINK)
            else:
                head(cr, x, y, 18, BLUE, 1 - gone)
                if gone > 0.5:
                    cr.arc(x, y, 18, 0, 2 * math.pi)
                    cr.set_source_rgba(1, 1, 1, 0.25); cr.set_line_width(3); cr.stroke()
    _text(cr, "Women hold 27.5% of seats", 540, 1190, 44, (1, 1, 1))
    _text(cr, "Only ~28 countries are led by women", 540, 1250, 34, rgb("#FFD45C"), bold=False)


def ov_crime(cr, t):
    title(cr, "MONTH 1", "the murder rate collapses")
    p = ease((lt() - 1.0) * 0.8)
    rrect(cr, 180, 800, 300, 450, 16)
    cr.set_source_rgb(*rgb("#2A3145")); cr.fill()
    rrect(cr, 600, 800, 300, 450, 16)
    cr.set_source_rgb(*rgb("#2A3145")); cr.fill()
    rrect(cr, 180, 800, 300, 450, 16)
    cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
    h = 450 * (1 - 0.95 * p)
    rrect(cr, 600, 1250 - h, 300, max(20, h), 16)
    cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
    _text(cr, "Before", 330, 1310, 40, (1, 1, 1))
    _text(cr, "After", 750, 1310, 40, (1, 1, 1))
    if p > 0.5:
        _text(cr, "-95%", 750, 1150 - h * 0.0, 70, rgb("#FFD45C"))
    _text(cr, "~95% of murderers are men (UNODC)", 540, 680, 36, rgb("#FFD45C"))


def ov_births(cr, t):
    title(cr, "YEAR 1", "births almost stop")
    p = min(1.0, lt() / 5.0)
    cr.move_to(120, 1300); cr.line_to(960, 1300)
    cr.move_to(120, 1300); cr.line_to(120, 700)
    cr.set_source_rgb(*rgb("#9AA3B2")); cr.set_line_width(4); cr.stroke()
    pts = [(120, 760), (380, 760), (420, 1260), (700, 1250), (960, 1150)]
    cr.move_to(*pts[0])
    seg = p * (len(pts) - 1)
    for i in range(1, len(pts)):
        if i <= seg:
            cr.line_to(*pts[i])
        else:
            f = seg - (i - 1)
            if f > 0:
                x0, y0 = pts[i - 1]; x1, y1 = pts[i]
                cr.line_to(x0 + (x1 - x0) * f, y0 + (y1 - y0) * f)
            break
    cr.set_source_rgb(*rgb("#FF8A73")); cr.set_line_width(12); cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
    _text(cr, "Births per year", 540, 680, 34, (1, 1, 1), bold=False)
    if p > 0.75:
        for k in range(5):
            x = 640 + k * 60
            rrect(cr, x, 1000, 34, 110, 10)
            fill_stroke(cr, rgb("#BFE3F2"), 4)
            cr.rectangle(x, 1000, 34, 24)
            cr.set_source_rgb(*rgb("#3D8BFF")); cr.fill()
        _text(cr, "frozen sperm", 740, 980, 30, rgb("#FFD45C"))


def ov_boys(cr, t):
    title(cr, "YEAR 2+", "and baby boys can be born again")
    random.seed(17)
    n = min(40, int(lt() * 9))
    for k in range(n):
        x = 140 + (k % 8) * 115
        y = 800 + (k // 8) * 110
        head(cr, x, y, 34, BLUE if k % 2 == 0 else PINK)
    _text(cr, "Frozen sperm can make boys, too", 540, 1340, 40, (1, 1, 1))


def ov_mice(cr, t):
    title(cr, "THE FUTURE?", "science without sperm")
    for k, x in enumerate((360, 720)):
        cr.save(); cr.translate(x, 900)
        cr.scale(1.4, 1.0)
        cr.arc(0, 0, 70, 0, 2 * math.pi); cr.restore()
        fill_stroke(cr, rgb("#D9D9D9"), 5)
        cr.arc(x + (60 if k == 0 else -60), 840, 30, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#F7A1B5"), 4)
        _text(cr, "MOM", x, 1030, 36, rgb("#FF9FB5"))
    if lt() > 1.5:
        cr.save(); cr.translate(540, 1170); cr.scale(1.2, 0.85)
        cr.arc(0, 0, 50, 0, 2 * math.pi); cr.restore()
        fill_stroke(cr, rgb("#EDEDED"), 5)
        _text(cr, "baby mouse", 540, 1270, 32, (1, 1, 1), bold=False)
    _text(cr, "Mice with two mothers (2004, 2018)", 540, 660, 36, rgb("#FFD45C"))


def ov_earth_end(cr, t):
    cx, cy, R = 540, 900, 330
    cr.arc(cx, cy, R, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#2F6FB0"), 6, rgb("#9FC8F0"))
    cr.set_source_rgb(*rgb("#5DB870"))
    for (x, y, r) in ((-120, -120, 120), (60, -40, 90), (140, 120, 110), (-90, 140, 80), (-200, 20, 70)):
        cr.arc(cx + x, cy + y, r, 0, 2 * math.pi)
        cr.fill()
    random.seed(4)
    back = ease(lt() * 0.25)
    for k in range(70):
        a = random.uniform(0, 2 * math.pi)
        d = R * math.sqrt(random.uniform(0, 0.85))
        x, y = cx + d * math.cos(a), cy + d * math.sin(a)
        head(cr, x, y, 14, BLUE if k % 2 == 0 else PINK, back if k % 2 == 0 else 1.0)


SHOTS = {
    "earth_end": dict(bg="dark", overlays=[ov_earth_end], layers=[]),
    "earth": dict(bg="dark", overlays=[ov_earth], layers=[]),
    "plane": dict(bg="sky", overlays=[ov_plane], layers=[]),
    "cabin": dict(bg="cabin", layers=[("char", "F", 540, 1740, 1.05, 1)]),
    "roads": dict(bg="dark", overlays=[ov_roads], layers=[]),
    "city": dict(bg="dark", overlays=[ov_city], layers=[]),
    "parliament": dict(bg="dark", overlays=[ov_parliament], layers=[]),
    "work": dict(bg="site", layers=[("char", "W", 640, 1740, 1.05, -1)]),
    "crime": dict(bg="dark", overlays=[ov_crime], layers=[]),
    "births": dict(bg="dark", overlays=[ov_births], layers=[]),
    "boys": dict(bg="dark", overlays=[ov_boys], layers=[]),
    "mice": dict(bg="dark", overlays=[ov_mice], layers=[]),
}

SCRIPT = [
    dict(shot="earth", s="N", t="Imagine that one second from now, every man on Earth simply disappears.",
         say="[mysterious] Imagine that one second from now, every man on Earth simply disappears."),
    dict(s="N", t="That's about four billion people. Half of humanity. Gone.", say="[dramatic] That's about four billion people. Half of humanity. Gone.",
         gap=0.4),
    dict(shot="plane", s="N", t="The chaos starts instantly. Around ninety five percent of airline pilots are men.",
         say="[serious] The chaos starts instantly. Around ninety five percent of airline pilots are men."),
    dict(s="N", t="Thousands of planes in the air suddenly have nobody at the controls.", say="[tense] Thousands of planes in the air suddenly have nobody at the controls."),
    dict(shot="cabin", s="F", t="Um, does anyone on this plane know how to fly?", e={"F": "worried"}, p={"F": "shrug"},
         say="[nervously] Um... does anyone on this plane know how to fly?", gap=0.3),
    dict(shot="roads", s="N", t="On the roads, millions of cars lose their drivers at the same moment.",
         say="[tense] On the roads, millions of cars lose their drivers at the same moment."),
    dict(s="N", t="Highways turn into giant pileups within minutes.", say="[serious] Highways turn into giant pileups within minutes.", gap=0.3),
    dict(shot="city", s="N", t="Then the lights start going out. In the US, about ninety seven percent of electricians are men.",
         say="[ominous] Then the lights start going out. In the US, about ninety seven percent of electricians are men."),
    dict(s="N", t="Power plants, oil rigs and water systems would be running with almost nobody who knows them.",
         say="[serious] Power plants, oil rigs and water systems would be running with almost nobody who knows them.", gap=0.3),
    dict(shot="parliament", s="N", t="Governments collapse too. Women hold only about a quarter of parliament seats worldwide.",
         say="[explaining] Governments collapse too. Women hold only about a quarter of parliament seats worldwide."),
    dict(s="N", t="And fewer than thirty countries are led by a woman.", say="[serious] And fewer than thirty countries are led by a woman.", gap=0.3),
    dict(shot="work", s="N", t="Construction, mining, trucking, firefighting. Entire industries would have to be relearned from scratch.",
         e={"W": "neutral"}, p={"W": "idle"}),
    dict(s="W", t="Okay. Who's got the manual for the power plant?", e={"W": "smug"}, p={"W": "explain"},
         say="[determined] Okay. Who's got the manual for the power plant?", gap=0.3),
    dict(shot="crime", s="N", t="But something else would change overnight. About ninety five percent of murderers are men.",
         say="[intrigued] But something else would change overnight. About ninety five percent of murderers are men."),
    dict(s="N", t="So the murder rate would drop like never before.", say="[thoughtful] So the murder rate would drop like never before.", gap=0.3),
    dict(shot="births", s="N", t="The biggest problem? Babies. Without men, births would almost stop.",
         say="[serious] The biggest problem? Babies. Without men, births would almost stop."),
    dict(s="N", t="The only hope would be the frozen sperm in fertility clinics and sperm banks around the world.",
         say="[hopeful] The only hope would be the frozen sperm in fertility clinics and sperm banks around the world."),
    dict(shot="boys", s="N", t="And here's the twist. Frozen sperm can still make boys. So men would slowly come back.",
         say="[surprised] And here's the twist. Frozen sperm can still make boys. So men would slowly come back."),
    dict(shot="mice", s="N", t="In the long run, science might not even need sperm. Researchers have already created mice with two mothers.",
         say="[amazed] In the long run, science might not even need sperm. Researchers have already created mice with two mothers."),
    dict(shot="earth_end", s="N", t="So, would humanity survive? Probably. But the first few weeks would be the hardest in human history.",
         say="[conclusive] So, would humanity survive? Probably. But the first few weeks would be the hardest in human history.", gap=0.8),
]
