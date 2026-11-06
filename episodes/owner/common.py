"""Gemeinsame Besetzung/Sets: "The janitor who secretly owns the company"."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss humiliates the janitor", "who secretly owns the company"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
PURPLE = (0.45, 0.33, 0.75)
CORAL = (1.0, 0.55, 0.45)

CHARS = {
    # Walter Hayes – Hausmeister / heimlicher Eigentümer (ruhig, tief)
    "W": dict(voice="en-US-ChristopherNeural", rate="+4%", pitch="+12Hz",
              look=Look(shirt=CYAN, belt=True, moustache=True)),
    # Derek Collins – arroganter Manager
    "D": dict(voice="en-US-AndrewMultilingualNeural", rate="+8%", pitch="+14Hz",
              look=Look(shirt=WHITE, tie=True, collar=True)),
    # Mia – freundliche Praktikantin
    "M": dict(voice="en-US-EmmaMultilingualNeural", rate="+6%", pitch="+6Hz",
              look=Look(shirt=CORAL, ponytail=True, lashes=True)),
    # Margaret – COO, kennt das Geheimnis
    "G": dict(voice="en-US-MichelleNeural", rate="+6%", pitch="+10Hz",
              look=Look(shirt=PURPLE, bun=True, lashes=True)),
}

BG = {
    "office": lambda: bg.office(False),
    "penthouse": bg.penthouse,
    "conference": bg.conference,
}

L, R, Y = 310, 770, 1740


def two(left, right, bgk="conference", lf=1, rf=-1):
    return dict(bg=bgk, layers=[("char", left, L, Y, 1.0, lf), ("char", right, R, Y, 1.0, rf)])


def three(a, b, c, fb=-1):
    return dict(bg="conference", layers=[("char", a, 215, Y, 0.9, 1), ("char", b, 545, Y, 0.9, fb),
                                         ("char", c, 870, Y, 0.9, -1)])


SHOTS = {
    "office_DW": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "D", 300, 1700, 1.0, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "W", 790, 1730, 1.0, -1),
    ]),
    "office_DWM": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 260, 960)),
        ("char", "D", 260, 1720, 0.92, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "W", 640, 1740, 0.92, -1),
        ("char", "M", 905, 1740, 0.92, -1),
    ]),
    "penthouse": dict(bg="penthouse", layers=[
        ("fn", bg.sofa_back),
        ("fn", bg.sofa_front),
        ("char", "W", 300, 1750, 1.0, 1, dict(sit=True)),
    ]),
    "conf_DM": two("D", "M"),
    "conf_DW": two("D", "W"),
    "conf_DG": two("D", "G"),
    "conf_MW": two("M", "W"),
    "conf_GW": two("G", "W"),
    "conf_DGW": three("D", "G", "W", fb=1),
    "conf_DWM": three("D", "W", "M", fb=-1),
}
