#Description: Chapter 4 Programming Challenge
##Comma Code: Write a function that takes a list value as an
#############argument and returns a string with all the items
#############separated by a comma and a space, with 'and' inserted
#############before the last item. Your function should be able to
#############work with any list value passed to it.
#Author: Ricardo Laborde

listOfValues=[]

def concatListValues(listVal):
	string=''
	for i in listOfValues:
		if listOfValues[-1]== i:
			string += 'and ' + i
		else:
			string += i + ', '
	print(string)
while True:
	addToList=input()
	if addToList == '':
		concatListValues(listOfValues)
		break
	listOfValues= listOfValues + [addToList]
