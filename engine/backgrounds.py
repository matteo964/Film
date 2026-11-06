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


def _text(cr, s, x, y, size, col, font="TikTok Sans", bold=True, center=True):
    cr.select_font_face(font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(size)
    e = cr.text_extents(s)
    cr.new_path()
    cr.move_to(x - (e.width / 2 + e.x_bearing if center else 0), y)
    cr.set_source_rgb(*col)
    cr.show_text(s)
    cr.new_path()


# ---------------------------------------------------------------- Penthouse (Nacht)
def penthouse():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    g = cairo.LinearGradient(0, 0, 0, H)
    g.add_color_stop_rgb(0, *rgb("#22305A"))
    g.add_color_stop_rgb(1, *rgb("#2F4170"))
    cr.set_source(g)
    cr.paint()
    # Boden Holz dunkel
    cr.rectangle(0, 1560, W, H - 1560)
    cr.set_source_rgb(*rgb("#4A3427"))
    cr.fill()
    cr.set_source_rgba(0, 0, 0, 0.18)
    cr.set_line_width(3)
    for y in range(1600, H, 60):
        cr.move_to(0, y)
        cr.line_to(W, y)
    cr.stroke()
    # Großes Fenster mit Skyline
    wx, wy, ww, wh = 560, 560, 540, 860
    cr.rectangle(wx, wy, ww, wh)
    fill_stroke(cr, rgb("#0E1630"), 7)
    cr.save()
    cr.rectangle(wx, wy, ww, wh)
    cr.clip()
    cr.arc(wx + 380, wy + 140, 55, 0, 2 * math.pi)
    cr.set_source_rgb(*rgb("#F4F1D0"))
    cr.fill()
    random.seed(11)
    x = wx
    while x < wx + ww:
        bw, bh = random.randint(60, 120), random.randint(260, 640)
        cr.rectangle(x, wy + wh - bh, bw, bh)
        cr.set_source_rgb(*rgb("#1A2547"))
        cr.fill()
        for yy in range(int(wy + wh - bh + 20), wy + wh, 34):
            for xx in range(x + 12, x + bw - 12, 24):
                if random.random() < 0.45:
                    cr.rectangle(xx, yy, 12, 16)
                    cr.set_source_rgb(*rgb("#FFD86B"))
                    cr.fill()
        x += bw + random.randint(6, 18)
    cr.restore()
    cr.move_to(wx + ww / 2, wy)
    cr.line_to(wx + ww / 2, wy + wh)
    cr.move_to(wx, wy + wh / 2)
    cr.line_to(wx + ww, wy + wh / 2)
    cr.set_source_rgb(*BLACK)
    cr.set_line_width(7)
    cr.stroke()
    # Bild an der Wand: Magazin-Cover
    fx, fy = 70, 465
    cr.rectangle(fx, fy, 300, 400)
    fill_stroke(cr, rgb("#C9A24A"), 7)
    cr.rectangle(fx + 22, fy + 22, 256, 356)
    fill_stroke(cr, rgb("#F4EEE2"), 4)
    _text(cr, "BUSINESS", fx + 150, fy + 75, 40, rgb("#B3261E"))
    _text(cr, "WEEKLY", fx + 150, fy + 115, 34, rgb("#B3261E"))
    cr.arc(fx + 150, fy + 210, 55, 0, 2 * math.pi)
    fill_stroke(cr, (1, 1, 1), 5)
    cr.arc(fx + 150, fy + 210, 55, math.pi * 1.05, math.pi * 1.95)
    cr.set_source_rgb(0.1, 0.1, 0.1)
    cr.fill()
    _text(cr, "?", fx + 150, fy + 238, 60, rgb("#B3261E"))
    _text(cr, "THE INVISIBLE", fx + 150, fy + 310, 30, BLACK)
    _text(cr, "OWNER", fx + 150, fy + 348, 34, BLACK)
    # Stehlampe
    cr.move_to(480, 1560)
    cr.line_to(480, 1060)
    stroke_black(cr, 8)
    cr.move_to(420, 1060)
    cr.line_to(540, 1060)
    cr.line_to(515, 960)
    cr.line_to(445, 960)
    cr.close_path()
    fill_stroke(cr, rgb("#F6D488"), 5)
    gl = cairo.RadialGradient(480, 1060, 10, 480, 1060, 420)
    gl.add_color_stop_rgba(0, 1, 0.85, 0.45, 0.35)
    gl.add_color_stop_rgba(1, 1, 0.85, 0.45, 0)
    cr.set_source(gl)
    cr.paint()
    surf.flush()
    return surf


def sofa_back(cr):
    rrect(cr, 30, 1150, 640, 260, 50)
    fill_stroke(cr, rgb("#5C86C8"), 6)


def sofa_front(cr):
    rrect(cr, 30, 1330, 640, 150, 30)
    fill_stroke(cr, rgb("#4F78B8"), 6)
    for x in (10, 620):
        rrect(cr, x, 1250, 80, 230, 30)
        fill_stroke(cr, rgb("#456CA9"), 6)
    for x in (80, 600):
        cr.rectangle(x, 1480, 22, 60)
        fill_stroke(cr, rgb("#2B2B2B"), 4)


# ---------------------------------------------------------------- Konferenzraum
def conference():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    cr.set_source_rgb(*rgb("#E3EAF1"))
    cr.paint()
    cr.rectangle(0, 0, W, 470)
    cr.set_source_rgb(*rgb("#D3DDE7"))
    cr.fill()
    cr.rectangle(0, 1560, W, H - 1560)
    cr.set_source_rgb(*rgb("#B98A5E"))
    cr.fill()
    cr.set_source_rgba(0, 0, 0, 0.12)
    cr.set_line_width(3)
    for x in range(-200, W + 400, 120):
        cr.move_to(x, 1560)
        cr.line_to(x - 200, H)
    cr.stroke()
    cr.rectangle(0, 1545, W, 18)
    cr.set_source_rgb(*rgb("#8EA0B2"))
    cr.fill()
    # Firmenschriftzug
    _text(cr, "HAYES INDUSTRIES", 540, 560, 54, rgb("#2C4A6E"))
    cr.rectangle(340, 580, 400, 6)
    cr.set_source_rgb(*rgb("#E0A33A"))
    cr.fill()
    # Bildschirm mit Chart
    sx, sy, sw, sh = 250, 640, 580, 360
    rrect(cr, sx, sy, sw, sh, 14)
    fill_stroke(cr, rgb("#22262E"), 7)
    cr.rectangle(sx + 24, sy + 24, sw - 48, sh - 48)
    cr.set_source_rgb(*rgb("#F7F9FC"))
    cr.fill()
    _text(cr, "Q3 RESULTS", sx + sw / 2, sy + 80, 40, rgb("#22262E"))
    for i, (hgt, c) in enumerate(((90, "#7BB6F0"), (140, "#7BB6F0"), (120, "#7BB6F0"), (200, "#3D8BFF"))):
        bx = sx + 90 + i * 110
        cr.rectangle(bx, sy + sh - 50 - hgt, 70, hgt)
        fill_stroke(cr, rgb(c), 3)
    # Fenster rechts / Pflanze links
    cr.rectangle(900, 640, 220, 560)
    fill_stroke(cr, rgb("#BFE3F2"), 6)
    cr.move_to(900, 920)
    cr.line_to(1120, 920)
    stroke_black(cr, 5)
    rrect(cr, 60, 1400, 120, 150, 14)
    fill_stroke(cr, rgb("#5E6B78"), 5)
    for (dx, dy, r) in ((-35, -40, 55), (35, -70, 60), (0, -130, 60)):
        cr.arc(120 + dx, 1400 + dy, r, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#4FA63E"), 5)
    # Stuhllehnen + langer Tisch
    for x in (250, 420, 590, 760):
        rrect(cr, x, 1110, 120, 200, 30)
        fill_stroke(cr, rgb("#3A3F48"), 5)
    rrect(cr, 180, 1270, 760, 46, 14)
    fill_stroke(cr, rgb("#8A5A36"), 6)
    cr.rectangle(220, 1316, 680, 120)
    fill_stroke(cr, rgb("#734A2C"), 5)
    # Laptop auf Tisch
    cr.move_to(470, 1272)
    cr.line_to(490, 1200)
    cr.line_to(590, 1200)
    cr.line_to(600, 1272)
    cr.close_path()
    fill_stroke(cr, rgb("#9AA5B1"), 4)
    surf.flush()
    return surf


# ---------------------------------------------------------------- Wohnung (Tag)
def apartment():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    cr.set_source_rgb(*rgb("#F6DCC8"))
    cr.paint()
    cr.rectangle(0, 1560, W, H - 1560)
    cr.set_source_rgb(*rgb("#A9744F"))
    cr.fill()
    cr.set_source_rgba(0, 0, 0, 0.12)
    cr.set_line_width(3)
    for y in range(1600, H, 55):
        cr.move_to(0, y)
        cr.line_to(W, y)
    cr.stroke()
    cr.rectangle(0, 1545, W, 18)
    cr.set_source_rgb(*rgb("#E7BFA3"))
    cr.fill()
    # Fenster rechts (Tag)
    wx, wy, ww, wh = 690, 600, 420, 620
    cr.rectangle(wx, wy, ww, wh)
    fill_stroke(cr, rgb("#FFFFFF"), 7)
    cr.save()
    cr.rectangle(wx + 20, wy + 20, ww - 40, wh - 40)
    cr.clip()
    g = cairo.LinearGradient(0, wy, 0, wy + wh)
    g.add_color_stop_rgb(0, *rgb("#9FDBF5"))
    g.add_color_stop_rgb(1, *rgb("#DDF3FB"))
    cr.set_source(g)
    cr.paint()
    random.seed(5)
    x = wx
    while x < wx + ww:
        bw, bh = random.randint(60, 110), random.randint(160, 380)
        cr.rectangle(x, wy + wh - bh, bw, bh)
        cr.set_source_rgb(*rgb("#B9D7E6"))
        cr.fill()
        x += bw + 10
    cr.restore()
    cr.move_to(wx + ww / 2, wy)
    cr.line_to(wx + ww / 2, wy + wh)
    stroke_black(cr, 6)
    cr.rectangle(wx, wy, ww, wh)
    stroke_black(cr, 7)
    # Poster
    for (px, py, col, txt) in ((90, 560, "#2E3A59", "SHIP IT"), (360, 600, "#E7664D", "</>")):
        cr.rectangle(px, py, 230, 300)
        fill_stroke(cr, rgb("#8B5E3C"), 6)
        cr.rectangle(px + 16, py + 16, 198, 268)
        fill_stroke(cr, rgb(col), 3)
        _text(cr, txt, px + 115, py + 170, 44, (1, 1, 1))
    # Regal
    cr.rectangle(110, 960, 460, 16)
    fill_stroke(cr, rgb("#8B5E3C"), 4)
    for i, c in enumerate(("#E7664D", "#3D8BFF", "#F2C230", "#5AC05A", "#7A5AF5", "#E7664D")):
        cr.rectangle(140 + i * 44, 870, 34, 90)
        fill_stroke(cr, rgb(c), 3)
    cr.arc(470, 920, 40, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#4FA63E"), 4)
    cr.rectangle(450, 925, 40, 35)
    fill_stroke(cr, rgb("#C46A3C"), 4)
    surf.flush()
    return surf


def couch_back(cr):
    rrect(cr, 30, 1150, 640, 260, 50)
    fill_stroke(cr, rgb("#6FAF8C"), 6)


def couch_front(cr):
    rrect(cr, 30, 1330, 640, 150, 30)
    fill_stroke(cr, rgb("#5E9E7B"), 6)
    for x in (10, 620):
        rrect(cr, x, 1250, 80, 230, 30)
        fill_stroke(cr, rgb("#548F6F"), 6)
    for x in (80, 600):
        cr.rectangle(x, 1480, 22, 60)
        fill_stroke(cr, rgb("#2B2B2B"), 4)


# ---------------------------------------------------------------- Launch-Bühne
def stage(mode="site"):
    def make():
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surf)
        g = cairo.LinearGradient(0, 0, 0, H)
        g.add_color_stop_rgb(0, *rgb("#141B33"))
        g.add_color_stop_rgb(1, *rgb("#26315A"))
        cr.set_source(g)
        cr.paint()
        cr.rectangle(0, 1560, W, H - 1560)
        cr.set_source_rgb(*rgb("#3B2A4F"))
        cr.fill()
        cr.rectangle(0, 1545, W, 18)
        cr.set_source_rgb(*rgb("#5B4775"))
        cr.fill()
        # Spots
        for sx in (180, 900):
            cr.move_to(sx - 30, 440)
            cr.line_to(sx + 30, 440)
            cr.line_to(sx + 260 * (1 if sx < 540 else -1) + 160, 1560)
            cr.line_to(sx + 260 * (1 if sx < 540 else -1) - 160, 1560)
            cr.close_path()
            cr.set_source_rgba(1, 0.95, 0.75, 0.0)
            cr.fill()
        # Banner
        rrect(cr, 330, 412, 420, 70, 14)
        fill_stroke(cr, rgb("#E0A33A"), 5)
        _text(cr, "LAUNCH DAY", 540, 463, 40, rgb("#1B1F2E"))
        # Leinwand
        sx, sy, sw, sh = 90, 495, 900, 400
        rrect(cr, sx, sy, sw, sh, 12)
        fill_stroke(cr, rgb("#0B0E16"), 8)
        ix, iy, iw, ih = sx + 22, sy + 22, sw - 44, sh - 44
        cr.save()
        cr.rectangle(ix, iy, iw, ih)
        cr.clip()
        if mode in ("site", "back"):
            cr.set_source_rgb(1, 1, 1)
            cr.paint()
            cr.rectangle(ix, iy, iw, 48)
            cr.set_source_rgb(*rgb("#1E2A44"))
            cr.fill()
            _text(cr, "GRANT & CO.", ix + 120, iy + 34, 26, (1, 1, 1))
            for k, s in enumerate(("Home", "Products", "Contact")):
                _text(cr, s, ix + 520 + k * 110, iy + 32, 20, rgb("#C9D3E6"), bold=False)
            g2 = cairo.LinearGradient(ix, iy + 48, ix + iw, iy + 250)
            g2.add_color_stop_rgb(0, *rgb("#5B8CFF"))
            g2.add_color_stop_rgb(1, *rgb("#9A6BFF"))
            cr.rectangle(ix, iy + 48, iw, 200)
            cr.set_source(g2)
            cr.fill()
            _text(cr, "Building the Future.", ix + iw / 2, iy + 135, 48, (1, 1, 1))
            rrect(cr, ix + iw / 2 - 110, iy + 165, 220, 52, 26)
            fill_stroke(cr, rgb("#FFD45C"), 3)
            _text(cr, "Get started", ix + iw / 2, iy + 200, 26, rgb("#1B1F2E"))
            for k in range(3):
                rrect(cr, ix + 40 + k * 280, iy + 268, 240, 70, 12)
                fill_stroke(cr, rgb("#EEF2FA"), 3, rgb("#C9D3E6"))
            if mode == "back":
                rrect(cr, ix + iw - 230, iy + 60, 210, 52, 26)
                fill_stroke(cr, rgb("#33C46A"), 3)
                _text(cr, "ONLINE", ix + iw - 125, iy + 96, 28, (1, 1, 1))
        else:
            cr.set_source_rgb(*rgb("#1A0B0E"))
            cr.paint()
            cr.move_to(ix + iw / 2, iy + 18)
            cr.line_to(ix + iw / 2 + 50, iy + 105)
            cr.line_to(ix + iw / 2 - 50, iy + 105)
            cr.close_path()
            fill_stroke(cr, rgb("#FF3B3B"), 5, rgb("#FF3B3B"))
            _text(cr, "!", ix + iw / 2, iy + 98, 58, rgb("#1A0B0E"))
            _text(cr, "WEBSITE SUSPENDED", ix + iw / 2, iy + 165, 54, rgb("#FF3B3B"))
            _text(cr, "Reason: Invoice #1042 unpaid", ix + iw / 2, iy + 220, 34, (1, 1, 1), bold=False)
            _text(cr, "Amount due: $4,800", ix + iw / 2, iy + 265, 34, (1, 1, 1), bold=False)
            _text(cr, "Contact: Zoe Parker Design", ix + iw / 2, iy + 315, 30, rgb("#FFB3B3"), bold=False)
        cr.restore()
        surf.flush()
        return surf
    return make


def podium(cr):
    cr.move_to(150, 1260)
    cr.line_to(370, 1260)
    cr.line_to(345, 1560)
    cr.line_to(175, 1560)
    cr.close_path()
    fill_stroke(cr, rgb("#2C2F3A"), 6)
    rrect(cr, 135, 1240, 250, 34, 8)
    fill_stroke(cr, rgb("#3A3E4C"), 5)
    _text(cr, "G&C", 260, 1420, 50, rgb("#E0A33A"))
    cr.move_to(300, 1240)
    cr.line_to(330, 1150)
    stroke_black(cr, 5)
    cr.arc(333, 1140, 12, 0, 2 * math.pi)
    cr.set_source_rgb(*BLACK)
    cr.fill()


# ---------------------------------------------------------------- Klassenzimmer
def _chalk(cr, s, x, y, size=40, col=(0.96, 0.96, 0.92)):
    cr.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(size)
    cr.new_path()
    cr.move_to(x, y)
    cr.set_source_rgb(*col)
    cr.show_text(s)
    cr.new_path()


def classroom(board="final"):
    def make():
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surf)
        cr.set_source_rgb(*rgb("#F3E9C6"))
        cr.paint()
        cr.rectangle(0, 1250, W, 310)
        cr.set_source_rgb(*rgb("#9FC7A0"))
        cr.fill()
        cr.rectangle(0, 1240, W, 14)
        cr.set_source_rgb(*rgb("#7DAA80"))
        cr.fill()
        cr.rectangle(0, 1560, W, H - 1560)
        cr.set_source_rgb(*rgb("#C9A27A"))
        cr.fill()
        cr.set_source_rgba(0, 0, 0, 0.10)
        cr.set_line_width(3)
        for x in range(-300, W + 300, 130):
            cr.move_to(x, 1560)
            cr.line_to(x + (x - 540) * 0.6, H)
        cr.stroke()
        # Uhr
        cr.arc(980, 520, 46, 0, 2 * math.pi)
        fill_stroke(cr, (1, 1, 1), 6)
        cr.move_to(980, 520)
        cr.line_to(980, 490)
        cr.move_to(980, 520)
        cr.line_to(1000, 532)
        stroke_black(cr, 5)
        # Tafel
        bx, by, bw, bh = 70, 440, 860, 480
        rrect(cr, bx - 20, by - 20, bw + 40, bh + 40, 10)
        fill_stroke(cr, rgb("#9A6A3F"), 6)
        cr.rectangle(bx, by, bw, bh)
        fill_stroke(cr, rgb("#2F5D46"), 5)
        cr.set_source_rgba(1, 1, 1, 0.05)
        for k in range(5):
            cr.arc(bx + 150 + k * 170, by + 200 + (k % 2) * 90, 90, 0, 2 * math.pi)
            cr.fill()
        cr.rectangle(bx, by + bh + 20, bw, 18)
        fill_stroke(cr, rgb("#8A5D36"), 4)
        cr.rectangle(bx + 600, by + bh + 8, 70, 14)
        fill_stroke(cr, rgb("#EEEEEE"), 3)
        if board == "final":
            _chalk(cr, "CALCULUS FINAL", bx + 40, by + 80, 52)
            _chalk(cr, "Class average: 61%", bx + 40, by + 160, 40)
            _chalk(cr, "Highest score: ???", bx + 40, by + 225, 40)
            _chalk(cr, "No phones. No excuses.", bx + 40, by + 300, 36, rgb("#F7D774"))
        elif board in ("problem", "solved"):
            _chalk(cr, "BONUS PROBLEM", bx + 40, by + 70, 46, rgb("#F7D774"))
            _chalk(cr, "∫ (2t+3) dt  from 1 to x  =  66", bx + 40, by + 140, 40)
            _chalk(cr, "Solve for x  (x > 0)", bx + 40, by + 195, 38)
            if board == "solved":
                _chalk(cr, "x² + 3x − 4 = 66   →   (x + 10)(x − 7) = 0", bx + 40, by + 265, 36)
                _chalk(cr, "x = 7  ✓", bx + 40, by + 330, 46, rgb("#9BF29B"))
                _chalk(cr, "Answer key: 9 ?  → line 3 divides by 2 twice!", bx + 40, by + 405, 32, rgb("#FF8A8A"))
                cr.arc(bx + 110, by + 316, 70, 0, 2 * math.pi)
                cr.set_source_rgb(*rgb("#FF8A8A"))
                cr.set_line_width(5)
                cr.stroke()
        # Lehrerpult rechts unten
        rrect(cr, 760, 1300, 300, 30, 6)
        fill_stroke(cr, rgb("#A26B3E"), 5)
        cr.rectangle(780, 1330, 260, 230)
        fill_stroke(cr, rgb("#8B5A33"), 5)
        cr.arc(840, 1270, 26, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#D9442B"), 4)
        cr.move_to(840, 1244)
        cr.line_to(846, 1230)
        stroke_black(cr, 4)
        for k in range(3):
            cr.rectangle(900, 1290 - k * 16, 120, 14)
            fill_stroke(cr, rgb(("#3D8BFF", "#F2C230", "#5AC05A")[k]), 3)
        surf.flush()
        return surf
    return make


def student_desk(cr, x=150):
    rrect(cr, x - 120, 1330, 240, 24, 6)
    fill_stroke(cr, rgb("#C99B6D"), 5)
    for dx in (-100, 100):
        cr.move_to(x + dx, 1354)
        cr.line_to(x + dx, 1560)
        stroke_black(cr, 8)
