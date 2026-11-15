"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="M", t="Twenty three days. Twenty three lunches. Gone.", e={"M": "angry"}, sfx=[("ding", 0.0)],
         say="[intense, quiet] Twenty-three days. Twenty-three lunches. Gone."),
    dict(s="M", t="Today, I finally find out who's been eating them.", say="[determined] Today... I finally find out who's been eating them.",
         gap=0.4),
    dict(shot="day1", s="M", t="Day one. My lasagna is gone. Okay. Maybe a mistake.", e={"M": "confused"}, p={"M": "shrug"}, sfx=[("whoosh", 0.0)]),
    dict(shot="day7", s="M", t="Day seven. Still gone. So I left a note. Please stop.", e={"M": "annoyed"}, p={"M": "point"}, sfx=[("whoosh", 0.0)]),
    dict(shot="day15", s="M", t="Day fifteen. They wrote back. Delicious. Thanks.", e={"M": "angry"}, p={"M": "head"}, sfx=[("whoosh", 0.0)],
         say="[outraged] Day fifteen. They wrote BACK. 'Delicious. Thanks.'"),
    dict(s="M", t="With a smiley face.", e={"M": "angry"}, cam="close", say="[through gritted teeth] With a smiley face.", gap=0.4),
    dict(shot="board_MJ", s="J", t="Okay, detective. Who are the suspects?", e={"J": "smug", "M": "neutral"}, p={"J": "cross", "M": "point"}),
    dict(shot="board_M", s="M", t="Brenda. Says she's on a diet. But she's always in the kitchen.", e={"M": "neutral"}, p={"M": "point"}, look={"M": "away"}),
    dict(s="M", t="Kevin from IT. Eats literally everything. Once ate a birthday candle.", e={"M": "neutral"},
         say="[deadpan] Kevin from IT. Eats literally everything. Once ate a birthday candle."),
    dict(s="M", t="And Zac. The intern. Always hungry. Never brings lunch.", e={"M": "annoyed"}, look={"M": None}),
    dict(shot="kit_MJ_trap", s="J", t="So what's the plan?", e={"J": "neutral", "M": "smug"}, p={"J": "idle", "M": "explain"}),
    dict(s="M", t="Ghost pepper lasagna. Over a million Scoville. Same box. Same label.", e={"M": "smug"}, p={"M": "point"},
         say="[evil grin] Ghost pepper lasagna. Over a million Scoville. Same box. Same label."),
    dict(s="J", t="Milo, that's evil.", e={"J": "shocked"}, p={"J": "chest"}, say="[laughing] Milo, that's EVIL."),
    dict(s="M", t="Whoever eats this is going to tell on themselves.", e={"M": "smug"}, cam="med", gap=0.4),
    dict(shot="gone_M", s="M", t="Twelve thirty one. It's gone. They took the bait.", e={"M": "shocked"}, p={"M": "point"}, cam="close",
         sfx=[("ding", 0.0)], say="[excited whisper] Twelve thirty-one. It's gone. They took the bait.", gap=0.8),
]
