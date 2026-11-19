"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 2"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="lobby2", s="G", t="Jake? Is that you? Aren't you dying in bed?", e={"G": "shocked", "J": "shocked"},
         say="[shocked] Jake? Is that you? Aren't you dying in bed?"),
    dict(s="J", t="Gary? Aren't you in Chicago? With no signal?", e={"J": "smug"}, say="[smug] Gary? Aren't you in Chicago? With no signal?"),
    dict(shot="gcouch", s="G", t="The flight got, uh, cancelled.", e={"G": "worried"}, p={"G": "game"}, prop={"G": "controller"},
         say="[nervous] The flight got... uh... cancelled."),
    dict(shot="jcouch", s="J", t="My cold got, uh, better.", e={"J": "smug"}, p={"J": "game"}, prop={"J": "controller"}, say="[fake cough] My cold got... uh... better."),
    dict(shot="gcouch", s="G", t="Okay. Deal. You saw nothing. I saw nothing.", e={"G": "worried"}),
    dict(shot="jcouch", s="J", t="Deal. Now, are we doing this heist or not?", e={"J": "happy"}, gap=0.4),
    dict(shot="lobby2", s="J", t="Gary, you're driving into the ocean.", e={"J": "annoyed"}, say="[deadpan] Gary. You're driving into the ocean."),
    dict(s="G", t="Which button is brake? Why does this controller have so many buttons?", e={"G": "worried"},
         say="[panicking] Which button is brake? Why does this controller have so many buttons?"),
    dict(shot="gcouch", s="G", t="I think I just robbed the wrong bank.", e={"G": "confused"}, p={"G": "head"}, say="[confused] I think I just robbed the wrong bank."),
    dict(shot="jcouch", s="J", t="Real adults don't play video games, huh?", e={"J": "smug"}, cam="med", say="[laughing] Real adults don't play video games, huh?"),
    dict(shot="gcouch", s="G", t="Just carry me through this mission and we never speak of it.", e={"G": "sad"}, p={"G": "pray"}),
    dict(shot="lobby3_join", s="P", t="Hey, team! Mind if I join your heist?", e={"P": "happy"}, sfx=[("ding", 0.0)],
         say="[cheerful, through headset] Hey, team! Mind if I join your heist?"),
    dict(shot="jcouch", s="J", t="Gary. Look at the name.", e={"J": "shocked"}, look={"J": "up"}),
    dict(shot="gcouch", s="G", t="CEO Pamela?", e={"G": "shocked"}, cam="close", punch=True, say="[terrified whisper] CEO... Pamela?", gap=0.8),
]
