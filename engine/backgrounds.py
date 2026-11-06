"""Flat-Cartoon-Hintergründe (1080x1920)."""
import math
import random
import cairo
from stickman import rrect, stroke_black, BLACK

W, H = 1080, 1920


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def fill_stroke(cr, col, lw=5, line=BLACK):
    cr.set_source_rgb(*col)
    cr.fill_preserve()
    cr.set_source_rgb(*line)
    cr.set_line_width(lw)
    cr.set_line_join(cairo.LINE_JOIN_ROUND)
    cr.stroke()


# ---------------------------------------------------------------- Büro
def office(cold=False):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    wall = rgb("#F7E3A8") if not cold else rgb("#D5E0EA")
    floor = rgb("#F2D5B1") if not cold else rgb("#C9D3DE")
    cr.set_source_rgb(*wall)
    cr.paint()
    # Fußleiste + Boden
    cr.rectangle(0, 1560, W, H - 1560)
    cr.set_source_rgb(*floor)
    cr.fill()
    cr.rectangle(0, 1545, W, 18)
    cr.set_source_rgb(*(rgb("#E2B47E") if not cold else rgb("#9FB0C2")))
    cr.fill()
    # Bodenfugen
    cr.set_source_rgba(0, 0, 0, 0.06)
    cr.set_line_width(3)
    for i in range(-3, 9):
        cr.move_to(540 + i * 160, 1563)
        cr.line_to(540 + i * 260, H)
    cr.stroke()

    # Fenster
    wx, wy, ww, wh = -20, 640, 880, 540
    cr.rectangle(wx, wy, ww, wh)
    fill_stroke(cr, rgb("#FFF7E6") if not cold else rgb("#EEF3F8"), 6)
    panes = [(wx + 30, wy + 26, 250, wh - 52), (wx + 300, wy + 26, 250, wh - 52), (wx + 570, wy + 26, 280, wh - 52)]
    for (px, py, pw, ph) in panes:
        cr.save()
        cr.rectangle(px, py, pw, ph)
        cr.clip()
        g = cairo.LinearGradient(0, py, 0, py + ph)
        if not cold:
            g.add_color_stop_rgb(0, *rgb("#D8F7F2"))
            g.add_color_stop_rgb(1, *rgb("#A6E9E1"))
        else:
            g.add_color_stop_rgb(0, *rgb("#C3CCD6"))
            g.add_color_stop_rgb(1, *rgb("#E6ECF2"))
        cr.set_source(g)
        cr.paint()
        # Skyline
        random.seed(7)
        cr.set_source_rgb(*(rgb("#B5E3DC") if not cold else rgb("#AEB9C5")))
        x = wx
        while x < wx + ww:
            bw = random.randint(50, 110)
            bh = random.randint(120, 300)
            cr.rectangle(x, wy + wh - 120 - bh, bw, bh + 120)
            x += bw + random.randint(4, 20)
        cr.fill()
        # Hecke / Bäume
        if not cold:
            for i, col in enumerate(("#6CC04A", "#55AE3B")):
                cr.set_source_rgb(*rgb(col))
                for k in range(14):
                    cx = wx + k * 70 + i * 35
                    cr.arc(cx, wy + wh - 70 + i * 25, 55 - i * 8, 0, 2 * math.pi)
                    cr.fill()
        else:
            cr.set_source_rgb(*rgb("#F5F8FB"))
            cr.rectangle(wx, wy + wh - 90, ww, 90)
            cr.fill()
            for k in range(14):
                cr.arc(wx + k * 70, wy + wh - 90, 40, math.pi, 2 * math.pi)
                cr.fill()
        # Lichtstreifen
        cr.set_source_rgba(1, 1, 1, 0.35)
        for k in range(3):
            ox = px + k * 120 - 60
            cr.move_to(ox, py + ph)
            cr.line_to(ox + 50, py + ph)
            cr.line_to(ox + 230, py)
            cr.line_to(ox + 180, py)
            cr.close_path()
            cr.fill()
        if cold:
            # Eisblumen in den Ecken
            cr.set_source_rgba(1, 1, 1, 0.85)
            for (cx, cy) in ((px, py), (px + pw, py), (px, py + ph), (px + pw, py + ph)):
                cr.arc(cx, cy, 70, 0, 2 * math.pi)
                cr.fill()
            cr.set_source_rgba(1, 1, 1, 0.5)
            for (cx, cy) in ((px, py), (px + pw, py), (px, py + ph), (px + pw, py + ph)):
                cr.arc(cx, cy, 110, 0, 2 * math.pi)
                cr.fill()
        cr.restore()
        cr.rectangle(px, py, pw, ph)
        cr.set_source_rgb(*BLACK)
        cr.set_line_width(5)
        cr.stroke()

    # Uhr
    cx, cy = 400, 520
    cr.arc(cx, cy, 52, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#E5683C"), 5)
    cr.arc(cx, cy, 40, 0, 2 * math.pi)
    fill_stroke(cr, (1, 1, 1), 3)
    cr.move_to(cx, cy)
    cr.line_to(cx, cy - 28)
    cr.move_to(cx, cy)
    cr.line_to(cx + 20, cy + 6)
    stroke_black(cr, 5)

    # Bild rechts
    cr.rectangle(1000, 640, 120, 160)
    fill_stroke(cr, rgb("#D9442B"), 5)
    cr.rectangle(1018, 660, 90, 120)
    fill_stroke(cr, rgb("#BFE7F0"), 3)
    cr.move_to(1018, 780)
    cr.line_to(1050, 715)
    cr.line_to(1075, 750)
    cr.line_to(1090, 730)
    cr.line_to(1108, 780)
    cr.close_path()
    fill_stroke(cr, rgb("#5A8F5E"), 3)

    if cold:
        # Thermometer an der Wand
        tx, ty = 960, 900
        rrect(cr, tx - 28, ty, 56, 230, 26)
        fill_stroke(cr, (1, 1, 1), 5)
        cr.arc(tx, ty + 195, 22, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#3D8BFF"), 4)
        cr.rectangle(tx - 7, ty + 140, 14, 50)
        cr.set_source_rgb(*rgb("#3D8BFF"))
        cr.fill()
        cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(40)
        cr.set_source_rgb(*rgb("#1E5BC6"))
        cr.move_to(tx - 38, ty - 18)
        cr.show_text("9°C")
    surf.flush()
    return surf


def office_chair(cr, x, y, cold=False):
    """Roter Chefsessel; x,y = Mitte Lehne oben."""
    col = rgb("#8E1D27")
    rrect(cr, x - 150, y, 300, 330, 60)
    fill_stroke(cr, col, 6)
    rrect(cr, x - 120, y + 25, 240, 280, 45)
    cr.set_source_rgba(1, 1, 1, 0.08)
    cr.fill()


def office_desk(cr, cold=False):
    """Roter Schreibtisch mit Monitor/Stiftebecher."""
    top = rgb("#E04A24")
    front = rgb("#C3161C")
    dark = rgb("#A10F15")
    # Monitor (Rückseite)
    rrect(cr, 560, 1060, 230, 175, 12)
    fill_stroke(cr, rgb("#3A3E46"), 5)
    cr.rectangle(650, 1230, 50, 30)
    fill_stroke(cr, rgb("#3A3E46"), 4)
    # Tastatur, Papier
    cr.rectangle(190, 1238, 230, 22)
    fill_stroke(cr, rgb("#3A3E46"), 4)
    cr.rectangle(40, 1240, 110, 18)
    fill_stroke(cr, (0.97, 0.97, 0.97), 3)
    # Stiftebecher
    for i, c in enumerate(("#F2C230", "#E34B3D", "#3D8BFF", "#5AC05A")):
        cr.move_to(880 + i * 14, 1190)
        cr.line_to(876 + i * 14, 1150 - (i % 2) * 18)
        cr.set_source_rgb(*rgb(c))
        cr.set_line_width(9)
        cr.stroke()
    rrect(cr, 862, 1180, 70, 80, 8)
    fill_stroke(cr, rgb("#3FB37F"), 4)
    # Tischplatte
    cr.rectangle(-30, 1255, 1020, 34)
    fill_stroke(cr, top, 5)
    # Front
    cr.rectangle(-10, 1289, 980, 330)
    fill_stroke(cr, front, 5)
    for (px, pw) in ((20, 420), (480, 460)):
        cr.rectangle(px, 1320, pw, 120)
        fill_stroke(cr, front, 4, dark)
        cr.rectangle(px, 1460, pw, 130)
        fill_stroke(cr, front, 4, dark)
    # Stuhlfuß unter dem Tisch sichtbar
    cr.set_source_rgba(0, 0, 0, 0.12)
    cr.rectangle(-10, 1600, 980, 20)
    cr.fill()


# ---------------------------------------------------------------- Heizungskeller
def cellar():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    g = cairo.LinearGradient(0, 0, 0, H)
    g.add_color_stop_rgb(0, *rgb("#1E2A33"))
    g.add_color_stop_rgb(1, *rgb("#2E3E49"))
    cr.set_source(g)
    cr.paint()
    # Ziegel-Andeutung
    cr.set_source_rgba(1, 1, 1, 0.04)
    cr.set_line_width(3)
    for row in range(0, 1560, 70):
        cr.move_to(0, row)
        cr.line_to(W, row)
        off = 0 if (row // 70) % 2 else 70
        for x in range(off, W, 140):
            cr.move_to(x, row)
            cr.line_to(x, row + 70)
    cr.stroke()
    cr.rectangle(0, 1560, W, H - 1560)
    cr.set_source_rgb(*rgb("#3A4752"))
    cr.fill()
    # Rohre
    for (y, c) in ((420, "#B5562E"), (480, "#7D8A94")):
        cr.rectangle(-10, y, W + 20, 34)
        fill_stroke(cr, rgb(c), 5)
        for x in range(60, W, 240):
            cr.rectangle(x, y - 8, 26, 50)
            fill_stroke(cr, rgb("#5E6A73"), 4)
    cr.rectangle(880, 450, 34, 900)
    fill_stroke(cr, rgb("#B5562E"), 5)
    # Kessel
    rrect(cr, 260, 760, 520, 820, 70)
    fill_stroke(cr, rgb("#8F9BA5"), 7)
    rrect(cr, 290, 790, 120, 760, 40)
    cr.set_source_rgba(1, 1, 1, 0.15)
    cr.fill()
    for y in (900, 1180, 1460):
        cr.move_to(262, y)
        cr.line_to(778, y)
        stroke_black(cr, 5)
        for x in range(290, 780, 60):
            cr.arc(x, y, 6, 0, 2 * math.pi)
            cr.set_source_rgb(*BLACK)
            cr.fill()
    # Rohr oben
    cr.rectangle(480, 470, 80, 300)
    fill_stroke(cr, rgb("#7D8A94"), 6)
    # Typenschild
    rrect(cr, 400, 960, 240, 120, 10)
    fill_stroke(cr, rgb("#D9C27A"), 5)
    cr.select_font_face("DejaVu Sans Mono", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(34)
    cr.set_source_rgb(*BLACK)
    for i, s in enumerate(("KESSEL 1", "BJ. 1987")):
        ext = cr.text_extents(s)
        cr.move_to(520 - ext.width / 2, 1010 + i * 46)
        cr.show_text(s)
    # Manometer-Gehäuse (Nadel in overlay)
    cr.new_path()
    cr.arc(520, 1300, 95, 0, 2 * math.pi)
    fill_stroke(cr, (0.97, 0.97, 0.95), 7)
    cr.arc(520, 1300, 75, math.pi * 0.8, math.pi * 1.25)
    cr.set_source_rgb(*rgb("#E23B3B"))
    cr.set_line_width(14)
    cr.stroke()
    cr.arc(520, 1300, 75, math.pi * 1.3, math.pi * 2.2)
    cr.set_source_rgb(*rgb("#4CC25A"))
    cr.stroke()
    # Lampe-Gehäuse
    cr.rectangle(500, 655, 40, 30)
    fill_stroke(cr, rgb("#444444"), 4)
    surf.flush()
    return surf


def cellar_overlay(cr, t):
    # Nadel fällt in den roten Bereich
    p = min(1.0, t / 2.0)
    ang = math.pi * (1.9 - 0.95 * p) + math.sin(t * 30) * 0.03 * (1 - p)
    cr.move_to(520, 1300)
    cr.line_to(520 + 70 * math.cos(ang), 1300 + 70 * math.sin(ang))
    stroke_black(cr, 7)
    cr.arc(520, 1300, 12, 0, 2 * math.pi)
    cr.set_source_rgb(*BLACK)
    cr.fill()
    on = (int(t * 3) % 2) == 0
    cr.new_path()
    cr.arc(520, 630, 34, math.pi, 2 * math.pi)
    cr.close_path()
    cr.set_source_rgb(*(rgb("#FF2A2A") if on else rgb("#7A1515")))
    cr.fill_preserve()
    stroke_black(cr, 4)
    if on:
        g = cairo.RadialGradient(520, 620, 10, 520, 620, 520)
        g.add_color_stop_rgba(0, 1, 0.1, 0.1, 0.35)
        g.add_color_stop_rgba(1, 1, 0.1, 0.1, 0)
        cr.set_source(g)
        cr.paint()
    # Dampfwölkchen
    for k in range(3):
        ph = (t * 0.8 + k / 3) % 1
        cr.arc(600 + ph * 120, 760 - ph * 260, 30 + ph * 50, 0, 2 * math.pi)
        cr.set_source_rgba(0.9, 0.9, 0.95, 0.35 * (1 - ph))
        cr.fill()


# ---------------------------------------------------------------- Flur mit Aufzug
def corridor():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    cr.set_source_rgb(*rgb("#A9C0D3"))
    cr.paint()
    cr.rectangle(0, 1560, W, H - 1560)
    cr.set_source_rgb(*rgb("#DCE6EE"))
    cr.fill()
    cr.set_source_rgba(0, 0, 0, 0.08)
    cr.set_line_width(3)
    for i in range(-4, 10):
        cr.move_to(540 + i * 140, 1560)
        cr.line_to(540 + i * 300, H)
    for y in (1640, 1760, 1900):
        cr.move_to(0, y)
        cr.line_to(W, y)
    cr.stroke()
    cr.rectangle(0, 1545, W, 18)
    cr.set_source_rgb(*rgb("#7F97AB"))
    cr.fill()
    # Aufzug-Rahmen
    cr.rectangle(250, 780, 580, 780)
    fill_stroke(cr, rgb("#6F8193"), 7)
    cr.rectangle(285, 815, 255, 745)
    fill_stroke(cr, rgb("#BAC5CF"), 5)
    cr.rectangle(540, 815, 255, 745)
    fill_stroke(cr, rgb("#BAC5CF"), 5)
    cr.set_source_rgba(1, 1, 1, 0.3)
    for x in (300, 555):
        cr.move_to(x + 30, 830)
        cr.line_to(x + 60, 830)
        cr.line_to(x + 20, 1540)
        cr.line_to(x - 10, 1540)
        cr.close_path()
        cr.fill()
    # Display-Kasten
    rrect(cr, 380, 640, 320, 110, 12)
    fill_stroke(cr, rgb("#1B1F24"), 6)
    # Rufknöpfe
    rrect(cr, 880, 1080, 80, 170, 12)
    fill_stroke(cr, rgb("#C9D2DA"), 5)
    for y in (1125, 1205):
        cr.arc(920, y, 20, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#F2F2F2"), 4)
    # Schild
    rrect(cr, 60, 700, 140, 90, 10)
    fill_stroke(cr, rgb("#2F7D4F"), 5)
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(40)
    cr.set_source_rgb(1, 1, 1)
    cr.move_to(88, 760)
    cr.show_text("3.OG")
    # Topfpflanze
    rrect(cr, 900, 1420, 110, 140, 14)
    fill_stroke(cr, rgb("#C46A3C"), 5)
    for (dx, dy, r) in ((-30, -40, 50), (30, -60, 55), (0, -110, 55)):
        cr.arc(955 + dx, 1420 + dy, r, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#4FA63E"), 5)
    surf.flush()
    return surf


def corridor_overlay(cr, t):
    on = (int(t * 2.5) % 2) == 0
    cr.select_font_face("DejaVu Sans Mono", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(58)
    s = "STÖRUNG"
    ext = cr.text_extents(s)
    cr.set_source_rgb(*(rgb("#FF3030") if on else rgb("#5A1010")))
    cr.move_to(540 - ext.width / 2 - ext.x_bearing, 715)
    cr.show_text(s)
    # Alarmleuchte
    cr.new_path()
    cr.arc(540, 600, 36, math.pi, 2 * math.pi)
    cr.close_path()
    cr.set_source_rgb(*(rgb("#FF2A2A") if on else rgb("#8A1A1A")))
    cr.fill_preserve()
    stroke_black(cr, 4)
    cr.rectangle(494, 598, 92, 16)
    cr.set_source_rgb(*rgb("#444444"))
    cr.fill()
    if on:
        g = cairo.RadialGradient(540, 590, 10, 540, 590, 420)
        g.add_color_stop_rgba(0, 1, 0.15, 0.15, 0.30)
        g.add_color_stop_rgba(1, 1, 0.15, 0.15, 0)
        cr.set_source(g)
        cr.paint()


def snow_overlay(cr, t):
    """Schneeflocken im Fenster (Büro kalt)."""
    random.seed(3)
    cr.save()
    cr.rectangle(10, 666, 840, 488)
    cr.clip()
    cr.set_source_rgba(1, 1, 1, 0.95)
    for i in range(70):
        x0 = random.uniform(0, 860)
        sp = random.uniform(40, 90)
        r = random.uniform(3, 7)
        y = 640 + (random.uniform(0, 540) + t * sp) % 540
        x = x0 + math.sin(t + i) * 12
        cr.arc(x, y, r, 0, 2 * math.pi)
        cr.fill()
    cr.restore()
