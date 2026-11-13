"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="spk_G", s="G", t="That's not mine! That's a template. For my nephew's school project.",
         e={"G": "shocked", "P": "smug", "H": "angry", "M": "smug", "N": "smug", "T": "smug"}, p={"G": "panic"},
         say="[panicking] That's not mine! That's a template. For my nephew's school project."),
    dict(shot="spk_T", s="T", t="A school project about a yacht called Bonus Season?", e={"T": "smug"},
         say="[sarcastic] A school project about a yacht called Bonus Season?"),
    dict(shot="spk_H", s="H", t="Gordon, you told me the raise pool was frozen. Why is it funding your bonus?", e={"H": "angry"}),
    dict(shot="spk_G", s="G", t="Great meeting, everyone! Thanks for coming! Bye!", e={"G": "worried"}, p={"G": "stop"},
         say="[fast, nervous] Great meeting, everyone! Thanks for coming! Bye!", sfx=[("whoosh", 1.6)], gap=0.6),
    dict(shot="office_GP", s="G", t="Priya. Close the door. I know you took a screenshot.", e={"G": "angry", "P": "calm"},
         p={"G": "desk_point", "P": "cross"}),
    dict(shot="office_P", s="P", t="A hundred and forty people saw it live, Gordon.", e={"P": "calm"}),
    dict(shot="office_G", s="G", t="Do you have any idea what I do for this company?", e={"G": "angry"}, p={"G": "desk_explain"}),
    dict(shot="office_P", s="P", t="Based on your screen? Mostly yacht shopping.", e={"P": "smug"}, say="[dryly] Based on your screen? Mostly yacht shopping."),
    dict(shot="office_G", s="G", t="Delete it. Or you're fired.", e={"G": "angry"}, p={"G": "desk_point"}, cam="med",
         say="[threatening] Delete it. Or you're fired."),
    dict(shot="office_P", s="P", t="Fired for what? Watching a meeting you invited me to?", e={"P": "smug"}, p={"P": "shrug"}),
    dict(shot="office_G", s="G", t="For leaking confidential company data!", e={"G": "angry"}, p={"G": "desk_lean"},
         say="[shouting] For leaking confidential company data!"),
    dict(shot="office_P", s="P", t="You leaked it, Gordon. On your own screen.", e={"P": "smug"}, p={"P": "point"}),
    dict(shot="office_G", s="G", t="I'm the CEO. Nobody in this building can touch me.", e={"G": "smug"}, p={"G": "desk_explain"},
         say="[arrogant] I'm the CEO. Nobody in this building can touch me."),
    dict(shot="office_P_mail", s="P", t="Actually, someone can. I just got an email.", e={"P": "neutral"}, p={"P": "phone"},
         prop={"P": "phone"}, sfx=[("ding", 0.3)], say="[looking at phone] Actually... someone can. I just got an email."),
    dict(s="P", t="Emergency board meeting. Today at noon. Agenda, executive compensation.", e={"P": "smug"}),
    dict(shot="office_G", s="G", t="The board? How would the board even know?", e={"G": "shocked"}, p={"G": "desk_lean"}, punch=True),
    dict(shot="office_P", s="P", t="They were in the call too, Gordon.", e={"P": "smug"}, prop={"P": None}, cam="close",
         say="[quietly] They were in the call too, Gordon.", gap=0.8),
]
