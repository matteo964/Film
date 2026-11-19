"""Serie: "You call in sick for GTA 6... and your boss joins your online lobby"."""
import math
import random

import cairo
import backgrounds as bgm
import backgrounds_v2 as B
import mailui as MU
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect, stroke_black, draw_figure, POSES

GAP = 0.15
HOOK_BASE = ["POV: You call in sick for GTA 6...", "and your boss is in line right behind you"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
JAKE = Look(shirt=(0.20, 0.20, 0.25), skin=SKIN, iris=(0.30, 0.55, 0.30), hair="curly", hair_color=(0.45, 0.28, 0.15),
            outfit="hoodie", shoes=True, headset=True)
JAKE_WORK = Look(shirt=(0.30, 0.45, 0.65), skin=SKIN, iris=(0.30, 0.55, 0.30), hair="curly", hair_color=(0.45, 0.28, 0.15),
                 outfit="blouse", shoes=True)
GARY = Look(shirt=(0.20, 0.25, 0.40), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="sidepart", hair_color=(0.55, 0.55, 0.58),
            moustache=True, outfit="suit", tie_color=(0.85, 0.20, 0.25), shoes=True, glasses=True)
GARY_HOME = Look(shirt=(0.85, 0.30, 0.55), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="sidepart", hair_color=(0.55, 0.55, 0.58),
                 moustache=True, outfit="hoodie", shoes=True, glasses=True, headset=True)
MIA = Look(shirt=(0.95, 0.70, 0.30), skin=(0.70, 0.52, 0.40), iris=(0.22, 0.14, 0.08), hair="bob", hair_color=(0.08, 0.06, 0.06),
           outfit="blouse", shoes=True, lashes=True)
PAMELA = Look(shirt=(0.40, 0.15, 0.40), skin=(0.48, 0.33, 0.24), iris=(0.22, 0.14, 0.08), hair="updo", hair_color=(0.08, 0.06, 0.06),
              outfit="hoodie", shoes=True, lashes=True, headset=True)

CLERK = Look(shirt=(0.15, 0.15, 0.18), skin=(0.66, 0.48, 0.35), iris=(0.2, 0.12, 0.08), hair="spiky", hair_color=(0.08, 0.06, 0.06),
             outfit="hoodie", shoes=True, cap=True)
GARY_CASUAL = Look(shirt=(0.85, 0.30, 0.55), skin=SKIN, iris=(0.35, 0.25, 0.15), hair="sidepart", hair_color=(0.55, 0.55, 0.58),
                   moustache=True, outfit="hoodie", shoes=True, glasses=True)
JAKE_CASUAL = Look(shirt=(0.20, 0.20, 0.25), skin=SKIN, iris=(0.30, 0.55, 0.30), hair="curly", hair_color=(0.45, 0.28, 0.15),
                   outfit="hoodie", shoes=True)
PAM_CASUAL = Look(shirt=(0.40, 0.15, 0.40), skin=(0.48, 0.33, 0.24), iris=(0.22, 0.14, 0.08), hair="updo", hair_color=(0.08, 0.06, 0.06),
                  outfit="hoodie", shoes=True, lashes=True)

CHARS = {
    "C": dict(voice="en-US-AndrewNeural", el_voice="IKne3meq5aSn9XLyUdCD", look=CLERK),           # Charlie
    "J": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=JAKE),            # Liam
    "G": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal", look=GARY),  # Eric
    "M": dict(voice="en-US-AvaNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=MIA),                # Jessica
    "P": dict(voice="en-US-MichelleNeural", el_voice="hpp4J3VqNfWAUOO0d1Us", look=PAMELA),        # Bella
}


def lt():
    return bgm.CLOCK["lt"]


# ------------------------------------------------------------------ Neon-Spielwelt (generisch)
def neon_city(cr, x, y, w, h):
    cr.save(); cr.rectangle(x, y, w, h); cr.clip()
    g = cairo.LinearGradient(0, y, 0, y + h)
    g.add_color_stop_rgb(0, *rgb("#2A0E4A")); g.add_color_stop_rgb(0.55, *rgb("#E0457B")); g.add_color_stop_rgb(1, *rgb("#FFB36B"))
    cr.set_source(g); cr.paint()
    cr.arc(x + w * 0.5, y + h * 0.62, h * 0.22, math.pi, 2 * math.pi); cr.set_source_rgb(*rgb("#FFE38A")); cr.fill()
    random.seed(7)
    xx = x
    while xx < x + w:
        bw, bh = random.randint(int(w * 0.05), int(w * 0.1)), random.uniform(h * 0.2, h * 0.55)
        cr.rectangle(xx, y + h * 0.75 - bh, bw, bh + h * 0.3); cr.set_source_rgb(*rgb("#1A0A2E")); cr.fill()
        for k in range(4):
            if random.random() < 0.6:
                cr.rectangle(xx + bw * 0.2, y + h * 0.75 - bh + 10 + k * bh / 5, bw * 0.6, 3)
                cr.set_source_rgb(*rgb(random.choice(("#29E7FF", "#FF4FD8")))); cr.fill()
        xx += bw + 4
    for px in (x + w * 0.12, x + w * 0.85):
        cr.move_to(px, y + h); cr.curve_to(px + 6, y + h * 0.75, px - 4, y + h * 0.6, px + 8, y + h * 0.48)
        cr.set_source_rgb(*rgb("#140820")); cr.set_line_width(max(4, w * 0.01)); cr.stroke()
        for a in range(6):
            ang = math.pi * (1.0 + a / 5)
            cr.move_to(px + 8, y + h * 0.48)
            cr.curve_to(px + 8 + math.cos(ang) * w * 0.04, y + h * 0.46, px + 8 + math.cos(ang) * w * 0.08,
                        y + h * 0.48 + math.sin(ang) * -h * 0.02, px + 8 + math.cos(ang) * w * 0.09, y + h * 0.52)
            cr.set_line_width(max(3, w * 0.008)); cr.stroke()
    cr.rectangle(x, y + h * 0.88, w, h * 0.12); cr.set_source_rgb(*rgb("#140820")); cr.fill()
    cr.restore()


PLAYERS = {
    "jake": ("xX_Jake_Xx", "J", "#29E7FF"),
    "gary": ("BigBoss_Gary", "G", "#FFB36B"),
    "pam": ("CEO_Pamela", "P", "#FF4FD8"),
}


def lobby(players, joined=None, kicked=None, mission="ONLINE HEIST · Diamond Vault"):
    """players: Liste von keys; joined: key, dessen Beitritt per Banner animiert wird."""
    def fn(cr, t):
        l = lt()
        neon_city(cr, 0, 0, 1080, 1920)
        cr.set_source_rgba(0.05, 0.02, 0.10, 0.45); cr.rectangle(0, 0, 1080, 1920); cr.fill()
        x, y, w = 60, 470, 960
        rrect(cr, x, y, w, 90, 14); cr.set_source_rgba(0, 0, 0, 0.75); cr.fill()
        _text(cr, mission, x + 30, y + 58, 34, rgb("#FFE38A"), center=False)
        for k, key in enumerate(players):
            name, cid, col = PLAYERS[key]
            yy = y + 120 + k * 130
            if key == kicked and l > 1.5:
                continue
            rrect(cr, x, yy, w, 112, 14); cr.set_source_rgba(0, 0, 0, 0.65); cr.fill()
            cr.arc(x + 62, yy + 56, 38, 0, 2 * math.pi); cr.set_source_rgb(*rgb(col)); cr.fill()
            _text(cr, name[0], x + 62, yy + 70, 38, rgb("#1A0A2E"))
            _text(cr, name, x + 125, yy + 70, 38, (1, 1, 1), center=False)
            speaking = bgm.CLOCK.get("speaker") == cid
            mx = x + w - 70
            cr.arc(mx, yy + 56, 26, 0, 2 * math.pi)
            cr.set_source_rgb(*(rgb("#33E07A") if speaking else rgb("#555B66"))); cr.fill()
            if speaking:
                for r in (40, 54):
                    cr.arc(mx, yy + 56, r, -0.6, 0.6); cr.set_source_rgba(0.2, 0.9, 0.5, 0.8); cr.set_line_width(4); cr.stroke()
        if joined and l < 3.5:
            name = PLAYERS[joined][0]
            a = min(1.0, l * 3)
            rrect(cr, 120, 1200, 840, 100, 20); cr.set_source_rgba(0.1, 0.7, 0.4, 0.9 * a); cr.fill()
            _text(cr, f"{name} joined your session", 540, 1264, 36, (1, 1, 1))
        if kicked and l > 1.5:
            rrect(cr, 120, 1200, 840, 100, 20); cr.set_source_rgba(0.85, 0.15, 0.2, 0.92); cr.fill()
            _text(cr, f"{PLAYERS[kicked][0]} was kicked from the lobby", 540, 1264, 32, (1, 1, 1))
    return fn


# ------------------------------------------------------------------ Wohnzimmer mit TV
def tv(cr, x=500, y=560, w=520, h=320, on=True):
    rrect(cr, x, y, w, h, 12); fill_stroke(cr, rgb("#0D0F14"), 6)
    if on:
        neon_city(cr, x + 14, y + 14, w - 28, h - 28)
    cr.rectangle(x + w / 2 - 50, y + h, 100, 40); cr.set_source_rgb(*rgb("#2B2F38")); cr.fill()


def jake_room():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#3B3F63"), rgb("#6E5A4A"), tiles="wood", ceiling=(0.20, 0.21, 0.30))
    tv(cr)
    # Snacks / Energy drinks auf dem Boden
    for k in range(4):
        rrect(cr, 760 + k * 50, 1500, 34, 70, 6); fill_stroke(cr, rgb(("#33E07A", "#29E7FF", "#33E07A", "#FF4FD8")[k]), 3)
    gl = cairo.RadialGradient(760, 720, 20, 760, 720, 700)
    gl.add_color_stop_rgba(0, 1, 0.3, 0.7, 0.25); gl.add_color_stop_rgba(1, 1, 0.3, 0.7, 0)
    cr.set_source(gl); cr.paint()
    s.flush()
    return s


def gary_room():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#1E1A2E"), rgb("#3A2F45"), tiles="wood", ceiling=(0.12, 0.10, 0.18))
    for y_, c in ((420, "#FF4FD8"), (1235, "#29E7FF")):
        cr.rectangle(0, y_, 1080, 8); cr.set_source_rgb(*rgb(c)); cr.fill()
    tv(cr, 80, 560, 560, 340)
    # Schild "Chicago"-Flugticket ungenutzt
    cr.save(); cr.translate(860, 720); cr.rotate(0.08)
    cr.rectangle(-110, -60, 220, 120); cr.set_source_rgb(1, 1, 1); cr.fill()
    _text(cr, "FLIGHT TO", 0, -10, 24, rgb("#1B1F27")); _text(cr, "CHICAGO", 0, 26, 30, rgb("#B3261E"))
    cr.restore()
    gl = cairo.RadialGradient(360, 730, 20, 360, 730, 700)
    gl.add_color_stop_rgba(0, 0.2, 0.9, 1, 0.22); gl.add_color_stop_rgba(1, 0.2, 0.9, 1, 0)
    cr.set_source(gl); cr.paint()
    s.flush()
    return s


def couch_back(cr, x=120, col="#3C4A6E"):
    rrect(cr, x, 1150, 640, 240, 40); fill_stroke(cr, rgb(col), 5)


def couch_front(cr, x=120, col="#34405F"):
    rrect(cr, x, 1330, 640, 150, 30); fill_stroke(cr, rgb(col), 5)
    for dx in (-30, 610):
        rrect(cr, x + dx, 1250, 80, 230, 30); fill_stroke(cr, rgb(col), 5)


def phone_call(name, sub="calling..."):
    def fn(cr, t):
        cr.set_source_rgb(*rgb("#11151C")); cr.paint()
        x, y, w, h = 240, 460, 600, 1080
        rrect(cr, x, y, w, h, 60); cr.set_source_rgb(*rgb("#1B1F27")); cr.fill()
        rrect(cr, x + 20, y + 20, w - 40, h - 40, 44)
        g = cairo.LinearGradient(0, y, 0, y + h); g.add_color_stop_rgb(0, *rgb("#2C3E66")); g.add_color_stop_rgb(1, *rgb("#14213D"))
        cr.set_source(g); cr.fill()
        cr.arc(540, y + 300, 110, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#8EA0B2")); cr.fill()
        _text(cr, name[0], 540, y + 340, 110, (1, 1, 1))
        _text(cr, name, 540, y + 500, 52, (1, 1, 1))
        _text(cr, sub, 540, y + 560, 32, rgb("#C9D3E6"), bold=False)
        for dx, c in ((-140, "#E23B3B"), (140, "#33C46A")):
            cr.arc(540 + dx, y + 900, 56, 0, 2 * math.pi); cr.set_source_rgb(*rgb(c)); cr.fill()
    return fn


EMAIL_BODY = ("Team,\nTomorrow is GTA 6 release day. The whole company gets a PAID day off.\n"
              "Enjoy the game. See you Friday!\n- Pamela (CEO)\n\nP.S. Managers, please forward this to your teams.")


def ceo_email(cr, t):
    MU.compose(cr, "Managers (12)", "FWD to your teams: Paid day off tomorrow!", EMAIL_BODY, typed=1.0, title="Outlook – Gary Wells")
    rrect(cr, 260, 1360, 560, 80, 16); cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
    _text(cr, "Forwarded by Gary: NO", 540, 1412, 36, (1, 1, 1))


# ------------------------------------------------------------------ Game-Store
def game_box(cr, x, y, s=1.0, art=True):
    cr.save(); cr.translate(x, y); cr.scale(s, s)
    rrect(cr, -50, -70, 100, 140, 6); fill_stroke(cr, rgb("#1A0A2E"), 3)
    if art:
        neon_city(cr, -44, -64, 88, 128)
    cr.restore()


def store(mode="full"):
    def make():
        s_ = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
        cr = cairo.Context(s_)
        B.room(cr, rgb("#2B2140"), rgb("#4A4458"), tiles="tile", ceiling=(0.16, 0.14, 0.22))
        # Banner
        rrect(cr, 150, 440, 780, 110, 14)
        g = cairo.LinearGradient(150, 0, 930, 0); g.add_color_stop_rgb(0, *rgb("#FF4FD8")); g.add_color_stop_rgb(1, *rgb("#29E7FF"))
        cr.set_source(g); cr.fill()
        _text(cr, "GTA 6 · LAUNCH DAY", 540, 515, 56, (1, 1, 1))
        # Regale mit Spielen
        for r in range(3):
            cr.rectangle(60, 760 + r * 170, 960, 14); cr.set_source_rgb(*rgb("#8C96A3")); cr.fill()
            for k in range(9):
                filled = mode == "full" or (mode == "low" and k < 2 and r == 0)
                if filled:
                    game_box(cr, 120 + k * 105, 690 + r * 170, 0.8)
        if mode == "sold":
            rrect(cr, 300, 690, 480, 120, 12); cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
            _text(cr, "SOLD OUT", 540, 770, 70, (1, 1, 1))
        # Theke
        rrect(cr, 520, 1250, 560, 40, 8); fill_stroke(cr, rgb("#3A3F48"), 5)
        cr.rectangle(540, 1290, 540, 270); fill_stroke(cr, rgb("#2E3440"), 5)
        rrect(cr, 900, 1170, 120, 80, 8); fill_stroke(cr, rgb("#15181F"), 4)
        gl = cairo.RadialGradient(540, 500, 20, 540, 500, 700)
        gl.add_color_stop_rgba(0, 1, 0.3, 0.8, 0.18); gl.add_color_stop_rgba(1, 1, 0.3, 0.8, 0)
        cr.set_source(gl); cr.paint()
        s_.flush()
        return s_
    return make


def queue_crowd(cr):
    t = bgm.CLOCK["t"]
    import anim
    for k in range(4):
        lk = Look(shirt=[(0.4, 0.7, 0.9), (0.9, 0.5, 0.3), (0.5, 0.8, 0.5), (0.8, 0.4, 0.7)][k], skin=SKIN if k % 2 else (0.70, 0.52, 0.40),
                  iris=(0.3, 0.3, 0.3), hair=["long", "buzz", "spiky", "bob"][k], hair_color=[(0.2, 0.1, 0.05), (0.1, 0.1, 0.1), (0.9, 0.8, 0.5), (0.6, 0.3, 0.1)][k],
                  outfit="hoodie", shoes=True)
        anim.actor(cr, f"q{k}", lk, 20 + k * 95, 1620, 0.5, 1, pose=("phone", "cross", "idle", "hips")[k], emotion="neutral", t=t,
                   prop="phone" if k == 0 else None)


def stamp(s_):
    return lambda cr, t: MU.stamp(cr, s_)


BG = {"store": store("full"), "store_low": store("low"), "store_sold": store("sold"), "office": B.boss_office, "open": B.open_office, "jroom": jake_room, "groom": gary_room, "dark": None}


def _dark():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    c = cairo.Context(s); c.set_source_rgb(*rgb("#11151C")); c.paint(); s.flush()
    return s


BG["dark"] = _dark

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def jake_couch(after=None):
    d = dict(bg="jroom", layers=[("fn", couch_back), ("char", "J", 380, 1760, 1.05, 1, dict(sit=True)), ("fn", couch_front)])
    if after:
        d["front"] = after
    return d


def gary_couch():
    return dict(bg="groom", layers=[("fn", lambda cr: couch_back(cr, 360, "#5E2B4A")),
                                    ("char", "G", 620, 1760, 1.05, -1, dict(sit=True, look=GARY_HOME)),
                                    ("fn", lambda cr: couch_front(cr, 360, "#4E2240"))])


def st(bg, layers, crowd=True):
    return dict(bg=bg, layers=([("fn", queue_crowd)] if crowd else []) + layers)


def boxprop(x, y, s=1.0):
    return ("fn", lambda cr: game_box(cr, x, y, s))


SHOTS = {
    "s_cold": st("store_low", [("char", "C", 860, Y2, 0.95, -1), ("char", "J", 560, Y2, 0.95, 1, dict(look=JAKE_CASUAL)),
                                ("char", "G", 240, Y2, 0.95, 1, dict(look=GARY_CASUAL))], crowd=False),
    "s_J": st("store_low", [("char", "C", 900, Y2, 0.95, -1), ("char", "J", 540, Y1, 1.2, 1, dict(look=JAKE_CASUAL))]),
    "s_G": st("store_low", [("char", "G", 540, Y1, 1.2, 1, dict(look=GARY_CASUAL))]),
    "s_JG": st("store_low", [("char", "G", 260, Y2, 0.95, 1, dict(look=GARY_CASUAL)), ("char", "J", 560, Y2, 0.95, -1, dict(look=JAKE_CASUAL)),
                              ("char", "C", 880, Y2, 0.95, -1)], crowd=False),
    "s_C": st("store_low", [("char", "C", 880, Y1, 1.2, -1), boxprop(700, 1210, 1.3)], crowd=False),
    "s_Jbox": st("store", [("char", "J", 540, Y1, 1.2, 1, dict(look=JAKE_CASUAL)), boxprop(720, 1080, 1.4)], crowd=False),
    "s_JGP": st("store_low", [("char", "G", 200, Y2, 0.9, 1, dict(look=GARY_CASUAL)), ("char", "J", 470, Y2, 0.9, 1, dict(look=JAKE_CASUAL)),
                               ("char", "P", 760, Y2, 0.9, -1, dict(look=PAM_CASUAL))], crowd=False),
    "s_P": st("store_low", [("char", "P", 540, Y1, 1.2, -1, dict(look=PAM_CASUAL))], crowd=False),
    "sold_GP": st("store_sold", [("char", "G", 300, Y2, S2, 1, dict(look=GARY_CASUAL)), ("char", "P", 760, Y2, S2, -1, dict(look=PAM_CASUAL))], crowd=False),
    "sold_C": st("store_sold", [("char", "C", 880, Y1, 1.2, -1)], crowd=False),
    "sold_G": st("store_sold", [("char", "G", 860, Y1, 1.2, -1, dict(look=GARY_CASUAL))], crowd=False),
    "email_store": dict(bg="dark", overlays=[lambda cr, t: ceo_email(cr, t)], layers=[]),
    "cold": dict(bg="dark", overlays=[lobby(["jake", "gary"], joined="gary")], layers=[]),
    "night": dict(bg="office", layers=[("char", "G", 540, Y1, S1, 1), ("fn", B.boss_desk)], front=[stamp("THE DAY BEFORE")]),
    "office_G": dict(bg="office", layers=[("char", "G", 540, 1700, 1.3, 1, dict(hide_legs=True)), ("fn", B.boss_desk)]),
    "office_J": dict(bg="office", layers=[("char", "J", 600, Y1, S1, -1, dict(look=JAKE_WORK))]),
    "office_GJ": dict(bg="office", layers=[("char", "G", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "J", 820, 1760, 1.0, -1, dict(look=JAKE_WORK))]),
    "open_JM": dict(bg="open", layers=[("char", "M", 300, Y2, S2, 1), ("char", "J", 780, Y2, S2, -1, dict(look=JAKE_WORK))]),
    "call_gary": dict(bg="dark", overlays=[phone_call("Gary (Boss)", "00:12")], layers=[]),
    "jcouch": jake_couch(),
    "gcouch": gary_couch(),
    "lobby2": dict(bg="dark", overlays=[lobby(["jake", "gary"])], layers=[]),
    "lobby2_join": dict(bg="dark", overlays=[lobby(["jake", "gary"], joined="gary")], layers=[]),
    "lobby3_join": dict(bg="dark", overlays=[lobby(["jake", "gary", "pam"], joined="pam")], layers=[]),
    "lobby3": dict(bg="dark", overlays=[lobby(["jake", "gary", "pam"])], layers=[]),
    "kick": dict(bg="dark", overlays=[lobby(["jake", "gary", "pam"], kicked="gary")], layers=[]),
    "email": dict(bg="dark", overlays=[ceo_email], layers=[]),
    "pam_couch": dict(bg="jroom", layers=[("fn", lambda cr: couch_back(cr, 220, "#5B3B6E")),
                                          ("char", "P", 480, 1760, 1.05, 1, dict(sit=True)),
                                          ("fn", lambda cr: couch_front(cr, 220, "#4B2F5E"))]),
}
