"""Gemeinsame Besetzung/Sets: "An influencer tries to get a free meal by blaming the waitress"."""
import backgrounds as bg
from backgrounds import rgb, _text
from stickman import Look, rrect

GAP = 0.15
HOOK_BASE = ["POV: An influencer tries to get a free meal", "by blaming the waitress"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
MAGENTA = (0.92, 0.35, 0.62)
NAVY = (0.12, 0.17, 0.32)

CHARS = {
    # Jess – Kellnerin (Heldin)
    "J": dict(voice="en-US-EmmaMultilingualNeural", el_voice="EXAVITQu4vr4xnSDxMaL",  # Sarah
              look=Look(shirt=CYAN, ponytail=True, lashes=True, apron=True)),
    # Brittany – Influencerin
    "B": dict(voice="en-US-AvaNeural", el_voice="FGY2WhTYpPnrIDTdsKH5",  # Laura
              look=Look(shirt=MAGENTA, bun=True, lashes=True)),
    # Frank – Restaurantmanager
    "F": dict(voice="en-US-RogerNeural", el_voice="cjVigY5qzO86Huf0OWal",  # Eric
              look=Look(shirt=WHITE, tie=True, collar=True, moustache=True)),
    # Officer Davis
    "O": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb",  # Brian
              look=Look(shirt=NAVY, police=True)),
}

BG = {m: bg.restaurant(m) for m in ("menu", "cctv", "cctv2", "viral")}


def live_panel(viewers, comments, bad=False):
    """Livestream-Handy rechts unten (Brittanys Stream)."""
    def fn(cr, t):
        x, y, w, h = 700, 1180, 340, 560
        rrect(cr, x, y, w, h, 30)
        cr.set_source_rgba(0.05, 0.05, 0.08, 0.92)
        cr.fill()
        rrect(cr, x + 20, y + 22, 82, 40, 10)
        cr.set_source_rgb(*rgb("#FF2D55"))
        cr.fill()
        _text(cr, "LIVE", x + 61, y + 52, 26, (1, 1, 1))
        _text(cr, viewers, x + 120, y + 52, 26, (1, 1, 1), center=False)
        _text(cr, "@brittany.eats", x + 20, y + 100, 24, rgb("#C9D3E6"), center=False)
        n = min(len(comments), 1 + int(bg.CLOCK["lt"] / 0.9))
        for k, c in enumerate(comments[:n]):
            yy = y + 150 + k * 78
            rrect(cr, x + 16, yy, w - 32, 64, 14)
            cr.set_source_rgba(1, 1, 1, 0.12)
            cr.fill()
            _text(cr, c, x + 30, yy + 42, 22, rgb("#FF8A8A") if bad else (1, 1, 1), bold=False, center=False)
    return fn


LIVE_GOOD = live_panel("48.2K", ["omg you poor thing", "get her fired!!", "this place is trash", "free meal queen"])
LIVE_BAD = live_panel("48.2K", ["SHE PUT IT THERE", "caught in 4K", "unfollowed.", "apologize to Jess!!", "scammer"], bad=True)

L, R, Y = 300, 780, 1740


def two(m, left, right, front=None):
    d = dict(bg=m, layers=[("char", left, L, Y, 1.0, 1), ("char", right, R, Y, 1.0, -1)])
    if front:
        d["front"] = [front]
    return d


def three(m, a, b, c, fb=-1, front=None):
    d = dict(bg=m, layers=[("char", a, 210, Y, 0.9, 1), ("char", b, 545, Y, 0.9, fb), ("char", c, 875, Y, 0.9, -1)])
    if front:
        d["front"] = [front]
    return d


SHOTS = {}
for m in ("menu", "cctv", "cctv2", "viral"):
    SHOTS[f"{m}_BJ"] = two(m, "B", "J")
    SHOTS[f"{m}_FJ"] = two(m, "F", "J")
    SHOTS[f"{m}_BF"] = two(m, "B", "F")
    SHOTS[f"{m}_OB"] = two(m, "O", "B")
    SHOTS[f"{m}_BFJ"] = three(m, "B", "F", "J")
    SHOTS[f"{m}_OBJ"] = three(m, "O", "B", "J")
    SHOTS[f"{m}_B"] = dict(bg=m, layers=[("char", "B", 400, Y, 1.05, 1)])
SHOTS["menu_B_live"] = dict(bg="menu", layers=[("char", "B", 330, Y, 1.05, 1)], front=[LIVE_GOOD])
SHOTS["cctv2_B_live"] = dict(bg="cctv2", layers=[("char", "B", 330, Y, 1.05, 1)], front=[LIVE_BAD])
