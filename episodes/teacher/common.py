"""Gemeinsame Besetzung/Sets: "Teacher accuses you of cheating because you got 100%"."""
import backgrounds as bg
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your teacher accuses you of cheating", "because you got 100%"]

CYAN = (0.15, 0.80, 0.91)
TAN = (0.80, 0.66, 0.45)
PURPLE = (0.45, 0.33, 0.75)
CORAL = (1.0, 0.55, 0.45)

CHARS = {
    # Leo – stiller Schüler (Held)
    "L": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o",  # Will
              look=Look(shirt=CYAN)),
    # Mr. Crane – arroganter Mathelehrer
    "C": dict(voice="en-US-ChristopherNeural", el_voice="N2lVS1w4EtoT3dr4eOWO",  # Callum
              look=Look(shirt=TAN, tie=True, collar=True, glasses=True)),
    # Kayla – Mitschülerin
    "K": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9",  # Jessica
              look=Look(shirt=CORAL, ponytail=True, lashes=True)),
    # Dr. Reyes – Schulleiterin
    "R": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX",  # Matilda
              look=Look(shirt=PURPLE, bun=True, lashes=True)),
}

BG = {
    "final": bg.classroom("final"),
    "problem": bg.classroom("problem"),
    "solved": bg.classroom("solved"),
}

L, R, Y = 300, 770, 1740


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, L, Y, 1.0, 1), ("char", right, R, Y, 1.0, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y, 0.9, 1), ("char", m, 545, Y, 0.9, fm),
                              ("char", c, 875, Y, 0.9, -1)])


SHOTS = {}
for b in ("final", "problem", "solved"):
    SHOTS[f"{b}_CL"] = two(b, "C", "L")
    SHOTS[f"{b}_CK"] = two(b, "C", "K")
    SHOTS[f"{b}_KL"] = two(b, "K", "L")
    SHOTS[f"{b}_RC"] = two(b, "R", "C")
    SHOTS[f"{b}_RL"] = two(b, "R", "L")
    SHOTS[f"{b}_CLK"] = three(b, "C", "L", "K")
    SHOTS[f"{b}_RCL"] = three(b, "R", "C", "L")
    # Leo schreibt an der Tafel (Blick nach rechts zur Tafel hin), Crane schaut zu
    SHOTS[f"{b}_board"] = dict(bg=b, layers=[("char", "L", 300, Y, 1.0, 1), ("char", "C", 840, Y, 1.0, -1)])
