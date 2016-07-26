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
