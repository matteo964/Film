"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="office_TA", s="T", t="Ava. Sit down. We need to talk about your vacation.", e={"T": "annoyed", "A": "happy"},
         p={"T": "desk", "A": "idle"}),
    dict(s="A", t="Sure! I fly to Italy tomorrow morning. My sister's wedding is on Saturday.", e={"A": "happy"},
         p={"A": "explain"}, say="[excited] Sure! I fly to Italy tomorrow morning. My sister's wedding is on Saturday!"),
    dict(s="T", t="Yeah. About that. Your vacation is cancelled.", e={"T": "smug"}, p={"T": "desk_point"}, cam="med",
         say="[flatly] Yeah. About that. Your vacation is cancelled."),
    dict(s="A", t="Cancelled? You approved it six months ago!", e={"A": "shocked"}, p={"A": "chest"}, punch=True),
    dict(s="T", t="The Morgan presentation got moved to Friday. And you're the only one who knows that account.",
         e={"T": "neutral"}, p={"T": ["desk_explain", "desk"]}),
    dict(s="A", t="Todd, I'm the maid of honor. I'm giving the speech.", e={"A": "worried"}, p={"A": "pray"}),
    dict(s="T", t="Approvals can be un-approved. That's how management works.", e={"T": "smug"}, p={"T": "desk_lean"},
         say="[smugly] Approvals can be UN-approved. That's how management works."),
    dict(s="A", t="I have the approval email right here. Signed by you and HR.", e={"A": "annoyed"}, p={"A": "phone"},
         prop={"A": "phone"}),
    dict(s="T", t="I don't care about an email. If you get on that plane, don't bother coming back.", e={"T": "angry"},
         p={"T": "desk_point"}, prop={"A": None}),
    dict(s="A", t="Is that a threat?", e={"A": "angry"}, p={"A": "hips"}, cam="med"),
    dict(s="T", t="It's a promise. Your job or your sister's wedding. Choose.", e={"T": "smug"}, p={"T": "desk_lean"},
         say="[coldly] It's a promise. Your job, or your sister's wedding. Choose."),
    dict(s="A", t="I choose the wedding.", e={"A": "calm"}, p={"A": "idle"}, cam="close",
         say="[calmly, without hesitation] I choose the wedding."),
    dict(s="T", t="Then you're fired!", e={"T": "angry"}, p={"T": "desk_point"}, punch=True, say="[shouting] Then you're FIRED!"),
    dict(s="A", t="Could you put that in writing for me?", e={"A": "calm"}, p={"A": "explain"}),
    dict(s="T", t="With pleasure.", e={"T": "smug"}, p={"T": "desk"}, say="[smugly] With pleasure.", sfx=[("whoosh", 0.9)]),
    dict(s="T", t="There. Fired for abandoning the company before the Morgan presentation. Signed and dated.",
         p={"T": "desk_explain"}),
    dict(s="A", t="Perfect. Thank you, Todd.", e={"A": "smug"}, p={"A": "paper"}, prop={"A": "paper:FIRED"}),
    dict(s="T", t="Don't thank me. Enjoy unemployment.", e={"T": "smug"}, p={"T": "desk_lean"}),
    dict(s="A", t="Oh, and Todd? Good luck on Friday. Mr. Morgan always has a lot of questions.", e={"A": "smug"},
         cam="close", say="[sweetly] Oh, and Todd? Good luck on Friday. Mr. Morgan ALWAYS has a lot of questions.", gap=0.8),
]
