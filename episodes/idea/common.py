"""Gemeinsame Besetzung/Sets (Illustrationsstil): "Your coworker steals your idea in front of the CEO"."""
import backgrounds_v2 as B
import explainer_kit as K
from backgrounds import rgb, _text
from stickman import Look, rrect

GAP = 0.15
HOOK_BASE = ["POV: Your coworker steals your idea", "in front of the CEO"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
MIA = Look(shirt=(0.93, 0.58, 0.42), skin=(0.90, 0.76, 0.62), iris=(0.40, 0.28, 0.16), hair="curly",
           hair_color=(0.55, 0.22, 0.12), outfit="blouse", shoes=True, lashes=True)
BRAD = Look(shirt=(0.18, 0.35, 0.65), skin=SKIN, iris=(0.30, 0.50, 0.80), hair="sidepart", hair_color=(0.10, 0.09, 0.09),
            outfit="suit", tie_color=(0.90, 0.85, 0.30), shoes=True)
OKAFOR = Look(shirt=(0.22, 0.22, 0.26), skin=(0.48, 0.33, 0.24), iris=(0.25, 0.16, 0.10), hair="bald",
              hair_color=(0.75, 0.75, 0.78), beard=(0.78, 0.78, 0.80), outfit="suit", tie_color=(0.10, 0.45, 0.50), shoes=True)
JENNA = Look(shirt=(0.40, 0.68, 0.45), skin=SKIN, iris=(0.25, 0.50, 0.30), hair="long", hair_color=(0.78, 0.30, 0.15),
             outfit="blouse", shoes=True, lashes=True)

CHARS = {
    "M": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=MIA),     # Jessica
    "B": dict(voice="en-US-AndrewMultilingualNeural", el_voice="IKne3meq5aSn9XLyUdCD", look=BRAD),  # Charlie
    "O": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=OKAFOR),       # Brian
    "J": dict(voice="en-US-AvaNeural", el_voice="FGY2WhTYpPnrIDTdsKH5", look=JENNA),                # Laura
}

BG = {"open": B.open_office}
for m in ("pitch", "blank", "history", "approved"):
    BG[m] = B.meeting2(m)

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def clock_label(s):
    def fn(cr, t):
        K.label(cr, s, 540, 560, 44, rgb("#FFD45C"))
    return fn


def night(cr, t):
    B.night_overlay(cr)


def gym_phone(cr, t):
    x, y, w, h = 90, 900, 420, 600
    rrect(cr, x, y, w, h, 34)
    cr.set_source_rgb(*rgb("#15181F")); cr.fill()
    rrect(cr, x + 18, y + 22, w - 36, h - 44, 22)
    cr.set_source_rgb(*rgb("#F4F7FD")); cr.fill()
    _text(cr, "@brad_lifts", x + 50, y + 80, 30, rgb("#1B1F27"), center=False)
    _text(cr, "Tue 2:04 AM", x + 50, y + 118, 24, rgb("#6E7A88"), bold=False, center=False)
    rrect(cr, x + 40, y + 140, w - 80, 300, 16)
    cr.set_source_rgb(*rgb("#FFB36B")); cr.fill()
    # Hantel
    cr.rectangle(x + 120, y + 280, 180, 16); cr.set_source_rgb(*rgb("#2B2B2B")); cr.fill()
    for dx in (100, 300):
        cr.rectangle(x + dx, y + 245, 22, 86); cr.fill()
    _text(cr, "No days off. Grinding.", x + w / 2, y + 500, 28, rgb("#1B1F27"))


def one(b, cid, x=540, facing=1, front=None, after=None, opts=None):
    d = dict(bg=b, layers=[("char", cid, x, Y1, S1, facing, opts or {})] + ([("fn", front)] if front else []))
    if after:
        d["front"] = after
    return d


def two(b, left, right, after=None):
    d = dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])
    if after:
        d["front"] = after
    return d


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, fm), ("char", c, 875, Y2, 0.9, -1)])


SHOTS = {
    "night_M": one("open", "M", 330, 1, front=lambda cr: B.work_desk(cr, True), after=[night, clock_label("TUESDAY · 2:07 AM")]),
    "eve_BM": dict(bg="open", layers=[("char", "M", 300, Y2, S2, 1), ("fn", lambda cr: B.work_desk(cr, True)),
                                      ("char", "B", 820, Y2, S2, -1)], front=[clock_label("TUESDAY · 5:03 PM")]),
    "open_MJ": two("open", "J", "M"),
    "open_M": one("open", "M", 560, -1),
    "open_J": one("open", "J", 480, 1),
}
for m in ("pitch", "blank", "history", "approved"):
    SHOTS[f"{m}_O"] = one(m, "O", 880, -1)
    SHOTS[f"{m}_B"] = one(m, "B", 880, -1)
    SHOTS[f"{m}_M"] = one(m, "M", 880, -1)
    SHOTS[f"{m}_BO"] = two(m, "B", "O")
    SHOTS[f"{m}_MO"] = two(m, "M", "O")
    SHOTS[f"{m}_BMO"] = three(m, "B", "M", "O")
SHOTS["history_O_phone"] = dict(bg="history", layers=[("char", "O", 880, Y1, S1, -1)], front=[gym_phone])
