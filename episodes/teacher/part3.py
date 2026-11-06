"""Part 3."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = [HOOK_BASE[0], HOOK_BASE[1] + " Part 3.."]
HOOK_UNTIL = 8.0

SCRIPT = [
    # Überlappung mit dem Ende von Teil 2
    dict(shot="solved_RC", s="R", t="The student who just won first place at the state math olympiad?",
         e={"R": "neutral", "C": "neutral"}, p={"R": "cross", "C": "idle"}),
    dict(s="C", t="The what?", e={"C": "shocked"}, cam="close", punch=True, say="[stunned] The... what?"),
    dict(s="R", t="First place. Out of four thousand students. It was in the school newsletter.", e={"R": "annoyed"},
         p={"R": "explain"}),
    dict(s="C", t="I don't read the newsletter.", e={"C": "annoyed"}, p={"C": "cross"}),
    dict(s="R", t="Clearly. And why is there a torn test on the floor?", e={"R": "angry"}, p={"R": "point"},
         look={"R": "down"}),
    dict(shot="solved_RL", s="L", t="That's my final, Dr. Reyes. Mr. Crane gave me a zero for getting a hundred.",
         e={"L": "neutral", "R": "shocked"}, p={"L": "explain"}, look={"R": None}),
    dict(s="L", t="So I solved his hardest problem on the board. And found a mistake in his answer key.",
         p={"L": ["explain", "point"]}),
    dict(s="R", t="Let me see.", e={"R": "neutral"}, look={"R": "up"}, gap=0.6),
    dict(s="R", t="He's right. Line three divides by two twice.", e={"R": "annoyed"}, look={"R": None}, cam="med"),
    dict(shot="solved_RC", s="R", t="Mr. Crane, you marked correct answers as wrong. On the final exam.",
         e={"R": "angry", "C": "worried"}, p={"R": "point"}),
    dict(s="C", t="It's one tiny mistake!", e={"C": "worried"}, p={"C": "shrug"}),
    dict(s="R", t="On a hundred and twenty tests.", e={"R": "angry"}, p={"R": "cross"}),
    dict(s="R", t="Every single final gets regraded. Tonight. By you.", p={"R": "point"}, cam="med"),
    dict(s="C", t="Tonight? All hundred and twenty?", e={"C": "shocked"}, p={"C": "head"}, punch=True,
         say="[horrified] Tonight? All hundred and twenty?"),
    dict(s="R", t="And I believe you promised this class an apology.", e={"R": "smug"}, p={"R": "hips"}),
    dict(shot="solved_CLK", s="C", t="Leo. I'm sorry I accused you of cheating.", e={"C": "sad", "L": "calm", "K": "happy"},
         p={"C": "idle", "L": "idle", "K": "cross"}, say="[reluctantly] Leo. I'm sorry I accused you of cheating."),
    dict(s="K", t="Louder! The back row can't hear you!", e={"K": "smug"}, p={"K": "point"}, look={"K": "away"},
         say="[teasing] Louder! The back row can't hear you!"),
    dict(s="C", t="I'm sorry I accused you of cheating!", e={"C": "angry"}, p={"C": "panic"},
         say="[shouting, embarrassed] I'm SORRY I accused you of cheating!", look={"K": None}),
    dict(shot="solved_RL", s="R", t="Leo, your final is a hundred percent. And the university called.",
         e={"R": "happy", "L": "happy"}, p={"R": "explain"}),
    dict(s="R", t="They want you in their advanced math program. Starting next semester.", p={"R": "chest"}),
    dict(s="L", t="Seriously? That's amazing! Thank you, Dr. Reyes!", e={"L": "happy"}, p={"L": "panic"},
         say="[excited] Seriously? That's amazing! Thank you, Dr. Reyes!"),
    dict(s="R", t="One more thing. Until then, you'll double check Mr. Crane's answer keys.", e={"R": "smug"}),
    dict(shot="solved_RC", s="C", t="He's grading my answer keys?", e={"C": "shocked"}, p={"C": "head"},
         say="[outraged] HE'S grading MY answer keys?"),
    dict(s="R", t="Someone has to check your math.", e={"R": "smug"}, p={"R": "cross"}, cam="med"),
    dict(shot="solved_CL", s="L", t="Don't worry, Mr. Crane. Nobody gets a hundred percent on everything.",
         e={"L": "smug", "C": "sad"}, p={"L": "hips", "C": "idle"}, cam="close",
         say="[playfully] Don't worry, Mr. Crane. Nobody gets a hundred percent on everything.", gap=0.8),
]
