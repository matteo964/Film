"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="baby_EW", s="W", t="Say hi to your daughter, Ethan.", e={"W": "happy", "E": "happy"}, p={"W": "lap", "E": "tablet"},
         say="[soft, emotional] Say hi to your daughter, Ethan."),
    dict(s="E", t="Hi, Lily. I'm your dad. I'm never missing a moment.", e={"E": "happy"}, say="[whispering, emotional] Hi, Lily. I'm your dad. I'm never missing a moment."),
    dict(shot="baby_TE", s="T", t="Excuse me. Ethan? I'm Keiko Tanaka. We met an hour ago.", e={"T": "happy", "E": "shocked"}, p={"T": "chest"}),
    dict(s="E", t="Mrs. Tanaka? What are you doing here?", e={"E": "confused"}),
    dict(s="T", t="I came to congratulate you. And to offer you something.", e={"T": "happy"}, p={"T": "explain"}),
    dict(shot="hosp_T", s="T", t="We'll sign the partnership. But only if you lead our account.", e={"T": "smug"}, p={"T": "point"}),
    dict(shot="hosp_E", s="E", t="I don't work there anymore. My boss fired me an hour ago.", e={"E": "sad"}),
    dict(shot="hosp_T", s="T", t="I called your CEO on the way. You're rehired. With six weeks of paid leave. And a promotion.", e={"T": "happy"},
         p={"T": "phone"}, prop={"T": "phone"}, cam="med"),
    dict(shot="hosp_E", s="E", t="A promotion? To what?", e={"E": "shocked"}, punch=True),
    dict(shot="hosp_T", s="T", t="Doug's job.", e={"T": "smug"}, prop={"T": None}, say="[dry, satisfied] Doug's job.", gap=0.4),
    dict(shot="baby_DE", s="D", t="Ethan! Buddy! Congratulations! Beautiful baby! Listen, about that text.", e={"D": "worried", "E": "calm"},
         p={"D": "explain"}, say="[nervous, fake cheerful] Ethan! Buddy! Congratulations! Beautiful baby! Listen, about that text..."),
    dict(s="D", t="Can we talk for five minutes? Just a quick meeting?", e={"D": "worried"}, p={"D": "pray"}),
    dict(shot="hosp_E", s="E", t="Sorry, Doug. I'm already in a very important meeting.", e={"E": "smug"}, look={"E": "down"}, cam="med",
         say="[calm, looking at the baby] Sorry, Doug. I'm already in a very important meeting."),
    dict(s="E", t="And nobody leaves this meeting.", e={"E": "happy"}, cam="close", say="[softly, smiling] And nobody leaves this meeting.", gap=0.8),
]
