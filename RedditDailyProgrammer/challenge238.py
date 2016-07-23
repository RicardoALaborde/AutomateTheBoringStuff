'''
You were hired to create words for a new language. However, your boss wants these words
 to follow a strict pattern of consonants and vowels. You are bad at creating words by
  yourself, so you decide it would be best to randomly generate them.

Your task is to create a program that generates a random word given a pattern of consonants (c) and vowels (v).

~~~~~Input Description~~~~~~

Any string of the letters c and v, uppercase or lowercase.

~~~~~Output Description~~~~~

A random lowercase string of letters in which consonants (bcdfghjklmnpqrstvwxyz) occupy the given 'c' indices and vowels (aeiou) occupy the given 'v' indices.

~~~~~Sample Inputs~~~~~~

cvcvcc

CcvV

cvcvcvcvcvcvcvcvcvcv

~~~~~Sample Outputs~~~~~

litunn

ytie

poxuyusovevivikutire

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~Bonus~~~~~~~~~~~~~~

Error handling: make your program react when a user inputs a pattern that doesn't consist of only c's and v's.
When the user inputs a capital C or V, capitalize the letter in that index of the output.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Idea by: /u/boxofkangaroos
Taken from: https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

Author: Ricardo Laborde
'''

import re
from random import shuffle

vowels=['a','e','i','o','u']
consonants = 'bcdfghjklmnpqrstvwxyz'
consonantLst =[]
#lets convert this into a list because of laziness
for consonant in consonants:
    consonantLst.append(consonant)

wordToConvert = re.compile(r'''
    ^(['c','C','v','V']+)$  #I only want strings which consist of only Cs and Vs
''',re.VERBOSE)

givenWord = input()

mo = wordToConvert.search(givenWord)

#handle bonus 1, dont accept strings which have other characters
if mo != None:
    for i in mo.group():
        if i in ('c','C'):
            #shuffle the order of the list of consonants
            shuffle(consonantLst)
            #handle bonus 2, capitalize the character if it was given as a capital letter
            if i == 'C':
                print(consonantLst[0].upper(),end='')
            else:
                print(consonantLst[0],end='')
        else:
            #shuffle the order of the list of vowels
            shuffle(vowels)
            #handle bonus 2, capitalize the character if it was given as a capital letter
            if i == 'V':
                print(vowels[0].upper(),end='')
            else:
                print(vowels[0],end='')
else:
    print('Invalid input, input must consist of only \'C\' and \'V\'')
