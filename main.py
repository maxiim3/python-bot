import math
from random import random

data_set = {
    'greetings': {
        'trigger': [ "hello", "hi", "hey", "yo" ],
        'answer': [ "hello", "hello baby", "hey", "greetings" ]
    },
    'bye': {
        'trigger': [ "bye", "see you", "ciao" ],
        'answer': [ "see you next time", "take care" ]
    },
    'how': {
        'trigger': [ "whats up", "how are you", "how are you doing" ],
        'answer': [ "fine n you ?", "really good and you ?" ]
    }
}


def random_index(items: list):
    num = random()
    return math.floor(random() * (len(items)))


def chat_bot(message):
    if_succeed = False

    for types in data_set.values():
        if message.lower() in types[ "trigger" ]:
            output = types[ "answer" ]
            res = output[ random_index(output) ].capitalize()
            True
            return res
        else:
            pass
    if not if_succeed:
        return "sorry i didn't understand"


i = 0
while i < 5:
    console_msg = "Say something: " if i == 0 else "> "
    msg = input(console_msg)
    result = chat_bot(msg)
    print(result)
    i += 1 if result not in data_set[ "bye" ][ "answer" ] else 5
