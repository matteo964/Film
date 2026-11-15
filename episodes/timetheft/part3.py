"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="rep_OT", s="O", t="So. The first company wide WorkWatch report. Thank you for the idea, Trent.", e={"O": "neutral", "T": "smug", "N": "calm"},
         p={"O": "explain", "T": "chest"}, look={"O": "up"}, sfx=[("ding", 0.0)]),
    dict(s="T", t="My pleasure, sir. As you can see, I'm one hundred percent active.", e={"T": "smug"}, p={"T": "point"}, look={"T": "up"}),
    dict(shot="rep_O", s="O", t="Nora Kim. A hundred and twelve percent. Fourteen hours of unpaid overtime this month.", e={"O": "happy"}, look={"O": "up"}),
    dict(s="O", t="And Trent tells me she's guilty of time theft. For an eleven minute bathroom break.", e={"O": "annoyed"}, look={"O": None}, cam="med"),
    dict(shot="rep_T", s="T", t="Rules are rules, sir.", e={"T": "smug"}, p={"T": "shrug"}),
    dict(shot="rep_O", s="O", t="I agree. So let's look at your webcam snapshots.", e={"O": "smug"}, look={"O": "up"}),
    dict(shot="rep_ONT", s="O", t="One oh five. Empty chair. Two thirty. Empty chair. Four ten. Empty chair.", e={"O": "annoyed", "T": "shocked", "N": "smug"},
         p={"O": "point", "T": "idle", "N": "cross"}, look={"O": "up"}),
    dict(s="T", t="I was working remotely!", e={"T": "worried"}, p={"T": "panic"}, say="[desperate] I was working remotely!"),
    dict(s="N", t="From the golf course? Your report is forty pages of the letter A.", e={"N": "smug"}, p={"N": "point"},
         say="[dry] From the golf course? Your report is forty pages of the letter A."),
    dict(shot="rep_T", s="T", t="That's a draft!", e={"T": "worried"}, p={"T": "chest"}, say="[squeaky] That's a DRAFT!"),
    dict(shot="rep_O", s="O", t="Six hours, a mouse jiggler, and a tee time. That's called time theft, Trent.", e={"O": "angry"}, p={"O": "point"}, cam="med",
         say="[cold] Six hours. A mouse jiggler. And a tee time. That's called time theft, Trent."),
    dict(s="O", t="You're done here. Effective immediately.", e={"O": "angry"}),
    dict(shot="rep_N", s="O", t="Nora, your overtime gets paid. All fourteen hours. And WorkWatch is uninstalled. For everyone.", e={"O": "happy", "N": "happy"},
         p={"N": "chest"}),
    dict(s="N", t="Thank you. We'd rather be trusted than watched.", e={"N": "happy"}, p={"N": "idle"}),
    dict(shot="rep_OT", s="T", t="Before I pack up, can I quickly use the bathroom?", e={"T": "sad", "O": "smug"}, p={"T": "pray", "O": "cross"},
         say="[defeated] Before I pack up... can I quickly use the bathroom?"),
    dict(shot="rep_N", s="N", t="Sure, Trent. But make it quick. The clock is running.", e={"N": "smug"}, p={"N": "hips"}, cam="close",
         say="[sweetly] Sure, Trent. But make it quick. The clock is running.", gap=0.8),
]
