"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="logo_BN", s="B", t="Diane! Hi. It's just a tiny glitch. Nothing to worry about.",
         e={"B": "worried", "N": "angry"}, p={"B": "shrug", "N": "cross"}, say="[nervously] Diane! Hi. It's just a tiny glitch. Nothing to worry about."),
    dict(s="N", t="A glitch? The warehouse is threatening to walk out.", e={"N": "angry"}, p={"N": "point"}),
    dict(s="B", t="PayBot will fix it. Watch this.", e={"B": "smug"}, p={"B": "explain2"}),
    dict(s="B", t="PayBot. Send everyone's salary. Right now.", p={"B": "point"}, look={"B": "up"}, gap=0.4),
    dict(shot="error_BN", s="P", t="Hi Brad! I'm sorry, I can't access the bank account. Please contact the authorized signer. Dave Miller.",
         e={"B": "shocked", "N": "annoyed"}, p={"B": "idle"}, look={"B": "up", "N": "up"},
         say="[robotic, overly cheerful] Hi Brad! I'm sorry, I can't access the bank account. Please contact the authorized signer. Dave Miller.",
         sfx=[("ding", 0.0)]),
    dict(shot="error_BNK", s="K", t="The robot wants Dave.", e={"K": "smug"}, p={"K": "cross"}, look={"B": None, "N": None, "K": "away"}),
    dict(s="B", t="Then make me the signer. I'm the vice president!", e={"B": "angry"}, p={"B": "chest"}),
    dict(s="N", t="Only the bank can change that. It takes ten business days.", e={"N": "annoyed"}, p={"N": "explain"}),
    dict(s="K", t="Ten days? My rent is due tomorrow!", e={"K": "angry"}, p={"K": "panic"}, punch=True,
         say="[panicking] Ten DAYS? My rent is due tomorrow!"),
    dict(s="N", t="And accounting just told me the quarterly tax filing is due on the fifteenth.", e={"N": "annoyed"},
         p={"N": "cross"}, look={"K": None}),
    dict(s="B", t="Wait. We have a tax filing?", e={"B": "shocked"}, p={"B": "shrug"}),
    dict(s="N", t="Dave did it every quarter. For fifteen years.", e={"N": "angry"}, p={"N": "point"}, cam="med"),
    dict(shot="error_B", s="B", t="PayBot! Override! Pay everyone! That's an order!", e={"B": "angry"}, p={"B": "point"},
         look={"B": "up"}, say="[shouting] PayBot! Override! Pay everyone! That's an ORDER!"),
    dict(s="P", t="Great question! Did you know payroll is very important? Please contact Dave Miller. Have a wonderful day!",
         e={"B": "shocked"}, p={"B": "head"},
         say="[robotic, overly cheerful] Great question! Did you know payroll is very important? Please contact Dave Miller. Have a wonderful day!"),
    dict(shot="error_BN", s="N", t="Brad. Call Dave. Now.", e={"N": "angry", "B": "worried"}, p={"N": "point", "B": "idle"},
         look={"B": None, "N": None}, cam="med"),
    dict(s="B", t="That might be a little awkward. I kind of told him he was replaceable.", e={"B": "worried"},
         p={"B": "shrug"}),
    dict(s="N", t="Then you'd better sound very, very sorry.", e={"N": "smug"}, p={"N": "cross"}),
    dict(shot="error_B", s="B", t="Fine. I'm calling him.", e={"B": "sad"}, p={"B": "phone"}, prop={"B": "phone"},
         say="[sighs] Fine. I'm calling him.", gap=0.6),
    dict(s="B", t="Dave! My man! Long time no see!", e={"B": "happy"}, cam="close",
         say="[fake cheerful] Dave! My man! Long time no see!", gap=0.8),
]
