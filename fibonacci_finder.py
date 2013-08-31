import inflect
p = inflect.engine()
#https://pypi.python.org/pypi/inflect -> for creating the proper suffix in the final output

print """
Welcome to the Fibonacci Finder!

This program helps you find a specific 
number in the Fibonacci sequence.
1, 1, 2, 3, 5, 8, 13, 21, 34...
"""

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return (fibonacci(n-1) + fibonacci(n-2))

def get_index(index):
	try:
		index = int(index)
		fib_list = []
		
		for i in range(1, index + 1):
			fib_list.append(fibonacci(i))	

		ordinal = p.ordinal(index)
		result = fib_list[-1]
		return "The %s number in the sequence is %d." % (ordinal, result)
	except (TypeError, IndexError, ValueError, RuntimeError):
		print "Your input was not valid. Please enter a positive integer."
		index = raw_input("> ")
		return get_index(index)

print "Which number in the sequence would you like to find?"
index = raw_input("> ")

print get_index(index)

print "Thanks and goodbye!"