'''
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters
 will be removed from the beginning and end of the string. Otherwise, the characters specified
  in the second argument to the function will be removed from the string.

  Author: Ricardo Laborde
'''

import re,sys

#if only one argument was given, the character to remove will default to
#a white space
if len(sys.argv)<3:
    word=sys.argv[1]
    characters=' '
else:
    word=sys.argv[1]
    characters=sys.argv[2]

def stripCharacters(word,characters):
    #strip character at the beggining and end of the string
    stripRegexBeggining = re.compile(r'^%s+'%characters,re.IGNORECASE)
    stripRegexEnd = re.compile(r'%s+$'%characters,re.IGNORECASE)
    wordStripped=stripRegexBeggining.sub(r'',word)
    wordStripped = stripRegexEnd.sub(r'',wordStripped)
    print(wordStripped)

stripCharacters(word,characters)
