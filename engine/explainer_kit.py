"""Bausteine für "What if"-Erklärvideos: Szenen, Titel-Pillen, Animationshilfen."""
import math
import random

import cairo
import backgrounds as bg
from backgrounds import rgb, _text, fill_stroke
from stickman import stroke_black, rrect

W, H = 1080, 1920


def lt():
    return bg.CLOCK["lt"]


def T():
    return bg.CLOCK["t"]


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


def pill(cr, s, sub=None, y=440, col="#FFD45C"):
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(40)
    w = max(260, cr.text_extents(s).x_advance + 70)
    rrect(cr, 540 - w / 2, y, w, 76, 38)
    cr.set_source_rgb(*rgb(col))
    cr.fill()
    _text(cr, s, 540, y + 52, 40, rgb("#1B1F2E"))
    if sub:
        cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(32)
        w2 = cr.text_extents(sub).x_advance + 40
        rrect(cr, 540 - w2 / 2, y + 92, w2, 50, 25)
        cr.set_source_rgba(0.05, 0.07, 0.15, 0.78)
        cr.fill()
        _text(cr, sub, 540, y + 128, 32, (1, 1, 1), bold=False)


def label(cr, s, x, y, size=40, col=(1, 1, 1), bgcol=(0.05, 0.07, 0.15, 0.78)):
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(size)
    w = cr.text_extents(s).x_advance + 36
    rrect(cr, x - w / 2, y - size * 0.95, w, size * 1.35, size * 0.45)
    cr.set_source_rgba(*bgcol)
    cr.fill()
    _text(cr, s, x, y, size, col)


def surface(draw):
    def make():
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(s)
        draw(cr)
        s.flush()
        return s
    return make


# ------------------------------------------------------------------ Szenen (statisch)
def _floor(cr, y, col):
    cr.rectangle(0, y, W, H - y)
    cr.set_source_rgb(*rgb(col))
    cr.fill()


def draw_dark(cr):
    g = cairo.LinearGradient(0, 0, 0, H)
    g.add_color_stop_rgb(0, *rgb("#0E1630"))
    g.add_color_stop_rgb(1, *rgb("#1F2D5C"))
    cr.set_source(g)
    cr.paint()
    random.seed(2)
    for _ in range(140):
        cr.arc(random.uniform(0, W), random.uniform(0, H), random.uniform(1, 2.6), 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, random.uniform(0.2, 0.7))
        cr.fill()


def draw_bedroom(cr):
    cr.set_source_rgb(*rgb("#2B3566"))
    cr.paint()
    _floor(cr, 1560, "#4A3A5E")
    # Fenster mit Nacht
    cr.rectangle(640, 600, 340, 420)
    fill_stroke(cr, rgb("#0E1630"), 7, rgb("#C9D3E6"))
    cr.arc(860, 700, 40, 0, 2 * math.pi)
    cr.set_source_rgb(*rgb("#F4F1D0")); cr.fill()
    cr.move_to(810, 600); cr.line_to(810, 1020)
    cr.set_source_rgb(*rgb("#C9D3E6")); cr.set_line_width(7); cr.stroke()
    # Bett
    rrect(cr, 60, 1330, 520, 150, 20)
    fill_stroke(cr, rgb("#5B8CFF"), 5)
    rrect(cr, 60, 1250, 140, 230, 20)
    fill_stroke(cr, rgb("#3D5BA8"), 5)
    rrect(cr, 210, 1290, 140, 50, 20)
    fill_stroke(cr, (1, 1, 1), 4)
    # Nachttisch + Lampe
    cr.rectangle(640, 1380, 160, 180)
    fill_stroke(cr, rgb("#7A5233"), 5)
    cr.move_to(690, 1380); cr.line_to(700, 1300); cr.line_to(740, 1300); cr.line_to(750, 1380)
    cr.close_path(); fill_stroke(cr, rgb("#FFD86B"), 4)


def draw_street(cr):
    g = cairo.LinearGradient(0, 0, 0, 1300)
    g.add_color_stop_rgb(0, *rgb("#8FD0F5"))
    g.add_color_stop_rgb(1, *rgb("#E8F6FD"))
    cr.set_source(g)
    cr.paint()
    random.seed(6)
    x = -20
    while x < W:
        bw, bh = random.randint(120, 200), random.randint(380, 760)
        cr.rectangle(x, 1300 - bh, bw, bh)
        fill_stroke(cr, rgb(random.choice(("#F3C5A0", "#D9CBB3", "#BFD7EA", "#F2DDB0"))), 4)
        for yy in range(1300 - bh + 40, 1260, 80):
            for xx in range(x + 22, x + bw - 40, 55):
                cr.rectangle(xx, yy, 30, 44)
                fill_stroke(cr, rgb("#9FD3F5"), 2)
        x += bw + 10
    _floor(cr, 1300, "#C9C9C9")
    _floor(cr, 1560, "#5A5F69")
    cr.rectangle(0, 1300, W, 20)
    cr.set_source_rgb(*rgb("#9A9A9A")); cr.fill()


def draw_cafe(cr):
    cr.set_source_rgb(*rgb("#F3E3C7"))
    cr.paint()
    _floor(cr, 1560, "#9C6B43")
    _text(cr, "BEAN STOP", 540, 560, 54, rgb("#6E3B1F"))
    rrect(cr, 200, 600, 680, 260, 14)
    fill_stroke(cr, rgb("#1E3B2F"), 6)
    for k, (a, b) in enumerate((("Latte", "$4.50"), ("Croissant", "$3.20"), ("Muffin", "$2.90"))):
        _text(cr, a, 250, 680 + k * 60, 34, (1, 1, 1), bold=False, center=False)
        _text(cr, b, 730, 680 + k * 60, 34, rgb("#FFD45C"), center=False)
    # Theke
    cr.rectangle(0, 1250, W, 310)
    fill_stroke(cr, rgb("#7A5233"), 6)
    cr.rectangle(0, 1230, W, 30)
    fill_stroke(cr, rgb("#5B3B22"), 5)


def draw_bank(cr):
    cr.set_source_rgb(*rgb("#DDE3EA"))
    cr.paint()
    _floor(cr, 1560, "#8C96A3")
    _text(cr, "CITY BANK", 540, 560, 54, rgb("#1F3B63"))
    rrect(cr, 360, 620, 360, 940, 20)
    fill_stroke(cr, rgb("#5B6B80"), 6)
    rrect(cr, 400, 680, 280, 200, 12)
    fill_stroke(cr, rgb("#0F1320"), 5)
    cr.rectangle(430, 930, 220, 160)
    fill_stroke(cr, rgb("#3A4555"), 4)
    for r in range(3):
        for c in range(3):
            rrect(cr, 450 + c * 66, 945 + r * 48, 52, 38, 6)
            fill_stroke(cr, rgb("#C9D2DA"), 2)
    cr.rectangle(450, 1130, 180, 18)
    cr.set_source_rgb(*rgb("#111111")); cr.fill()


def draw_airport(cr):
    cr.set_source_rgb(*rgb("#E6ECF2"))
    cr.paint()
    _floor(cr, 1560, "#A3AEBB")
    cr.rectangle(0, 1100, W, 460)
    cr.set_source_rgb(*rgb("#BFE3F2")); cr.fill()
    cr.move_to(700, 1300); cr.line_to(1000, 1290); cr.line_to(1060, 1320); cr.line_to(700, 1330)
    cr.close_path(); fill_stroke(cr, (1, 1, 1), 4)
    for x in range(0, W, 180):
        cr.move_to(x, 1100); cr.line_to(x, 1560)
    cr.set_source_rgb(*rgb("#7F8C99")); cr.set_line_width(8); cr.stroke()


def draw_shop(cr):
    cr.set_source_rgb(*rgb("#F2F5F7"))
    cr.paint()
    _floor(cr, 1560, "#C9CED4")
    _text(cr, "SUPERMARKET", 540, 560, 50, rgb("#2F7D4F"))
    for k in range(4):
        y = 640 + k * 230
        cr.rectangle(80, y + 180, 920, 22)
        fill_stroke(cr, rgb("#9AA3B2"), 4)
    cr.rectangle(70, 620, 20, 940); cr.rectangle(990, 620, 20, 940)
    cr.set_source_rgb(*rgb("#7F8C99")); cr.fill()


def draw_living(cr):
    cr.set_source_rgb(*rgb("#F6DCC8"))
    cr.paint()
    _floor(cr, 1560, "#A9744F")
    cr.rectangle(690, 600, 360, 520)
    fill_stroke(cr, (1, 1, 1), 7)
    cr.rectangle(710, 620, 320, 480)
    cr.set_source_rgb(*rgb("#9FDBF5")); cr.fill()
    rrect(cr, 120, 1300, 840, 30, 8)
    fill_stroke(cr, rgb("#C9A27A"), 5)
    cr.rectangle(160, 1330, 760, 230)
    fill_stroke(cr, rgb("#A9825C"), 5)


def draw_beach(cr):
    g = cairo.LinearGradient(0, 0, 0, 1100)
    g.add_color_stop_rgb(0, *rgb("#5AB2EA"))
    g.add_color_stop_rgb(1, *rgb("#DDF3FB"))
    cr.set_source(g)
    cr.paint()
    cr.arc(850, 620, 70, 0, 2 * math.pi)
    cr.set_source_rgb(*rgb("#FFE58A")); cr.fill()
    cr.move_to(0, 1600); cr.line_to(W, 1250); cr.line_to(W, H); cr.line_to(0, H); cr.close_path()
    cr.set_source_rgb(*rgb("#F0D9A0")); cr.fill()


def draw_hill(cr):
    g = cairo.LinearGradient(0, 0, 0, 1500)
    g.add_color_stop_rgb(0, *rgb("#0B1026"))
    g.add_color_stop_rgb(1, *rgb("#26315A"))
    cr.set_source(g)
    cr.paint()
    random.seed(12)
    for _ in range(90):
        cr.arc(random.uniform(0, W), random.uniform(380, 1300), random.uniform(1, 2.4), 0, 2 * math.pi)
        cr.set_source_rgba(1, 1, 1, random.uniform(0.3, 0.8)); cr.fill()
    cr.move_to(0, 1500); cr.curve_to(300, 1400, 700, 1420, W, 1520); cr.line_to(W, H); cr.line_to(0, H)
    cr.close_path(); cr.set_source_rgb(*rgb("#1D3A2A")); cr.fill()


BGS = {
    "dark": surface(draw_dark), "bedroom": surface(draw_bedroom), "street": surface(draw_street),
    "cafe": surface(draw_cafe), "bank": surface(draw_bank), "airport": surface(draw_airport),
    "shop": surface(draw_shop), "living": surface(draw_living), "beach": surface(draw_beach),
    "hill": surface(draw_hill),
}


# ------------------------------------------------------------------ dynamische Elemente
def phone(cr, x, y, scale=1.0, screen="#1B1F27", content=None):
    cr.save(); cr.translate(x, y); cr.scale(scale, scale)
    rrect(cr, -70, -130, 140, 260, 22)
    fill_stroke(cr, rgb("#15181F"), 5)
    rrect(cr, -58, -112, 116, 224, 12)
    cr.set_source_rgb(*rgb(screen)); cr.fill()
    if content:
        content(cr)
    cr.restore()


def no_signal(cr, x, y, s=1.0):
    cr.save(); cr.translate(x, y); cr.scale(s, s)
    for k in range(4):
        cr.rectangle(-45 + k * 25, 20 - k * 18, 16, 20 + k * 18)
        cr.set_source_rgb(*rgb("#9AA3B2")); cr.fill()
    cr.move_to(-55, -50); cr.line_to(55, 45)
    cr.set_source_rgb(*rgb("#E23B3B")); cr.set_line_width(10); cr.stroke()
    cr.restore()


def zzz(cr, x, y, t):
    for k in range(3):
        ph = (t * 0.6 + k / 3) % 1
        cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(40 + 30 * ph)
        cr.set_source_rgba(1, 1, 1, 1 - ph)
        cr.move_to(x + ph * 80, y - ph * 160)
        cr.show_text("z")


def globe(cr, cx, cy, R, tilt=0.4, spin=0.0):
    cr.save(); cr.translate(cx, cy); cr.rotate(tilt)
    cr.arc(0, 0, R, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#2F6FB0"), 6, rgb("#9FC8F0"))
    cr.save(); cr.arc(0, 0, R, 0, 2 * math.pi); cr.clip()
    cr.set_source_rgb(*rgb("#5DB870"))
    for (x, y, r) in ((-0.35, -0.3, 0.33), (0.2, -0.1, 0.25), (0.4, 0.35, 0.3), (-0.25, 0.4, 0.22)):
        xx = ((x + spin) % 2.0) - 1.0
        cr.arc(xx * R * 1.3, y * R, r * R, 0, 2 * math.pi); cr.fill()
    cr.restore()
    cr.move_to(0, -R - 70); cr.line_to(0, R + 70)
    cr.set_source_rgb(*rgb("#FFD45C")); cr.set_line_width(6); cr.stroke()
    cr.restore()


def moon(cr, x, y, r, alpha=1.0):
    cr.arc(x, y, r, 0, 2 * math.pi)
    cr.set_source_rgba(0.96, 0.95, 0.85, alpha); cr.fill()
    for (dx, dy, rr) in ((-0.3, -0.2, 0.18), (0.25, 0.1, 0.22), (-0.1, 0.35, 0.12)):
        cr.arc(x + dx * r, y + dy * r, rr * r, 0, 2 * math.pi)
        cr.set_source_rgba(0.82, 0.81, 0.72, alpha); cr.fill()
