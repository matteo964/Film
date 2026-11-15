"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="red_G", s="G", t="Who put ghost pepper in the lasagna?", e={"G": "angry", "M": "smug", "J": "shocked"}, p={"G": "panic"},
         cam="close", punch=True, say="[screaming, voice cracking] WHO PUT GHOST PEPPER IN THE LASAGNA?!"),
    dict(shot="red_GMJ", s="M", t="Interesting question, Gary.", e={"M": "smug", "J": "smug"}, p={"M": "cross", "J": "idle"},
         say="[calm, slow] Interesting question, Gary."),
    dict(s="M", t="How did you know there was a lasagna?", e={"M": "smug"}, p={"M": "point"}, cam="med"),
    dict(s="G", t="I, uh, I smelled it. From the meeting room.", e={"G": "worried"}, p={"G": "shrug"}, say="[sweating, panicked] I, uh... I smelled it. From the meeting room."),
    dict(s="J", t="Through a closed glass door?", e={"J": "smug"}, p={"J": "cross"}),
    dict(s="G", t="I have a very good nose!", e={"G": "angry"}, p={"G": "panic"}, say="[voice cracking] I have a very good nose!"),
    dict(shot="open_M", s="M", t="Then you won't mind if we check the fridge camera.", e={"M": "smug"}, p={"M": "phone"}, prop={"M": "phone"}),
    dict(shot="cam_reveal", s="J", t="Day twenty four. Twelve thirty. And there's the hand.", e={"J": "neutral"}, sfx=[("ding", 1.6)],
         say="[narrating, tense] Day twenty-four. Twelve thirty. And there's the hand..."),
    dict(s="M", t="And there's the face. Hi, Gary.", e={"M": "smug"}, say="[dry] And there's the face. Hi, Gary."),
    dict(shot="red_GMJ", s="G", t="That could be anyone! Anyone with gray hair and a yellow tie!", e={"G": "worried"}, p={"G": "explain"},
         prop={"M": None}, say="[croaking, desperate] That could be anyone! Anyone with gray hair and a yellow tie!"),
    dict(s="J", t="Gary. You're wearing a yellow tie. Right now.", e={"J": "smug"}, p={"J": "point"}, say="[deadpan] Gary. You're wearing a yellow tie. Right now."),
    dict(s="G", t="It's a very common tie!", e={"G": "angry"}, p={"G": "panic"}, say="[squeaky] It's a very common tie!"),
    dict(shot="red_GC", s="C", t="Gary. Did you just say your people come first?", e={"C": "smug", "G": "sad"}, p={"C": "cross", "G": "idle"}, prop={"M": None}),
    dict(s="C", t="Drink some milk, Gary. We'll continue when you can feel your tongue again.", e={"C": "smug"}, p={"C": "explain"}),
    dict(s="G", t="It was one lasagna!", e={"G": "worried"}, p={"G": "pray"}, say="[desperate] It was ONE lasagna!"),
    dict(shot="red_GMJ", s="M", t="Twenty three lasagnas, Gary. And one very rude note.", e={"M": "angry"}, p={"M": "point"}),
    dict(s="J", t="Delicious. Thanks. With a smiley face.", e={"J": "smug"}, say="[mocking] 'Delicious. Thanks.' With a smiley face."),
    dict(s="G", t="Fine! I'll buy you lunch. For twenty three days.", e={"G": "sad"}, p={"G": "shrug"}, say="[defeated, hoarse] Fine! I'll buy you lunch. For twenty-three days."),
    dict(s="M", t="For the whole team, Gary.", e={"M": "smug"}, cam="med"),
    dict(shot="end_MG", s="M", t="Oh, and Gary? I made extra. Want some?", e={"M": "smug", "G": "shocked"}, p={"M": "point", "G": "idle"},
         say="[sweetly] Oh, and Gary? I made extra. Want some?"),
    dict(s="G", t="No!", e={"G": "shocked"}, p={"G": "panic"}, cam="close", punch=True, say="[terrified, hoarse] NO!", gap=0.8),
]
