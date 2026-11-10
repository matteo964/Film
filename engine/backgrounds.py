"""Flat-Cartoon-Hintergründe (1080x1920)."""
import math
import random
import cairo
from stickman import rrect, stroke_black, BLACK

W, H = 1080, 1920
CLOCK = {"lt": 0.0, "t": 0.0}  # von render.py pro Frame gesetzt (lt = Zeit seit Shot-Beginn)


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


# ---------------------------------------------------------------- Großraumbüro mit Wand-Screen
def openoffice(mode="logo"):
    def bot(cr, x, y, r):
        rrect(cr, x - r, y - r * 0.8, 2 * r, 1.6 * r, r * 0.35)
        fill_stroke(cr, rgb("#5B8CFF"), 4)
        for dx in (-r * 0.4, r * 0.4):
            cr.arc(x + dx, y - r * 0.1, r * 0.22, 0, 2 * math.pi)
            fill_stroke(cr, (1, 1, 1), 3)
        cr.move_to(x - r * 0.35, y + r * 0.35)
        cr.curve_to(x - r * 0.1, y + r * 0.55, x + r * 0.1, y + r * 0.55, x + r * 0.35, y + r * 0.35)
        stroke_black(cr, 4)
        cr.move_to(x, y - r * 0.8)
        cr.line_to(x, y - r * 1.15)
        stroke_black(cr, 4)
        cr.arc(x, y - r * 1.2, r * 0.12, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#FFD45C"), 3)

    def make():
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surf)
        cr.set_source_rgb(*rgb("#E8EEF3"))
        cr.paint()
        cr.rectangle(0, 1560, W, H - 1560)
        cr.set_source_rgb(*rgb("#9AA7B4"))
        cr.fill()
        cr.set_source_rgba(0, 0, 0, 0.08)
        cr.set_line_width(3)
        for y in (1620, 1700, 1800, 1920):
            cr.move_to(0, y)
            cr.line_to(W, y)
        cr.stroke()
        cr.rectangle(0, 1545, W, 18)
        cr.set_source_rgb(*rgb("#7E8C99"))
        cr.fill()
        # Fenster
        for wx in (0, 860):
            cr.rectangle(wx, 640, 220, 520)
            fill_stroke(cr, rgb("#C6E6F5"), 6)
            cr.move_to(wx + 110, 640)
            cr.line_to(wx + 110, 1160)
            stroke_black(cr, 4)
        # Wand-Screen
        sx, sy, sw, sh = 200, 470, 680, 420
        rrect(cr, sx, sy, sw, sh, 14)
        fill_stroke(cr, rgb("#1B1F27"), 8)
        ix, iy, iw, ih = sx + 20, sy + 20, sw - 40, sh - 40
        cr.save()
        cr.rectangle(ix, iy, iw, ih)
        cr.clip()
        cr.set_source_rgb(*rgb("#F4F7FD"))
        cr.paint()
        cr.rectangle(ix, iy, iw, 54)
        cr.set_source_rgb(*rgb("#2D3E66"))
        cr.fill()
        _text(cr, "PayBot 3000  ·  AI Payroll", ix + iw / 2, iy + 38, 28, (1, 1, 1))
        if mode == "logo":
            bot(cr, ix + iw / 2, iy + 175, 80)
            _text(cr, "Payroll on autopilot!", ix + iw / 2, iy + 320, 36, rgb("#2D3E66"))
        elif mode == "error":
            bot(cr, ix + 90, iy + 140, 46)
            rrect(cr, ix + 160, iy + 80, iw - 190, 210, 18)
            fill_stroke(cr, (1, 1, 1), 3, rgb("#C9D3E6"))
            _text(cr, "Sorry! I can't access the bank.", ix + 175, iy + 130, 28, rgb("#1B1F27"), bold=False, center=False)
            _text(cr, "Please contact the", ix + 175, iy + 180, 28, rgb("#1B1F27"), bold=False, center=False)
            _text(cr, "authorized signer:", ix + 175, iy + 220, 28, rgb("#1B1F27"), bold=False, center=False)
            _text(cr, "DAVE MILLER", ix + 175, iy + 268, 34, rgb("#E23B3B"), center=False)
            rrect(cr, ix + 30, iy + 305, iw - 60, 40, 10)
            fill_stroke(cr, rgb("#FFE3E3"), 3, rgb("#E23B3B"))
            _text(cr, "Payroll status: FAILED  (0 / 200 paid)", ix + iw / 2, iy + 334, 26, rgb("#B3261E"))
        elif mode == "paid":
            cr.arc(ix + iw / 2, iy + 170, 80, 0, 2 * math.pi)
            fill_stroke(cr, rgb("#33C46A"), 5)
            cr.move_to(ix + iw / 2 - 40, iy + 170)
            cr.line_to(ix + iw / 2 - 10, iy + 200)
            cr.line_to(ix + iw / 2 + 45, iy + 140)
            cr.set_source_rgb(1, 1, 1)
            cr.set_line_width(16)
            cr.set_line_cap(cairo.LINE_CAP_ROUND)
            cr.stroke()
            _text(cr, "PAYROLL COMPLETE", ix + iw / 2, iy + 305, 40, rgb("#1F8A47"))
            _text(cr, "200 / 200 paid  ·  approved by D. Miller", ix + iw / 2, iy + 345, 24, rgb("#2D3E66"), bold=False)
        cr.restore()
        # Schreibtischreihe hinten
        for dx in (60, 400, 740):
            rrect(cr, dx + 70, 1150, 140, 100, 8)
            fill_stroke(cr, rgb("#3A3F48"), 4)
            cr.rectangle(dx + 130, 1250, 20, 30)
            fill_stroke(cr, rgb("#3A3F48"), 3)
        cr.rectangle(30, 1280, 1020, 26)
        fill_stroke(cr, rgb("#D9DEE4"), 5)
        cr.rectangle(50, 1306, 980, 140)
        fill_stroke(cr, rgb("#BCC4CD"), 5)
        surf.flush()
        return surf
    return make


# ---------------------------------------------------------------- Marketing-Raum mit Social-Media-Screen
def _heart(cr, x, y, r, col):
    cr.new_path()
    cr.move_to(x, y + r * 0.9)
    cr.curve_to(x - r * 1.6, y - r * 0.2, x - r * 0.6, y - r * 1.3, x, y - r * 0.35)
    cr.curve_to(x + r * 0.6, y - r * 1.3, x + r * 1.6, y - r * 0.2, x, y + r * 0.9)
    cr.close_path()
    cr.set_source_rgb(*col)
    cr.fill()


def _mini_stick(cr, x, y, s, shirt, dance=False, bun=False):
    cr.save()
    cr.translate(x, y)
    cr.scale(s, s)
    if bun:
        cr.arc(-30, -128, 14, 0, 2 * math.pi)
        fill_stroke(cr, (1, 1, 1), 3)
    cr.arc(0, -110, 30, 0, 2 * math.pi)
    fill_stroke(cr, (1, 1, 1), 3)
    cr.rectangle(-12, -80, 24, 60)
    fill_stroke(cr, shirt, 3)
    if dance:
        cr.move_to(-12, -75); cr.line_to(-45, -110)
        cr.move_to(12, -75); cr.line_to(48, -60)
        cr.move_to(-6, -20); cr.line_to(-30, 20)
        cr.move_to(6, -20); cr.line_to(26, 22)
    else:
        cr.move_to(-12, -75); cr.line_to(-22, -30)
        cr.move_to(12, -75); cr.line_to(22, -30)
        cr.move_to(-6, -20); cr.line_to(-12, 22)
        cr.move_to(6, -20); cr.line_to(12, 22)
    stroke_black(cr, 4)
    cr.restore()


def socialroom(mode="profile"):
    CYAN = (0.15, 0.80, 0.91)
    WHITE = (0.99, 0.99, 0.99)

    def make():
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surf)
        cr.set_source_rgb(*rgb("#F1E4D3"))
        cr.paint()
        cr.rectangle(0, 1560, W, H - 1560)
        cr.set_source_rgb(*rgb("#8C6A4F"))
        cr.fill()
        cr.rectangle(0, 1545, W, 18)
        cr.set_source_rgb(*rgb("#6E523C"))
        cr.fill()
        # Firmenlogo
        _text(cr, "BEAN & CO.", 125, 610, 30, rgb("#6E3B1F"))
        cr.arc(125, 525, 42, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#6E3B1F"), 5)
        cr.save(); cr.translate(125, 525); cr.scale(16, 26)
        cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
        fill_stroke(cr, rgb("#C98A55"), 3)
        # Ringlicht
        cr.arc(1000, 960, 60, 0, 2 * math.pi)
        cr.set_source_rgb(*rgb("#FFF6D8")); cr.set_line_width(22); cr.stroke()
        cr.arc(1000, 960, 60, 0, 2 * math.pi)
        cr.set_source_rgb(*BLACK); cr.set_line_width(3); cr.stroke()
        cr.move_to(1000, 1020); cr.line_to(1000, 1560)
        cr.move_to(1000, 1560); cr.line_to(955, 1560)
        cr.move_to(1000, 1560); cr.line_to(1045, 1560)
        stroke_black(cr, 7)
        # Wand-Screen
        sx, sy, sw, sh = 250, 440, 600, 470
        rrect(cr, sx, sy, sw, sh, 16)
        fill_stroke(cr, rgb("#15181F"), 8)
        ix, iy, iw, ih = sx + 18, sy + 18, sw - 36, sh - 36
        cr.save()
        cr.rectangle(ix, iy, iw, ih)
        cr.clip()
        cr.set_source_rgb(*rgb("#101217"))
        cr.paint()
        if mode in ("profile", "flop", "back"):
            # Profilkopf
            cr.arc(ix + 70, iy + 70, 44, 0, 2 * math.pi)
            fill_stroke(cr, rgb("#C98A55"), 4, rgb("#FF4F7B"))
            _text(cr, "B&C", ix + 70, iy + 82, 26, (1, 1, 1))
            _text(cr, "@beanandco", ix + 135, iy + 58, 30, (1, 1, 1), center=False)
            fol = {"profile": "2.1M", "flop": "1.4M", "back": "2.6M"}[mode]
            col = {"profile": (1, 1, 1), "flop": rgb("#FF5A5A"), "back": rgb("#5BEA8B")}[mode]
            _text(cr, fol, ix + 135, iy + 102, 34, col, center=False)
            _text(cr, "followers", ix + 135 + 15 + len(fol) * 20, iy + 102, 24, rgb("#9AA3B2"), bold=False, center=False)
            if mode == "flop":
                _text(cr, "-700K", ix + iw - 150, iy + 102, 30, rgb("#FF5A5A"), center=False)
            if mode == "back":
                _text(cr, "+500K", ix + iw - 160, iy + 102, 30, rgb("#5BEA8B"), center=False)
            # Video-Kachel
            vx, vy, vw, vh = ix + 30, iy + 140, 190, 260
            rrect(cr, vx, vy, vw, vh, 12)
            g = cairo.LinearGradient(0, vy, 0, vy + vh)
            g.add_color_stop_rgb(0, *rgb("#FFB36B")); g.add_color_stop_rgb(1, *rgb("#FF5E8A"))
            cr.set_source(g); cr.fill()
            if mode == "profile":
                _mini_stick(cr, vx + vw / 2, vy + vh - 40, 1.0, CYAN, dance=True)
                likes, l2 = "1.2M", "48K comments"
            elif mode == "flop":
                _mini_stick(cr, vx + vw / 2, vy + vh - 40, 1.0, WHITE, dance=True)
                likes, l2 = "12", "3.4K comments"
            else:
                _mini_stick(cr, vx + vw / 2 - 40, vy + vh - 40, 0.8, CYAN, dance=True)
                _mini_stick(cr, vx + vw / 2 + 40, vy + vh - 40, 0.8, WHITE, dance=True)
                likes, l2 = "3.9M", "210K comments"
            _heart(cr, vx + 30, vy + 30, 14, rgb("#FF4F7B"))
            _text(cr, likes, vx + 52, vy + 40, 26, (1, 1, 1), center=False)
            # Kommentare
            com = {
                "profile": ["Best coffee account ever!", "Chloe never misses", "Ordering right now!"],
                "flop": ["Who is this guy??", "WHERE IS CHLOE", "my grandpa dances better", "Unfollowed."],
                "back": ["CHLOE IS BACK!!", "Rick's apology dance lol", "Best video they ever made"],
            }[mode]
            _text(cr, l2, ix + 250, iy + 170, 24, rgb("#9AA3B2"), bold=False, center=False)
            for k, s in enumerate(com):
                rrect(cr, ix + 245, iy + 190 + k * 58, iw - 270, 48, 12)
                cr.set_source_rgb(*rgb("#232733")); cr.fill()
                _text(cr, s, ix + 260, iy + 223 + k * 58, 22,
                      rgb("#FF8A8A") if mode == "flop" else (1, 1, 1), bold=False, center=False)
        elif mode == "chloe":
            cr.arc(ix + 70, iy + 70, 44, 0, 2 * math.pi)
            fill_stroke(cr, rgb("#25C9E6"), 4, rgb("#FF4F7B"))
            _text(cr, "@chloe.creates", ix + 135, iy + 75, 32, (1, 1, 1), center=False)
            vx, vy, vw, vh = ix + 30, iy + 135, iw - 60, 200
            rrect(cr, vx, vy, vw, vh, 12)
            g = cairo.LinearGradient(vx, 0, vx + vw, 0)
            g.add_color_stop_rgb(0, *rgb("#5B8CFF")); g.add_color_stop_rgb(1, *rgb("#9A6BFF"))
            cr.set_source(g); cr.fill()
            _mini_stick(cr, vx + 90, vy + vh - 25, 1.1, CYAN)
            _text(cr, "I got fired for making", vx + 175, vy + 85, 28, (1, 1, 1), center=False)
            _text(cr, "my company go viral", vx + 175, vy + 125, 28, (1, 1, 1), center=False)
            _text(cr, "5.2M views", ix + 40, iy + 385, 34, rgb("#5BEA8B"), center=False)
            _heart(cr, ix + 330, iy + 373, 15, rgb("#FF4F7B"))
            _text(cr, "980K", ix + 355, iy + 385, 30, (1, 1, 1), center=False)
            _text(cr, "\"Boycott Bean & Co until Chloe is back\"", ix + iw / 2, iy + 425, 22, rgb("#FFB3B3"), bold=False)
        cr.restore()
        # Sofa / Tisch vorne
        rrect(cr, 330, 1300, 420, 30, 8)
        fill_stroke(cr, rgb("#C9A27A"), 5)
        cr.rectangle(360, 1330, 360, 150)
        fill_stroke(cr, rgb("#A9825C"), 5)
        surf.flush()
        return surf
    return make


# ---------------------------------------------------------------- Callcenter mit Wand-Screen
def callcenter(mode="queue"):
    def make():
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surf)
        cr.set_source_rgb(*rgb("#DDE7EF"))
        cr.paint()
        cr.rectangle(0, 1560, W, H - 1560)
        cr.set_source_rgb(*rgb("#5E6E80"))
        cr.fill()
        cr.set_source_rgba(0, 0, 0, 0.10)
        cr.set_line_width(3)
        for x in range(-300, W + 300, 120):
            cr.move_to(x, 1560); cr.line_to(x + (x - 540) * 0.5, H)
        cr.stroke()
        cr.rectangle(0, 1545, W, 18)
        cr.set_source_rgb(*rgb("#4A586A"))
        cr.fill()
        _text(cr, "CUSTOMER CARE", 540, 445, 34, rgb("#2C4A6E"))
        sx, sy, sw, sh = 160, 470, 760, 430
        rrect(cr, sx, sy, sw, sh, 14)
        fill_stroke(cr, rgb("#151922"), 8)
        ix, iy, iw, ih = sx + 20, sy + 20, sw - 40, sh - 40
        cr.save()
        cr.rectangle(ix, iy, iw, ih)
        cr.clip()
        cr.set_source_rgb(*rgb("#0F1320"))
        cr.paint()
        if mode == "queue":
            _text(cr, "LIVE QUEUE", ix + iw / 2, iy + 60, 36, rgb("#7FB2FF"))
            stats = [("CALLS WAITING", "12", "#FFD45C"), ("AVG HOLD", "4:32", "#FFFFFF"), ("TOP AGENT", "MAYA  98%", "#5BEA8B")]
            for k, (a, b, c) in enumerate(stats):
                y = iy + 140 + k * 85
                rrect(cr, ix + 40, y - 45, iw - 80, 70, 12)
                cr.set_source_rgb(*rgb("#1C2233")); cr.fill()
                _text(cr, a, ix + 70, y, 30, rgb("#9AA3B2"), center=False)
                _text(cr, b, ix + iw - 70 - len(b) * 19, y, 34, rgb(c), center=False)
        elif mode == "recording":
            cr.arc(ix + 50, iy + 50, 14, 0, 2 * math.pi)
            cr.set_source_rgb(*rgb("#FF3B3B")); cr.fill()
            _text(cr, "CALL #4471  ·  09:42 AM  ·  RECORDED", ix + 80, iy + 62, 28, (1, 1, 1), center=False)
            random.seed(9)
            for k in range(70):
                x = ix + 40 + k * 9.4
                h = (abs(math.sin(k * 0.45)) * 70 + random.uniform(5, 60)) * (1.6 if 18 < k < 44 else 0.8)
                cr.rectangle(x, iy + 200 - h / 2, 6, h)
                cr.set_source_rgb(*(rgb("#FF6B6B") if 18 < k < 44 else rgb("#5BEA8B")))
                cr.fill()
            _text(cr, "Customer", ix + 260, iy + 330, 26, rgb("#FF6B6B"), center=False)
            _text(cr, "Agent", ix + 40, iy + 330, 26, rgb("#5BEA8B"), center=False)
            cr.rectangle(ix + 40, iy + 352, iw - 80, 8)
            cr.set_source_rgb(*rgb("#2A3145")); cr.fill()
            cr.rectangle(ix + 40, iy + 352, (iw - 80) * 0.45, 8)
            cr.set_source_rgb(*rgb("#7FB2FF")); cr.fill()
        elif mode == "report":
            _text(cr, "QUALITY ASSURANCE · MYSTERY SHOPPER REPORT", ix + iw / 2, iy + 50, 24, rgb("#FFD45C"))
            rows = [("Agent Maya: calm & professional", True), ("Agent Maya: followed policy", True),
                    ("Manager listened to recording", False), ("Manager gave away $1,200", False),
                    ("Manager threatened to fire agent", False)]
            for k, (s, ok) in enumerate(rows):
                y = iy + 115 + k * 58
                cr.arc(ix + 60, y - 9, 18, 0, 2 * math.pi)
                cr.set_source_rgb(*(rgb("#33C46A") if ok else rgb("#E23B3B"))); cr.fill()
                _text(cr, "✓" if ok else "x", ix + 60, y + 1, 26, (1, 1, 1), font="DejaVu Sans")
                _text(cr, s, ix + 95, y, 28, (1, 1, 1), bold=False, center=False)
        cr.restore()
        # Arbeitsplätze hinten
        for dx in (40, 380, 720):
            rrect(cr, dx + 90, 1150, 140, 100, 8)
            fill_stroke(cr, rgb("#2E3440"), 4)
            cr.rectangle(dx + 150, 1250, 20, 30)
            fill_stroke(cr, rgb("#2E3440"), 3)
            cr.move_to(dx + 30, 1280); cr.line_to(dx + 30, 1110); cr.line_to(dx + 300, 1110); cr.line_to(dx + 300, 1280)
            cr.set_source_rgb(*rgb("#A9B8C8")); cr.set_line_width(10); cr.stroke()
        cr.rectangle(20, 1280, 1040, 26)
        fill_stroke(cr, rgb("#E4E9EE"), 5)
        cr.rectangle(40, 1306, 1000, 140)
        fill_stroke(cr, rgb("#C3CCD5"), 5)
        surf.flush()
        return surf
    return make


# ---------------------------------------------------------------- Meetingraum mit Präsentation
def meeting(mode="slides"):
    def make():
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        cr = cairo.Context(surf)
        cr.set_source_rgb(*rgb("#E9E4DC"))
        cr.paint()
        cr.rectangle(0, 1560, W, H - 1560)
        cr.set_source_rgb(*rgb("#7C6A5A"))
        cr.fill()
        cr.rectangle(0, 1545, W, 18)
        cr.set_source_rgb(*rgb("#5F5044"))
        cr.fill()
        # Fenster rechts
        cr.rectangle(930, 600, 190, 600)
        fill_stroke(cr, rgb("#BFE3F2"), 6)
        cr.move_to(930, 900); cr.line_to(1120, 900)
        stroke_black(cr, 4)
        sx, sy, sw, sh = 110, 450, 780, 460
        rrect(cr, sx, sy, sw, sh, 12)
        fill_stroke(cr, rgb("#1B1F27"), 8)
        ix, iy, iw, ih = sx + 20, sy + 20, sw - 40, sh - 40
        cr.save()
        cr.rectangle(ix, iy, iw, ih)
        cr.clip()
        cr.set_source_rgb(1, 1, 1)
        cr.paint()
        cr.rectangle(ix, iy, iw, 70)
        cr.set_source_rgb(*rgb("#1F3B63"))
        cr.fill()
        if mode == "slides":
            _text(cr, "MORGAN LOGISTICS  ·  Q1 PROPOSAL", ix + iw / 2, iy + 46, 30, (1, 1, 1))
            _text(cr, "Projected savings:", ix + 50, iy + 140, 34, rgb("#1F3B63"), center=False)
            _text(cr, "$ ???", ix + 360, iy + 140, 40, rgb("#E23B3B"), center=False)
            _text(cr, "Delivery routes:", ix + 50, iy + 210, 34, rgb("#1F3B63"), center=False)
            _text(cr, "TBD (ask Ava)", ix + 330, iy + 210, 34, rgb("#E23B3B"), center=False)
            for k, h in enumerate((60, 110, 90, 150)):
                cr.rectangle(ix + 70 + k * 120, iy + ih - 30 - h, 80, h)
                fill_stroke(cr, rgb("#7BB6F0"), 3)
            _text(cr, "Slide 2 of 31", ix + iw - 120, iy + ih - 30, 24, rgb("#9AA3B2"), bold=False)
        elif mode == "signed":
            _text(cr, "MORGAN LOGISTICS  ·  CONTRACT", ix + iw / 2, iy + 46, 30, (1, 1, 1))
            cr.arc(ix + iw / 2, iy + 190, 75, 0, 2 * math.pi)
            fill_stroke(cr, rgb("#33C46A"), 5)
            cr.move_to(ix + iw / 2 - 38, iy + 190)
            cr.line_to(ix + iw / 2 - 8, iy + 220)
            cr.line_to(ix + iw / 2 + 42, iy + 160)
            cr.set_source_rgb(1, 1, 1); cr.set_line_width(16); cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
            _text(cr, "SIGNED  ·  3-year contract", ix + iw / 2, iy + 320, 38, rgb("#1F8A47"))
            _text(cr, "Account lead: Ava Brooks", ix + iw / 2, iy + 370, 30, rgb("#1F3B63"), bold=False)
        cr.restore()
        # Tisch
        rrect(cr, 120, 1270, 840, 46, 14)
        fill_stroke(cr, rgb("#5B4636"), 6)
        cr.rectangle(160, 1316, 760, 120)
        fill_stroke(cr, rgb("#4A392C"), 5)
        surf.flush()
        return surf
    return make


# ---------------------------------------------------------------- Hochzeitsterrasse Italien
def wedding():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    cr = cairo.Context(surf)
    g = cairo.LinearGradient(0, 0, 0, 1200)
    g.add_color_stop_rgb(0, *rgb("#7EC8F2"))
    g.add_color_stop_rgb(1, *rgb("#FDE7C2"))
    cr.set_source(g)
    cr.paint()
    cr.arc(860, 560, 80, 0, 2 * math.pi)
    cr.set_source_rgb(*rgb("#FFE58A"))
    cr.fill()
    # Meer + Küste
    cr.rectangle(0, 1080, W, 200)
    cr.set_source_rgb(*rgb("#2F8FD1"))
    cr.fill()
    cr.set_source_rgba(1, 1, 1, 0.5)
    cr.set_line_width(4)
    for y in (1110, 1150, 1200, 1240):
        for x in range(30, W, 160):
            cr.move_to(x + (y % 50), y); cr.line_to(x + 60 + (y % 50), y)
    cr.stroke()
    cr.move_to(0, 1090)
    cr.curve_to(150, 940, 300, 980, 420, 1090)
    cr.close_path()
    fill_stroke(cr, rgb("#E9C58D"), 4)
    for (hx, hw, hh, c) in ((40, 70, 80, "#F6B38A"), (110, 60, 110, "#FBE3A6"), (170, 80, 70, "#F59E8B"), (250, 60, 95, "#FFF3D6")):
        cr.rectangle(hx, 1090 - hh, hw, hh)
        fill_stroke(cr, rgb(c), 3)
    # Terrasse
    cr.rectangle(0, 1280, W, H - 1280)
    cr.set_source_rgb(*rgb("#E8D3B0"))
    cr.fill()
    cr.set_source_rgba(0, 0, 0, 0.08)
    cr.set_line_width(3)
    for x in range(-300, W + 300, 110):
        cr.move_to(x, 1280); cr.line_to(x + (x - 540) * 0.6, H)
    cr.stroke()
    # Balustrade
    cr.rectangle(0, 1240, W, 26)
    fill_stroke(cr, rgb("#F7F1E6"), 4)
    for x in range(20, W, 70):
        cr.rectangle(x, 1266, 26, 60)
        fill_stroke(cr, rgb("#F7F1E6"), 3)
    # Lichterkette
    cr.move_to(0, 470)
    cr.curve_to(300, 560, 700, 560, W, 470)
    stroke_black(cr, 3)
    for k in range(13):
        tt = k / 12
        x = (1 - tt) ** 3 * 0 + 3 * (1 - tt) ** 2 * tt * 300 + 3 * (1 - tt) * tt ** 2 * 700 + tt ** 3 * W
        y = (1 - tt) ** 3 * 470 + 3 * (1 - tt) ** 2 * tt * 560 + 3 * (1 - tt) * tt ** 2 * 560 + tt ** 3 * 470
        cr.arc(x, y + 14, 11, 0, 2 * math.pi)
        fill_stroke(cr, rgb("#FFE58A"), 3)
    # Blumenbogen
    cr.arc(540, 1240, 330, math.pi, 2 * math.pi)
    cr.set_source_rgb(*rgb("#FFFFFF")); cr.set_line_width(26); cr.stroke()
    random.seed(4)
    for k in range(26):
        a = math.pi + math.pi * k / 25
        cr.arc(540 + 330 * math.cos(a), 1240 + 330 * math.sin(a), random.uniform(14, 24), 0, 2 * math.pi)
        cr.set_source_rgb(*rgb(random.choice(("#F7A1B5", "#FFFFFF", "#F9C9D4", "#B7E1A1"))))
        cr.fill()
    # Hochzeitstorte
    for (w_, y_) in ((150, 1440), (110, 1380), (70, 1330)):
        rrect(cr, 900 - w_ / 2, y_, w_, 60, 8)
        fill_stroke(cr, (1, 1, 1), 4)
    cr.rectangle(830, 1500, 140, 60)
    fill_stroke(cr, rgb("#D9B48A"), 4)
    surf.flush()
    return surf
