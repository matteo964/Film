"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="slides_MH", s="H", t="Mark. It's nine fifteen. Where is your presenter?", e={"H": "annoyed", "M": "worried"},
         p={"H": "cross", "M": "shrug"}),
    dict(s="M", t="He's on his way. Traffic, probably.", e={"M": "worried"}, say="[nervously] He's on his way. Traffic, probably."),
    dict(shot="slides_T", s="T", t="Sorry I'm late, bro. I mean, ma'am.", e={"T": "happy"}, p={"T": "explain"},
         say="[out of breath, casual] Sorry I'm late, bro. I mean... ma'am.", gap=0.3),
    dict(shot="slides_H", s="H", t="Fifteen minutes late. In my business, that's a resignation letter.", e={"H": "angry"}, p={"H": "hips"},
         say="[cold, British] Fifteen minutes late. In my business, that's a resignation letter."),
    dict(shot="fail_T", s="T", t="Okay. Let's gooo. Slide one. Our plan for the Hendrson Gruop.", e={"T": "smug"}, p={"T": "point"},
         look={"T": "up"}, sfx=[("ding", 0.0)], say="[hyped] Okay. Let's gooo. Slide one. Our plan for the Hendrson Gruop."),
    dict(shot="fail_H", s="H", t="You spelled my company's name wrong.", e={"H": "annoyed"}, look={"H": "up"}),
    dict(shot="fail_T", s="T", t="It's a creative choice.", e={"T": "worried"}, look={"T": None}, p={"T": "shrug"}),
    dict(shot="fail_H", s="H", t="Revenue. Vibes? Strategy. Just grind? Is this a joke?", e={"H": "angry"}, look={"H": "up"},
         say="[appalled] Revenue... vibes? Strategy... just grind? Is this a joke?"),
    dict(shot="fail_T", s="T", t="It's called a vibe check.", e={"T": "smug"}, p={"T": "cross"}, say="[proudly] It's called a vibe check."),
    dict(shot="fail_MTH", s="H", t="Mark. Where is Emma?", e={"H": "angry", "M": "worried", "T": "confused"}, look={"H": None},
         p={"H": "cross", "M": "idle", "T": "idle"}),
    dict(s="M", t="Tyler leads the account now. He's family.", e={"M": "worried"}, p={"M": "explain"}),
    dict(shot="fail_H", s="H", t="Family? Emma built this plan with us for three months. She's the reason we renewed. Twice.",
         e={"H": "angry"}, p={"H": "point"}),
    dict(shot="fail_M", s="M", t="Emma is, uh, still with the company.", e={"M": "worried"}, p={"M": "shrug"}),
    dict(shot="fail_H", s="H", t="Not for long. She told me Brightline offered her a job.", e={"H": "smug"}, p={"H": "cross"}),
    dict(shot="fail_M", s="M", t="Brightline? Our biggest competitor?", e={"M": "shocked"}, p={"M": "head"}, punch=True,
         say="[shocked] Brightline? Our biggest COMPETITOR?"),
    dict(shot="fail_H", s="H", t="If Emma isn't leading our account by Friday, we're taking our business to Brightline. With her.",
         e={"H": "angry"}, p={"H": "point"}, cam="close",
         say="[firm, final] If Emma isn't leading our account by Friday, we're taking our business to Brightline. With her."),
    dict(shot="fail_T", s="T", t="So, is that a no on the vibe check?", e={"T": "confused"}, p={"T": "shrug"}, cam="close",
         say="[clueless] So... is that a no on the vibe check?", gap=0.8),
]
