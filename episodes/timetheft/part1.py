"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="T", t="Eleven minutes, Nora. Eleven minutes of nothing. That's called time theft.", e={"T": "smug", "N": "shocked"},
         sfx=[("alarm", 0.0)], say="[smug, accusing] Eleven minutes, Nora. Eleven minutes of NOTHING. That's called time theft."),
    dict(s="N", t="Trent. I was in the bathroom.", e={"N": "annoyed"}, say="[stunned, flat] Trent. I was in the bathroom.", gap=0.4),
    dict(shot="office_T", s="T", t="Bathroom breaks are personal time. And on my team, personal time comes out of your pay.", e={"T": "smug"},
         p={"T": "desk_explain"}),
    dict(shot="office_N", s="N", t="You're docking my pay for going to the bathroom?", e={"N": "shocked"}, p={"N": "shrug"}, punch=True,
         say="[outraged] You're docking my pay for going to the BATHROOM?"),
    dict(shot="office_T", s="T", t="WorkWatch doesn't lie. Screenshots every five minutes. Mouse tracking. Webcam. It sees everything.",
         e={"T": "happy"}, p={"T": "desk_point"}, say="[proud] WorkWatch doesn't lie. Screenshots every five minutes. Mouse tracking. Webcam. It sees everything."),
    dict(shot="office_N", s="N", t="Then it also saw this.", e={"N": "smug"}, p={"N": "phone"}, prop={"N": "phone"}),
    dict(shot="late", s="N", t="Yesterday I logged out at nine fourteen p.m. Three hours of overtime. Unpaid.", e={"N": "calm"}, sfx=[("ding", 0.0)]),
    dict(shot="office_T", s="T", t="Nobody asked you to stay late. Overtime doesn't count.", e={"T": "smug"}, p={"T": "desk_lean"},
         say="[dismissive] Nobody asked you to stay late. Overtime doesn't count."),
    dict(shot="office_N", s="N", t="So my eleven minutes count. But my three hours don't?", e={"N": "angry"}, p={"N": "cross"}, prop={"N": None}),
    dict(shot="office_T", s="T", t="Exactly. Written warning. And if it happens again, you're out.", e={"T": "smug"}, p={"T": "desk_point"}, cam="med"),
    dict(shot="office_TNP", s="P", t="Trent, quick update. The CEO loves your WorkWatch idea.", e={"P": "neutral", "T": "happy", "N": "annoyed"},
         p={"P": "explain", "T": "desk", "N": "cross"}),
    dict(s="T", t="Of course he does. Productivity!", e={"T": "happy"}, p={"T": "desk_explain"}, say="[smug] Of course he does. Productivity!"),
    dict(s="P", t="He wants a company wide report on Friday. Every employee.", e={"P": "neutral"}),
    dict(shot="office_P", s="P", t="Including managers.", e={"P": "smug"}, cam="close", say="[pointed] Including managers."),
    dict(shot="office_T", s="T", t="Managers?", e={"T": "shocked"}, p={"T": "desk_lean"}, cam="close", punch=True,
         say="[voice cracking] Managers?", gap=0.8),
]
