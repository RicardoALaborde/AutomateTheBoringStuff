'''
Extend the multiclipboard program in this chapter so that it has a delete <keyword> command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.
'''

import shelve,pyperclip,sys

mcbShelf=shelve.open('mcb')

#if there are 3 arguments given, and the first argument 
#contains the word 'save', the second argument is
#the keyword we want to use to save clipboard items to the
#mcb
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
#if the first argument is the string 'delete' and has a
#keyword following it, we delete the keyword from the
#mcb
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
#we use list to copy all the keywords to the clipboard of
#the user, we use delete to delete all of the keywords in
#the mcb, and we type in a keyword to copy the keyword's
#content to the clipboard
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()


