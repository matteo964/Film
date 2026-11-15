"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="gone_M", s="M", t="Twelve thirty one. It's gone. They took the bait.", e={"M": "shocked", "J": "neutral"}, p={"M": "point"},
         cam="close", say="[excited whisper] Twelve thirty-one. It's gone. They took the bait."),
    dict(s="M", t="Now we just look for the person whose face is on fire.", e={"M": "smug"}, p={"M": "hips"}, gap=0.4),
    dict(shot="open_JB", s="J", t="Brenda! Hi! How was lunch?", e={"J": "happy", "B": "neutral"}, p={"J": "explain", "B": "idle"},
         say="[suspiciously cheerful] Brenda! Hi! How was lunch?"),
    dict(s="B", t="A salad. Again. I'm on a diet. Why is everyone asking?", e={"B": "confused"}, p={"B": "shrug"}),
    dict(shot="board1_J", s="J", t="Totally normal face. Not Brenda.", e={"J": "neutral"}, p={"J": "point"}, look={"J": "away"}, sfx=[("ding", 0.3)]),
    dict(shot="open_MK", s="M", t="Kevin. You eat anything. Did you eat my lasagna?", e={"M": "annoyed", "K": "neutral"}, p={"M": "point", "K": "idle"}),
    dict(s="K", t="I wish. I've been fixing the printer since ten. It ate my lunch too.", e={"K": "sad"}, p={"K": "shrug"},
         say="[tired] I wish. I've been fixing the printer since ten. It ate my lunch too."),
    dict(shot="board2_M", s="M", t="Not Kevin.", e={"M": "neutral"}, p={"M": "point"}, look={"M": "away"}, sfx=[("ding", 0.3)]),
    dict(shot="open_JZ", s="J", t="Zac. Be honest. Where were you at twelve thirty?", e={"J": "annoyed", "Z": "worried"}, p={"J": "cross", "Z": "idle"}),
    dict(s="Z", t="Lunch with my mom. She brought sandwiches. Am I in trouble?", e={"Z": "worried"}, p={"Z": "chest"}),
    dict(shot="board3_MJ", s="M", t="Then who? Nobody else uses that fridge.", e={"M": "confused", "J": "confused"}, p={"M": "shrug"}, sfx=[("ding", 0.3)],
         say="[frustrated] Then WHO? Nobody else uses that fridge."),
    dict(s="J", t="Wait. What about the meeting room? Gary's been in there with a client since twelve forty five.", e={"J": "neutral"}, p={"J": "point"}),
    dict(shot="glass_GC", s="G", t="As you can see, at our company, our people come first.", e={"G": "smug", "C": "neutral"}, p={"G": "point", "C": "cross"},
         look={"G": "up"}),
    dict(s="C", t="Gary, are you alright? You're turning red.", e={"C": "confused"}, p={"C": "explain"}),
    dict(shot="red_GC", s="G", t="I'm fine. It's just warm in here.", e={"G": "worried"}, p={"G": "chest"}, look={"G": None},
         say="[voice cracking, strained] I'm fine. It's just... warm in here."),
    dict(shot="red_G", s="G", t="Who put ghost pepper in the lasagna?", e={"G": "angry"}, p={"G": "panic"}, cam="close", punch=True,
         sfx=[("clunk", 0.0)], say="[screaming, voice cracking] WHO PUT GHOST PEPPER IN THE LASAGNA?!", gap=0.8),
]
