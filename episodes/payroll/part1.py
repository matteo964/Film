"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_BD", s="B", t="Dave! Come in. Close the door.", e={"B": "smug", "D": "neutral"},
         p={"B": "desk", "D": "idle"}),
    dict(s="D", t="You wanted to see me, Brad?", e={"D": "calm"}),
    dict(s="B", t="I'll keep it short. You're fired.", p={"B": "desk_point"}, cam="med",
         say="[casually] I'll keep it short. You're fired."),
    dict(s="D", t="Fired? I've been running payroll here for fifteen years.", e={"D": "shocked"}, p={"D": "chest"},
         punch=True),
    dict(s="B", t="Exactly. Fifteen years of typing numbers into spreadsheets.", e={"B": "smug"},
         p={"B": ["desk_explain", "desk"]}),
    dict(s="B", t="I just bought PayBot. AI payroll. It does your entire job for forty nine dollars a month.",
         e={"B": "happy"}, p={"B": ["desk_explain", "desk_point"]}),
    dict(s="D", t="Forty nine dollars.", e={"D": "annoyed"}, p={"D": "cross"}),
    dict(s="B", t="It never sleeps, never takes vacation, and never asks for a raise.", e={"B": "smug"},
         p={"B": "desk_lean"}, say="[smugly] It never sleeps, never takes vacation, and NEVER asks for a raise."),
    dict(s="D", t="Does it know about the bank authorization? Or the tax filing on the fifteenth?", e={"D": "neutral"},
         p={"D": "explain"}),
    dict(s="B", t="It's AI, Dave. It knows everything.", e={"B": "smug"}, cam="med",
         say="[laughs] It's AI, Dave. It knows EVERYTHING."),
    dict(s="D", t="If you say so.", e={"D": "calm"}, p={"D": "cross"}),
    dict(s="B", t="That's it? No begging?", e={"B": "confused"}, p={"B": "desk"}),
    dict(s="D", t="Would it help?", e={"D": "calm"}),
    dict(s="B", t="Not even a little.", e={"B": "smug"}),
    dict(s="B", t="Leave your passwords on the desk on your way out.", p={"B": "desk_point"}),
    dict(s="D", t="Already written down. Page one of my handover notes.", e={"D": "neutral"}, p={"D": "explain"}),
    dict(s="B", t="See? Easily replaceable.", e={"B": "happy"}, p={"B": "desk_lean"}),
    dict(s="D", t="One quick question.", e={"D": "neutral"}, p={"D": "explain2"}),
    dict(s="B", t="Make it fast.", e={"B": "annoyed"}),
    dict(s="D", t="Did anyone tell PayBot that payday is this Friday?", e={"D": "smug"}, p={"D": "think"},
         cam="close"),
    dict(s="B", t="It's AI. It'll figure it out.", e={"B": "annoyed"}, p={"B": "desk_explain"}),
    dict(s="D", t="Right. Good luck, Brad.", e={"D": "calm"}, p={"D": "idle"}, gap=0.5),

    dict(shot="logo_BK", s="K", t="Brad? My paycheck didn't come in this morning.", e={"K": "worried", "B": "smug"},
         p={"K": "chest", "B": "cross"}),
    dict(s="B", t="Probably just the bank. Give it an hour.", e={"B": "neutral"}, p={"B": "shrug"}),
    dict(s="K", t="It's not just mine. Nobody got paid. The entire company.", e={"K": "angry"}, p={"K": "point"},
         cam="med"),
    dict(s="B", t="Relax. PayBot is handling it. It's AI.", e={"B": "smug"}, p={"B": "point"}, gap=0.4),
    dict(shot="logo_BNK", s="N", t="Brad. Two hundred employees just didn't get paid.",
         e={"N": "angry", "B": "worried", "K": "worried"}, p={"N": "hips", "B": "idle", "K": "idle"},
         look={"K": "away"}),
    dict(s="N", t="So tell me. Where is Dave?", e={"N": "angry"}, p={"N": "point"}, cam="close",
         say="[coldly] So tell me. Where is Dave?", gap=0.8),
]
