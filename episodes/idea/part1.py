"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="night_M", s="M", t="Okay. Page twenty four. Done. Project Lighthouse is finally finished.", e={"M": "happy"},
         p={"M": "type"}, say="[tired but proud] Okay. Page twenty four. Done. Project Lighthouse is finally finished."),
    dict(s="M", t="This could save the company three million dollars a year.", e={"M": "happy"}, p={"M": "explain"}, cam="med",
         say="[excited whisper] This could save the company three million dollars a year.", gap=0.4),
    dict(shot="eve_BM", s="B", t="Still here, Mia? What are you working on?", e={"B": "smug", "M": "happy"}, p={"B": "cross", "M": "idle"},
         say="[casual] Still here, Mia? What are you working on?"),
    dict(s="M", t="A plan to cut our shipping costs. I'm pitching it to the CEO next week.", e={"M": "happy"}, p={"M": "explain"}),
    dict(s="B", t="Cool. Mind if I take a look?", e={"B": "smug"}, p={"B": "point"}, look={"B": "down"}),
    dict(s="M", t="Sure, just page one for now. The rest isn't ready.", e={"M": "neutral"}, look={"B": None}, gap=0.4),
    dict(shot="pitch_BO", s="B", t="Mr. Okafor, I had a breakthrough at two a.m. last night. I call it Project Lighthouse.",
         e={"B": "smug", "O": "neutral"}, p={"B": "point", "O": "cross"}, look={"B": "up"}, sfx=[("ding", 0.0)],
         say="[confident] Mr. Okafor, I had a breakthrough at two a.m. last night. I call it Project Lighthouse."),
    dict(shot="pitch_O", s="O", t="Interesting. How did you come up with it?", e={"O": "neutral"}, p={"O": "think"}),
    dict(shot="pitch_B", s="B", t="Honestly? Raw talent. And a lot of late nights.", e={"B": "smug"}, p={"B": "chest"},
         say="[smugly] Honestly? Raw talent. And a lot of late nights."),
    dict(shot="pitch_M", s="M", t="Wait. What?", e={"M": "shocked"}, p={"M": "chest"}, punch=True, say="[stunned whisper] Wait... what?"),
    dict(shot="pitch_O", s="O", t="Three million dollars in savings? Brad, this is brilliant.", e={"O": "happy"}, p={"O": "explain"},
         look={"O": "up"}, say="[impressed] Three million dollars in savings? Brad, this is brilliant."),
    dict(shot="pitch_BMO", s="M", t="Mr. Okafor, that's actually my-", e={"M": "worried", "B": "smug", "O": "neutral"},
         p={"M": "explain", "B": "cross", "O": "idle"}, look={"O": None}),
    dict(s="B", t="Mia helped too. With the fonts.", e={"B": "smug"}, p={"B": "shrug"}, cam="med",
         say="[smugly] Mia helped too. With the fonts."),
    dict(shot="pitch_M", s="M", t="The fonts?", e={"M": "angry"}, say="[outraged whisper] The FONTS?"),
    dict(shot="pitch_O", s="O", t="Brad, you'll lead Lighthouse. Present the full plan to the board on Friday.", e={"O": "happy"},
         p={"O": "point"}),
    dict(shot="pitch_B", s="B", t="The full plan? Absolutely. No problem.", e={"B": "worried"}, p={"B": "chest"},
         say="[slightly nervous] The full plan? Absolutely. No problem."),
    dict(shot="pitch_M", s="M", t="The full plan is twenty four pages. Brad only saw page one.", e={"M": "smug"}, cam="close",
         look={"M": "front"}, say="[quietly, smiling] The full plan is twenty four pages. Brad only saw page one.", gap=0.8),
]
