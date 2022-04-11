'''
Fizz and Buzz refer to any number that is a multiple of 3 and 5
if the input is a multiple of 3 it will output fizz
if the input is a multiple of 5 it will output buzz
if it is both it will output fizzbuzz

inputs:
	int: number we want to evaluate

returns:
	string: fizz, buzz, fizzbuzz, or the inputed number

'''

def fizz_buzz(i: int):
	if i % 3 == 0 and i % 5 == 0:
		return "fizzbuzz"
	elif i % 3 == 0:
		return "fizz"
	elif i % 5 == 0:
		return "buzz"
	else:
		return i

# test cases
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
