"""What if the internet shut down for a week?

Quellen: Microsoft/TechTarget (CrowdStrike-Ausfall 19.7.2024, ~8,5 Mio. Geräte), Parametrix ($5,4 Mrd. Schaden Fortune 500),
Delta (~$500 Mio.), Federal Reserve 2024 (Kartenzahlungen brauchen meist Internet), Spanien-Blackout 2025 (Geldautomaten aus),
Niederlande Mai 2024 (Kartenausfall -> Ansturm auf Geldautomaten).
"""
import math
import random

import cairo
import anim
import explainer_kit as K
from backgrounds import rgb, _text, fill_stroke
from stickman import Look, stroke_black, rrect

GAP = 0.22
HOOK = ["What if the internet", "shut down for a week?"]
HOOK_UNTIL = None
CAPTIONS = True

CYAN = (0.15, 0.80, 0.91)
MAX = Look(shirt=CYAN)
BARISTA = Look(shirt=(0.45, 0.28, 0.16), ponytail=True, lashes=True, apron=True)
CHARS = {
    "N": dict(voice="en-US-ChristopherNeural", el_voice="nPczCjzI2devNBz1zQrb", look=Look()),  # Brian
    "M": dict(voice="en-US-AndrewNeural", el_voice="bIHbv24MWmeRgasZH58o", look=MAX),  # Will
    "B": dict(voice="en-US-EmmaMultilingualNeural", el_voice="cgSgspJ2msm6clMCkdW9", look=BARISTA),  # Jessica
}
BG = K.BGS
PAL = [(0.95, 0.45, 0.45), (0.45, 0.75, 0.95), (0.98, 0.80, 0.25), (0.55, 0.85, 0.50), (0.75, 0.55, 0.95)]


def stamp(cr, s):
    K.pill(cr, s, y=430)


def sc_phone(cr, t):
    lt = K.lt()
    stamp(cr, "MINUTE 1")
    random.seed(3)
    for k in range(4):
        x = 150 + k * 260
        lk = Look(shirt=PAL[k], ponytail=k % 2 == 1, lashes=k % 2 == 1)
        looking_up = lt > 2.5 + k * 0.4
        anim.actor(cr, f"p{k}", lk, x, 1740, 0.8, 1 if k < 2 else -1, pose="idle" if looking_up else "film",
                   emotion="confused" if looking_up else "neutral", t=t, prop=None if looking_up else "phone",
                   look_dir=(0.5, -0.6) if looking_up else (0.9, 0.5))
    if lt > 1.5:
        K.phone(cr, 540, 1000, 1.1, "#F4F7FD", lambda c: K.no_signal(c, 0, 0, 0.9))
        K.label(cr, "No connection", 540, 1200, 40, rgb("#FF8A8A"))


def sc_cafe(cr, t):
    lt = K.lt()
    stamp(cr, "HOUR 1")
    anim.actor(cr, "B", BARISTA, 760, 1640, 0.95, -1, pose="explain" if lt > 2 else "idle", emotion="worried", t=t)
    anim.actor(cr, "M", MAX, 300, 1740, 1.0, 1, pose="phone" if lt < 2 else "shrug", emotion="neutral" if lt < 2 else "shocked",
               t=t, prop="phone" if lt < 2 else None)
    # Kartenterminal
    rrect(cr, 480, 1120, 120, 110, 14)
    fill_stroke(cr, rgb("#2B2F38"), 4)
    rrect(cr, 492, 1132, 96, 50, 6)
    cr.set_source_rgb(*(rgb("#E23B3B") if lt > 1.2 else rgb("#33C46A"))); cr.fill()
    if lt > 1.2:
        K.label(cr, "CARD DECLINED · OFFLINE", 540, 1060, 38, (1, 1, 1), (0.85, 0.15, 0.15, 0.95))
    if lt > 3.5:
        rrect(cr, 640, 860, 320, 90, 10)
        fill_stroke(cr, (1, 1, 1), 5)
        _text(cr, "CASH ONLY", 800, 922, 46, rgb("#B3261E"))


def sc_atm(cr, t):
    lt = K.lt()
    stamp(cr, "HOUR 3")
    K.label(cr, "OUT OF SERVICE", 540, 790, 34, rgb("#FF6B6B"), (0.05, 0.05, 0.08, 0.95))
    n = min(9, 2 + int(lt * 1.6))
    for k in range(n):
        x = 300 - k * 70 + (0 if k else 0)
        lk = Look(shirt=PAL[k % 5], ponytail=k % 3 == 1, lashes=k % 3 == 1)
        anim.actor(cr, f"q{k}", lk, 1000 - k * 95, 1760, 0.7, -1, pose="cross" if k % 2 else "hips",
                   emotion="annoyed" if k % 2 else "worried", t=t)


def sc_airport(cr, t):
    lt = K.lt()
    stamp(cr, "DAY 1")
    rrect(cr, 140, 700, 800, 420, 12)
    fill_stroke(cr, rgb("#15181F"), 7)
    _text(cr, "DEPARTURES", 540, 760, 36, rgb("#FFD45C"), font="DejaVu Sans Mono")
    flights = ["NYC  09:10", "LON  09:35", "TYO  10:05", "PAR  10:20", "DXB  10:45"]
    for k, f in enumerate(flights):
        y = 830 + k * 58
        _text(cr, f, 190, y, 32, (1, 1, 1), font="DejaVu Sans Mono", center=False)
        flip = lt > 0.8 + k * 0.5
        _text(cr, "CANCELLED" if flip else "ON TIME", 640, y, 32, rgb("#FF5A5A") if flip else rgb("#5BEA8B"),
              font="DejaVu Sans Mono", center=False)
    anim.actor(cr, "M", MAX, 540, 1760, 0.85, 1, pose="head" if lt > 3 else "idle", emotion="shocked" if lt > 3 else "neutral",
               t=t, look_dir=(0.3, -0.7))
    if lt > 3:
        K.label(cr, "2024: one bad update grounded thousands of flights", 540, 1210, 30)


def sc_shop(cr, t):
    lt = K.lt()
    stamp(cr, "DAY 3")
    random.seed(9)
    left = 1.0 - K.ease(lt / 5.0)
    for row in range(4):
        y = 640 + row * 230 + 120
        for k in range(16):
            if random.random() < left:
                cr.rectangle(100 + k * 56, y, 44, 60)
                fill_stroke(cr, PAL[(k + row) % 5], 3)
    anim.actor(cr, "M", MAX, 540, 1760, 0.85, 1, pose="shrug", emotion="worried", t=t)
    if lt > 2:
        K.label(cr, "Deliveries run on online orders", 540, 1210, 34)


def sc_offline(cr, t):
    lt = K.lt()
    stamp(cr, "DAY 5")
    # Brettspiel auf dem Tisch
    rrect(cr, 380, 1240, 320, 70, 10)
    fill_stroke(cr, rgb("#F2C230"), 4)
    for k in range(4):
        cr.arc(430 + k * 70, 1275, 14, 0, 2 * math.pi)
        fill_stroke(cr, PAL[k], 3)
    anim.actor(cr, "M", MAX, 260, 1740, 0.95, 1, pose="explain", emotion="happy", t=t)
    anim.actor(cr, "n1", Look(shirt=PAL[2], ponytail=True, lashes=True), 820, 1740, 0.95, -1,
               pose="shrug" if (lt % 2) < 1 else "explain", emotion="happy", t=t)
    K.label(cr, "People start talking again", 540, 780, 40)


def sc_back(cr, t):
    lt = K.lt()
    stamp(cr, "DAY 7")
    n = int(min(9999, (lt ** 3) * 120))
    shake = math.sin(lt * 60) * 6 if lt > 1 else 0

    def content(c):
        for k in range(min(5, int(lt * 2))):
            rrect(c, -52, -100 + k * 42, 104, 36, 8)
            c.set_source_rgb(*PAL[k]); c.fill()
    K.phone(cr, 540 + shake, 1000, 1.3, "#F4F7FD", content)
    cr.arc(620 + shake, 850, 44, 0, 2 * math.pi)
    cr.set_source_rgb(*rgb("#FF3B30")); cr.fill()
    _text(cr, str(n), 620 + shake, 864, 30 if n < 1000 else 24, (1, 1, 1))
    anim.actor(cr, "M", MAX, 260, 1760, 0.9, 1, pose="panic" if lt > 2 else "idle", emotion="shocked", t=t)


def sc_cost(cr, t):
    lt = K.lt()
    K.label(cr, "July 19, 2024", 540, 560, 44, rgb("#FFD45C"))
    random.seed(5)
    n = min(60, int(lt * 18))
    for k in range(n):
        x = 160 + (k % 10) * 85
        y = 820 + (k // 10) * 70
        rrect(cr, x - 30, y - 22, 60, 44, 6)
        fill_stroke(cr, rgb("#3D7BFF"), 3)
        _text(cr, ":(", x, y + 10, 22, (1, 1, 1))
    if lt > 2:
        K.label(cr, "~8.5 million computers crashed", 540, 1240, 40)
    if lt > 4:
        K.label(cr, "$5.4 billion lost in one day", 540, 1320, 44, rgb("#5BEA8B"))


SHOTS = {
    "phone": dict(bg="street", overlays=[sc_phone], layers=[]),
    "cafe": dict(bg="cafe", overlays=[sc_cafe], layers=[]),
    "atm": dict(bg="bank", overlays=[sc_atm], layers=[]),
    "airport": dict(bg="airport", overlays=[sc_airport], layers=[]),
    "cost": dict(bg="dark", overlays=[sc_cost], layers=[]),
    "shop": dict(bg="shop", overlays=[sc_shop], layers=[]),
    "offline": dict(bg="living", overlays=[sc_offline], layers=[]),
    "back": dict(bg="dark", overlays=[sc_back], layers=[]),
}

SCRIPT = [
    dict(shot="phone", s="N", t="Imagine one morning, the entire internet just stops. Everywhere. For a whole week.",
         say="[mysterious] Imagine one morning, the entire internet just stops. Everywhere. For a whole week."),
    dict(s="N", t="At first, people think it's just their Wi-Fi.", say="[amused] At first, people think it's just their Wi-Fi.", gap=0.3),
    dict(shot="cafe", s="M", t="One latte, please. I'll pay by phone.", say="[cheerful] One latte, please. I'll pay by phone."),
    dict(s="B", t="Sorry. Card machines are down. Cash only.", say="[apologetic] Sorry. Card machines are down. Cash only."),
    dict(s="N", t="Most card payments need an internet connection. Suddenly, your phone wallet is useless.",
         say="[explaining] Most card payments need an internet connection. Suddenly, your phone wallet is useless.", gap=0.3),
    dict(shot="atm", s="N", t="So everyone rushes to the ATM. But many ATMs need the network too.",
         say="[tense] So everyone rushes to the ATM. But many ATMs need the network too."),
    dict(s="N", t="When Spain had a massive blackout in 2025, ATMs and card terminals simply stopped working.",
         say="[serious] When Spain had a massive blackout in 2025, ATMs and card terminals simply stopped working.", gap=0.3),
    dict(shot="airport", s="N", t="Airports grind to a halt. Booking, check in and flight planning all run online.",
         say="[serious] Airports grind to a halt. Booking, check in and flight planning all run online."),
    dict(shot="cost", s="N", t="We've had a tiny preview. In July 2024, one faulty software update crashed about eight and a half million computers.",
         say="[dramatic] We've had a tiny preview. In July 2024, one faulty software update crashed about eight and a half million computers."),
    dict(s="N", t="Fortune 500 companies lost an estimated five point four billion dollars. In one day.",
         say="[impressed] Fortune 500 companies lost an estimated five point four billion dollars. In one day.", gap=0.3),
    dict(shot="shop", s="N", t="By day three, supermarket shelves start emptying. Orders, deliveries and stock all run through online systems.",
         say="[ominous] By day three, supermarket shelves start emptying. Orders, deliveries and stock all run through online systems."),
    dict(s="M", t="Does anyone still know how to read a paper map?", say="[worried] Does anyone still know how to read a paper map?",
         gap=0.3),
    dict(shot="offline", s="N", t="But something unexpected happens. People start talking to their neighbors again. Board games make a comeback.",
         say="[warm] But something unexpected happens. People start talking to their neighbors again. Board games make a comeback."),
    dict(shot="back", s="N", t="Then, on day seven, the internet comes back.", say="[upbeat] Then, on day seven, the internet comes back."),
    dict(s="M", t="Nine thousand notifications? Can we turn it off again?", say="[overwhelmed] Nine thousand notifications? Can we turn it off again?",
         gap=0.8),
]
