"""Stickman-Zeichenroutinen im Stil der Referenzvideos (pycairo)."""
import math
import cairo

BLACK = (0.05, 0.05, 0.06)
HEAD = (0.96, 0.96, 0.96)

# Hand-Zielpunkte (Blickrichtung rechts), relativ zu den Füßen.
# Wert: (x, y, bend) – bend: +1 Ellbogen nach außen/unten (je Arm)
POSES = {
    "idle":    {"L": (-50, -392, "out"), "R": (50, -392, "out")},
    "hips":    {"L": (-34, -445, "out"), "R": (34, -445, "out")},
    "point":   {"L": (-50, -392, "out"), "R": (270, -640)},
    "explain": {"L": (-50, -392, "out"), "R": (150, -600)},
    "explain2": {"L": (-50, -392, "out"), "R": (165, -700)},
    "shrug":   {"L": (-165, -690), "R": (165, -690)},
    "phone":   {"L": (-34, -445, "out"), "R": (80, -735)},
    "cross":   {"L": (34, -565, "out"), "R": (-30, -580, "out")},
    "think":   {"L": (-50, -392, "out"), "R": (62, -690)},
    "head":    {"L": (-50, -392, "out"), "R": (20, -885, "out")},
    "panic":   {"L": (-150, -870), "R": (150, -870)},
    "keys":    {"L": (-50, -392, "out"), "R": (165, -570)},
    "stop":    {"L": (-50, -392, "out"), "R": (170, -760)},
    "facepalm": {"L": (-50, -392, "out"), "R": (55, -790)},
    "desk":    {"L": (-60, -470, "out"), "R": (90, -470, "out")},
    "desk_point": {"L": (-60, -470, "out"), "R": (270, -600)},
    "desk_explain": {"L": (-60, -470, "out"), "R": (150, -640)},
    "desk_lean": {"L": (10, -490, "out"), "R": (70, -495, "out")},
    "chest":   {"L": (-50, -392, "out"), "R": (8, -600)},
    "pray":    {"L": (55, -620), "R": (75, -615)},
    "mop":     {"L": (40, -520, "out"), "R": (75, -600)},
    "mop2":    {"L": (60, -500, "out"), "R": (100, -590)},
    "lap":     {"L": (60, -400), "R": (110, -405)},
    "lap_phone": {"L": (60, -400), "R": (80, -735)},
    "lap_explain": {"L": (60, -400), "R": (160, -600)},
    "mug":     {"L": (-50, -392, "out"), "R": (110, -560)},
    "type":    {"L": (60, -440), "R": (125, -445)},
    "write":   {"L": (-50, -392, "out"), "R": (175, -820)},
    "film":    {"L": (60, -640), "R": (185, -690)},
    "shoot":   {"L": (90, -730), "R": (120, -745)},
    "camera_hold": {"L": (-50, -392, "out"), "R": (120, -560)},
    "dance1":  {"L": (-160, -880), "R": (170, -600)},
    "dance2":  {"L": (-170, -600), "R": (160, -880)},
    "dance3":  {"L": (-60, -760), "R": (60, -760)},
    "write2":  {"L": (-50, -392, "out"), "R": (205, -790)},
    "paper":   {"L": (-50, -392, "out"), "R": (150, -600)},
    "type2":   {"L": (75, -446), "R": (110, -440)},
    "tablet":  {"L": (110, -560), "R": (150, -570)},
}


EMO = {
    #          brow_l, brow_r (Neigung: + = innen runter), brow_h, lid, pupil, mouth
    "neutral": dict(tilt=0.0, bh=0, lid=0.0, pupil=9, mouth="line"),
    "calm":    dict(tilt=0.0, bh=-2, lid=0.28, pupil=9, mouth="smile_s"),
    "smug":    dict(tilt=0.25, bh=-4, lid=0.48, pupil=9, mouth="smirk"),
    "annoyed": dict(tilt=0.15, bh=-6, lid=0.40, pupil=9, mouth="flat"),
    "shocked": dict(tilt=-0.35, bh=14, lid=0.0, pupil=6, mouth="o"),
    "worried": dict(tilt=-0.45, bh=6, lid=0.0, pupil=8, mouth="frown"),
    "angry":   dict(tilt=0.55, bh=-6, lid=0.18, pupil=8, mouth="frown"),
    "happy":   dict(tilt=-0.15, bh=6, lid=0.0, pupil=9, mouth="smile"),
    "sad":     dict(tilt=-0.5, bh=2, lid=0.30, pupil=8, mouth="frown"),
    "confused": dict(tilt=0.3, bh=4, lid=0.1, pupil=8, mouth="wavy", asym=True),
    "asleep":  dict(tilt=-0.1, bh=-2, lid=1.0, pupil=8, mouth="o"),
}


def ik(sx, sy, tx, ty, a, b, bend):  # bend: "low" | "out" | "up"; side: -1 L, +1 R
    dx, dy = tx - sx, ty - sy
    d = math.hypot(dx, dy)
    d = max(1e-3, min(d, a + b - 0.5))
    base = math.atan2(dy, dx)
    cosang = (a * a + d * d - b * b) / (2 * a * d)
    ang = math.acos(max(-1, min(1, cosang)))
    c1 = (sx + a * math.cos(base + ang), sy + a * math.sin(base + ang))
    c2 = (sx + a * math.cos(base - ang), sy + a * math.sin(base - ang))
    mode, side = bend
    if mode == "out":
        ex, ey = max((c1, c2), key=lambda c: c[0] * side)
    elif mode == "up":
        ex, ey = min((c1, c2), key=lambda c: c[1])
    else:
        ex, ey = max((c1, c2), key=lambda c: c[1])
    # Hand auf erreichbaren Punkt klemmen
    hx = sx + dx / math.hypot(dx, dy) * d if math.hypot(dx, dy) > 0 else tx
    hy = sy + dy / math.hypot(dx, dy) * d if math.hypot(dx, dy) > 0 else ty
    return ex, ey, hx, hy


def rrect(cr, x, y, w, h, r):
    cr.new_sub_path()
    cr.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    cr.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    cr.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    cr.arc(x + r, y + r, r, math.pi, 1.5 * math.pi)
    cr.close_path()


def stroke_black(cr, w):
    cr.set_source_rgb(*BLACK)
    cr.set_line_width(w)
    cr.set_line_cap(cairo.LINE_CAP_ROUND)
    cr.set_line_join(cairo.LINE_JOIN_ROUND)
    cr.stroke()


class Look:
    """Aussehen einer Figur."""

    def __init__(self, shirt=(0.15, 0.80, 0.91), tie=False, bun=False, cap=False,
                 belt=False, lashes=False, ponytail=False, glasses=False, headset=False, apron=False, police=False, moustache=False, scarf=False, collar=False,
                 hair_color=(0.35, 0.22, 0.14), **extra):
        self.skin = None        # Hautfarbe (Stil v2), None = klassisch weiß
        self.iris = None        # Irisfarbe
        self.hair = None        # "sidepart" | "spiky" | "long" | "bob"
        self.outfit = None      # "suit" | "blouse"
        self.tie_color = (0.12, 0.13, 0.2)
        self.shirt_inner = (0.98, 0.98, 0.98)
        self.shoes = False
        for k, v in extra.items():
            setattr(self, k, v)
        self.shirt = shirt
        self.tie = tie
        self.bun = bun
        self.cap = cap
        self.belt = belt
        self.ponytail = ponytail
        self.glasses = glasses
        self.headset = headset
        self.apron = apron
        self.police = police
        self.lashes = lashes
        self.moustache = moustache
        self.scarf = scarf
        self.collar = collar
        self.hair_color = hair_color


def draw_arm(cr, sx, sy, hand, side, a=150, b=145):
    bend = (hand[2] if len(hand) > 2 else "low", side)
    ex, ey, hx, hy = ik(sx, sy, hand[0], hand[1], a, b, bend)
    cr.move_to(sx, sy)
    cr.line_to(ex, ey)
    cr.line_to(hx, hy)
    stroke_black(cr, 12)
    cr.arc(hx, hy, 15, 0, 2 * math.pi)
    cr.set_source_rgb(*BLACK)
    cr.fill()
    return hx, hy


def draw_keys(cr, hx, hy, t):
    sw = math.sin(t * 5) * 0.12
    cr.save()
    cr.translate(hx, hy + 8)
    cr.rotate(sw)
    cr.arc(0, 34, 30, 0, 2 * math.pi)
    cr.set_source_rgb(0.75, 0.75, 0.78)
    cr.set_line_width(7)
    cr.stroke_preserve()
    cr.set_source_rgb(*BLACK)
    cr.set_line_width(2)
    cr.stroke()
    cols = [(0.85, 0.7, 0.25), (0.7, 0.72, 0.76), (0.6, 0.45, 0.25), (0.82, 0.82, 0.86)]
    for i in range(9):
        ang = math.pi * (0.15 + 0.7 * i / 8)
        kx, ky = 30 * math.cos(ang), 34 + 30 * math.sin(ang)
        cr.save()
        cr.translate(kx, ky)
        cr.rotate(ang - math.pi / 2)
        cr.rectangle(-5, 0, 10, 38)
        cr.arc(0, 0, 9, 0, 2 * math.pi)
        cr.set_source_rgb(*cols[i % 4])
        cr.fill_preserve()
        cr.set_source_rgb(*BLACK)
        cr.set_line_width(2.5)
        cr.stroke()
        cr.restore()
    cr.restore()


def draw_phone(cr, hx, hy):
    cr.save()
    cr.translate(hx, hy)
    cr.rotate(-0.3)
    rrect(cr, -12, -34, 24, 52, 5)
    cr.set_source_rgb(0.98, 0.52, 0.18)
    cr.fill_preserve()
    cr.set_source_rgb(*BLACK)
    cr.set_line_width(3)
    cr.stroke()
    cr.restore()
    cr.arc(hx, hy, 15, 0, 2 * math.pi)
    cr.set_source_rgb(*BLACK)
    cr.fill()


def draw_mop(cr, hx, hy):
    bx, by = hx + 55, -6
    tx, ty = hx - 14, hy - 60
    cr.move_to(tx, ty)
    cr.line_to(bx, by - 30)
    cr.set_source_rgb(0.55, 0.36, 0.18)
    cr.set_line_width(12)
    cr.set_line_cap(cairo.LINE_CAP_ROUND)
    cr.stroke_preserve()
    cr.set_source_rgb(*BLACK)
    cr.set_line_width(2)
    cr.stroke()
    rrect(cr, bx - 45, by - 40, 90, 18, 6)
    cr.set_source_rgb(0.3, 0.45, 0.85)
    cr.fill_preserve()
    stroke_black(cr, 3)
    for k in range(9):
        cr.move_to(bx - 40 + k * 10, by - 22)
        cr.line_to(bx - 44 + k * 11, by + 4)
    cr.set_source_rgb(0.85, 0.85, 0.82)
    cr.set_line_width(7)
    cr.stroke()


def draw_mug(cr, hx, hy):
    rrect(cr, hx - 18, hy - 50, 40, 52, 6)
    cr.set_source_rgb(0.95, 0.95, 0.95)
    cr.fill_preserve()
    stroke_black(cr, 4)
    cr.arc(hx + 26, hy - 26, 12, -1.4, 1.4)
    stroke_black(cr, 5)
    cr.arc(hx, hy, 15, 0, 2 * math.pi)
    cr.set_source_rgb(*BLACK)
    cr.fill()


def draw_figure(cr, look, x, y, scale, facing, st, t, hide_legs=False, shiver=0.0, sit=False):
    """st: dict mit hands(L,R), emotion, mouth_open(0..1), blink(0..1), look(dx,dy), prop."""
    cr.save()
    if shiver:
        x += math.sin(t * 61) * 3 * shiver
        y += math.cos(t * 47) * 1.5 * shiver
    cr.translate(x, y)
    cr.scale(scale * facing, scale)
    bob = math.sin(t * 2.1 + x) * 3
    e = EMO[st.get("emotion", "neutral")]

    hip_y = -420
    sh_y = -672 + bob
    head_cy = -770 + bob

    if look.shoes and not sit and not hide_legs:
        cr.save(); cr.translate(10, 0); cr.scale(120, 18); cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
        cr.set_source_rgba(0, 0, 0, 0.16); cr.fill()

    # Beine
    if sit:
        for side in (-1, 1):
            cr.move_to(side * 12, hip_y + 10)
            cr.line_to(150 + side * 12, hip_y + 4)
            cr.line_to(160 + side * 14, hip_y + 250)
            cr.line_to(195 + side * 14, hip_y + 252)
            stroke_black(cr, 12)
    elif not hide_legs and st.get("walk") is not None:
        ph = st["walk"]
        for side in (-1, 1):
            sw = math.sin(ph + (0 if side < 0 else math.pi)) * 0.42
            kx = 6 + math.sin(sw) * 210
            ky = hip_y + 10 + math.cos(sw) * 210
            lift = max(0.0, math.sin(ph + (0 if side < 0 else math.pi) + 1.2)) * 40
            fx = math.sin(sw) * 420
            fy = -8 - lift
            cr.move_to(side * 6, hip_y + 10)
            cr.line_to(kx + 10 * (1 if sw > 0 else 0), ky - lift * 0.5)
            cr.line_to(fx, fy)
            cr.line_to(fx + 34, fy + 4)
            stroke_black(cr, 12)
    elif not hide_legs:
        for side in (-1, 1):
            cr.move_to(side * 14, hip_y + 10)
            fx = side * 42
            cr.line_to(fx, -8)
            cr.line_to(fx + 34, -4)
            stroke_black(cr, 12)
            if look.shoes:
                cr.save(); cr.translate(fx + 16, -10); cr.scale(30, 15); cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
                cr.set_source_rgb(0.06, 0.06, 0.07); cr.fill()

    # Hinterer Arm (links)
    hands = st["hands"]
    draw_arm(cr, -24, sh_y + 6, hands["L"], -1)

    # Haarknoten hinten
    if look.bun:
        for (bx, by, br) in ((-88, head_cy - 52, 40), (-58, head_cy - 92, 30)):
            cr.arc(bx, by, br, 0, 2 * math.pi)
            cr.set_source_rgb(*HEAD)
            cr.fill_preserve()
            stroke_black(cr, 6)

    if look.ponytail:
        cr.save()
        cr.translate(-96, head_cy - 20 + bob * 0.5)
        cr.rotate(0.35 + math.sin(t * 3) * 0.05)
        cr.scale(32, 70)
        cr.arc(0, 0.6, 1, 0, 2 * math.pi)
        cr.restore()
        cr.set_source_rgb(*HEAD)
        cr.fill_preserve()
        stroke_black(cr, 6)

    hc = head_cy
    if look.hair in ("long", "bob"):
        cr.save()
        if look.hair == "long":
            cr.move_to(-104, hc - 30)
            cr.curve_to(-140, hc + 60, -120, hc + 190, -50, hc + 205)
            cr.curve_to(10, hc + 215, 70, hc + 200, 96, hc + 160)
            cr.curve_to(110, hc + 80, 108, hc + 10, 96, hc - 30)
            cr.close_path()
        else:
            cr.move_to(-106, hc - 20)
            cr.curve_to(-122, hc + 60, -100, hc + 110, -40, hc + 112)
            cr.line_to(90, hc + 100)
            cr.curve_to(112, hc + 60, 112, hc + 10, 100, hc - 20)
            cr.close_path()
        cr.set_source_rgb(*[c * 0.85 for c in look.hair_color])
        cr.fill_preserve()
        stroke_black(cr, 5)
        cr.restore()

    # Torso
    cr.move_to(-34, sh_y - 8)
    cr.curve_to(-38, sh_y + 80, -36, hip_y - 60, -32, hip_y + 18)
    cr.line_to(32, hip_y + 18)
    cr.curve_to(36, hip_y - 60, 38, sh_y + 80, 34, sh_y - 8)
    cr.close_path()
    cr.set_source_rgb(*look.shirt)
    cr.fill_preserve()
    stroke_black(cr, 6)
    if look.outfit == "hoodie":
        cr.move_to(-36, sh_y - 4); cr.curve_to(-30, sh_y + 30, 30, sh_y + 30, 36, sh_y - 4)
        cr.set_source_rgb(*[c * 0.8 for c in look.shirt]); cr.set_line_width(16); cr.stroke()
        for dx in (-10, 10):
            cr.move_to(dx, sh_y + 18); cr.line_to(dx + 2, sh_y + 80)
            cr.set_source_rgb(0.95, 0.95, 0.95); cr.set_line_width(4); cr.stroke()
        cr.move_to(-26, hip_y - 70); cr.line_to(26, hip_y - 70); cr.line_to(22, hip_y - 20); cr.line_to(-22, hip_y - 20)
        cr.close_path(); cr.set_source_rgb(*[c * 0.85 for c in look.shirt]); cr.fill_preserve(); stroke_black(cr, 3)
    if look.outfit in ("suit", "blouse"):
        # helles Hemd / Top im V-Ausschnitt
        cr.move_to(-20, sh_y - 6); cr.line_to(0, sh_y + (150 if look.outfit == "suit" else 70)); cr.line_to(20, sh_y - 6)
        cr.close_path(); cr.set_source_rgb(*look.shirt_inner); cr.fill()
        if look.outfit == "suit":
            cr.move_to(0, sh_y - 4); cr.line_to(-8, sh_y + 16); cr.line_to(-5, sh_y + 120); cr.line_to(0, sh_y + 138)
            cr.line_to(5, sh_y + 120); cr.line_to(8, sh_y + 16); cr.close_path()
            cr.set_source_rgb(*look.tie_color); cr.fill()
        # Revers
        cr.move_to(-30, sh_y - 6); cr.line_to(-4, sh_y + (150 if look.outfit == "suit" else 70))
        cr.move_to(30, sh_y - 6); cr.line_to(4, sh_y + (150 if look.outfit == "suit" else 70))
        stroke_black(cr, 4)
        if look.outfit == "suit":
            for yy in (sh_y + 175, sh_y + 205):
                cr.arc(-2, yy, 4, 0, 2 * math.pi); cr.set_source_rgb(0.1, 0.1, 0.1); cr.fill()
    if look.tie and look.outfit is None:
        cr.move_to(0, sh_y - 6)
        cr.line_to(-10, sh_y + 20)
        cr.line_to(-6, sh_y + 140)
        cr.line_to(0, sh_y + 160)
        cr.line_to(6, sh_y + 140)
        cr.line_to(10, sh_y + 20)
        cr.close_path()
        cr.set_source_rgb(0.12, 0.13, 0.2)
        cr.fill()
    if look.collar:
        cr.move_to(-30, sh_y - 4)
        cr.line_to(-6, sh_y + 34)
        cr.move_to(30, sh_y - 4)
        cr.line_to(6, sh_y + 34)
        stroke_black(cr, 4)
    if look.apron:
        cr.move_to(-30, sh_y + 90)
        cr.line_to(30, sh_y + 90)
        cr.line_to(34, hip_y + 60)
        cr.line_to(-34, hip_y + 60)
        cr.close_path()
        cr.set_source_rgb(1, 1, 1)
        cr.fill_preserve()
        stroke_black(cr, 4)
        cr.rectangle(-14, sh_y + 130, 28, 22)
        stroke_black(cr, 3)
    if look.police:
        cr.move_to(-20, sh_y + 40)
        cr.line_to(-8, sh_y + 30)
        cr.line_to(4, sh_y + 40)
        cr.line_to(-2, sh_y + 60)
        cr.line_to(-14, sh_y + 60)
        cr.close_path()
        cr.set_source_rgb(0.95, 0.78, 0.25)
        cr.fill_preserve()
        stroke_black(cr, 3)
    if look.belt:
        cr.rectangle(-34, hip_y - 14, 68, 20)
        cr.set_source_rgb(0.45, 0.28, 0.12)
        cr.fill_preserve()
        stroke_black(cr, 4)
        cr.rectangle(-8, hip_y - 16, 16, 24)
        cr.set_source_rgb(0.85, 0.7, 0.25)
        cr.fill_preserve()
        stroke_black(cr, 3)

    # Kopf
    hx0 = 0
    g = cairo.RadialGradient(hx0 + 25, head_cy - 30, 10, hx0, head_cy, 98)
    if look.skin:
        sk = look.skin
        g.add_color_stop_rgb(0, min(1, sk[0] * 1.05), min(1, sk[1] * 1.05), min(1, sk[2] * 1.05))
        g.add_color_stop_rgb(1, sk[0] * 0.9, sk[1] * 0.88, sk[2] * 0.85)
    else:
        g.add_color_stop_rgb(0, 1, 1, 1)
        g.add_color_stop_rgb(1, 0.88, 0.88, 0.89)
    cr.arc(hx0, head_cy, 96, 0, 2 * math.pi)
    cr.set_source(g)
    cr.fill_preserve()
    stroke_black(cr, 7)

    if look.scarf:
        cr.move_to(-40, sh_y - 14)
        cr.curve_to(-20, sh_y + 10, 20, sh_y + 10, 42, sh_y - 14)
        cr.set_source_rgb(0.85, 0.15, 0.18)
        cr.set_line_width(26)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.stroke()
        cr.move_to(-20, sh_y + 2)
        cr.line_to(-34, sh_y + 110)
        cr.set_line_width(22)
        cr.stroke()

    if look.cap:
        cr.arc(hx0, head_cy, 97, math.pi * 1.02, math.pi * 1.98)
        cr.close_path()
        cr.set_source_rgb(0.1, 0.1, 0.12)
        cr.fill()
        cr.move_to(-90, head_cy - 30)
        cr.curve_to(-140, head_cy - 30, -150, head_cy - 5, -120, head_cy)
        cr.line_to(-85, head_cy - 8)
        cr.close_path()
        cr.fill()

    if look.police:
        cr.move_to(-96, head_cy - 40)
        cr.curve_to(-90, head_cy - 120, 90, head_cy - 120, 96, head_cy - 40)
        cr.close_path()
        cr.set_source_rgb(0.12, 0.17, 0.32)
        cr.fill_preserve()
        stroke_black(cr, 5)
        cr.move_to(-20, head_cy - 45)
        cr.curve_to(40, head_cy - 30, 110, head_cy - 34, 128, head_cy - 22)
        cr.line_to(96, head_cy - 40)
        cr.close_path()
        cr.set_source_rgb(0.05, 0.05, 0.08)
        cr.fill()
        cr.arc(10, head_cy - 78, 12, 0, 2 * math.pi)
        cr.set_source_rgb(0.95, 0.78, 0.25)
        cr.fill()

    if look.hair:
        hcol = look.hair_color
        if look.hair == "sidepart":
            cr.move_to(-98, hc + 14)
            cr.curve_to(-114, hc - 80, -40, hc - 126, 30, hc - 113)
            cr.curve_to(84, hc - 104, 106, hc - 70, 99, hc - 34)
            cr.curve_to(74, hc - 62, 26, hc - 70, -6, hc - 60)
            cr.curve_to(-48, hc - 52, -80, hc - 22, -84, hc + 18)
            cr.close_path()
        elif look.hair == "spiky":
            pts = []
            for k in range(11):
                a = math.pi * (1.02 + 0.96 * k / 10)
                r = 96 + (10, 34, 14, 46, 12, 42, 18, 48, 14, 30, 8)[k]
                a += 0.06 * (k % 2)
                pts.append((r * math.cos(a), hc + r * math.sin(a)))
            cr.move_to(-96, hc + 6)
            for (px_, py_) in pts:
                cr.line_to(px_, py_)
            cr.line_to(97, hc - 30)
            cr.curve_to(60, hc - 60, 0, hc - 66, -60, hc - 40)
            cr.close_path()
        elif look.hair == "long":
            cr.move_to(-102, hc + 30)
            cr.curve_to(-112, hc - 90, -20, hc - 130, 50, hc - 108)
            cr.curve_to(104, hc - 90, 116, hc - 20, 104, hc + 60)
            cr.curve_to(94, hc + 0, 84, hc - 46, 46, hc - 64)
            cr.curve_to(6, hc - 74, -44, hc - 58, -72, hc - 16)
            cr.close_path()
        elif look.hair == "curly":
            random_pts = [(-92, -10), (-96, -50), (-80, -86), (-48, -110), (-8, -120), (32, -116), (66, -100),
                          (90, -72), (98, -44)]
            for (cx_, cy_) in random_pts:
                cr.new_sub_path()
                cr.arc(cx_, hc + cy_, 30, 0, 2 * math.pi)
            cr.new_sub_path()
            cr.arc(-20, hc - 80, 60, 0, 2 * math.pi)
        elif look.hair == "buzz":
            cr.move_to(-97, hc - 4)
            cr.curve_to(-104, hc - 90, -20, hc - 112, 40, hc - 104)
            cr.curve_to(84, hc - 96, 100, hc - 66, 97, hc - 44)
            cr.curve_to(70, hc - 68, 20, hc - 80, -20, hc - 74)
            cr.curve_to(-60, hc - 66, -88, hc - 40, -90, hc - 4)
            cr.close_path()
        elif look.hair == "bald":
            cr.move_to(-97, hc - 10)
            cr.curve_to(-104, hc - 34, -100, hc - 48, -92, hc - 58)
            cr.line_to(-76, hc - 50)
            cr.curve_to(-82, hc - 30, -84, hc - 16, -80, hc + 10)
            cr.close_path()
        elif look.hair == "updo":
            cr.new_sub_path()
            cr.arc(-30, hc - 120, 46, 0, 2 * math.pi)
            cr.move_to(-98, hc + 6)
            cr.curve_to(-108, hc - 86, -20, hc - 120, 46, hc - 104)
            cr.curve_to(92, hc - 92, 104, hc - 60, 98, hc - 30)
            cr.curve_to(70, hc - 58, 20, hc - 70, -20, hc - 64)
            cr.curve_to(-60, hc - 56, -86, hc - 30, -88, hc + 6)
            cr.close_path()
        elif look.hair == "bob":
            cr.move_to(-106, hc + 40)
            cr.curve_to(-114, hc - 92, 0, hc - 132, 70, hc - 104)
            cr.curve_to(110, hc - 82, 114, hc - 20, 106, hc + 40)
            cr.line_to(96, hc + 40)
            cr.curve_to(96, hc - 8, 92, hc - 40, 82, hc - 54)
            cr.line_to(-36, hc - 58)
            cr.curve_to(-70, hc - 50, -90, hc - 10, -92, hc + 40)
            cr.close_path()
        if look.hair == "curly":
            cr.set_source_rgb(*BLACK); cr.set_line_width(10); cr.stroke_preserve()
            cr.set_source_rgb(*hcol); cr.fill()
        else:
            cr.set_source_rgb(*hcol)
            cr.fill_preserve()
            stroke_black(cr, 5)
        # Glanzlinien
        cr.move_to(-40, hc - 98); cr.curve_to(-10, hc - 108, 20, hc - 106, 40, hc - 96)
        cr.set_source_rgba(1, 1, 1, 0.25); cr.set_line_width(6); cr.stroke()

    if getattr(look, "beard", None):
        cr.move_to(-70, hc + 10)
        cr.curve_to(-60, hc + 110, 90, hc + 120, 96, hc + 6)
        cr.curve_to(80, hc + 40, 60, hc + 36, 40, hc + 36)
        cr.curve_to(20, hc + 30, -10, hc + 34, -30, hc + 30)
        cr.curve_to(-50, hc + 30, -62, hc + 20, -70, hc + 10)
        cr.close_path()
        cr.set_source_rgb(*look.beard)
        cr.fill_preserve()
        stroke_black(cr, 4)

    # Gesicht
    lookv = st.get("look", (1.0, 0.0))
    ecx = hx0 + 22
    ey = head_cy - 18
    blink = st.get("blink", 0.0)
    lid = max(e["lid"], blink)
    for i, dx in enumerate((-25, 25)):
        cx = ecx + dx
        rx, ry = 23, 31
        cr.save()
        cr.translate(cx, ey)
        cr.scale(rx, ry)
        cr.arc(0, 0, 1, 0, 2 * math.pi)
        cr.restore()
        cr.set_source_rgb(1, 1, 1)
        cr.fill_preserve()
        cr.save()
        cr.clip_preserve()
        # Pupille
        px = cx + lookv[0] * (rx - 11)
        py = ey + lookv[1] * (ry - 12) + 4
        cr.new_path()
        if look.iris:
            cr.arc(px, py, 14, 0, 2 * math.pi)
            cr.set_source_rgb(*look.iris)
            cr.fill_preserve()
            cr.set_source_rgb(*[c * 0.6 for c in look.iris]); cr.set_line_width(2.5); cr.stroke()
            cr.arc(px, py, max(5, e["pupil"] - 2), 0, 2 * math.pi)
            cr.set_source_rgb(*BLACK)
            cr.fill()
            cr.arc(px + 4, py - 5, 3.5, 0, 2 * math.pi)
            cr.set_source_rgb(1, 1, 1)
            cr.fill()
        else:
            cr.arc(px, py, e["pupil"], 0, 2 * math.pi)
            cr.set_source_rgb(*BLACK)
            cr.fill()
        # Lid
        if lid > 0.02:
            ly = ey - ry + 2 * ry * lid
            cr.rectangle(cx - rx - 2, ey - ry - 2, 2 * rx + 4, ly - (ey - ry) + 2)
            cr.set_source_rgb(*(look.skin if look.skin else (0.92, 0.92, 0.93)))
            cr.fill()
            cr.move_to(cx - rx, ly)
            cr.line_to(cx + rx, ly)
            stroke_black(cr, 5)
        cr.restore()
        cr.save()
        cr.translate(cx, ey)
        cr.scale(rx, ry)
        cr.arc(0, 0, 1, 0, 2 * math.pi)
        cr.restore()
        stroke_black(cr, 5)
        if look.lashes:
            ox = cx + (rx if dx > 0 else -rx) * 0.85
            sgn = 1 if dx > 0 else -1
            cr.move_to(ox, ey - ry * 0.55)
            cr.line_to(ox + sgn * 12, ey - ry * 0.85)
            stroke_black(cr, 4)
        # Augenbraue
        tilt = e["tilt"] * (1 if dx < 0 else -1)
        if e.get("asym") and dx > 0:
            tilt = -tilt
        by = ey - ry - 14 - e["bh"]
        cr.move_to(cx - 16, by - tilt * 14)
        cr.line_to(cx + 16, by + tilt * 14)
        if look.skin:
            cr.set_source_rgb(*[c * 0.55 for c in look.hair_color]); cr.set_line_width(8)
            cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
        else:
            stroke_black(cr, 6)

    if look.glasses:
        for dx in (-25, 25):
            rrect(cr, ecx + dx - 30, ey - 36, 60, 70, 14)
            stroke_black(cr, 5)
        cr.move_to(ecx - 5, ey - 6)
        cr.line_to(ecx + 5, ey - 6)
        stroke_black(cr, 5)
        cr.move_to(ecx - 55, ey - 10)
        cr.line_to(ecx - 90, ey - 18)
        stroke_black(cr, 5)

    if look.headset:
        cr.arc(hx0, head_cy, 104, math.pi * 1.08, math.pi * 1.92)
        stroke_black(cr, 9)
        rrect(cr, -112, head_cy - 30, 30, 56, 10)
        cr.set_source_rgb(0.2, 0.22, 0.28)
        cr.fill_preserve()
        stroke_black(cr, 4)
        cr.move_to(-96, head_cy + 20)
        cr.curve_to(-80, head_cy + 75, -10, head_cy + 80, ecx - 26, head_cy + 58)
        stroke_black(cr, 5)
        cr.arc(ecx - 22, head_cy + 57, 8, 0, 2 * math.pi)
        cr.set_source_rgb(0.2, 0.22, 0.28)
        cr.fill()

    if look.moustache:
        mx, my = ecx + 2, head_cy + 30
        cr.move_to(mx - 34, my + 6)
        cr.curve_to(mx - 20, my - 12, mx - 4, my - 6, mx, my)
        cr.curve_to(mx + 4, my - 6, mx + 20, my - 12, mx + 34, my + 6)
        cr.curve_to(mx + 16, my + 2, mx + 6, my + 6, mx, my + 4)
        cr.curve_to(mx - 6, my + 6, mx - 16, my + 2, mx - 34, my + 6)
        cr.set_source_rgb(0.55, 0.55, 0.57)
        cr.fill_preserve()
        stroke_black(cr, 3)

    # Mund
    mo = st.get("mouth_open", 0.0)
    mx, my = ecx + 4, head_cy + 52
    if mo > 0.08 or e["mouth"] == "o":
        h = 6 + 24 * mo if mo > 0.08 else 10
        w = 22 + 6 * mo
        cr.save()
        cr.translate(mx, my)
        cr.scale(w, h)
        cr.arc(0, 0, 1, 0, 2 * math.pi)
        cr.restore()
        cr.set_source_rgb(0.22, 0.05, 0.06)
        cr.fill_preserve()
        cr.save()
        cr.clip()
        if h > 12:
            cr.arc(mx + 4, my + h * 0.9, w * 0.7, 0, 2 * math.pi)
            cr.set_source_rgb(0.9, 0.38, 0.45)
            cr.fill()
            cr.rectangle(mx - w, my - h, 2 * w, h * 0.35)
            cr.set_source_rgb(1, 1, 1)
            cr.fill()
        cr.restore()
        cr.save()
        cr.translate(mx, my)
        cr.scale(w, h)
        cr.arc(0, 0, 1, 0, 2 * math.pi)
        cr.restore()
        stroke_black(cr, 5)
    else:
        m = e["mouth"]
        if m == "line":
            cr.move_to(mx - 14, my)
            cr.line_to(mx + 14, my)
        elif m == "flat":
            cr.move_to(mx - 18, my + 2)
            cr.line_to(mx + 16, my)
        elif m == "smile_s":
            cr.move_to(mx - 16, my - 2)
            cr.curve_to(mx - 6, my + 8, mx + 6, my + 8, mx + 16, my - 4)
        elif m == "smile":
            cr.move_to(mx - 24, my - 6)
            cr.curve_to(mx - 10, my + 18, mx + 10, my + 18, mx + 24, my - 6)
        elif m == "smirk":
            cr.move_to(mx - 18, my + 4)
            cr.curve_to(mx - 4, my + 6, mx + 10, my + 2, mx + 20, my - 8)
        elif m == "frown":
            cr.move_to(mx - 20, my + 8)
            cr.curve_to(mx - 8, my - 6, mx + 8, my - 6, mx + 20, my + 8)
        elif m == "wavy":
            cr.move_to(mx - 20, my)
            cr.curve_to(mx - 10, my - 8, mx - 4, my + 8, mx + 4, my)
            cr.curve_to(mx + 10, my - 8, mx + 16, my + 6, mx + 20, my)
        stroke_black(cr, 6)

    if st.get("prop") == "laptop":
        lx, ly = 95, hip_y - 6
        cr.move_to(lx - 70, ly)
        cr.line_to(lx + 70, ly)
        cr.line_to(lx + 60, ly + 12)
        cr.line_to(lx - 60, ly + 12)
        cr.close_path()
        cr.set_source_rgb(0.75, 0.78, 0.82)
        cr.fill_preserve()
        stroke_black(cr, 4)
        cr.move_to(lx - 64, ly)
        cr.line_to(lx - 10, ly - 95)
        cr.line_to(lx + 8, ly - 92)
        cr.line_to(lx - 44, ly)
        cr.close_path()
        cr.set_source_rgb(0.25, 0.28, 0.33)
        cr.fill_preserve()
        stroke_black(cr, 4)

    # Vorderer Arm (rechts)
    hr = draw_arm(cr, 24, sh_y + 6, hands["R"], 1)
    prop = st.get("prop")
    if prop == "keys":
        draw_keys(cr, hr[0], hr[1], t)
    elif prop == "phone":
        draw_phone(cr, hr[0], hr[1])
    elif prop == "mop":
        draw_mop(cr, hr[0], hr[1])
        cr.arc(hr[0], hr[1], 15, 0, 2 * math.pi)
        cr.set_source_rgb(*BLACK)
        cr.fill()
    elif prop == "camera":
        cr.save()
        cr.translate(hr[0] + 6, hr[1] - 30)
        rrect(cr, -48, -34, 96, 64, 10)
        cr.set_source_rgb(0.12, 0.12, 0.14)
        cr.fill_preserve()
        stroke_black(cr, 3)
        cr.arc(8, -2, 24, 0, 2 * math.pi)
        cr.set_source_rgb(0.25, 0.27, 0.32)
        cr.fill_preserve()
        stroke_black(cr, 3)
        cr.arc(8, -2, 13, 0, 2 * math.pi)
        cr.set_source_rgb(0.35, 0.55, 0.85)
        cr.fill()
        cr.rectangle(-40, -44, 24, 12)
        cr.set_source_rgb(0.12, 0.12, 0.14)
        cr.fill()
        cr.restore()
        cr.arc(hr[0], hr[1], 15, 0, 2 * math.pi)
        cr.set_source_rgb(*BLACK)
        cr.fill()
    elif prop == "tablet":
        cr.save()
        cr.translate(hr[0] - 20, hr[1] - 10)
        cr.rotate(-0.25)
        rrect(cr, -55, -75, 110, 80, 8)
        cr.set_source_rgb(0.2, 0.22, 0.26)
        cr.fill_preserve()
        stroke_black(cr, 4)
        cr.rectangle(-45, -66, 90, 62)
        cr.set_source_rgb(0.55, 0.85, 0.95)
        cr.fill()
        cr.restore()
        cr.arc(hr[0], hr[1], 15, 0, 2 * math.pi)
        cr.set_source_rgb(*BLACK)
        cr.fill()
    elif prop and prop.startswith("paper"):
        label = prop.split(":", 1)[1] if ":" in prop else "100%"
        cr.save()
        cr.translate(hr[0] + 10, hr[1] - 20)
        cr.rotate(0.12)
        cr.rectangle(-45, -120, 90, 120)
        cr.set_source_rgb(1, 1, 1)
        cr.fill_preserve()
        stroke_black(cr, 4)
        for k in range(4):
            cr.move_to(-32, -95 + k * 18)
            cr.line_to(32, -95 + k * 18)
        cr.set_source_rgb(0.6, 0.6, 0.65)
        cr.set_line_width(3)
        cr.stroke()
        cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(30)
        cr.set_source_rgb(0.85, 0.1, 0.1)
        ext = cr.text_extents(label)
        if cr.get_matrix().xx < 0:
            cr.scale(-1, 1)
        cr.move_to(-ext.width / 2 - ext.x_bearing, -12)
        cr.show_text(label)
        cr.restore()
        cr.arc(hr[0], hr[1], 15, 0, 2 * math.pi)
        cr.set_source_rgb(*BLACK)
        cr.fill()
    elif prop == "chalk":
        cr.move_to(hr[0] + 4, hr[1] - 6)
        cr.line_to(hr[0] + 22, hr[1] - 26)
        cr.set_source_rgb(1, 1, 1)
        cr.set_line_width(9)
        cr.stroke()
        cr.arc(hr[0], hr[1], 15, 0, 2 * math.pi)
        cr.set_source_rgb(*BLACK)
        cr.fill()
    elif prop == "mug":
        draw_mug(cr, hr[0], hr[1])
    cr.restore()
