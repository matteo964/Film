"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="s_JG", s="G", t="Jake? Is that you? Aren't you dying in bed?", e={"G": "shocked", "J": "shocked", "C": "neutral"},
         p={"G": "point", "J": "idle", "C": "idle"}, say="[shocked] Jake? Is that you? Aren't you dying in bed?"),
    dict(s="J", t="Gary? Aren't you in Chicago? With no signal?", e={"J": "smug"}, say="[smug] Gary? Aren't you in Chicago? With no signal?"),
    dict(s="G", t="The flight got, uh, cancelled.", e={"G": "worried"}, p={"G": "shrug"}, say="[nervous] The flight got... uh... cancelled."),
    dict(s="J", t="My cold got, uh, better.", e={"J": "smug"}, say="[fake cough] My cold got... uh... better."),
    dict(s="G", t="Okay. Deal. You saw nothing. I saw nothing.", e={"G": "worried"}, p={"G": "stop"}),
    dict(s="J", t="Deal.", e={"J": "happy"}, gap=0.4),
    dict(shot="s_C", s="C", t="Alright. Good news and bad news. This is the very last copy.", e={"C": "smug"}, p={"C": "point"}),
    dict(shot="s_G", s="G", t="I'll take it. I'm his boss. Bosses go first.", e={"G": "smug"}, p={"G": "chest"},
         say="[pushy] I'll take it. I'm his boss. Bosses go first."),
    dict(shot="s_J", s="J", t="Real adults don't play video games, Gary. Your words.", e={"J": "smug"}, p={"J": "cross"},
         say="[mocking] Real adults don't play video games, Gary. Your words."),
    dict(shot="s_C", s="C", t="Sorry, sir. He pre-ordered it two years ago. You didn't.", e={"C": "smug"}),
    dict(shot="s_G", s="G", t="I'll pay double! Triple! Cash!", e={"G": "worried"}, p={"G": "explain"}, say="[desperate] I'll pay double! Triple! Cash!"),
    dict(shot="s_C", s="C", t="Pre-order rules, sir. Even for bosses.", e={"C": "smug"}, p={"C": "cross"}),
    dict(shot="s_G", s="G", t="Jake. I'll give you a raise. Right now. For that copy.", e={"G": "smug"}, p={"G": "point"}),
    dict(shot="s_J", s="J", t="You told me last month there's no budget for raises.", e={"J": "smug"}, p={"J": "cross"},
         say="[dry] You told me last month there's no budget for raises."),
    dict(shot="s_Jbox", s="J", t="Twelve years. Finally.", e={"J": "happy"}, p={"J": "tablet"}, sfx=[("ding", 0.0)],
         say="[emotional whisper] Twelve years. Finally."),
    dict(shot="s_G", s="G", t="Jake. Buddy. Can I at least come over and watch you play?", e={"G": "sad"}, p={"G": "pray"},
         say="[pleading] Jake. Buddy. Can I at least come over and watch you play?"),
    dict(shot="s_J", s="J", t="On one condition. Next year, I get release day off. Officially.", e={"J": "smug"}, p={"J": "point"}),
    dict(shot="s_G", s="G", t="Fine! Deal! Just let me watch!", e={"G": "worried"}, p={"G": "panic"}, say="[desperate] Fine! Deal! Just let me watch!"),
    dict(shot="s_JGP", s="P", t="Gary? Jake? Is that you two?", e={"P": "happy", "G": "shocked", "J": "shocked"}, p={"P": "explain", "G": "idle", "J": "idle"},
         say="[cheerful, from behind] Gary? Jake? Is that you two?"),
    dict(s="J", t="Gary. Turn around.", e={"J": "shocked"}, look={"J": "away"}),
    dict(s="G", t="Pamela? The CEO?", e={"G": "shocked"}, cam="close", punch=True, say="[terrified whisper] Pamela? The... CEO?", gap=0.8),
]
