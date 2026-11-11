"""Hilfen, um Figuren direkt in Overlays zu animieren (laufen, Posen, Emotionen, Lippensync)."""
import math
from stickman import POSES, draw_figure

_STATE = {}


def actor(cr, key, look, x, y, scale=1.0, facing=1, pose="idle", emotion="neutral", t=0.0, walk=None,
          prop=None, talk=0.0, look_dir=(1.0, 0.05), sit=False, shiver=0.0):
    """Zeichnet eine Figur; Hände gleiten weich zur Zielpose. walk = Phase (rad) oder None."""
    tgt = POSES[pose]
    st = _STATE.setdefault(key, {s: tgt[s] for s in ("L", "R")})
    if walk is not None and pose == "idle":
        sw = math.sin(walk) * 70
        tgt = {"L": (-40 + sw, -420, "out"), "R": (40 - sw, -420, "out")}
    for s in ("L", "R"):
        hx, hy = st[s][:2]
        tx, ty = tgt[s][:2]
        st[s] = (hx + (tx - hx) * 0.3, hy + (ty - hy) * 0.3, tgt[s][2] if len(tgt[s]) > 2 else "low")
    import backgrounds as _bg
    mouth = _bg.CLOCK.get("mouth", 0.0) if _bg.CLOCK.get("speaker") == key else 0.0
    blink = 1.0 if (t + hash(key) % 7) % 4.0 < 0.1 else 0.0
    draw_figure(cr, look, x, y, scale, facing,
                dict(hands=st, emotion=emotion, mouth_open=mouth, blink=blink, look=look_dir, prop=prop, walk=walk),
                t, sit=sit, shiver=shiver)
