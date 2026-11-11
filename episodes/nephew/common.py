"""Gemeinsame Besetzung/Sets im Illustrationsstil (Referenz 4): "Your boss gives your promotion to his nephew"."""
import backgrounds_v2 as B
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss gives your", "promotion to his nephew"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
CHARS = {
    # Emma Clarke – seit 6 Jahren im Team (Heldin)
    "E": dict(voice="en-US-MichelleNeural", el_voice="XrExE9yKIg1WjnnlVkGX",  # Matilda
              look=Look(shirt=(0.36, 0.62, 0.58), skin=SKIN, iris=(0.25, 0.45, 0.25), hair="long",
                        hair_color=(0.30, 0.18, 0.10), outfit="blouse", shoes=True, lashes=True)),
    # Mark – Chef
    "M": dict(voice="en-US-AndrewMultilingualNeural", el_voice="cjVigY5qzO86Huf0OWal",  # Eric
              look=Look(shirt=(0.20, 0.27, 0.45), skin=SKIN, iris=(0.45, 0.30, 0.15), hair="sidepart",
                        hair_color=(0.62, 0.62, 0.64), outfit="suit", tie_color=(0.75, 0.15, 0.18), shoes=True,
                        moustache=True)),
    # Tyler – Neffe
    "T": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ",  # Liam
              look=Look(shirt=(0.55, 0.55, 0.58), skin=SKIN, iris=(0.30, 0.55, 0.85), hair="spiky",
                        hair_color=(0.93, 0.78, 0.35), outfit="suit", tie_color=(0.95, 0.75, 0.2), shoes=True)),
    # Margaret Henderson – wichtigste Kundin
    "H": dict(voice="en-US-AriaNeural", el_voice="Xb7hH8MSUJpSbSDYk0k2",  # Alice
              look=Look(shirt=(0.55, 0.15, 0.25), skin=(0.85, 0.70, 0.58), iris=(0.35, 0.25, 0.15), hair="bob",
                        hair_color=(0.82, 0.82, 0.85), outfit="blouse", shoes=True, lashes=True)),
    # Recruiterin von Brightline (nur Telefonstimme)
    "R": dict(voice="en-US-AvaNeural", el_voice="EXAVITQu4vr4xnSDxMaL", look=Look()),  # Sarah
}

BG = {
    "office": B.boss_office,
    "open": B.open_office,
    "slides": B.meeting("slides"),
    "fail": B.meeting("fail"),
    "signed": B.meeting("signed"),
    "living": B.living,
}

Y1, S1 = 1700, 1.3     # Einzel-Einstellung (groß, wie in der Referenz)
Y2, S2 = 1740, 1.0     # Zweier-Einstellung


def one(b, cid, x=540, facing=1, front=None, opts=None):
    layers = [("char", cid, x, Y1, S1, facing, opts or {})]
    if front:
        layers.append(("fn", front))
    return dict(bg=b, layers=layers)


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, fm), ("char", c, 875, Y2, 0.9, -1)])


SHOTS = {
    "office_M": one("office", "M", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_E": one("office", "E", 600, -1),
    "office_ME": dict(bg="office", layers=[("char", "M", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "E", 820, 1760, 1.0, -1)]),
    "open_T": one("open", "T", 480, 1),
    "open_E": one("open", "E", 600, -1),
    "open_ET": two("open", "T", "E"),
    "open_MTE": three("open", "M", "T", "E"),
    "living_E": dict(bg="living", layers=[("fn", B.sofa_back), ("fn", B.sofa_front),
                                          ("char", "E", 420, 1740, 1.05, 1, dict(sit=True))]),
}
for m in ("slides", "fail", "signed"):
    SHOTS[f"{m}_H"] = one(m, "H", 880, -1)
    SHOTS[f"{m}_T"] = one(m, "T", 880, -1)
    SHOTS[f"{m}_M"] = one(m, "M", 880, -1)
    SHOTS[f"{m}_TH"] = two(m, "T", "H")
    SHOTS[f"{m}_MH"] = two(m, "M", "H")
    SHOTS[f"{m}_MTH"] = three(m, "M", "T", "H")
