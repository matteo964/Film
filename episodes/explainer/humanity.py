"""Erklärvideo: Can 2 people really restart humanity?

Quellen: Hu et al., Science 2023 (Flaschenhals ~1.280 Individuen); Bradford-Studie 2013 (Cousins 3 % -> 6 %);
Seemanová 1971 (Inzest, ~42 % schwere Fehlbildungen/früher Tod, Sekundärzitat); Franklin/Soulé 50/500-Regel;
Generationenschiff-Studien (98 Personen, Smith 2014: 10.000-40.000); Tristan da Cunha (~15 Gründer, Genealogie-Studie 2003).
"""
import math
import random

import cairo
import backgrounds as bg
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, stroke_black, rrect

GAP = 0.25
HOOK = ["Can 2 people really", "restart humanity?"]
HOOK_UNTIL = None
CAPTIONS = True

CYAN = (0.15, 0.80, 0.91)
CORAL = (1.0, 0.55, 0.45)
GREEN = (0.35, 0.75, 0.45)
YELLOW = (0.98, 0.80, 0.25)

CHARS = {
    "N": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=Look()),  # Erzähler: Brian
    "A": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=Look(shirt=CYAN)),  # Will
    "E": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9",  # Jessica
              look=Look(shirt=CORAL, ponytail=True, lashes=True)),
    "B": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=Look(shirt=GREEN, cap=True)),  # Liam
    "S": dict(voice="en-US-AvaNeural", el_voice="FGY2WhTYpPnrIDTdsKH5", look=Look(shirt=YELLOW, ponytail=True, lashes=True)),
}


def lt():
    return bg.CLOCK["lt"]


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


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


def city():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    g = cairo.LinearGradient(0, 0, 0, 1560)
    g.add_color_stop_rgb(0, *rgb("#3B2E5A"))
    g.add_color_stop_rgb(0.6, *rgb("#E07A5F"))
    g.add_color_stop_rgb(1, *rgb("#F2CC8F"))
    cr.set_source(g)
    cr.paint()
    cr.arc(540, 1150, 170, 0, 2 * math.pi)
    cr.set_source_rgba(1, 0.9, 0.6, 0.8)
    cr.fill()
    random.seed(8)
    x = -20
    while x < 1100:
        bw, bh = random.randint(70, 140), random.randint(250, 650)
        cr.rectangle(x, 1560 - bh, bw, bh)
        cr.set_source_rgb(*rgb("#2A2140"))
        cr.fill()
        for yy in range(1560 - bh + 30, 1540, 46):
            for xx in range(x + 14, x + bw - 14, 30):
                if random.random() < 0.08:
                    cr.rectangle(xx, yy, 14, 20)
                    cr.set_source_rgb(*rgb("#5A4A78"))
                    cr.fill()
        x += bw + random.randint(4, 14)
    cr.rectangle(0, 1560, 1080, 360)
    cr.set_source_rgb(*rgb("#3A3550"))
    cr.fill()
    # Gras/Risse = verlassene Stadt
    cr.set_source_rgb(*rgb("#5C8A4A"))
    for k in range(40):
        gx = random.uniform(0, 1080)
        cr.move_to(gx, 1570)
        cr.line_to(gx + 6, 1540)
        cr.line_to(gx + 12, 1570)
        cr.fill()
    s.flush()
    return s


BG = {"dark": dark, "city": city}


# ------------------------------------------------------------------ Infografik-Overlays
def head(cr, x, y, r, col, alpha=1.0):
    cr.arc(x, y, r, 0, 2 * math.pi)
    cr.set_source_rgba(*col, alpha)
    cr.fill_preserve()
    cr.set_source_rgba(0.05, 0.05, 0.06, alpha)
    cr.set_line_width(max(2, r * 0.18))
    cr.stroke()


def ov_tree(cr, t):
    gens = [2, 6, 18, 54]
    shown = min(len(gens), 1 + int(lt() / 1.6))
    y0 = 600
    for gi in range(shown):
        n = gens[gi]
        y = y0 + gi * 150
        r = (46, 34, 22, 15)[gi]
        per_row = min(n, 27)
        rows = math.ceil(n / per_row)
        for k in range(n):
            row, colk = divmod(k, per_row)
            span = min(940, per_row * (2 * r + 8))
            x = 540 - span / 2 + (colk + 0.5) * span / per_row
            yy = y + row * (2 * r + 6) - (rows - 1) * r
            a = ease((lt() - gi * 1.6) * 2.5)
            head(cr, x, yy, r, CYAN if k % 2 == 0 else CORAL, a)
    total = sum(gens[:shown])
    _text(cr, f"Generation {shown}: {gens[shown - 1]} people", 540, 1250, 50, (1, 1, 1))


def ov_dna(cr, t):
    # zwei Eltern, je zwei Genkopien (grün = ok, rot = versteckt schädlich)
    def card(x, y, bad, a=1.0):
        rrect(cr, x - 40, y - 60, 80, 120, 14)
        cr.set_source_rgba(*(rgb("#E23B3B") if bad else rgb("#33C46A")), a)
        cr.fill_preserve()
        cr.set_source_rgba(1, 1, 1, a)
        cr.set_line_width(5)
        cr.stroke()
    _text(cr, "Mom", 290, 560, 44, (1, 1, 1))
    _text(cr, "Dad", 790, 560, 44, (1, 1, 1))
    card(240, 660, False); card(340, 660, True)
    card(740, 660, True); card(840, 660, False)
    _text(cr, "1 hidden harmful copy each = healthy", 540, 820, 34, rgb("#C9D3E6"), bold=False)
    a = ease((lt() - 2.0) * 1.5)
    if a > 0:
        cr.move_to(340, 730); cr.line_to(500, 960)
        cr.move_to(740, 730); cr.line_to(580, 960)
        cr.set_source_rgba(1, 1, 1, a); cr.set_line_width(5); cr.stroke()
        card(490, 1040, True, a); card(590, 1040, True, a)
        _text(cr, "Child gets BOTH bad copies", 540, 1170, 42, rgb("#FF8A8A"))
        _text(cr, "Close relatives share the same bad copies", 540, 1230, 32, rgb("#C9D3E6"), bold=False)


def ov_chart(cr, t):
    bars = [("Unrelated parents", 3, "#33C46A"), ("First cousins", 6, "#F2C230"), ("Siblings (severe / early death)*", 42, "#E23B3B")]
    _text(cr, "Risk of birth defects", 540, 560, 44, (1, 1, 1))
    for k, (lab, v, c) in enumerate(bars):
        y = 680 + k * 190
        a = ease((lt() - k * 1.2) * 1.2)
        _text(cr, lab, 90, y, 36, rgb("#C9D3E6"), bold=False, center=False)
        w = 800 * (v / 45) * a
        rrect(cr, 90, y + 20, max(20, w), 70, 14)
        cr.set_source_rgb(*rgb(c)); cr.fill()
        if a > 0.05:
            _text(cr, f"~{v}%", 90 + max(20, w) + 20, y + 72, 44, (1, 1, 1), center=False)
    _text(cr, "*small 1971 Czech study", 540, 1300, 28, rgb("#9AA3B2"), bold=False)


def ov_diversity(cr, t):
    random.seed(13)
    pal = [rgb(c) for c in ("#25C9E6", "#FF8A73", "#33C46A", "#F2C230", "#9A6BFF", "#FF5E8A", "#5B8CFF",
                            "#C98A55", "#7CE0B4", "#E07A5F", "#B5E3DC", "#F7A1B5")]
    four = pal[:4] if False else [rgb("#25C9E6"), rgb("#FF8A73"), rgb("#25C9E6"), rgb("#FF8A73")]
    collapse = ease((lt() - 2.2) * 0.9)
    virus = ease((lt() - 4.6) * 1.2)
    for k in range(48):
        row, col = divmod(k, 8)
        x, y = 160 + col * 110, 560 + row * 120
        c0 = pal[k % len(pal)]
        c1 = four[k % 4]
        c = tuple(c0[i] * (1 - collapse) + c1[i] * collapse for i in range(3))
        alive = 1.0 - virus * (0.9 if (k * 7) % 10 < 7 else 0.0)
        head(cr, x, y, 40, c, alive)
    if collapse > 0.5:
        _text(cr, "2 people = only 4 copies of each gene", 540, 1330, 38, rgb("#FFD45C"))
    if virus > 0:
        cx, cy, r = 540, 900, 110 * virus
        for k in range(12):
            a = 2 * math.pi * k / 12
            cr.move_to(cx + r * math.cos(a), cy + r * math.sin(a))
            cr.line_to(cx + 1.35 * r * math.cos(a), cy + 1.35 * r * math.sin(a))
        cr.set_source_rgb(*rgb("#7CFF6B")); cr.set_line_width(10); cr.stroke()
        cr.arc(cx, cy, r, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#58C24A"), 6)


def ov_rule(cr, t):
    a1, a2 = ease(lt() * 1.5), ease((lt() - 3.0) * 1.5)
    if a1 > 0:
        cr.save(); cr.translate(540, 760); cr.scale(0.6 + 0.4 * a1, 0.6 + 0.4 * a1)
        _text(cr, "50", 0, 60, 200, rgb("#FFD45C")); cr.restore()
        _text(cr, "to avoid inbreeding", 540, 880, 40, (1, 1, 1), bold=False)
    if a2 > 0:
        cr.save(); cr.translate(540, 1130); cr.scale(0.6 + 0.4 * a2, 0.6 + 0.4 * a2)
        _text(cr, "500", 0, 60, 200, rgb("#5BEA8B")); cr.restore()
        _text(cr, "to keep diversity long-term", 540, 1250, 40, (1, 1, 1), bold=False)
    _text(cr, "Conservation biology's 50/500 rule", 540, 560, 38, rgb("#C9D3E6"))


def ov_ship(cr, t):
    x = -300 + 1500 * min(1, lt() / 7.0)
    cr.save(); cr.translate(x, 820)
    cr.move_to(-260, -60); cr.line_to(170, -60); cr.line_to(260, 0); cr.line_to(170, 60); cr.line_to(-260, 60)
    cr.close_path(); fill_stroke(cr, rgb("#C9D3E6"), 6)
    for k in range(5):
        cr.arc(-180 + k * 80, 0, 20, 0, 2 * math.pi); fill_stroke(cr, rgb("#7FB2FF"), 4)
    cr.move_to(-260, -40); cr.line_to(-340, 0); cr.line_to(-260, 40); cr.close_path()
    cr.set_source_rgb(*rgb("#FF9F43")); cr.fill()
    cr.restore()
    a1, a2 = ease((lt() - 1.0) * 1.5), ease((lt() - 4.0) * 1.5)
    if a1 > 0:
        _text(cr, "~98 people", 540, 1060, 70, (1, 1, 1))
        _text(cr, "absolute minimum (one study)", 540, 1115, 32, rgb("#C9D3E6"), bold=False)
    if a2 > 0:
        _text(cr, "10,000 – 40,000", 540, 1230, 70, rgb("#5BEA8B"))
        _text(cr, "to be safe (Smith, 2014)", 540, 1285, 32, rgb("#C9D3E6"), bold=False)
    _text(cr, "Generation ship crew estimates", 540, 560, 38, rgb("#C9D3E6"))


def ov_island(cr, t):
    cr.rectangle(0, 900, 1080, 400)
    cr.set_source_rgb(*rgb("#2F6FB0")); cr.fill()
    cr.move_to(180, 1000); cr.curve_to(300, 640, 760, 640, 900, 1000); cr.close_path()
    fill_stroke(cr, rgb("#6BAA5A"), 5)
    cr.move_to(470, 760); cr.line_to(540, 620); cr.line_to(610, 760); cr.close_path()
    fill_stroke(cr, rgb("#8C8C8C"), 4)
    random.seed(3)
    n = min(15, int(lt() * 5))
    for k in range(n):
        head(cr, 330 + (k % 8) * 60, 880 + (k // 8) * 60, 22, CYAN if k % 2 else CORAL)
    _text(cr, "Tristan da Cunha", 540, 1120, 56, (1, 1, 1))
    _text(cr, "Today's islanders descend from ~15 founders", 540, 1180, 34, rgb("#FFD45C"), bold=False)


def ov_bottleneck(cr, t):
    _text(cr, "Our ancestors' population (est.)", 540, 560, 38, rgb("#C9D3E6"))
    p = min(1.0, lt() / 4.0)
    pts = [(80, 760), (300, 740), (420, 1180), (640, 1190), (760, 900), (1000, 700)]
    cr.move_to(*pts[0])
    total = len(pts) - 1
    seg = p * total
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
    if p > 0.45:
        _text(cr, "~1,280 breeding individuals", 540, 1270, 46, rgb("#FFD45C"))
        _text(cr, "~900,000 years ago  ·  for ~100,000 years", 540, 1325, 32, (1, 1, 1), bold=False)
        _text(cr, "(Hu et al., Science 2023 – still debated)", 540, 1370, 26, rgb("#9AA3B2"), bold=False)


def ov_crowd(cr, t):
    random.seed(21)
    n = min(120, int(lt() * 30))
    for k in range(n):
        x = random.uniform(40, 1040)
        y = random.uniform(1640, 1880)
        head(cr, x, y, random.uniform(16, 26),
             rgb(random.choice(("#25C9E6", "#FF8A73", "#33C46A", "#F2C230", "#9A6BFF", "#FF5E8A"))))


SHOTS = {
    "city_AE": dict(bg="city", layers=[("char", "A", 400, 1700, 0.95, 1), ("char", "E", 680, 1700, 0.95, -1)]),
    "tree": dict(bg="dark", overlays=[ov_tree], layers=[]),
    "kids": dict(bg="city", layers=[("char", "B", 400, 1700, 0.95, 1), ("char", "S", 680, 1700, 0.95, -1)]),
    "dna": dict(bg="dark", overlays=[ov_dna], layers=[]),
    "chart": dict(bg="dark", overlays=[ov_chart], layers=[]),
    "diversity": dict(bg="dark", overlays=[ov_diversity], layers=[]),
    "rule": dict(bg="dark", overlays=[ov_rule], layers=[]),
    "ship": dict(bg="dark", overlays=[ov_ship], layers=[]),
    "island": dict(bg="dark", overlays=[ov_island], layers=[]),
    "bottleneck": dict(bg="dark", overlays=[ov_bottleneck], layers=[]),
    "end": dict(bg="city", front=[ov_crowd], layers=[("char", "A", 400, 1600, 0.8, 1), ("char", "E", 680, 1600, 0.8, -1)]),
}

SCRIPT = [
    dict(shot="city_AE", s="N", t="Imagine every human on Earth suddenly disappears. Except two.", e={"A": "neutral", "E": "neutral"},
         p={"A": "idle", "E": "idle"}, say="[mysterious] Imagine every human on Earth suddenly disappears. Except two."),
    dict(s="A", t="So... it's just us?", e={"A": "worried"}, p={"A": "shrug"}, say="[nervously] So... it's just us?"),
    dict(s="E", t="Looks like it.", e={"E": "worried"}, p={"E": "cross"}),
    dict(s="N", t="Could these two people really restart humanity?", e={"A": "confused", "E": "confused"},
         say="[curious] Could these two people really restart humanity?", gap=0.4),
    dict(shot="tree", s="N", t="On paper, it works. They have kids, those kids have kids, and the numbers grow fast.",
         say="[upbeat] On paper, it works. They have kids, those kids have kids, and the numbers grow fast."),
    dict(s="N", t="But there's a massive problem.", say="[serious] But there's a massive problem.", gap=0.3),
    dict(shot="kids", s="N", t="Their children would have nobody to start a family with. Except each other.",
         e={"B": "neutral", "S": "neutral"}, p={"B": "idle", "S": "idle"}),
    dict(s="B", t="Wait. Who are we supposed to marry?", e={"B": "shocked", "S": "shocked"}, p={"B": "shrug"},
         say="[horrified] Wait. Who are we supposed to marry?", gap=0.3),
    dict(shot="dna", s="N", t="Every person carries a few hidden, harmful gene variants. With one copy, you're usually fine.",
         say="[explaining] Every person carries a few hidden, harmful gene variants. With one copy, you're usually fine."),
    dict(s="N", t="But close relatives share the same hidden copies. So their kids are far more likely to get two.",
         say="[serious] But close relatives share the same hidden copies. So their kids are far more likely to get two."),
    dict(shot="chart", s="N", t="For unrelated parents, the risk of birth defects is about three percent. For first cousins, about six.",
         say="[explaining] For unrelated parents, the risk of birth defects is about three percent. For first cousins, about six."),
    dict(s="N", t="For siblings, one study found around four in ten children had severe defects, or died young.",
         say="[grim] For siblings, one study found around four in ten children had severe defects, or died young.", gap=0.4),
    dict(shot="diversity", s="N", t="And there's a second problem. Two people carry at most four versions of each gene.",
         say="[serious] And there's a second problem. Two people carry at most four versions of each gene."),
    dict(s="N", t="All of humanity's diversity would be gone. One new disease could wipe out everyone.",
         say="[dramatic] All of humanity's diversity would be gone. One new disease could wipe out everyone.", gap=0.4),
    dict(shot="rule", s="N", t="So how many people do we actually need? Biologists use the fifty five hundred rule.",
         say="[curious] So how many people do we actually need? Biologists use the fifty, five hundred rule."),
    dict(s="N", t="At least fifty to avoid inbreeding. And five hundred to keep a species healthy long term.",
         say="[explaining] At least fifty to avoid inbreeding. And five hundred to keep a species healthy long term."),
    dict(shot="ship", s="N", t="Scientists planning ships to other stars came up with numbers from about ninety eight people, to forty thousand, to be safe.",
         say="[impressed] Scientists planning ships to other stars came up with numbers from about ninety eight people, to forty thousand, to be safe."),
    dict(shot="island", s="N", t="Real life shows small groups can make it. Everyone on the island of Tristan da Cunha descends from about fifteen founders.",
         say="[interested] Real life shows small groups can make it. Everyone on the island of Tristan da Cunha descends from about fifteen founders."),
    dict(shot="bottleneck", s="N", t="And here's the wild part. A 2023 study suggests our own ancestors may have dropped to about thirteen hundred breeding adults.",
         say="[amazed] And here's the wild part. A 2023 study suggests our own ancestors may have dropped to about thirteen hundred breeding adults."),
    dict(s="N", t="Around nine hundred thousand years ago. And they barely survived.", say="[dramatic] Around nine hundred thousand years ago. And they barely survived.",
         gap=0.4),
    dict(shot="end", s="N", t="So, can two people restart humanity? For a few generations, maybe. Long term? Almost certainly not.",
         e={"A": "neutral", "E": "neutral"}, p={"A": "idle", "E": "idle"},
         say="[thoughtful] So, can two people restart humanity? For a few generations, maybe. Long term? Almost certainly not."),
    dict(s="N", t="We'd need hundreds of people. Ideally thousands.", say="[conclusive] We'd need hundreds of people. Ideally thousands."),
    dict(s="E", t="Guess we need more friends.", e={"E": "happy", "A": "happy"}, p={"E": "shrug"},
         say="[laughs] Guess we need more friends.", gap=0.8),
]
