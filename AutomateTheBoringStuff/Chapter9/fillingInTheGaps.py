'''
Write a program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on, in a single
folder and locates any gaps in the numbering (such as if
there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert
gaps into numbered files so that a new file can be added.

Author: Ricardo Laborde
'''
import os,shutil,re,sys

#get file start
filePrefix = input('Enter the file prefix: ')

#get current directory
currentDir = os.getcwd()

numberingRegex = re.compile(r'''
^(.*?) #start of filename
(\d+) #file numbering
(.*?)$ #rest of file
''',re.VERBOSE)

#initialize a counter for file numbering

def countFiles():
    count=1
    for foldername,subfolders,filenames in os.walk(currentDir):
        for filename in filenames:
            currentPath = os.path.join(foldername,filename)
            if filename.startswith(filePrefix):
                mo = numberingRegex.search(filename)
                if int(mo.group(2)) == count:
                    count+=1
                else:
                    shutil.move(filename,mo.group(1)+str(count).zfill(len(mo.group(2)))+mo.group(3))
                    count+=1

def addGap():
    #flag for identifying if a record was added
    flag=0
    for foldername,subfolders,filenames in os.walk(currentDir):
        #reverse the order of the list, so we count records from highest number to lowest
        filenames.reverse()
        for filename in filenames:
            currentPath = os.path.join(foldername,filename)
            if filename.startswith(filePrefix):
                mo = numberingRegex.search(filename)
                #we dont want any invalid arguments being passed!
                if int(mo.group(2)) < int(fileToInsert):
                    break
                #if the current file being read is equal to our second argument, we rename the file and add
                #towards the counter and we give the file a flag so we know a record has already been added
                if int(mo.group(2)) == int(fileToInsert):
                    shutil.move(filename,mo.group(1)+str(int(mo.group(2))+1).zfill(len(mo.group(2)))+mo.group(3))
                    flag=1
                else:
                    shutil.move(filename,mo.group(1)+str(int(mo.group(2))+1).zfill(len(mo.group(2)))+mo.group(3))



#if a third argument is given, we insert a new file with the numbering in
#the given integer and increase the number of the following files
if len(sys.argv) == 2:
    fileToInsert = sys.argv[1]
    try:
        int(fileToInsert)
        #pass the number of args parameter to function
        addGap()
    except:
        print('Third argument must be an integer')
else:
    countFiles()
