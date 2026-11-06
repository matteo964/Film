"""Part 2."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 2.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    dict(shot="problem_board", s="C", t="Tick tock, Mr. Genius. The whole class is watching.",
         e={"C": "smug", "L": "neutral"}, p={"C": "cross", "L": ["write", "write2"]}, prop={"L": "chalk"},
         look={"L": "up"}, say="[mockingly] Tick tock, Mr. Genius. The whole class is watching."),
    dict(s="L", t="Integral of two t plus three. That gives t squared plus three t.", p={"L": ["write", "write2"]}),
    dict(s="C", t="Anyone can write the first line.", e={"C": "annoyed"}),
    dict(s="L", t="From one to x. So x squared plus three x minus four equals sixty six.",
         p={"L": ["write2", "write"]}),
    dict(shot="problem_CLK", s="K", t="Go Leo!", e={"K": "happy", "C": "annoyed"}, p={"K": "panic"},
         look={"K": "away", "L": None}, say="[excited] Go Leo!"),
    dict(s="C", t="Quiet!", e={"C": "angry"}, p={"C": "stop"}, say="[shouting] Quiet!"),
    dict(shot="solved_board", s="L", t="Factor it. x plus ten, times x minus seven. And x has to be positive.",
         e={"L": "calm"}, p={"L": ["write", "write2"]}, look={"L": "up", "K": None}),
    dict(s="L", t="Done. x equals seven.", e={"L": "smug"}, p={"L": "idle"}, look={"L": None}, sfx=[("ding", 0.6)]),
    dict(shot="solved_CL", s="C", t="Wrong! The answer is nine. It says so right here in my answer key.",
         e={"C": "smug", "L": "calm"}, p={"C": "paper"}, prop={"C": "paper", "L": None},
         say="[triumphant] WRONG! The answer is nine. It says so right here in my answer key."),
    dict(s="L", t="Check line three of your key.", e={"L": "calm"}, p={"L": "point"}, cam="med"),
    dict(s="C", t="Line three? What about it?", e={"C": "confused"}),
    dict(s="L", t="You divided by two. Twice.", e={"L": "smug"}, p={"L": "hips"}),
    dict(s="C", t="That's ridiculous. I never make mistakes.", e={"C": "annoyed"}, look={"C": "down"}),
    dict(s="C", t="...", tone="shocked", e={"C": "shocked"}, beat=1.4, look={"C": "down"}),
    dict(shot="solved_CLK", s="K", t="Wait. If the key is wrong, then was the final graded wrong too?",
         e={"K": "shocked", "C": "worried"}, p={"K": "chest"}, look={"C": None, "K": "away"}),
    dict(s="L", t="Question twelve. Everyone who got it right was marked wrong.", e={"L": "neutral"},
         p={"L": "explain"}),
    dict(s="K", t="I got question twelve marked wrong!", e={"K": "angry"}, p={"K": "point"},
         say="[outraged] I got question twelve marked wrong!"),
    dict(s="C", t="That's impossible. Sit down, both of you!", e={"C": "angry"}, p={"C": "stop"}, gap=0.4),
    dict(shot="solved_RC", s="R", t="Mr. Crane. I could hear you from the hallway. What is going on here?",
         e={"R": "annoyed", "C": "worried"}, p={"R": "hips", "C": "idle"}, prop={"C": None}),
    dict(s="C", t="Dr. Reyes! This student cheated on my final. I'm handling it.", e={"C": "neutral"},
         p={"C": "point"}),
    dict(s="R", t="Cheated? Leo Martinez?", e={"R": "confused"}, cam="med"),
    dict(s="R", t="The student who just won first place at the state math olympiad?", e={"R": "neutral"},
         p={"R": "cross"}),
    dict(s="C", t="The what?", e={"C": "shocked"}, cam="close", punch=True, say="[stunned] The... what?", gap=0.8),
]
