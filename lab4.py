from math import sqrt

# In its simplest form, Euclid's algorithm starts with a pair of positive integers, and forms a new pair that consists of the smaller number and the difference between the larger and smaller numbers. The process repeats until the numbers in the pair are equal. That number then is the greatest common divisor of the original pair of integers.

# def Euclid_algorithm(number1, number2):
# 	numbers = sorted([number1, number2])
# 	if numbers[1] - numbers[0] != 0:
# 		return Euclid_algorithm(numbers[0], numbers[1] - numbers[0])
# 	else:
# 		return numbers[0]
# 		
# print Euclid_algorithm(100,10)

# To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:
# 
# 	Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
#
# 	Initially, let p equal 2, the first prime number.
#
# 	Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list (these will be 2p, 3p, 4p, etc.; the p itself should not be marked).
#
# 	Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
#
# 	When the algorithm terminates, all the numbers in the list that are not marked are prime.
# 

def Sieve_Erasthones(number, nonprimes = [1], p = 2):
	if p not in nonprimes:
		for element in range( p + 1, number + 1):
			if ( element % p == 0 and element not in nonprimes):
				nonprimes.append(element)
	if p >= sqrt(number):
		return [element for element in range(2, number + 1) if element not in nonprimes]
	return Sieve_Erasthones(number = number, nonprimes = nonprimes, p = (p + 1) )

print Sieve_Erasthones(121)

#### towers of hanoi
# empty tower, available, goal tower
# 1 game: move 1 to goal tower WIN
# 2 game: play 1 game.  Move 2 to goal tower. Play 1 game. WIN
# 3 game: play 2 game. Move 3 to goal tower.  Play 2 game.  WIN.
# 4 game: play 3 game.  Move 4 to goal tower.  Play 3 game.  WIN.

def Towers_of_Hanoi(start = [], goal = [], available = []):
	if start == [] and (goal == [] or available == []):
		return "Congrats, you win"
	if 
	start.(0,goal.pop(0))
	
	
	 
	