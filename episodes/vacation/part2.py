"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="slides_TM", s="T", t="Mr. Morgan! Welcome. Today I'll walk you through our proposal personally.",
         e={"T": "happy", "M": "neutral"}, p={"T": "explain2", "M": "cross"}),
    dict(s="M", t="Where's Ava?", e={"M": "neutral"}),
    dict(s="T", t="Ava is no longer with us. But don't worry, I know this account inside and out.", e={"T": "smug"},
         p={"T": "chest"}),
    dict(s="M", t="Good. Then what are our projected savings for the first quarter?", e={"M": "neutral"}, p={"M": "explain"}),
    dict(s="T", t="Great question. The savings are... significant.", e={"T": "worried"}, p={"T": "shrug"}, look={"T": "up"},
         say="[nervously] Great question. The savings are... significant."),
    dict(s="M", t="Your slide says question mark, question mark, question mark.", e={"M": "annoyed"}, look={"M": "up"}),
    dict(s="T", t="That's, uh, a placeholder.", e={"T": "worried"}, look={"T": None}),
    dict(s="M", t="And the delivery routes? It says ask Ava.", e={"M": "angry"}, p={"M": "point"}, look={"M": None}, cam="med"),
    dict(s="T", t="Ava abandoned the company for a vacation. Very unprofessional.", e={"T": "annoyed"}, p={"T": "cross"}),
    dict(s="M", t="Ava told me about her sister's wedding three months ago. She said the vacation was approved.",
         e={"M": "annoyed"}, p={"M": "cross"}),
    dict(s="M", t="She even set up the whole handover. Did you read it?", e={"M": "neutral"}),
    dict(s="T", t="I've been very busy.", e={"T": "worried"}, p={"T": "shrug"}),
    dict(s="M", t="Let me be clear. We chose your company because of Ava. No Ava, no contract.", e={"M": "angry"},
         p={"M": "point"}, cam="close", say="[firmly] Let me be clear. We chose your company because of Ava. No Ava, no contract."),
    dict(s="T", t="No contract? That's two million dollars!", e={"T": "shocked"}, p={"T": "panic"}, punch=True,
         say="[panicking] No contract? That's two MILLION dollars!", gap=0.4),
    dict(shot="slides_THM", s="H", t="Todd. A word. Now.", e={"H": "angry", "T": "worried", "M": "neutral"},
         p={"H": "paper", "T": "idle", "M": "cross"}, prop={"H": "paper:FIRED"}),
    dict(s="H", t="Is this your signature on a termination letter for Ava Brooks?", e={"H": "annoyed"}),
    dict(s="T", t="Yes! She left during a critical week.", e={"T": "neutral"}, p={"T": "explain"}),
    dict(s="H", t="For a vacation that you approved. And HR approved. Six months ago.", e={"H": "angry"}, cam="med"),
    dict(s="H", t="You fired her for taking approved leave. And you put it in writing.", e={"H": "angry"}, p={"H": "point"},
         prop={"H": None}),
    dict(s="M", t="Sounds like you should call Ava.", e={"M": "smug"}),
    dict(shot="slides_T", s="T", t="Okay. Okay. I'm calling her.", e={"T": "worried"}, p={"T": "phone"}, prop={"T": "phone"},
         say="[nervously] Okay. Okay. I'm calling her."),
    dict(s="T", t="Ava! Hi! It's Todd. How's Italy?", e={"T": "happy"}, cam="close",
         say="[fake cheerful] Ava! Hi! It's Todd. How's Italy?", gap=0.8),
]
