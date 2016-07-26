'''
Disemvoweling means removing the vowels from text.
(For this challenge, the letters a, e, i, o, and u are considered vowels, and the letter y is not.)
The idea is to make text difficult but not impossible to read, for when somebody posts something so
idiotic you want people who are reading it to get extra frustrated.
To make things even harder to read, we'll remove spaces too. For example, this string:
        two drums and a cymbal fall off a cliff
can be disemvoweled to get:
        twdrmsndcymblfllffclff
We also want to keep the vowels we removed around (in their original order), which in this case is:
        ouaaaaoai
'''

import re

sentence = input('Enter a sentence to be disemvoweled. \n')

disemvoweledSentence=''
vowelStorage = {}

def toDisemvowel(words):
    global disemvoweledSentence
    global vowelStorage
    lookForVowels = re.compile(r'''
        ([aeiouAEIOU ]+)
    ''',re.VERBOSE)
    indexCount=0
    for d in words:
        if lookForVowels.search(d) == None:
            indexCount+=1
            continue
        for i in lookForVowels.search(d).group():
            indexCount+=1
            vowelStorage[indexCount] = i
    words = lookForVowels.sub('',words)
    print(words)
    disemvoweledSentence=words

toDisemvowel(sentence)
