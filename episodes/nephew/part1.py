"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_M", s="M", t="Emma! Come in, come in. Big news today.", e={"M": "happy", "E": "happy"},
         p={"M": "desk_explain", "E": "idle"}),
    dict(shot="office_E", s="E", t="Is it about the team lead position? You said it was mine.", e={"E": "happy"},
         p={"E": "chest"}, say="[hopeful] Is it about the team lead position? You said it was mine."),
    dict(shot="office_M", s="M", t="Funny you mention that. I gave it to Tyler.", e={"M": "smug"}, p={"M": "desk"},
         say="[casually] Funny you mention that. I gave it to Tyler."),
    dict(shot="office_E", s="E", t="Tyler? Your nephew? He started three weeks ago!", e={"E": "shocked"}, p={"E": "shrug"},
         punch=True, say="[shocked] Tyler? Your NEPHEW? He started three weeks ago!"),
    dict(shot="office_M", s="M", t="He has leadership energy. You can't teach that.", e={"M": "smug"}, p={"M": "desk_point"}),
    dict(shot="office_E", s="E", t="He called our biggest client bro. On the phone. Yesterday.", e={"E": "annoyed"}, p={"E": "cross"},
         say="[dryly] He called our biggest client bro. On the phone. Yesterday."),
    dict(shot="office_M", s="M", t="Exactly. Confidence!", e={"M": "happy"}, p={"M": "desk_explain"},
         say="[enthusiastic] Exactly. Confidence!"),
    dict(shot="office_ME", s="E", t="Mark, I've been here six years. I trained half of this office.", e={"E": "angry", "M": "annoyed"},
         p={"E": "explain", "M": "desk"}),
    dict(s="M", t="And now you'll train Tyler too. Family first, Emma.", e={"M": "smug"}, p={"M": "desk_point"}, cam="med",
         say="[smugly] And now you'll train Tyler too. Family first, Emma."),
    dict(shot="open_T", s="T", t="Yo, Emma! Guess who's your new boss?", e={"T": "happy", "E": "annoyed"}, p={"T": "point"},
         say="[cocky] Yo, Emma! Guess who's your new boss?", gap=0.3),
    dict(shot="open_E", s="E", t="I heard.", e={"E": "annoyed"}, p={"E": "cross"}),
    dict(shot="open_T", s="T", t="So, I'm presenting the Henderson deal on Monday. Big moves.", e={"T": "smug"}, p={"T": "explain"}),
    dict(shot="open_E", s="E", t="Do you even know who Mrs. Henderson is?", e={"E": "neutral"}),
    dict(shot="open_T", s="T", t="Some rich lady?", e={"T": "confused"}, p={"T": "shrug"}),
    dict(shot="open_E", s="E", t="She's the client who pays forty percent of everyone's salary in this building.", e={"E": "annoyed"},
         p={"E": "explain"}),
    dict(shot="open_T", s="T", t="Relax. I'll just wing it.", e={"T": "smug"}, p={"T": "hips"}, say="[confident] Relax. I'll just wing it."),
    dict(shot="open_MTE", s="M", t="Emma, give Tyler your presentation files.", e={"M": "neutral", "T": "smug", "E": "shocked"},
         p={"M": "point", "T": "cross", "E": "idle"}),
    dict(s="E", t="The files I worked on for three months?", e={"E": "shocked"}, p={"E": "chest"}),
    dict(s="M", t="He's the team lead now.", e={"M": "smug"}, p={"M": "shrug"}),
    dict(s="E", t="Okay. Good luck on Monday, Tyler.", e={"E": "smug"}, p={"E": "idle"}, cam="med",
         say="[calmly] Okay. Good luck on Monday, Tyler.", gap=0.4),
    dict(shot="open_E", beat=0.8, p={"E": "phone"}, prop={"E": "phone"}, e={"E": "neutral"}, sfx=[("ding", 0.0)]),
    dict(s="R", t="Hi, is this Emma Clarke? I'm calling from Brightline Consulting. We'd love to talk to you.", fx="phone",
         say="[friendly, professional] Hi, is this Emma Clarke? I'm calling from Brightline Consulting. We'd love to talk to you."),
    dict(s="E", t="Brightline? Perfect timing.", e={"E": "smug"}, cam="close", say="[slowly smiling] Brightline? Perfect timing.",
         gap=0.8),
]
