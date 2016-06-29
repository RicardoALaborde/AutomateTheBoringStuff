#Programming challenge #1 of Chapter 3 automatetheboringstuff.com
#Author: Ricardo Laborde

def collatz(number):
	if number % 2 ==0: #if even
		return number//2 #return division of even
	else: #if odd
		return 3*number+1 #return odd *3+1

print("Enter a Number")
try: #validate if user is entering an int
	number=int(input()) #ask user for any integer
	
	while collatz(number)!=1: #while the user input is not 1
		number = collatz(number) #pass the int through collatz function
		print(number)
	else:
		print(collatz(number)) #after running while loop, return the remaining 1
except:
	print("You did not enter an integer")
