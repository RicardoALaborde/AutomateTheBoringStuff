#AUTOMATE THE BORING STUFF#
---

####Programming Challenges from the book:####

---
CHAPTERS|LINK TO BOOK|LINK TO SOLUTIONS
--------|-----|-------
[Chapter 1](./README.md#chapter-1-python-basics)|[Link to Page](https://automatetheboringstuff.com/chapter1/)|No Projects in this Chapter
[Chapter 2](./README.md#chapter-2-flow-control)|[Link to Page](https://automatetheboringstuff.com/chapter2/)|[Solutions](./Chapter2/)
[Chapter 3](./README.md#chapter-3-functions)|[Link to Page](https://automatetheboringstuff.com/chapter3/)|[Solutions](./Chapter3/)
[Chapter 4](./README.md#chapter-4-lists)|[Link to Page](https://automatetheboringstuff.com/chapter4/)|[Solutions](./Chapter4/)
[Chapter 5](./README.md#chapter-5-dictionaries-and-structuring-data)|[Link to Page](https://automatetheboringstuff.com/chapter5/)|[Solutions](./Chapter5/)
[Chapter 6](./README.md#chapter-6-manipulating-strings)|[Link to Page](https://automatetheboringstuff.com/chapter6/)|[Solutions](./Chapter6/)
[Chapter 7](./README.md#chapter-7-pattern-matching-with-regular-expressions)|[Link to Page](https://automatetheboringstuff.com/chapter7/)|[Solutions](./Chapter7/)
[Chapter 8](./README.md#chapter-8-reading-and-writing-files)|[Link to Page](https://automatetheboringstuff.com/chapter8/)|[Solutions](./Chapter8/)
[Chapter 9](./README.md#chapter-9-organizing-files)|[Link to Page](https://automatetheboringstuff.com/chapter9/)|[Solutions](./Chapter9/)
[Chapter 10](./README.md#chapter-10-debugging)|[Link to Page](https://automatetheboringstuff.com/chapter10/)|[Solutions](./Chapter10/)
[Chapter 11](./README.md#chapter-11-web-scraping)|[Link to Page](https://automatetheboringstuff.com/chapter11/)|[Solutions](./Chapter11/)
[Chapter 12](./README.md#chapter-12-working-with-excel-spreadsheets)|[Link to Page](https://automatetheboringstuff.com/chapter12/)|[Solutions](./Chapter12/)
[Chapter 13](./README.md#chapter-13-working-with-pdf-and-word-documents)|[Link to Page](https://automatetheboringstuff.com/chapter13/)|[Solutions](./Chapter13/)
[Chapter 14](./README.md#chapter-14-working-with-csv-files-and-json-data)|[Link to Page](https://automatetheboringstuff.com/chapter14/)|[Solutions](./Chapter14/)
[Chapter 15](./README.md#chapter-15-keeping-time-scheduling-tasks-and-launching-programs)|[Link to Page](https://automatetheboringstuff.com/chapter15/)|[Solutions](./Chapter15/)
Chapter 16|[Link to Page](https://automatetheboringstuff.com/chapter16/)|Solutions to be added
Chapter 17|[Link to Page](https://automatetheboringstuff.com/chapter17/)|Solutions to be added
Chapter 18|[Link to Page](https://automatetheboringstuff.com/chapter18/)|Solutions to be added

---

###Chapter 1: Python Basics###
  
* **No challenges for this chapter**

---
  
###Chapter 2: Flow Control###
  
1. [**Quesiton 13**](./Chapter2/Chapter2_Q13.py)

  Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

---

###Chapter 3: Functions###

1. [**The Collatz Sequence**](./Chapter3/CollatzChallenge.py)

  Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
  
  Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

  Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

---

###Chapter 4: Lists###

1. [**Comma Code**](./Chapter4/CommaCode.py)

  Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
  
2. [**Character Picture Grid**](./Chapter4/CharacterPictureGrid.py)

  Say you have a list of lists where each value in the inner lists is a one-character string, like this:


    
            grid = [['.', '.', '.', '.', '.', '.'],
            
                    ['.', 'O', 'O', '.', '.', '.'],
            
                    ['O', 'O', 'O', 'O', '.', '.'],
            
                    ['O', 'O', 'O', 'O', 'O', '.'],
            
                    ['.', 'O', 'O', 'O', 'O', 'O'],
            
                    ['O', 'O', 'O', 'O', 'O', '.'],
            
                    ['O', 'O', 'O', 'O', '.', '.'],
            
                    ['.', 'O', 'O', '.', '.', '.'],
            
                    ['.', '.', '.', '.', '.', '.']]


  You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

  Copy the previous grid value, and write code that uses it to print the image.

        ..OO.OO..
        .OOOOOOO.
        .OOOOOOO.
        ..OOOOO..
        ...OOO...
        ....O....

---

###Chapter 5: Dictionaries and Structuring Data###

1. [**Fantasy Game Inventory**](./Chapter5/fantasyGameInventory.py)

  You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
  
  Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

      Inventory:
      12 arrow
      42 gold coin
      1 rope
      6 torch
      1 dagger
      Total number of items: 62

2. [**List to Dictionary Function for Fantasy Game Inventory**](./Chapter5/addToInventory.py)

  Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

      dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

  Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

        def addToInventory(inventory, addedItems):
            # your code goes here

        inv = {'gold coin': 42, 'rope': 1}
        dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
        inv = addToInventory(inv, dragonLoot)
        displayInventory(inv)

  The previous program (with your displayInventory() function from the previous project) would output the following:

        Inventory:
        45 gold coin
        1 rope
        1 ruby
        1 dagger
        Total number of items: 48

---

###Chapter 6: Manipulating Strings###

1. [**Table Printer**](./Chapter6/tablePrinter.py)
  
  Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

         tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]

  Your printTable() function would print the following:

          apples Alice  dogs
         oranges   Bob  cats
        cherries Carol moose
          banana David goose

---

###Chapter 7: Pattern Matching with Regular Expressions###

1. [**Strong Password Detection**](./Chapter7/strongPasswordDetection.py)

  Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
  
2. [**Regex Version of strip()**](./Chapter7/regexVersionOfStrip.py)

  Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
  
---
  
###Chapter 8: Reading and Writing Files###

1. [**Extending the Multiclipboard**](./Chapter8/extendingMulticlipboard.py)

  Extend the multiclipboard program in this chapter so that it has a delete <keyword> command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.
  
2. [**Mad Libs**](./Chapter8/madLibs.py)

  Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

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
  
3. [**Regex Search**](./Chapter8/regexSearch.py)

  Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.

---
  
###Chapter 9: Organizing Files###

1. [**Selective Copy**](./Chapter9/selectiveCopy.py)

  Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
  
2. [**Deleting Unneeded Files**](./Chapter9/deletingUnneededFiles.py)

  It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.
  
  Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.
  
3. [**Filling in the Gaps**](./Chapter9/fillingInTheGaps.py)

  Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.
  
  As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

---

###Chapter 10: Debugging###

1. [**Debugging Coin Toss**](./Chapter10/debuggingCoinToss.py)

  The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.

      import random
      guess = ''
      while guess not in ('heads', 'tails'):
          print('Guess the coin toss! Enter heads or tails:')
          guess = input()
      toss = random.randint(0, 1) # 0 is tails, 1 is heads
      if toss == guess:
          print('You got it!')
      else:
          print('Nope! Guess again!')
          guesss = input()
          if toss == guess:
            print('You got it!')
          else:
            print('Nope. You are really bad at this game.')

---

###Chapter 11: Web Scraping###

1. [**Command Line Emailer**](./Chapter11/commandLineEmailer.py)

  Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.)
  
  This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.
  
2. [**Image Site Downloader**](./Chapter11/imageSiteDownloader.py)

  Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then downloads all the resulting images. You could write a program that works with any photo site that has a search feature.

3. [**2048**](./Chapter11/2048.py)

  2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.

4. [**Link Verification**](./Chapter11/linkVerification.py)

  Write a program that, given the URL of a web page, will attempt to download every linked page on the page. The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
  
---

###Chapter 12: Working with Excel Spreadsheets###

1. [**Multiplication Table Maker**](./Chapter12/multiplicationTableMaker.py)

  Create a program multiplicationTable.py that takes a number N from the command line and creates an N×N multiplication table in an Excel spreadsheet. For example, when the program is run like this:

    py multiplicationTable.py 6
  
  ... it should create a spreadsheet that looks like Figure 12-11.
  
  ![Figure 12-11](https://automatetheboringstuff.com/images/000052.jpg)
  
  *Figure 12-11*
  
  Row 1 and column A should be used for labels and should be in bold.
  
2. [**Blank Row Inserter**](./Chapter12/blankRowInserter.py)

  Create a program blankRowInserter.py that takes two integers and a filename string as command line arguments. Let’s call the first integer N and the second integer M. Starting at row N, the program should insert M blank rows into the spreadsheet. For example, when the program is run like this:

    python blankRowInserter.py 3 2 myProduce.xlsx

  ... the “before” and “after” spreadsheets should look like Figure 12-12.
  
  ![Figure 12-12](https://automatetheboringstuff.com/images/000055.jpg)
  
  *Figure 12-12. Before (left) and after (right) the two blank rows are inserted at row 3*
  
  You can write this program by reading in the contents of the spreadsheet. Then, when writing out the new spreadsheet, use a for loop to copy the first N lines. For the remaining lines, add M to the row number in the output spreadsheet.

3. [**Spreadsheet Cell Inverter**](./Chapter12/spreadsheetCellInverter.py)

  Write a program to invert the row and column of the cells in the spreadsheet. For example, the value at row 5, column 3 will be at row 3, column 5 (and vice versa). This should be done for all cells in the spreadsheet. For example, the “before” and “after” spreadsheets would look something like Figure 12-13.
  
  ![Figure 12-13](https://automatetheboringstuff.com/images/000079.jpg)
  
  *Figure 12-13. The spreadsheet before (top) and after (bottom) inversion*

  You can write this program by using nested for loops to read in the spreadsheet’s data into a list of lists data structure. This data structure could have sheetData[x][y] for the cell at column x and row y. Then, when writing out the new spreadsheet, use sheetData[y][x] for the cell at column x and row y.
  
4. [**Text Files to Spreadsheet**](./Chapter12/textFilesToSpreadsheet.py)

  Write a program to read in the contents of several text files (you can make the text files yourself) and insert those contents into a spreadsheet, with one line of text per row. The lines of the first text file will be in the cells of column A, the lines of the second text file will be in the cells of column B, and so on.

  Use the readlines() File object method to return a list of strings, one string per line in the file. For the first file, output the first line to column 1, row 1. The second line should be written to column 1, row 2, and so on. The next file that is read with readlines() will be written to column 2, the next file to column 3, and so on.
  
5. [**Spreadsheet to Text Files**](./Chapter12/spreadsheetToTextFiles.py)

  Write a program that performs the tasks of the previous program in reverse order: The program should open a spreadsheet and write the cells of column A into one text file, the cells of column B into another text file, and so on.

---

###Chapter 13: Working with PDF and WORD Documents###

1. [**PDF Paranoia (Part 1 - Encrypt)**](./Chapter13/pdfParanoia_encryptFiles.py)

  Using the os.walk() function from Chapter 9, write a script that will go through every PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename. Before deleting the original file, have the program attempt to read and decrypt the file to ensure that it was encrypted correctly.
  
  [**PDF Paranoia (Part 2 - Decrypt)**](./Chapter13/pdfParanoia_decryptFiles.py)
  
  Then, write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF using a provided password. If the password is incorrect, the program should print a message to the user and continue to the next PDF.
  
2. [**Custom Invitations as Word Documents**](./Chapter13/customInvitations.py)

  Say you have a text file of guest names. This guests.txt file has one name per line, as follows:

    * Prof. Plum
    * Miss Scarlet
    * Col. Mustard
    * Al Sweigart
    * Robocop

  Write a program that would generate a Word document with custom invitations that look like Figure 13-11.

  Since Python-Docx can use only those styles that already exist in the Word document, you will have to first add these styles to a blank Word file and then open that file with Python-Docx. There should be one invitation per page in the resulting Word document, so call add_break() to add a page break after the last paragraph of each invitation. This way, you will need to open only one Word document to print all of the invitations at once.
  
  ![Figure 13-11](https://automatetheboringstuff.com/images/000053.jpg)
  
  *Figure 13-11. The Word document generated by your custom invite script*
  
  You can download a sample guests.txt file from http://nostarch.com/automatestuff/.
  
3. [**Brute-Force PDF Password Breaker**](./Chapter13/bruteForcePDF.py)

  Say you have an encrypted PDF that you have forgotten the password to, but you remember it was a single English word. Trying to guess your forgotten password is quite a boring task. Instead you can write a program that will decrypt the PDF by trying every possible English word until it finds one that works. This is called a brute-force password attack. Download the text file dictionary.txt from http://nostarch.com/automatestuff/. This dictionary file contains over 44,000 English words with one word per line.
  
  Using the file-reading skills you learned in Chapter 8, create a list of word strings by reading this file. Then loop over each word in this list, passing it to the decrypt() method. If this method returns the integer 0, the password was wrong and your program should continue to the next password. If decrypt() returns 1, then your program should break out of the loop and print the hacked password. You should try both the uppercase and lower-case form of each word. (On my laptop, going through all 88,000 uppercase and lowercase words from the dictionary file takes a couple of minutes. This is why you shouldn’t use a simple English word for your passwords.)

---

###Chapter 14: Working with CSV Files and JSON Data###

1. [**Excel-to-CSV Converter**](./Chapter14/excelToCsvConverter.py)

  Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if you had to convert hundreds of Excel files to CSVs, it would take hours of clicking. Using the openpyxl module from Chapter 12, write a program that reads all the Excel files in the current working directory and outputs them as CSV files.

  A single Excel file might contain multiple sheets; you’ll have to create one CSV file per sheet. 
  
  The filenames of the CSV files should be: 
  
      <excel filename>_<sheet title>.csv 
  
  where <excel filename> is the filename of the Excel file without the file extension (for example, 'spam_data', not 'spam_data.xlsx') and <sheet title> is the string from the Worksheet object’s title variable.

  This program will involve many nested for loops. The skeleton of the program will look something like this:

      for excelFile in os.listdir('.'):
          # Skip non-xlsx files, load the workbook object.
          for sheetName in wb.get_sheet_names():
              # Loop through every sheet in the workbook.
              sheet = wb.get_sheet_by_name(sheetName)
      
              # Create the CSV filename from the Excel filename and sheet title.
              # Create the csv.writer object for this CSV file.
      
              # Loop through every row in the sheet.
              for rowNum in range(1, sheet.get_highest_row() + 1):
                  rowData = []    # append each cell to this list
                  # Loop through each cell in the row.
                  for colNum in range(1, sheet.get_highest_column() + 1):
                      # Append each cell's data to rowData.
      
                  # Write the rowData list to the CSV file.
      
              csvFile.close()

---

###Chapter 15: Keeping Time, Scheduling Tasks, and Launching Programs###

1. [**Prettified Stopwatch**](./Chapter15/prettifiedStopwatch.py)

  Expand the stopwatch project from this chapter so that it uses the rjust() and ljust() string methods to “prettify” the output. (These methods were covered in Chapter 6.) Instead of output such as this:

      Lap #1: 3.56 (3.56)
      Lap #2: 8.63 (5.07)
      Lap #3: 17.68 (9.05)
      Lap #4: 19.11 (1.43)
  
  ... the output will look like this:

      Lap # 1:  3.56 (  3.56)
      Lap # 2:  8.63 (  5.07)
      Lap # 3: 17.68 (  9.05)
      Lap # 4: 19.11 (  1.43)
  
  Note that you will need string versions of the lapNum, lapTime, and totalTime integer and float variables in order to call the string methods on them.

  Next, use the pyperclip module introduced in Chapter 6 to copy the text output to the clipboard so the user can quickly paste the output to a text file or email.
  
2. [**Scheduled Web Comic Downloader**](./Chapter15/scheduledWebDownloader.py)

  Write a program that checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit. Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X, and cron on Linux) can run your Python program once a day. The Python program itself can download the comic and then copy it to your desktop so that it is easy to find. This will free you from having to check the website yourself to see whether it has updated. (A list of web comics is available at http://nostarch.com/automatestuff/.)
