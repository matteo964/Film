"""Gemeinsame Besetzung/Sets: "Your boss fires the employee keeping the company running" (Payroll)."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss fires the employee", "keeping the company running"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
PURPLE = (0.45, 0.33, 0.75)
CORAL = (1.0, 0.55, 0.45)

CHARS = {
    # Dave Miller – Gehaltsabrechnung seit 15 Jahren (Held)
    "D": dict(voice="en-US-ChristopherNeural", el_voice="CwhRBWXzGAHq8TQ4Fs17",  # Roger
              look=Look(shirt=CYAN, glasses=True)),
    # Brad – neuer "VP of Efficiency"
    "B": dict(voice="en-US-AndrewMultilingualNeural", el_voice="pNInz6obpgDQGcFmaJgB",  # Adam
              look=Look(shirt=WHITE, tie=True, collar=True)),
    # Diane – CEO
    "N": dict(voice="en-US-MichelleNeural", el_voice="EXAVITQu4vr4xnSDxMaL",  # Sarah
              look=Look(shirt=PURPLE, bun=True, lashes=True)),
    # Kayla – Mitarbeiterin
    "K": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9",  # Jessica
              look=Look(shirt=CORAL, ponytail=True, lashes=True)),
    # PayBot – KI-App (nur Stimme)
    "P": dict(voice="en-US-AriaNeural", el_voice="SAz9YHcvj6GT2YYXdXww", robot=True,  # River
              look=Look()),
}

BG = {
    "office": lambda: bg.office(False),
    "apartment": bg.apartment,
    "oo_logo": bg.openoffice("logo"),
    "oo_error": bg.openoffice("error"),
    "oo_paid": bg.openoffice("paid"),
}

L, R, Y = 300, 780, 1740


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, L, Y, 1.0, 1), ("char", right, R, Y, 1.0, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y, 0.9, 1), ("char", m, 545, Y, 0.9, fm),
                              ("char", c, 875, Y, 0.9, -1)])


SHOTS = {
    "office_BD": dict(bg="office", layers=[
        ("fn", lambda cr: bg.office_chair(cr, 300, 930)),
        ("char", "B", 300, 1700, 1.0, 1, dict(hide_legs=True)),
        ("fn", lambda cr: bg.office_desk(cr)),
        ("char", "D", 790, 1730, 1.0, -1),
    ]),
    "home": dict(bg="apartment", layers=[
        ("fn", bg.couch_back), ("fn", bg.couch_front),
        ("char", "D", 300, 1750, 1.0, 1, dict(sit=True)),
    ]),
}
for m in ("logo", "error", "paid"):
    b = "oo_" + m
    SHOTS[f"{m}_BK"] = two(b, "B", "K")
    SHOTS[f"{m}_BN"] = two(b, "B", "N")
    SHOTS[f"{m}_NK"] = two(b, "N", "K")
    SHOTS[f"{m}_BNK"] = three(b, "B", "N", "K")
    SHOTS[f"{m}_B"] = dict(bg=b, layers=[("char", "B", 540, Y, 1.05, 1)])
    SHOTS[f"{m}_N"] = dict(bg=b, layers=[("char", "N", 540, Y, 1.05, 1)])
