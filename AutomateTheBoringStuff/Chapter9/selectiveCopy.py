'''
Write a program that walks through a folder tree and searches for files with a certain file
extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a
 new folder.

 Author: Ricardo Laborde
'''

import os,shutil,re

currentDir = os.getcwd()
lookForExtension = input('What file extension are you looking for?')
dotRegex = re.compile(r'(\.)?')
lookForExtension = dotRegex.sub('',lookForExtension)
destination = input('Where do you want to place the files?')
for foldername,subfolders,filenames in os.walk(currentDir):
    for filename in filenames:
        currentPath = os.path.join(foldername,filename)
        if filename.endswith('.'+lookForExtension):
            shutil.copy(currentPath,destination+'\\'+filename)
