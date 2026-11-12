"""Gemeinsame Besetzung/Sets (Illustrationsstil): Kunde zahlt die Hochzeitsfotografin nicht."""
import backgrounds_v2 as B
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your client refuses to pay the freelance", "photographer who shot his daughter's wedding"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
LILY = Look(shirt=(0.15, 0.15, 0.18), skin=(0.93, 0.84, 0.70), iris=(0.25, 0.17, 0.10), hair="bob",
            hair_color=(0.08, 0.07, 0.08), outfit="blouse", shirt_inner=(0.85, 0.30, 0.35), shoes=True, lashes=True)
RICHARD = Look(shirt=(0.16, 0.20, 0.35), skin=SKIN, iris=(0.35, 0.45, 0.60), hair="sidepart", hair_color=(0.93, 0.93, 0.95),
               glasses=True, outfit="suit", tie_color=(0.80, 0.65, 0.20), shoes=True)
EMILY = Look(shirt=(0.99, 0.99, 0.99), skin=SKIN, iris=(0.30, 0.50, 0.75), hair="updo", hair_color=(0.62, 0.42, 0.22),
             outfit="blouse", shirt_inner=(0.97, 0.94, 0.90), shoes=True, lashes=True)
JAKE = Look(shirt=(0.55, 0.30, 0.25), skin=SKIN, iris=(0.30, 0.45, 0.30), hair="spiky", hair_color=(0.45, 0.28, 0.15),
            outfit="suit", tie_color=(0.20, 0.55, 0.85), shoes=True)
SOPHIE = Look(shirt=(0.60, 0.35, 0.70), skin=(0.70, 0.52, 0.40), iris=(0.25, 0.16, 0.10), hair="long",
              hair_color=(0.10, 0.08, 0.08), outfit="blouse", shoes=True, lashes=True)

CHARS = {
    "L": dict(voice="en-US-EmmaMultilingualNeural", el_voice="FGY2WhTYpPnrIDTdsKH5", look=LILY),     # Laura
    "R": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal", look=RICHARD),  # Eric
    "E": dict(voice="en-US-AvaNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=EMILY),                 # Jessica
    "J": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=JAKE),               # Liam
    "S": dict(voice="en-US-MichelleNeural", el_voice="hpp4J3VqNfWAUOO0d1Us", look=SOPHIE),           # Bella
}

BG = {"office": B.boss_office, "living": B.living}
for m in ("photo", "watermark", "nephew", "final"):
    BG[m] = B.reception(m)

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def one(b, cid, x=540, facing=1, front=None, opts=None, back=None):
    layers = ([("fn", back)] if back else []) + [("char", cid, x, Y1, S1, facing, opts or {})]
    if front:
        layers.append(("fn", front))
    return dict(bg=b, layers=layers)


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, fm), ("char", c, 875, Y2, 0.9, -1)])


SHOTS = {
    "office_R": one("office", "R", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_L": one("office", "L", 600, -1),
    "office_RL": dict(bg="office", layers=[("char", "R", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "L", 820, 1760, 1.0, -1)]),
    "home_L": dict(bg="living", layers=[("fn", B.sofa_back), ("fn", B.sofa_front),
                                        ("char", "L", 420, 1740, 1.05, 1, dict(sit=True)), ("fn", B.tripod_camera)]),
}
for m in ("photo", "watermark", "nephew", "final"):
    for cid in ("R", "E", "J", "S"):
        SHOTS[f"{m}_{cid}"] = one(m, cid, 880, -1)
    SHOTS[f"{m}_RE"] = two(m, "R", "E")
    SHOTS[f"{m}_RJ"] = two(m, "R", "J")
    SHOTS[f"{m}_RS"] = two(m, "R", "S")
    SHOTS[f"{m}_RJE"] = three(m, "R", "J", "E")
    SHOTS[f"{m}_RES"] = three(m, "R", "E", "S")
