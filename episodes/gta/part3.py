"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="lobby3", s="P", t="Gary? Jake? Is that you two? What a coincidence!", e={"P": "happy", "G": "shocked", "J": "worried"},
         say="[cheerful] Gary? Jake? Is that you two? What a coincidence!"),
    dict(shot="gcouch", s="G", t="Pamela! I can explain. Jake called in sick and I was just, uh, checking on him.", e={"G": "worried"},
         p={"G": "game"}, prop={"G": "controller"}, say="[panicking] Pamela! I can explain. Jake called in sick and I was just... uh... checking on him."),
    dict(shot="jcouch", s="J", t="In a bank heist?", e={"J": "smug"}, p={"J": "game"}, prop={"J": "controller"}, say="[dry] In a bank heist?"),
    dict(shot="pam_couch", s="P", t="Why would Jake call in sick? I gave the whole company the day off today.", e={"P": "confused"}, p={"P": "game"},
         prop={"P": "controller"}),
    dict(shot="jcouch", s="J", t="You did what?", e={"J": "shocked"}, punch=True),
    dict(shot="email", s="P", t="I sent an email yesterday. Paid day off for release day. Managers, please forward this to your teams.",
         e={"P": "neutral"}, sfx=[("ding", 0.0)]),
    dict(shot="pam_couch", s="P", t="Gary. Did you forward it?", e={"P": "annoyed"}, cam="med", say="[slowly] Gary. Did you forward it?"),
    dict(shot="gcouch", s="G", t="My email might have been a little broken yesterday.", e={"G": "worried"}, p={"G": "shrug"},
         say="[squeaky] My email might have been... a little broken yesterday."),
    dict(shot="jcouch", s="J", t="He told us real adults don't play video games. And that nobody takes off today.", e={"J": "angry"}),
    dict(shot="pam_couch", s="P", t="So you made your team work. While you played at home. And told them you were in Chicago.", e={"P": "angry"},
         p={"P": "point"}),
    dict(s="P", t="Gary, you're working the weekend shift. For the next month.", e={"P": "smug"}, cam="med"),
    dict(shot="gcouch", s="G", t="The weekend? But I just bought the game!", e={"G": "shocked"}, p={"G": "head"}, punch=True,
         say="[devastated] The WEEKEND? But I just bought the game!"),
    dict(shot="pam_couch", s="P", t="Jake, your sick day is now a paid day off. And take tomorrow off too.", e={"P": "happy"}),
    dict(shot="jcouch", s="J", t="Best CEO ever.", e={"J": "happy"}, say="[thrilled] Best CEO ever."),
    dict(shot="gcouch", s="G", t="Can I at least finish this heist with you guys?", e={"G": "sad"}, p={"G": "pray"},
         say="[pleading] Can I at least finish this heist with you guys?"),
    dict(shot="kick", s="P", t="Sorry, Gary. Real adults don't play video games.", e={"P": "smug"}, sfx=[("whoosh", 1.5)],
         say="[sweetly] Sorry, Gary. Real adults don't play video games.", gap=0.8),
]
