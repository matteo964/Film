"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="s_JGP", s="P", t="Gary? Jake? What a coincidence!", e={"P": "happy", "G": "shocked", "J": "worried"},
         p={"P": "explain", "G": "idle", "J": "idle"}, say="[cheerful] Gary? Jake? What a coincidence!"),
    dict(s="G", t="Pamela! I can explain. Jake called in sick and I was just, uh, checking on him.", e={"G": "worried"}, p={"G": "shrug"},
         say="[panicking] Pamela! I can explain. Jake called in sick and I was just... uh... checking on him."),
    dict(s="J", t="In a game store? At eight a.m.?", e={"J": "smug"}, say="[dry] In a game store? At eight a.m.?"),
    dict(shot="s_P", s="P", t="Why would Jake call in sick? I gave the whole company the day off today.", e={"P": "confused"}, p={"P": "shrug"}),
    dict(shot="s_J", s="J", t="You did what?", e={"J": "shocked"}, punch=True, look={"J": None}),
    dict(shot="email_store", s="P", t="I sent an email yesterday. Paid day off for release day. Managers, please forward this to your teams.",
         e={"P": "neutral"}, sfx=[("ding", 0.0)]),
    dict(shot="s_P", s="P", t="Gary. Did you forward it?", e={"P": "annoyed"}, cam="med", say="[slowly] Gary. Did you forward it?"),
    dict(shot="s_G", s="G", t="My email might have been a little broken yesterday.", e={"G": "worried"}, p={"G": "shrug"},
         say="[squeaky] My email might have been... a little broken yesterday."),
    dict(shot="s_J", s="J", t="He told us real adults don't play video games. And that nobody takes off today.", e={"J": "angry"}, p={"J": "point"}),
    dict(shot="s_P", s="P", t="So you made your team work. While you stood in line for a game. And told them you were in Chicago.", e={"P": "angry"},
         p={"P": "point"}),
    dict(s="P", t="Gary, you're working the weekend shift. For the next two weeks.", e={"P": "smug"}, cam="med"),
    dict(shot="s_G", s="G", t="The weekend? But I didn't even get the game!", e={"G": "shocked"}, p={"G": "head"}, punch=True,
         say="[devastated] The WEEKEND? But I didn't even get the game!"),
    dict(shot="s_P", s="P", t="Jake, your sick day is now a paid day off. And take tomorrow off too.", e={"P": "happy"}),
    dict(shot="s_Jbox", s="J", t="Best CEO ever.", e={"J": "happy"}, p={"J": "tablet"}, say="[thrilled] Best CEO ever."),
    dict(shot="sold_G", s="G", t="Excuse me! Do you have any more copies? Anything?", e={"G": "sad"}, p={"G": "pray"},
         say="[desperate] Excuse me! Do you have any more copies? Anything?"),
    dict(shot="sold_C", s="C", t="Sold out, sir. Next shipment in two weeks.", e={"C": "smug"}, p={"C": "shrug"}, sfx=[("ding", 0.0)]),
    dict(shot="sold_GP", s="P", t="Perfect timing, Gary. That's exactly when your weekend shifts end.", e={"P": "smug", "G": "sad"},
         p={"P": "cross", "G": "idle"}, say="[sweetly] Perfect timing, Gary. That's exactly when your weekend shifts end."),
    dict(s="P", t="And remember. Real adults don't play video games.", e={"P": "smug"}, cam="close",
         say="[teasing] And remember... real adults don't play video games.", gap=0.8),
]
