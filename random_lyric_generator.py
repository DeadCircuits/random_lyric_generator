import random
from random_word import RandomWords
r = RandomWords()

def random_line():
    with open("random_lines.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def random_noun():
    return r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun")


def random_verb():
    return r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb")


def random_adjective():
    return r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="adjective")


print(
    eval(random_line())
)