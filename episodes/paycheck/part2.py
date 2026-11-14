"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="wb1_L", s="L", t="Then I'll go first. Who's next?", e={"L": "smug", "R": "neutral", "D": "angry", "T": "neutral"},
         p={"L": "write"}, prop={"L": "chalk"}, say="[calm, defiant] Then I'll go first. Who's next?"),
    dict(shot="wb_ramp", s="R", t="Six years. Sixty four thousand. Maya, you're up.", e={"R": "smug"}, p={"R": "write"}, prop={"R": "chalk"},
         sfx=[("ding", 1.6), ("ding", 3.2)], gap=1.2),
    dict(s="R", t="Maya, five years, fifty nine. Chris, two months, a hundred and five.", e={"R": "shocked"}, p={"R": "point"},
         look={"R": "up"}, say="[reading, getting angry] Maya, five years, fifty-nine. Chris... two months, a hundred and five."),
    dict(s="R", t="Everyone who's been here for years makes half of what the new people get.", e={"R": "angry"}, look={"R": None}, cam="med"),
    dict(shot="wb4_D", s="D", t="What is going on here? Wipe that board. Now!", e={"D": "angry"}, p={"D": "point"}, prop={"R": None},
         say="[furious] What is going on here? Wipe that board. NOW!"),
    dict(s="D", t="This is confidential company information!", e={"D": "angry"}, p={"D": "stop"}),
    dict(s="D", t="Everyone who wrote on that board is getting a written warning!", e={"D": "angry"}, p={"D": "point"},
         say="[shouting] Everyone who wrote on that board is getting a written warning!"),
    dict(shot="wb4_R", s="R", t="Go ahead. Warn all of us. Who's going to do the work then?", e={"R": "smug"}, p={"R": "cross"},
         prop={"R": None}),
    dict(shot="wb4_D", s="D", t="The new people can do it! That's why I hired them!", e={"D": "angry"}, p={"D": "explain"},
         say="[desperate] The new people can do it! That's why I hired them!"),
    dict(shot="wb4_DT", s="T", t="Hold on, Darren.", e={"T": "neutral", "D": "angry"}, p={"T": "stop", "D": "idle"}, look={"D": "away"}),
    dict(s="D", t="Tyler. Stay out of this. This doesn't concern you.", e={"D": "annoyed"}, p={"D": "point"}),
    dict(s="T", t="Lena trained me for a month. She's the reason I can do this job.", e={"T": "annoyed"}, p={"T": "explain"}),
    dict(shot="wb5_T", s="T", t="Tyler. Three weeks. One hundred twelve thousand.", e={"T": "smug"}, p={"T": "write"}, prop={"T": "chalk"},
         sfx=[("ding", 0.2)], say="[firm] Tyler. Three weeks. One hundred twelve thousand."),
    dict(s="T", t="She should be making more than me. Not half.", e={"T": "angry"}, p={"T": "point"}, prop={"T": None}, cam="med"),
    dict(shot="wb5_DT", s="D", t="Tyler, you just ended your career here.", e={"D": "angry"}, p={"D": "point"}, look={"D": None},
         say="[cold] Tyler, you just ended your career here."),
    dict(shot="wb5_M", s="M", t="I don't think it's his career that's ending, Darren.", e={"M": "angry"}, p={"M": "cross"}, cam="close",
         say="[calm, ice-cold] I don't think it's HIS career that's ending, Darren.", gap=0.8),
]
