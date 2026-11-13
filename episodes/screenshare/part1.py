"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="grid", s="G", t="Morning, team. Can everyone hear me? Great. I'll keep this short.",
         e={"G": "smug", "P": "neutral", "H": "neutral", "M": "neutral", "N": "neutral", "T": "neutral"}, p={"G": "explain"}),
    dict(shot="spk_G", s="G", t="It's been a tough year. So there will be no raises. And no bonuses.", e={"G": "sad"},
         say="[fake sympathy] It's been a tough year. So there will be no raises. And no bonuses."),
    dict(s="G", t="We all need to make sacrifices. Also, office coffee is now two dollars.", e={"G": "smug"}, p={"G": "shrug"},
         say="[smugly] We all need to make sacrifices. Also... office coffee is now two dollars."),
    dict(shot="grid", s="P", t="Sorry, Gordon. Didn't we just announce record revenue last month?", e={"P": "confused", "M": "annoyed",
         "N": "annoyed", "T": "annoyed"}, p={"P": "explain"}),
    dict(shot="spk_G", s="G", t="Revenue isn't profit, Priya. Let me show you the numbers. Sharing my screen.", e={"G": "annoyed"},
         p={"G": "point"}),
    dict(shot="share_slides", s="G", t="As you can see, a very tough year. Very sad chart.", e={"G": "sad"}, sfx=[("ding", 0.0)],
         say="[dramatic] As you can see. A very tough year. Very sad chart."),
    dict(s="G", t="Hold on. Let me find the second slide.", e={"G": "neutral"}, say="[distracted] Hold on. Let me find the second slide...",
         gap=0.4),
    dict(shot="share_yacht", s="T", t="Wait. Is that a yacht?", e={"T": "shocked"}, sfx=[("ding", 0.0)],
         say="[whispering, shocked] Wait... is that a yacht?"),
    dict(s="G", t="Where is that chart? Wrong window.", e={"G": "confused"}, say="[muttering] Where is that chart... wrong window."),
    dict(shot="share_bonus", s="G", t="There we go. As I said, we're all making sacrifices this year.", e={"G": "smug"},
         say="[confident, oblivious] There we go. As I said... we're all making sacrifices this year."),
    dict(s="H", t="Gordon. Please stop sharing.", e={"H": "angry"}, say="[urgent, British] Gordon. Please stop sharing."),
    dict(shot="spk_G", s="G", t="Why is everyone so quiet? Did my microphone freeze?", e={"G": "confused"}, p={"G": "shrug"},
         say="[oblivious] Why is everyone so quiet? Did my microphone freeze?"),
    dict(shot="spk_P", s="P", t="Gordon. You're still sharing your screen. We can all see your bonus.", e={"P": "smug"}, cam="med",
         say="[calm, slowly] Gordon... you're still sharing your screen. We can all see your bonus.", gap=0.8),
]
