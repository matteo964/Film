"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="wb5_DMT", s="M", t="Monica Hayes, HR. Darren, did you just threaten to fire people for discussing their pay?",
         e={"M": "angry", "D": "worried", "T": "neutral", "L": "calm"}, p={"M": "point", "D": "idle", "T": "idle"}),
    dict(s="D", t="It's company policy! Salaries are confidential!", e={"D": "worried"}, p={"D": "shrug"}),
    dict(s="M", t="There is no such policy. Because it would be illegal.", e={"M": "smug"}, p={"M": "cross"}),
    dict(shot="wb5_L", s="L", t="Darren also told me I was at the top of my pay band.", e={"L": "calm"}, p={"L": "explain"}),
    dict(shot="bands_M", s="M", t="These are the official bands. Seniors with six plus years start at a hundred fifteen thousand.",
         e={"M": "neutral"}, p={"M": "point"}, look={"M": "up"}, sfx=[("ding", 0.0)]),
    dict(s="M", t="Lena, you're below the junior band. After eight years.", e={"M": "annoyed"}, look={"M": None}),
    dict(shot="bands_D", s="D", t="I was saving the company money!", e={"D": "worried"}, p={"D": "pray"},
         say="[desperate] I was saving the company money!"),
    dict(shot="bands_DM", s="M", t="You were underpaying your most loyal people. And keeping the difference in your team budget for your bonus.",
         e={"M": "angry"}, p={"M": "point"}),
    dict(s="D", t="How do you know about my bonus?", e={"D": "shocked"}, p={"D": "head"}, punch=True,
         say="[panicked] How do you know about my bonus?"),
    dict(s="M", t="I'm HR, Darren. I know everyone's salary.", e={"M": "smug"}, p={"M": "cross"}, cam="med",
         say="[dry] I'm HR, Darren. I know everyone's salary."),
    dict(shot="bands_D", s="D", t="Lena. Okay. Let's talk privately. Seventy thousand. Final offer.", e={"D": "worried"}, p={"D": "explain"},
         say="[fake friendly] Lena. Okay. Let's talk privately. Seventy thousand. Final offer."),
    dict(shot="bands_LM", s="L", t="Read the screen, Darren. Juniors start at seventy.", e={"L": "smug", "M": "smug"}, p={"L": "point"},
         look={"L": "up"}, say="[dry] Read the screen, Darren. JUNIORS start at seventy."),
    dict(shot="bands_LM", s="M", t="Effective today, everyone on that board gets paid within their band. With back pay. Lena, a hundred twenty thousand.",
         e={"M": "happy", "L": "shocked"}, p={"M": "explain", "L": "idle"}),
    dict(s="L", t="A hundred twenty?", e={"L": "happy"}, p={"L": "chest"}, say="[emotional] A hundred and twenty?"),
    dict(shot="wb5_LT", s="T", t="Told you. More than me.", e={"T": "happy", "L": "happy"}, p={"T": "shrug", "L": "idle"},
         say="[grinning] Told you. More than me."),
    dict(shot="bands_D", s="D", t="And what happens to my salary?", e={"D": "sad"}, p={"D": "chest"}, say="[nervous] And what happens to MY salary?"),
    dict(shot="wb5_L", s="L", t="Sorry, Darren. Salaries are confidential.", e={"L": "smug"}, p={"L": "hips"}, cam="close",
         say="[sweetly] Sorry, Darren. Salaries are confidential.", gap=0.8),
]
