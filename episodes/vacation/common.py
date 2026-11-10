"""Gemeinsame Besetzung/Sets: "Your manager cancels your approved vacation"."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your manager cancels", "your approved vacation"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
PURPLE = (0.45, 0.33, 0.75)
NAVY = (0.20, 0.27, 0.45)
PINK = (0.97, 0.62, 0.72)

CHARS = {
    # Ava Brooks – Account-Managerin (Heldin)
    "A": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9",  # Jessica
              look=Look(shirt=CYAN, ponytail=True, lashes=True)),
    # Todd – Manager
    "T": dict(voice="en-US-AndrewMultilingualNeural", el_voice="pNInz6obpgDQGcFmaJgB",  # Adam
              look=Look(shirt=WHITE, tie=True, collar=True)),
    # Richard Morgan – Großkunde
    "M": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb",  # Brian
              look=Look(shirt=NAVY, tie=True, collar=True, moustache=True)),
    # Ms. Grant – HR-Direktorin
    "H": dict(voice="en-US-MichelleNeural", el_voice="EXAVITQu4vr4xnSDxMaL",  # Sarah
              look=Look(shirt=PURPLE, bun=True, lashes=True, glasses=True)),
    # Lily – Avas Schwester, die Braut
    "L": dict(voice="en-US-AvaNeural", el_voice="FGY2WhTYpPnrIDTdsKH5",  # Laura
              look=Look(shirt=WHITE, bun=True, lashes=True)),
}
AVA_DRESS = Look(shirt=PINK, ponytail=True, lashes=True)

BG = {
    "office": lambda: bg.office(False),
    "slides": bg.meeting("slides"),
    "signed": bg.meeting("signed"),
    "wedding": bg.wedding,
}

L, R, Y = 300, 780, 1740


def two(b, left, right, lo=None, ro=None):
    return dict(bg=b, layers=[("char", left, L, Y, 1.0, 1, lo or {}), ("char", right, R, Y, 1.0, -1, ro or {})])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y, 0.9, 1), ("char", m, 545, Y, 0.9, fm),
                              ("char", c, 875, Y, 0.9, -1)])


SHOTS = {
    "office_TA": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "T", 300, 1700, 1.0, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "A", 790, 1730, 1.0, -1),
    ]),
    "wedding_A": dict(bg="wedding", layers=[("char", "A", 400, Y, 1.05, 1, dict(look=AVA_DRESS))]),
    "wedding_LA": two("wedding", "A", "L", lo=dict(look=AVA_DRESS)),
}
for m in ("slides", "signed"):
    SHOTS[f"{m}_TM"] = two(m, "T", "M")
    SHOTS[f"{m}_TH"] = two(m, "T", "H")
    SHOTS[f"{m}_THM"] = three(m, "T", "H", "M")
    SHOTS[f"{m}_T"] = dict(bg=m, layers=[("char", "T", 540, Y, 1.05, 1)])
    SHOTS[f"{m}_M"] = dict(bg=m, layers=[("char", "M", 540, Y, 1.05, -1)])
