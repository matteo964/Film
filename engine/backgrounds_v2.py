"""Hintergründe im Illustrationsstil (Perspektive, weiches Licht) – Referenz 4."""
import math
import random

import cairo
from backgrounds import rgb, _text, fill_stroke
from stickman import stroke_black, rrect

W, H = 1080, 1920
VP = (540, 760)          # Fluchtpunkt
WALL_TOP, WALL_BOT = 330, 1240


def _lerp(a, b, t):
    return a + (b - a) * t


def _shade(c, f):
    return tuple(max(0, min(1, x * f)) for x in c)


def room(cr, wall, floor, tiles="tile", side=None, ceiling=(0.93, 0.94, 0.96)):
    """Raum: Rückwand, Seitenwände, Decke, perspektivischer Boden."""
    side = side or _shade(wall, 0.82)
    # Decke
    cr.rectangle(0, 0, W, WALL_TOP)
    cr.set_source_rgb(*ceiling); cr.fill()
    # Rückwand
    g = cairo.LinearGradient(0, WALL_TOP, 0, WALL_BOT)
    g.add_color_stop_rgb(0, *_shade(wall, 1.04)); g.add_color_stop_rgb(1, *_shade(wall, 0.92))
    cr.rectangle(0, WALL_TOP, W, WALL_BOT - WALL_TOP); cr.set_source(g); cr.fill()
    # Boden
    g = cairo.LinearGradient(0, WALL_BOT, 0, H)
    g.add_color_stop_rgb(0, *_shade(floor, 0.92)); g.add_color_stop_rgb(1, *_shade(floor, 1.06))
    cr.rectangle(0, WALL_BOT, W, H - WALL_BOT); cr.set_source(g); cr.fill()
    cr.set_line_width(2.5)
    cr.set_source_rgba(0, 0, 0, 0.10)
    if tiles == "tile":
        for k in range(-14, 15):
            x0 = 540 + k * 70
            cr.move_to(x0, WALL_BOT); cr.line_to(540 + k * 260, H)
        y, step = WALL_BOT, 30
        while y < H:
            cr.move_to(0, y); cr.line_to(W, y)
            y += step; step *= 1.35
        cr.stroke()
    elif tiles == "wood":
        for k in range(-20, 21):
            cr.move_to(540 + k * 45, WALL_BOT); cr.line_to(540 + k * 170, H)
        cr.stroke()
    # Sockelleiste + Kantenschatten
    cr.rectangle(0, WALL_BOT - 14, W, 14)
    cr.set_source_rgb(*_shade(wall, 0.7)); cr.fill()
    g = cairo.LinearGradient(0, WALL_BOT, 0, WALL_BOT + 60)
    g.add_color_stop_rgba(0, 0, 0, 0, 0.18); g.add_color_stop_rgba(1, 0, 0, 0, 0)
    cr.rectangle(0, WALL_BOT, W, 60); cr.set_source(g); cr.fill()
    g = cairo.LinearGradient(0, WALL_TOP, 0, WALL_TOP + 50)
    g.add_color_stop_rgba(0, 0, 0, 0, 0.15); g.add_color_stop_rgba(1, 0, 0, 0, 0)
    cr.rectangle(0, WALL_TOP, W, 50); cr.set_source(g); cr.fill()


def ceiling_lamp(cr, x, cone=True):
    cr.move_to(x, 0); cr.line_to(x, 250); stroke_black(cr, 3)
    cr.move_to(x - 90, 300); cr.curve_to(x - 80, 250, x + 80, 250, x + 90, 300); cr.close_path()
    fill_stroke(cr, rgb("#E9EDF2"), 4, rgb("#5E6A78"))
    if cone:
        g = cairo.LinearGradient(0, 300, 0, 1500)
        g.add_color_stop_rgba(0, 1, 1, 0.95, 0.28); g.add_color_stop_rgba(1, 1, 1, 0.95, 0)
        cr.move_to(x - 85, 300); cr.line_to(x + 85, 300); cr.line_to(x + 380, 1500); cr.line_to(x - 380, 1500)
        cr.close_path(); cr.set_source(g); cr.fill()


def sun_beams(cr, x0, y0, w, h, ang=0.55, alpha=0.20):
    for k in range(3):
        g = cairo.LinearGradient(x0, y0, x0 + 600, y0 + 900)
        g.add_color_stop_rgba(0, 1, 0.98, 0.9, alpha); g.add_color_stop_rgba(1, 1, 0.98, 0.9, 0)
        ox = x0 + k * w / 3
        cr.move_to(ox, y0); cr.line_to(ox + w / 4, y0)
        cr.line_to(ox + w / 4 + h * ang * 2.2, y0 + h * 2.2); cr.line_to(ox + h * ang * 2.2, y0 + h * 2.2)
        cr.close_path(); cr.set_source(g); cr.fill()


def window_city(cr, x, y, w, h, night=False):
    cr.rectangle(x, y, w, h)
    fill_stroke(cr, rgb("#F4F6F8"), 8, rgb("#9AA6B2"))
    ix, iy, iw, ih = x + 16, y + 16, w - 32, h - 32
    cr.save(); cr.rectangle(ix, iy, iw, ih); cr.clip()
    g = cairo.LinearGradient(0, iy, 0, iy + ih)
    if night:
        g.add_color_stop_rgb(0, *rgb("#0E1630")); g.add_color_stop_rgb(1, *rgb("#26315A"))
    else:
        g.add_color_stop_rgb(0, *rgb("#9ED4F2")); g.add_color_stop_rgb(1, *rgb("#E3F4FB"))
    cr.set_source(g); cr.paint()
    random.seed(int(x + y))
    xx = ix
    while xx < ix + iw:
        bw, bh = random.randint(50, 110), random.randint(int(ih * 0.3), int(ih * 0.85))
        cr.rectangle(xx, iy + ih - bh, bw, bh)
        cr.set_source_rgb(*(rgb("#1A2547") if night else rgb("#B7D3E3"))); cr.fill()
        for yy in range(int(iy + ih - bh + 14), int(iy + ih), 26):
            for wx in range(int(xx + 8), int(xx + bw - 10), 18):
                if random.random() < (0.5 if night else 0.35):
                    cr.rectangle(wx, yy, 8, 12)
                    cr.set_source_rgb(*(rgb("#FFD86B") if night else rgb("#D6E8F2"))); cr.fill()
        xx += bw + random.randint(6, 16)
    cr.restore()
    cr.move_to(x + w / 2, y); cr.line_to(x + w / 2, y + h)
    cr.set_source_rgb(*rgb("#9AA6B2")); cr.set_line_width(8); cr.stroke()


def plant(cr, x, y, s=1.0):
    cr.save(); cr.translate(x, y); cr.scale(s, s)
    for (a, l) in ((-0.9, 150), (-0.5, 190), (-0.1, 210), (0.3, 190), (0.7, 160), (1.0, 130)):
        cr.move_to(0, -60)
        cx, cy = math.sin(a) * l, -60 - math.cos(a) * l
        cr.curve_to(cx * 0.3, -60 - l * 0.4, cx * 0.8 + 20, cy + 30, cx, cy)
        cr.curve_to(cx * 0.8 - 20, cy + 40, cx * 0.2, -60 - l * 0.3, 0, -60)
        cr.set_source_rgb(*rgb("#4E9A5A")); cr.fill_preserve(); stroke_black(cr, 3)
    rrect(cr, -55, -70, 110, 90, 14)
    fill_stroke(cr, rgb("#E9E2D6"), 4)
    cr.restore()


def frame_art(cr, x, y, w, h):
    cr.rectangle(x, y, w, h)
    fill_stroke(cr, rgb("#F7F4EE"), 6, rgb("#3B3B3B"))
    cr.arc(x + w * 0.5, y + h * 0.48, min(w, h) * 0.28, 0.3, 5.6)
    cr.set_source_rgb(*rgb("#C9B79C")); cr.set_line_width(5); cr.stroke()


def bookshelf(cr, x, y, w, h):
    cr.rectangle(x, y, w, h)
    fill_stroke(cr, rgb("#8A6446"), 6)
    random.seed(int(x))
    for r in range(4):
        sy = y + 20 + r * (h - 40) / 4
        cr.rectangle(x + 10, sy + (h - 40) / 4 - 12, w - 20, 10)
        cr.set_source_rgb(*rgb("#6E4E36")); cr.fill()
        bx = x + 16
        while bx < x + w - 30:
            bw = random.randint(14, 26); bh = random.randint(50, (h - 40) // 4 - 18)
            cr.rectangle(bx, sy + (h - 40) / 4 - 12 - bh, bw, bh)
            fill_stroke(cr, rgb(random.choice(("#C0504D", "#4F81BD", "#9BBB59", "#F2C230", "#8064A2", "#E9E2D6"))), 2)
            bx += bw + 3


# ------------------------------------------------------------------ Sets
def boss_office():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(s)
    room(cr, rgb("#D8D2C8"), rgb("#B88A5E"), tiles="wood")
    window_city(cr, 40, 470, 520, 640)
    sun_beams(cr, 60, 480, 500, 640)
    bookshelf(cr, 720, 500, 300, 740)
    frame_art(cr, 600, 560, 90, 120)
    plant(cr, 650, 1240, 0.9)
    s.flush()
    return s


def boss_desk(cr):
    """Schreibtisch vorn (über den Beinen der Figur hinter dem Tisch)."""
    rrect(cr, 120, 1290, 840, 40, 10)
    fill_stroke(cr, rgb("#7A5233"), 5)
    cr.rectangle(150, 1330, 780, 250)
    fill_stroke(cr, rgb("#6A4529"), 5)
    cr.rectangle(190, 1370, 320, 170)
    fill_stroke(cr, rgb("#5E3D24"), 3)
    rrect(cr, 640, 1170, 220, 130, 10)
    fill_stroke(cr, rgb("#2B2F38"), 5)
    cr.rectangle(730, 1290, 40, 10); cr.set_source_rgb(*rgb("#2B2F38")); cr.fill()
    cr.rectangle(220, 1270, 120, 20); fill_stroke(cr, (1, 1, 1), 3)


def open_office():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(s)
    room(cr, rgb("#4F7AA8"), rgb("#E6ECF2"), tiles="tile")
    # Wandbildschirm
    rrect(cr, 90, 520, 380, 230, 12)
    fill_stroke(cr, rgb("#1B2230"), 6, rgb("#8EA0B2"))
    for k in range(5):
        cr.rectangle(120, 560 + k * 34, 120 + (k * 47) % 160, 14)
        cr.set_source_rgb(*rgb(("#5BEA8B", "#FFB36B", "#7FB2FF")[k % 3])); cr.fill()
    # Arbeitsplätze in Perspektive
    for (x, y, sc) in ((620, 1150, 0.8), (860, 1170, 0.85)):
        cr.save(); cr.translate(x, y); cr.scale(sc, sc)
        rrect(cr, -90, -170, 180, 120, 10); fill_stroke(cr, rgb("#E9EDF2"), 5, rgb("#3B4555"))
        cr.rectangle(-15, -50, 30, 30); fill_stroke(cr, rgb("#9AA6B2"), 3)
        cr.rectangle(-170, -20, 340, 26); fill_stroke(cr, rgb("#3B4555"), 4)
        cr.rectangle(-150, 6, 20, 100); cr.rectangle(130, 6, 20, 100)
        cr.set_source_rgb(*rgb("#3B4555")); cr.fill()
        cr.restore()
    ceiling_lamp(cr, 300)
    ceiling_lamp(cr, 820)
    s.flush()
    return s


def meeting(mode="slides"):
    def make():
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(s)
        room(cr, rgb("#E6E2DA"), rgb("#9A8C7E"), tiles="wood")
        window_city(cr, 820, 470, 230, 640)
        sun_beams(cr, 830, 480, 220, 640, alpha=0.15)
        sx, sy, sw, sh = 100, 450, 680, 420
        rrect(cr, sx, sy, sw, sh, 12)
        fill_stroke(cr, rgb("#1B1F27"), 8)
        ix, iy, iw, ih = sx + 18, sy + 18, sw - 36, sh - 36
        cr.save(); cr.rectangle(ix, iy, iw, ih); cr.clip()
        cr.set_source_rgb(1, 1, 1); cr.paint()
        cr.rectangle(ix, iy, iw, 64); cr.set_source_rgb(*rgb("#1F3B63")); cr.fill()
        if mode == "slides":
            _text(cr, "HENDERSON GROUP · Q1 PLAN", ix + iw / 2, iy + 44, 28, (1, 1, 1))
            for k, (a, b) in enumerate((("Revenue", "+18%"), ("New stores", "12"), ("Budget", "$2.4M"))):
                _text(cr, a, ix + 50, iy + 130 + k * 70, 34, rgb("#1F3B63"), center=False)
                _text(cr, b, ix + iw - 170, iy + 130 + k * 70, 34, rgb("#1F8A47"), center=False)
        elif mode == "fail":
            _text(cr, "HENDRSON GRUOP · Q1 PLAN", ix + iw / 2, iy + 44, 28, (1, 1, 1))
            _text(cr, "Revenue:  vibes ↑", ix + 50, iy + 140, 34, rgb("#E23B3B"), center=False)
            _text(cr, "Strategy:  just grind", ix + 50, iy + 205, 34, rgb("#E23B3B"), center=False)
            # Meme-Bild
            rrect(cr, ix + iw - 230, iy + 110, 190, 190, 12)
            cr.set_source_rgb(*rgb("#FFD45C")); cr.fill()
            _text(cr, "LET'S", ix + iw - 135, iy + 190, 40, rgb("#1B1F27"))
            _text(cr, "GOOO", ix + iw - 135, iy + 240, 40, rgb("#1B1F27"))
        elif mode == "signed":
            _text(cr, "HENDERSON GROUP · CONTRACT", ix + iw / 2, iy + 44, 28, (1, 1, 1))
            cr.arc(ix + iw / 2, iy + 185, 70, 0, 2 * math.pi)
            fill_stroke(cr, rgb("#33C46A"), 5)
            cr.move_to(ix + iw / 2 - 34, iy + 185); cr.line_to(ix + iw / 2 - 6, iy + 213); cr.line_to(ix + iw / 2 + 38, iy + 157)
            cr.set_source_rgb(1, 1, 1); cr.set_line_width(15); cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
            _text(cr, "RENEWED · Account lead: Emma Clarke", ix + iw / 2, iy + 320, 30, rgb("#1F8A47"))
        cr.restore()
        rrect(cr, 60, 1300, 960, 44, 12)
        fill_stroke(cr, rgb("#F2F2F2"), 5, rgb("#6E6E6E"))
        cr.rectangle(120, 1344, 840, 120)
        cr.set_source_rgba(0, 0, 0, 0.08); cr.fill()
        s.flush()
        return s
    return make


def living():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(s)
    room(cr, rgb("#F3F1EC"), rgb("#E7D8C2"), tiles="wood", ceiling=(0.97, 0.97, 0.96))
    frame_art(cr, 300, 560, 220, 290)
    window_city(cr, 780, 480, 260, 560)
    sun_beams(cr, 790, 490, 250, 560, ang=-0.45, alpha=0.18)
    plant(cr, 140, 1240, 0.8)
    # Teppich
    cr.move_to(150, 1500); cr.line_to(930, 1500); cr.line_to(1040, 1780); cr.line_to(40, 1780); cr.close_path()
    cr.set_source_rgb(*rgb("#FBF9F5")); cr.fill_preserve(); cr.set_source_rgba(0, 0, 0, 0.08); cr.set_line_width(3); cr.stroke()
    s.flush()
    return s


def sofa_back(cr):
    rrect(cr, 200, 1120, 700, 230, 40)
    fill_stroke(cr, rgb("#ECE8E1"), 5, rgb("#8C857A"))
    for (x, c) in ((250, "#F7F4EE"), (720, "#E9D9BD")):
        rrect(cr, x, 1150, 140, 110, 30)
        fill_stroke(cr, rgb(c), 4, rgb("#8C857A"))


def sofa_front(cr):
    rrect(cr, 200, 1300, 700, 150, 30)
    fill_stroke(cr, rgb("#F4F1EB"), 5, rgb("#8C857A"))
    for x in (170, 840):
        rrect(cr, x, 1230, 90, 230, 30)
        fill_stroke(cr, rgb("#E4DFD6"), 5, rgb("#8C857A"))
    # Decke über der Lehne
    cr.move_to(700, 1300); cr.curve_to(760, 1280, 820, 1290, 860, 1320); cr.line_to(860, 1420); cr.line_to(720, 1400)
    cr.close_path(); fill_stroke(cr, rgb("#E9C9A0"), 4, rgb("#8C857A"))
