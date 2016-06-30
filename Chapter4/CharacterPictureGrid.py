#Description: Second programming challenge from automatetheboringstuff.com
#Drawing a picture from a list of lists
#Author: Ricardo Laborde
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#get length of first list, as it will determine the length of every other list, the lenght would act as a guide for X coordinates
for a in range(len(grid[0])):
	#get length of the list of lists, that is, the Y coordinates
	for b in range(len(grid)):
		#print out grid[0][0] then [1][0] then [2][0], and so on
		print(grid[b][a],end='')
	print(end='\n')
