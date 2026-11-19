"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="cold", s="G", t="Wait. Jake? Aren't you sick?", e={"G": "shocked", "J": "shocked"}, sfx=[("ding", 0.0)],
         say="[shocked, through headset] Wait... Jake? Aren't you SICK?"),
    dict(s="J", t="Gary? Aren't you at the client meeting in Chicago?", say="[stunned] Gary?? Aren't YOU at the client meeting in Chicago?", gap=0.3),
    dict(shot="night", beat=1.4, sfx=[("whoosh", 0.0)]),
    dict(shot="office_GJ", s="J", t="Gary, can I take tomorrow off? It's a really important day for me.", e={"J": "happy", "G": "annoyed"},
         p={"J": "pray", "G": "desk"}),
    dict(shot="office_G", s="G", t="Tomorrow? Let me guess. That video game comes out.", e={"G": "smug"}, p={"G": "desk_explain"}),
    dict(shot="office_J", s="J", t="I've been waiting for it for twelve years.", e={"J": "happy"}, p={"J": "chest"}),
    dict(shot="office_G", s="G", t="Grow up, Jake. Nobody takes off tomorrow. Real adults don't play video games.", e={"G": "smug"},
         p={"G": "desk_point"}, say="[condescending] Grow up, Jake. Nobody takes off tomorrow. Real adults don't play video games."),
    dict(s="G", t="Besides, I'm flying to Chicago. Client meeting. All day. Very important.", e={"G": "smug"}, p={"G": "desk_lean"}),
    dict(shot="open_JM", s="M", t="So? Are you coming in tomorrow?", e={"M": "smug", "J": "smug"}, p={"M": "cross", "J": "idle"}),
    dict(s="J", t="I feel a very bad cold coming on. Very sudden. Very contagious.", e={"J": "smug"}, p={"J": "chest"},
         say="[fake coughing, grinning] I feel a very bad cold coming on. Very sudden. Very contagious."),
    dict(shot="call_gary", s="J", t="Gary, I'm so sick. I can't even get out of bed.", e={"J": "sad"}, fx="phone",
         say="[dramatic fake cough, hoarse] Gary... I'm so sick. I can't even get out of bed."),
    dict(s="G", t="Fine. Get well soon. I'll be in Chicago all day anyway. No signal in the meeting.", e={"G": "neutral"}, fx="phone",
         say="[distracted, hurried] Fine. Get well soon. I'll be in Chicago all day anyway. No signal in the meeting.", gap=0.4),
    dict(shot="jcouch", s="J", t="Twelve years. Snacks ready. Energy drinks ready. Let's go.", e={"J": "happy"}, p={"J": "game"}, prop={"J": "controller"},
         say="[excited whisper] Twelve years. Snacks ready. Energy drinks ready. Let's GO."),
    dict(s="J", t="Okay. Online heist. I just need one more player.", e={"J": "smug"}, look={"J": "up"}),
    dict(shot="lobby2_join", s="G", t="Alright, rookie. Follow my lead. I've been waiting for this game for twelve years.", e={"G": "smug"},
         say="[confident, through headset] Alright, rookie. Follow my lead. I've been waiting for this game for twelve years."),
    dict(shot="jcouch", s="J", t="Wait. I know that voice.", e={"J": "shocked"}, cam="close", look={"J": "front"},
         say="[slowly, horrified] Wait... I know that voice.", gap=0.8),
]
