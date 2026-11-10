"""Part 1."""
from common import *  # noqa: F401,F403
from common import HOOK_BASE

HOOK = HOOK_BASE
HOOK_UNTIL = None

SCRIPT = [
    dict(shot="queue_M", s="M", t="Thank you for calling Customer Care, this is Maya. How can I help you today?",
         e={"M": "happy"}, p={"M": "idle"}, say="[warmly] Thank you for calling Customer Care, this is Maya. How can I help you today?"),
    dict(s="K", t="Finally! I've been on hold for forty minutes! Your stupid company charged me twice!", fx="phone",
         e={"M": "worried"}, say="[shouting angrily] Finally! I've been on hold for forty minutes! Your stupid company charged me twice!"),
    dict(s="M", t="I'm so sorry about that, ma'am. I can see the double charge. I'll refund it right now.", fx="phone_none",
         e={"M": "neutral"}, p={"M": "explain"},
         say="[politely] I'm so sorry about that, ma'am. I can see the double charge. I'll refund it right now."),
    dict(s="K", t="A refund? That's it? I want a free year of service, and I want you fired!", fx="phone",
         e={"M": "shocked"}, p={"M": "chest"}, say="[outraged] A refund? That's it? I want a free year of service, and I want you FIRED!"),
    dict(s="M", t="I can refund the charge today, but I'm not able to offer a free year.", e={"M": "calm"}, p={"M": "idle"}),
    dict(s="K", t="Then get me your manager. Now!", fx="phone", say="[screaming] Then get me your manager. NOW!"),
    dict(s="M", t="Of course. One moment, please.", e={"M": "annoyed"}, say="[sighs] Of course. One moment, please.",
         gap=0.4),
    dict(shot="queue_GM", s="M", t="Gary, the customer on line four wants a supervisor. I already refunded her double charge.",
         e={"M": "neutral", "G": "annoyed"}, p={"M": "explain", "G": "cross"}),
    dict(s="G", t="What did you do to her?", e={"G": "angry"}, p={"G": "point"}),
    dict(s="M", t="Nothing. I offered a refund. She wants a free year and she wants me fired.", e={"M": "annoyed"},
         p={"M": "shrug"}),
    dict(s="G", t="Give me the line. Let a professional handle this.", e={"G": "smug"}, p={"G": "phone"},
         prop={"G": "phone"}, say="[smugly] Give me the line. Let a professional handle this."),
    dict(s="G", t="Ma'am, I am so, so sorry. Our agent was completely out of line.", e={"G": "worried"}, cam="med",
         say="[groveling] Ma'am, I am so, SO sorry. Our agent was completely out of line."),
    dict(s="M", t="Out of line? I was polite the entire call!", e={"M": "shocked"}, p={"M": "chest"}, punch=True),
    dict(s="G", t="A free year? Absolutely. And a written apology from the agent. Of course.", e={"G": "happy"},
         say="[eagerly] A free year? Absolutely. And a written apology from the agent. Of course."),
    dict(s="K", t="And I want to hear her apologize. In person. Tomorrow morning.", fx="phone",
         say="[smugly] And I want to hear her apologize. In person. Tomorrow morning."),
    dict(s="G", t="Wonderful. We'll see you at ten.", e={"G": "happy"}, gap=0.4),
    dict(s="G", t="Congratulations, Maya. You just earned a written warning.", e={"G": "smug"}, p={"G": "point"},
         prop={"G": None}),
    dict(s="M", t="For what? Every call is recorded. Just listen to it.", e={"M": "angry"}, p={"M": "explain"}),
    dict(s="G", t="Nobody listens to recordings. The customer is always right.", e={"G": "smug"}, p={"G": "cross"},
         cam="med", say="[condescending] Nobody listens to recordings. The customer is ALWAYS right."),
    dict(s="M", t="Gary, you just gave away twelve hundred dollars.", e={"M": "annoyed"}, p={"M": "hips"}),
    dict(s="G", t="And tomorrow you apologize to her. Face to face. Or you're fired.", e={"G": "angry"}, p={"G": "point"}),
    dict(shot="queue_M", s="M", t="Fine. Then tomorrow, everyone is going to hear that call.", e={"M": "smug"}, cam="close",
         look={"M": "front"}, say="[quietly determined] Fine. Then tomorrow, everyone is going to hear that call.", gap=0.8),
]
