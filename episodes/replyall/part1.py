"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="open_SJ_plain", s="J", t="Did you see the invite for the team building retreat? Martin says it's for bonding.",
         e={"J": "smug", "S": "neutral"}, p={"J": "explain", "S": "idle"}),
    dict(s="S", t="Martin hasn't bonded with anyone since twenty nineteen.", e={"S": "smug"}, p={"S": "cross"},
         say="[dryly] Martin hasn't bonded with anyone since twenty nineteen."),
    dict(s="S", t="I just hope my Q3 project finally gets noticed in the promotion review.", e={"S": "worried"}, p={"S": "chest"}),
    dict(s="J", t="Didn't Martin promise he'd present it with your name on it?", e={"J": "neutral"}),
    dict(s="S", t="Full credit. His words.", e={"S": "happy"}, say="[hopeful] Full credit. His words.", gap=0.4),
    dict(shot="desk_M", s="M", t="Okay. Quick email to Greg before the meeting. Just between us.", e={"M": "smug"}, p={"M": "type"},
         say="[smug, to himself] Okay. Quick email to Greg before the meeting. Just between us."),
    dict(shot="mail_typing", s="M", t="Greg. Between us. The team building retreat is just so I can pick who to lay off.",
         e={"M": "smug"}, say="[typing, smug] Greg. Between us... the team building retreat is just so I can pick who to lay off."),
    dict(s="M", t="And I'm presenting Sofia's project as mine in my promotion review.", say="[chuckling] And I'm presenting Sofia's project as mine in my promotion review."),
    dict(s="M", t="LOL. These people will believe anything.", say="[laughs] LOL. These people will believe anything.", gap=0.5),
    dict(shot="mail_replyall", s="M", t="Reply. And send.", e={"M": "smug"}, say="[clicking, confident] Reply... and send.", gap=0.3),
    dict(shot="mail_send", beat=2.6, sfx=[("whoosh", 0.4), ("ding", 1.2)]),
    dict(shot="open_SJ", s="J", t="Uh. Did everyone just get an email from Martin?", e={"J": "shocked", "S": "neutral"},
         p={"J": "phone", "S": "idle"}, prop={"J": "phone"}, say="[confused] Uh... did everyone just get an email from Martin?"),
    dict(s="J", t="The team building retreat is just so I can pick who to lay off?", e={"J": "shocked"}, look={"J": "down"},
         say="[reading, shocked] The team building retreat is just so I can pick who to LAY OFF?"),
    dict(shot="open_S", s="S", t="Wait. I'm presenting Sofia's project as mine?", e={"S": "shocked"}, p={"S": "phone"}, prop={"S": "phone"},
         look={"S": "down"}, punch=True, say="[stunned] Wait... I'm presenting SOFIA'S project as mine?"),
    dict(s="S", t="That's my project. I worked on it for four months.", e={"S": "angry"}, look={"S": None}, prop={"S": None}, p={"S": "chest"}),
    dict(shot="open_J", s="J", t="And he sent it to all three hundred and twelve of us. Including the CEO.", e={"J": "smug"},
         prop={"J": None}, p={"J": "explain"}),
    dict(shot="open_M", s="M", t="Morning, team! Big day. Why is everyone so quiet?", e={"M": "happy"}, p={"M": "mug"}, prop={"M": "mug"},
         say="[cheerful, oblivious] Morning, team! Big day. Why is everyone so quiet?"),
    dict(s="M", t="Why is everyone looking at me like that?", e={"M": "confused"}, cam="close",
         say="[uneasy] Why is everyone looking at me like that?", gap=0.8),
]
