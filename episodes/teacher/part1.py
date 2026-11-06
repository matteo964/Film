"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="final_CL", s="C", t="Leo Martinez. Stand up.", e={"C": "annoyed", "L": "neutral"},
         p={"C": "paper", "L": "idle"}, prop={"C": "paper"}, say="[coldly] Leo Martinez. Stand up."),
    dict(s="L", t="Yes, Mr. Crane?", e={"L": "confused"}),
    dict(s="C", t="You got a hundred percent on my calculus final.", p={"C": "paper"}, cam="med"),
    dict(s="L", t="Really? I studied really hard for that one.", e={"L": "happy"}, p={"L": "chest"}),
    dict(s="C", t="Nobody gets a hundred on my final. Nobody. Not in twenty years.", e={"C": "angry"},
         say="[angry] Nobody gets a hundred on my final. NOBODY. Not in twenty years."),
    dict(s="L", t="Maybe I'm the first.", e={"L": "calm"}, p={"L": "idle"}),
    dict(s="C", t="Or maybe you cheated.", e={"C": "smug"}, cam="close", say="[sarcastically] Or maybe you cheated."),
    dict(shot="final_CLK", s="K", t="He didn't cheat! He sat right next to me the whole time.",
         e={"K": "angry", "L": "worried"}, p={"K": "point", "L": "idle"}, look={"K": "away"}),
    dict(s="C", t="Nobody asked you, Kayla.", e={"C": "annoyed"}, p={"C": "stop"}),
    dict(s="C", t="So where did you get the answers? Your phone? A smartwatch?", p={"C": "point"}, look={"K": None}),
    dict(s="L", t="I don't even own a smartwatch.", e={"L": "annoyed"}, p={"L": "shrug"}),
    dict(shot="final_CL", s="C", t="Then you won't mind starting over. With a zero.", e={"C": "smug"},
         p={"C": "paper"}, sfx=[("whoosh", 1.6)], say="[smugly] Then you won't mind starting over. With a zero."),
    dict(s="L", t="Wait! You can't just give me a zero without any proof!", e={"L": "shocked"}, p={"L": "stop"},
         prop={"C": None}, punch=True),
    dict(s="C", t="My classroom. My rules.", e={"C": "smug"}, p={"C": "cross"}),
    dict(s="L", t="Then test me again. Right now. Any problem you want.", e={"L": "angry"}, p={"L": "explain"},
         cam="med"),
    dict(s="C", t="You want a test? Fine.", e={"C": "smug"}, say="[laughs] You want a test? Fine."),
    dict(shot="problem_CL", s="C", t="This is the hardest problem I've ever written. Not even my college students could solve it.",
         e={"C": "smug", "L": "neutral"}, p={"C": "explain2", "L": "idle"}),
    dict(s="C", t="If you can't solve it, the zero stays. And I report you for cheating.", p={"C": "point"}),
    dict(s="L", t="And if I solve it?", e={"L": "calm"}, p={"L": "hips"}),
    dict(s="C", t="Then I'll apologize. In front of the whole class.", e={"C": "smug"}, p={"C": "chest"}),
    dict(s="C", t="But that's not going to happen.", say="[laughs] But that's not going to happen.", cam="med"),
    dict(shot="problem_CLK", s="K", t="Leo, you don't have to do this.", e={"K": "worried", "L": "calm"},
         p={"K": "chest"}, look={"K": "away"}),
    dict(s="L", t="It's okay, Kayla. I've got this.", e={"L": "smug"}, p={"L": "idle"}, look={"K": None}),
    dict(shot="problem_CL", s="C", t="You have five minutes. Starting now.", e={"C": "smug"}, p={"C": "cross"}),
    dict(s="L", t="I won't need five.", e={"L": "smug"}, p={"L": "paper"}, prop={"L": "chalk"}, cam="close",
         say="[confidently] I won't need five.", gap=0.8),
]
