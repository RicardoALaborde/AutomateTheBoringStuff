'''
Say you have an encrypted PDF that you have forgotten the password to,
but you remember it was a single English word. Trying to guess your
forgotten password is quite a boring task. Instead you can write a
program that will decrypt the PDF by trying every possible English word
until it finds one that works. This is called a brute-force password attack.
Download the text file dictionary.txt from http://nostarch.com/automatestuff/.
This dictionary file contains over 44,000 English words with one word per line.

Using the file-reading skills you learned in Chapter 8, create a list of word
strings by reading this file. Then loop over each word in this list, passing it
to the decrypt() method. If this method returns the integer 0, the password was
wrong and your program should continue to the next password. If decrypt() returns
1, then your program should break out of the loop and print the hacked password.
You should try both the uppercase and lower-case form of each word. (On my laptop,
going through all 88,000 uppercase and lowercase words from the dictionary file
takes a couple of minutes. This is why you shouldn’t use a simple English word
for your passwords.)
'''

import PyPDF2,requests,sys

# english dictionary, we will delete this once we are done with it
res = requests.get('http://norvig.com/ngrams/enable1.txt')

englishDict = open('dictionary.txt','wb')

for chunk in res.iter_content(10000):
        englishDict.write(chunk)
englishDict.close()

pdfFile = open('PDFPARANOIA\\combinedminutes_encrypted.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
i=1
with open('dictionary.txt','r') as dictionary:
    for line in dictionary:
        i+=1
        sys.stdout.write("\r Line %i of 172,820" % i)
        sys.stdout.flush()
        if pdfReader.decrypt(line.rstrip('\n'))==1:
            print('\nDECRYPTED WITH PASSWORD %s'%(line))
            break

pdfFile.close()
