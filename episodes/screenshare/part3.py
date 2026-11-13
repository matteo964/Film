"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1], "Part 3"]
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="board_GA", s="A", t="Gordon. The board watched the recording. All of it.", e={"A": "annoyed", "G": "worried", "P": "calm", "H": "neutral"},
         p={"A": "cross", "G": "idle"}),
    dict(s="G", t="That was out of context! The yacht is for client meetings.", e={"G": "worried"}, p={"G": "explain"},
         say="[defensive] That was out of context! The yacht is for... client meetings."),
    dict(shot="board_A", s="A", t="A yacht named Bonus Season?", e={"A": "smug"}, say="[dry] A yacht named Bonus Season?"),
    dict(shot="board_G", s="G", t="It's a fun name.", e={"G": "worried"}, p={"G": "shrug"}, say="[weakly] It's a fun name."),
    dict(shot="board_H", s="H", t="He moved the entire raise pool into his own bonus. Without board approval.", e={"H": "angry"}, p={"H": "point"}),
    dict(shot="board_PA", s="A", t="Ms. Nair. You work in finance?", e={"A": "neutral", "P": "calm"}, p={"A": "explain", "P": "idle"}),
    dict(s="P", t="Junior analyst. I ran the numbers last night.", e={"P": "calm"}, p={"P": "point"}, look={"P": "up"}),
    dict(shot="board_P", s="P", t="Raises for all hundred and forty employees cost one point nine million. His bonus was two point four.",
         e={"P": "neutral"}, look={"P": "up"}),
    dict(s="P", t="We can pay every single raise. And still have half a million left over.", e={"P": "smug"}, look={"P": None}, cam="med"),
    dict(shot="board_A", s="A", t="Then that's exactly what we'll do.", e={"A": "happy"}, say="[decisive] Then that's exactly what we'll do."),
    dict(s="A", t="The board votes to cancel the bonus. And to remove you as CEO. Effective immediately.", e={"A": "angry"}, p={"A": "point"}),
    dict(shot="board_G", s="G", t="You can't do that! I built this company!", e={"G": "angry"}, p={"G": "panic"}, punch=True,
         say="[outraged] You can't do that! I BUILT this company!"),
    dict(shot="board_H", s="H", t="No, Gordon. A hundred and forty people built it. You just bought a boat.", e={"H": "smug"}, cam="med",
         say="[cutting] No, Gordon. A hundred and forty people built it. You just bought a boat."),
    dict(shot="board_PA", s="A", t="Ms. Nair, Helen needs a senior analyst. The job is yours if you want it.", e={"A": "happy", "P": "happy"},
         p={"A": "explain", "P": "idle"}),
    dict(s="P", t="I'd love that. Thank you.", e={"P": "happy"}, p={"P": "chest"}),
    dict(shot="board_GPA", s="G", t="But what about my yacht deposit?", e={"G": "sad", "P": "smug", "A": "neutral"}, p={"G": "pray", "P": "cross"},
         say="[pathetic] But... what about my yacht deposit?"),
    dict(s="P", t="We all need to make sacrifices, Gordon.", e={"P": "smug"}, cam="close",
         say="[sweetly] We all need to make sacrifices, Gordon.", gap=0.8),
]
