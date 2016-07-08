#Write a function named printTable() that takes a list of lists of strings
#and displays it in a well-organized tabe with each column right-justified.
#Assume that all the inner lists will contain the same number of strings.
#Author:Ricardo Laborde
#initialize a list of lists containing same number of strings in each list
tableData=[['apples','oranges','cherries','banana'],
	   ['Alice','Bobby Tables','Carol','David'],
	   ['dogs','cats','moose','goose']]
#list for length values
lengthOfList=[]
#define function for printing table
def printTable(table):
	#get max length of string in list
	maxLength=[0]*len(table)
	#initialize counter for list of lists
	c=0
	#for each list in lists of lists
	for x in maxLength:
		#for each item inside each list
		for i in table[c]:#start with first list[0]
			#append the length of each string inside the list that is being counted
			lengthOfList.append(len(i))
		#get the max length inside the list
		maxLength[c]=max(lengthOfList)
		c+=1	
		
		#empty the lengthOfList list
		del lengthOfList[:]
	#not the prettiest solution, but it works
	m=0
	for l in range(len(table[0])):
		print(table[0][m].rjust(maxLength[0]),table[1][m].rjust(maxLength[1]),table[2][m].rjust(maxLength[2]))
		m+=1

printTable(tableData)
