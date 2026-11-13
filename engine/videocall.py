"""Videocall-Oberfläche (Kachelraster, Bildschirmfreigabe, Chat) – Figuren lippensynchron über anim.actor."""
import math

import cairo
import anim
import backgrounds as bgm
from backgrounds import rgb, _text
from stickman import rrect

W, H = 1080, 1920
TOP, BOTTOM = 430, 1560          # Call-Bereich (oben Hook, unten Untertitel/Leiste)
TILE_BG = ["#3B4A5E", "#4E5D47", "#5E4A55", "#4A5568", "#5A5246", "#3F5560", "#55485E", "#46584E", "#5B4E44"]


def _ui_frame(cr):
    cr.set_source_rgb(*rgb("#1E2128"))
    cr.paint()
    rrect(cr, 0, TOP - 60, W, 50, 0)
    cr.set_source_rgb(*rgb("#2A2E37")); cr.fill()
    cr.arc(40, TOP - 35, 9, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#FF3B30")); cr.fill()
    _text(cr, "REC   ·   All-Hands Meeting   ·   142 participants", 62, TOP - 25, 24, (0.85, 0.87, 0.9), bold=False, center=False)
    # Leiste unten
    cr.rectangle(0, BOTTOM + 10, W, 90)
    cr.set_source_rgb(*rgb("#2A2E37")); cr.fill()
    for k, (lab, col) in enumerate((("Mute", "#C9D3E6"), ("Video", "#C9D3E6"), ("Share", "#5BEA8B"), ("Chat", "#C9D3E6"),
                                    ("Leave", "#FF6B6B"))):
        _text(cr, lab, 110 + k * 215, BOTTOM + 66, 26, rgb(col), bold=False)


def tile(cr, x, y, w, h, cid, look, name, idx, t, muted=True, emotion="neutral", pose="idle", cam_off=False, prop=None,
         look_dir=(0.15, 0.25)):
    speaking = bgm.CLOCK.get("speaker") == cid
    rrect(cr, x, y, w, h, 14)
    cr.set_source_rgb(*rgb(TILE_BG[idx % len(TILE_BG)])); cr.fill()
    cr.save()
    rrect(cr, x, y, w, h, 14); cr.clip()
    if cam_off:
        cr.arc(x + w / 2, y + h / 2, min(w, h) * 0.22, 0, 2 * math.pi)
        cr.set_source_rgb(*rgb("#7A8899")); cr.fill()
        _text(cr, name[0], x + w / 2, y + h / 2 + 18, 56, (1, 1, 1))
    else:
        # Hintergrund-Andeutung (Regal / Fenster)
        cr.rectangle(x + w * 0.62, y + h * 0.12, w * 0.3, h * 0.4)
        cr.set_source_rgba(1, 1, 1, 0.08); cr.fill()
        sc = h / 520.0
        anim.actor(cr, cid, look, x + w / 2, y + h * 0.5 + 770 * sc + 40 * sc, sc, 1, pose=pose, emotion=emotion, t=t,
                   look_dir=look_dir, prop=prop)
    cr.restore()
    rrect(cr, x + 10, y + h - 46, min(w - 20, 30 + len(name) * 15), 36, 8)
    cr.set_source_rgba(0, 0, 0, 0.55); cr.fill()
    _text(cr, name, x + 22, y + h - 20, 22, (1, 1, 1), bold=False, center=False)
    if muted:
        cr.arc(x + w - 30, y + h - 28, 14, 0, 2 * math.pi); cr.set_source_rgb(*rgb("#FF3B30")); cr.fill()
        cr.move_to(x + w - 38, y + h - 36); cr.line_to(x + w - 22, y + h - 20)
        cr.set_source_rgb(1, 1, 1); cr.set_line_width(3); cr.stroke()
    rrect(cr, x, y, w, h, 14)
    if speaking:
        cr.set_source_rgb(*rgb("#33E07A")); cr.set_line_width(7)
    else:
        cr.set_source_rgba(1, 1, 1, 0.08); cr.set_line_width(2)
    cr.stroke()


def chat(cr, msgs, x=600, y=TOP + 20, w=460, h=None, start=0.0, per=0.8):
    """msgs: Liste (name, text, farbe). Erscheinen nacheinander ab start (Shot-Zeit)."""
    lt = bgm.CLOCK["lt"]
    h = h or (BOTTOM - TOP - 40)
    rrect(cr, x, y, w, h, 14)
    cr.set_source_rgba(0.12, 0.13, 0.16, 0.96); cr.fill()
    _text(cr, "Chat", x + 24, y + 44, 28, (1, 1, 1), center=False)
    n = max(0, min(len(msgs), int((lt - start) / per) + 1)) if lt >= start else 0
    shown = msgs[:n][-9:]
    for k, (name, text, col) in enumerate(shown):
        yy = y + 90 + k * 108
        _text(cr, name, x + 24, yy, 22, rgb(col), center=False)
        rrect(cr, x + 20, yy + 10, w - 40, 62, 12)
        cr.set_source_rgba(1, 1, 1, 0.08); cr.fill()
        _text(cr, text, x + 32, yy + 52, 24 if w > 400 else 21, (1, 1, 1), bold=False, center=False)


def share_window(cr, kind, x=20, y=TOP + 20, w=None, h=None):
    w = w or (W - 40)
    h = h or (BOTTOM - TOP - 40)
    rrect(cr, x, y, w, h, 14)
    cr.set_source_rgb(1, 1, 1); cr.fill()
    rrect(cr, x, y, w, 56, 14)
    cr.set_source_rgb(*rgb("#E9EDF2")); cr.fill()
    for k, c in enumerate(("#FF5F57", "#FEBC2E", "#28C840")):
        cr.arc(x + 30 + k * 26, y + 28, 8, 0, 2 * math.pi); cr.set_source_rgb(*rgb(c)); cr.fill()
    title = {"slides": "Q4_Update.pptx", "yacht": "luxemarine.com – Order Confirmation",
             "bonus": "EXEC_COMP_FINAL_dont_share.xlsx", "budget": "Raises_Budget.xlsx"}[kind]
    _text(cr, title, x + 120, y + 37, 22, rgb("#3B4555"), bold=False, center=False)
    cx = x + w / 2
    if kind == "slides":
        _text(cr, "A TOUGH YEAR", cx, y + 170, 54, rgb("#B3261E"))
        cr.move_to(x + 120, y + 280); cr.line_to(x + 300, y + 320); cr.line_to(x + 480, y + 300); cr.line_to(x + 700, y + 420)
        cr.line_to(x + w - 120, y + 460)
        cr.set_source_rgb(*rgb("#E23B3B")); cr.set_line_width(10); cr.stroke()
        _text(cr, "No raises · No bonuses", cx, y + 560, 40, rgb("#1B1F27"))
        _text(cr, "We all need to make sacrifices.", cx, y + 620, 32, rgb("#6E7A88"), bold=False)
        _text(cr, "(Office coffee: now $2)", cx, y + 680, 28, rgb("#6E7A88"), bold=False)
    elif kind == "yacht":
        g = cairo.LinearGradient(0, y + 56, 0, y + 520)
        g.add_color_stop_rgb(0, *rgb("#8FD0F5")); g.add_color_stop_rgb(1, *rgb("#2F8FD1"))
        cr.rectangle(x, y + 56, w, 460); cr.set_source(g); cr.fill()
        cr.move_to(x + 160, y + 380); cr.line_to(x + w - 160, y + 380); cr.line_to(x + w - 230, y + 450); cr.line_to(x + 230, y + 450)
        cr.close_path(); cr.set_source_rgb(1, 1, 1); cr.fill_preserve(); cr.set_source_rgb(*rgb("#1B1F27")); cr.set_line_width(4); cr.stroke()
        cr.rectangle(x + 330, y + 310, 340, 70); cr.set_source_rgb(1, 1, 1); cr.fill_preserve(); cr.stroke()
        for k in range(5):
            cr.rectangle(x + 350 + k * 64, y + 330, 40, 26); cr.set_source_rgb(*rgb("#2B3A55")); cr.fill()
        _text(cr, "ORDER CONFIRMED", cx, y + 600, 46, rgb("#1F8A47"))
        _text(cr, "Model: Serenity 120  ·  $1,800,000", cx, y + 660, 34, rgb("#1B1F27"))
        _text(cr, "Name on hull: \"BONUS SEASON\"", cx, y + 720, 30, rgb("#6E7A88"), bold=False)
        _text(cr, "Buyer: Gordon Pratt, CEO", cx, y + 780, 30, rgb("#6E7A88"), bold=False)
    elif kind in ("bonus", "budget"):
        rows = [("Employee raises (140 people)", "$1,900,000", "FROZEN"),
                ("Executive bonus – G. Pratt", "$2,400,000", "APPROVED"),
                ("Source of bonus funds", "Raise pool", "")]
        if kind == "budget":
            rows = [("Raises for all 140 employees", "$1,900,000", ""), ("CEO bonus", "$2,400,000", ""),
                    ("Left over after raises", "$500,000", "")]
        _text(cr, "FY2026 COMPENSATION", cx, y + 150, 44, rgb("#1B1F27"))
        for k, (a, b, c) in enumerate(rows):
            yy = y + 240 + k * 130
            cr.rectangle(x + 40, yy, w - 80, 110)
            cr.set_source_rgb(*(rgb("#FFF4D6") if k == 1 else rgb("#F4F6F8"))); cr.fill()
            _text(cr, a, x + 70, yy + 48, 30, rgb("#1B1F27"), center=False)
            _text(cr, b, x + 70, yy + 92, 34, rgb("#1F3B63"), center=False)
            if c:
                _text(cr, c, x + w - 200, yy + 72, 30, rgb("#E23B3B") if c == "FROZEN" else rgb("#1F8A47"), center=False)
