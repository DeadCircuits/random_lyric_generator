import random
from random_word import RandomWords
r = RandomWords()

def random_line():
    with open("random_lines.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def random_noun():
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb", minCorpusCount=1000)  
    return word


def random_verb():
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb", minCorpusCount=1000)
    return word



def random_adjective():
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb", minCorpusCount=1000)
    return word


for x in range(5):
    print(
        eval(random_line())
    )