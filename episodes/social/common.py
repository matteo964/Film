"""Gemeinsame Besetzung/Sets: "Boss fires the social media manager who made the company go viral"."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss fires the social media manager", "who made the company go viral"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
PURPLE = (0.45, 0.33, 0.75)
GREEN = (0.35, 0.75, 0.45)

CHARS = {
    # Chloe – Social-Media-Managerin (Heldin)
    "C": dict(voice="en-US-EmmaMultilingualNeural", el_voice="FGY2WhTYpPnrIDTdsKH5",  # Laura
              look=Look(shirt=CYAN, ponytail=True, lashes=True)),
    # Rick – Boomer-Chef
    "R": dict(voice="en-US-RogerNeural", el_voice="pqHfZKP75CvOlQylNhV4",  # Bill
              look=Look(shirt=WHITE, tie=True, collar=True, moustache=True)),
    # Jake – junger Kollege aus dem Marketing
    "J": dict(voice="en-US-SteffanNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ",  # Liam
              look=Look(shirt=GREEN, cap=True)),
    # Grace Park – Sponsorin (Sneaker-Marke Sprinto)
    "P": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX",  # Matilda
              look=Look(shirt=PURPLE, bun=True, lashes=True)),
}

BG = {
    "office": lambda: bg.office(False),
    "apartment": bg.apartment,
    "s_profile": bg.socialroom("profile"),
    "s_flop": bg.socialroom("flop"),
    "s_chloe": bg.socialroom("chloe"),
    "s_back": bg.socialroom("back"),
}

L, R, Y = 300, 780, 1740


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, L, Y, 1.0, 1), ("char", right, R, Y, 1.0, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y, 0.9, 1), ("char", m, 545, Y, 0.9, fm),
                              ("char", c, 875, Y, 0.9, -1)])


SHOTS = {
    "office_RC": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "R", 300, 1700, 1.0, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "C", 790, 1730, 1.0, -1),
    ]),
    "home": dict(bg="apartment", layers=[
        ("fn", bg.couch_back), ("fn", bg.couch_front),
        ("char", "C", 300, 1750, 1.0, 1, dict(sit=True)),
    ]),
}
for m in ("profile", "flop", "chloe", "back"):
    b = "s_" + m
    SHOTS[f"{m}_RJ"] = two(b, "R", "J")
    SHOTS[f"{m}_RP"] = two(b, "R", "P")
    SHOTS[f"{m}_RPJ"] = three(b, "R", "P", "J")
    SHOTS[f"{m}_R"] = dict(bg=b, layers=[("char", "R", 540, Y, 1.05, 1)])
    SHOTS[f"{m}_RC"] = two(b, "R", "C")
