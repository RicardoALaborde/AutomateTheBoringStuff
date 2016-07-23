'''
Given an input, rearrange words as to imitate
typoglycemia. According to Urban Dictionary, typoglycemia is
the mind's ability to decipher a mis-spelled word if the first
 and last letters of the word are correct.

Idea by: /u/lepickle

Author: Ricardo Laborde
'''
import re
from random import shuffle

wordRegex = re.compile(r'''
        ^(\w) #first letter
        (\w+) #middle of word
        ((\w)(\W+)?)$ #last letter, include digits and other stuff
''',re.VERBOSE)

nonCharacterRegex = re.compile(r'\W')

inputString = input('What is the string? ')
letterLst = []

for word in inputString.split():
    #remove pesky non-letter characters
    if len(word.lstrip(str(nonCharacterRegex.search(word)))) > 3:
        mo = wordRegex.search(word)
        firstLetter = mo.group(1)
        middleOfWord = mo.group(2)
        lastLetter = mo.group(3)
        #check if its just a word with more than one non-letter character
        if len(middleOfWord) <2:
            print(word,end=' ')
            continue
        #append letter of middle of word to list
        for letter in middleOfWord:
            letterLst.append(letter)
        #randomly shuffle the letter order
        shuffle(letterLst)
        wordOutput = firstLetter + ''.join(letterLst)+lastLetter
        letterLst.clear()
        print(wordOutput,end=' ')
    else:
        print(word,end=' ')
