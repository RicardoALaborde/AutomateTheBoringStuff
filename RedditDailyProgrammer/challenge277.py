'''
A fraction exists of a numerator (top part) and a denominator (bottom part) as you probably all know.

Simplifying (or reducing) fractions means to make the fraction as simple as possible. Meaning that the denominator is a close to 1 as possible. This can be done by dividing the numerator and denominator by their greatest common divisor.

Most languages have by default this kind of functionality, but if you want to challenge yourself, you should go back to the basic theory and implement it yourself.
'''
import sys

if len(sys.argv) == 3:
	numerator = int(sys.argv[1])
	denominator = int(sys.argv[2])	
	try:
		while True:
			#follow Euclidean algorithm
			#the remainder of the numerator and denominator
			#is used to find the GCD until the remainder reaches 0
			division = numerator%denominator
			numerator = denominator
			denominator = division
			if division == 0:
				break
		print(int(sys.argv[1])/numerator,int(sys.argv[2])/numerator)
	except:
		print('Error')
