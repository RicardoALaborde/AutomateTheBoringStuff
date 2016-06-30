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


for a in range(len(grid[0])):
	for b in range(len(grid)):
		print(grid[b][a],end='')
	print(end='\n')
