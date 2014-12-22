# Ex B.1.1
def union(set1, set2):
	'''Returns a set that is the union of the inputted sets.'''
	union = set([])
	for item in set1:
		union.add(item)
	for item in set2:
		union.add(item)
	return union

# Ex B.1.2
def intersection(set1, set2):
	'''Returns a set that is the intersection of the inputted sets.'''
	intersection = set([])
	for item in set1:
		for item2 in set2:
			if item == item2:
				intersection.add(item)
	return intersection

# Ex B.2
def mySum(*n): 
	'''Sums the arguments inputted.'''
	sum = 0
	for i in n:
		if type(i) is not int:
			raise TypeError('All values must be of type int.')
		if i < 0:
			raise ValueError('All values must be >= 0.')
		sum += i
	return sum

# Ex B.3
def myNewSum(*a):
	'''Sums the arguments inputted.'''
	sumlst, sumint = 0, 0
	for i in a:
			if type(i) is int:
				if i <= 0:
					raise ValueError('All values must be \
					>= 0.')
				sumint += i
			if type(i) is list:
				for x in i:
					if x <= 0:
						raise ValueError('All values \
						must be >= 0.')
					sumlst += x
			if type(i) is not int and type(i) is not list:
				raise TypeError('All values must be of type \
				int or list.')
	if sumlst > 0 and sumint > 0:
		raise TypeError('Inputted values cannot be both int and list')
	return max(sumlst, sumint)

def myOpReduce(lst, **arg):
	'''Modifies list based on inputted argument.'''
	mult = 1
	for a in arg:
		name, value = a, arg[a]
	if len(arg) == 0 :
		raise ValueError('no keyword argument')
	if len(arg) > 1:
		raise ValueError('too many keyword arguments')
	if name != 'op':
		raise ValueError('invalid keyword argument')
	if type(value) is not str:
		raise TypeError('value for keyword argument op must be a \
		string.')
	if value == '*':
		for i in lst:
			mult *= i
		return mult
	if value == '+':
		return sum(lst)
	if value == 'max':
		if len(lst) == 0:
			return 0
		else:
			return max(lst)
	else:
		raise ValueError('invalid keyword argument')


# Ex C.1
# The issue is that quit() is too drastic as it exits out of all instances of 
# python. Python will inherently return the error if dict[key1] + dict[key2] 
# does not work.

import sys
def sum_of_key_values(dict, key1, key2):
	'''Return the sum of the values in the dictionary stored at key1 and \
	key2.'''
	return dict[key1] + dict[key2]


# Ex C.2

# The issue is that you don't have to add the except part because you don't 
# want it to quit out of all instances of python. This is too drastic and 
# unnecessary. 

import sys
def sum_of_key_values(dict, key1, key2):
	'''Return the sum of the values in the dictionary stored at key1 and \
	key2.'''
	return dict[key1] + dict[key2]

# Ex C.3
# The issue is still that the except is unnecessary. Furthermore, when 
# raising an error, a message should be printed that explains the reasoning.


import sys
def sum_of_key_values(dict, key1, key2):
	'''Return the sum of the values in the dictionary stored at key1 and \
	key2.'''
	return dict[key1] + dict[key2]

# Ex C.4
# Again, the code is inefficient and unnecessary because it doesn't have 
# to use try and except or raise an error.

import sys
def sum_of_key_values(dict, key1, key2):
	'''Return the sum of the values in the dictionary stored at key1 and 
	key2.'''
	return dict[key1] + dict[key2]

# Ex C.5
# This is a syntax error. The print statement should be next to the
# raise ValueError.

import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError(print >> sys.stderr, 'n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)


# Ex C.6
# This should raise the Value Error before printing the error.

import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError(print >> sys.stderr, 'n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex C.7
# There are more errors to consider in this case. Plus,
# it should be x <= 0 because it needs to check if x = 0.
# Also it is a ValueError not a TypeError

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0:
        raise ValueError('x must be >= 0.0')
    elif type(x) is not float:
    	raise TypeError('x must be a float.')
    return (exp(x) / x)

# Ex C.8
# It can't just say Exception, it has to say what kind of error
# it is.

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0:
        raise ValueError('x must be >= 0.0')
    elif type(x) is not float:
    	raise TypeError('x must be a float.')
    return (exp(x) / x)



