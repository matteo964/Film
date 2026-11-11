"""What happens if you don't sleep for 11 days? (Randy Gardner, 1963/64, 264 Stunden)

Quellen: NPR 2024 (60. Jahrestag), Guinness World Records 2023 (Rekord wird nicht mehr überwacht),
Discover Magazine, scienceblog (Erholung ~14 h 40 min), Dawson & Reid 1997 (24 h wach ≈ 0,10 ‰ BAK).
"""
import math
import random

import cairo
import anim
import explainer_kit as K
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, stroke_black, rrect

GAP = 0.22
HOOK = ["What happens if you don't", "sleep for 11 days?"]
HOOK_UNTIL = None
CAPTIONS = True

CYAN = (0.15, 0.80, 0.91)
RANDY = Look(shirt=CYAN)
CHARS = {
    "N": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=Look()),  # Brian
    "R": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=RANDY),  # Will
}
BG = K.BGS


def hours(cr, h, y=620):
    K.label(cr, f"HOURS AWAKE: {int(h)}", 540, y, 46, rgb("#FFD45C"))


def bags(cr, x, y, s, strength):
    """Augenringe."""
    if strength <= 0:
        return
    for dx in (-3, 47):
        cr.save(); cr.translate(x + (22 + dx - 25) * s, y + (-770 + 20) * s); cr.scale(s, s)
        cr.arc(0, 0, 24, 0.2 * math.pi, 0.8 * math.pi)
        cr.set_source_rgba(0.35, 0.25, 0.45, 0.8 * strength); cr.set_line_width(7); cr.stroke()
        cr.restore()


def mugs(cr, n, x=820, y=1540):
    for k in range(n):
        cx = x + (k % 4) * 52 - 80
        cy = y - (k // 4) * 70
        rrect(cr, cx - 20, cy - 55, 40, 55, 6)
        fill_stroke(cr, (1, 1, 1), 3)
        cr.arc(cx + 24, cy - 28, 10, -1.4, 1.4)
        stroke_black(cr, 4)


# ------------------------------------------------------------------ Szenen
def sc_intro(cr, t):
    h = min(1.0, K.lt() / 6.0) * 0
    hours(cr, 0)
    anim.actor(cr, "R", RANDY, 420, 1740, 1.0, 1, pose="mug", emotion="happy", t=t, prop="mug")


def sc_day1(cr, t):
    lt = K.lt()
    hours(cr, 24 + min(lt, 6) * 2)
    x = -150 + lt * 140
    walking = x < 520
    xx = min(x, 520)
    anim.actor(cr, "R", RANDY, xx, 1740, 1.0, 1, pose="idle" if walking else "mug", emotion="annoyed", t=t,
               walk=(lt * 7) if walking else None, prop=None if walking else "mug")
    bags(cr, xx, 1740, 1.0, 0.4)
    mugs(cr, 3 + int(lt / 2))
    if lt > 3:
        K.label(cr, "24 hours awake ≈ legally drunk", 540, 760, 36)


def sc_day2(cr, t):
    lt = K.lt()
    hours(cr, 48 + min(lt, 6) * 2)
    off = 18 + math.sin(lt * 3) * 10
    cr.push_group()
    anim.actor(cr, "Rg", RANDY, 540 + off, 1740, 1.0, 1, pose="mug", emotion="annoyed", t=t, prop="mug")
    cr.pop_group_to_source()
    cr.paint_with_alpha(0.35)
    drop = lt > 3.2
    anim.actor(cr, "R", RANDY, 540, 1740, 1.0, 1, pose="shrug" if drop else "mug", emotion="shocked" if drop else "annoyed",
               t=t, prop=None if drop else "mug")
    bags(cr, 540, 1740, 1.0, 0.6)
    if drop:
        fy = min(1530, 1150 + (lt - 3.2) ** 2 * 900)
        rrect(cr, 660, fy - 55, 40, 55, 6)
        fill_stroke(cr, (1, 1, 1), 3)
        if fy >= 1530:
            cr.set_source_rgba(0.45, 0.28, 0.12, 0.9)
            cr.save(); cr.translate(690, 1555); cr.scale(90, 14); cr.arc(0, 0, 1, 0, 2 * math.pi); cr.restore()
            cr.fill()
    K.label(cr, "blurry vision · clumsy hands", 540, 760, 36)


def sc_day3(cr, t):
    lt = K.lt()
    hours(cr, 72 + min(lt, 6) * 2)
    emo = ["angry", "sad", "angry", "happy", "sad", "angry"][int(lt / 0.9) % 6]
    pose = {"angry": "point", "sad": "idle", "happy": "shrug"}[emo]
    anim.actor(cr, "R", RANDY, 540, 1740, 1.0, 1, pose=pose, emotion=emo, t=t)
    bags(cr, 540, 1740, 1.0, 0.8)
    K.label(cr, "irritable · nauseous · forgetful", 540, 760, 36)


def sc_day4(cr, t):
    lt = K.lt()
    cr.set_source_rgba(0.45, 0.1, 0.6, 0.35); cr.paint()
    hours(cr, 96 + min(lt, 6) * 2)
    # Laterne mit Gesicht
    cr.move_to(820, 1560); cr.line_to(820, 900); stroke_black(cr, 14)
    cr.arc(820, 860, 70, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#FFE58A"), 6)
    wink = (lt % 2.0) < 0.3
    cr.arc(795, 850, 9, 0, 2 * math.pi); cr.set_source_rgb(0, 0, 0); cr.fill()
    if wink:
        cr.move_to(835, 850); cr.line_to(860, 850); stroke_black(cr, 5)
    else:
        cr.arc(845, 850, 9, 0, 2 * math.pi); cr.set_source_rgb(0, 0, 0); cr.fill()
    cr.arc(820, 880, 22, 0.1 * math.pi, 0.9 * math.pi); stroke_black(cr, 5)
    random.seed(4)
    for k in range(7):
        x = random.uniform(100, 980); y = 800 + random.uniform(0, 500) + math.sin(lt * 2 + k) * 30
        cr.arc(x, y, random.uniform(14, 34), 0, 2 * math.pi)
        cr.set_source_rgba(*random.choice(((1, 0.4, 0.7), (0.4, 1, 0.8), (1, 0.9, 0.3))), 0.6); cr.fill()
    anim.actor(cr, "R", RANDY, 380, 1740, 1.0, 1, pose="stop", emotion="shocked", t=t)
    bags(cr, 380, 1740, 1.0, 1.0)
    K.label(cr, "Day 4: hallucinations", 540, 760, 38)


def sc_micro(cr, t):
    lt = K.lt()
    hours(cr, 150)
    asleep = 2.4 < lt < 4.6
    jolt = 4.6 <= lt < 5.0
    y = 1740 + (math.sin(lt * 1.5) * 8 if asleep else 0)
    anim.actor(cr, "R", RANDY, 540, y, 1.0, 1, pose="idle" if asleep else ("panic" if jolt else "explain"),
               emotion="asleep" if asleep else ("shocked" if jolt else "annoyed"), t=t, look_dir=(1.0, 0.6) if asleep else (1, 0.05))
    if asleep:
        # Augen zu: Lider über die Augen zeichnen
        K.label(cr, "MICROSLEEP", 540, 900, 60, rgb("#FFD45C"))
        K.zzz(cr, 650, 950, t)
    bags(cr, 540, y, 1.0, 1.0)


def sc_pinball(cr, t):
    lt = K.lt()
    hours(cr, 250)
    rrect(cr, 600, 900, 300, 660, 20)
    fill_stroke(cr, rgb("#7A5AF5"), 6)
    rrect(cr, 625, 930, 250, 220, 12)
    cr.set_source_rgb(*rgb("#0F1320")); cr.fill()
    win = (lt % 1.2) < 0.6
    _text(cr, "WIN!" if win else "x3", 750, 1060, 70, rgb("#FFD45C") if win else (1, 1, 1))
    cr.move_to(630, 1250); cr.line_to(870, 1180); stroke_black(cr, 6)
    cr.arc(700 + math.sin(lt * 5) * 80, 1300 + math.cos(lt * 4) * 60, 16, 0, 2 * math.pi)
    fill_stroke(cr, rgb("#D9D9D9"), 3)
    anim.actor(cr, "R", RANDY, 420, 1740, 1.0, 1, pose="desk" if not win else "panic", emotion="happy", t=t)
    bags(cr, 420, 1740, 1.0, 1.0)
    K.label(cr, "Day 11: still winning at pinball", 540, 760, 36)


def sc_sleep(cr, t):
    lt = K.lt()
    # schlafender Kopf auf dem Kissen
    K.head(cr, 280, 1270, 70, (0.96, 0.96, 0.96))
    for dx in (-25, 25):
        cr.arc(285 + dx, 1262, 16, 0.1 * math.pi, 0.9 * math.pi); stroke_black(cr, 5)
    cr.save()
    cr.move_to(330, 1300); cr.curve_to(400, 1270, 520, 1280, 570, 1330)
    cr.line_to(570, 1340); cr.line_to(330, 1340); cr.close_path()
    cr.set_source_rgb(*rgb("#7FA6FF")); cr.fill()
    cr.restore()
    K.zzz(cr, 330, 1200, t)
    hh = min(14, lt * 2.2)
    K.label(cr, f"SLEPT: {int(hh)}h {int((hh % 1) * 60):02d}m", 540, 760, 46, rgb("#5BEA8B"))


def sc_warning(cr, t):
    lt = K.lt()
    cx, cy = 540, 1000
    cr.move_to(cx - 120, cy - 180); cr.line_to(cx + 120, cy - 180); cr.curve_to(cx + 120, cy, cx + 40, cy + 40, cx, cy + 40)
    cr.curve_to(cx - 40, cy + 40, cx - 120, cy, cx - 120, cy - 180); cr.close_path()
    fill_stroke(cr, rgb("#F2C230"), 6)
    cr.rectangle(cx - 25, cy + 40, 50, 80); fill_stroke(cr, rgb("#F2C230"), 5)
    rrect(cr, cx - 110, cy + 120, 220, 50, 10); fill_stroke(cr, rgb("#7A5233"), 5)
    a = K.ease((lt - 1.0) * 2)
    if a > 0:
        cr.move_to(cx - 200, cy - 250); cr.line_to(cx + 200, cy + 230)
        cr.move_to(cx + 200, cy - 250); cr.line_to(cx - 200, cy + 230)
        cr.set_source_rgba(0.9, 0.2, 0.2, a); cr.set_line_width(26); cr.set_line_cap(cairo.LINE_CAP_ROUND); cr.stroke()
    K.label(cr, "Record no longer monitored", 540, 1330, 40)


def sc_bed(cr, t):
    anim.actor(cr, "R", RANDY, 760, 1740, 1.0, -1, pose="shrug", emotion="happy", t=t)


SHOTS = {
    "intro": dict(bg="bedroom", overlays=[sc_intro], layers=[]),
    "day1": dict(bg="street", overlays=[sc_day1], layers=[]),
    "day2": dict(bg="bedroom", overlays=[sc_day2], layers=[]),
    "day3": dict(bg="street", overlays=[sc_day3], layers=[]),
    "day4": dict(bg="street", overlays=[sc_day4], layers=[]),
    "micro": dict(bg="living", overlays=[sc_micro], layers=[]),
    "pinball": dict(bg="dark", overlays=[sc_pinball], layers=[]),
    "sleep": dict(bg="bedroom", overlays=[sc_sleep], layers=[]),
    "warning": dict(bg="dark", overlays=[sc_warning], layers=[]),
    "bed": dict(bg="bedroom", overlays=[sc_bed], layers=[]),
}

SCRIPT = [
    dict(shot="intro", s="N", t="In 1964, a seventeen year old named Randy Gardner tried to stay awake for eleven days. For a science fair.",
         say="[storytelling] In 1964, a seventeen year old named Randy Gardner tried to stay awake for eleven days. For a science fair."),
    dict(s="R", t="Eleven days without sleep? How hard can it be?", say="[confident] Eleven days without sleep? How hard can it be?",
         gap=0.4),
    dict(shot="day1", s="N", t="After just twenty four hours, your brain works about as badly as if you were legally drunk.",
         say="[serious] After just twenty four hours, your brain works about as badly as if you were legally drunk."),
    dict(s="R", t="I'm fine. I just need more coffee.", say="[grumpy] I'm fine. I just need more coffee.", gap=0.3),
    dict(shot="day2", s="N", t="On day two, focusing gets hard. Your vision gets blurry, and your hands get clumsy.",
         say="[explaining] On day two, focusing gets hard. Your vision gets blurry, and your hands get clumsy."),
    dict(s="R", t="Who moved my hand?", say="[confused] Who moved my hand?", gap=0.3),
    dict(shot="day3", s="N", t="By day three, his mood swings wildly. He's irritable, nauseous, and his memory starts slipping.",
         say="[serious] By day three, his mood swings wildly. He's irritable, nauseous, and his memory starts slipping."),
    dict(shot="day4", s="N", t="On day four, an observer reported hallucinations and delusions.",
         say="[ominous] On day four, an observer reported hallucinations and delusions."),
    dict(s="R", t="Did that street lamp just wink at me?", say="[freaked out] Did that street lamp just wink at me?", gap=0.3),
    dict(shot="micro", s="N", t="Then the brain starts taking things into its own hands. It forces tiny naps called microsleeps.",
         say="[intrigued] Then the brain starts taking things into its own hands. It forces tiny naps called microsleeps."),
    dict(s="R", t="Where was I? Oh, right.", say="[startled] Where was I? Oh... right.", gap=0.3),
    dict(shot="pinball", s="N", t="And yet, near the end, Randy kept beating a sleep scientist at pinball. Game after game.",
         say="[amused] And yet, near the end, Randy kept beating a sleep scientist at pinball. Game after game."),
    dict(shot="sleep", s="N", t="After two hundred sixty four hours, he finally slept. About fourteen hours. And woke up feeling surprisingly normal.",
         say="[relieved] After two hundred sixty four hours, he finally slept. About fourteen hours. And woke up feeling surprisingly normal."),
    dict(shot="warning", s="N", t="But don't try this. Guinness World Records stopped tracking this record, because it's too dangerous.",
         say="[serious warning] But don't try this. Guinness World Records stopped tracking this record, because it's too dangerous."),
    dict(shot="bed", s="R", t="Okay. I'm going to bed.", say="[sleepy] Okay. I'm going to bed.", gap=0.8),
]
