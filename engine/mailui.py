"""E-Mail-Programm-Oberfläche (Schreiben mit Tipp-Animation, Senden, Postfach-Flut, Rückruf-Dialog)."""
import math

import backgrounds as bgm
from backgrounds import rgb, _text
from stickman import rrect

W = 1080
X0, Y0, X1, Y1 = 20, 430, 1060, 1560


def frame(cr, title="Outlook – Martin Reed"):
    cr.set_source_rgb(*rgb("#E9EDF2")); cr.paint()
    cr.rectangle(0, Y0 - 60, W, 56); cr.set_source_rgb(*rgb("#0F6CBD")); cr.fill()
    _text(cr, title, 30, Y0 - 22, 26, (1, 1, 1), center=False)
    # Seitenleiste
    cr.rectangle(0, Y0 - 4, 170, Y1 - Y0 + 120); cr.set_source_rgb(*rgb("#F4F6F8")); cr.fill()
    for k, (lab, n) in enumerate((("Inbox", ""), ("Sent", ""), ("Drafts", ""), ("Deleted", ""))):
        _text(cr, lab, 24, Y0 + 50 + k * 60, 24, rgb("#3B4555"), bold=(k == 0), center=False)


def _wrap(cr, text, width, size):
    import cairo
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(size)
    lines, cur = [], ""
    for para in text.split("\n"):
        cur = ""
        for w in para.split(" "):
            test = (cur + " " + w).strip()
            if cr.text_extents(test).x_advance > width and cur:
                lines.append(cur); cur = w
            else:
                cur = test
        lines.append(cur)
    return lines


def compose(cr, to, subject, body, typed=1.0, hover_reply_all=False, highlight_to=False, sent=False):
    frame(cr)
    x, y, w = 190, Y0 + 10, 860
    rrect(cr, x, y, w, Y1 - Y0 - 20, 12); cr.set_source_rgb(1, 1, 1); cr.fill()
    # Toolbar
    for k, (lab, col) in enumerate((("Send", "#0F6CBD"), ("Reply", "#3B4555"), ("Reply All", "#3B4555"), ("Forward", "#3B4555"))):
        bx = x + 20 + k * 205
        rrect(cr, bx, y + 18, 190, 54, 10)
        hl = (lab == "Reply All" and hover_reply_all)
        cr.set_source_rgb(*(rgb("#FFE14D") if hl else (rgb("#0F6CBD") if lab == "Send" else rgb("#EEF2F6")))); cr.fill()
        _text(cr, lab, bx + 95, y + 55, 26, (1, 1, 1) if lab == "Send" else rgb(col), bold=True)
    # Felder
    _text(cr, "To:", x + 24, y + 130, 28, rgb("#6E7A88"), center=False)
    if highlight_to:
        rrect(cr, x + 80, y + 96, w - 110, 48, 8); cr.set_source_rgb(*rgb("#FFD6D6")); cr.fill()
    _text(cr, to, x + 90, y + 130, 28, rgb("#B3261E") if highlight_to else rgb("#1B1F27"), center=False)
    cr.move_to(x + 20, y + 156); cr.line_to(x + w - 20, y + 156)
    cr.set_source_rgb(*rgb("#E1E5EA")); cr.set_line_width(2); cr.stroke()
    _text(cr, "Subject:", x + 24, y + 200, 28, rgb("#6E7A88"), center=False)
    _text(cr, subject, x + 150, y + 200, 28, rgb("#1B1F27"), center=False)
    cr.move_to(x + 20, y + 226); cr.line_to(x + w - 20, y + 226); cr.stroke()
    n = int(len(body) * max(0.0, min(1.0, typed)))
    lines = _wrap(cr, body[:n], w - 70, 30)
    for k, ln in enumerate(lines[:16]):
        _text(cr, ln, x + 30, y + 280 + k * 46, 30, rgb("#1B1F27"), bold=False, center=False)
    if typed < 1.0 and int(bgm.CLOCK["t"] * 2) % 2 == 0 and lines:
        import cairo
        cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL); cr.set_font_size(30)
        cx = x + 30 + cr.text_extents(lines[min(len(lines), 16) - 1]).x_advance + 4
        cr.rectangle(cx, y + 252 + (min(len(lines), 16) - 1) * 46, 3, 36); cr.set_source_rgb(0, 0, 0); cr.fill()
    if sent:
        rrect(cr, 260, Y1 - 160, 720, 110, 18)
        cr.set_source_rgb(*rgb("#1B1F27")); cr.fill()
        _text(cr, "Message sent to 312 recipients", 620, Y1 - 92, 34, (1, 1, 1))


def inbox(cr, mails, start=0.0, per=0.7, counter_label=None):
    """mails: Liste (absender, betreff, vorschau, rot?) – erscheinen nacheinander von oben."""
    frame(cr)
    lt = bgm.CLOCK["lt"]
    x, y, w = 190, Y0 + 10, 860
    rrect(cr, x, y, w, Y1 - Y0 - 20, 12); cr.set_source_rgb(1, 1, 1); cr.fill()
    n = max(0, min(len(mails), int((lt - start) / per) + 1)) if lt >= start else 0
    shown = list(reversed(mails[:n]))[:8]
    for k, (frm, subj, prev, hot) in enumerate(shown):
        yy = y + 20 + k * 132
        rrect(cr, x + 14, yy, w - 28, 118, 10)
        cr.set_source_rgb(*(rgb("#FFF1F1") if hot else (rgb("#EEF5FF") if k == 0 else rgb("#F7F9FB")))); cr.fill()
        cr.rectangle(x + 14, yy, 8, 118); cr.set_source_rgb(*(rgb("#E23B3B") if hot else rgb("#0F6CBD"))); cr.fill()
        _text(cr, frm, x + 40, yy + 40, 28, rgb("#1B1F27"), center=False)
        _text(cr, subj, x + 40, yy + 76, 24, rgb("#0F6CBD") if not hot else rgb("#B3261E"), center=False)
        _text(cr, prev, x + 40, yy + 106, 22, rgb("#6E7A88"), bold=False, center=False)
    if counter_label:
        cnt = int(min(len(mails), n) * counter_label[1])
        rrect(cr, 30, Y0 + 300, 120, 70, 14); cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
        _text(cr, str(cnt), 90, Y0 + 348, 38, (1, 1, 1))
        _text(cr, counter_label[0], 90, Y0 + 400, 20, rgb("#B3261E"))


def dialog(cr, title, lines, color="#B3261E"):
    cr.set_source_rgba(0, 0, 0, 0.35); cr.rectangle(0, Y0 - 60, W, Y1 - Y0 + 160); cr.fill()
    x, y, w, h = 110, 780, 860, 420
    rrect(cr, x, y, w, h, 20); cr.set_source_rgb(1, 1, 1); cr.fill()
    rrect(cr, x, y, w, 80, 20); cr.set_source_rgb(*rgb(color)); cr.fill()
    _text(cr, title, x + w / 2, y + 54, 34, (1, 1, 1))
    for k, ln in enumerate(lines):
        _text(cr, ln, x + w / 2, y + 160 + k * 60, 32, rgb("#1B1F27"), bold=(k == 0))


def cold_open(cr, frm, to, subject, lines, marks, lt, read_max=287):
    """Großformatige E-Mail mit Textmarker-Animation (marks: Liste (zeile, start, ende) in Zeichen) und Lese-Zähler."""
    import cairo
    cr.set_source_rgb(*rgb("#11151C")); cr.paint()
    x, y, w = 40, 470, 1000
    rrect(cr, x, y, w, 960, 22); cr.set_source_rgb(1, 1, 1); cr.fill()
    rrect(cr, x, y, w, 70, 22); cr.set_source_rgb(*rgb("#0F6CBD")); cr.fill()
    cr.rectangle(x, y + 40, w, 30); cr.fill()
    _text(cr, "New message", x + 30, y + 48, 28, (1, 1, 1), center=False)
    _text(cr, "From:", x + 30, y + 130, 30, rgb("#6E7A88"), center=False)
    _text(cr, frm, x + 130, y + 130, 30, rgb("#1B1F27"), center=False)
    rrect(cr, x + 20, y + 152, w - 40, 56, 10); cr.set_source_rgb(*rgb("#FFD6D6")); cr.fill()
    _text(cr, "To:", x + 30, y + 192, 30, rgb("#B3261E"), center=False)
    _text(cr, to, x + 90, y + 192, 32, rgb("#B3261E"), center=False)
    _text(cr, "Subject: " + subject, x + 30, y + 260, 28, rgb("#3B4555"), center=False)
    cr.select_font_face("TikTok Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    size = 42
    cr.set_font_size(size)
    for k, ln in enumerate(lines):
        ly = y + 350 + k * 70
        for (li, a, b, t0) in marks:
            if li != k:
                continue
            f = max(0.0, min(1.0, (lt - t0) / 0.7))
            if f <= 0:
                continue
            xa = x + 40 + cr.text_extents(ln[:a]).x_advance
            xb = x + 40 + cr.text_extents(ln[:b]).x_advance
            cr.rectangle(xa - 4, ly - size * 0.85, (xb - xa + 8) * f, size * 1.1)
            cr.set_source_rgba(1.0, 0.9, 0.1, 0.85); cr.fill()
        cr.move_to(x + 40, ly)
        cr.set_source_rgb(*rgb("#1B1F27"))
        cr.show_text(ln)
    n = int(read_max * max(0.0, min(1.0, lt / 4.0)) ** 0.6)
    rrect(cr, x + w - 330, y + 222, 300, 60, 30); cr.set_source_rgb(*rgb("#E23B3B")); cr.fill()
    _text(cr, f"Read by {n}", x + w - 180, y + 263, 32, (1, 1, 1))


def stamp(cr, s):
    import cairo
    cr.select_font_face("Bebas Neue", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(110)
    e = cr.text_extents(s)
    cr.set_source_rgba(0, 0, 0, 0.6); cr.paint()
    cr.move_to((W - e.x_advance) / 2, 1000)
    cr.text_path(s)
    cr.set_source_rgb(0, 0, 0); cr.set_line_width(12); cr.stroke_preserve()
    cr.set_source_rgb(1, 1, 1); cr.fill()
