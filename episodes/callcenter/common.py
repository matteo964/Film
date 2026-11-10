"""Gemeinsame Besetzung/Sets: "Your manager makes you apologize to a rude customer"."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your manager makes you apologize", "to a rude customer"]

CYAN = (0.15, 0.80, 0.91)
WHITE = (0.99, 0.99, 0.99)
MAGENTA = (0.85, 0.30, 0.55)
GREEN = (0.35, 0.75, 0.45)

CHARS = {
    # Maya – Callcenter-Agentin (Heldin)
    "M": dict(voice="en-US-MichelleNeural", el_voice="EXAVITQu4vr4xnSDxMaL",  # Sarah
              look=Look(shirt=CYAN, ponytail=True, lashes=True, headset=True)),
    # Gary – Teamleiter
    "G": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal",  # Eric
              look=Look(shirt=WHITE, tie=True, collar=True)),
    # "Karen" – unverschämte Kundin / in Wahrheit Linda Holt, Qualitätsprüferin der Zentrale
    "K": dict(voice="en-US-EmmaMultilingualNeural", el_voice="FGY2WhTYpPnrIDTdsKH5",  # Laura
              look=Look(shirt=MAGENTA, bun=True, lashes=True, glasses=True)),
    # Devin – Kollege
    "D": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o",  # Will
              look=Look(shirt=GREEN, headset=True)),
}

BG = {
    "queue": bg.callcenter("queue"),
    "recording": bg.callcenter("recording"),
    "report": bg.callcenter("report"),
}

L, R, Y = 300, 780, 1740


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, L, Y, 1.0, 1), ("char", right, R, Y, 1.0, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y, 0.9, 1), ("char", m, 545, Y, 0.9, fm),
                              ("char", c, 875, Y, 0.9, -1)])


SHOTS = {}
for m in ("queue", "recording", "report"):
    SHOTS[f"{m}_GM"] = two(m, "G", "M")
    SHOTS[f"{m}_DM"] = two(m, "D", "M")
    SHOTS[f"{m}_KM"] = two(m, "K", "M")
    SHOTS[f"{m}_GK"] = two(m, "G", "K")
    SHOTS[f"{m}_GKM"] = three(m, "G", "K", "M")
    SHOTS[f"{m}_GDM"] = three(m, "G", "D", "M")
    SHOTS[f"{m}_M"] = dict(bg=m, layers=[("char", "M", 540, Y, 1.05, -1)])
