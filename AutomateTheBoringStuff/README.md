#AUTOMATE THE BORING STUFF#

Programming Challenges from the book:

###Chapter 1: Python Basics###
  
* No challenges for this chapter
  
###Chapter 2: Flow Control###
  
1. [Quesiton 13](./Chapter2/Chapter2_Q13.py)

  Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

###Chapter 3: Functions###

1. [The Collatz Sequence](./Chapter3/CollatzChallenge.py)

  Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
  
  Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

  Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.


###Chapter 4: Lists###

1. [Comma Code](./Chapter4/CommaCode.py)

  Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
  
2. [Character Picture Grid](./Chapter4/CharacterPictureGrid.py)

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

###Chapter 5: Dictionaries and Structuring Data###

1. [Fantasy Game Inventory](./Chapter5/fantasyGameInventory.py)

  You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
  
  Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

      Inventory:
      12 arrow
      42 gold coin
      1 rope
      6 torch
      1 dagger
      Total number of items: 62

2. [List to Dictionary Function for Fantasy Game Inventory](./Chapter5/addToInventory.py)

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

###Chapter 6: Manipulating Strings###

1. [Table Printer](./Chapter6/tablePrinter.py)
  
  Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

         tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]

  Your printTable() function would print the following:

          apples Alice  dogs
         oranges   Bob  cats
        cherries Carol moose
          banana David goose

###Chapter 7: Pattern Matching with Regular Expressions###

1. [Strong Password Detection](./Chapter7/strongPasswordDetection.py)

  Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
  
2. [Regex Version of strip()](./Chapter7/regexVersionOfStrip.py)

  Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
  
###Chapter 8: Reading and Writing Files###

1. [Extending the Multiclipboard](./Chapter8/extendingMulticlipboard.py)

  Extend the multiclipboard program in this chapter so that it has a delete <keyword> command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.
  
2. [Mad Libs](./Chapter8/madLibs.py)

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
  
3. [Regex Search](./Chapter8/regexSearch.py)

  Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.
  
###Chapter 9: Organizing Files###

1. [Selective Copy](./Chapter9/selectiveCopy.py)

  Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
  
2. [Deleting Unneeded Files](./Chapter9/deletingUnneededFiles.py)

  It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.
  
  Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.
  
3. [Filling in the Gaps](./Chapter9/fillingInTheGaps.py)

  Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.
  
  As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

###Chapter 10: Debugging###

1. Debugging Coin Toss

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

###Chapter 11: Web Scraping###

1. [Command Line Emailer](./Chapter11/commandLineEmailer.py)

  Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.)
  
  This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.
  
2. [Image Site Downloader](./Chapter11/imageSiteDownloader.py)

  Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
