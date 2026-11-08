"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="error_B", s="B", t="Dave! My man! Long time no see!", e={"B": "happy", "D": "calm"},
         p={"B": "phone", "D": "lap_phone"}, prop={"B": "phone", "D": "phone"},
         say="[fake cheerful] Dave! My man! Long time no see!"),
    dict(shot="home", s="D", t="It's been two days, Brad.", e={"D": "calm"}, cam="med"),
    dict(shot="error_B", s="B", t="Funny thing. PayBot says it needs you to approve payroll.", e={"B": "worried"},
         say="[nervous laugh] Funny thing. PayBot says it needs you to approve payroll."),
    dict(shot="home", s="D", t="I know. I'm the authorized signer at the bank. It's on page one of my notes.",
         e={"D": "smug"}),
    dict(shot="error_B", s="B", t="Great! So can you just log in real quick?", e={"B": "happy"}),
    dict(shot="home", s="D", t="I don't work there anymore, Brad. You fired me.", e={"D": "calm"}),
    dict(shot="error_B", s="B", t="Come on! Two hundred people didn't get paid!", e={"B": "angry"},
         say="[desperate] Come on! Two hundred people didn't get paid!"),
    dict(shot="home", s="D", t="I'm aware. Most of them already called me.", e={"D": "smug"}, cam="close"),
    dict(shot="error_BN", s="N", t="Give me that phone.", e={"N": "annoyed", "B": "worried"},
         p={"N": "stop", "B": "idle"}, prop={"B": None}),
    dict(s="N", t="Dave, it's Diane. I'm sorry about all of this. What would it take to get you back?",
         p={"N": "phone"}, prop={"N": "phone"}, e={"N": "neutral"}),
    dict(shot="home", s="D", t="My job back. A thirty percent raise. And I report to you. Not Brad.", e={"D": "neutral"},
         p={"D": "lap_explain"}),
    dict(shot="error_BN", s="N", t="Done.", e={"N": "calm"}),
    dict(shot="home", s="D", t="And PayBot?", e={"D": "smug"}, p={"D": "lap_phone"}),
    dict(shot="error_BN", s="N", t="Cancelled.", e={"N": "smug"}),
    dict(shot="home", s="D", t="Then give me ten seconds.", e={"D": "calm"}, p={"D": "lap_phone"}, gap=0.5),
    dict(shot="paid_BNK", beat=1.3, sfx=[("ding", 0.0)], e={"B": "shocked", "N": "happy", "K": "happy"},
         p={"N": "idle", "B": "idle", "K": "idle"}, prop={"N": None}, look={"B": "up", "N": "up", "K": "up"}),
    dict(s="K", t="My paycheck just came in! Everybody got paid!", e={"K": "happy"}, p={"K": "panic"},
         look={"B": None, "N": None, "K": "away"}, say="[excited] My paycheck just came in! Everybody got paid!"),
    dict(shot="paid_BN", s="N", t="Brad. You almost caused a walkout to save forty nine dollars a month.",
         e={"N": "angry", "B": "worried"}, p={"N": "point"}),
    dict(s="B", t="Technically, it was a really good deal.", e={"B": "worried"}, p={"B": "shrug"}),
    dict(s="N", t="Here's another good deal. Your position has been replaced.", e={"N": "smug"}, p={"N": "cross"},
         cam="med"),
    dict(s="B", t="Replaced? By who?", e={"B": "shocked"}, p={"B": "chest"}, punch=True),
    dict(s="N", t="PayBot.", e={"N": "smug"}, say="[smugly] PayBot."),
    dict(shot="paid_B", s="P", t="Hi Brad! I'm your replacement. Have a wonderful day!", e={"B": "shocked"},
         p={"B": "head"}, look={"B": "up"}, sfx=[("ding", 0.0)],
         say="[robotic, overly cheerful] Hi Brad! I'm your replacement. Have a wonderful day!"),
    dict(shot="home", s="D", t="Don't worry, Brad. It never sleeps, never takes vacation, and never asks for a raise.",
         e={"D": "smug"}, p={"D": "lap_phone"}, cam="close",
         say="[dryly] Don't worry, Brad. It never sleeps, never takes vacation, and never asks for a raise.", gap=0.8),
]
