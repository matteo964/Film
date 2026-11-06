"""Gemeinsame Besetzung/Sets: "Boss refuses to pay the freelancer who built the website"."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss refuses to pay the freelancer", "who built the company website"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
PURPLE = (0.45, 0.33, 0.75)
GREY = (0.62, 0.64, 0.68)

CHARS = {
    # Zoe Parker – Freelance-Webdesignerin (Heldin, trocken-sarkastisch)
    "Z": dict(voice="en-US-EmmaMultilingualNeural", el_voice="FGY2WhTYpPnrIDTdsKH5",  # Laura
              look=Look(shirt=CYAN, ponytail=True, lashes=True)),
    # Greg Grant – geiziger Chef
    "G": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal",  # Eric
              look=Look(shirt=WHITE, tie=True, collar=True)),
    # Tyler – Neffe, "kennt sich mit Computern aus"
    "T": dict(voice="en-US-SteffanNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ",  # Liam
              look=Look(shirt=GREY, cap=True)),
    # Linda Chen – Investorin
    "L": dict(voice="en-US-MichelleNeural", el_voice="hpp4J3VqNfWAUOO0d1Us",  # Bella
              look=Look(shirt=PURPLE, bun=True, lashes=True)),
}

BG = {
    "office": lambda: bg.office(False),
    "apartment": bg.apartment,
    "stage_site": bg.stage("site"),
    "stage_down": bg.stage("down"),
    "stage_back": bg.stage("back"),
}

L, R, Y = 310, 770, 1740


def stage_shot(mode, left, right, podium_left=True):
    layers = []
    if podium_left:
        layers += [("char", left, 260, 1720, 1.0, 1), ("fn", bg.podium)]
    else:
        layers += [("char", left, L, Y, 1.0, 1)]
    layers += [("char", right, R, Y, 1.0, -1)]
    return dict(bg="stage_" + mode, layers=layers)


def stage_three(mode, a, b, c):
    return dict(bg="stage_" + mode, layers=[("char", a, 200, Y, 0.9, 1), ("char", b, 540, Y, 0.9, -1),
                                            ("char", c, 880, Y, 0.9, -1)])


SHOTS = {
    "office_GZ": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "G", 300, 1700, 1.0, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "Z", 790, 1730, 1.0, -1),
    ]),
    "office_GZT": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 260, 960)),
        ("char", "G", 260, 1720, 0.92, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "Z", 640, 1740, 0.92, -1),
        ("char", "T", 905, 1740, 0.92, -1),
    ]),
    "apt": dict(bg="apartment", layers=[
        ("fn", bg.couch_back),
        ("fn", bg.couch_front),
        ("char", "Z", 300, 1750, 1.0, 1, dict(sit=True)),
    ]),
}
for m in ("site", "down", "back"):
    SHOTS[f"stage_{m}_GL"] = stage_shot(m, "G", "L")
    SHOTS[f"stage_{m}_GT"] = stage_shot(m, "G", "T", podium_left=False)
    SHOTS[f"stage_{m}_LT"] = stage_shot(m, "L", "T", podium_left=False)
    SHOTS[f"stage_{m}_GLT"] = stage_three(m, "G", "L", "T")
    SHOTS[f"stage_{m}_G"] = dict(bg="stage_" + m, layers=[("char", "G", 540, Y, 1.05, 1)])
