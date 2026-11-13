"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="ceo_BM", s="B", t="Sit down, Martin. I read your email. So did three hundred and eleven other people.",
         e={"B": "annoyed", "M": "worried", "S": "calm"}, p={"B": "desk", "M": "idle"}),
    dict(shot="ceo_M", s="M", t="Victoria, that was a joke. Office humor.", e={"M": "worried"}, p={"M": "shrug"},
         say="[nervous laugh] Victoria, that was a joke. Office humor."),
    dict(shot="ceo_B", s="B", t="You're planning layoffs at a team building retreat. That's not humor.", e={"B": "angry"}, p={"B": "desk_point"}),
    dict(s="B", t="Also, you don't have the authority to fire anyone. You never did.", e={"B": "smug"}, p={"B": "desk_lean"}, cam="med"),
    dict(shot="ceo_M", s="M", t="I don't?", e={"M": "shocked"}, punch=True),
    dict(shot="ceo_BMS", s="B", t="Sofia. Come in. Is this your file?", e={"B": "neutral", "S": "calm", "M": "worried"}, p={"B": "desk_explain", "S": "idle"}),
    dict(s="S", t="Four months of work. Created August second. Martin was copied on it once. In October.", e={"S": "calm"}, p={"S": "explain"}),
    dict(s="M", t="I was going to mention her. In the footnotes.", e={"M": "worried"}, p={"M": "shrug"},
         say="[weakly] I was going to mention her. In the footnotes."),
    dict(shot="ceo_B", s="B", t="Martin, your promotion review is cancelled. And so is your job.", e={"B": "angry"}, p={"B": "desk_point"}),
    dict(s="B", t="Sofia, I'd like you to lead the team. With the promotion Martin wanted.", e={"B": "happy"}, p={"B": "desk_explain"}),
    dict(shot="ceo_S", s="S", t="I'd be honored. Thank you.", e={"S": "happy"}, p={"S": "chest"}),
    dict(shot="ceo_M", s="M", t="Fine. Can I at least send a goodbye email? Just to Greg.", e={"M": "sad"}, p={"M": "phone"}, prop={"M": "phone"},
         say="[bitter] Fine. Can I at least send a goodbye email? Just to Greg."),
    dict(shot="inbox_end", s="M", t="Greg. Honestly, this company never deserved me. Send.", e={"M": "smug"}, sfx=[("whoosh", 0.2), ("ding", 1.4), ("ding", 2.4)],
         say="[smug, typing] Greg. Honestly, this company never deserved me. Send."),
    dict(shot="ceo_B", s="B", t="Martin. Check the recipients.", e={"B": "smug"}, p={"B": "desk"}, cam="med",
         say="[dry] Martin... check the recipients."),
    dict(shot="ceo_M", s="M", t="All staff? Again?", e={"M": "shocked"}, p={"M": "head"}, cam="close", punch=True,
         say="[devastated] All staff? AGAIN?", gap=0.8),
]
