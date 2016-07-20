#Write a function named printTable() that takes a list of lists of strings
#and displays it in a well-organized tabe with each column right-justified.
#Assume that all the inner lists will contain the same number of strings.
#Author:Ricardo Laborde
#initialize a list of lists containing same number of strings in each list
'''
this would work out as follows:
take the 'l' column (0) at first, iterate through all the column(0)
in every list inside the list of lists, adjusting it to the max length of each
column inside each respective list. Print a blank space at the end of the iteration,
print a new line and then restart the 'm' counter which will give each list their
respective width
this works out the same as: print(table[0][0].rjust(maxLength[0])), etc...
'''
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
	m=0
	#we iterate through each column in the list
	for l in range(len(table[0])):
		#we iterate through each list in the list of lists
		for k in range(len(table)):
			#print the 'l'th item in the 'k'th column, giving each 'l' item
			#the 'm' width
			print(table[k][l].rjust(maxLength[m]),end=' ')
			m+=1
		#print a newline
		print('')
		#reset to 0
		m=0

printTable(tableData)
