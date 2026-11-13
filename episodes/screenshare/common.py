"""Gemeinsame Besetzung/Sets: "Your boss cancels everyone's raise... then accidentally shares his screen"."""
import cairo
import backgrounds as bgm
import backgrounds_v2 as B
import explainer_kit as K
import videocall as VC
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, rrect

GAP = 0.15
HOOK_BASE = ["POV: Your boss cancels everyone's raise...", "then accidentally shares his screen"]
CAPTIONS = True
CAPTION_STYLE = "highlight"

SKIN = (0.95, 0.88, 0.78)
PRIYA = Look(shirt=(0.40, 0.35, 0.75), skin=(0.72, 0.53, 0.40), iris=(0.22, 0.14, 0.08), hair="long",
             hair_color=(0.08, 0.06, 0.06), outfit="blouse", shoes=True, lashes=True)
GORDON = Look(shirt=(0.22, 0.24, 0.30), skin=(0.96, 0.82, 0.70), iris=(0.30, 0.50, 0.75), hair="sidepart",
              hair_color=(0.88, 0.72, 0.40), outfit="suit", tie_color=(0.85, 0.20, 0.25), shoes=True)
HELEN = Look(shirt=(0.15, 0.40, 0.45), skin=SKIN, iris=(0.35, 0.30, 0.20), hair="updo", hair_color=(0.30, 0.22, 0.18),
             outfit="suit", tie_color=(0.95, 0.95, 0.95), shoes=True, lashes=True, glasses=True)
ADEYEMI = Look(shirt=(0.55, 0.20, 0.30), skin=(0.45, 0.30, 0.22), iris=(0.22, 0.14, 0.08), hair="curly",
               hair_color=(0.75, 0.75, 0.78), outfit="blouse", shoes=True, lashes=True)
MARCUS = Look(shirt=(0.25, 0.60, 0.45), skin=(0.55, 0.38, 0.28), iris=(0.2, 0.12, 0.08), hair="buzz", hair_color=(0.08, 0.06, 0.06),
              outfit="hoodie", shoes=True)
ANNA = Look(shirt=(0.95, 0.70, 0.30), skin=SKIN, iris=(0.30, 0.50, 0.30), hair="bob", hair_color=(0.92, 0.80, 0.50),
            outfit="blouse", shoes=True, lashes=True)
TOM = Look(shirt=(0.70, 0.30, 0.30), skin=SKIN, iris=(0.30, 0.45, 0.70), hair="spiky", hair_color=(0.75, 0.35, 0.15),
           outfit="blouse", shoes=True, glasses=True)

CHARS = {
    "P": dict(voice="en-US-MichelleNeural", el_voice="EXAVITQu4vr4xnSDxMaL", look=PRIYA),       # Sarah
    "G": dict(voice="en-US-ChristopherNeural", el_voice="N2lVS1w4EtoT3dr4eOWO", look=GORDON),   # Callum
    "H": dict(voice="en-US-AriaNeural", el_voice="Xb7hH8MSUJpSbSDYk0k2", look=HELEN),           # Alice
    "A": dict(voice="en-US-MichelleNeural", el_voice="hpp4J3VqNfWAUOO0d1Us", look=ADEYEMI),     # Bella
    "T": dict(voice="en-US-AndrewNeural", el_voice="TX3LPaxmHKxFdv7VOQHJ", look=TOM),           # Liam
    "M": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=MARCUS),        # Will
    "N": dict(voice="en-US-AvaNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=ANNA),             # Jessica
}
NAMES = {"G": "Gordon Pratt (CEO)", "P": "Priya Nair", "H": "Helen Cho (CFO)", "M": "Marcus", "N": "Anna", "T": "Tom",
         "A": "R. Adeyemi (Board)"}


def _st(cid):
    emo = bgm.CLOCK.get("emo", {}).get(cid, "neutral")
    pose = bgm.CLOCK.get("pose", {}).get(cid, "idle")
    if isinstance(pose, list):
        pose = pose[int(bgm.CLOCK.get("line_t", 0) / 1.1) % len(pose)] if bgm.CLOCK.get("speaker") == cid else pose[0]
    return emo, pose, bgm.CLOCK.get("prop", {}).get(cid)


def _tile(cr, t, cid, x, y, w, h, idx, muted=None):
    emo, pose, prop = _st(cid)
    speaking = bgm.CLOCK.get("speaker") == cid
    VC.tile(cr, x, y, w, h, cid, CHARS[cid]["look"], NAMES[cid], idx, t, muted=not speaking if muted is None else muted,
            emotion=emo, pose=pose, prop=prop)


GRID = ["G", "P", "H", "M", "N", "T"]


def grid(cr, t):
    VC._ui_frame(cr)
    tw, th = 510, 350
    for i, cid in enumerate(GRID):
        x = 20 + (i % 2) * (tw + 20)
        y = VC.TOP + 10 + (i // 2) * (th + 20)
        _tile(cr, t, cid, x, y, tw, th, i)


def speaker(cid):
    def fn(cr, t):
        VC._ui_frame(cr)
        _tile(cr, t, cid, 20, VC.TOP + 10, 1040, 760, GRID.index(cid) if cid in GRID else 6)
        small = [c for c in GRID if c != cid][:3]
        for k, c in enumerate(small):
            _tile(cr, t, c, 20 + k * 350, VC.TOP + 790, 340, 300, GRID.index(c))
    return fn


def share(kind, msgs=None, start=0.0):
    def fn(cr, t):
        VC._ui_frame(cr)
        if msgs:
            k = 720 / 1040
            cr.save(); cr.translate(20, VC.TOP + 20); cr.scale(k, k)
            VC.share_window(cr, kind, x=0, y=0, w=1040, h=1090)
            cr.restore()
            VC.chat(cr, msgs, x=755, w=310, start=start)
            _tile(cr, t, "G", 30, VC.BOTTOM - 260, 300, 230, 0)
        else:
            VC.share_window(cr, kind)
            _tile(cr, t, "G", W_ - 330, VC.BOTTOM - 260, 300, 230, 0)
    return fn


W_ = 1080

CHAT_SLIDES = [("Marcus", "record revenue though??", "#7FB2FF"), ("Anna", "coffee is $2 now?!", "#FFB36B")]
CHAT_YACHT = [("Tom", "is that... a yacht?", "#FF8A8A"), ("Anna", "BONUS SEASON lmao", "#FFB36B"),
              ("Marcus", "1.8 MILLION??", "#7FB2FF"), ("Tom", "screenshot screenshot", "#FF8A8A"),
              ("Anna", "he doesn't know", "#FFB36B"), ("Marcus", "someone tell him", "#7FB2FF")]
CHAT_BONUS = [("Marcus", "FROM THE RAISE POOL", "#7FB2FF"), ("Tom", "our raises = his bonus", "#FF8A8A"),
              ("Anna", "sacrifices huh", "#FFB36B"), ("Helen Cho (CFO)", "Gordon. Stop sharing.", "#5BEA8B"),
              ("Tom", "he still doesn't know", "#FF8A8A")]


def email_popup(cr, t):
    lt = bgm.CLOCK["lt"]
    if lt < 0.6:
        return
    x, y, w, h = 90, 760, 900, 380
    rrect(cr, x, y, w, h, 20)
    cr.set_source_rgb(1, 1, 1); cr.fill_preserve(); cr.set_source_rgba(0, 0, 0, 0.3); cr.set_line_width(4); cr.stroke()
    rrect(cr, x, y, w, 70, 20); cr.set_source_rgb(*rgb("#B3261E")); cr.fill()
    _text(cr, "URGENT · Board of Directors", x + 40, y + 46, 30, (1, 1, 1), center=False)
    _text(cr, "Emergency board meeting – today 12:00", x + 40, y + 140, 34, rgb("#1B1F27"), center=False)
    _text(cr, "Agenda: Executive compensation", x + 40, y + 200, 30, rgb("#3B4555"), bold=False, center=False)
    _text(cr, "Attendees: G. Pratt, H. Cho, P. Nair", x + 40, y + 250, 30, rgb("#3B4555"), bold=False, center=False)
    _text(cr, "Ref: All-Hands recording, 10:42 AM", x + 40, y + 300, 26, rgb("#6E7A88"), bold=False, center=False)


def boardroom():
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1080, 1920)
    cr = cairo.Context(s)
    B.room(cr, rgb("#2F3B4C"), rgb("#7D6B5D"), tiles="wood")
    B.window_city(cr, 840, 470, 220, 640)
    rrect(cr, 90, 450, 700, 470, 12)
    fill_stroke(cr, rgb("#1B1F27"), 8)
    cr.save(); cr.translate(108, 468); cr.scale(664 / 1040, 434 / 1090)
    VC.share_window(cr, "budget", x=0, y=0, w=1040, h=1090)
    cr.restore()
    rrect(cr, 60, 1300, 960, 44, 12)
    fill_stroke(cr, rgb("#3A2E26"), 5)
    s.flush()
    return s


BG = {"call": K.BGS["dark"], "office": B.boss_office, "board": boardroom}

Y1, S1 = 1700, 1.3
Y2, S2 = 1740, 1.0


def one(b, cid, x=540, facing=1, front=None, opts=None, after=None):
    d = dict(bg=b, layers=[("char", cid, x, Y1, S1, facing, opts or {})] + ([("fn", front)] if front else []))
    if after:
        d["front"] = after
    return d


def two(b, left, right):
    return dict(bg=b, layers=[("char", left, 300, Y2, S2, 1), ("char", right, 780, Y2, S2, -1)])


def three(b, a, m, c, fm=-1):
    return dict(bg=b, layers=[("char", a, 210, Y2, 0.9, 1), ("char", m, 545, Y2, 0.9, fm), ("char", c, 875, Y2, 0.9, -1)])


SHOTS = {
    "grid": dict(bg="call", overlays=[grid], layers=[]),
    "spk_G": dict(bg="call", overlays=[speaker("G")], layers=[]),
    "spk_P": dict(bg="call", overlays=[speaker("P")], layers=[]),
    "spk_H": dict(bg="call", overlays=[speaker("H")], layers=[]),
    "spk_T": dict(bg="call", overlays=[speaker("T")], layers=[]),
    "share_slides": dict(bg="call", overlays=[share("slides", CHAT_SLIDES, 1.0)], layers=[]),
    "share_yacht": dict(bg="call", overlays=[share("yacht", CHAT_YACHT, 0.6)], layers=[]),
    "share_bonus": dict(bg="call", overlays=[share("bonus", CHAT_BONUS, 0.4)], layers=[]),
    "office_G": one("office", "G", 540, 1, front=B.boss_desk, opts=dict(hide_legs=True)),
    "office_P": one("office", "P", 600, -1),
    "office_GP": dict(bg="office", layers=[("char", "G", 330, 1720, 1.0, 1, dict(hide_legs=True)), ("fn", B.boss_desk),
                                           ("char", "P", 820, 1760, 1.0, -1)]),
    "office_P_mail": one("office", "P", 600, -1, after=[email_popup]),
    "board_A": one("board", "A", 880, -1),
    "board_G": one("board", "G", 880, -1),
    "board_P": one("board", "P", 880, -1),
    "board_H": one("board", "H", 880, -1),
    "board_GA": two("board", "G", "A"),
    "board_PA": two("board", "P", "A"),
    "board_GPA": three("board", "G", "P", "A"),
    "board_GHA": three("board", "G", "H", "A"),
}
