"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="open_MS", s="S", t="Martin. Check your sent folder.", e={"S": "angry", "M": "confused"}, p={"S": "cross", "M": "mug"},
         prop={"M": "mug"}),
    dict(s="M", t="My sent folder? Why would I-", e={"M": "confused"}, look={"M": "down"}),
    dict(shot="mail_send", s="M", t="All staff? Three hundred and twelve recipients?", e={"M": "shocked"},
         say="[horrified whisper] All staff? Three hundred and twelve recipients?"),
    dict(s="M", t="Okay. Okay. Don't panic. I'll just recall it.", say="[panicking] Okay. Okay. Don't panic. I'll just recall it."),
    dict(shot="recall", s="M", t="Recall failed? Two hundred eighty seven people already read it?", e={"M": "shocked"},
         sfx=[("alarm", 0.8)], say="[desperate] Recall failed? Two hundred eighty seven people already read it?"),
    dict(shot="open_M", s="M", t="Kevin! IT emergency! Can you delete one email from everyone's inbox?", e={"M": "shocked"},
         p={"M": "phone"}, prop={"M": "phone"}, say="[frantic] Kevin! IT emergency! Can you delete one email from everyone's inbox?"),
    dict(s="K", t="Sure, Martin. If you have a time machine.", fx="phone", say="[deadpan] Sure, Martin. If you have a time machine."),
    dict(shot="recall", s="M", t="Okay. Plan B.", e={"M": "worried"}, prop={"M": None}, say="[muttering] Okay. Plan B."),
    dict(s="M", t="Fine. I'll just tell everyone I got hacked.", say="[scheming, panicked] Fine. I'll just tell everyone I got hacked.",
         gap=0.4),
    dict(shot="inbox2", s="J", t="Hacked by who? Your honesty?", e={"J": "smug"}, sfx=[("ding", 1.3), ("ding", 2.4)],
         say="[reading aloud, laughing] Hacked by who? Your honesty?"),
    dict(s="S", t="I just replied all too. With my original file. Created by Sofia Ramos. August second.", e={"S": "smug"},
         sfx=[("ding", 0.5)]),
    dict(s="J", t="Dave from Ops just asked to be removed from the list. For the fourth time.", e={"J": "happy"},
         say="[cracking up] Dave from Ops just asked to be removed from the list. For the fourth time."),
    dict(s="J", t="Oh, and Anna from HR would like a word. Publicly. In the thread.", e={"J": "smug"}),
    dict(s="M", t="HR? Already?", e={"M": "shocked"}, say="[panicked] HR? ALREADY?"),
    dict(s="M", t="Why is my inbox still going? A hundred replies? Two hundred?", e={"M": "shocked"},
         say="[spiraling] Why is my inbox still going? A hundred replies? Two hundred?"),
    dict(s="J", t="Uh, Martin. Top of your inbox.", e={"J": "shocked"}, sfx=[("ding", 0.0)]),
    dict(shot="open_M", s="M", t="Victoria Brennan. The CEO. Martin. My office. Now.", e={"M": "shocked"}, p={"M": "head"}, prop={"M": None},
         cam="close", punch=True, say="[reading, terrified] Victoria Brennan. The CEO. 'Martin. My office. Now.'", gap=0.8),
]
