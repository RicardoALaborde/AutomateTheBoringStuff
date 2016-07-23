'''

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

For example, a text file may look like this:



The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was

unaffected by these events.

The program would find these occurrences and prompt the user to replace them.



Enter an adjective:

silly

Enter a noun:

chandelier

Enter a verb:

screamed

Enter a noun:

pickup truck

The following text file would then be created:



The silly panda walked to the chandelier and then screamed. A nearby pickup

truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.

Author: Ricardo Laborde
'''

import re

fileToRead=open('madLibs.txt','r')

fileToWrite=open('madLibs_New.txt','w')

fileContent=re.findall(r'\w+|\S+|\s+',fileToRead.read())

findNoun=re.compile(r'NOUN|VERB|ADJECTIVE')

sentenceToReplace=[]

for word in fileContent:
    regSearch = findNoun.search(word)
    if regSearch != None:
        wordToinput=input("Enter a %s:"%(regSearch.group()))
        sentenceToReplace.append(wordToinput)
    else:
        sentenceToReplace.append(word)

print('.'.join(''.join(sentenceToReplace).split(' .')))
fileToWrite.write('.'.join(''.join(sentenceToReplace).split(' .')))
fileToRead.close()
fileToWrite.close()
