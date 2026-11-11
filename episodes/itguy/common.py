"""Gemeinsame Besetzung/Sets (Illustrationsstil): "Your boss fires the IT guy who runs the company for someone cheaper"."""
import math

import anim
import backgrounds as bgm
import backgrounds_v2 as B
from stickman import Look

GAP = 0.15
HOOK_BASE = ["POV: Your boss fires the IT guy who runs", "the company for someone cheaper"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
NOAH = Look(shirt=(0.30, 0.45, 0.70), skin=(0.78, 0.60, 0.45), iris=(0.30, 0.20, 0.12), hair="curly",
            hair_color=(0.12, 0.10, 0.10), outfit="hoodie", shoes=True)
VICTOR = Look(shirt=(0.25, 0.25, 0.28), skin=SKIN, iris=(0.35, 0.45, 0.60), hair="bald", hair_color=(0.35, 0.25, 0.18),
              beard=(0.40, 0.28, 0.20), outfit="suit", tie_color=(0.55, 0.20, 0.65), shoes=True)
KEVIN = Look(shirt=(0.85, 0.55, 0.25), skin=SKIN, iris=(0.30, 0.55, 0.30), hair="buzz", hair_color=(0.55, 0.35, 0.20),
             glasses=True, outfit="blouse", shirt_inner=(0.2, 0.2, 0.22), shoes=True)
DIANA = Look(shirt=(0.15, 0.20, 0.30), skin=SKIN, iris=(0.30, 0.45, 0.70), hair="long", hair_color=(0.92, 0.80, 0.50),
             glasses=True, outfit="suit", tie_color=(0.9, 0.9, 0.9), shoes=True, lashes=True)

CHARS = {
    "N": dict(voice="en-US-ChristopherNeural", el_voice="CwhRBWXzGAHq8TQ4Fs17", look=NOAH),      # Roger
    "V": dict(voice="en-US-AndrewMultilingualNeural", el_voice="pNInz6obpgDQGcFmaJgB", look=VICTOR),  # Adam
    "K": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=KEVIN),          # Liam
    "D": dict(voice="en-US-MichelleNeural", el_voice="hpp4J3VqNfWAUOO0d1Us", look=DIANA),        # Bella
}

BG = {
    "office": B.boss_office,
    "it": B.it_room,
    "lobby": B.lobby("red"),
    "lobby_ok": B.lobby("green"),
    "living": B.living,
}

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0
PAL = [(0.95, 0.45, 0.45), (0.45, 0.75, 0.95), (0.98, 0.80, 0.25), (0.55, 0.85, 0.50), (0.75, 0.55, 0.95)]
HAIRS = ["long", "sidepart", "bob", "buzz", "spiky", "curly"]


def one(b, cid, x=540, facing=1, front=None, opts=None, back=None):
    layers = []
    if back:
        layers.append(("fn", back))
    layers.append(("char", cid, x, Y1, S1, facing, opts or {}))
    if front:
        layers.append(("fn", front))
    return dict(bg=b, layers=layers)


def two(b, left, right, front=None, back=None):
    layers = ([("fn", back)] if back else []) + [("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)]
    if front:
        layers.append(("fn", front))
    return dict(bg=b, layers=layers)


def desk_plugged(cr):
    B.it_desk(cr, True)


UNPLUG_AT = 1.0


def desk_unplug(cr):
    lt = bgm.CLOCK["lt"]
    B.it_desk(cr, lt < UNPLUG_AT)


def blackout(cr, t):
    lt = bgm.CLOCK["lt"]
    if lt > UNPLUG_AT:
        k = min(1.0, (lt - UNPLUG_AT) * 3)
        cr.set_source_rgba(0.02, 0.03, 0.08, 0.55 * k); cr.paint()
        if int((lt - UNPLUG_AT) * 2.5) % 2 == 0:
            g = __import__("cairo").RadialGradient(540, 300, 20, 540, 300, 900)
            g.add_color_stop_rgba(0, 1, 0.1, 0.1, 0.30); g.add_color_stop_rgba(1, 1, 0.1, 0.1, 0)
            cr.set_source(g); cr.paint()


def crowd(cr):
    t = bgm.CLOCK["t"]
    for k in range(6):
        lk = Look(shirt=PAL[k % 5], skin=SKIN if k % 3 else (0.78, 0.60, 0.45), iris=(0.3, 0.3, 0.3), hair=HAIRS[k],
                  hair_color=((0.3, 0.2, 0.1), (0.9, 0.8, 0.5), (0.1, 0.1, 0.1))[k % 3], outfit="blouse", shoes=True)
        x = 80 + k * 190
        anim.actor(cr, f"c{k}", lk, x, 2010, 0.62, 1 if k % 2 else -1, pose=("cross", "hips", "phone", "shrug")[k % 4],
                   emotion=("annoyed", "worried", "confused")[k % 3], t=t, prop="phone" if k % 4 == 2 else None)


def kevin_inside(cr):
    t = bgm.CLOCK["t"]
    cr.push_group()
    knock = (t * 2.5) % 1 < 0.5
    anim.actor(cr, "K", KEVIN, 430, 1290, 0.75, 1, pose="stop" if knock else "panic", emotion="worried", t=t)
    cr.pop_group_to_source()
    cr.paint_with_alpha(0.75)
    cr.rectangle(320, 540, 220, 760)
    cr.set_source_rgba(0.75, 0.88, 0.96, 0.25); cr.fill()


SHOTS = {
    "office_V": one("office", "V", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_N": one("office", "N", 600, -1),
    "office_VN": dict(bg="office", layers=[("char", "V", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "N", 820, 1760, 1.0, -1)]),
    "office_VNK": dict(bg="office", layers=[("char", "V", 230, 1720, 0.9, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                            ("char", "N", 640, 1760, 0.9, -1), ("char", "K", 900, 1760, 0.9, -1)]),
    "office_K": one("office", "K", 600, -1),
    "it_K": one("it", "K", 330, 1, front=desk_plugged),
    "it_K_unplug": dict(bg="it", layers=[("char", "K", 330, Y1, S1, 1), ("fn", desk_unplug)], front=[blackout]),
    "lobby_V": dict(bg="lobby", layers=[("char", "V", 540, Y1, S1, 1)], front=[]),
    "lobby_D": dict(bg="lobby", layers=[("char", "D", 600, Y1, S1, -1)]),
    "lobby_VD": two("lobby", "V", "D", front=crowd),
    "lobby_K": dict(bg="lobby", layers=[("fn", kevin_inside), ("char", "V", 760, Y1, S1, -1)]),
    "home_N": dict(bg="living", layers=[("fn", B.sofa_back), ("fn", B.sofa_front),
                                        ("char", "N", 420, 1740, 1.05, 1, dict(sit=True))]),
    "lobby_V_phone": dict(bg="lobby", layers=[("char", "V", 540, Y1, S1, 1)]),
    "lobby_VD_phone": two("lobby", "V", "D"),
    "ok_VD": two("lobby_ok", "V", "D", front=crowd),
    "ok_NK": two("lobby_ok", "K", "N"),
    "ok_NV": two("lobby_ok", "V", "N"),
}
