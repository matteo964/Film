"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="slides_T", s="T", t="Ava! Hi! It's Todd. How's Italy?", e={"T": "happy", "A": "calm"},
         p={"T": "phone", "A": "phone"}, prop={"T": "phone", "A": "phone"}, say="[fake cheerful] Ava! Hi! It's Todd. How's Italy?"),
    dict(shot="wedding_A", s="A", t="Beautiful. I'm at my sister's wedding, Todd. The one you fired me for.", e={"A": "smug"},
         cam="med"),
    dict(shot="slides_T", s="T", t="About that. Funny story. Mr. Morgan has a few questions.", e={"T": "worried"},
         say="[nervous laugh] About that. Funny story. Mr. Morgan has a few questions."),
    dict(shot="wedding_A", s="A", t="I left a twelve page handover on your desk. With every answer.", e={"A": "calm"}),
    dict(shot="slides_T", s="T", t="I may not have read it.", e={"T": "sad"}),
    dict(shot="wedding_A", s="A", t="I know. That's why the slides say ask Ava.", e={"A": "smug"},
         say="[laughs] I know. That's why the slides say ask Ava."),
    dict(shot="slides_THM", s="M", t="Give me the phone, Todd.", e={"M": "annoyed", "T": "worried", "H": "neutral"},
         p={"M": "stop", "T": "idle", "H": "cross"}, prop={"T": None}),
    dict(s="M", t="Ava, it's Richard Morgan. We'll sign the contract. But only with you as account lead.", p={"M": "phone"},
         prop={"M": "phone"}, e={"M": "happy"}),
    dict(shot="wedding_A", s="A", t="That's very kind, Mr. Morgan. But I don't work there anymore.", e={"A": "neutral"}),
    dict(shot="slides_THM", s="H", t="Ava, it's Ms. Grant from HR. The termination is reversed. With full back pay.",
         e={"H": "happy"}, p={"H": "explain"}, look={"H": "away"}),
    dict(s="H", t="And we'd like to offer you a promotion. Account director.", p={"H": "chest"}),
    dict(shot="wedding_A", s="A", t="Account director? That's Todd's job.", e={"A": "confused"}),
    dict(shot="slides_TH", s="H", t="It was Todd's job.", e={"H": "smug", "T": "shocked"}, p={"H": "cross", "T": "idle"},
         look={"H": None}, prop={"M": None}),
    dict(s="T", t="What? You can't do that! My promotion was approved!", e={"T": "angry"}, p={"T": "panic"}, punch=True,
         say="[outraged] What? You can't do that! My promotion was APPROVED!"),
    dict(s="H", t="Approvals can be un-approved, Todd. That's how management works.", e={"H": "smug"}, cam="med",
         say="[dryly] Approvals can be un-approved, Todd. That's how management works."),
    dict(shot="wedding_A", s="A", t="Then I accept. Starting Monday after next.", e={"A": "happy"}),
    dict(shot="signed_T", s="T", t="Monday after next? Can't you at least come in this week?", e={"T": "worried"},
         p={"T": "phone"}, prop={"T": "phone"}),
    dict(shot="wedding_LA", s="L", t="Ava! Your speech is in five minutes!", e={"L": "happy", "A": "happy"},
         p={"L": "explain", "A": "phone"}, say="[excited] Ava! Your speech is in five minutes!"),
    dict(s="A", t="Sorry, Todd. I'm on vacation. It was approved.", e={"A": "smug"}, cam="close",
         say="[sweetly] Sorry, Todd. I'm on vacation. It was approved.", gap=0.8),
]
