'''
Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.
The results should be printed to the screen.

Author: Ricardo Laborde
'''
import re,os

regexMatch = input('What pattern do you want to look for? ')

patternRegex = re.compile(r'[\w\s\d]*%s[\w\s\d]*'%(regexMatch))

lookAtCWD = input('Is the folder in the current directory:\n %s \n(Y\\N\\X)' %(str(os.getcwd())))

def lookForRegex(lookAtPath):

    if os.path.exists(lookAtPath):
        os.chdir(lookAtPath)
        for c in os.listdir(lookAtPath):
            if c.endswith(".txt"):
                fileToRead = open(c,'r')
                fileContent = fileToRead.readlines()
                print(patternRegex.findall(str(fileContent)))
    else:
        print('That folder doesn\'t exist')

try:
    if lookAtCWD == 'Y':
        currentCWD = input('Please specify the name of the folder: ')
        pathOfFolder = os.path.join(str(os.getcwd()),str(currentCWD)+'\\')
        lookForRegex(pathOfFolder)
    elif lookAtCWD == 'N':
        directoryToLookAt = input('Specify the path of the folder you want to look at: ')
        lookForRegex(directoryToLookAt)
    elif lookAtCWD == 'X':
        print('Exit')
    else:
        print('You did not enter a valid option. (Y\\N\\X)')
except ValueError:
   print('Error')
