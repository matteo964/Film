"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="queue_GM", s="G", t="She'll be here any minute. You apologize, you smile, and not one word about that recording.",
         e={"G": "annoyed", "M": "calm"}, p={"G": "point", "M": "cross"}),
    dict(s="M", t="Got it.", e={"M": "smug"}),
    dict(shot="queue_GKM", s="K", t="So this is the rude little agent.", e={"K": "smug", "G": "happy", "M": "calm"},
         p={"K": "hips", "G": "idle", "M": "idle"}, look={"K": "away"}, say="[condescending] So THIS is the rude little agent."),
    dict(s="G", t="Welcome! Coffee? A pastry? Anything you want.", e={"G": "happy"}, p={"G": "explain"},
         look={"K": None}, say="[overly friendly] Welcome! Coffee? A pastry? Anything you want."),
    dict(s="K", t="I want my apology.", e={"K": "annoyed"}, p={"K": "cross"}),
    dict(s="G", t="Maya. Now.", e={"G": "angry"}, p={"G": "point"}),
    dict(s="M", t="Of course. But first, let's make sure I apologize for the right things.", e={"M": "smug"},
         p={"M": "explain"}, cam="med"),
    dict(shot="queue_DM", s="M", t="Devin, can you put call forty four seventy one on the big screen?", e={"M": "neutral", "D": "happy"},
         p={"D": "idle"}),
    dict(s="D", t="Already loading it.", e={"D": "smug"}, p={"D": "point"}, look={"D": "up"}, gap=0.4),
    dict(shot="recording_GKM", s="M", t="I'm so sorry about that, ma'am. I can see the double charge. I'll refund it right now.",
         fx="phone", e={"G": "shocked", "K": "neutral", "M": "calm"}, p={"G": "idle", "K": "cross", "M": "idle"},
         look={"G": "up", "K": "up", "M": "up", "D": None},
         say="[politely] I'm so sorry about that, ma'am. I can see the double charge. I'll refund it right now.",
         sfx=[("ding", 0.0)]),
    dict(s="K", t="A refund? That's it? I want a free year of service, and I want you fired!", fx="phone",
         say="[outraged] A refund? That's it? I want a free year of service, and I want you FIRED!"),
    dict(s="G", t="Turn that off!", e={"G": "angry"}, p={"G": "stop"}, look={"G": None}, punch=True,
         say="[panicking] Turn that OFF!"),
    dict(shot="recording_DM", s="D", t="Sir, she offered the refund in the first thirty seconds.", e={"D": "neutral"},
         look={"D": None, "M": None}, p={"D": "explain"}),
    dict(shot="recording_GKM", s="K", t="Interesting. So your agent was polite, solved the problem, and followed policy.",
         e={"K": "calm"}, look={"K": None, "M": None}, p={"K": "think"}),
    dict(s="G", t="Well, technically. But the customer is always right!", e={"G": "worried"}, p={"G": "shrug"}),
    dict(s="K", t="And you gave me a free year, a written apology, and promised to fire her.", e={"K": "neutral"},
         p={"K": "explain"}),
    dict(s="G", t="Exactly! Five star service!", e={"G": "happy"}, p={"G": "chest"}, say="[proudly] Exactly! Five star service!"),
    dict(s="K", t="Then let me introduce myself properly.", e={"K": "smug"}, p={"K": "idle"}, cam="med"),
    dict(s="K", t="Linda Holt. Corporate Quality Assurance. I'm a mystery shopper.", e={"K": "smug"}, cam="close",
         say="[calmly, professional] Linda Holt. Corporate Quality Assurance. I'm a mystery shopper."),
    dict(s="G", t="A mystery shopper?", e={"G": "shocked"}, p={"G": "head"}, punch=True, say="[stunned] A... mystery shopper?",
         gap=0.8),
]
